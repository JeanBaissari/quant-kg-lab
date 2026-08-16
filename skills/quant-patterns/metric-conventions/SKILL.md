---
name: quant-metric-conventions
description: "Use when auditing or combining performance metrics (drawdown, Sharpe, risk-free returns, annualization) produced by different Python quant libraries — empyrical, quantstats, pyfolio, backtrader, pyportfolioopt — in one report or pipeline."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [empyrical-stats, quantstats-stats, pyfolio-timeseries, backtrader-analyzers, pyportfolioopt-efficient-frontier]
tags: [quantitative-finance, metrics, conventions, reporting, workflow, harmonization]
related_skills: [empyrical-stats, quantstats-stats, pyfolio-timeseries, backtrader-analyzers, pyportfolioopt-efficient-frontier]
---

# Quant Metric Conventions (signs, defaults, annualization)

Performance metrics look identical across libraries but are NOT comparable
as-is: each library embeds its own conventions for drawdown sign, risk-free
return defaults, and annualization factors. A mixed-library report that forgets
this will silently invert drawdowns and mis-rank Sharpe ratios. This playbook
teaches the audit-and-harmonize workflow (findings verified against the
empyrical/quantstats/pyfolio/backtrader/pyportfolioopt API surfaces).

## Steps

1. **Inventory the metric producers** — list which library computed each number
   in the report (`empyrical-stats`, `quantstats-stats`, `pyfolio-timeseries`,
   `backtrader-analyzers`, `pyportfolioopt-efficient-frontier`). The same name
   (e.g. `max_drawdown`, `sharpe_ratio`) may carry a different convention per
   producer.
2. **Harmonize drawdown sign** — the convention table below decides what each
   library returns; normalize to ONE internal sign (recommend: negative = loss)
   before any comparison, table render, or aggregation:
   ```python
   def normalize_drawdown(value):
       # empyrical/pyfolio/backtrader → positive magnitude; quantstats → negative
       return -abs(value)
   ```
3. **Harmonize the risk-free return** — every Sharpe/Sortino/Calmar-style ratio
   embeds a risk-free default. Recompute each ratio with the SAME explicit
   `risk_free`/`rf`/`riskfreerate`/`risk_free_rate` argument (as a per-period
   fraction matching the return frequency) instead of relying on defaults.
4. **Align annualization** — confirm every annualized metric uses the same
   `periods_per_year`/`annualization` factor for the input frequency (252 daily,
   12 monthly, 52 weekly); standardize on `sqrt(periods_per_year)` scaling.
5. **Cross-check one metric across producers** — after harmonizing, compute e.g.
   Sharpe and max drawdown on the SAME returns series with two libraries and
   confirm they agree within rounding; disagreement means a convention was missed.

## Pitfalls

1. **Drawdown sign flip**: empyrical/pyfolio return a POSITIVE magnitude (negate
   for display), quantstats returns a NEGATIVE drawdown, backtrader reports a
   positive % — concatenating raw values into one table inverts half the rows.
2. **Silent risk-free defaults**: empyrical defaults to 0.0, pypfopt `max_sharpe`
   defaults to 0.02, backtrader's SharpeRatio analyzer defaults to 0.01, quantstats
   defaults to 0.0 — comparing Sharpe ratios computed with different implied
   risk-free rates mis-ranks strategies.
3. **Annualization mismatch**: a daily-scaled metric compared against a
   monthly-scaled one is off by ~√21; never mix `sqrt(252)` and `sqrt(12)` values
   without rescaling.
4. **Sign conventions vs charting**: plotting layers often negate drawdown
   internally (pyfolio charts), so the raw value in a DataFrame and the charted
   value may differ in sign — trace the convention at the call site, not the plot.
5. **Frequency drift across libraries**: backtrader annualizes from its
   `timeframe` parameter while empyrical infers from `period` — set both
   explicitly to the same trading frequency (252 daily).

| Convention | empyrical | quantstats | pyfolio | backtrader | pypfopt |
|------------|-----------|------------|---------|------------|---------|
| Drawdown sign | positive (negate for display) | negative | positive (negate for display) | positive % | n/a (optimizer) |
| Risk-free default | 0.0 | 0.0 | 0.0 | 0.01 | 0.02 (`max_sharpe`) |
| Annualization | `sqrt(252)` daily via `annualization_factor` | `periods_per_year=252` | `periods_per_year` (252 daily) | 252 for `TimeFrame.Days` | `periods_per_year=252` |

## Composed Skills & Bridges

| Stage | Skill | Bridge (relation) |
|-------|-------|-------------------|
| metric primitives | `empyrical-stats` | raw stats on returns |
| analytics surface | `quantstats-stats` | trading-metric family |
| strategy analytics | `pyfolio-timeseries` | perf stats + tearsheet inputs |
| trade-level metrics | `backtrader-analyzers` | analyzer outputs (Sharpe, drawdown) |
| optimization layer | `pyportfolioopt-efficient-frontier` | risk-free-sensitive `max_sharpe` |
| harmonization | this playbook | sign/default/annualization normalization |
