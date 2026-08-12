---
name: scikit-learn
description: Use when working with scikit-learn. Router indexing the 14 scikit-learn
  sub-skills; load the sub-skill for the module you need.
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
related_skills:
- scikit-learn-cluster
- scikit-learn-compose
- scikit-learn-decomposition
- scikit-learn-ensemble
- scikit-learn-feature-selection
- scikit-learn-gaussian-process
- scikit-learn-impute
- scikit-learn-linear-model
- scikit-learn-metrics
- scikit-learn-model-selection
- scikit-learn-neural-network
- scikit-learn-preprocessing
- scikit-learn-svm
- scikit-learn-tree
---

# scikit-learn (router)

Indexes the 14 spec-driven scikit-learn sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [scikit-learn-cluster](cluster/SKILL.md) | `sklearn.cluster` | scikit-learn Clustering |
| [scikit-learn-compose](compose/SKILL.md) | `sklearn.compose` | composite estimators and pipelines in scikit-learn |
| [scikit-learn-decomposition](decomposition/SKILL.md) | `sklearn.decomposition` | scikit-learn matrix decomposition and dimensionality reduction |
| [scikit-learn-ensemble](ensemble/SKILL.md) | `sklearn.ensemble` | scikit-learn Ensemble methods |
| [scikit-learn-feature-selection](feature_selection/SKILL.md) | `sklearn.feature_selection` | scikit-learn feature selection |
| [scikit-learn-gaussian-process](gaussian_process/SKILL.md) | `sklearn.gaussian_process` | scikit-learn Gaussian Processes |
| [scikit-learn-impute](impute/SKILL.md) | `sklearn.impute` | scikit-learn Imputation |
| [scikit-learn-linear-model](linear_model/SKILL.md) | `sklearn.linear_model` | scikit-learn linear models |
| [scikit-learn-metrics](metrics/SKILL.md) | `sklearn.metrics` | scikit-learn metrics, scoring functions, pairwise distances, or clustering evaluation |
| [scikit-learn-model-selection](model_selection/SKILL.md) | `sklearn.model_selection` | scikit-learn model selection, cross-validation, hyperparameter tuning, or GridSearchCV/RandomizedSearchCV workflows |
| [scikit-learn-neural-network](neural_network/SKILL.md) | `sklearn.neural_network` | scikit-learn Neural Networks |
| [scikit-learn-preprocessing](preprocessing/SKILL.md) | `sklearn.preprocessing` | scikit-learn data preprocessing, scaling, encoding, discretization, or feature transformations |
| [scikit-learn-svm](svm/SKILL.md) | `sklearn.svm` | scikit-learn SVMs |
| [scikit-learn-tree](tree/SKILL.md) | `sklearn.tree` | scikit-learn Decision Trees |

## Provenance
- Knowledge graph: scikit-learn, 8662 nodes, 29241 edges, 401 communities
- Rebuild: `scripts/rebuild_graph.sh scikit-learn` (pinned commit 6f8b95aa2234)
