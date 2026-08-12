---
name: optuna-visualization
description: "Use when working with Optuna visualization functions \u2014 plot_optimization_history,\
  \ plot_slice, plot_contour, plot_param_importances, plot_edf, plot_parallel_coordinate,\
  \ plot_pareto_front, plot_rank. Covers study analysis, parameter relationships,\
  \ and interactive Plotly charts."
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
- visualization
related_skills:
- optuna-samplers
- optuna-pruners
- optuna-study
- optuna-trial
- optuna-visualization
- optuna-integration
- optuna-distributions
---

# Optuna Visualization

Extracted from optuna knowledge graph. Source: `optuna.visualization` module.

## Quick Reference
| Function | Plot Type | Purpose | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node |
|----------|-----------|---------|
| `plot_optimization_history()` | Line chart | Show objective value over trials; identify convergence | visualization/_optimization_history.py:L174 |
| `plot_slice()` | Slice plot | Show parameter vs objective; identify promising regions | visualization/_slice.py:L148 |
| `plot_contour()` | Contour plot | Show 2-parameter interactions as heatmap | visualization/_contour.py:L70 |
| `plot_param_importances()` | Bar chart | Rank parameters by importance (fANOVA or MDI) | visualization/_param_importances.py:L118 |
| `plot_edf()` | EDF curve | Empirical distribution function; compare sampler efficiency | visualization/_edf.py:L42 |
| `plot_parallel_coordinate()` | Parallel coordinates | Visualize high-dimensional parameter relationships | visualization/_parallel_coordinate.py:L56 |
| `plot_intermediate_values()` | Line chart per trial | Show learning curves; visualize pruning | visualization/_intermediate_values.py:L59 |
| `plot_pareto_front()` | Scatter plot | Visualize Pareto front in multi-objective studies | visualization/_pareto_front.py:L40 |
| `plot_hypervolume_history()` | Line chart | Track hypervolume over trials (multi-objective) | visualization/_hypervolume_history.py:L34 |
| `plot_rank()` | Rank plot | Visualize trial rankings across objectives | visualization/_rank.py:L70 |

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

## Provenance

- Knowledge graph: optuna, 2205 nodes, 4010 edges, 226 communities
- God nodes: `_rank.py` (14), `_contour.py` (13), `_contour.py` (12) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ b6f2ea62fbe7, backend opencode, description coverage 85%
