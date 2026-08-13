---
name: statsmodels
description: "Use when working with statsmodels — the statistical-modelling entry point. Router indexing the statsmodels sub-skills; load the sub-skill for the model family you need."
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
  graph_hash: 460a1b24977f4557
tags:
- statsmodels
- router
related_skills:
- statsmodels-core
- statsmodels-glm
- statsmodels-diagnostics
- statsmodels-tsa
- statsmodels-statespace
- statsmodels-vector-ar
- pandas-core
- scipy-stats
---

# statsmodels

Classical statistical modelling for econometrics and quant research — linear and
generalized linear models, model results, diagnostics, and the formula API.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [statsmodels-core](core/SKILL.md) | OLS/GLS/WLS, LikelihoodModel, formula API, summaries — the workhorse surface |
| [statsmodels-glm](glm/SKILL.md) | GLM families/links, GEE + covariance structures, GLMGam, robust covariance |
| [statsmodels-diagnostics](diagnostics/SKILL.md) | residual tests, influence/Cook's distance, VIF, ANOVA, model comparison |
| [statsmodels-tsa](tsa/SKILL.md) | ARIMA/SARIMAX, ExponentialSmoothing, arima specification API |
| [statsmodels-statespace](statespace/SKILL.md) | MLEModel/MLEResults, Kalman filtering, news analysis |
| [statsmodels-vector-ar](vector_ar/SKILL.md) | VAR/VECM, impulse response, Granger causality |

## Common Patterns

- **Factor research**: `sm.OLS(ret, sm.add_constant(factors)).fit()` — factor exposures,
  t-stats, and residuals in one object.
- **GLM for non-normal outcomes**: Poisson (counts), Binomial (classification-style) with
  family/link selection.
- **Formula API**: `sm.formula.ols("ret ~ mkt + size", data=df)` — patsy formulas over a
  DataFrame, matching pandas-style data prep.

## Provenance

Graph: `knowledge_graphs/statsmodels/.graphify/graph.json` — 11616 nodes · 33529 edges ·
638 communities · graphify @ 179d1f4df416, backend opencode, description coverage 82.2%.

## Verification Checklist

- [ ] Router links resolve: `core/SKILL.md` exists
- [ ] `related_skills` names resolve to real skills
