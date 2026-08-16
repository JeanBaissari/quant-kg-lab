---
name: scikit-learn-preprocessing
description: Use when working with scikit-learn data preprocessing, scaling, encoding,
  discretization, or feature transformations. Covers StandardScaler, OneHotEncoder,
  LabelEncoder, PolynomialFeatures, PowerTransformer, and more.
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
- preprocessing
- encoding
- scaling
- feature-engineering
related_skills:
- scikit-learn-model-selection
- scikit-learn-metrics
- scikit-learn-compose
---

# scikit-learn Preprocessing

Extracted from scikit-learn knowledge graph. Source: `sklearn.preprocessing` module.

## Quick Reference
### Scalers (Numerical Features)

| Class | Purpose | Key Params | Graph Node |
| ----- | ------- | ---------- |
| `StandardScaler` | Zero-mean, unit-variance scaling | `with_mean`, `with_std` | preprocessing/_data.py:L742 |
| `MinMaxScaler` | Scale to [0, 1] or custom range | `feature_range` | preprocessing/_data.py:L305 |
| `MaxAbsScaler` | Scale by max absolute value (sparse-safe) | (none) | preprocessing/_data.py:L1190 |
| `RobustScaler` | Scale using median/IQR (outlier-robust) | `with_centering`, `with_scaling`, `quantile_range` | preprocessing/_data.py:L1552 |
| `Normalizer` | Row-wise normalization to unit norm | `norm` ('l2', 'l1', 'max') | preprocessing/_data.py:L2092 |

### Power / Distribution Transforms

| Class | Purpose | Key Params | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|------------|
| `PowerTransformer` | Box-Cox or Yeo-Johnson transform | `method` ('yeo-johnson', 'box-cox'), `standardize` | preprocessing/_data.py:L3257 |
| `QuantileTransformer` | Map to uniform or normal distribution | `n_quantiles`, `output_distribution`, `subsample` | preprocessing/_data.py:L2670 |

### Encoders (Categorical Features)

| Class | Purpose | Key Params | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|------------|
| `OneHotEncoder` | One-hot / dummy encoding | `drop`, `sparse_output`, `handle_unknown`, `min_frequency` | preprocessing/_encoders.py:L474 |
| `OrdinalEncoder` | Integer ordinal encoding | `categories`, `handle_unknown`, `encoded_missing_value` | preprocessing/_encoders.py:L1263 |
| `LabelEncoder` | Encode target labels (1D only) | (none) | preprocessing/_label.py:L39 |
| `LabelBinarizer` | One-vs-all binary encoding (1D) | `neg_label`, `pos_label`, `sparse_output` | preprocessing/_label.py:L183 |
| `TargetEncoder` | Target-based encoding (for high-cardinality) | `categories`, `target_type`, `smooth` | preprocessing/_target_encoder.py:L34 |

### Feature Construction

| Class | Purpose | Key Params | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|------------|
| `PolynomialFeatures` | Generate polynomial/interaction features | `degree`, `interaction_only`, `include_bias` | preprocessing/_polynomial.py:L92 |
| `SplineTransformer` | B-spline basis functions | `n_knots`, `degree`, `knots`, `extrapolation` | preprocessing/_polynomial.py:L586 |
| `KBinsDiscretizer` | Bin continuous data into intervals | `n_bins`, `encode`, `strategy` ('uniform', 'quantile', 'kmeans') | preprocessing/_discretization.py:L24 |
| `FunctionTransformer` | Apply arbitrary function as transform | `func`, `inverse_func`, `check_inverse` | preprocessing/_function_transformer.py:L30 |
| `Binarizer` | Threshold numerical data to binary | `threshold` | preprocessing/_data.py:L2295 |

### Standalone Functions

| Function | Purpose | covariance/_elliptic_envelope.py:L187 |
|----------|---------|
| `scale` | Standardize (equiv. `StandardScaler`) | preprocessing/_data.py:L146 |
| `minmax_scale` | Min-max scale (equiv. `MinMaxScaler`) | preprocessing/_data.py:L631 |
| `maxabs_scale` | Max-abs scale (equiv. `MaxAbsScaler`) | preprocessing/_data.py:L1458 |
| `robust_scale` | Robust scale (equiv. `RobustScaler`) | preprocessing/_data.py:L1831 |
| `normalize` | Row-wise normalize (equiv. `Normalizer`) | preprocessing/_data.py:L1978 |
| `binarize` | Threshold binarize (equiv. `Binarizer`) | preprocessing/_data.py:L2236 |
| `label_binarize` | One-vs-all binary encoding | preprocessing/_label.py:L474 |
| `add_dummy_feature` | Add constant bias column | preprocessing/_data.py:L2612 |
| `power_transform` | Box-Cox / Yeo-Johnson (equiv. `PowerTransformer`) | preprocessing/_data.py:L3659 |
| `quantile_transform` | Quantile transform (equiv. `QuantileTransformer`) | preprocessing/_data.py:L3113 |

## Common Patterns

```python
# Impute missing quotes, robust-scale fat-tailed returns, then regress
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (KBinsDiscretizer, PolynomialFeatures,
                                   RobustScaler, StandardScaler)

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 4))
X_clean = X.copy()
X[rng.uniform(size=X.shape) < 0.05] = np.nan  # missing data points
y = X_clean[:, 0] + rng.normal(scale=0.3, size=400)

pipe = Pipeline([("imp", SimpleImputer(strategy="median")),
                 ("scale", RobustScaler()),
                 ("ridge", Ridge(alpha=1.0))])
pipe.fit(X, y)
print(pipe.score(X, y))

# Polynomial interactions for momentum/vol cross-terms
clean = SimpleImputer(strategy="median").fit_transform(X)
X_poly = PolynomialFeatures(degree=2, include_bias=False).fit_transform(clean)
print(X_poly.shape)

# Quantile bins as regime labels for a classifier target
disc = KBinsDiscretizer(n_bins=5, encode="ordinal", strategy="quantile")
labels = disc.fit_transform(clean[:, :1].reshape(-1, 1)).ravel()
print(np.unique(labels, return_counts=True))

# StandardScaler for mean/variance-sensitive models
std = StandardScaler().fit(clean)
print(std.mean_, std.scale_)
```

## Pitfalls
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

## Provenance

- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `OneHotEncoder` (99), `PowerTransformer` (25), `QuantileTransformer` (24) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
