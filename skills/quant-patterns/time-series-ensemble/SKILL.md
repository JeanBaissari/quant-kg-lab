---
name: quant-time-series-ensemble
description: "Use when combining multiple time series forecasting approaches — SARIMAX, GARCH, and darts models — into an ensemble for more robust predictions."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [statsmodels-tsa, arch-forecast, arch-volatility, darts-models, pandas-ts, numpy-core]
tags: [quantitative-finance, time-series, forecasting, ensemble, SARIMAX, GARCH, workflow]
related_skills: [statsmodels-tsa, arch-forecast, arch-volatility, darts-models, pandas-ts, numpy-core]
target_version: cross-lib
---

# Quant Time Series Ensemble (statsmodels + darts + arch)

Single-model forecasts are fragile. This playbook chains three families — statistical (SARIMAX),
volatility (GARCH), and flexible (darts ARIMA/Ensemble) — into a forecast ensemble that is robust
to model misspecification and regime shifts.

## Steps

1. **Prepare the return series** — `pandas-ts`: clean, stationary daily returns with a
   DatetimeIndex. Check stationarity (ADF/KPSS) before any modelling.
   ```python
   import pandas as pd
   ret = prices.pct_change().dropna()
   ```
2. **Fit a SARIMAX model** — `statsmodels-tsa`:
   ```python
   from statsmodels.tsa.statespace.sarimax import SARIMAX
   res = SARIMAX(ret, order=(1,0,1), seasonal_order=(1,0,1,5)).fit(disp=False)
   sarimax_fc = res.forecast(steps=20)     # tsa/statespace/sarimax.py:L37
   ```
   *Citation*: `statsmodels/tsa/statespace/sarimax.py:L37`
3. **Fit a GARCH volatility forecast** — `arch-forecast`: model the variance dynamics
   separately; GARCH(1,1) with StudentT is the baseline.
   ```python
   from arch import arch_model
   garch = arch_model(ret * 100, vol="GARCH", p=1, q=1, dist="StudentT").fit(disp="off")
   vol_fc = np.sqrt(garch.forecast(horizon=20).variance.iloc[-1])  # univariate/base.py:L993
   ```
   *Citation*: `arch/univariate/base.py:L993`
4. **Fit a darts model** — `darts-models`: ARIMA or NaiveDrift as a second statistical
   perspective; darts handles multivariate covariates natively.
   ```python
   from darts.models import ARIMA, NaiveDrift
   model = ARIMA(p=1, d=0, q=1)
   model.fit(ts)
   fc_darts = model.predict(n=20)           # models/forecasting/arima.py:L32
   ```
   *Citations*: `darts/models/forecasting/arima.py:L32`, `darts/models/forecasting/baselines.py:L123`
5. **Combine into an ensemble** — weight by inverse AIC/BIC or by out-of-sample RMSE on a
   validation window. A simple average often outperforms the best single model.
   ```python
   ensemble_fc = (w1 * sarimax_fc.values + w2 * darts_fc + w3 * ret.mean()) / (w1+w2+w3)
   ```
6. **Cross-validate the ensemble** — rolling-origin evaluation: re-fit every K periods, compare
   ensemble RMSE/MAE against each component.

## Pitfalls

1. **Stationarity is a gate** — SARIMAX and GARCH both assume stationarity. Modelling non-stationary
   levels produces meaningless forecasts. Always ADF-test the input series.
2. **Lookahead bias** — fitting the ensemble weights on the full sample leaks future information.
   Compute weights on a rolling training window only.
3. **Horizon mismatch** — SARIMAX forecasts levels of the input series; GARCH forecasts variance.
   They operate on different targets — do not average them directly without mapping to a common
   metric (e.g., both as return predictions).
4. **Model selection overfitting** — comparing too many model variants on a single validation window
   reintroduces in-sample bias. Use a holdout test period that no model or weight was tuned on.

## Composed Skills & Bridges

| Stage | Skill | Bridge (relation) |
|-------|-------|-------------------|
| stationarity | `statsmodels-tsa` | ADF/KPSS gate |
| mean model | `statsmodels-tsa` | SARIMAX forecasts |
| vol model | `arch-volatility`, `arch-forecast` | GARCH variance forecasts |
| flexible | `darts-models` | ARIMA / NaiveDrift / EnsembleModel |
| ensemble | (this playbook) | weighted combination of forecasts |
| validation | `pandas-ts`, `numpy-core` | rolling-origin RMSE |

## Related Skills

- [[statsmodels-tsa]]
- [[arch-forecast]]
- [[arch-volatility]]
- [[darts-models]]
- [[pandas-ts]]
- [[numpy-core]]
