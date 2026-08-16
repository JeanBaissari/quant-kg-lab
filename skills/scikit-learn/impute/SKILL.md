---
name: scikit-learn-impute
description: "Use when working with scikit-learn Imputation \u2014 SimpleImputer,\
  \ KNNImputer, IterativeImputer, and MissingIndicator. Covers core classes, methods,\
  \ and quant-relevant patterns."
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
- imputation
- missing-data
- preprocessing
- quant
related_skills:
- scikit-learn-preprocessing
- scikit-learn-model-selection
- scikit-learn-metrics
target_version: '1.9.0 (dev: after 1.9.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `scikit-learn` ahead of the latest PyPI release (1.9.0 (dev: after 1.9.0)). Some APIs may not exist in your installed version.

# scikit-learn Imputation

Extracted from scikit-learn knowledge graph. Source: `sklearn.impute` module.
Communities: 140 ("Imputation SimpleImputer/MissingIndicator"), 297 ("IterativeImputer"), 436 ("KNNImputer").

## Quick Reference
| Class/Function | Source File | Purpose | Key Params |
|---------------|-------------|---------|------------|
| `SimpleImputer` | `impute/_base.py:L171` | Basic univariate imputation | `strategy` ('mean'/'median'/'most_frequent'/'constant'), `missing_values` (np.nan), `fill_value`, `keep_empty_features` |
| `KNNImputer` | `impute/_knn.py:L24` | k-Nearest Neighbors imputation | `n_neighbors`, `weights` ('uniform'/'distance'), `metric`, `keep_empty_features` |
| `IterativeImputer` | `impute/_iterative.py:L58` | Multivariate MICE-style imputation | `estimator` (default BayesianRidge), `max_iter`, `n_nearest_features`, `initial_strategy`, `imputation_order`, `skip_complete`, `keep_empty_features` |
| `MissingIndicator` | `impute/_base.py:L787` | Binary indicator of missingness | `missing_values`, `features` ('all'/'missing-only'), `sparse` |

### Key Methods (from graph node analysis)

| Method | Prevalence | Description |
|--------|-----------|-------------|
| `.transform(X)` | 8 nodes | Impute values in X |
| `.fit(X, y=None)` | 7 nodes | Learn imputation parameters |
| `.fit_transform(X, y=None)` | 2 nodes | Fit and transform in one call |
| `.__init__()` | 5 nodes | Constructors |
| `.get_feature_names_out()` | 4 nodes | Get output feature names (useful with `keep_empty_features`) |
| `._validate_input(X)` | 2 nodes | Internal input validation |

### Additional Imputer Internals

| Method | Class | Description |
|--------|-------|-------------|
| `._impute_one_feature()` | IterativeImputer | Impute a single feature column using all others |
| `._get_neighbor_feat_idx()` | IterativeImputer | Select most correlated neighbor features |
| `._get_ordered_idx()` | IterativeImputer | Determine feature imputation order |
| `._get_abs_corr_mat()` | IterativeImputer | Compute absolute correlation matrix for feature selection |
| `._initial_imputation()` | IterativeImputer | Initial fill (mean/median/most_frequent) |
| `._calc_impute()` | KNNImputer | Core k-NN weighted average computation |

## Common Patterns

```python
# SimpleImputer — fast, univariate, good default
from sklearn.impute import SimpleImputer
imp = SimpleImputer(strategy='median', missing_values=np.nan)
X_clean = imp.fit_transform(X_train)
# Apply to test data with same statistics
X_test_clean = imp.transform(X_test)

# KNNImputer — multivariate, similarity-based
from sklearn.impute import KNNImputer
knn_imp = KNNImputer(n_neighbors=5, weights='distance')
X_clean = knn_imp.fit_transform(X)

# IterativeImputer (MICE) — model-based, best for quant data
from sklearn.impute import IterativeImputer
from sklearn.linear_model import BayesianRidge
from sklearn.ensemble import RandomForestRegressor

# Bayesian ridge (default) — probabilistic, handles uncertainty
mice = IterativeImputer(
    estimator=BayesianRidge(),
    max_iter=20,
    n_nearest_features=10,   # limit to top-K correlated features
    initial_strategy='median',
    imputation_order='ascending',  # least-to-most missing
    random_state=42,
    skip_complete=True,          # skip features with no missing values
)
X_clean = mice.fit_transform(X)

# Tree-based iterative imputation — captures non-linear relationships
mice_rf = IterativeImputer(
    estimator=RandomForestRegressor(n_estimators=50, random_state=42),
    max_iter=20,
    random_state=42,
)
X_clean_rf = mice_rf.fit_transform(X)

# MissingIndicator — preserve the signal of missingness
from sklearn.impute import MissingIndicator
from sklearn.pipeline import make_union, make_pipeline
from sklearn.compose import ColumnTransformer

# Add missingness indicators as features
indicator = MissingIndicator(features='all', sparse=False)
missing_flags = indicator.fit_transform(X)
# Often improves model performance — missingness is informative in quant data

# Full pipeline: impute + indicator + model
from sklearn.pipeline import make_pipeline
pipeline = make_pipeline(
    SimpleImputer(strategy='median'),
    SomeEstimator()
)

# ColumnTransformer approach for mixed strategies
from sklearn.compose import ColumnTransformer
preprocessor = ColumnTransformer([
    ('num_median', SimpleImputer(strategy='median'), numeric_cols),
    ('num_knn', KNNImputer(n_neighbors=5), high_missing_cols),
    ('cat_mode', SimpleImputer(strategy='most_frequent'), categorical_cols),
])
```

## Pitfalls

1. **Data leakage**: Always fit imputers on training data only, then transform both train and test. Never fit on the full dataset before splitting.
2. **IterativeImputer convergence**: `max_iter` default is 10 — may not converge for complex patterns. Check `imputation_sequence_` for stability. Increase to 20–50 for quant data with structured missingness.
3. **KNNImputer with many features**: Distance-based imputation breaks down in high dimensions (curse of dimensionality). Use `n_nearest_features` to restrict to top correlated features.
4. **Constant imputation trap**: `strategy='constant'` with `fill_value=0` creates artificial point masses that mislead tree-based models (splits on the imputed value). Prefer `strategy='median'` or add `MissingIndicator`.
5. **`keep_empty_features`**: When a column is all-NaN in training, default behavior drops it. Set `keep_empty_features=True` to preserve column count for pipelines with fixed feature ordering.
6. **MissingIndicator `features` parameter**: `'all'` returns indicator for all features (even those without missing values). `'missing-only'` (default) only returns indicators for features with at least one missing value — changes output dimension.
7. **Performance**: `IterativeImputer` trains `max_iter × n_features_with_missing` models. For 100 features with missing values and `max_iter=20`, that's 2000 model fits. Use `n_nearest_features` and `sample_posterior=False` for speed.

## Provenance

- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `IterativeImputer` (19), `MissingIndicator` (17), `SimpleImputer` (16) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
