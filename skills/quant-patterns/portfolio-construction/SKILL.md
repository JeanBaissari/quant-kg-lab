---
name: quant-portfolio-construction
description: Use when building portfolios from strategy signals — mean-variance optimization, risk parity, Black-Litterman, and position sizing from Kelly criterion. Integrates scikit-learn covariance and decomposition for risk modeling.
version: 0.1.0
author: quant-kg-lab
license: MIT
metadata:
  hermes:
    tags: [quantitative-finance, portfolio-optimization, risk-parity, mean-variance, position-sizing]
    related_skills: [scikit-learn-covariance, scikit-learn-decomposition]
---

# Portfolio Construction & Position Sizing

Raw strategy signals must be translated into portfolio weights. This skill covers three approaches to weight allocation with risk-awareness.

## Pattern 1: Inverse Volatility / Risk Parity

```python
import numpy as np
from sklearn.covariance import LedoitWolf

def risk_parity_weights(returns):
    """Equal risk contribution weights."""
    cov = LedoitWolf().fit(returns).covariance_
    vols = np.sqrt(np.diag(cov))
    inv_vols = 1.0 / vols
    return inv_vols / inv_vols.sum()

def inverse_volatility_weights(returns):
    """Simple inverse-vol weighting (no correlation adjustment)."""
    vols = returns.std(axis=0)
    inv_vols = 1.0 / vols
    return inv_vols / inv_vols.sum()
```

## Pattern 2: Minimum Variance (Markowitz)

```python
from scipy.optimize import minimize

def minimum_variance_weights(cov_matrix):
    """Minimum variance portfolio (no expected returns needed)."""
    n = cov_matrix.shape[0]
    
    def portfolio_variance(w):
        return w @ cov_matrix @ w
    
    constraints = [{'type': 'eq', 'fun': lambda w: w.sum() - 1}]
    bounds = [(0, 1) for _ in range(n)]  # long-only
    
    result = minimize(
        portfolio_variance,
        x0=np.ones(n) / n,
        bounds=bounds,
        constraints=constraints
    )
    return result.x
```

## Pattern 3: Kelly Criterion Position Sizing

```python
def kelly_fraction(win_rate, avg_win, avg_loss):
    """Kelly criterion for optimal bet size."""
    b = avg_win / abs(avg_loss)  # win/loss ratio
    p = win_rate
    q = 1 - p
    return (p * b - q) / b

def half_kelly(win_rate, avg_win, avg_loss):
    """Half-Kelly: more conservative, 75% of growth, 25% of volatility."""
    return kelly_fraction(win_rate, avg_win, avg_loss) / 2
```

## Graph Nodes Used

| Concept | Graph Node | Source |
|---------|------------|--------|
| LedoitWolf covariance | `sklearn.covariance.LedoitWolf` | `sklearn/covariance/_shrunk_covariance.py` |
| PCA (risk factor decomposition) | `sklearn.decomposition.PCA` | `sklearn/decomposition/_pca.py` |

## Pitfalls

1. **Covariance estimation noise**: Sample covariance is unstable with many assets. Always use shrinkage (LedoitWolf) or factor models.
2. **Kelly over-betting**: Full Kelly is aggressive — 50% drawdowns are common. Use half-Kelly in production.
3. **Long-only constraint realism**: Many quant strategies are long-short. Don't artificially restrict to [0,1] if the strategy allows shorting.
