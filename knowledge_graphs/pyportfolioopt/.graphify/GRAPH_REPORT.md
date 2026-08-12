# Graph Report - knowledge_graphs/pyportfolioopt/repo/pypfopt  (2026-08-12)

## Corpus Check
- Corpus is ~19,105 words - fits in a single context window. You may not need a graph.

## Summary
- 332 nodes · 512 edges · 15 communities detected
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 73 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: rationale_for: 143 · calls: 115 · method: 110 · uses: 73 · contains: 55 · inherits: 10 · imports_from: 6


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 18 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `a6638d2`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `EfficientFrontier` - 42 edges
2. `OptimizationError` - 25 edges
3. `InstantiationError` - 24 edges
4. `CLA` - 23 edges
5. `BlackLittermanModel` - 18 edges
6. `BaseConvexOptimizer` - 17 edges
7. `EfficientCDaR` - 16 edges
8. `EfficientCVaR` - 15 edges
9. `EfficientSemivariance` - 13 edges
10. `BaseOptimizer` - 11 edges

## Surprising Connections (you probably didn't know these)
- `BaseConvexOptimizer` --uses--> `InstantiationError`  [INFERRED]
  base/_base_optimizer.py → exceptions.py
- `BaseConvexOptimizer` --uses--> `OptimizationError`  [INFERRED]
  base/_base_optimizer.py → exceptions.py
- `BaseOptimizer` --uses--> `InstantiationError`  [INFERRED]
  base/_base_optimizer.py → exceptions.py
- `BaseOptimizer` --uses--> `OptimizationError`  [INFERRED]
  base/_base_optimizer.py → exceptions.py
- `The ``base_optimizer`` module houses the parent classes ``BaseOptimizer`` from w` --uses--> `InstantiationError`  [INFERRED]
  base/_base_optimizer.py → exceptions.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (31): BaseConvexOptimizer, BaseOptimizer, _flatten(), _get_all_args(), portfolio_performance(), The ``base_optimizer`` module houses the parent classes ``BaseOptimizer`` from w, Utility method to save weights to a text file.          Parameters         -----, The BaseConvexOptimizer contains many private variables for use by     ``cvxpy`` (+23 more)

### Community 1 - "Community 1"
Cohesion: 0.08
Nodes (29): corr_to_cov(), cov_to_corr(), CovarianceShrinkage, exp_cov(), fix_nonpositive_semidefinite(), _is_positive_semidefinite(), min_cov_determinant(), _pair_exp_cov() (+21 more)

### Community 2 - "Community 2"
Cohesion: 0.09
Nodes (17): BlackLittermanModel, market_implied_prior_returns(), market_implied_risk_aversion(), The ``black_litterman`` module houses the BlackLittermanModel class, which gener, A BlackLittermanModel object (inheriting from BaseOptimizer) contains requires, Parameters         ----------         cov_matrix : pd.DataFrame or np.ndarray, r"""     Compute the prior estimate of returns implied by the market weights., Given a collection (dict or series) of absolute views, construct         the app (+9 more)

### Community 3 - "Community 3"
Cohesion: 0.11
Nodes (9): CLA, Helper method to map None to float infinity.          Parameters         -------, Instance variables:      - Inputs:          - ``n_assets`` - int         - ``tic, Extract a submatrix from the given matrix using specified row and column indices, Maximise the Sharpe ratio.          Returns         -------         OrderedDict, Minimise volatility.          Returns         -------         OrderedDict, Efficiently compute the entire efficient frontier          Parameters         --, After optimising, calculate (and optionally print) the performance of the optima (+1 more)

### Community 4 - "Community 4"
Cohesion: 0.16
Nodes (21): _ef_default_returns_range(), _get_plotly(), _import_matplotlib(), _plot_cla(), plot_covariance(), plot_dendrogram(), _plot_ef(), plot_efficient_frontier() (+13 more)

### Community 5 - "Community 5"
Cohesion: 0.12
Nodes (11): BaseOptimizer, The ``cla`` module houses the CLA class, which generates optimal portfolios usin, HRPOpt, The ``hierarchical_portfolio`` module seeks to implement one of the recent advan, Sort clustered items by distance          Parameters         ----------, Given the clusters, compute the portfolio that minimises risk by         recursi, Construct a hierarchical risk parity portfolio, using Scipy hierarchical cluster, After optimising, calculate (and optionally print) the performance of the optima (+3 more)

### Community 6 - "Community 6"
Cohesion: 0.12
Nodes (8): EfficientCDaR, The ``efficient_cdar`` submodule houses the EfficientCDaR class, which generates, Minimise portfolio CDaR (see docs for further explanation).          Parameters, Minimise CDaR for a given target return.          Parameters         ----------, The EfficientCDaR class allows for optimisation along the mean-CDaR frontier, us, Maximise return for a target CDaR.         The resulting portfolio will have a C, After optimising, calculate (and optionally print) the performance of the optima, Parameters         ----------         expected_returns : pd.Series, list, or np.

### Community 7 - "Community 7"
Cohesion: 0.14
Nodes (19): ex_ante_tracking_error(), ex_post_tracking_error(), L2_reg(), _objective_value(), portfolio_return(), portfolio_variance(), quadratic_utility(), The ``objective_functions`` module provides optimization objectives, including t (+11 more)

### Community 8 - "Community 8"
Cohesion: 0.11
Nodes (8): EfficientCVaR, The ``efficient_cvar`` submodule houses the EfficientCVaR class, which generates, Minimise portfolio CVaR (see docs for further explanation).          Parameters, Minimise CVaR for a given target return.          Parameters         ----------, The EfficientCVaR class allows for optimization along the mean-CVaR frontier, us, Maximise return for a target CVaR.         The resulting portfolio will have a C, After optimising, calculate (and optionally print) the performance of the optima, Parameters         ----------         expected_returns : pd.Series, list, or np.

### Community 9 - "Community 9"
Cohesion: 0.11
Nodes (10): EfficientSemivariance, The ``efficient_semivariance`` submodule houses the EfficientSemivariance class,, Minimise portfolio semivariance (see docs for further explanation).          Par, EfficientSemivariance objects allow for optimization along the mean-semivariance, Maximise the given quadratic utility, using portfolio semivariance instead, Maximise return for a target semideviation (downside standard deviation)., Minimise semideviation for a given target return.          Parameters         --, After optimising, calculate (and optionally print) the performance of the optima (+2 more)

### Community 10 - "Community 10"
Cohesion: 0.13
Nodes (9): BaseConvexOptimizer, EfficientFrontier, The ``efficient_frontier`` submodule houses the EfficientFrontier class, which g, Helper method to validate daily returns (needed for some efficient frontiers), An EfficientFrontier object (inheriting from BaseConvexOptimizer) contains multi, Minimise volatility.          Returns         -------         OrderedDict, Maximise the Sharpe Ratio. The result is also referred to as the tangency portfo, After optimising, calculate (and optionally print) the performance of the optima (+1 more)

### Community 11 - "Community 11"
Cohesion: 0.16
Nodes (10): DiscreteAllocation, get_latest_prices(), The ``discrete_allocation`` module contains the ``DiscreteAllocation`` class, wh, Utility function to remove zero positions (i.e with no shares being bought), Utility function to calculate and print RMSE error between discretised         w, Convert continuous weights into a discrete portfolio allocation         using a, A helper tool which retrieves the most recent asset prices from a dataframe of, Convert continuous weights into a discrete portfolio allocation         using in (+2 more)

### Community 12 - "Community 12"
Cohesion: 0.22
Nodes (14): capm_return(), _check_returns(), ema_historical_return(), mean_historical_return(), prices_from_returns(), The ``expected_returns`` module provides functions for estimating the expected r, Calculate annualised mean (daily) historical return from input (daily) asset pri, Calculate the exponentially-weighted mean of (daily) historical returns, giving (+6 more)

### Community 13 - "Community 13"
Cohesion: 0.22
Nodes (5): Helper method to make the weight sum constraint. If market neutral,         vali, Helper method to maximise return. This should not be used to optimize a portfoli, r"""         Maximise the given quadratic utility, i.e:          .. math::, Maximise return for a target risk. The resulting portfolio will have a volatilit, Calculate the 'Markowitz portfolio', minimising volatility for a given target re

### Community 14 - "Community 14"
Cohesion: 1.00
Nodes (1): The ``efficient_frontier`` module houses the EfficientFrontier class and its des

## Knowledge Gaps
- **100 isolated node(s):** `The ``black_litterman`` module houses the BlackLittermanModel class, which gener`, `r"""     Compute the prior estimate of returns implied by the market weights.`, `r"""     Calculate the market-implied risk-aversion parameter (i.e market price`, `A BlackLittermanModel object (inheriting from BaseOptimizer) contains requires`, `Parameters         ----------         cov_matrix : pd.DataFrame or np.ndarray` (+95 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 14`** (1 nodes): `The ``efficient_frontier`` module houses the EfficientFrontier class and its des`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `CLA` connect `Community 3` to `Community 5`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Why does `BlackLittermanModel` connect `Community 2` to `Community 5`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Why does `EfficientFrontier` connect `Community 10` to `Community 6`, `Community 8`, `Community 13`, `Community 9`, `Community 14`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Are the 26 inferred relationships involving `EfficientFrontier` (e.g. with `EfficientCDaR` and `The ``efficient_cdar`` submodule houses the EfficientCDaR class, which generates`) actually correct?**
  _`EfficientFrontier` has 26 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `OptimizationError` (e.g. with `BaseConvexOptimizer` and `BaseOptimizer`) actually correct?**
  _`OptimizationError` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `InstantiationError` (e.g. with `BaseConvexOptimizer` and `BaseOptimizer`) actually correct?**
  _`InstantiationError` has 21 INFERRED edges - model-reasoned connections that need verification._
- **What connects `The ``black_litterman`` module houses the BlackLittermanModel class, which gener`, `r"""     Compute the prior estimate of returns implied by the market weights.`, `r"""     Calculate the market-implied risk-aversion parameter (i.e market price` to the rest of the system?**
  _100 weakly-connected nodes found - possible documentation gaps or missing edges._