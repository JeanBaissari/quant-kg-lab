---
name: quant-feature-engineering
description: "Use when creating features from price/volume data for ML models — technical indicators, statistical transforms, scaling, and dimensionality reduction."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [ta-lib-indicators, scikit-learn-preprocessing, scikit-learn-decomposition, scipy-stats, pandas-ts, numpy-core]
tags: [quantitative-finance, feature-engineering, ta-lib, scikit-learn, scipy, ML, workflow]
related_skills: [ta-lib-indicators, scikit-learn-preprocessing, scikit-learn-decomposition, scipy-stats, pandas-ts, numpy-core]
target_version: cross-lib
---

# Quant Feature Engineering (raw OHLCV -> indicators -> scaling -> model-ready features)

Raw price and volume data must be transformed into stationary, scaled, low-dimensional features
before feeding any ML model. This playbook chains technical indicators (ta-lib), statistical
transforms (scipy), and sklearn preprocessing into a leak-free feature pipeline.

## Steps

1. **Compute technical indicators** — `ta-lib-indicators`: RSI, MACD, SMA on numpy arrays.
   ta-lib is C-backed and operates on raw floats; wrap results back into a DataFrame.
   ```python
   import talib
   c = df["close"].to_numpy(dtype=np.float64)
   df["rsi_14"] = talib.RSI(c, 14)         # _ta_lib.c:L34584
   df["macd"], df["macd_signal"], df["macd_hist"] = talib.MACD(c)  # _ta_lib.c:L29064
   df["sma_20"] = talib.SMA(c, 20)         # _ta_lib.c:L35583
   ```
   *Citations*: `ta-lib/_ta_lib.c:L34584`, `ta-lib/_ta_lib.c:L29064`, `ta-lib/_ta_lib.c:L35583`
2. **Add statistical features** — `scipy-stats`, `numpy-core`: rolling z-scores, skew, kurtosis,
   returns, realized volatility. Everything computed point-in-time.
   ```python
   from scipy.stats import zscore
   df["ret_5d_z"] = df["ret"].rolling(20).apply(lambda x: zscore(x)[-1])  # stats/_stats_py.py:L2673
   ```
   *Citation*: `scipy/stats/_stats_py.py:L2673`
3. **Scale features** — `scikit-learn-preprocessing`: StandardScaler for z-normalization,
   MinMaxScaler for [0,1] bounded inputs. Fit on training data only.
   ```python
   from sklearn.preprocessing import StandardScaler
   scaler = StandardScaler()                # preprocessing/_data.py:L742
   X_train_scaled = scaler.fit_transform(X_train)
   X_test_scaled = scaler.transform(X_test) # no fit on test!
   ```
   *Citation*: `scikit-learn/preprocessing/_data.py:L742`
4. **Reduce dimensionality** — `scikit-learn-decomposition`: PCA to compress correlated indicators
   into orthogonal components. Keep enough components for 95% explained variance.
   ```python
   from sklearn.decomposition import PCA
   pca = PCA(n_components=0.95)             # decomposition/_pca.py:L113
   X_reduced = pca.fit_transform(X_train_scaled)
   ```
   *Citation*: `scikit-learn/decomposition/_pca.py:L113`
5. **Drop warmup NaNs** — ta-lib indicators have a warmup period (max lookback). Mask or drop the
   first N rows before any model fitting.
6. **Assemble the feature matrix** — concatenate indicators, statistical features, and PCA
   components into a single DataFrame. Verify no NaN/inf values remain.

## Pitfalls

1. **Lookahead bias** — scaling, PCA, and z-score transforms must be fit on training data only.
   Applying `.fit_transform()` on the full dataset leaks future information into features.
2. **Scaling mismatch** — StandardScaler assumes roughly Gaussian features; heavy-tailed financial
   returns can produce extreme scaled values. Use RobustScaler for fat-tailed distributions.
3. **Multicollinearity** — RSI, MACD, and SMA are correlated by construction. PCA helps, but
   interpretability is lost. Document which original indicators map to which components.
4. **Feature selection without validation** — selecting features by correlation with returns on the
   full sample is overfitting. Use walk-forward or purged cross-validation to select features.

## Composed Skills & Bridges

| Source | Target | Relation | Description |
|--------|--------|----------|-------------|
| ta-lib-indicators | scikit-learn-preprocessing | feeds_into | indicator arrays -> StandardScaler.fit_transform |
| scipy-stats | pandas-ts | extends | zscore/skew/kurtosis as rolling features |
| scikit-learn-decomposition | scikit-learn-preprocessing | chains | StandardScaler -> PCA pipeline |
| numpy-core | ta-lib-indicators | provides | raw float64 arrays for ta-lib functions |
| this playbook | quant-full-pipeline | feeds_into | feature matrix -> model training step |
| this playbook | quant-ml-strategy | generates | features -> model predictions -> signals |

## Related Skills

- [[ta-lib-indicators]]
- [[scikit-learn-preprocessing]]
- [[scikit-learn-decomposition]]
- [[scipy-stats]]
- [[pandas-ts]]
- [[numpy-core]]
