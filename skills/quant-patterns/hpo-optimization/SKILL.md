---
name: quant-hpo-optimization
description: "Use when tuning trading strategy hyperparameters via Bayesian optimization — Optuna study lifecycle, sampler selection, pruning strategies, and distributed parallel sweeps for walk-forward backtesting."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [optuna-samplers, optuna-study, scikit-learn-model-selection, quant-walk-forward-validation]
tags: [quantitative-finance, hyperparameter-optimization, bayesian-optimization, backtesting]
related_skills: [optuna-samplers, optuna-study, scikit-learn-model-selection, quant-walk-forward-validation]
---

# Hyperparameter Optimization for Trading Strategies

Trading strategies have more hyperparameters than ML models — entry/exit thresholds, lookback windows, stop-loss distances, position sizing rules. Grid search is combinatorially explosive. Bayesian optimization (Optuna) is the standard.

## Steps

1. **Define the objective: strategy hyperparameters + walk-forward scoring** — `optuna-study` + `scikit-learn-model-selection`. Every strategy knob becomes a `suggest_*` call; the objective value is the mean OOS Sharpe across `TimeSeriesSplit` windows (never a shuffled fold — see `quant-walk-forward-validation`). Report progress per window and prune weak trials early. Graph nodes: `optuna.study.Study` (`optuna/study/study.py`), `sklearn.model_selection.TimeSeriesSplit` (`sklearn/model_selection/_split.py`).
   ```python
   import optuna
   from sklearn.model_selection import TimeSeriesSplit

   def objective(trial):
       # Strategy hyperparameters
       entry_threshold = trial.suggest_float("entry_z", -3.0, -0.5)
       exit_threshold = trial.suggest_float("exit_z", 0.5, 3.0)
       stop_loss = trial.suggest_float("stop_loss", 0.01, 0.10)
       lookback = trial.suggest_int("lookback", 10, 200)
       
       # Walk-forward validation across time windows
       tscv = TimeSeriesSplit(n_splits=5)
       sharpes = []
       for train_idx, test_idx in tscv.split(data):
           sharpe = backtest_window(
               data[train_idx], data[test_idx],
               entry_threshold, exit_threshold, stop_loss, lookback
           )
           sharpes.append(sharpe)
           trial.report(np.mean(sharpes), step=len(sharpes))
           
           # Prune if clearly underperforming
           if trial.should_prune():
               raise optuna.TrialPruned()
       
       return np.mean(sharpes)
   ```
2. **Configure the study: sampler + pruner, then optimize** — `optuna-samplers` + `optuna-study`. A seeded `TPESampler` makes the sweep reproducible; a `MedianPruner` stops bad trials before they burn walk-forward compute. Graph nodes: `optuna.samplers.TPESampler` (`optuna/samplers/_tpe`), `optuna.pruners.MedianPruner` (`optuna/pruners/_median`).
   ```python
   study = optuna.create_study(
       direction="maximize",
       sampler=optuna.samplers.TPESampler(seed=42),
       pruner=optuna.pruners.MedianPruner(n_startup_trials=5)
   )
   study.optimize(objective, n_trials=500)
   ```
3. **Pick the sampler for your search regime** — `optuna-samplers`:

   | Scenario | Sampler | Why |
   |----------|---------|-----|
   | <50 trials, exploration | `RandomSampler` | TPE needs warm-up |
   | 50-500 trials, continuous params | `TPESampler` | Best general-purpose |
   | >500 trials, <20 params | `BoTorchSampler` | GP-based, sample-efficient |
   | Multi-objective (Sharpe + maxDD) | `NSGAIISampler` | Pareto-front optimization |
   | Categorical params dominant | `TPESampler` | Handles categorical well |

## Pitfalls

1. **Overfitting to walk-forward windows**: Tuning on all windows simultaneously leaks future information. Use rolling or anchored walk-forward.
2. **Pruner aggression**: MedianPruner kills trials too early on noisy Sharpe ratios. Use `n_startup_trials >= 10` for financial data.
3. **Single-objective vs multi-objective**: Optimizing Sharpe alone ignores drawdown. Use `NSGAIISampler` with `directions=["maximize", "minimize"]` for Sharpe + maxDD.

## Composed Skills & Bridges

| Skill / Bridge | Role in this workflow |
|----------------|-----------------------|
| `optuna-study` | study lifecycle — objective, `create_study`, `optimize` (Steps 1–2) |
| `optuna-samplers` | search strategy per regime — TPE/random/BoTorch/NSGA-II (Steps 2–3) |
| `optuna-pruners` | early stopping of weak trials via `MedianPruner` (Step 2) |
| `scikit-learn-model-selection` | `TimeSeriesSplit` walk-forward folds (Step 1) |
| `quant-walk-forward-validation` | leak-free OOS protocol the objective must follow (Step 1) |
| `quant-full-pipeline` | consumer playbook — HPO is the optimize stage of the research loop |
