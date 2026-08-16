# Graph Report - knowledge_graphs/darts/repo/darts  (2026-08-13)

## Corpus Check
- 173 files · ~347,746 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3954 nodes · 8240 edges · 245 communities detected
- Non-singleton communities: 245
- Extraction: EXTRACTED: 59.0% · INFERRED: 40.9%
- Edge kinds: calls: 730 · contains: 632 · imports: 2 · imports_from: 107 · inherits: 305 · method: 1655 · rationale_for: 1435 · uses: 3374

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 173 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `080b534`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `PLForecastingModule` (283)
- `SeriesType` (250)
- `Likelihood` (194)
- `TimeSeries` (194)
- `ForecastingModel` (181)
- `LikelihoodType` (181)
- `SequentialEncoder` (180)
- `GlobalForecastingModel` (160)
- `Pipeline` (142)
- `TorchForecastingModel` (142)

## Surprising Connections (you probably didn't know these)
- `Base Forecasting Model Explainer --------------------------------  A `_Forecasti` --uses--> `ForecastingModel`  [INFERRED]
  explainability/explainability.py → models/forecasting/forecasting_model.py
- `Explains a foreground time series, and returns a :class:`_ExplainabilityResult` --uses--> `ForecastingModel`  [INFERRED]
  explainability/explainability.py → models/forecasting/forecasting_model.py
- `The base class for forecasting model explainers. It defines the *minimal* behavi` --uses--> `ForecastingModel`  [INFERRED]
  explainability/explainability.py → models/forecasting/forecasting_model.py
- `TFTModel Explainer ------------------  The `TFTExplainer` uses a trained :class:` --uses--> `SeriesType`  [INFERRED]
  explainability/tft_explainer.py → utils/ts_utils.py
- `Returns the :class:`TFTExplainabilityResult         <darts.explainability.explai` --uses--> `SeriesType`  [INFERRED]
  explainability/tft_explainer.py → utils/ts_utils.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.03
Nodes (66): BasePointLoss, BlockRNNModel, _BlockRNNModule, CustomBlockRNNModule, Block Recurrent Neural Networks ------------------------------- .. autoclass:: C, PyTorch module implementing a block RNN to be used in `BlockRNNModel`., Block Recurrent Neural Network Model (RNNs).          This is a neural network m, This class allows to create custom block RNN modules that can later be used with (+58 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (69): Base Ensemble Model -------------------, Minimum prediction horizon for base models to satisfy the ensemble         (regr, Defines how to ensemble the individual models' predictions to produce a single p, Reduce the sample dimension of the forecasting models predictions, ForecastingModel, GlobalForecastingModel, _DartsCheckpointIO, FutureCovariatesTorchModel (+61 more)

### Community 2 - "Community 2"
Cohesion: 0.03
Nodes (58): Encoder, Returns a tuple of (past covariates encoders, future covariates encoders), SequentialEncoder, r"""Compute error values that the model produced for historical forecasts on (po, The base class for forecasting models. It defines the *minimal* behavior that al, Fit/train the model on the provided series.          Parameters         --------, Compute the residuals that the model produced for historical forecasts on (poten, Checks if the forecasting model supports a range index.         Some models may (+50 more)

### Community 3 - "Community 3"
Cohesion: 0.02
Nodes (48): Darts -----  A Python library for user-friendly forecasting and anomaly detectio, Create a ``TimeSeries`` from a time index and value array.          Parameters, Create an ``TimeSeries`` from an array of values.          The series will have, Read a pickled ``TimeSeries``.          Parameters         ----------         pa, The static covariates of this series.          If defined, the static covariates, The hierarchy of this series.          If defined, the hierarchy is given as a d, The metadata of this series.          If defined, the metadata is given as a dic, The top level component name of this series, or `None` if the series has no hier (+40 more)

### Community 4 - "Community 4"
Cohesion: 0.04
Nodes (48): HuggingFaceConnector, Hugging Face Connector ----------------------, Load the model by creating an instance of the given module class and loading, Get the path to a file either from a local directory or by downloading it from H, Extract params from `config` to set up the given `module_class`., HuggingFaceConnector enables loading a model configuration and weights from Hugg, Load the model configuration from a JSON file.          Returns         -------, Load the model weights from a safetensors file.          Parameters         ---- (+40 more)

### Community 5 - "Community 5"
Cohesion: 0.03
Nodes (23): ConformalModel, ConformalNaiveModel, ConformalQRModel, _get_calibration_hfc_start(), Conformal Models ----------------  A collection of conformal prediction models f, Generate calibrated historical forecasts.          In general the workflow of th, Cleans the model and sub-model., Saves the conformal model under a given path or file handle.          Additional (+15 more)

### Community 6 - "Community 6"
Cohesion: 0.07
Nodes (40): _ClassifierMixin, _QuantileModelContainer, SKLearn-Like Models -------------------  Darts provides a comprehensive set of f, Regression Model         Can be used to fit any scikit-learn-like regressor clas, Forecasts values for `n` time steps after the end of the series.          Parame, Generate predictions.          Generates deterministic predictions if no `Likeli, The lagged feature names the model has been trained on.          The naming conv, The lagged label name for the model's estimators.          The naming convention (+32 more)

### Community 7 - "Community 7"
Cohesion: 0.05
Nodes (33): AnomalyModel, Base Anomaly Model ------------------, Abstract method to implement the generation of predictions for the input `series, Compute the accuracy of the anomaly scores computed by the model.          Predi, Plot the results of the anomaly model.          Computes the score on the given, Base class for all anomaly models., Whether any of the Scorers is univariate., Whether any of the Scorers is trainable. (+25 more)

### Community 8 - "Community 8"
Cohesion: 0.05
Nodes (21): LinearRegressionModel, Linear Regression Model -----------------------  A forecasting model using a lin, Linear regression model.          Parameters         ----------         lags, RandomForest, RandomForestModel, Random Forest -------------  A forecasting model using a random forest regressio, Random Forest Model          Note: `RandomForest` is deprecated and will be remo, Random Forest Model          Parameters         ----------         lags (+13 more)

### Community 9 - "Community 9"
Cohesion: 0.06
Nodes (28): ABC, TimeSeries Datasets -------------------  Datasets and utilities for preparing ti, Dataset, LightningDataModule to handle train, val and predict dataloaders for ``TorchFore, Base Torch Dataset ------------------, Abstract class for all datasets that can be used with Darts' `TorchForecastingMo, The total number of samples that can be extracted., Returns a sample drawn from this dataset. (+20 more)

### Community 10 - "Community 10"
Cohesion: 0.04
Nodes (28): CatBoostClassifierModel, CatBoost Model for classification forecasting          Parameters         ------, Instantiate the underlying CatBoostClassifier model, Check and set the likelihood.         Only ClassProbability is supported for Cat, For some reason CatBoostClassifier does regression when given continuous labels, XGBoost Models --------------  This module offers wrappers around XGBoost's Grad, Custom loss function for XGBoost to compute quantile loss gradient.      Inspire, xgb_quantile_loss() (+20 more)

### Community 11 - "Community 11"
Cohesion: 0.04
Nodes (23): Data Processing ---------------  Tools for preprocessing and transforming time s, Pipeline, Fit all fittable transformers in pipeline.          Parameters         ---------, For each data transformer in the pipeline, first fit the data if transformer is, For each data transformer in pipeline transform data. Then transformed data is p, For each data transformer in the pipeline, inverse-transform data. Then inverse, Returns whether the pipeline is invertible or not.         A pipeline is inverti, Returns whether the pipeline is fittable or not.         A pipeline is fittable (+15 more)

### Community 12 - "Community 12"
Cohesion: 0.05
Nodes (16): EnsembleModel, EnsembleModel, Abstract base class for ensemble models.     Ensemble models take in a list of f, Cleans the model and sub-models., Saves the ensemble model under a given path or file handle.          Additionall, Loads a model from a given path or file handle.          Parameters         ----, Return `True` if all the `forecasting_models` are probabilistic and fit the same, EnsembleModel can predict likelihood parameters if all its forecasting models we (+8 more)

### Community 13 - "Community 13"
Cohesion: 0.06
Nodes (44): _classification_handling(), classification_support(), _compute_score(), _confusion_matrix(), _get_error_scale(), _get_highest_count_label(), _get_highest_probability_label(), _get_quantile_intervals() (+36 more)

### Community 14 - "Community 14"
Cohesion: 0.05
Nodes (24): Aggregator, Aggregator, FittableAggregator, Base Aggregator ---------------, Aggregates the (sequence of) multivariate series given as input into one (sequen, Base class for Aggregators that require training., Fits the aggregator, assuming the input is in the correct shape.          Parame, Fit the aggregators on the (sequence of) multivariate binary anomaly series. (+16 more)

### Community 15 - "Community 15"
Cohesion: 0.05
Nodes (17): _AddNorm, _GateAddNorm, _GatedLinearUnit, _GatedResidualNetwork, get_embedding_size(), _InterpretableMultiHeadAttention, _MultiEmbedding, TFTModel Sub-Modules --------------------  Implementation of ``nn.Modules`` for (+9 more)

### Community 16 - "Community 16"
Cohesion: 0.06
Nodes (29): FilteringAnomalyModel, Filtering Anomaly Model -----------------------  A `FilteringAnomalyModel` wraps, Compute the anomaly score(s) for the given (sequence of) series.          Predic, Filters the given sequence of target time series with the filtering model., Compute a metric for the anomaly scores computed by the model.          Predicts, Plot the results of the anomaly model.          Computes the score on the given, Fit the filters (if applicable) and scorers., # TODO: add support for covariates (see eg. Kalman Filter) (+21 more)

### Community 17 - "Community 17"
Cohesion: 0.06
Nodes (25): Prophet, Facebook Prophet ----------------, Returns a pandas DataFrame in the format required for Prophet.predict() with `n`, Checks if the conditions for custom conditional seasonalities are met. Each cust, Facebook Prophet          This class provides a basic wrapper around `Facebook P, Returns stochastic forecast of `n_samples` samples.         This method is a rep, Returns the output of the base Facebook Prophet model in form of a pandas DataFr, Adds a custom seasonality to the model that repeats after every n `seasonal_peri (+17 more)

### Community 18 - "Community 18"
Cohesion: 0.06
Nodes (43): _adjust_historical_forecasts_time_index(), _adjust_historical_forecasts_time_index_training(), _adjust_start(), _apply_data_transformers(), _apply_inverse_data_transformers(), _check_optimizable_historical_forecasts_global_models(), _check_start(), _convert_data_transformers() (+35 more)

### Community 19 - "Community 19"
Cohesion: 0.07
Nodes (43): add_static_covariates_to_lagged_data(), _all_equal_freq(), _check_lags(), _check_series_length(), create_lagged_component_names(), create_lagged_data(), _create_lagged_data_autoregression(), _create_lagged_data_by_intersecting_times() (+35 more)

### Community 20 - "Community 20"
Cohesion: 0.06
Nodes (20): Normalize ``x`` using statistics previously computed by :meth:`forward`., Reversible Instance Normalization based on [1]_          Parameters         ----, RINorm, io_processor(), Base Lightning Module ---------------------  Contains abstract classes for deter, Returns the index of the first predicted within the output of self.model., Same as :meth:`torch.nn.Module.forward`.          Parameters         ----------, performs the training step (+12 more)

### Community 21 - "Community 21"
Cohesion: 0.06
Nodes (18): _ClassifierMixin, CatBoostModel, CatBoost Models ---------------  This module offers wrappers around CatBoost's G, Fits/trains the model using the provided list of features time series and the ta, Returns the name of the categorical features parameter from model's `fit` method, CatBoost currently only supports categorical features as int.         If categor, CatBoost Model          Parameters         ----------         lags             L, LightGBMClassifierModel (+10 more)

### Community 22 - "Community 22"
Cohesion: 0.06
Nodes (27): describe_option(), get_option(), _Option, option_context(), _OptionsManager, Configuration -------------  Darts configuration system for global options and s, Manager for all Darts configuration options., Validator for positive integers. (+19 more)

### Community 23 - "Community 23"
Cohesion: 0.06
Nodes (19): The duration of the series (as a ``pandas.Timedelta`` or `int`)., Start time of the series.          Returns         -------         pandas.Timest, End time of the series.          Returns         -------         pandas.Timestam, Compute and return gaps in the series.          Works only on deterministic time, Convert a point along the time index into an integer index ranging from (0, len(, Convert a point into a ``pandas.Timestamp`` (if datetime-indexed) or integer (if, Split the series in two, after a provided `split_point`.          Parameters, Split the series in two, before a provided `split_point`.          Parameters (+11 more)

### Community 24 - "Community 24"
Cohesion: 0.06
Nodes (27): _make_attn_mask(), _MultiHeadAttention, _PerDimScale, TimesFM 2.5 Submodels ---------------------  --- title: TimesFM 2.5 Submodels su, Residual block with two linear layers and a linear residual connection., Makes attention mask., Rotary positional embedding., Generates a JTensor of sinusoids with different frequencies. (+19 more)

### Community 25 - "Community 25"
Cohesion: 0.06
Nodes (20): BaseDataTransformer, Set the verbosity status.          `True` for enabling the detailed report about, Set the number of processors to be used by the transformer while processing mult, Applies component masking to `ts_transform`., The function that will be applied to each series when :func:`transform()` is cal, Transforms a (sequence of) of series by calling the user-implemeneted `ts_transf, Creates generator of dictionaries containing fixed parameter values         (i.e, Raises `ValueError` if `self._parallel_params` specifies a `key` in         `sel (+12 more)

### Community 26 - "Community 26"
Cohesion: 0.06
Nodes (15): ClassProbabilityLikelihood, GaussianLikelihood, _get_likelihood(), PoissonLikelihood, Likelihoods for SKLearnModel ----------------------------, Gaussian distribution [1]_.          Parameters         ----------         n_out, Poisson distribution [1]_.          Parameters         ----------         n_outp, Class probability likelihood.         Likelihood to predict the probability of e (+7 more)

### Community 27 - "Community 27"
Cohesion: 0.09
Nodes (10): _extract_targets(), GlobalNaiveAggregate, _GlobalNaiveAggregateModule, _GlobalNaiveDrift, _GlobalNaiveModel, _GlobalNaiveModule, GlobalNaiveSeasonal, _GlobalNaiveSeasonalModule (+2 more)

### Community 28 - "Community 28"
Cohesion: 0.06
Nodes (19): Anomaly Detection -----------------  A suite of tools for performing anomaly det, Utils for Historical Forecasting --------------------------------  Utilities for, _optimized_historical_forecasts_regression(), Optimized Historical Forecasts for SKLearnModel --------------------------------, Optimized historical forecasts for SKLearnModel.      Rely on _check_optimizable, Metrics =======  Regression Metrics ------------------  For deterministic foreca, Torch Data Module -----------------, _parse_input_chunk_length() (+11 more)

### Community 29 - "Community 29"
Cohesion: 0.07
Nodes (16): _Attention, _LearnedPositionalEmbedding, _make_attn_mask(), _MLP, Learned positional embedding added to patch embeddings., Feed-forward network used in transformer blocks., SwiGLU feed-forward network (alternative to MLP in transformer blocks)., Multi-head self-attention with scaled dot-product attention. (+8 more)

### Community 30 - "Community 30"
Cohesion: 0.08
Nodes (33): _bartlett_formula(), check_seasonality(), extract_trend_and_seasonality(), granger_causality_tests(), plot_acf(), plot_ccf(), plot_hist(), plot_pacf() (+25 more)

### Community 31 - "Community 31"
Cohesion: 0.11
Nodes (19): CustomFeedForwardDecoderLayer, CustomFeedForwardEncoderLayer, Transformer Modules -------------------, Overwrites the PyTorch TransformerEncoderLayer to use Darts' Position-wise Feed-, Parameters         ----------         ffn             One of Darts' Position-wis, Overwrites the PyTorch TransformerDecoderLayer to use Darts' custom Position Wis, Parameters         ----------         ffn             One of Darts' Position-wis, _generate_coder() (+11 more)

### Community 32 - "Community 32"
Cohesion: 0.07
Nodes (17): Temporal Fusion Transformer (TFT) ---------------------------------, List of all continuous variables in model, List of all static variables in model, List of numeric static variables in model, List of categorical static variables in model, List of all encoder variables in model (excluding static variables), List of all decoder variables in model (excluding static variables), add time dimension to static context (+9 more)

### Community 33 - "Community 33"
Cohesion: 0.09
Nodes (18): Stores the explainability results of a :class:`ShapExplainer <darts.explainabili, Returns one or several ``TimeSeries`` representing the feature values         fo, Returns the underlying ``shap.Explanation`` object for a given horizon and compo, Stores the explainability results of a :class:`ShapExplainer <darts.explainabili, Returns the ``TimeSeries`` representing the explanation for a given component., Returns the ``TimeSeries`` representing the feature values for a given component, Returns the underlying ``shap.Explanation`` object for a given component., ShapExplainabilityResult (+10 more)

### Community 34 - "Community 34"
Cohesion: 0.09
Nodes (18): KMeansScorer, k-means Scorer --------------  `k`-means Scorer implementing `k`-means clusterin, Wrapper around model inference method, k-means Scorer          When calling `fit(series)`, a moving window is applied,, PyODScorer, PyOD Scorer -----------  This scorer can wrap around detection algorithms of PyO, Wrapper around model inference method, PyOD Scorer          When calling ``fit(series)``, a moving window is applied, w (+10 more)

### Community 35 - "Community 35"
Cohesion: 0.10
Nodes (29): _assert_binary(), _assert_fit_called(), _assert_same_length(), _assert_timeseries(), _check_input(), _eval_metric(), eval_metric_from_binary_prediction(), eval_metric_from_scores() (+21 more)

### Community 36 - "Community 36"
Cohesion: 0.08
Nodes (16): Generates/extracts time index (or integer index) for covariates for training and, If (actual) covariates are given, merge the encoded index with the covariates, Avoid pitfalls: `encode_train()` or `encode_inference()` can be called multiple, `SingleEncoder`: Abstract class for single index encoders.     Single encoders c, Single encoders take an `index_generator` to generate the required index for enc, Single Encoders must implement an _encode() method to encode the index., Returns encoded index for training.          Parameters         ----------, Returns encoded index for inference/prediction.          Parameters         ---- (+8 more)

### Community 37 - "Community 37"
Cohesion: 0.09
Nodes (11): FeedForward, r""" Feed-Forward Module -------------------  The MIT License (MIT)  Copyright (, FFN module [1]_.          Parameters         ----------         d_model, Bilinear, GEGLU, GELU, GLU, GLU Variants ------------ (+3 more)

### Community 38 - "Community 38"
Cohesion: 0.10
Nodes (12): DualCovariatesTorchModel, CustomRNNModule, Recurrent Neural Networks ------------------------- .. autoclass:: CustomRNNModu, overwrite parent classes `_produce_predict_output` method, This model is recurrent, so we have to write a specific way to         obtain th, PyTorch module implementing an RNN to be used in `RNNModel`.          PyTorch mo, Recurrent Neural Network Model (RNNs).          This class provides three varian, This class allows to create custom RNN modules that can later be used with Darts (+4 more)

### Community 39 - "Community 39"
Cohesion: 0.08
Nodes (15): TFTModel Explainer ------------------  The `TFTExplainer` uses a trained :class:, Returns the :class:`TFTExplainabilityResult         <darts.explainability.explai, Plots the variable selection / feature importances of the `TFTModel` based on th, Plots the attention heads of the `TFTModel`.          Parameters         -------, Returns the encoder variable importance of the TFT model.          The encoder_w, Returns the decoder variable importance of the TFT model.          The decoder_w, Returns the static covariates importance of the TFT model.          The static c, Returns the encoder or decoder variable of the TFT model.          Parameters (+7 more)

### Community 40 - "Community 40"
Cohesion: 0.08
Nodes (14): FutureCovariatesLocalForecastingModel, Generates covariate encodings for training and inference/prediction and returns, Verify that the assumptions for likelihood parameters prediction are verified:, Forecasts values for `n` time steps after the end of the series.          If :fu, The base class for future covariates "local" forecasting models, handling single, Forecasts values for `n` time steps after the end of the training series., Forecasts values for a certain number of time steps after the end of the series., Simple check if user supplied/did not supply covariates as done at fitting time. (+6 more)

### Community 41 - "Community 41"
Cohesion: 0.11
Nodes (14): InvertibleDataTransformer, Inverse transforms a (sequence of) series by calling the user-implemented `ts_in, Abstract class for invertible transformers.          All the deriving classes ha, Prepend the historic part of the `insample` series to the `series` if it is not, Static Covariates Transformer -----------------------------, Collates static covariates of all provided `TimeSeries` and fits the following p, Extracts numerical and categorical static covariate (component / columns) names, Returns mapping from names of untransformed categorical static covariates names (+6 more)

### Community 42 - "Community 42"
Cohesion: 0.10
Nodes (13): NLLScorer, ExponentialNLLScorer, NLL Exponential Scorer ----------------------  Exponential distribution negative, NLL Exponential Scorer          Parameters         ----------         window, LaplaceNLLScorer, NLL Laplace Scorer ------------------  Laplace distribution negative log-likelih, NLL Laplace Scorer          Parameters         ----------         window, PoissonNLLScorer (+5 more)

### Community 43 - "Community 43"
Cohesion: 0.10
Nodes (13): FittableAnomalyScorer, Extract a deterministic series from `series` (quantile=0.5 if `series` is probab, Base class of scorers that require training., Parameters         ----------         is_univariate             Whether the scor, Fits the scorer on the given time series.          If a sequence of series, the, Fits the scorer on the two (sequences of) series.          The function `diff_fn, Computes the anomaly score on the given series.          If a sequence of series, Computes the anomaly score on the two (sequence of) series.          The functio (+5 more)

### Community 44 - "Community 44"
Cohesion: 0.08
Nodes (20): _clean_components(), _concat_hierarchy(), _concat_static_covs(), concatenate(), Timeseries ----------  ``TimeSeries`` is `Darts` container for storing and handl, Return a new series with the first `size` points.          Parameters         --, Return a new series with the last `size` points.          Parameters         ---, # TODO: potential to use timezone-aware index since `TimeSeries` was refactored (+12 more)

### Community 45 - "Community 45"
Cohesion: 0.09
Nodes (26): autoregressive_timeseries(), _build_forecast_series(), _build_forecast_series_from_schema(), constant_timeseries(), datetime_attribute_timeseries(), _extend_time_index_until(), gaussian_timeseries(), _generate_new_dates() (+18 more)

### Community 46 - "Community 46"
Cohesion: 0.11
Nodes (14): FittableDataTransformer, Data Transformers -----------------  Data transformers for preprocessing time se, BottomUpReconciliator, _get_summation_matrix(), MinTReconciliator, Hierarchical Reconciliation ---------------------------  A set of posthoc hierar, Performs top down reconciliation, as defined `here <https://otexts.com/fpp3/reco, MinT Reconcilator.          This implements the MinT reconciliation approach pre (+6 more)

### Community 47 - "Community 47"
Cohesion: 0.11
Nodes (16): DatasetLoaderCSV, AustralianTourismDataset, ElectricityConsumptionZurichDataset, GasRateCO2Dataset, HeartRateDataset, MonthlyMilkIncompleteDataset, Datasets --------  A few popular time series datasets.  Overall usage of this pa, Gas Rate CO2 dataset     Two components, length 296 (integer time index) (+8 more)

### Community 48 - "Community 48"
Cohesion: 0.12
Nodes (14): FutureCovariatesIndexGenerator, Generates index for future covariates on train and inference datasets., CyclicTemporalEncoder, FutureCyclicEncoder, PastCyclicEncoder, `CyclicTemporalEncoder`: Cyclic encoding of time series datetime attributes., Cyclic index encoding for `TimeSeries` that have a time index of type `pd.Dateti, applies cyclic encoding from `datetime_attribute_timeseries()` to `self.attribut (+6 more)

### Community 49 - "Community 49"
Cohesion: 0.13
Nodes (11): _Block, NHiTSModel, _NHiTSModule, PyTorch module implementing one stack of the N-BEATS architecture that comprises, # TODO: leave option to share weights across blocks?, PyTorch module implementing the N-HiTS architecture.          Parameters, # TODO: shouldn't this be output_dim?, An implementation of the N-HiTS model, as presented in [1]_.          N-HiTS is (+3 more)

### Community 50 - "Community 50"
Cohesion: 0.10
Nodes (7): CostMatrix, DenseCostMatrix, DTW Cost Matrix ---------------, (n+1) x (m+1) Matrix     Cell (i,j) corresponds to minimum total cost/distance o, Returns         -------         Dense n x m numpy array, where empty cells are s, Creates a cost matrix from a window.         Depending on the density of the act, SparseCostMatrix

### Community 51 - "Community 51"
Cohesion: 0.09
Nodes (12): Callback, TQDMProgressBar, PyTorchLightningPruningCallback, Callbacks for TorchForecastingModel -----------------------------------, Override this to customize the tqdm bar for validation., PyTorch Lightning callback to prune unpromising Optuna trials.      Reports the, Raise :class:`optuna.TrialPruned` manually if pruned.          Currently, ``inte, Darts' Progress Bar for `TorchForecastingModels`.          Allows to customize f (+4 more)

### Community 52 - "Community 52"
Cohesion: 0.14
Nodes (6): _is_xarray(), The time index of the series., Return a 2-D array of shape (time, component), containing the series' values for, Create a copy of the series.          Returns         -------         TimeSeries, Extract values from another series or array and check for compatible shapes., Check if *obj* is an xarray type without importing xarray.

### Community 53 - "Community 53"
Cohesion: 0.10
Nodes (10): Return a `Series` representation of the series in a given `backend`.          Wo, First value of the univariate series.          Returns         -------         f, Last value of the univariate series.          Returns         -------         fl, First values of the potentially multivariate series.          Returns         --, Last values of the potentially multivariate series.          Returns         ---, Return a 1-D Numpy array of shape (time,) containing the univariate series' valu, Return a new series with the `other` series stacked to this series along the com, Return a new series with one (or more) additional component(s) that contain an a (+2 more)

### Community 54 - "Community 54"
Cohesion: 0.10
Nodes (12): Encoder, Abstract class for all encoders, Each subclass must implement a method to encode the covariates index for trainin, Each subclass must implement a method to encode the covariates index for predict, Each subclass must implement a method to encode the covariates index for trainin, Returns whether the `Encoder` object has been fitted., Whether the `Encoder` sub class must be fit with `Encoder.encode_train()` before, FutureIntegerIndexEncoder (+4 more)

### Community 55 - "Community 55"
Cohesion: 0.11
Nodes (13): `SequentialEncoderTransformer` applies transformation to the non-transformed enc, Parameters         ----------         transformer             A `FittableDataTra, This method applies transformation to the non-transformed encoded covariates out, if user supplied additional covariates to model.fit() or model.predict(), `self., Return whether the transformer has been fitted., SequentialEncoderTransformer, FutureCallableIndexEncoder, Returns the past covariates component names generated by `SequentialEncoder.past (+5 more)

### Community 56 - "Community 56"
Cohesion: 0.11
Nodes (9): DLinearModel, _DLinearModule, _MovingAvg, x_in             comes as tuple `(x_past, x_future, x_static, future_target)` wh, Moving average block to highlight the trend of time series, An implementation of the DLinear model, as presented in [1]_.          This impl, Series decomposition block, PyTorch module implementing the DLinear architecture.          Parameters (+1 more)

### Community 57 - "Community 57"
Cohesion: 0.17
Nodes (9): BaseException, DatasetLoader, DatasetLoadingException, Dataset Loader --------------, Downloads the dataset in the root_path directory          Raises         -------, Given a Path to the file and a DataLoaderMetadata object, return a TimeSeries, Class that downloads a dataset and caches it locally.     Assumes that the file, Load the dataset in memory, as a TimeSeries.         Downloads the dataset if it (+1 more)

### Community 58 - "Community 58"
Cohesion: 0.12
Nodes (11): CovariatesIndexGenerator, Generates/extracts time index (or integer index) for covariates at model trainin, Generates/extracts time index (or integer index) for covariates at model inferen, Returns the index generator base component name.         - "pc": past covariates, Check the base requirements for `min_covariates_lag` and `max_covariates_lag`:, :class:`CovariatesIndexGenerator` generates a time index for covariates at train, PastCallableIndexEncoder, Returns the future covariates encoders (+3 more)

### Community 59 - "Community 59"
Cohesion: 0.10
Nodes (3): MultivariateModel, Multivariate Model ------------------  A wrapper around any base forecasting mod, Wrapper for any base ForecastingModel to enable multivariate forecasting support

### Community 60 - "Community 60"
Cohesion: 0.12
Nodes (9): _Block, _GType, _NBEATSModule, PyTorch module implementing the basic building block of the N-BEATS architecture, PyTorch module implementing one stack of the N-BEATS architecture that comprises, PyTorch module implementing the N-BEATS architecture.          Parameters, _SeasonalityGenerator, _Stack (+1 more)

### Community 61 - "Community 61"
Cohesion: 0.14
Nodes (4): _get_checkpoint_fname(), _get_checkpoint_folder(), _get_logs_folder(), _get_runs_folder()

### Community 62 - "Community 62"
Cohesion: 0.13
Nodes (9): BoxCox, Box-Cox Transformer -------------------, Box-Cox data transformer.          See [1]_ for more information about Box-Cox t, FittableDataTransformer, Fits transformer to a (sequence of) `TimeSeries` by calling the user-implemented, Fit the transformer to the (sequence of) series and return the transformed input, Overrides `_get_params` of `BaseDataTransformer`. Creates generator of dictionar, Base class for fittable transformers.          All the deriving classes have to (+1 more)

### Community 63 - "Community 63"
Cohesion: 0.15
Nodes (9): _dtw_path(), DTWAlignment, Dynamic Time Warping (DTW) Alignment.      Attributes     ----------     n, Gives the index paths from `series1` to `series2`.          Returns         ----, Gives the total distance between pair-wise elements in the two series after warp, Gives the mean distance between pair-wise elements in the two series after warpi, Warps the two time series according to the warp path returned by `DTWAlignment.p, NoWindow (+1 more)

### Community 64 - "Community 64"
Cohesion: 0.12
Nodes (8): KalmanFilter, Sequentially applies the Kalman filter on the provided series of observations., This model implements a Kalman filter over a time series.          The key metho, Initializes the Kalman filter using the N4SID algorithm.          Parameters, KalmanForecaster, Kalman Filter Forecaster ------------------------  A model producing stochastic, Kalman filter Forecaster          This model uses a Kalman filter to produce for, TransferableFutureCovariatesLocalForecastingModel

### Community 65 - "Community 65"
Cohesion: 0.14
Nodes (10): _finite_rows_boundaries(), Create a ``TimeSeries`` from a time index `times` and values `values`., Return a 2-D array of shape (time, component), containing the series' values for, Return a slice of the deterministic time series where NaN-containing entries at, Return the time index and values with missing dates inserted.          This requ, Sort `times` and `values` by ascending dates.          Only performed if `times`, Return all observed/inferred frequencies of a ``pandas.Index`` (an integer-value, Return `times` re-indexed into a `pandas.RangeIndex` and `values` in the re-inde (+2 more)

### Community 66 - "Community 66"
Cohesion: 0.12
Nodes (9): BaseDataTransformer, Mapper, Data transformer to apply a custom function to a (sequence of) ``TimeSeries``, MissingValuesFiller, Missing Values Filler ---------------------, Data transformer to fill missing values from a (sequence of) deterministic ``Tim, Window Transformer ------------------, A transformer that applies window transformation to a TimeSeries or a Sequence o (+1 more)

### Community 67 - "Community 67"
Cohesion: 0.12
Nodes (9): Stores the explainability results of a :class:`TFTExplainer <darts.explainabilit, Returns the time-dependent attention on the encoder and decoder for each `horizo, Returns the feature importances for the encoder, decoder and static covariates a, Returns the encoder importances aggregated over time as a pd.DataFrames., Returns the decoder importances aggregated over time as a pd.DataFrames., Returns the numeric and categorical static covariates importances as a pd.DataFr, Returns the encoder importances over time as a `TimeSeries`, with one component, Returns the decoder importances over time as a `TimeSeries`, with one component (+1 more)

### Community 68 - "Community 68"
Cohesion: 0.15
Nodes (9): MIDAS, Mixed-data sampling (MIDAS) Transformer ---------------------------------------, MIDAS needs the high frequency period name in order to easily reverse_transform, Transforms series from high to low frequency using a mixed-data sampling approac, Transforms series back to high frequency by retrieving the original high frequen, Mixed-data sampling transformer.          A transformer that converts higher fre, Some sanity checks on the input, the high_freq and low_freq arguments are mutual, If static covariates are component-specific, they must be reshaped appropriately (+1 more)

### Community 69 - "Community 69"
Cohesion: 0.17
Nodes (12): FeatureType, _get_matching_index(), Data Utils ----------, Given two overlapping series `ts_target` and `ts_covariate` and an index point `, Enum, _build_tqdm_iterator(), ModelMode, ModelType (+4 more)

### Community 70 - "Community 70"
Cohesion: 0.17
Nodes (11): DatasetLoaderMetadata, AusBeerDataset, EnergyDataset, Half-hourly electricity demand in England and Wales from Monday 5 June 2000 to S, Total quarterly beer production in Australia (in megalitres) from 1956:Q1 to 200, Weather includes 21 indicators of weather, such as air     temperature, and humi, Parameters         ----------         multivariate: bool             Whether to, Load the WeatherDataset dataset as a list of univariate timeseries, one for weat (+3 more)

### Community 71 - "Community 71"
Cohesion: 0.14
Nodes (11): FutureDatetimeAttributeEncoder, PastDatetimeAttributeEncoder, PastIntegerIndexEncoder, Time Axes Encoders ------------------  Encoders can generate past and/or future, Datetime attribute encoder for past covariates., Parameters         ----------         attribute             The attribute of the, Datetime attribute encoder for future covariates., Parameters         ----------         attribute             The attribute of the (+3 more)

### Community 72 - "Community 72"
Cohesion: 0.14
Nodes (10): StatsForecastModel ------------------, Unpack the dictionary that is returned by the StatsForecast 'predict()' method., StatsForecast Model.          Can be used to fit any `StatsForecast` base model., _unpack_sf_dict(), Likelihood, QuantilePrediction, Likelihoods for StatsForecastModel ----------------------------------, Quantile Prediction Likelihood          Can be used to generate quantile predict (+2 more)

### Community 73 - "Community 73"
Cohesion: 0.14
Nodes (7): Temporal Convolutional Network ------------------------------, PyTorch module implementing a dilated TCN module used in `TCNModel`.           P, Temporal Convolutional Network Model (TCN).          This is an implementation o, PyTorch module implementing a residual block module used in `_TCNModule`., _ResidualBlock, TCNModel, _TCNModule

### Community 74 - "Community 74"
Cohesion: 0.15
Nodes (7): Base Adapter for SHAP Explainer -------------------------------, SHAPMethod, TorchForecastingModel Adapter for SHAP Explainer -------------------------------, Builds the SHAP explainer based on the specified SHAP method.          Parameter, Wrapper function to adapt the SHAP explainer to the torch forecasting model. It, TorchShapAdapter, ShapAdapter

### Community 75 - "Community 75"
Cohesion: 0.13
Nodes (7): Return a new series with the mean computed over the specified `axis`.          I, Return a new series with the median computed over the specified `axis`., Return a new series with the sum computed over the specified `axis`.          If, Return a new series with the minimum computed over the specified `axis`., Return a new series with the maximum computed over the specified `axis`., Get output time index and components based on a aggregation `axis` and potential, Create a representation of the TimeSeries values.          The returned dimensio

### Community 76 - "Community 76"
Cohesion: 0.14
Nodes (9): _divide_no_nan(), MAELoss, MapeLoss, PyTorch Loss Functions ----------------------, a/b where the resulted NaN or Inf are replaced by 0., sMAPE loss as defined in https://robjhyndman.com/hyndsight/smape/ (Chen and Yang, MAPE loss as defined in: https://en.wikipedia.org/wiki/Mean_absolute_percentage_, MAE loss as defined in: https://en.wikipedia.org/wiki/Mean_absolute_error. (+1 more)

### Community 77 - "Community 77"
Cohesion: 0.15
Nodes (6): CRWindow, gtz(), Compressed row representation window.     Stores the range of active grid cells, Parameters         ----------         n             The width of the window, mus, Extends the active cells in the column by the range (start,end).         Ranges, Marks a grid cell as active.          Parameters         ----------         elem

### Community 78 - "Community 78"
Cohesion: 0.17
Nodes (7): PastCovariatesIndexGenerator, Generates index for past covariates on train and inference datasets, Returns encoded index for all past and/or future covariates for training., Returns encoded index for all past and/or future covariates for inference/predic, Returns encoded index for all past and/or future covariates for training and inf, Launches the encode sequence for past covariates and future covariates for eithe, Sequentially encodes the index of all input target/covariates TimeSeries with th

### Community 79 - "Community 79"
Cohesion: 0.14
Nodes (9): ComponentBasedExplainabilityResult, _ExplainabilityResult, Explainability Result ---------------------  Contains the explainability results, Helper that validates the input parameters of a method that queries the `Compone, Abstract class for explainability results of a :class:`_ForecastingModelExplaine, Returns one or multiple explanations based on some input parameters., Stores the explainability results of a :class:`_ForecastingModelExplainer     <d, Returns one or several explanations for a given component.          Parameters (+1 more)

### Community 80 - "Community 80"
Cohesion: 0.14
Nodes (6): NaiveDrift, NaiveMean, Baseline Models ---------------  A collection of simple benchmark models for sin, Naive Drift Model          This model fits a line between the first and last poi, Naive Mean Model          This model has no parameter, and always predicts the, LocalForecastingModel

### Community 81 - "Community 81"
Cohesion: 0.13
Nodes (6): InvertibleDataTransformer, InvertibleMapper, Mapper and InvertibleMapper ---------------------------, Data transformer to apply a custom function and its inverse to a (sequence of) `, Generic wrapper class for using scalers on time series.          The underlying, Scaler

### Community 82 - "Community 82"
Cohesion: 0.14
Nodes (6): AnomalyScorer, DifferenceScorer, Difference Scorer -----------------  This scorer simply computes the elementwise, NormScorer, Norm Scorer -----------  Norm anomaly score (of given order) [1]_.  References -, Norm Scorer          Returns the element-wise norm of a given order between two

### Community 83 - "Community 83"
Cohesion: 0.19
Nodes (9): DatasetLoaderCSV, AirPassengersDataset, ETTh1Dataset, ETTm1Dataset, IceCreamHeaterDataset, Monthly sales of heaters and ice cream between January 2004 and June 2020., Monthly Air Passengers Dataset, from 1949 to 1960., The data of 1 Electricity Transformers at 1 stations, including load, oil temper (+1 more)

### Community 84 - "Community 84"
Cohesion: 0.15
Nodes (8): Dynamic Time Warping (DTW) --------------------------  Tools for computing Dynam, Itakura, DTW Windows -----------, Forms the Itakura parallelogram, where max_slope determines the slope of the ste, Parameters         ----------         max_slope             The slope of the ste, Forms a diagonal window where window_size controls the maximum allowed shift bet, Parameters         ----------         window_size             The maximum allowe, SakoeChiba

### Community 85 - "Community 85"
Cohesion: 0.16
Nodes (4): Croston, Croston Method --------------, Croston method as presented `in this paper <https://otexts.com/fpp3/counts.html>, StatsForecastModel

### Community 86 - "Community 86"
Cohesion: 0.20
Nodes (5): This serves as a protocol for expected StatsForecast model API., Computes the model output.          When this method is called, it is guaranteed, Computes the OLS residuals for predicting the target series from `future_covaria, _SFModel, Protocol

### Community 87 - "Community 87"
Cohesion: 0.18
Nodes (4): VARIMA ------  Models for VARIMA (Vector Autoregressive moving average) [1]_. Th, Differentiate the series self.d times, VARIMA          Parameters         ----------         p : int             Order, VARIMA

### Community 88 - "Community 88"
Cohesion: 0.20
Nodes (7): Builds the feature names for the SHAP explanations based on the input features u, Builds the SHAP explainer based on the specified SHAP method.          Parameter, Creates the SHAP input for the given series and covariates, by following the log, Specifies the supported SHAP methods., Return the default SHAP method., Model-specific adapter between Darts forecasting models and the SHAP library., ShapAdapter

### Community 89 - "Community 89"
Cohesion: 0.23
Nodes (8): sk_MultiOutputClassifier, sk_MultiOutputRegressor, MultiOutputClassifier, MultiOutputRegressor, Multi-Output Models for SKLearnModel ------------------------------------, Whether model supports sample weight for training., :class:`sklearn.utils.multioutput.MultiOutputRegressor` with a modified ``fit()`, Fit the model to data, separately for each output variable.          Parameters

### Community 90 - "Community 90"
Cohesion: 0.15
Nodes (6): Called by dtw to initialize the window to a certain size.          Parameters, Gives the number of active grid cells before row element j, in column i., Gives the number of active grid cells in a column.          Parameters         -, Gives the number of activate grid cells in each column.          Returns, Returns         -------         Iterator             Iterate over all active cel, Window

### Community 91 - "Community 91"
Cohesion: 0.17
Nodes (6): CallableIndexEncoder, `CallableIndexEncoder`: Applies a user-defined callable to encode the underlying, Parameters         ----------         index_generator             An instance of, Test the callable with sample `pd.DatetimeIndex` and `pd.RangeIndex` to determin, Apply the user-defined callable to encode the index., `CallableIndexEncoder` accepts transformations.

### Community 92 - "Community 92"
Cohesion: 0.17
Nodes (3): Fits the model on the provided series.         Note that `EnsembleModel.fit()` d, Verify that any non-None covariates comply with the model type., LocalForecastingModel

### Community 93 - "Community 93"
Cohesion: 0.21
Nodes (6): Sequence, Model selection utilities -------------------------  Utilities that help in mode, This class is primarily meant to be instantiated from ``train_test_split()`` fun, Splits the provided series into training and test series.      Supports splittin, SplitTimeSeriesSequence, train_test_split()

### Community 94 - "Community 94"
Cohesion: 0.19
Nodes (6): Return a new series similar to this one but with new `values`.          Paramete, Return a deterministic series with the desired quantile(s) `q` of each component, Return a deterministic series with the variance of each component computed over, Return a deterministic series with the standard deviation of each component comp, Return a deterministic series with the skew of each component computed over the, Return a deterministic series with the kurtosis of each component computed over

### Community 95 - "Community 95"
Cohesion: 0.15
Nodes (12): format_bytes(), format_dict(), format_list(), make_collapsible_section(), make_paragraph(), Formats a list as a string, showing at most `max_items` items.     Pass `render_, Creates a collapsible HTML section.      Parameters     ----------     title, Creates an HTML paragraph with optional bold text and margin. (+4 more)

### Community 96 - "Community 96"
Cohesion: 0.19
Nodes (12): get_series_seq_type(), get_single_series(), Additional TimeSeries related util functions -----------------------------------, If `ts` is a Sequence with only a single series, return the single series as Tim, Returns a single (first) TimeSeries or `None` from `ts`. Returns `ts` if  `ts` i, Returns the sequence type of `ts`.      - SeriesType.SINGLE: `TimeSeries` (e.g., # TODO: we do not check the time index here, Trims all series in the provided list, if necessary, so that the returned time s (+4 more)

### Community 97 - "Community 97"
Cohesion: 0.17
Nodes (6): IntegerIndexEncoder, IntegerIndexEncoder: Adds integer index value (position) derived from the underl, Parameters         ----------         index_generator             An instance of, Adds integer index value (position) to the provided `index`.         For attribu, `IntegerIndexEncoder` accepts transformations. Note that transforming 'relative', SingleEncoder

### Community 98 - "Community 98"
Cohesion: 0.17
Nodes (6): Sets up/Initializes all past and future encoders and an optional transformer fro, Sets up/Initializes an optional transformer from `add_encoder` parameter used at, Processes input and returns two lists of tuples `(encoder_id, attribute)` from r, Processes input params used at model creation and returns tuple of one transform, Processes input params used at model creation for time zone specification, and r, SequentialEncoder automatically creates encoder objects from parameter `add_enco

### Community 99 - "Community 99"
Cohesion: 0.18
Nodes (5): FFT, Fast Fourier Transform Model          This model performs forecasting on a TimeS, Helper function, used to make FFT model pickable., Helper function, for consistency with the other trends, Helper function, used to make FFT model pickable.

### Community 100 - "Community 100"
Cohesion: 0.20
Nodes (6): _check(), _check_in_open_0_1_intvl(), GeometricLikelihood, Likelihoods for TorchForecastingModel -------------------------------------  The, # TODO: Table on README listing distribution, possible priors and wiki article, Geometric distribution.          https://en.wikipedia.org/wiki/Geometric_distrib

### Community 101 - "Community 101"
Cohesion: 0.17
Nodes (11): accuracy(), ae(), ape(), arre(), Metrics -------  Some metrics to compare time series., Absolute Percentage Error (APE).      For the true series :math:`y` and predicte, Absolute Ranged Relative Error (ARRE).      For the true series :math:`y` and pr, Absolute Error (AE).      For the true series :math:`y` and predicted series :ma (+3 more)

### Community 102 - "Community 102"
Cohesion: 0.17
Nodes (6): Transforms a window-wise anomaly score into a point-wise anomaly score., Wrapper around model inference method, Train one sub-model for each component when self.is_univariate=False and series, Apply the scorer (sub) model scoring method on the series components, Internal function called by WindowedAnomalyScorer `fit()` and `score()` function, Converts generated anomaly score from `np.ndarray` into a sequence of series. Fo

### Community 103 - "Community 103"
Cohesion: 0.20
Nodes (6): Return a 3-D array of dimension (time, component, sample) containing the series', Return a slice of the series where the time index was intersected with the `othe, Return the sliced values of the series where the time index was intersected with, Return the time index of the series where the time index was intersected with th, Find the start (absolute index) and end (index relative to the end) indices that, Whether the series has the same time index as the `other` series.          Param

### Community 104 - "Community 104"
Cohesion: 0.20
Nodes (11): _auto_fill(), _const_fill(), extract_subseries(), fill_missing_values(), missing_values_ratio(), Utils for filling missing values --------------------------------, Computes the ratio of missing values      Parameters     ----------     series, Fills the missing values of `series` with only the value provided (default zeroe (+3 more)

### Community 105 - "Community 105"
Cohesion: 0.26
Nodes (11): _compute_central_series(), _compute_quantile_bounds(), plot(), plotly(), _prepare_plot_params(), Plotting utilities for TimeSeries visualization using matplotlib and plotly., Compute the central TimeSeries for a component., Compute the low and high quantile TimeSeries for confidence intervals.      Retu (+3 more)

### Community 106 - "Community 106"
Cohesion: 0.18
Nodes (7): ETTh2Dataset, ETTm2Dataset, MonthlyMilkDataset, Monthly production of milk (in pounds per cow) between January 1962 and December, The data of 1 Electricity Transformers at 1 stations, including load, oil temper, The data of 1 Electricity Transformers at 1 stations, including load, oil temper, Datasets ========  A few popular time series datasets.  Overall usage of this pa

### Community 107 - "Community 107"
Cohesion: 0.18
Nodes (5): DatetimeAttributeEncoder, `DatetimeAttributeEncoder`: Adds pd.DatatimeIndex attribute information derived, Parameters         ----------         index_generator             An instance of, Encode `index` as a scalar., `DatetimeAttributeEncoder` accepts transformations

### Community 108 - "Community 108"
Cohesion: 0.24
Nodes (10): _check_valid_input(), get_component_names(), process_horizons_and_targets(), process_input(), Explainability Utils --------------------, Processes the input horizons and target component names.      horizons         O, Extract and return the components of target series, static covariate, past and f, Checks that the input is valid (+2 more)

### Community 109 - "Community 109"
Cohesion: 0.27
Nodes (1): NeuralForecastModel

### Community 110 - "Community 110"
Cohesion: 0.20
Nodes (5): LayerNorm, LayerNormNoBias, Layer Norm Variants -------------------  MIT License  Copyright (c) 2020 Phil Wa, An alternate to layer normalization, without mean centering and the learned bias, RMSNorm

### Community 111 - "Community 111"
Cohesion: 0.22
Nodes (5): Detector, Quantile Detector -----------------  Flags anomalies that are beyond some quanti, # TODO: we could make this more efficient when low_quantile or high_quantile con, Threshold Detector ------------------  Detector that detects anomaly based on us, ThresholdDetector

### Community 112 - "Community 112"
Cohesion: 0.22
Nodes (5): Detector, Base class for all detectors, Detect anomalies on given time series.          Parameters         ----------, Score the results against true anomalies.          Parameters         ----------, Threshold Detector          Flags values that are either below or above the `low

### Community 113 - "Community 113"
Cohesion: 0.20
Nodes (5): _BoundedDetectorMixin, Base Detector -------------, A class containing functions supporting bounds-based detection, to be used as a, Process the boundaries argument and perform some sanity checks          Paramete, # TODO:

### Community 114 - "Community 114"
Cohesion: 0.31
Nodes (7): _down_sample(), dtw(), _dtw_cost_matrix(), _expand_window(), _fast_dtw(), Dynamic Time Warping (DTW) --------------------------, Determines the optimal alignment between two time series `series1` and `series2`

### Community 115 - "Community 115"
Cohesion: 0.20
Nodes (3): ARIMA, ARIMA -----  Models for ARIMA (Autoregressive integrated moving average) [1]_. T, ARIMA         ARIMA-type models extensible with exogenous variables (future cova

### Community 116 - "Community 116"
Cohesion: 0.20
Nodes (3): ExponentialSmoothing, Exponential Smoothing ---------------------, Exponential Smoothing          This is a wrapper around         `statsmodels  Ho

### Community 117 - "Community 117"
Cohesion: 0.24
Nodes (9): _check_approximate_seasonality(), _compare_timestamps_on_attributes(), _crop_to_match_seasons(), _find_relevant_timestamp_attributes(), Fast Fourier Transform ----------------------, Compares pd.Timestamp instances on attributes.      Compares two timestamps acco, Crops TimeSeries instance to contain full periods.      Crops a given TimeSeries, Checks whether the given series has a given seasonality.      Analyzes the given (+1 more)

### Community 118 - "Community 118"
Cohesion: 0.27
Nodes (3): NegativeBinomialLikelihood, Negative Binomial distribution.          https://en.wikipedia.org/wiki/Negative_, Overwrite the parent since the parameters are extracted in two steps.

### Community 119 - "Community 119"
Cohesion: 0.22
Nodes (2): SKLearnModel Adapter for SHAP Explainer ---------------------------------------, SKLearnShapAdapter

### Community 120 - "Community 120"
Cohesion: 0.20
Nodes (5): Return a DataFrame representation of the series in a given `backend`.          E, Return a new series where the time index was shifted by `n` steps.          If :, Return a new series with the specified window transformations applied., Return a JSON string representation of the deterministic series.          At the, Write the deterministic series to a CSV file.          For a list of parameters,

### Community 121 - "Community 121"
Cohesion: 0.20
Nodes (10): drop_after_index(), drop_before_index(), generate_index(), n_steps_between(), Returns a new Index with the same type as the input `index`, containing the valu, Drops everything before the provided time `split_point` (excluded) from the inde, Drops everything after the provided time `split_point` (excluded) from the index, Get the number of time steps with a given frequency `freq` between `end` and `st (+2 more)

### Community 122 - "Community 122"
Cohesion: 0.22
Nodes (4): _BoundedDetectorMixin, QuantileDetector, Quantile Detector          Flags values that are either below or above the `low_, FittableDetector

### Community 123 - "Community 123"
Cohesion: 0.25
Nodes (4): Applies rotary position embeddings (RoPE) to input tensors.      Implementation, Rotates half the hidden dims of the input., Applies Rotary Position Embedding to the query and key tensors.          Args:, _RoPE

### Community 124 - "Community 124"
Cohesion: 0.22
Nodes (4): _Patch, Chronos-2 Submodels -------------------  --- title: Chronos-2 Submodels summary:, A generic residual block which can be used for input and output embedding layers, _ResidualBlock

### Community 125 - "Community 125"
Cohesion: 0.28
Nodes (4): FittableDetector, Base class of Detectors that require training., Trains the detector on the given time series.          Parameters         ------, Trains the detector and detects anomalies on the same series.          Parameter

### Community 126 - "Community 126"
Cohesion: 0.22
Nodes (5): Anomaly Detectors -----------------  Detectors provide binary anomaly classifica, IQRDetector, Interquartile Range (IQR) Detector ----------------------------------  Flags ano, IQR Detector          Flags values that lie outside of the interquartile range (, QuantileDetector

### Community 127 - "Community 127"
Cohesion: 0.22
Nodes (5): _EncoderMethod, _generate_train_idx(), Encoder Base Classes --------------------, Connects the encoder stage to the corresponding methods, The returned index depends on the following cases:      case 1         (steps_ah

### Community 128 - "Community 128"
Cohesion: 0.22
Nodes (5): HorizonBasedExplainabilityResult, Stores the explainability results of a :class:`_ForecastingModelExplainer     <d, Returns one or several ``TimeSeries`` representing the explanations         for, Helper that extracts and returns the explainability result attribute for a speci, Helper that validates the input parameters of a method that queries the `Horizon

### Community 129 - "Community 129"
Cohesion: 0.22
Nodes (4): _ForecastingModelExplainer, Base Forecasting Model Explainer --------------------------------  A `_Forecasti, Explains a foreground time series, and returns a :class:`_ExplainabilityResult, The base class for forecasting model explainers. It defines the *minimal* behavi

### Community 130 - "Community 130"
Cohesion: 0.22
Nodes (5): AutoARIMA, Auto-ARIMA based on the `Statsforecasts package <https://github.com/Nixtla/stats, TBATS based on the `Statsforecasts package <https://github.com/Nixtla/statsforec, TBATS, StatsForecastModel

### Community 131 - "Community 131"
Cohesion: 0.22
Nodes (3): FourTheta, An implementation of the 4Theta method with configurable `theta` parameter., Performs a grid search over all hyper parameters to select the best model,

### Community 132 - "Community 132"
Cohesion: 0.22
Nodes (3): Theta Method ------------, An implementation of the Theta method with configurable `theta` parameter. See [, Theta

### Community 133 - "Community 133"
Cohesion: 0.22
Nodes (7): quantile_interval_names(), quantile_names(), Base Likelihood Model ---------------------, Generates formatted likelihood parameter names for components and parameter name, Generates formatted quantile names, optionally added to a component name.      P, Generates formatted quantile interval names, optionally added to a component nam, Generates names for the parameters of the Likelihood.

### Community 134 - "Community 134"
Cohesion: 0.22
Nodes (3): Likelihood Models -----------------  Likelihood models for producing probabilist, Weibull distribution.          https://en.wikipedia.org/wiki/Weibull_distributio, WeibullLikelihood

### Community 135 - "Community 135"
Cohesion: 0.22
Nodes (6): MonteCarloDropout, random_method(), Utils for Pytorch and its usage -------------------------------, Defines Monte Carlo dropout Module as defined     in the paper https://arxiv.org, # NOTE: we could use the following line in case a different rate, Decorator usable on any method within a class that will provide an isolated torc

### Community 136 - "Community 136"
Cohesion: 0.25
Nodes (6): ABCMeta, ModelMeta, Base Forecasting Model ----------------------  A forecasting model captures the, # TODO: LocalForecastingModels do not yet handle extreme lags properly. Especial, # TODO: LocalForecastingModels do not yet handle extreme lags properly. Especial, Meta class to store parameters used at model creation.      When creating a mode

### Community 137 - "Community 137"
Cohesion: 0.25
Nodes (3): _Chronos2LayerNorm, _MLP, Construct a layernorm module in the T5 style. No bias and no subtraction of mean

### Community 138 - "Community 138"
Cohesion: 0.32
Nodes (5): _MHA, Multi-head Attention Layer, Eager attention implementation using manual matmul.          Args:             q, SDPA attention implementation using torch.nn.functional.scaled_dot_product_atten, Multi-head attention forward pass.          Args:             hidden_states : In

### Community 139 - "Community 139"
Cohesion: 0.25
Nodes (2): NaiveMovingAverage, Naive Moving Average Model          This model forecasts using an autoregressive

### Community 140 - "Community 140"
Cohesion: 0.25
Nodes (4): Get full description for this estimator (includes all params)., Get short description for this estimator (only includes params with non-default, Get model description string of structure `model_name`(`model_param_key_value_pa, Get parameter key : default_value pairs for the estimator

### Community 141 - "Community 141"
Cohesion: 0.25
Nodes (3): _check_strict_positive(), LogNormalLikelihood, Log-normal distribution.          https://en.wikipedia.org/wiki/Log-normal_distr

### Community 142 - "Community 142"
Cohesion: 0.25
Nodes (2): DirichletLikelihood, Dirichlet distribution.          https://en.wikipedia.org/wiki/Dirichlet_distrib

### Community 143 - "Community 143"
Cohesion: 0.25
Nodes (2): GaussianLikelihood, Univariate Gaussian distribution.          https://en.wikipedia.org/wiki/Normal_

### Community 144 - "Community 144"
Cohesion: 0.25
Nodes (2): PoissonLikelihood, Poisson distribution. Can typically be used to model event counts during time in

### Community 145 - "Community 145"
Cohesion: 0.25
Nodes (3): Anomaly Scorers ---------------  Scorers are at the core of the anomaly detectio, CauchyNLLScorer, NLL Cauchy Scorer -----------------  Cauchy distribution negative log-likelihood

### Community 146 - "Community 146"
Cohesion: 0.25
Nodes (4): Checks if the series is stochastic (number of samples is larger than one)., Extract deterministic values from `series` (quantile=0.5 if `series` is probabil, For each timestamp of the inputs:          - the parameters of the considered di, For each timestamp, the corresponding distribution is fitted on the probabilisti

### Community 147 - "Community 147"
Cohesion: 0.25
Nodes (4): Create a ``TimeSeries`` from a `Series`.          The series must contain an ind, Create a ``TimeSeries`` from the JSON String representation of a ``TimeSeries``., Create a ``TimeSeries`` from a CSV file.          One column can be used to repr, Create a ``TimeSeries`` from a selection of columns of a `DataFrame`.          O

### Community 148 - "Community 148"
Cohesion: 0.25
Nodes (4): Return an ``xarray.DataArray`` representation of the series.          Parameters, Return a new series with the values have been converted to the desired `dtype`., Return a new series where the time index and values were resampled with a given, Create a ``TimeSeries`` from an `xarray.DataArray`.          The dimensions of t

### Community 149 - "Community 149"
Cohesion: 0.25
Nodes (3): Diff, Differencing Transformer ------------------------, r"""Differencing data transformer.          Differencing is typically applied to

### Community 150 - "Community 150"
Cohesion: 0.38
Nodes (2): _Chronos2Encoder, _Chronos2EncoderBlock

### Community 151 - "Community 151"
Cohesion: 0.29
Nodes (2): NaiveSeasonal, Naive Seasonal Model          This model always predicts the value of `K` time s

### Community 152 - "Community 152"
Cohesion: 0.33
Nodes (6): _create_dataset_bounds(), _optimized_historical_forecasts(), Optimized Historical Forecasts for TorchForecastingModel -----------------------, Creates the bounds for the inference dataset based on the input series and wheth, Optimized historical forecasts for TorchForecastingModels      Rely on _check_op, # TODO: is there a better way to call the super().predict() from TorchForecastin

### Community 153 - "Community 153"
Cohesion: 0.29
Nodes (2): BernoulliLikelihood, Bernoulli distribution.          https://en.wikipedia.org/wiki/Bernoulli_distrib

### Community 154 - "Community 154"
Cohesion: 0.29
Nodes (2): BetaLikelihood, Beta distribution.          https://en.wikipedia.org/wiki/Beta_distribution

### Community 155 - "Community 155"
Cohesion: 0.29
Nodes (2): CauchyLikelihood, Cauchy Distribution.          https://en.wikipedia.org/wiki/Cauchy_distribution

### Community 156 - "Community 156"
Cohesion: 0.29
Nodes (2): ContinuousBernoulliLikelihood, Continuous Bernoulli distribution.          https://en.wikipedia.org/wiki/Contin

### Community 157 - "Community 157"
Cohesion: 0.29
Nodes (2): ExponentialLikelihood, Exponential distribution.          https://en.wikipedia.org/wiki/Exponential_dis

### Community 158 - "Community 158"
Cohesion: 0.29
Nodes (2): GammaLikelihood, Gamma distribution.          https://en.wikipedia.org/wiki/Gamma_distribution

### Community 159 - "Community 159"
Cohesion: 0.29
Nodes (2): GumbelLikelihood, Gumbel distribution.          https://en.wikipedia.org/wiki/Gumbel_distribution

### Community 160 - "Community 160"
Cohesion: 0.29
Nodes (2): HalfNormalLikelihood, Half-normal distribution.          https://en.wikipedia.org/wiki/Half-normal_dis

### Community 161 - "Community 161"
Cohesion: 0.29
Nodes (2): LaplaceLikelihood, Laplace distribution.          https://en.wikipedia.org/wiki/Laplace_distributio

### Community 162 - "Community 162"
Cohesion: 0.29
Nodes (3): GammaNLLScorer, NLL Gamma Scorer ----------------  Gamma distribution negative log-likelihood Sc, NLL Gamma Scorer          Parameters         ----------         window

### Community 163 - "Community 163"
Cohesion: 0.29
Nodes (3): GaussianNLLScorer, NLL Gaussian Scorer -------------------  Gaussian negative log-likelihood Scorer, NLL Gaussian Scorer          Parameters         ----------         window

### Community 164 - "Community 164"
Cohesion: 0.33
Nodes (2): _FeedForward, _TimeSelfAttention

### Community 165 - "Community 165"
Cohesion: 0.33
Nodes (4): ElectricityDataset, Measurements of electric power consumption in one household with 15 minute sampl, Parameters         ----------         multivariate: bool             Whether to, Load the electricity dataset as a list of univariate series, one for each househ

### Community 166 - "Community 166"
Cohesion: 0.33
Nodes (4): ExchangeRateDataset, The collection of the daily exchange rates of eight foreign countries, including, Parameters         ----------         multivariate: bool             Whether to, Load the ExchangeRateDataset dataset as a list of univariate timeseries, one for

### Community 167 - "Community 167"
Cohesion: 0.33
Nodes (4): 14.3 million Uber pickups from January to June 2015. The data is resampled to ho, Parameters         ----------         sample_freq: str             The sampling, load the Uber TLC dataset as a list of univariate timeseries, one for each locat, UberTLCDataset

### Community 168 - "Community 168"
Cohesion: 0.33
Nodes (4): The data in this repo is a collection of 48 months (2015-2016) hourly data from, Parameters         ----------         multivariate: bool             Whether to, Load the TrafficDataset dataset as a list of univariate timeseries, one for each, TrafficDataset

### Community 169 - "Community 169"
Cohesion: 0.40
Nodes (3): DartsShapExplanation, Computes SHAP explanations for the given foreground data, horizons, and target c, Similar to :func:`shap_explanations()`, but computes SHAP explanations for only

### Community 170 - "Community 170"
Cohesion: 0.33
Nodes (2): Validation dataloader., Predict/inference dataloader.

### Community 171 - "Community 171"
Cohesion: 0.40
Nodes (2): _InstanceNorm, Apply standardization along the last dimension and optionally apply arcsinh afte

### Community 172 - "Community 172"
Cohesion: 0.40
Nodes (3): ILINetDataset, ILI describes the number of patients seen with influenzalike illness and the tot, Load the ILINetDataset dataset as a list of univariate timeseries.

### Community 173 - "Community 173"
Cohesion: 0.50
Nodes (4): plot(), plot_alignment(), Plots the uni-variate component of each series,     with lines between them indi, Plot the warp path.      Parameters     ----------     new_plot         Boolean

### Community 174 - "Community 174"
Cohesion: 0.40
Nodes (3): NBEATSModel, Neural Basis Expansion Analysis Time Series Forecasting (N-BEATS).          This, PastCovariatesTorchModel

### Community 175 - "Community 175"
Cohesion: 0.40
Nodes (2): AutoMFLES, Auto-MFLES based on the `Statsforecasts package <https://github.com/Nixtla/stats

### Community 176 - "Community 176"
Cohesion: 0.50
Nodes (2): _GroupSelfAttention, Self-attention applied along the batch axis masked by the group attention mask

### Community 177 - "Community 177"
Cohesion: 0.50
Nodes (2): AutoCES, Auto-CES based on the `Statsforecasts package <https://github.com/Nixtla/statsfo

### Community 178 - "Community 178"
Cohesion: 0.50
Nodes (2): AutoETS, Auto-ETS based on the `Statsforecasts package <https://github.com/Nixtla/statsfo

### Community 179 - "Community 179"
Cohesion: 0.50
Nodes (2): AutoTBATS, Auto-TBATS based on the `Statsforecasts package <https://github.com/Nixtla/stats

### Community 180 - "Community 180"
Cohesion: 0.50
Nodes (2): AutoTheta, Auto-Theta based on the `Statsforecasts package <https://github.com/Nixtla/stats

### Community 181 - "Community 181"
Cohesion: 0.50
Nodes (2): Computes the anomaly score between `series` and `pred_series`, and returns the s, Checks if `anomalies` contains only univariate series when the scorer has the

### Community 182 - "Community 182"
Cohesion: 0.50
Nodes (2): Checks if the parameter window is less or equal than the length of the given ser, Computes the anomaly score on the two (sequence of) series.          If a pair o

### Community 183 - "Community 183"
Cohesion: 0.50
Nodes (3): Base Scorer -----------, # TODO:, # TODO: can we use window_transform here?

### Community 184 - "Community 184"
Cohesion: 0.50
Nodes (3): prepare_onnx_inputs(), ONNX Utils ----------, Helper function to slice and concatenate the input features.      In order to re

### Community 185 - "Community 185"
Cohesion: 0.50
Nodes (4): _is_method(), random_method(), Check if the specified function is a method.      Parameters     ----------, Decorator usable on any method within a class that will provide a random context

### Community 186 - "Community 186"
Cohesion: 0.50
Nodes (2): NotImportedModule, Helper class for handling import errors of optional dependencies.

### Community 187 - "Community 187"
Cohesion: 0.67
Nodes (2): Daily temperature in Melbourne between 1981 and 1990, TemperatureDataset

### Community 188 - "Community 188"
Cohesion: 0.67
Nodes (2): Weekly U.S. Product Supplied of Finished Motor Gasoline between 1991-02-08 and 2, USGasolineDataset

### Community 189 - "Community 189"
Cohesion: 0.67
Nodes (2): Quarterly production of woollen yarn in Australia: tonnes. Mar 1965 -- Sep 1994., WoolyDataset

### Community 190 - "Community 190"
Cohesion: 0.67
Nodes (2): Taxi Passengers in New York, from 2014-07 to 2015-01.     The data consists of a, TaxiNewYorkDataset

### Community 191 - "Community 191"
Cohesion: 1.00
Nodes (1): Model Components ----------------  Internal components and building blocks used

### Community 192 - "Community 192"
Cohesion: 1.00
Nodes (1): Filtering Models ----------------  Models for filtering and smoothing time serie

### Community 193 - "Community 193"
Cohesion: 1.00
Nodes (1): Forecasting Models ==================  Regression Models -----------------  Base

### Community 194 - "Community 194"
Cohesion: 1.00
Nodes (2): ase(), Absolute Scaled Error (ASE) (see [1]_ for more information on scaled forecasting

### Community 195 - "Community 195"
Cohesion: 1.00
Nodes (2): autc(), Area Under Tolerance Curve (AUTC).      AUTC measures the overall alignment betw

### Community 196 - "Community 196"
Cohesion: 1.00
Nodes (2): coefficient_of_variation(), Coefficient of Variation (percentage).      For the true series :math:`y` and pr

### Community 197 - "Community 197"
Cohesion: 1.00
Nodes (2): confusion_matrix(), Confusion Matrix (CM) [1]_.      For the true series :math:`y` and predicted ser

### Community 198 - "Community 198"
Cohesion: 1.00
Nodes (2): crps(), Continuous Ranked Probability Score (CRPS).      CRPS is a proper scoring rule t

### Community 199 - "Community 199"
Cohesion: 1.00
Nodes (2): dtw_metric(), Applies Dynamic Time Warping to `actual_series` and `pred_series` before passing

### Community 200 - "Community 200"
Cohesion: 1.00
Nodes (2): err(), Error (ERR).      For the true series :math:`y` and predicted series :math:`\\ha

### Community 201 - "Community 201"
Cohesion: 1.00
Nodes (2): f1(), F1 Score [1]_.      For the true series :math:`y` and predicted series :math:`\\

### Community 202 - "Community 202"
Cohesion: 1.00
Nodes (2): ic(), Interval Coverage (IC).      IC gives a binary outcome with `1` if the observati

### Community 203 - "Community 203"
Cohesion: 1.00
Nodes (2): incs_qr(), Interval Non-Conformity Score for Quantile Regression (INCS_QR).      INCS_QR gi

### Community 204 - "Community 204"
Cohesion: 1.00
Nodes (2): iw(), Interval Width (IW).      IL gives the width / length of predicted quantile inte

### Community 205 - "Community 205"
Cohesion: 1.00
Nodes (2): iws(), Interval Winkler Score (IWS) [1]_.      IWS gives the length / width of the quan

### Community 206 - "Community 206"
Cohesion: 1.00
Nodes (2): mae(), Mean Absolute Error (MAE).      For the true series :math:`y` and predicted seri

### Community 207 - "Community 207"
Cohesion: 1.00
Nodes (2): mape(), Mean Absolute Percentage Error (MAPE).      For the true series :math:`y` and pr

### Community 208 - "Community 208"
Cohesion: 1.00
Nodes (2): marre(), Mean Absolute Ranged Relative Error (MARRE).      For the true series :math:`y`

### Community 209 - "Community 209"
Cohesion: 1.00
Nodes (2): mase(), Mean Absolute Scaled Error (MASE) (see [1]_ for more information on scaled forec

### Community 210 - "Community 210"
Cohesion: 1.00
Nodes (2): mcrps(), Mean Continuous Ranked Probability Score (MCRPS).      MCRPS is a proper scoring

### Community 211 - "Community 211"
Cohesion: 1.00
Nodes (2): merr(), Mean Error (MERR).      For the true series :math:`y` and predicted series :math

### Community 212 - "Community 212"
Cohesion: 1.00
Nodes (2): mic(), Mean Interval Coverage (MIC).      MIC gives the time-aggregated Interval Covera

### Community 213 - "Community 213"
Cohesion: 1.00
Nodes (2): mincs_qr(), Mean Interval Non-Conformity Score for Quantile Regression (MINCS_QR).      MINC

### Community 214 - "Community 214"
Cohesion: 1.00
Nodes (2): miw(), Mean Interval Width (MIW).      MIW gives the time-aggregated width / length of

### Community 215 - "Community 215"
Cohesion: 1.00
Nodes (2): miws(), Mean Interval Winkler Score (IWS) [1]_.      MIWS gives the time-aggregated leng

### Community 216 - "Community 216"
Cohesion: 1.00
Nodes (2): mql(), Mean Quantile Loss (MQL).      Also known as Pinball Loss. QL is a metric that q

### Community 217 - "Community 217"
Cohesion: 1.00
Nodes (2): mse(), Mean Squared Error (MSE).      For the true series :math:`y` and predicted serie

### Community 218 - "Community 218"
Cohesion: 1.00
Nodes (2): msse(), Mean Squared Scaled Error (MSSE) (see [1]_ for more information on scaled foreca

### Community 219 - "Community 219"
Cohesion: 1.00
Nodes (2): ope(), Overall Percentage Error (OPE).      For the true series :math:`y` and predicted

### Community 220 - "Community 220"
Cohesion: 1.00
Nodes (2): precision(), Precision Score [1]_.      For the true series :math:`y` and predicted series :m

### Community 221 - "Community 221"
Cohesion: 1.00
Nodes (2): ql(), Quantile Loss (QL).      Also known as Pinball Loss. QL is a metric that quantif

### Community 222 - "Community 222"
Cohesion: 1.00
Nodes (2): qr(), Quantile Risk (QR)      QR is a metric that quantifies the accuracy of a specifi

### Community 223 - "Community 223"
Cohesion: 1.00
Nodes (2): r2_score(), Coefficient of Determination :math:`R^2` (see [1]_ for more details).      For t

### Community 224 - "Community 224"
Cohesion: 1.00
Nodes (2): Root Mean Squared Error (RMSE).      For the true series :math:`y` and predicted, rmse()

### Community 225 - "Community 225"
Cohesion: 1.00
Nodes (2): Root Mean Squared Scaled Error (RMSSE) (see [1]_ for more information on scaled, rmsse()

### Community 226 - "Community 226"
Cohesion: 1.00
Nodes (2): Squared Log Error (SLE).      For the true series :math:`y` and predicted series, sle()

### Community 227 - "Community 227"
Cohesion: 1.00
Nodes (2): Root Mean Squared Log Error (RMSLE).      For the true series :math:`y` and pred, rmsle()

### Community 228 - "Community 228"
Cohesion: 1.00
Nodes (2): Weighted Mean Absolute Percentage Error (WMAPE). (see [1]_ for more information), wmape()

### Community 229 - "Community 229"
Cohesion: 1.00
Nodes (2): symmetric Absolute Percentage Error (sAPE).      For the true series :math:`y` a, sape()

### Community 230 - "Community 230"
Cohesion: 1.00
Nodes (2): symmetric Mean Absolute Percentage Error (sMAPE).      For the true series :math, smape()

### Community 231 - "Community 231"
Cohesion: 1.00
Nodes (2): Computes the tolerance coverages for different tolerance levels.      More info, _tolerance_coverages()

### Community 232 - "Community 232"
Cohesion: 1.00
Nodes (2): Recall Score [1]_.      For the true series :math:`y` and predicted series :math, recall()

### Community 233 - "Community 233"
Cohesion: 1.00
Nodes (2): Squared Error (SE).      For the true series :math:`y` and predicted series :mat, se()

### Community 234 - "Community 234"
Cohesion: 1.00
Nodes (1): Model Adapters for SHAP Explainer ---------------------------------

### Community 235 - "Community 235"
Cohesion: 1.00
Nodes (1): Tabularization for SKLearnModel -------------------------------  Functions for c

### Community 236 - "Community 236"
Cohesion: 1.00
Nodes (1): Datasets for TorchForecastingModel ----------------------------------  PyTorch d

### Community 237 - "Community 237"
Cohesion: 1.00
Nodes (1): Utils -----  Utility functions and helper classes for various operations in Dart

### Community 238 - "Community 238"
Cohesion: 1.00
Nodes (2): dataframe_col_to_time_index(), Convert a dataframe column to a pandas Index or DatetimeIndex.      Parameters

### Community 239 - "Community 239"
Cohesion: 1.00
Nodes (2): expand_arr(), Expands a np.ndarray to `ndim` dimensions (if not already satisfied).

### Community 240 - "Community 240"
Cohesion: 1.00
Nodes (2): infer_freq_intersection(), Infers the frequency at which two frequencies `freq` and `other` intersect.

### Community 241 - "Community 241"
Cohesion: 1.00
Nodes (2): _maybe_cast_array_dtype(), Cast an array to `dtype` if it does not yet have the correct data type.

### Community 242 - "Community 242"
Cohesion: 1.00
Nodes (2): _parallel_apply(), Utility function that parallelise the execution of a function over an Iterator

### Community 243 - "Community 243"
Cohesion: 1.00
Nodes (2): Decorator allowing to specify some sanity check method(s) to be used on a class, _with_sanity_checks()

### Community 244 - "Community 244"
Cohesion: 1.00
Nodes (2): Generates `num_samples` samples from quantile predictions using linear interpola, sample_from_quantiles()

## Knowledge Gaps
- **577 isolated node(s):** `Anomaly Detection -----------------  A suite of tools for performing anomaly det`, `Base Aggregator ---------------`, `Base class for Aggregators.`, `returns the name of the aggregator`, `Aggregates the sequence of multivariate binary series given as         input int` (+572 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 109`** (1 nodes): `NeuralForecastModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 119`** (2 nodes): `SKLearnModel Adapter for SHAP Explainer ---------------------------------------`, `SKLearnShapAdapter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 139`** (2 nodes): `NaiveMovingAverage`, `Naive Moving Average Model          This model forecasts using an autoregressive`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 142`** (2 nodes): `DirichletLikelihood`, `Dirichlet distribution.          https://en.wikipedia.org/wiki/Dirichlet_distrib`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 143`** (2 nodes): `GaussianLikelihood`, `Univariate Gaussian distribution.          https://en.wikipedia.org/wiki/Normal_`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 144`** (2 nodes): `PoissonLikelihood`, `Poisson distribution. Can typically be used to model event counts during time in`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 150`** (2 nodes): `_Chronos2Encoder`, `_Chronos2EncoderBlock`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 151`** (2 nodes): `NaiveSeasonal`, `Naive Seasonal Model          This model always predicts the value of `K` time s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 153`** (2 nodes): `BernoulliLikelihood`, `Bernoulli distribution.          https://en.wikipedia.org/wiki/Bernoulli_distrib`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 154`** (2 nodes): `BetaLikelihood`, `Beta distribution.          https://en.wikipedia.org/wiki/Beta_distribution`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 155`** (2 nodes): `CauchyLikelihood`, `Cauchy Distribution.          https://en.wikipedia.org/wiki/Cauchy_distribution`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 156`** (2 nodes): `ContinuousBernoulliLikelihood`, `Continuous Bernoulli distribution.          https://en.wikipedia.org/wiki/Contin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 157`** (2 nodes): `ExponentialLikelihood`, `Exponential distribution.          https://en.wikipedia.org/wiki/Exponential_dis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 158`** (2 nodes): `GammaLikelihood`, `Gamma distribution.          https://en.wikipedia.org/wiki/Gamma_distribution`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 159`** (2 nodes): `GumbelLikelihood`, `Gumbel distribution.          https://en.wikipedia.org/wiki/Gumbel_distribution`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 160`** (2 nodes): `HalfNormalLikelihood`, `Half-normal distribution.          https://en.wikipedia.org/wiki/Half-normal_dis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 161`** (2 nodes): `LaplaceLikelihood`, `Laplace distribution.          https://en.wikipedia.org/wiki/Laplace_distributio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 164`** (2 nodes): `_FeedForward`, `_TimeSelfAttention`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 170`** (2 nodes): `Validation dataloader.`, `Predict/inference dataloader.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 171`** (2 nodes): `_InstanceNorm`, `Apply standardization along the last dimension and optionally apply arcsinh afte`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 175`** (2 nodes): `AutoMFLES`, `Auto-MFLES based on the `Statsforecasts package <https://github.com/Nixtla/stats`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 176`** (2 nodes): `_GroupSelfAttention`, `Self-attention applied along the batch axis masked by the group attention mask`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 177`** (2 nodes): `AutoCES`, `Auto-CES based on the `Statsforecasts package <https://github.com/Nixtla/statsfo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 178`** (2 nodes): `AutoETS`, `Auto-ETS based on the `Statsforecasts package <https://github.com/Nixtla/statsfo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 179`** (2 nodes): `AutoTBATS`, `Auto-TBATS based on the `Statsforecasts package <https://github.com/Nixtla/stats`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 180`** (2 nodes): `AutoTheta`, `Auto-Theta based on the `Statsforecasts package <https://github.com/Nixtla/stats`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 181`** (2 nodes): `Computes the anomaly score between `series` and `pred_series`, and returns the s`, `Checks if `anomalies` contains only univariate series when the scorer has the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 182`** (2 nodes): `Checks if the parameter window is less or equal than the length of the given ser`, `Computes the anomaly score on the two (sequence of) series.          If a pair o`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 186`** (2 nodes): `NotImportedModule`, `Helper class for handling import errors of optional dependencies.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 187`** (2 nodes): `Daily temperature in Melbourne between 1981 and 1990`, `TemperatureDataset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 188`** (2 nodes): `Weekly U.S. Product Supplied of Finished Motor Gasoline between 1991-02-08 and 2`, `USGasolineDataset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 189`** (2 nodes): `Quarterly production of woollen yarn in Australia: tonnes. Mar 1965 -- Sep 1994.`, `WoolyDataset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (2 nodes): `Taxi Passengers in New York, from 2014-07 to 2015-01.     The data consists of a`, `TaxiNewYorkDataset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 191`** (1 nodes): `Model Components ----------------  Internal components and building blocks used`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 192`** (1 nodes): `Filtering Models ----------------  Models for filtering and smoothing time serie`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 193`** (1 nodes): `Forecasting Models ==================  Regression Models -----------------  Base`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 194`** (2 nodes): `ase()`, `Absolute Scaled Error (ASE) (see [1]_ for more information on scaled forecasting`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 195`** (2 nodes): `autc()`, `Area Under Tolerance Curve (AUTC).      AUTC measures the overall alignment betw`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 196`** (2 nodes): `coefficient_of_variation()`, `Coefficient of Variation (percentage).      For the true series :math:`y` and pr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 197`** (2 nodes): `confusion_matrix()`, `Confusion Matrix (CM) [1]_.      For the true series :math:`y` and predicted ser`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 198`** (2 nodes): `crps()`, `Continuous Ranked Probability Score (CRPS).      CRPS is a proper scoring rule t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 199`** (2 nodes): `dtw_metric()`, `Applies Dynamic Time Warping to `actual_series` and `pred_series` before passing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 200`** (2 nodes): `err()`, `Error (ERR).      For the true series :math:`y` and predicted series :math:`\\ha`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 201`** (2 nodes): `f1()`, `F1 Score [1]_.      For the true series :math:`y` and predicted series :math:`\\`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 202`** (2 nodes): `ic()`, `Interval Coverage (IC).      IC gives a binary outcome with `1` if the observati`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 203`** (2 nodes): `incs_qr()`, `Interval Non-Conformity Score for Quantile Regression (INCS_QR).      INCS_QR gi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 204`** (2 nodes): `iw()`, `Interval Width (IW).      IL gives the width / length of predicted quantile inte`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 205`** (2 nodes): `iws()`, `Interval Winkler Score (IWS) [1]_.      IWS gives the length / width of the quan`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 206`** (2 nodes): `mae()`, `Mean Absolute Error (MAE).      For the true series :math:`y` and predicted seri`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 207`** (2 nodes): `mape()`, `Mean Absolute Percentage Error (MAPE).      For the true series :math:`y` and pr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 208`** (2 nodes): `marre()`, `Mean Absolute Ranged Relative Error (MARRE).      For the true series :math:`y``
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 209`** (2 nodes): `mase()`, `Mean Absolute Scaled Error (MASE) (see [1]_ for more information on scaled forec`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 210`** (2 nodes): `mcrps()`, `Mean Continuous Ranked Probability Score (MCRPS).      MCRPS is a proper scoring`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 211`** (2 nodes): `merr()`, `Mean Error (MERR).      For the true series :math:`y` and predicted series :math`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 212`** (2 nodes): `mic()`, `Mean Interval Coverage (MIC).      MIC gives the time-aggregated Interval Covera`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 213`** (2 nodes): `mincs_qr()`, `Mean Interval Non-Conformity Score for Quantile Regression (MINCS_QR).      MINC`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 214`** (2 nodes): `miw()`, `Mean Interval Width (MIW).      MIW gives the time-aggregated width / length of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 215`** (2 nodes): `miws()`, `Mean Interval Winkler Score (IWS) [1]_.      MIWS gives the time-aggregated leng`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 216`** (2 nodes): `mql()`, `Mean Quantile Loss (MQL).      Also known as Pinball Loss. QL is a metric that q`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 217`** (2 nodes): `mse()`, `Mean Squared Error (MSE).      For the true series :math:`y` and predicted serie`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 218`** (2 nodes): `msse()`, `Mean Squared Scaled Error (MSSE) (see [1]_ for more information on scaled foreca`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 219`** (2 nodes): `ope()`, `Overall Percentage Error (OPE).      For the true series :math:`y` and predicted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 220`** (2 nodes): `precision()`, `Precision Score [1]_.      For the true series :math:`y` and predicted series :m`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 221`** (2 nodes): `ql()`, `Quantile Loss (QL).      Also known as Pinball Loss. QL is a metric that quantif`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 222`** (2 nodes): `qr()`, `Quantile Risk (QR)      QR is a metric that quantifies the accuracy of a specifi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 223`** (2 nodes): `r2_score()`, `Coefficient of Determination :math:`R^2` (see [1]_ for more details).      For t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 224`** (2 nodes): `Root Mean Squared Error (RMSE).      For the true series :math:`y` and predicted`, `rmse()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 225`** (2 nodes): `Root Mean Squared Scaled Error (RMSSE) (see [1]_ for more information on scaled`, `rmsse()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 226`** (2 nodes): `Squared Log Error (SLE).      For the true series :math:`y` and predicted series`, `sle()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 227`** (2 nodes): `Root Mean Squared Log Error (RMSLE).      For the true series :math:`y` and pred`, `rmsle()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 228`** (2 nodes): `Weighted Mean Absolute Percentage Error (WMAPE). (see [1]_ for more information)`, `wmape()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 229`** (2 nodes): `symmetric Absolute Percentage Error (sAPE).      For the true series :math:`y` a`, `sape()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 230`** (2 nodes): `symmetric Mean Absolute Percentage Error (sMAPE).      For the true series :math`, `smape()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 231`** (2 nodes): `Computes the tolerance coverages for different tolerance levels.      More info`, `_tolerance_coverages()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 232`** (2 nodes): `Recall Score [1]_.      For the true series :math:`y` and predicted series :math`, `recall()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 233`** (2 nodes): `Squared Error (SE).      For the true series :math:`y` and predicted series :mat`, `se()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 234`** (1 nodes): `Model Adapters for SHAP Explainer ---------------------------------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 235`** (1 nodes): `Tabularization for SKLearnModel -------------------------------  Functions for c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 236`** (1 nodes): `Datasets for TorchForecastingModel ----------------------------------  PyTorch d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 237`** (1 nodes): `Utils -----  Utility functions and helper classes for various operations in Dart`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 238`** (2 nodes): `dataframe_col_to_time_index()`, `Convert a dataframe column to a pandas Index or DatetimeIndex.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 239`** (2 nodes): `expand_arr()`, `Expands a np.ndarray to `ndim` dimensions (if not already satisfied).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 240`** (2 nodes): `infer_freq_intersection()`, `Infers the frequency at which two frequencies `freq` and `other` intersect.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 241`** (2 nodes): `_maybe_cast_array_dtype()`, `Cast an array to `dtype` if it does not yet have the correct data type.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 242`** (2 nodes): `_parallel_apply()`, `Utility function that parallelise the execution of a function over an Iterator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 243`** (2 nodes): `Decorator allowing to specify some sanity check method(s) to be used on a class`, `_with_sanity_checks()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 244`** (2 nodes): `Generates `num_samples` samples from quantile predictions using linear interpola`, `sample_from_quantiles()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TimeSeries` connect `Community 3` to `Community 59`, `Community 18`, `Community 44`, `Community 52`, `Community 53`, `Community 103`, `Community 94`, `Community 148`, `Community 23`, `Community 65`, `Community 147`, `Community 75`, `Community 120`, `Community 28`, `Community 45`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Why does `SeriesType` connect `Community 13` to `Community 39`, `Community 5`, `Community 1`, `Community 40`, `Community 92`, `Community 136`, `Community 2`, `Community 11`, `Community 140`, `Community 38`, `Community 0`, `Community 49`, `Community 18`, `Community 25`, `Community 28`, `Community 96`, `Community 69`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Why does `PLForecastingModule` connect `Community 0` to `Community 4`, `Community 56`, `Community 27`, `Community 60`, `Community 174`, `Community 109`, `Community 49`, `Community 20`, `Community 9`, `Community 1`, `Community 38`, `Community 73`, `Community 32`, `Community 5`, `Community 31`, `Community 74`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Are the 250 inferred relationships involving `PLForecastingModule` (e.g. with `HuggingFaceConnector` and `Hugging Face Connector ----------------------`) actually correct?**
  _`PLForecastingModule` has 250 INFERRED edges - model-reasoned connections that need verification._
- **Are the 242 inferred relationships involving `SeriesType` (e.g. with `TFTModel Explainer ------------------  The `TFTExplainer` uses a trained :class:` and `Returns the :class:`TFTExplainabilityResult         <darts.explainability.explai`) actually correct?**
  _`SeriesType` has 242 INFERRED edges - model-reasoned connections that need verification._
- **Are the 37 inferred relationships involving `TimeSeries` (e.g. with `MultivariateModel` and `Multivariate Model ------------------  A wrapper around any base forecasting mod`) actually correct?**
  _`TimeSeries` has 37 INFERRED edges - model-reasoned connections that need verification._
- **Are the 184 inferred relationships involving `Likelihood` (e.g. with `ConformalModel` and `ConformalNaiveModel`) actually correct?**
  _`Likelihood` has 184 INFERRED edges - model-reasoned connections that need verification._