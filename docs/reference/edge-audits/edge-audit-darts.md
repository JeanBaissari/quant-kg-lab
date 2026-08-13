# Edge Audit — darts

**Date**: 2026-08-13

## Summary

- Total edges: 8238
- EXTRACTED: 4864 (59.0%)
- INFERRED: 3374 (41.0%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `PLForecastingModule`: 250 inferred edges
- `SeriesType`: 242 inferred edges
- `Likelihood`: 184 inferred edges
- `LikelihoodType`: 179 inferred edges
- `SequentialEncoder`: 154 inferred edges
- `GlobalForecastingModel`: 148 inferred edges
- `Pipeline`: 126 inferred edges
- `ForecastingModel`: 115 inferred edges
- `TorchLikelihood`: 107 inferred edges
- `MixedCovariatesTorchModel`: 101 inferred edges
- `QuantileRegression`: 85 inferred edges
- `TorchForecastingModel`: 72 inferred edges
- `CovariatesIndexGenerator`: 69 inferred edges
- `Encoder`: 69 inferred edges
- `FutureCovariatesIndexGenerator`: 69 inferred edges
- `PastCovariatesIndexGenerator`: 69 inferred edges
- `SequentialEncoderTransformer`: 69 inferred edges
- `SingleEncoder`: 69 inferred edges
- `DatasetLoaderCSV`: 65 inferred edges
- `DatasetLoaderMetadata`: 65 inferred edges

## Cross-Module Suspicious Edges

- `forecasting` ↔ `likelihood_models`: 511
- `forecasting` ↔ `ts_utils.py`: 168
- `forecasting` ↔ `encoders`: 147
- `datasets.py` ↔ `dataset_loaders.py`: 130
- `forecasting` ↔ `pipeline.py`: 106
- `forecasting` ↔ `components`: 68
- `forecasting` ↔ `data`: 62
- `__init__.py` ↔ `forecasting`: 57
- `forecasting` ↔ `multioutput.py`: 37
- `anomaly_model` ↔ `scorers`: 34
- `__init__.py` ↔ `datasets.py`: 27
- `utils.py` ↔ `ts_utils.py`: 22
- `shap_adapters` ↔ `forecasting`: 22
- `historical_forecasts` ↔ `pipeline.py`: 19
- `historical_forecasts` ↔ `timeseries.py`: 19
- `historical_forecasts` ↔ `ts_utils.py`: 19
- `transformers` ↔ `ts_utils.py`: 18
- `statistics.py` ↔ `likelihood_models`: 17
- `tft_explainer.py` ↔ `ts_utils.py`: 15
- `shap_explainer.py` ↔ `explainability_result.py`: 14
