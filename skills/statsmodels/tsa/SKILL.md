---
name: statsmodels-tsa
description: "Use when forecasting time series with statsmodels — ARIMA/SARIMAX, ExponentialSmoothing, and the arima process tools."
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
target_version: '0.14.6 (dev: after 0.14.6)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `statsmodels` ahead of the latest PyPI release (0.14.6 (dev: after 0.14.6)). Some APIs may not exist in your installed version.

# statsmodels.tsa

Classical time-series modelling and forecasting: ARIMA/SARIMAX via the
`SARIMAX` model (statespace-backed) and `ARIMA` (the modern specification API),
plus `ExponentialSmoothing` for trend/seasonal baselines. This skill covers the
**user-facing surface**: the model classes you instantiate, the results objects
you interrogate, and the stationarity/order-selection tools that gate a fit.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `SARIMAX` | `tsa/statespace/sarimax.py:L37` | Full ARIMA/SARIMAX model (statespace): order + seasonal_order + exog; `.fit()`, `.forecast()`, `.predict()` |
| `SARIMAXResults` | `tsa/statespace/sarimax.py:L1817` | Fitted results: `.params`, `.aic`/`.bic`, `.forecast(steps, exog)`, `.plot_diagnostics()` |
| `ARIMA` | `tsa/arima/model.py:L26` | Modern specification-based ARIMA (`sm.tsa.arima.ARIMA`) — replaces the legacy `ARMA`/`ARIMA` classes |
| `ARIMAResults` | `tsa/arima/model.py:L509` | Modern-API results: `.params`, `.predict(start, end)`, `.fittedvalues`, `.summary()` |
| `ExponentialSmoothing` | `tsa/holtwinters/model.py:L116` | Triple exponential smoothing — `trend=`, `seasonal=`, `seasonal_periods=`, `damped_trend=` |
| `SimpleExpSmoothing` | `tsa/holtwinters/model.py:L1415` | Single exponential smoothing baseline — `smoothing_level=` |
| `HoltWintersResults` | `tsa/holtwinters/results.py:L19` | Fit results: `.level`, `.trend`, `.season`, `.fittedvalues`, `.forecast(h)` |
| `ArmaProcess` | `tsa/arima_process.py:L677` | ARMA process simulation and ACV/PSD analytics — `generate_sample()`, `impulse_response()` |
| `arma_impulse_response()` | `tsa/arima_process.py:L322` | MA-representation impulse response coefficients for an ARMA process |
| `adfuller()` | `tsa/stattools/_stattools.py:L225` | ADF unit-root test — stationarity gate before fitting an ARIMA family model |
| `grangercausalitytests()` | `tsa/stattools/_stattools.py:L2353` | Pairwise Granger causality across lags for two series |

## Common Patterns

- **SARIMAX fit → forecast**:
  ```python
  import statsmodels.api as sm
  res = sm.tsa.SARIMAX(y, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12),
                       exog=exog).fit()
  fc = res.forecast(steps=12, exog=exog_future)   # out-of-sample
  ```
  `predict(start, end)` covers in-sample + out-of-sample with `dynamic=True`
  for multi-step-ahead in-sample evaluation.
- **Modern ARIMA API**: `sm.tsa.arima.ARIMA(y, order=(p, d, q)).fit()` — the
  spec/params pipeline under the hood; results expose the same `predict`/`summary`
  surface. Prefer it for new code over the legacy `ARIMA`/`ARMA` classes.
- **Exponential smoothing baseline**: `ExponentialSmoothing(y, trend='add',
  seasonal='add', seasonal_periods=12, damped_trend=True).fit()` — compare AIC vs
  the plain-Holt and additive-seasonal variants. `SimpleExpSmoothing(y).fit()`
  is the flat forecast benchmark; add `smoothing_level` to control memory.
- **Stationarity gate**: run `adfuller(y)` and require a rejected unit root
  before choosing `d`; pair with the KPSS test when the series is borderline.
- **Order selection by AIC**: grid-search `(p, q)` over a small range
  (`arima_select_order`-style loop), refitting `SARIMAX(order=(p, d, q), ...)`
  for each candidate and keeping the lowest AIC/BIC — see Pitfalls on overfitting.
- **Forecast with intervals**: `res.get_forecast(steps=12)` returns a
  `PredictionResults` with `.predicted_mean` and `.conf_int(alpha=0.05)` — report
  bands, not points; `res.forecast(steps)` is the bare-mean convenience wrapper.
- **Simulation / Monte-Carlo**: `ArmaProcess(ar, ma)` with
  `generate_sample(nsample)` for synthetic ARMA series and
  `arma_impulse_response(ar, ma, nobs)` for the structural impulse-response shape.
- **Diagnostics before trusting forecasts**: `res.plot_diagnostics()` — residual
  normality/ACF panels; a failing Ljung-Box on `res.resid` means the order is
  under-parameterized.

## Pitfalls

- **Exogenous alignment**: `exog` must be indexed like `y` and provided for every
  forecast step — a future-exog gap silently produces NaN forecasts. Align on the
  same frequency and reindex before fitting.
- **Frequency setting**: set a `DatetimeIndex` frequency before fitting
  (`y.index.freq = 'MS'` or `pd.date_range(..., freq=...)`). Missing/inferred
  frequency breaks `seasonal_order`, forecast indexing, and out-of-sample periods.
- **Order selection via AIC**: lower AIC is not automatically better — with few
  observations the grid can pick overfit orders; cap `(p, q)` and cross-validate
  out-of-sample before trusting the AIC-minimal order.
- **Differencing vs `d`**: `SARIMAX(order=(p, d, q))` differences *internally*;
  if you pre-difference the series yourself, set `d=0` or you double-difference.
  Check `res.resid` stationarity rather than assuming `d` fixed the problem.
- **Forecast horizon**: statespace forecasts converge to the mean/trend and
  standard errors widen with horizon — bound forecast windows and report intervals
  (`get_forecast(...).conf_int()`), not point values.
- **SimpleExpSmoothing has no seasonality**: it models a flat level only — using it
  on seasonal data produces lagged, biased forecasts; use `ExponentialSmoothing`
  with `seasonal` instead.
- **Seasonal period must divide the data length**: `seasonal_periods=12` on a
  series with fewer than ~2 full cycles fits garbage — check the sample covers
  the seasonality you claim (12 or 52 for monthly/weekly).
- **Legacy vs modern classes**: the old `sm.tsa.ARIMA`/`ARMA` classes are legacy;
  the modern `sm.tsa.arima.ARIMA` spec API and `SARIMAX` are maintained paths —
  match the import to the model family you actually want.

## Provenance

Graph: `knowledge_graphs/statsmodels/.graphify/graph.json` — 11616 nodes · 33529 edges ·
638 communities · graphify @ 179d1f4df416, backend opencode, description coverage 82.2%.

## Verification Checklist

- [ ] `sm.tsa.SARIMAX(y, order=(1,1,1)).fit().forecast(5)` runs
- [ ] `sm.tsa.ExponentialSmoothing(y, trend='add', seasonal='add', seasonal_periods=12).fit().forecast(5)` runs
- [ ] `sm.tsa.arima.ARIMA(y, order=(1,1,1)).fit()` produces an `ARIMAResults`
- [ ] QR rows cite `tsa/*.py:L*` resolvable in the statsmodels graph
