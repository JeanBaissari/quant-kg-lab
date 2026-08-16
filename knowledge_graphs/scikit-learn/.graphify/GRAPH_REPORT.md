# Graph Report - sklearn  (2026-08-06)

## Corpus Check
- Large corpus: 397 files · ~826,838 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 8450 nodes · 28094 edges · 367 communities detected
- Non-singleton communities: 346
- Extraction: EXTRACTED: 39.8% · INFERRED: 60.2%
- Edge kinds: calls: 2321 · contains: 2160 · imports: 5 · imports_from: 64 · inherits: 744 · method: 2598 · rationale_for: 3284 · uses: 16918

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 397 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `6f8b95a`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `Interval` (2234)
- `StrOptions` (2007)
- `BaseEstimator` (1531)
- `TransformerMixin` (883)
- `RegressorMixin` (740)
- `Parallel` (732)
- `ClassifierMixin` (664)
- `HasMethods` (608)
- `ConvergenceWarning` (509)
- `ClassNamePrefixFeaturesOutMixin` (501)

## Surprising Connections (you probably didn't know these)
- `Time column with millisecond precision and color styling.` --uses--> `Interval`  [INFERRED]
  callback/_progressbar.py → utils/_param_validation.py
- `Percentage column with color styling.` --uses--> `Interval`  [INFERRED]
  callback/_progressbar.py → utils/_param_validation.py
- `Thread monitoring the progress of an estimator with rich based display.      The` --uses--> `Interval`  [INFERRED]
  callback/_progressbar.py → utils/_param_validation.py
- `Create a progress bar for the task and update the list of ordered tasks.` --uses--> `Interval`  [INFERRED]
  callback/_progressbar.py → utils/_param_validation.py
- `Update the progress of the task and its ancestors recursively.` --uses--> `Interval`  [INFERRED]
  callback/_progressbar.py → utils/_param_validation.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.02
Nodes (461): BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin, Affinity Propagation clustering algorithm., Perform Affinity Propagation Clustering of data.      Read more in the :ref:`Use, Perform Affinity Propagation Clustering of data.      Read more in the :ref:`Use, Main affinity propagation algorithm., Fit the clustering from features, or affinity matrix.          Parameters (+453 more)

### Community 1 - "Community 1"
Cohesion: 0.02
Nodes (202): AttributeError, _BaseHeterogeneousEnsemble, make_column_selector, The :mod:`sklearn.compose._column_transformer` module implements utilities to wo, Transform X separately by each transformer, concatenate results.          Parame, Stacks Xs horizontally.          This allows subclasses to control the stacking, Get metadata routing of this object.          Please check :ref:`User Guide <met, Use check_array only when necessary, e.g. on lists and other non-array-likes. (+194 more)

### Community 2 - "Community 2"
Cohesion: 0.02
Nodes (162): OneToOneFeatureMixin, Fit the model.          Parameters         ----------         X : array-like of, Fit the model and recover the sources from X.          Parameters         ------, Fit the model to X.          Parameters         ----------         X : array-lik, FeatureHasher, _iteritems(), Transform a sequence of instances to a scipy.sparse matrix.          Parameters, Utilities to build feature vectors from text documents. (+154 more)

### Community 3 - "Community 3"
Cohesion: 0.02
Nodes (136): Enables Successive Halving search-estimators  The API and results of these estim, _MetadataRequester, BaseThresholdClassifier, _check_is_fitted(), _fit_and_score_over_thresholds(), FixedThresholdClassifier, _mean_interpolated_score(), Fit the classifier.          Parameters         ----------         X : {array-li (+128 more)

### Community 4 - "Community 4"
Cohesion: 0.02
Nodes (128): MultiOutputMixin, fetch_california_housing(), California housing dataset.  The original database is available from StatLib, Load the California housing dataset (regression).      ==============   ========, fetch_covtype(), Forest covertype dataset.  A classic dataset for classification benchmarks, feat, Load the covertype dataset (classification).      Download it if necessary., fetch_olivetti_faces() (+120 more)

### Community 5 - "Community 5"
Cohesion: 0.03
Nodes (126): ClassifierMixin, MetaEstimatorMixin, RegressorMixin, _CalibratedClassifier, calibration_curve(), CalibrationDisplay, _convert_to_logits(), _fit_calibrator() (+118 more)

### Community 6 - "Community 6"
Cohesion: 0.08
Nodes (127): BiclusterMixin, clone(), _clone_parametrized(), ClusterMixin, DensityMixin, _fit_context(), is_classifier(), is_clusterer() (+119 more)

### Community 7 - "Community 7"
Cohesion: 0.04
Nodes (71): GammaRegressor, _GeneralizedLinearRegressor, PoissonRegressor, Fit a Generalized Linear Model.          Parameters         ----------         X, # TODO: if alpha=0 check that X is not rank deficient, # NOTE: Rescaling of sample_weight:, Compute the linear_predictor = `X @ coef_ + intercept_`.          Note that we o, Predict using GLM with feature matrix X.          Parameters         ---------- (+63 more)

### Community 8 - "Community 8"
Cohesion: 0.03
Nodes (61): BaseEstimator, ClassifierMixin, _BinaryGaussianProcessClassifierLaplace, GaussianProcessClassifier, Gaussian processes classification., Fit Gaussian process classification model.          Parameters         ---------, Perform classification on an array of test vectors X.          Parameters, Return probability estimates for the test vector X.          Parameters (+53 more)

### Community 9 - "Community 9"
Cohesion: 0.09
Nodes (61): CalibratedClassifierCV, LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis, DummyClassifier, Nystroem, PolynomialCountSketch, RBFSampler, SkewedChi2Sampler (+53 more)

### Community 10 - "Community 10"
Cohesion: 0.03
Nodes (77): cluster_optics_dbscan(), cluster_optics_xi(), _compute_core_distances_(), compute_optics_graph(), _correct_predecessor(), _extend_region(), _extract_xi_labels(), OPTICS (+69 more)

### Community 11 - "Community 11"
Cohesion: 0.06
Nodes (59): DummyRegressor, BaseGradientBoosting, GradientBoostingClassifier, GradientBoostingRegressor, _init_raw_predictions(), Gradient Boosted Regression Trees.  This module contains methods for fitting gra, The impurity-based feature importances.          The higher, the more important, Fast partial dependence computation.          Parameters         ---------- (+51 more)

### Community 12 - "Community 12"
Cohesion: 0.08
Nodes (53): BaseHistGradientBoosting, HistGradientBoostingClassifier, HistGradientBoostingRegressor, _patch_raw_predict(), Fast Gradient Boosting decision trees for classification and regression., Check if fitting should be early-stopped based on scorer.          Scores are co, Check if fitting should be early-stopped based on loss.          Scores are comp, Return True (do early stopping) if the last n scores aren't better         than (+45 more)

### Community 13 - "Community 13"
Cohesion: 0.06
Nodes (66): BaseLink, HalfLogitLink, IdentityLink, _inclusive_low_high(), Interval, LogitLink, LogLink, MultinomialLogit (+58 more)

### Community 14 - "Community 14"
Cohesion: 0.03
Nodes (39): _BaseDiscreteNB, _BaseNB, BernoulliNB, CategoricalNB, ComplementNB, MultinomialNB, Naive Bayes algorithms.  These are supervised learning methods based on applying, Count feature occurrences. (+31 more)

### Community 15 - "Community 15"
Cohesion: 0.03
Nodes (48): BaseBagging, BaggingClassifier, BaggingRegressor, BaseBagging, _consumes_sample_weight(), _generate_bagging_indices(), _generate_indices(), _parallel_build_estimators() (+40 more)

### Community 16 - "Community 16"
Cohesion: 0.05
Nodes (40): Models based on neural networks., BaseMultilayerPerceptron, MLPClassifier, MLPRegressor, _pack(), Multi-layer Perceptron, Predict using the multi-layer perceptron classifier.          Parameters, Private predict method with optional input validation (+32 more)

### Community 17 - "Community 17"
Cohesion: 0.05
Nodes (74): additive_chi2_kernel(), _check_chunk_size(), check_paired_arrays(), check_pairwise_arrays(), chi2_kernel(), cosine_distances(), cosine_similarity(), distance_metrics() (+66 more)

### Community 18 - "Community 18"
Cohesion: 0.03
Nodes (19): ClassNamePrefixFeaturesOutMixin, _PLS, PLSSVD, _BasePCA, fastica(), _BinMapper, Data embedding techniques., Isomap (+11 more)

### Community 19 - "Community 19"
Cohesion: 0.04
Nodes (39): ABC, _ArrayLikes, _Booleans, _Callables, _Constraint, _CVObjects, generate_invalid_param_val(), _InstancesOf (+31 more)

### Community 20 - "Community 20"
Cohesion: 0.06
Nodes (21): BaseSGDClassifier, BaseSGDRegressor, PassiveAggressiveClassifier, PassiveAggressiveRegressor, Passive Aggressive Classifier.      .. deprecated:: 1.8         The whole class, Fit linear model with Passive Aggressive algorithm.          Parameters, Fit linear model with Passive Aggressive algorithm.          Parameters, Passive Aggressive Regressor.      .. deprecated:: 1.8         The whole class ` (+13 more)

### Community 21 - "Community 21"
Cohesion: 0.05
Nodes (37): _BaseScorer, _cached_call(), _check_multimetric_scoring(), check_scoring(), _CurveScorer, _get_func_repr_or_name(), _get_response_method_name(), get_scorer() (+29 more)

### Community 22 - "Community 22"
Cohesion: 0.05
Nodes (16): _BaseSparseCoding, _check_positive_coding(), _dict_learning(), dict_learning_online(), DictionaryLearning, MiniBatchDictionaryLearning, # TODO: move this handling (which is currently too broad), sparse_encode() (+8 more)

### Community 23 - "Community 23"
Cohesion: 0.04
Nodes (26): DotProduct, ExpSineSquared, GenericKernelMixin, Hyperparameter, White kernel.      The main use-case of this kernel is as part of a sum-kernel w, Return the kernel k(X, Y) and optionally its gradient.          Parameters, Returns the diagonal of the kernel k(X, X).          The result of this method i, Rational Quadratic kernel.      The RationalQuadratic kernel can be seen as a sc (+18 more)

### Community 24 - "Community 24"
Cohesion: 0.07
Nodes (34): _check_copy_and_writeable(), Lars, lars_path(), lars_path_gram(), _lars_path_residues(), _lars_path_solver(), LarsCV, LassoLars (+26 more)

### Community 25 - "Community 25"
Cohesion: 0.05
Nodes (29): BaseDecisionTree, DecisionTreeClassifier, DecisionTreeRegressor, ExtraTreeClassifier, ExtraTreeRegressor, This module gathers tree-based methods, including decision, regression and rando, Build a decision tree classifier from the training set (X, y).          Paramete, Predict class probabilities of the input samples X.          The predicted class (+21 more)

### Community 26 - "Community 26"
Cohesion: 0.06
Nodes (29): _BaseTreeExporter, _color_brew(), _compute_depth(), _DOTTreeExporter, export_graphviz(), export_text(), _matplotlib_to_rgb(), _MPLTreeExporter (+21 more)

### Community 27 - "Community 27"
Cohesion: 0.06
Nodes (55): check_all_zero_sample_weights_error(), check_array_api_same_namespace(), check_classifier_multioutput(), check_classifiers_multilabel_output_format_decision_function(), check_classifiers_multilabel_output_format_predict(), check_classifiers_multilabel_output_format_predict_proba(), check_classifiers_multilabel_representation_invariance(), check_classifiers_one_label() (+47 more)

### Community 28 - "Community 28"
Cohesion: 0.07
Nodes (39): be_shrunk(), check_probability_model(), check_regression_model(), clone(), cross_validation(), free_and_destroy_model(), free_model_content(), fun() (+31 more)

### Community 29 - "Community 29"
Cohesion: 0.07
Nodes (24): Spectral biclustering algorithms., Validate parameters depending on the input data., Create a biclustering for X.          Parameters         ----------         X :, Returns first `n_components` left and right singular         vectors u and v, di, Spectral Co-Clustering algorithm (Dhillon, 2001) [1]_.      Clusters rows and co, Normalize ``X`` by scaling rows and columns independently.      Returns the norm, Spectral biclustering (Kluger, 2003) [1]_.      Partitions rows and columns unde, Normalize rows and columns of ``X`` simultaneously so that all     rows sum to o (+16 more)

### Community 30 - "Community 30"
Cohesion: 0.06
Nodes (26): _fill_predictor_arrays(), This module contains the TreeGrower class.  TreeGrower builds a regression tree, Set children values bounds to respect monotonic constraints., Comparison for priority queue.          Nodes with high gain are higher priority, Tree Node class used in TreeGrower.      This isn't used for prediction purposes, Validate parameters passed to __init__.          Also validate parameters passed, Grow the tree, from root to leaves., Multiply leaves values by shrinkage parameter.          This must be done at the (+18 more)

### Community 31 - "Community 31"
Cohesion: 0.06
Nodes (18): Descriptor for defining `set_{method}_request` methods in estimators.      .. ve, RequestMethod, ArraySlicingWrapper, CheckingClassifier, MockDataFrame, _MockEstimatorOnOffPrediction, NoSampleWeightWrapper, Validate X and y and make extra check.          Parameters         ---------- (+10 more)

### Community 32 - "Community 32"
Cohesion: 0.10
Nodes (44): FitFailedWarning, Custom warnings and errors used across scikit-learn., Warning class used if there is an error while fitting the estimator.      This W, Exception class to raise if a metadata is passed which is not explicitly \, UnsetMetadataPassedError, _aggregate_score_dicts(), _check_groups_routing_disabled(), _check_is_permutation() (+36 more)

### Community 33 - "Community 33"
Cohesion: 0.09
Nodes (37): be_shrunk(), Cache, calculate_rho(), clone(), do_shrinking(), dot(), get_data(), info() (+29 more)

### Community 34 - "Community 34"
Cohesion: 0.06
Nodes (17): BaseLibSVM, BaseSVC, Parameter learned in Platt scaling when `probability=True`.          Returns, Parameter learned in Platt scaling when `probability=True`.          Returns, Fit the SVM model according to the given training data.          Parameters, Validation of y and class_weight.          Default implementation for SVR and on, Perform regression on samples in X.          For a one-class model, +1 (inlier), Return the data transformed by a callable kernel (+9 more)

### Community 35 - "Community 35"
Cohesion: 0.08
Nodes (30): AutoPropagatedCallback, _BaseCallback, FitCallback, Method called at the beginning of the fit method of the estimator.          For, Protocol for the auto-propagated callbacks      An auto-propagated callback is a, The maximum number of nested estimators at which the callback should be, Method called after finishing the fit method of the estimator.          For auto, Protocol for the callbacks evaluated on tasks during the fit of an estimator. (+22 more)

### Community 36 - "Community 36"
Cohesion: 0.06
Nodes (23): clip(), cumulative_prod(), cumulative_sum(), empty(), iinfo(), isdtype(), ones(), These are functions that are just aliases of existing functions in NumPy. (+15 more)

### Community 37 - "Community 37"
Cohesion: 0.05
Nodes (44): _generate_hypercube(), make_biclusters(), make_blobs(), make_checkerboard(), make_circles(), make_classification(), make_friedman1(), make_friedman2() (+36 more)

### Community 38 - "Community 38"
Cohesion: 0.07
Nodes (18): Birch, _CFNode, _CFSubcluster, _iterate_sparse_X(), _split_node(), dbscan(), estimate_bandwidth(), get_bin_seeds() (+10 more)

### Community 39 - "Community 39"
Cohesion: 0.07
Nodes (18): BaseEnsemble, AdaBoostClassifier, AdaBoostRegressor, BaseWeightBoosting, Weight Boosting.  This module contains weight boosting estimators for both class, Predict regression value for X.          The predicted regression value of an in, Implement a single boost.          Warning: This method needs to be overridden b, Return staged scores for X, y.          This generator method yields the ensembl (+10 more)

### Community 40 - "Community 40"
Cohesion: 0.06
Nodes (23): _BaseImputer, Transformers for missing value imputation., _assign_where(), IterativeImputer, Impute a single feature from the others provided.          This function predict, Assign X2 to X1 where cond is True.      Parameters     ----------     X1 : ndar, Get a list of other features to predict `feat_idx`.          If `self.n_nearest_, Decide in what order we will update the features.          As a homage to the MI (+15 more)

### Community 41 - "Community 41"
Cohesion: 0.07
Nodes (41): clear_data_home(), _convert_data_dataframe(), _derive_folder_and_filename_from_url(), fetch_file(), _fetch_remote(), _filter_filename(), get_data_home(), load_breast_cancer() (+33 more)

### Community 42 - "Community 42"
Cohesion: 0.06
Nodes (20): Bunch, Set key in dictionary to be deprecated with its warning message., Container object exposing keys as attributes.      Bunch objects are sometimes u, _MetadataRequester, Return params consumed as metadata in a :term:`router` or its sub-estimators., Get names of all metadata that can be consumed or routed by specified \, Prepare the given metadata to be passed to the method.          This is used whe, Get the values of metadata requested by :term:`consumers <consumer>`.          R (+12 more)

### Community 43 - "Community 43"
Cohesion: 0.07
Nodes (19): _BaseRidge, _BaseRidgeCV, _find_smallest_angle(), _get_rescaled_operator(), _get_valid_accept_sparse(), resolve_solver(), resolve_solver_for_numpy(), Ridge (+11 more)

### Community 44 - "Community 44"
Cohesion: 0.06
Nodes (32): _ensure_sparse_index_int32(), _in_unstable_openblas_configuration(), _min_or_max_axis(), _minor_reduce(), _preserve_dia_indices_dtype(), Compatibility fixes for older version of the dependencies  If you add content to, # TODO: Adapt when Pandas > 2.2 is the minimum supported version, # TODO: remove when SciPy 1.12 is the minimum supported version (+24 more)

### Community 45 - "Community 45"
Cohesion: 0.06
Nodes (28): check_class_weight_balanced_linear_classifier(), check_classifier_not_supporting_multiclass(), check_classifiers_classes(), check_classifiers_one_label_sample_weights(), check_classifiers_predictions(), check_clusterer_compute_labels_predict(), check_do_not_raise_errors_in_init_or_set_params(), check_dont_overwrite_parameters() (+20 more)

### Community 46 - "Community 46"
Cohesion: 0.07
Nodes (38): auc(), average_precision_score(), _binary_roc_auc_score(), _check_dcg_target_type(), confusion_matrix_at_thresholds(), coverage_error(), _dcg_sample_scores(), dcg_score() (+30 more)

### Community 47 - "Community 47"
Cohesion: 0.08
Nodes (38): count_nonzero(), csc_median_axis_0(), _get_elem_at_rank(), _get_median(), _implicit_column_offset(), incr_mean_variance_axis(), inplace_column_scale(), inplace_csr_column_scale() (+30 more)

### Community 48 - "Community 48"
Cohesion: 0.06
Nodes (23): BaseLibSVM, BaseSVC, OutlierMixin, SparseCoefMixin, LinearSVC, LinearSVR, OneClassSVM, Epsilon-Support Vector Regression.      The free parameters in the model are C a (+15 more)

### Community 49 - "Community 49"
Cohesion: 0.07
Nodes (20): _Progress, ProgressBar, Time column with millisecond precision and color styling., Percentage column with color styling., Thread monitoring the progress of an estimator with rich based display.      The, Create a progress bar for the task and update the list of ordered tasks., Update the progress of the task and its ancestors recursively., Callback that displays progress bars for each iterative step of an estimator. (+12 more)

### Community 50 - "Community 50"
Cohesion: 0.10
Nodes (35): _ClsToXPInfo, _dask_device, Various helper functions which are not part of the spec.  Functions which start, Return True if x is potentially a future or it may be otherwise impossible or, # TODO: Should we reject ndarray subclasses?, Return True if `x` is a CuPy array.      This function does not import CuPy if i, Return True if `x` is a PyTorch tensor.      This function does not import PyTor, Return True if `x` is a ndonnx Array.      This function does not import ndonnx (+27 more)

### Community 51 - "Community 51"
Cohesion: 0.08
Nodes (37): _assemble_fraction_of_explained_deviance(), _check_reg_targets(), _check_reg_targets_with_floating_dtype(), d2_absolute_error_score(), d2_pinball_score(), explained_variance_score(), max_error(), mean_absolute_error() (+29 more)

### Community 52 - "Community 52"
Cohesion: 0.12
Nodes (35): array_namespace(), _check_api_version(), _check_device(), _cls_to_namespace(), _compat_module_name(), _cupy_to_device(), device(), _is_array_api_cls() (+27 more)

### Community 53 - "Community 53"
Cohesion: 0.11
Nodes (16): _BaseNMF, _beta_divergence(), _beta_loss_to_float(), _check_init(), _fit_coordinate_descent(), _fit_multiplicative_update(), _initialize_nmf(), MiniBatchNMF (+8 more)

### Community 54 - "Community 54"
Cohesion: 0.06
Nodes (35): argpartition(), atleast_nd(), broadcast_shapes(), cov(), create_diagonal(), expand_dims(), isclose(), isin() (+27 more)

### Community 55 - "Community 55"
Cohesion: 0.10
Nodes (6): _check_X(), ColumnTransformer, _get_transformer_list(), _is_empty_column_selection(), make_column_transformer(), Meta-estimators for building composite models with transformers.  In addition to

### Community 56 - "Community 56"
Cohesion: 0.07
Nodes (21): get_routing_for_object(), _manual_routing(), process_routing(), _raise_for_params(), _raise_for_unsupported_routing(), Metadata Routing Utility  In order to better understand the components implement, Validate given metadata for a method.          This raises a ``TypeError`` if so, Get a ``Metadata{Router, Request}`` instance from the given object.      This fu (+13 more)

### Community 57 - "Community 57"
Cohesion: 0.09
Nodes (30): _as_numpy_array(), assert_close(), assert_close_nulp(), assert_equal(), assert_less(), _check_ns_shape_dtype(), _clone_function(), _CountingDaskScheduler (+22 more)

### Community 58 - "Community 58"
Cohesion: 0.11
Nodes (32): _download_data_to_bunch(), fetch_openml(), _get_data_description_by_id(), _get_data_features(), _get_data_info_by_name(), _get_data_qualities(), _get_json_content_from_openml_api(), _get_local_path() (+24 more)

### Community 59 - "Community 59"
Cohesion: 0.07
Nodes (14): MultiTaskElasticNet, MultiTaskElasticNetCV, MultiTaskLasso, MultiTaskLassoCV, Multi-task ElasticNet model trained with L1/L2 mixed-norm as regularizer.      T, Multi-task Lasso model trained with L1/L2 mixed-norm as regularizer.      The op, Multi-task L1/L2 ElasticNet with built-in cross-validation.      See glossary en, Multi-task Lasso model trained with L1/L2 mixed-norm as regularizer.      See gl (+6 more)

### Community 60 - "Community 60"
Cohesion: 0.07
Nodes (24): ArgKmin, ArgKminClassMode, BaseDistancesReductionDispatcher, RadiusNeighbors, RadiusNeighborsClassMode, # FIXME: the current Cython implementation is too slow for a large number of, # TODO: support CSR matrices without non-zeros elements, # TODO: support CSR matrices with int64 indices and indptr (+16 more)

### Community 61 - "Community 61"
Cohesion: 0.11
Nodes (32): adjusted_mutual_info_score(), adjusted_rand_score(), check_clusterings(), completeness_score(), contingency_matrix(), _entropy(), fowlkes_mallows_score(), _generalized_average() (+24 more)

### Community 62 - "Community 62"
Cohesion: 0.06
Nodes (11): BaseEnsemble, Check the base estimator.          Sets the `estimator_` attributes., Return the number of estimators in the ensemble., Return the index'th estimator in the ensemble., Return iterator over estimators in the ensemble., Base class for all ensemble classes.      Warning: This class should not be used, MetaEstimatorMixin, _available_if_base_estimator_has() (+3 more)

### Community 63 - "Community 63"
Cohesion: 0.11
Nodes (32): accuracy_score(), balanced_accuracy_score(), _check_set_wise_labels(), _check_targets(), _check_zero_division(), class_likelihood_ratios(), classification_report(), cohen_kappa_score() (+24 more)

### Community 64 - "Community 64"
Cohesion: 0.07
Nodes (19): Enum, _alpha_grid(), CD_Algo, enet_path(), Lasso, lasso_path(), LassoCV, LinearModelCV (+11 more)

### Community 65 - "Community 65"
Cohesion: 0.07
Nodes (27): _array_api_for_tests(), assert_allclose(), assert_allclose_dense_sparse(), assert_run_python_script_without_output(), check_docstring_parameters(), _convert_container(), _diff_key(), _get_args() (+19 more)

### Community 66 - "Community 66"
Cohesion: 0.08
Nodes (22): AgglomerationTransform, AgglomerativeClustering, FeatureAgglomeration, _hc_cut(), Hierarchical Agglomerative Clustering  These routines perform some hierarchical, Fit and return the result of each sample's clustering assignment.          In ad, Agglomerate features.      Recursively merges pair of clusters of features., Fit the hierarchical clustering on the data.          Parameters         ------- (+14 more)

### Community 67 - "Community 67"
Cohesion: 0.06
Nodes (17): KernelOperator, Product, Base class for all kernel operators.      .. versionadded:: 0.18, Get parameters of this kernel.          Parameters         ----------         de, Returns a list of all hyperparameter., Returns the (flattened, log-transformed) non-fixed hyperparameters.          Not, Sets the (flattened, log-transformed) non-fixed hyperparameters.          Parame, Returns the log-transformed bounds on the theta.          Returns         ------ (+9 more)

### Community 68 - "Community 68"
Cohesion: 0.06
Nodes (30): binary_log_loss(), inplace_exp(), inplace_identity(), inplace_identity_derivative(), inplace_logistic(), inplace_logistic_derivative(), inplace_relu(), inplace_relu_derivative() (+22 more)

### Community 69 - "Community 69"
Cohesion: 0.07
Nodes (2): eye(), zeros()

### Community 70 - "Community 70"
Cohesion: 0.11
Nodes (6): _BaseImputer, _check_inputs_dtype(), MissingIndicator, _most_frequent(), _safe_min(), SimpleImputer

### Community 71 - "Community 71"
Cohesion: 0.07
Nodes (1): Pipeline

### Community 72 - "Community 72"
Cohesion: 0.07
Nodes (22): _BinaryClassifierCurveDisplayMixin, _check_param_lengths(), _convert_to_list_leaving_none(), _deprecate_estimator_name(), _deprecate_y_pred_parameter(), _despine(), _interval_max_min_ratio(), Generate legend information dictionary and expand `metric` if required. (+14 more)

### Community 73 - "Community 73"
Cohesion: 0.09
Nodes (16): _BaseKMeans, BisectingKMeans, _BisectingTree, Bisecting K-means clustering., Warn when vcomp and mkl are both present, Calculate the sum of squared errors (inertia) per cluster.          Parameters, Split a cluster into 2 subsclusters.          Parameters         ----------, Tree structure representing the hierarchical clusters of BisectingKMeans. (+8 more)

### Community 74 - "Community 74"
Cohesion: 0.10
Nodes (19): EmpiricalCovariance, Maximum likelihood covariance estimator.      Read more in the :ref:`User Guide, Saves the covariance and precision estimates          Storage is done accordingl, Getter for the precision matrix.          Returns         -------         precis, Fit the maximum likelihood covariance estimator to X.          Parameters, Compute the Mean Squared Error between two covariance estimators.          Param, Compute the squared Mahalanobis distances of given observations.          For a, c_step() (+11 more)

### Community 75 - "Community 75"
Cohesion: 0.09
Nodes (24): _compute_gradient_3d(), _compute_n_patches(), _extract_patches(), extract_patches_2d(), grid_to_graph(), img_to_graph(), _make_edges_3d(), _mask_edges_weights() (+16 more)

### Community 76 - "Community 76"
Cohesion: 0.09
Nodes (22): _brute_mst(), _get_finite_row_indices(), HDBSCAN, _hdbscan_brute(), _hdbscan_prims(), _process_mst(), HDBSCAN: Hierarchical Density-Based Spatial Clustering          of Applications, Builds a single-linkage tree (SLT) from the provided minimum spanning tree     ( (+14 more)

### Community 77 - "Community 77"
Cohesion: 0.13
Nodes (7): dedent_lines(), A line-based string reader., Parameters         ----------         data : str            String with lines se, func_name : Descriptive text             continued text         another_func_nam, Grab signature (if given) and summary, Deindent a list of lines maximally, Reader

### Community 78 - "Community 78"
Cohesion: 0.08
Nodes (14): _inverse_binarize_multiclass(), _inverse_binarize_thresholding(), label_binarize(), LabelBinarizer, MultiLabelBinarizer, Transform the given indicator matrix into label sets.          Parameters, Fit label binarizer.          Parameters         ----------         y : ndarray, Fit label binarizer/transform multi-class labels to binary labels.          The (+6 more)

### Community 79 - "Community 79"
Cohesion: 0.07
Nodes (27): _approximate_mode(), cartesian(), density(), _deterministic_vector_sign_flip(), fast_logdet(), make_nonnegative(), _nanaverage(), Utilities to perform optimal mathematical operations in scikit-learn. (+19 more)

### Community 80 - "Community 80"
Cohesion: 0.11
Nodes (14): BiclusterMixin, BaseSpectral, _bistochastic_normalize(), _check_rows_and_columns(), consensus_score(), _jaccard(), _log_normalize(), _pairwise_similarity() (+6 more)

### Community 81 - "Community 81"
Cohesion: 0.09
Nodes (6): csr_copy_predict(), csr_copy_predict_proba(), csr_copy_predict_values(), csr_set_model(), csr_set_problem(), csr_to_libsvm()

### Community 82 - "Community 82"
Cohesion: 0.08
Nodes (26): _atol_for_type(), indexing_dtype(), _logsumexp(), Tools to support array_api., Yield mixed namespace and device inputs for testing.      We do not test for all, Return the absolute tolerance for a given numpy dtype., Return a platform-specific integer dtype suitable for indexing.      On 32-bit p, # TODO: once sufficiently adopted, we might want to instead rely on the (+18 more)

### Community 83 - "Community 83"
Cohesion: 0.10
Nodes (15): _auto_wrap_is_configured(), check_library_installed(), ContainerAdaptersManager, _get_adapter_from_container(), _get_container_adapter(), _get_output_config(), PandasAdapter, PolarsAdapter (+7 more)

### Community 84 - "Community 84"
Cohesion: 0.13
Nodes (13): eigh(), EighResult, EigResult, qr(), QRResult, slogdet(), SlogdetResult, svd() (+5 more)

### Community 85 - "Community 85"
Cohesion: 0.09
Nodes (17): _assess_dimension(), _infer_dimension(), PCA, Principal Component Analysis., Infers the dimension of a dataset with a given spectrum.      The returned value, Principal component analysis (PCA).      Linear dimensionality reduction using S, Compute the log-likelihood of a rank ``rank`` dataset.      The dataset is assum, Fit the model with X.          Parameters         ----------         X : {array- (+9 more)

### Community 86 - "Community 86"
Cohesion: 0.10
Nodes (2): _BaseComposition, FeatureUnion

### Community 87 - "Community 87"
Cohesion: 0.12
Nodes (21): dict, _check_unknown(), _encode(), _extract_missing(), _get_counts(), _map_to_integer(), MissingValues, _nandict (+13 more)

### Community 88 - "Community 88"
Cohesion: 0.08
Nodes (24): argpartition(), broadcast_shapes(), create_diagonal(), isin(), nan_to_num(), one_hot(), pad(), partition() (+16 more)

### Community 89 - "Community 89"
Cohesion: 0.10
Nodes (19): _cholesky_omp(), _gram_omp(), _omp_path_residues(), orthogonal_mp(), orthogonal_mp_gram(), OrthogonalMatchingPursuit, OrthogonalMatchingPursuitCV, Orthogonal matching pursuit algorithms (+11 more)

### Community 90 - "Community 90"
Cohesion: 0.09
Nodes (11): BayesianGaussianMixture, Check that the parameters are well defined.          Parameters         --------, Check the parameter of the Dirichlet distribution., Check the parameters of the Gaussian distribution.          Parameters         -, Check the prior parameters of the precision distribution.          Parameters, Check the `covariance_prior_`.          Parameters         ----------         X, Estimate the full Wishart distribution parameters.          Parameters         -, Estimate the tied Wishart distribution parameters.          Parameters         - (+3 more)

### Community 91 - "Community 91"
Cohesion: 0.10
Nodes (16): _check_params(), kneighbors_graph(), KNeighborsTransformer, _query_include_self(), radius_neighbors_graph(), RadiusNeighborsTransformer, Nearest Neighbors graph functions, Compute the (weighted) graph of Neighbors for points in X.      Neighborhoods ar (+8 more)

### Community 92 - "Community 92"
Cohesion: 0.10
Nodes (15): tuple, _changed_params(), _EstimatorPrettyPrinter, KeyValTuple, KeyValTupleParam, This module contains the _EstimatorPrettyPrinter class used in BaseEstimator.__r, Pretty Printer class for estimator objects.      This extends the pprint.PrettyP, Format dict items or parameters respecting the compact=True         parameter. F (+7 more)

### Community 93 - "Community 93"
Cohesion: 0.12
Nodes (12): _BaseEncoder, Fit the :class:`TargetEncoder` to X and y.          It is discouraged to use thi, Fit :class:`TargetEncoder` and transform `X` with the target encoding., Target Encoder for regression and classification targets.      Each category is, Transform X with the target encoding.          This method internally uses the `, Fit a target encoding with all the data., Learn target encodings., Learn multiclass encodings.          Learn encodings for each class (c) then reo (+4 more)

### Community 94 - "Community 94"
Cohesion: 0.16
Nodes (2): DensityMixin, BaseMixture

### Community 95 - "Community 95"
Cohesion: 0.08
Nodes (12): Classes labels available when `estimator` is a classifier.          Returns, Fit the RFE model and then the underlying estimator on the selected features., Reduce X to the selected features and predict using the estimator.          Para, Reduce X to the selected features and return the score of the estimator., Return the score and n_features per step for a fit across one fold., Compute the decision function of ``X``.          Parameters         ----------, Predict class probabilities for X.          Parameters         ----------, Predict class log-probabilities for X.          Parameters         ---------- (+4 more)

### Community 96 - "Community 96"
Cohesion: 0.11
Nodes (14): Loss functions for linear models with raw_prediction = X @ coef, Helper function to get coefficients and intercept.          Parameters         -, Helper function to get coefficients, intercept and raw_prediction.          Para, Compute the sandwich product X.T @ diag(W) @ X., Compute L1 penalty term: l1_reg_strength * ||w||_1., # TODO: This "sandwich product" is the main computational bottleneck for solvers, Compute L2 penalty term l2_reg_strength / 2 * ||w||_2^2., Compute the loss as weighted average over point-wise losses.          Parameters (+6 more)

### Community 97 - "Community 97"
Cohesion: 0.10
Nodes (22): _check_means(), _check_precision_matrix(), _check_precision_positivity(), _check_precisions(), _check_precisions_full(), _check_weights(), _estimate_gaussian_covariances_diag(), _estimate_gaussian_covariances_full() (+14 more)

### Community 98 - "Community 98"
Cohesion: 0.10
Nodes (9): _create_expansion(), PolynomialFeatures, This file contains preprocessing tools based on polynomials., Get output feature names for transformation.          Parameters         -------, Helper function for creating and appending sparse expansion matrices, Get output feature names for transformation.          Parameters         -------, Compute knot positions of splines.          Parameters         ----------, Transform each feature data to B-splines.          Parameters         ---------- (+1 more)

### Community 99 - "Community 99"
Cohesion: 0.09
Nodes (11): Exponentiation, Get parameters of this kernel.          Parameters         ----------         de, Returns a list of all hyperparameter., Returns the (flattened, log-transformed) non-fixed hyperparameters.          Not, Sets the (flattened, log-transformed) non-fixed hyperparameters.          Parame, Returns the log-transformed bounds on the theta.          Returns         ------, Return the kernel k(X, Y) and optionally its gradient.          Parameters, Returns the diagonal of the kernel k(X, X).          The result of this method i (+3 more)

### Community 100 - "Community 100"
Cohesion: 0.12
Nodes (12): at, Allow for the alternate syntax ``at(x)[start:stop:step]``.          It looks pre, Implement all update operations.          Parameters         ----------, Apply ``x[idx] = y`` and return the update array., Apply ``x[idx] += y`` and return the updated array., Apply ``x[idx] -= y`` and return the updated array., Apply ``x[idx] *= y`` and return the updated array., Apply ``x[idx] /= y`` and return the updated array. (+4 more)

### Community 101 - "Community 101"
Cohesion: 0.11
Nodes (6): copy_predict(), copy_predict_proba(), copy_predict_values(), dense_to_libsvm(), set_model(), set_problem()

### Community 102 - "Community 102"
Cohesion: 0.14
Nodes (3): _check_gcv_mode(), _IdentityClassifier, _RidgeGCV

### Community 103 - "Community 103"
Cohesion: 0.13
Nodes (22): _array_indexing(), _determine_key_type(), _get_column_indices(), _get_column_indices_for_bool_or_int(), _list_indexing(), _narwhals_indexing(), _pandas_indexing(), Determine the data type of key.      Parameters     ----------     key : scalar, (+14 more)

### Community 104 - "Community 104"
Cohesion: 0.10
Nodes (11): ARDRegression, BayesianRidge, Various bayesian regression, Fit the model.          Parameters         ----------         X : ndarray of sha, Bayesian ridge regression.      Fit a Bayesian ridge model. See the Notes sectio, Predict using the linear model.          In addition to the mean of the predicti, Update posterior mean and compute corresponding sse (sum of squared errors)., Log marginal likelihood. (+3 more)

### Community 105 - "Community 105"
Cohesion: 0.12
Nodes (18): arange(), argsort(), asarray(), astype(), clip(), _ensure_single_chunk(), Array API compatibility wrapper for asarray().      See the corresponding docume, # TODO: respect device keyword? (+10 more)

### Community 106 - "Community 106"
Cohesion: 0.11
Nodes (15): Extra array functions built on top of the array API standard., _AtOp, Update operations for read-only arrays., Operations for use in `xpx.at`., Return string representation (useful for pytest logs).          Returns, Sentinel for undefined values., Undef, _is_jax_jit_enabled() (+7 more)

### Community 107 - "Community 107"
Cohesion: 0.11
Nodes (11): BaseSearchCV, BaseSuccessiveHalving, Custom refit callable to return the index of the best candidate.          We wan, Run fit with all sets of parameters.          Parameters         ----------, Splitter that subsamples a given fraction of the dataset, # TODO: remove this when we add array API support to, Trim results to the last halving iteration only., Implements successive halving.      Ref:     Almost optimal exploration in multi (+3 more)

### Community 108 - "Community 108"
Cohesion: 0.11
Nodes (15): _ledoit_wolf(), ledoit_wolf_shrinkage(), LedoitWolf, Covariance estimators using shrinkage.  Shrinkage corresponds to regularising `c, Calculate covariance matrices shrunk on the diagonal.      Read more in the :ref, Covariance estimator with shrinkage.      Read more in the :ref:`User Guide <shr, Fit the shrunk covariance model to X.          Parameters         ----------, Estimate the shrunk Ledoit-Wolf covariance matrix.      Read more in the :ref:`U (+7 more)

### Community 109 - "Community 109"
Cohesion: 0.11
Nodes (13): _BaseHeterogeneousEnsemble, _fit_single_estimator(), _partition_estimators(), Base class for ensemble-based estimators., Make and configure a copy of the `estimator_` attribute.          Warning: This, Private function used to partition estimators between jobs., Base class for heterogeneous ensemble of learners.      Parameters     ---------, Dictionary to access any fitted sub-estimators by name.          Returns (+5 more)

### Community 110 - "Community 110"
Cohesion: 0.10
Nodes (11): _approx_fprime(), _check_length_scale(), Matern, PairwiseKernel, Return the kernel k(X, Y) and optionally its gradient.          Parameters, Matern kernel.      The class of Matern kernels is a generalization of the :clas, Return the kernel k(X, Y) and optionally its gradient.          Parameters, Wrapper for kernels in sklearn.metrics.pairwise.      A thin wrapper around the (+3 more)

### Community 111 - "Community 111"
Cohesion: 0.12
Nodes (9): LocalOutlierFactor, Unsupervised Outlier Detection using the Local Outlier Factor (LOF).      The an, Fit the model to the training set X and return the labels.          **Not availa, Fit the local outlier factor detector from the training dataset.          Parame, Predict the labels (1 inlier, -1 outlier) of X according to LOF.          **Only, Predict the labels (1 inlier, -1 outlier) of X according to LOF.          If X i, Shifted opposite of the Local Outlier Factor of X.          Bigger is better, i., Opposite of the Local Outlier Factor of X.          It is the opposite as bigger (+1 more)

### Community 112 - "Community 112"
Cohesion: 0.11
Nodes (15): _fetch_fixture(), hide_available_matplotlib(), hide_available_pandas(), munge_scipy_to_check_spmatrix_usage(), pyplot(), pytest_collection_modifyitems(), pytest_configure(), pytest_generate_tests() (+7 more)

### Community 113 - "Community 113"
Cohesion: 0.14
Nodes (10): Tools for model inspection., PartialDependenceDisplay, Plot 2-way partial dependence.          Parameters         ----------         av, Plot partial dependence plots.          Parameters         ----------         ax, Partial Dependence Plot (PDP) and Individual Conditional Expectation (ICE)., Partial dependence (PD) and individual conditional expectation (ICE) plots., Compute the number of samples as an integer., Plot the ICE lines.          Parameters         ----------         preds : ndarr (+2 more)

### Community 114 - "Community 114"
Cohesion: 0.11
Nodes (12): _adjusted_metric(), RadiusNeighborsClassifier, Nearest Neighbor Classification, Return probability estimates for the test data X.          Parameters         --, # TODO: systematize this mapping of metric for, # TODO: Implement efficient multi-output solution, # TODO: adapt the heuristic for `strategy="auto"` for, Classifier implementing a vote among neighbors within a given radius.      Read (+4 more)

### Community 115 - "Community 115"
Cohesion: 0.15
Nodes (8): BernoulliRBM, Restricted Boltzmann Machine, Computes the probabilities P(h=1|v).          Parameters         ----------, Sample from the distribution P(h|v).          Parameters         ----------, Perform one Gibbs sampling step.          Parameters         ----------, Inner fit for one mini-batch.          Adjust the parameters to maximize the lik, Compute the pseudo-likelihood of X.          Parameters         ----------, Fit the model to the data X.          Parameters         ----------         X :

### Community 116 - "Community 116"
Cohesion: 0.14
Nodes (15): BaseGraphicalLasso, _dual_gap(), _graphical_lasso(), graphical_lasso_path(), GraphicalLasso, _objective(), GraphicalLasso: sparse inverse covariance estimation with an l1-penalized estima, # NOTE: Warm-restarting graphical_lasso_path has been tried, (+7 more)

### Community 117 - "Community 117"
Cohesion: 0.14
Nodes (7): DiscriminantAnalysisPredictionMixin, DiscriminantAnalysisPredictionMixin, NearestCentroid, Nearest Centroid Classification, Fit the NearestCentroid model according to the given training data.          Par, Perform classification on an array of test vectors `X`.          The predicted c, Nearest centroid classifier.      Each class is represented by its centroid, wit

### Community 118 - "Community 118"
Cohesion: 0.13
Nodes (13): _graph_connected_component(), _graph_is_connected(), Set the diagonal of the laplacian matrix and convert it to a     sparse format w, Project the sample on the first eigenvectors of the graph Laplacian.      The ad, Find the largest graph connected components that contains one     given node., Spectral embedding for non-linear dimensionality reduction.      Forms an affini, Calculate the affinity matrix from data         Parameters         ----------, Fit the model from data in X.          Parameters         ----------         X : (+5 more)

### Community 119 - "Community 119"
Cohesion: 0.18
Nodes (4): Mapping, NumpyDocString, Parses a numpydoc string to an abstract representation      Instances define a m, .. index:: default            :refguide: something, else, and more

### Community 120 - "Community 120"
Cohesion: 0.13
Nodes (7): FunctionTransformer, _identity(), Fit transformer by checking X.          If ``validate`` is ``True``, ``X`` will, Transform X using the inverse function.          Parameters         ----------, Get output feature names for transformation.          This method is only define, Return True since FunctionTransformer is stateless., Set output container.          Refer to the :ref:`user guide <df_output_transfor

### Community 121 - "Community 121"
Cohesion: 0.12
Nodes (17): asarrays(), capabilities(), eager_shape(), in1d(), is_python_scalar(), jax_autojit(), meta_namespace(), ndindex() (+9 more)

### Community 122 - "Community 122"
Cohesion: 0.11
Nodes (8): MetadataRequest, Return subset of `params` consumed by the method that owns this instance., Container for storing metadata request info and an associated consumer (`owner`), Return params consumed as metadata in a :term:`consumer`.          This method r, Get names of all metadata that can be consumed or routed by specified \, Prepare the given parameters to be passed to the method.          The output of, Check whether metadata is passed which is marked as WARN.          If any metada, Serialize the object.          Returns         -------         obj : dict

### Community 123 - "Community 123"
Cohesion: 0.13
Nodes (16): check_classification_targets(), _check_partial_fit_first_call(), class_distribution(), _is_integral_float(), is_multilabel(), _ovr_decision_function(), Utilities to handle multiclass/multioutput target in classifiers., Check if ``y`` is in a multilabel format.      Parameters     ----------     y : (+8 more)

### Community 124 - "Community 124"
Cohesion: 0.14
Nodes (8): Check transformer and fit transformer.          Create the default transformer,, Fit the model according to the given training data.          Parameters, # FIXME: a FunctionTransformer can return a 1D array even when validate, Meta-estimator to regress on a transformed target.      Useful for applying a no, Predict using the base regressor, applying inverse.          The regressor is us, Number of features seen during :term:`fit`., Get metadata routing of this object.          Please check :ref:`User Guide <met, TransformedTargetRegressor

### Community 125 - "Community 125"
Cohesion: 0.17
Nodes (10): EllipticEnvelope, An object for detecting outliers in a Gaussian distributed dataset.      Read mo, Fit the EllipticEnvelope model.          Parameters         ----------         X, Compute the decision function of the given observations.          Parameters, Compute the negative Mahalanobis distances.          Parameters         --------, Predict labels (1 inlier, -1 outlier) of X according to fitted model.          P, Return the mean accuracy on the given test data and labels.          In multi-la, MinCovDet (+2 more)

### Community 126 - "Community 126"
Cohesion: 0.12
Nodes (18): Warning used when the metric is invalid      .. versionchanged:: 0.18        Mov, UndefinedMetricWarning, hinge_loss(), Compute the Matthews correlation coefficient (MCC).      The Matthews correlatio, Zero-one classification loss.      If normalize is ``True``, returns the fractio, Compute the F1 score, also known as balanced F-score or F-measure.      The F1 s, Compute binary classification positive and negative likelihood ratios.      The, Compute the balanced accuracy.      The balanced accuracy in binary and multicla (+10 more)

### Community 127 - "Community 127"
Cohesion: 0.12
Nodes (13): ArffDecoder, BadAttributeName, BadRelationFormat, load(), loads(), Load a file-like object containing the ARFF document and convert it into     a P, Convert a string instance containing the ARFF document into a Python     object., Error raised when the relation declaration is in an invalid format. (+5 more)

### Community 128 - "Community 128"
Cohesion: 0.11
Nodes (8): _estimator_has(), FrozenEstimator, Set the parameters of this estimator.          The only valid key here is `estim, Check that final_estimator has `attr`.      Used together with `available_if`., Get parameters for this estimator.          Returns a `{"estimator": estimator}`, Estimator that wraps a fitted estimator to prevent re-fitting.      This meta-es, __getitem__ is defined in :class:`~sklearn.pipeline.Pipeline` and \, No-op.          As a frozen estimator, calling `fit` has no effect.          Par

### Community 129 - "Community 129"
Cohesion: 0.11
Nodes (10): _HTMLDocumentationLinkMixin, _IDCounter, Generate sequential ids with a prefix., Mixin to handle consistently the HTML representation.      When inheriting from, HTML representation of estimator.         This is redundant with the logic of `_, This function is returned by the @property `_repr_html_` to make         `hasatt, Mime bundle used by jupyter kernels to display estimator, Mixin class allowing to generate a link to the API documentation.      This mixi (+2 more)

### Community 130 - "Community 130"
Cohesion: 0.16
Nodes (12): detectTheme(), estimator_html_repr(), forceTheme(), _get_visual_block(), Write labeled html with or without a dropdown with named details.      Parameter, Generate information about how to display an estimator., Write estimator to html in serial, parallel, or by itself (single).      For mul, HTML Representation of Estimator      Parameters     ----------     kind : {'ser (+4 more)

### Community 131 - "Community 131"
Cohesion: 0.16
Nodes (4): Semi-supervised learning algorithms.  These algorithms utilize small amounts of, BaseLabelPropagation, LabelPropagation, LabelSpreading

### Community 132 - "Community 132"
Cohesion: 0.13
Nodes (7): BaseMixture, GaussianMixture, Gaussian Mixture.      Representation of a Gaussian mixture model probability di, Return the number of free parameters in the model., Bayesian information criterion for the current model on the input X.          Yo, Akaike information criterion for the current model on the input X.          You, Mixture modeling algorithms.

### Community 133 - "Community 133"
Cohesion: 0.27
Nodes (1): LatentDirichletAllocation

### Community 134 - "Community 134"
Cohesion: 0.13
Nodes (12): Exception, ArffException, BadAttributeFormat, BadAttributeType, BadNominalFormatting, BadStringValue, Error raised when some attribute declaration is in an invalid format., Error raised when some invalid type is provided into the attribute     declarati (+4 more)

### Community 135 - "Community 135"
Cohesion: 0.17
Nodes (11): BadDataFormat, BadLayout, BadNumericalValue, DenseGeneratorData, _parse_values(), (INTERNAL) Split a line into a list of values, Error raised when some data instance is in an invalid format., Error raised when and invalid numerical value is used in some data     instance. (+3 more)

### Community 136 - "Community 136"
Cohesion: 0.15
Nodes (11): _get_feature_importances(), Generic feature selection mixin, Reduce X to the selected features., Reverse the transformation operation.          Parameters         ----------, Mask feature names according to selected features.          Parameters         -, Retrieve and aggregate (ndim > 1)  the feature importances     from an estimator, Transformer mixin that performs feature selection given a support mask.      Thi, Get a mask, or integer index, of the features selected.          Parameters (+3 more)

### Community 137 - "Community 137"
Cohesion: 0.13
Nodes (10): KNeighborsMixin, KNeighborsRegressor, Fit the k-nearest neighbors regressor from the training dataset.          Parame, Regression based on k-nearest neighbors.      The target is predicted by local i, Predict the target for the provided data.          Parameters         ----------, NearestNeighbors, Unsupervised nearest neighbors learner, Unsupervised learner for implementing neighbor searches.      Read more in the : (+2 more)

### Community 138 - "Community 138"
Cohesion: 0.12
Nodes (1): Version

### Community 139 - "Community 139"
Cohesion: 0.18
Nodes (9): _cached_transform(), _final_estimator_has(), _fit_one(), _fit_transform_one(), _fit_transform_one_with_callbacks(), make_pipeline(), make_union(), _name_estimators() (+1 more)

### Community 140 - "Community 140"
Cohesion: 0.12
Nodes (17): _asarray_with_order(), _check_array_api_dispatch(), _count_nonzero(), _cov(), _expit(), get_namespace(), _logit(), Helper to support the order kwarg only for NumPy-backed arrays      Memory layou (+9 more)

### Community 141 - "Community 141"
Cohesion: 0.13
Nodes (12): delayed(), _FuncWrapper, _get_threadpool_controller(), Customizations of :mod:`joblib` and :mod:`threadpoolctl` tools for scikit-learn, Load the global configuration before calling the function., Return the global threadpool controller instance., Decorator to limit the number of threads used at the function level.      It sho, Helper function that intends to attach a config to a delayed function. (+4 more)

### Community 142 - "Community 142"
Cohesion: 0.17
Nodes (17): as_float_array(), check_array(), _check_estimator_name(), check_X_y(), _check_y(), column_or_1d(), _ensure_no_complex_data(), _is_extension_array_dtype() (+9 more)

### Community 143 - "Community 143"
Cohesion: 0.12
Nodes (16): _allclose_dense_sparse(), check_memory(), _check_pos_label_consistency(), check_random_state(), check_scalar(), _deprecate_positional_args(), has_fit_parameter(), Functions to validate input and parameters within scikit-learn estimators. (+8 more)

### Community 144 - "Community 144"
Cohesion: 0.13
Nodes (6): Log for one run of a scoring monitor.      The recorded scores are accessed thro, Restore state, opening a fresh listener if the inherited one is unusable., Retrieve the logged scores.          Log entries are grouped by runs, which are, Callback that monitors a score for each iterative step of an estimator.      The, ScoringMonitor, ScoringMonitorLog

### Community 145 - "Community 145"
Cohesion: 0.16
Nodes (11): cluster_qr(), discretize(), Algorithms for spectral clustering, Apply clustering to a projection of the normalized Laplacian.      In practice S, Find the discrete partition closest to the eigenvector embedding.          This, Apply clustering to a projection of the normalized Laplacian.      In practice S, Search for a partition matrix which is closest to the eigenvector embedding., Perform spectral clustering from features, or affinity matrix.          Paramete (+3 more)

### Community 147 - "Community 147"
Cohesion: 0.17
Nodes (9): Algorithms for cross decomposition., CCA, _center_scale_xy(), _get_first_singular_vectors_power_method(), _get_first_singular_vectors_svd(), _pinv2_old(), PLSCanonical, PLSRegression (+1 more)

### Community 148 - "Community 148"
Cohesion: 0.13
Nodes (10): __array_namespace_info__, Array API Inspection namespace  This is the namespace for inspection functions a, The default device used for new CuPy arrays.          See Also         --------, The default data types used for new CuPy arrays.          For CuPy, this always, # TODO: Does this depend on device?, The array API data types supported by CuPy.          Note that this function onl, # TODO: Does this depend on device?, Get the array API inspection namespace for CuPy.      The array API inspection n (+2 more)

### Community 149 - "Community 149"
Cohesion: 0.13
Nodes (16): PositiveSpectrumWarning, Warning raised when the eigenvalues of a PSD matrix have issues      This warnin, _check_categorical_features(), _check_monotonic_cst(), _check_psd_eigenvalues(), _check_response_method(), check_symmetric(), _estimator_has() (+8 more)

### Community 150 - "Community 150"
Cohesion: 0.17
Nodes (4): CountVectorizer, _document_frequency(), _make_int_array(), Check if vocabulary is empty or missing (not fitted)

### Community 151 - "Community 151"
Cohesion: 0.16
Nodes (12): _breakdown_point(), _lstsq(), _modified_weiszfeld_step(), A Theil-Sen Estimator for Multiple Linear Regression Model, Approximation of the breakdown point.      Parameters     ----------     n_sampl, Least Squares Estimator for TheilSenRegressor class.      This function calculat, Theil-Sen Estimator: robust multivariate regression model.      The algorithm ca, Modified Weiszfeld step.      This function defines one iteration step in order (+4 more)

### Community 152 - "Community 152"
Cohesion: 0.13
Nodes (3): LegacyVersion, parse(), Parse the given version from a string to an appropriate class.      Parameters

### Community 153 - "Community 153"
Cohesion: 0.16
Nodes (15): RuntimeError, _cg(), _check_optimize_result(), _line_search_wolfe1(), _line_search_wolfe12(), _LineSearchError, _newton_cg(), Our own implementation of the Newton algorithm  Unlike the scipy.optimize versio (+7 more)

### Community 154 - "Community 154"
Cohesion: 0.19
Nodes (10): ArffEncoder, dump(), dumps(), Serialize an object representing the ARFF document to a given file-like     obje, Serialize an object representing the ARFF document, returning a string.      :pa, (INTERNAL) Encodes a comment line.          Comments are single line strings sta, (INTERNAL) Decodes a relation line.          The relation declaration is a line, (INTERNAL) Encodes an attribute line.          The attribute follow the template (+2 more)

### Community 155 - "Community 155"
Cohesion: 0.18
Nodes (14): _compute_mi(), _compute_mi_cc(), _compute_mi_cd(), _estimate_mi(), _iterate_columns(), mutual_info_classif(), mutual_info_regression(), Compute mutual information between two variables.      This is a simple wrapper (+6 more)

### Community 156 - "Community 156"
Cohesion: 0.16
Nodes (14): chi2(), _chisquare(), f_classif(), f_oneway(), f_regression(), r_regression(), Univariate features selection., Compute the ANOVA F-value for the provided sample.      Read more in the :ref:`U (+6 more)

### Community 157 - "Community 157"
Cohesion: 0.13
Nodes (7): ElasticNet, ElasticNetCV, Sparse representation of the fitted `coef_`., Decision function of the linear model.          Parameters         ----------, Elastic Net model with iterative fitting along a regularization path.      See g, Fit ElasticNet model with coordinate descent.          Fit is on grid of alphas, Linear regression with combined L1 and L2 priors as regularizer.      Minimizes

### Community 158 - "Community 158"
Cohesion: 0.16
Nodes (8): _dynamic_max_trials(), RANSACRegressor, Fit estimator using RANSAC algorithm.          Parameters         ----------, Determine number trials such that at least one outlier-free subset is     sample, Predict using the estimated model.          This is a wrapper for `estimator_.pr, Return the score of the prediction.          This is a wrapper for `estimator_.s, Get metadata routing of this object.          Please check :ref:`User Guide <met, RANSAC (RANdom SAmple Consensus) algorithm.      RANSAC is an iterative algorith

### Community 159 - "Community 159"
Cohesion: 0.19
Nodes (7): _gradient_descent(), _joint_probabilities(), _joint_probabilities_nn(), _kl_divergence(), _kl_divergence_bh(), trustworthiness(), TSNE

### Community 160 - "Community 160"
Cohesion: 0.13
Nodes (8): __array_namespace_info__, Array API Inspection namespace  This is the namespace for inspection functions a, The default device used for new NumPy arrays.          For NumPy, this always re, The default data types used for new NumPy arrays.          For NumPy, this alway, The array API data types supported by NumPy.          Note that this function on, The devices supported by NumPy.          For NumPy, this always returns ``['cpu', Get the array API inspection namespace for NumPy.      The array API inspection, Return a dictionary of array API library capabilities.          The resulting di

### Community 161 - "Community 161"
Cohesion: 0.18
Nodes (10): _check_boundary_response_method(), DecisionBoundaryDisplay, _deprecate_multiclass_colors(), Decisions boundary visualization.      It is recommended to use     :func:`~skle, Validate the response methods to be used with the fitted estimator.      Paramet, Plot visualization.          Parameters         ----------         plot_method :, Plot decision boundary given an estimator.          Read more in the :ref:`User, Handle deprecation of `multiclass_colors` renamed to `target_colors`. (+2 more)

### Community 162 - "Community 162"
Cohesion: 0.20
Nodes (6): BaseRandomProjection, _check_density(), _check_input_size(), _gaussian_random_matrix(), johnson_lindenstrauss_min_dim(), _sparse_random_matrix()

### Community 163 - "Community 163"
Cohesion: 0.18
Nodes (15): check_same_namespace(), _cholesky(), get_namespace_and_device(), _is_numpy_namespace(), _linalg_solve(), _matching_numpy_dtype(), _modify_in_place_if_numpy(), _nanmax() (+7 more)

### Community 164 - "Community 164"
Cohesion: 0.17
Nodes (15): check_estimator(), _check_name(), estimator_checks_generator(), _maybe_mark(), _raise_for_missing_tags(), _should_be_skipped_or_marked(), _yield_all_checks(), _yield_api_checks() (+7 more)

### Community 165 - "Community 165"
Cohesion: 0.14
Nodes (8): __array_namespace_info__, Array API Inspection namespace  This is the namespace for inspection functions a, The default device used for new Dask arrays.          For Dask, this always retu, The default data types used for new Dask arrays.          For Dask, this always, The array API data types supported by Dask.          Note that this function onl, The devices supported by Dask.          For Dask, this always returns ``['cpu',, Get the array API inspection namespace for Dask.      The array API inspection n, Return a dictionary of array API library capabilities.          The resulting di

### Community 166 - "Community 166"
Cohesion: 0.19
Nodes (13): calinski_harabasz_score(), check_number_of_labels(), davies_bouldin_score(), Unsupervised evaluation metrics., Accumulate silhouette statistics for vertical chunk of X.      Parameters     --, Compute the Silhouette Coefficient for each sample.      The Silhouette Coeffici, Check that number of labels are valid.      Parameters     ----------     n_labe, Compute the Calinski and Harabasz score.      It is also known as the Variance R (+5 more)

### Community 167 - "Community 167"
Cohesion: 0.26
Nodes (10): DTypesAll, DTypesBool, DTypesComplex, DTypesIntegral, DTypesNumeric, DTypesReal, DTypesSigned, DTypesUnsigned (+2 more)

### Community 168 - "Community 168"
Cohesion: 0.29
Nodes (12): _laplace(), _laplace_normed(), _laplace_normed_sym(), _laplace_sym(), laplacian(), _laplacian_dense(), _laplacian_dense_flo(), _laplacian_sparse_flo() (+4 more)

### Community 169 - "Community 169"
Cohesion: 0.16
Nodes (4): asarray(), isin(), Array API compatibility wrapper for asarray().      See the corresponding docume, searchsorted()

### Community 170 - "Community 170"
Cohesion: 0.21
Nodes (13): _liac_arff_parser(), load_arff_from_gzip_file(), _pandas_arff_parser(), _post_process_frame(), Implementation of ARFF parsers: via LIAC-ARFF and pandas., ARFF parser using the LIAC-ARFF library coded purely in Python.      This parser, Obtains several columns from sparse ARFF representation. Additionally,     the c, ARFF parser using `pandas.read_csv`.      This parser uses the metadata fetched (+5 more)

### Community 171 - "Community 171"
Cohesion: 0.20
Nodes (13): _download_20newsgroups(), fetch_20newsgroups(), fetch_20newsgroups_vectorized(), Caching loader for the 20 newsgroups text classification dataset.   The descript, Given text in "news" format, strip the headers, by removing everything     befor, Given text in "news" format, strip lines beginning with the quote     characters, Given text in "news" format, attempt to remove a signature block.      As a roug, Load the filenames and data from the 20 newsgroups dataset \ (classification). (+5 more)

### Community 172 - "Community 172"
Cohesion: 0.19
Nodes (2): TfidfTransformer, TfidfVectorizer

### Community 173 - "Community 173"
Cohesion: 0.15
Nodes (14): brier_score_loss(), d2_brier_score(), d2_log_loss_score(), _one_hot_encoding_binary_target(), _one_hot_encoding_multiclass_target(), Convert multi-class `y_true` into a one-hot encoded array and also ensure     th, r"""Convert y_true and y_prob to shape (n_samples, n_classes)      1. Verify tha, Convert binary `y_true` into a one-hot encoded array and also ensure that     th (+6 more)

### Community 174 - "Community 174"
Cohesion: 0.16
Nodes (7): The k-nearest neighbors algorithms., KernelDensity, Fit the Kernel Density model on the data.          Parameters         ----------, Compute the log-likelihood of each sample under the model.          Parameters, Compute the total log-likelihood under the model.          Parameters         --, Generate random samples from the model.          Currently, this is implemented, Kernel Density Estimation.      Read more in the :ref:`User Guide <kernel_densit

### Community 175 - "Community 175"
Cohesion: 0.14
Nodes (8): __array_namespace_info__, Array API Inspection namespace  This is the namespace for inspection functions a, The default data types used for new PyTorch arrays.          Parameters, Get the array API inspection namespace for PyTorch.      The array API inspectio, The array API data types supported by PyTorch.          Note that this function, The devices supported by PyTorch.          Returns         -------         devic, Return a dictionary of array API library capabilities.          The resulting di, The default device used for new PyTorch arrays.          See Also         ------

### Community 176 - "Community 176"
Cohesion: 0.19
Nodes (9): deprecated, Decorator to mark a function or class as deprecated.      Issue a warning when t, Call method          Parameters         ----------         obj : object, Decorate function fun, randomized_range_finder(), Compute an orthonormal matrix whose range approximates the range of A.      Para, Body of randomized_range_finder without input validation., Row-wise (squared) Euclidean norm of X.      Equivalent to np.sqrt((X * X).sum(a (+1 more)

### Community 177 - "Community 177"
Cohesion: 0.17
Nodes (7): _BasePCA, IncrementalPCA, Incremental Principal Components Analysis., Incremental principal components analysis (IPCA).      Linear dimensionality red, Fit the model with X, using minibatches of size batch_size.          Parameters, Incremental fit with X. All of X is processed as a single batch.          Parame, Apply dimensionality reduction to X.          X is projected on the first princi

### Community 178 - "Community 178"
Cohesion: 0.15
Nodes (8): _from_reconstruction_attributes(), get_context_path(), Helper to call the hook of all callbacks with their respective arguments., Call the `on_fit_task_begin` hook of the callbacks.          Parameters, Call the `on_fit_task_end` hook of the callbacks.          Parameters         --, Propagate the context and callbacks to a sub-estimator.          Clear the propa, Return a copy of the estimator as if it was fitted.      Parameters     --------, Helper function to get the path from the root context down to a given context.

### Community 179 - "Community 179"
Cohesion: 0.21
Nodes (12): _dump_svmlight(), dump_svmlight_file(), _gen_open(), load_svmlight_file(), load_svmlight_files(), _open_and_load(), This module implements a loader and dumper for the svmlight format  This format, Load dataset from multiple files in SVMlight format.      This function is equiv (+4 more)

### Community 180 - "Community 180"
Cohesion: 0.26
Nodes (8): ArffContainerType, Data, _DataListMixin, _get_data_object_for_decoding(), _get_data_object_for_encoding(), LODData, LODGeneratorData, Mixin to return a list from decode_rows instead of a generator

### Community 181 - "Community 181"
Cohesion: 0.19
Nodes (2): DictVectorizer, Feature extraction from raw data.

### Community 182 - "Community 182"
Cohesion: 0.18
Nodes (4): csr_set_problem(), csr_to_sparse(), dense_to_sparse(), set_problem()

### Community 183 - "Community 183"
Cohesion: 0.17
Nodes (10): _compute_precision_cholesky(), _compute_precision_cholesky_from_precisions(), _estimate_gaussian_parameters(), _flipudlr(), Estimate the Gaussian distribution parameters.      Parameters     ----------, Compute the Cholesky decomposition of the precisions.      Parameters     ------, Reverse the rows and columns of an array., r"""Compute the Cholesky decomposition of precisions using precisions themselves (+2 more)

### Community 184 - "Community 184"
Cohesion: 0.21
Nodes (6): PrecisionRecallDisplay, Precision Recall visualization.      It is recommended to use     :func:`~sklear, Plot visualization.          Parameters         ----------         ax : Matplotl, Plot precision-recall curve given an estimator and some data.          For gener, Plot precision-recall curve given binary class predictions.          For general, Plot multi-fold precision-recall curves given cross-validation results.

### Community 185 - "Community 185"
Cohesion: 0.21
Nodes (6): Plot visualization.          Parameters         ----------         ax : matplotl, ROC Curve visualization.      It is recommended to use     :func:`~sklearn.metri, Create a ROC Curve display from an estimator.          For general information r, Plot ROC curve given the true and predicted values.          For general informa, Create a multi-fold ROC curve display given cross-validation results.          ., RocCurveDisplay

### Community 186 - "Community 186"
Cohesion: 0.17
Nodes (7): CallbackSupportMixin, HeterogeneousMetaEstimator, NoSubtaskEstimator, A class that mimics a third-party estimator with callback support only using, A meta-estimator that fits a list of estimators in order., A class mimicking an estimator without subtasks in fit., ThirdPartyEstimator

### Community 187 - "Community 187"
Cohesion: 0.23
Nodes (11): _check_fetch_lfw(), _fetch_lfw_pairs(), _fetch_lfw_people(), _load_imgs(), Labeled Faces in the Wild (LFW) dataset  This dataset is a collection of JPEG pi, Internally used to load images, Perform the actual data loading for the lfw people dataset      This operation i, Load the Labeled Faces in the Wild (LFW) people dataset \ (classification). (+3 more)

### Community 188 - "Community 188"
Cohesion: 0.24
Nodes (2): FactorAnalysis, _ortho_rotation()

### Community 189 - "Community 189"
Cohesion: 0.30
Nodes (1): KernelPCA

### Community 190 - "Community 190"
Cohesion: 0.23
Nodes (2): _calculate_threshold(), SelectFromModel

### Community 191 - "Community 191"
Cohesion: 0.20
Nodes (5): Sequential feature selection, Learn the features to select from X.          Parameters         ----------, Get metadata routing of this object.          Please check :ref:`User Guide <met, Transformer that performs Sequential Feature Selection.      This Sequential Fea, SequentialFeatureSelector

### Community 192 - "Community 192"
Cohesion: 0.20
Nodes (6): Score functions, performance metrics, pairwise metrics and distance computations, PredictionErrorDisplay, Visualization of the prediction error of a regression model.      This tool can, Plot the prediction error given a regressor and some data.          For general, Plot the prediction error given the true and predicted targets.          For gen, Plot visualization.          Extra keyword arguments will be passed to matplotli

### Community 193 - "Community 193"
Cohesion: 0.18
Nodes (6): FunctionDoc, ObjDoc, Extract reference documentation from the NumPy source tree., Remove leading and trailing blank lines from a list of lines, # NOTE: param line with single element should never have a, strip_blank_lines()

### Community 194 - "Community 194"
Cohesion: 0.17
Nodes (2): NegativeInfinityType, Vendoered from https://github.com/pypa/packaging/blob/main/packaging/_structures

### Community 195 - "Community 195"
Cohesion: 0.23
Nodes (9): _cmpkey(), InvalidVersion, _legacy_cmpkey(), _parse_letter_version(), _parse_local_version(), _parse_version_parts(), Vendored from https://github.com/pypa/packaging/blob/main/packaging/version.py, Takes a string like abc.1.twelve and turns it into ("abc", 1, "twelve"). (+1 more)

### Community 196 - "Community 196"
Cohesion: 0.21
Nodes (11): is_df_or_series(), is_pandas_df_or_series(), is_polars_df(), is_polars_df_or_series(), is_pyarrow_data(), Functions to determine if an object is a dataframe or series., Return True if the X is a dataframe or series.      Parameters     ----------, Return True if the X is a pandas dataframe or series.      Parameters     ------ (+3 more)

### Community 197 - "Community 197"
Cohesion: 0.18
Nodes (5): _BaseComposition, Utilities for meta-estimators., Create subset of dataset and properly handle kernels.      Slice X, y according, Base class for estimators that are composed of named sub-estimators.      This a, _safe_split()

### Community 198 - "Community 198"
Cohesion: 0.22
Nodes (6): _BinaryClassifierCurveDisplayMixin, DetCurveDisplay, Plot DET curve given an estimator and data.          For general information reg, Detection Error Tradeoff (DET) curve visualization.      It is recommended to us, Plot the DET curve given the true and predicted labels.          For general inf, Plot visualization.          Parameters         ----------         ax : matplotl

### Community 199 - "Community 199"
Cohesion: 0.20
Nodes (10): can_reuse_listener(), close_listener(), ListenerHandle, open_listener(), Stop listening for `listener_handle` and free its background threads., Whether the listener at `listener_handle` is usable from this process.      Help, Deliver `message` to whoever is listening on `listener_handle`.      There are t, A picklable reference to a main-process listener.      Attributes     ---------- (+2 more)

### Community 200 - "Community 200"
Cohesion: 0.18
Nodes (9): alpha_max(), Find the maximum alpha for which there are some non-zeros off-diagonal.      Par, Fit the GraphicalLasso covariance model to X.          Parameters         ------, _oas(), Estimate covariance with the Oracle Approximating Shrinkage algorithm.      The, Estimate covariance with the Oracle Approximating Shrinkage.      Read more in t, Oracle Approximating Shrinkage Estimator.      Read more in the :ref:`User Guide, Fit the Oracle Approximating Shrinkage covariance model to X.          Parameter (+1 more)

### Community 201 - "Community 201"
Cohesion: 0.18
Nodes (5): _BaseFilter, Initialize the univariate feature selection.      Parameters     ----------, Run score function on (X, y) and get the appropriate features.          Paramete, Filter: Select the pvalues below alpha based on a FPR test.      FPR test stands, SelectFpr

### Community 202 - "Community 202"
Cohesion: 0.20
Nodes (4): asarray(), count_nonzero(), # NOTE: this is currently incorrectly typed in numpy, but will be fixed in, Array API compatibility wrapper for asarray().      See the corresponding docume

### Community 203 - "Community 203"
Cohesion: 0.18
Nodes (4): NotRequiredKwargsCallback, A callback with a `on_fit_task_end` not requiring all possible kwargs., A minimal callback used for smoke testing purposes.      This callback keeps a r, RecordingCallback

### Community 204 - "Community 204"
Cohesion: 0.24
Nodes (11): all(), any(), _axis_none_keepdims(), mean(), prod(), Implements `sum(..., axis=())` and `prod(..., axis=())`.          Works around h, _reduce_multiple_axes(), std() (+3 more)

### Community 205 - "Community 205"
Cohesion: 0.20
Nodes (8): _AutoJITWrapper, pickle_flatten(), pickle_unflatten(), Use the pickle machinery to extract objects out of an arbitrary container., Reverse of ``pickle_flatten``.      Parameters     ----------     instances : It, Helper of :func:`jax_autojit`.      Wrap arbitrary inputs and outputs of the jit, Return wrapped object., Register upon first use instead of at import time, to avoid         globally imp

### Community 206 - "Community 206"
Cohesion: 0.22
Nodes (11): check_consistent_length(), _check_method_params(), indexable(), _make_indexable(), _num_samples(), _nw_is_into_df_or_series(), Check and validate the parameters passed to a specific     method like `fit`., Return number of samples in array-like x. (+3 more)

### Community 207 - "Community 207"
Cohesion: 0.29
Nodes (9): config_context(), get_config(), _get_threadlocal_config(), Global configuration state and functions for management, Context manager to temporarily change the global scikit-learn configuration., Get a threadlocal **mutable** configuration. If the configuration     does not e, Retrieve the current scikit-learn configuration.      This reflects the effectiv, Set global scikit-learn configuration.      These settings control the behaviour (+1 more)

### Community 208 - "Community 208"
Cohesion: 0.24
Nodes (9): construct_grids(), fetch_species_distributions(), _load_coverage(), _load_csv(), ============================= Species distribution dataset =====================, Construct the map grid from the batch object      Parameters     ----------, Loader for species distribution dataset from Phillips et. al. (2006).      Read, Load a coverage file from an open file object.      This will return a numpy arr (+1 more)

### Community 209 - "Community 209"
Cohesion: 0.24
Nodes (5): BadObject, COOData, encode_string(), Error raised when the object representing the ARFF file has something     wrong., (INTERNAL) Encodes a line of data.          Data instances follow the csv format

### Community 210 - "Community 210"
Cohesion: 0.20
Nodes (5): Feature selection algorithms.  These include univariate filter selection methods, Filter: Select the p-values for an estimated false discovery rate.      This use, Filter: Select the p-values corresponding to Family-wise error rate.      Read m, SelectFdr, SelectFwe

### Community 211 - "Community 211"
Cohesion: 0.27
Nodes (5): Recursive feature elimination with cross-validation to select features.      The, Fit the RFE model and automatically tune the number of selected features., Score using the `scoring` option on the given test data and labels.          Par, Get metadata routing of this object.          Please check :ref:`User Guide <met, RFECV

### Community 212 - "Community 212"
Cohesion: 0.22
Nodes (6): Backend, Backends against which array-api-extra runs its tests., All array library backends explicitly tested by array-api-extra.      Parameters, Module name to be imported., Check if this backend uses the same module as others., Backend as a pytest parameter.          Returns         -------         pytest.m

### Community 213 - "Community 213"
Cohesion: 0.20
Nodes (7): _path_residuals(), Fit model with coordinate descent.          Parameters         ----------, Returns the MSE for the models computed by 'path'.      Parameters     ---------, Compute path with coordinate descent., Fit MultiTaskElasticNet model with coordinate descent.          Parameters, Change the order of X and y if necessary.      Parameters     ----------     X :, _set_order()

### Community 214 - "Community 214"
Cohesion: 0.22
Nodes (5): ClassicalMDS, Classical multi-dimensional scaling (classical MDS)., Compute the embedding positions.          Parameters         ----------, Compute and return the embedding positions.          Parameters         --------, Classical multidimensional scaling (MDS).      This is also known as principal c

### Community 215 - "Community 215"
Cohesion: 0.24
Nodes (5): Initialization of the mixture parameters.          Parameters         ----------, Estimate the parameters of the Dirichlet distribution.          Parameters, Estimate the parameters of the Gaussian distribution.          Parameters, Estimate the precisions parameters of the precision distribution.          Param, M step.          Parameters         ----------         X : array-like of shape (

### Community 216 - "Community 216"
Cohesion: 0.24
Nodes (5): _estimators_has(), _partial_fit_binary(), _partial_fit_ovo_binary(), _predict_binary(), _threshold_for_binary_predict()

### Community 217 - "Community 217"
Cohesion: 0.20
Nodes (5): KNeighborsClassifier, Fit the k-nearest neighbors classifier from the training dataset.          Param, Predict the class labels for the provided data.          Parameters         ----, Return the mean accuracy on the given test data and labels.          In multi-la, Classifier implementing the k-nearest neighbors vote.      Read more in the :ref

### Community 218 - "Community 218"
Cohesion: 0.20
Nodes (6): RadiusNeighborsRegressor, Nearest Neighbor Regression., Regression based on neighbors within a fixed radius.      The target is predicte, Fit the radius neighbors regressor from the training dataset.          Parameter, Predict the target for the provided data.          Parameters         ----------, RadiusNeighborsMixin

### Community 219 - "Community 219"
Cohesion: 0.20
Nodes (1): InfinityType

### Community 220 - "Community 220"
Cohesion: 0.24
Nodes (5): ConfusionMatrixDisplay, Plot visualization.          Parameters         ----------         include_value, Confusion Matrix visualization.      It is recommended to use     :func:`~sklear, Plot Confusion Matrix given an estimator and some data.          For general inf, Plot Confusion Matrix given true and predicted labels.          For general info

### Community 221 - "Community 221"
Cohesion: 0.24
Nodes (9): axis0_safe_slice(), _get_dense_mask(), _get_mask(), indices_to_mask(), Return a mask which is safer to use on X than safe_mask.      This mask is safer, Convert list of indices to boolean mask.      Parameters     ----------     indi, Compute the boolean mask X == value_to_mask.      Parameters     ----------, Return an indexing mask compatible with X.      Parameters     ----------     X (+1 more)

### Community 222 - "Community 222"
Cohesion: 0.27
Nodes (9): _get_response_values(), _get_response_values_binary(), _process_decision_function(), _process_predict_proba(), Utilities to get the response values of a classifier or a regressor.  It allows, Compute the response values of a classifier, an outlier detector, a regressor, Get the response values when the response method is `predict_proba`.      This f, Compute the response values of a binary classifier.      Parameters     -------- (+1 more)

### Community 223 - "Community 223"
Cohesion: 0.20
Nodes (5): ignore_warnings(), _IgnoreWarnings, Improved and simplified Python warnings context manager and decorator.      This, Decorator to catch and hide warnings without visual nesting., Context manager and decorator to ignore warnings.      Note: Using this (in both

### Community 224 - "Community 224"
Cohesion: 0.22
Nodes (2): MinimalClassifier, Minimal classifier implementation without inheriting from BaseEstimator.      Th

### Community 225 - "Community 225"
Cohesion: 0.31
Nodes (3): _affinity_propagation(), AffinityPropagation, _equal_similarities_and_preferences()

### Community 226 - "Community 226"
Cohesion: 0.36
Nodes (3): _class_cov(), _class_means(), _cov()

### Community 227 - "Community 227"
Cohesion: 0.22
Nodes (4): BadNominalValue, EncodedNominalConversor, NominalConversor, Error raised when a value in used in some data instance but is not     declared

### Community 228 - "Community 228"
Cohesion: 0.31
Nodes (1): HashingVectorizer

### Community 229 - "Community 229"
Cohesion: 0.33
Nodes (1): _VectorizerMixin

### Community 230 - "Community 230"
Cohesion: 0.22
Nodes (4): Feature selector that removes all low-variance features.      This feature selec, Learn empirical variances from X.          Parameters         ----------, VarianceThreshold, SelectorMixin

### Community 231 - "Community 231"
Cohesion: 0.31
Nodes (3): info(), trcg(), TRON()

### Community 232 - "Community 232"
Cohesion: 0.22
Nodes (3): _PassthroughScorer, Method that wraps estimator.score, Get requested data properties.          Please check :ref:`User Guide <metadata_

### Community 233 - "Community 233"
Cohesion: 0.25
Nodes (4): OneTimeSplitter, Common utilities for testing model selection., A wrapper to make KFold single entry cv iterator, Split can be called only once

### Community 234 - "Community 234"
Cohesion: 0.22
Nodes (4): MaxIterEstimator, ParentFitEstimator, A class that mimics the behavior of an estimator.      The iterative part uses a, A class that mimics an estimator using its parent fit method.

### Community 235 - "Community 235"
Cohesion: 0.22
Nodes (8): chunk_generator(), gen_batches(), gen_even_slices(), get_chunk_n_rows(), Calculate how many rows can be processed within `working_memory`.      Parameter, Chunk generator, ``gen`` into lists of length ``chunksize``. The last     chunk, Generator to create slices containing `batch_size` elements from 0 to `n`., Generator to create `n_packs` evenly spaced slices going up to `n`.      If `n_p

### Community 236 - "Community 236"
Cohesion: 0.22
Nodes (7): all_displays(), all_estimators(), all_functions(), Utilities to discover scikit-learn objects., Get a list of all displays from `sklearn`.      Returns     -------     displays, Get a list of all functions from `sklearn`.      Returns     -------     functio, Get a list of all estimators from `sklearn`.      This function crawls the modul

### Community 237 - "Community 237"
Cohesion: 0.22
Nodes (9): check_classifier_data_not_an_array(), check_classifiers_regression_target(), check_estimators_data_not_an_array(), check_estimators_unfitted(), check_regressor_data_not_an_array(), check_regressors_int(), check_regressors_train(), check_transformers_unfitted() (+1 more)

### Community 238 - "Community 238"
Cohesion: 0.22
Nodes (9): _check_generated_dataframe(), check_global_output_transform_pandas(), check_global_set_output_transform_polars(), _check_set_output_transform_dataframe(), check_set_output_transform_pandas(), _check_set_output_transform_pandas_context(), check_set_output_transform_polars(), _check_set_output_transform_polars_context() (+1 more)

### Community 239 - "Community 239"
Cohesion: 0.22
Nodes (5): ContainerAdapterProtocol, Create container from `X_output` with additional metadata.          Parameters, Return True if X is a supported container.          Parameters         ---------, Rename columns in `X`.          Parameters         ----------         X : contai, Stack containers horizontally (column-wise).          Parameters         -------

### Community 240 - "Community 240"
Cohesion: 0.22
Nodes (7): Wrapper used by `_SetOutputMixin` to automatically wrap methods., Mixin that dynamically wraps methods to return container based on config.      C, Set output container.          Refer to the :ref:`user guide <df_output_transfor, Safely call estimator.set_output and error if it not available.      This is use, _safe_set_output(), _SetOutputMixin, _wrap_method_output()

### Community 241 - "Community 241"
Cohesion: 0.22
Nodes (6): create_memmap_backed_data(), _delete_folder(), Utility function to cleanup a temporary folder if still existing.      Copy from, Parameters     ----------     data     mmap_mode : str, default='r', Parameters     ----------     data     mmap_mode : str, default='r'     return_f, TempMemmap

### Community 242 - "Community 242"
Cohesion: 0.22
Nodes (2): MinimalRegressor, Minimal regressor implementation without inheriting from BaseEstimator.      Thi

### Community 243 - "Community 243"
Cohesion: 0.25
Nodes (2): MinimalTransformer, Minimal transformer implementation without inheriting from     BaseEstimator.

### Community 244 - "Community 244"
Cohesion: 0.46
Nodes (7): _average_linkage(), _complete_linkage(), _fix_connectivity(), linkage_tree(), _single_linkage(), _single_linkage_tree(), ward_tree()

### Community 245 - "Community 245"
Cohesion: 0.29
Nodes (6): empirical_covariance(), log_likelihood(), Maximum likelihood covariance estimator., Compute the log-likelihood of `X_test` under the estimated Gaussian model., Compute the sample mean of the log_likelihood under a covariance model.      Com, Compute the Maximum likelihood covariance estimator.      Parameters     -------

### Community 246 - "Community 246"
Cohesion: 0.32
Nodes (7): _fetch_brute_kddcup99(), fetch_kddcup99(), _mkdirp(), KDDCUP 99 dataset.  A classic dataset for anomaly detection.  The dataset page i, Load the kddcup99 dataset, downloading it if necessary.      Parameters     ----, Ensure directory d exists (like mkdir -p on Unix)     No guarantee that the dire, Load the kddcup99 dataset (classification).      Download it if necessary.

### Community 247 - "Community 247"
Cohesion: 0.32
Nodes (7): fetch_rcv1(), _find_permutation(), _inverse_permutation(), RCV1 dataset.  The dataset page is available at      http://jmlr.csail.mit.edu/p, Load the RCV1 multilabel dataset (classification).      Download it if necessary, Inverse permutation p., Find the permutation from a to b.

### Community 248 - "Community 248"
Cohesion: 0.32
Nodes (4): _gs_decorrelation(), _ica_def(), _ica_par(), _sym_decorrelation()

### Community 249 - "Community 249"
Cohesion: 0.25
Nodes (6): _analyze(), _check_stop_list(), _preprocess(), strip_accents_ascii(), strip_accents_unicode(), strip_tags()

### Community 250 - "Community 250"
Cohesion: 0.25
Nodes (4): _clean_nans(), Fixes Issue #1240: NaNs can't be properly compared, so change them to the     sm, Select features according to a percentile of the highest scores.      Read more, SelectPercentile

### Community 251 - "Community 251"
Cohesion: 0.25
Nodes (1): AdditiveChi2Sampler

### Community 252 - "Community 252"
Cohesion: 0.25
Nodes (8): angle(), default_dtype(), nunique(), Return the default dtype for the given namespace and device.      This is a conv, Count the number of unique elements in an array.      Compatible with JAX and Da, See docstring in `array_api_extra._delegation.py`., Return the angle of the complex argument.      Parameters     ----------     z :, searchsorted()

### Community 253 - "Community 253"
Cohesion: 0.25
Nodes (8): atleast_nd(), cov(), expand_dims(), kron(), See docstring in array_api_extra._delegation., See docstring in array_api_extra._delegation., See docstring in array_api_extra._delegation., See docstring in array_api_extra._delegation.

### Community 254 - "Community 254"
Cohesion: 0.39
Nodes (3): MDS, smacof(), _smacof_single()

### Community 255 - "Community 255"
Cohesion: 0.29
Nodes (6): _log_dirichlet_norm(), _log_wishart_norm(), Bayesian Gaussian Mixture Model., Compute the log of the Dirichlet distribution normalization term.      Parameter, Compute the log of the Wishart distribution normalization term.      Parameters, Estimate the lower bound of the model.          The lower bound on the likelihoo

### Community 257 - "Community 257"
Cohesion: 0.25
Nodes (1): _BaseVersion

### Community 258 - "Community 258"
Cohesion: 0.25
Nodes (4): NotValidCallback, A minimal auto-propagated callback used for smoke testing purposes.      This ca, Invalid callback since it's missing methods from the protocol., RecordingAutoPropagatedCallback

### Community 259 - "Community 259"
Cohesion: 0.25
Nodes (8): _fix_promotion(), matmul(), result_type(), take(), take_along_axis(), tensordot(), vecdot(), where()

### Community 261 - "Community 261"
Cohesion: 0.32
Nodes (4): available_if(), _AvailableIfDescriptor, An attribute that is available only if check returns a truthy value.      Parame, Implements a conditional property using the descriptor protocol.      Using this

### Community 262 - "Community 262"
Cohesion: 0.25
Nodes (6): Check if an item is a valid string alias for a metadata.      Values in ``VALID_, Check if an item is a valid request value (and not an alias).      Parameters, Add request info for a metadata.          Parameters         ----------, Get names of all metadata that can be consumed or routed by this method., request_is_alias(), request_is_valid()

### Community 263 - "Community 263"
Cohesion: 0.32
Nodes (7): _get_deps_info(), _get_sys_info(), Utility methods to print system info for debugging  adapted from :func:`pandas.s, System information      Returns     -------     sys_info : dict         system a, Overview of the installed version of main dependencies      This function does n, Print useful debugging information.      .. versionadded:: 0.20      Examples, show_versions()

### Community 264 - "Community 264"
Cohesion: 0.25
Nodes (8): assert_docstring_consistency(), _check_consistency_items(), _check_item_included(), _get_diff_msg(), Helper to check if item should be included in checking., Get message showing the difference between type/desc docstrings of all objects., Helper to check docstring consistency of all `items_docs`.      If item is not p, r"""Check consistency between docstring parameters/attributes/returns of objects

### Community 265 - "Community 265"
Cohesion: 0.25
Nodes (8): _assert_all_finite(), _assert_all_finite_element_wise(), _check_large_sparse(), _ensure_sparse_format(), Like assert_all_finite, but only for ndarray., Raise a ValueError if X has 64bit indices and accept_large_sparse=False, Throw a ValueError if X contains NaN or infinity.      Parameters     ----------, Convert a sparse container to a given format.      Checks the sparse format of `

### Community 266 - "Community 266"
Cohesion: 0.33
Nodes (4): # TODO: use the QR wrapper once dask, # TODO: can't avoid computing U or V for dask, svd(), svdvals()

### Community 267 - "Community 267"
Cohesion: 0.29
Nodes (4): GraphicalLassoCV, Get metadata routing of this object.          Please check :ref:`User Guide <met, Sparse inverse covariance w/ cross-validated choice of the l1 penalty.      See, Methods and algorithms to robustly estimate covariance.  They estimate the covar

### Community 268 - "Community 268"
Cohesion: 0.38
Nodes (2): GenericUnivariateSelect, Univariate feature selector with configurable strategy.      Read more in the :r

### Community 269 - "Community 269"
Cohesion: 0.29
Nodes (3): _ConstantPredictor, _fit_binary(), _fit_ovo_binary()

### Community 270 - "Community 270"
Cohesion: 0.29
Nodes (2): FailingCallback, A callback that raises an error at some point.

### Community 272 - "Community 272"
Cohesion: 0.29
Nodes (7): array_device(), _bincount(), Hardware device where the array data resides on., Hardware device where the array data resides on.      If the hardware device is, Filter arrays to exclude None and/or specific types.      Sparse arrays are alwa, _remove_non_arrays(), _single_array_device()

### Community 273 - "Community 273"
Cohesion: 0.33
Nodes (7): _convert_to_numpy(), _is_xp_namespace(), _max_precision_float_dtype(), move_to(), Convert X into a NumPy ndarray on the CPU.      This function uses library-speci, Move all arrays to `xp` and `device`.      Each array will be moved to the refer, Return the float dtype with the highest precision supported by the device.

### Community 274 - "Community 274"
Cohesion: 0.29
Nodes (7): _randomized_eigsh(), randomized_svd(), Compute a truncated randomized SVD.      This method solves the fixed-rank appro, Body of randomized_svd without input validation., Computes a truncated eigendecomposition using randomized methods      This metho, Sign correction to ensure deterministic output from SVD.      Adjusts the column, svd_flip()

### Community 275 - "Community 275"
Cohesion: 0.29
Nodes (6): check_matplotlib_support(), check_pandas_support(), check_rich_support(), Raise ImportError with detailed error message if pandas is not installed.      P, Raise ImportError with detailed error message if rich is not installed.      Cal, Raise ImportError with detailed error message if mpl is not installed.      Plot

### Community 276 - "Community 276"
Cohesion: 0.29
Nodes (6): _attach_unique(), _cached_unique(), Attach unique values of y to y and return the result.      The result is a view, Attach unique values of ys to ys and return the results.      The result is a vi, Return the unique values of y.      Use the cached values from dtype.metadata if, Return the unique values of ys.      Use the cached values from dtype.metadata i

### Community 277 - "Community 277"
Cohesion: 0.33
Nodes (4): clone_module(), get_xp(), Decorator to automatically replace xp with the corresponding array module., Import everything from module, updating globals().     Returns __all__.

### Community 278 - "Community 278"
Cohesion: 0.33
Nodes (3): Private constructor to create a sub-context.          Parameters         -------, Add `child_context` as a child of this context., Create a context for a subtask of the current task.          Parameters

### Community 279 - "Community 279"
Cohesion: 0.33
Nodes (3): Configure global settings and get information about the working environment., Fixture for the tests to assure globally controllable seeding of RNGs, setup_module()

### Community 280 - "Community 280"
Cohesion: 0.40
Nodes (5): get_auto_step_size(), Solvers for Ridge and LogisticRegression using SAG algorithm, SAG solver for Ridge and LogisticRegression.      SAG stands for Stochastic Aver, Compute automatic step size for SAG solver.      The step size is set to 1 / (al, sag_solver()

### Community 281 - "Community 281"
Cohesion: 0.33
Nodes (5): _average_binary_score(), _average_multiclass_ovo_score(), Common code for all metrics., Average one-versus-one scores for multiclass classification.      Uses the binar, Average a binary metric for multilabel classification.      Parameters     -----

### Community 282 - "Community 282"
Cohesion: 0.53
Nodes (1): ClassDoc

### Community 283 - "Community 283"
Cohesion: 0.40
Nodes (5): generate_link_to_param_doc(), get_docstring(), URL to the relevant section of the docstring using a Text Fragment      https://, Extract and format docstring information for a specific item.      Parses the es, scrape_estimator_docstring()

### Community 284 - "Community 284"
Cohesion: 0.33
Nodes (6): _add_to_diagonal(), _fill_diagonal(), Validate arguments to `_fill_diagonal`/`_add_to_diagonal`., Minimal implementation of `numpy.fill_diagonal`.      `wrap` is not supported (i, Add `value` to diagonal of `array`.      Related to `fill_diagonal`. `value` sho, _validate_diagonal_args()

### Community 285 - "Community 285"
Cohesion: 0.40
Nodes (5): compute_class_weight(), compute_sample_weight(), Utilities for handling weights based on class labels., Estimate sample weights by class for unbalanced datasets.      Parameters     --, Estimate class weights for unbalanced datasets.      Parameters     ----------

### Community 286 - "Community 286"
Cohesion: 0.33
Nodes (5): _fix_connected_components(), Graph utilities and algorithms., Return the length of the shortest path from source to all reachable nodes., Add connections to sparse graph to connect unconnected components.      For each, single_source_shortest_path_length()

### Community 287 - "Community 287"
Cohesion: 0.40
Nodes (1): Resolve which estimator to return (default is LinearSVC)

### Community 288 - "Community 288"
Cohesion: 0.40
Nodes (2): Select features according to the k highest scores.      Read more in the :ref:`U, SelectKBest

### Community 289 - "Community 289"
Cohesion: 0.40
Nodes (3): Set the parameters of this kernel.          The method works on simple kernels a, Returns the (flattened, log-transformed) non-fixed hyperparameters.          Not, Sets the (flattened, log-transformed) non-fixed hyperparameters.          Parame

### Community 290 - "Community 290"
Cohesion: 0.40
Nodes (4): _find_binning_thresholds(), This module contains the BinMapper class.  BinMapper is used for mapping a real-, Extract quantiles from a continuous feature.      Missing values are ignored for, # TODO: complexity is O(n_categorical_features * 255). Maybe this is

### Community 291 - "Community 291"
Cohesion: 0.40
Nodes (4): _check_feature_names(), _get_feature_index(), Get feature index.      Parameters     ----------     fx : int or str         Fe, Check feature names.      Parameters     ----------     X : array-like of shape

### Community 292 - "Community 292"
Cohesion: 0.70
Nodes (4): _calculate_permutation_scores(), _create_importances_bunch(), permutation_importance(), _weights_scorer()

### Community 293 - "Community 293"
Cohesion: 0.40
Nodes (5): apply_where(), isclose(), Helper of `apply_where`. On Dask, this runs on a single chunk., See docstring in array_api_extra._delegation., Run one of two elementwise functions depending on a condition.      Equivalent t

### Community 294 - "Community 294"
Cohesion: 0.40
Nodes (4): _compute_log_det_cholesky(), _estimate_log_gaussian_prob(), Compute the log-det of the Cholesky decomposition of matrices.      Parameters, Estimate the log Gaussian probability.      Parameters     ----------     X : ar

### Community 295 - "Community 295"
Cohesion: 0.40
Nodes (3): Compute online update of Gaussian mean and variance.          Given starting sam, Incremental fit on a batch of samples.          This method is expected to be ca, Actual implementation of Gaussian NB fitting.          Parameters         ------

### Community 297 - "Community 297"
Cohesion: 0.50
Nodes (4): _params_html_repr(), Categorizes parameters as 'default' or 'user-set' and formats their values., Generate HTML representation of estimator parameters.      Creates an HTML table, _read_params()

### Community 298 - "Community 298"
Cohesion: 0.40
Nodes (2): NoCallbackEstimator, A class that mimics an estimator without callback support.

### Community 299 - "Community 299"
Cohesion: 0.40
Nodes (5): _average(), _find_matching_floating_dtype(), _median(), Find a suitable floating point dtype when computing with arrays.      If any of, Partial port of np.average to support the Array API.      It does a best effort

### Community 300 - "Community 300"
Cohesion: 0.40
Nodes (5): _check_array_api_core(), check_array_api_input(), check_array_api_input_and_values(), check_array_api_mixed_inputs(), check_array_api_string_and_numeric_inputs()

### Community 301 - "Community 301"
Cohesion: 0.40
Nodes (4): is_pandas_na(), is_scalar_nan(), Test if x is NaN.      This function is meant to overcome the issue that np.isna, Test if x is pandas.NA.      We intentionally do not use this function to return

### Community 302 - "Community 302"
Cohesion: 0.40
Nodes (4): Compute the weighted percentile.      Implement an array API compatible (weighte, Compute weighted percentiles for sorted 1D data and percentile ranks.      This, _weighted_percentile(), _weighted_percentile_1d_sorted()

### Community 303 - "Community 303"
Cohesion: 0.50
Nodes (4): _message_with_time(), _print_elapsed_time(), Log elapsed time to stdout when the context is exited.      Parameters     -----, Create one line message for logging purposes.      Parameters     ----------

### Community 304 - "Community 304"
Cohesion: 0.67
Nodes (3): main(), process_tempita(), Process tempita templated file and write out the result.      The template file

### Community 305 - "Community 305"
Cohesion: 0.50
Nodes (3): _get_n_samples_bootstrap(), Utility function to get the number of bootstrap samples., Get the number of samples in a bootstrap sample.      Notes     -----     The fr

### Community 306 - "Community 306"
Cohesion: 0.50
Nodes (3): get_equivalent_estimator(), This module contains utility routines., Return an unfitted estimator from another lib with matching hyperparams.      Th

### Community 307 - "Community 307"
Cohesion: 0.50
Nodes (3): Private testing utilities.  See also ..testing for public testing utilities., XFAIL the currently running test.      Unlike ``pytest.xfail``, allow rest of te, xfail()

### Community 308 - "Community 308"
Cohesion: 0.50
Nodes (4): _multiclass_roc_auc_score(), Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) \     f, Multiclass roc auc score.      Parameters     ----------     y_true : array-like, roc_auc_score()

### Community 310 - "Community 310"
Cohesion: 0.67
Nodes (3): _fitted_attr_html_repr(), Generate HTML representation of estimator fitted attributes.      Creates an HTM, _read_fitted_attr()

### Community 311 - "Community 311"
Cohesion: 0.50
Nodes (3): l1_min_c(), Determination of parameter bounds, Return the lowest bound for `C`.      The lower bound for `C` is computed such t

### Community 312 - "Community 312"
Cohesion: 0.50
Nodes (2): MetaEstimator, A class that mimics the behavior of a meta-estimator.      It has two levels of

### Community 313 - "Community 313"
Cohesion: 0.50
Nodes (2): A class that mimics the behavior of an estimator.      The iterative part uses a, WhileEstimator

### Community 314 - "Community 314"
Cohesion: 0.50
Nodes (4): _estimator_with_converted_arrays(), move_estimator_to(), Create a new estimator with converted array attributes.      All attributes that, Move estimator array attributes to the given namespace and device.      Attribut

### Community 315 - "Community 315"
Cohesion: 0.50
Nodes (4): Yield supported namespace.      This is meant to be used for testing purposes on, Yield supported namespace, device_name, dtype_name tuples for testing.      Use, yield_namespace_device_dtype_combinations(), yield_namespaces()

### Community 316 - "Community 316"
Cohesion: 0.50
Nodes (4): _incremental_mean_and_var(), This function provides array accumulator functions with a maximum floating     p, Calculate mean update and a Youngs and Cramer variance update.      If sample_we, _safe_accumulator_op()

### Community 317 - "Community 317"
Cohesion: 0.50
Nodes (3): _random_choice_csc(), Utilities for random sampling., Generate a sparse random matrix given column class distributions      Parameters

### Community 318 - "Community 318"
Cohesion: 0.50
Nodes (3): _align_api_if_sparse(), Control sparse interface based on config, Convert to sparse interface as set in config.      Input can be dense or sparse.

### Community 319 - "Community 319"
Cohesion: 0.50
Nodes (4): _check_feature_names_in(), _generate_get_feature_names_out(), Check `input_features` and generate names if needed.      Commonly used in :term, Generate feature names out for estimator using the estimator name as the prefix.

### Community 320 - "Community 320"
Cohesion: 0.50
Nodes (4): _check_feature_names(), _get_feature_names(), Get feature names from X.      Support for other (2d) data containers should pla, Set or check the `feature_names_in_` attribute of an estimator.      .. versiona

### Community 321 - "Community 321"
Cohesion: 0.50
Nodes (4): check_is_fitted(), _is_fitted(), Determine if an estimator is fitted      Parameters     ----------     estimator, Perform is_fitted validation for estimator.      Checks if the estimator is fitt

### Community 322 - "Community 322"
Cohesion: 0.50
Nodes (4): _check_n_features(), _num_features(), Set the `n_features_in_` attribute, or check against it on an estimator.      .., Return the number of features in an array-like X.      This helper function trie

### Community 323 - "Community 323"
Cohesion: 0.50
Nodes (4): check_non_negative(), _check_sample_weight(), Check if there is any negative value in an array.      Parameters     ----------, Validate sample weights.      Note that passing sample_weight=None will output a

### Community 324 - "Community 324"
Cohesion: 0.50
Nodes (4): _is_arraylike(), _is_arraylike_not_scalar(), Returns whether the input is array-like., Return True if array is array-like and not a scalar

### Community 325 - "Community 325"
Cohesion: 0.67
Nodes (1): Module to give helpful messages to the user that did not compile scikit-learn pr

### Community 326 - "Community 326"
Cohesion: 0.67
Nodes (1): Utilities to load popular datasets and artificial data generators.

### Community 327 - "Community 327"
Cohesion: 0.67
Nodes (2): Returns the (flattened, log-transformed) non-fixed hyperparameters.          Not, Sets the (flattened, log-transformed) non-fixed hyperparameters.          Parame

### Community 328 - "Community 328"
Cohesion: 0.67
Nodes (2): _features_html(), Generate HTML representation of feature names.      Creates a collapsible HTML d

### Community 329 - "Community 329"
Cohesion: 0.67
Nodes (2): NotValidFitTaskBeginCallback, Invalid callback since it has invalid keyword-only parameters.

### Community 330 - "Community 330"
Cohesion: 0.67
Nodes (2): NotValidSetupKwargOnlyCallback, Invalid callback since it has invalid kwarg-only parameters.

### Community 331 - "Community 331"
Cohesion: 0.67
Nodes (2): NotValidSetupPositionalCallback, Invalid callback since it has invalid positional parameters.

### Community 332 - "Community 332"
Cohesion: 0.67
Nodes (2): A callback with a `on_fit_task_end` hook returning True., StopFitCallback

### Community 333 - "Community 333"
Cohesion: 0.67
Nodes (3): count_nonzero(), expand_dims(), reshape()

### Community 334 - "Community 334"
Cohesion: 0.67
Nodes (2): _init_arpack_v0(), Initialize the starting vector for iteration in ARPACK functions.      Initializ

### Community 335 - "Community 335"
Cohesion: 0.67
Nodes (2): _is_deprecated(), Helper to check if func is wrapped by our deprecated decorator

### Community 336 - "Community 336"
Cohesion: 0.67
Nodes (3): _check_transformer(), check_transformer_data_not_an_array(), check_transformer_general()

### Community 337 - "Community 337"
Cohesion: 1.00
Nodes (1): NumPy Array API compatibility library  This is a small wrapper around NumPy, CuP

### Community 343 - "Community 343"
Cohesion: 1.00
Nodes (1): Distributor init file  Distributors: you can add custom code here to support par

### Community 344 - "Community 344"
Cohesion: 1.00
Nodes (1): This is now a no-op and can be safely removed from your code.  It used to enable

### Community 345 - "Community 345"
Cohesion: 1.00
Nodes (1): This is now a no-op and can be safely removed from your code.  It used to enable

### Community 346 - "Community 346"
Cohesion: 1.00
Nodes (1): Importable modules that enable the use of experimental features or estimators.

### Community 348 - "Community 348"
Cohesion: 1.00
Nodes (1): External, bundled dependencies.

### Community 349 - "Community 349"
Cohesion: 1.00
Nodes (1): This module implements histogram-based gradient boosting estimators.  The implem

### Community 350 - "Community 350"
Cohesion: 1.00
Nodes (1): Internals of array-api-extra.

### Community 351 - "Community 351"
Cohesion: 1.00
Nodes (1): All minimum dependencies for scikit-learn.

### Community 354 - "Community 354"
Cohesion: 1.00
Nodes (2): arange(), empty()

### Community 355 - "Community 355"
Cohesion: 1.00
Nodes (2): broadcast_arrays(), broadcast_to()

### Community 356 - "Community 356"
Cohesion: 1.00
Nodes (2): isdtype(), Returns a boolean indicating whether a provided dtype is of a specified data typ

### Community 357 - "Community 357"
Cohesion: 1.00
Nodes (2): _normalize_axes(), squeeze()

### Community 359 - "Community 359"
Cohesion: 1.00
Nodes (1): Decision tree based models for classification and regression.

### Community 360 - "Community 360"
Cohesion: 1.00
Nodes (2): _apply_on_subsets(), check_methods_subset_invariance()

### Community 361 - "Community 361"
Cohesion: 1.00
Nodes (2): check_regressor_multioutput(), _is_pairwise_metric()

### Community 362 - "Community 362"
Cohesion: 1.00
Nodes (2): _pandas_dtype_needs_early_conversion(), Return True if pandas extension pd_dtype need to be converted early.

## Knowledge Gaps
- **605 isolated node(s):** `Module to give helpful messages to the user that did not compile scikit-learn pr`, `Configure global settings and get information about the working environment.`, `Fixture for the tests to assure globally controllable seeding of RNGs`, `Process tempita templated file and write out the result.      The template file`, `Global configuration state and functions for management` (+600 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 69`** (2 nodes): `eye()`, `zeros()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 71`** (1 nodes): `Pipeline`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 86`** (2 nodes): `_BaseComposition`, `FeatureUnion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 94`** (2 nodes): `DensityMixin`, `BaseMixture`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 133`** (1 nodes): `LatentDirichletAllocation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 138`** (1 nodes): `Version`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 172`** (2 nodes): `TfidfTransformer`, `TfidfVectorizer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 181`** (2 nodes): `DictVectorizer`, `Feature extraction from raw data.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 188`** (2 nodes): `FactorAnalysis`, `_ortho_rotation()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 189`** (1 nodes): `KernelPCA`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (2 nodes): `_calculate_threshold()`, `SelectFromModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 194`** (2 nodes): `NegativeInfinityType`, `Vendoered from https://github.com/pypa/packaging/blob/main/packaging/_structures`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 219`** (1 nodes): `InfinityType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 224`** (2 nodes): `MinimalClassifier`, `Minimal classifier implementation without inheriting from BaseEstimator.      Th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 228`** (1 nodes): `HashingVectorizer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 229`** (1 nodes): `_VectorizerMixin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 242`** (2 nodes): `MinimalRegressor`, `Minimal regressor implementation without inheriting from BaseEstimator.      Thi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 243`** (2 nodes): `MinimalTransformer`, `Minimal transformer implementation without inheriting from     BaseEstimator.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 251`** (1 nodes): `AdditiveChi2Sampler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 257`** (1 nodes): `_BaseVersion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 268`** (2 nodes): `GenericUnivariateSelect`, `Univariate feature selector with configurable strategy.      Read more in the :r`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 270`** (2 nodes): `FailingCallback`, `A callback that raises an error at some point.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 282`** (1 nodes): `ClassDoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 287`** (1 nodes): `Resolve which estimator to return (default is LinearSVC)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 288`** (2 nodes): `Select features according to the k highest scores.      Read more in the :ref:`U`, `SelectKBest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 298`** (2 nodes): `NoCallbackEstimator`, `A class that mimics an estimator without callback support.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 312`** (2 nodes): `MetaEstimator`, `A class that mimics the behavior of a meta-estimator.      It has two levels of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 313`** (2 nodes): `A class that mimics the behavior of an estimator.      The iterative part uses a`, `WhileEstimator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 325`** (1 nodes): `Module to give helpful messages to the user that did not compile scikit-learn pr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 326`** (1 nodes): `Utilities to load popular datasets and artificial data generators.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 327`** (2 nodes): `Returns the (flattened, log-transformed) non-fixed hyperparameters.          Not`, `Sets the (flattened, log-transformed) non-fixed hyperparameters.          Parame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 328`** (2 nodes): `_features_html()`, `Generate HTML representation of feature names.      Creates a collapsible HTML d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 329`** (2 nodes): `NotValidFitTaskBeginCallback`, `Invalid callback since it has invalid keyword-only parameters.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 330`** (2 nodes): `NotValidSetupKwargOnlyCallback`, `Invalid callback since it has invalid kwarg-only parameters.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 331`** (2 nodes): `NotValidSetupPositionalCallback`, `Invalid callback since it has invalid positional parameters.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 332`** (2 nodes): `A callback with a `on_fit_task_end` hook returning True.`, `StopFitCallback`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 334`** (2 nodes): `_init_arpack_v0()`, `Initialize the starting vector for iteration in ARPACK functions.      Initializ`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 335`** (2 nodes): `_is_deprecated()`, `Helper to check if func is wrapped by our deprecated decorator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 337`** (1 nodes): `NumPy Array API compatibility library  This is a small wrapper around NumPy, CuP`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 343`** (1 nodes): `Distributor init file  Distributors: you can add custom code here to support par`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 344`** (1 nodes): `This is now a no-op and can be safely removed from your code.  It used to enable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 345`** (1 nodes): `This is now a no-op and can be safely removed from your code.  It used to enable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 346`** (1 nodes): `Importable modules that enable the use of experimental features or estimators.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 348`** (1 nodes): `External, bundled dependencies.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 349`** (1 nodes): `This module implements histogram-based gradient boosting estimators.  The implem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 350`** (1 nodes): `Internals of array-api-extra.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 351`** (1 nodes): `All minimum dependencies for scikit-learn.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 354`** (2 nodes): `arange()`, `empty()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 355`** (2 nodes): `broadcast_arrays()`, `broadcast_to()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 356`** (2 nodes): `isdtype()`, `Returns a boolean indicating whether a provided dtype is of a specified data typ`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 357`** (2 nodes): `_normalize_axes()`, `squeeze()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 359`** (1 nodes): `Decision tree based models for classification and regression.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 360`** (2 nodes): `_apply_on_subsets()`, `check_methods_subset_invariance()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 361`** (2 nodes): `check_regressor_multioutput()`, `_is_pairwise_metric()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 362`** (2 nodes): `_pandas_dtype_needs_early_conversion()`, `Return True if pandas extension pd_dtype need to be converted early.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Interval` connect `Community 4` to `Community 5`, `Community 9`, `Community 49`, `Community 225`, `Community 0`, `Community 66`, `Community 80`, `Community 29`, `Community 38`, `Community 73`, `Community 10`, `Community 145`, `Community 61`, `Community 166`, `Community 55`, `Community 1`, `Community 125`, `Community 116`, `Community 267`, `Community 200`, `Community 74`, `Community 108`, `Community 147`, `Community 18`, `Community 41`, `Community 246`, `Community 187`, `Community 58`, `Community 247`, `Community 37`, `Community 208`, `Community 179`, `Community 171`, `Community 22`, `Community 188`, `Community 2`, `Community 177`, `Community 189`, `Community 133`, `Community 53`, `Community 85`, `Community 117`, `Community 11`, `Community 15`, `Community 39`, `Community 75`, `Community 150`, `Community 228`, `Community 172`, `Community 229`, `Community 190`, `Community 155`, `Community 95`, `Community 211`, `Community 191`, `Community 201`, `Community 268`, `Community 156`, `Community 250`, `Community 288`, `Community 210`, `Community 230`, `Community 8`, `Community 7`, `Community 76`, `Community 12`, `Community 40`, `Community 251`, `Community 104`, `Community 64`, `Community 157`, `Community 59`, `Community 213`, `Community 24`, `Community 89`, `Community 20`, `Community 158`, `Community 43`, `Community 102`, `Community 151`, `Community 214`, `Community 254`, `Community 118`, `Community 159`, `Community 63`, `Community 126`, `Community 173`, `Community 17`, `Community 46`, `Community 308`, `Community 51`, `Community 94`, `Community 90`, `Community 255`, `Community 215`, `Community 3`, `Community 107`, `Community 32`, `Community 269`, `Community 14`, `Community 295`, `Community 91`, `Community 174`, `Community 111`, `Community 16`, `Community 115`, `Community 78`, `Community 98`, `Community 93`, `Community 162`, `Community 131`, `Community 34`, `Community 311`, `Community 48`, `Community 25`, `Community 26`, `Community 235`, `Community 6`, `Community 79`, `Community 316`, `Community 176`, `Community 274`, `Community 286`, `Community 103`, `Community 19`?**
  _High betweenness centrality (0.283) - this node is a cross-community bridge._
- **Why does `StrOptions` connect `Community 0` to `Community 5`, `Community 9`, `Community 144`, `Community 225`, `Community 66`, `Community 80`, `Community 29`, `Community 73`, `Community 10`, `Community 145`, `Community 61`, `Community 166`, `Community 55`, `Community 1`, `Community 116`, `Community 267`, `Community 200`, `Community 147`, `Community 18`, `Community 41`, `Community 246`, `Community 187`, `Community 58`, `Community 247`, `Community 37`, `Community 179`, `Community 171`, `Community 22`, `Community 188`, `Community 2`, `Community 189`, `Community 133`, `Community 53`, `Community 85`, `Community 117`, `Community 11`, `Community 4`, `Community 15`, `Community 39`, `Community 150`, `Community 228`, `Community 172`, `Community 229`, `Community 155`, `Community 191`, `Community 201`, `Community 268`, `Community 156`, `Community 250`, `Community 288`, `Community 210`, `Community 8`, `Community 7`, `Community 76`, `Community 12`, `Community 70`, `Community 40`, `Community 251`, `Community 64`, `Community 157`, `Community 59`, `Community 213`, `Community 24`, `Community 89`, `Community 20`, `Community 158`, `Community 43`, `Community 102`, `Community 254`, `Community 118`, `Community 159`, `Community 63`, `Community 126`, `Community 173`, `Community 17`, `Community 46`, `Community 308`, `Community 51`, `Community 21`, `Community 232`, `Community 94`, `Community 90`, `Community 255`, `Community 215`, `Community 132`, `Community 97`, `Community 183`, `Community 294`, `Community 3`, `Community 107`, `Community 32`, `Community 62`, `Community 217`, `Community 114`, `Community 91`, `Community 174`, `Community 111`, `Community 137`, `Community 218`, `Community 16`, `Community 120`, `Community 98`, `Community 93`, `Community 162`, `Community 131`, `Community 34`, `Community 311`, `Community 48`, `Community 25`, `Community 26`, `Community 285`, `Community 6`, `Community 79`, `Community 316`, `Community 176`, `Community 274`, `Community 19`?**
  _High betweenness centrality (0.227) - this node is a cross-community bridge._
- **Why does `CD_Algo` connect `Community 64` to `Community 5`, `Community 24`, `Community 1`, `Community 4`, `Community 0`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Are the 2222 inferred relationships involving `Interval` (e.g. with `_CalibratedClassifier` and `CalibratedClassifierCV`) actually correct?**
  _`Interval` has 2222 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2003 inferred relationships involving `StrOptions` (e.g. with `_CalibratedClassifier` and `CalibratedClassifierCV`) actually correct?**
  _`StrOptions` has 2003 INFERRED edges - model-reasoned connections that need verification._
- **Are the 1548 inferred relationships involving `BaseEstimator` (e.g. with `InconsistentVersionWarning` and `AttrsDict`) actually correct?**
  _`BaseEstimator` has 1548 INFERRED edges - model-reasoned connections that need verification._
- **Are the 878 inferred relationships involving `TransformerMixin` (e.g. with `InconsistentVersionWarning` and `AttrsDict`) actually correct?**
  _`TransformerMixin` has 878 INFERRED edges - model-reasoned connections that need verification._