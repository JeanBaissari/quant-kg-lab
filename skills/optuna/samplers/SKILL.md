---
name: optuna-samplers
description: "Use when working with Optuna hyperparameter optimization samplers \u2014\
  \ TPESampler, RandomSampler, GridSampler, CmaEsSampler, NSGAIISampler, BoTorchSampler,\
  \ QMCSampler, BruteForceSampler. Covers sampler selection, parameter suggestion,\
  \ and multi-objective optimization."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: optuna/optuna
source_commit: b6f2ea62fbe7fb09d0d1c75783c65dad098d9a06
extraction_date: 2026-07-29
graph:
  nodes: 2205
  edges: 4010
  community_count: 226
  graph_hash: fa73620b99133289
tags:
- optuna
- hyperparameter-optimization
- samplers
related_skills:
- optuna-samplers
- optuna-pruners
- optuna-study
- optuna-trial
- optuna-visualization
- optuna-integration
- optuna-distributions
---

# Optuna Samplers

Extracted from optuna knowledge graph. Source: `optuna.samplers` module.

## Quick Reference

| Sampler | Algorithm | Best For | Multi-Objective |
|---------|-----------|----------|-----------------|
| `TPESampler` | Tree-structured Parzen Estimator (TPE) | General-purpose Bayesian optimization (default) | No |
| `RandomSampler` | Uniform random search | Baseline, high-dimensional categorical spaces | Yes |
| `GridSampler` | Exhaustive grid search | Small search spaces, reproducibility | No |
| `CmaEsSampler` | Covariance Matrix Adaptation Evolution Strategy | Continuous spaces, ill-conditioned problems | No |
| `NSGAIISampler` | Non-dominated Sorting Genetic Algorithm II | Multi-objective optimization | Yes |
| `NSGAIIISampler` | NSGA-III with reference directions | Many-objective optimization (3+ objectives) | Yes |
| `QMCSampler` | Quasi-Monte Carlo (Sobol/Halton) | Low-discrepancy sequences, initial exploration | Yes |
| `BruteForceSampler` | Exhaustive enumeration | Tiny discrete search spaces | No |
| `GPSampler` | Gaussian Process (GP) | Low-dimensional continuous spaces (<20) | No |
| `PartialFixedSampler` | Wrapper that fixes some parameters | Conditional/DAG search spaces | Wraps any |

## Common Patterns

### Basic TPE Optimization
```python
import optuna

def objective(trial):
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

### Multi-Objective with NSGA-II
```python
study = optuna.create_study(
    directions=["maximize", "minimize"],
    sampler=optuna.samplers.NSGAIISampler(seed=42)
)
study.optimize(objective, n_trials=100)

# Access Pareto front
for trial in study.best_trials:
    print(trial.values)
```

### Random Search Baseline
```python
sampler = optuna.samplers.RandomSampler(seed=42)
study = optuna.create_study(sampler=sampler)
```

### CMA-ES for Continuous Optimization
```python
sampler = optuna.samplers.CmaEsSampler(
    seed=42,
    sigma0=0.1,            # Initial standard deviation
    restart_strategy="ipop" # Restart with increased population
)
```

### QMC for Low-Discrepancy Initialization
```python
sampler = optuna.samplers.QMCSampler(seed=42)
# Often used as initial sampler before TPE
```

## Pitfalls

1. **TPESampler with few trials**: TPE needs warm-up (default `n_startup_trials=10`). Below that, behaves like random search.
2. **Dynamic search spaces**: Changing parameter ranges mid-study via `suggest_float` with different ranges confuses TPE inference. Prefer conditional parameters.
3. **Multi-objective requires compatible sampler**: Use `NSGAIISampler`, `NSGAIIISampler`, `QMCSampler`, or `RandomSampler` with `directions`. TPE and CMA-ES don't support multi-objective.
4. **CMA-ES and integer parameters**: CMA-ES only supports continuous float parameters natively. Integer parameters require special handling or alternative samplers.
5. **GridSampler memory**: Grid size grows exponentially with parameter count. Only practical for 2-5 parameters with small cardinalities.

## Verification Checklist

- [ ] Sampler is compatible with study direction(s) (single vs multi-objective)
- [ ] `n_startup_trials` is appropriate for TPE warm-up
- [ ] Search space bounds are finite (TPE, CMA-ES require bounded spaces)
- [ ] `seed` is set for reproducibility
- [ ] Dynamic parameters use conditional logic, not mid-study range changes