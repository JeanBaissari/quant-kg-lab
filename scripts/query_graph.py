#!/usr/bin/env python3
"""Query knowledge graphs using graph traversal.

Usage:
    python scripts/query_graph.py sklearn "How does Pipeline work?"
    python scripts/query_graph.py optuna "What samplers exist?"
    python scripts/query_graph.py sklearn --path "GridSearchCV" "TPESampler"
    python scripts/query_graph.py sklearn --explain "BaseEstimator"
"""
import json
import sys
from pathlib import Path
from collections import deque, Counter

REPO_ROOT = Path(__file__).resolve().parent.parent

def load_graph(library):
    path = REPO_ROOT / "knowledge_graphs" / library / ".graphify" / "graph.json"
    if not path.exists():
        print(f"ERROR: No graph for '{library}' at {path}")
        sys.exit(1)
    with open(path) as f:
        return json.load(f)

def find_nodes(graph, query):
    """Find nodes matching a query string (substring match on label)."""
    nodes = graph.get("nodes", [])
    query_lower = query.lower()
    matches = []
    for n in nodes:
        label = (n.get("label") or "").lower()
        desc = (n.get("description") or "").lower()
        if query_lower in label or query_lower in desc:
            matches.append(n)
    return matches

def bfs_traverse(graph, start_node_ids, depth=3):
    """BFS from start nodes, returning subgraph."""
    nodes = {n["id"]: n for n in graph.get("nodes", [])}
    links = graph.get("links", graph.get("edges", []))
    
    # Build adjacency
    adj = {}
    for l in links:
        s, t = l["source"], l["target"]
        adj.setdefault(s, []).append((t, l))
        adj.setdefault(t, []).append((s, l))
    
    visited = set()
    frontier = set(start_node_ids)
    result_nodes = []
    result_edges = []
    
    for d in range(depth):
        next_frontier = set()
        for nid in frontier:
            if nid in visited:
                continue
            visited.add(nid)
            if nid in nodes:
                result_nodes.append(nodes[nid])
            for neighbor, edge in adj.get(nid, []):
                if neighbor not in visited:
                    next_frontier.add(neighbor)
                    result_edges.append(edge)
        frontier = next_frontier
    
    return result_nodes, result_edges

def bfs_query(library, query, depth=3):
    """Run a BFS query against a library graph."""
    graph = load_graph(library)
    matches = find_nodes(graph, query)
    
    if not matches:
        print(f"No nodes matching '{query}' in {library} graph.")
        return
    
    print(f"Found {len(matches)} matching nodes for '{query}' in {library}:")
    for m in matches[:10]:
        desc = m.get("description", "")[:80]
        loc = m.get("source_file", "") + ":" + m.get("source_location", "")
        print(f"  • {m['label']} ({loc})")
        if desc:
            print(f"    {desc}")
    
    if len(matches) > 10:
        print(f"  ... and {len(matches) - 10} more")
    
    # BFS from top 3 matches
    top_ids = [m["id"] for m in matches[:3]]
    print(f"\nBFS traversal (depth={depth}) from top {len(top_ids)} matches:")
    rnodes, redges = bfs_traverse(graph, top_ids, depth)
    print(f"  Subgraph: {len(rnodes)} nodes, {len(redges)} edges")
    
    # Most connected in subgraph
    degrees = Counter()
    for e in redges:
        degrees[e["source"]] += 1
        degrees[e["target"]] += 1
    
    print("\n  Key connections:")
    for nid, deg in degrees.most_common(5):
        label = next((n["label"] for n in rnodes if n["id"] == nid), nid)
        print(f"    {label} ({deg} connections)")

def path_query(library, node_a, node_b):
    """Find shortest path between two nodes."""
    graph = load_graph(library)
    matches_a = find_nodes(graph, node_a)
    matches_b = find_nodes(graph, node_b)
    
    if not matches_a or not matches_b:
        print(f"Could not find one or both nodes: '{node_a}' ({len(matches_a)} found), '{node_b}' ({len(matches_b)} found)")
        return
    
    a_id = matches_a[0]["id"]
    b_id = matches_b[0]["id"]
    nodes = {n["id"]: n for n in graph.get("nodes", [])}
    links = graph.get("links", graph.get("edges", []))
    
    # Build adjacency
    adj = {}
    for l in links:
        s, t = l["source"], l["target"]
        adj.setdefault(s, []).append(t)
        adj.setdefault(t, []).append(s)
    
    # BFS path
    queue = deque([[a_id]])
    visited = {a_id}
    
    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == b_id:
            print(f"Path ({len(path)-1} hops):")
            for i, nid in enumerate(path):
                label = nodes.get(nid, {}).get("label", nid)
                prefix = "  → " if i > 0 else "  • "
                print(f"{prefix}{label}")
            return
        for neighbor in adj.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    
    print(f"No path found between '{node_a}' and '{node_b}'")

def explain_node(library, node_query):
    """Explain a single node and its connections."""
    graph = load_graph(library)
    matches = find_nodes(graph, node_query)
    
    if not matches:
        print(f"No node matching '{node_query}' in {library}.")
        return
    
    node = matches[0]
    print(f"Node: {node['label']}")
    print(f"  Source: {node.get('source_file', 'unknown')}:{node.get('source_location', '')}")
    print(f"  Type: {node.get('file_type', 'unknown')}")
    if node.get('description'):
        print(f"  Description: {node['description']}")
    
    # Find connections
    links = graph.get("links", graph.get("edges", []))
    connections = []
    for l in links:
        if l["source"] == node["id"]:
            connections.append(("→", l["target"], l.get("relation", ""), l.get("confidence", "")))
        elif l["target"] == node["id"]:
            connections.append(("←", l["source"], l.get("relation", ""), l.get("confidence", "")))
    
    print(f"\n  Connections ({len(connections)}):")
    nodes = {n["id"]: n for n in graph.get("nodes", [])}
    for direction, other_id, rel, conf in connections[:20]:
        other_label = nodes.get(other_id, {}).get("label", other_id)
        print(f"    {direction} {other_label} [{rel}] ({conf})")
    
    if len(connections) > 20:
        print(f"    ... and {len(connections) - 20} more")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Query knowledge graphs")
    parser.add_argument("library", choices=["sklearn", "optuna", "scikit-learn"], help="Library to query")
    parser.add_argument("query", nargs="?", help="Search query or node name")
    parser.add_argument("--path", nargs=2, metavar=("A", "B"), help="Find path between two nodes")
    parser.add_argument("--explain", action="store_true", help="Explain a single node")
    parser.add_argument("--depth", type=int, default=3, help="BFS depth (default: 3)")
    
    args = parser.parse_args()
    
    # Normalize library name
    lib = args.library.replace("-", "_")
    if lib == "sklearn":
        lib = "scikit-learn"
    
    if args.path:
        path_query(lib, args.path[0], args.path[1])
    elif args.explain and args.query:
        explain_node(lib, args.query)
    elif args.query:
        bfs_query(lib, args.query, args.depth)
    else:
        parser.print_help()
