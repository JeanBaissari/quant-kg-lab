---
name: pyportfolioopt-expected-returns
description: "Use when estimating expected returns with PyPortfolioOpt — mean_historical_return, capm_return, return_model, and returns_from_prices."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: robertmartin8/PyPortfolioOpt
source_commit: a6638d2e06dae6f444fd022cfd4b3c528902a85b
extraction_date: 2026-08-12
graph:
  nodes: 342
  edges: 512
  community_count: 16
  graph_hash: 50f7a3628b7218f1
tags:
- pyportfolioopt
- expected-returns
related_skills:
- pyportfolioopt
- pyportfolioopt-risk-models
---

# pypfopt.expected_returns

Expected-return estimators feeding the optimizer: historical means, CAPM, and the
`return_model()` dispatch — with `returns_from_prices()` for the raw series.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `return_model()` | `expected_returns.py` | Computes an expected-returns estimate using the specified return model |
| `mean_historical_return()` | `expected_returns.py` | Estimates the annualized mean of historical daily asset returns |
| `returns_from_prices()` | `expected_returns.py` | Converts asset price data into a daily returns series |
| `capm_return` | `expected_returns.py` | CAPM-based expected returns (module: Black-Litterman priors) |

## Common Patterns

- **Quick estimate**: `mu = expected_returns.mean_historical_return(prices)` — annualized
  (252-day) mean; the default for exploration.
- **CAPM prior**: `expected_returns.capm_return(prices)` — market-driven prior, the natural
  input for Black-Litterman.
- **Explicit dispatch**: `return_model(prices, method="mean_historical_return")`.

## Pitfalls

- **Return frequency mismatch**: mu is annualized while the optimizer assumes the same
  frequency as S — keep both from the same price window.
- **Negative/zero means**: historical means can be negative; that is fine for
  `min_volatility()` but makes `max_sharpe()` ill-defined (use `efficient_return`).

## Provenance

Graph: `knowledge_graphs/pyportfolioopt/.graphify/graph.json` — 342 nodes · 512 edges ·
16 communities · graphify @ a6638d2e06da, backend opencode, description coverage 91.3%.

## Verification Checklist

- [ ] `mean_historical_return(prices)` returns an annualized Series aligned to prices columns
