---
name: quant-volatility-modelling
description: "Use when modelling and forecasting volatility — stationarity checks, GARCH-family fits, volatility/risk forecasts, and feeding variance paths into position sizing and risk reporting."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [arch-volatility, arch-forecast, arch-unitroot, statsmodels-tsa, pandas-ts, numpy-core]
tags: [quantitative-finance, volatility, garch, forecast, risk, workflow]
related_skills: [arch-volatility, arch-forecast, arch-unitroot, statsmodels-tsa, pandas-ts, numpy-core]
---

# Quant Volatility Modelling (returns → stationarity → GARCH → forecast → risk)

Volatility modelling answers "what will return dispersion be over the next h periods, and
what does that mean for risk limits?" — the risk layer under every position-size decision.
This playbook chains stationarity gates, ARCH-family estimation, horizon forecasts, and
risk metric conversion.

## Steps

1. **Prepare and gate the series** — `pandas-ts` + `arch-unitroot`: build a clean daily
   return series; run `ADF` (reject unit root) and `KPSS` (fail to reject stationarity)
   before any vol modelling.
2. **Estimate the volatility process** — `arch-volatility`: fit the ARCH family with a
   distribution matched to the data.
   ```python
   from arch import arch_model
   res = arch_model(returns * 100, vol="GARCH", p=1, q=1, dist="StudentT").fit(disp="off")
   ```
   Compare GARCH(1,1) vs EGARCH vs GARCH with StudentT by AIC/BIC (`res.aic`, `res.bic`).
3. **Diagnose the fit** — `arch-volatility`: check `res.std_resid()` whiteness (Ljung-Box),
   and `res.conditional_volatility` for regime alignment.
4. **Forecast the horizon** — `arch-forecast`: 
   ```python
   fc = res.forecast(horizon=10, method="analytic")
   vol = np.sqrt(fc.variance.iloc[-1])          # h-step-ahead vol
   paths = res.forecast(horizon=10, method="simulation").variance  # full paths
   ```
   Use `method="analytic"` for the mean path, `simulation`/`bootstrap` when you need the
   whole distribution (ES, scenario stress).
5. **Convert to risk metrics** — `numpy-core` + `arch-forecast`: VaR = `z_α · σ_h`,
   position size = risk budget / σ_h (vol targeting), or feed the forecast into the
   reporting layer as an expected-vol series.
6. **Cross-check with regressions** — `statsmodels-tsa`: for mean dynamics (drift,
   AR terms), fit alongside; the vol layer and the mean layer should agree on regime.

## Pitfalls

1. **Scale**: arch warns on tiny/large input scales — multiply returns by 100 and
   annualize back with `sqrt(252)`.
2. **GARCH(1,1) baseline**: higher orders rarely beat (1,1)+StudentT on daily returns —
   complexity buys instability, not likelihood.
3. **Forecast method ≠ accuracy**: analytic is a closed-form mean; simulation/bootstrap give
   paths. Report which method produced the number you trade on.
4. **Stationarity is a gate, not a check**: modelling non-stationary series (levels, regime
   breaks) with GARCH produces meaningless variance.
5. **Horizon alignment**: `horizon=1` is one step of the input frequency — re-fit at the
   frequency you size positions on.

## Composed Skills & Bridges

| Stage | Skill | Bridge (relation) |
|-------|-------|-------------------|
| preparation | `pandas-ts` | returns panel |
| stationarity | `arch-unitroot` | ADF/KPSS gates |
| estimation | `arch-volatility` | GARCH/EGARCH fits |
| forecasting | `arch-forecast` | variance paths → risk |
| risk conversion | `numpy-core` | vol → VaR / position size |
| mean dynamics | `statsmodels-tsa` | AR/drift cross-check |
