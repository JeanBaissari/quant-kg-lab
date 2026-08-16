---
name: darts-timeseries
description: "Use when working with darts TimeSeries containers and forecasting metrics\
  \ \u2014 series construction/alignment, frequency handling, imputation, and the\
  \ metric family (MAPE/SMAPE/MASE/RMSE/quantile)."
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
  graph_hash: a7e60646dbde36e7
tags:
- darts
- timeseries
- metrics
- preprocessing
related_skills:
- darts
- darts-models
- darts-backtesting
- pandas-core
- empyrical-stats
- quantstats-stats
target_version: '0.46.1 (dev: after 0.46.1)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `darts` ahead of the latest PyPI release (0.46.1 (dev: after 0.46.1)). Some APIs may not exist in your installed version.

# darts.timeseries + metrics

The `TimeSeries` container (frequency-aware, univariate/multivariate) and the
forecasting metric family — the evaluation surface for every forecast.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `TimeSeries` | `timeseries.py:L110` | The core series container — deg 194 hub |
| `.start_time()` | `timeseries.py:L1974` | First timestamp of the series |
| `.end_time()` | `timeseries.py:L1990` | Last timestamp of the series |
| `.copy()` | `timeseries.py:L2347` | Deep copy — avoid aliasing mutations |
| `.get_index_at_point()` | `timeseries.py:L2365` | Index lookup at a time point |
| `err()` | `metrics/metrics.py:L3010` | Element-wise error |
| `merr()` | `metrics/metrics.py:L138` | Mean error |
| `ae()` | `metrics/metrics.py:L226` | Absolute error |
| `mae()` | `metrics/metrics.py:L323` | Mean absolute error |
| `mse()` | `metrics/metrics.py:L765` | Mean squared error |
| `rmse()` | `metrics/metrics.py:L1114` | Root mean squared error |
| `mape()` | `metrics/metrics.py:L323` | Mean absolute percentage error |
| `mase()` | `metrics/metrics.py:L542` | Mean absolute scaled error — scale-free |
| `smape()` | `metrics/metrics.py:L138` | Symmetric MAPE |
| `quantile_loss()` | `metrics/metrics.py:L3010` | Pinball/quantile loss — interval quality |
| `coefficient_of_variation()` | `metrics/metrics.py:L2516` | CV of errors — scale-relative accuracy |

## Common Patterns

- **Series construction**: `TimeSeries.from_dataframe(df, time_col, value_cols)` /
  `from_values(np_array)` — the standard entry points.
- **Frequency discipline**: series carry a frequency — `pd.date_range`-style index
  alignment; darts validates monotonicity.
- **Imputation**: missing values inside a series break forecasting — impute before
  fit (`fillna`/interpolation in the container or upstream pandas).
- **Metric choice**: `mape` (interpretable, explodes near zero), `mase`
  (scale-free, robust), `rmse` (squared sensitivity), `quantile_loss` (interval
  quality for conformal/quantile models).
- **Comparison set**: always compare a model against the naive baseline with the SAME
  metric — relative improvement, not absolute numbers.
- **Multivariate**: `TimeSeries` holds multiple components; metrics average over
  components by default (check `componentwise`).

## Pitfalls

- **MAPE near zero**: percentage errors blow up when actuals are near zero —
  prefer `mase`/`smape` for returns-like series.
- **Frequency mismatch**: forecast series and actuals must share the frequency —
  `historical_forecasts` validates this and silently trims otherwise.
- **NaN leakage**: imputing the FULL series before the train/test split leaks the
  test window — impute on the train portion only (or use a causal imputer).
- **TimeSeries is not a DataFrame**: indexing differs (`.values()` returns
  (n, n_components) not a 1-D array) — adapt slicing habits.
- **Metric inputs**: metrics take TimeSeries (or arrays) — mixing shapes raises
  alignment errors; use `align()` first.

## Provenance

Graph: `knowledge_graphs/darts/.graphify/graph.json` — 3954 nodes · 8240 edges ·
245 communities · graphify @ 080b5340366b, backend opencode, description coverage 85.2%.

## Verification Checklist

- [ ] `TimeSeries.from_dataframe(df, time_col, value_cols)` builds a series
- [ ] `mape(actual, pred)` / `mase(actual, pred)` compute on aligned series
- [ ] QR rows cite `timeseries.py:L1`/`metrics/metrics.py:L1` files resolvable in the darts graph
