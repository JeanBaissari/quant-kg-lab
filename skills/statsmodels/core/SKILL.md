---
name: statsmodels-core
description: "Use when building statistical models in Python \u2014 OLS/GLS/WLS, GLM,\
  \ model results and diagnostics, formula API, and summary tables."
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
- regression
- glm
- statistical-models
related_skills:
- statsmodels
- scipy-stats
- pandas-core
target_version: '0.14.6 (dev: after 0.14.6)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `statsmodels` ahead of the latest PyPI release (0.14.6 (dev: after 0.14.6)). Some APIs may not exist in your installed version.

# statsmodels.core

Classical statistical modelling: linear models (OLS/GLS/WLS), generalized linear
models (GLM), the `LikelihoodModel` framework, the formula API, and the summary/table
layer. The bridge between pandas data prep and econometric inference — use it when
`scipy.stats` testing is not enough and you need fitted models, standard errors,
p-values, and diagnostics.

## Quick Reference

| API | Source File | Degree | Description |
|-----|------------|--------|-------------|
| `OLS` | `regression/linear_model.py:L938` | 857 | Ordinary Least Squares — `sm.OLS(y, X).fit()`; add constant with `add_constant` |
| `GLM` | `genmod/generalized_linear_model.py:L66` | 375 | Generalized linear model — families (Gaussian, Binomial, Poisson), link functions |
| `LikelihoodModel` | `base/model.py:L283` | 331 | Abstract maximum-likelihood base — powers OLS/GLM and the discrete/tsa families |
| `PandasData` | `base/data.py:L542` | 360 | DataFrame handling layer — formula/endog/exog extraction from pandas |
| `FormulaManager` | `formula/_manager.py:L207` | 929 | Formula API engine behind `sm.formula.ols("y ~ x1 + x2", data=df)` |
| `SimpleTable` | `iolib/table.py:L138` | 681 | ASCII/HTML summary table renderer — powers `results.summary()` |
| `ValueWarning` | `tools/sm_exceptions.py:L104` | 838 | Warning class for suspicious values (e.g. missing data, NaN handling) |
| `SpecificationWarning` | `tools/sm_exceptions.py:L128` | 690 | Warning for model-specification concerns (rank deficiency, collinearity) |
| `ConvergenceWarning` | `tools/sm_exceptions.py:L66` | 658 | Warning when an optimizer does not converge (GLM/IRLS, discrete MLE) |
| `add_constant` | `tools/tools.py:L85` | — | Prepend a constant column to the design matrix (intercept) |

## Common Patterns

- **Fit a linear model with a constant**: `sm.OLS(y, sm.add_constant(X)).fit()` — always
  add the constant explicitly; statsmodels does not auto-insert an intercept.
- **Formula API**: `sm.formula.ols("return ~ mkt_ret + size", data=df).fit()` — the
  `FormulaManager` parses patsy formulas directly on a DataFrame; ideal for quant factor
  regressions.
- **GLM for count/binary outcomes**: `sm.GLM(y, X, family=sm.families.Poisson()).fit()` —
  use binomial family with `logit` link for classification-style modelling.
- **Model results object**: `fit()` returns a results object with `.params`, `.bse`,
  `.pvalues`, `.tvalues`, `.rsquared`, `.summary()`, `.resid`, `.fittedvalues` — the
  standard extraction surface for factor/regression research.
- **Diagnostics**: check `.summary()` for the F-statistic, Jarque-Bera normality, and
  Durbin-Watson autocorrelation rows before trusting a factor regression.

## Pitfalls

- **Missing constant → spurious R²**: without `add_constant`, R² is computed without an
  intercept and can be misleadingly high for trending series.
- **NaN handling**: statsmodels drops NaN rows silently in many fits — check
  `df.dropna()` explicitly before fitting so results are reproducible.
- **`sm.OLS` vs `sm.formula.ols`**: the former takes arrays (y, X); the latter a formula +
  DataFrame. Mixing them up produces confusing errors.
- **Warnings are signals**: `ValueWarning`/`SpecificationWarning`/`ConvergenceWarning` are
  worth reading — a converged-but-warning GLM can still be numerically suspect.
- **Newer API surface**: `statsmodels` keeps legacy aliases (e.g. `sm.GLS`, `sm.WLS`,
  `sm.OLS`) stable; prefer the module-level constructors over internal classes.

## Provenance

Graph: `knowledge_graphs/statsmodels/.graphify/graph.json` — 11616 nodes · 33529 edges ·
638 communities · graphify @ 179d1f4df416, backend opencode, description coverage 82.2% ·
God nodes: `Appender` (1093), `FormulaManager` (929), `OLS` (857) — public-API hubs only (see
GRAPH_SPEC noise filter).

## Verification Checklist

- [ ] `sm.OLS(y, sm.add_constant(X)).fit()` runs and `.summary()` renders
- [ ] `sm.formula.ols("y ~ x", data=df).fit()` works with a pandas DataFrame
- [ ] QR rows cite source files resolvable in `knowledge_graphs/statsmodels/.graphify/graph.json`
