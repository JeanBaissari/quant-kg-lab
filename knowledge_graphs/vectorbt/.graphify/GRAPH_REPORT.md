# Graph Report - .  (2026-07-29)

## Corpus Check
- cluster-only mode - file stats not available

## Summary
- 5411 nodes · 13588 edges · 385 communities detected
- Extraction: 59% EXTRACTED · 41% INFERRED · 0% AMBIGUOUS · INFERRED: 5569 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: uses: 5569 · method: 1795 · contains: 1794 · rationale_for: 1705 · calls: 1645 · imports_from: 688 · imports: 258 · inherits: 134


## Graph Freshness
- Built from Git commit: `f989752`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Config` - 575 edges
2. `ArrayWrapper` - 530 edges
3. `Wrapping` - 422 edges
4. `PlotsBuilderMixin` - 288 edges
5. `StatsBuilderMixin` - 288 edges
6. `MappedArray` - 270 edges
7. `Drawdowns` - 239 edges
8. `Configured` - 216 edges
9. `Ranges` - 183 edges
10. `RepEval` - 182 edges

## Surprising Connections (you probably didn't know these)
- `Regression tests for vectorbt plotting behavior.  These tests are intended to en` --uses--> `Bar`  [INFERRED]
  tests/test_plotting.py → vectorbt/generic/plotting.py
- `Regression tests for vectorbt plotting behavior.  These tests are intended to en` --uses--> `Box`  [INFERRED]
  tests/test_plotting.py → vectorbt/generic/plotting.py
- `Regression tests for vectorbt plotting behavior.  These tests are intended to en` --uses--> `Gauge`  [INFERRED]
  tests/test_plotting.py → vectorbt/generic/plotting.py
- `Regression tests for vectorbt plotting behavior.  These tests are intended to en` --uses--> `Heatmap`  [INFERRED]
  tests/test_plotting.py → vectorbt/generic/plotting.py
- `Regression tests for vectorbt plotting behavior.  These tests are intended to en` --uses--> `Histogram`  [INFERRED]
  tests/test_plotting.py → vectorbt/generic/plotting.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.04
Nodes (154): Drawdowns, MetaPortfolio, Class for modeling portfolio and measuring its performance.      Args:         w, Engine preference for dispatch functions., Perform indexing on `Portfolio`., Simulate portfolio from orders - size, price, fees, and other information., Simulate portfolio from entry and exit signals.          See `vectorbt.portfolio, Simulate portfolio from holding.          Based on `Portfolio.from_signals`. (+146 more)

### Community 1 - "Community 1"
Cohesion: 0.03
Nodes (161): AttrResolver, Wrapping, MetaData, Dict that contains symbols as keys., Class that downloads, updates, and manages data coming from a data source., Perform indexing on `Data`., Data dictionary keyed by symbol., `tz_localize` initially passed to `Data.download_symbol`. (+153 more)

### Community 2 - "Community 2"
Cohesion: 0.03
Nodes (102): ArrayWrapper, Extends `vectorbt.generic.ranges.Ranges` for working with drawdown records., Perform indexing on `Drawdowns`., Build `Drawdowns` from time series `ts`.          `**kwargs` will be passed to `, Original time series that records are built from (optional)., See `vectorbt.generic.dispatch.dd_drawdown`.          Takes into account both re, Average drawdown (ADD).          Based on `Drawdowns.drawdown`., Maximum drawdown (MDD).          Based on `Drawdowns.drawdown`. (+94 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (98): BaseAccessor, BaseDFAccessor, BaseSRAccessor, Accessor on top of Series.      Accessible through `pd.Series.vbt` and all child, Accessor on top of DataFrames.      Accessible through `pd.DataFrame.vbt` and al, Accessor on top of Series and DataFrames.      Accessible through `pd.Series.vbt, BaseAccessor, BaseDFAccessor (+90 more)

### Community 4 - "Community 4"
Cohesion: 0.05
Nodes (91): build_param_indexer(), indexing_on_mapper(), Broadcast `mapper` Series to `ref_obj` and perform pandas indexing using `pd_ind, A factory to create a class with parameter indexing.      Parameter indexer enab, bottleneck, collections, attach_nb_methods(), attach_transform_methods() (+83 more)

### Community 5 - "Community 5"
Cohesion: 0.02
Nodes (82): alpha(), annualized_return(), annualized_volatility(), beta(), calmar_ratio(), capture(), cond_value_at_risk(), cum_returns() (+74 more)

### Community 6 - "Community 6"
Cohesion: 0.05
Nodes (2): Portfolio, Plot one column/group of gross exposure.          Args:             column (str)

### Community 7 - "Community 7"
Cohesion: 0.03
Nodes (24): datetime, hashlib, numba, pandas_ta, pandas_ta_classic, ParamIndexer, pytest, pytz (+16 more)

### Community 8 - "Community 8"
Cohesion: 0.07
Nodes (40): Class that stores index, columns and shape metadata for wrapping NumPy arrays., Perform indexing on `ArrayWrapper` and also return indexing metadata.          T, Perform indexing on `ArrayWrapper`, Derive metadata from an object., Derive metadata from shape., Get group-aware `ArrayWrapper.columns`., Get group-aware `ArrayWrapper.name`., Number of dimensions. (+32 more)

### Community 9 - "Community 9"
Cohesion: 0.03
Nodes (69): approx_order_value(), asset_returns(), asset_value(), asset_value_grouped(), assets(), benchmark_value(), benchmark_value_grouped(), build_call_seq() (+61 more)

### Community 10 - "Community 10"
Cohesion: 0.03
Nodes (66): asset_flow_nb(), asset_returns_nb(), asset_value_nb(), assets_nb(), benchmark_value_nb(), cash_nb(), dir_enex_signal_func_nb(), final_value_nb() (+58 more)

### Community 11 - "Community 11"
Cohesion: 0.04
Nodes (62): between_partition_ranges_nb(), between_ranges_nb(), between_two_ranges_nb(), clean_enex_1d_nb(), clean_enex_nb(), first_choice_nb(), generate_enex_nb(), generate_ex_nb() (+54 more)

### Community 12 - "Community 12"
Cohesion: 0.05
Nodes (58): chacha8rng, generic, prelude, pymodulemethods, rand, sample, seedablerng, between_partition_ranges() (+50 more)

### Community 13 - "Community 13"
Cohesion: 0.04
Nodes (55): any_squeeze_nb(), apply_and_reduce_nb(), apply_nb(), applymap_nb(), argmax_reduce_nb(), argmin_reduce_nb(), _bshift_1d_nb(), _bshift_nb() (+47 more)

### Community 14 - "Community 14"
Cohesion: 0.06
Nodes (42): exceptions, approx_order_value(), approx_order_value_py(), asset_returns_py(), asset_value_grouped_py(), build_call_seq_py(), cash_flow_grouped_py(), fill_log_record_raw() (+34 more)

### Community 15 - "Community 15"
Cohesion: 0.05
Nodes (39): Whether to allow enabling grouping., Whether to allow disabling grouping., Whether to allow changing groups., Check whether column grouping has changed in any way., Check whether the number of groups has changed., DirNamesMixin, Documented, clean_labels() (+31 more)

### Community 16 - "Community 16"
Cohesion: 0.05
Nodes (26): _maybe_await(), Pass bot object to func command., Blocking Telegram bot for `python-telegram-bot` 20 and later.          `**kwargs, Dispatcher-like application., Custom handlers to add.              Override to add custom handlers. Order coun, Chat ids that ever interacted with this bot.              A chat id is added upo, Start the bot.              `**kwargs` are passed to `telegram.ext.Updater.start, Callback once the bot has been started.              Override to execute custom (+18 more)

### Community 17 - "Community 17"
Cohesion: 0.04
Nodes (53): init_cash(), is_grouped(), order_not_filled(), raise_rejected_order(), Engine-neutral `vectorbt.portfolio.nb.sum_grouped_nb`., Engine-neutral `vectorbt.portfolio.nb.init_cash_nb`., Engine-neutral `vectorbt.portfolio.nb.value_nb`., Engine-neutral `vectorbt.portfolio.nb.total_return_nb`. (+45 more)

### Community 18 - "Community 18"
Cohesion: 0.06
Nodes (41): cow, rng, slicerandom, any_squeeze_1d(), any_squeeze_rs(), argmax_reduce_1d(), argmax_reduce_rs(), argmin_reduce_1d() (+33 more)

### Community 19 - "Community 19"
Cohesion: 0.04
Nodes (41): numba_core_errors, _OHLCSTCX, _OHLCSTX, _RAND, _RANDNX, _RANDX, Random entry and exit signal generator based on the number of signals.      Gene, Random entry signal generator based on probabilities.      Generates `entries` b (+33 more)

### Community 20 - "Community 20"
Cohesion: 0.04
Nodes (1): TestAccessors

### Community 21 - "Community 21"
Cohesion: 0.06
Nodes (3): GenericAccessor, SignalsAccessor, SignalsSRAccessor

### Community 22 - "Community 22"
Cohesion: 0.06
Nodes (42): add_core_flex_aliases(), as_timed_contiguous(), assert_nested_same(), assert_same(), BenchmarkCase, call_case_func(), effective_layout_for_args(), filter_cases_by_suite() (+34 more)

### Community 23 - "Community 23"
Cohesion: 0.04
Nodes (46): numba_extending, numba_np_numpy_support, apply_on_mapped_nb(), apply_on_records_nb(), bottom_n_inout_map_nb(), col_map_nb(), col_map_select_nb(), col_range_nb() (+38 more)

### Community 24 - "Community 24"
Cohesion: 0.04
Nodes (1): ReturnsAccessor

### Community 25 - "Community 25"
Cohesion: 0.05
Nodes (43): apply_and_concat_multiple(), apply_and_concat_multiple_nb(), apply_and_concat_multiple_ray(), apply_and_concat_none(), apply_and_concat_none_nb(), apply_and_concat_one(), apply_and_concat_one_nb(), apply_and_concat_one_ray() (+35 more)

### Community 26 - "Community 26"
Cohesion: 0.07
Nodes (44): broadcast(), broadcast_index(), broadcast_to(), broadcast_to_array_of(), broadcast_to_axis_of(), flex_choose_i_and_col_nb(), flex_select_auto_nb(), flex_select_nb() (+36 more)

### Community 27 - "Community 27"
Cohesion: 0.07
Nodes (28): Config, SafeToStr, Class that can be safely converted into a string in `prepare_for_doc`., SafeToStr, deep_substitute(), has_templates(), Evaluate `RepEval.expression` using `mapping`.          Merges `mapping` and `Re, Function to be called with argument names from `mapping`. (+20 more)

### Community 28 - "Community 28"
Cohesion: 0.05
Nodes (41): dataclasses, bn_cont_sat_trend_labels(), bn_cont_trend_labels(), bn_trend_labels(), breakout_labels(), fixed_labels_apply(), future_max_apply(), future_mean_apply() (+33 more)

### Community 29 - "Community 29"
Cohesion: 0.05
Nodes (1): TestFactory

### Community 30 - "Community 30"
Cohesion: 0.05
Nodes (33): asyncio, binance_client, ccxt_base_exchange, classmethod, functools, logging, schedule, telegram (+25 more)

### Community 31 - "Community 31"
Cohesion: 0.05
Nodes (25): collections_abc, copy, itertools, numba_typed, os, TestAttr, TestEnum, TestMapping (+17 more)

### Community 32 - "Community 32"
Cohesion: 0.08
Nodes (36): array1_as_slice_cow, array2, intopydict, array_raw_parts(), AsArrayPtr, bottom_n_mapped_mask(), bottom_n_mapped_mask_rs(), Bound<'py, pyo3::PyAny> (+28 more)

### Community 33 - "Community 33"
Cohesion: 0.10
Nodes (35): _ATR, _BBANDS, _MA, _MACD, _MSTD, _OBV, Plot `MA.ma` against `MA.close`.          Args:             column (str): Name o, Moving Standard Deviation (MSTD).      Standard deviation is an indicator that m (+27 more)

### Community 34 - "Community 34"
Cohesion: 0.09
Nodes (1): Records

### Community 35 - "Community 35"
Cohesion: 0.05
Nodes (36): atr_apply(), atr_cache(), bb_apply(), bb_cache(), ma(), ma_apply(), ma_cache(), macd_apply() (+28 more)

### Community 36 - "Community 36"
Cohesion: 0.07
Nodes (36): atr_apply_nb(), atr_cache_nb(), bb_apply_nb(), bb_cache_nb(), ma_apply_nb(), ma_cache_nb(), ma_nb(), macd_apply_nb() (+28 more)

### Community 37 - "Community 37"
Cohesion: 0.11
Nodes (35): ndarray, pyvalueerror, bn_cont_sat_trend_labels(), bn_cont_sat_trend_labels_rs(), bn_cont_trend_labels(), bn_cont_trend_labels_rs(), bn_trend_labels(), bn_trend_labels_rs() (+27 more)

### Community 38 - "Community 38"
Cohesion: 0.05
Nodes (1): TestChecks

### Community 39 - "Community 39"
Cohesion: 0.06
Nodes (35): Exception, AccumulationModeT, AdjustSLContext, AdjustTPContext, CallSeqTypeT, ConflictModeT, DirectionConflictModeT, DirectionT (+27 more)

### Community 40 - "Community 40"
Cohesion: 0.08
Nodes (34): align_index_to(), _align_index_to_nb(), align_indexes(), combine_indexes(), drop_duplicate_levels(), drop_levels(), drop_redundant_levels(), find_first_occurrence() (+26 more)

### Community 41 - "Community 41"
Cohesion: 0.06
Nodes (32): fetch_data(), Select all/random exit patterns, clear, or configure the same way as entry patte, Update candle settings in TA-Lib., Update OHLCV graph.      Also update probability settings, as they also depend u, Simulate portfolio of the main strategy, buy & hold strategy, and a bunch of ran, Final stage where we calculate key performance metrics and compare strategies., Once a new metric has been selected, plot its distribution., Reset most settings. Other settings are reset in their callbacks. (+24 more)

### Community 42 - "Community 42"
Cohesion: 0.10
Nodes (23): plotly_subplots, Regression tests for built-in indicator plot methods.      These create subplots, MA.plot() should show Close line + MA line., RSI.plot() should show RSI line + band shape., BBANDS.plot() should show Close + 3 band lines., MACD.plot() should show MACD + Signal lines + Histogram bar., STOCH.plot() should show %K + %D lines + band shape., ATR.plot() should show TR + ATR lines. (+15 more)

### Community 43 - "Community 43"
Cohesion: 0.09
Nodes (30): ast, contextlib, dict, Context, format_github_link(), generate_api(), _getmembers_all(), git_head_commit() (+22 more)

### Community 44 - "Community 44"
Cohesion: 0.12
Nodes (31): intopyobject, atr_apply_rs(), atr_cache_rs(), bb_apply_rs(), bb_cache_rs(), build_ma_cache(), build_mstd_cache(), diff_2d() (+23 more)

### Community 45 - "Community 45"
Cohesion: 0.06
Nodes (1): TestPortfolio

### Community 46 - "Community 46"
Cohesion: 0.11
Nodes (20): Configured, Box, Histogram, Update the trace data.          Usage:             ```pycon             >>> bar., Whether to plot horizontally., Whether to remove NaN values., Filter out data points before this quantile., Filter out data points after this quantile. (+12 more)

### Community 47 - "Community 47"
Cohesion: 0.06
Nodes (1): TestAccessors

### Community 48 - "Community 48"
Cohesion: 0.06
Nodes (1): TestAccessors

### Community 49 - "Community 49"
Cohesion: 0.08
Nodes (32): array_and_non_neg_int_compatible_with_rust(), array_compatible_with_rust(), col_map_compatible_with_rust(), col_range_compatible_with_rust(), combine_rust_support(), exact_array_compatible_with_rust(), flex_array_compatible_with_rust(), mask_and_array_compatible_with_rust() (+24 more)

### Community 50 - "Community 50"
Cohesion: 0.09
Nodes (30): argparse, calc_stats(), companion_output_path(), format_duration(), format_metric_value(), format_stat(), main(), make_matrix() (+22 more)

### Community 51 - "Community 51"
Cohesion: 0.08
Nodes (30): bn_cont_sat_trend_labels_nb(), bn_cont_trend_labels_nb(), bn_trend_labels_nb(), breakout_labels_nb(), fixed_labels_apply_nb(), future_max_apply_nb(), future_mean_apply_nb(), future_min_apply_nb() (+22 more)

### Community 52 - "Community 52"
Cohesion: 0.06
Nodes (1): TestMappedArray

### Community 53 - "Community 53"
Cohesion: 0.11
Nodes (24): ordering, alpha_1d(), beta_1d(), calmar_ratio_1d(), calmar_ratio_rs(), cond_value_at_risk_1d(), cond_value_at_risk_rs(), cum_returns_1d() (+16 more)

### Community 54 - "Community 54"
Cohesion: 0.10
Nodes (29): array1_as_slice_cow(), broadcast_get(), broadcast_len2(), broadcast_len3(), dd_decline_duration_rs(), dd_drawdown_rs(), dd_recovery_duration_ratio_rs(), dd_recovery_duration_rs() (+21 more)

### Community 55 - "Community 55"
Cohesion: 0.07
Nodes (20): get_func_arg_names(), get_func_kwargs(), Class for wrapping default values., Extends dict with config features such as nested updates, frozen keys/values, an, Select keyword arguments., Parameters for copying `dct`., Dict to fall back to in case of resetting., Get keyword arguments with defaults of a function. (+12 more)

### Community 56 - "Community 56"
Cohesion: 0.08
Nodes (15): object, cached_methodT, cached_property, class_or_instanceproperty, classproperty, custom_methodT, custom_property, Check whether to cache the method/property based on a range of conditions define (+7 more)

### Community 57 - "Community 57"
Cohesion: 0.28
Nodes (5): from_orders_both(), from_orders_longonly(), from_orders_shortonly(), from_signals_shortonly(), TestFromOrders

### Community 58 - "Community 58"
Cohesion: 0.09
Nodes (15): get_group_lens_nb(), get_groups_and_index(), group_by_to_index(), Check whether column grouping has been modified.          Doesn't care if groupi, Resolve `group_by` from either object variable or keyword argument., Convert mapper `group_by` to `pd.Index`.      !!! note         Index and mapper, See `get_groups_and_index`., Return grouped columns. (+7 more)

### Community 59 - "Community 59"
Cohesion: 0.10
Nodes (13): DataUpdater, Data instance.          See `vectorbt.data.base.Data`., Schedule manager instance.          See `vectorbt.utils.schedule_.ScheduleManage, Method that updates data.          Override to do pre- and postprocessing., Schedule `DataUpdater.update`.          For `*args`, `to` and `tags`, see `vecto, Class for scheduling data updates.      Usage:         * Update in the foregroun, Run pending jobs in a loop., Async run pending jobs in a loop. (+5 more)

### Community 60 - "Community 60"
Cohesion: 0.08
Nodes (14): IndicatorFactory, IndicatorBase, pandas_ta(), Shortcut for `vectorbt.indicators.factory.IndicatorFactory.from_talib`., Shortcut for `vectorbt.indicators.factory.IndicatorFactory.from_pandas_ta`., Shortcut for `vectorbt.indicators.factory.IndicatorFactory.from_ta`., ta(), talib() (+6 more)

### Community 61 - "Community 61"
Cohesion: 0.10
Nodes (26): close_position_nb(), generate_stop_signal_nb(), get_stop_price_nb(), is_grouped_nb(), order_nb(), Generate stop signal and change accumulation if needed., Resolve price and slippage of a stop order., Resolve any conflict between an entry and an exit. (+18 more)

### Community 62 - "Community 62"
Cohesion: 0.11
Nodes (26): add(), aggregate_position(), asset_flow_inner(), assets_py(), benchmark_value_grouped_py(), benchmark_value_py(), cash_flow_inner(), cash_grouped_py() (+18 more)

### Community 63 - "Community 63"
Cohesion: 0.08
Nodes (1): TestReshapeFns

### Community 64 - "Community 64"
Cohesion: 0.08
Nodes (24): any_squeeze(), apply(), apply_and_reduce(), applymap(), argmax_reduce(), argmin_reduce(), bfill(), bfill_1d() (+16 more)

### Community 65 - "Community 65"
Cohesion: 0.12
Nodes (15): Bar, Plotting multi-column portfolio without column selection should raise., Shared portfolio with group_by=False should produce same structure as ungrouped., Requesting multiple specific subplots should produce traces from each., Multiple subplots should place traces in separate rows., Return {name: [trace, ...]} mapping. Unnamed traces go under None key., Volume wrapper should create 1 go.Volume trace., Portfolio.plot() with column selection should return BaseFigure. (+7 more)

### Community 66 - "Community 66"
Cohesion: 0.09
Nodes (24): alpha_1d_nb(), alpha_nb(), beta_1d_nb(), beta_nb(), Rolling version of `cum_returns_final_nb`., Rolling version of `annualized_return_nb`., Rolling version of `annualized_volatility_nb`., Rolling version of `max_drawdown_nb`. (+16 more)

### Community 67 - "Community 67"
Cohesion: 0.11
Nodes (13): named_traces(), Regression tests for vectorbt plotting behavior.  These tests are intended to en, Return {name: trace} for first trace of each non-None name., plot_against with both pos and neg regions should have fill + main traces., When self > other everywhere, only positive fill traces should exist., plot_zones=False should produce same traces but no shapes., plot_pnl should show profit markers and zeroline shape., Drawdowns.plot() should show TS, Peak, Valley, Recovery, Active traces + zones. (+5 more)

### Community 68 - "Community 68"
Cohesion: 0.15
Nodes (3): from_signals_both(), from_signals_longonly(), TestFromSignals

### Community 69 - "Community 69"
Cohesion: 0.09
Nodes (2): TestDrawdowns, TestRanges

### Community 70 - "Community 70"
Cohesion: 0.11
Nodes (17): iLoc, IndexingBase, Loc, LocBase, _normalize_numpy_scalars(), ParamLoc, Indexing keyword arguments., Purely integer-location based indexing for selection by position. (+9 more)

### Community 71 - "Community 71"
Cohesion: 0.14
Nodes (1): Data

### Community 72 - "Community 72"
Cohesion: 0.09
Nodes (22): dateparser, convert_naive_time(), convert_tzaware_time(), datetime_to_ms(), freq_to_timedelta(), get_local_tz(), interval_to_ms(), is_tz_aware() (+14 more)

### Community 73 - "Community 73"
Cohesion: 0.16
Nodes (24): check_group_init_cash_nb(), flex_simulate_nb(), flex_simulate_row_wise_nb(), get_group_value_ctx_nb(), get_group_value_nb(), init_last_pos_record_nb(), init_records_nb(), Replace infinity price in an order. (+16 more)

### Community 74 - "Community 74"
Cohesion: 0.08
Nodes (1): TestPortfolioRustParity

### Community 75 - "Community 75"
Cohesion: 0.10
Nodes (22): apply_2d_by_col_inplace(), bfill_1d(), bfill_1d_into(), bfill_2d_c(), bfill_rs(), ffill_1d(), ffill_1d_into(), ffill_2d_c() (+14 more)

### Community 76 - "Community 76"
Cohesion: 0.13
Nodes (22): apply_2d_by_col(), ewm_mean_1d(), ewm_mean_1d_rs(), ewm_mean_rs(), ewm_std_1d(), ewm_std_1d_rs(), ewm_std_rs(), expanding_max_1d() (+14 more)

### Community 77 - "Community 77"
Cohesion: 0.11
Nodes (4): TestEntryTrades, TestExitTrades, TestOrders, TestPositions

### Community 78 - "Community 78"
Cohesion: 0.15
Nodes (4): Doc, External, Function, Variable

### Community 79 - "Community 79"
Cohesion: 0.10
Nodes (1): TestRecordsRustParity

### Community 80 - "Community 80"
Cohesion: 0.17
Nodes (3): Regression tests for each Portfolio plot_* method.      Asserts return type, tra, Benchmark trace should be a Scatter with data matching cumulative benchmark retu, TestPortfolioPlotSmoke

### Community 81 - "Community 81"
Cohesion: 0.12
Nodes (21): assert_array_equal(), assert_dtype(), assert_meta_equal(), assert_ndim(), assert_shape_equal(), assert_subdtype(), assert_type_equal(), is_any_array() (+13 more)

### Community 82 - "Community 82"
Cohesion: 0.12
Nodes (7): OHLCVDFAccessor, Accessor on top of OHLCV data. For DataFrames only.      Accessible through `pd., Get column from `OHLCVDFAccessor.column_names`., Open, high, low, and close series., Defaults for `OHLCVDFAccessor.stats`.          Merges `vectorbt.generic.accessor, Plot OHLCV data.          Args:             plot_type: Either 'OHLC', 'Candlesti, Defaults for `OHLCVDFAccessor.plots`.          Merges `vectorbt.generic.accessor

### Community 83 - "Community 83"
Cohesion: 0.18
Nodes (20): alpha_rs(), annualized_return_from_product(), beta_rs(), capture_1d(), capture_2d(), capture_rs(), down_capture_1d(), down_capture_rs() (+12 more)

### Community 84 - "Community 84"
Cohesion: 0.11
Nodes (4): assert_same_tuple(), test_execute_order_nb(), TestFromHolding, TestFromRandomSignals

### Community 85 - "Community 85"
Cohesion: 0.11
Nodes (18): dill, keyword, assert_dtype_equal(), assert_in(), assert_len_equal(), assert_level_not_exists(), assert_not_none(), is_hashable() (+10 more)

### Community 86 - "Community 86"
Cohesion: 0.11
Nodes (19): asset_value_grouped_nb(), benchmark_value_grouped_nb(), cash_flow_grouped_nb(), cash_grouped_nb(), cash_in_sim_order_nb(), check_group_lens_nb(), Squeeze each group of columns into a single column using sum operation., Get cash flow series per group. (+11 more)

### Community 87 - "Community 87"
Cohesion: 0.12
Nodes (18): get_ranges_arr(), insert_argsort_nb(), is_sorted(), is_sorted_nb(), max_rel_rescale(), min_rel_rescale(), Rescale elements in `a` relatively to maximum., Rescale a float array into an int array. (+10 more)

### Community 88 - "Community 88"
Cohesion: 0.11
Nodes (1): TestColumnGrouper

### Community 89 - "Community 89"
Cohesion: 0.11
Nodes (1): TestConfig

### Community 90 - "Community 90"
Cohesion: 0.18
Nodes (5): Class, filter_type(), link_inheritance(), linkify(), toposort()

### Community 91 - "Community 91"
Cohesion: 0.16
Nodes (9): TraceUpdater, Bar wrapper should create 1 go.Bar per column., Bar.update() should change y values., add_trace_kwargs with row/col should position Bar traces in correct subplot., Histogram wrapper should create 1 go.Histogram per column with matching data., Histogram.update() should change trace data., horizontal=True should put data on y-axis instead of x-axis., TestBarWrapper (+1 more)

### Community 92 - "Community 92"
Cohesion: 0.28
Nodes (17): asset_flow_py(), cash_flow_py(), get_entry_trades_py(), get_exit_trades_py(), get_positions_py(), log_record_offsets(), order_record_offsets(), portfolio_sim_error_to_pyerr() (+9 more)

### Community 93 - "Community 93"
Cohesion: 0.12
Nodes (1): TestArrayWrapper

### Community 94 - "Community 94"
Cohesion: 0.17
Nodes (13): Data, AlpacaData, BinanceData, CCXTData, `Data` for data coming from `yfinance`.      Stocks are usually in the timezone, Download the symbol.          Args:             symbol (str): Symbol., `Data` for data coming from `python-binance`.      Usage:         * Fetch the 1-, Override `vectorbt.data.base.Data.download` to instantiate a Binance client. (+5 more)

### Community 95 - "Community 95"
Cohesion: 0.18
Nodes (10): Volume, Regression tests for signals accessor plot methods.      These overlay markers o, plot_as_entry_markers should add triangle-up markers to existing figure., plot_as_exit_markers should add triangle-down markers to existing figure., Entry + Exit markers should compose correctly on same figure., Scatter wrapper should create 1 go.Scatter per column., Scatter.update() should change y values on all traces., add_trace_kwargs with row/col should position traces in correct subplot. (+2 more)

### Community 96 - "Community 96"
Cohesion: 0.13
Nodes (1): TestAccessors

### Community 97 - "Community 97"
Cohesion: 0.13
Nodes (16): assert_engine_func(), assert_numba_func(), assert_rust_func(), func_accepts_arg(), is_engine_compatible_func(), is_engine_dispatch_func(), is_numba_func(), is_rust_func() (+8 more)

### Community 98 - "Community 98"
Cohesion: 0.19
Nodes (9): Gauge, Default use_widgets=True should return FigureWidget., Toggling use_widgets=False should return plain Figure., Default layout settings should be applied to the figure., Custom layout kwargs are recursively merged, not replaced., make_subplots should return a BaseFigure instance., pct_scale=True should use returns, False should use raw PnL., TestFigureFactory (+1 more)

### Community 99 - "Community 99"
Cohesion: 0.16
Nodes (9): Job, Scheduler, AsyncJob, AsyncScheduler, Create a new job that runs every `interval` units of time.          `*args` can, Async `Scheduler.run_pending`., Async `Scheduler.run_all`., Async `Scheduler.run_job`. (+1 more)

### Community 100 - "Community 100"
Cohesion: 0.16
Nodes (15): downside_risk_1d(), downside_risk_rs(), nanmean_shifted(), nanstd_shifted(), rolling_apply_2d_by_col(), rolling_downside_risk_rs(), rolling_max_drawdown_rs(), rolling_sharpe_ratio_rs() (+7 more)

### Community 101 - "Community 101"
Cohesion: 0.13
Nodes (1): TestIndexFns

### Community 102 - "Community 102"
Cohesion: 0.14
Nodes (2): TestLogs, TestRecords

### Community 103 - "Community 103"
Cohesion: 0.17
Nodes (10): copy_dict(), merge_dicts(), Copy dict based on a copy mode.      The following modes are supported:      * ', Update dict with keys and values from other dict.      Set `nested` to True to u, Merge dicts.      Args:         *dicts (dict): Dicts.         to_dict (bool): Wh, Clears the config and updates it with the initial config.          `reset_dct_co, Replace `reset_dct` by the current state.          `reset_dct_copy_kwargs` overr, Set dict item.      If the dict is of the type `Config`, also passes `force` key (+2 more)

### Community 104 - "Community 104"
Cohesion: 0.14
Nodes (7): Apply function `apply_func` on index of the pandas object.          Set `axis` t, See `vectorbt.base.index_fns.stack_indexes`.          Set `on_top` to False to s, See `vectorbt.base.index_fns.drop_levels`.          See `BaseAccessor.apply_on_i, See `vectorbt.base.index_fns.rename_levels`.          See `BaseAccessor.apply_on, See `vectorbt.base.index_fns.select_levels`.          See `BaseAccessor.apply_on, See `vectorbt.base.index_fns.drop_redundant_levels`.          See `BaseAccessor., See `vectorbt.base.index_fns.drop_duplicate_levels`.          See `BaseAccessor.

### Community 105 - "Community 105"
Cohesion: 0.14
Nodes (14): copy_trade_record_nb(), fill_entry_trades_in_position_nb(), fill_position_record_nb(), fill_trade_record_nb(), get_entry_trades_nb(), get_exit_trades_nb(), get_positions_nb(), get_trade_stats_nb() (+6 more)

### Community 106 - "Community 106"
Cohesion: 0.14
Nodes (14): annualized_return_1d_nb(), annualized_return_nb(), capture_1d_nb(), capture_nb(), cum_returns_final_1d_nb(), cum_returns_final_nb(), 2-dim version of `cum_returns_final_1d_nb`., Mean annual growth rate of returns.      This is equivalent to the compound annu (+6 more)

### Community 107 - "Community 107"
Cohesion: 0.16
Nodes (13): between_partition_ranges(), between_ranges(), between_two_ranges(), part_pos_rank(), rank(), _rank_support(), Engine-neutral `vectorbt.signals.nb.between_ranges_nb`., Engine-neutral `vectorbt.signals.nb.between_two_ranges_nb`. (+5 more)

### Community 108 - "Community 108"
Cohesion: 0.25
Nodes (14): buy(), buy_py(), execute_order(), execute_order_py(), get_entry_trades_inner(), get_exit_trades_inner(), is_addition_zero(), is_close() (+6 more)

### Community 109 - "Community 109"
Cohesion: 0.22
Nodes (8): Heatmap, OHLC plot without volume should have 1 Ohlc trace., Candlestick plot with volume should have Candlestick + Bar traces., Default plot type should be OHLC (from settings)., OHLCV with volume should create 2-row subplot with correct structure., Box wrapper should create 1 go.Box per column., TestBoxWrapper, TestOHLCVPlot

### Community 110 - "Community 110"
Cohesion: 0.22
Nodes (8): Scatter, Series.vbt.plot() should produce 1 Scatter trace with matching data., DataFrame.vbt.plot() should produce 1 Scatter trace per column., return_fig=False should return Scatter wrapper, not BaseFigure., Passing fig= should add traces to existing figure, not create new one., Gauge wrapper should create 1 go.Indicator trace., TestGaugeWrapper, TestGenericAccessorPlot

### Community 111 - "Community 111"
Cohesion: 0.19
Nodes (8): Pickleable, PickleableDict, Superclass that defines abstract properties and methods for pickle-able classes., Save dumps to a file., Load dumps from a file and create new instance., Dict that may contain values of type `Pickleable`., Load dumps from a file and update this instance., Load dumps from a file and update this instance.          !!! note             U

### Community 112 - "Community 112"
Cohesion: 0.17
Nodes (12): _add_var_nb(), expanding_std_1d_nb(), expanding_std_nb(), Return expanding standard deviation.      Numba equivalent to `pd.Series(a).expa, 2-dim version of `expanding_std_1d_nb`., Add a value to a rolling variance state., Remove a value from a rolling variance state., Return rolling standard deviation.      Numba equivalent to `pd.Series(a).rollin (+4 more)

### Community 113 - "Community 113"
Cohesion: 0.17
Nodes (12): asset_flow(), cash_flow(), get_entry_trades(), get_exit_trades(), order_record_array_compatible_with_rust(), Engine-neutral `vectorbt.portfolio.nb.get_entry_trades_nb`., Engine-neutral `vectorbt.portfolio.nb.get_exit_trades_nb`., Engine-neutral `vectorbt.portfolio.nb.asset_flow_nb`. (+4 more)

### Community 114 - "Community 114"
Cohesion: 0.17
Nodes (3): TestIndicatorRustParity, TestLabelsRustParity, TestReturnsRustParity

### Community 115 - "Community 115"
Cohesion: 0.17
Nodes (1): TestFromOrderFunc

### Community 116 - "Community 116"
Cohesion: 0.17
Nodes (1): TestGenerators

### Community 117 - "Community 117"
Cohesion: 0.17
Nodes (1): TestDatetime

### Community 118 - "Community 118"
Cohesion: 0.20
Nodes (10): importlib, pkgutil, sys, types, import_submodules(), is_from_module(), list_module_keys(), Return whether `obj` is from module `module`. (+2 more)

### Community 119 - "Community 119"
Cohesion: 0.18
Nodes (1): TestEngineResolution

### Community 120 - "Community 120"
Cohesion: 0.18
Nodes (1): TestGenericRustParity

### Community 121 - "Community 121"
Cohesion: 0.20
Nodes (6): Update the config.          See `update_dict`., Shallow operation, primarily used by `copy.copy`.          Does not take into ac, Deep operation, primarily used by `copy.deepcopy`.          Does not take into a, Copy the instance in the same way it's done during initialization.          `cop, Create a new instance by copying the config.          See `Configured.replace`., Force-update the config.

### Community 122 - "Community 122"
Cohesion: 0.20
Nodes (2): Module, render_template()

### Community 123 - "Community 123"
Cohesion: 0.20
Nodes (4): ExecuteOrderState, Order, OrderResult, ProcessOrderState

### Community 124 - "Community 124"
Cohesion: 0.20
Nodes (2): TestData, TestDataUpdater

### Community 125 - "Community 125"
Cohesion: 0.20
Nodes (1): TestGenerators

### Community 126 - "Community 126"
Cohesion: 0.20
Nodes (10): is_index(), is_mapping(), is_mapping_like(), is_namedtuple(), is_series(), Check whether object is an instance of namedtuple., Check whether the argument is `pd.Series`., Check whether the argument is `pd.Index`. (+2 more)

### Community 127 - "Community 127"
Cohesion: 0.29
Nodes (9): add_nb(), is_addition_zero_nb(), is_close_nb(), is_close_or_less_nb(), is_less_nb(), Tell whether two values are approximately equal., Tell whether the first value is approximately less than or equal to the second v, Tell whether the first value is approximately less than the second value. (+1 more)

### Community 128 - "Community 128"
Cohesion: 0.20
Nodes (10): Decorator to register a custom `pd.DataFrame` accessor on top of the `pd.DataFra, Decorator to register a `pd.Series` accessor on top of a parent accessor., Decorator to register a `pd.DataFrame` accessor on top of a parent accessor., Register a custom accessor.      `cls` should subclass `pandas.core.accessor.Dir, Decorator to register a custom `pd.Series` accessor on top of the `pd.Series`., register_accessor(), register_dataframe_accessor(), register_dataframe_vbt_accessor() (+2 more)

### Community 129 - "Community 129"
Cohesion: 0.25
Nodes (8): GBMData, generate_gbm_paths(), Generate the symbol using `generate_gbm_paths`.          Args:             symbo, `Data` for synthetically generated data., Abstract method to generate a symbol., Generate using Geometric Brownian Motion (GBM).      See https://stackoverflow.c, `SyntheticData` for data generated using Geometric Brownian Motion (GBM).      U, SyntheticData

### Community 130 - "Community 130"
Cohesion: 0.33
Nodes (2): fenced_code_blocks_hidden(), ToMarkdown

### Community 131 - "Community 131"
Cohesion: 0.22
Nodes (6): DrawdownStatusT, RangeStatusT, TrendModeT, FactoryModeT, StopTypeT, vectorbt_utils_docs

### Community 133 - "Community 133"
Cohesion: 0.33
Nodes (7): pandas_api_types, re, assert_frame_equal_compat(), assert_index_equal_compat(), assert_series_equal_compat(), normalize_test_index(), normalize_test_pandas()

### Community 134 - "Community 134"
Cohesion: 0.28
Nodes (9): buy_nb(), execute_order_nb(), order_not_filled_nb(), Execute an order without persistence., Sell or/and short sell., Execute an order given the current state.      Args:         state (ProcessOrder, Return `OrderResult` for order that hasn't been filled., sell_nb() (+1 more)

### Community 135 - "Community 135"
Cohesion: 0.22
Nodes (9): fill_log_record_nb(), fill_order_record_nb(), process_order_nb(), raise_rejected_order_nb(), Fill an order record., Raise an `vectorbt.portfolio.enums.RejectedOrderError`., Update valuation price and value., Process an order by executing it, saving relevant information to the logs, and r (+1 more)

### Community 136 - "Community 136"
Cohesion: 0.25
Nodes (8): requests, requests_adapters, requests_packages_urllib3_util_retry, urllib_parse, Retry `retries` times if unsuccessful., Translate text to GIF.      See https://engineering.giphy.com/contextually-aware, requests_retry_session(), text_to_giphy_url()

### Community 137 - "Community 137"
Cohesion: 0.42
Nodes (5): rolling_std_1d(), rolling_std_1d_rs(), rolling_std_2d_c(), rolling_std_rs(), RollingVarState

### Community 138 - "Community 138"
Cohesion: 0.22
Nodes (9): annualized_return_1d(), annualized_return_2d(), annualized_return_rs(), cum_returns_final_1d(), cum_returns_final_1d_rs(), cum_returns_final_2d(), cum_returns_final_rs(), rolling_annualized_return_rs() (+1 more)

### Community 139 - "Community 139"
Cohesion: 0.22
Nodes (1): TestSignalsRustParity

### Community 141 - "Community 141"
Cohesion: 0.22
Nodes (1): TestBasic

### Community 142 - "Community 142"
Cohesion: 0.22
Nodes (1): TestArray

### Community 143 - "Community 143"
Cohesion: 0.22
Nodes (9): assert_equal(), _functions_equal(), is_deep_equal(), is_equal(), Check whether two objects are equal., Compare functions by their semantic behavior, ignoring position metadata.      C, Check whether two objects are equal (deep check)., Raise exception if the first argument and the second argument are different. (+1 more)

### Community 144 - "Community 144"
Cohesion: 0.29
Nodes (4): Check whether columns are grouped., Check whether column grouping has been enabled., Check whether column grouping has been disabled., Check passed `group_by` object against restrictions.

### Community 145 - "Community 145"
Cohesion: 0.25
Nodes (8): describe_reduce_nb(), nanstd_1d_nb(), nanstd_nb(), Return std (ignores NaNs)., Return descriptive statistics (ignores NaNs).      Numba equivalent to `pd.Serie, Numba-equivalent of `np.nanstd`., 2-dim version of `nanstd_1d_nb`., std_reduce_nb()

### Community 146 - "Community 146"
Cohesion: 0.25
Nodes (8): expanding_mean_1d_nb(), expanding_mean_nb(), Return expanding mean.      Numba equivalent to `pd.Series(a).expanding(min_peri, 2-dim version of `expanding_mean_1d_nb`., Return rolling mean.      Numba equivalent to `pd.Series(a).rolling(window, min_, 2-dim version of `rolling_mean_1d_nb`., rolling_mean_1d_nb(), rolling_mean_nb()

### Community 147 - "Community 147"
Cohesion: 0.25
Nodes (8): get_positions(), Engine-neutral `vectorbt.portfolio.nb.trade_winning_streak_nb`., Engine-neutral `vectorbt.portfolio.nb.trade_losing_streak_nb`., Engine-neutral `vectorbt.portfolio.nb.get_positions_nb`., Return whether trade records have the exact Rust-compatible dtype., trade_losing_streak(), trade_record_array_compatible_with_rust(), trade_winning_streak()

### Community 148 - "Community 148"
Cohesion: 0.25
Nodes (8): approx_order_value_nb(), get_col_elem_nb(), Sort call sequence `call_seq_out` based on the value of each potential order., Sort call sequence attached to `vectorbt.portfolio.enums.SegmentContext`.      S, Get the current element using flexible indexing given the context and the column, Approximate value of an order., sort_call_seq_nb(), sort_call_seq_out_nb()

### Community 149 - "Community 149"
Cohesion: 0.25
Nodes (8): build_call_seq(), build_call_seq_nb(), Shuffle the call sequence array., Build a new call sequence array., Force the call sequence array to pass our requirements., Not compiled but faster version of `build_call_seq_nb`., require_call_seq(), shuffle_call_seq_nb()

### Community 150 - "Community 150"
Cohesion: 0.25
Nodes (8): calmar_ratio_1d_nb(), calmar_ratio_nb(), max_drawdown_1d_nb(), max_drawdown_nb(), Total maximum drawdown (MDD)., 2-dim version of `max_drawdown_1d_nb`., Calmar ratio, or drawdown ratio, of a strategy., 2-dim version of `calmar_ratio_1d_nb`.

### Community 151 - "Community 151"
Cohesion: 0.25
Nodes (8): downside_risk_1d_nb(), downside_risk_nb(), Downside deviation below a threshold., 2-dim version of `downside_risk_1d_nb`., Sortino ratio of a strategy., 2-dim version of `sortino_ratio_1d_nb`., sortino_ratio_1d_nb(), sortino_ratio_nb()

### Community 152 - "Community 152"
Cohesion: 0.25
Nodes (8): generate_enex(), generate_rand_enex_by_prob(), rand_chain_by_prob_apply(), rand_enex_by_prob_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_enex_by_prob_nb`., Engine-neutral `vectorbt.signals.nb.generate_enex_nb`., Apply function used by `vectorbt.signals.generators.RPROBNX`., Apply function used by `vectorbt.signals.generators.RPROBCX`.

### Community 153 - "Community 153"
Cohesion: 0.25
Nodes (1): TestColumnMapper

### Community 154 - "Community 154"
Cohesion: 0.25
Nodes (8): assert_instance_of(), assert_subclass_of(), is_instance_of(), is_subclass_of(), Check whether the argument is a subclass of `types`.      `types` can be one or, Check whether the argument is an instance of `types`.      `types` can be one or, Raise exception if the argument is none of types `types`., Raise exception if the argument is not a subclass of classes `classes`.

### Community 155 - "Community 155"
Cohesion: 0.29
Nodes (7): cum_returns_1d_nb(), cum_returns_nb(), drawdown_1d_nb(), drawdown_nb(), Drawdown of cumulative returns., 2-dim version of `drawdown_1d_nb`., 2-dim version of `cum_returns_1d_nb`.

### Community 156 - "Community 156"
Cohesion: 0.33
Nodes (7): flatten_grouped(), flatten_grouped_rs(), flatten_uniform_grouped(), flatten_uniform_grouped_rs(), validate_group_lens(), value_counts(), value_counts_rs()

### Community 157 - "Community 157"
Cohesion: 0.29
Nodes (4): Trades.plot() should show Close, Entry, Exit markers and profit zones., Entry/Exit trace positions should match trade records., Passing fig= should add trade traces to existing figure., TestTradesPlot

### Community 158 - "Community 158"
Cohesion: 0.29
Nodes (6): adjust_lightness(), adjust_opacity(), Map `value_range` to colormap with name `cmap_name` and get RGB of the `value` f, Adjust opacity of color., Lightens the given color by multiplying (1-luminosity) by the given amount., rgb_from_cmap()

### Community 159 - "Community 159"
Cohesion: 0.29
Nodes (6): atomic_dict, AtomicConfig, convert_to_dict(), Dict that behaves like a single value when merging., Config that behaves like a single value when merging., Convert any dict (apart from `atomic_dict`) to `dict`.      Set `nested` to True

### Community 160 - "Community 160"
Cohesion: 0.38
Nodes (6): apply_mapping(), Reverse a mapping.      Returns a dict., Convert mapping-like object to a mapping.      Enable `reverse` to apply `revers, Apply mapping on object using a mapping-like object.      Args:         obj (any, reverse_mapping(), to_mapping()

### Community 161 - "Community 161"
Cohesion: 0.33
Nodes (3): See `vectorbt.base.reshape_fns.broadcast`., Concatenate with `others` along columns.          Args:             *others (arr, Combine with `other` using `combine_func`.          Args:             other (arr

### Community 162 - "Community 162"
Cohesion: 0.33
Nodes (6): dd_decline_duration_nb(), dd_recovery_duration_nb(), dd_recovery_duration_ratio_nb(), Return the duration of the peak-to-valley phase of each drawdown record., Return the duration of the valley-to-recovery phase of each drawdown record., Return the ratio of the recovery duration to the decline duration of each drawdo

### Community 163 - "Community 163"
Cohesion: 0.33
Nodes (6): flat_reduce_grouped_nb(), flat_reduce_grouped_to_array_nb(), flatten_forder_nb(), Flatten `a` in F order., Same as `reduce_grouped_nb` but passes flattened array., Same as `reduce_grouped_to_array_nb` but passes flattened 1D array.

### Community 164 - "Community 164"
Cohesion: 0.33
Nodes (4): Handler, LogHandler, _message_type(), Handler to log user updates.

### Community 165 - "Community 165"
Cohesion: 0.33
Nodes (6): Return whether a structured record array is compatible with the Rust engine., Engine-neutral `vectorbt.records.nb.record_col_map_select_nb`., Engine-neutral `vectorbt.records.nb.record_col_range_select_nb`., record_array_compatible_with_rust(), record_col_map_select(), record_col_range_select()

### Community 166 - "Community 166"
Cohesion: 0.40
Nodes (5): approx_exp_max_sharpe(), deflated_sharpe_ratio(), Expected Maximum Sharpe Ratio., Deflated Sharpe Ratio (DSR).      See [Deflated Sharpe Ratio](https://gmarti.git, scipy_stats

### Community 167 - "Community 167"
Cohesion: 0.33
Nodes (6): get_return_nb(), Calculate return from input and output value., Calculate returns from value., 2-dim version of `returns_1d_nb`., returns_1d_nb(), returns_nb()

### Community 168 - "Community 168"
Cohesion: 0.47
Nodes (2): DrawdownRecord, RangeRecord

### Community 169 - "Community 169"
Cohesion: 0.33
Nodes (1): TestDecorators

### Community 170 - "Community 170"
Cohesion: 0.33
Nodes (1): TestMath

### Community 171 - "Community 171"
Cohesion: 0.33
Nodes (1): TestTemplate

### Community 172 - "Community 172"
Cohesion: 0.33
Nodes (3): Pre-process an attribute before resolution.          Should return an attribute., Post-process an object after resolution.          Should return an object., Resolve an attribute using keyword arguments and built-in caching.          * If

### Community 173 - "Community 173"
Cohesion: 0.33
Nodes (6): assert_index_equal(), is_default_index(), is_index_equal(), Check whether indexes are equal.      Introduces naming tests on top of `pd.Inde, Check whether index is a basic range., Raise exception if the first argument and the second argument have different ind

### Community 174 - "Community 174"
Cohesion: 0.33
Nodes (3): Remove attributes of the removed keys given keys prior to the removal., Remove and return the pair by the key., Remove and return some pair.

### Community 175 - "Community 175"
Cohesion: 0.60
Nodes (2): OrderRecord, TradeRecord

### Community 176 - "Community 176"
Cohesion: 0.50
Nodes (5): information_ratio_1d(), information_ratio_2d(), information_ratio_rs(), nanmean_pair_diff(), nanstd_pair_diff()

### Community 177 - "Community 177"
Cohesion: 0.40
Nodes (5): percentile_unsorted(), rolling_value_at_risk_rs(), tail_ratio_1d(), value_at_risk_1d(), value_at_risk_rs()

### Community 178 - "Community 178"
Cohesion: 0.40
Nodes (3): Heatmap wrapper should create 1 go.Heatmap trace., Heatmap.update() should change z values., TestHeatmapWrapper

### Community 179 - "Community 179"
Cohesion: 0.40
Nodes (4): map_enum_fields(), map_enum_values(), Map fields to values.      See `vectorbt.utils.mapping.apply_mapping`., Map values to fields.      See `vectorbt.utils.mapping.apply_mapping`.

### Community 180 - "Community 180"
Cohesion: 0.50
Nodes (2): Generate an empty Series/DataFrame of shape `shape` and fill with `fill_value`., Generate an empty Series/DataFrame like `other` and fill with `fill_value`.

### Community 181 - "Community 181"
Cohesion: 0.50
Nodes (2): Perform indexing on `BaseAccessor`., Convert to 2-dim NumPy array.          See `vectorbt.base.reshape_fns.to_2d`.

### Community 182 - "Community 182"
Cohesion: 0.50
Nodes (4): bfill_1d_nb(), bfill_nb(), Fill NaNs by propagating first valid observation backward.      Numba equivalent, 2-dim version of `bfill_1d_nb`.

### Community 183 - "Community 183"
Cohesion: 0.50
Nodes (4): crossed_above_1d_nb(), crossed_above_nb(), Get the crossover of the first array going above the second array., 2-dim version of `crossed_above_1d_nb`.

### Community 184 - "Community 184"
Cohesion: 0.50
Nodes (4): diff_1d_nb(), diff_nb(), Return the 1-th discrete difference.      Numba equivalent to `pd.Series(a).diff, 2-dim version of `diff_1d_nb`.

### Community 185 - "Community 185"
Cohesion: 0.50
Nodes (4): ewm_mean_1d_nb(), ewm_mean_nb(), Return exponential weighted average.      Numba equivalent to `pd.Series(a).ewm(, 2-dim version of `ewm_mean_1d_nb`.

### Community 186 - "Community 186"
Cohesion: 0.50
Nodes (4): ewm_std_1d_nb(), ewm_std_nb(), 2-dim version of `ewm_std_1d_nb`., Return exponential weighted standard deviation.      Numba equivalent to `pd.Ser

### Community 187 - "Community 187"
Cohesion: 0.50
Nodes (4): expanding_apply_nb(), Provide rolling window calculations.      `apply_func_nb` should accept index of, Expanding version of `rolling_apply_nb`., rolling_apply_nb()

### Community 188 - "Community 188"
Cohesion: 0.50
Nodes (4): expanding_matrix_apply_nb(), `rolling_apply_nb` with `apply_func_nb` being applied on all columns at once., Expanding version of `rolling_matrix_apply_nb`., rolling_matrix_apply_nb()

### Community 189 - "Community 189"
Cohesion: 0.50
Nodes (4): expanding_max_1d_nb(), expanding_max_nb(), Return expanding max.      Numba equivalent to `pd.Series(a).expanding(min_perio, 2-dim version of `expanding_max_1d_nb`.

### Community 190 - "Community 190"
Cohesion: 0.50
Nodes (4): expanding_min_1d_nb(), expanding_min_nb(), Return expanding min.      Numba equivalent to `pd.Series(a).expanding(min_perio, 2-dim version of `expanding_min_1d_nb`.

### Community 191 - "Community 191"
Cohesion: 0.50
Nodes (4): ffill_1d_nb(), ffill_nb(), Fill NaNs by propagating last valid observation forward.      Numba equivalent t, 2-dim version of `ffill_1d_nb`.

### Community 192 - "Community 192"
Cohesion: 0.50
Nodes (4): pct_change_1d_nb(), pct_change_nb(), Return the percentage change.      Numba equivalent to `pd.Series(a).pct_change(, 2-dim version of `pct_change_1d_nb`.

### Community 193 - "Community 193"
Cohesion: 0.50
Nodes (4): Return rolling min.      Numba equivalent to `pd.Series(a).rolling(window, min_p, 2-dim version of `rolling_min_1d_nb`., rolling_min_1d_nb(), rolling_min_nb()

### Community 194 - "Community 194"
Cohesion: 0.50
Nodes (4): Return rolling max.      Numba equivalent to `pd.Series(a).rolling(window, min_p, 2-dim version of `rolling_max_1d_nb`., rolling_max_1d_nb(), rolling_max_nb()

### Community 195 - "Community 195"
Cohesion: 0.50
Nodes (4): cash_flow_nb(), get_free_cash_diff_nb(), Get updated debt and free cash flow., Get (free) cash flow series per column.

### Community 196 - "Community 196"
Cohesion: 0.50
Nodes (4): Return whether `init_value` matches the number of columns in `value`., Engine-neutral `vectorbt.returns.nb.returns_nb`., returns(), returns_init_value_compatible_with_rust()

### Community 197 - "Community 197"
Cohesion: 0.50
Nodes (4): annualized_volatility_1d_nb(), annualized_volatility_nb(), Annualized volatility of a strategy., 2-dim version of `annualized_volatility_1d_nb`.

### Community 198 - "Community 198"
Cohesion: 0.50
Nodes (4): cond_value_at_risk_1d_nb(), cond_value_at_risk_nb(), Conditional value at risk (CVaR) of a returns stream., 2-dim version of `cond_value_at_risk_1d_nb`.

### Community 199 - "Community 199"
Cohesion: 0.50
Nodes (4): down_capture_1d_nb(), down_capture_nb(), Capture ratio for periods when the benchmark return is negative., 2-dim version of `down_capture_1d_nb`.

### Community 200 - "Community 200"
Cohesion: 0.50
Nodes (4): information_ratio_1d_nb(), information_ratio_nb(), Information ratio of a strategy., 2-dim version of `information_ratio_1d_nb`.

### Community 201 - "Community 201"
Cohesion: 0.50
Nodes (4): omega_ratio_1d_nb(), omega_ratio_nb(), Omega ratio of a strategy.., 2-dim version of `omega_ratio_1d_nb`.

### Community 202 - "Community 202"
Cohesion: 0.50
Nodes (4): Sharpe ratio of a strategy., 2-dim version of `sharpe_ratio_1d_nb`., sharpe_ratio_1d_nb(), sharpe_ratio_nb()

### Community 203 - "Community 203"
Cohesion: 0.50
Nodes (4): Ratio between the right (95%) and left tail (5%)., 2-dim version of `tail_ratio_1d_nb`., tail_ratio_1d_nb(), tail_ratio_nb()

### Community 204 - "Community 204"
Cohesion: 0.50
Nodes (4): Value at risk (VaR) of a returns stream., 2-dim version of `value_at_risk_1d_nb`., value_at_risk_1d_nb(), value_at_risk_nb()

### Community 205 - "Community 205"
Cohesion: 0.50
Nodes (4): generate_ohlc_stop_enex(), ohlc_stop_enex_apply(), Apply function used by `vectorbt.signals.generators.OHLCSTCX`., Engine-neutral `vectorbt.signals.nb.generate_ohlc_stop_enex_nb`.

### Community 206 - "Community 206"
Cohesion: 0.50
Nodes (4): generate_ohlc_stop_ex(), ohlc_stop_ex_apply(), Engine-neutral `vectorbt.signals.nb.generate_ohlc_stop_ex_nb`., Apply function used by `vectorbt.signals.generators.OHLCSTX`.

### Community 207 - "Community 207"
Cohesion: 0.50
Nodes (4): generate_rand_by_prob(), rand_by_prob_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_by_prob_nb`., Apply function used by `vectorbt.signals.generators.RPROB`.

### Community 208 - "Community 208"
Cohesion: 0.50
Nodes (4): generate_rand_enex(), rand_enex_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_enex_nb`., Apply function used by `vectorbt.signals.generators.RANDNX`.

### Community 209 - "Community 209"
Cohesion: 0.50
Nodes (4): generate_rand_ex_by_prob(), rand_ex_by_prob_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_ex_by_prob_nb`., Apply function used by `vectorbt.signals.generators.RPROBX`.

### Community 210 - "Community 210"
Cohesion: 0.50
Nodes (4): generate_rand_ex(), rand_ex_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_ex_nb`., Apply function used by `vectorbt.signals.generators.RANDX`.

### Community 211 - "Community 211"
Cohesion: 0.50
Nodes (4): generate_rand(), rand_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_nb`., Apply function used by `vectorbt.signals.generators.RAND`.

### Community 212 - "Community 212"
Cohesion: 0.50
Nodes (4): generate_stop_enex(), Engine-neutral `vectorbt.signals.nb.generate_stop_enex_nb`., Apply function used by `vectorbt.signals.generators.STCX`., stop_enex_apply()

### Community 213 - "Community 213"
Cohesion: 0.50
Nodes (4): generate_stop_ex(), Engine-neutral `vectorbt.signals.nb.generate_stop_ex_nb`., Apply function used by `vectorbt.signals.generators.STX`., stop_ex_apply()

### Community 214 - "Community 214"
Cohesion: 0.67
Nodes (4): bshift_1d(), bshift_1d_into(), bshift_2d_c(), bshift_rs()

### Community 215 - "Community 215"
Cohesion: 0.67
Nodes (4): check_bounds(), normalize_index(), nth_index_reduce_rs(), nth_reduce_rs()

### Community 216 - "Community 216"
Cohesion: 0.50
Nodes (4): count_reduce_rs(), nancnt_1d(), nancnt_2d_c(), nancnt_rs()

### Community 217 - "Community 217"
Cohesion: 0.67
Nodes (4): diff_1d(), diff_1d_into(), diff_2d_c(), diff_rs()

### Community 218 - "Community 218"
Cohesion: 0.50
Nodes (4): expanding_mean_1d(), expanding_mean_1d_rs(), expanding_mean_2d_c(), expanding_mean_rs()

### Community 219 - "Community 219"
Cohesion: 0.50
Nodes (4): expanding_std_1d(), expanding_std_1d_rs(), expanding_std_2d_c(), expanding_std_rs()

### Community 220 - "Community 220"
Cohesion: 0.50
Nodes (1): FlexArray<'py, T>

### Community 221 - "Community 221"
Cohesion: 0.67
Nodes (4): fshift_1d(), fshift_1d_into(), fshift_2d_c(), fshift_rs()

### Community 222 - "Community 222"
Cohesion: 0.50
Nodes (4): min_reduce_rs(), min_squeeze_1d(), min_squeeze_rs(), nanmin_1d()

### Community 223 - "Community 223"
Cohesion: 0.50
Nodes (4): annualized_volatility_1d(), annualized_volatility_2d(), annualized_volatility_rs(), rolling_annualized_volatility_rs()

### Community 224 - "Community 224"
Cohesion: 0.50
Nodes (2): pandas_applymap(), Pandas' native element-wise map, compatible with pandas 2.0+.

### Community 225 - "Community 225"
Cohesion: 0.50
Nodes (1): TestSettings

### Community 226 - "Community 226"
Cohesion: 0.50
Nodes (4): assert_dict_sequence_valid(), assert_dict_valid(), Raise exception if dict the argument has keys that are not in `lvl_keys`.      `, Raise exception if a dict or any dict in a sequence of dicts has keys that are n

### Community 227 - "Community 227"
Cohesion: 0.50
Nodes (4): assert_iterable(), is_iterable(), Raise exception if the argument is not an iterable., Check whether the argument is iterable.

### Community 228 - "Community 228"
Cohesion: 0.50
Nodes (4): assert_sequence(), is_sequence(), Check whether the argument is a sequence., Raise exception if the argument is not a sequence.

### Community 229 - "Community 229"
Cohesion: 0.50
Nodes (2): Merge with another dict into one single dict.          See `merge_dicts`., Create a new instance by copying and (optionally) changing the config.

### Community 230 - "Community 230"
Cohesion: 0.50
Nodes (4): prepare_for_doc(), Prepare object for use in documentation., Convert object to a JSON string., to_doc()

### Community 235 - "Community 235"
Cohesion: 0.67
Nodes (1): setuptools

### Community 236 - "Community 236"
Cohesion: 0.67
Nodes (1): nanmean_nb()

### Community 237 - "Community 237"
Cohesion: 0.67
Nodes (3): deep_getattr(), See `vectorbt.utils.attr_.deep_getattr`., Retrieve attribute consecutively.      The attribute chain `attr_chain` can be:

### Community 238 - "Community 238"
Cohesion: 1.00
Nodes (1): Align to `other` on their axes.          Usage:             ```pycon

### Community 239 - "Community 239"
Cohesion: 1.00
Nodes (1): Apply `apply_func` `ntimes` times and concatenate the results along columns.

### Community 240 - "Community 240"
Cohesion: 1.00
Nodes (1): Apply a function `apply_func`.          Args:             *args: Variable argume

### Community 241 - "Community 241"
Cohesion: 1.00
Nodes (1): See `vectorbt.base.reshape_fns.broadcast_to`.

### Community 242 - "Community 242"
Cohesion: 1.00
Nodes (1): Allows passing arguments to the initializer.

### Community 243 - "Community 243"
Cohesion: 1.00
Nodes (1): Accessor class for `pd.DataFrame`.

### Community 244 - "Community 244"
Cohesion: 1.00
Nodes (1): See `vectorbt.base.reshape_fns.make_symmetric`.

### Community 245 - "Community 245"
Cohesion: 1.00
Nodes (1): See `vectorbt.base.reshape_fns.repeat`.          Set `axis` to 1 for columns and

### Community 246 - "Community 246"
Cohesion: 1.00
Nodes (1): Accessor class for `pd.Series`.

### Community 247 - "Community 247"
Cohesion: 1.00
Nodes (1): See `vectorbt.base.reshape_fns.tile`.          Set `axis` to 1 for columns and 0

### Community 248 - "Community 248"
Cohesion: 1.00
Nodes (1): Convert to 1-dim NumPy array          See `vectorbt.base.reshape_fns.to_1d`.

### Community 249 - "Community 249"
Cohesion: 1.00
Nodes (1): See `vectorbt.base.reshape_fns.to_dict`.

### Community 250 - "Community 250"
Cohesion: 1.00
Nodes (1): See `vectorbt.base.reshape_fns.unstack_to_array`.

### Community 251 - "Community 251"
Cohesion: 1.00
Nodes (1): See `vectorbt.base.reshape_fns.unstack_to_df`.

### Community 252 - "Community 252"
Cohesion: 1.00
Nodes (2): count_reduce(), Engine-neutral `vectorbt.generic.nb.count_reduce_nb`.

### Community 253 - "Community 253"
Cohesion: 1.00
Nodes (2): crossed_above_1d(), Engine-neutral `vectorbt.generic.nb.crossed_above_1d_nb`.

### Community 254 - "Community 254"
Cohesion: 1.00
Nodes (2): crossed_above(), Engine-neutral `vectorbt.generic.nb.crossed_above_nb`.

### Community 255 - "Community 255"
Cohesion: 1.00
Nodes (2): dd_decline_duration(), Engine-neutral `vectorbt.generic.nb.dd_decline_duration_nb`.

### Community 256 - "Community 256"
Cohesion: 1.00
Nodes (2): dd_drawdown(), Engine-neutral `vectorbt.generic.nb.dd_drawdown_nb`.

### Community 257 - "Community 257"
Cohesion: 1.00
Nodes (2): dd_recovery_duration_ratio(), Engine-neutral `vectorbt.generic.nb.dd_recovery_duration_ratio_nb`.

### Community 258 - "Community 258"
Cohesion: 1.00
Nodes (2): dd_recovery_duration(), Engine-neutral `vectorbt.generic.nb.dd_recovery_duration_nb`.

### Community 259 - "Community 259"
Cohesion: 1.00
Nodes (2): dd_recovery_return(), Engine-neutral `vectorbt.generic.nb.dd_recovery_return_nb`.

### Community 260 - "Community 260"
Cohesion: 1.00
Nodes (2): describe_reduce(), Engine-neutral `vectorbt.generic.nb.describe_reduce_nb`.

### Community 261 - "Community 261"
Cohesion: 1.00
Nodes (2): diff_1d(), Engine-neutral `vectorbt.generic.nb.diff_1d_nb`.

### Community 262 - "Community 262"
Cohesion: 1.00
Nodes (2): diff(), Engine-neutral `vectorbt.generic.nb.diff_nb`.

### Community 263 - "Community 263"
Cohesion: 1.00
Nodes (2): ewm_mean_1d(), Engine-neutral `vectorbt.generic.nb.ewm_mean_1d_nb`.

### Community 264 - "Community 264"
Cohesion: 1.00
Nodes (2): ewm_mean(), Engine-neutral `vectorbt.generic.nb.ewm_mean_nb`.

### Community 265 - "Community 265"
Cohesion: 1.00
Nodes (2): ewm_std_1d(), Engine-neutral `vectorbt.generic.nb.ewm_std_1d_nb`.

### Community 266 - "Community 266"
Cohesion: 1.00
Nodes (2): ewm_std(), Engine-neutral `vectorbt.generic.nb.ewm_std_nb`.

### Community 267 - "Community 267"
Cohesion: 1.00
Nodes (2): expanding_apply(), Engine-neutral `vectorbt.generic.nb.expanding_apply_nb`.

### Community 268 - "Community 268"
Cohesion: 1.00
Nodes (2): expanding_matrix_apply(), Engine-neutral `vectorbt.generic.nb.expanding_matrix_apply_nb`.

### Community 269 - "Community 269"
Cohesion: 1.00
Nodes (2): expanding_max_1d(), Engine-neutral `vectorbt.generic.nb.expanding_max_1d_nb`.

### Community 270 - "Community 270"
Cohesion: 1.00
Nodes (2): expanding_max(), Engine-neutral `vectorbt.generic.nb.expanding_max_nb`.

### Community 271 - "Community 271"
Cohesion: 1.00
Nodes (2): expanding_mean_1d(), Engine-neutral `vectorbt.generic.nb.expanding_mean_1d_nb`.

### Community 272 - "Community 272"
Cohesion: 1.00
Nodes (2): expanding_mean(), Engine-neutral `vectorbt.generic.nb.expanding_mean_nb`.

### Community 273 - "Community 273"
Cohesion: 1.00
Nodes (2): expanding_min_1d(), Engine-neutral `vectorbt.generic.nb.expanding_min_1d_nb`.

### Community 274 - "Community 274"
Cohesion: 1.00
Nodes (2): expanding_min(), Engine-neutral `vectorbt.generic.nb.expanding_min_nb`.

### Community 275 - "Community 275"
Cohesion: 1.00
Nodes (2): expanding_std_1d(), Engine-neutral `vectorbt.generic.nb.expanding_std_1d_nb`.

### Community 276 - "Community 276"
Cohesion: 1.00
Nodes (2): expanding_std(), Engine-neutral `vectorbt.generic.nb.expanding_std_nb`.

### Community 277 - "Community 277"
Cohesion: 1.00
Nodes (2): ffill_1d(), Engine-neutral `vectorbt.generic.nb.ffill_1d_nb`.

### Community 278 - "Community 278"
Cohesion: 1.00
Nodes (2): ffill(), Engine-neutral `vectorbt.generic.nb.ffill_nb`.

### Community 279 - "Community 279"
Cohesion: 1.00
Nodes (2): fillna_1d(), Engine-neutral `vectorbt.generic.nb.fillna_1d_nb`.

### Community 280 - "Community 280"
Cohesion: 1.00
Nodes (2): fillna(), Engine-neutral `vectorbt.generic.nb.fillna_nb`.

### Community 281 - "Community 281"
Cohesion: 1.00
Nodes (2): filter(), Engine-neutral `vectorbt.generic.nb.filter_nb`.

### Community 282 - "Community 282"
Cohesion: 1.00
Nodes (2): find_ranges(), Engine-neutral `vectorbt.generic.nb.find_ranges_nb`.

### Community 283 - "Community 283"
Cohesion: 1.00
Nodes (2): flat_reduce_grouped_to_array(), Engine-neutral `vectorbt.generic.nb.flat_reduce_grouped_to_array_nb`.

### Community 284 - "Community 284"
Cohesion: 1.00
Nodes (2): flat_reduce_grouped(), Engine-neutral `vectorbt.generic.nb.flat_reduce_grouped_nb`.

### Community 285 - "Community 285"
Cohesion: 1.00
Nodes (2): flatten_forder(), Engine-neutral `vectorbt.generic.nb.flatten_forder_nb`.

### Community 286 - "Community 286"
Cohesion: 1.00
Nodes (2): flatten_grouped(), Engine-neutral `vectorbt.generic.nb.flatten_grouped_nb`.

### Community 287 - "Community 287"
Cohesion: 1.00
Nodes (2): flatten_uniform_grouped(), Engine-neutral `vectorbt.generic.nb.flatten_uniform_grouped_nb`.

### Community 288 - "Community 288"
Cohesion: 1.00
Nodes (2): fshift_1d(), Engine-neutral `vectorbt.generic.nb.fshift_1d_nb`.

### Community 289 - "Community 289"
Cohesion: 1.00
Nodes (2): fshift(), Engine-neutral `vectorbt.generic.nb.fshift_nb`.

### Community 290 - "Community 290"
Cohesion: 1.00
Nodes (2): get_drawdowns(), Engine-neutral `vectorbt.generic.nb.get_drawdowns_nb`.

### Community 291 - "Community 291"
Cohesion: 1.00
Nodes (2): groupby_apply(), Engine-neutral `vectorbt.generic.nb.groupby_apply_nb`.

### Community 292 - "Community 292"
Cohesion: 1.00
Nodes (2): groupby_matrix_apply(), Engine-neutral `vectorbt.generic.nb.groupby_matrix_apply_nb`.

### Community 293 - "Community 293"
Cohesion: 1.00
Nodes (2): max_reduce(), Engine-neutral `vectorbt.generic.nb.max_reduce_nb`.

### Community 294 - "Community 294"
Cohesion: 1.00
Nodes (2): max_squeeze(), Engine-neutral `vectorbt.generic.nb.max_squeeze_nb`.

### Community 295 - "Community 295"
Cohesion: 1.00
Nodes (2): mean_reduce(), Engine-neutral `vectorbt.generic.nb.mean_reduce_nb`.

### Community 296 - "Community 296"
Cohesion: 1.00
Nodes (2): median_reduce(), Engine-neutral `vectorbt.generic.nb.median_reduce_nb`.

### Community 297 - "Community 297"
Cohesion: 1.00
Nodes (2): min_reduce(), Engine-neutral `vectorbt.generic.nb.min_reduce_nb`.

### Community 298 - "Community 298"
Cohesion: 1.00
Nodes (2): min_squeeze(), Engine-neutral `vectorbt.generic.nb.min_squeeze_nb`.

### Community 299 - "Community 299"
Cohesion: 1.00
Nodes (2): nancnt(), Engine-neutral `vectorbt.generic.nb.nancnt_nb`.

### Community 300 - "Community 300"
Cohesion: 1.00
Nodes (2): nancumprod(), Engine-neutral `vectorbt.generic.nb.nancumprod_nb`.

### Community 301 - "Community 301"
Cohesion: 1.00
Nodes (2): nancumsum(), Engine-neutral `vectorbt.generic.nb.nancumsum_nb`.

### Community 302 - "Community 302"
Cohesion: 1.00
Nodes (2): nanmax(), Engine-neutral `vectorbt.generic.nb.nanmax_nb`.

### Community 303 - "Community 303"
Cohesion: 1.00
Nodes (2): nanmean(), Engine-neutral `vectorbt.generic.nb.nanmean_nb`.

### Community 304 - "Community 304"
Cohesion: 1.00
Nodes (2): nanmedian(), Engine-neutral `vectorbt.generic.nb.nanmedian_nb`.

### Community 305 - "Community 305"
Cohesion: 1.00
Nodes (2): nanmin(), Engine-neutral `vectorbt.generic.nb.nanmin_nb`.

### Community 306 - "Community 306"
Cohesion: 1.00
Nodes (2): nanprod(), Engine-neutral `vectorbt.generic.nb.nanprod_nb`.

### Community 307 - "Community 307"
Cohesion: 1.00
Nodes (2): nanstd_1d(), Engine-neutral `vectorbt.generic.nb.nanstd_1d_nb`.

### Community 308 - "Community 308"
Cohesion: 1.00
Nodes (2): nanstd(), Engine-neutral `vectorbt.generic.nb.nanstd_nb`.

### Community 309 - "Community 309"
Cohesion: 1.00
Nodes (2): nansum(), Engine-neutral `vectorbt.generic.nb.nansum_nb`.

### Community 310 - "Community 310"
Cohesion: 1.00
Nodes (2): nth_index_reduce(), Engine-neutral `vectorbt.generic.nb.nth_index_reduce_nb`.

### Community 311 - "Community 311"
Cohesion: 1.00
Nodes (2): nth_reduce(), Engine-neutral `vectorbt.generic.nb.nth_reduce_nb`.

### Community 312 - "Community 312"
Cohesion: 1.00
Nodes (2): pct_change_1d(), Engine-neutral `vectorbt.generic.nb.pct_change_1d_nb`.

### Community 313 - "Community 313"
Cohesion: 1.00
Nodes (2): pct_change(), Engine-neutral `vectorbt.generic.nb.pct_change_nb`.

### Community 314 - "Community 314"
Cohesion: 1.00
Nodes (2): range_coverage(), Engine-neutral `vectorbt.generic.nb.range_coverage_nb`.

### Community 315 - "Community 315"
Cohesion: 1.00
Nodes (2): range_duration(), Engine-neutral `vectorbt.generic.nb.range_duration_nb`.

### Community 316 - "Community 316"
Cohesion: 1.00
Nodes (2): ranges_to_mask(), Engine-neutral `vectorbt.generic.nb.ranges_to_mask_nb`.

### Community 317 - "Community 317"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.row_apply_nb`., row_apply()

### Community 318 - "Community 318"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_apply_nb`., rolling_apply()

### Community 319 - "Community 319"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_matrix_apply_nb`., rolling_matrix_apply()

### Community 320 - "Community 320"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.set_by_mask_nb`., set_by_mask()

### Community 321 - "Community 321"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.reduce_nb`., reduce()

### Community 322 - "Community 322"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.reduce_to_array_nb`., reduce_to_array()

### Community 323 - "Community 323"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.reduce_grouped_nb`., reduce_grouped()

### Community 324 - "Community 324"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.reduce_grouped_to_array_nb`., reduce_grouped_to_array()

### Community 325 - "Community 325"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.squeeze_grouped_nb`., squeeze_grouped()

### Community 326 - "Community 326"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.set_by_mask_mult_1d_nb`., set_by_mask_mult_1d()

### Community 327 - "Community 327"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.std_reduce_nb`., std_reduce()

### Community 328 - "Community 328"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.sum_reduce_nb`., sum_reduce()

### Community 329 - "Community 329"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.set_by_mask_mult_nb`., set_by_mask_mult()

### Community 330 - "Community 330"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.sum_squeeze_nb`., sum_squeeze()

### Community 331 - "Community 331"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.shuffle_1d_nb`., shuffle_1d()

### Community 332 - "Community 332"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.shuffle_nb`., shuffle()

### Community 333 - "Community 333"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_min_1d_nb`., rolling_min_1d()

### Community 334 - "Community 334"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_min_nb`., rolling_min()

### Community 335 - "Community 335"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_max_1d_nb`., rolling_max_1d()

### Community 336 - "Community 336"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_max_nb`., rolling_max()

### Community 337 - "Community 337"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_mean_1d_nb`., rolling_mean_1d()

### Community 338 - "Community 338"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_mean_nb`., rolling_mean()

### Community 339 - "Community 339"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_std_1d_nb`., rolling_std_1d()

### Community 340 - "Community 340"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_std_nb`., rolling_std()

### Community 341 - "Community 341"
Cohesion: 1.00
Nodes (2): min_reduce_nb(), Return min (ignores NaNs).

### Community 342 - "Community 342"
Cohesion: 1.00
Nodes (2): min_squeeze_nb(), Return min (ignores NaNs) of a group.

### Community 343 - "Community 343"
Cohesion: 1.00
Nodes (2): nancnt_nb(), Compute count while ignoring NaNs.

### Community 344 - "Community 344"
Cohesion: 1.00
Nodes (2): _nancumprod_nb(), Numba equivalent of `np.nancumprod` along axis 0.

### Community 345 - "Community 345"
Cohesion: 1.00
Nodes (2): _nancumsum_nb(), Numba equivalent of `np.nancumsum` along axis 0.

### Community 346 - "Community 346"
Cohesion: 1.00
Nodes (2): nanmax_nb(), Numba-equivalent of `np.nanmax` along axis 0.

### Community 347 - "Community 347"
Cohesion: 1.00
Nodes (2): nanmean_nb(), Numba-equivalent of `np.nanmean` along axis 0.

### Community 348 - "Community 348"
Cohesion: 1.00
Nodes (2): nanmedian_nb(), Numba-equivalent of `np.nanmedian` along axis 0.

### Community 349 - "Community 349"
Cohesion: 1.00
Nodes (2): nanmin_nb(), Numba-equivalent of `np.nanmin` along axis 0.

### Community 350 - "Community 350"
Cohesion: 1.00
Nodes (2): _nanprod_nb(), Numba equivalent of `np.nanprod` along axis 0.

### Community 351 - "Community 351"
Cohesion: 1.00
Nodes (2): _nansum_nb(), Numba equivalent of `np.nansum` along axis 0.

### Community 352 - "Community 352"
Cohesion: 1.00
Nodes (2): nth_index_reduce_nb(), Return index of n-th element.

### Community 353 - "Community 353"
Cohesion: 1.00
Nodes (2): range_coverage_nb(), Get coverage of range records.      Set `overlapping` to True to get the number

### Community 354 - "Community 354"
Cohesion: 1.00
Nodes (2): range_duration_nb(), Get duration of each duration record.

### Community 355 - "Community 355"
Cohesion: 1.00
Nodes (2): ranges_to_mask_nb(), Convert ranges to 2-dim mask.

### Community 356 - "Community 356"
Cohesion: 1.00
Nodes (2): Apply function on each row.      `apply_func_nb` should accept index of the row,, row_apply_nb()

### Community 357 - "Community 357"
Cohesion: 1.00
Nodes (2): Set each element to a value by boolean mask., _set_by_mask_1d_nb()

### Community 358 - "Community 358"
Cohesion: 1.00
Nodes (2): Reduce each column into a single value using `reduce_func_nb`.      `reduce_func, reduce_nb()

### Community 359 - "Community 359"
Cohesion: 1.00
Nodes (2): Reduce each column into an array of values using `reduce_func_nb`.      `reduce_, reduce_to_array_nb()

### Community 360 - "Community 360"
Cohesion: 1.00
Nodes (2): Reduce each group of columns into a single value using `reduce_func_nb`.      `r, reduce_grouped_nb()

### Community 361 - "Community 361"
Cohesion: 1.00
Nodes (2): Reduce each group of columns into an array of values using `reduce_func_nb`., reduce_grouped_to_array_nb()

### Community 362 - "Community 362"
Cohesion: 1.00
Nodes (2): 2-dim version of `set_by_mask_1d_nb`., _set_by_mask_nb()

### Community 363 - "Community 363"
Cohesion: 1.00
Nodes (2): Squeeze each group of columns into a single column using `squeeze_func_nb`., squeeze_grouped_nb()

### Community 364 - "Community 364"
Cohesion: 1.00
Nodes (2): Return sum (ignores NaNs)., sum_reduce_nb()

### Community 365 - "Community 365"
Cohesion: 1.00
Nodes (2): Return value counts per column/group., value_counts_nb()

### Community 366 - "Community 366"
Cohesion: 1.00
Nodes (2): Return sum (ignores NaNs) of a group., sum_squeeze_nb()

### Community 367 - "Community 367"
Cohesion: 1.00
Nodes (2): Set each element in one array to the corresponding element in another by boolean, _set_by_mask_mult_1d_nb()

### Community 368 - "Community 368"
Cohesion: 1.00
Nodes (2): 2-dim version of `set_by_mask_mult_1d_nb`., _set_by_mask_mult_nb()

### Community 369 - "Community 369"
Cohesion: 1.00
Nodes (2): Shuffle each column in `a`.      Specify `seed` to make output deterministic., shuffle_1d_nb()

### Community 370 - "Community 370"
Cohesion: 1.00
Nodes (2): _plot(), Plot `close` and overlay it with the heatmap of `labels`.      `**kwargs` are pa

### Community 372 - "Community 372"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.returns.nb.up_capture_nb`., up_capture()

### Community 373 - "Community 373"
Cohesion: 1.00
Nodes (2): Rolling version of `sortino_ratio_nb`., rolling_sortino_ratio_nb()

### Community 374 - "Community 374"
Cohesion: 1.00
Nodes (2): Rolling version of `information_ratio_nb`., rolling_information_ratio_nb()

### Community 375 - "Community 375"
Cohesion: 1.00
Nodes (2): Rolling version of `beta_nb`., rolling_beta_nb()

### Community 376 - "Community 376"
Cohesion: 1.00
Nodes (2): Rolling version of `alpha_nb`., rolling_alpha_nb()

### Community 377 - "Community 377"
Cohesion: 1.00
Nodes (2): Rolling version of `tail_ratio_nb`., rolling_tail_ratio_nb()

### Community 378 - "Community 378"
Cohesion: 1.00
Nodes (2): Rolling version of `value_at_risk_nb`., rolling_value_at_risk_nb()

### Community 379 - "Community 379"
Cohesion: 1.00
Nodes (2): Rolling version of `cond_value_at_risk_nb`., rolling_cond_value_at_risk_nb()

### Community 380 - "Community 380"
Cohesion: 1.00
Nodes (2): Rolling version of `capture_nb`., rolling_capture_nb()

### Community 381 - "Community 381"
Cohesion: 1.00
Nodes (2): Calculate total return from returns., total_return_apply_nb()

### Community 382 - "Community 382"
Cohesion: 1.00
Nodes (2): Rolling version of `up_capture_nb`., rolling_up_capture_nb()

### Community 383 - "Community 383"
Cohesion: 1.00
Nodes (2): clean_enex_1d(), Engine-neutral `vectorbt.signals.nb.clean_enex_1d_nb`.

### Community 384 - "Community 384"
Cohesion: 1.00
Nodes (2): clean_enex(), Engine-neutral `vectorbt.signals.nb.clean_enex_nb`.

### Community 385 - "Community 385"
Cohesion: 1.00
Nodes (2): generate_ex(), Engine-neutral `vectorbt.signals.nb.generate_ex_nb`.

### Community 386 - "Community 386"
Cohesion: 1.00
Nodes (2): generate(), Engine-neutral `vectorbt.signals.nb.generate_nb`.

### Community 387 - "Community 387"
Cohesion: 1.00
Nodes (2): norm_avg_index_1d(), Engine-neutral `vectorbt.signals.nb.norm_avg_index_1d_nb`.

### Community 388 - "Community 388"
Cohesion: 1.00
Nodes (2): norm_avg_index(), Engine-neutral `vectorbt.signals.nb.norm_avg_index_nb`.

### Community 389 - "Community 389"
Cohesion: 1.00
Nodes (2): nth_index_1d(), Engine-neutral `vectorbt.signals.nb.nth_index_1d_nb`.

### Community 390 - "Community 390"
Cohesion: 1.00
Nodes (2): nth_index(), Engine-neutral `vectorbt.signals.nb.nth_index_nb`.

### Community 391 - "Community 391"
Cohesion: 1.00
Nodes (2): partition_ranges(), Engine-neutral `vectorbt.signals.nb.partition_ranges_nb`.

## Knowledge Gaps
- **821 isolated node(s):** `Fetch OHLCV data from Yahoo! Finance.`, `Store data into a hidden DIV to avoid repeatedly calling Yahoo's API.`, `Once index (dates) has changed, reset the date slider.`, `Once dates have changed, update entry/exit dates in custom pattern section.`, `Select all/random entry patterns or clear.` (+816 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 6`** (2 nodes): `Portfolio`, `Plot one column/group of gross exposure.          Args:             column (str)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `TestAccessors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `ReturnsAccessor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (1 nodes): `TestFactory`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (1 nodes): `Records`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (1 nodes): `TestChecks`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (1 nodes): `TestPortfolio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (1 nodes): `TestAccessors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (1 nodes): `TestAccessors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (1 nodes): `TestMappedArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (1 nodes): `TestReshapeFns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 69`** (2 nodes): `TestDrawdowns`, `TestRanges`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 71`** (1 nodes): `Data`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 74`** (1 nodes): `TestPortfolioRustParity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 79`** (1 nodes): `TestRecordsRustParity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 88`** (1 nodes): `TestColumnGrouper`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 89`** (1 nodes): `TestConfig`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 93`** (1 nodes): `TestArrayWrapper`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 96`** (1 nodes): `TestAccessors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 101`** (1 nodes): `TestIndexFns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 102`** (2 nodes): `TestLogs`, `TestRecords`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 115`** (1 nodes): `TestFromOrderFunc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 116`** (1 nodes): `TestGenerators`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 117`** (1 nodes): `TestDatetime`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 119`** (1 nodes): `TestEngineResolution`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 120`** (1 nodes): `TestGenericRustParity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 122`** (2 nodes): `Module`, `render_template()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 124`** (2 nodes): `TestData`, `TestDataUpdater`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 125`** (1 nodes): `TestGenerators`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 130`** (2 nodes): `fenced_code_blocks_hidden()`, `ToMarkdown`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 139`** (1 nodes): `TestSignalsRustParity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 141`** (1 nodes): `TestBasic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 142`** (1 nodes): `TestArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 153`** (1 nodes): `TestColumnMapper`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 168`** (2 nodes): `DrawdownRecord`, `RangeRecord`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 169`** (1 nodes): `TestDecorators`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 170`** (1 nodes): `TestMath`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 171`** (1 nodes): `TestTemplate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 175`** (2 nodes): `OrderRecord`, `TradeRecord`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 180`** (2 nodes): `Generate an empty Series/DataFrame of shape `shape` and fill with `fill_value`.`, `Generate an empty Series/DataFrame like `other` and fill with `fill_value`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 181`** (2 nodes): `Perform indexing on `BaseAccessor`.`, `Convert to 2-dim NumPy array.          See `vectorbt.base.reshape_fns.to_2d`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 220`** (1 nodes): `FlexArray<'py, T>`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 224`** (2 nodes): `pandas_applymap()`, `Pandas' native element-wise map, compatible with pandas 2.0+.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 225`** (1 nodes): `TestSettings`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 229`** (2 nodes): `Merge with another dict into one single dict.          See `merge_dicts`.`, `Create a new instance by copying and (optionally) changing the config.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 235`** (1 nodes): `setuptools`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 236`** (1 nodes): `nanmean_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 238`** (1 nodes): `Align to `other` on their axes.          Usage:             ```pycon`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 239`** (1 nodes): `Apply `apply_func` `ntimes` times and concatenate the results along columns.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 240`** (1 nodes): `Apply a function `apply_func`.          Args:             *args: Variable argume`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 241`** (1 nodes): `See `vectorbt.base.reshape_fns.broadcast_to`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 242`** (1 nodes): `Allows passing arguments to the initializer.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 243`** (1 nodes): `Accessor class for `pd.DataFrame`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 244`** (1 nodes): `See `vectorbt.base.reshape_fns.make_symmetric`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 245`** (1 nodes): `See `vectorbt.base.reshape_fns.repeat`.          Set `axis` to 1 for columns and`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 246`** (1 nodes): `Accessor class for `pd.Series`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 247`** (1 nodes): `See `vectorbt.base.reshape_fns.tile`.          Set `axis` to 1 for columns and 0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 248`** (1 nodes): `Convert to 1-dim NumPy array          See `vectorbt.base.reshape_fns.to_1d`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 249`** (1 nodes): `See `vectorbt.base.reshape_fns.to_dict`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 250`** (1 nodes): `See `vectorbt.base.reshape_fns.unstack_to_array`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 251`** (1 nodes): `See `vectorbt.base.reshape_fns.unstack_to_df`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 252`** (2 nodes): `count_reduce()`, `Engine-neutral `vectorbt.generic.nb.count_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 253`** (2 nodes): `crossed_above_1d()`, `Engine-neutral `vectorbt.generic.nb.crossed_above_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 254`** (2 nodes): `crossed_above()`, `Engine-neutral `vectorbt.generic.nb.crossed_above_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 255`** (2 nodes): `dd_decline_duration()`, `Engine-neutral `vectorbt.generic.nb.dd_decline_duration_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 256`** (2 nodes): `dd_drawdown()`, `Engine-neutral `vectorbt.generic.nb.dd_drawdown_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 257`** (2 nodes): `dd_recovery_duration_ratio()`, `Engine-neutral `vectorbt.generic.nb.dd_recovery_duration_ratio_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 258`** (2 nodes): `dd_recovery_duration()`, `Engine-neutral `vectorbt.generic.nb.dd_recovery_duration_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 259`** (2 nodes): `dd_recovery_return()`, `Engine-neutral `vectorbt.generic.nb.dd_recovery_return_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 260`** (2 nodes): `describe_reduce()`, `Engine-neutral `vectorbt.generic.nb.describe_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 261`** (2 nodes): `diff_1d()`, `Engine-neutral `vectorbt.generic.nb.diff_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 262`** (2 nodes): `diff()`, `Engine-neutral `vectorbt.generic.nb.diff_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 263`** (2 nodes): `ewm_mean_1d()`, `Engine-neutral `vectorbt.generic.nb.ewm_mean_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 264`** (2 nodes): `ewm_mean()`, `Engine-neutral `vectorbt.generic.nb.ewm_mean_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 265`** (2 nodes): `ewm_std_1d()`, `Engine-neutral `vectorbt.generic.nb.ewm_std_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 266`** (2 nodes): `ewm_std()`, `Engine-neutral `vectorbt.generic.nb.ewm_std_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 267`** (2 nodes): `expanding_apply()`, `Engine-neutral `vectorbt.generic.nb.expanding_apply_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 268`** (2 nodes): `expanding_matrix_apply()`, `Engine-neutral `vectorbt.generic.nb.expanding_matrix_apply_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 269`** (2 nodes): `expanding_max_1d()`, `Engine-neutral `vectorbt.generic.nb.expanding_max_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 270`** (2 nodes): `expanding_max()`, `Engine-neutral `vectorbt.generic.nb.expanding_max_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 271`** (2 nodes): `expanding_mean_1d()`, `Engine-neutral `vectorbt.generic.nb.expanding_mean_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 272`** (2 nodes): `expanding_mean()`, `Engine-neutral `vectorbt.generic.nb.expanding_mean_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 273`** (2 nodes): `expanding_min_1d()`, `Engine-neutral `vectorbt.generic.nb.expanding_min_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 274`** (2 nodes): `expanding_min()`, `Engine-neutral `vectorbt.generic.nb.expanding_min_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 275`** (2 nodes): `expanding_std_1d()`, `Engine-neutral `vectorbt.generic.nb.expanding_std_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 276`** (2 nodes): `expanding_std()`, `Engine-neutral `vectorbt.generic.nb.expanding_std_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 277`** (2 nodes): `ffill_1d()`, `Engine-neutral `vectorbt.generic.nb.ffill_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 278`** (2 nodes): `ffill()`, `Engine-neutral `vectorbt.generic.nb.ffill_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 279`** (2 nodes): `fillna_1d()`, `Engine-neutral `vectorbt.generic.nb.fillna_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 280`** (2 nodes): `fillna()`, `Engine-neutral `vectorbt.generic.nb.fillna_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 281`** (2 nodes): `filter()`, `Engine-neutral `vectorbt.generic.nb.filter_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 282`** (2 nodes): `find_ranges()`, `Engine-neutral `vectorbt.generic.nb.find_ranges_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 283`** (2 nodes): `flat_reduce_grouped_to_array()`, `Engine-neutral `vectorbt.generic.nb.flat_reduce_grouped_to_array_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 284`** (2 nodes): `flat_reduce_grouped()`, `Engine-neutral `vectorbt.generic.nb.flat_reduce_grouped_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 285`** (2 nodes): `flatten_forder()`, `Engine-neutral `vectorbt.generic.nb.flatten_forder_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 286`** (2 nodes): `flatten_grouped()`, `Engine-neutral `vectorbt.generic.nb.flatten_grouped_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 287`** (2 nodes): `flatten_uniform_grouped()`, `Engine-neutral `vectorbt.generic.nb.flatten_uniform_grouped_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 288`** (2 nodes): `fshift_1d()`, `Engine-neutral `vectorbt.generic.nb.fshift_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 289`** (2 nodes): `fshift()`, `Engine-neutral `vectorbt.generic.nb.fshift_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 290`** (2 nodes): `get_drawdowns()`, `Engine-neutral `vectorbt.generic.nb.get_drawdowns_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 291`** (2 nodes): `groupby_apply()`, `Engine-neutral `vectorbt.generic.nb.groupby_apply_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 292`** (2 nodes): `groupby_matrix_apply()`, `Engine-neutral `vectorbt.generic.nb.groupby_matrix_apply_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 293`** (2 nodes): `max_reduce()`, `Engine-neutral `vectorbt.generic.nb.max_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 294`** (2 nodes): `max_squeeze()`, `Engine-neutral `vectorbt.generic.nb.max_squeeze_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 295`** (2 nodes): `mean_reduce()`, `Engine-neutral `vectorbt.generic.nb.mean_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 296`** (2 nodes): `median_reduce()`, `Engine-neutral `vectorbt.generic.nb.median_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 297`** (2 nodes): `min_reduce()`, `Engine-neutral `vectorbt.generic.nb.min_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 298`** (2 nodes): `min_squeeze()`, `Engine-neutral `vectorbt.generic.nb.min_squeeze_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 299`** (2 nodes): `nancnt()`, `Engine-neutral `vectorbt.generic.nb.nancnt_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 300`** (2 nodes): `nancumprod()`, `Engine-neutral `vectorbt.generic.nb.nancumprod_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 301`** (2 nodes): `nancumsum()`, `Engine-neutral `vectorbt.generic.nb.nancumsum_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 302`** (2 nodes): `nanmax()`, `Engine-neutral `vectorbt.generic.nb.nanmax_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 303`** (2 nodes): `nanmean()`, `Engine-neutral `vectorbt.generic.nb.nanmean_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 304`** (2 nodes): `nanmedian()`, `Engine-neutral `vectorbt.generic.nb.nanmedian_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 305`** (2 nodes): `nanmin()`, `Engine-neutral `vectorbt.generic.nb.nanmin_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 306`** (2 nodes): `nanprod()`, `Engine-neutral `vectorbt.generic.nb.nanprod_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 307`** (2 nodes): `nanstd_1d()`, `Engine-neutral `vectorbt.generic.nb.nanstd_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 308`** (2 nodes): `nanstd()`, `Engine-neutral `vectorbt.generic.nb.nanstd_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 309`** (2 nodes): `nansum()`, `Engine-neutral `vectorbt.generic.nb.nansum_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 310`** (2 nodes): `nth_index_reduce()`, `Engine-neutral `vectorbt.generic.nb.nth_index_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 311`** (2 nodes): `nth_reduce()`, `Engine-neutral `vectorbt.generic.nb.nth_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 312`** (2 nodes): `pct_change_1d()`, `Engine-neutral `vectorbt.generic.nb.pct_change_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 313`** (2 nodes): `pct_change()`, `Engine-neutral `vectorbt.generic.nb.pct_change_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 314`** (2 nodes): `range_coverage()`, `Engine-neutral `vectorbt.generic.nb.range_coverage_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 315`** (2 nodes): `range_duration()`, `Engine-neutral `vectorbt.generic.nb.range_duration_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 316`** (2 nodes): `ranges_to_mask()`, `Engine-neutral `vectorbt.generic.nb.ranges_to_mask_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 317`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.row_apply_nb`.`, `row_apply()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 318`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_apply_nb`.`, `rolling_apply()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 319`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_matrix_apply_nb`.`, `rolling_matrix_apply()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 320`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.set_by_mask_nb`.`, `set_by_mask()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 321`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.reduce_nb`.`, `reduce()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 322`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.reduce_to_array_nb`.`, `reduce_to_array()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 323`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.reduce_grouped_nb`.`, `reduce_grouped()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 324`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.reduce_grouped_to_array_nb`.`, `reduce_grouped_to_array()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 325`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.squeeze_grouped_nb`.`, `squeeze_grouped()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 326`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.set_by_mask_mult_1d_nb`.`, `set_by_mask_mult_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 327`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.std_reduce_nb`.`, `std_reduce()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 328`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.sum_reduce_nb`.`, `sum_reduce()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 329`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.set_by_mask_mult_nb`.`, `set_by_mask_mult()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 330`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.sum_squeeze_nb`.`, `sum_squeeze()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 331`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.shuffle_1d_nb`.`, `shuffle_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 332`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.shuffle_nb`.`, `shuffle()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 333`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_min_1d_nb`.`, `rolling_min_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 334`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_min_nb`.`, `rolling_min()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 335`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_max_1d_nb`.`, `rolling_max_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 336`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_max_nb`.`, `rolling_max()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 337`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_mean_1d_nb`.`, `rolling_mean_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 338`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_mean_nb`.`, `rolling_mean()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 339`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_std_1d_nb`.`, `rolling_std_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 340`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_std_nb`.`, `rolling_std()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 341`** (2 nodes): `min_reduce_nb()`, `Return min (ignores NaNs).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 342`** (2 nodes): `min_squeeze_nb()`, `Return min (ignores NaNs) of a group.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 343`** (2 nodes): `nancnt_nb()`, `Compute count while ignoring NaNs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 344`** (2 nodes): `_nancumprod_nb()`, `Numba equivalent of `np.nancumprod` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 345`** (2 nodes): `_nancumsum_nb()`, `Numba equivalent of `np.nancumsum` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 346`** (2 nodes): `nanmax_nb()`, `Numba-equivalent of `np.nanmax` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 347`** (2 nodes): `nanmean_nb()`, `Numba-equivalent of `np.nanmean` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 348`** (2 nodes): `nanmedian_nb()`, `Numba-equivalent of `np.nanmedian` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 349`** (2 nodes): `nanmin_nb()`, `Numba-equivalent of `np.nanmin` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 350`** (2 nodes): `_nanprod_nb()`, `Numba equivalent of `np.nanprod` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 351`** (2 nodes): `_nansum_nb()`, `Numba equivalent of `np.nansum` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 352`** (2 nodes): `nth_index_reduce_nb()`, `Return index of n-th element.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 353`** (2 nodes): `range_coverage_nb()`, `Get coverage of range records.      Set `overlapping` to True to get the number`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 354`** (2 nodes): `range_duration_nb()`, `Get duration of each duration record.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 355`** (2 nodes): `ranges_to_mask_nb()`, `Convert ranges to 2-dim mask.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 356`** (2 nodes): `Apply function on each row.      `apply_func_nb` should accept index of the row,`, `row_apply_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 357`** (2 nodes): `Set each element to a value by boolean mask.`, `_set_by_mask_1d_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 358`** (2 nodes): `Reduce each column into a single value using `reduce_func_nb`.      `reduce_func`, `reduce_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 359`** (2 nodes): `Reduce each column into an array of values using `reduce_func_nb`.      `reduce_`, `reduce_to_array_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 360`** (2 nodes): `Reduce each group of columns into a single value using `reduce_func_nb`.      `r`, `reduce_grouped_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 361`** (2 nodes): `Reduce each group of columns into an array of values using `reduce_func_nb`.`, `reduce_grouped_to_array_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 362`** (2 nodes): `2-dim version of `set_by_mask_1d_nb`.`, `_set_by_mask_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 363`** (2 nodes): `Squeeze each group of columns into a single column using `squeeze_func_nb`.`, `squeeze_grouped_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 364`** (2 nodes): `Return sum (ignores NaNs).`, `sum_reduce_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 365`** (2 nodes): `Return value counts per column/group.`, `value_counts_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 366`** (2 nodes): `Return sum (ignores NaNs) of a group.`, `sum_squeeze_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 367`** (2 nodes): `Set each element in one array to the corresponding element in another by boolean`, `_set_by_mask_mult_1d_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 368`** (2 nodes): `2-dim version of `set_by_mask_mult_1d_nb`.`, `_set_by_mask_mult_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 369`** (2 nodes): `Shuffle each column in `a`.      Specify `seed` to make output deterministic.`, `shuffle_1d_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 370`** (2 nodes): `_plot()`, `Plot `close` and overlay it with the heatmap of `labels`.      `**kwargs` are pa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 372`** (2 nodes): `Engine-neutral `vectorbt.returns.nb.up_capture_nb`.`, `up_capture()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 373`** (2 nodes): `Rolling version of `sortino_ratio_nb`.`, `rolling_sortino_ratio_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 374`** (2 nodes): `Rolling version of `information_ratio_nb`.`, `rolling_information_ratio_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 375`** (2 nodes): `Rolling version of `beta_nb`.`, `rolling_beta_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 376`** (2 nodes): `Rolling version of `alpha_nb`.`, `rolling_alpha_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 377`** (2 nodes): `Rolling version of `tail_ratio_nb`.`, `rolling_tail_ratio_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 378`** (2 nodes): `Rolling version of `value_at_risk_nb`.`, `rolling_value_at_risk_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 379`** (2 nodes): `Rolling version of `cond_value_at_risk_nb`.`, `rolling_cond_value_at_risk_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 380`** (2 nodes): `Rolling version of `capture_nb`.`, `rolling_capture_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 381`** (2 nodes): `Calculate total return from returns.`, `total_return_apply_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 382`** (2 nodes): `Rolling version of `up_capture_nb`.`, `rolling_up_capture_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 383`** (2 nodes): `clean_enex_1d()`, `Engine-neutral `vectorbt.signals.nb.clean_enex_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 384`** (2 nodes): `clean_enex()`, `Engine-neutral `vectorbt.signals.nb.clean_enex_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 385`** (2 nodes): `generate_ex()`, `Engine-neutral `vectorbt.signals.nb.generate_ex_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 386`** (2 nodes): `generate()`, `Engine-neutral `vectorbt.signals.nb.generate_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 387`** (2 nodes): `norm_avg_index_1d()`, `Engine-neutral `vectorbt.signals.nb.norm_avg_index_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 388`** (2 nodes): `norm_avg_index()`, `Engine-neutral `vectorbt.signals.nb.norm_avg_index_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 389`** (2 nodes): `nth_index_1d()`, `Engine-neutral `vectorbt.signals.nb.nth_index_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 390`** (2 nodes): `nth_index()`, `Engine-neutral `vectorbt.signals.nb.nth_index_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 391`** (2 nodes): `partition_ranges()`, `Engine-neutral `vectorbt.signals.nb.partition_ranges_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Configured` connect `Community 15` to `Community 2`, `Community 8`, `Community 1`, `Community 144`, `Community 58`, `Community 59`, `Community 65`, `Community 46`, `Community 98`, `Community 109`, `Community 110`, `Community 91`, `Community 95`, `Community 164`, `Community 16`, `Community 34`, `Community 0`, `Community 4`, `Community 121`, `Community 111`, `Community 103`, `Community 229`, `Community 55`, `Community 128`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Why does `ArrayWrapper` connect `Community 2` to `Community 3`, `Community 242`, `Community 246`, `Community 243`, `Community 181`, `Community 180`, `Community 104`, `Community 248`, `Community 247`, `Community 245`, `Community 238`, `Community 161`, `Community 241`, `Community 244`, `Community 250`, `Community 251`, `Community 249`, `Community 240`, `Community 239`, `Community 4`, `Community 8`, `Community 46`, `Community 15`, `Community 71`, `Community 1`, `Community 0`, `Community 60`, `Community 33`, `Community 6`, `Community 34`, `Community 24`, `Community 21`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Why does `Config` connect `Community 0` to `Community 71`, `Community 1`, `Community 3`, `Community 4`, `Community 2`, `Community 60`, `Community 33`, `Community 6`, `Community 34`, `Community 24`, `Community 21`, `Community 19`, `Community 159`, `Community 15`, `Community 55`, `Community 121`, `Community 174`, `Community 111`, `Community 103`, `Community 229`, `Community 30`, `Community 56`, `Community 82`, `Community 27`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._
- **Are the 539 inferred relationships involving `Config` (e.g. with `Data` and `MetaData`) actually correct?**
  _`Config` has 539 INFERRED edges - model-reasoned connections that need verification._
- **Are the 497 inferred relationships involving `ArrayWrapper` (e.g. with `BaseAccessor` and `BaseDFAccessor`) actually correct?**
  _`ArrayWrapper` has 497 INFERRED edges - model-reasoned connections that need verification._
- **Are the 410 inferred relationships involving `Wrapping` (e.g. with `BaseAccessor` and `BaseDFAccessor`) actually correct?**
  _`Wrapping` has 410 INFERRED edges - model-reasoned connections that need verification._
- **Are the 279 inferred relationships involving `PlotsBuilderMixin` (e.g. with `Data` and `MetaData`) actually correct?**
  _`PlotsBuilderMixin` has 279 INFERRED edges - model-reasoned connections that need verification._