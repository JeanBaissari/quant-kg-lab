# Edge Audit — scipy

**Date**: 2026-07-29

## Summary

- Total edges: 51352
- EXTRACTED: 43581 (84.9%)
- INFERRED: 7771 (15.1%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `Benchmark`: 428 inferred edges
- `CensoredData`: 321 inferred edges
- `FitError`: 309 inferred edges
- `SmallSampleWarning`: 295 inferred edges
- `safe_import`: 284 inferred edges
- `Benchmark`: 282 inferred edges
- `LowLevelCallable`: 245 inferred edges
- `rv_continuous`: 242 inferred edges
- `MapWrapper`: 182 inferred edges
- `sparray`: 174 inferred edges
- `FitDataError`: 145 inferred edges
- `spmatrix`: 144 inferred edges
- `OptimizeResult`: 141 inferred edges
- `FunctionDoc`: 139 inferred edges
- `csr_array`: 128 inferred edges
- `BootstrapMethod`: 98 inferred edges
- `MonteCarloMethod`: 98 inferred edges
- `PermutationMethod`: 98 inferred edges
- `csc_array`: 95 inferred edges
- `LinearOperator`: 83 inferred edges

## Cross-Module Suspicious Edges

- `stats` ↔ `_lib`: 454
- `optimize` ↔ `_lib`: 149
- `interpolate` ↔ `benchmarks`: 121
- `sparse` ↔ `_lib`: 58
- `cluster` ↔ `_lib`: 47
- `integrate` ↔ `_lib`: 28
- `linalg` ↔ `sparse`: 20
- `benchmarks` ↔ `fft`: 11
- `conftest.py` ↔ `_lib`: 9
- `source` ↔ `stats`: 8
- `io` ↔ `_lib`: 3
- `source` ↔ `_lib`: 3
- `benchmarks` ↔ `sparse`: 2
- `fft` ↔ `_lib`: 2
- `__init__.py` ↔ `_lib`: 2
- `spatial` ↔ `_lib`: 2
- `sparse` ↔ `linalg`: 2
- `constants` ↔ `_lib`: 1
- `datasets` ↔ `_lib`: 1
- `differentiate` ↔ `_lib`: 1
