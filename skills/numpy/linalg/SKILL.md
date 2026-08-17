---
name: numpy-linalg
description: "Use when doing linear algebra with NumPy \u2014 solve, eig/eigh, svd,\
  \ qr, cholesky, inv, det, and norm."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
source_commit: ab2199763cb17878cd8f34fcbc97106c5397f922
extraction_date: 2026-07-29
graph:
  nodes: 8306
  edges: 13483
  community_count: 619
  graph_hash: f1603daca7bed1df
tags:
- numpy
- linalg
related_skills: []
target_version: '2.5.1 (dev: after 2.5.1, before 2.5.2)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `numpy` ahead of the latest PyPI release (2.5.1 (dev: after 2.5.1, before 2.5.2)). Some APIs may not exist in your installed version.

# NumPy Linear Algebra (`numpy.linalg`)

Linear algebra functions backed by BLAS and LAPACK. All functions operate on the last two axes by default for stacked (batched) matrices.

## Quick Reference

| API | Signature | Description | Graph Node |
|---|---------|-----------|----------|
| `solve` | `solve(a, b)` | Solve `a @ x = b` for x | linalg/_linalg.py:L374 |
| `eig` | `eig(a)` | Eigenvalues and right eigenvectors of a square array | linalg/_linalg.py:L1342 |
| `eigh` | `eigh(a, UPLO='L')` | Eigenvalues/vectors of complex Hermitian or real symmetric matrix | linalg/_linalg.py:L1489 |
| `svd` | `svd(a, full_matrices=True)` | Singular Value Decomposition → U, S, Vh | linalg/_linalg.py:L1642 |
| `norm` | `norm(x, ord=None, axis=None)` | Matrix or vector norm | linalg/_linalg.py:L2573 |
| `det` | `det(a)` | Determinant of an array | linalg/_linalg.py:L2331 |
| `inv` | `inv(a)` | Multiplicative inverse of a matrix | linalg/_linalg.py:L547 |
| `cholesky` | `cholesky(a)` | Cholesky decomposition (lower or upper triangular) | linalg/_linalg.py:L789 |
| `qr` | `qr(a, mode='reduced')` | QR factorization → Q, R | linalg/_linalg.py:L976 |
| `lstsq` | `lstsq(a, b, rcond=None)` | Least-squares solution to `a @ x = b` | linalg/_linalg.py:L2393 |

### Additional APIs (by degree rank from knowledge graph)

| API | Description | _core/code_generators/generate_numpy_api.py:L1 |
|-----|-------------|
| `eigvals(a)` | Eigenvalues of a general matrix | linalg/_linalg.py:L1157 |
| `eigvalsh(a, UPLO='L')` | Eigenvalues of Hermitian/symmetric matrix | linalg/_linalg.py:L1245 |
| `pinv(a, rcond=1e-15)` | Moore-Penrose pseudo-inverse | linalg/_linalg.py:L2129 |
| `slogdet(a)` | Sign and natural log of determinant (avoids overflow) | linalg/_linalg.py:L2247 |
| `cond(x, p=None)` | Condition number of a matrix | linalg/_linalg.py:L1889 |
| `tensorinv(a, ind=2)` | Inverse of an N-dimensional array | linalg/_linalg.py:L472 |
| `tensorsolve(a, b, axes=None)` | Solve tensor equation `a @ x = b` | linalg/_linalg.py:L293 |
| `matrix_power(a, n)` | Raise a square matrix to integer power n | linalg/_linalg.py:L667 |
| `matrix_rank(M, tol=None)` | Matrix rank using SVD method | linalg/_linalg.py:L2010 |
| `multi_dot(arrays)` | Optimal order dot product of 2+ arrays | linalg/_linalg.py:L2839 |
| `svdvals(x)` | Singular values only (no vectors) | linalg/_linalg.py:L1835 |
| `outer(a, b)` | Outer product of two vectors | _core/numeric.py:L906 |
| `matmul(x1, x2)` | Matrix product of two arrays | linalg/_linalg.py:L3292 |
| `matrix_norm(x, ord='fro', axis=...)` | Matrix norm only | linalg/_linalg.py:L3414 |
| `vector_norm(x, ord=2, axis=None)` | Vector norm only | linalg/_linalg.py:L3477 |
| `cross(a, b, axisa=-1, axisb=-1, axisc=-1)` | Cross product of 3-element vectors | _core/numeric.py:L1565 |
| `vecdot(x1, x2, axis=-1)` | Vector dot product along an axis | linalg/_linalg.py:L3579 |
| `diagonal(x, offset=0, axis1=0, axis2=1)` | Return specified diagonals | _core/fromnumeric.py:L1750 |
| `trace(x, offset=0, axis1=0, axis2=1)` | Sum along specified diagonals | _core/fromnumeric.py:L1886 |
| `matrix_transpose(x)` | Transpose a matrix (or stack of matrices) | _core/fromnumeric.py:L702 |

### Result Types

| Type | Fields | Returned By | _core/_add_newdocs_scalars.py:L76 |
|------|--------|-------------|
| `EigResult` | `eigenvalues`, `eigenvectors` | `eig()` | linalg/_linalg.py:L82 |
| `EighResult` | `eigenvalues`, `eigenvectors` | `eigh()` | linalg/_linalg.py:L86 |
| `QRResult` | `Q`, `R` | `qr()` | linalg/_linalg.py:L90 |
| `SVDResult` | `U`, `S`, `Vh` | `svd()` (with `full_matrices=False` and `compute_uv=True`) | linalg/_linalg.py:L98 |
| `SlogdetResult` | `sign`, `logabsdet` | `slogdet()` | linalg/_linalg.py:L94 |

## Common Patterns

```python
import numpy as np
from numpy import linalg as LA

# Solve linear system
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)  # array([2., 3.])

# Compute inverse
A_inv = np.linalg.inv(A)

# Eigenvalues and eigenvectors
w, v = np.linalg.eig(A)  # general
w, v = np.linalg.eigh(A)  # symmetric/Hermitian (faster, real eigenvalues)

# SVD for dimensionality reduction or pseudo-inverse
U, S, Vh = np.linalg.svd(A)
# Reconstruct: A ≈ U @ np.diag(S) @ Vh

# Compute determinant
d = np.linalg.det(A)
sign, logdet = np.linalg.slogdet(A)  # avoids overflow for large matrices

# Cholesky decomposition (A must be positive-definite)
L = np.linalg.cholesky(A)  # returns lower-triangular L where A = L @ L.T

# QR decomposition
Q, R = np.linalg.qr(A)

# Least squares
x, residuals, rank, sv = np.linalg.lstsq(A, b, rcond=None)

# Matrix norm
np.linalg.norm(A, ord='fro')     # Frobenius norm
np.linalg.norm(A, ord=2)         # Spectral norm (largest singular value)
np.linalg.norm(v, ord=2)         # Euclidean vector norm

# Condition number
c = np.linalg.cond(A)  # default: 2-norm

# Batch / stacked operations (last two axes)
A_batch = np.random.randn(5, 3, 3)  # 5 matrices, each 3x3
b_batch = np.random.randn(5, 3)
x_batch = np.linalg.solve(A_batch, b_batch)  # solves each system

# Pseudo-inverse
A_pinv = np.linalg.pinv(A)

# Multi-dot (optimal order for 3+ arrays)
result = np.linalg.multi_dot([A, B, C])
```

## Error Handling

All linalg functions raise `numpy.linalg.LinAlgError` on failure — a generic Python-exception-derived object. Common scenarios:

```python
from numpy.linalg import LinAlgError

try:
    x = np.linalg.solve(A, b)
except LinAlgError:
    print("Singular matrix")
```

## Pitfalls

1. **Singular matrices**: `solve()` and `inv()` raise `LinAlgError` for singular or near-singular matrices. Use `lstsq()` for over-determined systems, or `pinv()` for singular systems.

2. **eig vs eigh**: `eig()` is for general square matrices (returns complex eigenvalues). `eigh()` is for Hermitian/symmetric matrices only — it is faster and returns real eigenvalues. Using `eigh()` on non-symmetric input gives wrong results silently.

3. **det overflow**: Computing determinant directly can overflow for large matrices. Use `slogdet()` instead — it returns `(sign, log|det|)`, avoiding overflow.

4. **Cholesky for positive-definite only**: `cholesky()` requires the input to be positive-definite. If your matrix is only semi-definite or has negative eigenvalues, use `eigh()` or SVD instead.

5. **norm ambiguity**: The `norm()` function dispatches to `vector_norm()` or `matrix_norm()` based on `axis`. For explicit behavior, use `np.linalg.vector_norm()` or `np.linalg.matrix_norm()` directly.

## Cross-Library Bridges

| Source | Target | Relation | Description |
| -------- | ---------- | ------------- |
| numpy.linalg | `scipy.linalg` | **superset_of** | scipy.linalg extends numpy.linalg with additional decompositions (LU, Schur, polar, etc.) and sparse support |
| numpy.linalg | `scipy.sparse.linalg` | **data_source** | scipy sparse solvers consume numpy arrays as input |

- **scipy.linalg** provides: `lu`, `lu_factor`, `lu_solve`, `schur`, `polar`, `sqrtm`, `expm`, `logm`, `sinm`, `cosm`, `funm`, `solve_continuous_are`, `solve_discrete_are`, `subspace_angles`, `orthogonal_procrustes`, and more.
- **scipy.sparse.linalg** provides: `eigs`, `eigsh`, `svds`, `lobpcg`, `splu`, `spilu`, `cg`, `gmres`, `minres`, `bicgstab`, and iterative solvers for sparse systems.

## Verification Checklist

- [ ] `solve()` returns correct solution for well-conditioned system
- [ ] `solve()` raises `LinAlgError` for singular matrix
- [ ] `eigh()` returns real eigenvalues for symmetric input
- [ ] `eig()` handles complex eigenvalues for non-symmetric input
- [ ] `svd()` returns orthonormal U, Vh with correct singular values
- [ ] `norm()` dispatches correctly for matrix vs vector norms
- [ ] `det()` and `slogdet()` agree for non-degenerate matrices
- [ ] `cholesky()` reconstructs `A = L @ L.T`
- [ ] `qr()` reconstructs `A = Q @ R`
- [ ] `lstsq()` returns minimum-norm solution for under-determined systems
- [ ] Batch/stacked operations work correctly on last two axes
- [ ] `pinv(A) @ A @ pinv(A)` ≈ `pinv(A)` (Moore-Penrose property)

## Provenance

- Knowledge graph: numpy, 8094 nodes, 13271 edges, 670 communities
- God nodes: `f2c_d_lapack.c:L1` (124), `f2c_s_lapack.c:L1` (124), `umath_linalg.cpp` (101) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ ab2199763cb1, backend opencode, description coverage 83%
