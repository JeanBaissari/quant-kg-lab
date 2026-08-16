---
name: cvxpy-core
description: "Use when solving convex optimization problems with cvxpy \u2014 variables,\
  \ parameters, objectives, Problem.solve(), and DCP analysis."
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
  graph_hash: e985870ca0f4d020
tags:
- cvxpy
- convex-optimization
related_skills:
- cvxpy
- cvxpy-cone
- cvxpy-problems
- numpy-core
---

# cvxpy.core

Disciplined convex programming: model a problem with `Variable`/`Parameter`,
`Minimize`/`Maximize` objectives, atoms and constraints — then `Problem.solve()`
canonicalizes and dispatches to a solver (SCS/ECOS/OSQP/Clarabel).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Variable` | `expressions/variable.py:L34` | Decision variable with shape and attributes (nonneg, symmetric, PSD...) |
| `Parameter` | `expressions/constants/parameter.py:L36` | Solver-side constant you can change between solves (warm re-solve) |
| `Constant` | `expressions/constants/constant.py:L34` | Fixed numeric constant in an expression tree |
| `Expression` | `expressions/expression.py:L144` | Base of the expression tree — value, shape, is_affine()/is_convex() |
| `Minimize` | `problems/objective.py:L118` | Minimization objective — `Minimize(cost_expr)` |
| `Maximize` | `problems/objective.py:L194` | Maximization objective — `Maximize(utility_expr)` |
| `Problem` | `problems/problem.py:L138` | Holds objective + constraints; `solve()` returns the optimal value |
| `norm()` | `atoms/norm.py:L30` | Convex atom: vector/matrix norm (p-norm, spectral, nuclear) |
| `quad_form()` | `atoms/quad_form.py:L290` | Convex atom: quadratic form xᵀPx with P PSD |
| `sum_squares()` | `atoms/sum_squares.py:L21` | Convex atom: sum of squared entries — least-squares staple |

## Common Patterns

- **Least squares**: `x = Variable(n); prob = Problem(Minimize(sum_squares(A @ x - b))); prob.solve()`.
- **Parameters for re-solve**: `p = Parameter(); x = Variable(n); prob = Problem(Minimize(sum_squares(p - x)))` —
  change `p.value` between `solve()` calls to warm-start families of problems (efficient
  frontier sweeps).
- **DCP check**: `prob.is_dcp()` / `expr.is_convex()` before solving — the solver only
  accepts DCP-compliant models.
- **Solver selection**: `prob.solve(solver=SCS)` or OSQP/Clarabel/ECOS; `prob.solver_stats` for
  iterations/time.
- **Portfolio optimization**: PyPortfolioOpt builds exactly this — `EfficientFrontier` wraps
  cvxpy Problems (see `pyportfolioopt-efficient-frontier`).

## Pitfalls

- **DCP violations**: products of two variables are non-convex — reformulate (e.g. use
  `quad_form` with PSD P instead of `x * P * x`).
- **Solver availability**: SCS/ECOS/OSQP ship with cvxpy; Clarabel needs an extra install —
  check `Problem.solver_stats`/`installed_solvers()`.
- **Parameter reuse**: set `.value` explicitly before each solve; stale values silently
  change the model.

## Provenance

Graph: `knowledge_graphs/cvxpy/.graphify/graph.json` — 6330 nodes · 16465 edges ·
297 communities · graphify @ e3b50dccf808, backend opencode.

## Verification Checklist

- [ ] `Problem(Minimize(sum_squares(A @ x - b))).solve()` runs with numpy A/b
- [ ] `prob.is_dcp()` True for the examples above
- [ ] QR rows cite source files resolvable in the cvxpy graph
