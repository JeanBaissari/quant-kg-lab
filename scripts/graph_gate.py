#!/usr/bin/env python3
"""GRAPH_SPEC §5 quality-gate checker for library knowledge graphs (stdlib only).

Criteria (all five must PASS for a graph to be gold-standard):
  c1 real labels     .graphify_labels.json + graph.community_labels contain no
                     default "Community N" entries; real labels cover >=95% of
                     non-singleton communities.
  c2 descriptions    >=80% of retained public-API code nodes carry semantic
                     descriptions (reuses describe_nodes.public()/is_stub()).
  c3 god nodes       top-20 by degree contains no GRAPH_SPEC §6 noise symbols
                     or noise-path source files.
  c4 pin             graph.json built_from_commit == graphs.lock commit.
  c5 audited         docs/reference/edge-audits/edge-audit-<lib>.md exists.

Usage:
  python3 scripts/graph_gate.py <lib>   one library (report)
  python3 scripts/graph_gate.py --all   all 10 libraries (report)
  python3 scripts/graph_gate.py --json  machine-readable JSON on stdout
  python3 scripts/graph_gate.py --ci    exit 1 when any criterion fails

Writes docs/reference/quality-gate/gate-<lib>.md for every selected library.
Report mode always exits 0; --ci exits 1 on any FAIL.
"""
import json, re, sys, datetime
from collections import Counter
from pathlib import Path

import describe_nodes
from prune_graph import LIB_EXTRA_SYMBOLS

ROOT = describe_nodes.ROOT
# Lock-driven roster (QKG_018 F5): every graphs.lock library is gate-able —
# adding a library must never require a code edit here.
ALL = list(json.load(open(ROOT / "graphs.lock"))["libraries"])
GATE_DIR = ROOT / "docs" / "reference" / "quality-gate"
DEFAULT_LABEL = re.compile(r"^Community \d+$")
NOISE_SYM = (re.compile(r"__[Pp]yx_"), re.compile(r"JNI", re.IGNORECASE),
             re.compile(r"_safe_call"))
NOISE_TEST = re.compile(r"^(Benchmark|TestCase|TestSuite|TestRunner|TestHarness|Tests)$")


def labels_map(lib):
    p = describe_nodes.gpath(lib).parent / ".graphify_labels.json"
    if not p.exists():
        return {}
    return json.load(open(p))


def check_c1(g, labels):
    nodes = g["nodes"]
    comm = Counter(n["community"] for n in nodes)
    distinct = len(comm)
    non_single = {c for c, k in comm.items() if k > 1}

    def lab(cid):
        if str(cid) in labels:
            return labels[str(cid)]
        if cid in labels:
            return labels[cid]
        return None

    def is_default(v):
        return bool(v) and DEFAULT_LABEL.match(str(v)) is not None

    graph_lbls = g.get("graph", {}).get("community_labels", {})
    default_labels = sum(1 for v in labels.values() if is_default(v))
    default_graph = sum(1 for v in graph_lbls.values() if is_default(v))
    covered = sum(1 for c in non_single if lab(c) and not is_default(lab(c)))
    coverage = 100.0 * covered / len(non_single) if non_single else 100.0
    ok = default_labels == 0 and default_graph == 0 and coverage >= 95.0
    counts = (f"distinct={distinct} non_singleton={len(non_single)} "
              f"default_labels={default_labels} default_graph={default_graph} "
              f"coverage={coverage:.1f}%")
    return ok, counts


def check_c2(g, lib):
    pub = [n for n in g["nodes"] if describe_nodes.public(n, lib)]
    described = sum(1 for n in pub if not describe_nodes.is_stub(n.get("description")))
    pct = 100.0 * described / len(pub) if pub else 100.0
    return pct >= 80.0, f"described={described} describable={len(pub)} pct={pct:.1f}%"


def check_c3(g, deg, lib):
    # §6 "retain but demote": rank god nodes over public-API code nodes only, so
    # rationale/docstring nodes cannot dominate centrality.
    byid = {n["id"]: n for n in g["nodes"]}
    public_ids = {n["id"] for n in g["nodes"] if describe_nodes.public(n, lib)}
    top = sorted((nid for nid in public_ids), key=lambda x: -deg[x])[:20]
    hits = []
    for nid in top:
        n = byid.get(nid, {})
        lbl = n.get("label") or ""
        sf = (n.get("source_file") or "").lower()
        # ta-lib exception (§6): __pyx_pw_ indicator wrappers ARE the public API.
        if lib == "ta-lib" and describe_nodes.talib_name(lbl):
            continue
        if any(p.search(lbl) for p in NOISE_SYM) or NOISE_TEST.match(lbl) \
                or any(s in lbl for s in LIB_EXTRA_SYMBOLS.get(lib, ())) \
                or any(p in sf for p in describe_nodes.NOISE):
            hits.append(f"{nid}({lbl})")
    counts = f"top20={len(top)} noise={len(hits)}"
    if hits:
        counts += f" hits={', '.join(hits[:6])}"
    return not hits, counts


def check_c4(g, lib, lock):
    expected = lock["libraries"][lib]["commit"]
    found = g.get("built_from_commit")
    where = "top-level"
    if found is None:
        found = g.get("graph", {}).get("built_from_commit")
        where = "graph"
    return found == expected, f"expected={expected} found={found or 'absent'} ({where})"


def check_c5(lib):
    p = ROOT / "docs" / "reference" / "edge-audits" / f"edge-audit-{lib}.md"
    return p.exists(), "exists" if p.exists() else "missing"


def check_c6(lib, g):
    """API-surface coverage (GRAPH_SPEC §5.6, ADR-0008): every curated-manifest
    entry must resolve in the graph, and the committed probe report must show
    >=95% coverage when it exists. Libs without manifest/report pass trivially
    (probe pending) — enforcement is per-library opt-in."""
    labels = {n.get("label", "") for n in g["nodes"]}
    mpath = ROOT / "tools" / "curated" / f"{lib}.json"
    if not mpath.exists():
        return True, "no manifest (probe pending)"
    manifest = json.load(open(mpath))
    unresolved = []
    for s in manifest.get("symbols", []):
        lbl = s["label"]
        if lbl in labels:
            continue
        if lbl.endswith("()") and lbl[:-2] in labels:
            continue
        if not lbl.endswith("()") and f"{lbl}()" in labels:
            continue
        unresolved.append(lbl)
    ok = not unresolved
    counts = f"curated={len(manifest.get('symbols', []))} unresolved={len(unresolved)}"
    rpath = ROOT / "docs" / "reference" / "api-surface" / f"{lib}.json"
    if rpath.exists():
        data = json.load(open(rpath))
        cov = float(data.get("coverage", 0.0))
        ok = ok and cov >= 95.0
        counts += f" surface_coverage={cov:.1f}% (target 95.0%)"
    return ok, counts


def check(lib, lock):
    g, deg = describe_nodes.load(lib)
    labels = labels_map(lib)
    return {
        "c1": {"name": "real labels", **dict(zip(["ok", "counts"], check_c1(g, labels)))},
        "c2": {"name": "descriptions", **dict(zip(["ok", "counts"], check_c2(g, lib)))},
        "c3": {"name": "god nodes", **dict(zip(["ok", "counts"], check_c3(g, deg, lib)))},
        "c4": {"name": "pin", **dict(zip(["ok", "counts"], check_c4(g, lib, lock)))},
        "c5": {"name": "audited", **dict(zip(["ok", "counts"], check_c5(lib)))},
        "c6": {"name": "api surface", **dict(zip(["ok", "counts"], check_c6(lib, g)))},
    }


def write_report(lib, res):
    GATE_DIR.mkdir(parents=True, exist_ok=True)
    rows = "\n".join(
        f"| {k} {v['name']} | {'PASS' if v['ok'] else 'FAIL'} | {v['counts']} |"
        for k, v in res.items())
    body = (f"<!-- generated by scripts/graph_gate.py — do not edit; regenerate to update -->\n\n"
            f"# Quality Gate — {lib}\n\n"
            f"Graph: `knowledge_graphs/{lib}/.graphify/graph.json` · GRAPH_SPEC §5 · "
            f"generated {datetime.date.today().isoformat()}\n\n"
            f"| criterion | status | counts |\n|---|---|---|\n{rows}\n")
    (GATE_DIR / f"gate-{lib}.md").write_text(body)


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    ci = "--ci" in args
    if "--all" in args:
        libs = list(ALL)
    else:
        libs = [a for a in args if not a.startswith("--")]
        for lib in libs:
            if lib not in ALL:
                print(f"unknown library: {lib}", file=sys.stderr)
                sys.exit(2)
    if not libs:
        print(__doc__)
        sys.exit(2)
    lock = json.load(open(ROOT / "graphs.lock"))
    results = {lib: check(lib, lock) for lib in libs}
    for lib, res in results.items():
        write_report(lib, res)
    if as_json:
        doc = {"generated_by": "scripts/graph_gate.py",
               "mode": "all" if "--all" in args else "single",
               "ci": ci, "libraries": [
                   {"lib": lib, "pass": all(v["ok"] for v in res.values()),
                    "criteria": res} for lib, res in results.items()]}
        print(json.dumps(doc, indent=2))
    else:
        print(f"{'lib':13} {'c1':>3} {'c2':>3} {'c3':>3} {'c4':>3} {'c5':>3}")
        for lib, res in results.items():
            print(f"{lib:13} " + " ".join(f"{'PASS' if v['ok'] else 'FAIL':>3}"
                                          for v in res.values()))
    sys.exit(1 if (ci and any(not v["ok"] for res in results.values() for v in res.values())) else 0)


if __name__ == "__main__":
    main()
