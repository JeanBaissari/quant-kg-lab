# Graph Report - .  (2026-07-29)

## Corpus Check
- cluster-only mode - file stats not available

## Summary
- 31042 nodes · 51352 edges · 1469 communities detected
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 7771 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: method: 15716 · contains: 12224 · calls: 9048 · uses: 7771 · rationale_for: 5315 · inherits: 1195 · imports_from: 75 · imports: 8


## Graph Freshness
- Built from Git commit: `0514ef9`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Benchmark` - 441 edges
2. `CensoredData` - 335 edges
3. `FitError` - 313 edges
4. `SmallSampleWarning` - 297 edges
5. `safe_import` - 288 edges
6. `Benchmark` - 286 edges
7. `rv_continuous` - 278 edges
8. `LowLevelCallable` - 256 edges
9. `UnivariateDistribution` - 196 edges
10. `MapWrapper` - 191 edges

## Surprising Connections (you probably didn't know these)
- `Bench` --uses--> `MikotaPair`  [INFERRED]
  benchmarks/benchmarks/sparse_linalg_lobpcg.py → scipy/sparse/linalg/_special_sparse_arrays.py
- `Bench` --uses--> `Sakurai`  [INFERRED]
  benchmarks/benchmarks/sparse_linalg_lobpcg.py → scipy/sparse/linalg/_special_sparse_arrays.py
- `Return list of docutils nodes representing a reST table.` --uses--> `BackendSupportStatus`  [INFERRED]
  doc/source/array_api_capabilities_table.py → scipy/_lib/_array_api_docs_tables.py
- `LegacyDirective` --uses--> `rv_generic`  [INFERRED]
  doc/source/conf.py → scipy/stats/_distn_infrastructure.py
- `# TODO: eventually these should be eliminated!` --uses--> `rv_generic`  [INFERRED]
  doc/source/conf.py → scipy/stats/_distn_infrastructure.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.01
Nodes (129): LowLevelCallable, Create a low-level callback function from an exported Cython function., Low-level callback function.      Some functions in SciPy take as arguments call, rv_continuous, anglit_gen, arcsine_gen, argus_gen, beta_gen (+121 more)

### Community 1 - "Community 1"
Cohesion: 0.02
Nodes (144): GetBlasLapackFuncs, Test the speed of grabbing the correct BLAS/LAPACK routine flavor.      In parti, Benchmark, LimitedParamBenchmark, Base class with sensible options, Limits parameter combinations to `max_number` choices, chosen     pseudo-randoml, safe_import, AAA (+136 more)

### Community 2 - "Community 2"
Cohesion: 0.01
Nodes (183): _asarray(), assert_almost_equal(), assert_array_almost_equal(), _assert_less(), _assert_matching_namespace(), _check_finite(), concat_1d(), _count_nonmasked() (+175 more)

### Community 3 - "Community 3"
Cohesion: 0.03
Nodes (216): PearsonRResultBase, SmallSampleWarning, BootstrapMethod, MonteCarloMethod, PermutationMethod, Configuration information for a Monte Carlo hypothesis test.      Instances of t, Configuration information for a permutation hypothesis test.      Instances of t, Configuration information for a bootstrap confidence interval.      Instances of (+208 more)

### Community 4 - "Community 4"
Cohesion: 0.01
Nodes (152): Benchmark, Evaluation of the benchmark function.          Parameters         ----------, Changes the dimensionality of the benchmark problem          The dimensionality, The lower/upper bounds to be used for minimizing the problem.         This a lis, The dimensionality of the problem.          Returns         -------         N :, The lower bounds for the problem          Returns         -------         xmin :, The upper bounds for the problem          Returns         -------         xmax :, Initialises the problem          Parameters         ----------          dimensio (+144 more)

### Community 6 - "Community 6"
Cohesion: 0.01
Nodes (61): _argus_phi(), burr_gen, chi_gen, cosine_gen, dpareto_lognorm_gen, expon_gen, fisk_gen, genextreme_gen (+53 more)

### Community 7 - "Community 7"
Cohesion: 0.01
Nodes (36): NormmaxTest, _old_loggamma_rvs(), Tests for stats.binomtest., Test boxcox_normmax raises ValueError if x contains non-positive values., # TODO: add method "pearsonr" after fix overflow issue, TestAnderson, TestAndersonKSamp, TestAndersonKSampVariant (+28 more)

### Community 8 - "Community 8"
Cohesion: 0.02
Nodes (42): Scalar function and its derivatives.      This class defines a scalar function F, ScalarFunction, brute_func(), CheckOptimize, CheckOptimizeParameterized, f1(), f2(), f3() (+34 more)

### Community 9 - "Community 9"
Cohesion: 0.01
Nodes (6): Regression test for #912., TestCephes, TestEllip, TestExp, TestFresnelIntegral, TestKelvin

### Community 10 - "Community 10"
Cohesion: 0.02
Nodes (132): fmin_cobyla(), _minimize_cobyla(), Interface to Constrained Optimization By Linear Approximation  Functions -------, Minimize a scalar function of one or more variables using the     Constrained Op, Minimize a function using the Constrained Optimization By Linear     Approximati, isotonic_regression(), r"""Nonparametric isotonic regression.      A (not strictly) monotonically incre, _convert_to_highs_enum() (+124 more)

### Community 11 - "Community 11"
Cohesion: 0.03
Nodes (54): rv_discrete, rv_discrete_frozen, bernoulli_gen, betabinom_gen, betanbinom_gen, binom_gen, boltzmann_gen, dlaplace_gen (+46 more)

### Community 13 - "Community 13"
Cohesion: 0.03
Nodes (109): Some statistics of the given RV.          Parameters         ----------, Variance of the distribution.          Parameters         ----------         arg, Standard deviation of the distribution.          Parameters         ----------, Class which encapsulates common functionality between rv_discrete     and rv_con, Construct the parser string for the shape arguments.          This method should, Construct the instance docstring with string substitutions., Construct instance docstring from the default template., Freeze the distribution for the given arguments.          Parameters         --- (+101 more)

### Community 14 - "Community 14"
Cohesion: 0.01
Nodes (1): # TODO: Do we want to support this for all Array API frameworks?

### Community 15 - "Community 15"
Cohesion: 0.02
Nodes (58): _assert_close_in_norm(), direct_dft(), direct_dftn(), direct_idft(), direct_idftn(), direct_irdft(), direct_rdft(), direct_rdftn() (+50 more)

### Community 16 - "Community 16"
Cohesion: 0.01
Nodes (1): TestNdimageMorphology

### Community 17 - "Community 17"
Cohesion: 0.03
Nodes (90): _arr_to_scalar(), new_bounds_to_old(), new_constraint_to_old(), old_bound_to_new(), old_constraint_to_new(), Constraints definition for minimize., Linear constraint on the variables.      The constraint has the general inequali, Calculate the residual between the constraint function and the limits. (+82 more)

### Community 18 - "Community 18"
Cohesion: 0.03
Nodes (31): NearestNDInterpolator, Benchmark NearestNDInterpolator.      Derived from the docstring example,     ht, BPoly, PPoly, B, _dpow(), P, _ppoly2d_eval() (+23 more)

### Community 19 - "Community 19"
Cohesion: 0.03
Nodes (6): _ProbabilityDistribution, _guess_bracket(), _isnull(), _log_real_standardize(), Mixture, UnivariateDistribution

### Community 20 - "Community 20"
Cohesion: 0.01
Nodes (1): TestSystematic

### Community 21 - "Community 21"
Cohesion: 0.05
Nodes (65): MapWrapper, Parallelisation wrapper for working with map-like callables, such as     `multip, Bounds, LinearConstraint, NonlinearConstraint, PreparedConstraint, _ConstraintWrapper, differential_evolution() (+57 more)

### Community 22 - "Community 22"
Cohesion: 0.03
Nodes (56): Benchmark, BatchedCholeskyBench, BatchedEigBench, BatchedLstsqBench, BatchedPinvBench, BatchedQRBench, BatchedSolveBench, BatchedSVDBench (+48 more)

### Community 23 - "Community 23"
Cohesion: 0.03
Nodes (90): LineSearchWarning, approx_fhess_p(), approx_fprime(), bracket(), BracketError, Brent, brute(), _Brute_Wrapper (+82 more)

### Community 24 - "Community 24"
Cohesion: 0.02
Nodes (1): TestNdimageFilters

### Community 25 - "Community 25"
Cohesion: 0.04
Nodes (66): ClassDoc, NumpyDocString, Parses a numpydoc string to an abstract representation      Instances define a m, Mapping, _combine_docs(), _Domain, _generate_domain_support(), _generate_example() (+58 more)

### Community 26 - "Community 26"
Cohesion: 0.05
Nodes (85): sparray, SparseEfficiencyWarning, _make_diagonal_csr(), Base class for sparse matrix formats using compressed storage., Remove zero entries from the array/matrix.          This is an *in place* operat, Whether the array/matrix has sorted indices and no duplicates          Returns, Eliminate duplicate entries by adding them together.          This is an *in pla, Whether the indices are sorted          Returns             - True: if the indic (+77 more)

### Community 27 - "Community 27"
Cohesion: 0.04
Nodes (3): Upcast array to a floating point format (if necessary), _spbase, SparseABC

### Community 28 - "Community 28"
Cohesion: 0.04
Nodes (45): fmin_l_bfgs_b(), LbfgsInvHessProduct, _minimize_lbfgsb(), Functions --------- .. autosummary::    :toctree: generated/      fmin_l_bfgs_b, Minimize a scalar function of one or more variables using the L-BFGS-B     algor, Linear operator for the L-BFGS approximate inverse Hessian.      This operator c, Construct the operator., Efficient matrix-vector multiply with the BFGS matrices.          This calculati (+37 more)

### Community 29 - "Community 29"
Cohesion: 0.03
Nodes (45): CensoredData, The number of values (censored and not censored)., Number of censored values.          Returns         -------         int, Create a `CensoredData` instance of right-censored data.          Parameters, Create a `CensoredData` instance of left-censored data.          Parameters, Create a `CensoredData` instance of interval-censored data.          This method, This function is used when a non-censored version of the data         is needed, Return a subset of self containing the values that are in         (or overlap wi (+37 more)

### Community 30 - "Community 30"
Cohesion: 0.03
Nodes (6): assert_array_equal_dtype(), test common functionality shared by all sparse formats, sparse_may_share_memory(), _TestCommon, _TestSlicingAssign, toarray()

### Community 31 - "Community 31"
Cohesion: 0.03
Nodes (29): alpha_gen, fatiguelife_gen, gibrat_gen, halfnorm_gen, johnsonsb_gen, johnsonsu_gen, levy_l_gen, lognorm_gen (+21 more)

### Community 33 - "Community 33"
Cohesion: 0.04
Nodes (26): check_equal_gmean(), check_equal_hmean(), check_equal_pmean(), check_equal_xmean(), NormalityTests, Test functions for stats module      WRITTEN BY LOUIS LUANGKESORN <lluang@yahoo., # TODO: isolate use of alt backend to ttest_ind, # TODO: write these tests to handle missing values properly (+18 more)

### Community 34 - "Community 34"
Cohesion: 0.07
Nodes (71): bsr_matrix, Block Sparse Row format sparse matrix.      .. warning::         SciPy sparse is, _block(), block_array(), block_diag(), bmat(), _compressed_sparse_stack(), diags() (+63 more)

### Community 35 - "Community 35"
Cohesion: 0.02
Nodes (2): Delegators for alternative backends in scipy.signal.  The signature of `func_sig, # TODO: fix me - `prominence` is not necessarily an array.

### Community 37 - "Community 37"
Cohesion: 0.04
Nodes (73): _all_partitions_concatenated(), _batch_generator(), _bca_interval(), bootstrap(), _bootstrap_iv(), _bootstrap_resample(), BootstrapResult, _calculate_null_both() (+65 more)

### Community 38 - "Community 38"
Cohesion: 0.03
Nodes (5): Yield points at which to compare Cephes implementation to AMOS, Negative-order Bessels, Real-valued Bessel domains, Real-valued Bessel I overflow, TestBessel

### Community 39 - "Community 39"
Cohesion: 0.05
Nodes (71): qh_all_merges(), qh_all_vertexmerges(), qh_appendmergeset(), qh_appendvertexmerge(), qh_basevertices(), qh_checkdelridge(), qh_checkzero(), qh_copynonconvex() (+63 more)

### Community 40 - "Community 40"
Cohesion: 0.03
Nodes (12): _desc_stats(), TestKendallTau, TestKendallTauAlternative, TestLMoment, TestObrientransform, TestSigmaClip, TestTTestInd, TestTTestIndMore (+4 more)

### Community 41 - "Community 41"
Cohesion: 0.04
Nodes (51): Base classes for low memory simplicial complex structures., Convert a vertex-face mesh to a vertex-vertex mesh used by this class          P, Adds a vertex at coords v_x to the complex that is not symmetric to the, Check if a vector v_x is in simplex `S`.          Parameters         ----------, # NOTE: We keep the variable A_11, but we loop through A_jj, # TODO: Unlikely to work in many cases, # TODO: Note that scipy might be faster to add as an optional, # TODO: Note if sign_det_A_j0 == then the point is coplanar to the (+43 more)

### Community 42 - "Community 42"
Cohesion: 0.02
Nodes (17): _assert_hasattr(), _distr3_gen, Test functions for stats module, Test the powerlaw stats function.      This unit test is also a regression test, # FIXME: this is only a quick-and-dirty test of a quick-and-dirty bugfix., regression test for gh-6219, Test fitting invweibull to data.      Here is a the same calculation in R:, test_api_regression() (+9 more)

### Community 43 - "Community 43"
Cohesion: 0.05
Nodes (77): dlti, r"""     Discrete-time linear time invariant system base class.      Parameters, Return the sampling time of the system., _angle(), _bvalfromboundary(), choose_conv_method(), _conv_ops(), convolve() (+69 more)

### Community 44 - "Community 44"
Cohesion: 0.04
Nodes (25): check_equal_gmean(), check_equal_hmean(), Tests for the stats.mstats module (support for masked arrays), Simple test to ensure tuple backwards-compatibility of the returned         Thei, Simple test to ensure tuple backwards-compatibility of the returned     Siegelsl, # TODO: for all ttest functions, add tests with masked array inputs, Tests for mstats.describe.      Note that there are also tests for `mstats.descr, test_siegelslopes_namedtuple_consistency() (+17 more)

### Community 45 - "Community 45"
Cohesion: 0.03
Nodes (20): assert_any_equal(), _cases(), check_mat_write_warning(), _load_check_case(), mlarr(), _rt_check_case(), test_deprecation(), test_invalid_field_name_warning() (+12 more)

### Community 46 - "Community 46"
Cohesion: 0.14
Nodes (62): SparseABC, sparray, isspmatrix(), Base class for sparse matrices, Reverses the dimensions of the sparse array/matrix.          Parameters, Element-wise complex conjugation.          If the array/matrix is of non-complex, Nonzero indices of the array/matrix.          Returns         -------         ro, Returns a copy of column j of the array, as an (m x 1) sparse         array (col (+54 more)

### Community 47 - "Community 47"
Cohesion: 0.04
Nodes (45): BaseQuadraticSubproblem, BaseQuadraticSubproblem, DoglegSubproblem, _minimize_dogleg(), Dog-leg trust-region optimization., Minimization of scalar function of one or more variables using     the dog-leg t, Quadratic subproblem solved by the dogleg method, The Cauchy point is minimal along the direction of steepest descent. (+37 more)

### Community 48 - "Community 48"
Cohesion: 0.04
Nodes (55): _asarray_square(), coshm(), cosm(), _ell(), _eq_10_42(), _exp_sinch(), expm(), _ExpmPadeHelper (+47 more)

### Community 49 - "Community 49"
Cohesion: 0.03
Nodes (25): FitError, _check_fit_input_parameters(), FitSolverError, FitUniformFixedScaleDataError, _get_left_bracket(), halfcauchy_gen, laplace_gen, pareto_gen (+17 more)

### Community 50 - "Community 50"
Cohesion: 0.05
Nodes (10): abs(), exp(), FoldedDistribution, log(), MonotonicTransformedDistribution, OrderStatisticDistribution, ShiftedScaledDistribution, TransformedDistribution (+2 more)

### Community 51 - "Community 51"
Cohesion: 0.03
Nodes (1): TestPdist

### Community 52 - "Community 52"
Cohesion: 0.04
Nodes (7): solve_triangular on a simple 2x2 matrix., solve_triangular on a simple 2x2 complex matrix, TestInv, TestPinv, TestPinvSymmetric, TestSolve, TestSolveTriangular

### Community 53 - "Community 53"
Cohesion: 0.03
Nodes (10): _get_al_mohy_higham_2012_experiment_1(), _normalized_like(), _relative_error(), TestExpmConditionNumber, TestExpmFrechet, TestFractionalMatrixPower, TestKhatriRao, TestLogM (+2 more)

### Community 54 - "Community 54"
Cohesion: 0.07
Nodes (24): ContinuousDistribution, DiscreteDistribution, ContinuousDistribution, DiscreteDistribution, .. _statsrefmanual:  ========================================== Statistical func, Binomial, _Gamma, _log_diff() (+16 more)

### Community 55 - "Community 55"
Cohesion: 0.03
Nodes (5): W.II.D. Compute a correlation matrix on all the variables.          All the corr, TestCorrSpearmanr, TestMedianAbsDeviation, TestPageTrendTest, TestPearsonrWilkinson

### Community 56 - "Community 56"
Cohesion: 0.03
Nodes (14): _TestPythranFunc, Some tests to show that barnard_exact() works correctly., The expected values have been generated by R, using a resolution         for the, "The expected values have been generated by R, using a resolution         for th, Some tests to show that boschloo_exact() works correctly., # TODO: complete input validation tests, # NOTE: No statistics are computed for x * y because x has fewer, TestBarnardExact (+6 more)

### Community 57 - "Community 57"
Cohesion: 0.03
Nodes (1): TestDifferentialEvolutionSolver

### Community 58 - "Community 58"
Cohesion: 0.04
Nodes (32): MaratosTestArgs, LennardJones objective function. Used to test symmetry constraints     settings., Iterative simplicial sampling on TestFunction 1 (multivariate), Iterative simplicial on TestFunction 2 (univariate), Iterative Sobol sampling on TestFunction 1 (multivariate), Iterative Sobol sampling on TestFunction 2 (univariate), Iterative sampling on TestFunction 1 and 2  (multi and univariate), Using `args` used to cause `shgo` to fail; see #14589, #15986,         #16506 (+24 more)

### Community 59 - "Community 59"
Cohesion: 0.07
Nodes (64): barthann(), bartlett(), blackman(), blackmanharris(), bohman(), boxcar(), chebwin(), cosine() (+56 more)

### Community 60 - "Community 60"
Cohesion: 0.07
Nodes (41): Anderson, _array_like(), _as_inexact(), asjacobian(), BroydenFirst, BroydenSecond, DiagBroyden, ExcitingMixing (+33 more)

### Community 61 - "Community 61"
Cohesion: 0.06
Nodes (43): _AdjointLinearOperator, _AdjointMatrixOperator, aslinearoperator(), _CustomLinearOperator, _get_dtype(), MatrixLinearOperator, _PowerLinearOperator, _ProductLinearOperator (+35 more)

### Community 62 - "Community 62"
Cohesion: 0.04
Nodes (18): check_ccdf2(), check_cdf2(), check_dist_func(), check_lmoment_funcs(), check_moment_funcs(), check_nans_and_edges(), check_sample_shape_NaNs(), check_support() (+10 more)

### Community 63 - "Community 63"
Cohesion: 0.07
Nodes (12): Class to compare mstats results with stats results.      It is in general assume, Returns list of sample sizes to be used for comparison., Checks that mstats.ks_1samp and stats.ks_1samp agree on masked arrays., Checks that 1-sample mstats.kstest and stats.kstest agree on masked arrays., Checks that mstats.ks_2samp and stats.ks_2samp agree on masked arrays.         g, Checks that 2-sample mstats.kstest and stats.kstest agree on masked arrays., Comparison numbers are found using R v.1.5.1          note that length(testcase), TestCompareWithStats (+4 more)

### Community 64 - "Community 64"
Cohesion: 0.06
Nodes (21): TestBeta, TestBetaPrime, TestChi, TestChi2, TestDweibull, TestExponWeib, TestGamma, TestGenLogistic (+13 more)

### Community 65 - "Community 65"
Cohesion: 0.05
Nodes (3): np.matrix inputs are allowed for backwards compatibility, TestInterpN, TestRegularGridInterpolator

### Community 66 - "Community 66"
Cohesion: 0.04
Nodes (6): TestIQR, TestJarqueBera, TestKruskal, TestMode, TestPowerDivergence, TestScoreatpercentile

### Community 67 - "Community 67"
Cohesion: 0.06
Nodes (42): qh_check_bestdist(), qh_check_maxout(), qh_check_output(), qh_check_point(), qh_check_points(), qh_checkconvex(), qh_checkflipped_all(), qh_checklists() (+34 more)

### Community 68 - "Community 68"
Cohesion: 0.06
Nodes (2): _dok_base, isspmatrix_dok()

### Community 69 - "Community 69"
Cohesion: 0.06
Nodes (2): BaseQRinsert, check_qr()

### Community 70 - "Community 70"
Cohesion: 0.03
Nodes (57): Unit tests for module `_short_time_fft`.  This file's structure loosely groups t, Test the parameter 'padding' of `stft` with roundtrips.      The STFT parametriz, Test if a `psd`-scaled STFT conserves the L2 norm.      This test is adapted fro, STFT Roundtrip correctness of closest dual window., STFT Roundtrip correctness of closest dual window with complex values., Test if `closest_STFT_dual_window` generalizes `check_COLA`.      The parameters, Verify that exceptions get raised on invalid parameters when     instantiating S, Verify that exceptions get raised when setting properties or calling     method (+49 more)

### Community 71 - "Community 71"
Cohesion: 0.05
Nodes (31): Get the mean of the transforms.          The mean of a set of transforms is the, Return a copy of the matrix representation of the transform.          4x4 rigid, Return the translation and rotation components of the transform,         where t, Return the exponential coordinates of the transform.          This implements th, Return the dual quaternion representation of the transform.          Unit dual q, Return the length of the leading transform dimension.          A transform can s, Extract transform(s) at given index(es) from this object.          Creates a new, Set transform(s) at given index(es) in this object.          Parameters (+23 more)

### Community 72 - "Community 72"
Cohesion: 0.16
Nodes (50): MATLAB® file utilities (:mod:`scipy.io.matlab`) ================================, _has_struct(), _inspect_cell_array(), _matstruct_to_dict(), mat_struct, MatlabFunction, MatlabObject, MatlabOpaque (+42 more)

### Community 73 - "Community 73"
Cohesion: 0.06
Nodes (18): assert_array_identical(), assert_identical(), Assert whether value AND type are the same, Assert whether values AND type are the same, Test that sav files with description tag read at all, Test that .sav file with IDENTIFICATION section read correctly., test_identification(), test_invalid_pointer() (+10 more)

### Community 74 - "Community 74"
Cohesion: 0.04
Nodes (10): HistFunctionsTest, quantile_test_reference(), Comparison numbers are found using R v.1.5.1         note that length(testcase), r""" Test the non-parametric quantile test,     including the computation of con, TestCumfreq, TestMoments, TestPearsonr, TestQuantileTest (+2 more)

### Community 75 - "Community 75"
Cohesion: 0.04
Nodes (29): ABC, issparse(), Is `x` either sparse array or sparse matrix type?      Parameters     ----------, _ProbabilityDistribution, r"""Log of the probability mass function          The probability mass function, r"""Random sample from the distribution.          Parameters         ----------, r"""Cumulative distribution function          The cumulative distribution functi, r"""Inverse of the cumulative distribution function.          For monotonic cont (+21 more)

### Community 76 - "Community 76"
Cohesion: 0.08
Nodes (39): ArpackError, ArpackNoConvergence, _ArpackParams, choose_ncv(), eigs(), eigsh(), _fast_spmatrix_to_csc(), get_inv_matvec() (+31 more)

### Community 77 - "Community 77"
Cohesion: 0.06
Nodes (31): complex_ode, dop853, dopri5, find_integrator(), IntegratorBase, IntegratorConcurrencyError, lsoda, ode (+23 more)

### Community 78 - "Community 78"
Cohesion: 0.07
Nodes (49): _align_32(), AttrDict, ObjectPointer, Pointer, Read a signed 32-bit integer, Read a signed 16-bit integer, Read a signed 64-bit integer, Read an unsigned 16-bit integer (+41 more)

### Community 79 - "Community 79"
Cohesion: 0.08
Nodes (10): _block_diag(), _convert_to_2d(), _coo_base, _extract_block_diag(), _get_dense_data_and_coords(), _get_sparse_data_and_coords(), isspmatrix_coo(), _process_axes() (+2 more)

### Community 80 - "Community 80"
Cohesion: 0.05
Nodes (29): assert_in(), ComparisonTester, COONonCanonicalMixin, _NonCanonicalCompressedMixin, _NonCanonicalCSMixin, _NonCanonicalMixin, _possibly_unimplemented(), Construct a class that either runs tests as usual (require=True),     or each me (+21 more)

### Community 81 - "Community 81"
Cohesion: 0.09
Nodes (3): get_nearly_hermitian(), get_random(), TestBatch

### Community 82 - "Community 82"
Cohesion: 0.04
Nodes (15): assert_fit_warnings(), _assert_less_or_close_loglike(), Test that the vonmises expectation values are         computed correctly.  This, This utility function checks that the negative log-likelihood function     (or `, TestGumbel_r_l, TestHalfCauchy, TestHalfNorm, TestLaplace (+7 more)

### Community 83 - "Community 83"
Cohesion: 0.06
Nodes (22): BenchDFO, BenchGlobal, BenchLeastSquares, _BenchOptimizers, BenchSmoothUnbounded, group the results by minimizer and average over the runs, Do an optimization run for basinhopping, Do an optimization run for direct (+14 more)

### Community 84 - "Community 84"
Cohesion: 0.05
Nodes (25): FitDataError, Sample data points for pdf computed with CERN's ROOT          See - https://root, Tests fit for cases where floc is set.          `rel_breitwigner` has special ha, Sample data points computed using the `ST5` distribution from the         GAMLSS, Compare the pdf with a table of reference values. The table of         reference, Setup default parameters for levy_stable generator, Sample data points for pdf computed with Nolan's stablec          See - http://f, Sample data points for cdf computed with Nolan's stablec          See - http://f (+17 more)

### Community 85 - "Community 85"
Cohesion: 0.08
Nodes (34): RegularGridInterpolator, F, Fperiodic, The r.h.s. of ``f(p) = s``.      Given scalar `p`, we solve the system of equati, Fit a smooth periodic B-spline curve to given data points.      This class fits, _add_knot(), B_012(), B_0123() (+26 more)

### Community 86 - "Community 86"
Cohesion: 0.08
Nodes (28): MatFileReader, arr_to_2d(), MatFile4Reader, Classes for read / write of matlab (TM) 4 files, Class to read matlab 4 variables, Read and return header for variable, Mat4 read using header `hdr` dtype and dims          Parameters         --------, Full (rather than sparse) matrix getter          Read matrix (array) can be real (+20 more)

### Community 87 - "Community 87"
Cohesion: 0.04
Nodes (36): LinearTimeInvariant, r"""     Discrete-time Linear Time Invariant system in transfer function form., r"""     Linear Time Invariant system class in zeros, poles, gain form.      Rep, Initialize the zeros, poles, gain system., Return representation of the `ZerosPolesGain` system., Zeros of the `ZerosPolesGain` system., Poles of the `ZerosPolesGain` system., Gain of the `ZerosPolesGain` system. (+28 more)

### Community 88 - "Community 88"
Cohesion: 0.05
Nodes (34): Matyas, McCormick, Meyer, Michalewicz, MieleCantrell, Mishra01, Mishra02, Mishra03 (+26 more)

### Community 89 - "Community 89"
Cohesion: 0.11
Nodes (51): bispeu(), bispev(), clocur(), curfit(), dblint(), fpader(), fpback(), fpbacp() (+43 more)

### Community 90 - "Community 90"
Cohesion: 0.07
Nodes (22): InfinityType, NegativeInfinityType, This class abstracts handling of a project's versions.      A :class:`Version` i, A representation of the Version that shows all internal state.          >>> Vers, A string representation of the version that can be round-tripped.          >>> s, The epoch of the version.          >>> Version("2.0.0").epoch         0, The components of the "release" segment of the version.          >>> Version("1., The pre-release segment of the version.          >>> print(Version("1.2.3").pre) (+14 more)

### Community 91 - "Community 91"
Cohesion: 0.05
Nodes (47): _all_partitions(), barnard_exact(), BarnardExactResult, boschloo_exact(), BoschlooExactResult, _cdf_cvm(), _cdf_cvm_inf(), _compute_log_combinations() (+39 more)

### Community 92 - "Community 92"
Cohesion: 0.09
Nodes (20): Unit test for constraint conversion, TestNewToOld, TestNewToOldCobyla, TestNewToOldSLSQP, TestOldToNew, BoundedRosenbrock, Elec, EqIneqRosenbrock (+12 more)

### Community 93 - "Community 93"
Cohesion: 0.05
Nodes (18): All values are calculated using the independent implementation of the         RO, TestArrayArgument, TestBernoulli, TestBinom, TestCrystalBall, TestDLaplace, TestErlang, TestFoldNorm (+10 more)

### Community 94 - "Community 94"
Cohesion: 0.06
Nodes (26): compute_error(), fun_rational(), _get_harmonic_oscillator(), jac_complex(), jac_complex_sparse(), jac_linear(), medazko_sparsity(), Verify that select_initial_step respects max_step (+18 more)

### Community 95 - "Community 95"
Cohesion: 0.09
Nodes (52): assoc_legendre_factor(), assoc_legendre_p_0_0(), assoc_legendre_p_0_0_jac(), assoc_legendre_p_1_0_jac(), assoc_legendre_p_1_1(), assoc_legendre_p_1_1_jac(), assoc_legendre_p_1_1_jac_div_z(), assoc_legendre_p_1_m1() (+44 more)

### Community 96 - "Community 96"
Cohesion: 0.07
Nodes (14): F(), Unit tests for nonlinear solvers Author: Ondrej Certik May 2007, Check the Broyden methods for a few test problems.      broyden1, broyden2, and, Test for ENH #21986, for behavior of `nonlin.newton_krylov`         Test the fol, Check that some Jacobian approximations satisfy the secant condition, Check that the given Jacobian approximation satisfies secant         conditions, Solve a linear equation;     some methods find the exact solution in a finite nu, Check that solve/dot methods in Jacobian approximations are consistent (+6 more)

### Community 97 - "Community 97"
Cohesion: 0.06
Nodes (23): Argmax, Arithmetic, BlockDiagDenseConstruction, BlockDiagSparseConstruction, Construction, Conversion, CsrHstack, Densify (+15 more)

### Community 98 - "Community 98"
Cohesion: 0.06
Nodes (15): _get_backend(), Module for RBF interpolation., Evaluate the interpolation while controlling memory consumption.         We chun, Evaluate the interpolant at `x`.          Parameters         ----------, Radial basis function interpolator in N ≥ 1 dimensions.      Parameters     ----, RBFInterpolator, _1d_test_function(), _2d_test_function() (+7 more)

### Community 99 - "Community 99"
Cohesion: 0.04
Nodes (8): MatrixPowerOperator, ProductOperator, For now, this is limited to products of multiple square matrices., Initialize the object.          Parameters         ----------         A : a dens, _burkardt_13_power(), A helper function for testing matrix functions.      Parameters     ----------, TestExpM, TestOperators

### Community 100 - "Community 100"
Cohesion: 0.04
Nodes (1): r""" Parameters used in test and benchmark methods.  Collections of test cases s

### Community 101 - "Community 101"
Cohesion: 0.07
Nodes (52): chyp1f1_wrap(), special_cairy(), special_cairye(), special_ccyl_bessel_i(), special_ccyl_bessel_ie(), special_ccyl_bessel_j(), special_ccyl_bessel_je(), special_ccyl_bessel_k() (+44 more)

### Community 102 - "Community 102"
Cohesion: 0.06
Nodes (34): check_onetree_query(), kdtree_type(), # NOTE: this will fail when run via valgrind,, simulate_periodic_box(), test_ball_point_ints(), test_ckdtree_parallel(), test_discontiguous(), test_immutable() (+26 more)

### Community 103 - "Community 103"
Cohesion: 0.06
Nodes (5): BatchSpline, _make_random_spline(), _sum_basis_elements(), TestBatch, TestBSpline

### Community 104 - "Community 104"
Cohesion: 0.05
Nodes (24): check_cdf_logcdf(), check_cdf_ppf(), check_cdf_sf(), check_distribution_rvs(), check_fit_args(), check_fit_args_fix(), check_loc_scale(), check_pdf() (+16 more)

### Community 105 - "Community 105"
Cohesion: 0.08
Nodes (50): sph_legendre_factor(), sph_legendre_p_0_0(), sph_legendre_p_1_0(), sph_legendre_p_1_0_jac(), sph_legendre_p_1_1(), sph_legendre_p_1_1_jac(), sph_legendre_p_1_m1(), sph_legendre_p_1_m1_jac() (+42 more)

### Community 106 - "Community 106"
Cohesion: 0.05
Nodes (32): Parsopoulos, Pathological, Paviani, Penalty01, Penalty02, PenHolder, PermFunction01, PermFunction02 (+24 more)

### Community 108 - "Community 108"
Cohesion: 0.06
Nodes (34): big_fun(), big_fun_with_parameters(), big_sol(), big_sol_with_parameters(), emden_bc(), emden_bc_jac(), emden_fun(), emden_fun_jac() (+26 more)

### Community 109 - "Community 109"
Cohesion: 0.04
Nodes (25): If set, add linear phase `phase_shift` / `mfft` * `f` to each FFT         slice, The absolute value of the phase shift needs to be less than mfft         samples, Check if STFT is invertible.          This is achieved by trying to calculate th, Factor to multiply the STFT values by to scale each frequency slice         to a, Number of samples in window `win`.          Note that the FFT can be oversampled, Center index of window `win`.          For odd `m_num`, ``(m_num - 1) / 2`` is r, Smallest signal index and slice index due to padding.           Since, per conve, The smallest possible signal index of the STFT.          `k_min` is the index of (+17 more)

### Community 110 - "Community 110"
Cohesion: 0.06
Nodes (28): dirichlet_frozen, matrix_normal_frozen, matrix_t_frozen, multi_rv_frozen, normal_inverse_gamma_frozen, ortho_group_frozen, random_correlation_frozen, random_table_frozen (+20 more)

### Community 111 - "Community 111"
Cohesion: 0.04
Nodes (2): # NOTE: tests the reuse of bin_edges from previous call, TestBinnedStatistic

### Community 112 - "Community 112"
Cohesion: 0.04
Nodes (6): Unit test for DIRECT optimization algorithm., TestBlasIntSize, TestBLASLevel1, TestBLASLevel3, TestDIRECT, TestLAPACK

### Community 113 - "Community 113"
Cohesion: 0.06
Nodes (10): _check_svds(), _check_svds_n(), CheckingLinearOperator, # TODO: arpack crashes when v0=v0, which="SM", sorted_svd(), SVDSCommonTests, Test_SVDS_ARPACK, Test_SVDS_LOBPCG (+2 more)

### Community 114 - "Community 114"
Cohesion: 0.07
Nodes (30): FixedRule, NestedFixedRule, _apply_fixed_rule(), _cached_cast(), _cartesian_product(), FixedRule, NestedFixedRule, ProductNestedFixed (+22 more)

### Community 115 - "Community 115"
Cohesion: 0.06
Nodes (41): det(), _format_emit_errors_warnings(), _get_axis_len(), inv(), lstsq(), matmul_toeplitz(), _matmul_toepltiz(), matrix_balance() (+33 more)

### Community 116 - "Community 116"
Cohesion: 0.04
Nodes (1): Delegators for alternative backends in scipy.ndimage.  The signature of `func_si

### Community 117 - "Community 117"
Cohesion: 0.08
Nodes (2): _cs_matrix, _process_slice()

### Community 118 - "Community 118"
Cohesion: 0.04
Nodes (1): TestQR

### Community 119 - "Community 119"
Cohesion: 0.09
Nodes (31): BaseAxpy, BaseCopy, BaseGemv, BaseScal, BaseSwap, matrixmultiply(), Mixin class for scal testing, Mixin class for copy testing (+23 more)

### Community 121 - "Community 121"
Cohesion: 0.05
Nodes (15): Scalar arguments still produce a 2D array., Test convolution_matrix vs. numpy.convolve for various parameters., Make a complex or real test vector of length n., TestBlockDiag, TestCirculant, TestCompanion, TestConvolutionMatrix, TestHadamard (+7 more)

### Community 122 - "Community 122"
Cohesion: 0.05
Nodes (19): Ackley, AsymmetricQuadratic, Beale, Booth, CrossInTray, EggHolder, HolderTable, Levi (+11 more)

### Community 123 - "Community 123"
Cohesion: 0.07
Nodes (32): qh_copypoints(), qh_determinant(), qh_detjoggle(), qh_detmaxoutside(), qh_detroundoff(), qh_detsimplex(), qh_distround(), qh_divzero() (+24 more)

### Community 124 - "Community 124"
Cohesion: 0.08
Nodes (39): _briggs_helper_function(), _fractional_matrix_power(), _fractional_power_pade(), _fractional_power_pade_constant(), _fractional_power_superdiag_entry(), FractionalMatrixPowerError, _inverse_squaring_helper(), _logm() (+31 more)

### Community 125 - "Community 125"
Cohesion: 0.07
Nodes (43): binary_closing(), binary_dilation(), _binary_erosion(), binary_fill_holes(), binary_hit_or_miss(), binary_opening(), binary_propagation(), black_tophat() (+35 more)

### Community 126 - "Community 126"
Cohesion: 0.05
Nodes (41): broadcast_shapes(), check_shape(), convert_pydata_sparse_to_scipy(), downcast_intp_index(), get_index_dtype(), get_sum_dtype(), getdata(), getdtype() (+33 more)

### Community 127 - "Community 127"
Cohesion: 0.05
Nodes (12): dgamma_gen, genhyperbolic_gen, nct_gen, norminvgauss_gen, _norminvgauss_quadrature(), r"""A Von Mises continuous random variable.      %(before_notes)s      See Also, r"""A double gamma continuous random variable.      The double gamma distributio, r"""A generalized hyperbolic continuous random variable.      %(before_notes)s (+4 more)

### Community 128 - "Community 128"
Cohesion: 0.09
Nodes (13): BetaPrime, Burr, LogLaplace, LogNormal, Normal, NormInvGauss, Pearson3, Reference implementation of the SkewNormal distribution.      Follow the example (+5 more)

### Community 129 - "Community 129"
Cohesion: 0.15
Nodes (22): cases_64bit(), Test functions involving 64bit or 32bit indexing, Yield all tests for all formats      This is more than testing get_index_dtype., RunAll64Bit, Test64BitArray, Test64BitArrayExtra, Test64BitMatrix, Test64BitMatrixExtra (+14 more)

### Community 130 - "Community 130"
Cohesion: 0.08
Nodes (7): _assert_success(), LinprogCommonTests, Test whether bug described at:         https://github.com/scipy/scipy/issues/897, Additional test for:         https://github.com/scipy/scipy/issues/8973, Test for linprog docstring problem         'disp'=True caused revised simplex fa, Test for redundancy removal tolerance issue         https://github.com/scipy/sci, Base class for `linprog` tests. Generally, each test will be performed     once

### Community 131 - "Community 131"
Cohesion: 0.05
Nodes (16): Hock and Schittkowski 18 problem (HS18). Hoch and Schittkowski (1981)     http:/, Hock and Schittkowski 11 problem (HS11). Hoch and Schittkowski (1981)      NOTE:, Test function with no feasible domain., Scalar function with several minima to test all minimiser retrievals, # TODO: Make default n higher for faster tests, # TODO: This test doesn't cover anything new, it is unknown what the, StructTest1, StructTest2 (+8 more)

### Community 132 - "Community 132"
Cohesion: 0.07
Nodes (27): ArrayNamespace, scipy wrapper around array_api_compat.array_namespace, Bare array_api_compat.array_namespace, Trivial function that internally calls `xp=array_namespace(*args)`, IsIsomorphic, KMeans, KMeans2, Linkage (+19 more)

### Community 133 - "Community 133"
Cohesion: 0.14
Nodes (30): InterpolatedUnivariateSpline, LSQBivariateSpline, LSQSphereBivariateSpline, LSQUnivariateSpline, 1-D interpolating spline for a given set of data points.      .. legacy:: class, 1-D spline with explicit internal knots.      .. legacy:: class          Specifi, Smooth bivariate spline approximation.      Parameters     ----------     x, y,, Weighted least-squares bivariate spline approximation.      Parameters     ----- (+22 more)

### Community 134 - "Community 134"
Cohesion: 0.10
Nodes (38): _compute_cost_div_m(), _compute_p_max(), _condition_3_13(), _exact_1_norm(), _exact_inf_norm(), expm_multiply(), _expm_multiply_interval(), _expm_multiply_interval_core_0() (+30 more)

### Community 135 - "Community 135"
Cohesion: 0.06
Nodes (42): center_of_mass(), extrema(), find_objects(), histogram(), label(), labeled_comprehension(), maximum(), maximum_position() (+34 more)

### Community 136 - "Community 136"
Cohesion: 0.07
Nodes (27): cdist_cosine(), cdist_hamming_char(), cdist_hamming_double(), cdist_mahalanobis(), cdist_minkowski(), cdist_seuclidean(), cdist_weighted_chebyshev(), cdist_weighted_minkowski() (+19 more)

### Community 137 - "Community 137"
Cohesion: 0.05
Nodes (11): _axis_nan_policy_test(), _check_arrays_broadcastable(), _homogeneous_data_generator(), _mixed_data_generator(), nan_policy_1d(), skip_nan_unexpected_exception(), test_axis_nan_policy_axis_is_None(), test_axis_nan_policy_fast() (+3 more)

### Community 138 - "Community 138"
Cohesion: 0.05
Nodes (5): Test that logsumexp doesn't accidentally write back to its parameters., Test input device propagation to output., TestLogSoftmax, TestLogSumExp, TestSoftmax

### Community 139 - "Community 139"
Cohesion: 0.08
Nodes (29): array_size(), backend_for_each_domain(), backend_for_each_domain_string(), backend_validate_ua_domain(), call(), canonicalize_args(), canonicalize_kwargs(), clear() (+21 more)

### Community 140 - "Community 140"
Cohesion: 0.13
Nodes (43): algdiv(), alngam(), alnrel(), apser(), basym(), bcorr(), betaln(), bfrac() (+35 more)

### Community 142 - "Community 142"
Cohesion: 0.06
Nodes (13): data_file(), f1(), makepairs(), norm2(), Derivatives of sin->cos->-sin->-cos., Helper function to create an array of pairs of x and y., Smoke tests (with a few asserts) for fitpack routines -- mostly     check that t, test_gh_1766() (+5 more)

### Community 143 - "Community 143"
Cohesion: 0.06
Nodes (21): test_roots_chebyc(), test_roots_chebys(), test_roots_chebyt(), test_roots_chebyu(), test_roots_hermite(), test_roots_hermitenorm(), test_roots_laguerre(), test_roots_legendre() (+13 more)

### Community 144 - "Community 144"
Cohesion: 0.09
Nodes (4): Verify the factor of ``sum(abs(window)**2)*fs / abs(sum(window))**2``         us, TestCSD, TestPeriodogram, TestWelch

### Community 145 - "Community 145"
Cohesion: 0.08
Nodes (39): align_vectors(), _align_vectors_fixed(), apply(), approx_equal(), as_davenport(), as_euler(), as_quat(), as_rotvec() (+31 more)

### Community 146 - "Community 146"
Cohesion: 0.06
Nodes (22): AlphaPineneDirect, ChebyshevQuadrature, CoatingThickness, EnzymeReaction, ExponentialFitting, extract_lsq_problems(), GaussianFitting, LSQBenchmarkProblem (+14 more)

### Community 147 - "Community 147"
Cohesion: 0.06
Nodes (29): LatinHypercube, MultinomialQMC, MultivariateNormalQMC, n_primes(), PoissonDisk, primes_from_2_to(), Reset the engine to base state.          Returns         -------         engine, Fast-forward the sequence by `n` positions.          Parameters         -------- (+21 more)

### Community 148 - "Community 148"
Cohesion: 0.05
Nodes (1): BaseQRupdate

### Community 149 - "Community 149"
Cohesion: 0.08
Nodes (8): assert_quad(), get_clib_test_routine(), TestCtypesQuad, TestDblquad, TestMultivariateCtypesQuad, TestNQuad, TestQuad, TestTplquad

### Community 150 - "Community 150"
Cohesion: 0.08
Nodes (3): Unit tests for TNC optimization routine from tnc.py, TNC non-linear optimization.      These tests are taken from Prof. K. Schittkows, TestTnc

### Community 151 - "Community 151"
Cohesion: 0.06
Nodes (36): all_of_type(), clear_backends(), create_multimethod(), determine_backend(), determine_backend_multi(), Dispatchable, generate_multimethod(), get_defaults() (+28 more)

### Community 152 - "Community 152"
Cohesion: 0.08
Nodes (30): NdBSpline, Evaluate the tensor product b-spline at ``xi``.          Parameters         ----, Construct a new NdBSpline representing the partial derivative.          Paramete, Tensor product spline object.      The value at point ``xp = (x1, x2, ..., xN)``, _add_knots(), _apply_bbox_grid(), _build_design_matrices(), F (+22 more)

### Community 153 - "Community 153"
Cohesion: 0.09
Nodes (41): MikotaPair, Construct a Sakurai matrix in various formats and its eigenvalues.      Construc, Construct the Mikota pair of matrices in various formats and     eigenvalues of, Sakurai, ElasticRod(), Test functions for the sparse.linalg._eigen.lobpcg module, Check the warning of a Ritz matrix being not Hermitian     by feeding a non-Herm, Check the eigenvalue of the identity matrix is one. (+33 more)

### Community 154 - "Community 154"
Cohesion: 0.11
Nodes (31): MatFile4Writer, Class for writing matlab 4 format files, EmptyStructMarker, MatFile5Reader, MatFile5Writer, varmats_from_mat(), loadmat(), mat_reader_factory() (+23 more)

### Community 155 - "Community 155"
Cohesion: 0.06
Nodes (13): _minmax_mixin, _bsr_base, isspmatrix_bsr(), Compressed Block Sparse Row format, Check whether the array/matrix respects the BSR format.          Parameters, Block size of the matrix., Remove zero elements in-place., Eliminate duplicate array/matrix entries by adding them together.          The i (+5 more)

### Community 156 - "Community 156"
Cohesion: 0.07
Nodes (13): _data_matrix, _find_missing_index(), _minmax_mixin, Base class for sparse matrice with a .data attribute      subclasses must provid, This function performs element-wise power.          Parameters         ---------, Mixin for min and max methods.      These are not implemented for dia_matrix, he, Return the maximum of the array/matrix or maximum along an axis.          By def, Return the minimum of the array/matrix or maximum along an axis.          By def (+5 more)

### Community 157 - "Community 157"
Cohesion: 0.05
Nodes (4): JacobianHessianTest, TestDerivative, TestHessian, TestJacobian

### Community 158 - "Community 158"
Cohesion: 0.05
Nodes (40): _dispatch(), fft(), fft2(), fftn(), hfft(), hfft2(), hfftn(), ifft() (+32 more)

### Community 159 - "Community 159"
Cohesion: 0.08
Nodes (4): IndexMixin, isspmatrix_lil(), _lil_base, _prepare_index_for_memoryview()

### Community 160 - "Community 160"
Cohesion: 0.10
Nodes (27): dqagie(), dqagpe(), dqagse(), dqawce(), dqawfe(), dqawoe(), dqawse(), dqc25c() (+19 more)

### Community 161 - "Community 161"
Cohesion: 0.09
Nodes (26): approximate_taylor_polynomial(), barycentric_interpolate(), BarycentricInterpolator, _Interpolator1D, _Interpolator1DWithDerivatives, _isscalar(), krogh_interpolate(), KroghInterpolator (+18 more)

### Community 162 - "Community 162"
Cohesion: 0.07
Nodes (16): asstr(), _is_fromfile_compatible(), MMFile, mminfo(), mmread(), mmwrite(), Matrix Market I/O in Python.   See http://math.nist.gov/MatrixMarket/formats.htm, r"""     Writes the sparse or dense array `a` to Matrix Market file-like `target (+8 more)

### Community 163 - "Community 163"
Cohesion: 0.07
Nodes (29): _cdf_single_value_piecewise_post_rounding_Z0(), _cdf_single_value_piecewise_Z0(), _cdf_single_value_piecewise_Z1(), _cf(), _fitstart_S0(), _fitstart_S1(), levy_stable_frozen, levy_stable_gen (+21 more)

### Community 164 - "Community 164"
Cohesion: 0.06
Nodes (9): TestCase, TestOrthogonality, TestProjections, TestBoxBoundariesIntersections, TestBoxSphereBoundariesIntersections, TestEQPDirectFactorization, TestModifiedDogleg, TestProjectCG (+1 more)

### Community 165 - "Community 165"
Cohesion: 0.05
Nodes (36): Smoke test "array_like" inputs.  All cases here are numpy-only: a list's namespa, test_binary_fill_holes_accepts_lists(), test_binary_opening_accepts_lists(), test_black_tophat_accepts_lists(), test_convolve1d_accepts_lists(), test_correlate1d_accepts_lists(), test_distance_transform_bf_accepts_lists(), test_distance_transform_edt_accepts_lists() (+28 more)

### Community 166 - "Community 166"
Cohesion: 0.08
Nodes (18): Global optimisation tests with Sobol sampling:, Multivariate test function 1:         x[0]**2 + x[1]**2 with bounds=[(-1, 6), (-, Multivariate test function 1:          x[0]**2 + x[1]**2 with bounds=[(0, 1), (0, Multivariate test function 1:         x[0]**2 + x[1]**2 with bounds=[(None, None, Univariate test function on         f(x) = (x - 30) * sin(x) with bounds=[(0, 60, Univariate test function on         f(x) = (x - 30) * sin(x) bounds=[(0, 4.5)], NLP: Hock and Schittkowski problem 18, NLP: (High dimensional) Hock and Schittkowski 11 problem (HS11) (+10 more)

### Community 167 - "Community 167"
Cohesion: 0.06
Nodes (25): Damavandi, Deb01, Deb03, Decanomial, Deceptive, DeckkersAarts, DeflectedCorrugatedSpring, DeVilliersGlasser01 (+17 more)

### Community 168 - "Community 168"
Cohesion: 0.10
Nodes (30): qh_setaddnth(), qh_setaddsorted(), qh_setappend(), qh_setappend2ndlast(), qh_setappend_set(), qh_setcheck(), qh_setcompact(), qh_setcopy() (+22 more)

### Community 169 - "Community 169"
Cohesion: 0.06
Nodes (35): bode(), Bunch, dbode(), dfreqresp(), freqresp(), _KNV0(), _KNV0_loop(), _order_complex_poles() (+27 more)

### Community 170 - "Community 170"
Cohesion: 0.05
Nodes (40): _assert_same_result(), test_affine_transform_accepts_lists(), test_binary_closing_accepts_lists(), test_binary_dilation_accepts_lists(), test_binary_erosion_accepts_lists(), test_binary_hit_or_miss_accepts_lists(), test_binary_propagation_accepts_lists(), test_center_of_mass_accepts_lists() (+32 more)

### Community 171 - "Community 171"
Cohesion: 0.05
Nodes (19): Module to read ARFF files ========================= ARFF is the standard data fo, ========================================= Clustering package (:mod:`scipy.cluste, r""" ================================== Constants (:mod:`scipy.constants`) =====, r""" Compressed sparse graph routines (:mod:`scipy.sparse.csgraph`) ============, ================================ Datasets (:mod:`scipy.datasets`) ==============, ============================================================== Finite Difference, Linear Solvers ==============  The default solver is SuperLU (included in the sc, FFT backend using pyduccfft (+11 more)

### Community 172 - "Community 172"
Cohesion: 0.08
Nodes (11): contdist1, contdist2, contdist3, contdist4, contdist5, DiscreteAliasUrn, DiscreteGuideTable, NumericalInverseHermite (+3 more)

### Community 173 - "Community 173"
Cohesion: 0.05
Nodes (3): Test of 1D aspects of sparse array classes, test common functionality shared by 1D sparse formats, TestCommon1D

### Community 174 - "Community 174"
Cohesion: 0.05
Nodes (10): _count_nonzero(), Some tests for filters, Regression test for #1311., Regression test for gh-822., Regression test for #413: median_filter does not handle bytes orders., test_bad_convolve_and_correlate_origins(), test_byte_order_median(), test_gaussian_truncate() (+2 more)

### Community 175 - "Community 175"
Cohesion: 0.06
Nodes (14): CommonTrapezoidSimpsonTests, cumulative_simpson_nd_reference(), If initial is not None or 0, a ValueError is raised., `cumulative_simpson` and `simpson` can be tested against other to verify, Theoretically, the output of `cumulative_simpson` will be identical         to `, Test the first few degrees, for evenly spaced points., Test newton_cotes with points that are not evenly spaced., TestCumulative_trapezoid (+6 more)

### Community 176 - "Community 176"
Cohesion: 0.05
Nodes (2): Test SLSQP algorithm using Example 14.4 from Numerical Methods for     Engineers, TestSLSQP

### Community 177 - "Community 177"
Cohesion: 0.08
Nodes (26): dict, argsort_which(), assert_allclose_cc(), DictWithRepr, eval_evec(), generate_matrix(), generate_matrix_symmetric(), _get_test_tolerance() (+18 more)

### Community 178 - "Community 178"
Cohesion: 0.08
Nodes (28): call_minpack(), check_jac_sparsity(), check_tolerance(), check_x_scale(), construct_loss_function(), least_squares(), prepare_bounds(), Generic interface for least-squares minimization. (+20 more)

### Community 179 - "Community 179"
Cohesion: 0.06
Nodes (23): _dirichlet_multinomial_check_parameters(), dirichlet_multinomial_frozen, dirichlet_multinomial_gen, multinomial_frozen, multivariate_hypergeom_frozen, Mean of the Dirichlet distribution.          Parameters         ----------, Mean of the Wishart distribution.          Parameters         ----------, Mean of the inverse Wishart distribution.          Parameters         ---------- (+15 more)

### Community 180 - "Community 180"
Cohesion: 0.06
Nodes (29): _lnB(), Computes the differential entropy of the multivariate normal.          Returns, Log of the matrix normal probability density function.          Parameters, Log of the matrix t probability density function.          Parameters         --, r"""Internal helper function to compute the log of the useful quotient.      .., Log of the Dirichlet probability density function.          Parameters         -, Differential entropy of the Dirichlet distribution.          Parameters, Log of the Wishart probability density function.          Parameters         --- (+21 more)

### Community 181 - "Community 181"
Cohesion: 0.07
Nodes (34): check_random_state(), discrepancy(), _ensure_in_unit_hypercube(), geometric_discrepancy(), _l1_norm(), _lloyd_centroidal_voronoi_tessellation(), _lloyd_iteration(), _perturb_discrepancy() (+26 more)

### Community 182 - "Community 182"
Cohesion: 0.07
Nodes (2): assert_unitary(), BaseQRdelete

### Community 183 - "Community 183"
Cohesion: 0.05
Nodes (1): # TODO: Add a test for ONB?

### Community 184 - "Community 184"
Cohesion: 0.10
Nodes (24): Attribute, csv_sniffer_has_bug_last_field(), DateAttribute, NominalAttribute, NumericAttribute, Given a string containing a nominal type, returns a tuple of the         possibl, Parse a value of this type.          Parameters         ----------         data_, # TODO: (+16 more)

### Community 185 - "Community 185"
Cohesion: 0.08
Nodes (10): CubatureOscillatory, CubatureSphere, CumulativeSimpson, from_cython(), LowLevelCallable(), NquadOscillatory, NquadSphere, Quad (+2 more)

### Community 186 - "Community 186"
Cohesion: 0.09
Nodes (30): DCSRCH, dcstep(), Parameters     ----------     phi : callable phi(alpha)         Function at poin, Parameters         ----------         alpha1 : float             alpha1 is the c, Parameters         ----------         stp : float             The current estima, Subroutine dcstep      This subroutine computes a safeguarded step for a search, _check_c1_c2(), _cubicmin() (+22 more)

### Community 187 - "Community 187"
Cohesion: 0.06
Nodes (17): gaussian_kde, _get_output_dtype(), Evaluate the estimated pdf on a set of points.          Parameters         -----, Multiply estimated density by a multivariate Gaussian and integrate         over, Computes the integral of a 1D pdf between two bounds.          Parameters, Computes the integral of a pdf over a rectangular interval.          Parameters, Representation of a kernel-density estimate using Gaussian kernels.      Kernel, Computes the integral of the product of this  kernel density estimate         wi (+9 more)

### Community 188 - "Community 188"
Cohesion: 0.05
Nodes (1): TestConstructUtils

### Community 189 - "Community 189"
Cohesion: 0.06
Nodes (12): _chk_asarrays(), _chk_weights(), _freq_weights(), _is_32bit(), metric(), # NOTE: Extra args should be checked with a dedicated test, runs fn on its arguments 2 or 3 ways, checks that the results are the same,, # NOTE: The correctness should be checked within each metric tests. (+4 more)

### Community 190 - "Community 190"
Cohesion: 0.06
Nodes (2): _sample_orthonormal_matrix(), TestMultivariateNormal

### Community 191 - "Community 191"
Cohesion: 0.10
Nodes (14): direct_diff(), direct_hilbert(), direct_ihilbert(), direct_itilbert(), direct_shift(), direct_tilbert(), Check input overwrite behavior, TestDiff (+6 more)

### Community 192 - "Community 192"
Cohesion: 0.05
Nodes (3): TestKMeans, TestVq, TestWhiten

### Community 193 - "Community 193"
Cohesion: 0.10
Nodes (17): Fft, FftBackends, Fftn, FftnBackends, FftThreading, get_module(), NextFastLen, PyfftwBackend (+9 more)

### Community 194 - "Community 194"
Cohesion: 0.13
Nodes (6): netcdf_file, Initialize netcdf_file from fileobj (str or file-like)., Closes the NetCDF file., Adds a dimension to the Dimension section of the NetCDF data structure., Perform a sync-to-disk flush if the `netcdf_file` object is in write mode., A file object for NetCDF data.      A `netcdf_file` object has two standard attr

### Community 195 - "Community 195"
Cohesion: 0.10
Nodes (12): dedent_lines(), ObjDoc, Remove leading and trailing blank lines from a list of lines, # NOTE: param line with single element should never have a, A line-based string reader., Parameters         ----------         data : str            String with lines se, func_name : Descriptive text             continued text         another_func_nam, .. index:: default            :refguide: something, else, and more (+4 more)

### Community 196 - "Community 196"
Cohesion: 0.07
Nodes (24): _eigvalsh_to_eps(), multivariate_normal_gen, ortho_group_gen, Infer dimensionality from mean or covariance matrices. Handle         defaults., r"""     A multivariate normal random variable.      The `mean` keyword specifie, Returns: n_, p_, npcond.          n_ and p_ are arrays of the correct shape; npc, r"""     A Special Orthogonal matrix (SO(N)) random variable.      Return a rand, Dimension N must be specified; it cannot be inferred. (+16 more)

### Community 197 - "Community 197"
Cohesion: 0.08
Nodes (20): invwishart_frozen, invwishart_gen, r"""     A Wishart random variable.      The `df` keyword specifies the degrees, Wishart probability density function.          Parameters         ----------, Mode of the Wishart distribution.          Parameters         ----------, Mode of the Wishart distribution          Only valid if the degrees of freedom a, Variance of the Wishart distribution.          Parameters         ----------, Parameters         ----------         n : int             Number of variates to (+12 more)

### Community 198 - "Community 198"
Cohesion: 0.08
Nodes (4): fft1(), get_expected_input_dtype(), TestFFT, TestFFTThreadSafe

### Community 199 - "Community 199"
Cohesion: 0.07
Nodes (7): Regression test for ticket 1441., TestFreqs, TestFreqs_zpk, TestFreqz, TestFreqz_sos, TestFreqz_zpk, TestGroupDelay

### Community 200 - "Community 200"
Cohesion: 0.06
Nodes (5): graphs(), matrices(), same_matrix(), sp_sparse_cls(), sparse_cls()

### Community 201 - "Community 201"
Cohesion: 0.06
Nodes (14): dct_2d_ref(), dst_2d_ref(), idct_2d_ref(), idst_2d_ref(), is_longdouble_binary_compatible(), Calculate reference values for testing dct2., Calculate reference values for testing idct2., Calculate reference values for testing dst2. (+6 more)

### Community 202 - "Community 202"
Cohesion: 0.06
Nodes (18): Rotation in 3 dimensions.      This class provides an interface to initialize fr, Represent as rotation matrix.          3D rotations can be represented using rot, Represent as Euler angles.          Any orientation can be expressed as a compos, Represent as Davenport angles.          Any orientation can be expressed as a co, Represent as Modified Rodrigues Parameters (MRPs).          MRPs are a 3 dimensi, Compose this rotation with itself `n` times.          Composition of a rotation, Get the magnitude(s) of the rotation(s).          Returns         -------, Get the mean of the rotations.          The mean used is the chordal L2 mean (al (+10 more)

### Community 203 - "Community 203"
Cohesion: 0.11
Nodes (20): CanonicalConstraint, initial_constraints_as_canonical(), Convert initial values of the constraints to the canonical format.      The purp, Create an instance from `PreparedConstrained` object., Canonical constraint to use with trust-constr algorithm.      It represents the, Create an "empty" instance.          This "empty" instance is required to allow, Concatenate multiple `CanonicalConstraint` into one.          `sparse_jacobian`, HessianLinearOperator (+12 more)

### Community 204 - "Community 204"
Cohesion: 0.06
Nodes (23): ClusterWarning, is_isomorphic(), leaders(), maxdists(), maxRstat(), Set list of matplotlib color codes for use by dendrogram.      Note that this pa, Determine if two different cluster assignments are equivalent.      Parameters, Return the maximum distance between any non-singleton cluster.      Parameters (+15 more)

### Community 205 - "Community 205"
Cohesion: 0.11
Nodes (33): _as_float_array(), _augknt(), _convert_string_aliases(), _diff_dual_poly(), _dual_poly(), fpcheck(), _get_dtype(), _handle_lhs_derivatives() (+25 more)

### Community 206 - "Community 206"
Cohesion: 0.17
Nodes (29): OdeSolver, Base class for ODE solvers.      In order to implement a new solver you need to, BDF, Implicit method based on backward-differentiation formulas.      This is a varia, OdeSolution, Continuous ODE solution.      It is organized as a collection of `DenseOutput` o, Suite of ODE solvers implemented in Python., find_active_events() (+21 more)

### Community 207 - "Community 207"
Cohesion: 0.06
Nodes (32): block_diag(), circulant(), companion(), convolution_matrix(), dft(), fiedler(), fiedler_companion(), hadamard() (+24 more)

### Community 208 - "Community 208"
Cohesion: 0.08
Nodes (15): NA_NewArray(), NI_ObjectToInputArray(), NI_ObjectToInputOutputArray(), NI_ObjectToOptionalInputArray(), NI_ObjectToOptionalOutputArray(), NI_ObjectToOutputArray(), Py_BinaryErosion(), Py_BinaryErosion2() (+7 more)

### Community 209 - "Community 209"
Cohesion: 0.09
Nodes (16): multivariate_normal_frozen, MVNProblem, Test that sample mean consistent with known mean., Regression test for gh-8844., Instantiate a multivariate normal integration problem with special structure., Random lambdas, random upper bounds, infinite lower bounds., Constant off-diagonal covariance, random upper bounds, infinite lower bounds., Off-diagonal covariance of 0.5, negative orthant bounds.          True analytica (+8 more)

### Community 210 - "Community 210"
Cohesion: 0.06
Nodes (3): BatchFloaterHormann, TestAAA, TestFloaterHormann

### Community 211 - "Community 211"
Cohesion: 0.07
Nodes (3): assert_really_equal(), Sharper assertion function that is stricter about matching types, not just value, TestFactorialFunctions

### Community 212 - "Community 212"
Cohesion: 0.06
Nodes (3): TestSolveBanded, TestSolveCirculant, TestSolveHBanded

### Community 213 - "Community 213"
Cohesion: 0.06
Nodes (30): Test fitting just the shape parameter (df) of chi2 to mixed data.      Calculati, For the exponential distribution with loc=0, the exact solution for     fitting, Test fitting beta shape parameters to interval-censored data.      Calculation i, Fit gamma shape and scale to data with one right-censored value.      Calculatio, Fit gumbel_l and gumbel_r to censored data.      This R calculation should match, Fit just the shape parameter of invgauss to data with one value     left-censore, Fit invweibull to censored data.      Here is the calculation in R.  The 'freche, Fir the Laplace distribution to left- and right-censored data.      Calculation (+22 more)

### Community 214 - "Community 214"
Cohesion: 0.08
Nodes (6): TestEigVals, TestHessenberg, TestRQ, TestSVD_GESDD, TestSVD_GESVD, TestSVDVals

### Community 215 - "Community 215"
Cohesion: 0.07
Nodes (10): _assert_n_smooth(), Includes test functions for fftpack.helper module  Copied from fftpack.helper by, Test 2D input, which has uneven dimension sizes, Test_init_nd_shape_and_axes, test_next_fast_len(), TestFFTFreq, TestFFTShift, TestNextFastLen (+2 more)

### Community 216 - "Community 216"
Cohesion: 0.14
Nodes (28): datafile(), Nonseekable, test_12_bit_even_size(), test_20_bit_extra_data(), test_24_bit_odd_size_with_pad(), test_36_bit_odd_size(), test_45_bit_even_size(), test_53_bit_odd_size() (+20 more)

### Community 217 - "Community 217"
Cohesion: 0.08
Nodes (22): _apply_field(), _fmm_version(), _FMMThreadPoolCtlController, _get_read_cursor(), _get_write_cursor(), mminfo(), mmread(), mmwrite() (+14 more)

### Community 218 - "Community 218"
Cohesion: 0.09
Nodes (33): _arg_peaks_as_expected(), _arg_wlen_as_expected(), _arg_x_as_expected(), argrelextrema(), argrelmax(), argrelmin(), _boolrelextrema(), _filter_ridge_lines() (+25 more)

### Community 219 - "Community 219"
Cohesion: 0.11
Nodes (20): Covariance, CovViaCholesky, CovViaDiagonal, CovViaEigendecomposition, CovViaPrecision, CovViaPSD, _dot_diag(), Representation of a covariance matrix.      Calculations involving covariance ma (+12 more)

### Community 220 - "Community 220"
Cohesion: 0.07
Nodes (5): _distr2_gen, _distr6_gen, _distr_gen, TestSubclassingExplicitShapes, TestSubclassingNoShapes

### Community 222 - "Community 222"
Cohesion: 0.06
Nodes (1): TestDualAnnealing

### Community 223 - "Community 223"
Cohesion: 0.07
Nodes (2): test_complex(), TestInterp1D

### Community 224 - "Community 224"
Cohesion: 0.06
Nodes (1): TestAffineTransform

### Community 225 - "Community 225"
Cohesion: 0.06
Nodes (1): TestCurveFit

### Community 226 - "Community 226"
Cohesion: 0.07
Nodes (5): Verify all exceptions are raised., TestAllFreqConvolves, TestConvolve, TestConvolve2d, TestCorrelate

### Community 227 - "Community 227"
Cohesion: 0.07
Nodes (15): netcdf_variable, NetCDF reader/writer module.  This module is used to read and create NetCDF file, The default encoded fill-value for this Variable's data type., Returns the encoded fill value for this variable as bytes.          This is take, Returns the value denoting "no data" for this variable.          If this variabl, Applies the given missing value to the data array.          Returns a numpy.ma a, # TODO:, Create an empty variable for the `netcdf_file` object, specifying its data (+7 more)

### Community 228 - "Community 228"
Cohesion: 0.09
Nodes (20): qh_countfacets(), qh_detvnorm(), qh_eachvoronoi(), qh_eachvoronoi_all(), qh_facetvertices(), qh_markkeep(), qh_markvoronoi(), qh_order_vertexneighbors() (+12 more)

### Community 229 - "Community 229"
Cohesion: 0.13
Nodes (19): Halton, QMCEngine, Halton sequence.      Pseudo-random number generator that generalize the Van der, A generic Quasi-Monte Carlo sampler class meant for subclassing.      QMCEngine, CustomDistPINV, FastGeneratorInversion, ====================================================== Random Number Generators, Support of the distribution.          Returns         -------         a, b : flo (+11 more)

### Community 230 - "Community 230"
Cohesion: 0.10
Nodes (4): NdBSpline0, TestMakeSplprep, TestMakeSplprepPeriodic, TestNdBSpline

### Community 231 - "Community 231"
Cohesion: 0.06
Nodes (4): check_remains_sorted(), Checks that sorted indices property is retained through an operation, TestGetSet1D, TestSlicingAndFancy1D

### Community 232 - "Community 232"
Cohesion: 0.10
Nodes (25): assert_mask_matches(), check_simple(), in_tempdir(), make_simple(), Create, return, and change directory to a temporary directory      Examples, Example fileobj tests, Asserts that the mask of arr is effectively the same as expected_mask.      In c, test_append_recordDimension() (+17 more)

### Community 233 - "Community 233"
Cohesion: 0.09
Nodes (9): _generate_cube(), _generate_dodecahedron(), _generate_icosahedron(), _generate_octahedron(), _generate_polytope(), _generate_tetrahedron(), _hypersphere_area(), _sample_sphere() (+1 more)

### Community 234 - "Community 234"
Cohesion: 0.08
Nodes (4): Some tests to show that fisher_exact() works correctly.      Note that in SciPy, TestCombinePvalues, TestFisherExact, TestPercentileOfScore

### Community 235 - "Community 235"
Cohesion: 0.08
Nodes (9): _data_matrix, _dia_base, _invert_index(), isspmatrix_dia(), Sparse DIAgonal format, Returns a mask of the same shape as self.data, where         mask[i,j] is True w, Returns a matrix with the same sparsity structure as self,         but with diff, Helper function to invert an index array. (+1 more)

### Community 236 - "Community 236"
Cohesion: 0.08
Nodes (20): Rana, Rastrigin, r"""     Ratkowsky02 objective function.      This class defines the Ratkowsky 2, r"""     Ripple 1 objective function.      This class defines the Ripple 1 [1]_, r"""     Ripple 25 objective function.      This class defines the Ripple 25 [1], r"""     Rosenbrock objective function.      This class defines the Rosenbrock [, r"""     Modified Rosenbrock objective function.      This class defines the Mod, r"""     Rotated Ellipse 1 objective function.      This class defines the Rotat (+12 more)

### Community 237 - "Community 237"
Cohesion: 0.09
Nodes (15): blend(), eq(), ge(), gt(), le(), lt(), mask_all(), mask_any() (+7 more)

### Community 238 - "Community 238"
Cohesion: 0.09
Nodes (14): _BSpline, _get_xp_bspline_cls(), Evaluate a spline function.          Parameters         ----------         x : a, Return a B-spline representing the derivative.          Parameters         -----, Return a B-spline representing the antiderivative.          Parameters         -, Compute a definite integral of the spline.          Parameters         ---------, Insert a new knot at `x` of multiplicity `m`.          Given the knots and coeff, NumPy Backend for BSpline.      The public BSpline class below is set up to dele (+6 more)

### Community 239 - "Community 239"
Cohesion: 0.06
Nodes (8): _csr_base, isspmatrix_csr(), Compressed Sparse Row matrix format, swap the members of x if this is a column-oriented matrix, Returns a copy of row i of the matrix, as a (1 x n)         CSR matrix (row vect, Returns a copy of column i. A (m x 1) sparse array (column vector)., # TODO: uncomment this once it's faster:, Is `x` of csr_matrix type?      .. warning::         SciPy sparse is shifting fr

### Community 240 - "Community 240"
Cohesion: 0.10
Nodes (6): BaseTestCOO, Ensure has_sorted_indices memoizes sorted state for sort_indices, Ensure has_canonical_format memoizes state for sum_duplicates, Replace D with a non-canonical equivalent: containing         duplicate elements, TestCSC, TestCSR

### Community 241 - "Community 241"
Cohesion: 0.08
Nodes (8): Test private conversions between 'z' and 'z**-1' polynomials., Test_bode, Test_dfreqresp, TestDLTI, TestStateSpaceDisc, TestTransferFunction, TestTransferFunctionZConversion, TestZerosPolesGain

### Community 242 - "Community 242"
Cohesion: 0.07
Nodes (2): TestMannWhitneyU, TestPoissonMeansTest

### Community 243 - "Community 243"
Cohesion: 0.09
Nodes (4): Check that the eval_* functions sig='ld->d' and 'dd->d' agree., Check that the eval_* functions agree with the constructed polynomials, TestPolys, TestRecurrence

### Community 244 - "Community 244"
Cohesion: 0.08
Nodes (9): Unit test for Linear Programming via Simplex Algorithm., Checks whether a matrix contains only independent rows of another, # TODO: add tests for:, redundancy_removed(), RRCommonTests, TestRRID, TestRRPivotDense, TestRRPivotSparse (+1 more)

### Community 245 - "Community 245"
Cohesion: 0.06
Nodes (2): Test two failures from gh-20904: int32 and indices-as-None., test_20904()

### Community 246 - "Community 246"
Cohesion: 0.07
Nodes (6): Tests kstest and ks_samp 1-samples with K-S various sizes, alternatives, modes., Tests 2-samples with K-S various sizes, alternatives, modes., Checks that all of the warnings from a list returned by         `warnings.catch_, Ensure gh-12218 is fixed., TestKSOneSample, TestKSTwoSamples

### Community 247 - "Community 247"
Cohesion: 0.08
Nodes (9): CalculateWindowedFFT, Convolve, Convolve2D, FFTConvolve, FIRLS, LTI, Resample, Upfirdn1D (+1 more)

### Community 248 - "Community 248"
Cohesion: 0.09
Nodes (16): build_noncritical(), cfmav(), contiguous(), data(), extend_and_broadcast(), idx(), mavref(), multiprep() (+8 more)

### Community 249 - "Community 249"
Cohesion: 0.09
Nodes (30): BVPResult, collocation_fun(), compute_jac_indices(), construct_global_jac(), create_spline(), estimate_bc_jac(), estimate_fun_jac(), estimate_rms_residuals() (+22 more)

### Community 250 - "Community 250"
Cohesion: 0.09
Nodes (30): _coeff_smooth(), collapse_2d(), compute_root_from_lambda(), cspline1d(), cspline1d_eval(), cspline2d(), _cubic(), _cubic_coeff() (+22 more)

### Community 251 - "Community 251"
Cohesion: 0.07
Nodes (4): ifill(), ilu_set_default_options(), set_default_options(), super_stats()

### Community 252 - "Community 252"
Cohesion: 0.08
Nodes (3): make_interp_full_matr(), Assemble a spline order k with knots t to interpolate     y(x) using full matric, TestInterp

### Community 253 - "Community 253"
Cohesion: 0.07
Nodes (4): TestArgus, TestFrozen, TestGenpareto, TestHalfgennorm

### Community 254 - "Community 254"
Cohesion: 0.07
Nodes (6): TestCauchy, TestGeom, TestGumbelL, TestInvgauss, TestKSTwo, TestStudentT

### Community 255 - "Community 255"
Cohesion: 0.13
Nodes (27): _assert_success(), Case, IterativeParams, Test functions for the sparse.linalg._isolve module, Fixture for all cases in IterativeParams, # NOTE: the following was previously uncommented as dead code --, # TODO: minres / tfqmr. It didn't historically use absolute tolerances, so, Fixture for all solvers in scipy.sparse.linalg._isolve (+19 more)

### Community 256 - "Community 256"
Cohesion: 0.07
Nodes (8): _kde_subclass1, _kde_subclass2, _kde_subclass4, Ugly, but people may rely on this.  See scipy pull request 123,     specifically, Regression test for #1181., test_gaussian_kde_monkeypatch(), test_gaussian_kde_subclassing(), test_kde_integer_input()

### Community 257 - "Community 257"
Cohesion: 0.07
Nodes (6): _mpmath_wrightomega(), test_beta(), test_erf_complex(), test_wrightomega_branch(), test_wrightomega_region1(), test_wrightomega_region2()

### Community 258 - "Community 258"
Cohesion: 0.12
Nodes (7): l2_norm(), QMCEngineTests, Generic tests for QMC engines., test_deterministic(), TestHalton, TestLHS, TestPoisson

### Community 259 - "Community 259"
Cohesion: 0.09
Nodes (17): _promote(), Apply this rotation to a set of vectors.          If the original frame rotates, Compose this rotation with the other.          If `p` and `q` are two rotations,, Determine if another rotation is approximately equal to this one.          Equal, # TODO: We defer the implementation of groups for arbitrary Array API frameworks, # TODO: This special case handling is mainly a result of Array API limitations., # TODO: We should move to one single way of specifying the output shape and, Estimate a rotation to optimally align two sets of vectors.          Find a rota (+9 more)

### Community 260 - "Community 260"
Cohesion: 0.12
Nodes (14): BarrierSubproblem, Trust-region interior point method.  References ---------- .. [1] Byrd, Richard, Returns scaling vector.         Given by:             scaling = [ones(n_vars), s, Returns scaled gradient.          Return scaled gradient:             gradient =, Assemble sparse Jacobian given its components.          Given ``J_eq``, ``J_ineq, Returns Lagrangian Hessian (in relation to `x`) -> Hx, Returns scaled Lagrangian Hessian (in relation to`s`) -> S Hs S, Barrier optimization problem:         minimize fun(x) - barrier_parameter*sum(lo (+6 more)

### Community 261 - "Community 261"
Cohesion: 0.12
Nodes (28): get_arrays_tol(), hypot(), inprod(), inv(), isinv(), isminor(), isorth(), istril() (+20 more)

### Community 262 - "Community 262"
Cohesion: 0.09
Nodes (29): check_COLA(), check_NOLA(), coherence(), csd(), _fft_helper(), istft(), lombscargle(), _median_bias() (+21 more)

### Community 263 - "Community 263"
Cohesion: 0.08
Nodes (15): dunnett(), DunnettResult, _iv_dunnett(), _params_dunnett(), _pvalue_dunnett(), Compute the confidence interval for the specified confidence level.          Par, Dunnett's test: multiple comparisons of means against a control group.      This, Result object returned by `scipy.stats.dunnett`.      Attributes     ---------- (+7 more)

### Community 264 - "Community 264"
Cohesion: 0.09
Nodes (5): direct_lstsq(), _eps_cast(), Get the epsilon for dtype, possibly downcast to BLAS types., TestDet, TestLstsq

### Community 265 - "Community 265"
Cohesion: 0.10
Nodes (2): TestBarycentric, TestKrogh

### Community 266 - "Community 266"
Cohesion: 0.07
Nodes (1): TestTanhSinh

### Community 267 - "Community 267"
Cohesion: 0.17
Nodes (29): addConstraint(), coercex(), daxpy1(), dcopy1(), ddot1(), diagonalScaling(), dneg1(), dnrm21() (+21 more)

### Community 268 - "Community 268"
Cohesion: 0.09
Nodes (18): r"""     Trefethen objective function.      This class defines the Trefethen [1], r"""     Three Hump Camel objective function.      This class defines the Three, r"""     Trid objective function.      This class defines the Trid [1]_ global o, r"""     Trigonometric 1 objective function.      This class defines the Trigono, r"""     Trigonometric 2 objective function.      This class defines the Trigono, r"""     Tripod objective function.      This class defines the Tripod [1]_ glob, r"""     Thurber [1]_ objective function.      .. [1] https://www.itl.nist.gov/d, r"""     TestTubeHolder objective function.      This class defines the TestTube (+10 more)

### Community 269 - "Community 269"
Cohesion: 0.16
Nodes (20): ExpFormat, IntFormat, _expect_int(), hb_read(), hb_write(), HBInfo, HBMatrixType, LineOverflow (+12 more)

### Community 270 - "Community 270"
Cohesion: 0.10
Nodes (26): cdf2rdf(), _check_format_errors_warnings(), _check_info(), _check_select(), eig(), eig_banded(), eigh(), eigh_tridiagonal() (+18 more)

### Community 271 - "Community 271"
Cohesion: 0.07
Nodes (26): _betai(), ks_1samp(), ks_2samp(), kstest(), linregress(), plotting_positions(), pointbiserialr(), An extension of scipy.stats._stats_py to support masked arrays (+18 more)

### Community 272 - "Community 272"
Cohesion: 0.09
Nodes (19): B(), bspline(), bspline2(), data_file(), _make_multiples(), _naive_B(), _naive_eval(), _naive_eval_2() (+11 more)

### Community 273 - "Community 273"
Cohesion: 0.07
Nodes (3): Vasicek results are compared with the R package vsgoftest.      # library(vsgoft, TestDifferentialEntropy, TestEntropy

### Community 274 - "Community 274"
Cohesion: 0.10
Nodes (17): # TODO: split into multiple tests, or parameterize across filter types, # TODO: Why so inaccurate?  Is reference flawed?, Test not the expected number of p/z (effectively at origin)., TestBilinear_zpk, TestFindFreqs, TestLp2bp, TestLp2bp_zpk, TestLp2bs (+9 more)

### Community 275 - "Community 275"
Cohesion: 0.09
Nodes (10): data_file(), Test that SciPy can interpolate to a regular grid from the boundary.      Based, Test that SciPy can interpolate to the edge of a triangle.      Based on gh-2283, Test that SciPy can interpolate to the input points.      Based on gh-21279., test_interp_from_boundary(), test_reproduction_NaN_on_input_points(), test_reproduction_NaN_on_points_linear_combination(), TestCloughTocher2DInterpolator (+2 more)

### Community 276 - "Community 276"
Cohesion: 0.13
Nodes (25): get_arrays(), test_combine_pvalues(), test_correlation(), test_describe(), test_directional_stats(), test_entropy(), test_goodness_of_fit(), test_k_sample_paired_tests() (+17 more)

### Community 277 - "Community 277"
Cohesion: 0.08
Nodes (2): _random_covariance(), TestMultivariateT

### Community 278 - "Community 278"
Cohesion: 0.10
Nodes (9): Check stats.rankdata with an array of length 1., Basic tests of stats.rankdata., An empty array requires no correction, should return 1.0., A single element requires no correction, should return 1.0., Arrays with no ties require no correction., Check a few basic examples of the tie correction factor., stats.rankdata of empty array should return an empty array., TestRankData (+1 more)

### Community 279 - "Community 279"
Cohesion: 0.13
Nodes (26): _TestIDCTBase, TestIDCTIDouble, TestIDCTIFloat, TestIDCTIIDouble, TestIDCTIIFloat, TestIDCTIIIDouble, TestIDCTIIIFloat, TestIDCTIIIInt (+18 more)

### Community 280 - "Community 280"
Cohesion: 0.07
Nodes (2): TestFFTConvolve, TestOAConvolve

### Community 281 - "Community 281"
Cohesion: 0.17
Nodes (1): _TestLinearFilter

### Community 282 - "Community 282"
Cohesion: 0.07
Nodes (5): Data generated in R with         > set.seed(1)         > library("onewaytests"), Data taken from 'The Modification and Evaluation of the         Alexander-Govern, Data taken from 'Robustness And Comparative Power Of WelchAspin,         Alexand, TestAlexanderGovern, TestFOneWay

### Community 283 - "Community 283"
Cohesion: 0.10
Nodes (17): ArffError, Base exception for errors when reading ARFF files.          Raised when an ARFF, FortranEOFError, FortranFile, FortranFormattingError, Module to read / write Fortran unformatted sequential files.  This is in the spi, Write a record (including sizes) to the file.          Parameters         ------, Indicates that the file ended properly.      This error descends from TypeError (+9 more)

### Community 284 - "Community 284"
Cohesion: 0.12
Nodes (11): ParseArffError, Exception for syntax and parsing errors in ARFF files.          Raised when an A, Regression test for issue #10232:      Exception in loadarff with quoted nominal, TestDateAttribute, TestHeader, TestMissingData, TestNoData, TestQuotedNominal (+3 more)

### Community 285 - "Community 285"
Cohesion: 0.18
Nodes (27): BernoulliH(), binoexpand(), CMultiWalleniusNCHypergeometric(), CWalleniusNCHypergeometric(), Erf(), FallingFactorial(), findpars(), FloorLog2() (+19 more)

### Community 286 - "Community 286"
Cohesion: 0.10
Nodes (13): cKDTree, ============================================================= Spatial algorithms, distance_matrix(), innernode, leafnode, minkowski_distance(), minkowski_distance_p(), node (+5 more)

### Community 287 - "Community 287"
Cohesion: 0.11
Nodes (27): _append_contraction_marks(), _append_contraction_marks_sub(), _append_nonsingleton_leaf_node(), _append_singleton_leaf_node(), cophenet(), dendrogram(), _dendrogram_calculate_info(), from_mlab_linkage() (+19 more)

### Community 288 - "Community 288"
Cohesion: 0.10
Nodes (20): adjust_nthreads(), available_hardware_threads(), concurrent_queue, Distribution, do_pinning(), ducc0_default_num_threads(), ducc_pseudo_thread_pool, ducc_thread_pool (+12 more)

### Community 289 - "Community 289"
Cohesion: 0.10
Nodes (27): _basic_simpson(), _cached_roots_legendre(), cumulative_simpson(), _cumulative_simpson_equal_intervals(), _cumulative_simpson_unequal_intervals(), cumulative_trapezoid(), _cumulatively_sum_simpson_integrals(), fixed_quad() (+19 more)

### Community 290 - "Community 290"
Cohesion: 0.12
Nodes (23): _ci_lower(), _ci_upper(), _conditional_oddsratio(), _conditional_oddsratio_ci(), _hypergeom_params_from_table(), _nc_hypergeom_mean_inverse(), odds_ratio(), OddsRatioResult (+15 more)

### Community 291 - "Community 291"
Cohesion: 0.10
Nodes (5): F_dense, The r.h.s. of ``f(p) = s``, an analog of _fitpack_repro.F     Uses full matrices, TestMakeSplrep, _TestMakeSplrepBase, TestMakeSplrepPeriodic

### Community 293 - "Community 293"
Cohesion: 0.11
Nodes (9): estimated_warns(), less_than_or_close(), Test functions for the sparse.linalg._expm_multiply module., If trace is estimated, it should warn.      We warn that estimation of trace mig, Make sure `expm_multiply` handles all numerical dtypes correctly., These tests do not consider the case of multiple time steps in one call., test_expm_multiply_dtype(), TestExpmActionInterval (+1 more)

### Community 294 - "Community 294"
Cohesion: 0.07
Nodes (14): mp_hyp2f1(), 0.9 <= |z| <= 1 and |1 - z| < 0.9., 0.9 <= |z| <= 1 and |1 - z| >= 1.          This region is unhandled by of the st, 1 < |z| < 1.1 and |1 - z| >= 0.9 and real(z) >= 0, |z| > 1 but not in region 5., Return mpmath hyp2f1 calculated on same branch as scipy hyp2f1.      For most va, Test that expected values match what is computed by mpmath.          This gather, Get pytest.mark parameters for a test in this class. (+6 more)

### Community 295 - "Community 295"
Cohesion: 0.11
Nodes (9): estimated_cdf_reference(), estimated_cdf_reference_last_axis(), np_searchsorted(), quantile_reference(), quantile_reference_last_axis(), Test_XPSearchsorted, TestEstimatedCDF, TestQuantile (+1 more)

### Community 296 - "Community 296"
Cohesion: 0.10
Nodes (19): _calculate_rmsd(), _generate_icosahedron(), _generate_octahedron(), _generate_prism(), _generate_pyramid(), _generate_tetrahedron(), Test that the tetrahedral group correctly fixes the rotations of a     tetrahedr, Test that the dicyclic group correctly fixes the rotations of a     prism. (+11 more)

### Community 297 - "Community 297"
Cohesion: 0.08
Nodes (14): check_filtfilt_gust(), filtfilt_gust_opt(), gen_oa_shapes(), gen_oa_shapes_2d(), An alternative implementation of filtfilt with Gustafsson edges.      This funct, # NOTE: This was changed (rel. to TestLinear...) to add a pole @zero:, test_filtfilt_gust(), TestCorrelate2d (+6 more)

### Community 298 - "Community 298"
Cohesion: 0.09
Nodes (1): TestTransitionToRNG

### Community 299 - "Community 299"
Cohesion: 0.07
Nodes (24): Efficiently solve WH of order 2 according to Weinert.      Needs order = 2 and n, Test that _polynomial_fit works as expected., Test that whittaker raises errors., Test that whittaker works on a few data points., Test equivalent results, Test whittaker for penalty lamb close to zero., Test whittaker for penalty lamb close to infinity., Test whittaker for lamb=0. (+16 more)

### Community 300 - "Community 300"
Cohesion: 0.12
Nodes (19): Verify basic parametrizations., TestBartHann, TestBartlett, TestBlackman, TestBlackmanHarris, TestBohman, TestBoxcar, TestFlatTop (+11 more)

### Community 301 - "Community 301"
Cohesion: 0.14
Nodes (21): IntEnum, _array_tofile(), _handle_pad_byte(), _raise_bad_format(), Module to read / write wav files using NumPy arrays  Functions --------- `read`:, Warning for WAV files with format issues that can still be read.          Raised, Returns     -------     size : int         size of format subchunk in bytes (min, Tracks stream position, provides tell(), and emulates only those     seeks that (+13 more)

### Community 302 - "Community 302"
Cohesion: 0.08
Nodes (19): arr_dtype_number(), arr_to_chars(), convert_dtypes(), _get_matfile_version(), matdims(), matfile_version(), MatVarReader, Convert dtypes in mapping to given order      Parameters     ----------     dtyp (+11 more)

### Community 303 - "Community 303"
Cohesion: 0.12
Nodes (17): create_header(), get_header_field(), get_header_format(), get_header_object(), get_header_symmetry(), header_repr(), header_to_dict(), open_read_file() (+9 more)

### Community 304 - "Community 304"
Cohesion: 0.09
Nodes (10): loop_pos, looper, Helper for looping over sequences, particular in templates.  Often in a loop in, Returns true if this item is the start of a new group,         where groups mean, Returns true if this item is the end of a new group,         where groups mean t, Helper for looping (particularly in templates)      Use this like::          for, A small templating language  This implements a small templating language.  This, Lex a string into chunks:          >>> lex('hey')         ['hey']         >>> le (+2 more)

### Community 305 - "Community 305"
Cohesion: 0.10
Nodes (5): convert_to_ndbspline(), _numdiff_2d(), Create an array of (xi, yi) pairs for all xi in x and yi in y,         and resha, TestRectBivariateSpline, TestRectSphereBivariateSpline

### Community 306 - "Community 306"
Cohesion: 0.08
Nodes (3): TestNormalInverseGamma, TestUniformDirection, TestVonMises_Fisher

### Community 307 - "Community 307"
Cohesion: 0.09
Nodes (2): TestMultinomial, TestMultivariateHypergeom

### Community 308 - "Community 308"
Cohesion: 0.09
Nodes (8): Test that _cdf_distance() (via wasserstein_distance()) raises ValueErrors     fo, Tests for wasserstein_distance_nd() output values., Tests for wasserstein_distance() output values., Tests for energy_distance() output values., TestCdfDistanceValidation, TestEnergyDistance, TestWassersteinDistance, TestWassersteinDistanceND

### Community 309 - "Community 309"
Cohesion: 0.08
Nodes (5): test__workers_wrapper(), TestContainsNaN, TestRenameParameter, TestValidateInt, user_of_workers()

### Community 310 - "Community 310"
Cohesion: 0.13
Nodes (24): add_knot(), Bunch, disc(), fprati(), generate_knots(), _generate_knots_impl(), _get_residuals(), make_splprep() (+16 more)

### Community 311 - "Community 311"
Cohesion: 0.08
Nodes (18): _BivariateSplineBase, _DerivedBivariateSpline, Base class for Bivariate spline s(x,y) interpolation on the rectangle     [xb,xe, Construct a spline object from given tck and degree, Return weighted sum of squared residuals of the spline approximation.          T, Return a tuple (tx,ty) where tx,ty contain knots positions         of the spline, Return spline coefficients.          Returns         -------         1D array, Evaluate the spline or its derivatives at given positions.          Parameters (+10 more)

### Community 312 - "Community 312"
Cohesion: 0.11
Nodes (20): _calc_b(), _calc_e(), _curfit(), fitpack --- curve and surface fitting with splines  fitpack is based on a collec, Wrapper for surfit with iopt=0 (smoothing spline).     Returns: nx, tx, ny, ty,, Wrapper for surfit with iopt=-1 (least squares fit with fixed knots).     Return, Wrapper for regrid with iopt=0 (smoothing spline on rectangular grid).     Retur, Wrapper for sphere with iopt=0 (smoothing spline on sphere).     Returns: nt, tt (+12 more)

### Community 313 - "Community 313"
Cohesion: 0.10
Nodes (13): interp1d, Interpolate a 1-D function (legacy).      .. legacy:: class          For a guide, Find nearest neighbor interpolated y_new = f(x_new)., Use previous/next neighbor of x_new, y_new = f(x_new)., Check the inputs for being in the bounds of the interpolated data.          Para, griddata(), NearestNDInterpolator, Convenience interface to N-D interpolation  .. versionadded:: 0.9 (+5 more)

### Community 314 - "Community 314"
Cohesion: 0.08
Nodes (23): ai_zeros(), assoc_laguerre(), bei_zeros(), beip_zeros(), ber_zeros(), bernoulli(), berp_zeros(), bi_zeros() (+15 more)

### Community 315 - "Community 315"
Cohesion: 0.08
Nodes (1): TestMakeTupleBunch

### Community 316 - "Community 316"
Cohesion: 0.10
Nodes (5): Tests for cholesky_banded() and cho_solve_banded., TestChoFactor, TestCholesky, TestCholeskyBanded, TestOverwrite

### Community 317 - "Community 317"
Cohesion: 0.09
Nodes (15): check_lapack_misaligned(), _check_orth(), # NOTE: These matrices may be ill-conditioned and lead to a, Check linalg works with non-aligned memory (float32), Check linalg works with non-aligned memory (float64), Check that complex objects don't need to be completely aligned, test_aligned_mem(), test_aligned_mem_complex() (+7 more)

### Community 318 - "Community 318"
Cohesion: 0.08
Nodes (4): # TODO: add more distributions, pdf, cdf etc should map scalar values to scalars. check with and     w/o domain, test_scalar_inputs(), TestQRVS

### Community 319 - "Community 319"
Cohesion: 0.13
Nodes (6): TestKolmogi, TestKolmogorov, TestKolmogp, TestSmirnov, TestSmirnovi, TestSmirnovp

### Community 320 - "Community 320"
Cohesion: 0.08
Nodes (7): check_pickling(), marginal_pdf(), Test functions for multivariate normal, t, and related distributions., Integrate marginalized dimensions of multivariate     probability distribution t, test_random_state_property(), TestMarginal, TestWishart

### Community 321 - "Community 321"
Cohesion: 0.08
Nodes (1): TestBootstrap

### Community 322 - "Community 322"
Cohesion: 0.09
Nodes (8): _cs_matrix, _csc_base, isspmatrix_csc(), Compressed Sparse Column matrix format, Returns a copy of column i of the matrix, as a (m x 1)         CSC matrix (colum, swap the members of x if this is a column-oriented matrix, Is `x` of csc_matrix type?      .. warning::         SciPy sparse is shifting fr, Returns a copy of row i of the matrix, as a (1 x n)         CSR matrix (row vect

### Community 323 - "Community 323"
Cohesion: 0.10
Nodes (12): DenseSuper_from_Numeric(), droprule_cvt(), droprule_one_cvt(), LU_to_csc(), LU_to_csc_matrix(), NCFormat_from_spMatrix(), newSuperLUObject(), NRFormat_from_spMatrix() (+4 more)

### Community 324 - "Community 324"
Cohesion: 0.12
Nodes (16): _Bunch, DoubleInfiniteFunc, LRUDict, quad_vec(), _quadrature_gk(), _quadrature_gk15(), _quadrature_gk21(), _quadrature_trapezoid() (+8 more)

### Community 325 - "Community 325"
Cohesion: 0.11
Nodes (19): FPUModeChangeWarning, Warning about FPU mode change, RuntimeWarning, _backends_kwargs_from_request(), check_fpu_mode(), devices(), pytest_configure(), Check FPU mode was not changed during the test. (+11 more)

### Community 326 - "Community 326"
Cohesion: 0.12
Nodes (11): r"""     Linear Time Invariant system in state-space form.      Represents the s, Create new StateSpace object and settle inheritance., Post-multiply another system or a scalar          Handles multiplication of syst, Pre-multiply a scalar or matrix (but not StateSpace), Negate the system (equivalent to pre-multiplying by -1)., Adds two systems in the sense of frequency domain addition., State matrix of the `StateSpace` system., Input matrix of the `StateSpace` system. (+3 more)

### Community 327 - "Community 327"
Cohesion: 0.13
Nodes (13): Arg, ComplexArg, FixedArg, IntArg, Generate a set of numbers on the real axis, concentrating on     'interesting' r, Return an array containing n numbers., _CDFData, EndpointFilter (+5 more)

### Community 329 - "Community 329"
Cohesion: 0.10
Nodes (25): _chk_asarray(), describe(), kurtosis(), kurtosistest(), mode(), moment(), normaltest(), Compute the trimmed maximum      This function computes the maximum value of an (+17 more)

### Community 330 - "Community 330"
Cohesion: 0.09
Nodes (5): geninvgauss_mode(), geninvgauss_pdf(), invgauss_mode(), invgauss_pdf(), _validate_qmc_input()

### Community 331 - "Community 331"
Cohesion: 0.11
Nodes (24): cdf_mp(), main(), moment_mp(), mp_res_to_dict(), pdf_mp(), Straightforward implementation of studentized range CDF, Straightforward implementation of studentized range PDF, Implementation of the studentized range moment (+16 more)

### Community 332 - "Community 332"
Cohesion: 0.23
Nodes (4): _bracket_minimum(), _bracket_root(), TestBracketMinimum, TestBracketRoot

### Community 333 - "Community 333"
Cohesion: 0.11
Nodes (2): assert_nlff_less_or_close(), TestFit

### Community 334 - "Community 334"
Cohesion: 0.11
Nodes (6): lowerBidiagonalMatrix(), Copyright (C) 2010 David Fong and Michael Saunders Distributed under the same li, Check that >2-D operators are rejected cleanly., test_nD(), TestLSMR, TestLSMRReturns

### Community 335 - "Community 335"
Cohesion: 0.15
Nodes (2): TestMMIOArray, TestMMIOSparseCSR

### Community 336 - "Community 336"
Cohesion: 0.08
Nodes (25): rotation_to_xp(), test_align_vectors_mixed_dtypes(), test_align_vectors_no_noise(), test_align_vectors_noise(), test_approx_equal(), test_approx_equal_batched(), test_boolean_indexes(), test_concatenate() (+17 more)

### Community 337 - "Community 337"
Cohesion: 0.08
Nodes (11): Test function `signal.hilbert2`., Raise all exceptions in `hilbert2`., Needed for 100% coverage, gh-25176: for a separable signal `hilbert2` is the outer product of         the, Compare passing tuple to single int., Compare desired and calculated values in Fourier space., Test that a real signal with Z[-p,-q] == np.conj(Z[p,q])         produces a zero, 2d transform on 3d array is equal to 2d transform on 2d slices. (+3 more)

### Community 338 - "Community 338"
Cohesion: 0.09
Nodes (4): int_to_int8(), Wrap an integer to the interval [-128, 127]., Some of the sparsetools routines use dense 2D matrices whose     total size is n, TestInt32Overflow

### Community 339 - "Community 339"
Cohesion: 0.10
Nodes (23): factorized(), _get_umf_family(), is_sptriangular(), MatrixRankWarning, Get umfpack family string given the sparse matrix dtype., Solve the sparse linear system Ax=b, where b may be a vector or a matrix.      P, Warning for exactly singular matrices., Select default sparse direct solver to be used.      Parameters     ---------- (+15 more)

### Community 340 - "Community 340"
Cohesion: 0.09
Nodes (21): cc_diff(), cs_diff(), diff(), hilbert(), ihilbert(), itilbert(), Differential and pseudo-differential operators., Return inverse h-Tilbert transform of a periodic sequence x.      If ``x_j`` and (+13 more)

### Community 341 - "Community 341"
Cohesion: 0.10
Nodes (13): ClusterNode, _order_cluster_tree(), The identifier of the target node.          For ``0 <= i < n``, `i` corresponds, The number of leaf nodes (original observations) belonging to         the cluste, Return a reference to the left child tree object.          Returns         -----, Return a reference to the right child tree object.          Returns         ----, Return True if the target node is a leaf.          Returns         -------, Perform pre-order traversal without recursive function calls.          When a le (+5 more)

### Community 342 - "Community 342"
Cohesion: 0.12
Nodes (15): cubature(), CubatureRegion, CubatureResult, _InfiniteLimitsTransform, _is_strictly_in_region(), Given the integration limits `a` and `b` describing a rectangular region and a l, A transformation that can be applied to an integral., New limits of integration after applying the transformation. (+7 more)

### Community 343 - "Community 343"
Cohesion: 0.14
Nodes (7): _check_dimensionality(), _check_points(), interpn(), Interpolation at coordinates.          Parameters         ----------         xi, Multidimensional interpolation on regular or rectilinear grids.      Strictly sp, Interpolator of specified order on a rectilinear grid in N ≥ 1 dimensions., RegularGridInterpolator

### Community 344 - "Community 344"
Cohesion: 0.12
Nodes (14): qh_appendfacet(), qh_deletevisible(), qh_delfacet(), qh_gethash(), qh_makenew_nonsimplicial(), qh_makenewfacet(), qh_matchneighbor(), qh_matchnewfacets() (+6 more)

### Community 345 - "Community 345"
Cohesion: 0.15
Nodes (14): LaplacianNd, MikotaK, MikotaM, The grid Laplacian in ``N`` dimensions and its eigenvalues/eigenvectors.      Co, Converts the Laplacian data to a dense array.          Returns         -------, Constructs a sparse array from the Laplacian data. The returned sparse         a, Construct the Sakurai matrix as a banded array., Construct the Sakurai matrix in a sparse format. (+6 more)

### Community 346 - "Community 346"
Cohesion: 0.10
Nodes (21): _dhtm(), firls(), firwin(), firwin2(), firwin_2d(), kaiser_atten(), kaiser_beta(), kaiserord() (+13 more)

### Community 347 - "Community 347"
Cohesion: 0.13
Nodes (23): _clip_prob(), _kolmogn(), _kolmogn_DMTW(), _kolmogn_p(), _kolmogn_PelzGood(), _kolmogn_Pomeranz(), _kolmogni(), kolmognp() (+15 more)

### Community 348 - "Community 348"
Cohesion: 0.10
Nodes (24): brunnermunzel(), _chk_size(), count_tied_groups(), find_repeats(), friedmanchisquare(), _kendall_p_exact(), kendalltau(), kendalltau_seasonal() (+16 more)

### Community 349 - "Community 349"
Cohesion: 0.09
Nodes (21): compare_medians_ms(), hdmedian(), hdquantiles(), hdquantiles_sd(), idealfourths(), median_cihs(), mjci(), mquantiles_cimj() (+13 more)

### Community 350 - "Community 350"
Cohesion: 0.09
Nodes (14): multivariate_t_frozen, multivariate_t_gen, _PSD, Determine if input dimensions can be marginalized.      Parameters     ---------, Compute coordinated functions of a symmetric positive semidefinite matrix., Check whether x lies in the support of the distribution., r"""     A multivariate t-distributed random variable.      The `loc` parameter, Multivariate t-distribution probability density function.          Parameters (+6 more)

### Community 351 - "Community 351"
Cohesion: 0.12
Nodes (18): _choose_method(), _l_p_asymptotic(), _l_p_exact(), _l_vectorized(), page_trend_test(), _PageL, PageTrendTestResult, r"""     Perform Page's Test, a measure of trend in observations between treatme (+10 more)

### Community 352 - "Community 352"
Cohesion: 0.14
Nodes (3): Test of 1D arithmetic operations, TestArithmetic1D, toarray()

### Community 353 - "Community 353"
Cohesion: 0.08
Nodes (5): Test method='gbt' with alpha=0.25 for tf and zpk cases., Test that the solution to the discrete approximation of a continuous         sys, TestC2D, TestC2dInvariants, TestC2dLti

### Community 354 - "Community 354"
Cohesion: 0.12
Nodes (5): Tests from old fortran based lu test suite, Check lu decomposition on medium size, rectangular matrix., TestLU, TestLUFactor, TestLUSolve

### Community 355 - "Community 355"
Cohesion: 0.11
Nodes (9): check_cdf_ppf(), check_discrete_chisquare(), check_moment_frozen(), check_oth(), check_pmf_cdf(), check_scale_docstring(), Perform chisquare test for random sample of a discrete distribution      Paramet, test_discrete_basic() (+1 more)

### Community 356 - "Community 356"
Cohesion: 0.09
Nodes (3): TestGenHyperbolic, TestGenInvGauss, TestNormInvGauss

### Community 357 - "Community 357"
Cohesion: 0.25
Nodes (9): dB(), TestButter, TestButtord, TestCheb1ord, TestCheb2ord, TestCheby1, TestCheby2, TestEllip (+1 more)

### Community 358 - "Community 358"
Cohesion: 0.11
Nodes (4): Tests errors and warnings derived from MGC., Test validity of MGC test statistic, TestMGCErrorWarnings, TestMGCStat

### Community 359 - "Community 359"
Cohesion: 0.10
Nodes (14): Test input validation and raised exceptions., Test if an empty array is returned if no peaks are provided., Test if height of prominences is correctly calculated in signal with         ris, Test with non-C-contiguous input arrays., Test if wlen actually shrinks the evaluation range correctly., Verify that exceptions and warnings are raised., Verify that appropriate warnings are raised., Test a simple use case with easy to verify results at different relative (+6 more)

### Community 360 - "Community 360"
Cohesion: 0.08
Nodes (3): Results above from SAS PROC NPAR1WAY, e.g.          DATA myData;         INPUT X, Results above from R cor.test, e.g.          options(digits=16)         x <- c(1, TestPermutationTest

### Community 361 - "Community 361"
Cohesion: 0.11
Nodes (10): _load_data(), Load npz data file under data/     Returns a copy of the data, rather than keepi, Checks if 0 = XA + A'X - XB(R)^{-1} B'X + Q is true, Checks if X = A'XA-(A'XB)(R+B'XB)^-1(B'XA)+Q) is true, test_solve_generalized_discrete_are(), TestSolveCommonAre, TestSolveContinuousAre, TestSolveDiscreteAre (+2 more)

### Community 362 - "Community 362"
Cohesion: 0.08
Nodes (3): test newton with array, test secant doesn't continue to iterate zero derivatives, TestNewton

### Community 363 - "Community 363"
Cohesion: 0.09
Nodes (8): f1(), f1_1(), f1_2(), f1_and_p_and_pp(), Test Halley's works with complex roots, Test secant method with a non-zero dp, but an infinite newton step, test_complex_halley(), test_zero_der_nz_dp()

### Community 364 - "Community 364"
Cohesion: 0.13
Nodes (20): apply(), as_exp_coords(), compose_transforms(), _compute_se3_exp_translation_transform(), _compute_se3_log_translation_transform(), _create_skew_matrix(), _create_transformation_matrix(), from_components() (+12 more)

### Community 365 - "Community 365"
Cohesion: 0.13
Nodes (17): Enum, BackendSupportStatus, calculate_table_statistics(), is_inherently_out_of_scope(), make_flat_capabilities_table(), _process_capabilities_table_entry(), Generate flat tables showing Array API capabilities for use in docs.  These tabl, Generate full table of array api capabilities across public functions.      Para (+9 more)

### Community 366 - "Community 366"
Cohesion: 0.17
Nodes (22): _execute_1D(), _execute_nD(), fft(), fft2(), fftn(), hfft(), hfft2(), hfftn() (+14 more)

### Community 367 - "Community 367"
Cohesion: 0.11
Nodes (14): Easom, Eckerle4, EggCrate, EggHolder, ElAttarVidyasagarDutta, Exp2, Exponential, r"""     Egg Crate objective function.      This class defines the Egg Crate [1] (+6 more)

### Community 368 - "Community 368"
Cohesion: 0.11
Nodes (14): Hansen, Hartmann3, Hartmann6, HelicalValley, HimmelBlau, HolderTable, Hosaki, r"""     Hartmann6 objective function.      This class defines the Hartmann6 [1] (+6 more)

### Community 369 - "Community 369"
Cohesion: 0.11
Nodes (14): r"""     Wayburn and Seader 1 objective function.      This class defines the Wa, r"""     Wayburn and Seader 2 objective function.      This class defines the Wa, r"""     Weierstrass objective function.      This class defines the Weierstrass, r"""     Whitley objective function.      This class defines the Whitley [1]_ gl, r"""     Wolfe objective function.      This class defines the Wolfe [1]_ global, r"""     Wavy objective function.      This class defines the W / Wavy [1]_ glob, r"""     Watson objective function.      This class defines the Watson [1]_ glob, Watson (+6 more)

### Community 370 - "Community 370"
Cohesion: 0.10
Nodes (14): _build_evaluation_coefficients(), _build_system(), kernel_matrix(), kernel_vector(), polynomial_matrix(), polynomial_vector(), Build the system used to solve for the RBF interpolant coefficients.      Parame, Construct the coefficients needed to evaluate     the RBF.      Parameters     - (+6 more)

### Community 371 - "Community 371"
Cohesion: 0.12
Nodes (21): bicg(), bicgstab(), cg(), cgs(), _get_atol_rtol(), gmres(), qmr(), A helper function to handle tolerance normalization (+13 more)

### Community 372 - "Community 372"
Cohesion: 0.11
Nodes (21): Decorator, doc_replace(), docformat(), extend_notes_in_docstring(), filldoc(), indentcount_lines(), inherit_docstring_from(), Utilities to allow inserting docstring fragments for common parameters into func (+13 more)

### Community 373 - "Community 373"
Cohesion: 0.10
Nodes (23): _align_nums(), bilinear(), bilinear_zpk(), lp2bp(), lp2bp_zpk(), lp2bs(), lp2bs_zpk(), lp2hp() (+15 more)

### Community 374 - "Community 374"
Cohesion: 0.12
Nodes (21): _default_response_times(), dimpulse(), dlsim(), dstep(), impulse(), lsim(), Simulate output of a continuous-time linear system.      Parameters     --------, Compute a reasonable set of time samples for the response time.      This functi (+13 more)

### Community 375 - "Community 375"
Cohesion: 0.15
Nodes (15): cast_order(), Func, generate_loop(), generate_ufuncs(), get_declaration(), iter_variants(), main(), Generate a UFunc loop function that calls a function given as its     data param (+7 more)

### Community 376 - "Community 376"
Cohesion: 0.11
Nodes (20): _add_reduced_axes(), _axis_nan_policy_factory(), _broadcast_array_shapes_remove_axis(), _broadcast_arrays(), _broadcast_concatenate(), _broadcast_shapes(), _broadcast_shapes_remove_axis(), _check_empty_inputs() (+12 more)

### Community 377 - "Community 377"
Cohesion: 0.09
Nodes (1): TestLSQ

### Community 378 - "Community 378"
Cohesion: 0.21
Nodes (3): _assert_inverts(), ProbArg, TestCDFlib

### Community 379 - "Community 379"
Cohesion: 0.09
Nodes (3): _noncentral_chi_cdf(), _noncentral_chi_pdf(), TestPdtrik

### Community 380 - "Community 380"
Cohesion: 0.13
Nodes (4): _bracket_minimum(), TestChandrupatlaMinimize, TestFindRoot, _vectorize()

### Community 381 - "Community 381"
Cohesion: 0.11
Nodes (6): Simple test to ensure tuple backwards-compatibility of the returned object., RobustSlopesTest, TestChatterjeeXi, TestSiegelslopes, TestSpearmanRho, TestTheilslopes

### Community 382 - "Community 382"
Cohesion: 0.09
Nodes (12): Test behavior for signal without local maxima., Test plateau size condition for peaks., Test height condition for peaks., Test threshold condition for peaks., Test distance condition for peaks., Test prominence condition for peaks., Test width condition for peaks., Test returned properties. (+4 more)

### Community 383 - "Community 383"
Cohesion: 0.09
Nodes (2): _generate_spherical_points(), TestGeometricSlerp

### Community 384 - "Community 384"
Cohesion: 0.09
Nodes (2): Test class for scipy.stats.variation, TestVariation

### Community 385 - "Community 385"
Cohesion: 0.14
Nodes (19): _angular_acceleration_nonlinear_term(), _angular_rate_to_rotvec_dot_matrix(), _compute_angular_acceleration(), _compute_angular_rate(), _create_block_3_diagonal_matrix(), _create_skew_matrix(), _matrix_vector_product_of_stacks(), Compute the non-linear term in angular acceleration.      The angular accelerati (+11 more)

### Community 386 - "Community 386"
Cohesion: 0.11
Nodes (16): _check_obsolete(), ConstantWarning, find(), parse_constants_2002to2014(), parse_constants_2018toXXXX(), precision(), Fundamental Physical Constants ------------------------------  These constants a, Accessing a constant no longer in current CODATA data set. (+8 more)

### Community 387 - "Community 387"
Cohesion: 0.11
Nodes (16): odeint(), ODEintWarning, Warning raised during the execution of `odeint`., Integrate a system of ordinary differential equations.      .. note:: For new co, ======================================== Special functions (:mod:`scipy.special`, Warnings and Exceptions that can be raised by special functions., Exception that can be raised by special functions., Warning that can be emitted by special functions. (+8 more)

### Community 388 - "Community 388"
Cohesion: 0.14
Nodes (11): AAA, _BarycentricRational, FloaterHormannInterpolator, Compute the poles of the rational approximation.          Returns         ------, Compute the residues of the poles of the approximation.          Returns, Compute the roots of the rational approximation.          Returns         ------, r"""     AAA real or complex rational approximation.      As described in [1]_,, Base class for barycentric representation of a rational function. (+3 more)

### Community 389 - "Community 389"
Cohesion: 0.12
Nodes (10): _BPoly, _PPoly, Piecewise polynomial in the power basis.      The polynomial between ``x[i]`` an, Evaluate the piecewise polynomial or its derivative.          Parameters, Compute a definite integral over a piecewise polynomial.          Parameters, Find real solutions of the equation ``pp(x) == y``.          Parameters, Find real roots of the piecewise polynomial.          Parameters         -------, Piecewise polynomial in the Bernstein basis.      The polynomial between ``x[i]` (+2 more)

### Community 390 - "Community 390"
Cohesion: 0.11
Nodes (12): _build_and_solve_system(), _build_evaluation_coefficients(), _build_system(), compute_interpolation(), kernel_matrix(), polynomial_matrix(), 'Generic' Array API backend for RBF interpolation.  The general logic is this: `, Evaluate RBFs, with centers at `x`, at `x`. (+4 more)

### Community 391 - "Community 391"
Cohesion: 0.16
Nodes (16): qh_appendprint(), qh_freebuffers(), qh_freebuild(), qh_freeqhull(), qh_init_A(), qh_init_B(), qh_init_qhull_command(), qh_initflags() (+8 more)

### Community 392 - "Community 392"
Cohesion: 0.15
Nodes (21): _C_contiguous_copy(), estimate_rank(), estimate_spectral_norm(), estimate_spectral_norm_diff(), id_to_svd(), interp_decomp(), _is_real(), Same as np.ascontiguousarray, but ensure a copy (+13 more)

### Community 393 - "Community 393"
Cohesion: 0.14
Nodes (19): _adjust_scheme_to_bounds(), approx_derivative(), check_derivative(), _compute_absolute_step(), _dense_difference(), _eps_for_method(), _Fun_Wrapper, group_columns() (+11 more)

### Community 394 - "Community 394"
Cohesion: 0.13
Nodes (16): MemoizeDer, Unified interfaces to root finding algorithms for real or complex scalar functio, Decorator that caches the value and derivative(s) of function each     time it i, r"""     Options     -------     args : tuple, optional         Extra arguments, r"""Calculate f or use cached value if available, r"""Calculate f' or use a cached value if available, Find a root of a scalar function.      Parameters     ----------     f : callabl, root_scalar() (+8 more)

### Community 395 - "Community 395"
Cohesion: 0.19
Nodes (16): _back_substitute(), _coloc_matrix(), _coloc_nd(), _compute_residuals(), data_matrix(), data_matrix_periodic(), _deBoor_D(), _evaluate_ndbspline() (+8 more)

### Community 396 - "Community 396"
Cohesion: 0.21
Nodes (19): bnorm(), cfode(), ewset(), fnorm(), int_max(), int_min(), intdy(), lsoda() (+11 more)

### Community 397 - "Community 397"
Cohesion: 0.14
Nodes (12): _get_mwu_z(), mannwhitneyu(), _MWU, _mwu_choose_method(), _mwu_input_validation(), Build all the array of frequencies for u from 0 to maxu.         Assumptions:, Standardized MWU statistic, Distribution of MWU statistic under the null hypothesis (+4 more)

### Community 398 - "Community 398"
Cohesion: 0.14
Nodes (5): Check backwards compatibility for dtypes vs scipy 1.16., Check input overwrite behavior of the FFT functions., Check input overwrite behavior of the FFT functions., TestDTypes, TestOverwrite

### Community 399 - "Community 399"
Cohesion: 0.10
Nodes (5): test sparse matrix construction functions, Tests of diags_array that do not rely on diags wrapper., _sprandn(), _sprandn_array(), test_diags_array()

### Community 400 - "Community 400"
Cohesion: 0.10
Nodes (7): _eval_indefinite_integral(), f_gaussian(), f_modified_gaussian(), genz_malik_1980_f_4_exact(), Calculates a definite integral from points `a` to `b` by summing up over the cor, r"""     .. math::          f(\mathbf x) = \exp\left(-\sum^n_{i = 1} (\alpha_i x, r"""     .. math::          f(x, y, z, w) = x^n \sqrt{y} \exp(-y-z^2-w^2)

### Community 401 - "Community 401"
Cohesion: 0.09
Nodes (1): TestGeometricTransform

### Community 402 - "Community 402"
Cohesion: 0.09
Nodes (1): TestInterpolativeDecomposition

### Community 403 - "Community 403"
Cohesion: 0.09
Nodes (1): BaseMixin

### Community 404 - "Community 404"
Cohesion: 0.12
Nodes (15): AutoscaleTests, l1_regression_prob(), LinprogRSTests, Unit test for Linear Programming, Training data is {(x0, y0), (x1, y2), ..., (xn-1, yn-1)}         x in R^d, The scaled model should be optimal, i.e. not produce unscaled model         infe, RRTests, test_choose_solver() (+7 more)

### Community 405 - "Community 405"
Cohesion: 0.09
Nodes (1): Test_abcd_normalize

### Community 406 - "Community 406"
Cohesion: 0.11
Nodes (1): TestApproxDerivativesDense

### Community 407 - "Community 407"
Cohesion: 0.10
Nodes (3): _centered(), TestOrthogonalProcrustes, TestProcrustes

### Community 408 - "Community 408"
Cohesion: 0.09
Nodes (3): TestMultinomialQMC, TestMultivariateNormalQMC, TestNormalQMC

### Community 409 - "Community 409"
Cohesion: 0.10
Nodes (12): alt_sg_coeffs(), check_polyder(), compare_coeffs_to_alt(), If deriv > polyorder, the coefficients should be all 0.     This is a regression, Test some trivial edge cases for savgol_filter()., Tests that the window_length check is using the correct axis., This is an alternative implementation of the SG coefficients.      It uses numpy, test_polyder() (+4 more)

### Community 410 - "Community 410"
Cohesion: 0.12
Nodes (7): Test equivalence between sosfiltfilt and filtfilt, TestCSpline1DEval, TestDetrend, _TestFiltFilt, TestOrderFilt, TestSOSFiltFilt, TestWiener

### Community 411 - "Community 411"
Cohesion: 0.09
Nodes (1): TestCoherence

### Community 412 - "Community 412"
Cohesion: 0.09
Nodes (2): unit tests for sparse utility functions, TestSparseUtils

### Community 413 - "Community 413"
Cohesion: 0.16
Nodes (15): direct_dirchoose_(), direct_dirdivide_(), direct_dirget_i__(), direct_dirgetlevel_(), direct_dirgetmaxdeep_(), direct_dirinfcn_(), direct_dirinit_(), direct_dirinsertlist_() (+7 more)

### Community 414 - "Community 414"
Cohesion: 0.12
Nodes (14): Directive, LegacyDirective, linkcode_resolve(), # TODO: eventually these should be eliminated!, Determine the URL corresponding to Python object, Adapted from docutils/parsers/rst/directives/admonitions.py      Uses a default, multi_rv_generic, random_correlation_gen (+6 more)

### Community 415 - "Community 415"
Cohesion: 0.11
Nodes (20): c2c(), c2cn(), c2r(), c2rn(), hfft2(), ihfft2(), r2c(), r2cn() (+12 more)

### Community 416 - "Community 416"
Cohesion: 0.11
Nodes (19): _asfarray(), _datacopied(), _fix_shape(), _fix_shape_1d(), get_workers(), _init_nd_shape_and_axes(), _iterable_of_int(), _normalization() (+11 more)

### Community 417 - "Community 417"
Cohesion: 0.12
Nodes (12): Langermann, LennardJones, Leon, Levy03, Levy05, Levy13, r"""     Leon objective function.      This class defines the Leon [1]_ global o, r"""     Levy 3 objective function.      This class defines the Levy 3 [1]_ glob (+4 more)

### Community 418 - "Community 418"
Cohesion: 0.13
Nodes (13): Akima1DInterpolator, CubicHermiteSpline, pchip_interpolate(), PchipInterpolator, prepare_input(), Interpolation algorithms using piecewise cubic polynomials., r"""PCHIP shape-preserving interpolator (C1 smooth).      ``x`` and ``y`` are ar, Prepare input for cubic spline interpolators.      All data are converted to num (+5 more)

### Community 419 - "Community 419"
Cohesion: 0.19
Nodes (20): qh_allstatA(), qh_allstatB(), qh_allstatC(), qh_allstatD(), qh_allstatE(), qh_allstatE2(), qh_allstatF(), qh_allstatG() (+12 more)

### Community 420 - "Community 420"
Cohesion: 0.14
Nodes (19): arg_casts(), generate_decl_c(), generate_decl_pxd(), generate_decl_pyx(), generate_file_c(), generate_file_pxd(), generate_file_pyx(), _get_pxd_preamble() (+11 more)

### Community 421 - "Community 421"
Cohesion: 0.30
Nodes (1): VarWriter5

### Community 422 - "Community 422"
Cohesion: 0.13
Nodes (21): braycurtis(), canberra(), chebyshev(), cityblock(), hamming(), jaccard(), mahalanobis(), r"""     Compute the Chebyshev distance.      The *Chebyshev distance* between r (+13 more)

### Community 423 - "Community 423"
Cohesion: 0.21
Nodes (20): clear_mark(), colamd_get_debug(), COLAMD_MAIN(), COLAMD_recommended(), COLAMD_report(), COLAMD_set_defaults(), debug_deg_lists(), debug_mark() (+12 more)

### Community 424 - "Community 424"
Cohesion: 0.18
Nodes (18): check_array(), py_coloc(), py_coloc_nd(), py_data_matrix(), py_data_matrix_periodic(), py_evaluate_all_bspl(), py_evaluate_ndbspline(), py_evaluate_spline() (+10 more)

### Community 425 - "Community 425"
Cohesion: 0.21
Nodes (20): cdist(), cdist_impl(), cdist_unweighted(), cdist_weighted(), cdist_weighted_impl(), common_type(), dtype_num(), get_descriptor() (+12 more)

### Community 427 - "Community 427"
Cohesion: 0.17
Nodes (20): cnorm1(), cnorm1est(), dnorm1(), dnorm1est(), matrix_exponential_c(), matrix_exponential_d(), matrix_exponential_s(), matrix_exponential_z() (+12 more)

### Community 428 - "Community 428"
Cohesion: 0.17
Nodes (11): _binary_search_for_binom_tst(), _binom_exact_conf_int(), _binom_wilson_conf_int(), binomtest(), BinomTestResult, Result of `scipy.stats.binomtest`.      Attributes     ----------     k : int, Compute the estimate and confidence interval for the binomial test.      Returns, Perform a test that the probability of success is p.      The binomial test [1]_ (+3 more)

### Community 429 - "Community 429"
Cohesion: 0.11
Nodes (21): Trims an array by masking the data outside some given limits.      Returns a mas, Trims an array by masking some proportion of the data on each end.     Returns a, Trims the smallest and largest data values.      Trims the `data` by masking the, Trims the data by masking values from one tail.      Parameters     ----------, Returns the trimmed mean of the data along the given axis.      %s, Returns the trimmed variance of the data along the given axis.      %s     ddof, Returns the trimmed standard deviation of the data along the given axis.      %s, Compute the trimmed mean.      Parameters     ----------     a : array_like (+13 more)

### Community 430 - "Community 430"
Cohesion: 0.14
Nodes (20): _bvn(), _cbc_lattice(), _factorize_int(), _mvn_qmc_integrand(), _permuted_cholesky(), _primitive_root(), _qauto(), _qmvn() (+12 more)

### Community 432 - "Community 432"
Cohesion: 0.10
Nodes (11): Compare dsbev eigenvalues and eigenvectors with            the result of linalg., Compare dsbevd eigenvalues and eigenvectors with            the result of linalg, Compare dsbevx eigenvalues and eigenvectors            with the result of linalg, Compare zhbevd eigenvalues and eigenvectors            with the result of linalg, Compare zhbevx eigenvalues and eigenvectors            with the result of linalg, Compare eigenvalues of eigvals_banded with those of linalg.eig., Compare dgbtrf  LU factorisation with the LU factorisation result            of, Compare zgbtrf  LU factorisation with the LU factorisation result            of (+3 more)

### Community 433 - "Community 433"
Cohesion: 0.10
Nodes (3): TestExpect, TestGennorm, TestLaplaceasymmetric

### Community 434 - "Community 434"
Cohesion: 0.10
Nodes (1): TestUnivariateSpline

### Community 435 - "Community 435"
Cohesion: 0.10
Nodes (4): Tests for edge cases of log_gammaincc(a, z) = log(Q(a, z)) = log(1 - P(a, z))., TestLogGammainc, TestLogGammaincc, TestRgamma

### Community 436 - "Community 436"
Cohesion: 0.10
Nodes (21): generate_random_dtype_array(), Test the lapack routine ?gejsv.      This function tests that a singular value d, These tests uses ?gtsvx to solve a random Ax=b system for each dtype.     It tes, This tests the ?ptsvx lapack routine wrapper to solve a random system     Ax = b, test_gees_trexc(), test_gees_trsen(), test_gejsv_general(), test_geqrfp() (+13 more)

### Community 437 - "Community 437"
Cohesion: 0.14
Nodes (7): _assert_unable_to_find_basic_feasible_sol(), _assert_unbounded(), LinprogSimplexTests, Test whether presolve pathway for detecting unboundedness after         constrai, TestLinprogSimplexBland, TestLinprogSimplexDefault, TestLinprogSimplexNoPresolve

### Community 438 - "Community 438"
Cohesion: 0.11
Nodes (5): BaseMixin, SparseMixin, TestBVLS, TestErrorChecking, TestTRF

### Community 439 - "Community 439"
Cohesion: 0.13
Nodes (3): sequence_parallel(), TestFSolve, TestLeastSq

### Community 440 - "Community 440"
Cohesion: 0.13
Nodes (7): For an (m,n) array `a_mat` the output `vec(a_mat)` is an (m*n, 1)         array, r"""         Gupta and Nagar (2000) Theorem 4.3.1 (p.135)         --------------, Test values generated from Julia.          Dockerfile         ----------, Test values generated from Mathematica 13.0.0 for Linux x86 (64-bit)         Rel, r"""         Gupta and Nagar (2000) p.133f         When the number of rows or th, TestMatrixNormal, TestMatrixT

### Community 441 - "Community 441"
Cohesion: 0.10
Nodes (3): TestGriddata, TestNDInterpolators, TestNearestNDInterpolator

### Community 442 - "Community 442"
Cohesion: 0.11
Nodes (8): RandomEngine, test_integers(), test_integers_nd(), test_raises(), test_subclassing_QMCEngine(), TestLow0Bit, TestSobol, TestVDC

### Community 443 - "Community 443"
Cohesion: 0.14
Nodes (14): check_2drbf1d_interpolation(), check_2drbf1d_regularity(), check_2drbf2d_interpolation(), check_2drbf3d_interpolation(), check_rbf1d_interpolation(), check_rbf1d_regularity(), check_rbf1d_stability(), check_rbf2d_interpolation() (+6 more)

### Community 444 - "Community 444"
Cohesion: 0.18
Nodes (16): Binomial(), BinomialInver(), BinomialRatioOfUniforms(), fc_lnpk(), Hypergeometric(), HypInversionMod(), HypRatioOfUnifoms(), LnFac() (+8 more)

### Community 445 - "Community 445"
Cohesion: 0.11
Nodes (17): fft(), fft2(), fftn(), ifft(), ifft2(), ifftn(), irfft(), Discrete Fourier Transforms - _basic.py (+9 more)

### Community 446 - "Community 446"
Cohesion: 0.11
Nodes (11): BivariateSpline, Base class for bivariate splines.      This describes a spline ``s(x, y)`` of de, Evaluate the spline at points.          Returns the interpolated value at ``(xi[, Evaluate the integral of the spline over area [xa,xb] x [ya,yb].          Parame, 1-D smoothing spline fit to a given set of data points.      .. legacy:: class, Return definite integral of the spline between two given points.          Parame, Return all derivatives of the spline at the point x.          Parameters, Return the zeros of the spline.          Notes         -----         Restriction (+3 more)

### Community 447 - "Community 447"
Cohesion: 0.11
Nodes (4): ======================================== Interpolation (:mod:`scipy.interpolate`, rbf - Radial basis functions for interpolation/smoothing scattered N-D data.  Wr, Rbf(*args, **kwargs)      Class for radial basis function interpolation of funct, Rbf

### Community 448 - "Community 448"
Cohesion: 0.12
Nodes (14): check_arguments(), ConstantDenseOutput, DenseOutput, Compute a local interpolant over the last successful step.          Returns, Base class for local interpolant over step made by an ODE solver.      It interp, Evaluate the interpolant.          Parameters         ----------         t : flo, Constant value interpolator.      This class used for degenerate integration cas, Helper function for checking arguments common to all solvers. (+6 more)

### Community 449 - "Community 449"
Cohesion: 0.17
Nodes (17): affine_transform(), geometric_transform(), map_coordinates(), _prepad_for_spline_filter(), Multidimensional spline filter.      Parameters     ----------     %(input)s, Apply an arbitrary geometric transform.      The given mapping function is used, Map the input array to new coordinates by interpolation.      The array of coord, Apply an affine transformation.      Given an output image pixel index vector `` (+9 more)

### Community 450 - "Community 450"
Cohesion: 0.23
Nodes (19): append_c_digits(), append_d_digits(), append_n_digits(), append_nine_digits(), copy_special_str_printf(), d2exp(), d2exp_buffered(), d2exp_buffered_n() (+11 more)

### Community 451 - "Community 451"
Cohesion: 0.11
Nodes (15): buttap(), cheb1ap(), cheb2ap(), gammatone(), _hz_to_erb(), iircomb(), r"""     Return a single transfer function from a series of second-order section, Return (z,p,k) for analog prototype of Nth-order Butterworth filter.      The fi (+7 more)

### Community 452 - "Community 452"
Cohesion: 0.13
Nodes (20): factorial(), factorial2(), factorialk(), _factorialx_approx_core(), _factorialx_array_approx(), _factorialx_array_exact(), _factorialx_wrapper(), _gamma1p() (+12 more)

### Community 453 - "Community 453"
Cohesion: 0.12
Nodes (15): assert_mpmath_equal(), exception_to_nan(), get_args(), inf_to_nan(), mp_assert_allclose(), mpc2complex(), mpf2float(), MpmathData (+7 more)

### Community 454 - "Community 454"
Cohesion: 0.20
Nodes (19): active(), bmv(), cauchy(), cmprlb(), dcsrch(), dcstep(), errclb(), formk() (+11 more)

### Community 455 - "Community 455"
Cohesion: 0.19
Nodes (14): int_max(), int_min(), zewset(), zvhin(), zvindy(), zvjac(), zvjust(), zvnlsd() (+6 more)

### Community 456 - "Community 456"
Cohesion: 0.10
Nodes (1): TestFBLAS2Simple

### Community 457 - "Community 457"
Cohesion: 0.12
Nodes (8): Tests for fortran sequential files, Read a Fortran-style unformatted binary file written with a single write() call,, Read a Fortran unformatted binary file that contains a mix of:     - a double pr, Read a Fortran unformatted binary file     containing a 3D integer array (m, n,, read_unformatted_double(), read_unformatted_int(), read_unformatted_mixed(), test_fortran_roundtrip()

### Community 458 - "Community 458"
Cohesion: 0.10
Nodes (3): matvec_for_pickle(), Test functions for the sparse.linalg._interface module, Needed for test_pickle as local functions are not pickleable

### Community 459 - "Community 459"
Cohesion: 0.12
Nodes (10): LinprogIPTests, magic_square(), Test that autoscale fixes poorly-scaled problem, Generates a linear program for which integer solutions represent an     n x n ma, test_highs_status_message(), TestLinprogIPDense, TestLinprogIPSparse, TestLinprogIPSparseCholmod (+2 more)

### Community 460 - "Community 460"
Cohesion: 0.10
Nodes (1): TestWilcoxon

### Community 461 - "Community 461"
Cohesion: 0.13
Nodes (3): assert_close(), TestCovariance, TestDirichletMultinomial

### Community 462 - "Community 462"
Cohesion: 0.10
Nodes (1): TestDirichlet

### Community 463 - "Community 463"
Cohesion: 0.12
Nodes (9): _compute_symiirorder2_bwd_hs(), get_spline_knot_values(), make_spline_knot_matrix(), Tests for spline filtering., Knot values to the right of a B-spline's center., Matrix to invert to find the spline coefficients., test_spline_filter_reflect_small_n(), test_spline_filter_vs_matrix_solution() (+1 more)

### Community 464 - "Community 464"
Cohesion: 0.10
Nodes (2): TestRegression, TestTrimMean

### Community 465 - "Community 465"
Cohesion: 0.13
Nodes (5): Test vs. manually computed results for modes not in numpy's pad., Naive upfirdn processing in Python.      Note: arg order (x, h) differs to facil, TestUpfirdn, upfirdn_naive(), UpFIRDnCase

### Community 466 - "Community 466"
Cohesion: 0.12
Nodes (19): _kmeans(), kmeans2(), _kpoints(), _kpp(), _krandinit(), _missing_warn(), _py_vq(), Python version of vq algorithm.      The algorithm computes the Euclidean distan (+11 more)

### Community 467 - "Community 467"
Cohesion: 0.12
Nodes (10): AssertionError, assert_deallocated(), gc_state(), Module for testing automatic garbage collection of objects  .. autosummary::, Set status of garbage collector, Context manager to set state of garbage collector to `state`      Parameters, Context manager to check that object is deallocated      This is useful for chec, ReferenceError (+2 more)

### Community 468 - "Community 468"
Cohesion: 0.16
Nodes (16): embed_time_trace(), log_to_dicts(), main(), Read a file-like object |trace| containing -ftime-trace data and yields     abou, Produce time trace output for the specified ninja target. Expects     time-trace, Reads a file-like object |log| containing a .ninja_log, and yields one     about, Represents a single line read for a .ninja_log file. Start and end times     are, Reads all targets from .ninja_log file |log_file|, sorted by start     time (+8 more)

### Community 469 - "Community 469"
Cohesion: 0.19
Nodes (16): int_to_string(), read_float(), read_float_fallback(), read_float_fast_float(), read_float_from_chars(), read_int(), read_int_fallback(), read_int_from_chars() (+8 more)

### Community 470 - "Community 470"
Cohesion: 0.13
Nodes (12): bisplev(), bisplrep(), dblint(), _int_overflow(), fitpack (dierckx in netlib) --- A Python-C wrapper to FITPACK (by P. Dierckx)., Cast the value to a dfitpack_int and raise an OverflowError if the value     can, Find a bivariate B-spline representation of a surface.      Given a set of data, Evaluate a bivariate B-spline and its derivatives.      Return a rank-2 array of (+4 more)

### Community 471 - "Community 471"
Cohesion: 0.11
Nodes (18): insert(), Find the B-spline representation of a 1-D curve.      .. legacy:: function, Find the B-spline representation of an N-D curve.      .. legacy:: function, Evaluate a B-spline or its derivatives.      .. legacy:: function          Speci, Evaluate the definite integral of a B-spline between two given points.      .. l, Find the roots of a cubic B-spline.      .. legacy:: function          Specifica, Evaluate a B-spline and all its derivatives at one point (or set of points) up, Insert knots into a B-spline.      .. legacy:: function          Specifically, w (+10 more)

### Community 472 - "Community 472"
Cohesion: 0.13
Nodes (18): _are_validate_args(), Matrix equation solver routines, Solves the continuous Lyapunov equation :math:`AX + XA^H = Q`.      Uses the Bar, Solves the discrete Lyapunov equation directly.      This function is called by, Solves the discrete Lyapunov equation using a bilinear transformation.      This, Solves the discrete Lyapunov equation :math:`AXA^H - X + Q = 0`.      Parameters, Computes a solution (X) to the Sylvester equation :math:`AX + XB = Q`.      Para, r"""     Solves the continuous-time algebraic Riccati equation (CARE).      The (+10 more)

### Community 473 - "Community 473"
Cohesion: 0.12
Nodes (16): chirp(), _chirp_phase(), gausspulse(), Return a Gaussian modulated sinusoid.      The formula for the returned signal i, Return a periodic sawtooth or triangle waveform.      The sawtooth waveform has, r"""Frequency-swept cosine generator.      In the following, 'Hz' should be inte, Calculate the phase used by `chirp` to generate its output.      See `chirp` for, Frequency-swept cosine generator, with a time-dependent frequency.      This fun (+8 more)

### Community 474 - "Community 474"
Cohesion: 0.15
Nodes (11): _betaincc(), _chdtr(), _chdtrc(), _FuncInfo, _get_native_func(), # IMPORTANT: this only works because all functions in this module, # IMPORTANT: map_blocks works only because all functions in this module, # IMPORTANT: these must all be **elementwise** functions! (+3 more)

### Community 475 - "Community 475"
Cohesion: 0.12
Nodes (4): random_double(), random_float(), rol64(), xoshiro256p()

### Community 479 - "Community 479"
Cohesion: 0.15
Nodes (12): library_call_nodata(), library_call_nonlocal(), library_call_simple(), test_call_nodata(), test_call_nonlocal(), test_call_simple(), test_plus1_callback(), test_plus1b_callback() (+4 more)

### Community 481 - "Community 481"
Cohesion: 0.11
Nodes (14): _cholesky_invwishart_rvs(), matrix_normal_gen, matrix_t_gen, r"""     A matrix normal random variable.      The `mean` keyword specifies the, Adjust quantiles array so that last two axes labels the components of         ea, Matrix normal probability density function.          Parameters         --------, Draw random samples from a matrix normal distribution.          Parameters, r"""     A matrix t-random variable.      The `mean` keyword specifies the mean. (+6 more)

### Community 482 - "Community 482"
Cohesion: 0.11
Nodes (11): multinomial_gen, multivariate_hypergeom_gen, r"""     A multinomial random variable.      Parameters     ----------     %(_do, Multinomial probability mass function.          Parameters         ----------, Covariance matrix of the multinomial distribution.          Parameters         -, Draw random samples from a Multinomial distribution.          Parameters, r"""     A multivariate hypergeometric random variable.      Parameters     ----, Multivariate hypergeometric probability mass function.          Parameters (+3 more)

### Community 483 - "Community 483"
Cohesion: 0.11
Nodes (6): Test that the `array_namespace` function used by         array-api-extra has bee, Test array_namespace special case for JAX zero-gradient arrays, which are, A void dtype that is not a jax.float0 must not be caught in the         special, Test that if all parameters of array_namespace are Array-likes,         the outp, Test that if there is at least one Array API object among         the parameters, TestArrayAPI

### Community 484 - "Community 484"
Cohesion: 0.12
Nodes (6): TestBurr12, TestExpon, TestExponNorm, TestExponpow, TestNorm, TestUniform

### Community 485 - "Community 485"
Cohesion: 0.11
Nodes (2): Test that the reversal of the edges of the input graph works     as expected., test_add_reverse_edges()

### Community 486 - "Community 486"
Cohesion: 0.15
Nodes (11): If x is much greater than v, the bounds                      x, If both x and v are very large, the bounds                      x, The reference values are one minus those of TestIvRatio., If x is +/-0.0, return 1., The reference values are computed using mpmath as follows.          from mpmath, If exactly one of v or x is inf and the other is within domain,         should r, If at least one argument is out of domain, or if v = x = inf,         the functi, If x is +/-0.0, return x to ensure iv_ratio is an odd function. (+3 more)

### Community 487 - "Community 487"
Cohesion: 0.12
Nodes (6): fun_rosenbrock(), fun_rosenbrock_cropped(), jac_rosenbrock(), jac_rosenbrock_cropped(), jac_trivial(), jac_wrong_dimensions()

### Community 488 - "Community 488"
Cohesion: 0.20
Nodes (3): TestImpulse, TestLsim, TestStep

### Community 489 - "Community 489"
Cohesion: 0.11
Nodes (1): Unit test for Mixed Integer Linear Programming

### Community 490 - "Community 490"
Cohesion: 0.12
Nodes (8): Test failure on insufficient iterations, Rejection of unknown sampling method, Check that the routine stops when no minimiser is found            after maximum, Specified bounds ub > lb, Specified bounds are of the form (lb, ub), Ensures the algorithm terminates on infeasible problems            after maxev i, Test Global mode limiting local evaluations with f* too high, TestShgoFailures

### Community 491 - "Community 491"
Cohesion: 0.14
Nodes (10): Unit tests for function `._signaltools.envelope()`., For `envelope()` Raise all exceptions that are used to verify function         p, Ensure that the various parametrizations produce compatible results., Test envelope calculation with real-valued test signals.          The comparison, Test envelope calculation with complex-valued test signals.          We only nee, Test for multi-channel envelope calculations., Test for multi-channel envelope calculations with complex values., Compare output of `envelope()` and `hilbert()`. (+2 more)

### Community 492 - "Community 492"
Cohesion: 0.13
Nodes (3): _kaplan_meier_reference(), TestLogRank, TestSurvival

### Community 493 - "Community 493"
Cohesion: 0.12
Nodes (2): chirp_geometric(), TestChirp

### Community 494 - "Community 494"
Cohesion: 0.11
Nodes (5): Unit test for `scipy.signal.get_windows`., Verify that the `_windows._WIN_FUNC_DATA` dict is consistent.            The key, Raise all exceptions (except those concerning parameter `Nx`)., Ensure that suffixes `_periodic` and `_symmetric` work for window names., TestGetWindow

### Community 495 - "Community 495"
Cohesion: 0.15
Nodes (18): box_intersections(), box_sphere_intersections(), eqp_kktfact(), inside_box_boundaries(), modified_dogleg(), projected_cg(), Equality-constrained quadratic programming solvers., Find the intersection between segment (or line) and box constraints.      Find t (+10 more)

### Community 496 - "Community 496"
Cohesion: 0.27
Nodes (16): cnaupd_wrap(), cneupd_wrap(), dnaupd_wrap(), dneupd_wrap(), dsaupd_wrap(), dseupd_wrap(), pack_dict_to_state_d(), pack_dict_to_state_s() (+8 more)

### Community 497 - "Community 497"
Cohesion: 0.11
Nodes (14): initfilt(), initxfc(), This module contains subroutines for initialization.  Translated from Zaikun Zha, This function initializes the filter (XFILT, etc) that will be used when selecti, This subroutine does the initialization concerning X, function values, and     c, checkbreak_con(), checkbreak_unc(), This module checks whether to break out of the solver loop.  Translated from Zai (+6 more)

### Community 498 - "Community 498"
Cohesion: 0.13
Nodes (11): process_bounds(), `bounds` can either be an object with the properties lb and ub, or a list of tup, process_nl_constraints(), The Python interfaces receives the constraints as lb <= constraint(x) <= ub,, transform_constraint_function(), _project(), This module provides the _project function that attempts to project the initial, Projection of the initial guess onto the feasible set.      Parameters     ----- (+3 more)

### Community 499 - "Community 499"
Cohesion: 0.19
Nodes (14): c2c(), c2c_internal(), c2c_sym_internal(), c2r_internal(), dct(), dct_internal(), dst(), dst_internal() (+6 more)

### Community 500 - "Community 500"
Cohesion: 0.15
Nodes (15): dct(), dctn(), dst(), dstn(), idct(), idctn(), idst(), idstn() (+7 more)

### Community 501 - "Community 501"
Cohesion: 0.11
Nodes (18): average(), centroid(), complete(), linkage(), median(), optimal_leaf_ordering(), Given a linkage matrix Z and distance, reorder the cut tree.      Parameters, Perform complete/max/farthest point linkage on a condensed distance matrix. (+10 more)

### Community 502 - "Community 502"
Cohesion: 0.26
Nodes (15): qh_addpoint(), qh_build_withrestart(), qh_buildcone(), qh_buildcone_mergepinched(), qh_buildcone_onlygood(), qh_buildhull(), qh_buildtracing(), qh_errexit2() (+7 more)

### Community 503 - "Community 503"
Cohesion: 0.15
Nodes (15): diagsvd(), _format_emit_errors_warnings(), null_space(), orth(), SVD decomposition functions., Format/emit errors/warnings from a lowlevel batched routine., Compute singular values of a matrix.      Parameters     ----------     a : (M,, Construct the sigma matrix in SVD from singular values and size M, N.      Param (+7 more)

### Community 504 - "Community 504"
Cohesion: 0.17
Nodes (17): _applyConstraints(), _as2d(), _b_orthonormalize(), _get_indx(), _handle_gramA_gramB_verbosity(), lobpcg(), _makeMatMat(), _matmul_inplace() (+9 more)

### Community 505 - "Community 505"
Cohesion: 0.18
Nodes (11): basinhopping(), BasinHoppingRunner, MinimizerWrapper, basinhopping: The basinhopping global optimization algorithm, Do one cycle of the basinhopping algorithm, print a status update, Class used to store the lowest energy structure, wrap a minimizer function as a minimizer class (+3 more)

### Community 506 - "Community 506"
Cohesion: 0.11
Nodes (18): _cplxpair(), _cplxreal(), _nearest_real_complex_idx(), Sort into pairs of complex conjugates.      Complex conjugates in `z` are sorted, r"""Return zero, pole, gain (z, p, k) representation from a numerator,     denom, r"""     Return polynomial transfer function representation from zeros and poles, r"""     Return second-order sections from transfer function representation., Return zeros, poles, and gain of a series of second-order sections.      Paramet (+10 more)

### Community 507 - "Community 507"
Cohesion: 0.24
Nodes (12): _check_dtype_and_flags(), convert_vec_status(), get_err_mesg(), _linalg_cholesky(), _linalg_det(), _linalg_eig(), _linalg_inv(), _linalg_lstsq() (+4 more)

### Community 508 - "Community 508"
Cohesion: 0.20
Nodes (12): callocateA(), cexpand(), cLUMemInit(), cLUMemXpand(), cLUWorkInit(), cmemory_usage(), copy_mem_singlecomplex(), cSetupSpace() (+4 more)

### Community 509 - "Community 509"
Cohesion: 0.20
Nodes (12): copy_mem_double(), dallocateA(), dexpand(), dLUMemInit(), dLUMemXpand(), dLUWorkInit(), dmemory_usage(), doubleMalloc() (+4 more)

### Community 510 - "Community 510"
Cohesion: 0.29
Nodes (16): dogleg(), enorm(), fdjac1(), fdjac2(), HYBRD(), HYBRJ(), LMDER(), LMDIF() (+8 more)

### Community 511 - "Community 511"
Cohesion: 0.20
Nodes (12): copy_mem_float(), floatMalloc(), sallocateA(), sexpand(), sLUMemInit(), sLUMemXpand(), sLUWorkInit(), smemory_usage() (+4 more)

### Community 512 - "Community 512"
Cohesion: 0.20
Nodes (12): copy_mem_doublecomplex(), doublecomplexMalloc(), zallocateA(), zexpand(), zLUMemInit(), zLUMemXpand(), zLUWorkInit(), zmemory_usage() (+4 more)

### Community 513 - "Community 513"
Cohesion: 0.16
Nodes (14): _mgc_stat(), multiscale_graphcorr(), _ParallelP, _perm_test(), r"""Computes the Multiscale Graph Correlation (MGC) test statistic.      Specifi, Helper function to calculate parallel p-value., r"""Helper function that calculates the p-value. See below for uses.      Parame, r"""Helper function that calculates the MGC stat. See above for use.      Parame (+6 more)

### Community 514 - "Community 514"
Cohesion: 0.14
Nodes (6): bunch, coerce_text(), _Empty, TemplateDef, TemplateObject, TemplateObjectGetter

### Community 515 - "Community 515"
Cohesion: 0.25
Nodes (16): find_position(), isolate_expression(), lex(), parse(), parse_cond(), parse_def(), parse_default(), parse_expr() (+8 more)

### Community 516 - "Community 516"
Cohesion: 0.14
Nodes (14): _analytical_solution(), _band_count(), _linear_banded_jac(), _linear_func(), _linear_jac(), Analytical solution to the linear differential equations dy/dt = a*y.      The s, Linear system dy/dt = a * y, Jacobian of a * y is a. (+6 more)

### Community 517 - "Community 517"
Cohesion: 0.14
Nodes (2): BinopTester, BinopTester_with_shape

### Community 518 - "Community 518"
Cohesion: 0.12
Nodes (5): check_remains_sorted(), _CompressedMixin, Checks that sorted indices property is retained through an operation, _TestFancyIndexingAssign, _TestFancyMultidimAssign

### Community 519 - "Community 519"
Cohesion: 0.11
Nodes (2): TestInsert, TestInterop

### Community 520 - "Community 520"
Cohesion: 0.14
Nodes (4): Check that passing arrays of with different shapes         raises a ValueError., Return a random symmetric (Hermitian) matrix.      If 'dim_or_eigv' is an intege, symrand(), TestEig

### Community 521 - "Community 521"
Cohesion: 0.12
Nodes (2): TestHyp1f1, TestHyperu

### Community 522 - "Community 522"
Cohesion: 0.20
Nodes (10): generate_broadcastable_shapes(), This class aims to help ensure correctness of the LinearOperator     interface,, This check verifies the equivalence of the forward and adjoint computation,, Simple identity operator on square matrices.         Tests batches of RHS via `a, Identity operator with zero-padding on non-square matrices.         Tests batche, Simple (complex) scaling operator on square matrices.         Tests batches of R, Simple rotation operator defined by `matmat` and `adjoint`,         subclassing, Test operators coming from `aslinearoperator`,         *including batched LHS*. (+2 more)

### Community 523 - "Community 523"
Cohesion: 0.16
Nodes (4): setup_bug_8278(), test_is_sptriangular_and_spbandwidth(), TestLinsolve, toarray()

### Community 524 - "Community 524"
Cohesion: 0.12
Nodes (2): linear_sum_assignment_assertions(), test_min_weight_full_matching_small_inputs()

### Community 525 - "Community 525"
Cohesion: 0.13
Nodes (4): MatrixProductOperator, Test functions for the sparse.linalg._onenormest module, This is purely for onenormest testing., TestOnenormest

### Community 526 - "Community 526"
Cohesion: 0.11
Nodes (1): TestOptimizeScalar

### Community 527 - "Community 527"
Cohesion: 0.21
Nodes (16): get_constraints(), run_problem(), test_biggs3(), test_biggs6(), test_cresc4(), test_degenlpb(), test_errinbar(), test_hs102() (+8 more)

### Community 528 - "Community 528"
Cohesion: 0.17
Nodes (8): chr12c(), _doubly_stochastic(), QAPCommonTests, _range_matrix(), Base class for `quadratic_assignment` tests., Test2opt, TestFAQ, TestQAPOnce

### Community 529 - "Community 529"
Cohesion: 0.14
Nodes (6): StandardNormal, test_error_mode_not_in_domain(), test_rvs_size(), test_warning_center_not_in_domain(), TestQRVS, TestTransformedDensityRejection

### Community 530 - "Community 530"
Cohesion: 0.21
Nodes (2): TestCorrelateComplex, TestCorrelateReal

### Community 531 - "Community 531"
Cohesion: 0.11
Nodes (2): Some further tests of the spearmanr function., TestCorrSpearmanr2

### Community 532 - "Community 532"
Cohesion: 0.18
Nodes (6): klee_minty(), KleeMinty, LpGen, MagicSquare, Netlib, Netlib_infeasible

### Community 533 - "Community 533"
Cohesion: 0.12
Nodes (7): complex_incompatible, fmm_error, invalid_argument, invalid_mm, no_vector_support, out_of_range, support_not_selected

### Community 534 - "Community 534"
Cohesion: 0.12
Nodes (16): dct(), dctn(), dst(), dstn(), idct(), idctn(), idst(), idstn() (+8 more)

### Community 535 - "Community 535"
Cohesion: 0.15
Nodes (10): Gear, Giunta, GoldsteinPrice, Griewank, Gulf, r"""     Griewank objective function.      This class defines the Griewank globa, r"""     Gulf objective function.      This class defines the Gulf [1]_ global o, r"""     Giunta objective function.      This class defines the Giunta [1]_ glob (+2 more)

### Community 536 - "Community 536"
Cohesion: 0.15
Nodes (10): r"""     Xin-She Yang 4 objective function.      This class defines the Xin-She, r"""     Xor objective function.      This class defines the Xor [1]_ global opt, r"""     Xin-She Yang 2 objective function.      This class defines the Xin-She, r"""     Xin-She Yang 1 objective function.      This class defines the Xin-She, r"""     Xin-She Yang 3 objective function.      This class defines the Xin-She, XinSheYang01, XinSheYang02, XinSheYang03 (+2 more)

### Community 537 - "Community 537"
Cohesion: 0.15
Nodes (10): r"""     Zimmerman objective function.      This class defines the Zimmerman [1], r"""     Zettl objective function.      This class defines the Zirilli [1]_ glob, r"""     ZeroSum objective function.      This class defines the ZeroSum [1]_ gl, r"""     Zacharov objective function.      This class defines the Zacharov [1]_, r"""     Zettl objective function.      This class defines the Zettl [1]_ global, Zacharov, ZeroSum, Zettl (+2 more)

### Community 538 - "Community 538"
Cohesion: 0.19
Nodes (13): _compute_pair(), _direct(), _get_base_step(), _get_pairs(), _integral_bound(), nsum(), _nsum_iv(), _pair_cache() (+5 more)

### Community 539 - "Community 539"
Cohesion: 0.16
Nodes (13): _check_lsq_design_matrix(), _get_dtype(), _make_lsq_ndbspl(), make_ndbspl(), _preprocess_inputs(), Return np.complex128 for complex dtypes, np.float64 otherwise., Construct the design matrix as a CSR format sparse array.          Parameters, Helpers: validate and preprocess NdBSpline inputs.         Parameters        --- (+5 more)

### Community 540 - "Community 540"
Cohesion: 0.24
Nodes (15): qh_backnormal(), qh_distplane(), qh_findbest(), qh_findbesthorizon(), qh_findbestnew(), qh_gausselim(), qh_getcenter(), qh_getcentrum() (+7 more)

### Community 541 - "Community 541"
Cohesion: 0.15
Nodes (12): expm_cond(), expm_frechet(), expm_frechet_algo_64(), expm_frechet_block_enlarge(), expm_frechet_kronform(), Frechet derivative of the matrix exponential., Frechet derivative of the matrix exponential of A in the direction E.      Param, This is a helper function, mostly for testing and profiling.     Return expm(A), (+4 more)

### Community 542 - "Community 542"
Cohesion: 0.21
Nodes (15): _blocked_elementwise(), column_needs_resampling(), elementary_vector(), every_col_of_X_is_parallel_to_a_col_of_Y(), _max_abs_axis1(), onenormest(), _onenormest_core(), Sparse block 1-norm estimator. (+7 more)

### Community 543 - "Community 543"
Cohesion: 0.20
Nodes (16): check_dist_keyword_names(), check_items(), check_rest(), compare(), find_names(), get_all_dict(), is_deprecated(), main() (+8 more)

### Community 544 - "Community 544"
Cohesion: 0.24
Nodes (10): ARNAUD_BLAS(), ARNAUD_znaupd(), ARNAUD_zneupd(), zgetv0(), znaitr(), znapps(), znaup2(), zneigh() (+2 more)

### Community 545 - "Community 545"
Cohesion: 0.20
Nodes (10): ARNAUD_dnaupd(), ARNAUD_dneupd(), dgetv0(), dnaitr(), dnapps(), dnaup2(), dnconv(), dneigh() (+2 more)

### Community 546 - "Community 546"
Cohesion: 0.24
Nodes (10): ARNAUD_BLAS(), ARNAUD_cnaupd(), ARNAUD_cneupd(), cgetv0(), cnaitr(), cnapps(), cnaup2(), cneigh() (+2 more)

### Community 547 - "Community 547"
Cohesion: 0.20
Nodes (10): ARNAUD_snaupd(), ARNAUD_sneupd(), sgetv0(), snaitr(), snapps(), snaup2(), snconv(), sneigh() (+2 more)

### Community 548 - "Community 548"
Cohesion: 0.22
Nodes (12): ARNAUD_dsaupd(), ARNAUD_dseupd(), dgetv0(), dsaitr(), dsapps(), dsaup2(), dsconv(), dseigt() (+4 more)

### Community 549 - "Community 549"
Cohesion: 0.22
Nodes (12): ARNAUD_ssaupd(), ARNAUD_sseupd(), sgetv0(), ssaitr(), ssapps(), ssaup2(), ssconv(), sseigt() (+4 more)

### Community 550 - "Community 550"
Cohesion: 0.15
Nodes (7): NI_ArrayToLineBuffer(), NI_CanonicalType(), NI_ExtendLine(), NI_InitLineBuffer(), NI_InitPointIterator(), NI_LineIterator(), NI_SubspaceIterator()

### Community 551 - "Community 551"
Cohesion: 0.25
Nodes (14): dewset(), dvhin(), dvindy(), dvjac(), dvjust(), dvnlsd(), dvnorm(), dvode() (+6 more)

### Community 552 - "Community 552"
Cohesion: 0.14
Nodes (15): _correa_entropy(), differential_entropy(), _ebrahimi_entropy(), entropy(), _pad_along_last_axis(), Created on Fri Apr  2 09:06:05 2021  @author: matth, r"""Given a sample of a distribution, estimate the differential entropy.      Se, Calculate the Shannon entropy/relative entropy of given distribution(s).      If (+7 more)

### Community 553 - "Community 553"
Cohesion: 0.16
Nodes (13): _combine_bounds(), _compute_dminus(), _compute_dplus(), _corr(), _filliben(), fit(), _get_fit_fun(), _gof_iv() (+5 more)

### Community 554 - "Community 554"
Cohesion: 0.12
Nodes (2): Compare eigenvalues and eigenvectors of eig_banded            with those of lina, TestOverwrite

### Community 555 - "Community 555"
Cohesion: 0.15
Nodes (3): TestDiagSVD, TestQZ, TestSchur

### Community 556 - "Community 556"
Cohesion: 0.13
Nodes (11): assert_upper_tri(), BaseQRdeltas, check_form_qTu(), make_strided(), test_form_qTu(), TestQRdelete_d, TestQRdelete_f, TestQRinsert_d (+3 more)

### Community 557 - "Community 557"
Cohesion: 0.13
Nodes (8): TestBradford, TestGenExpon, TestGibrat, TestInvGamma, TestJohnsonb, TestJohnsonsu, TestTruncexpon, TestWeibull

### Community 558 - "Community 558"
Cohesion: 0.12
Nodes (1): TestShift

### Community 559 - "Community 559"
Cohesion: 0.12
Nodes (5): Unit test for Linear Programming via Simplex Algorithm., Test for ensuring that no objects referred to by `lp` attributes,     `c`, `A_ub, Similar purpose as `test_aliasing` above., test_aliasing(), test_aliasing2()

### Community 560 - "Community 560"
Cohesion: 0.15
Nodes (1): TestSplu

### Community 561 - "Community 561"
Cohesion: 0.20
Nodes (4): TestOrthoGroup, TestRandomCorrelation, TestSpecialOrthoGroup, TestUnitaryGroup

### Community 562 - "Community 562"
Cohesion: 0.12
Nodes (1): TestNNLS

### Community 563 - "Community 563"
Cohesion: 0.12
Nodes (16): naive_dct1(), naive_dct4(), naive_dst1(), naive_dst4(), Calculate textbook definition version  of DST-I., Calculate textbook definition version of DCT-IV., Calculate textbook definition version of DCT-I., Calculate textbook definition version of DST-IV. (+8 more)

### Community 564 - "Community 564"
Cohesion: 0.15
Nodes (6): check_cont_samples(), check_discr_samples(), test_NumericalInverseHermite_refcycle(), test_with_scipy_distribution(), TestDiscreteAliasUrn, TestDiscreteGuideTable

### Community 565 - "Community 565"
Cohesion: 0.12
Nodes (4): Test callable window function., Verify behavior for parameter `t`.          Note that only `t[0]` and `t[1]` are, Test behavior at Nyquist frequency to ensure issue #14569 is fixed., TestResample

### Community 566 - "Community 566"
Cohesion: 0.13
Nodes (1): TestPartialFractionExpansion

### Community 567 - "Community 567"
Cohesion: 0.12
Nodes (2): Test if frequency location of peak corresponds to frequency of         generated, TestLombscargle

### Community 568 - "Community 568"
Cohesion: 0.14
Nodes (13): cobylb(), fcratio(), getcpen(), This module performs the major calculations of COBYLA.  Translated from Zaikun Z, This subroutine performs the actual computations of COBYLA., This function gets the penalty parameter CPEN so that PREREM = PREREF + CPEN * P, This function calculates the ratio between the "typical change" of F and that of, This module calculates the reduction ratio for trust-region methods.  Translated (+5 more)

### Community 569 - "Community 569"
Cohesion: 0.22
Nodes (12): complex_parse_adapter, generalize_symmetry_array(), generalize_symmetry_coordinate(), pattern_parse_adapter, read_array_body_sequential(), read_chunk_array(), read_chunk_matrix_coordinate(), read_chunk_vector_coordinate() (+4 more)

### Community 570 - "Community 570"
Cohesion: 0.20
Nodes (12): dblquad(), nquad(), _OptFunc, quad(), _quad_weight(), _RangeFunc, Return stored value.          *args needed because range_ can be float or func,, Compute a definite integral.      Integrate func from `a` to `b` (possibly infin (+4 more)

### Community 571 - "Community 571"
Cohesion: 0.15
Nodes (15): _dense_num_jac(), norm(), num_jac(), Assert that first_step is valid and return it., Assert that max_Step is valid and return it., Finite differences Jacobian approximation tailored for ODE solvers.      This fu, Display a warning for extraneous keyword arguments.      The initializer of each, Validate tolerance values. (+7 more)

### Community 572 - "Community 572"
Cohesion: 0.15
Nodes (13): _check_format_errors_warnings(), cho_factor(), cho_solve(), cho_solve_banded(), _cholesky(), cholesky_banded(), Cholesky decomposition functions., Compute the Cholesky decomposition of a matrix, to use in cho_solve.      Return (+5 more)

### Community 573 - "Community 573"
Cohesion: 0.16
Nodes (16): _expand_footprint(), _expand_mode(), _expand_origin(), generic_filter(), maximum_filter(), median_filter(), _min_or_max_filter(), minimum_filter() (+8 more)

### Community 574 - "Community 574"
Cohesion: 0.23
Nodes (11): dual_annealing(), EnergyState, LocalSearchWrapper, ObjectiveFunWrapper, Class used to record the energy state. At any time, it knows what is the     cur, Initialize current location is the search domain. If `x0` is not         provide, Class used to generate new coordinates based on the distorted     Cauchy-Lorentz, Class used to wrap around the minimizer used for local search     Default local (+3 more)

### Community 575 - "Community 575"
Cohesion: 0.19
Nodes (9): call_python_function(), jac_multipack_calling_function(), jac_multipack_lm_function(), minpack_hybrd(), minpack_hybrj(), minpack_lmder(), minpack_lmdif(), raw_multipack_calling_function() (+1 more)

### Community 576 - "Community 576"
Cohesion: 0.20
Nodes (15): Unified interfaces to root finding algorithms.  Functions --------- - root : fin, r"""     Find a root of a vector function.      Parameters     ----------     fu, Solve for least squares with Levenberg-Marquardt      Options     -------     co, Options     -------     nit : int, optional         Number of iterations to make, root(), _root_anderson_doc(), _root_broyden1_doc(), _root_broyden2_doc() (+7 more)

### Community 577 - "Community 577"
Cohesion: 0.16
Nodes (15): axis_reverse(), axis_slice(), const_ext(), even_ext(), odd_ext(), Functions for acting on a axis of an array., Even extension at the boundaries of an array      Generate a new ndarray by maki, Constant extension at the boundaries of an array      Generate a new ndarray tha (+7 more)

### Community 578 - "Community 578"
Cohesion: 0.21
Nodes (9): BadCoefficients, Warning about badly conditioned filter coefficients., _assert_poles_close(), Check each pole in P1 is close to a pole in P2 with a 1e-8     relative toleranc, # TODO: add meaningful test where X0 is a list, TestLti, TestStateSpace, TestTransferFunction (+1 more)

### Community 579 - "Community 579"
Cohesion: 0.18
Nodes (13): abcd_normalize(), cont2discrete(), ltisys -- a collection of functions to convert linear time invariant systems fro, r"""Check state-space matrices compatibility and ensure they are 2d arrays., r"""Transfer function to state-space representation.      Parameters     -------, r"""State-space to transfer function.      A, B, C, D defines a linear state-spa, Zero-pole-gain representation to state-space representation.      Parameters, State-space representation to zero-pole-gain representation.      A, B, C, D def (+5 more)

### Community 580 - "Community 580"
Cohesion: 0.15
Nodes (13): lti, Returns the discretized `TransferFunction` system.          Parameters         -, r"""     Continuous-time Linear Time Invariant system in zeros, poles, gain form, r"""     Continuous-time linear time invariant system base class.      Parameter, Returns the discretized `ZerosPolesGain` system.          Parameters         ---, r"""     Continuous-time Linear Time Invariant system in state-space form., Returns the discretized `StateSpace` system.          Parameters         -------, Create an instance of the appropriate subclass. (+5 more)

### Community 581 - "Community 581"
Cohesion: 0.15
Nodes (11): _lstsq(), _poly1d(), polyfit(), polymul(), polyroots(), polyval(), Partial replacements for numpy polynomial routines, with Array API compatibility, Constructor of np.poly1d object from an array of coefficients (r=False) (+3 more)

### Community 582 - "Community 582"
Cohesion: 0.13
Nodes (8): Inverse short-time Fourier transform.          Parameters         ----------, Largest signal index and slice index due to padding.          Parameters, First sample index after signal end not touched by a time slice.          `k_max, Index of first non-overlapping upper time slice for `n` sample         input., Number of time slices for an input signal with `n` samples.          It is given, Return nearest sample index k_p for which ``t[k_p] == t[p]`` holds.          The, Inverse to `_fft_func`.          Returned is an array of length `m_num`. If the, Return minimum and maximum time-frequency values.          Parameters         --

### Community 583 - "Community 583"
Cohesion: 0.15
Nodes (16): _cmplx_sort(), _compute_factors(), _compute_residues(), _group_poles(), invres(), invresz(), Sort roots based on magnitude.      Parameters     ----------     p : array_like, Determine unique roots and their multiplicities from a list of roots.      Param (+8 more)

### Community 584 - "Community 584"
Cohesion: 0.13
Nodes (10): r"""     A vector-valued uniform direction.      Return a random direction (unit, Draw random samples from S(N-1).          Parameters         ----------, Private method to generate uniform directions     Reference: Marsaglia, G. (1972, In 2D, the von Mises-Fisher distribution reduces to the         von Mises distri, Generate samples from a von Mises-Fisher distribution         with mu = [1, 0, 0, Generate samples from an n-dimensional von Mises-Fisher distribution         wit, A QR decomposition is used to find the rotation that maps the         north pole, Draw random samples from a von Mises-Fisher distribution.          Parameters (+2 more)

### Community 585 - "Community 585"
Cohesion: 0.26
Nodes (5): fill_command(), get_file_template(), paste_script_template_renderer(), sub(), Template

### Community 586 - "Community 586"
Cohesion: 0.18
Nodes (15): _butter_analog_poles(), butter_lp(), _prod(), Some signal functions implemented using mpmath., Frequency response of a filter in zpk format, using mpmath.      This is the sam, Returns the product of the elements in the sequence `seq`., Return relative degree of transfer function from zeros and poles.      This is s, Bilinear transformation to convert a filter from analog to digital. (+7 more)

### Community 587 - "Community 587"
Cohesion: 0.13
Nodes (6): _dt_from_prefix(), parametrize_blas(), Array dtype from a blas-style prefix., Parametrize a test over BLAS prefixes, "sdcz", and over the BLAS modules,     `f, # FIXME: suppress?, TestFBLAS3Simple

### Community 588 - "Community 588"
Cohesion: 0.13
Nodes (7): Verify blas_int size matches the build configuration., Test dgemm works correctly - exercises blas_int for dimensions., Tests for blas_int type used in cython_blas/cython_lapack., Test the function pointers that are expected to fail on     Mac OS X without the, TestBlasInt, TestDGEMM, TestWfuncPointers

### Community 589 - "Community 589"
Cohesion: 0.19
Nodes (2): Check that passing a non-square array raises a ValueError., TestCDF2RDF

### Community 590 - "Community 590"
Cohesion: 0.13
Nodes (1): TestGoodnessOfFit

### Community 591 - "Community 591"
Cohesion: 0.13
Nodes (2): # NOTE: using a Generator changes the, TestHausdorff

### Community 592 - "Community 592"
Cohesion: 0.15
Nodes (9): ComplexExp, CoupledDecay, ODE, Pi, r"""     Free vibration of a simple oscillator::         m \ddot{u} + k u = 0, u, r"""The equation :lm:`\dot u = i u`, r"""Integrate 1/(t + 1j) from t=-10 to t=10, r"""     3 coupled decays suited for banded treatment     (banded mode makes it (+1 more)

### Community 593 - "Community 593"
Cohesion: 0.13
Nodes (2): Regression test for gh-8217., test_repeated_t_values()

### Community 594 - "Community 594"
Cohesion: 0.13
Nodes (1): TestMMIOCoordinate

### Community 595 - "Community 595"
Cohesion: 0.13
Nodes (2): TestBinaryOpeningClosing, TestDilateFix

### Community 596 - "Community 596"
Cohesion: 0.13
Nodes (2): Alternative definitions from Matt Haberland., TestUtils

### Community 597 - "Community 597"
Cohesion: 0.13
Nodes (5): Raise all exceptions in `lfilter_zi`., Return signal as `remainder` when ``len(divisor) > len(signal)``., TestDeconvolve, TestLFilterZI, TestMedFilt

### Community 598 - "Community 598"
Cohesion: 0.13
Nodes (2): Verify behavior of scaling parameter., TestSTFT

### Community 599 - "Community 599"
Cohesion: 0.14
Nodes (3): SkewKurtosisTest, TestKurtosis, TestSkew

### Community 600 - "Community 600"
Cohesion: 0.13
Nodes (1): TestNSum

### Community 601 - "Community 601"
Cohesion: 0.13
Nodes (4): Accumulator, Unit tests for trust-region optimization routines., This is for testing callbacks., TestTrustRegionSolvers

### Community 602 - "Community 602"
Cohesion: 0.16
Nodes (4): r"""Run a collection of tests using the specified method.          The name is u, r"""Run test-cases using the specified method and the supplied signature., TestBracketMethods, TestScalarRootFinders

### Community 603 - "Community 603"
Cohesion: 0.17
Nodes (15): augmented_system_projections(), normal_equation_projections(), orthogonality(), projections(), qr_factorization_projections(), Basic linear factorizations needed by the solver., # TODO: Use a symmetric indefinite factorization, Return linear operators for matrix A using ``QRFactorization`` approach. (+7 more)

### Community 604 - "Community 604"
Cohesion: 0.21
Nodes (6): generate_coo(), generate_csr(), generate_dense(), IOSpeed, MemUsage, Basic speed test. Does not show full potential as     1) a relatively small matr

### Community 605 - "Community 605"
Cohesion: 0.18
Nodes (6): Decimate, FreqzRfft, Lfilter, MedFilt2D, ParallelSosfilt, Sosfilt

### Community 606 - "Community 606"
Cohesion: 0.15
Nodes (12): geostep(), This module contains subroutines concerning the geometry-improving of the interp, This function calculates a geometry step so that the geometry of the interpolati, This function finds (the index) of a current interpolation point to be replaced, setdrop_tr(), findpole(), This module contains subroutines concerning the update of the interpolation set., This subroutine identifies the best vertex of the current simplex with respect t (+4 more)

### Community 607 - "Community 607"
Cohesion: 0.16
Nodes (9): _check_broadcast_up_to(), _do_extrapolate(), interp2d, lagrange(), interp2d(x, y, z, kind='linear', copy=True, bounds_error=False,              fil, Helper to check that arr_from broadcasts up to shape_to, Helper to check if fill_value == "extrapolate" without warnings, r"""     Return a Lagrange interpolating polynomial.      Given two 1-D arrays ` (+1 more)

### Community 608 - "Community 608"
Cohesion: 0.14
Nodes (11): _check_work_float(), _compute_lwork(), _ensure_aligned_and_native(), get_lapack_funcs(), _normalize_lapack_dtype(), Low-level LAPACK functions (:mod:`scipy.linalg.lapack`) ========================, Round floating-point lwork returned by lapack to integer.      Several LAPACK ro, Convert LAPACK-returned work array size float to integer,     carefully for sing (+3 more)

### Community 609 - "Community 609"
Cohesion: 0.25
Nodes (10): Metropolis, RandomDisplacement, Add a random displacement of maximum size `stepsize` to each coordinate.      Ca, Metropolis acceptance criterion.      Parameters     ----------     T : float, MyAcceptTest, MyCallBack, MyTakeStep1, use a copy of displace, but have it set a special parameter to     make sure it' (+2 more)

### Community 610 - "Community 610"
Cohesion: 0.23
Nodes (14): bg_update_dense(), _get_densest(), Routines for removing redundant (linearly dependent) equations from linear progr, Eliminates redundant equations from system of equations defined by Ax = b     an, Counts the number of nonzeros in each row of input array A.     Nonzeros are def, Returns the index of the densest row of A. Ignores rows that are not     eligibl, Eliminates redundant equations from a system of equations.      Eliminates redun, Eliminates trivial equations from system of equations defined by Ax = b    and i (+6 more)

### Community 611 - "Community 611"
Cohesion: 0.19
Nodes (14): asymptotic_series(), dg_series(), main(), optimal_epsilon_integral(), pg_series(), Precompute coefficients of several series expansions of Wright's generalized Bes, Asymptotic expansion for large x.      Phi(a, b, x) ~ Z^(1/2-b) * exp((1+a)/a *, Tylor series expansion of Phi(a, b, x) in a=0 up to order 5. (+6 more)

### Community 613 - "Community 613"
Cohesion: 0.26
Nodes (13): div10(), div100(), div1e8(), div1e9(), div5(), mod1e9(), mulShift64(), mulShiftAll64() (+5 more)

### Community 614 - "Community 614"
Cohesion: 0.19
Nodes (12): CZT, czt_points(), Calculate the chirp z-transform of a signal.          Parameters         -------, Return the points at which the chirp z-transform is computed.          Returns, Create a callable zoom FFT transform function.      This is a specialization of, Return the points at which the chirp z-transform is computed.      Parameters, Compute the frequency response around a spiral in the Z plane.      Parameters, Compute the DFT of `x` only for frequencies in range `fn`.      Parameters     - (+4 more)

### Community 615 - "Community 615"
Cohesion: 0.25
Nodes (15): band_stop_obj(), buttord(), cheb1ord(), cheb2ord(), ellipord(), _find_nat_freq(), _postprocess_wn(), _pre_warp() (+7 more)

### Community 616 - "Community 616"
Cohesion: 0.13
Nodes (8): Generate signal slices along last axis of `x`.          This method is only used, Perform the short-time Fourier transform.          A two-dimensional matrix with, Calculate short-time Fourier transform with a trend being subtracted from, r"""Calculate spectrogram or cross-spectrogram.          The spectrogram is the, Determine and validate slice index range.          Parameters         ----------, Times of STFT for an input signal with `n` samples.          Returns a 1d array, FFT based on the `fft_mode`, `mfft`, `scaling` and `phase_shift`         attribu, Sampling interval of input signal and of the window.          A ``ValueError`` i

### Community 617 - "Community 617"
Cohesion: 0.16
Nodes (15): _apply_conv_mode(), _calc_oa_lens(), _centered(), fftconvolve(), _freq_domain_conv(), _init_freq_conv_axes(), oaconvolve(), Handle the axes argument for frequency-domain convolution.      Returns the inpu (+7 more)

### Community 618 - "Community 618"
Cohesion: 0.14
Nodes (10): directed_hausdorff(), jensenshannon(), MetricInfo, pdist(), Distance computations (:mod:`scipy.spatial.distance`) ==========================, Compute the Jensen-Shannon distance (metric) between     two probability arrays., Pairwise distances between observations in n-dimensional space.      See Notes f, Compute the directed Hausdorff distance between two 2-D arrays.      Distances b (+2 more)

### Community 619 - "Community 619"
Cohesion: 0.13
Nodes (8): Hyperrectangle class.      Represents a Cartesian product of intervals.      Par, Compute the total volume of the hyperrectangle.          Returns         -------, Produce two hyperrectangles by splitting.          In general, if you need to co, Return the minimum distance between input and points in the         hyperrectang, Return the maximum distance between input and points in the hyperrectangle., Compute the minimum distance between points in the two hyperrectangles., Compute the maximum distance between points in the two hyperrectangles., Rectangle

### Community 620 - "Community 620"
Cohesion: 0.18
Nodes (8): calculate_solid_angles(), Spherical Voronoi Code  .. versionadded:: 0.18.0, Calculates the Voronoi vertices and regions of the generators stored         in, Calculates the solid angles of plane triangles. Implements the method of     Van, Sort indices of the vertices to be (counter-)clockwise ordered.          Raises, Calculates the areas of the Voronoi regions.          For 2D point sets, the reg, Voronoi diagrams on the surface of a sphere.      .. versionadded:: 0.18.0, SphericalVoronoi

### Community 621 - "Community 621"
Cohesion: 0.13
Nodes (1): TestBasinHopping

### Community 622 - "Community 622"
Cohesion: 0.13
Nodes (1): TestMakeLSQNdBSpline

### Community 623 - "Community 623"
Cohesion: 0.17
Nodes (3): test_vector_constraints(), TestBounds, TestCobyla

### Community 624 - "Community 624"
Cohesion: 0.13
Nodes (1): TestChi2Contingency

### Community 625 - "Community 625"
Cohesion: 0.15
Nodes (3): check_czt(), check_zoom_fft(), test_1D()

### Community 626 - "Community 626"
Cohesion: 0.24
Nodes (12): get_arrays(), test_boxcox_llf(), test_combine_pvalues(), test_describe(), test_differential_entropy(), test_directional_stats(), test_entropy(), test_hypothesis_tests() (+4 more)

### Community 627 - "Community 627"
Cohesion: 0.16
Nodes (2): is_valid_dm_throw(), TestIsValidDM

### Community 628 - "Community 628"
Cohesion: 0.15
Nodes (7): Test for false positive on allclose in normalize() in         filter_design.py, Test the error cases., TestGammatone, TestIIRComb, TestIIRNotch, TestIIRPeak, TestNormalize

### Community 629 - "Community 629"
Cohesion: 0.15
Nodes (2): test_optimal_leaf_ordering(), TestLinkage

### Community 630 - "Community 630"
Cohesion: 0.13
Nodes (4): SAS code used to generate results for each sample:         DATA ACHE;         IN, vals = [24.5, 23.5,  26.4, 27.1, 29.9, 28.4, 34.2, 29.5, 32.2, 30.1,          26, Example sourced from:         https://www.itl.nist.gov/div898/handbook/prc/secti, TestTukeyHSD

### Community 631 - "Community 631"
Cohesion: 0.13
Nodes (1): TestZoom

### Community 632 - "Community 632"
Cohesion: 0.23
Nodes (14): _Test_random, _Test_random_ball, _Test_random_ball_approx, _Test_random_ball_approx_periodic, _Test_random_ball_far, _Test_random_ball_l1, _Test_random_ball_linf, _Test_random_far (+6 more)

### Community 633 - "Community 633"
Cohesion: 0.13
Nodes (3): TestBounds, TestQuadraticFunction, TestTrustRegion

### Community 634 - "Community 634"
Cohesion: 0.23
Nodes (1): TestRandomTable

### Community 635 - "Community 635"
Cohesion: 0.22
Nodes (1): TestMonteCarloHypothesisTest

### Community 636 - "Community 636"
Cohesion: 0.17
Nodes (1): TestDecimate

### Community 637 - "Community 637"
Cohesion: 0.13
Nodes (1): TestVectorstrength

### Community 638 - "Community 638"
Cohesion: 0.13
Nodes (3): tests that a warning is emitted when p is nan         p-value with t-distributio, tests that a p is 0 for datasets that cause p->nan         when t-distribution i, TestBrunnerMunzel

### Community 639 - "Community 639"
Cohesion: 0.13
Nodes (1): TestZscore

### Community 640 - "Community 640"
Cohesion: 0.16
Nodes (10): Test mix-n-match of int and float arguments, Skip tests for specific intersections of scipy.special functions      vs. backen, xp_capabilities updates the docstring in place.      Make sure it does so exactl, Test that numpy-specific out= and dtype= keyword arguments     of ufuncs still w, _skip_or_tweak_alternative_backends(), test_doc(), test_support_alternative_backends(), test_support_alternative_backends_hypothesis() (+2 more)

### Community 641 - "Community 641"
Cohesion: 0.14
Nodes (3): TestSawtoothWaveform, TestSquareWaveform, TestUnitImpulse

### Community 642 - "Community 642"
Cohesion: 0.18
Nodes (5): Airy, Comb, Erf, Expn, Loggamma

### Community 643 - "Community 643"
Cohesion: 0.26
Nodes (13): FishersNCHyp(), FishersNCHypInversion(), FishersNCHypRatioOfUnifoms(), MultiComplWalleniusNCHyp(), MultiFishersNCHyp(), MultiWalleniusNCHyp(), SetAccuracy(), StochasticLib3() (+5 more)

### Community 644 - "Community 644"
Cohesion: 0.16
Nodes (11): cobyla(), COBYLAResult, get_lincon(), This module provides Powell's COBYLA algorithm.  Translated from Zaikun Zhang's, This subroutine wraps the linear and bound constraints into a single constraint:, Among all the arguments, only CALCFC, M_NLCON, and X are obligatory. The others, preproc(), This is a module that preprocesses the inputs.  Translated from Zaikun Zhang's m (+3 more)

### Community 645 - "Community 645"
Cohesion: 0.15
Nodes (12): This module provides subroutines concerning the trust-region calculations of COB, This subroutine does the real calculations for trstlp, both stage 1 and stage 2., This function calculated an n-component vector d by the following two stages. In, This function updates the trust region radius according to RATIO and DNORM., trrad(), trstlp(), trstlp_sub(), qradd_Rdiag() (+4 more)

### Community 646 - "Community 646"
Cohesion: 0.29
Nodes (12): _laplace(), _laplace_normed(), _laplace_normed_sym(), _laplace_sym(), laplacian(), _laplacian_dense(), _laplacian_dense_flo(), _laplacian_sparse_flo() (+4 more)

### Community 647 - "Community 647"
Cohesion: 0.22
Nodes (7): DenseOutput, Dop853DenseOutput, Perform a single Runge-Kutta step.      This function computes a prediction of a, Base class for explicit Runge-Kutta methods., rk_step(), RkDenseOutput, RungeKutta

### Community 648 - "Community 648"
Cohesion: 0.19
Nodes (12): _backend_from_arg(), Context manager to set the backend within a fixed scope.      Upon entering the, Context manager to skip a backend within a fixed scope.      Within the context, Maps strings to known backends and validates the backend, Sets the global fft backend.      This utility method replaces the default backe, The default backend for fft calculations      Notes     -----     We use the dom, Register a backend for permanent use.      Registered backends have the lowest p, register_backend() (+4 more)

### Community 649 - "Community 649"
Cohesion: 0.25
Nodes (7): copy_input(), copy_output(), dataBuf(), exec_n(), general_c2r(), general_r2c(), transformBuf()

### Community 650 - "Community 650"
Cohesion: 0.18
Nodes (8): r"""     Ursem Waves objective function.      This class defines the Ursem Waves, r"""     Ursem 3 objective function.      This class defines the Ursem 3 [1]_ gl, r"""     Ursem 1 objective function.      This class defines the Ursem 1 [1]_ gl, r"""     Ursem 4 objective function.      This class defines the Ursem 4 [1]_ gl, Ursem01, Ursem03, Ursem04, UrsemWaves

### Community 651 - "Community 651"
Cohesion: 0.26
Nodes (10): activate_odepack_callback(), cleanup_odepack_callback(), compute_lrw_liw(), copy_array_to_fortran(), deactivate_odepack_callback(), ode_jacobian_thunk(), odepack_lsoda_step(), odepack_odeint() (+2 more)

### Community 652 - "Community 652"
Cohesion: 0.16
Nodes (8): BdfDenseOutput, change_D(), compute_R(), Compute the matrix for changing the differences array., # TODO: switch to csc_array after spmatrix is removed, Change differences array in-place when step size is changed., Solve the algebraic system resulting from BDF method., solve_bdf_system()

### Community 653 - "Community 653"
Cohesion: 0.16
Nodes (12): check_free_memory(), _get_mem_available(), _parse_size(), _pytest_has_xdist(), Generic test utilities., Check if the pytest-xdist plugin is installed, providing parallel tests, Check *free_mb* of memory is available, otherwise do pytest.skip, Get information about memory available, not counting swap. (+4 more)

### Community 654 - "Community 654"
Cohesion: 0.21
Nodes (13): get_region(), get_result(), get_result_no_mp(), get_results(), main(), _make_hyp2f1_test_case(), make_hyp2f1_test_cases(), This script evaluates scipy's implementation of hyp2f1 against mpmath's.  Author (+5 more)

### Community 655 - "Community 655"
Cohesion: 0.14
Nodes (14): _aberth(), _bessel_poly(), _bessel_zeros(), besselap(), _campos_zeros(), _falling_factorial(), _norm_factor(), r"""     Return the factorial of `x` to the `n` falling.      This is defined as (+6 more)

### Community 656 - "Community 656"
Cohesion: 0.14
Nodes (14): bessel(), butter(), cheby1(), cheby2(), ellip(), iirdesign(), iirfilter(), Complete IIR digital and analog filter design.      Given passband and stopband (+6 more)

### Community 657 - "Community 657"
Cohesion: 0.14
Nodes (8): KDTree, kd-tree for quick nearest-neighbor lookup.      This class provides an index int, r"""Query the kd-tree for nearest neighbors.          Parameters         -------, Find all points within distance r of point(s) x.          Parameters         ---, Find all pairs of points between `self` and `other` whose distance is         at, Find all pairs of points in `self` whose distance is at most r.          Paramet, Count how many nearby pairs can be formed.          Count the number of pairs ``, Compute a sparse distance matrix.          Computes a distance matrix between tw

### Community 658 - "Community 658"
Cohesion: 0.15
Nodes (4): MultiUFunc, Set `key` method by decorating a function., Set `resolve_out_shapes` method by decorating a function., Resolve to a ufunc based on keyword arguments.

### Community 659 - "Community 659"
Cohesion: 0.16
Nodes (14): _gen_roots_and_weights(), legendre(), r"""Gauss-Gegenbauer quadrature.      Compute the sample points and weights for, [x,w] = gen_roots_and_weights(n,an_func,sqrt_bn_func,mu)      Returns the roots, r"""Gauss-Jacobi quadrature.      Compute the sample points and weights for Gaus, r"""Gauss-Legendre quadrature.      Compute the sample points and weights for Ga, r"""Legendre polynomial.      Defined to be the solution of      .. math::, r"""Gauss-Legendre (shifted) quadrature.      Compute the sample points and weig (+6 more)

### Community 660 - "Community 660"
Cohesion: 0.22
Nodes (13): _bin_edges(), _bin_numbers(), _bincount(), binned_statistic(), binned_statistic_2d(), binned_statistic_dd(), _calc_binned_statistic(), _create_binned_data() (+5 more)

### Community 661 - "Community 661"
Cohesion: 0.20
Nodes (12): chatterjeexi(), _chatterjeexi_iv(), r"""Calculate a Spearman rho correlation coefficient with associated p-value., r"""     Computes the Theil-Sen estimator for a set of points (x, y).      `thei, r"""     Computes the Siegel estimator for a set of points (x, y).      `siegels, r"""Compute the xi correlation and perform a test of independence.      The xi c, _robust_slopes(), siegelslopes() (+4 more)

### Community 662 - "Community 662"
Cohesion: 0.19
Nodes (12): _a_ij_Aij_Dij2(), _Aij(), _compute_outer_prob_inside_method(), _concordant_pairs(), _Dij(), _discordant_pairs(), Sum of lower-left and upper-right blocks of contingency table., Twice the number of concordant pairs, excluding ties. (+4 more)

### Community 663 - "Community 663"
Cohesion: 0.14
Nodes (1): _TestSlicing

### Community 664 - "Community 664"
Cohesion: 0.14
Nodes (2): Test parity follows well known identity.          en.wikipedia.org/wiki/Stirling, TestStirling2

### Community 665 - "Community 665"
Cohesion: 0.14
Nodes (1): TestTrigonometric

### Community 666 - "Community 666"
Cohesion: 0.19
Nodes (1): TestErf

### Community 667 - "Community 667"
Cohesion: 0.14
Nodes (1): TestContinuedFraction

### Community 669 - "Community 669"
Cohesion: 0.14
Nodes (1): TestCdist

### Community 670 - "Community 670"
Cohesion: 0.14
Nodes (1): TestStudentizedRange

### Community 671 - "Community 671"
Cohesion: 0.14
Nodes (1): TestTruncnorm

### Community 672 - "Community 672"
Cohesion: 0.14
Nodes (2): _complex_correlate(), Utility to perform a reference complex-valued convolutions.      When convolve==

### Community 673 - "Community 673"
Cohesion: 0.14
Nodes (5): Test the fs and nyq keywords., Test firwin2 when window=None., Test firwin2 for calculating Type IV filters, Test firwin2 for calculating Type III filters, TestFirwin2

### Community 674 - "Community 674"
Cohesion: 0.15
Nodes (3): _check_loc_scale_mle_fit(), test_non_default_loc_scale_mle_fit(), TestFitResult

### Community 675 - "Community 675"
Cohesion: 0.25
Nodes (2): TestGammainc, TestGammaincc

### Community 676 - "Community 676"
Cohesion: 0.29
Nodes (11): _assert_allclose_sparse(), check_int_type(), _check_laplacian_dtype(), _check_laplacian_dtype_none(), _check_symmetric_graph_laplacian(), _explicit_laplacian(), test_asymmetric_laplacian(), test_format() (+3 more)

### Community 677 - "Community 677"
Cohesion: 0.22
Nodes (3): Rosenbrock function.      The following optimization problem:         minimize s, Rosenbrock, TestHessianUpdateStrategy

### Community 678 - "Community 678"
Cohesion: 0.16
Nodes (5): calculate_maximum_distances(), eager, TestFclusterData, TestLeaders, TestMaxDists

### Community 679 - "Community 679"
Cohesion: 0.24
Nodes (7): ODECheckParameterUse, Call an ode-class solver with several cases of parameter use., TestDOP853CheckParameterUse, TestDOPRI5CheckParameterUse, TestLSODACheckParameterUse, TestVODECheckParameterUse, TestZVODECheckParameterUse

### Community 680 - "Community 680"
Cohesion: 0.16
Nodes (3): do_solve(), Tests for the linalg._isolve.lgmres module, TestLGMRES

### Community 681 - "Community 681"
Cohesion: 0.18
Nodes (1): TestFactorized

### Community 682 - "Community 682"
Cohesion: 0.21
Nodes (3): TestExpit, TestLogExpit, TestLogit

### Community 683 - "Community 683"
Cohesion: 0.18
Nodes (10): dummy_func(), pressure_network(), pressure_network_fun_and_grad(), pressure_network_jacobian(), Unit tests for optimization routines from minpack.py., A function that returns an array of ones of the given shape.     `x` is ignored., Evaluate non-linear equation system representing     the pressures and flows in, Return the jacobian of the equation system F(flow_rates)     computed by `pressu (+2 more)

### Community 684 - "Community 684"
Cohesion: 0.16
Nodes (7): _cached_sample_problem(), get_sample_problem(), get_sample_problem_complex(), Asymmetric matrix should raise `ValueError` when check=True, Non-symmetric (non-Hermitian) preconditioner M        should raise ValueError wh, test_asymmetric_fail(), test_asymmetric_preconditioner_fail()

### Community 685 - "Community 685"
Cohesion: 0.14
Nodes (1): TestApproxDerivativeLinearOperator

### Community 686 - "Community 686"
Cohesion: 0.14
Nodes (2): Ensure that we can use pathlib.Path objects in all relevant IO functions., TestPaths

### Community 687 - "Community 687"
Cohesion: 0.18
Nodes (6): check_shape(), test_deriv_shapes(), test_derivs_shapes(), test_shapes(), TestTaylor, TestZeroSizeArrays

### Community 688 - "Community 688"
Cohesion: 0.16
Nodes (3): TestFixedQuad, TestLebedev, TestQMCQuad

### Community 689 - "Community 689"
Cohesion: 0.16
Nodes (4): dist0, dist1, dist2, dist3

### Community 690 - "Community 690"
Cohesion: 0.16
Nodes (4): _check_action(), # TODO: special expert should correct, test_errstate(), test_seterr()

### Community 691 - "Community 691"
Cohesion: 0.20
Nodes (4): Test the dot-product for type preservation and consistency., TestLaplacianNd, TestMikotaPair, TestSakurai

### Community 692 - "Community 692"
Cohesion: 0.21
Nodes (5): setup_test_file(), test_make_stream(), test_read(), test_tell_seek(), TestZlibInputStream

### Community 693 - "Community 693"
Cohesion: 0.14
Nodes (5): Tests for Part 1: sklearn-like wrappers with internal .pxd and int->blas_int., TestBlasIntSize, TestBLASLevel1, TestBLASLevel3, TestLAPACK

### Community 694 - "Community 694"
Cohesion: 0.14
Nodes (12): Test cases of test_data that do not reach relative accuracy of 1e-11, Test cases of test_data that do not reach relative accuracy of 1e-11      Here w, Test that log_wright_bessel equals log of wright_bessel., Test for log_wright_bessel, in particular for large x., Test relation of wright_bessel and modified bessel function iv.      iv(z) = (1/, Test functional relation of wright_bessel.      Phi(a, b-1, z) = a*z*Phi(a, b+a,, test_log_wright_bessel(), test_log_wright_bessel_same_as_wright_bessel() (+4 more)

### Community 695 - "Community 695"
Cohesion: 0.15
Nodes (8): loadarff(), MetaData, Read the header of the iterable ofile., Small container to keep useful information on an ARFF dataset.      Knows about, Return the list of attribute names.          Returns         -------         att, Return the list of attribute types.          Returns         -------         att, Read an arff file.      The data is returned as a record array, which can be acc, read_header()

### Community 696 - "Community 696"
Cohesion: 0.15
Nodes (1): NdimageInterpolation

### Community 697 - "Community 697"
Cohesion: 0.33
Nodes (10): CFishersNCHypergeometric(), lng(), loop(), MakeTable(), mean(), mode(), moments(), probability() (+2 more)

### Community 698 - "Community 698"
Cohesion: 0.28
Nodes (12): conv(), expand_sub(), find_and_remove_repl_patterns(), find_repl_patterns(), main(), parse_structure(), process_file(), process_str() (+4 more)

### Community 699 - "Community 699"
Cohesion: 0.15
Nodes (1): TestOddsRatio

### Community 700 - "Community 700"
Cohesion: 0.15
Nodes (10): Exception, ParseError, _NoConvergence, _TemplateBreak, _TemplateContinue, K-means clustering and vector quantization (:mod:`scipy.cluster.vq`) ===========, ClusterError, _missing_raise() (+2 more)

### Community 701 - "Community 701"
Cohesion: 0.15
Nodes (12): fftfreq(), fftshift(), ifftshift(), next_fast_len(), prev_fast_len(), Find the next fast size of input data to ``fft``, for zero-padding, etc.      Sc, Return the Discrete Fourier Transform sample frequencies.      The returned floa, Return the Discrete Fourier Transform sample frequencies     (for usage with rff (+4 more)

### Community 702 - "Community 702"
Cohesion: 0.23
Nodes (8): cleanup_dvode_callback(), copy_array_to_fortran(), copy_complex_array_to_fortran(), dvode_jacobian_thunk(), dvode_wrapper(), setup_dvode_callback(), zvode_jacobian_thunk(), zvode_wrapper()

### Community 703 - "Community 703"
Cohesion: 0.19
Nodes (8): NdPPoly, Construct a new piecewise polynomial representing the derivative.          Param, Construct a new piecewise polynomial representing the antiderivative.          P, Piecewise tensor product polynomial.      The value at point ``xp = (x', y', z',, Compute 1-D derivative along a selected dimension in-place         May result to, Compute 1-D antiderivative along a selected dimension         May result to non-, r"""         Compute NdPPoly representation for one dimensional definite integra, Construct a new piecewise polynomial representing the antiderivative.          A

### Community 704 - "Community 704"
Cohesion: 0.18
Nodes (7): predict_factor(), RadauDenseOutput, Predict by which factor to increase/decrease the step size.      The algorithm i, # TODO: use I = eye_array(self.n, format="csc") after spmatrix removed, # TODO: Use csc_array after spmatrix removed, Solve the collocation system.      Parameters     ----------     fun : callable, solve_collocation_system()

### Community 705 - "Community 705"
Cohesion: 0.26
Nodes (12): check_ruff_version(), diff_files(), find_branch_point(), main(), List commits in reverse chronological order.      Only the first `num_commits` a, Find when the current branch split off from the given branch.      It is based o, Find the diff since the given SHA., rev_list() (+4 more)

### Community 706 - "Community 706"
Cohesion: 0.21
Nodes (10): fourier_ellipsoid(), fourier_gaussian(), fourier_shift(), fourier_uniform(), _get_output_fourier(), _get_output_fourier_complex(), Multidimensional uniform fourier filter.      The array is multiplied with the F, Multidimensional ellipsoid Fourier filter.      The array is multiplied with the (+2 more)

### Community 707 - "Community 707"
Cohesion: 0.29
Nodes (5): CachedGet, get_issues(), get_milestones(), GithubGet, main()

### Community 708 - "Community 708"
Cohesion: 0.15
Nodes (13): check_COLA_signature(), check_NOLA_signature(), coherence_signature(), csd_signature(), istft_signature(), periodogram_signature(), Handle `window` being a str or a tuple or an array-like., resample_poly_signature() (+5 more)

### Community 709 - "Community 709"
Cohesion: 0.17
Nodes (13): findfreqs(), freqs(), freqs_zpk(), freqz_zpk(), group_delay(), _is_int_type(), _logspace(), Find array of frequencies for computing the response of an analog filter.      P (+5 more)

### Community 710 - "Community 710"
Cohesion: 0.23
Nodes (12): _logdet_difference_matrix(), _polynomial_fit(), Solve the equation ``a @ x = b`` for ``x``,  where ``a`` is the      Hermitian p, Polynomial fit equivalent to WH for lamb -> infinity., Solve the WH optimization problem via the normal equations.          A @ x = y, Logarithm of the determinant of the difference matrix.      If D is the differen, Calculate the restricted maximum likelihood (REML).          Parameters     ----, r"""     Whittaker-Henderson (WH) smoothing/graduation of a discrete signal. (+4 more)

### Community 711 - "Community 711"
Cohesion: 0.15
Nodes (13): _bessel_diff_formula(), h1vp(), h2vp(), ivp(), jvp(), kvp(), Compute derivatives of modified Bessel functions of the first kind.      Compute, Compute derivatives of Hankel function H1v(z) with respect to `z`.      Paramete (+5 more)

### Community 712 - "Community 712"
Cohesion: 0.18
Nodes (12): chebyu(), gegenbauer(), jacobi(), r"""Gegenbauer (ultraspherical) polynomial.      Defined to be the solution of t, r"""Chebyshev polynomial of the second kind.      Defined to be the solution of, r"""Shifted Chebyshev polynomial of the first kind.      Defined as :math:`T^*_n, r"""Shifted Chebyshev polynomial of the second kind.      Defined as :math:`U^*_, r"""Jacobi polynomial.      Defined to be the solution of      .. math:: (+4 more)

### Community 713 - "Community 713"
Cohesion: 0.17
Nodes (11): genlaguerre(), laguerre(), orthopoly1d, r"""Laguerre polynomial.      Defined to be the solution of      .. math::, r"""     Shifted Legendre polynomial.      Defined as :math:`P^*_n(x) = P_n(2x -, r"""Gauss-generalized Laguerre quadrature.      Compute the sample points and we, r"""Generalized (associated) Laguerre polynomial.      Defined to be the solutio, r"""Gauss-Laguerre quadrature.      Compute the sample points and weights for Ga (+3 more)

### Community 714 - "Community 714"
Cohesion: 0.21
Nodes (7): assert_func_equal(), FuncData, MissingModule, Check the special function against the data., Enable special function errors (such as underflow, overflow,     loss of precisi, Data set for checking a special function.      Parameters     ----------     fun, with_special_errors()

### Community 715 - "Community 715"
Cohesion: 0.26
Nodes (12): ccgs(), cmgs(), creorth(), dcgs(), dmgs(), dreorth(), scgs(), smgs() (+4 more)

### Community 716 - "Community 716"
Cohesion: 0.33
Nodes (10): maxSortDown(), maxSortUp(), Mediator, MediatorInsert(), minSortDown(), minSortUp(), mmCmpExch(), mmexchange() (+2 more)

### Community 717 - "Community 717"
Cohesion: 0.24
Nodes (12): association(), chi2_contingency(), _chi2_monte_carlo_method(), _chi2_permutation_method(), _chi2_resampling_methods(), expected_freq(), margins(), Contingency table functions (:mod:`scipy.stats.contingency`) =================== (+4 more)

### Community 718 - "Community 718"
Cohesion: 0.15
Nodes (12): _pinv_1d(), A helper function for computing the pseudoinverse.      Parameters     ---------, Create a frozen inverse Wishart distribution.          Parameters         ------, Create a frozen SO(N) distribution.          Parameters         ----------, Create a frozen O(N) distribution.          Parameters         ----------, Create a frozen random correlation matrix distribution.          Parameters, Create a frozen (U(N)) n-dimensional unitary matrix distribution.          Param, Initialize a multivariate t-distributed random variable.          Parameters (+4 more)

### Community 719 - "Community 719"
Cohesion: 0.29
Nodes (12): estimated_cdf(), _estimated_cdf_hf(), _post_quantile(), quantile(), _quantile_bc(), _quantile_hd(), _quantile_hf(), _quantile_iv() (+4 more)

### Community 720 - "Community 720"
Cohesion: 0.26
Nodes (5): _correction_sign(), _wilcoxon_iv(), _wilcoxon_nd(), _wilcoxon_statistic(), WilcoxonDistribution

### Community 721 - "Community 721"
Cohesion: 0.15
Nodes (2): Tests fancy indexing features.  The tests for any matrix formats     that implem, _TestFancyIndexing

### Community 722 - "Community 722"
Cohesion: 0.15
Nodes (1): TestCensoredData

### Community 723 - "Community 723"
Cohesion: 0.22
Nodes (1): TestCOBYQA

### Community 724 - "Community 724"
Cohesion: 0.17
Nodes (6): Create the full matrix `self.fullmat` and            the corresponding band matr, Create the full matrix `self.fullmat`, `self.d`, and `self.e`., Test error conditions., Compare eigenvalues of eigvalsh_tridiagonal with those of eig., Compare eigenvalues and eigenvectors of eigh_tridiagonal            with those o, TestEigTridiagonal

### Community 725 - "Community 725"
Cohesion: 0.27
Nodes (1): TestOrdQZ

### Community 726 - "Community 726"
Cohesion: 0.29
Nodes (12): generate_random_token(), get_elements(), test_add(), test_binary_tree(), test_contains(), test_element_not_present(), test_equal_size_ordering(), test_init() (+4 more)

### Community 727 - "Community 727"
Cohesion: 0.22
Nodes (2): is_valid_y_throw(), TestIsValidY

### Community 728 - "Community 728"
Cohesion: 0.15
Nodes (5): Different author, different style, different tests..., Test that invalid cutoff argument raises ValueError., Test that attempt to create a highpass filter with an even number         of tap, Test degenerate pass_zero cases., TestFirWinMore

### Community 729 - "Community 729"
Cohesion: 0.19
Nodes (3): TestFirls, TestMinimumPhase, TestRemez

### Community 730 - "Community 730"
Cohesion: 0.15
Nodes (1): TestNdimageFourier

### Community 731 - "Community 731"
Cohesion: 0.21
Nodes (4): TestComplexOde, TestOde, TestODEClass, TestOdeint

### Community 732 - "Community 732"
Cohesion: 0.27
Nodes (2): BroydenTridiagonal, SparseMixin

### Community 733 - "Community 733"
Cohesion: 0.15
Nodes (5): assoc_legendre_p_1_0(), assoc_legendre_p_3_0(), TestAssocLegendreP, TestLegendreP, TestSphLegendreP

### Community 734 - "Community 734"
Cohesion: 0.17
Nodes (5): @pytest.mark.parametrize("m_max", [3])     @pytest.mark.parametrize("n_max", [5], algorithm for real arguments changes at 1.0001            test against analytica, Tests for correct output shapes., Tests for correct output shapes and dtypes., TestLegendreFunctions

### Community 735 - "Community 735"
Cohesion: 0.15
Nodes (1): _assert_infeasible()

### Community 736 - "Community 736"
Cohesion: 0.15
Nodes (2): # TODO: check that implementation is correct., TestQuantiles

### Community 737 - "Community 737"
Cohesion: 0.15
Nodes (3): Test functions for the sparse.linalg.norm module, TestNorm, TestVsNumpyNorm

### Community 738 - "Community 738"
Cohesion: 0.26
Nodes (2): Check that spline coefficients satisfy the continuity and boundary         condi, TestCubicSpline

### Community 739 - "Community 739"
Cohesion: 0.17
Nodes (11): is_unexpected(), This test script is adopted from:     https://github.com/numpy/numpy/blob/main/n, Check if this needs to be considered., Test that we don't add anything that looks like a new public module by     accid, Assert that output of dir has only one "testing/tester"     attribute without du, Method checking all objects. The pkgutil-based method in     `test_all_modules_a, Check that all submodules listed higher up in this file can be imported     Note, test_all_modules_are_expected() (+3 more)

### Community 740 - "Community 740"
Cohesion: 0.18
Nodes (4): Check that utility functions work., Test that incremental mode gives the same volume/area as         non-incremental, Check that a triangulation has reasonable barycentric transforms, TestUtilities

### Community 741 - "Community 741"
Cohesion: 0.15
Nodes (1): TestQuadVec

### Community 742 - "Community 742"
Cohesion: 0.15
Nodes (7): Spatial Transformations (:mod:`scipy.spatial.transform`) =======================, Represent as rotation vectors.          A rotation vector is a 3 dimensional vec, Invert this rotation.          Composition of a rotation with its inverse result, Spherical Linear Interpolation of Rotations.      The interpolation between cons, Interpolate rotations.          Compute the interpolated rotations at the given, Initialize from quaternions.          Rotations in 3 dimensions can be represent, Slerp

### Community 743 - "Community 743"
Cohesion: 0.23
Nodes (6): Bench, direct_diff(), direct_hilbert(), direct_shift(), direct_tilbert(), Benchmark functions for fftpack.pseudo_diffs module

### Community 744 - "Community 744"
Cohesion: 0.23
Nodes (2): MemUsage, StructArr

### Community 745 - "Community 745"
Cohesion: 0.18
Nodes (2): MaximumBipartiteMatching, MinWeightFullBipartiteMatching

### Community 746 - "Community 746"
Cohesion: 0.17
Nodes (4): HBFile, Gives the header corresponding to this instance as a string., _read_hb_data(), _write_data()

### Community 747 - "Community 747"
Cohesion: 0.20
Nodes (3): qh_memcheck(), qh_meminit(), qh_memstatistics()

### Community 748 - "Community 748"
Cohesion: 0.26
Nodes (7): qh_errexit(), qh_errprint(), qh_printhelp_degenerate(), qh_printhelp_internal(), qh_printhelp_singular(), qh_printhelp_topology(), qh_printhelp_wide()

### Community 749 - "Community 749"
Cohesion: 0.21
Nodes (9): qr(), qr_multiply(), QR decomposition functions., Call a LAPACK routine, determining lwork automatically and handling     error re, Calculate the QR decomposition and multiply Q with a matrix.      Calculate the, Compute QR decomposition of a matrix.      Calculate the decomposition ``A = Q R, Compute RQ decomposition of a matrix.      Calculate the decomposition ``A = R Q, rq() (+1 more)

### Community 750 - "Community 750"
Cohesion: 0.18
Nodes (9): generic_filter1d(), maximum_filter1d(), minimum_filter1d(), Calculate a 1-D minimum filter along the given axis.      The lines of the array, Calculate a 1-D maximum filter along the given axis.      The lines of the array, Filter an array with a vectorized Python callable as the kernel.      Parameters, Calculate a 1-D filter along the given axis.      `generic_filter1d` iterates ov, vectorized_filter() (+1 more)

### Community 751 - "Community 751"
Cohesion: 0.20
Nodes (6): AdaptiveStepsize, Do one Monte Carlo iteration          Randomly displace the coordinates, minimiz, Class to implement adaptive stepsize.      This class wraps the step taking clas, called by basinhopping to report the result of the step, Assuming the local search underlying res_new was successful:         If new ener, f_new and f_old are mandatory in kwargs

### Community 752 - "Community 752"
Cohesion: 0.23
Nodes (11): compute_a(), compute_alpha(), compute_d(), compute_g(), eta(), main(), Precompute coefficients of Temme's asymptotic expansion for gammainc.  This take, g_k from DLMF 5.11.3/5.11.5 (+3 more)

### Community 753 - "Community 753"
Cohesion: 0.26
Nodes (7): eff(), freq_eval(), lagrange_interp(), pre_remez(), remez(), _sigtools_remez(), wate()

### Community 754 - "Community 754"
Cohesion: 0.24
Nodes (11): cdist(), _cdist_callable(), CDistMetricWrapper, _convert_to_type(), _np_pdist(), _pdist_callable(), PDistMetricWrapper, _prepare_out_argument() (+3 more)

### Community 755 - "Community 755"
Cohesion: 0.21
Nodes (9): chebys(), A collection of functions to find the weights and abscissas for Gaussian Quadrat, r"""Gauss-Chebyshev (second kind) quadrature.      Computes the sample points an, r"""Gauss-Chebyshev (second kind) quadrature.      Compute the sample points and, r"""Chebyshev polynomial of the second kind on :math:`[-2, 2]`.      Defined as, r"""Gauss-Chebyshev (second kind, shifted) quadrature.      Computes the sample, roots_chebys(), roots_chebyu() (+1 more)

### Community 756 - "Community 756"
Cohesion: 0.41
Nodes (11): etdfs(), finalize_disjoint_sets(), find(), initialize_disjoint_sets(), link(), make_set(), mxCallocInt(), nr_etdfs() (+3 more)

### Community 757 - "Community 757"
Cohesion: 0.21
Nodes (8): _dirichlet_check_input(), _dirichlet_check_parameters(), dirichlet_gen, r"""     A Dirichlet random variable.      The ``alpha`` keyword specifies the c, The Dirichlet probability density function.          Parameters         --------, Variance of the Dirichlet distribution.          Parameters         ----------, Covariance matrix of the Dirichlet distribution.          Parameters         ---, Draw random samples from a Dirichlet distribution.          Parameters         -

### Community 758 - "Community 758"
Cohesion: 0.21
Nodes (5): random_table_gen, r"""     Contingency tables from independent samples with fixed marginal sums., Probability of table to occur in the distribution.          Parameters         -, Draw random tables with fixed column and row marginals.          Parameters, Compute the number of samples to be drawn and the shape of the output

### Community 759 - "Community 759"
Cohesion: 0.20
Nodes (1): TestDIA

### Community 760 - "Community 760"
Cohesion: 0.30
Nodes (3): TestBdtr, TestBdtrc, TestBdtri

### Community 761 - "Community 761"
Cohesion: 0.17
Nodes (2): Tests if hstack properly promotes to indices and indptr arrays to np.int64     w, test_csr_hstack_int64()

### Community 762 - "Community 762"
Cohesion: 0.21
Nodes (3): _random_hermitian_matrix(), Generate random sym/hermitian array of the given size n, TestEigh

### Community 763 - "Community 763"
Cohesion: 0.17
Nodes (1): TestJaccard

### Community 764 - "Community 764"
Cohesion: 0.20
Nodes (4): TestExp1, TestExpi, TestExpn, TestScaledExp1

### Community 765 - "Community 765"
Cohesion: 0.17
Nodes (2): Test functions for the sparse.linalg._krylov_funm module., TestKrylovFunmv

### Community 766 - "Community 766"
Cohesion: 0.20
Nodes (2): do_solve(), TestGCROTMK

### Community 767 - "Community 767"
Cohesion: 0.20
Nodes (3): calculate_maximum_inconsistencies(), TestMaxInconsts, TestMaxRStat

### Community 768 - "Community 768"
Cohesion: 0.20
Nodes (1): TestIsIsomorphic

### Community 769 - "Community 769"
Cohesion: 0.17
Nodes (1): TestIsMonotonic

### Community 770 - "Community 770"
Cohesion: 0.17
Nodes (1): TestRotate

### Community 771 - "Community 771"
Cohesion: 0.20
Nodes (6): ball_consistency, distance_box(), _Test_random_ball_far_periodic, _Test_random_ball_largep_issue9890, _Test_random_ball_periodic, two_trees_consistency

### Community 773 - "Community 773"
Cohesion: 0.24
Nodes (4): _assert_iteration_limit_reached(), nontrivial_problem(), TestAutoscaleRS, TestLinprogRSCommon

### Community 774 - "Community 774"
Cohesion: 0.20
Nodes (5): generic_callback_test(), LinprogHiGHSTests, Test that `linprog` now solves a poorly-scaled problem, TestLinprogHiGHSIPM, very_random_gen()

### Community 775 - "Community 775"
Cohesion: 0.17
Nodes (12): _check_eigen(), _check_fiedler(), Test ``m - m_excluded`` eigenvalues and eigenvectors of     diagonal matrices of, Check if the eigenvalue residual is small., Check the Fiedler vector computation., Check the dense workaround path for small matrices., Check the dense workaround path avoided for non-small matrices., Check eigsh vs. lobpcg consistency. (+4 more)

### Community 776 - "Community 776"
Cohesion: 0.35
Nodes (10): _make_readerlike(), _make_tag(), Testing mio5_utils Cython module, Makes a simple matlab tag, full or sde, test_read_numeric(), test_read_numeric_writeable(), test_read_stream(), test_read_tag() (+2 more)

### Community 778 - "Community 778"
Cohesion: 0.17
Nodes (6): Generate a series of gaussians and attempt to find the peak locations., Verify that peak locations are (approximately) found         for a series of gau, Verify that no peak is found in         data that's just noise., Verify that window_size is passed correctly to private function and         affe, Verify that the `width` argument         in `find_peaks_cwt` can be a float, TestFindPeaksCwt

### Community 779 - "Community 779"
Cohesion: 0.18
Nodes (2): Check that every line in arr1 is only once in arr2, Test_HalfspaceIntersection

### Community 780 - "Community 780"
Cohesion: 0.18
Nodes (5): _add_inc_data(), assert_unordered_tuple_list_equal(), # NOTE: testing exact degeneracy is less predictable than this, Generate incremental datasets from basic data sets, Test_Qhull

### Community 781 - "Community 781"
Cohesion: 0.17
Nodes (11): _TestDSTBase, _TestDSTIBase, TestDSTIDouble, TestDSTIFloat, TestDSTIIDouble, TestDSTIIFloat, TestDSTIIIDouble, TestDSTIIIFloat (+3 more)

### Community 782 - "Community 782"
Cohesion: 0.17
Nodes (1): TestGSTD

### Community 783 - "Community 783"
Cohesion: 0.26
Nodes (5): compute_frequency(), Use an array of coefficients instead of a poly1d., Use a list of coefficients instead of a poly1d., Compute theta'(t)/(2*pi), where theta'(t) is the derivative of theta(t)., TestSweepPoly

### Community 784 - "Community 784"
Cohesion: 0.20
Nodes (10): cpenmsg(), fmsg(), get_info_string(), This module provides some functions that print messages to terminal/files.  Tran, This function prints messages when RHO is updated., This function prints a message when CPEN is updated., This subroutine prints messages for each evaluation of the objective function., This function prints messages at return. (+2 more)

### Community 785 - "Community 785"
Cohesion: 0.29
Nodes (7): Py_gssv(), Py_gstrf(), Py_gstrs(), XDestroy_CompCol_Matrix(), XDestroy_SuperMatrix_Store(), XDestroy_SuperNode_Matrix(), XStatFree()

### Community 786 - "Community 786"
Cohesion: 0.25
Nodes (4): emulu(), full_multiplication(), _umul128(), umul128_generic()

### Community 787 - "Community 787"
Cohesion: 0.22
Nodes (6): Katsuura, Keane, Kowalik, r"""     Kowalik objective function.      This class defines the Kowalik [1]_ gl, r"""     Keane objective function.      This class defines the Keane [1]_ global, r"""     Katsuura objective function.      This class defines the Katsuura [1]_

### Community 788 - "Community 788"
Cohesion: 0.22
Nodes (6): NeedleEye, NewFunction01, NewFunction02, r"""     NewFunction02 objective function.      This class defines the NewFuncti, r"""     NewFunction01 objective function.      This class defines the NewFuncti, r"""     NeedleEye objective function.      This class defines the Needle-Eye [1

### Community 789 - "Community 789"
Cohesion: 0.22
Nodes (6): Qing, Quadratic, Quintic, r"""     Quadratic objective function.      This class defines the Quadratic [1], r"""     Qing objective function.      This class defines the Qing [1]_ global o, r"""     Quintic objective function.      This class defines the Quintic [1]_ gl

### Community 790 - "Community 790"
Cohesion: 0.27
Nodes (4): Preliminary module to handle Fortran formats for IO. Does not use this outside s, \         Parameters         ----------         width : int             number o, Token, Tokenizer

### Community 791 - "Community 791"
Cohesion: 0.29
Nodes (7): dataToString(), equal_nocase(), intToString(), parse_words_from_file(), stringToData(), tolower(), trim()

### Community 792 - "Community 792"
Cohesion: 0.18
Nodes (11): _get_fitpack_packed_column(), _lsq_clamp_preprocess(), _lsq_solve_qr(), _lsq_solve_qr_clamp_values(), _lsq_solve_qr_for_root_rati_periodic(), Apply the clamp preprocessing to packed matrix + RHS for the QR path.          A, Solve for the LSQ spline coeffs given x, y and knots.      `y` is always 2D: for, Solve for the LSQ spline coeffs given x, y, knots and clamp_values.          `y` (+3 more)

### Community 793 - "Community 793"
Cohesion: 0.24
Nodes (6): assert_no_overwrite(), _FakeMatrix, _FakeMatrix2, _get_array(), Get a test array of given shape and data type.     Returned NxN matrices are pos, Test that a call does not overwrite its input arguments

### Community 794 - "Community 794"
Cohesion: 0.25
Nodes (4): Formula Visita from p. 405 of reference [2], Class that implements within a Markov chain the strategy for location     accept, Based on the step in the strategy chain, new coordinates are         generated b, StrategyChain

### Community 795 - "Community 795"
Cohesion: 0.22
Nodes (5): Rule, BadErrorRule, Tests related to the general Rule interface (currently private)., A rule with fake high error so that cubature will keep on subdividing., TestRules

### Community 796 - "Community 796"
Cohesion: 0.18
Nodes (11): bode_signature(), cont2discrete_signature(), dimpulse_signature(), dlsim_signature(), dstep_signature(), freqresp_signature(), impulse_signature(), lsim_signature() (+3 more)

### Community 797 - "Community 797"
Cohesion: 0.25
Nodes (10): _fit_edge(), _fit_edges_polyfit(), _polyder(), Compute the coefficients for a 1-D Savitzky-Golay FIR filter.      Parameters, Differentiate polynomials represented with coefficients.      p must be a 1-D or, Given an N-d array `x` and the specification of a slice of `x` from     `window_, Use polynomial interpolation of x at the low and high ends of the axis     to fi, Apply a Savitzky-Golay filter to an array.      This is a 1-D filter. If `x`  ha (+2 more)

### Community 799 - "Community 799"
Cohesion: 0.20
Nodes (9): r"""Spherical Bessel function of the second kind or its derivative.      Defined, r"""Modified spherical Bessel function of the first kind or its derivative., r"""Modified spherical Bessel function of the second kind or its derivative., r"""Spherical Bessel function of the first kind or its derivative.      Defined, spherical_in(), spherical_jn(), spherical_kn(), spherical_kn_reflection() (+1 more)

### Community 801 - "Community 801"
Cohesion: 0.33
Nodes (9): clanbpro(), csafescal(), dlanbpro(), dsafescal(), int_max(), slanbpro(), ssafescal(), zlanbpro() (+1 more)

### Community 802 - "Community 802"
Cohesion: 0.33
Nodes (10): matrix_squareroot_c(), matrix_squareroot_d(), matrix_squareroot_s(), matrix_squareroot_z(), sqrtm_recursion_c(), sqrtm_recursion_d(), sqrtm_recursion_s(), sqrtm_recursion_z() (+2 more)

### Community 803 - "Community 803"
Cohesion: 0.20
Nodes (2): _apply_filter(), _apply_filter_gain()

### Community 804 - "Community 804"
Cohesion: 0.24
Nodes (9): _cmpkey(), InvalidVersion, parse(), _parse_letter_version(), _parse_local_version(), Initialize a Version object.          :param version:             The string rep, Parse the given version string.      >>> parse('1.0.dev1')     <Version('1.0.dev, Takes a string like abc.1.twelve and turns it into ("abc", 1, "twelve"). (+1 more)

### Community 805 - "Community 805"
Cohesion: 0.18
Nodes (2): Tests for betainc, betaincinv, betaincc, betainccinv., TestBetaInc

### Community 806 - "Community 806"
Cohesion: 0.18
Nodes (1): TestHyper

### Community 807 - "Community 807"
Cohesion: 0.22
Nodes (2): Test_Metropolis, Test_Storage

### Community 808 - "Community 808"
Cohesion: 0.18
Nodes (1): TestFBLAS1Simple

### Community 809 - "Community 809"
Cohesion: 0.18
Nodes (1): TestFpchec

### Community 810 - "Community 810"
Cohesion: 0.27
Nodes (1): TestMakeND

### Community 811 - "Community 811"
Cohesion: 0.18
Nodes (2): TestNegativeBinomialFunctions, TestNoncentralChiSquaredFunctions

### Community 813 - "Community 813"
Cohesion: 0.18
Nodes (3): TestConvertTemperature, TestLambdaToNu, TestNuToLambda

### Community 814 - "Community 814"
Cohesion: 0.20
Nodes (4): basic_1d_integrand_exact(), basic_nd_integrand_exact(), Tests related to the interface of `cubature`., TestCubature

### Community 815 - "Community 815"
Cohesion: 0.18
Nodes (1): TestSomeDistanceFunctions

### Community 816 - "Community 816"
Cohesion: 0.31
Nodes (1): TestNumObsY

### Community 817 - "Community 817"
Cohesion: 0.18
Nodes (1): TestFitMethod

### Community 818 - "Community 818"
Cohesion: 0.18
Nodes (1): TestBessel

### Community 819 - "Community 819"
Cohesion: 0.25
Nodes (7): _fit_lsq_bivariate(), _fit_lsq_sphere(), _fit_smooth_bivariate(), _fit_smooth_sphere(), # NOTE: The systems in this test class are rank-deficient, _scattered_data(), _sphere_scattered_data()

### Community 820 - "Community 820"
Cohesion: 0.18
Nodes (1): TestDendrogram

### Community 821 - "Community 821"
Cohesion: 0.18
Nodes (3): Tests based on examples from gh-2640, TestBoundaries, TestGeometricTransformExtra

### Community 822 - "Community 822"
Cohesion: 0.18
Nodes (2): BoundsMixin, TestTRF

### Community 823 - "Community 823"
Cohesion: 0.18
Nodes (2): Test that when integrality is a list of all zeros, linprog gives the         sam, TestLinprogHiGHSMIP

### Community 824 - "Community 824"
Cohesion: 0.18
Nodes (1): TestFindObjects

### Community 825 - "Community 825"
Cohesion: 0.18
Nodes (1): TestMMIOReadLargeIntegers

### Community 826 - "Community 826"
Cohesion: 0.18
Nodes (2): TestLogNdtr, TestNdtri

### Community 827 - "Community 827"
Cohesion: 0.22
Nodes (1): TestPCHIP

### Community 828 - "Community 828"
Cohesion: 0.18
Nodes (9): _TestDCTBase, _TestDCTIBase, TestDCTIDouble, TestDCTIFloat, TestDCTIInt, _TestDCTIVBase, TestDCTIVDouble, TestDCTIVFloat (+1 more)

### Community 829 - "Community 829"
Cohesion: 0.18
Nodes (1): TestTrimmedStats

### Community 830 - "Community 830"
Cohesion: 0.20
Nodes (7): Test the length edge cases are handled correctly., Testing that the length edge cases are handled correctly., Verify the correctness of the default value of function parameter `sym`., Testing that `general_gaussian` with p = 1 is equivalent to the normal         `, Testing that if M is odd, the peak is at 1., TestCosine, TestGeneralGaussian

### Community 831 - "Community 831"
Cohesion: 0.31
Nodes (7): allocate(), deallocate(), default_construct_buffer(), destroy_buffer(), move_construct_buffer(), size_(), SmallDynamicArray()

### Community 832 - "Community 832"
Cohesion: 0.27
Nodes (3): LinearAssignment, ParallelLinearAssignment, random_uniform()

### Community 833 - "Community 833"
Cohesion: 0.27
Nodes (9): evaluate(), moderatec(), moderatef(), moderatex(), This is a module evaluating the objective/constraint function with Nan/Inf handl, This function moderates a decision variable. It replaces NaN by 0 and Inf/-Inf b, This function moderates the function value of a MINIMIZATION problem. It replace, This function moderates the constraint value, the constraint demanding this valu (+1 more)

### Community 834 - "Community 834"
Cohesion: 0.20
Nodes (7): convert_temperature(), lambda2nu(), nu2lambda(), Collection of physical constants and conversion factors.  Most constants are in, Convert from a temperature scale to another one among Celsius, Kelvin,     Fahre, Convert wavelength to optical frequency.      Parameters     ----------     lamb, Convert optical frequency to wavelength.      Parameters     ----------     nu :

### Community 835 - "Community 835"
Cohesion: 0.36
Nodes (7): get_tls_global(), mc64ad_(), mc64id_(), superlu_python_jmpbuf(), superlu_python_module_abort(), superlu_python_module_free(), superlu_python_module_malloc()

### Community 836 - "Community 836"
Cohesion: 0.38
Nodes (9): dct(), dctn(), dst(), dstn(), _execute(), idct(), idctn(), idst() (+1 more)

### Community 837 - "Community 837"
Cohesion: 0.24
Nodes (6): _get_xp_bpoly_cls(), Returns bpoly class to delegate to for xp along with internal array namespace., Construct a piecewise polynomial in Bernstein basis         from a power basis p, Construct a piecewise polynomial in the Bernstein basis,         compatible with, r"""Compute the coefficients of a polynomial in the Bernstein basis         give, r"""Raise a degree of a polynomial in the Bernstein basis.          Given the co

### Community 838 - "Community 838"
Cohesion: 0.31
Nodes (7): CData, _get_cffi_data(), _get_cffi_func(), _get_ctypes_data(), _get_ctypes_func(), _import_cffi(), _typename_from_ctypes()

### Community 839 - "Community 839"
Cohesion: 0.49
Nodes (9): qh_errexit_rbox(), qh_out1(), qh_out2n(), qh_out3n(), qh_outcoincident(), qh_outcoord(), qh_rboxpoints(), qh_rboxpoints2() (+1 more)

### Community 840 - "Community 840"
Cohesion: 0.24
Nodes (9): find_best_blas_type(), get_blas_funcs(), _get_funcs(), _memoize_get_funcs(), Low-level BLAS functions (:mod:`scipy.linalg.blas`) ============================, Find best-matching BLAS/LAPACK type.      Arrays are used to determine the optim, Return available BLAS/LAPACK functions.      Used also in lapack.py. See get_bla, Memoized fast path for _get_funcs instances (+1 more)

### Community 841 - "Community 841"
Cohesion: 0.24
Nodes (5): ordqz(), _qz(), QZ decomposition for generalized eigenvalues of a pair of matrices.      The QZ,, QZ decomposition for a pair of matrices with reordering.      Parameters     ---, _select_function()

### Community 842 - "Community 842"
Cohesion: 0.24
Nodes (7): _castCopy(), _commonType(), Schur decomposition functions., Compute Schur decomposition of a matrix.      The Schur decomposition is::, Convert real Schur form to complex Schur form.      Convert a quasi-diagonal rea, rsf2csf(), schur()

### Community 843 - "Community 843"
Cohesion: 0.20
Nodes (5): Compute `m` largest eigenvalues in each of the ``N`` directions,         i.e., u, Return the requested number of eigenvalues.          Parameters         --------, Return 1 eigenvector in 1d with index `j`         and number of grid points `n`, Return 1 eigenvector in Nd with multi-index `j`         as a tensor product of t, Return the requested number of eigenvectors for ordered eigenvalues.          Pa

### Community 844 - "Community 844"
Cohesion: 0.22
Nodes (5): _AProd, # TODO: once `svds` drops legacy positional `random_state` support,, Wrapper class for linear operator      The call signature of the __call__ method, Compute the singular value decomposition of a linear operator using PROPACK, _svdp()

### Community 845 - "Community 845"
Cohesion: 0.20
Nodes (5): build_quadratic_1d(), Functions used by least-squares algorithms., Parameterize a multivariate quadratic function along a line.      The resulting, Return a matrix arising in regularized least squares as LinearOperator.      The, regularized_lsq_operator()

### Community 846 - "Community 846"
Cohesion: 0.20
Nodes (10): _complex_via_real_components(), convolve1d(), correlate1d(), prewitt(), Complex convolution via a linear combination of real convolutions., Calculate a 1-D correlation along the given axis.      The lines of the array al, Calculate a 1-D convolution along the given axis.      The lines of the array al, Calculate a Prewitt filter.      Parameters     ----------     %(input)s     %(a (+2 more)

### Community 847 - "Community 847"
Cohesion: 0.20
Nodes (9): bracket_minimum(), bracket_root(), find_minimum(), find_root(), =================================================================== Elementwise, Find the root of a monotonic, real-valued function of a real variable.      For, Find the minimum of a unimodal, real-valued function of a real variable.      Fo, Bracket the root of a monotonic, real-valued function of a real variable.      F (+1 more)

### Community 848 - "Community 848"
Cohesion: 0.36
Nodes (9): _calc_score(), _common_input_validation(), _doubly_stochastic(), quadratic_assignment(), _quadratic_assignment_2opt(), _quadratic_assignment_faq(), r"""     Approximates solution to the quadratic assignment problem and     the g, r"""Solve the quadratic assignment problem (approximately).      This function s (+1 more)

### Community 849 - "Community 849"
Cohesion: 0.29
Nodes (9): _complex2real(), Spectral Algorithm for Nonlinear Equations, Wrap a function and an initial value so that (i) complex values     are wrapped, r"""     Solve nonlinear equation with the DF-SANE method      Options     -----, Convert from real to complex and reshape result arrays., _real2complex(), _root_df_sane(), _wrap_func() (+1 more)

### Community 850 - "Community 850"
Cohesion: 0.22
Nodes (4): RandomDisplacement, Tests setup.          Run tests based on the 1-D and 2-D functions described abo, Test_AdaptiveStepsize, Test_RandomDisplacement

### Community 851 - "Community 851"
Cohesion: 0.33
Nodes (3): Cmd, load_name_map(), main()

### Community 852 - "Community 852"
Cohesion: 0.31
Nodes (9): compute_md5(), compute_sha256(), get_latest_release_doc(), main(), Standalone script for writing release doc and logs::      python tools/release/w, Checks weather release directory is present or not     and calls the method to g, Method to pick the file from 'doc/release' with the highest     release number (, write_log_task() (+1 more)

### Community 853 - "Community 853"
Cohesion: 0.22
Nodes (2): ceil_log2pow5(), log2pow5()

### Community 854 - "Community 854"
Cohesion: 0.20
Nodes (10): _arc_jac_sc1(), _arc_jac_sn(), ellipap(), _ellipdeg(), _pow10m1(), 10 ** x - 1 for x near 0, Solve degree equation using nomes      Given n, m1, solve        n * K(m) / K'(m, Inverse Jacobian elliptic sn      Solve for z in w = sn(z, m)      Parameters (+2 more)

### Community 855 - "Community 855"
Cohesion: 0.22
Nodes (7): _calc_dual_canonical_window(), closest_STFT_dual_window(), Implementation of an FFT-based Short-time Fourier Transform., Dual window (canonical dual window by default).          A STFT can be interpret, Calculate canonical dual window for 1d window `win` and a time step     of `hop`, r"""Instantiate a `ShortTimeFFT` by only providing a dual window.          If an, r"""Calculate the STFT dual window of a given window closest to a desired dual

### Community 856 - "Community 856"
Cohesion: 0.24
Nodes (7): _check_mode(), _pad_h(), Upsample, FIR filter, and downsample.      Parameters     ----------     h : arr, Store coefficients in a transposed, flipped arrangement.      For example, suppo, Helper for resampling., Apply the prepared filter to the specified axis of N-D signal x., _UpFIRDn

### Community 857 - "Community 857"
Cohesion: 0.20
Nodes (7): find(), Functions to extract parts of sparse matrices, Return the upper triangular portion of a sparse array or matrix.      Returns th, Return the indices and values of the nonzero elements of a matrix.      Paramete, Return the lower triangular portion of a sparse array or matrix.      Returns th, tril(), triu()

### Community 858 - "Community 858"
Cohesion: 0.20
Nodes (10): jn_zeros(), jnp_zeros(), jnyn_zeros(), Compute nt zeros of Bessel functions Jn(x), Jn'(x), Yn(x), and Yn'(x).      Retu, r"""Compute zeros of integer-order Bessel functions Jn.      Compute `nt` zeros, r"""Compute zeros of integer-order Bessel function derivatives Jn'.      Compute, r"""Compute zeros of integer-order Bessel function Yn(x).      Compute `nt` zero, r"""Compute zeros of integer-order Bessel function derivatives Yn'(x).      Comp (+2 more)

### Community 859 - "Community 859"
Cohesion: 0.33
Nodes (7): scipy_ccos(), scipy_cexp(), scipy_clog(), scipy_cpow(), scipy_csin(), scipy_csqrt(), _scipy_from_dz()

### Community 861 - "Community 861"
Cohesion: 0.20
Nodes (10): chebyc(), chebyt(), r"""Gauss-Chebyshev (first kind) quadrature.      Computes the sample points and, r"""Chebyshev polynomial of the first kind.      Defined to be the solution of, r"""Gauss-Chebyshev (first kind) quadrature.      Compute the sample points and, r"""Chebyshev polynomial of the first kind on :math:`[-2, 2]`.      Defined as :, r"""Gauss-Chebyshev (first kind, shifted) quadrature.      Compute the sample po, roots_chebyc() (+2 more)

### Community 862 - "Community 862"
Cohesion: 0.20
Nodes (10): hermite(), _newton(), _pbcf(), r"""Gauss-Hermite (physicist's) quadrature.      Compute the sample points and w, r"""Asymptotic series expansion of parabolic cylinder function      The implemen, Newton iteration for polishing the asymptotic approximation     to the zeros of, r"""Gauss-Hermite (physicist's) quadrature for large n.      Computes the sample, r"""Physicist's Hermite polynomial.      Defined by      .. math::          H_n( (+2 more)

### Community 864 - "Community 864"
Cohesion: 0.22
Nodes (2): intMalloc(), SetIWork()

### Community 866 - "Community 866"
Cohesion: 0.24
Nodes (5): normal_inverse_gamma_gen, r"""     Normal-inverse-gamma distribution.      The normal-inverse-gamma distri, Draw random samples from the distribution.          Parameters         ---------, The probability density function.          Parameters         ----------, The variance of the distribution.          Parameters         ----------

### Community 867 - "Community 867"
Cohesion: 0.24
Nodes (9): istft_compare(), _istft_wrapper(), Helpers to utilize existing stft / istft tests for testing `ShortTimeFFT`.  This, Wrapper for the SciPy `istft()` function based on `ShortTimeFFT` for         uni, Assert that the results from the existing `stft()` and `_stft_wrapper()`     are, Assert that the results from the existing `istft()` and     `_istft_wrapper()` a, Wrapper for the SciPy `stft()` function based on `ShortTimeFFT` for     unit tes, stft_compare() (+1 more)

### Community 868 - "Community 868"
Cohesion: 0.20
Nodes (1): TestLIL

### Community 869 - "Community 869"
Cohesion: 0.20
Nodes (1): TestHankel

### Community 870 - "Community 870"
Cohesion: 0.20
Nodes (1): TestCombinatorics

### Community 871 - "Community 871"
Cohesion: 0.20
Nodes (1): TestGamma

### Community 872 - "Community 872"
Cohesion: 0.22
Nodes (2): TestMatrixNorms, TestVectorNorms

### Community 873 - "Community 873"
Cohesion: 0.22
Nodes (3): Quick and simple tests for (zc)-symm, syrk, syr2k., TestBLAS3Syrk, TestSyHe

### Community 875 - "Community 875"
Cohesion: 0.20
Nodes (2): Test behaviors of B-splines. Some of the values tested against were     returned, TestBSplines

### Community 876 - "Community 876"
Cohesion: 0.20
Nodes (1): TestGenerateKnots

### Community 879 - "Community 879"
Cohesion: 0.31
Nodes (9): _extract_capi(), Return {name: signature} for every entry in module.__pyx_capi__., No existing cython_special signature may change or disappear., No existing cython_blas signature may change or disappear., No existing cython_lapack signature may change or disappear., test_cython_blas_abi_stability(), test_cython_lapack_abi_stability(), test_cython_optimize_abi_stability() (+1 more)

### Community 881 - "Community 881"
Cohesion: 0.20
Nodes (1): TestZipfian

### Community 882 - "Community 882"
Cohesion: 0.20
Nodes (2): Compare 1d and 2d frequency response., Testfirwin_2d

### Community 883 - "Community 883"
Cohesion: 0.33
Nodes (1): TestFortranFormatParser

### Community 884 - "Community 884"
Cohesion: 0.24
Nodes (2): TestAsLinearOperator, TestLinearOperator

### Community 885 - "Community 885"
Cohesion: 0.20
Nodes (1): TestIsotonicRegression

### Community 886 - "Community 886"
Cohesion: 0.22
Nodes (3): ConsistencyTests, _Test_small, _Test_small_nonleaf

### Community 887 - "Community 887"
Cohesion: 0.20
Nodes (5): Test real (f07vef) and complex (f07vsf) examples from NAG          Examples avai, Test if invalid values of uplo, trans and diag raise exceptions, Test if a matrix with a zero diagonal element is singular          If the i-th d, Test ?tbtrs fails correctly if shapes are invalid., TestTbtrs

### Community 888 - "Community 888"
Cohesion: 0.24
Nodes (3): lpgen_2d(), -> A b c LP test: m*n vars, m+n constraints         row sums == n/m, col sums ==, TestLinprogIPSpecific

### Community 889 - "Community 889"
Cohesion: 0.29
Nodes (5): _check_save_and_load(), _save_and_load(), test_save_and_load_empty(), test_save_and_load_one_entry(), test_save_and_load_random()

### Community 890 - "Community 890"
Cohesion: 0.20
Nodes (1): TestWatershedIft

### Community 891 - "Community 891"
Cohesion: 0.29
Nodes (4): Test of min-max 1D features of sparse array classes, Test_MinMaxMixin1D, Test_ShapeMinMax2DWithAxis, toarray()

### Community 892 - "Community 892"
Cohesion: 0.20
Nodes (2): Example code used to generate SAS output:         DATA myData;         INPUT X Y, TestMood

### Community 893 - "Community 893"
Cohesion: 0.22
Nodes (3): log_ndtr_ndtri_exp(), Tests that ndtri_exp is sufficiently close to an inverse of log_ndtr.      We ha, TestNdtriExp

### Community 894 - "Community 894"
Cohesion: 0.22
Nodes (2): assert_hulls_equal(), TestConvexHull

### Community 896 - "Community 896"
Cohesion: 0.22
Nodes (3): test_random_state(), test_set_random_state(), TestRatioUniforms

### Community 897 - "Community 897"
Cohesion: 0.24
Nodes (1): TestSOSFilt

### Community 898 - "Community 898"
Cohesion: 0.20
Nodes (3): MyCallBack, Unit test for SLSQP optimization., pass a custom callback function      This makes sure it's being used.

### Community 899 - "Community 899"
Cohesion: 0.20
Nodes (1): Test functions for linalg._solve_toeplitz module

### Community 900 - "Community 900"
Cohesion: 0.20
Nodes (5): Check energy/power relations from `Spectral Analysis` section in the user guide., Create Cosine signal with amplitude a from spectrum., Test energy and power formulas., Verify spectral representations of windowed DFT.          Furthermore, the scali, TestSampledSpectralRepresentations

### Community 901 - "Community 901"
Cohesion: 0.22
Nodes (1): TestDescribe

### Community 902 - "Community 902"
Cohesion: 0.27
Nodes (4): FindFuncs, ParseCall, Tests which scan for certain occurrences in the code, they may not find all of t, warning_calls()

### Community 904 - "Community 904"
Cohesion: 0.29
Nodes (9): classify_libs(), loaded_libs(), main(), print_section(), Show which shared libraries are loaded by numpy and scipy imports.  Reads /proc/, Print one import section with categorized libraries., Strip the repo root prefix, keeping paths starting from .pixi/ or build-*., Classify libraries into shared libs, stdlib extensions, and package extensions (+1 more)

### Community 907 - "Community 907"
Cohesion: 0.22
Nodes (1): Bench

### Community 908 - "Community 908"
Cohesion: 0.31
Nodes (5): Expm, ExpmMultiply, random_sparse_csc(), random_sparse_csr(), benchmarks for the scipy.sparse.linalg._expm_multiply module

### Community 909 - "Community 909"
Cohesion: 0.22
Nodes (1): Bench

### Community 910 - "Community 910"
Cohesion: 0.31
Nodes (5): Bench, _create_sparse_poisson1d(), _create_sparse_poisson2d(), Lgmres, Check the speed of the conjugate gradient solver.

### Community 911 - "Community 911"
Cohesion: 0.25
Nodes (2): CMultiWalleniusNCHypergeometric(), CMultiWalleniusNCHypergeometricMoments()

### Community 912 - "Community 912"
Cohesion: 0.22
Nodes (1): tuple

### Community 913 - "Community 913"
Cohesion: 0.39
Nodes (8): _chlrps(), _gaminv(), _Phi(), _Phinv(), _primes(), _qsimvtv(), Computes permuted and scaled lower Cholesky factor c for R which may be     sing, Estimates the multivariate t CDF using randomized QMC      Parameters     ------

### Community 914 - "Community 914"
Cohesion: 0.31
Nodes (7): derivative(), _derivative_iv(), hessian(), jacobian(), r"""Evaluate the Jacobian of a function numerically.      Parameters     -------, Evaluate the derivative of an elementwise, real scalar function numerically., r"""Evaluate the Hessian of a function numerically.      Parameters     --------

### Community 915 - "Community 915"
Cohesion: 0.33
Nodes (5): is_line_all_spaces(), parse_header_enum(), read_comment(), read_header(), strip_trailing_cr()

### Community 916 - "Community 916"
Cohesion: 0.28
Nodes (4): bufsize(), exec(), good_size_cmplx(), good_size_complex()

### Community 917 - "Community 917"
Cohesion: 0.33
Nodes (8): fht(), fhtcoeff(), fhtoffset(), _fhtq(), ifht(), Return optimal offset for a fast Hankel transform.      Returns an offset close, Compute the biased fast Hankel transform.      This is the basic FFTLog routine., Compute the coefficient array for a fast Hankel transform.

### Community 918 - "Community 918"
Cohesion: 0.22
Nodes (6): _good_shape(), next_fast_len(), Ensure that shape argument is valid for scipy.fftpack      scipy.fftpack does no, DFT sample frequencies (for usage with rfft, irfft).      The returned float arr, Find the next fast size of input data to `fft`, for zero-padding, etc.      SciP, rfftfreq()

### Community 919 - "Community 919"
Cohesion: 0.25
Nodes (9): is_valid_im(), is_valid_linkage(), _lazy_valid_checks(), Return True if the inconsistency matrix passed is valid.      It must be a :math, Variant of `is_valid_im` to be called internally by other scipy functions,     w, Check the validity of a linkage matrix.      A linkage matrix is valid if it is, Variant of `is_valid_linkage` to be called internally by other scipy functions,, Validate a set of conditions on the contents of possibly lazy arrays.      Param (+1 more)

### Community 920 - "Community 920"
Cohesion: 0.22
Nodes (5): _get_xp_ppoly_cls(), Returns ppoly class to delegate to for xp along with internal array namespace., Construct the piecewise polynomial without making checks.          Takes the sam, Construct a piecewise polynomial from a spline          Parameters         -----, Construct a piecewise polynomial in the power basis         from a polynomial in

### Community 921 - "Community 921"
Cohesion: 0.39
Nodes (8): assert_almost_equal(), assert_array_almost_equal(), _check_scalar(), Extra testing functions that forbid 0d-input, see #21044  While the xp_assert_*, Backwards compatible replacement. In new code, use xp_assert_close instead., xp_assert_close(), xp_assert_equal(), xp_assert_less()

### Community 922 - "Community 922"
Cohesion: 0.28
Nodes (2): These are situations that can be tested in our pythran tests:     - A function w, _TestPythranFunc

### Community 924 - "Community 924"
Cohesion: 0.31
Nodes (8): ldl(), _ldl_construct_tri_factor(), _ldl_get_d_and_l(), _ldl_sanitize_ipiv(), This helper function takes the rather strangely encoded permutation array     re, Computes the LDLt or Bunch-Kaufman factorization of a symmetric/     hermitian m, Helper function to extract the diagonal and triangular matrices for     LDL.T fa, Helper function to construct explicit outer factors of LDL factorization.      I

### Community 925 - "Community 925"
Cohesion: 0.22
Nodes (6): bandwidth(), _datacopied(), norm(), Strict check for `arr` not sharing any data with `original`,     under the assum, Return the lower and upper bandwidth of a numeric array.      Parameters     ---, Matrix or vector norm.      This function is able to return one of eight differe

### Community 926 - "Community 926"
Cohesion: 0.31
Nodes (8): dogbox(), dogleg_step(), find_intersection(), lsmr_operator(), Dogleg algorithm with rectangular trust regions for least-squares minimization., Find dogleg step in a rectangular region.      Returns     -------     step : nd, Compute LinearOperator to use in LSMR by dogbox algorithm.      `active_set` mas, Find intersection of trust-region bounds and initial bounds.      Returns     --

### Community 927 - "Community 927"
Cohesion: 0.31
Nodes (8): backtracking(), The adaptation of Trust Region Reflective algorithm for a linear least-squares p, Solve regularized least squares using information from QR-decomposition.      Th, Find an appropriate step size using backtracking line search., Select the best step according to Trust Region Reflective algorithm., regularized_lsq_with_qr(), select_step(), trf_linear()

### Community 928 - "Community 928"
Cohesion: 0.22
Nodes (6): NamedTuple, Hyp2f1TestCase, Tests for hyp2f1 for complex values.  Author: Albert Steppi, with credit to Adam, TestHyp2f1ExtremeInputs, OperatorArgs, shape: (core) shape of the operator         op_dtype: dtype of the operator

### Community 929 - "Community 929"
Cohesion: 0.22
Nodes (6): _extend_mode_to_code(), _normalize_sequence(), array or dtype' polymorphism.      Return None for np.int8, dtype('float32') or, Convert an extension mode to the corresponding integer code., If input is a scalar, create a sequence of length equal to the     rank by dupli, _skip_if_dtype()

### Community 930 - "Community 930"
Cohesion: 0.36
Nodes (8): _linprog_highs_doc(), _linprog_highs_ds_doc(), _linprog_highs_ipm_doc(), _linprog_ip_doc(), _linprog_rs_doc(), _linprog_simplex_doc(), Created on Sat Aug 22 19:49:17 2020  @author: matth, r"""     Linear programming: minimize a linear objective function subject to lin

### Community 931 - "Community 931"
Cohesion: 0.33
Nodes (5): _bisect(), _brenth(), _brentq(), call_solver(), _ridder()

### Community 932 - "Community 932"
Cohesion: 0.25
Nodes (4): PythonDomain, =========== scipyoptdoc ===========  Proper docstrings for scipy.optimize.minimi, ScipyOptimizeInterfaceDomain, wrap_mangling_directive()

### Community 933 - "Community 933"
Cohesion: 0.22
Nodes (9): freqz(), freqz_sos(), Compute the frequency response of a digital filter.      Given the M-order numer, Helper to validate a SOS input, r"""     Compute the frequency response of a digital filter in SOS format., Compute the frequency response of a digital filter in SOS format (legacy).     ., _real_dtype_for_complex(), sosfreqz() (+1 more)

### Community 934 - "Community 934"
Cohesion: 0.33
Nodes (8): get_thunk_type_set(), main(), newer(), parse_routine(), Return true if 'source' exists and is more recently modified than     'target',, Get a list containing cartesian product of data types, plus a getter routine., Generate thunk and method code for a given routine.      Parameters     --------, write_autogen_blurb()

### Community 935 - "Community 935"
Cohesion: 0.39
Nodes (8): _adjust_bounds(), convex_hull_plot_2d(), delaunay_plot_2d(), _get_axes(), Plot the given Voronoi diagram in 2-D.      Parameters     ----------     vor :, Plot the given Delaunay triangulation in 2-D.      Parameters     ----------, Plot the given convex hull diagram in 2-D.      Parameters     ----------     hu, voronoi_plot_2d()

### Community 937 - "Community 937"
Cohesion: 0.28
Nodes (8): _elements_and_indices_with_max_real(), log_softmax(), logsumexp(), Compute the log of the sum of exponentials of input elements.      Parameters, r"""Compute the softmax function.      The softmax function transforms each elem, r"""Compute the logarithm of the softmax function.      In principle::, softmax(), _wrap_radians()

### Community 938 - "Community 938"
Cohesion: 0.25
Nodes (2): z_abs(), z_sgn()

### Community 939 - "Community 939"
Cohesion: 0.28
Nodes (4): csgemm_kernel(), csgemm_ovwr_left(), zdgemm_kernel(), zdgemm_ovwr_left()

### Community 940 - "Community 940"
Cohesion: 0.25
Nodes (2): showmanyc(), underflow()

### Community 941 - "Community 941"
Cohesion: 0.25
Nodes (2): c_abs(), c_sgn()

### Community 942 - "Community 942"
Cohesion: 0.25
Nodes (9): _chk2_asarray(), Calculates the T-test for the mean of ONE group of scores.      Parameters     -, Calculates the T-test for the means of TWO INDEPENDENT samples of scores.      P, Calculates the T-test on TWO RELATED samples of scores, a and b.      Parameters, Common code between all 3 t-test functions., ttest_1samp(), _ttest_finish(), ttest_ind() (+1 more)

### Community 943 - "Community 943"
Cohesion: 0.28
Nodes (5): ce_fourier_coefficient_using_integral(), Compute the Fourier coefficient of the even Mathieu function.     The integral d, Compute the Fourier coefficient of the odd Mathieu function.     The integral de, se_fourier_coefficient_using_integral(), TestMathieu

### Community 944 - "Community 944"
Cohesion: 0.22
Nodes (5): Test identities expressing the Legendre elliptic integrals in terms     of Carls, Test identity:         K(m) = R_F(0, 1-m, 1), Test identity:         K(m) = R_F(0, 1-m, 1)         But with the ellipkm1 funct, Test identity:         E(m) = 2*R_G(0, 1-k^2, 1), TestEllipLegendreCarlsonIdentities

### Community 945 - "Community 945"
Cohesion: 0.22
Nodes (4): func2d_easyderiv(), myTakeStep2(), Unit tests for the basin hopping global minimization algorithm., redo RandomDisplacement in function form without the attribute stepsize     to m

### Community 947 - "Community 947"
Cohesion: 0.22
Nodes (1): TestNoncentralTFunctions

### Community 948 - "Community 948"
Cohesion: 0.22
Nodes (4): Test for blas_int/blas_bint types used in cython_blas/cython_lapack.      Note s, Verify blas_int and blas_bint sizes matches the build configuration., TestBlasInt, TestLamch

### Community 949 - "Community 949"
Cohesion: 0.22
Nodes (1): TestChebyshev

### Community 950 - "Community 950"
Cohesion: 0.39
Nodes (1): TestNumObsDM

### Community 951 - "Community 951"
Cohesion: 0.22
Nodes (1): TestIrwinHall

### Community 952 - "Community 952"
Cohesion: 0.22
Nodes (2): test sparse matrix construction functions, TestExtract

### Community 953 - "Community 953"
Cohesion: 0.22
Nodes (1): TestVectorizedFilter

### Community 954 - "Community 954"
Cohesion: 0.22
Nodes (2): Unit tests for the global optimization benchmark functions, TestGoBenchmarkFunctions

### Community 955 - "Community 955"
Cohesion: 0.22
Nodes (1): TestIsValidLinkage

### Community 956 - "Community 956"
Cohesion: 0.22
Nodes (1): TestGMRES

### Community 957 - "Community 957"
Cohesion: 0.22
Nodes (1): Test_bode

### Community 958 - "Community 958"
Cohesion: 0.31
Nodes (2): Test functions for linalg.matmul_toeplitz function, TestMatmulToeplitz

### Community 959 - "Community 959"
Cohesion: 0.22
Nodes (1): TestTrustRegionConstr

### Community 960 - "Community 960"
Cohesion: 0.22
Nodes (1): TestFixedPoint

### Community 961 - "Community 961"
Cohesion: 0.28
Nodes (3): check_threadpoolctl(), test_scipy_threadpoolctl_version(), test_threadpoolctl()

### Community 962 - "Community 962"
Cohesion: 0.31
Nodes (1): TestApproxDerivativeSparse

### Community 963 - "Community 963"
Cohesion: 0.22
Nodes (1): TestAdjustSchemeToBounds

### Community 964 - "Community 964"
Cohesion: 0.33
Nodes (2): TestPdtr, TestPdtrc

### Community 965 - "Community 965"
Cohesion: 0.31
Nodes (3): _gen_ridge_line(), Generate coordinates for a ridge line.      Will be a series of coordinates, sta, TestRidgeLines

### Community 966 - "Community 966"
Cohesion: 0.22
Nodes (5): Test if flat maxima are detected correctly., Test if behavior on signal edges is correct., Test with linear signal., Test with simple signal., TestLocalMaxima1d

### Community 967 - "Community 967"
Cohesion: 0.31
Nodes (4): check_svdp(), is_complex_type(), test_examples(), test_svdp()

### Community 968 - "Community 968"
Cohesion: 0.22
Nodes (2): Check that triangulation works., TestDelaunay

### Community 969 - "Community 969"
Cohesion: 0.28
Nodes (1): TestVoronoi

### Community 970 - "Community 970"
Cohesion: 0.25
Nodes (3): Calculate 2-D reference data from a 1d transform, ref_2d(), Test_DCTN_IDCTN

### Community 971 - "Community 971"
Cohesion: 0.22
Nodes (2): Unit tests for optimization routines from _root.py., TestRoot

### Community 973 - "Community 973"
Cohesion: 0.25
Nodes (2): TestNumericalInversePolynomial, TestSimpleRatioUniforms

### Community 974 - "Community 974"
Cohesion: 0.22
Nodes (3): Tests for _sketches.py., Testing the Clarkson Woodruff Transform, TestClarksonWoodruffTransform

### Community 975 - "Community 975"
Cohesion: 0.22
Nodes (1): TestSphericalJn

### Community 976 - "Community 976"
Cohesion: 0.22
Nodes (4): Using PairedData's yuen.t.test method. Something to note is that there         a, The PairedData library only supports unequal variances. To compare         sampl, > library(PairedData)         > a <- c(2.7,2.7,1.1,3.0,1.9,3.0,3.8,3.8,0.3,1.9,1, TestTTestTrimmed

### Community 978 - "Community 978"
Cohesion: 0.25
Nodes (7): get_blas_macro_and_name(), Helper functions and variables for generation of BLAS/LAPACK wrappers., Complex-valued and some Accelerate functions have special symbols., Takes a mapping of full filepath to file contents to write at that path., Read BLAS/LAPACK signatures and split into name, return type, argument     names, read_signatures(), write_files()

### Community 979 - "Community 979"
Cohesion: 0.32
Nodes (7): isbetter(), This module provides subroutines that ensure the returned X is optimal among all, This function compares whether FC1 = (F1, C1) is (strictly) better than FC2 = (F, This subroutine selects X according to FHIST and CHIST, which represents (a part, This subroutine saves X, F, and CSTRV in XFILT, FFILT, and CFILT (and CONSTR in, savefilt(), selectx()

### Community 980 - "Community 980"
Cohesion: 0.36
Nodes (7): ascent(), electrocardiogram(), face(), fetch_data(), Get a 1024 x 768, color image of a raccoon face.      The image is derived from, Get an 8-bit grayscale bit-depth, 512 x 512 derived image for easy     use in de, Load an electrocardiogram as an example for a 1-D signal.      The returned sign

### Community 981 - "Community 981"
Cohesion: 0.25
Nodes (7): array_formatter, chunk, csc_formatter, dense_2d_call_formatter, line_formatter, triplet_formatter, vector_line_formatter

### Community 982 - "Community 982"
Cohesion: 0.25
Nodes (7): dense_2d_call_adding_parse_handler, dense_adding_parse_handler, doublet_parse_handler, triplet_calling_parse_handler, triplet_parse_handler, triplet_pattern_parse_handler, tuple_parse_handler

### Community 983 - "Community 983"
Cohesion: 0.29
Nodes (4): JennrichSampson, Judge, r"""     Judge objective function.      This class defines the Judge [1]_ global, r"""     Jennrich-Sampson objective function.      This class defines the Jennri

### Community 984 - "Community 984"
Cohesion: 0.29
Nodes (4): r"""     Vincent objective function.      This class defines the Vincent [1]_ gl, r"""     Venter Sobiezcczanski-Sobieski objective function.      This class defi, VenterSobiezcczanskiSobieski, Vincent

### Community 985 - "Community 985"
Cohesion: 0.29
Nodes (4): r"""     Yao-Liu 9 objective function.      This class defines the Yao-Liu [1]_, r"""     Yao-Liu 4 objective function.      This class defines the Yao-Liu funct, YaoLiu04, YaoLiu09

### Community 986 - "Community 986"
Cohesion: 0.36
Nodes (6): check_option(), _highs_wrapper(), Solve linear programs using HiGHS [1]_.      Assume problems of the form:, _constraints_to_components(), milp(), _milp_iv()

### Community 987 - "Community 987"
Cohesion: 0.25
Nodes (7): _coeff_of_divided_diff(), _compute_optimal_gcv_parameter(), make_smoothing_spline(), Returns a design matrix as a CSR format sparse array.          Parameters, Returns an optimal regularization parameter from the GCV criteria [1].      Para, Returns the coefficients of the divided difference.      Parameters     --------, r"""     Create a smoothing B-spline satisfying the Generalized Cross Validation

### Community 988 - "Community 988"
Cohesion: 0.25
Nodes (8): _lsq_clamp_postprocess(), make_lsq_spline(), _norm_eq_clamp_preprocess(), Checks if clamp_values has valid values or not., r"""Create a smoothing B-spline satisfying the Least SQuares (LSQ) criterion., Apply the clamp preprocessing to the banded matrix and RHS for the     norm-eq p, Reassemble the full coefficient vector after solving the reduced system., _validate_clamp_values()

### Community 989 - "Community 989"
Cohesion: 0.36
Nodes (6): _build_and_solve_system(), _build_evaluation_coefficients(), _build_system(), compute_interpolation(), polynomial_matrix(), Build and solve the RBF interpolation system of equations.      Parameters     -

### Community 990 - "Community 990"
Cohesion: 0.29
Nodes (4): _make_tuple_bunch(), Create a namedtuple-like class with additional attributes.      This function cr, Ensure that all the given names are valid Python identifiers that     do not sta, _validate_names()

### Community 991 - "Community 991"
Cohesion: 0.39
Nodes (7): _check_termination(), _initialize(), _loop(), _prepare_result(), Main loop of a vectorized scalar optimization algorithm      Parameters     ----, Initialize abscissa, function, and args arrays for elementwise function      Par, _update_active()

### Community 992 - "Community 992"
Cohesion: 0.46
Nodes (7): next_double(), next_uint32(), next_uint64(), random_interval(), random_normal(), random_standard_normal(), random_standard_uniform()

### Community 993 - "Community 993"
Cohesion: 0.46
Nodes (7): d2d(), d2d_small_int(), d2s(), d2s_buffered(), d2s_buffered_n(), decimalLength17(), to_chars()

### Community 994 - "Community 994"
Cohesion: 0.36
Nodes (4): convert_shape_to_errmsg(), RawFilter(), scipy_signal__sigtools_linear_filter(), zfill()

### Community 995 - "Community 995"
Cohesion: 0.29
Nodes (2): convert_strides(), FIRsepsym2d()

### Community 996 - "Community 996"
Cohesion: 0.29
Nodes (5): count_blocks(), estimate_blocksize(), Functions that operate on sparse matrices, Attempt to determine the blocksize of a sparse matrix      Returns a blocksize=(, For a given blocksize=(r,c) count the number of occupied     blocks in a sparse

### Community 997 - "Community 997"
Cohesion: 0.39
Nodes (5): allocate_std_vector_typenum(), array_from_std_vector_and_free(), c_array_from_object(), call_thunk(), free_std_vector_typenum()

### Community 998 - "Community 998"
Cohesion: 0.25
Nodes (8): _copy_array_if_base_present(), is_valid_dm(), num_obs_dm(), Copy the array if its base points to a parent array., Convert a vector-form distance vector to a square-form distance     matrix, and, Return True if input array satisfies basic distance matrix properties     (symme, Return the number of original observations that correspond to a     square, redu, squareform()

### Community 999 - "Community 999"
Cohesion: 0.29
Nodes (7): ellip_harm(), ellip_harm_2(), ellip_normal(), _ellip_normal_vec(), r"""     Ellipsoidal harmonic functions :math:`F^p_n(s)`.      These are also kn, r"""     Ellipsoidal harmonic normalization constants :math:`\gamma^p_n`.      T, r"""     Ellipsoidal harmonic functions :math:`E^p_n(s)`.      These are also kn

### Community 1000 - "Community 1000"
Cohesion: 0.25
Nodes (8): _compute_tauk(), _initial_nodes(), _initial_nodes_a(), _initial_nodes_b(), Helper function for Tricomi initial guesses      For details, see formula 3.1 in, r"""Tricomi initial guesses      Computes an initial approximation to the square, r"""Gatteschi initial guesses      Computes an initial approximation to the squa, Initial guesses for the Hermite roots      Computes an initial approximation to

### Community 1001 - "Community 1001"
Cohesion: 0.46
Nodes (7): cDumpLine(), cParseFloatFormat(), cParseIntFormat(), creadhb(), cReadValues(), FormFullA(), ReadVector()

### Community 1002 - "Community 1002"
Cohesion: 0.46
Nodes (7): cDumpLine(), cParseFloatFormat(), cParseIntFormat(), creadrb(), cReadValues(), FormFullA(), ReadVector()

### Community 1004 - "Community 1004"
Cohesion: 0.39
Nodes (6): dopcor(), dopri5(), dopri853(), dp86co(), hinit(), hinit853()

### Community 1005 - "Community 1005"
Cohesion: 0.46
Nodes (7): dDumpLine(), dParseFloatFormat(), dParseIntFormat(), dreadhb(), dReadValues(), FormFullA(), ReadVector()

### Community 1006 - "Community 1006"
Cohesion: 0.46
Nodes (7): dDumpLine(), dParseFloatFormat(), dParseIntFormat(), dreadrb(), dReadValues(), FormFullA(), ReadVector()

### Community 1007 - "Community 1007"
Cohesion: 0.32
Nodes (3): _ComputeFT(), NI_EuclideanFeatureTransform(), _VoronoiFT()

### Community 1008 - "Community 1008"
Cohesion: 0.46
Nodes (7): FormFullA(), ReadVector(), sDumpLine(), sParseFloatFormat(), sParseIntFormat(), sreadhb(), sReadValues()

### Community 1009 - "Community 1009"
Cohesion: 0.46
Nodes (7): FormFullA(), ReadVector(), sDumpLine(), sParseFloatFormat(), sParseIntFormat(), sreadrb(), sReadValues()

### Community 1010 - "Community 1010"
Cohesion: 0.25
Nodes (1): _BaseVersion

### Community 1011 - "Community 1011"
Cohesion: 0.46
Nodes (7): FormFullA(), ReadVector(), zDumpLine(), zParseFloatFormat(), zParseIntFormat(), zreadhb(), zReadValues()

### Community 1012 - "Community 1012"
Cohesion: 0.46
Nodes (7): FormFullA(), ReadVector(), zDumpLine(), zParseFloatFormat(), zParseIntFormat(), zreadrb(), zReadValues()

### Community 1013 - "Community 1013"
Cohesion: 0.32
Nodes (6): Compute the relative risk (also known as the risk ratio).      This function com, Result of `scipy.stats.contingency.relative_risk`.      Attributes     ---------, Compute the confidence interval for the relative risk.          The confidence i, relative_risk(), RelativeRiskResult, _validate_int()

### Community 1014 - "Community 1014"
Cohesion: 0.39
Nodes (1): TestData

### Community 1015 - "Community 1015"
Cohesion: 0.25
Nodes (1): TestArrayTools

### Community 1016 - "Community 1016"
Cohesion: 0.25
Nodes (1): _TestMinMax

### Community 1017 - "Community 1017"
Cohesion: 0.25
Nodes (2): Test for Carlson elliptic integrals ellipr[cdfgj].     The special values used i, TestEllipCarlson

### Community 1018 - "Community 1018"
Cohesion: 0.29
Nodes (4): Compute Struve function & error estimate from its power series., Check Struve function versus its power series, Regression test for #679, TestStruve

### Community 1019 - "Community 1019"
Cohesion: 0.25
Nodes (1): TestParabolicCylinder

### Community 1020 - "Community 1020"
Cohesion: 0.25
Nodes (1): TestMatrix_Balance

### Community 1021 - "Community 1021"
Cohesion: 0.36
Nodes (4): create_quadratic_function(), test_concatenation(), test_initial_constraints_as_canonical(), test_nonlinear_constraint()

### Community 1022 - "Community 1022"
Cohesion: 0.25
Nodes (1): TestFullCoverage

### Community 1023 - "Community 1023"
Cohesion: 0.32
Nodes (3): _has_hash(), Check if the provided path has the expected hash., TestDatasets

### Community 1024 - "Community 1024"
Cohesion: 0.29
Nodes (4): _patch_args(), Test dtype deprecations., Make sure func(*args) does not raise because *args is wrong., test_deprecations()

### Community 1026 - "Community 1026"
Cohesion: 0.25
Nodes (1): TestKappa4

### Community 1027 - "Community 1027"
Cohesion: 0.25
Nodes (1): TestNct

### Community 1028 - "Community 1028"
Cohesion: 0.25
Nodes (1): TestTruncWeibull

### Community 1029 - "Community 1029"
Cohesion: 0.25
Nodes (1): TestVoigtProfile

### Community 1030 - "Community 1030"
Cohesion: 0.25
Nodes (2): Test the identity transfer function., TestZpk2Tf

### Community 1031 - "Community 1031"
Cohesion: 0.61
Nodes (1): TestThreading

### Community 1032 - "Community 1032"
Cohesion: 0.25
Nodes (1): TestIsValidInconsistent

### Community 1033 - "Community 1033"
Cohesion: 0.25
Nodes (1): Test of csgraph public API with int64 index arrays in csr format.  See gh-24629

### Community 1034 - "Community 1034"
Cohesion: 0.39
Nodes (2): TestComplexSolout, TestSolout

### Community 1035 - "Community 1035"
Cohesion: 0.25
Nodes (1): TestMapCoordinates

### Community 1036 - "Community 1036"
Cohesion: 0.25
Nodes (1): Test_rectangle

### Community 1037 - "Community 1037"
Cohesion: 0.36
Nodes (2): Test_vectorization_cKDTree, Test_vectorization_KDTree

### Community 1038 - "Community 1038"
Cohesion: 0.25
Nodes (4): fun_trivial(), LossFunctionMixin, test_basic(), TestDogbox

### Community 1039 - "Community 1039"
Cohesion: 0.25
Nodes (1): TestLM

### Community 1040 - "Community 1040"
Cohesion: 0.25
Nodes (2): Check that >2-D operators are rejected cleanly., test_nD()

### Community 1041 - "Community 1041"
Cohesion: 0.29
Nodes (1): TestSS2TF

### Community 1043 - "Community 1043"
Cohesion: 0.36
Nodes (5): _gen_gaussians(), _gen_gaussians_even(), Verify parsing of condition arguments for `scipy.signal.find_peaks` function., test_unpack_condition_args(), TestArgrel

### Community 1044 - "Community 1044"
Cohesion: 0.29
Nodes (6): fftw_dct_ref(), fftw_dst_ref(), test_definition(), test_idct_definition(), test_idst_definition(), TestDCT

### Community 1045 - "Community 1045"
Cohesion: 0.43
Nodes (2): Check input overwrite behavior., TestOverwrite

### Community 1046 - "Community 1046"
Cohesion: 0.32
Nodes (1): TestNumericalInverseHermite

### Community 1047 - "Community 1047"
Cohesion: 0.25
Nodes (1): TestUniqueRoots

### Community 1048 - "Community 1048"
Cohesion: 0.25
Nodes (3): Various made-up tests to hit different branches of the code in specfun.c, (z == 1.0) && (c-a-b > 0.0), test_hygfz_branches()

### Community 1049 - "Community 1049"
Cohesion: 0.25
Nodes (1): TestSphericalKn

### Community 1050 - "Community 1050"
Cohesion: 0.25
Nodes (1): TestSphericalYn

### Community 1051 - "Community 1051"
Cohesion: 0.25
Nodes (2): TestSphericalJnYnCrossProduct, TestSphericalKnDerivatives

### Community 1052 - "Community 1052"
Cohesion: 0.25
Nodes (2): See Section 6 of         I. Steinwart, C. Pasin, R.C. Williamson & S. Zhang (201, TestExpectile

### Community 1053 - "Community 1053"
Cohesion: 0.25
Nodes (1): TestTTest_1samp

### Community 1054 - "Community 1054"
Cohesion: 0.25
Nodes (2): Unit tests for Krylov space trust-region subproblem solver., TestKrylovQuadraticSubproblem

### Community 1055 - "Community 1055"
Cohesion: 0.36
Nodes (3): A, B, test_no_spooky_action_at_a_distance()

### Community 1056 - "Community 1056"
Cohesion: 0.25
Nodes (4): Represent as quaternions.          Rotations in 3 dimensions can be represented, Concatenate a sequence of `Rotation` objects into a single object.          This, Reduce this rotation with the provided rotation groups.          Reduction of a, Set rotation(s) at given index(es) from object.          Parameters         ----

### Community 1057 - "Community 1057"
Cohesion: 0.38
Nodes (4): Bench, _create_sparse_poisson1d(), _create_sparse_poisson2d_half(), Check the speed of the sparse triangular solve function.

### Community 1058 - "Community 1058"
Cohesion: 0.29
Nodes (6): Partial singular value decomposition of a sparse matrix using LOBPCG.      Compu, Partial singular value decomposition of a sparse matrix using PROPACK.      Comp, Partial singular value decomposition of a sparse matrix using ARPACK.      Compu, _svds_arpack_doc(), _svds_lobpcg_doc(), _svds_propack_doc()

### Community 1059 - "Community 1059"
Cohesion: 0.43
Nodes (4): BadFortranFormat, SyntaxError, TestExpFormat, TestIntFormat

### Community 1061 - "Community 1061"
Cohesion: 0.29
Nodes (4): _PPolyBase, Add additional breakpoints and coefficients to the polynomial.          Paramete, Base class for piecewise polynomials -- NumPy backend., c and x may be modified by the user. The Cython code expects         that they a

### Community 1062 - "Community 1062"
Cohesion: 0.38
Nodes (6): _batch_dot(), clarkson_woodruff_transform(), cwt_matrix(), Sketching-based Matrix Computations, r"""     Generate a matrix S which represents a Clarkson-Woodruff transform., r"""     Applies a Clarkson-Woodruff Transform/sketch to the input matrix.

### Community 1063 - "Community 1063"
Cohesion: 0.33
Nodes (5): check_python_h_included_first(), diff_files(), process_files(), Find the diff since the given SHA.      Adapted from lint.py, Check that the passed file includes Python.h first if it does at all.      Perha

### Community 1064 - "Community 1064"
Cohesion: 0.43
Nodes (6): Trust Region Reflective algorithm for least-squares optimization.  The algorithm, Select the best step according to Trust Region Reflective algorithm., select_step(), trf(), trf_bounds(), trf_no_bounds()

### Community 1065 - "Community 1065"
Cohesion: 0.38
Nodes (6): _bracket_minimum(), _bracket_minimum_iv(), _bracket_root(), _bracket_root_iv(), Bracket the minimum of a unimodal scalar function of one variable      This func, Bracket the root of a monotonic scalar function of one variable      This functi

### Community 1066 - "Community 1066"
Cohesion: 0.33
Nodes (5): gammainc(), gammaincc(), Compute gammainc and gammaincc for large arguments and parameters and save the v, Compute gammainc exactly like mpmath does but allow for more     summands in hyp, Compute gammaincc exactly like mpmath does but allow for more     terms in hyper

### Community 1067 - "Community 1067"
Cohesion: 0.43
Nodes (5): mulPow5divPow2(), mulPow5InvDivPow2(), mulShift32(), multipleOfPowerOf5_32(), pow5factor_32()

### Community 1068 - "Community 1068"
Cohesion: 0.52
Nodes (6): ccallback__err_invalid_signature(), ccallback__get_thread_local(), ccallback_obtain(), ccallback_prepare(), ccallback_release(), ccallback__set_thread_local()

### Community 1069 - "Community 1069"
Cohesion: 0.62
Nodes (6): clansvd_irl(), dlansvd_irl(), int_max(), int_min(), slansvd_irl(), zlansvd_irl()

### Community 1070 - "Community 1070"
Cohesion: 0.67
Nodes (6): clansvd(), dlansvd(), int_max(), int_min(), slansvd(), zlansvd()

### Community 1071 - "Community 1071"
Cohesion: 0.52
Nodes (6): mins(), pop(), push(), push_greater_of(), push_less_of(), _resize_stack()

### Community 1072 - "Community 1072"
Cohesion: 0.52
Nodes (6): ldl_update(), ldp(), lsei(), lsi(), lsq(), __slsqp_body()

### Community 1073 - "Community 1073"
Cohesion: 0.33
Nodes (6): _bws_input_validation(), _bws_statistic(), bws_test(), Input validation and standardization for bws test, Compute the BWS test statistic for two independent samples, r'''Perform the Baumgartner-Weiss-Schindler test on two independent samples.

### Community 1074 - "Community 1074"
Cohesion: 0.29
Nodes (2): powerlognorm_gen, r"""A power log-normal continuous random variable.      %(before_notes)s      No

### Community 1075 - "Community 1075"
Cohesion: 0.29
Nodes (1): TestAiry

### Community 1076 - "Community 1076"
Cohesion: 0.29
Nodes (1): TestSepfir2d

### Community 1077 - "Community 1077"
Cohesion: 0.29
Nodes (2): Check the SciPy config is valid., TestSciPyConfigs

### Community 1078 - "Community 1078"
Cohesion: 0.29
Nodes (2): Tests that `cubature` gives the correct answer., TestCubatureProblems

### Community 1079 - "Community 1079"
Cohesion: 0.29
Nodes (1): Test Cython optimize zeros API functions: ``bisect``, ``ridder``, ``brenth``, an

### Community 1081 - "Community 1081"
Cohesion: 0.29
Nodes (1): TestNCH

### Community 1082 - "Community 1082"
Cohesion: 0.43
Nodes (1): TestSquareForm

### Community 1083 - "Community 1083"
Cohesion: 0.29
Nodes (2): test_support(), TestTukeyLambda

### Community 1084 - "Community 1084"
Cohesion: 0.29
Nodes (1): TestTrapezoid

### Community 1085 - "Community 1085"
Cohesion: 0.29
Nodes (1): Some tests for the documenting decorator and support functions

### Community 1087 - "Community 1087"
Cohesion: 0.29
Nodes (4): Tests for function `signal.bilinear`., Raise all exceptions in `bilinear()`., TestBilinear, TestIIRDesign

### Community 1088 - "Community 1088"
Cohesion: 0.43
Nodes (2): TestCplxPair, TestCplxReal

### Community 1089 - "Community 1089"
Cohesion: 0.29
Nodes (1): TestIIRFilter

### Community 1090 - "Community 1090"
Cohesion: 0.43
Nodes (3): For one lowpass, bandpass, and highpass example filter, this test         checks, Compute mean squared error versus ideal response across frequency         band., TestFirwin

### Community 1092 - "Community 1092"
Cohesion: 0.38
Nodes (2): Check if the GIL is properly released by scipy.interpolate functions., TestGIL

### Community 1093 - "Community 1093"
Cohesion: 0.52
Nodes (3): assert_csc_almost_equal(), TestHBReader, TestHBReadWrite

### Community 1094 - "Community 1094"
Cohesion: 0.29
Nodes (2): sparse_distance_matrix_consistency, _Test_sparse_distance_matrix

### Community 1095 - "Community 1095"
Cohesion: 0.29
Nodes (2): ExponentialFittingProblem, Provide data and function for exponential fitting in the form     y = a + exp(b

### Community 1096 - "Community 1096"
Cohesion: 0.29
Nodes (1): TestSpsolveTriangular

### Community 1098 - "Community 1098"
Cohesion: 0.43
Nodes (2): Perform the most common tests on the poles computed by place_poles         and r, TestPlacePoles

### Community 1099 - "Community 1099"
Cohesion: 0.29
Nodes (1): Test_freqresp

### Community 1100 - "Community 1100"
Cohesion: 0.29
Nodes (2): ndimage._measurements._stats() is a utility used by other functions.          Si, Test_measurements_stats

### Community 1101 - "Community 1101"
Cohesion: 0.29
Nodes (2): This class exists to create a callable that does not have a '__name__' attribute, ReturnShape

### Community 1102 - "Community 1102"
Cohesion: 0.29
Nodes (1): TestPlotting

### Community 1103 - "Community 1103"
Cohesion: 0.29
Nodes (1): TestComplex

### Community 1104 - "Community 1104"
Cohesion: 0.52
Nodes (1): TestPower

### Community 1105 - "Community 1105"
Cohesion: 0.29
Nodes (7): rigid_transform_to_xp(), test_as_dual_quat(), test_empty_transform_composition(), test_empty_transform_concatenation(), test_empty_transform_indexing(), test_rigid_transform_iter(), test_vector_validation()

### Community 1106 - "Community 1106"
Cohesion: 0.33
Nodes (3): _check_multigammaln_array_result(), test_multigammaln_array_arg(), TestMultiGammaLn

### Community 1107 - "Community 1107"
Cohesion: 0.38
Nodes (2): SphericalDerivativesTestCase, TestSphericalYnDerivatives

### Community 1108 - "Community 1108"
Cohesion: 0.29
Nodes (1): TestSphericalIn

### Community 1109 - "Community 1109"
Cohesion: 0.33
Nodes (2): Tests kstest and ks_1samp agree with K-S various sizes, alternatives, modes., TestKSTest

### Community 1111 - "Community 1111"
Cohesion: 0.29
Nodes (6): Compare results with some values that were computed using mpmath., Test values of lambda outside the domains of the functions., Compare results with some known exact formulas., test_tukeylambda_stats_invalid(), test_tukeylambda_stats_known_exact(), test_tukeylambda_stats_mpmath()

### Community 1112 - "Community 1112"
Cohesion: 0.29
Nodes (1): TestGaussPulse

### Community 1113 - "Community 1113"
Cohesion: 0.29
Nodes (4): Tests windows of small length that are normalized to 1. See the         document, Test windows of small length that are not normalized to 1. See         the docum, This test ensures the correctness of the implemented Taylor         Windowing fu, TestTaylor

### Community 1114 - "Community 1114"
Cohesion: 0.33
Nodes (3): future<R> submit(), submit_detach(), task_thread_pool

### Community 1115 - "Community 1115"
Cohesion: 0.67
Nodes (6): create_group(), cyclic(), dicyclic(), icosahedral(), octahedral(), tetrahedral()

### Community 1116 - "Community 1116"
Cohesion: 0.57
Nodes (6): build_arg_tuple(), build_kwarg_dict(), Q_PyObject_Vectorcall(), Q_PyObject_VectorcallDict(), Q_PyObject_VectorcallMethod(), Q_PyVectorcall_NARGS()

### Community 1117 - "Community 1117"
Cohesion: 0.47
Nodes (3): generalize_symmetry_triplet(), read_matrix_market_body_triplet(), read_matrix_market_triplet()

### Community 1119 - "Community 1119"
Cohesion: 0.47
Nodes (5): generate_decl_wrapper(), generate_file_wrapper(), make_all(), Create wrapper function declaration.      Wrapper has symbol `F_FUNC(name,NAME)`, Returns text of file containing wrappers for all BLAS/LAPACK functions.

### Community 1120 - "Community 1120"
Cohesion: 0.33
Nodes (5): fht(), ifht(), Fast Hankel transforms using the FFTLog algorithm.  The implementation closely f, r'''Compute the fast Hankel transform.      Computes the discrete Hankel transfo, r"""Compute the inverse fast Hankel transform.      Computes the discrete invers

### Community 1121 - "Community 1121"
Cohesion: 0.53
Nodes (2): FortranFormatParser, Parser for Fortran format strings. The parse method returns a *Format     instan

### Community 1122 - "Community 1122"
Cohesion: 0.33
Nodes (6): correspond(), cut_tree(), num_obs_linkage(), Given a linkage matrix Z, return the cut tree.      Parameters     ----------, Return the number of original observations of the linkage matrix passed.      Pa, Check for correspondence between linkage and condensed distance matrices.      T

### Community 1123 - "Community 1123"
Cohesion: 0.40
Nodes (6): fcluster(), fclusterdata(), inconsistent(), r"""     Calculate inconsistency statistics on a linkage matrix.      Parameters, Form flat clusters from the hierarchical clustering defined by     the given lin, Cluster observation data using a given metric.      Clusters the original observ

### Community 1124 - "Community 1124"
Cohesion: 0.40
Nodes (5): lsqr(), Sparse Equations and Least Squares.  The original Fortran code was written by C., Stable implementation of Givens rotation.      Notes     -----     The routine ', Find the least-squares solution to a large, sparse, linear system     of equatio, _sym_ortho()

### Community 1125 - "Community 1125"
Cohesion: 0.33
Nodes (2): LsodaDenseOutput, # IMPORTANT: Must copy solver._y because the C code reuses the same

### Community 1126 - "Community 1126"
Cohesion: 0.40
Nodes (5): array_namespace(), _ArrayClsInfo, Override functions from array_api_compat, for use by array-api-extra and interna, Get the array API compatible namespace for the arrays xs.      Parameters     --, _validate_array_cls()

### Community 1127 - "Community 1127"
Cohesion: 0.53
Nodes (5): get_sig_name(), get_type(), make_signature(), A script that uses f2py to generate the signature files used to make the Cython, sigs_from_dir()

### Community 1129 - "Community 1129"
Cohesion: 0.60
Nodes (5): get_pyi_files(), get_suffix_path(), get_test_files(), main(), Script for checking if all the test files are installed after building.  Example

### Community 1130 - "Community 1130"
Cohesion: 0.60
Nodes (5): _find_names(), _is_fixture(), is_misnamed_test_class(), is_misnamed_test_func(), main()

### Community 1131 - "Community 1131"
Cohesion: 0.33
Nodes (6): left_multiplied_operator(), left_multiply(), Return diag(d) J as LinearOperator., Compute diag(d) J.      If `copy` is False, `J` is modified in place (unless bei, Scale Jacobian and residuals for a robust loss function.      Arrays are modifie, scale_for_robust_loss_function()

### Community 1132 - "Community 1132"
Cohesion: 0.33
Nodes (3): Byteorder utilities for system - numpy byteorder encoding  Converts a variety of, Convert various order codings to NumPy format.      Parameters     ----------, to_numpy_code()

### Community 1133 - "Community 1133"
Cohesion: 0.33
Nodes (3): _convert_codecs(), Constants and classes for matlab 5 read and write  See also mio5_utils.pyx where, Convert codec template mapping to byte order      Set codecs not on this system

### Community 1134 - "Community 1134"
Cohesion: 0.33
Nodes (6): convolve(), correlate(), _correlate_or_convolve(), _invalid_origin(), Multidimensional correlation.      The array is correlated with the given kernel, Multidimensional convolution.      The array is convolved with the given kernel.

### Community 1135 - "Community 1135"
Cohesion: 0.33
Nodes (6): gaussian_filter(), gaussian_filter1d(), _gaussian_kernel1d(), Computes a 1-D Gaussian convolution kernel., 1-D Gaussian filter.      Parameters     ----------     %(input)s     sigma : sc, Multidimensional Gaussian filter.      Parameters     ----------     %(input)s

### Community 1136 - "Community 1136"
Cohesion: 0.33
Nodes (6): gaussian_laplace(), generic_laplace(), laplace(), N-D Laplace filter based on approximate second derivatives.      Parameters, Multidimensional Laplace filter using Gaussian second derivatives.      Paramete, N-D Laplace filter using a provided second derivative function.      Parameters

### Community 1137 - "Community 1137"
Cohesion: 0.47
Nodes (5): _chandrupatla(), _chandrupatla_iv(), _chandrupatla_minimize(), Find the root of an elementwise function using Chandrupatla's algorithm.      Fo, Find the minimizer of an elementwise function.      For each element of the outp

### Community 1139 - "Community 1139"
Cohesion: 0.47
Nodes (5): main(), mp_wright_bessel(), Compute a grid of values for Wright's generalized Bessel function and save the v, Compute Wright's generalized Bessel function as Series with mpmath., rgamma_cached()

### Community 1140 - "Community 1140"
Cohesion: 0.60
Nodes (5): f2d(), f2s(), f2s_buffered(), f2s_buffered_n(), to_chars()

### Community 1141 - "Community 1141"
Cohesion: 0.33
Nodes (6): _design_notch_peak_filter(), iirnotch(), iirpeak(), Design second-order IIR notch digital filter.      A notch filter is a band-stop, Design second-order IIR peak (resonant) digital filter.      A peak filter is a, Design notch or peak digital filter.      Parameters     ----------     w0 : flo

### Community 1142 - "Community 1142"
Cohesion: 0.33
Nodes (1): doilinks     ~~~~~~~~     Extension to add links to DOIs. With this extension yo

### Community 1143 - "Community 1143"
Cohesion: 0.33
Nodes (5): load_npz(), Save a sparse matrix or array to a file using ``.npz`` format.      Parameters, # TODO: After a few releases, switch 2D case to save with coords only., Load a sparse array/matrix from a file using ``.npz`` format.      Parameters, save_npz()

### Community 1144 - "Community 1144"
Cohesion: 0.33
Nodes (6): euclidean(), minkowski(), Compute the Minkowski distance between two arrays.      The Minkowski distance b, Computes the Euclidean distance between two arrays.      The Euclidean distance, Return the standardized Euclidean distance between two 1-D arrays.      The stan, seuclidean()

### Community 1145 - "Community 1145"
Cohesion: 0.40
Nodes (5): _parse_core_ndims(), Helpers for producing efficient wrappers of ufuncs., Helper to ensure optimal iteration order for ufuncs that use caching.      This, Return tuple of num core dims per input from gufunc signature., _with_cache_optimization()

### Community 1146 - "Community 1146"
Cohesion: 0.60
Nodes (5): at_plus_a(), get_colamd(), get_metis(), get_perm_c(), getata()

### Community 1147 - "Community 1147"
Cohesion: 0.60
Nodes (5): genmmd_(), slu_mmdelm_(), slu_mmdint_(), slu_mmdnum_(), slu_mmdupd_()

### Community 1148 - "Community 1148"
Cohesion: 0.53
Nodes (4): _bessel_j1(), NI_FourierFilter(), p1evl(), polevl()

### Community 1149 - "Community 1149"
Cohesion: 0.60
Nodes (4): _get_spline_boundary_mode(), map_coordinate(), NI_GeometricTransform(), NI_ZoomShift()

### Community 1150 - "Community 1150"
Cohesion: 0.33
Nodes (6): argstoarray(), f_oneway(), obrientransform(), Constructs a 2D array from a group of sequences.      Sequences are filled with, Computes a transform on input data (any number of columns).  Used to     test fo, Performs a 1-way ANOVA, returning an F-value and probability given     any numbe

### Community 1151 - "Community 1151"
Cohesion: 0.33
Nodes (2): Quick and simple tests for *trmm., TestTRMM

### Community 1152 - "Community 1152"
Cohesion: 0.33
Nodes (3): `side=1` means C <- B*A, hence shapes of A and B are to be         compatible. O, SYMM only considers the upper/lower part of A. Hence setting         wrong value, TestBLAS3Symm

### Community 1154 - "Community 1154"
Cohesion: 0.33
Nodes (1): TestReconstructPath

### Community 1157 - "Community 1157"
Cohesion: 0.47
Nodes (4): check_precomputed_polar(), test_precomputed_cases(), test_verify_cases(), verify_polar()

### Community 1158 - "Community 1158"
Cohesion: 0.33
Nodes (2): TestArcsine, TestF

### Community 1159 - "Community 1159"
Cohesion: 0.33
Nodes (1): TestGenGamma

### Community 1160 - "Community 1160"
Cohesion: 0.33
Nodes (1): TestLevy

### Community 1163 - "Community 1163"
Cohesion: 0.33
Nodes (1): TestInverseErrorFunction

### Community 1164 - "Community 1164"
Cohesion: 0.33
Nodes (1): TestNumObsLinkage

### Community 1165 - "Community 1165"
Cohesion: 0.33
Nodes (1): TestSpline

### Community 1166 - "Community 1166"
Cohesion: 0.33
Nodes (6): pteqr_get_d_e_A_z(), Tests the ?pteqr lapack routine for all dtypes and compute_z parameters.     It, test_pteqr(), test_pteqr_error_non_spd(), test_pteqr_error_singular(), test_pteqr_raise_error_wrong_shape()

### Community 1167 - "Community 1167"
Cohesion: 0.40
Nodes (4): objfun(), simplified objective func to test lbfgsb bound violation, test if setulb() violates bounds      checks for violation due to floating point, test_setulb_floatround()

### Community 1168 - "Community 1168"
Cohesion: 0.33
Nodes (1): TestGstrsErrors

### Community 1170 - "Community 1170"
Cohesion: 0.33
Nodes (2): Regression tests for optimize., TestRegression

### Community 1171 - "Community 1171"
Cohesion: 0.33
Nodes (2): # TODO: use `xp` as backend when cupy works with `rankdata`, TestMonteCarloMethod

### Community 1173 - "Community 1173"
Cohesion: 0.33
Nodes (6): Test that Rotation is promoted to RigidTransform in composition., rotation_to_xp(), test_as_components(), test_from_components(), test_from_rotation(), test_rotation_promotion()

### Community 1174 - "Community 1174"
Cohesion: 0.33
Nodes (1): TestSphericalOld

### Community 1175 - "Community 1175"
Cohesion: 0.33
Nodes (2): chirp_hyperbolic(), chirp_quadratic()

### Community 1176 - "Community 1176"
Cohesion: 0.33
Nodes (2): TestDPSS, TestTukey

### Community 1177 - "Community 1177"
Cohesion: 0.33
Nodes (3): Return the rotation component of the transform.          A transform is a compos, Initialize from a 4x4 transformation matrix.          Rotations are not meant to, Initialize from a 4x4 transformation matrix.          Parameters         -------

### Community 1180 - "Community 1180"
Cohesion: 0.40
Nodes (2): Benchmark the solve_toeplitz solver (Levinson recursion), SolveToeplitz

### Community 1181 - "Community 1181"
Cohesion: 0.50
Nodes (3): calcfc_chebyquad(), This is an example to illustrate the usage of the solver.  Translated from Zaiku, test_chebyquad()

### Community 1182 - "Community 1182"
Cohesion: 0.50
Nodes (4): download_all(), main(), Platform independent script to download all the `scipy.datasets` module data fil, Utility method to download all the dataset files     for `scipy.datasets` module

### Community 1183 - "Community 1183"
Cohesion: 0.40
Nodes (4): _r2r(), _r2rn(), Forward or backward 1-D DCT/DST      Parameters     ----------     forward : boo, Forward or backward nd DCT/DST      Parameters     ----------     forward : bool

### Community 1184 - "Community 1184"
Cohesion: 0.60
Nodes (4): _herm(), _iv(), Partial singular value decomposition of a sparse matrix.      Compute the larges, svds()

### Community 1185 - "Community 1185"
Cohesion: 0.60
Nodes (4): get_preconditioner(), main(), Compute the preconditioner M, solve()

### Community 1186 - "Community 1186"
Cohesion: 0.60
Nodes (4): get_lebedev_recurrence_points(), get_lebedev_sphere(), lebedev_rule(), r"""Lebedev quadrature.      Compute the sample points and weights for Lebedev q

### Community 1187 - "Community 1187"
Cohesion: 0.50
Nodes (4): _fgmres(), gcrotmk(), FGMRES Arnoldi process, with optional projection or augmentation      Parameters, Solve ``Ax = b`` with the flexible GCROT(m,k) algorithm.      Parameters     ---

### Community 1188 - "Community 1188"
Cohesion: 0.50
Nodes (3): coerce(), make_system(), Make a linear system Ax=b      Parameters     ----------     A : LinearOperator

### Community 1190 - "Community 1190"
Cohesion: 0.60
Nodes (4): norm(), Norm of a sparse matrix.      This function is able to return one of seven diffe, _ravel(), _sparse_frobenius_norm()

### Community 1191 - "Community 1191"
Cohesion: 0.60
Nodes (4): main(), # TODO: the following ufuncs do not have a `__signature__`, this is worth fixing, walk_class(), walk_module()

### Community 1192 - "Community 1192"
Cohesion: 0.50
Nodes (4): bvls(), compute_kkt_optimality(), Bounded-variable least-squares algorithm., Compute the maximum violation of KKT conditions.

### Community 1193 - "Community 1193"
Cohesion: 0.50
Nodes (4): lsq_linear(), prepare_bounds(), Linear least squares with bound constraints on independent variables., r"""Solve a linear least-squares problem with bounds on the variables.      Give

### Community 1194 - "Community 1194"
Cohesion: 0.40
Nodes (1): Integration convergence comparison: MC vs Sobol'.  The function is a synthetic e

### Community 1195 - "Community 1195"
Cohesion: 0.40
Nodes (1): Integration convergence.  The function is a synthetic example specifically desig

### Community 1196 - "Community 1196"
Cohesion: 0.60
Nodes (4): main(), Precompute series coefficients for log-Gamma., stirling_series(), taylor_series_at_1()

### Community 1197 - "Community 1197"
Cohesion: 0.80
Nodes (4): main(), mpmath_wrightomega(), wrightomega_exp_error(), wrightomega_series_error()

### Community 1198 - "Community 1198"
Cohesion: 0.60
Nodes (3): ptr(), rcont1(), rcont2()

### Community 1199 - "Community 1199"
Cohesion: 0.70
Nodes (4): argsort_iter(), augmenting_path(), solve(), solve_rectangular_linear_sum_assignment()

### Community 1200 - "Community 1200"
Cohesion: 0.50
Nodes (2): _correlate_nd_imp(), scipy_signal__sigtools_correlateND()

### Community 1202 - "Community 1202"
Cohesion: 0.40
Nodes (5): dice(), _nbool_correspond_ft_tf(), Compute the Dice dissimilarity between two boolean 1-D arrays.      The Dice dis, Compute the Sokal-Sneath dissimilarity between two boolean 1-D arrays.      The, sokalsneath()

### Community 1203 - "Community 1203"
Cohesion: 0.40
Nodes (5): _nbool_correspond_all(), Compute the Yule dissimilarity between two boolean 1-D arrays.      The Yule dis, Compute the Rogers-Tanimoto dissimilarity between two boolean 1-D arrays.      T, rogerstanimoto(), yule()

### Community 1205 - "Community 1205"
Cohesion: 0.40
Nodes (2): multigammaln(), r"""Returns the log of multivariate gamma, also sometimes called the     general

### Community 1206 - "Community 1206"
Cohesion: 0.60
Nodes (4): add_weights(), build(), build_ckdtree(), build_weights()

### Community 1208 - "Community 1208"
Cohesion: 0.50
Nodes (2): interval_interval_p(), rect_rect_p()

### Community 1213 - "Community 1213"
Cohesion: 0.50
Nodes (3): _continued_fraction(), _continued_fraction_iv(), r"""Evaluate a generalized continued fraction numerically.      `_continued_frac

### Community 1214 - "Community 1214"
Cohesion: 0.50
Nodes (4): _central_diff_weights(), _derivative(), Return weights for an Np-point central derivative.      Assumes equally-spaced f, Find the nth derivative of a function at a point.      Given a function, use a c

### Community 1215 - "Community 1215"
Cohesion: 0.40
Nodes (4): Kurtosis of the Tukey Lambda distribution.      Parameters     ----------     la, Variance of the Tukey Lambda distribution.      Parameters     ----------     la, tukeylambda_kurtosis(), tukeylambda_variance()

### Community 1216 - "Community 1216"
Cohesion: 0.40
Nodes (1): _MockFunction

### Community 1217 - "Community 1217"
Cohesion: 0.60
Nodes (2): Test real/complex arithmetic, _TestArithmetic

### Community 1218 - "Community 1218"
Cohesion: 0.40
Nodes (1): _TestInplaceArithmetic

### Community 1219 - "Community 1219"
Cohesion: 0.40
Nodes (2): Test beta and betaln., TestBeta

### Community 1220 - "Community 1220"
Cohesion: 0.40
Nodes (1): TestFresnel

### Community 1221 - "Community 1221"
Cohesion: 0.40
Nodes (4): f_with_problematic_points(), Test that break points are correctly mapped under the _InfiniteLimitsTransform, This emulates a function with a list of singularities given by `points`.      If, TestTransformations

### Community 1222 - "Community 1222"
Cohesion: 0.40
Nodes (3): Tests underlying cubature rules (ndim >= 2)., Tests that the number of function evaluations required for Genz-Malik cubature, TestRulesCubature

### Community 1223 - "Community 1223"
Cohesion: 0.40
Nodes (1): TestBurr

### Community 1224 - "Community 1224"
Cohesion: 0.40
Nodes (1): TestRecipInvGauss

### Community 1225 - "Community 1225"
Cohesion: 0.40
Nodes (1): TestCorrespond

### Community 1226 - "Community 1226"
Cohesion: 0.40
Nodes (1): TestFcluster

### Community 1227 - "Community 1227"
Cohesion: 0.40
Nodes (1): TestLeavesList

### Community 1228 - "Community 1228"
Cohesion: 0.40
Nodes (2): count_neighbors_consistency, _Test_count_neighbors

### Community 1230 - "Community 1230"
Cohesion: 0.40
Nodes (1): TestFlapackSimple

### Community 1231 - "Community 1231"
Cohesion: 0.40
Nodes (1): TestLeastSquaresSolvers

### Community 1232 - "Community 1232"
Cohesion: 0.40
Nodes (1): TestNfev

### Community 1233 - "Community 1233"
Cohesion: 0.60
Nodes (4): Jottings to work out format for __function_workspace__ matrix at end of mat file, read_minimat_vars(), read_workspace_vars(), test_jottings()

### Community 1234 - "Community 1234"
Cohesion: 0.40
Nodes (1): Test how the ufuncs in special handle nan inputs.

### Community 1237 - "Community 1237"
Cohesion: 0.70
Nodes (1): TestVertexNeighborVertices

### Community 1238 - "Community 1238"
Cohesion: 0.40
Nodes (2): Verify that the input samples are not mutated in place and that they do, TestLloyd

### Community 1240 - "Community 1240"
Cohesion: 0.40
Nodes (2): Arguments:         d     - A list of two elements, where d[0] represents x and d, This is the derivative of fun, returning a NumPy array         representing df/d

### Community 1241 - "Community 1241"
Cohesion: 0.40
Nodes (1): TestSparseFunctions

### Community 1242 - "Community 1242"
Cohesion: 0.40
Nodes (1): _vectorize()

### Community 1244 - "Community 1244"
Cohesion: 0.50
Nodes (3): _get_nan_val(), Test that all ufuncs have float32-preserving signatures.  This was once guarante, test_nep50()

### Community 1245 - "Community 1245"
Cohesion: 0.40
Nodes (1): TestChebWin

### Community 1246 - "Community 1246"
Cohesion: 0.50
Nodes (4): extract_capi(), generate(), Return a sorted dict {function_name: capsule_signature_string} for every     ent, Generate a test file and JSON signatures file for the given submodule.      subm

### Community 1247 - "Community 1247"
Cohesion: 0.40
Nodes (3): equality_constrained_sqp(), Byrd-Omojokun Trust-Region SQP method., Solve nonlinear equality-constrained problem using trust-region SQP.      Solve

### Community 1248 - "Community 1248"
Cohesion: 0.70
Nodes (4): dump_dataset(), dump_datasets(), parse_ipp_file(), _raw_data()

### Community 1249 - "Community 1249"
Cohesion: 0.50
Nodes (4): main(), newer(), python makenpz.py DIRECTORY  Build a npz containing all data files in the direct, Return true if 'source' exists and is more recently modified than     'target',

### Community 1250 - "Community 1250"
Cohesion: 0.67
Nodes (3): main(), process_tempita(), Process tempita templated file and write out the result.      The template file

### Community 1252 - "Community 1252"
Cohesion: 0.67
Nodes (2): count_lines(), is_all_spaces()

### Community 1254 - "Community 1254"
Cohesion: 0.67
Nodes (2): write_body(), write_body_sequential()

### Community 1255 - "Community 1255"
Cohesion: 0.67
Nodes (2): exec_(), footprint()

### Community 1256 - "Community 1256"
Cohesion: 0.50
Nodes (3): number_digits(), Given an integer, returns a "reasonable" IntFormat instance to represent, Given a float number, returns a "reasonable" ExpFormat instance to         repre

### Community 1257 - "Community 1257"
Cohesion: 0.50
Nodes (1): HighsOptionsManager

### Community 1258 - "Community 1258"
Cohesion: 0.50
Nodes (3): lsmr(), Copyright (C) 2010 David Fong and Michael Saunders  LSMR uses an iterative metho, Iterative solver for least-squares problems.      lsmr solves the system of line

### Community 1259 - "Community 1259"
Cohesion: 0.50
Nodes (3): orthogonal_procrustes(), Solve the orthogonal Procrustes problem., Compute the matrix solution of the orthogonal (or unitary) Procrustes problem.

### Community 1260 - "Community 1260"
Cohesion: 0.50
Nodes (2): MarkerCollector, Check for functions advertising alt backend support without tests.  This checks

### Community 1261 - "Community 1261"
Cohesion: 0.50
Nodes (4): find_active_constraints(), make_strictly_feasible(), Determine which constraints are active in a given point.      The threshold is c, Shift a point to the interior of a feasible region.      Each element of the ret

### Community 1262 - "Community 1262"
Cohesion: 0.50
Nodes (4): in_bounds(), Check if a point lies within bounds., Compute reflective transformation and its gradient., reflective_transformation()

### Community 1263 - "Community 1263"
Cohesion: 0.50
Nodes (4): Return J diag(d) as LinearOperator., Compute J diag(d).      If `copy` is False, `J` is modified in place (unless bei, right_multiplied_operator(), right_multiply()

### Community 1264 - "Community 1264"
Cohesion: 0.50
Nodes (4): gaussian_gradient_magnitude(), generic_gradient_magnitude(), Gradient magnitude using a provided gradient function.      Parameters     -----, Multidimensional gradient magnitude using Gaussian derivatives.      Parameters

### Community 1265 - "Community 1265"
Cohesion: 0.50
Nodes (4): Calculate a 1-D uniform filter along the given axis.      The lines of the array, Multidimensional uniform filter.      Parameters     ----------     %(input)s, uniform_filter(), uniform_filter1d()

### Community 1266 - "Community 1266"
Cohesion: 0.50
Nodes (2): _maybe_convert_arg(), Convert arrays/scalars hiding in the sequence `arg`.

### Community 1268 - "Community 1268"
Cohesion: 0.50
Nodes (1): Pythran implementation of columns grouping for finite difference Jacobian estima

### Community 1271 - "Community 1271"
Cohesion: 0.50
Nodes (1): StandardNormal

### Community 1272 - "Community 1272"
Cohesion: 0.67
Nodes (3): generate_A(), main(), Precompute the polynomials for the asymptotic expansion of the generalized expon

### Community 1273 - "Community 1273"
Cohesion: 0.67
Nodes (3): lambertw_pade(), main(), Compute a Pade approximation for the principal branch of the Lambert W function

### Community 1274 - "Community 1274"
Cohesion: 0.67
Nodes (3): main(), Compute the Taylor series for zeta(x) - 1 around x = 0., zetac_series()

### Community 1275 - "Community 1275"
Cohesion: 0.83
Nodes (3): circular_wrap_index(), pylab_convolve_2d(), reflect_symm_index()

### Community 1276 - "Community 1276"
Cohesion: 0.50
Nodes (1): r""" =================================== Sparse arrays (:mod:`scipy.sparse`) ===

### Community 1277 - "Community 1277"
Cohesion: 0.50
Nodes (4): correlation(), cosine(), Compute the correlation distance between two 1-D arrays.      The correlation di, Compute the Cosine distance between 1-D arrays.      The Cosine distance between

### Community 1278 - "Community 1278"
Cohesion: 0.50
Nodes (4): is_valid_y(), num_obs_y(), Return True if the input array is a valid condensed distance matrix.      Conden, Return the number of original observations that correspond to a     condensed di

### Community 1279 - "Community 1279"
Cohesion: 0.50
Nodes (3): procrustes(), This module provides functions to perform full Procrustes analysis.  This code w, r"""Procrustes analysis, a similarity test for two data sets.      Each input ma

### Community 1280 - "Community 1280"
Cohesion: 0.50
Nodes (4): polygamma(), r"""Polygamma functions.      Defined as :math:`\psi^{(n)}(x)` where :math:`\psi, r"""     Riemann or Hurwitz zeta function.      Parameters     ----------     x, zeta()

### Community 1281 - "Community 1281"
Cohesion: 0.50
Nodes (3): lambertw(), # TODO: special expert should inspect this, r"""     lambertw(z, k=0, tol=1e-8)      Lambert W function.      The Lambert W

### Community 1282 - "Community 1282"
Cohesion: 0.50
Nodes (4): hermitenorm(), r"""Gauss-Hermite (statistician's) quadrature.      Compute the sample points an, r"""Probabilist's Hermite polynomial.      Defined by      .. math::          He, roots_hermitenorm()

### Community 1286 - "Community 1286"
Cohesion: 0.67
Nodes (2): traverse_checking(), traverse_no_checking()

### Community 1287 - "Community 1287"
Cohesion: 0.67
Nodes (2): traverse_checking(), traverse_no_checking()

### Community 1288 - "Community 1288"
Cohesion: 0.67
Nodes (2): traverse_checking(), traverse_no_checking()

### Community 1291 - "Community 1291"
Cohesion: 0.50
Nodes (4): _mask_to_limits(), Mask an array for values outside of given limits.      This is primarily a utili, Compute the trimmed variance      This function computes the sample variance of, tvar()

### Community 1292 - "Community 1292"
Cohesion: 0.50
Nodes (4): mquantiles(), Computes empirical quantiles for a data array.      Samples quantile are defined, Calculate the score at the given 'per' percentile of the     sequence a.  For ex, scoreatpercentile()

### Community 1293 - "Community 1293"
Cohesion: 0.50
Nodes (4): convert_type(), is_inexact(), test_xp_result_type_force_floating(), test_xp_result_type_no_force()

### Community 1294 - "Community 1294"
Cohesion: 0.50
Nodes (1): Tests for byteorder module

### Community 1297 - "Community 1297"
Cohesion: 0.50
Nodes (2): Tests underlying quadrature rules (ndim == 1)., TestRulesQuadrature

### Community 1298 - "Community 1298"
Cohesion: 0.67
Nodes (2): _generate_test_points(), test_cython_api()

### Community 1299 - "Community 1299"
Cohesion: 0.50
Nodes (4): test_boost(), _test_factory(), test_gsl(), test_local()

### Community 1300 - "Community 1300"
Cohesion: 0.50
Nodes (1): Testing data types for ndimage calls

### Community 1301 - "Community 1301"
Cohesion: 0.50
Nodes (1): TestDgamma

### Community 1302 - "Community 1302"
Cohesion: 0.50
Nodes (1): TestLogUniform

### Community 1303 - "Community 1303"
Cohesion: 0.50
Nodes (1): TestRdist

### Community 1304 - "Community 1304"
Cohesion: 0.50
Nodes (1): TestRice

### Community 1305 - "Community 1305"
Cohesion: 0.50
Nodes (1): sumsq()

### Community 1308 - "Community 1308"
Cohesion: 0.50
Nodes (1): TestCopheneticDistance

### Community 1309 - "Community 1309"
Cohesion: 0.50
Nodes (1): TestMLabLinkageConversion

### Community 1310 - "Community 1310"
Cohesion: 0.50
Nodes (2): Test possibility of patching fftpack with pyfftw.  No module source outside of s, TestFFTPackImport

### Community 1311 - "Community 1311"
Cohesion: 0.50
Nodes (2): Previous behavior was to sort the returned indices if there were         multipl, _Test_sorted_query_ball_point

### Community 1312 - "Community 1312"
Cohesion: 0.50
Nodes (4): Test Cholesky factorization of a positive definite Rectangular Full     Packed (, test_pftrf(), test_pftri(), test_pftrs()

### Community 1313 - "Community 1313"
Cohesion: 0.50
Nodes (2): Tests for the blocked QR factorization, namely through geqrt, gemqrt, tpqrt, TestBlockedQR

### Community 1316 - "Community 1316"
Cohesion: 0.50
Nodes (1): TestMLS

### Community 1318 - "Community 1318"
Cohesion: 0.50
Nodes (1): Test reading of files not conforming to matlab specification  We try and read an

### Community 1319 - "Community 1319"
Cohesion: 0.50
Nodes (1): Tests for parabolic cylinder functions.

### Community 1321 - "Community 1321"
Cohesion: 0.50
Nodes (1): TestInversion

### Community 1322 - "Community 1322"
Cohesion: 0.50
Nodes (4): _TestDCTIIIBase, TestDCTIIIDouble, TestDCTIIIFloat, TestDCTIIIInt

### Community 1323 - "Community 1323"
Cohesion: 0.50
Nodes (4): _TestDSTIVBase, TestDSTIVDouble, TestDSTIVFloat, TestDSTIVInt

### Community 1325 - "Community 1325"
Cohesion: 0.50
Nodes (4): maybe_warn_gimbal_lock(), test_as_davenport_degenerate(), test_as_euler_degenerate_asymmetric_axes(), test_as_euler_degenerate_symmetric_axes()

### Community 1326 - "Community 1326"
Cohesion: 0.50
Nodes (1): dist

### Community 1327 - "Community 1327"
Cohesion: 0.50
Nodes (2): `scipy.version` may not be quite public, but we install it.      So check that w, test_version_submodule_members()

### Community 1328 - "Community 1328"
Cohesion: 0.50
Nodes (2): Equality constraint, derivative, Scalar equality constraint, derivative

### Community 1329 - "Community 1329"
Cohesion: 0.50
Nodes (1): TestSpectrogram

### Community 1330 - "Community 1330"
Cohesion: 0.50
Nodes (1): TestSphHarm

### Community 1331 - "Community 1331"
Cohesion: 0.50
Nodes (1): TestSphericalInDerivatives

### Community 1332 - "Community 1332"
Cohesion: 0.50
Nodes (1): TestSphericalJnDerivatives

### Community 1334 - "Community 1334"
Cohesion: 0.50
Nodes (1): TestWavelets

### Community 1337 - "Community 1337"
Cohesion: 0.67
Nodes (2): process_global_benchmarks(), Processes the global benchmarks results into pandas DataFrame.      Parameters

### Community 1341 - "Community 1341"
Cohesion: 0.67
Nodes (2): Routine for validation and conversion of csgraph inputs, validate_graph()

### Community 1342 - "Community 1342"
Cohesion: 0.67
Nodes (2): _clear_cache(), Cleans the SciPy datasets cache directory.      Parameters     ----------     da

### Community 1352 - "Community 1352"
Cohesion: 0.67
Nodes (1): Here we perform some symbolic computations required for the N-D interpolation ro

### Community 1354 - "Community 1354"
Cohesion: 0.67
Nodes (2): pade(), Return Pade approximation to a polynomial as the ratio of two polynomials.

### Community 1355 - "Community 1355"
Cohesion: 0.67
Nodes (2): _monomial_powers_impl(), Return the powers for each monomial in a polynomial.      Parameters     -------

### Community 1357 - "Community 1357"
Cohesion: 0.67
Nodes (2): lgmres(), Solve ``Ax = b`` with the LGMRES algorithm.      The LGMRES algorithm [1]_ [2]_

### Community 1358 - "Community 1358"
Cohesion: 0.67
Nodes (2): minres(), Solve ``Ax = b`` with the MINimum RESidual method,     for a real symmetric or c

### Community 1359 - "Community 1359"
Cohesion: 0.67
Nodes (2): Solve ``Ax = b`` with the Transpose-Free Quasi-Minimal Residual method.      Par, tfqmr()

### Community 1360 - "Community 1360"
Cohesion: 0.67
Nodes (1): Perform one integration step.          Returns         -------         message :

### Community 1361 - "Community 1361"
Cohesion: 0.67
Nodes (1): Evaluate the solution.          Parameters         ----------         t : float

### Community 1363 - "Community 1363"
Cohesion: 0.67
Nodes (2): cossin(), Compute the cosine-sine (CS) decomposition of an orthogonal/unitary matrix.

### Community 1364 - "Community 1364"
Cohesion: 0.67
Nodes (2): polar(), Compute the polar decomposition.      Returns the factors of the polar decomposi

### Community 1368 - "Community 1368"
Cohesion: 0.67
Nodes (2): check_unicode(), If showall is True, all non-ASCII characters are displayed.

### Community 1369 - "Community 1369"
Cohesion: 0.67
Nodes (2): get_submodule_paths(), Get paths to submodules so that we can exclude them from things like     check_t

### Community 1374 - "Community 1374"
Cohesion: 0.67
Nodes (2): _minimize_cobyqa(), Minimize a scalar function of one or more variables using the     Constrained Op

### Community 1379 - "Community 1379"
Cohesion: 0.67
Nodes (2): nnls(), Solve ``argmin_x || Ax - b ||_2^2`` for ``x>=0``.      This problem, often calle

### Community 1381 - "Community 1381"
Cohesion: 0.67
Nodes (2): _minimize_trust_krylov(), Minimization of a scalar function of one or more variables using     a nearly ex

### Community 1382 - "Community 1382"
Cohesion: 0.67
Nodes (1): FunctionWithRoot

### Community 1384 - "Community 1384"
Cohesion: 0.67
Nodes (2): my_kde_bandwidth(), We use Scott's Rule, multiplied by a constant factor.

### Community 1385 - "Community 1385"
Cohesion: 0.67
Nodes (2): my_kde_bandwidth(), We use Scott's Rule, multiplied by a constant factor.

### Community 1386 - "Community 1386"
Cohesion: 0.67
Nodes (2): measure(), Measurement model, return two coupled measurements.

### Community 1387 - "Community 1387"
Cohesion: 0.67
Nodes (2): mgc_plot(), Plot sim and MGC-plot

### Community 1388 - "Community 1388"
Cohesion: 0.67
Nodes (2): mgc_plot(), Plot sim and MGC-plot

### Community 1389 - "Community 1389"
Cohesion: 0.67
Nodes (2): mgc_plot(), Plot sim and MGC-plot

### Community 1390 - "Community 1390"
Cohesion: 0.67
Nodes (2): mgc_plot(), Plot sim and MGC-plot

### Community 1391 - "Community 1391"
Cohesion: 0.67
Nodes (2): lagrange_inversion(), Given a series      f(x) = a[1]*x + a[2]*x**2 + ... + a[n-1]*x**(n - 1),      us

### Community 1394 - "Community 1394"
Cohesion: 0.67
Nodes (2): max_len_seq(), Maximum length sequence (MLS) generator.      Parameters     ----------     nbit

### Community 1395 - "Community 1395"
Cohesion: 0.67
Nodes (2): Mode of utilized FFT ('twosided', 'centered', 'onesided' or         'onesided2X', Set mode of FFT.          Allowed values are 'twosided', 'centered', 'onesided',

### Community 1396 - "Community 1396"
Cohesion: 0.67
Nodes (2): Length of input for the FFT used - may be larger than window         length `m_n, Setter for the length of FFT utilized.          See the property `mfft` for furt

### Community 1404 - "Community 1404"
Cohesion: 0.67
Nodes (2): _geometric_slerp(), Geometric spherical linear interpolation.      The interpolation occurs along a

### Community 1406 - "Community 1406"
Cohesion: 0.67
Nodes (3): call_hypergeometric_pFq(), hyp1f1_double(), hyp1f1_wrap()

### Community 1407 - "Community 1407"
Cohesion: 0.67
Nodes (3): erfinv_double(), erfinv_float(), erfinv_wrap()

### Community 1408 - "Community 1408"
Cohesion: 0.67
Nodes (3): ibeta_double(), ibeta_float(), ibeta_wrap()

### Community 1409 - "Community 1409"
Cohesion: 0.67
Nodes (3): ibeta_inv_double(), ibeta_inv_float(), ibeta_inv_wrap()

### Community 1410 - "Community 1410"
Cohesion: 0.67
Nodes (3): ibeta_inva_double(), ibeta_inva_float(), ibeta_inva_wrap()

### Community 1411 - "Community 1411"
Cohesion: 0.67
Nodes (3): ibeta_invb_double(), ibeta_invb_float(), ibeta_invb_wrap()

### Community 1412 - "Community 1412"
Cohesion: 0.67
Nodes (3): ibetac_double(), ibetac_float(), ibetac_wrap()

### Community 1413 - "Community 1413"
Cohesion: 0.67
Nodes (3): ibetac_inv_double(), ibetac_inv_float(), ibetac_inv_wrap()

### Community 1414 - "Community 1414"
Cohesion: 0.67
Nodes (3): lgamma_p_double(), lgamma_p_float(), lgamma_p_wrap()

### Community 1415 - "Community 1415"
Cohesion: 0.67
Nodes (3): lgamma_q_double(), lgamma_q_float(), lgamma_q_wrap()

### Community 1416 - "Community 1416"
Cohesion: 0.67
Nodes (3): nbinom_invn_double(), nbinom_invn_float(), nbinom_invn_wrap()

### Community 1417 - "Community 1417"
Cohesion: 0.67
Nodes (3): powm1_double(), powm1_float(), powm1_wrap()

### Community 1420 - "Community 1420"
Cohesion: 1.00
Nodes (2): cgstrs(), cprint_soln()

### Community 1425 - "Community 1425"
Cohesion: 1.00
Nodes (2): dgstrs(), dprint_soln()

### Community 1444 - "Community 1444"
Cohesion: 1.00
Nodes (2): sgstrs(), sprint_soln()

### Community 1450 - "Community 1450"
Cohesion: 1.00
Nodes (2): zgstrs(), zprint_soln()

### Community 1455 - "Community 1455"
Cohesion: 0.67
Nodes (2): crosstab(), Return table of counts for each possible unique combination in ``*args``.      W

### Community 1458 - "Community 1458"
Cohesion: 0.67
Nodes (2): Compute the coefficient of variation.      The coefficient of variation is the s, variation()

### Community 1460 - "Community 1460"
Cohesion: 1.00
Nodes (2): gen(), main()

### Community 1462 - "Community 1462"
Cohesion: 0.67
Nodes (1): TestBLAS3Syr2k

### Community 1463 - "Community 1463"
Cohesion: 0.67
Nodes (1): TestBetaNBinom

### Community 1464 - "Community 1464"
Cohesion: 0.67
Nodes (1): TestPrototypeType

### Community 1465 - "Community 1465"
Cohesion: 0.67
Nodes (1): TestTf2zpk

### Community 1466 - "Community 1466"
Cohesion: 1.00
Nodes (1): TestInconsistent

### Community 1468 - "Community 1468"
Cohesion: 0.67
Nodes (3): Test conversion routines between the Rectangular Full Packed (RFP) format     an, test_tfttr_trttf(), test_tpttr_trttp()

### Community 1469 - "Community 1469"
Cohesion: 0.67
Nodes (1): TestHetrd

### Community 1470 - "Community 1470"
Cohesion: 0.67
Nodes (1): TestSytrd

### Community 1471 - "Community 1471"
Cohesion: 0.67
Nodes (2): ndimage._measurements._select() is a utility used by other functions., Test_measurements_select

### Community 1472 - "Community 1472"
Cohesion: 0.67
Nodes (2): Here we minimize x^2+y^2 subject to x^2-y^2>1.     The actual minimum is at (0,, TestEmptyConstraint

### Community 1474 - "Community 1474"
Cohesion: 0.67
Nodes (1): Testing miobase module

### Community 1475 - "Community 1475"
Cohesion: 0.67
Nodes (1): TestBinomial

### Community 1476 - "Community 1476"
Cohesion: 0.67
Nodes (1): Used to test passing custom arguments with check_derivative()

### Community 1478 - "Community 1478"
Cohesion: 0.67
Nodes (3): basis_vec(), test_compare_as_davenport_as_euler(), test_compare_from_davenport_from_euler()

### Community 1480 - "Community 1480"
Cohesion: 0.67
Nodes (1): Scalar equality constraint

### Community 1481 - "Community 1481"
Cohesion: 0.67
Nodes (1): Test the minimum spanning tree function

### Community 1484 - "Community 1484"
Cohesion: 0.67
Nodes (1): chirp_linear()

### Community 1485 - "Community 1485"
Cohesion: 0.67
Nodes (1): TestRidderUnderflow

### Community 1486 - "Community 1486"
Cohesion: 0.67
Nodes (1): TestRootResults

### Community 1489 - "Community 1489"
Cohesion: 1.00
Nodes (2): trlib_leftmost(), trlib_leftmost_irreducible()

### Community 1490 - "Community 1490"
Cohesion: 1.00
Nodes (2): parse_txt_data(), run_test()

### Community 1491 - "Community 1491"
Cohesion: 0.67
Nodes (2): generate_test_vecs(), test label with different structuring element neighborhoods

### Community 1492 - "Community 1492"
Cohesion: 1.00
Nodes (1): Eigenvalue solver using iterative methods.  Find k eigenvectors and eigenvalues

### Community 1496 - "Community 1496"
Cohesion: 1.00
Nodes (1): Cython optimize root finding API ================================ The underlying

### Community 1503 - "Community 1503"
Cohesion: 1.00
Nodes (1): Module containing external code ===============================  The code in thi

### Community 1506 - "Community 1506"
Cohesion: 1.00
Nodes (1): ============================================================================== `

### Community 1509 - "Community 1509"
Cohesion: 1.00
Nodes (1): PUBLIC_MODULES was once included in scipy._lib.tests.test_public_api.  It has be

### Community 1510 - "Community 1510"
Cohesion: 1.00
Nodes (1): `uarray` provides functions for generating multimethods that dispatch to multipl

### Community 1516 - "Community 1516"
Cohesion: 1.00
Nodes (1): ============================================================================== `

### Community 1517 - "Community 1517"
Cohesion: 1.00
Nodes (2): check_termination(), Check termination condition for nonlinear least squares.

### Community 1518 - "Community 1518"
Cohesion: 1.00
Nodes (2): CL_scaling_vector(), Compute Coleman-Li scaling vector and its derivatives.      Components of a vect

### Community 1519 - "Community 1519"
Cohesion: 1.00
Nodes (2): compute_grad(), Compute gradient of the least-squares cost function.

### Community 1520 - "Community 1520"
Cohesion: 1.00
Nodes (2): compute_jac_scale(), Compute variables scale based on the Jacobian matrix.

### Community 1521 - "Community 1521"
Cohesion: 1.00
Nodes (2): evaluate_quadratic(), Compute values of a quadratic function arising in least squares.      The functi

### Community 1522 - "Community 1522"
Cohesion: 1.00
Nodes (2): intersect_trust_region(), Find the intersection of a line with the boundary of a trust region.      This f

### Community 1523 - "Community 1523"
Cohesion: 1.00
Nodes (2): minimize_quadratic_1d(), Minimize a 1-D quadratic function subject to bounds.      The free term `c` is 0

### Community 1524 - "Community 1524"
Cohesion: 1.00
Nodes (2): Solve a general trust-region problem in 2 dimensions.      The problem is reform, solve_trust_region_2d()

### Community 1525 - "Community 1525"
Cohesion: 1.00
Nodes (2): Update the radius of a trust region based on the cost reduction.      Returns, update_tr_radius()

### Community 1526 - "Community 1526"
Cohesion: 1.00
Nodes (2): Compute a min_step size required to reach a bound.      The function computes a, step_size_to_bound()

### Community 1527 - "Community 1527"
Cohesion: 1.00
Nodes (2): Solve a trust-region problem arising in least-squares minimization.      This fu, solve_lsq_trust_region()

### Community 1528 - "Community 1528"
Cohesion: 1.00
Nodes (1): This module contains least-squares algorithms.

### Community 1532 - "Community 1532"
Cohesion: 1.00
Nodes (1): This is the 'bare' ndimage API.  This --- private! --- module only collects impl

### Community 1533 - "Community 1533"
Cohesion: 1.00
Nodes (1): Docstring components common to several ndimage functions.

### Community 1534 - "Community 1534"
Cohesion: 1.00
Nodes (2): _add_a_b(), r"""Add "a" and "b" keys to each test from the "bracket" value

### Community 1535 - "Community 1535"
Cohesion: 1.00
Nodes (2): aps01_f(), r"""Straightforward sum of trigonometric function and polynomial

### Community 1536 - "Community 1536"
Cohesion: 1.00
Nodes (2): aps02_f(), r"""poles at x=n**2, 1st and 2nd derivatives at root are also close to 0

### Community 1537 - "Community 1537"
Cohesion: 1.00
Nodes (2): aps03_f(), r"""Rapidly changing at the root

### Community 1538 - "Community 1538"
Cohesion: 1.00
Nodes (2): aps04_f(), r"""Medium-degree polynomial

### Community 1539 - "Community 1539"
Cohesion: 1.00
Nodes (2): aps05_f(), r"""Simple Trigonometric function

### Community 1540 - "Community 1540"
Cohesion: 1.00
Nodes (2): aps06_f(), r"""Exponential rapidly changing from -1 to 1 at x=0

### Community 1541 - "Community 1541"
Cohesion: 1.00
Nodes (2): aps07_f(), r"""Upside down parabola with parametrizable height

### Community 1542 - "Community 1542"
Cohesion: 1.00
Nodes (2): aps08_f(), r"""Degree n polynomial

### Community 1543 - "Community 1543"
Cohesion: 1.00
Nodes (2): aps09_f(), r"""Upside down quartic with parametrizable height

### Community 1544 - "Community 1544"
Cohesion: 1.00
Nodes (2): aps10_f(), r"""Exponential plus a polynomial

### Community 1545 - "Community 1545"
Cohesion: 1.00
Nodes (2): aps11_f(), r"""Rational function with a zero at x=1/n and a pole at x=0

### Community 1546 - "Community 1546"
Cohesion: 1.00
Nodes (2): aps12_f(), r"""nth root of x, with a zero at x=n

### Community 1547 - "Community 1547"
Cohesion: 1.00
Nodes (2): aps13_f(), r"""Function with *all* derivatives 0 at the root

### Community 1548 - "Community 1548"
Cohesion: 1.00
Nodes (2): aps14_f(), r"""0 for negative x-values, trigonometric+linear for x positive

### Community 1549 - "Community 1549"
Cohesion: 1.00
Nodes (2): aps15_f(), r"""piecewise linear, constant outside of [0, 0.002/(1+n)]

### Community 1550 - "Community 1550"
Cohesion: 1.00
Nodes (2): cplx01_f(), r"""z**n-a:  Use to find the nth root of a

### Community 1551 - "Community 1551"
Cohesion: 1.00
Nodes (2): cplx02_f(), r"""e**z - a: Use to find the log of a

### Community 1552 - "Community 1552"
Cohesion: 1.00
Nodes (2): f1(), r"""f1 is a quadratic with roots at 0 and 1

### Community 1553 - "Community 1553"
Cohesion: 1.00
Nodes (2): f2(), r"""f2 is a symmetric parabola, x**2 - 1

### Community 1554 - "Community 1554"
Cohesion: 1.00
Nodes (2): f3(), r"""A quartic with roots at 0, 1, 2 and 3

### Community 1555 - "Community 1555"
Cohesion: 1.00
Nodes (2): f4(), r"""Piecewise linear, left- and right- discontinuous at x=1, the root.

### Community 1556 - "Community 1556"
Cohesion: 1.00
Nodes (2): f5(), r"""     Hyperbola with a pole at x=1, but pole replaced with 0. Not continuous

### Community 1557 - "Community 1557"
Cohesion: 1.00
Nodes (2): get_tests(), r"""Return the requested collection of test cases, as an array of dicts with sub

### Community 1558 - "Community 1558"
Cohesion: 1.00
Nodes (1): Visualize the curse-of-dimensionality.  It presents a saturated design in 1, 2 a

### Community 1559 - "Community 1559"
Cohesion: 1.00
Nodes (1): Calculate the discrepancy of 2 designs and compare them.

### Community 1560 - "Community 1560"
Cohesion: 1.00
Nodes (1): MC vs QMC in terms of space filling.

### Community 1561 - "Community 1561"
Cohesion: 1.00
Nodes (1): Multiple MC to show how it can be bad.

### Community 1562 - "Community 1562"
Cohesion: 1.00
Nodes (1): Sobol' and Halton sequences.

### Community 1564 - "Community 1564"
Cohesion: 1.00
Nodes (1): Distributor init file  Distributors: you can replace the contents of this file w

### Community 1565 - "Community 1565"
Cohesion: 1.00
Nodes (2): _skip_if_poly1d(), sweep_poly_signature()

### Community 1566 - "Community 1566"
Cohesion: 1.00
Nodes (1): ======================================= Signal processing (:mod:`scipy.signal`)

### Community 1568 - "Community 1568"
Cohesion: 1.00
Nodes (1): This is the 'bare' scipy.signal API.  This --- private! --- module only collects

### Community 1573 - "Community 1573"
Cohesion: 1.00
Nodes (2): erf_zeros(), Compute the first nt zero in the first quadrant, ordered by absolute value.

### Community 1574 - "Community 1574"
Cohesion: 1.00
Nodes (2): euler(), Euler numbers E(0), E(1), ..., E(n).      The Euler numbers [1]_ are also known

### Community 1575 - "Community 1575"
Cohesion: 1.00
Nodes (2): fresnel_zeros(), Compute nt complex zeros of sine and cosine Fresnel integrals S(z) and C(z).

### Community 1576 - "Community 1576"
Cohesion: 1.00
Nodes (2): fresnelc_zeros(), Compute nt complex zeros of cosine Fresnel integral C(z).      Parameters     --

### Community 1577 - "Community 1577"
Cohesion: 1.00
Nodes (2): fresnels_zeros(), Compute nt complex zeros of sine Fresnel integral S(z).      Parameters     ----

### Community 1578 - "Community 1578"
Cohesion: 1.00
Nodes (2): jnjnp_zeros(), Compute zeros of integer-order Bessel functions Jn and Jn'.      Results are arr

### Community 1579 - "Community 1579"
Cohesion: 1.00
Nodes (2): kei_zeros(), Compute nt zeros of the Kelvin function kei.      Parameters     ----------

### Community 1580 - "Community 1580"
Cohesion: 1.00
Nodes (2): keip_zeros(), Compute nt zeros of the derivative of the Kelvin function kei.      Parameters

### Community 1581 - "Community 1581"
Cohesion: 1.00
Nodes (2): kelvin_zeros(), Compute `nt` zeros of all Kelvin functions.      Parameters     ----------     n

### Community 1582 - "Community 1582"
Cohesion: 1.00
Nodes (2): ker_zeros(), Compute nt zeros of the Kelvin function ker.      Parameters     ----------

### Community 1583 - "Community 1583"
Cohesion: 1.00
Nodes (2): kerp_zeros(), Compute nt zeros of the derivative of the Kelvin function ker.      Parameters

### Community 1584 - "Community 1584"
Cohesion: 1.00
Nodes (2): lmbda(), r"""Jahnke-Emden Lambda function, Lambdav(x).      This function is defined as [

### Community 1585 - "Community 1585"
Cohesion: 1.00
Nodes (2): lqmn(), Sequence of associated Legendre functions of the second kind.      Computes the

### Community 1586 - "Community 1586"
Cohesion: 1.00
Nodes (2): lqn(), Legendre functions of the second kind.      Compute sequence of Legendre functio

### Community 1587 - "Community 1587"
Cohesion: 1.00
Nodes (2): mathieu_even_coef(), r"""Fourier coefficients for even Mathieu and modified Mathieu functions.      T

### Community 1588 - "Community 1588"
Cohesion: 1.00
Nodes (2): mathieu_odd_coef(), r"""Fourier coefficients for odd Mathieu and modified Mathieu functions.      Th

### Community 1589 - "Community 1589"
Cohesion: 1.00
Nodes (2): obl_cv_seq(), Characteristic values for oblate spheroidal wave functions.      Compute a seque

### Community 1590 - "Community 1590"
Cohesion: 1.00
Nodes (2): pbdn_seq(), Parabolic cylinder functions Dn(z) and derivatives.      Parameters     --------

### Community 1591 - "Community 1591"
Cohesion: 1.00
Nodes (2): pbdv_seq(), Parabolic cylinder functions Dv(x) and derivatives.      Parameters     --------

### Community 1592 - "Community 1592"
Cohesion: 1.00
Nodes (2): pbvv_seq(), Parabolic cylinder functions Vv(x) and derivatives.      Parameters     --------

### Community 1593 - "Community 1593"
Cohesion: 1.00
Nodes (2): perm(), Permutations of N things taken k at a time, i.e., k-permutations of N.      It's

### Community 1594 - "Community 1594"
Cohesion: 1.00
Nodes (2): pro_cv_seq(), Characteristic values for prolate spheroidal wave functions.      Compute a sequ

### Community 1595 - "Community 1595"
Cohesion: 1.00
Nodes (2): r"""Compute Riccati-Bessel function of the first kind and its derivative.      T, riccati_jn()

### Community 1596 - "Community 1596"
Cohesion: 1.00
Nodes (2): Compute Riccati-Bessel function of the second kind and its derivative.      The, riccati_yn()

### Community 1597 - "Community 1597"
Cohesion: 1.00
Nodes (2): r"""Generate Stirling number(s) of the second kind.      Stirling numbers of the, stirling2()

### Community 1598 - "Community 1598"
Cohesion: 1.00
Nodes (2): r"""     Compute the softplus function element-wise.      The softplus function, softplus()

### Community 1599 - "Community 1599"
Cohesion: 1.00
Nodes (2): Compute nt zeros of Bessel function Y0(z), and derivative at each zero.      The, y0_zeros()

### Community 1600 - "Community 1600"
Cohesion: 1.00
Nodes (2): Compute nt zeros of Bessel function Y1(z), and derivative at each zero.      The, y1_zeros()

### Community 1733 - "Community 1733"
Cohesion: 1.00
Nodes (1): Statistics-related constants.

### Community 1734 - "Community 1734"
Cohesion: 1.00
Nodes (1): Sane parameters for stats.distributions.

### Community 1735 - "Community 1735"
Cohesion: 1.00
Nodes (1): =================================================================== Statistical

### Community 1738 - "Community 1738"
Cohesion: 1.00
Nodes (2): Same idea as `test_default_construction_fn_matrices`, but for the     stacking c, test_default_is_matrix_stacks()

### Community 1739 - "Community 1739"
Cohesion: 1.00
Nodes (2): Same idea as `test_default_construction_fn_matrices`, but block functions, test_blocks_default_construction_fn_matrices()

### Community 1743 - "Community 1743"
Cohesion: 1.00
Nodes (1): This test is for backwards compatibility post scipy 1.13.         The behavior o

### Community 1744 - "Community 1744"
Cohesion: 1.00
Nodes (1): This can be removed after sparse matrix is removed

### Community 1745 - "Community 1745"
Cohesion: 1.00
Nodes (1): test for indptr overflow when concatenating matrices

### Community 1746 - "Community 1746"
Cohesion: 1.00
Nodes (1): basic test for block_diag

### Community 1747 - "Community 1747"
Cohesion: 1.00
Nodes (1): block_diag with scalar and 1d arguments

### Community 1748 - "Community 1748"
Cohesion: 1.00
Nodes (1): block_diag with one matrix

### Community 1749 - "Community 1749"
Cohesion: 1.00
Nodes (1): block_diag with sparse arrays

### Community 1753 - "Community 1753"
Cohesion: 1.00
Nodes (2): genz_malik_1980_f_1(), r"""     .. math:: f_1(\mathbf x) = \cos\left(2\pi r + \sum^n_{i = 1}\alpha_i x_

### Community 1754 - "Community 1754"
Cohesion: 1.00
Nodes (2): genz_malik_1980_f_2(), r"""     .. math:: f_2(\mathbf x) = \prod^n_{i = 1} (\alpha_i^2 + (x_i - \beta_i

### Community 1755 - "Community 1755"
Cohesion: 1.00
Nodes (2): genz_malik_1980_f_3(), r"""     .. math:: f_3(\mathbf x) = \exp\left(\sum^n_{i = 1} \alpha_i x_i\right)

### Community 1756 - "Community 1756"
Cohesion: 1.00
Nodes (2): genz_malik_1980_f_4(), r"""     .. math:: f_4(\mathbf x) = \left(1 + \sum^n_{i = 1} \alpha_i x_i\right)

### Community 1757 - "Community 1757"
Cohesion: 1.00
Nodes (2): genz_malik_1980_f_5(), r"""     .. math::          f_5(\mathbf x) = \exp\left(-\sum^n_{i = 1} \alpha^2_

### Community 1760 - "Community 1760"
Cohesion: 1.00
Nodes (1): TestPoissonBinomial

### Community 1761 - "Community 1761"
Cohesion: 1.00
Nodes (1): TestRandInt

### Community 1762 - "Community 1762"
Cohesion: 1.00
Nodes (1): TestZipf

### Community 1764 - "Community 1764"
Cohesion: 1.00
Nodes (2): KDTreeTest(), Class decorator to create test cases for KDTree and cKDTree      Tests use the c

### Community 1765 - "Community 1765"
Cohesion: 1.00
Nodes (2): This test performs an RZ decomposition in which an m x n upper trapezoidal     a, test_tzrzf()

### Community 1766 - "Community 1766"
Cohesion: 1.00
Nodes (2): Test for solving a linear system with the coefficient matrix is a     triangular, test_tfsm()

### Community 1767 - "Community 1767"
Cohesion: 1.00
Nodes (2): This test performs a matrix multiplication with an arbitrary m x n matrix C, test_ormrz_unmrz()

### Community 1768 - "Community 1768"
Cohesion: 1.00
Nodes (2): Test for performing a symmetric rank-k operation for matrix in RFP format., test_sfrk_hfrk()

### Community 1769 - "Community 1769"
Cohesion: 1.00
Nodes (2): Test for going back and forth between the returned format of he/sytrf to     L a, test_syconv()

### Community 1770 - "Community 1770"
Cohesion: 1.00
Nodes (2): Test edge arguments return expected status, test_gejsv_edge_arguments()

### Community 1771 - "Community 1771"
Cohesion: 1.00
Nodes (2): Test invalid job arguments raise an Exception, test_gejsv_invalid_job_arguments()

### Community 1772 - "Community 1772"
Cohesion: 1.00
Nodes (2): This test implements the example found in the NAG manual, f08khf.     An example, test_gejsv_NAG()

### Community 1773 - "Community 1773"
Cohesion: 1.00
Nodes (2): Implements real (f08jgf) example from NAG Manual Mark 26.     Tests for correct, test_pteqr_NAG_f08jgf()

### Community 1774 - "Community 1774"
Cohesion: 1.00
Nodes (2): This test implements the example found in the NAG manual,     f08qfc, f08qtc, f0, test_trexc_NAG()

### Community 1775 - "Community 1775"
Cohesion: 1.00
Nodes (2): This test implements the example found in the NAG manual,     f08qgc, f08quc., test_trsen_NAG()

### Community 1776 - "Community 1776"
Cohesion: 1.00
Nodes (2): Test that all entries are in the doc., test_lapack_documented()

### Community 1777 - "Community 1777"
Cohesion: 1.00
Nodes (1): TestDlasd4

### Community 1778 - "Community 1778"
Cohesion: 1.00
Nodes (1): TestDpotr

### Community 1779 - "Community 1779"
Cohesion: 1.00
Nodes (1): TestRegression

### Community 1780 - "Community 1780"
Cohesion: 1.00
Nodes (1): TestLegendre

### Community 1781 - "Community 1781"
Cohesion: 1.00
Nodes (2): Github issue #3025 - improper merging of labels, test_gh_issue_3025()

### Community 1782 - "Community 1782"
Cohesion: 1.00
Nodes (2): Test dictionary keys and entries, test_value_indices01()

### Community 1783 - "Community 1783"
Cohesion: 1.00
Nodes (2): Test different input array shapes, from 1-D to 4-D, test_value_indices03()

### Community 1786 - "Community 1786"
Cohesion: 1.00
Nodes (2): Test documented equivalence for single transform:     `apply(vector) == translat, test_apply_matrix_equivalence()

### Community 1787 - "Community 1787"
Cohesion: 1.00
Nodes (2): Test documented equivalence for single rotation:     `apply(vectors) == vectors, test_apply_matrix_equivalence()

### Community 1788 - "Community 1788"
Cohesion: 1.00
Nodes (2): Verify spectrogram and cross-spectrogram methods., test_spectrogram()

### Community 1789 - "Community 1789"
Cohesion: 1.00
Nodes (2): Test roundtrip `ifft_func(fft_func(x)) == x` for all permutations of     relevan, test_fft_func_roundtrip()

### Community 1790 - "Community 1790"
Cohesion: 1.00
Nodes (2): Roundtrip for an impulse being at different positions `i`., test_impulse_roundtrip()

### Community 1791 - "Community 1791"
Cohesion: 1.00
Nodes (2): An asymmetric window could uncover indexing problems., test_asymmetric_window_roundtrip()

### Community 1792 - "Community 1792"
Cohesion: 1.00
Nodes (2): Verify that the shortest allowed signal works., test_minimal_length_signal()

### Community 1793 - "Community 1793"
Cohesion: 1.00
Nodes (2): Test the detrending in `ShortTimeFFT.stft_detrend()`., test_compare_stft_detrend()

### Community 1794 - "Community 1794"
Cohesion: 1.00
Nodes (2): Verify example in "Sliding Windows" subsection from the "User Guide".      In :r, test_tutorial_stft_sliding_win()

### Community 1795 - "Community 1795"
Cohesion: 1.00
Nodes (2): Verify STFT example in "Comparison with Legacy Implementation" from the     "Use, test_tutorial_stft_legacy_stft()

### Community 1796 - "Community 1796"
Cohesion: 1.00
Nodes (2): Verify spectrogram example in "Comparison with Legacy Implementation"     from t, test_tutorial_stft_legacy_spectrogram()

### Community 1797 - "Community 1797"
Cohesion: 1.00
Nodes (2): Do roundtrip, i.e., compare dual of dual windows.      The  default for paramete, test_closest_STFT_dual_window_roundtrip()

### Community 1798 - "Community 1798"
Cohesion: 1.00
Nodes (2): Verify correctness of four-dimensional signal by permuting its     shape., test_permute_axes()

### Community 1799 - "Community 1799"
Cohesion: 1.00
Nodes (2): Test roundtrip of a multidimensional input signal versus its components.      Th, test_roundtrip_multidimensional()

### Community 1800 - "Community 1800"
Cohesion: 1.00
Nodes (2): Test roundtrip of a 2 channel input signal with `mfft` set with different     va, test_roundtrip_two_dimensional()

### Community 1801 - "Community 1801"
Cohesion: 1.00
Nodes (2): Roundtrip test adapted from `test_spectral.TestSTFT`.      The parameters are ta, test_roundtrip_windows()

### Community 1802 - "Community 1802"
Cohesion: 1.00
Nodes (2): Test roundtrip for complex-valued window function      The purpose of this test, test_roundtrip_complex_window()

### Community 1803 - "Community 1803"
Cohesion: 1.00
Nodes (1): Vector inequality constraint

### Community 1804 - "Community 1804"
Cohesion: 1.00
Nodes (1): Vector inequality constraint, derivative

### Community 1805 - "Community 1805"
Cohesion: 1.00
Nodes (1): Inequality constraint

### Community 1806 - "Community 1806"
Cohesion: 1.00
Nodes (1): Inequality constraint, derivative

### Community 1807 - "Community 1807"
Cohesion: 1.00
Nodes (1): Test zero-padding for input `x.shape[axis] != y.shape[axis]` for 1d arrays.

### Community 1808 - "Community 1808"
Cohesion: 1.00
Nodes (1): Test zero-padding for input `x.shape[axis] != y.shape[axis]` for 3d arrays.

### Community 1812 - "Community 1812"
Cohesion: 1.00
Nodes (2): Test that array newton fails as expected, test_array_newton_failures()

### Community 1813 - "Community 1813"
Cohesion: 1.00
Nodes (2): Test that Newton or Halley don't warn if zero derivative at root, test_gh8904_zeroder_at_root_fails()

### Community 1814 - "Community 1814"
Cohesion: 1.00
Nodes (2): r"""Test that Halley's method realizes that the 2nd order adjustment     is too, test_gh_8881()

### Community 1815 - "Community 1815"
Cohesion: 1.00
Nodes (2): Test that shape is preserved for array inputs even if fprime or fprime2 is     s, test_gh_9608_preserve_array_shape()

### Community 1816 - "Community 1816"
Cohesion: 1.00
Nodes (2): Test that if the maximum iterations is exceeded that the flag is not     converg, test_gh9254_flag_if_maxiter_exceeded()

### Community 1817 - "Community 1817"
Cohesion: 1.00
Nodes (2): Test that if disp is true then zero derivative raises RuntimeError, test_gh9551_raise_error_if_disp_true()

### Community 1818 - "Community 1818"
Cohesion: 1.00
Nodes (2): Test that zero slope with secant method results in a converged=False, test_gh_14486_converged_false()

### Community 1821 - "Community 1821"
Cohesion: 1.00
Nodes (1): This module contains the equality constrained SQP solver.

### Community 1822 - "Community 1822"
Cohesion: 1.00
Nodes (1): .. note:     If you are looking for overrides for NumPy-specific methods, see th

### Community 1823 - "Community 1823"
Cohesion: 1.00
Nodes (1): Window functions (:mod:`scipy.signal.windows`) =================================

## Knowledge Gaps
- **3095 isolated node(s):** `Airspeed Velocity benchmark utilities`, `Base class with sensible options`, `Base class for benchmarks that are run on multiple Array API backends     and de`, `Skip benchmark if backend/device combination is not available.         Configure`, `Wait until the given arrays have finished generating and return a         synchr` (+3090 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 14`** (1 nodes): `# TODO: Do we want to support this for all Array API frameworks?`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (1 nodes): `TestNdimageMorphology`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `TestSystematic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `TestNdimageFilters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (2 nodes): `Delegators for alternative backends in scipy.signal.  The signature of `func_sig`, `# TODO: fix me - `prominence` is not necessarily an array.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (1 nodes): `TestPdist`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (1 nodes): `TestDifferentialEvolutionSolver`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 68`** (2 nodes): `_dok_base`, `isspmatrix_dok()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 69`** (2 nodes): `BaseQRinsert`, `check_qr()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 100`** (1 nodes): `r""" Parameters used in test and benchmark methods.  Collections of test cases s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 111`** (2 nodes): `# NOTE: tests the reuse of bin_edges from previous call`, `TestBinnedStatistic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 116`** (1 nodes): `Delegators for alternative backends in scipy.ndimage.  The signature of `func_si`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 117`** (2 nodes): `_cs_matrix`, `_process_slice()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 118`** (1 nodes): `TestQR`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 148`** (1 nodes): `BaseQRupdate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 176`** (2 nodes): `Test SLSQP algorithm using Example 14.4 from Numerical Methods for     Engineers`, `TestSLSQP`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 182`** (2 nodes): `assert_unitary()`, `BaseQRdelete`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 183`** (1 nodes): `# TODO: Add a test for ONB?`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 188`** (1 nodes): `TestConstructUtils`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (2 nodes): `_sample_orthonormal_matrix()`, `TestMultivariateNormal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 222`** (1 nodes): `TestDualAnnealing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 223`** (2 nodes): `test_complex()`, `TestInterp1D`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 224`** (1 nodes): `TestAffineTransform`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 225`** (1 nodes): `TestCurveFit`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 242`** (2 nodes): `TestMannWhitneyU`, `TestPoissonMeansTest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 245`** (2 nodes): `Test two failures from gh-20904: int32 and indices-as-None.`, `test_20904()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 265`** (2 nodes): `TestBarycentric`, `TestKrogh`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 266`** (1 nodes): `TestTanhSinh`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 277`** (2 nodes): `_random_covariance()`, `TestMultivariateT`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 280`** (2 nodes): `TestFFTConvolve`, `TestOAConvolve`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 281`** (1 nodes): `_TestLinearFilter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 298`** (1 nodes): `TestTransitionToRNG`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 307`** (2 nodes): `TestMultinomial`, `TestMultivariateHypergeom`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 315`** (1 nodes): `TestMakeTupleBunch`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 321`** (1 nodes): `TestBootstrap`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 333`** (2 nodes): `assert_nlff_less_or_close()`, `TestFit`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 335`** (2 nodes): `TestMMIOArray`, `TestMMIOSparseCSR`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 377`** (1 nodes): `TestLSQ`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 383`** (2 nodes): `_generate_spherical_points()`, `TestGeometricSlerp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 384`** (2 nodes): `Test class for scipy.stats.variation`, `TestVariation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 401`** (1 nodes): `TestGeometricTransform`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 402`** (1 nodes): `TestInterpolativeDecomposition`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 403`** (1 nodes): `BaseMixin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 405`** (1 nodes): `Test_abcd_normalize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 406`** (1 nodes): `TestApproxDerivativesDense`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 411`** (1 nodes): `TestCoherence`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 412`** (2 nodes): `unit tests for sparse utility functions`, `TestSparseUtils`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 421`** (1 nodes): `VarWriter5`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 434`** (1 nodes): `TestUnivariateSpline`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 456`** (1 nodes): `TestFBLAS2Simple`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 460`** (1 nodes): `TestWilcoxon`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 462`** (1 nodes): `TestDirichlet`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 464`** (2 nodes): `TestRegression`, `TestTrimMean`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 485`** (2 nodes): `Test that the reversal of the edges of the input graph works     as expected.`, `test_add_reverse_edges()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 489`** (1 nodes): `Unit test for Mixed Integer Linear Programming`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 493`** (2 nodes): `chirp_geometric()`, `TestChirp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 517`** (2 nodes): `BinopTester`, `BinopTester_with_shape`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 519`** (2 nodes): `TestInsert`, `TestInterop`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 521`** (2 nodes): `TestHyp1f1`, `TestHyperu`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 524`** (2 nodes): `linear_sum_assignment_assertions()`, `test_min_weight_full_matching_small_inputs()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 526`** (1 nodes): `TestOptimizeScalar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 530`** (2 nodes): `TestCorrelateComplex`, `TestCorrelateReal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 531`** (2 nodes): `Some further tests of the spearmanr function.`, `TestCorrSpearmanr2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 554`** (2 nodes): `Compare eigenvalues and eigenvectors of eig_banded            with those of lina`, `TestOverwrite`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 558`** (1 nodes): `TestShift`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 560`** (1 nodes): `TestSplu`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 562`** (1 nodes): `TestNNLS`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 566`** (1 nodes): `TestPartialFractionExpansion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 567`** (2 nodes): `Test if frequency location of peak corresponds to frequency of         generated`, `TestLombscargle`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 589`** (2 nodes): `Check that passing a non-square array raises a ValueError.`, `TestCDF2RDF`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 590`** (1 nodes): `TestGoodnessOfFit`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 591`** (2 nodes): `# NOTE: using a Generator changes the`, `TestHausdorff`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 593`** (2 nodes): `Regression test for gh-8217.`, `test_repeated_t_values()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 594`** (1 nodes): `TestMMIOCoordinate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 595`** (2 nodes): `TestBinaryOpeningClosing`, `TestDilateFix`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 596`** (2 nodes): `Alternative definitions from Matt Haberland.`, `TestUtils`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 598`** (2 nodes): `Verify behavior of scaling parameter.`, `TestSTFT`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 600`** (1 nodes): `TestNSum`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 621`** (1 nodes): `TestBasinHopping`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 622`** (1 nodes): `TestMakeLSQNdBSpline`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 624`** (1 nodes): `TestChi2Contingency`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 627`** (2 nodes): `is_valid_dm_throw()`, `TestIsValidDM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 629`** (2 nodes): `test_optimal_leaf_ordering()`, `TestLinkage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 631`** (1 nodes): `TestZoom`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 634`** (1 nodes): `TestRandomTable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 635`** (1 nodes): `TestMonteCarloHypothesisTest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 636`** (1 nodes): `TestDecimate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 637`** (1 nodes): `TestVectorstrength`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 639`** (1 nodes): `TestZscore`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 663`** (1 nodes): `_TestSlicing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 664`** (2 nodes): `Test parity follows well known identity.          en.wikipedia.org/wiki/Stirling`, `TestStirling2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 665`** (1 nodes): `TestTrigonometric`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 666`** (1 nodes): `TestErf`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 667`** (1 nodes): `TestContinuedFraction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 669`** (1 nodes): `TestCdist`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 670`** (1 nodes): `TestStudentizedRange`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 671`** (1 nodes): `TestTruncnorm`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 672`** (2 nodes): `_complex_correlate()`, `Utility to perform a reference complex-valued convolutions.      When convolve==`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 675`** (2 nodes): `TestGammainc`, `TestGammaincc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 681`** (1 nodes): `TestFactorized`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 685`** (1 nodes): `TestApproxDerivativeLinearOperator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 686`** (2 nodes): `Ensure that we can use pathlib.Path objects in all relevant IO functions.`, `TestPaths`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 696`** (1 nodes): `NdimageInterpolation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 699`** (1 nodes): `TestOddsRatio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 721`** (2 nodes): `Tests fancy indexing features.  The tests for any matrix formats     that implem`, `_TestFancyIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 722`** (1 nodes): `TestCensoredData`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 723`** (1 nodes): `TestCOBYQA`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 725`** (1 nodes): `TestOrdQZ`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 727`** (2 nodes): `is_valid_y_throw()`, `TestIsValidY`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 730`** (1 nodes): `TestNdimageFourier`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 732`** (2 nodes): `BroydenTridiagonal`, `SparseMixin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 735`** (1 nodes): `_assert_infeasible()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 736`** (2 nodes): `# TODO: check that implementation is correct.`, `TestQuantiles`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 738`** (2 nodes): `Check that spline coefficients satisfy the continuity and boundary         condi`, `TestCubicSpline`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 741`** (1 nodes): `TestQuadVec`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 744`** (2 nodes): `MemUsage`, `StructArr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 745`** (2 nodes): `MaximumBipartiteMatching`, `MinWeightFullBipartiteMatching`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 759`** (1 nodes): `TestDIA`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 761`** (2 nodes): `Tests if hstack properly promotes to indices and indptr arrays to np.int64     w`, `test_csr_hstack_int64()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 763`** (1 nodes): `TestJaccard`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 765`** (2 nodes): `Test functions for the sparse.linalg._krylov_funm module.`, `TestKrylovFunmv`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 766`** (2 nodes): `do_solve()`, `TestGCROTMK`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 768`** (1 nodes): `TestIsIsomorphic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 769`** (1 nodes): `TestIsMonotonic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 770`** (1 nodes): `TestRotate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 779`** (2 nodes): `Check that every line in arr1 is only once in arr2`, `Test_HalfspaceIntersection`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 782`** (1 nodes): `TestGSTD`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 803`** (2 nodes): `_apply_filter()`, `_apply_filter_gain()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 805`** (2 nodes): `Tests for betainc, betaincinv, betaincc, betainccinv.`, `TestBetaInc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 806`** (1 nodes): `TestHyper`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 807`** (2 nodes): `Test_Metropolis`, `Test_Storage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 808`** (1 nodes): `TestFBLAS1Simple`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 809`** (1 nodes): `TestFpchec`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 810`** (1 nodes): `TestMakeND`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 811`** (2 nodes): `TestNegativeBinomialFunctions`, `TestNoncentralChiSquaredFunctions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 815`** (1 nodes): `TestSomeDistanceFunctions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 816`** (1 nodes): `TestNumObsY`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 817`** (1 nodes): `TestFitMethod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 818`** (1 nodes): `TestBessel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 820`** (1 nodes): `TestDendrogram`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 822`** (2 nodes): `BoundsMixin`, `TestTRF`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 823`** (2 nodes): `Test that when integrality is a list of all zeros, linprog gives the         sam`, `TestLinprogHiGHSMIP`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 824`** (1 nodes): `TestFindObjects`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 825`** (1 nodes): `TestMMIOReadLargeIntegers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 826`** (2 nodes): `TestLogNdtr`, `TestNdtri`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 827`** (1 nodes): `TestPCHIP`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 829`** (1 nodes): `TestTrimmedStats`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 853`** (2 nodes): `ceil_log2pow5()`, `log2pow5()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 864`** (2 nodes): `intMalloc()`, `SetIWork()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 868`** (1 nodes): `TestLIL`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 869`** (1 nodes): `TestHankel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 870`** (1 nodes): `TestCombinatorics`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 871`** (1 nodes): `TestGamma`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 872`** (2 nodes): `TestMatrixNorms`, `TestVectorNorms`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 875`** (2 nodes): `Test behaviors of B-splines. Some of the values tested against were     returned`, `TestBSplines`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 876`** (1 nodes): `TestGenerateKnots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 881`** (1 nodes): `TestZipfian`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 882`** (2 nodes): `Compare 1d and 2d frequency response.`, `Testfirwin_2d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 883`** (1 nodes): `TestFortranFormatParser`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 884`** (2 nodes): `TestAsLinearOperator`, `TestLinearOperator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 885`** (1 nodes): `TestIsotonicRegression`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 890`** (1 nodes): `TestWatershedIft`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 892`** (2 nodes): `Example code used to generate SAS output:         DATA myData;         INPUT X Y`, `TestMood`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 894`** (2 nodes): `assert_hulls_equal()`, `TestConvexHull`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 897`** (1 nodes): `TestSOSFilt`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 899`** (1 nodes): `Test functions for linalg._solve_toeplitz module`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 901`** (1 nodes): `TestDescribe`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 907`** (1 nodes): `Bench`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 909`** (1 nodes): `Bench`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 911`** (2 nodes): `CMultiWalleniusNCHypergeometric()`, `CMultiWalleniusNCHypergeometricMoments()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 912`** (1 nodes): `tuple`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 922`** (2 nodes): `These are situations that can be tested in our pythran tests:     - A function w`, `_TestPythranFunc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 938`** (2 nodes): `z_abs()`, `z_sgn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 940`** (2 nodes): `showmanyc()`, `underflow()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 941`** (2 nodes): `c_abs()`, `c_sgn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 947`** (1 nodes): `TestNoncentralTFunctions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 949`** (1 nodes): `TestChebyshev`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 950`** (1 nodes): `TestNumObsDM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 951`** (1 nodes): `TestIrwinHall`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 952`** (2 nodes): `test sparse matrix construction functions`, `TestExtract`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 953`** (1 nodes): `TestVectorizedFilter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 954`** (2 nodes): `Unit tests for the global optimization benchmark functions`, `TestGoBenchmarkFunctions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 955`** (1 nodes): `TestIsValidLinkage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 956`** (1 nodes): `TestGMRES`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 957`** (1 nodes): `Test_bode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 958`** (2 nodes): `Test functions for linalg.matmul_toeplitz function`, `TestMatmulToeplitz`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 959`** (1 nodes): `TestTrustRegionConstr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 960`** (1 nodes): `TestFixedPoint`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 962`** (1 nodes): `TestApproxDerivativeSparse`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 963`** (1 nodes): `TestAdjustSchemeToBounds`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 964`** (2 nodes): `TestPdtr`, `TestPdtrc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 968`** (2 nodes): `Check that triangulation works.`, `TestDelaunay`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 969`** (1 nodes): `TestVoronoi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 971`** (2 nodes): `Unit tests for optimization routines from _root.py.`, `TestRoot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 973`** (2 nodes): `TestNumericalInversePolynomial`, `TestSimpleRatioUniforms`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 975`** (1 nodes): `TestSphericalJn`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 995`** (2 nodes): `convert_strides()`, `FIRsepsym2d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1010`** (1 nodes): `_BaseVersion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1014`** (1 nodes): `TestData`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1015`** (1 nodes): `TestArrayTools`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1016`** (1 nodes): `_TestMinMax`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1017`** (2 nodes): `Test for Carlson elliptic integrals ellipr[cdfgj].     The special values used i`, `TestEllipCarlson`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1019`** (1 nodes): `TestParabolicCylinder`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1020`** (1 nodes): `TestMatrix_Balance`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1022`** (1 nodes): `TestFullCoverage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1026`** (1 nodes): `TestKappa4`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1027`** (1 nodes): `TestNct`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1028`** (1 nodes): `TestTruncWeibull`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1029`** (1 nodes): `TestVoigtProfile`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1030`** (2 nodes): `Test the identity transfer function.`, `TestZpk2Tf`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1031`** (1 nodes): `TestThreading`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1032`** (1 nodes): `TestIsValidInconsistent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1033`** (1 nodes): `Test of csgraph public API with int64 index arrays in csr format.  See gh-24629`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1034`** (2 nodes): `TestComplexSolout`, `TestSolout`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1035`** (1 nodes): `TestMapCoordinates`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1036`** (1 nodes): `Test_rectangle`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1037`** (2 nodes): `Test_vectorization_cKDTree`, `Test_vectorization_KDTree`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1039`** (1 nodes): `TestLM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1040`** (2 nodes): `Check that >2-D operators are rejected cleanly.`, `test_nD()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1041`** (1 nodes): `TestSS2TF`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1045`** (2 nodes): `Check input overwrite behavior.`, `TestOverwrite`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1046`** (1 nodes): `TestNumericalInverseHermite`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1047`** (1 nodes): `TestUniqueRoots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1049`** (1 nodes): `TestSphericalKn`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1050`** (1 nodes): `TestSphericalYn`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1051`** (2 nodes): `TestSphericalJnYnCrossProduct`, `TestSphericalKnDerivatives`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1052`** (2 nodes): `See Section 6 of         I. Steinwart, C. Pasin, R.C. Williamson & S. Zhang (201`, `TestExpectile`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1053`** (1 nodes): `TestTTest_1samp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1054`** (2 nodes): `Unit tests for Krylov space trust-region subproblem solver.`, `TestKrylovQuadraticSubproblem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1074`** (2 nodes): `powerlognorm_gen`, `r"""A power log-normal continuous random variable.      %(before_notes)s      No`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1075`** (1 nodes): `TestAiry`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1076`** (1 nodes): `TestSepfir2d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1077`** (2 nodes): `Check the SciPy config is valid.`, `TestSciPyConfigs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1078`** (2 nodes): `Tests that `cubature` gives the correct answer.`, `TestCubatureProblems`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1079`** (1 nodes): `Test Cython optimize zeros API functions: ``bisect``, ``ridder``, ``brenth``, an`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1081`** (1 nodes): `TestNCH`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1082`** (1 nodes): `TestSquareForm`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1083`** (2 nodes): `test_support()`, `TestTukeyLambda`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1084`** (1 nodes): `TestTrapezoid`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1085`** (1 nodes): `Some tests for the documenting decorator and support functions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1088`** (2 nodes): `TestCplxPair`, `TestCplxReal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1089`** (1 nodes): `TestIIRFilter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1092`** (2 nodes): `Check if the GIL is properly released by scipy.interpolate functions.`, `TestGIL`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1094`** (2 nodes): `sparse_distance_matrix_consistency`, `_Test_sparse_distance_matrix`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1095`** (2 nodes): `ExponentialFittingProblem`, `Provide data and function for exponential fitting in the form     y = a + exp(b`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1096`** (1 nodes): `TestSpsolveTriangular`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1098`** (2 nodes): `Perform the most common tests on the poles computed by place_poles         and r`, `TestPlacePoles`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1099`** (1 nodes): `Test_freqresp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1100`** (2 nodes): `ndimage._measurements._stats() is a utility used by other functions.          Si`, `Test_measurements_stats`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1101`** (2 nodes): `This class exists to create a callable that does not have a '__name__' attribute`, `ReturnShape`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1102`** (1 nodes): `TestPlotting`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1103`** (1 nodes): `TestComplex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1104`** (1 nodes): `TestPower`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1107`** (2 nodes): `SphericalDerivativesTestCase`, `TestSphericalYnDerivatives`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1108`** (1 nodes): `TestSphericalIn`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1109`** (2 nodes): `Tests kstest and ks_1samp agree with K-S various sizes, alternatives, modes.`, `TestKSTest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1112`** (1 nodes): `TestGaussPulse`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1121`** (2 nodes): `FortranFormatParser`, `Parser for Fortran format strings. The parse method returns a *Format     instan`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1125`** (2 nodes): `LsodaDenseOutput`, `# IMPORTANT: Must copy solver._y because the C code reuses the same`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1142`** (1 nodes): `doilinks     ~~~~~~~~     Extension to add links to DOIs. With this extension yo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1151`** (2 nodes): `Quick and simple tests for *trmm.`, `TestTRMM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1154`** (1 nodes): `TestReconstructPath`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1158`** (2 nodes): `TestArcsine`, `TestF`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1159`** (1 nodes): `TestGenGamma`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1160`** (1 nodes): `TestLevy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1163`** (1 nodes): `TestInverseErrorFunction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1164`** (1 nodes): `TestNumObsLinkage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1165`** (1 nodes): `TestSpline`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1168`** (1 nodes): `TestGstrsErrors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1170`** (2 nodes): `Regression tests for optimize.`, `TestRegression`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1171`** (2 nodes): `# TODO: use `xp` as backend when cupy works with `rankdata``, `TestMonteCarloMethod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1174`** (1 nodes): `TestSphericalOld`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1175`** (2 nodes): `chirp_hyperbolic()`, `chirp_quadratic()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1176`** (2 nodes): `TestDPSS`, `TestTukey`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1180`** (2 nodes): `Benchmark the solve_toeplitz solver (Levinson recursion)`, `SolveToeplitz`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1194`** (1 nodes): `Integration convergence comparison: MC vs Sobol'.  The function is a synthetic e`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1195`** (1 nodes): `Integration convergence.  The function is a synthetic example specifically desig`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1200`** (2 nodes): `_correlate_nd_imp()`, `scipy_signal__sigtools_correlateND()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1205`** (2 nodes): `multigammaln()`, `r"""Returns the log of multivariate gamma, also sometimes called the     general`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1208`** (2 nodes): `interval_interval_p()`, `rect_rect_p()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1216`** (1 nodes): `_MockFunction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1217`** (2 nodes): `Test real/complex arithmetic`, `_TestArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1218`** (1 nodes): `_TestInplaceArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1219`** (2 nodes): `Test beta and betaln.`, `TestBeta`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1220`** (1 nodes): `TestFresnel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1223`** (1 nodes): `TestBurr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1224`** (1 nodes): `TestRecipInvGauss`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1225`** (1 nodes): `TestCorrespond`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1226`** (1 nodes): `TestFcluster`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1227`** (1 nodes): `TestLeavesList`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1228`** (2 nodes): `count_neighbors_consistency`, `_Test_count_neighbors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1230`** (1 nodes): `TestFlapackSimple`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1231`** (1 nodes): `TestLeastSquaresSolvers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1232`** (1 nodes): `TestNfev`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1234`** (1 nodes): `Test how the ufuncs in special handle nan inputs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1237`** (1 nodes): `TestVertexNeighborVertices`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1238`** (2 nodes): `Verify that the input samples are not mutated in place and that they do`, `TestLloyd`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1240`** (2 nodes): `Arguments:         d     - A list of two elements, where d[0] represents x and d`, `This is the derivative of fun, returning a NumPy array         representing df/d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1241`** (1 nodes): `TestSparseFunctions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1242`** (1 nodes): `_vectorize()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1245`** (1 nodes): `TestChebWin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1252`** (2 nodes): `count_lines()`, `is_all_spaces()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1254`** (2 nodes): `write_body()`, `write_body_sequential()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1255`** (2 nodes): `exec_()`, `footprint()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1257`** (1 nodes): `HighsOptionsManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1260`** (2 nodes): `MarkerCollector`, `Check for functions advertising alt backend support without tests.  This checks`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1266`** (2 nodes): `_maybe_convert_arg()`, `Convert arrays/scalars hiding in the sequence `arg`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1268`** (1 nodes): `Pythran implementation of columns grouping for finite difference Jacobian estima`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1271`** (1 nodes): `StandardNormal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1276`** (1 nodes): `r""" =================================== Sparse arrays (:mod:`scipy.sparse`) ===`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1286`** (2 nodes): `traverse_checking()`, `traverse_no_checking()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1287`** (2 nodes): `traverse_checking()`, `traverse_no_checking()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1288`** (2 nodes): `traverse_checking()`, `traverse_no_checking()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1294`** (1 nodes): `Tests for byteorder module`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1297`** (2 nodes): `Tests underlying quadrature rules (ndim == 1).`, `TestRulesQuadrature`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1298`** (2 nodes): `_generate_test_points()`, `test_cython_api()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1300`** (1 nodes): `Testing data types for ndimage calls`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1301`** (1 nodes): `TestDgamma`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1302`** (1 nodes): `TestLogUniform`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1303`** (1 nodes): `TestRdist`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1304`** (1 nodes): `TestRice`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1305`** (1 nodes): `sumsq()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1308`** (1 nodes): `TestCopheneticDistance`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1309`** (1 nodes): `TestMLabLinkageConversion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1310`** (2 nodes): `Test possibility of patching fftpack with pyfftw.  No module source outside of s`, `TestFFTPackImport`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1311`** (2 nodes): `Previous behavior was to sort the returned indices if there were         multipl`, `_Test_sorted_query_ball_point`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1313`** (2 nodes): `Tests for the blocked QR factorization, namely through geqrt, gemqrt, tpqrt`, `TestBlockedQR`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1316`** (1 nodes): `TestMLS`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1318`** (1 nodes): `Test reading of files not conforming to matlab specification  We try and read an`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1319`** (1 nodes): `Tests for parabolic cylinder functions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1321`** (1 nodes): `TestInversion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1326`** (1 nodes): `dist`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1327`** (2 nodes): ``scipy.version` may not be quite public, but we install it.      So check that w`, `test_version_submodule_members()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1328`** (2 nodes): `Equality constraint, derivative`, `Scalar equality constraint, derivative`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1329`** (1 nodes): `TestSpectrogram`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1330`** (1 nodes): `TestSphHarm`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1331`** (1 nodes): `TestSphericalInDerivatives`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1332`** (1 nodes): `TestSphericalJnDerivatives`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1334`** (1 nodes): `TestWavelets`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1337`** (2 nodes): `process_global_benchmarks()`, `Processes the global benchmarks results into pandas DataFrame.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1341`** (2 nodes): `Routine for validation and conversion of csgraph inputs`, `validate_graph()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1342`** (2 nodes): `_clear_cache()`, `Cleans the SciPy datasets cache directory.      Parameters     ----------     da`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1352`** (1 nodes): `Here we perform some symbolic computations required for the N-D interpolation ro`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1354`** (2 nodes): `pade()`, `Return Pade approximation to a polynomial as the ratio of two polynomials.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1355`** (2 nodes): `_monomial_powers_impl()`, `Return the powers for each monomial in a polynomial.      Parameters     -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1357`** (2 nodes): `lgmres()`, `Solve ``Ax = b`` with the LGMRES algorithm.      The LGMRES algorithm [1]_ [2]_`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1358`** (2 nodes): `minres()`, `Solve ``Ax = b`` with the MINimum RESidual method,     for a real symmetric or c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1359`** (2 nodes): `Solve ``Ax = b`` with the Transpose-Free Quasi-Minimal Residual method.      Par`, `tfqmr()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1360`** (1 nodes): `Perform one integration step.          Returns         -------         message :`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1361`** (1 nodes): `Evaluate the solution.          Parameters         ----------         t : float`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1363`** (2 nodes): `cossin()`, `Compute the cosine-sine (CS) decomposition of an orthogonal/unitary matrix.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1364`** (2 nodes): `polar()`, `Compute the polar decomposition.      Returns the factors of the polar decomposi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1368`** (2 nodes): `check_unicode()`, `If showall is True, all non-ASCII characters are displayed.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1369`** (2 nodes): `get_submodule_paths()`, `Get paths to submodules so that we can exclude them from things like     check_t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1374`** (2 nodes): `_minimize_cobyqa()`, `Minimize a scalar function of one or more variables using the     Constrained Op`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1379`** (2 nodes): `nnls()`, `Solve ``argmin_x || Ax - b ||_2^2`` for ``x>=0``.      This problem, often calle`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1381`** (2 nodes): `_minimize_trust_krylov()`, `Minimization of a scalar function of one or more variables using     a nearly ex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1382`** (1 nodes): `FunctionWithRoot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1384`** (2 nodes): `my_kde_bandwidth()`, `We use Scott's Rule, multiplied by a constant factor.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1385`** (2 nodes): `my_kde_bandwidth()`, `We use Scott's Rule, multiplied by a constant factor.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1386`** (2 nodes): `measure()`, `Measurement model, return two coupled measurements.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1387`** (2 nodes): `mgc_plot()`, `Plot sim and MGC-plot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1388`** (2 nodes): `mgc_plot()`, `Plot sim and MGC-plot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1389`** (2 nodes): `mgc_plot()`, `Plot sim and MGC-plot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1390`** (2 nodes): `mgc_plot()`, `Plot sim and MGC-plot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1391`** (2 nodes): `lagrange_inversion()`, `Given a series      f(x) = a[1]*x + a[2]*x**2 + ... + a[n-1]*x**(n - 1),      us`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1394`** (2 nodes): `max_len_seq()`, `Maximum length sequence (MLS) generator.      Parameters     ----------     nbit`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1395`** (2 nodes): `Mode of utilized FFT ('twosided', 'centered', 'onesided' or         'onesided2X'`, `Set mode of FFT.          Allowed values are 'twosided', 'centered', 'onesided',`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1396`** (2 nodes): `Length of input for the FFT used - may be larger than window         length `m_n`, `Setter for the length of FFT utilized.          See the property `mfft` for furt`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1404`** (2 nodes): `_geometric_slerp()`, `Geometric spherical linear interpolation.      The interpolation occurs along a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1420`** (2 nodes): `cgstrs()`, `cprint_soln()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1425`** (2 nodes): `dgstrs()`, `dprint_soln()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1444`** (2 nodes): `sgstrs()`, `sprint_soln()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1450`** (2 nodes): `zgstrs()`, `zprint_soln()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1455`** (2 nodes): `crosstab()`, `Return table of counts for each possible unique combination in ``*args``.      W`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1458`** (2 nodes): `Compute the coefficient of variation.      The coefficient of variation is the s`, `variation()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1460`** (2 nodes): `gen()`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1462`** (1 nodes): `TestBLAS3Syr2k`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1463`** (1 nodes): `TestBetaNBinom`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1464`** (1 nodes): `TestPrototypeType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1465`** (1 nodes): `TestTf2zpk`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1466`** (1 nodes): `TestInconsistent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1469`** (1 nodes): `TestHetrd`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1470`** (1 nodes): `TestSytrd`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1471`** (2 nodes): `ndimage._measurements._select() is a utility used by other functions.`, `Test_measurements_select`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1472`** (2 nodes): `Here we minimize x^2+y^2 subject to x^2-y^2>1.     The actual minimum is at (0,`, `TestEmptyConstraint`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1474`** (1 nodes): `Testing miobase module`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1475`** (1 nodes): `TestBinomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1476`** (1 nodes): `Used to test passing custom arguments with check_derivative()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1480`** (1 nodes): `Scalar equality constraint`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1481`** (1 nodes): `Test the minimum spanning tree function`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1484`** (1 nodes): `chirp_linear()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1485`** (1 nodes): `TestRidderUnderflow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1486`** (1 nodes): `TestRootResults`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1489`** (2 nodes): `trlib_leftmost()`, `trlib_leftmost_irreducible()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1490`** (2 nodes): `parse_txt_data()`, `run_test()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1491`** (2 nodes): `generate_test_vecs()`, `test label with different structuring element neighborhoods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1492`** (1 nodes): `Eigenvalue solver using iterative methods.  Find k eigenvectors and eigenvalues`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1496`** (1 nodes): `Cython optimize root finding API ================================ The underlying`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1503`** (1 nodes): `Module containing external code ===============================  The code in thi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1506`** (1 nodes): `============================================================================== ``
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1509`** (1 nodes): `PUBLIC_MODULES was once included in scipy._lib.tests.test_public_api.  It has be`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1510`** (1 nodes): ``uarray` provides functions for generating multimethods that dispatch to multipl`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1516`** (1 nodes): `============================================================================== ``
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1517`** (2 nodes): `check_termination()`, `Check termination condition for nonlinear least squares.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1518`** (2 nodes): `CL_scaling_vector()`, `Compute Coleman-Li scaling vector and its derivatives.      Components of a vect`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1519`** (2 nodes): `compute_grad()`, `Compute gradient of the least-squares cost function.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1520`** (2 nodes): `compute_jac_scale()`, `Compute variables scale based on the Jacobian matrix.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1521`** (2 nodes): `evaluate_quadratic()`, `Compute values of a quadratic function arising in least squares.      The functi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1522`** (2 nodes): `intersect_trust_region()`, `Find the intersection of a line with the boundary of a trust region.      This f`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1523`** (2 nodes): `minimize_quadratic_1d()`, `Minimize a 1-D quadratic function subject to bounds.      The free term `c` is 0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1524`** (2 nodes): `Solve a general trust-region problem in 2 dimensions.      The problem is reform`, `solve_trust_region_2d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1525`** (2 nodes): `Update the radius of a trust region based on the cost reduction.      Returns`, `update_tr_radius()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1526`** (2 nodes): `Compute a min_step size required to reach a bound.      The function computes a`, `step_size_to_bound()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1527`** (2 nodes): `Solve a trust-region problem arising in least-squares minimization.      This fu`, `solve_lsq_trust_region()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1528`** (1 nodes): `This module contains least-squares algorithms.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1532`** (1 nodes): `This is the 'bare' ndimage API.  This --- private! --- module only collects impl`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1533`** (1 nodes): `Docstring components common to several ndimage functions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1534`** (2 nodes): `_add_a_b()`, `r"""Add "a" and "b" keys to each test from the "bracket" value`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1535`** (2 nodes): `aps01_f()`, `r"""Straightforward sum of trigonometric function and polynomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1536`** (2 nodes): `aps02_f()`, `r"""poles at x=n**2, 1st and 2nd derivatives at root are also close to 0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1537`** (2 nodes): `aps03_f()`, `r"""Rapidly changing at the root`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1538`** (2 nodes): `aps04_f()`, `r"""Medium-degree polynomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1539`** (2 nodes): `aps05_f()`, `r"""Simple Trigonometric function`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1540`** (2 nodes): `aps06_f()`, `r"""Exponential rapidly changing from -1 to 1 at x=0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1541`** (2 nodes): `aps07_f()`, `r"""Upside down parabola with parametrizable height`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1542`** (2 nodes): `aps08_f()`, `r"""Degree n polynomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1543`** (2 nodes): `aps09_f()`, `r"""Upside down quartic with parametrizable height`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1544`** (2 nodes): `aps10_f()`, `r"""Exponential plus a polynomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1545`** (2 nodes): `aps11_f()`, `r"""Rational function with a zero at x=1/n and a pole at x=0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1546`** (2 nodes): `aps12_f()`, `r"""nth root of x, with a zero at x=n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1547`** (2 nodes): `aps13_f()`, `r"""Function with *all* derivatives 0 at the root`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1548`** (2 nodes): `aps14_f()`, `r"""0 for negative x-values, trigonometric+linear for x positive`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1549`** (2 nodes): `aps15_f()`, `r"""piecewise linear, constant outside of [0, 0.002/(1+n)]`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1550`** (2 nodes): `cplx01_f()`, `r"""z**n-a:  Use to find the nth root of a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1551`** (2 nodes): `cplx02_f()`, `r"""e**z - a: Use to find the log of a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1552`** (2 nodes): `f1()`, `r"""f1 is a quadratic with roots at 0 and 1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1553`** (2 nodes): `f2()`, `r"""f2 is a symmetric parabola, x**2 - 1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1554`** (2 nodes): `f3()`, `r"""A quartic with roots at 0, 1, 2 and 3`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1555`** (2 nodes): `f4()`, `r"""Piecewise linear, left- and right- discontinuous at x=1, the root.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1556`** (2 nodes): `f5()`, `r"""     Hyperbola with a pole at x=1, but pole replaced with 0. Not continuous`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1557`** (2 nodes): `get_tests()`, `r"""Return the requested collection of test cases, as an array of dicts with sub`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1558`** (1 nodes): `Visualize the curse-of-dimensionality.  It presents a saturated design in 1, 2 a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1559`** (1 nodes): `Calculate the discrepancy of 2 designs and compare them.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1560`** (1 nodes): `MC vs QMC in terms of space filling.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1561`** (1 nodes): `Multiple MC to show how it can be bad.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1562`** (1 nodes): `Sobol' and Halton sequences.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1564`** (1 nodes): `Distributor init file  Distributors: you can replace the contents of this file w`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1565`** (2 nodes): `_skip_if_poly1d()`, `sweep_poly_signature()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1566`** (1 nodes): `======================================= Signal processing (:mod:`scipy.signal`)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1568`** (1 nodes): `This is the 'bare' scipy.signal API.  This --- private! --- module only collects`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1573`** (2 nodes): `erf_zeros()`, `Compute the first nt zero in the first quadrant, ordered by absolute value.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1574`** (2 nodes): `euler()`, `Euler numbers E(0), E(1), ..., E(n).      The Euler numbers [1]_ are also known`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1575`** (2 nodes): `fresnel_zeros()`, `Compute nt complex zeros of sine and cosine Fresnel integrals S(z) and C(z).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1576`** (2 nodes): `fresnelc_zeros()`, `Compute nt complex zeros of cosine Fresnel integral C(z).      Parameters     --`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1577`** (2 nodes): `fresnels_zeros()`, `Compute nt complex zeros of sine Fresnel integral S(z).      Parameters     ----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1578`** (2 nodes): `jnjnp_zeros()`, `Compute zeros of integer-order Bessel functions Jn and Jn'.      Results are arr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1579`** (2 nodes): `kei_zeros()`, `Compute nt zeros of the Kelvin function kei.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1580`** (2 nodes): `keip_zeros()`, `Compute nt zeros of the derivative of the Kelvin function kei.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1581`** (2 nodes): `kelvin_zeros()`, `Compute `nt` zeros of all Kelvin functions.      Parameters     ----------     n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1582`** (2 nodes): `ker_zeros()`, `Compute nt zeros of the Kelvin function ker.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1583`** (2 nodes): `kerp_zeros()`, `Compute nt zeros of the derivative of the Kelvin function ker.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1584`** (2 nodes): `lmbda()`, `r"""Jahnke-Emden Lambda function, Lambdav(x).      This function is defined as [`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1585`** (2 nodes): `lqmn()`, `Sequence of associated Legendre functions of the second kind.      Computes the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1586`** (2 nodes): `lqn()`, `Legendre functions of the second kind.      Compute sequence of Legendre functio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1587`** (2 nodes): `mathieu_even_coef()`, `r"""Fourier coefficients for even Mathieu and modified Mathieu functions.      T`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1588`** (2 nodes): `mathieu_odd_coef()`, `r"""Fourier coefficients for odd Mathieu and modified Mathieu functions.      Th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1589`** (2 nodes): `obl_cv_seq()`, `Characteristic values for oblate spheroidal wave functions.      Compute a seque`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1590`** (2 nodes): `pbdn_seq()`, `Parabolic cylinder functions Dn(z) and derivatives.      Parameters     --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1591`** (2 nodes): `pbdv_seq()`, `Parabolic cylinder functions Dv(x) and derivatives.      Parameters     --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1592`** (2 nodes): `pbvv_seq()`, `Parabolic cylinder functions Vv(x) and derivatives.      Parameters     --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1593`** (2 nodes): `perm()`, `Permutations of N things taken k at a time, i.e., k-permutations of N.      It's`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1594`** (2 nodes): `pro_cv_seq()`, `Characteristic values for prolate spheroidal wave functions.      Compute a sequ`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1595`** (2 nodes): `r"""Compute Riccati-Bessel function of the first kind and its derivative.      T`, `riccati_jn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1596`** (2 nodes): `Compute Riccati-Bessel function of the second kind and its derivative.      The`, `riccati_yn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1597`** (2 nodes): `r"""Generate Stirling number(s) of the second kind.      Stirling numbers of the`, `stirling2()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1598`** (2 nodes): `r"""     Compute the softplus function element-wise.      The softplus function`, `softplus()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1599`** (2 nodes): `Compute nt zeros of Bessel function Y0(z), and derivative at each zero.      The`, `y0_zeros()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1600`** (2 nodes): `Compute nt zeros of Bessel function Y1(z), and derivative at each zero.      The`, `y1_zeros()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1733`** (1 nodes): `Statistics-related constants.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1734`** (1 nodes): `Sane parameters for stats.distributions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1735`** (1 nodes): `=================================================================== Statistical`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1738`** (2 nodes): `Same idea as `test_default_construction_fn_matrices`, but for the     stacking c`, `test_default_is_matrix_stacks()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1739`** (2 nodes): `Same idea as `test_default_construction_fn_matrices`, but block functions`, `test_blocks_default_construction_fn_matrices()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1743`** (1 nodes): `This test is for backwards compatibility post scipy 1.13.         The behavior o`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1744`** (1 nodes): `This can be removed after sparse matrix is removed`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1745`** (1 nodes): `test for indptr overflow when concatenating matrices`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1746`** (1 nodes): `basic test for block_diag`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1747`** (1 nodes): `block_diag with scalar and 1d arguments`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1748`** (1 nodes): `block_diag with one matrix`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1749`** (1 nodes): `block_diag with sparse arrays`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1753`** (2 nodes): `genz_malik_1980_f_1()`, `r"""     .. math:: f_1(\mathbf x) = \cos\left(2\pi r + \sum^n_{i = 1}\alpha_i x_`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1754`** (2 nodes): `genz_malik_1980_f_2()`, `r"""     .. math:: f_2(\mathbf x) = \prod^n_{i = 1} (\alpha_i^2 + (x_i - \beta_i`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1755`** (2 nodes): `genz_malik_1980_f_3()`, `r"""     .. math:: f_3(\mathbf x) = \exp\left(\sum^n_{i = 1} \alpha_i x_i\right)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1756`** (2 nodes): `genz_malik_1980_f_4()`, `r"""     .. math:: f_4(\mathbf x) = \left(1 + \sum^n_{i = 1} \alpha_i x_i\right)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1757`** (2 nodes): `genz_malik_1980_f_5()`, `r"""     .. math::          f_5(\mathbf x) = \exp\left(-\sum^n_{i = 1} \alpha^2_`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1760`** (1 nodes): `TestPoissonBinomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1761`** (1 nodes): `TestRandInt`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1762`** (1 nodes): `TestZipf`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1764`** (2 nodes): `KDTreeTest()`, `Class decorator to create test cases for KDTree and cKDTree      Tests use the c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1765`** (2 nodes): `This test performs an RZ decomposition in which an m x n upper trapezoidal     a`, `test_tzrzf()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1766`** (2 nodes): `Test for solving a linear system with the coefficient matrix is a     triangular`, `test_tfsm()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1767`** (2 nodes): `This test performs a matrix multiplication with an arbitrary m x n matrix C`, `test_ormrz_unmrz()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1768`** (2 nodes): `Test for performing a symmetric rank-k operation for matrix in RFP format.`, `test_sfrk_hfrk()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1769`** (2 nodes): `Test for going back and forth between the returned format of he/sytrf to     L a`, `test_syconv()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1770`** (2 nodes): `Test edge arguments return expected status`, `test_gejsv_edge_arguments()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1771`** (2 nodes): `Test invalid job arguments raise an Exception`, `test_gejsv_invalid_job_arguments()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1772`** (2 nodes): `This test implements the example found in the NAG manual, f08khf.     An example`, `test_gejsv_NAG()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1773`** (2 nodes): `Implements real (f08jgf) example from NAG Manual Mark 26.     Tests for correct`, `test_pteqr_NAG_f08jgf()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1774`** (2 nodes): `This test implements the example found in the NAG manual,     f08qfc, f08qtc, f0`, `test_trexc_NAG()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1775`** (2 nodes): `This test implements the example found in the NAG manual,     f08qgc, f08quc.`, `test_trsen_NAG()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1776`** (2 nodes): `Test that all entries are in the doc.`, `test_lapack_documented()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1777`** (1 nodes): `TestDlasd4`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1778`** (1 nodes): `TestDpotr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1779`** (1 nodes): `TestRegression`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1780`** (1 nodes): `TestLegendre`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1781`** (2 nodes): `Github issue #3025 - improper merging of labels`, `test_gh_issue_3025()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1782`** (2 nodes): `Test dictionary keys and entries`, `test_value_indices01()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1783`** (2 nodes): `Test different input array shapes, from 1-D to 4-D`, `test_value_indices03()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1786`** (2 nodes): `Test documented equivalence for single transform:     `apply(vector) == translat`, `test_apply_matrix_equivalence()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1787`** (2 nodes): `Test documented equivalence for single rotation:     `apply(vectors) == vectors`, `test_apply_matrix_equivalence()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1788`** (2 nodes): `Verify spectrogram and cross-spectrogram methods.`, `test_spectrogram()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1789`** (2 nodes): `Test roundtrip `ifft_func(fft_func(x)) == x` for all permutations of     relevan`, `test_fft_func_roundtrip()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1790`** (2 nodes): `Roundtrip for an impulse being at different positions `i`.`, `test_impulse_roundtrip()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1791`** (2 nodes): `An asymmetric window could uncover indexing problems.`, `test_asymmetric_window_roundtrip()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1792`** (2 nodes): `Verify that the shortest allowed signal works.`, `test_minimal_length_signal()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1793`** (2 nodes): `Test the detrending in `ShortTimeFFT.stft_detrend()`.`, `test_compare_stft_detrend()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1794`** (2 nodes): `Verify example in "Sliding Windows" subsection from the "User Guide".      In :r`, `test_tutorial_stft_sliding_win()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1795`** (2 nodes): `Verify STFT example in "Comparison with Legacy Implementation" from the     "Use`, `test_tutorial_stft_legacy_stft()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1796`** (2 nodes): `Verify spectrogram example in "Comparison with Legacy Implementation"     from t`, `test_tutorial_stft_legacy_spectrogram()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1797`** (2 nodes): `Do roundtrip, i.e., compare dual of dual windows.      The  default for paramete`, `test_closest_STFT_dual_window_roundtrip()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1798`** (2 nodes): `Verify correctness of four-dimensional signal by permuting its     shape.`, `test_permute_axes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1799`** (2 nodes): `Test roundtrip of a multidimensional input signal versus its components.      Th`, `test_roundtrip_multidimensional()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1800`** (2 nodes): `Test roundtrip of a 2 channel input signal with `mfft` set with different     va`, `test_roundtrip_two_dimensional()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1801`** (2 nodes): `Roundtrip test adapted from `test_spectral.TestSTFT`.      The parameters are ta`, `test_roundtrip_windows()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1802`** (2 nodes): `Test roundtrip for complex-valued window function      The purpose of this test`, `test_roundtrip_complex_window()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1803`** (1 nodes): `Vector inequality constraint`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1804`** (1 nodes): `Vector inequality constraint, derivative`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1805`** (1 nodes): `Inequality constraint`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1806`** (1 nodes): `Inequality constraint, derivative`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1807`** (1 nodes): `Test zero-padding for input `x.shape[axis] != y.shape[axis]` for 1d arrays.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1808`** (1 nodes): `Test zero-padding for input `x.shape[axis] != y.shape[axis]` for 3d arrays.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1812`** (2 nodes): `Test that array newton fails as expected`, `test_array_newton_failures()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1813`** (2 nodes): `Test that Newton or Halley don't warn if zero derivative at root`, `test_gh8904_zeroder_at_root_fails()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1814`** (2 nodes): `r"""Test that Halley's method realizes that the 2nd order adjustment     is too`, `test_gh_8881()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1815`** (2 nodes): `Test that shape is preserved for array inputs even if fprime or fprime2 is     s`, `test_gh_9608_preserve_array_shape()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1816`** (2 nodes): `Test that if the maximum iterations is exceeded that the flag is not     converg`, `test_gh9254_flag_if_maxiter_exceeded()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1817`** (2 nodes): `Test that if disp is true then zero derivative raises RuntimeError`, `test_gh9551_raise_error_if_disp_true()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1818`** (2 nodes): `Test that zero slope with secant method results in a converged=False`, `test_gh_14486_converged_false()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1821`** (1 nodes): `This module contains the equality constrained SQP solver.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1822`** (1 nodes): `.. note:     If you are looking for overrides for NumPy-specific methods, see th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1823`** (1 nodes): `Window functions (:mod:`scipy.signal.windows`) =================================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FunctionDoc` connect `Community 2` to `Community 195`, `Community 25`, `Community 21`, `Community 376`, `Community 3`, `Community 13`, `Community 0`, `Community 11`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Why does `MapWrapper` connect `Community 21` to `Community 342`, `Community 324`, `Community 2`, `Community 393`, `Community 23`, `Community 28`, `Community 10`, `Community 17`, `Community 41`, `Community 513`, `Community 963`, `Community 685`, `Community 406`, `Community 962`, `Community 8`, `Community 526`, `Community 309`, `Community 298`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._
- **Why does `SmallSampleWarning` connect `Community 3` to `Community 376`, `Community 2`, `Community 325`, `Community 381`, `Community 56`, `Community 630`, `Community 242`, `Community 7`, `Community 892`, `Community 460`, `Community 44`, `Community 63`, `Community 74`, `Community 33`, `Community 531`, `Community 55`, `Community 1109`, `Community 246`, `Community 976`, `Community 282`, `Community 234`, `Community 308`, `Community 638`, `Community 1052`, `Community 599`, `Community 901`, `Community 782`, `Community 66`, `Community 40`, `Community 464`, `Community 829`, `Community 1053`, `Community 639`, `Community 384`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **Are the 428 inferred relationships involving `Benchmark` (e.g. with `Ackley01` and `Ackley02`) actually correct?**
  _`Benchmark` has 428 INFERRED edges - model-reasoned connections that need verification._
- **Are the 321 inferred relationships involving `CensoredData` (e.g. with `alpha_gen` and `anglit_gen`) actually correct?**
  _`CensoredData` has 321 INFERRED edges - model-reasoned connections that need verification._
- **Are the 309 inferred relationships involving `FitError` (e.g. with `alpha_gen` and `anglit_gen`) actually correct?**
  _`FitError` has 309 INFERRED edges - model-reasoned connections that need verification._
- **Are the 295 inferred relationships involving `SmallSampleWarning` (e.g. with `FunctionDoc` and `AlexanderGovernResult`) actually correct?**
  _`SmallSampleWarning` has 295 INFERRED edges - model-reasoned connections that need verification._