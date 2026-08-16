---
name: xgboost-sklearn
description: "Use when working with XGBoost scikit-learn wrappers \u2014 XGBClassifier,\
  \ XGBRegressor, XGBRanker. Covers sklearn-compatible fit/predict, parameter interface,\
  \ and Pipeline/GridSearchCV integration."
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
  graph_hash: 47615a42dd12a0a8
tags:
- xgboost
- gradient-boosting
- machine-learning
- scikit-learn
- sklearn
related_skills:
- xgboost-core
- scikit-learn-model-selection
- optuna-samplers
---

# XGBoost Scikit-learn API

Extracted from XGBoost knowledge graph. Source: `python-package/xgboost/sklearn.py`.

## Quick Reference
### Estimators

| Class | Purpose | Graph Node | Special Methods |
|-------|---------|-----------|----------------|
| `XGBModel` | Base class for all sklearn wrappers | sklearn.py:L866 | `get_booster()`, `get_xgb_params()`, `evals_result()`, `feature_importances_`, `save_model()`, `load_model()` |
| `XGBClassifier` | Classification (binary + multi-class) | sklearn.py:L1758 | `predict_proba()`, `classes_` |
| `XGBRegressor` | Regression | sklearn.py:L2051 | `predict()`, `coef_`, `intercept_` (for gblinear) |
| `XGBRanker` | Learning-to-rank | sklearn.py:L2194 | `predict()`, `score()` — requires `qid` in input |
| `XGBRFClassifier` | Random forest classifier (deprecated) | sklearn.py:L1995 | Inherits from XGBClassifier — use `num_parallel_tree` instead |
| `XGBRFRegressor` | Random forest regressor (deprecated) | sklearn.py:L2075 | Inherits from XGBRegressor — use `num_parallel_tree` instead |

### Key Attributes (on fitted model)

| Attribute | Description | Graph Node |
|-----------|-------------|-----------|
| `booster_` | Underlying `xgb.Booster` object | sklearn.py:L866 |
| `feature_importances_` | Feature importance array (depends on `importance_type`) | sklearn.py:L866 |
| `evals_result_` | Dict of evaluation metrics per iteration | sklearn.py:L866 |
| `best_score_` | Best score from early stopping | sklearn.py:L866 |
| `best_iteration_` | 0-based best iteration | sklearn.py:L866 |
| `n_features_in_` | Number of features seen during fit | sklearn.py:L866 |
| `feature_names_in_` | Feature names (when X has column names) | sklearn.py:L866 |
| `classes_` | Class labels (classifier only) | sklearn.py:L1758 |
| `coef_` / `intercept_` | Coefficients (linear models only) | sklearn.py:L2051 |

### Common Parameters

| Parameter | Type | Default | Description | Source |
|-----------|------|---------|-------------|--------|
| `n_estimators` | int | 100 | Number of boosting rounds | `sklearn.py:L866` |
| `max_depth` | int | 6 | Maximum tree depth | `sklearn.py:L866` |
| `learning_rate` | float | 0.3 | Step size shrinkage (eta) | `sklearn.py:L866` |
| `objective` | str | 'reg:squarederror' | Learning objective | `sklearn.py:L866` |
| `booster` | str | 'gbtree' | Booster type: 'gbtree', 'gblinear', 'dart' | `core.py:L1750` |
| `eval_metric` | str/list | None | Metric(s) for evaluation | `sklearn.py:L866` |
| `early_stopping_rounds` | int | None | Rounds without improvement before stopping | `sklearn.py:L866` |
| `importance_type` | str | 'gain' | Feature importance metric: 'gain', 'weight', 'cover', 'total_gain', 'total_cover' | `sklearn.py:L866` |
| `device` | str | 'cpu' | 'cpu', 'cuda', 'gpu' | `sklearn.py:L866` |
| `enable_categorical` | bool | False | Enable categorical feature support | `sklearn.py:L866` |
| `max_cat_to_onehot` | int | 4 | Max categories for one-hot encoding | `sklearn.py:L866` |
| `verbosity` | int | 1 | 0 (silent), 1 (warning), 2 (info), 3 (debug) | `sklearn.py:L866` |

## Common Patterns

### XGBClassifier (Binary)
```python
from xgboost import XGBClassifier

model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    objective='binary:logistic',
    eval_metric='logloss',
    early_stopping_rounds=10,
    random_state=42
)
model.fit(
    X_train, y_train,
    eval_set=[(X_valid, y_valid)],
    verbose=True
)
probs = model.predict_proba(X_test)
preds = model.predict(X_test)
```

### XGBClassifier (Multi-class)
```python
model = XGBClassifier(
    n_estimators=100,
    objective='multi:softprob',  # Returns probabilities
    num_class=3,
    eval_metric='mlogloss'
)
model.fit(X_train, y_train, eval_set=[(X_valid, y_valid)])
probs = model.predict_proba(X_test)  # shape: (n_samples, n_classes)
```

### XGBRegressor
```python
from xgboost import XGBRegressor

model = XGBRegressor(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    objective='reg:squarederror',
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
model.fit(X_train, y_train, eval_set=[(X_valid, y_valid)])
preds = model.predict(X_test)
importance = model.feature_importances_
```

### XGBRanker
```python
from xgboost import XGBRanker

# qid identifies which queries rows belong to
model = XGBRanker(
    n_estimators=100,
    objective='rank:ndcg',
    eval_metric='ndcg@5-10',
    early_stopping_rounds=20
)
model.fit(X_train, y_train, qid=train_qids,
          eval_set=[(X_valid, y_valid)],
          eval_qid=[valid_qids])
```

### Scikit-learn Pipeline Integration
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('xgb', XGBClassifier(n_estimators=100))
])
pipeline.fit(X_train, y_train)
preds = pipeline.predict(X_test)
```

### GridSearchCV Integration
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.3],
    'subsample': [0.6, 0.8, 1.0]
}
grid = GridSearchCV(
    XGBClassifier(n_estimators=100),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid.fit(X_train, y_train)
print(grid.best_params_, grid.best_score_)
```

### Incremental Training (warm start)
```python
model = XGBClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Continue training
model.n_estimators += 50
model.fit(X_train2, y_train2, xgb_model=model.get_booster())
```

## Pitfalls

1. **`eval_set` deprecation**: In newer versions, use separate `eval_X`/`eval_y` keyword args instead of `eval_set` tuples. The old format still works but emits deprecation warning.
2. **`n_estimators` vs `num_boost_round`**: Sklearn uses `n_estimators`; `num_boost_round` is an alias. Don't use both.
3. **`fit()` called multiple times**: XGBoost sklearn wrapper does NOT support incremental `fit()` by default. Calling `fit()` again retrains from scratch unless you use `xgb_model` parameter.
4. **Random forest estimators deprecated**: `XGBRFClassifier`/`XGBRFRegressor` are deprecated. Use `num_parallel_tree` parameter on the base estimators instead.
5. **Categorical features**: Must set `enable_categorical=True` AND ensure categorical columns are properly typed (pandas category or explicit `feature_types`). XGBoost does its own encoding — don't one-hot encode first.
6. **`feature_importances_` type**: Default `importance_type='gain'` changes after loading a saved model — prefer `'weight'` for persistence.
7. **`predict_proba` output shape**: For binary classification, `predict_proba()` returns (n_samples, 2); for multi-class, (n_samples, n_classes); for multi-label, (n_samples, n_classes).
8. **XGBRanker `qid`**: Must pass `qid` to `fit()`, and use `eval_qid` with `eval_set`. Without it, ranking metrics are meaningless.

## Cross-Library Bridges

| Source | Target | Relation | Description |
|--------|--------|----------|-------------|
| `XGBClassifierBase` | `sklearn.feature_selection` | **consumer** | Used with RFECV, SelectFromModel, etc. |
| `XGBRegressorBase` | `backtrader.simulate_portfolio()` | **quant_bridge** | XGBoost regressor feeds predictions into portfolio simulation |
| `XGBClassifier` | `sklearn.pipeline.Pipeline` | **compatible** | Fully compatible with sklearn Pipeline, FeatureUnion |
| `XGBClassifier` | `sklearn.model_selection.GridSearchCV` | **compatible** | Accepts sklearn-compatible param grids |
| `XGBRegressor` | `optuna.Trial` | **optimization_target** | Hyperparameters tuned via optuna |
| `XGBModel.get_booster()` | `xgb.Booster` | **bridge** | Access native API from sklearn wrapper |

### Optuna Hyperparameter Optimization
```python
import optuna
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score

def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 500),
        'max_depth': trial.suggest_int('max_depth', 3, 15),
        'learning_rate': trial.suggest_float('lr', 1e-3, 0.5, log=True),
        'subsample': trial.suggest_float('subsample', 0.5, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 1.0),
        'reg_alpha': trial.suggest_float('reg_alpha', 1e-8, 10.0, log=True),
        'reg_lambda': trial.suggest_float('reg_lambda', 1e-8, 10.0, log=True),
        'random_state': 42,
    }
    model = XGBClassifier(**params)
    return cross_val_score(model, X, y, cv=5, scoring='accuracy').mean()

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)
```

## Verification Checklist

- [ ] `objective` parameter matches task (binary, multi, regression, ranking)
- [ ] `eval_metric` is set for early stopping to work
- [ ] `eval_set` provided with separate validation data (not train data)
- [ ] `early_stopping_rounds` > 0 to avoid training full `n_estimators` every time
- [ ] For multi-class: `num_class` set and `objective` is `'multi:softprob'` or `'multi:softmax'`
- [ ] For ranking: `qid` passed to `fit()`, `eval_qid` passed for validation
- [ ] Categorical features: `enable_categorical=True` and columns are properly typed
- [ ] Model saved via sklearn wrapper (`.save_model()`) or joblib for Pipeline
- [ ] `random_state` set for reproducibility

## References

- Source: `python-package/xgboost/sklearn.py` (XGBModel, XGBClassifier, XGBRegressor, XGBRanker, mixins)
- Graph communities: 0, 1, 23, 37, 79, 83, 124, 132, 149, 187, 370, 371, 394

## Provenance

- Knowledge graph: xgboost, 1631 nodes, 4318 edges, 80 communities
- God nodes: `XGBModel` (51), `sklearn.py` (48), `XGBRanker` (19) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 2a4786e61e08, backend opencode, description coverage 84%
