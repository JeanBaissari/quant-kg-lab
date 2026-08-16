---
name: scikit-learn-ensemble
description: "Use when working with scikit-learn Ensemble methods \u2014 bagging,\
  \ boosting, stacking, voting, and forests. Covers core classes, methods, and quant-relevant\
  \ patterns."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn/scikit-learn
source_commit: 6f8b95aa2234102acc3804fc8c7a3e6bd0506bfb
extraction_date: 2026-07-29
graph:
  nodes: 8450
  edges: 28094
  community_count: 367
  graph_hash: 75a69cbf83913826
tags:
- scikit-learn
- machine-learning
- ensemble
- bagging
- boosting
- random-forest
related_skills:
- scikit-learn-model-selection
- scikit-learn-metrics
- scikit-learn-tree
target_version: '1.9.0 (dev: after 1.9.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `scikit-learn` ahead of the latest PyPI release (1.9.0 (dev: after 1.9.0)). Some APIs may not exist in your installed version.

# scikit-learn Ensemble Methods

Extracted from scikit-learn knowledge graph. Source: `sklearn.ensemble` module.
Communities: 3 ("Ensemble Methods Bagging"), 5 ("Ensemble Methods Boosting"), 235 ("BaggingClassifier").

## Quick Reference
| Class/Function | Source File | Purpose | Key Params |
|---------------|-------------|---------|------------|
| `RandomForestClassifier` | `ensemble/_forest.py:L1174` | RF classification; bagged trees + feature randomness | `n_estimators`, `max_depth`, `max_features`, `min_samples_split`, `oob_score` |
| `RandomForestRegressor` | `ensemble/_forest.py:L1577` | RF regression | `n_estimators`, `max_depth`, `max_features`, `oob_score` |
| `GradientBoostingClassifier` | `ensemble/_gb.py:L1123` | Gradient-boosted trees for classification | `n_estimators`, `learning_rate`, `max_depth`, `subsample`, `loss` |
| `GradientBoostingRegressor` | `ensemble/_gb.py:L1734` | Gradient-boosted trees for regression | `n_estimators`, `learning_rate`, `max_depth`, `loss`, `alpha` (Huber/quantile) |
| `BaggingClassifier` | `ensemble/_bagging.py:L683` | Bootstrap-aggregated classifier | `estimator`, `n_estimators`, `max_samples`, `bootstrap`, `oob_score` |
| `BaggingRegressor` | `ensemble/_bagging.py:L1192` | Bootstrap-aggregated regressor | `estimator`, `n_estimators`, `max_samples`, `bootstrap` |
| `AdaBoostClassifier` | `ensemble/_weight_boosting.py:L321` | Adaptive boosting (SAMME) | `estimator`, `n_estimators`, `learning_rate`, `random_state` |
| `AdaBoostRegressor` | `ensemble/_weight_boosting.py:L823` | AdaBoost for regression | `estimator`, `n_estimators`, `learning_rate`, `loss` |
| `StackingClassifier` | `ensemble/_stacking.py:L422` | Stacked generalization classifier | `estimators`, `final_estimator`, `cv`, `stack_method` |
| `StackingRegressor` | `ensemble/_stacking.py:L841` | Stacked generalization regressor | `estimators`, `final_estimator`, `cv` |
| `VotingClassifier` | `ensemble/_voting.py:L194` | Soft/hard voting over estimators | `estimators`, `voting` ('soft'/'hard'), `weights` |
| `VotingRegressor` | `ensemble/_voting.py:L546` | Average predictions over estimators | `estimators`, `weights` |
| `HistGradientBoostingClassifier` | `ensemble/_hist_gradient_boosting/` | Histogram-based GBDT (fast) | `max_iter`, `learning_rate`, `max_depth`, `l2_regularization` | `ensemble/_hist_gradient_boosting/gradient_boosting.py:L1761` |

| `HistGradientBoostingRegressor` | `ensemble/_hist_gradient_boosting/` | Histogram-based GBDT regression | `max_iter`, `learning_rate`, `max_depth`, `loss` | `ensemble/_hist_gradient_boosting/gradient_boosting.py:L1359` |

| `ExtraTreesClassifier` | `ensemble/_forest.py:L1963` | Extremely randomized trees | `n_estimators`, `max_depth`, `max_features`, `bootstrap` |
| `IsolationForest` | `ensemble/_iforest.py:L54` | Anomaly detection via random partitioning | `n_estimators`, `max_samples`, `contamination` |

### Key Methods (from graph node analysis)

| Method | Prevalence | Description |
|--------|-----------|-------------|
| `.fit(X, y)` | 13 nodes across all classes | Train the ensemble |
| `.predict(X)` | 14 nodes | Predict class/value |
| `.predict_proba(X)` | 8 nodes | Class probabilities (classifiers) |
| `.predict_log_proba(X)` | 5 nodes | Log-probabilities |
| `.decision_function(X)` | 3 nodes | Raw decision scores |
| `.apply(X)` | 2 nodes | Leaf indices per tree (GBDT, RF) |
| `.staged_predict(X)` | 2 nodes | Iterable of predictions per boosting stage |
| `.score(X, y)` | 2 nodes | R² or accuracy |
| `._set_oob_score()` | 3 nodes | Internal OOB scoring (bagging/RF) |
| `.feature_importances_` | — | Gini/permutation importance (post-fit) |

## Common Patterns

```python
# Random Forest — robust baseline for tabular quant data
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    max_features=0.3,
    min_samples_leaf=5,
    oob_score=True,
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
print(f"OOB R²: {rf.oob_score_:.4f}")
importances = rf.feature_importances_

# Gradient Boosting — sequential tree boosting with early stopping
from sklearn.ensemble import GradientBoostingRegressor
gbr = GradientBoostingRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=4,
    subsample=0.8,
    validation_fraction=0.1,
    n_iter_no_change=20,
    random_state=42,
)
gbr.fit(X_train, y_train)
# Access staged predictions for custom validation curves
staged_preds = gbr.staged_predict(X_val)

# HistGradientBoosting — faster alternative, native NA handling
from sklearn.ensemble import HistGradientBoostingRegressor
hgb = HistGradientBoostingRegressor(
    max_iter=500, learning_rate=0.05, max_depth=4,
    early_stopping=True, validation_fraction=0.1,
    random_state=42
)
hgb.fit(X_train, y_train)

# Stacking — combine diverse base models
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import Ridge
estimators = [('rf', RandomForestRegressor()), ('gbr', GradientBoostingRegressor())]
stack = StackingRegressor(estimators=estimators, final_estimator=Ridge(), cv=5)
stack.fit(X_train, y_train)
```

## Pitfalls

1. **OOB vs. cross-validation**: `oob_score_` is convenient but biased for small datasets; prefer proper CV for model selection.
2. **GBDT overfits easily**: Always use `validation_fraction` + `n_iter_no_change` (or `early_stopping` for HistGBDT). Small learning rates need more estimators.
3. **`predict_proba` vs `predict_log_proba`**: Use `predict_log_proba` for numerical stability in pipeline scoring functions.
4. **IsolationForest `contamination`**: Must be set correctly — auto-detection is unreliable for time-series data.
5. **memory**: Forests with many deep trees can consume GBs. Use `max_depth` and `max_leaf_nodes` to bound model size.
6. **Stacking CV leak**: The `cv` parameter in stacking splits *training* data; don't confuse with outer CV.

## Provenance

- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `TreeGrower` (56), `BaseHistGradientBoosting` (50), `BaseGradientBoosting` (46) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
