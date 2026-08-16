#!/usr/bin/env python3
"""Regenerate GRAPH_REPORT.md from graph truth (QKG_068).

The committed GRAPH_REPORTs are graphify's raw-extraction output — 15/28 drift
from the committed graph.json (prune/curate happened after extraction). This
script rewrites ONLY the data-derived sections from graph.json + graphs.lock:

  ## Summary        — nodes/edges (graph truth), communities (distinct non-null),
                     Extraction % (from link confidence), Edge kinds (relation counts),
                     + Non-singleton communities line (GRAPH_SPEC §7 "report BOTH")
  ## God Nodes      — top-10 by raw degree from graph.json links
  ## Graph Freshness — commit from graphs.lock

Everything else (header date, Corpus Check, Input Scope, Surprising Connections,
Communities, Knowledge Gaps, Suggested Questions) is preserved byte-identical.

Usage:
  python3 scripts/regenerate_graph_reports.py          # dry-run
  python3 scripts/regenerate_graph_reports.py --apply  # write
"""
import sys, json, pathlib, re
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOCK = json.load(open(ROOT / "graphs.lock"))["libraries"]

NOISE = ("tests/", "/test", "test_", "asv_bench", "benchmarks/", "bench_", "examples/",
         "r-package", "apps/", "/doc/", "docs/", ".github", "conftest", "samples/")


def build(lib):
    gdir = ROOT / "knowledge_graphs" / lib / ".graphify"
    gpath = gdir / "graph.json"
    rpath = gdir / "GRAPH_REPORT.md"
    if not gpath.exists() or not rpath.exists():
        return None
    g = json.load(open(gpath))
    nodes, links = g.get("nodes", []), g.get("links", [])
    n, e = len(nodes), len(links)
    communities = {nd.get("community") for nd in nodes if nd.get("community") is not None}
    # extraction percentages from link confidence
    conf = Counter(l.get("confidence", "EXTRACTED") for l in links)
    total = max(len(links), 1)
    pct = {k: round(v * 100 / total, 1) for k, v in conf.items()}
    kinds = Counter(l.get("relation", "?") for l in links)
    deg = Counter()
    for l in links:
        deg[l["source"]] += 1
        deg[l["target"]] += 1
    labels = {nd["id"]: (nd.get("label") or nd["id"]) for nd in nodes}
    god = []
    for nid, d in deg.most_common(10):
        lbl = labels.get(nid, nid)
        sf = ""
        for nd in nodes:
            if nd["id"] == nid:
                sf = nd.get("source_file") or ""
                break
        if any(p in sf.lower() for p in NOISE):
            continue
        god.append(f"- `{lbl}` ({d})")
    commit = LOCK.get(lib, {}).get("commit", "?")
    non_singleton = sum(1 for c, cnt in Counter(
        nd.get("community") for nd in nodes if nd.get("community") is not None).items() if cnt > 1)

    text = rpath.read_text()
    # Summary block
    kinds_line = " · ".join(f"{k}: {v}" for k, v in sorted(kinds.items()))
    pct_line = " · ".join(f"{k}: {pct.get(k, 0)}%" for k in ("EXTRACTED", "INFERRED", "AMBIGUOUS") if pct.get(k))
    summary = (f"- {n} nodes · {e} edges · {len(communities)} communities detected\n"
               f"- Non-singleton communities: {non_singleton}\n"
               f"- Extraction: {pct_line}\n"
               f"- Edge kinds: {kinds_line}\n")
    text = re.sub(r"^## Summary.*?(?=^## )", "## Summary\n" + summary + "\n", text, flags=re.S | re.M)
    # God Nodes
    god_block = "## God Nodes\n\n" + "\n".join(god) + "\n\n" if god else "## God Nodes\n\n- (none)\n\n"
    text = re.sub(r"^## God Nodes.*?(?=^## )", god_block, text, flags=re.S | re.M)
    # Freshness
    text = re.sub(r"(?i)(pinned commit[^\n]*|commit[:\s]*)[0-9a-f]{7,40}",
                  lambda m: m.group(1) + commit[:12], text, count=1)
    return text, rpath


def main():
    apply = "--apply" in sys.argv[1:]
    changed = 0
    for lib in sorted(LOCK):
        res = build(lib)
        if not res:
            continue
        text, rpath = res
        if text == rpath.read_text():
            continue
        print(f"{lib}: report regenerated")
        if apply:
            rpath.write_text(text)
            changed += 1
    if apply:
        print(f"regenerated {changed} reports")
    else:
        print(f"{changed} reports would change; re-run with --apply")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
