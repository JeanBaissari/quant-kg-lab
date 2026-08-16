---
name: arch-forecast
description: "Use when forecasting with arch models \u2014 forecast()/rolling_forecast,\
  \ variance vs mean forecasts, analytic/simulation/bootstrap methods, and ARCHModelForecast\
  \ result objects."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: bashtage/arch
source_commit: 704bb70e48372e3ccccdde7da379811657ad0224
extraction_date: 2026-08-12
graph:
  nodes: 1367
  edges: 3900
  community_count: 135
  graph_hash: e3f8bcd939a66a6d
tags:
- arch
- forecast
- volatility
- garch
- risk
related_skills:
- arch
- arch-volatility
- arch-unitroot
- statsmodels-tsa
- pandas-ts
- numpy-core
target_version: '8.0.0 (dev: after 8.0.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `arch` ahead of the latest PyPI release (8.0.0 (dev: after 8.0.0)). Some APIs may not exist in your installed version.

# arch.forecast

Forecasting from fitted ARCH-family models: `res.forecast()` returns an
`ARCHModelForecast` with variance/mean forecasts by method (analytic,
simulation, bootstrap); `rolling_forecast()` walks a horizon across the sample
for out-of-sample validation.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `.forecast()` | `univariate/base.py:L993` | Fit-result forecast — horizon + method; returns ARCHModelForecast |
| `ARCHModelForecast` | `univariate/base.py:L2161` | Forecast result: `.variance`, `.mean` DataFrame indexed by horizon |
| `ARCHModelForecastSimulation` | `univariate/base.py:L2094` | Simulation-based forecast result (path/simulated draws) |
| `.rolling_forecast()` | `univariate/base.py:L1446` | Rolling-window forecast — out-of-sample validation walk |
| `_analytic_forecast()` | `univariate/volatility.py:L386` | Analytic variance forecast (closed form for GARCH family) |
| `_simulation_forecast()` | `univariate/volatility.py:L423` | Simulation-based variance forecast (future shocks sampled) |
| `_bootstrap_forecast()` | `univariate/volatility.py:L471` | Bootstrap-based forecast (resampled standardized residuals) |
| `VarianceForecast` | `univariate/volatility.py:L158` | Variance forecast object — `.forecasts()` / `.forecast_paths()` |
| `.forecasts()` | `univariate/volatility.py:L187` | Variance forecast values by horizon |
| `.forecast_paths()` | `univariate/volatility.py:L192` | Simulated variance paths (for VaR/ES scenario analysis) |
| `_one_step_forecast()` | `univariate/volatility.py:L337` | Recursive one-step-ahead variance forecast |
| `.forecast()` (mean) | `univariate/mean.py:L955` | Mean forecast — AR terms projected forward |

## Common Patterns

- **Volatility forecast**:
  ```python
  res = arch_model(returns, vol="GARCH", p=1, q=1).fit(disp="off")
  fc = res.forecast(horizon=5, method="analytic")
  fc.variance  # h-step-ahead variance per row
  ```
- **One-day-ahead VaR**: `vol = np.sqrt(fc.variance.iloc[-1, 0])` → `VaR = z_alpha * vol`.
- **Method choice**: `analytic` = closed-form GARCH variance; `simulation`
  and `bootstrap` give full paths (`forecast_paths()`) for ES/quantile work —
  use them when you need the whole distribution, not just the mean.
- **Rolling validation**: `res.rolling_forecast(horizon=1, method="analytic")`
  — compare forecast volatility vs realized |returns| out-of-sample.
- **Forecast to risk layer**: variance forecasts feed position sizing
  (vol-targeting), pyfolio perf reporting, and stress-test overlays.

## Pitfalls

- **Variance vs mean**: `fc.variance` is the volatility-process forecast;
  `fc.mean` requires mean-model terms (AR/constant) — don't confuse the two.
- **Horizon index**: forecasts are indexed by the last in-sample date with
  horizon columns h.1, h.2, … — `.iloc[-1, 0]` is the first step ahead.
- **Simulation seed**: simulation/bootstrap forecasts are stochastic — set
  `random_state` in fit/forecast for reproducible paths.
- **Wrong horizon alignment**: `.forecast(horizon=1)` on a daily series is one
  step (usually one day) — for monthly aggregation re-fit at that frequency.
- **ARCH-in-mean forecasts**: `ARCHModelForecast.mean` includes the mean term
  recursion; ignore it when the model is pure volatility.

## Provenance

Graph: `knowledge_graphs/arch/.graphify/graph.json` — 1367 nodes · 3900 edges ·
135 communities · graphify @ pin, backend opencode, description coverage 94.3%.

## Verification Checklist

- [ ] `res.forecast(horizon=5, method="analytic").variance` returns a horizon × n index frame
- [ ] `res.rolling_forecast(1)` runs over a fitted GARCH
- [ ] QR rows cite `univariate/*.py` files resolvable in the arch graph
