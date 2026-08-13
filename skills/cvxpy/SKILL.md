---
name: cvxpy
description: "Use when working with cvxpy — the convex-optimization entry point. Router indexing the cvxpy sub-skills; load the sub-skill for the layer you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: cvxpy/cvxpy
source_commit: e3b50dccf808e52e36f7b134b710e0e245742cc0
extraction_date: 2026-08-12
graph:
  nodes: 6379
  edges: 16514
  community_count: 297
  graph_hash: 844b4634a60894f8
tags:
- cvxpy
- router
related_skills:
- cvxpy-core
- cvxpy-cone
- cvxpy-problems
- numpy-core
- pyportfolioopt-efficient-frontier
---

# cvxpy

Disciplined convex programming in Python: variables, objectives, conic
constraints, and solvers — the engine underneath portfolio optimizers like
PyPortfolioOpt.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [core](core/SKILL.md) | Variable/Parameter/Constant, Minimize/Maximize, atoms (norm, quad_form, sum_squares), DCP |
| [cone](cone/SKILL.md) | Equality/NonPos/SOC/ExpCone/PSD constraints, dual values |
| [problems](problems/SKILL.md) | Problem.solve(), solver selection (SCS/ECOS/OSQP/Clarabel), warm starts, stats |

## Common Patterns

- **Model → solve**: define variables, build objective + constraints, `Problem(...).solve()`.
- **Quant use**: portfolio optimization (PyPortfolioOpt wraps cvxpy), risk budgeting with
  dual values, calibration/regression as QPs.
- **Parametrized re-solves**: Parameters + cached canonicalization for frontier sweeps.

## Provenance

Graph: `knowledge_graphs/cvxpy/.graphify/graph.json` — 6330 nodes · 16465 edges ·
297 communities · graphify @ e3b50dccf808, backend opencode.

## Verification Checklist

- [ ] Router links resolve to the 3 module skills
- [ ] `related_skills` names resolve to real skills
