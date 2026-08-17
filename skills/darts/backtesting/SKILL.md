---
name: darts-backtesting
description: "Use when validating darts forecasts \u2014 historical_forecasts rolling\
  \ out-of-sample evaluation, backtest-driven model selection, and grid search over\
  \ forecasting parameters."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: unit8co/darts
source_commit: 080b5340366b8df25e048f4cfd11ca99e3806e97
extraction_date: 2026-08-13
graph:
  nodes: 3954
  edges: 8240
  community_count: 245
  graph_hash: 5c5d8a76d0253ade
tags:
- darts
- backtesting
- historical-forecasts
- model-selection
related_skills:
- darts
- darts-models
- darts-timeseries
- quant-walk-forward-validation
- optuna-study
target_version: '0.46.1 (dev: after 0.46.1)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `darts` ahead of the latest PyPI release (0.46.1 (dev: after 0.46.1)). Some APIs may not exist in your installed version.

# darts.backtesting

Out-of-sample validation: `historical_forecasts()` walks the model forward across the
series producing rolling forecasts; metrics over those forecasts drive model selection
and grid search.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `.historical_forecasts()` | `models/forecasting/forecasting_model.py:L674` | Rolling out-of-sample forecasts — start, forecast_horizon, stride |
| `.supports_optimized_historical_forecasts()` | `models/forecasting/forecasting_model.py:L344` | Whether the model family has the fast path |
| `_historical_forecasts_sanity_checks()` | `models/forecasting/forecasting_model.py:L644` | Validation of start/horizon/stride arguments |
| `_check_optimizable_historical_forecasts()` | `models/forecasting/forecasting_model.py:L666` | Fast-path eligibility check |

## Common Patterns

- **The standard validation loop**:
  ```python
  forecasts = model.historical_forecasts(
      series, start=0.8, forecast_horizon=7, stride=1, retrain=True)
  ```
  — rolling 7-step-ahead forecasts over the last 20% of the series.
- **Backtest-driven selection**: score each candidate model with the same metric over
  the same `historical_forecasts` window — apples-to-apples.
- **Grid search**: `model.gridsearch(parameters, series, forecast_horizon=7,
  metric=mape)` — parameter sweep on the backtest, not a single train/test split.
- **Retrain discipline**: `retrain=True` (default) refits per step — expensive but
  honest; `retrain=False` only for cheap/fast models.
- **Stride**: `stride > 1` samples fewer evaluation points — faster, coarser
  confidence; `stride=1` is the full evaluation.
- **Purging/embargo**: align with `quant-walk-forward-validation` — the same
  leak-free OOS philosophy; darts' `start` fraction + horizon must respect the
  embargo window.

## Pitfalls

- **retrain cost**: deep models with `retrain=True` over a long series are
  computationally brutal — budget wall-clock first (a common hang).
- **start semantics**: `start=0.8` is a fraction of the series; `start` as a timestamp
  is also accepted — be explicit.
- **Optimized path**: `supports_optimized_historical_forecasts` is False for most
  deep models — the loop is the slow path; don't expect the fast one.
- **Horizon alignment**: For modern darts (≥0.40), torch-based models auto-regressively
  generate forecasts for horizons exceeding `output_chunk_length` — no truncation occurs.
  Only `predict_likelihood_parameters` is restricted to `output_chunk_length`. Older deep
  models without autoregressive support will truncate.
- **Metrics on partial horizons**: compare forecasts of the SAME horizon — mixing
  1-step and 7-step metrics across candidates is invalid.

## Provenance

Graph: `knowledge_graphs/darts/.graphify/graph.json` — 3954 nodes · 8240 edges ·
245 communities · graphify @ 080b5340366b, backend opencode, description coverage 85.2%.

## Verification Checklist

- [ ] `model.historical_forecasts(series, start=0.8, forecast_horizon=7)` runs
- [ ] `model.gridsearch(parameters, series, metric=mape)` returns best params
- [ ] QR rows cite `models/forecasting/forecasting_model.py:L1` resolvable in the darts graph
