---
name: pyfolio-timeseries
description: "Use when computing portfolio performance statistics with pyfolio — perf_stats, rolling Sharpe/drawdown, drawdown series, and timeseries analytics."
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
---

# pyfolio.timeseries

Performance analytics over the returns series: `perf_stats`, rolling metrics,
drawdown analysis — the numbers behind the tear sheets.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `timeseries.py` | `timeseries.py` | Module implementing returns-based performance statistics |
| `perf_stats` | `timeseries.py` | Performance statistics table: annual return/vol, Sharpe, Sortino, max drawdown |
| `rolling_sharpe` | `timeseries.py` | Rolling Sharpe ratio series over the period |
| `max_drawdown` | `timeseries.py` | Maximum drawdown magnitude and its window |
| `plotting.py` | `plotting.py` | Chart helpers: returns/drawdown/rolling panels |

## Common Patterns

- **Stats table**: `pyfolio.timeseries.perf_stats(returns, factor_returns, periods_per_year=252)` —
  the standard summary for strategy reviews.
- **Rolling risk**: `rolling_sharpe(returns, rolling_window=90)` — stability check vs a
  single-point Sharpe.
- **Drawdown drill-down**: `max_drawdown(returns)` for the worst window; `drawdown(returns)`
  for the full series.
- **Monthly heatmaps**: `plotting.plot_monthly_returns_heatmap(returns)`.

## Pitfalls

- **Annualization**: `periods_per_year` must match the data frequency (252 daily, 12
  monthly) or all ratios are wrong.
- **NaN handling**: forward-fill gaps in returns before stats; zeros are fine, NaNs are not.
- **Benchmark alignment**: `factor_returns` (benchmark) must share the index with returns.

## Provenance

Graph: `knowledge_graphs/pyfolio/.graphify/graph.json` — 305 nodes · 361 edges ·
61 communities · graphify @ 4b901f6d73aa, backend opencode, description coverage 80.4%.

## Verification Checklist

- [ ] `perf_stats(returns)` returns the standard table with correct annualization
