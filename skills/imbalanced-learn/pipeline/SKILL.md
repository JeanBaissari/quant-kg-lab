---
name: imbalanced-learn-pipeline
description: "Use when building sampling-aware pipelines with imblearn \u2014 Pipeline/make_pipeline\
  \ that hold samplers between transformers and estimators, and the imbalanced scoring/metrics\
  \ surface."
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
  graph_hash: f6c2a46427904f14
tags:
- imbalanced-learn
- pipeline
- sampling
- cross-validation
related_skills:
- imbalanced-learn
- imbalanced-learn-samplers
- imbalanced-learn-ensemble
- scikit-learn-compose
- scikit-learn-model-selection
---

# imblearn.pipeline

The sampling-aware `Pipeline`: unlike sklearn's, it lets a sampler sit between a
transformer and an estimator — sampling happens inside the fold, not before the split
(the anti-leakage requirement for imbalanced workflows).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Pipeline` | `pipeline.py:L111` | Sampling-aware step chain — samplers valid between transformers/estimators |
| `.fit_transform()` | `pipeline.py:L537` | Fit + transform through the chain |
| `.transform()` | `pipeline.py:L999` | Transform stage outputs (post-sampler) |
| `.fit()` | `pipeline.py:L111` | Fit all steps (with internal resampling in the right position) |
| `InputTags` | `utils/_tags.py:L20` | Tags: which steps accept what data |
| `SamplerTags` | `utils/_tags.py:L82` | Sampler capability tags |
| `InstanceHardnessCV` | `model_selection/_split.py:L11` | Hardness-based cross-validation splitter |

## Common Patterns

- **The canonical imbalanced pipeline**:
  ```python
  from imblearn.pipeline import make_pipeline
  from imblearn.over_sampling import SMOTE
  from sklearn.preprocessing import StandardScaler
  from sklearn.ensemble import RandomForestClassifier

  pipe = make_pipeline(StandardScaler(), SMOTE(), RandomForestClassifier())
  ```
- **Cross-validation**: use `cross_val_score(pipe, X, y, scoring="balanced_accuracy")` —
  sampling happens per-fold inside the pipeline, so the validation set is never
  resampled.
- **GridSearch**: `GridSearchCV(pipe, {"smote__k_neighbors": [3, 5]})` — sampler
  hyperparameters via the `step__param` convention.
- **Custom scoring**: `make_scorer(geometric_mean_score)` for imbalanced-aware tuning.

## Pitfalls

- **NEVER resample before the split**: `SMOTE().fit_resample(X_full, y_full)` then
  `train_test_split` leaks — the whole point of `imblearn.pipeline` is resampling
  inside each fold.
- **sklearn Pipeline import**: importing `Pipeline` from `sklearn.pipeline` silently
  drops the sampler step — always import from `imblearn.pipeline`.
- **Step naming**: samplers are addressable as `step__param`; a sampler named "smote"
  exposes `smote__k_neighbors`.
- **Transform after sampler**: `.transform()` on the pipeline output is post-sampling
  shape — expect augmented row counts at intermediate steps.

## Provenance

Graph: `knowledge_graphs/imbalanced-learn/.graphify/graph.json` — 611 nodes · 865 edges ·
41 communities · graphify @ 8504e95f0160, backend opencode, description coverage 84.6%.

## Verification Checklist

- [ ] `make_pipeline(StandardScaler(), SMOTE(), RandomForestClassifier())` fits + scores
- [ ] `cross_val_score(pipe, X, y)` runs without resampling leakage
- [ ] QR rows cite `pipeline.py:L1`/`model_selection/_split.py:L1` resolvable in the imbalanced-learn graph
