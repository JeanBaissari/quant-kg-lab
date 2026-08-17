---
name: pyportfolioopt-efficient-frontier
description: "Use when optimizing a portfolio with PyPortfolioOpt \u2014 mean-variance\
  \ EfficientFrontier, max_sharpe, min_volatility, efficient_return/risk, and weight\
  \ cleaning."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: robertmartin8/PyPortfolioOpt
source_commit: a6638d2e06dae6f444fd022cfd4b3c528902a85b
extraction_date: 2026-08-12
graph:
  nodes: 342
  edges: 522
  community_count: 16
  graph_hash: c8c490eaf5b8ac05
tags:
- pyportfolioopt
- portfolio
- mean-variance
related_skills:
- pyportfolioopt
- pyportfolioopt-risk-models
- pyportfolioopt-expected-returns
target_version: '1.6.0 (dev: after 1.6.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `pyportfolioopt` ahead of the latest PyPI release (1.6.0 (dev: after 1.6.0)). Some APIs may not exist in your installed version.

# pypfopt.efficient_frontier

Mean-variance portfolio optimization: `EfficientFrontier` builds the Markowitz
optimizer from expected returns + covariance and returns optimal weights via
`max_sharpe()`, `min_volatility()`, `efficient_return()`, `efficient_risk()` —
plus the tail-risk variants (`EfficientCVaR`, `EfficientCDaR`, `EfficientSemivariance`).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `EfficientFrontier` | `efficient_frontier/efficient_frontier.py:L17` | Mean-variance optimizer — `max_sharpe()`/`min_volatility()` return optimal weights |
| `EfficientCVaR` | `efficient_frontier/efficient_cvar.py:L15` | Optimizer minimizing portfolio Conditional Value at Risk along the mean-CVaR frontier |
| `EfficientCDaR` | `efficient_frontier/efficient_cdar.py:L15` | Optimizer minimizing Conditional Drawdown at Risk along the mean-CDaR frontier |
| `EfficientSemivariance` | `efficient_frontier/efficient_semivariance.py:L13` | Optimizer minimizing downside risk through semivariance |
| `BaseConvexOptimizer` | `base/_base_optimizer.py:L141` | Parent class adding cvxpy constraints/objectives to the optimizer |
| `BaseOptimizer` | `base/_base_optimizer.py:L30` | Parent class storing weights and exposing `clean_weights()` |
| `EfficientFrontier.max_sharpe()` | `efficient_frontier/efficient_frontier.py:L238` | Max-Sharpe weights — `risk_free_rate` parameter |
| `EfficientFrontier.min_volatility()` | `efficient_frontier/efficient_frontier.py:L195` | Minimum-variance weights |
| `EfficientFrontier.efficient_return()` | `efficient_frontier/efficient_frontier.py:L418` | Frontier point at a target return |
| `EfficientFrontier.add_constraint()` | `base/_base_optimizer.py:L371` | Custom cvxpy constraint — `w >= 0`, `w <= 0.1`, sector bounds |
| `EfficientFrontier.add_objective()` | `base/_base_optimizer.py:L347` | Custom cvxpy objective term — L2 reg, turnover penalty |
| `EfficientFrontier.portfolio_performance()` | `efficient_frontier/efficient_frontier.py:L472` | Expected return/vol/Sharpe of the optimal weights |
| `EfficientFrontier.clean_weights()` | `base/_base_optimizer.py:L88` | Round/clip weights below a cutoff to zero |
| `EfficientFrontier.save_weights_to_file()` | `efficient_frontier/efficient_frontier.py:L17` | Persist weights (txt/csv) |
| `DiscreteAllocation` | `discrete_allocation.py:L42` | Whole-share allocation from continuous weights + latest prices |

## Common Patterns

- **Max-Sharpe portfolio**: `ef = EfficientFrontier(mu, S); w = ef.max_sharpe(); ef.clean_weights()` —
  then `ef.portfolio_performance(verbose=True)` for the expected metrics.
- **Minimum volatility**: `ef.min_volatility()` — the default low-risk benchmark.
- **Target-return frontier**: `ef.efficient_return(target_return)` — pick a point on the
  efficient frontier; sweep targets for the frontier curve.
- **Tail-risk variants**: `EfficientCVaR(returns, beta=0.95).min_cvar()` for CVaR-optimal
  portfolios when returns are fat-tailed.
- **Discrete allocation**: feed cleaned weights to `DiscreteAllocation(w, prices)` →
  `lp_portfolio()`/`greedy_portfolio()` for whole-share trades.
- **Concentration control**: `EfficientFrontier(mu, S, weight_bounds=(0, 0.1))` or
  `ef.add_constraint(lambda w: w <= 0.1)` — cap single-name risk.
- **Sector/industry constraints**: `ef.add_constraint(lambda w: sector_weights @ w <= 0.4)` —
  sector caps via a sector-dummy matrix.
- **Turnover/L2 penalties**: `ef.add_objective(objective_functions.L2_reg(gamma=0.1))` —
  shrinkage toward 1/N; `transaction_cost` objective for churn control.
- **Frontier sweep**: loop `efficient_return(t)` over a return grid, collect weights +
  `portfolio_performance()` — the classic efficient-frontier curve for reporting.

## Pitfalls

- **Garbage-in**: mu/S must come from the same data window; mixing `mean_historical_return`
  and `sample_cov` with different price periods silently skews weights.
- **Weights are continuous**: always `clean_weights()` before `DiscreteAllocation`.
- **`max_sharpe()` may concentrate**: check weights for 1-2 assets dominating; constrain with
  `add_constraint(lambda w: w <= 0.1)` or `max_weight` in the constructor.
- **CVaR/CVaR-drawdown need returns, not mu/S**: EfficientCVaR/EfficientCDaR/
  EfficientSemivariance take the returns DataFrame — passing mu/S to them is an API error
  caught late.
- **Constraint feasibility**: tight `weight_bounds` plus an equality sum-to-one constraint
  can make the problem infeasible — relax bounds before suspecting cvxpy.
- **L2_reg scale**: gamma is not normalized by asset count — tune on a validation window;
  too large collapses weights toward 1/N, too small does nothing.

## Provenance

Graph: `knowledge_graphs/pyportfolioopt/.graphify/graph.json` — 342 nodes · 512 edges ·
16 communities · graphify @ a6638d2e06da, backend opencode, description coverage 91.3%.

## Verification Checklist

- [ ] `EfficientFrontier(mu, S).max_sharpe()` runs with 2+ assets
- [ ] QR rows cite source files resolvable in the pyportfolioopt graph
