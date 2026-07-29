---
name: optuna-visualization
description: Use when working with Optuna visualization functions — plot_optimization_history, plot_slice, plot_contour, plot_param_importances, plot_edf, plot_parallel_coordinate, plot_pareto_front, plot_rank. Covers study analysis, parameter relationships, and interactive Plotly charts.
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
metadata:
  hermes:
    tags: [optuna, hyperparameter-optimization, visualization]
    related_skills: [optuna-samplers, optuna-pruners, optuna-study, optuna-trial, optuna-visualization, optuna-integration, optuna-distributions]
---

# Optuna Visualization

Extracted from optuna knowledge graph. Source: `optuna.visualization` module.

## Quick Reference

| Function | Plot Type | Purpose |
|----------|-----------|---------|
| `plot_optimization_history()` | Line chart | Show objective value over trials; identify convergence |
| `plot_slice()` | Slice plot | Show parameter vs objective; identify promising regions |
| `plot_contour()` | Contour plot | Show 2-parameter interactions as heatmap |
| `plot_param_importances()` | Bar chart | Rank parameters by importance (fANOVA or MDI) |
| `plot_edf()` | EDF curve | Empirical distribution function; compare sampler efficiency |
| `plot_parallel_coordinate()` | Parallel coordinates | Visualize high-dimensional parameter relationships |
| `plot_intermediate_values()` | Line chart per trial | Show learning curves; visualize pruning |
| `plot_pareto_front()` | Scatter plot | Visualize Pareto front in multi-objective studies |
| `plot_hypervolume_history()` | Line chart | Track hypervolume over trials (multi-objective) |
| `plot_rank()` | Rank plot | Visualize trial rankings across objectives |

## Common Patterns

### Convergence Analysis
```python
import optuna
from optuna.visualization import plot_optimization_history

study = optuna.load_study("my_study", "sqlite:///optuna.db")
fig = plot_optimization_history(study)
fig.show()  # Interactive Plotly chart
```

### Parameter Importance
```python
from optuna.visualization import plot_param_importances

fig = plot_param_importances(study)
fig.show()
```

### Parameter Relationships
```python
from optuna.visualization import (
    plot_slice,
    plot_contour,
    plot_parallel_coordinate
)

# 1D: parameter vs objective
plot_slice(study, params=["lr", "n_layers"]).show()

# 2D: parameter interaction heatmap
plot_contour(study, params=["lr", "n_layers"]).show()

# High-dimensional overview
plot_parallel_coordinate(study).show()
```

### Multi-Objective Analysis
```python
from optuna.visualization import plot_pareto_front

# Visualize trade-offs
plot_pareto_front(study).show()
```

### Matplotlib Backend
```python
from optuna.visualization.matplotlib import (
    plot_optimization_history,
    plot_param_importances
)
import matplotlib.pyplot as plt

plot_optimization_history(study)
plt.show()
```

## Pitfalls

1. **Empty study**: All plot functions raise errors on studies with zero completed trials.
2. **Single-trial studies**: `plot_contour` and `plot_slice` need multiple trials to show meaningful patterns.
3. **Categorical-only studies**: `plot_contour` requires at least 2 numeric parameters.
4. **Importance evaluation cost**: `plot_param_importances` with default fANOVA can be slow for many parameters (>20). Use `evaluator=MeanDecreaseImpurityImportanceEvaluator` for faster approximation.
5. **Plotly not installed**: `pip install plotly` required; functions raise clear errors if missing.

## Verification Checklist

- [ ] Study has ≥ 2 completed trials for most plots
- [ ] Plotly or matplotlib is installed
- [ ] Parameters of interest are specified in `params` argument for slice/contour
- [ ] Multi-objective plots (Pareto, hypervolume) only used with multi-objective studies
- [ ] Importance evaluator chosen appropriately (fANOVA vs MDI)

## References

- Source: `optuna/visualization/__init__.py`
- `references/api.md` — Full visualization API surface from knowledge graph
