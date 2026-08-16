---
name: pyfolio-timeseries
description: "Use when computing portfolio performance statistics with pyfolio \u2014\
  \ perf_stats, rolling Sharpe/drawdown, drawdown series, and timeseries analytics."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: quantopian/pyfolio
source_commit: 4b901f6d73aa02ceb6d04b7d83502e5c6f2e81aa
extraction_date: 2026-08-12
graph:
  nodes: 305
  edges: 361
  community_count: 61
  graph_hash: cc432015b7700967
tags:
- pyfolio
- timeseries
- performance-stats
related_skills:
- pyfolio
- pyfolio-tearsheets
- pandas-core
target_version: '0.9.2 (dev: after 0.9.2)'
upstream_status: dead
---

## Version Note

> ⚠️ **Upstream is frozen** (no commits since the pin). This skill describes `pyfolio` at its pinned commit — an abandoned release line. Target version: 0.9.2 (dev: after 0.9.2). Verify against your installed version before use.

# pyfolio.timeseries

Performance analytics over the returns series: `perf_stats`, rolling metrics,
drawdown analysis — the numbers behind the tear sheets.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `perf_stats()` | `timeseries.py:L692` | Performance statistics table: annual return/vol, Sharpe, Sortino, max drawdown |
| `rolling_sharpe()` | `timeseries.py:L1050` | Rolling Sharpe ratio series over the period |
| `rolling_volatility()` | `timeseries.py:L1028` | Rolling annualized volatility |
| `rolling_beta()` | `timeseries.py:L507` | Rolling beta vs a benchmark series |
| `max_drawdown()` | `timeseries.py:L63` | Maximum drawdown magnitude and its window |
| `get_max_drawdown_underwater()` | `timeseries.py:L870` | Underwater curve — drawdown over time |
| `get_top_drawdowns()` | `timeseries.py:L931` | The n worst drawdown episodes |
| `gen_drawdown_table()` | `timeseries.py:L974` | Drawdown summary table (depth, length, recovery) |
| `annual_return()` | `timeseries.py:L87` | Annualized return |
| `annual_volatility()` | `timeseries.py:L111` | Annualized volatility |
| `sharpe_ratio()` | `timeseries.py:L262` | Sharpe with configurable risk-free rate |
| `sortino_ratio()` | `timeseries.py:L202` | Downside-deviation-based ratio |
| `calmar_ratio()` | `timeseries.py:L135` | Annual return / max drawdown |
| `omega_ratio()` | `timeseries.py:L164` | Probability-weighted gain/loss ratio |
| `tail_ratio()` | `timeseries.py:L390` | Right/left tail ratio — skew of returns |
| `value_at_risk()` | `timeseries.py:L626` | Parametric/historical VaR |
| `var_cov_var_normal()` | `timeseries.py:L38` | Normal parametric VaR |
| `alpha_beta()` | `timeseries.py:L294` | Regression alpha/beta vs benchmark |
| `stability_of_timeseries()` | `timeseries.py:L368` | R² of the cumulative-return trend — strategy stability |
| `cum_returns()` | `timeseries.py:L459` | Cumulative returns series |
| `aggregate_returns()` | `timeseries.py:L486` | Aggregate to periods (weekly/monthly/quarterly) |
| `perf_stats_bootstrap()` | `timeseries.py:L742` | Bootstrap CI around performance stats |
| `forecast_cone_bootstrap()` | `timeseries.py:L1149` | Monte-Carlo forecast cone from bootstrap |
| `simulate_paths()` | `timeseries.py:L1077` | Simulated return paths for the cone |
| `plotting.py:L1` | Chart helpers: returns/drawdown/rolling panels |

## Common Patterns

- **Stats table**: `pyfolio.timeseries.perf_stats(returns, factor_returns, periods_per_year=252)` —
  the standard summary for strategy reviews.
- **Rolling risk**: `rolling_sharpe(returns, rolling_window=90)` — stability check vs a
  single-point Sharpe.
- **Drawdown drill-down**: `max_drawdown(returns)` for the worst window; `drawdown(returns)`
  for the full series.
- **Monthly heatmaps**: `plotting.plot_monthly_returns_heatmap(returns)`.
- **Risk metrics for reporting**: `sortino_ratio`, `calmar_ratio`, `omega_ratio`, `tail_ratio`
  — the tail-aware complement to plain Sharpe.
- **Strategy stability**: `stability_of_timeseries(returns)` — R² of the trend; low values
  mean the "edge" is episodic, not persistent.
- **Uncertainty quantification**: `perf_stats_bootstrap(returns)` — CIs around the headline
  stats instead of point estimates.
- **VaR discipline**: `value_at_risk(returns, cutoff=0.05)` for the position-sizing layer;
  cross-check `var_cov_var_normal` (parametric) vs historical.

## Pitfalls

- **Annualization**: `periods_per_year` must match the data frequency (252 daily, 12
  monthly) or all ratios are wrong.
- **NaN handling**: forward-fill gaps in returns before stats; zeros are fine, NaNs are not.
- **Benchmark alignment**: `factor_returns` (benchmark) must share the index with returns.
- **Cross-library convention harmonization**: pyfolio's positive drawdown magnitude
  and 0.0 risk-free default match empyrical but differ from quantstats/backtrader —
  see `quant-metric-conventions` before mixing metrics in one report.

## Provenance

Graph: `knowledge_graphs/pyfolio/.graphify/graph.json` — 305 nodes · 361 edges ·
61 communities · graphify @ 4b901f6d73aa, backend opencode, description coverage 80.4%.

## Verification Checklist

- [ ] `perf_stats(returns)` returns the standard table with correct annualization
