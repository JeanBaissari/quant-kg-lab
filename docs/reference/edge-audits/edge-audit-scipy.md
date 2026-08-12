# Edge Audit — scipy

**Date**: 2026-08-12

## Summary

- Total edges: 23466
- EXTRACTED: 18730 (79.8%)
- INFERRED: 4736 (20.2%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `CensoredData`: 328 inferred edges
- `FitError`: 316 inferred edges
- `rv_continuous`: 242 inferred edges
- `LowLevelCallable`: 239 inferred edges
- `sparray`: 175 inferred edges
- `FunctionDoc`: 147 inferred edges
- `MapWrapper`: 145 inferred edges
- `spmatrix`: 144 inferred edges
- `csr_array`: 129 inferred edges
- `OptimizeResult`: 123 inferred edges
- `BootstrapMethod`: 98 inferred edges
- `MonteCarloMethod`: 98 inferred edges
- `PermutationMethod`: 98 inferred edges
- `SmallSampleWarning`: 97 inferred edges
- `csc_array`: 96 inferred edges
- `coo_array`: 84 inferred edges
- `bsr_array`: 78 inferred edges
- `dia_array`: 78 inferred edges
- `csr_matrix`: 69 inferred edges
- `LinearOperator`: 68 inferred edges

## Cross-Module Suspicious Edges

- `_stats_py.py` ↔ `_resampling.py`: 288
- `_continuous_distns.py` ↔ `_ccallback.py`: 238
- `_continuous_distns.py` ↔ `_censored_data.py`: 238
- `_continuous_distns.py` ↔ `_distn_infrastructure.py`: 238
- `_continuous_distns.py` ↔ `_warnings_errors.py`: 238
- `_distribution_infrastructure.py` ↔ `_docscrape.py`: 130
- `_stats_py.py` ↔ `_axis_nan_policy.py`: 96
- `_discrete_distns.py` ↔ `_distn_infrastructure.py`: 94
- `_differentialevolution.py` ↔ `_constraints.py`: 84
- `_distn_infrastructure.py` ↔ `_docscrape.py`: 77
- `_distn_infrastructure.py` ↔ `_censored_data.py`: 77
- `_distn_infrastructure.py` ↔ `_warnings_errors.py`: 77
- `_compressed.py` ↔ `_base.py`: 60
- `_compressed.py` ↔ `_csr.py`: 60
- `_constraints.py` ↔ `_differentiable_functions.py`: 54
- `_minimize.py` ↔ `_constraints.py`: 52
- `_construct.py` ↔ `_bsr.py`: 52
- `_construct.py` ↔ `_coo.py`: 52
- `_construct.py` ↔ `_csc.py`: 52
- `_construct.py` ↔ `_csr.py`: 52
