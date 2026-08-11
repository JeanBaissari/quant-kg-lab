---
name: optuna
description: "Use when working with Optuna hyperparameter optimization framework. Covers samplers, pruners, study lifecycle, trial parameter suggestion, visualization, integrations, and distributions. Load sub-skills for domain-specific detail."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: optuna/optuna
source_commit: b6f2ea62fbe7fb09d0d1c75783c65dad098d9a06
extraction_date: 2026-07-29
graph:
  nodes: 2318
  edges: 4252
  community_count: 226
  graph_hash: a4c296debfeefdef
tags: [optuna, hyperparameter-optimization, bayesian-optimization, HPO, automated-machine-learning]
related_skills: [optuna-samplers, optuna-pruners, optuna-study, optuna-trial, optuna-visualization, optuna-integration, optuna-distributions]
---

# Optuna Knowledge Graph Extraction

Extracted from the full Optuna codebase (381 Python files, 3,912 nodes, 228 communities).

## Module Skills

This top-level skill indexes seven spec-driven sub-skills covering each major Optuna module:

| Skill | Module | Coverage |
|-------|--------|----------|
| [optuna-samplers](samplers/SKILL.md) | `optuna.samplers` | TPESampler, RandomSampler, GridSampler, CmaEsSampler, NSGAIISampler, QMCSampler, BruteForceSampler, GPSampler |
| [optuna-pruners](pruners/SKILL.md) | `optuna.pruners` | MedianPruner, PercentilePruner, SuccessiveHalvingPruner, HyperbandPruner, ThresholdPruner, PatientPruner, WilcoxonPruner |
| [optuna-study](study/SKILL.md) | `optuna.study` | create_study, Study.optimize, Study.ask, Study.tell, load_study, delete_study |
| [optuna-trial](trial/SKILL.md) | `optuna.trial` | Trial.suggest_float, suggest_int, suggest_categorical, should_prune, report |
| [optuna-visualization](visualization/SKILL.md) | `optuna.visualization` | plot_optimization_history, plot_slice, plot_contour, plot_param_importances, plot_edf, plot_parallel_coordinate |
| [optuna-integration](integration/SKILL.md) | `optuna.integration` | PyTorch, TensorFlow, XGBoost, LightGBM, CatBoost, MLflow, W&B, FastAI, scikit-learn |
| [optuna-distributions](distributions/SKILL.md) | `optuna.distributions` | FloatDistribution, IntDistribution, CategoricalDistribution, BaseDistribution |

## Graph Overview

- **3,912 nodes** across 381 Python source files
- **228 communities** detected via graph clustering
- **1,437 node descriptions** generated and merged into graph.json
- **7 module skills** extracted following agentskills.io template specification

## Key God Nodes (by connection degree)

| Node | Description |
|------|-------------|
| `Study` | A study corresponds to an optimization task, i.e., a set of trials |
| `BaseDistribution` | Base class for distributions used internally by Trial and samplers |
| `optuna.trial` | Module providing parameter suggestion and pruning interface |
| `optuna.study` | Module providing study lifecycle management |
| `optuna.samplers` | Module providing sampling algorithms for parameter suggestion |

## Knowledge Graph

Located at: `knowledge_graphs/optuna/.graphify/graph.json`

Query the graph:
```bash
cd knowledge_graphs/optuna
graphify query "How does TPESampler work?" --graph .graphify/graph.json
graphify explain "Study" --graph .graphify/graph.json
```
