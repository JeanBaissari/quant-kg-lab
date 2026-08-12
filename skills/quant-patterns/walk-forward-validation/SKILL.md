---
name: quant-walk-forward-validation
description: "Use when implementing walk-forward validation, time-series cross-validation, or rolling/expanding window backtesting for trading strategies. Integrates scikit-learn TimeSeriesSplit with custom purging/embargo logic."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [scikit-learn-model-selection, optuna-study]
tags: [quantitative-finance, backtesting, walk-forward, time-series, cross-validation]
related_skills: [scikit-learn-model-selection, optuna-study]
---

# Walk-Forward Validation for Trading Strategies

Standard k-fold cross-validation leaks future information in time-series data. Walk-forward validation (also called backtesting or time-series CV) preserves temporal order by training on past data and testing on future data.

## Steps

1. **Set up sequential splits** — `scikit-learn-model-selection`: `TimeSeriesSplit` trains on the past and tests on the future. Graph node: `sklearn.model_selection.TimeSeriesSplit` (`sklearn/model_selection/_split.py`).
2. **Add purging** — remove training samples that overlap the test period; the purge window must cover the label horizon.
3. **Add an embargo** — leave a gap between the last train sample and the test window to kill leakage from autocorrelated returns.
4. **Run the walk-forward loop** — fit on train, predict test, across all folds, with optional purging inline:
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
   For sparse label horizons, combinatorial purge — cross-validating over multiple purge windows — is the advanced pattern.
5. **Tune the protocol itself with Optuna** — `optuna-study`: search the purge window and fold count as part of the HPO objective. Graph node: `optuna.study.Study.optimize` (`optuna/study/study.py`).
   ```python
   import optuna

   def objective(trial):
       purge_window = trial.suggest_int("purge_window", 0, 30)
       n_splits = trial.suggest_int("n_splits", 3, 10)
       # ... walk-forward validate and return Sharpe
   ```

## Pitfalls

1. **Default CV shuffle=True leaks**: Never shuffle time-series data in CV.
2. **Stationarity assumption**: Walk-forward assumes regime stability within windows.
3. **Purge window sizing**: Too small → leakage; too large → insufficient training data.

## Composed Skills & Bridges

| Skill / Bridge | Role in this workflow |
|----------------|-----------------------|
| `scikit-learn-model-selection` | `TimeSeriesSplit` sequential folds (Steps 1, 4) |
| `optuna-study` | tune purge/embargo protocol inside HPO (Step 5) |
| `quant-full-pipeline` | consumer playbook — leak-free split stage of the research loop |
| `quant-factor-research` | consumer playbook — OOS IC/importance validation |
| `quant-ml-strategy` | consumer playbook — OOS model predictions |
| `quant-hpo-optimization` | consumer playbook — walk-forward HPO objective |
