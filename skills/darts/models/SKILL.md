---
name: darts-models
description: "Use when choosing a darts forecasting model — the model zoo (naive/statistical/ML/deep/ensemble/conformal families), fit/predict contract, and covariates support."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: unit8co/darts
source_commit: 080b5340366b8df25e048f4cfd11ca99e3806e97
extraction_date: 2026-08-13
graph:
  nodes: 3954
  edges: 8240
  community_count: 245
  graph_hash: 4deb706235a6ae4a
tags:
- darts
- models
- forecasting
- deep-learning
related_skills:
- darts
- darts-timeseries
- darts-backtesting
- statsmodels-tsa
- pymc-distributions
- optuna-study
---

# darts.models

The model zoo: `ForecastingModel` (base) with local (statistical), global (ML/deep),
ensemble, and conformal families — a unified `fit(series)` → `predict(n)` contract
across every model.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `ForecastingModel` | `models/forecasting/forecasting_model.py:L133` | Base class — fit/predict/historical_forecasts (deg 181 hub) |
| `GlobalForecastingModel` | `models/forecasting/forecasting_model.py:L2979` | Global models — train across many series |
| `LocalForecastingModel` | `models/forecasting/forecasting_model.py:L2906` | Local statistical models (per-series) |
| `TorchForecastingModel` | `models/forecasting/torch_forecasting_model.py:L161` | PyTorch deep models — PLForecastingModule-backed |
| `PLForecastingModule` | `models/forecasting/pl_forecasting_module.py:L76` | Lightning wrapper — the deep-model engine (deg 283 hub) |
| `SKLearnModel` | `models/forecasting/sklearn_model.py:L101` | sklearn regressors as forecasters (wrapping) |
| `SKLearnModelWithCategoricalFeatures` | `models/forecasting/sklearn_model.py:L1629` | sklearn wrapper with categorical covariate support |
| `CatBoostModel` | `models/forecasting/catboost_model.py` | CatBoost forecaster — native categoricals |
| `LightGBMModel` | `models/forecasting/lightgbm_model.py` | LightGBM forecaster |
| `LinearRegressionModel` | `models/forecasting/linear_regression_model.py` | Linear regression forecaster |
| `RandomForest` | `models/forecasting/random_forest.py` | Random forest forecaster |
| `XGBModel` | `models/forecasting/xgboost_model.py` | XGBoost forecaster |
| `NBEATSModel` | `models/forecasting/nbeats.py` | N-BEATS — deep basis-expansion forecaster |
| `NHiTSModel` | `models/forecasting/nhits.py` | N-HiTS — hierarchical interpolation, multi-horizon |
| `TCNModel` | `models/forecasting/tcn_model.py` | Temporal convolution network |
| `BlockRNNModel` | `models/forecasting/block_rnn_model.py` | Block RNN — LSTM/GRU forecasters |
| `DLinearModel` | `models/forecasting/dlinear.py` | DLinear — linear decomposition forecaster |
| `NLinearModel` | `models/forecasting/nlinear.py` | NLinear — normalization + linear |
| `PatchTSTFMModel` | `models/forecasting/patch_tst.py` | PatchTST foundation-style transformer |
| `Chronos2Model` | `models/forecasting/chronos2_model.py` | Chronos2 — LLM-style token forecasting |
| `NeuralForecastModel` | `models/forecasting/neuralforecast_model.py` | NeuralForecast integration |
| `StatsForecastModel` | `models/forecasting/sf_model.py:L39` | StatsForecast integration |
| `FoundationModel` | `models/forecasting/foundation_model.py:L20` | Foundation-model adapter (zero-shot) |
| `EnsembleModel` | `models/forecasting/ensemble_model.py:L43` | Ensemble of forecasters |
| `NaiveEnsembleModel` | `models/forecasting/naive_ensemble_model.py` | Simple averaging ensemble |
| `ConformalModel` | `models/forecasting/conformal_models.py:L62` | Conformal prediction — prediction intervals |
| `ConformalQRModel` | `models/forecasting/conformal_models.py` | Conformal via quantile regression |
| `ConformalNaiveModel` | `models/forecasting/conformal_models.py` | Conformal via naive residual bounds |
| `GlobalNaiveDrift` | `models/forecasting/global_baseline_models.py` | Naive-with-drift baseline (curated M2b) |
| `MultivariateModel` | `models/forecasting/multivariate_model.py` | Multivariate-capable base |
| `MixedCovariatesTorchModel` | `models/forecasting/torch_forecasting_model.py:L3177` | Deep model with past+future covariates |
| `PastCovariatesTorchModel` | `models/forecasting/torch_forecasting_model.py:L3081` | Deep model with past covariates only |

## Common Patterns

- **Baseline first**: `NaiveDrift`/`ExponentialSmoothing`/`Theta` — establish the
  beatable baseline before any ML model.
- **ML forecaster**: `LinearRegressionModel(lags=14, output_chunk_length=7)` — fast,
  interpretable, good default for tabular factor data.
- **Boosting**: `CatBoostModel(lags=14)` — native categorical covariates (calendar
  features as categories).
- **Deep**: `NHiTSModel(input_chunk_length=24, output_chunk_length=12)` for
  multi-horizon; `TCNModel`/`BlockRNNModel` for sequences.
- **Intervals**: `ConformalModel(base_model)` — calibrated prediction intervals
  without bespoke quantile training.
- **Ensembles**: `EnsembleModel([m1, m2, m3])` — average the zoo for robustness.
- **Covariates**: past covariates (lags) vs future covariates (calendar) — declare
  which the model family supports (`supports_past_covariates`/`_future_`).
- **Zero-shot**: `FoundationModel`/`Chronos2Model` — no training for quick
  baselines; verify horizon fit.

## Pitfalls

- **Deep models need scaled data**: torch models expect normalized inputs — use
  `darts.utils.scalers` before fit and inverse after predict.
- **input vs output chunk**: `input_chunk_length` (lookback) and
  `output_chunk_length` (horizon) define the deep-model window — mismatches silently
  truncate the effective forecast horizon.
- **Global models need many series**: a global model on one series ≈ a local model —
  the benefit only appears across a series corpus.
- **Ensemble composition**: mixed family types (local+deep) can double training time —
  budget wall-clock.
- **Determinism**: torch models seed via `torch.manual_seed` — set it per run for
  reproducible forecasts.
- **Covariate support varies**: check `supports_past_covariates` /
  `supports_future_covariates` per model BEFORE building the pipeline.

## Provenance

Graph: `knowledge_graphs/darts/.graphify/graph.json` — 3954 nodes · 8240 edges ·
245 communities · graphify @ 080b5340366b, backend opencode, description coverage 85.2%,
2 curated M2b entries (ADR-0008).

## Verification Checklist

- [ ] `LinearRegressionModel(lags=14).fit(series).predict(7)` runs end-to-end
- [ ] `ConformalModel(LinearRegressionModel(lags=14)).fit(series)` yields intervals
- [ ] QR rows cite `models/forecasting/*.py` files resolvable in the darts graph
