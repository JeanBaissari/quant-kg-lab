---
name: cvxpy-solvers
description: "Use when choosing and tuning cvxpy solvers \u2014 solver families and\
  \ tradeoffs, dual values, solver options, warm starts, and reading solver_stats."
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
- solvers
- clarabel
- scs
- osqp
- duals
related_skills:
- cvxpy
- cvxpy-core
- cvxpy-problems
- cvxpy-atoms
- numpy-core
target_version: '1.9.2 (dev: after 1.9.2)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `cvxpy` ahead of the latest PyPI release (1.9.2 (dev: after 1.9.2)). Some APIs may not exist in your installed version.

# cvxpy.solvers

cvxpy canonicalizes every problem into a standard conic form and dispatches to
a numeric solver. Choosing the solver family — conic (SCS/Clarabel/ECOS),
QP (OSQP), LP (GLPK/HiGHS), or mixed-integer (CBC/SCIP) — sets speed, accuracy
and feature availability.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `CLARABEL` | `reductions/solvers/conic_solvers/clarabel_conif.py:L65` | Interior-point conic solver — default for new cvxpy; quad-objective support |
| `SCS` | `reductions/solvers/conic_solvers/scs_conif.py:L82` | First-order splitting conic solver — scalable, lower accuracy, warm-startable |
| `ECOS` | `reductions/solvers/conic_solvers/ecos_conif.py:L40` | Interior-point conic — small/medium, high accuracy |
| `OSQP` | `reductions/solvers/qp_solvers/osqp_qpif.py:L13` | ADMM QP solver — fast re-solves, warm-start friendly |
| `CBC` | `reductions/solvers/conic_solvers/cbc_conif.py:L28` | Mixed-integer LP solver (branch-and-cut) |
| `GLPK` | `reductions/solvers/conic_solvers/glpk_conif.py:L24` | LP solver — simplex/interior point via GLPK |
| `HiGHS` | `reductions/solvers/conic_solvers/highs_conif.py:L106` | Modern LP solver — dual simplex, fast |
| `Problem.solve()` | `problems/problem.py:L592` | Dispatch: solver=..., warm_start=..., solver_opts=..., verbose=... |
| `Problem.solver_stats` | `problems/problem.py:L525` | Solver stats: solve_time, iterations, setup_time, num_iters |
| `Problem.status` | `problems/problem.py:L226` | "optimal", "infeasible", "unbounded", "optimal_inaccurate", "user_limit" |
| `Problem.value` | `problems/problem.py:L216` | Optimal objective value after solve |
| `Problem.unpack_results()` | `problems/problem.py:L1423` | Repack solver solution into the problem (after manual solver runs) |
| `Constraint.dual_value` | `constraints/constraint.py:L356` | Dual variable of a constraint — sensitivity/KKT multipliers |
| `Variable.value` | `expressions/variable.py:L34` | Primal solution — attribute of the variable after solve |
| `installed_solvers()` | `reductions/solvers/defines.py:L120` | List of solvers importable in this environment |

## Common Patterns

- **Default choice**: `prob.solve()` → Clarabel for conic; for QP-only models
  `prob.solve(solver=OSQP)` is typically fastest.
- **Warm re-solves (portfolio sweeps)**: 
  ```python
  for lam in lams:
      p.value = lam
      prob.solve(solver=SCS, warm_start=True)
  ```
  — first-order solvers reuse the previous iterate; interior-point solvers
  re-factorize but keep the problem structure cached.
- **Reading duals**: `constraint.dual_value` — e.g. `w >= 0` duals tell you
  which constraints bind (marginally most valuable weights).
- **Verbose debugging**: `prob.solve(verbose=True)` prints iteration traces;
  `prob.solver_stats.num_iters` + `solve_time` for tuning.
- **Big sparse models**: SCS (or Clarabel with sparse data) beats interior
  point on large factor models; pass scipy.sparse matrices.

## Pitfalls

- **Accuracy vs speed**: first-order solvers (SCS) accept looser tolerances —
  set `solver_opts={"eps": 1e-5}` when duals feed downstream math; OSQP/ECOS
  default tolerances are tighter.
- **Status ≠ optimal**: always check `prob.status == "optimal"` — 
  "optimal_inaccurate" returns values you should not trade on.
- **Solver availability**: SCS/OSQP/ECOS ship with cvxpy; Clarabel, GLPK,
  HiGHS, CBC, SCIP need separate installs (`installed_solvers()` to check).
- **Warm start needs a feasible-ish starting point**: a fresh `Variable`
  starts at zero — for warm_start to help, seed `var.value` from the previous
  solution.
- **Mixed-integer limits**: `solver=GLPK_MI`/CBC add branch-and-bound; integer
  problems are much slower — keep the integer variable count small.
- **OSQP is QP-only**: passing a conic model (exp/log constraints) to OSQP
  raises — cvxpy falls back only when you omit the solver argument.

## Provenance

Graph: `knowledge_graphs/cvxpy/.graphify/graph.json` — 6380 nodes · 16465 edges ·
297 communities · graphify @ e3b50dccf808, backend opencode.

## Verification Checklist

- [ ] `installed_solvers()` returns the expected set for the environment
- [ ] `prob.solve(solver=SCS, warm_start=True)` twice with a changed parameter
- [ ] QR rows cite `reductions/solvers/**` files resolvable in the cvxpy graph
