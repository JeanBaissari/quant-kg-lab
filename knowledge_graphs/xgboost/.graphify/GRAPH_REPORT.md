# Graph Report - xgboost  (2026-08-06)

## Corpus Check
- 53 files · ~78,025 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1631 nodes · 4318 edges · 80 communities detected
- Non-singleton communities: 80
- Extraction: EXTRACTED: 55.5% · INFERRED: 44.5%
- Edge kinds: calls: 584 · contains: 560 · imports_from: 189 · inherits: 98 · method: 370 · rationale_for: 597 · uses: 1920

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 53 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `2a4786e`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `Categories` (179)
- `DMatrix` (161)
- `Objective` (146)
- `Booster` (144)
- `TransformedDf` (133)
- `ArrowTransformed` (105)
- `PandasTransformed` (105)
- `XGBoostError` (102)
- `TreeObjective` (100)
- `data.py` (94)

## Surprising Connections (you probably didn't know these)
- `XGBoost Experimental Federated Learning related API.` --uses--> `RabitTracker`  [INFERRED]
  federated.py → tracker.py
- `Experimental support for a new objective interface with target dimension reducti` --uses--> `DMatrix`  [INFERRED]
  objective.py → core.py
- `Base class for custom objective functions.      .. warning::          Do not use` --uses--> `DMatrix`  [INFERRED]
  objective.py → core.py
- `Base class for tree-specific custom objective functions.      .. warning::` --uses--> `DMatrix`  [INFERRED]
  objective.py → core.py
- `Provide a different gradient type for finding tree structures.` --uses--> `DMatrix`  [INFERRED]
  objective.py → core.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (95): CCtx, HasArbitraryParamsDict, HasBaseMarginCol, HasContribPredictionCol, HasEnableSparseDataOptim, HasFeaturesCol, HasFeaturesCols, HasLabelCol (+87 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (84): _arrow_feature_info(), _check_data_shape(), _check_pyarrow_for_polars(), _convert_unknown_data(), dispatch_data_backend(), dispatch_meta_backend(), dispatch_proxy_set_data(), _from_arrow_table() (+76 more)

### Community 2 - "Community 2"
Cohesion: 0.06
Nodes (37): CallbackContainer, EarlyStopping, EvaluationMonitor, A special internal callback for invoking a list of other callbacks.      .. vers, Function called before training., Function called after training., Function called before training iteration., Callback function for early stopping      .. versionadded:: 1.3.0      Parameter (+29 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (42): Dummy class for sklearn.base.BaseEstimator., Dummy class for sklearn.base.ClassifierMixin., Dummy class for sklearn.base.RegressorMixin., XGBClassifierBase, XGBModelBase, XGBRegressorBase, QuantileDMatrix, get_model_categories() (+34 more)

### Community 4 - "Community 4"
Cohesion: 0.14
Nodes (56): Error thrown by xgboost trainer., XGBoostError, ExtMemQuantileDMatrix, Parse an eval result string from the booster., Save DMatrix to an XGBoost buffer.  Saved binary can be later loaded         by, Get the label of the DMatrix., Get the weight of the DMatrix., Get the base margin of the DMatrix. (+48 more)

### Community 5 - "Community 5"
Cohesion: 0.07
Nodes (43): Load the model from a file or a bytearray.          The model is saved in an XGB, Get unsigned integer property from the DMatrix.          Parameters         ----, Set float type property into the DMatrix            for numpy 2d array input, CudfTransformed, A storage class for transformed cuDF dataframe., Return shape of the transformed DataFrame., Predicate for scipy CSR input., Initialize DMatrix from cupy ndarray. (+35 more)

### Community 6 - "Community 6"
Cohesion: 0.07
Nodes (49): IteratorForTest, Iterator for testing streaming DMatrix. (external memory, quantile), Return concatenated arrays., Different strategies produce similar feature importance ratios., run_feature_importance_strategy_compare(), asarray(), _basic_example(), comp_booster() (+41 more)

### Community 7 - "Community 7"
Cohesion: 0.04
Nodes (52): check_categorical_mixed(), Use vector leaf for multi-label classification models., Check quantile regression for vector leaf., Check that reparameterized expectile regression produces non-crossing curves., Test mean absolute error with vector leaf., Test mixed numerical, one-hot, and partition-based splits., Check the vector leaf implementation is deterministic., Test column sampling with feature importance for multi-target trees. (+44 more)

### Community 8 - "Community 8"
Cohesion: 0.06
Nodes (42): array_hasobject(), array_interface(), array_interface_dict(), _ArrayLikeArg, _arrow_array_inf(), _arrow_buf_inf(), arrow_cat_inf(), _arrow_cat_names_inf() (+34 more)

### Community 9 - "Community 9"
Cohesion: 0.07
Nodes (20): plot_tree(), Convert specified tree to graphviz instance. IPython can automatically plot, Plot specified tree.      Parameters     ----------     booster :         Booste, to_graphviz(), _can_use_qdm(), Get the underlying xgboost Booster of this model.          This will raise an ex, Set the parameters of this estimator.  Modification of the sklearn method to, Get xgboost specific parameters. (+12 more)

### Community 10 - "Community 10"
Cohesion: 0.10
Nodes (38): _as_numpy(), check_external_memory(), check_init_estimation(), check_init_estimation_clf(), check_init_estimation_reg(), check_multi_output_tree_classifier(), check_multi_output_tree_regressor(), check_multi_output_tree_shap() (+30 more)

### Community 11 - "Community 11"
Cohesion: 0.08
Nodes (36): concat(), import_cupy(), import_pandas(), import_polars(), import_pyarrow(), _is_arrow(), is_cudf_available(), _is_cudf_df() (+28 more)

### Community 12 - "Community 12"
Cohesion: 0.06
Nodes (36): check_inf(), get_ames_housing(), get_california_housing(), get_cancer(), get_digits(), get_mq2008(), get_sparse(), make_batches() (+28 more)

### Community 13 - "Community 13"
Cohesion: 0.06
Nodes (32): CatIter, An iterator for testing categorical features., Return the concatenated data., check_categorical_bitfield_boundaries(), check_categorical_missing(), check_categorical_ohe(), check_cut(), check_extmem_qdm() (+24 more)

### Community 14 - "Community 14"
Cohesion: 0.06
Nodes (19): _ClassificationModel, Estimator, HasProbabilityCol, HasRawPredictionCol, The model returned by :func:`xgboost.spark.SparkXGBRegressor.fit`      .. Note::, SparkXGBClassifier is a PySpark ML estimator. It implements the XGBoost     clas, The model returned by :func:`xgboost.spark.SparkXGBClassifier.fit`      .. Note:, SparkXGBRanker is a PySpark ML estimator. It implements the XGBoost     ranking (+11 more)

### Community 15 - "Community 15"
Cohesion: 0.07
Nodes (27): allreduce(), broadcast(), communicator_print(), CommunicatorContext, finalize(), _find_nccl(), get_processor_name(), get_rank() (+19 more)

### Community 16 - "Community 16"
Cohesion: 0.07
Nodes (30): deserialize_booster(), deserialize_xgb_model(), get_class_name(), _get_default_params_from_func(), _get_gpu_id(), _get_host_ip(), get_logger(), get_logger_level() (+22 more)

### Community 17 - "Community 17"
Cohesion: 0.09
Nodes (13): _aggcv(), _allreduce_metric(), LearningRateScheduler, Callback library containing training routines.  See :doc:`Callback Functions </p, Aggregate cross-validation results., Helper function for computing customized metric in distributed     environment., Function called after training iteration., Callback function for scheduling learning rate.      .. versionadded:: 1.3.0 (+5 more)

### Community 18 - "Community 18"
Cohesion: 0.11
Nodes (18): no_arrow(), no_cudf(), no_cupy(), no_dask(), no_dask_cuda(), no_dask_cudf(), no_dask_ml(), no_graphviz() (+10 more)

### Community 19 - "Community 19"
Cohesion: 0.10
Nodes (25): c_str(), _check_call(), from_cstr_to_pystr(), from_pystr_to_cstr(), _get_log_callback_func(), _lib_version(), _load_lib(), _log_callback() (+17 more)

### Community 20 - "Community 20"
Cohesion: 0.12
Nodes (3): Booster, plot_importance(), Plot importance based on fitted trees.      Parameters     ----------     booste

### Community 21 - "Community 21"
Cohesion: 0.13
Nodes (21): _can_output_df(), _check_workers_are_alive(), CommunicatorContext, _direct_predict_impl(), _get_model_future(), _get_rabit_args(), _get_workers_from_data(), _infer_predict_output() (+13 more)

### Community 22 - "Community 22"
Cohesion: 0.13
Nodes (5): c_array(), _check_distributed_params(), _configure_metrics(), ctypes2buffer(), _expect()

### Community 23 - "Community 23"
Cohesion: 0.10
Nodes (13): DaskPartitionIter, A data iterator for the `DaskQuantileDMatrix`., Utility function for obtaining current batch of data., Yield next batch of data, DataIter, cache_partitions(), create_dmatrix_from_partitions(), make_qdm() (+5 more)

### Community 24 - "Community 24"
Cohesion: 0.14
Nodes (11): Xgboost training summary integration submodule., Test parameters for the leaf output test., check decay has effect on leaf output., Test learning rate scheduler, used by both CPU and GPU tests., run_eta_decay(), run_eta_decay_leaf_output(), tree_methods_objs(), Helpers for testing monotone constraints. (+3 more)

### Community 25 - "Community 25"
Cohesion: 0.12
Nodes (13): FederatedTracker, Tracker for federated training.      Parameters     ----------     n_workers :, See :py:class:`~xgboost.federated.FederatedTracker` for more info.      Paramete, run_federated_server(), RabitTracker, get_family(), RabitTracker, Internal function for testing. (+5 more)

### Community 26 - "Community 26"
Cohesion: 0.11
Nodes (19): check_expectile_error(), check_precision_score(), check_quantile_error(), _expectile_loss(), _expectile_loss_multi(), Tests for evaluation metrics., Test for the `expectile` loss., Test for precision with ranking and classification. (+11 more)

### Community 27 - "Community 27"
Cohesion: 0.13
Nodes (9): _is_iter(), Internal method for retrieving a reference to the training DMatrix., Parameters         ----------         data :             A user-defined :py:clas, Get callback functions for iterating in C. This is an internal function., Reraise the exception thrown during iteration., An iterator for single batch data to help creating device DMatrix.     Transform, Parameters         ----------         data :             Data source of DMatrix., SingleBatchInternalIter (+1 more)

### Community 28 - "Community 28"
Cohesion: 0.22
Nodes (16): _add_column(), _create_dmatrix(), _create_quantile_dmatrix(), _dmatrix_from_list_of_parts(), _extract_data(), _get_dmatrices(), _get_is_cuda(), _get_worker_parts() (+8 more)

### Community 29 - "Community 29"
Cohesion: 0.14
Nodes (9): DataIter, The interface for user defined data iterator. The iterator facilitates     distr, Handle of DMatrix proxy., A wrapper for user defined `reset` function., A wrapper for user defined `next` function.          `this` is not used in Pytho, Reset the data iterator.  Prototype for user defined function., Set the next batch of data.          Parameters         ----------          inpu, Decorator for methods that issues warnings for positional arguments      Using t (+1 more)

### Community 30 - "Community 30"
Cohesion: 0.17
Nodes (7): XGBoost: eXtreme Gradient Boosting library.  Contributors: https://github.com/dm, _check_rf_callback(), Emit the deprecation warning for the random forest estimators., _warn_rf_deprecated(), XGBRegressor, XGBRFClassifier, XGBRFRegressor

### Community 31 - "Community 31"
Cohesion: 0.13
Nodes (8): _get_categories(), Get the categories in the dataset.          .. versionadded:: 3.1.0          .., Same method as :py:meth:`DMatrix.get_categories`., Run prediction in-place when possible, Unlike :py:meth:`predict` method,, Number of features in booster., Dump model into a text or JSON file.  Unlike :py:meth:`save_model`, the, Returns the model dump as a list of strings.  Unlike :py:meth:`save_model`,, Get split value histogram of a feature          Parameters         ----------

### Community 32 - "Community 32"
Cohesion: 0.14
Nodes (7): _ProxyDMatrix, A placeholder class when DMatrix cannot be constructed (QuantileDMatrix,     inp, Reference data from CUDA array interface., Reference data from CUDA columnar format., Reference data from numpy array., Reference data from a CPU DataFrame., Reference data from scipy csr.

### Community 33 - "Community 33"
Cohesion: 0.14
Nodes (7): Set label of dmatrix          Parameters         ----------         label: array, Set weight of each instance.          Parameters         ----------         weig, Set base margin of booster to start from.          This can be used to specify a, Set group size of DMatrix (used for ranking).          Parameters         ------, Set meta info for DMatrix.  See doc string for :py:obj:`xgboost.DMatrix`., Set float type property into the DMatrix.          Parameters         ----------, Set uint type property into the DMatrix.          Parameters         ----------

### Community 34 - "Community 34"
Cohesion: 0.14
Nodes (7): DaskDMatrix, DaskQuantileDMatrix, DMatrix holding on references to Dask DataFrame or Dask Array.  Constructing a, Obtain references to local data., Create a dictionary of objects that can be pickled for function         argument, Get the number of columns (features) in the DMatrix.          Returns         --, A dask version of :py:class:`QuantileDMatrix`. See :py:class:`DaskDMatrix` for

### Community 35 - "Community 35"
Cohesion: 0.21
Nodes (9): ABC, build_info(), ctypes2numpy(), _numpy2ctypes_type(), _parse_eval_str(), _prediction_output(), Objective, Experimental support for a new objective interface with target dimension reducti (+1 more)

### Community 36 - "Community 36"
Cohesion: 0.17
Nodes (7): Get the predictors from DMatrix as a CSR matrix. This getter is mostly for, Get quantile cuts for quantization.          .. versionadded:: 2.0.0, Get the number of columns (features) in the DMatrix., Get the number of non-missing values in the DMatrix.          .. versionadded::, Labels for features (column labels).          Setting it to ``None`` resets exis, Type of features (column types).          This is for displaying the results and, _validate_feature_info()

### Community 37 - "Community 37"
Cohesion: 0.18
Nodes (11): ClickFold, init_rank_score(), PBM, A structure containing information about generated user-click data., Simulate click data with position bias model. There are other models available i, Sample clicks for one query based on input relevance degree and position., We use XGBoost to generate the initial score instead of SVMRank for     simplici, Simulate clicks for one fold. (+3 more)

### Community 38 - "Community 38"
Cohesion: 0.18
Nodes (8): _array_impl(), LsObj0, Split grad is the same as value grad., Test vector leaf with external memory., Test for learning rate., run_eta(), run_with_iter(), TreeObjective

### Community 39 - "Community 39"
Cohesion: 0.20
Nodes (7): _cls_predict_proba(), _metric_decorator(), xgboost_model_doc(), Tests for parsing trees., Test plotting functions for XGBoost., Tests plotting functions for categorical features., run_categorical()

### Community 40 - "Community 40"
Cohesion: 0.18
Nodes (12): _assert_monotone(), is_correctly_constrained(), is_decreasing(), is_increasing(), Check for a positive (``f0``) and negative (``f1``) constraint., Grid-check monotonicity per output column for every constrained feature.      Fo, Whether ``v`` is nondecreasing along the sweep axis., Monotonicity check for deep trees with mixed feature constraints.      Uses more (+4 more)

### Community 41 - "Community 41"
Cohesion: 0.20
Nodes (5): DaskXGBClassifier, Temporarily set the client for sklearn model., Get the correct client, when method is invoked inside a worker we         should, _set_worker_client(), XGBClassifierMixIn

### Community 42 - "Community 42"
Cohesion: 0.20
Nodes (8): data_dir(), demo_dir(), DirectoryExcursion, load_agaricus(), normpath(), project_root(), Change directory.  Change back and optionally cleaning up the directory when, Look for the demo directory based on the test file name.

### Community 43 - "Community 43"
Cohesion: 0.18
Nodes (5): make_dataset_strategy(), make_datasets_with_margin(), Contains a dataset in numpy format as well as the relevant objective and metric., Factory function for creating strategies that generates datasets with weight and, TestDataset

### Community 44 - "Community 44"
Cohesion: 0.18
Nodes (10): Testwith the cali housing dataset., Test re-coding for training continuation., Tests for the intercept., Parameters     ----------      as_frame: A callable function to convert margin i, Boosting from prediction with multi-class clf., run_boost_from_prediction_binary(), run_boost_from_prediction_multi_clasas(), run_housing_rf_regression() (+2 more)

### Community 45 - "Community 45"
Cohesion: 0.20
Nodes (7): _get_client(), inplace_predict(), predict(), Run prediction with a trained booster.      .. note::          Using ``inplace_p, Inplace prediction. See doc in :py:meth:`xgboost.Booster.inplace_predict` for, The dask client used in this model.  The `Client` object can not be         seri, Simple wrapper around testing None.

### Community 46 - "Community 46"
Cohesion: 0.20
Nodes (9): Tests for estimating the intercept., Test for adaptive trees., Exp family has a closed solution., Test for init estimation., Test https://github.com/dmlc/xgboost/issues/11499 ., run_adaptive(), run_exp_family(), run_init_estimation() (+1 more)

### Community 47 - "Community 47"
Cohesion: 0.20
Nodes (9): assert_allclose(), non_decreasing(), non_increasing(), predictor_equal(), Helpers for test code., Dispatch the assert_allclose for devices., Assert whether two DMatrices contain the same predictors., Values in the sequence are not increasing. (+1 more)

### Community 48 - "Community 48"
Cohesion: 0.22
Nodes (4): DaskXGBRegressor, DaskXGBRFRegressor, dummy doc string to workaround pylint, replaced by the decorator., XGBRegressorMixIn

### Community 49 - "Community 49"
Cohesion: 0.28
Nodes (8): _DASK_2024_12_1(), _DASK_2025_3_0(), _DASK_VERSION(), get_address_from_user(), get_n_threads(), Utilities for the XGBoost Dask interface., Get the number of threads from a worker and the user-supplied parameters., Get the tracker address from the optional user configuration.      Parameters

### Community 50 - "Community 50"
Cohesion: 0.25
Nodes (8): Launcher for clients and the server., Run federated learning tests., Run federated server for test., Run federated client worker for test., run_federated(), run_federated_learning(), run_server(), run_worker()

### Community 51 - "Community 51"
Cohesion: 0.32
Nodes (5): _async_wrap_evaluation_matrices(), _get_dask_config(), A switch function for async environment., Train XGBoost model.      .. versionadded:: 1.0.0      .. note::          Other, train()

### Community 52 - "Community 52"
Cohesion: 0.32
Nodes (7): Exception, find_lib_path(), is_sphinx_build(), Error thrown by when xgboost is not found, `XGBOOST_BUILD_DOC` is used by the sphinx conf.py to skip building the C++ code., Find the path to xgboost dynamic library files.      Returns     -------     lib, XGBoostLibraryNotFound

### Community 53 - "Community 53"
Cohesion: 0.25
Nodes (6): concat_or_none(), pred_contribs(), Stack a series of arrays., Concatenate the data if it's not None., Predict contributions with data with the full model., stack_series()

### Community 54 - "Community 54"
Cohesion: 0.25
Nodes (7): check_invalid_cat_batches(), check_uneven_sizes(), Tests related to the `DataIter` interface., Check QDM with mixed batches., Check error message for inconsistent feature types., Tests for having irregular data shapes., run_mixed_sparsity()

### Community 55 - "Community 55"
Cohesion: 0.25
Nodes (8): _make_leaf_dmatrix(), _predict_leaf(), Make a prediction matrix and an in-memory reference for external memory., Predict leaves and compare external memory against in-memory data., Validate that each predicted node is a leaf in the corresponding tree., Run tests for leaf index prediction., run_predict_leaf(), _validate_leaf_indices()

### Community 56 - "Community 56"
Cohesion: 0.25
Nodes (7): get_feature_weights(), Testing code shared by other tests., Validate output for predict leaf tests., Assert that we don't create duplicated DMatrix., Get feature weights using the demo parser., validate_data_initialization(), validate_leaf_output()

### Community 57 - "Community 57"
Cohesion: 0.29
Nodes (3): DaskScikitLearnBase, Base class for implementing scikit-learn interface with Dask, XGBModel

### Community 58 - "Community 58"
Cohesion: 0.33
Nodes (4): Config, User configuration for the communicator context. This is used for easier     int, Worker side arguments resolution., Update the arguments for the communicator.

### Community 59 - "Community 59"
Cohesion: 0.47
Nodes (5): config_context(), config_doc(), get_config(), Decorator to format docstring for config functions.      Parameters     --------, set_config()

### Community 60 - "Community 60"
Cohesion: 0.33
Nodes (5): Tests for interaction constraints., Tests interaction constraints on a synthetic dataset. Only x1 and x2 are allowed, Test accuracy, reused by GPU tests., run_interaction_constraints(), training_accuracy()

### Community 61 - "Community 61"
Cohesion: 0.40
Nodes (2): DaskXGBRanker, XGBRankerMixIn

### Community 62 - "Community 62"
Cohesion: 0.40
Nodes (1): DaskXGBRFClassifier

### Community 63 - "Community 63"
Cohesion: 0.70
Nodes (4): _as_booster(), _as_prediction_dmatrix(), _get_iteration_range(), shap_values()

### Community 64 - "Community 64"
Cohesion: 0.40
Nodes (4): NamedTuple, Simple data struct for holding a train-test split of a learning to rank dataset., Whether the label consists of binary relevance degree., RelDataCV

### Community 65 - "Community 65"
Cohesion: 0.40
Nodes (5): _make_subsample_params(), Test row subsampling., Test that gradient-based sampling provides better accuracy., run_gradient_based_sampling_accuracy(), run_subsample()

### Community 66 - "Community 66"
Cohesion: 0.50
Nodes (2): XGBoost Experimental Federated Learning related API., Tracker for XGBoost collective.

### Community 67 - "Community 67"
Cohesion: 0.50
Nodes (3): Xgboost pyspark integration submodule for estimator API., This function automatically infer to xgboost parameters and set them     into co, _set_pyspark_xgb_cls_param_attrs()

### Community 68 - "Community 68"
Cohesion: 0.50
Nodes (3): Tests for basic features of the Booster., Tests custom objective and metric functions., run_custom_objective()

### Community 69 - "Community 69"
Cohesion: 0.50
Nodes (3): get_avail_port(), Collective module related utilities., Returns a port that's available during the function call. It doesn't prevent the

### Community 70 - "Community 70"
Cohesion: 0.50
Nodes (4): has_ipv6(), no_ipv6(), PyTest skip mark for IPv6., Check whether IPv6 is enabled on this host.

### Community 71 - "Community 71"
Cohesion: 0.67
Nodes (3): is_windows(), Check if the current platform is Windows., skip_win()

### Community 72 - "Community 72"
Cohesion: 1.00
Nodes (1): Provide a different gradient type for finding tree structures.

### Community 73 - "Community 73"
Cohesion: 1.00
Nodes (2): captured_output(), Reassign stdout temporarily in order to test printed statements     Taken from:

### Community 74 - "Community 74"
Cohesion: 1.00
Nodes (2): eval_error_metric_skl(), Evaluation metric that looks like metrics provided by sklearn.

### Community 75 - "Community 75"
Cohesion: 1.00
Nodes (2): eval_error_metric(), Evaluation metric for xgb.train.      Parameters     ----------     rev_link : W

### Community 76 - "Community 76"
Cohesion: 1.00
Nodes (2): logregobj(), Binary regression custom objective.

### Community 77 - "Community 77"
Cohesion: 1.00
Nodes (2): make_regression(), Make a simple regression dataset.

### Community 78 - "Community 78"
Cohesion: 1.00
Nodes (2): Custom softprob objective for testing.      Parameters     ----------     use_cu, softprob_obj()

### Community 79 - "Community 79"
Cohesion: 1.00
Nodes (2): Make a pytest mark for the `pytest-timeout` package.      Parameters     -------, timeout()

## Knowledge Gaps
- **248 isolated node(s):** `Low-level ctypes bridge for the XGBoost C API.`, `Error thrown by xgboost trainer.`, `Convert a Python str or list of Python str to C pointer.`, `Revert C pointer to Python str.`, `Make JSON-based arguments for C functions.` (+243 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 61`** (2 nodes): `DaskXGBRanker`, `XGBRankerMixIn`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 62`** (1 nodes): `DaskXGBRFClassifier`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 66`** (2 nodes): `XGBoost Experimental Federated Learning related API.`, `Tracker for XGBoost collective.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 72`** (1 nodes): `Provide a different gradient type for finding tree structures.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 73`** (2 nodes): `captured_output()`, `Reassign stdout temporarily in order to test printed statements     Taken from:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 74`** (2 nodes): `eval_error_metric_skl()`, `Evaluation metric that looks like metrics provided by sklearn.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 75`** (2 nodes): `eval_error_metric()`, `Evaluation metric for xgb.train.      Parameters     ----------     rev_link : W`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 76`** (2 nodes): `logregobj()`, `Binary regression custom objective.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 77`** (2 nodes): `make_regression()`, `Make a simple regression dataset.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 78`** (2 nodes): `Custom softprob objective for testing.      Parameters     ----------     use_cu`, `softprob_obj()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 79`** (2 nodes): `Make a pytest mark for the `pytest-timeout` package.      Parameters     -------`, `timeout()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DMatrix` connect `Community 17` to `Community 2`, `Community 35`, `Community 4`, `Community 36`, `Community 31`, `Community 27`, `Community 22`, `Community 33`, `Community 5`, `Community 32`, `Community 3`, `Community 30`, `Community 72`, `Community 9`?**
  _High betweenness centrality (0.102) - this node is a cross-community bridge._
- **Why does `IteratorForTest` connect `Community 6` to `Community 12`, `Community 23`, `Community 42`, `Community 18`, `Community 70`, `Community 77`, `Community 43`, `Community 76`, `Community 75`, `Community 74`, `Community 78`, `Community 73`, `Community 79`, `Community 71`, `Community 38`, `Community 10`, `Community 35`, `Community 7`, `Community 65`, `Community 55`, `Community 13`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Why does `Booster` connect `Community 20` to `Community 2`, `Community 17`, `Community 35`, `Community 4`, `Community 22`, `Community 31`, `Community 5`, `Community 30`, `Community 9`, `Community 3`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 172 inferred relationships involving `Categories` (e.g. with `Booster` and `DataIter`) actually correct?**
  _`Categories` has 172 INFERRED edges - model-reasoned connections that need verification._
- **Are the 128 inferred relationships involving `DMatrix` (e.g. with `CallbackContainer` and `EarlyStopping`) actually correct?**
  _`DMatrix` has 128 INFERRED edges - model-reasoned connections that need verification._
- **Are the 141 inferred relationships involving `Objective` (e.g. with `Booster` and `DataIter`) actually correct?**
  _`Objective` has 141 INFERRED edges - model-reasoned connections that need verification._
- **Are the 98 inferred relationships involving `Booster` (e.g. with `CallbackContainer` and `EarlyStopping`) actually correct?**
  _`Booster` has 98 INFERRED edges - model-reasoned connections that need verification._