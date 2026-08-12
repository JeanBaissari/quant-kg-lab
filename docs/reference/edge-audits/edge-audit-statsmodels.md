# Edge Audit — statsmodels

**Date**: 2026-08-12

## Summary

- Total edges: 33529
- EXTRACTED: 14325 (42.7%)
- INFERRED: 19204 (57.3%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `Appender`: 1089 inferred edges
- `FormulaManager`: 899 inferred edges
- `OLS`: 843 inferred edges
- `ValueWarning`: 835 inferred edges
- `SpecificationWarning`: 687 inferred edges
- `SimpleTable`: 657 inferred edges
- `ConvergenceWarning`: 655 inferred edges
- `Docstring`: 441 inferred edges
- `Substitution`: 421 inferred edges
- `PandasData`: 342 inferred edges
- `GLM`: 338 inferred edges
- `LikelihoodModel`: 318 inferred edges
- `SingularMatrixWarning`: 305 inferred edges
- `EstimationWarning`: 292 inferred edges
- `MLEInfluence`: 261 inferred edges
- `LinearConstraints`: 258 inferred edges
- `DiscreteMargins`: 257 inferred edges
- `PerfectSeparationWarning`: 257 inferred edges
- `PerfectSeparationError`: 232 inferred edges
- `Model`: 221 inferred edges

## Cross-Module Suspicious Edges

- `discrete_model.py` ↔ `sm_exceptions.py`: 570
- `statespace` ↔ `sm_exceptions.py`: 513
- `generalized_estimating_equations.py` ↔ `sm_exceptions.py`: 483
- `discrete_model.py` ↔ `diagnostic.py`: 380
- `discrete_model.py` ↔ `docstring_helpers.py`: 380
- `linear_model.py` ↔ `sm_exceptions.py`: 360
- `stattools` ↔ `sm_exceptions.py`: 355
- `generalized_linear_model.py` ↔ `sm_exceptions.py`: 335
- `count_model.py` ↔ `discrete_model.py`: 306
- `ar_model.py` ↔ `deterministic.py`: 304
- `model.py` ↔ `sm_exceptions.py`: 300
- `regression` ↔ `linear_model.py`: 294
- `truncated_model.py` ↔ `discrete_model.py`: 273
- `regression` ↔ `model.py`: 258
- `linear_model.py` ↔ `elastic_net.py`: 240
- `model.py` ↔ `contrast.py`: 200
- `ardl` ↔ `ar_model.py`: 196
- `discrete_model.py` ↔ `_constraints.py`: 190
- `discrete_model.py` ↔ `model.py`: 190
- `discrete_model.py` ↔ `discrete_margins.py`: 190
