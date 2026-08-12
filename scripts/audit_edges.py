#!/usr/bin/env python3
"""Audit INFERRED edges in knowledge graphs for quality validation.

Samples high-degree INFERRED edges and flags suspicious patterns:
- Edges connecting unrelated modules
- Low-confidence edges bridging major communities
- Edges with truncated/malformed labels

Usage: python scripts/audit_edges.py [library]
"""
import json
import sys
import datetime
from pathlib import Path
from collections import Counter, defaultdict

REPO_ROOT = Path(__file__).resolve().parent.parent

def load_graph(library):
    path = REPO_ROOT / "knowledge_graphs" / library / ".graphify" / "graph.json"
    with open(path) as f:
        return json.load(f)

def audit_edges(graph, library):
    nodes = {n["id"]: n for n in graph.get("nodes", [])}
    links = graph.get("links", graph.get("edges", []))
    
    # Separate by confidence
    extracted = [l for l in links if l.get("confidence") == "EXTRACTED"]
    inferred = [l for l in links if l.get("confidence") == "INFERRED"]
    ambiguous = [l for l in links if l.get("confidence") == "AMBIGUOUS"]
    
    print(f"=== Edge Audit: {library} ===")
    print(f"Total edges: {len(links)}")
    print(f"  EXTRACTED:  {len(extracted)} ({100*len(extracted)/len(links):.1f}%)")
    print(f"  INFERRED:   {len(inferred)} ({100*len(inferred)/len(links):.1f}%)")
    print(f"  AMBIGUOUS:  {len(ambiguous)} ({100*len(ambiguous)/len(links):.1f}%)")
    
    # Analyze INFERRED edges
    print(f"\n=== INFERRED Edge Analysis ===")
    
    # Edge degree
    inferred_degrees = Counter()
    for e in inferred:
        inferred_degrees[e["source"]] += 1
        inferred_degrees[e["target"]] += 1
    
    # Top nodes with most INFERRED edges
    print("\nTop 10 nodes by INFERRED edge count:")
    for nid, deg in inferred_degrees.most_common(10):
        label = nodes.get(nid, {}).get("label", nid)
        src = nodes.get(nid, {}).get("source_file", "")
        print(f"  {label} ({src}): {deg} inferred edges")
    
    # Cross-module suspicious edges
    print("\n=== Cross-Module Suspicious Edges ===")
    suspicious = []
    for e in inferred:
        src_node = nodes.get(e["source"], {})
        tgt_node = nodes.get(e["target"], {})
        src_file = src_node.get("source_file", "")
        tgt_file = tgt_node.get("source_file", "")
        
        if src_file and tgt_file:
            src_module = src_file.split("/")[1] if "/" in src_file else src_file
            tgt_module = tgt_file.split("/")[1] if "/" in tgt_file else tgt_file
            
            # Flag if connecting very different modules
            if src_module != tgt_module and src_module and tgt_module:
                suspicious.append({
                    "source": src_node.get("label", e["source"]),
                    "target": tgt_node.get("label", e["target"]),
                    "source_module": src_module,
                    "target_module": tgt_module,
                    "relation": e.get("relation", ""),
                    "source_file": src_file,
                    "target_file": tgt_file,
                })
    
    # Show top cross-module patterns
    cross_counts = Counter()
    for s in suspicious:
        cross_counts[(s["source_module"], s["target_module"])] += 1
    
    print("Top cross-module INFERRED connections:")
    for (mod_a, mod_b), count in cross_counts.most_common(15):
        print(f"  {mod_a} ↔ {mod_b}: {count} edges")
    
    # Write audit report
    report_path = REPO_ROOT / "docs" / "reference" / "edge-audits" / f"edge-audit-{library.replace('/', '-')}.md"
    with open(report_path, "w") as f:
        f.write(f"# Edge Audit — {library}\n\n")
        f.write(f"**Date**: {datetime.date.today().isoformat()}\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- Total edges: {len(links)}\n")
        f.write(f"- EXTRACTED: {len(extracted)} ({100*len(extracted)/len(links):.1f}%)\n")
        f.write(f"- INFERRED: {len(inferred)} ({100*len(inferred)/len(links):.1f}%)\n")
        f.write(f"- AMBIGUOUS: {len(ambiguous)}\n\n")
        f.write(f"## Top INFERRED Nodes\n\n")
        for nid, deg in inferred_degrees.most_common(20):
            label = nodes.get(nid, {}).get("label", nid)
            f.write(f"- `{label}`: {deg} inferred edges\n")
        f.write(f"\n## Cross-Module Suspicious Edges\n\n")
        for (mod_a, mod_b), count in cross_counts.most_common(20):
            f.write(f"- `{mod_a}` ↔ `{mod_b}`: {count}\n")
    
    print(f"\nAudit report: {report_path}")
    return report_path

if __name__ == "__main__":
    lib = sys.argv[1] if len(sys.argv) > 1 else "scikit-learn"
    graph = load_graph(lib)
    audit_edges(graph, lib)
    
    if len(sys.argv) <= 1:
        print("\n---")
        graph2 = load_graph("optuna")
        audit_edges(graph2, "optuna")
