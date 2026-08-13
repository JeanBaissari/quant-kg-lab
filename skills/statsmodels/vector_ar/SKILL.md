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
  graph_hash: 460a1b24977f4557
tags:
- statsmodels
- vector-ar
- multivariate
related_skills:
- statsmodels
- statsmodels-core
- arch-unitroot
---

# statsmodels.vector_ar

Multivariate time series: `VAR` estimation, impulse-response functions (`IRAnalysis`),
Granger-causality and whiteness tests, and VECM cointegration modelling.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `VAR` | `tsa/vector_ar/var_model.py` | Vector autoregression — fit, forecast, summary |
| `CausalityTestResults` | `tsa/vector_ar/hypothesis_test_results.py` | Granger-causality test results (stat, pvalue, conclusion) |
| `WhitenessTestResults` | `tsa/vector_ar/hypothesis_test_results.py` | Residual whiteness test results |
| `IRAnalysis` | `tsa/vector_ar/irf.py` | Impulse-response functions and variance decomposition |
| `tsa/vector_ar/vecm.py` | VECM — cointegration-constrained VAR |

## Common Patterns

- **VAR fit**: `model = sm.tsa.VAR(df); res = model.fit(maxlags=4)` → `res.forecast(df.values, 10)`.
- **Causality**: `res.test_causality('asset_a', 'asset_b')` — Granger direction between
  signals.
- **Impulse response**: `res.irf(10).plot()` — how a shock to one series propagates.
- **Cointegrated pairs**: `sm.tsa.VECM(df, k_ar_diff=2, coint_rank=1).fit()` after
  Engle-Granger.

## Pitfalls

- **Lag order**: `maxlags` vs AIC/BIC selection — too few lags leaves autocorrelation,
  too many overfits.
- **Causality ≠ direction of trade**: statistical Granger causality is about predictive
  content, not structural causation.
- **Degrees of freedom**: VAR params grow with p×k² — keep the universe small.

## Provenance

Graph: `knowledge_graphs/statsmodels/.graphify/graph.json` — 11616 nodes · 33529 edges ·
638 communities · graphify @ 179d1f4df416, backend opencode, description coverage 82.2%.

## Verification Checklist

- [ ] `sm.tsa.VAR(df).fit(maxlags=2).test_causality('a','b')` runs
