# Edge Audit — cvxpy

**Date**: 2026-08-12

## Summary

- Total edges: 16465
- EXTRACTED: 7054 (42.8%)
- INFERRED: 9411 (57.2%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `Constraint`: 801 inferred edges
- `Expression`: 612 inferred edges
- `Atom`: 453 inferred edges
- `Solution`: 442 inferred edges
- `Variable`: 387 inferred edges
- `reshape`: 305 inferred edges
- `AffAtom`: 294 inferred edges
- `ConicSolver`: 274 inferred edges
- `Elementwise`: 235 inferred edges
- `conj`: 177 inferred edges
- `multiply`: 161 inferred edges
- `CvxpyDeprecationWarning`: 161 inferred edges
- `AxisAtom`: 155 inferred edges
- `Minimize`: 132 inferred edges
- `log`: 131 inferred edges
- `Constant`: 129 inferred edges
- `DictTensorView`: 129 inferred edges
- `PythonCanonBackend`: 129 inferred edges
- `TensorRepresentation`: 129 inferred edges
- `Solver`: 122 inferred edges

## Cross-Module Suspicious Edges

- `expression.py` ↔ `elementwise`: 656
- `expression.py` ↔ `affine`: 437
- `solvers` ↔ `solution.py`: 365
- `affine` ↔ `constraint.py`: 259
- `affine` ↔ `expression.py`: 190
- `problem.py` ↔ `solvers`: 132
- `elementwise` ↔ `constraint.py`: 118
- `expression.py` ↔ `variable.py`: 110
- `expression.py` ↔ `warn.py`: 110
- `solvers` ↔ `dcp2cone`: 100
- `complex2real` ↔ `affine`: 90
- `problem.py` ↔ `objective.py`: 88
- `cone2cone` ↔ `second_order.py`: 78
- `cone2cone` ↔ `nonpos.py`: 72
- `solvers` ↔ `error.py`: 66
- `solvers` ↔ `cone2cone`: 61
- `cone2cone` ↔ `psd.py`: 54
- `cone2cone` ↔ `affine`: 53
- `solvers` ↔ `versioning.py`: 52
- `affine` ↔ `error.py`: 51
