---
name: statsmodels-vector-ar
description: "Use when modelling multivariate time series with statsmodels — VAR/VECM, impulse-response analysis, and causality/whiteness tests."
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
- vector-ar
- multivariate
related_skills:
- statsmodels
- statsmodels-core
- arch-unitroot
target_version: '0.14.6 (dev: after 0.14.6)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `statsmodels` ahead of the latest PyPI release (0.14.6 (dev: after 0.14.6)). Some APIs may not exist in your installed version.

# statsmodels.vector_ar

Multivariate time series: `VAR` estimation with lag selection, impulse-response
functions (`IRAnalysis`) and forecast-error variance decomposition, Granger
causality/whiteness tests, and `VECM` cointegration modelling.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `VAR` | `tsa/vector_ar/var_model.py:L542` | Vector autoregression — `.fit(maxlags)`, `.select_order()`, `.forecast()`, `.summary()` |
| `VARResults` | `tsa/vector_ar/var_model.py:L1327` | Fitted VAR: `.irf()`, `.test_causality()`, `.fevd()`, `.forecast_interval()` |
| `.select_order()` | `tsa/vector_ar/var_model.py:L816` | Lag selection by AIC/BIC/HQIC/FPE across `maxlags` |
| `.test_causality()` | `tsa/vector_ar/var_model.py:L1960` | Granger causality between series in a fitted VAR |
| `CausalityTestResults` | `tsa/vector_ar/hypothesis_test_results.py:L131` | Causality test result (stat, p-value, conclusion) |
| `IRAnalysis` | `tsa/vector_ar/irf.py:L342` | Impulse-response functions + FEVD — via `res.irf(periods)`; `.plot()`, `.fevd()` |
| `WhitenessTestResults` | `tsa/vector_ar/hypothesis_test_results.py:L226` | Residual whiteness (Portmanteau) test result |
| `VECM` | `tsa/vector_ar/vecm.py:L828` | Cointegration-constrained VAR — `k_ar_diff`, `coint_rank`, `deterministic` |
| `VECMResults` | `tsa/vector_ar/vecm.py:L1165` | Fitted VECM: `.test_granger_causality()`, `.irf()`, `.alpha`, `.beta` |
| `.test_granger_causality()` | `tsa/vector_ar/vecm.py:L1939` | Granger-causality tests on VECM residuals |
| `coint_johansen()` | `tsa/vector_ar/vecm.py:L599` | Johansen cointegration rank test — choose `coint_rank` from its result |
| `JohansenTestResult` | `tsa/vector_ar/vecm.py:L731` | Johansen test output: `.lr1`, `.cvm`, `.eig`, `.r` |

## Common Patterns

- **VAR fit with lag selection**:
  ```python
  import statsmodels.api as sm
  model = sm.tsa.VAR(df)                       # DataFrame, DatetimeIndex
  sel = model.select_order(maxlags=8)          # AIC/BIC/HQIC/FPE table
  res = model.fit(maxlags=sel.aic)             # fit at the AIC-chosen lag
  ```
  then `res.forecast(df.values[-sel.aic:], 10)` for the point path and
  `res.forecast_interval(...)` for bands.
- **Impulse-response + variance decomposition**: `res.irf(10).plot()` — how a
  one-unit shock to one series propagates through the system; `.fevd(10)` tells
  you how much of each series' forecast variance the others explain.
- **Granger causality**: `res.test_causality('asset_a', 'asset_b')` — Granger
  direction between signals (all-lag F-test); for pairwise series use
  `sm.tsa.grangercausalitytests(series, maxlag)`.
- **Cointegrated pairs**: run `sm.tsa.coint_johansen(df, det_order=0, k_ar_diff=1)`
  first to pick `coint_rank` from the trace/eigen statistics, then
  `sm.tsa.VECM(df, k_ar_diff=2, coint_rank=1).fit()`; inspect `res.alpha`/`res.beta`
  for the adjustment speed and the cointegrating vector.
- **Residual whiteness**: `res.test_whiteness(nlags=10)` — lagged autocorrelation
  remaining in the residuals signals an under-parameterized lag order; re-fit with
  one more lag and re-test before moving on.
- **Structural VAR**: for identified impulse responses use `SVAR` (in
  `tsa/vector_ar/svar_model.py:L31`) — `IRAnalysis` from a plain VAR is
  reduced-form, so its responses mix direct and indirect effects.

## Pitfalls

- **Lag order**: rely on `select_order()` (AIC/BIC/HQIC/FPE), not `maxlags`
  guesses — too few lags leaves autocorrelation (visible in `test_whiteness`),
  too many overfits and eats degrees of freedom.
- **Causality ≠ direction of trade**: statistical Granger causality is about
  predictive content, not structural causation — don't build a trading rule on it
  alone.
- **Degrees of freedom**: VAR parameters grow with p×k² — with k series and p
  lags you need observations ≫ p·k² or coefficients are noise; keep the universe
  small or shrink.
- **Stationarity before VECM**: VECM is for cointegrated I(1) series — check
  unit roots first (see `arch-unitroot`); fitting VECM on stationary series or
  VAR on cointegrated I(1) series both give misleading inference.
- **coint_rank / det_order**: Johansen results are sensitive to both — compare
  trace vs max-eigen statistic and confirm the deterministic trend assumption
  before trusting the chosen rank.
- **Data hygiene**: `VAR`/`VECM` want a single-frequency DataFrame with no NaN
  gaps and a regular `DatetimeIndex` — mixed frequencies or missing rows shift
  the lag structure silently.
- **IRF confidence bands**: `res.irf(periods, orth=True).plot()` — orthogonalized
  responses depend on the variable ordering; check whether your conclusion
  survives reordering before reporting it.
- **VECM deterministic terms**: `deterministic`/`coint_rank` interplay changes the
  error-correction dynamics — the no-intercept default removes a trend that may be
  present; match `deterministic` to the series' drift behaviour.
- **Don't VAR-difference cointegrated series**: if the Johansen test says rank > 0,
  fit `VECM` (which encodes the long-run levels) — differencing the I(1) series and
  fitting VAR on the differences throws away the cointegration relationship.

## Provenance

Graph: `knowledge_graphs/statsmodels/.graphify/graph.json` — 11616 nodes · 33529 edges ·
638 communities · graphify @ 179d1f4df416, backend opencode, description coverage 82.2%.

## Verification Checklist

- [ ] `sm.tsa.VAR(df).fit(maxlags=2).test_causality('a','b')` runs
- [ ] `res.irf(10)` returns an `IRAnalysis` and `.fevd(10)` resolves
- [ ] `sm.tsa.coint_johansen(df, det_order=0, k_ar_diff=1)` runs on an I(1) pair
- [ ] QR rows cite `tsa/vector_ar/*.py:L*` resolvable in the statsmodels graph
