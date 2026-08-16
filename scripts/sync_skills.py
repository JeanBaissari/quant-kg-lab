#!/usr/bin/env python3
"""Refresh every library skill's `graph:` block against the final graph (QKG_010).

Recomputes graph_hash = sha256(graph.json bytes)[:16] and syncs nodes/edges/
community_count from the actual graph. Playbooks (name: quant-*) are exempt.
  --dry-run (default)   report would-change files
  --apply               rewrite frontmatter in place
"""
import sys, json, hashlib, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
try:
    import yaml
except ImportError:
    sys.exit("ERROR: PyYAML required")


def graph_stats(lib):
    p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not p.exists():
        return None
    g = json.load(open(p))
    h = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
    return {
        "graph_hash": h,
        "nodes": len(g["nodes"]),
        "edges": len(g["links"]),
        "community_count": len({nd.get("community") for nd in g.get("nodes", []) if nd.get("community") is not None}),  # GRAPH_SPEC §7: distinct non-null IDs (QKG_068)
    }


def lib_of(skill_path):
    parts = skill_path.relative_to(ROOT / "skills").parts
    return parts[0] if parts else None


def main():
    a = sys.argv[1:]
    apply = "--apply" in a
    changed = []
    for p in sorted((ROOT / "skills").rglob("SKILL.md")):
        if "quant-patterns" in p.parts:
            continue
        text = p.read_text()
        fm = text.split("---", 2)
        if len(fm) < 3:
            continue
        try:
            meta = yaml.safe_load(fm[1]) or {}
        except Exception:
            continue
        if meta.get("name", "").startswith("quant-"):
            continue
        g = meta.get("graph")
        if not isinstance(g, dict):
            continue
        lib = lib_of(p)
        stats = graph_stats(lib)
        if not stats:
            continue
        diffs = {k: (g.get(k), stats[k]) for k in stats if g.get(k) != stats[k]}
        if not diffs:
            continue
        changed.append((p, fm, meta, g, stats, diffs))
    print(f"skills with stale graph block: {len(changed)}")
    for p, fm, meta, g, stats, diffs in changed:
        print(f"  {str(p.relative_to(ROOT)):52} " +
              " ".join(f"{k}: {old}->{new}" for k, (old, new) in diffs.items()))
    if not changed:
        return 0
    if not apply:
        print("dry-run; re-run with --apply to write")
        return 0
    for p, fm, meta, g, stats, diffs in changed:
        g.update(stats)
        new_fm = "---\n" + yaml.safe_dump(meta, sort_keys=False, default_flow_style=False).rstrip() + "\n---"
        p.write_text(new_fm + fm[2])
    print(f"wrote {len(changed)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
