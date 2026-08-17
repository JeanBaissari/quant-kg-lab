---
name: catboost
description: "Use when working with catboost \u2014 the boosting entry point. Router\
  \ indexing the catboost sub-skills; load the sub-skill for the layer you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: catboost/catboost
source_commit: 549af60ecd40819be138046cd9c5ec737dca5e3b
extraction_date: 2026-08-13
graph:
  nodes: 793
  edges: 1569
  community_count: 52
  graph_hash: f926c24c431eefad
tags:
- catboost
- router
- boosting
related_skills:
- catboost-core
- catboost-pool
- catboost-evaluation
- xgboost
- lightgbm
- scikit-learn
- optuna
- shap
target_version: '1.2.10 (dev: after 1.2.10)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `catboost` ahead of the latest PyPI release (1.2.10 (dev: after 1.2.10)). Some APIs may not exist in your installed version.

# catboost

Gradient boosting with **native categorical-feature handling** (`cat_features`,
text/embedding features, missing-value-native) — the categorical-boosting layer over
the sklearn-compatible stack, with native SHAP interop.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [core](core/SKILL.md) | CatBoostClassifier/Regressor/Ranker, loss functions, eval metrics, save/load |
| [pool](pool/SKILL.md) | Pool data container — cat_features, group_id, pairs |
| [evaluation](evaluation/SKILL.md) | cv() cross-validation, CatboostEvaluation, metric evaluation |

## Common Patterns

- **Categorical data**: `CatBoostClassifier(cat_features=[2, 5])` — no manual encoding;
  ordered boosting handles categories natively.
- **Optuna integration**: `OptunaCatBoost` (see optuna-integration skill) — native
  categorical + HPO.
- **Explainability**: `get_feature_importance(type=PredictionValuesChange)` or the
  native SHAP interop (shap TreeExplainer works directly).

## Provenance

Graph: `knowledge_graphs/catboost/.graphify/graph.json` — 793 nodes · 1569 edges ·
38 communities · graphify @ 549af60ecd40, backend opencode, description coverage 87.5%.

## Verification Checklist

- [ ] Router links resolve to the 3 module skills
- [ ] `related_skills` names resolve to real skills
