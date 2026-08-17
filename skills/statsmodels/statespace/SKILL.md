---
name: statsmodels-statespace
description: "Use when working with statsmodels state-space models — SARIMAX, DynamicFactor, UnobservedComponents, VARMAX, and custom MLEModel specifications with the Kalman filter."
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
  graph_hash: 8d751b1519a13938
tags:
- statsmodels
- statespace
- kalman
related_skills:
- statsmodels
- statsmodels-core
- statsmodels-tsa
target_version: '0.14.6 (dev: after 0.14.6)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `statsmodels` ahead of the latest PyPI release (0.14.6 (dev: after 0.14.6)). Some APIs may not exist in your installed version.

# statsmodels.statespace

State-space (Kalman-filter) modelling. The module ships **ready-to-use model
classes** — `SARIMAX`, `DynamicFactor`, `UnobservedComponents`, `VARMAX` — plus
`MLEModel` for custom specifications, with `MLEResults` exposing filtering,
smoothing, forecasting, and news/impact analysis.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `SARIMAX` | `tsa/statespace/sarimax.py:L37` | ARIMA/SARIMAX with seasonal + exogenous terms — the workhorse statespace model |
| `SARIMAXResults` | `tsa/statespace/sarimax.py:L1817` | Fitted output: `.filtered_state`, `.smoothed_state`, `.forecast()`, `.impulse_responses()` |
| `DynamicFactor` | `tsa/statespace/dynamic_factor.py:L32` | Dynamic factor models — common factors driving a panel of series |
| `UnobservedComponents` | `tsa/statespace/structural.py:L47` | Structural models: local level, local linear trend, seasonal, cycle (`level=`, `trend=`, `seasonal=`, `cycle=`) |
| `VARMAX` | `tsa/statespace/varmax.py:L36` | Vector ARMA with exogenous regressors (`order=`, `trend=`) |
| `VARMAXResults` | `tsa/statespace/varmax.py:L870` | Multivariate results: `.forecast()`, `.impulse_responses()`, `.plot_irf()` |
| `MLEModel` | `tsa/statespace/mlemodel.py:L92` | Base maximum-likelihood state-space model — subclass to define your own system |
| `MLEResults` | `tsa/statespace/mlemodel.py:L2686` | Filtered/smoothed results: states, covariances, forecasts, `.impulse_responses()` |
| `Initialization` | `tsa/statespace/initialization.py:L17` | State initialization policies — stationary, diffuse, known, approximate-diffuse |
| `NewsResults` | `tsa/statespace/news.py:L17` | News/impact decomposition of forecast revisions between two models |
| `SimulationSmoothResults` | `tsa/statespace/simulation_smoother.py:L342` | Simulation-smoothed state draws — for posterior/path analysis |

## Common Patterns

- **SARIMAX quick path**: `sm.tsa.SARIMAX(y, order=(1,1,1),
  seasonal_order=(1,1,1,12)).fit()` then `res.get_forecast(steps=12)` — the
  highest-level entry point to the statespace machinery (see `statsmodels-tsa`).
- **Dynamic factor for correlated panels**: `DynamicFactor(endog, k_factors=1,
  factor_order=2).fit()` — latent common factor + idiosyncratic terms; useful for
  asset universes or macro panels before feeding factors downstream.
- **Trend decomposition with UnobservedComponents**: `UnobservedComponents(y,
  level='local linear trend', seasonal=12, cycle=True).fit()` — separates trend,
  seasonal, and cycle components; inspect `.level.smoothed`, `.seasonal.smoothed`.
- **Multivariate statespace**: `sm.tsa.statespace.VARMAX(df, order=(1, 0)).fit()`
  — a VAR in statespace form; `res.impulse_responses(10)` traces shock propagation
  across series (contrast with `statsmodels-vector-ar`).
- **Shock propagation**: `res.impulse_responses(steps=10)` (method on `MLEResults`
  subclasses) — one-shock-at-a-time response paths with error bands.
- **Custom model**: subclass `MLEModel`, implement `update()` + `start_params`
  (+ optionally `transform_params`), then `.fit(disp=False)` — the general
  framework under every prebuilt class above.
- **Filtering vs smoothing**: `res.filtered_state` is causal (uses data up to t);
  `res.smoothed_state` uses the full sample — use smoothed for attribution,
  filtered for online/rolling evaluation.
- **Simulation smoothing**: `res.simulation_smoother().simulate(nsimulations)`
  draws posterior state paths — useful for uncertainty bands on latent states
  (the machinery behind `SimulationSmoothResults`).
- **News decomposition**: fit two nested models (e.g. with/without a new
  observation) and compare via `NewsResults` to attribute forecast revisions to
  specific data releases — `NewsResults.summary()` tables the per-observation
  contributions.

## Pitfalls

- **Identification**: unidentifiable systems give flat likelihoods — check
  parameter covariance conditioning and start from multiple initial values.
- **Initialization**: diffuse initialization is common for non-stationary states;
  wrong priors inflate early-period variance — use `res.filter_results.converged`
  to verify the filter settled.
- **Exogenous alignment**: `exog` must align with the endog index and be supplied
  for all forecast periods — a missing future `exog` silently truncates or NaN-fills
  the forecast horizon.
- **Frequency setting**: statespace models infer periods from the index — set an
  explicit `freq` on the `DatetimeIndex` before fitting or seasonal/forecast
  indexing degrades silently.
- **Diffuse vs stationary init**: mixing diffuse initialization for non-stationary
  states with stationary initialization elsewhere can create flat likelihood
  directions — initialize only truly non-stationary states as diffuse.
- **UnobservedComponents parameter explosion**: `level`, `trend`, `seasonal`, and
  `cycle` each add stochastic states — combining all of them on short series
  produces unidentified components; start minimal (local level) and add one at a
  time, comparing log-likelihood/AIC.
- **DynamicFactor factor count**: `k_factors` is a specification choice, not a fit
  output — compare 1 vs 2+ factors by likelihood and check idiosyncratic variances
  for signs of an over- or under-extracted factor.
- **VARMAX vs VAR**: `VARMAX(order=(p, 0))` with no MA part is equivalent to a VAR
  but in statespace form; don't fit both and compare AICs directly — the statespace
  estimation routine differs from `statsmodels-vector-ar`'s OLS/GLS estimator.

## Provenance

Graph: `knowledge_graphs/statsmodels/.graphify/graph.json` — 11616 nodes · 33529 edges ·
638 communities · graphify @ 179d1f4df416, backend opencode, description coverage 82.2%.

## Verification Checklist

- [ ] A custom `MLEModel` subclass fits and produces smoothed states
- [ ] `sm.tsa.statespace.DynamicFactor(df, k_factors=1, factor_order=2).fit()` runs
- [ ] `res.impulse_responses(10)` returns a response path for a fitted statespace model
- [ ] QR rows cite `tsa/statespace/*.py:L*` resolvable in the statsmodels graph
