---
name: darts
description: "Use when working with darts \u2014 the forecasting entry point. Router\
  \ indexing the darts sub-skills; load the sub-skill for the forecasting stage you\
  \ need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: unit8co/darts
source_commit: 080b5340366b8df25e048f4cfd11ca99e3806e97
extraction_date: 2026-08-13
graph:
  nodes: 3954
  edges: 8240
  community_count: 245
  graph_hash: 98a2e69ac67ca67f
tags:
- darts
- router
- forecasting
related_skills:
- darts-models
- darts-timeseries
- darts-backtesting
- statsmodels-tsa
- pymc-distributions
- yfinance-ticker
- optuna-study
target_version: '0.46.1 (dev: after 0.46.1)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `darts` ahead of the latest PyPI release (0.46.1 (dev: after 0.46.1)). Some APIs may not exist in your installed version.

# darts

ML time-series forecasting: unified model zoo (statistical → ML → deep), the
`TimeSeries` container, forecasting metrics, and historical-forecast backtesting —
the forecasting layer over the statsmodels/arch/pymc econometrics stack.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [models](models/SKILL.md) | ForecastingModel zoo — naive/statistical/ML/deep/ensemble families |
| [timeseries](timeseries/SKILL.md) | TimeSeries container + forecasting metrics |
| [backtesting](backtesting/SKILL.md) | historical_forecasts, model selection, backtest-driven tuning |

## Common Patterns

- **Forecast loop**: `model.fit(series)` → `model.predict(n)` / `model.historical_forecasts(...)`.
- **Metrics**: MAPE/SMAPE/MASE/RMSE/quantile-loss via `darts.metrics`.
- **Covariates**: past/future covariates for calendar/regime features.

## Provenance

Graph: `knowledge_graphs/darts/.graphify/graph.json` — 3954 nodes · 8240 edges ·
245 communities · graphify @ 080b5340366b, backend opencode, description coverage 85.2%,
2 curated M2b entries (ADR-0008).

## Verification Checklist

- [ ] Router links resolve to the 3 module skills
- [ ] `related_skills` names resolve to real skills
