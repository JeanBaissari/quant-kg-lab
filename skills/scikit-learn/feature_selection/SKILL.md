---
name: scikit-learn-feature-selection
description: Use when working with scikit-learn feature selection — filter methods (SelectKBest, chi2, f_classif), wrapper methods (RFE, RFECV), embedded methods (SelectFromModel), and sequential feature selection.
version: 0.1.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn/scikit-learn
source_version: main
extraction_date: 2026-07-29
graph_hash: 18753_nodes_49978_edges
graph_stats:
  nodes: 18753
  edges: 49978
  communities: [97, 154, 225, 341, 461]
metadata:
  hermes:
    tags: [scikit-learn, machine-learning, feature-selection, feature-engineering, dimensionality-reduction]
    related_skills: [scikit-learn-model-selection, scikit-learn-linear-model, scikit-learn-decomposition]
---

# scikit-learn Feature Selection

Extracted from scikit-learn knowledge graph. Source: `sklearn.feature_selection` module.

## Quick Reference

### Filter Methods (Univariate)

| Class/Function | Purpose | Key Params |
|---------------|---------|------------|
| `SelectKBest` | Select top-k scoring features | `score_func`, `k` |
| `SelectPercentile` | Select top percentile of features | `score_func`, `percentile` |
| `SelectFpr` | Select based on FPR (false positive rate) | `score_func`, `alpha` |
| `SelectFdr` | Select based on FDR (false discovery rate) | `score_func`, `alpha` |
| `SelectFwe` | Select based on family-wise error | `score_func`, `alpha` |
| `GenericUnivariateSelect` | Configurable univariate selection | `score_func`, `mode`, `param` |

### Scoring Functions

| Function | Purpose | Target Type |
|----------|---------|-------------|
| `chi2` | Chi-squared statistic | Classification (non-negative features) |
| `f_classif` | ANOVA F-value | Classification |
| `f_regression` | F-value between feature and target | Regression |
| `f_oneway` | One-way ANOVA | Classification |
| `mutual_info_classif` | Mutual information | Classification |
| `mutual_info_regression` | Mutual information | Regression |
| `r_regression` | Pearson correlation coefficient | Regression |

### Wrapper Methods

| Class | Purpose | Key Params |
|-------|---------|------------|
| `RFE` | Recursive Feature Elimination | `estimator`, `n_features_to_select`, `step` |
| `RFECV` | RFE with cross-validated feature count | `estimator`, `step`, `cv`, `scoring`, `min_features_to_select` |
| `SequentialFeatureSelector` | Forward/backward sequential selection | `estimator`, `n_features_to_select`, `direction`, `cv`, `scoring` |

### Embedded / Model-Based Methods

| Class | Purpose | Key Params |
|-------|---------|------------|
| `SelectFromModel` | Select features based on model importance | `estimator`, `threshold`, `prefit`, `max_features` |

### Variance-Based

| Class | Purpose | Key Params |
|-------|---------|------------|
| `VarianceThreshold` | Remove low-variance features | `threshold` |

### Base Mixin

| Class | Purpose |
|-------|---------|
| `SelectorMixin` | Mixin providing `get_support()` and `inverse_transform()` to all selectors |

## Common Pitfalls

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

## References

- `references/api.md` — Full API surface from knowledge graph
- `references/examples.md` — Extracted from scikit-learn examples/
