---
name: catboost-pool
description: "Use when building catboost data containers — Pool with cat_features/text_features/group_id/pairs, and the from_dataframe/from_numpy constructors."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: catboost/catboost
source_commit: 549af60ecd40819be138046cd9c5ec737dca5e3b
extraction_date: 2026-08-13
graph:
  nodes: 793
  edges: 1569
  community_count: 38
  graph_hash: 59f3c1631da37620
tags:
- catboost
- pool
- data-container
related_skills:
- catboost
- catboost-core
- catboost-evaluation
- pandas-core
- numpy-core
---

# catboost.pool

The `Pool` data container: X/y with native categorical/text/embedding feature
declarations, group/pair metadata for ranking, and the DataFrame/numpy constructors.
Every fit/cv call consumes a Pool (or converts automatically).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Pool` | `core.py:L603` | The data container — deg 68 hub |
| `Pool.__init__()` | `core.py:L608` | Constructor — X/y, cat_features, group_id, pairs, weight |
| `Pool.is_fitted()` | `core.py:L1840` | Whether the Pool has been built/validated |
| `CatBoost` | `core.py:L2563` | Models consume Pool or raw arrays |

## Common Patterns

- **Explicit Pool**:
  ```python
  from catboost import Pool
  train_pool = Pool(X_train, y_train, cat_features=[2, 5], group_id=groups)
  model.fit(train_pool)
  ```
- **Categorical declaration**: `cat_features` as integer column indices (or names when
  X is a DataFrame).
- **Ranking metadata**: `group_id` (query ids) + optional `pairs` for pairwise losses.
- **Sample weights**: `weight=` per-row — the standard class-weight/importance path.
- **Reuse**: build the Pool once and pass it to fit/cv — avoids repeated conversion.

## Pitfalls

- **Column drift**: after any DataFrame slice, `cat_features` indices must be re-checked
  — a dropped column shifts them silently.
- **String categories**: unlisted categorical columns are auto-detected only in some
  constructors — declare them explicitly.
- **group_id alignment**: group ids must be sorted/contiguous per query for ranking
  losses — catboost validates this at fit time.

## Provenance

Graph: `knowledge_graphs/catboost/.graphify/graph.json` — 793 nodes · 1569 edges ·
38 communities · graphify @ 549af60ecd40, backend opencode, description coverage 87.5%.

## Verification Checklist

- [ ] `Pool(X, y, cat_features=[...])` builds without error
- [ ] `model.fit(Pool)` uses the declared categoricals
- [ ] QR rows cite `core.py` files resolvable in the catboost graph
