#!/usr/bin/env python3
"""Query knowledge graphs using graph traversal.

Usage:
    python scripts/query_graph.py sklearn "How does Pipeline work?"
    python scripts/query_graph.py optuna "What samplers exist?"
    python scripts/query_graph.py sklearn --path "GridSearchCV" "TPESampler"
    python scripts/query_graph.py sklearn --explain "BaseEstimator"
    python scripts/query_graph.py --all "risk free"
    python scripts/query_graph.py --all "ARIMA"
"""
import difflib
import json
import re
import sys
from pathlib import Path
import math
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
    """Find nodes matching a query (QKG_066: tokenized AND-match).

    The query is normalized (lowercase, dashes/underscores/unicode-punctuation
    folded to spaces) and split into terms; English stop-words are dropped;
    a node matches when EVERY remaining term appears in its label or
    description — so `kolmogorov smirnov` hits the `ks_2samp`-adjacent nodes,
    `kolmogorov–smirnov` (en-dash) works, and question-phrases like
    "how does Pipeline work?" reduce to `[pipeline, work]`.
    """
    STOP = {"how", "does", "what", "which", "where", "when", "why", "the", "a",
            "an", "and", "or", "in", "on", "of", "to", "for", "with", "is", "are",
            "do", "exist", "work", "works", "any", "many", "all", "about", "using"}
    nodes = graph.get("nodes", [])
    tokens = []
    for tok in re.sub(r"[–—_\-]+", " ", query.lower()).split():
        tok = re.sub(r"[^a-z0-9]+$", "", tok)
        if tok and tok not in STOP:
            tokens.append(tok)
    if not tokens:
        return []
    matches = []
    for n in nodes:
        label = (n.get("label") or "").lower()
        desc = (n.get("description") or "").lower()
        if all(tok in label or tok in desc for tok in tokens):
            matches.append(n)
    return matches

# ── Cross-library search (QKG_076) ──────────────────────────────────────────

def _tokenize(text):
    """Normalize and split *text* into lowercase alphanumeric tokens."""
    STOP = {"how", "does", "what", "which", "where", "when", "why", "the", "a",
            "an", "and", "or", "in", "on", "of", "to", "for", "with", "is", "are",
            "do", "exist", "work", "works", "any", "many", "all", "about", "using"}
    tokens = []
    for tok in re.sub(r"[–—_\-]+", " ", text.lower()).split():
        tok = re.sub(r"[^a-z0-9]+$", "", tok)
        if tok and tok not in STOP:
            tokens.append(tok)
    return tokens

# BM25 parameters
BM25_K1 = 1.5
BM25_B = 0.75

def _compute_idf(nodes):
    """Pre-compute IDF across all loaded nodes.

    Returns (idf dict, average document length).
    IDF formula: ``log((N - df + 0.5) / (df + 0.5) + 1)``
    where N = total nodes, df = document frequency per token.
    """
    N = len(nodes)
    doc_freq = Counter()       # token -> how many nodes contain it
    doc_lengths = []           # length (in tokens) of each node
    for node in nodes:
        text = ((node.get("label") or "") + " " + (node.get("description") or "")).lower()
        toks = []
        for tok in re.sub(r"[–—_\-]+", " ", text).split():
            tok = re.sub(r"[^a-z0-9]+$", "", tok)
            if tok:
                toks.append(tok)
        doc_lengths.append(len(toks))
        for tok in set(toks):
            doc_freq[tok] += 1
    avgdl = sum(doc_lengths) / N if N else 1
    idf = {}
    for tok, df in doc_freq.items():
        idf[tok] = math.log((N - df + 0.5) / (df + 0.5) + 1)
    return idf, avgdl

def _score_node(node, query_tokens, idf, avgdl):
    """Score a node against query tokens using BM25.

    score = sum(idf[t] * (tf[t] * (k1 + 1)) / (tf[t] + k1 * (1 - b + b * dl/avgdl)))
    """
    label = (node.get("label") or "").lower()
    desc = (node.get("description") or "").lower()
    text = label + " " + desc
    # Tokenize the node's full text
    doc_toks = []
    for tok in re.sub(r"[–—_\-]+", " ", text).split():
        tok = re.sub(r"[^a-z0-9]+$", "", tok)
        if tok:
            doc_toks.append(tok)
    dl = len(doc_toks)
    tf = Counter(doc_toks)
    score = 0.0
    for t in query_tokens:
        if t not in idf:
            continue
        tf_t = tf.get(t, 0)
        if tf_t == 0:
            continue
        numerator = idf[t] * (tf_t * (BM25_K1 + 1))
        denominator = tf_t + BM25_K1 * (1 - BM25_B + BM25_B * dl / avgdl)
        score += numerator / denominator
    return score

def _load_all_graphs():
    """Load every committed graph, skipping the ``_cross_library`` directory."""
    kg_root = REPO_ROOT / "knowledge_graphs"
    if not kg_root.exists():
        return []
    graphs = []
    for lib_dir in sorted(kg_root.iterdir()):
        if lib_dir.name.startswith("_"):
            continue
        gpath = lib_dir / ".graphify" / "graph.json"
        if gpath.exists():
            with open(gpath) as f:
                graphs.append((lib_dir.name, json.load(f)))
    return graphs

def cross_library_search(query, top_n=50, lib_filter=None, min_score=0.0):
    """Search across every library graph and return BM25-scored results.

    Parameters
    ----------
    query : str
        Natural-language query.
    top_n : int
        Maximum results to display (hard cap 50).
    lib_filter : str | None
        If set, restrict search to this library name only.
    min_score : float
        Discard results with score below this threshold.
    """
    MAX_RESULTS = 50
    top_n = min(top_n, MAX_RESULTS)

    query_tokens = _tokenize(query)
    if not query_tokens:
        print("No search terms after tokenisation.")
        return

    graphs = _load_all_graphs()
    if not graphs:
        print("No library graphs found under knowledge_graphs/.")
        return

    # Filter to requested library
    if lib_filter:
        lib_filter_resolved = LIBRARY_ALIASES.get(lib_filter, lib_filter)
        graphs = [(ln, g) for ln, g in graphs if ln == lib_filter_resolved]
        if not graphs:
            available = [ln for ln, _ in _load_all_graphs()]
            print(f"Library '{lib_filter}' not found. Available: {', '.join(available)}")
            return

    # Collect all nodes across (filtered) graphs for IDF computation
    all_nodes = []
    for lib_name, graph in graphs:
        all_nodes.extend(graph.get("nodes", []))

    if not all_nodes:
        print("No nodes found to index.")
        return

    idf, avgdl = _compute_idf(all_nodes)

    results = []  # (score, lib, node)
    for lib_name, graph in graphs:
        for node in graph.get("nodes", []):
            sc = _score_node(node, query_tokens, idf, avgdl)
            if sc > min_score:
                results.append((sc, lib_name, node))

    if not results:
        print(f"No matches found for '{query}' across {len(graphs)} libraries.")
        return

    results.sort(key=lambda x: -x[0])
    top = results[:top_n]

    print(f"Cross-library results for '{query}' ({len(results)} total, top {len(top)}):\n")
    print(f"{'lib':<18} {'score':>7}  {'node_label':<40} source")
    print("-" * 107)
    for sc, lib, node in top:
        loc = node.get("source_file", "") + ":" + node.get("source_location", "")
        label = node.get("label", node.get("id", ""))
        print(f"{lib:<18} {sc:>7.2f}  {label:<40} {loc}")

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

def available_libraries():
    """Discover libraries that have a committed graph on disk."""
    kg_root = REPO_ROOT / "knowledge_graphs"
    if not kg_root.exists():
        return []
    return sorted(
        p.name for p in kg_root.iterdir()
        if (p / ".graphify" / "graph.json").exists()
    )

# Aliases → on-disk directory name (dirs use hyphens: scikit-learn, ta-lib)
LIBRARY_ALIASES = {"sklearn": "scikit-learn", "talib": "ta-lib"}

if __name__ == "__main__":
    import argparse
    libs = available_libraries()
    parser = argparse.ArgumentParser(
        description="Query knowledge graphs",
        epilog="Available: " + (", ".join(libs) or "<none>") + "  (aliases: sklearn, talib)",
    )
    parser.add_argument("positional", nargs="*", help="Library and/or query (see below)")
    parser.add_argument("--all", action="store_true", dest="all_libs",
                        help="Search across ALL library graphs (cross-library mode)")
    parser.add_argument("--path", nargs=2, metavar=("A", "B"), help="Find path between two nodes")
    parser.add_argument("--explain", action="store_true", help="Explain a single node")
    parser.add_argument("--depth", type=int, default=3, help="BFS depth (default: 3)")
    parser.add_argument("--top", type=int, default=50, help="Number of cross-library results (default: 50, max: 50)")
    parser.add_argument("--lib", type=str, default=None, help="Restrict search to a specific library (cross-library mode)")
    parser.add_argument("--min-score", type=float, default=0.0, help="Minimum BM25 score threshold (default: 0)")

    args = parser.parse_args()

    if args.all_libs:
        query_str = " ".join(args.positional)
        if not query_str:
            parser.error("--all requires a query string")
        cross_library_search(query_str, top_n=args.top, lib_filter=args.lib, min_score=args.min_score)
    elif not args.positional:
        parser.print_help()
    else:
        # Determine library vs query from positional args
        # If first arg is a known library (or alias), treat it as library; otherwise treat all as query
        first = args.positional[0]
        lib_candidate = LIBRARY_ALIASES.get(first, first)
        if lib_candidate in libs and not args.path:
            lib = lib_candidate
            query_str = " ".join(args.positional[1:]) if len(args.positional) > 1 else None
            if args.path:
                path_query(lib, args.path[0], args.path[1])
            elif args.explain and query_str:
                explain_node(lib, query_str)
            elif query_str:
                bfs_query(lib, query_str, args.depth)
            else:
                parser.print_help()
        elif args.path:
            # --path requires a library first
            if len(args.positional) >= 1:
                lib = LIBRARY_ALIASES.get(args.positional[0], args.positional[0])
            else:
                parser.error("--path requires a library argument")
            path_query(lib, args.path[0], args.path[1])
        else:
            # No known library prefix — treat all positionals as a query in cross-library mode
            query_str = " ".join(args.positional)
            cross_library_search(query_str, top_n=args.top, lib_filter=args.lib, min_score=args.min_score)
