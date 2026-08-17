---
name: alphalens-factor-analysis
description: "Use when analyzing a factor's predictive power with alphalens \u2014\
  \ FactorData, forward returns, quantile analysis, and IC (information coefficient)\
  \ metrics."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: quantopian/alphalens
source_commit: 77084f1e4c2c0be407e032d444fb19e4be4b0f37
extraction_date: 2026-08-12
graph:
  nodes: 172
  edges: 231
  community_count: 5
  graph_hash: b9a5f8898b936c87
tags:
- alphalens
- factor-research
- ic
related_skills:
- alphalens
- alphalens-tearsheets
- pandas-core
target_version: 0.4.0 (released tag v0.4.0)
upstream_status: dead
---

## Version Note

> ⚠️ **Upstream is frozen** (no commits since the pin). This skill describes `alphalens` at its pinned commit — an abandoned release line. Target version: 0.4.0 (released tag v0.4.0). Verify against your installed version before use.

# alphalens.factor_analysis

Factor-performance analysis: wrap factor values + prices in `FactorData`,
compute forward returns, and measure predictive power through quantile
breakdowns and information coefficients (IC).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `get_clean_factor_and_forward_returns` | `utils.py:L666` | Prepare factor + prices → aligned forward-return panel (the pipeline entry point) |
| `get_clean_factor` | `utils.py:L453` | Clean factor values (winsorize, z-score, group mapping) without returns |
| `compute_forward_returns` | `utils.py:L216` | Build forward returns from prices for the given periods |
| `quantize_factor` | `utils.py:L85` | Bin factor values into quantiles for group analysis |
| `mean_information_coefficient` | `performance.py:L77` | Mean IC over the period with std and IC quantiles |
| `factor_information_coefficient` | `performance.py:L28` | Per-period IC series for the factor |
| `mean_return_by_quantile` | `performance.py:L453` | Mean returns by quantile — the monotonicity check |
| `factor_alpha_beta` | `performance.py:L258` | Regression alpha/beta of factor returns vs benchmark |
| `factor_weights()` | `performance.py:L129` | Factor-value-weighted portfolio returns (long-short) |
| `factor_returns()` | `performance.py:L208` | Period-by-period factor portfolio returns |
| `cumulative_returns()` | `performance.py:L333` | Cumulative factor returns over the sample |
| `positions()` | `performance.py:L355` | Daily long/short positions implied by the factor |
| `compute_mean_returns_spread()` | `performance.py:L520` | Top-minus-bottom quantile spread — the monotonicity magnitude |
| `quantile_turnover()` | `performance.py:L568` | Fraction of names changing quantile between rebalances |
| `factor_rank_autocorrelation()` | `performance.py:L601` | Rank persistence of the factor — stability of signal |
| `common_start_returns()` | `performance.py:L642` | Align returns to a common start window |
| `average_cumulative_return_by_quantile()` | `performance.py:L730` | Event-style cumulative returns per quantile |
| `factor_cumulative_returns()` | `performance.py:L866` | Cumulative factor-return series for plotting |
| `factor_positions()` | `performance.py:L936` | Position series per quantile for turnover analysis |
| `create_pyfolio_input()` | `performance.py:L1008` | Convert alphalens analysis → pyfolio-compatible returns/positions |

## Common Patterns

- **Factor tear sheet pipeline**: `get_clean_factor_and_forward_returns(factor, prices,
  quantiles=5, periods=(1, 5, 10))` → IC/quantile analytics → tear sheets.
- **Quantile returns**: `mean_return_by_quantile(factor_data)` — monotonic top-vs-bottom
  spread is the factor's core signal; confirm with `compute_mean_returns_spread`.
- **IC series**: `factor_information_coefficient(factor_data)` then
  `mean_information_coefficient` for the period summary.
- **Alpha/beta**: `factor_alpha_beta(factor_data, benchmark)` — risk-adjusted factor
  contribution.
- **Turnover discipline**: `quantile_turnover(factor_data)` + `factor_rank_autocorrelation`
  — a factor with high IC but churning ranks dies after transaction costs.
- **Group-neutral factors**: pass `groupby` data to `get_clean_factor...` and compare
  `mean_return_by_quantile(..., by_group=True)` — neutralize sector biases before
  concluding.
- **Event study**: `average_cumulative_return_by_quantile(factor_data)` — how quantile
  membership performs around rebalance dates.
- **pyfolio handoff**: `create_pyfolio_input(factor_data, ...)` — factor long-short
  returns straight into pyfolio tear sheets.

## Pitfalls

- **Alignment**: factor values indexed by (timestamp, asset) MultiIndex; prices as a wide
  DataFrame — mismatched formats silently yield empty panels.
- **Lookahead**: `periods` are forward returns; the factor must use only data known at `t`
  or IC is inflated.
- **Version pin**: this graph is pinned at `77084f1e` (2020-04-27) — the modern
  utils/data.py split (FactorData) does not exist here; use the function API above.

## Provenance

Graph: `knowledge_graphs/alphalens/.graphify/graph.json` — 172 nodes · 231 edges ·
5 communities · graphify @ 77084f1e4c2c, backend opencode, description coverage 86.8%.

## Verification Checklist

- [ ] `get_clean_factor_and_forward_returns` runs on a synthetic factor + prices
- [ ] QR rows cite source files resolvable in the alphalens graph
