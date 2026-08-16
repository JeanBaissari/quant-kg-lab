---
name: numpy-ufuncs
description: "Use when working with NumPy universal functions \u2014 element-wise\
  \ ufuncs (arithmetic/math/comparison), reduction methods, broadcasting rules, einsum,\
  \ and error-state configuration."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
source_commit: ab2199763cb17878cd8f34fcbc97106c5397f922
extraction_date: 2026-08-13
graph:
  nodes: 8306
  edges: 13483
  community_count: 619
  graph_hash: d4d4b78b27085eac
tags:
- numpy
- ufuncs
- broadcasting
- einsum
related_skills:
- numpy
- numpy-core
- numpy-linalg
- pandas-core
target_version: '2.5.1 (dev: after 2.5.1, before 2.5.2)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `numpy` ahead of the latest PyPI release (2.5.1 (dev: after 2.5.1, before 2.5.2)). Some APIs may not exist in your installed version.

# NumPy ufuncs & broadcasting

Element-wise computation layer: ufuncs (C-implemented, SIMD) apply operations with
broadcasting; reduction methods collapse axes; einsum expresses arbitrary tensor
contractions; `seterr`/`errstate` control floating-point error handling.

## Quick Reference

| API | Signature | Description | Graph Node |
|-----|-----------|-------------|------------|
| `add` | `np.add(a, b)` | Element-wise addition — the canonical ufunc |
| `einsum` | `np.einsum(subscripts, *operands)` | Einstein summation — any tensor contraction | `_core/einsumfunc.py:L1243` |
| `broadcast_to` | `np.broadcast_to(arr, shape)` | Explicit broadcast to a target shape (read-only view) |
| `broadcast_shapes` | `np.broadcast_shapes(*shapes)` | Resolve the broadcast result shape of inputs | `lib/_stride_tricks_impl.py:L541` |

| `seterr` | `np.seterr(all='warn')` | Set floating-point error handling (ignore/warn/raise) | `_core/_ufunc_config.py:L20` |

| `geterr` | `np.geterr()` | Current floating-point error settings | `_core/_ufunc_config.py:L112` |

| `ufunc` | `np.ufunc` | The ufunc type — `add.reduce`, `multiply.accumulate`, `outer` |
| `ndarray` | `np.ndarray` | The N-dimensional array — ufunc operand |

## Common Patterns

- **Vectorized arithmetic**: `np.add(a, b)` / `a + b` — ufuncs under the hood; avoid
  Python loops over arrays.
- **Reductions**: `np.add.reduce(a)` (sum), `np.multiply.reduce(a)` (product),
  `np.add.accumulate(a)` (cumsum), `np.multiply.outer(a, b)` (outer product).
- **In-place scatter**: `np.add.at(arr, indices, values)` — unbuffered in-place
  addition (the safe alternative to `arr[idx] += v` for repeated indices).
- **Broadcasting rules**: prepend 1s to the smaller shape; size-1 dims expand; any
  other mismatch raises. `(3,1)+(1,4)→(3,4)`, `(3,4)+(4,)→(3,4)`.
- **Explicit broadcast**: `np.broadcast_to(a[:, None], (3,4))` — make intent visible;
  `np.broadcast_arrays(a, b)` for several aligned arrays.
- **einsum as a Swiss Army knife**: matmul `'ij,jk->ik'`, batch matmul
  `'bij,bjk->bik'`, trace `'ii->'`, diagonal `'ii->i'`, outer `'i,j->ij'`, transpose
  `'ij->ji'`; `np.einsum_path` for optimal contraction order on long chains.
- **Error control**: `with np.errstate(divide='ignore'):` — local, scoped FP handling
  (avoids global `seterr` leakage).

## Pitfalls

- **`broadcast_to` is read-only**: writing to the result raises — use
  `np.array(...)`/`np.copy` when mutation is needed.
- **`np.add.at` vs `arr[idx] += v`**: repeated indices in `+=` silently drop values —
  `add.at` is the correct scatter.
- **einsum string errors**: mismatched subscripts raise at call time — verify the
  equation against shapes before wrapping in hot loops.
- **seterr is global**: `np.seterr` changes process-wide state — prefer the
  `errstate` context manager.
- **Size-1 broadcasting surprises**: `(3,1)` + `(4,)` broadcasts fine — but a `(3,)`
  + `(4,)` mismatch raises; check shapes before relying on the rules.
- **Ufunc dtype promotion**: mixed dtypes (int + float) promote silently — cast
  explicitly when the result dtype matters.

## Provenance

Graph: `knowledge_graphs/numpy/.graphify/graph.json` — 8306 nodes · 13483 edges ·
670 communities · graphify @ ab2199763c, backend opencode, description coverage ~84%.
Split from `numpy-core` (QKG_055).

## Verification Checklist

- [ ] `np.einsum('ij,jk->ik', A, B)` equals `A @ B`
- [ ] `np.add.reduce(a)` / `np.add.accumulate(a)` run on a small array
- [ ] QR rows cite graph-resolvable numpy nodes
