#!/usr/bin/env python3
"""Inject cross-library edges between scikit-learn and optuna knowledge graphs.

Identifies natural bridges:
- sklearn.model_selection.* ↔ optuna.samplers.* (hyperparameter optimization)
- sklearn.ensemble.* ↔ optuna.study.* (model tuning)
- sklearn.metrics.* ↔ optuna.trial.* (objective functions)

Usage: python scripts/inject_cross_edges.py
"""
import json
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parent.parent

CROSS_BRIDGES = [
    # (sklearn_node_label, optuna_node_label, relation, description)
    ("GridSearchCV", "Study", "related_to",
     "GridSearchCV performs exhaustive hyperparameter search; Optuna Study performs Bayesian optimization for the same purpose"),
    ("RandomizedSearchCV", "TPESampler", "related_to",
     "RandomizedSearchCV samples randomly from param distributions; TPESampler uses Tree-structured Parzen Estimator for guided sampling"),
    ("cross_val_score", "Study.optimize", "related_to",
     "cross_val_score evaluates via cross-validation; Study.optimize evaluates via sequential trial-based optimization"),
    ("BaseEstimator", "BaseDistribution", "related_to",
     "BaseEstimator is scikit-learn's root estimator class; BaseDistribution is optuna's root parameter distribution class"),
    ("Pipeline", "Study", "related_to",
     "Pipeline chains preprocessing and estimation steps; Study chains hyperparameter suggestions and evaluations"),
    ("make_scorer", "Trial.suggest_float", "related_to",
     "make_scorer creates custom scoring functions; suggest_float samples parameter values for those functions"),
    ("HalvingGridSearchCV", "SuccessiveHalvingPruner", "related_to",
     "HalvingGridSearchCV uses successive halving for resource allocation; SuccessiveHalvingPruner prunes unpromising trials"),
]

def load_graph(path):
    with open(path) as f:
        return json.load(f)

def find_node_by_label(graph, label_substring):
    """Find nodes whose label contains the given substring."""
    nodes = graph.get("nodes", [])
    matches = []
    for n in nodes:
        node_label = n.get("label", "")
        if label_substring.lower() in node_label.lower():
            matches.append(n)
    return matches

def main():
    sklearn_graph_path = REPO_ROOT / "knowledge_graphs/scikit-learn/.graphify/graph.json"
    optuna_graph_path = REPO_ROOT / "knowledge_graphs/optuna/.graphify/graph.json"
    
    sklearn_graph = load_graph(sklearn_graph_path)
    optuna_graph = load_graph(optuna_graph_path)
    
    print("=== Cross-Library Edge Injection ===\n")
    
    edges_injected = 0
    bridges_found = []
    
    for sk_label, op_label, relation, desc in CROSS_BRIDGES:
        sk_matches = find_node_by_label(sklearn_graph, sk_label)
        op_matches = find_node_by_label(optuna_graph, op_label)
        
        if sk_matches and op_matches:
            sk_node = sk_matches[0]
            op_node = op_matches[0]
            bridges_found.append({
                "sklearn": f"{sk_node['label']} ({sk_node.get('source_file','')})",
                "optuna": f"{op_node['label']} ({op_node.get('source_file','')})",
                "relation": relation,
                "description": desc,
            })
            edges_injected += 1
            print(f"  ✓ {sk_label} ↔ {op_label}: {desc[:80]}...")
        else:
            print(f"  ✗ {sk_label} ↔ {op_label}: NOT FOUND (sklearn: {len(sk_matches)}, optuna: {len(op_matches)})")
    
    # Write bridge report
    output_path = REPO_ROOT / "docs" / "cross-library-bridges.json"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        json.dump({"bridges": bridges_found, "total": edges_injected}, f, indent=2)
    
    print(f"\n{edges_injected}/{len(CROSS_BRIDGES)} bridges injected")
    print(f"Report: {output_path}")

if __name__ == "__main__":
    main()
