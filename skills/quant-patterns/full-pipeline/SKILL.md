---
name: quant-full-pipeline
description: "Use when building an end-to-end quantitative research loop — from raw OHLCV data through features, model, backtest, hyperparameter search, and risk analysis — composing the whole quant stack."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [quant-factor-research, quant-ml-strategy, quant-walk-forward-validation]
tags: [quantitative-finance, pipeline, backtesting, feature-engineering, workflow]
related_skills: [quant-factor-research, quant-ml-strategy, quant-walk-forward-validation]
---

# Quant Full Pipeline (data → features → model → backtest → HPO → risk)

The canonical research loop. Each stage is a library the repo already covers; this playbook is the
connective tissue that chains them. Load the per-stage skill (see **Composed Skills** below) for
the API detail of any single step.

```
pandas ──▶ ta-lib ──▶ scipy/numpy ──▶ sklearn/xgboost ──▶ vectorbt ──▶ optuna ──▶ risk
 (data)   (indicators)  (features)       (model)          (backtest)   (HPO)     (analysis)
```

## Steps

1. **Load & align data** — `pandas` (`pandas-core`, `pandas-ts`). Parse dates, set a monotonic
   `DatetimeIndex`, forward-fill gaps, resample to the trading frequency.
   ```python
   df = pd.read_csv("ohlcv.csv", parse_dates=["date"], index_col="date").sort_index()
   df = df.asfreq("1D").ffill()
   ```
2. **Engineer indicators** — `ta-lib` (`ta-lib-indicators`). Compute the indicator panel on numpy
   arrays; mind the warmup NaNs.
   ```python
   import talib, numpy as np
   c = df["close"].to_numpy(np.float64)
   feat = pd.DataFrame({"rsi": talib.RSI(c, 14), "atr": talib.ATR(df.high, df.low, c, 14)}, index=df.index)
   ```
3. **Add statistical features** — `numpy`/`scipy` (`scipy-stats`): rolling z-scores, returns,
   volatility, rank/entropy features. Keep everything point-in-time (no look-ahead).
4. **Label & split (leak-free)** — build forward-return labels, then split with
   `quant-walk-forward-validation` (never a shuffled k-fold on time series).
5. **Train a model** — `scikit-learn-ensemble` or `xgboost-sklearn`. Fit on the training window,
   predict the next window; collect out-of-sample predictions across folds.
6. **Convert predictions → signals → portfolio** — `vectorbt` (`vectorbt-signals`,
   `vectorbt-portfolio`). Map probabilities/scores to entries/exits, then simulate.
   ```python
   entries = preds > preds.quantile(0.8); exits = preds < preds.quantile(0.2)
   pf = vbt.Portfolio.from_signals(df["close"], entries, exits, fees=0.001, freq="1D")
   ```
7. **Optimize the whole loop** — `optuna` (`optuna-study`). The objective *re-runs steps 2–6* and
   returns a risk-adjusted metric (Sharpe/Calmar) computed on the walk-forward OOS folds, never
   on in-sample data.
   ```python
   def objective(trial):
       rsi_n = trial.suggest_int("rsi_n", 5, 30)
       thr   = trial.suggest_float("entry_q", 0.6, 0.95)
       return walk_forward_sharpe(rsi_n, thr)   # steps 2–6 inside
   study = optuna.create_study(direction="maximize"); study.optimize(objective, n_trials=100)
   ```
8. **Risk analysis** — `vectorbt-portfolio` stats + `scipy-stats` (bootstrap CIs on Sharpe,
   drawdown distribution). Report OOS metrics with confidence intervals, not a single number.

## Pitfalls

1. **Look-ahead leakage** is the #1 killer: indicators, scaling, and labels must all be computed
   point-in-time. Fit scalers inside each training fold only.
2. **Optimizing on in-sample data** inflates Sharpe. The Optuna objective must score OOS folds.
3. **Warmup NaNs** from ta-lib propagate into features/labels — drop or mask the first `max(period)` bars.
4. **Overfitting the HPO** — cap `n_trials`, prefer robust metrics (median OOS Sharpe), and hold out a final untouched test period.
5. **Fees/slippage** materially change results — always set `fees`/`slippage` in `Portfolio.from_signals`.

## Composed Skills & Bridges

| Stage | Skill | Bridge (relation) |
|-------|-------|-------------------|
| data | `pandas-core`, `pandas-ts` | pandas.DataFrame → everything (data source) |
| indicators | `ta-lib-indicators` | ta-lib.RSI → vectorbt.SignalFactory (generates) |
| features | `scipy-stats`, `numpy-core` | numpy.ndarray → sklearn (fit input) |
| model | `scikit-learn-ensemble`, `xgboost-sklearn` | sklearn/xgb → vectorbt signals (powers) |
| backtest | `vectorbt-signals`, `vectorbt-portfolio` | pandas.DataFrame → vectorbt.Portfolio (input) |
| HPO | `optuna-study` | vectorbt/model params → optuna.Study (optimized_by) |
| validation | `quant-walk-forward-validation` | sklearn.TimeSeriesSplit + purge/embargo |
