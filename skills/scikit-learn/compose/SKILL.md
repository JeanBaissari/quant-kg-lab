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
  community_count: 401
  graph_hash: fc25a6d284e9a3ed
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
---

# scikit-learn Compose (Composite Estimators)

Extracted from scikit-learn knowledge graph. Source: `sklearn.compose` module and `sklearn.pipeline`.

## Quick Reference
### Core Pipeline & Column Transformers

| Class/Function | Purpose | Key Params | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node |
|---------------|---------|------------|
| `Pipeline` | Chain transforms + estimator sequentially | `steps` (list of (name, transform) tuples), `memory`, `verbose` | pipeline.py:L93 |
| `make_pipeline` | Shorthand Pipeline (auto-names steps) | `*steps` | pipeline.py:L1471 |
| `ColumnTransformer` | Apply different transforms to different columns | `transformers`, `remainder`, `sparse_threshold`, `verbose_feature_names_out` | compose/_column_transformer.py:L64 |
| `make_column_transformer` | Shorthand ColumnTransformer (auto-names) | `*transformers`, `remainder`, `verbose_feature_names_out` | compose/_column_transformer.py:L1312 |
| `make_column_selector` | Select columns by dtype or pattern | `pattern`, `dtype_include`, `dtype_exclude` | compose/_column_transformer.py:L1427 |

### Feature Union

| Class/Function | Purpose | Key Params |
|---------------|---------|------------|
| `FeatureUnion` | Concatenate results of multiple transforms | `transformer_list`, `n_jobs`, `transformer_weights`, `verbose` | pipeline.py:L1626 |
| `make_union` | Shorthand FeatureUnion (auto-names) | `*transformers`, `n_jobs`, `verbose` | pipeline.py:L2234 |

### Target Transformation

| Class | Purpose | Key Params | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|------------|
| `TransformedTargetRegressor` | Transform target y before fitting | `regressor`, `transformer`, `func`, `inverse_func`, `check_inverse` | compose/_target.py:L28 |

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
