#!/usr/bin/env python3
"""Normalize every skills/**/SKILL.md to docs/specs/SKILL_SPEC.md (one template).

Deterministic structural pass (Phase 2). It does NOT rewrite prose/content — that
is the post-rebuild content pass. It DOES:

  * rebuild frontmatter to the single schema (source_commit from graphs.lock,
    graph block with real nodes/edges/community_count/graph_hash), fixed key order
  * ensure `description` starts with "Use when" (hand-authored triggers for the 14
    Gen-B skills that used noun-phrase blurbs)
  * strip dangling `## References` sections that link non-existent references/ files
  * (re)generate a proper router for every library with >=2 sub-skills; fixes the
    scikit-learn router name collision; preserves optuna's existing router body

Usage:
  python scripts/normalize_skills.py            # dry run: report only, write nothing
  python scripts/normalize_skills.py --apply    # write changes
  python scripts/normalize_skills.py --show <relpath>   # print proposed file to stdout
"""
import sys, re, json, hashlib, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
LOCK = json.load(open(ROOT / "graphs.lock"))["libraries"]

LIB_DISPLAY = {
    "numpy": "NumPy", "scipy": "SciPy", "pandas": "pandas", "scikit-learn": "scikit-learn",
    "optuna": "Optuna", "vectorbt": "vectorbt", "backtrader": "backtrader",
    "ta-lib": "TA-Lib", "xgboost": "XGBoost", "lightgbm": "LightGBM",
}
IMPORT_NAME = {"scikit-learn": "sklearn", "ta-lib": "talib"}

# Hand-authored "Use when" triggers for the skills that used noun-phrase blurbs.
DESC_OVERRIDE = {
    "backtrader-analyzers": "Use when adding performance analyzers to a backtrader strategy — SharpeRatio, DrawDown, TradeAnalyzer, TimeReturn, and other Cerebro analyzers.",
    "backtrader-core": "Use when building event-driven backtests with backtrader — Cerebro, Strategy, DataFeed, Broker, Order, and Trade.",
    "numpy-core": "Use when working with NumPy arrays — ndarray, ufuncs, broadcasting, indexing, dtypes, and array creation.",
    "numpy-linalg": "Use when doing linear algebra with NumPy — solve, eig/eigh, svd, qr, cholesky, inv, det, and norm.",
    "numpy-random": "Use when generating random numbers with NumPy — Generator, default_rng, distributions, permutation, and seeding.",
    "pandas-core": "Use when manipulating tabular data with pandas — DataFrame, Series, Index, GroupBy, merge, concat, pivot, and melt.",
    "pandas-ts": "Use when working with pandas time series — resample, rolling, expanding, ewm, shift, diff, pct_change, and DateOffset.",
    "scipy-optimize": "Use when solving optimization or root-finding problems with SciPy — minimize, curve_fit, root, linprog, milp, and differential_evolution.",
    "scipy-signal": "Use when processing signals with SciPy — filtering (butter/filtfilt), spectral analysis (welch/stft), detrending, and convolution/correlation.",
    "scipy-stats": "Use when doing statistics with SciPy — distributions, hypothesis tests (ttest/ks/mannwhitneyu), gaussian_kde, zscore, and bootstrap/permutation resampling.",
    "ta-lib-indicators": "Use when computing technical indicators with TA-Lib — SMA, EMA, RSI, MACD, BBANDS, ATR, ADX, STOCH, and 200+ others.",
    "vectorbt-core": "Use when working with vectorbt internals — Config, ArrayWrapper, Wrapping, accessors, and settings.",
    "vectorbt-portfolio": "Use when simulating portfolios with vectorbt — Portfolio.from_signals/from_orders, stats, metrics, and trades.",
    "vectorbt-signals": "Use when generating entry/exit signals with vectorbt — SignalFactory, indicator pipelines, and signal generation.",
}

_GRAPH_FACTS = {}
def graph_facts(lib):
    """Return (community_count, graph_hash) for a library; cache across calls."""
    if lib in _GRAPH_FACTS:
        return _GRAPH_FACTS[lib]
    gpath = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    cc, gh = None, None
    if gpath.exists():
        gh = hashlib.sha256(gpath.read_bytes()).hexdigest()[:16]
        data = json.load(open(gpath))
        cc = len({n.get("community") for n in data.get("nodes", []) if n.get("community") is not None})
    _GRAPH_FACTS[lib] = (cc, gh)
    return _GRAPH_FACTS[lib]

def dq(s):
    """Safely double-quote a YAML scalar."""
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'

def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return None, text
    import yaml
    return yaml.safe_load(m.group(1)) or {}, m.group(2)

def existing_tags(fm):
    if isinstance(fm.get("tags"), list):
        return fm["tags"]
    meta = fm.get("metadata") or {}
    herm = (meta.get("hermes") or {}) if isinstance(meta, dict) else {}
    return herm.get("tags") if isinstance(herm.get("tags"), list) else None

def existing_related(fm):
    if isinstance(fm.get("related_skills"), list):
        return fm["related_skills"]
    meta = fm.get("metadata") or {}
    herm = (meta.get("hermes") or {}) if isinstance(meta, dict) else {}
    return herm.get("related_skills") if isinstance(herm.get("related_skills"), list) else None

def strip_dangling_references(body):
    """Remove a `## References` section whose body links references/ files."""
    lines = body.split("\n")
    out, i, removed = [], 0, False
    while i < len(lines):
        if re.match(r"^#{1,2}\s+References\s*$", lines[i]):
            j = i + 1
            while j < len(lines) and not re.match(r"^#{1,2}\s+\S", lines[j]):
                j += 1
            section = "\n".join(lines[i:j])
            if "references/" in section:
                removed = True
                i = j
                while out and out[-1].strip() == "":
                    out.pop()
                continue
        out.append(lines[i]); i += 1
    return "\n".join(out), removed

def emit_frontmatter(lib, name, description, module=None, is_router=False, is_playbook=False,
                     tags=None, related=None, extraction_date="2026-07-29", composes=None):
    L = [f"name: {name}", f"description: {dq(description)}", "version: 0.2.0",
         "author: quant-kg-lab", "license: MIT"]
    if is_playbook:
        L.append(f"composes: [{', '.join(composes or [])}]")
    else:
        info = LOCK[lib]
        cc, gh = graph_facts(lib)
        L += [f"source_repo: {info['repo']}", f"source_commit: {info['commit']}",
              f"extraction_date: {extraction_date}", "graph:",
              f"  nodes: {info['nodes']}", f"  edges: {info['edges']}",
              f"  community_count: {cc if cc is not None else 0}",
              f"  graph_hash: {gh or 'unknown'}"]
    L.append(f"tags: [{', '.join(tags)}]" if tags else "tags: []")
    L.append(f"related_skills: [{', '.join(related)}]" if related else "related_skills: []")
    return "---\n" + "\n".join(L) + "\n---\n"

def module_dirs(lib):
    d = SKILLS / lib
    return sorted(p.name for p in d.iterdir() if p.is_dir() and (p / "SKILL.md").exists())

def build_router(lib):
    disp = LIB_DISPLAY.get(lib, lib)
    mods = module_dirs(lib)
    info = LOCK[lib]; cc, gh = graph_facts(lib)
    subnames, rows = [], []
    for mod in mods:
        fm, _ = split_frontmatter((SKILLS / lib / mod / "SKILL.md").read_text())
        sub_name = fm.get("name", f"{lib}-{mod.replace('_','-')}")
        subnames.append(sub_name)
        raw = DESC_OVERRIDE.get(sub_name, fm.get("description", "") or "")
        covers = raw.split(" — ")[0].split(". ")[0].strip()
        for pfx in ("Use when ", "working with ", "doing ", "computing ", "generating ", "processing ", "manipulating ", "solving ", "building ", "adding "):
            if covers.startswith(pfx):
                covers = covers[len(pfx):]
        imp = IMPORT_NAME.get(lib, lib)
        rows.append(f"| [{sub_name}]({mod}/SKILL.md) | `{imp}.{mod}` | {covers} |")
    fm_txt = emit_frontmatter(
        lib, name=lib,
        description=f"Use when working with {disp}. Router indexing the {len(mods)} {lib} sub-skills; load the sub-skill for the module you need.",
        is_router=True, tags=[lib], related=subnames or None,
    )
    body = [f"\n# {disp} (router)", "",
            f"Indexes the {len(mods)} spec-driven {disp} sub-skills. Load the one for the module you need.",
            "", "## Sub-skills", "| Skill | Module | Covers |", "|-------|--------|--------|",
            *rows, "", "## Provenance",
            f"- Knowledge graph: {lib}, {info['nodes']} nodes, {info['edges']} edges, {cc} communities",
            f"- Rebuild: `scripts/rebuild_graph.sh {lib}` (pinned commit {info['commit'][:12]})", ""]
    return fm_txt + "\n".join(body)

def normalize_file(path):
    """Return (new_text, notes) for a non-router skill file."""
    rel = path.relative_to(SKILLS)
    lib = rel.parts[0]
    fm, body = split_frontmatter(path.read_text())
    if fm is None:
        return None, ["no frontmatter — skipped"]
    notes = []
    name = fm.get("name")
    is_playbook = (lib == "quant-patterns")
    is_router = (len(rel.parts) == 2)  # skills/<lib>/SKILL.md

    desc = DESC_OVERRIDE.get(name, fm.get("description", ""))
    if name in DESC_OVERRIDE:
        notes.append("description → Use-when trigger")
    if not desc.lower().lstrip("\"'").startswith("use when"):
        notes.append("WARN: description still not 'Use when'")

    body2, removed = strip_dangling_references(body)
    if removed:
        notes.append("stripped dangling references/")

    module = rel.parts[1] if len(rel.parts) >= 3 else None
    if is_playbook:
        composes = existing_related(fm) or []
        fm_txt = emit_frontmatter(lib, name, desc, is_playbook=True,
                                  composes=composes, tags=existing_tags(fm),
                                  related=existing_related(fm))
    else:
        fm_txt = emit_frontmatter(lib, name, desc, module=module, is_router=is_router,
                                  tags=existing_tags(fm) or [lib] + ([module] if module else []),
                                  related=existing_related(fm),
                                  extraction_date=str(fm.get("extraction_date", "2026-07-29")))
    return fm_txt + body2, notes

# Libraries whose router we (re)generate rather than normalize in place.
ROUTER_GEN = {}  # filled in main()

def main():
    apply = "--apply" in sys.argv
    # Which libraries get a generated router (>=2 sub-skills). optuna keeps its own
    # richer router body (frontmatter normalized in the file loop); scikit-learn's
    # root is a broken duplicate so it IS regenerated.
    for lib in LIB_DISPLAY:
        if len(module_dirs(lib)) >= 2 and lib != "optuna":
            ROUTER_GEN[lib] = True

    if "--show" in sys.argv:
        target = sys.argv[sys.argv.index("--show") + 1]
        p = SKILLS / target
        parts = pathlib.Path(target).parts
        if len(parts) == 2 and parts[0] in ROUTER_GEN:
            print(build_router(parts[0])); return
        text, _ = normalize_file(p); print(text); return

    changed, warnings = [], []
    for path in sorted(SKILLS.rglob("SKILL.md")):
        rel = path.relative_to(SKILLS)
        lib = rel.parts[0]
        is_root = (len(rel.parts) == 2)
        if is_root and lib in ROUTER_GEN:
            new = build_router(lib)
            note = ["router (re)generated"]
        else:
            new, note = normalize_file(path)
            if new is None:
                warnings.append((str(rel), note)); continue
        old = path.read_text()
        if new != old:
            changed.append((str(rel), note))
            if apply:
                path.write_text(new)
        if any("WARN" in n for n in note):
            warnings.append((str(rel), note))

    # Create routers for libs that had no root file at all.
    for lib in ROUTER_GEN:
        rp = SKILLS / lib / "SKILL.md"
        if not rp.exists():
            changed.append((f"{lib}/SKILL.md", ["router created"]))
            if apply:
                rp.write_text(build_router(lib))

    mode = "APPLIED" if apply else "DRY RUN (use --apply to write)"
    print(f"=== normalize_skills — {mode} ===")
    print(f"changed: {len(changed)}")
    for rel, note in changed:
        print(f"  ~ {rel:48s} {', '.join(note)}")
    if warnings:
        print(f"\nwarnings: {len(warnings)}")
        for rel, note in warnings:
            print(f"  ! {rel:48s} {', '.join(note)}")

if __name__ == "__main__":
    main()
