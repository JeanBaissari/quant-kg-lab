#!/usr/bin/env python3
"""Extract a references/api.md for one graph community.

Usage: python scripts/extract_skill_refs.py <lib> <community_label_or_id> [--out <dir>]

Reads knowledge_graphs/<lib>/.graphify/graph.json, resolves the community via
graph.community_labels / node.community, takes the top 20 nodes by link degree,
and writes references/api.md into the --out directory (default: stdout-adjacent
skills/<lib>/<slug>/references/ is NOT touched; --out is required in practice).

The community argument accepts a community id ("37") or a label ("Community 37").
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TOP_N = 20


def load_graph(lib):
    path = REPO_ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not path.exists():
        print(f"ERROR: {path} not found", file=sys.stderr)
        sys.exit(1)
    with open(path) as f:
        return json.load(f)


def resolve_community(graph, query):
    labels = graph.get("graph", {}).get("community_labels", {})
    if str(query) in labels:
        return str(query), labels[str(query)]
    for cid, name in labels.items():
        if name.lower() == query.lower():
            return cid, name
    for cid, name in labels.items():
        if str(query).lower() in name.lower():
            print(f"Fuzzy matched '{query}' → community {cid}: '{name}'")
            return cid, name
    print(f"ERROR: Community '{query}' not found. Available (first 20):", file=sys.stderr)
    for cid, name in list(labels.items())[:20]:
        print(f"  {cid}: {name}", file=sys.stderr)
    sys.exit(1)


def top_nodes(graph, cid):
    degrees = Counter()
    for link in graph.get("links", graph.get("edges", [])):
        degrees[link["source"]] += 1
        degrees[link["target"]] += 1
    members = [n for n in graph.get("nodes", []) if str(n.get("community")) == cid]
    return sorted(members, key=lambda n: degrees.get(n["id"], 0), reverse=True)[:TOP_N]


def generate_markdown(lib, cid, label, nodes):
    lines = [
        f"# {lib} — {label} — API Reference",
        "",
        f"Auto-extracted from the {lib} knowledge graph (community {cid}).",
        f"Top {len(nodes)} nodes by link degree.",
        "",
    ]
    for n in nodes:
        lines.append(f"### {n.get('label', n['id'])}")
        lines.append(f"- source: {n.get('source_file', '')}:{n.get('source_location', '')}")
        lines.append(f"- description: {n.get('description') or '(undescribed)'}")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lib", help="library key, e.g. optuna")
    parser.add_argument("community", help="community id or label, e.g. '37' or 'Community 37'")
    parser.add_argument("--out", required=True, help="target dir; writes <dir>/references/api.md")
    args = parser.parse_args()

    graph = load_graph(args.lib)
    cid, label = resolve_community(graph, args.community)
    nodes = top_nodes(graph, cid)
    if not nodes:
        print(f"ERROR: no nodes found in community {cid}", file=sys.stderr)
        sys.exit(1)

    out_path = Path(args.out) / "references" / "api.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(generate_markdown(args.lib, cid, label, nodes))
    print(f"Community {cid} '{label}': {len(nodes)} nodes → {out_path}")


if __name__ == "__main__":
    main()
