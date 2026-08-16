---
name: quantstats-stats
description: "Use when computing portfolio analytics metrics with quantstats \u2014\
  \ sharpe/sortino/cagr/max_drawdown/VaR/CVaR/kelly/ulcer/win-rate and the extended\
  \ risk-metric family."
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
- metrics
- risk
- sharpe
- var
related_skills:
- quantstats
- quantstats-reports
- quantstats-plots
- empyrical-stats
- pandas-core
target_version: 0.0.81 (released tag v0.0.81)
upstream_status: stale
---

# quantstats.stats

The analytics metric surface: classic ratios (Sharpe/Sortino/Calmar/CAGR), drawdown
analysis, tail risk (VaR/CVaR), and trading-oriented stats (win rate, profit factor,
kelly, ulcer, serenity). Thin wrappers extend empyrical with the trading-metric family.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `sharpe()` | `stats.py:L841` | Sharpe ratio (annualized, risk-free adjustable) |
| `adjusted_sortino()` | `stats.py:L1149` | Sortino adjusted for autocorrelation penalty |
| `sortino()` | `stats.py:L982` | Downside-deviation ratio |
| `calmar()` | `stats.py:L1642` | CAGR / max drawdown |
| `cagr()` | `stats.py:L1507` | Compound annual growth rate |
| `max_drawdown()` | `stats.py:L2451` | Worst peak-to-trough decline |
| `to_drawdown_series()` | `stats.py:L2499` | Drawdown series over time |
| `expected_return()` | `stats.py:L198` | Mean daily/annualized expected return |
| `value_at_risk()` | `stats.py:L1861` | Historical VaR at a confidence level |
| `conditional_value_at_risk()` | `stats.py:L1921` | CVaR/expected shortfall — tail beyond VaR |
| `cvar()` | `stats.py:L1971` | CVaR alias for the same tail measure |
| `kelly_criterion()` | `stats.py:L2553` | Optimal bet size from win rate + payoff |
| `win_rate()` | `stats.py:L509` | Fraction of positive-period returns |
| `win_loss_ratio()` | `stats.py:L2093` | Avg win / avg loss magnitude |
| `profit_factor()` | `stats.py:L2161` | Gross profit / gross loss |
| `payoff_ratio()` | `stats.py:L2054` | Avg winning trade / avg losing trade |
| `probabilistic_ratio()` | `stats.py:L1188` | Probability-weighted payoff ratio |
| `ulcer_index()` | `stats.py:L1680` | RMS of drawdown series — depth+recovery combined |
| `ulcer_performance_index()` | `stats.py:L1706` | Return per unit of ulcer index |
| `serenity_index()` | `stats.py:L1757` | Sharpe-like, drawdown-scaled risk-adjusted return |
| `common_sense_ratio()` | `stats.py:L2228` | Tail-ratio-based stability measure |
| `cpc_index()` | `stats.py:L2201` | Cornish-Fisher-based tail-adjusted index |
| `risk_of_ruin()` | `stats.py:L1815` | Probability of ruin over the horizon |
| `rar()` | `stats.py:L1561` | Risk-adjusted return (drawdown-scaled) |
| `treynor_ratio()` | `stats.py:L1355` | Excess return per unit of market beta |
| `autocorr_penalty()` | `stats.py:L793` | Autocorrelation penalty for the adjusted sortino |
| `comp()` | `stats.py:L99` | Compounded growth factor from returns |

## Common Patterns

- **One-call metrics table**: `qs.stats.metrics(returns)` — the whole analytics block;
  render via `qs.reports.html(...)` when a report is needed.
- **Tail-risk trio**: `value_at_risk`, `conditional_value_at_risk`, `cvar` — report all
  three; VaR alone understates tail exposure.
- **Trading statistics**: `win_rate` + `profit_factor` + `payoff_ratio` + `kelly_criterion`
  — the bet-sizing decision set.
- **Drawdown pair**: `max_drawdown` (depth) + `to_drawdown_series` (path) + `ulcer_index`
  (depth×recovery) — a complete drawdown picture.
- **Stability family**: `serenity_index` / `common_sense_ratio` / `cpc_index` — robust
  risk-adjusted measures when Sharpe's assumptions are violated.

## Pitfalls

- **Sharpe vs adjusted_sortino**: `adjusted_sortino` penalizes autocorrelated returns
  (`autocorr_penalty`) — for daily momentum strategies the two diverge meaningfully.
- **VaR vs CVaR**: always pair them — VaR says "5% worse than X", CVaR says "average
  loss when it IS worse than X".
- **Kelly is aggressive**: `kelly_criterion` returns the full-Kelly fraction — halve it
  (half-Kelly) in practice.
- **win_rate is period-dependent**: daily win rate ≠ trade win rate — label the
  frequency in any report.
- **Risk-free consistency**: pass the same `rf`/period to sharpe and sortino or the
  report's ratios are not comparable.
- **Cross-library convention harmonization**: quantstats returns a NEGATIVE drawdown
  while empyrical/pyfolio return positive magnitudes, and its risk-free default (0.0)
  differs from backtrader (0.01) and pypfopt (0.02) — see
  `quant-metric-conventions` before comparing across libraries.

## Provenance

Graph: `knowledge_graphs/quantstats/.graphify/graph.json` — 393 nodes · 531 edges ·
48 communities · graphify @ fbd10daed022, backend opencode, description coverage 93.5%.

## Verification Checklist

- [ ] `qs.stats.metrics(returns)` produces the metric table
- [ ] `value_at_risk`/`conditional_value_at_risk`/`cvar` agree on ordering
- [ ] QR rows cite `stats.py:L*` resolvable in the quantstats graph
