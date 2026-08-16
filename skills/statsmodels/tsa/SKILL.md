---
name: statsmodels-tsa
description: "Use when forecasting time series with statsmodels \u2014 ARIMA/SARIMAX,\
  \ ExponentialSmoothing, and the arima process tools."
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
- timeseries
- arima
related_skills:
- statsmodels
- statsmodels-core
- statsmodels-statespace
- pandas-ts
---

# statsmodels.tsa

Classical time-series modelling and forecasting: ARIMA/SARIMAX via the
`SARIMAX` model (statespace-backed) and `ARIMA` (the modern specification API),
plus `ExponentialSmoothing` for trend/seasonal baselines.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `SARIMAXSpecification` | `tsa/arima/specification.py:L23` | Builds the SARIMAX model spec from order/seasonal terms |
| `SARIMAXParams` | `tsa/arima/params.py:L15` | Parameter container for ARIMA-family models |
| `ArmaProcess` | `tsa/arima_process.py:L677` | ARMA process simulation and ACV/PSD analytics |
| `ARMAEstimationResult` | `tsa/arima/estimators/_base.py:L11` | Estimation result container (params, cov, fit stats) |
| `tsa/arima/estimators/` | Estimators: statespace, conditional-sum-of-squares, etc. |

## Common Patterns

- **SARIMAX**: `sm.tsa.SARIMAX(y, order=(1,1,1), seasonal_order=(1,1,1,12)).fit()` →
  `res.forecast(steps)`, `res.summary()`.
- **Modern ARIMA**: `sm.tsa.arima.ARIMA(y, order=(1,1,1)).fit()` — spec/params API above.
- **Baseline**: `sm.tsa.ExponentialSmoothing(y, trend='add', seasonal='add', seasonal_periods=12).fit()`.
- **Diagnostics**: `res.plot_diagnostics()` — residual normality/ACF before trusting forecasts.

## Pitfalls

- **Differencing**: `order=(p,d,q)` — the `d` term is internal; verify stationarity of the
  original series first (arch.unitroot).
- **Seasonality**: wrong `seasonal_order` inflates params — use AIC to compare.
- **Forecast horizon**: statespace forecasts degrade with horizon; bound them.

## Provenance

Graph: `knowledge_graphs/statsmodels/.graphify/graph.json` — 11616 nodes · 33529 edges ·
638 communities · graphify @ 179d1f4df416, backend opencode, description coverage 82.2%.

## Verification Checklist

- [ ] `sm.tsa.SARIMAX(y, order=(1,1,1)).fit().forecast(5)` runs
