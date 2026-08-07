---
name: optuna-distributions
description: "Use when working with Optuna probability distributions for parameter spaces — FloatDistribution, IntDistribution, CategoricalDistribution, BaseDistribution. Covers internal/external representations, distribution single-range checks, and deprecated distribution classes."
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
tags: [optuna, hyperparameter-optimization, distributions]
related_skills: [optuna-samplers, optuna-pruners, optuna-study, optuna-trial, optuna-visualization, optuna-integration, optuna-distributions]
---

# Optuna Distributions

Extracted from optuna knowledge graph. Source: `optuna.distributions` module.

## Quick Reference

| Distribution | Domain | Internal Repr | Use Case |
|-------------|--------|---------------|----------|
| `FloatDistribution` | Continuous float `[low, high]` | `[0, 1]` uniform | Learning rate, dropout, regularization |
| `IntDistribution` | Discrete integer `[low, high]` | `[0, N-1]` uniform | Number of layers, units, epochs |
| `CategoricalDistribution` | Finite set of choices | Index in choices | Optimizer, activation function, architecture |
| `BaseDistribution` (ABC) | Abstract base | — | Custom distribution implementation |
| `UniformDistribution` (deprecated) | Continuous uniform | `[0, 1]` | **Use `FloatDistribution` instead** |
| `LogUniformDistribution` (deprecated) | Continuous log-uniform | `[0, 1]` | **Use `FloatDistribution(log=True)` instead** |
| `DiscreteUniformDistribution` (deprecated) | Discrete uniform | `[0, N-1]` | **Use `IntDistribution` or `FloatDistribution(step=...)` instead** |
| `IntUniformDistribution` (deprecated) | Integer uniform | `[0, N-1]` | **Use `IntDistribution` instead** |
| `IntLogUniformDistribution` (deprecated) | Integer log-uniform | `[0, N-1]` | **Use `IntDistribution(log=True)` instead** |

## Distribution Internal/External Representation

Optuna samplers work with an internal `[0, 1]` space. Distributions convert between external (user-facing) and internal (sampler-facing) representations:

- `to_internal_repr(value)` → convert user value to `[0, 1]`
- `to_external_repr(value)` → convert `[0, 1]` to user value
- `single()` → True if distribution contains only one possible value
- `_contains(value)` → check if internal value is in range

## Common Patterns

### Defining Parameter Spaces with Distributions
```python
from optuna.distributions import (
    FloatDistribution,
    IntDistribution,
    CategoricalDistribution
)

# These are what trial.suggest_*() creates internally
lr_dist = FloatDistribution(low=1e-5, high=1e-2, log=True)
n_layers_dist = IntDistribution(low=1, high=10)
optimizer_dist = CategoricalDistribution(choices=["adam", "sgd", "rmsprop"])
```

### Fixed Distributions in Ask-and-Tell
```python
study = optuna.create_study()
distributions = {
    "lr": FloatDistribution(1e-5, 1e-2, log=True),
    "n_layers": IntDistribution(1, 5),
}
trial = study.ask(fixed_distributions=distributions)
# Now trial.suggest_float("lr", ...) uses the fixed distribution
```

### Checking Distribution Properties
```python
dist = FloatDistribution(0.0, 1.0)
print(dist.single())  # False
print(dist._contains(0.5))  # True

# Transform values
internal = dist.to_internal_repr(0.7)     # ~0.7 (linear)
external = dist.to_external_repr(0.7)     # 0.7
```

## Pitfalls

1. **Deprecated distribution classes**: `UniformDistribution`, `LogUniformDistribution`, etc. are deprecated since Optuna v3.0. Use `FloatDistribution` and `IntDistribution` instead.
2. **Don't create distributions directly in `suggest_*` calls**: `Trial.suggest_float()` creates the distribution internally. Only use explicit distributions with `study.ask(fixed_distributions=...)`.
3. **`single()` vs `_contains()`**: `single()` checks if the distribution has exactly one value (e.g., `IntDistribution(5, 5)`); `_contains()` checks if a value is valid.
4. **Internal representation is always `[0, 1]`**: Samplers don't see the original parameter ranges; transformations must be properly configured.
5. **Categorical NaN handling**: `CategoricalDistribution` treats `float('nan')` as a valid choice; `_categorical_choice_equal()` handles NaN comparison.

## Verification Checklist

- [ ] Using `FloatDistribution`/`IntDistribution` (not deprecated `UniformDistribution`/etc.)
- [ ] `low < high` for all numeric distributions
- [ ] `choices` in `CategoricalDistribution` is non-empty
- [ ] `log=True` only for strictly positive ranges (`low > 0`)
- [ ] `step` parameter is consistent with distribution type