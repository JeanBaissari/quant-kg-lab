#!/usr/bin/env python3
"""Validate + lint skills against docs/specs/SKILL_SPEC.md and the live library APIs.

Three independent checks (all reported; gating differs):

  LINT (gates --ci)  — frontmatter schema, unique "Use when" names, no dangling
                       references/, source_commit matches graphs.lock, routers exist,
                       required body sections (SKILL_SPEC §3), graph_hash matches the
                       committed graph.json (sha256[:16]), related_skills/composes
                       resolve against the skill registry.
  API  (gates --strict) — every claimed class/function exists in the skill's OWN
                       library module (installed) or in that library's graph node
                       labels; a symbol found nowhere is flagged as a likely
                       hallucination. Cross-library symbols no longer satisfy a claim.
  PROVENANCE (reported) — cited source files resolve to a node in graph.json.

Usage:
  python scripts/validate_skills.py                # all checks, report
  python scripts/validate_skills.py <library>      # one library
  python scripts/validate_skills.py --ci           # exit 1 on LINT errors
  python scripts/validate_skills.py --strict        # also exit 1 on API failures
  python scripts/validate_skills.py --provenance    # also run provenance (loads graphs)
  python scripts/validate_skills.py --root <dir>   # run against a different repo root
  python scripts/validate_skills.py --skills <dir> # run against a different skills tree
  python scripts/validate_skills.py --exclude-known-debt
                                                   # demote listed tools/known_debt.json
                                                   # violations to info (QKG_010/011 bridge)
  python scripts/validate_skills.py --dump-known-debt
                                                   # emit current section/hash/related
                                                   # debt as JSON on stdout (redirect to
                                                   # tools/known_debt.json)
"""
import sys, os, re, json, hashlib, datetime, importlib, pkgutil, warnings, pathlib, contextlib
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

# Required body sections for module skills (SKILL_SPEC §3). Playbooks (§7) and
# routers (§6) are exempt. Older variants are violations, not silently accepted.
REQUIRED_SECTIONS = ["Quick Reference", "Common Patterns", "Pitfalls", "Provenance"]
SECTION_VARIANTS = {"Common Pitfalls": "Pitfalls", "Graph Provenance": "Provenance"}

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
                # methods of public classes (e.g. numpy.random.Generator.integers)
                if isinstance(obj, type):
                    for m in dir(obj):
                        if m.startswith("_"):
                            continue
                        syms.setdefault(m, f"{mod.__name__}.{a}.{m}")
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


# ------------------------------------------------------------------ curated
_CURATED = {}
def curated_symbols(lib):
    """Curated-manifest labels (tools/curated/<lib>.json, ADR-0008): symbols the
    graph cannot extract (Cython/C-only/lazy-loaded) but that ARE public API.
    A claim resolving in the manifest is real — never an api_fail (QKG_050)."""
    if lib in _CURATED:
        return _CURATED[lib]
    p = REPO_ROOT / "tools" / "curated" / f"{lib}.json"
    syms = set()
    if p.exists():
        m = json.load(open(p))
        for s in m.get("symbols", []):
            lbl = s.get("label", "").rstrip("()")
            if lbl:
                syms.add(lbl)
    _CURATED[lib] = syms
    return syms


# ------------------------------------------------------------- global universe
_GLOBAL = None
def global_universe():
    """Every symbol visible anywhere in the ecosystem: all installed libraries'
    deep symbol sets + every committed graph's node labels + every curated
    manifest. Used to distinguish cross-library references (real, resolved
    elsewhere) from hallucinations (resolve nowhere) — QKG_050."""
    global _GLOBAL
    if _GLOBAL is not None:
        return _GLOBAL
    merged = set()
    for lib in LOCK:
        deep = library_symbols(lib, deep=True)
        if deep:
            merged.update(deep)
        merged.update(graph_node_labels(lib))
        merged.update(curated_symbols(lib))
    _GLOBAL = merged
    return _GLOBAL

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
    """Classes/functions/source-files claimed by a skill's QR tables.

    QKG_050: table-header-aware — rows inside parameter/alias/attribute tables
    (headers like ``Parameter``/``Alias``/``Primary``/``Attribute``) are documented
    API surface, NOT callable claims: ``n_estimators``, ``booster_`` and friends
    must not be validated as functions against the live library.
    """
    classes, functions, srcfiles = set(), set(), set()
    # Strong param-table markers (QKG_050): a table whose header names one of these
    # documents parameters/aliases/attributes, not callable API. ("Description" /
    # "Graph Node" alone do NOT mark a table — they appear in every QR table.)
    param_tables = {"parameter", "alias", "primary", "attribute", "default"}
    # Cross-library comparison tables (e.g. "| LightGBM | XGBoost |") compare API
    # surfaces; their rows are not own-library claims (QKG_050).
    lib_names = set(LOCK) | {"sklearn", "pandas", "numpy", "scipy", "xgboost",
                             "lightgbm", "optuna", "talib", "vectorbt", "backtrader"}
    in_table, header_is_param = False, False
    for line in text.split("\n"):
        if not line.lstrip().startswith("|"):
            in_table, header_is_param = False, False
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or set(cells[0]) <= set("-: "):
            continue                                     # separator row
        if not in_table:
            # first | row after non-table text = table header (unless it is a
            # separator-only row, which was skipped above)
            in_table = True
            header_is_param = (any(c.lower() in param_tables for c in cells)
                               or any(c.strip().lower() in lib_names for c in cells))
            if header_is_param:
                continue
        if header_is_param:
            continue                                     # param/alias/attribute rows
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

# ----------------------------------------------------------------- graph facts
_GINFO, _HASH = {}, {}
def graph_info(lib):
    """Cached facts about the library's committed graph.json: node/edge/community
    counts, node label set, and the graph path. None when the graph is absent."""
    if lib in _GINFO:
        return _GINFO[lib]
    g = REPO_ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not g.exists():
        _GINFO[lib] = None
        return None
    with open(g) as f:
        data = json.load(f)
    info = {
        "nodes": len(data.get("nodes", [])),
        "edges": len(data.get("links", [])),
        "communities": len(data.get("graph", {}).get("community_labels", [])),
        "labels": {n.get("label", "") for n in data.get("nodes", [])},
        "path": g,
    }
    _GINFO[lib] = info
    return info

def graph_hash_actual(lib):
    """sha256(graph.json bytes)[:16] — the reproducible hash SKILL_SPEC §2 pins."""
    if lib in _HASH:
        return _HASH[lib]
    g = REPO_ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    _HASH[lib] = hashlib.sha256(g.read_bytes()).hexdigest()[:16] if g.exists() else None
    return _HASH[lib]
def graph_node_labels(lib):
    info = graph_info(lib)
    return info["labels"] if info else set()

def in_graph_labels(labels, sym):
    """Graph node labels are function names with a trailing '()' (e.g. 'hstack()')
    or bare type names (e.g. 'ndarray'); accept either spelling."""
    return sym in labels or f"{sym}()" in labels

def collect_headers(body):
    """`## <Header>` set outside code fences — the section inventory for §3 checks."""
    headers, in_fence = set(), False
    for line in body.split("\n"):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^##\s+(\S.*?)\s*$", line)
        if m:
            headers.add(m.group(1))
    return headers

# ------------------------------------------------------------------------ main
def main():
    argv = sys.argv[1:]
    ci = strict = provenance = exclude = dump = False
    root_override = skills_override = None
    positional = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--ci": ci = True
        elif a == "--strict": strict = True
        elif a == "--provenance": provenance = True
        elif a == "--exclude-known-debt": exclude = True
        elif a == "--dump-known-debt": dump = True
        elif a in ("--root", "--skills"):
            if i + 1 >= len(argv):
                print(f"{a} requires a value", file=sys.stderr)
                sys.exit(2)
            if a == "--root": root_override = argv[i + 1]
            else: skills_override = argv[i + 1]
            i += 1
        elif a.startswith("-"):
            print(f"unknown flag: {a}", file=sys.stderr)
            sys.exit(2)
        else:
            positional.append(a)
        i += 1
    target = positional[0] if positional else None

    global REPO_ROOT, SKILLS, LOCK
    if root_override:                       # run against a different repo root
        REPO_ROOT = pathlib.Path(root_override)
        SKILLS = REPO_ROOT / "skills"
        LOCK = json.load(open(REPO_ROOT / "graphs.lock"))["libraries"]
        _SRC.clear(); _GINFO.clear(); _HASH.clear(); _SYMS.clear()
    if skills_override:                     # different skills tree (or one library dir)
        p = pathlib.Path(skills_override)
        if (p / "SKILL.md").exists():       # a library dir itself → target it
            SKILLS = p.parent
            target = target or p.name
        else:
            SKILLS = p

    debt = {}
    if exclude:                             # QKG_010/011 bridge: demote listed violations
        kd = REPO_ROOT / "tools" / "known_debt.json"
        if kd.exists():
            with open(kd) as f:
                debt = json.load(f).get("violations", {})
        else:
            print(f"WARNING: --exclude-known-debt set but {kd} not found — nothing excluded",
                  file=sys.stderr)

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
        parts = p.relative_to(SKILLS).parts
        r = {"lint": [], "api_fail": [], "api_warn": [], "meta_warn": [],
             "provenance": [], "_keys": []}
        def _lint(key, msg):
            r["lint"].append(msg); r["_keys"].append(key)

        # ---- LINT
        if fm == "ERR" or fm is None:
            _lint("frontmatter:invalid", "invalid or missing YAML frontmatter")
        else:
            for k in REQUIRED_FM:
                if not fm.get(k):
                    _lint(f"frontmatter:missing:{k}", f"missing frontmatter: {k}")
            nm = fm.get("name", "")
            if not NAME_RE.match(nm or ""):
                _lint("name:kebab", f"name not kebab-case: {nm!r}")
            if len(names.get(nm, [])) > 1:
                _lint("name:duplicate", f"duplicate name {nm!r} also in {names[nm]}")
            if not str(fm.get("description", "")).lower().startswith("use when"):
                _lint("description:trigger", "description must start with 'Use when'")
            if lib != "quant-patterns":
                if fm.get("source_commit") != LOCK.get(lib, {}).get("commit"):
                    _lint("commit:lock", "source_commit does not match graphs.lock")
        for m in re.finditer(r"\]\((references/[^)]+|scripts/[^)]+)\)", text):
            if not (p.parent / m.group(1)).exists():
                _lint("link:dangling", f"dangling link: {m.group(1)}")

        # ---- required body sections (SKILL_SPEC §3; routers §6 / playbooks §7 exempt)
        is_router = lib != "quant-patterns" and len(parts) == 2 \
            and isinstance(fm, dict) and fm.get("name") == lib
        if lib != "quant-patterns" and not is_router:
            headers = collect_headers(body)
            for req in REQUIRED_SECTIONS:
                if req in headers:
                    continue
                variant = next((v for v, canon in SECTION_VARIANTS.items()
                                if canon == req and v in headers), None)
                if variant:
                    _lint(f"section:variant:{variant}",
                          f"section variant: '{variant}' — spec requires '## {req}'")
                else:
                    _lint(f"section:missing:{req}", f"missing required section: ## {req}")

        # ---- graph_hash + graph meta (any skill carrying a `graph:` block)
        gblock = fm.get("graph") if isinstance(fm, dict) else None
        if isinstance(gblock, dict):
            info = graph_info(lib)
            claimed = str(gblock.get("graph_hash") or "")
            if info and claimed:
                actual = graph_hash_actual(lib)
                if actual and actual != claimed:
                    _lint(f"hash:stale:{actual}",
                          f"graph_hash mismatch: expected {actual} "
                          f"(sha256({info['path'].relative_to(REPO_ROOT)})[:16]), "
                          f"found {claimed}")
                for key, label in (("nodes", "nodes"), ("edges", "edges"),
                                   ("community_count", "communities")):
                    if gblock.get(key) is not None and gblock.get(key) != info[label]:
                        r["meta_warn"].append(
                            f"graph meta: {key} mismatch — graph has {info[label]}, "
                            f"skill claims {gblock.get(key)}")
            elif not info:
                r["meta_warn"].append(f"graph.json missing for {lib} — graph checks skipped")

        # ---- related_skills / composes resolve against the live skill registry
        if isinstance(fm, dict):
            for ref in fm.get("related_skills") or []:
                if ref not in names:
                    _lint(f"related:{ref}",
                          f"related_skills: '{ref}' does not resolve to any skill "
                          "in the registry")
            for ref in fm.get("composes") or []:
                if ref not in names:
                    _lint(f"composes:{ref}",
                          f"composes: '{ref}' does not resolve to any skill "
                          "in the registry")

        # ---- API (skip playbooks; graceful warn-only when library not installed)
        # Exclude cross-library bridge + provenance sections: they cite OTHER libraries
        # and internal god-nodes, not this skill's own public API.
        if lib != "quant-patterns" and len(parts) >= 3 and not dump:
            api_text = strip_sections(text, ["Cross-Library Bridges", "Provenance"])
            classes, functions, _ = extract_claims(api_text)
            own = library_symbols(lib)
            labels = graph_node_labels(lib)
            curated = curated_symbols(lib)
            if own is None and not labels and not curated:
                r["api_warn"].append(f"{lib} not installed — API check skipped")
            else:
                deep = library_symbols(lib, deep=True) or {}
                mod_ok = module_importable(lib, parts[1])
                installed = own is not None
                universe = global_universe()
                for c in sorted(classes):
                    if (own and c in own) or in_graph_labels(labels, c) or c in curated:
                        continue
                    if not installed:
                        r["api_warn"].append(
                            f"class {c}: not found (library not installed, no graph node)")
                    elif c in universe:
                        r["api_warn"].append(
                            f"class {c}: cross-library reference (resolved in another "
                            "library/graph — not a hallucination)")
                    elif c in deep:
                        r["api_warn"].append(f"class {c}: internal/private (real, not public API)")
                    elif not mod_ok:
                        r["api_warn"].append(
                            f"class {c}: module '{parts[1]}' not importable (optional dependency?)")
                    else:
                        r["api_fail"].append(
                            f"class {c}: NOT FOUND — review (renamed/removed/hallucinated)")
                for fn in sorted(functions):
                    if (own and fn in own) or in_graph_labels(labels, fn) or fn in curated:
                        continue
                    if not installed:
                        r["api_warn"].append(
                            f"func {fn}: not found (library not installed, no graph node)")
                    elif fn in universe:
                        r["api_warn"].append(
                            f"func {fn}: cross-library reference (resolved in another "
                            "library/graph — not a hallucination)")
                    elif fn in deep:
                        r["api_warn"].append(f"func {fn}: internal/private (real, not public API)")
                    elif not mod_ok:
                        r["api_warn"].append(
                            f"func {fn}: module '{parts[1]}' not importable (optional dependency?)")
                    else:
                        r["api_fail"].append(
                            f"func {fn}: NOT FOUND — review (renamed/removed/hallucinated)")

        # ---- PROVENANCE
        if provenance and lib != "quant-patterns" and not dump:
            _, _, srcfiles = extract_claims(text)
            gsrc = graph_source_files(lib)
            if gsrc:
                for sf in sorted(srcfiles):
                    if sf not in gsrc and not any(s.endswith(sf) or sf.endswith(s) for s in gsrc):
                        r["provenance"].append(f"cited source not in graph: {sf}")

        n_lint += len(r["lint"]); n_api += len(r["api_fail"]); n_prov += len(r["provenance"])
        report[rel] = r

    # ---- --dump-known-debt: emit current lint debt as JSON (all kinds — the real
    # repo currently only produces section/hash/related/composes entries)
    if dump:
        dump_out = {}
        for rel, r in sorted(report.items()):
            keys = sorted(set(r["_keys"]))
            if keys:
                dump_out[rel] = keys
        payload = {
            "generated": datetime.date.today().isoformat(),
            "note": "Known-debt allowlist for validate_skills.py --exclude-known-debt "
                    "(QKG_007 bridge). Violations listed here are demoted to info until "
                    "the QKG_010/QKG_011 authoring waves clear them. Regenerate with: "
                    "python scripts/validate_skills.py --dump-known-debt > tools/known_debt.json",
            "violations": dump_out,
        }
        json.dump(payload, sys.stdout, indent=2, sort_keys=True)
        print()
        sys.exit(0)

    # ---- --exclude-known-debt: demote listed violations to info
    n_demoted = 0
    for rel, r in report.items():
        known = debt.get(rel, [])
        kept = []
        for key, msg in zip(r["_keys"], r["lint"]):
            if key in known:
                r.setdefault("known", []).append(msg)
                n_demoted += 1
            else:
                kept.append(msg)
        r["lint"] = kept
    n_lint = sum(len(r["lint"]) for r in report.values())

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
        if flags or r["api_warn"] or r["meta_warn"] or r.get("known"):
            print(f"{status} {rel}  [{', '.join(flags) or 'warn only'}]")
            for x in r["lint"]:        print(f"     LINT  {x}")
            for x in r.get("known", []): print(f"     KNOWN {x}")
            for x in r["api_fail"]:    print(f"     API   {x}")
            for x in r["provenance"][:5]: print(f"     PROV  {x}")
    if router_errs:
        print("Router errors:")
        for e in router_errs: print(f"     LINT  {e}")

    extra = f"  demoted_known={n_demoted}" if exclude else ""
    print(f"\n=== Summary ===  lint={n_lint}  api_fail={n_api}  provenance={n_prov}{extra}")
    for r in report.values():
        r.pop("_keys", None)                # internal key bookkeeping, not part of the report
    (REPO_ROOT / "docs" / "reference").mkdir(parents=True, exist_ok=True)
    with open(REPO_ROOT / "docs" / "reference" / "skill-validation-report.json", "w") as f:
        json.dump({"report": report, "router_errors": router_errs,
                   "totals": {"lint": n_lint, "api_fail": n_api, "provenance": n_prov}},
                  f, indent=2, default=list)
    if ci and n_lint > 0:
        sys.exit(1)
    if strict and (n_lint > 0 or n_api > 0):
        sys.exit(1)

if __name__ == "__main__":
    main()
