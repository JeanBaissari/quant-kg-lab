---
name: quant-portfolio-construction
description: "Use when building portfolios from strategy signals — mean-variance optimization, risk parity, Black-Litterman, and position sizing from Kelly criterion. Integrates scikit-learn covariance and decomposition for risk modeling."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [scikit-learn-covariance, scikit-learn-decomposition, quant-portfolio-optimization, pyportfolioopt-efficient-frontier, riskfolio-portfolio]
tags: [quantitative-finance, portfolio-optimization, risk-parity, mean-variance, position-sizing]
related_skills: [scikit-learn-covariance, scikit-learn-decomposition, quant-portfolio-optimization, pyportfolioopt-efficient-frontier, riskfolio-portfolio]
target_version: cross-lib
---

# Portfolio Construction & Position Sizing

Raw strategy signals must be translated into portfolio weights. This skill covers three approaches to weight allocation with risk-awareness.

## Steps

1. **Estimate a stable covariance matrix** — sample covariance is unstable with many assets; shrink it with `LedoitWolf` before any weight computation. Graph node: `sklearn.covariance.LedoitWolf` (`sklearn/covariance/_shrunk_covariance.py`).
2. **Inverse volatility / risk parity weights** — equal-risk-contribution weighting built on the shrunk covariance (inverse-vol variant skips the correlation adjustment).
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
3. **Minimum variance (Markowitz)** — `scipy-optimize`: minimize portfolio variance with weights summing to one; no expected-return estimates needed.
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
4. **Factor-model risk decomposition (optional)** — `scikit-learn-decomposition`: PCA on the return space identifies the risk factors driving the covariance. Graph node: `sklearn.decomposition.PCA` (`sklearn/decomposition/_pca.py`).
5. **Kelly criterion position sizing** — size each signal with the Kelly fraction; use half-Kelly in production.
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

## Pitfalls

1. **Covariance estimation noise**: Sample covariance is unstable with many assets. Always use shrinkage (LedoitWolf) or factor models.
2. **Kelly over-betting**: Full Kelly is aggressive — 50% drawdowns are common. Use half-Kelly in production.
3. **Long-only constraint realism**: Many quant strategies are long-short. Don't artificially restrict to [0,1] if the strategy allows shorting.

## Composed Skills & Bridges

| Skill / Bridge | Role in this workflow |
|----------------|-----------------------|
| `scipy-optimize` | `minimize` solver for Markowitz allocation (Step 3) |
| `scikit-learn-decomposition` | PCA risk-factor decomposition (Step 4) |
| `numpy-core` | array math for covariance/weights (Steps 2–3, 5) |
| `quant-ml-strategy` | consumer playbook — sizes ML-signal positions with these weights |
