#!/usr/bin/env python3
"""Validate + lint skills against docs/SKILL_SPEC.md and the live library APIs.

Three independent checks (all reported; gating differs):

  LINT (gates --ci)  — frontmatter schema, unique "Use when" names, no dangling
                       references/, source_commit matches graphs.lock, routers exist.
  API  (gates --strict) — every claimed class/function exists somewhere in the
                       installed quant stack; a symbol found nowhere is flagged as a
                       likely hallucination (this is the anti-hallucination guarantee).
  PROVENANCE (reported) — cited source files resolve to a node in graph.json.

Usage:
  python scripts/validate_skills.py                # all checks, report
  python scripts/validate_skills.py <library>      # one library
  python scripts/validate_skills.py --ci           # exit 1 on LINT errors
  python scripts/validate_skills.py --strict        # also exit 1 on API failures
  python scripts/validate_skills.py --provenance    # also run provenance (loads graphs)
"""
import sys, os, re, json, importlib, pkgutil, warnings, pathlib, contextlib
import yaml

@contextlib.contextmanager
def _silence():
    """Suppress stdout/stderr/warnings during noisy library imports."""
    with warnings.catch_warnings(), open(os.devnull, "w") as devnull:
        warnings.simplefilter("ignore")
        with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
            yield

SKIP_SUBMODULES = {"tests", "test", "testing", "benchmarks", "conftest", "f2py",
                   "distutils", "__main__", "setup", "_distributor_init"}

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = REPO_ROOT / "skills"
LOCK = json.load(open(REPO_ROOT / "graphs.lock"))["libraries"]
IMPORT_BASE = {"scikit-learn": "sklearn", "ta-lib": "talib"}
REQUIRED_FM = ["name", "description", "version", "license"]
NAME_RE = re.compile(r"^[a-z0-9-]+$")

# ---------------------------------------------------------------- symbol tables
_SYMS = {}
def library_symbols(lib, deep=False):
    """{leaf_name: qualname} of classes/callables in a library. Cached per (lib, deep).

    deep=False: public API only (skip underscore submodules).
    deep=True:  also crawl private (underscore) submodules, so real-but-internal base
                classes like sklearn.svm._base.BaseSVC are found (they are not
                hallucinations, just not part of the public surface).
    """
    key = (lib, deep)
    if key in _SYMS:
        return _SYMS[key]
    base = IMPORT_BASE.get(lib, lib)
    syms = {}
    with _silence():
        try:
            top = importlib.import_module(base)
        except Exception:
            _SYMS[key] = None      # not installed
            return None
        def collect(mod):
            for a in dir(mod):
                if a.startswith("_"):
                    continue
                try:
                    obj = getattr(mod, a)
                except Exception:
                    continue
                if isinstance(obj, type) or callable(obj):
                    syms.setdefault(a, f"{mod.__name__}.{a}")
        collect(top)
        def crawl(mod, depth):
            if depth == 0 or not hasattr(mod, "__path__"):
                return
            for _, sub, _ in pkgutil.iter_modules(mod.__path__, mod.__name__ + "."):
                leaf = sub.rsplit(".", 1)[-1]
                if leaf in SKIP_SUBMODULES:
                    continue
                if leaf.startswith("_") and not deep:
                    continue
                try:
                    m = importlib.import_module(sub)
                except Exception:
                    continue
                collect(m)
                crawl(m, depth - 1)
        crawl(top, 3 if deep else 2)
    _SYMS[key] = syms
    return syms

def module_importable(lib, module):
    """Can `<base>.<module_dir>` be imported? Used to downgrade misses for optional
    submodules (e.g. optuna.integration needs the optuna-integration package)."""
    base = IMPORT_BASE.get(lib, lib)
    if not module:
        return True
    with _silence():
        try:
            importlib.import_module(f"{base}.{module}")
            return True
        except Exception:
            return False

def all_installed_symbols(deep=False):
    merged = {}
    for lib in LOCK:
        s = library_symbols(lib, deep=deep)
        if s:
            for k, v in s.items():
                merged.setdefault(k, v)
    return merged

# --------------------------------------------------------------- claim extract
def strip_sections(text, headers):
    """Remove named `## <header>` sections (they cite OTHER libraries / internal nodes,
    not the skill's own public API)."""
    lines = text.split("\n")
    out, i = [], 0
    drop = {h.lower() for h in headers}
    while i < len(lines):
        m = re.match(r"^#{1,3}\s+(.+?)\s*$", lines[i])
        if m and m.group(1).lower() in drop:
            i += 1
            while i < len(lines) and not re.match(r"^#{1,3}\s+\S", lines[i]):
                i += 1
            continue
        out.append(lines[i]); i += 1
    return "\n".join(out)

def extract_claims(text):
    classes, functions, srcfiles = set(), set(), set()
    for line in text.split("\n"):                                        # table col 1 (the API column)
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or set(cells[0]) <= set("-: "):                     # skip separator rows
            continue
        m = re.match(r"`([A-Za-z_][A-Za-z0-9_.]*)`", cells[0])
        if not m:
            continue
        sym = m.group(1)
        head = sym.split(".")[0]
        leaf = sym.split(".")[-1].split("(")[0]
        if head[0].isupper():
            classes.add(head)          # qualified Class.attr → validate the class itself
        elif leaf and leaf[0].isupper():
            classes.add(leaf)
        elif leaf:
            functions.add(leaf)
    for m in re.finditer(r"`([A-Z][A-Za-z0-9]+(?:Classifier|Regressor|Encoder|Scaler|"
                         r"Imputer|Transformer|CV|Search|Split|Sampler|Pruner|Study|Trial|"
                         r"Distribution|Booster|Portfolio|Strategy|Analyzer))`", text):
        classes.add(m.group(1))
    # drop param-like tokens (single letter / C / Cs) — not classes
    classes = {c for c in classes if not re.match(r"^[A-Z][a-z]?$", c)}
    for m in re.finditer(r"`([\w./-]+\.(?:py|pyx|c))(?::L?\d+)?`", text):  # cited source files
        srcfiles.add(m.group(1))
    return classes, functions, srcfiles

# --------------------------------------------------------------------- helpers
def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return None, text
    try:
        return yaml.safe_load(m.group(1)) or {}, m.group(2)
    except Exception:
        return "ERR", m.group(2)

def skill_lib(path):
    return path.relative_to(SKILLS).parts[0]

def module_dirs(lib):
    d = SKILLS / lib
    return [p.name for p in d.iterdir() if p.is_dir() and (p / "SKILL.md").exists()] if d.exists() else []

# ------------------------------------------------------------------ provenance
_SRC = {}
def graph_source_files(lib):
    if lib in _SRC:
        return _SRC[lib]
    g = REPO_ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    _SRC[lib] = ({n.get("source_file", "") for n in json.load(open(g)).get("nodes", [])}
                 if g.exists() else set())
    return _SRC[lib]

# ------------------------------------------------------------------------ main
def main():
    argv = sys.argv[1:]
    ci = "--ci" in argv
    strict = "--strict" in argv
    provenance = "--provenance" in argv
    target = next((a for a in argv if not a.startswith("-")), None)

    names = {}
    skills = sorted(SKILLS.rglob("SKILL.md"))
    for p in skills:                                            # global uniqueness pass
        fm, _ = parse_frontmatter(p.read_text())
        if isinstance(fm, dict):
            names.setdefault(fm.get("name"), []).append(str(p.relative_to(REPO_ROOT)))

    report, n_lint, n_api, n_prov = {}, 0, 0, 0
    for p in skills:
        lib = skill_lib(p)
        if target and lib != target:
            continue
        rel = str(p.relative_to(REPO_ROOT))
        text = p.read_text()
        fm, body = parse_frontmatter(text)
        r = {"lint": [], "api_fail": [], "api_warn": [], "provenance": []}

        # ---- LINT
        if fm == "ERR" or fm is None:
            r["lint"].append("invalid or missing YAML frontmatter")
        else:
            for k in REQUIRED_FM:
                if not fm.get(k):
                    r["lint"].append(f"missing frontmatter: {k}")
            nm = fm.get("name", "")
            if not NAME_RE.match(nm or ""):
                r["lint"].append(f"name not kebab-case: {nm!r}")
            if len(names.get(nm, [])) > 1:
                r["lint"].append(f"duplicate name {nm!r} also in {names[nm]}")
            if not str(fm.get("description", "")).lower().startswith("use when"):
                r["lint"].append("description must start with 'Use when'")
            if lib != "quant-patterns":
                if fm.get("source_commit") != LOCK.get(lib, {}).get("commit"):
                    r["lint"].append("source_commit does not match graphs.lock")
        for m in re.finditer(r"\]\((references/[^)]+|scripts/[^)]+)\)", text):
            if not (p.parent / m.group(1)).exists():
                r["lint"].append(f"dangling link: {m.group(1)}")

        # ---- API (skip playbooks; skip if library not installed)
        # Exclude cross-library bridge + provenance sections: they cite OTHER libraries
        # and internal god-nodes, not this skill's own public API.
        api_text = strip_sections(text, ["Cross-Library Bridges", "Provenance"])
        classes, functions, _ = extract_claims(api_text)
        _, _, srcfiles = extract_claims(text)
        parts = p.relative_to(SKILLS).parts
        if lib != "quant-patterns" and len(parts) >= 3:
            own = library_symbols(lib)
            if own is None:
                r["api_warn"].append(f"{lib} not installed — API check skipped")
            else:
                universe = all_installed_symbols()
                # If the specific submodule won't import (optional dep), downgrade misses.
                # `integration(s)` modules document optional third-party bridges by design.
                mod_ok = module_importable(lib, parts[1]) and parts[1] not in {"integration", "integrations"}
                for c in sorted(classes):
                    if c in own or c in universe:
                        continue
                    if c in (library_symbols(lib, deep=True) or {}):
                        r["api_warn"].append(f"class {c}: internal/private (real, not public API)")
                    elif not mod_ok:
                        r["api_warn"].append(f"class {c}: module '{parts[1]}' not importable (optional dependency?)")
                    else:
                        r["api_fail"].append(f"class {c}: NOT FOUND — review (renamed/removed/hallucinated)")
                for fn in sorted(functions):
                    if fn not in own and fn not in universe:
                        r["api_warn"].append(f"func {fn}: not found in public API (cross-ref or renamed)")

        # ---- PROVENANCE
        if provenance and lib != "quant-patterns":
            gsrc = graph_source_files(lib)
            if gsrc:
                for sf in sorted(srcfiles):
                    if sf not in gsrc and not any(s.endswith(sf) or sf.endswith(s) for s in gsrc):
                        r["provenance"].append(f"cited source not in graph: {sf}")

        n_lint += len(r["lint"]); n_api += len(r["api_fail"]); n_prov += len(r["provenance"])
        report[rel] = r

    # ---- router-presence (global, not per-file)
    router_errs = []
    for lib in LOCK:
        if len(module_dirs(lib)) >= 2:
            rp = SKILLS / lib / "SKILL.md"
            fm, _ = parse_frontmatter(rp.read_text()) if rp.exists() else (None, "")
            if not rp.exists() or not isinstance(fm, dict) or fm.get("name") != lib:
                router_errs.append(f"{lib}: missing/invalid router (skills/{lib}/SKILL.md name must be '{lib}')")
    n_lint += len(router_errs)

    # ---- output
    print("=== Skill validation ===")
    for rel, r in report.items():
        flags = []
        if r["lint"]: flags.append(f"{len(r['lint'])} lint")
        if r["api_fail"]: flags.append(f"{len(r['api_fail'])} api-fail")
        if r["provenance"]: flags.append(f"{len(r['provenance'])} prov")
        status = "OK " if not (r["lint"] or r["api_fail"]) else "ERR"
        if flags or r["api_warn"]:
            print(f"{status} {rel}  [{', '.join(flags) or 'warn only'}]")
            for x in r["lint"]:        print(f"     LINT  {x}")
            for x in r["api_fail"]:    print(f"     API   {x}")
            for x in r["provenance"][:5]: print(f"     PROV  {x}")
    if router_errs:
        print("Router errors:")
        for e in router_errs: print(f"     LINT  {e}")

    print(f"\n=== Summary ===  lint={n_lint}  api_fail={n_api}  provenance={n_prov}")
    (REPO_ROOT / "docs").mkdir(exist_ok=True)
    json.dump({"report": report, "router_errors": router_errs,
               "totals": {"lint": n_lint, "api_fail": n_api, "provenance": n_prov}},
              open(REPO_ROOT / "docs" / "skill-validation-report.json", "w"),
              indent=2, default=list)
    if ci and n_lint > 0:
        sys.exit(1)
    if strict and (n_lint > 0 or n_api > 0):
        sys.exit(1)

if __name__ == "__main__":
    main()
