---
name: lightgbm-sklearn
description: "Use when working with LightGBM scikit-learn wrappers \u2014 LGBMClassifier,\
  \ LGBMRegressor, LGBMRanker. Covers sklearn-compatible fit/predict, parameter aliases,\
  \ categorical handling, and Pipeline/GridSearchCV integration."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: microsoft/LightGBM
source_commit: f9bf8d1358cd7b5d649b47175e56543b62856f98
extraction_date: 2026-07-29
graph:
  nodes: 593
  edges: 2029
  community_count: 17
  graph_hash: a8013a25fbe34b59
tags:
- lightgbm
- gradient-boosting
- machine-learning
- scikit-learn
- sklearn
related_skills:
- lightgbm-core
- scikit-learn-model-selection
- optuna-samplers
---

# LightGBM Scikit-learn API

Extracted from LightGBM knowledge graph. Source: `python-package/lightgbm/sklearn.py`.

## Quick Reference
### Estimators

| Class | Purpose | Special Methods | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node |
|-------|---------|----------------|
| `LGBMModel` | Base class for all sklearn wrappers | `booster_`, `feature_importances_`, `evals_result_`, `n_features_in_`, `n_estimators_`, `n_iter_` | sklearn.py:L575 |
| `LGBMClassifier` | Classification (binary + multi-class) | `predict_proba()`, `decision_function()`, `classes_`, `n_classes_` | : |
| `LGBMRegressor` | Regression | `predict()` | : |
| `LGBMRanker` | Learning-to-rank | `predict()` — requires `group` parameter | : |

### Key Attributes (on fitted model)

| Attribute | Description |
|-----------|-------------|
| `booster_` | Underlying `lgb.Booster` object |
| `feature_importances_` | Feature importance array (default: `'split'`) |
| `feature_name_` | List of feature names (internal) |
| `feature_names_in_` | Feature names (sklearn-compatible, when X has columns) |
| `evals_result_` | Dict of evaluation metrics per iteration |
| `best_score_` | Dict of best scores from early stopping |
| `best_iteration_` | Best iteration (0-based) |
| `objective_` | Concrete objective string/callable used during fit |
| `n_estimators_` | True number of boosting iterations performed |
| `n_iter_` | Same as `n_estimators_` (scikit-learn convention) |
| `n_features_in_` | Number of features seen during fit |
| `classes_` | Class labels (classifier only, shape: [n_classes]) |
| `n_classes_` | Number of classes (classifier only) |

### Common Parameters

| Parameter | Type | Default | Description | basic.py:L4167 |
|-----------|------|---------|-------------|
| `n_estimators` | int | 100 | Number of boosting rounds |
| `num_leaves` | int | 31 | Maximum tree leaves (leaf-wise growth) |
| `max_depth` | int | -1 | Max tree depth; -1 = no limit |
| `learning_rate` | float | 0.1 | Step size shrinkage |
| `objective` | str | 'regression' | Objective: 'regression', 'binary', 'multiclass', 'lambdarank' | sklearn.py:L1336 |
| `boosting_type` | str | 'gbdt' | 'gbdt', 'dart', 'goss', 'rf' |
| `metric` | str/list | '' | Metric: 'rmse', 'binary_logloss', 'auc', 'ndcg', etc. | plotting.py:L294 |
| `num_iterations` | int | 100 | Alias for `n_estimators` (both work) |
| `early_stopping_rounds` | int | 0 | Rounds without improvement; 0 = disabled |
| `importance_type` | str | 'split' | 'split' (default) or 'gain' |
| `device_type` | str | 'cpu' | 'cpu', 'cuda', 'gpu' |
| `n_jobs` | int | -1 | Number of parallel threads; -1 = all cores |
| `verbosity` | int | 1 | -1 (silent), 0 (warnings only), 1 (info), >1 (debug) |
| `feature_fraction` | float | 1.0 | Column subsampling ratio (alias: `colsample_bytree`) |
| `bagging_fraction` | float | 1.0 | Row subsampling ratio (alias: `subsample`) |
| `bagging_freq` | int | 0 | Frequency for bagging; 0 = disabled |
| `reg_alpha` | float | 0.0 | L1 regularization |
| `reg_lambda` | float | 0.0 | L2 regularization |
| `min_child_samples` | int | 20 | Minimum data in leaf (alias: `min_data_in_leaf`) |
| `categorical_feature` | list | 'auto' | Categorical feature indices/names; 'auto' = infer |
| `class_weight` | dict/str | None | Class weights for classifier; 'balanced' auto-computes |

### Parameter Aliases

| Primary | Alias |
|---------|-------|
| `n_estimators` | `num_iterations`, `n_estimators`, `num_round`, `num_trees` |
| `learning_rate` | `eta`, `shrinkage_rate` |
| `num_leaves` | `num_leaf` |
| `feature_fraction` | `colsample_bytree` |
| `bagging_fraction` | `subsample`, `sub_row` |
| `bagging_freq` | `subsample_freq` |
| `min_child_samples` | `min_data_in_leaf` |
| `reg_alpha` | `lambda_l1` |
| `reg_lambda` | `lambda_l2` |
| `device_type` | `device`, `boosting` |

## Common Patterns

### LGBMClassifier
```python
from lightgbm import LGBMClassifier

model = LGBMClassifier(
    n_estimators=100,
    num_leaves=31,
    learning_rate=0.1,
    objective='binary',
    metric='binary_logloss',
    boosting_type='gbdt',
    random_state=42
)
model.fit(
    X_train, y_train,
    eval_set=[(X_valid, y_valid)],
    eval_metric='logloss',
    callbacks=[lgb.early_stopping(10), lgb.log_evaluation(100)]
)
probs = model.predict_proba(X_test)
preds = model.predict(X_test)
```

### LGBMRegressor
```python
from lightgbm import LGBMRegressor

model = LGBMRegressor(
    n_estimators=200,
    num_leaves=63,
    learning_rate=0.05,
    objective='regression',
    metric='rmse',
    feature_fraction=0.8,
    bagging_fraction=0.8,
    bagging_freq=5,
    verbosity=-1
)
model.fit(X_train, y_train, eval_set=[(X_valid, y_valid)])
preds = model.predict(X_test)
importance = model.feature_importances_
```

### LGBMRanker
```python
from lightgbm import LGBMRanker

# group = array of query sizes: [q1_rows, q2_rows, ...]
model = LGBMRanker(
    n_estimators=100,
    objective='lambdarank',
    metric='ndcg',
    num_leaves=255,
    learning_rate=0.1,
    boosting_type='gbdt',
    label_gain=[0, 1, 3, 5]  # relevance gains
)
model.fit(
    X_train, y_train,
    group=train_groups,
    eval_set=[(X_valid, y_valid)],
    eval_group=[valid_groups],
    eval_at=[1, 3, 5, 10],
    callbacks=[lgb.early_stopping(20)]
)
```

### Scikit-learn Pipeline
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from lightgbm import LGBMClassifier

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('lgb', LGBMClassifier(n_estimators=100, verbosity=-1))
])
pipeline.fit(X_train, y_train)
preds = pipeline.predict(X_test)
```

### GridSearchCV with Aliases
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'num_leaves': [15, 31, 63],
    'learning_rate': [0.01, 0.05, 0.1],
    'feature_fraction': [0.6, 0.8, 1.0],  # or 'colsample_bytree'
    'bagging_fraction': [0.6, 0.8, 1.0],   # or 'subsample'
    'bagging_freq': [0, 5],
    'reg_alpha': [0, 0.1, 1.0],
    'reg_lambda': [0, 0.1, 1.0],
}
grid = GridSearchCV(
    LGBMClassifier(n_estimators=200, verbosity=-1),
    param_grid, cv=5, scoring='accuracy', n_jobs=-1
)
grid.fit(X_train, y_train)
```

### Incremental Training (Continue from Previous)
```python
model = LGBMClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Continue training — pass booster directly
model.fit(X_train2, y_train2, init_model=model.booster_)

# Or set new n_estimators
model.n_estimators = 150
model.fit(X_train2, y_train2, init_model=model.booster_)
```

### Categorical Features
```python
# Option A: Auto-detect (pandas category columns)
model = LGBMClassifier(categorical_feature='auto')
model.fit(X_train, y_train)  # X_train has pd.Categorical columns

# Option B: Explicit indices/names
model = LGBMClassifier(categorical_feature=[0, 3, 5])
model.fit(X_train, y_train)

# Option C: Pass during fit
model.fit(X_train, y_train, categorical_feature=['color', 'brand'])
```

## Pitfalls

1. **`eval_set` deprecation**: `eval_set` keyword in `fit()` is deprecated. Use separate `eval_X`, `eval_y`, `eval_group` arguments. Both still work but `eval_set` emits deprecation warning.
2. **`n_estimators` vs `num_iterations`**: Both work — LightGBM accepts many aliases. But when using `GridSearchCV`, use `n_estimators` which is the sklearn canonical name.
3. **`num_leaves` > 2^max_depth**: If both are set, LightGBM uses leaf-wise growth limited by `num_leaves`. Setting `max_depth` only restricts tree depth as a secondary constraint.
4. **`fit()` called multiple times**: Calling `fit()` again retrains from scratch unless `init_model` is passed. Pass `init_model=model.booster_` for warm-start/continue.
5. **`categorical_feature='auto'`**: Only works with pandas DataFrames where columns are `pd.Categorical` dtype. For numpy arrays, specify indices explicitly.
6. **`feature_names_in_` deletion**: Scikit-learn can delete `feature_names_in_` in some code paths (check_is_fitted). LightGBM intercepts this — use `feature_name_` as the internal equivalent.
7. **LGBMRanker `group`**: Ranking requires `group` parameter (array of query sizes). Without it, metrics are meaningless.
8. **`importance_type` default**: Default is `'split'` (number of times a feature is used), not `'gain'` like XGBoost. Use `importance_type='gain'` for feature contribution-based importance.
9. **Subclassing**: When subclassing LGBM estimators, all init args must be repeated in the subclass `__init__`. LightGBM introspects constructor parameters — missing args break `get_params()`.

## Cross-Library Bridges

| Source | Target | Relation | Description |
|--------|--------|----------|-------------|
| `_LGBMClassifierBase` | `GridSearchCV` | **compatible** | LightGBM sklearn wrappers compatible with sklearn CV |
| `LGBMClassifier` | `sklearn.pipeline.Pipeline` | **compatible** | Fully compatible with sklearn Pipeline |
| `LGBMRegressor` | `sklearn.model_selection.RandomizedSearchCV` | **compatible** | Works with sklearn parameter search |
| `LGBMModel.get_params()` | `optuna.Trial` | **optimization_target** | Hyperparameters tuned via optuna |
| `lgb.LGBMClassifier` | `sklearn.calibration.CalibratedClassifierCV` | **compatible** | Supports probability calibration |

### Optuna Hyperparameter Optimization
```python
import optuna
from lightgbm import LGBMClassifier
from sklearn.model_selection import cross_val_score

def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 500),
        'num_leaves': trial.suggest_int('num_leaves', 15, 255),
        'learning_rate': trial.suggest_float('lr', 1e-3, 0.5, log=True),
        'feature_fraction': trial.suggest_float('feature_fraction', 0.5, 1.0),
        'bagging_fraction': trial.suggest_float('bagging_fraction', 0.5, 1.0),
        'bagging_freq': trial.suggest_int('bagging_freq', 1, 10),
        'reg_alpha': trial.suggest_float('reg_alpha', 1e-8, 10.0, log=True),
        'reg_lambda': trial.suggest_float('reg_lambda', 1e-8, 10.0, log=True),
        'min_child_samples': trial.suggest_int('min_child_samples', 5, 100),
        'verbosity': -1,
        'random_state': 42,
    }
    model = LGBMClassifier(**params)
    return cross_val_score(model, X, y, cv=5, scoring='accuracy').mean()

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)
```

### XGBoost Sklearn Equivalents
| LightGBM | XGBoost |
|----------|---------|
| `LGBMClassifier` | `XGBClassifier` |
| `LGBMRegressor` | `XGBRegressor` |
| `LGBMRanker` | `XGBRanker` |
| `n_estimators` / `num_iterations` | `n_estimators` |
| `num_leaves` | `max_depth` (XGBoost is depth-wise) |
| `importance_type='split'` | `importance_type='gain'` (different defaults!) |

## Verification Checklist

- [ ] `objective` matches task: regression, binary, multiclass, lambdarank
- [ ] Validation data provided via `eval_set` or `eval_X`/`eval_y` for early stopping
- [ ] `early_stopping_round` > 0 to actually trigger early stopping
- [ ] For ranking: `group` passed to fit, `eval_group` for validation
- [ ] Categorical features handled natively (not one-hot encoded externally)
- [ ] `num_leaves` tuned — default 31 may be too high for small datasets
- [ ] `bagging_freq > 0` when `bagging_fraction < 1.0`
- [ ] `random_state` set for reproducibility
- [ ] `verbosity=-1` to silence warnings in production/grid search
- [ ] Model saved via joblib (for Pipeline) or `.booster_.save_model()` (for booster only)

## References

- Source: `python-package/lightgbm/sklearn.py` (LGBMModel, LGBMClassifier, LGBMRegressor, LGBMRanker, wrappers)
- Graph communities: 1, 3, 56, 72, 77, 87, 100, 101, 107, 123, 132

## Provenance

- Knowledge graph: lightgbm, 593 nodes, 2029 edges, 17 communities
- God nodes: `LGBMModel` (72), `LGBMClassifier` (49), `LGBMRegressor` (43) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ f9bf8d1358cd, backend opencode, description coverage 84%
