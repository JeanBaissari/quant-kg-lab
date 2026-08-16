---
name: catboost-evaluation
description: "Use when cross-validating or evaluating catboost models \u2014 cv()\
  \ fold training, CatboostEvaluation model comparison, metric evaluation results,\
  \ and fold handling."
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
  graph_hash: 59f3c1631da37620
tags:
- catboost
- cross-validation
- evaluation
- metrics
related_skills:
- catboost
- catboost-core
- catboost-pool
- scikit-learn-model-selection
- optuna-study
target_version: '1.2.10 (dev: after 1.2.10)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `catboost` ahead of the latest PyPI release (1.2.10 (dev: after 1.2.10)). Some APIs may not exist in your installed version.

# catboost.evaluation

Cross-validation and evaluation: `cv()` trains per-fold models and returns metric
scores, `CatboostEvaluation` compares model families on split data, and the
`eval/` machinery (fold handlers, metric evaluation results) backs both.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `cv()` | `core.py:L7063` | Cross-validated training — fold_count, partition_random_seed, early stopping |
| `CatboostEvaluation` | `eval/catboost_evaluation.py:L30` | Model-comparison runner on train/test splits |
| `MetricEvaluationResult` | `eval/evaluation_result.py:L248` | Per-fold metric outcome — deg 24 hub |
| `CaseEvaluationResult` | `eval/evaluation_result.py:L84` | Per-case metric result |
| `FoldModelsHandler` | `eval/_fold_models_handler.py:L13` | Fold model bookkeeping |
| `FoldStorage` | `eval/_fold_storage.py:L16` | Fold data storage |
| `ExecutionCase` | `eval/execution_case.py:L8` | Evaluation case descriptor (model + split) |
| `FactorUtils` | `eval/factor_utils.py:L9` | Utility helpers for factor evaluation |
| `BuiltinMetric` | `metrics.py:L25` | Built-in metric enum (deg 123 hub) |

## Common Patterns

- **Cross-validation**:
  ```python
  from catboost import cv, Pool
  results = cv(Pool(X, y, cat_features=[2]), {'iterations': 500, 'loss_function': 'Logloss'},
               fold_count=5, partition_random_seed=42)
  # results: mean/std of the eval metric per iteration
  ```
- **Metric parity**: pass the SAME `eval_metric` to cv and the final fit so the
  reported numbers are comparable.
- **Model comparison**: `CatboostEvaluation` — head-to-head model families on the
  same folds, with per-case metric results.
- **Early stopping in cv**: `early_stopping_rounds` applies per fold — watch the
  averaged best-iteration for the final fit.

## Pitfalls

- **cv vs fit metrics**: cv averages per-fold; the final model's metric on the full
  train differs — report both, never swap.
- **Random seed**: `partition_random_seed` must be fixed for reproducible folds.
- **Fold cost**: `fold_count` × iterations — budget the wall-clock before large sweeps
  (optuna adds its own trials on top).
- **Metric enum**: `BuiltinMetric` names are exact — a typo silently falls back or
  raises late; validate the metric string first.

## Provenance

Graph: `knowledge_graphs/catboost/.graphify/graph.json` — 793 nodes · 1569 edges ·
38 communities · graphify @ 549af60ecd40, backend opencode, description coverage 87.5%.

## Verification Checklist

- [ ] `cv(Pool(...), params, fold_count=3)` returns per-iteration metric stats
- [ ] `CatboostEvaluation(...)` runs a head-to-head comparison
- [ ] QR rows cite `core.py:L1`/`eval/*.py`/`metrics.py:L1` files resolvable in the catboost graph
