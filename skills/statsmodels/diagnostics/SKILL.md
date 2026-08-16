---
name: statsmodels-diagnostics
description: "Use when diagnosing fitted models with statsmodels \u2014 residual tests\
  \ (jarque_bera, durbin_watson, breusch_pagan, Ljung-Box), influence analysis (OLSInfluence/MLEInfluence,\
  \ Cook's distance, VIF), ANOVA, and model-comparison tests."
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
- diagnostics
- residuals
- influence
- anova
related_skills:
- statsmodels
- statsmodels-core
- statsmodels-glm
- scipy-stats
- pandas-core
---

# statsmodels.diagnostics

Model-validation surface: residual-based tests (`stats/diagnostic.py`), influence and
outlier analysis (`stats/outliers_influence.py`), ANOVA (`stats/anova.py`), and
model-comparison utilities. The "is this fit trustworthy?" layer.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `jarque_bera()` | `stats/stattools.py:L86` | Normality test on residuals (skew + kurtosis) |
| `durbin_watson()` | `stats/diagnostic.py` | Autocorrelation of residuals — DW ≈ 2 is clean |
| `het_breuschpagan()` | `stats/diagnostic.py:L1144` | Heteroskedasticity test (Breusch-Pagan LM) |
| `het_arch()` | `stats/diagnostic.py:L936` | ARCH effects test (volatility clustering) |
| `acorr_ljungbox()` | `stats/diagnostic.py:L596` | Ljung-Box autocorrelation — white-noise check |
| `acorr_breusch_godfrey()` | `stats/diagnostic.py:L1002` | Serial correlation test, higher-order |
| `spec_white()` | `stats/diagnostic.py:L1813` | White specification test |
| `breaks_hansen()` | `stats/diagnostic.py:L2050` | Hansen structural-break test |
| `breaks_cusumolsresid()` | `stats/diagnostic.py:L2097` | CUSUM structural-break test |
| `recursive_olsresiduals()` | `stats/diagnostic.py:L1898` | Recursive residuals — CUSUM input |
| `compare_cox()` | `stats/diagnostic.py:L142` | Cox non-nested model comparison |
| `compare_j()` | `stats/diagnostic.py:L253` | J-test non-nested comparison |
| `compare_encompassing()` | `stats/diagnostic.py:L508` | Encompassing test |
| `OLSInfluence` | `stats/outliers_influence.py:L801` | Influence for OLS — cooks, leverage, dfbeta |
| `MLEInfluence` | `stats/outliers_influence.py:L388` | Influence for ML models (GLM/GLM results) |
| `GLMInfluence` | `stats/outliers_influence.py:L1456` | GLM influence wrapper |
| `variance_inflation_factor()` | `stats/outliers_influence.py` | VIF — multicollinearity per regressor |
| `anova_lm()` | `stats/anova.py:L349` | ANOVA table from fitted models (type I/II/III) |
| `AnovaRM` | `stats/anova.py:L523` | Repeated-measures ANOVA |
| `CompareMeans` | `stats/weightstats.py:L862` | Two-sample mean comparison (ttest/ztest) |
| `DescrStatsW` | `stats/weightstats.py:L38` | Weighted descriptive statistics |
| `Table2x2` | `stats/contingency_tables.py:L666` | 2×2 contingency analysis |
| `Power` | `stats/power.py:L445` | Power/sample-size calculations |
| `TrimmedMean` | `stats/robust_compare.py:L95` | Robust mean comparison |

## Common Patterns

- **Residual sanity check**:
  ```python
  from statsmodels.stats.diagnostic import (
      jarque_bera, durbin_watson, het_breusch_pagan, acorr_ljungbox)
  res = ols_fit  # fitted OLS/GLM
  from statsmodels.stats.stattools import jarque_bera
  jb_stat, jb_p, skew, kurt = jarque_bera(res.resid)
  dw = durbin_watson(res.resid)
  lm, lmpval, fval, fpval = het_breusch_pagan(res.resid, res.model.exog)
  lb = acorr_ljungbox(res.resid, lags=10)
  ```
- **Influence scan**: `infl = OLSInfluence(res); infl.cooks_distance` /
  `infl.hat_matrix_diag` — find high-leverage/high-influence rows before trusting
  the coefficients.
- **Multicollinearity**: `variance_inflation_factor(exog, i)` per column — VIF > 10
  flags redundant regressors.
- **White-noise gate for factor returns**: `acorr_ljungbox` on strategy residuals —
  a significant lag means the model left signal on the table.
- **Volatility clustering**: `het_arch` on squared residuals — if significant,
  the mean model is misspecified without a vol model (arch layer).
- **ANOVA for factor significance**: `anova_lm(m1, m2)` — nested model comparison;
  `CompareMeans` for two-group factor tests.
- **Structural breaks**: `breaks_cusumolsresid` / `breaks_hansen` — regime detection
  in the residual series.

## Pitfalls

- **DW only tests lag-1**: for higher-order autocorrelation use
  `acorr_ljungbox`/`acorr_breusch_godfrey`.
- **jarque_bera on small samples**: the test is weak with < 30 observations — treat
  with care in short backtests.
- **het_breusch_pagan needs exog**: pass the design matrix, not the residuals alone —
  wrong exog silently changes the test.
- **Influence ≠ outlier**: high leverage with low residual isn't a problem row;
  Cook's distance combines both — judge on Cook's D, not leverage alone.
- **VIF with constants**: include the constant column in exog; dropping it biases
  VIFs.
- **anova_lm type**: the default type II vs III matters for unbalanced designs —
  pick `typ` explicitly.

## Provenance

Graph: `knowledge_graphs/statsmodels/.graphify/graph.json` — 11616 nodes · 33529 edges ·
638 communities · graphify @ pin, backend opencode, description coverage 43%.

## Verification Checklist

- [ ] `jarque_bera`/`durbin_watson`/`het_breusch_pagan` run on a fitted model's resid
- [ ] `OLSInfluence(res).cooks_distance` returns distances + p-values
- [ ] `variance_inflation_factor(exog, i)` runs per column
- [ ] QR rows cite `stats/*.py` files resolvable in the statsmodels graph
