# Edge Audit — catboost

**Date**: 2026-08-13

## Summary

- Total edges: 1569
- EXTRACTED: 1256 (80.1%)
- INFERRED: 313 (19.9%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `BuiltinMetric`: 115 inferred edges
- `OfflineMetricVisualizer`: 115 inferred edges
- `Pool`: 14 inferred edges
- `FactorUtils`: 9 inferred edges
- `FoldModelsHandler`: 9 inferred edges
- `ExecutionCase`: 8 inferred edges
- `FoldStorage`: 8 inferred edges
- `EvaluationResults`: 7 inferred edges
- `MetricEvaluationResult`: 7 inferred edges
- `LabelMode`: 7 inferred edges
- `CatboostEvaluation`: 6 inferred edges
- `EvalType`: 6 inferred edges
- `This method calculate metrics and return them.          Args:             :param`: 6 inferred edges
- `Type of feature evaluation:             All: All factors presented             S`: 6 inferred edges
- `Evaluate features.             Args:             learn_config: dict with params`: 6 inferred edges
- `More flexible evaluation of any cases.             Args:             baseline_ca`: 6 inferred edges
- `Args:             :param path_to_dataset: (str) Path to the dataset to be used f`: 6 inferred edges
- `CaseEvaluationResult`: 5 inferred edges
- `FoldModel`: 5 inferred edges
- `MetricsPlotter`: 5 inferred edges

## Cross-Module Suspicious Edges

- `core.py` ↔ `metrics.py`: 115
- `core.py` ↔ `plot_helpers.py`: 115
- `catboost_evaluation.py` ↔ `evaluation_result.py`: 14
- `catboost_evaluation.py` ↔ `factor_utils.py`: 14
- `utils.py` ↔ `core.py`: 12
- `_splitter.py` ↔ `_fold_storage.py`: 8
- `catboost_evaluation.py` ↔ `execution_case.py`: 7
- `catboost_evaluation.py` ↔ `_fold_models_handler.py`: 7
- `_fold_models_handler.py` ↔ `evaluation_result.py`: 5
- `_fold_models_handler.py` ↔ `_fold_model.py`: 5
- `metrics_plotter.py` ↔ `ipythonwidget.py`: 5
- `callbacks.py` ↔ `metrics_plotter.py`: 4
- `execution_case.py` ↔ `factor_utils.py`: 2
