---
name: optuna-samplers
description: Use when working with Optuna hyperparameter optimization samplers — TPESampler, RandomSampler, GridSampler, CmaEsSampler, BoTorchSampler. Covers sampler selection, parameter suggestion, and multi-objective optimization.
version: 0.1.0
author: quant-kg-lab
license: MIT
source_repo: optuna/optuna
source_version: master
extraction_date: 2026-07-29
graph_hash: 3912_nodes_8405_edges
graph_stats:
  nodes: 3912
  edges: 8405
  communities: 228
  top_god_nodes:
    - Study (degree=228)
    - BaseDistribution (degree=213)
    - StudyDirection (degree=150)
    - optuna.trial (degree=139)
    - optuna.study (degree=100)
metadata:
  hermes:
    tags: [optuna, hyperparameter-optimization, bayesian-optimization, samplers, HPO]
    related_skills: [optuna-pruners, optuna-study, scikit-learn-model-selection]
---

# Optuna Samplers

Extracted from optuna knowledge graph. Source: `optuna.samplers` module.

## Quick Reference

| Sampler | Algorithm | Best For |
|---------|-----------|----------|
| `TPESampler` | Tree-structured Parzen Estimator | General-purpose Bayesian opt (default) |
| `RandomSampler` | Uniform random | Baseline, high-dimensional categorical |
| `GridSampler` | Exhaustive grid | Small search spaces, reproducibility |
| `CmaEsSampler` | CMA-ES | Continuous, ill-conditioned spaces |
| `BoTorchSampler` | Gaussian Process (BoTorch) | Low-dim (<20) continuous, sample-efficient |
| `NSGAIISampler` | NSGA-II | Multi-objective optimization |

## Common Patterns

```python
import optuna

def objective(trial):
    # Suggest hyperparameters
    lr = trial.suggest_float("lr", 1e-5, 1e-2, log=True)
    n_layers = trial.suggest_int("n_layers", 1, 5)
    dropout = trial.suggest_float("dropout", 0.0, 0.5)
    # ... train and return metric

study = optuna.create_study(
    direction="maximize",
    sampler=optuna.samplers.TPESampler(seed=42)
)
study.optimize(objective, n_trials=100)
```

## Pitfalls

1. **TPESampler with few trials**: TPE needs warm-up (default `n_startup_trials=10`). Below that, behaves like random.
2. **Dynamic search spaces**: Changing param ranges mid-study confuses TPE inference.
3. **Multi-objective requires specific sampler**: Use `NSGAIISampler` or `BoTorchSampler` with `directions`.

## References

- `references/api.md` — Full sampler API surface from knowledge graph
