---
name: shap
description: "Use when working with shap — the model-explainability entry point. Router indexing the shap sub-skills; load the sub-skill for the layer you need."
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
- router
related_skills:
- shap-explainers
- shap-plots
- xgboost
- lightgbm
- scikit-learn
---

# shap

SHAP (Shapley additive explanations) for quant ML models — the interpretability
layer over the boosting/linear stack.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [explainers](explainers/SKILL.md) | Explainer variants, Explanation, maskers, TreeExplainer |
| [plots](plots/SKILL.md) | waterfall/beeswarm/force/bar/dependence plots |

## Common Patterns

- **Model validation**: SHAP values per feature across the universe — confirm factor
  directions match thesis.
- **Signal explainability**: TreeExplainer on the live xgboost/lightgbm model for each
  signal batch.

## Provenance

Graph: `knowledge_graphs/shap/.graphify/graph.json` — 1277 nodes · 1752 edges ·
108 communities · graphify @ df974a196629, backend opencode, description coverage 80.1%.

## Verification Checklist

- [ ] Router links resolve to the 2 module skills
- [ ] `related_skills` names resolve to real skills
