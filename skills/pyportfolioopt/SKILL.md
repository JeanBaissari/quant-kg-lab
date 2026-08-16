---
name: pyportfolioopt
description: "Use when working with PyPortfolioOpt \u2014 the portfolio-optimization\
  \ entry point. Router indexing the pypfopt sub-skills; load the sub-skill for the\
  \ estimator you need."
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
  graph_hash: e238a0e0014fb438
tags:
- pyportfolioopt
- router
related_skills:
- pyportfolioopt-efficient-frontier
- pyportfolioopt-risk-models
- pyportfolioopt-expected-returns
- pyportfolioopt-black-litterman
---

# pypfopt

Portfolio optimization built on cvxpy: expected-return estimation → risk/covariance
models → mean-variance (and tail-risk) optimizers → discrete allocation.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [efficient_frontier](efficient_frontier/SKILL.md) | EfficientFrontier, EfficientCVaR/CDaR/Semivariance, clean_weights |
| [risk_models](risk_models/SKILL.md) | sample_cov, CovarianceShrinkage, risk_matrix, PSD repair |
| [expected_returns](expected_returns/SKILL.md) | mean_historical_return, capm_return, return_model |
| [black_litterman](black_litterman/SKILL.md) | BlackLittermanModel, market-implied priors, views |

## Common Patterns

- **Canonical pipeline**: `mu = expected_returns.mean_historical_return(prices)`;
  `S = risk_models.sample_cov(prices)`; `ef = EfficientFrontier(mu, S)`;
  `w = ef.max_sharpe(); ef.clean_weights()`.
- **Black-Litterman variant**: prior → views → posterior → same optimizer.
- **CVaR/semivariance for fat tails**: `EfficientCVaR(returns).min_cvar()`.

## Provenance

Graph: `knowledge_graphs/pyportfolioopt/.graphify/graph.json` — 342 nodes · 512 edges ·
16 communities · graphify @ a6638d2e06da, backend opencode, description coverage 91.3%.

## Verification Checklist

- [ ] Router links resolve to the 4 module skills
- [ ] `related_skills` names resolve to real skills
