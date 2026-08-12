# Edge Audit — scikit-learn

**Date**: 2026-08-12

## Summary

- Total edges: 28094
- EXTRACTED: 11176 (39.8%)
- INFERRED: 16918 (60.2%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `Interval`: 2222 inferred edges
- `StrOptions`: 2003 inferred edges
- `BaseEstimator`: 1514 inferred edges
- `TransformerMixin`: 878 inferred edges
- `RegressorMixin`: 736 inferred edges
- `Parallel`: 729 inferred edges
- `ClassifierMixin`: 660 inferred edges
- `HasMethods`: 601 inferred edges
- `ConvergenceWarning`: 506 inferred edges
- `ClassNamePrefixFeaturesOutMixin`: 498 inferred edges
- `Hidden`: 422 inferred edges
- `RealNotInt`: 396 inferred edges
- `NotFittedError`: 393 inferred edges
- `MultiOutputMixin`: 314 inferred edges
- `MetaEstimatorMixin`: 269 inferred edges
- `DataConversionWarning`: 207 inferred edges
- `OneToOneFeatureMixin`: 206 inferred edges
- `Options`: 198 inferred edges
- `ClusterMixin`: 181 inferred edges
- `OutlierMixin`: 135 inferred edges

## Cross-Module Suspicious Edges

- `estimator_checks.py` ↔ `base.py`: 540
- `loss.py` ↔ `link.py`: 360
- `_base.py` ↔ `base.py`: 343
- `_gb.py` ↔ `loss.py`: 287
- `_data.py` ↔ `base.py`: 284
- `base.py` ↔ `_tags.py`: 260
- `_base.py` ↔ `_param_validation.py`: 260
- `_hist_gradient_boosting` ↔ `loss.py`: 252
- `estimator_checks.py` ↔ `_tags.py`: 225
- `_data.py` ↔ `_param_validation.py`: 213
- `pairwise.py` ↔ `_param_validation.py`: 190
- `text.py` ↔ `_param_validation.py`: 188
- `_forest.py` ↔ `base.py`: 180
- `estimator_checks.py` ↔ `exceptions.py`: 180
- `_classes.py` ↔ `base.py`: 179
- `_gb.py` ↔ `_param_validation.py`: 164
- `_split.py` ↔ `_param_validation.py`: 160
- `_ridge.py` ↔ `base.py`: 159
- `_classes.py` ↔ `_param_validation.py`: 158
- `_hist_gradient_boosting` ↔ `base.py`: 142
