---
name: imbalanced-learn
description: "Use when working with imbalanced-learn \u2014 the class-imbalance entry\
  \ point. Router indexing the imblearn sub-skills; load the sub-skill for the resampling\
  \ layer you need."
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
- router
- imblearn
- resampling
related_skills:
- imbalanced-learn-samplers
- imbalanced-learn-ensemble
- imbalanced-learn-pipeline
- scikit-learn-ensemble
- scikit-learn-model-selection
target_version: 0.14.2 (released tag 0.14.2)
upstream_status: current
---

# imbalanced-learn

scikit-learn-compatible toolkit for imbalanced classification: synthetic oversampling
(SMOTE family), prototype selection (NearMiss/ENN), combined strategies (SMOTEENN), and
balanced ensembles — the resampling layer over the sklearn stack.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [samplers](samplers/SKILL.md) | SMOTE/ADASYN/random over+under/NearMiss/ENN/TomekLinks/SMOTENC/SMOTEN — resampling algorithms |
| [ensemble](ensemble/SKILL.md) | BalancedBagging/RandomForest, EasyEnsemble, RUSBoost — balanced estimators |
| [pipeline](pipeline/SKILL.md) | Pipeline/make_pipeline — sampling-aware step chains, metrics |

## Common Patterns

- **Sampling in a pipeline**: `imblearn.pipeline.make_pipeline(StandardScaler(), SMOTE(), classifier)`.
- **Balanced ensemble**: `BalancedRandomForestClassifier(n_estimators=100)` — no explicit
  sampler needed.
- **Imbalanced metrics**: `geometric_mean_score`, `classification_report_imbalanced` —
  accuracy hides minority-class failure.

## Provenance

Graph: `knowledge_graphs/imbalanced-learn/.graphify/graph.json` — 611 nodes · 865 edges ·
41 communities · graphify @ 8504e95f0160, backend opencode, description coverage 84.6%.

## Verification Checklist

- [ ] Router links resolve to the 3 module skills
- [ ] `related_skills` names resolve to real skills
