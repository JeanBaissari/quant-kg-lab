#!/usr/bin/env python3
"""Merge node description chunks into a single descriptions.json and apply to graph."""
import json
import sys
import glob
import os

DESC_DIR = "/home/baissarienterprises/projects/quant-kg-lab/knowledge_graphs/scikit-learn/repo/.graphify/description-instructions"
GRAPH_PATH = "/home/baissarienterprises/projects/quant-kg-lab/knowledge_graphs/scikit-learn/repo/.graphify/graph.json"

def merge_chunks():
    """Merge all descriptions_chunk_*.json files into one dict."""
    merged = {}
    pattern = os.path.join(DESC_DIR, "descriptions_chunk_*.json")
    files = sorted(glob.glob(pattern))
    
    if not files:
        print("ERROR: No description chunk files found.")
        print(f"Looked for: {pattern}")
        return None
    
    for f in files:
        with open(f) as fh:
            chunk = json.load(fh)
        merged.update(chunk)
        print(f"  {os.path.basename(f)}: {len(chunk)} descriptions")
    
    print(f"\nTotal merged: {len(merged)} descriptions from {len(files)} chunks")
    return merged

def apply_to_graph(descriptions: dict):
    """Apply descriptions to graph nodes."""
    with open(GRAPH_PATH) as f:
        graph = json.load(f)
    
    nodes = graph.get("nodes", [])
    updated = 0
    for node in nodes:
        nid = node.get("id", "")
        if nid in descriptions:
            node["description"] = descriptions[nid]
            updated += 1
    
    # Write updated graph
    backup = GRAPH_PATH + ".backup"
    os.rename(GRAPH_PATH, backup)
    with open(GRAPH_PATH, "w") as f:
        json.dump(graph, f, indent=2)
    
    print(f"\nApplied descriptions to {updated}/{len(nodes)} nodes")
    print(f"Backup saved to {backup}")
    return updated

if __name__ == "__main__":
    print("=== Merging description chunks ===")
    merged = merge_chunks()
    if merged is None:
        sys.exit(1)
    
    print("\n=== Applying to graph ===")
    apply_to_graph(merged)
    
    print("\n=== Done ===")
    print("Next: run 'graphify cluster-only .' to regenerate studio with descriptions")
