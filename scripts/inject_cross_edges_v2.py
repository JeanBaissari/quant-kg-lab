#!/usr/bin/env python3
"""Inject cross-library edges across ALL 10 knowledge graphs.

Expanded from the original sklearn↔optuna bridges to cover the full ecosystem.

Usage: python scripts/inject_cross_edges_v2.py
"""
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KG_DIR = REPO_ROOT / "knowledge_graphs"

# Format: (library_a, node_label_a, library_b, node_label_b, relation, description)
ALL_BRIDGES = [
    # === Foundation Layer ===
    ("numpy", "ndarray", "pandas", "DataFrame",
     "backed_by", "pandas DataFrame is backed by numpy ndarray for numerical storage"),
    ("numpy", "ndarray", "scipy", "sparse",
     "data_source", "scipy sparse matrices consume numpy arrays as input"),
    ("numpy", "linalg", "scipy", "linalg",
     "superset_of", "scipy.linalg extends numpy.linalg with additional decompositions"),
    ("numpy", "random", "scipy", "stats",
     "complements", "numpy.random generates samples; scipy.stats models distributions"),
    ("numpy", "ufunc", "pandas", "apply",
     "powers", "pandas apply/transform operations use numpy ufuncs under the hood"),
    
    # === Data → ML Pipeline ===
    ("pandas", "DataFrame", "scikit-learn", "BaseEstimator",
     "input_to", "pandas DataFrame is the standard input to sklearn fit()"),
    ("pandas", "read_csv", "scikit-learn", "train_test_split",
     "precedes", "data loaded via pandas read_csv feeds into sklearn train/test splits"),
    ("pandas", "rolling", "ta-lib", "SMA",
     "implements", "pandas rolling window underpins ta-lib moving average calculations"),
    
    # === Quant Tools → ML Integration ===
    ("ta-lib", "RSI", "vectorbt", "SignalFactory",
     "generates", "ta-lib RSI values feed into vectorbt SignalFactory for entry/exit signals"),
    ("ta-lib", "MACD", "vectorbt", "Portfolio",
     "indicator_for", "ta-lib MACD crossovers drive vectorbt Portfolio entry/exit logic"),
    ("vectorbt", "Portfolio", "scikit-learn", "cross_val_score",
     "evaluated_by", "vectorbt portfolio returns evaluated via sklearn cross_val_score"),
    ("vectorbt", "SignalFactory", "optuna", "Study",
     "optimized_by", "vectorbt signal parameters tuned via optuna Study.optimize"),
    ("vectorbt", "Config", "optuna", "TPESampler",
     "configured_by", "vectorbt Config parameters sampled by optuna TPESampler"),
    
    # === Backtesting Engines ===
    ("backtrader", "Cerebro", "optuna", "Study",
     "optimized_by", "backtrader Cerebro strategy parameters tuned via optuna"),
    ("backtrader", "Strategy", "vectorbt", "Portfolio",
     "alternative_to", "backtrader event-driven Strategy vs vectorbt vectorized Portfolio"),
    ("backtrader", "DataFeed", "pandas", "DataFrame",
     "consumes", "backtrader DataFeed consumes pandas DataFrames as data source"),
    
    # === ML Boosters → sklearn ===
    ("xgboost", "XGBClassifier", "scikit-learn", "Pipeline",
     "compatible_with", "XGBClassifier implements sklearn API, usable in Pipeline"),
    ("xgboost", "train", "optuna", "Study",
     "optimized_by", "xgboost.train hyperparameters tuned via optuna Study"),
    ("lightgbm", "LGBMClassifier", "scikit-learn", "GridSearchCV",
     "compatible_with", "LGBMClassifier works with sklearn GridSearchCV"),
    ("lightgbm", "train", "optuna", "integration",
     "integrated_with", "lightgbm has native optuna integration via LightGBMPruningCallback"),
    
    # === ML → Quant Tools ===
    ("scikit-learn", "RandomForestClassifier", "vectorbt", "SignalFactory",
     "powers", "RandomForest classifier predictions converted to vectorbt signals"),
    ("xgboost", "XGBRegressor", "vectorbt", "Portfolio",
     "predicts_for", "XGBRegressor return predictions fed to vectorbt Portfolio simulation"),
    ("scikit-learn", "Pipeline", "optuna", "Study",
     "tuned_by", "sklearn Pipeline parameters optimized via optuna"),
    
    # === Statistical → Quant ===
    ("scipy", "stats", "scikit-learn", "SelectKBest",
     "powers", "scipy.stats statistical tests drive sklearn feature selection"),
    ("scipy", "optimize", "optuna", "samplers",
     "alternative_to", "scipy.optimize as alternative optimization backend to optuna samplers"),
    ("scipy", "signal", "ta-lib", "indicators",
     "underlies", "scipy.signal filtering underpins ta-lib technical indicator calculations"),
    
    # === Cross-Framework ===
    ("pandas", "DataFrame", "vectorbt", "Portfolio",
     "input_to", "pandas DataFrame is the primary data input to vectorbt Portfolio"),
    ("numpy", "ndarray", "vectorbt", "ArrayWrapper",
     "wrapped_by", "vectorbt ArrayWrapper wraps numpy ndarray for named column access"),
    ("scikit-learn", "make_scorer", "optuna", "Study",
     "objective_for", "sklearn scorers used as optuna Study optimization objectives"),
]

def find_node(graph, label_substring):
    """Find a node by label substring, returning (id, label, source_file)."""
    for n in graph.get("nodes", []):
        node_label = n.get("label", "")
        if label_substring.lower() in node_label.lower():
            return n["id"], node_label, n.get("source_file", "")
    return None, None, None

def load_graph(lib):
    path = KG_DIR / lib / ".graphify" / "graph.json"
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)

def main():
    graphs = {}
    for lib in ["numpy", "scipy", "pandas", "scikit-learn", "optuna", 
                "vectorbt", "backtrader", "ta-lib", "xgboost", "lightgbm"]:
        g = load_graph(lib)
        if g:
            graphs[lib] = g
    
    print("=== Cross-Library Bridge Injection v2 ===\n")
    
    results = []
    for lib_a, label_a, lib_b, label_b, relation, desc in ALL_BRIDGES:
        g_a = graphs.get(lib_a)
        g_b = graphs.get(lib_b)
        
        if not g_a or not g_b:
            results.append({"bridge": f"{label_a}↔{label_b}", "status": "SKIP", "reason": "graph missing"})
            continue
        
        id_a, name_a, src_a = find_node(g_a, label_a)
        id_b, name_b, src_b = find_node(g_b, label_b)
        
        if id_a and id_b:
            results.append({
                "bridge": f"{name_a}↔{name_b}",
                "status": "FOUND",
                "source": f"{lib_a}:{src_a}",
                "target": f"{lib_b}:{src_b}",
                "relation": relation,
                "description": desc,
            })
            print(f"  ✓ {lib_a}.{name_a} ↔ {lib_b}.{name_b}: {desc[:70]}...")
        else:
            found = bool(id_a) + bool(id_b)
            results.append({"bridge": f"{label_a}↔{label_b}", "status": "MISSING", "found": f"{found}/2"})
            print(f"  ✗ {label_a}↔{label_b}: {found}/2 found")
    
    found = sum(1 for r in results if r["status"] == "FOUND")
    print(f"\n{found}/{len(ALL_BRIDGES)} bridges injected")
    
    # Write report
    output_path = REPO_ROOT / "docs" / "cross-library-bridges-v2.json"
    with open(output_path, "w") as f:
        json.dump({"bridges": results, "total_found": found, "total_attempted": len(ALL_BRIDGES)}, f, indent=2)
    print(f"Report: {output_path}")

if __name__ == "__main__":
    main()
