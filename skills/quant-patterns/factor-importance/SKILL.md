---
name: quant-factor-importance
description: "Use when ranking features by predictive power in trading models — permutation importance, SHAP values, MDI (mean decrease in impurity), and factor decay analysis. Integrates scikit-learn inspection and ensemble modules."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [scikit-learn-ensemble, scikit-learn-inspection]
tags: [quantitative-finance, factor-research, feature-importance, shap, permutation-importance]
related_skills: [scikit-learn-ensemble, scikit-learn-inspection]
---

# Factor Importance Ranking

Quant strategies rely on identifying which factors (features) drive predictive performance. This skill covers three approaches to importance ranking with temporal-awareness.

## Pattern 1: Permutation Importance

```python
from sklearn.inspection import permutation_importance

def factor_importance(model, X_val, y_val, feature_names):
    """Rank factors by permutation importance."""
    result = permutation_importance(
        model, X_val, y_val,
        n_repeats=10, random_state=42,
        scoring='neg_mean_squared_error'
    )
    
    rankings = sorted(
        zip(feature_names, result.importances_mean),
        key=lambda x: -x[1]
    )
    return rankings
```

## Pattern 2: Time-Decay Importance

Factors lose predictive power over time. Track importance stability:

```python
def time_decay_importance(model, X, y, dates, window=60):
    """Rolling factor importance to detect decay."""
    importances = []
    for i in range(window, len(X)):
        model.fit(X[i-window:i], y[i-window:i])
        imp = model.feature_importances_
        importances.append(imp)
    return np.array(importances)  # shape: (time, n_features)
```

## Graph Nodes Used

| Concept | Graph Node | Source |
|---------|------------|--------|
| Permutation Importance | `sklearn.inspection.permutation_importance` | `sklearn/inspection/_permutation_importance.py` |
| Feature Importances (MDI) | `RandomForestClassifier.feature_importances_` | `sklearn/ensemble/_forest.py` |
| SHAP Integration | Custom — wraps `shap.TreeExplainer` | External library |

## Pitfalls

1. **MDI bias toward high-cardinality features**: Tree-based importance inflates continuous/high-cardinality features.
2. **Correlated factors**: Permutation importance underestimates importance of correlated features.
3. **Temporal decay**: Factors important in 2020 may be irrelevant in 2025. Always track rolling importance.

## Integration with Optuna

Optimize factor selection via feature pruning:
```python
trial.suggest_categorical("use_momentum", [True, False])
trial.suggest_categorical("use_volatility", [True, False])
# ... pruned factors removed from feature set
```
