---
name: shap-plots
description: "Use when visualizing SHAP explanations — waterfall, summary/beeswarm, force, bar, and dependence plots."
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
- plots
- visualization
related_skills:
- shap
- shap-explainers
---

# shap.plots

Explanation visualization: `waterfall_plot` (single prediction decomposition),
`summary_plot`/`beeswarm` (global feature importance), `force_plot`, `bar_plot`,
and `dependence_plot` (feature interaction).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `waterfall_plot()` | `plots/_waterfall.py` | Base value → prediction, per-feature contributions stacked |
| `beeswarm()` | `plots/_beeswarm.py` | Global summary: feature importance with value distribution |
| `force_plot()` | `plots/_force.py` | Additive force layout for single or multiple rows |
| `bar_plot()` | `plots/_bar.py` | Mean |SHAP| bar summary |
| `dependence_plot()` | `plots/_dependence.py` | Feature value vs SHAP value (interaction view) |
| `plots/resources/` | `plots/resources/` | Bundled JS/logo assets for interactive force plots |

## Common Patterns

- **Single explanation**: `shap.waterfall_plot(explainer(X)[0])` — the standard drill-down.
- **Global view**: `shap.beeswarm(explainer(X))` — importance + direction in one plot.
- **Interactions**: `shap.dependence_plot("feature_a", shap_values, X, interaction_index="feature_b")`.

## Pitfalls

- **Plot backends**: waterfall/beeswarm are matplotlib; `force_plot` in notebooks uses HTML
  (resources bundled in the package).
- **Explanation vs raw arrays**: newer shap prefers `Explanation` objects — pass them, not
  bare `shap_values` arrays, for full plot support.

## Provenance

Graph: `knowledge_graphs/shap/.graphify/graph.json` — 1277 nodes · 1752 edges ·
108 communities · graphify @ df974a196629, backend opencode, description coverage 80.1%.

## Verification Checklist

- [ ] `shap.waterfall_plot(exp[0])` and `shap.beeswarm(exp)` render
