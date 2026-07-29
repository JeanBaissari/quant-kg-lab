---
name: quant-walk-forward-validation
description: Use when implementing walk-forward validation, time-series cross-validation, or rolling/expanding window backtesting for trading strategies. Integrates scikit-learn TimeSeriesSplit with custom purging/embargo logic.
version: 0.1.0
author: quant-kg-lab
license: MIT
metadata:
  hermes:
    tags: [quantitative-finance, backtesting, walk-forward, time-series, cross-validation]
    related_skills: [scikit-learn-model-selection, optuna-study]
---

# Walk-Forward Validation for Trading Strategies

Standard k-fold cross-validation leaks future information in time-series data. Walk-forward validation (also called backtesting or time-series CV) preserves temporal order by training on past data and testing on future data.

## Pattern

```python
from sklearn.model_selection import TimeSeriesSplit
import numpy as np

def walk_forward_validate(X, y, model, n_splits=5, purge_window=0):
    """Walk-forward validation with optional purging."""
    tscv = TimeSeriesSplit(n_splits=n_splits)
    results = []
    
    for train_idx, test_idx in tscv.split(X):
        if purge_window > 0:
            # Purge: remove training samples too close to test period
            test_start = test_idx[0]
            train_idx = train_idx[train_idx < test_start - purge_window]
        
        model.fit(X[train_idx], y[train_idx])
        pred = model.predict(X[test_idx])
        results.append(pred)
    
    return results
```

## Key Concepts

| Concept | Description | Graph Node |
|---------|-------------|------------|
| TimeSeriesSplit | Sequential train/test splits preserving order | `sklearn.model_selection.TimeSeriesSplit` |
| Purging | Remove training data overlapping with test period | Custom implementation |
| Embargo | Gap between train and test to avoid leakage | Custom implementation |
| Combinatorial Purge | Cross-validation with multiple purge windows | Advanced pattern |

## Pitfalls

1. **Default CV shuffle=True leaks**: Never shuffle time-series data in CV.
2. **Stationarity assumption**: Walk-forward assumes regime stability within windows.
3. **Purge window sizing**: Too small → leakage; too large → insufficient training data.

## Integration with Optuna

```python
import optuna

def objective(trial):
    purge_window = trial.suggest_int("purge_window", 0, 30)
    n_splits = trial.suggest_int("n_splits", 3, 10)
    # ... walk-forward validate and return Sharpe
```

## References

- `sklearn.model_selection.TimeSeriesSplit` — graph node: `sklearn/model_selection/_split.py`
- `optuna.study.Study.optimize` — graph node: `optuna/study/study.py`
