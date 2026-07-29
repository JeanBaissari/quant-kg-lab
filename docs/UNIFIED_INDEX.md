# Unified Quant Knowledge Index

> **Authoritative cross-library reference for quantitative research & development.**
> Every entry links to a knowledge graph node or spec-driven skill.
> Updated: 2026-07-29 | Libraries indexed: 11 | Skills: 21 (target: 47)

---

## Library Index

### Foundation Layer — Numerical Computing

| Library | Graph | Skills | Core Abstractions |
|---------|-------|--------|-------------------|
| **numpy** | 🔄 Extracting | ⬜ 3 planned | `ndarray`, `linalg`, `random` |
| **scipy** | 🔄 Extracting | ⬜ 3 planned | `optimize`, `stats`, `signal` |
| **pandas** | 🔄 Extracting | ⬜ 2 planned | `DataFrame`, `Series`, `GroupBy` |

### ML & Optimization Layer

| Library | Graph | Skills | Core Abstractions |
|---------|-------|--------|-------------------|
| **scikit-learn** | ✅ 18,753 nodes | ✅ 15 skills | `BaseEstimator`, `Pipeline`, `GridSearchCV` |
| **optuna** | ✅ 3,912 nodes | 🔄 1→8 skills | `Study`, `BaseDistribution`, `TPESampler` |
| **xgboost** | 🔄 Extracting | ⬜ 2 planned | `DMatrix`, `XGBClassifier`, `Booster` |
| **lightgbm** | 🔄 Extracting | ⬜ 2 planned | `Dataset`, `LGBMClassifier`, `Booster` |

### Quant Tools Layer

| Library | Graph | Skills | Core Abstractions |
|---------|-------|--------|-------------------|
| **vectorbt** | 🔄 Extracting | ⬜ 3 planned | `Portfolio`, `SignalFactory`, `IndicatorFactory` |
| **ta-lib** | 🔄 Extracting | ⬜ 1 planned | 200+ technical indicators |
| **backtrader** | 🔄 Extracting | ⬜ 2 planned | `Cerebro`, `Strategy`, `DataFeed` |

---

## Quant Workflow Patterns

### Pattern 1: Strategy Development Loop
```
pandas (data) → ta-lib (indicators) → scikit-learn (feature selection)
    → xgboost (model) → vectorbt (backtest) → optuna (optimize)
    → backtrader (live) → pyfolio (analysis)
```

### Pattern 2: Factor Research
```
pandas (universe) → numpy (factor computation) → scipy.stats (significance)
    → sklearn.ensemble (importance ranking) → alphalens (IC analysis)
```

### Pattern 3: Hyperparameter Optimization
```
sklearn.model_selection (param grid) → optuna.Study (Bayesian search)
    → optuna.samplers.TPESampler (surrogate model) → vectorbt (evaluation)
```

### Pattern 4: Regime-Aware Allocation
```
sklearn.mixture.GMM (regime detection) → sklearn.covariance.LedoitWolf (risk)
    → cvxpy (constrained optimization) → pyfolio (tear sheet)
```

---

## Concept Index

### A — Arrays & Data Structures
- `numpy.ndarray` → [graph: numpy] N-dimensional array backbone
- `pandas.DataFrame` → [graph: pandas] Labeled 2D data structure
- `pandas.Series` → [graph: pandas] 1D labeled array
- `xgboost.DMatrix` → [graph: xgboost] Optimized data structure for XGBoost
- `lightgbm.Dataset` → [graph: lightgbm] Optimized data structure for LightGBM

### B — Backtesting
- `vectorbt.Portfolio.from_signals` → [graph: vectorbt] Vectorized portfolio simulation
- `vectorbt.Portfolio.from_orders` → [graph: vectorbt] Order-based backtesting
- `backtrader.Cerebro` → [graph: backtrader] Event-driven backtesting engine
- `backtrader.Strategy` → [graph: backtrader] Base strategy class

### C — Cross-Validation
- `sklearn.model_selection.TimeSeriesSplit` → [skill: sklearn/model_selection] Temporal CV
- `sklearn.model_selection.GridSearchCV` → [skill: sklearn/model_selection] Exhaustive param search
- Walk-Forward Validation → [skill: quant-patterns/walk-forward-validation]

### D — Distributions & Sampling
- `optuna.distributions.FloatDistribution` → [skill: optuna/samplers] Continuous parameter space
- `optuna.samplers.TPESampler` → [skill: optuna/samplers] Bayesian optimization sampler
- `scipy.stats` → [graph: scipy] Statistical distributions + tests

### E — Ensembles
- `sklearn.ensemble.RandomForestClassifier` → [skill: sklearn/ensemble]
- `sklearn.ensemble.GradientBoostingClassifier` → [skill: sklearn/ensemble]
- `xgboost.XGBClassifier` → [graph: xgboost] sklearn-compatible gradient boosting
- `lightgbm.LGBMClassifier` → [graph: lightgbm] Microsoft's gradient boosting

### F — Feature Engineering
- `sklearn.preprocessing.StandardScaler` → [skill: sklearn/preprocessing]
- `sklearn.preprocessing.OneHotEncoder` → [skill: sklearn/preprocessing]
- `ta-lib` indicators → [graph: ta-lib] 200+ technical indicators
- `sklearn.feature_selection.SelectKBest` → [skill: sklearn/feature_selection]

### G — Gaussian Processes
- `sklearn.gaussian_process.GaussianProcessRegressor` → [skill: sklearn/gaussian_process]
- `sklearn.gaussian_process.kernels.RBF` → [skill: sklearn/gaussian_process]

### H — Hyperparameter Optimization
- `optuna.Study.optimize` → [skill: optuna/study]
- `optuna.pruners.MedianPruner` → [skill: optuna/pruners] ⬜
- Bayesian Optimization Pattern → [skill: quant-patterns/hpo-optimization]

### I — Imputation
- `sklearn.impute.SimpleImputer` → [skill: sklearn/impute]
- `sklearn.impute.KNNImputer` → [skill: sklearn/impute]

### L — Linear Models
- `sklearn.linear_model.LinearRegression` → [skill: sklearn/linear_model]
- `sklearn.linear_model.LogisticRegression` → [skill: sklearn/linear_model]
- `sklearn.linear_model.Ridge` → [skill: sklearn/linear_model]
- `sklearn.linear_model.Lasso` → [skill: sklearn/linear_model]

### M — Metrics
- `sklearn.metrics.accuracy_score` → [skill: sklearn/metrics]
- `sklearn.metrics.mean_squared_error` → [skill: sklearn/metrics]
- `sklearn.metrics.r2_score` → [skill: sklearn/metrics]

### O — Optimization
- `scipy.optimize.minimize` → [graph: scipy] General-purpose optimization
- `optuna.create_study` → [skill: optuna/study]
- `cvxpy` (future) → Portfolio optimization

### P — Portfolio Construction
- Risk Parity → [skill: quant-patterns/portfolio-construction]
- Kelly Criterion → [skill: quant-patterns/portfolio-construction]
- Minimum Variance → [skill: quant-patterns/portfolio-construction]

### R — Regime Detection
- `sklearn.mixture.GaussianMixture` → [skill: sklearn/cluster]
- `sklearn.cluster.KMeans` → [skill: sklearn/cluster]
- HMM Regimes → [skill: quant-patterns/regime-detection]

### S — Signal Processing
- `scipy.signal` → [graph: scipy] Filtering, detrending, spectral analysis
- `numpy.fft` → [graph: numpy] Frequency domain analysis
- `vectorbt.SignalFactory` → [graph: vectorbt] Signal generation framework

### T — Technical Indicators
- `ta-lib.SMA` → [graph: ta-lib] Simple Moving Average
- `ta-lib.RSI` → [graph: ta-lib] Relative Strength Index
- `ta-lib.MACD` → [graph: ta-lib] Moving Average Convergence Divergence
- `ta-lib.BBANDS` → [graph: ta-lib] Bollinger Bands

---

## Graph Statistics

| Library | Nodes | Edges | Communities | God Node | Coverage |
|---------|-------|-------|-------------|----------|----------|
| scikit-learn | 18,753 | 49,978 | 1,149 | BaseEstimator (2,309°) | 88.9% |
| optuna | 3,912 | 8,405 | 228 | Study (228°) | 0% |
| numpy | — | — | — | — | 🔄 |
| scipy | — | — | — | — | 🔄 |
| pandas | — | — | — | — | 🔄 |
| vectorbt | — | — | — | — | 🔄 |
| ta-lib | — | — | — | — | 🔄 |
| backtrader | — | — | — | — | 🔄 |
| xgboost | — | — | — | — | 🔄 |
| lightgbm | — | — | — | — | 🔄 |

**Total**: 22,665 nodes | 58,383 edges | 1,377 communities (extracted so far)
