#!/usr/bin/env python3
"""Generate docs/reference/unified-index.md from the normalized skills + graphs.lock + bridges.

Reproducible replacement for the old hand-written (stale) template. Re-run after the
Phase-1 rebuild to refresh graph stats, and after any graph/label change to refresh the
node-level A–Z concept index (QKG_017).

Usage: python scripts/build_unified_index.py
"""
import json, re, pathlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
LOCK = json.load(open(ROOT / "graphs.lock"))["libraries"]

DOMAIN = {
    "Foundation Layer": ["numpy", "scipy", "pandas"],
    "ML & Optimization": ["scikit-learn", "xgboost", "lightgbm", "optuna"],
    "Quant Tools": ["vectorbt", "backtrader", "ta-lib"],
    "Statistical Models": ["statsmodels"],
}
LIB_DOMAIN = {lib: dom for dom, libs in DOMAIN.items() for lib in libs}

# Node-level A–Z concept seed (QKG_017): keywords match node/community labels;
# libs restrict the search. Seeded from the quant-patterns playbooks' domains.
CONCEPTS = {
    "Backtesting": {"keywords": ["cerebro", "backtest", "portfolio"], "libs": ["backtrader", "vectorbt"]},
    "Data Wrangling": {"keywords": ["frame", "array", "series", "index"], "libs": ["pandas", "numpy"]},
    "Feature Engineering": {"keywords": ["scaler", "encoder", "polynomial", "selection"], "libs": ["scikit-learn"]},
    "Gradient Boosting": {"keywords": ["booster", "xgbr", "lgbm", "gradient"], "libs": ["xgboost", "lightgbm"]},
    "Hyperparameter Optimization": {"keywords": ["study", "trial", "sampler", "pruner"], "libs": ["optuna"]},
    "Linear Algebra": {"keywords": ["linalg", "matrix", "det", "eig"], "libs": ["numpy", "scipy"]},
    "Machine Learning": {"keywords": ["classifier", "regressor", "estimator", "cluster"], "libs": ["scikit-learn"]},
    "Portfolio Construction": {"keywords": ["portfolio", "order", "position", "returns"], "libs": ["vectorbt"]},
    "Probability & Distributions": {"keywords": ["distribution", "random", "normal", "poisson"], "libs": ["scipy", "numpy"]},
    "Random Generation": {"keywords": ["random", "generator", "seed"], "libs": ["numpy"]},
    "Regression": {"keywords": ["regress", "glm", "ols", "logit"], "libs": ["statsmodels", "scikit-learn"]},
    "Regime Detection": {"keywords": ["signal", "filter", "spectral", "markov"], "libs": ["scipy", "numpy"]},
    "Signal Processing": {"keywords": ["filter", "fft", "conv", "signal"], "libs": ["scipy"]},
    "Statistical Inference": {"keywords": ["stats", "test", "dist", "ttest"], "libs": ["scipy", "statsmodels"]},
    "Technical Analysis": {"keywords": ["rsi", "macd", "sma", "indicator", "stoch"], "libs": ["ta-lib"]},
    "Time Series": {"keywords": ["series", "tsa", "arima", "rolling", "asof"], "libs": ["pandas", "statsmodels"]},
    "Walk-Forward Validation": {"keywords": ["time", "split", "walk", "cv"], "libs": ["scikit-learn", "backtrader"]},
}


def fm_of(path):
    m = re.match(r"^---\n(.*?)\n---", path.read_text(), re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def scan():
    libs = {}
    playbooks = []
    for p in sorted(SKILLS.rglob("SKILL.md")):
        rel = p.relative_to(SKILLS)
        lib = rel.parts[0]
        fm = fm_of(p)
        entry = {"name": fm.get("name", ""), "desc": fm.get("description", ""),
                 "router": len(rel.parts) == 2, "path": str(rel)}
        if lib == "quant-patterns":
            if len(rel.parts) >= 3:
                playbooks.append(entry)
        else:
            libs.setdefault(lib, []).append(entry)
    return libs, playbooks


def graph_facts(lib):
    """(labels_with_degree, community_labels) for a library — empty when absent."""
    p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not p.exists():
        return {}, set()
    g = json.load(open(p))
    deg = {}
    for l in g.get("links", []):
        deg[l["source"]] = deg.get(l["source"], 0) + 1
        deg[l["target"]] = deg.get(l["target"], 0) + 1
    labels = {}
    for n in g.get("nodes", []):
        lbl = n.get("label", "")
        if lbl and not lbl.startswith("_") and " " not in lbl:
            labels[lbl] = deg.get(n["id"], 0)
    comms = set()
    for v in g.get("graph", {}).get("community_labels", {}).values():
        if v and not re.match(r"^Community \d+$", str(v)):
            comms.add(str(v).lower())
    return labels, comms


def concept_index():
    """A–Z concept → real graph nodes (QKG_017). Deterministic: sorted everywhere."""
    facts = {lib: graph_facts(lib) for lib in LOCK}
    out = []
    for concept in sorted(CONCEPTS):
        spec = CONCEPTS[concept]
        kws = [k.lower() for k in spec["keywords"]]
        rows = []
        for lib in spec["libs"]:
            labels, comms = facts.get(lib, ({}, set()))
            hits = []
            for lbl, d in labels.items():
                low = lbl.lower().lstrip("_")
                if any(k in low for k in kws) and not low.endswith(
                        (".py", ".c", ".cpp", ".h", ".hpp", ".pyx")):
                    hits.append((d, lbl))
            comm_hit = any(any(k in c for k in kws) for c in comms)
            rows.append((lib, sorted(hits, reverse=True)[:3], comm_hit))
        out.append((concept, spec, rows))
    L = ["", "## Concepts (A–Z) — node-level index", "",
         "> Every concept resolves to real nodes in the committed graphs (labels matched "
         "against the concept keywords; top-degree per library shown). Regenerated by "
         "`scripts/build_unified_index.py` — deterministic across runs.", ""]
    for concept, spec, rows in out:
        cells = []
        for lib, hits, comm_hit in rows:
            if not hits:
                continue
            names = ", ".join(f"`{l}`" for _, l in hits[:3])
            cells.append(f"{lib}: {names}")
        if not cells:
            continue
        L.append(f"### {concept}")
        L.append("")
        L.append(" - ".join(cells))
        L.append("")
    return L


def main():
    libs, playbooks = scan()
    bridges = []
    bpath = ROOT / "docs" / "reference" / "cross-library-bridges.json"
    if bpath.exists():
        bridges = [b for b in json.load(open(bpath)).get("bridges", []) if b.get("status") == "RESOLVED"]

    L = ["# Unified Index",
         "",
         "> Cross-library map of the quant-kg-lab stack. Generated by "
         "`scripts/build_unified_index.py` from the skills + `graphs.lock` + the "
         "committed graphs (node-level A–Z concept index included, QKG_017).",
         "",
         "## Domain taxonomy (the overlay on the library-first layout)",
         "",
         "| Domain | Libraries |",
         "|--------|-----------|"]
    for dom, ls in DOMAIN.items():
        L.append(f"| **{dom}** | {', '.join(ls)} |")
    L.append("| **Workflows** | quant-patterns (composable playbooks) |")

    L += ["", "## Libraries", "",
          "| Library | Domain | Nodes · Edges | Skills | Router |",
          "|---------|--------|---------------|--------|--------|"]
    for lib in sorted(LOCK, key=lambda x: (LIB_DOMAIN.get(x, "z"), x)):
        info = LOCK.get(lib, {})
        n_skills = len([e for e in libs.get(lib, []) if not e["router"]])
        has_router = any(e["router"] for e in libs.get(lib, []))
        router = f"[`{lib}`](../../skills/{lib}/SKILL.md)" if has_router else "—"
        L.append(f"| {lib} | {LIB_DOMAIN.get(lib,'—')} | {info.get('nodes','?')} · {info.get('edges','?')} "
                 f"| {n_skills} | {router} |")

    L += ["", "## Skills index", ""]
    for lib in sorted(libs, key=lambda x: (LIB_DOMAIN.get(x, "z"), x)):
        L.append(f"### {lib}")
        for e in sorted(libs[lib], key=lambda x: (not x["router"], x["name"])):
            tag = " *(router)*" if e["router"] else ""
            L.append(f"- [`{e['name']}`](../../skills/{e['path']}){tag} — {e['desc']}")
        L.append("")

    L += ["## Workflow playbooks (composable stack)", ""]
    for e in sorted(playbooks, key=lambda x: x["name"]):
        L.append(f"- [`{e['name']}`](../../skills/{e['path']}) — {e['desc']}")

    L += ["", "## Cross-library bridges (resolved to clean nodes)", ""]
    if bridges:
        L += ["| Source | Target | Relation |", "|--------|--------|----------|"]
        for b in bridges:
            L.append(f"| {b.get('source','')} | {b.get('target','')} | {b.get('relation','')} |")
        L.append("")
        L.append("_Generated by `scripts/inject_cross_edges_v2.py`; overlay graph at "
                 "`knowledge_graphs/_cross_library/`. A few endpoints that exist only as "
                 "Cython/internal nodes (e.g. ta-lib RSI/MACD) are omitted._")
    else:
        L.append("_Run `scripts/inject_cross_edges_v2.py` to populate resolved bridges._")

    L += concept_index()

    out = ROOT / "docs" / "reference" / "unified-index.md"
    out.write_text("\n".join(L) + "\n")
    print(f"wrote {out} ({len(libs)} libraries, {sum(len(v) for v in libs.values())} skill entries, "
          f"{len(playbooks)} playbooks, {len(bridges)} bridges, {len(CONCEPTS)} concepts)")


if __name__ == "__main__":
    main()
