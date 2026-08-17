---
name: cvxpy
description: "Use when working with cvxpy \u2014 the convex-optimization entry point.\
  \ Router indexing the cvxpy sub-skills; load the sub-skill for the layer you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: cvxpy/cvxpy
source_commit: e3b50dccf808e52e36f7b134b710e0e245742cc0
extraction_date: 2026-08-12
graph:
  nodes: 6380
  edges: 16515
  community_count: 297
  graph_hash: 5473cba3f4275a9b
tags:
- cvxpy
- router
related_skills:
- cvxpy-core
- cvxpy-cone
- cvxpy-problems
- cvxpy-atoms
- cvxpy-solvers
- numpy-core
- pyportfolioopt-efficient-frontier
target_version: '1.9.2 (dev: after 1.9.2)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `cvxpy` ahead of the latest PyPI release (1.9.2 (dev: after 1.9.2)). Some APIs may not exist in your installed version.

# cvxpy

Disciplined convex programming in Python: variables, objectives, conic
constraints, atoms, and solvers — the engine underneath portfolio optimizers
like PyPortfolioOpt.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [core](core/SKILL.md) | Variable/Parameter/Constant, Minimize/Maximize, DCP |
| [cone](cone/SKILL.md) | Equality/NonPos/SOC/ExpCone/PSD constraints, dual values |
| [problems](problems/SKILL.md) | Problem.solve(), status/stats, warm starts, canonicalization |
| [atoms](atoms/SKILL.md) | norm/quad_form/elementwise/matrix atoms, curvature rules |
| [solvers](solvers/SKILL.md) | solver families (Clarabel/SCS/OSQP/ECOS), solver_opts, duals |

## Common Patterns

- **Model → solve**: define variables, build objective + constraints, `Problem(...).solve()`.
- **Quant use**: portfolio optimization (PyPortfolioOpt wraps cvxpy), risk budgeting with
  dual values, calibration/regression as QPs.
- **Parametrized re-solves**: Parameters + cached canonicalization for frontier sweeps.

## Provenance

Graph: `knowledge_graphs/cvxpy/.graphify/graph.json` — 6380 nodes · 16465 edges ·
297 communities · graphify @ e3b50dccf808, backend opencode.

## Verification Checklist

- [ ] Router links resolve to the 5 module skills
- [ ] `related_skills` names resolve to real skills
