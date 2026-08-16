---
name: catboost-core
description: "Use when training catboost models \u2014 CatBoostClassifier/Regressor/Ranker,\
  \ loss_function and eval_metric choices, native categorical handling, model persistence,\
  \ and feature importance."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: catboost/catboost
source_commit: 549af60ecd40819be138046cd9c5ec737dca5e3b
extraction_date: 2026-08-13
graph:
  nodes: 793
  edges: 1569
  community_count: 52
  graph_hash: 59f3c1631da37620
tags:
- catboost
- classifier
- regressor
- boosting
related_skills:
- catboost
- catboost-pool
- catboost-evaluation
- scikit-learn-ensemble
- shap-explainers
- optuna-integration
---

# catboost.core

The model classes: sklearn-compatible `CatBoostClassifier`/`CatBoostRegressor`/
`CatBoostRanker` plus the shared `CatBoost` base — `fit`/`predict`/`predict_proba`,
loss-function and eval-metric selection, native categorical features, persistence.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `CatBoost` | `core.py:L2563` | Base model class — shared fit/predict/save/load machinery |
| `CatBoostClassifier` | `core.py:L4872` | Classification — binary/multiclass, predict_proba |
| `CatBoostRegressor` | `core.py` | Regression — quantile/multi-target variants |
| `CatBoostRanker` | `core.py` | Ranking — group_id + pairwise losses |
| `Pool` | `core.py:L603` | The data container — X/y/cat_features/group_id/pairs |
| `.is_fitted()` | `core.py:L1840` | Check whether the model has been fitted |
| `.get_feature_importance()` | `core.py` | Feature importances — PredictionValuesChange or SHAP |
| `.save_model()` / `.load_model()` | `core.py` | Model persistence (cbm format) |
| `.predict()` | `core.py` | Prediction — numpy/DataFrame output |
| `BuiltinMetric` | `metrics.py:L25` | Enum of built-in eval metrics (deg 123 hub) |

## Common Patterns

- **Native categoricals**:
  ```python
  model = CatBoostClassifier(iterations=1000, cat_features=[2, 5], verbose=0)
  model.fit(X, y)
  ```
  — no one-hot/label encoding needed; ordered boosting respects category statistics.
- **Loss choice**: `loss_function='Logloss'` (binary), `'MultiClass'`, `'RMSE'`,
  `'Quantile:alpha=0.5'`, `'MAE'`, `'CrossEntropy'` (probabilities in).
- **Eval discipline**: `eval_metric='AUC'` (classifier), `'RMSE'` (regression),
  `'NDCG'` (ranking) — set separately from the loss; early stopping via
  `early_stopping_rounds` + an eval set.
- **Missing values**: catboost handles NaNs natively for both numeric and categorical
  features — no imputation pass required.
- **Feature importance**: `model.get_feature_importance(type='PredictionValuesChange')`
  or the native SHAP path (`shap.TreeExplainer(model)`).
- **Ranking**: `CatBoostRanker` + `Pool(group_id=...)` with `loss_function='YetiRank'`.
- **Persistence**: `.save_model('m.cbm')` / `CatBoostClassifier().load_model('m.cbm')`
  — the cbm format carries the full config.

## Pitfalls

- **cat_features indices**: they index the raw X columns AFTER any preprocessing —
  using sklearn ColumnTransformer indices is a common mismatch.
- **Verbose spam**: `verbose=0` or `verbose_eval=50` in production loops; the default
  prints per-iteration metrics.
- **Overfitting on small data**: catboost's symmetric trees + ordered boosting can
  overfit quickly — use `l2_leaf_reg`, `depth` (default 6), and early stopping.
- **`use_best_model`**: needs an `eval_set` — without it, the "best" iteration logic
  silently falls back to the last.
- **Text features**: `text_features` require the text-processing pipeline config —
  not free.
- **Ranking requires groups**: `group_id` in Pool is mandatory for ranker losses.

## Provenance

Graph: `knowledge_graphs/catboost/.graphify/graph.json` — 793 nodes · 1569 edges ·
38 communities · graphify @ 549af60ecd40, backend opencode, description coverage 87.5%.

## Verification Checklist

- [ ] `CatBoostClassifier(cat_features=[...]).fit(X, y)` trains with raw categoricals
- [ ] `.get_feature_importance()` returns per-feature values
- [ ] `.save_model()`/`.load_model()` round-trips
- [ ] QR rows cite `core.py`/`metrics.py` files resolvable in the catboost graph
