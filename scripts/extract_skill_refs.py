#!/usr/bin/env python3
"""Extract skill reference docs from a knowledge graph community.

Usage: python scripts/extract_skill_refs.py <library> <community_label>

Example:
    python scripts/extract_skill_refs.py scikit-learn "GradientBoosting Ensemble"
    
Outputs: skills/<library>/<community_slug>/references/api.md
"""
import json
import sys
import os
import re
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def find_community_nodes(graph_path, community_labels_path, target_label):
    """Find all nodes belonging to a named community."""
    with open(graph_path) as f:
        graph = json.load(f)
    
    nodes = {n["id"]: n for n in graph.get("nodes", [])}
    links = graph.get("links", graph.get("edges", []))
    
    # Find community ID from label
    with open(community_labels_path) as f:
        labels = json.load(f)
    
    cid = None
    for k, v in labels.items():
        if v.lower() == target_label.lower():
            cid = k
            break
    
    if cid is None:
        # Fuzzy match
        for k, v in labels.items():
            if target_label.lower() in v.lower():
                cid = k
                print(f"Fuzzy matched '{target_label}' → community {k}: '{v}'")
                break
    
    if cid is None:
        print(f"ERROR: Community '{target_label}' not found in labels.")
        print(f"Available labels (first 20):")
        for k, v in list(labels.items())[:20]:
            print(f"  {k}: {v}")
        sys.exit(1)
    
    # Load analysis to get community members
    analysis_path = graph_path.parent / ".graphify_analysis.json"
    if not analysis_path.exists():
        print(f"ERROR: {analysis_path} not found. Run clustering first.")
        sys.exit(1)
    
    with open(analysis_path) as f:
        analysis = json.load(f)
    
    communities = analysis.get("communities", {})
    member_ids = communities.get(cid, communities.get(str(cid), []))
    
    print(f"Community {cid} '{target_label}': {len(member_ids)} members")
    return nodes, links, member_ids, labels.get(cid, labels.get(str(cid), target_label))

def extract_api_refs(nodes, links, member_ids):
    """Extract API reference info for community members."""
    refs = []
    seen = set()
    
    for nid in member_ids:
        if nid not in nodes:
            continue
        node = nodes[nid]
        label = node.get("label", nid)
        source = node.get("source_file", "")
        loc = node.get("source_location", "")
        desc = node.get("description", "")
        file_type = node.get("file_type", "")
        
        if file_type == "code" and source and not source.startswith("test_"):
            key = f"{label}@{source}"
            if key not in seen:
                seen.add(key)
                refs.append({
                    "label": label,
                    "source_file": source,
                    "source_location": loc,
                    "description": desc,
                })
    
    # Sort by source file
    refs.sort(key=lambda r: (r["source_file"], r["label"]))
    return refs

def generate_markdown(library, community_label, community_id, refs):
    """Generate references/api.md content."""
    lines = [
        f"# {community_label} — API Reference",
        "",
        f"Auto-extracted from {library} knowledge graph.",
        f"Community ID: {community_id}",
        f"Nodes: {len(refs)}",
        "",
        "---",
        "",
    ]
    
    current_file = None
    for r in refs:
        if r["source_file"] != current_file:
            current_file = r["source_file"]
            lines.append(f"## `{current_file}`")
            lines.append("")
        
        lines.append(f"### `{r['label']}`")
        if r["source_location"]:
            lines.append(f"**Location**: `{r['source_file']}:{r['source_location']}`")
        if r["description"]:
            lines.append(f"**Description**: {r['description']}")
        lines.append("")
    
    return "\n".join(lines)

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    
    library = sys.argv[1]
    community_label = sys.argv[2]
    community_slug = re.sub(r'[^a-z0-9]+', '-', community_label.lower()).strip('-')
    
    graph_path = REPO_ROOT / "knowledge_graphs" / library / ".graphify" / "graph.json"
    labels_path = REPO_ROOT / "knowledge_graphs" / library / ".graphify" / ".graphify_labels.json"
    
    if not graph_path.exists():
        print(f"ERROR: {graph_path} not found")
        sys.exit(1)
    
    nodes, links, member_ids, actual_label = find_community_nodes(
        graph_path, labels_path, community_label
    )
    
    refs = extract_api_refs(nodes, links, member_ids)
    print(f"Extracted {len(refs)} API references")
    
    output_dir = REPO_ROOT / "skills" / library / community_slug / "references"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "api.md"
    
    md = generate_markdown(library, actual_label, "TBD", refs)
    output_path.write_text(md)
    print(f"Written: {output_path}")

if __name__ == "__main__":
    main()
