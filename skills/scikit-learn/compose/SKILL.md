---
name: scikit-learn-compose
description: "Use when building composite estimators and pipelines in scikit-learn\
  \ \u2014 Pipeline, ColumnTransformer, FeatureUnion, and TransformedTargetRegressor\
  \ for heterogeneous data and multi-step workflows."
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
- pipelines
- composite-estimators
- column-transformer
- feature-union
related_skills:
- scikit-learn-preprocessing
- scikit-learn-model-selection
- scikit-learn-linear-model
target_version: '1.9.0 (dev: after 1.9.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `scikit-learn` ahead of the latest PyPI release (1.9.0 (dev: after 1.9.0)). Some APIs may not exist in your installed version.

# scikit-learn Compose (Composite Estimators)

Extracted from scikit-learn knowledge graph. Source: `sklearn.compose` module and `sklearn.pipeline`.

## Quick Reference
### Core Pipeline & Column Transformers

| Class/Function | Purpose | Graph Node | Key Params |
|---------------|---------|-----------|------------|
| `Pipeline` | Chain transforms + estimator sequentially | pipeline.py:L93 | `steps` (list of (name, transform) tuples), `memory`, `verbose` |
| `make_pipeline` | Shorthand Pipeline (auto-names steps) | pipeline.py:L1471 | `*steps` |
| `ColumnTransformer` | Apply different transforms to different columns | compose/_column_transformer.py:L64 | `transformers`, `remainder`, `sparse_threshold`, `verbose_feature_names_out` |
| `make_column_transformer` | Shorthand ColumnTransformer (auto-names) | compose/_column_transformer.py:L1312 | `*transformers`, `remainder`, `verbose_feature_names_out` |
| `make_column_selector` | Select columns by dtype or pattern | compose/_column_transformer.py:L1427 | `pattern`, `dtype_include`, `dtype_exclude` |

### Feature Union

| Class/Function | Purpose | Graph Node | Key Params |
|---------------|---------|-----------|------------|
| `FeatureUnion` | Concatenate results of multiple transforms | pipeline.py:L1626 | `transformer_list`, `n_jobs`, `transformer_weights`, `verbose` |
| `make_union` | Shorthand FeatureUnion (auto-names) | pipeline.py:L2234 | `*transformers`, `n_jobs`, `verbose` |

### Target Transformation

| Class | Purpose | Key Params | Graph Node |
|-------|---------|------------|-----------|
| `TransformedTargetRegressor` | Transform target y before fitting | `regressor`, `transformer`, `func`, `inverse_func`, `check_inverse` | compose/_target.py:L28 |

## Common Patterns

```python
# Quant feature pipeline: impute + scale momentum/vol, passthrough sector dummies
import numpy as np
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(0)
X = rng.normal(size=(500, 4))
X[rng.uniform(size=X.shape) < 0.05] = np.nan  # missing prints in continuous cols
X[:, 3] = rng.integers(0, 2, size=500).astype(float)  # clean sector dummy (passthrough)
y = 0.5 * np.nan_to_num(X[:, 1]) + rng.normal(scale=0.4, size=500)

prep = ColumnTransformer(
    transformers=[
        ("scale", Pipeline([("imp", SimpleImputer(strategy="median")),
                            ("std", StandardScaler())]), [0, 1, 2]),
        ("sector", "passthrough", [3]),
    ]
)
pipe = Pipeline([("prep", prep), ("ridge", Ridge(alpha=1.0))])
pipe.fit(X, y)
print(pipe.predict(X[:3]))

# TransformedTargetRegressor: log-shift the return target, back-transform
ttr = TransformedTargetRegressor(
    regressor=Ridge(alpha=1.0), func=np.log1p, inverse_func=np.expm1
)
ttr.fit(np.nan_to_num(X), y + 1.0)
print(ttr.predict(np.nan_to_num(X[:3])))
```

## Pitfalls
1. **Pipeline step ordering**: Steps execute in order. Preprocessing must come before the final estimator. `Pipeline([('scaler', StandardScaler()), ('clf', LogisticRegression())])` — the last step must be an estimator (has `fit()` and `predict()`), all prior steps must be transformers (have `fit_transform()`).
2. **`ColumnTransformer` `remainder` default**: `remainder='drop'` — columns not mentioned in any transformer are silently dropped! Set `remainder='passthrough'` to keep them unchanged.
3. **`make_column_transformer` auto-selection**: Unlike `ColumnTransformer`, this automatically selects columns via `make_column_selector`. Use `dtype_include` and `dtype_exclude` to control which columns each transformer processes.
4. **`FeatureUnion` parallel execution**: `n_jobs` parallelizes transformers across CPU cores. Memory usage scales with number of parallel transformers × output size.
5. **`TransformedTargetRegressor` inverse transform**: Automatically applies `inverse_transform()` to predictions. The `transformer` must implement `inverse_transform()`, or provide `func` + `inverse_func` callables.
6. **Sparse output cascading**: `ColumnTransformer` with `sparse_threshold=0.3` (default) densifies if <30% of values are non-zero. Set lower for sparse pipelines.
7. **Pipeline `memory` for caching**: Setting `memory` to a joblib cache path caches intermediate transforms, avoiding recomputation in grid search. Great for expensive preprocessing steps.

## Verification Checklist

- [ ] Pipeline last step is an estimator (not a transformer)
- [ ] `ColumnTransformer` `remainder` behavior explicitly set (not default `'drop'`)
- [ ] All column selectors cover intended feature subsets
- [ ] `FeatureUnion` transformers produce compatible output dimensions
- [ ] `TransformedTargetRegressor` `transformer` implements `inverse_transform`
- [ ] `random_state` propagated through all randomized steps
- [ ] Pipeline used in `GridSearchCV` for no-leak preprocessing

## Provenance

- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `ColumnTransformer` (40), `TransformedTargetRegressor` (20), `.fit_transform()` (12) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
