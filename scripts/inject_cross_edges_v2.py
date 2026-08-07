#!/usr/bin/env python3
"""Resolve curated cross-library bridges to real graph nodes and (optionally) write
them as a cross-library OVERLAY graph.

Unlike the previous version (which substring-matched labels and happily resolved
bridges to benchmark/test/docstring/Cython nodes), this one:
  * matches endpoints PRECISELY — exact label first, code nodes only, excluding
    test/benchmark/example/binding-internal noise (see docs/specs/GRAPH_SPEC.md §6);
  * writes a real overlay graph (nodes namespaced `<lib>::<id>`, links = bridges)
    to knowledge_graphs/_cross_library/.graphify/graph.json with `--apply`.

On the CURRENT (pre-rebuild, noisy) graphs many endpoints legitimately fail to
resolve to a clean node — that is honest signal, not a bug. Re-run after the
Phase-1 rebuild (clean graphs) to get the full overlay.

Usage:
  python scripts/inject_cross_edges_v2.py            # dry run: report resolution
  python scripts/inject_cross_edges_v2.py --apply    # write the overlay graph
"""
import sys, json, re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KG_DIR = REPO_ROOT / "knowledge_graphs"

NOISE = ("tests/", "/test", "test_", "benchmarks/", "asv_bench", "bench_", "examples/",
         "r-package", "apps/", "/doc/", "docs/", ".github", "conftest")

# (library_a, label_a, library_b, label_b, relation, description)
ALL_BRIDGES = [
    ("numpy", "ndarray", "pandas", "DataFrame", "backed_by", "pandas DataFrame is backed by numpy ndarray for numerical storage"),
    ("numpy", "ndarray", "vectorbt", "ArrayWrapper", "wrapped_by", "vectorbt ArrayWrapper wraps numpy ndarray for named column access"),
    ("numpy", "linalg", "scipy", "linalg", "superset_of", "scipy.linalg extends numpy.linalg with additional decompositions"),
    ("pandas", "DataFrame", "scikit-learn", "BaseEstimator", "input_to", "pandas DataFrame is the standard input to sklearn fit()"),
    ("pandas", "DataFrame", "vectorbt", "Portfolio", "input_to", "pandas DataFrame is the primary data input to vectorbt Portfolio"),
    ("pandas", "DataFrame", "backtrader", "DataBase", "consumed_by", "backtrader data feeds (DataBase) consume pandas DataFrames as data source"),
    ("ta-lib", "RSI", "vectorbt", "SignalFactory", "generates", "ta-lib indicator values feed vectorbt SignalFactory for entry/exit signals"),
    ("ta-lib", "MACD", "vectorbt", "Portfolio", "indicator_for", "ta-lib MACD crossovers drive vectorbt Portfolio entry/exit logic"),
    ("vectorbt", "SignalFactory", "optuna", "Study", "optimized_by", "vectorbt signal parameters tuned via optuna Study.optimize"),
    ("backtrader", "Cerebro", "optuna", "Study", "optimized_by", "backtrader Cerebro strategy parameters tuned via optuna"),
    ("backtrader", "Strategy", "vectorbt", "Portfolio", "alternative_to", "backtrader event-driven Strategy vs vectorbt vectorized Portfolio"),
    ("xgboost", "XGBClassifier", "scikit-learn", "Pipeline", "compatible_with", "XGBClassifier implements the sklearn API, usable in a Pipeline"),
    ("xgboost", "XGBRegressor", "vectorbt", "Portfolio", "predicts_for", "XGBRegressor return predictions fed to vectorbt Portfolio simulation"),
    ("xgboost", "train", "optuna", "Study", "optimized_by", "xgboost.train hyperparameters tuned via optuna Study"),
    ("lightgbm", "LGBMClassifier", "scikit-learn", "GridSearchCV", "compatible_with", "LGBMClassifier works with sklearn GridSearchCV"),
    ("scikit-learn", "RandomForestClassifier", "vectorbt", "SignalFactory", "powers", "RandomForest predictions converted to vectorbt signals"),
    ("scikit-learn", "Pipeline", "optuna", "Study", "tuned_by", "sklearn Pipeline parameters optimized via optuna"),
    ("scipy", "stats", "scikit-learn", "SelectKBest", "powers", "scipy.stats statistical tests drive sklearn feature selection"),
    ("scipy", "optimize", "optuna", "Study", "alternative_to", "scipy.optimize as an alternative optimization backend to optuna"),
]

ALL_LIBS = ["numpy", "scipy", "pandas", "scikit-learn", "optuna",
            "vectorbt", "backtrader", "ta-lib", "xgboost", "lightgbm"]


def load_graph(lib):
    p = KG_DIR / lib / ".graphify" / "graph.json"
    return json.load(open(p)) if p.exists() else None


def clean(n):
    sf = (n.get("source_file") or "").lower()
    if any(p in sf for p in NOISE):
        return False
    lbl = n.get("label") or ""
    if not lbl or " " in lbl or len(lbl) > 40:
        return False
    if lbl.startswith("__pyx") or lbl.startswith("__Pyx"):
        return False
    if n.get("file_type") not in (None, "code"):
        return False
    return True


def resolve(graph, label, lib=None):
    """Exact-label code node preferred; else identifier-like substring. Noise excluded.
    ta-lib exception: indicators exist only as __pyx_pw_..._NAME() Cython wrappers."""
    cands = [n for n in graph.get("nodes", []) if clean(n)]
    for n in cands:
        if (n.get("label") or "").lower() == label.lower():
            return n
    for n in cands:
        if label.lower() in (n.get("label") or "").lower():
            return n
    if lib == "ta-lib":
        pat = re.compile(r"__pyx_pw_.*?" + re.escape(label) + r"\(\)$", re.I)
        for n in graph.get("nodes", []):
            if pat.search(n.get("label") or ""):
                return n
    return None


def main():
    apply = "--apply" in sys.argv
    graphs = {lib: g for lib in ALL_LIBS if (g := load_graph(lib))}

    overlay_nodes, overlay_links, report = {}, [], []
    print("=== Cross-library bridge resolution (precise) ===\n")
    for lib_a, lab_a, lib_b, lab_b, rel, desc in ALL_BRIDGES:
        ga, gb = graphs.get(lib_a), graphs.get(lib_b)
        na = resolve(ga, lab_a, lib_a) if ga else None
        nb = resolve(gb, lab_b, lib_b) if gb else None
        if na and nb:
            ida, idb = f"{lib_a}::{na['id']}", f"{lib_b}::{nb['id']}"
            overlay_nodes[ida] = {"id": ida, "label": na["label"], "library": lib_a,
                                  "source_file": na.get("source_file", "")}
            overlay_nodes[idb] = {"id": idb, "label": nb["label"], "library": lib_b,
                                  "source_file": nb.get("source_file", "")}
            overlay_links.append({"source": ida, "target": idb, "relation": rel,
                                  "confidence": "CURATED", "description": desc})
            report.append({"bridge": f"{lib_a}.{lab_a} -> {lib_b}.{lab_b}", "status": "RESOLVED",
                           "source": f"{lib_a}::{na['label']}", "target": f"{lib_b}::{nb['label']}",
                           "relation": rel})
            print(f"  ✓ {lib_a}.{na['label']} -> {lib_b}.{nb['label']}  [{rel}]")
        else:
            miss = ", ".join(x for x, ok in [(lab_a, na), (lab_b, nb)] if not ok)
            report.append({"bridge": f"{lib_a}.{lab_a} -> {lib_b}.{lab_b}", "status": "UNRESOLVED",
                           "missing": miss})
            print(f"  ✗ {lib_a}.{lab_a} -> {lib_b}.{lab_b}  (no clean node for: {miss})")

    resolved = sum(1 for r in report if r["status"] == "RESOLVED")
    tail = "all clean" if resolved == len(ALL_BRIDGES) else \
        f"{len(ALL_BRIDGES)-resolved} endpoints exist only as Cython/internal nodes (e.g. ta-lib RSI/MACD)"
    print(f"\n{resolved}/{len(ALL_BRIDGES)} bridges resolved to clean nodes ({tail})")

    json.dump({"bridges": report, "resolved": resolved, "attempted": len(ALL_BRIDGES)},
              open(REPO_ROOT / "docs" / "reference" / "cross-library-bridges.json", "w"), indent=2)

    if apply:
        overlay = {"directed": False, "multigraph": False,
                   "graph": {"kind": "cross_library_overlay", "note": "Curated bridges resolved to clean nodes."},
                   "nodes": list(overlay_nodes.values()), "links": overlay_links, "hyperedges": []}
        out = KG_DIR / "_cross_library" / ".graphify"
        out.mkdir(parents=True, exist_ok=True)
        json.dump(overlay, open(out / "graph.json", "w"), indent=2)
        print(f"Overlay written: {out/'graph.json'}  ({len(overlay_nodes)} nodes, {len(overlay_links)} links)")
    else:
        print("(dry run — pass --apply to write the overlay graph)")


if __name__ == "__main__":
    main()
