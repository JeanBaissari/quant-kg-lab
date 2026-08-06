# Edge Audit — scikit-learn

**Date**: 2026-07-29

## Summary

- Total edges: 49978
- EXTRACTED: 23359 (46.7%)
- INFERRED: 26619 (53.3%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `Interval`: 2319 inferred edges
- `BaseEstimator`: 2292 inferred edges
- `StrOptions`: 2097 inferred edges
- `TransformerMixin`: 1166 inferred edges
- `ClassifierMixin`: 1068 inferred edges
- `NotFittedError`: 944 inferred edges
- `ConvergenceWarning`: 852 inferred edges
- `Parallel`: 841 inferred edges
- `RegressorMixin`: 798 inferred edges
- `HasMethods`: 643 inferred edges
- `ClassNamePrefixFeaturesOutMixin`: 498 inferred edges
- `Pipeline`: 496 inferred edges
- `Hidden`: 464 inferred edges
- `RealNotInt`: 438 inferred edges
- `MultiOutputMixin`: 314 inferred edges
- `MetaEstimatorMixin`: 312 inferred edges
- `DummyRegressor`: 278 inferred edges
- `DummyClassifier`: 260 inferred edges
- `Options`: 240 inferred edges
- `DataConversionWarning`: 230 inferred edges

## Cross-Module Suspicious Edges

- `utils` ↔ `base.py`: 1007
- `linear_model` ↔ `utils`: 908
- `ensemble` ↔ `utils`: 878
- `ensemble` ↔ `base.py`: 815
- `utils` ↔ `exceptions.py`: 669
- `metrics` ↔ `utils`: 609
- `ensemble` ↔ `_loss`: 599
- `model_selection` ↔ `utils`: 592
- `tests` ↔ `base.py`: 573
- `linear_model` ↔ `base.py`: 538
- `preprocessing` ↔ `base.py`: 477
- `decomposition` ↔ `base.py`: 450
- `preprocessing` ↔ `utils`: 413
- `cluster` ↔ `base.py`: 412
- `decomposition` ↔ `utils`: 405
- `base.py` ↔ `utils`: 364
- `cluster` ↔ `utils`: 348
- `linear_model` ↔ `exceptions.py`: 305
- `linear_model` ↔ `_loss`: 278
- `metrics` ↔ `exceptions.py`: 272
