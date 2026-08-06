---
name: scikit-learn-model-selection
description: "Use when working with scikit-learn model selection, cross-validation, hyperparameter tuning, or GridSearchCV/RandomizedSearchCV workflows. Covers train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV, and validation curve analysis."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn/scikit-learn
source_commit: 6f8b95aa2234102acc3804fc8c7a3e6bd0506bfb
extraction_date: 2026-07-29
graph:
  nodes: 18753
  edges: 49978
  community_count: 1149
  graph_hash: e4761fba3e257880
tags: [scikit-learn, machine-learning, model-selection, cross-validation, hyperparameter-tuning]
related_skills: [scikit-learn-metrics, scikit-learn-preprocessing]
---

# scikit-learn Model Selection

Extracted from scikit-learn knowledge graph. Source: `sklearn.model_selection` module.

## Quick Reference

### Cross-Validation Splitters

| Class | Purpose | Key Params |
|-------|---------|------------|
| `KFold` | K-fold cross-validation | `n_splits`, `shuffle`, `random_state` |
| `StratifiedKFold` | Stratified K-fold (preserves class %) | `n_splits`, `shuffle`, `random_state` |
| `GroupKFold` | Non-overlapping group K-fold | `n_splits` |
| `TimeSeriesSplit` | Time-series aware CV | `n_splits`, `max_train_size`, `test_size` |
| `LeaveOneOut` | Leave-one-out CV | (none) |
| `LeavePOut` | Leave-P-out CV | `p` |
| `ShuffleSplit` | Random train/test splits | `n_splits`, `test_size`, `random_state` |
| `StratifiedShuffleSplit` | Stratified shuffle split | `n_splits`, `test_size`, `random_state` |
| `GroupShuffleSplit` | Group-aware shuffle split | `n_splits`, `test_size`, `random_state` |
| `RepeatedKFold` | Repeated K-fold | `n_splits`, `n_repeats`, `random_state` |
| `RepeatedStratifiedKFold` | Repeated stratified K-fold | `n_splits`, `n_repeats`, `random_state` |
| `PredefinedSplit` | User-defined split indices | `test_fold` |

### Hyperparameter Search

| Class | Purpose | Key Params |
|-------|---------|------------|
| `GridSearchCV` | Exhaustive param grid search | `param_grid`, `cv`, `scoring`, `n_jobs`, `refit` |
| `RandomizedSearchCV` | Randomized param sampling | `param_distributions`, `n_iter`, `cv`, `scoring` |
| `HalvingGridSearchCV` | Successive halving grid search | `param_grid`, `cv`, `factor`, `resource` |
| `HalvingRandomSearchCV` | Successive halving random search | `param_distributions`, `n_candidates`, `cv` |
| `ParameterGrid` | Cartesian product of param grid | `param_grid` |
| `ParameterSampler` | Sample from param distributions | `param_distributions`, `n_iter`, `random_state` |

### Tuning Utilities

| Function/Class | Purpose |
|----------------|---------|
| `TunedThresholdClassifierCV` | Post-hoc decision threshold tuning |
| `BaseSearchCV` | Base class for all CV search estimators |
| `LearningCurveDisplay` | Plot learning curves from `learning_curve()` |
| `ValidationCurveDisplay` | Plot validation curves from `validation_curve()` |

### Core Functions

| Function | Purpose | Key Params |
|----------|---------|------------|
| `train_test_split` | Split arrays into train/test | `test_size`, `random_state`, `stratify` |
| `cross_val_score` | Evaluate score by CV | `estimator`, `X`, `y`, `cv`, `scoring` |
| `cross_validate` | Evaluate multiple metrics via CV | `cv`, `scoring` (dict), `return_train_score` |
| `validation_curve` | Compute train/test scores vs param | `param_name`, `param_range`, `cv` |
| `learning_curve` | Compute scores vs training size | `train_sizes`, `cv`, `scoring` |
| `check_cv` | Validate/normalize CV splitter | `cv`, `y`, `classifier` |

## Common Pitfalls

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