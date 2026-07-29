---
name: numpy-linalg
description: NumPy linear algebra — solve, eig, eigh, svd, norm, det, inv, cholesky, qr, lstsq, pinv, matrix decompositions, and norms. Extracted from the NumPy knowledge graph.
version: 0.1.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
graph_hash: 20436_nodes_30581_edges
---

# NumPy Linear Algebra (`numpy.linalg`)

Linear algebra functions backed by BLAS and LAPACK. All functions operate on the last two axes by default for stacked (batched) matrices.

## Quick Reference: Top 10 APIs

| API | Signature | Description |
|-----|-----------|-------------|
| `solve` | `solve(a, b)` | Solve `a @ x = b` for x |
| `eig` | `eig(a)` | Eigenvalues and right eigenvectors of a square array |
| `eigh` | `eigh(a, UPLO='L')` | Eigenvalues/vectors of complex Hermitian or real symmetric matrix |
| `svd` | `svd(a, full_matrices=True)` | Singular Value Decomposition → U, S, Vh |
| `norm` | `norm(x, ord=None, axis=None)` | Matrix or vector norm |
| `det` | `det(a)` | Determinant of an array |
| `inv` | `inv(a)` | Multiplicative inverse of a matrix |
| `cholesky` | `cholesky(a)` | Cholesky decomposition (lower or upper triangular) |
| `qr` | `qr(a, mode='reduced')` | QR factorization → Q, R |
| `lstsq` | `lstsq(a, b, rcond=None)` | Least-squares solution to `a @ x = b` |

### Additional APIs (by degree rank from knowledge graph)

| API | Description |
|-----|-------------|
| `eigvals(a)` | Eigenvalues of a general matrix |
| `eigvalsh(a, UPLO='L')` | Eigenvalues of Hermitian/symmetric matrix |
| `pinv(a, rcond=1e-15)` | Moore-Penrose pseudo-inverse |
| `slogdet(a)` | Sign and natural log of determinant (avoids overflow) |
| `cond(x, p=None)` | Condition number of a matrix |
| `tensorinv(a, ind=2)` | Inverse of an N-dimensional array |
| `tensorsolve(a, b, axes=None)` | Solve tensor equation `a @ x = b` |
| `matrix_power(a, n)` | Raise a square matrix to integer power n |
| `matrix_rank(M, tol=None)` | Matrix rank using SVD method |
| `multi_dot(arrays)` | Optimal order dot product of 2+ arrays |
| `svdvals(x)` | Singular values only (no vectors) |
| `outer(a, b)` | Outer product of two vectors |
| `matmul(x1, x2)` | Matrix product of two arrays |
| `matrix_norm(x, ord='fro', axis=...)` | Matrix norm only |
| `vector_norm(x, ord=2, axis=None)` | Vector norm only |
| `cross(a, b, axisa=-1, axisb=-1, axisc=-1)` | Cross product of 3-element vectors |
| `vecdot(x1, x2, axis=-1)` | Vector dot product along an axis |
| `diagonal(x, offset=0, axis1=0, axis2=1)` | Return specified diagonals |
| `trace(x, offset=0, axis1=0, axis2=1)` | Sum along specified diagonals |
| `matrix_transpose(x)` | Transpose a matrix (or stack of matrices) |

### Result Types

| Type | Fields | Returned By |
|------|--------|-------------|
| `EigResult` | `eigenvalues`, `eigenvectors` | `eig()` |
| `EighResult` | `eigenvalues`, `eigenvectors` | `eigh()` |
| `QRResult` | `Q`, `R` | `qr()` |
| `SVDResult` | `U`, `S`, `Vh` | `svd()` (with `full_matrices=False` and `compute_uv=True`) |
| `SlogdetResult` | `sign`, `logabsdet` | `slogdet()` |

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
|--------|--------|----------|-------------|
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
