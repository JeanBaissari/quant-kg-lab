---
name: imbalanced-learn-samplers
description: "Use when resampling imbalanced data with imblearn \u2014 SMOTE/ADASYN/BorderlineSMOTE\
  \ oversampling, NearMiss/RandomUnderSampler/ENN undersampling, SMOTENC/SMOTEN categorical\
  \ variants, and combined SMOTEENN/SMOTETomek."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn-contrib/imbalanced-learn
source_commit: 8504e95f0160f61d1b617ca66f779646d2ee609e
extraction_date: 2026-08-13
graph:
  nodes: 611
  edges: 865
  community_count: 43
  graph_hash: 1f3d925de8211eee
tags:
- imbalanced-learn
- smote
- oversampling
- undersampling
- samplers
related_skills:
- imbalanced-learn
- imbalanced-learn-ensemble
- imbalanced-learn-pipeline
- scikit-learn-ensemble
- pandas-core
target_version: 0.14.2 (released tag 0.14.2)
upstream_status: current
---

# imblearn.samplers

Resampling algorithms: `fit_resample(X, y)` returns augmented arrays. Oversampling
synthesizes minority samples (SMOTE family); undersampling selects majority prototypes
(NearMiss/ENN); combined strategies chain both.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `BaseSampler` | `base.py:L145` | Sampler base — fit_resample contract, sampling_strategy handling |
| `SamplerMixin` | `base.py:L36` | Mixin exposing `fit_resample`/`resample` |
| `FunctionSampler` | `base.py:L255` | Wrap an arbitrary callable as a sampler |
| `SMOTE` | `over_sampling/_smote/base.py:L242` | Synthetic minority oversampling via k-NN interpolation |
| `BaseSMOTE` | `over_sampling/_smote/base.py:L40` | SMOTE machinery base (k_neighbors, m_neighbors) |
| `SMOTENC` | `over_sampling/_smote/base.py:L381` | SMOTE with categorical features (categorical_features arg) |
| `SMOTEN` | `over_sampling/_smote/base.py:L786` | SMOTE for all-categorical data |
| `KMeansSMOTE` | `over_sampling/_smote/cluster.py:L30` | Cluster-then-SMOTE — synthetic points per cluster |
| `ADASYN` | `over_sampling/_adasyn.py:L23` | Adaptive synthetic sampling — weights by density |
| `RandomOverSampler` | `over_sampling/_random_over_sampler.py:L27` | Duplicate minority rows to target ratio |
| `RandomUnderSampler` | `under_sampling/_prototype_selection/_random_under_sampler.py:L21` | Random majority drop |
| `NearMiss` | `under_sampling/_prototype_selection/_nearmiss.py:L24` | Majority prototypes nearest to minorities (v1/v2/v3) |
| `EditedNearestNeighbours` | `under_sampling/_prototype_selection/_edited_nearest_neighbours.py:L28` | Drop majority samples misclassified by k-NN |
| `RepeatedEditedNearestNeighbours` | `under_sampling/_prototype_selection/_edited_nearest_neighbours.py:L205` | Iterated ENN until stable |
| `AllKNN` | `under_sampling/_prototype_selection/_edited_nearest_neighbours.py:L431` | ENN with growing k per pass |
| `TomekLinks` | `under_sampling/_prototype_selection/_tomek_links.py:L23` | Remove majority side of Tomek links (border points) |
| `OneSidedSelection` | `under_sampling/_prototype_selection/_one_sided_selection.py:L27` | ENN + Tomek combo selection |
| `CondensedNearestNeighbour` | `under_sampling/_prototype_selection/_condensed_nearest_neighbour.py:L28` | Minimal consistent majority subset |
| `NeighbourhoodCleaningRule` | `under_sampling/_prototype_selection/_neighbourhood_cleaning_rule.py:L30` | ENN + NCR hybrid cleaning |
| `InstanceHardnessThreshold` | `under_sampling/_prototype_selection/_instance_hardness_threshold.py:L30` | Drop easy-classified majority via a classifier |
| `ClusterCentroids` | `under_sampling/_prototype_generation/_cluster_centroids.py:L28` | K-means centroids as majority prototypes |
| `SMOTEENN` | `combine/_smote_enn.py:L25` | SMOTE then ENN cleaning |
| `SMOTETomek` | `combine/_smote_tomek.py:L26` | SMOTE then Tomek-link cleaning |
| `InputTags` | `utils/_tags.py:L20` | Tag schema for sampler input validation |
| `ArraysTransformer` | `utils/_validation.py:L32` | Input validation/conversion helper |

## Common Patterns

- **Standard SMOTE**:
  ```python
  from imblearn.over_sampling import SMOTE
  Xr, yr = SMOTE(random_state=42).fit_resample(X, y)
  ```
- **Categorical data**: `SMOTENC(categorical_features=[2, 5])` — never plain SMOTE on
  one-hot/categorical columns (it interpolates meaningless values).
- **Ratio control**: `sampling_strategy=0.5` (minority:majority ratio) or a dict
  `{class: n_samples}`.
- **Border cases**: `ADASYN` (density-weighted) or `BorderlineSMOTE` for noisy borders;
  `KMeansSMOTE` when clusters are well separated.
- **Cleaning after synthesis**: `SMOTEENN`/`SMOTETomek` — synthesize then remove
  borderline junk; standard for noisy datasets.
- **No-synthesis alternative**: `NearMiss`/`TomekLinks` when synthetic samples could
  leak (e.g. time-ordered data).
- **Pipeline placement**: samplers go between preprocessing and the estimator
  (`imblearn.pipeline` handles this correctly — see the pipeline skill).

## Pitfalls

- **Time-series leakage**: SMOTE interpolates between neighbors — on temporal data it
  fabricates look-ahead samples. Use undersampling or time-aware strategies.
- **Overlapping classes**: SMOTE on heavily overlapping classes adds noise — clean
  with ENN/Tomek first (SMOTEENN).
- **k_neighbors > class size**: SMOTE raises if the minority class has fewer samples
  than k+1 — reduce k or use random oversampling first.
- **One-hot interpolation**: plain SMOTE on one-hot columns creates fractional
  categories — use SMOTENC with the raw categorical columns.
- **validation**: always cross-validate after resampling INSIDE the fold — resampling
  the full dataset before splitting leaks the validation set.

## Provenance

Graph: `knowledge_graphs/imbalanced-learn/.graphify/graph.json` — 611 nodes · 865 edges ·
41 communities · graphify @ 8504e95f0160, backend opencode, description coverage 84.6%.

## Verification Checklist

- [ ] `SMOTE().fit_resample(X, y)` returns balanced arrays
- [ ] `SMOTENC(categorical_features=...)` runs on mixed data
- [ ] QR rows cite `over_sampling/**`/`under_sampling/**`/`combine/**` files resolvable in the imbalanced-learn graph
