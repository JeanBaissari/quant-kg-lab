---
name: optuna-pruners
description: "Use when working with Optuna pruning algorithms \u2014 MedianPruner,\
  \ PercentilePruner, SuccessiveHalvingPruner, HyperbandPruner, ThresholdPruner, PatientPruner,\
  \ WilcoxonPruner. Covers early stopping, pruning schedules, and trial efficiency."
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
- pruners
related_skills:
- optuna-samplers
- optuna-pruners
- optuna-study
- optuna-trial
- optuna-visualization
- optuna-integration
- optuna-distributions
---

# Optuna Pruners

Extracted from optuna knowledge graph. Source: `optuna.pruners` module.

## Quick Reference
| Pruner | Strategy | Best For | Requires Report | Graph Node |
|------|--------|--------|---------------|----------|
| `MedianPruner` | Prune if intermediate value is worse than median of previous trials at same step | Simple early stopping | Yes | pruners/_median.py:L4 |
| `PercentilePruner` | Prune if value is below specified percentile of previous trials | Tunable aggressiveness | Yes | : |
| `SuccessiveHalvingPruner` | Allocate equal budget across trials, prune worst half at each rung | Fixed budget problems | Yes | pruners/_successive_halving.py:L15 |
| `HyperbandPruner` | Adaptive budget allocation across brackets (SuccessiveHalving on steroids) | Large-scale HPO, unknown optimal budgets | Yes | pruners/_hyperband.py:L21 |
| `ThresholdPruner` | Prune if value exceeds a fixed threshold | Known performance bounds | Yes | pruners/_threshold.py:L29 |
| `PatientPruner` | Prune if no improvement for N consecutive steps | Avoiding premature stopping | Yes | pruners/_patient.py:L17 |
| `WilcoxonPruner` | Wilcoxon signed-rank test to detect stagnation | Statistical rigor | Yes | pruners/_wilcoxon.py:L27 |
| `NopPruner` | Never prunes (passthrough) | Disabling pruning | No | pruners/_nop.py:L13 |

## Common Patterns

### MedianPruner with Early Stopping
```python
import optuna

def objective(trial):
    for step in range(100):
        val = train_one_epoch()
        trial.report(val, step)
        if trial.should_prune():
            raise optuna.TrialPruned()
    return val

study = optuna.create_study(
    pruner=optuna.pruners.MedianPruner(
        n_startup_trials=5,
        n_warmup_steps=10,
        interval_steps=1
    )
)
study.optimize(objective, n_trials=100)
```

### HyperbandPruner for Large-Scale HPO
```python
study = optuna.create_study(
    direction="maximize",
    pruner=optuna.pruners.HyperbandPruner(
        min_resource=1,
        max_resource=100,
        reduction_factor=3
    )
)
```

### PercentilePruner for Aggressive Pruning
```python
pruner = optuna.pruners.PercentilePruner(
    percentile=25.0,      # Prune bottom 25%
    n_startup_trials=5,
    n_warmup_steps=10
)
```

### PatientPruner (Wrap Another Pruner)
```python
pruner = optuna.pruners.PatientPruner(
    wrapped_pruner=optuna.pruners.MedianPruner(),
    patience=5,           # Wait 5 steps before pruning
    min_delta=0.01        # Minimum improvement required
)
```

## Pitfalls

1. **Missing `trial.report()` calls**: Pruning silently does nothing without intermediate value reports.
2. **Forgetting `TrialPruned` exception**: If you use `trial.should_prune()` without raising `optuna.TrialPruned`, pruning is ignored.
3. **Hyperband with wrong `min_resource`**: Setting `min_resource` too low creates too many brackets; too high wastes budget on poor trials.
4. **MedianPruner with small samples**: Below `n_startup_trials`, pruning is disabled entirely.
5. **PatientPruner patience too high**: Effectively disables pruning if patience exceeds training steps.

## Verification Checklist

- [ ] `trial.report(value, step)` is called in the objective at every checkpoint
- [ ] `trial.should_prune()` check is followed by `raise optuna.TrialPruned()`
- [ ] `n_startup_trials` is ≥ 5 for statistical stability
- [ ] `n_warmup_steps` provides enough early training before pruning begins
- [ ] Hyperband's `max_resource` matches actual training budget

## Provenance

- Knowledge graph: optuna, 2205 nodes, 4010 edges, 226 communities
- God nodes: `HyperbandPruner` (11), `SuccessiveHalvingPruner` (11), `PercentilePruner` (9) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ b6f2ea62fbe7, backend opencode, description coverage 85%
