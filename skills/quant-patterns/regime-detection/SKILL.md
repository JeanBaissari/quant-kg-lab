---
name: quant-regime-detection
description: "Use when detecting market regimes for conditional strategy switching — Hidden Markov Models, Gaussian Mixture Models, threshold-based segmentation, and volatility clustering. Integrates scikit-learn mixture, cluster, and decomposition modules."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [scikit-learn-cluster, scikit-learn-decomposition, scikit-learn-gaussian-process]
tags: [quantitative-finance, regime-detection, market-regimes, hmm, gmm, clustering]
related_skills: [scikit-learn-cluster, scikit-learn-decomposition, scikit-learn-gaussian-process]
target_version: cross-lib
---

# Market Regime Detection

Markets alternate between trending, mean-reverting, high-volatility, and low-volatility regimes. A strategy optimal in one regime may fail in another. Regime detection enables conditional strategy switching.

## Steps

1. **Build regime features** — rolling trend (20-bar return mean), volatility (20-bar std), and short-term momentum (5-bar return mean), all point-in-time.
2. **Reduce dimensionality** — `scikit-learn-preprocessing` (`StandardScaler`) + `scikit-learn-decomposition` (`PCA`, keep 95% variance). Graph nodes: `sklearn.preprocessing.StandardScaler` (`sklearn/preprocessing/_data.py`), `sklearn.decomposition.PCA` (`sklearn/decomposition/_pca.py`).
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
3. **Cluster market states with a GMM** — `GaussianMixture` groups the feature vectors into `n_regimes` regime states; `scikit-learn-cluster` covers the neighboring clustering APIs. Graph node: `sklearn.mixture.GaussianMixture` (`sklearn/mixture/_gaussian_mixture.py`).
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
4. **Hidden Markov Model for volatility regimes** — `hmmlearn` (external library) models the hidden state sequence explicitly, including state transitions.
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
5. **Validate the regime count** — score candidate `n_regimes` with `GaussianMixture.bic()`/AIC and pick the minimum; then sanity-check regime persistence before switching strategy logic on it.

## Pitfalls

1. **Look-ahead bias**: Compute features on expanding windows only — never use future data.
2. **Regime count selection**: Use BIC/AIC scores, not intuition. GMM's `bic()` method helps.
3. **Regime persistence**: Real regimes persist for weeks/months. Hourly regime switching = noise, not signal.

## Composed Skills & Bridges

| Skill / Bridge | Role in this workflow |
|----------------|-----------------------|
| `scikit-learn-cluster` | regime-state clustering family around GMM (Step 3) |
| `scikit-learn-decomposition` | PCA dimensionality reduction (Step 2) |
| `scikit-learn-preprocessing` | `StandardScaler` before PCA (Step 2) |
| `scikit-learn-gaussian-process` | composes — Gaussian-process machinery for regime models |
| `numpy-core` | feature matrix assembly (Steps 1, 3) |
