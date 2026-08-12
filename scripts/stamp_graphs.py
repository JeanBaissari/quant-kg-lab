#!/usr/bin/env python3
"""Embed `built_from_commit` (full SHA from graphs.lock) into every graph.json.

Per GRAPH_SPEC §2 the pin lives in the graph's `graph` meta dict. Idempotent:
libraries already stamped with the correct SHA are skipped. Backup before write.
  --dry-run (default)   report what would change
  --apply               write
"""
import sys, json, shutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main():
    a = sys.argv[1:]
    apply = "--apply" in a
    lock = json.load(open(ROOT / "graphs.lock"))["libraries"]
    changed, ok = [], 0
    for lib, meta in lock.items():
        p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
        if not p.exists():
            continue
        g = json.load(open(p))
        cur = g.get("graph", {}).get("built_from_commit")
        want = meta["commit"]
        if cur == want:
            ok += 1
            continue
        g.setdefault("graph", {})["built_from_commit"] = want
        if apply:
            shutil.copy(p, str(p) + ".stamp.bak")
            json.dump(g, open(p, "w"))
        changed.append((lib, cur or "absent", want[:12]))
    print(f"stamped-ok={ok} to-change={len(changed)}")
    for lib, cur, want in changed:
        print(f"  {lib:13} {cur} -> {want}")
    if changed and not apply:
        print("dry-run; re-run with --apply to write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
