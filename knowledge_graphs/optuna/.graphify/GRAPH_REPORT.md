# Graph Report - .  (2026-07-29)

## Corpus Check
- cluster-only mode - file stats not available

## Summary
- 3912 nodes · 8405 edges · 191 communities detected
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 1253 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: imports_from: 1840 · contains: 1765 · uses: 1253 · method: 1102 · calls: 1063 · imports: 704 · rationale_for: 488 · inherits: 190


## Graph Freshness
- Built from Git commit: `b6f2ea6`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Study` - 228 edges
2. `BaseDistribution` - 213 edges
3. `StudyDirection` - 150 edges
4. `FloatDistribution` - 94 edges
5. `CategoricalDistribution` - 87 edges
6. `IntDistribution` - 84 edges
7. `FrozenStudy` - 68 edges
8. `RDBStorage` - 58 edges
9. `StorageTestCase` - 51 edges
10. `LazyRandomState` - 48 edges

## Surprising Connections (you probably didn't know these)
- `.. _user_defined_pruner:  User-Defined Pruner ===================  In :mod:`optu` --uses--> `TrialState`  [INFERRED]
  tutorial/20_recipes/006_user_defined_pruner.py → optuna/trial/_state.py
- `Test _get_best_trial method with deepcopy parameter control.` --uses--> `StorageSupplier`  [INFERRED]
  tests/study_tests/test_study.py → optuna/testing/storages.py
- `FailArtifactStore` --uses--> `ArtifactNotFound`  [INFERRED]
  tests/artifacts_tests/stubs.py → optuna/artifacts/exceptions.py
- `FailArtifactStore` --uses--> `ArtifactStore`  [INFERRED]
  tests/artifacts_tests/stubs.py → optuna/artifacts/_protocol.py
- `InMemoryArtifactStore` --uses--> `ArtifactNotFound`  [INFERRED]
  tests/artifacts_tests/stubs.py → optuna/artifacts/exceptions.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.03
Nodes (92): BaseImportanceEvaluator, BaseCrossover, Base class for crossovers.      A crossover operation is used by :class:`~optuna, Number of parent individuals required to perform crossover., Perform crossover of selected parent individuals.          This method is called, FanovaImportanceEvaluator, fANOVA importance evaluator.      Implements the fANOVA hyperparameter importanc, BaseImportanceEvaluator (+84 more)

### Community 1 - "Community 1"
Cohesion: 0.04
Nodes (73): # TODO: Make it an index array., _ScaleType, IntEnum, Returns whether visualization with Matplotlib is available or not.      .. note:, _categorical_choice_equal(), CategoricalDistribution, _convert_old_distribution_to_new_distribution(), FloatDistribution (+65 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (37): hashlib, _get_hypervolume_history_plot(), plot_hypervolume_history(), Plot hypervolume history of all trials in a study with Matplotlib.      .. note:, _get_optimization_history_plot(), plot_optimization_history(), Plot optimization history of all trials in a study with Matplotlib.      .. seea, _get_parallel_coordinate_plot() (+29 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (49): .. _distributed:  Easy Parallelization ====================  Optuna supports mul, ABC, alembic.command, alembic.config, alembic.migration, alembic.script, binascii, collections.abc (+41 more)

### Community 4 - "Community 4"
Cohesion: 0.04
Nodes (44): BaseMutation, Uniform Crossover operation used by :class:`~optuna.samplers.NSGAIISampler`., UniformCrossover, Sampler using Gaussian process-based Bayesian optimization.      .. note::, BaseImprovementEvaluator, BestValueStagnationEvaluator, _compute_standardized_regret_bound(), _get_beta() (+36 more)

### Community 5 - "Community 5"
Cohesion: 0.05
Nodes (50): gRPC client for :func:`~optuna.storages.run_grpc_proxy_server`.      Example:, Set up the gRPC channel and stub., Wait until the gRPC server is ready.          Args:             timeout: The max, Close the gRPC channel., JournalOperation, Removes the current session.          A session is stored in SQLAlchemy's Thread, Upgrade the storage schema., Return the schema version currently used by this storage. (+42 more)

### Community 6 - "Community 6"
Cohesion: 0.04
Nodes (46): atexit, gc, grpc, make_server(), Run a gRPC server for the given storage URL, host, and port.      Example:, run_grpc_proxy_server(), json, optuna.integration (+38 more)

### Community 8 - "Community 8"
Cohesion: 0.04
Nodes (36): copy_study(), create_study(), delete_study(), get_all_study_names(), get_all_study_summaries(), load_study(), Add trials to study.          The trials are validated before being added., Set metric names.          This method names each dimension of the returned valu (+28 more)

### Community 9 - "Community 9"
Cohesion: 0.05
Nodes (33): alembic, Enum, ValueType, sqlalchemy, sqlalchemy.exc, sqlalchemy.ext.declarative, sqlalchemy.orm, empty message  Revision ID: v0.9.0.a Revises: Create Date: 2019-03-12 12:30:31.1 (+25 more)

### Community 10 - "Community 10"
Cohesion: 0.10
Nodes (24): BaseModel, StudyDirectionModel, StudyModel, StudySystemAttributeModel, StudyUserAttributeModel, TrialHeartbeatModel, TrialIntermediateValueModel, TrialIntermediateValueType (+16 more)

### Community 11 - "Community 11"
Cohesion: 0.07
Nodes (4): _create_scoped_session(), escape_alembic_config_value(), RDBStorage, _VersionManager

### Community 12 - "Community 12"
Cohesion: 0.06
Nodes (34): build_state_fn(), frozen_trial_factory(), Prepare sample from uniform distribution for cheking other distributions., Test samples from discrete have expected intervals., Test samples are drawn from the specified category., Test sampling from int distribution returns integer., Tests FAIL, RUNNING, and WAITING states are equally., Tests PRUNED state is treated differently from both FAIL and COMPLETE. (+26 more)

### Community 13 - "Community 13"
Cohesion: 0.06
Nodes (38): colorlog, _batched_lbfgsb(), Batched L-BFGS-B optimization with/without greenlet.     - `func_and_grad` is ex, greenlet, _get_intermediate_plot(), plot_intermediate_values(), Plot intermediate values of all trials in a study with Matplotlib.      .. seeal, optuna.visualization.intermediate.values (+30 more)

### Community 14 - "Community 14"
Cohesion: 0.08
Nodes (42): inspect, _add_commands(), _add_common_arguments(), _Ask, _BaseCommand, _BestTrial, _BestTrials, CellValue (+34 more)

### Community 15 - "Community 15"
Cohesion: 0.06
Nodes (27): *         Create a new study., *         Delete a study., *         Set a study's user attribute., *         Set a study's system attribute., *         Get a study id by its name., *         Get a study name by its id., *         Get study directions., *         Get study user attributes. (+19 more)

### Community 16 - "Community 16"
Cohesion: 0.06
Nodes (11): _generate_trial(), is_equal_floats(), _setup_studies(), StorageTestCase, _test_set_and_get_study_system_attrs_for_floats(), _test_set_and_get_study_user_attrs_for_floats(), _test_set_and_get_trial_param_for_floats(), _test_set_and_get_trial_system_attr_for_floats() (+3 more)

### Community 17 - "Community 17"
Cohesion: 0.11
Nodes (3): JournalStorage, JournalStorageReplayResult, Storage class for Journal storage backend.      Note that library users can inst

### Community 18 - "Community 18"
Cohesion: 0.07
Nodes (19): decimal, _check_evaluate_args(), _get_distributions(), itertools, numbers, check_distribution_compatibility(), distribution_to_json(), Serialize a distribution to JSON format.      Args:         dist: A distribution (+11 more)

### Community 19 - "Community 19"
Cohesion: 0.05
Nodes (4): optuna.samplers.nsgaii.crossover, optuna.samplers.nsgaii.mutation, optuna.testing.trials, test_crowding_distance_sort()

### Community 20 - "Community 20"
Cohesion: 0.06
Nodes (17): subprocess, _get_output(), test_ask(), test_ask_empty_search_space(), test_ask_empty_search_space_flatten(), test_ask_flatten(), test_best_trial_command(), test_best_trial_command_flatten() (+9 more)

### Community 21 - "Community 21"
Cohesion: 0.06
Nodes (24): _get_pareto_front_2d(), _get_pareto_front_3d(), _get_pareto_front_plot(), plot_pareto_front(), Plot the Pareto front of a study.      .. seealso::         Please refer to :fun, optuna.visualization.matplotlib.contour, optuna.visualization.matplotlib.edf, optuna.visualization.matplotlib.hypervolume.history (+16 more)

### Community 22 - "Community 22"
Cohesion: 0.06
Nodes (18): plotly.io, sklearn.exceptions, plot_contour ============  .. autofunction:: optuna.visualization.plot_contour, ackley(), objective(), plot_edf ========  .. autofunction:: optuna.visualization.plot_edf  The followin, plot_hypervolume_history ========================  .. autofunction:: optuna.visu, df() (+10 more)

### Community 23 - "Community 23"
Cohesion: 0.12
Nodes (15): BasicSamplerTestCase, MultiObjectiveSamplerTestCase, RelativeSamplerTestCase, TestBasicSampler, TestMultiObjectiveSampler, TestRelativeSampler, TestSingleOnlySampler, SingleOnlySamplerTestCase (+7 more)

### Community 24 - "Community 24"
Cohesion: 0.06
Nodes (3): optuna.testing.pruners, optuna.testing.samplers, optuna.trial.trial

### Community 25 - "Community 25"
Cohesion: 0.07
Nodes (15): _get_improvement_plot(), plot_terminator_improvement(), Plot the potentials for future objective improvement.      This function visuali, optuna.study.study, optuna.study.study.summary, optuna.terminator.callback, optuna.terminator.erroreval, optuna.terminator.improvement.emmr (+7 more)

### Community 26 - "Community 26"
Cohesion: 0.08
Nodes (3): BaseHeartbeat, _CachedStorage, _StudyInfo

### Community 27 - "Community 27"
Cohesion: 0.08
Nodes (4): create_insecure_channel(), GrpcClientCache, GrpcClientCacheEntry, GrpcStorageProxy

### Community 28 - "Community 28"
Cohesion: 0.10
Nodes (10): BaseSampler, BruteForceSampler, _enumerate_candidates(), _get_non_waiting_trials_and_current_trial_index(), _is_nan(), Sampler that performs exhaustive search over the define-by-run search space., _TreeNode, _UnexpandedTreeNode (+2 more)

### Community 29 - "Community 29"
Cohesion: 0.11
Nodes (22): optuna.testing.pytest.storages, TestStorage, _check_trials(), f(), get_storage(), objective(), run_optimize(), test_get_best_trial() (+14 more)

### Community 30 - "Community 30"
Cohesion: 0.09
Nodes (14): .. _pruning:  Efficient Optimization Algorithms ================================, .. _attributes:  User Attributes ===============  This feature is to annotate ex, .. _user_defined_pruner:  User-Defined Pruner ===================  In :mod:`optu, .. _specify_params:  Specify Hyperparameters Manually ==========================, .. _ask_and_tell:  Ask-and-Tell Interface =======================  Optuna has an, .. _reuse_best_trial:  Re-use the best trial ======================  In some cas, lightgbm, optuna.visualization (+6 more)

### Community 31 - "Community 31"
Cohesion: 0.14
Nodes (14): BasicImportanceEvaluatorTestCase, ConditionalImportanceEvaluatorTestCase, TestBasicImportanceEvaluator, TestConditionalImportanceEvaluator, TestMultiObjectiveImportanceEvaluator, TestNonConditionalImportanceEvaluator, MultiObjectiveImportanceEvaluatorTestCase, NonConditionalImportanceEvaluatorTestCase (+6 more)

### Community 33 - "Community 33"
Cohesion: 0.08
Nodes (3): cmaes, _create_trials(), test_get_trials()

### Community 34 - "Community 34"
Cohesion: 0.07
Nodes (3): pytest.capture, pytest.logging, unittest

### Community 35 - "Community 35"
Cohesion: 0.12
Nodes (15): LastPlacePruner, BasePruner, HyperbandPruner, Pruner using Hyperband.      As SuccessiveHalving (SHA) requires the number of c, Compute the trial allocated budget for a bracket of ``bracket_id``.          In, Compute the index of bracket for a trial of ``trial_number``.          The index, NopPruner, Pruner which never prunes trials.      Example:          .. testcode:: (+7 more)

### Community 36 - "Community 36"
Cohesion: 0.10
Nodes (7): _check_uploaded_artifact_meta(), test_get_all_artifact_meta_in_frozen_trial(), test_get_all_artifact_meta_in_study(), test_get_all_artifact_meta_in_trial(), optuna.artifacts, pathlib, stubs

### Community 37 - "Community 37"
Cohesion: 0.18
Nodes (5): _FanovaTree, _get_cardinality(), _get_cardinality_batched(), _get_subspaces(), sklearn.tree

### Community 38 - "Community 38"
Cohesion: 0.08
Nodes (2): optuna.samplers.nsgaii, optuna.samplers.nsgaiii.elite.population.selection.strategy

### Community 39 - "Community 39"
Cohesion: 0.09
Nodes (7): _compare_with_expected_suggested_values(), conditional_objective(), The tree shape of this template trials.     tree (param_name="a")     |_ 0: a0_b, template_trials_and_tree(), test_study_optimize_with_pruned_trials(), test_study_optimize_with_single_search_space(), test_study_optimize_with_single_search_space_user_added()

### Community 40 - "Community 40"
Cohesion: 0.08
Nodes (2): create_trial(), FrozenTrial

### Community 41 - "Community 41"
Cohesion: 0.12
Nodes (17): _create_study_mixture_category_types(), _create_study_with_constraints(), _create_study_with_log_scale_and_str_category_2d(), _create_study_with_log_scale_and_str_category_3d(), _get_nested_list_shape(), _named_tuple_equal(), test_generate_rank_info_with_constraints(), test_generate_rank_plot_for_few_observations() (+9 more)

### Community 42 - "Community 42"
Cohesion: 0.08
Nodes (6): .. _configurations:  Pythonic Search Space =====================  For hyperparam, _Fanova, An implementation of `An Efficient Approach for Assessing Hyperparameter Importa, optuna.importance.fanova.tree, sklearn.ensemble, sklearn.svm

### Community 43 - "Community 43"
Cohesion: 0.13
Nodes (3): BaseStorage, InMemoryStorage, Storage class that stores data in memory of the Python process.      Example:

### Community 44 - "Community 44"
Cohesion: 0.09
Nodes (5): _from_proto_trial(), _from_proto_trial_state(), OptunaStorageProxyService, _to_proto_trial(), _to_proto_trial_state()

### Community 45 - "Community 45"
Cohesion: 0.10
Nodes (11): BaseCrossover, BLXAlphaCrossover, Blend Crossover operation used by :class:`~optuna.samplers.NSGAIISampler`., Simulated Binary Crossover operation used by :class:`~optuna.samplers.NSGAIISamp, SBXCrossover, Simplex Crossover operation used by :class:`~optuna.samplers.NSGAIISampler`., SPXCrossover, Unimodal Normal Distribution Crossover used by :class:`~optuna.samplers.NSGAIISa (+3 more)

### Community 46 - "Community 46"
Cohesion: 0.14
Nodes (14): _extend_cholesky(), fit_kernel_params(), GPRegressor, Notations in this Gaussian process implementation  X_train: Observed parameter v, Return the kernel matrix with the shape of (..., n_A, n_B) given X1 and X2 each, This method computes the posterior mean and variance given the points `x` where, This method computes the marginal log-likelihood of the kernel hyperparameters g, Return conditional joint posterior samples for each query point.          For ba (+6 more)

### Community 47 - "Community 47"
Cohesion: 0.16
Nodes (21): _init_QMCSampler_without_exp_warning(), test_call_after_trial(), test_find_sample_id(), test_infer_relative_search_space(), test_infer_relative_search_space_dynamic_warning(), test_infer_relative_search_space_with_ask_fixed(), test_infer_relative_search_space_with_suggested_running(), test_infer_relative_search_space_without_any() (+13 more)

### Community 48 - "Community 48"
Cohesion: 0.09
Nodes (4): _compute_hssp_truth_and_approx(), test_solve_hssp(), test_solve_hssp_infinite_loss(), pytest

### Community 49 - "Community 49"
Cohesion: 0.10
Nodes (8): _create_study_mixture_category_types(), _create_study_with_log_scale_and_str_category_2d(), _create_study_with_log_scale_and_str_category_3d(), _create_study_with_overlapping_params(), test_get_contour_info_log_scale_and_str_category_2_params(), test_get_contour_info_log_scale_and_str_category_more_than_2_params(), test_get_contour_info_mixture_category_types(), test_get_contour_info_overlapping_params()

### Community 50 - "Community 50"
Cohesion: 0.12
Nodes (2): BaseTrial, FixedTrial

### Community 51 - "Community 51"
Cohesion: 0.26
Nodes (16): BaseAcquisitionFunc, ConstrainedLogEHVI, ConstrainedLogEI, LCB, logehvi(), logei(), LogPI, qLogEI (+8 more)

### Community 52 - "Community 52"
Cohesion: 0.16
Nodes (18): _calculate_hypervolume_improvement(), _extract_pareto_sols(), _generate_concave_instances(), _generate_convex_instances(), _generate_instances_with_negative(), _generate_linear_instances(), _generate_uniform_samples(), InstanceGenerator (+10 more)

### Community 53 - "Community 53"
Cohesion: 0.09
Nodes (4): multiprocessing.managers, optuna.testing.pytest.samplers, pytest.fixtures, unittest.mock

### Community 54 - "Community 54"
Cohesion: 0.11
Nodes (13): GCSArtifactStore, An artifact backend for Google Cloud Storage (GCS).      Args:         bucket_na, get_all_artifact_meta(), List the associated artifact information of the provided trial or study.      Ar, ArtifactStore, A protocol defining the interface for an artifact backend.      The methods defi, Open the artifact identified by the artifact_id.          This method should ret, Save the content to the backend.          Args:             artifact_id: The ide (+5 more)

### Community 55 - "Community 55"
Cohesion: 0.20
Nodes (14): A callback that terminates the optimization using Terminator.      This class im, TerminatorCallback, BaseErrorEvaluator, CrossValidationErrorEvaluator, An error evaluator that always returns a constant value.      This evaluator can, Base class for error evaluators., An error evaluator for objective functions based on cross-validation.      This, Evaluate the statistical error of the objective function based on cross-validati (+6 more)

### Community 56 - "Community 56"
Cohesion: 0.19
Nodes (16): build_state_fn(), frozen_trial_factory(), MockSystemAttr, Test samples are drawn from the specified category., Test sampling from int distribution returns integer., Tests FAIL, RUNNING, and WAITING states are equally., suggest(), test_multi_objective_sample_independent_categorical_distributions() (+8 more)

### Community 57 - "Community 57"
Cohesion: 0.11
Nodes (3): optuna.importance, optuna.importance.ped.anova.evaluator, optuna.testing.pytest.importance

### Community 58 - "Community 58"
Cohesion: 0.21
Nodes (17): _adjust_discrete_uniform_high(), _adjust_int_uniform_high(), DiscreteUniformDistribution, IntLogUniformDistribution, IntUniformDistribution, LogUniformDistribution, A uniform distribution in the linear domain.      This object is instantiated by, A uniform distribution in the log domain.      This object is instantiated by :f (+9 more)

### Community 59 - "Community 59"
Cohesion: 0.13
Nodes (20): _configure_library_root_logger(), create_default_formatter(), disable_default_handler(), disable_propagation(), enable_default_handler(), enable_propagation(), _get_library_name(), _get_library_root_logger() (+12 more)

### Community 60 - "Community 60"
Cohesion: 0.10
Nodes (2): BaseTrial, Base class for trials.      Note that this class is not supposed to be directly

### Community 61 - "Community 61"
Cohesion: 0.17
Nodes (15): _create_trial(), test_datetime_start(), test_not_contained_param(), test_report(), test_set_constraint(), test_set_constraint_nan(), test_set_constraint_override(), test_set_user_attrs() (+7 more)

### Community 62 - "Community 62"
Cohesion: 0.16
Nodes (15): define_model(), eval_model(), objective(), .. _visualization:  Quick Visualization for Hyperparameter Optimization Analysis, train_model(), define_model(), eval_model(), objective() (+7 more)

### Community 63 - "Community 63"
Cohesion: 0.12
Nodes (6): BaseTerminator, optuna.terminator, _DeterministicTerminator, test_terminator_callback_terminator(), _StaticImprovementEvaluator, test_should_terminate()

### Community 64 - "Community 64"
Cohesion: 0.18
Nodes (16): create.db, optuna.storages.rdb, platform, create_test_storage(), test_check_table_schema_compatibility(), test_create_new_trial_with_retries(), test_create_scoped_session(), test_engine_kwargs() (+8 more)

### Community 65 - "Community 65"
Cohesion: 0.11
Nodes (7): importlib, optuna.gp.acqf, optuna.gp.gp, optuna.gp.optim.mixed, optuna.gp.prior, Test that GPSampler works when torch.set_default_device('cuda') is set.      Reg, test_gpsampler_with_cuda_default_device()

### Community 66 - "Community 66"
Cohesion: 0.12
Nodes (7): optuna.importance.ped.anova.scott.parzen.estimator, optuna.samplers.tpe.parzen.estimator, optuna.samplers.tpe.probability.distributions, build_parzen_estimator_on_grid(), _count_categorical_param_in_grid(), _count_numerical_param_in_grid(), tests.samplers.tests.tpe.tests.test.parzen.estimator

### Community 67 - "Community 67"
Cohesion: 0.17
Nodes (12): _create_trial(), test_distributions(), test_eq_ne(), test_init(), test_lt(), test_number(), test_params(), test_set_value() (+4 more)

### Community 68 - "Community 68"
Cohesion: 0.13
Nodes (10): _create_study_with_categorical_params(), _create_study_with_failed_trial(), _create_study_with_log_params(), _create_study_with_log_scale_and_str_and_numeric_category(), _create_study_with_numeric_categorical_params(), test_get_parallel_coordinate_info(), test_get_parallel_coordinate_info_categorical_numeric_params(), test_get_parallel_coordinate_info_categorical_params() (+2 more)

### Community 69 - "Community 69"
Cohesion: 0.12
Nodes (4): _create_study_mixture_category_types(), _create_study_with_log_scale_and_str_category_2d(), test_get_slice_plot_info_log_scale_and_str_category_2_params(), test_get_slice_plot_info_mixture_category_types()

### Community 70 - "Community 70"
Cohesion: 0.17
Nodes (15): atoms_to_json(), create_mol(), create_slab(), file_to_atoms(), get_opt_energy(), json_to_atoms(), main(), Objective (+7 more)

### Community 71 - "Community 71"
Cohesion: 0.16
Nodes (7): Backoff, An artifact store's middleware for exponential backoff.      Example:        .., ArtifactNotFound, Exception raised when an artifact is not found.      It is typically raised whil, FileSystemArtifactStore, An artifact store for file systems.      Args:         base_path:             Th, OptunaError

### Community 72 - "Community 72"
Cohesion: 0.17
Nodes (9): download_artifact(), Download an artifact from the artifact store.      Args:         artifact_store:, FailArtifactStore, InMemoryArtifactStore, google.cloud.storage, io, optuna.artifacts.exceptions, optuna.artifacts.protocol (+1 more)

### Community 73 - "Community 73"
Cohesion: 0.11
Nodes (3): optuna.visualization.matplotlib.optimization.history, optuna.visualization.optimization.history, tests.visualization.tests.test.optimization.history

### Community 74 - "Community 74"
Cohesion: 0.15
Nodes (14): optuna.samplers.tpe.erf, _log_gauss_mass(), _log_ndtr(), _log_ndtr_single(), logpdf(), _ndtr_single(), _ndtri_exp(), _norm_logpdf() (+6 more)

### Community 75 - "Community 75"
Cohesion: 0.20
Nodes (11): optuna.samplers.tpe, _BatchedCategoricalDistributions, _BatchedDiscreteTruncLogNormDistributions, _BatchedDiscreteTruncNormDistributions, _BatchedTruncLogNormDistributions, _BatchedTruncNormDistributions, _log_gauss_mass_unique(), _MixtureOfProductDistribution (+3 more)

### Community 76 - "Community 76"
Cohesion: 0.16
Nodes (2): CmaEsSampler, _is_compatible_search_space()

### Community 77 - "Community 77"
Cohesion: 0.13
Nodes (7): Boto3ArtifactStore, _is_not_found_error(), An artifact backend for Boto3.      Args:         bucket_name:             The n, boto3, botocore.exceptions, moto, mypy.boto3.s3

### Community 78 - "Community 78"
Cohesion: 0.14
Nodes (4): JournalLogStorageSupplier, test_concurrent_append_logs_for_multi_processes(), test_concurrent_append_logs_for_multi_threads(), test_invalid_grace_period()

### Community 79 - "Community 79"
Cohesion: 0.13
Nodes (10): _DeferredImportExceptionContextManager, _LazyImport, Create a context manager that can wrap imports of optional packages to defer exc, Module wrapper for lazy import.      This class wraps the specified modules and, Context manager to defer exceptions from imports.      Catches :exc:`ImportError, Enter the context manager.          Returns:             Itself., Exit the context manager.          Args:             exc_type:                 R, Return whether the context manager has caught any exceptions.          Returns: (+2 more)

### Community 80 - "Community 80"
Cohesion: 0.19
Nodes (2): TPESampler, _warn_if_deprecated_argument()

### Community 81 - "Community 81"
Cohesion: 0.18
Nodes (4): _get_constraint_vals_and_feasibility(), _get_params(), GPSampler, _standardize_values()

### Community 82 - "Community 82"
Cohesion: 0.17
Nodes (13): BaseJournalFileLock, DeprecatedJournalFileOpenLock, DeprecatedJournalFileSymlinkLock, JournalFileOpenLock, JournalFileSymlinkLock, Lock class for synchronizing processes for NFSv2 or later.      On acquiring the, Acquire a lock in a blocking way by creating a symbolic link of a file., Release a lock by removing the symbolic link. (+5 more)

### Community 83 - "Community 83"
Cohesion: 0.13
Nodes (8): BaseSampler, Sample parameters in a given search space.          This method is called once a, Sample a parameter for a given distribution.          This method is called only, Trial pre-processing.          This method is called before the objective functi, Trial post-processing.          This method is called after the objective functi, Reseed sampler's random number generator.          This method is called by the, Base class for samplers.      Optuna combines two types of sampling strategies,, Infer the search space that will be used by relative sampling in the target tria

### Community 84 - "Community 84"
Cohesion: 0.14
Nodes (14): check_frozen_trial(), check_params(), check_study(), check_value(), func(), test_optimize_parallel(), test_optimize_parallel_timeout(), test_optimize_trivial_in_memory_new() (+6 more)

### Community 85 - "Community 85"
Cohesion: 0.13
Nodes (3): summary          detail, summary          detail          .. warning::             Deprecated in v1.1.0., _Sample

### Community 86 - "Community 86"
Cohesion: 0.13
Nodes (3): summary          detail, summary          detail          .. note::             Added in v1.1.0 as an exp, _Sample

### Community 87 - "Community 87"
Cohesion: 0.18
Nodes (8): BaseGASampler, optuna.samplers.ga.base, BaseGASamplerTestSampler, test_get_generation(), test_get_generation_already_set(), test_get_parent_population(), test_get_population(), test_systemattr_keys()

### Community 88 - "Community 88"
Cohesion: 0.17
Nodes (6): BaseGASampler, Get the population of the given generation.          Args:             study:, Get the parent population of the given generation.          This method caches t, Base class for Genetic Algorithm (GA) samplers.      Genetic Algorithm samplers, Select parent trials from the population for the given generation.          This, Get the generation number of the given trial.          This method returns the g

### Community 89 - "Community 89"
Cohesion: 0.21
Nodes (12): optuna.study.multi.objective, assert_is_output_equal_to_ans(), test_get_pareto_front_trials(), test_get_pareto_front_trials_with_constraint(), _trial_to_values(), _get_non_pareto_front_trials(), _get_pareto_front_info(), _get_pareto_front_plot() (+4 more)

### Community 90 - "Community 90"
Cohesion: 0.14
Nodes (4): optuna.testing.storages, pandas, _test_set_and_get_compatibility(), test_set_and_get_trial_state_values()

### Community 92 - "Community 92"
Cohesion: 0.20
Nodes (8): BaseHeartbeatThread, get_heartbeat_thread(), HeartbeatThread, is_heartbeat_enabled(), NullHeartbeatThread, Check whether the storage enables the heartbeat.      Returns:         :obj:`Tru, Record the heartbeat of the trial.          Args:             trial_id:, Get the heartbeat interval if it is set.          Returns:             The heart

### Community 93 - "Community 93"
Cohesion: 0.22
Nodes (10): _get_infeasible_trial_score(), _get_pruned_trial_score(), _get_reference_point(), _solve_hssp_with_cache(), _split_complete_trials(), _split_complete_trials_multi_objective(), _split_complete_trials_single_objective(), _split_infeasible_trials() (+2 more)

### Community 94 - "Community 94"
Cohesion: 0.25
Nodes (6): init_mock_client(), MockBlob, MockBucket, test_file_not_found_exception(), test_remove(), test_upload_download()

### Community 95 - "Community 95"
Cohesion: 0.14
Nodes (14): Exception, CLIUsageError, DuplicatedStudyError, OptunaError, Base class for Optuna specific errors., Exception for CLI.      CLI raises this exception when it receives invalid confi, Exception for storage operation.      This error is raised when an operation fai, Exception for a duplicated study name.      This error is raised when a specifie (+6 more)

### Community 96 - "Community 96"
Cohesion: 0.14
Nodes (1): optuna.testing.threading

### Community 97 - "Community 97"
Cohesion: 0.24
Nodes (13): _calculate_nondomination_rank(), _dominates(), _fast_non_domination_rank(), _get_pareto_front_trials(), _get_pareto_front_trials_by_trials(), _is_pareto_front(), _is_pareto_front_2d(), _is_pareto_front_for_unique_sorted() (+5 more)

### Community 98 - "Community 98"
Cohesion: 0.22
Nodes (9): save_static_image(), test_edf_plot_no_trials(), test_edf_plot_no_trials_studies(), test_get_edf_info(), test_inconsistent_number_of_trial_values(), test_plot_edf_with_multiple_studies(), test_plot_edf_with_target(), test_plot_edf_with_target_name() (+1 more)

### Community 100 - "Community 100"
Cohesion: 0.15
Nodes (5): .. _rdb:  Saving/Resuming Study with RDB Backend ===============================, .. _optuna_callback:  Callback for Study.optimize ===========================  T, StopWhenTrialKeepBeingPrunedCallback, .. _journal_storage:  (File-based) Journal Storage ============================, logging

### Community 101 - "Community 101"
Cohesion: 0.19
Nodes (8): AbstractContextManager, fakeredis, optuna.storages.journal, optuna.testing.tempfile.pool, socket, _find_free_port(), _lock_to_search_for_free_port(), StorageSupplier

### Community 102 - "Community 102"
Cohesion: 0.18
Nodes (11): _get_state_name(), _get_timeline_plot(), plot_timeline(), Plot the timeline of a study.      .. seealso::         Please refer to :func:`o, optuna.visualization.contour, optuna.visualization.edf, optuna.visualization.parallel.coordinate, optuna.visualization.param.importances (+3 more)

### Community 103 - "Community 103"
Cohesion: 0.17
Nodes (9): optuna.pruners.percentile, PercentilePruner, MedianPruner, Pruner using the median stopping rule.      Prune if the trial's best intermedia, _get_best_intermediate_result_over_steps(), _get_percentile_intermediate_result_over_trials(), _is_first_in_interval_step(), PercentilePruner (+1 more)

### Community 104 - "Community 104"
Cohesion: 0.23
Nodes (1): GridSampler

### Community 105 - "Community 105"
Cohesion: 0.17
Nodes (13): check_progressbar(), stop_objective(), test_optimize_progbar_n_trials_prioritized(), test_optimize_progbar_no_constraints(), test_optimize_with_progbar(), test_optimize_with_progbar_parallel_timeout(), test_optimize_with_progbar_timeout(), test_optimize_with_progbar_timeout_formats() (+5 more)

### Community 106 - "Community 106"
Cohesion: 0.20
Nodes (4): BaseJournalSnapshot, JournalRedisBackend, JournalRedisStorage, Redis storage class for Journal log backend.      Args:         url:

### Community 107 - "Community 107"
Cohesion: 0.26
Nodes (10): collections, _calc_lim_with_padding(), _generate_slice_subplot(), _get_categorical_plot_values(), _get_slice_plot(), plot_slice(), Plot the parameter relationship as slice plot in a study with Matplotlib.      ., _create_records_and_aggregate_column() (+2 more)

### Community 108 - "Community 108"
Cohesion: 0.23
Nodes (1): QMCSampler

### Community 109 - "Community 109"
Cohesion: 0.25
Nodes (5): _shuffle_and_filter_sols(), test_wfg_2d(), test_wfg_3d(), test_wfg_duplicate_points(), test_wfg_nd()

### Community 110 - "Community 110"
Cohesion: 0.18
Nodes (10): _associate_individuals_with_reference_points(), _filter_inf(), _generate_default_reference_point(), _normalize_objective_values(), _preserve_niche_individuals(), Generates default reference points which are `uniformly` spread on a hyperplane., Normalizes objective values of population.      An ideal point z* consists of mi, Associates each objective value to the closest reference point.      Associate e (+2 more)

### Community 111 - "Community 111"
Cohesion: 0.20
Nodes (3): optuna.testing.visualization, _is_plotly_available(), test_visualization_is_available()

### Community 113 - "Community 113"
Cohesion: 0.22
Nodes (3): re, _SimpleClass, test_convert_positional_args_future_warning_for_methods()

### Community 114 - "Community 114"
Cohesion: 0.20
Nodes (8): optuna.samplers.brute.force, optuna.samplers.cmaes, optuna.samplers.gp.sampler, optuna.samplers.grid, optuna.samplers.nsgaii.sampler, optuna.samplers.nsgaiii.sampler, optuna.samplers.partial.fixed, optuna.samplers.qmc

### Community 115 - "Community 115"
Cohesion: 0.33
Nodes (9): _discrete_line_search(), _exhaustive_search(), _gradient_ascent_batched(), _local_search_discrete(), _local_search_discrete_batched(), local_search_mixed_batched(), optimize_acqf_mixed(), # NOTE: Ideally, separating lengthscales should be used for the constraint funct (+1 more)

### Community 116 - "Community 116"
Cohesion: 0.27
Nodes (8): optuna.storages.cached.storage, optuna.storages.callbacks, optuna.storages.in.memory, optuna.storages.journal.base, optuna.storages.journal.file, optuna.storages.journal.redis, optuna.storages.journal.storage, optuna.storages.rdb.storage

### Community 117 - "Community 117"
Cohesion: 0.36
Nodes (9): _calculate_griddata(), _create_zmap(), _filter_missing_values(), _generate_contour_subplot(), _get_contour_plot(), _interpolate_zmap(), plot_contour(), Plot the parameter relationship as contour plot in a study with Matplotlib. (+1 more)

### Community 119 - "Community 119"
Cohesion: 0.20
Nodes (6): Return the list of retried trial numbers with respect to the specified trial., Deprecated alias of :class:`~optuna.storages.RetryHeartbeatStaleTrialCallback`., Retry a heartbeat-stale trial up to a maximum number of times.      When a runni, Return the number of the original trial being retried.          Args:, RetryFailedTrialCallback, RetryHeartbeatStaleTrialCallback

### Community 121 - "Community 121"
Cohesion: 0.36
Nodes (1): _ParzenEstimator

### Community 122 - "Community 122"
Cohesion: 0.33
Nodes (9): tqdm, _get_error_scatter(), _get_improvement_info(), _get_improvement_plot(), _get_improvement_scatter(), _get_y_range(), _ImprovementInfo, plot_terminator_improvement() (+1 more)

### Community 123 - "Community 123"
Cohesion: 0.36
Nodes (7): objective(), .. _wilcoxon_pruner:  Early-stopping independent evaluations by Wilcoxon pruner, SAOptions, tsp_cost(), tsp_greedy(), tsp_simulated_annealing(), numpy.linalg

### Community 124 - "Community 124"
Cohesion: 0.22
Nodes (3): argparse, This script generates assets for testing backward compatibility of `JournalStora, This script generates assets for testing schema migration.  1. Prepare Optuna  I

### Community 125 - "Community 125"
Cohesion: 0.50
Nodes (7): get_gpr(), test_eval_acqf(), test_eval_acqf_with_constraints(), test_eval_multi_objective_acqf(), test_eval_multi_objective_acqf_with_constraints(), test_eval_qlogei(), verify_eval_acqf()

### Community 126 - "Community 126"
Cohesion: 0.28
Nodes (5): test_batched_lbfgsb(), _verify_results(), X0_and_bounds(), optuna.gp.batched.lbfgsb, scipy.optimize

### Community 127 - "Community 127"
Cohesion: 0.33
Nodes (8): _compute_2d(), _compute_3d(), _compute_exclusive_hv(), _compute_hv(), compute_hypervolume(), Hypervolume calculator for any dimension.      This class exactly calculates the, Compute hypervolume in 3D. Time complexity is O(N^2) where N is sorted_pareto_so, # NOTE: For 3D points, we always prefer _compute_3d to _compute_hv because the t

### Community 129 - "Community 129"
Cohesion: 0.22
Nodes (3): matplotlib.axes.axes, matplotlib.pyplot, plot_hypervolume_history ========================  .. autofunction:: optuna.visu

### Community 130 - "Community 130"
Cohesion: 0.22
Nodes (3): is_available(), optuna.visualization.matplotlib, plot_terminator_improvement ===========================  .. autofunction:: optun

### Community 131 - "Community 131"
Cohesion: 0.22
Nodes (7): optuna.pruners.hyperband, optuna.pruners.median, optuna.pruners.nop, optuna.pruners.patient, optuna.pruners.successive.halving, optuna.pruners.threshold, optuna.pruners.wilcoxon

### Community 132 - "Community 132"
Cohesion: 0.28
Nodes (4): optuna.samplers.tpe.sampler, assert_distribution_almost_equal(), test_calculate(), test_init_parzen_estimator()

### Community 133 - "Community 133"
Cohesion: 0.25
Nodes (3): plotly.colors, _make_hovertext(), _make_json_compatible()

### Community 134 - "Community 134"
Cohesion: 0.39
Nodes (8): create_rdb_storage(), Test CachedStorage does flush to persistent storages.      The CachedStorage flu, test_create_trial(), test_delete_study(), test_read_trials_from_remote_storage(), test_set_trial_state_values(), test_uncached_set(), test_unfinished_trial_ids()

### Community 135 - "Community 135"
Cohesion: 0.31
Nodes (7): empty message  Revision ID: v2.4.0.a Revises: v1.3.0.a Create Date: 2020-11-17 0, StudyDirectionModel, StudyModel, TrialIntermediateValueModel, TrialModel, TrialValueModel, upgrade()

### Community 136 - "Community 136"
Cohesion: 0.36
Nodes (7): _create_study(), _create_study_negative_elapsed_time(), test_get_timeline_info(), test_get_timeline_info_n_recent_trials(), test_get_timeline_info_negative_elapsed_time(), test_get_timeline_plot(), test_plot_timeline_n_recent_trials_invalid()

### Community 137 - "Community 137"
Cohesion: 0.25
Nodes (2): .. _user_defined_sampler:  User-Defined Sampler ====================  Thanks to, SimulatedAnnealingSampler

### Community 138 - "Community 138"
Cohesion: 0.25
Nodes (7): optuna.artifacts.backoff, optuna.artifacts.boto3, optuna.artifacts.download, optuna.artifacts.filesystem, optuna.artifacts.gcs, optuna.artifacts.list.artifact.meta, optuna.artifacts.upload

### Community 139 - "Community 139"
Cohesion: 0.43
Nodes (7): concurrent.futures, grpc_journal_file_context(), _pop_waiting_trial_id(), test_pop_waiting_trial_multiprocess_safe(), test_pop_waiting_trial_thread_safe(), _verify_racing_condition(), multiprocessing

### Community 140 - "Community 140"
Cohesion: 0.29
Nodes (5): _IntegrationModule, Module class that implements `optuna.integration` package.          This class a, _LightGBMModule, Module class that implements `optuna.integration.lightgbm` package., ModuleType

### Community 141 - "Community 141"
Cohesion: 0.25
Nodes (6): optuna.samplers.nsgaii.crossovers.blxalpha, optuna.samplers.nsgaii.crossovers.sbx, optuna.samplers.nsgaii.crossovers.spx, optuna.samplers.nsgaii.crossovers.undx, optuna.samplers.nsgaii.crossovers.vsbx, optuna.samplers.nsgaii.mutations.polynomial

### Community 142 - "Community 142"
Cohesion: 0.25
Nodes (6): _calc_crowding_distance(), _crowding_distance_sort(), NSGAIIElitePopulationSelectionStrategy, _rank_population(), Select elite population from the given trials by NSGA-II algorithm.          Arg, Calculates the crowding distance of population.      We define the crowding dist

### Community 143 - "Community 143"
Cohesion: 0.25
Nodes (4): _ProgressBar, Progress Bar implementation for :func:`~optuna.study.Study.optimize` on the top, Update the progress bars if ``is_valid`` is :obj:`True`.          Args:, _TqdmLoggingHandler

### Community 144 - "Community 144"
Cohesion: 0.43
Nodes (6): optuna.pruners.base, _completed_rung_key(), _estimate_min_resource(), _get_competing_values(), _get_current_rung(), _is_trial_promotable_to_next_rung()

### Community 145 - "Community 145"
Cohesion: 0.25
Nodes (3): optuna.samplers.tpe.truncnorm, scipy.special, scipy.stats.continuous.distns

### Community 148 - "Community 148"
Cohesion: 0.25
Nodes (5): fail_stale_trials(), Fail stale trials and run their failure callbacks.      The running trials whose, Get the stale trial ids of the study.          Args:             study_id:, Get the heartbeat-stale trial callback function.          Returns:             T, Get the failed trial callback function.

### Community 149 - "Community 149"
Cohesion: 0.29
Nodes (3): NamedTemporaryFilePool, _parse_output(), Parse CLI output.      Args:         output:             The output of command.

### Community 150 - "Community 150"
Cohesion: 0.29
Nodes (6): Run migrations in 'offline' mode.      This configures the context with just a U, Run migrations in 'online' mode.      In this scenario we need to create an Engi, run_migrations_offline(), run_migrations_online(), logging.config, optuna.storages.rdb.models

### Community 151 - "Community 151"
Cohesion: 0.33
Nodes (5): BaseImprovementEvaluator, _compute_gp_posterior(), _compute_gp_posterior_cov_two_thetas(), EMMREvaluator, Evaluates a kind of regrets, called the Expected Minimum Model Regret(EMMR).

### Community 152 - "Community 152"
Cohesion: 0.29
Nodes (5): BaseJournalBackend, get_lock_file(), JournalFileBackend, JournalFileStorage, File storage class for Journal log backend.      Compared to SQLite3, the benefi

### Community 153 - "Community 153"
Cohesion: 0.29
Nodes (5): _get_unnormalized_param(), _normalize_one_param(), _round_one_normalized_param(), _sample_normalized_params(), _unnormalize_one_param()

### Community 154 - "Community 154"
Cohesion: 0.29
Nodes (1): optuna.gp.search.space

### Community 155 - "Community 155"
Cohesion: 0.43
Nodes (6): _lazy_contribs_update(), Solve a hypervolume subset selection problem (HSSP) via a greedy algorithm., Lazy update the hypervolume contributions.      (1) Lazy update of the hypervolu, _solve_hssp(), _solve_hssp_2d(), _solve_hssp_on_unique_loss_vals()

### Community 156 - "Community 156"
Cohesion: 0.33
Nodes (5): BaseJournalBackend, BaseJournalLogStorage, Base class for Journal storages.      Storage classes implementing this base cla, Read logs with a log number greater than or equal to ``log_number_from``., Append logs to the backend.          Args:             logs:                 A l

### Community 157 - "Community 157"
Cohesion: 0.48
Nodes (2): _calculate_axis_data(), _LabelEncoder

### Community 158 - "Community 158"
Cohesion: 0.29
Nodes (6): matplotlib, matplotlib.collections, matplotlib.colors, matplotlib.dates, matplotlib.figure, mpl.toolkits.mplot3d.axes3d

### Community 159 - "Community 159"
Cohesion: 0.52
Nodes (6): _inlined_categorical_uniform_crossover(), _is_contained(), perform_crossover(), _select_parent(), _select_parents(), _try_crossover()

### Community 162 - "Community 162"
Cohesion: 0.38
Nodes (3): _create_trial(), test_cross_validation_evaluator(), test_static_evaluator()

### Community 165 - "Community 165"
Cohesion: 0.47
Nodes (5): _get_box_bounds(), _get_non_dominated_box_bounds(), _get_upper_bound_set(), The functions in this file are mostly based on BoTorch v0.13.0, but they are ref, This function follows Algorithm 2 of Lacour17.      Args:         sorted_pareto_

### Community 166 - "Community 166"
Cohesion: 0.33
Nodes (4): BaseJournalSnapshot, Optional base class for Journal storages.      Storage classes implementing this, Save snapshot to the backend.          Args:             snapshot: A serialized, Load snapshot from the backend.          Returns:             A serialized snaps

### Community 167 - "Community 167"
Cohesion: 0.40
Nodes (2): _GroupDecomposedSearchSpace, _SearchSpaceGroup

### Community 168 - "Community 168"
Cohesion: 0.33
Nodes (4): _get_feasible_trials(), _is_constrained_optimization(), Return whether the given trials are created in constrained optimization., Return feasible trials from given trials.      This function assumes that the tr

### Community 169 - "Community 169"
Cohesion: 0.53
Nodes (5): _check_state_and_values(), _check_values_are_feasible(), _get_frozen_trial(), Internal method of :func:`~optuna.study.Study.tell`.      Refer to the document, _tell_with_warning()

### Community 170 - "Community 170"
Cohesion: 0.40
Nodes (3): BaseErrorEvaluator, MedianErrorEvaluator, An error evaluator that returns the ratio to initial median.      This error eva

### Community 171 - "Community 171"
Cohesion: 0.40
Nodes (3): Matern52Kernel, This method calculates `exp(-sqrt5d) * (1/3 * sqrt5d ** 2 + sqrt5d + 1)` where, Let x be squared_distance, f(x) be forward(ctx, x), and g(f) be a provided funct

### Community 172 - "Community 172"
Cohesion: 0.40
Nodes (5): experimental_class(), experimental_func(), Decorate function as experimental.      Args:         version: The first version, Decorate class as experimental.      Args:         version: The first version th, _validate_version()

### Community 173 - "Community 173"
Cohesion: 0.40
Nodes (4): packaging, plotly, plotly.graph.objects, plotly.subplots

### Community 174 - "Community 174"
Cohesion: 0.40
Nodes (3): _check_value(), Pruner to detect outlying metrics of the trials.      Prune if a metric exceeds, ThresholdPruner

### Community 175 - "Community 175"
Cohesion: 0.40
Nodes (1): DeterministicSampler

### Community 176 - "Community 176"
Cohesion: 0.60
Nodes (4): df(), f(), objective(), plot_intermediate_values ========================  .. autofunction:: optuna.visu

### Community 177 - "Community 177"
Cohesion: 0.50
Nodes (1): .. _ablation_study:  Ablation Study Becomes Easy with BruteForceSampler ========

### Community 178 - "Community 178"
Cohesion: 0.67
Nodes (3): numpy.polynomial, erf(), _erf_right_non_big()

### Community 179 - "Community 179"
Cohesion: 0.50
Nodes (3): BasePruner, Base class for pruners., Judge whether the trial should be pruned based on the reported values.

### Community 180 - "Community 180"
Cohesion: 0.50
Nodes (2): PatientPruner, Pruner which wraps another pruner with tolerance.      This pruner monitors inte

### Community 181 - "Community 181"
Cohesion: 0.50
Nodes (2): Pruner based on the `Wilcoxon signed-rank test <https://en.wikipedia.org/w/index, WilcoxonPruner

### Community 182 - "Community 182"
Cohesion: 0.50
Nodes (4): _assert_population_per_rank(), test_rank_population_missing_constraint_values(), test_rank_population_no_constraints(), test_rank_population_with_constraints()

### Community 183 - "Community 183"
Cohesion: 0.50
Nodes (1): DeterministicPruner

### Community 184 - "Community 184"
Cohesion: 0.50
Nodes (1): _TestableThread

### Community 185 - "Community 185"
Cohesion: 0.50
Nodes (4): _get_hypervolume_history_info(), _get_hypervolume_history_plot(), plot_hypervolume_history(), Plot hypervolume history of all trials in a study.      Args:         study:

### Community 186 - "Community 186"
Cohesion: 0.67
Nodes (3): ackley(), objective(), plot_edf ========  .. autofunction:: optuna.visualization.matplotlib.plot_edf  T

### Community 187 - "Community 187"
Cohesion: 0.67
Nodes (1): .. _first:  Lightweight, versatile, and platform agnostic architecture =========

### Community 188 - "Community 188"
Cohesion: 0.67
Nodes (1): .. _cli:  Command-Line Interface ======================  .. csv-table::    :head

### Community 189 - "Community 189"
Cohesion: 0.67
Nodes (2): google.protobuf, google.protobuf.internal

### Community 190 - "Community 190"
Cohesion: 0.67
Nodes (2): optuna.storages.grpc.client, optuna.storages.grpc.server

### Community 191 - "Community 191"
Cohesion: 0.67
Nodes (3): ExperimentalWarning, Experimental Warning class.      This implementation exists here because the pol, Warning

### Community 192 - "Community 192"
Cohesion: 0.67
Nodes (2): optuna.search.space.group.decomposed, optuna.search.space.intersection

### Community 193 - "Community 193"
Cohesion: 0.67
Nodes (1): _StudyInfo

### Community 195 - "Community 195"
Cohesion: 0.67
Nodes (1): plot_contour ============  .. autofunction:: optuna.visualization.matplotlib.plo

### Community 196 - "Community 196"
Cohesion: 0.67
Nodes (1): plot_optimization_history =========================  .. autofunction:: optuna.vi

### Community 197 - "Community 197"
Cohesion: 0.67
Nodes (1): plot_parallel_coordinate ========================  .. autofunction:: optuna.visu

### Community 198 - "Community 198"
Cohesion: 0.67
Nodes (1): plot_param_importances ======================  .. autofunction:: optuna.visualiz

### Community 199 - "Community 199"
Cohesion: 0.67
Nodes (1): plot_pareto_front =================  .. autofunction:: optuna.visualization.matp

### Community 200 - "Community 200"
Cohesion: 0.67
Nodes (1): plot_rank =========  .. autofunction:: optuna.visualization.matplotlib.plot_rank

### Community 201 - "Community 201"
Cohesion: 0.67
Nodes (1): plot_slice ============  .. autofunction:: optuna.visualization.matplotlib.plot_

### Community 202 - "Community 202"
Cohesion: 1.00
Nodes (1): optuna.importance.fanova.evaluator

### Community 203 - "Community 203"
Cohesion: 1.00
Nodes (1): test_mutation_deterministic()

### Community 204 - "Community 204"
Cohesion: 1.00
Nodes (2): _nan_equal(), test_calc_crowding_distance()

### Community 205 - "Community 205"
Cohesion: 1.00
Nodes (2): Test _get_best_trial method with deepcopy parameter control., test_get_best_trial()

## Knowledge Gaps
- **220 isolated node(s):** `plot_contour ============  .. autofunction:: optuna.visualization.plot_contour`, `plot_edf ========  .. autofunction:: optuna.visualization.plot_edf  The followin`, `plot_hypervolume_history ========================  .. autofunction:: optuna.visu`, `plot_intermediate_values ========================  .. autofunction:: optuna.visu`, `plot_optimization_history =========================  .. autofunction:: optuna.vi` (+215 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 38`** (2 nodes): `optuna.samplers.nsgaii`, `optuna.samplers.nsgaiii.elite.population.selection.strategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (2 nodes): `create_trial()`, `FrozenTrial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (2 nodes): `BaseTrial`, `FixedTrial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 60`** (2 nodes): `BaseTrial`, `Base class for trials.      Note that this class is not supposed to be directly`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 76`** (2 nodes): `CmaEsSampler`, `_is_compatible_search_space()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 80`** (2 nodes): `TPESampler`, `_warn_if_deprecated_argument()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 96`** (1 nodes): `optuna.testing.threading`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 104`** (1 nodes): `GridSampler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 108`** (1 nodes): `QMCSampler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 121`** (1 nodes): `_ParzenEstimator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 137`** (2 nodes): `.. _user_defined_sampler:  User-Defined Sampler ====================  Thanks to`, `SimulatedAnnealingSampler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 154`** (1 nodes): `optuna.gp.search.space`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 157`** (2 nodes): `_calculate_axis_data()`, `_LabelEncoder`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 167`** (2 nodes): `_GroupDecomposedSearchSpace`, `_SearchSpaceGroup`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 175`** (1 nodes): `DeterministicSampler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 177`** (1 nodes): `.. _ablation_study:  Ablation Study Becomes Easy with BruteForceSampler ========`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 180`** (2 nodes): `PatientPruner`, `Pruner which wraps another pruner with tolerance.      This pruner monitors inte`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 181`** (2 nodes): `Pruner based on the `Wilcoxon signed-rank test <https://en.wikipedia.org/w/index`, `WilcoxonPruner`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 183`** (1 nodes): `DeterministicPruner`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 184`** (1 nodes): `_TestableThread`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 187`** (1 nodes): `.. _first:  Lightweight, versatile, and platform agnostic architecture =========`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 188`** (1 nodes): `.. _cli:  Command-Line Interface ======================  .. csv-table::    :head`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 189`** (2 nodes): `google.protobuf`, `google.protobuf.internal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (2 nodes): `optuna.storages.grpc.client`, `optuna.storages.grpc.server`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 192`** (2 nodes): `optuna.search.space.group.decomposed`, `optuna.search.space.intersection`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 193`** (1 nodes): `_StudyInfo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 195`** (1 nodes): `plot_contour ============  .. autofunction:: optuna.visualization.matplotlib.plo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 196`** (1 nodes): `plot_optimization_history =========================  .. autofunction:: optuna.vi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 197`** (1 nodes): `plot_parallel_coordinate ========================  .. autofunction:: optuna.visu`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 198`** (1 nodes): `plot_param_importances ======================  .. autofunction:: optuna.visualiz`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 199`** (1 nodes): `plot_pareto_front =================  .. autofunction:: optuna.visualization.matp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 200`** (1 nodes): `plot_rank =========  .. autofunction:: optuna.visualization.matplotlib.plot_rank`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 201`** (1 nodes): `plot_slice ============  .. autofunction:: optuna.visualization.matplotlib.plot_`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 202`** (1 nodes): `optuna.importance.fanova.evaluator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 203`** (1 nodes): `test_mutation_deterministic()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 204`** (2 nodes): `_nan_equal()`, `test_calc_crowding_distance()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 205`** (2 nodes): `Test _get_best_trial method with deepcopy parameter control.`, `test_get_best_trial()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Study` connect `Community 0` to `Community 54`, `Community 45`, `Community 4`, `Community 88`, `Community 81`, `Community 157`, `Community 117`, `Community 2`, `Community 13`, `Community 21`, `Community 107`, `Community 25`, `Community 102`, `Community 142`, `Community 110`, `Community 143`, `Community 35`, `Community 174`, `Community 83`, `Community 28`, `Community 104`, `Community 108`, `Community 1`, `Community 87`, `Community 167`, `Community 3`, `Community 8`, `Community 5`, `Community 55`, `Community 63`, `Community 23`, `Community 80`, `Community 185`, `Community 9`, `Community 89`, `Community 122`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Why does `BaseDistribution` connect `Community 4` to `Community 81`, `Community 1`, `Community 51`, `Community 27`, `Community 5`, `Community 0`, `Community 17`, `Community 18`, `Community 58`, `Community 83`, `Community 28`, `Community 76`, `Community 104`, `Community 108`, `Community 87`, `Community 23`, `Community 167`, `Community 8`, `Community 31`, `Community 175`, `Community 121`, `Community 80`, `Community 60`, `Community 50`, `Community 40`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **Why does `StudyDirection` connect `Community 5` to `Community 27`, `Community 44`, `Community 17`, `Community 180`, `Community 103`, `Community 35`, `Community 181`, `Community 10`, `Community 11`, `Community 76`, `Community 4`, `Community 26`, `Community 43`, `Community 193`, `Community 29`, `Community 97`, `Community 9`, `Community 8`, `Community 0`, `Community 63`, `Community 1`, `Community 16`, `Community 80`, `Community 185`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 194 inferred relationships involving `Study` (e.g. with `List the associated artifact information of the provided trial or study.      Ar` and `ArtifactMeta`) actually correct?**
  _`Study` has 194 INFERRED edges - model-reasoned connections that need verification._
- **Are the 200 inferred relationships involving `BaseDistribution` (e.g. with `GPSampler` and `Sampler using Gaussian process-based Bayesian optimization.      .. note::`) actually correct?**
  _`BaseDistribution` has 200 INFERRED edges - model-reasoned connections that need verification._
- **Are the 148 inferred relationships involving `StudyDirection` (e.g. with `GrpcClientCache` and `GrpcClientCacheEntry`) actually correct?**
  _`StudyDirection` has 148 INFERRED edges - model-reasoned connections that need verification._
- **What connects `plot_contour ============  .. autofunction:: optuna.visualization.plot_contour`, `plot_edf ========  .. autofunction:: optuna.visualization.plot_edf  The followin`, `plot_hypervolume_history ========================  .. autofunction:: optuna.visu` to the rest of the system?**
  _220 weakly-connected nodes found - possible documentation gaps or missing edges._