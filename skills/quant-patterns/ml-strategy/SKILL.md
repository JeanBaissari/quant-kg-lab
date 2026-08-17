---
name: quant-ml-strategy
description: "Use when turning a machine-learning model into a tradable strategy — mapping predictions to positions, backtesting on an execution engine, tuning with HPO, and sizing with risk controls."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [quant-full-pipeline, quant-portfolio-construction, quant-walk-forward-validation]
tags: [quantitative-finance, machine-learning, strategy, backtesting, workflow]
related_skills: [quant-full-pipeline, quant-portfolio-construction, quant-walk-forward-validation]
target_version: cross-lib
---

# Quant ML Strategy (model → signal → execution → HPO → sizing)

Bridges the ML world (sklearn/xgboost/lightgbm) and the execution world (vectorbt/backtrader). The
crux is the mapping from model output to positions, and evaluating it without leakage.

## Steps

1. **Train the predictive model** — `scikit-learn-ensemble`, `xgboost-sklearn`, or
   `lightgbm-sklearn`. Target a tradable label (sign of forward return, triple-barrier, or a
   volatility-scaled return). Produce out-of-sample predictions via `quant-walk-forward-validation`.
2. **Map predictions → positions** — thresholds on probability, quantile ranks (long top decile /
   short bottom), or a continuous position ∝ expected return / variance. Keep it monotonic and simple.
   ```python
   pos = np.sign(pred) * np.clip(np.abs(pred) / pred.std(), 0, 1)   # vol-scaled position
   ```
3. **Backtest on an engine**:
   - **Vectorized** — `vectorbt-portfolio` (`Portfolio.from_signals`/`from_orders`) for fast sweeps.
   - **Event-driven** — `backtrader-core` (`Cerebro`/`Strategy`) when you need order types, partial
     fills, or realistic intrabar logic.
4. **Size with risk controls** — `quant-portfolio-construction`: volatility targeting, position
   caps, and (for multi-asset) a covariance-aware allocation instead of equal weight.
5. **Tune end-to-end** — `optuna-study`: search model hyperparameters *and* the signal-mapping
   thresholds together, scoring risk-adjusted OOS performance (not accuracy — accuracy ≠ PnL).
   ```python
   def objective(trial):
       params = {"max_depth": trial.suggest_int("max_depth", 2, 8),
                 "n_estimators": trial.suggest_int("n_estimators", 100, 800)}
       q = trial.suggest_float("long_q", 0.6, 0.95)
       return walk_forward_calmar(params, q)
   ```

## Pitfalls

1. **Accuracy is not PnL** — optimize a financial objective (Sharpe/Calmar/turnover-penalized return), never classification accuracy.
2. **Label leakage via overlapping windows** — with horizon-*h* labels, purge/embargo *h* bars around each test fold (`quant-walk-forward-validation`).
3. **Position mapping overfitting** — a hand-tuned threshold per period is curve-fitting; tune it inside the HPO across folds.
4. **Vectorbt vs backtrader mismatch** — vectorized fills assume close-to-close; if your live execution differs, validate the winner in backtrader before trusting it.
5. **Ignoring turnover/costs** — an ML edge is often eaten by transaction costs; include fees and a turnover penalty in the objective.

## Composed Skills & Bridges

| Stage | Skill | Bridge (relation) |
|-------|-------|-------------------|
| model | `scikit-learn-ensemble`, `xgboost-sklearn`, `lightgbm-sklearn` | sklearn-compatible API |
| signal | (this playbook) | model.predict → positions |
| backtest | `vectorbt-portfolio`, `backtrader-core` | predictions → Portfolio (predicts_for) |
| sizing | `quant-portfolio-construction` | covariance → weights |
| HPO | `optuna-study` | xgboost.train / params → optuna.Study (optimized_by) |
| validation | `quant-walk-forward-validation` | purge/embargo OOS |

## Related Skills

- [[quant-full-pipeline]]
- [[quant-portfolio-construction]]
- [[quant-walk-forward-validation]]
