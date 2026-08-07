# Graph Report - optuna  (2026-08-06)

## Corpus Check
- 220 files · ~127,168 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2318 nodes · 4252 edges · 180 communities detected
- Extraction: 75% EXTRACTED · 25% INFERRED · 0% AMBIGUOUS · INFERRED: 1058 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: uses: 1058 · method: 1017 · calls: 768 · contains: 638 · rationale_for: 412 · inherits: 175 · imports_from: 150 · imports: 34


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 220 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `b6f2ea6`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Study` - 227 edges
2. `BaseDistribution` - 207 edges
3. `StudyDirection` - 139 edges
4. `FloatDistribution` - 88 edges
5. `CategoricalDistribution` - 81 edges
6. `IntDistribution` - 78 edges
7. `FrozenStudy` - 68 edges
8. `RDBStorage` - 57 edges
9. `StorageTestCase` - 50 edges
10. `TrialState` - 44 edges

## Surprising Connections (you probably didn't know these)
- `Set a maximum number of trials before ending the study.      While the ``n_trial` --uses--> `Study`  [INFERRED]
  _callbacks.py → study/study.py
- `Base class for crossovers.      A crossover operation is used by :class:`~optuna` --uses--> `Study`  [INFERRED]
  samplers/nsgaii/_crossovers/_base.py → study/study.py
- `Number of parent individuals required to perform crossover.` --uses--> `Study`  [INFERRED]
  samplers/nsgaii/_crossovers/_base.py → study/study.py
- `Perform crossover of selected parent individuals.          This method is called` --uses--> `Study`  [INFERRED]
  samplers/nsgaii/_crossovers/_base.py → study/study.py
- `Blend Crossover operation used by :class:`~optuna.samplers.NSGAIISampler`.` --uses--> `Study`  [INFERRED]
  samplers/nsgaii/_crossovers/_blxalpha.py → study/study.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (29): NopPruner, Pruner which never prunes trials.      Example:          .. testcode::, Add trials to study.          The trials are validated before being added., Set metric names.          This method names each dimension of the returned valu, Return :obj:`True` if the study has multiple objectives.          Returns:, Return parameters of the best trial in the study.          .. note::, Return the best objective value in the study.          .. note::             Thi, Return the best trial in the study.          .. note::             This feature (+21 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (5): BaseHeartbeat, _create_scoped_session(), escape_alembic_config_value(), RDBStorage, _VersionManager

### Community 2 - "Community 2"
Cohesion: 0.07
Nodes (38): CategoricalDistribution, FloatDistribution, IntDistribution, json_to_distribution(), A distribution on floats.      This object is instantiated by :func:`~optuna.tri, A distribution on integers.      This object is instantiated by :func:`~optuna.t, A categorical distribution.      This object is instantiated by :func:`~optuna.t, Deserialize a distribution in JSON format.      Args:         json_str: A JSON-s (+30 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (11): _generate_trial(), is_equal_floats(), _setup_studies(), StorageTestCase, _test_set_and_get_study_system_attrs_for_floats(), _test_set_and_get_study_user_attrs_for_floats(), _test_set_and_get_trial_param_for_floats(), _test_set_and_get_trial_system_attr_for_floats() (+3 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (25): BaseDistribution, Base class for distributions.      Note that distribution classes are not suppos, Convert internal representation of a parameter value into external representatio, Convert external representation of a parameter value into internal representatio, Test whether the range of this distribution contains just a single value., Test if a parameter value is contained in the range of this distribution., Sampler using Gaussian process-based Bayesian optimization.      .. note::, BaseImprovementEvaluator (+17 more)

### Community 5 - "Community 5"
Cohesion: 0.10
Nodes (2): JournalStorage, JournalStorageReplayResult

### Community 6 - "Community 6"
Cohesion: 0.06
Nodes (29): _adjust_discrete_uniform_high(), _adjust_int_uniform_high(), _categorical_choice_equal(), check_distribution_compatibility(), _convert_old_distribution_to_new_distribution(), DiscreteUniformDistribution, distribution_to_json(), IntLogUniformDistribution (+21 more)

### Community 7 - "Community 7"
Cohesion: 0.06
Nodes (22): BaseJournalBackend, BaseJournalSnapshot, BaseJournalFileLock, DeprecatedJournalFileOpenLock, DeprecatedJournalFileSymlinkLock, get_lock_file(), JournalFileBackend, JournalFileOpenLock (+14 more)

### Community 8 - "Community 8"
Cohesion: 0.08
Nodes (28): Run migrations in 'offline' mode.      This configures the context with just a U, Run migrations in 'online' mode.      In this scenario we need to create an Engi, run_migrations_offline(), run_migrations_online(), _get_constraint_vals_and_feasibility(), _get_params(), GPSampler, _standardize_values() (+20 more)

### Community 9 - "Community 9"
Cohesion: 0.10
Nodes (2): InMemoryStorage, _StudyInfo

### Community 10 - "Community 10"
Cohesion: 0.08
Nodes (2): _CachedStorage, _StudyInfo

### Community 11 - "Community 11"
Cohesion: 0.10
Nodes (14): _get_infeasible_trial_score(), _get_pruned_trial_score(), _get_reference_point(), Return the the default parameters of hyperopt (v0.1.2).          :class:`~optuna, Sampler using TPE (Tree-structured Parzen Estimator) algorithm.      On each tri, _solve_hssp_with_cache(), _split_complete_trials(), _split_complete_trials_multi_objective() (+6 more)

### Community 12 - "Community 12"
Cohesion: 0.07
Nodes (7): BaseStorage, create_insecure_channel(), GrpcStorageProxy, gRPC client for :func:`~optuna.storages.run_grpc_proxy_server`.      Example:, Set up the gRPC channel and stub., Wait until the gRPC server is ready.          Args:             timeout: The max, Close the gRPC channel.

### Community 13 - "Community 13"
Cohesion: 0.11
Nodes (22): JournalOperation, Storage class for Journal storage backend.      Note that library users can inst, Removes the current session.          A session is stored in SQLAlchemy's Thread, Upgrade the storage schema., Return the schema version currently used by this storage., Return the latest schema version., Return the schema version list., Storage class for RDB backend.      Note that library users can instantiate this (+14 more)

### Community 14 - "Community 14"
Cohesion: 0.14
Nodes (7): _BaseSamplerTestCase, BasicSamplerTestCase, _create_new_trial(), FixedSampler, MultiObjectiveSamplerTestCase, RelativeSamplerTestCase, SingleOnlySamplerTestCase

### Community 15 - "Community 15"
Cohesion: 0.10
Nodes (17): BaseImportanceEvaluator, FanovaImportanceEvaluator, fANOVA importance evaluator.      Implements the fANOVA hyperparameter importanc, BaseImportanceEvaluator, Abstract parameter importance evaluator., Evaluate parameter importances based on completed trials in the given study., get_param_importances(), Evaluate parameter importances (:class:`~optuna.importance.PedAnovaImportanceEva (+9 more)

### Community 16 - "Community 16"
Cohesion: 0.12
Nodes (16): A callback that terminates the optimization using Terminator.      This class im, TerminatorCallback, BaseErrorEvaluator, CrossValidationErrorEvaluator, A function to report cross-validation scores of a trial.      This function shou, An error evaluator that always returns a constant value.      This evaluator can, Base class for error evaluators., An error evaluator for objective functions based on cross-validation.      This (+8 more)

### Community 17 - "Community 17"
Cohesion: 0.09
Nodes (18): convert_positional_args(), Convert positional arguments to keyword arguments.      Args:         previous_p, deprecated_class(), deprecated_func(), Decorate class as deprecated.      Args:         deprecated_version:, Decorate function as deprecated.      Args:         deprecated_version:, _validate_two_version(), experimental_class() (+10 more)

### Community 18 - "Community 18"
Cohesion: 0.07
Nodes (15): BaseStorage, Read the ID of a study.          Args:             study_name:                 N, Read the study name of a study.          Args:             study_id:, Read the user-defined attributes of a study.          Args:             study_id, Read the optuna-internal attributes of a study.          Args:             study, Base class for storages.      This class is not supposed to be directly accessed, Read a list of :class:`~optuna.study.FrozenStudy` objects.          Returns:, Create and add a new trial to a study.          The returned trial ID is unique (+7 more)

### Community 19 - "Community 19"
Cohesion: 0.11
Nodes (11): _LazyTrialSystemAttrs, Suggest a value for the continuous parameter.          The value is sampled from, Suggest a value for the continuous parameter.          The value is sampled from, Suggest a value for the discrete parameter.          The value is sampled from t, Suggest a value for the integer parameter.          The value is sampled from th, Suggest a value for the categorical parameter.          The value is sampled fro, A trial is a process of evaluating an objective function.      This object is pa, Suggest whether the trial should be pruned or not.          The suggestion is ma (+3 more)

### Community 20 - "Community 20"
Cohesion: 0.10
Nodes (2): ABC, # NOTE: ei(z) = z * cdf(z) + pdf(z)

### Community 21 - "Community 21"
Cohesion: 0.08
Nodes (2): create_trial(), FrozenTrial

### Community 22 - "Community 22"
Cohesion: 0.10
Nodes (5): _from_proto_trial(), _from_proto_trial_state(), OptunaStorageProxyService, _to_proto_trial(), _to_proto_trial_state()

### Community 23 - "Community 23"
Cohesion: 0.10
Nodes (11): BaseHeartbeatThread, fail_stale_trials(), get_heartbeat_thread(), HeartbeatThread, is_heartbeat_enabled(), NullHeartbeatThread, Fail stale trials and run their failure callbacks.      The running trials whose, Check whether the storage enables the heartbeat.      Returns:         :obj:`Tru (+3 more)

### Community 24 - "Community 24"
Cohesion: 0.19
Nodes (4): _FanovaTree, _get_cardinality(), _get_cardinality_batched(), _get_subspaces()

### Community 25 - "Community 25"
Cohesion: 0.11
Nodes (2): BaseTrial, FixedTrial

### Community 26 - "Community 26"
Cohesion: 0.16
Nodes (6): _BaseImportanceEvaluatorTestCase, BasicImportanceEvaluatorTestCase, ConditionalImportanceEvaluatorTestCase, _get_study(), MultiObjectiveImportanceEvaluatorTestCase, NonConditionalImportanceEvaluatorTestCase

### Community 27 - "Community 27"
Cohesion: 0.10
Nodes (2): *     Optuna storage service defines APIs to interact with the storage., StorageService

### Community 28 - "Community 28"
Cohesion: 0.10
Nodes (9): BaseCrossover, BLXAlphaCrossover, Blend Crossover operation used by :class:`~optuna.samplers.NSGAIISampler`., Simulated Binary Crossover operation used by :class:`~optuna.samplers.NSGAIISamp, SBXCrossover, Simplex Crossover operation used by :class:`~optuna.samplers.NSGAIISampler`., SPXCrossover, Modified Simulated Binary Crossover operation used by     :class:`~optuna.sample (+1 more)

### Community 29 - "Community 29"
Cohesion: 0.18
Nodes (6): BruteForceSampler, _enumerate_candidates(), _get_non_waiting_trials_and_current_trial_index(), _is_nan(), Sampler that performs exhaustive search over the define-by-run search space., _TreeNode

### Community 30 - "Community 30"
Cohesion: 0.10
Nodes (2): BaseTrial, Base class for trials.      Note that this class is not supposed to be directly

### Community 31 - "Community 31"
Cohesion: 0.18
Nodes (10): BasePruner, HyperbandPruner, Pruner using Hyperband.      As SuccessiveHalving (SHA) requires the number of c, Compute the trial allocated budget for a bracket of ``bracket_id``.          In, Compute the index of bracket for a trial of ``trial_number``.          The index, Pruner using Asynchronous Successive Halving Algorithm.      `Successive Halving, SuccessiveHalvingPruner, Return a bool value to represent whether the trial state is unfinished or not. (+2 more)

### Community 32 - "Community 32"
Cohesion: 0.12
Nodes (10): _DeferredImportExceptionContextManager, _LazyImport, Create a context manager that can wrap imports of optional packages to defer exc, Module wrapper for lazy import.      This class wraps the specified modules and, Context manager to defer exceptions from imports.      Catches :exc:`ImportError, Enter the context manager.          Returns:             Itself., Exit the context manager.          Args:             exc_type:                 R, Return whether the context manager has caught any exceptions.          Returns: (+2 more)

### Community 33 - "Community 33"
Cohesion: 0.11
Nodes (8): StudyDirectionModel, StudyModel, StudySystemAttributeModel, StudyUserAttributeModel, TrialHeartbeatModel, TrialIntermediateValueType, TrialValueType, VersionInfoModel

### Community 34 - "Community 34"
Cohesion: 0.16
Nodes (2): CmaEsSampler, _is_compatible_search_space()

### Community 35 - "Community 35"
Cohesion: 0.11
Nodes (10): *     Optuna storage service defines APIs to interact with the storage., *         Create a new study., *         Delete a study., *         Set a study's user attribute., *         Set a study's system attribute., *         Get a study id by its name., *         Get a study name by its id., *         Get study directions. (+2 more)

### Community 36 - "Community 36"
Cohesion: 0.14
Nodes (17): Exception, CLIUsageError, DuplicatedStudyError, ExperimentalWarning, OptunaError, Base class for Optuna specific errors., Exception for CLI.      CLI raises this exception when it receives invalid confi, Exception for storage operation.      This error is raised when an operation fai (+9 more)

### Community 37 - "Community 37"
Cohesion: 0.20
Nodes (8): fit_kernel_params(), GPRegressor, Return the kernel matrix with the shape of (..., n_A, n_B) given X1 and X2 each, This method computes the posterior mean and variance given the points `x` where, This method computes the marginal log-likelihood of the kernel hyperparameters g, Return conditional joint posterior samples for each query point.          For ba, This function returns the tensor `X` by solving the linear system `A @ X = B`,, _solve_cholesky()

### Community 38 - "Community 38"
Cohesion: 0.20
Nodes (11): _calculate_axis_data(), _calculate_griddata(), _create_zmap(), _filter_missing_values(), _generate_contour_subplot(), _get_contour_plot(), _interpolate_zmap(), _LabelEncoder (+3 more)

### Community 39 - "Community 39"
Cohesion: 0.13
Nodes (14): copy_study(), create_study(), delete_study(), get_all_study_names(), get_all_study_summaries(), load_study(), Create a new :class:`~optuna.study.Study`.      Example:          .. testcode::, Load the existing :class:`~optuna.study.Study` that has the specified name. (+6 more)

### Community 40 - "Community 40"
Cohesion: 0.14
Nodes (8): _BatchedCategoricalDistributions, _BatchedDiscreteTruncLogNormDistributions, _BatchedDiscreteTruncNormDistributions, _log_gauss_mass_unique(), _MixtureOfProductDistribution, This function is a quicker version of:         np.unique(np.concatenate([a[:, No, This function reduces the log Gaussian probability mass computation by avoiding, _unique_inverse_2d()

### Community 41 - "Community 41"
Cohesion: 0.16
Nodes (13): _log_gauss_mass(), _log_ndtr(), _log_ndtr_single(), logpdf(), _ndtr_single(), _ndtri_exp(), _norm_logpdf(), ppf() (+5 more)

### Community 42 - "Community 42"
Cohesion: 0.16
Nodes (5): AbstractContextManager, _find_free_port(), _lock_to_search_for_free_port(), StorageSupplier, NamedTemporaryFilePool

### Community 43 - "Community 43"
Cohesion: 0.16
Nodes (7): BaseSampler, BaseGASampler, Get the population of the given generation.          Args:             study:, Get the parent population of the given generation.          This method caches t, Base class for Genetic Algorithm (GA) samplers.      Genetic Algorithm samplers, Select parent trials from the population for the given generation.          This, Get the generation number of the given trial.          This method returns the g

### Community 44 - "Community 44"
Cohesion: 0.13
Nodes (8): BaseSampler, Sample parameters in a given search space.          This method is called once a, Sample a parameter for a given distribution.          This method is called only, Trial pre-processing.          This method is called before the objective functi, Trial post-processing.          This method is called after the objective functi, Reseed sampler's random number generator.          This method is called by the, Base class for samplers.      Optuna combines two types of sampling strategies,, Infer the search space that will be used by relative sampling in the target tria

### Community 45 - "Community 45"
Cohesion: 0.14
Nodes (10): BaseJournalBackend, BaseJournalLogStorage, BaseJournalSnapshot, Base class for Journal storages.      Storage classes implementing this base cla, Read logs with a log number greater than or equal to ``log_number_from``., Append logs to the backend.          Args:             logs:                 A l, Optional base class for Journal storages.      Storage classes implementing this, Save snapshot to the backend.          Args:             snapshot: A serialized (+2 more)

### Community 46 - "Community 46"
Cohesion: 0.22
Nodes (14): _calculate_nondomination_rank(), _dominates(), _fast_non_domination_rank(), _get_pareto_front_trials(), _get_pareto_front_trials_by_trials(), _is_pareto_front(), _is_pareto_front_2d(), _is_pareto_front_for_unique_sorted() (+6 more)

### Community 47 - "Community 47"
Cohesion: 0.25
Nodes (14): _AxisInfo, _convert_color_idxs_to_scaled_rgb_colors(), _get_axis_info(), _get_order_with_same_order_averaging(), _get_rank_info(), _get_rank_plot(), _get_rank_subplot(), _get_rank_subplot_info() (+6 more)

### Community 48 - "Community 48"
Cohesion: 0.14
Nodes (4): BaseAcquisitionFunc, LCB, logehvi(), UCB

### Community 49 - "Community 49"
Cohesion: 0.21
Nodes (1): GridSampler

### Community 50 - "Community 50"
Cohesion: 0.14
Nodes (7): Read the trial number of a trial.          .. note::              The trial numb, Read the parameter of a trial.          Args:             trial_id:, Read a trial.          Args:             trial_id:                 ID of the tri, Read the parameter dictionary of a trial.          Args:             trial_id:, Read the user-defined attributes of a trial.          Args:             trial_id, Read the optuna-internal attributes of a trial.          Args:             trial, Check whether a trial state is updatable.          Args:             trial_id:

### Community 51 - "Community 51"
Cohesion: 0.19
Nodes (7): Untransform a parameter configuration from continuous space to actual values., Transform a search space and parameter configurations to continuous space., Transform a parameter configuration from actual values to continuous space., _SearchSpaceTransform, _transform_numerical_param(), _transform_search_space(), _untransform_numerical_param()

### Community 52 - "Community 52"
Cohesion: 0.26
Nodes (13): _AxisInfo, _ContourInfo, _create_scatter(), _get_axis_info(), _get_contour_info(), _get_contour_plot(), _get_contour_subplot(), _get_contour_subplot_info() (+5 more)

### Community 53 - "Community 53"
Cohesion: 0.22
Nodes (9): ValueType, Enum, _get_optimization_history_info_list(), _get_optimization_history_plot(), _OptimizationHistoryInfo, plot_optimization_history(), Plot optimization history of all trials in a study.      Args:         study:, _ValuesInfo (+1 more)

### Community 54 - "Community 54"
Cohesion: 0.24
Nodes (11): _add_commands(), _add_common_arguments(), _convert_to_dict(), _format_value(), _get_parser(), main(), _preprocess_argv(), Optuna CLI module. If you want to add a new command, you also need to update the (+3 more)

### Community 55 - "Community 55"
Cohesion: 0.21
Nodes (8): PercentilePruner, MedianPruner, Pruner using the median stopping rule.      Prune if the trial's best intermedia, _get_best_intermediate_result_over_steps(), _get_percentile_intermediate_result_over_trials(), _is_first_in_interval_step(), PercentilePruner, Pruner to keep the specified percentile of the trials.      Prune if the best in

### Community 56 - "Community 56"
Cohesion: 0.21
Nodes (1): QMCSampler

### Community 57 - "Community 57"
Cohesion: 0.29
Nodes (6): _get_unnormalized_param(), _normalize_one_param(), _round_one_normalized_param(), _sample_normalized_params(), SearchSpace, _unnormalize_one_param()

### Community 58 - "Community 58"
Cohesion: 0.23
Nodes (10): _associate_individuals_with_reference_points(), _filter_inf(), _generate_default_reference_point(), _normalize_objective_values(), _preserve_niche_individuals(), Generates default reference points which are `uniformly` spread on a hyperplane., Normalizes objective values of population.      An ideal point z* consists of mi, Associates each objective value to the closest reference point.      Associate e (+2 more)

### Community 59 - "Community 59"
Cohesion: 0.30
Nodes (11): _generate_slice_subplot(), _get_categorical_labels(), _get_categorical_plot_values(), _get_slice_plot(), _get_slice_plot_info(), _get_slice_subplot_info(), plot_slice(), _PlotValues (+3 more)

### Community 60 - "Community 60"
Cohesion: 0.20
Nodes (5): ArtifactNotFound, Exception raised when an artifact is not found.      It is typically raised whil, GCSArtifactStore, An artifact backend for Google Cloud Storage (GCS).      Args:         bucket_na, OptunaError

### Community 61 - "Community 61"
Cohesion: 0.18
Nodes (2): BaseGASampler, NSGAIISampler

### Community 62 - "Community 62"
Cohesion: 0.18
Nodes (6): _BaseCommand, _DeleteStudy, Base class for commands.      Note that command classes are not intended to be c, Add arguments required for each command.          Args:             parser:, Define action if the command is called.          Args:             parsed_args:, Delete a specified study.

### Community 63 - "Community 63"
Cohesion: 0.22
Nodes (5): ConstrainedLogEHVI, ConstrainedLogEI, LogPI, ConditionalGPRegressor, Gaussian process regressor conditioned on a fixed set of samples.      We first

### Community 64 - "Community 64"
Cohesion: 0.18
Nodes (7): _extend_cholesky(), Matern52Kernel, Notations in this Gaussian process implementation  X_train: Observed parameter v, This method calculates `exp(-sqrt5d) * (1/3 * sqrt5d ** 2 + sqrt5d + 1)` where, Let x be squared_distance, f(x) be forward(ctx, x), and g(f) be a provided funct, # TODO: Move this function into a method of `GPRegressor`, This function calculates the Cholesky decompsition L of K=[[K11,K12],[K21,K22]]

### Community 65 - "Community 65"
Cohesion: 0.24
Nodes (7): _ParzenEstimator, build_parzen_estimator_on_grid(), _count_categorical_param_in_grid(), _count_numerical_param_in_grid(), 1D ParzenEstimator using the bandwidth selection by Scott's rule., # NOTE: The Optuna TPE bandwidth selection is too wide for this analysis., ScottParzenEstimator

### Community 66 - "Community 66"
Cohesion: 0.20
Nodes (6): Return the list of retried trial numbers with respect to the specified trial., Deprecated alias of :class:`~optuna.storages.RetryHeartbeatStaleTrialCallback`., Retry a heartbeat-stale trial up to a maximum number of times.      When a runni, Return the number of the original trial being retried.          Args:, RetryFailedTrialCallback, RetryHeartbeatStaleTrialCallback

### Community 67 - "Community 67"
Cohesion: 0.31
Nodes (1): _ParzenEstimator

### Community 68 - "Community 68"
Cohesion: 0.20
Nodes (6): ArtifactStore, A protocol defining the interface for an artifact backend.      The methods defi, Open the artifact identified by the artifact_id.          This method should ret, Save the content to the backend.          Args:             artifact_id: The ide, Remove the artifact identified by the artifact_id.          This method should d, Protocol

### Community 69 - "Community 69"
Cohesion: 0.36
Nodes (8): BaseModel, empty message  Revision ID: v2.4.0.a Revises: v1.3.0.a Create Date: 2020-11-17 0, StudyDirectionModel, StudyModel, TrialIntermediateValueModel, TrialModel, TrialValueModel, upgrade()

### Community 70 - "Community 70"
Cohesion: 0.20
Nodes (6): _Ask, _BestTrials, _dump_value(), _format_output(), Show a list of trials located at the Pareto front., Create a new trial and suggest parameters.

### Community 71 - "Community 71"
Cohesion: 0.33
Nodes (9): _discrete_line_search(), _exhaustive_search(), _gradient_ascent_batched(), _local_search_discrete(), _local_search_discrete_batched(), local_search_mixed_batched(), optimize_acqf_mixed(), # NOTE: Ideally, separating lengthscales should be used for the constraint funct (+1 more)

### Community 72 - "Community 72"
Cohesion: 0.22
Nodes (5): _IntegrationModule, Module class that implements `optuna.integration` package.          This class a, _LightGBMModule, Module class that implements `optuna.integration.lightgbm` package., ModuleType

### Community 73 - "Community 73"
Cohesion: 0.20
Nodes (1): NSGAIIISampler

### Community 74 - "Community 74"
Cohesion: 0.20
Nodes (2): PartialFixedSampler, Sampler with partially fixed parameters.      Example:          After several st

### Community 75 - "Community 75"
Cohesion: 0.20
Nodes (5): Read whether a study maximizes or minimizes an objective.          Args:, Read the trial ID of a trial.          Args:             study_id:, Read all trials in a study.          Args:             study_id:, Count the number of trials in a study.          Args:             study_id:, Return the trial with the best value in a study.          This method is valid o

### Community 76 - "Community 76"
Cohesion: 0.36
Nodes (9): _get_distribution(), _get_hover_template(), _get_importances_info(), _get_importances_infos(), _get_importances_plot(), _ImportancesInfo, _make_hovertext(), plot_param_importances() (+1 more)

### Community 77 - "Community 77"
Cohesion: 0.33
Nodes (8): _get_non_pareto_front_trials(), _get_pareto_front_info(), _get_pareto_front_plot(), _make_marker(), _make_scatter_object(), _ParetoFrontInfo, plot_pareto_front(), Plot the Pareto front of a study.      .. seealso::         Please refer to :ref

### Community 78 - "Community 78"
Cohesion: 0.36
Nodes (9): _get_max_datetime_complete(), _get_timeline_info(), _get_timeline_plot(), _is_running_trials_in_study(), _plot_bars(), plot_timeline(), Plot the timeline of a study.      Args:         study:             A :class:`~o, _TimelineBarInfo (+1 more)

### Community 79 - "Community 79"
Cohesion: 0.22
Nodes (4): _get_skipped_trial_numbers(), is_available(), _make_hovertext(), _make_json_compatible()

### Community 80 - "Community 80"
Cohesion: 0.28
Nodes (2): GrpcClientCache, GrpcClientCacheEntry

### Community 81 - "Community 81"
Cohesion: 0.33
Nodes (8): _compute_2d(), _compute_3d(), _compute_exclusive_hv(), _compute_hv(), compute_hypervolume(), Hypervolume calculator for any dimension.      This class exactly calculates the, Compute hypervolume in 3D. Time complexity is O(N^2) where N is sorted_pareto_so, # NOTE: For 3D points, we always prefer _compute_3d to _compute_hv because the t

### Community 82 - "Community 82"
Cohesion: 0.31
Nodes (6): _calc_crowding_distance(), _crowding_distance_sort(), NSGAIIElitePopulationSelectionStrategy, _rank_population(), Select elite population from the given trials by NSGA-II algorithm.          Arg, Calculates the crowding distance of population.      We define the crowding dist

### Community 83 - "Community 83"
Cohesion: 0.25
Nodes (4): _ProgressBar, Progress Bar implementation for :func:`~optuna.study.Study.optimize` on the top, Update the progress bars if ``is_valid`` is :obj:`True`.          Args:, _TqdmLoggingHandler

### Community 84 - "Community 84"
Cohesion: 0.28
Nodes (6): _calculate(), intersection_search_space(), IntersectionSearchSpace, Return the intersection search space of the given trials.      Intersection sear, A class to calculate the intersection search space of a :class:`~optuna.study.St, Returns the intersection search space of the :class:`~optuna.study.Study`.

### Community 85 - "Community 85"
Cohesion: 0.39
Nodes (8): _DimensionInfo, _get_dims_from_info(), _get_parallel_coordinate_info(), _get_parallel_coordinate_plot(), _ParallelCoordinateInfo, plot_parallel_coordinate(), Plot the high-dimensional parameter relationships in a study.      Note that, if, _truncate_label()

### Community 86 - "Community 86"
Cohesion: 0.39
Nodes (8): _get_error_scatter(), _get_improvement_info(), _get_improvement_plot(), _get_improvement_scatter(), _get_y_range(), _ImprovementInfo, plot_terminator_improvement(), Plot the potentials for future objective improvement.      This function visuali

### Community 87 - "Community 87"
Cohesion: 0.36
Nodes (2): Backoff, An artifact store's middleware for exponential backoff.      Example:        ..

### Community 88 - "Community 88"
Cohesion: 0.29
Nodes (3): Boto3ArtifactStore, _is_not_found_error(), An artifact backend for Boto3.      Args:         bucket_name:             The n

### Community 89 - "Community 89"
Cohesion: 0.36
Nodes (2): FileSystemArtifactStore, An artifact store for file systems.      Args:         base_path:             Th

### Community 90 - "Community 90"
Cohesion: 0.29
Nodes (6): get_all_artifact_meta(), List the associated artifact information of the provided trial or study.      Ar, ArtifactMeta, Meta information for an artifact.      .. note::         All the artifact meta l, Upload an artifact to the artifact store.      Args:         artifact_store:, upload_artifact()

### Community 91 - "Community 91"
Cohesion: 0.36
Nodes (5): BaseImprovementEvaluator, _compute_gp_posterior(), _compute_gp_posterior_cov_two_thetas(), EMMREvaluator, Evaluates a kind of regrets, called the Expected Minimum Model Regret(EMMR).

### Community 92 - "Community 92"
Cohesion: 0.25
Nodes (5): _check_storage_url(), _CreateStudy, _get_storage(), Upgrade the schema of an RDB storage., _StorageUpgrade

### Community 93 - "Community 93"
Cohesion: 0.39
Nodes (2): Unimodal Normal Distribution Crossover used by :class:`~optuna.samplers.NSGAIISa, UNDXCrossover

### Community 94 - "Community 94"
Cohesion: 0.29
Nodes (2): _check_evaluate_args(), _get_distributions()

### Community 95 - "Community 95"
Cohesion: 0.43
Nodes (7): NamedTuple, _get_intermediate_plot(), _get_intermediate_plot_info(), _IntermediatePlotInfo, plot_intermediate_values(), Plot intermediate values of all trials in a study.      Args:         study:, _TrialInfo

### Community 96 - "Community 96"
Cohesion: 0.32
Nodes (2): _GroupDecomposedSearchSpace, _SearchSpaceGroup

### Community 97 - "Community 97"
Cohesion: 0.29
Nodes (4): Handle inf/-inf for trial_values table.  Revision ID: v3.0.0.d Revises: v3.0.0.c, TrialValueModel, TrialValueType, upgrade()

### Community 98 - "Community 98"
Cohesion: 0.29
Nodes (4): *     Optuna storage service defines APIs to interact with the storage., Constructor.          Args:             channel: A grpc.Channel., StorageServiceStub, object

### Community 99 - "Community 99"
Cohesion: 0.29
Nodes (4): BaseCrossover, Base class for crossovers.      A crossover operation is used by :class:`~optuna, Number of parent individuals required to perform crossover., Perform crossover of selected parent individuals.          This method is called

### Community 100 - "Community 100"
Cohesion: 0.33
Nodes (2): _Fanova, An implementation of `An Efficient Approach for Assessing Hyperparameter Importa

### Community 101 - "Community 101"
Cohesion: 0.43
Nodes (6): _lazy_contribs_update(), Solve a hypervolume subset selection problem (HSSP) via a greedy algorithm., Lazy update the hypervolume contributions.      (1) Lazy update of the hypervolu, _solve_hssp(), _solve_hssp_2d(), _solve_hssp_on_unique_loss_vals()

### Community 102 - "Community 102"
Cohesion: 0.48
Nodes (6): _calc_lim_with_padding(), _generate_slice_subplot(), _get_categorical_plot_values(), _get_slice_plot(), plot_slice(), Plot the parameter relationship as slice plot in a study with Matplotlib.      .

### Community 103 - "Community 103"
Cohesion: 0.29
Nodes (3): NSGAIIChildGenerationStrategy, NSGAIIIElitePopulationSelectionStrategy, Multi-objective sampler using the NSGA-III algorithm.      NSGA-III stands for "

### Community 104 - "Community 104"
Cohesion: 0.52
Nodes (6): _inlined_categorical_uniform_crossover(), _is_contained(), perform_crossover(), _select_parent(), _select_parents(), _try_crossover()

### Community 105 - "Community 105"
Cohesion: 0.52
Nodes (5): _completed_rung_key(), _estimate_min_resource(), _get_competing_values(), _get_current_rung(), _is_trial_promotable_to_next_rung()

### Community 106 - "Community 106"
Cohesion: 0.29
Nodes (1): RandomSampler

### Community 108 - "Community 108"
Cohesion: 0.29
Nodes (4): Change floating point precision and make intermediate_value nullable.  Revision, TrialModel, TrialState, TrialValueModel

### Community 109 - "Community 109"
Cohesion: 0.33
Nodes (4): IntermediateValueModel, Add intermediate_value_type column to represent +inf and -inf  Revision ID: v3.0, TrialIntermediateValueType, upgrade()

### Community 110 - "Community 110"
Cohesion: 0.33
Nodes (3): BaseErrorEvaluator, MedianErrorEvaluator, An error evaluator that returns the ratio to initial median.      This error eva

### Community 111 - "Community 111"
Cohesion: 0.33
Nodes (3): BaseMutation, PolynomialMutation, Polynomial mutation operation used by :class:`~optuna.samplers.NSGAIISampler`.

### Community 112 - "Community 112"
Cohesion: 0.47
Nodes (2): CellValue, _dump_table()

### Community 113 - "Community 113"
Cohesion: 0.47
Nodes (5): _get_box_bounds(), _get_non_dominated_box_bounds(), _get_upper_bound_set(), The functions in this file are mostly based on BoTorch v0.13.0, but they are ref, This function follows Algorithm 2 of Lacour17.      Args:         sorted_pareto_

### Community 114 - "Community 114"
Cohesion: 0.53
Nodes (5): _get_pareto_front_2d(), _get_pareto_front_3d(), _get_pareto_front_plot(), plot_pareto_front(), Plot the Pareto front of a study.      .. seealso::         Please refer to :fun

### Community 115 - "Community 115"
Cohesion: 0.33
Nodes (3): NSGAIIAfterTrialStrategy, Carry out the after trial process of default NSGA-II.          This method is ca, Multi-objective sampler using the NSGA-II algorithm.      NSGA-II stands for "No

### Community 116 - "Community 116"
Cohesion: 0.33
Nodes (4): _constrained_dominates(), _evaluate_penalty(), Checks constrained-domination.      A trial x is said to constrained-dominate a, Evaluate feasibility of trials in population.     Returns:         A list of fea

### Community 117 - "Community 117"
Cohesion: 0.40
Nodes (3): _check_value(), Pruner to detect outlying metrics of the trials.      Prune if a metric exceeds, ThresholdPruner

### Community 118 - "Community 118"
Cohesion: 0.40
Nodes (1): TrialModel

### Community 119 - "Community 119"
Cohesion: 0.33
Nodes (4): _get_feasible_trials(), _is_constrained_optimization(), Return whether the given trials are created in constrained optimization., Return feasible trials from given trials.      This function assumes that the tr

### Community 120 - "Community 120"
Cohesion: 0.53
Nodes (5): _check_state_and_values(), _check_values_are_feasible(), _get_frozen_trial(), Internal method of :func:`~optuna.study.Study.tell`.      Refer to the document, _tell_with_warning()

### Community 121 - "Community 121"
Cohesion: 0.33
Nodes (1): DeterministicSampler

### Community 122 - "Community 122"
Cohesion: 0.40
Nodes (4): downgrade(), empty message  Revision ID: v1.3.0.a Revises: v1.2.0.a Create Date: 2020-02-14 1, TrialModel, TrialSystemAttributeModel

### Community 123 - "Community 123"
Cohesion: 0.53
Nodes (5): _EDFInfo, _EDFLineInfo, _get_edf_info(), plot_edf(), Plot the objective value EDF (empirical distribution function) of a study.

### Community 124 - "Community 124"
Cohesion: 0.53
Nodes (5): _get_hypervolume_history_info(), _get_hypervolume_history_plot(), _HypervolumeHistoryInfo, plot_hypervolume_history(), Plot hypervolume history of all trials in a study.      Args:         study:

### Community 125 - "Community 125"
Cohesion: 0.40
Nodes (2): MaxTrialsCallback, Set a maximum number of trials before ending the study.      While the ``n_trial

### Community 126 - "Community 126"
Cohesion: 0.40
Nodes (2): Uniform Crossover operation used by :class:`~optuna.samplers.NSGAIISampler`., UniformCrossover

### Community 127 - "Community 127"
Cohesion: 0.40
Nodes (3): logei(), Return E_{x ~ N(0, 1)}[max(0, x+z)]     The calculation depends on the value of, standard_logei()

### Community 128 - "Community 128"
Cohesion: 0.60
Nodes (4): _get_importances_plot(), plot_param_importances(), Plot hyperparameter importances (:class:`~optuna.importance.PedAnovaImportanceEv, _set_bar_labels()

### Community 129 - "Community 129"
Cohesion: 0.60
Nodes (4): _add_rank_subplot(), _get_rank_plot(), plot_rank(), Plot parameter relations as scatter plots with colors indicating ranks of target

### Community 130 - "Community 130"
Cohesion: 0.60
Nodes (4): _get_state_name(), _get_timeline_plot(), plot_timeline(), Plot the timeline of a study.      .. seealso::         Please refer to :func:`o

### Community 131 - "Community 131"
Cohesion: 0.40
Nodes (1): is_available()

### Community 132 - "Community 132"
Cohesion: 0.40
Nodes (3): BaseMutation, Base class for mutations.      A mutation operation is used by :class:`~optuna.s, Mutate the given parameter.          Args:             param:                 A

### Community 133 - "Community 133"
Cohesion: 0.40
Nodes (2): PatientPruner, Pruner which wraps another pruner with tolerance.      This pruner monitors inte

### Community 134 - "Community 134"
Cohesion: 0.40
Nodes (2): Pruner based on the `Wilcoxon signed-rank test <https://en.wikipedia.org/w/index, WilcoxonPruner

### Community 135 - "Community 135"
Cohesion: 0.40
Nodes (1): TrialIntermediateValueModel

### Community 136 - "Community 136"
Cohesion: 0.40
Nodes (1): TrialValueModel

### Community 137 - "Community 137"
Cohesion: 0.40
Nodes (1): _TestableThread

### Community 138 - "Community 138"
Cohesion: 0.40
Nodes (1): _BatchedTruncLogNormDistributions

### Community 139 - "Community 139"
Cohesion: 0.40
Nodes (1): _BatchedTruncNormDistributions

### Community 140 - "Community 140"
Cohesion: 0.50
Nodes (2): Set a user attribute to a study., _StudySetUserAttribute

### Community 141 - "Community 141"
Cohesion: 0.50
Nodes (2): Get all study names stored in a specified storage, _StudyNames

### Community 142 - "Community 142"
Cohesion: 0.50
Nodes (2): Show a list of studies., _Studies

### Community 143 - "Community 143"
Cohesion: 0.50
Nodes (2): Show a list of trials., _Trials

### Community 144 - "Community 144"
Cohesion: 0.50
Nodes (2): Finish a trial, which was created by the ask command., _Tell

### Community 145 - "Community 145"
Cohesion: 0.67
Nodes (3): make_server(), Run a gRPC server for the given storage URL, host, and port.      Example:, run_grpc_proxy_server()

### Community 146 - "Community 146"
Cohesion: 0.67
Nodes (3): _get_hypervolume_history_plot(), plot_hypervolume_history(), Plot hypervolume history of all trials in a study with Matplotlib.      .. note:

### Community 147 - "Community 147"
Cohesion: 0.67
Nodes (3): _get_intermediate_plot(), plot_intermediate_values(), Plot intermediate values of all trials in a study with Matplotlib.      .. seeal

### Community 148 - "Community 148"
Cohesion: 0.67
Nodes (3): _get_optimization_history_plot(), plot_optimization_history(), Plot optimization history of all trials in a study with Matplotlib.      .. seea

### Community 149 - "Community 149"
Cohesion: 0.67
Nodes (3): _get_parallel_coordinate_plot(), plot_parallel_coordinate(), Plot the high-dimensional parameter relationships in a study with Matplotlib.

### Community 150 - "Community 150"
Cohesion: 0.67
Nodes (3): _get_improvement_plot(), plot_terminator_improvement(), Plot the potentials for future objective improvement.      This function visuali

### Community 151 - "Community 151"
Cohesion: 0.50
Nodes (3): BasePruner, Base class for pruners., Judge whether the trial should be pruned based on the reported values.

### Community 152 - "Community 152"
Cohesion: 0.67
Nodes (1): TrialParamModel

### Community 153 - "Community 153"
Cohesion: 0.50
Nodes (2): Get the heartbeat-stale trial callback function.          Returns:             T, Get the failed trial callback function.

### Community 154 - "Community 154"
Cohesion: 0.83
Nodes (3): _create_records_and_aggregate_column(), _flatten_columns(), _trials_dataframe()

### Community 155 - "Community 155"
Cohesion: 0.50
Nodes (1): DeterministicPruner

### Community 156 - "Community 156"
Cohesion: 0.50
Nodes (1): empty message  Revision ID: v0.9.0.a Revises: Create Date: 2019-03-12 12:30:31.1

### Community 157 - "Community 157"
Cohesion: 0.50
Nodes (1): empty message  Revision ID: v1.2.0.a Revises: v0.9.0.a Create Date: 2020-02-05 1

### Community 158 - "Community 158"
Cohesion: 0.50
Nodes (1): empty message  Revision ID: v2.6.0.a Revises: v2.4.0.a Create Date: 2021-03-01 1

### Community 159 - "Community 159"
Cohesion: 0.50
Nodes (1): Add index to study_id column in trials table  Revision ID: v3.2.0.a Revises: v3.

### Community 160 - "Community 160"
Cohesion: 0.67
Nodes (2): download_artifact(), Download an artifact from the artifact store.      Args:         artifact_store:

### Community 161 - "Community 161"
Cohesion: 0.67
Nodes (1): _BestTrial

### Community 162 - "Community 162"
Cohesion: 0.67
Nodes (1): qLogEI

### Community 163 - "Community 163"
Cohesion: 0.67
Nodes (2): _batched_lbfgsb(), Batched L-BFGS-B optimization with/without greenlet.     - `func_and_grad` is ex

### Community 164 - "Community 164"
Cohesion: 0.67
Nodes (2): limit_threads_in_optimization(), Context manager to limit threading to resolve a thread oversubscription issue.

### Community 165 - "Community 165"
Cohesion: 0.67
Nodes (2): plot_edf(), Plot the objective value EDF (empirical distribution function) of a study with M

### Community 166 - "Community 166"
Cohesion: 0.67
Nodes (1): TrialSystemAttributeModel

### Community 167 - "Community 167"
Cohesion: 0.67
Nodes (1): TrialUserAttributeModel

### Community 169 - "Community 169"
Cohesion: 0.67
Nodes (2): prepare_study_with_trials(), Return a dummy study object for tests.      This function is added to reduce the

### Community 170 - "Community 170"
Cohesion: 1.00
Nodes (2): erf(), _erf_right_non_big()

### Community 171 - "Community 171"
Cohesion: 1.00
Nodes (1): *         Get study user attributes.

### Community 172 - "Community 172"
Cohesion: 1.00
Nodes (1): *         Get study system attributes.

### Community 173 - "Community 173"
Cohesion: 1.00
Nodes (1): *         Get all studies.

### Community 174 - "Community 174"
Cohesion: 1.00
Nodes (1): *         Create a new trial.

### Community 175 - "Community 175"
Cohesion: 1.00
Nodes (1): *         Set a trial parameter.

### Community 176 - "Community 176"
Cohesion: 1.00
Nodes (1): *         Get a trial id from its study id and trial number.

### Community 177 - "Community 177"
Cohesion: 1.00
Nodes (1): *         Set trial state and values.

### Community 178 - "Community 178"
Cohesion: 1.00
Nodes (1): *         Set a trial intermediate value.

### Community 179 - "Community 179"
Cohesion: 1.00
Nodes (1): *         Set a trial user attribute.

### Community 180 - "Community 180"
Cohesion: 1.00
Nodes (1): *         Set a trial system attribute.

### Community 181 - "Community 181"
Cohesion: 1.00
Nodes (1): *         Get a trial by its ID.

## Knowledge Gaps
- **171 isolated node(s):** `Convert positional arguments to keyword arguments.      Args:         previous_p`, `Decorate function as deprecated.      Args:         deprecated_version:`, `Decorate class as deprecated.      Args:         deprecated_version:`, `Decorate function as experimental.      Args:         version: The first version`, `Decorate class as experimental.      Args:         version: The first version th` (+166 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 5`** (2 nodes): `JournalStorage`, `JournalStorageReplayResult`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 9`** (2 nodes): `InMemoryStorage`, `_StudyInfo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 10`** (2 nodes): `_CachedStorage`, `_StudyInfo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (2 nodes): `ABC`, `# NOTE: ei(z) = z * cdf(z) + pdf(z)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (2 nodes): `create_trial()`, `FrozenTrial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (2 nodes): `BaseTrial`, `FixedTrial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (2 nodes): `*     Optuna storage service defines APIs to interact with the storage.`, `StorageService`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (2 nodes): `BaseTrial`, `Base class for trials.      Note that this class is not supposed to be directly`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (2 nodes): `CmaEsSampler`, `_is_compatible_search_space()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 49`** (1 nodes): `GridSampler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (1 nodes): `QMCSampler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (2 nodes): `BaseGASampler`, `NSGAIISampler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 67`** (1 nodes): `_ParzenEstimator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 73`** (1 nodes): `NSGAIIISampler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 74`** (2 nodes): `PartialFixedSampler`, `Sampler with partially fixed parameters.      Example:          After several st`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 80`** (2 nodes): `GrpcClientCache`, `GrpcClientCacheEntry`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 87`** (2 nodes): `Backoff`, `An artifact store's middleware for exponential backoff.      Example:        ..`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 89`** (2 nodes): `FileSystemArtifactStore`, `An artifact store for file systems.      Args:         base_path:             Th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 93`** (2 nodes): `Unimodal Normal Distribution Crossover used by :class:`~optuna.samplers.NSGAIISa`, `UNDXCrossover`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 94`** (2 nodes): `_check_evaluate_args()`, `_get_distributions()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 96`** (2 nodes): `_GroupDecomposedSearchSpace`, `_SearchSpaceGroup`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 100`** (2 nodes): `_Fanova`, `An implementation of `An Efficient Approach for Assessing Hyperparameter Importa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 106`** (1 nodes): `RandomSampler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 112`** (2 nodes): `CellValue`, `_dump_table()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 118`** (1 nodes): `TrialModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 121`** (1 nodes): `DeterministicSampler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 125`** (2 nodes): `MaxTrialsCallback`, `Set a maximum number of trials before ending the study.      While the ``n_trial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 126`** (2 nodes): `Uniform Crossover operation used by :class:`~optuna.samplers.NSGAIISampler`.`, `UniformCrossover`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 131`** (1 nodes): `is_available()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 133`** (2 nodes): `PatientPruner`, `Pruner which wraps another pruner with tolerance.      This pruner monitors inte`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 134`** (2 nodes): `Pruner based on the `Wilcoxon signed-rank test <https://en.wikipedia.org/w/index`, `WilcoxonPruner`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 135`** (1 nodes): `TrialIntermediateValueModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 136`** (1 nodes): `TrialValueModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 137`** (1 nodes): `_TestableThread`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 138`** (1 nodes): `_BatchedTruncLogNormDistributions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 139`** (1 nodes): `_BatchedTruncNormDistributions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 140`** (2 nodes): `Set a user attribute to a study.`, `_StudySetUserAttribute`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 141`** (2 nodes): `Get all study names stored in a specified storage`, `_StudyNames`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 142`** (2 nodes): `Show a list of studies.`, `_Studies`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 143`** (2 nodes): `Show a list of trials.`, `_Trials`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 144`** (2 nodes): `Finish a trial, which was created by the ask command.`, `_Tell`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 152`** (1 nodes): `TrialParamModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 153`** (2 nodes): `Get the heartbeat-stale trial callback function.          Returns:             T`, `Get the failed trial callback function.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 155`** (1 nodes): `DeterministicPruner`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 156`** (1 nodes): `empty message  Revision ID: v0.9.0.a Revises: Create Date: 2019-03-12 12:30:31.1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 157`** (1 nodes): `empty message  Revision ID: v1.2.0.a Revises: v0.9.0.a Create Date: 2020-02-05 1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 158`** (1 nodes): `empty message  Revision ID: v2.6.0.a Revises: v2.4.0.a Create Date: 2021-03-01 1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 159`** (1 nodes): `Add index to study_id column in trials table  Revision ID: v3.2.0.a Revises: v3.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 160`** (2 nodes): `download_artifact()`, `Download an artifact from the artifact store.      Args:         artifact_store:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 161`** (1 nodes): `_BestTrial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 162`** (1 nodes): `qLogEI`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 163`** (2 nodes): `_batched_lbfgsb()`, `Batched L-BFGS-B optimization with/without greenlet.     - `func_and_grad` is ex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 164`** (2 nodes): `limit_threads_in_optimization()`, `Context manager to limit threading to resolve a thread oversubscription issue.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 165`** (2 nodes): `plot_edf()`, `Plot the objective value EDF (empirical distribution function) of a study with M`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 166`** (1 nodes): `TrialSystemAttributeModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 167`** (1 nodes): `TrialUserAttributeModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 169`** (2 nodes): `prepare_study_with_trials()`, `Return a dummy study object for tests.      This function is added to reduce the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 170`** (2 nodes): `erf()`, `_erf_right_non_big()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 171`** (1 nodes): `*         Get study user attributes.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 172`** (1 nodes): `*         Get study system attributes.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 173`** (1 nodes): `*         Get all studies.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 174`** (1 nodes): `*         Create a new trial.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 175`** (1 nodes): `*         Set a trial parameter.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 176`** (1 nodes): `*         Get a trial id from its study id and trial number.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 177`** (1 nodes): `*         Set trial state and values.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 178`** (1 nodes): `*         Set a trial intermediate value.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 179`** (1 nodes): `*         Set a trial user attribute.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 180`** (1 nodes): `*         Set a trial system attribute.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 181`** (1 nodes): `*         Get a trial by its ID.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Study` connect `Community 0` to `Community 90`, `Community 125`, `Community 99`, `Community 28`, `Community 93`, `Community 126`, `Community 15`, `Community 43`, `Community 8`, `Community 4`, `Community 38`, `Community 165`, `Community 146`, `Community 147`, `Community 148`, `Community 149`, `Community 128`, `Community 114`, `Community 129`, `Community 102`, `Community 150`, `Community 130`, `Community 132`, `Community 111`, `Community 115`, `Community 103`, `Community 82`, `Community 61`, `Community 58`, `Community 73`, `Community 83`, `Community 117`, `Community 44`, `Community 29`, `Community 49`, `Community 74`, `Community 56`, `Community 2`, `Community 106`, `Community 96`, `Community 84`, `Community 39`, `Community 13`, `Community 16`, `Community 14`, `Community 11`, `Community 19`, `Community 52`, `Community 123`, `Community 124`, `Community 95`, `Community 53`, `Community 85`, `Community 76`, `Community 77`, `Community 47`, `Community 59`, `Community 86`, `Community 78`?**
  _High betweenness centrality (0.217) - this node is a cross-community bridge._
- **Why does `BaseDistribution` connect `Community 4` to `Community 6`, `Community 2`, `Community 8`, `Community 57`, `Community 80`, `Community 12`, `Community 15`, `Community 13`, `Community 5`, `Community 103`, `Community 61`, `Community 115`, `Community 73`, `Community 65`, `Community 44`, `Community 29`, `Community 34`, `Community 49`, `Community 74`, `Community 56`, `Community 106`, `Community 96`, `Community 84`, `Community 18`, `Community 75`, `Community 50`, `Community 0`, `Community 39`, `Community 26`, `Community 14`, `Community 121`, `Community 67`, `Community 11`, `Community 51`, `Community 30`, `Community 25`, `Community 21`, `Community 19`, `Community 76`?**
  _High betweenness centrality (0.169) - this node is a cross-community bridge._
- **Why does `StudyDirection` connect `Community 13` to `Community 80`, `Community 12`, `Community 22`, `Community 5`, `Community 133`, `Community 55`, `Community 31`, `Community 134`, `Community 33`, `Community 135`, `Community 118`, `Community 152`, `Community 166`, `Community 167`, `Community 136`, `Community 1`, `Community 34`, `Community 4`, `Community 18`, `Community 75`, `Community 50`, `Community 10`, `Community 9`, `Community 46`, `Community 53`, `Community 0`, `Community 39`, `Community 3`, `Community 11`, `Community 124`, `Community 2`?**
  _High betweenness centrality (0.163) - this node is a cross-community bridge._
- **Are the 193 inferred relationships involving `Study` (e.g. with `List the associated artifact information of the provided trial or study.      Ar` and `ArtifactMeta`) actually correct?**
  _`Study` has 193 INFERRED edges - model-reasoned connections that need verification._
- **Are the 194 inferred relationships involving `BaseDistribution` (e.g. with `GPSampler` and `Sampler using Gaussian process-based Bayesian optimization.      .. note::`) actually correct?**
  _`BaseDistribution` has 194 INFERRED edges - model-reasoned connections that need verification._
- **Are the 137 inferred relationships involving `StudyDirection` (e.g. with `GrpcClientCache` and `GrpcClientCacheEntry`) actually correct?**
  _`StudyDirection` has 137 INFERRED edges - model-reasoned connections that need verification._
- **Are the 76 inferred relationships involving `FloatDistribution` (e.g. with `# TODO: Make it an index array.` and `_ScaleType`) actually correct?**
  _`FloatDistribution` has 76 INFERRED edges - model-reasoned connections that need verification._