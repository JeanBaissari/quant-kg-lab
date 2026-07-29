---
name: quant-regime-detection
description: Use when detecting market regimes for conditional strategy switching — Hidden Markov Models, Gaussian Mixture Models, threshold-based segmentation, and volatility clustering. Integrates scikit-learn mixture, cluster, and decomposition modules.
version: 0.1.0
author: quant-kg-lab
license: MIT
metadata:
  hermes:
    tags: [quantitative-finance, regime-detection, market-regimes, hmm, gmm, clustering]
    related_skills: [scikit-learn-cluster, scikit-learn-decomposition, scikit-learn-gaussian-process]
---

# Market Regime Detection

Markets alternate between trending, mean-reverting, high-volatility, and low-volatility regimes. A strategy optimal in one regime may fail in another. Regime detection enables conditional strategy switching.

## Pattern 1: Gaussian Mixture Regimes

```python
from sklearn.mixture import GaussianMixture
import numpy as np

def detect_regimes_gmm(returns, volatility, n_regimes=3):
    """Cluster market states using GMM."""
    features = np.column_stack([
        returns.rolling(20).mean(),     # trend
        volatility.rolling(20).std(),   # vol
        returns.rolling(5).mean(),      # short-term momentum
    ])
    features = features[~np.isnan(features).any(axis=1)]
    
    gmm = GaussianMixture(n_components=n_regimes, random_state=42)
    labels = gmm.fit_predict(features)
    return labels, gmm.means_
```

## Pattern 2: PCA Dimensionality Reduction

Reduce correlated market indicators before clustering:

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def reduce_market_features(features, n_components=0.95):
    """PCA on market features, keeping 95% variance."""
    scaled = StandardScaler().fit_transform(features)
    pca = PCA(n_components=n_components)
    reduced = pca.fit_transform(scaled)
    return reduced, pca.explained_variance_ratio_
```

## Pattern 3: Volatility Clustering (HMM)

```python
from hmmlearn import hmm  # external library

def hmm_regimes(returns, n_states=2):
    """Hidden Markov Model for regime detection."""
    model = hmm.GaussianHMM(
        n_components=n_states,
        covariance_type="full",
        n_iter=1000
    )
    model.fit(returns.reshape(-1, 1))
    states = model.predict(returns.reshape(-1, 1))
    return states
```

## Graph Nodes Used

| Concept | Graph Node | Source |
|---------|------------|--------|
| GaussianMixture | `sklearn.mixture.GaussianMixture` | `sklearn/mixture/_gaussian_mixture.py` |
| PCA | `sklearn.decomposition.PCA` | `sklearn/decomposition/_pca.py` |
| StandardScaler | `sklearn.preprocessing.StandardScaler` | `sklearn/preprocessing/_data.py` |

## Pitfalls

1. **Look-ahead bias**: Compute features on expanding windows only — never use future data.
2. **Regime count selection**: Use BIC/AIC scores, not intuition. GMM's `bic()` method helps.
3. **Regime persistence**: Real regimes persist for weeks/months. Hourly regime switching = noise, not signal.
