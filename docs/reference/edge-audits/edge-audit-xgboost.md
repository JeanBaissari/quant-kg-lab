# Edge Audit — xgboost

**Date**: 2026-08-12

## Summary

- Total edges: 4318
- EXTRACTED: 2398 (55.5%)
- INFERRED: 1920 (44.5%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `Categories`: 172 inferred edges
- `Objective`: 141 inferred edges
- `DMatrix`: 128 inferred edges
- `TransformedDf`: 127 inferred edges
- `ArrowTransformed`: 99 inferred edges
- `PandasTransformed`: 99 inferred edges
- `Booster`: 98 inferred edges
- `XGBoostError`: 96 inferred edges
- `TreeObjective`: 96 inferred edges
- `TrainingCallback`: 64 inferred edges
- `HasArbitraryParamsDict`: 56 inferred edges
- `HasBaseMarginCol`: 56 inferred edges
- `HasContribPredictionCol`: 56 inferred edges
- `HasEnableSparseDataOptim`: 56 inferred edges
- `HasFeaturesCols`: 56 inferred edges
- `HasQueryIdCol`: 56 inferred edges
- `XGBoostTrainingSummary`: 56 inferred edges
- `CommunicatorContext`: 56 inferred edges
- `QuantileDMatrix`: 53 inferred edges
- `XGBClassifierBase`: 45 inferred edges

## Cross-Module Suspicious Edges

- `core.py` ↔ `params.py`: 336
- `core.py` ↔ `data.py`: 192
- `core.py` ↔ `_data_utils.py`: 192
- `core.py` ↔ `objective.py`: 192
- `sklearn.py` ↔ `compat.py`: 135
- `sklearn.py` ↔ `core.py`: 135
- `core.py` ↔ `_c_api.py`: 96
- `data.py` ↔ `_data_utils.py`: 93
- `training.py` ↔ `callback.py`: 68
- `core.py` ↔ `summary.py`: 56
- `core.py` ↔ `utils.py`: 56
- `callback.py` ↔ `core.py`: 46
- `sklearn.py` ↔ `callback.py`: 45
- `sklearn.py` ↔ `_data_utils.py`: 45
- `sklearn.py` ↔ `objective.py`: 45
- `training.py` ↔ `core.py`: 34
- `dask.py` ↔ `multi_target.py`: 32
- `multi_target.py` ↔ `updater.py`: 31
- `data.py` ↔ `core.py`: 29
- `updater.py` ↔ `data_iter.py`: 16
