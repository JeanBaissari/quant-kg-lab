---
name: scikit-learn-feature-selection
description: "Use when working with scikit-learn feature selection \u2014 filter methods\
  \ (SelectKBest, chi2, f_classif), wrapper methods (RFE, RFECV), embedded methods\
  \ (SelectFromModel), and sequential feature selection."
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
  graph_hash: 9ce80bbf4dcf8c7c
tags:
- scikit-learn
- machine-learning
- feature-selection
- feature-engineering
- dimensionality-reduction
related_skills:
- scikit-learn-model-selection
- scikit-learn-linear-model
- scikit-learn-decomposition
target_version: '1.9.0 (dev: after 1.9.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `scikit-learn` ahead of the latest PyPI release (1.9.0 (dev: after 1.9.0)). Some APIs may not exist in your installed version.

# scikit-learn Feature Selection

Extracted from scikit-learn knowledge graph. Source: `sklearn.feature_selection` module.

## Quick Reference
### Filter Methods (Univariate)

| Class/Function | Purpose | Key Params | Graph Node |
| -------------- | ------- | ---------- |
| `SelectKBest` | Select top-k scoring features | `score_func`, `k` | feature_selection/_univariate_selection.py:L698 |
| `SelectPercentile` | Select top percentile of features | `score_func`, `percentile` | feature_selection/_univariate_selection.py:L593 |
| `SelectFpr` | Select based on FPR (false positive rate) | `score_func`, `alpha` | feature_selection/_univariate_selection.py:L809 |
| `SelectFdr` | Select based on FDR (false discovery rate) | `score_func`, `alpha` | feature_selection/_univariate_selection.py:L889 |
| `SelectFwe` | Select based on family-wise error | `score_func`, `alpha` | feature_selection/_univariate_selection.py:L980 |
| `GenericUnivariateSelect` | Configurable univariate selection | `score_func`, `mode`, `param` | feature_selection/_univariate_selection.py:L1062 |

### Scoring Functions

| Function | Purpose | Target Type | covariance/_elliptic_envelope.py:L187 |
|----------|---------|-------------|
| `chi2` | Chi-squared statistic | Classification (non-negative features) | feature_selection/_univariate_selection.py:L200 |
| `f_classif` | ANOVA F-value | Classification | feature_selection/_univariate_selection.py:L125 |
| `f_regression` | F-value between feature and target | Regression | feature_selection/_univariate_selection.py:L406 |
| `f_oneway` | One-way ANOVA | Classification | feature_selection/_univariate_selection.py:L41 |
| `mutual_info_classif` | Mutual information | Classification | feature_selection/_mutual_info.py:L465 |
| `mutual_info_regression` | Mutual information | Regression | feature_selection/_mutual_info.py:L337 |
| `r_regression` | Pearson correlation coefficient | Regression | feature_selection/_univariate_selection.py:L301 |

### Wrapper Methods

| Class | Purpose | Key Params | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|------------|
| `RFE` | Recursive Feature Elimination | `estimator`, `n_features_to_select`, `step` | feature_selection/_rfe.py:L74 |
| `RFECV` | RFE with cross-validated feature count | `estimator`, `step`, `cv`, `scoring`, `min_features_to_select` | feature_selection/_rfe.py:L559 |
| `SequentialFeatureSelector` | Forward/backward sequential selection | `estimator`, `n_features_to_select`, `direction`, `cv`, `scoring` | feature_selection/_sequential.py:L34 |

### Embedded / Model-Based Methods

| Class | Purpose | Key Params | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|------------|
| `SelectFromModel` | Select features based on model importance | `estimator`, `threshold`, `prefit`, `max_features` | feature_selection/_from_model.py:L95 |

### Variance-Based

| Class | Purpose | Key Params | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|------------|
| `VarianceThreshold` | Remove low-variance features | `threshold` | feature_selection/_variance_threshold.py:L15 |

### Base Mixin

| Class | Purpose | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|
| `SelectorMixin` | Mixin providing `get_support()` and `inverse_transform()` to all selectors | feature_selection/_base.py:L27 |

## Common Patterns

```python
# Filter: keep the top-k factor features by F-test against forward returns
import numpy as np
from sklearn.feature_selection import (RFE, SelectKBest, SequentialFeatureSelector,
                                       f_regression, mutual_info_regression)
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 8))  # momentum, vol, skew, volume z + 4 noise factors
y = 2.0 * X[:, 0] - 1.0 * X[:, 2] + rng.normal(scale=0.5, size=400)

sel = SelectKBest(score_func=f_regression, k=3).fit(X, y)
print(sel.get_support(indices=True))

# Nonlinear filter for non-linear factor/return relationships
mi = SelectKBest(score_func=mutual_info_regression, k=3).fit(X, y)
print(mi.get_support(indices=True))

# Wrapper: recursive feature elimination with a regularized estimator
rfe = RFE(estimator=Ridge(alpha=1.0), n_features_to_select=3, step=1).fit(X, y)
print(rfe.support_)

# Sequential forward selection scored inside a scaled pipeline
pipe = Pipeline([("scale", StandardScaler()), ("ridge", Ridge(alpha=1.0))])
sfs = SequentialFeatureSelector(pipe, n_features_to_select=3, direction="forward", cv=5)
sfs.fit(X, y)
print(sfs.get_support(indices=True))
```

## Pitfalls
1. **`chi2` requires non-negative features**: Chi-squared assumes frequencies/counts. For negative or continuous features, use `f_classif` or `mutual_info_classif` instead.
2. **Univariate ≠ Multivariate**: `SelectKBest` scores features independently. Features that are useless alone but useful in combination will be discarded. Use `RFE` or `SequentialFeatureSelector` for multivariate selection.
3. **`RFECV` `min_features_to_select`**: Default is 1. For models that need multiple features (e.g., `LogisticRegression` with `penalty='l1'`), set higher if 1-feature models crash.
4. **`SelectFromModel` `threshold`**: Default is `"mean"` (mean importance). `"median"` and `1.25*mean` are alternatives. Numeric thresholds select features with importance >= value.
5. **`SequentialFeatureSelector` `direction='forward'`** is greedy and can miss optimal subsets. `direction='backward'` starts from all features and removes one at a time — often more accurate but slower with many features.
6. **`VarianceThreshold` only removes constant features**: The default `threshold=0` only drops features with zero variance (all identical values). Near-constant features need a non-zero threshold, but this requires normalized data.
7. **`mutual_info_*` randomness**: These use nearest-neighbor estimation with randomness. Set `random_state` for reproducibility.

## Verification Checklist

- [ ] `score_func` compatible with feature values and target type
- [ ] Chi2 used only with non-negative features
- [ ] `RFECV` `min_features_to_select` high enough for estimator
- [ ] `random_state` set for mutual_info and SequentialFeatureSelector
- [ ] Feature selection performed inside Pipeline to avoid data leakage
- [ ] CV split strategy appropriate for data size

## Provenance

- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `RFE` (27), `SelectFromModel` (21), `SequentialFeatureSelector` (20) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
