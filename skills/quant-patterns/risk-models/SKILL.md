---
name: quant-risk-models
description: "Use when building risk models and constructing portfolios — covariance estimation, constrained optimization, and risk-aware allocation across riskfolio, pyportfolioopt, and cvxpy."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [riskfolio-portfolio, riskfolio-risk-measures, pyportfolioopt-expected-returns, pyportfolioopt-risk-models, pyportfolioopt-efficient-frontier, cvxpy-problems, cvxpy-atoms, pandas-core, numpy-core]
tags: [quantitative-finance, risk-models, portfolio-optimization, riskfolio, pyportfolioopt, cvxpy, workflow]
related_skills: [riskfolio-portfolio, riskfolio-risk-measures, pyportfolioopt-expected-returns, pyportfolioopt-risk-models, pyportfolioopt-efficient-frontier, cvxpy-problems, cvxpy-atoms]
target_version: cross-lib
---

# Quant Risk Models (covariance -> optimization -> allocation -> risk decomposition)

Portfolio construction starts with a risk model: estimate covariance, choose an objective, solve
under constraints, and decompose risk to verify. This playbook chains pyportfolioopt for the
standard mean-variance workflow, riskfolio for tail-aware and hierarchical alternatives, and cvxpy
for custom constrained problems.

## Steps

1. **Estimate expected returns** — `pyportfolioopt-expected-returns`:
   ```python
   from pypfopt import expected_returns, risk_models
   mu = expected_returns.mean_historical_return(prices)
   ```
2. **Build a covariance model** — `pyportfolioopt-risk-models`: shrinkage estimators for
   high-dimensional universes; verify PSD before optimization.
   ```python
   S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()
   from pypfopt.risk_models import fix_nonpositive_semidefinite
   S = fix_nonpositive_semidefinite(S)      # base/_base_optimizer.py:L307
   ```
   *Citation*: `pyportfolioopt/base/_base_optimizer.py:L307`
3. **Solve the efficient frontier** — `pyportfolioopt-efficient-frontier`:
   ```python
   from pypfopt.efficient_frontier import EfficientFrontier
   ef = EfficientFrontier(mu, S, weight_bounds=(0, 1))  # efficient_frontier.py:L17
   ef.max_sharpe()
   ef.clean_weights()
   ```
   *Citation*: `pyportfolioopt/efficient_frontier/efficient_frontier.py:L17`
4. **Cross-check with Riskfolio** — `riskfolio-portfolio`: risk parity, CVaR optimization, and
   hierarchical risk parity. Decompose risk contribution to see where concentration lives.
   ```python
   import riskfolio as rp
   port = rp.Portfolio(returns=returns)     # src/Portfolio.py:L56
   w_rp = port.rp_optimization(model="RLS") # risk parity
   ```
   *Citation*: `riskfolio/src/Portfolio.py:L56`
5. **Custom constraints via cvxpy** — `cvxpy-problems`: when pyportfolioopt's constraint surface
   is not enough (turnover caps, sector-neutral, L2 regularization), build the problem directly.
   ```python
   import cvxpy as cp
   w = cp.Variable(n)
   risk = cp.quad_form(w, S)
   prob = cp.Problem(cp.Minimize(risk),     # problems/problem.py:L138
                     [cp.sum(w) == 1, w >= 0])
   prob.solve()
   ```
   *Citation*: `cvxpy/problems/problem.py:L138`
6. **Risk decomposition** — verify that the optimized weights produce the expected risk
   contribution per asset; large deviations indicate solver numerical issues.

## Pitfalls

1. **Covariance estimation** — sample covariance is noisy for p > T universes. Always use
   shrinkage (Ledoit-Wolf) or a factor model. Mixing estimation windows between mu and S
   silently skews weights.
2. **Short selling constraints** — `weight_bounds=(-1, 1)` allows unlimited short exposure.
   Use sector-level caps or gross-exposure constraints to bound total short interest.
3. **Transaction costs** — mean-variance ignores turnover. Add L2 regularization or explicit
   turnover constraints; otherwise the "optimal" portfolio trades excessively.
4. **Rebalancing frequency** — the optimizer assumes you can trade to the target weights
   immediately. In practice, bid-ask spread and market impact erode returns for high-turnover
   strategies. Model rebalancing costs explicitly.

## Composed Skills & Bridges

| Source | Target | Relation | Description |
|--------|--------|----------|-------------|
| pyportfolioopt-risk-models | pyportfolioopt-efficient-frontier | feeds_into | mu/S -> EfficientFrontier |
| pyportfolioopt-efficient-frontier | cvxpy-problems | extends | when constraints exceed ef.add_constraint |
| riskfolio-portfolio | riskfolio-risk-measures | decomposes | weights -> risk contribution per asset |
| cvxpy-problems | cvxpy-atoms | uses | quad_form, sum, norm atoms |
| this playbook | quant-full-pipeline | completes | portfolio weights -> position sizing |
| this playbook | quant-portfolio-optimization | overlaps | this playbook adds risk decomposition focus |
