#!/usr/bin/env python3
"""Post-process graph.json files to add a node_type field to each node.

Heuristic classification (covers ~90%+ of nodes across all 28 graphs):
  1. file_type == "rationale"          → "module"   (docstring / comment node)
  2. label ends with ".py"             → "module"   (file reference)
  3. label starts with "."             → "method"   (instance method, e.g. ".__len__()")
  4. label matches ^__.*__$ with "()"  → "method"   (dunder method, e.g. "__init__()")
  5. label matches ^[A-Z][a-zA-Z0-9]+$→ "class"    (CamelCase, no parens)
  6. label matches ^[A-Z][A-Z0-9_]+$  → "constant" (ALL_CAPS)
  7. label ends with "()"              → "function" (regular function)
  8. default                           → "function"

Usage:
  python3 scripts/add_node_type.py <graph.json>        # in-place update
  python3 scripts/add_node_type.py --all               # all libs in knowledge_graphs/
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Pre-compiled patterns
RE_DUNDER = re.compile(r"^__.*__\(\)$")
RE_CAMEL = re.compile(r"^[A-Z][a-zA-Z0-9]+$")
RE_ALLCAPS = re.compile(r"^[A-Z][A-Z0-9_]+$")


def infer_node_type(node):
    """Return node_type string for a single node dict."""
    label = node.get("label", "")
    file_type = node.get("file_type", "")

    # 1. rationale docstrings / comments → module
    if file_type == "rationale":
        return "module"
    # 2. file references ending with .py → module
    if label.endswith(".py"):
        return "module"
    # 3. dot-prefixed instance methods (e.g. ".__len__()") → method
    if label.startswith("."):
        return "method"
    # 4. dunder methods without dot (e.g. "__init__()") → method
    if RE_DUNDER.match(label):
        return "method"
    # 5. CamelCase (no parens, no underscores) → class
    if RE_CAMEL.match(label):
        return "class"
    # 6. ALL_CAPS with optional underscores/digits → constant
    if RE_ALLCAPS.match(label):
        return "constant"
    # 7. label ends with () → function
    if label.endswith("()"):
        return "function"
    # 8. default
    return "function"


def add_node_types(graph_path):
    """Read graph.json, add node_type to every node, write back. Returns counts."""
    with open(graph_path) as f:
        g = json.load(f)
    counts = {}
    for node in g["nodes"]:
        nt = infer_node_type(node)
        node["node_type"] = nt
        counts[nt] = counts.get(nt, 0) + 1
    with open(graph_path, "w") as f:
        json.dump(g, f, indent=2)
        f.write("\n")
    return counts


def main():
    args = sys.argv[1:]
    if "--all" in args:
        graphs = sorted(
            p for p in (ROOT / "knowledge_graphs").rglob("graph.json")
            if p.parent.name == ".graphify"
        )
    elif args and not args[0].startswith("--"):
        graphs = [pathlib.Path(args[0])]
    else:
        print(__doc__.strip())
        sys.exit(2)

    total_counts = {}
    for gp in graphs:
        counts = add_node_types(gp)
        for k, v in counts.items():
            total_counts[k] = total_counts.get(k, 0) + v
        total = sum(counts.values())
        summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
        print(f"  {gp.parent.parent.name:20s} {total:6d} nodes  {summary}")

    grand = sum(total_counts.values())
    print(f"\n  {'TOTAL':20s} {grand:6d} nodes  "
          + ", ".join(f"{k}={v}" for k, v in sorted(total_counts.items())))


if __name__ == "__main__":
    main()
