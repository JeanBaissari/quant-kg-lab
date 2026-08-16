---
name: scikit-learn-model-selection
description: Use when working with scikit-learn model selection, cross-validation,
  hyperparameter tuning, or GridSearchCV/RandomizedSearchCV workflows. Covers train_test_split,
  cross_val_score, GridSearchCV, RandomizedSearchCV, and validation curve analysis.
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
- model-selection
- cross-validation
- hyperparameter-tuning
related_skills:
- scikit-learn-metrics
- scikit-learn-preprocessing
---

# scikit-learn Model Selection

Extracted from scikit-learn knowledge graph. Source: `sklearn.model_selection` module.

## Quick Reference
### Cross-Validation Splitters

| Class | Purpose | Graph Node | Key Params |
|-------|---------|-----------|------------|
| `KFold` | K-fold cross-validation | model_selection/_split.py:L437 | `n_splits`, `shuffle`, `random_state` |
| `StratifiedKFold` | Stratified K-fold (preserves class %) | model_selection/_split.py:L687 | `n_splits`, `shuffle`, `random_state` |
| `GroupKFold` | Non-overlapping group K-fold | model_selection/_split.py:L533 | `n_splits` |
| `TimeSeriesSplit` | Time-series aware CV | model_selection/_split.py:L1116 | `n_splits`, `max_train_size`, `test_size` |
| `LeaveOneOut` | Leave-one-out CV | model_selection/_split.py:L171 | (none) |
| `LeavePOut` | Leave-P-out CV | model_selection/_split.py:L250 | `p` |
| `ShuffleSplit` | Random train/test splits | model_selection/_split.py:L1982 | `n_splits`, `test_size`, `random_state` |
| `StratifiedShuffleSplit` | Stratified shuffle split | model_selection/_split.py:L2233 | `n_splits`, `test_size`, `random_state` |
| `GroupShuffleSplit` | Group-aware shuffle split | model_selection/_split.py:L2087 | `n_splits`, `test_size`, `random_state` |
| `RepeatedKFold` | Repeated K-fold | model_selection/_split.py:L1683 | `n_splits`, `n_repeats`, `random_state` |
| `RepeatedStratifiedKFold` | Repeated stratified K-fold | model_selection/_split.py:L1749 | `n_splits`, `n_repeats`, `random_state` |
| `PredefinedSplit` | User-defined split indices | model_selection/_split.py:L2520 | `test_fold` |

### Hyperparameter Search

| Class | Purpose | Graph Node | Key Params |
|-------|---------|-----------|------------|
| `GridSearchCV` | Exhaustive param grid search | model_selection/_search.py:L1346 | `param_grid`, `cv`, `scoring`, `n_jobs`, `refit` |
| `RandomizedSearchCV` | Randomized param sampling | model_selection/_search.py:L1726 | `param_distributions`, `n_iter`, `cv`, `scoring` |
| `HalvingGridSearchCV` | Successive halving grid search | model_selection/_search_successive_halving.py:L426 | `param_grid`, `cv`, `factor`, `resource` |
| `HalvingRandomSearchCV` | Successive halving random search | model_selection/_search_successive_halving.py:L785 | `param_distributions`, `n_candidates`, `cv` |
| `ParameterGrid` | Cartesian product of param grid | model_selection/_search.py:L70 | `param_grid` |
| `ParameterSampler` | Sample from param distributions | model_selection/_search.py:L223 | `param_distributions`, `n_iter`, `random_state` |

### Tuning Utilities

| Function/Class | Purpose | Graph Node |
|----------------|---------|-----------|
| `TunedThresholdClassifierCV` | Post-hoc decision threshold tuning | model_selection/_classification_threshold.py:L499 |
| `BaseSearchCV` | Base class for all CV search estimators | model_selection/_search.py:L443 |
| `LearningCurveDisplay` | Plot learning curves from `learning_curve()` | model_selection/_plot.py:L126 |
| `ValidationCurveDisplay` | Plot validation curves from `validation_curve()` | model_selection/_plot.py:L511 |

### Core Functions

| Function | Purpose | Key Params | Graph Node |
|----------|---------|------------|-----------|
| `train_test_split` | Split arrays into train/test | `test_size`, `random_state`, `stratify` | model_selection/_split.py:L2797 |
| `cross_val_score` | Evaluate score by CV | `estimator`, `X`, `y`, `cv`, `scoring` | model_selection/_validation.py:L512 |
| `cross_validate` | Evaluate multiple metrics via CV | `cv`, `scoring` (dict), `return_train_score` | model_selection/_validation.py:L101 |
| `validation_curve` | Compute train/test scores vs param | `param_name`, `param_range`, `cv` | model_selection/_validation.py:L2276 |
| `learning_curve` | Compute scores vs training size | `train_sizes`, `cv`, `scoring` | model_selection/_validation.py:L1769 |
| `check_cv` | Validate/normalize CV splitter | `cv`, `y`, `classifier` | model_selection/_split.py:L2697 |

## Common Patterns

```python
# Quant CV must be temporal: TimeSeriesSplit never shuffles the return series
import numpy as np
from scipy.stats import loguniform
from sklearn.linear_model import Ridge
from sklearn.model_selection import (GridSearchCV, RandomizedSearchCV, TimeSeriesSplit,
                                     cross_val_score, train_test_split)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(0)
X = rng.normal(size=(500, 6))
y = X[:, 0] + 0.3 * X[:, 1] + rng.normal(scale=0.5, size=500)

tscv = TimeSeriesSplit(n_splits=5, test_size=50)
pipe = Pipeline([("std", StandardScaler()), ("ridge", Ridge())])

grid = {"ridge__alpha": [0.1, 1.0, 10.0]}
search = GridSearchCV(pipe, grid, cv=tscv, scoring="neg_mean_squared_error", n_jobs=-1)
search.fit(X, y)
print(search.best_params_, search.best_score_)

# RandomizedSearchCV for continuous alpha priors
dist = {"ridge__alpha": loguniform(1e-3, 1e2)}
rs = RandomizedSearchCV(pipe, dist, n_iter=20, cv=tscv, random_state=42, n_jobs=-1)
rs.fit(X, y)
print(rs.best_params_)

# Final estimate on a temporal holdout kept out of tuning
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, shuffle=False)
print(cross_val_score(rs.best_estimator_, Xtr, ytr, cv=tscv).mean())
```

## Pitfalls
1. **Data leakage in CV**: Always split before scaling. Use `Pipeline` to chain preprocessing + estimator so transforms are re-fit per fold.
2. **GridSearchCV `best_score_` vs production**: `best_score_` is the mean CV score on training data, not an independent test score. Always evaluate the refitted `best_estimator_` on a holdout set.
3. **`n_jobs` interaction**: `n_jobs=-1` uses all CPU cores but can conflict with underlying BLAS threading. Consider setting `OMP_NUM_THREADS=1` for CPU-bound estimators.
4. **Shuffle + `random_state`**: Without `shuffle=True`, `KFold` and `StratifiedKFold` do NOT shuffle — they split sequentially. This can bias results on ordered data.
5. **Halving vs Grid**: `HalvingGridSearchCV` is iterative — give it a broad `param_grid` and it will prune aggressively. Much faster than `GridSearchCV` for large grids.

## Verification Checklist

- [ ] Preprocessing inside `Pipeline`, not before CV split
- [ ] `scoring` metric matches business objective
- [ ] `random_state` set for reproducibility
- [ ] `refit=True` (default) for GridSearchCV to get a usable `best_estimator_`
- [ ] Holdout test set reserved for final evaluation after CV

## Provenance

- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `BaseSearchCV` (50), `StratifiedShuffleSplit` (31), `_split.py` (30) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
