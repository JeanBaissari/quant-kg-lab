---
name: scikit-learn-preprocessing
description: "Use when working with scikit-learn data preprocessing, scaling, encoding, discretization, or feature transformations. Covers StandardScaler, OneHotEncoder, LabelEncoder, PolynomialFeatures, PowerTransformer, and more."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn/scikit-learn
source_commit: 6f8b95aa2234102acc3804fc8c7a3e6bd0506bfb
extraction_date: 2026-07-29
graph:
  nodes: 8662
  edges: 29241
  community_count: 401
  graph_hash: e587e89627b31941
tags: [scikit-learn, machine-learning, preprocessing, encoding, scaling, feature-engineering]
related_skills: [scikit-learn-model-selection, scikit-learn-metrics, scikit-learn-compose]
---

# scikit-learn Preprocessing

Extracted from scikit-learn knowledge graph. Source: `sklearn.preprocessing` module.

## Quick Reference

### Scalers (Numerical Features)

| Class | Purpose | Key Params |
|-------|---------|------------|
| `StandardScaler` | Zero-mean, unit-variance scaling | `with_mean`, `with_std` |
| `MinMaxScaler` | Scale to [0, 1] or custom range | `feature_range` |
| `MaxAbsScaler` | Scale by max absolute value (sparse-safe) | (none) |
| `RobustScaler` | Scale using median/IQR (outlier-robust) | `with_centering`, `with_scaling`, `quantile_range` |
| `Normalizer` | Row-wise normalization to unit norm | `norm` ('l2', 'l1', 'max') |

### Power / Distribution Transforms

| Class | Purpose | Key Params |
|-------|---------|------------|
| `PowerTransformer` | Box-Cox or Yeo-Johnson transform | `method` ('yeo-johnson', 'box-cox'), `standardize` |
| `QuantileTransformer` | Map to uniform or normal distribution | `n_quantiles`, `output_distribution`, `subsample` |

### Encoders (Categorical Features)

| Class | Purpose | Key Params |
|-------|---------|------------|
| `OneHotEncoder` | One-hot / dummy encoding | `drop`, `sparse_output`, `handle_unknown`, `min_frequency` |
| `OrdinalEncoder` | Integer ordinal encoding | `categories`, `handle_unknown`, `encoded_missing_value` |
| `LabelEncoder` | Encode target labels (1D only) | (none) |
| `LabelBinarizer` | One-vs-all binary encoding (1D) | `neg_label`, `pos_label`, `sparse_output` |
| `TargetEncoder` | Target-based encoding (for high-cardinality) | `categories`, `target_type`, `smooth` |

### Feature Construction

| Class | Purpose | Key Params |
|-------|---------|------------|
| `PolynomialFeatures` | Generate polynomial/interaction features | `degree`, `interaction_only`, `include_bias` |
| `SplineTransformer` | B-spline basis functions | `n_knots`, `degree`, `knots`, `extrapolation` |
| `KBinsDiscretizer` | Bin continuous data into intervals | `n_bins`, `encode`, `strategy` ('uniform', 'quantile', 'kmeans') |
| `FunctionTransformer` | Apply arbitrary function as transform | `func`, `inverse_func`, `check_inverse` |
| `Binarizer` | Threshold numerical data to binary | `threshold` |

### Standalone Functions

| Function | Purpose |
|----------|---------|
| `scale` | Standardize (equiv. `StandardScaler`) |
| `minmax_scale` | Min-max scale (equiv. `MinMaxScaler`) |
| `maxabs_scale` | Max-abs scale (equiv. `MaxAbsScaler`) |
| `robust_scale` | Robust scale (equiv. `RobustScaler`) |
| `normalize` | Row-wise normalize (equiv. `Normalizer`) |
| `binarize` | Threshold binarize (equiv. `Binarizer`) |
| `label_binarize` | One-vs-all binary encoding |
| `add_dummy_feature` | Add constant bias column |
| `power_transform` | Box-Cox / Yeo-Johnson (equiv. `PowerTransformer`) |
| `quantile_transform` | Quantile transform (equiv. `QuantileTransformer`) |

## Common Pitfalls

1. **`LabelEncoder` is NOT for features**: It's designed for 1D target labels. Use `OrdinalEncoder` for feature columns — it handles 2D arrays and unknown categories.
2. **`StandardScaler` on sparse data**: Setting `with_mean=True` on sparse matrices raises an error (cannot center sparse). Use `with_mean=False` or densify first.
3. **`PowerTransformer` with `method='box-cox'`**: Requires strictly positive data. Use `method='yeo-johnson'` for zero or negative values.
4. **`OneHotEncoder` `handle_unknown='error'`** (default): Crashes on unseen categories in `transform()`. Set `handle_unknown='ignore'` for production pipelines.
5. **`QuantileTransformer` `subsample`**: Defaults to 10000 for large datasets — can cause non-deterministic behavior. Set `subsample=None` for full-data quantile computation.
6. **Scaler fit on train only**: Always `fit_transform()` on train, then only `transform()` on test. Chaining in a `Pipeline` automates this.

## Verification Checklist

- [ ] `OrdinalEncoder` used for feature columns (not `LabelEncoder`)
- [ ] `handle_unknown='ignore'` on `OneHotEncoder` for production pipelines
- [ ] `PowerTransformer` using correct `method` for data range
- [ ] Scaler fitted only on training data (inside Pipeline)
- [ ] Sparse matrices handled correctly (no centering)
- [ ] Target encoding uses proper cross-fitting to avoid leakage