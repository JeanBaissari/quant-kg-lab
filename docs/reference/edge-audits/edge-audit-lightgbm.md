# Edge Audit — lightgbm

**Date**: 2026-08-12

## Summary

- Total edges: 2029
- EXTRACTED: 1003 (49.4%)
- INFERRED: 1026 (50.6%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `pd_DataFrame`: 228 inferred edges
- `pd_Series`: 170 inferred edges
- `pd_CategoricalDtype`: 139 inferred edges
- `LightGBMError`: 99 inferred edges
- `Booster`: 95 inferred edges
- `Dataset`: 68 inferred edges
- `LGBMDeprecationWarning`: 54 inferred edges
- `LGBMModel`: 43 inferred edges
- `EvalResult`: 37 inferred edges
- `LGBMClassifier`: 36 inferred edges
- `LGBMRanker`: 36 inferred edges
- `LGBMRegressor`: 36 inferred edges
- `CVBooster`: 24 inferred edges
- `DaskLGBMClassifier`: 7 inferred edges
- `_DaskLGBMModel`: 7 inferred edges
- `DaskLGBMRanker`: 7 inferred edges
- `DaskLGBMRegressor`: 7 inferred edges
- `_DatasetNames`: 7 inferred edges
- `Choose a Dask client to use.      Parameters     ----------     client : distrib`: 7 inferred edges
- `:obj:`distributed.Client`: Dask client.          This property can be passed in`: 7 inferred edges

## Cross-Module Suspicious Edges

- `basic.py` ↔ `compat.py`: 417
- `sklearn.py` ↔ `basic.py`: 204
- `dask.py` ↔ `sklearn.py`: 124
- `dask.py` ↔ `compat.py`: 62
- `engine.py` ↔ `basic.py`: 56
- `sklearn.py` ↔ `compat.py`: 51
- `callback.py` ↔ `basic.py`: 40
- `dask.py` ↔ `basic.py`: 31
- `callback.py` ↔ `engine.py`: 20
- `plotting.py` ↔ `basic.py`: 7
- `plotting.py` ↔ `compat.py`: 7
- `plotting.py` ↔ `sklearn.py`: 7
