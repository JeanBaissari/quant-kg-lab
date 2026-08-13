---
name: cvxpy-problems
description: "Use when driving cvxpy problem lifecycle — Problem.solve() options, solver stats, warm starts, and solver selection (SCS/ECOS/OSQP/Clarabel)."
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
- problems
- solvers
related_skills:
- cvxpy
- cvxpy-core
- cvxpy-cone
---

# cvxpy.problems

The solve lifecycle: `Problem(Minimize(obj), constraints)`, `solve()` options,
solver selection and stats, and the canonicalization/reduction pipeline.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Problem` | `problems/problem.py` | Objective + constraints container; `solve()` returns the optimal value |
| `installed_solvers()` | `reductions/solvers/defines.py` | Lists solver backends available in this install |
| `SCS` | `reductions/solvers/conic_solvers/scs_conif.py` | Splitting-conic-solver backend (default conic) |
| `ECOS` | `reductions/solvers/conic_solvers/ecos_conif.py` | Embedded cone solver (SOCP) |
| `OSQP` | `reductions/solvers/qp_solvers/osqp_qpif.py` | QP-first solver — fastest on pure QPs |
| `Clarabel` | `reductions/solvers/conic_solvers/clarabel_conif.py` | Modern interior-point conic solver |

## Common Patterns

- **Basic solve**: `prob.solve()` — default solver chosen by the canonicalization chain.
- **Explicit solver**: `prob.solve(solver=OSQP, verbose=True)` for QPs; SCS for large conic.
- **Warm starts**: fix `Parameter.value`, re-call `solve()` — canonicalization is cached
  across solves with unchanged structure.
- **Stats**: `prob.solver_stats.iter_count`, `.solve_time` — budget solver time in
  optimization loops (e.g. portfolio frontier sweeps).

## Pitfalls

- **Default solver ≠ fastest**: cvxpy picks by problem class; OSQP is usually fastest for
  QPs, SCS more robust on large conic.
- **`verbose=True` spam**: silence production loops; keep it for debugging.
- **Numerical tolerance**: SCS is first-order — tighten `eps` for finance-grade accuracy or
  prefer interior-point (Clarabel/ECOS).

## Provenance

Graph: `knowledge_graphs/cvxpy/.graphify/graph.json` — 6330 nodes · 16465 edges ·
297 communities · graphify @ e3b50dccf808, backend opencode.

## Verification Checklist

- [ ] `prob.solve(solver=OSQP)` on a QP returns a value and stats
- [ ] QR rows cite source files resolvable in the cvxpy graph
