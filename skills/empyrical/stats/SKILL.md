---
name: empyrical-stats
description: "Use when computing portfolio/strategy performance metrics from returns — annual return/volatility, Sharpe/Sortino/omega/Calmar ratios, max drawdown, alpha/beta, downside risk, tail ratio, stability, and cumulative-return helpers."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: Quantopian/empyrical
source_commit: 40f61b4f229df10898d46d08f7b1bdc543c0f99c
extraction_date: 2026-08-13
graph:
  nodes: 180
  edges: 258
  community_count: 23
  graph_hash: ce35d5e4b0a5c431
tags:
- empyrical
- metrics
- sharpe
- drawdown
- alpha-beta
related_skills:
- empyrical
- empyrical-perf-attrib
- pyfolio-timeseries
- pandas-core
- quant-volatility-modelling
---

# empyrical.stats

The metric primitives: every statistic takes a returns series (pandas Series, daily by
default) and returns a scalar. `period`/`annualization` are shared conventions across the
whole module.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `annual_return()` | `stats.py:L408` | Annualized return from cumulative returns over the period |
| `annual_volatility()` | `stats.py:L487` | Annualized standard deviation of returns |
| `sharpe_ratio()` | `stats.py:L652` | Annualized Sharpe — (mean - risk_free) / vol, period-scaled |
| `excess_sharpe()` | `stats.py:L894` | Sharpe of returns minus a benchmark series |
| `sortino_ratio()` | `stats.py:L727` | Downside-deviation-based ratio — penalizes only losses |
| `omega_ratio()` | `stats.py:L599` | Probability-weighted gain/loss ratio (threshold 0 by default) |
| `calmar_ratio()` | `stats.py:L548` | Annual return / max drawdown |
| `max_drawdown()` | `stats.py:L352` | Largest peak-to-trough decline (positive fraction) |
| `downside_risk()` | `stats.py:L811` | Deviation of returns below a required minimum return |
| `alpha()` | `stats.py:L1154` | Excess return vs the benchmark after beta adjustment |
| `beta()` | `stats.py:L1314` | Regression slope of returns on factor returns |
| `alpha_beta()` | `stats.py:L1004` | (alpha, beta) pair from one regression |
| `alpha_aligned()` | `stats.py:L1219` | Alpha on the aligned returns∩factor window (pyfolio's path) |
| `beta_aligned()` | `stats.py:L1352` | Beta on the aligned window |
| `alpha_beta_aligned()` | `stats.py:L1086` | Aligned (alpha, beta) pair |
| `tail_ratio()` | `stats.py:L1501` | Right-tail / left-tail probability ratio — return skew |
| `stability_of_timeseries()` | `stats.py:L1471` | R² of the cumulative-return trend — edge persistence |
| `up_down_capture()` | `stats.py:L1955` | Ratio of upside vs downside capture of the benchmark |
| `roll_up_down_capture()` | `stats.py:L2070` | Rolling up/down capture over a window |
| `cagr()` | `stats.py:L450` | Compound annual growth rate |
| `simple_returns()` | `stats.py:L193` | pct_change-based returns (drops NaN head) |
| `cum_returns()` | `stats.py:L219` | Cumulative returns series (capital-gain convention) |
| `cum_returns_final()` | `stats.py:L280` | Final cumulative growth factor |
| `aggregate_returns()` | `stats.py:L316` | Resample returns to a lower frequency |
| `annualization_factor()` | `stats.py:L153` | sqrt(periods_per_year) scaling for annualization |
| `_adjust_returns()` | `stats.py:L134` | Subtract risk-free rate from returns |
| `gpd_es_calculator()` | `stats.py:L1792` | Generalized-Pareto expected-shortfall calculator |
| `gpd_var_calculator()` | `stats.py:L1804` | Generalized-Pareto VaR calculator (EVT tail) |
| `gpd_loglikelihood()` | `stats.py:L1840` | GPD log-likelihood for tail estimation |

## Common Patterns

- **One-call summary**:
  ```python
  from empyrical import sharpe_ratio, sortino_ratio, max_drawdown, calmar_ratio
  stats = {
      "sharpe": sharpe_ratio(returns),
      "sortino": sortino_ratio(returns),
      "max_dd": max_drawdown(returns),
      "calmar": calmar_ratio(returns),
  }
  ```
- **Benchmark-relative**: `alpha_beta(returns, factor_returns)` — the standard
  market-adjusted pair; use the `*_aligned` variants when the two series have
  different lengths (pyfolio does this internally).
- **Period consistency**: daily data + `period='daily'` (default) annualizes with
  `sqrt(252)` via `annualization_factor`; for weekly/monthly pass the matching period
  and let the module pick the right factor.
- **Risk-free handling**: `sharpe_ratio(returns, risk_free=0.0)` — pass your funding
  rate as a per-period fraction for a funding-aware Sharpe.
- **Drawdown reporting**: `max_drawdown` returns a positive fraction — report as
  `-max_drawdown` for the conventional negative drawdown.
- **EVT tails**: `gpd_var_calculator` / `gpd_es_calculator` for fat-tail VaR/ES when
  historical quantiles understate tail risk.

## Pitfalls

- **period vs annualization mismatch**: passing `period='monthly'` without overriding
  `annualization` scales volatility by the wrong factor — verify `annualization_factor`.
- **NaN handling**: returns with NaN gaps propagate; pre-fill or drop before calling
  (the module does not impute).
- **max_drawdown sign**: it returns a positive magnitude — negate for display or for
  feeding Calmar consistently.
- **cum_returns convention**: cumulative returns use the capital-gain convention
  (first value = 1 + r0 style), not raw product of (1+r) — read the docs before
  chaining with `aggregate_returns`.
- **Aligned vs raw**: `alpha_beta` on unaligned series silently uses their intersection
  only when you call the `*_aligned` forms — the raw forms assume aligned inputs.
- **GPD estimators need thresholds**: the EVT calculators assume you've selected a
  tail threshold — garbage thresholds yield garbage tail metrics.

## Provenance

Graph: `knowledge_graphs/empyrical/.graphify/graph.json` — 180 nodes · 258 edges ·
23 communities · graphify @ 40f61b4f229d, backend opencode, description coverage 93.3%.

## Verification Checklist

- [ ] `sharpe_ratio(returns)` / `max_drawdown(returns)` run on a small returns Series
- [ ] `alpha_beta_aligned(returns, factor_returns)` returns (alpha, beta)
- [ ] QR rows cite `stats.py:L*` resolvable in the empyrical graph
