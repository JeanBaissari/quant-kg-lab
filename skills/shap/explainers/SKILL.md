---
name: shap-explainers
description: "Use when computing SHAP values with shap \u2014 Explainer (Tree/Linear/Kernel/Deep),\
  \ Explanation objects, and maskers."
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
  graph_hash: 2ef1103a6cfaf03b
tags:
- shap
- explainability
- shapley
related_skills:
- shap
- shap-plots
- xgboost-core
- lightgbm-core
target_version: '0.52.0 (dev: after 0.52.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `shap` ahead of the latest PyPI release (0.52.0 (dev: after 0.52.0)). Some APIs may not exist in your installed version.

# shap.explainers

SHAP value computation: `Explainer` (with `TreeExplainer`/`LinearExplainer`/
`KernelExplainer`/`DeepExplainer` variants) returns `Explanation` objects —
values, base_values, and data ready for plotting.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Explainer` | `explainers/_explainer.py:L22` | Unified explainer entry — auto-selects the variant from the model type |
| `Explanation` | `_explanation.py:L96` | Output object: `values`, `base_values`, `data`, `feature_names`; carries `.plot()` |
| `Masker` | `maskers/_masker.py:L14` | Input masking strategies (Independent, Tabular, Partition) for the explainer |
| `Model` | `models/_model.py:L12` | Model wrapper abstraction (callable/ensemble adapters) |
| `TreeExplainer` | `explainers/_tree.py:L141` | Exact SHAP for tree ensembles (xgboost/lightgbm/sklearn) — fast, model-structure-aware |
| `KernelExplainer` | `explainers/_kernel.py:L41` | Model-agnostic SHAP — any callable, slower, needs background data |
| `LinearExplainer` | `explainers/_linear.py:L20` | Exact SHAP for linear models (incl. correlation-aware via `feature_perturbation`) |
| `DeepExplainer` | `explainers/_deep/__init__.py:L7` | Deep-learning SHAP (TensorFlow/PyTorch) via DeepLIFT-style backprop |
| `TreeExplainer.shap_values()` | `explainers/_tree.py:L617` | Per-row SHAP values for tree ensembles |
| `TreeExplainer.shap_interaction_values()` | `explainers/_tree.py:L801` | Pairwise interaction SHAP — feature × feature |
| `TreeExplainer.assert_additivity()` | `explainers/_tree.py:L937` | Verify values sum to prediction — built-in correctness check |
| `KernelExplainer.shap_values()` | `explainers/_kernel.py:L229` | Model-agnostic SHAP values |
| `LinearExplainer.shap_values()` | `explainers/_linear.py:L428` | Exact linear SHAP values |

## Common Patterns

- **Tree models**: `shap.TreeExplainer(model).shap_values(X)` — exact and fast for
  xgboost/lightgbm/sklearn trees (pass `tree_limit` for ensemble length).
- **Any model**: `shap.Explainer(model).shap_values(X)` — auto-dispatch.
- **Explanation object**: `exp = explainer(X)` → `exp.base_values`, `exp.values` —
  then `shap.waterfall_plot(exp[0])`.
- **Interaction**: `TreeExplainer(model, feature_perturbation="interventional")`
  with `shap_values(..., interactions=True)`.
- **Explainer selection matrix**: Tree (exact, fast, trees only) → Kernel
  (any model, background-dependent, slow) → Linear (linear models, exact) →
  Deep (NNs). Use `shap.Explainer` for auto-dispatch, then pin the variant
  once chosen.
- **Additivity check**: `explainer.assert_additivity()` after a TreeExplainer
  run — catches model/version mismatches (e.g. early-stopped ensembles).

## Pitfalls

- **Background data**: kernel/partition explainers need a background dataset — small,
  representative samples only.
- **Tree limit**: boosted ensembles: use `tree_limit` matching the deployed model; defaults
  may differ.
- **Performance**: TreeExplainer is O(leaves × features) per row; for large universes batch
  the `shap_values` calls.
- **Deep vs Gradient**: DeepExplainer is approximate (DeepLIFT-based); for exact values on
  trees use TreeExplainer — never use Deep on tree ensembles.
- **Model wrapper**: passing a raw sklearn/xgboost object works via the built-in
  `Model` adapters; custom classes need `Model(..., model_input=...)` — a silent
  fallback to KernelExplainer is a performance trap.

## Provenance

Graph: `knowledge_graphs/shap/.graphify/graph.json` — 1277 nodes · 1752 edges ·
108 communities · graphify @ df974a196629, backend opencode, description coverage 80.1%;
122 curated nodes cover the Cython/C++ core (ADR-0008).

## Verification Checklist

- [ ] `shap.TreeExplainer(model).shap_values(X)` runs on a fitted xgboost model
- [ ] `explainer.assert_additivity()` passes on a small batch
- [ ] QR rows cite source files resolvable in the shap graph
