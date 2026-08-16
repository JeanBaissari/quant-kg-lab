---
name: statsmodels-statespace
description: "Use when working with statsmodels state-space models \u2014 MLEModel,\
  \ MLEResults, Initialization, and news/impact analysis."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: statsmodels/statsmodels
source_commit: 179d1f4df4164c94c69256fc9436d578a1beb163
extraction_date: 2026-08-12
graph:
  nodes: 11616
  edges: 33529
  community_count: 638
  graph_hash: 22b3083cca514704
tags:
- statsmodels
- statespace
- kalman
related_skills:
- statsmodels
- statsmodels-core
- statsmodels-tsa
---

# statsmodels.statespace

State-space (Kalman-filter) modelling: `MLEModel` for custom specifications,
`MLEResults` with smoothing/filtering output, and `Initialization` for state
priors — the engine behind SARIMAX and structural models.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Initialization` | `tsa/statespace/initialization.py:L17` | State initialization policies (stationary, diffuse, known) |
| `MLEModel` | `tsa/statespace/mlemodel.py:L92` | Base maximum-likelihood state-space model — subclass to define your system |
| `MLEResults` | `tsa/statespace/mlemodel.py:L2686` | Filtered/smoothed results: states, covariances, forecasts |
| `NewsResults` | `tsa/statespace/news.py:L17` | News/impact decomposition of forecast revisions |

## Common Patterns

- **Custom model**: subclass `MLEModel`, implement `update()` + `start_params` — the
  general state-space framework.
- **Filtering vs smoothing**: `res.filtered_state` vs `res.smoothed_state` — smoothed uses
  all data; filtered is causal.
- **Forecast updates**: `NewsResults` decomposes how new observations revise the forecast.

## Pitfalls

- **Identification**: unidentifiable systems give flat likelihoods — check parameter
  covariance conditioning.
- **Initialization**: diffuse initialization is common for non-stationary states; wrong
  priors inflate early-period variance.

## Provenance

Graph: `knowledge_graphs/statsmodels/.graphify/graph.json` — 11616 nodes · 33529 edges ·
638 communities · graphify @ 179d1f4df416, backend opencode, description coverage 82.2%.

## Verification Checklist

- [ ] A custom `MLEModel` subclass fits and produces smoothed states
