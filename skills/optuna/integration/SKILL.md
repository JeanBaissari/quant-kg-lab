---
name: optuna-integration
description: "Use when working with Optuna integration modules \u2014 PyTorch, TensorFlow,\
  \ XGBoost, LightGBM, CatBoost, MLflow, Weights & Biases, FastAI, scikit-learn, Keras.\
  \ Covers pruning callbacks, automated tuning, and experiment tracking."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: optuna/optuna
source_commit: b6f2ea62fbe7fb09d0d1c75783c65dad098d9a06
extraction_date: 2026-07-29
graph:
  nodes: 2208
  edges: 4013
  community_count: 226
  graph_hash: f183610fc15fb948
tags:
- optuna
- hyperparameter-optimization
- integration
related_skills:
- optuna-samplers
- optuna-pruners
- optuna-study
- optuna-trial
- optuna-visualization
- optuna-integration
- optuna-distributions
---

# Optuna Integration

Extracted from optuna knowledge graph. Source: `optuna.integration` module.

## Quick Reference
| Integration | Key Classes | Purpose | Graph Node |
|-------------|-------------|---------|-----------|
| **LightGBM** | `LightGBMPruningCallback`, `LightGBMTuner`, `LightGBMTunerCV` | Automated LightGBM tuning with step-wise algorithm | — |
| **XGBoost** | `XGBoostPruningCallback` | Pruning callback for XGBoost training | — |
| **CatBoost** | `CatBoostPruningCallback` | Pruning callback for CatBoost training | — |
| **PyTorch Lightning** | `PyTorchLightningPruningCallback` | Pruning callback for PyTorch Lightning Trainer | — |
| **PyTorch Ignite** | `PyTorchIgnitePruningHandler` | Pruning handler for PyTorch Ignite | — |
| **PyTorch Distributed** | `TorchDistributedTrial` | Synchronized trials across distributed nodes | — |
| **TensorFlow** | `TensorFlowPruningHook` | Pruning hook for TensorFlow Estimator | — |
| **TF Keras** | `TFKerasPruningCallback` | Pruning callback for TensorFlow Keras | — |
| **FastAI** | `FastAIPruningCallback`, `FastAIV2PruningCallback` | Pruning callbacks for FastAI v1 and v2 | — |
| **scikit-learn** | `OptunaSearchCV` | GridSearchCV-compatible hyperparameter search | — |
| **MLflow** | `MLflowCallback` | Log trials to MLflow tracking server | — |
| **Weights & Biases** | `WeightsAndBiasesCallback` | Log trials to W&B dashboard | — |
| **Dask** | `DaskStorage` | Distributed storage backend for Dask | — |
| **SHAP** | `ShapleyImportanceEvaluator` | SHAP-based parameter importance | — |

> Note: The optuna.integration classes (LightGBMPruningCallback, XGBoostPruningCallback, CatBoostPruningCallback, PyTorchLightningPruningCallback, TorchDistributedTrial, OptunaSearchCV, MLflowCallback, WeightsAndBiasesCallback, etc.) exist in the library but are absent from the committed graph (extraction gap).

## Common Patterns

### LightGBM Automated Tuning
```python
import optuna.integration.lightgbm as lgb

# LightGBM handles Optuna internally
params = {
    "objective": "binary",
    "metric": "binary_logloss",
}

model = lgb.train(
    params,
    dtrain,
    valid_sets=[dvalid],
    callbacks=[lgb.LightGBMPruningCallback(trial, "binary_logloss")]
)
```

### PyTorch Lightning with Pruning
```python
from optuna.integration import PyTorchLightningPruningCallback

def objective(trial):
    model = MyLightningModel(trial)
    trainer = pl.Trainer(
        callbacks=[PyTorchLightningPruningCallback(trial, monitor="val_loss")],
        max_epochs=10
    )
    trainer.fit(model)
    return trainer.callback_metrics["val_loss"].item()
```

### scikit-learn Compatible Search
```python
from optuna.integration import OptunaSearchCV
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
optuna_search = OptunaSearchCV(
    model,
    {"n_estimators": optuna.distributions.IntDistribution(50, 300),
     "max_depth": optuna.distributions.IntDistribution(3, 20)},
    cv=5, n_trials=50
)
optuna_search.fit(X_train, y_train)
```

### Experiment Tracking with W&B
```python
from optuna.integration import WeightsAndBiasesCallback

study.optimize(
    objective, n_trials=100,
    callbacks=[WeightsAndBiasesCallback()]
)
```

## Pitfalls

1. **LightGBM integration requires specific import path**: Use `optuna.integration.lightgbm`, not `optuna.integration`.
2. **Integration modules are lazy-loaded**: Each integration raises a clear `ImportError` if its dependency is missing.
3. **OptunaSearchCV distribution format**: Uses `optuna.distributions` classes, not raw ranges like scikit-learn's `GridSearchCV`.
4. **Distributed training**: `TorchDistributedTrial` requires all ranks to call `suggest_*` in the same order.
5. **Callback order**: W&B/MLflow callbacks must be added to `study.optimize(callbacks=...)`, not to the trainer.

## Verification Checklist

- [ ] Required packages installed (lightgbm, xgboost, pytorch_lightning, etc.)
- [ ] Correct import paths used (`optuna.integration.lightgbm` for LightGBM)
- [ ] Pruning callbacks monitor the correct metric name
- [ ] Distributed trials synchronize parameter suggestions across ranks
- [ ] Experiment tracking callbacks configured with correct project/entity

## Provenance

- Knowledge graph: optuna, 2205 nodes, 4010 edges, 226 communities
- God nodes: `_IntegrationModule` (5), `_LightGBMModule` (4), `__init__.py` (2) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ b6f2ea62fbe7, backend opencode, description coverage 85%
