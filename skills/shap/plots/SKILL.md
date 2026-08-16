---
name: shap-plots
description: "Use when visualizing SHAP explanations \u2014 waterfall, summary/beeswarm,\
  \ force, bar, and dependence plots."
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
  graph_hash: 56d741979f6b195b
tags:
- shap
- plots
- visualization
related_skills:
- shap
- shap-explainers
target_version: '0.52.0 (dev: after 0.52.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `shap` ahead of the latest PyPI release (0.52.0 (dev: after 0.52.0)). Some APIs may not exist in your installed version.

# shap.plots

Explanation visualization: `waterfall_plot` (single prediction decomposition),
`summary_plot`/`beeswarm` (global feature importance), `force_plot`, `bar_plot`,
and `dependence_plot` (feature interaction).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `waterfall_plot()` | `plots/_waterfall.py:L16` | Base value → prediction, per-feature contributions stacked |
| `beeswarm()` | `plots/_beeswarm.py:L40` | Global summary: feature importance with value distribution |
| `force_plot()` | `plots/_force.py:L30` | Additive force layout for single or multiple rows |
| `bar_plot()` | `plots/_bar.py:L22` | Mean |SHAP| bar summary |
| `dependence_plot()` | `plots/_scatter.py:L517` | Feature value vs SHAP value — at this pin a legacy alias of `dependence_legacy` (see `shap/__init__.py:L36`) |
| `decision_plot()` | `plots/_decision.py:L212` | Full additive decomposition across all rows — model-agnostic |
| `image_plot()` | `plots/_image.py:L27` | Image-model explanations — pixel/region attributions overlaid |
| `heatmap()` | `plots/_heatmap.py:L11` | Per-sample × feature heatmap of SHAP values |
| `embedding_plot()` | `plots/_embedding.py:L9` | SHAP values projected into an embedding space |
| `plots/resources/` | Bundled JS/logo assets for interactive force plots |

## Common Patterns

- **Single explanation**: `shap.waterfall_plot(explainer(X)[0])` — the standard drill-down.
- **Global view**: `shap.beeswarm(explainer(X))` — importance + direction in one plot.
- **Interactions**: `shap.dependence_plot("feature_a", shap_values, X, interaction_index="feature_b")`.
- **Portfolio of rows**: `shap.decision_plot(exp.base_values[0], exp.values[:20], X[:20])` —
  compare many predictions on one additive scale.
- **Model report**: `shap.summary_plot(exp, show=False)` → save fig → embed in a report;
  `bar_plot` for the top-k headline numbers.
- **Factor research**: beeswarm of the ML factor model + dependence plots per top
  feature — the explainability half of factor-importance work.

## Pitfalls

- **Plot backends**: waterfall/beeswarm are matplotlib; `force_plot` in notebooks uses HTML
  (resources bundled in the package).
- **Explanation vs raw arrays**: newer shap prefers `Explanation` objects — pass them, not
  bare `shap_values` arrays, for full plot support.
- **dependence_plot is a legacy alias at this pin**: use it for compatibility, but verify
  the output function against the installed shap version; new code can call the scatter
  backend directly.
- **Show vs save**: plotting functions call `plt.show()` by default — pass `show=False`
  and `plt.savefig`/`plt.close` in loops, or notebooks accumulate figures.
- **Base values in ensembles**: `exp.base_values` is the model average — with a background
  masker it may differ from the training mean; report the base value you plotted.

## Provenance

Graph: `knowledge_graphs/shap/.graphify/graph.json` — 1277 nodes · 1752 edges ·
108 communities · graphify @ df974a196629, backend opencode, description coverage 80.1%.

## Verification Checklist

- [ ] `shap.waterfall_plot(exp[0])` and `shap.beeswarm(exp)` render
- [ ] `shap.decision_plot(...)` renders over a small batch
- [ ] QR rows cite `plots/*.py` files resolvable in the shap graph
