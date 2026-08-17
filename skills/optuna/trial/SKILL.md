---
name: optuna-trial
description: "Use when working with Optuna Trial parameter suggestion and pruning\
  \ \u2014 Trial.suggest_float, suggest_int, suggest_categorical, suggest_loguniform,\
  \ should_prune, report. Covers parameter space definition, conditional parameters,\
  \ and intermediate value reporting."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: optuna/optuna
source_commit: b6f2ea62fbe7fb09d0d1c75783c65dad098d9a06
extraction_date: 2026-07-29
graph:
  nodes: 2208
  edges: 4013
  community_count: 223
  graph_hash: e89ef51b72ea62be
tags:
- optuna
- hyperparameter-optimization
- trial
related_skills:
- optuna-samplers
- optuna-pruners
- optuna-study
- optuna-trial
- optuna-visualization
- optuna-integration
- optuna-distributions
target_version: '4.9.0 (dev: after 4.9.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `optuna` ahead of the latest PyPI release (4.9.0 (dev: after 4.9.0)). Some APIs may not exist in your installed version.

# Optuna Trial

Extracted from optuna knowledge graph. Source: `optuna.trial` module.

## Quick Reference
| API | Purpose | Parameters | Graph Node |
|-----|---------|------------|-----------|
| `Trial.suggest_float()` | Suggest a floating-point parameter | `name`, `low`, `high`, `step`, `log` | trial/_trial.py:L87 |
| `Trial.suggest_int()` | Suggest an integer parameter | `name`, `low`, `high`, `step`, `log` | trial/_trial.py:L254 |
| `Trial.suggest_categorical()` | Suggest a categorical choice | `name`, `choices` | trial/_trial.py:L344 |
| `Trial.suggest_uniform()` | Deprecated: use `suggest_float` | `name`, `low`, `high` | trial/_base.py:L42 |
| `Trial.suggest_loguniform()` | Deprecated: use `suggest_float(log=True)` | `name`, `low`, `high` | trial/_base.py:L47 |
| `Trial.suggest_discrete_uniform()` | Deprecated: use `suggest_float(step=...)` | `name`, `low`, `high`, `q` | trial/_base.py:L52 |
| `Trial.should_prune()` | Check if trial should be pruned | — | trial/_trial.py:L520 |
| `Trial.report()` | Report intermediate objective value | `value`, `step` | trial/_base.py:L94 |
| `Trial.set_user_attr()` | Attach custom metadata to trial | `key`, `value` | trial/_trial.py:L552 |
| `Trial.params` | Access current trial parameters | — (property) | trial/_trial.py:L713 |

## Common Patterns

### Parameter Suggestion
```python
def objective(trial):
    # Float with log scale
    lr = trial.suggest_float("lr", 1e-5, 1e-2, log=True)
    
    # Integer with step
    n_units = trial.suggest_int("n_units", 16, 256, step=16)
    
    # Categorical choice
    optimizer = trial.suggest_categorical("optimizer", ["adam", "sgd", "rmsprop"])
    
    # Float with discrete step
    dropout = trial.suggest_float("dropout", 0.0, 0.5, step=0.05)
    
    return train_and_evaluate(lr, n_units, optimizer, dropout)
```

### Conditional Parameters
```python
def objective(trial):
    model_type = trial.suggest_categorical("model", ["cnn", "rnn"])
    
    if model_type == "cnn":
        n_filters = trial.suggest_int("n_filters", 32, 256)
        kernel_size = trial.suggest_int("kernel_size", 3, 7)
        return train_cnn(n_filters, kernel_size)
    else:
        n_units = trial.suggest_int("n_units", 64, 512)
        n_layers = trial.suggest_int("n_layers", 1, 4)
        return train_rnn(n_units, n_layers)
```

### Pruning with Intermediate Reports
```python
def objective(trial):
    lr = trial.suggest_float("lr", 1e-5, 1e-2, log=True)
    
    for epoch in range(100):
        val = train_one_epoch(lr, epoch)
        trial.report(val, epoch)
        
        if trial.should_prune():
            raise optuna.TrialPruned()
    
    return val
```

### User Attributes for Metadata
```python
def objective(trial):
    trial.set_user_attr("model_size_mb", model_size)
    trial.set_user_attr("gpu", gpu_name)
    # ... training
```

## Pitfalls

1. **Deprecated suggest methods**: `suggest_uniform`, `suggest_loguniform`, `suggest_discrete_uniform` are deprecated since Optuna v3.0. Use `suggest_float` with appropriate kwargs.
2. **Forgetting `raise TrialPruned()`**: `trial.should_prune()` returns True/False but doesn't stop execution. Must raise `optuna.TrialPruned`.
3. **Non-deterministic parameter suggestion**: Calling `suggest_*` with the same name but different ranges crashes. Use conditional logic to avoid re-definition.
4. **`step` and `log` are mutually exclusive**: Cannot use both `step` and `log=True` in `suggest_float`.
5. **Trial objects are single-use**: Each call to `objective(trial)` gets a fresh `Trial` instance.

## Verification Checklist

- [ ] All `suggest_*()` calls use `suggest_float`/`suggest_int`/`suggest_categorical` (not deprecated methods)
- [ ] Parameter names are unique within each trial
- [ ] `trial.report()` is called at regular intervals if using pruning
- [ ] `optuna.TrialPruned` is raised after `trial.should_prune()` returns `True`
- [ ] Conditional parameters don't re-define the same name with different bounds

## Provenance

- Knowledge graph: optuna, 2205 nodes, 4010 edges, 226 communities
- God nodes: `TrialState` (44), `FrozenTrial` (40), `Trial` (33) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ b6f2ea62fbe7, backend opencode, description coverage 85%
