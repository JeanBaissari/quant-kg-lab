---
name: lightgbm-core
description: Use when working with LightGBM native API — Dataset, train(), Booster, cv(), callbacks. Covers data loading, training, model persistence, and cross-validation.
version: 0.1.0
author: quant-kg-lab
license: MIT
source_repo: microsoft/LightGBM
source_version: main
extraction_date: 2026-07-29
graph_hash: 2952_nodes_5138_edges
graph_stats:
  nodes: 2952
  edges: 5138
  communities: [0, 3, 4, 5, 6, 8, 13, 20, 33, 34, 38, 98, 99, 106, 114, 115, 116, 133, 134, 146]
metadata:
  hermes:
    tags: [lightgbm, gradient-boosting, machine-learning, core-api]
    related_skills: [lightgbm-sklearn, xgboost-core]
---

# LightGBM Core API

Extracted from LightGBM knowledge graph. Sources: `python-package/lightgbm/basic.py`, `engine.py`, `callback.py`.

## Quick Reference

### Data Structures

| API | Purpose | Key Methods |
|-----|---------|-------------|
| `Dataset` | Core data container; LightGBM discretizes data into histograms from this | `construct()`, `set_field()`, `get_field()`, `save_binary()`, `subset()`, `create_valid()` |
| `Booster` | The trained model object | `predict()`, `save_model()`, `dump_model()`, `feature_importance()`, `trees_to_dataframe()`, `refit()` |
| `CVBooster` | Holds all CV fold boosters | Load/save as JSON, redirect method calls to underlying boosters |
| `Sequence` | Data access interface for custom loading | Implement `__getitem__(idx)` returning data for given row index |
| `_InnerPredictor` | Internal fast predictor (not exposed) | Used for sklearn wrapper prediction |

### Core Training

| API | Purpose | Signature |
|-----|---------|-----------|
| `train()` | Perform the training with given parameters | `train(params, train_set, num_boost_round, valid_sets, feval, callbacks, ...)` |
| `cv()` | Cross-validation | `cv(params, train_set, num_boost_round, nfold, stratified, feval, callbacks, ...)` |

### Callbacks

| Callback | Purpose |
|----------|---------|
| `log_evaluation()` | Log evaluation results at specified period |
| `record_evaluation()` | Record evaluation history into `evals_result` dict |
| `early_stopping()` | Stop training when metric stops improving |
| `reset_parameter()` | Reset a parameter after first iteration |

### Field Operations (Dataset)

| Method | Purpose |
|--------|---------|
| `set_field(field_name, data)` | Set label, weight, group, init_score, position |
| `get_field(field_name)` | Get field data |
| `set_categorical_feature(features)` | Mark categorical feature indices |
| `set_feature_name(feature_names)` | Assign feature names |
| `set_reference(reference)` | Set reference Dataset for aligned binning |

## Common Patterns

### Basic Training
```python
import lightgbm as lgb

# Create Dataset (automatically handles binning)
train_data = lgb.Dataset(X_train, label=y_train, feature_name=feat_names,
                         categorical_feature=cat_cols)
valid_data = lgb.Dataset(X_valid, label=y_valid, reference=train_data)

# Set parameters
params = {
    'objective': 'regression',
    'metric': 'rmse',
    'boosting_type': 'gbdt',
    'num_leaves': 31,
    'learning_rate': 0.1,
    'feature_fraction': 0.8,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0
}

# Train with early stopping
model = lgb.train(
    params,
    train_data,
    num_boost_round=1000,
    valid_sets=[train_data, valid_data],
    valid_names=['train', 'valid'],
    callbacks=[lgb.early_stopping(stopping_rounds=50),
               lgb.log_evaluation(period=100)]
)

# Predict
preds = model.predict(X_test)
model.save_model('model.txt')
```

### Custom Objective and Evaluation
```python
def custom_obj(preds, train_data):
    labels = train_data.get_label()
    grad = 2 * (preds - labels)
    hess = 2 * np.ones_like(labels)
    return grad, hess

def custom_metric(preds, train_data):
    labels = train_data.get_label()
    return 'my_metric', np.mean(np.abs(preds - labels)), False

model = lgb.train(params, train_data, fobj=custom_obj, feval=custom_metric)
```

### Cross-Validation
```python
cv_results = lgb.cv(
    params,
    train_data,
    num_boost_round=1000,
    nfold=5,
    stratified=False,
    callbacks=[lgb.early_stopping(50), lgb.log_evaluation(100)]
)
# cv_results dict: 'train rmse-mean', 'valid rmse-stdv', etc.
print(cv_results)
```

### Dataset Management
```python
# Create from file
ds = lgb.Dataset('data.bin')

# Save to binary
ds.save_binary('data.bin')

# Subset
subset = ds.subset(used_indices=[0, 1, 5, 10])

# Create validation with same binning
valid = ds.create_valid(X_valid)

# Add features from another dataset
ds.add_features_from(other_dataset)

# Get properties
nrow = ds.num_data()
ncol = ds.num_feature()
feature_names = ds.feature_name
label = ds.get_label()
weight = ds.get_weight()
group = ds.get_group()
```

### Model Persistence and Inspection
```python
# Save/Load
model.save_model('model.txt')
loaded = lgb.Booster(model_file='model.txt')

# Save/Load from string
model_str = model.model_to_string()
loaded2 = lgb.Booster(model_str=model_str)

# Model inspection
importance = model.feature_importance(importance_type='gain')
trees_df = model.trees_to_dataframe()
json_str = model.dump_model()  # Full model as JSON

# Number of trees
n_trees = model.num_trees()

# Slice model (keep first N iterations)
sliced = model.model_from_string(
    model.model_to_string(num_iteration=50)
)
```

## Common Pitfalls

1. **`reference` Dataset for validation**: When creating validation Dataset, always set `reference=train_data` to ensure consistent binning. Without it, validation data gets its own bin boundaries and results are inconsistent.
2. **Categorical features**: Specify via `categorical_feature` in `Dataset()` or `params['categorical_feature']`. LightGBM handles categoricals natively — do NOT one-hot encode.
3. **`num_leaves` vs `max_depth`**: LightGBM uses leaf-wise (best-first) tree growth controlled by `num_leaves`, not depth-wise like XGBoost. Use `num_leaves < 2^max_depth` to avoid overfitting.
4. **`save_binary`**: Saved binary format contains pre-binned data — it loads faster than raw data but takes more disk space and is tied to parameter settings.
5. **`Dataset` re-creation**: Calling `Dataset()` re-bins the data. For incremental training, reuse the original Dataset with `init_model` parameter.
6. **Validation without `reference`**: If you create a validation Dataset without `reference=train_data`, the histogram bin boundaries will differ, and validation metrics will be meaningless.
7. **`Bagging` parameter dependencies**: `bagging_fraction` requires `bagging_freq > 0` to take effect. Without `bagging_freq`, no bagging is performed.
8. **`predict` data format**: `predict()` accepts raw arrays (numpy/pandas), Dataset, or file path. The method automatically creates a temporary Dataset if needed.

## Cross-Library Bridges

| Source | Target | Relation | Description |
|--------|--------|----------|-------------|
| `lgb.Dataset` | `sklearn.model_selection.GridSearchCV` | **data_source** | Dataset feeds into sklearn CV workflows |
| `lgb.Booster` | `optuna.Trial` | **optimization_target** | Booster params tuned via optuna |
| `lgb.train()` | `optuna.integration.LightGBMPruningCallback` | **callback_bridge** | Optuna pruning integrates as a training callback |
| `lgb.cv()` | `xgboost.cv()` | **sibling** | Nearly identical CV API with compatible output format |

### Optuna Integration
```python
import optuna.integration.lightgbm as optuna_lgb

# Simplified API (auto-handles pruning + optimization)
params = {
    'objective': 'binary',
    'metric': 'binary_logloss',
    'boosting_type': 'gbdt',
}
train_set = lgb.Dataset(X_train, label=y_train)
valid_set = lgb.Dataset(X_valid, label=y_valid, reference=train_set)

model = optuna_lgb.train(
    params, train_set,
    valid_sets=[valid_set],
    verbose_eval=False,
    num_boost_round=1000,
    early_stopping_rounds=50
)
# Access best params: model.params
```

### XGBoost Equivalents
| LightGBM | XGBoost |
|----------|---------|
| `lgb.Dataset` | `xgb.DMatrix` |
| `lgb.train()` | `xgb.train()` |
| `lgb.cv()` | `xgb.cv()` |
| `lgb.Booster` | `xgb.Booster` |
| `lgb.early_stopping()` | `xgb.callback.EarlyStopping` |
| `num_leaves` ~ 2^max_depth | `max_depth` |

## Verification Checklist

- [ ] Validation Dataset has `reference=train_data` for consistent binning
- [ ] Categorical features specified via `categorical_feature` (not one-hot encoded)
- [ ] `num_leaves` is appropriate: too high → overfitting, too low → underfitting
- [ ] `bagging_freq > 0` if `bagging_fraction < 1.0`
- [ ] `eval_metric` / `metric` is set for early stopping to function
- [ ] Model saved as `.txt` (human-readable) or via `model_to_string()` for cross-version compat
- [ ] `predict()` output format correct for objective (raw score vs probability)
- [ ] `Dataset.construct()` not called manually — done automatically during `train()`

## References

- Source: `python-package/lightgbm/basic.py` (Dataset, Booster, Sequence, _InnerPredictor)
- Source: `python-package/lightgbm/engine.py` (train, cv, CVBooster)
- Source: `python-package/lightgbm/callback.py` (early_stopping, log_evaluation, record_evaluation, reset_parameter)
