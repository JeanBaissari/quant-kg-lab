# Graph Report - knowledge_graphs/arch/repo/arch  (2026-08-13)

## Corpus Check
- 73 files · ~93,237 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1368 nodes · 3900 edges · 116 communities detected
- Extraction: 44% EXTRACTED · 56% INFERRED · 0% AMBIGUOUS · INFERRED: 2181 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: uses: 2181 · method: 650 · rationale_for: 417 · calls: 315 · contains: 219 · inherits: 82 · imports_from: 36


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 73 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `704bb70`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `AbstractDocStringInheritor` - 249 edges
2. `Normal` - 186 edges
3. `VolatilityProcess` - 149 edges
4. `Distribution` - 132 edges
5. `ConstantVariance` - 126 edges
6. `WaldTestStatistic` - 82 edges
7. `ConvergenceWarning` - 74 edges
8. `StartingValueWarning` - 74 edges
9. `DataScaleWarning` - 74 edges
10. `Substitution` - 72 edges

## Surprising Connections (you probably didn't know these)
- `Distributions to use in ARCH models.  All distributions must inherit from :class` --uses--> `AbstractDocStringInheritor`  [INFERRED]
  univariate/distribution.py → utility/array.py
- `Generalized Error distribution for use with ARCH models      Parameters     ----` --uses--> `AbstractDocStringInheritor`  [INFERRED]
  univariate/distribution.py → utility/array.py
- `r"""         Partial moment for ordinary generalized normal parameterization.` --uses--> `AbstractDocStringInheritor`  [INFERRED]
  univariate/distribution.py → utility/array.py
- `r"""Computes the log-likelihood of assuming residuals are normally         distr` --uses--> `AbstractDocStringInheritor`  [INFERRED]
  univariate/distribution.py → utility/array.py
- `Standardized Student's distribution for use with ARCH models      Parameters` --uses--> `AbstractDocStringInheritor`  [INFERRED]
  univariate/distribution.py → utility/array.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (26): _add_extra_kwargs(), _get_prng_state(), IIDBootstrap, IndependentSamplesBootstrap, Compute parameter covariance using bootstrap          Parameters         -------, Compute parameter variance using bootstrap          Parameters         ---------, Resample all data using the values in _index, Bootstrap where each input is independently resampled      Parameters     ------ (+18 more)

### Community 1 - "Community 1"
Cohesion: 0.09
Nodes (24): CircularBlockBootstrap, MovingBlockBootstrap, Bootstrap using blocks of the same length with end-to-start wrap around      Par, Bootstrap using blocks of the same length without wrap around      Parameters, Tools for implementing statistical bootstraps, _info_to_str(), MultipleComparison, StepM multiple comparison procedure of Romano and Wolf.      Parameters     ---- (+16 more)

### Community 2 - "Community 2"
Cohesion: 0.10
Nodes (20): ARCHModel, Abstract base class for mean models in ARCH processes.  Specifies the     condit, Construct linear constraint arrays  for use in non-linear optimization, Construct bounds for parameters to use in non-linear optimization          Retur, Called when the scale has changed.  This allows the model         to update any, Computes the model r-square.  Optional to over-ride.  Must match         signatu, Must be overridden with closed form estimator the return parameters ony, Must be overridden with closed form estimator (+12 more)

### Community 3 - "Community 3"
Cohesion: 0.07
Nodes (19): Bartlett, CovarianceEstimator, NeweyWest, r"""     %(kernel_name)s kernel covariance estimation.      Parameters     -----, The covariance estimator's name.          Returns         -------         str, The bandwidth used by the covariance estimator.          Returns         -------, Flag indicating whether the data are centered (demeaned).           Returns, The constant used in optimal bandwidth calculation.          Returns         --- (+11 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (21): NamedTuple, estimate_cv_regression(), fit_pval_model(), PvalueResult, # TODO: Bug in pandas-stubs prevents valid index types, # TODO: Bug in pandas-stubs prevents valid index types, # TODO: Bug in pandas-stubs prevents valid index types, # TODO: Bug in pandas-stubs prevents valid index types (+13 more)

### Community 5 - "Community 5"
Cohesion: 0.07
Nodes (21): engle_granger(), engle_granger_cv(), engle_granger_pval(), Results class for Engle-Granger cointegration tests.      Parameters     -------, The number of lags used in the Augmented Dickey-Fuller regression., The maximum number of lags used in the lag-length selection., r"""         The estimated coefficient in the Dickey-Fuller Test          Return, Summary of test, containing statistic, p-value and critical values (+13 more)

### Community 6 - "Community 6"
Cohesion: 0.06
Nodes (21): r"""         Computes the log-likelihood of assuming residuals are have a, Construct starting values for use in optimization.          Parameters         -, Simulates i.i.d. draws from the distribution          Parameters         -------, Construct arrays to use in constrained optimization.          Returns         --, Parameter bounds for use in optimization.          Parameters         ----------, Loglikelihood evaluation.          Parameters         ----------         paramet, Construct starting values for use in optimization.          Parameters         -, Names of distribution shape parameters          Returns         ------- (+13 more)

### Community 7 - "Community 7"
Cohesion: 0.11
Nodes (19): ARCHModelFixedResult, format_float_fixed(), Results for fixed parameters for an ARCHModel model      Parameters     --------, Constructs a summary of the results from a fit model.          Returns         -, Model instance used to produce the fit, Akaike Information Criteria          -2 * loglikelihood + 2 * num_params, Number of parameters in model, Schwarz/Bayesian Information Criteria          -2 * loglikelihood + log(nobs) * (+11 more)

### Community 8 - "Community 8"
Cohesion: 0.09
Nodes (14): RuntimeWarning, _CommonCointegrationResults, The estimated parameter covariance of the cointegrating vector, The kernel used to estimate the covariance, The degree-of-freedom adjusted R², r"""         The variance of the regression residual.          Returns         -, The long-run variance of the regression residual.          Returns         -----, Summary of the model, containing estimated parameters and std. errors          R (+6 more)

### Community 9 - "Community 9"
Cohesion: 0.09
Nodes (17): _align_forecast(), ARCHModelForecast, _callback(), constraint(), _format_forecasts(), implicit_constant(), Core classes for ARCH models, Generate constraints from arrays      Parameters     ----------     a : ndarray (+9 more)

### Community 10 - "Community 10"
Cohesion: 0.10
Nodes (14): ARCHModelResult, Results from estimation of an ARCHModel model      Parameters     ----------, The scale applied to the original data before estimating the model.          If, Parameter confidence intervals          Parameters         ----------         al, Constructs a summary of the results from a fit model.          Returns         -, Start of sample used to estimate parameters, End of sample used to estimate parameters, Degree of freedom adjusted R-squared (+6 more)

### Community 11 - "Community 11"
Cohesion: 0.11
Nodes (14): Base class to be used for inheritance in unit root bootstrap, Display as HTML for IPython notebook., Check that the data are compatible with running a test., This is the core routine that computes the test statistic, computes         the, The alternative hypothesis, The number of observations used when computing the test statistic.         Accou, List of valid trend terms., Summary of test, containing statistic, p-value and critical values (+6 more)

### Community 12 - "Community 12"
Cohesion: 0.11
Nodes (22): _add_column_names(), auto_bandwidth(), _autolag_ols(), _autolag_ols_low_memory(), _df_select_lags(), _estimate_df_regression(), _is_reduced_rank(), mackinnoncrit() (+14 more)

### Community 13 - "Community 13"
Cohesion: 0.10
Nodes (6): r"""         Partial moment for ordinary generalized normal parameterization., r"""         Partial moments for ordinary parameterization of Students t df=nu, r"""         Computes the log-likelihood of assuming residuals are have a, Compute a constant.          Parameters         ----------         parameters :, Compute b constant.          Parameters         ----------         parameters :, Compute c constant.          Parameters         ----------         parameters :

### Community 14 - "Community 14"
Cohesion: 0.14
Nodes (26): Volatility processes for ARCH model estimation.  All volatility processes must i, Compute variance recursion for EWMA/RiskMetrics Variance      Parameters     ---, r"""     Heterogeneous ARCH process      Parameters     ----------     lags : {l, Container for variance forecasts      Parameters     ----------     forecasts :, r"""     MIDAS Hyperbolic ARCH process      Parameters     ----------     m : in, Constraints          Notes         -----         Parameters are (omega, alpha, g, The variance forecasts, The variance forecast paths (+18 more)

### Community 15 - "Community 15"
Cohesion: 0.08
Nodes (20): aparch_recursion_python(), arch_recursion_python(), egarch_recursion_python(), EWMAUpdater, figarch_recursion_python(), figarch_weights_python(), garch_core_python(), garch_recursion_python() (+12 more)

### Community 16 - "Community 16"
Cohesion: 0.09
Nodes (6): Gallant, Parzen, ParzenCauchy, ParzenGeometric, ParzenRiesz, Alternative name for Parzen covariance estimator.      See Also     --------

### Community 17 - "Community 17"
Cohesion: 0.12
Nodes (12): PhillipsPerron, Returns the OLS regression results from the ADF model estimated, Phillips-Perron unit root test      Parameters     ----------     y : {ndarray,, Gets or sets the test type returned by stat.         Valid values are "tau" or ", Returns OLS regression results for the specification used in the test          T, Checks whether the statistic needs to be computed, and computed if         neede, Returns the p-value for the test statistic, The test statistic for a unit root (+4 more)

### Community 18 - "Community 18"
Cohesion: 0.11
Nodes (8): ARCHModelForecastSimulation, Container for a simulation or bootstrap-based forecasts from an ARCH Model, The index aligned to dimension 0 of the simulation paths, The values of the process, Simulated residuals used to produce the values, Simulated variances of the values, Simulated variance of the residuals, Normal

### Community 19 - "Community 19"
Cohesion: 0.14
Nodes (9): ARCHModel, HARX, r"""     Heterogeneous Autoregression (HAR), with optional exogenous regressors,, Called when the scale has changed.  This allows the model         to update any, Checks the specification for obvious errors, Reformat input lags to be a 2 by m array, which simplifies other         operati, Should be called whenever the model is initialized or changed, Estimates model parameters          Parameters         ----------         cov_ty (+1 more)

### Community 20 - "Community 20"
Cohesion: 0.12
Nodes (12): DynamicOLSResults, Estimation results for Dynamic OLS models      Parameters     ----------     par, The complete set of parameters, including leads and lags, Parameter covariance of the all model parameters, incl. leads and lags, The number of lags included in the model, The number of leads included in the model, The type of parameter covariance estimator used, Appender (+4 more)

### Community 21 - "Community 21"
Cohesion: 0.10
Nodes (6): r"""     Standardized Skewed Student's distribution for use with ARCH models, SkewStudent, ARCHInMean, r"""     (G)ARCH-in-mean model and simulation      Parameters     ----------, The form of the conditional variance in the mean, Parameters         ----------         parameters         x         errors

### Community 22 - "Community 22"
Cohesion: 0.10
Nodes (12): dataset_loader(), Load a dataset using the new syntax is possible, Simulation of ADF z-test critical values.  Closely follows MacKinnon (2010)., Wraps and blocks the main simulation so that the maximum amount of memory     ca, single_experiment(), Simulation of ADF z-test critical values.  Closely follows MacKinnon (2010). Run, Wraps and blocks the main simulation so that the maximum amount of memory     ca, wrapper() (+4 more)

### Community 23 - "Community 23"
Cohesion: 0.11
Nodes (14): ABC, ABCMeta, Distributions to use in ARCH models.  All distributions must inherit from :class, ConcreteClassMeta, cutoff_to_index(), date_to_index(), find_index(), Utility functions that do not explicitly relate to Volatility modeling (+6 more)

### Community 24 - "Community 24"
Cohesion: 0.17
Nodes (10): Politis and Romano (1994) bootstrap with expon distributed block sizes      Para, StationaryBootstrap, MCS, Compute the set of models in the confidence set., Computes the model confidence set using the R method, Computes the model confidence set using the R method, List of model indices that are included in the MCS          Returns         ----, List of model indices that are excluded from the MCS          Returns         -- (+2 more)

### Community 25 - "Community 25"
Cohesion: 0.11
Nodes (7): Construct forecasts from estimated model          Parameters         ----------, Set or gets the error distribution          Distributions must be a subclass of, Number of parameters in the model, P-value of test statistic, Critical values test for common test sizes, Test statistic holder for Wald-type tests      Parameters     ----------     sta, WaldTestStatistic

### Community 26 - "Community 26"
Cohesion: 0.17
Nodes (2): ewma_recursion(), RiskMetrics2006

### Community 27 - "Community 27"
Cohesion: 0.20
Nodes (9): ResidualCointegrationTestResult, DynamicOLS, r"""     Dynamic OLS (DOLS) cointegrating vector estimation      Parameters, Format the variables for the regression, Compute an info criterion, Select the optimal number of leads and lags, r"""         Estimate the Dynamic OLS regression          Parameters         ---, Estimate the covariance (+1 more)

### Community 28 - "Community 28"
Cohesion: 0.18
Nodes (12): phillips_ouliaris(), phillips_ouliaris_cv(), phillips_ouliaris_pval(), PhillipsOuliarisTestResults, _po_ptests(), _po_ztests(), r"""     Test for cointegration within a set of time series.      Parameters, Name of the long-run covariance estimator (+4 more)

### Community 29 - "Community 29"
Cohesion: 0.13
Nodes (5): Standardized Student's distribution for use with ARCH models      Parameters, StudentsT, ConstantMean, r"""     Constant mean model estimation and simulation.      Parameters     ----, Simulated data from a constant mean model          Parameters         ----------

### Community 30 - "Community 30"
Cohesion: 0.18
Nodes (1): VarianceForecast

### Community 31 - "Community 31"
Cohesion: 0.13
Nodes (2): _common_names(), GARCH

### Community 32 - "Community 32"
Cohesion: 0.16
Nodes (8): CovarianceEstimate, The long-run covariance estimate., The short-run covariance estimate., The one-sided covariance estimate., The one-sided strict covariance estimate., r"""     Covariance estimate using a long-run covariance estimator      Paramete, The bandwidth used in the parameter covariance estimation, P-value of the parameters in the cointegrating vector

### Community 33 - "Community 33"
Cohesion: 0.18
Nodes (8): RuntimeError, Variance Ratio test of a random walk.      Parameters     ----------     y : {nd, The ratio of the long block lags-period variance         to the 1-period varianc, Sets of gets the indicator to use overlapping returns in the         long-period, Sets of gets the indicator to use a heteroskedasticity robust         variance e, Sets of gets the indicator to use debiased variances in the ratio, VarianceRatio, InfeasibleTestException

### Community 34 - "Community 34"
Cohesion: 0.14
Nodes (3): Returns the number of parameters, Estimates model parameters excluding sigma2          Returns         -------, HARCH

### Community 35 - "Community 35"
Cohesion: 0.16
Nodes (10): _get_acceleration(), _loo_jackknife(), MOONBootstrap, optimal_block_length(), r"""     Estimate optimal window length for time-series bootstraps      Paramete, # TODO: This should use overload ensure2d definitions to know it is ndarray, Estimates the BCa acceleration parameter using jackknife estimates     of theta., Leave one out jackknife estimation      Parameters     ----------     func : cal (+2 more)

### Community 36 - "Community 36"
Cohesion: 0.22
Nodes (5): CanonicalCointegratingReg, CointegrationAnalysisResults, FullyModifiedOLS, Estimate the cointegrating vector.          Parameters         ----------, Long-run variance estimate used in the parameter covariance estimator

### Community 37 - "Community 37"
Cohesion: 0.14
Nodes (3): Simulates data from a linear regression, AR or HAR models          Parameters, Generates variable names or use in summaries, EGARCH

### Community 38 - "Community 38"
Cohesion: 0.14
Nodes (2): Gets the value of the exogenous regressors in the model, FIGARCH

### Community 39 - "Community 39"
Cohesion: 0.18
Nodes (7): _ar_forecast(), _ar_to_impulse(), _forecast_pad(), Mean models to use with ARCH processes.  All mean models must inherit from :clas, # TODO: This is not tested, but probably right, Generate mean forecasts from an AR-X model      Parameters     ----------     y, Always return a correctly formatted 3-d array          Parameters         ------

### Community 40 - "Community 40"
Cohesion: 0.18
Nodes (6): GeneralizedError, Generalized Error distribution for use with ARCH models      Parameters     ----, arch_model(), LS, r"""     Least squares model estimation and simulation      Parameters     -----, Initialization of common ARCH model specifications      Parameters     ---------

### Community 41 - "Community 41"
Cohesion: 0.19
Nodes (6): ARX, r"""     Autoregressive model with optional exogenous regressors estimation and, Generates the model description for use by __str__ and related         functions, Generates the model description for use by __str__ and related         functions, Base class that all volatility updaters must inherit from.      Notes     -----, VolatilityUpdater

### Community 42 - "Community 42"
Cohesion: 0.19
Nodes (1): MIDASHyperbolic

### Community 43 - "Community 43"
Cohesion: 0.35
Nodes (9): block(), demean(), inner_prod(), load_partial(), p_tests_vec(), save_partial(), temp_file_name(), worker() (+1 more)

### Community 45 - "Community 45"
Cohesion: 0.17
Nodes (1): FixedVariance

### Community 46 - "Community 46"
Cohesion: 0.18
Nodes (3): HTML representation for IPython Notebook, Generates lag names.  Overridden by other models, APARCH

### Community 47 - "Community 47"
Cohesion: 0.22
Nodes (4): r"""     Model with zero conditional mean estimation and simulation      Paramet, Simulated data from a zero mean model          Parameters         ----------, ZeroMean, ARCH

### Community 48 - "Community 48"
Cohesion: 0.20
Nodes (3): DFGLS, Sets or gets the maximum lags used when automatically selecting lag         leng, Elliott, Rothenberg and Stock's ([ers]_) GLS detrended Dickey-Fuller      Parame

### Community 49 - "Community 49"
Cohesion: 0.20
Nodes (4): The name of the model., Returns the dependent variable, Set or gets the volatility process          Volatility processes must be a subcl, VolatilityProcess

### Community 50 - "Community 50"
Cohesion: 0.20
Nodes (1): EWMAVariance

### Community 51 - "Community 51"
Cohesion: 0.25
Nodes (5): KPSS, kpss_crit(), Kwiatkowski, Phillips, Schmidt and Shin (KPSS) stationarity test      Parameters, Computes the number of lags for covariance matrix estimation in KPSS         tes, Linear interpolation for KPSS p-values and critical values      Parameters     -

### Community 52 - "Community 52"
Cohesion: 0.28
Nodes (5): Zivot-Andrews structural-break unit-root test      The Zivot-Andrews test can be, Minimal implementation of LS estimator for internal use, This is the core routine that computes the test statistic, computes         the, Linear interpolation for Zivot-Andrews p-values and critical values          Not, ZivotAndrews

### Community 53 - "Community 53"
Cohesion: 0.25
Nodes (3): _get_random_integers(), Update indices for the next iteration of the bootstrap.  This must         be ov, Update indices for the next iteration of the bootstrap.  This must         be ov

### Community 54 - "Community 54"
Cohesion: 0.25
Nodes (4): BootstrapRng, Simulation-based volatility forecasts using model residuals          Parameters, Simple fake RNG used to transform bootstrap-based forecasting into a standard, Forecast volatility from the model          Parameters         ----------

### Community 55 - "Community 55"
Cohesion: 0.29
Nodes (3): Andrews, QuadraticSpectral, Alternative name of the QuadraticSpectral covariance estimator.      See Also

### Community 57 - "Community 57"
Cohesion: 0.33
Nodes (2): agg_backend(), Fixture that switches the backend to agg for the duration of the test      Retur

### Community 58 - "Community 58"
Cohesion: 0.33
Nodes (5): clear_cache(), Simulation of ADF z-test critical values.  Closely follows MacKinnon (2010). Run, Cache-clearing function from mailing list, Wraps and blocks the main simulation so that the maximum amount of memory     ca, wrapper()

### Community 59 - "Community 59"
Cohesion: 0.40
Nodes (5): dfgsl_simulation(), Critical value simulation for the Dickey-Fuller GLS model.  Similar in design to, Wraps and blocks the main simulation so that the maximum amount of memory     ca, Simulates the empirical distribution of the DFGLS test statistic, wrapper()

### Community 60 - "Community 60"
Cohesion: 0.40
Nodes (5): Calculates quantiles of the KPSS test statistic for both the constant and consta, Simulated the KPSS test statistic for nobs observations,     performing b replic, A wrapper around the main simulation that runs it in blocks so that large     si, simulate_kpss(), wrapper()

### Community 61 - "Community 61"
Cohesion: 0.40
Nodes (1): TukeyHamming

### Community 62 - "Community 62"
Cohesion: 0.40
Nodes (1): TukeyHanning

### Community 63 - "Community 63"
Cohesion: 0.40
Nodes (1): TukeyParzen

### Community 64 - "Community 64"
Cohesion: 0.50
Nodes (2): Base class for returning summary as repr and str, _SummaryRepr

### Community 65 - "Community 65"
Cohesion: 0.50
Nodes (1): EGARCHUpdater

### Community 66 - "Community 66"
Cohesion: 0.50
Nodes (1): MIDASUpdater

### Community 67 - "Community 67"
Cohesion: 0.40
Nodes (4): pval_format(), Preferred formatting for x in [0,1], Preferred basic formatter, str_format()

### Community 68 - "Community 68"
Cohesion: 0.50
Nodes (1): FIGARCHUpdater

### Community 69 - "Community 69"
Cohesion: 0.50
Nodes (1): GARCHUpdater

### Community 70 - "Community 70"
Cohesion: 0.50
Nodes (1): HARCHUpdater

### Community 71 - "Community 71"
Cohesion: 0.50
Nodes (1): RiskMetrics2006Updater

### Community 72 - "Community 72"
Cohesion: 0.67
Nodes (2): load(), Load the graduate school admissions data used in the examples      Returns     -

### Community 73 - "Community 73"
Cohesion: 0.67
Nodes (2): Generate indices for sampling from the stationary bootstrap.      Parameters, stationary_bootstrap_sample_python()

### Community 75 - "Community 75"
Cohesion: 0.67
Nodes (2): load(), Load the Core CPI data used in the examples      Returns     -------     data :

### Community 76 - "Community 76"
Cohesion: 0.67
Nodes (2): load(), Load the Core CPI data used in the examples      Returns     -------     data :

### Community 77 - "Community 77"
Cohesion: 0.67
Nodes (2): load_file(), Load data from a csv.gz file.      Parameters     ----------     file_base : str

### Community 78 - "Community 78"
Cohesion: 0.67
Nodes (2): load(), Load the AAA and BAA rates used in the examples      Returns     -------     dat

### Community 79 - "Community 79"
Cohesion: 0.67
Nodes (2): load(), Load the Fama-French factor data used in the examples      Returns     -------

### Community 80 - "Community 80"
Cohesion: 0.67
Nodes (2): load(), Load the NASDAQ Composite data used in the examples      Returns     -------

### Community 81 - "Community 81"
Cohesion: 0.67
Nodes (2): adf_simulation(), Simulates the empirical distribution of the ADF z-test statistic

### Community 82 - "Community 82"
Cohesion: 0.67
Nodes (1): Simulation for critical value production for Engle-Granger

### Community 83 - "Community 83"
Cohesion: 0.67
Nodes (2): load(), Load the S&P 500 data used in the examples      Returns     -------     data : D

### Community 84 - "Community 84"
Cohesion: 0.67
Nodes (2): cov_nw(), Computes Newey-West covariance for 1-d and 2-d arrays      Parameters     ------

### Community 85 - "Community 85"
Cohesion: 0.67
Nodes (2): Test runner that allows testing of installed package.      Exists with test stat, test()

### Community 86 - "Community 86"
Cohesion: 0.67
Nodes (2): load(), Load the VIX Index data used in the examples      Returns     -------     data :

### Community 87 - "Community 87"
Cohesion: 0.67
Nodes (2): load(), Load the West Texas Intermediate crude oil price data used in the examples

### Community 88 - "Community 88"
Cohesion: 1.00
Nodes (1): Contains values used to approximate the critical value and p-value from DFGLS st

### Community 89 - "Community 89"
Cohesion: 1.00
Nodes (1): Contains values used to approximate the critical value and p-value from statist

### Community 90 - "Community 90"
Cohesion: 1.00
Nodes (1): Critical values produced by phillips-ouliaris-simulation.py  Z-type statistics

### Community 91 - "Community 91"
Cohesion: 1.00
Nodes (1): Critical values for the three different models specified for the Zivot-Andrews u

### Community 92 - "Community 92"
Cohesion: 1.00
Nodes (1): r"""Computes the log-likelihood of assuming residuals are normally         distr

### Community 93 - "Community 93"
Cohesion: 1.00
Nodes (1): r"""Computes the log-likelihood of assuming residuals are have a         standar

### Community 94 - "Community 94"
Cohesion: 1.00
Nodes (1): Construct starting values for use in optimization.          Parameters         -

### Community 95 - "Community 95"
Cohesion: 1.00
Nodes (1): Construct starting values for use in optimization.          Parameters         -

### Community 96 - "Community 96"
Cohesion: 1.00
Nodes (1): Initialize the recursion prior to calling update          Parameters         ---

### Community 97 - "Community 97"
Cohesion: 1.00
Nodes (1): Update the current variance at location t          Parameters         ----------

### Community 98 - "Community 98"
Cohesion: 1.00
Nodes (1): Testing shim for update with compatibility with the Cythonized version

### Community 99 - "Community 99"
Cohesion: 1.00
Nodes (1): The value of delta in the model. NaN is delta is estimated.

### Community 100 - "Community 100"
Cohesion: 1.00
Nodes (1): Truncation lag for the ARCH-infinity approximation

### Community 101 - "Community 101"
Cohesion: 1.00
Nodes (1): The name of the volatility process

### Community 102 - "Community 102"
Cohesion: 1.00
Nodes (1): Index to use to start variance subarray selection

### Community 103 - "Community 103"
Cohesion: 1.00
Nodes (1): Index to use to stop variance subarray selection

### Community 104 - "Community 104"
Cohesion: 1.00
Nodes (1): The number of parameters in the model

### Community 105 - "Community 105"
Cohesion: 1.00
Nodes (1): Flag indicating that the volatility process supports update

### Community 106 - "Community 106"
Cohesion: 1.00
Nodes (1): Get the volatility updater associated with the volatility process          Retur

### Community 107 - "Community 107"
Cohesion: 1.00
Nodes (1): Compute the variance for a single observation          Parameters         ------

### Community 108 - "Community 108"
Cohesion: 1.00
Nodes (1): Verify the requested forecasting method as valid for the specification

### Community 109 - "Community 109"
Cohesion: 1.00
Nodes (1): Analytic multi-step volatility forecasts from the model          Parameters

### Community 110 - "Community 110"
Cohesion: 1.00
Nodes (1): Simulation-based volatility forecasts from the model          Parameters

### Community 111 - "Community 111"
Cohesion: 1.00
Nodes (1): Returns starting values for the ARCH model          Parameters         ---------

### Community 112 - "Community 112"
Cohesion: 1.00
Nodes (1): Construct values for backcasting to start the recursion          Parameters

### Community 113 - "Community 113"
Cohesion: 1.00
Nodes (1): Transformation to apply to user-provided backcast values          Parameters

### Community 114 - "Community 114"
Cohesion: 1.00
Nodes (1): Returns bounds for parameters          Parameters         ----------         res

### Community 115 - "Community 115"
Cohesion: 1.00
Nodes (1): Compute the variance for the ARCH model          Parameters         ----------

### Community 116 - "Community 116"
Cohesion: 1.00
Nodes (1): Construct parameter constraints arrays for parameter estimation          Returns

### Community 117 - "Community 117"
Cohesion: 1.00
Nodes (1): Simulate data from the model          Parameters         ----------         para

### Community 118 - "Community 118"
Cohesion: 1.00
Nodes (1): Names of model parameters          Returns         -------         names : list

## Knowledge Gaps
- **69 isolated node(s):** `Generate indices for sampling from the stationary bootstrap.      Parameters`, `Load a dataset using the new syntax is possible`, `Fixture that switches the backend to agg for the duration of the test      Retur`, `Load the graduate school admissions data used in the examples      Returns     -`, `Load the Core CPI data used in the examples      Returns     -------     data :` (+64 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 26`** (2 nodes): `ewma_recursion()`, `RiskMetrics2006`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (1 nodes): `VarianceForecast`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (2 nodes): `_common_names()`, `GARCH`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (2 nodes): `Gets the value of the exogenous regressors in the model`, `FIGARCH`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (1 nodes): `MIDASHyperbolic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (1 nodes): `FixedVariance`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (1 nodes): `EWMAVariance`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (2 nodes): `agg_backend()`, `Fixture that switches the backend to agg for the duration of the test      Retur`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (1 nodes): `TukeyHamming`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 62`** (1 nodes): `TukeyHanning`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (1 nodes): `TukeyParzen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 64`** (2 nodes): `Base class for returning summary as repr and str`, `_SummaryRepr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 65`** (1 nodes): `EGARCHUpdater`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 66`** (1 nodes): `MIDASUpdater`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 68`** (1 nodes): `FIGARCHUpdater`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 69`** (1 nodes): `GARCHUpdater`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 70`** (1 nodes): `HARCHUpdater`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 71`** (1 nodes): `RiskMetrics2006Updater`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 72`** (2 nodes): `load()`, `Load the graduate school admissions data used in the examples      Returns     -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 73`** (2 nodes): `Generate indices for sampling from the stationary bootstrap.      Parameters`, `stationary_bootstrap_sample_python()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 75`** (2 nodes): `load()`, `Load the Core CPI data used in the examples      Returns     -------     data :`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 76`** (2 nodes): `load()`, `Load the Core CPI data used in the examples      Returns     -------     data :`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 77`** (2 nodes): `load_file()`, `Load data from a csv.gz file.      Parameters     ----------     file_base : str`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 78`** (2 nodes): `load()`, `Load the AAA and BAA rates used in the examples      Returns     -------     dat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 79`** (2 nodes): `load()`, `Load the Fama-French factor data used in the examples      Returns     -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 80`** (2 nodes): `load()`, `Load the NASDAQ Composite data used in the examples      Returns     -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 81`** (2 nodes): `adf_simulation()`, `Simulates the empirical distribution of the ADF z-test statistic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 82`** (1 nodes): `Simulation for critical value production for Engle-Granger`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 83`** (2 nodes): `load()`, `Load the S&P 500 data used in the examples      Returns     -------     data : D`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 84`** (2 nodes): `cov_nw()`, `Computes Newey-West covariance for 1-d and 2-d arrays      Parameters     ------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 85`** (2 nodes): `Test runner that allows testing of installed package.      Exists with test stat`, `test()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 86`** (2 nodes): `load()`, `Load the VIX Index data used in the examples      Returns     -------     data :`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 87`** (2 nodes): `load()`, `Load the West Texas Intermediate crude oil price data used in the examples`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 88`** (1 nodes): `Contains values used to approximate the critical value and p-value from DFGLS st`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 89`** (1 nodes): `Contains values used to approximate the critical value and p-value from statist`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 90`** (1 nodes): `Critical values produced by phillips-ouliaris-simulation.py  Z-type statistics`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 91`** (1 nodes): `Critical values for the three different models specified for the Zivot-Andrews u`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 92`** (1 nodes): `r"""Computes the log-likelihood of assuming residuals are normally         distr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 93`** (1 nodes): `r"""Computes the log-likelihood of assuming residuals are have a         standar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 94`** (1 nodes): `Construct starting values for use in optimization.          Parameters         -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 95`** (1 nodes): `Construct starting values for use in optimization.          Parameters         -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 96`** (1 nodes): `Initialize the recursion prior to calling update          Parameters         ---`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 97`** (1 nodes): `Update the current variance at location t          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 98`** (1 nodes): `Testing shim for update with compatibility with the Cythonized version`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 99`** (1 nodes): `The value of delta in the model. NaN is delta is estimated.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 100`** (1 nodes): `Truncation lag for the ARCH-infinity approximation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 101`** (1 nodes): `The name of the volatility process`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 102`** (1 nodes): `Index to use to start variance subarray selection`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 103`** (1 nodes): `Index to use to stop variance subarray selection`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 104`** (1 nodes): `The number of parameters in the model`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 105`** (1 nodes): `Flag indicating that the volatility process supports update`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 106`** (1 nodes): `Get the volatility updater associated with the volatility process          Retur`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 107`** (1 nodes): `Compute the variance for a single observation          Parameters         ------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 108`** (1 nodes): `Verify the requested forecasting method as valid for the specification`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 109`** (1 nodes): `Analytic multi-step volatility forecasts from the model          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 110`** (1 nodes): `Simulation-based volatility forecasts from the model          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 111`** (1 nodes): `Returns starting values for the ARCH model          Parameters         ---------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 112`** (1 nodes): `Construct values for backcasting to start the recursion          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 113`** (1 nodes): `Transformation to apply to user-provided backcast values          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 114`** (1 nodes): `Returns bounds for parameters          Parameters         ----------         res`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 115`** (1 nodes): `Compute the variance for the ARCH model          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 116`** (1 nodes): `Construct parameter constraints arrays for parameter estimation          Returns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 117`** (1 nodes): `Simulate data from the model          Parameters         ----------         para`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 118`** (1 nodes): `Names of model parameters          Returns         -------         names : list`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AbstractDocStringInheritor` connect `Community 6` to `Community 55`, `Community 3`, `Community 32`, `Community 16`, `Community 61`, `Community 62`, `Community 63`, `Community 5`, `Community 48`, `Community 51`, `Community 17`, `Community 12`, `Community 52`, `Community 33`, `Community 11`, `Community 10`, `Community 40`, `Community 18`, `Community 23`, `Community 13`, `Community 92`, `Community 29`, `Community 93`, `Community 94`, `Community 21`, `Community 95`, `Community 41`, `Community 19`, `Community 39`, `Community 47`, `Community 38`, `Community 46`, `Community 34`, `Community 37`, `Community 65`, `Community 15`, `Community 68`, `Community 69`, `Community 70`, `Community 66`, `Community 96`, `Community 97`, `Community 98`, `Community 71`, `Community 54`, `Community 9`, `Community 50`, `Community 45`, `Community 31`, `Community 42`, `Community 14`, `Community 101`, `Community 102`, `Community 103`, `Community 104`, `Community 105`, `Community 106`, `Community 107`, `Community 100`, `Community 108`, `Community 99`, `Community 109`, `Community 110`, `Community 111`, `Community 112`, `Community 113`, `Community 114`, `Community 115`, `Community 116`, `Community 117`, `Community 118`, `Community 26`, `Community 30`, `Community 49`, `Community 0`?**
  _High betweenness centrality (0.531) - this node is a cross-community bridge._
- **Why does `DocStringInheritor` connect `Community 0` to `Community 1`, `Community 35`, `Community 53`, `Community 24`, `Community 23`, `Community 6`?**
  _High betweenness centrality (0.154) - this node is a cross-community bridge._
- **Why does `Normal` connect `Community 18` to `Community 2`, `Community 7`, `Community 9`, `Community 10`, `Community 25`, `Community 64`, `Community 49`, `Community 23`, `Community 13`, `Community 92`, `Community 6`, `Community 21`, `Community 41`, `Community 29`, `Community 19`, `Community 40`, `Community 39`, `Community 47`, `Community 38`, `Community 46`, `Community 34`, `Community 37`, `Community 54`, `Community 50`, `Community 45`, `Community 31`, `Community 42`, `Community 14`, `Community 101`, `Community 102`, `Community 103`, `Community 104`, `Community 105`, `Community 106`, `Community 107`, `Community 100`, `Community 108`, `Community 99`, `Community 109`, `Community 110`, `Community 111`, `Community 112`, `Community 113`, `Community 114`, `Community 115`, `Community 116`, `Community 117`, `Community 118`, `Community 26`, `Community 30`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Are the 246 inferred relationships involving `AbstractDocStringInheritor` (e.g. with `Andrews` and `Bartlett`) actually correct?**
  _`AbstractDocStringInheritor` has 246 INFERRED edges - model-reasoned connections that need verification._
- **Are the 171 inferred relationships involving `Normal` (e.g. with `ARCHModel` and `ARCHModelFixedResult`) actually correct?**
  _`Normal` has 171 INFERRED edges - model-reasoned connections that need verification._
- **Are the 111 inferred relationships involving `VolatilityProcess` (e.g. with `ARCHModel` and `ARCHModelFixedResult`) actually correct?**
  _`VolatilityProcess` has 111 INFERRED edges - model-reasoned connections that need verification._
- **Are the 108 inferred relationships involving `Distribution` (e.g. with `ARCHModel` and `ARCHModelFixedResult`) actually correct?**
  _`Distribution` has 108 INFERRED edges - model-reasoned connections that need verification._