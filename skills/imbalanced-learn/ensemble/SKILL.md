---
name: imbalanced-learn-ensemble
description: "Use when training balanced ensembles with imblearn \u2014 BalancedBaggingClassifier,\
  \ BalancedRandomForestClassifier, EasyEnsembleClassifier, RUSBoostClassifier, and\
  \ the imbalanced metrics (geometric mean, imbalanced report)."
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
- ensemble
- balanced-bagging
- balanced-forest
- metrics
related_skills:
- imbalanced-learn
- imbalanced-learn-samplers
- imbalanced-learn-pipeline
- scikit-learn-ensemble
- scikit-learn-metrics
target_version: 0.14.2 (released tag 0.14.2)
upstream_status: current
---

# imblearn.ensemble

Balanced ensemble estimators: each base learner trains on a balanced bootstrap of the
data, so no explicit sampler is needed. Pair with imbalanced-aware metrics.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `BalancedBaggingClassifier` | `ensemble/_bagging.py:L29` | Bagging with per-iteration balanced bootstrap |
| `BalancedRandomForestClassifier` | `ensemble/_forest.py:L92` | Random forest with balanced bootstrap sampling per tree |
| `EasyEnsembleClassifier` | `ensemble/_easy_ensemble.py:L34` | Boosted set of balanced sub-ensembles |
| `RUSBoostClassifier` | `ensemble/_weight_boosting.py:L30` | Random-under-sampling + AdaBoost combination |
| `BalancedBatchGenerator` | `keras/_generator.py:L64` | Keras batch generator yielding balanced batches |

## Common Patterns

- **Balanced forest**: 
  ```python
  from imblearn.ensemble import BalancedRandomForestClassifier
  clf = BalancedRandomForestClassifier(n_estimators=200, random_state=42).fit(X, y)
  ```
- **Bagging wrapper**: `BalancedBaggingClassifier(estimator=AnySklearnEstimator())` —
  balance any base model without touching the pipeline.
- **Imbalanced metrics**: 
  ```python
  from imblearn.metrics import geometric_mean_score, classification_report_imbalanced
  gmean = geometric_mean_score(y, y_pred)   # sqrt(sens × spec)
  ```
- **Quant application**: minority class = rare event (default, jump, crash) —
  balanced ensembles + g-mean are the standard guard against the always-majority
  baseline.

## Pitfalls

- **G-mean vs accuracy**: accuracy on imbalanced data is meaningless — report
  geometric mean / balanced accuracy / recall-per-class.
- **Class distribution drift**: balanced training assumes the minority is
  under-represented because it's rare, not because of label noise — clean labels first.
- **Estimator API**: pass the base estimator without fitting; the ensemble fits
  balanced copies internally.
- **Keras generator**: `BalancedBatchGenerator` needs an already-balanced batch flow —
  verify the keras version supports the generator contract.

## Provenance

Graph: `knowledge_graphs/imbalanced-learn/.graphify/graph.json` — 611 nodes · 865 edges ·
41 communities · graphify @ 8504e95f0160, backend opencode, description coverage 84.6%.

## Verification Checklist

- [ ] `BalancedRandomForestClassifier(...).fit(X, y)` trains on imbalanced data
- [ ] `geometric_mean_score(y, y_pred)` computed for a small eval
- [ ] QR rows cite `ensemble/*.py` + `metrics/*.py` files resolvable in the imbalanced-learn graph
