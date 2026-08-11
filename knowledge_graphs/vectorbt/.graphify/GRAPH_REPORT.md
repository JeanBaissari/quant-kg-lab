# Graph Report - vectorbt  (2026-08-06)

## Corpus Check
- 95 files · ~199,949 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3682 nodes · 9212 edges · 327 communities detected
- Extraction: 49% EXTRACTED · 51% INFERRED · 0% AMBIGUOUS · INFERRED: 4731 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: uses: 4731 · rationale_for: 1638 · contains: 1057 · method: 856 · calls: 779 · inherits: 150 · imports_from: 1


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 95 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `f989752`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Config` - 579 edges
2. `ArrayWrapper` - 535 edges
3. `Wrapping` - 426 edges
4. `PlotsBuilderMixin` - 292 edges
5. `StatsBuilderMixin` - 292 edges
6. `MappedArray` - 274 edges
7. `Configured` - 247 edges
8. `Drawdowns` - 242 edges
9. `Ranges` - 186 edges
10. `RepEval` - 184 edges

## Surprising Connections (you probably didn't know these)
- `Class that exposes methods to group columns.      `group_by` can be:      * bool` --uses--> `Configured`  [INFERRED]
  base/column_grouper.py → utils/config.py
- `Whether to allow enabling grouping.` --uses--> `Configured`  [INFERRED]
  base/column_grouper.py → utils/config.py
- `Check whether columns are grouped.` --uses--> `Configured`  [INFERRED]
  base/column_grouper.py → utils/config.py
- `Check whether column grouping has been enabled.` --uses--> `Configured`  [INFERRED]
  base/column_grouper.py → utils/config.py
- `Check whether column grouping has been disabled.` --uses--> `Configured`  [INFERRED]
  base/column_grouper.py → utils/config.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.03
Nodes (83): Mixin that implements `StatsBuilderMixin.stats`.      Required to be a subclass, Set of writeable attributes that will be saved/copied along with the config., Defaults for `StatsBuilderMixin.stats`.          See `stats_builder` in `vectorb, Metrics supported by `${cls_name}`.          ```json         ${metrics}, StatsBuilderMixin, MetaFields, MetaRecords, Meta class that exposes a read-only class property `MetaFields.field_config`. (+75 more)

### Community 1 - "Community 1"
Cohesion: 0.04
Nodes (106): ArrayWrapper, Class that downloads, updates, and manages data coming from a data source., Perform indexing on `Data`., Data dictionary keyed by symbol., `tz_localize` initially passed to `Data.download_symbol`., `tz_convert` initially passed to `Data.download_symbol`., `missing_index` initially passed to `Data.download_symbol`., `missing_columns` initially passed to `Data.download_symbol`. (+98 more)

### Community 2 - "Community 2"
Cohesion: 0.02
Nodes (86): AttrResolver, Allows passing arguments to the initializer., Accessor class for `pd.Series`., Accessor class for `pd.DataFrame`., Convert to 1-dim NumPy array          See `vectorbt.base.reshape_fns.to_1d`., See `vectorbt.base.reshape_fns.tile`.          Set `axis` to 1 for columns and 0, See `vectorbt.base.reshape_fns.repeat`.          Set `axis` to 1 for columns and, Align to `other` on their axes.          Usage:             ```pycon (+78 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (93): BaseAccessor, BaseDFAccessor, BaseSRAccessor, BaseDFAccessor, BaseSRAccessor, GenericDFAccessor, GenericSRAccessor, MetaGenericAccessor (+85 more)

### Community 4 - "Community 4"
Cohesion: 0.03
Nodes (90): Rust support result for an engine-neutral function call., RustSupport, alpha(), annualized_return(), annualized_volatility(), beta(), calmar_ratio(), capture() (+82 more)

### Community 5 - "Community 5"
Cohesion: 0.02
Nodes (86): approx_order_value(), asset_returns(), asset_value(), asset_value_grouped(), assets(), benchmark_value(), benchmark_value_grouped(), build_call_seq() (+78 more)

### Community 6 - "Community 6"
Cohesion: 0.05
Nodes (42): Class that stores index, columns and shape metadata for wrapping NumPy arrays., Perform indexing on `ArrayWrapper` and also return indexing metadata.          T, Perform indexing on `ArrayWrapper`, Derive metadata from an object., Derive metadata from shape., Get group-aware `ArrayWrapper.columns`., Get group-aware `ArrayWrapper.name`., Number of dimensions. (+34 more)

### Community 7 - "Community 7"
Cohesion: 0.04
Nodes (37): Perform indexing on `BaseAccessor`., Generate an empty Series/DataFrame of shape `shape` and fill with `fill_value`., Generate an empty Series/DataFrame like `other` and fill with `fill_value`., Apply function `apply_func` on index of the pandas object.          Set `axis` t, See `vectorbt.base.index_fns.stack_indexes`.          Set `on_top` to False to s, See `vectorbt.base.index_fns.drop_levels`.          See `BaseAccessor.apply_on_i, See `vectorbt.base.index_fns.rename_levels`.          See `BaseAccessor.apply_on, See `vectorbt.base.index_fns.select_levels`.          See `BaseAccessor.apply_on (+29 more)

### Community 8 - "Community 8"
Cohesion: 0.03
Nodes (68): asset_flow_nb(), asset_returns_nb(), asset_value_nb(), assets_nb(), benchmark_value_nb(), cash_nb(), dir_enex_signal_func_nb(), final_value_nb() (+60 more)

### Community 9 - "Community 9"
Cohesion: 0.05
Nodes (34): Config, SafeToStr, Reset to default theme., Extends `vectorbt.utils.config.Config` for global settings., Register template of a theme., Register templates of all themes., SettingsConfig, prepare_for_doc() (+26 more)

### Community 10 - "Community 10"
Cohesion: 0.04
Nodes (33): Whether to allow disabling grouping., Whether to allow changing groups., Check whether column grouping has changed in any way., Documented, Histogram, Create a histogram plot.          Args:             data (array_like): Data in a, Whether to plot horizontally., Whether to remove NaN values. (+25 more)

### Community 11 - "Community 11"
Cohesion: 0.05
Nodes (54): array_and_non_neg_int_compatible_with_rust(), array_compatible_with_rust(), array_shape_compatible_with_rust(), broadcast_2d_to_shape(), broadcast_to_shape(), callback_unsupported_with_rust(), clear_engine_cache(), col_map_compatible_with_rust() (+46 more)

### Community 12 - "Community 12"
Cohesion: 0.05
Nodes (30): Configured, Bar, Box, clean_labels(), Gauge, Heatmap, The value range of the gauge., A matplotlib-compatible colormap name. (+22 more)

### Community 13 - "Community 13"
Cohesion: 0.06
Nodes (41): MetaData, Dict that contains symbols as keys., symbol_dict, PlotsBuilderMixin, Mixin that implements `PlotsBuilderMixin.plots`.      Required to be a subclass, Set of writeable attributes that will be saved/copied along with the config., Defaults for `PlotsBuilderMixin.plots`.          See `plots_builder` in `vectorb, Subplots supported by `${cls_name}`.          ```json         ${subplots} (+33 more)

### Community 14 - "Community 14"
Cohesion: 0.05
Nodes (3): GenericAccessor, SignalsAccessor, SignalsSRAccessor

### Community 15 - "Community 15"
Cohesion: 0.06
Nodes (26): Blocking Telegram bot for `python-telegram-bot` 20 and later.          `**kwargs, Dispatcher-like application., Start the bot.              `**kwargs` are passed to `telegram.ext.Updater.start, Callback once the bot has been started.              Override to execute custom, Send message of any kind to `chat_id`., Send message of any kind to all in `TelegramBot.chat_ids`., Send text message to `chat_id`., Send text message to all in `TelegramBot.chat_ids`. (+18 more)

### Community 16 - "Community 16"
Cohesion: 0.04
Nodes (28): classmethod, object, attach_binary_magic_methods(), attach_unary_magic_methods(), CacheCondition, cached_method(), cached_methodT, cached_property (+20 more)

### Community 17 - "Community 17"
Cohesion: 0.06
Nodes (21): MetaPortfolio, Whether to forward-backward fill NaN values in `Portfolio.close`., A structured NumPy array of order records., Pre-process an attribute before resolution.          Uses the following keys:, Defaults for `Portfolio.stats`.          Merges `vectorbt.generic.stats_builder., Plot orders.          Args:             column (str): Name of the column to plot, Defaults for `Trades.plots`.          Merges `vectorbt.generic.ranges.Ranges.plo, Extends `vectorbt.generic.ranges.Ranges` for working with trade-like records, su (+13 more)

### Community 18 - "Community 18"
Cohesion: 0.04
Nodes (1): ReturnsAccessor

### Community 19 - "Community 19"
Cohesion: 0.04
Nodes (44): apply_on_mapped_nb(), apply_on_records_nb(), bottom_n_inout_map_nb(), col_map_nb(), col_map_select_nb(), col_range_nb(), col_range_select_nb(), _expand_mapped_nb() (+36 more)

### Community 20 - "Community 20"
Cohesion: 0.07
Nodes (43): broadcast(), broadcast_index(), broadcast_to(), broadcast_to_array_of(), broadcast_to_axis_of(), flex_choose_i_and_col_nb(), flex_select_auto_nb(), flex_select_nb() (+35 more)

### Community 21 - "Community 21"
Cohesion: 0.08
Nodes (1): Records

### Community 22 - "Community 22"
Cohesion: 0.05
Nodes (36): any_squeeze_nb(), apply_and_reduce_nb(), apply_nb(), applymap_nb(), argmax_reduce_nb(), argmin_reduce_nb(), _bshift_1d_nb(), _bshift_nb() (+28 more)

### Community 23 - "Community 23"
Cohesion: 0.07
Nodes (36): apply_and_concat_multiple(), apply_and_concat_multiple_nb(), apply_and_concat_multiple_ray(), apply_and_concat_none(), apply_and_concat_none_nb(), apply_and_concat_one(), apply_and_concat_one_nb(), apply_and_concat_one_ray() (+28 more)

### Community 24 - "Community 24"
Cohesion: 0.05
Nodes (36): atr_apply(), atr_cache(), bb_apply(), bb_cache(), ma(), ma_apply(), ma_cache(), macd_apply() (+28 more)

### Community 25 - "Community 25"
Cohesion: 0.07
Nodes (36): atr_apply_nb(), atr_cache_nb(), bb_apply_nb(), bb_cache_nb(), ma_apply_nb(), ma_cache_nb(), ma_nb(), macd_apply_nb() (+28 more)

### Community 26 - "Community 26"
Cohesion: 0.06
Nodes (35): Exception, AccumulationModeT, AdjustSLContext, AdjustTPContext, CallSeqTypeT, ConflictModeT, DirectionConflictModeT, DirectionT (+27 more)

### Community 27 - "Community 27"
Cohesion: 0.08
Nodes (34): align_index_to(), _align_index_to_nb(), align_indexes(), combine_indexes(), drop_duplicate_levels(), drop_levels(), drop_redundant_levels(), find_first_occurrence() (+26 more)

### Community 28 - "Community 28"
Cohesion: 0.07
Nodes (19): build_param_indexer(), iLoc, indexing_on_mapper(), IndexingBase, Loc, LocBase, _normalize_numpy_scalars(), ParamLoc (+11 more)

### Community 29 - "Community 29"
Cohesion: 0.08
Nodes (30): bn_cont_sat_trend_labels_nb(), bn_cont_trend_labels_nb(), bn_trend_labels_nb(), breakout_labels_nb(), fixed_labels_apply_nb(), future_max_apply_nb(), future_mean_apply_nb(), future_min_apply_nb() (+22 more)

### Community 30 - "Community 30"
Cohesion: 0.09
Nodes (14): Portfolio, Class for modeling portfolio and measuring its performance.      Args:         w, Regroup this object.          See `vectorbt.base.array_wrapper.Wrapping.regroup`, `Portfolio.get_orders` with default arguments., Get order records.          See `vectorbt.portfolio.orders.Orders`., Get gross exposure.          Gross exposure is the sum of absolute position valu, Plot one column/group of orders., Plot one column/group of trades. (+6 more)

### Community 31 - "Community 31"
Cohesion: 0.07
Nodes (30): bottom_n_mapped_mask(), col_map(), col_map_select(), col_range(), col_range_select(), expand_mapped(), is_col_idx_sorted(), is_col_sorted() (+22 more)

### Community 32 - "Community 32"
Cohesion: 0.08
Nodes (15): first_price(), first_volume(), last_price(), last_volume(), OHLCVDFAccessor, Return the first valid OHLC price., Return the last valid OHLC price., Return the first valid volume. (+7 more)

### Community 33 - "Community 33"
Cohesion: 0.07
Nodes (2): BaseAccessor, GenericAccessor

### Community 34 - "Community 34"
Cohesion: 0.08
Nodes (14): DataUpdater, Data instance.          See `vectorbt.data.base.Data`., Schedule manager instance.          See `vectorbt.utils.schedule_.ScheduleManage, Method that updates data.          Override to do pre- and postprocessing., Schedule `DataUpdater.update`.          For `*args`, `to` and `tags`, see `vecto, Class for scheduling data updates.      Usage:         * Update in the foregroun, Create a new job that runs every `interval` units of time.          `*args` can, Run pending jobs in a loop. (+6 more)

### Community 35 - "Community 35"
Cohesion: 0.07
Nodes (26): bn_cont_sat_trend_labels(), bn_cont_trend_labels(), bn_trend_labels(), breakout_labels(), fixed_labels_apply(), future_max_apply(), future_mean_apply(), future_min_apply() (+18 more)

### Community 36 - "Community 36"
Cohesion: 0.11
Nodes (14): Get cash flow series per column/group.          Use `free` to return the flow of, `Portfolio.get_init_cash` with default arguments., Initial amount of cash per column/group with default arguments.          !!! not, Get cash balance series per column/group.          See the explanation on `in_si, Get portfolio value series per column/group.          By default, will generate, Get total profit per column/group.          Calculated directly from order recor, Get total profit per column/group., Get total profit per column/group. (+6 more)

### Community 37 - "Community 37"
Cohesion: 0.10
Nodes (26): close_position_nb(), generate_stop_signal_nb(), get_stop_price_nb(), is_grouped_nb(), order_nb(), Generate stop signal and change accumulation if needed., Resolve price and slippage of a stop order., Resolve any conflict between an entry and an exit. (+18 more)

### Community 38 - "Community 38"
Cohesion: 0.13
Nodes (1): Data

### Community 39 - "Community 39"
Cohesion: 0.08
Nodes (24): any_squeeze(), apply(), apply_and_reduce(), applymap(), argmax_reduce(), argmin_reduce(), bfill(), bfill_1d() (+16 more)

### Community 40 - "Community 40"
Cohesion: 0.09
Nodes (24): alpha_1d_nb(), alpha_nb(), beta_1d_nb(), beta_nb(), Rolling version of `cum_returns_final_nb`., Rolling version of `annualized_return_nb`., Rolling version of `annualized_volatility_nb`., Rolling version of `max_drawdown_nb`. (+16 more)

### Community 41 - "Community 41"
Cohesion: 0.10
Nodes (19): DirNamesMixin, GenericDFAccessor, GenericSRAccessor, Accessor, Decorator to register a custom `pd.DataFrame` accessor on top of the `pd.DataFra, The main vectorbt accessor for `pd.Series`., The main vectorbt accessor for `pd.DataFrame`., Decorator to register a `pd.Series` accessor on top of a parent accessor. (+11 more)

### Community 42 - "Community 42"
Cohesion: 0.16
Nodes (24): check_group_init_cash_nb(), flex_simulate_nb(), flex_simulate_row_wise_nb(), get_group_value_ctx_nb(), get_group_value_nb(), init_last_pos_record_nb(), init_records_nb(), Replace infinity price in an order. (+16 more)

### Community 43 - "Community 43"
Cohesion: 0.12
Nodes (22): _OHLCSTCX, _OHLCSTX, _RAND, _RANDNX, _RANDX, Random entry and exit signal generator based on the number of signals.      Gene, Random entry signal generator based on probabilities.      Generates `entries` b, Random exit signal generator based on probabilities.      Generates `exits` base (+14 more)

### Community 44 - "Community 44"
Cohesion: 0.09
Nodes (13): Class for wrapping default values., Extends dict with config features such as nested updates, frozen keys/values, an, Parameters for copying `dct`., Dict to fall back to in case of resetting., Parameters for copying `reset_dct`., Whether to deny updates to the keys and values of the config., Whether to deny any updates to the config., Whether to do operations recursively on each child dict. (+5 more)

### Community 45 - "Community 45"
Cohesion: 0.10
Nodes (21): convert_naive_time(), convert_tzaware_time(), datetime_to_ms(), freq_to_timedelta(), get_local_tz(), interval_to_ms(), is_tz_aware(), naive_to_tzaware_time() (+13 more)

### Community 46 - "Community 46"
Cohesion: 0.12
Nodes (16): copy_dict(), get_func_arg_names(), get_func_kwargs(), merge_dicts(), Copy dict based on a copy mode.      The following modes are supported:      * ', Update dict with keys and values from other dict.      Set `nested` to True to u, Merge dicts.      Args:         *dicts (dict): Dicts.         to_dict (bool): Wh, Select keyword arguments. (+8 more)

### Community 47 - "Community 47"
Cohesion: 0.12
Nodes (14): Figure, FigureMixin, FigureWidget, get_domain(), make_figure(), make_subplots(), Makes subplots and passes them to `FigureWidget`., Get domain of a coordinate axis. (+6 more)

### Community 48 - "Community 48"
Cohesion: 0.10
Nodes (8): IndicatorFactory, IndicatorBase, PlotsBuilderMixin, Build signal generator class around entry and exit choice functions.          A, A factory for building signal generators.      Extends `vectorbt.indicators.fact, SignalFactory, StatsBuilderMixin, Wrapping

### Community 49 - "Community 49"
Cohesion: 0.10
Nodes (9): Whether to share cash within the same group., A structured NumPy array of log records., Orders, Perform indexing on `Orders`., Reference price such as close (optional)., Defaults for `Orders.stats`.          Merges `vectorbt.records.base.Records.stat, Plot orders.          Args:             column (str): Name of the column to plot, Defaults for `Orders.plots`.          Merges `vectorbt.records.base.Records.plot (+1 more)

### Community 50 - "Community 50"
Cohesion: 0.11
Nodes (9): Simulate portfolio from entry and exit signals.          See `vectorbt.portfolio, Simulate portfolio from holding.          Based on `Portfolio.from_signals`., Simulate portfolio from random entry and exit signals.          Generates signal, Price per unit series., Post-process an object after resolution.          Uses the following keys:, Logs, Extends `Records` for working with log records., Defaults for `Logs.stats`.          Merges `vectorbt.records.base.Records.stats_ (+1 more)

### Community 51 - "Community 51"
Cohesion: 0.11
Nodes (19): asset_value_grouped_nb(), benchmark_value_grouped_nb(), cash_flow_grouped_nb(), cash_grouped_nb(), cash_in_sim_order_nb(), check_group_lens_nb(), Squeeze each group of columns into a single column using sum operation., Get cash flow series per group. (+11 more)

### Community 52 - "Community 52"
Cohesion: 0.12
Nodes (18): get_ranges_arr(), insert_argsort_nb(), is_sorted(), is_sorted_nb(), max_rel_rescale(), min_rel_rescale(), Rescale elements in `a` relatively to maximum., Rescale a float array into an int array. (+10 more)

### Community 53 - "Community 53"
Cohesion: 0.13
Nodes (11): GBMData, generate_gbm_paths(), Generate the symbol using `generate_gbm_paths`.          Args:             symbo, Update the symbol.          `**kwargs` will override keyword arguments passed to, `Data` for synthetically generated data., Abstract method to generate a symbol., Download the symbol.          Generates datetime index and passes it to `Synthet, Update the symbol.          `**kwargs` will override keyword arguments passed to (+3 more)

### Community 54 - "Community 54"
Cohesion: 0.13
Nodes (13): Handler, LogHandler, _maybe_await(), _message_type(), Pass bot object to func command., Handler to log user updates., Sends `action` while processing func command.          Suitable only for bound c, Pass bot object to func command. (+5 more)

### Community 55 - "Community 55"
Cohesion: 0.15
Nodes (10): Job, Scheduler, AsyncJob, AsyncScheduler, CancelledError, Thrown for the operation to be cancelled., Async `Scheduler.run_pending`., Async `Scheduler.run_all`. (+2 more)

### Community 56 - "Community 56"
Cohesion: 0.17
Nodes (9): Get asset flow series per column.          Returns the total transacted amount o, Get asset series per column.          Returns the current position at each time, Get position mask per column/group.          An element is True if the asset is, Get position coverage per column/group., Plot one column of asset flow.          Args:             column (str): Name of, Plot one column of assets.          Args:             column (str): Name of the, EntryTrades, Extends `Trades` for working with entry trade records. (+1 more)

### Community 57 - "Community 57"
Cohesion: 0.13
Nodes (8): Engine preference for dispatch functions., Build portfolio from a custom order function.          !!! hint             See, Sequence of calls per row and group., `Portfolio.get_qs` with default arguments., Get quantstats adapter of type `vectorbt.returns.qs_adapter.QSAdapter`., Names to associate with this object., QSAdapter, Adapter class for quantstats.

### Community 58 - "Community 58"
Cohesion: 0.13
Nodes (16): assert_engine_func(), assert_numba_func(), assert_rust_func(), func_accepts_arg(), is_engine_compatible_func(), is_engine_dispatch_func(), is_numba_func(), is_rust_func() (+8 more)

### Community 59 - "Community 59"
Cohesion: 0.16
Nodes (8): Load dumps from a file and create new instance., Load dumps from a file and update this instance., Update the config.          See `update_dict`., Shallow operation, primarily used by `copy.copy`.          Does not take into ac, Deep operation, primarily used by `copy.deepcopy`.          Does not take into a, Copy the instance in the same way it's done during initialization.          `cop, Load dumps from a file and update this instance.          !!! note             U, Force-update the config.

### Community 60 - "Community 60"
Cohesion: 0.14
Nodes (8): Perform indexing on `Portfolio`., Default `vectorbt.portfolio.trades.Trades` to use across `Portfolio`., `Portfolio.get_logs` with default arguments., Get log records.          See `vectorbt.portfolio.logs.Logs`., Defaults for `Portfolio.plot`.          Merges `vectorbt.generic.plots_builder.P, Positions, Extends `Trades` for working with position records., Build `Positions` from `Trades`.

### Community 61 - "Community 61"
Cohesion: 0.13
Nodes (14): between_partition_ranges_nb(), between_ranges_nb(), between_two_ranges_nb(), first_choice_nb(), ohlc_stop_choice_nb(), Create a record of type `vectorbt.generic.enums.range_dt` for each range between, Create a record of type `vectorbt.generic.enums.range_dt` for each range between, Create a record of type `vectorbt.generic.enums.range_dt` for each range between (+6 more)

### Community 62 - "Community 62"
Cohesion: 0.13
Nodes (14): assert_in(), assert_len_equal(), assert_level_not_exists(), assert_not_none(), is_hashable(), is_np_array(), is_valid_variable_name(), Check whether the argument can be hashed. (+6 more)

### Community 63 - "Community 63"
Cohesion: 0.18
Nodes (7): Get return series per column/group based on portfolio value., Get asset return series per column/group.          This type of returns is based, `Portfolio.get_returns_acc` with default arguments., Get returns accessor of type `vectorbt.returns.accessors.ReturnsAccessor`., Get return series per column/group based on benchmark value., Compute various statistics on returns of this portfolio.          See `Portfolio, Plot one column/group of cumulative returns.          Args:             column (

### Community 64 - "Community 64"
Cohesion: 0.15
Nodes (7): Simulate portfolio from orders - size, price, fees, and other information., `Portfolio.get_entry_trades` with default arguments., Get entry trade records.          See `vectorbt.portfolio.trades.EntryTrades`., `Portfolio.get_exit_trades` with default arguments., Get exit trade records.          See `vectorbt.portfolio.trades.ExitTrades`., `Portfolio.get_trades` with default arguments., Get trade/position records depending upon `Portfolio.trades_type`.

### Community 65 - "Community 65"
Cohesion: 0.14
Nodes (14): copy_trade_record_nb(), fill_entry_trades_in_position_nb(), fill_position_record_nb(), fill_trade_record_nb(), get_entry_trades_nb(), get_exit_trades_nb(), get_positions_nb(), get_trade_stats_nb() (+6 more)

### Community 66 - "Community 66"
Cohesion: 0.14
Nodes (14): annualized_return_1d_nb(), annualized_return_nb(), capture_1d_nb(), capture_nb(), cum_returns_final_1d_nb(), cum_returns_final_nb(), 2-dim version of `cum_returns_final_1d_nb`., Mean annual growth rate of returns.      This is equivalent to the compound annu (+6 more)

### Community 67 - "Community 67"
Cohesion: 0.16
Nodes (13): between_partition_ranges(), between_ranges(), between_two_ranges(), part_pos_rank(), rank(), _rank_support(), Engine-neutral `vectorbt.signals.nb.between_ranges_nb`., Engine-neutral `vectorbt.signals.nb.between_two_ranges_nb`. (+5 more)

### Community 68 - "Community 68"
Cohesion: 0.15
Nodes (9): Data, CCXTData, `Data` for data coming from `yfinance`.      Stocks are usually in the timezone, Download the symbol.          Args:             symbol (str): Symbol., Update the symbol.          `**kwargs` will override keyword arguments passed to, `Data` for data coming from `ccxt`.      Usage:         * Fetch the 1-minute dat, Download the symbol.          Args:             symbol (str): Symbol., Update the symbol.          `**kwargs` will override keyword arguments passed to (+1 more)

### Community 69 - "Community 69"
Cohesion: 0.26
Nodes (1): IndicatorFactory

### Community 70 - "Community 70"
Cohesion: 0.22
Nodes (12): _BOLB, _FIXLB, _LEXLB, _MEANLB, _plot(), Label generator based on `vectorbt.labels.nb.mean_labels_apply_nb`., Label generator based on `vectorbt.labels.nb.local_extrema_apply_nb`., Label generator based on `vectorbt.labels.nb.trend_labels_apply_nb`. (+4 more)

### Community 71 - "Community 71"
Cohesion: 0.17
Nodes (12): _add_var_nb(), expanding_std_1d_nb(), expanding_std_nb(), Return expanding standard deviation.      Numba equivalent to `pd.Series(a).expa, 2-dim version of `expanding_std_1d_nb`., Add a value to a rolling variance state., Remove a value from a rolling variance state., Return rolling standard deviation.      Numba equivalent to `pd.Series(a).rollin (+4 more)

### Community 72 - "Community 72"
Cohesion: 0.17
Nodes (12): asset_flow(), cash_flow(), get_entry_trades(), get_exit_trades(), order_record_array_compatible_with_rust(), Engine-neutral `vectorbt.portfolio.nb.get_entry_trades_nb`., Engine-neutral `vectorbt.portfolio.nb.get_exit_trades_nb`., Engine-neutral `vectorbt.portfolio.nb.asset_flow_nb`. (+4 more)

### Community 73 - "Community 73"
Cohesion: 0.20
Nodes (12): assert_array_equal(), assert_meta_equal(), assert_type_equal(), is_any_array(), is_frame(), is_pandas(), Check whether the argument is `pd.DataFrame`., Check whether the argument is `pd.Series` or `pd.DataFrame`. (+4 more)

### Community 74 - "Community 74"
Cohesion: 0.17
Nodes (12): assert_dtype(), assert_dtype_equal(), assert_ndim(), assert_shape_equal(), assert_subdtype(), Raise exception if the argument is not of data type `dtype`., Raise exception if the argument is not a sub data type of `dtype`., Raise exception if the first argument and the second argument have different dat (+4 more)

### Community 75 - "Community 75"
Cohesion: 0.17
Nodes (5): Pickleable, PickleableDict, Superclass that defines abstract properties and methods for pickle-able classes., Save dumps to a file., Dict that may contain values of type `Pickleable`.

### Community 76 - "Community 76"
Cohesion: 0.20
Nodes (10): broadcast_params(), create_param_combs(), create_param_product(), flatten_param_tuples(), Cast Python list to typed list.      Direct construction is flawed in Numba 0.52, Flattens a nested list of iterables using unzipping., Create arbitrary parameter combinations from the operation tree `op_tree`., Broadcast parameters in `param_list`. (+2 more)

### Community 77 - "Community 77"
Cohesion: 0.20
Nodes (5): Forward-backward-fill NaN values in `Portfolio.close`, Get asset value series per column/group., Get market benchmark value series per column/group.          If grouped, evenly, Get total benchmark return., Plot one column/group of asset value.          Args:             column (str): N

### Community 78 - "Community 78"
Cohesion: 0.20
Nodes (5): Get group-aware column array., Column index.          Faster than `ColumnMapper.col_map` but only compatible wi, Get group-aware column range., Column map.          More flexible than `ColumnMapper.col_range`.         More s, Get group-aware column map.

### Community 79 - "Community 79"
Cohesion: 0.20
Nodes (10): generate_ex_nb(), generate_ohlc_stop_ex_nb(), generate_rand_ex_by_prob_nb(), generate_rand_ex_nb(), generate_stop_ex_nb(), Pick exit signals using `exit_choice_func_nb` after each signal in `entries`., Pick an exit after each entry in `entries`.      Specify `seed` to make output d, Pick an exit after each entry in `entries` by probability `prob`.      `prob` sh (+2 more)

### Community 80 - "Community 80"
Cohesion: 0.20
Nodes (10): generate_nb(), generate_rand_by_prob_nb(), generate_rand_enex_nb(), generate_rand_nb(), rand_enex_apply_nb(), Create a boolean matrix of `shape` and pick a number of signals randomly.      S, Create a boolean matrix of `shape` and pick signals randomly by probability `pro, Pick a number of entries and the same number of exits one after another.      Re (+2 more)

### Community 81 - "Community 81"
Cohesion: 0.20
Nodes (10): is_index(), is_mapping(), is_mapping_like(), is_namedtuple(), is_series(), Check whether object is an instance of namedtuple., Check whether the argument is `pd.Series`., Check whether the argument is `pd.Index`. (+2 more)

### Community 82 - "Community 82"
Cohesion: 0.29
Nodes (9): add_nb(), is_addition_zero_nb(), is_close_nb(), is_close_or_less_nb(), is_less_nb(), Tell whether two values are approximately equal., Tell whether the first value is approximately less than or equal to the second v, Tell whether the first value is approximately less than the second value. (+1 more)

### Community 84 - "Community 84"
Cohesion: 0.28
Nodes (6): Relative Strength Index (RSI).      Compares the magnitude of recent gains and l, Plot `RSI.rsi`.          Args:             column (str): Name of the column to p, Stochastic Oscillator (STOCH).      A stochastic oscillator is a momentum indica, Plot `STOCH.percent_k` and `STOCH.percent_d`.          Args:             column, _RSI, _STOCH

### Community 85 - "Community 85"
Cohesion: 0.28
Nodes (9): buy_nb(), execute_order_nb(), order_not_filled_nb(), Execute an order without persistence., Sell or/and short sell., Execute an order given the current state.      Args:         state (ProcessOrder, Return `OrderResult` for order that hasn't been filled., sell_nb() (+1 more)

### Community 86 - "Community 86"
Cohesion: 0.22
Nodes (9): fill_log_record_nb(), fill_order_record_nb(), process_order_nb(), raise_rejected_order_nb(), Fill an order record., Raise an `vectorbt.portfolio.enums.RejectedOrderError`., Update valuation price and value., Process an order by executing it, saving relevant information to the logs, and r (+1 more)

### Community 87 - "Community 87"
Cohesion: 0.22
Nodes (2): ReturnsDFAccessor, ReturnsSRAccessor

### Community 88 - "Community 88"
Cohesion: 0.22
Nodes (9): assert_equal(), _functions_equal(), is_deep_equal(), is_equal(), Check whether two objects are equal., Compare functions by their semantic behavior, ignoring position metadata.      C, Check whether two objects are equal (deep check)., Raise exception if the first argument and the second argument are different. (+1 more)

### Community 89 - "Community 89"
Cohesion: 0.25
Nodes (5): BinanceData, `Data` for data coming from `python-binance`.      Usage:         * Fetch the 1-, Override `vectorbt.data.base.Data.download` to instantiate a Binance client., Download the symbol.          Args:             symbol (str): Symbol., Update the symbol.          `**kwargs` will override keyword arguments passed to

### Community 90 - "Community 90"
Cohesion: 0.25
Nodes (7): dict, atomic_dict, AtomicConfig, convert_to_dict(), Dict that behaves like a single value when merging., Config that behaves like a single value when merging., Convert any dict (apart from `atomic_dict`) to `dict`.      Set `nested` to True

### Community 91 - "Community 91"
Cohesion: 0.25
Nodes (8): describe_reduce_nb(), nanstd_1d_nb(), nanstd_nb(), Return std (ignores NaNs)., Return descriptive statistics (ignores NaNs).      Numba equivalent to `pd.Serie, Numba-equivalent of `np.nanstd`., 2-dim version of `nanstd_1d_nb`., std_reduce_nb()

### Community 92 - "Community 92"
Cohesion: 0.25
Nodes (8): expanding_mean_1d_nb(), expanding_mean_nb(), Return expanding mean.      Numba equivalent to `pd.Series(a).expanding(min_peri, 2-dim version of `expanding_mean_1d_nb`., Return rolling mean.      Numba equivalent to `pd.Series(a).rolling(window, min_, 2-dim version of `rolling_mean_1d_nb`., rolling_mean_1d_nb(), rolling_mean_nb()

### Community 93 - "Community 93"
Cohesion: 0.25
Nodes (5): Either split into `n` ranges each `range_len` long, or split into ranges between, Split by rolling a window.          `**kwargs` are passed to `split_ranges_into_, Similar to `RollingSplitter.split`, but expanding.          `**kwargs` are passe, Generate ranges between each in `start_idxs` and `end_idxs` and     optionally s, split_ranges_into_sets()

### Community 94 - "Community 94"
Cohesion: 0.25
Nodes (8): get_positions(), Engine-neutral `vectorbt.portfolio.nb.trade_winning_streak_nb`., Engine-neutral `vectorbt.portfolio.nb.trade_losing_streak_nb`., Engine-neutral `vectorbt.portfolio.nb.get_positions_nb`., Return whether trade records have the exact Rust-compatible dtype., trade_losing_streak(), trade_record_array_compatible_with_rust(), trade_winning_streak()

### Community 95 - "Community 95"
Cohesion: 0.25
Nodes (8): approx_order_value_nb(), get_col_elem_nb(), Sort call sequence `call_seq_out` based on the value of each potential order., Sort call sequence attached to `vectorbt.portfolio.enums.SegmentContext`.      S, Get the current element using flexible indexing given the context and the column, Approximate value of an order., sort_call_seq_nb(), sort_call_seq_out_nb()

### Community 96 - "Community 96"
Cohesion: 0.25
Nodes (8): build_call_seq(), build_call_seq_nb(), Shuffle the call sequence array., Build a new call sequence array., Force the call sequence array to pass our requirements., Not compiled but faster version of `build_call_seq_nb`., require_call_seq(), shuffle_call_seq_nb()

### Community 97 - "Community 97"
Cohesion: 0.25
Nodes (8): calmar_ratio_1d_nb(), calmar_ratio_nb(), max_drawdown_1d_nb(), max_drawdown_nb(), Total maximum drawdown (MDD)., 2-dim version of `max_drawdown_1d_nb`., Calmar ratio, or drawdown ratio, of a strategy., 2-dim version of `calmar_ratio_1d_nb`.

### Community 98 - "Community 98"
Cohesion: 0.25
Nodes (8): downside_risk_1d_nb(), downside_risk_nb(), Downside deviation below a threshold., 2-dim version of `downside_risk_1d_nb`., Sortino ratio of a strategy., 2-dim version of `sortino_ratio_1d_nb`., sortino_ratio_1d_nb(), sortino_ratio_nb()

### Community 99 - "Community 99"
Cohesion: 0.25
Nodes (8): generate_enex(), generate_rand_enex_by_prob(), rand_chain_by_prob_apply(), rand_enex_by_prob_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_enex_by_prob_nb`., Engine-neutral `vectorbt.signals.nb.generate_enex_nb`., Apply function used by `vectorbt.signals.generators.RPROBNX`., Apply function used by `vectorbt.signals.generators.RPROBCX`.

### Community 100 - "Community 100"
Cohesion: 0.25
Nodes (8): generate_enex_nb(), generate_ohlc_stop_enex_nb(), generate_rand_enex_by_prob_nb(), generate_stop_enex_nb(), Generate one after another using `generate_enex_nb` and `ohlc_stop_choice_nb`., Pick entry signals using `entry_choice_func_nb` and exit signals using     `exit, Pick entries by probability `entry_prob` and exits by probability `exit_prob` on, Generate one after another using `generate_enex_nb` and `stop_choice_nb`.      R

### Community 101 - "Community 101"
Cohesion: 0.25
Nodes (8): assert_instance_of(), assert_subclass_of(), is_instance_of(), is_subclass_of(), Check whether the argument is a subclass of `types`.      `types` can be one or, Check whether the argument is an instance of `types`.      `types` can be one or, Raise exception if the argument is none of types `types`., Raise exception if the argument is not a subclass of classes `classes`.

### Community 103 - "Community 103"
Cohesion: 0.29
Nodes (6): pandas_ta(), Shortcut for `vectorbt.indicators.factory.IndicatorFactory.from_talib`., Shortcut for `vectorbt.indicators.factory.IndicatorFactory.from_pandas_ta`., Shortcut for `vectorbt.indicators.factory.IndicatorFactory.from_ta`., ta(), talib()

### Community 104 - "Community 104"
Cohesion: 0.29
Nodes (7): cum_returns_1d_nb(), cum_returns_nb(), drawdown_1d_nb(), drawdown_nb(), Drawdown of cumulative returns., 2-dim version of `drawdown_1d_nb`., 2-dim version of `cum_returns_1d_nb`.

### Community 105 - "Community 105"
Cohesion: 0.29
Nodes (6): deep_getattr(), default_getattr_func(), get_dict_attr(), Get attribute without invoking the attribute lookup machinery., Default `getattr_func`., Retrieve attribute consecutively.      The attribute chain `attr_chain` can be:

### Community 106 - "Community 106"
Cohesion: 0.29
Nodes (6): adjust_lightness(), adjust_opacity(), Map `value_range` to colormap with name `cmap_name` and get RGB of the `value` f, Adjust opacity of color., Lightens the given color by multiplying (1-luminosity) by the given amount., rgb_from_cmap()

### Community 107 - "Community 107"
Cohesion: 0.29
Nodes (6): hstack_image_arrays(), Stack NumPy images horizontally., Stack NumPy images vertically., Save animation to a file.      Args:         fname (str): File name.         ind, save_animation(), vstack_image_arrays()

### Community 108 - "Community 108"
Cohesion: 0.38
Nodes (6): apply_mapping(), Reverse a mapping.      Returns a dict., Convert mapping-like object to a mapping.      Enable `reverse` to apply `revers, Apply mapping on object using a mapping-like object.      Args:         obj (any, reverse_mapping(), to_mapping()

### Community 109 - "Community 109"
Cohesion: 0.33
Nodes (6): import_submodules(), is_from_module(), list_module_keys(), Return whether `obj` is from module `module`., List the names of all public functions and classes defined in the module `module, Import all submodules of a module, recursively, including subpackages.      If p

### Community 110 - "Community 110"
Cohesion: 0.33
Nodes (4): AlpacaData, `Data` for data coming from `alpaca-py`.      Sign up for Alpaca API keys under, Download the symbol.          Args:             symbol (str): Symbol., Update the symbol.          `**kwargs` will override keyword arguments passed to

### Community 112 - "Community 112"
Cohesion: 0.33
Nodes (6): dd_decline_duration_nb(), dd_recovery_duration_nb(), dd_recovery_duration_ratio_nb(), Return the duration of the peak-to-valley phase of each drawdown record., Return the duration of the valley-to-recovery phase of each drawdown record., Return the ratio of the recovery duration to the decline duration of each drawdo

### Community 113 - "Community 113"
Cohesion: 0.33
Nodes (6): flat_reduce_grouped_nb(), flat_reduce_grouped_to_array_nb(), flatten_forder_nb(), Flatten `a` in F order., Same as `reduce_grouped_nb` but passes flattened array., Same as `reduce_grouped_to_array_nb` but passes flattened 1D array.

### Community 114 - "Community 114"
Cohesion: 0.53
Nodes (5): build_columns(), combine_objs(), params_to_list(), prepare_params(), run_pipeline()

### Community 115 - "Community 115"
Cohesion: 0.33
Nodes (3): `Portfolio.get_drawdowns` with default arguments., Get drawdown records from `Portfolio.value`.          See `vectorbt.generic.draw, Plot one column/group of drawdowns.          Args:             column (str): Nam

### Community 116 - "Community 116"
Cohesion: 0.33
Nodes (6): get_return_nb(), Calculate return from input and output value., Calculate returns from value., 2-dim version of `returns_1d_nb`., returns_1d_nb(), returns_nb()

### Community 117 - "Community 117"
Cohesion: 0.33
Nodes (3): Pre-process an attribute before resolution.          Should return an attribute., Post-process an object after resolution.          Should return an object., Resolve an attribute using keyword arguments and built-in caching.          * If

### Community 118 - "Community 118"
Cohesion: 0.33
Nodes (6): assert_index_equal(), is_default_index(), is_index_equal(), Check whether indexes are equal.      Introduces naming tests on top of `pd.Inde, Check whether index is a basic range., Raise exception if the first argument and the second argument have different ind

### Community 119 - "Community 119"
Cohesion: 0.33
Nodes (3): Remove attributes of the removed keys given keys prior to the removal., Remove and return the pair by the key., Remove and return some pair.

### Community 120 - "Community 120"
Cohesion: 0.33
Nodes (3): Merge with another dict into one single dict.          See `merge_dicts`., Create a new instance by copying and (optionally) changing the config., Create a new instance by copying the config.          See `Configured.replace`.

### Community 121 - "Community 121"
Cohesion: 0.40
Nodes (4): attach_nb_methods(), attach_transform_methods(), Class decorator to add Numba methods.      `config` should contain target method, Class decorator to add transformation methods.      `config` should contain targ

### Community 122 - "Community 122"
Cohesion: 0.60
Nodes (3): Protocol, SupportsArray, SupportsTZInfo

### Community 123 - "Community 123"
Cohesion: 0.40
Nodes (4): attach_fields(), override_field_config(), Class decorator to override field configs of all base classes in MRO that subcla, Class decorator to attach field properties in a `vectorbt.records.base.Records`

### Community 124 - "Community 124"
Cohesion: 0.50
Nodes (4): approx_exp_max_sharpe(), deflated_sharpe_ratio(), Expected Maximum Sharpe Ratio., Deflated Sharpe Ratio (DSR).      See [Deflated Sharpe Ratio](https://gmarti.git

### Community 125 - "Community 125"
Cohesion: 0.40
Nodes (4): map_enum_fields(), map_enum_values(), Map fields to values.      See `vectorbt.utils.mapping.apply_mapping`., Map values to fields.      See `vectorbt.utils.mapping.apply_mapping`.

### Community 126 - "Community 126"
Cohesion: 0.50
Nodes (4): Retry `retries` times if unsuccessful., Translate text to GIF.      See https://engineering.giphy.com/contextually-aware, requests_retry_session(), text_to_giphy_url()

### Community 127 - "Community 127"
Cohesion: 0.50
Nodes (4): bfill_1d_nb(), bfill_nb(), Fill NaNs by propagating first valid observation backward.      Numba equivalent, 2-dim version of `bfill_1d_nb`.

### Community 128 - "Community 128"
Cohesion: 0.50
Nodes (4): crossed_above_1d_nb(), crossed_above_nb(), Get the crossover of the first array going above the second array., 2-dim version of `crossed_above_1d_nb`.

### Community 129 - "Community 129"
Cohesion: 0.50
Nodes (4): diff_1d_nb(), diff_nb(), Return the 1-th discrete difference.      Numba equivalent to `pd.Series(a).diff, 2-dim version of `diff_1d_nb`.

### Community 130 - "Community 130"
Cohesion: 0.50
Nodes (4): ewm_mean_1d_nb(), ewm_mean_nb(), Return exponential weighted average.      Numba equivalent to `pd.Series(a).ewm(, 2-dim version of `ewm_mean_1d_nb`.

### Community 131 - "Community 131"
Cohesion: 0.50
Nodes (4): ewm_std_1d_nb(), ewm_std_nb(), 2-dim version of `ewm_std_1d_nb`., Return exponential weighted standard deviation.      Numba equivalent to `pd.Ser

### Community 132 - "Community 132"
Cohesion: 0.50
Nodes (4): expanding_apply_nb(), Provide rolling window calculations.      `apply_func_nb` should accept index of, Expanding version of `rolling_apply_nb`., rolling_apply_nb()

### Community 133 - "Community 133"
Cohesion: 0.50
Nodes (4): expanding_matrix_apply_nb(), `rolling_apply_nb` with `apply_func_nb` being applied on all columns at once., Expanding version of `rolling_matrix_apply_nb`., rolling_matrix_apply_nb()

### Community 134 - "Community 134"
Cohesion: 0.50
Nodes (4): expanding_max_1d_nb(), expanding_max_nb(), Return expanding max.      Numba equivalent to `pd.Series(a).expanding(min_perio, 2-dim version of `expanding_max_1d_nb`.

### Community 135 - "Community 135"
Cohesion: 0.50
Nodes (4): expanding_min_1d_nb(), expanding_min_nb(), Return expanding min.      Numba equivalent to `pd.Series(a).expanding(min_perio, 2-dim version of `expanding_min_1d_nb`.

### Community 136 - "Community 136"
Cohesion: 0.50
Nodes (4): ffill_1d_nb(), ffill_nb(), Fill NaNs by propagating last valid observation forward.      Numba equivalent t, 2-dim version of `ffill_1d_nb`.

### Community 137 - "Community 137"
Cohesion: 0.50
Nodes (4): pct_change_1d_nb(), pct_change_nb(), Return the percentage change.      Numba equivalent to `pd.Series(a).pct_change(, 2-dim version of `pct_change_1d_nb`.

### Community 138 - "Community 138"
Cohesion: 0.50
Nodes (4): Return rolling min.      Numba equivalent to `pd.Series(a).rolling(window, min_p, 2-dim version of `rolling_min_1d_nb`., rolling_min_1d_nb(), rolling_min_nb()

### Community 139 - "Community 139"
Cohesion: 0.50
Nodes (4): Return rolling max.      Numba equivalent to `pd.Series(a).rolling(window, min_p, 2-dim version of `rolling_max_1d_nb`., rolling_max_1d_nb(), rolling_max_nb()

### Community 140 - "Community 140"
Cohesion: 0.50
Nodes (2): Build metrics documentation., Call this method on each subclass that overrides `metrics`.

### Community 141 - "Community 141"
Cohesion: 0.67
Nodes (3): _ATR, Average True Range (ATR).      The indicator provide an indication of the degree, Plot `ATR.tr` and `ATR.atr`.          Args:             column (str): Name of th

### Community 142 - "Community 142"
Cohesion: 0.67
Nodes (3): _BBANDS, Bollinger Bands (BBANDS).      A Bollinger Band® is a technical analysis tool de, Plot `BBANDS.middle`, `BBANDS.upper` and `BBANDS.lower` against         `BBANDS.

### Community 143 - "Community 143"
Cohesion: 0.67
Nodes (3): _MACD, Moving Average Convergence Divergence (MACD).      Is a trend-following momentum, Plot `MACD.macd`, `MACD.signal` and `MACD.hist`.          Args:             colu

### Community 144 - "Community 144"
Cohesion: 0.67
Nodes (3): _MA, Plot `MA.ma` against `MA.close`.          Args:             column (str): Name o, Moving Average (MA).      A moving average is a widely used indicator in technic

### Community 145 - "Community 145"
Cohesion: 0.67
Nodes (3): _MSTD, Moving Standard Deviation (MSTD).      Standard deviation is an indicator that m, Plot `MSTD.mstd`.          Args:             column (str): Name of the column to

### Community 146 - "Community 146"
Cohesion: 0.67
Nodes (3): _OBV, On-balance volume (OBV).      It relates price and volume in the stock market. O, Plot `OBV.obv`.          Args:             column (str): Name of the column to p

### Community 147 - "Community 147"
Cohesion: 0.50
Nodes (2): `Portfolio.get_positions` with default arguments., Get position records.          See `vectorbt.portfolio.trades.Positions`.

### Community 148 - "Community 148"
Cohesion: 0.50
Nodes (4): cash_flow_nb(), get_free_cash_diff_nb(), Get updated debt and free cash flow., Get (free) cash flow series per column.

### Community 149 - "Community 149"
Cohesion: 0.50
Nodes (2): Check whether column array is sorted., Get metadata of column indices.          Returns element indices and new column

### Community 150 - "Community 150"
Cohesion: 0.50
Nodes (4): annualized_volatility_1d_nb(), annualized_volatility_nb(), Annualized volatility of a strategy., 2-dim version of `annualized_volatility_1d_nb`.

### Community 151 - "Community 151"
Cohesion: 0.50
Nodes (4): cond_value_at_risk_1d_nb(), cond_value_at_risk_nb(), Conditional value at risk (CVaR) of a returns stream., 2-dim version of `cond_value_at_risk_1d_nb`.

### Community 152 - "Community 152"
Cohesion: 0.50
Nodes (4): down_capture_1d_nb(), down_capture_nb(), Capture ratio for periods when the benchmark return is negative., 2-dim version of `down_capture_1d_nb`.

### Community 153 - "Community 153"
Cohesion: 0.50
Nodes (4): information_ratio_1d_nb(), information_ratio_nb(), Information ratio of a strategy., 2-dim version of `information_ratio_1d_nb`.

### Community 154 - "Community 154"
Cohesion: 0.50
Nodes (4): omega_ratio_1d_nb(), omega_ratio_nb(), Omega ratio of a strategy.., 2-dim version of `omega_ratio_1d_nb`.

### Community 155 - "Community 155"
Cohesion: 0.50
Nodes (4): Sharpe ratio of a strategy., 2-dim version of `sharpe_ratio_1d_nb`., sharpe_ratio_1d_nb(), sharpe_ratio_nb()

### Community 156 - "Community 156"
Cohesion: 0.50
Nodes (4): Ratio between the right (95%) and left tail (5%)., 2-dim version of `tail_ratio_1d_nb`., tail_ratio_1d_nb(), tail_ratio_nb()

### Community 157 - "Community 157"
Cohesion: 0.50
Nodes (4): Value at risk (VaR) of a returns stream., 2-dim version of `value_at_risk_1d_nb`., value_at_risk_1d_nb(), value_at_risk_nb()

### Community 158 - "Community 158"
Cohesion: 0.50
Nodes (4): generate_ohlc_stop_enex(), ohlc_stop_enex_apply(), Apply function used by `vectorbt.signals.generators.OHLCSTCX`., Engine-neutral `vectorbt.signals.nb.generate_ohlc_stop_enex_nb`.

### Community 159 - "Community 159"
Cohesion: 0.50
Nodes (4): generate_ohlc_stop_ex(), ohlc_stop_ex_apply(), Engine-neutral `vectorbt.signals.nb.generate_ohlc_stop_ex_nb`., Apply function used by `vectorbt.signals.generators.OHLCSTX`.

### Community 160 - "Community 160"
Cohesion: 0.50
Nodes (4): generate_rand_by_prob(), rand_by_prob_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_by_prob_nb`., Apply function used by `vectorbt.signals.generators.RPROB`.

### Community 161 - "Community 161"
Cohesion: 0.50
Nodes (4): generate_rand_enex(), rand_enex_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_enex_nb`., Apply function used by `vectorbt.signals.generators.RANDNX`.

### Community 162 - "Community 162"
Cohesion: 0.50
Nodes (4): generate_rand_ex_by_prob(), rand_ex_by_prob_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_ex_by_prob_nb`., Apply function used by `vectorbt.signals.generators.RPROBX`.

### Community 163 - "Community 163"
Cohesion: 0.50
Nodes (4): generate_rand_ex(), rand_ex_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_ex_nb`., Apply function used by `vectorbt.signals.generators.RANDX`.

### Community 164 - "Community 164"
Cohesion: 0.50
Nodes (4): generate_rand(), rand_apply(), Engine-neutral `vectorbt.signals.nb.generate_rand_nb`., Apply function used by `vectorbt.signals.generators.RAND`.

### Community 165 - "Community 165"
Cohesion: 0.50
Nodes (4): generate_stop_enex(), Engine-neutral `vectorbt.signals.nb.generate_stop_enex_nb`., Apply function used by `vectorbt.signals.generators.STCX`., stop_enex_apply()

### Community 166 - "Community 166"
Cohesion: 0.50
Nodes (4): generate_stop_ex(), Engine-neutral `vectorbt.signals.nb.generate_stop_ex_nb`., Apply function used by `vectorbt.signals.generators.STX`., stop_ex_apply()

### Community 167 - "Community 167"
Cohesion: 0.50
Nodes (4): clean_enex_1d_nb(), clean_enex_nb(), Clean entry and exit arrays by picking the first signal out of each.      Entry, 2-dim version of `clean_enex_1d_nb`.

### Community 168 - "Community 168"
Cohesion: 0.50
Nodes (4): norm_avg_index_1d_nb(), norm_avg_index_nb(), Get mean index normalized to (-1, 1)., 2-dim version of `norm_avg_index_1d_nb`.

### Community 169 - "Community 169"
Cohesion: 0.50
Nodes (4): nth_index_1d_nb(), nth_index_nb(), Get the index of the n-th True value.      !!! note         `n` starts with 0 an, 2-dim version of `nth_index_1d_nb`.

### Community 170 - "Community 170"
Cohesion: 0.50
Nodes (4): assert_dict_sequence_valid(), assert_dict_valid(), Raise exception if dict the argument has keys that are not in `lvl_keys`.      `, Raise exception if a dict or any dict in a sequence of dicts has keys that are n

### Community 171 - "Community 171"
Cohesion: 0.50
Nodes (4): assert_iterable(), is_iterable(), Raise exception if the argument is not an iterable., Check whether the argument is iterable.

### Community 172 - "Community 172"
Cohesion: 0.50
Nodes (4): assert_sequence(), is_sequence(), Check whether the argument is a sequence., Raise exception if the argument is not a sequence.

### Community 173 - "Community 173"
Cohesion: 0.67
Nodes (2): DrawdownStatusT, RangeStatusT

### Community 174 - "Community 174"
Cohesion: 0.67
Nodes (2): attach_returns_acc_methods(), Class decorator to add returns accessor methods.      `config` should contain ta

### Community 178 - "Community 178"
Cohesion: 0.67
Nodes (2): FactoryModeT, StopTypeT

### Community 179 - "Community 179"
Cohesion: 1.00
Nodes (2): set_seed(), set_seed_nb()

### Community 180 - "Community 180"
Cohesion: 1.00
Nodes (1): Whether this call needs any soft conversion before Rust dispatch.

### Community 187 - "Community 187"
Cohesion: 1.00
Nodes (2): count_reduce(), Engine-neutral `vectorbt.generic.nb.count_reduce_nb`.

### Community 188 - "Community 188"
Cohesion: 1.00
Nodes (2): crossed_above_1d(), Engine-neutral `vectorbt.generic.nb.crossed_above_1d_nb`.

### Community 189 - "Community 189"
Cohesion: 1.00
Nodes (2): crossed_above(), Engine-neutral `vectorbt.generic.nb.crossed_above_nb`.

### Community 190 - "Community 190"
Cohesion: 1.00
Nodes (2): dd_decline_duration(), Engine-neutral `vectorbt.generic.nb.dd_decline_duration_nb`.

### Community 191 - "Community 191"
Cohesion: 1.00
Nodes (2): dd_drawdown(), Engine-neutral `vectorbt.generic.nb.dd_drawdown_nb`.

### Community 192 - "Community 192"
Cohesion: 1.00
Nodes (2): dd_recovery_duration_ratio(), Engine-neutral `vectorbt.generic.nb.dd_recovery_duration_ratio_nb`.

### Community 193 - "Community 193"
Cohesion: 1.00
Nodes (2): dd_recovery_duration(), Engine-neutral `vectorbt.generic.nb.dd_recovery_duration_nb`.

### Community 194 - "Community 194"
Cohesion: 1.00
Nodes (2): dd_recovery_return(), Engine-neutral `vectorbt.generic.nb.dd_recovery_return_nb`.

### Community 195 - "Community 195"
Cohesion: 1.00
Nodes (2): describe_reduce(), Engine-neutral `vectorbt.generic.nb.describe_reduce_nb`.

### Community 196 - "Community 196"
Cohesion: 1.00
Nodes (2): diff_1d(), Engine-neutral `vectorbt.generic.nb.diff_1d_nb`.

### Community 197 - "Community 197"
Cohesion: 1.00
Nodes (2): diff(), Engine-neutral `vectorbt.generic.nb.diff_nb`.

### Community 198 - "Community 198"
Cohesion: 1.00
Nodes (2): ewm_mean_1d(), Engine-neutral `vectorbt.generic.nb.ewm_mean_1d_nb`.

### Community 199 - "Community 199"
Cohesion: 1.00
Nodes (2): ewm_mean(), Engine-neutral `vectorbt.generic.nb.ewm_mean_nb`.

### Community 200 - "Community 200"
Cohesion: 1.00
Nodes (2): ewm_std_1d(), Engine-neutral `vectorbt.generic.nb.ewm_std_1d_nb`.

### Community 201 - "Community 201"
Cohesion: 1.00
Nodes (2): ewm_std(), Engine-neutral `vectorbt.generic.nb.ewm_std_nb`.

### Community 202 - "Community 202"
Cohesion: 1.00
Nodes (2): expanding_apply(), Engine-neutral `vectorbt.generic.nb.expanding_apply_nb`.

### Community 203 - "Community 203"
Cohesion: 1.00
Nodes (2): expanding_matrix_apply(), Engine-neutral `vectorbt.generic.nb.expanding_matrix_apply_nb`.

### Community 204 - "Community 204"
Cohesion: 1.00
Nodes (2): expanding_max_1d(), Engine-neutral `vectorbt.generic.nb.expanding_max_1d_nb`.

### Community 205 - "Community 205"
Cohesion: 1.00
Nodes (2): expanding_max(), Engine-neutral `vectorbt.generic.nb.expanding_max_nb`.

### Community 206 - "Community 206"
Cohesion: 1.00
Nodes (2): expanding_mean_1d(), Engine-neutral `vectorbt.generic.nb.expanding_mean_1d_nb`.

### Community 207 - "Community 207"
Cohesion: 1.00
Nodes (2): expanding_mean(), Engine-neutral `vectorbt.generic.nb.expanding_mean_nb`.

### Community 208 - "Community 208"
Cohesion: 1.00
Nodes (2): expanding_min_1d(), Engine-neutral `vectorbt.generic.nb.expanding_min_1d_nb`.

### Community 209 - "Community 209"
Cohesion: 1.00
Nodes (2): expanding_min(), Engine-neutral `vectorbt.generic.nb.expanding_min_nb`.

### Community 210 - "Community 210"
Cohesion: 1.00
Nodes (2): expanding_std_1d(), Engine-neutral `vectorbt.generic.nb.expanding_std_1d_nb`.

### Community 211 - "Community 211"
Cohesion: 1.00
Nodes (2): expanding_std(), Engine-neutral `vectorbt.generic.nb.expanding_std_nb`.

### Community 212 - "Community 212"
Cohesion: 1.00
Nodes (2): ffill_1d(), Engine-neutral `vectorbt.generic.nb.ffill_1d_nb`.

### Community 213 - "Community 213"
Cohesion: 1.00
Nodes (2): ffill(), Engine-neutral `vectorbt.generic.nb.ffill_nb`.

### Community 214 - "Community 214"
Cohesion: 1.00
Nodes (2): fillna_1d(), Engine-neutral `vectorbt.generic.nb.fillna_1d_nb`.

### Community 215 - "Community 215"
Cohesion: 1.00
Nodes (2): fillna(), Engine-neutral `vectorbt.generic.nb.fillna_nb`.

### Community 216 - "Community 216"
Cohesion: 1.00
Nodes (2): filter(), Engine-neutral `vectorbt.generic.nb.filter_nb`.

### Community 217 - "Community 217"
Cohesion: 1.00
Nodes (2): find_ranges(), Engine-neutral `vectorbt.generic.nb.find_ranges_nb`.

### Community 218 - "Community 218"
Cohesion: 1.00
Nodes (2): flat_reduce_grouped_to_array(), Engine-neutral `vectorbt.generic.nb.flat_reduce_grouped_to_array_nb`.

### Community 219 - "Community 219"
Cohesion: 1.00
Nodes (2): flat_reduce_grouped(), Engine-neutral `vectorbt.generic.nb.flat_reduce_grouped_nb`.

### Community 220 - "Community 220"
Cohesion: 1.00
Nodes (2): flatten_forder(), Engine-neutral `vectorbt.generic.nb.flatten_forder_nb`.

### Community 221 - "Community 221"
Cohesion: 1.00
Nodes (2): flatten_grouped(), Engine-neutral `vectorbt.generic.nb.flatten_grouped_nb`.

### Community 222 - "Community 222"
Cohesion: 1.00
Nodes (2): flatten_uniform_grouped(), Engine-neutral `vectorbt.generic.nb.flatten_uniform_grouped_nb`.

### Community 223 - "Community 223"
Cohesion: 1.00
Nodes (2): fshift_1d(), Engine-neutral `vectorbt.generic.nb.fshift_1d_nb`.

### Community 224 - "Community 224"
Cohesion: 1.00
Nodes (2): fshift(), Engine-neutral `vectorbt.generic.nb.fshift_nb`.

### Community 225 - "Community 225"
Cohesion: 1.00
Nodes (2): get_drawdowns(), Engine-neutral `vectorbt.generic.nb.get_drawdowns_nb`.

### Community 226 - "Community 226"
Cohesion: 1.00
Nodes (2): groupby_apply(), Engine-neutral `vectorbt.generic.nb.groupby_apply_nb`.

### Community 227 - "Community 227"
Cohesion: 1.00
Nodes (2): groupby_matrix_apply(), Engine-neutral `vectorbt.generic.nb.groupby_matrix_apply_nb`.

### Community 228 - "Community 228"
Cohesion: 1.00
Nodes (2): max_reduce(), Engine-neutral `vectorbt.generic.nb.max_reduce_nb`.

### Community 229 - "Community 229"
Cohesion: 1.00
Nodes (2): max_squeeze(), Engine-neutral `vectorbt.generic.nb.max_squeeze_nb`.

### Community 230 - "Community 230"
Cohesion: 1.00
Nodes (2): mean_reduce(), Engine-neutral `vectorbt.generic.nb.mean_reduce_nb`.

### Community 231 - "Community 231"
Cohesion: 1.00
Nodes (2): median_reduce(), Engine-neutral `vectorbt.generic.nb.median_reduce_nb`.

### Community 232 - "Community 232"
Cohesion: 1.00
Nodes (2): min_reduce(), Engine-neutral `vectorbt.generic.nb.min_reduce_nb`.

### Community 233 - "Community 233"
Cohesion: 1.00
Nodes (2): min_squeeze(), Engine-neutral `vectorbt.generic.nb.min_squeeze_nb`.

### Community 234 - "Community 234"
Cohesion: 1.00
Nodes (2): nancnt(), Engine-neutral `vectorbt.generic.nb.nancnt_nb`.

### Community 235 - "Community 235"
Cohesion: 1.00
Nodes (2): nancumprod(), Engine-neutral `vectorbt.generic.nb.nancumprod_nb`.

### Community 236 - "Community 236"
Cohesion: 1.00
Nodes (2): nancumsum(), Engine-neutral `vectorbt.generic.nb.nancumsum_nb`.

### Community 237 - "Community 237"
Cohesion: 1.00
Nodes (2): nanmax(), Engine-neutral `vectorbt.generic.nb.nanmax_nb`.

### Community 238 - "Community 238"
Cohesion: 1.00
Nodes (2): nanmean(), Engine-neutral `vectorbt.generic.nb.nanmean_nb`.

### Community 239 - "Community 239"
Cohesion: 1.00
Nodes (2): nanmedian(), Engine-neutral `vectorbt.generic.nb.nanmedian_nb`.

### Community 240 - "Community 240"
Cohesion: 1.00
Nodes (2): nanmin(), Engine-neutral `vectorbt.generic.nb.nanmin_nb`.

### Community 241 - "Community 241"
Cohesion: 1.00
Nodes (2): nanprod(), Engine-neutral `vectorbt.generic.nb.nanprod_nb`.

### Community 242 - "Community 242"
Cohesion: 1.00
Nodes (2): nanstd_1d(), Engine-neutral `vectorbt.generic.nb.nanstd_1d_nb`.

### Community 243 - "Community 243"
Cohesion: 1.00
Nodes (2): nanstd(), Engine-neutral `vectorbt.generic.nb.nanstd_nb`.

### Community 244 - "Community 244"
Cohesion: 1.00
Nodes (2): nansum(), Engine-neutral `vectorbt.generic.nb.nansum_nb`.

### Community 245 - "Community 245"
Cohesion: 1.00
Nodes (2): nth_index_reduce(), Engine-neutral `vectorbt.generic.nb.nth_index_reduce_nb`.

### Community 246 - "Community 246"
Cohesion: 1.00
Nodes (2): nth_reduce(), Engine-neutral `vectorbt.generic.nb.nth_reduce_nb`.

### Community 247 - "Community 247"
Cohesion: 1.00
Nodes (2): pct_change_1d(), Engine-neutral `vectorbt.generic.nb.pct_change_1d_nb`.

### Community 248 - "Community 248"
Cohesion: 1.00
Nodes (2): pct_change(), Engine-neutral `vectorbt.generic.nb.pct_change_nb`.

### Community 249 - "Community 249"
Cohesion: 1.00
Nodes (2): range_coverage(), Engine-neutral `vectorbt.generic.nb.range_coverage_nb`.

### Community 250 - "Community 250"
Cohesion: 1.00
Nodes (2): range_duration(), Engine-neutral `vectorbt.generic.nb.range_duration_nb`.

### Community 251 - "Community 251"
Cohesion: 1.00
Nodes (2): ranges_to_mask(), Engine-neutral `vectorbt.generic.nb.ranges_to_mask_nb`.

### Community 252 - "Community 252"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.row_apply_nb`., row_apply()

### Community 253 - "Community 253"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_apply_nb`., rolling_apply()

### Community 254 - "Community 254"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_matrix_apply_nb`., rolling_matrix_apply()

### Community 255 - "Community 255"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.set_by_mask_nb`., set_by_mask()

### Community 256 - "Community 256"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.reduce_nb`., reduce()

### Community 257 - "Community 257"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.reduce_to_array_nb`., reduce_to_array()

### Community 258 - "Community 258"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.reduce_grouped_nb`., reduce_grouped()

### Community 259 - "Community 259"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.reduce_grouped_to_array_nb`., reduce_grouped_to_array()

### Community 260 - "Community 260"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.squeeze_grouped_nb`., squeeze_grouped()

### Community 261 - "Community 261"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.set_by_mask_mult_1d_nb`., set_by_mask_mult_1d()

### Community 262 - "Community 262"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.std_reduce_nb`., std_reduce()

### Community 263 - "Community 263"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.sum_reduce_nb`., sum_reduce()

### Community 264 - "Community 264"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.set_by_mask_mult_nb`., set_by_mask_mult()

### Community 265 - "Community 265"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.sum_squeeze_nb`., sum_squeeze()

### Community 266 - "Community 266"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.shuffle_1d_nb`., shuffle_1d()

### Community 267 - "Community 267"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.shuffle_nb`., shuffle()

### Community 268 - "Community 268"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_min_1d_nb`., rolling_min_1d()

### Community 269 - "Community 269"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_min_nb`., rolling_min()

### Community 270 - "Community 270"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_max_1d_nb`., rolling_max_1d()

### Community 271 - "Community 271"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_max_nb`., rolling_max()

### Community 272 - "Community 272"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_mean_1d_nb`., rolling_mean_1d()

### Community 273 - "Community 273"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_mean_nb`., rolling_mean()

### Community 274 - "Community 274"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_std_1d_nb`., rolling_std_1d()

### Community 275 - "Community 275"
Cohesion: 1.00
Nodes (2): Engine-neutral `vectorbt.generic.nb.rolling_std_nb`., rolling_std()

### Community 276 - "Community 276"
Cohesion: 1.00
Nodes (2): _fshift_1d_nb(), Shift forward by `n` positions.      Numba equivalent to `pd.Series(arr).shift(n

### Community 277 - "Community 277"
Cohesion: 1.00
Nodes (2): _fshift_nb(), 2-dim version of `fshift_1d_nb`.

### Community 278 - "Community 278"
Cohesion: 1.00
Nodes (2): get_drawdowns_nb(), Fill drawdown records by analyzing a time series.      Usage:         ```pycon

### Community 279 - "Community 279"
Cohesion: 1.00
Nodes (2): groupby_apply_nb(), Provide group-by calculations.      `groups` should be a dictionary, where each

### Community 280 - "Community 280"
Cohesion: 1.00
Nodes (2): groupby_matrix_apply_nb(), `groupby_apply_nb` with `apply_func_nb` being applied on all columns at once.

### Community 281 - "Community 281"
Cohesion: 1.00
Nodes (2): max_reduce_nb(), Return max (ignores NaNs).

### Community 282 - "Community 282"
Cohesion: 1.00
Nodes (2): max_squeeze_nb(), Return max (ignores NaNs) of a group.

### Community 283 - "Community 283"
Cohesion: 1.00
Nodes (2): mean_reduce_nb(), Return mean (ignores NaNs).

### Community 284 - "Community 284"
Cohesion: 1.00
Nodes (2): median_reduce_nb(), Return median (ignores NaNs).

### Community 285 - "Community 285"
Cohesion: 1.00
Nodes (2): min_reduce_nb(), Return min (ignores NaNs).

### Community 286 - "Community 286"
Cohesion: 1.00
Nodes (2): min_squeeze_nb(), Return min (ignores NaNs) of a group.

### Community 287 - "Community 287"
Cohesion: 1.00
Nodes (2): nancnt_nb(), Compute count while ignoring NaNs.

### Community 288 - "Community 288"
Cohesion: 1.00
Nodes (2): _nancumprod_nb(), Numba equivalent of `np.nancumprod` along axis 0.

### Community 289 - "Community 289"
Cohesion: 1.00
Nodes (2): _nancumsum_nb(), Numba equivalent of `np.nancumsum` along axis 0.

### Community 290 - "Community 290"
Cohesion: 1.00
Nodes (2): nanmax_nb(), Numba-equivalent of `np.nanmax` along axis 0.

### Community 291 - "Community 291"
Cohesion: 1.00
Nodes (2): nanmean_nb(), Numba-equivalent of `np.nanmean` along axis 0.

### Community 292 - "Community 292"
Cohesion: 1.00
Nodes (2): nanmedian_nb(), Numba-equivalent of `np.nanmedian` along axis 0.

### Community 293 - "Community 293"
Cohesion: 1.00
Nodes (2): nanmin_nb(), Numba-equivalent of `np.nanmin` along axis 0.

### Community 294 - "Community 294"
Cohesion: 1.00
Nodes (2): _nanprod_nb(), Numba equivalent of `np.nanprod` along axis 0.

### Community 295 - "Community 295"
Cohesion: 1.00
Nodes (2): _nansum_nb(), Numba equivalent of `np.nansum` along axis 0.

### Community 296 - "Community 296"
Cohesion: 1.00
Nodes (2): nth_index_reduce_nb(), Return index of n-th element.

### Community 297 - "Community 297"
Cohesion: 1.00
Nodes (2): range_coverage_nb(), Get coverage of range records.      Set `overlapping` to True to get the number

### Community 298 - "Community 298"
Cohesion: 1.00
Nodes (2): range_duration_nb(), Get duration of each duration record.

### Community 299 - "Community 299"
Cohesion: 1.00
Nodes (2): ranges_to_mask_nb(), Convert ranges to 2-dim mask.

### Community 300 - "Community 300"
Cohesion: 1.00
Nodes (2): Apply function on each row.      `apply_func_nb` should accept index of the row,, row_apply_nb()

### Community 301 - "Community 301"
Cohesion: 1.00
Nodes (2): Set each element to a value by boolean mask., _set_by_mask_1d_nb()

### Community 302 - "Community 302"
Cohesion: 1.00
Nodes (2): Reduce each column into a single value using `reduce_func_nb`.      `reduce_func, reduce_nb()

### Community 303 - "Community 303"
Cohesion: 1.00
Nodes (2): Reduce each column into an array of values using `reduce_func_nb`.      `reduce_, reduce_to_array_nb()

### Community 304 - "Community 304"
Cohesion: 1.00
Nodes (2): Reduce each group of columns into a single value using `reduce_func_nb`.      `r, reduce_grouped_nb()

### Community 305 - "Community 305"
Cohesion: 1.00
Nodes (2): Reduce each group of columns into an array of values using `reduce_func_nb`., reduce_grouped_to_array_nb()

### Community 306 - "Community 306"
Cohesion: 1.00
Nodes (2): 2-dim version of `set_by_mask_1d_nb`., _set_by_mask_nb()

### Community 307 - "Community 307"
Cohesion: 1.00
Nodes (2): Squeeze each group of columns into a single column using `squeeze_func_nb`., squeeze_grouped_nb()

### Community 308 - "Community 308"
Cohesion: 1.00
Nodes (2): Return sum (ignores NaNs)., sum_reduce_nb()

### Community 309 - "Community 309"
Cohesion: 1.00
Nodes (2): Return value counts per column/group., value_counts_nb()

### Community 310 - "Community 310"
Cohesion: 1.00
Nodes (2): Return sum (ignores NaNs) of a group., sum_squeeze_nb()

### Community 311 - "Community 311"
Cohesion: 1.00
Nodes (2): Set each element in one array to the corresponding element in another by boolean, _set_by_mask_mult_1d_nb()

### Community 312 - "Community 312"
Cohesion: 1.00
Nodes (2): 2-dim version of `set_by_mask_mult_1d_nb`., _set_by_mask_mult_nb()

### Community 313 - "Community 313"
Cohesion: 1.00
Nodes (2): Shuffle each column in `a`.      Specify `seed` to make output deterministic., shuffle_1d_nb()

### Community 314 - "Community 314"
Cohesion: 1.00
Nodes (1): TrendModeT

### Community 316 - "Community 316"
Cohesion: 1.00
Nodes (2): Rolling version of `sortino_ratio_nb`., rolling_sortino_ratio_nb()

### Community 317 - "Community 317"
Cohesion: 1.00
Nodes (2): Rolling version of `information_ratio_nb`., rolling_information_ratio_nb()

### Community 318 - "Community 318"
Cohesion: 1.00
Nodes (2): Rolling version of `beta_nb`., rolling_beta_nb()

### Community 319 - "Community 319"
Cohesion: 1.00
Nodes (2): Rolling version of `alpha_nb`., rolling_alpha_nb()

### Community 320 - "Community 320"
Cohesion: 1.00
Nodes (2): Rolling version of `tail_ratio_nb`., rolling_tail_ratio_nb()

### Community 321 - "Community 321"
Cohesion: 1.00
Nodes (2): Rolling version of `value_at_risk_nb`., rolling_value_at_risk_nb()

### Community 322 - "Community 322"
Cohesion: 1.00
Nodes (2): Rolling version of `cond_value_at_risk_nb`., rolling_cond_value_at_risk_nb()

### Community 323 - "Community 323"
Cohesion: 1.00
Nodes (2): Rolling version of `capture_nb`., rolling_capture_nb()

### Community 324 - "Community 324"
Cohesion: 1.00
Nodes (2): Calculate total return from returns., total_return_apply_nb()

### Community 325 - "Community 325"
Cohesion: 1.00
Nodes (2): Rolling version of `up_capture_nb`., rolling_up_capture_nb()

### Community 326 - "Community 326"
Cohesion: 1.00
Nodes (2): clean_enex_1d(), Engine-neutral `vectorbt.signals.nb.clean_enex_1d_nb`.

### Community 327 - "Community 327"
Cohesion: 1.00
Nodes (2): clean_enex(), Engine-neutral `vectorbt.signals.nb.clean_enex_nb`.

### Community 328 - "Community 328"
Cohesion: 1.00
Nodes (2): generate_ex(), Engine-neutral `vectorbt.signals.nb.generate_ex_nb`.

### Community 329 - "Community 329"
Cohesion: 1.00
Nodes (2): generate(), Engine-neutral `vectorbt.signals.nb.generate_nb`.

### Community 330 - "Community 330"
Cohesion: 1.00
Nodes (2): norm_avg_index_1d(), Engine-neutral `vectorbt.signals.nb.norm_avg_index_1d_nb`.

### Community 331 - "Community 331"
Cohesion: 1.00
Nodes (2): norm_avg_index(), Engine-neutral `vectorbt.signals.nb.norm_avg_index_nb`.

### Community 332 - "Community 332"
Cohesion: 1.00
Nodes (2): nth_index_1d(), Engine-neutral `vectorbt.signals.nb.nth_index_1d_nb`.

### Community 333 - "Community 333"
Cohesion: 1.00
Nodes (2): nth_index(), Engine-neutral `vectorbt.signals.nb.nth_index_nb`.

### Community 334 - "Community 334"
Cohesion: 1.00
Nodes (2): partition_ranges(), Engine-neutral `vectorbt.signals.nb.partition_ranges_nb`.

### Community 335 - "Community 335"
Cohesion: 1.00
Nodes (2): part_pos_rank_nb(), `rank_func_nb` that returns the rank of each partition by its position in the se

### Community 336 - "Community 336"
Cohesion: 1.00
Nodes (2): partition_ranges_nb(), Create a record of type `vectorbt.generic.enums.range_dt` for each partition of

### Community 337 - "Community 337"
Cohesion: 1.00
Nodes (2): rand_by_prob_choice_nb(), `choice_func_nb` to randomly pick values from range `[from_i, to_i)` with probab

### Community 338 - "Community 338"
Cohesion: 1.00
Nodes (2): rand_choice_nb(), `choice_func_nb` to randomly pick `n` values from range `[from_i, to_i)`.      `

### Community 339 - "Community 339"
Cohesion: 1.00
Nodes (2): rank_nb(), Rank each signal using `rank_func_nb`.      Applies `rank_func_nb` on each True

## Knowledge Gaps
- **786 isolated node(s):** `Array conversion required before calling the Rust engine.`, `Rust support result for an engine-neutral function call.`, `Whether this call needs any soft conversion before Rust dispatch.`, `Return whether `vectorbt-rust` is installed and version-compatible.`, `Clear cached engine availability checks.` (+781 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 18`** (1 nodes): `ReturnsAccessor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (1 nodes): `Records`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (2 nodes): `BaseAccessor`, `GenericAccessor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (1 nodes): `Data`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 69`** (1 nodes): `IndicatorFactory`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 87`** (2 nodes): `ReturnsDFAccessor`, `ReturnsSRAccessor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 140`** (2 nodes): `Build metrics documentation.`, `Call this method on each subclass that overrides `metrics`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 147`** (2 nodes): ``Portfolio.get_positions` with default arguments.`, `Get position records.          See `vectorbt.portfolio.trades.Positions`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 149`** (2 nodes): `Check whether column array is sorted.`, `Get metadata of column indices.          Returns element indices and new column`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 173`** (2 nodes): `DrawdownStatusT`, `RangeStatusT`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 174`** (2 nodes): `attach_returns_acc_methods()`, `Class decorator to add returns accessor methods.      `config` should contain ta`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 178`** (2 nodes): `FactoryModeT`, `StopTypeT`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 179`** (2 nodes): `set_seed()`, `set_seed_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 180`** (1 nodes): `Whether this call needs any soft conversion before Rust dispatch.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 187`** (2 nodes): `count_reduce()`, `Engine-neutral `vectorbt.generic.nb.count_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 188`** (2 nodes): `crossed_above_1d()`, `Engine-neutral `vectorbt.generic.nb.crossed_above_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 189`** (2 nodes): `crossed_above()`, `Engine-neutral `vectorbt.generic.nb.crossed_above_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (2 nodes): `dd_decline_duration()`, `Engine-neutral `vectorbt.generic.nb.dd_decline_duration_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 191`** (2 nodes): `dd_drawdown()`, `Engine-neutral `vectorbt.generic.nb.dd_drawdown_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 192`** (2 nodes): `dd_recovery_duration_ratio()`, `Engine-neutral `vectorbt.generic.nb.dd_recovery_duration_ratio_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 193`** (2 nodes): `dd_recovery_duration()`, `Engine-neutral `vectorbt.generic.nb.dd_recovery_duration_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 194`** (2 nodes): `dd_recovery_return()`, `Engine-neutral `vectorbt.generic.nb.dd_recovery_return_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 195`** (2 nodes): `describe_reduce()`, `Engine-neutral `vectorbt.generic.nb.describe_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 196`** (2 nodes): `diff_1d()`, `Engine-neutral `vectorbt.generic.nb.diff_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 197`** (2 nodes): `diff()`, `Engine-neutral `vectorbt.generic.nb.diff_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 198`** (2 nodes): `ewm_mean_1d()`, `Engine-neutral `vectorbt.generic.nb.ewm_mean_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 199`** (2 nodes): `ewm_mean()`, `Engine-neutral `vectorbt.generic.nb.ewm_mean_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 200`** (2 nodes): `ewm_std_1d()`, `Engine-neutral `vectorbt.generic.nb.ewm_std_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 201`** (2 nodes): `ewm_std()`, `Engine-neutral `vectorbt.generic.nb.ewm_std_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 202`** (2 nodes): `expanding_apply()`, `Engine-neutral `vectorbt.generic.nb.expanding_apply_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 203`** (2 nodes): `expanding_matrix_apply()`, `Engine-neutral `vectorbt.generic.nb.expanding_matrix_apply_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 204`** (2 nodes): `expanding_max_1d()`, `Engine-neutral `vectorbt.generic.nb.expanding_max_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 205`** (2 nodes): `expanding_max()`, `Engine-neutral `vectorbt.generic.nb.expanding_max_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 206`** (2 nodes): `expanding_mean_1d()`, `Engine-neutral `vectorbt.generic.nb.expanding_mean_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 207`** (2 nodes): `expanding_mean()`, `Engine-neutral `vectorbt.generic.nb.expanding_mean_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 208`** (2 nodes): `expanding_min_1d()`, `Engine-neutral `vectorbt.generic.nb.expanding_min_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 209`** (2 nodes): `expanding_min()`, `Engine-neutral `vectorbt.generic.nb.expanding_min_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 210`** (2 nodes): `expanding_std_1d()`, `Engine-neutral `vectorbt.generic.nb.expanding_std_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 211`** (2 nodes): `expanding_std()`, `Engine-neutral `vectorbt.generic.nb.expanding_std_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 212`** (2 nodes): `ffill_1d()`, `Engine-neutral `vectorbt.generic.nb.ffill_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 213`** (2 nodes): `ffill()`, `Engine-neutral `vectorbt.generic.nb.ffill_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 214`** (2 nodes): `fillna_1d()`, `Engine-neutral `vectorbt.generic.nb.fillna_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 215`** (2 nodes): `fillna()`, `Engine-neutral `vectorbt.generic.nb.fillna_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 216`** (2 nodes): `filter()`, `Engine-neutral `vectorbt.generic.nb.filter_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 217`** (2 nodes): `find_ranges()`, `Engine-neutral `vectorbt.generic.nb.find_ranges_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 218`** (2 nodes): `flat_reduce_grouped_to_array()`, `Engine-neutral `vectorbt.generic.nb.flat_reduce_grouped_to_array_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 219`** (2 nodes): `flat_reduce_grouped()`, `Engine-neutral `vectorbt.generic.nb.flat_reduce_grouped_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 220`** (2 nodes): `flatten_forder()`, `Engine-neutral `vectorbt.generic.nb.flatten_forder_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 221`** (2 nodes): `flatten_grouped()`, `Engine-neutral `vectorbt.generic.nb.flatten_grouped_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 222`** (2 nodes): `flatten_uniform_grouped()`, `Engine-neutral `vectorbt.generic.nb.flatten_uniform_grouped_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 223`** (2 nodes): `fshift_1d()`, `Engine-neutral `vectorbt.generic.nb.fshift_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 224`** (2 nodes): `fshift()`, `Engine-neutral `vectorbt.generic.nb.fshift_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 225`** (2 nodes): `get_drawdowns()`, `Engine-neutral `vectorbt.generic.nb.get_drawdowns_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 226`** (2 nodes): `groupby_apply()`, `Engine-neutral `vectorbt.generic.nb.groupby_apply_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 227`** (2 nodes): `groupby_matrix_apply()`, `Engine-neutral `vectorbt.generic.nb.groupby_matrix_apply_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 228`** (2 nodes): `max_reduce()`, `Engine-neutral `vectorbt.generic.nb.max_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 229`** (2 nodes): `max_squeeze()`, `Engine-neutral `vectorbt.generic.nb.max_squeeze_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 230`** (2 nodes): `mean_reduce()`, `Engine-neutral `vectorbt.generic.nb.mean_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 231`** (2 nodes): `median_reduce()`, `Engine-neutral `vectorbt.generic.nb.median_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 232`** (2 nodes): `min_reduce()`, `Engine-neutral `vectorbt.generic.nb.min_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 233`** (2 nodes): `min_squeeze()`, `Engine-neutral `vectorbt.generic.nb.min_squeeze_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 234`** (2 nodes): `nancnt()`, `Engine-neutral `vectorbt.generic.nb.nancnt_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 235`** (2 nodes): `nancumprod()`, `Engine-neutral `vectorbt.generic.nb.nancumprod_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 236`** (2 nodes): `nancumsum()`, `Engine-neutral `vectorbt.generic.nb.nancumsum_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 237`** (2 nodes): `nanmax()`, `Engine-neutral `vectorbt.generic.nb.nanmax_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 238`** (2 nodes): `nanmean()`, `Engine-neutral `vectorbt.generic.nb.nanmean_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 239`** (2 nodes): `nanmedian()`, `Engine-neutral `vectorbt.generic.nb.nanmedian_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 240`** (2 nodes): `nanmin()`, `Engine-neutral `vectorbt.generic.nb.nanmin_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 241`** (2 nodes): `nanprod()`, `Engine-neutral `vectorbt.generic.nb.nanprod_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 242`** (2 nodes): `nanstd_1d()`, `Engine-neutral `vectorbt.generic.nb.nanstd_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 243`** (2 nodes): `nanstd()`, `Engine-neutral `vectorbt.generic.nb.nanstd_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 244`** (2 nodes): `nansum()`, `Engine-neutral `vectorbt.generic.nb.nansum_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 245`** (2 nodes): `nth_index_reduce()`, `Engine-neutral `vectorbt.generic.nb.nth_index_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 246`** (2 nodes): `nth_reduce()`, `Engine-neutral `vectorbt.generic.nb.nth_reduce_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 247`** (2 nodes): `pct_change_1d()`, `Engine-neutral `vectorbt.generic.nb.pct_change_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 248`** (2 nodes): `pct_change()`, `Engine-neutral `vectorbt.generic.nb.pct_change_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 249`** (2 nodes): `range_coverage()`, `Engine-neutral `vectorbt.generic.nb.range_coverage_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 250`** (2 nodes): `range_duration()`, `Engine-neutral `vectorbt.generic.nb.range_duration_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 251`** (2 nodes): `ranges_to_mask()`, `Engine-neutral `vectorbt.generic.nb.ranges_to_mask_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 252`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.row_apply_nb`.`, `row_apply()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 253`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_apply_nb`.`, `rolling_apply()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 254`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_matrix_apply_nb`.`, `rolling_matrix_apply()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 255`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.set_by_mask_nb`.`, `set_by_mask()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 256`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.reduce_nb`.`, `reduce()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 257`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.reduce_to_array_nb`.`, `reduce_to_array()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 258`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.reduce_grouped_nb`.`, `reduce_grouped()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 259`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.reduce_grouped_to_array_nb`.`, `reduce_grouped_to_array()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 260`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.squeeze_grouped_nb`.`, `squeeze_grouped()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 261`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.set_by_mask_mult_1d_nb`.`, `set_by_mask_mult_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 262`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.std_reduce_nb`.`, `std_reduce()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 263`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.sum_reduce_nb`.`, `sum_reduce()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 264`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.set_by_mask_mult_nb`.`, `set_by_mask_mult()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 265`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.sum_squeeze_nb`.`, `sum_squeeze()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 266`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.shuffle_1d_nb`.`, `shuffle_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 267`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.shuffle_nb`.`, `shuffle()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 268`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_min_1d_nb`.`, `rolling_min_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 269`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_min_nb`.`, `rolling_min()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 270`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_max_1d_nb`.`, `rolling_max_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 271`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_max_nb`.`, `rolling_max()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 272`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_mean_1d_nb`.`, `rolling_mean_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 273`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_mean_nb`.`, `rolling_mean()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 274`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_std_1d_nb`.`, `rolling_std_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 275`** (2 nodes): `Engine-neutral `vectorbt.generic.nb.rolling_std_nb`.`, `rolling_std()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 276`** (2 nodes): `_fshift_1d_nb()`, `Shift forward by `n` positions.      Numba equivalent to `pd.Series(arr).shift(n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 277`** (2 nodes): `_fshift_nb()`, `2-dim version of `fshift_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 278`** (2 nodes): `get_drawdowns_nb()`, `Fill drawdown records by analyzing a time series.      Usage:         ```pycon`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 279`** (2 nodes): `groupby_apply_nb()`, `Provide group-by calculations.      `groups` should be a dictionary, where each`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 280`** (2 nodes): `groupby_matrix_apply_nb()`, ``groupby_apply_nb` with `apply_func_nb` being applied on all columns at once.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 281`** (2 nodes): `max_reduce_nb()`, `Return max (ignores NaNs).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 282`** (2 nodes): `max_squeeze_nb()`, `Return max (ignores NaNs) of a group.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 283`** (2 nodes): `mean_reduce_nb()`, `Return mean (ignores NaNs).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 284`** (2 nodes): `median_reduce_nb()`, `Return median (ignores NaNs).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 285`** (2 nodes): `min_reduce_nb()`, `Return min (ignores NaNs).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 286`** (2 nodes): `min_squeeze_nb()`, `Return min (ignores NaNs) of a group.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 287`** (2 nodes): `nancnt_nb()`, `Compute count while ignoring NaNs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 288`** (2 nodes): `_nancumprod_nb()`, `Numba equivalent of `np.nancumprod` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 289`** (2 nodes): `_nancumsum_nb()`, `Numba equivalent of `np.nancumsum` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 290`** (2 nodes): `nanmax_nb()`, `Numba-equivalent of `np.nanmax` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 291`** (2 nodes): `nanmean_nb()`, `Numba-equivalent of `np.nanmean` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 292`** (2 nodes): `nanmedian_nb()`, `Numba-equivalent of `np.nanmedian` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 293`** (2 nodes): `nanmin_nb()`, `Numba-equivalent of `np.nanmin` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 294`** (2 nodes): `_nanprod_nb()`, `Numba equivalent of `np.nanprod` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 295`** (2 nodes): `_nansum_nb()`, `Numba equivalent of `np.nansum` along axis 0.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 296`** (2 nodes): `nth_index_reduce_nb()`, `Return index of n-th element.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 297`** (2 nodes): `range_coverage_nb()`, `Get coverage of range records.      Set `overlapping` to True to get the number`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 298`** (2 nodes): `range_duration_nb()`, `Get duration of each duration record.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 299`** (2 nodes): `ranges_to_mask_nb()`, `Convert ranges to 2-dim mask.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 300`** (2 nodes): `Apply function on each row.      `apply_func_nb` should accept index of the row,`, `row_apply_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 301`** (2 nodes): `Set each element to a value by boolean mask.`, `_set_by_mask_1d_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 302`** (2 nodes): `Reduce each column into a single value using `reduce_func_nb`.      `reduce_func`, `reduce_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 303`** (2 nodes): `Reduce each column into an array of values using `reduce_func_nb`.      `reduce_`, `reduce_to_array_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 304`** (2 nodes): `Reduce each group of columns into a single value using `reduce_func_nb`.      `r`, `reduce_grouped_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 305`** (2 nodes): `Reduce each group of columns into an array of values using `reduce_func_nb`.`, `reduce_grouped_to_array_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 306`** (2 nodes): `2-dim version of `set_by_mask_1d_nb`.`, `_set_by_mask_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 307`** (2 nodes): `Squeeze each group of columns into a single column using `squeeze_func_nb`.`, `squeeze_grouped_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 308`** (2 nodes): `Return sum (ignores NaNs).`, `sum_reduce_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 309`** (2 nodes): `Return value counts per column/group.`, `value_counts_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 310`** (2 nodes): `Return sum (ignores NaNs) of a group.`, `sum_squeeze_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 311`** (2 nodes): `Set each element in one array to the corresponding element in another by boolean`, `_set_by_mask_mult_1d_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 312`** (2 nodes): `2-dim version of `set_by_mask_mult_1d_nb`.`, `_set_by_mask_mult_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 313`** (2 nodes): `Shuffle each column in `a`.      Specify `seed` to make output deterministic.`, `shuffle_1d_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 314`** (1 nodes): `TrendModeT`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 316`** (2 nodes): `Rolling version of `sortino_ratio_nb`.`, `rolling_sortino_ratio_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 317`** (2 nodes): `Rolling version of `information_ratio_nb`.`, `rolling_information_ratio_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 318`** (2 nodes): `Rolling version of `beta_nb`.`, `rolling_beta_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 319`** (2 nodes): `Rolling version of `alpha_nb`.`, `rolling_alpha_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 320`** (2 nodes): `Rolling version of `tail_ratio_nb`.`, `rolling_tail_ratio_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 321`** (2 nodes): `Rolling version of `value_at_risk_nb`.`, `rolling_value_at_risk_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 322`** (2 nodes): `Rolling version of `cond_value_at_risk_nb`.`, `rolling_cond_value_at_risk_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 323`** (2 nodes): `Rolling version of `capture_nb`.`, `rolling_capture_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 324`** (2 nodes): `Calculate total return from returns.`, `total_return_apply_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 325`** (2 nodes): `Rolling version of `up_capture_nb`.`, `rolling_up_capture_nb()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 326`** (2 nodes): `clean_enex_1d()`, `Engine-neutral `vectorbt.signals.nb.clean_enex_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 327`** (2 nodes): `clean_enex()`, `Engine-neutral `vectorbt.signals.nb.clean_enex_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 328`** (2 nodes): `generate_ex()`, `Engine-neutral `vectorbt.signals.nb.generate_ex_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 329`** (2 nodes): `generate()`, `Engine-neutral `vectorbt.signals.nb.generate_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 330`** (2 nodes): `norm_avg_index_1d()`, `Engine-neutral `vectorbt.signals.nb.norm_avg_index_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 331`** (2 nodes): `norm_avg_index()`, `Engine-neutral `vectorbt.signals.nb.norm_avg_index_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 332`** (2 nodes): `nth_index_1d()`, `Engine-neutral `vectorbt.signals.nb.nth_index_1d_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 333`** (2 nodes): `nth_index()`, `Engine-neutral `vectorbt.signals.nb.nth_index_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 334`** (2 nodes): `partition_ranges()`, `Engine-neutral `vectorbt.signals.nb.partition_ranges_nb`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 335`** (2 nodes): `part_pos_rank_nb()`, ``rank_func_nb` that returns the rank of each partition by its position in the se`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 336`** (2 nodes): `partition_ranges_nb()`, `Create a record of type `vectorbt.generic.enums.range_dt` for each partition of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 337`** (2 nodes): `rand_by_prob_choice_nb()`, ``choice_func_nb` to randomly pick values from range `[from_i, to_i)` with probab`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 338`** (2 nodes): `rand_choice_nb()`, ``choice_func_nb` to randomly pick `n` values from range `[from_i, to_i)`.      ``
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 339`** (2 nodes): `rank_nb()`, `Rank each signal using `rank_func_nb`.      Applies `rank_func_nb` on each True`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Config` connect `Community 1` to `Community 38`, `Community 13`, `Community 33`, `Community 3`, `Community 121`, `Community 2`, `Community 0`, `Community 140`, `Community 48`, `Community 69`, `Community 32`, `Community 17`, `Community 30`, `Community 57`, `Community 60`, `Community 64`, `Community 50`, `Community 49`, `Community 77`, `Community 147`, `Community 115`, `Community 56`, `Community 36`, `Community 63`, `Community 174`, `Community 21`, `Community 123`, `Community 18`, `Community 87`, `Community 9`, `Community 14`, `Community 43`, `Community 46`, `Community 90`, `Community 10`, `Community 44`, `Community 59`, `Community 119`, `Community 75`, `Community 120`, `Community 16`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Why does `ArrayWrapper` connect `Community 1` to `Community 3`, `Community 2`, `Community 7`, `Community 6`, `Community 12`, `Community 10`, `Community 38`, `Community 13`, `Community 33`, `Community 48`, `Community 69`, `Community 17`, `Community 30`, `Community 57`, `Community 60`, `Community 64`, `Community 50`, `Community 49`, `Community 77`, `Community 147`, `Community 115`, `Community 56`, `Community 36`, `Community 63`, `Community 0`, `Community 21`, `Community 149`, `Community 78`, `Community 18`, `Community 87`, `Community 14`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Why does `Configured` connect `Community 10` to `Community 1`, `Community 6`, `Community 2`, `Community 7`, `Community 34`, `Community 12`, `Community 54`, `Community 15`, `Community 0`, `Community 21`, `Community 57`, `Community 41`, `Community 46`, `Community 120`, `Community 75`, `Community 59`, `Community 44`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 544 inferred relationships involving `Config` (e.g. with `Data` and `MetaData`) actually correct?**
  _`Config` has 544 INFERRED edges - model-reasoned connections that need verification._
- **Are the 502 inferred relationships involving `ArrayWrapper` (e.g. with `BaseAccessor` and `BaseDFAccessor`) actually correct?**
  _`ArrayWrapper` has 502 INFERRED edges - model-reasoned connections that need verification._
- **Are the 414 inferred relationships involving `Wrapping` (e.g. with `BaseAccessor` and `BaseDFAccessor`) actually correct?**
  _`Wrapping` has 414 INFERRED edges - model-reasoned connections that need verification._
- **Are the 283 inferred relationships involving `PlotsBuilderMixin` (e.g. with `Data` and `MetaData`) actually correct?**
  _`PlotsBuilderMixin` has 283 INFERRED edges - model-reasoned connections that need verification._