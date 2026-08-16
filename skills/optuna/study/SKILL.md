---
name: optuna-study
description: "Use when working with Optuna Study lifecycle \u2014 create_study, Study.optimize,\
  \ Study.ask, Study.tell, load_study, delete_study, copy_study. Covers study creation,\
  \ optimization loops, ask-and-tell interface, persistence, and multi-objective studies."
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
  graph_hash: 1d44e2e3a333f787
tags:
- optuna
- hyperparameter-optimization
- study
related_skills:
- optuna-samplers
- optuna-pruners
- optuna-study
- optuna-trial
- optuna-visualization
- optuna-integration
- optuna-distributions
---

# Optuna Study

Extracted from optuna knowledge graph. Source: `optuna.study` module.

## Quick Reference
| API | Purpose | Key Parameters | Graph Node |
|-----|---------|----------------|-----------|
| `create_study()` | Create a new optimization study | `direction`, `sampler`, `pruner`, `storage`, `study_name` | study/study.py:L1204 |
| `Study.optimize()` | Run optimization with an objective function | `objective`, `n_trials`, `timeout`, `callbacks` | study/study.py:L414 |
| `Study.ask()` | Suggest next trial parameters (without evaluating) | `fixed_distributions` | study/study.py:L528 |
| `Study.tell()` | Report trial result back to study | `trial`, `values`, `state` | study/study.py:L614 |
| `load_study()` | Load existing study from storage | `study_name`, `storage` | study/study.py:L1355 |
| `delete_study()` | Delete study and all trials from storage | `study_name`, `storage` | study/study.py:L1442 |
| `copy_study()` | Copy study between storages | `from_study_name`, `to_study_name`, `from_storage`, `to_storage` | study/study.py:L1505 |
| `get_all_study_names()` | List all studies in storage | `storage` | study/study.py:L1706 |
| `Study.best_trial` | Get the best trial object | — (property) | study/study.py:L141 |
| `Study.trials_dataframe()` | Get trials as pandas DataFrame | — | study/study.py:L766 |

## Common Patterns

### Basic Optimization Loop
```python
import optuna

def objective(trial):
    x = trial.suggest_float("x", -10, 10)
    return (x - 2) ** 2

study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=100)

print(f"Best value: {study.best_value}")
print(f"Best params: {study.best_params}")
```

### Ask-and-Tell Interface (Manual Control)
```python
study = optuna.create_study(direction="minimize")

for _ in range(100):
    trial = study.ask()                    # Get suggested params
    value = (trial.suggest_float("x", -10, 10) - 2) ** 2
    study.tell(trial, value)               # Report result back

print(study.best_value)
```

### Persistent Storage (SQLite)
```python
storage = "sqlite:///optuna_study.db"
study = optuna.create_study(
    study_name="my_study",
    storage=storage,
    direction="minimize",
    load_if_exists=True    # Resume if exists
)
study.optimize(objective, n_trials=100)

# Later: load and analyze
study2 = optuna.load_study("my_study", storage=storage)
```

### Multi-Objective Study
```python
study = optuna.create_study(
    directions=["minimize", "maximize"],
    study_name="multi_obj"
)
study.optimize(objective, n_trials=100)

# Get Pareto front
for trial in study.best_trials:
    print(trial.values)
```

### Callbacks
```python
study.optimize(
    objective, n_trials=100,
    callbacks=[
        optuna.callbacks.MaxTrialsCallback(100),
        # Custom callback
    ]
)
```

## Pitfalls

1. **Forgetting `load_if_exists=True`**: Without it, re-running crashes if study already exists in storage.
2. **`timeout` vs `n_trials`**: `timeout` (seconds) only stops new trials; `n_trials` sets max count. Combine for safety.
3. **Multi-objective `direction` must be list**: Single string `"maximize"` for single-objective; list `["maximize", "minimize"]` for multi.
4. **Ask-and-Tell: don't forget `trial.suggest_*()`**: `study.ask()` returns a FrozenTrial; you still call `suggest_*` on it.
5. **Study deletion**: `delete_study()` requires storage reference; in-memory studies are auto-deleted at process exit.

## Verification Checklist

- [ ] `direction` or `directions` matches optimization goal
- [ ] `storage` is set for persistent studies
- [ ] `load_if_exists=True` when resuming
- [ ] Callbacks are non-blocking and exception-safe
- [ ] `timeout` is set as safety net for long-running optimizations

## Provenance

- Knowledge graph: optuna, 2205 nodes, 4010 edges, 226 communities
- God nodes: `Study` (221), `StudyDirection` (137), `FrozenStudy` (66) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ b6f2ea62fbe7, backend opencode, description coverage 85%
