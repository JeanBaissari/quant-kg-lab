# Graph Report - knowledge_graphs/quantstats/repo/quantstats  (2026-08-13)

## Corpus Check
- Corpus is ~42,133 words - fits in a single context window. You may not need a graph.

## Summary
- 393 nodes · 531 edges · 51 communities detected
- Non-singleton communities: 48
- Extraction: EXTRACTED: 100.0%
- Edge kinds: calls: 141 · contains: 186 · imports_from: 5 · inherits: 5 · method: 7 · rationale_for: 187

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 12 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `fbd10da`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `stats.py` (81)
- `utils.py` (37)
- `wrappers.py` (22)
- `reports.py` (16)
- `core.py` (15)
- `_compat.py` (14)
- `_get_utils()` (14)
- `html()` (11)
- `MonteCarloResult` (10)
- `_get_stats()` (10)

## Surprising Connections (you probably didn't know these)
- `cvar()` --calls--> `conditional_value_at_risk()`  [EXTRACTED]
  stats.py → stats.py  _Bridges community 1 → community 13_
- `probabilistic_ratio()` --calls--> `adjusted_sortino()`  [EXTRACTED]
  stats.py → stats.py  _Bridges community 10 → community 14_
- `probabilistic_ratio()` --calls--> `sharpe()`  [EXTRACTED]
  stats.py → stats.py  _Bridges community 10 → community 15_
- `sortino()` --calls--> `autocorr_penalty()`  [EXTRACTED]
  stats.py → stats.py  _Bridges community 14 → community 15_
- `DataValidationError` --inherits--> `QuantStatsError`  [EXTRACTED]
  utils.py → utils.py  _Bridges community 22 → community 12_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (40): daily_returns(), distribution(), drawdown(), drawdowns_periods(), earnings(), _get_stats(), _get_utils(), histogram() (+32 more)

### Community 1 - "Community 1"
Cohesion: 0.07
Nodes (32): cagr(), calmar(), comp(), cvar(), exposure(), _get_baseline_value(), greeks(), max_drawdown() (+24 more)

### Community 2 - "Community 2"
Cohesion: 0.14
Nodes (29): basic(), _calc_dd(), _download_html(), _embed_figure(), full(), _get_plots(), _get_stats(), _get_trading_periods() (+21 more)

### Community 3 - "Community 3"
Cohesion: 0.11
Nodes (27): format_cur_axis(), format_pct_axis(), _get_colors(), _get_stats(), plot_distribution(), plot_histogram(), plot_longest_drawdowns(), plot_montecarlo() (+19 more)

### Community 4 - "Community 4"
Cohesion: 0.09
Nodes (24): avg_loss(), avg_win(), common_sense_ratio(), cpc_index(), kelly_criterion(), payoff_ratio(), profit_factor(), Calculate the risk of ruin (probability of losing all capital).      This functi (+16 more)

### Community 5 - "Community 5"
Cohesion: 0.12
Nodes (20): get_datetime_accessor(), get_frequency_alias(), get_string_accessor(), handle_pandas_warnings(), normalize_timezone(), Safe concatenation that handles pandas version differences.      This function p, Safe append operation using pd.concat.      DataFrame.append() was removed in pa, Safe frequency conversion for time series data.      This function converts time (+12 more)

### Community 6 - "Community 6"
Cohesion: 0.11
Nodes (11): MonteCarloResult, Probability of exceeding the bust (drawdown) threshold.          Returns, Probability of reaching the goal (return) threshold.          Returns         --, Get the p-th percentile path across all simulations.          Parameters, Get lower and upper bounds for a confidence interval.          Parameters, Plot all simulation paths with the original path highlighted.          Parameter, Run Monte Carlo simulation by shuffling returns.      This function creates mult, Container for Monte Carlo simulation results.      This class holds the results (+3 more)

### Community 7 - "Community 7"
Cohesion: 0.11
Nodes (18): avg_return(), best(), compare(), compsum(), consecutive_losses(), consecutive_wins(), distribution(), Analyze return distributions across different time periods.      This function c (+10 more)

### Community 8 - "Community 8"
Cohesion: 0.11
Nodes (18): _count_consecutive(), _file_stream(), _flatten_dataframe(), _in_notebook(), _mtd(), multi_shift(), _pandas_current_month(), Filter dataframe to month-to-date data      Parameters     ----------     df : p (+10 more)

### Community 9 - "Community 9"
Cohesion: 0.12
Nodes (16): handle_numpy_warnings(), Context manager to handle numpy warnings appropriately.      This function retur, Safe percentile calculation.      This function provides a wrapper around np.per, Safe nanpercentile calculation that ignores NaN values.      This function provi, Safe quantile calculation.      This function provides a wrapper around np.quant, Safe random seed setting for numpy.      This function provides a unified interf, Safe datetime64 unit conversion.      This function provides a safe way to conve, Safe numpy operations with deprecation handling.      This function provides a u (+8 more)

### Community 10 - "Community 10"
Cohesion: 0.17
Nodes (12): kurtosis(), probabilistic_adjusted_sortino_ratio(), probabilistic_ratio(), probabilistic_sharpe_ratio(), probabilistic_sortino_ratio(), Calculate the probabilistic ratio for a given base metric.      This function co, Calculate the Probabilistic Sharpe Ratio (PSR).      This function computes the, Calculate the Probabilistic Sortino Ratio.      This function computes the proba (+4 more)

### Community 11 - "Community 11"
Cohesion: 0.17
Nodes (12): _clear_cache_if_full(), exponential_stdev(), _generate_cache_key(), _prepare_returns(), Generate a cache key for the _prepare_returns function      Parameters     -----, Clear cache if it exceeds maximum size      Uses a simple FIFO strategy, keeping, Calculate simple arithmetic returns from price series      Parameters     ------, Calculate exponential weighted standard deviation (volatility) of returns      P (+4 more)

### Community 12 - "Community 12"
Cohesion: 0.22
Nodes (9): Exception, BenchmarkError, CalculationError, PlottingError, QuantStatsError, Base exception class for QuantStats, Raised when a calculation fails, Raised when plotting operations fail (+1 more)

### Community 13 - "Community 13"
Cohesion: 0.25
Nodes (8): conditional_value_at_risk(), expected_shortfall(), Calculate the daily Value at Risk (VaR).      VaR estimates the maximum expected, Calculate the daily Value at Risk (VaR).      This is a shorthand function for v, Calculate the Conditional Value at Risk (CVaR), also known as Expected Shortfall, Calculate the Expected Shortfall (ES), also known as CVaR.      This is a shorth, value_at_risk(), var()

### Community 14 - "Community 14"
Cohesion: 0.33
Nodes (6): adjusted_sortino(), Calculate the Smart Sortino ratio (Sortino with autocorrelation penalty).      T, Calculate Jack Schwager's adjusted Sortino ratio.      This version of the Sorti, Calculate the Sortino ratio of excess returns.      The Sortino ratio is similar, smart_sortino(), sortino()

### Community 15 - "Community 15"
Cohesion: 0.33
Nodes (6): autocorr_penalty(), Calculate autocorrelation penalty for risk-adjusted metrics.      This function, Calculate the Sharpe ratio of excess returns.      The Sharpe ratio measures ris, Calculate the Smart Sharpe ratio (Sharpe with autocorrelation penalty).      Thi, sharpe(), smart_sharpe()

### Community 16 - "Community 16"
Cohesion: 0.33
Nodes (6): expected_return(), geometric_mean(), ghpr(), Calculate the expected return (geometric mean) for a given period.      This fun, Calculate geometric mean of returns.      This is a shorthand function for expec, Calculate Geometric Holding Period Return.      This is a shorthand function for

### Community 17 - "Community 17"
Cohesion: 0.33
Nodes (5): download_returns(), make_index(), _prepare_benchmark(), Download returns data for a given ticker using yfinance      Parameters     ----, Makes an index out of the given tickers and weights.     Optionally you can pass

### Community 18 - "Community 18"
Cohesion: 0.33
Nodes (6): make_portfolio(), _prepare_prices(), Convert returns series to price data      Parameters     ----------     returns, Convert return data into prices and perform cleanup      Parameters     --------, Calculate compounded value of portfolio from returns      Parameters     -------, to_prices()

### Community 19 - "Community 19"
Cohesion: 0.50
Nodes (4): montecarlo(), montecarlo_drawdown(), Run Monte Carlo simulation by shuffling returns.      This function creates mult, Distribution of maximum drawdowns across Monte Carlo simulations.      This func

### Community 20 - "Community 20"
Cohesion: 0.50
Nodes (4): r2(), r_squared(), Calculate the R-squared (coefficient of determination) versus benchmark.      R-, Calculate the R-squared (coefficient of determination) versus benchmark.      Th

### Community 21 - "Community 21"
Cohesion: 0.50
Nodes (4): aggregate_returns(), group_returns(), Summarize returns by grouping criteria      Parameters     ----------     return, Aggregate returns based on specified time periods      Parameters     ----------

### Community 22 - "Community 22"
Cohesion: 0.50
Nodes (4): DataValidationError, Raised when input data validation fails, Validate input data for QuantStats functions      Parameters     ----------, validate_input()

### Community 23 - "Community 23"
Cohesion: 0.50
Nodes (4): log_returns(), Shorthand for to_log_returns function      Parameters     ----------     returns, Convert returns series to log returns      Parameters     ----------     returns, to_log_returns()

### Community 24 - "Community 24"
Cohesion: 0.67
Nodes (2): extend_pandas(), Extends pandas by exposing methods to be used like:     df.sharpe(), df.best('da

### Community 25 - "Community 25"
Cohesion: 1.00
Nodes (2): drawdown_details(), Calculate detailed drawdown statistics for each drawdown period.      This funct

### Community 26 - "Community 26"
Cohesion: 1.00
Nodes (2): gain_to_pain_ratio(), Calculate Jack Schwager's Gain-to-Pain Ratio (GPR).      This ratio measures the

### Community 27 - "Community 27"
Cohesion: 1.00
Nodes (2): implied_volatility(), Calculate implied volatility using log returns.      This function computes vola

### Community 28 - "Community 28"
Cohesion: 1.00
Nodes (2): information_ratio(), Calculate the Information Ratio.      The Information Ratio measures the risk-ad

### Community 29 - "Community 29"
Cohesion: 1.00
Nodes (2): montecarlo_cagr(), Distribution of CAGR across Monte Carlo simulations.      This function runs Mon

### Community 30 - "Community 30"
Cohesion: 1.00
Nodes (2): montecarlo_sharpe(), Distribution of Sharpe ratios across Monte Carlo simulations.      This function

### Community 31 - "Community 31"
Cohesion: 1.00
Nodes (2): monthly_returns(), Calculate monthly returns in a pivot table format.      This function creates a

### Community 32 - "Community 32"
Cohesion: 1.00
Nodes (2): omega(), Calculate the Omega ratio of a strategy.      The Omega ratio measures the proba

### Community 33 - "Community 33"
Cohesion: 1.00
Nodes (2): outlier_loss_ratio(), Calculate the outlier losers ratio.      This function computes the ratio of the

### Community 34 - "Community 34"
Cohesion: 1.00
Nodes (2): outlier_win_ratio(), Calculate the outlier winners ratio.      This function computes the ratio of th

### Community 35 - "Community 35"
Cohesion: 1.00
Nodes (2): outliers(), Identify and return outlier returns above a specified quantile.      This functi

### Community 36 - "Community 36"
Cohesion: 1.00
Nodes (2): pct_rank(), Calculate the percentile rank of prices over a rolling window.      This functio

### Community 37 - "Community 37"
Cohesion: 1.00
Nodes (2): profit_ratio(), Calculate the profit ratio (win ratio / loss ratio).      This function measures

### Community 38 - "Community 38"
Cohesion: 1.00
Nodes (2): Calculate rolling Sortino ratio over a specified window.      This function comp, rolling_sortino()

### Community 39 - "Community 39"
Cohesion: 1.00
Nodes (2): Calculate the risk-return ratio (mean return / standard deviation).      This fu, risk_return_ratio()

### Community 40 - "Community 40"
Cohesion: 1.00
Nodes (2): Calculate rolling Greeks (alpha and beta) over time.      This function calculat, rolling_greeks()

### Community 41 - "Community 41"
Cohesion: 1.00
Nodes (2): Remove outlier returns above a specified quantile.      This function filters ou, remove_outliers()

### Community 42 - "Community 42"
Cohesion: 1.00
Nodes (2): Calculate volatility (standard deviation) of returns.      This function compute, volatility()

### Community 43 - "Community 43"
Cohesion: 1.00
Nodes (2): Calculate rolling volatility over a specified window.      This function compute, rolling_volatility()

### Community 44 - "Community 44"
Cohesion: 1.00
Nodes (2): _pandas_date(), Filter dataframe to specific dates      Parameters     ----------     df : pd.Da

### Community 45 - "Community 45"
Cohesion: 1.00
Nodes (2): _qtd(), Filter dataframe to quarter-to-date data      Parameters     ----------     df :

### Community 46 - "Community 46"
Cohesion: 1.00
Nodes (2): Rebase all series to a given intial base.     This makes comparing/plotting diff, rebase()

### Community 47 - "Community 47"
Cohesion: 1.00
Nodes (2): Round value to closest resolution      Parameters     ----------     val : float, _round_to_closest()

## Knowledge Gaps
- **186 isolated node(s):** `Extends pandas by exposing methods to be used like:     df.sharpe(), df.best('da`, `Get the correct frequency alias for current pandas version.      This function m`, `Normalize timezone information for consistent comparisons.          If data has`, `Safe resample operation that works with all pandas versions.      This function`, `Safe concatenation that handles pandas version differences.      This function p` (+181 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 24`** (2 nodes): `extend_pandas()`, `Extends pandas by exposing methods to be used like:     df.sharpe(), df.best('da`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (2 nodes): `drawdown_details()`, `Calculate detailed drawdown statistics for each drawdown period.      This funct`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (2 nodes): `gain_to_pain_ratio()`, `Calculate Jack Schwager's Gain-to-Pain Ratio (GPR).      This ratio measures the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (2 nodes): `implied_volatility()`, `Calculate implied volatility using log returns.      This function computes vola`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (2 nodes): `information_ratio()`, `Calculate the Information Ratio.      The Information Ratio measures the risk-ad`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (2 nodes): `montecarlo_cagr()`, `Distribution of CAGR across Monte Carlo simulations.      This function runs Mon`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (2 nodes): `montecarlo_sharpe()`, `Distribution of Sharpe ratios across Monte Carlo simulations.      This function`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (2 nodes): `monthly_returns()`, `Calculate monthly returns in a pivot table format.      This function creates a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (2 nodes): `omega()`, `Calculate the Omega ratio of a strategy.      The Omega ratio measures the proba`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (2 nodes): `outlier_loss_ratio()`, `Calculate the outlier losers ratio.      This function computes the ratio of the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (2 nodes): `outlier_win_ratio()`, `Calculate the outlier winners ratio.      This function computes the ratio of th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (2 nodes): `outliers()`, `Identify and return outlier returns above a specified quantile.      This functi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (2 nodes): `pct_rank()`, `Calculate the percentile rank of prices over a rolling window.      This functio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (2 nodes): `profit_ratio()`, `Calculate the profit ratio (win ratio / loss ratio).      This function measures`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (2 nodes): `Calculate rolling Sortino ratio over a specified window.      This function comp`, `rolling_sortino()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (2 nodes): `Calculate the risk-return ratio (mean return / standard deviation).      This fu`, `risk_return_ratio()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (2 nodes): `Calculate rolling Greeks (alpha and beta) over time.      This function calculat`, `rolling_greeks()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (2 nodes): `Remove outlier returns above a specified quantile.      This function filters ou`, `remove_outliers()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (2 nodes): `Calculate volatility (standard deviation) of returns.      This function compute`, `volatility()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (2 nodes): `Calculate rolling volatility over a specified window.      This function compute`, `rolling_volatility()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (2 nodes): `_pandas_date()`, `Filter dataframe to specific dates      Parameters     ----------     df : pd.Da`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (2 nodes): `_qtd()`, `Filter dataframe to quarter-to-date data      Parameters     ----------     df :`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (2 nodes): `Rebase all series to a given intial base.     This makes comparing/plotting diff`, `rebase()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (2 nodes): `Round value to closest resolution      Parameters     ----------     val : float`, `_round_to_closest()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `QuantStatsError` connect `Community 12` to `Community 8`, `Community 22`?**
  _High betweenness centrality (0.008) - this node is a cross-community bridge._
- **Why does `_prepare_returns()` connect `Community 11` to `Community 8`, `Community 18`, `Community 17`, `Community 23`?**
  _High betweenness centrality (0.005) - this node is a cross-community bridge._
- **Why does `probabilistic_ratio()` connect `Community 10` to `Community 7`, `Community 14`, `Community 15`?**
  _High betweenness centrality (0.005) - this node is a cross-community bridge._
- **What connects `Extends pandas by exposing methods to be used like:     df.sharpe(), df.best('da`, `Get the correct frequency alias for current pandas version.      This function m`, `Normalize timezone information for consistent comparisons.          If data has` to the rest of the system?**
  _186 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.07804878048780488 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.06653225806451613 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.14022988505747128 - nodes in this community are weakly interconnected._