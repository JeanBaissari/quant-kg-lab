# Graph Report - knowledge_graphs/pymc/repo/pymc  (2026-08-13)

## Corpus Check
- 128 files · ~222,789 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 4067 nodes · 11144 edges · 156 communities detected
- Non-singleton communities: 140
- Extraction: EXTRACTED: 46.9% · INFERRED: 53.1%
- Edge kinds: calls: 916 · contains: 1195 · imports: 3 · imports_from: 11 · inherits: 466 · method: 1478 · rationale_for: 1163 · uses: 5912

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 128 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `47bdf54`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `SymbolicRandomVariable` (339)
- `DictToArrayBijection` (319)
- `MeasurableOp` (234)
- `MinibatchOp` (206)
- `Distribution` (186)
- `Continuous` (170)
- `MultiTrace` (168)
- `RaveledVars` (150)
- `MeasurableElemwise` (137)
- `BlockModelAccessError` (122)

## Surprising Connections (you probably didn't know these)
- `Bundle warnings, convergence stats and metadata of a sampling run.` --uses--> `SamplerWarning`  [INFERRED]
  backends/report.py → stats/convergence.py
- `Whether the automatic convergence checks found serious problems.` --uses--> `SamplerWarning`  [INFERRED]
  backends/report.py → stats/convergence.py
- `Number of tune iterations - not necessarily kept in trace.` --uses--> `SamplerWarning`  [INFERRED]
  backends/report.py → stats/convergence.py
- `Number of draw iterations.` --uses--> `SamplerWarning`  [INFERRED]
  backends/report.py → stats/convergence.py
- `Number of seconds that the sampling procedure took.          (Includes paralleli` --uses--> `SamplerWarning`  [INFERRED]
  backends/report.py → stats/convergence.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.04
Nodes (97): BoundedContinuous, Whether a censoring bound is an infinite constant, and thus not censoring at all, r"""     Censored distribution.      The pdf of a censored distribution is, BoundedContinuous, Base class for bounded continuous distributions., DiscreteWeibullRV, R"""Discrete uniform distribution.      The pmf of this distribution is      .., R"""     Categorical distribution.      The most general discrete distribution. (+89 more)

### Community 1 - "Community 1"
Cohesion: 0.02
Nodes (66): Continuous, AsymmetricLaplace, Cauchy, ChiSquared, CircularContinuous, ExGaussian, Exponential, Flat (+58 more)

### Community 2 - "Community 2"
Cohesion: 0.02
Nodes (63): I0e, I1e, Modified Bessel function of the first kind of order 1, exponentially scaled., Modified Bessel function of the first kind of order 0, exponentially scaled., AbsTransform, ArccoshTransform, ArccosTransform, ArcsinhTransform (+55 more)

### Community 3 - "Community 3"
Cohesion: 0.07
Nodes (39): Gamma, LogNormal, Binomial, NegativeBinomial, Poisson, DiracDelta, partial_observed_rv_logprob(), r"""     DiracDelta distribution.      Parameters     ----------     c : tensor_ (+31 more)

### Community 4 - "Community 4"
Cohesion: 0.05
Nodes (41): BaseCovariance, Constant, Allow radd/rmul by numpy arrays., r"""     Constant valued covariance function.      .. math::         k(x, x') =, Base class for kernels/covariance functions., r"""         Evaluate the kernel/covariance function.          Parameters, Latent, LatentKron (+33 more)

### Community 5 - "Community 5"
Cohesion: 0.05
Nodes (59): DataClassState, ExpWeightedVarianceState, isquadpotential(), partial_check_positive_definite(), PositiveDefiniteError, PotentialState, quad_potential(), QuadPotentialDiag (+51 more)

### Community 6 - "Community 6"
Cohesion: 0.06
Nodes (76): Alloc, DeepCopyOp, Elemwise, Join, JoinDims, MeasurableElemwise, Base class for Measurable Elemwise variables., Return a string representation of the object. (+68 more)

### Community 7 - "Community 7"
Cohesion: 0.06
Nodes (40): Distribution, CensoredRV, Censored random variable., Normal, CustomSymbolicDistRV, Base class for CustomSymbolicDist.      This should be subclassed when defining, Distribution, Statistical distribution. (+32 more)

### Community 8 - "Community 8"
Cohesion: 0.04
Nodes (38): BetaRV, AsymmetricLaplaceRV, BetaClippedRV, bounded_cont_transform(), ExGaussianRV, FlatRV, HalfFlatRV, _interpolated_argcdf() (+30 more)

### Community 9 - "Community 9"
Cohesion: 0.04
Nodes (53): ABCMeta, CumOp, __init__(), Make PyMC aware of the xtensor functionality., DimShuffle, Base class for PyMC distribution that wrap pytensor.xtensor.random operations, a, # TODO: If this fails give a more informative error message, Base class for positive continuous distributions. (+45 more)

### Community 10 - "Community 10"
Cohesion: 0.09
Nodes (34): DimDistribution, Beta, HalfCauchyRV, HalfStudentTRV, WeibullBetaRV, DimDistribution, PositiveDimDistribution, UnitDimDistribution (+26 more)

### Community 11 - "Community 11"
Cohesion: 0.04
Nodes (52): dict, BlockModelAccessError, list, chains_and_samples(), check_dist_not_registered(), drop_warning_stat(), get_default_varnames(), get_random_generator() (+44 more)

### Community 12 - "Community 12"
Cohesion: 0.04
Nodes (26): EmpiricalGroup, Builds Approximation instance from a given trace.      It has the same interface, Approximation, *Dev* - Property to control scaling cost to minibatch., *Dev* - normalizing constant for `self.logq`, scales it to `minibatch_size` inst, *Dev* - collects `symbolic_logq` for all groups., *Dev* - collects `logQ` for all groups., *Dev* - collects `logQ` for all groups and normalizes it. (+18 more)

### Community 13 - "Community 13"
Cohesion: 0.05
Nodes (34): Base, Periodic, r"""     The Periodic kernel.      .. math::        k(x, x') = \mathrm{exp}\left, r"""Power spectral density approximation.          Technically, this is not a sp, Base, approx_hsgp_hyperparams(), calc_basis_periodic(), calc_eigenvalues() (+26 more)

### Community 14 - "Community 14"
Cohesion: 0.07
Nodes (37): ExceptionWithTraceback, ParallelSamplingError, Perform setup logic once before sampling starts., Calculate the next inverse temperature (beta).          The importance weights b, Tuning logic performed before every mutation step., Apply kernel-specific perturbation to the particles once per stage., Stats to be saved at the end of each stage.          These stats will be saved u, Perform a single SMC stage: resample, tune, and mutate. (+29 more)

### Community 15 - "Community 15"
Cohesion: 0.09
Nodes (44): ImputationWarning, Warning that there are missing values that will be imputed., Something that could lead to shape problems down the line., ShapeWarning, ParameterValueError, BlockModelAccess, compile_fn(), ContextMeta (+36 more)

### Community 16 - "Community 16"
Cohesion: 0.06
Nodes (29): CholeskyCovPacked, _default_transform(), Interval, LogExpM1, LogOddsTransform, LogTransform, Ordered, Transforms K - 1 dimensional simplex space (K values in [0, 1] that sum to 1) to (+21 more)

### Community 17 - "Community 17"
Cohesion: 0.07
Nodes (35): ABC, BaseTrace, Base trace object.      Parameters     ----------     name: str         Name of, Perform chain-specific setup.          Parameters         ----------         dra, Get the sample at index `idx`., _init_trace(), init_traces(), Marker base for :class:`pymc.backends.zarr.ZarrTrace`. See ``_ZarrChainBase``. (+27 more)

### Community 18 - "Community 18"
Cohesion: 0.05
Nodes (47): Enum, _build_mermaid_edges(), _build_mermaid_node(), _build_mermaid_nodes(), _build_mermaid_plates(), _create_mermaid_node_name(), default_data(), default_deterministic() (+39 more)

### Community 19 - "Community 19"
Cohesion: 0.11
Nodes (32): BaseHMC, BaseHMCState, GradientSharedStep, BaseHMC, BaseHMCState, DivergenceInfo, HMCStepData, Set up Hamiltonian samplers with common structures.          Parameters (+24 more)

### Community 20 - "Community 20"
Cohesion: 0.06
Nodes (45): DictToArrayBijection, Map between a `dict`s of variables to an array space.      Said array space cons, Map a dictionary of names and variables to a concatenated 1D array space., Map 1D concatenated array to a dictionary of variables in their original spaces., RaveledVars, SamplingError, Leapfrog integrator using CPU., Compute Hamiltonian functions using a position and momentum. (+37 more)

### Community 21 - "Community 21"
Cohesion: 0.06
Nodes (29): MinibatchOp, Encapsulate Minibatch random draws in an opaque OFG., BaseModel, Clone and replace random variables in graphs with their value variables., Compile and profile a PyTensor function which returns ``outs`` and takes values, r"""Check that the logp is defined and finite at the starting point.          Pa, Compute the log probability of `point` for all random variables in the model., Debug model function at point.          The method will evaluate the `fn` for ea (+21 more)

### Community 22 - "Community 22"
Cohesion: 0.06
Nodes (30): MarimoSimpleProgress, Simple marimo-aware progress bar for forward sampling functions.      This provi, Enter the context manager., Exit the context manager with final render., Add a task (interface compatibility with CustomProgress).          Kwargs are ig, Advance the progress bar.          Parameters         ----------         task_id, Update the progress bar state.          Parameters         ----------         ta, Render HTML progress to marimo output. (+22 more)

### Community 23 - "Community 23"
Cohesion: 0.11
Nodes (31): Operator, Empirical, FullRank, MeanField, Draw samples from variational posterior.      Parameters     ----------     appr, R"""         Allow to statically evaluate any symbolic expression over the trace, # NOTE: `Group._prepare_start` uses `self.model.free_RVs` to identify free varia, sample_approx() (+23 more)

### Community 24 - "Community 24"
Cohesion: 0.04
Nodes (1): _mean()

### Community 25 - "Community 25"
Cohesion: 0.05
Nodes (21): Approximation, Base class for Single Group Approximation., SingleGroupApproximation, Group, *Dev* - after node is sampled via :func:`symbolic_sample_over_posterior` or :fun, *Dev* - replace vars with flattened view stored in `self.inputs`., *Dev* - perform sampling of node applying single sample from posterior., *Dev* - create correct replacements for initial depending on sample size and det (+13 more)

### Community 26 - "Community 26"
Cohesion: 0.05
Nodes (10): Discrete, Bernoulli, BetaBinomial, Categorical, DiscreteUniform, DiscreteWeibull, Geometric, HyperGeometric (+2 more)

### Community 27 - "Community 27"
Cohesion: 0.07
Nodes (44): get_config(), get_keywords(), get_versions(), git_get_keywords(), git_pieces_from_vcs(), git_versions_from_keywords(), NotThisMethod, pep440_split_post() (+36 more)

### Community 28 - "Community 28"
Cohesion: 0.08
Nodes (25): DtypeError, Error that the dtype of a variable is incorrect., TypeError, MinibatchRandomVariable, RV whose logprob should be rescaled to match total_size., AEVBInferenceError, collect_shared_to_list(), ExplicitInferenceError (+17 more)

### Community 29 - "Community 29"
Cohesion: 0.07
Nodes (18): Coregion, Covariance, Exponentiated, Gibbs, handle_args(), Kron, r"""     The Gibbs kernel.      Use an arbitrary lengthscale function defined us, r"""     Construct a kernel by multiplying a base kernel with a scaling function (+10 more)

### Community 30 - "Community 30"
Cohesion: 0.09
Nodes (25): IBaseTrace, Record results of a sampling iteration.          Parameters         ----------, Minimal interface needed to record and access draws and stats for one MCMC chain, Get values from trace.          Parameters         ----------         varname: s, ZarrChain, BaseTrace, _check_start_shape(), Return True if nutpie is installed, importable, and meets the minimum version. (+17 more)

### Community 31 - "Community 31"
Cohesion: 0.06
Nodes (21): BackendError, _choose_chains(), Return point values at `idx` for current chain.          Returns         -------, Close the backend.          This is called after sampling has finished., Get sampler statistics from the trace.          Note: This implementation attemp, Get sampler statistics., Length of the chains., Get values from traces.          Parameters         ----------         varname: (+13 more)

### Community 32 - "Community 32"
Cohesion: 0.06
Nodes (19): nullcontext, MarimoProgressBackend, Update progress for a specific task.          Parameters         ----------, Render HTML progress display to marimo output., Generate HTML for all progress bars as a table with headers., Render a single task's progress as a table row., Marimo-based progress bar backend for HTML rendering.      This backend renders, Whether the progress bar is enabled (always True for marimo backend). (+11 more)

### Community 33 - "Community 33"
Cohesion: 0.09
Nodes (28): apply_function_over_dataset(), coords_and_dims_for_inferencedata(), dataset_to_point_list(), DataTreeConverter, dict_to_dataset(), dict_to_dataset_drop_incompatible_coords(), find_constants(), find_observations() (+20 more)

### Community 34 - "Community 34"
Cohesion: 0.10
Nodes (22): Whether each truncation bound is finite, when this can be known statically., r"""     Univariate truncated normal distribution.      The pdf of this distribu, TruncatedNormal, _truncation_is_bounded(), change_truncated_size(), # TODO: This will be simplified by https://github.com/pymc-devs/pytensor/pull/19, Create lower and upper logcdf expressions for base_rv.          Uses `value` as, Create logccdf expression at lower bound for base_rv.          Uses `value` as a (+14 more)

### Community 35 - "Community 35"
Cohesion: 0.07
Nodes (19): NDArray, point_list_to_multitrace(), Get values from trace.          Parameters         ----------         varname: s, Return point values at `idx` for current chain.          Returns         -------, Transform point list into MultiTrace., NDArray trace object.      Parameters     ----------     name: str         Name, Perform chain-specific setup.          Parameters         ----------         dra, Record results of a sampling iteration.          Parameters         ---------- (+11 more)

### Community 36 - "Community 36"
Cohesion: 0.10
Nodes (26): MinibatchIndexRV, Base class for SimulatorRVs.      This should be subclassed when defining custom, simulator_logp(), SimulatorRV, IntegersRV, conditional_logp(), _find_unallowed_rvs_in_graph(), icdf() (+18 more)

### Community 37 - "Community 37"
Cohesion: 0.09
Nodes (27): IfElse, PromisedValuedRV, r"""Marks a variable as being promised a valued variable that will only be assig, expand_indices(), find_measurable_ifelse_mixture(), find_measurable_index_mixture(), get_stack_mixture_vars(), logprob_ifelse() (+19 more)

### Community 38 - "Community 38"
Cohesion: 0.10
Nodes (8): _cpu_count(), _initialize_multiprocessing_context(), ParallelSampler, _Process, ProcessAdapter, rebuild_exc(), RemoteTraceback, _run_process()

### Community 39 - "Community 39"
Cohesion: 0.08
Nodes (19): IMH, MH, Pearson, Independent Metropolis-Hastings SMC_kernel., Create the Independent Metropolis-Hastings SMC kernel object.          Parameter, Independent Metropolis-Hastings perturbation., Metropolis-Hastings SMC_kernel., Create a Metropolis-Hastings SMC kernel.          Parameters         ---------- (+11 more)

### Community 40 - "Community 40"
Cohesion: 0.06
Nodes (30): binomln(), check_icdf_value(), check_parameters(), clipped_beta_rvs(), factln(), log_diff_normal_cdf(), log_i0(), log_normal() (+22 more)

### Community 41 - "Community 41"
Cohesion: 0.07
Nodes (17): Cosine, Exponential, ExpQuad, Matern12, Matern32, Matern52, r"""     Base class for stationary kernels/covariance functions.      Parameters, r"""     The Exponentiated Quadratic kernel.      Also referred to as the Square (+9 more)

### Community 42 - "Community 42"
Cohesion: 0.09
Nodes (14): _CustomDist, CustomDistRV, _CustomSymbolicDist, default_not_implemented(), DensityDist, dist_support_point(), Add size and updates to user provided gufunc signature if they are missing., A helper class to create custom distributions.      This class can be used to wr (+6 more)

### Community 43 - "Community 43"
Cohesion: 0.08
Nodes (25): CheckAndRaise, find_measurable_check_and_raise(), find_measurable_specify_shapes(), MeasurableCheckAndRaise, MeasurableSpecifyShape, r"""Find `AssertOp`\s for which a `logprob` can be computed., A placeholder used to specify a log-likelihood for a specify-shape sub-graph., r"""Find `SpecifyShapeOp`\s for which a `logprob` can be computed. (+17 more)

### Community 44 - "Community 44"
Cohesion: 0.16
Nodes (22): IntEnum, CallableTensor, Turns a symbolic variable with one input into a function that returns symbolic a, Replace the single input of symbolic variable to be the passed argument., Competence, BinaryGibbsMetropolisState, BinaryMetropolisState, CategoricalGibbsMetropolisState (+14 more)

### Community 45 - "Community 45"
Cohesion: 0.07
Nodes (19): batched_diag(), BatchedDiag, cartesian(), expand_packed_triangular(), kron_diag(), kron_matrix_op(), kronecker(), log1mexp() (+11 more)

### Community 46 - "Community 46"
Cohesion: 0.12
Nodes (29): _default_repr_pretty(), _dims_expression(), _format_underscore(), _latex_escape(), _latex_text_format(), _model_parameter_count(), model_table(), Make a human-readable string representation of a Data variable in a model. (+21 more)

### Community 47 - "Community 47"
Cohesion: 0.11
Nodes (29): adadelta(), adagrad(), adagrad_window(), adam(), adamax(), apply_momentum(), apply_nesterov_momentum(), _get_call_kwargs() (+21 more)

### Community 48 - "Community 48"
Cohesion: 0.09
Nodes (19): Data(), determine_coords(), GenTensorVariable, get_data(), is_valid_observed(), Minibatch(), Get random slices from variables from the leading dimension.      Parameters, Determine coordinate values from data or the model (via ``dims``). (+11 more)

### Community 49 - "Community 49"
Cohesion: 0.08
Nodes (25): _change_dist_size(), change_specify_shape_size(), convert_dims(), convert_dims_with_ellipsis(), convert_shape(), convert_size(), find_size(), get_support_shape() (+17 more)

### Community 50 - "Community 50"
Cohesion: 0.16
Nodes (19): PopulationArrayStepShared, _iter_population(), PopulationStepper, _prepare_iter_population(), Emit informative errors/warnings for dangerously small population size., Wraps population of step methods to step them in parallel with single or multipr, Use multiprocessing to parallelize chains.          Falls back to sequential eva, Do nothing: processes are already started in ``__init__``. (+11 more)

### Community 51 - "Community 51"
Cohesion: 0.13
Nodes (22): assert_equivalent_model(), build_model(), check_icdf(), check_selfconsistency_icdf(), continuous_random_tester(), discrete_random_tester(), Domain, equal_computations_up_to_root() (+14 more)

### Community 52 - "Community 52"
Cohesion: 0.09
Nodes (24): Blockwise, _icdf(), _icdf_helper(), _logccdf(), _logccdf_helper(), _logcdf(), _logcdf_helper(), _logprob() (+16 more)

### Community 53 - "Community 53"
Cohesion: 0.09
Nodes (12): IncorrectArgumentsError, Error from trying to load a trace from an incorrectly-structured directory., TraceDirectoryError, QuadPotentialFullAdapt, Set up a diagonal mass matrix.          Parameters         ----------         n, Check if the mass matrix is ok, and raise ValueError if not.          Parameters, Online algorithm for computing mean of variance., Adapt a dense mass matrix using the sample covariances. (+4 more)

### Community 54 - "Community 54"
Cohesion: 0.08
Nodes (12): _DefaultTrace, Utility for collecting samples into a dictionary.      Name comes from its simil, Insert `v` as the value of the `idx`th sample for the variable `k`.          Par, Decorator that returns None if all required attributes on the wrapped instance a, requires, MultiTrace, Main interface for accessing values from MCMC results.      The core method to s, Return a string representation of MultiTrace. (+4 more)

### Community 55 - "Community 55"
Cohesion: 0.09
Nodes (14): NotImplementedError, ObjectiveFunction, KSDObjective, R"""Helper class for construction loss and updates for variational inference., ObjectiveFunction, Operator, Return the standard deviation of the latent variables as an unstructured 1-dimen, Return the covariance between the latent variables as an unstructured 2-dimensio (+6 more)

### Community 56 - "Community 56"
Cohesion: 0.09
Nodes (15): ModelVar, A dummy Op that describes the purpose of a Model variable.      The variable's `, assert_no_rvs(), mock_sample(), mock_sample_setup_and_teardown(), Assert that there are no `MeasurableOp` nodes in a graph., Mock :func:`pymc.sample` with :func:`pymc.sample_prior_predictive`.      Useful, Set up and tear down mocking of PyMC sampling functions for testing.      This f (+7 more)

### Community 57 - "Community 57"
Cohesion: 0.15
Nodes (24): ImplicitFreezeWarning, Warning that trace values are being reused instead of resampled.      Emitted by, _build_constant_data(), compile_forward_sampling_function(), _compute_volatile_vars(), _data_var_is_volatile(), draw(), get_vars_in_point_list() (+16 more)

### Community 58 - "Community 58"
Cohesion: 0.09
Nodes (12): Feature, Apply transforms to value variables.      It is assumed that the input value var, r"""A `Feature` that maintains a map between value variables and their transform, A no-op that pairs the original value with its transformed version.      This is, A no-op that identifies RVs whose values were transformed.      This is introduc, Compute the log-probability graph for a `TransformedRV`.      This is introduced, transform_values(), transformed_value_logprob() (+4 more)

### Community 59 - "Community 59"
Cohesion: 0.10
Nodes (12): BarColumn, Progress, CustomBarColumn, CustomProgress, MarkerProgressBar, A progress bar with a thin gap at a given position (e.g. tune/draw boundary)., Bar column that recolors on divergences and renders a separator marker., Update bar color based on failure state. (+4 more)

### Community 60 - "Community 60"
Cohesion: 0.15
Nodes (13): VectorDimDistribution, ZeroSumNormal random variable., _squeeze_to_ndim(), ZeroSumNormalRV, Categorical, Dirichlet, MvNormal, Multivariate Normal distribution.      Parameters     ----------     mu : xtenso (+5 more)

### Community 61 - "Community 61"
Cohesion: 0.09
Nodes (5): Group, FullRankGroup, MeanFieldGroup, Full Rank approximation to the posterior.      Multivariate Gaussian family is f, Mean Field approximation to the posterior.      Spherical Gaussian family is fit

### Community 62 - "Community 62"
Cohesion: 0.15
Nodes (4): get_initial_fill_value_and_codec(), ZarrTrace, Check that vars not include discrete variables., _ZarrTraceBase

### Community 63 - "Community 63"
Cohesion: 0.15
Nodes (19): _device_put(), _get_batched_jittered_initial_points(), get_jaxified_graph(), get_jaxified_logp(), _get_log_likelihood(), _numpyro_stats_to_dict(), _postprocess_samples(), Compile a PyTensor graph into an optimized JAX function. (+11 more)

### Community 64 - "Community 64"
Cohesion: 0.12
Nodes (10): ArrayStep, BlockedStep, ArrayStep, metrop_select(), BinaryGibbsMetropolis, BinaryMetropolis, Metropolis-Hastings optimized for binary variables.      Unlike BinaryGibbsMetro, BinaryMetropolis is only suitable for binary (bool) and Categorical variables wi (+2 more)

### Community 65 - "Community 65"
Cohesion: 0.12
Nodes (9): ArrayStepShared, ArrayStepShared, DEMetropolisZ, Adaptive Differential Evolution Metropolis sampling step that uses the past to i, Reset the tuned sampler parameters and history to their initial values., Remove the first x% of the history at the end of the tuning phase.          This, Univariate slice sampler step method.      Parameters     ----------     vars :, Slice (+1 more)

### Community 66 - "Community 66"
Cohesion: 0.12
Nodes (10): assume_valued_outputs(), construct_ir_fgraph(), local_lift_DiracDelta(), r"""Lift basic `Op`\s through `DiracDelta`\s., r"""Remove `DiracDelta`\s., r"""Construct a `FunctionGraph` in measurable IR form for the keys in `rv_values, Run IR rewrite assuming each output is measured.      IR variables could depend, remove_DiracDelta() (+2 more)

### Community 67 - "Community 67"
Cohesion: 0.12
Nodes (10): create_distance_op_from_fn(), create_sum_stat_op_from_fn(), identity(), KullbackLeibler, # TODO: Wrap KL in pytensor OP, # TODO: Model rngs should be updated prior to multiprocessing split,, Identity function, used as a summary statistics., Approximate Kullback-Leibler. (+2 more)

### Community 68 - "Community 68"
Cohesion: 0.20
Nodes (18): all_continuous(), assign_step_methods(), get_default_tune_steps(), _init_jitter(), init_nuts(), instantiate_steppers(), _iter_sample(), _mp_sample() (+10 more)

### Community 69 - "Community 69"
Cohesion: 0.13
Nodes (8): delta_logp(), Metropolis, NormalProposal, Metropolis-Hastings sampling step., Create an instance of a Metropolis stepper.          Parameters         --------, Reset the tuned sampler parameters to their initial values., Tune the scaling parameter for the proposal distribution.      Uses the acceptan, tune()

### Community 70 - "Community 70"
Cohesion: 0.18
Nodes (16): clone_model(), deepcopy_shared_variable(), fgraph_from_model(), model_deterministic(), model_free_rv(), model_from_fgraph(), model_named(), model_observed_rv() (+8 more)

### Community 71 - "Community 71"
Cohesion: 0.12
Nodes (5): CpuLeapfrogIntegrator, QuadPotential, Compute the current velocity at a position in parameter space., Inform the potential about a new sample during tuning.          This can be used, Check if the mass matrix is ok, and raise ValueError if not.          Parameters

### Community 72 - "Community 72"
Cohesion: 0.16
Nodes (15): construct_scan(), convert_outer_out_to_in(), find_measurable_scans(), get_initval_from_scan_tap_input(), get_random_outer_outputs(), logprob_scan(), MeasurableScan, Get the measurable outputs of a `Scan` (well, its `ScanArgs`).      Returns (+7 more)

### Community 73 - "Community 73"
Cohesion: 0.13
Nodes (11): convert_indices(), find_negated_var(), get_related_valued_nodes(), indices_from_subtensor(), local_remove_check_parameter(), Compute a useable index tuple from the inputs of a ``*Subtensor**`` ``Op``., Rewrite that removes CheckParameterValue.      This is used when compile_rv_inpl, Return a variable that is being multiplied by -1 or None otherwise. (+3 more)

### Community 74 - "Community 74"
Cohesion: 0.18
Nodes (13): constant_fold(), cont_inputs(), gradient(), gradient1(), hessian(), hessian_diag(), hessian_diag1(), jacobian() (+5 more)

### Community 75 - "Community 75"
Cohesion: 0.15
Nodes (4): Circular, r"""     White noise covariance function.      .. math::         k(x, x') = \sig, R"""     Circular Kernel.      .. math::          k_g(x, y) = W_\pi(\operatornam, WhiteNoise

### Community 76 - "Community 76"
Cohesion: 0.13
Nodes (14): clip_logcdf(), clip_logprob(), find_measurable_clips(), find_measurable_roundings(), measurable_max_min_to_clip(), MeasurableClip, Convert one-sided censoring maximum(x, c) and minimum(x, c) to clip form.      T, r"""Logprob of a clipped censored distribution.      The probability is given by (+6 more)

### Community 77 - "Community 77"
Cohesion: 0.18
Nodes (6): ChainRecordAdapter, find_data(), get_variables_and_point_fn(), init_chain_adapters(), make_runmeta_and_point_fn(), IBaseTrace

### Community 78 - "Community 78"
Cohesion: 0.22
Nodes (9): find_measurable_xtensor_from_tensor(), measurable_xtensor_from_tensor_icdf(), measurable_xtensor_from_tensor_logccdf(), measurable_xtensor_from_tensor_logcdf(), measurable_xtensor_from_tensor_logprob(), MeasurableXTensorFromTensor, _to_tensor(), _to_xtensor() (+1 more)

### Community 79 - "Community 79"
Cohesion: 0.16
Nodes (5): Clone the model.          To access variables in the cloned model use `cloned_mo, Return a function that reuses the compiled graph but owns its shared variables., Profiling information of the underlying PyTensor function., Compile a PyTensor function that computes logp and gradient.          Parameters, ValueGradFunction

### Community 80 - "Community 80"
Cohesion: 0.18
Nodes (12): convert_str_to_rv_dict(), InitialPoint, make_initial_point_expression(), make_initial_point_fn(), make_initial_point_fns_per_chain(), non_support_point_ancestors(), Create seeded function that computes initial values for all free model variables, Create the tensor variables that need to be evaluated to obtain an initial point (+4 more)

### Community 81 - "Community 81"
Cohesion: 0.26
Nodes (11): ModelDeterministic, ModelFreeRV, ModelValuedVar, change_value_transforms(), do(), observe(), Replace model variables by intervention variables.      Intervention variables w, r"""Change the value variables transforms in the model.      Parameters     ---- (+3 more)

### Community 82 - "Community 82"
Cohesion: 0.20
Nodes (14): check_logccdf(), check_logcdf(), check_logp(), check_selfconsistency_discrete_logcdf(), create_dist_from_paramdomains(), find_invalid_scalar_params(), Choose reasonable decimal cutoffs for different floatX modes., Create a PyMC distribution from a dictionary of parameter domains.      Returns (+6 more)

### Community 83 - "Community 83"
Cohesion: 0.21
Nodes (13): adjust_precision(), adjust_scaling(), bound(), eig_recompose(), find_hessian(), find_hessian_diag(), fixed_hessian(), guess_scaling() (+5 more)

### Community 84 - "Community 84"
Cohesion: 0.18
Nodes (2): Stein, WithMemoization

### Community 85 - "Community 85"
Cohesion: 0.21
Nodes (6): Add, Combination, Prod, Use constituent factors to get input_dim and active_dims for the Combination cov, Evaluate either all the sums or all the products of kernels that are possible to, Evaluate spectral densities of combination kernels when possible.          Imple

### Community 86 - "Community 86"
Cohesion: 0.15
Nodes (7): QuadPotentialDiagAdapt, Adapt a diagonal mass matrix from the sample variances., Compute the current velocity at a position in parameter space., Compute kinetic energy at a position in parameter space., Compute velocity and return kinetic energy at a position in parameter space., Draw random value from QuadPotential., Inform the potential about a new sample during tuning.

### Community 87 - "Community 87"
Cohesion: 0.20
Nodes (3): DifferentialEquation, r"""Solve both ODE and sensitivities.          This function will be passed to o, r"""     Specify an ordinary differential equation.      Due to the nature of th

### Community 88 - "Community 88"
Cohesion: 0.21
Nodes (4): BaseTestDistributionRandom, Base class for tests that new RandomVariables are correctly implemented.      Al, seeded_numpy_distribution_builder(), seeded_scipy_distribution_builder()

### Community 89 - "Community 89"
Cohesion: 0.18
Nodes (4): Callback, Get the element at index `item`., Helper class to record arbitrary stats during VI.      It is possible to pass a, Tracker

### Community 90 - "Community 90"
Cohesion: 0.27
Nodes (6): Censored, censored_logcdf(), change_censored_size(), _is_unbounded(), # TODO: Make this a SymbolicRandomVariable that can itself be resized, # TODO: Hack -- we have no rng of our own to thread forward.

### Community 91 - "Community 91"
Cohesion: 0.22
Nodes (4): Linear, Polynomial, r"""     The Linear kernel.      .. math::        k(x, x') = (x - c)(x' - c), r"""     The Polynomial kernel.      .. math::        k(x, x') = [(x - c)(x' - c

### Community 92 - "Community 92"
Cohesion: 0.18
Nodes (10): conditioned_vars(), kmeans_inducing_points(), plot_gp_dist(), Validate attrs that are conditioned on., Plot 1D GP posteriors from trace.      Parameters     ----------     ax : axes, R"""     Replace random variable nodes in the graph with values given by the rep, R"""     Add small diagonal to a covariance matrix.      Often the matrices calc, R"""     Use the K-means algorithm to initialize the locations `X` for the induc (+2 more)

### Community 93 - "Community 93"
Cohesion: 0.20
Nodes (11): convert_data(), convert_observed_data(), floatX(), intX(), largest_common_dtype(), Convert a PyTensor tensor or numpy array to pytensor.config.floatX type., Convert a pytensor tensor or numpy array to pytensor.tensor.int32 type., Convert numpy float values to floatX and leaves values of other types unchanged. (+3 more)

### Community 94 - "Community 94"
Cohesion: 0.20
Nodes (4): CategoricalGibbsMetropolis, A Metropolis-within-Gibbs step method optimized for categorical variables., CategoricalGibbsMetropolis is only suitable for Bernoulli and Categorical variab, sample_except()

### Community 95 - "Community 95"
Cohesion: 0.22
Nodes (3): _ExpWeightedVariance, QuadPotentialDiagAdaptExp, Set up a diagonal mass matrix.          Parameters         ----------         n

### Community 96 - "Community 96"
Cohesion: 0.29
Nodes (9): _extract_scale_from_measurable_mul(), find_measurable_switch_non_overlapping(), logprob_switch_non_overlapping(), MeasurableSwitchNonOverlapping, Extract scale `a` from a measurable multiplication that represents `a * x`., Detect `switch(x > 0, x, a * x)` and replace it by a measurable op., Placeholder for switch transforms whose branch images do not overlap.      Curre, Return whether `cond` is a zero threshold on `x` and includes `0` in the true br (+1 more)

### Community 97 - "Community 97"
Cohesion: 0.20
Nodes (5): Copy compiled functions, updating their random number generators.          This, Create an initial population from the prior distribution., Initialize particles and compute their prior and likelihood logp.          This, Reset the sampling state for a new run., Initialize the kernel for sampling.          Parameters         ----------

### Community 98 - "Community 98"
Cohesion: 0.29
Nodes (9): log_warning(), log_warning_stats(), log_warnings(), Check sampler stats and creates a list of warnings about divergences., Check sampler stats and creates a list of warnings about tree depth., Log 'warning' stats if present., run_convergence_checks(), warn_divergences() (+1 more)

### Community 99 - "Community 99"
Cohesion: 0.28
Nodes (6): find_measurable_bitwise(), find_measurable_comparisons(), MeasurableBitwise, MeasurableComparison, A placeholder used to specify a log-likelihood for a bitwise operation RV sub-gr, A placeholder used to specify a log-likelihood for a binary comparison RV sub-gr

### Community 100 - "Community 100"
Cohesion: 0.22
Nodes (6): _logp_forw(), Initialize the SMC_kernel class.          Parameters         ----------, Resample particles based on importance weights., Systematic resampling.      Parameters     ----------     weights :         The, Compile PyTensor function of the model and the input and output variables., systematic_resampling()

### Community 101 - "Community 101"
Cohesion: 0.32
Nodes (7): Data(), Deterministic(), Potential(), Wrapper around pymc.Data that returns an XtensorVariable.      Dimensions are re, Wrapper around pymc.Deterministic that returns an XtensorVariable.      If the i, Wrapper around pymc.Potential that returns an XtensorVariable.      If the input, _register_and_return_xtensor_variable()

### Community 102 - "Community 102"
Cohesion: 0.29
Nodes (2): InverseGamma, r"""     Inverse gamma distribution, the reciprocal of the gamma distribution.

### Community 103 - "Community 103"
Cohesion: 0.36
Nodes (3): IntervalTransform, Create the IntervalTransform object.          Parameters         ----------, Return interval bound values.          Also returns two boolean variables indica

### Community 104 - "Community 104"
Cohesion: 0.36
Nodes (7): _build_transform_graph(), constrain_values(), _eval_transform_graph(), Transform a dataset of constrained to unconstrained values.      Example     ---, Transform a dataset of unconstrained to constrained values.      Example     ---, Build a per-sample graph that applies transforms to all free RVs.      Parameter, unconstrain_values()

### Community 105 - "Community 105"
Cohesion: 0.25
Nodes (8): collect_default_updates(), collect_default_updates_inner_fgraph(), compile(), Create a new set of RandomState/Generator for each rng based on a seed., Collect default updates from node with inner fgraph., Collect default update expression for shared-variable RNGs used by RVs between i, Use ``pytensor.function`` with specialized pymc rewrites always enabled.      Th, reseed_rngs()

### Community 106 - "Community 106"
Cohesion: 0.36
Nodes (7): _constant_from_shared(), _extract_initial_values(), freeze_dims_and_data(), freeze_model(), Return a frozen copy of the model that caches its compiled functions.      On th, Return the model's non-default initial values, keyed by variable name.      Symb, Recreate a Model with fixed RV dimensions and Data values.      The dimensions o

### Community 107 - "Community 107"
Cohesion: 0.33
Nodes (2): r"""     Wald distribution.      The pdf of this distribution is      .. math::, Wald

### Community 108 - "Community 108"
Cohesion: 0.48
Nodes (1): _Tree

### Community 109 - "Community 109"
Cohesion: 0.33
Nodes (4): FrozenModel, A model whose graph is immutable and whose compiled functions are cached.      C, Whether ``mode``'s linker copies RNG shared variables at compile time.      Such, _rng_detaching_linker()

### Community 110 - "Community 110"
Cohesion: 0.29
Nodes (5): format_time(), in_marimo_notebook(), Format elapsed time as mm:ss or hh:mm:ss., Check if running inside a marimo notebook.      Returns     -------     bool, Generate HTML for the progress bar as a table.

### Community 111 - "Community 111"
Cohesion: 0.38
Nodes (6): compute_log_density(), compute_log_likelihood(), compute_log_prior(), Compute elemwise log_likelihood or log_prior of model given InferenceData with p, Compute elemwise log_likelihood of model given InferenceData with posterior grou, Compute elemwise log_prior of model given InferenceData with posterior group.

### Community 112 - "Community 112"
Cohesion: 0.38
Nodes (2): CostFuncWrapper, find_MAP()

### Community 113 - "Community 113"
Cohesion: 0.33
Nodes (3): Compose, Create a callable that first maps back to ``dict`` inputs and then applies a fun, Compose two functions in a pickleable way.

### Community 114 - "Community 114"
Cohesion: 0.40
Nodes (1): LKJCorrRV

### Community 115 - "Community 115"
Cohesion: 0.33
Nodes (3): r"""     The Rational Quadratic kernel.      .. math::         k(x, x') = \left(, r"""         Power spectral density for the Rational Quadratic kernel., RatQuad

### Community 116 - "Community 116"
Cohesion: 0.33
Nodes (4): prune_vars_detached_from_observed(), Prune model variables that are not related to any observed variable in the Model, Remove all uses of pm.Minibatch in the Model., remove_minibatched_nodes()

### Community 117 - "Community 117"
Cohesion: 0.40
Nodes (5): create_minibatch_rv(), get_scaling(), minibatch_rv_logprob(), Create variable whose logp is rescaled by total_size., Get scaling constant for logp.

### Community 118 - "Community 118"
Cohesion: 0.40
Nodes (4): augment_system(), make_sens_ic(), r"""     Make initial condition for the sensitivity matrix.      The sensitivity, Create augmented system.      Take a function which specifies a set of different

### Community 119 - "Community 119"
Cohesion: 0.50
Nodes (4): compute_deterministics(), Select the relevant group when a whole InferenceData object is passed., Compute model deterministics given a dataset with values for model variables., _select_group()

### Community 120 - "Community 120"
Cohesion: 0.67
Nodes (3): Resolve a removed root-namespace symbol or raise ``AttributeError``., resolve(), _warn()

### Community 121 - "Community 121"
Cohesion: 0.50
Nodes (4): extract_obs_data(), Extract data from observed symbolic variables.      Raises     ------     TypeEr, Assert that there are no random nodes in a graph., rvs_in_graph()

### Community 122 - "Community 122"
Cohesion: 0.50
Nodes (4): find_rng_nodes(), Return shared RNG variables in a graph., Replace any RNG nodes upstream of outputs by new RNGs of the same type.      Thi, replace_rng_nodes()

### Community 123 - "Community 123"
Cohesion: 0.50
Nodes (4): get_symbolic_rv_shapes(), Rewrite shape expressions via ShapeFeature + infer_shape rewrites.      Replaces, Compute symbolic shapes of random variables without referencing the RVs themselv, resolve_shapes()

### Community 124 - "Community 124"
Cohesion: 0.50
Nodes (4): Replace multiple variables in place in topological order., Replace variables in graphs.      Graphs are cloned and not modified in place, u, replace_vars_in_graphs(), toposort_replace()

### Community 125 - "Community 125"
Cohesion: 0.67
Nodes (2): Exception, UndefinedMomentException

### Community 126 - "Community 126"
Cohesion: 0.67
Nodes (2): find_constrained_prior(), Find optimal parameters to get `mass` % of probability of a distribution between

### Community 132 - "Community 132"
Cohesion: 1.00
Nodes (2): inputvars(), Get the inputs into PyTensor variables.      Parameters     ----------         a

### Community 133 - "Community 133"
Cohesion: 1.00
Nodes (2): ix_(), PyTensor np.ix_ analog.      See numpy.lib.index_tricks.ix_ for reference

### Community 134 - "Community 134"
Cohesion: 1.00
Nodes (2): join_nonshared_inputs(), Create new outputs and input TensorVariables where the non-shared inputs are joi

### Community 135 - "Community 135"
Cohesion: 1.00
Nodes (2): make_shared_replacements(), Make shared replacements for all *other* variables than the ones passed.      Th

### Community 136 - "Community 136"
Cohesion: 1.00
Nodes (2): normalize_rng_param(), Validate rng is a valid type or create a new one if None.

### Community 137 - "Community 137"
Cohesion: 1.00
Nodes (2): pregrad_inner_graphs(), Apply the pre-grad rewrites to the inner graph of every inner-graph op.

### Community 138 - "Community 138"
Cohesion: 1.00
Nodes (2): Apply simplifying or stabilizing rewrites to graph that are safe to use pre-grad, rewrite_pregrad()

### Community 139 - "Community 139"
Cohesion: 1.00
Nodes (2): Materialize a `backend` shortcut as `compile_kwargs['mode']`.      Returns a new, resolve_backend_compile_kwargs()

## Knowledge Gaps
- **199 isolated node(s):** `Resolve a removed root-namespace symbol or raise ``AttributeError``.`, `Get the keywords needed to look up the version information.`, `Container for Versioneer configuration parameters.`, `Create, populate and return the VersioneerConfig() object.`, `Exception raised if a method is not valid for the current scenario.` (+194 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 24`** (1 nodes): `_mean()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 84`** (2 nodes): `Stein`, `WithMemoization`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 102`** (2 nodes): `InverseGamma`, `r"""     Inverse gamma distribution, the reciprocal of the gamma distribution.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 107`** (2 nodes): `r"""     Wald distribution.      The pdf of this distribution is      .. math::`, `Wald`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 108`** (1 nodes): `_Tree`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 112`** (2 nodes): `CostFuncWrapper`, `find_MAP()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 114`** (1 nodes): `LKJCorrRV`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 125`** (2 nodes): `Exception`, `UndefinedMomentException`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 126`** (2 nodes): `find_constrained_prior()`, `Find optimal parameters to get `mass` % of probability of a distribution between`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 132`** (2 nodes): `inputvars()`, `Get the inputs into PyTensor variables.      Parameters     ----------         a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 133`** (2 nodes): `ix_()`, `PyTensor np.ix_ analog.      See numpy.lib.index_tricks.ix_ for reference`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 134`** (2 nodes): `join_nonshared_inputs()`, `Create new outputs and input TensorVariables where the non-shared inputs are joi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 135`** (2 nodes): `make_shared_replacements()`, `Make shared replacements for all *other* variables than the ones passed.      Th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 136`** (2 nodes): `normalize_rng_param()`, `Validate rng is a valid type or create a new one if None.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 137`** (2 nodes): `pregrad_inner_graphs()`, `Apply the pre-grad rewrites to the inner graph of every inner-graph op.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 138`** (2 nodes): `Apply simplifying or stabilizing rewrites to graph that are safe to use pre-grad`, `rewrite_pregrad()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 139`** (2 nodes): `Materialize a `backend` shortcut as `compile_kwargs['mode']`.      Returns a new`, `resolve_backend_compile_kwargs()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MeasurableOp` connect `Community 9` to `Community 10`, `Community 78`, `Community 60`, `Community 1`, `Community 3`, `Community 0`, `Community 7`, `Community 52`, `Community 6`, `Community 36`, `Community 43`, `Community 37`, `Community 72`, `Community 96`, `Community 58`, `Community 2`, `Community 103`, `Community 66`, `Community 15`, `Community 73`, `Community 46`, `Community 28`, `Community 117`?**
  _High betweenness centrality (0.230) - this node is a cross-community bridge._
- **Why does `DictToArrayBijection` connect `Community 20` to `Community 113`, `Community 19`, `Community 71`, `Community 21`, `Community 15`, `Community 109`, `Community 48`, `Community 79`, `Community 30`, `Community 68`, `Community 62`, `Community 14`, `Community 38`, `Community 39`, `Community 100`, `Community 97`, `Community 64`, `Community 65`, `Community 50`, `Community 44`, `Community 94`, `Community 69`, `Community 83`, `Community 112`, `Community 23`, `Community 12`, `Community 61`, `Community 25`, `Community 28`, `Community 55`, `Community 35`, `Community 36`?**
  _High betweenness centrality (0.166) - this node is a cross-community bridge._
- **Why does `SymbolicRandomVariable` connect `Community 0` to `Community 90`, `Community 7`, `Community 1`, `Community 8`, `Community 10`, `Community 3`, `Community 102`, `Community 34`, `Community 107`, `Community 42`, `Community 26`, `Community 9`, `Community 43`, `Community 114`, `Community 60`, `Community 6`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Are the 319 inferred relationships involving `SymbolicRandomVariable` (e.g. with `Censored` and `CensoredRV`) actually correct?**
  _`SymbolicRandomVariable` has 319 INFERRED edges - model-reasoned connections that need verification._
- **Are the 314 inferred relationships involving `DictToArrayBijection` (e.g. with `BaseHMC` and `BaseHMCState`) actually correct?**
  _`DictToArrayBijection` has 314 INFERRED edges - model-reasoned connections that need verification._
- **Are the 230 inferred relationships involving `MeasurableOp` (e.g. with `Make PyMC aware of the xtensor functionality.` and `DimDistribution`) actually correct?**
  _`MeasurableOp` has 230 INFERRED edges - model-reasoned connections that need verification._
- **Are the 200 inferred relationships involving `MinibatchOp` (e.g. with `ShapeError` and `BaseModel`) actually correct?**
  _`MinibatchOp` has 200 INFERRED edges - model-reasoned connections that need verification._