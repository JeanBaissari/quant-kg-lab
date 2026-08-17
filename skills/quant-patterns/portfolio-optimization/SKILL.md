---
name: quant-portfolio-optimization
description: "Use when building portfolios from expected returns and risk models — mean-variance frontiers with PyPortfolioOpt, custom constrained optimization with cvxpy, hierarchical/risk-budget cross-checks with Riskfolio, and implementation-aware allocation."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [pyportfolioopt-expected-returns, pyportfolioopt-risk-models, pyportfolioopt-efficient-frontier, pyportfolioopt-black-litterman, cvxpy-problems, cvxpy-atoms, riskfolio-portfolio, riskfolio-risk-measures, pandas-core]
tags: [quantitative-finance, portfolio-optimization, mean-variance, cvxpy, riskfolio, black-litterman, workflow]
related_skills: [pyportfolioopt-expected-returns, pyportfolioopt-risk-models, pyportfolioopt-efficient-frontier, pyportfolioopt-black-litterman, cvxpy-problems, cvxpy-atoms, riskfolio-portfolio, riskfolio-risk-measures, pandas-core]
target_version: cross-lib
---

# Quant Portfolio Optimization (returns → risk model → frontier → constraints → allocation)

Portfolio optimization answers "given expected returns and a risk model, what weights maximize
the objective under my constraints?" — with a robustness cross-check from a second optimizer
family before any allocation is implemented.

## Steps

1. **Estimate expected returns** — `pyportfolioopt-expected-returns`: 
   ```python
   from pypfopt import expected_returns, risk_models
   mu = expected_returns.mean_historical_return(prices)   # or ema_historical_return
   S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()  # or sample_cov
   ```
   Use shrinkage for short-history/many-asset universes; verify PSD with
   `fix_nonpositive_semidefinite`.
2. **Solve the frontier** — `pyportfolioopt-efficient-frontier`:
   ```python
   ef = EfficientFrontier(mu, S, weight_bounds=(0, 1))
   w = ef.max_sharpe()
   ef.clean_weights()
   ```
   Sweep `efficient_return(t)` across targets for the frontier curve.
3. **Add constraints** — `pyportfolioopt-efficient-frontier` + `cvxpy-atoms`: concentration
   caps (`weight_bounds`), sector caps (`add_constraint`), L2/transaction-cost objectives
   (`add_objective`). Tight bounds + sum-to-one can make the problem infeasible — relax
   before blaming the solver.
4. **Tail-aware variant** — `riskfolio-portfolio` + `riskfolio-risk-measures`: cross-check
   with a CVaR-optimized portfolio; risk-contribution decomposition tells you where risk
   actually lives vs where the MV weights imply it lives.
5. **Views (optional)** — `pyportfolioopt-black-litterman`: `BlackLittermanModel` blends
   market priors with views; compare posterior weights vs the unconstrained frontier.
6. **Custom constraints via cvxpy** — `cvxpy-problems`: when PyPortfolioOpt's constraint
   surface isn't enough, build the problem directly (quad_form risk, norm turnover caps,
   dual values for shadow prices).
7. **Allocation** — `pandas-core` + `pyportfolioopt-efficient-frontier`:
   `DiscreteAllocation(w, latest_prices)` → whole-share trades; verify weights sum within
   tolerance and the portfolio is implementable.

## Pitfalls

1. **Garbage-in**: mu and S must come from the same price window — mixing estimators
   silently skews every downstream weight.
2. **Max-Sharpe concentration**: max_sharpe often concentrates in 1–2 assets — always add
   weight bounds and eyeball the weights before believing them.
3. **Mean-variance blindness**: MV ignores tails — always run a CVaR/riskfolio cross-check
   on fat-tailed universes before committing.
4. **Infeasibility**: tight bounds + equality constraints conflict — diagnose by relaxing
   constraints one at a time.
5. **Continuous ≠ tradable**: clean weights are fractions, not orders — DiscreteAllocation
   (or your broker's sizing) must be the last step, never skipped.

## Composed Skills & Bridges

| Stage | Skill | Bridge (relation) |
|-------|-------|-------------------|
| returns | `pyportfolioopt-expected-returns` | prices → mu |
| risk | `pyportfolioopt-risk-models` | prices → S (PSD-checked) |
| frontier | `pyportfolioopt-efficient-frontier` | mu/S → weights |
| constraints | `pyportfolioopt-efficient-frontier`, `cvxpy-atoms` | add_constraint/add_objective |
| cross-check | `riskfolio-portfolio`, `riskfolio-risk-measures` | CVaR + risk decomposition |
| views | `pyportfolioopt-black-litterman` | priors + views → posterior |
| custom | `cvxpy-problems` | direct conic formulation |
| allocation | `pyportfolioopt-efficient-frontier` | `DiscreteAllocation` (input_to) |

## Related Skills

- [[pyportfolioopt-expected-returns]]
- [[pyportfolioopt-risk-models]]
- [[pyportfolioopt-efficient-frontier]]
- [[pyportfolioopt-black-litterman]]
- [[cvxpy-problems]]
- [[cvxpy-atoms]]
- [[riskfolio-portfolio]]
- [[riskfolio-risk-measures]]
- [[pandas-core]]
