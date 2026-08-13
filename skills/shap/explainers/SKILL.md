---
name: shap-explainers
description: "Use when computing SHAP values with shap — Explainer (Tree/Linear/Kernel/Deep), Explanation objects, and maskers."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: shap/shap
source_commit: df974a1966294b9c7acebb1373fd6dc5445d1d3d
extraction_date: 2026-08-12
graph:
  nodes: 1277
  edges: 1752
  community_count: 108
  graph_hash: bc0cb8c9a6ed8ed2
tags:
- shap
- explainability
- shapley
related_skills:
- shap
- shap-plots
- xgboost-core
- lightgbm-core
---

# shap.explainers

SHAP value computation: `Explainer` (with `TreeExplainer`/`LinearExplainer`/
`KernelExplainer`/`DeepExplainer` variants) returns `Explanation` objects —
values, base_values, and data ready for plotting.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Explainer` | `explainers/_explainer.py` | Unified explainer entry — auto-selects the variant from the model type |
| `Explanation` | `_explanation.py` | Output object: `values`, `base_values`, `data`, `feature_names`; carries `.plot()` |
| `Masker` | `maskers/_masker.py` | Input masking strategies (Independent, Tabular, Partition) for the explainer |
| `Model` | `models/_model.py` | Model wrapper abstraction (callable/ensemble adapters) |
| `_tree.py` | `explainers/_tree.py` | TreeExplainer machinery — exact SHAP for tree ensembles |

## Common Patterns

- **Tree models**: `shap.TreeExplainer(model).shap_values(X)` — exact and fast for
  xgboost/lightgbm/sklearn trees (pass `tree_limit` for ensemble length).
- **Any model**: `shap.Explainer(model).shap_values(X)` — auto-dispatch.
- **Explanation object**: `exp = explainer(X)` → `exp.base_values`, `exp.values` —
  then `shap.waterfall_plot(exp[0])`.
- **Interaction**: `TreeExplainer(model, feature_perturbation="interventional")`
  with `shap_values(..., interactions=True)`.

## Pitfalls

- **Background data**: kernel/partition explainers need a background dataset — small,
  representative samples only.
- **Tree limit**: boosted ensembles: use `tree_limit` matching the deployed model; defaults
  may differ.
- **Performance**: TreeExplainer is O(leaves × features) per row; for large universes batch
  the `shap_values` calls.

## Provenance

Graph: `knowledge_graphs/shap/.graphify/graph.json` — 1277 nodes · 1752 edges ·
108 communities · graphify @ df974a196629, backend opencode, description coverage 80.1%;
122 curated nodes cover the Cython/C++ core (ADR-0008).

## Verification Checklist

- [ ] `shap.TreeExplainer(model).shap_values(X)` runs on a fitted xgboost model
- [ ] QR rows cite source files resolvable in the shap graph
