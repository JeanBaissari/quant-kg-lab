---
name: alphalens-factor-analysis
description: "Use when analyzing a factor's predictive power with alphalens — FactorData, forward returns, quantile analysis, and IC (information coefficient) metrics."
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
  graph_hash: b1726a0e2484f41b
tags:
- alphalens
- factor-research
- ic
related_skills:
- alphalens
- alphalens-tearsheets
- pandas-core
---

# alphalens.factor_analysis

Factor-performance analysis: wrap factor values + prices in `FactorData`,
compute forward returns, and measure predictive power through quantile
breakdowns and information coefficients (IC).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `FactorData` | `utils/data.py` | Wraps factor values + prices + group data; `compute_returns()` builds forward returns |
| `performance.py` | `performance.py` | Factor returns, IC, quantile and turnover analytics |
| `utils.py` | `utils.py` | Data preparation helpers for forward-return alignment |
| `mean_information_coefficient` | `performance.py` | Mean IC over the period with std and IC quantiles |

## Common Patterns

- **Factor tear sheet pipeline**: `factor_data = alphalens.utils.get_clean_factor_and_forward_returns(factor, prices,
  quantiles=5, periods=(1, 5, 10))` → `alphalens.performance.factor_alpha_beta` / IC
  metrics → tear sheets.
- **Quantile returns**: `alphalens.performance.mean_return_by_quantile(factor_data)` — the
  monotonicity check (top-quantile beats bottom) is the factor's core signal.
- **IC series**: `alphalens.performance.factor_information_coefficient(factor_data)` — then
  mean/vol of IC across periods.

## Pitfalls

- **Alignment**: factor values must be indexed by (timestamp, asset) with a MultiIndex on
  `factor`; prices as a wide DataFrame — mixing formats silently produces empty returns.
- **Lookahead**: `periods` are forward returns; ensure the factor itself only uses data known
  at `t` or the IC is inflated.
- **Group data**: omit or provide correctly — wrong group labels distort quantile grouping.

## Provenance

Graph: `knowledge_graphs/alphalens/.graphify/graph.json` — 172 nodes · 231 edges ·
5 communities · graphify @ 77084f1e4c2c, backend opencode, description coverage 86.8%.

## Verification Checklist

- [ ] `get_clean_factor_and_forward_returns` runs on a synthetic factor + prices
- [ ] QR rows cite source files resolvable in the alphalens graph
