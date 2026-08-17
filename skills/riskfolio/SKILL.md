---
name: riskfolio
description: "Use when working with Riskfolio-Lib \u2014 the portfolio-optimization\
  \ entry point. Router indexing the riskfolio sub-skills; load the sub-skill for\
  \ the construction method you need."
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
  graph_hash: 372545b1ab9706e9
tags:
- riskfolio
- router
related_skills:
- riskfolio-portfolio
- riskfolio-risk-measures
- riskfolio-hrp
- cvxpy
- pyportfolioopt
target_version: '7.3.0 (dev: after 7.3.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `riskfolio` ahead of the latest PyPI release (7.3.0 (dev: after 7.3.0)). Some APIs may not exist in your installed version.

# riskfolio

Constraint/risk-based portfolio optimization (cvxpy-backed) plus hierarchical
construction (HRP/HERC) — the deeper counterpart to PyPortfolioOpt.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [portfolio](portfolio/SKILL.md) | Portfolio + optimization(), constraints, statistics |
| [risk_measures](risk_measures/SKILL.md) | MV/CVaR/CDaR/MAD/LPM, risk contribution, matrix helpers |
| [hrp](hrp/SKILL.md) | HCPortfolio HRP/HERC, DBHT clustering |

## Common Patterns

- **Classic vs hierarchical**: use Portfolio for constrained mean-risk; HCPortfolio when
  the covariance is ill-conditioned.
- **Tail risk**: CVaR/CDaR objectives when returns are fat-tailed.

## Provenance

Graph: `knowledge_graphs/riskfolio/.graphify/graph.json` — 426 nodes · 599 edges ·
29 communities · graphify @ 632a9e48fbaf, backend opencode.

## Verification Checklist

- [ ] Router links resolve to the 3 module skills
- [ ] `related_skills` names resolve to real skills
