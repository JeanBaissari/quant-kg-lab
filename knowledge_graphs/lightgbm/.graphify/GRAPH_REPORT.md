# Graph Report - lightgbm  (2026-08-06)

## Corpus Check
- Corpus is ~42,094 words - fits in a single context window. You may not need a graph.

## Summary
- 594 nodes · 2099 edges · 17 communities detected
- Extraction: 51% EXTRACTED · 49% INFERRED · 0% AMBIGUOUS · INFERRED: 1026 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: uses: 1026 · calls: 459 · rationale_for: 240 · method: 209 · contains: 122 · imports_from: 24 · inherits: 18 · imports: 1


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 9 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `f9bf8d1`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `pd_DataFrame` - 231 edges
2. `pd_Series` - 173 edges
3. `pd_CategoricalDtype` - 142 edges
4. `Booster` - 138 edges
5. `Dataset` - 120 edges
6. `LightGBMError` - 118 edges
7. `LGBMModel` - 72 edges
8. `_safe_call()` - 70 edges
9. `LGBMDeprecationWarning` - 57 edges
10. `LGBMClassifier` - 49 edges

## Surprising Connections (you probably didn't know these)
- `Booster` --uses--> `pd_CategoricalDtype`  [INFERRED]
  basic.py → compat.py
- `Booster` --uses--> `pd_DataFrame`  [INFERRED]
  basic.py → compat.py
- `Booster` --uses--> `pd_Series`  [INFERRED]
  basic.py → compat.py
- `_ConfigAliases` --uses--> `pd_CategoricalDtype`  [INFERRED]
  basic.py → compat.py
- `_ConfigAliases` --uses--> `pd_DataFrame`  [INFERRED]
  basic.py → compat.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (44): _c_array(), _c_float_array(), _c_int_array(), _c_str(), _cast_numpy_array_to_dtype(), _cfloat32_array_to_numpy(), _cfloat64_array_to_numpy(), _check_for_bad_pandas_dtypes() (+36 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (54): _acquire_port(), _assign_open_ports_to_workers(), _concat(), DaskLGBMClassifier, _DaskLGBMModel, DaskLGBMRanker, DaskLGBMRegressor, _DatasetNames (+46 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (48): EvalResult, CallbackEnv, early_stopping(), EarlyStopException, _EarlyStoppingCallback, _format_eval_result(), _is_using_cv(), log_evaluation() (+40 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (43): _MissingType, # TODO: remove 'type: ignore[assignment]' when https://github.com/lightgbm-org/L, Predict for a 2-D numpy matrix., Predict for a CSC data., Dataset in LightGBM.      LightGBM does not train on raw data.     It discretize, Create dataset from a reference dataset.          Parameters         ----------, Get the used parameters in the Dataset.          Returns         -------, Initialize data from list of Sequence objects.          Sequence: Generic Data A (+35 more)

### Community 4 - "Community 4"
Cohesion: 0.05
Nodes (43): Predict logic.          Parameters         ----------         data : str, pathli, # TODO: remove 'type: ignore[assignment]' when https://github.com/lightgbm-org/L, Predict for a CSR data., Predict for a narwhals DataFrame., Initialize Dataset.          Parameters         ----------         data : str, p, Create Dataset from sampled data structures.          Parameters         -------, Register custom logger.      Parameters     ----------     logger : Any, Initialize data from a 2-D numpy matrix. (+35 more)

### Community 5 - "Community 5"
Cohesion: 0.05
Nodes (43): # TODO: remove 'type: ignore[assignment]' when https://github.com/lightgbm-org/L, Get size of prediction result., Error thrown by LightGBM., Get the index of the current iteration.          Returns         -------, Get an array of randomly chosen indices from this ``Dataset``.          Indices, Add rows to Dataset.          Parameters         ----------         data : numpy, Sample data from seqs.          Mimics behavior in c_api.cpp:LGBM_DatasetCreateF, Initialize data from a list of 2-D numpy matrices. (+35 more)

### Community 6 - "Community 6"
Cohesion: 0.09
Nodes (2): Booster, _dump_pandas_categorical()

### Community 7 - "Community 7"
Cohesion: 0.09
Nodes (22): _LGBMClassifierBase, _LGBMModelBase, _LGBMRegressorBase, Dummy class for sklearn.base.BaseEstimator., Dummy class for sklearn.base.ClassifierMixin., Dummy class for sklearn.base.RegressorMixin., # NOTE: check_X_y() calls check_array() internally, so only need to call one or, _check_not_tuple_of_2_elements() (+14 more)

### Community 8 - "Community 8"
Cohesion: 0.08
Nodes (12): Docstring is set after definition, using a template., :obj:`int`: The number of features of fitted model., :obj:`dict`: The best score of fitted model., :obj:`int`: The best iteration of fitted model if ``early_stopping()`` callback, :obj:`str` or :obj:`callable`: The concrete objective used while fitting this mo, :obj:`int`: True number of boosting iterations performed.          This might be, :obj:`int`: True number of boosting iterations performed.          This might be, Booster: The underlying Booster of this model. (+4 more)

### Community 9 - "Community 9"
Cohesion: 0.16
Nodes (20): LGBMDeprecationWarning, LightGBMError, FutureWarning, :obj:`int`: The number of features of fitted model., Set number of features found in passed-in dataset.          Starting with ``scik, :obj:`list` of shape = [n_features]: The names of features.          .. note::, :obj:`array` of shape = [n_features]: scikit-learn compatible version of ``.feat, Intercept calls to delete ``feature_names_in_``.          Some code paths in ``s (+12 more)

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (17): _EvalFunctionWrapper, _extract_evaluation_meta_data(), _get_group_from_constructed_dataset(), _get_label_from_constructed_dataset(), _get_weight_from_constructed_dataset(), Docstring is set after definition, using a template., # NOTE: _LGBMValidateData() is also responsible for setting n_features_in_, # NOTE: all args from LGBMModel.__init__() are intentionally repeated here for (+9 more)

### Community 11 - "Community 11"
Cohesion: 0.20
Nodes (6): _ObjectiveFunctionWrapper, Proxy class for objective function., Construct a proxy class.          This class transforms objective function to ma, Get parameters for this estimator.          Parameters         ----------, Process the parameters of this estimator based on its type, parameter aliases, e, Convert special values of n_jobs to their actual values according to the formula

### Community 12 - "Community 12"
Cohesion: 0.33
Nodes (4): Generic data access interface.      Object should support the following operatio, Return data for given row index.          A basic implementation should look lik, Return row count of this sequence., Sequence

### Community 13 - "Community 13"
Cohesion: 0.50
Nodes (2): Make a prediction.          Parameters         ----------         data : str, pa, Initialize an ``_InnerPredictor`` from a ``Booster``.          Parameters

### Community 14 - "Community 14"
Cohesion: 0.50
Nodes (2): Proxy class to workaround errors on Windows., _TempFile

### Community 15 - "Community 15"
Cohesion: 0.67
Nodes (1): _DummyLogger

### Community 16 - "Community 16"
Cohesion: 0.67
Nodes (2): _find_lib_path(), Find the path to LightGBM library files.      Returns     -------     lib_path:

## Knowledge Gaps
- **8 isolated node(s):** `Dummy class for sklearn.base.BaseEstimator.`, `Dummy class for sklearn.base.ClassifierMixin.`, `Dummy class for sklearn.base.RegressorMixin.`, `Dummy class for pandas.Series.`, `Dummy class for pandas.DataFrame.` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 6`** (2 nodes): `Booster`, `_dump_pandas_categorical()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (2 nodes): `Make a prediction.          Parameters         ----------         data : str, pa`, `Initialize an ``_InnerPredictor`` from a ``Booster``.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (2 nodes): `Proxy class to workaround errors on Windows.`, `_TempFile`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (1 nodes): `_DummyLogger`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (2 nodes): `_find_lib_path()`, `Find the path to LightGBM library files.      Returns     -------     lib_path:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `pd_DataFrame` connect `Community 4` to `Community 6`, `Community 0`, `Community 15`, `Community 2`, `Community 9`, `Community 3`, `Community 5`, `Community 13`, `Community 14`, `Community 12`, `Community 7`, `Community 1`, `Community 10`, `Community 11`, `Community 8`?**
  _High betweenness centrality (0.301) - this node is a cross-community bridge._
- **Why does `Booster` connect `Community 6` to `Community 0`, `Community 13`, `Community 5`, `Community 4`, `Community 3`, `Community 2`, `Community 7`, `Community 10`, `Community 1`, `Community 11`, `Community 8`, `Community 9`?**
  _High betweenness centrality (0.188) - this node is a cross-community bridge._
- **Why does `pd_Series` connect `Community 3` to `Community 6`, `Community 0`, `Community 15`, `Community 2`, `Community 9`, `Community 4`, `Community 5`, `Community 13`, `Community 14`, `Community 12`, `Community 7`, `Community 1`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Are the 228 inferred relationships involving `pd_DataFrame` (e.g. with `Booster` and `_ConfigAliases`) actually correct?**
  _`pd_DataFrame` has 228 INFERRED edges - model-reasoned connections that need verification._
- **Are the 170 inferred relationships involving `pd_Series` (e.g. with `Booster` and `_ConfigAliases`) actually correct?**
  _`pd_Series` has 170 INFERRED edges - model-reasoned connections that need verification._
- **Are the 139 inferred relationships involving `pd_CategoricalDtype` (e.g. with `Booster` and `_ConfigAliases`) actually correct?**
  _`pd_CategoricalDtype` has 139 INFERRED edges - model-reasoned connections that need verification._
- **Are the 95 inferred relationships involving `Booster` (e.g. with `pd_CategoricalDtype` and `pd_DataFrame`) actually correct?**
  _`Booster` has 95 INFERRED edges - model-reasoned connections that need verification._