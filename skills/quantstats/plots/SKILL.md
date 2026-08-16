---
name: quantstats-plots
description: "Use when plotting portfolio analytics with quantstats \u2014 returns/drawdown/rolling/heatmap/distribution\
  \ plots, the plotting wrappers, and montecarlo simulations."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: ranaroussi/quantstats
source_commit: fbd10daed0227aa0d10da6513f1b15e7e98d7fae
extraction_date: 2026-08-13
graph:
  nodes: 393
  edges: 531
  community_count: 51
  graph_hash: 98393f286b04d0d2
tags:
- quantstats
- plots
- visualization
- montecarlo
related_skills:
- quantstats
- quantstats-stats
- quantstats-reports
- pandas-core
- numpy-core
target_version: 0.0.81 (released tag v0.0.81)
upstream_status: stale
---

# quantstats.plots

Visualization layer: wrapper functions (`returns()`, `drawdown()`, `rolling_*`,
heatmaps, distribution) backed by `_plotting/core.py:L1` primitives, plus
Monte-Carlo simulation (`_montecarlo.py:L1`) for path-based risk analytics.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `returns()` | `_plotting/wrappers.py:L571` | Cumulative returns vs benchmark plot |
| `daily_returns()` | `_plotting/wrappers.py:L772` | Daily returns bar chart |
| `log_returns()` | `_plotting/wrappers.py:L670` | Log-returns series plot |
| `monthly_returns()` | `_plotting/wrappers.py:L1871` | Monthly returns plot |
| `yearly_returns()` | `_plotting/wrappers.py:L863` | Yearly returns bars |
| `distribution()` | `_plotting/wrappers.py:L972` | Returns distribution + stats overlay |
| `histogram()` | `_plotting/wrappers.py:L1044` | Histogram of returns |
| `drawdown()` | `_plotting/wrappers.py:L1134` | Drawdown series plot (underwater curve) |
| `drawdowns_periods()` | `_plotting/wrappers.py:L1221` | Highlight the worst drawdown periods |
| `rolling_sharpe()` | `_plotting/wrappers.py:L1484` | Rolling Sharpe over a window |
| `rolling_sortino()` | `_plotting/wrappers.py:L1580` | Rolling Sortino over a window |
| `rolling_volatility()` | `_plotting/wrappers.py:L1397` | Rolling annualized volatility |
| `monthly_heatmap()` | `_plotting/wrappers.py:L1671` | Monthly return heatmap (calendar layout) |
| `snapshot()` | `_plotting/wrappers.py:L110` | Returns + drawdown + rolling snapshot panel |
| `montecarlo()` | `_plotting/wrappers.py:L1945` | Monte-Carlo path plot wrapper |
| `montecarlo_distribution()` | `_plotting/wrappers.py:L2042` | Distribution of simulated end values |
| `plot_timeseries()` | `_plotting/core.py:L350` | Core timeseries primitive |
| `plot_returns_bars()` | `_plotting/core.py:L128` | Core returns-bar primitive |
| `plot_rolling_beta()` | `_plotting/core.py:L1052` | Rolling beta vs benchmark |
| `plot_longest_drawdowns()` | `_plotting/core.py:L1264` | Longest drawdown episodes |
| `plot_montecarlo()` | `_plotting/core.py:L1811` | Simulated paths with confidence band |
| `plot_distribution()` | `_plotting/core.py:L1435` | Distribution + fitted curve |
| `run_montecarlo()` | `_montecarlo.py:L220` | Run path simulations (n paths, horizon) |
| `MonteCarloResult` | `_montecarlo.py:L36` | Simulation result — paths, VaR/ES stats |
| `_get_colors()` | `_plotting/core.py:L104` | Theme/color palette for the plot family |

## Common Patterns

- **Report plots**: `qs.plots.returns(returns, benchmark)` + `qs.plots.drawdown(returns)`
  — the two canonical charts for any review.
- **Rolling stability**: `rolling_sharpe` + `rolling_volatility` — how the edge varies
  over time; the flat-line test for strategy persistence.
- **Calendar view**: `monthly_heatmap(returns)` — seasonality at a glance.
- **Tail visualization**: `distribution(returns)` + `histogram(returns)` — skew/kurtosis
  visible before any metric is quoted.
- **Scenario risk**: `run_montecarlo(returns, n=1000)` then `plot_montecarlo` — path
  dispersion and end-value distribution for VaR/ES story-telling.
- **Snapshot deck**: `snapshot(returns)` — one call, the standard trio panel.

## Pitfalls

- **matplotlib vs plotly**: wrapper defaults differ by install — pin the backend in
  production plotting code or the report output varies.
- **Monte-Carlo seed**: `run_montecarlo` is stochastic — set a seed for reproducible
  paths in reports.
- **Window semantics**: `rolling_*` windows are in periods — a 90 on daily data is 90
  days, not 90 weeks.
- **Heatmap frequency**: `monthly_heatmap` expects daily/OHLCV-indexed returns — other
  frequencies produce an empty or malformed calendar.
- **Plot-heavy reports**: `snapshot()`/`full()` render many figures — call
  `matplotlib.use("Agg")` headlessly to avoid GUI backend errors.

## Provenance

Graph: `knowledge_graphs/quantstats/.graphify/graph.json` — 393 nodes · 531 edges ·
48 communities · graphify @ fbd10daed022, backend opencode, description coverage 93.5%.

## Verification Checklist

- [ ] `qs.plots.returns(returns)` renders with Agg backend
- [ ] `run_montecarlo(returns, n=100, seed=1)` returns a MonteCarloResult
- [ ] QR rows cite `_plotting/*.py` / `_montecarlo.py:L1` resolvable in the quantstats graph
