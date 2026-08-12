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
  community_count: 401
  graph_hash: fc25a6d284e9a3ed
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

| Class | Purpose | Key Params | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node |
|-------|---------|------------|
| `KFold` | K-fold cross-validation | `n_splits`, `shuffle`, `random_state` | model_selection/_split.py:L437 |
| `StratifiedKFold` | Stratified K-fold (preserves class %) | `n_splits`, `shuffle`, `random_state` | model_selection/_split.py:L687 |
| `GroupKFold` | Non-overlapping group K-fold | `n_splits` | model_selection/_split.py:L533 |
| `TimeSeriesSplit` | Time-series aware CV | `n_splits`, `max_train_size`, `test_size` | model_selection/_split.py:L1116 |
| `LeaveOneOut` | Leave-one-out CV | (none) | model_selection/_split.py:L171 |
| `LeavePOut` | Leave-P-out CV | `p` | model_selection/_split.py:L250 |
| `ShuffleSplit` | Random train/test splits | `n_splits`, `test_size`, `random_state` | model_selection/_split.py:L1982 |
| `StratifiedShuffleSplit` | Stratified shuffle split | `n_splits`, `test_size`, `random_state` | model_selection/_split.py:L2233 |
| `GroupShuffleSplit` | Group-aware shuffle split | `n_splits`, `test_size`, `random_state` | model_selection/_split.py:L2087 |
| `RepeatedKFold` | Repeated K-fold | `n_splits`, `n_repeats`, `random_state` | model_selection/_split.py:L1683 |
| `RepeatedStratifiedKFold` | Repeated stratified K-fold | `n_splits`, `n_repeats`, `random_state` | model_selection/_split.py:L1749 |
| `PredefinedSplit` | User-defined split indices | `test_fold` | model_selection/_split.py:L2520 |

### Hyperparameter Search

| Class | Purpose | Key Params | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|------------|
| `GridSearchCV` | Exhaustive param grid search | `param_grid`, `cv`, `scoring`, `n_jobs`, `refit` | model_selection/_search.py:L1346 |
| `RandomizedSearchCV` | Randomized param sampling | `param_distributions`, `n_iter`, `cv`, `scoring` | model_selection/_search.py:L1726 |
| `HalvingGridSearchCV` | Successive halving grid search | `param_grid`, `cv`, `factor`, `resource` | model_selection/_search_successive_halving.py:L426 |
| `HalvingRandomSearchCV` | Successive halving random search | `param_distributions`, `n_candidates`, `cv` | model_selection/_search_successive_halving.py:L785 |
| `ParameterGrid` | Cartesian product of param grid | `param_grid` | model_selection/_search.py:L70 |
| `ParameterSampler` | Sample from param distributions | `param_distributions`, `n_iter`, `random_state` | model_selection/_search.py:L223 |

### Tuning Utilities

| Function/Class | Purpose |
|----------------|---------|
| `TunedThresholdClassifierCV` | Post-hoc decision threshold tuning | model_selection/_classification_threshold.py:L499 | model_selection/_classification_threshold.py:L499 |
| `BaseSearchCV` | Base class for all CV search estimators | model_selection/_search.py:L443 | model_selection/_search.py:L443 |
| `LearningCurveDisplay` | Plot learning curves from `learning_curve()` | model_selection/_plot.py:L126 | model_selection/_plot.py:L126 |
| `ValidationCurveDisplay` | Plot validation curves from `validation_curve()` | model_selection/_plot.py:L511 | model_selection/_plot.py:L511 |

### Core Functions

| Function | Purpose | Key Params | covariance/_elliptic_envelope.py:L187 |
|----------|---------|------------|
| `train_test_split` | Split arrays into train/test | `test_size`, `random_state`, `stratify` | model_selection/_split.py:L2797 |
| `cross_val_score` | Evaluate score by CV | `estimator`, `X`, `y`, `cv`, `scoring` | model_selection/_validation.py:L512 |
| `cross_validate` | Evaluate multiple metrics via CV | `cv`, `scoring` (dict), `return_train_score` | model_selection/_validation.py:L101 |
| `validation_curve` | Compute train/test scores vs param | `param_name`, `param_range`, `cv` | model_selection/_validation.py:L2276 |
| `learning_curve` | Compute scores vs training size | `train_sizes`, `cv`, `scoring` | model_selection/_validation.py:L1769 |
| `check_cv` | Validate/normalize CV splitter | `cv`, `y`, `classifier` | model_selection/_split.py:L2697 |

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
