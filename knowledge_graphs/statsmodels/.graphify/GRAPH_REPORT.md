# Graph Report - knowledge_graphs/statsmodels/repo/statsmodels  (2026-08-12)

## Corpus Check
- Large corpus: 458 files · ~871,206 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 11645 nodes · 33581 edges · 540 communities detected
- Extraction: 43% EXTRACTED · 57% INFERRED · 0% AMBIGUOUS · INFERRED: 19222 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: uses: 19222 · rationale_for: 4855 · method: 4071 · calls: 2673 · contains: 2192 · inherits: 515 · imports_from: 53


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 458 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `179d1f4`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Appender` - 1093 edges
2. `FormulaManager` - 929 edges
3. `OLS` - 857 edges
4. `ValueWarning` - 838 edges
5. `SpecificationWarning` - 690 edges
6. `SimpleTable` - 681 edges
7. `ConvergenceWarning` - 658 edges
8. `Docstring` - 450 edges
9. `Substitution` - 426 edges
10. `GLM` - 375 edges

## Surprising Connections (you probably didn't know these)
- `Holds common functions for l1 solvers.` --uses--> `ConvergenceWarning`  [INFERRED]
  base/l1_solvers_common.py → tools/sm_exceptions.py
- `Theory dictates that one of two conditions holds:         i) abs(score[i]) == al` --uses--> `ConvergenceWarning`  [INFERRED]
  base/l1_solvers_common.py → tools/sm_exceptions.py
- `Trims (set to zero) params that are zero at the theoretical minimum.     Uses he` --uses--> `ConvergenceWarning`  [INFERRED]
  base/l1_solvers_common.py → tools/sm_exceptions.py
- `Prediction results for GLM      This results class is used for backwards compati` --uses--> `FormulaManager`  [INFERRED]
  base/_prediction_inference.py → formula/_manager.py
- `Confidence interval for the predicted value          This is currently only avai` --uses--> `FormulaManager`  [INFERRED]
  base/_prediction_inference.py → formula/_manager.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.02
Nodes (153): ARDL, ardl_select_order(), ARDLOrderSelectionResults, ARDLResults, ARDLResultsWrapper, BoundsTestResult, _format_order(), _pss_pvalue() (+145 more)

### Community 1 - "Community 1"
Cohesion: 0.02
Nodes (81): MLEModel, MLEResults, MLEResultsWrapper, DynamicFactorResults, DynamicFactorResultsWrapper, Dynamic factor model  Author: Chad Fulton License: Simplified-BSD, Estimates of unobserved factors          Returns         -------         out : B, Coefficients of determination (:math:`R^2`) from regressions of         individu (+73 more)

### Community 2 - "Community 2"
Cohesion: 0.02
Nodes (139): LikelihoodModelResults, Model, Non-linear least squares  Author: Josef Perktold based on scipy.optimize.curve_f, # NOTE: This needs to call super for data checking, Just a dummy placeholder for now      Most results from RegressionResults can be, # TODO: check effect of `weights` on result statistics, Results, MultivariateLS (+131 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (203): LinearConstraints, LikelihoodModel, CountDiagnostic, PoissonDiagnostic, Diagnostic and specification tests and plots for Poisson models      Status: exp, Diagnostic and specification tests and plots for count models      Status: exper, DiscreteMargins, Get marginal effects of a Discrete Choice model      Parameters     ---------- (+195 more)

### Community 4 - "Community 4"
Cohesion: 0.02
Nodes (152): ETSResultsWrapper, PredictionResults, PredictionResultsWrapper, r""" ETS models for time series analysis  The ETS models are a family of time se, Calculates mean prediction and prediction intervals          Parameters, ETS mean prediction and prediction intervals      Parameters     ----------, The variance of the predicted mean, Calculates prediction intervals for the forecasted values          Parameters (+144 more)

### Community 5 - "Community 5"
Cohesion: 0.03
Nodes (143): PredictionResultsMean, Prediction results for GLM      This results class is used for backwards compati, Confidence interval for the predicted value          This is currently only avai, Summary frame          Parameters         ----------         alpha : float, opti, Link, Second derivative of the inverse link function g^(-1)(z).          Parameters, A generic link function for one-parameter exponential family.      `Link` does n, Return the value of the link function.  This is just a placeholder.          Par (+135 more)

### Community 6 - "Community 6"
Cohesion: 0.03
Nodes (98): dict, _norm(), PCA, Principal Component Analysis  Author: josef-pktd Modified by Kevin Sheppard, Compute the Euclidean (L2) norm of an array      Parameters     ----------     x, Implements alternatives for handling missing values, Principal Component Analysis      Parameters     ----------     data : array_lik, Computes GLS weights based on percentage of data fit (+90 more)

### Community 7 - "Community 7"
Cohesion: 0.05
Nodes (130): PandasData, Data handling class which knows how to reattach pandas metadata to model     res, # TODO: check if this is reasonable for statespace, # TODO: changed this to nobs_effective, has to be changed when merging, # TODO: changed this to nobs_effective, has to be changed when merging, # TODO: seems like maybe self.fixed_params should be the dictionary, # TODO: this was changed from the original, requires some work when, # TODO: Case with "not approx_complex_step" is not hit in (+122 more)

### Community 8 - "Community 8"
Cohesion: 0.02
Nodes (103): ARIMA, ARIMAResults, ARIMAResultsWrapper, ARIMA model class  Author: Chad Fulton License: BSD-3, # TODO: if trend='c', then we could alternatively use `demean=True` in, Fit (estimate) the parameters of the model          Parameters         ---------, r"""     Autoregressive Integrated Moving Average (ARIMA) model, and extensions, # TODO: may want to consider using innovations (MLE) if possible here, (+95 more)

### Community 9 - "Community 9"
Cohesion: 0.04
Nodes (102): LikelihoodResultsWrapper, _LLRMixin, Log-likelihood of model at params, Negative log-likelihood of model at params, Log-likelihood of the model for all observations at params          Parameters, Gradient of log-likelihood evaluated at params, Jacobian/Gradient of log-likelihood evaluated at params for each         observa, Hessian of log-likelihood evaluated at params (+94 more)

### Community 10 - "Community 10"
Cohesion: 0.08
Nodes (131): Results for models estimated using regularization      Parameters     ----------, RegularizedResults, RegularizedResultsWrapper, burg(), CompareLRTestResult, ELTestResult, _get_sigma(), GLSAR (+123 more)

### Community 11 - "Community 11"
Cohesion: 0.03
Nodes (79): GenericLikelihoodModel, GenericLikelihoodModelResults, DiscretizedModel, experimental model to fit discretized distribution      Count models based on di, frozen distribution instance of the discrete distribution., GenericLikelihoodModel, GenericLikelihoodModelResults, _LLRMixin (+71 more)

### Community 12 - "Community 12"
Cohesion: 0.02
Nodes (107): Linear Model with Student-t distributed errors  Because the t distribution has f, Loglikelihood of the model evaluated at params          Parameters         -----, Negative loglikelihood of linear model with t distributed errors          Parame, Return predicted mean values          Parameters         ----------         para, Maximum Likelihood Estimation of Linear Model with t-distributed errors      Thi, Initialize the model, setting up parameter names and start values, # TODO: here or in __init__, Set starting values for the parameters          Parameters         ---------- (+99 more)

### Community 13 - "Community 13"
Cohesion: 0.03
Nodes (58): LagOrderResults, VAR, coint_johansen(), CointRankResults, _deterministic_to_exog(), _endog_matrices(), JohansenTestResult, _linear_trend() (+50 more)

### Community 14 - "Community 14"
Cohesion: 0.03
Nodes (105): fit_constrained(), fit_constrained_wrap(), Created on Thu May 15 16:36:05 2014  Author: Josef Perktold License: BSD-3, Class to hold linear constraints information      Affine constraints are defined, # TODO: make this work, there is something wrong, does not round-trip, Transform from the reduced to the full parameter space          Parameters, Transform from the full to the reduced parameter space          This transform c, Find the parameters that satisfy linear constraint from unconstrained      The l (+97 more)

### Community 15 - "Community 15"
Cohesion: 0.03
Nodes (76): Penalty, A class for representing a scalar-value penalty.      Parameters     ----------, A penalty function on a vector of parameters.          Parameters         ------, The gradient of a penalty function.          Parameters         ----------, Penalty classes for Generalized Additive Models  Author: Luca Puggini Author: Jo, Penalty matrix for the smooth term of a GAM          Parameters         --------, Penalty for smooth term in Generalized Additive Models      Parameters     -----, # TODO: Review this, (+68 more)

### Community 16 - "Community 16"
Cohesion: 0.11
Nodes (104): TimeSeriesModel, TimeSeriesResultsWrapper, OutputWarning, Function output contains atypical values, CausalityTestResults, ErrorBand, ForecastInterval, NormalityTestResults (+96 more)

### Community 17 - "Community 17"
Cohesion: 0.07
Nodes (108): NamedTuple, RuntimeError, ResultsStore, acf(), AcfResult, acovf(), adfuller(), ADFullerResult (+100 more)

### Community 18 - "Community 18"
Cohesion: 0.03
Nodes (32): VARProcess, VARResults, Vector Autoregression (VAR) processes  References ---------- Lütkepohl (2005) Ne, # TODO: change this when masked support is better or with formula, Fit the SVAR model and solve for structural parameters          Parameters, Returns either the given starting values or .1 if none are given, Estimate the reduced-form VAR and then solve for structural params          Para, # TODO: should give users the option to use a dof correction or not (+24 more)

### Community 19 - "Community 19"
Cohesion: 0.02
Nodes (70): _BaseInfluenceMixin, outlier_test(), Influence and Outlier Measures  Created on Sun Jan 29 11:16:09 2012  Author: Jos, dffits measure for influence of an observation          Returns         -------, # TODO: do I want to use different sigma estimate in, dfbetas          uses results from leave-one-observation-out loop, dfbeta          uses results from leave-one-observation-out loop, error variance for all LOOO regressions          This is 'mse_resid' from each a (+62 more)

### Community 20 - "Community 20"
Cohesion: 0.03
Nodes (51): The predicted values from the model at the estimated parameters, Results, make_wrapper(), populate_wrapper(), Save a pickle of this instance.          Parameters         ----------         f, Class which wraps a statsmodels estimation Results class and steps in to     rea, Load a pickled results instance          .. warning::             Loading pickle, ResultsWrapper (+43 more)

### Community 21 - "Community 21"
Cohesion: 0.03
Nodes (40): Autoregressive, CategoricalCovStruct, CovStruct, Equivalence, Exchangeable, GlobalOddsRatio, Independence, Nested (+32 more)

### Community 22 - "Community 22"
Cohesion: 0.08
Nodes (54): PenalizedMixin, Logit, KFold, K-Folds cross validation iterator      Provides train/test indexes to split data, MultivariateGAMCVPath, MultivariateGamPenalty, Penalty for Generalized Additive Models      Parameters     ----------     multi, GLMGamResultsWrapper (+46 more)

### Community 23 - "Community 23"
Cohesion: 0.04
Nodes (59): approx_copula_pdf(), average_grid(), cdf2prob_grid(), _ecdf_mv(), _eval_bernstein_1d(), _eval_bernstein_2d(), _eval_bernstein_dd(), frequencies_fromdata() (+51 more)

### Community 24 - "Community 24"
Cohesion: 0.03
Nodes (27): ETSModel, ETSResults, Log-likelihood function to be called from fit to avoid reallocation of         m, r"""         Log-likelihood of model          Parameters         ----------, Calculates residuals of a prediction, Exponential smoothing with given parameters          Parameters         --------, Exponential smoothing with given parameters          Parameters         --------, r"""         Hessian matrix of the likelihood function, evaluated at the given (+19 more)

### Community 25 - "Community 25"
Cohesion: 0.04
Nodes (42): cy_hamilton_filter_log(), cy_kim_smoother_log(), HamiltonFilterResults, KimSmootherResults, _logistic(), MarkovSwitching, MarkovSwitchingParams, MarkovSwitchingResultsWrapper (+34 more)

### Community 26 - "Community 26"
Cohesion: 0.06
Nodes (42): ContrastResults, GMM, WLS, _AIPWGMM, _AIPWWLSGMM, ate_ipw(), _IPWGMM, _IPWRAGMM (+34 more)

### Community 27 - "Community 27"
Cohesion: 0.04
Nodes (15): BinaryModel, BinaryResults, BinaryResultsWrapper, L1BinaryResults, L1MultinomialResults, L1NegativeBinomialResults, LogitResults, MNLogit (+7 more)

### Community 28 - "Community 28"
Cohesion: 0.06
Nodes (19): gbic(), im_ratio(), _lm_robust(), Created on Wed May 30 15:11:09 2018  @author: josef, # TODO: check if usecase for pinv exists, score test for restrictions or for omitted variables      Null Hypothesis : cons, Result of :func:`_lm_robust` and :func:`score_test`.      Parameters     -------, # TODO: we are computing unnecessary things for cov_type nonrobust (+11 more)

### Community 29 - "Community 29"
Cohesion: 0.06
Nodes (59): AllPairsResults, binom_test_reject_interval(), _bisection_search_conservative(), _bound_proportion_confint(), confint_proportions_2indep(), _confint_riskratio_koopman(), _confint_riskratio_paired_nam(), KoopmanConfintResult (+51 more)

### Community 30 - "Community 30"
Cohesion: 0.07
Nodes (47): GEE, GLM, abline_plot(), add_ellipse(), add_lowess(), added_variable_resids(), ceres_resids(), _high_leverage() (+39 more)

### Community 31 - "Community 31"
Cohesion: 0.04
Nodes (35): Cell, csv2st(), get_output_format(), pad(), Provides a simple table class  A SimpleTable is essentially a list of lists plus, Escape special LaTeX characters in `data`, if needed          Parameters, Return the formatted cell          This is the default formatter for cells. Over, Return the cell's datatype          Returns         -------         object (+27 more)

### Community 32 - "Community 32"
Cohesion: 0.06
Nodes (21): extend_index(), r""" Implementation of the Theta forecasting method of  Assimakopoulos, V., & Ni, r"""         Estimate model parameters          Parameters         ----------, Whether to deseasonalize the data, The period of the seasonality, Whether to test the data for seasonality, Whether the data is differenced in the seasonality test, The method used to deseasonalize the data (+13 more)

### Community 33 - "Community 33"
Cohesion: 0.06
Nodes (25): KalmanFilter, CFASimulationSmoother, "Cholesky Factor Algorithm" (CFA) simulation smoothing for state space models  A, r"""         Posterior mean of the states conditional on the data          .. ma, r"""         Sparse Cholesky factor of inverse posterior covariance matrix, r"""     "Cholesky Factor Algorithm" (CFA) simulation smoother      Parameters, r"""         Posterior covariance of the states conditional on the data, r"""         Perform simulation smoothing (via Cholesky factor algorithm) (+17 more)

### Community 34 - "Community 34"
Cohesion: 0.06
Nodes (23): MICE, MICEData, PatsyFormula, Multiple Imputation through Chained Equations (MICE)  This module implements the, Gaussian perturbation of model parameters          The normal approximation to t, Impute missing values for a single variable          This is a two-step process, Use predictive mean matching to impute missing values          Notes         ---, Perform one complete MICE iteration          A single MICE iteration updates all (+15 more)

### Community 35 - "Community 35"
Cohesion: 0.06
Nodes (50): cov_cluster(), cov_cluster_2groups(), cov_crosssection_0(), cov_hac_simple(), cov_hc0(), cov_hc1(), cov_hc2(), cov_hc3() (+42 more)

### Community 36 - "Community 36"
Cohesion: 0.09
Nodes (27): CountResults, CountResults, L1CountResults, HurdleCountResults, HurdleCountResultsWrapper, L1HurdleCountResults, L1HurdleCountResultsWrapper, L1TruncatedLFGenericResults (+19 more)

### Community 37 - "Community 37"
Cohesion: 0.07
Nodes (14): ConditionalLogit, ConditionalMNLogit, _ConditionalModel, ConditionalPoisson, ConditionalResults, ConditionalResultsWrapper, Conditional logistic, Poisson, and multinomial logit regression, Return a regularized fit to a linear regression model.          Parameters (+6 more)

### Community 38 - "Community 38"
Cohesion: 0.05
Nodes (36): _check_discrete_args(), _check_margeff_args(), _effects_at(), _get_const_index(), _get_count_effects(), _get_count_index(), _get_dummy_effects(), _get_dummy_index() (+28 more)

### Community 39 - "Community 39"
Cohesion: 0.06
Nodes (34): _col_info(), _col_params(), _df_to_simpletable(), _formatter(), _make_unique(), _measure_tables(), Append a note to the bottom of the summary table          Parameters         ---, Insert a title on top of the summary table          Parameters         --------- (+26 more)

### Community 40 - "Community 40"
Cohesion: 0.05
Nodes (37): clip_evals(), corr_clipped(), corr_nearest(), corr_nearest_factor(), corr_thresholded(), cov_nearest(), cov_nearest_factor_homog(), CovNearestResult (+29 more)

### Community 41 - "Community 41"
Cohesion: 0.08
Nodes (21): L1ZeroInflatedGeneralizedPoissonResults, L1ZeroInflatedGeneralizedPoissonResultsWrapper, L1ZeroInflatedNegativeBinomialResults, L1ZeroInflatedNegativeBinomialResultsWrapper, L1ZeroInflatedPoissonResults, L1ZeroInflatedPoissonResultsWrapper, Influence and outlier measures          See notes section for influence measures, Get marginal effects of the fitted model          Not yet implemented for Zero-I (+13 more)

### Community 42 - "Community 42"
Cohesion: 0.06
Nodes (18): MICEResults, Summarize the results of running MICE          Parameters         ----------, LikelihoodModelResults, Model, MANOVA, Multivariate analysis of variance  author: Yichuan Liu, # TODO: patsy migration, Multivariate Analysis of Variance      The implementation of MANOVA is based on (+10 more)

### Community 43 - "Community 43"
Cohesion: 0.06
Nodes (35): Tukey's biweight function for M-estimation      Parameters     ----------     c, Tuning parameter for given breakdown point or efficiency          This currently, Set and change the tuning parameter of the Norm          Parameters         ----, Tukey's biweight is defined piecewise over the range of z          Parameters, r"""         The robust criterion function for Tukey's biweight estimator, r"""         The psi function for Tukey's biweight estimator          The analyt, r"""         Tukey's biweight weighting function for the IRLS algorithm, The derivative of Tukey's biweight psi function          Parameters         ---- (+27 more)

### Community 44 - "Community 44"
Cohesion: 0.05
Nodes (22): _check_dynamic(), r"""         In-sample and out-of-sample prediction for state space models gener, Verify dynamic and warn or error if issues      Parameters     ----------     dy, Context manager for fixing the scale when FILTER_CONCENTRATED is set          Pa, Initialize the statespace model with component matrices          Parameters, Initialize the statespace model as stationary, Initialize the statespace model as diffuse, Update the snapshot to reflect the current state of the model          Parameter (+14 more)

### Community 45 - "Community 45"
Cohesion: 0.05
Nodes (32): ar2full(), ar2lhs(), padone(), Helper and filter functions for VAR and VARMA, and basic VAR class  Created on M, Creates inverse ar filter (MA representation) recursively      The VAR lag polyn, Generate a VAR process with errors u      similar to gauss     uses loop      Pa, Pad with zeros along one axis      Can be used sequentially to pad several axes., Trim a number of array elements along one axis      Parameters     ---------- (+24 more)

### Community 46 - "Community 46"
Cohesion: 0.06
Nodes (23): _check_args(), GaussianCovariance, ProcessCovariance, ProcessMLE, ProcessMLEResults, This module implements maximum likelihood-based estimation (MLE) of Gaussian reg, Fit a Gaussian mean/variance regression model      This class fits a one-dimensi, r"""     A covariance model for a process indexed by a real parameter      An im (+15 more)

### Community 47 - "Community 47"
Cohesion: 0.06
Nodes (36): cohensd2problarger(), _compute_rank_placements(), jonckheere_terpstra(), JonckheereTerpstraResult, prob_larger_continuous(), ProbSuperiorResult, rank_compare_2indep(), rank_compare_2ordinal() (+28 more)

### Community 48 - "Community 48"
Cohesion: 0.06
Nodes (16): AsymBiLogistic, AsymLogistic, AsymMixed, AsymNegLogistic, HR, PickandDependence, Pickand's dependence functions as generators for EV-copulas   Created on Wed Jan, asymmetric mixed model of Tawn 1988      special case:  k=0, theta in [0,1] : sy (+8 more)

### Community 49 - "Community 49"
Cohesion: 0.07
Nodes (10): GenericZeroInflated, Log-likelihood of Generic Zero-Inflated model.          Parameters         -----, Log-likelihood for observations of Generic Zero-Inflated model.          Paramet, Generic Zero-Inflated model score (gradient) vector of the log-likelihood., Predict expected response or other statistic given exogenous variables., Derivative of the expected endog with respect to the parameters.          Parame, Get a frozen instance of distribution based on predicted parameters          Par, ZeroInflatedGeneralizedPoisson (+2 more)

### Community 50 - "Community 50"
Cohesion: 0.06
Nodes (23): QIF, QIFAutoregressive, QIFCovariance, QIFExchangeable, QIFIndependence, QIFResults, QIFResultsWrapper, Fit a regression model using quadratic inference functions (QIF).      QIF is an (+15 more)

### Community 51 - "Community 51"
Cohesion: 0.06
Nodes (41): aic(), aic_sigma(), aicc(), aicc_sigma(), bias(), bic(), bic_sigma(), hqic() (+33 more)

### Community 52 - "Community 52"
Cohesion: 0.06
Nodes (37): add_lag(), add_trend(), _ar_invtransparams(), _ar_transparams(), commutation_matrix(), detrend(), duplication_matrix(), elimination_matrix() (+29 more)

### Community 53 - "Community 53"
Cohesion: 0.06
Nodes (11): RegressionModel, QuantReg, QuantRegResults, Quantile regression model  Model parameters are estimated using iterated reweigh, # TODO: better start, initial beta is used only for convergence check, Results instance for the QuantReg model, Quantile Regression      Estimate a quantile regression model using iterative re, Summarize the Regression Results          Parameters         ---------- (+3 more)

### Community 54 - "Community 54"
Cohesion: 0.07
Nodes (14): CountModel, DiscreteModel, HurdleCountModel, Log-likelihood for observations of Generic Truncated model.          Parameters, Log-likelihood of Generic Hurdle model.          Parameters         ----------, Generic Truncated model score (gradient) vector of the log-likelihood., Generic Truncated model score (gradient) vector of the log-likelihood., Generic Truncated model Hessian matrix of the log-likelihood.          Parameter (+6 more)

### Community 55 - "Community 55"
Cohesion: 0.06
Nodes (18): r"""     Class to hold results from fitting a state space model      Parameters, (float) Akaike Information Criterion, (float) Akaike Information Criterion with small sample correction, (float) Bayes Information Criterion, (float) Hannan-Quinn Information Criterion, (float) The value of the log-likelihood function evaluated at `params`, (float) Mean absolute error, (float) Mean squared error (+10 more)

### Community 56 - "Community 56"
Cohesion: 0.08
Nodes (20): FrozenRepresentation, FilterResults, Results from applying the Kalman filter to a state space model      Parameters, Update the results to match a given model          Parameters         ----------, Update the filter results          Parameters         ----------         kalman_, r"""         Standardized forecast errors          The forecast errors produced, r"""         Apply the Kalman filter to the statespace model          Parameters, r"""         Calculate the loglikelihood associated with the statespace model (+12 more)

### Community 57 - "Community 57"
Cohesion: 0.07
Nodes (27): holt__(), holt_add_dam(), holt_init(), holt_mul_dam(), holt_win__add(), holt_win_add_add_dam(), holt_win_add_mul_dam(), holt_win_init() (+19 more)

### Community 58 - "Community 58"
Cohesion: 0.08
Nodes (23): CovarianceReduction, _DimReductionRegression, DimReductionResults, DimReductionResultsWrapper, _grass_opt(), PrincipalHessianDirections, Dimension reduction regression models, A base class for dimension reduction regression methods (+15 more)

### Community 59 - "Community 59"
Cohesion: 0.06
Nodes (37): ar2arma(), arma2ar(), arma2ma(), arma_acf(), arma_acovf(), arma_generate_sample(), arma_impulse_response(), arma_pacf() (+29 more)

### Community 60 - "Community 60"
Cohesion: 0.09
Nodes (18): Created on Sun May 10 08:23:48 2015  Author: Josef Perktold License: BSD-3, Score based on finite difference derivative, Gradient of model at params, Gradient of model observations at params, Hessian based on finite difference derivative, Hessian of model at params, Mixin class for Maximum Penalized Likelihood      Parameters     ----------, Minimize negative penalized log-likelihood          Parameters         --------- (+10 more)

### Community 61 - "Community 61"
Cohesion: 0.11
Nodes (23): BaseCV, BasePenaltiesPathCV, MultivariateGAMCV, Cross-validation classes for GAM  Author: Luca Puggini, Split smoothers in test and train sets and create GenericSmoothers      Paramete, # TODO: Double check this part. cov_der2 is calculated with all data, # TODO: Double check this part. cov_der2 is calculated with all data, Cross validation error of a multivariate additive model      Parameters     ---- (+15 more)

### Community 62 - "Community 62"
Cohesion: 0.07
Nodes (30): BSplines, compute_all_knots(), _eval_bspline_basis(), get_covder2(), _get_integration_points(), get_knots_bsplines(), make_bsplines_basis(), make_poly_basis() (+22 more)

### Community 63 - "Community 63"
Cohesion: 0.09
Nodes (20): GenericKDE, GenericKDE, Base class for density estimation and regression KDE classes, Computes the bandwidth of the data          Parameters         ----------, Sets the default values for the efficient estimation          Parameters, Returns Scott's normal reference rule of thumb bandwidth parameter          Retu, Sets bandwidth lower bound to effectively zero (1e-10), and for         discrete, r"""         Returns the cross validation maximum likelihood bandwidth parameter (+12 more)

### Community 64 - "Community 64"
Cohesion: 0.08
Nodes (25): banddepth(), _curve_constrained(), fboxplot(), hdrboxplot(), HdrResults, _inverse_transform(), _min_max_band(), rainbowplot() (+17 more)

### Community 65 - "Community 65"
Cohesion: 0.06
Nodes (17): MarkovSwitchingResults, Compute the score per observation, evaluated at params          Parameters, Hessian matrix of the likelihood function, evaluated at the given         parame, r"""     Class to hold results from fitting a Markov switching model      Parame, (float) Akaike Information Criterion, (float) Bayes Information Criterion, (array) The variance / covariance matrix. Computed using the numerical         H, (array) The variance / covariance matrix. Computed using the outer         produ (+9 more)

### Community 66 - "Community 66"
Cohesion: 0.07
Nodes (18): Analyses that can be performed on a 2x2 contingency table      Parameters     --, Construct a Table object from data          Parameters         ----------, Returns the log odds ratio for a 2x2 table, Returns the odds ratio for a 2x2 table, Returns the standard error for the log odds ratio, P-value for a hypothesis test about the odds ratio          Parameters         -, P-value for a hypothesis test about the log odds ratio          Parameters, A confidence level for the log odds ratio          Parameters         ---------- (+10 more)

### Community 67 - "Community 67"
Cohesion: 0.08
Nodes (33): _construct_A_W(), durbin_watson(), expected_robust_kurtosis(), _finalize_h_kernel_sweep(), _h_kern(), jarque_bera(), _kr3(), medcouple() (+25 more)

### Community 68 - "Community 68"
Cohesion: 0.07
Nodes (26): combine_effects(), CombineResults, effectsize_2proportions(), effectsize_smd(), _fit_tau_iter_mm(), _fit_tau_iterative(), _fit_tau_mm(), HomogeneityTestResult (+18 more)

### Community 69 - "Community 69"
Cohesion: 0.07
Nodes (27): ftest_anova_power(), ftest_power(), ftest_power_f2(), FTestPower, ncf_sf(), nct_cdf(), nct_sf(), normal_power_het() (+19 more)

### Community 70 - "Community 70"
Cohesion: 0.06
Nodes (32): add_constant(), asstr2(), Bunch, clean0(), drop_missing(), _ensure_2d(), fullrank(), isestimable() (+24 more)

### Community 71 - "Community 71"
Cohesion: 0.08
Nodes (12): ABC, CalendarDeterministicTerm, CalendarFourier, CalendarSeasonality, FourierDeterministicTerm, Abstract Base Class for all Fourier Deterministic Terms, The order of the Fourier terms included, Abstract Base Class for calendar deterministic terms (+4 more)

### Community 72 - "Community 72"
Cohesion: 0.09
Nodes (18): AFTResults, emplikeAFT, OptAFT, Accelerated Failure Time (AFT) Model with empirical likelihood inference  AFT re, Uses EM algorithm to compute the maximum likelihood of a test          Parameter, Returns the difference between the log likelihood for a         parameter and so, Class for estimating and conducting inference in an AFT model      Parameters, Indicate if an observation takes the same value as the next         ordered obse (+10 more)

### Community 73 - "Community 73"
Cohesion: 0.10
Nodes (1): RollingRegressionResults

### Community 74 - "Community 74"
Cohesion: 0.10
Nodes (18): Representation, KalmanFilter, State Space Representation and Kalman Filter  Author: Chad Fulton License: Simpl, r"""         Simulate a new time series following the state space model, r"""         Impulse response function          Parameters         ----------, # TODO: We should only fill in the non-masked elements of, # TODO: there is a corner case here when the filter has not, (bool) Flag to prevent storing all forecast-related output (+10 more)

### Community 75 - "Community 75"
Cohesion: 0.09
Nodes (25): anova1_lm_single(), anova2_lm_single(), anova3_lm_single(), anova_lm(), anova_single(), AnovaResults, AnovaRM, _get_covariance() (+17 more)

### Community 76 - "Community 76"
Cohesion: 0.06
Nodes (18): Binomial, NegativeBinomial, Power, Variance functions for use with the link functions in statsmodels.family.links, Relates the variance of a random variable to its mean. Defaults to 1.      Metho, Derivative of the variance function v'(mu)          May be undefined at zero., Binomial variance function      Parameters     ----------     n : int, optional, Binomial variance function          Parameters         ----------         mu : a (+10 more)

### Community 77 - "Community 77"
Cohesion: 0.10
Nodes (31): _categories_level(), _create_default_properties(), _create_labels(), _get_position(), _hierarchical_split(), _key_splitting(), mosaic(), _normalize_data() (+23 more)

### Community 78 - "Community 78"
Cohesion: 0.10
Nodes (16): Panel data analysis for short T and large N  Created on Sat Dec 17 19:32:00 2011, Short Panel with general intertemporal within correlation      assumes data is s, Perform an iterative two-step procedure to estimate the GLS model.          Para, sum outerproduct dot(x_i, x_i.T) over individuals      loop version, sum outerproduct dot(x_i, x_i.T) over individuals      where x_i is (nobs_i, 1),, apply linear transform for each individual      loop version, Short Panel with general intertemporal within correlation      assumes data is s, ShortPanelGLS (+8 more)

### Community 79 - "Community 79"
Cohesion: 0.08
Nodes (17): describe(), Description, is_categorical_dtype(), _kurtosis(), pd_ptp(), Wrapper for scipy.stats.skew that returns nan instead of raising Error      Para, Signs test      Parameters     ----------     samp : array_like         1d array, Extended descriptive statistics for data      Parameters     ----------     data (+9 more)

### Community 80 - "Community 80"
Cohesion: 0.08
Nodes (15): EllipticalCopula, GaussianCopula, Created on Fri Jan 29 19:19:45 2021  Author: Josef Perktold Author: Pamphile Roy, Bivariate kendall's tau based on correlation coefficient.          Parameters, Pearson correlation from kendall's tau.          Parameters         ----------, Copula correlation parameter using Kendall's tau of sample data.          Parame, Base class for elliptical copula      This class requires subclassing and curren, r"""Gaussian copula.      It is constructed from a multivariate normal distribut (+7 more)

### Community 81 - "Community 81"
Cohesion: 0.08
Nodes (5): Poisson, _validate_l1_method(), Probability that count is not zero          internal use in Censored model, will, Predict response variable or other statistic given exogenous variables., Predict response variable or other statistic given exogenous variables.

### Community 82 - "Community 82"
Cohesion: 0.06
Nodes (16): MVElliptical, Base Class for multivariate elliptical distributions, normal and t      contains, initialize instance          Parameters         ----------         mean : array_, random variable          Parameters         ----------         size : int or tup, logarithm of probability density function          Parameters         ----------, cumulative distribution function          Parameters         ----------, affine transformation define in subclass because of distribution         specifi, whiten the data by linear transformation          Parameters         ---------- (+8 more)

### Community 83 - "Community 83"
Cohesion: 0.09
Nodes (21): _check_for(), _do_plot(), _fmt_probplot_axis(), plotting_pos(), ProbPlot, qqline(), qqplot(), qqplot_2samples() (+13 more)

### Community 84 - "Community 84"
Cohesion: 0.06
Nodes (15): cdf_kernel_asym(), kernel_cdf_gamma(), kernel_pdf_gamma(), kernel_pdf_invgauss(), kernel_pdf_lognorm(), kernel_pdf_recipinvgauss(), pdf_kernel_asym(), Asymmetric kernels for R+ and unit interval  References ----------  .. [1] Bouez (+7 more)

### Community 85 - "Community 85"
Cohesion: 0.11
Nodes (30): _convert_from_multidim(), _convert_to_multidim(), corr2cov(), cov2corr(), Cov2CorrResult, cum2mc(), mc2cum(), mc2mnc() (+22 more)

### Community 86 - "Community 86"
Cohesion: 0.08
Nodes (21): cochrans_q(), mcnemar(), median_test_ksample(), runstest  formulas for mean and var of runs taken from SAS manual NPAR tests, al, use runs test on binary discretized data above/below cutoff      Parameters, Wald-Wolfowitz runstest for two samples      This tests whether two samples come, class for the probability distribution of total runs      This is the exact prob, class for runs in a binary sequence       Parameters     ----------     x : arra (+13 more)

### Community 87 - "Community 87"
Cohesion: 0.08
Nodes (23): _calc_grad(), _calc_wdesign_mat(), DistributedModel, DistributedResults, _est_regularized_debiased(), _est_regularized_naive(), _est_unregularized_naive(), _helper_fit_partition() (+15 more)

### Community 88 - "Community 88"
Cohesion: 0.17
Nodes (23): Exception, RuntimeWarning, IOWarning, Contains custom errors and warnings  Errors should derive from Exception or anot, Error locating the X13 binary, Error when running modes using X13, Unexpected conditions when using X13, X13Error (+15 more)

### Community 89 - "Community 89"
Cohesion: 0.09
Nodes (21): _checkisfit(), kdensity(), kdensityfft(), KDEResult, KDEUnivariate, Univariate Kernel Density Estimators  References ---------- Racine, Jeff. (2008), Attach the density estimate to the KDEUnivariate class          Parameters, Returns the cumulative distribution function evaluated at the support          N (+13 more)

### Community 90 - "Community 90"
Cohesion: 0.12
Nodes (16): EstimatorSettings, Object to specify settings for density estimation or regression      `EstimatorS, Multivariate Conditional and Unconditional Kernel Regression with Mixed Data Typ, Significance test for the categorical variables in a nonparametric     regressio, Computes the test statistic, Calculates the significance level of the variable tested, Calculates the expected conditional mean         m(X, Z=l) for all possible l, # TODO: make default behavior efficient=True above a certain n_obs (+8 more)

### Community 91 - "Community 91"
Cohesion: 0.09
Nodes (28): coef_normalize_cov_truncated(), cov_ogk(), _cov_starting(), CovOGKResult, CovStartingResult, mad0(), _naive_ledoit_wolf_shrinkage(), NaiveLedoitWolfResult (+20 more)

### Community 92 - "Community 92"
Cohesion: 0.10
Nodes (15): DetSStartResult, Created on Apr. 19, 2024 12:17:03 p.m.  Author: Josef Perktold License: BSD-3, # TODO: detect constant, # TODO: iterate until convergence if start fits are not converged, # TODO: add extra start and convergence info, MM-estimator with S-estimator starting values.      Parameters     ----------, Result of one starting-value fit within :meth:`RLMDetS.fit`.      Parameters, Estimate the model          Parameters         ----------         h : int (+7 more)

### Community 93 - "Community 93"
Cohesion: 0.07
Nodes (10): ArmaProcess, r"""     Theoretical properties of an ARMA process for specified lag-polynomials, Create ArmaProcess from AR and MA polynomial roots          Parameters         -, Create ArmaProcess from an ARMA representation          Parameters         -----, Create an ArmaProcess from the results of an ARIMA estimation          Parameter, Roots of autoregressive lag-polynomial, Roots of moving average lag-polynomial, Arma process is stationary if AR roots are outside unit circle          Returns (+2 more)

### Community 94 - "Community 94"
Cohesion: 0.12
Nodes (10): ArchimedeanCopula, FrankCopula, Evaluate cdf of Archimedean copula., Evaluate pdf of Archimedean copula., Evaluate log pdf of multivariate Archimedean copula., r"""Frank copula.      Dependence is symmetric.      .. math::          C_\theta, Generate random variates from the copula.          Parameters         ----------, Conditional cdf of second component given the value of first. (+2 more)

### Community 95 - "Community 95"
Cohesion: 0.10
Nodes (26): _cache_it(), check_internet(), clear_data_home(), Dataset, _get_cache(), _get_data(), get_data_home(), _get_dataset_meta() (+18 more)

### Community 96 - "Community 96"
Cohesion: 0.08
Nodes (12): KernelSmoother, PolySmoother, This module contains scatterplot smoothers, that is classes who generate a smoot, # TODO: undo adjustments and fix dimensions correctly, alias of df_model for backwards compatibility, Degrees of freedom used in the fit., alias for fit,  for backwards compatibility,          do we need it with differe, Residual degrees of freedom from last fit. (+4 more)

### Community 97 - "Community 97"
Cohesion: 0.08
Nodes (26): HuberScale, iqr(), mad(), _qn_naive(), qn_scale(), Support and standalone functions for Robust Linear Models  References ----------, Computes the Qn robust estimator of scale      The Qn scale estimator is a more, A naive implementation of the Qn robust estimator of scale, used solely     to t (+18 more)

### Community 98 - "Community 98"
Cohesion: 0.13
Nodes (26): _asymptotic_pvalue(), distance_correlation(), distance_covariance(), distance_covariance_test(), distance_statistics(), distance_variance(), DistDependStat, _empirical_pvalue() (+18 more)

### Community 99 - "Community 99"
Cohesion: 0.10
Nodes (28): confint_mvmean(), confint_mvmean_fromstats(), CovOnewayResult, CovTestResult, _get_blocks(), HotellingResult, _logdet(), Created on Sun Nov  5 14:48:19 2017  Author: Josef Perktold License: BSD-3 (+20 more)

### Community 100 - "Community 100"
Cohesion: 0.08
Nodes (21): _as_array_with_name(), interpret_data(), is_data_frame(), is_design_matrix(), is_model_matrix(), _is_recarray(), is_series(), _is_using_formulaic() (+13 more)

### Community 101 - "Community 101"
Cohesion: 0.09
Nodes (26): ChisquareProbResult, _combine_bins(), DispersionResults, plot_probs(), Created on Fri Sep 15 12:53:45 2017  Author: Josef Perktold, Result of :func:`test_chisquare_prob`.      Parameters     ----------     statis, Chi-square test for predicted probabilities using cmt-opg.      Parameters     -, Group columns into bins using sums      This is mainly a helper function for com (+18 more)

### Community 102 - "Community 102"
Cohesion: 0.11
Nodes (17): property, _cache_readonly, CachedAttribute, CachedWritableAttribute, deprecated_alias(), Decorators and descriptors used for cached attributes, Descriptor that caches an attribute and permits reassignment, Decorate a method as a CachedAttribute (+9 more)

### Community 103 - "Community 103"
Cohesion: 0.08
Nodes (15): MarkovRegression, MarkovRegressionResults, MarkovRegressionResultsWrapper, Markov switching regression models  Author: Chad Fulton License: BSD-3, r"""     First-order k-regime Markov switching regression model      Parameters, In-sample prediction, conditional on the current regime          Parameters, Compute loglikelihoods conditional on the current period's regime, EM iteration          Notes         -----         This uses the inherited _em_it (+7 more)

### Community 104 - "Community 104"
Cohesion: 0.10
Nodes (26): ChisquareBinningResult, cov_multinomial(), prob_larger_2ordinal(), prob_larger_ordinal_choice(), Created on Tue Oct  6 12:42:11 2020  Author: Josef Perktold License: BSD-3, probability that observed category is larger than distribution prob      This is, Stochastically large probability for two ordinal distributions      Computes Pr(, Result of :func:`test_chisquare_binning`.      Parameters     ----------     sta (+18 more)

### Community 105 - "Community 105"
Cohesion: 0.07
Nodes (15): KFold, KStepAhead, LeaveOneLabelOut, LeavePOut, Utilities for cross validation.  taken from scikits.learn  # Author: Alexandre G, K-Folds cross validation iterator:     Provides train/test indexes to split data, K-Folds cross validation iterator:         Provides train/test indexes to split, Leave-One-Label_Out cross-validation iterator:     Provides train/test indexes t (+7 more)

### Community 106 - "Community 106"
Cohesion: 0.10
Nodes (25): check_kwargs(), _check_method(), _fit_basinhopping(), _fit_bfgs(), _fit_cg(), _fit_lbfgs(), _fit_minimize(), _fit_ncg() (+17 more)

### Community 107 - "Community 107"
Cohesion: 0.09
Nodes (19): _calc_incidence_right(), _calc_survfunc_right(), _checkargs(), CumIncidenceRight, plot_survfunc(), Calculate the survival function and its standard error for a     single group, Calculate the cumulative incidence function and its standard error      Paramete, Estimation and inference for a cumulative incidence function      If J = 1, 2, . (+11 more)

### Community 108 - "Community 108"
Cohesion: 0.09
Nodes (14): _OptFuncts, A class that holds functions that are optimized/solved      The general setup of, Transform the log of observation probabilities          In terms of the Lagrange, Calculate the hessian of a weighted empirical likelihood problem          Parame, Calculate the gradient of a weighted empirical likelihood problem          Param, Modified Newton's method for maximizing the log 'star' equation          This fu, Find the root of sum(xi-h0)/(1+eta(xi-mu))          Solves for eta when computin, Finds gamma that satisfies         sum(log(n * w(gamma))) - log(r0) = 0 (+6 more)

### Community 109 - "Community 109"
Cohesion: 0.13
Nodes (5): Mapping, NumpyDocString, Parses a numpydoc string to an abstract representation      Instances define a m, func_name : Descriptive text             continued text         another_func_nam, .. index: default         :refguide: something, else, and more

### Community 110 - "Community 110"
Cohesion: 0.11
Nodes (18): get_lilliefors_table(), ksstat(), kstest_fit(), _make_asymptotic_function(), pval_lf(), Implements Lilliefors corrected Kolmogorov-Smirnov tests for normal and exponent, Generates tables for significance levels of Lilliefors test statistics      Tabl, Approximate pvalues for Lilliefors test      This is only valid for pvalues smal (+10 more)

### Community 111 - "Community 111"
Cohesion: 0.08
Nodes (13): DescrStatsW, alias for number of observations/cases, equal to sum of weights, data with weighted mean subtracted, weighted sum of squares of demeaned data, standard deviation with default degrees of freedom correction, weighted covariance of data if data is 2 dimensional          assumes variables, weighted correlation with default ddof          assumes variables in columns and, standard deviation of weighted mean (+5 more)

### Community 112 - "Community 112"
Cohesion: 0.09
Nodes (19): Run the test suite      Parameters     ----------     extra_args : list[str], test(), _CompatUnpickler, load_pickle(), Helper files for pickling, Unpickler that remaps module paths for backward compatibility      statsmodels.t, Load a previously saved object      .. warning::         Loading pickled models, Save the object to file via pickling      Parameters     ----------     obj : ob (+11 more)

### Community 113 - "Community 113"
Cohesion: 0.09
Nodes (15): Copula, r"""A generic Copula class meant for subclassing.      Notes     -----     A fun, Draw `n` in the half-open interval ``[0, 1)``.          Marginals are uniformly, Probability density function of copula.          Parameters         ----------, Log of copula pdf, loglikelihood.          Parameters         ----------, Cumulative distribution function evaluated at points u.          Parameters, Sample the copula and plot.          Parameters         ----------         sampl, Plot the PDF.          Parameters         ----------         ticks_nbr : int, op (+7 more)

### Community 114 - "Community 114"
Cohesion: 0.08
Nodes (4): Generic Zero-Inflated model Hessian matrix of the log-likelihood.          Param, Predict values for conditional variance V(endog | exog)          Parameters, Predict values for conditional variance V(endog | exog)          Parameters, GeneralizedPoisson

### Community 115 - "Community 115"
Cohesion: 0.08
Nodes (14): BernsteinDistribution, BernsteinDistributionBV, BernsteinDistributionUV, Created on Wed Feb 17 15:35:23 2021  Author: Josef Perktold License: BSD-3, pdf values evaluated at x.          Parameters         ----------         x : ar, # TODO: check usage of k_grid_product. Should this go into eval?, Get marginal BernsteinDistribution.          Parameters         ----------, Generate random numbers from distribution.          Parameters         --------- (+6 more)

### Community 116 - "Community 116"
Cohesion: 0.08
Nodes (13): PHRegResults, Class to contain results of fitting a Cox proportional hazards     survival mode, Returns the standard errors of the parameter estimates, Returns the standard errors of the parameter estimates, Returns a scipy distribution object corresponding to the         distribution of, Descriptive statistics of the groups          Parameters         ----------, The average covariate values within the at-risk set at each         event time p, A matrix containing the score residuals (+5 more)

### Community 117 - "Community 117"
Cohesion: 0.09
Nodes (13): Estimate STL and forecasting model parameters          Parameters         ------, Results for forecasting using STL to remove seasonality      Parameters     ----, The period of the seasonal component, The STL instance used to decompose the time series, The result of applying STL to the data, The model fit to the additively deseasonalized data, The result class from the estimated model, Summary of both the STL decomposition and the model fit          Returns (+5 more)

### Community 118 - "Community 118"
Cohesion: 0.11
Nodes (25): month_plot(), plot_accf_grid(), plot_acf(), plot_ccf(), _plot_corr(), plot_pacf(), plot_pccf(), plot_predict() (+17 more)

### Community 119 - "Community 119"
Cohesion: 0.10
Nodes (13): Holder, compat_2tuple_unpack(), HolderTuple, Base classes for statistical test results  Created on Mon Apr 22 14:03:21 2013, Results class for pairwise comparisons, based on p-values      Parameters     --, Holder class with indexing      .. deprecated:: 0.15         ``HolderTuple`` is, p-values corrected for multiple testing problem          This uses the default p, # TODO: breaks with method=None (+5 more)

### Community 120 - "Community 120"
Cohesion: 0.11
Nodes (13): LeaveOneOut, Generator to give leave-one-out views on X      Parameters     ----------     X, KernelReg, Local linear estimator of g(x) in the regression ``y = g(x) + e``          Param, Local constant estimator of g(x) in the regression         y = g(x) + e, Computes the AIC Hurvich criteria for the estimation of the bandwidth          P, r"""         The cross-validation function with leave-one-out estimator, r"""         Returns the R-Squared for the nonparametric regression          Ret (+5 more)

### Community 121 - "Community 121"
Cohesion: 0.09
Nodes (23): aitchison_aitken(), aitchison_aitken_cdf(), aitchison_aitken_convolution(), aitchison_aitken_reg(), Epanechnikov, gaussian_cdf(), gaussian_convolution(), This models contains the Kernels for Kernel smoothing.  Hopefully in the future (+15 more)

### Community 122 - "Community 122"
Cohesion: 0.08
Nodes (13): Construct a Table object from data          Parameters         ----------, Estimate marginal probability distributions for the rows and columns          Re, Returns fitted joint probabilities under independence          The returned tabl, Returns fitted cell counts under independence          The returned cell counts, Returns Pearson residuals          The Pearson residuals are calculated under a, Returns standardized residuals under independence, Returns the contributions to the chi^2 statistic for independence          The r, Returns local log odds ratios          The local log odds ratios are the log odd (+5 more)

### Community 123 - "Community 123"
Cohesion: 0.13
Nodes (21): Return the threshold statistic for a given target FDR          Parameters, Control FDR in a regression procedure      Parameters     ----------     endog :, RegressionFDR, _ecdf(), fdrcorrection(), fdrcorrection_twostage(), local_fdr(), local_fdr_correction() (+13 more)

### Community 124 - "Community 124"
Cohesion: 0.10
Nodes (12): ARIMA, ARIMAResults, ARMA, ARMAResults, See statsmodels.tsa.arima.model.ARIMA and statsmodels.tsa.SARIMAX, ARMA has been deprecated in favor of the new implementation      See Also     --, ARIMA has been deprecated in favor of the new implementation      See Also     -, ARMA has been deprecated in favor of the new implementation      See Also     -- (+4 more)

### Community 125 - "Community 125"
Cohesion: 0.09
Nodes (4): Predict values for conditional variance V(endog | exog)          Parameters, list of exogs, for internal use in post-estimation, Derivative of score_obs w.r.t. endog          Parameters         ----------, NegativeBinomialP

### Community 126 - "Community 126"
Cohesion: 0.08
Nodes (13): Family, r"""         Weights for IRLS steps          Parameters         ----------, r"""         The deviance function evaluated at (endog, mu, var_weights,, r"""         The deviance residuals          Parameters         ----------, r"""         Fitted values based on linear predictors lin_pred.          Paramet, Linear predictors based on given mu values.          Parameters         --------, The parent class for one-parameter exponential families.      Parameters     ---, r"""         The log-likelihood function for each observation in terms of the fi (+5 more)

### Community 127 - "Community 127"
Cohesion: 0.10
Nodes (17): inverse_power, inverse_squared, InversePower, InverseSquared, _link_deprecation_warning(), nbinom, Defines the link functions to be used with GLM and GEE families., # TODO: Deprecated aliases, remove after 0.15 (+9 more)

### Community 128 - "Community 128"
Cohesion: 0.09
Nodes (12): FactorResults, Plot of the ordered eigenvalues and variance explained for the loadings, Plot factor loadings in 2-d plots          Parameters         ----------, Returns the fitted covariance matrix, The standard errors of the uniquenesses          Parameters         ----------, The standard errors of the loadings          Standard errors are only available, Factor results class      For result summary, scree/loading plots and factor rot, Apply rotation, inplace modification of this Results instance          Parameter (+4 more)

### Community 129 - "Community 129"
Cohesion: 0.08
Nodes (13): CustomKernel, Generic 1D Kernel object.     Can be constructed by selecting a standard named K, shape should be a function taking and returning numeric type.          For sanit, Getter for kernel bandwidth, h, Setter for kernel bandwidth, h, Returns the integral of the square of the kernal from -inf to inf, Normalising constant for kernel (integral from -inf to inf), Returns the second moment of the kernel (+5 more)

### Community 130 - "Community 130"
Cohesion: 0.09
Nodes (13): MarkovAutoregression, MarkovAutoregressionResults, MarkovAutoregressionResultsWrapper, Markov switching autoregression models  Author: Chad Fulton License: BSD-3, In-sample prediction, conditional on the current and previous regime          Pa, r"""     Markov switching autoregression model      Parameters     ----------, Compute loglikelihoods conditional on the current period's regime and the last `, EM step for autoregressive coefficients and variances (+5 more)

### Community 131 - "Community 131"
Cohesion: 0.11
Nodes (5): DynamicFactor, r"""     Dynamic factor model      Parameters     ----------     endog : array_l, Transform unconstrained parameters used by the optimizer to constrained, Transform constrained parameters used in likelihood evaluation         to uncons, Update the parameters of the model          Updates the representation matrices

### Community 132 - "Community 132"
Cohesion: 0.14
Nodes (4): CalendarTimeTrend, Extend the forecast index, r"""     Constant and time trend deterministic terms based on calendar time, Create a TimeTrend from a string description.          Provided for compatibilit

### Community 133 - "Community 133"
Cohesion: 0.09
Nodes (2): ModelData, Class responsible for handling input data and extracting metadata into the     a

### Community 134 - "Community 134"
Cohesion: 0.09
Nodes (8): Fit the model with some parameters subject to equality constraints          Para, (array) Starting parameters for maximum likelihood estimation, (list of str) List of human readable parameter names (for parameters actually in, Not implemented for state space models, This is a temporary base model from ETS; here I just copy everything I need, Hessian matrix computed by second-order complex-step differentiation on the `log, Fix parameters to specific values (context manager)          Parameters, StateSpaceMLEModel

### Community 135 - "Community 135"
Cohesion: 0.08
Nodes (13): Get the formula engine., Get the engine-specific error that may occur when evaluating a factor., Get the engine-specific error that may occur when materializing a formula., Get the formula-engine-specific intercept term.          Returns         -------, Get an empty evaluation environment.          Returns         -------         {E, Check if the model specification has an intercept term.          Parameters, Returns boolean array index indicating which column holds the intercept., Get the model specification from a formula.          Parameters         -------- (+5 more)

### Community 136 - "Community 136"
Cohesion: 0.13
Nodes (23): _func(), _interpolate_p(), _interpolate_v(), _isfloat(), _phi(), _psturng(), _psturng_scalar(), _ptransform() (+15 more)

### Community 137 - "Community 137"
Cohesion: 0.10
Nodes (11): BaseIRAnalysis, Impulse response-related code, Plot impulse responses          Parameters         ----------         orth : boo, Base class for plotting and computing IRF-related statistics, designed     to ha, Plot cumulative impulse response functions          Parameters         ---------, IRF Monte Carlo integrated error bands          Parameters         ----------, IRF Sims-Zha error band method 1. Assumes symmetric error bands around         m, IRF Sims-Zha error band method 2          This method does not assume symmetric (+3 more)

### Community 138 - "Community 138"
Cohesion: 0.10
Nodes (22): call_cached_func(), deprecate_kwarg(), get_cached_doc(), get_cached_func(), infer_freq(), _infer_freq_returns_offset(), is_float_index(), is_int_index() (+14 more)

### Community 139 - "Community 139"
Cohesion: 0.09
Nodes (1): DiscreteResults

### Community 140 - "Community 140"
Cohesion: 0.14
Nodes (17): cffilter(), # NOTE: uses a loop, could probably be sped-up for very large datasets, Christiano Fitzgerald asymmetric, random walk filter      Parameters     -------, # TODO: cythonize/vectorize loop?, add ability for symmetric filter,, CycleTrendResult, Result of :func:`cffilter`, :func:`hamilton_filter`, and     :func:`hpfilter`: a, hamilton_filter(), Hamilton (2018) filter — regression-based trend-cycle decomposition.  References (+9 more)

### Community 141 - "Community 141"
Cohesion: 0.11
Nodes (12): BayesGaussMI, MI, MIResults, Cycle through all Gibbs updates, Gibbs update of the missing data values, Gibbs update of the mean vector          Do not call until update_data has been, Gibbs update of the covariance matrix          Do not call until update_data has, MI performs multiple imputation using a provided imputer object      Parameters (+4 more)

### Community 142 - "Community 142"
Cohesion: 0.10
Nodes (17): ARCovariance, corr2cov(), corr_ar(), corr_arma(), corr_equi(), Correlation and Covariance Structures  Created on Sat Dec 17 20:46:05 2011  Auth, Whiten a series of columns according to an AR(p) covariance structure.      This, # TODO: dimension handling is not DRY (+9 more)

### Community 143 - "Community 143"
Cohesion: 0.11
Nodes (12): Construct a StratifiedTable object from data          Parameters         -------, Test that all tables have odds ratio equal to 1          This is the 'Mantel-Hae, The pooled odds ratio          The value is an estimate of a common odds ratio a, Returns the logarithm of the pooled odds ratio          See oddsratio_pooled for, Estimate of the pooled risk ratio, Estimated standard error of the pooled log odds ratio          Based on work by:, A confidence interval for the pooled log odds ratio          Parameters, A confidence interval for the pooled odds ratio          Parameters         ---- (+4 more)

### Community 144 - "Community 144"
Cohesion: 0.09
Nodes (13): FTestAnovaPower, _GofChisquareIndPower, Power, Statistical Power calculations F-test for one factor balanced ANOVA      This is, Calculate the power of a F-test for one factor ANOVA          Parameters, Solve for any one parameter of the power of a F-test          for the one sample, experimental, test failure in solve_power for effect_size, Statistical Power calculations for chisquare goodness-of-fit test      TODO: thi (+5 more)

### Community 145 - "Community 145"
Cohesion: 0.12
Nodes (22): approx_fprime(), approx_fprime_cs(), _approx_fprime_cs_scalar(), _approx_fprime_scalar(), approx_hess(), approx_hess1(), approx_hess2(), approx_hess3() (+14 more)

### Community 146 - "Community 146"
Cohesion: 0.13
Nodes (21): CF_objective(), ff_partial_target(), ff_target(), Gf(), GPA(), oblimin_objective(), orthomax_objective(), This file contains a Python version of the gradient projection rotation algorith (+13 more)

### Community 147 - "Community 147"
Cohesion: 0.12
Nodes (21): cohn_numbers(), _detection_limit_index(), _do_ros(), _impute(), impute_ros(), _norm_plot_pos(), plotting_positions(), Implementation of Regression on Order Statistics for imputing left- censored (no (+13 more)

### Community 148 - "Community 148"
Cohesion: 0.12
Nodes (12): Myfunc, NonlinearLS, Return the predicted values for `params`          Parameters         ----------, Non-linear prediction function, to be defined by a subclass          Parameters, Return starting values for the parameters          Returns         -------, Return the (optionally weighted) residuals at `params`          Parameters, Return the sum of squared (weighted) residuals at `params`          Parameters, Estimate the parameters of the model by non-linear least squares          Parame (+4 more)

### Community 149 - "Community 149"
Cohesion: 0.10
Nodes (13): _cabs(), estimate_location(), HuberT, # TODO: c needs to be changed if k != 4, Estimate a robust location parameter using an M-estimator.      This function it, Huber's T for M estimation      Parameters     ----------     t : float, optiona, Set and change the tuning parameter of the Norm          Parameters         ----, Huber's T is defined piecewise over the range of z          Parameters         - (+5 more)

### Community 150 - "Community 150"
Cohesion: 0.13
Nodes (11): Mediation, MediationResults, _pvalue(), Mediation analysis  Implements algorithm 1 ('parametric inference') and algorith, Simulate model parameters from fitted sampling distribution          Parameters, Return the mediator exog matrix with exposure set to the given         value.  S, Return the exog design matrix with mediator and exposure set to         the give, Conduct a mediation analysis      Parameters     ----------     outcome_model : (+3 more)

### Community 151 - "Community 151"
Cohesion: 0.09
Nodes (17): comp_matrix(), eigval_decomp(), get_var_endog(), make_lag_names(), parse_lutkepohl_data(), Miscellaneous utility code for VAR estimation, Return companion matrix for the VAR(1) representation for a VAR(p) process     (, Parse data files from Lütkepohl (2005) book      Source for data files: www.jmul (+9 more)

### Community 152 - "Community 152"
Cohesion: 0.10
Nodes (11): PHReg, Returns the score residuals calculated at a given vector of         parameters, Returns the hazard-weighted average of covariate values for         subjects who, Estimate the baseline cumulative hazard and survival         functions, Returns a function that calculates the baseline cumulative         hazard functi, Cox Proportional Hazards Regression Model      The Cox PH Model is for right cen, Create a proportional hazards regression model from a formula         and datafr, r"""         Return a regularized fit to a proportional hazards regression model (+3 more)

### Community 153 - "Community 153"
Cohesion: 0.11
Nodes (17): _adjust_shape(), _compute_min_std_IQR(), _compute_subset(), _get_type_pos(), gpke(), initialize_generator(), Module containing the base object for multivariate kernel density and regression, Computes the measure of dispersion          The minimum of the standard deviatio (+9 more)

### Community 154 - "Community 154"
Cohesion: 0.11
Nodes (15): aggregate_raters(), cohens_kappa(), fleiss_kappa(), _int_ifclose(), KappaResults, Inter Rater Agreement  Created on Thu Dec 06 22:57:56 2012 Author: Josef Perktol, Convert raw data with shape (subject, rater) to (rater1, rater2)      Brings dat, Fleiss' and Randolph's kappa multi-rater agreement measure      Parameters     - (+7 more)

### Community 155 - "Community 155"
Cohesion: 0.12
Nodes (15): dedent_lines(), indent(), Substantially copied from NumpyDoc 1.0pre, Deindent a list of lines maximally      Parameters     ----------     lines : li, Remove leading and trailing blank lines from a list of lines      Parameters, Remove parameters from the Parameters section of the docstring          Paramete, Insert parameters into the Parameters section of the docstring          Paramete, Replace a block of the docstring with a new block          Parameters         -- (+7 more)

### Community 156 - "Community 156"
Cohesion: 0.11
Nodes (11): ArmaProcess, ArmaFft, construct AR and MA polynomials that are zero-padded to a common length, power spectral density using padding to length n done by fft          currently, this looks bad, maybe with an fftshift, spectral density for frequency using polynomial roots          builds two arrays, spectral density for frequency using polynomial roots          builds two arrays, spectral density from MA polynomial representation for ARMA process          Ref (+3 more)

### Community 157 - "Community 157"
Cohesion: 0.10
Nodes (13): li3(), li4(), lin(), Special functions for copulas not available in scipy  Created on Jan. 27, 2023, Stirling numbers of the first kind, clear cache of Sterling numbers, Stirling numbers of the second kind, clear cache of Sterling numbers (+5 more)

### Community 158 - "Community 158"
Cohesion: 0.13
Nodes (1): NegativeBinomial

### Community 159 - "Community 159"
Cohesion: 0.10
Nodes (11): Grouping, Represent a pandas-style grouping index and related transformations      Paramet, Shape of the underlying (Multi)Index          Returns         -------         tu, Unique values for each grouping level          Returns         -------         F, Integer codes for each grouping level          Returns         -------         n, Names of the grouping levels          Returns         -------         FrozenList, Set `counts` to the bincount of the labels at the given level          Parameter, Sanity check that the index is sorted and/or unique          Parameters (+3 more)

### Community 160 - "Community 160"
Cohesion: 0.11
Nodes (11): Identity, Power, Deprecated alias of Identity.      .. deprecated:: 0.14.0          Use Identity, The power transform      Parameters     ----------     power : float         The, Power transform link function          Parameters         ----------         p :, Inverse of the power transform link function          Parameters         -------, Derivative of the power transform          Parameters         ----------, Second derivative of the power transform          Parameters         ---------- (+3 more)

### Community 161 - "Community 161"
Cohesion: 0.13
Nodes (15): _cov_iter(), cov_weighted(), CovIterResult, CovM, CovMResult, mahalanobis(), Weighted mean and covariance (for M-estimators)      wmean = sum (weights * data, Result of :func:`_cov_iter`.      Parameters     ----------     cov : ndarray (+7 more)

### Community 162 - "Community 162"
Cohesion: 0.11
Nodes (9): numpy array of trimmed and sorted data, mean of winsorized data, variance of winsorized data, standard error of trimmed mean, standard error of winsorized mean, One sample t-test for trimmed or Winsorized mean          Parameters         ---, Create a TrimmedMean instance with a new trimming fraction          This reuses, Class for trimmed and winsorized one sample statistics      axis is None, i.e., (+1 more)

### Community 163 - "Community 163"
Cohesion: 0.20
Nodes (4): Grab signature (if given) and summary, A line-based string reader, Parameters         ----------         data : str or list[str]             String, Reader

### Community 164 - "Community 164"
Cohesion: 0.16
Nodes (12): cumulant_from_moments(), ExpandedNormal, _faa_di_bruno_partitions(), _norm_cdf(), _norm_pdf(), _norm_sf(), Construct the Edgeworth expansion pdf given cumulants.      Parameters     -----, Return all non-negative integer solutions of the diophantine equation (+4 more)

### Community 165 - "Community 165"
Cohesion: 0.12
Nodes (7): mvndst(), mvnormcdf(), mvstdnormcdf(), Various extensions to distributions  * skew normal and skew t distribution by Az, standardized multivariate normal cumulative distribution function      This is a, multivariate normal cumulative distribution function      This is a wrapper for, # TODO: rename these functions to have unique names

### Community 166 - "Community 166"
Cohesion: 0.18
Nodes (11): EmpLikeTestResult, Result of an empirical likelihood hypothesis test.      Returned by the ``test_*, ELOriginRegress, OriginResults, This module implements empirical likelihood regression that is forced through th, A Results class for empirical likelihood regression through the origin      Para, Returns the llr and p-value for a hypothesized parameter value         for a reg, Returns the confidence interval for a regression parameter when the         regr (+3 more)

### Community 167 - "Community 167"
Cohesion: 0.11
Nodes (10): Package with factor rotation algorithms.  This file contains a Python version of, This module contains the one-parameter exponential families used for fitting GLM, Tools for nonparametric statistics, mainly density estimation and regression  Fo, Regression models and results, Utility functions and testing helpers for statsmodels, PytestTester, Pytest runner that allows tests to be run within Python, Initialize the tester for the calling module's package          Parameters (+2 more)

### Community 168 - "Community 168"
Cohesion: 0.12
Nodes (9): Biweight, Returns the filtered (xs, ys) based on the Kernel domain centred on x, Returns the kernel density estimate for point x based on x-values         xs, Returns the kernel smoothing estimate for point x based on x-values         xs a, Returns the kernel smoothing estimate of the variance at point x., Returns the kernel smoothing estimate with confidence 1sigma bounds, Returns the kernel smoothing estimate for point x based on x-values         xs a, Returns the kernel smoothing estimate of the variance at point x. (+1 more)

### Community 169 - "Community 169"
Cohesion: 0.16
Nodes (17): lowess(), _lowess_bisquare(), _lowess_initial_fit(), _lowess_mycube(), _lowess_robustify_fit(), _lowess_tricube(), _lowess_update_nn(), _lowess_wt_standardize() (+9 more)

### Community 170 - "Community 170"
Cohesion: 0.13
Nodes (7): Recursive least squares model  Author: Chad Fulton License: Simplified-BSD, Create a `RecursiveLS` model instance from a formula and dataframe.          Par, Fits the model by application of the Kalman filter          Returns         ----, Update the parameters of the model          This model has no estimable paramete, r"""     Recursive least squares      Parameters     ----------     endog : arra, RecursiveLS, RecursiveLSResultsWrapper

### Community 171 - "Community 171"
Cohesion: 0.12
Nodes (17): chisquare(), chisquare_effectsize(), chisquare_power(), ChisquareResult, gof_binning_discrete(), gof_chisquare_discrete(), powerdiscrepancy(), Extra statistical function and helper functions  contains:  * goodness-of-fit te (+9 more)

### Community 172 - "Community 172"
Cohesion: 0.11
Nodes (17): assert_equal(), bunch_factory(), check_fitted(), check_ftest_pvalues(), check_predict_types(), check_ttest_tvalues(), assert functions from numpy and pandas testing, Check that fitted values are consistent with resid and predict      Parameters (+9 more)

### Community 173 - "Community 173"
Cohesion: 0.12
Nodes (17): array_like(), bool_like(), dict_like(), float_like(), int_like(), Validation helpers for array-like and scalar inputs, Remove trailing singleton dimensions      Parameters     ----------     arr : nd, Convert to bool or raise if not bool_like      Parameters     ----------     val (+9 more)

### Community 174 - "Community 174"
Cohesion: 0.16
Nodes (12): acorr_plot(), adjust_subplots(), _get_irf_plot_config(), irf_grid_plot(), MPLConfigurator, plot_full_acorr(), plot_mts(), plot_with_error() (+4 more)

### Community 175 - "Community 175"
Cohesion: 0.13
Nodes (16): get_robustcov_results(), normalize_cov_type(), Created on Mon Aug 04 08:00:16 2014  Author: Josef Perktold License: BSD-3, # TODO: more options needed here, # TODO: make separate function that returns a robust cov plus info, # TODO: check also use_correction, do I need all combinations?, # TODO: this should be outsourced in a function so we can reuse it in, # TODO: make it DRYer   repeated code for checking kwds (+8 more)

### Community 176 - "Community 176"
Cohesion: 0.13
Nodes (12): _conf_set(), ECDF, ECDFDiscrete, monotone_fn_inverter(), Empirical CDF Functions, Return the Empirical CDF of an array as a step function.      Parameters     ---, # TODO: make `step` an arg and have a linear interpolation option?, Return the Empirical Weighted CDF of an array as a step function.      Parameter (+4 more)

### Community 177 - "Community 177"
Cohesion: 0.12
Nodes (9): CDFLink, The use the CDF of a scipy.stats distribution      CDFLink is a subclass of logi, CDF link function          Parameters         ----------         p : array_like, The inverse of the CDF link          Parameters         ----------         z : a, Derivative of CDF link          Parameters         ----------         p : array_, Second derivative of the link function g''(p)          implemented through numer, Second derivative of the link function g''(p)          implemented through numer, Derivative of the inverse link function          Parameters         ---------- (+1 more)

### Community 178 - "Community 178"
Cohesion: 0.13
Nodes (10): CyclicCubicSplines, _equally_spaced_knots(), Penalty matrix ``s = d.T.dot(b^-1).dot(d)``., Create the spline basis for new observations          Parameters         -------, additive smooth components using cyclic cubic regression splines      This splin, Compute equally spaced knots over the range of x      Parameters     ----------, cyclic cubic regression spline single smooth component      This creates and hol, Build the cyclic cubic regression spline basis and penalty          Returns (+2 more)

### Community 179 - "Community 179"
Cohesion: 0.19
Nodes (3): PredictionResults, r"""     Results of in-sample and out-of-sample prediction for state space model, Provide access to the representation and filtered output in the         appropri

### Community 180 - "Community 180"
Cohesion: 0.21
Nodes (14): _check_errors(), _check_x12(), _clean_order(), _convert_out_to_series(), _find_x12(), _make_automdl_options(), _make_forecast_options(), _make_regression_options() (+6 more)

### Community 181 - "Community 181"
Cohesion: 0.18
Nodes (9): The SCAD penalty of Fan and Li, quadratically smoothed around zero.      This fo, Work around for Null model          This will not be needed anymore when we can, SCADSmoothed, Created on Sat May 19 15:53:21 2018  Author: Josef Perktold License: BSD-3, # TODO: check what we want to do here, Results for Variable Screening      Note: Indices except for exog_idx and in the, # TODO: does it really help to change/trim params, # TODO: remove the need for x, use x1 separately from x0 (+1 more)

### Community 182 - "Community 182"
Cohesion: 0.14
Nodes (11): get_index_label_loc(), get_index_loc(), get_prediction_index(), Get the location of a specific key in an index or model row labels      Paramete, Get the location of the start and end of prediction, and the associated index, Get the location of a specific key in an index      Parameters     ----------, Get the location of a specific key in an index          Parameters         -----, Get the location of a specific key in an index or model row labels          Para (+3 more)

### Community 183 - "Community 183"
Cohesion: 0.13
Nodes (15): asbytes(), asstr(), asunicode(), lmap(), lrange(), lzip(), Compatibility tools for differences between Python 2 and 3, A list-producing version of zip      Parameters     ----------     *args (+7 more)

### Community 184 - "Community 184"
Cohesion: 0.15
Nodes (8): IndependenceCopula, _kernel_rvs_beta(), _kernel_rvs_beta1(), Created on Fri Jan 29 19:19:45 2021  Author: Josef Perktold License: BSD-3, Independence copula.      Copula with independent random variables.      .. math, Generate random variates from the copula.          Parameters         ----------, Random sampling from empirical copula using Beta distribution      Parameters, rvs_kernel()

### Community 185 - "Community 185"
Cohesion: 0.15
Nodes (11): API for empirical likelihood, ANOVA, _ANOVAOpt, ANOVAResult, This script contains empirical likelihood ANOVA  Currently the script only conta, Returns -2 log likelihood, the pvalue and the maximum likelihood         estimat, Result of :meth:`ANOVA.compute_ANOVA`.      Parameters     ----------     llr :, Class containing functions that are optimized over when     conducting ANOVA (+3 more)

### Community 186 - "Community 186"
Cohesion: 0.13
Nodes (9): LogC, The log-complement transform      .. deprecated:: 0.14.0         Use LogC instea, The log-complement transform      Notes     -----     call and derivative call a, Log-complement transform link function          Parameters         ----------, Inverse of log-complement transform link function          Parameters         --, Derivative of log-complement transform link function          Parameters, Second derivative of the log-complement transform link function          Paramet, Derivative of the inverse of the log-complement transform link         function (+1 more)

### Community 187 - "Community 187"
Cohesion: 0.13
Nodes (9): Logit, Alias of Logit      .. deprecated:: 0.14.0         Use Logit instead., The logit transform      Notes     -----     call and derivative use a private m, Clip logistic values to range (eps, 1-eps)          Parameters         ---------, The logit transform          Parameters         ----------         p : array_lik, Inverse of the logit transform          Parameters         ----------         z, Derivative of the logit transform          Parameters         ----------, Derivative of the inverse of the logit transform          Parameters         --- (+1 more)

### Community 188 - "Community 188"
Cohesion: 0.13
Nodes (9): LogLog, The log-log transform      LogLog inherits from Logit in order to have access to, Log-Log transform link function          Parameters         ----------         p, Inverse of Log-Log transform link function           Parameters         --------, Derivative of Log-Log transform link function          Parameters         ------, Second derivative of the Log-Log link function          Parameters         -----, Derivative of the inverse of the Log-Log transform link function          Parame, Second derivative of the inverse of the Log-Log transform link function (+1 more)

### Community 189 - "Community 189"
Cohesion: 0.13
Nodes (9): LikelihoodModel, Base Classes for Likelihood Models in time series analysis  Warning: imports num, # TODO: I take it this is only a stub and should be included in another, Univariate time series model for estimation with maximum likelihood      Notes, Loglikelihood for timeseries model          Parameters         ----------, Score vector for Arma model, Hessian of arma model, currently uses numdifftools, Estimate model by minimizing negative loglikelihood          Does this need to b (+1 more)

### Community 190 - "Community 190"
Cohesion: 0.14
Nodes (9): CovDetMM, CovDetS, S-estimator for mean and covariance with deterministic starts      Parameters, Starting parameters from a subsample given by index          Parameters, Compute local M-estimator for one starting set of observations          Paramete, Compute S-estimator of mean and covariance          Parameters         ---------, MM estimator using DetS as first stage estimator      Note: The tuning parameter, Estimate model parameters          Parameters         ----------         maxiter (+1 more)

### Community 191 - "Community 191"
Cohesion: 0.13
Nodes (8): AndrewWave, Andrew's wave for M estimation      Parameters     ----------     a : float, opt, Set and change the tuning parameter of the Norm          Parameters         ----, Andrew's wave is defined piecewise over the range of z          Parameters, r"""         The robust criterion function for Andrew's wave          Parameters, r"""         The psi function for Andrew's wave          The analytic derivative, r"""         Andrew's wave weighting function for the IRLS algorithm          Th, The derivative of Andrew's wave psi function          Parameters         -------

### Community 192 - "Community 192"
Cohesion: 0.13
Nodes (8): Hampel, Hampel's function is defined piecewise over the range of z          Parameters, r"""         The robust criterion function for Hampel's estimator          Param, r"""         The psi function for Hampel's estimator          The analytic deriv, r"""         Hampel weighting function for the IRLS algorithm          The psi f, Derivative of psi function, second derivative of rho function          Parameter, Hampel function for M-estimation      Parameters     ----------     a, b, c : fl, Set and change the tuning parameter of the Norm          The tuning constants `a

### Community 193 - "Community 193"
Cohesion: 0.13
Nodes (8): Variant of Tukey's biweight function with power 4 for M-estimation      Paramete, Set and change the tuning parameter of the Norm          Parameters         ----, TukeyQuartic is defined piecewise over the range of z          Parameters, r"""         The robust criterion function for TukeyQuartic norm          Parame, r"""         The psi function of TukeyQuartic norm          The analytic derivat, r"""         TukeyQuartic weighting function for the IRLS algorithm          The, The derivative of the TukeyQuartic psi function          Parameters         ----, TukeyQuartic

### Community 194 - "Community 194"
Cohesion: 0.13
Nodes (8): Trimmed mean function for M-estimation      Parameters     ----------     c : fl, Set and change the tuning parameter of the Norm          Parameters         ----, Least trimmed mean is defined piecewise over the range of z          Parameters, r"""         The robust criterion function for least trimmed mean          Param, r"""         The psi function for least trimmed mean          The analytic deriv, r"""         Least trimmed mean weighting function for the IRLS algorithm, The derivative of least trimmed mean psi function          Parameters         --, TrimmedMean

### Community 195 - "Community 195"
Cohesion: 0.13
Nodes (8): DecomposeResult, Results class for seasonal decompositions      Parameters     ----------     obs, The estimated seasonal component, The estimated trend component, The estimated residuals, The weights used in the robust estimation, Number of observations, Plot estimated components          Parameters         ----------         observe

### Community 196 - "Community 196"
Cohesion: 0.14
Nodes (8): Value of the function evaluated at the attached params          Note: This is no, Joint hypothesis tests that H0: f(params) = value          The alternative hypot, Standard error for each equation (row) treated separately, Standard error for each equation (row) treated separately, Confidence interval for predicted based on delta method          Parameters, Summarize the Results of the nonlinear transformation          This provides a p, First derivative, jacobian of func evaluated at params          Parameters, Covariance matrix of the transformed random variable

### Community 197 - "Community 197"
Cohesion: 0.19
Nodes (4): MSTL, Author: Kishan Manani License: BSD-3 Clause  An implementation of MSTL [1], an a, Estimate a trend component, multiple seasonal components, and a         residual, MSTL(endog, periods=None, windows=None, lmbda=None, iterate=2,          stl_kwar

### Community 198 - "Community 198"
Cohesion: 0.17
Nodes (11): _make_index(), mixture_rvs(), MixtureDistribution, mv_mixture_rvs(), Sample from a mixture of distributions.          Parameters         ----------, pdf a mixture of distributions.          Parameters         ----------         x, cdf of a mixture of distributions.          Parameters         ----------, Sample from a mixture of multivariate distributions.      Parameters     ------- (+3 more)

### Community 199 - "Community 199"
Cohesion: 0.14
Nodes (8): Gamma, r"""         Binomial deviance residuals          Parameters         ----------, Helper function to trim the data so that it is in (0,inf)          Notes, Gamma exponential family distribution.      Parameters     ----------     link :, r"""         Gamma deviance residuals          Parameters         ----------, r"""         The log-likelihood function for each observation in terms of the fi, r"""         The Anscombe residuals          Parameters         ----------, r"""         Frozen Gamma distribution instance for given parameters          Pa

### Community 200 - "Community 200"
Cohesion: 0.14
Nodes (8): Log, The log transform      .. deprecated:: 0.14.0         Use Log instead.      Note, The log transform      Notes     -----     call and derivative call a private me, Log transform link function          Parameters         ----------         p : a, Inverse of log transform link function          Parameters         ----------, Derivative of log transform link function          Parameters         ----------, Second derivative of the log transform link function          Parameters, Derivative of the inverse of the log transform link function          Parameters

### Community 201 - "Community 201"
Cohesion: 0.14
Nodes (8): _check_data(), _Default, LinearConstraintValues, _maybe_convert_data(), Function to order a formulaic formula so when materialized it matches patsy., Get the model matrices or design matrices from a formula and data.          Para, Get the linear constraints from the constraints and variable names.          Par, Check if data is a DataFrame and issue a warning if it is not.      Parameters

### Community 202 - "Community 202"
Cohesion: 0.19
Nodes (1): GLMGamResults

### Community 203 - "Community 203"
Cohesion: 0.13
Nodes (7): Class to hold results from fitting a recursive least squares model      Paramete, Estimates of regression coefficients, recursively estimated          Returns, r"""         Recursive residuals          Returns         -------         resid_, r"""         Cumulative sum of standardized recursive residuals statistics, r"""         Cumulative sum of squares of standardized recursive residuals, r"""         Plot the recursively estimated coefficients on a given variable, RecursiveLSResults

### Community 204 - "Community 204"
Cohesion: 0.13
Nodes (4): Class to contain RLM results      Attributes     ----------     bcov_scaled : nd, Summarize the fitted model          Parameters         ----------         yname, Experimental summary function for regression results          Parameters, RLMResults

### Community 205 - "Community 205"
Cohesion: 0.13
Nodes (13): _atleast_1d(), _atleast_2d(), concat(), constrain_stationary_univariate(), copy_index_matrix(), Statespace Tools  Author: Chad Fulton License: Simplified-BSD, Copy the rows or columns of a time-varying matrix where all non-index     values, Version of `np.atleast_1d`, copied from     https://github.com/numpy/numpy/blob/ (+5 more)

### Community 206 - "Community 206"
Cohesion: 0.16
Nodes (8): _Bunch, Assess independence for nominal factors          Assessment of independence betw, Assess independence between two ordinal variables          This is the 'linear b, Methods for analyzing a square contingency table      Parameters     ----------, Test for symmetry of a joint distribution          This procedure tests the null, Compare row and column marginal distributions          Parameters         ------, Produce a summary of the analysis          Parameters         ----------, SquareTable

### Community 207 - "Community 207"
Cohesion: 0.14
Nodes (13): corr_normal_scores(), corr_quadrant(), corr_rank(), Author: Josef Perktold License: BSD-3, # TODO: streamline calculation and save to linear interpolation, maybe, Spearman rank correlation      Simplified version of scipy.stats.spearmanr., Gaussian rank (normal scores) correlation      Status: unverified, subject to ch, # TODO: a full version should be same as scipy spearmanr (+5 more)

### Community 208 - "Community 208"
Cohesion: 0.17
Nodes (8): OaxacaBlinder, OaxacaResults, A helper function to calculate the variance/std          Used to keep the decomp, Calculates the three-fold Oaxaca Blinder Decompositions          Parameters, Calculates the two-fold or pooled Oaxaca Blinder Decompositions          Paramet, This class summarizes the fit of the OaxacaBlinder model      Parameters     ---, Print a summary table with the Oaxaca-Blinder effects, Class to perform Oaxaca-Blinder Decomposition      Parameters     ----------

### Community 209 - "Community 209"
Cohesion: 0.13
Nodes (9): CompareMeans, test of equivalence for two independent samples, base on t-test          Paramet, test of (non-)equivalence for two independent samples      TOST: two one-sided t, return an instance of CompareMeans with self and other          Parameters, class for two sample comparison      The tests and the confidence interval work, assume d1, d2 hold the relevant attributes, construct a CompareMeans object from data          Parameters         ----------, standard deviation of the mean difference assuming pooled variance (+1 more)

### Community 210 - "Community 210"
Cohesion: 0.15
Nodes (8): L2ConstraintsPenalty, L2Univariate, A collection of smooth penalty functions.  Penalties on vectors take a vector ar, The L2 (ridge) penalty applied to each parameter., # TODO: `and np.size(params) > 1` is hack for llnull, need better solution, # TODO: weights are missing, # TODO: `and np.size(params) > 1` is hack for llnull, need better solution, Convenience class of ConstraintsPenalty with L2 penalization

### Community 211 - "Community 211"
Cohesion: 0.19
Nodes (7): Copula, ExtremeValueCopula, Evaluate pdf of bivariate extreme value copula.          Parameters         ----, Evaluate log-pdf of bivariate extreme value copula.          Parameters, conditional distribution          not yet implemented          C2|1(u2|u1) := ∂C, Extreme value copula constructed from Pickand's dependence function.      Curren, Evaluate cdf of bivariate extreme value copula.          Parameters         ----

### Community 212 - "Community 212"
Cohesion: 0.15
Nodes (8): CLogLog, Derivative of C-Log-Log transform link function          Parameters         ----, Second derivative of the C-Log-Log ink function          Parameters         ----, Derivative of the inverse of the C-Log-Log transform link function          Para, The CLogLog transform link function.      .. deprecated:: 0.14.0         Use CLo, The complementary log-log transform      CLogLog inherits from Logit in order to, C-Log-Log transform link function          Parameters         ----------, Inverse of C-Log-Log transform link function           Parameters         ------

### Community 213 - "Community 213"
Cohesion: 0.14
Nodes (7): NegativeBinomial, The negative binomial link function      Parameters     ----------     alpha : f, Negative Binomial transform link function          Parameters         ----------, Inverse of the negative binomial transform          Parameters         ---------, Derivative of the negative binomial transform          Parameters         ------, Second derivative of the negative binomial link function.          Parameters, Derivative of the inverse of the negative binomial transform          Parameters

### Community 214 - "Community 214"
Cohesion: 0.15
Nodes (13): convolution_filter(), fftconvolve3(), fftconvolveinv(), miso_lfilter(), _pad_nans(), Linear Filters for time series analysis and testing   TODO: * check common seque, Convolve two N-dimensional arrays using FFT. See convolve      Parameters     --, Autoregressive, or recursive, filtering.      Parameters     ----------     x : (+5 more)

### Community 215 - "Community 215"
Cohesion: 0.22
Nodes (7): Cubic Spline single smooth component      Cubic splines as described in Wood's b, Rescale x according to `transform_data_method`          Parameters         -----, Cubic-spline reproducing-kernel function evaluated at x and z., Build the cubic-spline design matrix at x, using self.knots          Parameters, Penalty matrix based on `_rk` evaluated at pairs of knots., Create the spline basis for new observations          Parameters         -------, UnivariateCubicSplines

### Community 216 - "Community 216"
Cohesion: 0.20
Nodes (9): GLS, atleast_2dcols(), GLSHet, GLSHet2, Created on Tue Dec 20 20:24:20 2011  Author: Josef Perktold License: BSD-3, Perform an iterative two-step procedure to estimate a WLS model          The mod, WLS with heteroscedasticity that depends on explanatory variables      Notes, A regression model with an estimated heteroscedasticity.      A subclass of WLS, (+1 more)

### Community 217 - "Community 217"
Cohesion: 0.21
Nodes (13): beanplot(), _jitter_envelope(), Variations on boxplots, Draw a single violin onto `ax` at position `pos`, Set ticks and labels on horizontal axis, Make a violin plot of each dataset in the `data` sequence      A violin plot is, Bean plot of each dataset in a sequence      A bean plot is a combination of a `, Determine envelope for jitter markers (+5 more)

### Community 218 - "Community 218"
Cohesion: 0.16
Nodes (13): annotate_axes(), create_mpl_ax(), create_mpl_fig(), get_data_names(), _import_mpl(), maybe_name_or_idx(), Helper functions for graphics with Matplotlib, Return the name(s) and integer location(s) of column(s) in a design matrix (+5 more)

### Community 219 - "Community 219"
Cohesion: 0.18
Nodes (7): CanCorr, CanCorrTestResults, Canonical correlation analysis  author: Yichuan Liu, Approximate F test          Perform multivariate statistical tests of the hypoth, Canonical correlation analysis using singular value decomposition      For matri, Canonical correlation results class      Parameters     ----------     stats : D, Fit the model          A ValueError is raised if there are singular values small

### Community 220 - "Community 220"
Cohesion: 0.14
Nodes (11): cov_tyler(), CovTylerResult, median(), Robust standardization of random variable, Reweighting step, trims data and computes Pearson covariance      Parameters, Rescale covariance to be consistent with normal distribution      This matches m, Result of :func:`cov_tyler`.      Parameters     ----------     cov : ndarray, Tyler's M-estimator for normalized covariance (scatter)      The underlying (pop (+3 more)

### Community 221 - "Community 221"
Cohesion: 0.19
Nodes (7): MQuantileNorm, M-quantiles objective function based on a base norm      This norm has the same, The robust criterion function for MQuantileNorm          Parameters         ----, The psi function for MQuantileNorm estimator          The analytic derivative of, MQuantileNorm weighting function for the IRLS algorithm          The psi functio, The derivative of MQuantileNorm function          Parameters         ----------, Return the value of estimator rho applied to an input          Parameters

### Community 222 - "Community 222"
Cohesion: 0.14
Nodes (7): RamsayE, Ramsay's Ea for M estimation      Parameters     ----------     a : float, optio, Set and change the tuning parameter of the Norm          Parameters         ----, r"""         The robust criterion function for Ramsay's Ea          Parameters, r"""         The psi function for Ramsay's Ea estimator          The analytic de, r"""         Ramsay's Ea weighting function for the IRLS algorithm          The, The derivative of Ramsay's Ea psi function          Parameters         ---------

### Community 223 - "Community 223"
Cohesion: 0.14
Nodes (7): Robust norm based on t distribution      Rho is a rescaled version of the t-logl, Set and change the tuning parameter of the Norm          Parameters         ----, The rho function of the StudentT norm          Parameters         ----------, The psi function of the StudentT norm          The analytic derivative of rho., The weighting function for the IRLS algorithm of the StudentT norm          The, The derivative of the psi function of the StudentT norm          Parameters, StudentT

### Community 224 - "Community 224"
Cohesion: 0.14
Nodes (13): effectsize_oneway(), f2_to_wellek(), fstat_to_wellek(), power_equivalence_oneway(), Created on Wed Mar 18 10:33:38 2020  Author: Josef Perktold License: BSD-3, Power of oneway equivalence test      Parameters     ----------     f2_alt : flo, # TODO: reuse general case with weights, Effect size corresponding to Cohen's f = nc / nobs for oneway anova      This co (+5 more)

### Community 225 - "Community 225"
Cohesion: 0.18
Nodes (10): _calc_approx_inv_cov(), _calc_nodewise_row(), _calc_nodewise_weight(), Class for estimating regularized inverse covariance with nodewise regression, Estimate the regularized inverse covariance using nodewise regression          P, Returns the approximate inverse covariance matrix          Returns         -----, Calculate the nodewise_weight value for the idxth variable      Used to estimate, Calculate the nodewise_row values for the idxth variable      Used to estimate a (+2 more)

### Community 226 - "Community 226"
Cohesion: 0.14
Nodes (13): Tests and descriptive statistics with weights  Created on 2010-09-18  Author: jo, # TODO: why squeeze?, # TODO: remove tuple return, use same as for function tost_ind, # TODO: remove tuple return, use same as for function tost_ind, ttest independent sample      Convenience function that uses the classes and thr, # TODO: this should delegate to CompareMeans like ttest_ind, # TODO: add asymmetric, # TODO: check direction with R, smaller=less, larger=greater (+5 more)

### Community 227 - "Community 227"
Cohesion: 0.19
Nodes (7): LeybourneMcCabeStationarity, Class wrapper for Leybourne-McCabe stationarity test, Empirical method for Leybourne-McCabe auto AR lag detection         Set number o, Asymptotic critical values for the two different models specified         for th, Leybourne-McCabe stationarity test          The Leybourne-McCabe test can be use, Linear interpolation for Leybourne p-values and critical values          Paramet, Two-stage least squares approach for estimating ARIMA(p, 1, 1)         parameter

### Community 228 - "Community 228"
Cohesion: 0.14
Nodes (8): Group, Represent grouping labels and derived encodings      Parameters     ----------, Return the number of observations in each group          Returns         -------, Return string labels for each unique group          Returns         -------, Return a dummy/indicator matrix for the groups          Parameters         -----, Return a new Group formed from the intersection with another grouping          P, Sum `x` within each group          Parameters         ----------         x : arr, Demean `x` by subtracting the group means          Parameters         ----------

### Community 229 - "Community 229"
Cohesion: 0.14
Nodes (13): dummy_sparse(), group_sums(), group_sums_dummy(), Tools for working with groups  This provides several functions to work with grou, Sum ``x`` within integer groups      Parameters     ----------     x : array_lik, Sum by groups given group dummy variable      Parameters     ----------     x :, # TODO: See if this can be entirely replaced by Grouping.dummy_sparse;, Create a sparse indicator from a group array with integer labels      Parameters (+5 more)

### Community 230 - "Community 230"
Cohesion: 0.21
Nodes (13): bds(), correlation_sum(), correlation_sums(), distance_indicators(), BDS test for IID time series  References ----------  Broock, W. A., J. A. Schein, Calculate all correlation sums for embedding dimensions 1:max_dim      Parameter, Calculate the variance of a BDS effect      Parameters     ----------     indica, BDS Test Statistic for Independence of a Time Series      Parameters     ------- (+5 more)

### Community 231 - "Community 231"
Cohesion: 0.18
Nodes (10): _asarray_2d_null_rows(), FormulaicData, handle_data(), handle_data_class_factory(), handle_missing(), Base tools for handling various kinds of data structures, attaching metadata to, # NOTE: there may be a more performant way to do this, Makes sure input is an array and is 2d. Makes sure output is 2d. True     indica (+2 more)

### Community 232 - "Community 232"
Cohesion: 0.17
Nodes (12): _f_ieqcons(), fit_l1_slsqp(), _fprime(), _fprime_ieqcons(), _get_disp_slsqp(), _objective_func(), Holds files for l1 regularization of LikelihoodModel, using scipy.optimize.slsqp, Solve the l1 regularized problem using scipy.optimize.fmin_slsqp().      Specifi (+4 more)

### Community 233 - "Community 233"
Cohesion: 0.19
Nodes (7): BoxCox, Computes an estimate for the lambda parameter in the Box-Cox         transformat, Performs a Box-Cox transformation on the data array x. If lmbda is None,, Computes lambda using guerrero's coefficient of variation. If no         seasona, Taken from the Stata manual on Box-Cox regressions, where this is the         sp, Back-transforms the Box-Cox transformed data array, by means of the         indi, Mixin class to allow for a Box-Cox transformation.

### Community 234 - "Community 234"
Cohesion: 0.15
Nodes (7): CopulaDistribution, Which Archimedean is Best? Extreme Value copulas formulas are based on Genest 20, CDF of copula distribution.          Parameters         ----------         y : a, PDF of copula distribution.          Parameters         ----------         y : a, Log-pdf of copula distribution.          Parameters         ----------         y, Multivariate copula distribution      Parameters     ----------     copula : :cl, Draw `n` in the half-open interval ``[0, 1)``.          Sample the joint distrib

### Community 235 - "Community 235"
Cohesion: 0.23
Nodes (3): DiscretizedCount, Count distribution based on discretized distribution      Parameters     -------, Generate random variates.          Parameters         ----------         *args

### Community 236 - "Community 236"
Cohesion: 0.18
Nodes (10): bghfactor(), chi2_pdf(), chi_logpdf(), funbgh(), multivariate_t_rvs(), mvstdtprob(), Multivariate Distribution  Probability of a multivariate t distribution  Now als, generate random variables of multivariate t distribution      Parameters     --- (+2 more)

### Community 237 - "Community 237"
Cohesion: 0.15
Nodes (7): MVNormal, Class for Multivariate Normal Distribution      uses Cholesky decomposition of c, random variable          Parameters         ----------         size : int or tup, logarithm of probability density function          Parameters         ----------, cumulative distribution function          Parameters         ----------, return distribution of an affine transform          for full rank scale_matrix o, r"""return conditional distribution          indices are the variables to keep,

### Community 238 - "Community 238"
Cohesion: 0.15
Nodes (7): MVT, initialize instance          Parameters         ----------         mean : array_, random variables with Student T distribution          Parameters         -------, logarithm of probability density function          Parameters         ----------, cumulative distribution function          Parameters         ----------, covariance matrix          The covariance matrix for the t distribution does not, return distribution of a full rank affine transform          for full rank scale

### Community 239 - "Community 239"
Cohesion: 0.18
Nodes (8): DescStat(), DescStatMV, Empirical likelihood inference on descriptive statistics  This module conducts h, A class for conducting inference on multivariate means and correlation      Para, Returns -2 x log likelihood and the p-value         for a multivariate hypothesi, Creates a confidence region plot for the mean of bivariate data          Paramet, Returns the confidence intervals for the correlation coefficient          Parame, Return an instance to conduct inference on descriptive statistics      Uses empi

### Community 240 - "Community 240"
Cohesion: 0.15
Nodes (7): Binomial, r"""         The log-likelihood function for each observation in terms of the fi, r"""         The Anscombe residuals          Parameters         ----------, r"""         Frozen Binomial distribution instance for given parameters, Binomial exponential family distribution.      Parameters     ----------     lin, r"""         The starting values for the IRLS algorithm for the Binomial family., Initialize the response variable.          Parameters         ----------

### Community 241 - "Community 241"
Cohesion: 0.15
Nodes (7): PolynomialSmoother, Additive polynomial components for GAM      Parameters     ----------     x : ar, Base class for single smooth component      Parameters     ----------     x : nd, Polynomial single smooth component      Parameters     ----------     x : ndarra, Given a vector x returns poly=(1, x, x^2, ..., x^degree)         and its first a, UnivariateGamSmoother, UnivariatePolynomialSmoother

### Community 242 - "Community 242"
Cohesion: 0.15
Nodes (7): Return the value of psi(z) / z          Abstract method:          psi(z) / z, Derivative of psi.  Used to obtain robust covariance matrix          See statsmo, Return the value of estimator rho applied to an input          Parameters, The parent class for the norms used for robust regression      Lays out the meth, The robust criterion estimator function          Abstract method:          -2 lo, Derivative of rho.  Sometimes referred to as the influence function          Abs, RobustNorm

### Community 243 - "Community 243"
Cohesion: 0.17
Nodes (12): PoissonTestResult, _power_equivalence_het_v0(), Test for ratio of Poisson intensities in two independent samples  Author: Josef, # TODO: do I need these? return_results ?, # TODO: avoid possible circular import, check if needed, Power for equivalence test      Parameters     ----------     es_low : float, # TODO: avoid possible circular import, check if needed, # TODO: avoid possible circular import, check if needed (+4 more)

### Community 244 - "Community 244"
Cohesion: 0.22
Nodes (12): check_movorder(), expandarr(), movmean(), movmoment(), movorder(), movvar(), using scipy signal and numpy correlate to calculate some time series statistics, graphical test for movorder (+4 more)

### Community 245 - "Community 245"
Cohesion: 0.18
Nodes (6): hypothesis_test_table(), normality_summary(), _pfixed(), pprint_matrix(), # TODO: do we want individual statistics or should users just, # TODO: change when we allow coef restrictions

### Community 246 - "Community 246"
Cohesion: 0.21
Nodes (11): date_parser(), date_range_str(), dates_from_range(), dates_from_str(), _is_leap(), Tools for working with dates, Returns a list of abbreviated date strings      Parameters     ----------     st, Turns a sequence of date strings and returns a list of datetime      Parameters (+3 more)

### Community 247 - "Community 247"
Cohesion: 0.18
Nodes (11): fit_l1_cvxopt_cp(), _fprime(), _get_G(), _hessian_wrapper(), _objective_func(), Holds files for l1 regularization of LikelihoodModel, using cvxopt., Solve the l1 regularized problem using cvxopt.solvers.cp      Specifically:  We, The regularized objective function (+3 more)

### Community 248 - "Community 248"
Cohesion: 0.17
Nodes (1): TransfClayton

### Community 249 - "Community 249"
Cohesion: 0.17
Nodes (9): bivariate_normal(), expect_mc(), expect_mc_bounds(), Multivariate Normal and t distributions    Created on Sat May 28 15:38:23 2011, calculate expected value of function by Monte Carlo integration      Parameters, calculate expected value of function by Monte Carlo integration      Parameters, Bivariate Gaussian distribution for equal shape *X*, *Y*.      See `bivariate no, # TODO: make integration limits more flexible (+1 more)

### Community 250 - "Community 250"
Cohesion: 0.17
Nodes (7): Returns - 2 x log-likelihood and the p-value for the joint         hypothesis te, Returns -2 x log-likelihood ratio and  p-value for the         correlation coeff, Calculate the difference between the log likelihood ratio at kurt         and a, Emit the ``return_weights`` variable-arity FutureWarning for ``name``., Calculate the difference between the log likelihood ratio at corr         and a, Returns -2 x log-likelihood and the p-value for the hypothesized         kurtosi, _warn_return_weights()

### Community 252 - "Community 252"
Cohesion: 0.18
Nodes (6): EmptyContextManager, get_file_obj(), Handle file opening for read/write, When entering, return the embedded object, Light wrapper to handle strings, path objects and let files (anything     else), This class is needed to allow a file-like object to be used as a     context man

### Community 253 - "Community 253"
Cohesion: 0.18
Nodes (9): invertibleroots(), MLEGLS, mvn_loglike(), Return an invertible MA polynomial and whether the input was invertible      Par, ARMA model with exact loglikelihood for short time series      Inverts (nobs, no, Get autocovariance matrix from ARMA regression parameter          AR parameters, Loglikelihood evaluated at params          Parameters         ----------, Fit the model, re-fitting with invertible MA starting values if needed (+1 more)

### Community 254 - "Community 254"
Cohesion: 0.18
Nodes (6): KernelCensoredReg, Nonparametric censored regression      Calculates the conditional mean ``E[y|X]`, Provide something sane to print, Local linear estimator of g(x) in the regression ``y = g(x) + e``          Param, r"""         The cross-validation function with leave-one-out         estimator, Returns the mean and marginal effects at the `data_predict` points          Para

### Community 255 - "Community 255"
Cohesion: 0.17
Nodes (12): confint_poisson(), confint_poisson_2indep(), confint_quantile_poisson(), _invert_test_confint(), _invert_test_confint_2indep(), Confidence interval for ratio or difference of 2 indep poisson rates      Parame, Confidence interval for a Poisson mean or rate      The function is vectorized f, Tolerance interval for a poisson observation      Parameters     ---------- (+4 more)

### Community 256 - "Community 256"
Cohesion: 0.17
Nodes (8): degrees of freedom of Satterthwaite for unequal variance, ttest for the null hypothesis of identical means          this should also be th, confidence interval for the difference in means          Parameters         ----, two-sided confidence interval for weighted mean of data          If the data is, generic ttest based on summary statistic      The test statistic is :         ts, generic t-confint based on summary statistic      Parameters     ----------, _tconfint_generic(), _tstat_generic()

### Community 257 - "Community 257"
Cohesion: 0.21
Nodes (11): discrepancy(), halton(), n_primes(), primes_from_2_to(), Low discrepancy sequence tools, Van der Corput sequence      Pseudo-random number generator based on a b-adic ex, Halton sequence      Pseudo-random number generator that generalize the Van der, Discrepancy      Compute the centered discrepancy on a given sample.     It is a (+3 more)

### Community 258 - "Community 258"
Cohesion: 0.18
Nodes (6): Fourier transform of AR polynomial, zero-padded at end to n          Parameters, Fourier transform of MA polynomial, zero-padded at end to n          Parameters, power spectral density using fftshift          currently returns two-sided accor, filter a timeseries with the ARMA filter          padding with zero is missing,, filter a time series using fftconvolve3 with ARMA filter          padding of x c, pad 1d array with zeros at end to have length maxlag         function that is a

### Community 259 - "Community 259"
Cohesion: 0.18
Nodes (6): CovariancePenalty, PSD, Base class for a penalty applied to a covariance matrix      Parameters     ----, Parameters         ----------         mat : square matrix             The matrix, Parameters         ----------         mat : square matrix             The matrix, A penalty that converges to +infinity as the argument matrix     approaches the

### Community 260 - "Community 260"
Cohesion: 0.25
Nodes (6): Create new Penalty instance, Compute measure for ranking exog candidates for inclusion, Screen and select variables (columns) in exog          Parameters         ------, Batched version of screen exog          This screens variables in a two step pro, Ultra-high, conditional sure independence screening      This is an adjusted ver, VariableScreening

### Community 261 - "Community 261"
Cohesion: 0.18
Nodes (2): Zero Inflated Generalized Negative Binomial distribution, zinegativebinomial_gen

### Community 262 - "Community 262"
Cohesion: 0.18
Nodes (6): MVNormal0, Class for Multivariate Normal Distribution      original full version, kept for, whiten the data by linear transformation          Parameters         ----------, random variable          Parameters         ----------         size : int or tup, probability density function          Parameters         ----------         x :, logarithm of probability density function          Parameters         ----------

### Community 263 - "Community 263"
Cohesion: 0.22
Nodes (6): A class representing a collection of discrete distributions      Parameters, Returns a random sample from the discrete distribution          A vector is retu, Returns a vector containing the mean values of the discrete         distribution, Returns a vector containing the variances of the discrete         distributions, Returns a vector containing the standard deviations of the         discrete dist, rv_discrete_float

### Community 264 - "Community 264"
Cohesion: 0.18
Nodes (6): DescStatUV, Returns the confidence interval for skewness          Parameters         -------, Returns the confidence interval for kurtosis          Parameters         -------, A class to compute confidence intervals and hypothesis tests involving     mean,, Returns the confidence interval for the mean          Parameters         -------, Returns the confidence interval for the variance          Parameters         ---

### Community 265 - "Community 265"
Cohesion: 0.18
Nodes (6): Gaussian, Gaussian exponential family distribution.      Parameters     ----------     lin, r"""         Gaussian deviance residuals          Parameters         ----------, r"""         The log-likelihood function for each observation in terms of the fi, r"""         The Anscombe residuals          Parameters         ----------, r"""         Frozen Gaussian distribution instance for given parameters

### Community 266 - "Community 266"
Cohesion: 0.18
Nodes (6): InverseGaussian, InverseGaussian exponential family.      Parameters     ----------     link : a, r"""         Inverse Gaussian deviance residuals          Parameters         ---, r"""         The log-likelihood function for each observation in terms of the fi, r"""         The Anscombe residuals          Parameters         ----------, r"""         Frozen Inverse Gaussian distribution instance for given parameters

### Community 267 - "Community 267"
Cohesion: 0.18
Nodes (6): NegativeBinomial, r"""     Negative Binomial exponential family (corresponds to NB2).      Paramet, r"""         Negative Binomial deviance residuals          Parameters         --, r"""         The log-likelihood function for each observation in terms of the fi, r"""         The Anscombe residuals          Parameters         ----------, r"""         Frozen NegativeBinomial distribution instance for given parameters

### Community 268 - "Community 268"
Cohesion: 0.18
Nodes (6): Poisson, Poisson exponential family.      Parameters     ----------     link : a link ins, r"""         Poisson deviance residuals          Parameters         ----------, r"""         The log-likelihood function for each observation in terms of the fi, r"""         The Anscombe residuals          Parameters         ----------, r"""         Frozen Poisson distribution instance for given parameters

### Community 269 - "Community 269"
Cohesion: 0.18
Nodes (5): Get the term names from a model specification or DataFrame.          Parameters, Returns a list of column names from a model specification or DataFrame., Get a dictionary containing the term names and their location in the formula., Get the model specification attached to a DataFrame.          Parameters, Gets a string representation of the model specification.          Parameters

### Community 270 - "Community 270"
Cohesion: 0.33
Nodes (8): _alpha(), density_otherwise(), kappa(), logW(), _logWj(), Private experimental module for miscellaneous Tweedie functions.  References ---, _sumw(), _theta()

### Community 271 - "Community 271"
Cohesion: 0.20
Nodes (10): arma_innovations(), arma_loglike(), arma_loglikeobs(), arma_score(), arma_scoreobs(), Compute the log-likelihood of the given data assuming an ARMA process      Param, Compute the log-likelihood for each observation assuming an ARMA process      Pa, Compute innovations using a given ARMA process      Parameters     ---------- (+2 more)

### Community 272 - "Community 272"
Cohesion: 0.18
Nodes (10): getpoly(), mvn_loglike_chol(), mvn_loglike_sum(), mvn_nloglike_obs(), Multivariate Normal Model with full covariance matrix  toeplitz structure is not, Negative loglikelihood of multivariate normal for each observation      Assumes, Return the AR and MA lag polynomials for a model instance      Parameters     --, Loglikelihood of multivariate normal, concentrated version      Copied from GLS (+2 more)

### Community 273 - "Community 273"
Cohesion: 0.18
Nodes (5): Estimate factor model parameters.          Parameters         ----------, Extract factors using the iterative principal axis method          Parameters, Estimate Factor model using Maximum Likelihood          Parameters         -----, Estimate Factor model using EM algorithm          Parameters         ----------, Rotate loadings for MLE          Parameters         ----------         load : nd

### Community 274 - "Community 274"
Cohesion: 0.24
Nodes (10): bw_normal_reference(), bw_scott(), bw_silverman(), Returns the smaller of std(X, ddof=1) or normalized IQR(X) over axis 0      Refe, Selects bandwidth for a selection rule bw      This is a wrapper around existing, Scott's Rule of Thumb      Parameters     ----------     x : array_like, Silverman's Rule of Thumb      Parameters     ----------     x : array_like, Plug-in bandwidth with kernel specific constant based on normal reference      T (+2 more)

### Community 275 - "Community 275"
Cohesion: 0.18
Nodes (10): counts(), forrt(), kdesum(), Computes the sum of pairwise differences of x along the given axis      Paramete, Inverse of forrt, equivalent to Munro (1976) REVRT routine      Parameters     -, FFT of Gaussian kernel following to Silverman AS 176      Parameters     -------, RFFT with order like Munro (1976) FORTT routine      Parameters     ----------, Counts the number of elements of x that fall within the grid points v      Param (+2 more)

### Community 276 - "Community 276"
Cohesion: 0.20
Nodes (6): NdKernel, This simply returns the value of the kernel function at x          Does the same, Generic N-dimensional kernel      Can be constructed from either     a) a list o, Getter for kernel bandwidth, H, Setter for kernel bandwidth, H, returns the kernel weight for the independent multivariate kernel

### Community 277 - "Community 277"
Cohesion: 0.31
Nodes (1): RollingWLS

### Community 278 - "Community 278"
Cohesion: 0.18
Nodes (6): LeastSquares, Least squares rho for M-estimation and its derived functions      See Also     -, r"""         The robust criterion function for the least squares estimator, r"""         The psi function for the least squares estimator          The analy, r"""         The least squares estimator weighting function for the IRLS algorit, r"""         The derivative of the least squares psi function          Parameter

### Community 279 - "Community 279"
Cohesion: 0.22
Nodes (5): MatrixWrapper, State Space Representation  Author: Chad Fulton License: Simplified-BSD, # TODO: we could technically allow k_posdef > k_states, but the Cython, # TODO: Need to add a check for ndim, and if the matrix has, # TODO: move this function to tools?

### Community 280 - "Community 280"
Cohesion: 0.22
Nodes (9): cochrans_q(), CochransQResult, _make_df_square(), mcnemar(), Methods for analyzing two-way contingency tables (i.e., frequency tables for obs, McNemar test of homogeneity      Parameters     ----------     table : array_lik, Result of :func:`cochrans_q`.      Parameters     ----------     statistic : flo, Cochran's Q test for identical binomial proportions      Parameters     -------- (+1 more)

### Community 281 - "Community 281"
Cohesion: 0.20
Nodes (10): _power_equivalence_het(), power_equivalence_neginb_2indep(), power_equivalence_poisson_2indep(), PowerEquivalenceResult, Result of :func:`power_equivalence_poisson_2indep` and     :func:`power_equivale, Power of equivalence test of ratio of 2 independent poisson rates      Parameter, Power for equivalence test      Parameters     ----------     es_low : float, Variance based on constrained cmle, for score test version      For ratio compar (+2 more)

### Community 282 - "Community 282"
Cohesion: 0.20
Nodes (9): weighted mean of data, test for mean based on normal distribution, one or two samples      In the case, confidence interval based on normal distribution z-test      Parameters     ----, Equivalence test based on normal distribution      Parameters     ----------, variance with default degrees of freedom correction, variance without degrees of freedom correction          used for statistical tes, zconfint(), ztest() (+1 more)

### Community 283 - "Community 283"
Cohesion: 0.20
Nodes (4): Confidence interval construction for the predicted mean          This is current, Summary frame of mean, variance and confidence interval          Parameters, The variance of the predicted mean, The standard deviation of the predicted mean

### Community 284 - "Community 284"
Cohesion: 0.20
Nodes (4): check_global_randomstate_usage(), close_figures(), Fixture that closes all figures after a test function has completed      Returns, Ensure that the singleton RandomState is not modified      Notes     -----     U

### Community 285 - "Community 285"
Cohesion: 0.24
Nodes (8): _debye(), _debyem1_expansion(), Created on Fri Jan 29 19:19:45 2021  Author: Josef Perktold License: BSD-3, # TODO: how to we handle non-tuple args? two we allow single values?, Debye function minus 1, Taylor series approximation around zero      function is, Kendall's tau for Frank Copula      This uses Taylor series expansion for theta, tau_frank(), _tau_frank_expansion()

### Community 286 - "Community 286"
Cohesion: 0.20
Nodes (1): TransfGumbel

### Community 287 - "Community 287"
Cohesion: 0.20
Nodes (2): Zero Inflated Poisson distribution, zipoisson_gen

### Community 288 - "Community 288"
Cohesion: 0.20
Nodes (5): Returns a covariance matrix for the proportional hazards model         regressio, Fit a proportional hazards regression model          Parameters         --------, Returns the Hessian matrix of the log partial likelihood         function evalua, Returns the Hessian of the log partial likelihood evaluated at         `params`,, Returns the Hessian matrix of the partial log-likelihood         evaluated at `p

### Community 289 - "Community 289"
Cohesion: 0.20
Nodes (5): AdditiveGamSmoother, CubicSplines, Base class for additive smooth components      Parameters     ----------     x :, Create the spline basis for new observations          The main use of this state, additive smooth components using cubic splines as in Wood 2006      Note, these

### Community 290 - "Community 290"
Cohesion: 0.27
Nodes (3): diagonal of hat matrix          diag(X' xpxi X)          where xpxi = (X'X + sig, a measure for the fraction of the data in the estimation result          The sha, TheilRegressionResults

### Community 291 - "Community 291"
Cohesion: 0.20
Nodes (5): Create summary table showing revisions to the previous results' data          Pa, Create summary table showing news from new data since previous results, Create summary tables describing news and impacts          Parameters         --, Create summary table with detailed impacts from news; by date, variable, Create summary table with detailed impacts; by date, variable          Parameter

### Community 292 - "Community 292"
Cohesion: 0.24
Nodes (4): _KalmanSmoother, Kalman Smoother  Author: Chad Fulton License: Simplified-BSD, Seek the smoother to a specific point in time          Parameters         ------, Pure Python Kalman smoother      Parameters     ----------     model : Represent

### Community 293 - "Community 293"
Cohesion: 0.24
Nodes (9): cancorr(), cc_ranktest(), cc_stats(), partial_project(), Tools for multivariate analysis  Author : Josef Perktold License : BSD-3  TODO:, Rank tests based on smallest canonical correlation coefficients      Anderson ca, Helper function to get linear projection or partialling out of variables      en, MANOVA statistics based on canonical correlation coefficient      Calculates Pil (+1 more)

### Community 294 - "Community 294"
Cohesion: 0.20
Nodes (10): confint_effectsize_oneway(), confint_noncentrality(), ConfintEffectSizeResult, convert_effectsize_fsqu(), EffectSizeFsquResult, Result of :func:`convert_effectsize_fsqu`.      Parameters     ----------     f2, Convert squared effect sizes in f family      f2 is signal to noise ratio, var_e, Confidence interval for noncentrality parameter in F-test      This does not yet (+2 more)

### Community 295 - "Community 295"
Cohesion: 0.20
Nodes (10): equivalence_oneway_generic(), EquivalenceOnewayResult, _power_equivalence_oneway_emp(), Empirical power of oneway equivalence test      This only returns post-hoc, empi, Result of :func:`simulate_power_equivalence_oneway`.      Parameters     -------, Simulate Power for oneway equivalence test (Wellek's Anova)      This function i, Result of :func:`equivalence_oneway_generic` and :func:`equivalence_oneway`., Equivalence test for oneway anova (Wellek and extensions)      This is an helper (+2 more)

### Community 296 - "Community 296"
Cohesion: 0.20
Nodes (10): etest_poisson_2indep(), PoissonTest2indepResult, E-test for ratio of two sample Poisson rates      Rates are defined as expected, Result of :func:`tost_poisson_2indep`.      Parameters     ----------     statis, Equivalence test based on two one-sided `test_poisson_2indep`      This assumes, Result of :func:`test_poisson_2indep`.      Parameters     ----------     statis, Test for comparing two sample Poisson intensity rates      Rates are defined as, test_poisson_2indep() (+2 more)

### Community 297 - "Community 297"
Cohesion: 0.24
Nodes (9): Anova k-sample comparison without and with trimming  Created on Sun Jun 09 23:51, # TODO: add pandas handling, maybe not if this stays internal, Slice off a proportion of items from both ends of an array      Slices off the p, # TODO: this will not work if there is processing of meta-information, Transform data for variance comparison for Levene type tests      Parameters, Return mean of array after trimming observations from both tails      If `propor, scale_transform(), trim_mean() (+1 more)

### Community 298 - "Community 298"
Cohesion: 0.20
Nodes (9): logdet_symm(), matrix_sqrt(), Linear algebra solvers and other helpers., Return log(det(m)) asserting positive definiteness of m      Parameters     ----, Matrix square root for symmetric matrices      Usage is for decomposing a covari, Solve a linear system for a Toeplitz correlation matrix      A Toeplitz correlat, Use QR to get transformation matrix to impose constraint      Parameters     ---, stationary_solve() (+1 more)

### Community 299 - "Community 299"
Cohesion: 0.20
Nodes (4): Abstract Base Class for all Time Trend Deterministic Terms, Flag indicating that a constant is included, Order of the time trend, TimeTrendDeterministicTerm

### Community 300 - "Community 300"
Cohesion: 0.22
Nodes (5): ConstraintsPenalty, Penalty applied to linear transformation of parameters      Parameters     -----, Evaluate penalty function at params          Parameters         ----------, First derivative of penalty function w.r.t. params          Parameters         -, Second derivative of penalty function w.r.t. params          Parameters

### Community 301 - "Community 301"
Cohesion: 0.25
Nodes (8): ensure_patsy_compat(), get_all_sorted_knots(), monkey_patch_cat_dtype(), Apply the patsy categorical dtype compatibility patch, if possible, Patch patsy to use a version-compatible categorical dtype check, Get all knots locations with lower and upper exterior knots included      If nee, Check whether a dtype is a pandas categorical dtype across versions, _safe_is_pandas_categorical_dtype()

### Community 302 - "Community 302"
Cohesion: 0.22
Nodes (1): TransfFrank

### Community 303 - "Community 303"
Cohesion: 0.22
Nodes (4): _check_at_is_all(), Returns a DataFrame summarizing the marginal effects.          Parameters, Returns the confidence intervals of the marginal effects          Parameters, Returns a summary table for marginal effects          Parameters         -------

### Community 304 - "Community 304"
Cohesion: 0.22
Nodes (3): # TODO: need cdf, and rvs, Zero Inflated Generalized Poisson distribution, zigeneralizedpoisson_gen

### Community 305 - "Community 305"
Cohesion: 0.28
Nodes (2): BivariateNormal, Kullback-Leibler divergence between this and another distribution          int f

### Community 306 - "Community 306"
Cohesion: 0.22
Nodes (5): Tweedie family.      Parameters     ----------     link : a link instance, optio, r"""         Tweedie deviance residuals          Parameters         ----------, r"""         The log-likelihood function for each observation in terms of the fi, r"""         The Anscombe residuals          Parameters         ----------, Tweedie

### Community 307 - "Community 307"
Cohesion: 0.22
Nodes (6): d_gaussian(), Gaussian, Gaussian Kernel for continuous variables      Parameters     ----------     h :, Calculates the derivative of the Gaussian kernel      Parameters     ----------, Gaussian (Normal) Kernel      K(u) = 1 / (sqrt(2*pi)) exp(-0.5 u**2), Returns the kernel smoothing estimate for point x based on x-values         xs a

### Community 308 - "Community 308"
Cohesion: 0.22
Nodes (6): normal_power(), NormalIndPower, Statistical Power calculations for z-test for two independent samples      curre, Calculate the power of a z-test for two independent sample          Parameters, Solve for any one parameter of the power of a two sample z-test          for z-t, Calculate power of a normal distributed test statistic      Parameters     -----

### Community 309 - "Community 309"
Cohesion: 0.22
Nodes (5): Created on Tue May 27 13:23:24 2014  Author: Josef Perktold License: BSD-3, Class to reparameterize a model for standardized exog      Parameters     ------, Standardize the data using the stored transformation, Transform parameters of the standardized model to the original model          Pa, StandardizeTransform

### Community 310 - "Community 310"
Cohesion: 0.22
Nodes (3): Fourier, r"""     Fourier series deterministic terms      Parameters     ----------     p, The period of the Fourier terms

### Community 311 - "Community 311"
Cohesion: 0.29
Nodes (4): NoWarningsChecker, pytest_warns(), Context manager that asserts no warnings are raised in its block, Shim for pytest warn compatibility      Parameters     ----------     warning :

### Community 312 - "Community 312"
Cohesion: 0.25
Nodes (3): ClaytonCopula, r"""Clayton copula.      Dependence is greater in the negative tail than in the, Generate random variates from the copula.          Parameters         ----------

### Community 313 - "Community 313"
Cohesion: 0.25
Nodes (3): GumbelCopula, r"""Gumbel copula.      Dependence is greater in the positive tail than in the n, Generate random variates from the copula.          Parameters         ----------

### Community 314 - "Community 314"
Cohesion: 0.25
Nodes (1): TransfIndep

### Community 315 - "Community 315"
Cohesion: 0.25
Nodes (3): get_u_argskwargs(), a class for non-linear monotonic transformation of a continuous random variable, Transf_gen

### Community 316 - "Community 316"
Cohesion: 0.25
Nodes (2): univariate Skew-Normal distribution of Azzalini      class follows scipy.stats.d, SkewNorm_gen

### Community 317 - "Community 317"
Cohesion: 0.32
Nodes (3): PHSurvivalTime, Represent a collection of survival times with possible         stratification an, Returns a scipy distribution object corresponding to the         distribution of

### Community 318 - "Community 318"
Cohesion: 0.29
Nodes (7): procrustes(), promax(), This file contains analytic implementations of rotation methods., r"""     Analytically performs orthogonal rotations towards a target matrix,, r"""     Performs promax rotation of the matrix :math:`A`.      This method was, r"""     Analytically solves the following Procrustes problem:      .. math::, target_rotation()

### Community 319 - "Community 319"
Cohesion: 0.29
Nodes (5): Probit, The probit (standard normal CDF) transform      .. deprecated:: 0.14.0         U, The probit (standard normal CDF) transform      Notes     -----     g(p) = scipy, Second derivative of the inverse link function          This is the derivative o, Second derivative of the link function g''(p)

### Community 320 - "Community 320"
Cohesion: 0.25
Nodes (3): pandas_wrapper_freq(), # TODO: allow use index labels, Return a new function that catches the incoming X, checks if it's pandas,     ca

### Community 321 - "Community 321"
Cohesion: 0.29
Nodes (4): PanelSample, Generate a random process with panel structure  Created on Sat Dec 17 22:15:27 2, generate endog for a random panel dataset with within correlation, data generating process for panel with within correlation      allows various wi

### Community 322 - "Community 322"
Cohesion: 0.29
Nodes (4): _MinimalWLS, Construct results          Parameters         ----------         params : ndarra, Estimate the model parameters using weighted least squares          Parameters, Minimal implementation of WLS optimized for performance      Parameters     ----

### Community 323 - "Community 323"
Cohesion: 0.25
Nodes (7): CovDetMCDResult, _get_detcov_startidx(), _orthogonalize_det(), Orthogonalize      This is a simplified version of the OGK method.     Version f, Starting sets for deterministic robust covariance estimators      These are inte, Result of :meth:`CovDetMCD.fit`.      Also used internally for the per-starting-, Compute minimum covariance determinant estimate of mean and covariance

### Community 324 - "Community 324"
Cohesion: 0.32
Nodes (7): _extrapolate_trend(), Seasonal Decomposition by Moving Averages, Seasonal decomposition using moving averages.      Parameters     ----------, Replace nan values on trend's end-points with least-squares extrapolated     val, Return means for each period in x      Parameters     ----------     x : array_l, seasonal_decompose(), seasonal_mean()

### Community 325 - "Community 325"
Cohesion: 0.25
Nodes (8): companion_matrix(), _compute_multivariate_acovf_from_coefficients(), is_invertible(), r"""     Compute multivariate autocovariances from vector autoregression coeffic, r"""     Create a companion matrix      Parameters     ----------     polynomial, r"""     Determine if a polynomial is invertible      Requires all roots of the, r"""     Solve the discrete Lyapunov equation using a bilinear transformation, solve_discrete_lyapunov()

### Community 326 - "Community 326"
Cohesion: 0.25
Nodes (8): _compute_multivariate_pacf_from_autocovariances(), _compute_multivariate_pacf_from_coefficients(), Compute multivariate partial autocorrelations from autocovariances      Paramete, r"""     Transform matrices corresponding to a stationary (or invertible) proces, Transform constrained parameters used in likelihood evaluation     to unconstrai, Transform matrices with singular values less than one to arbitrary     matrices., unconstrain_stationary_multivariate(), _unconstrain_sv_less_than_one()

### Community 327 - "Community 327"
Cohesion: 0.36
Nodes (6): _design_knockoff_equi(), _design_knockoff_sdp(), _get_knmat(), Control false discovery rates (FDR) in regression analysis using the knockoff ap, Use semidefinite programming to construct a knockoff design matrix      Requires, Construct an equivariant design matrix for knockoff analysis      Follows the 'e

### Community 328 - "Community 328"
Cohesion: 0.25
Nodes (8): anova_generic(), anova_oneway(), AnovaResult, equivalence_oneway(), Equivalence test for oneway anova (Wellek's Anova)      The null hypothesis is t, Result of :func:`anova_generic` and :func:`anova_oneway`.      Parameters     --, Oneway Anova based on summary statistics      Parameters     ----------     mean, Oneway Anova      This implements standard anova, Welch and Brown-Forsythe, and

### Community 329 - "Community 329"
Cohesion: 0.25
Nodes (8): proportions_chisquare(), proportions_chisquare_allpairs(), proportions_chisquare_pairscontrol(), Create a k by 2 contingency table for proportion      helper function for propor, Test for proportions based on chisquare test      Parameters     ----------, Chisquare test of proportions for all pairs of k samples      Performs a chisqua, Chisquare test of proportions for pairs of k samples compared to control      Pe, _table_proportion()

### Community 330 - "Community 330"
Cohesion: 0.25
Nodes (7): power_poisson_diff_2indep(), PowerDiffResult, Score test and cmle for difference of 2 independent poisson rates      Parameter, Result of :func:`power_poisson_diff_2indep`.      Behaves like the scalar `power, Power of ztest for the difference between two independent poisson rates      Par, _score_diff(), _std_2poisson_power()

### Community 331 - "Community 331"
Cohesion: 0.25
Nodes (5): confidence interval for the difference in means          Parameters         ----, two-sided confidence interval for weighted mean of data          Confidence inte, generic normal-confint based on summary statistic      Parameters     ----------, summarize the results of the hypothesis test          Parameters         -------, _zconfint_generic()

### Community 332 - "Community 332"
Cohesion: 0.25
Nodes (4): Reset the index in-place          Parameters         ----------         index :, Set `slices` to a list of indices of the sorted groups          Parameters, Sort data based on the grouping index or a user-supplied index          Paramete, Apply function to each group          Similar to `transform_array` but does not

### Community 333 - "Community 333"
Cohesion: 0.29
Nodes (7): brentq_expanding(), BrentqExpandingInfo, Created on Mon Mar 18 15:48:23 2013 Author: Josef Perktold  Todo:   - test behav, # TODO: rtol is missing, what does it do?, Info returned by :func:`brentq_expanding` when ``full_output=True``.      Parame, # TODO: use Warnings, Note: brentq might still work even with max_it, Find the root of a function in one variable by expanding and brentq      Assumes

### Community 334 - "Community 334"
Cohesion: 0.38
Nodes (6): _get_data(), load(), load_pandas(), American National Election Survey 1996, Load the anes96 data and returns a Dataset class.      Returns     -------     D, Load the anes96 data and returns a Dataset class.      Returns     -------     D

### Community 335 - "Community 335"
Cohesion: 0.38
Nodes (6): fit_elasticnet(), _gen_npfuncs(), _opt_1d(), One-dimensional helper for elastic net.      Parameters     ----------     func, Negative penalized log-likelihood functions.      Returns the negative penalized, Return an elastic net regularized fit to a regression model.      Parameters

### Community 336 - "Community 336"
Cohesion: 0.33
Nodes (6): do_trim_params(), _get_verbose_addon(), qc_results(), Holds common functions for l1 solvers., Theory dictates that one of two conditions holds:         i) abs(score[i]) == al, Trims (set to zero) params that are zero at the theoretical minimum.     Uses he

### Community 337 - "Community 337"
Cohesion: 0.29
Nodes (3): The SCAD penalty of Fan and Li.      The SCAD penalty is linear around zero as a, Second derivative of function          This returns scalar or vector in same sha, SCAD

### Community 338 - "Community 338"
Cohesion: 0.38
Nodes (6): _get_data(), load(), load_pandas(), Bill Greene's credit scoring data, Load the credit card data and returns a Dataset class.      Returns     -------, Load the credit card data and returns a Dataset class.      Returns     -------

### Community 339 - "Community 339"
Cohesion: 0.29
Nodes (6): apply_where(), _next_regular(), Find the next regular number greater than or equal to target.     Regular number, Return an array of all value., Run one of two elementwise functions depending on a condition.      Equivalent t, _valarray()

### Community 340 - "Community 340"
Cohesion: 0.38
Nodes (6): _get_data(), load(), load_pandas(), World Copper Prices 1951-1975 dataset, Load the copper data and returns a Dataset class.      Returns     -------     D, Load the copper data and returns a Dataset class.      Returns     -------     D

### Community 341 - "Community 341"
Cohesion: 0.29
Nodes (3): Transformation Classes as generators for Archimedean copulas   Created on Wed Ja, generic multivariate Archimedean copula with additional power transforms      Ne, _TransfPower

### Community 342 - "Community 342"
Cohesion: 0.38
Nodes (6): _get_data(), load(), load_pandas(), US Capital Punishment dataset, Load the cpunish data and return a Dataset class.      Returns     -------     D, Load the cpunish data and return a Dataset class.      Returns     -------     D

### Community 343 - "Community 343"
Cohesion: 0.38
Nodes (5): _get_data(), load(), load_pandas(), Danish Money Demand Data, Load the Danish money demand data and return a Dataset class.      Returns     -

### Community 344 - "Community 344"
Cohesion: 0.29
Nodes (2): genpoisson_p_gen, Generalized Poisson distribution

### Community 345 - "Community 345"
Cohesion: 0.29
Nodes (3): Truncated Poisson discrete random variable, truncatedpoisson_gen, rv_discrete

### Community 346 - "Community 346"
Cohesion: 0.29
Nodes (2): Truncated Generalized Negative Binomial (NB-P) discrete random variable, truncatednegbin_gen

### Community 347 - "Community 347"
Cohesion: 0.29
Nodes (2): ACSkewT_gen, univariate Skew-T distribution of Azzalini      class follows scipy.stats.distri

### Community 348 - "Community 348"
Cohesion: 0.29
Nodes (4): NormExpan_gen, pdf_mvsk(), Return the Gaussian expanded pdf function given the list of 1st, 2nd     moment, Gram-Charlier Expansion of Normal distribution      class follows scipy.stats.di

### Community 349 - "Community 349"
Cohesion: 0.33
Nodes (2): Distribution based on a non-monotonic (u- or hump-shaped transformation)      th, TransfTwo_gen

### Community 350 - "Community 350"
Cohesion: 0.29
Nodes (2): class to hold quadratic function with inverse function and derivative      using, SquareFunc

### Community 351 - "Community 351"
Cohesion: 0.38
Nodes (5): _get_data(), load(), load_pandas(), Euro area 18 - Total Turnover Index, Manufacture of electrical equipment, Load the EU Electrical Equipment manufacturing data into a Dataset class      Re

### Community 352 - "Community 352"
Cohesion: 0.29
Nodes (4): _ELRegOpts, Empirical Likelihood Linear Regression Inference  The script contains the functi, A class that holds functions to be optimized over when conducting     hypothesis, A function that is optimized over nuisance parameters to conduct a         hypot

### Community 353 - "Community 353"
Cohesion: 0.29
Nodes (6): The one parameter exponential family distributions used by GLM., # TODO: add the ability to use the power links with an if test, # TODO: change these class attributes, use valid somewhere..., # TODO: quasi, quasibinomial, quasipoisson, # TODO: change the links class attribute in the families to hold, # TODO: it *should* work for a constant n>1 actually, if freq_weights

### Community 354 - "Community 354"
Cohesion: 0.33
Nodes (4): Cauchy, The Cauchy (standard Cauchy CDF) transform      .. deprecated:: 0.14.0         U, The Cauchy (standard Cauchy CDF) transform      Notes     -----     g(p) = scipy, Second derivative of the Cauchy link function.          Parameters         -----

### Community 355 - "Community 355"
Cohesion: 0.29
Nodes (4): BaseCrossValidator, Cross-validation iterators for GAM  Author: Luca Puggini, Base class for cross-validation iterators      Subclasses split the data into tr, # TODO: X and y are redundant, we only need nobs

### Community 356 - "Community 356"
Cohesion: 0.33
Nodes (6): _make_ellipse(), Create scatterplot with confidence ellipsis  Author: Josef Perktold License: BSD, # TODO: make sure we have same xlim and ylim, Support function for scatter_ellipse      Parameters     ----------     mean : a, Create a grid of scatter plots with confidence ellipses      Parameters     ----, scatter_ellipse()

### Community 357 - "Community 357"
Cohesion: 0.38
Nodes (6): _get_data(), load(), load_pandas(), Grunfeld (1950) Investment Data, Loads the Grunfeld data and returns a Dataset class.      Returns     -------, Loads the Grunfeld data and returns a Dataset class.      Returns     -------

### Community 358 - "Community 358"
Cohesion: 0.38
Nodes (5): _get_data(), load(), load_pandas(), (West) German interest and inflation rate 1972-1998, Load the West German interest/inflation data and return a Dataset class.      Re

### Community 359 - "Community 359"
Cohesion: 0.38
Nodes (5): _get_data(), load(), load_pandas(), United States Macroeconomic data, Load the US macro data and return a Dataset class.      Returns     -------

### Community 360 - "Community 360"
Cohesion: 0.33
Nodes (5): _check_args_1(), _check_args_2(), Validate the arguments provided to Factor before endog is processed      Paramet, Validate the arguments provided to Factor after endog is processed      Paramete, # TODO: check row versus column convention for T

### Community 361 - "Community 361"
Cohesion: 0.38
Nodes (6): _get_data(), load(), load_pandas(), RAND Health Insurance Experiment Data, Loads the RAND HIE data and returns a Dataset class.      Returns     -------, Loads the RAND HIE data and returns a Dataset class.      Returns     -------

### Community 362 - "Community 362"
Cohesion: 0.33
Nodes (4): CovDetMCD, Minimum covariance determinant estimator with deterministic starts      Prelimin, C-step for mcd iteration          Requires starting mean and cov.          Param, Compute mcd for one starting set of observations          Parameters         ---

### Community 363 - "Community 363"
Cohesion: 0.33
Nodes (4): Huber, Huber's proposal 2 for estimating location and scale jointly      Parameters, Compute Huber's proposal 2 estimate of scale          Uses an optional initial v, Estimate scale and location simultaneously          Parameters         ---------

### Community 364 - "Community 364"
Cohesion: 0.33
Nodes (3): MScale, M-scale estimation      Parameters     ----------     chi_func : callable, Estimate M-scale using iteration          Parameters         ----------

### Community 365 - "Community 365"
Cohesion: 0.38
Nodes (6): _get_data(), load(), load_pandas(), Taxation Powers Vote for the Scottish Parliament 1997 dataset, Load the Scotvote data and returns a Dataset instance.      Returns     -------, Load the Scotvote data and returns a Dataset instance.      Returns     -------

### Community 366 - "Community 366"
Cohesion: 0.38
Nodes (6): _get_data(), load(), load_pandas(), Spector and Mazzeo (1980) - Program Effectiveness Data, Load the Spector dataset and returns a Dataset class instance.      Returns, Load the Spector dataset and returns a Dataset class instance.      Returns

### Community 367 - "Community 367"
Cohesion: 0.29
Nodes (3): Summarize the results of the hypothesis test          Parameters         -------, Return the parameter table as a pandas DataFrame          This is only available, Return the confidence interval of the value, `effect` of the constraint

### Community 368 - "Community 368"
Cohesion: 0.38
Nodes (6): _get_data(), load(), load_pandas(), U.S. Strike Duration Data, Load the strikes data and return a Dataset class instance.      Returns     ----, Load the strikes data and return a Dataset class instance.      Returns     ----

### Community 369 - "Community 369"
Cohesion: 0.38
Nodes (6): _get_data(), load(), load_pandas(), Yearly sunspots data 1700-2008, # TODO: time series, Load the yearly sunspot data and returns a data class.      Returns     -------

### Community 370 - "Community 370"
Cohesion: 0.29
Nodes (6): _is_hierarchical(), _make_generic_names(), _make_hierarchical_index(), Check if the first item of an array-like object is also array-like      Paramete, Build a MultiIndex from an array-like of row-wise group tuples      Parameters, Create generic zero-padded level names for an index      Parameters     --------

### Community 371 - "Community 371"
Cohesion: 0.33
Nodes (6): parallel_func(), Parallel utility function using joblib  copied from https://github.com/mne-tools, Return parallel instance with delayed function      Util function to use joblib, ModuleUnavailableWarning, Non-fatal import error, Warning

### Community 372 - "Community 372"
Cohesion: 0.29
Nodes (6): mackinnoncrit(), mackinnonp(), # NOTE: The Z-statistic is used when lags are included to account for, # TODO: finish this and then integrate them into adf function, Return MacKinnon's approximate p-value for teststat      Parameters     --------, Return the critical values for cointegrating and the ADF test      In 2010 MacKi

### Community 373 - "Community 373"
Cohesion: 0.33
Nodes (5): SARIMAX tools  Author: Chad Fulton License: BSD-3, Standardize lag order input      Parameters     ----------     order : int or ar, Validate parameter vector for basic correctness      Parameters     ----------, standardize_lag_order(), validate_basic()

### Community 374 - "Community 374"
Cohesion: 0.33
Nodes (2): L2, The L2 (ridge) penalty.

### Community 375 - "Community 375"
Cohesion: 0.33
Nodes (2): PseudoHuber, The pseudo-Huber penalty.

### Community 376 - "Community 376"
Cohesion: 0.40
Nodes (5): load(), load_pandas(), Smoking and lung cancer in eight cities in China, Load the China smoking/lung cancer data and return a Dataset class.      Returns, Load the China smoking/lung cancer data and return a Dataset class.      Returns

### Community 377 - "Community 377"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), Mauna Loa Weekly Atmospheric CO2 Data, Load the data and return a Dataset class instance.      Returns     -------

### Community 378 - "Community 378"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), First 100 days of the US House of Representatives 1995, Load the committee data and returns a data class.      Returns     -------     D

### Community 379 - "Community 379"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), Load the data and return a Dataset class instance.      Returns     -------, Load the strikes data and return a Dataset class instance.      Returns     ----

### Community 380 - "Community 380"
Cohesion: 0.33
Nodes (3): Returns the score function evaluated at `params`          Parameters         ---, Returns the gradient of the log partial likelihood, using the         Breslow me, Returns the gradient of the log partial likelihood evaluated         at `params`

### Community 381 - "Community 381"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), El Nino dataset, 1950 - 2010, Load the El Nino data and return a Dataset class.      Returns     -------     D

### Community 382 - "Community 382"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), Engel (1857) food expenditure data, Load the data and return a Dataset class instance.      Returns     -------

### Community 383 - "Community 383"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), Fair's Extramarital Affairs Data, Load the data and return a Dataset class instance.      Returns     -------

### Community 384 - "Community 384"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), World Bank Fertility Data, Load the data and return a Dataset class instance.      Returns     -------

### Community 385 - "Community 385"
Cohesion: 0.33
Nodes (3): _FormulaOption, Get or set the formula engine          Returns         -------         str: {"pa, Get or set the ordering.          Returns         -------         {"degree", "so

### Community 386 - "Community 386"
Cohesion: 0.40
Nodes (5): plot_corr(), plot_corr_grid(), Correlation plots  Author: Josef Perktold License: BSD-3  example for usage with, Create a grid of correlation plots      The individual correlation plots are ass, Plot correlation of many variables in a tight color grid      Parameters     ---

### Community 387 - "Community 387"
Cohesion: 0.40
Nodes (5): interaction_plot(), Authors:    Josef Perktold, Skipper Seabold, Denis A. Engemann, Recode categorical data to int factor      Parameters     ----------     x : arr, Interaction plot for factor level statistics      Parameters     ----------, _recode()

### Community 388 - "Community 388"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), Heart Transplant Data, Miller 1976, Load the data and return a Dataset class instance.      Returns     -------

### Community 389 - "Community 389"
Cohesion: 0.33
Nodes (5): dentonm(), # NOTE: only D4 is the only one implemented, see IMF chapter 6., # TODO: break this out so that we can simplify the linalg?, # TODO: take code in the string at the end and implement Denton's original, Modified Denton's method to convert low-frequency to high-frequency data      Us

### Community 390 - "Community 390"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), Load the Longley data and return a Dataset class.      Returns     -------     D, Load the Longley data and return a Dataset class.      Returns     -------     D

### Community 391 - "Community 391"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), Load the data modechoice data and return a Dataset class instance.      Returns, Load the data modechoice data and return a Dataset class instance.      Returns

### Community 392 - "Community 392"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), Load the Nile data and return a Dataset class instance.      Returns     -------, # TODO: time series

### Community 393 - "Community 393"
Cohesion: 0.33
Nodes (5): atleast_2dcol(), Additional functions  prediction standard errors and confidence intervals   A: j, convert array_like to 2d from 1d or 0d      not tested because not used, calculate standard deviation and confidence interval for prediction      applies, wls_prediction_std()

### Community 394 - "Community 394"
Cohesion: 0.33
Nodes (6): cov_tyler_pairs_regularized(), cov_tyler_regularized(), CovTylerRegularizedResult, Result of :func:`cov_tyler_regularized` and     :func:`cov_tyler_pairs_regulariz, Regularized Tyler's M-estimator for normalized covariance (shape)      The under, Tyler's M-estimator for normalized covariance (scatter)      The underlying (pop

### Community 395 - "Community 395"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), Load the stack loss data and returns a Dataset class instance.      Returns, Load the stack loss data and returns a Dataset class instance.      Returns

### Community 396 - "Community 396"
Cohesion: 0.47
Nodes (5): _get_data(), load(), load_pandas(), Star98 Educational Testing dataset, Load the star98 data and returns a Dataset class instance.      Returns     ----

### Community 397 - "Community 397"
Cohesion: 0.40
Nodes (2): Set the smoother output          The smoother can produce several types of resul, r"""         Set the smoothing method          The smoothing method can be used

### Community 398 - "Community 398"
Cohesion: 0.33
Nodes (6): _compute_coefficients_from_multivariate_pacf_python(), constrain_stationary_multivariate_python(), _constrain_sv_less_than_one_python(), Transform arbitrary matrices to matrices with singular values less than     one., Transform matrices with singular values less than one to matrices     correspond, r"""     Transform unconstrained parameters used by the optimizer to constrained

### Community 399 - "Community 399"
Cohesion: 0.40
Nodes (5): anderson_statistic(), normal_ad(), Created on Sun Sep 25 21:23:38 2011  Author: Josef Perktold and Scipy developers, Calculate the Anderson-Darling a2 statistic      Parameters     ----------     x, Anderson-Darling test for normal distribution unknown mean and variance      Par

### Community 400 - "Community 400"
Cohesion: 0.33
Nodes (4): FTestPowerF2, Statistical Power calculations for generic F-test of a constraint      This is b, Calculate the power of a F-test          The effect size is Cohen's ``f^2``., Solve for any one parameter of the power of a F-test          for the one sample

### Community 401 - "Community 401"
Cohesion: 0.33
Nodes (4): Statistical Power calculations for one sample or paired sample t-test, Calculate the power of a t-test for one sample or paired samples          Parame, Solve for any one parameter of the power of a one sample t-test          for the, TTestPower

### Community 402 - "Community 402"
Cohesion: 0.33
Nodes (6): _power_ztost(), power_ztost_prop(), Standard error for the estimate of a proportion      This is just ``np.sqrt(p *, Generic statistical power function for normal based equivalence test      This i, Power of proportions equivalence test based on normal distribution      Paramete, std_prop()

### Community 403 - "Community 403"
Cohesion: 0.33
Nodes (4): z-test for the null hypothesis of identical means          Parameters         --, test of equivalence for two independent samples, based on z-test          Parame, generic (normal) z-test based on summary statistic      The test statistic is :, _zstat_generic()

### Community 404 - "Community 404"
Cohesion: 0.33
Nodes (4): test of (non-)equivalence for two dependent, paired sample      TOST: two one-si, ttest of Null hypothesis that mean is equal to value          The alternative hy, test of (non-)equivalence of one sample          TOST: two one-sided t tests, ttost_paired()

### Community 405 - "Community 405"
Cohesion: 0.33
Nodes (5): pca(), pcasvd(), Principal Component Analysis   Created on Tue Sep 29 20:11:23 2009 Author: josef, principal components with eigenvector decomposition     similar to princomp in m, principal components with svd      Parameters     ----------     data : ndarray,

### Community 406 - "Community 406"
Cohesion: 0.33
Nodes (1): Deterministic terms spanning a range of observations          Parameters

### Community 407 - "Community 407"
Cohesion: 0.33
Nodes (3): Fourier transform of ARMA polynomial, zero-padded at end to n          The Fouri, raw spectral density, returns Fourier transform          n is number of points i, autocovariance from spectral density          scaling is correct, but n needs to

### Community 408 - "Community 408"
Cohesion: 0.33
Nodes (2): HypothesisTestResults, Results class for hypothesis tests      Parameters     ----------     test_stati

### Community 409 - "Community 409"
Cohesion: 0.40
Nodes (2): Compute asymptotic standard errors for impulse response coefficients          Pa, Compute asymptotic standard errors for cumulative impulse response         coeff

### Community 410 - "Community 410"
Cohesion: 0.60
Nodes (4): _get_data(), load(), load_pandas(), Load the data and return a Dataset class instance.      Returns     -------

### Community 411 - "Community 411"
Cohesion: 0.40
Nodes (2): ExpTransf_gen, Distribution based on log/exp transformation      the constructor can be called

### Community 412 - "Community 412"
Cohesion: 0.40
Nodes (5): _hermnorm(), pdf_moments(), pdf_moments_st(), Return the Gaussian expanded pdf function given the list of central     moments, Return the Gaussian expanded pdf function given the list of central     moments

### Community 413 - "Community 413"
Cohesion: 0.40
Nodes (2): LogTransf_gen, Distribution based on log/exp transformation      the constructor can be called

### Community 414 - "Community 414"
Cohesion: 0.40
Nodes (4): _kernel_cumincidence(), _kernel_survfunc(), Estimate the marginal survival function under dependent censoring      Parameter, Calculates cumulative incidence functions using kernels      Parameters     ----

### Community 415 - "Community 415"
Cohesion: 0.40
Nodes (4): bkfilter(), Filter a time series using the Baxter-King bandpass filter      Parameters     -, # TODO: change the docstring to ..math::?, # TODO: allow windowing functions to correct for Gibb's Phenomenon?

### Community 416 - "Community 416"
Cohesion: 0.40
Nodes (2): NAAction, Get the NA action for the formula engine.          Parameters         ----------

### Community 417 - "Community 417"
Cohesion: 0.40
Nodes (1): Akaike Information Criterion         -2 * `llf` + 2 * (`df_model` + 1)

### Community 418 - "Community 418"
Cohesion: 0.40
Nodes (2): Evaluate the log-likelihood function.          Parameters         ----------, Evaluate the score function (first derivative of loglike).          Parameters

### Community 419 - "Community 419"
Cohesion: 0.40
Nodes (4): plot_loadings(), plot_scree(), Plot of the ordered eigenvalues and variance explained for the loadings      Par, Plot factor loadings in 2-d plots      Parameters     ----------     loadings :

### Community 420 - "Community 420"
Cohesion: 0.40
Nodes (4): lowess(), Lowess - wrapper for cythonized extension  Author : Chris Jordan-Squire Author :, # TODO: allow this again, LOWESS (Locally Weighted Scatterplot Smoothing)      A lowess function that outp

### Community 421 - "Community 421"
Cohesion: 0.60
Nodes (4): _get_data(), load(), load_pandas(), Load the statecrime data and return a Dataset class instance.      Returns     -

### Community 422 - "Community 422"
Cohesion: 0.40
Nodes (5): _compute_smoothed_state_weights(), Reorder the rows or columns of a time-varying matrix where all non-missing     v, Construct the weights of observations and the prior on the smoothed state      P, r"""     Construct the weights of observations and the prior on the smoothed sta, reorder_missing_matrix()

### Community 423 - "Community 423"
Cohesion: 0.40
Nodes (4): Author: Josef Perktold License: BSD-3, # TODO: why do I need to squeeze in poisson example, # TODO: add use_t option or not?, # TODO: predicted and se as arguments to avoid duplicate calculations

### Community 424 - "Community 424"
Cohesion: 0.40
Nodes (3): _mover_confint(), Created on Mar 30, 2022 1:21:54 PM  Author: Josef Perktold License: BSD-3, Compute a MOVER confidence interval for a contrast of two statistics      The "M

### Community 425 - "Community 425"
Cohesion: 0.40
Nodes (4): power_negbin_ratio_2indep(), PowerNegbinRatioResult, Result of :func:`power_negbin_ratio_2indep`.      Behaves like the scalar `power, Power of test of ratio of 2 independent negative binomial rates      Parameters

### Community 426 - "Community 426"
Cohesion: 0.40
Nodes (4): power_poisson_ratio_2indep(), PowerRatioResult, Result of :func:`power_poisson_ratio_2indep`.      Behaves like the scalar `powe, Power of test of ratio of 2 independent poisson rates      This is based on Zhu

### Community 427 - "Community 427"
Cohesion: 0.40
Nodes (4): add_indep(), Utilities for adding independent columns to design matrices, # TODO: this needs tests for subclasses, Construct an array with independent columns      Parameters     ----------     x

### Community 428 - "Community 428"
Cohesion: 0.40
Nodes (3): indent(), Vendored docstring decorators  Previously imported from pandas.util._decorators., Add indentation to each line of text      Uses 4-space blocks per indent level,

### Community 429 - "Community 429"
Cohesion: 0.50
Nodes (3): _nan_rows(), Handle missing data in endog, exog and any extra arrays          This returns a, Returns a boolean array which is True where any of the rows in any     of the _2

### Community 430 - "Community 430"
Cohesion: 0.67
Nodes (3): main(), process_tempita(), Process tempita templated file and write out the result.      The template file

### Community 431 - "Community 431"
Cohesion: 0.50
Nodes (3): inplace_reshape(), Compatibility functions for numpy versions in lib  np_new_unique ------------- O, Reshape an array in place when possible, falling back to a copy      Parameters

### Community 432 - "Community 432"
Cohesion: 0.50
Nodes (1): Transforms

### Community 433 - "Community 433"
Cohesion: 0.50
Nodes (3): Created on Wed Nov 18 15:17:58 2020  Author: Josef Perktold License: BSD-3, # TODO: verify upper bound, we drop last bin (may be open, inf), # TODO: what's the correct df, same as for multinomial/ordered ?

### Community 434 - "Community 434"
Cohesion: 0.50
Nodes (2): univariate Skew-Normal distribution of Azzalini      class follows scipy.stats.d, SkewNorm2_gen

### Community 435 - "Community 435"
Cohesion: 0.50
Nodes (3): Implementation of proportional hazards regression models for duration data that, # TODO: some disagreements with R, not the same algorithm but, # TODO: not used?

### Community 436 - "Community 436"
Cohesion: 0.50
Nodes (2): Calculate the difference between the log likelihood of mu_test and a         spe, Returns - 2 x log-likelihood ratio, p-value and weights         for a hypothesis

### Community 437 - "Community 437"
Cohesion: 0.50
Nodes (2): Calculate the difference between the log likelihood ratio at skew         and a, Returns  -2 x log-likelihood and p-value for the hypothesized         skewness.

### Community 438 - "Community 438"
Cohesion: 0.50
Nodes (2): Used to determine the confidence intervals for the variance          It calls te, Returns  -2 x log-likelihood ratio and the p-value for the         hypothesized

### Community 439 - "Community 439"
Cohesion: 0.50
Nodes (1): Initialization methods for states of exponential smoothing models

### Community 440 - "Community 440"
Cohesion: 0.50
Nodes (2): Get the list of categories for a factor.          Parameters         ----------, Get the contrast matrix for a term and factor.          Parameters         -----

### Community 441 - "Community 441"
Cohesion: 0.50
Nodes (3): mean_diff_plot(), Bland-Altman mean-difference plots  Author: Joses Ho License: BSD-3, Construct a Tukey/Bland-Altman Mean Difference Plot      Tukey's Mean Difference

### Community 443 - "Community 443"
Cohesion: 0.50
Nodes (3): Input/Output tools for working with binary data  See Also -------- numpy.lib.io, Save an array to a text file      This is just a copy of numpy.savetxt patched t, savetxt()

### Community 444 - "Community 444"
Cohesion: 0.67
Nodes (3): errfunc(), qhat(), This script builds the T table and A table for the upper quantile studentized ra

### Community 445 - "Community 445"
Cohesion: 0.50
Nodes (2): approximate pointwise variance for kernel density          not verified, approximate pointwise confidence interval for kernel density          The confid

### Community 446 - "Community 446"
Cohesion: 0.50
Nodes (3): Tricube Kernel for continuous variables      Parameters     ----------     h : 1, Tricube Kernel      K(u) = 0.864197530864 * (1 - abs(x)**3)**3 between -1.0 and, Tricube

### Community 447 - "Community 447"
Cohesion: 0.50
Nodes (2): Compute significance bounds for the CUSUM statistic          Parameters, r"""         Plot the CUSUM statistic and significance bounds          Parameter

### Community 448 - "Community 448"
Cohesion: 0.50
Nodes (2): Compute significance bounds for the CUSUM of squares statistic          Paramete, r"""         Plot the CUSUM of squares statistic and significance bounds

### Community 449 - "Community 449"
Cohesion: 0.50
Nodes (4): cov_gk(), cov_gk1(), Gnanadesikan and Kettenring covariance between two variables      Parameters, Gnanadesikan and Kettenring covariance matrix estimator      Parameters     ----

### Community 450 - "Community 450"
Cohesion: 0.50
Nodes (2): Combine details of impacts from news and revisions into one table          Param, Get impacts from news and revisions on variables of interest          Parameters

### Community 451 - "Community 451"
Cohesion: 0.50
Nodes (4): _compute_multivariate_sample_acovf(), _compute_multivariate_sample_pacf(), r"""     Compute multivariate sample autocovariances      Parameters     -------, Compute multivariate sample partial autocorrelations      Parameters     -------

### Community 452 - "Community 452"
Cohesion: 0.50
Nodes (4): equivalence_scale_oneway(), Result of :func:`equivalence_scale_oneway`.      Has the same attributes as :cla, Oneway Anova test for equivalence of scale, variance or dispersion      This hyp, ScaleEquivalenceResult

### Community 453 - "Community 453"
Cohesion: 0.50
Nodes (4): _fstat2effectsize(), FstatEffectSizeResult, Result of :func:`_fstat2effectsize`.      Parameters     ----------     f2 : arr, Compute anova effect size from F-statistic      This might be combined with conv

### Community 454 - "Community 454"
Cohesion: 0.50
Nodes (4): Result of :func:`test_scale_oneway`.      Has the same attributes as :class:`Ano, Oneway Anova test for equal scale, variance or dispersion      This hypothesis t, ScaleAnovaResult, test_scale_oneway()

### Community 455 - "Community 455"
Cohesion: 0.50
Nodes (4): binom_test(), binom_tost(), Exact TOST test for one proportion using binomial distribution      Parameters, Perform a test that the probability of success is p      This is an exact, two-s

### Community 456 - "Community 456"
Cohesion: 0.50
Nodes (4): binom_tost_reject_interval(), power_binom_tost(), Rejection region for binomial TOST      The interval includes the end points,, Power for exact binomial equivalence test      Parameters     ----------     low

### Community 457 - "Community 457"
Cohesion: 0.50
Nodes (4): proportions_ztest(), proportions_ztost(), Test for proportions based on normal (z) test      Parameters     ----------, Equivalence test based on normal distribution      Parameters     ----------

### Community 458 - "Community 458"
Cohesion: 0.50
Nodes (4): nonequivalence_poisson_2indep(), NonequivalencePoissonResult, Result of :func:`nonequivalence_poisson_2indep`.      Parameters     ----------, Test for non-equivalence, minimum effect for poisson      This reverses null and

### Community 459 - "Community 459"
Cohesion: 0.50
Nodes (2): variance of data given ddof          Parameters         ----------         ddof, standard deviation of data with given ddof          Parameters         ---------

### Community 460 - "Community 460"
Cohesion: 0.67
Nodes (3): arma_order_select_ic(), Compute information criteria for many ARMA models      Parameters     ----------, _safe_arma_fit()

### Community 461 - "Community 461"
Cohesion: 0.50
Nodes (2): Apply function to each column, by group          Parameters         ----------, Apply function to each column, by group          Parameters         ----------

### Community 462 - "Community 462"
Cohesion: 0.50
Nodes (3): check_random_state(), Random number generator helpers, Turn a seed into a random number generator      Parameters     ----------     se

### Community 463 - "Community 463"
Cohesion: 0.50
Nodes (1): Created on Thu Aug 30 12:26:38 2012 Author: Josef Perktold   function jc =  c_sj

### Community 464 - "Community 464"
Cohesion: 0.50
Nodes (1): Created on Mon Dec 14 19:53:25 2009  Author: josef-pktd  generate arma sample us

### Community 465 - "Community 465"
Cohesion: 0.50
Nodes (3): array_like(), Decorators for validating function arguments, Decorate a function argument with array_like validation      Parameters     ----

### Community 467 - "Community 467"
Cohesion: 0.67
Nodes (1): Initialize dates          Parameters         ----------         dates : array_li

### Community 469 - "Community 469"
Cohesion: 0.67
Nodes (2): r"""     Subroutine for orthogonal and oblique rotation of the matrix :math:`A`, rotate_factors()

### Community 470 - "Community 470"
Cohesion: 0.67
Nodes (2): dot_plot(), Dot plotting (also known as forest and blobbogram)      Produce a dotplot simila

### Community 471 - "Community 471"
Cohesion: 0.67
Nodes (2): rainbow(), Return a list of colors sampled at equal intervals over the spectrum      Parame

### Community 472 - "Community 472"
Cohesion: 0.67
Nodes (2): Plot a Tukey HSD pairwise mean-comparison confidence interval chart      Paramet, tukeyplot()

### Community 473 - "Community 473"
Cohesion: 0.67
Nodes (2): Cosine2, Cosine2 Kernel      K(u) = 1 + cos(2 * pi * u) between -0.5 and 0.5      Note: t

### Community 474 - "Community 474"
Cohesion: 0.67
Nodes (2): Cosine, Cosine Kernel      K(u) = pi/4 cos(0.5 * pi * u) between -1.0 and 1.0

### Community 475 - "Community 475"
Cohesion: 0.67
Nodes (2): combine_indices(), Use np.unique to get integer group indices for product, intersection      Parame

### Community 476 - "Community 476"
Cohesion: 1.00
Nodes (1): _make_endog_names()

### Community 477 - "Community 477"
Cohesion: 1.00
Nodes (1): _make_exog_names()

### Community 478 - "Community 478"
Cohesion: 1.00
Nodes (1): Labels for covariance matrices          In multidimensional models, each dimensi

### Community 479 - "Community 479"
Cohesion: 1.00
Nodes (1): PatsyData

### Community 480 - "Community 480"
Cohesion: 1.00
Nodes (1): TODO: how to add constraints?          Something like         sm.add_constraint(

### Community 481 - "Community 481"
Cohesion: 1.00
Nodes (1): Platform detection flags used across statsmodels

### Community 482 - "Community 482"
Cohesion: 1.00
Nodes (1): Dow-Jones Utilities Index, Aug.28--Dec.18, 1972  Dataset described in [1]_ and i

### Community 483 - "Community 483"
Cohesion: 1.00
Nodes (1): Lake level of Lake Huron in feet (reduced by 570), 1875--1972  Dataset described

### Community 484 - "Community 484"
Cohesion: 1.00
Nodes (1): 57 consecutive daily overshorts from an underground gasoline tank at a filling s

### Community 485 - "Community 485"
Cohesion: 1.00
Nodes (1): The number of car drivers killed or seriously injured monthly in Great Britain f

### Community 486 - "Community 486"
Cohesion: 1.00
Nodes (1): Plot observed versus predicted frequencies for entire sample

### Community 487 - "Community 487"
Cohesion: 1.00
Nodes (1): Moment test for binned probabilities using OPG          Parameters         -----

### Community 488 - "Community 488"
Cohesion: 1.00
Nodes (1): Hosmer-Lemeshow style test for count data          Note, this does not take into

### Community 489 - "Community 489"
Cohesion: 1.00
Nodes (1): Test for excess (over or under) dispersion in Poisson          Returns         -

### Community 490 - "Community 490"
Cohesion: 1.00
Nodes (1): Test for excess zeros, zero inflation or deflation          Parameters         -

### Community 491 - "Community 491"
Cohesion: 1.00
Nodes (1): temporary location for enhancements to scipy.stats  includes ^^^^^^^^  * Per Bro

### Community 492 - "Community 492"
Cohesion: 1.00
Nodes (1): standard deviation, square root of diagonal elements of sigma

### Community 493 - "Community 493"
Cohesion: 1.00
Nodes (1): Get a mask indicating if data are missing.          Returns         -------

### Community 494 - "Community 494"
Cohesion: 1.00
Nodes (1): Returns the engine-specific model specification type.          Returns         -

### Community 495 - "Community 495"
Cohesion: 1.00
Nodes (1): Remove intercept from Patsy terms.          Parameters         ----------

### Community 496 - "Community 496"
Cohesion: 1.00
Nodes (1): Get the model specification. Only available after calling get_arrays.

### Community 497 - "Community 497"
Cohesion: 1.00
Nodes (1): Yield index splits into train and test sets          Parameters         --------

### Community 498 - "Community 498"
Cohesion: 1.00
Nodes (1): Evaluate second derivative of penalty with respect to params          Parameters

### Community 499 - "Community 499"
Cohesion: 1.00
Nodes (1): Evaluate derivative of penalty with respect to params          Parameters

### Community 500 - "Community 500"
Cohesion: 1.00
Nodes (1): Evaluate penalization at params          Parameters         ----------         p

### Community 501 - "Community 501"
Cohesion: 1.00
Nodes (1): Penalty matrix for generalized additive model          Parameters         ------

### Community 503 - "Community 503"
Cohesion: 1.00
Nodes (1): . regress totemp gnpdefl gnp unemp armed pop year        Source |       SS

### Community 504 - "Community 504"
Cohesion: 1.00
Nodes (1): Summary Table formatting  This is here to help keep the formatting consistent ac

### Community 507 - "Community 507"
Cohesion: 1.00
Nodes (1): Loglikelihood at each observation, computed from recursive residuals

### Community 508 - "Community 508"
Cohesion: 1.00
Nodes (1): Loglikelihood defined by recursive residuals, equivalent to OLS

### Community 509 - "Community 509"
Cohesion: 1.00
Nodes (1): Sum of squared recursive residuals

### Community 510 - "Community 510"
Cohesion: 1.00
Nodes (1): Centered total sum of squares

### Community 511 - "Community 511"
Cohesion: 1.00
Nodes (1): Uncentered total sum of squares

### Community 512 - "Community 512"
Cohesion: 1.00
Nodes (1): Explained sum of squares

### Community 513 - "Community 513"
Cohesion: 1.00
Nodes (1): Mean squared error of the model

### Community 514 - "Community 514"
Cohesion: 1.00
Nodes (1): Mean squared error of the residuals

### Community 515 - "Community 515"
Cohesion: 1.00
Nodes (1): Total mean squared error

### Community 516 - "Community 516"
Cohesion: 1.00
Nodes (2): copy_index_vector(), Reorder the elements of a time-varying vector where all non-index     values are

### Community 517 - "Community 517"
Cohesion: 1.00
Nodes (2): copy_missing_matrix(), Copy the rows or columns of a time-varying matrix where all non-missing     valu

### Community 518 - "Community 518"
Cohesion: 1.00
Nodes (2): copy_missing_vector(), Reorder the elements of a time-varying vector where all non-missing     values a

### Community 519 - "Community 519"
Cohesion: 1.00
Nodes (2): diff(), r"""     Difference a series simply and/or seasonally along the zero-th axis

### Community 520 - "Community 520"
Cohesion: 1.00
Nodes (2): get_impact_dates(), Compute start/end periods and an index, often for impacts of data updates      P

### Community 521 - "Community 521"
Cohesion: 1.00
Nodes (2): prepare_exog(), Standardize the shape of an exog array and compute its number of columns      Pa

### Community 522 - "Community 522"
Cohesion: 1.00
Nodes (2): prepare_trend_data(), Construct the trend data array associated with a given trend polynomial      Par

### Community 523 - "Community 523"
Cohesion: 1.00
Nodes (2): prepare_trend_spec(), Translate a trend specification into a polynomial trend and its order      Param

### Community 524 - "Community 524"
Cohesion: 1.00
Nodes (2): Set the compatibility mode      Parameters     ----------     compatibility : bo, set_mode()

### Community 525 - "Community 525"
Cohesion: 1.00
Nodes (2): Validate the shape of a possibly time-varying matrix, or raise an exception, validate_matrix_shape()

### Community 526 - "Community 526"
Cohesion: 1.00
Nodes (2): Validate the shape of a possibly time-varying vector, or raise an exception, validate_vector_shape()

### Community 527 - "Community 527"
Cohesion: 1.00
Nodes (2): Reorder the elements of a time-varying vector where all non-missing     values a, reorder_missing_vector()

### Community 528 - "Community 528"
Cohesion: 1.00
Nodes (2): Compute condition while protecting from LinAlgError, _safe_cond()

### Community 529 - "Community 529"
Cohesion: 1.00
Nodes (1): column names for summary table

### Community 530 - "Community 530"
Cohesion: 1.00
Nodes (1): temporary location for enhancements to scipy.stats  includes ^^^^^^^^  * Per Bro

### Community 531 - "Community 531"
Cohesion: 1.00
Nodes (1): This file is automatically generated by littlefors_critical_values.py  Do not di

### Community 532 - "Community 532"
Cohesion: 1.00
Nodes (1): Update self.params with supplied args          Only valid when Substitution was

### Community 533 - "Community 533"
Cohesion: 1.00
Nodes (1): Typing aliases used by statsmodels

### Community 534 - "Community 534"
Cohesion: 1.00
Nodes (1): Create an identical deterministic process with a different index          Parame

### Community 535 - "Community 535"
Cohesion: 1.00
Nodes (1): The index of the process

### Community 536 - "Community 536"
Cohesion: 1.00
Nodes (1): The deterministic terms included in the process

### Community 537 - "Community 537"
Cohesion: 1.00
Nodes (1): tuple of attributes that are used for equality comparison

### Community 538 - "Community 538"
Cohesion: 1.00
Nodes (1): Produce deterministic trends for in-sample fitting          Parameters         -

### Community 539 - "Community 539"
Cohesion: 1.00
Nodes (1): Flag indicating whether the values produced are dummy variables

### Community 540 - "Community 540"
Cohesion: 1.00
Nodes (1): Produce deterministic trends for out-of-sample forecasts          Parameters

### Community 541 - "Community 541"
Cohesion: 1.00
Nodes (1): A meaningful string representation of the term

### Community 542 - "Community 542"
Cohesion: 1.00
Nodes (1): Create a TimeTrend from a string description.          Provided for compatibilit

### Community 543 - "Community 543"
Cohesion: 1.00
Nodes (1): The period of the seasonality

### Community 544 - "Community 544"
Cohesion: 1.00
Nodes (1): The seasonal index of the first observation

### Community 545 - "Community 545"
Cohesion: 1.00
Nodes (1): Construct a seasonality directly from an index using its frequency.          Par

### Community 546 - "Community 546"
Cohesion: 1.00
Nodes (1): functions and classes time series analysis   Status ------ work in progress  ari

## Knowledge Gaps
- **1564 isolated node(s):** `Run the test suite      Parameters     ----------     extra_args : list[str]`, `Process tempita templated file and write out the result.      The template file`, `A collection of smooth penalty functions.  Penalties on vectors take a vector ar`, `A class for representing a scalar-value penalty.      Parameters     ----------`, `A penalty function on a vector of parameters.          Parameters         ------` (+1559 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 73`** (1 nodes): `RollingRegressionResults`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 133`** (2 nodes): `ModelData`, `Class responsible for handling input data and extracting metadata into the     a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 139`** (1 nodes): `DiscreteResults`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 158`** (1 nodes): `NegativeBinomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 202`** (1 nodes): `GLMGamResults`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 248`** (1 nodes): `TransfClayton`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 261`** (2 nodes): `Zero Inflated Generalized Negative Binomial distribution`, `zinegativebinomial_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 277`** (1 nodes): `RollingWLS`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 286`** (1 nodes): `TransfGumbel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 287`** (2 nodes): `Zero Inflated Poisson distribution`, `zipoisson_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 302`** (1 nodes): `TransfFrank`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 305`** (2 nodes): `BivariateNormal`, `Kullback-Leibler divergence between this and another distribution          int f`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 314`** (1 nodes): `TransfIndep`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 316`** (2 nodes): `univariate Skew-Normal distribution of Azzalini      class follows scipy.stats.d`, `SkewNorm_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 344`** (2 nodes): `genpoisson_p_gen`, `Generalized Poisson distribution`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 346`** (2 nodes): `Truncated Generalized Negative Binomial (NB-P) discrete random variable`, `truncatednegbin_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 347`** (2 nodes): `ACSkewT_gen`, `univariate Skew-T distribution of Azzalini      class follows scipy.stats.distri`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 349`** (2 nodes): `Distribution based on a non-monotonic (u- or hump-shaped transformation)      th`, `TransfTwo_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 350`** (2 nodes): `class to hold quadratic function with inverse function and derivative      using`, `SquareFunc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 374`** (2 nodes): `L2`, `The L2 (ridge) penalty.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 375`** (2 nodes): `PseudoHuber`, `The pseudo-Huber penalty.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 397`** (2 nodes): `Set the smoother output          The smoother can produce several types of resul`, `r"""         Set the smoothing method          The smoothing method can be used`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 406`** (1 nodes): `Deterministic terms spanning a range of observations          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 408`** (2 nodes): `HypothesisTestResults`, `Results class for hypothesis tests      Parameters     ----------     test_stati`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 409`** (2 nodes): `Compute asymptotic standard errors for impulse response coefficients          Pa`, `Compute asymptotic standard errors for cumulative impulse response         coeff`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 411`** (2 nodes): `ExpTransf_gen`, `Distribution based on log/exp transformation      the constructor can be called`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 413`** (2 nodes): `LogTransf_gen`, `Distribution based on log/exp transformation      the constructor can be called`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 416`** (2 nodes): `NAAction`, `Get the NA action for the formula engine.          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 417`** (1 nodes): `Akaike Information Criterion         -2 * `llf` + 2 * (`df_model` + 1)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 418`** (2 nodes): `Evaluate the log-likelihood function.          Parameters         ----------`, `Evaluate the score function (first derivative of loglike).          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 432`** (1 nodes): `Transforms`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 434`** (2 nodes): `univariate Skew-Normal distribution of Azzalini      class follows scipy.stats.d`, `SkewNorm2_gen`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 436`** (2 nodes): `Calculate the difference between the log likelihood of mu_test and a         spe`, `Returns - 2 x log-likelihood ratio, p-value and weights         for a hypothesis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 437`** (2 nodes): `Calculate the difference between the log likelihood ratio at skew         and a`, `Returns  -2 x log-likelihood and p-value for the hypothesized         skewness.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 438`** (2 nodes): `Used to determine the confidence intervals for the variance          It calls te`, `Returns  -2 x log-likelihood ratio and the p-value for the         hypothesized`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 439`** (1 nodes): `Initialization methods for states of exponential smoothing models`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 440`** (2 nodes): `Get the list of categories for a factor.          Parameters         ----------`, `Get the contrast matrix for a term and factor.          Parameters         -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 445`** (2 nodes): `approximate pointwise variance for kernel density          not verified`, `approximate pointwise confidence interval for kernel density          The confid`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 447`** (2 nodes): `Compute significance bounds for the CUSUM statistic          Parameters`, `r"""         Plot the CUSUM statistic and significance bounds          Parameter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 448`** (2 nodes): `Compute significance bounds for the CUSUM of squares statistic          Paramete`, `r"""         Plot the CUSUM of squares statistic and significance bounds`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 450`** (2 nodes): `Combine details of impacts from news and revisions into one table          Param`, `Get impacts from news and revisions on variables of interest          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 459`** (2 nodes): `variance of data given ddof          Parameters         ----------         ddof`, `standard deviation of data with given ddof          Parameters         ---------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 461`** (2 nodes): `Apply function to each column, by group          Parameters         ----------`, `Apply function to each column, by group          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 463`** (1 nodes): `Created on Thu Aug 30 12:26:38 2012 Author: Josef Perktold   function jc =  c_sj`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 464`** (1 nodes): `Created on Mon Dec 14 19:53:25 2009  Author: josef-pktd  generate arma sample us`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 467`** (1 nodes): `Initialize dates          Parameters         ----------         dates : array_li`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 469`** (2 nodes): `r"""     Subroutine for orthogonal and oblique rotation of the matrix :math:`A``, `rotate_factors()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 470`** (2 nodes): `dot_plot()`, `Dot plotting (also known as forest and blobbogram)      Produce a dotplot simila`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 471`** (2 nodes): `rainbow()`, `Return a list of colors sampled at equal intervals over the spectrum      Parame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 472`** (2 nodes): `Plot a Tukey HSD pairwise mean-comparison confidence interval chart      Paramet`, `tukeyplot()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 473`** (2 nodes): `Cosine2`, `Cosine2 Kernel      K(u) = 1 + cos(2 * pi * u) between -0.5 and 0.5      Note: t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 474`** (2 nodes): `Cosine`, `Cosine Kernel      K(u) = pi/4 cos(0.5 * pi * u) between -1.0 and 1.0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 475`** (2 nodes): `combine_indices()`, `Use np.unique to get integer group indices for product, intersection      Parame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 476`** (1 nodes): `_make_endog_names()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 477`** (1 nodes): `_make_exog_names()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 478`** (1 nodes): `Labels for covariance matrices          In multidimensional models, each dimensi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 479`** (1 nodes): `PatsyData`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 480`** (1 nodes): `TODO: how to add constraints?          Something like         sm.add_constraint(`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 481`** (1 nodes): `Platform detection flags used across statsmodels`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 482`** (1 nodes): `Dow-Jones Utilities Index, Aug.28--Dec.18, 1972  Dataset described in [1]_ and i`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 483`** (1 nodes): `Lake level of Lake Huron in feet (reduced by 570), 1875--1972  Dataset described`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 484`** (1 nodes): `57 consecutive daily overshorts from an underground gasoline tank at a filling s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 485`** (1 nodes): `The number of car drivers killed or seriously injured monthly in Great Britain f`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 486`** (1 nodes): `Plot observed versus predicted frequencies for entire sample`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 487`** (1 nodes): `Moment test for binned probabilities using OPG          Parameters         -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 488`** (1 nodes): `Hosmer-Lemeshow style test for count data          Note, this does not take into`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 489`** (1 nodes): `Test for excess (over or under) dispersion in Poisson          Returns         -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 490`** (1 nodes): `Test for excess zeros, zero inflation or deflation          Parameters         -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 491`** (1 nodes): `temporary location for enhancements to scipy.stats  includes ^^^^^^^^  * Per Bro`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 492`** (1 nodes): `standard deviation, square root of diagonal elements of sigma`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 493`** (1 nodes): `Get a mask indicating if data are missing.          Returns         -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 494`** (1 nodes): `Returns the engine-specific model specification type.          Returns         -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 495`** (1 nodes): `Remove intercept from Patsy terms.          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 496`** (1 nodes): `Get the model specification. Only available after calling get_arrays.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 497`** (1 nodes): `Yield index splits into train and test sets          Parameters         --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 498`** (1 nodes): `Evaluate second derivative of penalty with respect to params          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 499`** (1 nodes): `Evaluate derivative of penalty with respect to params          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 500`** (1 nodes): `Evaluate penalization at params          Parameters         ----------         p`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 501`** (1 nodes): `Penalty matrix for generalized additive model          Parameters         ------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 503`** (1 nodes): `. regress totemp gnpdefl gnp unemp armed pop year        Source |       SS`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 504`** (1 nodes): `Summary Table formatting  This is here to help keep the formatting consistent ac`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 507`** (1 nodes): `Loglikelihood at each observation, computed from recursive residuals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 508`** (1 nodes): `Loglikelihood defined by recursive residuals, equivalent to OLS`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 509`** (1 nodes): `Sum of squared recursive residuals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 510`** (1 nodes): `Centered total sum of squares`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 511`** (1 nodes): `Uncentered total sum of squares`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 512`** (1 nodes): `Explained sum of squares`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 513`** (1 nodes): `Mean squared error of the model`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 514`** (1 nodes): `Mean squared error of the residuals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 515`** (1 nodes): `Total mean squared error`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 516`** (2 nodes): `copy_index_vector()`, `Reorder the elements of a time-varying vector where all non-index     values are`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 517`** (2 nodes): `copy_missing_matrix()`, `Copy the rows or columns of a time-varying matrix where all non-missing     valu`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 518`** (2 nodes): `copy_missing_vector()`, `Reorder the elements of a time-varying vector where all non-missing     values a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 519`** (2 nodes): `diff()`, `r"""     Difference a series simply and/or seasonally along the zero-th axis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 520`** (2 nodes): `get_impact_dates()`, `Compute start/end periods and an index, often for impacts of data updates      P`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 521`** (2 nodes): `prepare_exog()`, `Standardize the shape of an exog array and compute its number of columns      Pa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 522`** (2 nodes): `prepare_trend_data()`, `Construct the trend data array associated with a given trend polynomial      Par`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 523`** (2 nodes): `prepare_trend_spec()`, `Translate a trend specification into a polynomial trend and its order      Param`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 524`** (2 nodes): `Set the compatibility mode      Parameters     ----------     compatibility : bo`, `set_mode()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 525`** (2 nodes): `Validate the shape of a possibly time-varying matrix, or raise an exception`, `validate_matrix_shape()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 526`** (2 nodes): `Validate the shape of a possibly time-varying vector, or raise an exception`, `validate_vector_shape()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 527`** (2 nodes): `Reorder the elements of a time-varying vector where all non-missing     values a`, `reorder_missing_vector()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 528`** (2 nodes): `Compute condition while protecting from LinAlgError`, `_safe_cond()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 529`** (1 nodes): `column names for summary table`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 530`** (1 nodes): `temporary location for enhancements to scipy.stats  includes ^^^^^^^^  * Per Bro`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 531`** (1 nodes): `This file is automatically generated by littlefors_critical_values.py  Do not di`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 532`** (1 nodes): `Update self.params with supplied args          Only valid when Substitution was`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 533`** (1 nodes): `Typing aliases used by statsmodels`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 534`** (1 nodes): `Create an identical deterministic process with a different index          Parame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 535`** (1 nodes): `The index of the process`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 536`** (1 nodes): `The deterministic terms included in the process`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 537`** (1 nodes): `tuple of attributes that are used for equality comparison`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 538`** (1 nodes): `Produce deterministic trends for in-sample fitting          Parameters         -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 539`** (1 nodes): `Flag indicating whether the values produced are dummy variables`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 540`** (1 nodes): `Produce deterministic trends for out-of-sample forecasts          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 541`** (1 nodes): `A meaningful string representation of the term`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 542`** (1 nodes): `Create a TimeTrend from a string description.          Provided for compatibilit`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 543`** (1 nodes): `The period of the seasonality`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 544`** (1 nodes): `The seasonal index of the first observation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 545`** (1 nodes): `Construct a seasonality directly from an index using its frequency.          Par`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 546`** (1 nodes): `functions and classes time series analysis   Status ------ work in progress  ari`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `OLS` connect `Community 12` to `Community 0`, `Community 87`, `Community 101`, `Community 72`, `Community 166`, `Community 8`, `Community 83`, `Community 30`, `Community 34`, `Community 42`, `Community 11`, `Community 78`, `Community 58`, `Community 216`, `Community 2`, `Community 10`, `Community 26`, `Community 5`, `Community 290`, `Community 46`, `Community 92`, `Community 131`, `Community 1`, `Community 6`, `Community 75`, `Community 123`, `Community 208`, `Community 19`, `Community 3`, `Community 225`, `Community 227`, `Community 17`, `Community 13`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Why does `Appender` connect `Community 5` to `Community 0`, `Community 8`, `Community 138`, `Community 49`, `Community 41`, `Community 125`, `Community 114`, `Community 27`, `Community 36`, `Community 3`, `Community 54`, `Community 139`, `Community 22`, `Community 37`, `Community 158`, `Community 81`, `Community 152`, `Community 116`, `Community 317`, `Community 435`, `Community 288`, `Community 263`, `Community 380`, `Community 21`, `Community 30`, `Community 28`, `Community 11`, `Community 10`, `Community 12`, `Community 53`, `Community 2`, `Community 26`, `Community 170`, `Community 203`, `Community 507`, `Community 508`, `Community 509`, `Community 510`, `Community 511`, `Community 512`, `Community 513`, `Community 514`, `Community 515`, `Community 447`, `Community 448`, `Community 73`, `Community 277`, `Community 131`, `Community 1`, `Community 32`, `Community 6`, `Community 205`, `Community 451`, `Community 325`, `Community 326`, `Community 524`, `Community 525`, `Community 526`, `Community 422`, `Community 527`, `Community 517`, `Community 518`, `Community 516`, `Community 521`, `Community 523`, `Community 522`, `Community 528`, `Community 520`, `Community 519`, `Community 398`, `Community 79`, `Community 19`, `Community 428`, `Community 145`, `Community 93`, `Community 59`, `Community 71`, `Community 132`, `Community 310`, `Community 537`, `Community 535`, `Community 536`, `Community 406`, `Community 534`, `Community 299`, `Community 542`, `Community 543`, `Community 544`, `Community 545`, `Community 539`, `Community 538`, `Community 540`, `Community 541`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Why does `ValueWarning` connect `Community 10` to `Community 11`, `Community 3`, `Community 2`, `Community 9`, `Community 20`, `Community 182`, `Community 467`, `Community 16`, `Community 240`, `Community 126`, `Community 199`, `Community 265`, `Community 266`, `Community 267`, `Community 268`, `Community 353`, `Community 306`, `Community 60`, `Community 202`, `Community 22`, `Community 30`, `Community 5`, `Community 6`, `Community 12`, `Community 53`, `Community 26`, `Community 15`, `Community 46`, `Community 56`, `Community 74`, `Community 179`, `Community 44`, `Community 1`, `Community 7`, `Community 4`, `Community 144`, `Community 69`, `Community 400`, `Community 98`, `Community 308`, `Community 401`, `Community 67`, `Community 17`, `Community 88`, `Community 52`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 1089 inferred relationships involving `Appender` (e.g. with `ARDL` and `ARDLOrderSelectionResults`) actually correct?**
  _`Appender` has 1089 INFERRED edges - model-reasoned connections that need verification._
- **Are the 899 inferred relationships involving `FormulaManager` (e.g. with `LinearConstraints` and `Created on Thu May 15 16:36:05 2014  Author: Josef Perktold License: BSD-3`) actually correct?**
  _`FormulaManager` has 899 INFERRED edges - model-reasoned connections that need verification._
- **Are the 843 inferred relationships involving `OLS` (e.g. with `ARDL` and `ARDLOrderSelectionResults`) actually correct?**
  _`OLS` has 843 INFERRED edges - model-reasoned connections that need verification._
- **Are the 835 inferred relationships involving `ValueWarning` (e.g. with `GenericLikelihoodModel` and `GenericLikelihoodModelResults`) actually correct?**
  _`ValueWarning` has 835 INFERRED edges - model-reasoned connections that need verification._