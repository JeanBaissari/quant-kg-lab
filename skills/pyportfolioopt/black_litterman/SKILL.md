---
name: pyportfolioopt-black-litterman
description: "Use when combining market-implied priors with investor views via the Black-Litterman model — BlackLittermanModel, market-implied returns, posterior weights."
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
- black-litterman
- views
related_skills:
- pyportfolioopt
- pyportfolioopt-expected-returns
- pyportfolioopt-efficient-frontier
---

# pypfopt.black_litterman

The Black-Litterman model: market-implied (CAPM) prior returns blended with
investor views into a posterior return distribution — then optimized through
`EfficientFrontier` as usual.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `BlackLittermanModel` | `black_litterman.py` | Combines market-implied prior returns with investor views to produce posterior estimates |
| `market_implied_prior_returns` | `black_litterman.py` | CAPM-implied prior returns from market caps + risk aversion |
| `market_implied_risk_aversion` | `black_litterman.py` | Implied risk-aversion coefficient from the market portfolio |

## Common Patterns

- **Standard flow**: prior = `market_implied_prior_returns(market_caps, risk_aversion, cov)`;
  `bl = BlackLittermanModel(cov, pi=prior, absolute_views=views)`; `post = bl.bl_returns()`;
  then `ef = EfficientFrontier(post, cov)` and optimize as usual.
- **View uncertainty**: the default `omega` follows the model's heuristic; pass explicit
  uncertainty for trusted views.
- **Posterior weights**: `bl.bl_weights()` — or optimize the posterior returns directly.

## Pitfalls

- **Covariance consistency**: prior returns and S must come from the same market; mixing
  estimators silently distorts the posterior.
- **Views format**: absolute views as {asset: target_return}; relative views need the
  P/Q formulation — keep the dict form unless you need pairs.

## Provenance

Graph: `knowledge_graphs/pyportfolioopt/.graphify/graph.json` — 342 nodes · 512 edges ·
16 communities · graphify @ a6638d2e06da, backend opencode, description coverage 91.3%.

## Verification Checklist

- [ ] `BlackLittermanModel(cov, pi=prior, absolute_views=views).bl_returns()` runs
- [ ] QR rows cite source files resolvable in the pyportfolioopt graph
