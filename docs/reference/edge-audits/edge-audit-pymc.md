# Edge Audit — pymc

**Date**: 2026-08-13

## Summary

- Total edges: 11136
- EXTRACTED: 5224 (46.9%)
- INFERRED: 5912 (53.1%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `SymbolicRandomVariable`: 319 inferred edges
- `DictToArrayBijection`: 314 inferred edges
- `MeasurableOp`: 230 inferred edges
- `MinibatchOp`: 200 inferred edges
- `Distribution`: 180 inferred edges
- `Continuous`: 167 inferred edges
- `MultiTrace`: 150 inferred edges
- `RaveledVars`: 147 inferred edges
- `MeasurableElemwise`: 131 inferred edges
- `BlockModelAccessError`: 120 inferred edges
- `SamplingError`: 116 inferred edges
- `PointFunc`: 106 inferred edges
- `ShapeError`: 100 inferred edges
- `SplineWrapper`: 100 inferred edges
- `NDArray`: 99 inferred edges
- `SimulatorRV`: 97 inferred edges
- `ParameterValueError`: 97 inferred edges
- `Discrete`: 95 inferred edges
- `CheckParameterValue`: 91 inferred edges
- `EmpiricalGroup`: 90 inferred edges

## Cross-Module Suspicious Edges

- `core.py` ↔ `exceptions.py`: 380
- `multivariate.py` ↔ `distribution.py`: 268
- `multivariate.py` ↔ `transforms.py`: 201
- `continuous.py` ↔ `distribution.py`: 198
- `core.py` ↔ `blocking.py`: 152
- `tensor.py` ↔ `abstract.py`: 123
- `hmc` ↔ `state.py`: 118
- `metropolis.py` ↔ `arraystep.py`: 114
- `transforms.py` ↔ `distributions`: 104
- `distributions` ↔ `continuous.py`: 100
- `continuous.py` ↔ `dist_math.py`: 99
- `transforms.py` ↔ `abstract.py`: 94
- `opvi.py` ↔ `base.py`: 89
- `opvi.py` ↔ `ndarray.py`: 89
- `opvi.py` ↔ `blocking.py`: 89
- `opvi.py` ↔ `data.py`: 89
- `opvi.py` ↔ `simulator.py`: 89
- `opvi.py` ↔ `minibatch_rv.py`: 89
- `opvi.py` ↔ `approximations.py`: 86
- `mixture.py` ↔ `continuous.py`: 84
