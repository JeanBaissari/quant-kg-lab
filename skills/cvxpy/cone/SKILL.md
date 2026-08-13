---
name: cvxpy-cone
description: "Use when working with cvxpy constraints — equality/inequality, second-order, exponential, power and PSD cones that make a problem DCP-solvable."
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
| `Equality` | `constraints/zero.py` | Affine equality constraint `expr == 0` (built by `==`) |
| `NonPos` | `constraints/nonpos.py` | Affine inequality `expr <= 0` (built by `<=`) |
| `SOC` | `constraints/second_order.py` | Second-order cone constraint `||x|| <= t` |
| `ExpCone` | `constraints/exponential.py` | Exponential cone (log/exp constraints) |
| `PSD` | `constraints/psd.py` | Positive-semidefinite constraint on a symmetric matrix variable |
| `Constraint` | `constraints/constraint.py` | Base class: `dual_value`, violation, and canonicalization hooks |

## Common Patterns

- **Standard LP/QP form**: constraints = `[A @ x == b, G @ x <= h]` — affine only, keeps the
  solver fast.
- **Second-order cone**: `cp.SOC(t, x)` for `||x||_2 <= t` — convex, SOCP-solvable.
- **Matrix PSD**: declare `X = Variable((n, n), PSD=True)` — the cleaner idiom vs a PSD
  constraint.
- **Inspect duals**: `constraint.dual_value` after solve — shadow prices for finance
  (portfolio risk budget sensitivity).

## Pitfalls

- **`>=`/`<=` on vectors** produce elementwise constraints — one row per inequality, not a
  norm ball.
- **Strict inequalities are not supported** — `x > 0` is rejected; use `x >= eps` with a
  small positive `eps`.
- **Non-affine constraints** (e.g. `x * y <= 1`) break DCP — reformulate with the right cone.

## Provenance

Graph: `knowledge_graphs/cvxpy/.graphify/graph.json` — 6330 nodes · 16465 edges ·
297 communities · graphify @ e3b50dccf808, backend opencode.

## Verification Checklist

- [ ] `[A @ x == b, G @ x <= h]`-style problems solve with SCS
- [ ] `SOC(t, x)` constraint is DCP
