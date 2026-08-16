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
  nodes: 2208
  edges: 4013
  community_count: 223
  graph_hash: 1d44e2e3a333f787
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
target_version: '4.9.0 (dev: after 4.9.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `optuna` ahead of the latest PyPI release (4.9.0 (dev: after 4.9.0)). Some APIs may not exist in your installed version.

# Optuna Samplers

Extracted from optuna knowledge graph. Source: `optuna.samplers` module.

## Quick Reference
| Sampler | Algorithm | Best For | Multi-Objective | Graph Node |
|-------|---------|--------|---------------|----------|
| `TPESampler` | Tree-structured Parzen Estimator (TPE) | General-purpose Bayesian optimization (default) | No | samplers/_tpe/sampler.py:L88 |
| `RandomSampler` | Uniform random search | Baseline, high-dimensional categorical spaces | Yes | samplers/_random.py:L19 |
| `GridSampler` | Exhaustive grid search | Small search spaces, reproducibility | No | samplers/_grid.py:L33 |
| `CmaEsSampler` | Covariance Matrix Adaptation Evolution Strategy | Continuous spaces, ill-conditioned problems | No | samplers/_cmaes.py:L50 |
| `NSGAIISampler` | Non-dominated Sorting Genetic Algorithm II | Multi-objective optimization | Yes | samplers/nsgaii/_sampler.py:L33 |
| `NSGAIIISampler` | NSGA-III with reference directions | Many-objective optimization (3+ objectives) | Yes | samplers/_nsgaiii/_sampler.py:L36 |
| `QMCSampler` | Quasi-Monte Carlo (Sobol/Halton) | Low-discrepancy sequences, initial exploration | Yes | samplers/_qmc.py:L38 |
| `BruteForceSampler` | Exhaustive enumeration | Tiny discrete search spaces | No | samplers/_brute_force.py:L226 |
| `GPSampler` | Gaussian Process (GP) | Low-dimensional continuous spaces (<20) | No | samplers/_gp/sampler.py:L67 |
| `PartialFixedSampler` | Wrapper that fixes some parameters | Conditional/DAG search spaces | Wraps any | samplers/_partial_fixed.py:L21 |

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

## Provenance

- Knowledge graph: optuna, 2205 nodes, 4010 edges, 226 communities
- God nodes: `LazyRandomState` (42), `CmaEsSampler` (24), `TPESampler` (23) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ b6f2ea62fbe7, backend opencode, description coverage 85%
