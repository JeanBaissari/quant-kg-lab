---
name: cvxpy-cone
description: "Use when working with cvxpy constraints \u2014 equality/inequality,\
  \ second-order, exponential, power and PSD cones that make a problem DCP-solvable."
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
  graph_hash: 844b4634a60894f8
tags:
- cvxpy
- constraints
- cones
related_skills:
- cvxpy
- cvxpy-core
- cvxpy-problems
---

# cvxpy.cone

Constraint surface of cvxpy: affine equality/inequality plus the conic families
(second-order, exponential, power, PSD) that canonicalization turns into solver
cone programs.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Equality` | `constraints/zero.py:L105` | Affine equality constraint `expr == 0` (built by `==`) |
| `NonPos` | `constraints/nonpos.py:L25` | Affine inequality `expr <= 0` (built by `<=`) |
| `SOC` | `constraints/second_order.py:L25` | Second-order cone constraint `||x|| <= t` |
| `ExpCone` | `constraints/exponential.py:L30` | Exponential cone (log/exp constraints) |
| `PSD` | `constraints/psd.py:L25` | Positive-semidefinite constraint on a symmetric matrix variable |
| `Constraint` | `constraints/constraint.py` | Base class: `dual_value`, violation, and canonicalization hooks |
| `PowCone` | `constraints/power.py` | Power cone x^α y^(1-α) >= |z| — convex constraints with powers |
| `Zero` | `constraints/zero.py` | Canonical equality used by the solver reduction layer |
| `NonNeg` | `constraints/nonpos.py` | Canonical inequality `expr >= 0` |
| `Constraint.violation()` | `constraints/constraint.py` | Measure of how far a candidate point violates the constraint |
| `Constraint.dual_value` | `constraints/constraint.py` | Shadow price / KKT multiplier after solve |

## Common Patterns

- **Standard LP/QP form**: constraints = `[A @ x == b, G @ x <= h]` — affine only, keeps the
  solver fast.
- **Second-order cone**: `cp.SOC(t, x)` for `||x||_2 <= t` — convex, SOCP-solvable.
- **Matrix PSD**: declare `X = Variable((n, n), PSD=True)` — the cleaner idiom vs a PSD
  constraint.
- **Inspect duals**: `constraint.dual_value` after solve — shadow prices for finance
  (portfolio risk budget sensitivity).
- **Bounding norms**: `cp.norm(w - w0, 2) <= tol` — turnover/weight deviation caps via SOC.
- **Exponential-cone utility**: `cp.sum(cp.log(w)) <= target` style constraints — log
  utility with a floor (requires ExpCone-capable solvers: SCS/Clarabel/ECOS).
- **Block-diagonal PSD**: `X = Variable((n, n), PSD=True)` then `X[sub, sub]` blocks —
  keep block structure explicit for faster canonicalization.

## Pitfalls

- **`>=`/`<=` on vectors** produce elementwise constraints — one row per inequality, not a
  norm ball.
- **Strict inequalities are not supported** — `x > 0` is rejected; use `x >= eps` with a
  small positive `eps`.
- **Non-affine constraints** (e.g. `x * y <= 1`) break DCP — reformulate with the right cone.
- **SOC(t, x) argument order**: `SOC(t, x)` means `||x|| <= t` — the scalar comes FIRST;
  swapping is a silent wrong model.
- **PSD on non-symmetric input**: passing a non-symmetric expression to a PSD constraint
  errors — build `X = Variable((n, n), symmetric=True)` or `X + X.T`.
- **ExpCone solver support**: ECOS and some QP solvers cannot handle exponential cones —
  fall back to SCS/Clarabel or check `installed_solvers()`.

## Provenance

Graph: `knowledge_graphs/cvxpy/.graphify/graph.json` — 6380 nodes · 16465 edges ·
297 communities · graphify @ e3b50dccf808, backend opencode.

## Verification Checklist

- [ ] `[A @ x == b, G @ x <= h]`-style problems solve with SCS
- [ ] `SOC(t, x)` constraint is DCP
- [ ] `constraint.dual_value` populated after solve
