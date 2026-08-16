# Graph Report - knowledge_graphs/pyfolio/repo/pyfolio  (2026-08-13)

## Corpus Check
- Corpus is ~23,154 words - fits in a single context window. You may not need a graph.

## Summary
- 305 nodes · 361 edges · 61 communities detected
- Non-singleton communities: 60
- Extraction: EXTRACTED: 100.0%
- Edge kinds: calls: 58 · contains: 154 · imports_from: 13 · inherits: 1 · rationale_for: 135

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 15 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `4b901f6`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `timeseries.py` (40)
- `plotting.py` (38)
- `utils.py` (22)
- `_version.py` (20)
- `perf_attrib.py` (14)
- `tears.py` (11)
- `create_full_tear_sheet()` (9)
- `pos.py` (8)
- `round_trips.py` (8)
- `render()` (8)

## Surprising Connections (you probably didn't know these)
- `summarize_paths()` --calls--> `cum_returns()`  [EXTRACTED]
  timeseries.py → timeseries.py  _Bridges community 12 → community 10_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (36): check_intraday(), clip_returns_to_benchmark(), configure_legend(), detect_intraday(), estimate_intraday(), extract_rets_pos_txn_from_zipline(), format_asset(), get_symbol_rets() (+28 more)

### Community 1 - "Community 1"
Cohesion: 0.11
Nodes (22): _align_and_warn(), compute_exposures(), create_perf_attrib_stats(), _cumulative_returns_less_costs(), perf_attrib(), plot_alpha_returns(), plot_factor_contribution_to_perf(), plot_returns() (+14 more)

### Community 2 - "Community 2"
Cohesion: 0.19
Nodes (18): Exception, get_config(), get_keywords(), get_versions(), git_pieces_from_vcs(), git_versions_from_keywords(), NotThisMethod, plus_or_dot() (+10 more)

### Community 3 - "Community 3"
Cohesion: 0.13
Nodes (18): create_capacity_tear_sheet(), create_full_tear_sheet(), create_interesting_times_tear_sheet(), create_perf_attrib_tear_sheet(), create_position_tear_sheet(), create_returns_tear_sheet(), create_round_trip_tear_sheet(), create_simple_tear_sheet() (+10 more)

### Community 4 - "Community 4"
Cohesion: 0.13
Nodes (14): alpha(), alpha_beta(), annual_volatility(), calc_distribution_stats(), calmar_ratio(), downside_risk(), Determines the annual volatility of a strategy.      Parameters     ----------, Determines the Calmar ratio, or drawdown ratio, of a strategy.      Parameters (+6 more)

### Community 5 - "Community 5"
Cohesion: 0.15
Nodes (13): extract_pos(), get_long_short_pos(), get_max_median_position_concentration(), get_percent_alloc(), get_sector_exposures(), get_top_long_short_abs(), Extract position values from backtest object as returned by     get_backtest() o, # NOTE: Set name of DataFrame.columns to sid, to match the behavior (+5 more)

### Community 6 - "Community 6"
Cohesion: 0.18
Nodes (13): add_closing_transactions(), agg_all_long_short(), apply_sector_mappings_to_round_trips(), extract_round_trips(), gen_round_trip_stats(), _groupby_consecutive(), print_round_trip_stats(), Group transactions into "round trips". First, transactions are     grouped by da (+5 more)

### Community 7 - "Community 7"
Cohesion: 0.22
Nodes (10): apply_slippage_penalty(), daily_txns_with_bar_data(), days_to_liquidate_positions(), get_low_liquidity_transactions(), get_max_days_to_liquidate_by_ticker(), Finds the longest estimated liquidation time for each traded     name over the c, Sums the absolute value of shares traded in each name on each day.     Adds colu, For each traded name, find the daily transaction total that consumed     the gre (+2 more)

### Community 8 - "Community 8"
Cohesion: 0.24
Nodes (10): adjust_returns_for_slippage(), get_turnover(), get_txn_vol(), make_transaction_frame(), map_transaction(), Apply a slippage penalty for every dollar traded.      Parameters     ----------, - Value of purchases and sales divided     by either the actual gross book or th, Maps a single transaction row to a dictionary.      Parameters     ---------- (+2 more)

### Community 9 - "Community 9"
Cohesion: 0.20
Nodes (8): axes_style(), customize(), plot_annual_returns(), Create pyfolio default axes style context.      Under the hood, calls and return, Plots a bar graph of returns by year.      Parameters     ----------     returns, Decorator to set plotting context and axes style during function call., Prints some performance metrics of the strategy.      - Shows amount of time the, show_perf_stats()

### Community 10 - "Community 10"
Cohesion: 0.24
Nodes (10): cum_returns(), gen_drawdown_table(), get_max_drawdown(), get_max_drawdown_underwater(), get_top_drawdowns(), Compute cumulative returns from simple returns.      Parameters     ----------, Determines peak, valley, and recovery dates given an 'underwater'     DataFrame., Determines the maximum drawdown of a strategy.      Parameters     ---------- (+2 more)

### Community 11 - "Community 11"
Cohesion: 0.33
Nodes (6): annual_return(), common_sense_ratio(), Determines the ratio between the right (95%) and left tail (5%).      For exampl, Common sense ratio is the multiplication of the tail ratio and the     Gain-to-P, Determines the mean annual growth rate of returns.      Parameters     ---------, tail_ratio()

### Community 12 - "Community 12"
Cohesion: 0.33
Nodes (6): forecast_cone_bootstrap(), Gnerate alternate paths using available values from in-sample returns.      Para, Gnerate the upper and lower bounds of an n standard deviation     cone of foreca, Determines the upper and lower bounds of an n standard deviation     cone of for, simulate_paths(), summarize_paths()

### Community 13 - "Community 13"
Cohesion: 0.50
Nodes (3): deprecated(), Utilities for marking deprecated functions., Used to mark a function as deprecated.     Parameters     ----------     msg : s

### Community 14 - "Community 14"
Cohesion: 0.50
Nodes (4): aggregate_returns(), Aggregates returns by week, month, or year.      Parameters     ----------     r, Get value at risk (VaR).      Parameters     ----------     returns : pd.Series, value_at_risk()

### Community 15 - "Community 15"
Cohesion: 0.50
Nodes (4): beta(), Calculates beta.      Parameters     ----------     returns : pd.Series, Determines the rolling beta of a strategy.      Parameters     ----------     re, rolling_beta()

### Community 16 - "Community 16"
Cohesion: 0.50
Nodes (4): calc_bootstrap(), perf_stats_bootstrap(), Calculates various bootstrapped performance metrics of a strategy.      Paramete, Performs a bootstrap analysis on a user-defined function returning     a summary

### Community 17 - "Community 17"
Cohesion: 0.50
Nodes (4): gross_lev(), perf_stats(), Calculates the gross leverage of a strategy.      Parameters     ----------, Calculates various performance metrics of a strategy, for use in     plotting.sh

### Community 18 - "Community 18"
Cohesion: 1.00
Nodes (2): plot_cones(), Plots the upper and lower bounds of an n standard deviation     cone of forecast

### Community 19 - "Community 19"
Cohesion: 1.00
Nodes (2): plot_daily_turnover_hist(), Plots a histogram of daily turnover rates.      Parameters     ----------     tr

### Community 20 - "Community 20"
Cohesion: 1.00
Nodes (2): plot_daily_volume(), Plots trading volume per day vs. date.      Also displays all-time daily average

### Community 21 - "Community 21"
Cohesion: 1.00
Nodes (2): plot_drawdown_periods(), Plots cumulative returns highlighting top drawdown periods.      Parameters

### Community 22 - "Community 22"
Cohesion: 1.00
Nodes (2): plot_drawdown_underwater(), Plots how far underwaterr returns are over time, or plots current     drawdown v

### Community 23 - "Community 23"
Cohesion: 1.00
Nodes (2): plot_exposures(), Plots a cake chart of the long and short exposure.      Parameters     ---------

### Community 24 - "Community 24"
Cohesion: 1.00
Nodes (2): plot_gross_leverage(), Plots gross leverage versus date.      Gross leverage is the sum of long and sho

### Community 25 - "Community 25"
Cohesion: 1.00
Nodes (2): plot_holdings(), Plots total amount of stocks with an active position, either short     or long.

### Community 26 - "Community 26"
Cohesion: 1.00
Nodes (2): plot_long_short_holdings(), Plots total amount of stocks with an active position, breaking out     short and

### Community 27 - "Community 27"
Cohesion: 1.00
Nodes (2): plot_max_median_position_concentration(), Plots the max and median of long and short position concentrations     over the

### Community 28 - "Community 28"
Cohesion: 1.00
Nodes (2): plot_monthly_returns_dist(), Plots a distribution of monthly returns.      Parameters     ----------     retu

### Community 29 - "Community 29"
Cohesion: 1.00
Nodes (2): plot_monthly_returns_heatmap(), Plots a heatmap of returns by month.      Parameters     ----------     returns

### Community 30 - "Community 30"
Cohesion: 1.00
Nodes (2): plot_monthly_returns_timeseries(), Plots monthly returns as a timeseries.      Parameters     ----------     return

### Community 31 - "Community 31"
Cohesion: 1.00
Nodes (2): plot_perf_stats(), Create box plot of some performance metrics of the strategy.     The width of th

### Community 32 - "Community 32"
Cohesion: 1.00
Nodes (2): plot_prob_profit_trade(), Plots a probability distribution for the event of making     a profitable trade.

### Community 33 - "Community 33"
Cohesion: 1.00
Nodes (2): plot_return_quantiles(), Creates a box plot of daily, weekly, and monthly return     distributions.

### Community 34 - "Community 34"
Cohesion: 1.00
Nodes (2): plot_returns(), Plots raw returns over time.      Backtest returns are in green, and out-of-samp

### Community 35 - "Community 35"
Cohesion: 1.00
Nodes (2): plot_rolling_beta(), Plots the rolling 6-month and 12-month beta versus date.      Parameters     ---

### Community 36 - "Community 36"
Cohesion: 1.00
Nodes (2): plot_rolling_returns(), Plots cumulative rolling returns versus some benchmarks'.      Backtest returns

### Community 37 - "Community 37"
Cohesion: 1.00
Nodes (2): plot_rolling_sharpe(), Plots the rolling Sharpe ratio versus date.      Parameters     ----------     r

### Community 38 - "Community 38"
Cohesion: 1.00
Nodes (2): plot_rolling_volatility(), Plots the rolling volatility versus date.      Parameters     ----------     ret

### Community 39 - "Community 39"
Cohesion: 1.00
Nodes (2): plot_round_trip_lifetimes(), Plots timespans and directions of a sample of round trip trades.      Parameters

### Community 40 - "Community 40"
Cohesion: 1.00
Nodes (2): plot_sector_allocations(), Plots the sector exposures of the portfolio over time.      Parameters     -----

### Community 41 - "Community 41"
Cohesion: 1.00
Nodes (2): plot_slippage_sensitivity(), Plots curve relating per-dollar slippage to average annual returns.      Paramet

### Community 42 - "Community 42"
Cohesion: 1.00
Nodes (2): plot_slippage_sweep(), Plots equity curves at different per-dollar slippage assumptions.      Parameter

### Community 43 - "Community 43"
Cohesion: 1.00
Nodes (2): plot_turnover(), Plots turnover vs. date.      Turnover is the number of shares traded for a peri

### Community 44 - "Community 44"
Cohesion: 1.00
Nodes (2): plot_txn_time_hist(), Plots a histogram of transaction times, binning the times into     buckets of a

### Community 45 - "Community 45"
Cohesion: 1.00
Nodes (2): plotting_context(), Create pyfolio default plotting style context.      Under the hood, calls and re

### Community 46 - "Community 46"
Cohesion: 1.00
Nodes (2): Prints and/or plots the exposures of the top 10 held positions of     all time., show_and_plot_top_positions()

### Community 47 - "Community 47"
Cohesion: 1.00
Nodes (2): Prints information about the worst drawdown periods.      Prints peak dates, val, show_worst_drawdown_periods()

### Community 48 - "Community 48"
Cohesion: 1.00
Nodes (2): Prints the share of total PnL contributed by each     traded name.      Paramete, show_profit_attribution()

### Community 49 - "Community 49"
Cohesion: 2.00
Nodes (1): Wrapper module around seaborn to suppress warnings on import.  This should be re

### Community 50 - "Community 50"
Cohesion: 1.00
Nodes (2): extract_interesting_date_ranges(), Extracts returns based on interesting events. See     gen_date_range_interesting

### Community 51 - "Community 51"
Cohesion: 1.00
Nodes (2): max_drawdown(), Determines the maximum drawdown of a strategy.      Parameters     ----------

### Community 52 - "Community 52"
Cohesion: 1.00
Nodes (2): normalize(), Normalizes a returns timeseries based on the first value.      Parameters     --

### Community 53 - "Community 53"
Cohesion: 1.00
Nodes (2): omega_ratio(), Determines the Omega ratio of a strategy.      Parameters     ----------     ret

### Community 54 - "Community 54"
Cohesion: 1.00
Nodes (2): Determines the rolling volatility of a strategy.      Parameters     ----------, rolling_volatility()

### Community 55 - "Community 55"
Cohesion: 1.00
Nodes (2): Determines the rolling Sharpe ratio of a strategy.      Parameters     ---------, rolling_sharpe()

### Community 56 - "Community 56"
Cohesion: 1.00
Nodes (2): Determines the Sortino ratio of a strategy.      Parameters     ----------     r, sortino_ratio()

### Community 57 - "Community 57"
Cohesion: 1.00
Nodes (2): Determines the Sharpe ratio of a strategy.      Parameters     ----------     re, sharpe_ratio()

### Community 58 - "Community 58"
Cohesion: 1.00
Nodes (2): Determines R-squared of a linear fit to the cumulative     log returns. Computes, stability_of_timeseries()

### Community 59 - "Community 59"
Cohesion: 1.00
Nodes (2): Variance-covariance calculation of daily Value-at-Risk in a     portfolio., var_cov_var_normal()

## Knowledge Gaps
- **135 isolated node(s):** `Wrapper module around seaborn to suppress warnings on import.  This should be re`, `Sums the absolute value of shares traded in each name on each day.     Adds colu`, `Compute the number of days that would have been required     to fully liquidate`, `Finds the longest estimated liquidation time for each traded     name over the c`, `For each traded name, find the daily transaction total that consumed     the gre` (+130 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 18`** (2 nodes): `plot_cones()`, `Plots the upper and lower bounds of an n standard deviation     cone of forecast`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (2 nodes): `plot_daily_turnover_hist()`, `Plots a histogram of daily turnover rates.      Parameters     ----------     tr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (2 nodes): `plot_daily_volume()`, `Plots trading volume per day vs. date.      Also displays all-time daily average`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (2 nodes): `plot_drawdown_periods()`, `Plots cumulative returns highlighting top drawdown periods.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (2 nodes): `plot_drawdown_underwater()`, `Plots how far underwaterr returns are over time, or plots current     drawdown v`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (2 nodes): `plot_exposures()`, `Plots a cake chart of the long and short exposure.      Parameters     ---------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (2 nodes): `plot_gross_leverage()`, `Plots gross leverage versus date.      Gross leverage is the sum of long and sho`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (2 nodes): `plot_holdings()`, `Plots total amount of stocks with an active position, either short     or long.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (2 nodes): `plot_long_short_holdings()`, `Plots total amount of stocks with an active position, breaking out     short and`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (2 nodes): `plot_max_median_position_concentration()`, `Plots the max and median of long and short position concentrations     over the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (2 nodes): `plot_monthly_returns_dist()`, `Plots a distribution of monthly returns.      Parameters     ----------     retu`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (2 nodes): `plot_monthly_returns_heatmap()`, `Plots a heatmap of returns by month.      Parameters     ----------     returns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (2 nodes): `plot_monthly_returns_timeseries()`, `Plots monthly returns as a timeseries.      Parameters     ----------     return`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (2 nodes): `plot_perf_stats()`, `Create box plot of some performance metrics of the strategy.     The width of th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (2 nodes): `plot_prob_profit_trade()`, `Plots a probability distribution for the event of making     a profitable trade.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (2 nodes): `plot_return_quantiles()`, `Creates a box plot of daily, weekly, and monthly return     distributions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (2 nodes): `plot_returns()`, `Plots raw returns over time.      Backtest returns are in green, and out-of-samp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (2 nodes): `plot_rolling_beta()`, `Plots the rolling 6-month and 12-month beta versus date.      Parameters     ---`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (2 nodes): `plot_rolling_returns()`, `Plots cumulative rolling returns versus some benchmarks'.      Backtest returns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (2 nodes): `plot_rolling_sharpe()`, `Plots the rolling Sharpe ratio versus date.      Parameters     ----------     r`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (2 nodes): `plot_rolling_volatility()`, `Plots the rolling volatility versus date.      Parameters     ----------     ret`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (2 nodes): `plot_round_trip_lifetimes()`, `Plots timespans and directions of a sample of round trip trades.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (2 nodes): `plot_sector_allocations()`, `Plots the sector exposures of the portfolio over time.      Parameters     -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (2 nodes): `plot_slippage_sensitivity()`, `Plots curve relating per-dollar slippage to average annual returns.      Paramet`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (2 nodes): `plot_slippage_sweep()`, `Plots equity curves at different per-dollar slippage assumptions.      Parameter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (2 nodes): `plot_turnover()`, `Plots turnover vs. date.      Turnover is the number of shares traded for a peri`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (2 nodes): `plot_txn_time_hist()`, `Plots a histogram of transaction times, binning the times into     buckets of a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (2 nodes): `plotting_context()`, `Create pyfolio default plotting style context.      Under the hood, calls and re`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (2 nodes): `Prints and/or plots the exposures of the top 10 held positions of     all time.`, `show_and_plot_top_positions()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (2 nodes): `Prints information about the worst drawdown periods.      Prints peak dates, val`, `show_worst_drawdown_periods()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (2 nodes): `Prints the share of total PnL contributed by each     traded name.      Paramete`, `show_profit_attribution()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 49`** (1 nodes): `Wrapper module around seaborn to suppress warnings on import.  This should be re`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (2 nodes): `extract_interesting_date_ranges()`, `Extracts returns based on interesting events. See     gen_date_range_interesting`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (2 nodes): `max_drawdown()`, `Determines the maximum drawdown of a strategy.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (2 nodes): `normalize()`, `Normalizes a returns timeseries based on the first value.      Parameters     --`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (2 nodes): `omega_ratio()`, `Determines the Omega ratio of a strategy.      Parameters     ----------     ret`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (2 nodes): `Determines the rolling volatility of a strategy.      Parameters     ----------`, `rolling_volatility()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 55`** (2 nodes): `Determines the rolling Sharpe ratio of a strategy.      Parameters     ---------`, `rolling_sharpe()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (2 nodes): `Determines the Sortino ratio of a strategy.      Parameters     ----------     r`, `sortino_ratio()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (2 nodes): `Determines the Sharpe ratio of a strategy.      Parameters     ----------     re`, `sharpe_ratio()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (2 nodes): `Determines R-squared of a linear fit to the cumulative     log returns. Computes`, `stability_of_timeseries()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 59`** (2 nodes): `Variance-covariance calculation of daily Value-at-Risk in a     portfolio.`, `var_cov_var_normal()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `Wrapper module around seaborn to suppress warnings on import.  This should be re`, `Sums the absolute value of shares traded in each name on each day.     Adds colu`, `Compute the number of days that would have been required     to fully liquidate` to the rest of the system?**
  _135 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.057057057057057055 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.11067193675889328 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.12857142857142856 - nodes in this community are weakly interconnected._
- **Should `Community 4` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._