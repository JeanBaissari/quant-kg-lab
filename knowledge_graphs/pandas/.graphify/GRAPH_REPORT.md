# Graph Report - pandas  (2026-08-06)

## Corpus Check
- Large corpus: 324 files · ~946,406 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 11368 nodes · 39913 edges · 396 communities detected
- Non-singleton communities: 360
- Extraction: EXTRACTED: 41.6% · INFERRED: 58.4%
- Edge kinds: calls: 5064 · contains: 1928 · imports: 5 · imports_from: 235 · inherits: 372 · method: 4951 · rationale_for: 4033 · uses: 23325

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 324 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 2 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `9828540`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `DatetimeTZDtype` (1582)
- `CategoricalDtype` (1480)
- `PeriodDtype` (1087)
- `StringDtype` (1031)
- `ArrowDtype` (1018)
- `DataFrame` (887)
- `WriteBuffer` (777)
- `IntervalDtype` (745)
- `Series` (659)
- `MultiIndex` (530)

## Surprising Connections (you probably didn't know these)
- `Warning raised for any upcoming change.      This is the base class for all pand` --uses--> `OptionError`  [INFERRED]
  errors/__init__.py → _config/config.py
- `Version where change will be enforced.` --uses--> `OptionError`  [INFERRED]
  errors/__init__.py → _config/config.py
- `Warning raised for an upcoming change that is a PendingDeprecationWarning.` --uses--> `OptionError`  [INFERRED]
  errors/__init__.py → _config/config.py
- `Warning raised for an upcoming change that is a DeprecationWarning.      This wa` --uses--> `OptionError`  [INFERRED]
  errors/__init__.py → _config/config.py
- `Warning raised for an upcoming change that is a FutureWarning.      This warning` --uses--> `OptionError`  [INFERRED]
  errors/__init__.py → _config/config.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.01
Nodes (192): BaseStringArray, JointConditionBinOp, PyTablesExpr, Hold a pytables-like expression, comprised of possibly multiple 'terms'.      Pa, AppendableFrameTable, AppendableMultiFrameTable, AppendableMultiSeriesTable, AppendableSeriesTable (+184 more)

### Community 1 - "Community 1"
Cohesion: 0.01
Nodes (287): Concatenate multiple arrays of this dtype.          Parameters         ---------, Return a Series containing counts of unique values.          Parameters, # TODO: disable for Categorical if not ordered?, # TODO: technically __init__ isn't defined here., Analogous to np.empty(shape, dtype=dtype)          Parameters         ----------, Decorator to ravel a 2D array before passing it to a cython operation,     then, ExtensionArray that is backed by a single NumPy ndarray., ravel_compat() (+279 more)

### Community 2 - "Community 2"
Cohesion: 0.02
Nodes (180): CategoricalAccessor, SeriesApply, Data structure for 1-dimensional cross-sectional and time series data, Return cumulative maximum over a Series.          Returns a Series of the same s, Return cumulative sum over a Series.          Returns a Series of the same size, Return cumulative product over a Series.          Returns a Series of the same s, Return a list of the row axis labels., Return the i-th value or values in the Series by location.          Parameters (+172 more)

### Community 3 - "Community 3"
Cohesion: 0.03
Nodes (200): FloatingDtype, NumpyExtensionArray, Extension array for string data.      .. warning::         StringArray is consid, StringArray, Accessor, Custom property-like object.      A descriptor for accessors.      Parameters, Dtype for data stored in :class:`SparseArray`.      ``SparseDtype`` is used as t, SparseDtype (+192 more)

### Community 4 - "Community 4"
Cohesion: 0.02
Nodes (124): Specialized Cython take which sets NaN values in one pass., Part of _get_take_nd_function below that doesn't need `mask_info` and thus     c, Get the appropriate "take" implementation for the given dimension, axis     and, Specialized Cython take which sets NaN values in one pass      This dispatches t, ExtensionArray, Abstract base class for custom 1-D array types.      pandas will recognize insta, Formatting function for scalar values.          This is used in the default '__r, Return a transposed view on this array.          Because ExtensionArrays are alw (+116 more)

### Community 5 - "Community 5"
Cohesion: 0.07
Nodes (246): Parameters         ----------         result : array-like or tuple[array-like], Base class for masked arrays (which use _data and _mask to store the data)., Return boolean ndarray denoting duplicate values.          Parameters         --, Compute the BaseMaskedArray of unique values.          Returns         -------, Find indices where elements should be inserted to maintain order.          Find, Encode the extension array as an enumerated type.          Parameters         --, Return values for sorting.          Returns         -------         ndarray, Returns a Series containing counts of each unique value.          Parameters (+238 more)

### Community 6 - "Community 6"
Cohesion: 0.01
Nodes (244): add_doctest_imports(), all_arithmetic_functions(), all_arithmetic_operators(), all_binary_operators(), all_boolean_reductions(), all_logical_operators(), all_numeric_accumulations(), all_numeric_reductions() (+236 more)

### Community 7 - "Community 7"
Cohesion: 0.02
Nodes (163): DatelikeOps, dtype_to_unit(), _period_dispatch(), Get the int64 values and b_mask to pass to add_overflowsafe., Add a delta of a timedeltalike          Returns         -------         Same typ, Add a delta of a TimedeltaIndex          Returns         -------         Same ty, Subtract pd.NaT from self, Add or subtract array-like of DateOffset objects          Parameters         --- (+155 more)

### Community 8 - "Community 8"
Cohesion: 0.02
Nodes (146): BytesIO, _BaseXMLFormatter, :mod:`pandas.io.formats.xml` is a module for formatting data in XML., Build tree from  data.          This method initializes the root and builds attr, Validate elems_cols and attrs_cols.          This method will check if columns i, Validate encoding.          This method will check if encoding is among listed u, Adjust Data Frame to fit xml output.          This method will adjust underlying, Handle indexes.          This method will add indexes into attr_cols or elem_col (+138 more)

### Community 9 - "Community 9"
Cohesion: 0.02
Nodes (158): Return the index of minimum value.          In case of multiple occurrences of t, Return the index of maximum value.          In case of multiple occurrences of t, Fill NaN values using an interpolation method.          This method fills missin, Pointwise comparison for set containment in the given values.          Roughly e, Return an ExtensionArray performing an accumulation operation.          The unde, Specify how to render our entries in to_json.          Notes         -----, Return a list of the values.          These are each a scalar type, which is a P, Analogue to np.putmask(self, mask, value)          Parameters         ---------- (+150 more)

### Community 10 - "Community 10"
Cohesion: 0.02
Nodes (103): Index, all_indexes_same(), default_index(), _get_combined_index(), _get_distinct_objs(), get_objs_combined_axis(), Return a list with distinct elements of "objs" (different ids).     Preserves or, Return the union or intersection of indexes.      Parameters     ---------- (+95 more)

### Community 11 - "Community 11"
Cohesion: 0.02
Nodes (19): array_ufunc(), _assign_where(), default_array_ufunc(), dispatch_reduction_ufunc(), dispatch_ufunc_with_out(), Methods that can be shared by many array-like classes or subclasses:     Series, Compatibility with numpy ufuncs.      See also     --------     numpy.org/doc/st, # TODO: When we support multiple values in __finalize__, this (+11 more)

### Community 12 - "Community 12"
Cohesion: 0.02
Nodes (76): CSVFormatter, Module for formatting output data into CSV files., Dictionary used for storing number formatting settings., Create the writer & save., buffer_put_lines(), _Datetime64Formatter, EngFormatter, _ExtensionArrayFormatter (+68 more)

### Community 13 - "Community 13"
Cohesion: 0.03
Nodes (1): NDFrame

### Community 14 - "Community 14"
Cohesion: 0.08
Nodes (131): BaseGroupBy, Flags, Flags that apply to pandas objects.      “Flags” differ from “metadata”. Flags r, Equivalent to public method `where`, except that `other` is not         applied, # TODO: can we use a zero-copy alternative to "repeat"?, Replace values where the condition is False.          This method allows conditi, Replace values where the condition is True.          Where ``cond`` is True, the, Shift index by desired number of periods with an optional time `freq`. (+123 more)

### Community 15 - "Community 15"
Cohesion: 0.02
Nodes (78): _adjust_dates_anchored(), asfreq(), _asfreq_compat(), DatetimeIndexResampler, DatetimeIndexResamplerGroupby, _get_period_range_edges(), get_resampler(), get_resampler_for_grouping() (+70 more)

### Community 16 - "Community 16"
Cohesion: 0.04
Nodes (8): ensure_index(), Index, _maybe_try_sort(), Cached check equivalent to isinstance(self, MultiIndex), Get integer location, slice or boolean mask for requested label.          The re, _unpack_nested_dtype(), _validate_join_method(), IndexOpsMixin

### Community 17 - "Community 17"
Cohesion: 0.02
Nodes (67): ADBCDatabase, BaseEngine, _convert_arrays_to_dataframe(), get_engine(), get_schema(), _get_unicode_name(), _get_valid_sqlite_name(), _handle_date_column() (+59 more)

### Community 18 - "Community 18"
Cohesion: 0.02
Nodes (76): cat_core(), cat_safe(), forbid_nonstring_types(), _get_group_names(), _get_single_group_name(), Split the string at the first occurrence of `sep`.          This method splits t, Split the string at the last occurrence of `sep`.          This method splits th, Extract element from each component at specified position or with specified key. (+68 more)

### Community 19 - "Community 19"
Cohesion: 0.03
Nodes (46): IntervalArray, _maybe_convert_platform_interval(), ExtensionIndex, ExtensionIndex, Index subclass for indexes backed by ExtensionArray., Convert value to be insertable to underlying array., _get_next_label(), _get_prev_label() (+38 more)

### Community 20 - "Community 20"
Cohesion: 0.03
Nodes (55): GroupByApply, DataFrameGroupBy, NamedAgg, Define the SeriesGroupBy and DataFrameGroupBy classes that hold the groupby inte, # TODO: validate types on ScalarResult and move to _typing, Return a Series or DataFrame containing counts of unique rows.          The resu, Helper for column specific aggregation with control over output column names., # TODO: should we do this inside II? (+47 more)

### Community 21 - "Community 21"
Cohesion: 0.02
Nodes (62): _DataFrameTableBuilder, _DataFrameTableBuilderNonVerbose, _DataFrameTableBuilderVerbose, _get_dataframe_dtype_counts(), _initialize_memory_usage(), _put_str(), Memory usage in a form of human readable string., Make string of specified length, padding to the right if necessary.      Paramet (+54 more)

### Community 22 - "Community 22"
Cohesion: 0.02
Nodes (60): BooleanDtype, Return the array type associated with this dtype.          Returns         -----, Extension dtype for boolean data.      This is a pandas Extension dtype for bool, Define extension dtypes., Parameters         ----------         freq : PeriodDtype, BaseOffset, or string, The frequency object of this PeriodDtype.          The `freq` property returns t, Strict construction from a string, raise a TypeError if not         possible, Return a boolean if the passed type is an actual dtype that we         can match (+52 more)

### Community 23 - "Community 23"
Cohesion: 0.03
Nodes (3): ArrowExtensionArray, ArrowStringArrayMixin, ExtensionArrayNaResult

### Community 24 - "Community 24"
Cohesion: 0.03
Nodes (61): _background_gradient(), _bar(), _highlight_between(), _highlight_value(), Module for applying conditional formatting to DataFrames and Series., Write Styler to a file, buffer or string in Typst format.          .. versionadd, Write Styler to a file, buffer or string in HTML-CSS format.          The output, Write Styler to a file, buffer or string in text format.          Produces a pla (+53 more)

### Community 25 - "Community 25"
Cohesion: 0.03
Nodes (74): Float32Dtype, Float64Dtype, FloatingArray, An ExtensionDtype to hold a single size of floating dtype.      These specific i, Return the array type associated with this dtype.          Returns         -----, Safely cast the values to the given dtype.          "safe" in this context means, Array of floating (optional missing) values.      .. warning::         FloatingA, Int16Dtype (+66 more)

### Community 26 - "Community 26"
Cohesion: 0.03
Nodes (50): ExtensionArrayNaResult, DatetimeArray, Returns True if all of the dates are at midnight ("no time"), floor_div_int64(), mod_int(), # TODO: By using `zero_copy_only` it may be possible to implement this, The number of bytes needed to store this object in memory., Length of this array.          Returns         -------         length : int (+42 more)

### Community 27 - "Community 27"
Cohesion: 0.05
Nodes (67): ResamplerWindowApply, FixedWindowIndexer, GroupbyIndexer, Indexer objects for computing start/end window bounds for rolling operations, Creates window boundaries that are of fixed length., Computes the bounds of a window.          Parameters         ----------, Creates window boundaries that are of variable length, namely for time series., Computes the bounds of a window.          Parameters         ---------- (+59 more)

### Community 28 - "Community 28"
Cohesion: 0.03
Nodes (34): BaseExecutionEngine, frame_apply(), is_multi_agg_with_relabel(), _make_unique_kwarg_list(), _managle_lambda_list(), maybe_mangle_lambdas(), NDFrameApply, normalize_keyword_aggregation() (+26 more)

### Community 29 - "Community 29"
Cohesion: 0.05
Nodes (69): CategoricalDescription, ParserBase, Checks if length of data is equal to length of column names.          One set of, Validates that all usecols are present in a given         list of names. If not,, CParserWrapper, ensure_dtype_objs(), Set the columns that should not undergo dtype conversions.          Currently, a, Decide whether a parse_dates column is a candidate for the direct         char-b (+61 more)

### Community 30 - "Community 30"
Cohesion: 0.03
Nodes (47): Return the indices that would sort this array.          This method computes the, Sort the array in-place.          Reorders the elements of the array using :meth, Pad or backfill values, used by Series/DataFrame ffill and bfill.          This, Fill NA/NaN values using the specified method.          This method replaces mis, Return ExtensionArray without NA values.          This method removes all missin, Return boolean ndarray denoting duplicate values.          This method identifie, Shift values by desired number.          Newly introduced missing values are fil, Compute the ExtensionArray of unique values.          This method returns a new (+39 more)

### Community 31 - "Community 31"
Cohesion: 0.04
Nodes (89): can_hold_element(), coerce_indexer_dtype(), common_dtype_categorical_compat(), construct_1d_arraylike_from_scalar(), construct_1d_object_array_from_listlike(), construct_2d_arraylike_from_scalar(), convert_dtypes(), dict_compat() (+81 more)

### Community 32 - "Community 32"
Cohesion: 0.03
Nodes (32): BaseGrouper, BinGrouper, check_result_array(), DataSplitter, extract_result(), FrameSplitter, _is_indexed_like(), Provide classes to perform the groupby aggregate operations.  These are not expo (+24 more)

### Community 33 - "Community 33"
Cohesion: 0.04
Nodes (7): DatetimeLikeArrayMixin, TimelikeOps, infer_freq(), infer_freq_str(), Infer the most likely frequency given the input index.      .. deprecated:: 3.1., Internal version of infer_freq that returns a string without     emitting a depr, _TimedeltaFrequencyInferer

### Community 34 - "Community 34"
Cohesion: 0.05
Nodes (1): BaseMaskedArray

### Community 35 - "Community 35"
Cohesion: 0.03
Nodes (41): ABC, Accessors for arrow-backed data., # TODO: Support negative key but pyarrow does not allow, # TODO: Support negative start/stop/step, ideally this would be added, # TODO: When adding negative step support, _BaseInfo, Base class for DataFrameInfo and SeriesInfo.      Parameters     ----------, Dtypes.          Returns         -------         dtypes : sequence             D (+33 more)

### Community 36 - "Community 36"
Cohesion: 0.05
Nodes (33): ExpandingIndexer, Computes the bounds of a window.          Parameters         ----------, RollingAndExpandingMixin, Expanding, ExpandingGroupby, Calculate the expanding First (left-most) element of the window.          At eac, Calculate the expanding Last (right-most) element of the window.          At eac, Calculate the expanding quantile.          At each step the specified quantile i (+25 more)

### Community 37 - "Community 37"
Cohesion: 0.05
Nodes (18): check_bool_indexer(), check_dict_or_set_indexers(), convert_from_missing_indexer_tuple(), convert_missing_indexer(), _expansion_can_hold(), _iLocIndexer, infer_and_maybe_downcast(), _is_2d_value() (+10 more)

### Community 38 - "Community 38"
Cohesion: 0.04
Nodes (77): classes(), _classes_and_not_datetimelike(), ensure_python_int(), ensure_str(), _get_dtype(), is_1d_only_ea_dtype(), is_all_strings(), is_any_real_numeric_dtype() (+69 more)

### Community 39 - "Community 39"
Cohesion: 0.06
Nodes (27): ExcelFile, inspect_excel_format(), Extensions that writer engine supports., Mapping of sheet names to sheet objects., Book instance. Class type will depend on the engine used.          This attribut, Write given formatted cells into Excel an excel sheet          Parameters, Save workbook to disk., Format string for dates written into Excel files (e.g. 'YYYY-MM-DD'). (+19 more)

### Community 40 - "Community 40"
Cohesion: 0.05
Nodes (17): _ints_to_td64ns(), _objects_to_td64ns(), sequence_to_td64ns(), TimedeltaArray, _validate_td64_dtype(), DatetimeTimedeltaMixin, _new_TimedeltaIndex(), implement the TimedeltaIndex (+9 more)

### Community 41 - "Community 41"
Cohesion: 0.04
Nodes (60): CSSDict, _default_formatter(), _element(), _escape_latex(), _escape_latex_math(), format_table_styles(), _get_level_lengths(), _get_trimming_maximums() (+52 more)

### Community 42 - "Community 42"
Cohesion: 0.06
Nodes (36): add_ops(), _compose(), disallow(), _filter_nodes(), _is_type(), _node_not_implemented(), _op_maker(), PandasExprVisitor (+28 more)

### Community 43 - "Community 43"
Cohesion: 0.05
Nodes (17): Apply, include_axis(), Aggregate a list of named functions using DataFrame-level reductions.          I, compat apply method for funcs in listlikes and dictlikes.           Used for eac, Provide an implementation for the aggregators.          Returns         -------, Transform a DataFrame or Series.          Returns         -------         DataFr, Compute transform in the case of a dict-like func, Compute transform in the case of a string or callable func (+9 more)

### Community 44 - "Community 44"
Cohesion: 0.05
Nodes (2): BaseBlockManager, _preprocess_slice_or_indexer()

### Community 45 - "Community 45"
Cohesion: 0.03
Nodes (33): transforms.py is for shape-preserving functions., get_version(), import_optional_dependency(), Import an optional dependency.      By default, if a dependency is missing an Im, support pyarrow compatibility across versions, Safe wrapper for pyarrow.compute.fill_null with fallback for Windows + pyarrow 2, _safe_fill_null(), define generic base classes for pandas objects (+25 more)

### Community 46 - "Community 46"
Cohesion: 0.04
Nodes (31): dt64arr_to_periodarr(), _field_to_int64(), _get_ordinal_range(), _make_field_arrays(), period_array(), raise_on_incompatible(), _range_from_fields(), Determine the freq to stamp on the DatetimeArray returned by         ``self.to_t (+23 more)

### Community 48 - "Community 48"
Cohesion: 0.06
Nodes (21): _convert_datetimes(), SAS7BDATReader, _sas_to_gregorian_correction(), _utf8_translation_table(), _handle_truncated_float_vec(), _parse_date(), _parse_float_vec(), Read a SAS XPort format file into a Pandas DataFrame.  Based on code from Jack C (+13 more)

### Community 49 - "Community 49"
Cohesion: 0.05
Nodes (24): BaseExcelReader, Reader using calamine engine (xlsx/xls/xlsb/ods).          Parameters         --, Read tables out of OpenDocument formatted files.          Parameters         ---, Property for compat with other readers., Return a list of sheet names present in the document, OpenpyxlWriter, Mapping of sheet names to sheet objects., Save workbook to disk. (+16 more)

### Community 50 - "Community 50"
Cohesion: 0.05
Nodes (25): Correctly construct numpy arrays when passed to `np.asarray()`., An instance of 'ExtensionDtype'., Boolean NumPy array indicating if each value is missing.          This should re, Return a shallow copy of the array.          Underlying ChunkedArray is immutabl, Fill NA/NaN values using the specified method.          Parameters         -----, Return an array and missing value suitable for factorization.          Returns, Encode the arrow array as an enumerated type.          Parameters         ------, Find indices where elements should be inserted to maintain order.          Find (+17 more)

### Community 51 - "Community 51"
Cohesion: 0.05
Nodes (13): MPLPlot, get left (primary) or right (secondary) axes, Return the index of the axis where the column at col_idx should be plotted, Look for error keyword arguments and return the actual errorbar data         or, Base class for assembling a pandas plot using matplotlib      Parameters     ---, Validate the subplots parameter          - check type and content         - chec, check whether ax has data, Common post process for each axes (+5 more)

### Community 52 - "Community 52"
Cohesion: 0.08
Nodes (57): AttributeError, OptionError, Exception raised for pandas.options.      Backwards compatible with KeyError che, AttributeConflictWarning, CategoricalConversionWarning, ChainedAssignmentError, ClosedFileError, CSSWarning (+49 more)

### Community 53 - "Community 53"
Cohesion: 0.07
Nodes (10): check_ndim(), EABackedBlock, ensure_block_shape(), extend_blocks(), external_values(), extract_pandas_array(), get_block_type(), maybe_coerce_values() (+2 more)

### Community 54 - "Community 54"
Cohesion: 0.06
Nodes (56): _check_object_for_strings(), diff(), duplicated(), _ensure_arraylike(), _ensure_data(), factorize(), factorize_array(), factorize_monotonic_codes() (+48 more)

### Community 55 - "Community 55"
Cohesion: 0.04
Nodes (51): all_none(), all_not_none(), any_none(), any_not_none(), apply_if_callable(), asarray_tuplesafe(), cast_scalar_indexer(), convert_to_list_like() (+43 more)

### Community 56 - "Community 56"
Cohesion: 0.07
Nodes (26): BaseWindow, BaseWindowGroupby, ExponentialMovingWindowIndexer, Calculate ewm window bounds (the entire window), Computes the bounds of a window.          Parameters         ----------, _calculate_deltas(), ExponentialMovingWindow, ExponentialMovingWindowGroupby (+18 more)

### Community 57 - "Community 57"
Cohesion: 0.07
Nodes (33): AbstractEngine, _check_ne_builtin_clash(), NumExprEngine, PythonEngine, Engine classes for :func:`~pandas.eval`, Return an evaluated expression.          Parameters         ----------         e, Evaluate an expression in Python space.      Mostly for testing purposes., Attempt to prevent foot-shooting in a helpful way.      Parameters     --------- (+25 more)

### Community 58 - "Community 58"
Cohesion: 0.06
Nodes (2): DatetimeIndex, _time_to_micros()

### Community 59 - "Community 59"
Cohesion: 0.07
Nodes (36): bday_to_datetime(), get_finder(), Locates the ticks along an axis controlled by a :class:`Series`.      Parameters, Returns the default locations of ticks., Return the locations of the ticks., Sets the view limits to the nearest multiples of base that contain the         d, Formats the ticks along an axis controlled by a :class:`PeriodIndex`.      Param, Returns the default ticks spacing. (+28 more)

### Community 60 - "Community 60"
Cohesion: 0.07
Nodes (23): create_dataframe_from_blocks(), Low-level function to create a DataFrame from arrays as they are     representin, BlockManager, _consolidate(), create_block_manager_from_blocks(), create_block_manager_from_column_arrays(), ensure_np_dtype(), _form_blocks() (+15 more)

### Community 61 - "Community 61"
Cohesion: 0.12
Nodes (4): Reads value labels with variable length strings (108 and later format), Reads value labels with fixed-length strings (105 and earlier format), read_stata(), StataReader

### Community 62 - "Community 62"
Cohesion: 0.05
Nodes (36): after_nearest_workday(), before_nearest_workday(), get_calendar(), Holiday, HolidayCalendarFactory(), HolidayCalendarMetaClass, nearest_workday(), next_monday() (+28 more)

### Community 63 - "Community 63"
Cohesion: 0.07
Nodes (43): _build_option_description(), config_prefix(), deprecate_option(), DeprecatedOption, describe_option(), get_default_val(), _get_deprecated_option(), get_option() (+35 more)

### Community 64 - "Community 64"
Cohesion: 0.07
Nodes (44): arrays_to_mgr(), _check_values_indices_shape_match(), convert_object_array(), dataclasses_to_dicts(), dict_to_mgr(), _ensure_2d(), _extract_index(), _finalize_columns_and_data() (+36 more)

### Community 65 - "Community 65"
Cohesion: 0.05
Nodes (9): FrameApply, FrameColumnApply, FrameRowApply, we have an empty result; at least 1 axis is 0          we will try to apply the, apply to the values as a numpy array, return the results for the rows, Build a callable that constructs an EA row for a given row index.          Speci, return the results for the columns (+1 more)

### Community 66 - "Community 66"
Cohesion: 0.06
Nodes (20): Custom groupby class for time-interval grouping.      Parameters     ----------, TimeGrouper, _convert_grouper(), _factorize_monotonic(), get_grouper(), Grouping, Provide user facing operators for doing the split part of the split-apply-combin, Parameters         ----------         obj : Series or DataFrame             Obje (+12 more)

### Community 67 - "Community 67"
Cohesion: 0.05
Nodes (19): DatetimeIndexOpsMixin, period_range(), PeriodIndex, Convert the PeriodIndex to the specified frequency `freq`.          Equivalent t, Cast to DatetimeIndex.          If possible, gives microsecond-unit DatetimeInde, The hour of the period.          Returns the hour component for each period in t, The minute of the period.          Returns the minute component for each period, The second of the period.          Returns the second component for each period (+11 more)

### Community 68 - "Community 68"
Cohesion: 0.06
Nodes (26): ExcelWriter, checks that path's extension against the Writer's supported         extensions., Class for writing DataFrame objects into excel sheets.      The default ``engine, combine_kwargs(), _excel2num(), fill_mi_header(), get_default_engine(), maybe_convert_usecols() (+18 more)

### Community 69 - "Community 69"
Cohesion: 0.06
Nodes (26): _data_to_frame(), _EtreeFrameParser, get_data_from_filepath(), _LxmlFrameParser, _parse(), preprocess_data(), :mod:``pandas.io.xml`` is a module for reading XML., Parse xml data.          This method will call the other internal methods to (+18 more)

### Community 70 - "Community 70"
Cohesion: 0.09
Nodes (2): ArrowStringArrayMixin, Determine if regex pattern contains features not supported by RE2 / pyarrow.

### Community 71 - "Community 71"
Cohesion: 0.08
Nodes (1): DatetimeTimedeltaMixin

### Community 72 - "Community 72"
Cohesion: 0.09
Nodes (12): _pad_bytes(), _pad_bytes_new(), Take a char string and pads it with null bytes until it's length chars., Helper to call encode before writing to file for Python 3 compat., Helper to assert file is open before writing., Write 5 zeros for expansion fields, Takes a bytes instance and pads it with null bytes until it's length chars., Surround val with <tag></tag> (+4 more)

### Community 73 - "Community 73"
Cohesion: 0.06
Nodes (29): clean_backtick_quoted_toks(), clean_column_name(), create_valid_python_identifier(), ParseState, :func:`~pandas.eval` source string parsing functions, Function to emulate the cleaning of a backtick quoted name.      The purpose for, Splits a str into substrings along backtick characters (`).      Disregards back, Tokenize a Python source code string.      Parameters     ----------     source (+21 more)

### Community 74 - "Community 74"
Cohesion: 0.13
Nodes (2): Expression, Class representing a deferred column.      This is not meant to be instantiated

### Community 75 - "Community 75"
Cohesion: 0.05
Nodes (13): ExtensionArray, Map categories using an input mapping or function.          Parameters         -, Necessary for making this object picklable, Tests whether all elements evaluate True          Returns         -------, Tests whether at least one of elements evaluate True          Returns         --, Sum of non-NA/null values          Parameters         ----------         axis :, Mean of non-NA/null values.          Parameters         ----------         axis, An ExtensionArray for storing sparse data.      SparseArray efficiently stores d (+5 more)

### Community 76 - "Community 76"
Cohesion: 0.08
Nodes (32): _annual_finder(), bday_count(), bday_count_array(), bday_offset_array(), _daily_finder(), deregister(), _get_datevalue(), _get_default_annual_spacing() (+24 more)

### Community 77 - "Community 77"
Cohesion: 0.10
Nodes (10): PythonParser, Try several cases to get lines:          0) There are headers on row 0 and row 1, Cast values to specified type          Parameters         ----------         val, Sets self._col_indices          usecols_key is used if there are string usecols., Return a line from buffer, filling buffer if required., Checks whether the file begins with the BOM character.         If it does, remov, Check if a line is empty or not.          Parameters         ----------, Alert a user about a malformed row, depending on value of         `self.on_bad_l (+2 more)

### Community 78 - "Community 78"
Cohesion: 0.08
Nodes (17): ArrowTemporalProperties, CombinedDatetimelikeProperties, DatetimeProperties, PeriodProperties, Properties, datetimelike delegation, Accessor object for datetimelike properties of the Series values.      Examples, Return the data as a Series of :class:`datetime.datetime` objects.          Time (+9 more)

### Community 79 - "Community 79"
Cohesion: 0.06
Nodes (10): Overriding parent method for the case of all RangeIndex instances.          When, Conserve RangeIndex type for scalar and slice keys., Fastpath for __getitem__ when we know we have a slice., Round each value in the Index to the given number of decimals.          Paramete, Create :class:`pandas.RangeIndex` from a ``range`` object.          This method, return the class to use for construction, Create a new RangeIndex with the same class as the caller, don't copy the, Make a copy of this object.          Name is set on the new object.          Par (+2 more)

### Community 80 - "Community 80"
Cohesion: 0.10
Nodes (5): BaseExprVisitor, create and return the numexpr condition and filter, hold a term value that we use to construct a condition/filter, quote the string if not encoded else encode and return, TermValue

### Community 81 - "Community 81"
Cohesion: 0.07
Nodes (22): DeepChainMap, ensure_scope(), _get_pretty_string(), Module for scope operations, Return a prettier version of obj.      Parameters     ----------     obj : objec, Object to hold scope, with a few bells to deal with some custom syntax     and c, Return whether we have any extra scope.          For example, DataFrames pass Th, Resolve a variable name in a possibly local context.          Parameters (+14 more)

### Community 82 - "Community 82"
Cohesion: 0.09
Nodes (29): CheckedCall, determine_clipboard(), init_dev_clipboard_clipboard(), init_klipper_clipboard(), init_no_clipboard(), init_osx_pbcopy_clipboard(), init_osx_pyobjc_clipboard(), init_qt_clipboard() (+21 more)

### Community 83 - "Community 83"
Cohesion: 0.07
Nodes (11): BinOp, ConditionBinOp, FilterBinOp, JointFilterBinOp, return True if this is a valid field, return True if this is a valid column name for generation (e.g. an         actua, the metadata of my field, create and return the op string for this TermValue (+3 more)

### Community 84 - "Community 84"
Cohesion: 0.07
Nodes (25): dict, andrews_curves(), autocorrelation_plot(), bootstrap_plot(), deregister(), lag_plot(), _Options, parallel_coordinates() (+17 more)

### Community 85 - "Community 85"
Cohesion: 0.10
Nodes (12): _FrequencyInferer, get_period_alias(), _is_annual(), _is_monthly(), _is_multiple(), _is_quarterly(), is_subperiod(), is_superperiod() (+4 more)

### Community 86 - "Community 86"
Cohesion: 0.07
Nodes (21): DataFrame, Series, box_expected(), convert_rows_list_to_csv_str(), external_error_raised(), get_cython_table_params(), get_finest_unit(), get_op_from_name() (+13 more)

### Community 87 - "Community 87"
Cohesion: 0.08
Nodes (23): _adj_justify(), adjoin(), _as_escaped_string(), default_pprint(), _EastAsianTextAdjustment, format_object_summary(), get_adjustment(), _justify() (+15 more)

### Community 88 - "Community 88"
Cohesion: 0.09
Nodes (20): PeriodConverter, _color_in_style(), PiePlot, Specify whether xlabel/ylabel should be used to override index name, Manage style and color based on column number and its label.         Returns tup, Check if there is a color letter in the style string., # TODO: tighter typing for first return?, Specify kind str. Must be overridden in child class (+12 more)

### Community 89 - "Community 89"
Cohesion: 0.10
Nodes (19): Reshape the data of a frame for stack.      This function takes care of most of, # NOTE: This doesn't deal with hierarchical columns yet, Unstack an ExtensionArray-backed Series.      The ExtensionDtype is preserved., Convert DataFrame to Series with multi-level Index. Columns become the     secon, Helper class to unstack data / pivot with multi-level index      Parameters, Creates a MultiIndex from the first N-1 levels of this MultiIndex., Re-orders the values when stacking multiple extension-arrays.      The indirect, _reorder_for_extension_array_stack() (+11 more)

### Community 90 - "Community 90"
Cohesion: 0.07
Nodes (7): _BaseVersion, _cmpkey(), InvalidVersion, _parse_letter_version(), _parse_local_version(), An invalid version was found, users should refer to PEP 440.      The ``InvalidV, _Version

### Community 91 - "Community 91"
Cohesion: 0.10
Nodes (31): compress_group_index(), _decons_group_index(), decons_obs_group_ids(), ensure_key_mapped(), _ensure_key_mapped_multiindex(), get_compressed_ids(), get_group_index(), get_group_index_sorter() (+23 more)

### Community 92 - "Community 92"
Cohesion: 0.11
Nodes (28): _akima_interpolate(), _arrow_temporal_to_i8(), _backfill_1d(), _backfill_2d(), check_value_size(), clean_fill_method(), clean_interp_method(), clean_reindex_fill_method() (+20 more)

### Community 93 - "Community 93"
Cohesion: 0.12
Nodes (4): CSSToExcelConverter, A callable for converting CSS declarations to ExcelWriter styles      Supports p, Convert CSS declarations to ExcelWriter style.          Parameters         -----, Check if color code is shorthand.          #FFF is a shorthand as opposed to ful

### Community 94 - "Community 94"
Cohesion: 0.08
Nodes (12): BaseExprVisitor, Constant, maybe_expression(), PyTablesExprVisitor, PyTablesScope, manage PyTables query interface via Expressions, # TODO: return None might never be reached, Validate that the where statement is of the right type.      The type may either (+4 more)

### Community 95 - "Community 95"
Cohesion: 0.10
Nodes (17): Buffer, PandasBuffer, PandasBufferPyarrow, Buffer size in bytes., Pointer to start of the buffer as an integer., Represent this structure as DLPack interface., Device type and device ID for where the data in the buffer resides., Data in the buffer is guaranteed to be contiguous in memory. (+9 more)

### Community 96 - "Community 96"
Cohesion: 0.11
Nodes (11): ODSWriter, Write the frame cells using odf, Convert cell attributes to OpenDocument attributes          Parameters         -, Convert cell data to an OpenDocument spreadsheet cell          Parameters, Convert a style dictionary to an OpenDocument style sheet          Parameters, Create freeze panes in the sheet.          Parameters         ----------, Book instance of class odf.opendocument.OpenDocumentSpreadsheet.          This a, Mapping of sheet names to sheet objects. (+3 more)

### Community 97 - "Community 97"
Cohesion: 0.07
Nodes (29): check_array_indexer(), check_key_length(), check_setitem_lengths(), disallow_ndim_indexing(), getitem_returns_view(), is_empty_indexer(), is_list_like_indexer(), is_scalar_indexer() (+21 more)

### Community 98 - "Community 98"
Cohesion: 0.08
Nodes (27): cartesian_product(), _lexsort_depth(), maybe_droplevels(), MultiIndexPyIntEngine, MultiIndexUInt16Engine, MultiIndexUInt32Engine, MultiIndexUInt64Engine, MultiIndexUInt8Engine (+19 more)

### Community 99 - "Community 99"
Cohesion: 0.11
Nodes (18): _border_expander(), CSSResolver, _lowercase_css_values(), Utilities for interpreting CSS from Stylers for formatting non-HTML outputs., # TODO: Can we use current color as initial value to comply with CSS standards?, # TODO: Warn user if item entered more than once (e.g. "border: red green"), Preserves the case for all characters within single or double-quoted strings,, A callable for parsing and resolving CSS to atomic properties. (+10 more)

### Community 100 - "Community 100"
Cohesion: 0.10
Nodes (28): _adjust_to_origin(), _array_strptime_with_fallback(), _assemble_from_unit_mappings(), _box_as_indexlike(), _coerce_origin_overflow(), _convert_and_box_cache(), _convert_listlike_datetimes(), FulldatetimeDict (+20 more)

### Community 101 - "Community 101"
Cohesion: 0.09
Nodes (27): _check_arg_length(), _check_for_default_values(), _check_for_invalid_keys(), Module that contains many useful utilities for validating data or function argum, Checks whether the length of the `*args` argument passed into a function     has, Checks whether 'kwargs' contains any keys that are not     in 'compat_args' and, Checks whether parameters passed to the **kwargs argument in a     function `fna, Checks whether parameters passed to the *args and **kwargs argument in a     fun (+19 more)

### Community 102 - "Community 102"
Cohesion: 0.09
Nodes (10): LinePlot, _grouped_hist(), _grouped_plot(), hist_frame(), hist_series(), HistPlot, KdePlot, merge BoxPlot/KdePlot properties to passed kwds (+2 more)

### Community 103 - "Community 103"
Cohesion: 0.08
Nodes (13): PandasDelegate, BaseAccessor, Create a scipy.sparse.coo_matrix from a Series with MultiIndex.          Use row, Convert a Series from sparse values to dense.          Returns         -------, DataFrame accessor for sparse data.      It allows users to interact with a `Dat, Create a new DataFrame from a scipy sparse matrix.          This method converts, Convert a DataFrame with sparse values to dense.          This method converts a, Return the contents of the frame as a sparse SciPy COO matrix.          This met (+5 more)

### Community 104 - "Community 104"
Cohesion: 0.16
Nodes (12): _construct_from_dt64_naive(), _generate_range(), _infer_tz_from_endpoints(), maybe_convert_dtype(), _maybe_infer_tz(), _maybe_localize_point(), _maybe_normalize_endpoints(), objects_to_datetime64() (+4 more)

### Community 106 - "Community 106"
Cohesion: 0.08
Nodes (12): IndexOpsMixin, Return True if there are any NaNs.          Enables various performance speedups, Return True if values in the object are monotonically increasing.          This, Return True if values in the object are monotonically decreasing.          This, Construct an appropriately-wrapped result from the ArrayLike result         of a, Common ops mixin to support a unified interface / docs for Series / Index, Return the first element of the underlying data as a Python scalar.          Thi, The ExtensionArray of the data backing this Series or Index.          This prope (+4 more)

### Community 107 - "Community 107"
Cohesion: 0.08
Nodes (1): SingleBlockManager

### Community 108 - "Community 108"
Cohesion: 0.11
Nodes (26): _convert_arrays_and_get_rizer_klass(), _factorize_keys(), _get_empty_indexer(), get_join_indexers(), get_join_indexers_non_unique(), _get_join_keys(), _get_multiindex_indexer(), _get_no_sort_one_missing_indexer() (+18 more)

### Community 109 - "Community 109"
Cohesion: 0.08
Nodes (11): ArrowAccessor, ListAccessor, Index or slice lists in the Series.          Retrieves elements at the given int, Flatten list values.          Each list element is expanded into separate rows,, Accessor object for structured data properties of the Series values.      Parame, Return the dtype object of each child field of the struct.          The returned, Extract a child field of a struct as a Series.          This method accesses ind, Extract all child fields of a struct as a DataFrame.          Each child field o (+3 more)

### Community 110 - "Community 110"
Cohesion: 0.08
Nodes (25): is_array_like(), is_dataclass(), is_dict_like(), is_file_like(), is_hashable(), is_named_tuple(), is_nested_list_like(), is_number() (+17 more)

### Community 111 - "Community 111"
Cohesion: 0.11
Nodes (15): asuint32(), asuint64(), complexobject_cmp(), complexobject_hash(), floatobject_cmp(), floatobject_hash(), kh_complex128_hash_func(), kh_complex64_hash_func() (+7 more)

### Community 112 - "Community 112"
Cohesion: 0.08
Nodes (14): PandasObject, PlotAccessor, Plot Series or DataFrame as lines.          This function is useful to plot line, Vertical bar plot.          A bar plot is a plot that presents categorical data, Make a horizontal bar plot.          A horizontal bar plot is a plot that presen, r"""         Make a box plot of the DataFrame columns.          A box plot is a, Draw one histogram of the DataFrame's columns.          A histogram is a represe, Generate Kernel Density Estimate plot using Gaussian kernels.          In statis (+6 more)

### Community 113 - "Community 113"
Cohesion: 0.13
Nodes (24): array(), ensure_wrapped_if_datetimelike(), extract_array(), _maybe_repeat(), range_to_ndarray(), Constructor functions intended to be shared by pd.array, Series.__init__, and In, Extract the ndarray or ExtensionArray from a Series or Index.      For all other, Wrap datetime64 and timedelta64 ndarrays in DatetimeArray/TimedeltaArray. (+16 more)

### Community 114 - "Community 114"
Cohesion: 0.09
Nodes (12): _DataFrameInfoPrinter, _InfoPrinterAbstract, Class for printing dataframe or series info., Save dataframe info into buffer., Create instance of table builder., Class for printing dataframe info.      Parameters     ----------     info : Dat, Maximum info rows to be displayed., Check if number of columns to be summarized does not exceed maximum. (+4 more)

### Community 115 - "Community 115"
Cohesion: 0.09
Nodes (5): BoxPlot, BP, _grouped_plot_by_column(), Set the tick labels of a given axis.      Due to https://github.com/matplotlib/m, _set_ticklabels()

### Community 116 - "Community 116"
Cohesion: 0.10
Nodes (24): arithmetic_op(), _bool_arith_check(), comp_method_OBJECT_ARRAY(), comparison_op(), fill_binop(), get_array_op(), logical_op(), _masked_arith_op() (+16 more)

### Community 117 - "Community 117"
Cohesion: 0.29
Nodes (23): assert_almost_equal(), assert_attr_equal(), assert_categorical_equal(), assert_class_equal(), assert_copy(), assert_datetime_array_equal(), assert_dict_equal(), assert_equal() (+15 more)

### Community 118 - "Community 118"
Cohesion: 0.20
Nodes (23): ColumnNullType, DtypeKind, Integer enum for data types.      Attributes     ----------     INT : int, Integer enum for null type representation.      Attributes     ----------     NO, buffer_to_ndarray(), categorical_column_to_series(), datetime_column_to_ndarray(), from_dataframe() (+15 more)

### Community 119 - "Community 119"
Cohesion: 0.14
Nodes (23): _bins_to_cuts(), _coerce_to_type(), cut(), _format_labels(), _infer_precision(), _is_dt_or_td(), _nbins_to_bins(), _postprocess_for_cut() (+15 more)

### Community 120 - "Community 120"
Cohesion: 0.09
Nodes (18): Appender, deprecate(), deprecate_kwarg(), deprecate_nonkeyword_arguments(), _format_argument_list(), future_version_msg(), indent(), Decorator to deprecate a keyword argument of a function.      Parameters     --- (+10 more)

### Community 121 - "Community 121"
Cohesion: 0.15
Nodes (18): add_minutes_to_datetimestruct(), days_to_yearsdays(), extract_unit(), get_datetimestruct_days(), is_leapyear(), npy_datetimestruct_to_datetime(), pandas_datetime_to_datetimestruct(), scale_time_with_underflow_check() (+10 more)

### Community 122 - "Community 122"
Cohesion: 0.09
Nodes (13): Column, A column object, with only the methods and properties required by the     interc, Size of the column, in elements.          Corresponds to DataFrame.num_rows() if, Offset of first element.          May be > 0 if using chunks; for example for a, Dtype description as a tuple ``(kind, bit-width, format string, endianness)``., If the dtype is categorical, there are two options:         - There are only val, Return the missing value (or "null") representation the column dtype         use, Number of null elements, if known.          Note: Arrow uses -1 to indicate "unk (+5 more)

### Community 123 - "Community 123"
Cohesion: 0.13
Nodes (22): _cycle_colors(), _derive_colors(), _gen_list_of_colors_from_iterable(), _get_cmap_instance(), _get_colors_from_color(), _get_colors_from_color_type(), _get_colors_from_colormap(), get_standard_colors() (+14 more)

### Community 124 - "Community 124"
Cohesion: 0.11
Nodes (9): _any(), _MergeOperation, Validate the 'how' parameter and return the actual join type and whether, Add one indicator column to each of the left and right inputs.          These co, Add an indicator column to the merge result.          This column indicates for, Restore index levels specified as `on` parameters          Here we check for cas, return the join indexers, Returns         -------         left_keys, right_keys, join_names, left_drop, ri (+1 more)

### Community 125 - "Community 125"
Cohesion: 0.15
Nodes (6): _make_sparse(), make_sparse_index(), Change the dtype of a SparseArray.          The output will always be a SparseAr, Convert ndarray to sparse format      Parameters     ----------     arr : ndarra, Fill missing values with `value`.          Parameters         ----------, Return boolean ndarray denoting duplicate values.          Parameters         --

### Community 126 - "Community 126"
Cohesion: 0.14
Nodes (19): _bool_arith_fallback(), _can_use_numexpr(), evaluate(), _evaluate_numexpr(), _evaluate_standard(), get_test_result(), _has_bool_dtype(), Expressions -----------  Offer fast expression evaluation through numexpr (+11 more)

### Community 127 - "Community 127"
Cohesion: 0.09
Nodes (3): # TODO: preserve the original class for the index, # TODO: Check index matching?, # TODO: Range index support

### Community 128 - "Community 128"
Cohesion: 0.14
Nodes (8): ParserBase, ArrowParserWrapper, Rename some arguments to pass to pyarrow, Whether the index column with the given name/position should be parsed         a, Match other engines' header handling: empty names become         "Unnamed: {i}", Processes data read in based on kwargs.          Parameters         ----------, Reads the contents of a CSV file into a DataFrame and         processes it accor, Validates keywords before passing to pyarrow.

### Community 129 - "Community 129"
Cohesion: 0.13
Nodes (14): # TODO: chunks are implemented now, probably this should return something, Number of null elements. Should always be known., # TODO: this will need correcting, # TODO: maybe store as bit array to save space?.., # TODO: implement for other bit/byte masks?, Buffer, ColumnBuffers, A verbatim copy (vendored) of the spec from https://github.com/data-apis/datafra (+6 more)

### Community 130 - "Community 130"
Cohesion: 0.14
Nodes (5): HexBinPlot, holds_integer(), PlanePlot, Abstract class for plotting on plane, currently scatter and hexbin., ScatterPlot

### Community 131 - "Community 131"
Cohesion: 0.14
Nodes (12): DirNamesMixin, Delete unwanted __dir__ for this object., Add additional __dir__ for this object., Provide method name lookup and completion.          Notes         -----, PandasObject, Return a string representation for a particular object., Reset cached properties. If ``key`` is passed, only clears that key., Generates the total memory usage for an object that returns         either a val (+4 more)

### Community 132 - "Community 132"
Cohesion: 0.12
Nodes (12): bottleneck_switch, _datetimelike_compat(), _ensure_numeric(), get_corr_func(), maybe_operate_rowwise(), na_accum_func(), nancorr(), nancov() (+4 more)

### Community 133 - "Community 133"
Cohesion: 0.12
Nodes (10): _datetime_to_stata_elapsed_vec(), Convert from datetime to SIF. https://www.stata.com/help.cgi?datetime      Param, Export DataFrame object to Stata dta format.          This method writes the con, Close the file if it was created by the writer.          If a buffer or file-lik, Converter for Stata StrLs      Stata StrLs map 8 byte values to strings which ar, Generates the GSO lookup table for the DataFrame          Returns         ------, Generates the binary blob of GSOs that is written to the dta file.          Para, Convert columns to StrLs if either very large or in the         convert_strl var (+2 more)

### Community 134 - "Community 134"
Cohesion: 0.14
Nodes (17): boxplot(), boxplot_frame(), boxplot_frame_groupby(), _get_plot_backend(), hist_frame(), hist_series(), holds_integer(), _load_backend() (+9 more)

### Community 135 - "Community 135"
Cohesion: 0.12
Nodes (7): DatetimeConverter, MilliSecondLocator, PandasAutoDateFormatter, PandasAutoDateLocator, Return the :class:`~matplotlib.units.AxisInfo` for *unit*.          *unit* is a, Pick the best locator based on a distance., Set the view limits to include the data range.

### Community 136 - "Community 136"
Cohesion: 0.11
Nodes (15): CompatValidator, process_skipna(), For compatibility with numpy libraries, pandas functions or methods have to acce, If 'Series.argmax' is called via the 'numpy' library, the third parameter     in, If 'Categorical.argsort' is called via the 'numpy' library, the first     parame, If 'NDFrame.clip' is called via the numpy library, the third parameter in     it, If this function is called via the 'numpy' library, the third parameter in     i, 'args' and 'kwargs' should be empty, except for allowed kwargs because all     o (+7 more)

### Community 138 - "Community 138"
Cohesion: 0.16
Nodes (18): _add_margins(), _build_names_mapper(), _compute_grand_margin(), _convert_by(), crosstab(), _generate_marginal_results(), _generate_marginal_results_without_values(), _get_names() (+10 more)

### Community 139 - "Community 139"
Cohesion: 0.11
Nodes (17): is_platform_arm(), is_platform_linux(), is_platform_little_endian(), is_platform_mac(), is_platform_power(), is_platform_riscv64(), is_platform_windows(), compat ======  Cross-compatible functions for different versions of Python.  Oth (+9 more)

### Community 140 - "Community 140"
Cohesion: 0.11
Nodes (1): Get Addition of DataFrame and other, column-wise.          Equivalent to ``DataF

### Community 141 - "Community 141"
Cohesion: 0.20
Nodes (15): array_equals(), array_equivalent(), _array_equivalent_datetimelike(), _array_equivalent_float(), _array_equivalent_object(), is_valid_na_for_dtype(), isna(), isna_all() (+7 more)

### Community 142 - "Community 142"
Cohesion: 0.11
Nodes (16): AbstractMethodError, DuplicateLabelError, EmptyDataError, IntCastingNaNError, NullFrequencyError, ParserError, Exception raised when converting (``astype``) an array with NaN to an integer ty, Exception raised when attempting to call an unsupported numpy function.      For (+8 more)

### Community 143 - "Community 143"
Cohesion: 0.16
Nodes (14): create_subplots(), do_adjust_figure(), flatten_axes(), format_date_labels(), _get_layout(), handle_shared_axes(), _has_externally_shared_axis(), maybe_adjust_figure() (+6 more)

### Community 144 - "Community 144"
Cohesion: 0.18
Nodes (16): _get_max_value(), _get_min_value(), max(), mean(), min(), _minmax(), prod(), masked_reductions.py is for reduction algorithms using a mask-based approach for (+8 more)

### Community 145 - "Community 145"
Cohesion: 0.12
Nodes (8): ExtensionDtype, The scalar type for the array, e.g. ``int``          It's expected ``ExtensionAr, Whether this dtype should be considered boolean.          By default, ExtensionD, Return the common dtype, if one exists.          Used in `find_common_type` impl, Can arrays of this dtype hold NA values?, The Index subclass to return from Index.__new__ when this dtype is         encou, Is transposing an array with this dtype zero-copy?          Only relevant for ca, A custom data type, to be paired with an ExtensionArray.      This enables suppo

### Community 146 - "Community 146"
Cohesion: 0.19
Nodes (7): BaseImpl, FastParquetImpl, get_engine(), _get_path_or_handle(), PyArrowImpl, read_parquet(), to_parquet()

### Community 147 - "Community 147"
Cohesion: 0.21
Nodes (16): _clean_keys_and_objs(), concat(), _concat_indexes(), _get_concat_axis_dataframe(), _get_concat_axis_series(), _get_result(), _get_sample_object(), _make_concat_multiindex() (+8 more)

### Community 148 - "Community 148"
Cohesion: 0.15
Nodes (15): _get_fill(), SparseArray data structure, # NOTE: If we guarantee that SparseDType(bool), Create a 0-dim ndarray containing the fill value      Parameters     ----------, Perform a binary operation between two arrays.      Parameters     ----------, # TODO: make this more flexible than just ndarray..., # NOTE: if fill_value doesn't change, # TODO: copy (+7 more)

### Community 149 - "Community 149"
Cohesion: 0.16
Nodes (6): ExtensionOpsMixin, ExtensionScalarOpsMixin, An interface for extending pandas with custom arrays.  .. warning::     This is, A base class for linking the operators to their dunder names.      .. note::, A mixin for defining ops on an ExtensionArray.      It is assumed that the under, A class method that returns a method that will correspond to an         operator

### Community 150 - "Community 150"
Cohesion: 0.15
Nodes (6): BooleanArray, coerce_to_array(), Construct BooleanArray from pyarrow Array/ChunkedArray., Coerce the input values array to numpy arrays with a mask.      Parameters     -, Array of boolean (True/False) data with missing values.      This is a pandas Ex, BaseMaskedArray

### Community 151 - "Community 151"
Cohesion: 0.22
Nodes (11): _concat_homogeneous_fastpath(), _concatenate_join_units(), concatenate_managers(), _dtype_to_na_value(), _get_block_for_concat_plan(), _get_combined_plan(), _get_empty_dtype(), _is_homogeneous_mgr() (+3 more)

### Community 152 - "Community 152"
Cohesion: 0.17
Nodes (15): convert_to_line_delimits(), json_normalize(), nested_to_record(), _normalize_json(), _normalize_json_ordered(), Main recursive function     Designed for the most basic use case of pd.json_norm, Order the top level keys and then recursively go to depth      Parameters     --, An optimized basic json_normalize      Converts a nested dict into a flat dict ( (+7 more)

### Community 153 - "Community 153"
Cohesion: 0.13
Nodes (2): BarhPlot, BarPlot

### Community 154 - "Community 154"
Cohesion: 0.14
Nodes (7): Implementation of nlargest and nsmallest., Implement n largest/smallest for DataFrame      Parameters     ----------     ob, Helper function to determine if dtype is valid for         nsmallest/nlargest me, Implement n largest/smallest for Series      Parameters     ----------     obj :, SelectN, SelectNFrame, SelectNSeries

### Community 155 - "Community 155"
Cohesion: 0.18
Nodes (8): Column, PandasColumn, See `self.dtype` for details., Return a dictionary containing the underlying buffers.         The returned dict, Return the buffer containing the data and the buffer's associated dtype., Return the buffer containing the mask values indicating missing data and, Return the buffer containing the offset values for variable-size binary, A column object, with only the methods and properties required by the     interc

### Community 156 - "Community 156"
Cohesion: 0.14
Nodes (5): col(), _parse_args(), _parse_kwargs(), _pretty_print_args_kwargs(), Generate deferred object representing a column of a DataFrame.      Any place wh

### Community 157 - "Community 157"
Cohesion: 0.14
Nodes (10): Load pickled pandas object (or any object) from file and return unpickled object, Pickle (serialize) object to file.      Parameters     ----------     obj : any, read_pickle(), to_pickle(), Protocol, _SparseMatrixLike, AbstractHolidayCalendar, Abstract interface to create holidays following certain rules.      A subclass n (+2 more)

### Community 158 - "Community 158"
Cohesion: 0.20
Nodes (2): AreaPlot, LinePlot

### Community 159 - "Community 159"
Cohesion: 0.21
Nodes (7): main(), Convert each input to appropriate format for table output., Layout some DataFrames in vertical/horizontal layout for explanation.     Used i, Calculate table shape considering index levels., Calculate appropriate figure size based on left and right data., Plot left / right DataFrames in specified layout.          Parameters         --, TablePlotter

### Community 160 - "Community 160"
Cohesion: 0.14
Nodes (1): Reversed Operations not available in the stdlib operator module. Defining these

### Community 161 - "Community 161"
Cohesion: 0.14
Nodes (12): DeprecationWarning, Pandas4Warning, PandasChangeWarning, PandasDeprecationWarning, PandasFutureWarning, Warning raised for any upcoming change.      This is the base class for all pand, Version where change will be enforced., Warning raised for an upcoming change that is a DeprecationWarning.      This wa (+4 more)

### Community 162 - "Community 162"
Cohesion: 0.40
Nodes (13): createDouble(), decode_any(), decode_array(), decode_false(), decode_null(), decode_numeric(), decode_object(), decode_string() (+5 more)

### Community 163 - "Community 163"
Cohesion: 0.33
Nodes (13): Buffer_AppendDoubleUnchecked(), Buffer_AppendIndentNewlineUnchecked(), Buffer_AppendIndentUnchecked(), Buffer_AppendIntUnchecked(), Buffer_AppendLongUnchecked(), Buffer_AppendShortHexUnchecked(), Buffer_EscapeStringUnvalidated(), Buffer_EscapeStringValidated() (+5 more)

### Community 164 - "Community 164"
Cohesion: 0.30
Nodes (12): int_min(), _node_cmp(), node_decref(), node_destroy(), node_incref(), node_init(), skiplist_destroy(), skiplist_init() (+4 more)

### Community 165 - "Community 165"
Cohesion: 0.17
Nodes (12): extract_bool_array(), putmask_inplace(), putmask_without_repeat(), EA-compatible analogue to np.putmask, Validate mask and check if this putmask operation is a no-op., If we have a SparseArray or BooleanArray, convert it to ndarray[bool]., Parameters     ----------     values : np.ndarray     num_set : int         For, ExtensionArray-compatible implementation of np.putmask.  The main     difference (+4 more)

### Community 166 - "Community 166"
Cohesion: 0.19
Nodes (12): delegate_names(), accessor.py contains base classes for implementing accessor properties that can, Add delegated names to a class using a class decorator.  This provides     an al, # TODO: Deprecate as name is now misleading, Register a custom accessor on objects.      Parameters     ----------     name :, Register a custom accessor on DataFrame objects.      Use as a decorator to add, Register a custom accessor on Series objects.      Use as a decorator to add a c, Register a custom accessor on Index objects.      Use as a decorator to add a cu (+4 more)

### Community 167 - "Community 167"
Cohesion: 0.15
Nodes (6): Return elementwise ``self ^ other``.          Logical XOR for boolean operands,, Return elementwise ``other ^ self``., Return elementwise ``self & other``.          Logical AND for boolean operands,, Return elementwise ``other & self``., Return elementwise ``self | other``.          Logical OR for boolean operands, b, Return elementwise ``other | self``.

### Community 168 - "Community 168"
Cohesion: 0.23
Nodes (10): _align_core(), _align_core_single_unary_op(), align_terms(), _any_pandas_objects(), Core eval alignment algorithms., Align a set of terms., Reconstruct an object given its type, raw value, and possibly empty     (None) a, Check a sequence of terms for instances of PandasObject. (+2 more)

### Community 169 - "Community 169"
Cohesion: 0.18
Nodes (4): mixin implementing the selection & aggregation interface on a group-like     obj, sub-classes to define         return a sliced object          Parameters, Infer the `selection` to pass to our constructor in _gotitem., SelectionMixin

### Community 170 - "Community 170"
Cohesion: 0.17
Nodes (3): is_terminal(), This module is imported from the pandas package __init__.py file in order to ens, Detect if Python is running in a terminal.      Returns True if Python is runnin

### Community 171 - "Community 171"
Cohesion: 0.32
Nodes (11): _arrow_dtype_mapping(), _arrow_string_types_mapper(), arrow_table_to_pandas(), _maybe_convert_string_index_to_object(), _maybe_convert_string_to_object(), _normalize_pytz_timezone(), _normalize_timezone_dtypes(), _normalize_timezone_index() (+3 more)

### Community 172 - "Community 172"
Cohesion: 0.20
Nodes (11): get_op_result_name(), has_castable_attr(), _maybe_match_name(), maybe_warn_listlike(), Boilerplate functions used in defining binary operations., Find the appropriate name to pin to an operation result.  This result     should, Try to find a name to attach to the result of an operation between     a and b., Warn when operating against a list-like that is neither a standard container (+3 more)

### Community 173 - "Community 173"
Cohesion: 0.18
Nodes (2): module_clear(), module_free()

### Community 174 - "Community 174"
Cohesion: 0.21
Nodes (6): accumulate_central_diffs(), accumulate_central_diffs_scalar_direct(), accumulate_mean(), accumulate_mean_scalar_direct(), accumulate_moments_simd_impl(), compute_moments_with_correction()

### Community 175 - "Community 175"
Cohesion: 0.24
Nodes (11): _assert_caught_expected_warnings(), _assert_caught_no_extra_warnings(), assert_produces_warning(), _assert_raised_with_correct_stacklevel(), _is_unexpected_warning(), maybe_produces_warning(), Return a context manager that possibly checks a warning based on the condition, Assert that there was the expected warning among the caught warnings. (+3 more)

### Community 176 - "Community 176"
Cohesion: 0.24
Nodes (11): combine_hash_arrays(), hash_array(), _hash_ndarray(), hash_pandas_object(), hash_tuples(), data hash pandas / numpy objects, Hash a MultiIndex / listlike-of-tuples efficiently.      Parameters     --------, Given a 1d array, return an array of deterministic integers.      This function (+3 more)

### Community 177 - "Community 177"
Cohesion: 0.35
Nodes (9): _convert_wrapper(), _get_take_nd_function(), _get_take_nd_function_cached(), take_2d_multi(), _take_2d_multi_object(), take_nd(), _take_nd_ndarray(), _take_preprocess_indexer_and_fill_value() (+1 more)

### Community 178 - "Community 178"
Cohesion: 0.18
Nodes (6): _in(), MathCall, _not_in(), Operator classes for eval., Compute the vectorized membership of ``x in y`` if possible, otherwise     use P, Compute the vectorized membership of ``x not in y`` if possible,     otherwise u

### Community 179 - "Community 179"
Cohesion: 0.18
Nodes (7): Public API for Rolling Window Indexers., FixedForwardWindowIndexer, Calculate window boundaries based on a non-fixed offset such as a BusinessDay., Computes the bounds of a window.          Parameters         ----------, Creates window boundaries for fixed-length windows that include the current row., Computes the bounds of a window.          Parameters         ----------, VariableOffsetWindowIndexer

### Community 180 - "Community 180"
Cohesion: 0.25
Nodes (11): createTypeContext(), get_long_attr(), get_nat(), get_values(), NpyArr_encodeLabels(), NpyArr_freeLabels(), Object_beginTypeContext(), Object_endTypeContext() (+3 more)

### Community 181 - "Community 181"
Cohesion: 0.20
Nodes (5): _asof_by_function(), _AsOfMerge, merge_asof(), return the join indexers, Perform a merge by key distance.      This is similar to a left-join except that

### Community 182 - "Community 182"
Cohesion: 0.24
Nodes (10): _check_is_partition(), coo_to_sparse_series(), _levels_to_axis(), Interaction with scipy.sparse matrices.  Currently only includes to_coo helpers., Convert a sparse Series to a scipy.sparse.coo_matrix using index     levels row_, Convert a scipy.sparse.coo_matrix to a Series with type sparse.      Parameters, For a MultiIndexed sparse Series `ss`, return `ax_coords` and `ax_labels`,     w, For an arbitrary MultiIndexed sparse Series return (v, i, j, ilabels,     jlabel (+2 more)

### Community 183 - "Community 183"
Cohesion: 0.18
Nodes (9): get_jit_arguments(), jit_user_function(), maybe_use_numba(), prepare_function_arguments(), Common utilities for Numba operations, Signal whether to use numba routines., Return arguments to pass to numba.JIT, falling back on pandas default JIT settin, If user function is not jitted already, mark the user's function     as jitable. (+1 more)

### Community 184 - "Community 184"
Cohesion: 0.20
Nodes (4): Find indices where elements should be inserted to maintain order.          Find, Fill NA/NaN values using the specified method.          Parameters         -----, Analogue to np.putmask(self, mask, value)          Parameters         ----------, Analogue to np.where(mask, self, value)          Parameters         ----------

### Community 185 - "Community 185"
Cohesion: 0.27
Nodes (9): generate_daily_offset_range(), _generate_range_overflow_safe(), _generate_range_overflow_safe_signed(), generate_regular_range(), Helper functions to generate range-like data for DatetimeArray (and possibly Tim, Generate a range for offsets whose on-offset dates are a subset of a     daily g, Calculate the second endpoint for passing to np.arange, checking     to avoid an, A special case for _generate_range_overflow_safe where `periods * stride`     ca (+1 more)

### Community 186 - "Community 186"
Cohesion: 0.22
Nodes (6): loads(), patch_pickle(), Pickle compatibility to pandas version 1.0, Analogous to pickle._loads., Temporarily patch pickle to use our unpickler., Unpickler

### Community 187 - "Community 187"
Cohesion: 0.27
Nodes (9): can_set_locale(), get_locales(), Helpers for configuring locale settings.  Name `localization` is chosen to avoid, Get all the locales that are available on the system.      Parameters     ------, Context manager for temporarily setting a locale.      Parameters     ----------, Check to see if we can set a locale, and subsequently get the locale,     withou, Return a list of normalized locales that do not throw an ``Exception``     when, set_locale() (+1 more)

### Community 188 - "Community 188"
Cohesion: 0.29
Nodes (9): concat_compat(), _get_result_dtype(), _is_nonempty(), Utility functions related to concat., union_categoricals for concat(union_categories=True).      Unlike union_categori, Combine list-like of Categorical-like, unioning categories.      All categories, provide concatenation of an array of arrays each of which is a single     'norma, union_categoricals() (+1 more)

### Community 189 - "Community 189"
Cohesion: 0.22
Nodes (2): _get_marker_compat(), scatter_matrix()

### Community 190 - "Community 190"
Cohesion: 0.20
Nodes (2): Convert SparseArray to a NumPy array.          Returns         -------         a, Cumulative sum of non-NA/null values.          When performing the cumulative su

### Community 191 - "Community 191"
Cohesion: 0.20
Nodes (8): generate_numba_apply_func(), generate_numba_ewm_func(), generate_numba_ewm_table_func(), generate_numba_table_func(), Generate a numba jitted function to apply window calculations table-wise.      F, Generate a numba jitted apply function specified by values from engine_kwargs., Generate a numba jitted ewm mean or sum function applied table wise specified, Generate a numba jitted ewm mean or sum function specified by values     from en

### Community 192 - "Community 192"
Cohesion: 0.31
Nodes (8): _nanquantile(), _nanquantile_1d(), quantile_compat(), quantile_with_mask(), Wrapper for np.quantile that skips missing values, specialized to     1-dimensio, Wrapper for np.quantile that skips missing values.      Parameters     ---------, Compute the quantiles of the given values for each quantile in `qs`.      Parame, Compute the quantiles of the given values for each quantile in `qs`.      Parame

### Community 193 - "Community 193"
Cohesion: 0.25
Nodes (8): compare_or_regex_search(), Methods used by Block.replace and related methods., Parameters     ----------     values : ArrayLike         Object dtype.     rx :, Decide whether to treat `to_replace` as a regular expression., Compare two array-like inputs of the same shape or two scalar values      Calls, # TODO: should use missing.mask_missing?, replace_regex(), should_use_regex()

### Community 194 - "Community 194"
Cohesion: 0.25
Nodes (9): _get_fill_value(), _get_values(), _na_ok_dtype(), nanall(), nanany(), return the correct fill value for the dtype of the values, Utility to get the values view, mask, dtype, dtype_max, and fill_value.      If, Check if any elements along an axis evaluate to True.      Parameters     ------ (+1 more)

### Community 195 - "Community 195"
Cohesion: 0.22
Nodes (2): ExtensionDtype that may be backed by more than one implementation., StorageExtensionDtype

### Community 196 - "Community 196"
Cohesion: 0.25
Nodes (6): Extend pandas with custom array types., Register an ExtensionType with pandas as class decorator.      This enables oper, Registry for dtype inference.      The registry allows one to map a string repr, Parameters         ----------         dtype : ExtensionDtype class, register_extension_dtype(), Registry

### Community 197 - "Community 197"
Cohesion: 0.31
Nodes (8): kleene_and(), kleene_or(), kleene_xor(), raise_for_nan(), Ops for masked arrays., Boolean ``and`` using Kleene logic.      Values are ``NA`` for ``NA & NA`` or ``, Boolean ``or`` using Kleene logic.      Values are NA where we have ``NA | NA``, Boolean ``xor`` using Kleene logic.      This is the same as ``or``, with the fo

### Community 198 - "Community 198"
Cohesion: 0.25
Nodes (8): ensure_list_vars(), lreshape(), melt(), Reshape wide-format data to long. Generalized inverse of DataFrame.pivot.      A, r"""     Unpivot a DataFrame from wide to long format.      Less flexible but mo, Unpivot a DataFrame from wide to long format, optionally leaving identifiers set, # TODO: anything else to catch?, wide_to_long()

### Community 199 - "Community 199"
Cohesion: 0.25
Nodes (7): _cross_merge(), _CrossMergeOperation, merge(), Merge DataFrame or named Series objects with a database-style join.      A named, Fast-path for cross (Cartesian product) merges.      Bypasses key extraction, fa, See merge.__doc__ with how='cross', _validate_operand()

### Community 200 - "Community 200"
Cohesion: 0.22
Nodes (5): _items_overlap_with_suffix(), _OrderedMerge, reindex along index and concat along columns., Suffixes type validation.      If two indices overlap, add suffixes to overlappi, _should_fill()

### Community 201 - "Community 201"
Cohesion: 0.25
Nodes (1): Get the location of the first fill value.          Returns         -------

### Community 202 - "Community 202"
Cohesion: 0.31
Nodes (8): _get_commit_hash(), _get_dependency_info(), _get_sys_info(), Use vendored versioneer code to get git hash, which handles     git worktree cor, Returns system information as a JSON serializable dictionary., Returns dependency information as a JSON serializable dictionary., Provide useful information, important for bug reports.      It comprises info ab, show_versions()

### Community 203 - "Community 203"
Cohesion: 0.22
Nodes (1): InfinityType

### Community 204 - "Community 204"
Cohesion: 0.22
Nodes (1): NegativeInfinityType

### Community 205 - "Community 205"
Cohesion: 0.39
Nodes (7): _cum_func(), cummax(), cummin(), cumprod(), cumsum(), masked_accumulations.py is for accumulation algorithms using a mask-based approa, Accumulations for 1D masked array.      We will modify values in place to replac

### Community 206 - "Community 206"
Cohesion: 0.32
Nodes (8): _get_counts_nanvar(), _maybe_get_mask(), nansem(), nanvar(), Compute the variance along given axis while ignoring NaNs      Parameters     --, Compute the standard error in the mean along given axis while ignoring NaNs, Compute a mask if and only if necessary.      This function will compute a mask, Get the count of non-null values along an axis, accounting     for degrees of fr

### Community 207 - "Community 207"
Cohesion: 0.25
Nodes (8): _get_empty_reduction_result(), nanmedian(), nanstd(), wrap our results if needed, Parameters     ----------     values : ndarray     axis : int, optional     skip, The result from a reduction on an empty ndarray.      Parameters     ----------, Compute the standard deviation along given axis while ignoring NaNs      Paramet, _wrap_results()

### Community 208 - "Community 208"
Cohesion: 0.25
Nodes (6): preprocess_weights(), process_sampling_size(), Randomly sample `size` indices in `np.arange(obj_len)`.      Parameters     ----, Process and validate the `weights` argument to `NDFrame.sample` and     `.GroupB, Process and validate the `n` and `frac` arguments to `NDFrame.sample` and     `., sample()

### Community 209 - "Community 209"
Cohesion: 0.36
Nodes (4): apply_tzinfo_offset(), convert_pydatetime_to_datetimestruct(), PyDateTimeToEpoch(), PyDateTimeToIso()

### Community 210 - "Community 210"
Cohesion: 0.25
Nodes (4): Check whether 'other' is equal to self.          By default, 'other' is consider, r"""         Construct this type from a string.          This is useful mainly f, Check if we match 'dtype'.          Parameters         ----------         dtype, Parameters         ----------         dtype : ExtensionDtype class or instance o

### Community 211 - "Community 211"
Cohesion: 0.25
Nodes (3): Parse an ODF Table into a list of lists, Return number of times this row was repeated         Repeating an empty row appe, Find and decode OpenDocument text:s tags that represent         a run length enc

### Community 212 - "Community 212"
Cohesion: 0.32
Nodes (7): get_console_size(), in_interactive_session(), in_ipython_frontend(), Internal module for console introspection, Return console size as tuple = (width, height).      Returns (None,None) in non-, Check if we're running in an interactive shell.      Returns     -------     boo, Check if we're inside an IPython zmq frontend.      Returns     -------     bool

### Community 213 - "Community 213"
Cohesion: 0.25
Nodes (7): generate_numba_agg_func(), generate_numba_transform_func(), Common utilities for Numba operations with groupby ops, Generate a numba jitted transform function specified by values from engine_kwarg, Validate user defined function for ops when using Numba with groupby ops.      T, Generate a numba jitted agg function specified by values from engine_kwargs., validate_udf()

### Community 214 - "Community 214"
Cohesion: 0.25
Nodes (4): IndexType, This will assume that only strings are in object dtype     index.     (you shoul, The type class for Index objects., typeof_index()

### Community 215 - "Community 215"
Cohesion: 0.32
Nodes (7): dispatch_fill_zeros(), _fill_zeros(), mask_zero_div_zero(), Missing data handling for arithmetic operations.  In particular, pandas conventi, Call _fill_zeros with the appropriate fill value depending on the operation,, If this is a reversed op, then flip x,y      If we have an integer value (or arr, Set results of  0 // 0 to np.nan, regardless of the dtypes     of the numerator

### Community 216 - "Community 216"
Cohesion: 0.25
Nodes (8): NpyArr_freeItemValue(), NpyArr_iterEnd(), NpyArr_iterNext(), NpyArr_iterNextItem(), NpyArrPassThru_iterEnd(), PdBlock_iterEnd(), PdBlock_iterNextItem(), PdBlockPassThru_iterEnd()

### Community 217 - "Community 217"
Cohesion: 0.25
Nodes (6): decompress_file(), Open a compressed file and return a file object.      Parameters     ----------, Context manager for temporarily setting a timezone.      Parameters     --------, Context manager to temporarily register a CSV dialect for parsing CSV.      Para, set_timezone(), with_csv_dialect()

### Community 218 - "Community 218"
Cohesion: 0.32
Nodes (7): _coerce_scalar_to_timedelta_type(), _convert_listlike(), timedelta support tools, Convert string 'r' to a timedelta object., Convert a list of objects to a timedelta index object., Convert argument to timedelta.      Timedeltas are absolute differences in times, to_timedelta()

### Community 219 - "Community 219"
Cohesion: 0.25
Nodes (7): parametrize_fixture_doc(), This module provides decorator functions which can be applied to test objects in, Intended for use as a decorator for parametrized fixture,     this function will, Skip a test if a package is installed.      Parameters     ----------     packag, Generic function to help skip tests when required packages are not     present o, skip_if_installed(), skip_if_no()

### Community 220 - "Community 220"
Cohesion: 0.43
Nodes (6): _cum_func(), cummax(), cummin(), cumsum(), datetimelke_accumulations.py is for accumulations of datetimelike extension arra, Accumulations for 1D datetimelike arrays.      Parameters     ----------     fun

### Community 222 - "Community 222"
Cohesion: 0.33
Nodes (4): NoNewAttributesMixin, Base and utility classes for pandas objects., Mixin which prevents adding new attributes.      Prevents additional attributes, Prevents setting additional attributes.

### Community 223 - "Community 223"
Cohesion: 0.29
Nodes (7): _get_counts(), _get_dtype_max(), nanmean(), nansum(), Get the count of non-null values along an axis      Parameters     ----------, Sum the elements along an axis ignoring NaNs      Parameters     ----------, Compute the mean of the element along an axis ignoring NaNs      Parameters

### Community 224 - "Community 224"
Cohesion: 0.29
Nodes (6): Pandas5Warning, PandasPendingDeprecationWarning, Warning raised for an upcoming change that is a PendingDeprecationWarning., Warning raised for an upcoming change that will be enforced in pandas 5.0., Version where change will be enforced., PendingDeprecationWarning

### Community 226 - "Community 226"
Cohesion: 0.29
Nodes (4): GroupByPositionalSelector, Return positional selection for each group.      ``groupby._positional_selector[, Select by positional index per group.          Implements GroupBy._positional_se, Return positional selection for each group.          ``groupby._positional_selec

### Community 227 - "Community 227"
Cohesion: 0.48
Nodes (6): add_sum(), grouped_kahan_sum(), grouped_sum(), Numba 1D sum kernels that can be shared by * Dataframe / Series * groupby * roll, remove_sum(), sliding_sum()

### Community 228 - "Community 228"
Cohesion: 0.33
Nodes (2): murmur2_32_32to32(), murmur2_64to32()

### Community 229 - "Community 229"
Cohesion: 0.29
Nodes (6): create_iter_data_given_by(), Internal function to reformat y given `by` is applied or not for hist plot., Create data for iteration given `by` is assigned or not, and it is only     used, Internal function to group data, and reassign multiindex column names onto the, reconstruct_data_with_by(), reformat_hist_y_given_by()

### Community 230 - "Community 230"
Cohesion: 0.29
Nodes (4): generate_shared_aggregator(), # TODO: Preserve complex dtypes, Generate a Numba function that loops over the columns 2D object and applies, # TODO: Optimize this

### Community 231 - "Community 231"
Cohesion: 0.29
Nodes (3): The type class for Series objects., SeriesType, typeof_series()

### Community 232 - "Community 232"
Cohesion: 0.29
Nodes (6): Pickle an object and then read it again.      Parameters     ----------     obj, Write an object to file specified by a pathlib.Path and read it back      Parame, Write data to a compressed file.      Parameters     ----------     compression, round_trip_pathlib(), round_trip_pickle(), write_to_compressed()

### Community 233 - "Community 233"
Cohesion: 0.29
Nodes (6): find_stack_level(), Rewrite the message of an exception., Find the first place in the stack that is not inside pandas     (tests notwithst, Rewrite the message of a warning.      Parameters     ----------     target_mess, rewrite_exception(), rewrite_warning()

### Community 234 - "Community 234"
Cohesion: 0.40
Nodes (2): DictWrapper, provide attribute-style access to a nested dict

### Community 235 - "Community 235"
Cohesion: 0.33
Nodes (1): pandas._config is considered explicitly upstream of everything else in pandas, s

### Community 236 - "Community 236"
Cohesion: 0.33
Nodes (6): check_below_min_count(), _maybe_null_out(), nanprod(), Parameters     ----------     values : ndarray[dtype]     axis : int, optional, Returns     -------     Dtype         The product of all elements on a given axi, Check for the `min_count` keyword. Returns True if below `min_count` (when     m

### Community 237 - "Community 237"
Cohesion: 0.40
Nodes (6): _maybe_arg_null_out(), _maybe_fix_arg_at_na(), nanargmax(), nanargmin(), Parameters     ----------     values : ndarray     axis : int, optional     skip, Parameters     ----------     values : ndarray     axis : int, optional     skip

### Community 238 - "Community 238"
Cohesion: 0.40
Nodes (2): compare_format(), parse_iso_8601_datetime()

### Community 239 - "Community 239"
Cohesion: 0.33
Nodes (5): NumExprClobberingError, Exception raised when trying to use a built-in numexpr name as a variable name., Exception raised by ``query`` or ``eval`` when using an undefined variable name., UndefinedVariableError, NameError

### Community 240 - "Community 240"
Cohesion: 0.33
Nodes (5): PyperclipException, PyperclipWindowsException, Exception raised when clipboard functionality is unsupported.      Raised by ``t, Exception raised when clipboard functionality is unsupported by Windows.      Ac, RuntimeError

### Community 241 - "Community 241"
Cohesion: 0.33
Nodes (2): Convert 0-based column index to Excel column name.          Parameters         -, writer : path-like, file-like, or ExcelWriter object             File path or ex

### Community 242 - "Community 242"
Cohesion: 0.33
Nodes (5): Module for formatting output data in HTML., # TODO: Refactor to remove code duplication with code, # TODO: Refactor to use _get_column_name_list from, # TODO: Refactor to remove code duplication with code block, # TODO: Refactor to use _get_column_name_list from

### Community 243 - "Community 243"
Cohesion: 0.33
Nodes (5): _inherit_from_data(), inherit_names(), Shared methods for Index subclasses backed by ExtensionArray., Class decorator to pin attributes from an ExtensionArray to an Index subclass., Make an alias for a method of the underlying ExtensionArray.      Parameters

### Community 244 - "Community 244"
Cohesion: 0.47
Nodes (4): add_mean(), Numba 1D mean kernels that can be shared by * Dataframe / Series * groupby * rol, remove_mean(), sliding_mean()

### Community 245 - "Community 245"
Cohesion: 0.40
Nodes (4): bisect_left(), Numba 1D min/max kernels that can be shared by * Dataframe / Series * groupby *, Same as https://docs.python.org/3/library/bisect.html; not in numba yet!, sliding_min_max()

### Community 246 - "Community 246"
Cohesion: 0.53
Nodes (5): add_var(), grouped_var(), Numba 1D var kernels that can be shared by * Dataframe / Series * groupby * roll, remove_var(), sliding_var()

### Community 247 - "Community 247"
Cohesion: 0.33
Nodes (5): invalid_comparison(), make_invalid_op(), Templates for invalid operations., If a comparison has mismatched types and is not necessarily meaningful,     foll, Return a binary method that always raises a TypeError.      Parameters     -----

### Community 248 - "Community 248"
Cohesion: 0.40
Nodes (2): floatify(), to_double()

### Community 249 - "Community 249"
Cohesion: 0.40
Nodes (3): _concatenate_chunks(), _filter_usecols(), Concatenate chunks of data read with low_memory=True.      The tricky part is ha

### Community 250 - "Community 250"
Cohesion: 0.40
Nodes (5): from_dummies(), get_dummies(), _get_dummies_1d(), Create a categorical ``DataFrame`` from a ``DataFrame`` of dummy variables., Convert categorical variable into dummy/indicator variables.      Each variable

### Community 251 - "Community 251"
Cohesion: 0.33
Nodes (3): _left_join_on_index(), Create a join index by rearranging one index to match another          Parameter, Handle anti join by returning the correct join index and indexers          Param

### Community 252 - "Community 252"
Cohesion: 0.33
Nodes (3): Max of array values, ignoring NA values if specified.          Parameters, Min of array values, ignoring NA values if specified.          Parameters, Min/max of non-NA/null values          Parameters         ----------         kin

### Community 253 - "Community 253"
Cohesion: 0.40
Nodes (4): ensure_decoded(), If we have bytes, decode them to unicode., Wrapper around numpy.result_type which overcomes the NPY_MAXARGS (32)     argume, result_type_many()

### Community 254 - "Community 254"
Cohesion: 0.40
Nodes (2): Return number of unique elements in the object.          Excludes NA values by d, Return True if values in the object are unique.          This property checks wh

### Community 255 - "Community 255"
Cohesion: 0.40
Nodes (2): Construct a SparseDtype from a string form.          Parameters         --------, Parse a string to get the subtype          Parameters         ----------

### Community 256 - "Community 256"
Cohesion: 0.40
Nodes (2): return a list of tuples of start, stop, step, Return a list of tuples of the (attr, formatted_value)

### Community 257 - "Community 257"
Cohesion: 0.40
Nodes (2): The minimum value of the RangeIndex, The maximum value of the RangeIndex

### Community 258 - "Community 258"
Cohesion: 0.40
Nodes (4): Attempt to write text representation of object to the system clipboard     The c, r"""     Read text from clipboard and pass to :func:`~pandas.read_csv`.      Par, read_clipboard(), to_clipboard()

### Community 259 - "Community 259"
Cohesion: 0.40
Nodes (4): Write a DataFrame to an Apache Iceberg table.      .. versionadded:: 3.0.0, Read an Apache Iceberg table into a pandas DataFrame.      .. versionadded:: 3.0, read_iceberg(), to_iceberg()

### Community 260 - "Community 260"
Cohesion: 0.50
Nodes (4): create_data_for_split(), Convert the DataFrame to a dictionary.      The type of the key-value pairs can, Simple helper method to create data for to ``to_dict(orient="split")``     to cr, to_dict()

### Community 261 - "Community 261"
Cohesion: 0.40
Nodes (3): get_obj(), Helpers for sharing tests between DataFrame/Series, For sharing tests using frame_or_series, either return the DataFrame     unchang

### Community 262 - "Community 262"
Cohesion: 0.50
Nodes (3): flex_binary_moment(), prep_binary(), Common utility functions for rolling operations

### Community 263 - "Community 263"
Cohesion: 0.50
Nodes (3): detect_console_encoding(), Unopinionated display configuration., Try to find the most capable encoding supported by the console.     slightly mod

### Community 264 - "Community 264"
Cohesion: 0.50
Nodes (4): is_null_slice(), is_true_slices(), We have a null slice., Find non-trivial slices in "line": yields a bool.

### Community 265 - "Community 265"
Cohesion: 0.50
Nodes (1): disallow

### Community 267 - "Community 267"
Cohesion: 0.50
Nodes (2): Return the array type associated with this dtype.          Returns         -----, Construct an ExtensionArray of this dtype with the given shape.          Analogo

### Community 268 - "Community 268"
Cohesion: 0.50
Nodes (1): Construct the MaskedDtype corresponding to the given numpy dtype.

### Community 269 - "Community 269"
Cohesion: 0.50
Nodes (2): Parameters         ----------         other : Any         op : callable that acc, The value of the `step` parameter (``1`` if this was not supplied).          The

### Community 270 - "Community 270"
Cohesion: 0.50
Nodes (2): Check if other range is contained in self, Form the union of two Index objects and sorts if possible          Parameters

### Community 271 - "Community 271"
Cohesion: 0.50
Nodes (2): IlocType, typeof_iloc()

### Community 273 - "Community 273"
Cohesion: 0.83
Nodes (3): from_chars_to_status(), pd_strtoll(), pd_strtoull()

### Community 274 - "Community 274"
Cohesion: 0.50
Nodes (4): get_attr_length(), get_sub_attr(), NpyArr_iterBegin(), PdBlock_iterBegin()

### Community 275 - "Community 275"
Cohesion: 0.50
Nodes (4): _groupby_and_merge(), merge_ordered(), groupby & merge; we are always performing a left-by type operation      Paramete, Perform a merge for ordered data with optional filling/interpolation.      Desig

### Community 277 - "Community 277"
Cohesion: 0.50
Nodes (3): Entrypoint for testing from the top-level namespace., Run the pandas test suite using pytest.      By default, runs with the marks -m, test()

### Community 278 - "Community 278"
Cohesion: 0.67
Nodes (2): pyarrow_array_to_numpy_and_mask(), Convert a primitive pyarrow.Array to a numpy array and boolean mask based     on

### Community 279 - "Community 279"
Cohesion: 0.67
Nodes (1): search order for local (i.e., @variable) variables:          scope, key_variable

### Community 282 - "Community 282"
Cohesion: 0.67
Nodes (1): Create a SparseArray from a scipy.sparse matrix.          Parameters         ---

### Community 284 - "Community 284"
Cohesion: 1.00
Nodes (1): core.array_algos is for algorithms that operate on ndarray and ExtensionArray. T

### Community 285 - "Community 285"
Cohesion: 1.00
Nodes (1): All of pandas' ExtensionArrays.  See :ref:`extending.extension-types` for more.

### Community 286 - "Community 286"
Cohesion: 1.00
Nodes (1): _constants ======  Constants relevant for the Python implementation.

### Community 287 - "Community 287"
Cohesion: 1.00
Nodes (1): config for datetime formatting

### Community 288 - "Community 288"
Cohesion: 1.00
Nodes (1): Return an iterator of the values.          These are each a scalar type, which i

### Community 289 - "Community 289"
Cohesion: 1.00
Nodes (1): An internal function that maps values using the input         correspondence (wh

### Community 290 - "Community 290"
Cohesion: 1.00
Nodes (1): Memory usage of the values.          Parameters         ----------         deep

### Community 291 - "Community 291"
Cohesion: 1.00
Nodes (1): Return the number of bytes in the underlying data.          Includes only the me

### Community 292 - "Community 292"
Cohesion: 1.00
Nodes (1): Number of dimensions of the underlying data, by definition 1.          Series an

### Community 293 - "Community 293"
Cohesion: 1.00
Nodes (1): Find indices where elements should be inserted to maintain order.          Find

### Community 294 - "Community 294"
Cohesion: 1.00
Nodes (1): Return a tuple of the shape of the underlying data.          For a Series this i

### Community 295 - "Community 295"
Cohesion: 1.00
Nodes (1): Return the number of elements in the underlying data.          For a Series or I

### Community 296 - "Community 296"
Cohesion: 1.00
Nodes (1): A NumPy ndarray representing the values in this Series or Index.          This m

### Community 297 - "Community 297"
Cohesion: 1.00
Nodes (1): Return a list of the values.          These are each a scalar type, which is a P

### Community 298 - "Community 298"
Cohesion: 1.00
Nodes (1): Return the transpose, which is by definition self.          Returns         ----

### Community 299 - "Community 299"
Cohesion: 1.00
Nodes (1): Return a Series containing counts of unique values.          The resulting objec

### Community 300 - "Community 300"
Cohesion: 1.00
Nodes (1): Create an expression that evaluates :meth:`Series.case_when` in a DataFrame

### Community 301 - "Community 301"
Cohesion: 1.00
Nodes (1): Whether this object allows duplicate labels.          Setting ``allows_duplicate

### Community 302 - "Community 302"
Cohesion: 1.00
Nodes (2): _na_for_min_count(), Return the missing value for `values`.      Parameters     ----------     values

### Community 303 - "Community 303"
Cohesion: 1.00
Nodes (2): nankurt(), Compute the sample excess kurtosis      The statistic computed here is the adjus

### Community 304 - "Community 304"
Cohesion: 1.00
Nodes (2): nanskew(), Compute the sample skewness.      The statistic computed here is the adjusted Fi

### Community 305 - "Community 305"
Cohesion: 1.00
Nodes (1): Can arrays with this dtype be modified with __setitem__? If not, return

### Community 306 - "Community 306"
Cohesion: 1.00
Nodes (1): Whether columns with this dtype should be considered numeric.          By defaul

### Community 307 - "Community 307"
Cohesion: 1.00
Nodes (1): A character code (one of 'biufcmMOSUV'), default 'O'          This should match

### Community 308 - "Community 308"
Cohesion: 1.00
Nodes (1): Default NA value to use for this type.          This is used in e.g. ExtensionAr

### Community 309 - "Community 309"
Cohesion: 1.00
Nodes (1): A string identifying the data type.          Will be used for display in, e.g. `

### Community 310 - "Community 310"
Cohesion: 1.00
Nodes (1): Ordered list of field names, or None if there are no fields.          This is fo

### Community 311 - "Community 311"
Cohesion: 1.00
Nodes (1): Do ExtensionArrays with this dtype support 2D arrays?          Historically Exte

### Community 312 - "Community 312"
Cohesion: 1.00
Nodes (1): Public API for extending pandas objects.

### Community 313 - "Community 313"
Cohesion: 1.00
Nodes (1): Number of columns to be summarized.

### Community 314 - "Community 314"
Cohesion: 1.00
Nodes (1): Dtypes.          Returns         -------         dtypes             Dtype of eac

### Community 315 - "Community 315"
Cohesion: 1.00
Nodes (1): Column names.          Returns         -------         ids : Index             D

### Community 316 - "Community 316"
Cohesion: 1.00
Nodes (1): Sequence of non-null counts for all columns or column (if series).

### Community 317 - "Community 317"
Cohesion: 1.00
Nodes (1): Computes the bounds of a window.          Parameters         ----------

### Community 318 - "Community 318"
Cohesion: 1.00
Nodes (1): Returns a FrozenList with elements from other removed from self.          Parame

### Community 319 - "Community 319"
Cohesion: 1.00
Nodes (1): This method will not function because object is immutable.

### Community 320 - "Community 320"
Cohesion: 1.00
Nodes (1): Returns a FrozenList with other concatenated to the end of self.          Parame

### Community 321 - "Community 321"
Cohesion: 1.00
Nodes (1): Returns the indices that would sort the index and its         underlying data.

### Community 322 - "Community 322"
Cohesion: 1.00
Nodes (1): An int array that for performance reasons is created only when needed.

### Community 323 - "Community 323"
Cohesion: 1.00
Nodes (1): Get integer location for requested label.          Parameters         ----------

### Community 324 - "Community 324"
Cohesion: 1.00
Nodes (1): return if the index has unique values

### Community 325 - "Community 325"
Cohesion: 1.00
Nodes (1): Return an iterator of the values.          Returns         -------         itera

### Community 326 - "Community 326"
Cohesion: 1.00
Nodes (1): return the length of the RangeIndex

### Community 327 - "Community 327"
Cohesion: 1.00
Nodes (1): Memory usage of my values          Parameters         ----------         deep :

### Community 328 - "Community 328"
Cohesion: 1.00
Nodes (1): Return the number of bytes in the underlying data.

### Community 329 - "Community 329"
Cohesion: 1.00
Nodes (1): Should an integer key be treated as positional?

### Community 330 - "Community 330"
Cohesion: 1.00
Nodes (1): The value of the `start` parameter (``0`` if this was not supplied).          Th

### Community 331 - "Community 331"
Cohesion: 1.00
Nodes (1): The value of the `stop` parameter.          This property returns the `stop` val

### Community 332 - "Community 332"
Cohesion: 1.00
Nodes (1): If the dtype is categorical, there are two options:         - There are only val

### Community 333 - "Community 333"
Cohesion: 1.00
Nodes (1): Return an iterator yielding the chunks.         See `DataFrame.get_chunks` for d

### Community 334 - "Community 334"
Cohesion: 1.00
Nodes (1): Note: doesn't deal with extension arrays yet, just assume a regular         Seri

### Community 335 - "Community 335"
Cohesion: 1.00
Nodes (1): Store specific metadata of the column.

### Community 336 - "Community 336"
Cohesion: 1.00
Nodes (1): Return the number of chunks the column consists of.

### Community 337 - "Community 337"
Cohesion: 1.00
Nodes (1): Offset of first element. Always zero.

### Community 338 - "Community 338"
Cohesion: 1.00
Nodes (1): Size of the column, in elements.

### Community 339 - "Community 339"
Cohesion: 1.00
Nodes (1): Return an iterator yielding the chunks.

### Community 340 - "Community 340"
Cohesion: 1.00
Nodes (1): Constructor - an instance of this (private) class is returned from         `pd.D

### Community 341 - "Community 341"
Cohesion: 1.00
Nodes (1): Return an iterator yielding the column names.

### Community 342 - "Community 342"
Cohesion: 1.00
Nodes (1): Construct a new interchange object, potentially changing the parameters.

### Community 343 - "Community 343"
Cohesion: 1.00
Nodes (1): Return an iterator yielding the chunks.          By default (None), yields the c

### Community 344 - "Community 344"
Cohesion: 1.00
Nodes (1): Return the column whose name is the indicated name.

### Community 345 - "Community 345"
Cohesion: 1.00
Nodes (1): Return the column at the indicated position.

### Community 346 - "Community 346"
Cohesion: 1.00
Nodes (1): Return an iterator yielding the columns.

### Community 347 - "Community 347"
Cohesion: 1.00
Nodes (1): The metadata for the data frame, as a dictionary with string keys. The         c

### Community 348 - "Community 348"
Cohesion: 1.00
Nodes (1): Return the number of chunks the DataFrame consists of.

### Community 349 - "Community 349"
Cohesion: 1.00
Nodes (1): Return the number of columns in the DataFrame.

### Community 350 - "Community 350"
Cohesion: 1.00
Nodes (1): Return the number of rows in the DataFrame, if available.

### Community 351 - "Community 351"
Cohesion: 1.00
Nodes (1): Create a new DataFrame by selecting a subset of columns by name.

### Community 352 - "Community 352"
Cohesion: 1.00
Nodes (1): Create a new DataFrame by selecting a subset of columns by index.

### Community 353 - "Community 353"
Cohesion: 1.00
Nodes (1): Public API for DataFrame interchange protocol.

### Community 355 - "Community 355"
Cohesion: 1.00
Nodes (2): box_index(), Convert a native index structure to an Index object.      If our native index is

### Community 356 - "Community 356"
Cohesion: 1.00
Nodes (2): box_series(), Convert a native series structure to a Series object.

### Community 357 - "Community 357"
Cohesion: 1.00
Nodes (1): ILocModel

### Community 358 - "Community 358"
Cohesion: 1.00
Nodes (1): IndexModel

### Community 359 - "Community 359"
Cohesion: 1.00
Nodes (2): maybe_cast_str_impl(), Converts numba UnicodeCharSeq (numpy string scalar) -> unicode type (string).

### Community 360 - "Community 360"
Cohesion: 1.00
Nodes (2): Convert an Index object to a native structure.      Note: Object dtype is not al, unbox_index()

### Community 361 - "Community 361"
Cohesion: 1.00
Nodes (2): Convert a Series object to a native structure., unbox_series()

### Community 362 - "Community 362"
Cohesion: 1.00
Nodes (1): SeriesModel

### Community 363 - "Community 363"
Cohesion: 1.00
Nodes (1): support numpy compatibility across versions

### Community 364 - "Community 364"
Cohesion: 1.00
Nodes (1): Arithmetic operations for PandasObjects  This is not a public API.

### Community 367 - "Community 367"
Cohesion: 1.00
Nodes (1): The kind of sparse index for this array. One of {'integer', 'block'}.

### Community 368 - "Community 368"
Cohesion: 1.00
Nodes (1): The percent of non- ``fill_value`` points, as decimal.          This is calculat

### Community 369 - "Community 369"
Cohesion: 1.00
Nodes (1): Returns a Series containing counts of unique values.          Parameters

### Community 370 - "Community 370"
Cohesion: 1.00
Nodes (1): Implementation of pandas.Series.str and its interface.  * strings.accessor.Strin

### Community 371 - "Community 371"
Cohesion: 1.00
Nodes (1): Hypothesis data generator helpers.

### Community 372 - "Community 372"
Cohesion: 1.00
Nodes (1): Public testing utility functions.

## Knowledge Gaps
- **657 isolated node(s):** `pandas._config is considered explicitly upstream of everything else in pandas, s`, `The config module holds package-wide configurables and provides a uniform API fo`, `Exception raised for pandas.options.      Backwards compatible with KeyError che`, `Retrieve the value of the specified option.      This method allows users to que`, `Set the value of the specified option or options.      This method allows fine-g` (+652 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 13`** (1 nodes): `NDFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (1 nodes): `BaseMaskedArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (2 nodes): `BaseBlockManager`, `_preprocess_slice_or_indexer()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (2 nodes): `DatetimeIndex`, `_time_to_micros()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 70`** (2 nodes): `ArrowStringArrayMixin`, `Determine if regex pattern contains features not supported by RE2 / pyarrow.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 71`** (1 nodes): `DatetimeTimedeltaMixin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 74`** (2 nodes): `Expression`, `Class representing a deferred column.      This is not meant to be instantiated`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 107`** (1 nodes): `SingleBlockManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 140`** (1 nodes): `Get Addition of DataFrame and other, column-wise.          Equivalent to ``DataF`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 153`** (2 nodes): `BarhPlot`, `BarPlot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 158`** (2 nodes): `AreaPlot`, `LinePlot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 160`** (1 nodes): `Reversed Operations not available in the stdlib operator module. Defining these`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 173`** (2 nodes): `module_clear()`, `module_free()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 189`** (2 nodes): `_get_marker_compat()`, `scatter_matrix()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (2 nodes): `Convert SparseArray to a NumPy array.          Returns         -------         a`, `Cumulative sum of non-NA/null values.          When performing the cumulative su`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 195`** (2 nodes): `ExtensionDtype that may be backed by more than one implementation.`, `StorageExtensionDtype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 201`** (1 nodes): `Get the location of the first fill value.          Returns         -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 203`** (1 nodes): `InfinityType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 204`** (1 nodes): `NegativeInfinityType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 228`** (2 nodes): `murmur2_32_32to32()`, `murmur2_64to32()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 234`** (2 nodes): `DictWrapper`, `provide attribute-style access to a nested dict`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 235`** (1 nodes): `pandas._config is considered explicitly upstream of everything else in pandas, s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 238`** (2 nodes): `compare_format()`, `parse_iso_8601_datetime()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 241`** (2 nodes): `Convert 0-based column index to Excel column name.          Parameters         -`, `writer : path-like, file-like, or ExcelWriter object             File path or ex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 248`** (2 nodes): `floatify()`, `to_double()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 254`** (2 nodes): `Return number of unique elements in the object.          Excludes NA values by d`, `Return True if values in the object are unique.          This property checks wh`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 255`** (2 nodes): `Construct a SparseDtype from a string form.          Parameters         --------`, `Parse a string to get the subtype          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 256`** (2 nodes): `return a list of tuples of start, stop, step`, `Return a list of tuples of the (attr, formatted_value)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 257`** (2 nodes): `The minimum value of the RangeIndex`, `The maximum value of the RangeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 265`** (1 nodes): `disallow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 267`** (2 nodes): `Return the array type associated with this dtype.          Returns         -----`, `Construct an ExtensionArray of this dtype with the given shape.          Analogo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 268`** (1 nodes): `Construct the MaskedDtype corresponding to the given numpy dtype.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 269`** (2 nodes): `Parameters         ----------         other : Any         op : callable that acc`, `The value of the `step` parameter (``1`` if this was not supplied).          The`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 270`** (2 nodes): `Check if other range is contained in self`, `Form the union of two Index objects and sorts if possible          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 271`** (2 nodes): `IlocType`, `typeof_iloc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 278`** (2 nodes): `pyarrow_array_to_numpy_and_mask()`, `Convert a primitive pyarrow.Array to a numpy array and boolean mask based     on`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 279`** (1 nodes): `search order for local (i.e., @variable) variables:          scope, key_variable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 282`** (1 nodes): `Create a SparseArray from a scipy.sparse matrix.          Parameters         ---`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 284`** (1 nodes): `core.array_algos is for algorithms that operate on ndarray and ExtensionArray. T`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 285`** (1 nodes): `All of pandas' ExtensionArrays.  See :ref:`extending.extension-types` for more.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 286`** (1 nodes): `_constants ======  Constants relevant for the Python implementation.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 287`** (1 nodes): `config for datetime formatting`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 288`** (1 nodes): `Return an iterator of the values.          These are each a scalar type, which i`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 289`** (1 nodes): `An internal function that maps values using the input         correspondence (wh`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 290`** (1 nodes): `Memory usage of the values.          Parameters         ----------         deep`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 291`** (1 nodes): `Return the number of bytes in the underlying data.          Includes only the me`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 292`** (1 nodes): `Number of dimensions of the underlying data, by definition 1.          Series an`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 293`** (1 nodes): `Find indices where elements should be inserted to maintain order.          Find`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 294`** (1 nodes): `Return a tuple of the shape of the underlying data.          For a Series this i`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 295`** (1 nodes): `Return the number of elements in the underlying data.          For a Series or I`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 296`** (1 nodes): `A NumPy ndarray representing the values in this Series or Index.          This m`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 297`** (1 nodes): `Return a list of the values.          These are each a scalar type, which is a P`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 298`** (1 nodes): `Return the transpose, which is by definition self.          Returns         ----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 299`** (1 nodes): `Return a Series containing counts of unique values.          The resulting objec`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 300`** (1 nodes): `Create an expression that evaluates :meth:`Series.case_when` in a DataFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 301`** (1 nodes): `Whether this object allows duplicate labels.          Setting ``allows_duplicate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 302`** (2 nodes): `_na_for_min_count()`, `Return the missing value for `values`.      Parameters     ----------     values`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 303`** (2 nodes): `nankurt()`, `Compute the sample excess kurtosis      The statistic computed here is the adjus`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 304`** (2 nodes): `nanskew()`, `Compute the sample skewness.      The statistic computed here is the adjusted Fi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 305`** (1 nodes): `Can arrays with this dtype be modified with __setitem__? If not, return`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 306`** (1 nodes): `Whether columns with this dtype should be considered numeric.          By defaul`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 307`** (1 nodes): `A character code (one of 'biufcmMOSUV'), default 'O'          This should match`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 308`** (1 nodes): `Default NA value to use for this type.          This is used in e.g. ExtensionAr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 309`** (1 nodes): `A string identifying the data type.          Will be used for display in, e.g. ``
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 310`** (1 nodes): `Ordered list of field names, or None if there are no fields.          This is fo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 311`** (1 nodes): `Do ExtensionArrays with this dtype support 2D arrays?          Historically Exte`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 312`** (1 nodes): `Public API for extending pandas objects.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 313`** (1 nodes): `Number of columns to be summarized.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 314`** (1 nodes): `Dtypes.          Returns         -------         dtypes             Dtype of eac`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 315`** (1 nodes): `Column names.          Returns         -------         ids : Index             D`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 316`** (1 nodes): `Sequence of non-null counts for all columns or column (if series).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 317`** (1 nodes): `Computes the bounds of a window.          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 318`** (1 nodes): `Returns a FrozenList with elements from other removed from self.          Parame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 319`** (1 nodes): `This method will not function because object is immutable.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 320`** (1 nodes): `Returns a FrozenList with other concatenated to the end of self.          Parame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 321`** (1 nodes): `Returns the indices that would sort the index and its         underlying data.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 322`** (1 nodes): `An int array that for performance reasons is created only when needed.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 323`** (1 nodes): `Get integer location for requested label.          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 324`** (1 nodes): `return if the index has unique values`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 325`** (1 nodes): `Return an iterator of the values.          Returns         -------         itera`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 326`** (1 nodes): `return the length of the RangeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 327`** (1 nodes): `Memory usage of my values          Parameters         ----------         deep :`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 328`** (1 nodes): `Return the number of bytes in the underlying data.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 329`** (1 nodes): `Should an integer key be treated as positional?`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 330`** (1 nodes): `The value of the `start` parameter (``0`` if this was not supplied).          Th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 331`** (1 nodes): `The value of the `stop` parameter.          This property returns the `stop` val`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 332`** (1 nodes): `If the dtype is categorical, there are two options:         - There are only val`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 333`** (1 nodes): `Return an iterator yielding the chunks.         See `DataFrame.get_chunks` for d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 334`** (1 nodes): `Note: doesn't deal with extension arrays yet, just assume a regular         Seri`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 335`** (1 nodes): `Store specific metadata of the column.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 336`** (1 nodes): `Return the number of chunks the column consists of.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 337`** (1 nodes): `Offset of first element. Always zero.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 338`** (1 nodes): `Size of the column, in elements.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 339`** (1 nodes): `Return an iterator yielding the chunks.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 340`** (1 nodes): `Constructor - an instance of this (private) class is returned from         `pd.D`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 341`** (1 nodes): `Return an iterator yielding the column names.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 342`** (1 nodes): `Construct a new interchange object, potentially changing the parameters.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 343`** (1 nodes): `Return an iterator yielding the chunks.          By default (None), yields the c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 344`** (1 nodes): `Return the column whose name is the indicated name.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 345`** (1 nodes): `Return the column at the indicated position.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 346`** (1 nodes): `Return an iterator yielding the columns.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 347`** (1 nodes): `The metadata for the data frame, as a dictionary with string keys. The         c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 348`** (1 nodes): `Return the number of chunks the DataFrame consists of.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 349`** (1 nodes): `Return the number of columns in the DataFrame.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 350`** (1 nodes): `Return the number of rows in the DataFrame, if available.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 351`** (1 nodes): `Create a new DataFrame by selecting a subset of columns by name.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 352`** (1 nodes): `Create a new DataFrame by selecting a subset of columns by index.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 353`** (1 nodes): `Public API for DataFrame interchange protocol.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 355`** (2 nodes): `box_index()`, `Convert a native index structure to an Index object.      If our native index is`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 356`** (2 nodes): `box_series()`, `Convert a native series structure to a Series object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 357`** (1 nodes): `ILocModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 358`** (1 nodes): `IndexModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 359`** (2 nodes): `maybe_cast_str_impl()`, `Converts numba UnicodeCharSeq (numpy string scalar) -> unicode type (string).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 360`** (2 nodes): `Convert an Index object to a native structure.      Note: Object dtype is not al`, `unbox_index()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 361`** (2 nodes): `Convert a Series object to a native structure.`, `unbox_series()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 362`** (1 nodes): `SeriesModel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 363`** (1 nodes): `support numpy compatibility across versions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 364`** (1 nodes): `Arithmetic operations for PandasObjects  This is not a public API.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 367`** (1 nodes): `The kind of sparse index for this array. One of {'integer', 'block'}.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 368`** (1 nodes): `The percent of non- ``fill_value`` points, as decimal.          This is calculat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 369`** (1 nodes): `Returns a Series containing counts of unique values.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 370`** (1 nodes): `Implementation of pandas.Series.str and its interface.  * strings.accessor.Strin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 371`** (1 nodes): `Hypothesis data generator helpers.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 372`** (1 nodes): `Public testing utility functions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DatetimeTZDtype` connect `Community 1` to `Community 7`, `Community 33`, `Community 26`, `Community 9`, `Community 184`, `Community 46`, `Community 23`, `Community 50`, `Community 6`, `Community 11`, `Community 5`, `Community 13`, `Community 14`, `Community 37`, `Community 31`, `Community 38`, `Community 22`, `Community 12`, `Community 3`, `Community 78`, `Community 16`, `Community 71`, `Community 58`, `Community 19`, `Community 53`, `Community 44`, `Community 60`, `Community 107`, `Community 0`, `Community 17`, `Community 25`, `Community 181`, `Community 199`, `Community 124`, `Community 200`, `Community 108`, `Community 251`, `Community 275`, `Community 119`, `Community 148`, `Community 125`, `Community 75`, `Community 190`, `Community 252`, `Community 282`, `Community 367`, `Community 368`, `Community 201`, `Community 369`, `Community 157`, `Community 100`, `Community 85`, `Community 56`?**
  _High betweenness centrality (0.149) - this node is a cross-community bridge._
- **Why does `CategoricalDtype` connect `Community 7` to `Community 4`, `Community 2`, `Community 33`, `Community 19`, `Community 54`, `Community 11`, `Community 5`, `Community 1`, `Community 31`, `Community 38`, `Community 188`, `Community 22`, `Community 14`, `Community 12`, `Community 3`, `Community 20`, `Community 15`, `Community 66`, `Community 78`, `Community 16`, `Community 6`, `Community 10`, `Community 71`, `Community 98`, `Community 151`, `Community 44`, `Community 60`, `Community 107`, `Community 0`, `Community 8`, `Community 72`, `Community 133`, `Community 61`, `Community 158`, `Community 153`, `Community 130`, `Community 51`, `Community 88`, `Community 29`, `Community 249`, `Community 77`, `Community 250`, `Community 181`, `Community 199`, `Community 124`, `Community 200`, `Community 108`, `Community 251`, `Community 275`, `Community 119`, `Community 18`, `Community 176`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Why does `DataFrame` connect `Community 11` to `Community 5`, `Community 167`, `Community 140`, `Community 9`, `Community 23`, `Community 3`, `Community 2`, `Community 7`, `Community 1`, `Community 6`, `Community 10`, `Community 106`, `Community 8`, `Community 14`, `Community 49`, `Community 39`, `Community 68`, `Community 35`, `Community 114`, `Community 21`, `Community 314`, `Community 315`, `Community 313`, `Community 316`, `Community 24`, `Community 20`, `Community 15`, `Community 28`, `Community 66`, `Community 32`, `Community 97`, `Community 72`, `Community 133`, `Community 61`, `Community 29`, `Community 250`, `Community 89`, `Community 18`, `Community 12`, `Community 157`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Are the 1682 inferred relationships involving `DatetimeTZDtype` (e.g. with `DatelikeOps` and `DatetimeLikeArrayMixin`) actually correct?**
  _`DatetimeTZDtype` has 1682 INFERRED edges - model-reasoned connections that need verification._
- **Are the 1456 inferred relationships involving `CategoricalDtype` (e.g. with `Categorical` and `CategoricalAccessor`) actually correct?**
  _`CategoricalDtype` has 1456 INFERRED edges - model-reasoned connections that need verification._
- **Are the 1069 inferred relationships involving `PeriodDtype` (e.g. with `DatelikeOps` and `DatetimeLikeArrayMixin`) actually correct?**
  _`PeriodDtype` has 1069 INFERRED edges - model-reasoned connections that need verification._
- **Are the 1012 inferred relationships involving `StringDtype` (e.g. with `ExtensionArray` and `ExtensionArrayNaResult`) actually correct?**
  _`StringDtype` has 1012 INFERRED edges - model-reasoned connections that need verification._