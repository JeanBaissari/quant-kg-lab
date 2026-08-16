# Graph Report - knowledge_graphs/catboost/repo/catboost/python-package/catboost  (2026-08-13)

## Corpus Check
- 39 files · ~53,036 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 793 nodes · 1569 edges · 52 communities detected
- Non-singleton communities: 47
- Extraction: EXTRACTED: 80.1% · INFERRED: 19.9%
- Edge kinds: calls: 444 · contains: 201 · imports: 5 · imports_from: 24 · inherits: 38 · method: 362 · rationale_for: 182 · uses: 313

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 39 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `549af60`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `BuiltinMetric` (123)
- `OfflineMetricVisualizer` (122)
- `_CatBoostBase` (84)
- `core.py` (70)
- `Pool` (68)
- `CatBoost` (52)
- `.__init__()` (31)
- `.is_fitted()` (29)
- `helpers.h` (25)
- `MetricEvaluationResult` (24)

## Surprising Connections (you probably didn't know these)
- `polars` --uses--> `Pool`  [INFERRED]
  utils.py → core.py
- `Reads CatBoost column description file     (see https://catboost.ai/docs/concept` --uses--> `Pool`  [INFERRED]
  utils.py → core.py
- `Evaluate metrics with raw approxes and labels.      Parameters     ----------` --uses--> `Pool`  [INFERRED]
  utils.py → core.py
- `Build confusion matrix.      Parameters     ----------     model : catboost.CatB` --uses--> `Pool`  [INFERRED]
  utils.py → core.py
- `Build points of ROC curve.      Parameters     ----------     model : catboost.C` --uses--> `Pool`  [INFERRED]
  utils.py → core.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (44): BatchMetricCalcer, _build_binarized_feature_statistics_fig(), _build_train_pool(), _calc_feature_statistics_layout(), _cast_to_base_types(), _cast_value_to_list_of_strings(), CatBoost, _check_param_type() (+36 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (75): EFeaturesSelectionAlgorithm, EFeaturesSelectionGrouping, EFstrType, EShapCalcType, pandas, polars, estimator_type must be 'classifier', 'regressor', 'ranker' or None         train, # NOTE: Special case, avoiding new list creation. (+67 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (19): _FoldFile, FoldStorage, This module contains the abstractions for keeping small amount of data. It provi, Remove default directory for folds if there're no files nut models. In other way, Args:             :return: (str) Delimiter for data used when we saved fold to f, Args:             :return: (str) Path to the column description., Args:             :param group_id: (int) The number of group we want to check., FoldFile is the realisation of the interface of FoldStorage. It always saves dat (+11 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (18): DataFrame, Pool, Check type of weight parameter., Check type of group_id parameter., Check group_id length., Check type of group_weight parameter., Check group_weight length., Check type of subgroup_id parameter. (+10 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (20): Series, _TrainCallbacksWrapper, _BaseReader, Simple file reader. It intends to read lines from big files. Also it provides th, _SimpleDataReader, _SimpleStreamingFileReader, _current_params(), DataFrame (+12 more)

### Community 5 - "Community 5"
Cohesion: 0.08
Nodes (14): DOMWidget, MetricWidget, lgbm_plotting_callback(), XGBoost callback with metrics plotting widget from CatBoost, LightGBM callback with metrics plotting widget from CatBoost, XGBPlottingCallback, XGBTrainingCallback, MetricVisualizer (+6 more)

### Community 6 - "Community 6"
Cohesion: 0.08
Nodes (30): calc_features_strength(), _check_model(), explain_features(), plot_features_strength(), plot_pdp(), to_polynom(), to_polynom_string(), convert_to_onnx_object() (+22 more)

### Community 7 - "Community 7"
Cohesion: 0.08
Nodes (6): CatBoostClassifier, CatBoostRanker, CatBoostRegressor, Implementation of the scikit-learn estimator API for CatBoost regression.      S, Predict with data.         Parameters         ----------         X : catboost.Po, Calculate NDCG@top         Parameters         ----------         X : catboost.Po

### Community 8 - "Community 8"
Cohesion: 0.09
Nodes (1): _CatBoostBase

### Community 9 - "Community 9"
Cohesion: 0.09
Nodes (6): GetCachedLocalExecutor(), GetNumFeatureValuesSample(), BuildPolynom(), ConvertFullModelToPolynom(), ConvertFullModelToPolynomString(), ExplainFeatures()

### Community 10 - "Community 10"
Cohesion: 0.13
Nodes (25): adult(), amazon(), _cached_download(), _calc_md5(), _download_dataset(), _ensure_dir_exists(), epsilon(), _extract() (+17 more)

### Community 11 - "Community 11"
Cohesion: 0.14
Nodes (13): Enum, CatboostEvaluation, EvalType, This method calculate metrics and return them.          Args:             :param, Type of feature evaluation:             All: All factors presented             S, Evaluate features.             Args:             learn_config: dict with params, More flexible evaluation of any cases.             Args:             baseline_ca, Args:             :param path_to_dataset: (str) Path to the dataset to be used f (+5 more)

### Community 12 - "Community 12"
Cohesion: 0.09
Nodes (12): MetricEvaluationResult, Evaluation result for one metric.         Stores all ExecutionCases with specifi, :return: ExecutionCases used as a baseline (with everything else is compared), :return: Cases which are compared, :return: Metric for which results were calculated, Method to get human-friendly table with model comparisons.          Returns base, Method to get human-friendly table with model comparisons.         Same as get_b, :param case: new baseline case         :return: (+4 more)

### Community 13 - "Community 13"
Cohesion: 0.13
Nodes (7): FoldModel, This class provides the abstraction of model. I.e. it is an object relevant to p, FoldModelsHandler, Train models for each algorithm and learn dataset(folds). Than return them., Class that is responsible for learning models and computing their metrics, Run all processes to gain stats. It applies algorithms to fold files that gains, Args:             :param remove_models: Set true if you want models to be remove

### Community 14 - "Community 14"
Cohesion: 0.09
Nodes (11): CaseEvaluationResult, ExecutionCases for this result, :return: FoldsIds for which this caseResult was calculated, :param fold: id of fold to get result         :return: best metric value, best m, :param fold:         :return: fold learning curve (test scores on every eval_per, :return: Metric used to build this CaseEvaluationResult, :return: step which was used for metric computations, :param overfit_border: min fraction of iterations until overfitting starts one e (+3 more)

### Community 15 - "Community 15"
Cohesion: 0.12
Nodes (13): AsyncAddArrowCategoricalColumnOfIntOrBoolean(), AsyncAddArrowCategoricalColumnOfStrings(), AsyncAddArrowNumColumn(), AsyncAddArrowTextColumn(), ProcessArrowArrayStream(), ProcessNonNullableColumn(), ProcessNonNullableStringColumn(), TArrayLikeAsFloatBlockIterator (+5 more)

### Community 18 - "Community 18"
Cohesion: 0.19
Nodes (2): ExecutionCase, Instances of this class are cases which will be compared during evaluation

### Community 19 - "Community 19"
Cohesion: 0.21
Nodes (2): CatboostIpythonWidget, CatboostWidgetModel

### Community 20 - "Community 20"
Cohesion: 0.20
Nodes (6): calc_bootstrap_ci_for_mean(), calc_wilcoxon_test(), :return: pandas Series with best iterations on all folds, :return: pandas series with best metric values, Count confidence intervals for difference each two samples.      Args:         :, ScoreType

### Community 23 - "Community 23"
Cohesion: 0.29
Nodes (3): Config to present human-friendly evaluation results., :param score_type: type of score. For abs difference score will be (baseline - t, ScoreConfig

### Community 24 - "Community 24"
Cohesion: 0.43
Nodes (1): FactorUtils

### Community 26 - "Community 26"
Cohesion: 0.29
Nodes (2): Check files existence., Check type of column_description parameter.

### Community 27 - "Community 27"
Cohesion: 0.33
Nodes (2): Check type of pairs or graph parameter., Check values in pairs or graph parameter. Must be int indices.

### Community 28 - "Community 28"
Cohesion: 0.40
Nodes (4): carry(), Parameters     ----------     model :         CatBoost / CatBoostClassifier / Ca, Parameters     ----------     model :         CatBoost / CatBoostClassifier / Ca, uplift()

### Community 29 - "Community 29"
Cohesion: 0.40
Nodes (2): sample_gaussian_process(), sum_models()

### Community 30 - "Community 30"
Cohesion: 0.40
Nodes (1): Module that contains different utils functions.

### Community 31 - "Community 31"
Cohesion: 0.40
Nodes (1): save_plot_file()

### Community 35 - "Community 35"
Cohesion: 1.00
Nodes (1): Check label is not empty.

### Community 36 - "Community 36"
Cohesion: 1.00
Nodes (1): Check label length and dimension.

### Community 37 - "Community 37"
Cohesion: 1.00
Nodes (1): Check type of cat_feature parameter.

### Community 38 - "Community 38"
Cohesion: 1.00
Nodes (1): Check values in cat_feature parameter. Must be int indices.

### Community 39 - "Community 39"
Cohesion: 1.00
Nodes (1): Quantize this dataset          Parameters         ----------         ignored_fea

### Community 40 - "Community 40"
Cohesion: 1.00
Nodes (1): Save the quantized dataset to a file.          Parameters         ----------

### Community 41 - "Community 41"
Cohesion: 1.00
Nodes (1): Evaluate the metric with raw approxes and labels.          Parameters         --

### Community 42 - "Community 42"
Cohesion: 1.00
Nodes (1): Returns         ----------         bool : True if metric is maximizable, False o

### Community 43 - "Community 43"
Cohesion: 1.00
Nodes (1): Returns         ----------         bool :  True if metric is minimizable, False

### Community 44 - "Community 44"
Cohesion: 1.00
Nodes (1): Sets hints for the metric. Hints are not validated.         Implemented in child

### Community 45 - "Community 45"
Cohesion: 1.00
Nodes (1): Gets the representation of the metric object with overridden parameters.

## Knowledge Gaps
- **55 isolated node(s):** `Parameters     ----------     model :         CatBoost / CatBoostClassifier / Ca`, `Parameters     ----------     model :         CatBoost / CatBoostClassifier / Ca`, `Contains information from kaggle [1], which is made available here under the Ope`, `Download "epsilon" [1] data set.      Will return two pandas.DataFrame-s, first`, `Dataset with monotonic constraints.     Can be used for poisson regression.` (+50 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 8`** (1 nodes): `_CatBoostBase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (2 nodes): `ExecutionCase`, `Instances of this class are cases which will be compared during evaluation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (2 nodes): `CatboostIpythonWidget`, `CatboostWidgetModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `FactorUtils`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (2 nodes): `Check files existence.`, `Check type of column_description parameter.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (2 nodes): `Check type of pairs or graph parameter.`, `Check values in pairs or graph parameter. Must be int indices.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (2 nodes): `sample_gaussian_process()`, `sum_models()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (1 nodes): `Module that contains different utils functions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (1 nodes): `save_plot_file()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (1 nodes): `Check label is not empty.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (1 nodes): `Check label length and dimension.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (1 nodes): `Check type of cat_feature parameter.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (1 nodes): `Check values in cat_feature parameter. Must be int indices.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `Quantize this dataset          Parameters         ----------         ignored_fea`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `Save the quantized dataset to a file.          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (1 nodes): `Evaluate the metric with raw approxes and labels.          Parameters         --`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (1 nodes): `Returns         ----------         bool : True if metric is maximizable, False o`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (1 nodes): `Returns         ----------         bool :  True if metric is minimizable, False`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (1 nodes): `Sets hints for the metric. Hints are not validated.         Implemented in child`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (1 nodes): `Gets the representation of the metric object with overridden parameters.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BuiltinMetric` connect `Community 1` to `Community 0`, `Community 8`, `Community 7`, `Community 3`, `Community 40`, `Community 39`, `Community 26`, `Community 37`, `Community 38`, `Community 27`, `Community 35`, `Community 36`, `Community 4`, `Community 41`, `Community 42`, `Community 43`, `Community 44`, `Community 45`?**
  _High betweenness centrality (0.176) - this node is a cross-community bridge._
- **Why does `_CatBoostBase` connect `Community 8` to `Community 0`, `Community 21`, `Community 7`, `Community 22`, `Community 16`, `Community 17`, `Community 29`, `Community 25`, `Community 32`, `Community 1`, `Community 4`?**
  _High betweenness centrality (0.158) - this node is a cross-community bridge._
- **Why does `OfflineMetricVisualizer` connect `Community 1` to `Community 0`, `Community 8`, `Community 7`, `Community 3`, `Community 40`, `Community 39`, `Community 26`, `Community 37`, `Community 38`, `Community 27`, `Community 35`, `Community 36`, `Community 4`, `Community 31`, `Community 33`?**
  _High betweenness centrality (0.144) - this node is a cross-community bridge._
- **Are the 115 inferred relationships involving `BuiltinMetric` (e.g. with `BatchMetricCalcer` and `CatBoost`) actually correct?**
  _`BuiltinMetric` has 115 INFERRED edges - model-reasoned connections that need verification._
- **Are the 115 inferred relationships involving `OfflineMetricVisualizer` (e.g. with `BatchMetricCalcer` and `CatBoost`) actually correct?**
  _`OfflineMetricVisualizer` has 115 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `_CatBoostBase` (e.g. with `BuiltinMetric` and `OfflineMetricVisualizer`) actually correct?**
  _`_CatBoostBase` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 14 inferred relationships involving `Pool` (e.g. with `BuiltinMetric` and `OfflineMetricVisualizer`) actually correct?**
  _`Pool` has 14 INFERRED edges - model-reasoned connections that need verification._