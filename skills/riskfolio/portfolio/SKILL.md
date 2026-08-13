---
name: riskfolio-portfolio
description: "Use when building constrained portfolio optimizations with Riskfolio-Lib — Portfolio, risk measures, constraints, and the cvxpy-backed optimization() call."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: dcajasn/Riskfolio-Lib
source_commit: 632a9e48fbaf2b9f8e83864a492332364b6ed32c
extraction_date: 2026-08-12
graph:
  nodes: 426
  edges: 599
  community_count: 29
  graph_hash: dc57c0d4aa45a96d
tags:
- riskfolio
- portfolio
- optimization
related_skills:
- riskfolio
- riskfolio-risk-measures
- cvxpy-core
---

# riskfolio.portfolio

Constrained mean-risk portfolio optimization: `Portfolio` builds the problem
(returns, cov/risk measures, constraints) and `optimization()` solves it via
cvxpy — MV/CVaR/CDaR/EVaR objectives under weight/group/factor constraints.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Portfolio` | `src/Portfolio.py` | Builds the optimization problem: returns, risk measure, constraints |
| `Portfolio.optimization()` | `src/Portfolio.py` | Solves the portfolio problem and returns optimal weights |
| `Portfolio.returns()` | `src/Portfolio.py` | Accessor for the returns matrix |
| `Portfolio.numassets()` | `src/Portfolio.py` | Number of assets in the portfolio |
| `ConstraintsFunctions.py` | `src/ConstraintsFunctions.py` | Constraint builders: weight bounds, group, factor exposures |
| `ParamsEstimation.py` | `src/ParamsEstimation.py` | Covariance/returns estimation parameters |
| `AuxFunctions.py` | `src/AuxFunctions.py` | Shared helpers for the optimizer stack |

## Common Patterns

- **Classic MV**: `port = rp.Portfolio(returns=Y); port.assetsstatistics(method_mu='hist',
  method_cov='hist', d=0.94); w = port.optimization(model='Classic',
  rm='MV', obj='Sharpe', l=(0, 1))`.
- **Risk-budgeted**: `rm='CVaR'` with `obj='Sharpe'` — tail-aware tangency.
- **Constraints**: `port.ainequality`/`port.binequality` for linear constraints;
  `ConstraintsFunctions` for structured ones (group/factor).
- **Frontier sweep**: iterate `obj='MinRisk'` targets or use `PlotFunctions` for the
  efficient frontier.

## Pitfalls

- **Statistics first**: `assetsstatistics()` must run before `optimization()` — the problem
  is built from its outputs.
- **Risk measure choice**: MV underestimates tail risk; use CVaR/CDaR for fat-tailed
  universes.
- **Scale**: returns should be decimal (not %) or the solver tolerances misfire.

## Provenance

Graph: `knowledge_graphs/riskfolio/.graphify/graph.json` — 426 nodes · 599 edges ·
29 communities · graphify @ 632a9e48fbaf, backend opencode.

## Verification Checklist

- [ ] `rp.Portfolio(returns=Y).optimization(model='Classic', rm='MV', obj='Sharpe')` runs
- [ ] QR rows cite source files resolvable in the riskfolio graph
