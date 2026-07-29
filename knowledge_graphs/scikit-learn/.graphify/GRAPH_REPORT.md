# Graph Report - .  (2026-07-29)

## Corpus Check
- cluster-only mode - file stats not available

## Summary
- 18753 nodes · 49978 edges · 1043 communities detected
- Extraction: 47% EXTRACTED · 53% INFERRED · 0% AMBIGUOUS · INFERRED: 26619 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: uses: 26619 · contains: 8663 · rationale_for: 5757 · calls: 3908 · method: 3259 · inherits: 1067 · imports_from: 698 · imports: 7


## Graph Freshness
- Built from Git commit: `6f8b95a`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Interval` - 2331 edges
2. `BaseEstimator` - 2309 edges
3. `StrOptions` - 2101 edges
4. `TransformerMixin` - 1171 edges
5. `ClassifierMixin` - 1072 edges
6. `NotFittedError` - 948 edges
7. `ConvergenceWarning` - 855 edges
8. `Parallel` - 844 edges
9. `RegressorMixin` - 802 edges
10. `HasMethods` - 650 edges

## Surprising Connections (you probably didn't know these)
- `=========================== Covertype dataset benchmark ========================` --uses--> `GaussianNB`  [INFERRED]
  benchmarks/bench_covertype.py → sklearn/naive_bayes.py
- `Load the data, then cache and memmap the train/test split` --uses--> `GaussianNB`  [INFERRED]
  benchmarks/bench_covertype.py → sklearn/naive_bayes.py
- `===================================== SGDOneClassSVM benchmark =================` --uses--> `Nystroem`  [INFERRED]
  benchmarks/bench_online_ocsvm.py → sklearn/kernel_approximation.py
- `Attach a text label above each bar displaying its height.` --uses--> `Nystroem`  [INFERRED]
  benchmarks/bench_online_ocsvm.py → sklearn/kernel_approximation.py
- `Attach a text label above each bar displaying its height.` --uses--> `Nystroem`  [INFERRED]
  benchmarks/bench_online_ocsvm.py → sklearn/kernel_approximation.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.01
Nodes (408): Affinity Propagation clustering algorithm., Perform Affinity Propagation Clustering of data.      Read more in the :ref:`Use, Perform Affinity Propagation Clustering of data.      Read more in the :ref:`Use, Main affinity propagation algorithm., Fit the clustering from features, or affinity matrix.          Parameters, Predict the closest cluster each sample in X belongs to.          Parameters, Fit clustering from features/affinity matrix; return cluster labels.          Pa, Predict data using the ``centroids_`` of subclusters.          Avoid computation (+400 more)

### Community 1 - "Community 1"
Cohesion: 0.01
Nodes (446): Birch, Each node in a CFTree is called a CFNode.      The CFNode can have a maximum of, Remove a subcluster from a node and update it with the         split subclusters, Insert a new subcluster into the node., Each subcluster in a CFNode is called a CFSubcluster.      A CFSubcluster can ha, This little hack returns a densified row when iterating over a sparse     matrix, Check if a cluster is worthy enough to be merged. If         yes then merge., Return radius of the subcluster (+438 more)

### Community 2 - "Community 2"
Cohesion: 0.01
Nodes (402): DBSCAN: Density-Based Spatial Clustering of Applications with Noise, Perform DBSCAN clustering from vector array or distance matrix.      DBSCAN - De, Perform DBSCAN clustering from features, or distance matrix.          Parameters, Perform DBSCAN clustering from vector array or distance matrix.      This functi, Compute clusters from a data or distance matrix and predict labels.          Thi, OPTICS, Ordering Points To Identify the Clustering Structure (OPTICS)  These routines ex, Correct for predecessors.      Applies Algorithm 2 of [1]_.      Input parameter (+394 more)

### Community 3 - "Community 3"
Cohesion: 0.01
Nodes (389): make_column_selector, The :mod:`sklearn.compose._column_transformer` module implements utilities to wo, Transform X separately by each transformer, concatenate results.          Parame, Stacks Xs horizontally.          This allows subclasses to control the stacking, Get metadata routing of this object.          Please check :ref:`User Guide <met, Use check_array only when necessary, e.g. on lists and other non-array-likes., Return True if the column selection is empty (empty list or all-False     boolea, Construct (name, trans, column) tuples from list (+381 more)

### Community 4 - "Community 4"
Cohesion: 0.02
Nodes (266): ==================== Inductive Clustering ====================  Clustering can b, LinearRegression, LogisticRegression, Unsupervised Outlier Detection using the Local Outlier Factor (LOF).      The an, Fit the model to the training set X and return the labels.          **Not availa, Fit the local outlier factor detector from the training dataset.          Parame, Predict the labels (1 inlier, -1 outlier) of X according to LOF.          **Only, Predict the labels (1 inlier, -1 outlier) of X according to LOF.          If X i (+258 more)

### Community 5 - "Community 5"
Cohesion: 0.02
Nodes (217): AttributeError, BaseGradientBoosting, GradientBoostingClassifier, GradientBoostingRegressor, _init_raw_predictions(), Gradient Boosted Regression Trees.  This module contains methods for fitting gra, The impurity-based feature importances.          The higher, the more important, Fast partial dependence computation.          Parameters         ---------- (+209 more)

### Community 6 - "Community 6"
Cohesion: 0.03
Nodes (203): CallbackContext, Task level context for the callbacks.      This class is responsible for managin, Thread monitoring the progress of an estimator with rich based display.      The, RichProgressMonitor, Log for one run of a scoring monitor.      The recorded scores are accessed thro, ScoringMonitorLog, CallbackSupportMixin, CountVectorizer (+195 more)

### Community 7 - "Community 7"
Cohesion: 0.04
Nodes (137): ================================ Time-related feature engineering ==============, ======================= MNIST dataset benchmark =======================  Benchma, Load the data, then cache and memmap the train/test split, =========================== Random projection benchmark ========================, ====================================== Probability calibration of classifiers ==, ===================== Classifier comparison =====================  A comparison, ClassifierMixin, ClassNamePrefixFeaturesOutMixin (+129 more)

### Community 8 - "Community 8"
Cohesion: 0.01
Nodes (144): _BaseComposition, ================================================= Concatenating multiple feature, eval_and_get_f1(), ================================================ Semi-supervised Classification, Evaluate model performance and return F1 score, _cached_transform(), _fit_one(), Pipeline (+136 more)

### Community 9 - "Community 9"
Cohesion: 0.02
Nodes (108): ================================================================================, number_normalizer(), NumberNormalizingVectorizer, ================================================================ Biclustering do, Map all numeric tokens to a placeholder.      For many applications, tokens that, TfidfVectorizer, LinearSVC, ========================================================== Sample pipeline for t (+100 more)

### Community 10 - "Community 10"
Cohesion: 0.04
Nodes (144): _GeneralizedLinearRegressor, Fit a Generalized Linear Model.          Parameters         ----------         X, Compute the linear_predictor = `X @ coef_ + intercept_`.          Note that we o, Predict using GLM with feature matrix X.          Parameters         ----------, Compute D^2, the percentage of deviance explained.          D^2 is a generalizat, Regression via a penalized Generalized Linear Model (GLM).      GLMs based on a, This is only necessary because of the link and power arguments of the         Tw, BaseLink (+136 more)

### Community 11 - "Community 11"
Cohesion: 0.02
Nodes (126): _GeneralizedLinearRegressor, GammaRegressor, PoissonRegressor, # TODO: if alpha=0 check that X is not rank deficient, # NOTE: Rescaling of sample_weight:, # TODO: Adapt link to User Guide in the docstring, once, # TODO: make D^2 a score function in module metrics (and thereby get, Generalized Linear Model with a Poisson distribution.      This regressor uses t (+118 more)

### Community 12 - "Community 12"
Cohesion: 0.02
Nodes (90): _MetadataRequester, Tools for model selection, such as cross validation and hyper-parameter tuning., # TODO: remove this check once the estimator is no longer experimental., # TODO: remove this check once the estimator is no longer experimental., _BaseCurveDisplay, LearningCurveDisplay, Learning Curve visualization.      It is recommended to use     :meth:`~sklearn., Plot visualization.          Parameters         ----------         ax : matplotl (+82 more)

### Community 13 - "Community 13"
Cohesion: 0.03
Nodes (83): NaivelyCalibratedLinearSVC, LinearSVC with `predict_proba` method that naively scales     `decision_function, Min-max scale output of `decision_function` to [0, 1]., NaivelyCalibratedLinearSVC, LinearSVC with `predict_proba` method that naively scales     `decision_function, Min-max scale output of `decision_function` to [0,1]., generate_data(), plot_ellipse() (+75 more)

### Community 14 - "Community 14"
Cohesion: 0.01
Nodes (114): check_categorical_onehot(), Test that different parameters for combing 'a', and 'd' into     the infrequent, Test three levels and dropping the frequent category., Test three levels and dropping the infrequent category., Test that different parameters for combining 'a', and 'd' into     the infrequen, a' is the only frequent category, all other categories are infrequent., Test that the order of the categories provided by a user is respected., Test that the order of the categories provided by a user is respected.     In th (+106 more)

### Community 15 - "Community 15"
Cohesion: 0.03
Nodes (77): list, GroupKFold, GroupsConsumerMixin, K-fold iterator variant with non-overlapping groups.      Each group will appear, Generate indices to split data into training and test set.          Parameters, A Mixin to ``groups`` by default.      This Mixin makes the object to request ``, assert_request_is_empty(), check_recorded_metadata() (+69 more)

### Community 16 - "Community 16"
Cohesion: 0.05
Nodes (71): Ensemble-based methods for classification, regression and anomaly detection., BaseHistGradientBoosting, HistGradientBoostingClassifier, HistGradientBoostingRegressor, _patch_raw_predict(), Fast Gradient Boosting decision trees for classification and regression., Check if fitting should be early-stopped based on scorer.          Scores are co, Check if fitting should be early-stopped based on loss.          Scores are comp (+63 more)

### Community 17 - "Community 17"
Cohesion: 0.02
Nodes (88): create_mock_transformer(), DummyEstimatorParams, DummyTransf, FeatureNameSaver, FitParamT, Mult, NoInvTransf, NoTrans (+80 more)

### Community 18 - "Community 18"
Cohesion: 0.02
Nodes (46): check_cross_val_predict_binary(), check_cross_val_predict_multiclass(), check_cross_val_predict_multilabel(), check_cross_val_predict_with_method_binary(), check_cross_val_predict_with_method_multiclass(), check_cross_validate_multi_metric(), check_cross_validate_single_metric(), _check_sample_weight_common() (+38 more)

### Community 19 - "Community 19"
Cohesion: 0.02
Nodes (59): CallableEstimator, check_array_api_binary_classification_metric(), check_array_api_binary_continuous_classification_metric(), check_array_api_metric(), check_array_api_metric_pairwise(), check_array_api_multiclass_classification_metric(), check_array_api_multiclass_continuous_classification_metric(), check_array_api_multilabel_classification_metric() (+51 more)

### Community 20 - "Community 20"
Cohesion: 0.02
Nodes (70): _auc(), _average_precision(), _average_precision_slow(), check_alternative_lrap_implementation(), check_lrap_error_raised(), _dummy_metric(), _dummy_metric_no_sample_weight(), make_prediction() (+62 more)

### Community 21 - "Community 21"
Cohesion: 0.02
Nodes (29): early_stopping_monitor(), get_different_bitness_node_ndarray(), _make_dumb_dataset(), reduce_predictor_with_different_bitness(), test_binomial_error_exact_backward_compat(), test_categorical_different_order_same_model(), test_check_interaction_cst(), test_class_weights() (+21 more)

### Community 22 - "Community 22"
Cohesion: 0.02
Nodes (53): make_prediction(), Checks that confusion_matrix works with pandas nullable dtypes.      Non-regress, Check the behaviour of passing `labels` as a superset or subset of the labels., Check correct behaviour when different target types are sparse., Check the behaviour internal eps that changes depending on the input dtype., Check that log_loss raises a warning when y_proba values don't sum to 1., Test `y_pred` deprecation in favor of `y_proba` for `log_loss`., Check the behaviour of `zero_division` for f1-score.      Non-regression test fo (+45 more)

### Community 23 - "Community 23"
Cohesion: 0.02
Nodes (55): assert_is_subtree(), assert_pruning_creates_subtree(), assert_tree_equal(), check_min_weight_fraction_leaf(), check_min_weight_fraction_leaf_with_min_samples_leaf(), check_raise_error_on_1d_input(), check_sparse_input(), get_different_alignment_node_ndarray() (+47 more)

### Community 24 - "Community 24"
Cohesion: 0.02
Nodes (70): check_predictions(), _compute_class_weight_dictionary(), Test and compare solver results for unpenalized multinomial multiclass., Test that sparse and dense X gives same result for each solver., Test class_weight for LogisticRegressionCV., Compare Logistic regression with L2 regularization to glmnet, Test that 2 steps at once are the same as 2 single steps with warm start., # FIXME: SAGA on sparse data fits the intercept inaccurately with the (+62 more)

### Community 25 - "Community 25"
Cohesion: 0.04
Nodes (80): BaseCrossValidator, GroupsConsumerMixin, _aggregate_score_dicts(), _check_groups_routing_disabled(), _check_is_permutation(), cross_val_predict(), cross_val_score(), cross_validate() (+72 more)

### Community 26 - "Community 26"
Cohesion: 0.04
Nodes (54): Check transformer and fit transformer.          Create the default transformer,, Fit the model according to the given training data.          Parameters, # FIXME: a FunctionTransformer can return a 1D array even when validate, Meta-estimator to regress on a transformed target.      Useful for applying a no, Predict using the base regressor, applying inverse.          The regressor is us, Number of features seen during :term:`fit`., Get metadata routing of this object.          Please check :ref:`User Guide <met, TransformedTargetRegressor (+46 more)

### Community 27 - "Community 27"
Cohesion: 0.03
Nodes (50): autolabel(), get_minibatch(), iter_minibatches(), _not_in_sphinx(), plot_accuracy(), progress(), ====================================================== Out-of-core classificatio, Iterate over documents of the Reuters dataset.      The Reuters archive will aut (+42 more)

### Community 28 - "Community 28"
Cohesion: 0.02
Nodes (41): =================================================================== Analysis of, ============================================== Feature agglomeration vs. univari, =================================== Column Transformer with Mixed Types ========, ================================================== Column Transformer with Heter, ================================================================= Selecting dime, ========================================================= Pipelining: chaining a, ================================================================== Principal Com, =============================================== Feature transformations with ens (+33 more)

### Community 29 - "Community 29"
Cohesion: 0.03
Nodes (52): Bunch, Set key in dictionary to be deprecated with its warning message., Container object exposing keys as attributes.      Bunch objects are sometimes u, get_routing_for_object(), _manual_routing(), MetadataRequest, _MetadataRequester, process_routing() (+44 more)

### Community 30 - "Community 30"
Cohesion: 0.03
Nodes (46): _BinaryGaussianProcessClassifierLaplace, GaussianProcessClassifier, Gaussian processes classification., Fit Gaussian process classification model.          Parameters         ---------, Perform classification on an array of test vectors X.          Parameters, Return probability estimates for the test vector X.          Parameters, Returns log-marginal likelihood of theta for training data.          Parameters, Binary Gaussian process classification based on Laplace approximation.      The (+38 more)

### Community 31 - "Community 31"
Cohesion: 0.03
Nodes (44): load_data(), =========================== Covertype dataset benchmark ========================, Load the data, then cache and memmap the train/test split, ============================== Probability Calibration curves ==================, ================================================== Probability Calibration for 3, ======================================== Comparison of Calibration of Classifier, ========================================================= Hashing feature transf, =================================== Examples of Using `FrozenEstimator` ======== (+36 more)

### Community 32 - "Community 32"
Cohesion: 0.04
Nodes (54): C, DotProduct, ExpSineSquared, White kernel.      The main use-case of this kernel is as part of a sum-kernel w, Return the kernel k(X, Y) and optionally its gradient.          Parameters, Returns the diagonal of the kernel k(X, X).          The result of this method i, r"""Exp-Sine-Squared kernel (aka periodic kernel).      The ExpSineSquared kerne, Return the kernel k(X, Y) and optionally its gradient.          Parameters (+46 more)

### Community 33 - "Community 33"
Cohesion: 0.04
Nodes (32): BaseEstimator, MetaEstimatorMixin, check_metadata(), ExampleClassifier, ExampleRegressor, ExampleTransformer, MetaClassifier, MetaRegressor (+24 more)

### Community 34 - "Community 34"
Cohesion: 0.04
Nodes (77): auc(), average_precision_score(), _binary_roc_auc_score(), _check_dcg_target_type(), confusion_matrix_at_thresholds(), coverage_error(), _dcg_sample_scores(), dcg_score() (+69 more)

### Community 35 - "Community 35"
Cohesion: 0.04
Nodes (43): _BaseScorer, _cached_call(), _check_multimetric_scoring(), check_scoring(), _CurveScorer, _get_func_repr_or_name(), _get_response_method_name(), get_scorer() (+35 more)

### Community 36 - "Community 36"
Cohesion: 0.04
Nodes (76): _allclose_dense_sparse(), as_float_array(), _assert_all_finite(), _assert_all_finite_element_wise(), check_array(), _check_categorical_features(), check_consistent_length(), _check_estimator_name() (+68 more)

### Community 37 - "Community 37"
Cohesion: 0.05
Nodes (36): BaseSpectral, _bistochastic_normalize(), _check_rows_and_columns(), consensus_score(), _jaccard(), _log_normalize(), _pairwise_similarity(), Spectral biclustering algorithms. (+28 more)

### Community 38 - "Community 38"
Cohesion: 0.07
Nodes (70): array_namespace(), _check_api_version(), _check_device(), _cls_to_namespace(), _ClsToXPInfo, _compat_module_name(), _cupy_to_device(), _dask_device (+62 more)

### Community 39 - "Community 39"
Cohesion: 0.03
Nodes (10): test_countvectorizer_custom_token_pattern(), test_countvectorizer_custom_token_pattern_with_several_group(), test_countvectorizer_sort_features_64bit_sparse_indices(), test_hashing_vectorizer_requires_fit_tag(), test_hashing_vectorizer_transform_without_fit(), test_pickling_built_processors(), test_tf_transformer_feature_names_out(), test_tfidf_transformer_copy() (+2 more)

### Community 40 - "Community 40"
Cohesion: 0.03
Nodes (18): DEFAULT_JOBLIB_BACKEND, MyBackend, test_balance_property_random_forest(), test_classification_toy(), test_classifier_error_oob_score_multiclass_multioutput(), test_estimators_samples(), test_forest_classifier_oob(), test_forest_multioutput_integral_regression_target() (+10 more)

### Community 41 - "Community 41"
Cohesion: 0.03
Nodes (3): # NOTE: for such a small sample size, what we expect in the third column, # TODO: replace this torch/MPS-specific coverage by array-api-strict once, # TODO: replace this torch/MPS-specific coverage by array-api-strict once

### Community 42 - "Community 42"
Cohesion: 0.04
Nodes (50): ===================================== Multi-class AdaBoosted Decision Trees ====, _mean_frequency_by_risk_group(), Score an estimator on the test set., Compare predictions and observations for bins ordered by y_pred.      We order t, score_estimator(), load_mtpl2(), plot_obs_pred(), Evaluate an estimator on train and test sets with different metrics (+42 more)

### Community 43 - "Community 43"
Cohesion: 0.03
Nodes (71): PositiveSpectrumWarning, Warning raised when the eigenvalues of a PSD matrix have issues      This warnin, Test that `check_consistent_length` raises on inconsistent lengths and wrong, Test that check_consistent_length works with different array types., Check that pandas.DataFrame with bool return a boolean arrays., Check that pandas.DataFrame with boolean return a float array with dtype=None, Tests the _estimator_has function by verifying:     - Functionality with default, Test _num_samples on different non standard input X. (+63 more)

### Community 44 - "Community 44"
Cohesion: 0.05
Nodes (27): ConsumingClassifierWithOnlyPredict, ConsumingClassifierWithoutPredictLogProba, ConsumingClassifierWithoutPredictProba, ConsumingClassifier without a predict_proba method, but with predict_log_proba., ConsumingClassifier without a predict_log_proba method, but with predict_proba., ConsumingClassifier with only a predict method.      Used to mimic dynamic metho, DummySizeEstimator, EstimatorAcceptingSampleWeight (+19 more)

### Community 45 - "Community 45"
Cohesion: 0.03
Nodes (13): _mock_urlretrieve(), # TODO: replace this torch/MPS-specific coverage by array-api-strict once, test_clone_keeps_output_config(), test_estimator_empty_instance_dict(), test_estimator_getstate_using_slots_error_message(), test_fetch_file_using_data_home(), test_fetch_file_with_sha256(), test_fetch_file_without_sha256() (+5 more)

### Community 46 - "Community 46"
Cohesion: 0.03
Nodes (1): # TODO: remove mark once loky bug is fixed:

### Community 47 - "Community 47"
Cohesion: 0.04
Nodes (37): ABC, _average_linkage(), _complete_linkage(), _fix_connectivity(), linkage_tree(), _single_linkage(), _single_linkage_tree(), ward_tree() (+29 more)

### Community 48 - "Community 48"
Cohesion: 0.04
Nodes (45): estimate_bandwidth(), get_bin_seeds(), mean_shift(), MeanShift, Mean shift clustering algorithm.  Mean shift clustering aims to discover *blobs*, Perform mean shift clustering of data using a flat kernel.      Read more in the, Find seeds for mean_shift.      Finds seeds by first binning data onto a grid wh, Mean shift clustering using a flat kernel.      Mean shift clustering aims to di (+37 more)

### Community 49 - "Community 49"
Cohesion: 0.07
Nodes (20): BaseSGDClassifier, BaseSGDRegressor, PassiveAggressiveClassifier, PassiveAggressiveRegressor, Passive Aggressive Classifier.      .. deprecated:: 1.8         The whole class, Fit linear model with Passive Aggressive algorithm.          Parameters, Fit linear model with Passive Aggressive algorithm.          Parameters, Passive Aggressive Regressor.      .. deprecated:: 1.8         The whole class ` (+12 more)

### Community 50 - "Community 50"
Cohesion: 0.03
Nodes (1): Test the split module

### Community 51 - "Community 51"
Cohesion: 0.05
Nodes (32): all(), any(), arange(), _axis_none_keepdims(), broadcast_arrays(), broadcast_to(), count_nonzero(), empty() (+24 more)

### Community 52 - "Community 52"
Cohesion: 0.03
Nodes (30): plot_gallery(), ===================================================================== Faces reco, Plot a gallery of portraits., load_data(), autolabel_auc(), autolabel_time(), print_outlier_ratio(), ===================================== SGDOneClassSVM benchmark ================= (+22 more)

### Community 53 - "Community 53"
Cohesion: 0.03
Nodes (6): test_constant_int_target(), test_multiclass_estimator_attribute_error(), test_ovo_consistent_binary_classification(), test_ovr_single_label_predict_proba_zero(), test_ovr_ties(), test_pairwise_n_features_in()

### Community 54 - "Community 54"
Cohesion: 0.03
Nodes (6): # TODO: remove when NearestNeighbors methods uses parameter validation mechanism, # TODO: Remove ignore_warnings when minimum supported SciPy version is 1.17, # TODO: remove mark once loky bug is fixed:, # TODO: Remove ignore_warnings when minimum supported SciPy version is 1.17, # TODO: if score is refactored to evaluate models for other scoring, # TODO: also test radius_neighbors, but requires different assertion

### Community 56 - "Community 56"
Cohesion: 0.05
Nodes (40): _calculate_precisions(), generate_data(), _naive_lmvnpdf_diag(), RandomData, `GaussianMixture`'s best_parameters, `n_iter_` and `lower_bound_`     must be se, Check that we properly initialize `precision_cholesky_` when we manually     pro, Randomly generate samples and responsibilities., Calculate precision matrix of X and its Cholesky decomposition     for the given (+32 more)

### Community 57 - "Community 57"
Cohesion: 0.06
Nodes (55): check_all_zero_sample_weights_error(), check_array_api_same_namespace(), check_classifier_multioutput(), check_classifiers_multilabel_output_format_decision_function(), check_classifiers_multilabel_output_format_predict(), check_classifiers_multilabel_output_format_predict_proba(), check_classifiers_multilabel_representation_invariance(), check_classifiers_one_label() (+47 more)

### Community 58 - "Community 58"
Cohesion: 0.04
Nodes (26): _approx_fprime(), _check_length_scale(), Hyperparameter, Matern, NormalizedKernelMixin, PairwiseKernel, A set of kernels that can be combined by operators and used in Gaussian processe, Returns a list of all hyperparameter. (+18 more)

### Community 59 - "Community 59"
Cohesion: 0.06
Nodes (47): RandomForestClassifier, FixedImportanceEstimator, NaNTag, NaNTagRandomForest, NoNaNTag, Check max_features_ and output shape for integer max_features., Check max_features_ and output shape for callable max_features., Tests that the callable passed to `fit` is called on X. (+39 more)

### Community 60 - "Community 60"
Cohesion: 0.07
Nodes (39): be_shrunk(), check_probability_model(), check_regression_model(), clone(), cross_validation(), free_and_destroy_model(), free_model_content(), fun() (+31 more)

### Community 61 - "Community 61"
Cohesion: 0.05
Nodes (27): KernelRidge, Check that the representation of an empty Pipeline does not fail.      Non-regre, Check that repr fallback is in the HTML., Show arrow in pipeline for top level in pipeline, Invalidate stacking configuration uses default repr.      Non-regression test fo, Check HTML repr works where a value in get_params is a class., Check that we have the information that the estimator is fitted or not in the, Check the behaviour of the `_HTMLDocumentationLinkMixin` class for scikit-learn (+19 more)

### Community 62 - "Community 62"
Cohesion: 0.04
Nodes (5): # TODO: remove mark once loky bug is fixed:, # TODO: remove mark once loky bug is fixed:, # TODO: remove mark once loky bug is fixed:, # TODO: remove mark once loky bug is fixed:, # TODO: remove mark once loky bug is fixed:

### Community 63 - "Community 63"
Cohesion: 0.04
Nodes (2): _test_warm_start(), test_warm_start_multiclass()

### Community 64 - "Community 64"
Cohesion: 0.04
Nodes (5): # TODO: widening the range of alphas causes failures in the test, in, # FIXME: `assert_allclose(model.coef_, coef)` should work for all cases but fail, # FIXME: Note that this is NOT the minimum norm solution., # FIXME: Same as in test_ridge_regression_unpenalized., # FIXME: Same as in test_ridge_regression_unpenalized.

### Community 65 - "Community 65"
Cohesion: 0.05
Nodes (21): _check_precomputed_gram_matrix(), LinearModel, LinearRegression, make_dataset(), MultiOutputLinearModel, _pre_fit(), _preprocess_data(), _rescale_data() (+13 more)

### Community 66 - "Community 66"
Cohesion: 0.04
Nodes (5): Testing for Support Vector Machine module (sklearn.svm)  TODO: remove hard coded, # TODO: rework this test to be independent of the random seeds., # TODO: rework this test to be independent of the random seeds., # TODO: rework this test to be independent of the random seeds., # TODO: investigate why assertion on L148 fails.

### Community 67 - "Community 67"
Cohesion: 0.05
Nodes (37): check_memmap(), check_warnings_as_errors(), f_bad_order(), f_bad_sections(), f_check_param_definition(), f_five(), f_four(), f_missing() (+29 more)

### Community 69 - "Community 69"
Cohesion: 0.04
Nodes (13): _assert_same_lars_path_result(), # TODO: remove warning filter when numpy min version >= 2.0.0, # TODO: remove warning filter when numpy min version >= 2.0.0, # TODO: use another dataset that has multiple drops, Test that user input regarding copy_X is not being overridden (it was until, Test that user input to .fit for copy_X overrides default __init__ value, Check that we properly compute the AIC and BIC score.      In this test, we repr, Check the behaviour when `n_samples` < `n_features` and that one needs     to pr (+5 more)

### Community 70 - "Community 70"
Cohesion: 0.06
Nodes (31): fit_single(), _predict_proba(), Benchmarks of sklearn SAGA vs lightning SAGA vs Liblinear. Shows the gain in usi, Predict proba for lightning for n_classes >=3., ====================================================================== Decision, ==================================================== Multiclass sparse logistic, plot_hyperplane(), plot_subfigure() (+23 more)

### Community 71 - "Community 71"
Cohesion: 0.05
Nodes (19): _compute_gradient_3d(), _compute_n_patches(), _extract_patches(), extract_patches_2d(), grid_to_graph(), img_to_graph(), _make_edges_3d(), _mask_edges_weights() (+11 more)

### Community 72 - "Community 72"
Cohesion: 0.09
Nodes (37): be_shrunk(), Cache, calculate_rho(), clone(), do_shrinking(), dot(), get_data(), info() (+29 more)

### Community 73 - "Community 73"
Cohesion: 0.04
Nodes (10): Test isotonic regression fit, transform  and fit_transform     against the "seco, Non-regression test to handle issue 9432:     https://github.com/scikit-learn/sc, Check that calling fitting function of isotonic regression will not     overwrit, Check `get_feature_names_out` for `IsotonicRegression`., Check that `predict` does return the expected output type.      We need to check, test_get_feature_names_out(), test_isotonic_regression_output_predict(), test_isotonic_regression_sample_weight_not_overwritten() (+2 more)

### Community 74 - "Community 74"
Cohesion: 0.04
Nodes (44): Test that Kernel PCA produces deterministic output      Tests that the same inpu, Test that kPCA works on a sparse data input.      Same test as ``test_kernel_pca, Test that kPCA with linear kernel is equivalent to PCA for all solvers.      Ker, Test that `n_components` is correctly taken into account for projections      Fo, Check that the ``remove_zero_eig`` parameter works correctly.      Tests that th, Non-regression test for issue #12141 (PR #12143)      This test checks that fit(, Nominal test for all solvers and all known kernels + a custom one      It tests, Test that kPCA works with a precomputed kernel, for all solvers (+36 more)

### Community 75 - "Community 75"
Cohesion: 0.04
Nodes (10): _beta_divergence_dense(), Smoke test NMF with all inits, solvers on tall/wide arrays., Compute the beta-divergence of X and W.H for dense array only.      Used as a re, Check that an error is raised if beta_loss < 0 and X contains zeros., Check feature names out for NMF., # TODO: use the provided W when init="custom"., test_beta_divergence(), test_feature_names_out() (+2 more)

### Community 76 - "Community 76"
Cohesion: 0.08
Nodes (37): MockClassifier, Testing Recursive feature elimination, Dummy classifier to test recursive feature elimination, Check that RFE works with pipeline that accept nans.      Non-regression test fo, Check the behaviour of RFE with PLS estimators.      Non-regression test for:, Check that we raise the proper AttributeError when the estimator     does not im, Check if the correct warning is raised when trying to initialize a RFE     objec, Test that `RFE` works correctly with sample weights. (+29 more)

### Community 77 - "Community 77"
Cohesion: 0.06
Nodes (23): clip(), cumulative_prod(), cumulative_sum(), empty(), iinfo(), isdtype(), ones(), These are functions that are just aliases of existing functions in NumPy. (+15 more)

### Community 78 - "Community 78"
Cohesion: 0.05
Nodes (44): _generate_hypercube(), make_biclusters(), make_blobs(), make_checkerboard(), make_circles(), make_classification(), make_friedman1(), make_friedman2() (+36 more)

### Community 79 - "Community 79"
Cohesion: 0.06
Nodes (24): DummyRegressor, _check_shifted_by_one(), _check_standard_scaled(), DummyCheckerArrayTransformer, DummyCheckerListRegressor, DummyRegressorWithExtraFitParams, DummyRegressorWithExtraPredictParams, DummyTransformer (+16 more)

### Community 80 - "Community 80"
Cohesion: 0.06
Nodes (16): _check_behavior_2d(), _check_behavior_2d_for_constant(), _check_equality_regressor(), _check_predict_proba(), test_constant_strategy(), test_constant_strategy_multioutput(), test_constant_strategy_multioutput_regressor(), test_mean_strategy_multioutput_regressor() (+8 more)

### Community 81 - "Community 81"
Cohesion: 0.08
Nodes (5): Models based on neural networks., BaseMultilayerPerceptron, MLPClassifier, _pack(), BernoulliRBM

### Community 82 - "Community 82"
Cohesion: 0.05
Nodes (10): Make sure sklearn.utils.extmath._approximate_mode returns valid     results for, Test that `_randomized_eigsh` returns the appropriate components, Check that `_randomized_eigsh` is similar to other `eigsh`      Tests that for a, Check that randomized_eigsh is able to reconstruct a low rank psd matrix      Te, Check that the cartesian product works with mixed types., test_approximate_mode(), test_cartesian_mix_types(), test_randomized_eigsh() (+2 more)

### Community 83 - "Community 83"
Cohesion: 0.06
Nodes (26): BaseLibSVM, BaseSVC, OutlierMixin, LinearSVC, LinearSVR, NuSVC, NuSVR, OneClassSVM (+18 more)

### Community 84 - "Community 84"
Cohesion: 0.05
Nodes (16): assert_best_scores_kept(), Todo: cross-check the F-value with stats model, Check support for unsupervised feature selection for the filter that could     r, Check the behaviour of `force_finite` for some corner cases with `r_regression`., Check the behaviour of `force_finite` for some corner cases with `f_regression`., Check that the output datafarme dtypes are the same as the input.      Non-regre, test_dataframe_output_dtypes(), test_f_regression_corner_case() (+8 more)

### Community 85 - "Community 85"
Cohesion: 0.06
Nodes (33): custom_values_helper(), Check that the PD limit on the plots are properly set on one-way plots., Check that the PD limit on the plots are properly set on two-way plots., Check that we can provide a list of strings to kind parameter., Check that we raise an informative error when 2-way PD is requested     together, Check that passing `pd_line_kw` and `ice_lines_kw` will act on the     specific, Check that we raise an error when `kind` is a list with a wrong length.      Thi, Check that we properly center ICE and PD when passing kind as a string and as a (+25 more)

### Community 86 - "Community 86"
Cohesion: 0.07
Nodes (41): clear_data_home(), _convert_data_dataframe(), _derive_folder_and_filename_from_url(), fetch_file(), _fetch_remote(), _filter_filename(), get_data_home(), load_breast_cancer() (+33 more)

### Community 87 - "Community 87"
Cohesion: 0.05
Nodes (38): _check_pos_label_statistics(), Check correct error raised when only binary classification supported., Check that we raise an error with regressor., Check error raised when `response_method` not defined for `estimator`., Check passing `name` in `plot` overwrites name passed in `from_*` method., # TODO: Clean-up once `estimator_name` deprecated in all displays, Check correct error raised when `estimator` is not fitted., # TODO: Clean-up once `estimator_name` deprecated in all displays (+30 more)

### Community 88 - "Community 88"
Cohesion: 0.05
Nodes (15): assess_same_labelling(), Several basic tests for hierarchical clustering procedures, AgglomerativeClustering must work on mem-mapped dataset.      Non-regression tes, Util for comparison with scipy, The MST-LINKAGE-CORE algorithm must work on mem-mapped dataset.      Non-regress, Check that connecting components works when connectivity and     affinity are bo, Check that we raise an error when 'euclidean' or 'l2' are not passed with     wa, Check that we can pass 'euclidean' and 'l2' as metric with Ward linkage. (+7 more)

### Community 89 - "Community 89"
Cohesion: 0.06
Nodes (13): generate_multilabel_dataset_with_correlations(), test_base_chain_crossval_fit_and_predict(), test_base_chain_fit_and_predict_with_sparse_data_and_cv(), test_base_chain_random_order(), test_classifier_chain_fit_and_predict(), test_classifier_chain_fit_and_predict_with_linear_svc(), test_classifier_chain_fit_and_predict_with_sparse_data(), test_classifier_chain_vs_independent_models() (+5 more)

### Community 90 - "Community 90"
Cohesion: 0.05
Nodes (2): # TODO: explain what this is testing, # TODO: explain what this is testing

### Community 91 - "Community 91"
Cohesion: 0.05
Nodes (40): _approximate_mode(), cartesian(), density(), _deterministic_vector_sign_flip(), fast_logdet(), _incremental_mean_and_var(), make_nonnegative(), _nanaverage() (+32 more)

### Community 92 - "Community 92"
Cohesion: 0.06
Nodes (32): _ensure_sparse_index_int32(), _in_unstable_openblas_configuration(), _min_or_max_axis(), _minor_reduce(), _preserve_dia_indices_dtype(), Compatibility fixes for older version of the dependencies  If you add content to, # TODO: Adapt when Pandas > 2.2 is the minimum supported version, # TODO: remove when SciPy 1.12 is the minimum supported version (+24 more)

### Community 93 - "Community 93"
Cohesion: 0.08
Nodes (19): A variety of linear models., _check_copy_and_writeable(), Lars, lars_path(), lars_path_gram(), _lars_path_residues(), _lars_path_solver(), LarsCV (+11 more)

### Community 94 - "Community 94"
Cohesion: 0.08
Nodes (39): _assemble_fraction_of_explained_deviance(), _check_reg_targets(), _check_reg_targets_with_floating_dtype(), d2_absolute_error_score(), d2_pinball_score(), d2_tweedie_score(), explained_variance_score(), max_error() (+31 more)

### Community 95 - "Community 95"
Cohesion: 0.05
Nodes (8): Check _safe_indexing for polars as expected., Check that we raise a ValueError when axis=1 with input as list., Check that `_safe_assign` works as expected., Check _get_column_indices for edge cases with 2d input X., test_get_column_indices_dataframes(), test_polars_indexing(), test_safe_assign(), test_safe_indexing_list_axis_1_unsupported()

### Community 96 - "Community 96"
Cohesion: 0.06
Nodes (28): check_class_weight_balanced_linear_classifier(), check_classifier_not_supporting_multiclass(), check_classifiers_classes(), check_classifiers_one_label_sample_weights(), check_classifiers_predictions(), check_clusterer_compute_labels_predict(), check_do_not_raise_errors_in_init_or_set_params(), check_dont_overwrite_parameters() (+20 more)

### Community 97 - "Community 97"
Cohesion: 0.08
Nodes (15): Feature selection algorithms.  These include univariate filter selection methods, _BaseFilter, chi2(), _chisquare(), _clean_nans(), f_classif(), f_oneway(), f_regression() (+7 more)

### Community 98 - "Community 98"
Cohesion: 0.09
Nodes (27): _check_precomputed(), _get_weights(), _is_sorted_by_data(), _kneighbors_from_graph(), KNeighborsMixin, NeighborsBase, _radius_neighbors_from_graph(), RadiusNeighborsMixin (+19 more)

### Community 99 - "Community 99"
Cohesion: 0.06
Nodes (17): get_random_integer_x_three_classes_y(), get_random_normal_x_binary_y(), test_categoricalnb(), test_check_alpha(), test_discretenb_prior(), test_gnb_array_api_compliance(), test_gnb_check_update_with_no_data(), test_gnb_neg_priors() (+9 more)

### Community 100 - "Community 100"
Cohesion: 0.06
Nodes (29): assert_matrix_orthogonal(), _generate_test_scale_and_stability_datasets(), Generate dataset for test_scale_and_stability, scale=True is equivalent to scale=False on centered/scaled data     This allows, Check the validation of `n_components` upper bounds for `PLS` regressors., Check the validation of `n_components` upper bounds for PLSRegression., Test that CCA converges. Non-regression test for #19549., Checks warning when y is constant. Non-regression test for #19831 (+21 more)

### Community 101 - "Community 101"
Cohesion: 0.08
Nodes (38): count_nonzero(), csc_median_axis_0(), _get_elem_at_rank(), _get_median(), _implicit_column_offset(), incr_mean_variance_axis(), inplace_column_scale(), inplace_csr_column_scale() (+30 more)

### Community 102 - "Community 102"
Cohesion: 0.08
Nodes (6): BaseLibSVM, BaseSVC, _fit_liblinear(), _get_liblinear_solver_type(), _one_vs_one_coef(), Perform regression on samples in X.          For a one-class model, +1 (inlier)

### Community 103 - "Community 103"
Cohesion: 0.05
Nodes (4): Test the ColumnTransformer., # TODO: remove mark once loky bug is fixed:, Test that the right error is raised when metadata is not requested., test_metadata_routing_error_for_column_transformer()

### Community 104 - "Community 104"
Cohesion: 0.07
Nodes (29): assert_compatible_argkmin_results(), assert_compatible_radius_results(), assert_no_missing_neighbors(), assert_same_distances_for_common_neighbors(), _get_metric_params_list(), _non_trivial_radius(), Check that results do not depend on the chunk size., Compare the indices of neighbors in two results sets.      Any neighbor index wi (+21 more)

### Community 105 - "Community 105"
Cohesion: 0.11
Nodes (34): additive_chi2_kernel(), _check_chunk_size(), check_paired_arrays(), check_pairwise_arrays(), chi2_kernel(), cosine_distances(), cosine_similarity(), distance_metrics() (+26 more)

### Community 106 - "Community 106"
Cohesion: 0.08
Nodes (18): _inverse_binarize_multiclass(), _inverse_binarize_thresholding(), label_binarize(), LabelBinarizer, LabelEncoder, MultiLabelBinarizer, Checks that LabelBinarizer works with pandas nullable dtypes.      Non-regressio, Test that :class:`LabelBinarizer` works correctly with the array API for binary (+10 more)

### Community 107 - "Community 107"
Cohesion: 0.06
Nodes (35): argpartition(), atleast_nd(), broadcast_shapes(), cov(), create_diagonal(), expand_dims(), isclose(), isin() (+27 more)

### Community 108 - "Community 108"
Cohesion: 0.10
Nodes (6): _check_X(), ColumnTransformer, _get_transformer_list(), _is_empty_column_selection(), make_column_transformer(), Meta-estimators for building composite models with transformers.  In addition to

### Community 109 - "Community 109"
Cohesion: 0.10
Nodes (27): DummyClassifier, FastClassifier, Dummy classifier that accepts parameters a, b, ... z.      These parameter don't, Check that we raise an error if the minimum resources is set to 0., Check the selection strategy of the halving search., Check trimming cv_results_ to the last halving iteration., Check that NaN scores share the lowest rank in the last iteration., Check the behaviour of the `HalvingRandomSearchCV` with `param_distribution` (+19 more)

### Community 110 - "Community 110"
Cohesion: 0.06
Nodes (1): Testing for Multi-layer Perceptron module (sklearn.neural_network)

### Community 111 - "Community 111"
Cohesion: 0.06
Nodes (31): Check `_validate_from_predictions_params` returns the correct values., Check parameter validation is performed correctly., Check `_get_legend_label` returns the correct label., # TODO: Remove once kwargs deprecated on all displays, Check `_validate_curve_kwargs` deprecates kwargs correctly., Check `_validate_plot_params` returns the correct values., Check `_validate_curve_kwargs` performs parameter validation correctly., Check `_validate_curve_kwargs` returns correct kwargs for single legend entry. (+23 more)

### Community 112 - "Community 112"
Cohesion: 0.06
Nodes (4): Test that make_classification returns a Bunch when return_X_y is False.      Als, Test the construction of informative features in make_classification      Also t, test_make_classification_informative_features(), test_make_classification_return_x_y()

### Community 113 - "Community 113"
Cohesion: 0.08
Nodes (23): _load_svmlight_local_test_file(), load large libsvm / svmlight file with qid attribute. Tests 64-bit query ID, Helper to load resource `filename` with `importlib.resources`, Ensure that if y contains explicit zeros (i.e. elements of y.data equal to     0, Ensure that there is no ValueError when dumping a read-only `X`.      Non-regres, _svmlight_local_test_file_path(), test_dump(), test_dump_comment() (+15 more)

### Community 114 - "Community 114"
Cohesion: 0.06
Nodes (3): # NOTE: it's probably not valid from a mathematical point of view to use the, # TODO: re-enable this test if/when `manhattan_distances` is refactored to, # TODO: compare results on dense and sparse data as proposed in:

### Community 115 - "Community 115"
Cohesion: 0.08
Nodes (12): KMeansBenchmark, MiniBatchKMeansBenchmark, Benchmarks for MiniBatchKMeans., Benchmarks for KMeans., Abstract base class for benchmarks of estimators implementing transform, Transformer, DictionaryLearningBenchmark, MiniBatchDictionaryLearningBenchmark (+4 more)

### Community 116 - "Community 116"
Cohesion: 0.06
Nodes (17): KernelOperator, Product, Base class for all kernel operators.      .. versionadded:: 0.18, Get parameters of this kernel.          Parameters         ----------         de, Returns a list of all hyperparameter., Returns the (flattened, log-transformed) non-fixed hyperparameters.          Not, Sets the (flattened, log-transformed) non-fixed hyperparameters.          Parame, Returns the log-transformed bounds on the theta.          Returns         ------ (+9 more)

### Community 117 - "Community 117"
Cohesion: 0.06
Nodes (22): _make_func(), Check that `FunctionTransformer.check_inverse` raises error on mixed dtype., Check support for dataframes with only numerical values., Check error is raised when check_inverse=True.      Non-regression test for gh-2, Test that function transformer does not reset estimator in     `inverse_transfor, Check that get_feature_names_out works with DataFrames with string data., Check behavior of set_output with different settings., Check that we have a consistence between the feature names out of     `FunctionT (+14 more)

### Community 118 - "Community 118"
Cohesion: 0.06
Nodes (8): centered_matrices(), Test that sparse_matmul_to_dense raises when it should., Test that sparse_matmul_to_dense computes correctly., Check that we raise proper error when axis=1 and the dimension mismatch.     Non, Returns equivalent tuple[sp.linalg.LinearOperator, np.ndarray]., test_incr_mean_variance_axis_dim_mismatch(), test_sparse_matmul_to_dense(), test_sparse_matmul_to_dense_raises()

### Community 119 - "Community 119"
Cohesion: 0.06
Nodes (34): Check `weighted_percentile` with all weights equal to 0 returns `np.nan`., Check leading, trailing and middle 0 weights behave correctly.      Check that l, Check zero weights just before `max_index` handled correctly., Check integer weights give the same result as repeating values., Check multiplying weights by a constant does not change the result.      Note sc, Check sorted 1D helper against `_weighted_percentile`., Ensure `_weighted_percentile` matches `median` when expected.      With unit `sa, Check `_weighted_percentile` behaviour is correct when `array` is 2D. (+26 more)

### Community 120 - "Community 120"
Cohesion: 0.06
Nodes (6): Check that large amount of data will not lead to overflow in     `adjusted_rand_, Check that nmi returns a score between 0 (included) and 1 (excluded     for non-, test_adjusted_rand_score_overflow(), test_adjustment_for_chance(), test_normalized_mutual_info_score_bounded(), uniform_labelings_scores()

### Community 121 - "Community 121"
Cohesion: 0.09
Nodes (30): _as_numpy_array(), assert_close(), assert_close_nulp(), assert_equal(), assert_less(), _check_ns_shape_dtype(), _clone_function(), _CountingDaskScheduler (+22 more)

### Community 122 - "Community 122"
Cohesion: 0.08
Nodes (16): GenericKernelMixin, Mixin for kernels which are stationary: k(X, Y)= f(X-Y).      .. versionadded::, Returns whether the kernel is stationary., Mixin for kernels which operate on generic objects such as variable-     length, Whether the kernel works only on fixed-length feature vectors., StationaryKernelMixin, ========================================================================== Gauss, A minimal (but valid) convolutional kernel for sequences of variable     lengths (+8 more)

### Community 123 - "Community 123"
Cohesion: 0.07
Nodes (24): ArgKmin, ArgKminClassMode, BaseDistancesReductionDispatcher, RadiusNeighbors, RadiusNeighborsClassMode, # FIXME: the current Cython implementation is too slow for a large number of, # TODO: support CSR matrices without non-zeros elements, # TODO: support CSR matrices with int64 indices and indptr (+16 more)

### Community 124 - "Community 124"
Cohesion: 0.06
Nodes (28): Testing for Isolation Forest algorithm (sklearn.ensemble.iforest)., Check parallel regression., Test Isolation Forest performs well, Test iterative addition of iTrees to an iForest, Test whether iforest predicts inliers when using uniform data, Check that Isolation Forest does not segfault with n_jobs=2      Non-regression, Check that feature names are preserved when contamination is not "auto".      Fe, Check Isolation Forest for various parameter settings. (+20 more)

### Community 125 - "Community 125"
Cohesion: 0.11
Nodes (32): adjusted_mutual_info_score(), adjusted_rand_score(), check_clusterings(), completeness_score(), contingency_matrix(), _entropy(), fowlkes_mallows_score(), _generalized_average() (+24 more)

### Community 126 - "Community 126"
Cohesion: 0.06
Nodes (18): fit_and_score(), load_mnist(), ============================================= Early stopping of Stochastic Gradi, Load MNIST, select two classes, shuffle and return only n_samples., Fit the estimator on the train set and score it on both sets, get_auto_step_size(), Solvers for Ridge and LogisticRegression using SAG algorithm, SAG solver for Ridge and LogisticRegression.      SAG stands for Stochastic Aver (+10 more)

### Community 127 - "Community 127"
Cohesion: 0.09
Nodes (12): add_dummy_feature(), _handle_zeros_in_scale(), _is_constant_feature(), maxabs_scale(), minmax_scale(), MinMaxScaler, normalize(), power_transform() (+4 more)

### Community 128 - "Community 128"
Cohesion: 0.09
Nodes (27): _build_sparse_array(), check_verbosity(), # TODO: remove mark once loky bug is fixed:, # TODO: remove mark once loky bug is fixed:, Test LDA on empty document (all-zero rows)., Test Cython version of Dirichlet expectation calculation., Check feature names out for LatentDirichletAllocation., Check data type preservation of fitted attributes. (+19 more)

### Community 129 - "Community 129"
Cohesion: 0.09
Nodes (25): get_pobj(), get_step_size(), tests if the sag pobj matches log reg, tests if the sag pobj matches ridge reg, tests if the sag regressor is computed correctly, # TODO: uncomment when sparse Ridge with intercept will be fixed (#4710), tests if the sag regressor performs well, tests if the binary classifier is computed correctly (+17 more)

### Community 130 - "Community 130"
Cohesion: 0.09
Nodes (4): _BaseHeterogeneousEnsemble, _BaseStacking, StackingClassifier, StackingRegressor

### Community 131 - "Community 131"
Cohesion: 0.07
Nodes (19): BaseEnsemble, _BaseHeterogeneousEnsemble, _fit_single_estimator(), _partition_estimators(), Base class for ensemble-based estimators., Check the base estimator.          Sets the `estimator_` attributes., Make and configure a copy of the `estimator_` attribute.          Warning: This, Return the number of estimators in the ensemble. (+11 more)

### Community 132 - "Community 132"
Cohesion: 0.07
Nodes (17): _fill_predictor_arrays(), This module contains the TreeGrower class.  TreeGrower builds a regression tree, Set children values bounds to respect monotonic constraints., Comparison for priority queue.          Nodes with high gain are higher priority, Tree Node class used in TreeGrower.      This isn't used for prediction purposes, Validate parameters passed to __init__.          Also validate parameters passed, Grow the tree, from root to leaves., Multiply leaves values by shrinkage parameter.          This must be done at the (+9 more)

### Community 133 - "Community 133"
Cohesion: 0.13
Nodes (31): accuracy_score(), balanced_accuracy_score(), brier_score_loss(), _check_set_wise_labels(), _check_targets(), _check_zero_division(), class_likelihood_ratios(), classification_report() (+23 more)

### Community 134 - "Community 134"
Cohesion: 0.07
Nodes (27): _array_api_for_tests(), assert_allclose(), assert_allclose_dense_sparse(), assert_run_python_script_without_output(), check_docstring_parameters(), _convert_container(), _diff_key(), _get_args() (+19 more)

### Community 135 - "Community 135"
Cohesion: 0.08
Nodes (16): BaseSearchCV, Enables Successive Halving search-estimators  The API and results of these estim, BaseSuccessiveHalving, HalvingGridSearchCV, HalvingRandomSearchCV, Custom refit callable to return the index of the best candidate.          We wan, Run fit with all sets of parameters.          Parameters         ----------, Splitter that subsamples a given fraction of the dataset (+8 more)

### Community 136 - "Community 136"
Cohesion: 0.06
Nodes (30): binary_log_loss(), inplace_exp(), inplace_identity(), inplace_identity_derivative(), inplace_logistic(), inplace_logistic_derivative(), inplace_relu(), inplace_relu_derivative() (+22 more)

### Community 137 - "Community 137"
Cohesion: 0.08
Nodes (7): check_binarized_results(), test_label_binarize_binary(), test_label_binarize_multiclass(), test_label_binarize_multilabel(), test_label_binarizer(), test_sparse_output_multilabel_binarizer(), toarray()

### Community 138 - "Community 138"
Cohesion: 0.11
Nodes (5): BaseEnsemble, AdaBoostClassifier, AdaBoostRegressor, BaseWeightBoosting, _RoutingNotSupportedMixin

### Community 139 - "Community 139"
Cohesion: 0.12
Nodes (29): _download_data_to_bunch(), fetch_openml(), _get_data_description_by_id(), _get_data_features(), _get_data_info_by_name(), _get_data_qualities(), _get_json_content_from_openml_api(), _get_local_path() (+21 more)

### Community 140 - "Community 140"
Cohesion: 0.11
Nodes (6): _BaseImputer, _check_inputs_dtype(), MissingIndicator, _most_frequent(), _safe_min(), SimpleImputer

### Community 141 - "Community 141"
Cohesion: 0.09
Nodes (5): Semi-supervised learning algorithms.  These algorithms utilize small amounts of, BaseLabelPropagation, LabelPropagation, LabelSpreading, SelfTrainingClassifier

### Community 142 - "Community 142"
Cohesion: 0.09
Nodes (15): test_get_feature_names_out(), test_metadata_routing_error_for_stacking_estimators(), test_metadata_routing_for_stacking_estimators(), test_routing_passed_metadata_not_supported(), test_stacking_classifier_base_regressor(), test_stacking_classifier_drop_estimator(), test_stacking_classifier_iris(), test_stacking_classifier_multilabel_auto_predict() (+7 more)

### Community 143 - "Community 143"
Cohesion: 0.07
Nodes (25): _encode_target(), Check encoding for multiclass targets., Custom categories with unknown categories that are not in training data., Simple Python implementation of target encoding., Check invalidate input., Check inferred and specified `target_type` on regression target., Check TargetEncoder works with set_output., Check target encoder with multiple features. (+17 more)

### Community 144 - "Community 144"
Cohesion: 0.09
Nodes (12): Descriptor for defining `set_{method}_request` methods in estimators.      .. ve, RequestMethod, ArraySlicingWrapper, _MockEstimatorOnOffPrediction, Validate X and y and make extra check.          Parameters         ----------, Parameters     ----------     array, Fit classifier.          Parameters         ----------         X : array-like of, Predict the first class seen in `classes_`.          Parameters         -------- (+4 more)

### Community 145 - "Community 145"
Cohesion: 0.07
Nodes (22): _BinaryClassifierCurveDisplayMixin, _check_param_lengths(), _convert_to_list_leaving_none(), _deprecate_estimator_name(), _deprecate_y_pred_parameter(), _despine(), _interval_max_min_ratio(), Generate legend information dictionary and expand `metric` if required. (+14 more)

### Community 146 - "Community 146"
Cohesion: 0.09
Nodes (21): AgglomerationTransform, AgglomerativeClustering, FeatureAgglomeration, _hc_cut(), Hierarchical Agglomerative Clustering  These routines perform some hierarchical, Fit and return the result of each sample's clustering assignment.          In ad, Agglomerate features.      Recursively merges pair of clusters of features., Fit the hierarchical clustering on the data.          Parameters         ------- (+13 more)

### Community 147 - "Community 147"
Cohesion: 0.09
Nodes (16): _BaseKMeans, BisectingKMeans, _BisectingTree, Bisecting K-means clustering., Warn when vcomp and mkl are both present, Calculate the sum of squared errors (inertia) per cluster.          Parameters, Split a cluster into 2 subsclusters.          Parameters         ----------, Tree structure representing the hierarchical clusters of BisectingKMeans. (+8 more)

### Community 148 - "Community 148"
Cohesion: 0.09
Nodes (18): _affinity_propagation(), AffinityPropagation, _equal_similarities_and_preferences(), config_context(), get_config(), _get_threadlocal_config(), Global configuration state and functions for management, Context manager to temporarily change the global scikit-learn configuration. (+10 more)

### Community 149 - "Community 149"
Cohesion: 0.13
Nodes (7): dedent_lines(), A line-based string reader., Parameters         ----------         data : str            String with lines se, func_name : Descriptive text             continued text         another_func_nam, Grab signature (if given) and summary, Deindent a list of lines maximally, Reader

### Community 150 - "Community 150"
Cohesion: 0.07
Nodes (27): Test the interaction between remainder and column transformer, Test the interaction between {'drop', 'passthrough'} and     missing column name, Feature names are stored in column transformer.      Column transformer delibera, Check fitting and transforming on pandas and polars dataframes., Check __getitem__ for ColumnTransformer., Test that the right error message is raised when metadata is passed while     no, Check that the remainder columns format matches the format of the other     colu, test_column_transformer() (+19 more)

### Community 151 - "Community 151"
Cohesion: 0.07
Nodes (5): test_get_feature_names_out(), test_qda_prior_copy(), test_qda_prior_type(), test_raises_value_error_on_one_sample_per_class(), test_raises_value_error_on_same_number_of_classes_and_samples()

### Community 152 - "Community 152"
Cohesion: 0.08
Nodes (8): LassoBenchmark, Benchmarks for Lasso., Benchmarks for Ridge., RidgeBenchmark, SGDRegressorBenchmark, SVCBenchmark, Estimator, Predictor

### Community 153 - "Community 153"
Cohesion: 0.15
Nodes (13): _BaseNMF, _beta_divergence(), _beta_loss_to_float(), _check_init(), _fit_coordinate_descent(), _fit_multiplicative_update(), _initialize_nmf(), _multiplicative_update_h() (+5 more)

### Community 154 - "Community 154"
Cohesion: 0.09
Nodes (6): _calculate_threshold(), SelectFromModel, SequentialFeatureSelector, Learn empirical variances from X.          Parameters         ----------, VarianceThreshold, SelectorMixin

### Community 155 - "Community 155"
Cohesion: 0.07
Nodes (16): Testing for Clustering methods, Check the shape of the affinity matrix when using `affinity_propagation., Check that different random states lead to different initialisations     by look, Check that having sparse or dense `centers` format should not     influence the, # TODO: AffinityPropagation must preserve dtype for its fitted attributes, Make sure we do not assign multiple clusters to equal points.      Non-regressio, Test consistency of the affinity propagations., Check equality of precomputed affinity matrix to internally computed affinity (+8 more)

### Community 156 - "Community 156"
Cohesion: 0.07
Nodes (28): build_dataset(), build an ill-posed linear regression problem with many noisy features and     co, test_1d_multioutput_enet_and_multitask_enet_cv(), test_1d_multioutput_lasso_and_multitask_lasso_cv(), test_check_input_false(), test_elasticnet_precompute_gram_weighted_samples(), test_elasticnet_precompute_incorrect_gram(), test_enet_copy_X_False_check_input_False() (+20 more)

### Community 157 - "Community 157"
Cohesion: 0.07
Nodes (22): _naive_ledoit_wolf_shrinkage(), Check consistency between `ShrunkCovariance` and `shrunk_covariance`., Check that we validate X and raise proper error with 0-sample array., Checks that EmpiricalCovariance validates data with mahalanobis., empirical_covariance() should return the same result with array API inputs., ledoit_wolf_shrinkage() should return the same result with array API inputs., log_likelihood() should work with array API inputs., LedoitWolf.score() should work with array API inputs. (+14 more)

### Community 158 - "Community 158"
Cohesion: 0.08
Nodes (22): _check_figure_axes_and_labels(), Check the overall plotting of `from_cv_results`., Check `plot` parameter length validation performed correctly., Check mpl figure and axes are correct., Check chance level plotting behavior, for `from_estimator`/`from_predictions`., Check chance level plotting behavior for `from_cv_results`., Check the behaviour of the name parameters, Check the overall plotting rendering. (+14 more)

### Community 159 - "Community 159"
Cohesion: 0.07
Nodes (26): Check that `_get_response_values` will raise an error when `y_pred` has a     si, Check the behaviour of `_get_response_values` with `decision_function`     and b, Check that `_get_response_values` with `predict_proba` and binary     classifier, Check that we raise the proper error messages in _get_response_values_binary., Check the behaviour of `_get_response_values_binary` using `predict_proba`., Check the behaviour of `_get_response_values_binary` using decision_function., Check that we can call `_get_response_values` with a multiclass estimator.     I, Check the behaviour of passing a list of responses to `_get_response_values`. (+18 more)

### Community 160 - "Community 160"
Cohesion: 0.10
Nodes (14): GaussianProcessRegressor, Gaussian processes regression., Fit Gaussian process regression model.          Parameters         ----------, Gaussian process regression (GPR).      The implementation is based on Algorithm, Predict using the Gaussian process regression model.          We can also predic, Draw samples from Gaussian process and evaluate at X.          Parameters, Return log-marginal likelihood of theta for training data.          Parameters, ConstantKernel (+6 more)

### Community 161 - "Community 161"
Cohesion: 0.09
Nodes (6): csr_copy_predict(), csr_copy_predict_proba(), csr_copy_predict_values(), csr_set_model(), csr_set_problem(), csr_to_libsvm()

### Community 162 - "Community 162"
Cohesion: 0.07
Nodes (2): Make sure bin mapper treats negative categories as missing values., test_categorical_feature_negative_missing()

### Community 163 - "Community 163"
Cohesion: 0.07
Nodes (11): Testing for Neighborhood Component Analysis module (sklearn.neighbors.nca), Test on a simple example.      Puts four points in the input space where the opp, Test that the transformation has the expected shape., Check `get_feature_names_out` for `NeighborhoodComponentsAnalysis`.      Non-reg, Test on a toy example of three points that should collapse      We build a simpl, Test gradient of loss function      Assert that the gradient is almost equal to, test_expected_transformation_shape(), test_finite_differences() (+3 more)

### Community 164 - "Community 164"
Cohesion: 0.10
Nodes (21): EstimatorNoSetOutputWithTransform, EstimatorWithoutSetOutputAndWithoutTransform, EstimatorWithSetOutput, Check _safe_set_output works as expected., Check transform with invalid config., Check that the output is a dataframe., Check pandas adapter has expected behavior., Check transform fails with invalid transform. (+13 more)

### Community 165 - "Community 165"
Cohesion: 0.08
Nodes (26): _atol_for_type(), indexing_dtype(), _logsumexp(), Tools to support array_api., Yield mixed namespace and device inputs for testing.      We do not test for all, Return the absolute tolerance for a given numpy dtype., Return a platform-specific integer dtype suitable for indexing.      On 32-bit p, # TODO: once sufficiently adopted, we might want to instead rely on the (+18 more)

### Community 166 - "Community 166"
Cohesion: 0.14
Nodes (20): AutoPropagatedCallback, _BaseCallback, FitCallback, Method called at the beginning of the fit method of the estimator.          For, Protocol for the auto-propagated callbacks      An auto-propagated callback is a, The maximum number of nested estimators at which the callback should be, Protocol for the callbacks evaluated on tasks during the fit of an estimator., Protocol for the base callbacks. (+12 more)

### Community 167 - "Community 167"
Cohesion: 0.13
Nodes (13): eigh(), EighResult, EigResult, qr(), QRResult, slogdet(), SlogdetResult, svd() (+5 more)

### Community 168 - "Community 168"
Cohesion: 0.11
Nodes (3): _BaseVoting, VotingClassifier, VotingRegressor

### Community 169 - "Community 169"
Cohesion: 0.12
Nodes (6): BaseThresholdClassifier, _check_is_fitted(), _fit_and_score_over_thresholds(), FixedThresholdClassifier, _mean_interpolated_score(), TunedThresholdClassifierCV

### Community 170 - "Community 170"
Cohesion: 0.09
Nodes (7): OneToOneFeatureMixin, binarize(), Binarizer, MaxAbsScaler, Normalizer, RobustScaler, Methods for scaling, centering, normalization, binarization, and more.

### Community 171 - "Community 171"
Cohesion: 0.08
Nodes (2): # TODO:, # TODO: The high number of iterations are required for convergence and show room

### Community 172 - "Community 172"
Cohesion: 0.08
Nodes (6): Check the impact of `sample_weight` one computed quantiles., Make sure that `sample_weight` is not changed in place., Check get_feature_names_out for different settings.     Non-regression test for, test_kbinsdiscretizer_effect_sample_weight(), test_kbinsdiscretizer_no_mutating_sample_weight(), test_kbinsdiscrtizer_get_feature_names_out()

### Community 173 - "Community 173"
Cohesion: 0.08
Nodes (4): Check that we don't modify in-place the pre-computed sparse matrix.     Non-regr, Check that cluster correction using predecessor is working as expected.      In, test_optics_input_not_modified_precomputed_sparse_nodiag(), test_optics_predecessor_correction_ordering()

### Community 174 - "Community 174"
Cohesion: 0.08
Nodes (24): Check the behaviour of the `negate_score` parameter calling `from_estimator` and, Check that we can overwrite the default score name shown on the y-axis., Check the behaviour of setting the `score_type` parameter., Check the behaviour of setting the `score_type` parameter., Check that we raise a proper error when passing invalid parameters., Check the behaviour of the x-axis scaling depending on the data provided., Check the behaviour of the parameter `std_display_style`., Check the default usage of the LearningCurveDisplay class. (+16 more)

### Community 175 - "Community 175"
Cohesion: 0.13
Nodes (19): check_input_size_random_matrix(), check_input_with_sparse_random_matrix(), check_size_generated(), check_zero_mean_and_unit_norm(), densify(), make_sparse_random_data(), test_basic_property_of_random_matrix(), test_basic_property_of_sparse_random_matrix() (+11 more)

### Community 176 - "Community 176"
Cohesion: 0.12
Nodes (10): _BaseTreeExporter, _color_brew(), _compute_depth(), _DOTTreeExporter, export_graphviz(), export_text(), _matplotlib_to_rgb(), _MPLTreeExporter (+2 more)

### Community 177 - "Community 177"
Cohesion: 0.15
Nodes (23): check_conda_lock_version(), check_conda_version(), conda_lock(), create_conda_lock_file(), execute_command(), get_conda_environment_content(), get_package_with_constraint(), get_pip_requirements_content() (+15 more)

### Community 178 - "Community 178"
Cohesion: 0.12
Nodes (21): dict, _check_unknown(), _encode(), _extract_missing(), _get_counts(), _map_to_integer(), MissingValues, _nandict (+13 more)

### Community 179 - "Community 179"
Cohesion: 0.08
Nodes (24): argpartition(), broadcast_shapes(), create_diagonal(), isin(), nan_to_num(), one_hot(), pad(), partition() (+16 more)

### Community 180 - "Community 180"
Cohesion: 0.09
Nodes (11): BayesianGaussianMixture, Check that the parameters are well defined.          Parameters         --------, Check the parameter of the Dirichlet distribution., Check the parameters of the Gaussian distribution.          Parameters         -, Check the prior parameters of the precision distribution.          Parameters, Check the `covariance_prior_`.          Parameters         ----------         X, Estimate the full Wishart distribution parameters.          Parameters         -, Estimate the tied Wishart distribution parameters.          Parameters         - (+3 more)

### Community 181 - "Community 181"
Cohesion: 0.08
Nodes (3): Tests for Incremental PCA., Check feature names out for IncrementalPCA., test_incremental_pca_feature_names_out()

### Community 182 - "Community 182"
Cohesion: 0.10
Nodes (18): generate_toy_data(), Check feature names out for *SparsePCA., Check that `tol` and `max_no_improvement` act as early stopping., Check the equivalence of the components found by PCA and SparsePCA.      Non-reg, Check that `inverse_transform` in `SparsePCA` and `PCA` are similar., Check the `transform` and `inverse_transform` round trip with no loss of     inf, # TODO: remove mark once loky bug is fixed:, test_equivalence_components_pca_spca() (+10 more)

### Community 183 - "Community 183"
Cohesion: 0.10
Nodes (15): tuple, _changed_params(), _EstimatorPrettyPrinter, KeyValTuple, KeyValTupleParam, This module contains the _EstimatorPrettyPrinter class used in BaseEstimator.__r, Pretty Printer class for estimator objects.      This extends the pprint.PrettyP, Format dict items or parameters respecting the compact=True         parameter. F (+7 more)

### Community 184 - "Community 184"
Cohesion: 0.10
Nodes (16): _ArrayLikes, _Callables, generate_invalid_param_val(), make_constraint(), _NanConstraint, Convert the constraint into the appropriate Constraint object.      Parameters, Decorator to validate types and values of functions and methods.      Parameters, Validate types and values of given parameters.      Parameters     ---------- (+8 more)

### Community 185 - "Community 185"
Cohesion: 0.12
Nodes (12): _BaseEncoder, Fit the :class:`TargetEncoder` to X and y.          It is discouraged to use thi, Fit :class:`TargetEncoder` and transform `X` with the target encoding., Target Encoder for regression and classification targets.      Each category is, Transform X with the target encoding.          This method internally uses the `, Fit a target encoding with all the data., Learn target encodings., Learn multiclass encodings.          Learn encodings for each class (c) then reo (+4 more)

### Community 186 - "Community 186"
Cohesion: 0.11
Nodes (15): BiclusterMixin, _do_bistochastic_test(), _do_scale_test(), MockBiclustering, Check parameters validation in `SpectralBiClustering`, Different number of biclusters in A and B, test_bistochastic_normalize(), test_consensus_score_issue2445() (+7 more)

### Community 187 - "Community 187"
Cohesion: 0.16
Nodes (2): DensityMixin, BaseMixture

### Community 188 - "Community 188"
Cohesion: 0.10
Nodes (22): _check_means(), _check_precision_matrix(), _check_precision_positivity(), _check_precisions(), _check_precisions_full(), _check_weights(), _estimate_gaussian_covariances_diag(), _estimate_gaussian_covariances_full() (+14 more)

### Community 189 - "Community 189"
Cohesion: 0.08
Nodes (2): Check that we can fit a line where all samples are inliers.     Non-regression t, test_perfect_horizontal_line()

### Community 190 - "Community 190"
Cohesion: 0.09
Nodes (4): check_svm_model_equal(), Check that sparse SVC gives the same result as SVC., test_sparse_oneclasssvm(), test_svc()

### Community 191 - "Community 191"
Cohesion: 0.12
Nodes (12): at, Allow for the alternate syntax ``at(x)[start:stop:step]``.          It looks pre, Implement all update operations.          Parameters         ----------, Apply ``x[idx] = y`` and return the update array., Apply ``x[idx] += y`` and return the updated array., Apply ``x[idx] -= y`` and return the updated array., Apply ``x[idx] *= y`` and return the updated array., Apply ``x[idx] /= y`` and return the updated array. (+4 more)

### Community 192 - "Community 192"
Cohesion: 0.11
Nodes (6): copy_predict(), copy_predict_proba(), copy_predict_values(), dense_to_libsvm(), set_model(), set_problem()

### Community 193 - "Community 193"
Cohesion: 0.09
Nodes (21): Checks name when selecting only the second column, Checks name when selecting the second column with numpy array, Check feature_names_out for verbose_feature_names_out=True (default), Check feature_names_out for verbose_feature_names_out=True (default), Check feature_names_out for verbose_feature_names_out=False, Check feature_names_out for verbose_feature_names_out=False, Check column transformer behavior with set_output., Check ColumnTransformer outputs mixed types correctly. (+13 more)

### Community 194 - "Community 194"
Cohesion: 0.09
Nodes (23): check_normalizer(), Convenient checking function for `test_normalizer_l1_l2_max` and     `test_norma, test_add_dummy_feature_sparse(), test_binarizer(), test_maxabs_scaler_transform_one_row_csr(), test_maxabs_scaler_zero_variance_features(), test_normalize(), test_normalizer_l1_l2_max() (+15 more)

### Community 195 - "Community 195"
Cohesion: 0.09
Nodes (11): # TODO: compare results on dense and sparse data as proposed in:, Check that we raise a proper error message when n_neighbors == n_samples.      N, Check that the fitted attributes are stored using the data type of X., Check the equivalence of the results with 32 and 64 bits input., Check that LocalOutlierFactor raises a warning when duplicate values     in the, Tests LOF with a distance matrix., test_lof_dtype_equivalence(), test_lof_duplicate_samples() (+3 more)

### Community 196 - "Community 196"
Cohesion: 0.09
Nodes (2): Check `n_nonzero_coefs_` correct when `tol` is and isn't set., test_estimator_n_nonzero_coefs()

### Community 197 - "Community 197"
Cohesion: 0.09
Nodes (20): Check the behavior of the ParamsDict class., Test `_params_html_repr` when `link_to_param_doc` returns None., Return anchor URLs for documented parameters in the estimator., Ensure None is returned when the parameter is not documented., Ensure None is returned when the estimator has no docstring., Non-regression test for     https://github.com/scikit-learn/scikit-learn/issues/, Check the behavior of the `_read_params` function., Check returned HTML template (+12 more)

### Community 198 - "Community 198"
Cohesion: 0.14
Nodes (13): MyPassiveAggressive, Test that both are equivalent., Test that both are equivalent., test_class_weights(), test_classifier_accuracy(), test_classifier_correctness(), test_classifier_refit(), test_equal_class_weight() (+5 more)

### Community 199 - "Community 199"
Cohesion: 0.10
Nodes (20): _check_chance_level(), _check_figure_axes_and_labels(), Check `plot` parameter length validation performed correctly., Check overall plotting of `from_cv_results`., Check chance level line and line styles correct., Check chance level plotting behavior of `from_predictions`, `from_estimator`., Check mpl axes and figure defaults are correct., Check chance level plotting behavior with `from_cv_results`. (+12 more)

### Community 200 - "Community 200"
Cohesion: 0.11
Nodes (12): _assert_equal_with_sign_flipping(), # TODO: investigate why this test is seed-sensitive on 32-bit Python, Check that `SpectralEmbedding is preserving the dtype of the fitted     attribut, Test that `eigen_tol="auto"` is resolved correctly, Check array A and B are equal with possible sign flipping on     each column, test_spectral_eigen_tol_auto(), test_spectral_embedding_amg_solver(), test_spectral_embedding_amg_solver_failure() (+4 more)

### Community 201 - "Community 201"
Cohesion: 0.10
Nodes (17): Non-regression test to check that we can still convert a sparse container     fr, Check `assert_docstring_consistency` argument checking correct., Check `assert_docstring_consistency` difference message., Check that we convert the container to the right type of array with the     righ, test_assert_docstring_consistency_arg_checks(), test_assert_docstring_consistency_error_msg(), test_convert_container(), test_convert_container_sparse_to_sparse() (+9 more)

### Community 202 - "Community 202"
Cohesion: 0.09
Nodes (4): test_adaboost_decision_function(), test_adaboost_numerically_stable_feature_importance_with_small_weights(), test_multidimensional_X(), test_sample_weight_adaboost_regressor()

### Community 203 - "Community 203"
Cohesion: 0.13
Nodes (22): _array_indexing(), _determine_key_type(), _get_column_indices(), _get_column_indices_for_bool_or_int(), _list_indexing(), _narwhals_indexing(), _pandas_indexing(), Determine the data type of key.      Parameters     ----------     key : scalar, (+14 more)

### Community 204 - "Community 204"
Cohesion: 0.12
Nodes (14): _auto_wrap_is_configured(), check_library_installed(), _get_adapter_from_container(), _get_container_adapter(), _get_output_config(), PandasAdapter, PolarsAdapter, Check library is installed. (+6 more)

### Community 205 - "Community 205"
Cohesion: 0.10
Nodes (11): ARDRegression, BayesianRidge, Various bayesian regression, Fit the model.          Parameters         ----------         X : ndarray of sha, Bayesian ridge regression.      Fit a Bayesian ridge model. See the Notes sectio, Predict using the linear model.          In addition to the mean of the predicti, Update posterior mean and compute corresponding sse (sum of squared errors)., Log marginal likelihood. (+3 more)

### Community 206 - "Community 206"
Cohesion: 0.11
Nodes (14): center_and_norm(), Test the fastica algorithm., Centers and norms x **in place**      Parameters     -----------     x: ndarray, Test unit variance of transformed data using FastICA algorithm.      Check that, Test unit variance of transformed data using FastICA algorithm.      Bug #13056, Test FastICA is consistent between whiten_solvers., Test FastICA eigh solver raises warning for low-rank data., test_fastica_convergence_fail() (+6 more)

### Community 207 - "Community 207"
Cohesion: 0.09
Nodes (7): Testing for Gaussian process classification, Check that expected error are raised during fit., Checks that the latent mean and variance have the right shape., Checks that the latent mean and variance have the right shape., test_gpc_fit_error(), test_gpc_latent_mean_and_variance_complain_on_more_than_2_classes(), test_gpc_latent_mean_and_variance_shape()

### Community 208 - "Community 208"
Cohesion: 0.12
Nodes (15): AvailableParameterEstimator, DelegatorData, _generate_meta_estimator_instances_with_pipeline(), _get_instance_with_pipeline(), Common tests for metaestimators, This is a mock available_if function, Given a single meta-estimator instance, generate an instance with a pipeline, Generate instances of meta-estimators fed with a pipeline      Are considered me (+7 more)

### Community 209 - "Community 209"
Cohesion: 0.11
Nodes (14): assert_raises_on_all_points_same_cluster(), assert_raises_on_only_one_label(), Check that silhouette_samples works for sparse matrices correctly., Check that silhouette_samples works for sparse matrices correctly., Check for non-CSR input to private method `_silhouette_reduce`., Assert message when there is only one label, Assert message when all point are in different clusters, Check that silhouette_score works for precomputed metrics that are integers. (+6 more)

### Community 210 - "Community 210"
Cohesion: 0.13
Nodes (17): atomic_benchmark_estimator(), benchmark(), benchmark_estimator(), benchmark_throughputs(), boxplot_runtimes(), bulk_benchmark_estimator(), generate_dataset(), n_feature_influence() (+9 more)

### Community 211 - "Community 211"
Cohesion: 0.12
Nodes (18): arange(), argsort(), asarray(), astype(), clip(), _ensure_single_chunk(), Array API compatibility wrapper for asarray().      See the corresponding docume, # TODO: respect device keyword? (+10 more)

### Community 212 - "Community 212"
Cohesion: 0.11
Nodes (15): Extra array functions built on top of the array API standard., _AtOp, Update operations for read-only arrays., Operations for use in `xpx.at`., Return string representation (useful for pytest logs).          Returns, Sentinel for undefined values., Undef, _is_jax_jit_enabled() (+7 more)

### Community 213 - "Community 213"
Cohesion: 0.14
Nodes (13): bench_one(), _fit_projected_gradient(), load_20news(), _nls_subproblem(), _norm(), _PGNMF, plot_results(), Benchmarks of Non-Negative Matrix Factorization (+5 more)

### Community 214 - "Community 214"
Cohesion: 0.15
Nodes (10): DTypesAll, DTypesBool, DTypesComplex, DTypesIntegral, DTypesNumeric, DTypesReal, DTypesSigned, DTypesUnsigned (+2 more)

### Community 215 - "Community 215"
Cohesion: 0.12
Nodes (13): empirical_covariance(), EmpiricalCovariance, log_likelihood(), Maximum likelihood covariance estimator., Maximum likelihood covariance estimator.      Read more in the :ref:`User Guide, Saves the covariance and precision estimates          Storage is done accordingl, Getter for the precision matrix.          Returns         -------         precis, Fit the maximum likelihood covariance estimator to X.          Parameters (+5 more)

### Community 216 - "Community 216"
Cohesion: 0.10
Nodes (10): Exponentiation, Get parameters of this kernel.          Parameters         ----------         de, Returns the (flattened, log-transformed) non-fixed hyperparameters.          Not, Sets the (flattened, log-transformed) non-fixed hyperparameters.          Parame, Returns the log-transformed bounds on the theta.          Returns         ------, Return the kernel k(X, Y) and optionally its gradient.          Parameters, Returns the diagonal of the kernel k(X, X).          The result of this method i, Returns whether the kernel is stationary. (+2 more)

### Community 217 - "Community 217"
Cohesion: 0.10
Nodes (2): # TODO: replace this torch/MPS-specific coverage by array-api-strict once, # TODO: add cupy to the list of libraries once the following upstream issue

### Community 218 - "Community 218"
Cohesion: 0.10
Nodes (6): Check the posterior covariance matrix sigma_      Non-regression test for https:, Check scores attribute shape, Check value of score on toy example.      Compute log marginal likelihood with e, test_bayesian_covariance_matrix(), test_bayesian_ridge_score_values(), test_bayesian_ridge_scores()

### Community 219 - "Community 219"
Cohesion: 0.10
Nodes (20): Check the overall plotting rendering., Check the behaviour of the default constructor without using the class     metho, Check that we raise the proper error when validating parameters., Check that the text color is appropriate depending on background., Check the behaviour of the plotting with more complex pipeline., Check that when labels=None, the unique values in `y_pred` and `y_true`     will, Check that the max color is used for the color of the text., Check that im_kw passes kwargs to imshow (+12 more)

### Community 220 - "Community 220"
Cohesion: 0.10
Nodes (3): Tests for DBSCAN clustering algorithm, Check that we don't modify in-place the pre-computed sparse matrix.      Non-reg, test_dbscan_input_not_modified_precomputed_sparse_nodiag()

### Community 221 - "Community 221"
Cohesion: 0.10
Nodes (3): Testing for export functions of decision trees (sklearn.tree.export)., Test that _rgb_to_hexstring correctly converts an RGB tuple to a hex color strin, test_rgb_to_hexstring()

### Community 222 - "Community 222"
Cohesion: 0.10
Nodes (10): create_sample_data(), # TODO: compare results on dense and sparse data as proposed in:, Check that the fitted attributes are stored accordingly to the     data type of, Check the equivalence of the results with 32 and 64 bits input., Check get_feature_names_out for Isomap., test_get_feature_names_out(), test_isomap_dtype_equivalence(), test_isomap_fitted_attributes_dtype() (+2 more)

### Community 223 - "Community 223"
Cohesion: 0.10
Nodes (10): Check that we raise an error when tol<0 and direction='forward, Check that SequentialFeatureSelector works negative tol      non-regression test, Check that no exception raised when cv is generator      non-regression test for, Check the behaviour of `n_features_to_select="auto"` with different     values f, Check the behaviour stopping criterion for feature selection     depending on th, test_backward_neg_tol(), test_cv_generator_support(), test_forward_neg_tol_error() (+2 more)

### Community 224 - "Community 224"
Cohesion: 0.14
Nodes (13): gen_toy_problem_1d(), gen_toy_problem_2d(), gen_toy_problem_4d(), no_stdout_stderr(), Testing for Theil-Sen module (sklearn.linear_model.theil_sen), test_checksubparams_invalid_input(), test_subpopulation(), test_subsamples() (+5 more)

### Community 225 - "Community 225"
Cohesion: 0.13
Nodes (3): RFE, _rfe_single_fit(), RFECV

### Community 226 - "Community 226"
Cohesion: 0.14
Nodes (10): Tools for model inspection., PartialDependenceDisplay, Plot 2-way partial dependence.          Parameters         ----------         av, Plot partial dependence plots.          Parameters         ----------         ax, Partial Dependence Plot (PDP) and Individual Conditional Expectation (ICE)., Partial dependence (PD) and individual conditional expectation (ICE) plots., Compute the number of samples as an integer., Plot the ICE lines.          Parameters         ----------         preds : ndarr (+2 more)

### Community 227 - "Community 227"
Cohesion: 0.13
Nodes (6): _check_refit(), GridSearchCV, ParameterGrid, ParameterSampler, _search_estimator_has(), _yield_masked_array_for_each_param()

### Community 228 - "Community 228"
Cohesion: 0.11
Nodes (12): _adjusted_metric(), RadiusNeighborsClassifier, Nearest Neighbor Classification, Return probability estimates for the test data X.          Parameters         --, # TODO: systematize this mapping of metric for, # TODO: Implement efficient multi-output solution, # TODO: adapt the heuristic for `strategy="auto"` for, Classifier implementing a vote among neighbors within a given radius.      Read (+4 more)

### Community 229 - "Community 229"
Cohesion: 0.11
Nodes (15): _fetch_fixture(), hide_available_matplotlib(), hide_available_pandas(), munge_scipy_to_check_spmatrix_usage(), pyplot(), pytest_collection_modifyitems(), pytest_configure(), pytest_generate_tests() (+7 more)

### Community 230 - "Community 230"
Cohesion: 0.13
Nodes (3): _BaseDiscreteNB, _BaseNB, Compute the unnormalized posterior log probability of X          I.e. ``log P(c)

### Community 231 - "Community 231"
Cohesion: 0.11
Nodes (10): check_branching_factor(), check_threshold(), Tests for the birch clustering algorithm., Use the leaf linked list for traversal, Check `get_feature_names_out` for `Birch`., Check that both subclusters are updated when a node a split, even when there are, test_both_subclusters_updated(), test_branching_factor() (+2 more)

### Community 232 - "Community 232"
Cohesion: 0.15
Nodes (12): mock_function(), MockClass1, MockClass2, MockClass3, MockClass4, MockClass5, MockClass6, Number of input features. (+4 more)

### Community 233 - "Community 233"
Cohesion: 0.10
Nodes (2): # TODO: Inspect slight numerical discrepancy, # TODO: Inspect slight numerical discrepancy

### Community 234 - "Community 234"
Cohesion: 0.10
Nodes (4): Check that we raise the proper AttributeErrors when the `estimator`     does not, Test that the right error message is raised when metadata is passed while     no, test_routing_passed_metadata_not_supported(), test_self_training_estimator_attribute_error()

### Community 235 - "Community 235"
Cohesion: 0.16
Nodes (10): BaggingClassifier, _consumes_sample_weight(), _generate_bagging_indices(), _generate_indices(), _parallel_build_estimators(), _parallel_decision_function(), _parallel_predict_log_proba(), _parallel_predict_proba() (+2 more)

### Community 236 - "Community 236"
Cohesion: 0.18
Nodes (2): _check_gcv_mode(), _RidgeGCV

### Community 237 - "Community 237"
Cohesion: 0.18
Nodes (4): Mapping, NumpyDocString, Parses a numpydoc string to an abstract representation      Instances define a m, .. index:: default            :refguide: something, else, and more

### Community 238 - "Community 238"
Cohesion: 0.12
Nodes (13): _assert_graphical_lasso_cv_scores(), Test the graphical_lasso module., Check that we can pass an array-like to `alphas`.      Non-regression test for:, Check that if an array-like containing a value     outside of (0, inf] is passed, Check that `GraphicalLassoCV` internally dispatches metadata to     the splitter, Test the graphical lasso solvers., Test graphical_lasso's early return condition when alpha=0., test_graphical_lasso_cv_alphas_invalid_array() (+5 more)

### Community 239 - "Community 239"
Cohesion: 0.12
Nodes (4): check_hyperparameters_equal(), Testing for kernels for Gaussian processes., test_kernel_clone(), test_kernel_clone_after_set_params()

### Community 240 - "Community 240"
Cohesion: 0.11
Nodes (9): Testing for the nearest centroid module., Check that we raise an error when the user-defined priors are negative., Check that we raise a warning and normalize the user-defined priors when they, Check that we raise an AttributeError with Manhattan metric when trying     to c, Check that we raise an error when the variance for all features is zero., test_error_zero_variances(), test_method_not_available_with_manhattan(), test_negative_priors_error() (+1 more)

### Community 241 - "Community 241"
Cohesion: 0.11
Nodes (14): AnotherMixin, Check errors in _wrap_data_with_container., Check that multiple init_subclasses passes parameters up., Check adapters have the correct interface., Check the behavior fo `_get_adapter_from_container`., test_adapter_class_has_interface(), test__container_error_validation(), test_get_adapter_from_container() (+6 more)

### Community 242 - "Community 242"
Cohesion: 0.12
Nodes (17): asarrays(), capabilities(), eager_shape(), in1d(), is_python_scalar(), jax_autojit(), meta_namespace(), ndindex() (+9 more)

### Community 243 - "Community 243"
Cohesion: 0.13
Nodes (16): check_classification_targets(), _check_partial_fit_first_call(), class_distribution(), _is_integral_float(), is_multilabel(), _ovr_decision_function(), Utilities to handle multiclass/multioutput target in classifiers., Check if ``y`` is in a multilabel format.      Parameters     ----------     y : (+8 more)

### Community 244 - "Community 244"
Cohesion: 0.17
Nodes (10): EllipticEnvelope, An object for detecting outliers in a Gaussian distributed dataset.      Read mo, Fit the EllipticEnvelope model.          Parameters         ----------         X, Compute the decision function of the given observations.          Parameters, Compute the negative Mahalanobis distances.          Parameters         --------, Predict labels (1 inlier, -1 outlier) of X according to fitted model.          P, Return the mean accuracy on the given test data and labels.          In multi-la, MinCovDet (+2 more)

### Community 245 - "Community 245"
Cohesion: 0.12
Nodes (13): ArffDecoder, BadAttributeName, BadRelationFormat, load(), loads(), Load a file-like object containing the ARFF document and convert it into     a P, Convert a string instance containing the ARFF document into a Python     object., Error raised when the relation declaration is in an invalid format. (+5 more)

### Community 246 - "Community 246"
Cohesion: 0.13
Nodes (7): DictVectorizer, Learn a list of feature name -> indices mappings.          Parameters         --, Transform array or sparse matrix X back to feature mappings.          X must hav, Transform feature->value dicts to array or sparse matrix.          Named feature, Get output feature names for transformation.          Parameters         -------, Restrict the features to those in support using feature selection.          This, Feature extraction from raw data.

### Community 247 - "Community 247"
Cohesion: 0.11
Nodes (8): _estimator_has(), FrozenEstimator, Set the parameters of this estimator.          The only valid key here is `estim, Check that final_estimator has `attr`.      Used together with `available_if`., Get parameters for this estimator.          Returns a `{"estimator": estimator}`, Estimator that wraps a fitted estimator to prevent re-fitting.      This meta-es, __getitem__ is defined in :class:`~sklearn.pipeline.Pipeline` and \, No-op.          As a frozen estimator, calling `fit` has no effect.          Par

### Community 248 - "Community 248"
Cohesion: 0.19
Nodes (13): _find_smallest_angle(), _get_rescaled_operator(), _get_valid_accept_sparse(), resolve_solver(), resolve_solver_for_numpy(), Ridge, ridge_regression(), _solve_cholesky() (+5 more)

### Community 249 - "Community 249"
Cohesion: 0.16
Nodes (8): r""" ===================================================================== The J, # TODO: compute the expected value of eps and add them to the previous plot, BaseRandomProjection, _check_density(), _check_input_size(), _gaussian_random_matrix(), johnson_lindenstrauss_min_dim(), _sparse_random_matrix()

### Community 250 - "Community 250"
Cohesion: 0.14
Nodes (3): _create_expansion(), PolynomialFeatures, SplineTransformer

### Community 251 - "Community 251"
Cohesion: 0.11
Nodes (10): _HTMLDocumentationLinkMixin, _IDCounter, Generate sequential ids with a prefix., Mixin to handle consistently the HTML representation.      When inheriting from, HTML representation of estimator.         This is redundant with the logic of `_, This function is returned by the @property `_repr_html_` to make         `hasatt, Mime bundle used by jupyter kernels to display estimator, Mixin class allowing to generate a link to the API documentation.      This mixi (+2 more)

### Community 252 - "Community 252"
Cohesion: 0.16
Nodes (12): detectTheme(), estimator_html_repr(), forceTheme(), _get_visual_block(), Write labeled html with or without a dropdown with named details.      Parameter, Generate information about how to display an estimator., Write estimator to html in serial, parallel, or by itself (single).      For mul, HTML Representation of Estimator      Parameters     ----------     kind : {'ser (+4 more)

### Community 253 - "Community 253"
Cohesion: 0.11
Nodes (14): Check that centers dtype is the same as input data dtype., Check that the results are the same between float32 and float64., Tries to perform bisect k-means for three clusters to check     if splitting dat, Test that BisectingKMeans validates center shape correctly with callable init., Test Bisecting K-Means with sparse data.      Checks if labels and centers are t, Test if resulting labels are in range [0, n_clusters - 1]., Check if labels from fit(X) method are same as from fit(X).predict(X)., test_bisecting_kmeans_custom_init_validation() (+6 more)

### Community 254 - "Community 254"
Cohesion: 0.11
Nodes (8): Check the equivalence between between sparse and dense DictVectorizer.     Non-r, Check that we raise an error when the value associated to a feature     is not s, Check that integer feature names are converted to strings in     feature_names_o, Check that unfitted DictVectorizer instance raises NotFittedError.      This sho, test_dict_vectorizer_get_feature_names_out(), test_dict_vectorizer_not_fitted_error(), test_dict_vectorizer_unsupported_value_type(), test_dictvectorizer_dense_sparse_equivalence()

### Community 255 - "Community 255"
Cohesion: 0.11
Nodes (8): MockEst, MockMetaEstimator, MetaEstimator to check if doctest on delegated methods work.          Parameters, This is available only if delegate has predict.          Parameters         ----, This is available only if delegate has score.          Parameters         ------, This is available only if delegate has predict_proba.          Parameters, Incorrect docstring but should not be tested, test_check_docstring_parameters()

### Community 256 - "Community 256"
Cohesion: 0.11
Nodes (11): MockClassifier, test_cross_val_predict_y_none(), test_cross_val_score(), test_cross_val_score_allow_nans(), test_cross_val_score_fit_params(), test_cross_val_score_score_func(), test_cross_val_score_sparse_fit_params(), test_cross_validate_invalid_scoring_param() (+3 more)

### Community 257 - "Community 257"
Cohesion: 0.18
Nodes (1): BaseDecisionTree

### Community 258 - "Community 258"
Cohesion: 0.20
Nodes (9): ancestor(), apportion(), buchheim(), DrawTree, execute_shifts(), first_walk(), move_subtree(), second_walk() (+1 more)

### Community 259 - "Community 259"
Cohesion: 0.12
Nodes (9): _BaseImputer, NoFitIndicatorImputer, NoPrecomputedMaskFit, NoPrecomputedMaskTransform, NoTransformIndicatorImputer, test_base_imputer_not_fit(), test_base_imputer_not_transform(), test_base_no_precomputed_mask_fit() (+1 more)

### Community 260 - "Community 260"
Cohesion: 0.13
Nodes (7): BaseMixture, GaussianMixture, Gaussian Mixture.      Representation of a Gaussian mixture model probability di, Return the number of free parameters in the model., Bayesian information criterion for the current model on the input X.          Yo, Akaike information criterion for the current model on the input X.          You, Mixture modeling algorithms.

### Community 261 - "Community 261"
Cohesion: 0.24
Nodes (16): bench_a(), bench_b(), bench_c(), get_data(), handle_missing_dataset(), norm_diff(), plot_power_iter_vs_s(), plot_time_vs_s() (+8 more)

### Community 262 - "Community 262"
Cohesion: 0.13
Nodes (6): Predictor, Abstract base class for benchmarks of estimators implementing predict, ElasticNetBenchmark, Benchmarks for ElasticNet., KNeighborsClassifierBenchmark, Benchmarks for KNeighborsClassifier.

### Community 263 - "Community 263"
Cohesion: 0.27
Nodes (1): LatentDirichletAllocation

### Community 264 - "Community 264"
Cohesion: 0.19
Nodes (14): pytest_collection_modifyitems(), pytest_runtest_setup(), Called after collect is completed.      Parameters     ----------     config : p, # TODO: configure numpy to output scalar arrays as regular Python scalars, setup_compose(), setup_grid_search(), setup_impute(), setup_labeled_faces() (+6 more)

### Community 265 - "Community 265"
Cohesion: 0.13
Nodes (12): Exception, ArffException, BadAttributeFormat, BadAttributeType, BadNominalFormatting, BadStringValue, Error raised when some attribute declaration is in an invalid format., Error raised when some invalid type is provided into the attribute     declarati (+4 more)

### Community 266 - "Community 266"
Cohesion: 0.17
Nodes (11): BadDataFormat, BadLayout, BadNumericalValue, DenseGeneratorData, _parse_values(), (INTERNAL) Split a line into a list of values, Error raised when some data instance is in an invalid format., Error raised when and invalid numerical value is used in some data     instance. (+3 more)

### Community 267 - "Community 267"
Cohesion: 0.13
Nodes (10): KNeighborsMixin, KNeighborsRegressor, Fit the k-nearest neighbors regressor from the training dataset.          Parame, Regression based on k-nearest neighbors.      The target is predicted by local i, Predict the target for the provided data.          Parameters         ----------, NearestNeighbors, Unsupervised nearest neighbors learner, Unsupervised learner for implementing neighbor searches.      Read more in the : (+2 more)

### Community 268 - "Community 268"
Cohesion: 0.17
Nodes (7): _check_params(), kneighbors_graph(), KNeighborsTransformer, _query_include_self(), radius_neighbors_graph(), RadiusNeighborsTransformer, The k-nearest neighbors algorithms.

### Community 269 - "Community 269"
Cohesion: 0.12
Nodes (1): Version

### Community 270 - "Community 270"
Cohesion: 0.12
Nodes (4): Check that class_weight can contain more labels than in y.      Non-regression t, Check that we can compute weight for sparse `y`., test_class_weight_does_not_contains_more_classes(), test_compute_sample_weight_sparse()

### Community 271 - "Community 271"
Cohesion: 0.16
Nodes (10): assert_is_stump(), _check_children_consistency(), _make_training_data(), Check that grower respects interaction constraints., test_grow_tree(), test_grower_interaction_constraints(), test_init_parameters_validation(), test_input_validation() (+2 more)

### Community 273 - "Community 273"
Cohesion: 0.12
Nodes (3): # TODO: remove mark once loky bug is fixed:, Test that non-metric MDS normalized stress is scale-invariant., test_normed_stress()

### Community 274 - "Community 274"
Cohesion: 0.12
Nodes (4): Check that a proper error message is raised when `max_samples` is not     set to, Check that `__array_function__` (NEP18) is not called., test_permutation_importance_array_function_not_called(), test_permutation_importance_max_samples_error()

### Community 275 - "Community 275"
Cohesion: 0.12
Nodes (10): Test quantile regression for asymmetric distributed targets., Test equivariace of quantile regression.      See Koenker (2005) Quantile Regres, Test that linprog fails., Test that sparse and dense X give same results., Check that we will raise a proper error when requesting     `solver='interior-po, test_asymmetric_error(), test_equivariance(), test_error_interior_point_future() (+2 more)

### Community 276 - "Community 276"
Cohesion: 0.12
Nodes (2): Test that custom weights raise an error for single-output data., test__check_reg_targets_single_output_error()

### Community 277 - "Community 277"
Cohesion: 0.15
Nodes (10): make_sparse_data(), Test that a warning is issued if model does not converge, Test that sparse coordinate descent works for read-only buffers, test_enet_coordinate_descent_sparse(), test_enet_multitarget(), test_path_parameters(), test_same_output_sparse_dense_lasso_and_enet_cv(), test_sparse_enet_not_as_toy_dataset() (+2 more)

### Community 278 - "Community 278"
Cohesion: 0.12
Nodes (17): _asarray_with_order(), _check_array_api_dispatch(), _count_nonzero(), _cov(), _expit(), get_namespace(), _logit(), Helper to support the order kwarg only for NumPy-backed arrays      Memory layou (+9 more)

### Community 279 - "Community 279"
Cohesion: 0.13
Nodes (12): delayed(), _FuncWrapper, _get_threadpool_controller(), Customizations of :mod:`joblib` and :mod:`threadpoolctl` tools for scikit-learn, Load the global configuration before calling the function., Return the global threadpool controller instance., Decorator to limit the number of threads used at the function level.      It sho, Helper function that intends to attach a config to a delayed function. (+4 more)

### Community 280 - "Community 280"
Cohesion: 0.17
Nodes (4): BaseBagging, _average_path_length(), IsolationForest, _parallel_compute_tree_depths()

### Community 281 - "Community 281"
Cohesion: 0.15
Nodes (6): Benchmark, Abstract base class for all the benchmarks, CrossValidationBenchmark, GridSearchBenchmark, Benchmarks for Cross Validation., Benchmarks for GridSearch.

### Community 282 - "Community 282"
Cohesion: 0.17
Nodes (7): Estimator, Abstract base class for all benchmarks of estimators, Return the dataset for a combination of parameters, Return an instance of the estimator for a combination of parameters, Return True if the benchmark should be skipped for these params, Pickle a fitted estimator for all combinations of parameters, Generate dataset and load the fitted estimator

### Community 284 - "Community 284"
Cohesion: 0.21
Nodes (9): alpha_max(), BaseGraphicalLasso, _dual_gap(), _graphical_lasso(), graphical_lasso_path(), GraphicalLasso, GraphicalLassoCV, _objective() (+1 more)

### Community 285 - "Community 285"
Cohesion: 0.15
Nodes (12): c_step(), _consistency_factor(), fast_mcd(), Robust location and covariance estimators.  Here are implemented estimators that, Multiplicative factor to make covariance estimate consistent     at the normal d, Finds the best pure subset of observations to compute MCD from it.      The purp, Estimate the Minimum Covariance Determinant matrix.      Read more in the :ref:`, C_step procedure described in [Rouseeuw1984]_ aiming at computing MCD.      Para (+4 more)

### Community 286 - "Community 286"
Cohesion: 0.13
Nodes (10): __array_namespace_info__, Array API Inspection namespace  This is the namespace for inspection functions a, The default device used for new CuPy arrays.          See Also         --------, The default data types used for new CuPy arrays.          For CuPy, this always, # TODO: Does this depend on device?, The array API data types supported by CuPy.          Note that this function onl, # TODO: Does this depend on device?, Get the array API inspection namespace for CuPy.      The array API inspection n (+2 more)

### Community 287 - "Community 287"
Cohesion: 0.17
Nodes (5): fastica(), _gs_decorrelation(), _ica_def(), _ica_par(), _sym_decorrelation()

### Community 288 - "Community 288"
Cohesion: 0.13
Nodes (3): LegacyVersion, parse(), Parse the given version from a string to an appropriate class.      Parameters

### Community 289 - "Community 289"
Cohesion: 0.20
Nodes (2): _BaseEncoder, OrdinalEncoder

### Community 290 - "Community 290"
Cohesion: 0.16
Nodes (15): RuntimeError, _cg(), _check_optimize_result(), _line_search_wolfe1(), _line_search_wolfe12(), _LineSearchError, _newton_cg(), Our own implementation of the Newton algorithm  Unlike the scipy.optimize versio (+7 more)

### Community 291 - "Community 291"
Cohesion: 0.13
Nodes (6): Test that FeatureHasher has requires_fit=False tag., Test that FeatureHasher can transform without fitting., FeatureHasher raises error when a sample is a single string.      Non-regression, test_feature_hasher_requires_fit_tag(), test_feature_hasher_single_string(), test_feature_hasher_transform_without_fit()

### Community 292 - "Community 292"
Cohesion: 0.13
Nodes (2): Check `get_feature_names_out` for `BernoulliRBM`., test_feature_names_out()

### Community 293 - "Community 293"
Cohesion: 0.13
Nodes (5): Testing for Spectral Clustering methods, Check that spectral_clustering raises an informative error when passed     an np, Check that discretize raises LinAlgError when svd never converges.      Non-regr, test_spectral_clustering_not_infinite_loop(), test_spectral_clustering_np_matrix_raises()

### Community 294 - "Community 294"
Cohesion: 0.16
Nodes (8): Create a progress bar for the task and update the list of ordered tasks., Update the progress of the task and its ancestors recursively., A task, i.e. progressbar, in the tree of rich tasks.      There is a rich task f, Return the fraction of the task that is completed., Return a formatted description for the task., Return the descendants from this task along the given path., Pre-order depth-first traversal, only including tasks with a progress bar., RichTask

### Community 295 - "Community 295"
Cohesion: 0.13
Nodes (10): add_js_css_files(), infer_next_release_versions(), make_carousel_thumbs(), Load additional JS and CSS files only for certain pages.      Note that `html_js, Reset sklearn config to default values., produces the final resized carousel images, Skip properties that are fitted attributes, Infer the most likely next release versions to make. (+2 more)

### Community 296 - "Community 296"
Cohesion: 0.19
Nodes (10): ArffEncoder, dump(), dumps(), Serialize an object representing the ARFF document to a given file-like     obje, Serialize an object representing the ARFF document, returning a string.      :pa, (INTERNAL) Encodes a comment line.          Comments are single line strings sta, (INTERNAL) Decodes a relation line.          The relation declaration is a line, (INTERNAL) Encodes an attribute line.          The attribute follow the template (+2 more)

### Community 297 - "Community 297"
Cohesion: 0.25
Nodes (2): _assign_where(), IterativeImputer

### Community 298 - "Community 298"
Cohesion: 0.19
Nodes (7): _gradient_descent(), _joint_probabilities(), _joint_probabilities_nn(), _kl_divergence(), _kl_divergence_bh(), trustworthiness(), TSNE

### Community 299 - "Community 299"
Cohesion: 0.13
Nodes (8): __array_namespace_info__, Array API Inspection namespace  This is the namespace for inspection functions a, The default device used for new NumPy arrays.          For NumPy, this always re, The default data types used for new NumPy arrays.          For NumPy, this alway, The array API data types supported by NumPy.          Note that this function on, The devices supported by NumPy.          For NumPy, this always returns ``['cpu', Get the array API inspection namespace for NumPy.      The array API inspection, Return a dictionary of array API library capabilities.          The resulting di

### Community 300 - "Community 300"
Cohesion: 0.18
Nodes (10): _check_boundary_response_method(), DecisionBoundaryDisplay, _deprecate_multiclass_colors(), Decisions boundary visualization.      It is recommended to use     :func:`~skle, Validate the response methods to be used with the fitted estimator.      Paramet, Plot visualization.          Parameters         ----------         plot_method :, Plot decision boundary given an estimator.          Read more in the :ref:`User, Handle deprecation of `multiclass_colors` renamed to `target_colors`. (+2 more)

### Community 302 - "Community 302"
Cohesion: 0.13
Nodes (3): generate_valid_param(), Return a value that does satisfy a constraint.      This is only useful for test, ValueError

### Community 303 - "Community 303"
Cohesion: 0.13
Nodes (14): Test that calling fit_transform and fit_predict doesn't call fit., Test that cloning a frozen estimator keeps the frozen state., Test that check_is_fitted works on frozen estimators., Test that frozen estimators have the same tags as the original estimator     exc, Test that FrozenEstimator only exposes the estimator parameter., Test that frozen.fit doesn't do anything, and that all other methods are     exp, Test that metadata routing works with frozen estimators., test_check_is_fitted() (+6 more)

### Community 304 - "Community 304"
Cohesion: 0.13
Nodes (2): Testing for mean shift clustering methods, # TODO: remove mark once loky bug is fixed:

### Community 305 - "Community 305"
Cohesion: 0.13
Nodes (6): Check that `mutual_info_classif` and `mutual_info_regression` are     symmetric, Check that results agree when X is integer dtype and float dtype.      Non-regre, Check that results are consistent with different `n_jobs`., test_mutual_info_n_jobs(), test_mutual_info_regression_X_int_dtype(), test_mutual_information_symmetry_classif_regression()

### Community 306 - "Community 306"
Cohesion: 0.14
Nodes (9): get_warning_filters(), Check warning propagates to the job., Check that warnings filters are set correctly in the threading backend., Informative warnings should be raised when mixing sklearn and joblib API, Check that we properly dispatch the configuration in parallel processing.      N, test_check_warnings_threading(), test_dispatch_config_parallel(), test_filter_warning_propagates() (+1 more)

### Community 307 - "Community 307"
Cohesion: 0.13
Nodes (15): get_iris_dataset(), test_auto_weight(), test_decision_function(), test_decision_function_shape(), test_hasattr_predict_proba(), test_immutable_coef_property(), test_liblinear_set_coef(), test_libsvm_iris() (+7 more)

### Community 308 - "Community 308"
Cohesion: 0.13
Nodes (1): Test truncated SVD transformer.

### Community 309 - "Community 309"
Cohesion: 0.18
Nodes (15): check_same_namespace(), _cholesky(), get_namespace_and_device(), _is_numpy_namespace(), _linalg_solve(), _matching_numpy_dtype(), _modify_in_place_if_numpy(), _nanmax() (+7 more)

### Community 310 - "Community 310"
Cohesion: 0.17
Nodes (15): check_estimator(), _check_name(), estimator_checks_generator(), _maybe_mark(), _raise_for_missing_tags(), _should_be_skipped_or_marked(), _yield_all_checks(), _yield_api_checks() (+7 more)

### Community 311 - "Community 311"
Cohesion: 0.14
Nodes (8): __array_namespace_info__, Array API Inspection namespace  This is the namespace for inspection functions a, The default device used for new Dask arrays.          For Dask, this always retu, The default data types used for new Dask arrays.          For Dask, this always, The array API data types supported by Dask.          Note that this function onl, The devices supported by Dask.          For Dask, this always returns ``['cpu',, Get the array API inspection namespace for Dask.      The array API inspection n, Return a dictionary of array API library capabilities.          The resulting di

### Community 312 - "Community 312"
Cohesion: 0.14
Nodes (5): Benchmark, Benchmarks for t-SNE., TSNEBenchmark, PairwiseDistancesBenchmark, Benchmarks for pairwise distances.

### Community 313 - "Community 313"
Cohesion: 0.21
Nodes (13): get_canonical_name_git_grep(), get_canonical_name_meson(), get_git_grep_info(), get_meson_info(), has_openmp_flags(), has_source_openmp_flags(), main(), Check that OpenMP dependencies are correctly defined in meson.build files.  This (+5 more)

### Community 314 - "Community 314"
Cohesion: 0.30
Nodes (4): _CFNode, _CFSubcluster, _iterate_sparse_X(), _split_node()

### Community 315 - "Community 315"
Cohesion: 0.19
Nodes (13): calinski_harabasz_score(), check_number_of_labels(), davies_bouldin_score(), Unsupervised evaluation metrics., Accumulate silhouette statistics for vertical chunk of X.      Parameters     --, Compute the Silhouette Coefficient for each sample.      The Silhouette Coeffici, Check that number of labels are valid.      Parameters     ----------     n_labe, Compute the Calinski and Harabasz score.      It is also known as the Variance R (+5 more)

### Community 316 - "Community 316"
Cohesion: 0.18
Nodes (10): _ledoit_wolf(), ledoit_wolf_shrinkage(), LedoitWolf, Covariance estimators using shrinkage.  Shrinkage corresponds to regularising `c, Estimate the shrunk Ledoit-Wolf covariance matrix.      Read more in the :ref:`U, Estimate the shrunk Ledoit-Wolf covariance matrix., # TODO: gh-33986 discusses the idea of automatically determining the best, Estimate the shrunk Ledoit-Wolf covariance matrix.      Read more in the :ref:`U (+2 more)

### Community 317 - "Community 317"
Cohesion: 0.29
Nodes (12): _laplace(), _laplace_normed(), _laplace_normed_sym(), _laplace_sym(), laplacian(), _laplacian_dense(), _laplacian_dense_flo(), _laplacian_sparse_flo() (+4 more)

### Community 318 - "Community 318"
Cohesion: 0.16
Nodes (4): asarray(), isin(), Array API compatibility wrapper for asarray().      See the corresponding docume, searchsorted()

### Community 319 - "Community 319"
Cohesion: 0.21
Nodes (13): _liac_arff_parser(), load_arff_from_gzip_file(), _pandas_arff_parser(), _post_process_frame(), Implementation of ARFF parsers: via LIAC-ARFF and pandas., ARFF parser using the LIAC-ARFF library coded purely in Python.      This parser, Obtains several columns from sparse ARFF representation. Additionally,     the c, ARFF parser using `pandas.read_csv`.      This parser uses the metadata fetched (+5 more)

### Community 320 - "Community 320"
Cohesion: 0.20
Nodes (13): _download_20newsgroups(), fetch_20newsgroups(), fetch_20newsgroups_vectorized(), Caching loader for the 20 newsgroups text classification dataset.   The descript, Given text in "news" format, strip the headers, by removing everything     befor, Given text in "news" format, strip lines beginning with the quote     characters, Given text in "news" format, attempt to remove a signature block.      As a roug, Load the filenames and data from the 20 newsgroups dataset \ (classification). (+5 more)

### Community 321 - "Community 321"
Cohesion: 0.14
Nodes (13): DecisionTreeClassifier, test_clone_protocol(), test_feature_names_in(), test_feature_names_in_on_dataframes(), test_get_fitted_attr_html(), test_pickle_version_no_warning_is_issued_with_non_sklearn_estimator(), test_pickle_version_warning_is_issued_upon_different_version(), test_pickle_version_warning_is_issued_when_no_version_info_in_pickle() (+5 more)

### Community 322 - "Community 322"
Cohesion: 0.15
Nodes (7): object, cve_role(), IssueRole, A Sphinx extension for linking to your project's issue tracker.  Copyright 2014, Sphinx role for linking to a user profile. Defaults to linking to     Github pro, Sphinx role for linking to a CVE on https://cve.mitre.org.     Examples: ::, user_role()

### Community 323 - "Community 323"
Cohesion: 0.20
Nodes (2): FunctionTransformer, _identity()

### Community 324 - "Community 324"
Cohesion: 0.14
Nodes (12): Check that named constructors return the correct type when subclassed.      Non-, Check the behaviour of `_check_boundary_response_method` for the supported     c, Check multiclass `response=predict` gives expected results., Check input validation from_estimator., # TODO: Remove version check and the else branch once 3.10 is the minimal, # TODO: Remove version check and the else branch once 3.10 is the minimal, Check that `n_classes` is set correctly.      Introduced in https://github.com/s, test_check_boundary_response_method() (+4 more)

### Community 325 - "Community 325"
Cohesion: 0.15
Nodes (12): check_l1_min_c(), Test that `bounded_rand_int_wrap` is defined for unsigned 32bits ints, Test that bounded_rand_int_wrap without seeding respects the range      Note thi, Test that `set_seed` produces deterministic results, Test that `set_seed_wrap` is defined for unsigned 32bits ints, Test that `bounded_rand_int` follows a uniform distribution, test_l1_min_c(), test_newrand_bounded_rand_int() (+4 more)

### Community 326 - "Community 326"
Cohesion: 0.26
Nodes (12): _numpy_to_cython(), test_asum(), test_axpy(), test_copy(), test_dot(), test_gemm(), test_gemv(), test_ger() (+4 more)

### Community 327 - "Community 327"
Cohesion: 0.14
Nodes (1): test the label propagation module

### Community 329 - "Community 329"
Cohesion: 0.20
Nodes (7): assert_1d_reg_monotonic(), assert_1d_reg_tree_children_monotonic_bounded(), assert_nd_reg_tree_children_monotonic_bounded(), test_1d_tree_nodes_values(), test_assert_1d_reg_tree_children_monotonic_bounded(), test_assert_nd_reg_tree_children_monotonic_bounded(), test_nd_tree_nodes_values()

### Community 330 - "Community 330"
Cohesion: 0.16
Nodes (4): brute_force_neighbors(), compute_kernel_slow(), test_kernel_density(), test_nn_tree_query()

### Community 331 - "Community 331"
Cohesion: 0.14
Nodes (12): Check the behaviour of `subsample`., Check that we can pass an axis to the display., Check that we can tune the style of the line and the scatter., Check that we raise the proper error when making the parameters     # validation, Check that we raise a `NotFittedError` when the passed regressor is not     fit., Check the default behaviour of the display., test_from_estimator_not_fitted(), test_plot_prediction_error_ax() (+4 more)

### Community 332 - "Community 332"
Cohesion: 0.14
Nodes (8): __array_namespace_info__, Array API Inspection namespace  This is the namespace for inspection functions a, The default data types used for new PyTorch arrays.          Parameters, Get the array API inspection namespace for PyTorch.      The array API inspectio, The array API data types supported by PyTorch.          Note that this function, The devices supported by PyTorch.          Returns         -------         devic, Return a dictionary of array API library capabilities.          The resulting di, The default device used for new PyTorch arrays.          See Also         ------

### Community 333 - "Community 333"
Cohesion: 0.14
Nodes (6): _Booleans, _InstancesOf, Constraint representing instances of a given type.      Parameters     ---------, Constraint representing boolean likes.      Convenience class for     [bool, np., Helper constraint for the verbose parameter.      Convenience class for     [Int, _VerboseHelper

### Community 334 - "Community 334"
Cohesion: 0.17
Nodes (7): _BasePCA, IncrementalPCA, Incremental Principal Components Analysis., Incremental principal components analysis (IPCA).      Linear dimensionality red, Fit the model with X, using minibatches of size batch_size.          Parameters, Incremental fit with X. All of X is processed as a single batch.          Parame, Apply dimensionality reduction to X.          X is projected on the first princi

### Community 335 - "Community 335"
Cohesion: 0.18
Nodes (8): clear_tmp(), get_estimator_path(), get_from_config(), Get benchmarks configuration from the config.json file, Get path of pickled fitted estimator, Clean the tmp directory, track_same_prediction(), track_same_transform()

### Community 336 - "Community 336"
Cohesion: 0.15
Nodes (4): HistGradientBoostingClassifierBenchmark, RandomForestClassifierBenchmark, Benchmarks for RandomForestClassifier., Benchmarks for HistGradientBoostingClassifier.

### Community 337 - "Community 337"
Cohesion: 0.15
Nodes (8): _from_reconstruction_attributes(), get_context_path(), Helper to call the hook of all callbacks with their respective arguments., Call the `on_fit_task_begin` hook of the callbacks.          Parameters, Call the `on_fit_task_end` hook of the callbacks.          Parameters         --, Propagate the context and callbacks to a sub-estimator.          Clear the propa, Return a copy of the estimator as if it was fitted.      Parameters     --------, Helper function to get the path from the root context down to a given context.

### Community 338 - "Community 338"
Cohesion: 0.21
Nodes (5): _fit_and_score_cv(), ============================================== Supporting callbacks in third par, score_func(), SimpleGridSearch, SimpleKMeans

### Community 339 - "Community 339"
Cohesion: 0.29
Nodes (11): cluster_optics_dbscan(), cluster_optics_xi(), _compute_core_distances_(), compute_optics_graph(), _correct_predecessor(), _extend_region(), _extract_xi_labels(), _set_reach_dist() (+3 more)

### Community 340 - "Community 340"
Cohesion: 0.26
Nodes (8): ArffContainerType, Data, _DataListMixin, _get_data_object_for_decoding(), _get_data_object_for_encoding(), LODData, LODGeneratorData, Mixin to return a list from decode_rows instead of a generator

### Community 341 - "Community 341"
Cohesion: 0.21
Nodes (8): Reduce X to the selected features., Reverse the transformation operation.          Parameters         ----------, Mask feature names according to selected features.          Parameters         -, Transformer mixin that performs feature selection given a support mask.      Thi, Get a mask, or integer index, of the features selected.          Parameters, Get the boolean mask indicating which features are selected          Returns, Reduce X to the selected features.          Parameters         ----------, SelectorMixin

### Community 342 - "Community 342"
Cohesion: 0.15
Nodes (2): ========================================================== Comparison of kernel, ============================================= Comparison of kernel ridge regress

### Community 343 - "Community 343"
Cohesion: 0.18
Nodes (4): csr_set_problem(), csr_to_sparse(), dense_to_sparse(), set_problem()

### Community 344 - "Community 344"
Cohesion: 0.17
Nodes (10): _compute_precision_cholesky(), _compute_precision_cholesky_from_precisions(), _estimate_gaussian_parameters(), _flipudlr(), Estimate the Gaussian distribution parameters.      Parameters     ----------, Compute the Cholesky decomposition of the precisions.      Parameters     ------, Reverse the rows and columns of an array., r"""Compute the Cholesky decomposition of precisions using precisions themselves (+2 more)

### Community 345 - "Community 345"
Cohesion: 0.22
Nodes (1): LocalOutlierFactor

### Community 346 - "Community 346"
Cohesion: 0.21
Nodes (6): PrecisionRecallDisplay, Precision Recall visualization.      It is recommended to use     :func:`~sklear, Plot visualization.          Parameters         ----------         ax : Matplotl, Plot precision-recall curve given an estimator and some data.          For gener, Plot precision-recall curve given binary class predictions.          For general, Plot multi-fold precision-recall curves given cross-validation results.

### Community 347 - "Community 347"
Cohesion: 0.21
Nodes (6): Plot visualization.          Parameters         ----------         ax : matplotl, ROC Curve visualization.      It is recommended to use     :func:`~sklearn.metri, Create a ROC Curve display from an estimator.          For general information r, Plot ROC curve given the true and predicted values.          For general informa, Create a multi-fold ROC curve display given cross-validation results.          ., RocCurveDisplay

### Community 348 - "Community 348"
Cohesion: 0.15
Nodes (13): load_iris_2d_scaled(), Test renaming of `multiclass_colors_` attribute.      Check that FutureWarning i, Check input validation for `target_colors` in `from_estimator`., Check plot correct when plotting max multiclass class., Check behaviour if `n_classes` can't be inferred.      Non-regression test for i, Check the handling logic for `cmap` and `colors`., Check that using `multiclass_colors` raises as expected., test_cmap_and_colors_logic() (+5 more)

### Community 349 - "Community 349"
Cohesion: 0.18
Nodes (5): _assert_check_unknown(), When both np.nan and float("nan") are present, they get merged into np.nan., test_check_unknown(), test_check_unknown_missing_values(), test_get_counts_multiple_nans()

### Community 350 - "Community 350"
Cohesion: 0.15
Nodes (13): check_label_quality(), Tests that HDBSCAN works with sparse distance matrices., Tests that HDBSCAN works with feature array, including an arbitrary     goodness, Tests that HDBSCAN works with the expected combinations of algorithms and     me, Tests that HDBSCAN can generate a sufficiently accurate dbscan clustering.     T, Tests that HDBSCAN using `BallTree` works., Tests that HDBSCAN works with precomputed distance matrices, and throws the, test_dbscan_clustering() (+5 more)

### Community 351 - "Community 351"
Cohesion: 0.19
Nodes (12): check_playwright(), local_server(), _make_page(), Skip tests if playwright is not installed.      This fixture is used by the next, Test that forceTheme applies the right theme class to the element.      A light, Test that copyFeatureNamesToClipboard copies the right text to the clipboard., Start a simple HTTP server that serves custom HTML per test.      Usage :      `, Helper to create an HTML page that includes `estimator.js` and the given body. (+4 more)

### Community 352 - "Community 352"
Cohesion: 0.18
Nodes (3): check_results(), compute_kernel_slow(), test_kernel_density()

### Community 353 - "Community 353"
Cohesion: 0.15
Nodes (13): _monkey_patch_webbased_functions(), Check that we raise the expected error for sparse ARFF datasets and     a wrong, Check that we raise a warning regarding the working memory when using     LIAC-A, Check that we raise the proper errors when we require pandas., test_convert_arff_data_dataframe_warning_low_memory_pandas(), test_dataset_with_openml_error(), test_dataset_with_openml_warning(), test_fetch_openml_cache() (+5 more)

### Community 354 - "Community 354"
Cohesion: 0.15
Nodes (13): Test that data passed to validation callback correctly subsets.      Non-regress, SGDClassifier(), test_l1_ratio(), test_large_regularization(), test_multi_core_gridsearch_and_early_stopping(), test_multi_thread_multi_class_and_early_stopping(), test_numerical_stability_large_gradient(), test_sgd_error_on_zero_validation_weight() (+5 more)

### Community 355 - "Community 355"
Cohesion: 0.17
Nodes (6): _assert_categories_equals_bitset(), Check that allowed_features are respected., Check that feature_fraction_per_split is respected.      Because we set `n_featu, test_split_feature_fraction_per_split(), test_split_interaction_constraints(), test_splitting_categorical_sanity()

### Community 356 - "Community 356"
Cohesion: 0.23
Nodes (11): centrality_scores(), get_adjacency_matrix(), get_redirects(), index(), =============================== Wikipedia principal eigenvector ================, Extract the adjacency graph as a scipy sparse matrix      Redirects are resolved, Power iteration computation of the principal eigenvector      This method is als, Find the index of an article name after redirect resolution (+3 more)

### Community 357 - "Community 357"
Cohesion: 0.18
Nodes (11): create_or_update_comment(), find_lint_bot_comments(), get_message(), get_step_message(), get_versions(), Get the versions of the packages used in the linter job.      Parameters     ---, Get the comment from the linting bot., Create a new comment or update the existing linting comment. (+3 more)

### Community 358 - "Community 358"
Cohesion: 0.23
Nodes (7): _Progress, Time column with millisecond precision and color styling., Percentage column with color styling., _StyledPercentageColumn, _StyledTimeRemainingColumn, TextColumn, TimeRemainingColumn

### Community 359 - "Community 359"
Cohesion: 0.17
Nodes (4): Restore state, opening a fresh listener if the inherited one is unusable., Retrieve the logged scores.          Log entries are grouped by runs, which are, Callback that monitors a score for each iterative step of an estimator.      The, ScoringMonitor

### Community 360 - "Community 360"
Cohesion: 0.24
Nodes (2): FactorAnalysis, _ortho_rotation()

### Community 361 - "Community 361"
Cohesion: 0.30
Nodes (1): KernelPCA

### Community 362 - "Community 362"
Cohesion: 0.17
Nodes (6): CustomEstimator, ======================================== `__sklearn_is_fitted__` as Developer AP, Fit the estimator to the training data., Perform Predictions          If the estimator is not fitted, then raise NotFitte, Calculate Score          If the estimator is not fitted, then raise NotFittedErr, Check fitted status and return a Boolean value.

### Community 363 - "Community 363"
Cohesion: 0.20
Nodes (6): Score functions, performance metrics, pairwise metrics and distance computations, PredictionErrorDisplay, Visualization of the prediction error of a regression model.      This tool can, Plot the prediction error given a regressor and some data.          For general, Plot the prediction error given the true and predicted targets.          For gen, Plot visualization.          Extra keyword arguments will be passed to matplotli

### Community 364 - "Community 364"
Cohesion: 0.17
Nodes (6): ModuleLevelDocumenter, Allow documenting any object., Override default behavior to add no directive header or options., Override default behavior to add only the first line of the docstring., An autodocumenter that only renders the short summary of the object., ShortSummaryDocumenter

### Community 365 - "Community 365"
Cohesion: 0.18
Nodes (6): FunctionDoc, ObjDoc, Extract reference documentation from the NumPy source tree., Remove leading and trailing blank lines from a list of lines, # NOTE: param line with single element should never have a, strip_blank_lines()

### Community 366 - "Community 366"
Cohesion: 0.17
Nodes (2): NegativeInfinityType, Vendoered from https://github.com/pypa/packaging/blob/main/packaging/_structures

### Community 367 - "Community 367"
Cohesion: 0.23
Nodes (9): _cmpkey(), InvalidVersion, _legacy_cmpkey(), _parse_letter_version(), _parse_local_version(), _parse_version_parts(), Vendored from https://github.com/pypa/packaging/blob/main/packaging/version.py, Takes a string like abc.1.twelve and turns it into ("abc", 1, "twelve"). (+1 more)

### Community 368 - "Community 368"
Cohesion: 0.24
Nodes (9): brute_force_neighbors(), get_dataset_for_binary_tree(), Check that we do not accept object dtype array., test_array_object_type(), test_ball_tree_numerical_consistency(), test_ball_tree_query_metrics(), test_kernel_density_numerical_consistency(), test_query_haversine() (+1 more)

### Community 369 - "Community 369"
Cohesion: 0.17
Nodes (11): MyEstimator, test_clone_dict(), test_clone_empty_array(), test_clone_estimator_types(), test_clone_nan(), test_clone_sparse_matrices(), test_get_params_html(), test_n_features_in_no_validation() (+3 more)

### Community 370 - "Community 370"
Cohesion: 0.26
Nodes (9): Retain every `step` features (beginning with 0).      If `step < 1`, then no fea, Check output dtypes for dataframes is consistent with the input dtypes., StepSelector, test_get_support(), test_inverse_transform_dense(), test_inverse_transform_sparse(), test_output_dataframe(), test_transform_dense() (+1 more)

### Community 371 - "Community 371"
Cohesion: 0.21
Nodes (12): Ensure that the returned values of all metrics are consistent.      It can only, Ensure that the returned values of all metrics are consistent.      It can eithe, Make targets strictly positive, Make targets strictly larger than -1, _require_log1p_targets(), _require_positive_targets(), test_format_invariance_with_1d_vectors(), test_not_symmetric_metric() (+4 more)

### Community 372 - "Community 372"
Cohesion: 0.17
Nodes (8): Return the value of assume_finite after waiting `sleep_duration`., Test that the global config is threadsafe with all joblib backends.     Two jobs, Uses threads directly to test that the global config does not change     between, Check error when SciPy is too old, set_assume_finite(), test_config_array_api_dispatch_error_scipy(), test_config_threadsafe(), test_config_threadsafe_joblib()

### Community 373 - "Community 373"
Cohesion: 0.17
Nodes (8): Check the behaviour of `smallest_admissible_index_dtype` using the dtype of the, Check that we raise the proper error message., Check the behaviour of `smallest_admissible_index_dtype` depending only on the, Check the behaviour of `smallest_admissible_index_dtype` using the passed     ar, test_smallest_admissible_index_dtype_by_checking_contents(), test_smallest_admissible_index_dtype_error(), test_smallest_admissible_index_dtype_max_val(), test_smallest_admissible_index_dtype_without_checking_contents()

### Community 374 - "Community 374"
Cohesion: 0.18
Nodes (5): _has_explicit_diagonal(), Return True if the diagonal is explicitly stored, Check `get_feature_names_out` for transformers defined in `_graph.py`., test_explicit_diagonal(), test_graph_feature_names_out()

### Community 375 - "Community 375"
Cohesion: 0.17
Nodes (11): Tests for HDBSCAN clustering algorithm Based on the DBSCAN test code, Tests if np.inf and np.nan data are each treated as special outliers., Tests that HDBSCAN correctly does not generate a valid cluster when the     `min, Test that the smallest non-noise cluster has at least `min_cluster_size`     man, Tests that HDBSCAN correctly raises an error when passing precomputed data     w, Test that HDBSCAN raises a FutureWarning when the `copy`     parameter is not se, test_dbscan_clustering_outlier_data(), test_hdbscan_default_copy_warning() (+3 more)

### Community 376 - "Community 376"
Cohesion: 0.30
Nodes (10): make_regression_with_outliers(), test_huber_and_sgd_same_results(), test_huber_better_r2_score(), test_huber_equals_lr_for_high_epsilon(), test_huber_gradient(), test_huber_max_iter(), test_huber_sample_weights(), test_huber_scaling_invariant() (+2 more)

### Community 377 - "Community 377"
Cohesion: 0.17
Nodes (5): mock_data_home(), This test for the LFW require medium-size data downloading and processing  If th, Check that we properly crop the images.      Non-regression test for:     https:, Test fixture run once and common to all tests of this module, test_fetch_lfw_people_internal_cropping()

### Community 378 - "Community 378"
Cohesion: 0.17
Nodes (5): _MockHTTPResponse, Check that the md5 checksum is enforced and a corrupted download retried.      T, test_fetch_openml_verify_checksum(), test_open_openml_url_cache(), test_open_openml_url_retry_on_network_error()

### Community 379 - "Community 379"
Cohesion: 0.29
Nodes (6): make_simple_dataset(), NaiveSplitter, powerset(), returns all the subsets of `iterable` of length len(iterable) - 1., test_split_impurity(), to_categorical()

### Community 380 - "Community 380"
Cohesion: 0.21
Nodes (11): is_df_or_series(), is_pandas_df_or_series(), is_polars_df(), is_polars_df_or_series(), is_pyarrow_data(), Functions to determine if an object is a dataframe or series., Return True if the X is a dataframe or series.      Parameters     ----------, Return True if the X is a pandas dataframe or series.      Parameters     ------ (+3 more)

### Community 382 - "Community 382"
Cohesion: 0.22
Nodes (6): _BinaryClassifierCurveDisplayMixin, DetCurveDisplay, Plot DET curve given an estimator and data.          For general information reg, Detection Error Tradeoff (DET) curve visualization.      It is recommended to us, Plot the DET curve given the true and predicted labels.          For general inf, Plot visualization.          Parameters         ----------         ax : matplotl

### Community 383 - "Community 383"
Cohesion: 0.24
Nodes (8): get(), get_contributors(), get_profile(), key(), This script generates an html table of contributors, with names and avatars. The, Get the GitHub profile from login, Get a sorting key based on the lower case last name, then firstname, Get the list of contributor profiles. Require admin rights.

### Community 384 - "Community 384"
Cohesion: 0.20
Nodes (10): can_reuse_listener(), close_listener(), ListenerHandle, open_listener(), Stop listening for `listener_handle` and free its background threads., Whether the listener at `listener_handle` is usable from this process.      Help, Deliver `message` to whoever is listening on `listener_handle`.      There are t, A picklable reference to a main-process listener.      Attributes     ---------- (+2 more)

### Community 385 - "Community 385"
Cohesion: 0.33
Nodes (6): barycenter_kneighbors_graph(), barycenter_weights(), _locally_linear_embedding(), LocallyLinearEmbedding, null_space(), _UnstableArchMixin

### Community 386 - "Community 386"
Cohesion: 0.18
Nodes (6): BaseOptimizer, Stochastic optimization methods for MLP, Base (Stochastic) gradient descent optimizer      Parameters     ----------, Update parameters with given gradients          Parameters         ----------, Perform update to learning rate and potentially other states at the         end, Decides whether it is time to stop training          Parameters         --------

### Community 387 - "Community 387"
Cohesion: 0.20
Nodes (4): asarray(), count_nonzero(), # NOTE: this is currently incorrectly typed in numpy, but will be fixed in, Array API compatibility wrapper for asarray().      See the corresponding docume

### Community 388 - "Community 388"
Cohesion: 0.18
Nodes (10): Check that we properly strip double quotes from the data., Check that we properly parse with no quotes characters., Check the behaviour of the post-processing function for splitting a dataframe., An error will be raised if the parser is not known., Check that we properly strip single quotes from the data., test_load_arff_from_gzip_file_error_parser(), test_pandas_arff_parser_strip_double_quotes(), test_pandas_arff_parser_strip_no_quotes() (+2 more)

### Community 389 - "Community 389"
Cohesion: 0.20
Nodes (8): Convert estimator attributes to ndarray., Check validation of non-array input against fitted attribute ``X_``.      ``Simp, SimpleEstimator, test_check_fitted_attribute(), test_check_fitted_attribute_with_non_array_input(), test_convert_estimator_to_array_api_strict(), test_convert_estimator_to_ndarray(), test_convert_estimator_with_custom_logic()

### Community 390 - "Community 390"
Cohesion: 0.25
Nodes (8): filter_errors(), Pretty print original docstring and the obtained errors      Parameters     ----, Check function docstrings using numpydoc., # TODO: this detection can be improved. Currently we assume that we have, Ignore some errors based on the method type.      These rules are specific for s, repr_errors(), test_docstring(), test_function_docstring()

### Community 391 - "Community 391"
Cohesion: 0.18
Nodes (5): Check that we do not accept object dtype array., # TODO: remove mark once loky bug is fixed:, Make sure that KDTree queries work when joblib memmaps.      Non-regression test, test_array_object_type(), test_kdtree_picklable_with_joblib()

### Community 392 - "Community 392"
Cohesion: 0.25
Nodes (9): check_pyproject_sections(), extract_packages_and_pyproject_tags(), Tests for the minimum dependencies in README.rst and pyproject.toml, Check versions in pyproject.toml is consistent with _min_dependencies., Test the version check for matching packages., Test the version check for non-matching packages and versions., test_check_matching_pyproject_section(), test_check_non_matching_pyproject_section() (+1 more)

### Community 393 - "Community 393"
Cohesion: 0.31
Nodes (7): assert_children_values_bounded(), assert_children_values_monotonic(), assert_leaves_values_monotonic(), is_decreasing(), is_increasing(), test_nodes_values(), test_predictions()

### Community 394 - "Community 394"
Cohesion: 0.20
Nodes (11): _generate_test_params_for(), _parse_metric(), Helper function for properly building a type-specialized DistanceMetric instance, Return list of DistanceMetric kwargs for tests., test_kneighbors_brute_backend(), test_neigh_predictions_algorithm_agnosticity(), test_neighbors_metrics(), test_radius_neighbors_brute_backend() (+3 more)

### Community 395 - "Community 395"
Cohesion: 0.18
Nodes (5): datasets_column_names(), Test the openml loader., Check the auto mode of `fetch_openml`., Returns the columns names for each dataset., test_fetch_openml_auto_mode()

### Community 396 - "Community 396"
Cohesion: 0.29
Nodes (5): MyPerceptron, Check that `l1_ratio` has an impact when `penalty='elasticnet'`, test_perceptron_accuracy(), test_perceptron_correctness(), test_perceptron_l1_ratio()

### Community 397 - "Community 397"
Cohesion: 0.18
Nodes (8): An estimator with the callback registered but not yet fitted is picklable., An estimator with the callback registered and fitted is picklable., An estimator with callbacks survives an in-process pickle round-trip.      It al, An estimator with callbacks survives unpickling in a fresh interpreter.      It, test_callbacks_refit_after_load_in_fresh_process(), test_callbacks_refit_after_pickle_in_same_process(), test_estimator_with_callback_pickle_roundtrip_post_fit(), test_estimator_with_callback_pickle_roundtrip_pre_fit()

### Community 398 - "Community 398"
Cohesion: 0.20
Nodes (4): launch_mcd_on_dataset(), Check that MinCovDet does not underestimate the empirical     variance on Gaussi, test_mcd(), test_mincovdet_bias_on_normal()

### Community 399 - "Community 399"
Cohesion: 0.27
Nodes (8): assert_csr_equal_values(), _dense_dataset_factories(), _fused_types_dataset_factories(), _make_dense_dataset(), _make_sparse_dataset(), _sparse_dataset_factories(), test_seq_dataset_basic_iteration(), test_seq_dataset_shuffle()

### Community 400 - "Community 400"
Cohesion: 0.18
Nodes (8): Test that when not np.ndarray, we don't touch the array., Test that attach_unique returns a view of the array., Test return_tuple argument of the function., Test that check_array keeps the unique metadata., test_attach_unique_not_ndarray(), test_attach_unique_return_tuple(), test_attach_unique_returns_view(), test_check_array_keeps_unique()

### Community 401 - "Community 401"
Cohesion: 0.20
Nodes (8): _AutoJITWrapper, pickle_flatten(), pickle_unflatten(), Use the pickle machinery to extract objects out of an arbitrary container., Reverse of ``pickle_flatten``.      Parameters     ----------     instances : It, Helper of :func:`jax_autojit`.      Wrap arbitrary inputs and outputs of the jit, Return wrapped object., Register upon first use instead of at import time, to avoid         globally imp

### Community 402 - "Community 402"
Cohesion: 0.18
Nodes (6): _Constraint, _PandasNAConstraint, Base class for the constraint objects., Whether or not a value satisfies the constraint.          Parameters         ---, A human readable representational string of the constraint., Constraint representing the indicator `pd.NA`.

### Community 403 - "Community 403"
Cohesion: 0.42
Nodes (9): benchmark(), fixed_batch_size_comparison(), plot_batch_errors(), plot_batch_times(), plot_feature_errors(), plot_feature_times(), plot_results(), ======================== IncrementalPCA benchmark ========================  Benc (+1 more)

### Community 404 - "Community 404"
Cohesion: 0.24
Nodes (5): bench(), bench_one(), get_loss(), get_max_squared_sum(), Get the maximum row-wise sum of squares

### Community 405 - "Community 405"
Cohesion: 0.20
Nodes (7): bhtsne(), load_data(), nn_accuracy(), ============================= MNIST dataset T-SNE benchmark ====================, Wrapper for the reference lvdmaaten/bhtsne implementation., Load the data, then cache and memmap the train/test split, Accuracy of the first nearest neighbor

### Community 406 - "Community 406"
Cohesion: 0.24
Nodes (9): construct_grids(), fetch_species_distributions(), _load_coverage(), _load_csv(), ============================= Species distribution dataset =====================, Construct the map grid from the batch object      Parameters     ----------, Loader for species distribution dataset from Phillips et. al. (2006).      Read, Load a coverage file from an open file object.      This will return a numpy arr (+1 more)

### Community 407 - "Community 407"
Cohesion: 0.24
Nodes (5): BadObject, COOData, encode_string(), Error raised when the object representing the ARFF file has something     wrong., (INTERNAL) Encodes a line of data.          Data instances follow the csv format

### Community 408 - "Community 408"
Cohesion: 0.22
Nodes (6): Backend, Backends against which array-api-extra runs its tests., All array library backends explicitly tested by array-api-extra.      Parameters, Module name to be imported., Check if this backend uses the same module as others., Backend as a pytest parameter.          Returns         -------         pytest.m

### Community 409 - "Community 409"
Cohesion: 0.27
Nodes (3): info(), trcg(), TRON()

### Community 410 - "Community 410"
Cohesion: 0.24
Nodes (5): Initialization of the mixture parameters.          Parameters         ----------, Estimate the parameters of the Dirichlet distribution.          Parameters, Estimate the parameters of the Gaussian distribution.          Parameters, Estimate the precisions parameters of the precision distribution.          Param, M step.          Parameters         ----------         X : array-like of shape (

### Community 411 - "Community 411"
Cohesion: 0.20
Nodes (5): KNeighborsClassifier, Fit the k-nearest neighbors classifier from the training dataset.          Param, Predict the class labels for the provided data.          Parameters         ----, Return the mean accuracy on the given test data and labels.          In multi-la, Classifier implementing the k-nearest neighbors vote.      Read more in the :ref

### Community 412 - "Community 412"
Cohesion: 0.22
Nodes (1): NeighborhoodComponentsAnalysis

### Community 413 - "Community 413"
Cohesion: 0.20
Nodes (6): RadiusNeighborsRegressor, Nearest Neighbor Regression., Regression based on neighbors within a fixed radius.      The target is predicte, Fit the radius neighbors regressor from the training dataset.          Parameter, Predict the target for the provided data.          Parameters         ----------, RadiusNeighborsMixin

### Community 414 - "Community 414"
Cohesion: 0.20
Nodes (1): InfinityType

### Community 415 - "Community 415"
Cohesion: 0.24
Nodes (5): ConfusionMatrixDisplay, Plot visualization.          Parameters         ----------         include_value, Confusion Matrix visualization.      It is recommended to use     :func:`~sklear, Plot Confusion Matrix given an estimator and some data.          For general inf, Plot Confusion Matrix given true and predicted labels.          For general info

### Community 416 - "Community 416"
Cohesion: 0.33
Nodes (1): QuantileTransformer

### Community 417 - "Community 417"
Cohesion: 0.20
Nodes (6): All minimum dependencies for scikit-learn., Tests for dataframe detection functions., Check is_polars_df for object that looks like a polars dataframe, Check that is_polars_df return False for non-dataframe objects., test_is_polars_df(), test_is_polars_df_for_duck_typed_polars_dataframe()

### Community 418 - "Community 418"
Cohesion: 0.20
Nodes (3): Test the 20news downloader, if the data is available, or if specifically request, Checks the length consistencies within the bunch      This is a non-regression t, test_20news_length_consistency()

### Community 419 - "Community 419"
Cohesion: 0.20
Nodes (3): Check get_feature_names_out for LocallyLinearEmbedding., # TODO: rewrite this test to make less sensitive to the random seed,, test_get_feature_names_out()

### Community 420 - "Community 420"
Cohesion: 0.20
Nodes (1): This is testing the equivalence between some estimators with internal nearest ne

### Community 421 - "Community 421"
Cohesion: 0.20
Nodes (10): Test that the `offset_` of `SGDOneClassSVM` is close to the `offset_`     of `On, Check that SGDOneClassSVM has the correct estimator type.      Non-regression te, Test that SGDOneClassSVM minimizes the correct objective function., SGDOneClassSVM(), test_ocsvm_vs_sgdocsvm(), test_sgd_one_class_svm_estimator_type(), test_sgd_one_class_svm_formulation_with_scipy_minimize(), test_sgd_oneclass_convergence() (+2 more)

### Community 422 - "Community 422"
Cohesion: 0.20
Nodes (4): SGDRegressor(), _SparseSGDOneClassSVM, _SparseSGDRegressor, _update_kwargs()

### Community 423 - "Community 423"
Cohesion: 0.20
Nodes (8): bitset_to_tuple(), Split, test_2d_y(), test_cross_validator_with_default_params(), test_shuffle_kfold_stratifiedkfold_reproducibility(), test_shuffle_split_empty_trainset(), test_stratified_kfold_ratios(), test_stratifiedkfold_balance()

### Community 424 - "Community 424"
Cohesion: 0.24
Nodes (7): PassthroughTransformer, Check behavior of check_feature_names_in for arrays., test_check_array_links_to_imputer_doc_only_for_X(), test_check_feature_names_in(), test_check_is_fitted(), test_check_is_fitted_with_attributes(), test_check_is_fitted_with_is_fitted()

### Community 425 - "Community 425"
Cohesion: 0.27
Nodes (5): _assert_predictor_equal(), Assert that two HistGBM instances are identical., test_warm_start_clear(), test_warm_start_equal_n_estimators(), test_warm_start_yields_identical_results()

### Community 426 - "Community 426"
Cohesion: 0.24
Nodes (9): axis0_safe_slice(), _get_dense_mask(), _get_mask(), indices_to_mask(), Return a mask which is safer to use on X than safe_mask.      This mask is safer, Convert list of indices to boolean mask.      Parameters     ----------     indi, Compute the boolean mask X == value_to_mask.      Parameters     ----------, Return an indexing mask compatible with X.      Parameters     ----------     X (+1 more)

### Community 427 - "Community 427"
Cohesion: 0.27
Nodes (9): _get_response_values(), _get_response_values_binary(), _process_decision_function(), _process_predict_proba(), Utilities to get the response values of a classifier or a regressor.  It allows, Compute the response values of a classifier, an outlier detector, a regressor, Get the response values when the response method is `predict_proba`.      This f, Compute the response values of a binary classifier.      Parameters     -------- (+1 more)

### Community 428 - "Community 428"
Cohesion: 0.20
Nodes (5): ignore_warnings(), _IgnoreWarnings, Improved and simplified Python warnings context manager and decorator.      This, Decorator to catch and hide warnings without visual nesting., Context manager and decorator to ignore warnings.      Note: Using this (in both

### Community 429 - "Community 429"
Cohesion: 0.22
Nodes (2): MinimalClassifier, Minimal classifier implementation without inheriting from BaseEstimator.      Th

### Community 430 - "Community 430"
Cohesion: 0.22
Nodes (7): benchmark_influence(), generate_data(), plot_influence(), ========================== Model Complexity Influence ==========================, Benchmark influence of `changing_param` on both MSE and latency., Plot influence of model complexity on both accuracy and latency., Generate regression/classification data.

### Community 431 - "Community 431"
Cohesion: 0.22
Nodes (3): The :mod:`sklearn.callback` module implements the framework and off the shelf ca, ProgressBar, Callback that displays progress bars for each iterative step of an estimator.

### Community 432 - "Community 432"
Cohesion: 0.22
Nodes (3): _classifier_has(), InductiveClusterer, Check if we can delegate a method to the underlying classifier.      First, we c

### Community 433 - "Community 433"
Cohesion: 0.22
Nodes (6): Methods and algorithms to robustly estimate covariance.  They estimate the covar, Calculate covariance matrices shrunk on the diagonal.      Read more in the :ref, Covariance estimator with shrinkage.      Read more in the :ref:`User Guide <shr, Fit the shrunk covariance model to X.          Parameters         ----------, shrunk_covariance(), ShrunkCovariance

### Community 434 - "Community 434"
Cohesion: 0.22
Nodes (2): DiscriminantAnalysisPredictionMixin, NearestCentroid

### Community 435 - "Community 435"
Cohesion: 0.22
Nodes (4): BadNominalValue, EncodedNominalConversor, NominalConversor, Error raised when a value in used in some data instance but is not     declared

### Community 436 - "Community 436"
Cohesion: 0.22
Nodes (2): Transformers for missing value imputation., KNNImputer

### Community 437 - "Community 437"
Cohesion: 0.31
Nodes (2): _dynamic_max_trials(), RANSACRegressor

### Community 438 - "Community 438"
Cohesion: 0.22
Nodes (7): _SetOutputMixin, EstimatorNoSetOutputWithTransformNoFeatureNamesOut, EstimatorWithSetOutputNoAutoWrap, Estimator without get_feature_names_out does not define `set_output`., Check that auto_wrap_output_keys=None does not wrap., test_get_output_auto_wrap_false(), test_set_output_mixin()

### Community 439 - "Community 439"
Cohesion: 0.28
Nodes (1): _BaseChain

### Community 440 - "Community 440"
Cohesion: 0.25
Nodes (4): OneTimeSplitter, Common utilities for testing model selection., A wrapper to make KFold single entry cv iterator, Split can be called only once

### Community 441 - "Community 441"
Cohesion: 0.28
Nodes (5): mkchi2(), Tests for chi2, currently the only feature selection function designed specifica, Make k-best chi2 selector, test_chi2(), test_chi2_coo()

### Community 442 - "Community 442"
Cohesion: 0.22
Nodes (3): Test  kddcup99 loader, if the data is available, or if specifically requested vi, Check that a nice error message is raised when cache is corrupted., test_corrupted_file_error_message()

### Community 443 - "Community 443"
Cohesion: 0.31
Nodes (4): check_edge_case_of_sample_int(), check_sample_int(), check_sample_int_distribution(), test_sample_without_replacement_algorithms()

### Community 444 - "Community 444"
Cohesion: 0.22
Nodes (8): Check that we raise an error if the sparse format is not CSR., Check that the operation is happening inplace., Check that we get the same results for dense and sparse implementation., Check that the computation preserve dtype thanks to fused types., test_mutual_reachability_graph_equivalence_dense_sparse(), test_mutual_reachability_graph_error_sparse_format(), test_mutual_reachability_graph_inplace(), test_mutual_reachability_graph_preserves_dtype()

### Community 445 - "Community 445"
Cohesion: 0.22
Nodes (9): _make_sparse_offset_regression(), Check that ridge finds the same coefs and intercept on dense and sparse input, test_ridge_fit_intercept_sparse(), test_ridge_fit_intercept_sparse_error(), test_ridge_fit_intercept_sparse_sag(), test_ridge_gcv_sample_weights(), test_ridge_gcv_vs_ridge_loo_cv(), test_ridge_loo_cv_asym_scoring() (+1 more)

### Community 446 - "Community 446"
Cohesion: 0.22
Nodes (8): chunk_generator(), gen_batches(), gen_even_slices(), get_chunk_n_rows(), Calculate how many rows can be processed within `working_memory`.      Parameter, Chunk generator, ``gen`` into lists of length ``chunksize``. The last     chunk, Generator to create slices containing `batch_size` elements from 0 to `n`., Generator to create `n_packs` evenly spaced slices going up to `n`.      If `n_p

### Community 447 - "Community 447"
Cohesion: 0.22
Nodes (7): all_displays(), all_estimators(), all_functions(), Utilities to discover scikit-learn objects., Get a list of all displays from `sklearn`.      Returns     -------     displays, Get a list of all functions from `sklearn`.      Returns     -------     functio, Get a list of all estimators from `sklearn`.      This function crawls the modul

### Community 448 - "Community 448"
Cohesion: 0.22
Nodes (9): check_classifier_data_not_an_array(), check_classifiers_regression_target(), check_estimators_data_not_an_array(), check_estimators_unfitted(), check_regressor_data_not_an_array(), check_regressors_int(), check_regressors_train(), check_transformers_unfitted() (+1 more)

### Community 449 - "Community 449"
Cohesion: 0.22
Nodes (9): _check_generated_dataframe(), check_global_output_transform_pandas(), check_global_set_output_transform_polars(), _check_set_output_transform_dataframe(), check_set_output_transform_pandas(), _check_set_output_transform_pandas_context(), check_set_output_transform_polars(), _check_set_output_transform_polars_context() (+1 more)

### Community 450 - "Community 450"
Cohesion: 0.22
Nodes (4): _CVObjects, _IterablesNotString, Constraint representing iterables that are not strings., Constraint representing cv objects.      Convenient class for     [         Inte

### Community 451 - "Community 451"
Cohesion: 0.22
Nodes (4): _NoneConstraint, _RandomStates, Constraint representing the None singleton., Constraint representing random states.      Convenience class for     [Interval(

### Community 452 - "Community 452"
Cohesion: 0.22
Nodes (7): Wrapper used by `_SetOutputMixin` to automatically wrap methods., Mixin that dynamically wraps methods to return container based on config.      C, Set output container.          Refer to the :ref:`user guide <df_output_transfor, Safely call estimator.set_output and error if it not available.      This is use, _safe_set_output(), _SetOutputMixin, _wrap_method_output()

### Community 453 - "Community 453"
Cohesion: 0.22
Nodes (6): create_memmap_backed_data(), _delete_folder(), Utility function to cleanup a temporary folder if still existing.      Copy from, Parameters     ----------     data     mmap_mode : str, default='r', Parameters     ----------     data     mmap_mode : str, default='r'     return_f, TempMemmap

### Community 454 - "Community 454"
Cohesion: 0.22
Nodes (2): MinimalRegressor, Minimal regressor implementation without inheriting from BaseEstimator.      Thi

### Community 455 - "Community 455"
Cohesion: 0.25
Nodes (2): MinimalTransformer, Minimal transformer implementation without inheriting from     BaseEstimator.

### Community 456 - "Community 456"
Cohesion: 0.32
Nodes (7): construct_grids(), create_species_bunch(), plot_species_distribution(), ============================= Species distribution modeling ====================, Plot the species distribution., Construct the map grid from the batch object      Parameters     ----------, Create a bunch with information about a particular organism      This will use t

### Community 457 - "Community 457"
Cohesion: 0.32
Nodes (7): build_projection_operator(), _generate_center_coordinates(), generate_synthetic_data(), ====================================================================== Compressi, Compute the tomography design matrix.      Parameters     ----------      l_x :, Synthetic binary data, _weights()

### Community 458 - "Community 458"
Cohesion: 0.32
Nodes (4): explained_variance_ratio(), make_dict_learning_scorers(), make_pca_scorers(), neg_mean_data_error()

### Community 459 - "Community 459"
Cohesion: 0.32
Nodes (7): _fetch_brute_kddcup99(), fetch_kddcup99(), _mkdirp(), KDDCUP 99 dataset.  A classic dataset for anomaly detection.  The dataset page i, Load the kddcup99 dataset, downloading it if necessary.      Parameters     ----, Ensure directory d exists (like mkdir -p on Unix)     No guarantee that the dire, Load the kddcup99 dataset (classification).      Download it if necessary.

### Community 460 - "Community 460"
Cohesion: 0.32
Nodes (7): fetch_rcv1(), _find_permutation(), _inverse_permutation(), RCV1 dataset.  The dataset page is available at      http://jmlr.csail.mit.edu/p, Load the RCV1 multilabel dataset (classification).      Download it if necessary, Inverse permutation p., Find the permutation from a to b.

### Community 461 - "Community 461"
Cohesion: 0.43
Nodes (7): _compute_mi(), _compute_mi_cc(), _compute_mi_cd(), _estimate_mi(), _iterate_columns(), mutual_info_classif(), mutual_info_regression()

### Community 462 - "Community 462"
Cohesion: 0.25
Nodes (8): angle(), default_dtype(), nunique(), Return the default dtype for the given namespace and device.      This is a conv, Count the number of unique elements in an array.      Compatible with JAX and Da, See docstring in `array_api_extra._delegation.py`., Return the angle of the complex argument.      Parameters     ----------     z :, searchsorted()

### Community 463 - "Community 463"
Cohesion: 0.25
Nodes (8): atleast_nd(), cov(), expand_dims(), kron(), See docstring in array_api_extra._delegation., See docstring in array_api_extra._delegation., See docstring in array_api_extra._delegation., See docstring in array_api_extra._delegation.

### Community 464 - "Community 464"
Cohesion: 0.29
Nodes (3): ClassicalMDS, Classical multi-dimensional scaling (classical MDS)., Compute and return the embedding positions.          Parameters         --------

### Community 465 - "Community 465"
Cohesion: 0.32
Nodes (2): Data embedding techniques., SpectralEmbedding

### Community 466 - "Community 466"
Cohesion: 0.29
Nodes (1): Isomap

### Community 467 - "Community 467"
Cohesion: 0.39
Nodes (3): MDS, smacof(), _smacof_single()

### Community 468 - "Community 468"
Cohesion: 0.29
Nodes (6): _log_dirichlet_norm(), _log_wishart_norm(), Bayesian Gaussian Mixture Model., Compute the log of the Dirichlet distribution normalization term.      Parameter, Compute the log of the Wishart distribution normalization term.      Parameters, Estimate the lower bound of the model.          The lower bound on the likelihoo

### Community 469 - "Community 469"
Cohesion: 0.25
Nodes (1): _BaseVersion

### Community 471 - "Community 471"
Cohesion: 0.39
Nodes (6): _construct_compose_pipeline_instance(), _construct_searchcv_instance(), _construct_sparse_coder(), _get_all_fitted_attributes(), Get all the fitted attributes of an estimator including properties, test_fit_docstring_attributes()

### Community 472 - "Community 472"
Cohesion: 0.25
Nodes (8): Check regularization limits of _RidgeGCV (alpha near 0 or inf), Expected coef and intercept when alpha near 0 or inf, Check regularization limits of Ridge (alpha near 0 or inf), Check regularization limits of RidgeClassifierCV (alpha near 0 or inf), _ridge_regularization_limits(), test_regularization_limits_ridge(), test_regularization_limits_ridge_classifier_gcv(), test_regularization_limits_ridge_gcv()

### Community 474 - "Community 474"
Cohesion: 0.32
Nodes (4): available_if(), _AvailableIfDescriptor, An attribute that is available only if check returns a truthy value.      Parame, Implements a conditional property using the descriptor protocol.      Using this

### Community 475 - "Community 475"
Cohesion: 0.29
Nodes (2): _BaseComposition, Base class for estimators that are composed of named sub-estimators.      This a

### Community 476 - "Community 476"
Cohesion: 0.32
Nodes (7): _get_deps_info(), _get_sys_info(), Utility methods to print system info for debugging  adapted from :func:`pandas.s, System information      Returns     -------     sys_info : dict         system a, Overview of the installed version of main dependencies      This function does n, Print useful debugging information.      .. versionadded:: 0.20      Examples, show_versions()

### Community 477 - "Community 477"
Cohesion: 0.25
Nodes (8): assert_docstring_consistency(), _check_consistency_items(), _check_item_included(), _get_diff_msg(), Helper to check if item should be included in checking., Get message showing the difference between type/desc docstrings of all objects., Helper to check docstring consistency of all `items_docs`.      If item is not p, r"""Check consistency between docstring parameters/attributes/returns of objects

### Community 478 - "Community 478"
Cohesion: 0.33
Nodes (4): # TODO: use the QR wrapper once dask, # TODO: can't avoid computing U or V for dask, svd(), svdvals()

### Community 479 - "Community 479"
Cohesion: 0.29
Nodes (3): bench_isotonic_regression(), Benchmarks of isotonic regression performance.  We generate a synthetic dataset, Runs a single iteration of isotonic regression on the input data,     and report

### Community 480 - "Community 480"
Cohesion: 0.33
Nodes (2): bench_scikit_transformer(), compute_time()

### Community 481 - "Community 481"
Cohesion: 0.48
Nodes (6): _dump_svmlight(), dump_svmlight_file(), _gen_open(), load_svmlight_file(), load_svmlight_files(), _open_and_load()

### Community 482 - "Community 482"
Cohesion: 0.52
Nodes (6): get_current_dependencies_version(), get_current_min_python_version(), get_min_python_version(), get_min_version_pure_python_or_example_dependency(), get_min_version_with_wheel(), show_versions_update()

### Community 483 - "Community 483"
Cohesion: 0.29
Nodes (3): load_mnist(), NMSlibTransformer, ===================================== Approximate nearest neighbors in TSNE ====

### Community 484 - "Community 484"
Cohesion: 0.38
Nodes (1): KernelDensity

### Community 485 - "Community 485"
Cohesion: 0.29
Nodes (1): StandardScaler

### Community 486 - "Community 486"
Cohesion: 0.29
Nodes (4): DropdownAnchorAdder, Run the post transformation., Insert anchor links to the sphinx-design dropdowns.      Some of the dropdowns w, SphinxPostTransform

### Community 487 - "Community 487"
Cohesion: 0.29
Nodes (3): DfOutTransformer, Check that we properly rename columns when using `ColumnTransformer` and     sel, test_column_transformer_column_renaming()

### Community 488 - "Community 488"
Cohesion: 0.29
Nodes (5): DoubleTrans, test_column_transformer_drops_all_remainder_transformer(), test_column_transformer_no_remaining_remainder_transformer(), test_column_transformer_remainder_transformer(), test_n_features_in()

### Community 489 - "Community 489"
Cohesion: 0.29
Nodes (3): PandasOutTransformer, Check that set_config(transform="pandas") is compatible with more transformers., test_transformers_with_pandas_out_but_not_feature_names_out()

### Community 490 - "Community 490"
Cohesion: 0.29
Nodes (4): SparseMatrixTrans, test_column_transformer_drop_all_sparse_remainder_transformer(), test_column_transformer_sparse_remainder_transformer(), test_column_transformer_sparse_stacking()

### Community 491 - "Community 491"
Cohesion: 0.29
Nodes (7): _check_output(), Check `y_true` and `sample_weight` follows `y_pred` for mixed namespace inputs., Check string inputs accepted with array API dispatch enabled.      All threshold, Check string inputs and numeric inputs from mixed namespace and devices accepted, test_array_api_classification_mixed_string_numeric_input(), test_array_api_classification_string_input(), test_mixed_array_api_namespace_input_compliance()

### Community 492 - "Community 492"
Cohesion: 0.29
Nodes (7): _check_statistics(), Utility function for testing imputation for a given strategy.      Test with den, safe_mean(), safe_median(), test_imputation_mean_median(), test_imputation_median_special_cases(), test_imputation_most_frequent()

### Community 494 - "Community 494"
Cohesion: 0.29
Nodes (4): Test that newton_cg works with Array API input., Test the std output of verbose newton_cg solver., test_newton_cg_array_api_compliance(), test_newton_cg_verbosity()

### Community 495 - "Community 495"
Cohesion: 0.29
Nodes (7): asgd(), test_average_binary_computed_correctly(), test_average_sparse(), test_late_onset_averaging_reached(), test_sgd_averaged_computed_correctly(), test_sgd_averaged_partial_fit(), test_sgd_multiclass_average()

### Community 497 - "Community 497"
Cohesion: 0.29
Nodes (7): array_device(), _bincount(), Hardware device where the array data resides on., Hardware device where the array data resides on.      If the hardware device is, Filter arrays to exclude None and/or specific types.      Sparse arrays are alwa, _remove_non_arrays(), _single_array_device()

### Community 498 - "Community 498"
Cohesion: 0.33
Nodes (7): _convert_to_numpy(), _is_xp_namespace(), _max_precision_float_dtype(), move_to(), Convert X into a NumPy ndarray on the CPU.      This function uses library-speci, Move all arrays to `xp` and `device`.      Each array will be moved to the refer, Return the float dtype with the highest precision supported by the device.

### Community 499 - "Community 499"
Cohesion: 0.29
Nodes (6): check_matplotlib_support(), check_pandas_support(), check_rich_support(), Raise ImportError with detailed error message if pandas is not installed.      P, Raise ImportError with detailed error message if rich is not installed.      Cal, Raise ImportError with detailed error message if mpl is not installed.      Plot

### Community 500 - "Community 500"
Cohesion: 0.29
Nodes (6): _attach_unique(), _cached_unique(), Attach unique values of y to y and return the result.      The result is a view, Attach unique values of ys to ys and return the results.      The result is a vi, Return the unique values of y.      Use the cached values from dtype.metadata if, Return the unique values of ys.      Use the cached values from dtype.metadata i

### Community 501 - "Community 501"
Cohesion: 0.33
Nodes (4): clone_module(), get_xp(), Decorator to automatically replace xp with the corresponding array module., Import everything from module, updating globals().     Returns __all__.

### Community 502 - "Community 502"
Cohesion: 0.40
Nodes (4): bench(), get_data(), ========================================== IsolationForest prediction benchmark, Function based on code from: https://scikit-learn.org/stable/     auto_examples/

### Community 503 - "Community 503"
Cohesion: 0.33
Nodes (1): Benchmark SGD prediction time with dense/sparse coefficients.  Invoke with -----

### Community 504 - "Community 504"
Cohesion: 0.33
Nodes (5): bench_scikit_tree_classifier(), bench_scikit_tree_regressor(), To run this, you'll need to have installed.    * scikit-learn  Does two benchmar, Benchmark with scikit-learn decision tree classifier, Benchmark with scikit-learn decision tree regressor

### Community 505 - "Community 505"
Cohesion: 0.33
Nodes (2): GradientBoostingClassifierBenchmark, Benchmarks for GradientBoostingClassifier.

### Community 506 - "Community 506"
Cohesion: 0.33
Nodes (2): LinearRegressionBenchmark, Benchmarks for Linear Regression.

### Community 507 - "Community 507"
Cohesion: 0.33
Nodes (2): LogisticRegressionBenchmark, Benchmarks for LogisticRegression.

### Community 508 - "Community 508"
Cohesion: 0.33
Nodes (3): Private constructor to create a sub-context.          Parameters         -------, Add `child_context` as a child of this context., Create a context for a subtask of the current task.          Parameters

### Community 509 - "Community 509"
Cohesion: 0.33
Nodes (5): _oas(), Estimate covariance with the Oracle Approximating Shrinkage algorithm.      The, Estimate covariance with the Oracle Approximating Shrinkage.      Read more in t, Oracle Approximating Shrinkage Estimator.      Read more in the :ref:`User Guide, Fit the Oracle Approximating Shrinkage covariance model to X.          Parameter

### Community 510 - "Community 510"
Cohesion: 0.40
Nodes (5): =========================================== Sparse coding with a precomputed dic, Discrete sub-sampled Ricker (Mexican hat) wavelet, Dictionary of Ricker (Mexican hat) wavelets, ricker_function(), ricker_matrix()

### Community 511 - "Community 511"
Cohesion: 0.40
Nodes (2): Directive, AllowNanEstimators

### Community 512 - "Community 512"
Cohesion: 0.33
Nodes (5): _get_guide(), _get_submodule(), Configuration for the API reference documentation., Get the submodule docstring and automatically add the hook.      `module_name` i, Get the rst to refer to user/developer guide.      `refs` is several references

### Community 513 - "Community 513"
Cohesion: 0.40
Nodes (5): main(), make_distributor_init_64_bits(), Embed vcomp140.dll and msvcp140.dll., Create a _distributor_init.py file for 64-bit architectures.      This file is i, Embed vcomp140.dll and msvcp140.dll.

### Community 514 - "Community 514"
Cohesion: 0.33
Nodes (5): f(), g(), =================================== Polynomial and Spline interpolation ========, Function to be approximated by periodic spline interpolation., Function to be approximated by polynomial interpolation.

### Community 515 - "Community 515"
Cohesion: 0.33
Nodes (5): _average_binary_score(), _average_multiclass_ovo_score(), Common code for all metrics., Average one-versus-one scores for multiclass classification.      Uses the binar, Average a binary metric for multilabel classification.      Parameters     -----

### Community 516 - "Community 516"
Cohesion: 0.40
Nodes (5): print_dataframe(), ============================================================ Custom refit strate, Pretty print for filtered dataframe, Define the strategy to select the best estimator.      The strategy defined here, refit_strategy()

### Community 517 - "Community 517"
Cohesion: 0.40
Nodes (5): best_low_complexity(), lower_bound(), ================================================== Balance model complexity and, Calculate the lower bound within 1 standard deviation     of the best `mean_test, Balance model complexity with cross-validated score.      Parameters     -------

### Community 518 - "Community 518"
Cohesion: 0.40
Nodes (5): compute_corrected_ttest(), corrected_std(), ================================================== Statistical comparison of mod, Corrects standard deviation using Nadeau and Bengio's approach.      Parameters, Computes right-tailed paired t-test with corrected variance.      Parameters

### Community 519 - "Community 519"
Cohesion: 0.33
Nodes (3): Normalize, MidpointNormalize, ================== RBF SVM parameters ==================  This example illustrat

### Community 520 - "Community 520"
Cohesion: 0.53
Nodes (1): ClassDoc

### Community 521 - "Community 521"
Cohesion: 0.33
Nodes (4): levenshtein_distance(), Return the smallest absolute value of a 1D array., Return the Levenshtein distance between two strings., smallest_abs()

### Community 522 - "Community 522"
Cohesion: 0.40
Nodes (5): generate_link_to_param_doc(), get_docstring(), URL to the relevant section of the docstring using a Text Fragment      https://, Extract and format docstring information for a specific item.      Parses the es, scrape_estimator_docstring()

### Community 523 - "Community 523"
Cohesion: 0.40
Nodes (5): _get_git_revision(), _linkcode_resolve(), make_linkcode_resolve(), Determine a link to online source for a class/method/function      This is calle, Returns a linkcode_resolve function for the given URL format      revision is a

### Community 524 - "Community 524"
Cohesion: 0.33
Nodes (4): test_column_transformer_empty_columns(), test_column_transformer_error_msg_1D(), test_column_transformer_output_indices(), TransRaise

### Community 526 - "Community 526"
Cohesion: 0.33
Nodes (3): EstimatorWithListInput, Check set_output for list input.      Non-regression test for #27037., test_set_output_list_input()

### Community 527 - "Community 527"
Cohesion: 0.33
Nodes (3): EstimatorWithSetOutputIndex, Check that set_output does not override index.      Non-regression test for gh-2, test_set_output_pandas_keep_index()

### Community 528 - "Community 528"
Cohesion: 0.33
Nodes (2): _SparseSGDClassifier, test_sgd_proba()

### Community 529 - "Community 529"
Cohesion: 0.33
Nodes (6): test_gradient_squared_hinge(), _test_loss_common(), test_loss_epsilon_insensitive(), test_loss_hinge(), test_loss_modified_huber(), test_loss_squared_epsilon_insensitive()

### Community 530 - "Community 530"
Cohesion: 0.33
Nodes (6): check_cv_coverage(), check_valid_split(), test_kfold_indices(), test_kfold_valueerrors(), test_shuffle_groupkfold(), test_shuffle_stratifiedkfold()

### Community 531 - "Community 531"
Cohesion: 0.33
Nodes (3): test_no___sklearn_tags__with_more_tags(), test_tags_no_sklearn_tags_concrete_implementation(), test_type_error_is_thrown_for_class_vs_instance()

### Community 533 - "Community 533"
Cohesion: 0.33
Nodes (6): _add_to_diagonal(), _fill_diagonal(), Validate arguments to `_fill_diagonal`/`_add_to_diagonal`., Minimal implementation of `numpy.fill_diagonal`.      `wrap` is not supported (i, Add `value` to diagonal of `array`.      Related to `fill_diagonal`. `value` sho, _validate_diagonal_args()

### Community 534 - "Community 534"
Cohesion: 0.40
Nodes (5): compute_class_weight(), compute_sample_weight(), Utilities for handling weights based on class labels., Estimate sample weights by class for unbalanced datasets.      Parameters     --, Estimate class weights for unbalanced datasets.      Parameters     ----------

### Community 535 - "Community 535"
Cohesion: 0.33
Nodes (5): _fix_connected_components(), Graph utilities and algorithms., Return the length of the shortest path from source to all reachable nodes., Add connections to sparse graph to connect unconnected components.      For each, single_source_shortest_path_length()

### Community 536 - "Community 536"
Cohesion: 0.33
Nodes (3): Convert type into human readable string., Add a deprecated mark to an option if needed., _type_name()

### Community 537 - "Community 537"
Cohesion: 0.40
Nodes (2): n(), s()

### Community 538 - "Community 538"
Cohesion: 0.70
Nodes (4): get_file_extension(), get_file_size(), human_readable_data_quantity(), json_urlread()

### Community 539 - "Community 539"
Cohesion: 0.60
Nodes (4): fixed_classes_uniform_labelings_scores(), random_labels(), ========================================================== Adjustment for chance, uniform_labelings_scores()

### Community 540 - "Community 540"
Cohesion: 0.80
Nodes (4): _check_fetch_lfw(), _fetch_lfw_pairs(), _fetch_lfw_people(), _load_imgs()

### Community 541 - "Community 541"
Cohesion: 0.40
Nodes (1): =============================================================== Model selection

### Community 542 - "Community 542"
Cohesion: 0.40
Nodes (2): Sort example gallery by title of subsection.      Assumes README.txt exists for, SubSectionTitleOrder

### Community 543 - "Community 543"
Cohesion: 0.50
Nodes (4): cv_estimate(), heldout_score(), ====================================== Gradient Boosting Out-of-Bag estimates ==, compute deviance scores on ``X_test`` and ``y_test``.

### Community 544 - "Community 544"
Cohesion: 0.40
Nodes (3): Set the parameters of this kernel.          The method works on simple kernels a, Returns the (flattened, log-transformed) non-fixed hyperparameters.          Not, Sets the (flattened, log-transformed) non-fixed hyperparameters.          Parame

### Community 545 - "Community 545"
Cohesion: 0.40
Nodes (4): _check_feature_names(), _get_feature_index(), Get feature index.      Parameters     ----------     fx : int or str         Fe, Check feature names.      Parameters     ----------     X : array-like of shape

### Community 546 - "Community 546"
Cohesion: 0.70
Nodes (4): _calculate_permutation_scores(), _create_importances_bunch(), permutation_importance(), _weights_scorer()

### Community 547 - "Community 547"
Cohesion: 0.40
Nodes (5): apply_where(), isclose(), Helper of `apply_where`. On Dask, this runs on a single chunk., See docstring in array_api_extra._delegation., Run one of two elementwise functions depending on a condition.      Equivalent t

### Community 548 - "Community 548"
Cohesion: 0.60
Nodes (4): close_issue_if_opened(), create_or_update_issue(), get_issue(), Creates or updates an issue if the CI fails. This is useful to keep track of sch

### Community 549 - "Community 549"
Cohesion: 0.50
Nodes (3): add_2d_scatter(), plot_2d(), ========================================= Comparison of Manifold Learning method

### Community 550 - "Community 550"
Cohesion: 0.70
Nodes (4): _graph_connected_component(), _graph_is_connected(), _set_diag(), spectral_embedding()

### Community 551 - "Community 551"
Cohesion: 0.40
Nodes (3): make_estimator(), ========================================== Evaluation of outlier detection estim, Create an outlier detection estimator based on its name.

### Community 552 - "Community 552"
Cohesion: 0.40
Nodes (4): _compute_log_det_cholesky(), _estimate_log_gaussian_prob(), Compute the log-det of the Cholesky decomposition of matrices.      Parameters, Estimate the log Gaussian probability.      Parameters     ----------     X : ar

### Community 553 - "Community 553"
Cohesion: 0.40
Nodes (3): plot_cv_indices(), Visualizing cross-validation behavior in scikit-learn ==========================, Create a sample plot for indices of a cross-validation object.

### Community 554 - "Community 554"
Cohesion: 0.40
Nodes (4): Kernel Density Estimation -------------------------, # TODO: implement sampling for other valid kernel shapes, # TODO: implement a brute force version for testing purposes, # TODO: create a density estimation base class?

### Community 556 - "Community 556"
Cohesion: 0.40
Nodes (1): KernelCenterer

### Community 557 - "Community 557"
Cohesion: 0.60
Nodes (4): create_axes(), make_plot(), plot_distribution(), ============================================================= Compare the effect

### Community 558 - "Community 558"
Cohesion: 0.50
Nodes (4): _params_html_repr(), Categorizes parameters as 'default' or 'user-set' and formats their values., Generate HTML representation of estimator parameters.      Creates an HTML table, _read_params()

### Community 559 - "Community 559"
Cohesion: 0.40
Nodes (3): Compute online update of Gaussian mean and variance.          Given starting sam, Incremental fit on a batch of samples.          This method is expected to be ca, Actual implementation of Gaussian NB fitting.          Parameters         ------

### Community 560 - "Community 560"
Cohesion: 0.40
Nodes (1): doilinks ~~~~~~~~ Extension to add links to DOIs. With this extension you can us

### Community 561 - "Community 561"
Cohesion: 0.40
Nodes (2): SimpleEstimatorCustomLogic, test_custom_conversion_estimator_to_array_api_strict()

### Community 562 - "Community 562"
Cohesion: 0.40
Nodes (5): data_home(), load_files_root(), _remove_dir(), test_category_dir_1(), test_category_dir_2()

### Community 563 - "Community 563"
Cohesion: 0.40
Nodes (1): Test the california_housing loader, if the data is available, or if specifically

### Community 564 - "Community 564"
Cohesion: 0.40
Nodes (2): Check that warning is raised when working_memory is too low., test_get_chunk_n_rows_warns()

### Community 566 - "Community 566"
Cohesion: 0.40
Nodes (3): test_2D_transformer_output(), test_2D_transformer_output_pandas(), TransNo2D

### Community 567 - "Community 567"
Cohesion: 0.40
Nodes (1): # TODO: We are not entirely satisfied with this lax comparison, but the root

### Community 568 - "Community 568"
Cohesion: 0.40
Nodes (1): Test the covtype loader, if the data is available, or if specifically requested

### Community 569 - "Community 569"
Cohesion: 0.40
Nodes (2): 1. Check that an error is raised when both y_score and y_pred are specified., test_y_score_and_y_pred_specified_error()

### Community 570 - "Community 570"
Cohesion: 0.40
Nodes (4): Check docstrings parameters consistency between related classes., Check docstrings parameters consistency between related functions., test_class_docstring_consistency(), test_function_docstring_consistency()

### Community 571 - "Community 571"
Cohesion: 0.40
Nodes (3): Tests for sklearn.cluster._feature_agglomeration, Check `get_feature_names_out` for `FeatureAgglomeration`., test_feature_agglomeration_feature_names_out()

### Community 573 - "Community 573"
Cohesion: 0.40
Nodes (5): check_precomputed(), Tests unsupervised NearestNeighbors with a distance matrix., test_precomputed_dense(), test_precomputed_sparse_knn(), test_precomputed_sparse_radius()

### Community 575 - "Community 575"
Cohesion: 0.80
Nodes (4): _check_function_param_validation(), _get_func_info(), test_class_wrapper_param_validation(), test_function_param_validation()

### Community 576 - "Community 576"
Cohesion: 0.40
Nodes (3): EstimatorReturnTuple, Check that namedtuples are kept by default., test_set_output_named_tuple_out()

### Community 577 - "Community 577"
Cohesion: 0.40
Nodes (5): asgd_oneclass(), test_average_sparse_oneclass(), test_late_onset_averaging_reached_oneclass(), test_sgd_averaged_computed_correctly_oneclass(), test_sgd_averaged_partial_fit_oneclass()

### Community 578 - "Community 578"
Cohesion: 0.40
Nodes (5): _average(), _find_matching_floating_dtype(), _median(), Find a suitable floating point dtype when computing with arrays.      If any of, Partial port of np.average to support the Array API.      It does a best effort

### Community 579 - "Community 579"
Cohesion: 0.40
Nodes (5): _check_array_api_core(), check_array_api_input(), check_array_api_input_and_values(), check_array_api_mixed_inputs(), check_array_api_string_and_numeric_inputs()

### Community 580 - "Community 580"
Cohesion: 0.40
Nodes (4): is_pandas_na(), is_scalar_nan(), Test if x is NaN.      This function is meant to overcome the issue that np.isna, Test if x is pandas.NA.      We intentionally do not use this function to return

### Community 581 - "Community 581"
Cohesion: 0.40
Nodes (4): Compute the weighted percentile.      Implement an array API compatible (weighte, Compute weighted percentiles for sorted 1D data and percentile ranks.      This, _weighted_percentile(), _weighted_percentile_1d_sorted()

### Community 582 - "Community 582"
Cohesion: 0.50
Nodes (4): _message_with_time(), _print_elapsed_time(), Log elapsed time to stdout when the context is exited.      Parameters     -----, Create one line message for logging purposes.      Parameters     ----------

### Community 583 - "Community 583"
Cohesion: 0.50
Nodes (3): plot_digits(), ================================ Image denoising using kernel PCA ==============, Small helper function to plot 100 digits.

### Community 584 - "Community 584"
Cohesion: 0.50
Nodes (1): =========================================== Lagged features for time series fore

### Community 585 - "Community 585"
Cohesion: 0.67
Nodes (3): bench(), To run this, you'll need to have installed.    * glmnet-python   * scikit-learn, rmse()

### Community 587 - "Community 587"
Cohesion: 0.50
Nodes (3): print_outlier_ratio(), ========================================== IsolationForest benchmark ===========, Helper function to show the distinct value count of element in the target.     U

### Community 588 - "Community 588"
Cohesion: 0.67
Nodes (3): barplot_neighbors(), get_data(), Plot the scaling of the nearest neighbors algorithms with k, D, and N

### Community 590 - "Community 590"
Cohesion: 0.67
Nodes (3): bench_sample(), compute_time(), Benchmarks for sampling without replacement of integer.

### Community 591 - "Community 591"
Cohesion: 0.67
Nodes (3): main(), process_tempita(), Process tempita templated file and write out the result.      The template file

### Community 592 - "Community 592"
Cohesion: 0.50
Nodes (2): Merge this context with `other_context`.          This method is called on a sub, Private constructor to create a root context.          Parameters         ------

### Community 593 - "Community 593"
Cohesion: 0.50
Nodes (3): ================================================ Segmenting the picture of greek, # TODO: After #21194 is merged and #21243 is fixed, check which eigen_solver, # TODO: varying eigen_tol seems to have no effect for 'lobpcg' and 'amg' #21243.

### Community 594 - "Community 594"
Cohesion: 0.50
Nodes (3): bench_k_means(), =========================================================== A demo of K-Means cl, Benchmark to evaluate the KMeans initialization methods.      Parameters     ---

### Community 595 - "Community 595"
Cohesion: 0.50
Nodes (3): fetch_california_housing(), California housing dataset.  The original database is available from StatLib, Load the California housing dataset (regression).      ==============   ========

### Community 596 - "Community 596"
Cohesion: 0.50
Nodes (3): fetch_covtype(), Forest covertype dataset.  A classic dataset for classification benchmarks, feat, Load the covertype dataset (classification).      Download it if necessary.

### Community 597 - "Community 597"
Cohesion: 0.50
Nodes (3): fetch_olivetti_faces(), Modified Olivetti faces dataset.  The original database was available from (now, Load the Olivetti faces data-set from AT&T (classification).      Download it if

### Community 598 - "Community 598"
Cohesion: 0.50
Nodes (3): ========================================= Image denoising using dictionary learn, Helper function to display denoising, show_with_diff()

### Community 599 - "Community 599"
Cohesion: 0.50
Nodes (3): Sorts release highlights based on version number., SKExampleTitleSortKey, ExampleTitleSortKey

### Community 600 - "Community 600"
Cohesion: 0.50
Nodes (3): _get_n_samples_bootstrap(), Utility function to get the number of bootstrap samples., Get the number of samples in a bootstrap sample.      Notes     -----     The fr

### Community 601 - "Community 601"
Cohesion: 0.67
Nodes (3): f(), generate(), ============================================================ Single estimator ve

### Community 602 - "Community 602"
Cohesion: 0.50
Nodes (1): ==================================================== Imputing missing values bef

### Community 603 - "Community 603"
Cohesion: 0.50
Nodes (3): Private testing utilities.  See also ..testing for public testing utilities., XFAIL the currently running test.      Unlike ``pytest.xfail``, allow rest of te, xfail()

### Community 604 - "Community 604"
Cohesion: 0.50
Nodes (3): ============================================== Lasso model selection via informa, Rescale the information criterion to follow the definition of Zou et al., zou_et_al_criterion_rescaling()

### Community 605 - "Community 605"
Cohesion: 0.67
Nodes (3): plot_ellipses(), plot_results(), ======================================================================== Concent

### Community 606 - "Community 606"
Cohesion: 0.50
Nodes (3): gmm_bic_score(), ================================ Gaussian Mixture Model Selection ==============, Callable to pass to GridSearchCV that will use the BIC score.

### Community 607 - "Community 607"
Cohesion: 0.50
Nodes (1): ================================= Gaussian Mixture Model Sine Curve ============

### Community 608 - "Community 608"
Cohesion: 0.50
Nodes (3): make_heatmap(), Comparison between grid search and successive halving ==========================, Helper to make a heatmap.

### Community 609 - "Community 609"
Cohesion: 0.50
Nodes (3): ================================================= Outlier detection with Local O, Customize size of the legend marker, update_legend_marker_size()

### Community 610 - "Community 610"
Cohesion: 0.67
Nodes (3): link_thickness_i(), ============================================= Neighborhood Components Analysis I, relate_point()

### Community 611 - "Community 611"
Cohesion: 0.50
Nodes (3): construct_grids(), ================================================ Kernel Density Estimate of Spec, Construct the map grid from the batch object      Parameters     ----------

### Community 612 - "Community 612"
Cohesion: 0.50
Nodes (3): nudge_dataset(), ============================================================== Restricted Boltzm, This produces a dataset 5 times bigger than the original one,     by moving the

### Community 614 - "Community 614"
Cohesion: 0.67
Nodes (3): _fitted_attr_html_repr(), Generate HTML representation of estimator fitted attributes.      Creates an HTM, _read_fitted_attr()

### Community 615 - "Community 615"
Cohesion: 0.50
Nodes (2): override_pst_pagetoc(), Overrides the `generate_toc_html` function of pydata-sphinx-theme for API.

### Community 616 - "Community 616"
Cohesion: 0.50
Nodes (3): l1_min_c(), Determination of parameter bounds, Return the lowest bound for `C`.      The lower bound for `C` is computed such t

### Community 617 - "Community 617"
Cohesion: 0.50
Nodes (3): my_kernel(), ====================== SVM with custom kernel ======================  Simple usa, We create a custom kernel:                   (2  0)     k(X, Y) = X  (    ) Y.T

### Community 618 - "Community 618"
Cohesion: 0.50
Nodes (3): plot_decision_function(), ===================== SVM: Weighted samples =====================  Plot decision, Plot the synthetic data and the classifier decision function. Points with     la

### Community 620 - "Community 620"
Cohesion: 0.50
Nodes (2): _DummyPath, Minimal class that implements the os.PathLike interface.

### Community 621 - "Community 621"
Cohesion: 0.50
Nodes (4): make_estimator_with_param(), test_param_is_default(), test_param_is_non_default(), test_param_is_non_default_when_pandas_NA()

### Community 622 - "Community 622"
Cohesion: 0.50
Nodes (2): SingleInheritanceEstimator, test_pickling_works_when_getstate_is_overwritten_in_the_child_class()

### Community 623 - "Community 623"
Cohesion: 0.50
Nodes (1): Testing for the utility function _get_n_samples_bootstrap

### Community 624 - "Community 624"
Cohesion: 0.50
Nodes (2): Check that Cython extension types have a correct ``__module__``.      When a sub, test_extension_type_module()

### Community 625 - "Community 625"
Cohesion: 0.50
Nodes (4): assert_correct_incr(), test_maxabs_scaler_partial_fit(), test_minmax_scaler_partial_fit(), test_standard_scaler_partial_fit()

### Community 626 - "Community 626"
Cohesion: 0.50
Nodes (4): _check_dim_1axis(), test_maxabs_scaler_1d(), test_min_max_scaler_1d(), test_standard_scaler_1d()

### Community 628 - "Community 628"
Cohesion: 0.50
Nodes (4): _check_fitted_model(), test_all_init(), test_kmeans_copyx(), test_minibatch_kmeans_partial_fit_init()

### Community 629 - "Community 629"
Cohesion: 0.50
Nodes (4): check_object_arrays(), test_k_and_radius_neighbors_duplicates(), test_k_and_radius_neighbors_train_is_not_query(), test_k_and_radius_neighbors_X_None()

### Community 630 - "Community 630"
Cohesion: 0.50
Nodes (2): Test that min_norm_subgradient raises on wrong input., test_min_norm_subgradient_raises()

### Community 631 - "Community 631"
Cohesion: 0.50
Nodes (4): _check_fitted_pca_close(), Check that the results are the same for sparse and dense input., test_pca_sparse(), test_pca_sparse_fit_transform()

### Community 633 - "Community 633"
Cohesion: 0.83
Nodes (3): floyd_warshall_slow(), generate_graph(), test_shortest_path()

### Community 635 - "Community 635"
Cohesion: 0.50
Nodes (2): Check that worst case inputs do not exceed the recursion stack limit., test_simultaneous_sort_no_stackoverflow()

### Community 636 - "Community 636"
Cohesion: 0.50
Nodes (4): _run_answer_test(), test_answer_gradient_four_points(), test_answer_gradient_two_points(), test_skip_num_points_gradient()

### Community 637 - "Community 637"
Cohesion: 0.50
Nodes (2): Klass, Function f          Parameter         ---------         a : int             Para

### Community 638 - "Community 638"
Cohesion: 0.50
Nodes (3): DummyMemory, test_check_memory(), WrongDummyMemory

### Community 639 - "Community 639"
Cohesion: 0.50
Nodes (4): _estimator_with_converted_arrays(), move_estimator_to(), Create a new estimator with converted array attributes.      All attributes that, Move estimator array attributes to the given namespace and device.      Attribut

### Community 640 - "Community 640"
Cohesion: 0.50
Nodes (4): Yield supported namespace.      This is meant to be used for testing purposes on, Yield supported namespace, device_name, dtype_name tuples for testing.      Use, yield_namespace_device_dtype_combinations(), yield_namespaces()

### Community 641 - "Community 641"
Cohesion: 0.50
Nodes (3): _random_choice_csc(), Utilities for random sampling., Generate a sparse random matrix given column class distributions      Parameters

### Community 642 - "Community 642"
Cohesion: 0.50
Nodes (1): ContainerAdaptersManager

### Community 643 - "Community 643"
Cohesion: 0.50
Nodes (4): _check_feature_names_in(), _generate_get_feature_names_out(), Check `input_features` and generate names if needed.      Commonly used in :term, Generate feature names out for estimator using the estimator name as the prefix.

### Community 644 - "Community 644"
Cohesion: 0.50
Nodes (4): _check_feature_names(), _get_feature_names(), Get feature names from X.      Support for other (2d) data containers should pla, Set or check the `feature_names_in_` attribute of an estimator.      .. versiona

### Community 645 - "Community 645"
Cohesion: 0.50
Nodes (4): check_is_fitted(), _is_fitted(), Determine if an estimator is fitted      Parameters     ----------     estimator, Perform is_fitted validation for estimator.      Checks if the estimator is fitt

### Community 646 - "Community 646"
Cohesion: 0.50
Nodes (4): _check_n_features(), _num_features(), Set the `n_features_in_` attribute, or check against it on an estimator.      .., Return the number of features in an array-like X.      This helper function trie

### Community 651 - "Community 651"
Cohesion: 0.67
Nodes (1): Benchmarks of Lasso vs LassoLars  First, we fix a training set and increase the

### Community 653 - "Community 653"
Cohesion: 0.67
Nodes (1): Benchmarks of Lasso regularization path computation using Lars and CD  The input

### Community 654 - "Community 654"
Cohesion: 0.67
Nodes (1): Benchmarks of orthogonal matching pursuit (:ref:`OMP`) versus least angle regres

### Community 655 - "Community 655"
Cohesion: 0.67
Nodes (1): Benchmarks of Singular Value Decomposition (Exact and Approximate)  The data is

### Community 656 - "Community 656"
Cohesion: 0.67
Nodes (1): Module to give helpful messages to the user that did not compile scikit-learn pr

### Community 657 - "Community 657"
Cohesion: 0.67
Nodes (1): Agglomerative clustering with different metrics ================================

### Community 658 - "Community 658"
Cohesion: 0.67
Nodes (1): ============================================================================= Va

### Community 659 - "Community 659"
Cohesion: 0.67
Nodes (1): ============================================================ Empirical evaluatio

### Community 660 - "Community 660"
Cohesion: 0.67
Nodes (1): ====================================================== Effect of transforming th

### Community 661 - "Community 661"
Cohesion: 0.67
Nodes (1): Utilities to load popular datasets and artificial data generators.

### Community 662 - "Community 662"
Cohesion: 0.67
Nodes (1): ============================================== Plot randomly generated multilabe

### Community 663 - "Community 663"
Cohesion: 0.67
Nodes (1): ============================ Faces dataset decompositions ======================

### Community 664 - "Community 664"
Cohesion: 0.67
Nodes (1): ========================== FastICA on 2D point clouds ==========================

### Community 665 - "Community 665"
Cohesion: 0.67
Nodes (2): ============================= OOB Errors for Random Forests ====================, # NOTE: Setting the `warm_start` construction parameter to `True` disables

### Community 666 - "Community 666"
Cohesion: 0.67
Nodes (1): ============================================== Features in Histogram Gradient Bo

### Community 667 - "Community 667"
Cohesion: 0.67
Nodes (1): Close PRs labeled with 'autoclose' more than 14 days ago.  Called from .github/w

### Community 668 - "Community 668"
Cohesion: 0.67
Nodes (2): This module contains the TreePredictor class which is used for prediction., # TODO: consider always using platform agnostic dtypes for fitted

### Community 669 - "Community 669"
Cohesion: 0.67
Nodes (1): ================================================================= Permutation Im

### Community 670 - "Community 670"
Cohesion: 0.67
Nodes (1): ============================================ Curve Fitting with Bayesian Ridge R

### Community 671 - "Community 671"
Cohesion: 0.67
Nodes (1): ======================================== Plot multi-class SGD on the iris datase

### Community 672 - "Community 672"
Cohesion: 0.67
Nodes (1): ========================== SGD: convex loss functions ==========================

### Community 673 - "Community 673"
Cohesion: 0.67
Nodes (1): =============== GMM covariances ===============  Demonstration of several covari

### Community 674 - "Community 674"
Cohesion: 0.67
Nodes (1): ========================== GMM Initialization Methods ==========================

### Community 675 - "Community 675"
Cohesion: 0.67
Nodes (1): ================================= Gaussian Mixture Model Ellipsoids ============

### Community 676 - "Community 676"
Cohesion: 0.67
Nodes (2): Generate indices to split data into training and test set.          Parameters, Generate indices to split data into training and test set.          Yields

### Community 677 - "Community 677"
Cohesion: 0.67
Nodes (2): Generate indices to split data into training and test set.          Parameters, Generate indices to split data into training and test set.          Parameters

### Community 678 - "Community 678"
Cohesion: 0.67
Nodes (1): =================================== Simple 1D Kernel Density Estimation ========

### Community 680 - "Community 680"
Cohesion: 0.67
Nodes (1): ============================= Importance of Feature Scaling ====================

### Community 681 - "Community 681"
Cohesion: 0.67
Nodes (1): ============================================ Comparing Target Encoder with Other

### Community 682 - "Community 682"
Cohesion: 0.67
Nodes (1): ======================================== Release Highlights for scikit-learn 0.2

### Community 683 - "Community 683"
Cohesion: 0.67
Nodes (2): _features_html(), Generate HTML representation of feature names.      Creates a collapsible HTML d

### Community 684 - "Community 684"
Cohesion: 0.67
Nodes (1): ========================================================= Plot classification bo

### Community 686 - "Community 686"
Cohesion: 0.67
Nodes (1): CustomBinaryEstimator

### Community 687 - "Community 687"
Cohesion: 0.67
Nodes (1): CustomContinuousEstimator

### Community 688 - "Community 688"
Cohesion: 0.67
Nodes (1): CustomMulticlassEstimator

### Community 689 - "Community 689"
Cohesion: 0.67
Nodes (2): Check that bunch raises deprecation message with `__getattr__`., test_bunch_attribute_deprecation()

### Community 690 - "Community 690"
Cohesion: 0.67
Nodes (1): Smoke Test the check_build module

### Community 691 - "Community 691"
Cohesion: 0.67
Nodes (1): Tests for making sure experimental imports work as expected.

### Community 692 - "Community 692"
Cohesion: 0.67
Nodes (1): Tests for making sure experimental imports work as expected.

### Community 693 - "Community 693"
Cohesion: 0.67
Nodes (1): Tests for making sure experimental imports work as expected.

### Community 694 - "Community 694"
Cohesion: 0.67
Nodes (2): Test Cython's weighted Fenwick tree implementation, test_cython_weighted_fenwick_tree()

### Community 695 - "Community 695"
Cohesion: 0.67
Nodes (3): _assert_allclose_and_same_dtype(), _assert_array_equal_and_same_dtype(), test_simple_impute_pd_na()

### Community 696 - "Community 696"
Cohesion: 0.67
Nodes (1): Test Olivetti faces fetcher, if the data is available, or if specifically reques

### Community 697 - "Community 697"
Cohesion: 0.67
Nodes (3): check_pca_float_dtype_preservation(), check_pca_int_dtype_upcast_to_double(), test_pca_dtype_preservation()

### Community 698 - "Community 698"
Cohesion: 0.67
Nodes (1): Test the rcv1 loader, if the data is available, or if specifically requested via

### Community 699 - "Community 699"
Cohesion: 0.67
Nodes (3): assert_uniform_grid(), Make sure that TSNE can approximately recover a uniform 2D grid      Due to ties, test_uniform_grid()

### Community 700 - "Community 700"
Cohesion: 0.67
Nodes (3): _check_stop_words_consistency(), test_stop_word_validation_custom_preprocessor(), test_vectorizer_stop_words_inconsistent()

### Community 701 - "Community 701"
Cohesion: 0.67
Nodes (2): Check that the types defined in _typedefs correspond to the expected     numpy d, test_types()

### Community 703 - "Community 703"
Cohesion: 0.67
Nodes (2): Check the `dtype` consistency of `WeightVector`., test_type_invariance()

### Community 704 - "Community 704"
Cohesion: 0.67
Nodes (2): _init_arpack_v0(), Initialize the starting vector for iteration in ARPACK functions.      Initializ

### Community 705 - "Community 705"
Cohesion: 0.67
Nodes (3): _check_transformer(), check_transformer_data_not_an_array(), check_transformer_general()

### Community 706 - "Community 706"
Cohesion: 1.00
Nodes (1): ==================================== Outlier detection on a real data set ======

### Community 707 - "Community 707"
Cohesion: 1.00
Nodes (1): ======================================= Visualizing the stock market structure =

### Community 708 - "Community 708"
Cohesion: 1.00
Nodes (1): NumPy Array API compatibility library  This is a small wrapper around NumPy, CuP

### Community 711 - "Community 711"
Cohesion: 1.00
Nodes (1): A comparison of different methods in GLM  Data comes from a random square matrix

### Community 712 - "Community 712"
Cohesion: 1.00
Nodes (1): ============================================================= Kernel PCA Solvers

### Community 713 - "Community 713"
Cohesion: 1.00
Nodes (1): ========================================================== Kernel PCA Solvers co

### Community 714 - "Community 714"
Cohesion: 1.00
Nodes (1): ============================ LocalOutlierFactor benchmark ======================

### Community 717 - "Community 717"
Cohesion: 1.00
Nodes (1): Benchmark scikit-learn's Ward implement compared to SciPy's

### Community 718 - "Community 718"
Cohesion: 1.00
Nodes (1): Benchmark suite for scikit-learn using ASV

### Community 719 - "Community 719"
Cohesion: 1.00
Nodes (1): ============================================= A demo of the Spectral Biclusterin

### Community 720 - "Community 720"
Cohesion: 1.00
Nodes (1): ============================================== A demo of the Spectral Co-Cluster

### Community 721 - "Community 721"
Cohesion: 1.00
Nodes (1): Method called after finishing the fit method of the estimator.          For auto

### Community 722 - "Community 722"
Cohesion: 1.00
Nodes (1): Method called at the beginning of each fit task of the estimator.          Param

### Community 723 - "Community 723"
Cohesion: 1.00
Nodes (1): Method called at the end of each fit task of the estimator.          Parameters

### Community 724 - "Community 724"
Cohesion: 1.00
Nodes (1): Pre-order depth-first traversal of the task tree.

### Community 725 - "Community 725"
Cohesion: 1.00
Nodes (1): ================================ Recognizing hand-written digits ===============

### Community 726 - "Community 726"
Cohesion: 1.00
Nodes (1): ================================================= Demo of affinity propagation c

### Community 728 - "Community 728"
Cohesion: 1.00
Nodes (1): ================================= Compare BIRCH and MiniBatchKMeans ============

### Community 729 - "Community 729"
Cohesion: 1.00
Nodes (1): ============================================================= Bisecting K-Means

### Community 730 - "Community 730"
Cohesion: 1.00
Nodes (1): ========================================================= Comparing different cl

### Community 731 - "Community 731"
Cohesion: 1.00
Nodes (1): ====================================================================== A demo of

### Community 732 - "Community 732"
Cohesion: 1.00
Nodes (1): =================================== Demo of DBSCAN clustering algorithm ========

### Community 733 - "Community 733"
Cohesion: 1.00
Nodes (1): Online learning of a dictionary of parts of faces ==============================

### Community 734 - "Community 734"
Cohesion: 1.00
Nodes (1): ========================================================= Feature agglomeration

### Community 735 - "Community 735"
Cohesion: 1.00
Nodes (1): =========================== Vector Quantization Example ========================

### Community 737 - "Community 737"
Cohesion: 1.00
Nodes (1): ==================================== Demonstration of k-means assumptions ======

### Community 738 - "Community 738"
Cohesion: 1.00
Nodes (1): =========================================================== An example of K-Mean

### Community 739 - "Community 739"
Cohesion: 1.00
Nodes (1): ===============================================================================

### Community 740 - "Community 740"
Cohesion: 1.00
Nodes (1): ================================================================ Comparing diffe

### Community 741 - "Community 741"
Cohesion: 1.00
Nodes (1): ============================================= A demo of the mean-shift clusterin

### Community 742 - "Community 742"
Cohesion: 1.00
Nodes (1): ==================================================================== Comparison

### Community 743 - "Community 743"
Cohesion: 1.00
Nodes (1): =================================== Demo of OPTICS clustering algorithm ========

### Community 744 - "Community 744"
Cohesion: 1.00
Nodes (1): =========================================== Spectral clustering for image segmen

### Community 745 - "Community 745"
Cohesion: 1.00
Nodes (1): =================================================== Hierarchical clustering with

### Community 746 - "Community 746"
Cohesion: 1.00
Nodes (1): JustComplex

### Community 747 - "Community 747"
Cohesion: 1.00
Nodes (1): ======================================================================= Shrinkag

### Community 748 - "Community 748"
Cohesion: 1.00
Nodes (1): ============================= Ledoit-Wolf vs OAS estimation ====================

### Community 749 - "Community 749"
Cohesion: 1.00
Nodes (1): r""" ================================================================ Robust cov

### Community 750 - "Community 750"
Cohesion: 1.00
Nodes (1): r""" ======================================= Robust vs Empirical covariance esti

### Community 751 - "Community 751"
Cohesion: 1.00
Nodes (1): ====================================== Sparse inverse covariance estimation ====

### Community 752 - "Community 752"
Cohesion: 1.00
Nodes (1): =================================== Compare cross decomposition methods ========

### Community 756 - "Community 756"
Cohesion: 1.00
Nodes (1): ===================================== Blind source separation using FastICA ====

### Community 757 - "Community 757"
Cohesion: 1.00
Nodes (1): =============== Incremental PCA ===============  Incremental principal component

### Community 758 - "Community 758"
Cohesion: 1.00
Nodes (1): ========== Kernel PCA ==========  This example shows the difference between the

### Community 759 - "Community 759"
Cohesion: 1.00
Nodes (1): ================================================== Principal Component Analysis

### Community 760 - "Community 760"
Cohesion: 1.00
Nodes (1): =============================================================== Factor Analysis

### Community 761 - "Community 761"
Cohesion: 1.00
Nodes (1): ====================================== Decision Tree Regression with AdaBoost ==

### Community 762 - "Community 762"
Cohesion: 1.00
Nodes (1): ================== Two-class AdaBoost ==================  This example fits an A

### Community 763 - "Community 763"
Cohesion: 1.00
Nodes (1): =============================================================== Comparing Random

### Community 764 - "Community 764"
Cohesion: 1.00
Nodes (1): ========================================== Feature importances with a forest of

### Community 765 - "Community 765"
Cohesion: 1.00
Nodes (1): ==================================================================== Plot the de

### Community 766 - "Community 766"
Cohesion: 1.00
Nodes (1): =================================== Early stopping in Gradient Boosting ========

### Community 767 - "Community 767"
Cohesion: 1.00
Nodes (1): ============================ Gradient Boosting regression ======================

### Community 768 - "Community 768"
Cohesion: 1.00
Nodes (1): ================================ Gradient Boosting regularization ==============

### Community 769 - "Community 769"
Cohesion: 1.00
Nodes (1): ======================= IsolationForest example =======================  An exam

### Community 770 - "Community 770"
Cohesion: 1.00
Nodes (1): ===================== Monotonic Constraints =====================  This example

### Community 771 - "Community 771"
Cohesion: 1.00
Nodes (1): ================================================= Plot individual and voting reg

### Community 772 - "Community 772"
Cohesion: 1.00
Nodes (1): This is now a no-op and can be safely removed from your code.  It used to enable

### Community 773 - "Community 773"
Cohesion: 1.00
Nodes (1): This is now a no-op and can be safely removed from your code.  It used to enable

### Community 774 - "Community 774"
Cohesion: 1.00
Nodes (1): Importable modules that enable the use of experimental features or estimators.

### Community 776 - "Community 776"
Cohesion: 1.00
Nodes (1): External, bundled dependencies.

### Community 777 - "Community 777"
Cohesion: 1.00
Nodes (1): =========================================== Comparison of F-test and mutual info

### Community 778 - "Community 778"
Cohesion: 1.00
Nodes (1): =================================================== Recursive feature eliminatio

### Community 779 - "Community 779"
Cohesion: 1.00
Nodes (1): Checks that dist/* contains the number of wheels built from the .github/workflow

### Community 780 - "Community 780"
Cohesion: 1.00
Nodes (1): This module implements histogram-based gradient boosting estimators.  The implem

### Community 781 - "Community 781"
Cohesion: 1.00
Nodes (1): =================================================== Failure of Machine Learning

### Community 782 - "Community 782"
Cohesion: 1.00
Nodes (1): Internals of array-api-extra.

### Community 783 - "Community 783"
Cohesion: 1.00
Nodes (1): ========================================================================== Fitti

### Community 784 - "Community 784"
Cohesion: 1.00
Nodes (1): ======================================================= HuberRegressor vs Ridge

### Community 785 - "Community 785"
Cohesion: 1.00
Nodes (1): ================================== L1-based models for Sparse Signals ==========

### Community 786 - "Community 786"
Cohesion: 1.00
Nodes (1): ============================== Lasso on dense and sparse data ==================

### Community 787 - "Community 787"
Cohesion: 1.00
Nodes (1): ======================================== Lasso, Lasso-LARS, and Elastic Net path

### Community 788 - "Community 788"
Cohesion: 1.00
Nodes (1): ============================================== L1 Penalty and Sparsity in Logist

### Community 789 - "Community 789"
Cohesion: 1.00
Nodes (1): ============================================= Joint feature selection with multi

### Community 790 - "Community 790"
Cohesion: 1.00
Nodes (1): ========================== Non-negative least squares ==========================

### Community 791 - "Community 791"
Cohesion: 1.00
Nodes (1): =========================================== Ordinary Least Squares and Ridge Reg

### Community 792 - "Community 792"
Cohesion: 1.00
Nodes (1): =========================== Orthogonal Matching Pursuit ========================

### Community 793 - "Community 793"
Cohesion: 1.00
Nodes (1): =================== Quantile regression ===================  This example illust

### Community 794 - "Community 794"
Cohesion: 1.00
Nodes (1): =========================================== Robust linear model estimation using

### Community 795 - "Community 795"
Cohesion: 1.00
Nodes (1): ========================================================= Ridge coefficients as

### Community 796 - "Community 796"
Cohesion: 1.00
Nodes (1): =========================================================== Plot Ridge coefficie

### Community 797 - "Community 797"
Cohesion: 1.00
Nodes (1): ============== SGD: Penalties ==============  Contours of where the penalty is e

### Community 798 - "Community 798"
Cohesion: 1.00
Nodes (1): ========================================= SGD: Maximum margin separating hyperpl

### Community 799 - "Community 799"
Cohesion: 1.00
Nodes (1): ===================== SGD: Weighted samples =====================  Plot decision

### Community 800 - "Community 800"
Cohesion: 1.00
Nodes (1): ===================================================== MNIST classification using

### Community 801 - "Community 801"
Cohesion: 1.00
Nodes (1): ==================== Theil-Sen Regression ====================  Computes a Theil

### Community 803 - "Community 803"
Cohesion: 1.00
Nodes (1): ============================================= Manifold Learning methods on a sev

### Community 804 - "Community 804"
Cohesion: 1.00
Nodes (1): ========================= Multi-dimensional scaling =========================  A

### Community 805 - "Community 805"
Cohesion: 1.00
Nodes (1): =================================== Swiss Roll And Swiss-Hole Reduction ========

### Community 806 - "Community 806"
Cohesion: 1.00
Nodes (1): ============================================================================= t-

### Community 807 - "Community 807"
Cohesion: 1.00
Nodes (1): ============================================== Face completion with a multi-outp

### Community 808 - "Community 808"
Cohesion: 1.00
Nodes (1): ================================ ROC Curve with Visualization API ==============

### Community 809 - "Community 809"
Cohesion: 1.00
Nodes (1): ========================================= Density Estimation for a Gaussian mixt

### Community 810 - "Community 810"
Cohesion: 1.00
Nodes (1): ============================================================== Evaluate the perf

### Community 811 - "Community 811"
Cohesion: 1.00
Nodes (1): ==================================== Plotting Cross-Validated Predictions ======

### Community 812 - "Community 812"
Cohesion: 1.00
Nodes (1): ============================================================================ Dem

### Community 813 - "Community 813"
Cohesion: 1.00
Nodes (1): ========================================= Nested versus non-nested cross-validat

### Community 814 - "Community 814"
Cohesion: 1.00
Nodes (1): ================================================================= Test with perm

### Community 815 - "Community 815"
Cohesion: 1.00
Nodes (1): ============================================================= Receiver Operating

### Community 816 - "Community 816"
Cohesion: 1.00
Nodes (1): ================================================== Multiclass Receiver Operating

### Community 817 - "Community 817"
Cohesion: 1.00
Nodes (1): Successive Halving Iterations =============================  This example illust

### Community 818 - "Community 818"
Cohesion: 1.00
Nodes (1): ========================================================= Effect of model regula

### Community 819 - "Community 819"
Cohesion: 1.00
Nodes (1): ========================= Kernel Density Estimation =========================  T

### Community 820 - "Community 820"
Cohesion: 1.00
Nodes (1): ================================================= Novelty detection with Local O

### Community 821 - "Community 821"
Cohesion: 1.00
Nodes (1): =============================== Nearest Centroid Classification ================

### Community 822 - "Community 822"
Cohesion: 1.00
Nodes (1): ============================ Nearest Neighbors regression ======================

### Community 824 - "Community 824"
Cohesion: 1.00
Nodes (1): ========================================================== Demonstrating the dif

### Community 825 - "Community 825"
Cohesion: 1.00
Nodes (1): ================================================================ Using KBinsDisc

### Community 826 - "Community 826"
Cohesion: 1.00
Nodes (1): ================================= Map data to a normal distribution ============

### Community 828 - "Community 828"
Cohesion: 1.00
Nodes (1): ========================================= Label Propagation digits: Active learn

### Community 829 - "Community 829"
Cohesion: 1.00
Nodes (1): =================================================== Label Propagation digits: De

### Community 830 - "Community 830"
Cohesion: 1.00
Nodes (1): ======================================================= Label Propagation circle

### Community 831 - "Community 831"
Cohesion: 1.00
Nodes (1): Distributor init file  Distributors: you can add custom code here to support par

### Community 832 - "Community 832"
Cohesion: 1.00
Nodes (1): ================================================== Plot different SVM classifier

### Community 833 - "Community 833"
Cohesion: 1.00
Nodes (1): ===================================== Plot the support vectors in LinearSVC ====

### Community 834 - "Community 834"
Cohesion: 1.00
Nodes (1): ========================================== One-class SVM with non-linear kernel

### Community 835 - "Community 835"
Cohesion: 1.00
Nodes (1): ================================================= SVM: Separating hyperplane for

### Community 836 - "Community 836"
Cohesion: 1.00
Nodes (1): ========================================= SVM: Maximum margin separating hyperpl

### Community 837 - "Community 837"
Cohesion: 1.00
Nodes (1): ========================================================= SVM Margins Example ==

### Community 838 - "Community 838"
Cohesion: 1.00
Nodes (1): =================================================================== Support Vect

### Community 839 - "Community 839"
Cohesion: 1.00
Nodes (1): r""" ============================================== Scaling the regularization p

### Community 840 - "Community 840"
Cohesion: 1.00
Nodes (1): ========================================================= SVM Tie Breaking Examp

### Community 843 - "Community 843"
Cohesion: 1.00
Nodes (2): Test get_namespace on sparse arrays., test_get_namespace_sparse_with_dispatch()

### Community 844 - "Community 844"
Cohesion: 1.00
Nodes (2): Test get_namespace for ArrayAPI arrays., test_get_namespace_array_api()

### Community 845 - "Community 845"
Cohesion: 1.00
Nodes (2): Check conversion between various namespace-device-pairs., test_move_to_array_api_conversions()

### Community 846 - "Community 846"
Cohesion: 1.00
Nodes (2): Check sparse inputs are handled correctly., test_move_to_sparse()

### Community 847 - "Community 847"
Cohesion: 1.00
Nodes (2): Check NumPy arrays with negative strides can be moved to torch., test_move_to_numpy_negative_strides_to_torch()

### Community 848 - "Community 848"
Cohesion: 1.00
Nodes (2): Test _asarray_with_order passes along order for NumPy arrays., test_asarray_with_order()

### Community 849 - "Community 849"
Cohesion: 1.00
Nodes (2): Check NaN reductions like _nanmin and _nanmax, test_nan_reductions()

### Community 850 - "Community 850"
Cohesion: 1.00
Nodes (2): Check convert_to_numpy for GPU backed libraries., test_convert_to_numpy_gpu()

### Community 851 - "Community 851"
Cohesion: 1.00
Nodes (2): Check convert_to_numpy for PyTorch CPU arrays., test_convert_to_numpy_cpu()

### Community 852 - "Community 852"
Cohesion: 1.00
Nodes (2): Check that get_namespace returns NumPy wrapper, test_get_namespace_ndarray_or_similar_default()

### Community 853 - "Community 853"
Cohesion: 1.00
Nodes (2): Check expected behavior with device and creation functions., test_get_namespace_ndarray_creation_device()

### Community 854 - "Community 854"
Cohesion: 1.00
Nodes (2): Check `_validate_diagonal_args` raises the correct errors., test_validate_diagonal_args()

### Community 855 - "Community 855"
Cohesion: 1.00
Nodes (2): Check `_fill/add_to_diagonal` behaviour correct with numpy arrays., test_fill_and_add_to_diagonal()

### Community 856 - "Community 856"
Cohesion: 1.00
Nodes (2): Test get_namespace on NumPy ndarrays., test_get_namespace_ndarray_or_similar_default_with_dispatch()

### Community 857 - "Community 857"
Cohesion: 1.00
Nodes (2): Check array API `_fill_diagonal` consistent with `numpy._fill_diagonal`., test_fill_diagonal()

### Community 858 - "Community 858"
Cohesion: 1.00
Nodes (2): Check `_add_to_diagonal` consistent between array API xp and numpy namespace., test_add_to_diagonal()

### Community 859 - "Community 859"
Cohesion: 1.00
Nodes (2): Test get_namespace on dataframes and series., test_get_namespace_df_with_dispatch()

### Community 860 - "Community 860"
Cohesion: 1.00
Nodes (1): test_pickling_when_getstate_is_overwritten_by_mixin_outside_of_sklearn()

### Community 861 - "Community 861"
Cohesion: 1.00
Nodes (2): Check the behaviour of `allowed_extension` in `load_files`., test_load_files_allowed_extensions()

### Community 862 - "Community 862"
Cohesion: 1.00
Nodes (2): Test to check that we load a scaled version by default but that we can     get a, test_load_diabetes_raw()

### Community 863 - "Community 863"
Cohesion: 1.00
Nodes (2): Test Poisson loss against well tested HalfPoissonLoss., test_poisson_loss()

### Community 864 - "Community 864"
Cohesion: 1.00
Nodes (2): Check that we raise the ethical warning when trying to import `load_boston`., test_load_boston_error()

### Community 865 - "Community 865"
Cohesion: 1.00
Nodes (2): Check retry mechanism in _fetch_remote., test_fetch_remote_raise_warnings_with_invalid_url()

### Community 866 - "Community 866"
Cohesion: 1.00
Nodes (2): Check that LinearRegression is as good as `scipy.linalg.lstsq`.     Non regressi, test_linear_regression_vs_lstsq()

### Community 867 - "Community 867"
Cohesion: 1.00
Nodes (2): Test that the impact of sample_weight is consistent.      Note that this test is, test_linear_regression_sample_weight_consistency()

### Community 868 - "Community 868"
Cohesion: 1.00
Nodes (2): Test that _predict_proba_lr of LinearClassifierMixin deals with large     negati, test_predict_proba_lr_large_values()

### Community 869 - "Community 869"
Cohesion: 1.00
Nodes (2): Check the behaviour of the private helpers `_assign_where`., test_assign_where()

### Community 870 - "Community 870"
Cohesion: 1.00
Nodes (2): Check input validation for `plot`., test_display_plot_input_error()

### Community 871 - "Community 871"
Cohesion: 1.00
Nodes (2): Check that decision boundary is correct., test_decision_boundary_display_classifier()

### Community 872 - "Community 872"
Cohesion: 1.00
Nodes (2): Check that decision boundary is correct for outlier detector., test_decision_boundary_display_outlier_detector()

### Community 873 - "Community 873"
Cohesion: 1.00
Nodes (2): Check that we can display the decision boundary for a regressor., test_decision_boundary_display_regressor()

### Community 874 - "Community 874"
Cohesion: 1.00
Nodes (2): Check errors for bad response., test_error_bad_response()

### Community 875 - "Community 875"
Cohesion: 1.00
Nodes (2): Check that multilabel classifier raises correct error., test_multilabel_classifier_error()

### Community 876 - "Community 876"
Cohesion: 1.00
Nodes (2): Check that multi-output multi-class classifier raises correct error., test_multi_output_multi_class_classifier_error()

### Community 877 - "Community 877"
Cohesion: 1.00
Nodes (2): Check that multioutput regressor raises correct error., test_multioutput_regressor_error()

### Community 878 - "Community 878"
Cohesion: 1.00
Nodes (2): Check that column names are used for pandas., test_dataframe_labels_used()

### Community 879 - "Community 879"
Cohesion: 1.00
Nodes (2): Check that decision boundary works with classifiers trained on string labels., test_string_target()

### Community 880 - "Community 880"
Cohesion: 1.00
Nodes (2): Check that passing a dataframe at fit and to the Display does not     raise warn, test_dataframe_support()

### Community 881 - "Community 881"
Cohesion: 1.00
Nodes (2): Check the behaviour of passing `class_of_interest` for plotting the output of, test_class_of_interest_binary()

### Community 882 - "Community 882"
Cohesion: 1.00
Nodes (2): Check that we raise an error when `X` does not have exactly 2 features., test_input_data_dimension()

### Community 883 - "Community 883"
Cohesion: 1.00
Nodes (2): Check the behaviour of passing `class_of_interest` for plotting the output of, test_class_of_interest_multiclass()

### Community 884 - "Community 884"
Cohesion: 1.00
Nodes (2): Check error raised for multi-output multi-class classifiers by     `_check_bound, test_check_boundary_response_method_error()

### Community 885 - "Community 885"
Cohesion: 1.00
Nodes (2): Check correct cmap used for all `target_colors` inputs., test_target_colors_cmap()

### Community 886 - "Community 886"
Cohesion: 1.00
Nodes (2): Check that an error is raised if a qualitative colormap doesn't have enough colo, test_multiclass_not_enough_colors_error()

### Community 887 - "Community 887"
Cohesion: 1.00
Nodes (2): Test that `levels` are set such that all classes and class boundaries are displa, test_multiclass_levels()

### Community 888 - "Community 888"
Cohesion: 1.00
Nodes (2): Check that decision boundaries are plotted in the background., test_zorder()

### Community 889 - "Community 889"
Cohesion: 1.00
Nodes (2): Check that the visual block `name_details` matches the `feature_names_in_`     N, test_sk_visual_block_remainder_col_names_pandas()

### Community 890 - "Community 890"
Cohesion: 1.00
Nodes (2): Check that visual_block doesn't return remainder when it has no columns     Non-, test_sk_visual_block_full_transform()

### Community 891 - "Community 891"
Cohesion: 1.00
Nodes (2): Check that remainder still uses available string column names in visual block, test_sk_visual_block_int_remainder_cols_pandas()

### Community 892 - "Community 892"
Cohesion: 1.00
Nodes (2): Check that pandas output works when there is an empty selection.      Non-regres, test_empty_selection_pandas_output()

### Community 893 - "Community 893"
Cohesion: 1.00
Nodes (2): Check column transformer raises error if indices are not aligned.      Non-regre, test_raise_error_if_index_not_aligned()

### Community 894 - "Community 894"
Cohesion: 1.00
Nodes (2): Check that the output is set for the remainder.      Non-regression test for #26, test_remainder_set_output()

### Community 895 - "Community 895"
Cohesion: 1.00
Nodes (2): Check behavior when a transformer's output contains pandas.NA      It should rai, test_transform_pd_na()

### Community 896 - "Community 896"
Cohesion: 1.00
Nodes (2): Check that ColumnTransformer works in parallel with joblib's auto-memmapping., test_column_transformer_auto_memmap()

### Community 897 - "Community 897"
Cohesion: 1.00
Nodes (2): Check index handling when both pd.Series and pd.DataFrame slices are used in, test_column_transformer_non_default_index()

### Community 898 - "Community 898"
Cohesion: 1.00
Nodes (2): Test that metadata is routed correctly for column transformer., test_metadata_routing_for_column_transformer()

### Community 899 - "Community 899"
Cohesion: 1.00
Nodes (2): Test metadata routing when the sub-estimator doesn't implement     ``fit_transfo, test_metadata_routing_no_fit_transform()

### Community 900 - "Community 900"
Cohesion: 1.00
Nodes (2): Check that passing parameter not used by the coordinate descent solver     will, test_path_unknown_parameter()

### Community 901 - "Community 901"
Cohesion: 1.00
Nodes (2): Test that a warning is issued if model does not converge, test_enet_coordinate_descent_raises_convergence()

### Community 902 - "Community 902"
Cohesion: 1.00
Nodes (2): Test that the impact of sample_weight is consistent.      Note that this test is, test_enet_sample_weight_consistency()

### Community 903 - "Community 903"
Cohesion: 1.00
Nodes (2): Test that ElasticNetCV with sample weights gives correct results.      We fit th, test_enet_cv_sample_weight_correctness()

### Community 904 - "Community 904"
Cohesion: 1.00
Nodes (2): Test that ElasticNetCV gives same result as GridSearchCV., test_enet_cv_grid_search()

### Community 905 - "Community 905"
Cohesion: 1.00
Nodes (2): Test that the impact of sample_weight is consistent., test_enet_cv_sample_weight_consistency()

### Community 906 - "Community 906"
Cohesion: 1.00
Nodes (2): Check that ElasticNet does not overwrite sample_weights., test_enet_sample_weight_does_not_overwrite_sample_weight()

### Community 907 - "Community 907"
Cohesion: 1.00
Nodes (2): Test that ElasticNet(alpha=0) converges to the same solution as OLS., test_enet_ols_consistency()

### Community 908 - "Community 908"
Cohesion: 1.00
Nodes (2): Test that early_stopping works correctly., test_cython_solver_early_stopping()

### Community 909 - "Community 909"
Cohesion: 1.00
Nodes (2): Check that the models inheriting from class:`LinearModelCV` raise an     error w, test_cv_estimators_reject_params_with_no_routing_enabled()

### Community 910 - "Community 910"
Cohesion: 1.00
Nodes (2): Test enet_path works with check_input=False and various precompute settings., test_enet_path_check_input_false()

### Community 911 - "Community 911"
Cohesion: 1.00
Nodes (2): Check deprecation of n_alphas in favor of alphas., test_path_function_deprecated_n_alphas()

### Community 912 - "Community 912"
Cohesion: 1.00
Nodes (2): Check that Lasso.dual_gap_ matches its objective formulation, with the     dataf, test_lasso_dual_gap()

### Community 913 - "Community 913"
Cohesion: 1.00
Nodes (2): Check the `alphas` validation in LassoCV., test_lassocv_alphas_validation()

### Community 914 - "Community 914"
Cohesion: 1.00
Nodes (2): Check that _set_order returns arrays with promised order., test_set_order_dense()

### Community 915 - "Community 915"
Cohesion: 1.00
Nodes (2): Test that MultiTaskLasso gives same results as the one from skglm.      To repro, test_multi_task_lasso_vs_skglm()

### Community 916 - "Community 916"
Cohesion: 1.00
Nodes (2): Check that _set_order returns sparse matrices in promised format., test_set_order_sparse()

### Community 917 - "Community 917"
Cohesion: 1.00
Nodes (2): Test that all 3 Cython solvers for 1-d targets give same results., test_cython_solver_equivalence()

### Community 918 - "Community 918"
Cohesion: 1.00
Nodes (2): _check_identity_scalers_attributes(), test_scaler_return_identity()

### Community 919 - "Community 919"
Cohesion: 1.00
Nodes (2): Check the behaviour of `QuantileTransformer` when `subsample=None`., test_quantile_transform_subsampling_disabled()

### Community 920 - "Community 920"
Cohesion: 1.00
Nodes (2): Check kernel centering for non-linear kernel., test_kernelcenterer_non_linear_kernel()

### Community 921 - "Community 921"
Cohesion: 1.00
Nodes (2): Check that box-cox raises informative when a column contains all nans.      Non-, test_power_transformer_box_cox_raise_all_nans_col()

### Community 922 - "Community 922"
Cohesion: 1.00
Nodes (2): Check that `inverse_transform` from `StandardScaler` raises an error     with 1D, test_standard_scaler_raise_error_for_1d_input()

### Community 923 - "Community 923"
Cohesion: 1.00
Nodes (2): Check that significantly non-Gaussian data before transforms correctly.      For, test_power_transformer_significantly_non_gaussian()

### Community 924 - "Community 924"
Cohesion: 1.00
Nodes (2): Check one-to-one transformers give correct feature names., test_one_to_one_features()

### Community 925 - "Community 925"
Cohesion: 1.00
Nodes (2): Check one-to-one transformers give correct feature names., test_one_to_one_features_pandas()

### Community 926 - "Community 926"
Cohesion: 1.00
Nodes (2): Test that kernel centerer `feature_names_out`., test_kernel_centerer_feature_names_out()

### Community 927 - "Community 927"
Cohesion: 1.00
Nodes (2): Check that PowerTransformer leaves constant features unchanged., test_power_transformer_constant_feature()

### Community 928 - "Community 928"
Cohesion: 1.00
Nodes (2): Check if a warning is triggered when the inverse transformations of the     Box-, test_yeo_johnson_inverse_transform_warning()

### Community 929 - "Community 929"
Cohesion: 1.00
Nodes (2): Verify that PowerTransformer operates without raising any warnings on valid data, test_power_transformer_no_warnings()

### Community 930 - "Community 930"
Cohesion: 1.00
Nodes (2): Check that the results are consistent across different SciPy versions., test_yeojohnson_for_different_scipy_version()

### Community 931 - "Community 931"
Cohesion: 1.00
Nodes (2): Check that inverse_transform does not raise a warning about feature     names wh, test_transformer_inverse_transform_feature_names_warning()

### Community 932 - "Community 932"
Cohesion: 1.00
Nodes (2): Check that an informative error is raised when the input shape is incorrect., test_transformer_inverse_transform_shape_error()

### Community 933 - "Community 933"
Cohesion: 1.00
Nodes (2): Check that the reconstruction attributes are correctly passed., test_standard_scaler_callback_support()

### Community 934 - "Community 934"
Cohesion: 1.00
Nodes (2): Check feature names for dict learning estimators., test_get_feature_names_out()

### Community 935 - "Community 935"
Cohesion: 1.00
Nodes (2): Tests that HDBSCAN works when passed a callable metric., test_hdbscan_callable_metric()

### Community 936 - "Community 936"
Cohesion: 1.00
Nodes (2): Tests that HDBSCAN works correctly when passing sparse feature data.     Evaluat, test_hdbscan_sparse()

### Community 937 - "Community 937"
Cohesion: 1.00
Nodes (2): Tests that HDBSCAN centers are calculated and stored properly, and are     accur, test_hdbscan_centers()

### Community 938 - "Community 938"
Cohesion: 1.00
Nodes (2): Tests that HDBSCAN single-cluster selection with epsilon works correctly., test_hdbscan_allow_single_cluster_with_epsilon()

### Community 939 - "Community 939"
Cohesion: 1.00
Nodes (2): Validate that HDBSCAN can properly cluster this difficult synthetic     dataset., test_hdbscan_better_than_dbscan()

### Community 940 - "Community 940"
Cohesion: 1.00
Nodes (2): Tests that HDBSCAN works correctly for array-likes and precomputed inputs     wi, test_hdbscan_usable_inputs()

### Community 941 - "Community 941"
Cohesion: 1.00
Nodes (2): Tests that HDBSCAN raises the correct error when there are too few     non-zero, test_hdbscan_sparse_distances_too_few_nonzero()

### Community 942 - "Community 942"
Cohesion: 1.00
Nodes (2): Tests that HDBSCAN raises the correct error when the distance matrix     has mul, test_hdbscan_sparse_distances_disconnected_graph()

### Community 943 - "Community 943"
Cohesion: 1.00
Nodes (2): Tests that HDBSCAN correctly raises an error for invalid metric choices., test_hdbscan_tree_invalid_metric()

### Community 944 - "Community 944"
Cohesion: 1.00
Nodes (2): Tests that HDBSCAN correctly raises an error when setting `min_samples`     larg, test_hdbscan_too_many_min_samples()

### Community 945 - "Community 945"
Cohesion: 1.00
Nodes (2): Tests that HDBSCAN correctly raises an error when providing precomputed     dist, test_hdbscan_precomputed_dense_nan()

### Community 946 - "Community 946"
Cohesion: 1.00
Nodes (2): Tests that the `_do_labelling` helper function correctly assigns labels., test_labelling_distinct()

### Community 947 - "Community 947"
Cohesion: 1.00
Nodes (2): Tests if np.inf and np.nan data are each treated as special outliers., test_outlier_data()

### Community 948 - "Community 948"
Cohesion: 1.00
Nodes (2): Tests that the `_do_labelling` helper function correctly thresholds the     inco, test_labelling_thresholding()

### Community 949 - "Community 949"
Cohesion: 1.00
Nodes (2): Check that we raise an error if the centers are requested together with     a pr, test_hdbscan_error_precomputed_and_store_centers()

### Community 950 - "Community 950"
Cohesion: 1.00
Nodes (2): Test that HDBSCAN works with the "cosine" metric when the algorithm is set     t, test_hdbscan_cosine_metric_valid_algorithm()

### Community 951 - "Community 951"
Cohesion: 1.00
Nodes (2): Test that HDBSCAN raises an informative error is raised when an unsupported, test_hdbscan_cosine_metric_invalid_algorithm()

### Community 952 - "Community 952"
Cohesion: 1.00
Nodes (2): Check the tie breaking behavior of the most frequent strategy.      Non-regressi, test_most_frequent_tie_object()

### Community 953 - "Community 953"
Cohesion: 1.00
Nodes (2): Check the behaviour of the iterative imputer with different initial strategy, test_iterative_imputer_keep_empty_features()

### Community 954 - "Community 954"
Cohesion: 1.00
Nodes (2): Check that we propagate properly the parameter `fill_value`., test_iterative_imputer_constant_fill_value()

### Community 955 - "Community 955"
Cohesion: 1.00
Nodes (2): Check that we properly apply the empty feature mask to `min_value` and     `max_, test_iterative_imputer_min_max_value_remove_empty()

### Community 956 - "Community 956"
Cohesion: 1.00
Nodes (2): Check the behaviour of `keep_empty_features` for `KNNImputer`., test_knn_imputer_keep_empty_features()

### Community 957 - "Community 957"
Cohesion: 1.00
Nodes (2): Check that missing indicator return the feature names with a prefix., test_missing_indicator_feature_names_out()

### Community 958 - "Community 958"
Cohesion: 1.00
Nodes (2): Check transform uses object dtype when fitted on an object dtype.      Non-regre, test_imputer_lists_fit_transform()

### Community 959 - "Community 959"
Cohesion: 1.00
Nodes (2): Check transform preserves numeric dtype independent of fit dtype., test_imputer_transform_preserves_numeric_dtype()

### Community 960 - "Community 960"
Cohesion: 1.00
Nodes (2): Check the behaviour of `keep_empty_features` with all strategies but     'consta, test_simple_imputer_keep_empty_features()

### Community 961 - "Community 961"
Cohesion: 1.00
Nodes (2): Check that we raise a proper error message when we cannot cast the fill value, test_simple_imputer_constant_fill_value_casting()

### Community 962 - "Community 962"
Cohesion: 1.00
Nodes (2): Check the behaviour of `keep_empty_features` with no empty features.      With n, test_iterative_imputer_no_empty_features()

### Community 963 - "Community 963"
Cohesion: 1.00
Nodes (2): Check the behaviour of `keep_empty_features` in the presence of empty features., test_iterative_imputer_with_empty_features()

### Community 965 - "Community 965"
Cohesion: 1.00
Nodes (2): Check that init works with numpy scalar strings.      Non-regression test for #2, test_kmeans_with_array_like_or_np_scalar_init()

### Community 966 - "Community 966"
Cohesion: 1.00
Nodes (2): Check `feature_names_out` for `KMeans` and `MiniBatchKMeans`., test_feature_names_out()

### Community 967 - "Community 967"
Cohesion: 1.00
Nodes (2): Check that predict does not change cluster centers.      Non-regression test for, test_predict_does_not_change_cluster_centers()

### Community 968 - "Community 968"
Cohesion: 1.00
Nodes (2): Check that sample weight is used during init.      `_init_centroids` is shared a, test_sample_weight_init()

### Community 969 - "Community 969"
Cohesion: 1.00
Nodes (2): Check that if sample weight is 0, this sample won't be chosen.      `_init_centr, test_sample_weight_zero()

### Community 970 - "Community 970"
Cohesion: 1.00
Nodes (2): Check that kmeans stops when there are more centers than non-duplicate samples, test_relocating_with_duplicates()

### Community 971 - "Community 971"
Cohesion: 1.00
Nodes (2): Check that `n_init="auto"` chooses the right number of initializations.     Non-, test_kmeans_init_auto_with_initial_centroids()

### Community 972 - "Community 972"
Cohesion: 1.00
Nodes (2): _sort_centers(), test_weighted_vs_repeated()

### Community 975 - "Community 975"
Cohesion: 1.00
Nodes (2): Check partial fit does not fail after fit when early_stopping=True.      Non-reg, test_mlp_partial_fit_after_fit()

### Community 976 - "Community 976"
Cohesion: 1.00
Nodes (2): Test that a diverging model does not raise errors when early stopping is enabled, test_mlp_diverging_loss()

### Community 977 - "Community 977"
Cohesion: 1.00
Nodes (2): Test MLP with Poisson loss and no hidden layer equals GLM., test_mlp_vs_poisson_glm_equivalent()

### Community 978 - "Community 978"
Cohesion: 1.00
Nodes (2): Check error message when the validation set is too small., test_minimum_input_sample_size()

### Community 979 - "Community 979"
Cohesion: 1.00
Nodes (2): Check that labels can be strings when `early_stopping=True`.      Non-regression, test_mlp_early_stopping_string_labels()

### Community 980 - "Community 980"
Cohesion: 1.00
Nodes (2): Loading from MLP and partial fitting updates weights. Non-regression     test fo, test_mlp_loading_from_joblib_partial_fit()

### Community 981 - "Community 981"
Cohesion: 1.00
Nodes (2): Check that feature names are preserved when early stopping is enabled.      Feat, test_preserve_feature_names()

### Community 982 - "Community 982"
Cohesion: 1.00
Nodes (2): Check that early stopping works with warm start., test_mlp_warm_start_with_early_stopping()

### Community 983 - "Community 983"
Cohesion: 1.00
Nodes (2): Check that we stop the number of iteration at `max_iter` when warm starting., test_mlp_warm_start_no_convergence()

### Community 984 - "Community 984"
Cohesion: 1.00
Nodes (2): Test error is raised for mixed string and numerical input and dispatch enabled., test_unique_labels_mixed_str_numerical_array_api()

### Community 985 - "Community 985"
Cohesion: 1.00
Nodes (2): Check `unique_labels` compliance for array API., test_unique_labels_array_api()

### Community 986 - "Community 986"
Cohesion: 1.00
Nodes (2): Check that we raise a warning when the number of unique classes is greater than, test_check_classification_targets_too_many_unique_classes()

### Community 987 - "Community 987"
Cohesion: 1.00
Nodes (2): Check that type_of_target works with pandas nullable dtypes., test_type_of_target_pandas_nullable()

### Community 988 - "Community 988"
Cohesion: 1.00
Nodes (2): Checks that unique_labels work with pandas nullable dtypes.      Non-regression, test_unique_labels_pandas_nullable()

### Community 989 - "Community 989"
Cohesion: 1.00
Nodes (2): Test whether points lying on boundary are handled consistently      Also ensures, test_radius_neighbors_boundary_handling()

### Community 990 - "Community 990"
Cohesion: 1.00
Nodes (2): Weight function to replace lambda d: d ** -2.     The lambda function is not val, _weight_func()

### Community 991 - "Community 991"
Cohesion: 1.00
Nodes (2): Additional parameter validation for *Neighbors* estimators not covered by common, test_neighbors_validate_parameters()

### Community 992 - "Community 992"
Cohesion: 1.00
Nodes (2): Validation of all classes extending NeighborsBase with     Minkowski semi-metric, test_neighbors_minkowski_semimetric_algo_warn()

### Community 993 - "Community 993"
Cohesion: 1.00
Nodes (2): Check that we raise a proper error if `algorithm!='brute'` and `p<1`., test_neighbors_minkowski_semimetric_algo_error()

### Community 994 - "Community 994"
Cohesion: 1.00
Nodes (2): Validate parameter of NearestNeighbors., test_nearest_neighbors_validate_params()

### Community 995 - "Community 995"
Cohesion: 1.00
Nodes (2): Ensures that `predict` works for array-likes when `weights` is a callable., test_regressor_predict_on_arraylikes()

### Community 996 - "Community 996"
Cohesion: 1.00
Nodes (2): Check that the different neighbor estimators are lenient towards `nan`     value, test_nan_euclidean_support()

### Community 997 - "Community 997"
Cohesion: 1.00
Nodes (2): Check that KNN predict works with dataframes      non-regression test for issue, test_predict_dataframe()

### Community 998 - "Community 998"
Cohesion: 1.00
Nodes (2): Check that NearestNeighbors works with :math:`p \\in (0,1)` when `algorithm`, test_nearest_neighbours_works_with_p_less_than_1()

### Community 999 - "Community 999"
Cohesion: 1.00
Nodes (2): Check that `predict` and `predict_proba` raises on sample of all zeros weights., test_KNeighborsClassifier_raise_on_all_zero_weights()

### Community 1000 - "Community 1000"
Cohesion: 1.00
Nodes (2): Check that `predict` and related functions work fine with X=None      Calling pr, test_neighbor_classifiers_loocv()

### Community 1001 - "Community 1001"
Cohesion: 1.00
Nodes (2): Check that `predict` and related functions work fine with X=None, test_neighbor_regressors_loocv()

### Community 1002 - "Community 1002"
Cohesion: 1.00
Nodes (2): Ensure KNeighborsClassifier(algorithm='brute') works with string labels.      No, test_neighbors_classifier_with_string_labels()

### Community 1003 - "Community 1003"
Cohesion: 1.00
Nodes (2): Check that a warning is raised when multiple versions exist and no version is, test_fetch_openml_iris_warn_multiple_version()

### Community 1004 - "Community 1004"
Cohesion: 1.00
Nodes (2): Check that we can get a dataset without target., test_fetch_openml_no_target()

### Community 1005 - "Community 1005"
Cohesion: 1.00
Nodes (2): check that missing values in categories are compatible with pandas     categoric, test_missing_values_pandas()

### Community 1006 - "Community 1006"
Cohesion: 1.00
Nodes (2): Check that we raise a warning when the dataset is inactive., test_fetch_openml_inactive()

### Community 1007 - "Community 1007"
Cohesion: 1.00
Nodes (2): Check that we can overwrite the default parameters of `read_csv`., test_fetch_openml_overwrite_default_params_read_csv()

### Community 1008 - "Community 1008"
Cohesion: 1.00
Nodes (2): Check that we can load the "zoo" dataset.     Non-regression test for:     https, test_fetch_openml_with_ignored_feature()

### Community 1009 - "Community 1009"
Cohesion: 1.00
Nodes (2): Check that we strip the single quotes when used as a string delimiter.      Non-, test_fetch_openml_strip_quotes()

### Community 1010 - "Community 1010"
Cohesion: 1.00
Nodes (2): Check that we can strip leading whitespace in pandas parser.      Non-regression, test_fetch_openml_leading_whitespace()

### Community 1011 - "Community 1011"
Cohesion: 1.00
Nodes (2): Check that we can handle escapechar and single/double quotechar.      Non-regres, test_fetch_openml_quotechar_escapechar()

### Community 1012 - "Community 1012"
Cohesion: 1.00
Nodes (2): Check the behaviour of `fetch_openml` with `as_frame=True`.      Fetch by ID and, test_fetch_openml_as_frame_true()

### Community 1013 - "Community 1013"
Cohesion: 1.00
Nodes (2): Check the behaviour of `fetch_openml` with `as_frame=False`.      Fetch both by, test_fetch_openml_as_frame_false()

### Community 1014 - "Community 1014"
Cohesion: 1.00
Nodes (2): Check the consistency of the LIAC-ARFF and pandas parsers., test_fetch_openml_consistency_parser()

### Community 1015 - "Community 1015"
Cohesion: 1.00
Nodes (2): Check the equivalence of the dataset when using `as_frame=False` and     `as_fra, test_fetch_openml_equivalence_array_dataframe()

### Community 1016 - "Community 1016"
Cohesion: 1.00
Nodes (2): Check fetching on a numerical only dataset with string labels., test_fetch_openml_iris_pandas()

### Community 1017 - "Community 1017"
Cohesion: 1.00
Nodes (2): Check that we can force the target to not be the default target., test_fetch_openml_forcing_targets()

### Community 1018 - "Community 1018"
Cohesion: 1.00
Nodes (2): Check the behaviour of `return_X_y=True` when `as_frame=True`., test_fetch_openml_equivalence_frame_return_X_y()

### Community 1019 - "Community 1019"
Cohesion: 1.00
Nodes (2): Check the behaviour of `return_X_y=True` when `as_frame=False`., test_fetch_openml_equivalence_array_return_X_y()

### Community 1020 - "Community 1020"
Cohesion: 1.00
Nodes (2): Check the difference between liac-arff and pandas parser., test_fetch_openml_difference_parsers()

### Community 1021 - "Community 1021"
Cohesion: 1.00
Nodes (2): Check that `fetch_openml` infer the right number of categories, integers, and, test_fetch_openml_types_inference()

### Community 1022 - "Community 1022"
Cohesion: 1.00
Nodes (2): check_pairwise_distances_chunked(), test_pairwise_distances_chunked()

### Community 1023 - "Community 1023"
Cohesion: 1.00
Nodes (2): Check that `nan_euclidean` is lenient with `nan` values., test_nan_euclidean_support()

### Community 1024 - "Community 1024"
Cohesion: 1.00
Nodes (2): Check that the behavior of constant input is the same in the case of     full of, test_nan_euclidean_constant_input_argmin()

### Community 1025 - "Community 1025"
Cohesion: 1.00
Nodes (2): Check pairwise_distances with lists of strings as input., test_pairwise_dist_custom_metric_for_string()

### Community 1026 - "Community 1026"
Cohesion: 1.00
Nodes (2): Check that pairwise_distances does not convert boolean input to float     when u, test_pairwise_dist_custom_metric_for_bool()

### Community 1027 - "Community 1027"
Cohesion: 1.00
Nodes (2): Check that Y_norm_squared is correctly sliced alongside Y.      Non-regression t, test_parallel_pairwise_distances_y_norm_squared()

### Community 1028 - "Community 1028"
Cohesion: 1.00
Nodes (2): test_check_tuple_input(), tuplify()

### Community 1029 - "Community 1029"
Cohesion: 1.00
Nodes (2): Check that "auto" and "arpack" solvers are equivalent for sparse inputs., test_sparse_pca_auto_arpack_singular_values_consistency()

### Community 1030 - "Community 1030"
Cohesion: 1.00
Nodes (2): Check that exposing and setting `n_oversamples` will provide accurate results, test_pca_randomized_svd_n_oversamples()

### Community 1031 - "Community 1031"
Cohesion: 1.00
Nodes (2): Check feature names out for PCA., test_feature_names_out()

### Community 1032 - "Community 1032"
Cohesion: 1.00
Nodes (2): Check the accuracy of PCA's internal variance calculation, test_variance_correctness()

### Community 1034 - "Community 1034"
Cohesion: 1.00
Nodes (2): ols_ridge_dataset(), Dataset with OLS and Ridge solutions, well conditioned X.      The construction

### Community 1035 - "Community 1035"
Cohesion: 1.00
Nodes (2): Check that passing an array for alpha works with array API dispatch.      Non-re, test_ridge_per_target_alpha_array_api()

### Community 1036 - "Community 1036"
Cohesion: 1.00
Nodes (2): Test that Ridge converges for all solvers to correct solution.      We work with, test_ridge_regression()

### Community 1037 - "Community 1037"
Cohesion: 1.00
Nodes (2): Check class_weights resemble sample_weights behavior., test_class_weight_vs_sample_weight()

### Community 1038 - "Community 1038"
Cohesion: 1.00
Nodes (2): Check alpha=0.0 raises error only when `cv=None`., test_ridgecv_alphas_zero()

### Community 1039 - "Community 1039"
Cohesion: 1.00
Nodes (2): Check the `alphas` validation in RidgeCV and RidgeClassifierCV., test_ridgecv_alphas_validation()

### Community 1040 - "Community 1040"
Cohesion: 1.00
Nodes (2): Check the case when `alphas` is a scalar.     This case was supported in the pas, test_ridgecv_alphas_scalar()

### Community 1041 - "Community 1041"
Cohesion: 1.00
Nodes (2): check if all combinations of arguments give valid estimations, test_ridge_regression_check_arguments_validity()

### Community 1042 - "Community 1042"
Cohesion: 1.00
Nodes (2): Test that Ridge converges for all solvers to correct solution on hstacked data., test_ridge_regression_hstacked_X()

### Community 1043 - "Community 1043"
Cohesion: 1.00
Nodes (2): Check that multilabel classification is supported and give meaningful     result, test_ridgeclassifier_multilabel()

### Community 1044 - "Community 1044"
Cohesion: 1.00
Nodes (2): Test that positive Ridge finds true positive coefficients., test_ridge_positive_regression_test()

### Community 1045 - "Community 1045"
Cohesion: 1.00
Nodes (2): Test that Ridge w/wo positive converges to the same solution.      Ridge with po, test_ridge_ground_truth_positive_test()

### Community 1046 - "Community 1046"
Cohesion: 1.00
Nodes (2): Test input validation for positive argument in Ridge., test_ridge_positive_error_test()

### Community 1047 - "Community 1047"
Cohesion: 1.00
Nodes (2): Check ridge loss consistency when positive argument is enabled., test_positive_ridge_loss()

### Community 1048 - "Community 1048"
Cohesion: 1.00
Nodes (2): Test that LBGFS gets almost the same coef of svd when positive=False., test_lbfgs_solver_consistency()

### Community 1049 - "Community 1049"
Cohesion: 1.00
Nodes (2): Test that LBFGS solver raises ConvergenceWarning., test_lbfgs_solver_error()

### Community 1050 - "Community 1050"
Cohesion: 1.00
Nodes (2): Test that the impact of sample_weight is consistent.      Note that this test is, test_ridge_sample_weight_consistency()

### Community 1051 - "Community 1051"
Cohesion: 1.00
Nodes (2): Check that the predictions stored in `cv_results_` are on the original scale., test_ridge_cv_results_predictions()

### Community 1052 - "Community 1052"
Cohesion: 1.00
Nodes (2): Test that Ridge converges for all solvers to correct solution on vstacked data., test_ridge_regression_vstacked_X()

### Community 1053 - "Community 1053"
Cohesion: 1.00
Nodes (2): Check that `RidgeCV` works properly with multioutput and sample_weight     when, test_ridge_cv_multioutput_sample_weight()

### Community 1054 - "Community 1054"
Cohesion: 1.00
Nodes (2): Check that `RidgeCV` works properly with a custom multioutput scorer., test_ridge_cv_custom_multioutput_scorer()

### Community 1055 - "Community 1055"
Cohesion: 1.00
Nodes (2): Test that `RidgeCV` or `RidgeClassifierCV` with default `scoring`     argument (, test_metadata_routing_with_default_scoring()

### Community 1056 - "Community 1056"
Cohesion: 1.00
Nodes (2): Test that `set_score_request` is set within `RidgeCV.fit()` and     `RidgeClassi, test_set_score_request_with_default_scoring()

### Community 1057 - "Community 1057"
Cohesion: 1.00
Nodes (2): Test that unpenalized Ridge = OLS converges for all solvers to correct solution., test_ridge_regression_unpenalized()

### Community 1058 - "Community 1058"
Cohesion: 1.00
Nodes (2): Test that unpenalized Ridge = OLS converges for all solvers to correct solution., test_ridge_regression_unpenalized_hstacked_X()

### Community 1059 - "Community 1059"
Cohesion: 1.00
Nodes (2): Test that unpenalized Ridge = OLS converges for all solvers to correct solution., test_ridge_regression_unpenalized_vstacked_X()

### Community 1060 - "Community 1060"
Cohesion: 1.00
Nodes (2): Test that Ridge with sample weights gives correct results.      We use the follo, test_ridge_regression_sample_weights()

### Community 1061 - "Community 1061"
Cohesion: 1.00
Nodes (2): non-regression test for gh #25249, test_sgd_verbose()

### Community 1062 - "Community 1062"
Cohesion: 1.00
Nodes (2): Test that SGD raises with forbidden loss for passive-aggressive algo., test_learning_rate_PA_raises()

### Community 1063 - "Community 1063"
Cohesion: 1.00
Nodes (2): Check that l1_ratio is not used when penalty is not 'elasticnet, test_sgd_l1_ratio_not_used()

### Community 1064 - "Community 1064"
Cohesion: 1.00
Nodes (2): Check that a warning is raised when `power_t` is negative., test_power_t_limits()

### Community 1065 - "Community 1065"
Cohesion: 1.00
Nodes (2): Check that the shape of `coef_init` is validated., test_provide_coef()

### Community 1066 - "Community 1066"
Cohesion: 1.00
Nodes (2): Check that `intercept_init` or `offset_init` is validated., test_set_intercept_offset()

### Community 1067 - "Community 1067"
Cohesion: 1.00
Nodes (2): Check that we raise an error for `early_stopping` used with     `partial_fit`., test_sgd_early_stopping_with_partial_fit()

### Community 1068 - "Community 1068"
Cohesion: 1.00
Nodes (2): Check that we can pass a scaler with binary classification to     `intercept_ini, test_set_intercept_offset_binary()

### Community 1069 - "Community 1069"
Cohesion: 1.00
Nodes (2): _check_time_series_max_train_size(), test_time_series_max_train_size()

### Community 1070 - "Community 1070"
Cohesion: 1.00
Nodes (2): Check for integer overflow on 32-bit platforms.      Non-regression test for:, test_train_test_split_32bit_overflow()

### Community 1071 - "Community 1071"
Cohesion: 1.00
Nodes (2): Check get_metadata_routing returns the correct MetadataRouter., test_splitter_get_metadata_routing()

### Community 1072 - "Community 1072"
Cohesion: 1.00
Nodes (2): Check set_split_request is defined for group splitters and not for others., test_splitter_set_split_request()

### Community 1073 - "Community 1073"
Cohesion: 1.00
Nodes (2): Test if predict breaks ties in OVR mode.     Related issue: https://github.com/s, test_svc_ovr_tie_breaking()

### Community 1074 - "Community 1074"
Cohesion: 1.00
Nodes (2): Test using a custom kernel that is not fed with array-like for floats, test_custom_kernel_not_array_input()

### Community 1075 - "Community 1075"
Cohesion: 1.00
Nodes (2): Check that SVC raises error when internal representation is altered.      Non-re, test_svc_raises_error_internal_representation()

### Community 1076 - "Community 1076"
Cohesion: 1.00
Nodes (2): Check that we can pass `C=inf` that is equivalent to a very large C value., test_svm_with_infinite_C()

### Community 1077 - "Community 1077"
Cohesion: 1.00
Nodes (2): Test that accessing probA_ and probB_ raises FutureWarning for SVC and NuSVC., test_svc_nusvc_probA_probB_deprecated()

### Community 1079 - "Community 1079"
Cohesion: 1.00
Nodes (2): Make sure that TSNE works for different distance metrics, test_tsne_with_different_distance_metrics()

### Community 1080 - "Community 1080"
Cohesion: 1.00
Nodes (2): Make sure that the n_jobs parameter doesn't impact the output, test_tsne_n_jobs()

### Community 1081 - "Community 1081"
Cohesion: 1.00
Nodes (2): Make sure that method_parameters works with mahalanobis distance., test_tsne_with_mahalanobis_distance()

### Community 1082 - "Community 1082"
Cohesion: 1.00
Nodes (2): Make sure that perplexity > n_samples results in a ValueError, test_tsne_perplexity_validation()

### Community 1083 - "Community 1083"
Cohesion: 1.00
Nodes (2): Make sure that TSNE works when the output is set to "pandas".      Non-regressio, test_tsne_works_with_pandas_output()

### Community 1084 - "Community 1084"
Cohesion: 1.00
Nodes (2): Raise an error when n_neighbors >= n_samples / 2.      Non-regression test for #, test_trustworthiness_n_neighbors_error()

### Community 1085 - "Community 1085"
Cohesion: 1.00
Nodes (2): t-SNE should give a lower KL divergence with more iterations., test_optimization_minimizes_kl_divergence()

### Community 1086 - "Community 1086"
Cohesion: 1.00
Nodes (2): Make sure that TSNE works identically for sparse and dense matrix, test_sparse_precomputed_distance()

### Community 1088 - "Community 1088"
Cohesion: 1.00
Nodes (1): Decision tree based models for classification and regression.

### Community 1089 - "Community 1089"
Cohesion: 1.00
Nodes (1): ======================================================== Post pruning decision t

### Community 1090 - "Community 1090"
Cohesion: 1.00
Nodes (1): ======================================================================= Plot the

### Community 1091 - "Community 1091"
Cohesion: 1.00
Nodes (1): ======================== Decision Tree Regression ======================== In th

### Community 1092 - "Community 1092"
Cohesion: 1.00
Nodes (1): ========================================= Understanding the decision tree struct

### Community 1093 - "Community 1093"
Cohesion: 1.00
Nodes (2): _apply_on_subsets(), check_methods_subset_invariance()

### Community 1094 - "Community 1094"
Cohesion: 1.00
Nodes (2): check_regressor_multioutput(), _is_pairwise_metric()

### Community 1095 - "Community 1095"
Cohesion: 1.00
Nodes (1): Checks the bundled license is installed with the wheel.

## Knowledge Gaps
- **1348 isolated node(s):** `Benchmark suite for scikit-learn using ASV`, `Get benchmarks configuration from the config.json file`, `Get path of pickled fitted estimator`, `Clean the tmp directory`, `Abstract base class for all the benchmarks` (+1343 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 46`** (1 nodes): `# TODO: remove mark once loky bug is fixed:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (1 nodes): `Test the split module`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (2 nodes): `_test_warm_start()`, `test_warm_start_multiclass()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 90`** (2 nodes): `# TODO: explain what this is testing`, `# TODO: explain what this is testing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 110`** (1 nodes): `Testing for Multi-layer Perceptron module (sklearn.neural_network)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 162`** (2 nodes): `Make sure bin mapper treats negative categories as missing values.`, `test_categorical_feature_negative_missing()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 171`** (2 nodes): `# TODO:`, `# TODO: The high number of iterations are required for convergence and show room`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 187`** (2 nodes): `DensityMixin`, `BaseMixture`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 189`** (2 nodes): `Check that we can fit a line where all samples are inliers.     Non-regression t`, `test_perfect_horizontal_line()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 196`** (2 nodes): `Check `n_nonzero_coefs_` correct when `tol` is and isn't set.`, `test_estimator_n_nonzero_coefs()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 217`** (2 nodes): `# TODO: replace this torch/MPS-specific coverage by array-api-strict once`, `# TODO: add cupy to the list of libraries once the following upstream issue`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 233`** (2 nodes): `# TODO: Inspect slight numerical discrepancy`, `# TODO: Inspect slight numerical discrepancy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 236`** (2 nodes): `_check_gcv_mode()`, `_RidgeGCV`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 257`** (1 nodes): `BaseDecisionTree`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 263`** (1 nodes): `LatentDirichletAllocation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 269`** (1 nodes): `Version`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 276`** (2 nodes): `Test that custom weights raise an error for single-output data.`, `test__check_reg_targets_single_output_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 289`** (2 nodes): `_BaseEncoder`, `OrdinalEncoder`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 292`** (2 nodes): `Check `get_feature_names_out` for `BernoulliRBM`.`, `test_feature_names_out()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 297`** (2 nodes): `_assign_where()`, `IterativeImputer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 304`** (2 nodes): `Testing for mean shift clustering methods`, `# TODO: remove mark once loky bug is fixed:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 308`** (1 nodes): `Test truncated SVD transformer.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 323`** (2 nodes): `FunctionTransformer`, `_identity()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 327`** (1 nodes): `test the label propagation module`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 342`** (2 nodes): `========================================================== Comparison of kernel`, `============================================= Comparison of kernel ridge regress`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 345`** (1 nodes): `LocalOutlierFactor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 360`** (2 nodes): `FactorAnalysis`, `_ortho_rotation()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 361`** (1 nodes): `KernelPCA`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 366`** (2 nodes): `NegativeInfinityType`, `Vendoered from https://github.com/pypa/packaging/blob/main/packaging/_structures`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 412`** (1 nodes): `NeighborhoodComponentsAnalysis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 414`** (1 nodes): `InfinityType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 416`** (1 nodes): `QuantileTransformer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 420`** (1 nodes): `This is testing the equivalence between some estimators with internal nearest ne`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 429`** (2 nodes): `MinimalClassifier`, `Minimal classifier implementation without inheriting from BaseEstimator.      Th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 434`** (2 nodes): `DiscriminantAnalysisPredictionMixin`, `NearestCentroid`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 436`** (2 nodes): `Transformers for missing value imputation.`, `KNNImputer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 437`** (2 nodes): `_dynamic_max_trials()`, `RANSACRegressor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 439`** (1 nodes): `_BaseChain`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 454`** (2 nodes): `MinimalRegressor`, `Minimal regressor implementation without inheriting from BaseEstimator.      Thi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 455`** (2 nodes): `MinimalTransformer`, `Minimal transformer implementation without inheriting from     BaseEstimator.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 465`** (2 nodes): `Data embedding techniques.`, `SpectralEmbedding`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 466`** (1 nodes): `Isomap`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 469`** (1 nodes): `_BaseVersion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 475`** (2 nodes): `_BaseComposition`, `Base class for estimators that are composed of named sub-estimators.      This a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 480`** (2 nodes): `bench_scikit_transformer()`, `compute_time()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 484`** (1 nodes): `KernelDensity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 485`** (1 nodes): `StandardScaler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 503`** (1 nodes): `Benchmark SGD prediction time with dense/sparse coefficients.  Invoke with -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 505`** (2 nodes): `GradientBoostingClassifierBenchmark`, `Benchmarks for GradientBoostingClassifier.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 506`** (2 nodes): `LinearRegressionBenchmark`, `Benchmarks for Linear Regression.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 507`** (2 nodes): `LogisticRegressionBenchmark`, `Benchmarks for LogisticRegression.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 511`** (2 nodes): `Directive`, `AllowNanEstimators`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 520`** (1 nodes): `ClassDoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 528`** (2 nodes): `_SparseSGDClassifier`, `test_sgd_proba()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 537`** (2 nodes): `n()`, `s()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 541`** (1 nodes): `=============================================================== Model selection`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 542`** (2 nodes): `Sort example gallery by title of subsection.      Assumes README.txt exists for`, `SubSectionTitleOrder`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 556`** (1 nodes): `KernelCenterer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 560`** (1 nodes): `doilinks ~~~~~~~~ Extension to add links to DOIs. With this extension you can us`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 561`** (2 nodes): `SimpleEstimatorCustomLogic`, `test_custom_conversion_estimator_to_array_api_strict()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 563`** (1 nodes): `Test the california_housing loader, if the data is available, or if specifically`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 564`** (2 nodes): `Check that warning is raised when working_memory is too low.`, `test_get_chunk_n_rows_warns()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 567`** (1 nodes): `# TODO: We are not entirely satisfied with this lax comparison, but the root`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 568`** (1 nodes): `Test the covtype loader, if the data is available, or if specifically requested`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 569`** (2 nodes): `1. Check that an error is raised when both y_score and y_pred are specified.`, `test_y_score_and_y_pred_specified_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 584`** (1 nodes): `=========================================== Lagged features for time series fore`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 592`** (2 nodes): `Merge this context with `other_context`.          This method is called on a sub`, `Private constructor to create a root context.          Parameters         ------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 602`** (1 nodes): `==================================================== Imputing missing values bef`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 607`** (1 nodes): `================================= Gaussian Mixture Model Sine Curve ============`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 615`** (2 nodes): `override_pst_pagetoc()`, `Overrides the `generate_toc_html` function of pydata-sphinx-theme for API.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 620`** (2 nodes): `_DummyPath`, `Minimal class that implements the os.PathLike interface.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 622`** (2 nodes): `SingleInheritanceEstimator`, `test_pickling_works_when_getstate_is_overwritten_in_the_child_class()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 623`** (1 nodes): `Testing for the utility function _get_n_samples_bootstrap`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 624`** (2 nodes): `Check that Cython extension types have a correct ``__module__``.      When a sub`, `test_extension_type_module()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 630`** (2 nodes): `Test that min_norm_subgradient raises on wrong input.`, `test_min_norm_subgradient_raises()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 635`** (2 nodes): `Check that worst case inputs do not exceed the recursion stack limit.`, `test_simultaneous_sort_no_stackoverflow()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 637`** (2 nodes): `Klass`, `Function f          Parameter         ---------         a : int             Para`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 642`** (1 nodes): `ContainerAdaptersManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 651`** (1 nodes): `Benchmarks of Lasso vs LassoLars  First, we fix a training set and increase the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 653`** (1 nodes): `Benchmarks of Lasso regularization path computation using Lars and CD  The input`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 654`** (1 nodes): `Benchmarks of orthogonal matching pursuit (:ref:`OMP`) versus least angle regres`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 655`** (1 nodes): `Benchmarks of Singular Value Decomposition (Exact and Approximate)  The data is`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 656`** (1 nodes): `Module to give helpful messages to the user that did not compile scikit-learn pr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 657`** (1 nodes): `Agglomerative clustering with different metrics ================================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 658`** (1 nodes): `============================================================================= Va`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 659`** (1 nodes): `============================================================ Empirical evaluatio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 660`** (1 nodes): `====================================================== Effect of transforming th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 661`** (1 nodes): `Utilities to load popular datasets and artificial data generators.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 662`** (1 nodes): `============================================== Plot randomly generated multilabe`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 663`** (1 nodes): `============================ Faces dataset decompositions ======================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 664`** (1 nodes): `========================== FastICA on 2D point clouds ==========================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 665`** (2 nodes): `============================= OOB Errors for Random Forests ====================`, `# NOTE: Setting the `warm_start` construction parameter to `True` disables`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 666`** (1 nodes): `============================================== Features in Histogram Gradient Bo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 667`** (1 nodes): `Close PRs labeled with 'autoclose' more than 14 days ago.  Called from .github/w`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 668`** (2 nodes): `This module contains the TreePredictor class which is used for prediction.`, `# TODO: consider always using platform agnostic dtypes for fitted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 669`** (1 nodes): `================================================================= Permutation Im`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 670`** (1 nodes): `============================================ Curve Fitting with Bayesian Ridge R`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 671`** (1 nodes): `======================================== Plot multi-class SGD on the iris datase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 672`** (1 nodes): `========================== SGD: convex loss functions ==========================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 673`** (1 nodes): `=============== GMM covariances ===============  Demonstration of several covari`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 674`** (1 nodes): `========================== GMM Initialization Methods ==========================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 675`** (1 nodes): `================================= Gaussian Mixture Model Ellipsoids ============`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 676`** (2 nodes): `Generate indices to split data into training and test set.          Parameters`, `Generate indices to split data into training and test set.          Yields`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 677`** (2 nodes): `Generate indices to split data into training and test set.          Parameters`, `Generate indices to split data into training and test set.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 678`** (1 nodes): `=================================== Simple 1D Kernel Density Estimation ========`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 680`** (1 nodes): `============================= Importance of Feature Scaling ====================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 681`** (1 nodes): `============================================ Comparing Target Encoder with Other`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 682`** (1 nodes): `======================================== Release Highlights for scikit-learn 0.2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 683`** (2 nodes): `_features_html()`, `Generate HTML representation of feature names.      Creates a collapsible HTML d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 684`** (1 nodes): `========================================================= Plot classification bo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 686`** (1 nodes): `CustomBinaryEstimator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 687`** (1 nodes): `CustomContinuousEstimator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 688`** (1 nodes): `CustomMulticlassEstimator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 689`** (2 nodes): `Check that bunch raises deprecation message with `__getattr__`.`, `test_bunch_attribute_deprecation()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 690`** (1 nodes): `Smoke Test the check_build module`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 691`** (1 nodes): `Tests for making sure experimental imports work as expected.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 692`** (1 nodes): `Tests for making sure experimental imports work as expected.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 693`** (1 nodes): `Tests for making sure experimental imports work as expected.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 694`** (2 nodes): `Test Cython's weighted Fenwick tree implementation`, `test_cython_weighted_fenwick_tree()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 696`** (1 nodes): `Test Olivetti faces fetcher, if the data is available, or if specifically reques`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 698`** (1 nodes): `Test the rcv1 loader, if the data is available, or if specifically requested via`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 701`** (2 nodes): `Check that the types defined in _typedefs correspond to the expected     numpy d`, `test_types()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 703`** (2 nodes): `Check the `dtype` consistency of `WeightVector`.`, `test_type_invariance()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 704`** (2 nodes): `_init_arpack_v0()`, `Initialize the starting vector for iteration in ARPACK functions.      Initializ`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 706`** (1 nodes): `==================================== Outlier detection on a real data set ======`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 707`** (1 nodes): `======================================= Visualizing the stock market structure =`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 708`** (1 nodes): `NumPy Array API compatibility library  This is a small wrapper around NumPy, CuP`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 711`** (1 nodes): `A comparison of different methods in GLM  Data comes from a random square matrix`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 712`** (1 nodes): `============================================================= Kernel PCA Solvers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 713`** (1 nodes): `========================================================== Kernel PCA Solvers co`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 714`** (1 nodes): `============================ LocalOutlierFactor benchmark ======================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 717`** (1 nodes): `Benchmark scikit-learn's Ward implement compared to SciPy's`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 718`** (1 nodes): `Benchmark suite for scikit-learn using ASV`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 719`** (1 nodes): `============================================= A demo of the Spectral Biclusterin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 720`** (1 nodes): `============================================== A demo of the Spectral Co-Cluster`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 721`** (1 nodes): `Method called after finishing the fit method of the estimator.          For auto`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 722`** (1 nodes): `Method called at the beginning of each fit task of the estimator.          Param`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 723`** (1 nodes): `Method called at the end of each fit task of the estimator.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 724`** (1 nodes): `Pre-order depth-first traversal of the task tree.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 725`** (1 nodes): `================================ Recognizing hand-written digits ===============`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 726`** (1 nodes): `================================================= Demo of affinity propagation c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 728`** (1 nodes): `================================= Compare BIRCH and MiniBatchKMeans ============`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 729`** (1 nodes): `============================================================= Bisecting K-Means`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 730`** (1 nodes): `========================================================= Comparing different cl`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 731`** (1 nodes): `====================================================================== A demo of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 732`** (1 nodes): `=================================== Demo of DBSCAN clustering algorithm ========`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 733`** (1 nodes): `Online learning of a dictionary of parts of faces ==============================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 734`** (1 nodes): `========================================================= Feature agglomeration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 735`** (1 nodes): `=========================== Vector Quantization Example ========================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 737`** (1 nodes): `==================================== Demonstration of k-means assumptions ======`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 738`** (1 nodes): `=========================================================== An example of K-Mean`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 739`** (1 nodes): `===============================================================================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 740`** (1 nodes): `================================================================ Comparing diffe`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 741`** (1 nodes): `============================================= A demo of the mean-shift clusterin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 742`** (1 nodes): `==================================================================== Comparison`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 743`** (1 nodes): `=================================== Demo of OPTICS clustering algorithm ========`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 744`** (1 nodes): `=========================================== Spectral clustering for image segmen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 745`** (1 nodes): `=================================================== Hierarchical clustering with`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 746`** (1 nodes): `JustComplex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 747`** (1 nodes): `======================================================================= Shrinkag`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 748`** (1 nodes): `============================= Ledoit-Wolf vs OAS estimation ====================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 749`** (1 nodes): `r""" ================================================================ Robust cov`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 750`** (1 nodes): `r""" ======================================= Robust vs Empirical covariance esti`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 751`** (1 nodes): `====================================== Sparse inverse covariance estimation ====`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 752`** (1 nodes): `=================================== Compare cross decomposition methods ========`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 756`** (1 nodes): `===================================== Blind source separation using FastICA ====`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 757`** (1 nodes): `=============== Incremental PCA ===============  Incremental principal component`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 758`** (1 nodes): `========== Kernel PCA ==========  This example shows the difference between the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 759`** (1 nodes): `================================================== Principal Component Analysis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 760`** (1 nodes): `=============================================================== Factor Analysis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 761`** (1 nodes): `====================================== Decision Tree Regression with AdaBoost ==`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 762`** (1 nodes): `================== Two-class AdaBoost ==================  This example fits an A`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 763`** (1 nodes): `=============================================================== Comparing Random`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 764`** (1 nodes): `========================================== Feature importances with a forest of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 765`** (1 nodes): `==================================================================== Plot the de`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 766`** (1 nodes): `=================================== Early stopping in Gradient Boosting ========`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 767`** (1 nodes): `============================ Gradient Boosting regression ======================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 768`** (1 nodes): `================================ Gradient Boosting regularization ==============`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 769`** (1 nodes): `======================= IsolationForest example =======================  An exam`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 770`** (1 nodes): `===================== Monotonic Constraints =====================  This example`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 771`** (1 nodes): `================================================= Plot individual and voting reg`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 772`** (1 nodes): `This is now a no-op and can be safely removed from your code.  It used to enable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 773`** (1 nodes): `This is now a no-op and can be safely removed from your code.  It used to enable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 774`** (1 nodes): `Importable modules that enable the use of experimental features or estimators.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 776`** (1 nodes): `External, bundled dependencies.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 777`** (1 nodes): `=========================================== Comparison of F-test and mutual info`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 778`** (1 nodes): `=================================================== Recursive feature eliminatio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 779`** (1 nodes): `Checks that dist/* contains the number of wheels built from the .github/workflow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 780`** (1 nodes): `This module implements histogram-based gradient boosting estimators.  The implem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 781`** (1 nodes): `=================================================== Failure of Machine Learning`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 782`** (1 nodes): `Internals of array-api-extra.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 783`** (1 nodes): `========================================================================== Fitti`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 784`** (1 nodes): `======================================================= HuberRegressor vs Ridge`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 785`** (1 nodes): `================================== L1-based models for Sparse Signals ==========`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 786`** (1 nodes): `============================== Lasso on dense and sparse data ==================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 787`** (1 nodes): `======================================== Lasso, Lasso-LARS, and Elastic Net path`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 788`** (1 nodes): `============================================== L1 Penalty and Sparsity in Logist`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 789`** (1 nodes): `============================================= Joint feature selection with multi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 790`** (1 nodes): `========================== Non-negative least squares ==========================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 791`** (1 nodes): `=========================================== Ordinary Least Squares and Ridge Reg`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 792`** (1 nodes): `=========================== Orthogonal Matching Pursuit ========================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 793`** (1 nodes): `=================== Quantile regression ===================  This example illust`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 794`** (1 nodes): `=========================================== Robust linear model estimation using`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 795`** (1 nodes): `========================================================= Ridge coefficients as`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 796`** (1 nodes): `=========================================================== Plot Ridge coefficie`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 797`** (1 nodes): `============== SGD: Penalties ==============  Contours of where the penalty is e`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 798`** (1 nodes): `========================================= SGD: Maximum margin separating hyperpl`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 799`** (1 nodes): `===================== SGD: Weighted samples =====================  Plot decision`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 800`** (1 nodes): `===================================================== MNIST classification using`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 801`** (1 nodes): `==================== Theil-Sen Regression ====================  Computes a Theil`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 803`** (1 nodes): `============================================= Manifold Learning methods on a sev`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 804`** (1 nodes): `========================= Multi-dimensional scaling =========================  A`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 805`** (1 nodes): `=================================== Swiss Roll And Swiss-Hole Reduction ========`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 806`** (1 nodes): `============================================================================= t-`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 807`** (1 nodes): `============================================== Face completion with a multi-outp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 808`** (1 nodes): `================================ ROC Curve with Visualization API ==============`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 809`** (1 nodes): `========================================= Density Estimation for a Gaussian mixt`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 810`** (1 nodes): `============================================================== Evaluate the perf`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 811`** (1 nodes): `==================================== Plotting Cross-Validated Predictions ======`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 812`** (1 nodes): `============================================================================ Dem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 813`** (1 nodes): `========================================= Nested versus non-nested cross-validat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 814`** (1 nodes): `================================================================= Test with perm`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 815`** (1 nodes): `============================================================= Receiver Operating`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 816`** (1 nodes): `================================================== Multiclass Receiver Operating`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 817`** (1 nodes): `Successive Halving Iterations =============================  This example illust`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 818`** (1 nodes): `========================================================= Effect of model regula`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 819`** (1 nodes): `========================= Kernel Density Estimation =========================  T`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 820`** (1 nodes): `================================================= Novelty detection with Local O`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 821`** (1 nodes): `=============================== Nearest Centroid Classification ================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 822`** (1 nodes): `============================ Nearest Neighbors regression ======================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 824`** (1 nodes): `========================================================== Demonstrating the dif`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 825`** (1 nodes): `================================================================ Using KBinsDisc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 826`** (1 nodes): `================================= Map data to a normal distribution ============`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 828`** (1 nodes): `========================================= Label Propagation digits: Active learn`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 829`** (1 nodes): `=================================================== Label Propagation digits: De`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 830`** (1 nodes): `======================================================= Label Propagation circle`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 831`** (1 nodes): `Distributor init file  Distributors: you can add custom code here to support par`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 832`** (1 nodes): `================================================== Plot different SVM classifier`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 833`** (1 nodes): `===================================== Plot the support vectors in LinearSVC ====`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 834`** (1 nodes): `========================================== One-class SVM with non-linear kernel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 835`** (1 nodes): `================================================= SVM: Separating hyperplane for`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 836`** (1 nodes): `========================================= SVM: Maximum margin separating hyperpl`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 837`** (1 nodes): `========================================================= SVM Margins Example ==`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 838`** (1 nodes): `=================================================================== Support Vect`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 839`** (1 nodes): `r""" ============================================== Scaling the regularization p`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 840`** (1 nodes): `========================================================= SVM Tie Breaking Examp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 843`** (2 nodes): `Test get_namespace on sparse arrays.`, `test_get_namespace_sparse_with_dispatch()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 844`** (2 nodes): `Test get_namespace for ArrayAPI arrays.`, `test_get_namespace_array_api()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 845`** (2 nodes): `Check conversion between various namespace-device-pairs.`, `test_move_to_array_api_conversions()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 846`** (2 nodes): `Check sparse inputs are handled correctly.`, `test_move_to_sparse()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 847`** (2 nodes): `Check NumPy arrays with negative strides can be moved to torch.`, `test_move_to_numpy_negative_strides_to_torch()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 848`** (2 nodes): `Test _asarray_with_order passes along order for NumPy arrays.`, `test_asarray_with_order()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 849`** (2 nodes): `Check NaN reductions like _nanmin and _nanmax`, `test_nan_reductions()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 850`** (2 nodes): `Check convert_to_numpy for GPU backed libraries.`, `test_convert_to_numpy_gpu()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 851`** (2 nodes): `Check convert_to_numpy for PyTorch CPU arrays.`, `test_convert_to_numpy_cpu()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 852`** (2 nodes): `Check that get_namespace returns NumPy wrapper`, `test_get_namespace_ndarray_or_similar_default()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 853`** (2 nodes): `Check expected behavior with device and creation functions.`, `test_get_namespace_ndarray_creation_device()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 854`** (2 nodes): `Check `_validate_diagonal_args` raises the correct errors.`, `test_validate_diagonal_args()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 855`** (2 nodes): `Check `_fill/add_to_diagonal` behaviour correct with numpy arrays.`, `test_fill_and_add_to_diagonal()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 856`** (2 nodes): `Test get_namespace on NumPy ndarrays.`, `test_get_namespace_ndarray_or_similar_default_with_dispatch()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 857`** (2 nodes): `Check array API `_fill_diagonal` consistent with `numpy._fill_diagonal`.`, `test_fill_diagonal()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 858`** (2 nodes): `Check `_add_to_diagonal` consistent between array API xp and numpy namespace.`, `test_add_to_diagonal()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 859`** (2 nodes): `Test get_namespace on dataframes and series.`, `test_get_namespace_df_with_dispatch()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 860`** (1 nodes): `test_pickling_when_getstate_is_overwritten_by_mixin_outside_of_sklearn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 861`** (2 nodes): `Check the behaviour of `allowed_extension` in `load_files`.`, `test_load_files_allowed_extensions()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 862`** (2 nodes): `Test to check that we load a scaled version by default but that we can     get a`, `test_load_diabetes_raw()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 863`** (2 nodes): `Test Poisson loss against well tested HalfPoissonLoss.`, `test_poisson_loss()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 864`** (2 nodes): `Check that we raise the ethical warning when trying to import `load_boston`.`, `test_load_boston_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 865`** (2 nodes): `Check retry mechanism in _fetch_remote.`, `test_fetch_remote_raise_warnings_with_invalid_url()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 866`** (2 nodes): `Check that LinearRegression is as good as `scipy.linalg.lstsq`.     Non regressi`, `test_linear_regression_vs_lstsq()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 867`** (2 nodes): `Test that the impact of sample_weight is consistent.      Note that this test is`, `test_linear_regression_sample_weight_consistency()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 868`** (2 nodes): `Test that _predict_proba_lr of LinearClassifierMixin deals with large     negati`, `test_predict_proba_lr_large_values()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 869`** (2 nodes): `Check the behaviour of the private helpers `_assign_where`.`, `test_assign_where()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 870`** (2 nodes): `Check input validation for `plot`.`, `test_display_plot_input_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 871`** (2 nodes): `Check that decision boundary is correct.`, `test_decision_boundary_display_classifier()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 872`** (2 nodes): `Check that decision boundary is correct for outlier detector.`, `test_decision_boundary_display_outlier_detector()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 873`** (2 nodes): `Check that we can display the decision boundary for a regressor.`, `test_decision_boundary_display_regressor()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 874`** (2 nodes): `Check errors for bad response.`, `test_error_bad_response()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 875`** (2 nodes): `Check that multilabel classifier raises correct error.`, `test_multilabel_classifier_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 876`** (2 nodes): `Check that multi-output multi-class classifier raises correct error.`, `test_multi_output_multi_class_classifier_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 877`** (2 nodes): `Check that multioutput regressor raises correct error.`, `test_multioutput_regressor_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 878`** (2 nodes): `Check that column names are used for pandas.`, `test_dataframe_labels_used()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 879`** (2 nodes): `Check that decision boundary works with classifiers trained on string labels.`, `test_string_target()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 880`** (2 nodes): `Check that passing a dataframe at fit and to the Display does not     raise warn`, `test_dataframe_support()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 881`** (2 nodes): `Check the behaviour of passing `class_of_interest` for plotting the output of`, `test_class_of_interest_binary()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 882`** (2 nodes): `Check that we raise an error when `X` does not have exactly 2 features.`, `test_input_data_dimension()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 883`** (2 nodes): `Check the behaviour of passing `class_of_interest` for plotting the output of`, `test_class_of_interest_multiclass()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 884`** (2 nodes): `Check error raised for multi-output multi-class classifiers by     `_check_bound`, `test_check_boundary_response_method_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 885`** (2 nodes): `Check correct cmap used for all `target_colors` inputs.`, `test_target_colors_cmap()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 886`** (2 nodes): `Check that an error is raised if a qualitative colormap doesn't have enough colo`, `test_multiclass_not_enough_colors_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 887`** (2 nodes): `Test that `levels` are set such that all classes and class boundaries are displa`, `test_multiclass_levels()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 888`** (2 nodes): `Check that decision boundaries are plotted in the background.`, `test_zorder()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 889`** (2 nodes): `Check that the visual block `name_details` matches the `feature_names_in_`     N`, `test_sk_visual_block_remainder_col_names_pandas()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 890`** (2 nodes): `Check that visual_block doesn't return remainder when it has no columns     Non-`, `test_sk_visual_block_full_transform()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 891`** (2 nodes): `Check that remainder still uses available string column names in visual block`, `test_sk_visual_block_int_remainder_cols_pandas()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 892`** (2 nodes): `Check that pandas output works when there is an empty selection.      Non-regres`, `test_empty_selection_pandas_output()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 893`** (2 nodes): `Check column transformer raises error if indices are not aligned.      Non-regre`, `test_raise_error_if_index_not_aligned()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 894`** (2 nodes): `Check that the output is set for the remainder.      Non-regression test for #26`, `test_remainder_set_output()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 895`** (2 nodes): `Check behavior when a transformer's output contains pandas.NA      It should rai`, `test_transform_pd_na()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 896`** (2 nodes): `Check that ColumnTransformer works in parallel with joblib's auto-memmapping.`, `test_column_transformer_auto_memmap()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 897`** (2 nodes): `Check index handling when both pd.Series and pd.DataFrame slices are used in`, `test_column_transformer_non_default_index()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 898`** (2 nodes): `Test that metadata is routed correctly for column transformer.`, `test_metadata_routing_for_column_transformer()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 899`** (2 nodes): `Test metadata routing when the sub-estimator doesn't implement     ``fit_transfo`, `test_metadata_routing_no_fit_transform()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 900`** (2 nodes): `Check that passing parameter not used by the coordinate descent solver     will`, `test_path_unknown_parameter()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 901`** (2 nodes): `Test that a warning is issued if model does not converge`, `test_enet_coordinate_descent_raises_convergence()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 902`** (2 nodes): `Test that the impact of sample_weight is consistent.      Note that this test is`, `test_enet_sample_weight_consistency()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 903`** (2 nodes): `Test that ElasticNetCV with sample weights gives correct results.      We fit th`, `test_enet_cv_sample_weight_correctness()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 904`** (2 nodes): `Test that ElasticNetCV gives same result as GridSearchCV.`, `test_enet_cv_grid_search()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 905`** (2 nodes): `Test that the impact of sample_weight is consistent.`, `test_enet_cv_sample_weight_consistency()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 906`** (2 nodes): `Check that ElasticNet does not overwrite sample_weights.`, `test_enet_sample_weight_does_not_overwrite_sample_weight()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 907`** (2 nodes): `Test that ElasticNet(alpha=0) converges to the same solution as OLS.`, `test_enet_ols_consistency()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 908`** (2 nodes): `Test that early_stopping works correctly.`, `test_cython_solver_early_stopping()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 909`** (2 nodes): `Check that the models inheriting from class:`LinearModelCV` raise an     error w`, `test_cv_estimators_reject_params_with_no_routing_enabled()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 910`** (2 nodes): `Test enet_path works with check_input=False and various precompute settings.`, `test_enet_path_check_input_false()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 911`** (2 nodes): `Check deprecation of n_alphas in favor of alphas.`, `test_path_function_deprecated_n_alphas()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 912`** (2 nodes): `Check that Lasso.dual_gap_ matches its objective formulation, with the     dataf`, `test_lasso_dual_gap()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 913`** (2 nodes): `Check the `alphas` validation in LassoCV.`, `test_lassocv_alphas_validation()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 914`** (2 nodes): `Check that _set_order returns arrays with promised order.`, `test_set_order_dense()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 915`** (2 nodes): `Test that MultiTaskLasso gives same results as the one from skglm.      To repro`, `test_multi_task_lasso_vs_skglm()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 916`** (2 nodes): `Check that _set_order returns sparse matrices in promised format.`, `test_set_order_sparse()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 917`** (2 nodes): `Test that all 3 Cython solvers for 1-d targets give same results.`, `test_cython_solver_equivalence()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 918`** (2 nodes): `_check_identity_scalers_attributes()`, `test_scaler_return_identity()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 919`** (2 nodes): `Check the behaviour of `QuantileTransformer` when `subsample=None`.`, `test_quantile_transform_subsampling_disabled()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 920`** (2 nodes): `Check kernel centering for non-linear kernel.`, `test_kernelcenterer_non_linear_kernel()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 921`** (2 nodes): `Check that box-cox raises informative when a column contains all nans.      Non-`, `test_power_transformer_box_cox_raise_all_nans_col()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 922`** (2 nodes): `Check that `inverse_transform` from `StandardScaler` raises an error     with 1D`, `test_standard_scaler_raise_error_for_1d_input()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 923`** (2 nodes): `Check that significantly non-Gaussian data before transforms correctly.      For`, `test_power_transformer_significantly_non_gaussian()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 924`** (2 nodes): `Check one-to-one transformers give correct feature names.`, `test_one_to_one_features()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 925`** (2 nodes): `Check one-to-one transformers give correct feature names.`, `test_one_to_one_features_pandas()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 926`** (2 nodes): `Test that kernel centerer `feature_names_out`.`, `test_kernel_centerer_feature_names_out()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 927`** (2 nodes): `Check that PowerTransformer leaves constant features unchanged.`, `test_power_transformer_constant_feature()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 928`** (2 nodes): `Check if a warning is triggered when the inverse transformations of the     Box-`, `test_yeo_johnson_inverse_transform_warning()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 929`** (2 nodes): `Verify that PowerTransformer operates without raising any warnings on valid data`, `test_power_transformer_no_warnings()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 930`** (2 nodes): `Check that the results are consistent across different SciPy versions.`, `test_yeojohnson_for_different_scipy_version()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 931`** (2 nodes): `Check that inverse_transform does not raise a warning about feature     names wh`, `test_transformer_inverse_transform_feature_names_warning()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 932`** (2 nodes): `Check that an informative error is raised when the input shape is incorrect.`, `test_transformer_inverse_transform_shape_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 933`** (2 nodes): `Check that the reconstruction attributes are correctly passed.`, `test_standard_scaler_callback_support()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 934`** (2 nodes): `Check feature names for dict learning estimators.`, `test_get_feature_names_out()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 935`** (2 nodes): `Tests that HDBSCAN works when passed a callable metric.`, `test_hdbscan_callable_metric()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 936`** (2 nodes): `Tests that HDBSCAN works correctly when passing sparse feature data.     Evaluat`, `test_hdbscan_sparse()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 937`** (2 nodes): `Tests that HDBSCAN centers are calculated and stored properly, and are     accur`, `test_hdbscan_centers()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 938`** (2 nodes): `Tests that HDBSCAN single-cluster selection with epsilon works correctly.`, `test_hdbscan_allow_single_cluster_with_epsilon()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 939`** (2 nodes): `Validate that HDBSCAN can properly cluster this difficult synthetic     dataset.`, `test_hdbscan_better_than_dbscan()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 940`** (2 nodes): `Tests that HDBSCAN works correctly for array-likes and precomputed inputs     wi`, `test_hdbscan_usable_inputs()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 941`** (2 nodes): `Tests that HDBSCAN raises the correct error when there are too few     non-zero`, `test_hdbscan_sparse_distances_too_few_nonzero()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 942`** (2 nodes): `Tests that HDBSCAN raises the correct error when the distance matrix     has mul`, `test_hdbscan_sparse_distances_disconnected_graph()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 943`** (2 nodes): `Tests that HDBSCAN correctly raises an error for invalid metric choices.`, `test_hdbscan_tree_invalid_metric()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 944`** (2 nodes): `Tests that HDBSCAN correctly raises an error when setting `min_samples`     larg`, `test_hdbscan_too_many_min_samples()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 945`** (2 nodes): `Tests that HDBSCAN correctly raises an error when providing precomputed     dist`, `test_hdbscan_precomputed_dense_nan()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 946`** (2 nodes): `Tests that the `_do_labelling` helper function correctly assigns labels.`, `test_labelling_distinct()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 947`** (2 nodes): `Tests if np.inf and np.nan data are each treated as special outliers.`, `test_outlier_data()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 948`** (2 nodes): `Tests that the `_do_labelling` helper function correctly thresholds the     inco`, `test_labelling_thresholding()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 949`** (2 nodes): `Check that we raise an error if the centers are requested together with     a pr`, `test_hdbscan_error_precomputed_and_store_centers()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 950`** (2 nodes): `Test that HDBSCAN works with the "cosine" metric when the algorithm is set     t`, `test_hdbscan_cosine_metric_valid_algorithm()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 951`** (2 nodes): `Test that HDBSCAN raises an informative error is raised when an unsupported`, `test_hdbscan_cosine_metric_invalid_algorithm()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 952`** (2 nodes): `Check the tie breaking behavior of the most frequent strategy.      Non-regressi`, `test_most_frequent_tie_object()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 953`** (2 nodes): `Check the behaviour of the iterative imputer with different initial strategy`, `test_iterative_imputer_keep_empty_features()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 954`** (2 nodes): `Check that we propagate properly the parameter `fill_value`.`, `test_iterative_imputer_constant_fill_value()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 955`** (2 nodes): `Check that we properly apply the empty feature mask to `min_value` and     `max_`, `test_iterative_imputer_min_max_value_remove_empty()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 956`** (2 nodes): `Check the behaviour of `keep_empty_features` for `KNNImputer`.`, `test_knn_imputer_keep_empty_features()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 957`** (2 nodes): `Check that missing indicator return the feature names with a prefix.`, `test_missing_indicator_feature_names_out()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 958`** (2 nodes): `Check transform uses object dtype when fitted on an object dtype.      Non-regre`, `test_imputer_lists_fit_transform()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 959`** (2 nodes): `Check transform preserves numeric dtype independent of fit dtype.`, `test_imputer_transform_preserves_numeric_dtype()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 960`** (2 nodes): `Check the behaviour of `keep_empty_features` with all strategies but     'consta`, `test_simple_imputer_keep_empty_features()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 961`** (2 nodes): `Check that we raise a proper error message when we cannot cast the fill value`, `test_simple_imputer_constant_fill_value_casting()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 962`** (2 nodes): `Check the behaviour of `keep_empty_features` with no empty features.      With n`, `test_iterative_imputer_no_empty_features()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 963`** (2 nodes): `Check the behaviour of `keep_empty_features` in the presence of empty features.`, `test_iterative_imputer_with_empty_features()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 965`** (2 nodes): `Check that init works with numpy scalar strings.      Non-regression test for #2`, `test_kmeans_with_array_like_or_np_scalar_init()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 966`** (2 nodes): `Check `feature_names_out` for `KMeans` and `MiniBatchKMeans`.`, `test_feature_names_out()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 967`** (2 nodes): `Check that predict does not change cluster centers.      Non-regression test for`, `test_predict_does_not_change_cluster_centers()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 968`** (2 nodes): `Check that sample weight is used during init.      `_init_centroids` is shared a`, `test_sample_weight_init()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 969`** (2 nodes): `Check that if sample weight is 0, this sample won't be chosen.      `_init_centr`, `test_sample_weight_zero()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 970`** (2 nodes): `Check that kmeans stops when there are more centers than non-duplicate samples`, `test_relocating_with_duplicates()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 971`** (2 nodes): `Check that `n_init="auto"` chooses the right number of initializations.     Non-`, `test_kmeans_init_auto_with_initial_centroids()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 972`** (2 nodes): `_sort_centers()`, `test_weighted_vs_repeated()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 975`** (2 nodes): `Check partial fit does not fail after fit when early_stopping=True.      Non-reg`, `test_mlp_partial_fit_after_fit()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 976`** (2 nodes): `Test that a diverging model does not raise errors when early stopping is enabled`, `test_mlp_diverging_loss()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 977`** (2 nodes): `Test MLP with Poisson loss and no hidden layer equals GLM.`, `test_mlp_vs_poisson_glm_equivalent()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 978`** (2 nodes): `Check error message when the validation set is too small.`, `test_minimum_input_sample_size()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 979`** (2 nodes): `Check that labels can be strings when `early_stopping=True`.      Non-regression`, `test_mlp_early_stopping_string_labels()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 980`** (2 nodes): `Loading from MLP and partial fitting updates weights. Non-regression     test fo`, `test_mlp_loading_from_joblib_partial_fit()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 981`** (2 nodes): `Check that feature names are preserved when early stopping is enabled.      Feat`, `test_preserve_feature_names()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 982`** (2 nodes): `Check that early stopping works with warm start.`, `test_mlp_warm_start_with_early_stopping()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 983`** (2 nodes): `Check that we stop the number of iteration at `max_iter` when warm starting.`, `test_mlp_warm_start_no_convergence()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 984`** (2 nodes): `Test error is raised for mixed string and numerical input and dispatch enabled.`, `test_unique_labels_mixed_str_numerical_array_api()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 985`** (2 nodes): `Check `unique_labels` compliance for array API.`, `test_unique_labels_array_api()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 986`** (2 nodes): `Check that we raise a warning when the number of unique classes is greater than`, `test_check_classification_targets_too_many_unique_classes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 987`** (2 nodes): `Check that type_of_target works with pandas nullable dtypes.`, `test_type_of_target_pandas_nullable()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 988`** (2 nodes): `Checks that unique_labels work with pandas nullable dtypes.      Non-regression`, `test_unique_labels_pandas_nullable()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 989`** (2 nodes): `Test whether points lying on boundary are handled consistently      Also ensures`, `test_radius_neighbors_boundary_handling()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 990`** (2 nodes): `Weight function to replace lambda d: d ** -2.     The lambda function is not val`, `_weight_func()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 991`** (2 nodes): `Additional parameter validation for *Neighbors* estimators not covered by common`, `test_neighbors_validate_parameters()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 992`** (2 nodes): `Validation of all classes extending NeighborsBase with     Minkowski semi-metric`, `test_neighbors_minkowski_semimetric_algo_warn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 993`** (2 nodes): `Check that we raise a proper error if `algorithm!='brute'` and `p<1`.`, `test_neighbors_minkowski_semimetric_algo_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 994`** (2 nodes): `Validate parameter of NearestNeighbors.`, `test_nearest_neighbors_validate_params()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 995`** (2 nodes): `Ensures that `predict` works for array-likes when `weights` is a callable.`, `test_regressor_predict_on_arraylikes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 996`** (2 nodes): `Check that the different neighbor estimators are lenient towards `nan`     value`, `test_nan_euclidean_support()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 997`** (2 nodes): `Check that KNN predict works with dataframes      non-regression test for issue`, `test_predict_dataframe()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 998`** (2 nodes): `Check that NearestNeighbors works with :math:`p \\in (0,1)` when `algorithm``, `test_nearest_neighbours_works_with_p_less_than_1()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 999`** (2 nodes): `Check that `predict` and `predict_proba` raises on sample of all zeros weights.`, `test_KNeighborsClassifier_raise_on_all_zero_weights()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1000`** (2 nodes): `Check that `predict` and related functions work fine with X=None      Calling pr`, `test_neighbor_classifiers_loocv()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1001`** (2 nodes): `Check that `predict` and related functions work fine with X=None`, `test_neighbor_regressors_loocv()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1002`** (2 nodes): `Ensure KNeighborsClassifier(algorithm='brute') works with string labels.      No`, `test_neighbors_classifier_with_string_labels()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1003`** (2 nodes): `Check that a warning is raised when multiple versions exist and no version is`, `test_fetch_openml_iris_warn_multiple_version()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1004`** (2 nodes): `Check that we can get a dataset without target.`, `test_fetch_openml_no_target()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1005`** (2 nodes): `check that missing values in categories are compatible with pandas     categoric`, `test_missing_values_pandas()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1006`** (2 nodes): `Check that we raise a warning when the dataset is inactive.`, `test_fetch_openml_inactive()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1007`** (2 nodes): `Check that we can overwrite the default parameters of `read_csv`.`, `test_fetch_openml_overwrite_default_params_read_csv()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1008`** (2 nodes): `Check that we can load the "zoo" dataset.     Non-regression test for:     https`, `test_fetch_openml_with_ignored_feature()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1009`** (2 nodes): `Check that we strip the single quotes when used as a string delimiter.      Non-`, `test_fetch_openml_strip_quotes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1010`** (2 nodes): `Check that we can strip leading whitespace in pandas parser.      Non-regression`, `test_fetch_openml_leading_whitespace()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1011`** (2 nodes): `Check that we can handle escapechar and single/double quotechar.      Non-regres`, `test_fetch_openml_quotechar_escapechar()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1012`** (2 nodes): `Check the behaviour of `fetch_openml` with `as_frame=True`.      Fetch by ID and`, `test_fetch_openml_as_frame_true()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1013`** (2 nodes): `Check the behaviour of `fetch_openml` with `as_frame=False`.      Fetch both by`, `test_fetch_openml_as_frame_false()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1014`** (2 nodes): `Check the consistency of the LIAC-ARFF and pandas parsers.`, `test_fetch_openml_consistency_parser()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1015`** (2 nodes): `Check the equivalence of the dataset when using `as_frame=False` and     `as_fra`, `test_fetch_openml_equivalence_array_dataframe()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1016`** (2 nodes): `Check fetching on a numerical only dataset with string labels.`, `test_fetch_openml_iris_pandas()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1017`** (2 nodes): `Check that we can force the target to not be the default target.`, `test_fetch_openml_forcing_targets()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1018`** (2 nodes): `Check the behaviour of `return_X_y=True` when `as_frame=True`.`, `test_fetch_openml_equivalence_frame_return_X_y()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1019`** (2 nodes): `Check the behaviour of `return_X_y=True` when `as_frame=False`.`, `test_fetch_openml_equivalence_array_return_X_y()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1020`** (2 nodes): `Check the difference between liac-arff and pandas parser.`, `test_fetch_openml_difference_parsers()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1021`** (2 nodes): `Check that `fetch_openml` infer the right number of categories, integers, and`, `test_fetch_openml_types_inference()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1022`** (2 nodes): `check_pairwise_distances_chunked()`, `test_pairwise_distances_chunked()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1023`** (2 nodes): `Check that `nan_euclidean` is lenient with `nan` values.`, `test_nan_euclidean_support()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1024`** (2 nodes): `Check that the behavior of constant input is the same in the case of     full of`, `test_nan_euclidean_constant_input_argmin()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1025`** (2 nodes): `Check pairwise_distances with lists of strings as input.`, `test_pairwise_dist_custom_metric_for_string()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1026`** (2 nodes): `Check that pairwise_distances does not convert boolean input to float     when u`, `test_pairwise_dist_custom_metric_for_bool()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1027`** (2 nodes): `Check that Y_norm_squared is correctly sliced alongside Y.      Non-regression t`, `test_parallel_pairwise_distances_y_norm_squared()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1028`** (2 nodes): `test_check_tuple_input()`, `tuplify()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1029`** (2 nodes): `Check that "auto" and "arpack" solvers are equivalent for sparse inputs.`, `test_sparse_pca_auto_arpack_singular_values_consistency()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1030`** (2 nodes): `Check that exposing and setting `n_oversamples` will provide accurate results`, `test_pca_randomized_svd_n_oversamples()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1031`** (2 nodes): `Check feature names out for PCA.`, `test_feature_names_out()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1032`** (2 nodes): `Check the accuracy of PCA's internal variance calculation`, `test_variance_correctness()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1034`** (2 nodes): `ols_ridge_dataset()`, `Dataset with OLS and Ridge solutions, well conditioned X.      The construction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1035`** (2 nodes): `Check that passing an array for alpha works with array API dispatch.      Non-re`, `test_ridge_per_target_alpha_array_api()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1036`** (2 nodes): `Test that Ridge converges for all solvers to correct solution.      We work with`, `test_ridge_regression()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1037`** (2 nodes): `Check class_weights resemble sample_weights behavior.`, `test_class_weight_vs_sample_weight()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1038`** (2 nodes): `Check alpha=0.0 raises error only when `cv=None`.`, `test_ridgecv_alphas_zero()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1039`** (2 nodes): `Check the `alphas` validation in RidgeCV and RidgeClassifierCV.`, `test_ridgecv_alphas_validation()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1040`** (2 nodes): `Check the case when `alphas` is a scalar.     This case was supported in the pas`, `test_ridgecv_alphas_scalar()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1041`** (2 nodes): `check if all combinations of arguments give valid estimations`, `test_ridge_regression_check_arguments_validity()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1042`** (2 nodes): `Test that Ridge converges for all solvers to correct solution on hstacked data.`, `test_ridge_regression_hstacked_X()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1043`** (2 nodes): `Check that multilabel classification is supported and give meaningful     result`, `test_ridgeclassifier_multilabel()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1044`** (2 nodes): `Test that positive Ridge finds true positive coefficients.`, `test_ridge_positive_regression_test()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1045`** (2 nodes): `Test that Ridge w/wo positive converges to the same solution.      Ridge with po`, `test_ridge_ground_truth_positive_test()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1046`** (2 nodes): `Test input validation for positive argument in Ridge.`, `test_ridge_positive_error_test()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1047`** (2 nodes): `Check ridge loss consistency when positive argument is enabled.`, `test_positive_ridge_loss()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1048`** (2 nodes): `Test that LBGFS gets almost the same coef of svd when positive=False.`, `test_lbfgs_solver_consistency()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1049`** (2 nodes): `Test that LBFGS solver raises ConvergenceWarning.`, `test_lbfgs_solver_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1050`** (2 nodes): `Test that the impact of sample_weight is consistent.      Note that this test is`, `test_ridge_sample_weight_consistency()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1051`** (2 nodes): `Check that the predictions stored in `cv_results_` are on the original scale.`, `test_ridge_cv_results_predictions()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1052`** (2 nodes): `Test that Ridge converges for all solvers to correct solution on vstacked data.`, `test_ridge_regression_vstacked_X()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1053`** (2 nodes): `Check that `RidgeCV` works properly with multioutput and sample_weight     when`, `test_ridge_cv_multioutput_sample_weight()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1054`** (2 nodes): `Check that `RidgeCV` works properly with a custom multioutput scorer.`, `test_ridge_cv_custom_multioutput_scorer()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1055`** (2 nodes): `Test that `RidgeCV` or `RidgeClassifierCV` with default `scoring`     argument (`, `test_metadata_routing_with_default_scoring()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1056`** (2 nodes): `Test that `set_score_request` is set within `RidgeCV.fit()` and     `RidgeClassi`, `test_set_score_request_with_default_scoring()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1057`** (2 nodes): `Test that unpenalized Ridge = OLS converges for all solvers to correct solution.`, `test_ridge_regression_unpenalized()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1058`** (2 nodes): `Test that unpenalized Ridge = OLS converges for all solvers to correct solution.`, `test_ridge_regression_unpenalized_hstacked_X()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1059`** (2 nodes): `Test that unpenalized Ridge = OLS converges for all solvers to correct solution.`, `test_ridge_regression_unpenalized_vstacked_X()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1060`** (2 nodes): `Test that Ridge with sample weights gives correct results.      We use the follo`, `test_ridge_regression_sample_weights()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1061`** (2 nodes): `non-regression test for gh #25249`, `test_sgd_verbose()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1062`** (2 nodes): `Test that SGD raises with forbidden loss for passive-aggressive algo.`, `test_learning_rate_PA_raises()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1063`** (2 nodes): `Check that l1_ratio is not used when penalty is not 'elasticnet`, `test_sgd_l1_ratio_not_used()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1064`** (2 nodes): `Check that a warning is raised when `power_t` is negative.`, `test_power_t_limits()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1065`** (2 nodes): `Check that the shape of `coef_init` is validated.`, `test_provide_coef()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1066`** (2 nodes): `Check that `intercept_init` or `offset_init` is validated.`, `test_set_intercept_offset()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1067`** (2 nodes): `Check that we raise an error for `early_stopping` used with     `partial_fit`.`, `test_sgd_early_stopping_with_partial_fit()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1068`** (2 nodes): `Check that we can pass a scaler with binary classification to     `intercept_ini`, `test_set_intercept_offset_binary()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1069`** (2 nodes): `_check_time_series_max_train_size()`, `test_time_series_max_train_size()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1070`** (2 nodes): `Check for integer overflow on 32-bit platforms.      Non-regression test for:`, `test_train_test_split_32bit_overflow()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1071`** (2 nodes): `Check get_metadata_routing returns the correct MetadataRouter.`, `test_splitter_get_metadata_routing()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1072`** (2 nodes): `Check set_split_request is defined for group splitters and not for others.`, `test_splitter_set_split_request()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1073`** (2 nodes): `Test if predict breaks ties in OVR mode.     Related issue: https://github.com/s`, `test_svc_ovr_tie_breaking()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1074`** (2 nodes): `Test using a custom kernel that is not fed with array-like for floats`, `test_custom_kernel_not_array_input()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1075`** (2 nodes): `Check that SVC raises error when internal representation is altered.      Non-re`, `test_svc_raises_error_internal_representation()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1076`** (2 nodes): `Check that we can pass `C=inf` that is equivalent to a very large C value.`, `test_svm_with_infinite_C()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1077`** (2 nodes): `Test that accessing probA_ and probB_ raises FutureWarning for SVC and NuSVC.`, `test_svc_nusvc_probA_probB_deprecated()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1079`** (2 nodes): `Make sure that TSNE works for different distance metrics`, `test_tsne_with_different_distance_metrics()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1080`** (2 nodes): `Make sure that the n_jobs parameter doesn't impact the output`, `test_tsne_n_jobs()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1081`** (2 nodes): `Make sure that method_parameters works with mahalanobis distance.`, `test_tsne_with_mahalanobis_distance()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1082`** (2 nodes): `Make sure that perplexity > n_samples results in a ValueError`, `test_tsne_perplexity_validation()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1083`** (2 nodes): `Make sure that TSNE works when the output is set to "pandas".      Non-regressio`, `test_tsne_works_with_pandas_output()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1084`** (2 nodes): `Raise an error when n_neighbors >= n_samples / 2.      Non-regression test for #`, `test_trustworthiness_n_neighbors_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1085`** (2 nodes): `t-SNE should give a lower KL divergence with more iterations.`, `test_optimization_minimizes_kl_divergence()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1086`** (2 nodes): `Make sure that TSNE works identically for sparse and dense matrix`, `test_sparse_precomputed_distance()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1088`** (1 nodes): `Decision tree based models for classification and regression.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1089`** (1 nodes): `======================================================== Post pruning decision t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1090`** (1 nodes): `======================================================================= Plot the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1091`** (1 nodes): `======================== Decision Tree Regression ======================== In th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1092`** (1 nodes): `========================================= Understanding the decision tree struct`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1093`** (2 nodes): `_apply_on_subsets()`, `check_methods_subset_invariance()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1094`** (2 nodes): `check_regressor_multioutput()`, `_is_pairwise_metric()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1095`** (1 nodes): `Checks the bundled license is installed with the wheel.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BaseEstimator` connect `Community 1` to `Community 338`, `Community 148`, `Community 0`, `Community 146`, `Community 37`, `Community 314`, `Community 2`, `Community 48`, `Community 432`, `Community 4`, `Community 26`, `Community 215`, `Community 47`, `Community 360`, `Community 361`, `Community 263`, `Community 153`, `Community 362`, `Community 131`, `Community 246`, `Community 71`, `Community 6`, `Community 27`, `Community 9`, `Community 3`, `Community 154`, `Community 225`, `Community 97`, `Community 247`, `Community 30`, `Community 160`, `Community 11`, `Community 10`, `Community 16`, `Community 140`, `Community 65`, `Community 437`, `Community 248`, `Community 236`, `Community 49`, `Community 464`, `Community 466`, `Community 385`, `Community 467`, `Community 465`, `Community 298`, `Community 33`, `Community 187`, `Community 169`, `Community 227`, `Community 12`, `Community 483`, `Community 98`, `Community 484`, `Community 554`, `Community 412`, `Community 434`, `Community 81`, `Community 170`, `Community 556`, `Community 127`, `Community 416`, `Community 485`, `Community 289`, `Community 323`, `Community 106`, `Community 250`, `Community 141`, `Community 7`, `Community 13`, `Community 5`, `Community 61`, `Community 439`, `Community 230`, `Community 31`, `Community 559`, `Community 249`, `Community 102`, `Community 83`, `Community 15`, `Community 44`, `Community 25`, `Community 217`, `Community 843`, `Community 844`, `Community 845`, `Community 846`, `Community 847`, `Community 848`, `Community 849`, `Community 850`, `Community 851`, `Community 389`, `Community 852`, `Community 853`, `Community 854`, `Community 855`, `Community 856`, `Community 857`, `Community 858`, `Community 859`, `Community 561`, `Community 369`, `Community 370`, `Community 866`, `Community 45`, `Community 867`, `Community 868`, `Community 622`, `Community 186`, `Community 686`, `Community 687`, `Community 688`, `Community 348`, `Community 324`, `Community 870`, `Community 871`, `Community 872`, `Community 873`, `Community 874`, `Community 875`, `Community 876`, `Community 877`, `Community 878`, `Community 879`, `Community 880`, `Community 881`, `Community 882`, `Community 883`, `Community 884`, `Community 885`, `Community 886`, `Community 887`, `Community 888`, `Community 487`, `Community 488`, `Community 489`, `Community 103`, `Community 193`, `Community 889`, `Community 890`, `Community 891`, `Community 150`, `Community 892`, `Community 893`, `Community 894`, `Community 895`, `Community 896`, `Community 897`, `Community 898`, `Community 899`, `Community 490`, `Community 566`, `Community 524`, `Community 19`, `Community 87`, `Community 8`, `Community 59`, `Community 303`, `Community 208`, `Community 42`, `Community 17`, `Community 76`, `Community 79`, `Community 638`, `Community 256`, `Community 424`, `Community 43`, `Community 257`, `Community 447`, `Community 475`, `Community 144`, `Community 183`?**
  _High betweenness centrality (0.130) - this node is a cross-community bridge._
- **Why does `Interval` connect `Community 0` to `Community 358`, `Community 431`, `Community 6`, `Community 294`, `Community 148`, `Community 146`, `Community 37`, `Community 1`, `Community 314`, `Community 147`, `Community 2`, `Community 48`, `Community 125`, `Community 315`, `Community 108`, `Community 3`, `Community 244`, `Community 284`, `Community 285`, `Community 316`, `Community 433`, `Community 509`, `Community 86`, `Community 595`, `Community 596`, `Community 459`, `Community 597`, `Community 139`, `Community 460`, `Community 78`, `Community 406`, `Community 320`, `Community 360`, `Community 334`, `Community 361`, `Community 263`, `Community 153`, `Community 235`, `Community 5`, `Community 280`, `Community 138`, `Community 71`, `Community 27`, `Community 9`, `Community 154`, `Community 225`, `Community 97`, `Community 30`, `Community 160`, `Community 11`, `Community 10`, `Community 16`, `Community 297`, `Community 436`, `Community 65`, `Community 205`, `Community 26`, `Community 93`, `Community 49`, `Community 437`, `Community 248`, `Community 236`, `Community 464`, `Community 466`, `Community 385`, `Community 467`, `Community 465`, `Community 298`, `Community 34`, `Community 94`, `Community 187`, `Community 180`, `Community 468`, `Community 410`, `Community 169`, `Community 227`, `Community 12`, `Community 135`, `Community 15`, `Community 677`, `Community 676`, `Community 25`, `Community 98`, `Community 268`, `Community 484`, `Community 554`, `Community 345`, `Community 4`, `Community 412`, `Community 434`, `Community 81`, `Community 170`, `Community 556`, `Community 127`, `Community 416`, `Community 485`, `Community 289`, `Community 106`, `Community 250`, `Community 185`, `Community 141`, `Community 7`, `Community 13`, `Community 61`, `Community 230`, `Community 31`, `Community 559`, `Community 249`, `Community 102`, `Community 616`, `Community 83`, `Community 257`, `Community 176`, `Community 446`, `Community 91`, `Community 201`, `Community 535`, `Community 203`, `Community 184`, `Community 450`, `Community 402`, `Community 302`, `Community 451`, `Community 333`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._
- **Why does `StrOptions` connect `Community 2` to `Community 6`, `Community 359`, `Community 148`, `Community 0`, `Community 146`, `Community 37`, `Community 147`, `Community 1`, `Community 48`, `Community 125`, `Community 315`, `Community 108`, `Community 3`, `Community 284`, `Community 86`, `Community 459`, `Community 139`, `Community 460`, `Community 78`, `Community 320`, `Community 360`, `Community 361`, `Community 263`, `Community 153`, `Community 5`, `Community 280`, `Community 130`, `Community 168`, `Community 138`, `Community 27`, `Community 9`, `Community 154`, `Community 97`, `Community 30`, `Community 160`, `Community 11`, `Community 10`, `Community 16`, `Community 140`, `Community 297`, `Community 436`, `Community 26`, `Community 93`, `Community 49`, `Community 65`, `Community 437`, `Community 248`, `Community 236`, `Community 466`, `Community 385`, `Community 467`, `Community 465`, `Community 298`, `Community 34`, `Community 94`, `Community 35`, `Community 187`, `Community 180`, `Community 468`, `Community 410`, `Community 260`, `Community 188`, `Community 344`, `Community 552`, `Community 169`, `Community 227`, `Community 12`, `Community 135`, `Community 25`, `Community 98`, `Community 411`, `Community 228`, `Community 268`, `Community 484`, `Community 554`, `Community 345`, `Community 4`, `Community 412`, `Community 434`, `Community 267`, `Community 413`, `Community 81`, `Community 170`, `Community 556`, `Community 127`, `Community 416`, `Community 485`, `Community 289`, `Community 323`, `Community 250`, `Community 185`, `Community 141`, `Community 7`, `Community 13`, `Community 61`, `Community 439`, `Community 33`, `Community 249`, `Community 102`, `Community 616`, `Community 83`, `Community 257`, `Community 176`, `Community 534`, `Community 91`, `Community 201`, `Community 184`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 2319 inferred relationships involving `Interval` (e.g. with `_Progress` and `ProgressBar`) actually correct?**
  _`Interval` has 2319 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2292 inferred relationships involving `BaseEstimator` (e.g. with `============================================== Supporting callbacks in third par` and `SimpleGridSearch`) actually correct?**
  _`BaseEstimator` has 2292 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2097 inferred relationships involving `StrOptions` (e.g. with `Log for one run of a scoring monitor.      The recorded scores are accessed thro` and `Restore state, opening a fresh listener if the inherited one is unusable.`) actually correct?**
  _`StrOptions` has 2097 INFERRED edges - model-reasoned connections that need verification._
- **Are the 1166 inferred relationships involving `TransformerMixin` (e.g. with `Birch` and `_CFNode`) actually correct?**
  _`TransformerMixin` has 1166 INFERRED edges - model-reasoned connections that need verification._