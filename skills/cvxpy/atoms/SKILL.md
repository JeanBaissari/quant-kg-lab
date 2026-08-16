---
name: cvxpy-atoms
description: "Use when choosing cvxpy atoms \u2014 norm/quad_form/elementwise functions,\
  \ matrix atoms, and the curvature rules that keep models DCP."
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
  graph_hash: 0d326b4657b563eb
tags:
- cvxpy
- atoms
- dcp
- convex
related_skills:
- cvxpy
- cvxpy-core
- cvxpy-cone
- cvxpy-problems
- numpy-core
- pyportfolioopt-efficient-frontier
target_version: '1.9.2 (dev: after 1.9.2)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `cvxpy` ahead of the latest PyPI release (1.9.2 (dev: after 1.9.2)). Some APIs may not exist in your installed version.

# cvxpy.atoms

The building blocks of cvxpy models: each atom has a defined curvature,
monotonicity and shape signature that the DCP rules use to certify
convexity. Picking the right atom is what keeps a model solvable.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `norm()` | `atoms/norm.py:L30` | Vector/matrix norm — p-norm, spectral, nuclear, Frobenius |
| `quad_form()` | `atoms/quad_form.py:L290` | Quadratic form xᵀPx with P PSD — the risk term of portfolio problems |
| `quad_over_lin()` | `atoms/quad_over_lin.py:L29` | Convex quadratic-over-linear: quad_over_lin(x, y), y > 0 |
| `sum_squares()` | `atoms/sum_squares.py:L21` | Sum of squared entries — least-squares staple |
| `square()` | `atoms/elementwise/square.py:L21` | Elementwise square — convex |
| `abs` | `atoms/elementwise/abs.py:L25` | Elementwise absolute value — convex |
| `pos()` | `atoms/elementwise/pos.py:L21` | Positive part max(x, 0) — convex |
| `log` | `atoms/elementwise/log.py:L24` | Elementwise log — concave, DCP with positive argument |
| `exp` | `atoms/elementwise/exp.py:L24` | Elementwise exp — convex |
| `inv_pos()` | `atoms/elementwise/inv_pos.py:L21` | 1/x for x > 0 — convex |
| `power()` | `atoms/elementwise/power.py:L32` | x^p elementwise — convex/concave by p |
| `sqrt()` | `atoms/elementwise/sqrt.py:L23` | sqrt(x) — concave |
| `kl_div` | `atoms/elementwise/kl_div.py:L26` | x·log(x/y) — convex (relative entropy) |
| `max` | `atoms/max.py:L25` | Elementwise max across axes — convex |
| `min` | `atoms/min.py:L25` | Elementwise min — concave |
| `sum_largest` | `atoms/sum_largest.py:L23` | Sum of the k largest entries — convex |
| `sum_smallest()` | `atoms/sum_smallest.py:L21` | Sum of the k smallest entries — concave |
| `lambda_max` | `atoms/lambda_max.py:L27` | Largest eigenvalue of symmetric matrix — convex |
| `lambda_min()` | `atoms/lambda_min.py:L21` | Smallest eigenvalue — concave |
| `matrix_frac()` | `atoms/matrix_frac.py:L148` | xᵀP⁻¹x with P PSD — convex |
| `trace()` | `atoms/affine/trace.py:L29` | Matrix trace — affine |
| `matmul()` | `atoms/affine/binary_operators.py:L122` | Matrix multiplication @ — affine |
| `AddExpression` | `atoms/affine/add_expr.py:L32` | Affine sum — what `+` builds |
| `MulExpression` | `atoms/affine/binary_operators.py:L127` | Affine product — what `*` builds |

## Common Patterns

- **Risk terms**: `quad_form(w, Sigma)` for variance; `norm(w - w0, 2)` for
  turnover penalty; `sum_squares(w - target)` for tracking error.
- **Penalties**: `norm(x, 1)` for sparsity/LASSO; `sum_largest(losses, k)` for
  worst-case CVaR-style objectives; `kl_div` for distributional distance.
- **Elementwise vs matrix**: `abs`, `square`, `pos` are elementwise; `norm`
  and `quad_form` collapse dimensions — shape matters for constraint lists.
- **Concave utility**: `log`, `sqrt`, `min`, `lambda_min` are concave — use
  them in `Maximize` objectives (maximize log-utility).
- **Reformulating products**: a product of two variables is never DCP — use
  `quad_form` (PSD), `matrix_frac`, or introduce auxiliaries instead.

## Pitfalls

- **DCP violation**: composing convex(concave) is fine only under the
  monotonicity rules — `norm(x) ** 2` is not DCP; use `sum_squares(x)`.
- **PSD requirement**: `quad_form(x, P)` and `matrix_frac` require P PSD —
  pass `PSD=True` on the Parameter or use `psd_wrap`.
- **`power()` domain**: `power(x, 0)` is not allowed; fractional powers need
  positive arguments (constrain or use `pos()`).
- **lambda_max needs symmetric input**: pass a symmetric variable or
  `x + x.T`-style expressions, otherwise the atom silently assumes symmetry.
- **Large quad_forms**: `quad_form` densifies the matrix — for large P prefer
  factorized/scipy-sparse-friendly formulations.

## Provenance

Graph: `knowledge_graphs/cvxpy/.graphify/graph.json` — 6380 nodes · 16465 edges ·
297 communities · graphify @ e3b50dccf808, backend opencode.

## Verification Checklist

- [ ] `norm(w, 1)` / `quad_form(w, Sigma)` / `sum_squares(x)` are DCP in a test model
- [ ] `prob.is_dcp()` True for each QR pattern
- [ ] QR rows cite `atoms/*.py` files resolvable in the cvxpy graph
