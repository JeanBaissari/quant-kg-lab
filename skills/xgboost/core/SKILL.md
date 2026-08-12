---
name: xgboost-core
description: "Use when working with XGBoost native API \u2014 DMatrix, train(), Booster,\
  \ cv(), callbacks. Covers data loading, training loop, model persistence, and cross-validation."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: dmlc/xgboost
source_commit: 2a4786e61e08b41f63916089c35a10d0ac4626d2
extraction_date: 2026-07-29
graph:
  nodes: 1631
  edges: 4318
  community_count: 80
  graph_hash: fe8085677fab40cf
tags:
- xgboost
- gradient-boosting
- machine-learning
- core-api
related_skills:
- xgboost-sklearn
- lightgbm-core
---

# XGBoost Core API

Extracted from XGBoost knowledge graph. Sources: `python-package/xgboost/core.py`, `data.py`, `training.py`, `callback.py`.

## Quick Reference
### Data Structures

| API | Purpose | Key Methods | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node |
|-----|---------|-------------|
| `DMatrix` | Core data matrix for training/prediction | `set_info()`, `get_label()`, `save_binary()`, `slice()` | core.py:L666 |
| `QuantileDMatrix` | Memory-efficient DMatrix variant using quantilized data | Like DMatrix, plus `ExtMemQuantileDMatrix` for external memory | core.py:L1434 |
| `_ProxyDMatrix` | Lazy placeholder for deferred construction (device, external memory) | `ref_data_from_numpy()`, `ref_data_from_cudf()` | core.py:L1379 |
| `DataIter` | User-defined data iterator for distributed/custom data loading | `reset()`, `next()` — implement for each batch | core.py:L265 |

### Core Training

| API | Purpose | Signature | _c_api.py:L1 |
|-----|---------|-----------|
| `train()` | Train a booster with given params | `train(params, dtrain, num_boost_round, evals, obj, feval, ...)` | dask/__init__.py:L833 |
| `cv()` | Cross-validation | `cv(params, dtrain, nfold, num_boost_round, ...)` | training.py:L435 |
| `Booster` | The trained model object | `predict()`, `save_model()`, `load_model()`, `dump_model()`, `get_score()`, `trees_to_dataframe()` | core.py:L1750 |

### Callbacks

| Callback | Purpose | _c_api.py:L55 | _c_api.py:L55 |
|----------|---------|
| `TrainingCallback` | Base interface for custom callbacks (`before_training`, `after_training`, `before_iteration`, `after_iteration`) | callback.py:L51 | callback.py:L51 |
| `EarlyStopping` | Stop training when evaluation metric stops improving (`rounds`, `metric_name`, `minimize`) | callback.py:L311 | callback.py:L311 |
| `CallbackContainer` | Internal container that sequences multiple callbacks | callback.py:L149 | callback.py:L149 |
| `LearningRateScheduler` | Schedule learning rate by iteration | callback.py:L272 | callback.py:L272 |

### CV Utilities

| API | Purpose | _c_api.py:L1 | _c_api.py:L1 |
|-----|---------|
| `CVPack` | Holds one fold of CV — booster + dtrain/dtest | training.py:L212 | training.py:L212 |
| `_PackedBooster` | Lightweight pack of CV boosters | training.py:L239 | training.py:L239 |

## Common Patterns

### Basic Training
```python
import xgboost as xgb

# Create DMatrix from numpy/pandas
dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=feat_names)
dvalid = xgb.DMatrix(X_valid, label=y_valid)

# Set parameters
params = {
    'objective': 'reg:squarederror',
    'max_depth': 6,
    'learning_rate': 0.1,
    'n_estimators': 100,
    'eval_metric': 'rmse'
}

# Train with early stopping
model = xgb.train(
    params,
    dtrain,
    num_boost_round=1000,
    evals=[(dtrain, 'train'), (dvalid, 'valid')],
    early_stopping_rounds=50,
    callbacks=[xgb.callback.EarlyStopping(rounds=50)]
)

# Predict
preds = model.predict(xgb.DMatrix(X_test))
model.save_model('model.json')
```

### Custom Objective and Evaluation
```python
def custom_obj(preds, dtrain):
    labels = dtrain.get_label()
    grad = preds - labels
    hess = np.ones_like(labels)
    return grad, hess

def custom_metric(preds, dtrain):
    labels = dtrain.get_label()
    return 'my_metric', np.mean(np.abs(preds - labels))

model = xgb.train(params, dtrain, obj=custom_obj, feval=custom_metric)
```

### Cross-Validation
```python
cv_results = xgb.cv(
    params, dtrain,
    nfold=5,
    num_boost_round=1000,
    early_stopping_rounds=50,
    as_pandas=True
)
print(cv_results.tail())
```

### Using DataIter for Large Data
```python
class MyDataIter(xgb.DataIter):
    def __init__(self, data_source):
        super().__init__()
        self._it = iter(data_source)

    def next(self, input_data):
        batch = next(self._it)
        input_data(data=batch.data, label=batch.label)

    def reset(self):
        self._it = iter(data_source)

dtrain = xgb.DMatrix(MyDataIter(data_source))
```

### Model Persistence and Inspection
```python
# Save/Load
model.save_model('model.json')
loaded = xgb.Booster()
loaded.load_model('model.json')

# Dump/Save in text format
model.dump_model('dump.raw.txt')
trees_df = model.trees_to_dataframe()  # pandas DataFrame view

# Feature importance
importance = model.get_score(importance_type='gain')
```

## Pitfalls
1. **DMatrix cannot be pickled reliably**: Serialize via `save_binary()` / `load_binary()` or save the model, not the DMatrix.
2. **`train()` vs `fit()`**: The native `train()` expects `num_boost_round` and raw `DMatrix`; sklearn wrappers use `fit()` with numpy/pandas.
3. **GPU + DMatrix caching**: DMatrix caches data in GPU memory on first use. Free with `del dtrain` or call `gc.collect()` if OOM.
4. **Early stopping rounds**: `early_stopping_rounds` in `train()` is different from `EarlyStopping` callback — prefer the explicit callback for more control.
5. **`predict()` output type**: By default returns `numpy.ndarray`. For probability predictions with `objective='multi:softprob'`, set `output_margin=False`.
6. **Multi-GPU**: Set `device='cuda'` parameter, not `gpu_id`. For distributed, use `xgboost.collective` module.
7. **Feature names/weights**: `feature_names` and `feature_types` properties on DMatrix carry over to Booster — set early via `DMatrix(feature_names=...)`.

## Cross-Library Bridges

| Source | Target | Relation | Description |
|--------|--------|----------|-------------|
| `xgboost.DMatrix` | `sklearn.model_selection.GridSearchCV` | **data_source** | DMatrix feeds into sklearn CV (via `eval_set` wrapper) |
| `xgboost.Booster` | `optuna.Trial` | **optimization_target** | Booster params tuned via optuna `suggest_float/suggest_int` |
| `xgboost.train()` | `optuna.integration.XGBoostPruningCallback` | **callback_bridge** | Optuna pruning integrates as a training callback |
| `xgboost.cv()` | `lightgbm.cv()` | **sibling** | Similar CV API — both return history DataFrames with fold metrics |

### Optuna Integration
```python
import optuna

def objective(trial):
    params = {
        'max_depth': trial.suggest_int('max_depth', 3, 12),
        'learning_rate': trial.suggest_float('lr', 1e-3, 0.5, log=True),
        'objective': 'binary:logistic',
        'eval_metric': 'logloss',
    }
    pruning_cb = optuna.integration.XGBoostPruningCallback(trial, 'validation-logloss')
    model = xgb.train(params, dtrain, evals=[(dvalid, 'validation')],
                       callbacks=[pruning_cb])
    return model.best_score
```

### LightGBM Equivalents
| XGBoost | LightGBM |
|---------|----------|
| `xgb.DMatrix` | `lgb.Dataset` |
| `xgb.train()` | `lgb.train()` |
| `xgb.cv()` | `lgb.cv()` |
| `xgb.Booster` | `lgb.Booster` |
| `xgb.callback.EarlyStopping` | `lgb.early_stopping()` |

## Verification Checklist

- [ ] DMatrix created with correct `label` (and `weight`, `group` if needed)
- [ ] `params` dictionary keys match XGBoost parameter names exactly
- [ ] `num_boost_round` > `early_stopping_rounds` to ensure early stopping triggers
- [ ] Evaluation metric name matches one from `evals` list in callbacks
- [ ] Model saved in JSON format (not deprecated binary) for cross-version compatibility
- [ ] `predict()` output shape matches expectation (n_samples, n_classes) for multi-class
- [ ] Feature names preserved through DMatrix → Booster → predict

## References

- Source: `python-package/xgboost/core.py` (Booster, DMatrix, DataIter)
- Source: `python-package/xgboost/training.py` (train, cv, CVPack)
- Source: `python-package/xgboost/callback.py` (TrainingCallback, EarlyStopping, LearningRateScheduler)
- Source: `python-package/xgboost/data.py` (data dispatch, pandas/polars/cupy support)

## Provenance

- Knowledge graph: xgboost, 1631 nodes, 4318 edges, 80 communities
- God nodes: `Categories` (179), `DMatrix` (161), `Objective` (146) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 2a4786e61e08, backend opencode, description coverage 84%
