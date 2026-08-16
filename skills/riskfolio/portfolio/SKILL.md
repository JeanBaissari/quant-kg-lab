---
name: riskfolio-portfolio
description: "Use when building constrained portfolio optimizations with Riskfolio-Lib\
  \ \u2014 Portfolio, risk measures, constraints, and the cvxpy-backed optimization()\
  \ call."
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
target_version: '7.3.0 (dev: after 7.3.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `riskfolio` ahead of the latest PyPI release (7.3.0 (dev: after 7.3.0)). Some APIs may not exist in your installed version.

# riskfolio.portfolio

Constrained mean-risk portfolio optimization: `Portfolio` builds the problem
(returns, cov/risk measures, constraints) and `optimization()` solves it via
cvxpy — MV/CVaR/CDaR/EVaR objectives under weight/group/factor constraints.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Portfolio` | `src/Portfolio.py:L56` | Builds the optimization problem: returns, risk measure, constraints |
| `Portfolio.optimization()` | `src/Portfolio.py:L1978` | Solves the portfolio problem and returns optimal weights |
| `Portfolio.returns()` | `src/Portfolio.py:L510` | Accessor for the returns matrix |
| `Portfolio.numassets()` | `src/Portfolio.py:L531` | Number of assets in the portfolio |
| `Portfolio.ainequality()` | `src/Portfolio.py:L595` | Inequality constraint matrices (A/b) for the LP/QP form |
| `Portfolio.binequality()` | `src/Portfolio.py:L619` | Inequality bound vector |
| `Portfolio.arcinequality()` | `src/Portfolio.py:L639` | Return constraints (min/max per asset return) |
| `Portfolio.afrcinequality()` | `src/Portfolio.py:L683` | Factor-return inequality matrices |
| `assets_constraints()` | `src/ConstraintsFunctions.py:L37` | Weight bounds, group/sector caps, leverage limits |
| `integer_constraints()` | `src/ConstraintsFunctions.py:L397` | Cardinality/round-lot integer constraints |
| `assets_views()` | `src/ConstraintsFunctions.py:L717` | Views on asset returns (Black-Litterman style) |
| `risk_constraint()` | `src/ConstraintsFunctions.py:L1745` | Portfolio-level risk cap constraint |
| `hrp_constraints()` | `src/ConstraintsFunctions.py:L1597` | HRP-family constraint wiring |
| `assets_clusters()` | `src/ConstraintsFunctions.py:L1428` | Cluster assignment from a codependence matrix |
| `ParamsEstimation.py:L1` | `src/ParamsEstimation.py:L1` | Covariance/returns estimation parameters |
| `AuxFunctions.py:L1` | `src/AuxFunctions.py:L1` | Shared helpers for the optimizer stack |

## Common Patterns

- **Classic MV**: `port = rp.Portfolio(returns=Y); port.assetsstatistics(method_mu='hist',
  method_cov='hist', d=0.94); w = port.optimization(model='Classic',
  rm='MV', obj='Sharpe', l=(0, 1))`.
- **Risk-budgeted**: `rm='CVaR'` with `obj='Sharpe'` — tail-aware tangency.
- **Constraints**: `port.ainequality`/`port.binequality` for linear constraints;
  `ConstraintsFunctions` for structured ones (group/factor).
- **Frontier sweep**: iterate `obj='MinRisk'` targets or use `PlotFunctions` for the
  efficient frontier.
- **Sector caps**: `assets_constraints(w, cov, ...)` with `groups` + `group_max` — cap
  sector exposure in one call.
- **Views**: `assets_views(w_views, mu, cov, ...)` — tilt the optimizer toward a
  forecast view (BL-style) without a full Black-Litterman model.
- **Risk cap**: `risk_constraint(...)` — bind total portfolio risk to a level while
  optimizing a different objective.
- **Custom LP/QP access**: read `port.ainequality()` / `port.binequality()` after setup —
  audit the exact linear program before solving.

## Pitfalls

- **Statistics first**: `assetsstatistics()` must run before `optimization()` — the problem
  is built from its outputs.
- **Risk measure choice**: MV underestimates tail risk; use CVaR/CDaR for fat-tailed
  universes.
- **Scale**: returns should be decimal (not %) or the solver tolerances misfire.
- **Weight-bounds feasibility**: `l=(0, 1)` plus group constraints can conflict — when the
  solver reports infeasibility, relax the binding constraint rather than the risk measure.
- **Views vs bounds**: asset views and hard weight bounds interact nonlinearly — check the
  resulting weights for hidden corner solutions.

## Provenance

Graph: `knowledge_graphs/riskfolio/.graphify/graph.json` — 426 nodes · 599 edges ·
29 communities · graphify @ 632a9e48fbaf, backend opencode.

## Verification Checklist

- [ ] `rp.Portfolio(returns=Y).optimization(model='Classic', rm='MV', obj='Sharpe')` runs
- [ ] QR rows cite source files resolvable in the riskfolio graph
