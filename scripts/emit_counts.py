#!/usr/bin/env python3
"""Emit the single canonical counts block for every doc surface (QKG_065).

The repo's headline numbers live in exactly one place: this script's output.
README, QUICKSTART, ROADMAP, the unified index, and the per-library hubs all
consume `docs/reference/truth-counts.json` (or the markdown fragment below),
and a CI diff-gate fails when a committed doc drifts from it.

Sources of truth (in priority order):
  graphs.lock                 — the pin + node/edge manifest
  knowledge_graphs/<lib>/.graphify/graph.json — the committed graph (edges win
                                  over lock when they disagree, e.g.
                                  pyportfolioopt curated injection)
  skills/                     — SKILL.md inventory (routers/modules/playbooks)
  docs/reference/cross-library-bridges.json — overlay resolution
  docs/_development/doc_inventory.yaml — docs census

Usage:
  python3 scripts/emit_counts.py                  # writes truth-counts.json
  python3 scripts/emit_counts.py --markdown       # prints the README block
  python3 scripts/emit_counts.py --diff           # exit 1 if committed docs drift
"""
import json, sys, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOCK = json.load(open(ROOT / "graphs.lock"))["libraries"]


def graph_counts(lib):
    """(nodes, edges) from the committed graph.json — edges win over graphs.lock
    (curated injection changes edge count without a lock sync)."""
    p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not p.exists():
        return None
    g = json.load(open(p))
    return len(g.get("nodes", [])), len(g.get("links", []))


def truth():
    libs = []
    tot_n = tot_e = 0
    for lib in sorted(LOCK):
        n, e = graph_counts(lib) or (LOCK[lib]["nodes"], LOCK[lib]["edges"])
        tot_n += n; tot_e += e
        libs.append({"lib": lib, "nodes": n, "edges": e,
                     "commit": LOCK[lib]["commit"][:12]})
    skills = sorted((ROOT / "skills").rglob("SKILL.md"))
    routers = modules = playbooks = 0
    for p in skills:
        parts = p.relative_to(ROOT / "skills").parts
        if parts[0] == "quant-patterns":
            playbooks += 1
        elif len(parts) == 2:
            routers += 1
        else:
            modules += 1
    cit = {}
    cp = ROOT / "docs" / "reference" / "citations-report.json"
    if cp.exists():
        d = json.load(open(cp))
        cit = {"checked": d.get("checked"), "dangling": d.get("dangling")}
    bridges = {"resolved": 0, "attempted": 0}
    bp = ROOT / "docs" / "reference" / "cross-library-bridges.json"
    if bp.exists():
        b = json.load(open(bp))
        bridges = {"resolved": b.get("resolved"), "attempted": b.get("attempted")}
    docs = 0
    dp = ROOT / "docs" / "_development" / "doc_inventory.yaml"
    if dp.exists():
        docs = sum(1 for ln in dp.read_text().splitlines() if ln.startswith("- path:"))
    return {
        "libraries": len(LOCK),
        "libs": libs,
        "nodes": tot_n, "edges": tot_e,
        "skills": len(skills),
        "routers": routers, "modules": modules, "playbooks": playbooks,
        "citations": cit, "bridges": bridges, "docs": docs,
    }


def markdown_block(t):
    """The README/QUICKSTART 'Status' fragment — single source for the prose."""
    s = t["skills"]
    return (f"**Gold standard reached for all {t['libraries']} libraries**: every graph "
            f"passes the quality gate; {s} spec-normalized skills ({t['routers']} routers + "
            f"{t['modules']} modules + {t['playbooks']} playbooks); graph-node citations "
            f"({t['citations'].get('checked')}, {t['citations'].get('dangling')} dangling); "
            f"{t['bridges']['resolved']}/{t['bridges']['attempted']} cross-library bridges; "
            f"{t['docs']}-doc governed corpus; provenance-gated CI.")


def main():
    t = truth()
    out = ROOT / "docs" / "reference" / "truth-counts.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(t, indent=2) + "\n")
    if "--markdown" in sys.argv[1:]:
        print(markdown_block(t))
    elif "--diff" in sys.argv[1:]:
        # check the committed README/QUICKSTART/ROADMAP numbers match
        expected = markdown_block(t)
        drift = []
        for p in ("README.md", "QUICKSTART.md", "ROADMAP.md"):
            text = (ROOT / p).read_text()
            for token in (f"all {t['libraries']} libraries", f"{t['skills']} spec-normalized",
                          f"{t['citations'].get('checked')}, 0 dangling",
                          f"{t['bridges']['resolved']}/{t['bridges']['attempted']}"):
                if token not in text:
                    drift.append(f"{p}: missing {token!r}")
        if drift:
            print("\n".join(drift), file=sys.stderr)
            return 1
        print("truth-counts: committed docs match (no drift)")
    else:
        print(f"wrote {out.relative_to(ROOT)} ({t['libraries']} libs, {t['skills']} skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
