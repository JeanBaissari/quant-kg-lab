#!/usr/bin/env python3
"""Restamp graph metadata to graph truth (QKG_068).

For every library in graphs.lock:
  1. topology_signature: replace the leading `n=<N>;e=<E>` with the actual
     node/edge counts, leaving the <feature-hints> tail byte-identical
     (graphify's change-detection blob — its edge-triple order is internal
     and not reproducible, so only the prefix is restamped).
  2. graph.community_labels + .graphify_labels.json: drop STALE keys (keys
     whose community has no retained nodes) so label-map == distinct IDs.
  3. Prints the new counts for the summary.

GRAPH_SPEC §7 (QKG_068 amendment): community_count = distinct NON-NULL
community IDs among retained nodes; label maps must be a bijection with
retained communities.

Usage:
  python3 scripts/restamp_graphs.py          # dry-run
  python3 scripts/restamp_graphs.py --apply  # write
"""
import sys, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOCK = json.load(open(ROOT / "graphs.lock"))["libraries"]


def restamp(lib):
    gdir = ROOT / "knowledge_graphs" / lib / ".graphify"
    gpath = gdir / "graph.json"
    if not gpath.exists():
        return None
    g = json.load(open(gpath))
    nodes, links = g.get("nodes", []), g.get("links", [])
    n, e = len(nodes), len(links)
    # 1. topology_signature prefix — signature is "n=<N>;e=<E>;<feature-hints>".
    #    Split off BOTH n= and e= segments; keep only the hints tail byte-identical
    #    (graphify's change-detection blob — its edge-triple order is internal and
    #    not reproducible, so only the prefix is restamped).
    sig = g.get("topology_signature") or f"n={n};e={e};"
    tail = ""
    if ";" in sig:
        parts = sig.split(";")
        if len(parts) >= 3:
            tail = ";".join(parts[2:])
    new_sig = f"n={n};e={e};{tail}" if tail else f"n={n};e={e}"
    # 2. label-map: drop stale keys (no retained node references that community)
    labels = g.get("graph", {}).get("community_labels") or {}
    used = {nd.get("community") for nd in nodes if nd.get("community") is not None}
    kept = {k: v for k, v in labels.items() if int(k) in used}
    return g, new_sig, kept, n, e


def main():
    apply = "--apply" in sys.argv[1:]
    changed = 0
    for lib in sorted(LOCK):
        gdir = ROOT / "knowledge_graphs" / lib / ".graphify"
        gpath = gdir / "graph.json"
        res = restamp(lib)
        if not res:
            continue
        g, new_sig, kept, n, e = res
        old_sig = g.get("topology_signature", "")
        labels = g.get("graph", {}).get("community_labels") or {}
        sig_changed = old_sig.split(";", 1)[0] != new_sig.split(";", 1)[0]
        map_changed = len(kept) != len(labels)
        if not (sig_changed or map_changed):
            continue
        print(f"{lib}: n={n} e={e} communities={len(kept)} "
              f"{'sig' if sig_changed else ''}{'+map' if map_changed else ''}")
        if apply:
            g["topology_signature"] = new_sig
            g["graph"]["community_labels"] = kept
            json.dump(g, open(gpath, "w"), indent=2)
            lpath = gdir / ".graphify_labels.json"
            if lpath.exists():
                lmap = json.load(open(lpath))
                lmap = {k: v for k, v in lmap.items() if k in kept}
                json.dump(lmap, open(lpath, "w"), indent=2)
            changed += 1
    if apply:
        print(f"restamped {changed} graphs")
    else:
        print(f"{changed} graphs would change; re-run with --apply")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
