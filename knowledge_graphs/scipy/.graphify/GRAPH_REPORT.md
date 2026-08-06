# Graph Report - scipy  (2026-08-06)

## Corpus Check
- Large corpus: 835 files · ~2,140,474 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 14193 nodes · 23606 edges · 811 communities detected
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 4745 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: contains: 5601 · calls: 5027 · uses: 4745 · method: 4084 · rationale_for: 3698 · inherits: 432 · imports_from: 16 · imports: 3


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 835 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `0514ef9`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `CensoredData` - 342 edges
2. `FitError` - 320 edges
3. `rv_continuous` - 278 edges
4. `LowLevelCallable` - 250 edges
5. `UnivariateDistribution` - 196 edges
6. `sparray` - 178 edges
7. `spmatrix` - 168 edges
8. `MapWrapper` - 154 edges
9. `FunctionDoc` - 152 edges
10. `OptimizeResult` - 135 edges

## Surprising Connections (you probably didn't know these)
- `============================================== Discrete Fourier transforms (:mod` --uses--> `PytestTester`  [INFERRED]
  fft/__init__.py → _lib/_testutils.py
- `The identifier of the target node.          For ``0 <= i < n``, `i` corresponds` --uses--> `DisjointSet`  [INFERRED]
  cluster/hierarchy/_hierarchy_impl.py → _lib/_disjoint_set.py
- `The number of leaf nodes (original observations) belonging to         the cluste` --uses--> `DisjointSet`  [INFERRED]
  cluster/hierarchy/_hierarchy_impl.py → _lib/_disjoint_set.py
- `Return a reference to the left child tree object.          Returns         -----` --uses--> `DisjointSet`  [INFERRED]
  cluster/hierarchy/_hierarchy_impl.py → _lib/_disjoint_set.py
- `Return a reference to the right child tree object.          Returns         ----` --uses--> `DisjointSet`  [INFERRED]
  cluster/hierarchy/_hierarchy_impl.py → _lib/_disjoint_set.py

## Communities

### Community 1 - "Community 1"
Cohesion: 0.02
Nodes (90): deprecate_cython_api(), _DeprecationHelperStr, Helper class used by deprecate_cython_api, Deprecate an exported cdef function in a public Cython API module.      Only fun, FunctionDoc, argsreduce(), _check_shape(), _drv2_moment() (+82 more)

### Community 2 - "Community 2"
Cohesion: 0.03
Nodes (121): sparray, SparseEfficiencyWarning, Compressed Block Sparse Row format, Check whether the array/matrix respects the BSR format.          Parameters, Block size of the matrix., Remove zero elements in-place., Eliminate duplicate array/matrix entries by adding them together.          The i, Sort the indices of this array/matrix *in place*. (+113 more)

### Community 3 - "Community 3"
Cohesion: 0.02
Nodes (38): alpha_gen, fatiguelife_gen, foldnorm_gen, gibrat_gen, halfnorm_gen, johnsonsb_gen, johnsonsu_gen, levy_l_gen (+30 more)

### Community 4 - "Community 4"
Cohesion: 0.02
Nodes (4): _guess_bracket(), _isnull(), r"""positive float:         The desired relative tolerance of calculations. Left, UnivariateDistribution

### Community 5 - "Community 5"
Cohesion: 0.04
Nodes (96): _arr_to_scalar(), Bounds, LinearConstraint, new_bounds_to_old(), new_constraint_to_old(), NonlinearConstraint, old_bound_to_new(), old_constraint_to_new() (+88 more)

### Community 6 - "Community 6"
Cohesion: 0.03
Nodes (61): LMap, LMapCache, shgo: The simplicial homology global optimisation algorithm., Various stopping criteria ran every iteration          Returns         -------, Iterate a subdivision of the complex          Note: called with ``self.iterate_c, Build a complex of Delaunay triangulated points          Note: called with ``sel, Returns the indexes of all minimizers, # TODO: Only do this if global mode (+53 more)

### Community 7 - "Community 7"
Cohesion: 0.02
Nodes (35): LowLevelCallable, Create a low-level callback function from an exported Cython function., Low-level callback function.      Some functions in SciPy take as arguments call, rv_continuous, exponnorm_gen, exponpow_gen, gausshyper_gen, genexpon_gen (+27 more)

### Community 8 - "Community 8"
Cohesion: 0.03
Nodes (70): cubature(), CubatureRegion, CubatureResult, _InfiniteLimitsTransform, _is_strictly_in_region(), Given the integration limits `a` and `b` describing a rectangular region and a l, A transformation that can be applied to an integral., New limits of integration after applying the transformation. (+62 more)

### Community 9 - "Community 9"
Cohesion: 0.04
Nodes (83): Scalar function and its derivatives.      This class defines a scalar function F, Wrapper class for gradient calculation, ScalarFunction, _ScalarGradWrapper, LineSearchWarning, approx_fhess_p(), approx_fprime(), bracket() (+75 more)

### Community 10 - "Community 10"
Cohesion: 0.04
Nodes (3): Upcast array to a floating point format (if necessary), _spbase, SparseABC

### Community 11 - "Community 11"
Cohesion: 0.03
Nodes (91): fmin_cobyla(), _minimize_cobyla(), Interface to Constrained Optimization By Linear Approximation  Functions -------, Minimize a scalar function of one or more variables using the     Constrained Op, Minimize a function using the Constrained Optimization By Linear     Approximati, isotonic_regression(), r"""Nonparametric isotonic regression.      A (not strictly) monotonically incre, _convert_to_highs_enum() (+83 more)

### Community 12 - "Community 12"
Cohesion: 0.02
Nodes (2): Delegators for alternative backends in scipy.signal.  The signature of `func_sig, # TODO: fix me - `prominence` is not necessarily an array.

### Community 13 - "Community 13"
Cohesion: 0.05
Nodes (78): SmallSampleWarning, MonteCarloMethod, PermutationMethod, Configuration information for a Monte Carlo hypothesis test.      Instances of t, Configuration information for a permutation hypothesis test.      Instances of t, _attempt_exact_2kssamp(), _cdf_distance(), chisquare() (+70 more)

### Community 14 - "Community 14"
Cohesion: 0.04
Nodes (44): ABC, ClassDoc, issparse(), Is `x` either sparse array or sparse matrix type?      Parameters     ----------, _combine_docs(), _Domain, _generate_domain_support(), _get_domain_info() (+36 more)

### Community 15 - "Community 15"
Cohesion: 0.04
Nodes (79): dlti, r"""     Discrete-time linear time invariant system base class.      Parameters, Create an instance of the appropriate subclass., Initialize the `lti` baseclass.          The heavy lifting is done by the subcla, Return the sampling time of the system., _angle(), _bvalfromboundary(), choose_conv_method() (+71 more)

### Community 16 - "Community 16"
Cohesion: 0.04
Nodes (40): invwishart_frozen, invwishart_gen, r"""     A Wishart random variable.      The `df` keyword specifies the degrees, Create a frozen Wishart distribution.          See `wishart_frozen` for more inf, Adjust quantiles array so that last axis labels the components of         each d, Log of the Wishart probability density function.          Parameters         ---, Log of the Wishart probability density function.          Parameters         ---, Wishart probability density function.          Parameters         ---------- (+32 more)

### Community 17 - "Community 17"
Cohesion: 0.09
Nodes (68): bsr_matrix, _block(), block_array(), block_diag(), bmat(), _compressed_sparse_stack(), diags(), diags_array() (+60 more)

### Community 18 - "Community 18"
Cohesion: 0.03
Nodes (53): dict, _apply_over_batch(), _asarray_validated(), broadcastable(), _call_callback_maybe_halt(), check_random_state(), _dedent_for_py313(), _deprecate_dtypes() (+45 more)

### Community 19 - "Community 19"
Cohesion: 0.04
Nodes (22): FitError, anglit_gen, arcsine_gen, bradford_gen, crystalball_gen, FitSolverError, jf_skew_t_gen, r"""A Bradford continuous random variable.      %(before_notes)s      Notes (+14 more)

### Community 20 - "Community 20"
Cohesion: 0.03
Nodes (12): betaprime_gen, dgamma_gen, foldcauchy_gen, moyal_gen, nct_gen, r"""A wrapped Cauchy continuous random variable.      %(before_notes)s      Note, r"""A double gamma continuous random variable.      The double gamma distributio, r"""A folded Cauchy continuous random variable.      %(before_notes)s      Notes (+4 more)

### Community 21 - "Community 21"
Cohesion: 0.07
Nodes (64): barthann(), bartlett(), blackman(), blackmanharris(), bohman(), boxcar(), chebwin(), cosine() (+56 more)

### Community 22 - "Community 22"
Cohesion: 0.06
Nodes (20): dedent_lines(), NumpyDocString, ObjDoc, Parses a numpydoc string to an abstract representation      Instances define a m, Remove leading and trailing blank lines from a list of lines, # NOTE: param line with single element should never have a, A line-based string reader., Parameters         ----------         data : str            String with lines se (+12 more)

### Community 23 - "Community 23"
Cohesion: 0.19
Nodes (57): SparseABC, sparray, isspmatrix(), Base class for sparse matrices, Reverses the dimensions of the sparse array/matrix.          Parameters, Element-wise complex conjugation.          If the array/matrix is of non-complex, Nonzero indices of the array/matrix.          Returns         -------         ro, Returns a copy of column j of the array, as an (m x 1) sparse         array (col (+49 more)

### Community 24 - "Community 24"
Cohesion: 0.05
Nodes (39): BaseQuadraticSubproblem, BaseQuadraticSubproblem, DoglegSubproblem, _minimize_dogleg(), Dog-leg trust-region optimization., Minimization of scalar function of one or more variables using     the dog-leg t, Quadratic subproblem solved by the dogleg method, The Cauchy point is minimal along the direction of steepest descent. (+31 more)

### Community 25 - "Community 25"
Cohesion: 0.06
Nodes (54): _all_partitions_concatenated(), _batch_generator(), _bca_interval(), bootstrap(), _bootstrap_iv(), _bootstrap_resample(), _calculate_null_both(), _calculate_null_pairings() (+46 more)

### Community 26 - "Community 26"
Cohesion: 0.05
Nodes (31): CensoredData, The number of values (censored and not censored)., Number of censored values.          Returns         -------         int, Create a `CensoredData` instance of right-censored data.          Parameters, Create a `CensoredData` instance of left-censored data.          Parameters, Create a `CensoredData` instance of interval-censored data.          This method, This function is used when a non-censored version of the data         is needed, Return a subset of self containing the values that are in         (or overlap wi (+23 more)

### Community 27 - "Community 27"
Cohesion: 0.05
Nodes (32): FixedRule, NestedFixedRule, _apply_fixed_rule(), _cached_cast(), _cartesian_product(), FixedRule, NestedFixedRule, ProductNestedFixed (+24 more)

### Community 28 - "Community 28"
Cohesion: 0.08
Nodes (10): _block_diag(), _convert_to_2d(), _coo_base, _extract_block_diag(), _get_dense_data_and_coords(), _get_sparse_data_and_coords(), isspmatrix_coo(), _process_axes() (+2 more)

### Community 29 - "Community 29"
Cohesion: 0.05
Nodes (16): _check_fit_input_parameters(), FitDataError, FitUniformFixedScaleDataError, _get_left_bracket(), pareto_gen, r"""A uniform continuous random variable.      %(before_notes)s      Notes     -, Maximum likelihood estimate for the location and scale parameters.          `uni, Create a new distribution using the given histogram          Parameters (+8 more)

### Community 30 - "Community 30"
Cohesion: 0.07
Nodes (41): coerce(), make_system(), Make a linear system Ax=b      Parameters     ----------     A : LinearOperator, _compute_cost_div_m(), _compute_p_max(), _condition_3_13(), _exact_1_norm(), _exact_inf_norm() (+33 more)

### Community 31 - "Community 31"
Cohesion: 0.06
Nodes (42): _array_newton(), bisect(), brenth(), brentq(), _compute_divided_differences(), _interpolated_poly(), _inverse_poly_zero(), newton() (+34 more)

### Community 32 - "Community 32"
Cohesion: 0.11
Nodes (51): bispeu(), bispev(), clocur(), curfit(), dblint(), fpader(), fpback(), fpbacp() (+43 more)

### Community 33 - "Community 33"
Cohesion: 0.06
Nodes (39): fmin_l_bfgs_b(), LbfgsInvHessProduct, _minimize_lbfgsb(), Functions --------- .. autosummary::    :toctree: generated/      fmin_l_bfgs_b, Minimize a scalar function of one or more variables using the L-BFGS-B     algor, Linear operator for the L-BFGS approximate inverse Hessian.      This operator c, Construct the operator., Efficient matrix-vector multiply with the BFGS matrices.          This calculati (+31 more)

### Community 34 - "Community 34"
Cohesion: 0.04
Nodes (1): r""" Parameters used in test and benchmark methods.  Collections of test cases s

### Community 35 - "Community 35"
Cohesion: 0.07
Nodes (52): chyp1f1_wrap(), special_cairy(), special_cairye(), special_ccyl_bessel_i(), special_ccyl_bessel_ie(), special_ccyl_bessel_j(), special_ccyl_bessel_je(), special_ccyl_bessel_k() (+44 more)

### Community 36 - "Community 36"
Cohesion: 0.06
Nodes (26): approximate_taylor_polynomial(), barycentric_interpolate(), BarycentricInterpolator, _Interpolator1D, _Interpolator1DWithDerivatives, _isscalar(), krogh_interpolate(), KroghInterpolator (+18 more)

### Community 37 - "Community 37"
Cohesion: 0.06
Nodes (34): _br(), _calculate_winsorized_variance(), _compute_qth_percentile(), _equal_var_ttest_denom(), f_oneway(), _f_oneway_is_too_small(), fisher_exact(), _fisher_exact_monte_carlo_method() (+26 more)

### Community 38 - "Community 38"
Cohesion: 0.07
Nodes (29): ArpackError, ArpackNoConvergence, _ArpackParams, choose_ncv(), eigs(), eigsh(), _fast_spmatrix_to_csc(), get_inv_matvec() (+21 more)

### Community 39 - "Community 39"
Cohesion: 0.04
Nodes (1): Delegators for alternative backends in scipy.ndimage.  The signature of `func_si

### Community 40 - "Community 40"
Cohesion: 0.08
Nodes (2): _cs_matrix, _process_slice()

### Community 41 - "Community 41"
Cohesion: 0.05
Nodes (4): log(), Distribution with a standard shift/scale transformation., r"""Natural logarithm of a non-negative random variable.      Parameters     ---, ShiftedScaledDistribution

### Community 42 - "Community 42"
Cohesion: 0.05
Nodes (21): multivariate_normal_frozen, multivariate_normal_gen, Computes the differential entropy of the multivariate normal.          Returns, Draw random samples from a matrix normal distribution.          Parameters, Check whether x lies in the support of the distribution., r"""     A multivariate normal random variable.      The `mean` keyword specifie, Draw random samples from a Multinomial distribution.          Parameters, Create a frozen multivariate normal distribution.          See `multivariate_nor (+13 more)

### Community 43 - "Community 43"
Cohesion: 0.07
Nodes (29): array_size(), backend_for_each_domain(), backend_for_each_domain_string(), backend_validate_ua_domain(), call(), canonicalize_args(), canonicalize_kwargs(), clear() (+21 more)

### Community 44 - "Community 44"
Cohesion: 0.08
Nodes (39): _briggs_helper_function(), _fractional_matrix_power(), _fractional_power_pade(), _fractional_power_pade_constant(), _fractional_power_superdiag_entry(), FractionalMatrixPowerError, _inverse_squaring_helper(), _logm() (+31 more)

### Community 45 - "Community 45"
Cohesion: 0.07
Nodes (43): binary_closing(), binary_dilation(), _binary_erosion(), binary_fill_holes(), binary_hit_or_miss(), binary_opening(), binary_propagation(), black_tophat() (+35 more)

### Community 46 - "Community 46"
Cohesion: 0.09
Nodes (3): _ProbabilityDistribution, Mixture, r"""Representation of a mixture distribution.      A mixture distribution is the

### Community 47 - "Community 47"
Cohesion: 0.05
Nodes (41): broadcast_shapes(), check_shape(), convert_pydata_sparse_to_scipy(), downcast_intp_index(), get_index_dtype(), get_sum_dtype(), getdata(), getdtype() (+33 more)

### Community 48 - "Community 48"
Cohesion: 0.05
Nodes (37): factorized(), _get_umf_family(), is_sptriangular(), MatrixRankWarning, Get umfpack family string given the sparse matrix dtype., Solve the sparse linear system Ax=b, where b may be a vector or a matrix.      P, Warning for exactly singular matrices., Select default sparse direct solver to be used.      Parameters     ---------- (+29 more)

### Community 49 - "Community 49"
Cohesion: 0.06
Nodes (42): center_of_mass(), extrema(), find_objects(), histogram(), label(), labeled_comprehension(), maximum(), maximum_position() (+34 more)

### Community 50 - "Community 50"
Cohesion: 0.07
Nodes (41): _asarray_square(), coshm(), cosm(), _ell(), _eq_10_42(), _exp_sinch(), fractional_matrix_power(), _fragment_2_1() (+33 more)

### Community 51 - "Community 51"
Cohesion: 0.13
Nodes (43): algdiv(), alngam(), alnrel(), apser(), basym(), bcorr(), betaln(), bfrac() (+35 more)

### Community 52 - "Community 52"
Cohesion: 0.05
Nodes (21): matrix_t_frozen, multivariate_t_frozen, multivariate_t_gen, _PSD, Determine if input dimensions can be marginalized.      Parameters     ---------, Compute coordinated functions of a symmetric positive semidefinite matrix., r"""     A multivariate t-distributed random variable.      The `loc` parameter, Initialize a multivariate t-distributed random variable.          Parameters (+13 more)

### Community 53 - "Community 53"
Cohesion: 0.08
Nodes (39): align_vectors(), _align_vectors_fixed(), apply(), approx_equal(), as_davenport(), as_euler(), as_quat(), as_rotvec() (+31 more)

### Community 54 - "Community 54"
Cohesion: 0.06
Nodes (37): all_of_type(), clear_backends(), create_multimethod(), determine_backend(), determine_backend_multi(), Dispatchable, generate_multimethod(), get_defaults() (+29 more)

### Community 55 - "Community 55"
Cohesion: 0.09
Nodes (41): _as_float_array(), _augknt(), _convert_string_aliases(), _diff_dual_poly(), _dual_poly(), fpcheck(), _get_dtype(), _handle_lhs_derivatives() (+33 more)

### Community 56 - "Community 56"
Cohesion: 0.07
Nodes (30): _cdf_single_value_piecewise_post_rounding_Z0(), _cdf_single_value_piecewise_Z0(), _cdf_single_value_piecewise_Z1(), _cf(), _fitstart_S0(), _fitstart_S1(), levy_stable_frozen, levy_stable_gen (+22 more)

### Community 57 - "Community 57"
Cohesion: 0.05
Nodes (4): _cs_matrix, _csc_base, isspmatrix_csc(), _csr_base

### Community 58 - "Community 58"
Cohesion: 0.07
Nodes (25): bicg(), bicgstab(), cg(), cgs(), _get_atol_rtol(), gmres(), qmr(), A helper function to handle tolerance normalization (+17 more)

### Community 59 - "Community 59"
Cohesion: 0.07
Nodes (21): AdaptiveStepsize, basinhopping(), BasinHoppingRunner, Metropolis, MinimizerWrapper, RandomDisplacement, basinhopping: The basinhopping global optimization algorithm, Do one Monte Carlo iteration          Randomly displace the coordinates, minimiz (+13 more)

### Community 60 - "Community 60"
Cohesion: 0.05
Nodes (40): _dispatch(), fft(), fft2(), fftn(), hfft(), hfft2(), hfftn(), ifft() (+32 more)

### Community 61 - "Community 61"
Cohesion: 0.08
Nodes (4): IndexMixin, isspmatrix_lil(), _lil_base, _prepare_index_for_memoryview()

### Community 62 - "Community 62"
Cohesion: 0.06
Nodes (22): Draw random samples from S(N-1).          Parameters         ----------, Private method to generate uniform directions     Reference: Marsaglia, G. (1972, r"""     A von Mises-Fisher variable.      The `mu` keyword specifies the mean d, Create a frozen von Mises-Fisher distribution.          See `vonmises_fisher_fro, Infer dimensionality from mu and ensure that mu is a one-dimensional         uni, Log of the von Mises-Fisher probability density function.          As this funct, Log of the von Mises-Fisher probability density function.          Parameters, Von Mises-Fisher probability density function.          Parameters         ----- (+14 more)

### Community 63 - "Community 63"
Cohesion: 0.07
Nodes (20): _dirichlet_check_input(), _dirichlet_check_parameters(), dirichlet_frozen, dirichlet_gen, _eigvalsh_to_eps(), _lnB(), _pinv_1d(), A helper function for computing the pseudoinverse.      Parameters     --------- (+12 more)

### Community 64 - "Community 64"
Cohesion: 0.06
Nodes (18): _AdjointMatrixOperator, aslinearoperator(), _get_dtype(), MatrixLinearOperator, _PowerLinearOperator, Abstract linear algebra library.  This module defines a class hierarchy that imp, Representing ``alpha * A``, Representing ``A ** p`` (+10 more)

### Community 65 - "Community 65"
Cohesion: 0.10
Nodes (3): _ConstraintWrapper, differential_evolution(), DifferentialEvolutionSolver

### Community 66 - "Community 66"
Cohesion: 0.06
Nodes (28): _default_response_times(), dimpulse(), dlsim(), dstep(), impulse(), lsim(), lti, r"""     Continuous-time linear time invariant system base class.      Parameter (+20 more)

### Community 67 - "Community 67"
Cohesion: 0.08
Nodes (28): call_minpack(), check_jac_sparsity(), check_tolerance(), check_x_scale(), construct_loss_function(), least_squares(), prepare_bounds(), Generic interface for least-squares minimization. (+20 more)

### Community 68 - "Community 68"
Cohesion: 0.07
Nodes (29): PearsonRResultBase, BootstrapMethod, Configuration information for a bootstrap confidence interval.      Instances of, pearsonr(), _pearsonr_bootstrap_ci(), _pearsonr_fisher_ci(), PearsonRResult, pointbiserialr() (+21 more)

### Community 69 - "Community 69"
Cohesion: 0.05
Nodes (20): If set, add linear phase `phase_shift` / `mfft` * `f` to each FFT         slice, The absolute value of the phase shift needs to be less than mfft         samples, Check if STFT is invertible.          This is achieved by trying to calculate th, Factor to multiply the STFT values by to scale each frequency slice         to a, Factor to multiply the STFT values by to scale each frequency slice         to a, Number of samples in window `win`.          Note that the FFT can be oversampled, Center index of window `win`.          For odd `m_num`, ``(m_num - 1) / 2`` is r, Smallest signal index and slice index due to padding.           Since, per conve (+12 more)

### Community 70 - "Community 70"
Cohesion: 0.10
Nodes (20): CanonicalConstraint, initial_constraints_as_canonical(), Convert initial values of the constraints to the canonical format.      The purp, Create an instance from `PreparedConstrained` object., Canonical constraint to use with trust-constr algorithm.      It represents the, Create an "empty" instance.          This "empty" instance is required to allow, Concatenate multiple `CanonicalConstraint` into one.          `sparse_jacobian`, HessianLinearOperator (+12 more)

### Community 71 - "Community 71"
Cohesion: 0.06
Nodes (17): _get_xp_ppoly_cls(), _PPoly, Returns ppoly class to delegate to for xp along with internal array namespace., Piecewise polynomial in the power basis.      The polynomial between ``x[i]`` an, Construct the piecewise polynomial without making checks.          Takes the sam, Add additional breakpoints and coefficients to the polynomial.          Paramete, Evaluate the piecewise polynomial or its derivative.          Parameters, Construct a new piecewise polynomial representing the derivative.          Param (+9 more)

### Community 72 - "Community 72"
Cohesion: 0.08
Nodes (14): expm(), _ExpmPadeHelper, _is_upper_triangular(), MatrixPowerOperator, _onenormest_matrix_power(), A matrix product that knows about sparse and structured matrices.      Parameter, Compute the matrix exponential of an array.      Array argument(s) of this funct, Efficiently estimate the 1-norm of A^p.      Parameters     ----------     A : n (+6 more)

### Community 73 - "Community 73"
Cohesion: 0.09
Nodes (30): DCSRCH, dcstep(), Parameters     ----------     phi : callable phi(alpha)         Function at poin, Parameters         ----------         alpha1 : float             alpha1 is the c, Parameters         ----------         stp : float             The current estima, Subroutine dcstep      This subroutine computes a safeguarded step for a search, _check_c1_c2(), _cubicmin() (+22 more)

### Community 74 - "Community 74"
Cohesion: 0.07
Nodes (18): r"""     Linear Time Invariant system in state-space form.      Represents the s, Create new StateSpace object and settle inheritance., Initialize the state space lti/dlti system., Return representation of the `StateSpace` system., Post-multiply another system or a scalar          Handles multiplication of syst, Pre-multiply a scalar or matrix (but not StateSpace), Negate the system (equivalent to pre-multiplying by -1)., Adds two systems in the sense of frequency domain addition. (+10 more)

### Community 75 - "Community 75"
Cohesion: 0.06
Nodes (17): gaussian_kde, _get_output_dtype(), Evaluate the estimated pdf on a set of points.          Parameters         -----, Multiply estimated density by a multivariate Gaussian and integrate         over, Computes the integral of a 1D pdf between two bounds.          Parameters, Computes the integral of a pdf over a rectangular interval.          Parameters, Representation of a kernel-density estimate using Gaussian kernels.      Kernel, Computes the integral of the product of this  kernel density estimate         wi (+9 more)

### Community 76 - "Community 76"
Cohesion: 0.07
Nodes (20): _array_like(), _as_inexact(), asjacobian(), InverseJacobian, Jacobian, NoConvergence, _nonlin_line_search(), nonlin_solve() (+12 more)

### Community 77 - "Community 77"
Cohesion: 0.06
Nodes (23): ClusterWarning, is_isomorphic(), leaders(), maxdists(), maxRstat(), Set list of matplotlib color codes for use by dendrogram.      Note that this pa, Determine if two different cluster assignments are equivalent.      Parameters, Return the maximum distance between any non-singleton cluster.      Parameters (+15 more)

### Community 78 - "Community 78"
Cohesion: 0.06
Nodes (32): block_diag(), circulant(), companion(), convolution_matrix(), dft(), fiedler(), fiedler_companion(), hadamard() (+24 more)

### Community 79 - "Community 79"
Cohesion: 0.07
Nodes (20): Arg, assert_mpmath_equal(), ComplexArg, exception_to_nan(), FixedArg, get_args(), inf_to_nan(), IntArg (+12 more)

### Community 80 - "Community 80"
Cohesion: 0.08
Nodes (15): NA_NewArray(), NI_ObjectToInputArray(), NI_ObjectToInputOutputArray(), NI_ObjectToOptionalInputArray(), NI_ObjectToOptionalOutputArray(), NI_ObjectToOutputArray(), Py_BinaryErosion(), Py_BinaryErosion2() (+7 more)

### Community 81 - "Community 81"
Cohesion: 0.10
Nodes (28): add_knot(), Bunch, disc(), F, Fperiodic, fprati(), generate_knots(), _generate_knots_impl() (+20 more)

### Community 82 - "Community 82"
Cohesion: 0.09
Nodes (33): _arg_peaks_as_expected(), _arg_wlen_as_expected(), _arg_x_as_expected(), argrelextrema(), argrelmax(), argrelmin(), _boolrelextrema(), _filter_ridge_lines() (+25 more)

### Community 83 - "Community 83"
Cohesion: 0.08
Nodes (1): _dok_base

### Community 84 - "Community 84"
Cohesion: 0.06
Nodes (17): ========================================= Clustering package (:mod:`scipy.cluste, r""" ================================== Constants (:mod:`scipy.constants`) =====, r""" Compressed sparse graph routines (:mod:`scipy.sparse.csgraph`) ============, ================================ Datasets (:mod:`scipy.datasets`) ==============, ============================================================== Finite Difference, Linear Solvers ==============  The default solver is SuperLU (included in the sc, FFT backend using pyduccfft, Sparse Eigenvalue Solvers -------------------------  The submodules of sparse.li (+9 more)

### Community 85 - "Community 85"
Cohesion: 0.08
Nodes (14): _BPoly, _get_xp_bpoly_cls(), Returns bpoly class to delegate to for xp along with internal array namespace., Piecewise polynomial in the Bernstein basis.      The polynomial between ``x[i]`, Add additional breakpoints and coefficients to the polynomial.          Paramete, Evaluate the piecewise polynomial or its derivative.          Parameters, Construct a new piecewise polynomial representing the derivative.          Param, Construct a new piecewise polynomial representing the antiderivative.          P (+6 more)

### Community 86 - "Community 86"
Cohesion: 0.08
Nodes (29): cdf2rdf(), _check_format_errors_warnings(), _check_info(), _check_select(), eig(), eig_banded(), eigh(), eigh_tridiagonal() (+21 more)

### Community 87 - "Community 87"
Cohesion: 0.09
Nodes (3): _minmax_mixin, _bsr_base, isspmatrix_bsr()

### Community 88 - "Community 88"
Cohesion: 0.09
Nodes (31): _coeff_smooth(), collapse_2d(), compute_root_from_lambda(), cspline1d(), cspline1d_eval(), cspline2d(), _cubic(), _cubic_coeff() (+23 more)

### Community 89 - "Community 89"
Cohesion: 0.08
Nodes (17): _promote(), Apply this rotation to a set of vectors.          If the original frame rotates, Compose this rotation with the other.          If `p` and `q` are two rotations,, Compose this rotation with itself `n` times.          Composition of a rotation, Determine if another rotation is approximately equal to this one.          Equal, Get the mean of the rotations.          The mean used is the chordal L2 mean (al, Get identity rotation(s).          Composition with the identity rotation has no, Estimate a rotation to optimally align two sets of vectors.          Find a rota (+9 more)

### Community 90 - "Community 90"
Cohesion: 0.09
Nodes (30): BVPResult, collocation_fun(), compute_jac_indices(), construct_global_jac(), create_spline(), estimate_bc_jac(), estimate_fun_jac(), estimate_rms_residuals() (+22 more)

### Community 91 - "Community 91"
Cohesion: 0.10
Nodes (9): Bivariate spline approximation over a rectangular mesh.      Can be used for bot, Wrapper for regrid with iopt=0 (smoothing spline on rectangular grid).     Retur, RectBivariateSpline, _regrid_smth(), interpn(), Interpolation at coordinates.          Parameters         ----------         xi, Multidimensional interpolation on regular or rectilinear grids.      Strictly sp, Interpolator of specified order on a rectilinear grid in N ≥ 1 dimensions. (+1 more)

### Community 92 - "Community 92"
Cohesion: 0.07
Nodes (12): _ProductLinearOperator, Representing ``A @ B``, Default matrix-matrix multiplication handler.          If ``self`` is a linear o, Default matrix-vector multiplication handler.          If ``self`` is a linear o, Matrix-vector multiplication.          Applies ``A`` to `x`, where ``A`` is an `, Adjoint matrix-vector multiplication.          Applies ``A^H`` to `x`, where ``A, Default implementation of `_rmatvec`.         Defers to `_rmatmat` or `adjoint`., Matrix-matrix multiplication.          Performs the operation ``A @ X`` where `` (+4 more)

### Community 93 - "Community 93"
Cohesion: 0.07
Nodes (4): ifill(), ilu_set_default_options(), set_default_options(), super_stats()

### Community 94 - "Community 94"
Cohesion: 0.07
Nodes (8): exp(), _log_real_standardize(), Standardizes the (complex) logarithm of a real number.      The logarithm of a r, Truncated distribution., Truncate the support of a random variable.      Given a random variable `X`, `tr, r"""Natural exponential of a random variable.      Parameters     ----------, truncate(), TruncatedDistribution

### Community 95 - "Community 95"
Cohesion: 0.12
Nodes (14): BarrierSubproblem, Trust-region interior point method.  References ---------- .. [1] Byrd, Richard, Returns scaling vector.         Given by:             scaling = [ones(n_vars), s, Returns scaled gradient.          Return scaled gradient:             gradient =, Assemble sparse Jacobian given its components.          Given ``J_eq``, ``J_ineq, Returns Lagrangian Hessian (in relation to `x`) -> Hx, Returns scaled Lagrangian Hessian (in relation to`s`) -> S Hs S, Barrier optimization problem:         minimize fun(x) - barrier_parameter*sum(lo (+6 more)

### Community 96 - "Community 96"
Cohesion: 0.08
Nodes (16): _Bunch, DoubleInfiniteFunc, LRUDict, quad_vec(), _quadrature_gk(), _quadrature_gk15(), _quadrature_gk21(), _quadrature_trapezoid() (+8 more)

### Community 97 - "Community 97"
Cohesion: 0.14
Nodes (21): OdeSolution, Continuous ODE solution.      It is organized as a collection of `DenseOutput` o, Evaluate the solution.          Parameters         ----------         t : float, Suite of ODE solvers implemented in Python., find_active_events(), handle_events(), OdeResult, prepare_events() (+13 more)

### Community 98 - "Community 98"
Cohesion: 0.11
Nodes (14): dual_annealing(), EnergyState, LocalSearchWrapper, ObjectiveFunWrapper, Formula Visita from p. 405 of reference [2], Class used to record the energy state. At any time, it knows what is the     cur, Initialize current location is the search domain. If `x0` is not         provide, Class used to generate new coordinates based on the distorted     Cauchy-Lorentz (+6 more)

### Community 99 - "Community 99"
Cohesion: 0.07
Nodes (24): MemoizeDer, Unified interfaces to root finding algorithms for real or complex scalar functio, Decorator that caches the value and derivative(s) of function each     time it i, r"""     Options     -------     args : tuple, optional         Extra arguments, r"""Calculate f or use cached value if available, r"""     Options     -------     args : tuple, optional         Extra arguments, r"""     Options     -------     args : tuple, optional         Extra arguments, r"""     Options     -------     args : tuple, optional         Extra arguments (+16 more)

### Community 100 - "Community 100"
Cohesion: 0.07
Nodes (18): Returns the discretized `TransferFunction` system.          Parameters         -, r"""     Discrete-time Linear Time Invariant system in transfer function form., Convert system representation to `TransferFunction`.          Returns         --, Convert system representation to `TransferFunction`.          Parameters, r"""Linear Time Invariant system class in transfer function form.      Represent, Handle object conversion if input is an instance of lti., Initialize the state space LTI system., Return representation of the system's transfer function (+10 more)

### Community 101 - "Community 101"
Cohesion: 0.07
Nodes (18): r"""     Linear Time Invariant system class in zeros, poles, gain form.      Rep, Handle object conversion if input is an instance of `lti`, Initialize the zeros, poles, gain system., Return representation of the `ZerosPolesGain` system., Zeros of the `ZerosPolesGain` system., Poles of the `ZerosPolesGain` system., Gain of the `ZerosPolesGain` system., Copy the parameters of another `ZerosPolesGain` system.          Parameters (+10 more)

### Community 102 - "Community 102"
Cohesion: 0.09
Nodes (29): check_COLA(), check_NOLA(), coherence(), csd(), _fft_helper(), istft(), lombscargle(), _median_bias() (+21 more)

### Community 103 - "Community 103"
Cohesion: 0.17
Nodes (29): addConstraint(), coercex(), daxpy1(), dcopy1(), ddot1(), diagonalScaling(), dneg1(), dnrm21() (+21 more)

### Community 104 - "Community 104"
Cohesion: 0.07
Nodes (15): Rotation in 3 dimensions.      This class provides an interface to initialize fr, Represent as rotation matrix.          3D rotations can be represented using rot, Represent as Euler angles.          Any orientation can be expressed as a compos, Represent as Davenport angles.          Any orientation can be expressed as a co, Represent as Modified Rodrigues Parameters (MRPs).          MRPs are a 3 dimensi, Get the magnitude(s) of the rotation(s).          Returns         -------, Create a 3D rotation group.          Parameters         ----------         group, Extract rotation(s) at given index(es) from object.          Create a new `Rotat (+7 more)

### Community 105 - "Community 105"
Cohesion: 0.13
Nodes (17): dqagie(), dqagpe(), dqagse(), dqawce(), dqawfe(), dqawoe(), dqawse(), dqc25c() (+9 more)

### Community 106 - "Community 106"
Cohesion: 0.10
Nodes (14): _BSpline, _get_xp_bspline_cls(), _insert(), Return a B-spline representing the derivative.          Parameters         -----, Return a B-spline representing the antiderivative.          Parameters         -, Insert a new knot at `x` of multiplicity `m`.          Given the knots and coeff, Insert a single knot at `xval`., NumPy Backend for BSpline.      The public BSpline class below is set up to dele (+6 more)

### Community 107 - "Community 107"
Cohesion: 0.10
Nodes (15): _curfit(), InterpolatedUnivariateSpline, LSQUnivariateSpline, 1-D interpolating spline for a given set of data points.      .. legacy:: class, 1-D spline with explicit internal knots.      .. legacy:: class          Specifi, 1-D smoothing spline fit to a given set of data points.      .. legacy:: class, Wrapper for curfit that provides a simpler interface.      iopt=0: find smoothin, Construct a spline object from given tck (+7 more)

### Community 108 - "Community 108"
Cohesion: 0.07
Nodes (12): multinomial_frozen, multinomial_gen, r"""     A multinomial random variable.      Parameters     ----------     %(_do, Create a frozen multinomial distribution.          See `multinomial_frozen` for, Returns: n_, p_, npcond.          n_ and p_ are arrays of the correct shape; npc, Returns: x_, xcond.          x_ is an int array; xcond is a boolean array flaggi, Log of the Multinomial probability mass function.          Parameters         --, Multinomial probability mass function.          Parameters         ---------- (+4 more)

### Community 109 - "Community 109"
Cohesion: 0.11
Nodes (23): _ci_lower(), _ci_upper(), _conditional_oddsratio(), _conditional_oddsratio_ci(), _hypergeom_params_from_table(), _nc_hypergeom_mean_inverse(), odds_ratio(), OddsRatioResult (+15 more)

### Community 110 - "Community 110"
Cohesion: 0.11
Nodes (26): _chk_asarray(), describe(), friedmanchisquare(), _get_pvalue(), jarque_bera(), kruskal(), kurtosis(), kurtosistest() (+18 more)

### Community 111 - "Community 111"
Cohesion: 0.18
Nodes (27): BernoulliH(), binoexpand(), CMultiWalleniusNCHypergeometric(), CWalleniusNCHypergeometric(), Erf(), FallingFactorial(), findpars(), FloorLog2() (+19 more)

### Community 112 - "Community 112"
Cohesion: 0.11
Nodes (27): _append_contraction_marks(), _append_contraction_marks_sub(), _append_nonsingleton_leaf_node(), _append_singleton_leaf_node(), cophenet(), dendrogram(), _dendrogram_calculate_info(), from_mlab_linkage() (+19 more)

### Community 113 - "Community 113"
Cohesion: 0.10
Nodes (27): _basic_simpson(), _cached_roots_legendre(), cumulative_simpson(), _cumulative_simpson_equal_intervals(), _cumulative_simpson_unequal_intervals(), cumulative_trapezoid(), _cumulatively_sum_simpson_integrals(), fixed_quad() (+19 more)

### Community 114 - "Community 114"
Cohesion: 0.09
Nodes (11): AAA, _BarycentricRational, FloaterHormannInterpolator, Compute the poles of the rational approximation.          Returns         ------, Compute the residues of the poles of the approximation.          Returns, Compute the roots of the rational approximation.          Returns         ------, r"""     AAA real or complex rational approximation.      As described in [1]_,, Base class for barycentric representation of a rational function. (+3 more)

### Community 115 - "Community 115"
Cohesion: 0.09
Nodes (27): _autoscale(), _check_result(), _check_sparse_inputs(), _clean_inputs(), _display_summary(), _format_A_constraints(), _format_b_constraints(), _get_Abc() (+19 more)

### Community 116 - "Community 116"
Cohesion: 0.12
Nodes (14): Halton, Halton sequence.      Pseudo-random number generator that generalize the Van der, CustomDistPINV, FastGeneratorInversion, Support of the distribution.          Returns         -------         a, b : flo, Cumulative distribution function (CDF)          Parameters         ----------, Percent point function (inverse of `cdf`)          Parameters         ----------, Fast sampling by numerical inversion of the CDF for a large class of     continu (+6 more)

### Community 117 - "Community 117"
Cohesion: 0.10
Nodes (4): _data_matrix, _dia_base, _invert_index(), isspmatrix_dia()

### Community 118 - "Community 118"
Cohesion: 0.09
Nodes (20): Exception, odeint(), ODEintWarning, Warning raised during the execution of `odeint`., Integrate a system of ordinary differential equations.      .. note:: For new co, ParseError, _NoConvergence, ======================================== Special functions (:mod:`scipy.special` (+12 more)

### Community 119 - "Community 119"
Cohesion: 0.10
Nodes (23): bode(), Bunch, _KNV0(), _KNV0_loop(), _order_complex_poles(), place_poles(), ltisys -- a collection of classes and functions for modeling linear time invaria, r"""     Discrete-time Linear Time Invariant system in state-space form.      Re (+15 more)

### Community 120 - "Community 120"
Cohesion: 0.07
Nodes (4): burr_gen, fisk_gen, r"""A Burr (Type III) continuous random variable.      %(before_notes)s      See, r"""A Fisk continuous random variable.      The Fisk distribution is also known

### Community 121 - "Community 121"
Cohesion: 0.07
Nodes (5): invgauss_gen, r"""A Wald continuous random variable.      %(before_notes)s      Notes     ----, r"""An inverse Gaussian continuous random variable.      %(before_notes)s      N, Ref.: https://moser-isi.ethz.ch/docs/papers/smos-2012-10.pdf (eq. 9), wald_gen

### Community 122 - "Community 122"
Cohesion: 0.09
Nodes (20): anderson(), _anderson_simulate_pvalue(), bartlett(), false_discovery_control(), median_test(), mood(), _mood_statistic_no_ties(), _mood_statistic_with_ties() (+12 more)

### Community 123 - "Community 123"
Cohesion: 0.08
Nodes (24): _betai(), ks_1samp(), ks_2samp(), kstest(), linregress(), plotting_positions(), pointbiserialr(), An extension of scipy.stats._stats_py to support masked arrays (+16 more)

### Community 124 - "Community 124"
Cohesion: 0.09
Nodes (10): random_table_frozen, random_table_gen, r"""     Contingency tables from independent samples with fixed marginal sums., Create a frozen distribution of tables with given marginals.          See `rando, Log-probability of table to occur in the distribution.          Parameters, Probability of table to occur in the distribution.          Parameters         -, Mean of distribution of conditional tables.         %(_doc_mean_params)s, Draw random tables with fixed column and row marginals.          Parameters (+2 more)

### Community 125 - "Community 125"
Cohesion: 0.09
Nodes (24): K-means clustering and vector quantization (:mod:`scipy.cluster.vq`) ===========, ClusterError, _kmeans(), kmeans2(), _kpoints(), _kpp(), _krandinit(), _missing_raise() (+16 more)

### Community 126 - "Community 126"
Cohesion: 0.10
Nodes (13): interp1d, Interpolate a 1-D function (legacy).      .. legacy:: class          For a guide, Find nearest neighbor interpolated y_new = f(x_new)., Use previous/next neighbor of x_new, y_new = f(x_new)., Check the inputs for being in the bounds of the interpolated data.          Para, griddata(), NearestNDInterpolator, Convenience interface to N-D interpolation  .. versionadded:: 0.9 (+5 more)

### Community 127 - "Community 127"
Cohesion: 0.09
Nodes (26): bessel(), bilinear_zpk(), butter(), cheby1(), cheby2(), ellip(), iirdesign(), iirfilter() (+18 more)

### Community 128 - "Community 128"
Cohesion: 0.08
Nodes (23): ai_zeros(), assoc_laguerre(), bei_zeros(), beip_zeros(), ber_zeros(), bernoulli(), berp_zeros(), bi_zeros() (+15 more)

### Community 129 - "Community 129"
Cohesion: 0.08
Nodes (9): multivariate_hypergeom_frozen, multivariate_hypergeom_gen, r"""     A multivariate hypergeometric random variable.      Parameters     ----, Create a frozen multivariate_hypergeom distribution.          See `multivariate_, Log of the multivariate hypergeometric probability mass function.          Param, Multivariate hypergeometric probability mass function.          Parameters, Mean of the multivariate hypergeometric distribution.          Parameters, Variance of the multivariate hypergeometric distribution.          Parameters (+1 more)

### Community 130 - "Community 130"
Cohesion: 0.10
Nodes (12): DenseSuper_from_Numeric(), droprule_cvt(), droprule_one_cvt(), LU_to_csc(), LU_to_csc_matrix(), NCFormat_from_spMatrix(), newSuperLUObject(), NRFormat_from_spMatrix() (+4 more)

### Community 131 - "Community 131"
Cohesion: 0.11
Nodes (14): Akima1DInterpolator, CubicHermiteSpline, pchip_interpolate(), PchipInterpolator, prepare_input(), Interpolation algorithms using piecewise cubic polynomials., r"""PCHIP shape-preserving interpolator (C1 smooth).      ``x`` and ``y`` are ar, Prepare input for cubic spline interpolators.      All data are converted to num (+6 more)

### Community 133 - "Community 133"
Cohesion: 0.10
Nodes (25): _chk_asarray(), describe(), kurtosis(), kurtosistest(), mode(), moment(), normaltest(), Compute the trimmed maximum      This function computes the maximum value of an (+17 more)

### Community 134 - "Community 134"
Cohesion: 0.13
Nodes (21): apply(), as_exp_coords(), compose_transforms(), _compute_se3_exp_translation_transform(), _compute_se3_log_translation_transform(), _create_skew_matrix(), _create_transformation_matrix(), from_components() (+13 more)

### Community 135 - "Community 135"
Cohesion: 0.09
Nodes (21): cc_diff(), cs_diff(), diff(), hilbert(), ihilbert(), itilbert(), Differential and pseudo-differential operators., Return inverse h-Tilbert transform of a periodic sequence x.      If ``x_j`` and (+13 more)

### Community 136 - "Community 136"
Cohesion: 0.10
Nodes (13): ClusterNode, _order_cluster_tree(), The identifier of the target node.          For ``0 <= i < n``, `i` corresponds, The number of leaf nodes (original observations) belonging to         the cluste, Return a reference to the left child tree object.          Returns         -----, Return a reference to the right child tree object.          Returns         ----, Return True if the target node is a leaf.          Returns         -------, Perform pre-order traversal without recursive function calls.          When a le (+5 more)

### Community 137 - "Community 137"
Cohesion: 0.10
Nodes (22): Decorator, doc_replace(), docformat(), extend_notes_in_docstring(), filldoc(), indentcount_lines(), inherit_docstring_from(), Utilities to allow inserting docstring fragments for common parameters into func (+14 more)

### Community 138 - "Community 138"
Cohesion: 0.10
Nodes (21): _dhtm(), firls(), firwin(), firwin2(), firwin_2d(), kaiser_atten(), kaiser_beta(), kaiserord() (+13 more)

### Community 139 - "Community 139"
Cohesion: 0.13
Nodes (15): cast_order(), Func, generate_loop(), generate_ufuncs(), get_declaration(), iter_variants(), main(), Generate a UFunc loop function that calls a function given as its     data param (+7 more)

### Community 140 - "Community 140"
Cohesion: 0.13
Nodes (23): _clip_prob(), _kolmogn(), _kolmogn_DMTW(), _kolmogn_p(), _kolmogn_PelzGood(), _kolmogn_Pomeranz(), _kolmogni(), kolmognp() (+15 more)

### Community 141 - "Community 141"
Cohesion: 0.10
Nodes (24): brunnermunzel(), _chk_size(), count_tied_groups(), find_repeats(), friedmanchisquare(), _kendall_p_exact(), kendalltau(), kendalltau_seasonal() (+16 more)

### Community 142 - "Community 142"
Cohesion: 0.09
Nodes (21): compare_medians_ms(), hdmedian(), hdquantiles(), hdquantiles_sd(), idealfourths(), median_cihs(), mjci(), mquantiles_cimj() (+13 more)

### Community 143 - "Community 143"
Cohesion: 0.09
Nodes (4): geninvgauss_mode(), geninvgauss_pdf(), invgauss_mode(), invgauss_pdf()

### Community 144 - "Community 144"
Cohesion: 0.09
Nodes (18): brunnermunzel(), combine_pvalues(), kendalltau(), _order_ranks(), _pack_CorrelationResult(), rankdata(), ranksums(), Assign ranks to data, dealing with ties appropriately.      By default (``axis=N (+10 more)

### Community 145 - "Community 145"
Cohesion: 0.13
Nodes (18): _backends_kwargs_from_request(), check_fpu_mode(), devices(), pytest_configure(), Check FPU mode was not changed during the test., # NOTE: conftest.py is imported before its own ``pytest_configure`` runs, and, Run the test that uses this fixture on each available array API library.      Yo, Add pytest markers to avoid PytestUnknownMarkWarning      This needs to contain (+10 more)

### Community 146 - "Community 146"
Cohesion: 0.17
Nodes (22): _execute_1D(), _execute_nD(), fft(), fft2(), fftn(), hfft(), hfft2(), hfftn() (+14 more)

### Community 147 - "Community 147"
Cohesion: 0.10
Nodes (14): _build_evaluation_coefficients(), _build_system(), kernel_matrix(), kernel_vector(), polynomial_matrix(), polynomial_vector(), Build the system used to solve for the RBF interpolant coefficients.      Parame, Construct the coefficients needed to evaluate     the RBF.      Parameters     - (+6 more)

### Community 148 - "Community 148"
Cohesion: 0.13
Nodes (12): DenseOutput, Base class for local interpolant over step made by an ODE solver.      It interp, Evaluate the interpolant.          Parameters         ----------         t : flo, predict_factor(), Radau, RadauDenseOutput, Predict by which factor to increase/decrease the step size.      The algorithm i, Implicit Runge-Kutta method of Radau IIA family of order 5.      The implementat (+4 more)

### Community 149 - "Community 149"
Cohesion: 0.09
Nodes (8): Anderson, BroydenFirst, BroydenSecond, GenericBroyden, Find a root of a function, using (extended) Anderson mixing.      The Jacobian i, Collapse the low-rank matrix to a full-rank one., Find a root of a function, using Broyden's first Jacobian approximation.      Th, Find a root of a function, using Broyden\'s second Jacobian approximation.

### Community 150 - "Community 150"
Cohesion: 0.12
Nodes (10): _find_missing_index(), _minmax_mixin, Base class for sparse matrice with a .data attribute      subclasses must provid, Mixin for min and max methods.      These are not implemented for dia_matrix, he, Return the maximum of the array/matrix or maximum along an axis.          By def, Return the minimum of the array/matrix or maximum along an axis.          By def, Return the maximum, ignoring any Nans, along an axis.          Return the maximu, Return the minimum, ignoring any Nans, along an axis.          Return the minimu (+2 more)

### Community 151 - "Community 151"
Cohesion: 0.11
Nodes (20): _add_reduced_axes(), _axis_nan_policy_factory(), _broadcast_array_shapes_remove_axis(), _broadcast_arrays(), _broadcast_concatenate(), _broadcast_shapes(), _broadcast_shapes_remove_axis(), _check_empty_inputs() (+12 more)

### Community 152 - "Community 152"
Cohesion: 0.09
Nodes (17): Class which encapsulates common functionality between rv_discrete     and rv_con, rv_generic, anderson_ksamp(), _anderson_ksamp_continuous(), _anderson_ksamp_midrank(), _anderson_ksamp_right(), _BigFloat, fligner() (+9 more)

### Community 153 - "Community 153"
Cohesion: 0.09
Nodes (11): matrix_normal_frozen, matrix_normal_gen, r"""     A matrix normal random variable.      The `mean` keyword specifies the, Create a frozen matrix normal distribution.          See `matrix_normal_frozen`, Infer dimensionality from mean or covariance matrices. Handle         defaults., Adjust quantiles array so that last two axes labels the components of         ea, Log of the matrix normal probability density function.          Parameters, Log of the matrix normal probability density function.          Parameters (+3 more)

### Community 154 - "Community 154"
Cohesion: 0.11
Nodes (13): check_random_state(), LatinHypercube, QMCEngine, Reset the engine to base state.          Returns         -------         engine, Fast-forward the sequence by `n` positions.          Parameters         --------, r"""Latin hypercube sampling (LHS).      A Latin hypercube sample [1]_ generates, Turn `seed` into a `numpy.random.Generator` instance.      Parameters     ------, A generic Quasi-Monte Carlo sampler class meant for subclassing.      QMCEngine (+5 more)

### Community 155 - "Community 155"
Cohesion: 0.11
Nodes (22): discrepancy(), _ensure_in_unit_hypercube(), geometric_discrepancy(), _l1_norm(), _lloyd_centroidal_voronoi_tessellation(), _lloyd_iteration(), _perturb_discrepancy(), _random_cd() (+14 more)

### Community 156 - "Community 156"
Cohesion: 0.14
Nodes (19): _angular_acceleration_nonlinear_term(), _angular_rate_to_rotvec_dot_matrix(), _compute_angular_acceleration(), _compute_angular_rate(), _create_block_3_diagonal_matrix(), _create_skew_matrix(), _matrix_vector_product_of_stacks(), Compute the non-linear term in angular acceleration.      The angular accelerati (+11 more)

### Community 157 - "Community 157"
Cohesion: 0.11
Nodes (16): _check_obsolete(), ConstantWarning, find(), parse_constants_2002to2014(), parse_constants_2018toXXXX(), precision(), Fundamental Physical Constants ------------------------------  These constants a, Accessing a constant no longer in current CODATA data set. (+8 more)

### Community 158 - "Community 158"
Cohesion: 0.10
Nodes (21): c2c(), c2cn(), c2r(), c2rn(), hfft2(), ihfft2(), r2c(), r2cn() (+13 more)

### Community 159 - "Community 159"
Cohesion: 0.11
Nodes (12): _build_and_solve_system(), _build_evaluation_coefficients(), _build_system(), compute_interpolation(), kernel_matrix(), polynomial_matrix(), 'Generic' Array API backend for RBF interpolation.  The general logic is this: `, Evaluate RBFs, with centers at `x`, at `x`. (+4 more)

### Community 160 - "Community 160"
Cohesion: 0.15
Nodes (21): _C_contiguous_copy(), estimate_rank(), estimate_spectral_norm(), estimate_spectral_norm_diff(), id_to_svd(), interp_decomp(), _is_real(), Same as np.ascontiguousarray, but ensure a copy (+13 more)

### Community 161 - "Community 161"
Cohesion: 0.10
Nodes (10): FullHessianUpdateStrategy, Hessian update strategy with full dimensional internal representation., Initialize internal matrix.          Allocate internal memory for storing and up, Update internal matrix.          Update Hessian matrix or its inverse (depending, Compute the product of the internal matrix with the given vector.          Param, Return the current internal matrix.          Returns         -------         M :, Update the inverse Hessian matrix.          BFGS update using the formula:, Update the Hessian matrix.          BFGS update using the formula: (+2 more)

### Community 162 - "Community 162"
Cohesion: 0.17
Nodes (13): _check_dtype_and_flags(), convert_vec_status(), get_err_mesg(), _linalg_cholesky(), _linalg_det(), _linalg_eig(), _linalg_inv(), _linalg_lstsq() (+5 more)

### Community 163 - "Community 163"
Cohesion: 0.16
Nodes (11): _binary_search_for_binom_tst(), _binom_exact_conf_int(), _binom_wilson_conf_int(), binomtest(), BinomTestResult, Result of `scipy.stats.binomtest`.      Attributes     ----------     k : int, Compute the estimate and confidence interval for the binomial test.      Returns, Perform a test that the probability of success is p.      The binomial test [1]_ (+3 more)

### Community 164 - "Community 164"
Cohesion: 0.09
Nodes (4): erlang_gen, gamma_gen, r"""A gamma continuous random variable.      %(before_notes)s      See Also, An Erlang continuous random variable.      %(before_notes)s      See Also     --

### Community 165 - "Community 165"
Cohesion: 0.10
Nodes (4): r""" Update the numerical values of distribution parameters.          Parameters, r""" Checks whether the keyword arguments match the parameterization.          P, r""" Input validation / standardization of parameterization.          Parameters, TransformedDistribution

### Community 166 - "Community 166"
Cohesion: 0.14
Nodes (12): _get_mwu_z(), mannwhitneyu(), _MWU, _mwu_choose_method(), _mwu_input_validation(), Build all the array of frequencies for u from 0 to maxu.         Assumptions:, Standardized MWU statistic, Distribution of MWU statistic under the null hypothesis (+4 more)

### Community 167 - "Community 167"
Cohesion: 0.10
Nodes (22): Trims an array by masking the data outside some given limits.      Returns a mas, Trims an array by masking some proportion of the data on each end.     Returns a, Trims an array by masking the data outside some given limits.      Returns a mas, Trims the smallest and largest data values.      Trims the `data` by masking the, Trims the data by masking values from one tail.      Parameters     ----------, Returns the trimmed mean of the data along the given axis.      %s, Returns the trimmed variance of the data along the given axis.      %s     ddof, Returns the trimmed standard deviation of the data along the given axis.      %s (+14 more)

### Community 168 - "Community 168"
Cohesion: 0.11
Nodes (9): _dirichlet_multinomial_check_parameters(), dirichlet_multinomial_frozen, dirichlet_multinomial_gen, r"""     A Dirichlet multinomial random variable.      The Dirichlet multinomial, The log of the probability mass function.          Parameters         ----------, Probability mass function for a Dirichlet multinomial distribution.          Par, Mean of a Dirichlet multinomial distribution.          Parameters         ------, The variance of the Dirichlet multinomial distribution.          Parameters (+1 more)

### Community 169 - "Community 169"
Cohesion: 0.11
Nodes (8): normal_inverse_gamma_frozen, normal_inverse_gamma_gen, r"""     Normal-inverse-gamma distribution.      The normal-inverse-gamma distri, Draw random samples from the distribution.          Parameters         ---------, Log of the probability density function.          Parameters         ----------, The probability density function.          Parameters         ----------, The mean of the distribution.          Parameters         ----------         mu,, The variance of the distribution.          Parameters         ----------

### Community 170 - "Community 170"
Cohesion: 0.09
Nodes (2): Normal, r"""Normal distribution with prescribed mean and standard deviation.      The pr

### Community 171 - "Community 171"
Cohesion: 0.09
Nodes (2): r"""Standard normal distribution.      The probability density function of the s, StandardNormal

### Community 172 - "Community 172"
Cohesion: 0.16
Nodes (15): direct_dirchoose_(), direct_dirdivide_(), direct_dirget_i__(), direct_dirgetlevel_(), direct_dirgetmaxdeep_(), direct_dirinfcn_(), direct_dirinit_(), direct_dirinsertlist_() (+7 more)

### Community 173 - "Community 173"
Cohesion: 0.11
Nodes (19): _asfarray(), _datacopied(), _fix_shape(), _fix_shape_1d(), get_workers(), _init_nd_shape_and_axes(), _iterable_of_int(), _normalization() (+11 more)

### Community 174 - "Community 174"
Cohesion: 0.11
Nodes (10): NdPPoly, Piecewise tensor product polynomial.      The value at point ``xp = (x', y', z',, Construct the piecewise polynomial without making checks.          Takes the sam, Evaluate the piecewise polynomial or its derivative          Parameters, Compute 1-D derivative along a selected dimension in-place         May result to, Compute 1-D antiderivative along a selected dimension         May result to non-, Construct a new piecewise polynomial representing the derivative.          Param, Construct a new piecewise polynomial representing the antiderivative.          A (+2 more)

### Community 175 - "Community 175"
Cohesion: 0.14
Nodes (19): arg_casts(), generate_decl_c(), generate_decl_pxd(), generate_decl_pyx(), generate_file_c(), generate_file_pxd(), generate_file_pyx(), _get_pxd_preamble() (+11 more)

### Community 176 - "Community 176"
Cohesion: 0.11
Nodes (9): LaplacianNd, The grid Laplacian in ``N`` dimensions and its eigenvalues/eigenvectors.      Co, Compute `m` largest eigenvalues in each of the ``N`` directions,         i.e., u, Return the requested number of eigenvalues.          Parameters         --------, Return 1 eigenvector in 1d with index `j`         and number of grid points `n`, Return 1 eigenvector in Nd with multi-index `j`         as a tensor product of t, Return the requested number of eigenvectors for ordered eigenvalues.          Pa, Converts the Laplacian data to a dense array.          Returns         ------- (+1 more)

### Community 177 - "Community 177"
Cohesion: 0.13
Nodes (21): braycurtis(), canberra(), chebyshev(), cityblock(), hamming(), jaccard(), mahalanobis(), r"""     Compute the Chebyshev distance.      The *Chebyshev distance* between r (+13 more)

### Community 178 - "Community 178"
Cohesion: 0.21
Nodes (20): clear_mark(), colamd_get_debug(), COLAMD_MAIN(), COLAMD_recommended(), COLAMD_report(), COLAMD_set_defaults(), debug_deg_lists(), debug_mark() (+12 more)

### Community 179 - "Community 179"
Cohesion: 0.18
Nodes (18): check_array(), py_coloc(), py_coloc_nd(), py_data_matrix(), py_data_matrix_periodic(), py_evaluate_all_bspl(), py_evaluate_ndbspline(), py_evaluate_spline() (+10 more)

### Community 180 - "Community 180"
Cohesion: 0.21
Nodes (20): cdist(), cdist_impl(), cdist_unweighted(), cdist_weighted(), cdist_weighted_impl(), common_type(), dtype_num(), get_descriptor() (+12 more)

### Community 182 - "Community 182"
Cohesion: 0.20
Nodes (16): _back_substitute(), _coloc_matrix(), _coloc_nd(), _compute_residuals(), data_matrix(), data_matrix_periodic(), _deBoor_D(), _evaluate_ndbspline() (+8 more)

### Community 183 - "Community 183"
Cohesion: 0.17
Nodes (20): cnorm1(), cnorm1est(), dnorm1(), dnorm1est(), matrix_exponential_c(), matrix_exponential_d(), matrix_exponential_s(), matrix_exponential_z() (+12 more)

### Community 184 - "Community 184"
Cohesion: 0.10
Nodes (2): rv_frozen, # NOTE: To look at history using `git blame`, use `git blame -M -C -C`

### Community 185 - "Community 185"
Cohesion: 0.10
Nodes (13): PoissonDisk, r"""         Draw `n` integers from `l_bounds` (inclusive) to `u_bounds`, Poisson disk sampling.      Parameters     ----------     d : int         Dimens, Sampling pool and sample grid., Draw `n` in the interval ``[l_bounds, u_bounds]``.          Note that it can ret, Draw ``n`` samples in the interval ``[l_bounds, u_bounds]``.          Unlike `ra, Reset the engine to base state.          Returns         -------         engine, Uniform sampling within hypersphere. (+5 more)

### Community 186 - "Community 186"
Cohesion: 0.14
Nodes (20): _bvn(), _cbc_lattice(), _factorize_int(), _mvn_qmc_integrand(), _permuted_cholesky(), _primitive_root(), _qauto(), _qmvn() (+12 more)

### Community 187 - "Community 187"
Cohesion: 0.13
Nodes (21): alexandergovern(), _alexandergovern_input_validation(), AlexanderGovernResult, _demean(), gmean(), gstd(), hmean(), _linearized_pmean() (+13 more)

### Community 189 - "Community 189"
Cohesion: 0.18
Nodes (16): Binomial(), BinomialInver(), BinomialRatioOfUniforms(), fc_lnpk(), Hypergeometric(), HypInversionMod(), HypRatioOfUnifoms(), LnFac() (+8 more)

### Community 190 - "Community 190"
Cohesion: 0.11
Nodes (17): fft(), fft2(), fftn(), ifft(), ifft2(), ifftn(), irfft(), Discrete Fourier Transforms - _basic.py (+9 more)

### Community 191 - "Community 191"
Cohesion: 0.12
Nodes (17): dct(), dctn(), dst(), dstn(), idct(), idctn(), idst(), idstn() (+9 more)

### Community 192 - "Community 192"
Cohesion: 0.12
Nodes (19): _are_validate_args(), Matrix equation solver routines, Solves the continuous Lyapunov equation :math:`AX + XA^H = Q`.      Uses the Bar, Solves the discrete Lyapunov equation directly.      This function is called by, Solves the discrete Lyapunov equation using a bilinear transformation.      This, Solves the discrete Lyapunov equation :math:`AXA^H - X + Q = 0`.      Parameters, Computes a solution (X) to the Sylvester equation :math:`AX + XB = Q`.      Para, r"""     Solves the continuous-time algebraic Riccati equation (CARE).      The (+11 more)

### Community 193 - "Community 193"
Cohesion: 0.17
Nodes (17): affine_transform(), geometric_transform(), map_coordinates(), _prepad_for_spline_filter(), Multidimensional spline filter.      Parameters     ----------     %(input)s, Apply an arbitrary geometric transform.      The given mapping function is used, Map the input array to new coordinates by interpolation.      The array of coord, Apply an affine transformation.      Given an output image pixel index vector `` (+9 more)

### Community 194 - "Community 194"
Cohesion: 0.12
Nodes (7): rv_discrete_frozen, _parse_args(), poisson_binom_gen, poisson_binomial_frozen, # FIXME: problems sampling., r"""A Poisson Binomial discrete random variable.      %(before_notes)s      See, # FIXME: Fails _cdfvec

### Community 195 - "Community 195"
Cohesion: 0.11
Nodes (15): buttap(), cheb1ap(), cheb2ap(), gammatone(), _hz_to_erb(), iircomb(), r"""     Return a single transfer function from a series of second-order section, Return (z,p,k) for analog prototype of Nth-order Butterworth filter.      The fi (+7 more)

### Community 196 - "Community 196"
Cohesion: 0.13
Nodes (20): factorial(), factorial2(), factorialk(), _factorialx_approx_core(), _factorialx_array_approx(), _factorialx_array_exact(), _factorialx_wrapper(), _gamma1p() (+12 more)

### Community 197 - "Community 197"
Cohesion: 0.20
Nodes (19): active(), bmv(), cauchy(), cmprlb(), dcsrch(), dcstep(), errclb(), formk() (+11 more)

### Community 198 - "Community 198"
Cohesion: 0.25
Nodes (19): bnorm(), cfode(), ewset(), fnorm(), int_max(), int_min(), intdy(), lsoda() (+11 more)

### Community 199 - "Community 199"
Cohesion: 0.12
Nodes (1): DiscreteDistribution

### Community 200 - "Community 200"
Cohesion: 0.10
Nodes (11): Return the translation and rotation components of the transform,         where t, Return the exponential coordinates of the transform.          This implements th, Return the dual quaternion representation of the transform.          Unit dual q, Return the length of the leading transform dimension.          A transform can s, Extract transform(s) at given index(es) from this object.          Creates a new, Return the translation component of the transform.          A transform is a com, Whether this instance represents a single transform.          Single transforms, The shape of the transform's leading dimensions. (+3 more)

### Community 201 - "Community 201"
Cohesion: 0.13
Nodes (12): bisplev(), bisplrep(), dblint(), _int_overflow(), fitpack (dierckx in netlib) --- A Python-C wrapper to FITPACK (by P. Dierckx)., Cast the value to a dfitpack_int and raise an OverflowError if the value     can, Find a bivariate B-spline representation of a surface.      Given a set of data, Evaluate a bivariate B-spline and its derivatives.      Return a rank-2 array of (+4 more)

### Community 202 - "Community 202"
Cohesion: 0.11
Nodes (18): insert(), Find the B-spline representation of a 1-D curve.      .. legacy:: function, Find the B-spline representation of an N-D curve.      .. legacy:: function, Evaluate a B-spline or its derivatives.      .. legacy:: function          Speci, Evaluate the definite integral of a B-spline between two given points.      .. l, Find the roots of a cubic B-spline.      .. legacy:: function          Specifica, Evaluate a B-spline and all its derivatives at one point (or set of points) up, Insert knots into a B-spline.      .. legacy:: function          Specifically, w (+10 more)

### Community 203 - "Community 203"
Cohesion: 0.12
Nodes (16): chirp(), _chirp_phase(), gausspulse(), Return a Gaussian modulated sinusoid.      The formula for the returned signal i, Return a periodic sawtooth or triangle waveform.      The sawtooth waveform has, r"""Frequency-swept cosine generator.      In the following, 'Hz' should be inte, Calculate the phase used by `chirp` to generate its output.      See `chirp` for, Frequency-swept cosine generator, with a time-dependent frequency.      This fun (+8 more)

### Community 204 - "Community 204"
Cohesion: 0.15
Nodes (3): _data_matrix, This function performs element-wise power.          Parameters         ---------, _spbase

### Community 205 - "Community 205"
Cohesion: 0.15
Nodes (11): _betaincc(), _chdtr(), _chdtrc(), _FuncInfo, _get_native_func(), # IMPORTANT: this only works because all functions in this module, # IMPORTANT: map_blocks works only because all functions in this module, # IMPORTANT: these must all be **elementwise** functions! (+3 more)

### Community 206 - "Community 206"
Cohesion: 0.12
Nodes (4): random_double(), random_float(), rol64(), xoshiro256p()

### Community 210 - "Community 210"
Cohesion: 0.15
Nodes (12): library_call_nodata(), library_call_nonlocal(), library_call_simple(), test_call_nodata(), test_call_nonlocal(), test_call_simple(), test_plus1_callback(), test_plus1b_callback() (+4 more)

### Community 212 - "Community 212"
Cohesion: 0.12
Nodes (4): _log_gauss_mass(), Log of Gaussian probability mass within an interval, r"""A truncated normal continuous random variable.      %(before_notes)s      No, truncnorm_gen

### Community 213 - "Community 213"
Cohesion: 0.11
Nodes (2): r"""An upper truncated Pareto continuous random variable.      %(before_notes)s, truncpareto_gen

### Community 214 - "Community 214"
Cohesion: 0.11
Nodes (2): MonotonicTransformedDistribution, r"""Distribution underlying a strictly monotonic function of a random variable

### Community 215 - "Community 215"
Cohesion: 0.15
Nodes (14): dunnett(), DunnettResult, _iv_dunnett(), _params_dunnett(), _pvalue_dunnett(), Compute the confidence interval for the specified confidence level.          Par, Dunnett's test: multiple comparisons of means against a control group.      This, Result object returned by `scipy.stats.dunnett`.      Attributes     ---------- (+6 more)

### Community 216 - "Community 216"
Cohesion: 0.11
Nodes (2): Logistic, r"""Standard logistic distribution.      The probability density function of the

### Community 217 - "Community 217"
Cohesion: 0.11
Nodes (2): r"""Uniform distribution.      The probability density function of the uniform d, Uniform

### Community 218 - "Community 218"
Cohesion: 0.15
Nodes (18): box_intersections(), box_sphere_intersections(), eqp_kktfact(), inside_box_boundaries(), modified_dogleg(), projected_cg(), Equality-constrained quadratic programming solvers., Find the intersection between segment (or line) and box constraints.      Find t (+10 more)

### Community 219 - "Community 219"
Cohesion: 0.27
Nodes (16): cnaupd_wrap(), cneupd_wrap(), dnaupd_wrap(), dneupd_wrap(), dsaupd_wrap(), dseupd_wrap(), pack_dict_to_state_d(), pack_dict_to_state_s() (+8 more)

### Community 220 - "Community 220"
Cohesion: 0.19
Nodes (14): c2c(), c2c_internal(), c2c_sym_internal(), c2r_internal(), dct(), dct_internal(), dst(), dst_internal() (+6 more)

### Community 221 - "Community 221"
Cohesion: 0.11
Nodes (18): average(), centroid(), complete(), linkage(), median(), optimal_leaf_ordering(), Given a linkage matrix Z and distance, reorder the cut tree.      Parameters, Perform complete/max/farthest point linkage on a condensed distance matrix. (+10 more)

### Community 222 - "Community 222"
Cohesion: 0.11
Nodes (9): ode, A generic interface class to numeric integrators.      Solve an equation system, Set initial conditions y(t) = y., Find y=y(t), set y as an initial condition, and return y.          Parameters, Check if integration was successful., Extracts the return code for the integration to enable better control         if, Set extra parameters for user-supplied function f., Set extra parameters for user-supplied function jac. (+1 more)

### Community 223 - "Community 223"
Cohesion: 0.11
Nodes (10): _BivariateSplineBase, _DerivedBivariateSpline, Base class for Bivariate spline s(x,y) interpolation on the rectangle     [xb,xe, Construct a spline object from given tck and degree, Return weighted sum of squared residuals of the spline approximation.          T, Return a tuple (tx,ty) where tx,ty contain knots positions         of the spline, Return spline coefficients.          Returns         -------         1D array, Evaluate the spline or its derivatives at given positions.          Parameters (+2 more)

### Community 224 - "Community 224"
Cohesion: 0.16
Nodes (8): _assert_less(), _assert_matching_namespace(), Utility functions to use Python Array API compatible libraries.  For the context, _strict_check(), xp_assert_close_nulp(), xp_assert_equal(), xp_assert_less(), xp_assert_less_equal()

### Community 225 - "Community 225"
Cohesion: 0.15
Nodes (15): diagsvd(), _format_emit_errors_warnings(), null_space(), orth(), SVD decomposition functions., Format/emit errors/warnings from a lowlevel batched routine., Compute singular values of a matrix.      Parameters     ----------     a : (M,, Construct the sigma matrix in SVD from singular values and size M, N.      Param (+7 more)

### Community 226 - "Community 226"
Cohesion: 0.18
Nodes (16): _blocked_elementwise(), column_needs_resampling(), elementary_vector(), every_col_of_X_is_parallel_to_a_col_of_Y(), _max_abs_axis1(), onenormest(), _onenormest_core(), Sparse block 1-norm estimator. (+8 more)

### Community 227 - "Community 227"
Cohesion: 0.17
Nodes (17): _applyConstraints(), _as2d(), _b_orthonormalize(), _get_indx(), _handle_gramA_gramB_verbosity(), lobpcg(), _makeMatMat(), _matmul_inplace() (+9 more)

### Community 228 - "Community 228"
Cohesion: 0.11
Nodes (18): _cplxpair(), _cplxreal(), _nearest_real_complex_idx(), Sort into pairs of complex conjugates.      Complex conjugates in `z` are sorted, r"""Return zero, pole, gain (z, p, k) representation from a numerator,     denom, r"""     Return polynomial transfer function representation from zeros and poles, r"""     Return second-order sections from transfer function representation., Return zeros, poles, and gain of a series of second-order sections.      Paramet (+10 more)

### Community 229 - "Community 229"
Cohesion: 0.13
Nodes (4): innernode, leafnode, node, Create either an inner or leaf node, wrapping a cKDTreeNode instance

### Community 230 - "Community 230"
Cohesion: 0.20
Nodes (12): callocateA(), cexpand(), cLUMemInit(), cLUMemXpand(), cLUWorkInit(), cmemory_usage(), copy_mem_singlecomplex(), cSetupSpace() (+4 more)

### Community 231 - "Community 231"
Cohesion: 0.20
Nodes (12): copy_mem_double(), dallocateA(), dexpand(), dLUMemInit(), dLUMemXpand(), dLUWorkInit(), dmemory_usage(), doubleMalloc() (+4 more)

### Community 232 - "Community 232"
Cohesion: 0.29
Nodes (16): dogleg(), enorm(), fdjac1(), fdjac2(), HYBRD(), HYBRJ(), LMDER(), LMDIF() (+8 more)

### Community 233 - "Community 233"
Cohesion: 0.20
Nodes (12): copy_mem_float(), floatMalloc(), sallocateA(), sexpand(), sLUMemInit(), sLUMemXpand(), sLUWorkInit(), smemory_usage() (+4 more)

### Community 234 - "Community 234"
Cohesion: 0.20
Nodes (12): copy_mem_doublecomplex(), doublecomplexMalloc(), zallocateA(), zexpand(), zLUMemInit(), zLUMemXpand(), zLUWorkInit(), zmemory_usage() (+4 more)

### Community 235 - "Community 235"
Cohesion: 0.13
Nodes (18): _add_axis_labels_title(), boxcox_normplot(), _calc_uniform_order_statistic_medians(), _normplot(), _parse_dist_kw(), ppcc_max(), ppcc_plot(), probplot() (+10 more)

### Community 236 - "Community 236"
Cohesion: 0.11
Nodes (11): _cholesky_invwishart_rvs(), matrix_t_gen, r"""     A matrix t-random variable.      The `mean` keyword specifies the mean., Create a frozen matrix t distribution.          See `matrix_t_frozen` for more i, Infer dimensionality from mean or covariance matrices.         Handle defaults., Adjust quantiles array so that last two axes labels the component of         eac, Log of the matrix t probability density function.          Parameters         --, Log of the matrix normal probability density function.          Parameters (+3 more)

### Community 237 - "Community 237"
Cohesion: 0.12
Nodes (10): MultinomialQMC, Engine for generating (scrambled) Sobol' sequences.      Sobol' sequences are lo, Scramble the sequence using LMS+shift., Draw next point(s) in the Sobol' sequence.          Parameters         ---------, Draw point(s) from the Sobol' sequence.          This function draws :math:`n=2^, Reset the engine to base state.          Returns         -------         engine, Fast-forward the sequence by `n` positions.          Parameters         --------, r"""QMC sampling from a multinomial distribution.      Parameters     ---------- (+2 more)

### Community 238 - "Community 238"
Cohesion: 0.15
Nodes (6): ContinuousDistribution, ContinuousDistribution, _Gamma, _log_diff(), _LogUniform, r"""Log-uniform distribution.      The probability density function of the log-u

### Community 239 - "Community 239"
Cohesion: 0.12
Nodes (4): DiscreteDistribution, .. _statsrefmanual:  ========================================== Statistical func, Binomial, r"""Binomial distribution with prescribed success probability and number of tria

### Community 240 - "Community 240"
Cohesion: 0.12
Nodes (16): dct(), dctn(), dst(), dstn(), idct(), idctn(), idst(), idstn() (+8 more)

### Community 241 - "Community 241"
Cohesion: 0.19
Nodes (13): _compute_pair(), _direct(), _get_base_step(), _get_pairs(), _integral_bound(), nsum(), _nsum_iv(), _pair_cache() (+5 more)

### Community 242 - "Community 242"
Cohesion: 0.16
Nodes (13): _check_lsq_design_matrix(), _get_dtype(), _make_lsq_ndbspl(), make_ndbspl(), _preprocess_inputs(), Return np.complex128 for complex dtypes, np.float64 otherwise., Construct the design matrix as a CSR format sparse array.          Parameters, Helpers: validate and preprocess NdBSpline inputs.         Parameters        --- (+5 more)

### Community 243 - "Community 243"
Cohesion: 0.15
Nodes (8): check_arguments(), ConstantDenseOutput, OdeSolver, Perform one integration step.          Returns         -------         message :, Compute a local interpolant over the last successful step.          Returns, Constant value interpolator.      This class used for degenerate integration cas, Base class for ODE solvers.      In order to implement a new solver you need to, Helper function for checking arguments common to all solvers.

### Community 244 - "Community 244"
Cohesion: 0.15
Nodes (10): BDF, BdfDenseOutput, change_D(), compute_R(), Compute the matrix for changing the differences array., # TODO: switch to csc_array after spmatrix is removed, Change differences array in-place when step size is changed., Solve the algebraic system resulting from BDF method. (+2 more)

### Community 245 - "Community 245"
Cohesion: 0.15
Nodes (12): expm_cond(), expm_frechet(), expm_frechet_algo_64(), expm_frechet_block_enlarge(), expm_frechet_kronform(), Frechet derivative of the matrix exponential., Frechet derivative of the matrix exponential of A in the direction E.      Param, This is a helper function, mostly for testing and profiling.     Return expm(A), (+4 more)

### Community 246 - "Community 246"
Cohesion: 0.18
Nodes (16): bg_update_dense(), _get_densest(), Routines for removing redundant (linearly dependent) equations from linear progr, Eliminates redundant equations from system of equations defined by Ax = b     an, Counts the number of nonzeros in each row of input array A.     Nonzeros are def, Eliminates redundant equations from system of equations defined by Ax = b     an, Returns the index of the densest row of A. Ignores rows that are not     eligibl, Eliminates redundant equations from system of equations defined by Ax = b     an (+8 more)

### Community 247 - "Community 247"
Cohesion: 0.12
Nodes (9): Hyperrectangle class.      Represents a Cartesian product of intervals.      Par, Construct a hyperrectangle., Compute the total volume of the hyperrectangle.          Returns         -------, Produce two hyperrectangles by splitting.          In general, if you need to co, Return the minimum distance between input and points in the         hyperrectang, Return the maximum distance between input and points in the hyperrectangle., Compute the minimum distance between points in the two hyperrectangles., Compute the maximum distance between points in the two hyperrectangles. (+1 more)

### Community 248 - "Community 248"
Cohesion: 0.24
Nodes (10): ARNAUD_BLAS(), ARNAUD_znaupd(), ARNAUD_zneupd(), zgetv0(), znaitr(), znapps(), znaup2(), zneigh() (+2 more)

### Community 249 - "Community 249"
Cohesion: 0.20
Nodes (10): ARNAUD_dnaupd(), ARNAUD_dneupd(), dgetv0(), dnaitr(), dnapps(), dnaup2(), dnconv(), dneigh() (+2 more)

### Community 250 - "Community 250"
Cohesion: 0.24
Nodes (10): ARNAUD_BLAS(), ARNAUD_cnaupd(), ARNAUD_cneupd(), cgetv0(), cnaitr(), cnapps(), cnaup2(), cneigh() (+2 more)

### Community 251 - "Community 251"
Cohesion: 0.20
Nodes (10): ARNAUD_snaupd(), ARNAUD_sneupd(), sgetv0(), snaitr(), snapps(), snaup2(), snconv(), sneigh() (+2 more)

### Community 252 - "Community 252"
Cohesion: 0.22
Nodes (12): ARNAUD_dsaupd(), ARNAUD_dseupd(), dgetv0(), dsaitr(), dsapps(), dsaup2(), dsconv(), dseigt() (+4 more)

### Community 253 - "Community 253"
Cohesion: 0.22
Nodes (12): ARNAUD_ssaupd(), ARNAUD_sseupd(), sgetv0(), ssaitr(), ssapps(), ssaup2(), ssconv(), sseigt() (+4 more)

### Community 254 - "Community 254"
Cohesion: 0.15
Nodes (7): NI_ArrayToLineBuffer(), NI_CanonicalType(), NI_ExtendLine(), NI_InitLineBuffer(), NI_InitPointIterator(), NI_LineIterator(), NI_SubspaceIterator()

### Community 255 - "Community 255"
Cohesion: 0.13
Nodes (2): genextreme_gen, r"""A generalized extreme value continuous random variable.      %(before_notes)

### Community 256 - "Community 256"
Cohesion: 0.13
Nodes (4): nchypergeom_wallenius_gen, r"""A Wallenius' noncentral hypergeometric discrete random variable.      Wallen, A generic discrete random variable class meant for subclassing.      `rv_discret, rv_discrete

### Community 257 - "Community 257"
Cohesion: 0.12
Nodes (4): abs(), FoldedDistribution, r"""Distribution underlying the absolute value of a random variable      Given a, r"""Absolute value of a random variable.      Parameters     ----------     X :

### Community 258 - "Community 258"
Cohesion: 0.12
Nodes (4): order_statistic(), OrderStatisticDistribution, r"""Probability distribution of an order statistic.      An instance of this cla, r"""Probability distribution of an order statistic.      Returns a random variab

### Community 259 - "Community 259"
Cohesion: 0.14
Nodes (15): _correa_entropy(), differential_entropy(), _ebrahimi_entropy(), entropy(), _pad_along_last_axis(), Created on Fri Apr  2 09:06:05 2021  @author: matth, r"""Given a sample of a distribution, estimate the differential entropy.      Se, Calculate the Shannon entropy/relative entropy of given distribution(s).      If (+7 more)

### Community 260 - "Community 260"
Cohesion: 0.16
Nodes (13): _combine_bounds(), _compute_dminus(), _compute_dplus(), _corr(), _filliben(), fit(), _get_fit_fun(), _gof_iv() (+5 more)

### Community 261 - "Community 261"
Cohesion: 0.20
Nodes (15): BootstrapResult, Result object returned by `scipy.stats.bootstrap`.      Attributes     ---------, BootstrapSobolResult, f_ishigami(), r"""Saltelli2010 formulation.      .. math::          S_i = \frac{1}{N} \sum_{j=, Bootstrap Sobol' indices to provide confidence intervals.          Parameters, r"""Global sensitivity indices of Sobol'.      Parameters     ----------     fun, r"""Ishigami function.      .. math::          Y(\mathbf{x}) = \sin x_1 + 7 \sin (+7 more)

### Community 262 - "Community 262"
Cohesion: 0.14
Nodes (3): ======================================== Interpolation (:mod:`scipy.interpolate`, Rbf(*args, **kwargs)      Class for radial basis function interpolation of funct, Rbf

### Community 263 - "Community 263"
Cohesion: 0.14
Nodes (9): _check_broadcast_up_to(), _do_extrapolate(), interp2d, lagrange(), interp2d(x, y, z, kind='linear', copy=True, bounds_error=False,              fil, Helper to check that arr_from broadcasts up to shape_to, Helper to check if fill_value == "extrapolate" without warnings, r"""     Return a Lagrange interpolating polynomial.      Given two 1-D arrays ` (+1 more)

### Community 264 - "Community 264"
Cohesion: 0.15
Nodes (15): _dense_num_jac(), norm(), num_jac(), Assert that first_step is valid and return it., Assert that max_Step is valid and return it., Finite differences Jacobian approximation tailored for ODE solvers.      This fu, Display a warning for extraneous keyword arguments.      The initializer of each, Validate tolerance values. (+7 more)

### Community 265 - "Community 265"
Cohesion: 0.15
Nodes (13): _check_format_errors_warnings(), cho_factor(), cho_solve(), cho_solve_banded(), _cholesky(), cholesky_banded(), Cholesky decomposition functions., Compute the Cholesky decomposition of a matrix, to use in cho_solve.      Return (+5 more)

### Community 266 - "Community 266"
Cohesion: 0.13
Nodes (7): Construct a Sakurai matrix in various formats and its eigenvalues.      Construc, Return the requested number of eigenvalues.          Parameters         --------, Construct the Sakurai matrix as a banded array., Construct the Sakurai matrix in a sparse format., Construct matrix-free callable banded-matrix-vector multiplication by         th, Construct matrix-free callable matrix-matrix multiplication by         the Sakur, Sakurai

### Community 267 - "Community 267"
Cohesion: 0.16
Nodes (16): _expand_footprint(), _expand_mode(), _expand_origin(), generic_filter(), maximum_filter(), median_filter(), _min_or_max_filter(), minimum_filter() (+8 more)

### Community 268 - "Community 268"
Cohesion: 0.19
Nodes (9): call_python_function(), jac_multipack_calling_function(), jac_multipack_lm_function(), minpack_hybrd(), minpack_hybrj(), minpack_lmder(), minpack_lmdif(), raw_multipack_calling_function() (+1 more)

### Community 269 - "Community 269"
Cohesion: 0.16
Nodes (5): LowRankMatrix, r"""     A matrix represented as      .. math:: \alpha I + \sum_{n=0}^{n=M} c_n, Reduce the rank of the matrix by dropping all vectors., Reduce the rank of the matrix by dropping oldest vectors., Reduce the rank of the matrix by retaining some SVD components.          This co

### Community 270 - "Community 270"
Cohesion: 0.16
Nodes (15): axis_reverse(), axis_slice(), const_ext(), even_ext(), odd_ext(), Functions for acting on a axis of an array., Even extension at the boundaries of an array      Generate a new ndarray by maki, Constant extension at the boundaries of an array      Generate a new ndarray tha (+7 more)

### Community 271 - "Community 271"
Cohesion: 0.17
Nodes (12): CZT, czt_points(), Calculate the chirp z-transform of a signal.          Parameters         -------, Return the points at which the chirp z-transform is computed.          Returns, Create a callable zoom FFT transform function.      This is a specialization of, Return the points at which the chirp z-transform is computed.      Parameters, Compute the frequency response around a spiral in the Z plane.      Parameters, Compute the DFT of `x` only for frequencies in range `fn`.      Parameters     - (+4 more)

### Community 272 - "Community 272"
Cohesion: 0.18
Nodes (13): abcd_normalize(), cont2discrete(), ltisys -- a collection of functions to convert linear time invariant systems fro, r"""Check state-space matrices compatibility and ensure they are 2d arrays., r"""Transfer function to state-space representation.      Parameters     -------, r"""State-space to transfer function.      A, B, C, D defines a linear state-spa, Zero-pole-gain representation to state-space representation.      Parameters, State-space representation to zero-pole-gain representation.      A, B, C, D def (+5 more)

### Community 273 - "Community 273"
Cohesion: 0.15
Nodes (11): _lstsq(), _poly1d(), polyfit(), polymul(), polyroots(), polyval(), Partial replacements for numpy polynomial routines, with Array API compatibility, Constructor of np.poly1d object from an array of coefficients (r=False) (+3 more)

### Community 274 - "Community 274"
Cohesion: 0.13
Nodes (9): Generate signal slices along last axis of `x`.          This method is only used, Perform the short-time Fourier transform.          A two-dimensional matrix with, Calculate short-time Fourier transform with a trend being subtracted from, r"""Calculate spectrogram or cross-spectrogram.          The spectrogram is the, Determine and validate slice index range.          Parameters         ----------, Times of STFT for an input signal with `n` samples.          Returns a 1d array, FFT based on the `fft_mode`, `mfft`, `scaling` and `phase_shift`         attribu, Sampling interval of input signal and of the window.          A ``ValueError`` i (+1 more)

### Community 275 - "Community 275"
Cohesion: 0.13
Nodes (8): Inverse short-time Fourier transform.          Parameters         ----------, Largest signal index and slice index due to padding.          Parameters, First sample index after signal end not touched by a time slice.          `k_max, Index of first non-overlapping upper time slice for `n` sample         input., Number of time slices for an input signal with `n` samples.          It is given, Return nearest sample index k_p for which ``t[k_p] == t[p]`` holds.          The, Inverse to `_fft_func`.          Returned is an array of length `m_num`. If the, Return minimum and maximum time-frequency values.          Parameters         --

### Community 276 - "Community 276"
Cohesion: 0.15
Nodes (16): _cmplx_sort(), _compute_factors(), _compute_residues(), _group_poles(), invres(), invresz(), Sort roots based on magnitude.      Parameters     ----------     p : array_like, Determine unique roots and their multiplicities from a list of roots.      Param (+8 more)

### Community 277 - "Community 277"
Cohesion: 0.13
Nodes (2): nakagami_gen, r"""A Nakagami continuous random variable.      %(before_notes)s      Notes

### Community 278 - "Community 278"
Cohesion: 0.13
Nodes (9): multi_rv_frozen, Class which encapsulates common functionality between all frozen     multivariat, r"""     A Special Orthogonal matrix (SO(N)) random variable.      Return a rand, Create a frozen SO(N) distribution.          See `special_ortho_group_frozen` fo, Dimension N must be specified; it cannot be inferred., Draw random samples from SO(N).          Parameters         ----------         d, Create a frozen SO(N) distribution.          Parameters         ----------, special_ortho_group_frozen (+1 more)

### Community 279 - "Community 279"
Cohesion: 0.13
Nodes (9): multi_rv_generic, Class which encapsulates common functionality between all multivariate     distr, Get or set the Generator object for generating random variates.          If `see, r"""     A vector-valued uniform direction.      Return a random direction (unit, Create a frozen n-dimensional uniform direction distribution.          See `unif, Dimension N must be specified; it cannot be inferred., Create a frozen n-dimensional uniform direction distribution.          Parameter, uniform_direction_frozen (+1 more)

### Community 280 - "Community 280"
Cohesion: 0.15
Nodes (8): random_correlation_frozen, random_correlation_gen, r"""     A random correlation matrix.      Return a random correlation matrix, g, Create a frozen random correlation matrix.          See `random_correlation_froz, Computes a 2x2 Givens matrix to put 1's on the diagonal.          The input matr, Given a psd matrix m, rotate to put one's on the diagonal, turning it         in, Draw random correlation matrices.          Parameters         ----------, Create a frozen random correlation matrix distribution.          Parameters

### Community 281 - "Community 281"
Cohesion: 0.18
Nodes (15): _butter_analog_poles(), butter_lp(), _prod(), Some signal functions implemented using mpmath., Frequency response of a filter in zpk format, using mpmath.      This is the sam, Returns the product of the elements in the sequence `seq`., Return relative degree of transfer function from zeros and poles.      This is s, Bilinear transformation to convert a filter from analog to digital. (+7 more)

### Community 282 - "Community 282"
Cohesion: 0.17
Nodes (15): augmented_system_projections(), normal_equation_projections(), orthogonality(), projections(), qr_factorization_projections(), Basic linear factorizations needed by the solver., # TODO: Use a symmetric indefinite factorization, Return linear operators for matrix A using ``QRFactorization`` approach. (+7 more)

### Community 283 - "Community 283"
Cohesion: 0.20
Nodes (14): _add_knots(), _apply_bbox_grid(), _build_design_matrices(), _initialise_knots(), _p_search_hit_s(), Regrid (2-D smoothing B-splines via separable 1-D FITPACK kernels) =============, Interface for 2-D smoothing B-spline fitting (1/p penalty form).      Parameters, Build a 2D ``NdBSpline`` from knot vectors and a coefficient grid.      Paramete (+6 more)

### Community 284 - "Community 284"
Cohesion: 0.14
Nodes (11): _check_work_float(), _compute_lwork(), _ensure_aligned_and_native(), get_lapack_funcs(), _normalize_lapack_dtype(), Low-level LAPACK functions (:mod:`scipy.linalg.lapack`) ========================, Round floating-point lwork returned by lapack to integer.      Several LAPACK ro, Convert LAPACK-returned work array size float to integer,     carefully for sing (+3 more)

### Community 285 - "Community 285"
Cohesion: 0.13
Nodes (9): NamedTuple, This class abstracts handling of a project's versions.      A :class:`Version` i, A representation of the Version that shows all internal state.          >>> Vers, A string representation of the version that can be round-tripped.          >>> s, The epoch of the version.          >>> Version("2.0.0").epoch         0, The components of the "release" segment of the version.          >>> Version("1., The pre-release segment of the version.          >>> print(Version("1.2.3").pre), The development number of the version.          >>> print(Version("1.2.3").dev) (+1 more)

### Community 286 - "Community 286"
Cohesion: 0.18
Nodes (14): get_region(), get_result(), get_result_no_mp(), get_results(), main(), _make_hyp2f1_test_case(), make_hyp2f1_test_cases(), This script evaluates scipy's implementation of hyp2f1 against mpmath's.  Author (+6 more)

### Community 287 - "Community 287"
Cohesion: 0.19
Nodes (14): asymptotic_series(), dg_series(), main(), optimal_epsilon_integral(), pg_series(), Precompute coefficients of several series expansions of Wright's generalized Bes, Asymptotic expansion for large x.      Phi(a, b, x) ~ Z^(1/2-b) * exp((1+a)/a *, Tylor series expansion of Phi(a, b, x) in a=0 up to order 5. (+6 more)

### Community 289 - "Community 289"
Cohesion: 0.13
Nodes (5): rv_discrete, r"""A Zipf (Zeta) discrete random variable.      %(before_notes)s      See Also, r"""A  Skellam discrete random variable.      %(before_notes)s      Notes     --, skellam_gen, zipf_gen

### Community 290 - "Community 290"
Cohesion: 0.13
Nodes (15): _align_nums(), bilinear(), lp2bp(), lp2bs(), lp2hp(), lp2lp(), normalize(), Aligns the shapes of multiple numerators.      Given an array of numerator coeff (+7 more)

### Community 291 - "Community 291"
Cohesion: 0.25
Nodes (15): band_stop_obj(), buttord(), cheb1ord(), cheb2ord(), ellipord(), _find_nat_freq(), _postprocess_wn(), _pre_warp() (+7 more)

### Community 292 - "Community 292"
Cohesion: 0.16
Nodes (15): _apply_conv_mode(), _calc_oa_lens(), _centered(), fftconvolve(), _freq_domain_conv(), _init_freq_conv_axes(), oaconvolve(), Handle the axes argument for frequency-domain convolution.      Returns the inpu (+7 more)

### Community 294 - "Community 294"
Cohesion: 0.14
Nodes (10): directed_hausdorff(), jensenshannon(), MetricInfo, pdist(), Distance computations (:mod:`scipy.spatial.distance`) ==========================, Compute the Jensen-Shannon distance (metric) between     two probability arrays., Pairwise distances between observations in n-dimensional space.      See Notes f, Compute the directed Hausdorff distance between two 2-D arrays.      Distances b (+2 more)

### Community 295 - "Community 295"
Cohesion: 0.13
Nodes (8): KDTree, kd-tree for quick nearest-neighbor lookup.      This class provides an index int, r"""Query the kd-tree for nearest neighbors.          Parameters         -------, Find all points within distance r of point(s) x.          Parameters         ---, Find all pairs of points between `self` and `other` whose distance is         at, Find all pairs of points in `self` whose distance is at most r.          Paramet, Count how many nearby pairs can be formed.          Count the number of pairs ``, Compute a sparse distance matrix.          Computes a distance matrix between tw

### Community 296 - "Community 296"
Cohesion: 0.18
Nodes (8): calculate_solid_angles(), Spherical Voronoi Code  .. versionadded:: 0.18.0, Calculates the Voronoi vertices and regions of the generators stored         in, Calculates the solid angles of plane triangles. Implements the method of     Van, Sort indices of the vertices to be (counter-)clockwise ordered.          Raises, Calculates the areas of the Voronoi regions.          For 2D point sets, the reg, Voronoi diagrams on the surface of a sphere.      .. versionadded:: 0.18.0, SphericalVoronoi

### Community 297 - "Community 297"
Cohesion: 0.30
Nodes (14): dewset(), dvhin(), dvindy(), dvjac(), dvjust(), dvnlsd(), dvnorm(), dvode() (+6 more)

### Community 298 - "Community 298"
Cohesion: 0.30
Nodes (14): int_max(), int_min(), zewset(), zvhin(), zvindy(), zvjac(), zvjust(), zvnlsd() (+6 more)

### Community 299 - "Community 299"
Cohesion: 0.13
Nodes (2): gengamma_gen, r"""A generalized gamma continuous random variable.      %(before_notes)s      S

### Community 300 - "Community 300"
Cohesion: 0.13
Nodes (2): genpareto_gen, r"""A generalized Pareto continuous random variable.      %(before_notes)s

### Community 301 - "Community 301"
Cohesion: 0.13
Nodes (2): logistic_gen, r"""A logistic (or Sech-squared) continuous random variable.      %(before_notes

### Community 302 - "Community 302"
Cohesion: 0.13
Nodes (2): r"""A doubly truncated Weibull minimum continuous random variable.      %(before, truncweibull_min_gen

### Community 303 - "Community 303"
Cohesion: 0.13
Nodes (8): Covariance, Representation of a covariance matrix.      Calculations involving covariance ma, Perform a whitening transformation on data.          "Whitening" ("white" as in, Perform a colorizing transformation on data.          "Colorizing" ("color" as i, Log of the pseudo-determinant of the covariance matrix, Rank of the covariance matrix, Explicit representation of the covariance matrix, Shape of the covariance array

### Community 304 - "Community 304"
Cohesion: 0.13
Nodes (11): n_primes(), primes_from_2_to(), Initialize permutations for all Van der Corput sequences.          Permutations, Draw `n` in the half-open interval ``[0, 1)``.          Parameters         -----, Orthogonal array based LHS of strength 2., Prime numbers from 2 to *n*.      Parameters     ----------     n : int, List of the n-first prime numbers.      Parameters     ----------     n : int, Permutations for scrambling a Van der Corput sequence.      Parameters     ----- (+3 more)

### Community 305 - "Community 305"
Cohesion: 0.13
Nodes (9): Spatial Transformations (:mod:`scipy.spatial.transform`) =======================, # TODO: We defer the implementation of groups for arbitrary Array API frameworks, # TODO: This special case handling is mainly a result of Array API limitations., # TODO: We should move to one single way of specifying the output shape and, # TODO: We should move to one single way of specifying the output shape and, Spherical Linear Interpolation of Rotations.      The interpolation between cons, Interpolate rotations.          Compute the interpolated rotations at the given, Initialize from rotation vectors.          A rotation vector is a 3 dimensional (+1 more)

### Community 306 - "Community 306"
Cohesion: 0.26
Nodes (13): FishersNCHyp(), FishersNCHypInversion(), FishersNCHypRatioOfUnifoms(), MultiComplWalleniusNCHyp(), MultiFishersNCHyp(), MultiWalleniusNCHyp(), SetAccuracy(), StochasticLib3() (+5 more)

### Community 307 - "Community 307"
Cohesion: 0.29
Nodes (12): _laplace(), _laplace_normed(), _laplace_normed_sym(), _laplace_sym(), laplacian(), _laplacian_dense(), _laplacian_dense_flo(), _laplacian_sparse_flo() (+4 more)

### Community 308 - "Community 308"
Cohesion: 0.19
Nodes (12): _backend_from_arg(), Context manager to set the backend within a fixed scope.      Upon entering the, Context manager to skip a backend within a fixed scope.      Within the context, Maps strings to known backends and validates the backend, Sets the global fft backend.      This utility method replaces the default backe, The default backend for fft calculations      Notes     -----     We use the dom, Register a backend for permanent use.      Registered backends have the lowest p, register_backend() (+4 more)

### Community 309 - "Community 309"
Cohesion: 0.14
Nodes (7): IntegratorBase, IntegratorConcurrencyError, Failure due to concurrent usage of an integrator that can be used     only for a, Prepare integrator for call: allocate memory, set flags, etc.         n - number, Integrate from t=t0 to t=t1 using y0 as an initial condition.         Return 2-t, Make one integration step and return (y1,t1)., Integrate from t=t0 to t>=t1 and return (y1,t).

### Community 310 - "Community 310"
Cohesion: 0.26
Nodes (10): activate_odepack_callback(), cleanup_odepack_callback(), compute_lrw_liw(), copy_array_to_fortran(), deactivate_odepack_callback(), ode_jacobian_thunk(), odepack_lsoda_step(), odepack_odeint() (+2 more)

### Community 311 - "Community 311"
Cohesion: 0.15
Nodes (8): NdBSpline, Evaluate the tensor product b-spline at ``xi``.          Parameters         ----, Construct a new NdBSpline representing the partial derivative.          Paramete, Tensor product spline object.      The value at point ``xp = (x1, x2, ..., xN)``, _ndbspline_call_like_bivariate(), Evaluate a 2D `NdBSpline` like a classical bivariate API.      Parameters     --, Initialize a non-periodic knot vector.      Parameters     ----------     m : in, Knot-growth helper for knot-finding loop (non-periodic).      Parameters     ---

### Community 312 - "Community 312"
Cohesion: 0.16
Nodes (12): check_free_memory(), _get_mem_available(), _parse_size(), _pytest_has_xdist(), Generic test utilities., Check if the pytest-xdist plugin is installed, providing parallel tests, Check *free_mb* of memory is available, otherwise do pytest.skip, Get information about memory available, not counting swap. (+4 more)

### Community 313 - "Community 313"
Cohesion: 0.14
Nodes (13): _linprog_highs_doc(), _linprog_highs_ds_doc(), _linprog_highs_ipm_doc(), _linprog_ip_doc(), _linprog_rs_doc(), _linprog_simplex_doc(), Created on Sat Aug 22 19:49:17 2020  @author: matth, r"""     Linear programming: minimize a linear objective function subject to lin (+5 more)

### Community 314 - "Community 314"
Cohesion: 0.14
Nodes (14): _aberth(), _bessel_poly(), _bessel_zeros(), besselap(), _campos_zeros(), _falling_factorial(), _norm_factor(), r"""     Return the factorial of `x` to the `n` falling.      This is defined as (+6 more)

### Community 315 - "Community 315"
Cohesion: 0.14
Nodes (7): freqresp(), LinearTimeInvariant, Convert to `ZerosPolesGain` system, without copying.          Returns         --, r"""Calculate the frequency response of a continuous-time system.      Parameter, Create a new object, don't allow direct instances., Initialize the `lti` baseclass.          The heavy lifting is done by the subcla, Return the sampling time of the system, `None` for `lti` systems.

### Community 316 - "Community 316"
Cohesion: 0.16
Nodes (4): MultiUFunc, Set `key` method by decorating a function., Set `resolve_out_shapes` method by decorating a function., Resolve to a ufunc based on keyword arguments.

### Community 317 - "Community 317"
Cohesion: 0.16
Nodes (14): _gen_roots_and_weights(), legendre(), r"""Gauss-Gegenbauer quadrature.      Compute the sample points and weights for, [x,w] = gen_roots_and_weights(n,an_func,sqrt_bn_func,mu)      Returns the roots, r"""Gauss-Jacobi quadrature.      Compute the sample points and weights for Gaus, r"""Gauss-Legendre quadrature.      Compute the sample points and weights for Ga, r"""Legendre polynomial.      Defined to be the solution of      .. math::, r"""Gauss-Legendre (shifted) quadrature.      Compute the sample points and weig (+6 more)

### Community 318 - "Community 318"
Cohesion: 0.18
Nodes (7): assert_func_equal(), FuncData, MissingModule, Check the special function against the data., Enable special function errors (such as underflow, overflow,     loss of precisi, Data set for checking a special function.      Parameters     ----------     fun, with_special_errors()

### Community 319 - "Community 319"
Cohesion: 0.30
Nodes (10): maxSortDown(), maxSortUp(), Mediator, MediatorInsert(), minSortDown(), minSortUp(), mmCmpExch(), mmexchange() (+2 more)

### Community 320 - "Community 320"
Cohesion: 0.22
Nodes (13): _bin_edges(), _bin_numbers(), _bincount(), binned_statistic(), binned_statistic_2d(), binned_statistic_dd(), _calc_binned_statistic(), _create_binned_data() (+5 more)

### Community 321 - "Community 321"
Cohesion: 0.16
Nodes (2): dpareto_lognorm_gen, r"""A double Pareto lognormal continuous random variable.      %(before_notes)s

### Community 322 - "Community 322"
Cohesion: 0.14
Nodes (3): _log_diff(), r"""A loguniform or reciprocal continuous random variable.      %(before_notes)s, reciprocal_gen

### Community 323 - "Community 323"
Cohesion: 0.14
Nodes (2): loggamma_gen, r"""A log gamma continuous random variable.      %(before_notes)s      Notes

### Community 324 - "Community 324"
Cohesion: 0.20
Nodes (12): chatterjeexi(), _chatterjeexi_iv(), r"""Calculate a Spearman rho correlation coefficient with associated p-value., r"""     Computes the Theil-Sen estimator for a set of points (x, y).      `thei, r"""     Computes the Siegel estimator for a set of points (x, y).      `siegels, r"""Compute the xi correlation and perform a test of independence.      The xi c, _robust_slopes(), siegelslopes() (+4 more)

### Community 325 - "Community 325"
Cohesion: 0.14
Nodes (2): bernoulli_gen, r"""A Bernoulli discrete random variable.      %(before_notes)s      Notes     -

### Community 326 - "Community 326"
Cohesion: 0.14
Nodes (2): hypergeom_gen, r"""A hypergeometric discrete random variable.      The hypergeometric distribut

### Community 327 - "Community 327"
Cohesion: 0.23
Nodes (4): FitResult, Visually compare the data against the fitted distribution.          Available on, r"""Result of fitting a discrete or continuous distribution to data      Attribu, Negative log-likelihood function          Evaluates the negative of the log-like

### Community 328 - "Community 328"
Cohesion: 0.18
Nodes (12): _all_partitions(), epps_singleton_2samp(), poisson_means_test(), _poisson_means_test_iv(), r"""     Performs the Poisson means test, AKA the "E-test".      This is a test, Compute the Epps-Singleton (ES) test statistic.      Test the null hypothesis th, Calculate Somers' D and p-value from contingency table., r"""Calculates Somers' D, an asymmetric measure of ordinal association.      Lik (+4 more)

### Community 329 - "Community 329"
Cohesion: 0.19
Nodes (12): _a_ij_Aij_Dij2(), _Aij(), _compute_outer_prob_inside_method(), _concordant_pairs(), _Dij(), _discordant_pairs(), Sum of lower-left and upper-right blocks of contingency table., Twice the number of concordant pairs, excluding ties. (+4 more)

### Community 330 - "Community 330"
Cohesion: 0.33
Nodes (10): CFishersNCHypergeometric(), lng(), loop(), MakeTable(), mean(), mode(), moments(), probability() (+2 more)

### Community 331 - "Community 331"
Cohesion: 0.15
Nodes (12): fftfreq(), fftshift(), ifftshift(), next_fast_len(), prev_fast_len(), Find the next fast size of input data to ``fft``, for zero-padding, etc.      Sc, Return the Discrete Fourier Transform sample frequencies.      The returned floa, Return the Discrete Fourier Transform sample frequencies     (for usage with rff (+4 more)

### Community 332 - "Community 332"
Cohesion: 0.23
Nodes (8): cleanup_dvode_callback(), copy_array_to_fortran(), copy_complex_array_to_fortran(), dvode_jacobian_thunk(), dvode_wrapper(), setup_dvode_callback(), zvode_jacobian_thunk(), zvode_wrapper()

### Community 333 - "Community 333"
Cohesion: 0.15
Nodes (6): complex_ode, A wrapper of ode for complex systems.      This functions similarly as `ode`, bu, Set integrator by name.          Parameters         ----------         name : st, Set initial conditions y(t) = y., Find y=y(t), set y as an initial condition, and return y.          Parameters, Set callable to be called at every successful integration step.          Paramet

### Community 334 - "Community 334"
Cohesion: 0.19
Nodes (9): _calc_b(), _calc_e(), LSQBivariateSpline, fitpack --- curve and surface fitting with splines  fitpack is based on a collec, Wrapper for surfit with iopt=-1 (least squares fit with fixed knots).     Return, Weighted least-squares bivariate spline approximation.      Parameters     -----, Calculate lower bbox bound for LSQ splines (mimics f2py calc_b)., Calculate upper bbox bound for LSQ splines (mimics f2py calc_e). (+1 more)

### Community 335 - "Community 335"
Cohesion: 0.17
Nodes (9): det(), _get_axis_len(), pinv(), Compute the determinant of a matrix.      The determinant is a scalar that is a, Compute the (Moore-Penrose) pseudo-inverse of a matrix.      Calculate a general, Solve the equation ``a @ x = b`` for ``x``, where `a` is a triangular matrix., Solve the equation ``C @ x = b`` for ``x``, where ``C`` is a     circulant matri, solve_circulant() (+1 more)

### Community 336 - "Community 336"
Cohesion: 0.21
Nodes (4): MikotaM, Construct a mass matrix in various formats of Mikota pair.      The mass matrix, Construct matrix-free callable banded-matrix-vector multiplication by         th, Construct matrix-free callable matrix-matrix multiplication by         the Mikot

### Community 337 - "Community 337"
Cohesion: 0.17
Nodes (6): assert_no_overwrite(), _FakeMatrix, _FakeMatrix2, _get_array(), Get a test array of given shape and data type.     Returned NxN matrices are pos, Test that a call does not overwrite its input arguments

### Community 338 - "Community 338"
Cohesion: 0.21
Nodes (10): fourier_ellipsoid(), fourier_gaussian(), fourier_shift(), fourier_uniform(), _get_output_fourier(), _get_output_fourier_complex(), Multidimensional uniform fourier filter.      The array is multiplied with the F, Multidimensional ellipsoid Fourier filter.      The array is multiplied with the (+2 more)

### Community 339 - "Community 339"
Cohesion: 0.15
Nodes (13): check_COLA_signature(), check_NOLA_signature(), coherence_signature(), csd_signature(), istft_signature(), periodogram_signature(), Handle `window` being a str or a tuple or an array-like., resample_poly_signature() (+5 more)

### Community 340 - "Community 340"
Cohesion: 0.17
Nodes (13): findfreqs(), freqs(), freqs_zpk(), freqz_zpk(), group_delay(), _is_int_type(), _logspace(), Find array of frequencies for computing the response of an analog filter.      P (+5 more)

### Community 341 - "Community 341"
Cohesion: 0.23
Nodes (12): _logdet_difference_matrix(), _polynomial_fit(), Solve the equation ``a @ x = b`` for ``x``,  where ``a`` is the      Hermitian p, Polynomial fit equivalent to WH for lamb -> infinity., Solve the WH optimization problem via the normal equations.          A @ x = y, Logarithm of the determinant of the difference matrix.      If D is the differen, Calculate the restricted maximum likelihood (REML).          Parameters     ----, r"""     Whittaker-Henderson (WH) smoothing/graduation of a discrete signal. (+4 more)

### Community 342 - "Community 342"
Cohesion: 0.22
Nodes (11): cdist(), _cdist_callable(), CDistMetricWrapper, _convert_to_type(), _np_pdist(), _pdist_callable(), PDistMetricWrapper, _prepare_out_argument() (+3 more)

### Community 343 - "Community 343"
Cohesion: 0.15
Nodes (13): _bessel_diff_formula(), h1vp(), h2vp(), ivp(), jvp(), kvp(), Compute derivatives of modified Bessel functions of the first kind.      Compute, Compute derivatives of Hankel function H1v(z) with respect to `z`.      Paramete (+5 more)

### Community 344 - "Community 344"
Cohesion: 0.18
Nodes (12): chebyu(), gegenbauer(), jacobi(), r"""Gegenbauer (ultraspherical) polynomial.      Defined to be the solution of t, r"""Chebyshev polynomial of the second kind.      Defined to be the solution of, r"""Shifted Chebyshev polynomial of the first kind.      Defined as :math:`T^*_n, r"""Shifted Chebyshev polynomial of the second kind.      Defined as :math:`U^*_, r"""Jacobi polynomial.      Defined to be the solution of      .. math:: (+4 more)

### Community 345 - "Community 345"
Cohesion: 0.17
Nodes (11): genlaguerre(), laguerre(), orthopoly1d, r"""Laguerre polynomial.      Defined to be the solution of      .. math::, r"""     Shifted Legendre polynomial.      Defined as :math:`P^*_n(x) = P_n(2x -, r"""Gauss-generalized Laguerre quadrature.      Compute the sample points and we, r"""Generalized (associated) Laguerre polynomial.      Defined to be the solutio, r"""Gauss-Laguerre quadrature.      Compute the sample points and weights for Ga (+3 more)

### Community 346 - "Community 346"
Cohesion: 0.26
Nodes (12): ccgs(), cmgs(), creorth(), dcgs(), dmgs(), dreorth(), scgs(), smgs() (+4 more)

### Community 347 - "Community 347"
Cohesion: 0.15
Nodes (3): InfinityType, The post-release number of the version.          >>> print(Version("1.2.3").post, The third item of :attr:`release` or ``0`` if unavailable.          >>> Version(

### Community 348 - "Community 348"
Cohesion: 0.17
Nodes (3): NegativeInfinityType, Release segment without any trailing zeros.          >>> _TrimmedRelease('1.0.0', _TrimmedRelease

### Community 349 - "Community 349"
Cohesion: 0.24
Nodes (12): association(), chi2_contingency(), _chi2_monte_carlo_method(), _chi2_permutation_method(), _chi2_resampling_methods(), expected_freq(), margins(), Contingency table functions (:mod:`scipy.stats.contingency`) =================== (+4 more)

### Community 350 - "Community 350"
Cohesion: 0.15
Nodes (2): beta_gen, r"""A beta continuous random variable.      %(before_notes)s      Notes     ----

### Community 351 - "Community 351"
Cohesion: 0.15
Nodes (2): chi_gen, r"""A chi continuous random variable.      %(before_notes)s      Notes     -----

### Community 352 - "Community 352"
Cohesion: 0.15
Nodes (2): expon_gen, r"""An exponential continuous random variable.      %(before_notes)s      Notes

### Community 353 - "Community 353"
Cohesion: 0.15
Nodes (2): gennorm_gen, r"""A (symmetric) generalized normal continuous random variable.      %(before_n

### Community 354 - "Community 354"
Cohesion: 0.15
Nodes (2): gumbel_l_gen, r"""A left-skewed Gumbel continuous random variable.      %(before_notes)s

### Community 355 - "Community 355"
Cohesion: 0.15
Nodes (2): gumbel_r_gen, r"""A right-skewed Gumbel continuous random variable.      %(before_notes)s

### Community 356 - "Community 356"
Cohesion: 0.15
Nodes (2): halfgennorm_gen, r"""The upper half of a generalized normal continuous random variable.      %(be

### Community 357 - "Community 357"
Cohesion: 0.15
Nodes (2): invgamma_gen, r"""An inverted gamma continuous random variable.      %(before_notes)s      Not

### Community 358 - "Community 358"
Cohesion: 0.15
Nodes (2): irwinhall_gen, r"""An Irwin-Hall (Uniform Sum) continuous random variable.      An `Irwin-Hall

### Community 359 - "Community 359"
Cohesion: 0.18
Nodes (2): kappa4_gen, r"""Kappa 4 parameter distribution.      %(before_notes)s      Notes     -----

### Community 360 - "Community 360"
Cohesion: 0.15
Nodes (2): landau_gen, r"""A Landau continuous random variable.      %(before_notes)s      See Also

### Community 361 - "Community 361"
Cohesion: 0.15
Nodes (2): maxwell_gen, r"""A Maxwell continuous random variable.      %(before_notes)s      Notes     -

### Community 362 - "Community 362"
Cohesion: 0.22
Nodes (2): pearson3_gen, r"""     A pearson type III continuous random variable.      %(before_notes)s

### Community 363 - "Community 363"
Cohesion: 0.15
Nodes (2): powerlaw_gen, r"""A power-function continuous random variable.      %(before_notes)s      See

### Community 364 - "Community 364"
Cohesion: 0.15
Nodes (2): r"""Weibull minimum continuous random variable.      The Weibull Minimum Extreme, weibull_min_gen

### Community 365 - "Community 365"
Cohesion: 0.15
Nodes (2): binom_gen, r"""     A binomial discrete random variable.      %(before_notes)s      See Als

### Community 366 - "Community 366"
Cohesion: 0.15
Nodes (2): geom_gen, r"""A geometric discrete random variable.      %(before_notes)s      See Also

### Community 367 - "Community 367"
Cohesion: 0.15
Nodes (2): nbinom_gen, r"""     A negative binomial discrete random variable.      %(before_notes)s

### Community 368 - "Community 368"
Cohesion: 0.19
Nodes (5): nchypergeom_fisher_gen, _nchypergeom_gen, r"""A noncentral hypergeometric discrete random variable.      For subclassing b, r"""A Fisher's noncentral hypergeometric discrete random variable.      Fisher's, rv_discrete_frozen

### Community 369 - "Community 369"
Cohesion: 0.15
Nodes (2): poisson_gen, r"""A Poisson discrete random variable.      %(before_notes)s      Notes     ---

### Community 370 - "Community 370"
Cohesion: 0.17
Nodes (7): ortho_group_frozen, ortho_group_gen, r"""     An Orthogonal matrix (O(N)) random variable.      Return a random ortho, Create a frozen O(N) distribution.          See `ortho_group_frozen` for more in, Dimension N must be specified; it cannot be inferred., Draw random samples from O(N).          Parameters         ----------         di, Create a frozen O(N) distribution.          Parameters         ----------

### Community 371 - "Community 371"
Cohesion: 0.17
Nodes (7): r"""     A matrix-valued U(N) random variable.      Return a random unitary matr, Create a frozen (U(N)) n-dimensional unitary matrix distribution.          See `, Dimension N must be specified; it cannot be inferred., Draw random samples from U(N).          Parameters         ----------         di, Create a frozen (U(N)) n-dimensional unitary matrix distribution.          Param, unitary_group_frozen, unitary_group_gen

### Community 372 - "Community 372"
Cohesion: 0.29
Nodes (12): estimated_cdf(), _estimated_cdf_hf(), _post_quantile(), quantile(), _quantile_bc(), _quantile_hd(), _quantile_hf(), _quantile_iv() (+4 more)

### Community 373 - "Community 373"
Cohesion: 0.26
Nodes (5): _correction_sign(), _wilcoxon_iv(), _wilcoxon_nd(), _wilcoxon_statistic(), WilcoxonDistribution

### Community 374 - "Community 374"
Cohesion: 0.15
Nodes (6): Represent as quaternions.          Rotations in 3 dimensions can be represented, Represent as rotation vectors.          A rotation vector is a 3 dimensional vec, Concatenate a sequence of `Rotation` objects into a single object.          This, Invert this rotation.          Composition of a rotation with its inverse result, Reduce this rotation with the provided rotation groups.          Reduction of a, Set rotation(s) at given index(es) from object.          Parameters         ----

### Community 375 - "Community 375"
Cohesion: 0.20
Nodes (8): cKDTree, ============================================================= Spatial algorithms, distance_matrix(), minkowski_distance(), minkowski_distance_p(), Compute the pth power of the L**p distance between two arrays.      For efficien, Compute the L**p distance between two arrays.      The last dimensions of `x` an, Compute the distance matrix.      Returns the matrix of all pair-wise distances.

### Community 376 - "Community 376"
Cohesion: 0.18
Nodes (8): BivariateSpline, Wrapper for surfit with iopt=0 (smoothing spline).     Returns: nx, tx, ny, ty,, Base class for bivariate splines.      This describes a spline ``s(x, y)`` of de, Evaluate the spline at points.          Returns the interpolated value at ``(xi[, Evaluate the integral of the spline over area [xa,xb] x [ya,yb].          Parame, Smooth bivariate spline approximation.      Parameters     ----------     x, y,, SmoothBivariateSpline, _surfit_smth()

### Community 377 - "Community 377"
Cohesion: 0.17
Nodes (8): LSQSphereBivariateSpline, Bivariate spline s(x,y) of degrees 3 on a sphere, calculated from a     given se, Evaluate the spline or its derivatives at given positions.          Parameters, Evaluate the spline at points.          Returns the interpolated value at ``(the, Weighted least-squares bivariate spline approximation in spherical     coordinat, Wrapper for sphere with iopt=-1 (least squares fit with fixed knots on sphere)., SphereBivariateSpline, _spherfit_lsq()

### Community 378 - "Community 378"
Cohesion: 0.23
Nodes (6): _get_backend(), Module for RBF interpolation., Evaluate the interpolation while controlling memory consumption.         We chun, Evaluate the interpolant at `x`.          Parameters         ----------, Radial basis function interpolator in N ≥ 1 dimensions.      Parameters     ----, RBFInterpolator

### Community 379 - "Community 379"
Cohesion: 0.18
Nodes (12): _asarray(), _check_finite(), Copies an array.      Parameters     ----------     x : array      xp : array_na, Returns the dtype that results from applying type promotion rules     (see Array, Promotes elements of *args to result dtype, ignoring `None`s.     Includes optio, Return the array-api-compat(ible) namespace corresponding to `xp`.      A user-p, Check for NaNs or Infs., SciPy-specific replacement for `np.asarray` with `order`, `check_finite`, and (+4 more)

### Community 380 - "Community 380"
Cohesion: 0.21
Nodes (9): qr(), qr_multiply(), QR decomposition functions., Call a LAPACK routine, determining lwork automatically and handling     error re, Calculate the QR decomposition and multiply Q with a matrix.      Calculate the, Compute QR decomposition of a matrix.      Calculate the decomposition ``A = Q R, Compute RQ decomposition of a matrix.      Calculate the decomposition ``A = R Q, rq() (+1 more)

### Community 381 - "Community 381"
Cohesion: 0.17
Nodes (5): _AdjointLinearOperator, Hermitian adjoint.          Returns the Hermitian adjoint of this linear operato, Hermitian adjoint.          See Also         --------         scipy.sparse.linal, Default implementation of `_adjoint`.         Defers to adjoint functions, e.g., Adjoint of arbitrary Linear Operator

### Community 382 - "Community 382"
Cohesion: 0.17
Nodes (5): Transpose.          Returns         -------         `LinearOperator`, Transpose.          See Also         --------         scipy.sparse.linalg.Linear, Default implementation of `_transpose`.         For `_matvec`, defers to `_rmatv, Transposition of arbitrary Linear Operator, _TransposedLinearOperator

### Community 383 - "Community 383"
Cohesion: 0.17
Nodes (4): MikotaK, Construct a stiffness matrix in various formats of Mikota pair.      The stiffne, Construct matrix-free callable banded-matrix-vector multiplication by         th, Construct matrix-free callable matrix-matrix multiplication by         the Stiff

### Community 384 - "Community 384"
Cohesion: 0.18
Nodes (9): generic_filter1d(), maximum_filter1d(), minimum_filter1d(), Calculate a 1-D minimum filter along the given axis.      The lines of the array, Calculate a 1-D maximum filter along the given axis.      The lines of the array, Filter an array with a vectorized Python callable as the kernel.      Parameters, Calculate a 1-D filter along the given axis.      `generic_filter1d` iterates ov, vectorized_filter() (+1 more)

### Community 385 - "Community 385"
Cohesion: 0.23
Nodes (11): compute_a(), compute_alpha(), compute_d(), compute_g(), eta(), main(), Precompute coefficients of Temme's asymptotic expansion for gammainc.  This take, g_k from DLMF 5.11.3/5.11.5 (+3 more)

### Community 386 - "Community 386"
Cohesion: 0.17
Nodes (8): dbode(), dfreqresp(), Convert to `TransferFunction` system, without copying.          Returns, r"""     Calculate the frequency response of a discrete-time system.      Parame, r"""Calculate Bode magnitude and phase data of a discrete-time system.      Para, r"""         Calculate Bode magnitude and phase data of a discrete-time system., Calculate the frequency response of a discrete-time system.          Parameters, Change a transfer function from the variable `z` to `z**-1`.          Parameters

### Community 387 - "Community 387"
Cohesion: 0.26
Nodes (7): eff(), freq_eval(), lagrange_interp(), pre_remez(), remez(), _sigtools_remez(), wate()

### Community 388 - "Community 388"
Cohesion: 0.21
Nodes (9): chebys(), A collection of functions to find the weights and abscissas for Gaussian Quadrat, r"""Gauss-Chebyshev (second kind) quadrature.      Computes the sample points an, r"""Gauss-Chebyshev (second kind) quadrature.      Compute the sample points and, r"""Chebyshev polynomial of the second kind on :math:`[-2, 2]`.      Defined as, r"""Gauss-Chebyshev (second kind, shifted) quadrature.      Computes the sample, roots_chebys(), roots_chebyu() (+1 more)

### Community 389 - "Community 389"
Cohesion: 0.41
Nodes (11): etdfs(), finalize_disjoint_sets(), find(), initialize_disjoint_sets(), link(), make_set(), mxCallocInt(), nr_etdfs() (+3 more)

### Community 390 - "Community 390"
Cohesion: 0.20
Nodes (4): argus_gen, _argus_phi(), Utility function for the argus distribution used in the pdf, sf and     moment c, r"""     Argus distribution.      %(before_notes)s      Notes     -----     The

### Community 391 - "Community 391"
Cohesion: 0.17
Nodes (2): burr12_gen, r"""A Burr (Type XII) continuous random variable.      %(before_notes)s      See

### Community 392 - "Community 392"
Cohesion: 0.17
Nodes (2): cauchy_gen, r"""A Cauchy continuous random variable.      %(before_notes)s      Notes     --

### Community 393 - "Community 393"
Cohesion: 0.17
Nodes (2): chi2_gen, r"""A chi-squared continuous random variable.      For the noncentral chi-square

### Community 394 - "Community 394"
Cohesion: 0.17
Nodes (2): dweibull_gen, r"""A double Weibull continuous random variable.      %(before_notes)s      Note

### Community 395 - "Community 395"
Cohesion: 0.20
Nodes (3): genhyperbolic_gen, r"""A generalized hyperbolic continuous random variable.      %(before_notes)s, Integrate the pdf of the genhyberbolic distribution from x0 to x1.         This

### Community 396 - "Community 396"
Cohesion: 0.20
Nodes (2): geninvgauss_gen, r"""A Generalized Inverse Gaussian continuous random variable.      %(before_not

### Community 397 - "Community 397"
Cohesion: 0.17
Nodes (2): genlogistic_gen, r"""A generalized logistic continuous random variable.      %(before_notes)s

### Community 398 - "Community 398"
Cohesion: 0.17
Nodes (2): laplace_gen, r"""A Laplace continuous random variable.      %(before_notes)s      Notes     -

### Community 399 - "Community 399"
Cohesion: 0.17
Nodes (2): lomax_gen, r"""A Lomax (Pareto of the second kind) continuous random variable.      %(befor

### Community 400 - "Community 400"
Cohesion: 0.17
Nodes (2): ncx2_gen, r"""A non-central chi-squared continuous random variable.      %(before_notes)s

### Community 401 - "Community 401"
Cohesion: 0.18
Nodes (3): norminvgauss_gen, _norminvgauss_quadrature(), r"""A Normal Inverse Gaussian continuous random variable.      %(before_notes)s

### Community 402 - "Community 402"
Cohesion: 0.17
Nodes (2): r"""A truncated exponential continuous random variable.      %(before_notes)s, truncexpon_gen

### Community 403 - "Community 403"
Cohesion: 0.17
Nodes (2): r"""A Von Mises continuous random variable.      %(before_notes)s      See Also, vonmises_gen

### Community 404 - "Community 404"
Cohesion: 0.17
Nodes (2): r"""A Student's t continuous random variable.      For the noncentral t distribu, t_gen

### Community 405 - "Community 405"
Cohesion: 0.17
Nodes (2): r"""A Rayleigh continuous random variable.      %(before_notes)s      Notes, rayleigh_gen

### Community 406 - "Community 406"
Cohesion: 0.17
Nodes (2): planck_gen, r"""A Planck discrete exponential random variable.      %(before_notes)s      Se

### Community 407 - "Community 407"
Cohesion: 0.17
Nodes (3): randint_gen, r"""A uniform discrete random variable.      %(before_notes)s      Notes     ---, An array of *size* random integers >= ``low`` and < ``high``.

### Community 408 - "Community 408"
Cohesion: 0.21
Nodes (7): _ABW, ansari(), Distribution of Ansari-Bradley W-statistic under the null hypothesis., When necessary, recalculate exact distribution., Probability mass function., Cumulative distribution function., Perform the Ansari-Bradley test for equal scale parameters.      The Ansari-Brad

### Community 409 - "Community 409"
Cohesion: 0.17
Nodes (12): boxcox(), _boxcox_conf_interval(), _boxcox_inv_lmbda(), boxcox_llf(), boxcox_normmax(), _log_mean(), _log_var(), r"""Return a dataset transformed by a Box-Cox power transformation.      Paramet (+4 more)

### Community 410 - "Community 410"
Cohesion: 0.17
Nodes (6): Get the mean of the transforms.          The mean of a set of transforms is the, Compose this transform with itself `n` times.          A rigid transform `p` whe, Invert this transform.          Composition of a transform with its inverse resu, Iterate over transforms., Create a RigidTransform skipping all sanitization steps.          This method is, Initialize an identity transform.          Composition with the identity transfo

### Community 411 - "Community 411"
Cohesion: 0.29
Nodes (7): Py_gssv(), Py_gstrf(), Py_gstrs(), XDestroy_CompCol_Matrix(), XDestroy_SuperMatrix_Store(), XDestroy_SuperNode_Matrix(), XStatFree()

### Community 412 - "Community 412"
Cohesion: 0.24
Nodes (10): Enum, BackendSupportStatus, calculate_table_statistics(), is_inherently_out_of_scope(), make_flat_capabilities_table(), _process_capabilities_table_entry(), Generate flat tables showing Array API capabilities for use in docs.  These tabl, Generate full table of array api capabilities across public functions.      Para (+2 more)

### Community 413 - "Community 413"
Cohesion: 0.22
Nodes (3): Determine the `MF` parameter (Method Flag) for the Fortran subroutine `dvode`., vode, zvode

### Community 414 - "Community 414"
Cohesion: 0.18
Nodes (6): PackedMatrix, A simplified CSR format for when non-zeros in each row are consecutive.      Ass, Builds augmented banded matrix.      Parameters     ----------     A : PackedMat, Solve the 2-D tensor-product spline system using separable banded QR.      =====, _solve_2d_fitpack(), _stack_augmented_fitpack()

### Community 415 - "Community 415"
Cohesion: 0.29
Nodes (10): _calc_score(), _common_input_validation(), _doubly_stochastic(), quadratic_assignment(), _quadratic_assignment_2opt(), _quadratic_assignment_faq(), r"""     Approximates solution to the quadratic assignment problem and     the g, r"""Solve the quadratic assignment problem (approximately).      This function s (+2 more)

### Community 416 - "Community 416"
Cohesion: 0.18
Nodes (11): bode_signature(), cont2discrete_signature(), dimpulse_signature(), dlsim_signature(), dstep_signature(), freqresp_signature(), impulse_signature(), lsim_signature() (+3 more)

### Community 417 - "Community 417"
Cohesion: 0.25
Nodes (10): _fit_edge(), _fit_edges_polyfit(), _polyder(), Compute the coefficients for a 1-D Savitzky-Golay FIR filter.      Parameters, Differentiate polynomials represented with coefficients.      p must be a 1-D or, Given an N-d array `x` and the specification of a slice of `x` from     `window_, Use polynomial interpolation of x at the low and high ends of the axis     to fi, Apply a Savitzky-Golay filter to an array.      This is a 1-D filter. If `x`  ha (+2 more)

### Community 419 - "Community 419"
Cohesion: 0.20
Nodes (9): r"""Spherical Bessel function of the second kind or its derivative.      Defined, r"""Modified spherical Bessel function of the first kind or its derivative., r"""Modified spherical Bessel function of the second kind or its derivative., r"""Spherical Bessel function of the first kind or its derivative.      Defined, spherical_in(), spherical_jn(), spherical_kn(), spherical_kn_reflection() (+1 more)

### Community 420 - "Community 420"
Cohesion: 0.33
Nodes (9): clanbpro(), csafescal(), dlanbpro(), dsafescal(), int_max(), slanbpro(), ssafescal(), zlanbpro() (+1 more)

### Community 421 - "Community 421"
Cohesion: 0.33
Nodes (10): matrix_squareroot_c(), matrix_squareroot_d(), matrix_squareroot_s(), matrix_squareroot_z(), sqrtm_recursion_c(), sqrtm_recursion_d(), sqrtm_recursion_s(), sqrtm_recursion_z() (+2 more)

### Community 422 - "Community 422"
Cohesion: 0.20
Nodes (2): _apply_filter(), _apply_filter_gain()

### Community 423 - "Community 423"
Cohesion: 0.24
Nodes (9): _cmpkey(), InvalidVersion, parse(), _parse_letter_version(), _parse_local_version(), Initialize a Version object.          :param version:             The string rep, Parse the given version string.      >>> parse('1.0.dev1')     <Version('1.0.dev, Takes a string like abc.1.twelve and turns it into ("abc", 1, "twelve"). (+1 more)

### Community 424 - "Community 424"
Cohesion: 0.18
Nodes (2): cosine_gen, r"""A cosine continuous random variable.      %(before_notes)s      Notes     --

### Community 425 - "Community 425"
Cohesion: 0.20
Nodes (4): exponweib_gen, _pow1pm1(), Compute (1 + x)**y - 1.      Uses expm1 and xlog1py to avoid loss of precision w, r"""An exponentiated Weibull continuous random variable.      %(before_notes)s

### Community 426 - "Community 426"
Cohesion: 0.18
Nodes (2): f_gen, r"""An F continuous random variable.      For the noncentral F distribution, see

### Community 427 - "Community 427"
Cohesion: 0.18
Nodes (2): halfcauchy_gen, r"""A Half-Cauchy continuous random variable.      %(before_notes)s      Notes

### Community 428 - "Community 428"
Cohesion: 0.18
Nodes (2): halflogistic_gen, r"""A half-logistic continuous random variable.      %(before_notes)s      Notes

### Community 429 - "Community 429"
Cohesion: 0.18
Nodes (2): invweibull_gen, An inverted Weibull continuous random variable.      This distribution is also k

### Community 430 - "Community 430"
Cohesion: 0.18
Nodes (2): laplace_asymmetric_gen, r"""An asymmetric Laplace continuous random variable.      %(before_notes)s

### Community 431 - "Community 431"
Cohesion: 0.18
Nodes (2): ncf_gen, r"""A non-central F distribution continuous random variable.      %(before_notes

### Community 432 - "Community 432"
Cohesion: 0.18
Nodes (2): r"""Weibull maximum continuous random variable.      The Weibull Maximum Extreme, weibull_max_gen

### Community 433 - "Community 433"
Cohesion: 0.18
Nodes (2): r"""A Yule-Simon discrete random variable.      %(before_notes)s      Notes, yulesimon_gen

### Community 434 - "Community 434"
Cohesion: 0.20
Nodes (7): normalize_dual_quaternion(), Apply the transform to a vector.          If the original frame transforms to th, Select the backend for the given array library.      We need this selection func, Normalize dual quaternion., r"""Initialize from exponential coordinates of transform.          This implemen, Initialize from a unit dual quaternion.          Unit dual quaternions encode or, select_backend()

### Community 435 - "Community 435"
Cohesion: 0.24
Nodes (9): AssertionError, assert_deallocated(), gc_state(), Module for testing automatic garbage collection of objects  .. autosummary::, Set status of garbage collector, Context manager to set state of garbage collector to `state`      Parameters, Context manager to check that object is deallocated      This is useful for chec, ReferenceError (+1 more)

### Community 436 - "Community 436"
Cohesion: 0.20
Nodes (7): convert_temperature(), lambda2nu(), nu2lambda(), Collection of physical constants and conversion factors.  Most constants are in, Convert from a temperature scale to another one among Celsius, Kelvin,     Fahre, Convert wavelength to optical frequency.      Parameters     ----------     lamb, Convert optical frequency to wavelength.      Parameters     ----------     nu :

### Community 437 - "Community 437"
Cohesion: 0.36
Nodes (7): get_tls_global(), mc64ad_(), mc64id_(), superlu_python_jmpbuf(), superlu_python_module_abort(), superlu_python_module_free(), superlu_python_module_malloc()

### Community 438 - "Community 438"
Cohesion: 0.38
Nodes (9): dct(), dctn(), dst(), dstn(), _execute(), idct(), idctn(), idst() (+1 more)

### Community 439 - "Community 439"
Cohesion: 0.20
Nodes (7): find_integrator(), # NOTE: The C code modifies y in place, hence the copy., Set integrator by name.          Parameters         ----------         name : st, # FIXME: this really should be raise an exception. Will that break, Convert a real matrix of the form (for example)          [0 0 A B]        [0 0 0, # IMPORTANT: Must NOT use self.tmp here, as it may alias with y!, _transform_banded_jac()

### Community 440 - "Community 440"
Cohesion: 0.20
Nodes (10): _get_fitpack_packed_column(), _lsq_clamp_preprocess(), _lsq_solve_qr(), _lsq_solve_qr_clamp_values(), Apply the clamp preprocessing to packed matrix + RHS for the QR path.          A, Solve for the LSQ spline coeffs given x, y and knots.      `y` is always 2D: for, Solve for the LSQ spline coeffs given x, y, knots and clamp_values.          `y`, Extract conceptual dense column j from packed storage. (+2 more)

### Community 441 - "Community 441"
Cohesion: 0.22
Nodes (4): LSODA, LsodaDenseOutput, # IMPORTANT: Must copy solver._y because the C code reuses the same, Adams/BDF method with automatic stiffness detection and switching.      This is

### Community 442 - "Community 442"
Cohesion: 0.31
Nodes (9): assert_almost_equal(), assert_array_almost_equal(), _check_scalar(), Extra testing functions that forbid 0d-input, see #21044  While the xp_assert_*, Backwards compatible replacement. In new code, use xp_assert_close instead., Backwards compatible replacement. In new code, use xp_assert_close instead., xp_assert_close(), xp_assert_equal() (+1 more)

### Community 443 - "Community 443"
Cohesion: 0.31
Nodes (7): CData, _get_cffi_data(), _get_cffi_func(), _get_ctypes_data(), _get_ctypes_func(), _import_cffi(), _typename_from_ctypes()

### Community 444 - "Community 444"
Cohesion: 0.24
Nodes (9): find_best_blas_type(), get_blas_funcs(), _get_funcs(), _memoize_get_funcs(), Low-level BLAS functions (:mod:`scipy.linalg.blas`) ============================, Find best-matching BLAS/LAPACK type.      Arrays are used to determine the optim, Return available BLAS/LAPACK functions.      Used also in lapack.py. See get_bla, Memoized fast path for _get_funcs instances (+1 more)

### Community 445 - "Community 445"
Cohesion: 0.20
Nodes (7): lu(), lu_factor(), lu_solve(), LU decomposition functions., Solve an equation system, ``a @ x = b``, given the LU factorization of a.      T, Compute pivoted LU decomposition of a matrix.      The decomposition is::, Compute LU decomposition of a matrix with partial pivoting.      The decompositi

### Community 446 - "Community 446"
Cohesion: 0.24
Nodes (5): ordqz(), _qz(), QZ decomposition for generalized eigenvalues of a pair of matrices.      The QZ,, QZ decomposition for a pair of matrices with reordering.      Parameters     ---, _select_function()

### Community 447 - "Community 447"
Cohesion: 0.24
Nodes (7): _castCopy(), _commonType(), Schur decomposition functions., Compute Schur decomposition of a matrix.      The Schur decomposition is::, Convert real Schur form to complex Schur form.      Convert a quasi-diagonal rea, rsf2csf(), schur()

### Community 448 - "Community 448"
Cohesion: 0.20
Nodes (3): _CustomLinearOperator, Determine the dtype by executing `matvec` on an `int8` test vector.          In, Linear operator defined in terms of user-specified operations.

### Community 449 - "Community 449"
Cohesion: 0.20
Nodes (4): _onenormest_product(), ProductOperator, For now, this is limited to products of multiple square matrices., Efficiently estimate the 1-norm of the matrix product of the args.      Paramete

### Community 450 - "Community 450"
Cohesion: 0.22
Nodes (5): _AProd, # TODO: once `svds` drops legacy positional `random_state` support,, Wrapper class for linear operator      The call signature of the __call__ method, Compute the singular value decomposition of a linear operator using PROPACK, _svdp()

### Community 451 - "Community 451"
Cohesion: 0.20
Nodes (5): build_quadratic_1d(), Functions used by least-squares algorithms., Parameterize a multivariate quadratic function along a line.      The resulting, Return a matrix arising in regularized least squares as LinearOperator.      The, regularized_lsq_operator()

### Community 452 - "Community 452"
Cohesion: 0.20
Nodes (10): _complex_via_real_components(), convolve1d(), correlate1d(), prewitt(), Complex convolution via a linear combination of real convolutions., Calculate a 1-D correlation along the given axis.      The lines of the array al, Calculate a 1-D convolution along the given axis.      The lines of the array al, Calculate a Prewitt filter.      Parameters     ----------     %(input)s     %(a (+2 more)

### Community 453 - "Community 453"
Cohesion: 0.20
Nodes (9): bracket_minimum(), bracket_root(), find_minimum(), find_root(), =================================================================== Elementwise, Find the root of a monotonic, real-valued function of a real variable.      For, Find the minimum of a unimodal, real-valued function of a real variable.      Fo, Bracket the root of a monotonic, real-valued function of a real variable.      F (+1 more)

### Community 454 - "Community 454"
Cohesion: 0.20
Nodes (2): DiagBroyden, Find a root of a function, using diagonal Broyden Jacobian approximation.      T

### Community 455 - "Community 455"
Cohesion: 0.20
Nodes (2): ExcitingMixing, Find a root of a function, using a tuned diagonal Jacobian approximation.      T

### Community 456 - "Community 456"
Cohesion: 0.29
Nodes (9): _complex2real(), Spectral Algorithm for Nonlinear Equations, Wrap a function and an initial value so that (i) complex values     are wrapped, r"""     Solve nonlinear equation with the DF-SANE method      Options     -----, Convert from real to complex and reshape result arrays., _real2complex(), _root_df_sane(), _wrap_func() (+1 more)

### Community 457 - "Community 457"
Cohesion: 0.20
Nodes (10): _arc_jac_sc1(), _arc_jac_sn(), ellipap(), _ellipdeg(), _pow10m1(), 10 ** x - 1 for x near 0, Solve degree equation using nomes      Given n, m1, solve        n * K(m) / K'(m, Inverse Jacobian elliptic sn      Solve for z in w = sn(z, m)      Parameters (+2 more)

### Community 458 - "Community 458"
Cohesion: 0.22
Nodes (7): _calc_dual_canonical_window(), closest_STFT_dual_window(), Implementation of an FFT-based Short-time Fourier Transform., Dual window (canonical dual window by default).          A STFT can be interpret, Calculate canonical dual window for 1d window `win` and a time step     of `hop`, r"""Instantiate a `ShortTimeFFT` by only providing a dual window.          If an, r"""Calculate the STFT dual window of a given window closest to a desired dual

### Community 459 - "Community 459"
Cohesion: 0.24
Nodes (7): _check_mode(), _pad_h(), Upsample, FIR filter, and downsample.      Parameters     ----------     h : arr, Store coefficients in a transposed, flipped arrangement.      For example, suppo, Helper for resampling., Apply the prepared filter to the specified axis of N-D signal x., _UpFIRDn

### Community 460 - "Community 460"
Cohesion: 0.20
Nodes (7): find(), Functions to extract parts of sparse matrices, Return the upper triangular portion of a sparse array or matrix.      Returns th, Return the indices and values of the nonzero elements of a matrix.      Paramete, Return the lower triangular portion of a sparse array or matrix.      Returns th, tril(), triu()

### Community 461 - "Community 461"
Cohesion: 0.20
Nodes (10): jn_zeros(), jnp_zeros(), jnyn_zeros(), Compute nt zeros of Bessel functions Jn(x), Jn'(x), Yn(x), and Yn'(x).      Retu, r"""Compute zeros of integer-order Bessel functions Jn.      Compute `nt` zeros, r"""Compute zeros of integer-order Bessel function derivatives Jn'.      Compute, r"""Compute zeros of integer-order Bessel function Yn(x).      Compute `nt` zero, r"""Compute zeros of integer-order Bessel function derivatives Yn'(x).      Comp (+2 more)

### Community 463 - "Community 463"
Cohesion: 0.20
Nodes (10): chebyc(), chebyt(), r"""Gauss-Chebyshev (first kind) quadrature.      Computes the sample points and, r"""Chebyshev polynomial of the first kind.      Defined to be the solution of, r"""Gauss-Chebyshev (first kind) quadrature.      Compute the sample points and, r"""Chebyshev polynomial of the first kind on :math:`[-2, 2]`.      Defined as :, r"""Gauss-Chebyshev (first kind, shifted) quadrature.      Compute the sample po, roots_chebyc() (+2 more)

### Community 464 - "Community 464"
Cohesion: 0.20
Nodes (10): hermite(), _newton(), _pbcf(), r"""Gauss-Hermite (physicist's) quadrature.      Compute the sample points and w, r"""Asymptotic series expansion of parabolic cylinder function      The implemen, Newton iteration for polishing the asymptotic approximation     to the zeros of, r"""Gauss-Hermite (physicist's) quadrature for large n.      Computes the sample, r"""Physicist's Hermite polynomial.      Defined by      .. math::          H_n( (+2 more)

### Community 466 - "Community 466"
Cohesion: 0.22
Nodes (2): intMalloc(), SetIWork()

### Community 468 - "Community 468"
Cohesion: 0.20
Nodes (2): hypsecant_gen, r"""A hyperbolic secant continuous random variable.      %(before_notes)s      N

### Community 469 - "Community 469"
Cohesion: 0.20
Nodes (2): kappa3_gen, r"""Kappa 3 parameter distribution.      %(before_notes)s      Notes     -----

### Community 470 - "Community 470"
Cohesion: 0.20
Nodes (2): kstwo_gen, r"""Kolmogorov-Smirnov two-sided test statistic distribution.      This is the d

### Community 471 - "Community 471"
Cohesion: 0.20
Nodes (2): loglaplace_gen, r"""A log-Laplace continuous random variable.      %(before_notes)s      Notes

### Community 472 - "Community 472"
Cohesion: 0.20
Nodes (2): r"""A triangular continuous random variable.      %(before_notes)s      Notes, triang_gen

### Community 473 - "Community 473"
Cohesion: 0.20
Nodes (2): r"""A Tukey-Lambda continuous random variable.      %(before_notes)s      Notes, tukeylambda_gen

### Community 474 - "Community 474"
Cohesion: 0.20
Nodes (2): r"""An R-distributed (symmetric beta) continuous random variable.      %(before_, rdist_gen

### Community 475 - "Community 475"
Cohesion: 0.20
Nodes (2): r"""A semicircular continuous random variable.      %(before_notes)s      See Al, semicircular_gen

### Community 476 - "Community 476"
Cohesion: 0.20
Nodes (2): r"""     A trapezoidal continuous random variable.      %(before_notes)s      No, trapezoid_gen

### Community 477 - "Community 477"
Cohesion: 0.24
Nodes (9): istft_compare(), _istft_wrapper(), Helpers to utilize existing stft / istft tests for testing `ShortTimeFFT`.  This, Wrapper for the SciPy `istft()` function based on `ShortTimeFFT` for         uni, Assert that the results from the existing `stft()` and `_stft_wrapper()`     are, Assert that the results from the existing `istft()` and     `_istft_wrapper()` a, Wrapper for the SciPy `stft()` function based on `ShortTimeFFT` for     unit tes, stft_compare() (+1 more)

### Community 479 - "Community 479"
Cohesion: 0.39
Nodes (8): _chlrps(), _gaminv(), _Phi(), _Phinv(), _primes(), _qsimvtv(), Computes permuted and scaled lower Cholesky factor c for R which may be     sing, Estimates the multivariate t CDF using randomized QMC      Parameters     ------

### Community 480 - "Community 480"
Cohesion: 0.22
Nodes (3): DenseOutput, Dop853DenseOutput, RkDenseOutput

### Community 481 - "Community 481"
Cohesion: 0.31
Nodes (7): derivative(), _derivative_iv(), hessian(), jacobian(), r"""Evaluate the Jacobian of a function numerically.      Parameters     -------, Evaluate the derivative of an elementwise, real scalar function numerically., r"""Evaluate the Hessian of a function numerically.      Parameters     --------

### Community 482 - "Community 482"
Cohesion: 0.33
Nodes (8): fht(), fhtcoeff(), fhtoffset(), _fhtq(), ifht(), Return optimal offset for a fast Hankel transform.      Returns an offset close, Compute the biased fast Hankel transform.      This is the basic FFTLog routine., Compute the coefficient array for a fast Hankel transform.

### Community 483 - "Community 483"
Cohesion: 0.22
Nodes (6): _good_shape(), next_fast_len(), Ensure that shape argument is valid for scipy.fftpack      scipy.fftpack does no, DFT sample frequencies (for usage with rfft, irfft).      The returned float arr, Find the next fast size of input data to `fft`, for zero-padding, etc.      SciP, rfftfreq()

### Community 484 - "Community 484"
Cohesion: 0.25
Nodes (9): is_valid_im(), is_valid_linkage(), _lazy_valid_checks(), Return True if the inconsistency matrix passed is valid.      It must be a :math, Variant of `is_valid_im` to be called internally by other scipy functions,     w, Check the validity of a linkage matrix.      A linkage matrix is valid if it is, Variant of `is_valid_linkage` to be called internally by other scipy functions,, Validate a set of conditions on the contents of possibly lazy arrays.      Param (+1 more)

### Community 485 - "Community 485"
Cohesion: 0.22
Nodes (2): dop853, dopri5

### Community 486 - "Community 486"
Cohesion: 0.22
Nodes (3): _PPolyBase, Base class for piecewise polynomials -- NumPy backend., c and x may be modified by the user. The Cython code expects         that they a

### Community 487 - "Community 487"
Cohesion: 0.22
Nodes (5): Perform a single Runge-Kutta step.      This function computes a prediction of a, Base class for explicit Runge-Kutta methods., rk_step(), RungeKutta, OdeSolver

### Community 488 - "Community 488"
Cohesion: 0.28
Nodes (2): These are situations that can be tested in our pythran tests:     - A function w, _TestPythranFunc

### Community 489 - "Community 489"
Cohesion: 0.31
Nodes (8): ldl(), _ldl_construct_tri_factor(), _ldl_get_d_and_l(), _ldl_sanitize_ipiv(), This helper function takes the rather strangely encoded permutation array     re, Computes the LDLt or Bunch-Kaufman factorization of a symmetric/     hermitian m, Helper function to extract the diagonal and triangular matrices for     LDL.T fa, Helper function to construct explicit outer factors of LDL factorization.      I

### Community 490 - "Community 490"
Cohesion: 0.22
Nodes (6): bandwidth(), _datacopied(), norm(), Strict check for `arr` not sharing any data with `original`,     under the assum, Return the lower and upper bandwidth of a numeric array.      Parameters     ---, Matrix or vector norm.      This function is able to return one of eight differe

### Community 491 - "Community 491"
Cohesion: 0.31
Nodes (8): dogbox(), dogleg_step(), find_intersection(), lsmr_operator(), Dogleg algorithm with rectangular trust regions for least-squares minimization., Find dogleg step in a rectangular region.      Returns     -------     step : nd, Compute LinearOperator to use in LSMR by dogbox algorithm.      `active_set` mas, Find intersection of trust-region bounds and initial bounds.      Returns     --

### Community 492 - "Community 492"
Cohesion: 0.31
Nodes (8): backtracking(), The adaptation of Trust Region Reflective algorithm for a linear least-squares p, Solve regularized least squares using information from QR-decomposition.      Th, Find an appropriate step size using backtracking line search., Select the best step according to Trust Region Reflective algorithm., regularized_lsq_with_qr(), select_step(), trf_linear()

### Community 493 - "Community 493"
Cohesion: 0.22
Nodes (6): _extend_mode_to_code(), _normalize_sequence(), array or dtype' polymorphism.      Return None for np.int8, dtype('float32') or, Convert an extension mode to the corresponding integer code., If input is a scalar, create a sequence of length equal to the     rank by dupli, _skip_if_dtype()

### Community 494 - "Community 494"
Cohesion: 0.22
Nodes (2): LinearMixing, Find a root of a function, using a scalar Jacobian approximation.      .. warnin

### Community 495 - "Community 495"
Cohesion: 0.33
Nodes (5): _bisect(), _brenth(), _brentq(), call_solver(), _ridder()

### Community 496 - "Community 496"
Cohesion: 0.22
Nodes (9): freqz(), freqz_sos(), Compute the frequency response of a digital filter.      Given the M-order numer, Helper to validate a SOS input, r"""     Compute the frequency response of a digital filter in SOS format., Compute the frequency response of a digital filter in SOS format (legacy).     ., _real_dtype_for_complex(), sosfreqz() (+1 more)

### Community 497 - "Community 497"
Cohesion: 0.33
Nodes (8): get_thunk_type_set(), main(), newer(), parse_routine(), Return true if 'source' exists and is more recently modified than     'target',, Get a list containing cartesian product of data types, plus a getter routine., Generate thunk and method code for a given routine.      Parameters     --------, write_autogen_blurb()

### Community 498 - "Community 498"
Cohesion: 0.39
Nodes (8): _adjust_bounds(), convex_hull_plot_2d(), delaunay_plot_2d(), _get_axes(), Plot the given Voronoi diagram in 2-D.      Parameters     ----------     vor :, Plot the given Delaunay triangulation in 2-D.      Parameters     ----------, Plot the given convex hull diagram in 2-D.      Parameters     ----------     hu, voronoi_plot_2d()

### Community 500 - "Community 500"
Cohesion: 0.28
Nodes (8): _elements_and_indices_with_max_real(), log_softmax(), logsumexp(), Compute the log of the sum of exponentials of input elements.      Parameters, r"""Compute the softmax function.      The softmax function transforms each elem, r"""Compute the logarithm of the softmax function.      In principle::, softmax(), _wrap_radians()

### Community 501 - "Community 501"
Cohesion: 0.25
Nodes (2): z_abs(), z_sgn()

### Community 502 - "Community 502"
Cohesion: 0.28
Nodes (4): csgemm_kernel(), csgemm_ovwr_left(), zdgemm_kernel(), zdgemm_ovwr_left()

### Community 503 - "Community 503"
Cohesion: 0.25
Nodes (2): c_abs(), c_sgn()

### Community 504 - "Community 504"
Cohesion: 0.31
Nodes (4): CovViaDiagonal, _dot_diag(), Check whether x lies in the support of the distribution., r"""         Return a representation of a covariance matrix from its diagonal.

### Community 505 - "Community 505"
Cohesion: 0.22
Nodes (2): betabinom_gen, r"""     A beta-binomial discrete random variable.      %(before_notes)s      Se

### Community 506 - "Community 506"
Cohesion: 0.22
Nodes (2): boltzmann_gen, r"""A Boltzmann (Truncated Discrete Exponential) random variable.      %(before_

### Community 507 - "Community 507"
Cohesion: 0.22
Nodes (2): dlaplace_gen, r"""A  Laplacian discrete random variable.      %(before_notes)s      Notes

### Community 508 - "Community 508"
Cohesion: 0.22
Nodes (2): nhypergeom_gen, r"""A negative hypergeometric discrete random variable.      Consider a box cont

### Community 509 - "Community 509"
Cohesion: 0.22
Nodes (2): r"""A Zipfian discrete random variable.      %(before_notes)s      See Also, zipfian_gen

### Community 510 - "Community 510"
Cohesion: 0.22
Nodes (7): cramervonmises(), cramervonmises_2samp(), CramerVonMisesResult, _pval_cvm_2samp_exact(), Compute the exact p-value of the Cramer-von Mises two-sample test     for a give, r"""Perform the two-sample Cramér-von Mises test for goodness of fit.      This, r"""Perform the one-sample Cramér-von Mises test for goodness of fit.      This

### Community 511 - "Community 511"
Cohesion: 0.25
Nodes (6): Result of `scipy.stats.tukey_hsd`.      Attributes     ----------     statistic, Compute the confidence interval for the specified confidence level.          Par, Perform Tukey's HSD test for equality of means over multiple treatments.      Tu, tukey_hsd(), _tukey_hsd_iv(), TukeyHSDResult

### Community 512 - "Community 512"
Cohesion: 0.25
Nodes (9): _chk2_asarray(), Calculates the T-test for the mean of ONE group of scores.      Parameters     -, Calculates the T-test for the means of TWO INDEPENDENT samples of scores.      P, Calculates the T-test on TWO RELATED samples of scores, a and b.      Parameters, Common code between all 3 t-test functions., ttest_1samp(), _ttest_finish(), ttest_ind() (+1 more)

### Community 513 - "Community 513"
Cohesion: 0.25
Nodes (7): get_blas_macro_and_name(), Helper functions and variables for generation of BLAS/LAPACK wrappers., Complex-valued and some Accelerate functions have special symbols., Takes a mapping of full filepath to file contents to write at that path., Read BLAS/LAPACK signatures and split into name, return type, argument     names, read_signatures(), write_files()

### Community 514 - "Community 514"
Cohesion: 0.36
Nodes (7): ascent(), electrocardiogram(), face(), fetch_data(), Get a 1024 x 768, color image of a raccoon face.      The image is derived from, Get an 8-bit grayscale bit-depth, 512 x 512 derived image for easy     use in de, Load an electrocardiogram as an example for a 1-D signal.      The returned sign

### Community 515 - "Community 515"
Cohesion: 0.36
Nodes (6): check_option(), _highs_wrapper(), Solve linear programs using HiGHS [1]_.      Assume problems of the form:, _constraints_to_components(), milp(), _milp_iv()

### Community 516 - "Community 516"
Cohesion: 0.25
Nodes (7): _coeff_of_divided_diff(), _compute_optimal_gcv_parameter(), make_smoothing_spline(), Returns a design matrix as a CSR format sparse array.          Parameters, Returns an optimal regularization parameter from the GCV criteria [1].      Para, Returns the coefficients of the divided difference.      Parameters     --------, r"""     Create a smoothing B-spline satisfying the Generalized Cross Validation

### Community 517 - "Community 517"
Cohesion: 0.36
Nodes (6): _build_and_solve_system(), _build_evaluation_coefficients(), _build_system(), compute_interpolation(), polynomial_matrix(), Build and solve the RBF interpolation system of equations.      Parameters     -

### Community 518 - "Community 518"
Cohesion: 0.29
Nodes (4): _make_tuple_bunch(), Create a namedtuple-like class with additional attributes.      This function cr, Ensure that all the given names are valid Python identifiers that     do not sta, _validate_names()

### Community 519 - "Community 519"
Cohesion: 0.39
Nodes (7): _check_termination(), _initialize(), _loop(), _prepare_result(), Main loop of a vectorized scalar optimization algorithm      Parameters     ----, Initialize abscissa, function, and args arrays for elementwise function      Par, _update_active()

### Community 520 - "Community 520"
Cohesion: 0.46
Nodes (7): next_double(), next_uint32(), next_uint64(), random_interval(), random_normal(), random_standard_normal(), random_standard_uniform()

### Community 521 - "Community 521"
Cohesion: 0.32
Nodes (7): funm_multiply_krylov(), _funm_multiply_krylov_arnoldi(), _funm_multiply_krylov_lanczos(), Restared Krylov method for evaluating f(A)b    The original code was written in, A restarted Krylov method for evaluating ``y = f(tA) b`` from [1]_ [2]_.      Pa, The Arnoldi iteration for constructing the basis V and the projection H = V * A, The Lanczos iteration for constructing the basis V and the projection H = V * A

### Community 522 - "Community 522"
Cohesion: 0.25
Nodes (2): Wrapper class for hess calculation via finite differences, _ScalarHessWrapper

### Community 523 - "Community 523"
Cohesion: 0.32
Nodes (2): KrylovJacobian, Find a root of a function, using Krylov approximation for inverse Jacobian.

### Community 524 - "Community 524"
Cohesion: 0.36
Nodes (4): convert_shape_to_errmsg(), RawFilter(), scipy_signal__sigtools_linear_filter(), zfill()

### Community 525 - "Community 525"
Cohesion: 0.29
Nodes (2): convert_strides(), FIRsepsym2d()

### Community 526 - "Community 526"
Cohesion: 0.29
Nodes (5): count_blocks(), estimate_blocksize(), Functions that operate on sparse matrices, Attempt to determine the blocksize of a sparse matrix      Returns a blocksize=(, For a given blocksize=(r,c) count the number of occupied     blocks in a sparse

### Community 527 - "Community 527"
Cohesion: 0.39
Nodes (5): allocate_std_vector_typenum(), array_from_std_vector_and_free(), c_array_from_object(), call_thunk(), free_std_vector_typenum()

### Community 528 - "Community 528"
Cohesion: 0.25
Nodes (8): _copy_array_if_base_present(), is_valid_dm(), num_obs_dm(), Copy the array if its base points to a parent array., Convert a vector-form distance vector to a square-form distance     matrix, and, Return True if input array satisfies basic distance matrix properties     (symme, Return the number of original observations that correspond to a     square, redu, squareform()

### Community 529 - "Community 529"
Cohesion: 0.29
Nodes (7): ellip_harm(), ellip_harm_2(), ellip_normal(), _ellip_normal_vec(), r"""     Ellipsoidal harmonic functions :math:`F^p_n(s)`.      These are also kn, r"""     Ellipsoidal harmonic normalization constants :math:`\gamma^p_n`.      T, r"""     Ellipsoidal harmonic functions :math:`E^p_n(s)`.      These are also kn

### Community 530 - "Community 530"
Cohesion: 0.25
Nodes (8): _compute_tauk(), _initial_nodes(), _initial_nodes_a(), _initial_nodes_b(), Helper function for Tricomi initial guesses      For details, see formula 3.1 in, r"""Tricomi initial guesses      Computes an initial approximation to the square, r"""Gatteschi initial guesses      Computes an initial approximation to the squa, Initial guesses for the Hermite roots      Computes an initial approximation to

### Community 531 - "Community 531"
Cohesion: 0.46
Nodes (7): cDumpLine(), cParseFloatFormat(), cParseIntFormat(), creadhb(), cReadValues(), FormFullA(), ReadVector()

### Community 532 - "Community 532"
Cohesion: 0.46
Nodes (7): cDumpLine(), cParseFloatFormat(), cParseIntFormat(), creadrb(), cReadValues(), FormFullA(), ReadVector()

### Community 533 - "Community 533"
Cohesion: 0.39
Nodes (6): dopcor(), dopri5(), dopri853(), dp86co(), hinit(), hinit853()

### Community 534 - "Community 534"
Cohesion: 0.46
Nodes (7): dDumpLine(), dParseFloatFormat(), dParseIntFormat(), dreadhb(), dReadValues(), FormFullA(), ReadVector()

### Community 535 - "Community 535"
Cohesion: 0.46
Nodes (7): dDumpLine(), dParseFloatFormat(), dParseIntFormat(), dreadrb(), dReadValues(), FormFullA(), ReadVector()

### Community 536 - "Community 536"
Cohesion: 0.32
Nodes (3): _ComputeFT(), NI_EuclideanFeatureTransform(), _VoronoiFT()

### Community 537 - "Community 537"
Cohesion: 0.46
Nodes (7): FormFullA(), ReadVector(), sDumpLine(), sParseFloatFormat(), sParseIntFormat(), sreadhb(), sReadValues()

### Community 538 - "Community 538"
Cohesion: 0.46
Nodes (7): FormFullA(), ReadVector(), sDumpLine(), sParseFloatFormat(), sParseIntFormat(), sreadrb(), sReadValues()

### Community 539 - "Community 539"
Cohesion: 0.25
Nodes (1): _BaseVersion

### Community 540 - "Community 540"
Cohesion: 0.46
Nodes (7): FormFullA(), ReadVector(), zDumpLine(), zParseFloatFormat(), zParseIntFormat(), zreadhb(), zReadValues()

### Community 541 - "Community 541"
Cohesion: 0.46
Nodes (7): FormFullA(), ReadVector(), zDumpLine(), zParseFloatFormat(), zParseIntFormat(), zreadrb(), zReadValues()

### Community 542 - "Community 542"
Cohesion: 0.25
Nodes (3): CovViaEigendecomposition, r"""         Representation of a covariance provided via eigendecomposition., Check whether x lies in the support of the distribution.

### Community 543 - "Community 543"
Cohesion: 0.25
Nodes (2): betanbinom_gen, r"""     A beta-negative-binomial discrete random variable.      %(before_notes)

### Community 544 - "Community 544"
Cohesion: 0.25
Nodes (2): logser_gen, r"""A Logarithmic (Log-Series, Series) discrete random variable.      %(before_n

### Community 545 - "Community 545"
Cohesion: 0.25
Nodes (8): barnard_exact(), BarnardExactResult, boschloo_exact(), BoschlooExactResult, _compute_log_combinations(), Compute all log combination of C(n, k)., r"""Perform a Barnard exact test on a 2x2 contingency table.      Parameters, r"""Perform Boschloo's exact test on a 2x2 contingency table.      Parameters

### Community 546 - "Community 546"
Cohesion: 0.25
Nodes (4): _ProbabilityDistribution, r"""Cumulative distribution function          The cumulative distribution functi, r"""Complementary cumulative distribution function          The complementary cu, r"""Variance (central second moment)          Parameters         ----------

### Community 547 - "Community 547"
Cohesion: 0.32
Nodes (4): MultivariateNormalQMC, r"""QMC sampling from a multivariate Normal :math:`N(\mu, \Sigma)`.      Paramet, Draw `n` QMC samples from the multivariate Normal.          Parameters         -, Draw `n` QMC samples from the standard Normal :math:`N(0, I_d)`.          Parame

### Community 548 - "Community 548"
Cohesion: 0.32
Nodes (6): Compute the relative risk (also known as the risk ratio).      This function com, Result of `scipy.stats.contingency.relative_risk`.      Attributes     ---------, Compute the confidence interval for the relative risk.          The confidence i, relative_risk(), RelativeRiskResult, _validate_int()

### Community 549 - "Community 549"
Cohesion: 0.25
Nodes (6): pack_TtestResult(), Result of a t-test.      See the documentation of the particular t-test function, Parameters         ----------         confidence_level : float             The c, _t_confidence_interval(), TtestResult, TtestResultBase

### Community 550 - "Community 550"
Cohesion: 0.29
Nodes (6): Partial singular value decomposition of a sparse matrix using LOBPCG.      Compu, Partial singular value decomposition of a sparse matrix using PROPACK.      Comp, Partial singular value decomposition of a sparse matrix using ARPACK.      Compu, _svds_arpack_doc(), _svds_lobpcg_doc(), _svds_propack_doc()

### Community 551 - "Community 551"
Cohesion: 0.29
Nodes (4): EchoBackend, NumPyBackend, Backend that just prints the __ua_function__ arguments, Backend that uses numpy.fft

### Community 553 - "Community 553"
Cohesion: 0.29
Nodes (6): _deprecate_positional_args(), _deprecated(), Helper function for deprecating modules that are public but were     intended to, Decorator for methods that issues warnings for positional arguments.      Using, Deprecate a function by emitting a warning on use., _sub_module_deprecation()

### Community 554 - "Community 554"
Cohesion: 0.29
Nodes (7): matmul_toeplitz(), _matmul_toepltiz(), Validate arguments and format inputs for toeplitz functions      Parameters, r"""Efficient Toeplitz Matrix-Matrix Multiplication using FFT.      This functio, r"""Solve the equation ``T @ x = b`` for ``x``, where ``T`` is a Toeplitz     ma, solve_toeplitz(), _validate_args_for_toeplitz_ops()

### Community 555 - "Community 555"
Cohesion: 0.29
Nodes (7): matrix_balance(), pinvh(), Compute the (Moore-Penrose) pseudo-inverse of a Hermitian matrix.      Calculate, Compute a diagonal similarity transformation for row/column balancing.      The, LinAlgWarning, The warning emitted when a linear algebra related operation is close     to fail, RuntimeWarning

### Community 556 - "Community 556"
Cohesion: 0.38
Nodes (6): _batch_dot(), clarkson_woodruff_transform(), cwt_matrix(), Sketching-based Matrix Computations, r"""     Generate a matrix S which represents a Clarkson-Woodruff transform., r"""     Applies a Clarkson-Woodruff Transform/sketch to the input matrix.

### Community 557 - "Community 557"
Cohesion: 0.43
Nodes (6): Trust Region Reflective algorithm for least-squares optimization.  The algorithm, Select the best step according to Trust Region Reflective algorithm., select_step(), trf(), trf_bounds(), trf_no_bounds()

### Community 558 - "Community 558"
Cohesion: 0.38
Nodes (6): _bracket_minimum(), _bracket_minimum_iv(), _bracket_root(), _bracket_root_iv(), Bracket the minimum of a unimodal scalar function of one variable      This func, Bracket the root of a monotonic scalar function of one variable      This functi

### Community 559 - "Community 559"
Cohesion: 0.33
Nodes (2): Wrapper class for Jacobian calculation, _VectorHessWrapper

### Community 560 - "Community 560"
Cohesion: 0.33
Nodes (5): gammainc(), gammaincc(), Compute gammainc and gammaincc for large arguments and parameters and save the v, Compute gammainc exactly like mpmath does but allow for more     summands in hyp, Compute gammaincc exactly like mpmath does but allow for more     terms in hyper

### Community 562 - "Community 562"
Cohesion: 0.62
Nodes (6): clansvd_irl(), dlansvd_irl(), int_max(), int_min(), slansvd_irl(), zlansvd_irl()

### Community 563 - "Community 563"
Cohesion: 0.67
Nodes (6): clansvd(), dlansvd(), int_max(), int_min(), slansvd(), zlansvd()

### Community 564 - "Community 564"
Cohesion: 0.52
Nodes (6): ldl_update(), ldp(), lsei(), lsi(), lsq(), __slsqp_body()

### Community 565 - "Community 565"
Cohesion: 0.29
Nodes (7): _cdf_cvm(), _cdf_cvm_inf(), _psi1_mod(), _pval_cvm_2samp_asymptotic(), psi1 is defined in equation 1.10 in Csörgő, S. and Faraway, J. (1996).     This, Calculate the cdf of the Cramér-von Mises statistic (infinite sample size)., Calculate the cdf of the Cramér-von Mises statistic for a finite sample     size

### Community 566 - "Community 566"
Cohesion: 0.29
Nodes (7): _circfuncs_common(), circmean(), circstd(), circvar(), r"""Compute the circular mean of a sample of angle observations.      Given :mat, r"""Compute the circular variance of a sample of angle observations.      Given, r"""     Compute the circular standard deviation of a sample of angle observatio

### Community 567 - "Community 567"
Cohesion: 0.29
Nodes (3): Return a copy of the matrix representation of the transform.          4x4 rigid, Set transform(s) at given index(es) in this object.          Parameters, Concatenate a sequence of `RigidTransform` objects into a         single object.

### Community 568 - "Community 568"
Cohesion: 0.67
Nodes (6): create_group(), cyclic(), dicyclic(), icosahedral(), octahedral(), tetrahedral()

### Community 569 - "Community 569"
Cohesion: 0.57
Nodes (6): build_arg_tuple(), build_kwarg_dict(), Q_PyObject_Vectorcall(), Q_PyObject_VectorcallDict(), Q_PyObject_VectorcallMethod(), Q_PyVectorcall_NARGS()

### Community 570 - "Community 570"
Cohesion: 0.47
Nodes (5): generate_decl_wrapper(), generate_file_wrapper(), make_all(), Create wrapper function declaration.      Wrapper has symbol `F_FUNC(name,NAME)`, Returns text of file containing wrappers for all BLAS/LAPACK functions.

### Community 571 - "Community 571"
Cohesion: 0.33
Nodes (5): fht(), ifht(), Fast Hankel transforms using the FFTLog algorithm.  The implementation closely f, r'''Compute the fast Hankel transform.      Computes the discrete Hankel transfo, r"""Compute the inverse fast Hankel transform.      Computes the discrete invers

### Community 572 - "Community 572"
Cohesion: 0.33
Nodes (6): correspond(), cut_tree(), num_obs_linkage(), Given a linkage matrix Z, return the cut tree.      Parameters     ----------, Return the number of original observations of the linkage matrix passed.      Pa, Check for correspondence between linkage and condensed distance matrices.      T

### Community 573 - "Community 573"
Cohesion: 0.40
Nodes (6): fcluster(), fclusterdata(), inconsistent(), r"""     Calculate inconsistency statistics on a linkage matrix.      Parameters, Form flat clusters from the hierarchical clustering defined by     the given lin, Cluster observation data using a given metric.      Clusters the original observ

### Community 574 - "Community 574"
Cohesion: 0.33
Nodes (1): lsoda

### Community 575 - "Community 575"
Cohesion: 0.33
Nodes (3): Evaluate a spline function.          Parameters         ----------         x : a, Compute a definite integral of the spline.          Parameters         ---------, c and t may be modified by the user. The Cython code expects         that they a

### Community 576 - "Community 576"
Cohesion: 0.33
Nodes (4): Smooth bivariate spline approximation in spherical coordinates.      .. versiona, Wrapper for sphere with iopt=0 (smoothing spline on sphere).     Returns: nt, tt, SmoothSphereBivariateSpline, _spherfit_smth()

### Community 577 - "Community 577"
Cohesion: 0.33
Nodes (4): Bivariate spline approximation over a rectangular mesh on a sphere.      Can be, Wrapper for spgrid (smoothing on spherical grid).     Returns: nu, tu, nv, tv, c, RectSphereBivariateSpline, _regrid_smth_spher()

### Community 578 - "Community 578"
Cohesion: 0.40
Nodes (5): lsqr(), Sparse Equations and Least Squares.  The original Fortran code was written by C., Stable implementation of Givens rotation.      Notes     -----     The routine ', Find the least-squares solution to a large, sparse, linear system     of equatio, _sym_ortho()

### Community 579 - "Community 579"
Cohesion: 0.33
Nodes (6): concat_1d(), Return the device for the result of a function with inputs `args`,      The purp, Like `xp_result_device`, but return ``(device, devices)``.      ``devices[i]`` i, A replacement for `np.r_` as `xp.concat` does not accept python scalars        o, xp_result_device(), _xp_result_devices()

### Community 580 - "Community 580"
Cohesion: 0.40
Nodes (4): _make_sphinx_capabilities(), Decorator for a function that states its support among various     Array API com, xp_capabilities(), _XPSphinxCapability

### Community 581 - "Community 581"
Cohesion: 0.40
Nodes (5): array_namespace(), _ArrayClsInfo, Override functions from array_api_compat, for use by array-api-extra and interna, Get the array API compatible namespace for the arrays xs.      Parameters     --, _validate_array_cls()

### Community 582 - "Community 582"
Cohesion: 0.33
Nodes (6): _format_emit_errors_warnings(), inv(), lstsq(), Compute least-squares solution to the equation ``a @ x = b``.      Compute a vec, Format/emit errors/warnings from a lowlevel batched routine.      See inv, solve, r"""     Compute the inverse of a matrix.      If the data matrix is known to be

### Community 583 - "Community 583"
Cohesion: 0.33
Nodes (6): Solve the equation ``a @ x = b`` for ``x``, where ``a`` is the banded matrix, Solve the equation ``a @ x = b`` for ``x``,  where ``a`` is the     Hermitian po, Solve the equation ``a @ x = b`` for  ``x``,     where `a` is a square matrix., solve(), solve_banded(), solveh_banded()

### Community 584 - "Community 584"
Cohesion: 0.53
Nodes (5): get_sig_name(), get_type(), make_signature(), A script that uses f2py to generate the signature files used to make the Cython, sigs_from_dir()

### Community 586 - "Community 586"
Cohesion: 0.33
Nodes (3): MikotaPair, Construct the Mikota pair of matrices in various formats and     eigenvalues of, Return the requested number of eigenvalues.          Parameters         --------

### Community 587 - "Community 587"
Cohesion: 0.33
Nodes (6): left_multiplied_operator(), left_multiply(), Return diag(d) J as LinearOperator., Compute diag(d) J.      If `copy` is False, `J` is modified in place (unless bei, Scale Jacobian and residuals for a robust loss function.      Arrays are modifie, scale_for_robust_loss_function()

### Community 588 - "Community 588"
Cohesion: 0.33
Nodes (6): convolve(), correlate(), _correlate_or_convolve(), _invalid_origin(), Multidimensional correlation.      The array is correlated with the given kernel, Multidimensional convolution.      The array is convolved with the given kernel.

### Community 589 - "Community 589"
Cohesion: 0.33
Nodes (6): gaussian_filter(), gaussian_filter1d(), _gaussian_kernel1d(), Computes a 1-D Gaussian convolution kernel., 1-D Gaussian filter.      Parameters     ----------     %(input)s     sigma : sc, Multidimensional Gaussian filter.      Parameters     ----------     %(input)s

### Community 590 - "Community 590"
Cohesion: 0.33
Nodes (6): gaussian_laplace(), generic_laplace(), laplace(), N-D Laplace filter based on approximate second derivatives.      Parameters, Multidimensional Laplace filter using Gaussian second derivatives.      Paramete, N-D Laplace filter using a provided second derivative function.      Parameters

### Community 591 - "Community 591"
Cohesion: 0.47
Nodes (5): _chandrupatla(), _chandrupatla_iv(), _chandrupatla_minimize(), Find the root of an elementwise function using Chandrupatla's algorithm.      Fo, Find the minimizer of an elementwise function.      For each element of the outp

### Community 593 - "Community 593"
Cohesion: 0.47
Nodes (5): main(), mp_wright_bessel(), Compute a grid of values for Wright's generalized Bessel function and save the v, Compute Wright's generalized Bessel function as Series with mpmath., rgamma_cached()

### Community 594 - "Community 594"
Cohesion: 0.33
Nodes (6): _design_notch_peak_filter(), iirnotch(), iirpeak(), Design second-order IIR notch digital filter.      A notch filter is a band-stop, Design second-order IIR peak (resonant) digital filter.      A peak filter is a, Design notch or peak digital filter.      Parameters     ----------     w0 : flo

### Community 595 - "Community 595"
Cohesion: 0.33
Nodes (5): load_npz(), Save a sparse matrix or array to a file using ``.npz`` format.      Parameters, # TODO: After a few releases, switch 2D case to save with coords only., Load a sparse array/matrix from a file using ``.npz`` format.      Parameters, save_npz()

### Community 596 - "Community 596"
Cohesion: 0.33
Nodes (6): euclidean(), minkowski(), Compute the Minkowski distance between two arrays.      The Minkowski distance b, Computes the Euclidean distance between two arrays.      The Euclidean distance, Return the standardized Euclidean distance between two 1-D arrays.      The stan, seuclidean()

### Community 597 - "Community 597"
Cohesion: 0.40
Nodes (5): _parse_core_ndims(), Helpers for producing efficient wrappers of ufuncs., Helper to ensure optimal iteration order for ufuncs that use caching.      This, Return tuple of num core dims per input from gufunc signature., _with_cache_optimization()

### Community 598 - "Community 598"
Cohesion: 0.60
Nodes (5): at_plus_a(), get_colamd(), get_metis(), get_perm_c(), getata()

### Community 599 - "Community 599"
Cohesion: 0.60
Nodes (5): genmmd_(), slu_mmdelm_(), slu_mmdint_(), slu_mmdnum_(), slu_mmdupd_()

### Community 600 - "Community 600"
Cohesion: 0.53
Nodes (4): _bessel_j1(), NI_FourierFilter(), p1evl(), polevl()

### Community 601 - "Community 601"
Cohesion: 0.60
Nodes (4): _get_spline_boundary_mode(), map_coordinate(), NI_GeometricTransform(), NI_ZoomShift()

### Community 602 - "Community 602"
Cohesion: 0.33
Nodes (2): CovViaCholesky, r"""         Representation of a covariance provided via the (lower) Cholesky fa

### Community 603 - "Community 603"
Cohesion: 0.33
Nodes (2): CovViaPrecision, r"""         Return a representation of a covariance from its precision matrix.

### Community 605 - "Community 605"
Cohesion: 0.33
Nodes (6): r"""Return a dataset transformed by a Yeo-Johnson power transformation.      Par, Returns `x` transformed by the Yeo-Johnson power transform with given     parame, Compute optimal Yeo-Johnson transform parameter.      Compute optimal Yeo-Johnso, yeojohnson(), yeojohnson_normmax(), _yeojohnson_transform()

### Community 606 - "Community 606"
Cohesion: 0.33
Nodes (6): argstoarray(), f_oneway(), obrientransform(), Constructs a 2D array from a group of sequences.      Sequences are filled with, Computes a transform on input data (any number of columns).  Used to     test fo, Performs a 1-way ANOVA, returning an F-value and probability given     any numbe

### Community 607 - "Community 607"
Cohesion: 0.33
Nodes (3): Compose this transform with the other.          If ``p`` and ``q`` are two trans, Compose a rotation with this transform (rotation applied second).          See `, Initialize from a rotation, without a translation.          When applying this t

### Community 608 - "Community 608"
Cohesion: 0.33
Nodes (3): Return the rotation component of the transform.          A transform is a compos, Initialize from a 4x4 transformation matrix.          Rotations are not meant to, Initialize from a 4x4 transformation matrix.          Parameters         -------

### Community 611 - "Community 611"
Cohesion: 0.50
Nodes (4): download_all(), main(), Platform independent script to download all the `scipy.datasets` module data fil, Utility method to download all the dataset files     for `scipy.datasets` module

### Community 612 - "Community 612"
Cohesion: 0.40
Nodes (4): _r2r(), _r2rn(), Forward or backward 1-D DCT/DST      Parameters     ----------     forward : boo, Forward or backward nd DCT/DST      Parameters     ----------     forward : bool

### Community 613 - "Community 613"
Cohesion: 0.60
Nodes (4): _herm(), _iv(), Partial singular value decomposition of a sparse matrix.      Compute the larges, svds()

### Community 614 - "Community 614"
Cohesion: 0.40
Nodes (1): HighsOptionsManager

### Community 615 - "Community 615"
Cohesion: 0.60
Nodes (4): get_lebedev_recurrence_points(), get_lebedev_sphere(), lebedev_rule(), r"""Lebedev quadrature.      Compute the sample points and weights for Lebedev q

### Community 616 - "Community 616"
Cohesion: 0.50
Nodes (4): _fgmres(), gcrotmk(), FGMRES Arnoldi process, with optional projection or augmentation      Parameters, Solve ``Ax = b`` with the flexible GCROT(m,k) algorithm.      Parameters     ---

### Community 617 - "Community 617"
Cohesion: 0.40
Nodes (5): assert_almost_equal(), assert_array_almost_equal(), Backwards compatible replacement. In new code, use xp_assert_close instead., Backwards compatible replacement. In new code, use xp_assert_close instead., xp_assert_close()

### Community 618 - "Community 618"
Cohesion: 0.40
Nodes (5): _count_nonmasked(), is_marray(), _masked_apply(), Returns True if `xp` is an MArray namespace; False otherwise., _share_masks()

### Community 619 - "Community 619"
Cohesion: 0.40
Nodes (5): make_xp_pytest_marks(), make_xp_pytest_param(), make_xp_test_case(), Variant of ``make_xp_test_case`` that returns a pytest.param for a function,, Variant of ``make_xp_test_case`` that returns a list of pytest marks,     which

### Community 620 - "Community 620"
Cohesion: 0.60
Nodes (4): norm(), Norm of a sparse matrix.      This function is able to return one of seven diffe, _ravel(), _sparse_frobenius_norm()

### Community 621 - "Community 621"
Cohesion: 0.50
Nodes (4): bvls(), compute_kkt_optimality(), Bounded-variable least-squares algorithm., Compute the maximum violation of KKT conditions.

### Community 622 - "Community 622"
Cohesion: 0.50
Nodes (4): lsq_linear(), prepare_bounds(), Linear least squares with bound constraints on independent variables., r"""Solve a linear least-squares problem with bounds on the variables.      Give

### Community 623 - "Community 623"
Cohesion: 0.60
Nodes (4): main(), Precompute series coefficients for log-Gamma., stirling_series(), taylor_series_at_1()

### Community 624 - "Community 624"
Cohesion: 0.80
Nodes (4): main(), mpmath_wrightomega(), wrightomega_exp_error(), wrightomega_series_error()

### Community 625 - "Community 625"
Cohesion: 0.60
Nodes (3): ptr(), rcont1(), rcont2()

### Community 626 - "Community 626"
Cohesion: 0.70
Nodes (4): argsort_iter(), augmenting_path(), solve(), solve_rectangular_linear_sum_assignment()

### Community 627 - "Community 627"
Cohesion: 0.50
Nodes (2): _correlate_nd_imp(), scipy_signal__sigtools_correlateND()

### Community 629 - "Community 629"
Cohesion: 0.40
Nodes (5): dice(), _nbool_correspond_ft_tf(), Compute the Dice dissimilarity between two boolean 1-D arrays.      The Dice dis, Compute the Sokal-Sneath dissimilarity between two boolean 1-D arrays.      The, sokalsneath()

### Community 630 - "Community 630"
Cohesion: 0.40
Nodes (5): _nbool_correspond_all(), Compute the Yule dissimilarity between two boolean 1-D arrays.      The Yule dis, Compute the Rogers-Tanimoto dissimilarity between two boolean 1-D arrays.      T, rogerstanimoto(), yule()

### Community 632 - "Community 632"
Cohesion: 0.40
Nodes (2): multigammaln(), r"""Returns the log of multivariate gamma, also sometimes called the     general

### Community 633 - "Community 633"
Cohesion: 0.60
Nodes (4): add_weights(), build(), build_ckdtree(), build_weights()

### Community 638 - "Community 638"
Cohesion: 0.50
Nodes (3): _continued_fraction(), _continued_fraction_iv(), r"""Evaluate a generalized continued fraction numerically.      `_continued_frac

### Community 639 - "Community 639"
Cohesion: 0.40
Nodes (2): CovViaPSD, Representation of a covariance provided via an instance of _PSD

### Community 640 - "Community 640"
Cohesion: 0.50
Nodes (2): _generate_example(), r""" Draw a specific (fully-defined) distribution from the family.          See

### Community 641 - "Community 641"
Cohesion: 0.50
Nodes (4): _central_diff_weights(), _derivative(), Return weights for an Np-point central derivative.      Assumes equally-spaced f, Find the nth derivative of a function at a point.      Given a function, use a c

### Community 642 - "Community 642"
Cohesion: 0.40
Nodes (3): directional_stats(), DirectionalStats, Computes sample statistics for directional data.      Computes the directional m

### Community 643 - "Community 643"
Cohesion: 0.40
Nodes (4): Kurtosis of the Tukey Lambda distribution.      Parameters     ----------     la, Variance of the Tukey Lambda distribution.      Parameters     ----------     la, tukeylambda_kurtosis(), tukeylambda_variance()

### Community 644 - "Community 644"
Cohesion: 0.40
Nodes (1): _MockFunction

### Community 645 - "Community 645"
Cohesion: 0.40
Nodes (3): equality_constrained_sqp(), Byrd-Omojokun Trust-Region SQP method., Solve nonlinear equality-constrained problem using trust-region SQP.      Solve

### Community 646 - "Community 646"
Cohesion: 0.70
Nodes (4): dump_dataset(), dump_datasets(), parse_ipp_file(), _raw_data()

### Community 647 - "Community 647"
Cohesion: 0.50
Nodes (4): main(), newer(), python makenpz.py DIRECTORY  Build a npz containing all data files in the direct, Return true if 'source' exists and is more recently modified than     'target',

### Community 649 - "Community 649"
Cohesion: 0.50
Nodes (1): .. The heading is listed in the parent file `doc/reference/index.rst` to keep th

### Community 650 - "Community 650"
Cohesion: 0.50
Nodes (1): rbf - Radial basis functions for interpolation/smoothing scattered N-D data.  Wr

### Community 651 - "Community 651"
Cohesion: 0.50
Nodes (3): lsmr(), Copyright (C) 2010 David Fong and Michael Saunders  LSMR uses an iterative metho, Iterative solver for least-squares problems.      lsmr solves the system of line

### Community 652 - "Community 652"
Cohesion: 0.50
Nodes (3): orthogonal_procrustes(), Solve the orthogonal Procrustes problem., Compute the matrix solution of the orthogonal (or unitary) Procrustes problem.

### Community 653 - "Community 653"
Cohesion: 0.50
Nodes (4): find_active_constraints(), make_strictly_feasible(), Determine which constraints are active in a given point.      The threshold is c, Shift a point to the interior of a feasible region.      Each element of the ret

### Community 654 - "Community 654"
Cohesion: 0.50
Nodes (4): in_bounds(), Check if a point lies within bounds., Compute reflective transformation and its gradient., reflective_transformation()

### Community 655 - "Community 655"
Cohesion: 0.50
Nodes (4): Return J diag(d) as LinearOperator., Compute J diag(d).      If `copy` is False, `J` is modified in place (unless bei, right_multiplied_operator(), right_multiply()

### Community 656 - "Community 656"
Cohesion: 0.50
Nodes (4): gaussian_gradient_magnitude(), generic_gradient_magnitude(), Gradient magnitude using a provided gradient function.      Parameters     -----, Multidimensional gradient magnitude using Gaussian derivatives.      Parameters

### Community 657 - "Community 657"
Cohesion: 0.50
Nodes (4): Calculate a 1-D uniform filter along the given axis.      The lines of the array, Multidimensional uniform filter.      Parameters     ----------     %(input)s, uniform_filter(), uniform_filter1d()

### Community 658 - "Community 658"
Cohesion: 0.50
Nodes (2): _maybe_convert_arg(), Convert arrays/scalars hiding in the sequence `arg`.

### Community 660 - "Community 660"
Cohesion: 0.50
Nodes (1): Pythran implementation of columns grouping for finite difference Jacobian estima

### Community 663 - "Community 663"
Cohesion: 0.67
Nodes (3): generate_A(), main(), Precompute the polynomials for the asymptotic expansion of the generalized expon

### Community 664 - "Community 664"
Cohesion: 0.67
Nodes (3): lambertw_pade(), main(), Compute a Pade approximation for the principal branch of the Lambert W function

### Community 665 - "Community 665"
Cohesion: 0.67
Nodes (3): main(), Compute the Taylor series for zeta(x) - 1 around x = 0., zetac_series()

### Community 666 - "Community 666"
Cohesion: 0.83
Nodes (3): circular_wrap_index(), pylab_convolve_2d(), reflect_symm_index()

### Community 667 - "Community 667"
Cohesion: 0.50
Nodes (1): isspmatrix_dok()

### Community 668 - "Community 668"
Cohesion: 0.50
Nodes (1): r""" =================================== Sparse arrays (:mod:`scipy.sparse`) ===

### Community 669 - "Community 669"
Cohesion: 0.50
Nodes (4): correlation(), cosine(), Compute the correlation distance between two 1-D arrays.      The correlation di, Compute the Cosine distance between 1-D arrays.      The Cosine distance between

### Community 670 - "Community 670"
Cohesion: 0.50
Nodes (4): is_valid_y(), num_obs_y(), Return True if the input array is a valid condensed distance matrix.      Conden, Return the number of original observations that correspond to a     condensed di

### Community 671 - "Community 671"
Cohesion: 0.50
Nodes (3): procrustes(), This module provides functions to perform full Procrustes analysis.  This code w, r"""Procrustes analysis, a similarity test for two data sets.      Each input ma

### Community 672 - "Community 672"
Cohesion: 0.50
Nodes (4): polygamma(), r"""Polygamma functions.      Defined as :math:`\psi^{(n)}(x)` where :math:`\psi, r"""     Riemann or Hurwitz zeta function.      Parameters     ----------     x, zeta()

### Community 673 - "Community 673"
Cohesion: 0.50
Nodes (3): lambertw(), # TODO: special expert should inspect this, r"""     lambertw(z, k=0, tol=1e-8)      Lambert W function.      The Lambert W

### Community 674 - "Community 674"
Cohesion: 0.50
Nodes (4): hermitenorm(), r"""Gauss-Hermite (statistician's) quadrature.      Compute the sample points an, r"""Probabilist's Hermite polynomial.      Defined by      .. math::          He, roots_hermitenorm()

### Community 678 - "Community 678"
Cohesion: 0.67
Nodes (2): traverse_checking(), traverse_no_checking()

### Community 679 - "Community 679"
Cohesion: 0.67
Nodes (2): traverse_checking(), traverse_no_checking()

### Community 680 - "Community 680"
Cohesion: 0.67
Nodes (2): traverse_checking(), traverse_no_checking()

### Community 683 - "Community 683"
Cohesion: 0.50
Nodes (4): bayes_mvs(), mvsdist(), 'Frozen' distributions for mean, variance, and standard deviation of data., r"""     Bayesian confidence intervals for the mean, var, and std.      Paramete

### Community 684 - "Community 684"
Cohesion: 0.50
Nodes (4): kstat(), kstatvar(), r"""     Return the `n` th k-statistic ( ``1<=n<=4`` so far).      The `n` th k-, r"""Return an unbiased estimator of the variance of the k-statistic.      See `k

### Community 685 - "Community 685"
Cohesion: 0.50
Nodes (4): _mask_to_limits(), Mask an array for values outside of given limits.      This is primarily a utili, Compute the trimmed variance      This function computes the sample variance of, tvar()

### Community 686 - "Community 686"
Cohesion: 0.50
Nodes (4): mquantiles(), Computes empirical quantiles for a data array.      Samples quantile are defined, Calculate the score at the given 'per' percentile of the     sequence a.  For ex, scoreatpercentile()

### Community 687 - "Community 687"
Cohesion: 0.50
Nodes (2): Initialize from a translation numpy array, without a rotation.          When app, Initialize a rigid transform from translation and rotation         components.

### Community 689 - "Community 689"
Cohesion: 0.67
Nodes (2): Routine for validation and conversion of csgraph inputs, validate_graph()

### Community 690 - "Community 690"
Cohesion: 0.67
Nodes (2): _clear_cache(), Cleans the SciPy datasets cache directory.      Parameters     ----------     da

### Community 697 - "Community 697"
Cohesion: 0.67
Nodes (1): Here we perform some symbolic computations required for the N-D interpolation ro

### Community 699 - "Community 699"
Cohesion: 0.67
Nodes (2): pade(), Return Pade approximation to a polynomial as the ratio of two polynomials.

### Community 700 - "Community 700"
Cohesion: 0.67
Nodes (2): _monomial_powers_impl(), Return the powers for each monomial in a polynomial.      Parameters     -------

### Community 701 - "Community 701"
Cohesion: 0.67
Nodes (2): F, Callable wrapper for computing `fp(p)` for a fixed spline configuration.      Pa

### Community 702 - "Community 702"
Cohesion: 0.67
Nodes (2): lgmres(), Solve ``Ax = b`` with the LGMRES algorithm.      The LGMRES algorithm [1]_ [2]_

### Community 703 - "Community 703"
Cohesion: 0.67
Nodes (2): minres(), Solve ``Ax = b`` with the MINimum RESidual method,     for a real symmetric or c

### Community 704 - "Community 704"
Cohesion: 0.67
Nodes (2): Solve ``Ax = b`` with the Transpose-Free Quasi-Minimal Residual method.      Par, tfqmr()

### Community 706 - "Community 706"
Cohesion: 0.67
Nodes (2): cossin(), Compute the cosine-sine (CS) decomposition of an orthogonal/unitary matrix.

### Community 707 - "Community 707"
Cohesion: 0.67
Nodes (2): polar(), Compute the polar decomposition.      Returns the factors of the polar decomposi

### Community 712 - "Community 712"
Cohesion: 0.67
Nodes (2): _minimize_cobyqa(), Minimize a scalar function of one or more variables using the     Constrained Op

### Community 717 - "Community 717"
Cohesion: 0.67
Nodes (2): nnls(), Solve ``argmin_x || Ax - b ||_2^2`` for ``x>=0``.      This problem, often calle

### Community 719 - "Community 719"
Cohesion: 0.67
Nodes (2): _minimize_trust_krylov(), Minimization of a scalar function of one or more variables using     a nearly ex

### Community 720 - "Community 720"
Cohesion: 0.67
Nodes (1): FunctionWithRoot

### Community 722 - "Community 722"
Cohesion: 0.67
Nodes (2): lagrange_inversion(), Given a series      f(x) = a[1]*x + a[2]*x**2 + ... + a[n-1]*x**(n - 1),      us

### Community 724 - "Community 724"
Cohesion: 0.67
Nodes (2): max_len_seq(), Maximum length sequence (MLS) generator.      Parameters     ----------     nbit

### Community 725 - "Community 725"
Cohesion: 0.67
Nodes (2): Sampling frequency of input signal and of the window.          The sampling freq, Sampling frequency of input signal and of the window.          The sampling freq

### Community 726 - "Community 726"
Cohesion: 0.67
Nodes (2): Mode of utilized FFT ('twosided', 'centered', 'onesided' or         'onesided2X', Set mode of FFT.          Allowed values are 'twosided', 'centered', 'onesided',

### Community 727 - "Community 727"
Cohesion: 0.67
Nodes (2): Length of input for the FFT used - may be larger than window         length `m_n, Setter for the length of FFT utilized.          See the property `mfft` for furt

### Community 733 - "Community 733"
Cohesion: 0.67
Nodes (2): _geometric_slerp(), Geometric spherical linear interpolation.      The interpolation occurs along a

### Community 737 - "Community 737"
Cohesion: 1.00
Nodes (2): cgstrs(), cprint_soln()

### Community 742 - "Community 742"
Cohesion: 1.00
Nodes (2): dgstrs(), dprint_soln()

### Community 757 - "Community 757"
Cohesion: 1.00
Nodes (2): sgstrs(), sprint_soln()

### Community 763 - "Community 763"
Cohesion: 1.00
Nodes (2): zgstrs(), zprint_soln()

### Community 768 - "Community 768"
Cohesion: 0.67
Nodes (2): crosstab(), Return table of counts for each possible unique combination in ``*args``.      W

### Community 769 - "Community 769"
Cohesion: 0.67
Nodes (3): r"""     Computes the Theil-Sen estimator for a set of points (x, y).      `thei, r"""     Computes the Theil-Sen estimator for a set of points (x, y).      `thei, _theilslopes()

### Community 772 - "Community 772"
Cohesion: 0.67
Nodes (2): Compute the coefficient of variation.      The coefficient of variation is the s, variation()

### Community 773 - "Community 773"
Cohesion: 1.00
Nodes (2): gen(), main()

### Community 776 - "Community 776"
Cohesion: 1.00
Nodes (2): trlib_leftmost(), trlib_leftmost_irreducible()

### Community 777 - "Community 777"
Cohesion: 1.00
Nodes (2): parse_txt_data(), run_test()

### Community 778 - "Community 778"
Cohesion: 0.67
Nodes (2): generate_test_vecs(), test label with different structuring element neighborhoods

### Community 779 - "Community 779"
Cohesion: 1.00
Nodes (1): Eigenvalue solver using iterative methods.  Find k eigenvectors and eigenvalues

### Community 780 - "Community 780"
Cohesion: 1.00
Nodes (1): Cython optimize root finding API ================================ The underlying

### Community 784 - "Community 784"
Cohesion: 1.00
Nodes (1): Distributor init file  Distributors: you can replace the contents of this file w

### Community 785 - "Community 785"
Cohesion: 1.00
Nodes (1): Module containing external code ===============================  The code in thi

### Community 786 - "Community 786"
Cohesion: 1.00
Nodes (1): Return definite integral of the spline between two given points.          Parame

### Community 787 - "Community 787"
Cohesion: 1.00
Nodes (1): Return all derivatives of the spline at the point x.          Parameters

### Community 788 - "Community 788"
Cohesion: 1.00
Nodes (1): Return the zeros of the spline.          Notes         -----         Restriction

### Community 789 - "Community 789"
Cohesion: 1.00
Nodes (1): Construct a new spline representing the derivative of this spline.          Para

### Community 790 - "Community 790"
Cohesion: 1.00
Nodes (2): default_xp(), In all ``xp_assert_*`` and ``assert_*`` function calls executed within this

### Community 791 - "Community 791"
Cohesion: 1.00
Nodes (2): eager_warns(), pytest.warns context manager if arrays of specified namespace are always eager.

### Community 792 - "Community 792"
Cohesion: 1.00
Nodes (2): get_native_namespace_name(), Return name for native namespace (without array_api_compat prefix).

### Community 793 - "Community 793"
Cohesion: 1.00
Nodes (2): Copies a possibly on device array to a NumPy array.      This function is intend, _xp_copy_to_numpy()

### Community 794 - "Community 794"
Cohesion: 1.00
Nodes (2): Return the `scipy`-like namespace of a non-NumPy backend      That is, return th, scipy_namespace_for()

### Community 795 - "Community 795"
Cohesion: 1.00
Nodes (1): PUBLIC_MODULES was once included in scipy._lib.tests.test_public_api.  It has be

### Community 796 - "Community 796"
Cohesion: 1.00
Nodes (1): `uarray` provides functions for generating multimethods that dispatch to multipl

### Community 800 - "Community 800"
Cohesion: 1.00
Nodes (2): check_termination(), Check termination condition for nonlinear least squares.

### Community 801 - "Community 801"
Cohesion: 1.00
Nodes (2): CL_scaling_vector(), Compute Coleman-Li scaling vector and its derivatives.      Components of a vect

### Community 802 - "Community 802"
Cohesion: 1.00
Nodes (2): compute_grad(), Compute gradient of the least-squares cost function.

### Community 803 - "Community 803"
Cohesion: 1.00
Nodes (2): compute_jac_scale(), Compute variables scale based on the Jacobian matrix.

### Community 804 - "Community 804"
Cohesion: 1.00
Nodes (2): evaluate_quadratic(), Compute values of a quadratic function arising in least squares.      The functi

### Community 805 - "Community 805"
Cohesion: 1.00
Nodes (2): intersect_trust_region(), Find the intersection of a line with the boundary of a trust region.      This f

### Community 806 - "Community 806"
Cohesion: 1.00
Nodes (2): minimize_quadratic_1d(), Minimize a 1-D quadratic function subject to bounds.      The free term `c` is 0

### Community 807 - "Community 807"
Cohesion: 1.00
Nodes (2): Solve a general trust-region problem in 2 dimensions.      The problem is reform, solve_trust_region_2d()

### Community 808 - "Community 808"
Cohesion: 1.00
Nodes (2): Update the radius of a trust region based on the cost reduction.      Returns, update_tr_radius()

### Community 809 - "Community 809"
Cohesion: 1.00
Nodes (2): Compute a min_step size required to reach a bound.      The function computes a, step_size_to_bound()

### Community 810 - "Community 810"
Cohesion: 1.00
Nodes (2): Solve a trust-region problem arising in least-squares minimization.      This fu, solve_lsq_trust_region()

### Community 811 - "Community 811"
Cohesion: 1.00
Nodes (1): This module contains least-squares algorithms.

### Community 812 - "Community 812"
Cohesion: 1.00
Nodes (1): This is the 'bare' ndimage API.  This --- private! --- module only collects impl

### Community 813 - "Community 813"
Cohesion: 1.00
Nodes (1): Docstring components common to several ndimage functions.

### Community 814 - "Community 814"
Cohesion: 1.00
Nodes (2): _add_a_b(), r"""Add "a" and "b" keys to each test from the "bracket" value

### Community 815 - "Community 815"
Cohesion: 1.00
Nodes (2): aps01_f(), r"""Straightforward sum of trigonometric function and polynomial

### Community 816 - "Community 816"
Cohesion: 1.00
Nodes (2): aps02_f(), r"""poles at x=n**2, 1st and 2nd derivatives at root are also close to 0

### Community 817 - "Community 817"
Cohesion: 1.00
Nodes (2): aps03_f(), r"""Rapidly changing at the root

### Community 818 - "Community 818"
Cohesion: 1.00
Nodes (2): aps04_f(), r"""Medium-degree polynomial

### Community 819 - "Community 819"
Cohesion: 1.00
Nodes (2): aps05_f(), r"""Simple Trigonometric function

### Community 820 - "Community 820"
Cohesion: 1.00
Nodes (2): aps06_f(), r"""Exponential rapidly changing from -1 to 1 at x=0

### Community 821 - "Community 821"
Cohesion: 1.00
Nodes (2): aps07_f(), r"""Upside down parabola with parametrizable height

### Community 822 - "Community 822"
Cohesion: 1.00
Nodes (2): aps08_f(), r"""Degree n polynomial

### Community 823 - "Community 823"
Cohesion: 1.00
Nodes (2): aps09_f(), r"""Upside down quartic with parametrizable height

### Community 824 - "Community 824"
Cohesion: 1.00
Nodes (2): aps10_f(), r"""Exponential plus a polynomial

### Community 825 - "Community 825"
Cohesion: 1.00
Nodes (2): aps11_f(), r"""Rational function with a zero at x=1/n and a pole at x=0

### Community 826 - "Community 826"
Cohesion: 1.00
Nodes (2): aps12_f(), r"""nth root of x, with a zero at x=n

### Community 827 - "Community 827"
Cohesion: 1.00
Nodes (2): aps13_f(), r"""Function with *all* derivatives 0 at the root

### Community 828 - "Community 828"
Cohesion: 1.00
Nodes (2): aps14_f(), r"""0 for negative x-values, trigonometric+linear for x positive

### Community 829 - "Community 829"
Cohesion: 1.00
Nodes (2): aps15_f(), r"""piecewise linear, constant outside of [0, 0.002/(1+n)]

### Community 830 - "Community 830"
Cohesion: 1.00
Nodes (2): cplx01_f(), r"""z**n-a:  Use to find the nth root of a

### Community 831 - "Community 831"
Cohesion: 1.00
Nodes (2): cplx02_f(), r"""e**z - a: Use to find the log of a

### Community 832 - "Community 832"
Cohesion: 1.00
Nodes (2): f1(), r"""f1 is a quadratic with roots at 0 and 1

### Community 833 - "Community 833"
Cohesion: 1.00
Nodes (2): f2(), r"""f2 is a symmetric parabola, x**2 - 1

### Community 834 - "Community 834"
Cohesion: 1.00
Nodes (2): f3(), r"""A quartic with roots at 0, 1, 2 and 3

### Community 835 - "Community 835"
Cohesion: 1.00
Nodes (2): f4(), r"""Piecewise linear, left- and right- discontinuous at x=1, the root.

### Community 836 - "Community 836"
Cohesion: 1.00
Nodes (2): f5(), r"""     Hyperbola with a pole at x=1, but pole replaced with 0. Not continuous

### Community 837 - "Community 837"
Cohesion: 1.00
Nodes (2): get_tests(), r"""Return the requested collection of test cases, as an array of dicts with sub

### Community 838 - "Community 838"
Cohesion: 1.00
Nodes (2): _skip_if_poly1d(), sweep_poly_signature()

### Community 839 - "Community 839"
Cohesion: 1.00
Nodes (1): ======================================= Signal processing (:mod:`scipy.signal`)

### Community 841 - "Community 841"
Cohesion: 1.00
Nodes (1): Instantiate `ShortTimeFFT` by using `get_window`.          The method `get_windo

### Community 842 - "Community 842"
Cohesion: 1.00
Nodes (1): r"""Create instance where the window and its dual are equal up to a         scal

### Community 843 - "Community 843"
Cohesion: 1.00
Nodes (1): Window function as real- or complex-valued 1d array.          This attribute is

### Community 844 - "Community 844"
Cohesion: 1.00
Nodes (1): Time increment in signal samples for sliding window.          This attribute is

### Community 845 - "Community 845"
Cohesion: 1.00
Nodes (1): Normalization applied to the window function         ('magnitude', 'psd', 'unita

### Community 846 - "Community 846"
Cohesion: 1.00
Nodes (1): This is the 'bare' scipy.signal API.  This --- private! --- module only collects

### Community 848 - "Community 848"
Cohesion: 1.00
Nodes (2): erf_zeros(), Compute the first nt zero in the first quadrant, ordered by absolute value.

### Community 849 - "Community 849"
Cohesion: 1.00
Nodes (2): euler(), Euler numbers E(0), E(1), ..., E(n).      The Euler numbers [1]_ are also known

### Community 850 - "Community 850"
Cohesion: 1.00
Nodes (2): fresnel_zeros(), Compute nt complex zeros of sine and cosine Fresnel integrals S(z) and C(z).

### Community 851 - "Community 851"
Cohesion: 1.00
Nodes (2): fresnelc_zeros(), Compute nt complex zeros of cosine Fresnel integral C(z).      Parameters     --

### Community 852 - "Community 852"
Cohesion: 1.00
Nodes (2): fresnels_zeros(), Compute nt complex zeros of sine Fresnel integral S(z).      Parameters     ----

### Community 853 - "Community 853"
Cohesion: 1.00
Nodes (2): jnjnp_zeros(), Compute zeros of integer-order Bessel functions Jn and Jn'.      Results are arr

### Community 854 - "Community 854"
Cohesion: 1.00
Nodes (2): kei_zeros(), Compute nt zeros of the Kelvin function kei.      Parameters     ----------

### Community 855 - "Community 855"
Cohesion: 1.00
Nodes (2): keip_zeros(), Compute nt zeros of the derivative of the Kelvin function kei.      Parameters

### Community 856 - "Community 856"
Cohesion: 1.00
Nodes (2): kelvin_zeros(), Compute `nt` zeros of all Kelvin functions.      Parameters     ----------     n

### Community 857 - "Community 857"
Cohesion: 1.00
Nodes (2): ker_zeros(), Compute nt zeros of the Kelvin function ker.      Parameters     ----------

### Community 858 - "Community 858"
Cohesion: 1.00
Nodes (2): kerp_zeros(), Compute nt zeros of the derivative of the Kelvin function ker.      Parameters

### Community 859 - "Community 859"
Cohesion: 1.00
Nodes (2): lmbda(), r"""Jahnke-Emden Lambda function, Lambdav(x).      This function is defined as [

### Community 860 - "Community 860"
Cohesion: 1.00
Nodes (2): lqmn(), Sequence of associated Legendre functions of the second kind.      Computes the

### Community 861 - "Community 861"
Cohesion: 1.00
Nodes (2): lqn(), Legendre functions of the second kind.      Compute sequence of Legendre functio

### Community 862 - "Community 862"
Cohesion: 1.00
Nodes (2): mathieu_even_coef(), r"""Fourier coefficients for even Mathieu and modified Mathieu functions.      T

### Community 863 - "Community 863"
Cohesion: 1.00
Nodes (2): mathieu_odd_coef(), r"""Fourier coefficients for odd Mathieu and modified Mathieu functions.      Th

### Community 864 - "Community 864"
Cohesion: 1.00
Nodes (2): obl_cv_seq(), Characteristic values for oblate spheroidal wave functions.      Compute a seque

### Community 865 - "Community 865"
Cohesion: 1.00
Nodes (2): pbdn_seq(), Parabolic cylinder functions Dn(z) and derivatives.      Parameters     --------

### Community 866 - "Community 866"
Cohesion: 1.00
Nodes (2): pbdv_seq(), Parabolic cylinder functions Dv(x) and derivatives.      Parameters     --------

### Community 867 - "Community 867"
Cohesion: 1.00
Nodes (2): pbvv_seq(), Parabolic cylinder functions Vv(x) and derivatives.      Parameters     --------

### Community 868 - "Community 868"
Cohesion: 1.00
Nodes (2): perm(), Permutations of N things taken k at a time, i.e., k-permutations of N.      It's

### Community 869 - "Community 869"
Cohesion: 1.00
Nodes (2): pro_cv_seq(), Characteristic values for prolate spheroidal wave functions.      Compute a sequ

### Community 870 - "Community 870"
Cohesion: 1.00
Nodes (2): r"""Compute Riccati-Bessel function of the first kind and its derivative.      T, riccati_jn()

### Community 871 - "Community 871"
Cohesion: 1.00
Nodes (2): Compute Riccati-Bessel function of the second kind and its derivative.      The, riccati_yn()

### Community 872 - "Community 872"
Cohesion: 1.00
Nodes (2): r"""Generate Stirling number(s) of the second kind.      Stirling numbers of the, stirling2()

### Community 873 - "Community 873"
Cohesion: 1.00
Nodes (2): r"""     Compute the softplus function element-wise.      The softplus function, softplus()

### Community 874 - "Community 874"
Cohesion: 1.00
Nodes (2): Compute nt zeros of Bessel function Y0(z), and derivative at each zero.      The, y0_zeros()

### Community 875 - "Community 875"
Cohesion: 1.00
Nodes (2): Compute nt zeros of Bessel function Y1(z), and derivative at each zero.      The, y1_zeros()

### Community 979 - "Community 979"
Cohesion: 1.00
Nodes (1): The local version segment of the version.          >>> print(Version("1.2.3").lo

### Community 980 - "Community 980"
Cohesion: 1.00
Nodes (1): The public portion of the version.          >>> Version("1.2.3").public

### Community 981 - "Community 981"
Cohesion: 1.00
Nodes (1): The "base version" of the version.          >>> Version("1.2.3").base_version

### Community 982 - "Community 982"
Cohesion: 1.00
Nodes (1): Whether this version is a pre-release.          >>> Version("1.2.3").is_prerelea

### Community 983 - "Community 983"
Cohesion: 1.00
Nodes (1): Whether this version is a post-release.          >>> Version("1.2.3").is_postrel

### Community 984 - "Community 984"
Cohesion: 1.00
Nodes (1): Whether this version is a development release.          >>> Version("1.2.3").is_

### Community 985 - "Community 985"
Cohesion: 1.00
Nodes (1): The first item of :attr:`release` or ``0`` if unavailable.          >>> Version(

### Community 986 - "Community 986"
Cohesion: 1.00
Nodes (1): The second item of :attr:`release` or ``0`` if unavailable.          >>> Version

### Community 1012 - "Community 1012"
Cohesion: 1.00
Nodes (1): Statistics-related constants.

### Community 1013 - "Community 1013"
Cohesion: 1.00
Nodes (1): Sane parameters for stats.distributions.

### Community 1014 - "Community 1014"
Cohesion: 1.00
Nodes (2): _get_binomial_log_p_value_with_nuisance_param(), r"""     Compute the log pvalue in respect of a nuisance parameter considering

### Community 1015 - "Community 1015"
Cohesion: 1.00
Nodes (2): _get_wilcoxon_distr2(), Distribution of probability of the Wilcoxon ranksum statistic r_plus (sum     of

### Community 1016 - "Community 1016"
Cohesion: 1.00
Nodes (2): _get_wilcoxon_distr(), Distribution of probability of the Wilcoxon ranksum statistic r_plus (sum     of

### Community 1017 - "Community 1017"
Cohesion: 1.00
Nodes (2): Calculate Kendall's tau-b and p-value from contingency table., _tau_b()

### Community 1018 - "Community 1018"
Cohesion: 1.00
Nodes (1): =================================================================== Statistical

### Community 1019 - "Community 1019"
Cohesion: 1.00
Nodes (1): r"""Differential entropy          In terms of probability density function :math

### Community 1020 - "Community 1020"
Cohesion: 1.00
Nodes (1): r"""Inverse complementary cumulative distribution function.          The inverse

### Community 1021 - "Community 1021"
Cohesion: 1.00
Nodes (1): r"""Inverse of the cumulative distribution function.          For monotonic cont

### Community 1022 - "Community 1022"
Cohesion: 1.00
Nodes (1): r"""Inverse of the log of the complementary cumulative distribution function.

### Community 1023 - "Community 1023"
Cohesion: 1.00
Nodes (1): r"""Inverse of the logarithm of the cumulative distribution function.          T

### Community 1024 - "Community 1024"
Cohesion: 1.00
Nodes (1): r"""Kurtosis (standardized fourth moment)          By default, this is the stand

### Community 1025 - "Community 1025"
Cohesion: 1.00
Nodes (1): r"""L-moment or L-moment ratio of positive integer order.          The L-moment

### Community 1026 - "Community 1026"
Cohesion: 1.00
Nodes (1): r"""Log of the complementary cumulative distribution function          The compl

### Community 1027 - "Community 1027"
Cohesion: 1.00
Nodes (1): r"""Log of the cumulative distribution function          The cumulative distribu

### Community 1028 - "Community 1028"
Cohesion: 1.00
Nodes (1): r"""Logarithm of the differential entropy          In terms of probability densi

### Community 1029 - "Community 1029"
Cohesion: 1.00
Nodes (1): r"""Log of the probability density function          The probability density fun

### Community 1030 - "Community 1030"
Cohesion: 1.00
Nodes (1): r"""Log of the probability mass function          The probability mass function

### Community 1031 - "Community 1031"
Cohesion: 1.00
Nodes (1): r"""Mean (raw first moment about the origin)          Parameters         -------

### Community 1032 - "Community 1032"
Cohesion: 1.00
Nodes (1): r"""Median (50th percentile)          If a continuous random variable :math:`X`

### Community 1033 - "Community 1033"
Cohesion: 1.00
Nodes (1): r"""Mode (most likely value)          Informally, the mode is a value that a ran

### Community 1034 - "Community 1034"
Cohesion: 1.00
Nodes (1): r"""Raw, central, or standard moment of positive integer order.          In term

### Community 1035 - "Community 1035"
Cohesion: 1.00
Nodes (1): r"""Probability density function          The probability density function ("PDF

### Community 1036 - "Community 1036"
Cohesion: 1.00
Nodes (1): r"""Probability mass function          The probability mass function ("PMF"), de

### Community 1037 - "Community 1037"
Cohesion: 1.00
Nodes (1): r"""Random sample from the distribution.          Parameters         ----------

### Community 1038 - "Community 1038"
Cohesion: 1.00
Nodes (1): r"""Skewness (standardized third moment)          Parameters         ----------

### Community 1039 - "Community 1039"
Cohesion: 1.00
Nodes (1): r"""Standard deviation (square root of the second central moment)          Param

### Community 1040 - "Community 1040"
Cohesion: 1.00
Nodes (1): r"""Support of the random variable          The support of a random variable is

### Community 1044 - "Community 1044"
Cohesion: 1.00
Nodes (1): This module contains the equality constrained SQP solver.

### Community 1045 - "Community 1045"
Cohesion: 1.00
Nodes (1): .. note:     If you are looking for overrides for NumPy-specific methods, see th

### Community 1046 - "Community 1046"
Cohesion: 1.00
Nodes (1): Window functions (:mod:`scipy.signal.windows`) =================================

## Knowledge Gaps
- **2274 isolated node(s):** `Create wrapper function declaration.      Wrapper has symbol `F_FUNC(name,NAME)``, `Returns text of file containing wrappers for all BLAS/LAPACK functions.`, `Helper functions and variables for generation of BLAS/LAPACK wrappers.`, `Read BLAS/LAPACK signatures and split into name, return type, argument     names`, `Complex-valued and some Accelerate functions have special symbols.` (+2269 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 12`** (2 nodes): `Delegators for alternative backends in scipy.signal.  The signature of `func_sig`, `# TODO: fix me - `prominence` is not necessarily an array.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (1 nodes): `r""" Parameters used in test and benchmark methods.  Collections of test cases s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `Delegators for alternative backends in scipy.ndimage.  The signature of `func_si`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (2 nodes): `_cs_matrix`, `_process_slice()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 83`** (1 nodes): `_dok_base`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 170`** (2 nodes): `Normal`, `r"""Normal distribution with prescribed mean and standard deviation.      The pr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 171`** (2 nodes): `r"""Standard normal distribution.      The probability density function of the s`, `StandardNormal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 184`** (2 nodes): `rv_frozen`, `# NOTE: To look at history using `git blame`, use `git blame -M -C -C``
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 199`** (1 nodes): `DiscreteDistribution`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 213`** (2 nodes): `r"""An upper truncated Pareto continuous random variable.      %(before_notes)s`, `truncpareto_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 214`** (2 nodes): `MonotonicTransformedDistribution`, `r"""Distribution underlying a strictly monotonic function of a random variable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 216`** (2 nodes): `Logistic`, `r"""Standard logistic distribution.      The probability density function of the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 217`** (2 nodes): `r"""Uniform distribution.      The probability density function of the uniform d`, `Uniform`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 255`** (2 nodes): `genextreme_gen`, `r"""A generalized extreme value continuous random variable.      %(before_notes)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 277`** (2 nodes): `nakagami_gen`, `r"""A Nakagami continuous random variable.      %(before_notes)s      Notes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 299`** (2 nodes): `gengamma_gen`, `r"""A generalized gamma continuous random variable.      %(before_notes)s      S`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 300`** (2 nodes): `genpareto_gen`, `r"""A generalized Pareto continuous random variable.      %(before_notes)s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 301`** (2 nodes): `logistic_gen`, `r"""A logistic (or Sech-squared) continuous random variable.      %(before_notes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 302`** (2 nodes): `r"""A doubly truncated Weibull minimum continuous random variable.      %(before`, `truncweibull_min_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 321`** (2 nodes): `dpareto_lognorm_gen`, `r"""A double Pareto lognormal continuous random variable.      %(before_notes)s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 323`** (2 nodes): `loggamma_gen`, `r"""A log gamma continuous random variable.      %(before_notes)s      Notes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 325`** (2 nodes): `bernoulli_gen`, `r"""A Bernoulli discrete random variable.      %(before_notes)s      Notes     -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 326`** (2 nodes): `hypergeom_gen`, `r"""A hypergeometric discrete random variable.      The hypergeometric distribut`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 350`** (2 nodes): `beta_gen`, `r"""A beta continuous random variable.      %(before_notes)s      Notes     ----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 351`** (2 nodes): `chi_gen`, `r"""A chi continuous random variable.      %(before_notes)s      Notes     -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 352`** (2 nodes): `expon_gen`, `r"""An exponential continuous random variable.      %(before_notes)s      Notes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 353`** (2 nodes): `gennorm_gen`, `r"""A (symmetric) generalized normal continuous random variable.      %(before_n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 354`** (2 nodes): `gumbel_l_gen`, `r"""A left-skewed Gumbel continuous random variable.      %(before_notes)s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 355`** (2 nodes): `gumbel_r_gen`, `r"""A right-skewed Gumbel continuous random variable.      %(before_notes)s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 356`** (2 nodes): `halfgennorm_gen`, `r"""The upper half of a generalized normal continuous random variable.      %(be`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 357`** (2 nodes): `invgamma_gen`, `r"""An inverted gamma continuous random variable.      %(before_notes)s      Not`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 358`** (2 nodes): `irwinhall_gen`, `r"""An Irwin-Hall (Uniform Sum) continuous random variable.      An `Irwin-Hall`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 359`** (2 nodes): `kappa4_gen`, `r"""Kappa 4 parameter distribution.      %(before_notes)s      Notes     -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 360`** (2 nodes): `landau_gen`, `r"""A Landau continuous random variable.      %(before_notes)s      See Also`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 361`** (2 nodes): `maxwell_gen`, `r"""A Maxwell continuous random variable.      %(before_notes)s      Notes     -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 362`** (2 nodes): `pearson3_gen`, `r"""     A pearson type III continuous random variable.      %(before_notes)s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 363`** (2 nodes): `powerlaw_gen`, `r"""A power-function continuous random variable.      %(before_notes)s      See`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 364`** (2 nodes): `r"""Weibull minimum continuous random variable.      The Weibull Minimum Extreme`, `weibull_min_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 365`** (2 nodes): `binom_gen`, `r"""     A binomial discrete random variable.      %(before_notes)s      See Als`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 366`** (2 nodes): `geom_gen`, `r"""A geometric discrete random variable.      %(before_notes)s      See Also`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 367`** (2 nodes): `nbinom_gen`, `r"""     A negative binomial discrete random variable.      %(before_notes)s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 369`** (2 nodes): `poisson_gen`, `r"""A Poisson discrete random variable.      %(before_notes)s      Notes     ---`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 391`** (2 nodes): `burr12_gen`, `r"""A Burr (Type XII) continuous random variable.      %(before_notes)s      See`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 392`** (2 nodes): `cauchy_gen`, `r"""A Cauchy continuous random variable.      %(before_notes)s      Notes     --`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 393`** (2 nodes): `chi2_gen`, `r"""A chi-squared continuous random variable.      For the noncentral chi-square`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 394`** (2 nodes): `dweibull_gen`, `r"""A double Weibull continuous random variable.      %(before_notes)s      Note`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 396`** (2 nodes): `geninvgauss_gen`, `r"""A Generalized Inverse Gaussian continuous random variable.      %(before_not`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 397`** (2 nodes): `genlogistic_gen`, `r"""A generalized logistic continuous random variable.      %(before_notes)s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 398`** (2 nodes): `laplace_gen`, `r"""A Laplace continuous random variable.      %(before_notes)s      Notes     -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 399`** (2 nodes): `lomax_gen`, `r"""A Lomax (Pareto of the second kind) continuous random variable.      %(befor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 400`** (2 nodes): `ncx2_gen`, `r"""A non-central chi-squared continuous random variable.      %(before_notes)s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 402`** (2 nodes): `r"""A truncated exponential continuous random variable.      %(before_notes)s`, `truncexpon_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 403`** (2 nodes): `r"""A Von Mises continuous random variable.      %(before_notes)s      See Also`, `vonmises_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 404`** (2 nodes): `r"""A Student's t continuous random variable.      For the noncentral t distribu`, `t_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 405`** (2 nodes): `r"""A Rayleigh continuous random variable.      %(before_notes)s      Notes`, `rayleigh_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 406`** (2 nodes): `planck_gen`, `r"""A Planck discrete exponential random variable.      %(before_notes)s      Se`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 422`** (2 nodes): `_apply_filter()`, `_apply_filter_gain()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 424`** (2 nodes): `cosine_gen`, `r"""A cosine continuous random variable.      %(before_notes)s      Notes     --`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 426`** (2 nodes): `f_gen`, `r"""An F continuous random variable.      For the noncentral F distribution, see`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 427`** (2 nodes): `halfcauchy_gen`, `r"""A Half-Cauchy continuous random variable.      %(before_notes)s      Notes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 428`** (2 nodes): `halflogistic_gen`, `r"""A half-logistic continuous random variable.      %(before_notes)s      Notes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 429`** (2 nodes): `invweibull_gen`, `An inverted Weibull continuous random variable.      This distribution is also k`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 430`** (2 nodes): `laplace_asymmetric_gen`, `r"""An asymmetric Laplace continuous random variable.      %(before_notes)s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 431`** (2 nodes): `ncf_gen`, `r"""A non-central F distribution continuous random variable.      %(before_notes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 432`** (2 nodes): `r"""Weibull maximum continuous random variable.      The Weibull Maximum Extreme`, `weibull_max_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 433`** (2 nodes): `r"""A Yule-Simon discrete random variable.      %(before_notes)s      Notes`, `yulesimon_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 454`** (2 nodes): `DiagBroyden`, `Find a root of a function, using diagonal Broyden Jacobian approximation.      T`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 455`** (2 nodes): `ExcitingMixing`, `Find a root of a function, using a tuned diagonal Jacobian approximation.      T`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 466`** (2 nodes): `intMalloc()`, `SetIWork()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 468`** (2 nodes): `hypsecant_gen`, `r"""A hyperbolic secant continuous random variable.      %(before_notes)s      N`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 469`** (2 nodes): `kappa3_gen`, `r"""Kappa 3 parameter distribution.      %(before_notes)s      Notes     -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 470`** (2 nodes): `kstwo_gen`, `r"""Kolmogorov-Smirnov two-sided test statistic distribution.      This is the d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 471`** (2 nodes): `loglaplace_gen`, `r"""A log-Laplace continuous random variable.      %(before_notes)s      Notes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 472`** (2 nodes): `r"""A triangular continuous random variable.      %(before_notes)s      Notes`, `triang_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 473`** (2 nodes): `r"""A Tukey-Lambda continuous random variable.      %(before_notes)s      Notes`, `tukeylambda_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 474`** (2 nodes): `r"""An R-distributed (symmetric beta) continuous random variable.      %(before_`, `rdist_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 475`** (2 nodes): `r"""A semicircular continuous random variable.      %(before_notes)s      See Al`, `semicircular_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 476`** (2 nodes): `r"""     A trapezoidal continuous random variable.      %(before_notes)s      No`, `trapezoid_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 485`** (2 nodes): `dop853`, `dopri5`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 488`** (2 nodes): `These are situations that can be tested in our pythran tests:     - A function w`, `_TestPythranFunc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 494`** (2 nodes): `LinearMixing`, `Find a root of a function, using a scalar Jacobian approximation.      .. warnin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 501`** (2 nodes): `z_abs()`, `z_sgn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 503`** (2 nodes): `c_abs()`, `c_sgn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 505`** (2 nodes): `betabinom_gen`, `r"""     A beta-binomial discrete random variable.      %(before_notes)s      Se`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 506`** (2 nodes): `boltzmann_gen`, `r"""A Boltzmann (Truncated Discrete Exponential) random variable.      %(before_`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 507`** (2 nodes): `dlaplace_gen`, `r"""A  Laplacian discrete random variable.      %(before_notes)s      Notes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 508`** (2 nodes): `nhypergeom_gen`, `r"""A negative hypergeometric discrete random variable.      Consider a box cont`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 509`** (2 nodes): `r"""A Zipfian discrete random variable.      %(before_notes)s      See Also`, `zipfian_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 522`** (2 nodes): `Wrapper class for hess calculation via finite differences`, `_ScalarHessWrapper`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 523`** (2 nodes): `KrylovJacobian`, `Find a root of a function, using Krylov approximation for inverse Jacobian.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 525`** (2 nodes): `convert_strides()`, `FIRsepsym2d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 539`** (1 nodes): `_BaseVersion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 543`** (2 nodes): `betanbinom_gen`, `r"""     A beta-negative-binomial discrete random variable.      %(before_notes)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 544`** (2 nodes): `logser_gen`, `r"""A Logarithmic (Log-Series, Series) discrete random variable.      %(before_n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 559`** (2 nodes): `Wrapper class for Jacobian calculation`, `_VectorHessWrapper`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 574`** (1 nodes): `lsoda`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 602`** (2 nodes): `CovViaCholesky`, `r"""         Representation of a covariance provided via the (lower) Cholesky fa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 603`** (2 nodes): `CovViaPrecision`, `r"""         Return a representation of a covariance from its precision matrix.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 614`** (1 nodes): `HighsOptionsManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 627`** (2 nodes): `_correlate_nd_imp()`, `scipy_signal__sigtools_correlateND()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 632`** (2 nodes): `multigammaln()`, `r"""Returns the log of multivariate gamma, also sometimes called the     general`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 639`** (2 nodes): `CovViaPSD`, `Representation of a covariance provided via an instance of _PSD`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 640`** (2 nodes): `_generate_example()`, `r""" Draw a specific (fully-defined) distribution from the family.          See`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 644`** (1 nodes): `_MockFunction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 649`** (1 nodes): `.. The heading is listed in the parent file `doc/reference/index.rst` to keep th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 650`** (1 nodes): `rbf - Radial basis functions for interpolation/smoothing scattered N-D data.  Wr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 658`** (2 nodes): `_maybe_convert_arg()`, `Convert arrays/scalars hiding in the sequence `arg`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 660`** (1 nodes): `Pythran implementation of columns grouping for finite difference Jacobian estima`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 667`** (1 nodes): `isspmatrix_dok()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 668`** (1 nodes): `r""" =================================== Sparse arrays (:mod:`scipy.sparse`) ===`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 678`** (2 nodes): `traverse_checking()`, `traverse_no_checking()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 679`** (2 nodes): `traverse_checking()`, `traverse_no_checking()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 680`** (2 nodes): `traverse_checking()`, `traverse_no_checking()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 687`** (2 nodes): `Initialize from a translation numpy array, without a rotation.          When app`, `Initialize a rigid transform from translation and rotation         components.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 689`** (2 nodes): `Routine for validation and conversion of csgraph inputs`, `validate_graph()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 690`** (2 nodes): `_clear_cache()`, `Cleans the SciPy datasets cache directory.      Parameters     ----------     da`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 697`** (1 nodes): `Here we perform some symbolic computations required for the N-D interpolation ro`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 699`** (2 nodes): `pade()`, `Return Pade approximation to a polynomial as the ratio of two polynomials.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 700`** (2 nodes): `_monomial_powers_impl()`, `Return the powers for each monomial in a polynomial.      Parameters     -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 701`** (2 nodes): `F`, `Callable wrapper for computing `fp(p)` for a fixed spline configuration.      Pa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 702`** (2 nodes): `lgmres()`, `Solve ``Ax = b`` with the LGMRES algorithm.      The LGMRES algorithm [1]_ [2]_`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 703`** (2 nodes): `minres()`, `Solve ``Ax = b`` with the MINimum RESidual method,     for a real symmetric or c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 704`** (2 nodes): `Solve ``Ax = b`` with the Transpose-Free Quasi-Minimal Residual method.      Par`, `tfqmr()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 706`** (2 nodes): `cossin()`, `Compute the cosine-sine (CS) decomposition of an orthogonal/unitary matrix.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 707`** (2 nodes): `polar()`, `Compute the polar decomposition.      Returns the factors of the polar decomposi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 712`** (2 nodes): `_minimize_cobyqa()`, `Minimize a scalar function of one or more variables using the     Constrained Op`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 717`** (2 nodes): `nnls()`, `Solve ``argmin_x || Ax - b ||_2^2`` for ``x>=0``.      This problem, often calle`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 719`** (2 nodes): `_minimize_trust_krylov()`, `Minimization of a scalar function of one or more variables using     a nearly ex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 720`** (1 nodes): `FunctionWithRoot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 722`** (2 nodes): `lagrange_inversion()`, `Given a series      f(x) = a[1]*x + a[2]*x**2 + ... + a[n-1]*x**(n - 1),      us`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 724`** (2 nodes): `max_len_seq()`, `Maximum length sequence (MLS) generator.      Parameters     ----------     nbit`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 725`** (2 nodes): `Sampling frequency of input signal and of the window.          The sampling freq`, `Sampling frequency of input signal and of the window.          The sampling freq`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 726`** (2 nodes): `Mode of utilized FFT ('twosided', 'centered', 'onesided' or         'onesided2X'`, `Set mode of FFT.          Allowed values are 'twosided', 'centered', 'onesided',`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 727`** (2 nodes): `Length of input for the FFT used - may be larger than window         length `m_n`, `Setter for the length of FFT utilized.          See the property `mfft` for furt`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 733`** (2 nodes): `_geometric_slerp()`, `Geometric spherical linear interpolation.      The interpolation occurs along a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 737`** (2 nodes): `cgstrs()`, `cprint_soln()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 742`** (2 nodes): `dgstrs()`, `dprint_soln()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 757`** (2 nodes): `sgstrs()`, `sprint_soln()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 763`** (2 nodes): `zgstrs()`, `zprint_soln()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 768`** (2 nodes): `crosstab()`, `Return table of counts for each possible unique combination in ``*args``.      W`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 772`** (2 nodes): `Compute the coefficient of variation.      The coefficient of variation is the s`, `variation()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 773`** (2 nodes): `gen()`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 776`** (2 nodes): `trlib_leftmost()`, `trlib_leftmost_irreducible()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 777`** (2 nodes): `parse_txt_data()`, `run_test()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 778`** (2 nodes): `generate_test_vecs()`, `test label with different structuring element neighborhoods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 779`** (1 nodes): `Eigenvalue solver using iterative methods.  Find k eigenvectors and eigenvalues`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 780`** (1 nodes): `Cython optimize root finding API ================================ The underlying`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 784`** (1 nodes): `Distributor init file  Distributors: you can replace the contents of this file w`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 785`** (1 nodes): `Module containing external code ===============================  The code in thi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 786`** (1 nodes): `Return definite integral of the spline between two given points.          Parame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 787`** (1 nodes): `Return all derivatives of the spline at the point x.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 788`** (1 nodes): `Return the zeros of the spline.          Notes         -----         Restriction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 789`** (1 nodes): `Construct a new spline representing the derivative of this spline.          Para`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 790`** (2 nodes): `default_xp()`, `In all ``xp_assert_*`` and ``assert_*`` function calls executed within this`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 791`** (2 nodes): `eager_warns()`, `pytest.warns context manager if arrays of specified namespace are always eager.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 792`** (2 nodes): `get_native_namespace_name()`, `Return name for native namespace (without array_api_compat prefix).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 793`** (2 nodes): `Copies a possibly on device array to a NumPy array.      This function is intend`, `_xp_copy_to_numpy()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 794`** (2 nodes): `Return the `scipy`-like namespace of a non-NumPy backend      That is, return th`, `scipy_namespace_for()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 795`** (1 nodes): `PUBLIC_MODULES was once included in scipy._lib.tests.test_public_api.  It has be`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 796`** (1 nodes): ``uarray` provides functions for generating multimethods that dispatch to multipl`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 800`** (2 nodes): `check_termination()`, `Check termination condition for nonlinear least squares.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 801`** (2 nodes): `CL_scaling_vector()`, `Compute Coleman-Li scaling vector and its derivatives.      Components of a vect`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 802`** (2 nodes): `compute_grad()`, `Compute gradient of the least-squares cost function.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 803`** (2 nodes): `compute_jac_scale()`, `Compute variables scale based on the Jacobian matrix.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 804`** (2 nodes): `evaluate_quadratic()`, `Compute values of a quadratic function arising in least squares.      The functi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 805`** (2 nodes): `intersect_trust_region()`, `Find the intersection of a line with the boundary of a trust region.      This f`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 806`** (2 nodes): `minimize_quadratic_1d()`, `Minimize a 1-D quadratic function subject to bounds.      The free term `c` is 0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 807`** (2 nodes): `Solve a general trust-region problem in 2 dimensions.      The problem is reform`, `solve_trust_region_2d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 808`** (2 nodes): `Update the radius of a trust region based on the cost reduction.      Returns`, `update_tr_radius()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 809`** (2 nodes): `Compute a min_step size required to reach a bound.      The function computes a`, `step_size_to_bound()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 810`** (2 nodes): `Solve a trust-region problem arising in least-squares minimization.      This fu`, `solve_lsq_trust_region()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 811`** (1 nodes): `This module contains least-squares algorithms.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 812`** (1 nodes): `This is the 'bare' ndimage API.  This --- private! --- module only collects impl`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 813`** (1 nodes): `Docstring components common to several ndimage functions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 814`** (2 nodes): `_add_a_b()`, `r"""Add "a" and "b" keys to each test from the "bracket" value`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 815`** (2 nodes): `aps01_f()`, `r"""Straightforward sum of trigonometric function and polynomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 816`** (2 nodes): `aps02_f()`, `r"""poles at x=n**2, 1st and 2nd derivatives at root are also close to 0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 817`** (2 nodes): `aps03_f()`, `r"""Rapidly changing at the root`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 818`** (2 nodes): `aps04_f()`, `r"""Medium-degree polynomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 819`** (2 nodes): `aps05_f()`, `r"""Simple Trigonometric function`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 820`** (2 nodes): `aps06_f()`, `r"""Exponential rapidly changing from -1 to 1 at x=0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 821`** (2 nodes): `aps07_f()`, `r"""Upside down parabola with parametrizable height`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 822`** (2 nodes): `aps08_f()`, `r"""Degree n polynomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 823`** (2 nodes): `aps09_f()`, `r"""Upside down quartic with parametrizable height`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 824`** (2 nodes): `aps10_f()`, `r"""Exponential plus a polynomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 825`** (2 nodes): `aps11_f()`, `r"""Rational function with a zero at x=1/n and a pole at x=0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 826`** (2 nodes): `aps12_f()`, `r"""nth root of x, with a zero at x=n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 827`** (2 nodes): `aps13_f()`, `r"""Function with *all* derivatives 0 at the root`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 828`** (2 nodes): `aps14_f()`, `r"""0 for negative x-values, trigonometric+linear for x positive`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 829`** (2 nodes): `aps15_f()`, `r"""piecewise linear, constant outside of [0, 0.002/(1+n)]`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 830`** (2 nodes): `cplx01_f()`, `r"""z**n-a:  Use to find the nth root of a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 831`** (2 nodes): `cplx02_f()`, `r"""e**z - a: Use to find the log of a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 832`** (2 nodes): `f1()`, `r"""f1 is a quadratic with roots at 0 and 1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 833`** (2 nodes): `f2()`, `r"""f2 is a symmetric parabola, x**2 - 1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 834`** (2 nodes): `f3()`, `r"""A quartic with roots at 0, 1, 2 and 3`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 835`** (2 nodes): `f4()`, `r"""Piecewise linear, left- and right- discontinuous at x=1, the root.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 836`** (2 nodes): `f5()`, `r"""     Hyperbola with a pole at x=1, but pole replaced with 0. Not continuous`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 837`** (2 nodes): `get_tests()`, `r"""Return the requested collection of test cases, as an array of dicts with sub`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 838`** (2 nodes): `_skip_if_poly1d()`, `sweep_poly_signature()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 839`** (1 nodes): `======================================= Signal processing (:mod:`scipy.signal`)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 841`** (1 nodes): `Instantiate `ShortTimeFFT` by using `get_window`.          The method `get_windo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 842`** (1 nodes): `r"""Create instance where the window and its dual are equal up to a         scal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 843`** (1 nodes): `Window function as real- or complex-valued 1d array.          This attribute is`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 844`** (1 nodes): `Time increment in signal samples for sliding window.          This attribute is`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 845`** (1 nodes): `Normalization applied to the window function         ('magnitude', 'psd', 'unita`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 846`** (1 nodes): `This is the 'bare' scipy.signal API.  This --- private! --- module only collects`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 848`** (2 nodes): `erf_zeros()`, `Compute the first nt zero in the first quadrant, ordered by absolute value.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 849`** (2 nodes): `euler()`, `Euler numbers E(0), E(1), ..., E(n).      The Euler numbers [1]_ are also known`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 850`** (2 nodes): `fresnel_zeros()`, `Compute nt complex zeros of sine and cosine Fresnel integrals S(z) and C(z).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 851`** (2 nodes): `fresnelc_zeros()`, `Compute nt complex zeros of cosine Fresnel integral C(z).      Parameters     --`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 852`** (2 nodes): `fresnels_zeros()`, `Compute nt complex zeros of sine Fresnel integral S(z).      Parameters     ----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 853`** (2 nodes): `jnjnp_zeros()`, `Compute zeros of integer-order Bessel functions Jn and Jn'.      Results are arr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 854`** (2 nodes): `kei_zeros()`, `Compute nt zeros of the Kelvin function kei.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 855`** (2 nodes): `keip_zeros()`, `Compute nt zeros of the derivative of the Kelvin function kei.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 856`** (2 nodes): `kelvin_zeros()`, `Compute `nt` zeros of all Kelvin functions.      Parameters     ----------     n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 857`** (2 nodes): `ker_zeros()`, `Compute nt zeros of the Kelvin function ker.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 858`** (2 nodes): `kerp_zeros()`, `Compute nt zeros of the derivative of the Kelvin function ker.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 859`** (2 nodes): `lmbda()`, `r"""Jahnke-Emden Lambda function, Lambdav(x).      This function is defined as [`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 860`** (2 nodes): `lqmn()`, `Sequence of associated Legendre functions of the second kind.      Computes the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 861`** (2 nodes): `lqn()`, `Legendre functions of the second kind.      Compute sequence of Legendre functio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 862`** (2 nodes): `mathieu_even_coef()`, `r"""Fourier coefficients for even Mathieu and modified Mathieu functions.      T`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 863`** (2 nodes): `mathieu_odd_coef()`, `r"""Fourier coefficients for odd Mathieu and modified Mathieu functions.      Th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 864`** (2 nodes): `obl_cv_seq()`, `Characteristic values for oblate spheroidal wave functions.      Compute a seque`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 865`** (2 nodes): `pbdn_seq()`, `Parabolic cylinder functions Dn(z) and derivatives.      Parameters     --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 866`** (2 nodes): `pbdv_seq()`, `Parabolic cylinder functions Dv(x) and derivatives.      Parameters     --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 867`** (2 nodes): `pbvv_seq()`, `Parabolic cylinder functions Vv(x) and derivatives.      Parameters     --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 868`** (2 nodes): `perm()`, `Permutations of N things taken k at a time, i.e., k-permutations of N.      It's`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 869`** (2 nodes): `pro_cv_seq()`, `Characteristic values for prolate spheroidal wave functions.      Compute a sequ`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 870`** (2 nodes): `r"""Compute Riccati-Bessel function of the first kind and its derivative.      T`, `riccati_jn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 871`** (2 nodes): `Compute Riccati-Bessel function of the second kind and its derivative.      The`, `riccati_yn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 872`** (2 nodes): `r"""Generate Stirling number(s) of the second kind.      Stirling numbers of the`, `stirling2()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 873`** (2 nodes): `r"""     Compute the softplus function element-wise.      The softplus function`, `softplus()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 874`** (2 nodes): `Compute nt zeros of Bessel function Y0(z), and derivative at each zero.      The`, `y0_zeros()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 875`** (2 nodes): `Compute nt zeros of Bessel function Y1(z), and derivative at each zero.      The`, `y1_zeros()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 979`** (1 nodes): `The local version segment of the version.          >>> print(Version("1.2.3").lo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 980`** (1 nodes): `The public portion of the version.          >>> Version("1.2.3").public`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 981`** (1 nodes): `The "base version" of the version.          >>> Version("1.2.3").base_version`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 982`** (1 nodes): `Whether this version is a pre-release.          >>> Version("1.2.3").is_prerelea`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 983`** (1 nodes): `Whether this version is a post-release.          >>> Version("1.2.3").is_postrel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 984`** (1 nodes): `Whether this version is a development release.          >>> Version("1.2.3").is_`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 985`** (1 nodes): `The first item of :attr:`release` or ``0`` if unavailable.          >>> Version(`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 986`** (1 nodes): `The second item of :attr:`release` or ``0`` if unavailable.          >>> Version`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1012`** (1 nodes): `Statistics-related constants.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1013`** (1 nodes): `Sane parameters for stats.distributions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1014`** (2 nodes): `_get_binomial_log_p_value_with_nuisance_param()`, `r"""     Compute the log pvalue in respect of a nuisance parameter considering`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1015`** (2 nodes): `_get_wilcoxon_distr2()`, `Distribution of probability of the Wilcoxon ranksum statistic r_plus (sum     of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1016`** (2 nodes): `_get_wilcoxon_distr()`, `Distribution of probability of the Wilcoxon ranksum statistic r_plus (sum     of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1017`** (2 nodes): `Calculate Kendall's tau-b and p-value from contingency table.`, `_tau_b()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1018`** (1 nodes): `=================================================================== Statistical`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1019`** (1 nodes): `r"""Differential entropy          In terms of probability density function :math`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1020`** (1 nodes): `r"""Inverse complementary cumulative distribution function.          The inverse`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1021`** (1 nodes): `r"""Inverse of the cumulative distribution function.          For monotonic cont`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1022`** (1 nodes): `r"""Inverse of the log of the complementary cumulative distribution function.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1023`** (1 nodes): `r"""Inverse of the logarithm of the cumulative distribution function.          T`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1024`** (1 nodes): `r"""Kurtosis (standardized fourth moment)          By default, this is the stand`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1025`** (1 nodes): `r"""L-moment or L-moment ratio of positive integer order.          The L-moment`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1026`** (1 nodes): `r"""Log of the complementary cumulative distribution function          The compl`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1027`** (1 nodes): `r"""Log of the cumulative distribution function          The cumulative distribu`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1028`** (1 nodes): `r"""Logarithm of the differential entropy          In terms of probability densi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1029`** (1 nodes): `r"""Log of the probability density function          The probability density fun`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1030`** (1 nodes): `r"""Log of the probability mass function          The probability mass function`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1031`** (1 nodes): `r"""Mean (raw first moment about the origin)          Parameters         -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1032`** (1 nodes): `r"""Median (50th percentile)          If a continuous random variable :math:`X``
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1033`** (1 nodes): `r"""Mode (most likely value)          Informally, the mode is a value that a ran`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1034`** (1 nodes): `r"""Raw, central, or standard moment of positive integer order.          In term`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1035`** (1 nodes): `r"""Probability density function          The probability density function ("PDF`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1036`** (1 nodes): `r"""Probability mass function          The probability mass function ("PMF"), de`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1037`** (1 nodes): `r"""Random sample from the distribution.          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1038`** (1 nodes): `r"""Skewness (standardized third moment)          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1039`** (1 nodes): `r"""Standard deviation (square root of the second central moment)          Param`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1040`** (1 nodes): `r"""Support of the random variable          The support of a random variable is`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1044`** (1 nodes): `This module contains the equality constrained SQP solver.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1045`** (1 nodes): `.. note:     If you are looking for overrides for NumPy-specific methods, see th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1046`** (1 nodes): `Window functions (:mod:`scipy.signal.windows`) =================================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FunctionDoc` connect `Community 1` to `Community 224`, `Community 619`, `Community 379`, `Community 793`, `Community 790`, `Community 791`, `Community 617`, `Community 792`, `Community 794`, `Community 579`, `Community 618`, `Community 580`, `Community 553`, `Community 22`, `Community 18`, `Community 8`, `Community 151`, `Community 13`, `Community 19`, `Community 256`, `Community 152`, `Community 368`, `Community 184`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Why does `MapWrapper` connect `Community 8` to `Community 96`, `Community 18`, `Community 1`, `Community 65`, `Community 5`, `Community 9`, `Community 33`, `Community 11`, `Community 6`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Why does `PytestTester` connect `Community 84` to `Community 173`, `Community 649`, `Community 262`, `Community 312`, `Community 5`, `Community 668`, `Community 375`, `Community 118`, `Community 239`, `Community 305`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Are the 328 inferred relationships involving `CensoredData` (e.g. with `alpha_gen` and `anglit_gen`) actually correct?**
  _`CensoredData` has 328 INFERRED edges - model-reasoned connections that need verification._
- **Are the 316 inferred relationships involving `FitError` (e.g. with `alpha_gen` and `anglit_gen`) actually correct?**
  _`FitError` has 316 INFERRED edges - model-reasoned connections that need verification._
- **Are the 242 inferred relationships involving `rv_continuous` (e.g. with `alpha_gen` and `anglit_gen`) actually correct?**
  _`rv_continuous` has 242 INFERRED edges - model-reasoned connections that need verification._
- **Are the 239 inferred relationships involving `LowLevelCallable` (e.g. with `.. The heading is listed in the parent file `doc/reference/index.rst` to keep th` and `alpha_gen`) actually correct?**
  _`LowLevelCallable` has 239 INFERRED edges - model-reasoned connections that need verification._