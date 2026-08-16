# Graph Report - knowledge_graphs/mplfinance/repo/src/mplfinance  (2026-08-13)

## Corpus Check
- Corpus is ~24,964 words - fits in a single context window. You may not need a graph.

## Summary
- 244 nodes · 317 edges · 31 communities detected
- Non-singleton communities: 12
- Extraction: EXTRACTED: 94.0% · INFERRED: 6.0%
- Edge kinds: calls: 85 · contains: 119 · inherits: 1 · method: 6 · rationale_for: 87 · uses: 19

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 31 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `493811d`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `_utils.py` (31)
- `plotting.py` (30)
- `IntegerIndexDateTimeFormatter` (24)
- `_arg_validators.py` (22)
- `original_flavor.py` (16)
- `plot()` (11)
- `_styles.py` (10)
- `_helpers.py` (9)
- `_check_for_and_apply_style()` (6)
- `_construct_hollow_candlestick_collections()` (6)

## Surprising Connections (you probably didn't know these)
- `ema: exponential moving average` --uses--> `IntegerIndexDateTimeFormatter`  [INFERRED]
  plotting.py → _utils.py
- `Take data (pd.Series, pd.DataFrame, np.ndarray of floats, list of floats), and` --uses--> `IntegerIndexDateTimeFormatter`  [INFERRED]
  plotting.py → _utils.py
- `Given a Pandas DataFrame containing columns Open,High,Low,Close and optionally V` --uses--> `IntegerIndexDateTimeFormatter`  [INFERRED]
  plotting.py → _utils.py
- `This decoractor creates an rcParams context around a function, so that any chang` --uses--> `IntegerIndexDateTimeFormatter`  [INFERRED]
  plotting.py → _utils.py
- `# NOTE: If in external_axes_mode, then all code relating` --uses--> `IntegerIndexDateTimeFormatter`  [INFERRED]
  plotting.py → _utils.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (52): _calculate_atr(), _check_and_convert_xlim_configuration(), _check_input(), coalesce_volume_dates(), combine_adjacent(), _construct_aline_collections(), _construct_candlestick_collections(), _construct_hline_collections() (+44 more)

### Community 1 - "Community 1"
Cohesion: 0.09
Nodes (39): Formatter, _addplot_apply_supplements(), _addplot_collections(), _addplot_columns(), _adjust_figsize(), _adjust_fontsize(), _auto_secondary_y(), make_addplot() (+31 more)

### Community 2 - "Community 2"
Cohesion: 0.07
Nodes (28): _alines_validator(), _bypass_kwarg_validation(), _check_and_prepare_data(), _check_for_external_axes(), _fill_between_validator(), _is_datelike(), _is_marketcolor_object(), _kwarg_not_implemented() (+20 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (31): _candlestick(), candlestick2_ochl(), candlestick2_ohlc(), candlestick_ochl(), candlestick_ohlc(), _check_input(), index_bar(), _plot_day_summary() (+23 more)

### Community 4 - "Community 4"
Cohesion: 0.15
Nodes (12): _determine_format_string(), _is_uint8_rgb_or_rgba(), _list_of_dict(), _mpf_is_color_like(), _mpf_to_rgba(), Some helper functions for mplfinance. NOTE: This is the lowest level in mplfinan, Determine if an object is a color.          Identical to `matplotlib.colors.is_c, Determine the datetime format string based on the averge number     of days betw (+4 more)

### Community 5 - "Community 5"
Cohesion: 0.21
Nodes (11): available_styles(), _get_mpfstyle(), make_marketcolors(), make_mpf_style(), Return a copy of the specified pre-defined mpfstyle.  We return     a copy, beca, value must be a color, "inherit"-like, or dict of colors, Create a 'marketcolors' dict that is structured as expected     by mplfinance._s, _valid_make_marketcolors_kwargs() (+3 more)

### Community 6 - "Community 6"
Cohesion: 0.29
Nodes (9): _determine_width_config(), _dfinterpolate(), _get_widths_df(), Given x-axis xdates, and `mpf.plot()` kwargs config,     determine the widths an, Given a DataFrame, with all values and the Index as floats,     and given a floa, Provide a dataframe of width data that appropriate scales widths of     various, _scale_width_config(), _valid_scale_width_kwargs() (+1 more)

### Community 7 - "Community 7"
Cohesion: 0.46
Nodes (3): _check_for_and_apply_style(), figure(), Mpf_Figure

### Community 8 - "Community 8"
Cohesion: 0.70
Nodes (4): compare_styles(), main(), Main entry point of the app, rcParams_to_df()

### Community 9 - "Community 9"
Cohesion: 0.40
Nodes (3): _build_panels(), # TODO:  Throughout this section, right_pad is intentionally *less*, Create and return a DataFrame containing panel information     and Axes objects

### Community 10 - "Community 10"
Cohesion: 0.83
Nodes (3): df_wrapcols(), kwarg_help(), make_left_formatter()

### Community 11 - "Community 11"
Cohesion: 0.67
Nodes (1): __init__ for mplfinance._styledata module

## Knowledge Gaps
- **68 isolated node(s):** `Check and Prepare the data input:     For now, data must be a Pandas DataFrame w`, `Validates the input of [legend] label for added plots.     label_value may be a`, `Value for mav (moving average) keyword may be:     scalar int greater than 1, or`, `Validate `vlines` kwarg value:  must be "datelike" or sequence of "datelike"`, `Value for segments to be passed into LineCollection constructor must be:     - a` (+63 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 11`** (1 nodes): `__init__ for mplfinance._styledata module`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `IntegerIndexDateTimeFormatter` connect `Community 1` to `Community 0`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `IntegerIndexDateTimeFormatter` (e.g. with `ema: exponential moving average` and `Take data (pd.Series, pd.DataFrame, np.ndarray of floats, list of floats), and`) actually correct?**
  _`IntegerIndexDateTimeFormatter` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Check and Prepare the data input:     For now, data must be a Pandas DataFrame w`, `Validates the input of [legend] label for added plots.     label_value may be a`, `Value for mav (moving average) keyword may be:     scalar int greater than 1, or` to the rest of the system?**
  _68 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.06095791001451379 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.08710801393728224 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.0677361853832442 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.08064516129032258 - nodes in this community are weakly interconnected._