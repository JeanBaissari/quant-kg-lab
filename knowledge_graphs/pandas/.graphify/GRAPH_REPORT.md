# Graph Report - .  (2026-07-29)

## Corpus Check
- cluster-only mode - file stats not available

## Summary
- 37983 nodes · 69899 edges · 1771 communities detected
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 15263 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: method: 19543 · uses: 15263 · contains: 12810 · calls: 6889 · imports_from: 5745 · rationale_for: 5107 · imports: 3968 · inherits: 574


## Graph Freshness
- Built from Git commit: `9828540`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `StringDtype` - 1025 edges
2. `DataFrame` - 848 edges
3. `WriteBuffer` - 740 edges
4. `Series` - 648 edges
5. `MultiIndex` - 523 edges
6. `Accessor` - 471 edges
7. `ReadBuffer` - 466 edges
8. `OpsMixin` - 433 edges
9. `RangeIndex` - 428 edges
10. `ExtensionArray` - 397 edges

## Surprising Connections (you probably didn't know these)
- `DatelikeOps` --uses--> `ArrowExtensionArray`  [INFERRED]
  pandas/core/arrays/datetimelike.py → asv_bench/benchmarks/array.py
- `DatetimeLikeArrayMixin` --uses--> `ArrowExtensionArray`  [INFERRED]
  pandas/core/arrays/datetimelike.py → asv_bench/benchmarks/array.py
- `Get the int64 values and b_mask to pass to add_overflowsafe.` --uses--> `ArrowExtensionArray`  [INFERRED]
  pandas/core/arrays/datetimelike.py → asv_bench/benchmarks/array.py
- `Add a delta of a timedeltalike          Returns         -------         Same typ` --uses--> `ArrowExtensionArray`  [INFERRED]
  pandas/core/arrays/datetimelike.py → asv_bench/benchmarks/array.py
- `Add a delta of a TimedeltaIndex          Returns         -------         Same ty` --uses--> `ArrowExtensionArray`  [INFERRED]
  pandas/core/arrays/datetimelike.py → asv_bench/benchmarks/array.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.00
Nodes (263): MockEngineDecorator, assert_cannot_add(), assert_invalid_addsub_type(), assert_invalid_comparison(), get_upcast_box(), Assertion helpers for arithmetic tests., Helper function to assert that two objects cannot be added.      Parameters, Helper function to assert that two objects can     neither be added nor subtract (+255 more)

### Community 1 - "Community 1"
Cohesion: 0.01
Nodes (526): ABC, Test extension array that has custom attribute information (not stored on the dt, An interface for extending pandas with custom arrays.  .. warning::     This is, All of pandas' ExtensionArrays.  See :ref:`extending.extension-types` for more., # TODO: other cases?, # TODO: can we de-duplicate with Period._add_timedeltalike_scalar?, Helper functions to generate range-like data for DatetimeArray (and possibly Tim, Accessors for arrow-backed data. (+518 more)

### Community 2 - "Community 2"
Cohesion: 0.01
Nodes (170): argparse, ast, # TODO: Should Series cases also raise? Looks like they use numpy, Benchmarks for pandas at the package-level., TimeImport, Tests that work on both the Python and C engines but do not have a specific clas, Test whether read_csv does not close user-provided file handles.      GH 36980, Support memory map for compressed files.      GH 37621 (+162 more)

### Community 3 - "Community 3"
Cohesion: 0.02
Nodes (170): CategoricalAccessor, Accessor object for categorical properties of the Series values.      This acces, SeriesApply, Data structure for 1-dimensional cross-sectional and time series data, Return cumulative maximum over a Series.          Returns a Series of the same s, Return cumulative sum over a Series.          Returns a Series of the same size, Return cumulative product over a Series.          Returns a Series of the same s, Return a list of the row axis labels. (+162 more)

### Community 4 - "Community 4"
Cohesion: 0.04
Nodes (219): FloatingDtype, NumpyExtensionArray, StringArray, StringDtype, FloatArrayFormatter, PrettyDict, Dict extension to support abbreviated __repr__, get_unanimous_names() (+211 more)

### Community 5 - "Community 5"
Cohesion: 0.02
Nodes (160): ArrowStringArrayMixin, Determine if regex pattern contains features not supported by RE2 / pyarrow., ExtensionArray, ExtensionArrayNaResult, Return the index of minimum value.          In case of multiple occurrences of t, Return the index of maximum value.          In case of multiple occurrences of t, Fill NaN values using an interpolation method.          This method fills missin, Abstract base class for custom 1-D array types.      pandas will recognize insta (+152 more)

### Community 6 - "Community 6"
Cohesion: 0.01
Nodes (78): array_ufunc(), _assign_where(), default_array_ufunc(), dispatch_reduction_ufunc(), dispatch_ufunc_with_out(), Compatibility with numpy ufuncs.      See also     --------     numpy.org/doc/st, If kwargs contain "out1" and "out2", replace that with a tuple "out"      np.div, If we have an `out` keyword, then call the ufunc without `out` and then     set (+70 more)

### Community 7 - "Community 7"
Cohesion: 0.01
Nodes (66): bz2, Tests that work on both the Python and C engines but do not have a specific clas, Tests that work on both the Python and C engines but do not have a specific clas, Tests that work on both the Python and C engines but do not have a specific clas, Tests that work on both the Python and C engines but do not have a specific clas, Tests that work on both the Python and C engines but do not have a specific clas, Tests that work on both the Python and C engines but do not have a specific clas, Tests that work on both the Python and C engines but do not have a specific clas (+58 more)

### Community 8 - "Community 8"
Cohesion: 0.08
Nodes (203): ArrowExtensionArray, Accessor, Custom property-like object.      A descriptor for accessors.      Parameters, OpsMixin, DataFrame --------- An efficient 2D container for potentially mixed-type time se, Get Not equal to of dataframe and other, element-wise (binary operator `ne`)., Get Less than or equal to of dataframe and other, \         element-wise (binary, Get Less than of dataframe and other, element-wise (binary operator `lt`). (+195 more)

### Community 9 - "Community 9"
Cohesion: 0.02
Nodes (151): Module for formatting output data into CSV files., _BaseInfo, _DataFrameInfoPrinter, _DataFrameTableBuilder, _DataFrameTableBuilderNonVerbose, _DataFrameTableBuilderVerbose, _get_dataframe_dtype_counts(), _InfoPrinterAbstract (+143 more)

### Community 10 - "Community 10"
Cohesion: 0.03
Nodes (121): BaseWindow, BaseWindowGroupby, ResamplerWindowApply, BaseIndexer, ExpandingIndexer, ExponentialMovingWindowIndexer, FixedForwardWindowIndexer, FixedWindowIndexer (+113 more)

### Community 11 - "Community 11"
Cohesion: 0.02
Nodes (14): droplevel_result(), ensure_index(), ensure_index_from_sequences(), get_values_for_csv(), Index, maybe_extract_name(), maybe_sequence_to_range(), _maybe_try_sort() (+6 more)

### Community 12 - "Community 12"
Cohesion: 0.01
Nodes (1): pandas_core_arrays_arrow_extension_types

### Community 13 - "Community 13"
Cohesion: 0.01
Nodes (1): TestDataFrameConstructors

### Community 14 - "Community 14"
Cohesion: 0.03
Nodes (1): NDFrame

### Community 15 - "Community 15"
Cohesion: 0.01
Nodes (22): Tests for subclasses of NDArrayBackedExtensionArray, Collection of tests asserting things that should be true for any index subclass, # TODO: belongs in series arithmetic tests?, test_indexing tests the following Index methods:     __getitem__     get_loc, # TODO: make these more consistent?, TestConvertSliceIndexer, TestPutmask, block_maker() (+14 more)

### Community 16 - "Community 16"
Cohesion: 0.03
Nodes (7): ArrowExtensionArray, floor_div_int64(), mod_int(), to_pyarrow_type(), transpose_homogeneous_pyarrow(), ArrowStringArrayMixin, ExtensionArrayNaResult

### Community 17 - "Community 17"
Cohesion: 0.02
Nodes (77): # TODO: We do not have tests specific to string-dtypes,, # TODO: better way to handle this?  non-copying alternative?, # TODO: if tz is UTC, are there situations where we *don't* want a, # TODO: We have no tests for these, # TODO: preserve freq?, ArrowStringArray, _check_pyarrow_available(), _is_string_view() (+69 more)

### Community 18 - "Community 18"
Cohesion: 0.04
Nodes (129): BaseGroupBy, Flags, Flags that apply to pandas objects.      “Flags” differ from “metadata”. Flags r, Whether this object allows duplicate labels.          Setting ``allows_duplicate, Equivalent to public method `where`, except that `other` is not         applied, # TODO: can we use a zero-copy alternative to "repeat"?, Replace values where the condition is False.          This method allows conditi, Replace values where the condition is True.          Where ``cond`` is True, the (+121 more)

### Community 19 - "Community 19"
Cohesion: 0.01
Nodes (1): TestDataFramePlots

### Community 20 - "Community 20"
Cohesion: 0.03
Nodes (103): Float32Dtype, Float64Dtype, FloatingArray, An ExtensionDtype to hold a single size of floating dtype.      These specific i, Return the array type associated with this dtype.          Returns         -----, Safely cast the values to the given dtype.          "safe" in this context means, Array of floating (optional missing) values.      .. warning::         FloatingA, Int16Dtype (+95 more)

### Community 21 - "Community 21"
Cohesion: 0.01
Nodes (2): test_constructor(), TestSeriesConstructors

### Community 22 - "Community 22"
Cohesion: 0.02
Nodes (70): NumpyBlock, BaseBlockManager, _consolidate(), ensure_np_dtype(), interleaved_dtype(), make_na_array(), _merge_blocks(), _preprocess_slice_or_indexer() (+62 more)

### Community 23 - "Community 23"
Cohesion: 0.01
Nodes (44): TestSeriesPeriodValuesDtAccessor, Period benchmarks with non-tslibs dependencies.  See benchmarks.tslibs.period fo, calendar, detect_console_encoding(), Unopinionated display configuration., Try to find the most capable encoding supported by the console.     slightly mod, Tests for DatetimeIndex methods behaving like their Timestamp counterparts, hypothesis_strategies (+36 more)

### Community 24 - "Community 24"
Cohesion: 0.01
Nodes (1): # TODO: test the numeric_only=True case

### Community 25 - "Community 25"
Cohesion: 0.01
Nodes (65): assert_equal_cell_styles(), # TODO: should find a better way to check equality, test_styler_to_excel_unstyled(), frame(), Returns the first ten items in fixture "float_frame"., Fixture to open file for use in each test case., Fixture to set engine for use in each test case.      Rather than requiring `eng, # TODO: why do we get different units? (+57 more)

### Community 26 - "Community 26"
Cohesion: 0.03
Nodes (46): IntervalArray, _maybe_convert_platform_interval(), ExtensionIndex, ExtensionIndex, Index subclass for indexes backed by ExtensionArray., Convert value to be insertable to underlying array., _get_next_label(), _get_prev_label() (+38 more)

### Community 27 - "Community 27"
Cohesion: 0.02
Nodes (80): DatetimeLikeBlock, _DatetimeTZBlock, _make_block(), _maybe_infer_ndim(), This is a pseudo-public API for downstream libraries.  We ask that downstream au, If `ndim` is not provided, infer it from placement and values., This is an analogue to blocks.new_block(_2d) that ensures:     1) correct dimens, implement a datetime64 block with a tz attribute (+72 more)

### Community 28 - "Community 28"
Cohesion: 0.02
Nodes (65): all_indexes_same(), default_index(), _get_combined_index(), _get_distinct_objs(), get_objs_combined_axis(), Return a list with distinct elements of "objs" (different ids).     Preserves or, Return the union or intersection of indexes.      Parameters     ----------, # TODO: handle index names! (+57 more)

### Community 29 - "Community 29"
Cohesion: 0.02
Nodes (69): Index, cartesian_product(), _coerce_indexer_frozen(), _get_na_rep(), MultiIndexPyIntEngine, MultiIndexUInt16Engine, MultiIndexUInt32Engine, MultiIndexUInt64Engine (+61 more)

### Community 30 - "Community 30"
Cohesion: 0.03
Nodes (84): _background_gradient(), _bar(), _highlight_between(), _highlight_value(), Module for applying conditional formatting to DataFrames and Series., Write Styler to a file, buffer or string in Typst format.          .. versionadd, Write Styler to a file, buffer or string in HTML-CSS format.          The output, Write Styler to a file, buffer or string in text format.          Produces a pla (+76 more)

### Community 31 - "Community 31"
Cohesion: 0.02
Nodes (59): get_pandas_objects(), Get all pandas objects within a module.      An object is determined to be part, Ensures that all public objects have their __module__ set to the public import p, test_attributes_module(), string_dtype_highest_priority(), test_comparison_methods_array(), Tests that work on the Python, C and PyArrow engines but do not have a specific, doctest (+51 more)

### Community 32 - "Community 32"
Cohesion: 0.04
Nodes (65): CSVFormatter, Dictionary used for storing number formatting settings., Create the writer & save., buffer_put_lines(), _Datetime64Formatter, EngFormatter, _ExtensionArrayFormatter, format_array() (+57 more)

### Community 33 - "Community 33"
Cohesion: 0.03
Nodes (35): BooleanArray, BooleanDtype, coerce_to_array(), Return the array type associated with this dtype.          Returns         -----, Construct BooleanArray from pyarrow Array/ChunkedArray., Coerce the input values array to numpy arrays with a mask.      Parameters     -, Array of boolean (True/False) data with missing values.      This is a pandas Ex, Extension dtype for boolean data.      This is a pandas Extension dtype for bool (+27 more)

### Community 34 - "Community 34"
Cohesion: 0.05
Nodes (74): create_dataframe_from_blocks(), Low-level function to create a DataFrame from arrays as they are     representin, CSSDict, CategoricalDescription, BlockManager, ReadCsvBuffer, ParserBase, ArrowParserWrapper (+66 more)

### Community 35 - "Community 35"
Cohesion: 0.02
Nodes (70): cat_core(), cat_safe(), _get_group_names(), _get_single_group_name(), Split the string at the first occurrence of `sep`.          This method splits t, Split the string at the last occurrence of `sep`.          This method splits th, Extract element from each component at specified position or with specified key., Join lists contained as elements in the Series/Index with passed delimiter. (+62 more)

### Community 36 - "Community 36"
Cohesion: 0.02
Nodes (1): # TODO: the result below is wrong, should be fixed (GH53325)

### Community 37 - "Community 37"
Cohesion: 0.03
Nodes (97): BytesIO, _BufferedWriter, _BytesIOWrapper, _BytesTarFile, _BytesZipFile, check_parent_directory(), dedup_names(), _expand_user() (+89 more)

### Community 38 - "Community 38"
Cohesion: 0.02
Nodes (78): _adjust_dates_anchored(), asfreq(), _asfreq_compat(), DatetimeIndexResampler, DatetimeIndexResamplerGroupby, _get_period_range_edges(), get_resampler(), get_resampler_for_grouping() (+70 more)

### Community 39 - "Community 39"
Cohesion: 0.02
Nodes (1): TestPandasContainer

### Community 40 - "Community 40"
Cohesion: 0.02
Nodes (2): sqlalchemy, sqlite3

### Community 41 - "Community 41"
Cohesion: 0.03
Nodes (88): DatelikeOps, dtype_to_unit(), _period_dispatch(), Get the int64 values and b_mask to pass to add_overflowsafe., Add a delta of a timedeltalike          Returns         -------         Same typ, Add a delta of a TimedeltaIndex          Returns         -------         Same ty, Subtract pd.NaT from self, Add or subtract array-like of DateOffset objects          Parameters         --- (+80 more)

### Community 43 - "Community 43"
Cohesion: 0.02
Nodes (1): TestIndex

### Community 44 - "Community 44"
Cohesion: 0.02
Nodes (1): TestTSPlot

### Community 45 - "Community 45"
Cohesion: 0.02
Nodes (2): # TODO: Make inplace by using out parameter of ndarray.round?, # TODO: Cannot rely on Numpy returning view after version 2.3

### Community 46 - "Community 46"
Cohesion: 0.02
Nodes (46): data(), data_missing(), make_data(), This file contains a minimal set of tests for compliance with the extension arra, Length-100 array for this type.      * data[0] and data[1] should both be non mi, Length 2 array with [NA, Valid], Test2DCompat, data_for_grouping() (+38 more)

### Community 47 - "Community 47"
Cohesion: 0.04
Nodes (60): ADBCDatabase, BaseEngine, _convert_arrays_to_dataframe(), get_engine(), get_schema(), _get_unicode_name(), _get_valid_sqlite_name(), _handle_date_column() (+52 more)

### Community 48 - "Community 48"
Cohesion: 0.02
Nodes (2): Test that bar and line plots with the same x values are superposed         and t, TestSeriesPlots

### Community 49 - "Community 49"
Cohesion: 0.03
Nodes (25): arrayscalars, npy_math, createTypeContext(), get_attr_length(), get_long_attr(), get_nat(), get_sub_attr(), get_values() (+17 more)

### Community 50 - "Community 50"
Cohesion: 0.02
Nodes (49): # TODO: test True & False, dataclasses, # TODO: this condition is not clear about why we have different behavior, # TODO: most of the rest of this test belongs in indexing tests, # TODO: not clear if these raising is desired (no extant tests),, # TODO: make this not cast to object in pandas 3.0, # TODO: better location for this test?, TestDataFrameConstructorWithDtypeCoercion (+41 more)

### Community 51 - "Community 51"
Cohesion: 0.02
Nodes (1): TestLocBaseIndependent

### Community 52 - "Community 52"
Cohesion: 0.03
Nodes (1): TestStata

### Community 53 - "Community 53"
Cohesion: 0.02
Nodes (1): TestPivotTable

### Community 54 - "Community 54"
Cohesion: 0.02
Nodes (1): test .agg behavior / note that .apply is tested generally in test_groupby.py

### Community 55 - "Community 55"
Cohesion: 0.04
Nodes (49): GroupByApply, DataFrameGroupBy, NamedAgg, Define the SeriesGroupBy and DataFrameGroupBy classes that hold the groupby inte, # TODO: validate types on ScalarResult and move to _typing, Return a Series or DataFrame containing counts of unique rows.          The resu, Helper for column specific aggregation with control over output column names., # TODO: should we do this inside II? (+41 more)

### Community 56 - "Community 56"
Cohesion: 0.03
Nodes (47): Apply, BaseExecutionEngine, frame_apply(), FrameApply, FrameColumnApply, FrameRowApply, include_axis(), is_multi_agg_with_relabel() (+39 more)

### Community 57 - "Community 57"
Cohesion: 0.03
Nodes (43): Return the indices that would sort this array.          This method computes the, Sort the array in-place.          Reorders the elements of the array using :meth, Pad or backfill values, used by Series/DataFrame ffill and bfill.          This, Fill NA/NaN values using the specified method.          This method replaces mis, Return ExtensionArray without NA values.          This method removes all missin, Return boolean ndarray denoting duplicate values.          This method identifie, Shift values by desired number.          Newly introduced missing values are fil, Compute the ExtensionArray of unique values.          This method returns a new (+35 more)

### Community 58 - "Community 58"
Cohesion: 0.02
Nodes (1): TestDataFrameIndexing

### Community 60 - "Community 60"
Cohesion: 0.05
Nodes (39): JointConditionBinOp, _ensure_term(), HDFStore, Return the selection as an Index.          .. warning::             Pandas uses, Return a single column from the table.          This is generally only useful to, Retrieve pandas objects from multiple tables.          .. warning::, Store object in HDFStore.          This method writes a pandas DataFrame or Seri, Remove pandas object partially by specifying the where condition.          If `` (+31 more)

### Community 61 - "Community 61"
Cohesion: 0.03
Nodes (1): TestDataFrameReplace

### Community 62 - "Community 62"
Cohesion: 0.03
Nodes (3): test with the .transform, # TODO: implement SeriesGroupBy.corrwith, # TODO: create xfail condition given other params

### Community 63 - "Community 63"
Cohesion: 0.03
Nodes (1): # TODO: implemented SeriesGroupBy.corrwith. See GH 32293

### Community 64 - "Community 64"
Cohesion: 0.05
Nodes (32): _Column, _convert_datetimes(), Compute the additive correction (in `unit`) to convert SAS day/second counts, Convert to Timestamp if possible, otherwise to datetime.datetime.     SAS float6, Read SAS files in SAS7BDAT format.      Parameters     ----------     path_or_bu, Return a numpy int64 array of the column data lengths, Return a numpy int64 array of the column offsets, Returns a numpy character array of the column types:            s (string) or d (+24 more)

### Community 66 - "Community 66"
Cohesion: 0.03
Nodes (2): lzma, xml_etree_elementtree

### Community 67 - "Community 67"
Cohesion: 0.04
Nodes (72): can_hold_element(), coerce_indexer_dtype(), common_dtype_categorical_compat(), construct_1d_arraylike_from_scalar(), construct_1d_object_array_from_listlike(), construct_2d_arraylike_from_scalar(), convert_dtypes(), dict_compat() (+64 more)

### Community 68 - "Community 68"
Cohesion: 0.04
Nodes (23): DatetimeIndex, _new_DatetimeIndex(), Return the number of microseconds since midnight.          Returns         -----, Snap time stamps to nearest occurring frequency.          Each timestamp in the, Calculate datetime bounds for parsed time string and its resolution.          Pa, Check for mismatched-tzawareness indexing and re-raise as KeyError., Get integer location for requested label          Returns         -------, This function should be overloaded in subclasses that allow non-trivial (+15 more)

### Community 70 - "Community 70"
Cohesion: 0.08
Nodes (45): :func:`~pandas.eval` parsers., Replace local variables with a syntactically valid name.      Parameters     ---, Compose 2 or more callables., Compose a collection of tokenization functions.      Parameters     ----------, Factory for a type checking function of type ``t`` or tuple of types., Filter out AST nodes that are subclasses of ``superclass``., Return a function that raises a NotImplementedError with a passed node name., Decorator to disallow certain nodes from parsing. Raises a     NotImplementedErr (+37 more)

### Community 71 - "Community 71"
Cohesion: 0.03
Nodes (2): Tests Independent Of Base Class, TestiLocBaseIndependent

### Community 72 - "Community 72"
Cohesion: 0.03
Nodes (1): pandas_tests_apply_conftest

### Community 73 - "Community 73"
Cohesion: 0.03
Nodes (3): # TODO: For skipna=False, bool(pd.NA) raises; should groupby?, # TODO: Should be more consistent - return Int64 when dtype.na_value is pd.NA?, # TODO: test that has mixed na_value and NaN either working for

### Community 74 - "Community 74"
Cohesion: 0.05
Nodes (2): flavor_read_html(), TestReadHtml

### Community 75 - "Community 75"
Cohesion: 0.03
Nodes (2): BaseMethodsTests, Various Series and DataFrame methods.

### Community 76 - "Community 76"
Cohesion: 0.06
Nodes (21): CSSResolver, _lowercase_css_values(), Preserves the case for all characters within single or double-quoted strings,, A callable for parsing and resolving CSS to atomic properties., The given declarations to atomic properties.          Parameters         -------, Generates (prop, value) pairs from declarations.          In a future version ma, CssExcelCell, CSSToExcelConverter (+13 more)

### Community 77 - "Community 77"
Cohesion: 0.04
Nodes (26): BaseGrouper, BinGrouper, check_result_array(), DataSplitter, extract_result(), FrameSplitter, _is_indexed_like(), Returns the values of a cython operation. (+18 more)

### Community 78 - "Community 78"
Cohesion: 0.05
Nodes (27): Categorical, _get_codes_for_values(), Add new categories.          `new_categories` will be included at the last/highe, Map categories using an input mapping or function.          Maps the categories, Convert a user-facing fill_value to a representation to use with our         und, The numpy array interface.          Users should not call this directly. Rather,, Detect missing values          Missing values (-1 in .codes) are detected., Inverse of isna          Both missing values (-1 in .codes) and NA as a category (+19 more)

### Community 79 - "Community 79"
Cohesion: 0.03
Nodes (1): TestDataFrameColor

### Community 80 - "Community 80"
Cohesion: 0.05
Nodes (20): _color_in_style(), HexBinPlot, holds_integer(), MPLPlot, PiePlot, PlanePlot, get left (primary) or right (secondary) axes, Return the index of the axis where the column at col_idx should be plotted (+12 more)

### Community 81 - "Community 81"
Cohesion: 0.03
Nodes (1): TestAsOfMerge

### Community 82 - "Community 82"
Cohesion: 0.03
Nodes (1): TestToDatetime

### Community 83 - "Community 83"
Cohesion: 0.03
Nodes (1): TestCategoricalConstructors

### Community 84 - "Community 84"
Cohesion: 0.03
Nodes (1): TestDataFrameAnalytics

### Community 85 - "Community 85"
Cohesion: 0.05
Nodes (1): TestDataFrameToCSV

### Community 86 - "Community 86"
Cohesion: 0.05
Nodes (43): _any(), _asof_by_function(), _AsOfMerge, _convert_arrays_and_get_rizer_klass(), _cross_merge(), _CrossMergeOperation, _factorize_keys(), _get_empty_indexer() (+35 more)

### Community 87 - "Community 87"
Cohesion: 0.03
Nodes (1): TestStyler

### Community 88 - "Community 88"
Cohesion: 0.03
Nodes (3): _check_merge(), get_test_data(), TestMerge

### Community 89 - "Community 89"
Cohesion: 0.03
Nodes (1): TestAstype

### Community 90 - "Community 90"
Cohesion: 0.06
Nodes (18): BaseExprVisitor, BinOp, ConditionBinOp, FilterBinOp, JointFilterBinOp, maybe_expression(), return True if this is a valid field, return True if this is a valid column name for generation (e.g. an         actua (+10 more)

### Community 92 - "Community 92"
Cohesion: 0.03
Nodes (1): # TODO: constructing DatetimeIndex with dtype="M8[s]" without truncating

### Community 93 - "Community 93"
Cohesion: 0.05
Nodes (34): get_groupby_method_args(), Get required arguments for a groupby method.      When parametrizing a test over, _annual_finder(), bday_count_array(), bday_offset_array(), _daily_finder(), deregister(), _get_default_annual_spacing() (+26 more)

### Community 94 - "Community 94"
Cohesion: 0.03
Nodes (1): TestUltraJSONTests

### Community 95 - "Community 95"
Cohesion: 0.03
Nodes (1): pandas_tests_strings

### Community 96 - "Community 96"
Cohesion: 0.14
Nodes (51): Buffer, PandasBuffer, PandasBufferPyarrow, Data in the buffer is guaranteed to be contiguous in memory., Handle only regular columns (= numpy arrays) for now., Buffer size in bytes., Represent this structure as DLPack interface., Device type and device ID for where the data in the buffer resides. (+43 more)

### Community 97 - "Community 97"
Cohesion: 0.06
Nodes (13): assert_block_equal(), create_block(), create_mgr(), create_single_mgr(), fblock(), get_numeric_mat(), mgr(), Functions that take an Index and return an element that should have         blk. (+5 more)

### Community 98 - "Community 98"
Cohesion: 0.04
Nodes (1): TestSeriesReplace

### Community 99 - "Community 99"
Cohesion: 0.07
Nodes (3): ObjectStringArrayMixin, String Methods operating on object-dtype ndarrays., Map a callable over valid elements of the array.          Parameters         ---

### Community 102 - "Community 102"
Cohesion: 0.05
Nodes (23): dt64arr_to_periodarr(), _field_to_int64(), _get_ordinal_range(), _make_field_arrays(), period_array(), PeriodArray, raise_on_incompatible(), _range_from_fields() (+15 more)

### Community 103 - "Community 103"
Cohesion: 0.08
Nodes (55): AttributeError, OptionError, Exception raised for pandas.options.      Backwards compatible with KeyError che, AttributeConflictWarning, CategoricalConversionWarning, ChainedAssignmentError, ClosedFileError, CSSWarning (+47 more)

### Community 104 - "Community 104"
Cohesion: 0.04
Nodes (1): TestExcelWriter

### Community 105 - "Community 105"
Cohesion: 0.04
Nodes (4): left(), # TODO: might reconsider current raise behaviour, see issue 24782, # TODO: should the next loop be un-indented? doing so breaks this test, TestMergeOnIndexes

### Community 106 - "Community 106"
Cohesion: 0.07
Nodes (21): inspect_excel_format(), Extensions that writer engine supports., Mapping of sheet names to sheet objects., Book instance. Class type will depend on the engine used.          This attribut, Write given formatted cells into Excel an excel sheet          Parameters, How to behave when writing to a sheet that already exists in append mode., Convert numpy types to Python types for the Excel writers.          Parameters, checks that path's extension against the Writer's supported         extensions. (+13 more)

### Community 107 - "Community 107"
Cohesion: 0.04
Nodes (1): TestDataFrameSetItem

### Community 108 - "Community 108"
Cohesion: 0.04
Nodes (1): TestSeriesInterpolateData

### Community 109 - "Community 109"
Cohesion: 0.04
Nodes (2): _copy_array_with_layout(), test_mask_memory_layout_mismatch()

### Community 110 - "Community 110"
Cohesion: 0.06
Nodes (32): contains(), Reorder categories as specified in new_categories.          ``new_categories`` n, Necessary for making this object picklable, Memory usage of my values          Parameters         ----------         deep :, Helper for membership check for ``key`` in ``cat``.      This is a helper method, # TODO: GH#15362, Returns True if `key` is in this Categorical., Compute the inverse of a categorical, returning         a dict of categories -> (+24 more)

### Community 111 - "Community 111"
Cohesion: 0.06
Nodes (23): All, Any, Clip, ClipDt, Dir, Dropna, Fillna, Iter (+15 more)

### Community 112 - "Community 112"
Cohesion: 0.04
Nodes (3): _get_expected_range(), Helper to get expected range from a both inclusive range, TestDateRanges

### Community 113 - "Community 113"
Cohesion: 0.04
Nodes (14): hypothesis, hypothesis_extra_dateutil, Behavioral based tests for offsets and date_range.  This file is adapted from ht, Tests for offsets.Tick and subclasses, pandas_libs_byteswap, pandas_testing_hypothesis, _test(), test_float_byteswap() (+6 more)

### Community 114 - "Community 114"
Cohesion: 0.04
Nodes (4): test fancy indexing & misc, # TODO: rename?  remove?, TestDataFrameIndexingUInt64, pandas_tests_indexing_test_floats

### Community 115 - "Community 115"
Cohesion: 0.04
Nodes (9): pandas_core_tools, # TODO: should Index get "s" by default here?, Day and some time units.      * D     * s     * ms     * us     * ns, # TODO: Timestamp raises ValueError("could not convert string to Timestamp"), TestDaysInMonth, TestGuessDatetimeFormat, TestShouldCache, TestShouldCacheEarlyBail (+1 more)

### Community 117 - "Community 117"
Cohesion: 0.04
Nodes (1): TestPeriodIndex

### Community 118 - "Community 118"
Cohesion: 0.05
Nodes (9): PandasExprVisitor, PythonExprVisitor, # TODO: using range(5) here is a kludge, # TODO: update testing code so that assert_almost_equal statement, # TODO: 2022-01-29: result return list with numexpr 2.7.3 in CI, should_warn(), TestAlignment, TestScope (+1 more)

### Community 120 - "Community 120"
Cohesion: 0.06
Nodes (22): BaseExcelReader, Parse specified sheet(s) into a DataFrame.          .. deprecated:: 3.1.0, Reader using calamine engine (xlsx/xls/xlsb/ods).          Parameters         --, OpenpyxlWriter, Mapping of sheet names to sheet objects., Save workbook to disk., Convert a style_dict to a set of kwargs suitable for initializing         or upd, Convert ``color_spec`` to an openpyxl v2 Color object.          Parameters (+14 more)

### Community 121 - "Community 121"
Cohesion: 0.04
Nodes (1): TestReaders

### Community 122 - "Community 122"
Cohesion: 0.04
Nodes (1): hashlib

### Community 123 - "Community 123"
Cohesion: 0.04
Nodes (1): TestDataFrameSelectReindex

### Community 124 - "Community 124"
Cohesion: 0.04
Nodes (7): # TODO: ser.where(~mask, alt) unnecessarily upcasts to int64, # TODO: maybe go to float64 since we are changing the _whole_ Series?, # TODO: could also try np.full((1,), td), TestDataFrameSetItemCallable, TestSetitemCallable, TestSetitemCasting, TestSetitemViewCopySemantics

### Community 125 - "Community 125"
Cohesion: 0.05
Nodes (25): _ensure_encoding(), Fixed, GenericTable, represent an object in my store     facilitate read/write of various types of ob, return a pretty representation of myself, set our object attributes, get our object attributes, validate against an existing storable (+17 more)

### Community 127 - "Community 127"
Cohesion: 0.04
Nodes (1): # TODO: this is raising in constructing a Categorical when calling

### Community 128 - "Community 128"
Cohesion: 0.04
Nodes (2): Tests for Timedelta methods:          __mul__, __rmul__,         __div__, __rdiv, TestTimedeltaMultiplicationDivision

### Community 129 - "Community 129"
Cohesion: 0.06
Nodes (16): AsOf, DatetimeAccessor, DatetimeIndex, InferFreq, Iteration, Lookup, ResampleDataFrame, ResampleDatetetime64 (+8 more)

### Community 130 - "Community 130"
Cohesion: 0.06
Nodes (47): _akima_interpolate(), _arrow_temporal_to_i8(), _backfill_1d(), _backfill_2d(), check_value_size(), clean_fill_method(), clean_interp_method(), clean_reindex_fill_method() (+39 more)

### Community 131 - "Community 131"
Cohesion: 0.04
Nodes (3): Yields a dataframe with strings that may or may not need escaping         by bac, Only attributes and variables ('named functions') can be called.         .__call, TestDataFrameQueryBacktickQuoting

### Community 132 - "Community 132"
Cohesion: 0.07
Nodes (29): FrameParser, FrameWriter, JsonReader, JSONTableWriter, Parser, The function read_json accepts three input types:             1. filepath (strin, Combines a list of JSON objects into one JSON object., Read the whole JSON input into a pandas object.          Unlike iterating over t (+21 more)

### Community 133 - "Community 133"
Cohesion: 0.04
Nodes (43): add_doctest_imports(), all_arithmetic_functions(), all_arithmetic_operators(), all_binary_operators(), all_boolean_reductions(), all_logical_operators(), all_numeric_accumulations(), all_numeric_reductions() (+35 more)

### Community 134 - "Community 134"
Cohesion: 0.07
Nodes (23): BaseStringArray, GenericIndexCol, IndexCol, setattr on a PyTables AttributeSet only if the on-disk value differs.      Re-wr, an index column description class      Parameters     ----------     axis   : ax, return whether I am an indexed column, return my current col description, return my cython values (+15 more)

### Community 135 - "Community 135"
Cohesion: 0.04
Nodes (1): TestDatetimeIndex

### Community 136 - "Community 136"
Cohesion: 0.06
Nodes (49): classes(), _classes_and_not_datetimelike(), _get_dtype(), is_all_strings(), is_any_real_numeric_dtype(), is_bool_dtype(), is_complex_dtype(), is_datetime64_any_dtype() (+41 more)

### Community 138 - "Community 138"
Cohesion: 0.05
Nodes (8): _multichunk_csv(), Tests date parsing functionality for all of the parsers defined in parsers.py, # TODO: parse dates directly in pyarrow, see, test_parse_dates_low_memory_embedded_nul_chunks(), test_parse_dates_low_memory_iso8601_reso_bump_across_chunks(), test_parse_dates_low_memory_iso_then_mismatched_layout_chunks(), test_parse_dates_low_memory_iso_then_non_iso_chunks(), test_parse_dates_low_memory_multichunk_datetimes()

### Community 139 - "Community 139"
Cohesion: 0.07
Nodes (36): _assert_almost_equal_both(), _assert_not_almost_equal(), _assert_not_almost_equal_both(), Check that two objects are approximately equal.      This check is performed com, # TODO: to get the same deprecation in assert_numpy_array_equal we need, # TODO: to get the same deprecation in assert_index_equal we need to, Check that two objects are not approximately equal.      Parameters     --------, Check that two objects are not approximately equal.      This check is performed (+28 more)

### Community 140 - "Community 140"
Cohesion: 0.04
Nodes (2): TestBase, TestNumericBase

### Community 141 - "Community 141"
Cohesion: 0.12
Nodes (4): Reads value labels with variable length strings (108 and later format), Reads value labels with fixed-length strings (105 and earlier format), read_stata(), StataReader

### Community 142 - "Community 142"
Cohesion: 0.04
Nodes (4): When include is 'all', then setting exclude != None is not allowed., Test that the percentiles are returned correctly depending on the `percentiles`, TestDataFrameDescribe, TestSeriesDescribe

### Community 143 - "Community 143"
Cohesion: 0.04
Nodes (1): TestDataFrameShift

### Community 144 - "Community 144"
Cohesion: 0.04
Nodes (5): Tests the 'read_fwf' function in parsers.py. This test suite is independent of t, read_fwf supports opening files in binary mode.      GH 18035., encoding should be working, even when using a memory-mapped file.      GH 23254., test_binary_mode(), test_encoding_mmap()

### Community 145 - "Community 145"
Cohesion: 0.04
Nodes (6): Accept read-only mappings for index formatters., Accept read-only mappings for index-name formatters., Accept read-only mappings for column formatters., test_format_index_mapping(), test_format_index_names_mapping(), test_format_mapping()

### Community 146 - "Community 146"
Cohesion: 0.04
Nodes (1): TestTimedeltaArraylikeMulDivOps

### Community 147 - "Community 147"
Cohesion: 0.06
Nodes (32): _construct_from_dt64_naive(), _generate_range(), _infer_tz_from_endpoints(), maybe_convert_dtype(), _maybe_infer_tz(), _maybe_localize_point(), _maybe_normalize_endpoints(), objects_to_datetime64() (+24 more)

### Community 148 - "Community 148"
Cohesion: 0.04
Nodes (2): BaseSetitemTests, Fixture for an indexer to pass to obj.loc to get/set the full length of the

### Community 149 - "Community 149"
Cohesion: 0.06
Nodes (20): AsType, Clip, Count, Describe, Dropna, Dtypes, FindValidIndex, GetDtypeCounts (+12 more)

### Community 150 - "Community 150"
Cohesion: 0.04
Nodes (15): Append, CategoricalLevel, Difference, Duplicated, Duplicates, Equals, GetLoc, GetLocs (+7 more)

### Community 151 - "Community 151"
Cohesion: 0.05
Nodes (13): Crosstab, Cut, Explode, GetDummies, Melt, Pivot, PivotTable, ReshapeExtensionDtype (+5 more)

### Community 152 - "Community 152"
Cohesion: 0.08
Nodes (44): PyTablesExpr, Hold a pytables-like expression, comprised of possibly multiple 'terms'.      Pa, BlockManagerFixed, _dtype_to_kind(), _ensure_str(), FrameFixed, GenericDataIndexableCol, _get_converter() (+36 more)

### Community 153 - "Community 153"
Cohesion: 0.04
Nodes (1): TestInferFreqDeprecation

### Community 154 - "Community 154"
Cohesion: 0.07
Nodes (36): _make_large_csv(), Tests for the parallel read_csv implementation (C engine, large local files).  T, Write a fixed-width CSV, then overwrite the line at the second chunk     boundar, Write a CSV with enough rows to split into multiple parallel chunks., CSV files with newlines inside quoted fields must produce the same result     as, read_csv() transparently uses the parallel path for large local files.     Resul, For a file that exceeds the threshold, the parallel result equals the     result, The parallel path is off by default on Windows but on elsewhere.      Windows sh (+28 more)

### Community 155 - "Community 155"
Cohesion: 0.04
Nodes (1): TestTimedeltas

### Community 156 - "Community 156"
Cohesion: 0.05
Nodes (17): FloatAttrArray, DummyArray, DummyDtype, test_astype(), test_astype_no_copy(), data(), MyEA, Tests for behavior if an author does *not* implement EA methods. (+9 more)

### Community 157 - "Community 157"
Cohesion: 0.06
Nodes (12): DatetimeLikeArrayMixin, Check that left and right Series are equal.      This function compares two Seri, Check that the left and right SparseArray are equal.      Parameters     -------, iter1, iter2: iterables that produce elements     comparable with assert_almost_, Helper method for our assert_* methods that ensures that     the two objects bei, Checks that we have the combination of an ExtensionArraydtype and     a dtype th, Check that ser.iloc[i_slc] matches ser.loc[l_slc] and, if applicable,     ser[l_, Checks classes are equal. (+4 more)

### Community 158 - "Community 158"
Cohesion: 0.04
Nodes (3): Binary file objects should work (if 'mode' contains a 'b') or even without, Binary file objects should honor a specified encoding.          GH 23854 and GH, TestToCSV

### Community 159 - "Community 159"
Cohesion: 0.04
Nodes (1): TestResetIndex

### Community 160 - "Community 160"
Cohesion: 0.06
Nodes (16): _check_roundtrip(), _check_roundtrip_table(), test_can_serialize_dates(), test_empty_series(), test_empty_series_frame(), test_float_index(), test_frame(), test_index_types() (+8 more)

### Community 161 - "Community 161"
Cohesion: 0.05
Nodes (3): _multichunk_indexed_frame(), test_select_nested_or_query_no_warn_without_index(), test_select_nested_or_query_warns()

### Community 162 - "Community 162"
Cohesion: 0.05
Nodes (2): get_dir(), TestSeriesDatetimeValues

### Community 163 - "Community 163"
Cohesion: 0.04
Nodes (1): Tests that work on both the Python and C engines but do not have a specific clas

### Community 164 - "Community 164"
Cohesion: 0.04
Nodes (1): TestTypeInference

### Community 165 - "Community 165"
Cohesion: 0.05
Nodes (2): test_cast_pontwise_result_decimal_nan(), TestArrowArray

### Community 166 - "Community 166"
Cohesion: 0.04
Nodes (1): TestFillNA

### Community 167 - "Community 167"
Cohesion: 0.04
Nodes (1): TestRename

### Community 168 - "Community 168"
Cohesion: 0.04
Nodes (1): these are systematically testing all of the args to value_counts with different

### Community 169 - "Community 169"
Cohesion: 0.05
Nodes (3): assert_equal(), TestMultiIndexSetItem, TestSetitemWithExpansionMultiIndex

### Community 170 - "Community 170"
Cohesion: 0.04
Nodes (1): This module tests the functionality of StringArray and ArrowStringArray. Tests f

### Community 171 - "Community 171"
Cohesion: 0.05
Nodes (1): TestDataFrameReshape

### Community 172 - "Community 172"
Cohesion: 0.05
Nodes (2): Interval specific tests for is_unique in addition to base class tests, TestIntervalIndex

### Community 173 - "Community 173"
Cohesion: 0.05
Nodes (1): TestRangeIndex

### Community 174 - "Community 174"
Cohesion: 0.05
Nodes (1): TestGetDummies

### Community 175 - "Community 175"
Cohesion: 0.05
Nodes (1): TestRolling

### Community 176 - "Community 176"
Cohesion: 0.05
Nodes (13): ComparisonOps, NumericOps, BaseOpsUtil, data(), dtype(), Fixture returning boolean array with valid and missing data, Fixture returning BooleanDtype, TestComparisonOps (+5 more)

### Community 177 - "Community 177"
Cohesion: 0.06
Nodes (43): _check_object_for_strings(), duplicated(), _ensure_arraylike(), _ensure_data(), factorize(), factorize_array(), _get_hashtable_algo(), is_monotonic() (+35 more)

### Community 178 - "Community 178"
Cohesion: 0.05
Nodes (2): TestDataFrameToString, TestSeriesToString

### Community 179 - "Community 179"
Cohesion: 0.05
Nodes (2): Tests that apply specifically to the CParser. Unless specifically stated as a CP, # NOTE: This is only true for the C engine, not Python engine.

### Community 181 - "Community 181"
Cohesion: 0.06
Nodes (42): check_below_min_count(), _get_counts(), _get_counts_nanvar(), _get_dtype_max(), _get_empty_reduction_result(), _get_fill_value(), _get_values(), _maybe_arg_null_out() (+34 more)

### Community 182 - "Community 182"
Cohesion: 0.05
Nodes (19): DatetimeIndexOpsMixin, period_range(), PeriodIndex, Convert the PeriodIndex to the specified frequency `freq`.          Equivalent t, Cast to DatetimeIndex.          If possible, gives microsecond-unit DatetimeInde, The hour of the period.          Returns the hour component for each period in t, The minute of the period.          Returns the minute component for each period, The second of the period.          Returns the second component for each period (+11 more)

### Community 183 - "Community 183"
Cohesion: 0.05
Nodes (13): test date_range, bdate_range construction from the convenience range functions, Tests for date_range with timezones, TestDateRangeNonNano, TestDateRangeTZ, TestDateRangeUnitInference, TestTimestampEquivDateRange, FixedOffset, Fixed offset in minutes east from UTC. (+5 more)

### Community 184 - "Community 184"
Cohesion: 0.05
Nodes (2): dtype(), TestNumpyExtensionArray

### Community 185 - "Community 185"
Cohesion: 0.05
Nodes (1): TestDataFrameRepr

### Community 186 - "Community 186"
Cohesion: 0.06
Nodes (38): pandas_core_dtypes_api, assert_is_valid_plot_return_object(), _check_ax_scales(), _check_axes_shape(), _check_box_return_type(), _check_colors(), _check_data(), _check_has_errorbars() (+30 more)

### Community 187 - "Community 187"
Cohesion: 0.05
Nodes (2): pandas_io_sas_sas7bdat, pandas_io_sas_sas_constants

### Community 188 - "Community 188"
Cohesion: 0.05
Nodes (1): TestPeriodIndex

### Community 189 - "Community 189"
Cohesion: 0.05
Nodes (2): Cases where ``Series.argmax`` and related should raise an exception, TestSeriesReductions

### Community 191 - "Community 191"
Cohesion: 0.05
Nodes (4): TimestampAcrossDst, TimestampConstruction, TimestampOps, TimestampProperties

### Community 193 - "Community 193"
Cohesion: 0.05
Nodes (4): decimal_number_check(), Tests dtype specification during parsing for all of the parsers defined in parse, test_1000_sep_decimal_float_precision(), test_decimal_and_exponential()

### Community 194 - "Community 194"
Cohesion: 0.05
Nodes (1): TestJSONArray

### Community 195 - "Community 195"
Cohesion: 0.06
Nodes (5): # TODO: we could plausibly try to infer down to int16 here, TestFloat16Index, TestFloatNumericIndex, TestIntNumericIndex, TestNumericInt

### Community 196 - "Community 196"
Cohesion: 0.06
Nodes (4): _offset(), Tests for offsets.BusinessHour, TestBusinessHour, TestOpeningTimes

### Community 197 - "Community 197"
Cohesion: 0.05
Nodes (10): month_classes(), offset_types(), Tests of pandas.tseries.offsets, Fixture for month based datetime offsets available for a time series., Fixture for all the datetime offsets available for a time series., # TODO: belongs in arithmetic tests?, test_month_offset_name(), TestOffsetAliases (+2 more)

### Community 198 - "Community 198"
Cohesion: 0.05
Nodes (3): # TODO: parametrize over units just above/below the implementation bounds, TestTimedeltaConstructorKeywordBased, TestTimedeltaConstructorUnitKeyword

### Community 200 - "Community 200"
Cohesion: 0.05
Nodes (25): # TODO: parametrize over timezone?, # TODO: redundant with test_dt64arr_add_sub_DateOffset?  that includes, # TODO: moved from tests.series.test_operators; needs cleanup, # TODO: box + de-duplicate, # TODO: This next block of tests came from tests.series.test_operators,, # TODO: A couple other tests belong in this section.  Move them in, # TODO: Most of this block is moved from series or frame tests, needs, # TODO: Can we default to the ser unit? (+17 more)

### Community 201 - "Community 201"
Cohesion: 0.05
Nodes (2): PeriodIndex.__sub__ and __isub__ with several representations of         the int, TestPeriodIndexArithmetic

### Community 202 - "Community 202"
Cohesion: 0.05
Nodes (28): Determine the freq to stamp on the DatetimeArray returned by         ``self.to_t, If a dtype is specified both directly and indirectly via a `freq` (dtype2),, Return the frequency object for this PeriodArray., The number of days in the month.          .. deprecated:: 3.1.0             Use, Logical indicating if the date belongs to a leap year.          Returns a boolea, validate_dtype_freq(), ArrowPeriodType, all_data() (+20 more)

### Community 203 - "Community 203"
Cohesion: 0.05
Nodes (1): TestGrouping

### Community 206 - "Community 206"
Cohesion: 0.06
Nodes (7): DummyArray, DummyDtype, test_select_dtypes_arrow_instance_exact(), test_select_dtypes_datetime64_instance_unit(), test_select_dtypes_instance_overlap_raises(), test_select_dtypes_numpy_instance_exact(), test_select_dtypes_object_instance_exact()

### Community 207 - "Community 207"
Cohesion: 0.05
Nodes (1): # TODO: standardize return type for MultiIndex.get_loc

### Community 208 - "Community 208"
Cohesion: 0.09
Nodes (27): AbstractEngine, _check_ne_builtin_clash(), NumExprEngine, PythonEngine, Engine classes for :func:`~pandas.eval`, Return an evaluated expression.          Parameters         ----------         e, Evaluate an expression in Python space.      Mostly for testing purposes., Attempt to prevent foot-shooting in a helpful way.      Parameters     --------- (+19 more)

### Community 209 - "Community 209"
Cohesion: 0.05
Nodes (1): TestOperations

### Community 210 - "Community 210"
Cohesion: 0.05
Nodes (1): TestFromRecords

### Community 211 - "Community 211"
Cohesion: 0.05
Nodes (38): all_data(), as_array(), as_frame(), as_series(), box_in_series(), data(), data_for_grouping(), data_for_sorting() (+30 more)

### Community 212 - "Community 212"
Cohesion: 0.06
Nodes (2): This test will fail for:             period:                 since period isn't, TestDataFramePlotsSubplots

### Community 213 - "Community 213"
Cohesion: 0.05
Nodes (1): TestStackUnstackMultiLevel

### Community 214 - "Community 214"
Cohesion: 0.06
Nodes (12): min_fitting_element(), Overriding parent method for the case of all RangeIndex instances.          When, Conserve RangeIndex type for scalar and slice keys., Fastpath for __getitem__ when we know we have a slice., Round each value in the Index to the given number of decimals.          Paramete, Create :class:`pandas.RangeIndex` from a ``range`` object.          This method, return the class to use for construction, Create a new RangeIndex with the same class as the caller, don't copy the (+4 more)

### Community 215 - "Community 215"
Cohesion: 0.05
Nodes (2): TestDataFrameIsIn, TestSeriesIsIn

### Community 216 - "Community 216"
Cohesion: 0.06
Nodes (13): _assert_not_series_equal(), _assert_not_series_equal_both(), _assert_series_equal_both(), Check that two Series equal.      This check is performed commutatively.      Pa, Check that two Series are not equal.      Parameters     ----------     a : Seri, Check that two Series are not equal.      This check is performed commutatively., test_less_precise(), test_series_equal() (+5 more)

### Community 217 - "Community 217"
Cohesion: 0.05
Nodes (1): Methods

### Community 218 - "Community 218"
Cohesion: 0.05
Nodes (1): TestDataFrameFormatting

### Community 219 - "Community 219"
Cohesion: 0.08
Nodes (26): bday_to_datetime(), get_finder(), MilliSecondLocator, PandasAutoDateFormatter, PandasAutoDateLocator, Locates the ticks along an axis controlled by a :class:`Series`.      Parameters, Returns the default locations of ticks., Return the locations of the ticks. (+18 more)

### Community 220 - "Community 220"
Cohesion: 0.05
Nodes (2): TestSample, TestSampleDataFrame

### Community 221 - "Community 221"
Cohesion: 0.05
Nodes (3): pandas_io_formats_style_render, # NOTE: if this test fails for new features then 'mi_styler_comp' should be upda, test_export()

### Community 222 - "Community 222"
Cohesion: 0.05
Nodes (2): BaseGetitemTests, Tests for ExtensionArray.__getitem__.

### Community 223 - "Community 223"
Cohesion: 0.07
Nodes (18): ConstructorTests, Tests specific to IntervalIndex.from_arrays, Fixture for IntervalIndex.from_arrays constructor, converts intervals in breaks format to a dictionary of kwargs to         specifi, mixed int/float left/right results in float for both sides, Tests specific to IntervalIndex.from_breaks, Fixture for IntervalIndex.from_breaks constructor, Common tests for all variations of IntervalIndex construction. Input data     to (+10 more)

### Community 224 - "Community 224"
Cohesion: 0.05
Nodes (4): Tests for reductions on 2D masked arrays with axis parameter., Tests for any/all on 2D masked arrays with axis parameter., TestAnyAll2D, TestReductions2D

### Community 225 - "Community 225"
Cohesion: 0.08
Nodes (5): kind(), mix(), kind kwarg to pass to SparseArray, Fixture returning True or False, determining whether to operate     op(sparse, d, TestSparseArrayArithmetics

### Community 226 - "Community 226"
Cohesion: 0.05
Nodes (1): TestToDatetimeMisc

### Community 227 - "Community 227"
Cohesion: 0.07
Nodes (10): Float64IndexMethod, GC, IndexAppend, IndexEquals, Indexing, IntervalIndexMethod, SetDisjoint, SetOperations (+2 more)

### Community 228 - "Community 228"
Cohesion: 0.06
Nodes (1): TestCategoricalConcat

### Community 230 - "Community 230"
Cohesion: 0.06
Nodes (3): Public API for DataFrame interchange protocol., pandas_core_interchange_column, pandas_core_interchange_from_dataframe

### Community 231 - "Community 231"
Cohesion: 0.09
Nodes (21): AppendableFrameTable, AppendableMultiFrameTable, AppendableMultiSeriesTable, AppendableSeriesTable, AppendableTable, Append to Table in file.          Node must already exist and be Table format., support fully deleting the node in its entirety (only) - where         specifica, raise if any keywords are passed which are not-None (+13 more)

### Community 232 - "Community 232"
Cohesion: 0.06
Nodes (1): TestJoin

### Community 233 - "Community 233"
Cohesion: 0.06
Nodes (6): Fixture that creates a Categorical Series with no unused categories., Fixture that provides different data types for testing., Fixture that creates a Categorical Series with some unused categories., test_drop_duplicates(), test_drop_duplicates_no_duplicates(), TestSeriesDropDuplicates

### Community 234 - "Community 234"
Cohesion: 0.07
Nodes (30): all_parsers(), all_parsers_all_precisions(), BaseParser, c_parser_only(), CParser, CParserHighMemory, CParserLowMemory, csv1() (+22 more)

### Community 235 - "Community 235"
Cohesion: 0.06
Nodes (1): Tests that apply specifically to the Python parser. Unless specifically stated a

### Community 237 - "Community 237"
Cohesion: 0.06
Nodes (1): TestToDatetimeDataFrame

### Community 238 - "Community 238"
Cohesion: 0.06
Nodes (1): TestRollingTS

### Community 239 - "Community 239"
Cohesion: 0.07
Nodes (18): FloatAttrDtype, Return the array type associated with this dtype.          Returns         -----, CategoricalDtype, PandasExtensionDtype, An np.dtype duck-typed class, suitable for holding a custom dtype.      THIS IS, Return a string representation for a particular object., Type for categorical data with the categories and orderedness.      It is a dtyp, Convert the SparseDtype to a new dtype.          This takes care of converting t (+10 more)

### Community 240 - "Community 240"
Cohesion: 0.09
Nodes (12): _ints_to_td64ns(), _objects_to_td64ns(), Return a DataFrame of the individual resolution components of the Timedeltas., Parameters     ----------     data : list-like     copy : bool, default False, Convert an ndarray with integer-dtype to timedelta64[ns] dtype, treating     the, Convert an object-dtyped or string-dtyped array into a     timedelta64[ns]-dtype, The dtype for the TimedeltaArray.          .. warning::             A future ver, Shared logic for __truediv__, __rtruediv__, __floordiv__, __rfloordiv__ (+4 more)

### Community 241 - "Community 241"
Cohesion: 0.09
Nodes (16): Apply, EWMMethods, ForwardWindowMethods, Groupby, GroupbyEWM, GroupbyEWMEngine, GroupbyLargeGroups, Methods (+8 more)

### Community 242 - "Community 242"
Cohesion: 0.07
Nodes (16): CoercionTest, Fixture to enable raising pytest exceptions, TestCoercionBool, TestCoercionComplex, TestCoercionDatetime64, TestCoercionDatetime64HigherReso, TestCoercionDatetime64TZ, TestCoercionFloat64 (+8 more)

### Community 243 - "Community 243"
Cohesion: 0.06
Nodes (3): any_numpy_array(), Additional tests for NumpyExtensionArray that aren't covered by the interface te, Parametrized fixture for NumPy arrays with different dtypes.      This excludes

### Community 244 - "Community 244"
Cohesion: 0.06
Nodes (1): Tests that the file header is properly handled or inferred during parsing for al

### Community 245 - "Community 245"
Cohesion: 0.06
Nodes (1): TestDataFramePlots

### Community 246 - "Community 246"
Cohesion: 0.06
Nodes (12): Map categories using an input mapping or function.          Parameters         -, Necessary for making this object picklable, Tests whether all elements evaluate True          Returns         -------, Tests whether at least one of elements evaluate True          Returns         --, Sum of non-NA/null values          Parameters         ----------         axis :, Mean of non-NA/null values.          Parameters         ----------         axis, An ExtensionArray for storing sparse data.      SparseArray efficiently stores d, The SparseIndex containing the location of non- ``fill_value`` points. (+4 more)

### Community 247 - "Community 247"
Cohesion: 0.06
Nodes (3): _assert_frame_equal_both(), Check that two DataFrame equal.      This check is performed commutatively., test_frame_equal_row_order_mismatch()

### Community 249 - "Community 249"
Cohesion: 0.09
Nodes (17): ApplyDictReturn, ApplyNonUniqueUnsortedIndex, Cumulative, DateAttributes, Datelike, Float32, GroupByMethods, GroupManyLabels (+9 more)

### Community 250 - "Community 250"
Cohesion: 0.09
Nodes (29): CheckedCall, determine_clipboard(), init_dev_clipboard_clipboard(), init_klipper_clipboard(), init_no_clipboard(), init_osx_pbcopy_clipboard(), init_osx_pyobjc_clipboard(), init_qt_clipboard() (+21 more)

### Community 251 - "Community 251"
Cohesion: 0.10
Nodes (21): convert_from_missing_indexer_tuple(), convert_missing_indexer(), _iLocIndexer, _is_2d_value(), maybe_convert_ix(), maybe_warn_multiindex_expansion(), Purely integer-location based indexing for selection by position.      .. versio, Decide whether we will take a block-by-block path. (+13 more)

### Community 252 - "Community 252"
Cohesion: 0.09
Nodes (20): data(), data_for_grouping(), data_for_sorting(), data_for_twos(), data_missing(), data_missing_for_sorting(), DecimalArrayWithoutCoercion, DecimalArrayWithoutFromSequence (+12 more)

### Community 253 - "Community 253"
Cohesion: 0.08
Nodes (22): ArrowDtype, BaseMaskedDtype, NumpyEADtype, A Pandas ExtensionDtype for NumPy dtypes.      This is mostly for internal compa, The NumPy dtype this NumpyEADtype wraps., A bit-width name for this data-type., A character code (one of 'biufcmMOSUV') identifying the general kind of data., The element size of this data-type object. (+14 more)

### Community 254 - "Community 254"
Cohesion: 0.06
Nodes (7): bool_frame_with_na(), float_frame_with_na(), Fixture for DataFrame of booleans with index of unique strings      Columns are, Fixture for DataFrame of floats with index of unique strings      Columns are [', # TODO: np.median(df, axis=0) gives np.array([2.0, 2.0]) instead, # TODO: why does min_count=1 impact the resulting Windows dtype, TestNuisanceColumns

### Community 255 - "Community 255"
Cohesion: 0.06
Nodes (1): TestLocSetitemWithExpansion

### Community 256 - "Community 256"
Cohesion: 0.06
Nodes (5): test label based indexing with loc, # TODO: should it?  unambiguous when lengths dont match?, # TODO: should we have name="bar"?, # TODO: using a tuple key breaks here in many cases, # TODO: test something here?

### Community 257 - "Community 257"
Cohesion: 0.06
Nodes (1): pandas_core_util_hashing

### Community 258 - "Community 258"
Cohesion: 0.06
Nodes (2): Tests that NA values are properly handled during parsing for all of the parsers, # TODO: this test isn't about the na_values keyword, it is about the empty entri

### Community 259 - "Community 259"
Cohesion: 0.11
Nodes (3): engine=None (the default) should be treated the same as engine='c'., Unit tests for the eligibility predicate., TestCanParallelizeCsv

### Community 261 - "Community 261"
Cohesion: 0.07
Nodes (13): Arithmetic, ArithmeticBlock, FromCoo, GetItem, GetItemMask, make_array(), MinMax, SparseArrayConstructor (+5 more)

### Community 262 - "Community 262"
Cohesion: 0.07
Nodes (30): add_ops(), _compose(), disallow(), _filter_nodes(), _is_type(), _node_not_implemented(), _op_maker(), _preparse() (+22 more)

### Community 263 - "Community 263"
Cohesion: 0.06
Nodes (1): TestInference

### Community 264 - "Community 264"
Cohesion: 0.07
Nodes (12): # TODO: not sure what's correct here., Regression test for: https://github.com/pandas-dev/pandas/issues/33765, # TODO: test_bool_flex_frame needs a better name, Fixture for simple 3x3 DataFrame      Columns are ['one', 'two', 'three'], index, simple_frame(), test_arithmetic_multiindex_align(), test_dataframe_blockwise_slicelike(), test_dataframe_operation_with_non_numeric_types() (+4 more)

### Community 265 - "Community 265"
Cohesion: 0.06
Nodes (1): TestDataFrameSubclassing

### Community 267 - "Community 267"
Cohesion: 0.06
Nodes (2): pure get/set item & fancy indexing, TestFancy

### Community 268 - "Community 268"
Cohesion: 0.18
Nodes (31): pandas_libs_testing, assert_almost_equal(), assert_attr_equal(), assert_categorical_equal(), assert_class_equal(), assert_copy(), assert_datetime_array_equal(), assert_dict_equal() (+23 more)

### Community 270 - "Community 270"
Cohesion: 0.06
Nodes (1): TestMelt

### Community 271 - "Community 271"
Cohesion: 0.06
Nodes (5): _get_overlap_public_nat_methods(), Get overlapping public methods between NaT and another class.      Parameters, test_overlap_public_nat_methods(), TestNaTDeprecations, TestNaTFormatting

### Community 272 - "Community 272"
Cohesion: 0.06
Nodes (1): # TODO: should this raise TypeError

### Community 273 - "Community 273"
Cohesion: 0.06
Nodes (1): TestTimestampConstructors

### Community 275 - "Community 275"
Cohesion: 0.09
Nodes (6): engine(), parser(), TestDataFrameQueryNumExprPandas, TestDataFrameQueryNumExprPython, TestDataFrameQueryPythonPandas, TestDataFrameQueryPythonPython

### Community 276 - "Community 276"
Cohesion: 0.09
Nodes (2): check_round_trip(), TestParquetPyArrow

### Community 277 - "Community 277"
Cohesion: 0.09
Nodes (24): _data_to_frame(), _EtreeFrameParser, get_data_from_filepath(), _LxmlFrameParser, _parse(), preprocess_data(), Parse xml data.          This method will call the other internal methods to, Parse xml nodes.          This method will parse the children and attributes of (+16 more)

### Community 278 - "Community 278"
Cohesion: 0.06
Nodes (4): duplicate_columns_frame(), Test header column, spacer, first line and last line in verbose mode., Dataframe with duplicate column names., test_info_verbose_with_counts_spacing()

### Community 279 - "Community 279"
Cohesion: 0.06
Nodes (13): numba_core, numba_core_datamodel, numba_core_extending, numba_core_imputils, box_index(), box_series(), Convert a Series object to a native structure., Convert a native index structure to an Index object.      If our native index is (+5 more)

### Community 281 - "Community 281"
Cohesion: 0.06
Nodes (1): SharedTests

### Community 282 - "Community 282"
Cohesion: 0.06
Nodes (30): ArrowExtensionArray, OldArrowExtensionArray, test_arithmetic_temporal(), test_comparison_temporal(), test_dictionary_astype_categorical(), test_dt_properties(), test_dt_time_preserve_unit(), test_dt_timedelta_properties() (+22 more)

### Community 283 - "Community 283"
Cohesion: 0.07
Nodes (8): BaseReshapingTests, Tests for reshaping and concatenation., EABackedBlock, Deletes the locs from the block.          We split the block to avoid copying th, The array that Series.array returns. Always an ExtensionArray., return an internal format, currently just the ndarray         this is often over, Mixin for Block subclasses backed by ExtensionArray., return object dtype as boxed values, such as Timestamps/Timedelta

### Community 284 - "Community 284"
Cohesion: 0.08
Nodes (2): _eval_single_bin(), TestEval

### Community 285 - "Community 285"
Cohesion: 0.09
Nodes (27): _build_option_description(), describe_option(), DictWrapper, get_default_val(), _get_deprecated_option(), get_option(), _get_registered_option(), _get_root() (+19 more)

### Community 286 - "Community 286"
Cohesion: 0.07
Nodes (14): IndexOpsMixin, Return True if there are any NaNs.          Enables various performance speedups, An internal function that maps values using the input         correspondence (wh, Return True if values in the object are monotonically increasing.          This, Return True if values in the object are monotonically decreasing.          This, Construct an appropriately-wrapped result from the ArrayLike result         of a, Common ops mixin to support a unified interface / docs for Series / Index, Return the first element of the underlying data as a Python scalar.          Thi (+6 more)

### Community 288 - "Community 288"
Cohesion: 0.08
Nodes (9): Check each of several methods that _should_ be equivalent to `obj[key] = val`, Whether we expect the setting to be in-place or not., NA values that should generally be valid_na for *all* dtypes.          Include b, SetitemCastingEquivalents, TestCoercionFloat32, TestSetitemCastingEquivalents, TestSetitemDT64IntoInt, TestSetitemNADatetimeLikeDtype (+1 more)

### Community 289 - "Community 289"
Cohesion: 0.06
Nodes (24): df(), Test output when replacement is a Series, Test output if index is not RangeIndex, Test output on a callable, base dataframe for testing, Raise ValueError if caselist is not a list., Raise ValueError if no caselist is provided., Raise ValueError if no of caselist is odd. (+16 more)

### Community 290 - "Community 290"
Cohesion: 0.06
Nodes (4): interp_method(), (interpolation, method) arguments for quantile, # TODO: tests for axis=1?, # TODO: empty case?

### Community 291 - "Community 291"
Cohesion: 0.07
Nodes (17): pandas_plotting_misc, holds_integer(), PlotAccessor, This function makes calls to this accessor `__call__` method compatible, Make plots of Series or DataFrame.          Uses the backend specified by the, Plot Series or DataFrame as lines.          This function is useful to plot line, Vertical bar plot.          A bar plot is a plot that presents categorical data, Make a horizontal bar plot.          A horizontal bar plot is a plot that presen (+9 more)

### Community 292 - "Community 292"
Cohesion: 0.09
Nodes (20): _can_parallelize_csv(), _clean_na_values(), _extract_dialect(), _find_chunk_byte_offsets(), _find_data_start_offset(), _floatify_na_values(), _merge_with_dialect_properties(), _read() (+12 more)

### Community 293 - "Community 293"
Cohesion: 0.06
Nodes (1): TestCrosstab

### Community 294 - "Community 294"
Cohesion: 0.06
Nodes (4): Comparing df with int`s (1,2) with a string at isin() ("1")         -> should no, Comparing df with nan value (np.nan,2) with a string at isin() ("NaN")         -, Comparing df with floats (1.4245,2.32441) with a string at isin() ("1.4245"), TestIsin

### Community 295 - "Community 295"
Cohesion: 0.06
Nodes (7): pairwise_frames(), pairwise_other_frame(), pairwise_target_frame(), Pairwise frames test_pairwise, Pairwise target frame for test_pairwise, Pairwise other frame for test_pairwise, TestPairwise

### Community 296 - "Community 296"
Cohesion: 0.07
Nodes (1): TestDatetimeArray

### Community 297 - "Community 297"
Cohesion: 0.08
Nodes (11): BaseIO, ReadCSVCategorical, ToCSV, ToCSVDatetimeBig, NormalizeJSON, ReadJSON, ReadJSONLines, ToJSON (+3 more)

### Community 298 - "Community 298"
Cohesion: 0.07
Nodes (2): # TODO: Block splitting would allow us to avoid copying b, # TODO: Add these in a further optimization

### Community 299 - "Community 299"
Cohesion: 0.07
Nodes (3): Dummy, These test the public routines exposed in types/common.py related to inference a, fractions

### Community 300 - "Community 300"
Cohesion: 0.08
Nodes (20): ExcelFile, ExcelWriter, Format string for dates written into Excel files (e.g. 'YYYY-MM-DD')., combine_kwargs(), _excel2num(), fill_mi_header(), get_default_engine(), maybe_convert_usecols() (+12 more)

### Community 301 - "Community 301"
Cohesion: 0.07
Nodes (3): # TODO: split this test, test_to_html_truncate_multi_index(), test_to_html_truncation_index_false_max_rows()

### Community 302 - "Community 302"
Cohesion: 0.07
Nodes (5): Tests dealing with the NDFrame.allows_duplicates., # TODO:, # TODO: frame, TestPreserves, TestRaises

### Community 303 - "Community 303"
Cohesion: 0.07
Nodes (1): TestGroupBy

### Community 304 - "Community 304"
Cohesion: 0.07
Nodes (1): TestDataFrameIndexingWhere

### Community 305 - "Community 305"
Cohesion: 0.07
Nodes (2): # TODO: assert something?, TestDataFrameAlign

### Community 306 - "Community 306"
Cohesion: 0.07
Nodes (1): TestDataFrameInterpolate

### Community 307 - "Community 307"
Cohesion: 0.07
Nodes (1): TestDataFrameSortIndex

### Community 308 - "Community 308"
Cohesion: 0.09
Nodes (14): arrays_for_binary_ufunc(), # TODO: cases with NAs, axis kwarg for DataFrame, A pair of random, length-100 integer-dtype arrays, that are mostly 0., # TODO: cases with axis kwarg, test_array_ufuncs_for_many_arguments(), test_binary_ufunc_drops_series_name(), test_binary_ufunc_scalar(), test_binary_ufunc_with_array() (+6 more)

### Community 309 - "Community 309"
Cohesion: 0.07
Nodes (1): TestFactorize

### Community 310 - "Community 310"
Cohesion: 0.10
Nodes (2): TestDatetime64NaNOps, TestnanopsDataFrame

### Community 311 - "Community 311"
Cohesion: 0.07
Nodes (1): TestNonNano

### Community 312 - "Community 312"
Cohesion: 0.10
Nodes (10): _FrequencyInferer, infer_freq(), infer_freq_str(), _is_multiple(), _maybe_add_count(), Infer the most likely frequency given the input index.      .. deprecated:: 3.1., Not sure if I can avoid the state machine here, Find the appropriate frequency string to describe the inferred         frequency (+2 more)

### Community 313 - "Community 313"
Cohesion: 0.10
Nodes (15): algorithm, array, cassert, cmath, moments, moments_simd, optional, accumulate_central_diffs() (+7 more)

### Community 314 - "Community 314"
Cohesion: 0.10
Nodes (10): Base, TestApi, TestErrors, TestPDApi, TestTesting, TestUtil, TestTypes, Base (+2 more)

### Community 315 - "Community 315"
Cohesion: 0.07
Nodes (9): non_coercible_categorical(), Monkeypatch Categorical.__array__ to ensure no implicit conversion.      Raises, TestWhere, # TODO: also this op right now produces FutureWarning from numpy, # TODO: should right.asof(left[0]) also raise?, # TODO: Replace with fixturesult, # TODO: a bunch of scattered tests check this deprecation is enforced., # TODO: Parametrize numeric and str tests after self.strIndex fixture (+1 more)

### Community 316 - "Community 316"
Cohesion: 0.07
Nodes (1): TestDatetimeIndexSetOps

### Community 317 - "Community 317"
Cohesion: 0.08
Nodes (27): CategoricalDtypeType, the type of CategoricalDtype, this metaclass determines subclass ability, after_nearest_workday(), before_nearest_workday(), get_calendar(), HolidayCalendarMetaClass, nearest_workday(), next_monday() (+19 more)

### Community 318 - "Community 318"
Cohesion: 0.15
Nodes (19): ReadCSVCachedParseDates, ReadCSVComment, ReadCSVConcatDatetime, ReadCSVConcatDatetimeBadDateValue, ReadCSVCParserLowMemory, ReadCSVDatePyarrowEngine, ReadCSVDInferDatetimeFormat, ReadCSVFloatPrecision (+11 more)

### Community 319 - "Community 319"
Cohesion: 0.07
Nodes (1): TestSeriesFillNA

### Community 320 - "Community 320"
Cohesion: 0.07
Nodes (1): TestDataFrameQuantile

### Community 323 - "Community 323"
Cohesion: 0.07
Nodes (1): TestSeriesRepr

### Community 324 - "Community 324"
Cohesion: 0.07
Nodes (2): Tests for Timedelta methods:          __add__, __radd__,         __sub__, __rsub, TestTimedeltaAdditionSubtraction

### Community 325 - "Community 325"
Cohesion: 0.07
Nodes (1): Tests the usecols functionality during parsing for all of the parsers defined in

### Community 326 - "Community 326"
Cohesion: 0.09
Nodes (27): _check_arg_length(), _check_for_default_values(), _check_for_invalid_keys(), Module that contains many useful utilities for validating data or function argum, Checks whether the length of the `*args` argument passed into a function     has, Checks whether 'kwargs' contains any keys that are not     in 'compat_args' and, Checks whether parameters passed to the **kwargs argument in a     function `fna, Checks whether parameters passed to the *args and **kwargs argument in a     fun (+19 more)

### Community 327 - "Community 327"
Cohesion: 0.07
Nodes (9): FromArrays, FromDicts, FromDictwithTimestamp, FromLists, FromNDArray, FromRange, FromRecords, FromScalar (+1 more)

### Community 328 - "Community 328"
Cohesion: 0.12
Nodes (12): ParallelDatetimeFields, ParallelFactorize, ParallelGroupbyMethods, ParallelGroups, ParallelKth, ParallelReadCSV, ParallelRolling, ParallelTake1D (+4 more)

### Community 329 - "Community 329"
Cohesion: 0.09
Nodes (19): bottleneck_switch, _datetimelike_compat(), disallow, _ensure_numeric(), get_corr_func(), maybe_operate_rowwise(), na_accum_func(), _na_for_min_count() (+11 more)

### Community 330 - "Community 330"
Cohesion: 0.07
Nodes (1): TestDatetimeIndexOps

### Community 331 - "Community 331"
Cohesion: 0.10
Nodes (15): DocBuilder, main(), Execute a command as an OS terminal.          Parameters         ----------, Call sphinx to build documentation.          Attribute `num_jobs` from the class, Open a browser tab showing a single document., Open the rst file `page` and extract its title., Create in the build directory an html file with a redirect,         for every ro, Build HTML documentation. (+7 more)

### Community 332 - "Community 332"
Cohesion: 0.07
Nodes (1): TestSparseArray

### Community 333 - "Community 333"
Cohesion: 0.12
Nodes (22): _adj_justify(), adjoin(), _as_escaped_string(), default_pprint(), _EastAsianTextAdjustment, format_object_summary(), get_adjustment(), _justify() (+14 more)

### Community 334 - "Community 334"
Cohesion: 0.07
Nodes (1): TestDataFrameMisc

### Community 335 - "Community 335"
Cohesion: 0.12
Nodes (22): assert_label_reference(), assert_label_values(), assert_labels_dropped(), assert_level_reference(), assert_level_values(), assert_levels_dropped(), df(), df_ambig() (+14 more)

### Community 336 - "Community 336"
Cohesion: 0.07
Nodes (2): Also test support for datetime64[ns] in Series / DataFrame, TestDatetimeIndex

### Community 337 - "Community 337"
Cohesion: 0.07
Nodes (1): TestJSONNormalize

### Community 338 - "Community 338"
Cohesion: 0.10
Nodes (17): khash, asuint32(), asuint64(), complexobject_cmp(), complexobject_hash(), floatobject_cmp(), floatobject_hash(), kh_complex128_hash_func() (+9 more)

### Community 339 - "Community 339"
Cohesion: 0.07
Nodes (1): TestDataFrameDrop

### Community 340 - "Community 340"
Cohesion: 0.07
Nodes (1): TestTZLocalize

### Community 341 - "Community 341"
Cohesion: 0.08
Nodes (2): assert_array_dicts_equal(), TestTextReader

### Community 343 - "Community 343"
Cohesion: 0.11
Nodes (21): f(), Foo, g(), h(), i(), Tests for the `deprecate_nonkeyword_arguments` decorator, test_all_keyword_arguments(), test_class() (+13 more)

### Community 344 - "Community 344"
Cohesion: 0.07
Nodes (1): test all other .agg behavior

### Community 345 - "Community 345"
Cohesion: 0.07
Nodes (1): TestConcatenate

### Community 346 - "Community 346"
Cohesion: 0.07
Nodes (2): dtypes_for_minmax(), Fixture of dtypes with min and max values used for testing     cummin and cummax

### Community 347 - "Community 347"
Cohesion: 0.08
Nodes (5): Regression test for writing to a not-yet-existent GCS Parquet file., test_arrowparquet_options(), test_fastparquet_options(), test_to_parquet_new_file(), pandas_util

### Community 348 - "Community 348"
Cohesion: 0.07
Nodes (5): pandas_core_reshape_encoding, pandas_core_reshape_melt, pandas_core_reshape_merge, pandas_core_reshape_pivot, pandas_core_reshape_tile

### Community 349 - "Community 349"
Cohesion: 0.07
Nodes (1): TestDataFrameCombineFirst

### Community 350 - "Community 350"
Cohesion: 0.08
Nodes (2): test_join(), TestDataFrameJoin

### Community 354 - "Community 354"
Cohesion: 0.08
Nodes (6): f(), pair_different_warnings(), " Test module for testing ``pandas._testing.assert_produces_warning``., Return pair or different warnings.      Useful for testing how several different, test_assert_produces_warning_honors_filter(), TestFalseOrNoneExpectedWarning

### Community 356 - "Community 356"
Cohesion: 0.09
Nodes (7): DecimalArray2, DecimalDtype2, Return the array type associated with this dtype.          Returns         -----, test_array_string_nd(), test_array_unboxes(), DecimalDtype, pandas_tests_extension_decimal

### Community 357 - "Community 357"
Cohesion: 0.09
Nodes (4): DatetimeIndexConstructor, MultiIndexConstructor, SeriesConstructors, SeriesDtypesConstructors

### Community 358 - "Community 358"
Cohesion: 0.10
Nodes (10): col(), Expression, _parse_args(), _parse_kwargs(), _pretty_print_args_kwargs(), Create an expression that evaluates :meth:`Series.case_when` in a DataFrame, Generate deferred object representing a column of a DataFrame.      Any place wh, Class representing a deferred column.      This is not meant to be instantiated (+2 more)

### Community 359 - "Community 359"
Cohesion: 0.12
Nodes (12): is_label_like(), is_nested_tuple(), _LocIndexer, need_slice(), Returns         -------         bool, Access a group of rows and columns by label(s) or a boolean array.      ``.loc[], Check whether there is the possibility to use ``_multi_take``.          Currentl, Create the indexers for the passed tuple of keys, and         executes the take (+4 more)

### Community 360 - "Community 360"
Cohesion: 0.08
Nodes (25): is_array_like(), is_dataclass(), is_dict_like(), is_file_like(), is_hashable(), is_named_tuple(), is_nested_list_like(), is_number() (+17 more)

### Community 361 - "Community 361"
Cohesion: 0.08
Nodes (1): TestIsValidNAForDtype

### Community 362 - "Community 362"
Cohesion: 0.10
Nodes (22): _escape_latex(), _escape_latex_math(), _math_mode_with_dollar(), _math_mode_with_parentheses(), _maybe_wrap_formatter(), non_reducing_slice(), r"""         Format the text display value of index labels or column headers., r"""         Relabel the index, or column header, keys to display a set of speci (+14 more)

### Community 363 - "Community 363"
Cohesion: 0.08
Nodes (2): The tests in this package are to ensure the proper resultant dtypes of set opera, # TODO: pin down desired dtype; do we want it to be commutative?

### Community 364 - "Community 364"
Cohesion: 0.08
Nodes (1): TestXSWithMultiIndex

### Community 365 - "Community 365"
Cohesion: 0.08
Nodes (26): arrays_to_mgr(), convert_object_array(), dict_to_mgr(), _extract_index(), _finalize_columns_and_data(), _get_names_from_index(), _homogenize(), _list_of_dict_to_arrays() (+18 more)

### Community 366 - "Community 366"
Cohesion: 0.08
Nodes (2): TestGetIndexer, TestGetLoc

### Community 367 - "Community 367"
Cohesion: 0.08
Nodes (19): bday_count(), _get_datevalue(), PeriodConverter, Business-day ordinal for a date (replaces deprecated Period[B].ordinal)., TimeConverter, Specify whether xlabel/ylabel should be used to override index name, # TODO: tighter typing for first return?, # TODO: warn that we are ignoring self.norm if user specified it? (+11 more)

### Community 368 - "Community 368"
Cohesion: 0.08
Nodes (2): TestJoinMultiMulti, TestMergeMulti

### Community 369 - "Community 369"
Cohesion: 0.08
Nodes (1): pandas_tests_test_register_accessor

### Community 370 - "Community 370"
Cohesion: 0.08
Nodes (1): TestPeriodConstruction

### Community 371 - "Community 371"
Cohesion: 0.08
Nodes (1): TestDataFrameGroupByPlots

### Community 372 - "Community 372"
Cohesion: 0.08
Nodes (4): _helper_hypothesis_delimited_date(), Tests for Timestamp parsing, aimed at pandas/_libs/tslibs/parsing.pyx, test_parse_datetime_string_with_reso_dayfirst(), test_parse_datetime_string_with_reso_yearfirst()

### Community 374 - "Community 374"
Cohesion: 0.13
Nodes (6): BaseArithmeticOpsTests, BaseComparisonOpsTests, BaseOpsUtil, BaseUnaryOpsTests, Various Series and DataFrame arithmetic ops methods.      Subclasses supporting, Various Series and DataFrame comparison ops methods.

### Community 375 - "Community 375"
Cohesion: 0.08
Nodes (1): TestCategoricalRepr

### Community 376 - "Community 376"
Cohesion: 0.08
Nodes (1): TestConfig

### Community 377 - "Community 377"
Cohesion: 0.11
Nodes (13): date_conversions, compare_format(), parse_iso_8601_datetime(), apply_tzinfo_offset(), convert_pydatetime_to_datetimestruct(), PyDateTimeToEpoch(), PyDateTimeToIso(), ndarrayobject (+5 more)

### Community 378 - "Community 378"
Cohesion: 0.09
Nodes (2): TestBusinessDateRange, TestCustomDateRange

### Community 379 - "Community 379"
Cohesion: 0.08
Nodes (1): TestSlicing

### Community 380 - "Community 380"
Cohesion: 0.08
Nodes (1): TestCategoricalDtypeParametrized

### Community 381 - "Community 381"
Cohesion: 0.08
Nodes (25): expected_html(), Read HTML file from formats data directory.      Parameters     ----------     d, test_to_html_alignment_with_truncation(), test_to_html_basic_alignment(), test_to_html_decimal(), test_to_html_escaped(), test_to_html_float_format_no_fixed_width(), test_to_html_float_format_object_col() (+17 more)

### Community 382 - "Community 382"
Cohesion: 0.08
Nodes (4): An exhaustive list of pandas methods exercising NDFrame.__finalize__., # TODO: div, mul, etc., # TODO:, # TODO: mul, div, etc.

### Community 383 - "Community 383"
Cohesion: 0.08
Nodes (1): TestCategoricalIndex

### Community 384 - "Community 384"
Cohesion: 0.08
Nodes (3): Series.__getitem__ test classes are organized by the type of key passed., TestGetitemCallable, TestGetitemDeprecatedIndexers

### Community 386 - "Community 386"
Cohesion: 0.08
Nodes (1): TestDataFrameToDict

### Community 387 - "Community 387"
Cohesion: 0.08
Nodes (1): TestDataFramePlots

### Community 389 - "Community 389"
Cohesion: 0.08
Nodes (1): TestTimedeltas

### Community 390 - "Community 390"
Cohesion: 0.08
Nodes (1): TestTimeConversionFormats

### Community 391 - "Community 391"
Cohesion: 0.08
Nodes (25): equalize_decl(), test_attrs_cols_nan_output(), test_attrs_cols_prefix(), test_compression_output(), test_default_namespace(), test_ea_dtypes(), test_elems_and_attrs_cols(), test_elems_cols_nan_output() (+17 more)

### Community 392 - "Community 392"
Cohesion: 0.08
Nodes (14): datetime_index(), freqstr(), period_index(), # TODO: we should probably get the same behavior regardless?, # TODO: more freq variants, Fixture returning parametrized frequency in string format., A fixture to provide PeriodIndex objects with different frequencies.      Most P, # TODO: non-monotone indexes; NaTs, different start dates (+6 more)

### Community 393 - "Community 393"
Cohesion: 0.08
Nodes (1): TestNonNano

### Community 394 - "Community 394"
Cohesion: 0.08
Nodes (2): Though Index.fillna and Series.fillna has separate impl, test here to confirm th, pandas_tests_base_common

### Community 395 - "Community 395"
Cohesion: 0.08
Nodes (1): Iteration

### Community 396 - "Community 396"
Cohesion: 0.10
Nodes (4): CategoricalIndexIndexing, IntervalIndexing, NonNumericSeriesIndexing, NumericSeriesIndexing

### Community 397 - "Community 397"
Cohesion: 0.09
Nodes (4): DatetimeAccessor, Timedelta benchmarks with non-tslibs dependencies.  See benchmarks.tslibs.timede, TimedeltaComponents, TimedeltaIndexing

### Community 398 - "Community 398"
Cohesion: 0.12
Nodes (12): check_dict_or_set_indexers(), _IndexSlice, _LocationIndexer, If a tuple key includes an Ellipsis, replace it with an appropriate         numb, Check the key for valid keys across my indexer., Index with indexers that should return an object of the same dimension         a, Create an object to more easily perform multi-index slicing.      ``IndexSlice``, If we have an axis, adapt the given key to be axis-independent. (+4 more)

### Community 399 - "Community 399"
Cohesion: 0.08
Nodes (1): TestDateRangeNonTickFreq

### Community 400 - "Community 400"
Cohesion: 0.14
Nodes (11): dateutil_relativedelta, makeFY5253LastOfMonth(), makeFY5253LastOfMonthQuarter(), makeFY5253NearestEndMonth(), makeFY5253NearestEndMonthQuarter(), Tests for Fiscal Year and Fiscal Quarter offset classes, test_get_offset_name(), TestFY5253LastOfMonth (+3 more)

### Community 401 - "Community 401"
Cohesion: 0.10
Nodes (3): DecimalArray, to_decimal(), ExtensionScalarOpsMixin

### Community 402 - "Community 402"
Cohesion: 0.11
Nodes (10): Save workbook to disk., synonym for save, to make it more file-like, close io if necessary, ODFReader, Parse an ODF Table into a list of lists, Return number of times this row was repeated         Repeating an empty row appe, Find and decode OpenDocument text:s tags that represent         a run length enc, Read tables out of OpenDocument formatted files.          Parameters         --- (+2 more)

### Community 404 - "Community 404"
Cohesion: 0.09
Nodes (15): aws_credentials(), jsonl_file(), Create a private S3 bucket using moto., The following datasets     are loaded.      - tips.csv     - tips.csv.gz     - t, Path to the tips dataset, Path to a JSONL dataset, DataFrame with the salaries dataset, Mocked AWS Credentials for moto. (+7 more)

### Community 405 - "Community 405"
Cohesion: 0.14
Nodes (11): _convert_index(), _convert_string_array(), GenericFixed, _get_tz(), _maybe_convert_for_string_atom(), a generified fixed version, read an array for the specified node (off of group, for a tz-aware type, return an encoded zone (+3 more)

### Community 406 - "Community 406"
Cohesion: 0.08
Nodes (1): TestDataFrameDiff

### Community 407 - "Community 407"
Cohesion: 0.08
Nodes (1): TestDataFrameSortValues

### Community 408 - "Community 408"
Cohesion: 0.08
Nodes (1): TestToPeriod

### Community 409 - "Community 409"
Cohesion: 0.08
Nodes (1): TestMultiIndexLoc

### Community 410 - "Community 410"
Cohesion: 0.08
Nodes (1): _check_plot_works()

### Community 411 - "Community 411"
Cohesion: 0.08
Nodes (1): TestDataFramePlots

### Community 412 - "Community 412"
Cohesion: 0.08
Nodes (1): TestSeriesPlots

### Community 413 - "Community 413"
Cohesion: 0.08
Nodes (1): TestUnique

### Community 414 - "Community 414"
Cohesion: 0.08
Nodes (1): TestToDatetimeUnit

### Community 415 - "Community 415"
Cohesion: 0.08
Nodes (20): adjust(), engine(), engine_and_raw(), frame(), halflife_with_times(), ignore_na(), numeric_only(), Make mocked series as fixture. (+12 more)

### Community 416 - "Community 416"
Cohesion: 0.10
Nodes (3): adjust_negative_zero(), Helper to adjust the expected result if we are dividing by -0.0     as opposed t, TestDivisionByZero

### Community 417 - "Community 417"
Cohesion: 0.09
Nodes (4): Dim2CompatTests, NDArrayBacked2DTests, Base test suite for extension arrays.  These tests are intended for third-party, BaseParsingTests

### Community 418 - "Community 418"
Cohesion: 0.09
Nodes (2): BaseDtypeTests, Base class for ExtensionDtype classes

### Community 419 - "Community 419"
Cohesion: 0.11
Nodes (8): Duplicated, DuplicatedMaskedArray, Factorize, FactorizePeakmem, Hashing, _make_factorize_data(), Quantile, SortIntegerArray

### Community 420 - "Community 420"
Cohesion: 0.09
Nodes (4): BusinessHourStrftime, DatetimeStrftime, PeriodStrftime, Not optimized yet as %z is not supported by `convert_strftime_format`

### Community 421 - "Community 421"
Cohesion: 0.16
Nodes (22): _assert_match(), _check_promote(), These test the method maybe_promote from core/dtypes/cast.py, Auxiliary function to unify testing of scalar/array promotion.      Parameters, test_maybe_promote_any_numpy_dtype_with_datetimetz(), test_maybe_promote_any_numpy_dtype_with_na(), test_maybe_promote_any_with_bool(), test_maybe_promote_any_with_bytes() (+14 more)

### Community 422 - "Community 422"
Cohesion: 0.13
Nodes (20): _bool_arith_fallback(), _can_use_numexpr(), evaluate(), _evaluate_numexpr(), _evaluate_standard(), get_test_result(), _has_bool_dtype(), Expressions -----------  Offer fast expression evaluation through numexpr (+12 more)

### Community 423 - "Community 423"
Cohesion: 0.09
Nodes (1): pandas_tests_copy_view_util

### Community 424 - "Community 424"
Cohesion: 0.10
Nodes (16): _AtIndexer, _iAtIndexer, IndexingMixin, Mixin for adding .loc/.iloc/.at/.iat to Dataframes and Series., Purely integer-location based indexing for selection by position.          .. ve, Access scalars quickly., Access a single value for a row/column label pair.      Similar to ``loc``, in t, Require they keys to be the same type as the index. (so we don't         fallbac (+8 more)

### Community 425 - "Community 425"
Cohesion: 0.15
Nodes (18): add_minutes_to_datetimestruct(), days_to_yearsdays(), extract_unit(), get_datetimestruct_days(), is_leapyear(), npy_datetimestruct_to_datetime(), pandas_datetime_to_datetimestruct(), scale_time_with_underflow_check() (+10 more)

### Community 426 - "Community 426"
Cohesion: 0.09
Nodes (1): TestStringArray

### Community 427 - "Community 427"
Cohesion: 0.16
Nodes (3): _dedent(), Dedent without new line in the beginning.      Built-in textwrap.dedent would ke, TestToLatexMultiindex

### Community 428 - "Community 428"
Cohesion: 0.09
Nodes (6): Caption for table/tabular LaTeX environment., Short caption for testing \\caption[short_caption]{full_caption}., Label for table/tabular LaTeX environment., Caption for longtable LaTeX environment., Label for longtable LaTeX environment., TestToLatexCaptionLabel

### Community 429 - "Community 429"
Cohesion: 0.09
Nodes (3): _make_2d_ea_df(), Construct a DataFrame with a single 2D ExtensionArray block.      Used for dt64t, TestDataFrameReductions

### Community 430 - "Community 430"
Cohesion: 0.09
Nodes (1): TestLocSeries

### Community 431 - "Community 431"
Cohesion: 0.09
Nodes (19): _concat_homogeneous_fastpath(), _concatenate_join_units(), concatenate_managers(), _dtype_to_na_value(), _get_block_for_concat_plan(), _get_combined_plan(), _get_empty_dtype(), _is_homogeneous_mgr() (+11 more)

### Community 432 - "Community 432"
Cohesion: 0.09
Nodes (2): HDF, HDFStoreDataFrame

### Community 433 - "Community 433"
Cohesion: 0.09
Nodes (23): drop_table(), test_api_categorical(), test_api_chunksize_read(), test_api_dtype_argument(), test_api_escaped_table_name(), test_api_multiindex_roundtrip(), test_api_read_sql_duplicate_columns(), test_api_roundtrip() (+15 more)

### Community 434 - "Community 434"
Cohesion: 0.19
Nodes (17): murmur2_32_32to32(), murmur2_64to32(), createDouble(), decode_any(), decode_array(), decode_false(), decode_null(), decode_numeric() (+9 more)

### Community 435 - "Community 435"
Cohesion: 0.09
Nodes (1): TestDatetimeIndex

### Community 436 - "Community 436"
Cohesion: 0.09
Nodes (2): # TODO: these can work but need to update ser construction., # TODO: use ser.replace(np.nan, NA) once that works

### Community 437 - "Community 437"
Cohesion: 0.09
Nodes (1): TestSelectDtypes

### Community 438 - "Community 438"
Cohesion: 0.11
Nodes (13): PandasDelegate, BaseAccessor, Create a scipy.sparse.coo_matrix from a Series with MultiIndex.          Use row, Convert a Series from sparse values to dense.          Returns         -------, DataFrame accessor for sparse data.      It allows users to interact with a `Dat, Create a new DataFrame from a scipy sparse matrix.          This method converts, Convert a DataFrame with sparse values to dense.          This method converts a, Return the contents of the frame as a sparse SciPy COO matrix.          This met (+5 more)

### Community 439 - "Community 439"
Cohesion: 0.18
Nodes (5): End-to-end correctness: parallel result must match serial result., Call the internal helper directly so file-size guards don't apply., Return kwds as _read() would see them for a default read_csv call., TestFindDataStartOffset, TestReadCsvParallel

### Community 440 - "Community 440"
Cohesion: 0.09
Nodes (2): Test properties such as year, month, weekday, etc...., TestPeriodProperties

### Community 441 - "Community 441"
Cohesion: 0.09
Nodes (10): requests, MockResponse, unittest_mock, Preprocessors, Given the active maintainers defined in the yaml file, it fetches         the Gi, PDEP's (pandas enhancement proposals) are not part of the bar         navigation, Built-in context preprocessors.      Context preprocessors are functions that re, Add the current year to the context, so it can be used for the copyright (+2 more)

### Community 442 - "Community 442"
Cohesion: 0.09
Nodes (1): TestSeriesMisc

### Community 443 - "Community 443"
Cohesion: 0.15
Nodes (6): _make_sparse(), make_sparse_index(), Change the dtype of a SparseArray.          The output will always be a SparseAr, Convert ndarray to sparse format      Parameters     ----------     arr : ndarra, Fill missing values with `value`.          Parameters         ----------, Return boolean ndarray denoting duplicate values.          Parameters         --

### Community 444 - "Community 444"
Cohesion: 0.10
Nodes (6): bar_from_to(), bar_grad(), bar_to(), no_bar(), Used in multiple tests to simplify formatting of expected result, test_align_mixed_cases()

### Community 445 - "Community 445"
Cohesion: 0.09
Nodes (1): TestNonNano

### Community 446 - "Community 446"
Cohesion: 0.09
Nodes (23): _adjust_to_origin(), _array_strptime_with_fallback(), _assemble_from_unit_mappings(), _box_as_indexlike(), _coerce_origin_overflow(), _convert_and_box_cache(), _convert_listlike_datetimes(), _guess_datetime_format_for_array() (+15 more)

### Community 447 - "Community 447"
Cohesion: 0.09
Nodes (3): _BaseVersion, InfinityType, NegativeInfinityType

### Community 448 - "Community 448"
Cohesion: 0.09
Nodes (1): TestTimedeltaArraylikeAddSubOps

### Community 449 - "Community 449"
Cohesion: 0.09
Nodes (1): TestNonNano

### Community 450 - "Community 450"
Cohesion: 0.12
Nodes (11): ArrowAccessor, ListAccessor, Index or slice lists in the Series.          Retrieves elements at the given int, Flatten list values.          Each list element is expanded into separate rows,, Accessor object for structured data properties of the Series values.      Parame, Return the dtype object of each child field of the struct.          The returned, Extract a child field of a struct as a Series.          This method accesses ind, Extract all child fields of a struct as a DataFrame.          Each child field o (+3 more)

### Community 451 - "Community 451"
Cohesion: 0.10
Nodes (3): equal_contents(), Checks if the set of unique elements of arr1 and arr2 are equivalent., TestIndexSetOps

### Community 452 - "Community 452"
Cohesion: 0.13
Nodes (10): Align, I8Merge, JoinIndex, JoinMultiindexSubset, JoinNonUnique, MergeDatetime, MergeEA, MergeMultiIndex (+2 more)

### Community 453 - "Community 453"
Cohesion: 0.15
Nodes (9): Correlation, Covariance, FrameMixedDtypesOps, FrameMultiIndexOps, FrameOps, PearsonCorrelation, Rank, SeriesMultiIndexOps (+1 more)

### Community 454 - "Community 454"
Cohesion: 0.11
Nodes (14): deprecate_option(), DeprecatedOption, Register an option in the package-wide pandas config object      Parameters, Mark option `key` as deprecated, if code attempts to access this option,     a w, register_option(), RegisteredOption, BlockPairInfo, NamedTuple (+6 more)

### Community 456 - "Community 456"
Cohesion: 0.11
Nodes (22): array(), ensure_wrapped_if_datetimelike(), extract_array(), _maybe_repeat(), range_to_ndarray(), Extract the ndarray or ExtensionArray from a Series or Index.      For all other, Wrap datetime64 and timedelta64 ndarrays in DatetimeArray/TimedeltaArray., Convert numpy MaskedArray to ensure mask is softened. (+14 more)

### Community 457 - "Community 457"
Cohesion: 0.10
Nodes (9): DatetimeTimedeltaMixin, _new_TimedeltaIndex(), Immutable Index of timedelta64 data.      Represented internally as int64, and s, Can we compare values of the given dtype to our own?, Compute the result freq for arithmetic operations whose result         is also a, Compute the result freq for Timestamp/datetime - TimedeltaIndex.          Mirror, Get integer location for requested label          Returns         -------, This is called upon unpickling, rather than the default which doesn't     have a (+1 more)

### Community 458 - "Community 458"
Cohesion: 0.10
Nodes (9): IntervalDtype, An ExtensionDtype for Interval data.      **This is not an actual numpy dtype**,, The dtype of the Interval bounds.          Each interval in an :class:`~pandas.a, The type object used to instantiate a scalar of this NumPy data-type., Dtype for data stored in :class:`SparseArray`.      ``SparseDtype`` is used as t, The fill value of the array.          Converting the SparseArray to a dense ndar, Whether the SparseDtype's subtype should be considered ``str``.          Typical, Returns associated scalar type. (+1 more)

### Community 459 - "Community 459"
Cohesion: 0.10
Nodes (21): array_equals(), array_equivalent(), _array_equivalent_datetimelike(), _array_equivalent_float(), _array_equivalent_object(), is_valid_na_for_dtype(), isna(), isna_all() (+13 more)

### Community 460 - "Community 460"
Cohesion: 0.09
Nodes (1): TestFrameArithmeticUnsorted

### Community 461 - "Community 461"
Cohesion: 0.09
Nodes (1): TestFrameFlexArithmetic

### Community 462 - "Community 462"
Cohesion: 0.09
Nodes (1): TestCounting

### Community 463 - "Community 463"
Cohesion: 0.09
Nodes (1): # TODO: Should this be 3?

### Community 464 - "Community 464"
Cohesion: 0.10
Nodes (3): index_view(), test_index_ops(), test_infer_objects()

### Community 465 - "Community 465"
Cohesion: 0.09
Nodes (1): TestSetOpsUnsorted

### Community 466 - "Community 466"
Cohesion: 0.09
Nodes (1): TestChaining

### Community 467 - "Community 467"
Cohesion: 0.10
Nodes (3): CustomFSPath, For testing fspath on unknown objects, TestCommonIOCapabilities

### Community 468 - "Community 468"
Cohesion: 0.09
Nodes (1): TestTableOrient

### Community 469 - "Community 469"
Cohesion: 0.10
Nodes (3): _clean_dict(), Sanitize dictionary for JSON by converting all keys to strings.      Parameters, TestPandasJSONTests

### Community 470 - "Community 470"
Cohesion: 0.17
Nodes (19): Buffer_AppendDoubleUnchecked(), Buffer_AppendIndentNewlineUnchecked(), Buffer_AppendIndentUnchecked(), Buffer_AppendIntUnchecked(), Buffer_AppendLongUnchecked(), Buffer_AppendShortHexUnchecked(), Buffer_EscapeStringUnvalidated(), Buffer_EscapeStringValidated() (+11 more)

### Community 471 - "Community 471"
Cohesion: 0.14
Nodes (21): _cycle_colors(), _derive_colors(), _gen_list_of_colors_from_iterable(), _get_cmap_instance(), _get_colors_from_color(), _get_colors_from_color_type(), get_standard_colors(), _is_floats_color() (+13 more)

### Community 472 - "Community 472"
Cohesion: 0.09
Nodes (1): TestSetIndex

### Community 473 - "Community 473"
Cohesion: 0.10
Nodes (2): _get_with_delta(), TestToTimestamp

### Community 474 - "Community 474"
Cohesion: 0.09
Nodes (2): dataframe_with_duplicate_index(), Fixture for DataFrame used in tests for gh-4145 and gh-4146

### Community 475 - "Community 475"
Cohesion: 0.09
Nodes (1): TestGetIndexer

### Community 476 - "Community 476"
Cohesion: 0.09
Nodes (1): pandas_io_formats_style

### Community 477 - "Community 477"
Cohesion: 0.09
Nodes (1): Tests that the specified index column (a.k.a "index_col") is properly handled or

### Community 478 - "Community 478"
Cohesion: 0.09
Nodes (1): TestUnionCategoricals

### Community 479 - "Community 479"
Cohesion: 0.09
Nodes (1): TestConstructors

### Community 480 - "Community 480"
Cohesion: 0.09
Nodes (2): Testing that we work in the downstream packages, # TODO: could check with arraylike of Period objects

### Community 481 - "Community 481"
Cohesion: 0.13
Nodes (3): TestNankurtFixedValues, TestNanskewFixedValues, TestNanvarFixedValues

### Community 482 - "Community 482"
Cohesion: 0.20
Nodes (13): IsIn, IsinAlmostFullWithRandomInt, IsInFloat64, IsInForObjects, IsInIndexes, IsInLongSeriesLookUpDominates, IsInLongSeriesValuesDominate, IsinWithArange (+5 more)

### Community 483 - "Community 483"
Cohesion: 0.10
Nodes (1): TestMultiplicationDivision

### Community 484 - "Community 484"
Cohesion: 0.12
Nodes (1): Validate / convert value to be StringArray compatible.

### Community 485 - "Community 485"
Cohesion: 0.10
Nodes (10): AssignTimeseriesIndex, Block, ChainIndexing, DataFrameGetitemDuplicateColumns, DatetimeIndexIndexing, GetIndexerNonUnique, LocSetitem2dValue, Benchmark df[key] when columns have duplicate names but key is unique.      Prev (+2 more)

### Community 486 - "Community 486"
Cohesion: 0.10
Nodes (5): Align, DropDuplicates, LevelAlign, Reindex, ReindexMethod

### Community 487 - "Community 487"
Cohesion: 0.10
Nodes (1): TestCategoricalAnalytics

### Community 488 - "Community 488"
Cohesion: 0.10
Nodes (2): TestCategoricalOps, TestCategoricalOpsWithFactor

### Community 489 - "Community 489"
Cohesion: 0.10
Nodes (2): Test common dtype coercion rules between concat and append., TestConcatAppendCommon

### Community 490 - "Community 490"
Cohesion: 0.15
Nodes (20): compress_group_index(), _decons_group_index(), decons_obs_group_ids(), get_compressed_ids(), get_group_index(), get_group_index_sorter(), get_indexer_dict(), is_int64_overflow_possible() (+12 more)

### Community 491 - "Community 491"
Cohesion: 0.16
Nodes (3): adjust_expected(), get_exp_unit(), xfail_datetimes_with_pyxlsb()

### Community 492 - "Community 492"
Cohesion: 0.17
Nodes (20): exceptions, clean_version_list(), _get_dependencies_from_pixi_table(), get_operator_from(), _get_required_dependencies_from_pixi_content(), get_toml_map_from(), _get_version_from_pixi_spec(), get_versions_from_ci() (+12 more)

### Community 493 - "Community 493"
Cohesion: 0.10
Nodes (16): allow_in_pandas(), _assert_attr_equal(), data_for_grouping(), data_for_sorting(), data_missing_for_sorting(), This file contains a minimal set of tests for compliance with the extension arra, Length-3 array with a known sort order.      This should be three items [B, C, A, Length-3 array with a known sort order.      This should be three items [B, NA, (+8 more)

### Community 494 - "Community 494"
Cohesion: 0.10
Nodes (1): pandas_core_reshape

### Community 495 - "Community 495"
Cohesion: 0.10
Nodes (1): # TODO: desired behavior when operating with boolean?  defer?

### Community 496 - "Community 496"
Cohesion: 0.14
Nodes (9): DataCol, DataIndexableCol, a data holding column, by definition this is not indexable      Parameters     -, Get an appropriately typed and shaped pytables.Col object for values., return the PyTables column class for this column, represent a data column that can be indexed, create the description of the table from the axes & values, Open the file in the specified mode          Parameters         ---------- (+1 more)

### Community 497 - "Community 497"
Cohesion: 0.10
Nodes (12): _or_of_ands_columns(), set the position of this column in the Table, set my state from the passed info, return a dict of the kinds allowable columns for this object, validate the min_itemsize doesn't contain items that are not in the         axes, Create the axes sniffed from the table.          Parameters         ----------, Whether ``where`` contains a column selection such as "columns=['A']"., Look for an OR with at least one multi-column AND operand, e.g.     ``(A & B) | (+4 more)

### Community 498 - "Community 498"
Cohesion: 0.10
Nodes (2): assert_framelist_equal(), test_same_ordering()

### Community 499 - "Community 499"
Cohesion: 0.11
Nodes (1): TestBasic

### Community 500 - "Community 500"
Cohesion: 0.12
Nodes (1): JSONArray

### Community 501 - "Community 501"
Cohesion: 0.10
Nodes (6): BoxPlot, BP, _grouped_plot_by_column(), maybe_color_bp(), Set the tick labels of a given axis.      Due to https://github.com/matplotlib/m, _set_ticklabels()

### Community 502 - "Community 502"
Cohesion: 0.17
Nodes (7): AreaPlot, BarhPlot, BarPlot, LinePlot, Specify kind str. Must be overridden in child class, Post process for each axes. Overridden in child classes, Grouped histogram      Parameters     ----------     data : Series/DataFrame

### Community 503 - "Community 503"
Cohesion: 0.10
Nodes (3): TestDatetimeIndexFillNA, TestFillnaPad, pandas_tests_frame_common

### Community 504 - "Community 504"
Cohesion: 0.10
Nodes (2): # TODO: de-duplicate with test_get_loc_duplicates above?, # TODO: Try creating a UnicodeDecodeError in exception message

### Community 505 - "Community 505"
Cohesion: 0.17
Nodes (2): _create_offset(), TestCommon

### Community 506 - "Community 506"
Cohesion: 0.10
Nodes (1): TestDataFrameGroupByPlots

### Community 507 - "Community 507"
Cohesion: 0.10
Nodes (5): Check TimeGrouper's aggregation is identical as normal groupby., Similar test as test_groupby_resample_interpolate_with_apply_syntax but     with, test_aggregate_normal(), test_aggregate_nth(), test_groupby_resample_interpolate_with_apply_syntax_off_grid()

### Community 509 - "Community 509"
Cohesion: 0.10
Nodes (1): TestSeriesLogicalOps

### Community 512 - "Community 512"
Cohesion: 0.10
Nodes (2): Replicate result expected in GH #6297, test_rolling_max_gh6297()

### Community 513 - "Community 513"
Cohesion: 0.15
Nodes (13): read_xml_iterparse(), test_both_dtype_converters(), test_converters_date(), test_converters_str(), test_day_first_parse_dates(), test_dtype_float(), test_dtype_nullable_int(), test_dtype_single_str() (+5 more)

### Community 514 - "Community 514"
Cohesion: 0.10
Nodes (14): # TODO: get inplace ops into assert_invalid_addsub_type, # TODO: Put Series/DataFrame in others?, # TODO: All of these need to be parametrized over box, # TODO: operations with timedelta-like arrays, numeric arrays,, # TODO: making expected be object here a result of DataFrame.__divmod__, # TODO: Should we be parametrizing over types for `ser` too?, # TODO: better name, # TODO: Needs more informative name, probably split up into (+6 more)

### Community 515 - "Community 515"
Cohesion: 0.12
Nodes (9): Return the month names with specified locale.          This method returns the f, Return the day names with specified locale.          This method returns the ful, Convert to a pyarrow TimestampArray with local timestamps., Wrap a pyarrow StringArray in an ArrowStringArray with StringDtype., Returns numpy array of :class:`datetime.time` objects.          The time part of, Returns numpy array of python :class:`datetime.date` objects.          Namely, t, Calculate year, week, and day according to the ISO 8601 standard.          The I, Return boolean array for is_month_start, is_quarter_end, etc.          Parameter (+1 more)

### Community 516 - "Community 516"
Cohesion: 0.10
Nodes (20): ExtensionTests, BaseAccumulateTests, BaseArithmeticOpsTests, BaseCastingTests, BaseComparisonOpsTests, BaseConstructorsTests, BaseDtypeTests, BaseGetitemTests (+12 more)

### Community 517 - "Community 517"
Cohesion: 0.11
Nodes (2): BaseMissingTests, Whether the EA honors the copy keyword in methods like fillna.          EAs that

### Community 518 - "Community 518"
Cohesion: 0.11
Nodes (8): BaseExprVisitor, Constant, PyTablesExprVisitor, PyTablesScope, Validate that the where statement is of the right type.      The type may either, Term, UnaryOp, _validate_where()

### Community 519 - "Community 519"
Cohesion: 0.11
Nodes (5): ArrowStringArray, BooleanArray, IntegerArray, IntervalArray, StringArray

### Community 520 - "Community 520"
Cohesion: 0.10
Nodes (1): TestDataFrameBlockInternals

### Community 521 - "Community 521"
Cohesion: 0.10
Nodes (1): TestCommon

### Community 522 - "Community 522"
Cohesion: 0.15
Nodes (4): gen_obj(), comparator for results         we need to take care if we are indexing on a, make sure that we are raising on positional indexing         w.r.t. an integer i, TestFloatIndexers

### Community 523 - "Community 523"
Cohesion: 0.10
Nodes (6): Fixture to get a Series [(0.5, 1.5], (1.0, 2.0], (2.0, 3.0]], TestSetitemFloatNDarrayIntoIntegerSeries, TestSetitemIntoIntegerSeriesNeedsUpcast, TestSetitemMismatchedTZCastsToObject, TestSetitemNAPeriodDtype, TestSetitemRangeIntoIntegerSeries

### Community 524 - "Community 524"
Cohesion: 0.14
Nodes (8): AstypeTests, Tests specific to IntervalIndex with float subtype, Tests specific to IntervalIndex with datetime-like subtype, Tests common to IntervalIndex with any subtype, Tests specific to IntervalIndex with integer-like subtype, TestDatetimelikeSubtype, TestFloatSubtype, TestIntSubtype

### Community 525 - "Community 525"
Cohesion: 0.15
Nodes (1): TestFeather

### Community 526 - "Community 526"
Cohesion: 0.13
Nodes (6): DotSharedTests, other is a DataFrame that is indexed so that obj.dot(other) is valid, The expected result of obj.dot(other), Assertion about results with 1 fewer dimension that self.obj, TestDataFrameDot, TestSeriesDot

### Community 527 - "Community 527"
Cohesion: 0.10
Nodes (1): TestTimestampRound

### Community 528 - "Community 528"
Cohesion: 0.10
Nodes (1): TestDataFrameUpdate

### Community 529 - "Community 529"
Cohesion: 0.11
Nodes (3): assert_matching(), test_set_codes(), test_set_levels()

### Community 530 - "Community 530"
Cohesion: 0.10
Nodes (1): TestMultiIndexBasic

### Community 531 - "Community 531"
Cohesion: 0.10
Nodes (5): Tests encoding functionality during parsing for all of the parsers defined in pa, Chunk splits a multibyte character with memory_map=True      GH 43540, GH 43787      Test correct handling of UTF-8 chars when memory_map=True and enco, test_chunk_splits_multibyte_char(), test_readcsv_memmap_utf8()

### Community 532 - "Community 532"
Cohesion: 0.10
Nodes (2): Test frequency conversion of date objects, TestFreqConversion

### Community 533 - "Community 533"
Cohesion: 0.10
Nodes (1): TestPeriodMethods

### Community 535 - "Community 535"
Cohesion: 0.10
Nodes (1): ultrajson

### Community 536 - "Community 536"
Cohesion: 0.10
Nodes (1): TestWideToLong

### Community 537 - "Community 537"
Cohesion: 0.10
Nodes (1): TestPivot

### Community 538 - "Community 538"
Cohesion: 0.13
Nodes (20): _bins_to_cuts(), _coerce_to_type(), cut(), _format_labels(), _infer_precision(), _is_dt_or_td(), _nbins_to_bins(), _postprocess_for_cut() (+12 more)

### Community 539 - "Community 539"
Cohesion: 0.10
Nodes (2): _permute(), TestSeriesArithmetic

### Community 540 - "Community 540"
Cohesion: 0.12
Nodes (6): _equivalent_na(), _isnan(), TestGetIndexer, TestGetIndexerNonUnique, TestGetLoc, TestSliceLocs

### Community 541 - "Community 541"
Cohesion: 0.10
Nodes (1): TestMultiLevel

### Community 542 - "Community 542"
Cohesion: 0.10
Nodes (1): TestTimestampArithmetic

### Community 543 - "Community 543"
Cohesion: 0.10
Nodes (1): TestOrigin

### Community 544 - "Community 544"
Cohesion: 0.10
Nodes (4): _cmpkey(), _parse_letter_version(), _parse_local_version(), _Version

### Community 545 - "Community 545"
Cohesion: 0.11
Nodes (2): TestNamedAggregationDataFrame, TestNamedAggregationSeries

### Community 546 - "Community 546"
Cohesion: 0.11
Nodes (1): TestDatetime64Arithmetic

### Community 547 - "Community 547"
Cohesion: 0.11
Nodes (11): numeric_idx(), # TODO: taken from tests.frame.test_operators, needs cleanup, # TODO: add more dtypes, # TODO: moved from tests.series.test_operators; needs cleanup, # TODO: divmod?, # TODO: also test Tick objects;, # TODO: add more  dtypes here, Several types of numeric-dtypes Index objects (+3 more)

### Community 548 - "Community 548"
Cohesion: 0.11
Nodes (4): Algorithms, DataFramePeriodColumn, Indexing, PeriodIndexConstructor

### Community 549 - "Community 549"
Cohesion: 0.11
Nodes (1): TestCategoricalAPI

### Community 550 - "Community 550"
Cohesion: 0.13
Nodes (2): DateArray, DateDtype

### Community 551 - "Community 551"
Cohesion: 0.11
Nodes (3): Change directory and set engine for ExcelFile objects., Change directory and set engine for read_excel calls., TestExcelFileRead

### Community 552 - "Community 552"
Cohesion: 0.11
Nodes (10): data(), data_missing(), data_repeated(), make_data(), This file contains a minimal set of tests for compliance with the extension arra, # TODO: this fails bc we do not pass through data_missing. If we did,, # TODO: this fails bc we do not pass through nullable_string_dtype;, Length-10 SparseArray for semantics test. (+2 more)

### Community 553 - "Community 553"
Cohesion: 0.12
Nodes (3): gen_series_formatting(), TestSeriesFormatting, _three_digit_exp()

### Community 554 - "Community 554"
Cohesion: 0.11
Nodes (1): TestDataFrameConstructorWithDatetimeTZ

### Community 555 - "Community 555"
Cohesion: 0.11
Nodes (8): BaseGroupBy, Dict {group name -> group labels}.          This property provides a dictionary, Dict {group name -> group indices}.          The dictionary keys represent the g, Safe get multiple indices, translate keys for         datelike to underlying rep, Apply a ``func`` with arguments to this GroupBy object and return its result., Construct DataFrame from group with provided name.          This method retrieve, Groupby iterator.          This method provides an iterator over the groups crea, GroupByIndexingMixin

### Community 556 - "Community 556"
Cohesion: 0.15
Nodes (8): GroupByIndexingMixin, GroupByNthSelector, GroupByPositionalSelector, Return positional selection for each group.      ``groupby._positional_selector[, Mixin for adding ._positional_selector to GroupBy., Select by positional index per group.          Implements GroupBy._positional_se, Dynamically substituted for GroupBy.nth to enable both call and index, Return positional selection for each group.          ``groupby._positional_selec

### Community 558 - "Community 558"
Cohesion: 0.11
Nodes (6): # TODO: with mismatched resolution get_indexer currently raises;, TestContains, TestGetItem, TestPutmask, TestTake, TestWhere

### Community 559 - "Community 559"
Cohesion: 0.11
Nodes (5): left_right_dtypes(), Fixture for building an IntervalArray from various dtypes, TestAttributes, TestReductions, TestSetitem

### Community 560 - "Community 560"
Cohesion: 0.11
Nodes (2): check_partition_names(), TestParquetFastParquet

### Community 561 - "Community 561"
Cohesion: 0.23
Nodes (18): _asfreq_plotting(), decorate_axes(), _format_coord(), format_dateaxis(), _get_ax_freq(), _get_freq(), _get_index_freq(), _get_period_alias() (+10 more)

### Community 562 - "Community 562"
Cohesion: 0.11
Nodes (1): TestAsFreq

### Community 564 - "Community 564"
Cohesion: 0.11
Nodes (1): TestRank

### Community 565 - "Community 565"
Cohesion: 0.11
Nodes (1): # NOTE: if MI representation changes, may make sense to allow

### Community 567 - "Community 567"
Cohesion: 0.11
Nodes (15): CompatValidator, process_skipna(), For compatibility with numpy libraries, pandas functions or methods have to acce, If 'Series.argmax' is called via the 'numpy' library, the third parameter     in, If 'Categorical.argsort' is called via the 'numpy' library, the first     parame, If 'NDFrame.clip' is called via the numpy library, the third parameter in     it, If this function is called via the 'numpy' library, the third parameter in     i, 'args' and 'kwargs' should be empty, except for allowed kwargs because all     o (+7 more)

### Community 568 - "Community 568"
Cohesion: 0.15
Nodes (3): _offset(), offset2(), TestBusinessDay

### Community 569 - "Community 569"
Cohesion: 0.12
Nodes (2): _offset(), TestCustomBusinessHour

### Community 570 - "Community 570"
Cohesion: 0.11
Nodes (1): TestDataFrameGroupByPlots

### Community 573 - "Community 573"
Cohesion: 0.11
Nodes (1): TestTimedeltaIndex

### Community 575 - "Community 575"
Cohesion: 0.27
Nodes (3): Helper that performs elementwise comparisons between `array` and `other`, Fixture for all pandas native interval constructors.         To be used as the L, TestComparison

### Community 576 - "Community 576"
Cohesion: 0.11
Nodes (1): TestArithmetic

### Community 577 - "Community 577"
Cohesion: 0.11
Nodes (17): pandas_tests_extension_base_accumulate, pandas_tests_extension_base_casting, pandas_tests_extension_base_constructors, pandas_tests_extension_base_dim2, pandas_tests_extension_base_dtype, pandas_tests_extension_base_getitem, pandas_tests_extension_base_groupby, pandas_tests_extension_base_index (+9 more)

### Community 578 - "Community 578"
Cohesion: 0.11
Nodes (2): BaseInterfaceTests, Tests that the basic interface is satisfied.

### Community 579 - "Community 579"
Cohesion: 0.11
Nodes (5): AggFunctions, CountMultiDtype, CountMultiInt, Groups, MultiColumn

### Community 580 - "Community 580"
Cohesion: 0.11
Nodes (1): MultiIndexing

### Community 582 - "Community 582"
Cohesion: 0.11
Nodes (1): TestAppend

### Community 583 - "Community 583"
Cohesion: 0.11
Nodes (2): 48510 `concat` to an empty EA should maintain type EA dtype., TestEmptyConcat

### Community 585 - "Community 585"
Cohesion: 0.11
Nodes (1): Get Addition of DataFrame and other, column-wise.          Equivalent to ``DataF

### Community 586 - "Community 586"
Cohesion: 0.11
Nodes (1): TestDecimalArray

### Community 587 - "Community 587"
Cohesion: 0.14
Nodes (9): ODSWriter, Write the frame cells using odf, Convert cell attributes to OpenDocument attributes          Parameters         -, Convert cell data to an OpenDocument spreadsheet cell          Parameters, Convert a style dictionary to an OpenDocument style sheet          Parameters, Create freeze panes in the sheet.          Parameters         ----------, Book instance of class odf.opendocument.OpenDocumentSpreadsheet.          This a, Mapping of sheet names to sheet objects. (+1 more)

### Community 588 - "Community 588"
Cohesion: 0.11
Nodes (5): fastparquet, test_invalid_engine(), test_options_auto(), test_options_fp(), test_options_py()

### Community 590 - "Community 590"
Cohesion: 0.11
Nodes (1): TestDataFrameEval

### Community 591 - "Community 591"
Cohesion: 0.16
Nodes (9): _call_and_check(), test_groupby_raises_category(), test_groupby_raises_category_np(), test_groupby_raises_category_on_category(), test_groupby_raises_datetime(), test_groupby_raises_datetime_np(), test_groupby_raises_string(), test_groupby_raises_string_np() (+1 more)

### Community 592 - "Community 592"
Cohesion: 0.11
Nodes (1): TestDtypeEnforced

### Community 593 - "Community 593"
Cohesion: 0.11
Nodes (1): TestSeriesGetitemScalars

### Community 594 - "Community 594"
Cohesion: 0.11
Nodes (1): TestLocWithMultiIndex

### Community 595 - "Community 595"
Cohesion: 0.15
Nodes (3): ParseDateComparison, ReadCSVEngine, ReadUint64Integers

### Community 596 - "Community 596"
Cohesion: 0.11
Nodes (1): TestIndexing

### Community 597 - "Community 597"
Cohesion: 0.11
Nodes (1): TestMergeDtypes

### Community 598 - "Community 598"
Cohesion: 0.11
Nodes (1): TestConvertDtypes

### Community 599 - "Community 599"
Cohesion: 0.11
Nodes (1): TestDataFrameCorrWith

### Community 600 - "Community 600"
Cohesion: 0.11
Nodes (1): TestTZConvert

### Community 602 - "Community 602"
Cohesion: 0.11
Nodes (1): TestSeriesPeriod

### Community 604 - "Community 604"
Cohesion: 0.17
Nodes (5): unstack(), _unstack_extension_series(), _unstack_frame(), _unstack_multiple(), _Unstacker

### Community 606 - "Community 606"
Cohesion: 0.11
Nodes (2): Tests for GH#33603 - string resolution for TimedeltaIndex slicing., TestStringSliceResolution

### Community 607 - "Community 607"
Cohesion: 0.11
Nodes (5): PeriodConstructor, PeriodProperties, PeriodUnaryMethods, TimeDT64ArrToPeriodArr, TimePeriodArrToDT64Arr

### Community 608 - "Community 608"
Cohesion: 0.12
Nodes (4): # TODO: agg should raise for functions that don't aggregate, _convert_grouper(), _factorize_monotonic(), Grouping

### Community 609 - "Community 609"
Cohesion: 0.12
Nodes (9): groupby_func(), numba_supported_reductions(), yields the string names of all groupby reduction functions, one at a time., yields the string names of all groupby transformation functions., yields both aggregation and transformation functions., reductions supported with engine='numba, reduction_func(), transformation_func() (+1 more)

### Community 610 - "Community 610"
Cohesion: 0.15
Nodes (6): Helper to ensure we have the right type of object for a test parametrized     ov, test_transform_empty_dictlike(), test_transform_empty_listlike(), test_transform_udf(), test_transform_ufunc(), unpack_obj()

### Community 611 - "Community 611"
Cohesion: 0.18
Nodes (16): _get_max_value(), _get_min_value(), max(), mean(), min(), _minmax(), prod(), masked_reductions.py is for reduction algorithms using a mask-based approach for (+8 more)

### Community 612 - "Community 612"
Cohesion: 0.13
Nodes (10): Set the categories to the specified new categories.          ``new_categories``, Rename categories.          This method is commonly used to re-label or adjust t, See Series.rank.__doc__., For correctly ranking ordered categorical data. See GH#15420          Ordered ca, Returns True if categorical arrays are equal.          Parameters         ------, Re-encode another categorical using this Categorical's categories.          Note, Returns True if categoricals are the same dtype           same categories, and s, Convert a set of codes for to a new set of categories      Parameters     ------ (+2 more)

### Community 613 - "Community 613"
Cohesion: 0.15
Nodes (1): TimelikeOps

### Community 614 - "Community 614"
Cohesion: 0.15
Nodes (2): Column, PandasColumn

### Community 617 - "Community 617"
Cohesion: 0.15
Nodes (10): DirNamesMixin, Delete unwanted __dir__ for this object., Add additional __dir__ for this object., Provide method name lookup and completion.          Notes         -----, NoNewAttributesMixin, Base and utility classes for pandas objects., Mixin which prevents adding new attributes.      Prevents additional attributes, Memory usage of the values.          Parameters         ----------         deep (+2 more)

### Community 618 - "Community 618"
Cohesion: 0.18
Nodes (4): check_freq_ascending(), check_freq_nonmonotonic(), Check the expected freq on a PeriodIndex/DatetimeIndex/TimedeltaIndex     when t, TestSortValues

### Community 619 - "Community 619"
Cohesion: 0.13
Nodes (16): DeprecationWarning, Pandas4Warning, Pandas5Warning, PandasChangeWarning, PandasDeprecationWarning, PandasFutureWarning, PandasPendingDeprecationWarning, Warning raised for any upcoming change.      This is the base class for all pand (+8 more)

### Community 620 - "Community 620"
Cohesion: 0.12
Nodes (9): DatetimeTZDtype, Construct PeriodArray from pyarrow Array/ChunkedArray., Construct IntervalArray from pyarrow Array/ChunkedArray., Construct IntegerArray/FloatingArray from pyarrow Array/ChunkedArray., An ExtensionDtype for timezone-aware datetime data.      **This is not an actual, The NPY_DATETIMEUNIT corresponding to this dtype's resolution., The precision of the datetime data.          Returns the time resolution as one, The timezone.          Returns the :class:`datetime.tzinfo` object associated wi (+1 more)

### Community 621 - "Community 621"
Cohesion: 0.13
Nodes (7): PeriodDtype, An ExtensionDtype for Period data.      **This is not an actual numpy dtype**, b, Parameters         ----------         freq : PeriodDtype, BaseOffset, or string, The frequency object of this PeriodDtype.          The `freq` property returns t, Return a boolean if the passed type is an actual dtype that we         can match, Parse a string to get the subtype          Parameters         ----------, PeriodDtypeBase

### Community 622 - "Community 622"
Cohesion: 0.12
Nodes (1): TestIsNA

### Community 623 - "Community 623"
Cohesion: 0.12
Nodes (17): DuplicateLabelError, EmptyDataError, IntCastingNaNError, MergeError, NullFrequencyError, ParserError, Exception raised when converting (``astype``) an array with NaN to an integer ty, Exception raised when attempting to call an unsupported numpy function.      For (+9 more)

### Community 625 - "Community 625"
Cohesion: 0.12
Nodes (1): TestIteration

### Community 626 - "Community 626"
Cohesion: 0.12
Nodes (1): TestDataFrameNonuniqueIndexes

### Community 627 - "Community 627"
Cohesion: 0.19
Nodes (3): construct(), construct an object for the given shape     if value is specified use that if it, TestGeneric

### Community 629 - "Community 629"
Cohesion: 0.12
Nodes (5): Tests that can be parametrized over _any_ Index object., # TODO: could work that into the 'exact="equiv"'?, TestReductions, TestRendering, TestRoundTrips

### Community 630 - "Community 630"
Cohesion: 0.18
Nodes (2): test coercion triggered by where, TestWhereCoercion

### Community 631 - "Community 631"
Cohesion: 0.17
Nodes (2): test coercion triggered by fillna, TestFillnaSeriesCoercion

### Community 632 - "Community 632"
Cohesion: 0.12
Nodes (1): TestGetitemBooleanMask

### Community 633 - "Community 633"
Cohesion: 0.12
Nodes (2): Tests for DataFrame.mask; tests DataFrame.where as a side-effect., TestDataFrameMask

### Community 634 - "Community 634"
Cohesion: 0.12
Nodes (1): TestEmptyFrameSetitemExpansion

### Community 635 - "Community 635"
Cohesion: 0.12
Nodes (1): pandas_io

### Community 636 - "Community 636"
Cohesion: 0.19
Nodes (1): Render

### Community 637 - "Community 637"
Cohesion: 0.14
Nodes (4): _assert_all_na(), _assert_same_contents(), _check_join(), _restrict_to_columns()

### Community 638 - "Community 638"
Cohesion: 0.12
Nodes (1): TestSeriesQuantile

### Community 639 - "Community 639"
Cohesion: 0.12
Nodes (1): TestDataFrameToRecords

### Community 640 - "Community 640"
Cohesion: 0.13
Nodes (2): _distant_date_only_for_zoneinfo(), TestTimestampTZLocalize

### Community 641 - "Community 641"
Cohesion: 0.12
Nodes (1): # TODO: reshape

### Community 642 - "Community 642"
Cohesion: 0.19
Nodes (8): _df_bar_subplot_checker(), _df_bar_xyheight_from_ax_helper(), Test cases for misc plot functions, test_bar_1_subplot_1_double_stacked(), test_bar_2_subplot_1_double_stacked(), test_bar_2_subplot_2_double_stacked(), test_bar_2_subplots_1_triple_stacked(), test_bar_subplots_stacking_bool()

### Community 644 - "Community 644"
Cohesion: 0.13
Nodes (2): TestFrameAccessor, TestSeriesAccessor

### Community 645 - "Community 645"
Cohesion: 0.12
Nodes (1): # TODO: Strimg option, this should return string dtype

### Community 646 - "Community 646"
Cohesion: 0.12
Nodes (1): TestTake

### Community 649 - "Community 649"
Cohesion: 0.13
Nodes (1): test cython .agg behavior

### Community 650 - "Community 650"
Cohesion: 0.15
Nodes (11): announce, Directive, docutils, docutils_parsers_rst, git, build_components(), build_string(), get_authors() (+3 more)

### Community 651 - "Community 651"
Cohesion: 0.15
Nodes (2): TestPeriodArray, TestTimedeltaArray

### Community 652 - "Community 652"
Cohesion: 0.13
Nodes (5): BackendLoading, FramePlotting, Misc, SeriesPlotting, TimeseriesPlotting

### Community 654 - "Community 654"
Cohesion: 0.13
Nodes (2): Fixture that provides a CategoricalIndex., TestCategoricalIndex

### Community 655 - "Community 655"
Cohesion: 0.13
Nodes (1): TestTimeSeries

### Community 656 - "Community 656"
Cohesion: 0.13
Nodes (1): TestIntervalDtype

### Community 657 - "Community 657"
Cohesion: 0.13
Nodes (1): TestFrameArithmetic

### Community 658 - "Community 658"
Cohesion: 0.13
Nodes (1): TestNDFrame

### Community 659 - "Community 659"
Cohesion: 0.13
Nodes (1): TestMixedIntIndex

### Community 660 - "Community 660"
Cohesion: 0.15
Nodes (3): equal_contents(), Checks if the set of unique elements of arr1 and arr2 are equivalent., TestSetOps

### Community 661 - "Community 661"
Cohesion: 0.15
Nodes (4): constructor(), test_to_integer_array_bool(), test_to_integer_array_dtype_keyword(), test_to_integer_array_inferred_dtype()

### Community 662 - "Community 662"
Cohesion: 0.13
Nodes (1): TestNestedToRecord

### Community 663 - "Community 663"
Cohesion: 0.13
Nodes (2): # TODO: moved from test_algos; may be redundancies with other tests, tracemalloc

### Community 664 - "Community 664"
Cohesion: 0.21
Nodes (5): LinePlot, HistPlot, KdePlot, merge BoxPlot/KdePlot properties to passed kwds, Calculate bins given data

### Community 665 - "Community 665"
Cohesion: 0.13
Nodes (7): data(), np_dtype_to_arrays(), Fixture returning actual and expected dtype, pandas and numpy arrays and     mas, Test conversion from pyarrow array to numpy array.      Modifies the pyarrow buf, Fixture returning parametrized array from given dtype, including integer,     fl, test_pyarrow_array_to_numpy_and_mask(), pandas_core_arrays_arrow_arrow_utils

### Community 666 - "Community 666"
Cohesion: 0.13
Nodes (1): TestDataFrameMissingData

### Community 667 - "Community 667"
Cohesion: 0.13
Nodes (1): TestTimestampReplace

### Community 668 - "Community 668"
Cohesion: 0.13
Nodes (1): TestTranspose

### Community 670 - "Community 670"
Cohesion: 0.13
Nodes (3): pandas_io_pytables, Fixture for HDF5 path, temp_h5_path()

### Community 671 - "Community 671"
Cohesion: 0.13
Nodes (1): TestJoin

### Community 672 - "Community 672"
Cohesion: 0.13
Nodes (1): TestIndexReductions

### Community 673 - "Community 673"
Cohesion: 0.15
Nodes (16): _clean_keys_and_objs(), concat(), _concat_indexes(), _get_concat_axis_dataframe(), _get_concat_axis_series(), _get_result(), _get_sample_object(), _make_concat_multiindex() (+8 more)

### Community 674 - "Community 674"
Cohesion: 0.13
Nodes (1): TestSeriesCumulativeOps

### Community 675 - "Community 675"
Cohesion: 0.13
Nodes (2): Fixture returning SparseArray with integer entries and 'fill_value=0, zarr()

### Community 676 - "Community 676"
Cohesion: 0.13
Nodes (1): TestSafeSort

### Community 677 - "Community 677"
Cohesion: 0.13
Nodes (1): # TODO: Test more than just reductions (e.g. actually test transformations once

### Community 679 - "Community 679"
Cohesion: 0.13
Nodes (7): Return the values.          For internal compatibility with pandas formatting., Returns an Iterator over the values of this Categorical., return the base repr for the categories, Returns a string representation of the footer., Return formatted string representations of values., Format a list of values into a bracketed, width-respecting string., String representation.

### Community 681 - "Community 681"
Cohesion: 0.13
Nodes (1): BaseConstructorsTests

### Community 682 - "Community 682"
Cohesion: 0.13
Nodes (1): TestDatetimeConcat

### Community 683 - "Community 683"
Cohesion: 0.13
Nodes (1): TestTimezoneConcat

### Community 684 - "Community 684"
Cohesion: 0.13
Nodes (1): TestMultiIndexConcat

### Community 685 - "Community 685"
Cohesion: 0.16
Nodes (8): DropDuplicates, Fixture to test for different frequencies for PeriodIndex., Fixture to get PeriodIndex for 10 periods for different frequencies., Fixture to get DatetimeIndex for 10 periods for different frequencies., Fixture to get TimedeltaIndex for 10 periods for different frequencies., TestDropDuplicatesDatetimeIndex, TestDropDuplicatesPeriodIndex, TestDropDuplicatesTimedeltaIndex

### Community 686 - "Community 686"
Cohesion: 0.17
Nodes (7): EqualsTests, Fixture for creating a TimedeltaIndex for use in equality tests., Fixture for creating a PeriodIndex for use in equality tests., Fixture for creating a DatetimeIndex for use in equality tests., TestDatetimeIndexEquals, TestPeriodIndexEquals, TestTimedeltaIndexEquals

### Community 687 - "Community 687"
Cohesion: 0.14
Nodes (1): TestDatetimeIndex

### Community 688 - "Community 688"
Cohesion: 0.13
Nodes (2): # TODO: moved from test_datetimelike; de-duplicate with version below, # TODO: moved from test_datetimelike; dedup with version below

### Community 690 - "Community 690"
Cohesion: 0.13
Nodes (13): AbstractMethodError, NumExprClobberingError, PyperclipException, PyperclipWindowsException, Raise this error instead of NotImplementedError for abstract methods.      The `, Exception raised when trying to use a built-in numexpr name as a variable name., Exception raised by ``query`` or ``eval`` when using an undefined variable name., Exception raised when clipboard functionality is unsupported.      Raised by ``t (+5 more)

### Community 691 - "Community 691"
Cohesion: 0.21
Nodes (11): assert_resolves(), assert_same_resolution(), test_css_absolute_font_size(), test_css_border_shorthand_sides(), test_css_border_shorthands(), test_css_none_absent(), test_css_parse_invalid(), test_css_parse_normalisation() (+3 more)

### Community 692 - "Community 692"
Cohesion: 0.13
Nodes (3): MyMapping, TestPPrintThing, Mapping

### Community 693 - "Community 693"
Cohesion: 0.29
Nodes (2): get1(), TestFromScalar

### Community 694 - "Community 694"
Cohesion: 0.13
Nodes (2): TestBoxWithBy, TestHistWithBy

### Community 695 - "Community 695"
Cohesion: 0.13
Nodes (3): test where we are determining what we are grouping, or getting groups, # TODO: should prob allow a str of Interval work as well, TestIteration

### Community 697 - "Community 697"
Cohesion: 0.13
Nodes (1): TestIndexConstructorInference

### Community 698 - "Community 698"
Cohesion: 0.13
Nodes (1): TestLoc

### Community 700 - "Community 700"
Cohesion: 0.25
Nodes (11): BaseImpl, FastParquetImpl, get_engine(), _get_path_or_handle(), PyArrowImpl, read_parquet(), to_parquet(), # NOTE: this test is not run by default, because it requires a lot of memory (>5 (+3 more)

### Community 701 - "Community 701"
Cohesion: 0.14
Nodes (2): build_kwargs(), TestClipboard

### Community 702 - "Community 702"
Cohesion: 0.13
Nodes (1): TestNumpyJSONTests

### Community 703 - "Community 703"
Cohesion: 0.13
Nodes (1): TestAstypeCategorical

### Community 704 - "Community 704"
Cohesion: 0.13
Nodes (1): TestDataFrameCorr

### Community 705 - "Community 705"
Cohesion: 0.13
Nodes (1): TestGetLoc

### Community 706 - "Community 706"
Cohesion: 0.14
Nodes (2): check_level_names(), test_changing_names()

### Community 707 - "Community 707"
Cohesion: 0.13
Nodes (1): TestMultiIndexSlicers

### Community 708 - "Community 708"
Cohesion: 0.13
Nodes (1): Tests compressed data parsing functionality for all of the parsers defined in pa

### Community 709 - "Community 709"
Cohesion: 0.14
Nodes (2): _compare_with_tz(), test_append_with_timezones()

### Community 710 - "Community 710"
Cohesion: 0.13
Nodes (1): TestRangeIndexSetOps

### Community 711 - "Community 711"
Cohesion: 0.13
Nodes (1): TestSeriesMode

### Community 712 - "Community 712"
Cohesion: 0.13
Nodes (3): Series with period range index and random data for test purposes., simple_period_range_series(), test_corner_cases_period()

### Community 713 - "Community 713"
Cohesion: 0.13
Nodes (1): TestTimedeltaIndex

### Community 715 - "Community 715"
Cohesion: 0.13
Nodes (14): kml_cta_rail_lines(), Returns the path (as `str`) to the `books.xml` example file.      Examples     -, Returns the path (as `str`) to the `doc_ch_utf.xml` example file.      Examples, Returns the path (as `str`) to the `baby_names.xml` example file.      Examples, Returns the path (as `str`) to the `cta_rail_lines.kml` example file.      Examp, Returns the path (as `str`) to the `flatten_doc.xsl` example file.      Examples, Returns a Path object to the XML example directory.      Examples     --------, Returns the path (as `str`) to the `row_field_output.xsl` example file.      Exa (+6 more)

### Community 716 - "Community 716"
Cohesion: 0.15
Nodes (2): compare_op(), TestAdditionSubtraction

### Community 717 - "Community 717"
Cohesion: 0.14
Nodes (1): TestTimedelta64ArithmeticUnsorted

### Community 718 - "Community 718"
Cohesion: 0.15
Nodes (11): AttributeDocumenter, Documenter, MethodDocumenter, AccessorAttributeDocumenter, AccessorCallableDocumenter, AccessorDocumenter, AccessorLevelDocumenter, AccessorMethodDocumenter (+3 more)

### Community 719 - "Community 719"
Cohesion: 0.15
Nodes (6): CacheReadonly, FastZip, InferDtype, Benchmarks for code in pandas/_libs, excluding pandas/_libs/tslibs, which has it, # TODO: share with something in pd._testing?, ScalarListLike

### Community 720 - "Community 720"
Cohesion: 0.14
Nodes (1): TestDataFrameConcat

### Community 721 - "Community 721"
Cohesion: 0.14
Nodes (1): TestFromDict

### Community 722 - "Community 722"
Cohesion: 0.14
Nodes (1): Reversed Operations not available in the stdlib operator module. Defining these

### Community 723 - "Community 723"
Cohesion: 0.14
Nodes (7): ExtensionDtype, The scalar type for the array, e.g. ``int``          It's expected ``ExtensionAr, Return the common dtype, if one exists.          Used in `find_common_type` impl, Can arrays of this dtype hold NA values?, The Index subclass to return from Index.__new__ when this dtype is         encou, Is transposing an array with this dtype zero-copy?          Only relevant for ca, A custom data type, to be paired with an ExtensionArray.      This enables suppo

### Community 724 - "Community 724"
Cohesion: 0.14
Nodes (1): TestCategoricalDtype

### Community 725 - "Community 725"
Cohesion: 0.14
Nodes (1): TestReprHTML

### Community 727 - "Community 727"
Cohesion: 0.14
Nodes (1): TestDatetimeLike

### Community 728 - "Community 728"
Cohesion: 0.18
Nodes (2): test index's coercion triggered by assign key, TestSetitemCoercion

### Community 729 - "Community 729"
Cohesion: 0.14
Nodes (5): Tests for values coercion in setitem-like operations on DataFrame.  For the most, # TODO: OP in GH#12499 used np.datetim64("NaT") instead of pd.NaT,, # TODO: ATM inserting '2012-01-01 00:00:00' when we have obj.freq=="M", # TODO: i think this isn't about MultiIndex and could be done with iloc?, TestDataFrameSetitemCoercion

### Community 730 - "Community 730"
Cohesion: 0.14
Nodes (1): TestMisc

### Community 731 - "Community 731"
Cohesion: 0.14
Nodes (1): TestDataFrameSetitemCopyViewSemantics

### Community 732 - "Community 732"
Cohesion: 0.14
Nodes (1): TestSetitemBooleanMask

### Community 733 - "Community 733"
Cohesion: 0.14
Nodes (1): TestIntervalRange

### Community 734 - "Community 734"
Cohesion: 0.19
Nodes (6): csv_responder(), gz_csv_responder(), gz_json_responder(), gzip_bytes(), json_responder(), Tests for the pandas custom headers in http(s) requests

### Community 735 - "Community 735"
Cohesion: 0.14
Nodes (2): TestBuildSchema, TestTableOrientReader

### Community 736 - "Community 736"
Cohesion: 0.14
Nodes (1): TestTableSchemaType

### Community 737 - "Community 737"
Cohesion: 0.15
Nodes (3): test_outer_join_indexer(), TestIndexer, pandas_libs_join

### Community 738 - "Community 738"
Cohesion: 0.26
Nodes (10): check_skip(), data(), is_bool_not_implemented(), Fixture returning parametrized (array, scalar) tuple.      Used to test equivale, test_array_NA(), test_array_scalar_like_equivalence(), test_error_len_mismatch(), test_frame() (+2 more)

### Community 739 - "Community 739"
Cohesion: 0.14
Nodes (2): Should process np.nan argument as None, TestDataFrameClip

### Community 740 - "Community 740"
Cohesion: 0.14
Nodes (3): # TODO: this must be int64, # TODO: this must be datetime64, # TODO: should _cast_pointwise_result attempt to preserve unit?

### Community 742 - "Community 742"
Cohesion: 0.14
Nodes (1): TestInsert

### Community 743 - "Community 743"
Cohesion: 0.14
Nodes (1): TestSeriesRank

### Community 745 - "Community 745"
Cohesion: 0.14
Nodes (2): Factory function to create simple 3 x 3 dataframe with     both columns and row, simple_multiindex_dataframe()

### Community 746 - "Community 746"
Cohesion: 0.26
Nodes (2): TestCustomBusinessMonthBegin, TestCustomBusinessMonthEnd

### Community 747 - "Community 747"
Cohesion: 0.14
Nodes (1): TestDateOffset

### Community 748 - "Community 748"
Cohesion: 0.30
Nodes (12): int_min(), _node_cmp(), node_decref(), node_destroy(), node_incref(), node_init(), skiplist_destroy(), skiplist_init() (+4 more)

### Community 749 - "Community 749"
Cohesion: 0.14
Nodes (1): TestPeriodArithmetic

### Community 750 - "Community 750"
Cohesion: 0.16
Nodes (2): TestDateTimeConverter, TestPeriodConverter

### Community 751 - "Community 751"
Cohesion: 0.14
Nodes (1): TestSeriesComparison

### Community 752 - "Community 752"
Cohesion: 0.14
Nodes (1): TestSparseArray

### Community 754 - "Community 754"
Cohesion: 0.16
Nodes (2): tests solely that the result is the same whether or not numexpr is         enabl, TestExpressions

### Community 755 - "Community 755"
Cohesion: 0.19
Nodes (5): _compare_local_to_utc(), _compare_utc_to_local(), SubDatetime, test_tz_convert_single_matches_tz_convert(), test_tz_convert_single_matches_tz_convert_hourly()

### Community 756 - "Community 756"
Cohesion: 0.14
Nodes (1): Tests for helper functions in the cython tslibs.offsets

### Community 757 - "Community 757"
Cohesion: 0.14
Nodes (1): TestArrayToTimedelta64

### Community 758 - "Community 758"
Cohesion: 0.22
Nodes (7): main(), Convert each input to appropriate format for table output., Layout some DataFrames in vertical/horizontal layout for explanation.     Used i, Calculate table shape considering index levels., Calculate appropriate figure size based on left and right data., Plot left / right DataFrames in specified layout.          Parameters         --, TablePlotter

### Community 759 - "Community 759"
Cohesion: 0.15
Nodes (1): TestDatetimeIndexArithmetic

### Community 760 - "Community 760"
Cohesion: 0.15
Nodes (1): TestDatetimeIndexComparisons

### Community 761 - "Community 761"
Cohesion: 0.17
Nodes (12): extract_bool_array(), putmask_inplace(), putmask_without_repeat(), EA-compatible analogue to np.putmask, Validate mask and check if this putmask operation is a no-op., If we have a SparseArray or BooleanArray, convert it to ndarray[bool]., Parameters     ----------     values : np.ndarray     num_set : int         For, ExtensionArray-compatible implementation of np.putmask.  The main     difference (+4 more)

### Community 762 - "Community 762"
Cohesion: 0.17
Nodes (13): _convert_wrapper(), _get_take_nd_function(), _get_take_nd_function_cached(), Specialized Cython take which sets NaN values in one pass., Part of _get_take_nd_function below that doesn't need `mask_info` and thus     c, Get the appropriate "take" implementation for the given dimension, axis     and, Specialized Cython take which sets NaN values in one pass      This dispatches t, take_2d_multi() (+5 more)

### Community 763 - "Community 763"
Cohesion: 0.17
Nodes (3): arrayobject, module_clear(), module_free()

### Community 764 - "Community 764"
Cohesion: 0.18
Nodes (6): Contains, RemoveCategories, Repr, SearchSorted, SetCategories, ValueCounts

### Community 765 - "Community 765"
Cohesion: 0.15
Nodes (2): CheckDtypes, SelectDtypes

### Community 766 - "Community 766"
Cohesion: 0.26
Nodes (6): Float64GroupIndex, NumericSeriesIndexing, NumericSeriesIndexingShuffled, Unique, UniqueAndFactorizeArange, UniqueForLargePyObjectInts

### Community 767 - "Community 767"
Cohesion: 0.21
Nodes (6): MaybeConvertObjects, The functions benchmarked in this file depend _almost_ exclusively on _libs, but, ToDatetimeCacheSmallCount, ToDatetimeFormatQuarters, ToDatetimeYYYYMMDD, ToNumericDowncast

### Community 768 - "Community 768"
Cohesion: 0.15
Nodes (1): TestAstype

### Community 769 - "Community 769"
Cohesion: 0.15
Nodes (1): TestCategoricalIndexReprStringCategories

### Community 770 - "Community 770"
Cohesion: 0.15
Nodes (8): PandasObject, Return a string representation for a particular object., Reset cached properties. If ``key`` is passed, only clears that key., Generates the total memory usage for an object that returns         either a val, Encode the object as an enumerated type or categorical variable.          This m, Base class for various pandas objects., Class constructor (for this class it's just `__class__`)., DirNamesMixin

### Community 771 - "Community 771"
Cohesion: 0.17
Nodes (5): mixin implementing the selection & aggregation interface on a group-like     obj, sub-classes to define         return a sliced object          Parameters, Infer the `selection` to pass to our constructor in _gotitem., Number of dimensions of the underlying data, by definition 1.          Series an, SelectionMixin

### Community 772 - "Community 772"
Cohesion: 0.23
Nodes (5): dict, _Options, Stores pandas plotting options.      Allows for parameter aliasing so you can ju, Reset the option store to its initial state          Returns         -------, Temporarily set a parameter value using the with statement.         Aliasing all

### Community 773 - "Community 773"
Cohesion: 0.15
Nodes (1): TestDatetimeTZDtype

### Community 774 - "Community 774"
Cohesion: 0.15
Nodes (1): # TODO: should this be object with `not using_nan_is_na` to avoid

### Community 775 - "Community 775"
Cohesion: 0.15
Nodes (1): TestToLatex

### Community 776 - "Community 776"
Cohesion: 0.15
Nodes (1): TestFrameLegend

### Community 777 - "Community 777"
Cohesion: 0.17
Nodes (3): skip_if_no_pandas_parser(), TestDataFrameQueryInWithColumnRefs, pandas_core_computation_check

### Community 778 - "Community 778"
Cohesion: 0.15
Nodes (11): Public API for Rolling Window Indexers., Calculate window boundaries based on a non-fixed offset such as a BusinessDay., Parameters         ----------         index_array : np.ndarray or None, VariableOffsetWindowIndexer, pandas_core_indexers_utils, Make sure that decreasing indices give the same results as increasing indices., Ensure that a symmetrical inverted index return same result as non-inverted., Make sure the (rare) branch of non-monotonic indices is covered by a test. (+3 more)

### Community 779 - "Community 779"
Cohesion: 0.24
Nodes (1): TestFrozenList

### Community 780 - "Community 780"
Cohesion: 0.15
Nodes (1): TestPartialSetting

### Community 781 - "Community 781"
Cohesion: 0.28
Nodes (12): df_from_dict(), A verbatim copy (vendored) of the spec tests. Taken from https://github.com/data, test_buffer(), test_categorical(), test_column_get_chunks(), test_dataframe(), test_df_get_chunks(), test_get_columns() (+4 more)

### Community 782 - "Community 782"
Cohesion: 0.15
Nodes (2): Tests for the pseudo-public API implemented in internals/api.py and exposed in c, pandas_api_internals

### Community 783 - "Community 783"
Cohesion: 0.15
Nodes (1): TestBlockPlacement

### Community 784 - "Community 784"
Cohesion: 0.15
Nodes (2): Fixture providing a Series with an IntervalIndex., TestIntervalIndex

### Community 785 - "Community 785"
Cohesion: 0.15
Nodes (2): shared endpoints are marked as overlapping, TestIntervalTree

### Community 786 - "Community 786"
Cohesion: 0.27
Nodes (4): empty_index(), monotonic_index(), # TODO: standardize return type of non-union setops type(self vs other), TestIntervalIndex

### Community 787 - "Community 787"
Cohesion: 0.18
Nodes (13): check_iris_frame(), flavor(), test_api_read_sql_view(), test_read_iris_query(), test_read_iris_query_chunksize(), test_read_iris_query_expression_with_parameter(), test_read_iris_query_string_with_parameter(), test_read_iris_table() (+5 more)

### Community 788 - "Community 788"
Cohesion: 0.21
Nodes (13): create_and_load_iris(), create_and_load_iris_postgresql(), create_and_load_iris_sqlite3(), create_and_load_iris_view(), iris_table_metadata(), mysql_pymysql_engine_iris(), postgresql_adbc_iris(), postgresql_psycopg2_engine_iris() (+5 more)

### Community 789 - "Community 789"
Cohesion: 0.18
Nodes (2): TestHashTable, TestHashTableWithNans

### Community 791 - "Community 791"
Cohesion: 0.15
Nodes (1): TestMergeOrdered

### Community 792 - "Community 792"
Cohesion: 0.15
Nodes (1): TestMergeCategorical

### Community 793 - "Community 793"
Cohesion: 0.15
Nodes (2): Should process np.nan argument as None, TestSeriesClip

### Community 794 - "Community 794"
Cohesion: 0.18
Nodes (2): assert_check_nselect_boundary(), TestSeriesNLargestNSmallest

### Community 795 - "Community 795"
Cohesion: 0.15
Nodes (3): SharedSetAxisTests, TestDataFrameSetAxis, TestSeriesSetAxis

### Community 797 - "Community 797"
Cohesion: 0.18
Nodes (5): floatify(), to_double(), pd_parser, python, tokenizer

### Community 798 - "Community 798"
Cohesion: 0.17
Nodes (13): boxplot(), boxplot_frame(), boxplot_frame_groupby(), _get_plot_backend(), hist_frame(), hist_series(), _load_backend(), Make a histogram of the DataFrame's columns.      A `histogram`_ is a representa (+5 more)

### Community 799 - "Community 799"
Cohesion: 0.28
Nodes (1): TestSeriesStatReductions

### Community 800 - "Community 800"
Cohesion: 0.15
Nodes (1): TestTake

### Community 801 - "Community 801"
Cohesion: 0.21
Nodes (3): TestBlockIndex, TestIntIndex, TestSparseIndexCommon

### Community 802 - "Community 802"
Cohesion: 0.15
Nodes (1): TestReductions

### Community 803 - "Community 803"
Cohesion: 0.15
Nodes (1): TestMode

### Community 804 - "Community 804"
Cohesion: 0.15
Nodes (1): TestValueCounts

### Community 805 - "Community 805"
Cohesion: 0.23
Nodes (8): ensure_removed(), MyAccessor, Ensure that an attribute added to 'obj' during the test is     removed when we'r, test_accessor_works(), test_no_circular_reference(), test_overwrite_warns(), test_raises_attribute_error(), test_register()

### Community 806 - "Community 806"
Cohesion: 0.15
Nodes (1): TestTimestampComparison

### Community 807 - "Community 807"
Cohesion: 0.15
Nodes (1): TestTimestampProperties

### Community 808 - "Community 808"
Cohesion: 0.15
Nodes (3): OffestDatetimeArithmetic, OnOffset, ToOffsetPassthrough

### Community 809 - "Community 809"
Cohesion: 0.24
Nodes (11): _f1(), _f2(), _f3(), _f3_mapping(), _f4(), test_callable_deprecate_kwarg(), test_callable_deprecate_kwarg_fail(), test_deprecate_keyword() (+3 more)

### Community 810 - "Community 810"
Cohesion: 0.17
Nodes (1): TestDatetime64DateOffsetArithmetic

### Community 811 - "Community 811"
Cohesion: 0.23
Nodes (2): Test PeriodIndex and Period Series Ops consistency, TestPeriodIndexSeriesMethods

### Community 812 - "Community 812"
Cohesion: 0.24
Nodes (5): ExtensionOpsMixin, ExtensionScalarOpsMixin, A base class for linking the operators to their dunder names.      .. note::, A mixin for defining ops on an ExtensionArray.      It is assumed that the under, A class method that returns a method that will correspond to an         operator

### Community 813 - "Community 813"
Cohesion: 0.17
Nodes (2): DataFrameNumericIndexing, DataFrameStringIndexing

### Community 814 - "Community 814"
Cohesion: 0.17
Nodes (5): Cat, Construction, Encode, Repeat, Slice

### Community 815 - "Community 815"
Cohesion: 0.17
Nodes (6): Contains, Dtypes, Dummies, Extract, Iter, Split

### Community 816 - "Community 816"
Cohesion: 0.17
Nodes (1): TestCategoricalIndexing

### Community 818 - "Community 818"
Cohesion: 0.18
Nodes (6): DeepChainMap, Get specifically scoped variables from a list of stack frames.          Paramete, Variant of ChainMap that allows direct updates to inner scopes.      Only works, Update the current scope by going back `level` levels.          Parameters, Return the full scope for use with passing to engines transparently         as a, Raises         ------         KeyError             If `key` doesn't exist.

### Community 819 - "Community 819"
Cohesion: 0.17
Nodes (1): TestSeriesConcat

### Community 820 - "Community 820"
Cohesion: 0.17
Nodes (2): Fixture returning DatetimeArray with parametrized timezones, TestReductions

### Community 821 - "Community 821"
Cohesion: 0.17
Nodes (1): TestDatetimeIndexTimezones

### Community 822 - "Community 822"
Cohesion: 0.17
Nodes (6): Book instance of class xlsxwriter.Workbook.          This attribute can be used, Save workbook to disk., converts a style_dict to an xlsxwriter format dict          Parameters         -, _XlsxStyler, XlsxWriter, ExcelWriter

### Community 823 - "Community 823"
Cohesion: 0.18
Nodes (1): TestIntervalArray

### Community 824 - "Community 824"
Cohesion: 0.17
Nodes (1): TestDataFrameQueryStrings

### Community 825 - "Community 825"
Cohesion: 0.17
Nodes (1): TestDataFrameUnaryOperators

### Community 826 - "Community 826"
Cohesion: 0.17
Nodes (3): CoercionBase, Object we will pass to `Series.replace`, TestReplaceSeriesCoercion

### Community 827 - "Community 827"
Cohesion: 0.17
Nodes (1): TestLocILocDataFrameCategorical

### Community 828 - "Community 828"
Cohesion: 0.17
Nodes (1): TestDataFrameSetItemWithExpansion

### Community 829 - "Community 829"
Cohesion: 0.17
Nodes (4): ReadSQLTable, ReadSQLTableDtypes, SQL, WriteSQLDtypes

### Community 830 - "Community 830"
Cohesion: 0.17
Nodes (7): mock_ctypes(), Give CheckCall a function that returns a falsey value and     mock get_errno so, Give CheckCall a function that returns a truthy value and     mock get_errno so, Mocks WinError to help with testing the clipboard., test_checked_call_with_bad_call(), test_checked_call_with_valid_call(), pandas_io_clipboard

### Community 831 - "Community 831"
Cohesion: 0.32
Nodes (11): _arrow_dtype_mapping(), _arrow_string_types_mapper(), arrow_table_to_pandas(), _maybe_convert_string_index_to_object(), _maybe_convert_string_to_object(), _normalize_pytz_timezone(), _normalize_timezone_dtypes(), _normalize_timezone_index() (+3 more)

### Community 832 - "Community 832"
Cohesion: 0.17
Nodes (12): json_normalize(), nested_to_record(), _normalize_json(), _normalize_json_ordered(), Main recursive function     Designed for the most basic use case of pd.json_norm, Order the top level keys and then recursively go to depth      Parameters     --, An optimized basic json_normalize      Converts a nested dict into a flat dict (, Validate that meta parameter contains only strings or lists of strings.     Para (+4 more)

### Community 833 - "Community 833"
Cohesion: 0.20
Nodes (8): compute_expected(), left_df(), Construct left test DataFrame with specified levels     (any of 'outer', 'inner', Construct right test DataFrame with specified levels     (any of 'outer', 'inner, Compute the expected merge result for the test case.      This method computes t, right_df(), test_merge_indexes_and_columns_lefton_righton(), test_merge_indexes_and_columns_on()

### Community 834 - "Community 834"
Cohesion: 0.17
Nodes (5): left(), left dataframe (not multi-indexed) for multi-index join tests, right dataframe (multi-indexed) for multi-index join tests, right(), TestMergeMultiIndexNaN

### Community 835 - "Community 835"
Cohesion: 0.17
Nodes (1): TestTimedeltaIndex

### Community 836 - "Community 836"
Cohesion: 0.17
Nodes (1): TestSeriesConvertDtypes

### Community 837 - "Community 837"
Cohesion: 0.17
Nodes (1): TestDatetimeIndexShift

### Community 838 - "Community 838"
Cohesion: 0.17
Nodes (1): TestSeriesSortIndex

### Community 839 - "Community 839"
Cohesion: 0.17
Nodes (1): TestDataFrameValues

### Community 840 - "Community 840"
Cohesion: 0.17
Nodes (1): TestRepr

### Community 841 - "Community 841"
Cohesion: 0.24
Nodes (3): TestLastWeekOfMonth, TestWeek, TestWeekOfMonth

### Community 842 - "Community 842"
Cohesion: 0.17
Nodes (1): TestS3

### Community 843 - "Community 843"
Cohesion: 0.17
Nodes (5): date_converter(), get_na_values(), converts col numbers to names, Infer types of values, possibly casting          Parameters         ----------, Get the NaN values for a given column.      Parameters     ----------     col :

### Community 844 - "Community 844"
Cohesion: 0.23
Nodes (2): numeric_as_float(), TestXport

### Community 845 - "Community 845"
Cohesion: 0.17
Nodes (1): TestTimedeltas

### Community 846 - "Community 846"
Cohesion: 0.20
Nodes (6): Holiday, Class that defines a holiday with start/end dates and rules for observance., Calculate holidays observed between start date and end date.          Dates are, Get reference dates for the holiday.          Return reference dates for the hol, Apply the given offset/observance to a DatetimeIndex of dates.          Paramete, Return a curve with holidays between start_date and end_date.          The holid

### Community 847 - "Community 847"
Cohesion: 0.18
Nodes (1): TestTimestampSeriesArithmetic

### Community 848 - "Community 848"
Cohesion: 0.18
Nodes (1): TestDatetimeArray

### Community 849 - "Community 849"
Cohesion: 0.18
Nodes (1): TestReshape

### Community 850 - "Community 850"
Cohesion: 0.18
Nodes (3): DataFrameAttributes, Dir, SeriesArrayAttribute

### Community 851 - "Community 851"
Cohesion: 0.18
Nodes (1): Constructor

### Community 852 - "Community 852"
Cohesion: 0.18
Nodes (2): Eval, Query

### Community 853 - "Community 853"
Cohesion: 0.18
Nodes (1): Range

### Community 854 - "Community 854"
Cohesion: 0.25
Nodes (4): Convert, FillNa, ReplaceDict, ReplaceList

### Community 855 - "Community 855"
Cohesion: 0.18
Nodes (1): TestTake

### Community 856 - "Community 856"
Cohesion: 0.18
Nodes (1): TestMath

### Community 857 - "Community 857"
Cohesion: 0.22
Nodes (4): Return elementwise ``self ^ other``.          Logical XOR for boolean operands,, Return elementwise ``self & other``.          Logical AND for boolean operands,, Return elementwise ``other & self``., Return elementwise ``self | other``.          Logical OR for boolean operands, b

### Community 858 - "Community 858"
Cohesion: 0.18
Nodes (1): TestDatetimeIndexRendering

### Community 859 - "Community 859"
Cohesion: 0.18
Nodes (1): TestGetLoc

### Community 860 - "Community 860"
Cohesion: 0.18
Nodes (1): TestJoin

### Community 861 - "Community 861"
Cohesion: 0.20
Nodes (2): TestBusinessDatetimeIndex, TestCustomDatetimeIndex

### Community 862 - "Community 862"
Cohesion: 0.18
Nodes (2): dateutil_parser, Tests column conversion functionality during parsing for all of the parsers defi

### Community 863 - "Community 863"
Cohesion: 0.24
Nodes (6): dateutil_tz_tz, _get_offset(), _offset(), test_apply_out_of_range(), test_compare_str(), test_offsets_compare_equal()

### Community 864 - "Community 864"
Cohesion: 0.18
Nodes (1): TestPeriodDtype

### Community 865 - "Community 865"
Cohesion: 0.18
Nodes (4): MockNumpyLikeArray, A class which is numpy-like (e.g. Pint's Quantity) but not actually numpy      T, test_is_array_like(), test_is_array_like_deprecate_non_pandas()

### Community 866 - "Community 866"
Cohesion: 0.18
Nodes (2): Tests for write_only mode (GH#41681)., TestWriteOnly

### Community 867 - "Community 867"
Cohesion: 0.18
Nodes (1): TestCategorical

### Community 868 - "Community 868"
Cohesion: 0.18
Nodes (1): TestDatetimeArray

### Community 870 - "Community 870"
Cohesion: 0.25
Nodes (2): Parameters:         -----------         formatter: EngFormatter under test, TestEngFormatter

### Community 871 - "Community 871"
Cohesion: 0.38
Nodes (5): has_doubly_truncated_repr(), has_expanded_repr(), has_horizontally_truncated_repr(), has_truncated_repr(), has_vertically_truncated_repr()

### Community 872 - "Community 872"
Cohesion: 0.18
Nodes (1): TestDataFrameLogicalOperators

### Community 873 - "Community 873"
Cohesion: 0.18
Nodes (3): Tests that apply to all groupby operation methods.  The only tests that should a, # TODO: min, max *should* handle, pandas_tests_groupby

### Community 875 - "Community 875"
Cohesion: 0.18
Nodes (2): Tests for groupby operations on SparseArray columns (GH#36123)., TestSparseGroupby

### Community 877 - "Community 877"
Cohesion: 0.18
Nodes (1): TestAtErrors

### Community 878 - "Community 878"
Cohesion: 0.29
Nodes (2): test coercion triggered by insert, TestInsertIndexCoercion

### Community 879 - "Community 879"
Cohesion: 0.18
Nodes (1): TestGet

### Community 880 - "Community 880"
Cohesion: 0.18
Nodes (1): TestSeriesGetitemSlices

### Community 881 - "Community 881"
Cohesion: 0.18
Nodes (1): TestDataFrameSetItemBooleanMask

### Community 882 - "Community 882"
Cohesion: 0.22
Nodes (5): _generate_dataframe(), ReadExcel, ReadExcelNRows, WriteExcel, WriteExcelStyled

### Community 883 - "Community 883"
Cohesion: 0.22
Nodes (8): add_mean(), Numba 1D mean kernels that can be shared by * Dataframe / Series * groupby * rol, remove_mean(), sliding_mean(), pandas_core_numba_kernels_mean, pandas_core_numba_kernels_min_max, pandas_core_numba_kernels_sum, pandas_core_numba_kernels_var

### Community 884 - "Community 884"
Cohesion: 0.25
Nodes (2): TestHelpFunctions, TestHelpFunctionsWithNans

### Community 885 - "Community 885"
Cohesion: 0.22
Nodes (6): Implement n largest/smallest for DataFrame      Parameters     ----------     ob, Helper function to determine if dtype is valid for         nsmallest/nlargest me, Implement n largest/smallest for Series      Parameters     ----------     obj :, SelectN, SelectNFrame, SelectNSeries

### Community 886 - "Community 886"
Cohesion: 0.18
Nodes (1): TestAtTime

### Community 887 - "Community 887"
Cohesion: 0.18
Nodes (1): TestBetweenTime

### Community 888 - "Community 888"
Cohesion: 0.18
Nodes (1): TestCombineFirst

### Community 890 - "Community 890"
Cohesion: 0.18
Nodes (1): TestNLargestNSmallest

### Community 891 - "Community 891"
Cohesion: 0.25
Nodes (1): TestQuantileExtensionDtype

### Community 892 - "Community 892"
Cohesion: 0.18
Nodes (1): TestSeriesSortIndexKey

### Community 893 - "Community 893"
Cohesion: 0.18
Nodes (1): TestDataFrameSortKey

### Community 894 - "Community 894"
Cohesion: 0.18
Nodes (1): TestSeriesValueCounts

### Community 895 - "Community 895"
Cohesion: 0.18
Nodes (1): TestGetIndexer

### Community 897 - "Community 897"
Cohesion: 0.18
Nodes (1): TestMultiIndexPartial

### Community 898 - "Community 898"
Cohesion: 0.20
Nodes (7): IndexType, This will assume that only strings are in object dtype     index.     (you shoul, The type class for Index objects., The type class for Series objects., SeriesType, typeof_index(), typeof_series()

### Community 899 - "Community 899"
Cohesion: 0.27
Nodes (4): TestMonthBegin, TestMonthEnd, TestSemiMonthBegin, TestSemiMonthEnd

### Community 900 - "Community 900"
Cohesion: 0.18
Nodes (1): Tests that duplicate columns are handled appropriately when parsed by the CSV en

### Community 901 - "Community 901"
Cohesion: 0.18
Nodes (1): TestPeriodIndex

### Community 902 - "Community 902"
Cohesion: 0.18
Nodes (1): TestGetIndexer

### Community 903 - "Community 903"
Cohesion: 0.18
Nodes (1): TestReductions

### Community 904 - "Community 904"
Cohesion: 0.18
Nodes (3): scripts, TestNoDefaultUsedNotOnlyForTyping, TestStringsWithWrongPlacedWhitespace

### Community 905 - "Community 905"
Cohesion: 0.18
Nodes (1): TestCategoricalRepr

### Community 906 - "Community 906"
Cohesion: 0.29
Nodes (3): SubclassedSeries, test_constructor_from_dict(), TestSeriesSubclassing

### Community 907 - "Community 907"
Cohesion: 0.18
Nodes (1): TestAstype

### Community 909 - "Community 909"
Cohesion: 0.24
Nodes (2): Foo, test_AbstractMethodError_classmethod()

### Community 910 - "Community 910"
Cohesion: 0.18
Nodes (1): TestReductions

### Community 911 - "Community 911"
Cohesion: 0.18
Nodes (1): TestTimestampClassMethodConstructors

### Community 912 - "Community 912"
Cohesion: 0.18
Nodes (1): TestTimestamp

### Community 913 - "Community 913"
Cohesion: 0.27
Nodes (11): _is_annual(), _is_monthly(), _is_quarterly(), is_subperiod(), is_superperiod(), _is_weekly(), _maybe_coerce_freq(), _quarter_months_conform() (+3 more)

### Community 914 - "Community 914"
Cohesion: 0.18
Nodes (1): TimedeltaConstructor

### Community 915 - "Community 915"
Cohesion: 0.18
Nodes (10): check_categorical(), check_dtype(), check_exact(), check_index_type(), Fixture returning `True` or `False`, determining whether to     compare floating, Fixture returning `True` or `False`, determining whether to check     if the `In, Fixture returning 0.5e-3 or 0.5e-5. Those values are used as relative tolerance., Fixture returning `True` or `False`, determining whether to     compare internal (+2 more)

### Community 916 - "Community 916"
Cohesion: 0.18
Nodes (6): new_func(), new_func_with_deprecation(), new_func_wrong_docstring(), This is the summary. The deprecate directive goes next.      This is the extende, Summary should be in the next line., This is the summary. The deprecate directive goes next.      .. deprecated:: 1.0

### Community 918 - "Community 918"
Cohesion: 0.18
Nodes (11): read_xml_iterparse(), test_attribute_centric_xml(), test_comment(), test_default_namespace(), test_dtd(), test_prefix_namespace(), test_processing_instruction(), test_repeat_elements() (+3 more)

### Community 919 - "Community 919"
Cohesion: 0.20
Nodes (1): TestCatAccessor

### Community 921 - "Community 921"
Cohesion: 0.20
Nodes (1): TestNumericArithmeticUnsorted

### Community 922 - "Community 922"
Cohesion: 0.20
Nodes (2): BaseCastingTests, Casting to and from ExtensionDtypes

### Community 923 - "Community 923"
Cohesion: 0.20
Nodes (2): BaseGroupbyTests, Groupby-specific tests.

### Community 924 - "Community 924"
Cohesion: 0.38
Nodes (2): BaseReduceTests, Reduction specific tests. Generally these only     make sense for numeric/boolea

### Community 925 - "Community 925"
Cohesion: 0.20
Nodes (1): TestToIterable

### Community 926 - "Community 926"
Cohesion: 0.20
Nodes (1): Ops2

### Community 927 - "Community 927"
Cohesion: 0.20
Nodes (1): IndexCache

### Community 928 - "Community 928"
Cohesion: 0.31
Nodes (4): MaskedNumericEngineIndexing, NumericEngineIndexing, ObjectEngineIndexing, Benchmarks in this file depend mostly on code in _libs/  We have to created mask

### Community 929 - "Community 929"
Cohesion: 0.24
Nodes (4): data(), left_array(), Fixture returning boolean array with valid and missing values., right_array()

### Community 932 - "Community 932"
Cohesion: 0.20
Nodes (1): TestCategoricalDtypes

### Community 933 - "Community 933"
Cohesion: 0.20
Nodes (1): TestCategoricalMissing

### Community 935 - "Community 935"
Cohesion: 0.24
Nodes (10): ensure_key_mapped(), _ensure_key_mapped_multiindex(), get_indexer_indexer(), lexsort_indexer(), nargsort(), Performs lexical sorting on a set of keys      Parameters     ----------     key, Intended to be a drop-in replacement for np.argsort which handles NaNs.      Add, Returns a new MultiIndex in which key has been applied     to all levels specifi (+2 more)

### Community 936 - "Community 936"
Cohesion: 0.29
Nodes (5): ctypes, ArrowArrayWrapper, ArrowStreamWrapper, test_dataframe_arrow_interface(), test_dataframe_from_arrow()

### Community 937 - "Community 937"
Cohesion: 0.29
Nodes (9): concat_compat(), _get_result_dtype(), _is_nonempty(), Utility functions related to concat., union_categoricals for concat(union_categories=True).      Unlike union_categori, Combine list-like of Categorical-like, unioning categories.      All categories, provide concatenation of an array of arrays each of which is a single     'norma, union_categoricals() (+1 more)

### Community 938 - "Community 938"
Cohesion: 0.20
Nodes (1): TestRoundTrip

### Community 940 - "Community 940"
Cohesion: 0.27
Nodes (6): fast_float, from_chars_to_status(), pd_strtoll(), pd_strtoull(), pd_strtoi, system_error

### Community 941 - "Community 941"
Cohesion: 0.20
Nodes (2): Dataframe with special characters for testing chars escaping., TestToLatexEscape

### Community 942 - "Community 942"
Cohesion: 0.20
Nodes (1): TestDataFrameToStringFormatters

### Community 943 - "Community 943"
Cohesion: 0.20
Nodes (1): TestFrameFlexComparisons

### Community 945 - "Community 945"
Cohesion: 0.20
Nodes (1): TestSelection

### Community 946 - "Community 946"
Cohesion: 0.20
Nodes (1): TestValidateIndices

### Community 947 - "Community 947"
Cohesion: 0.20
Nodes (1): TestLabelSlicing

### Community 948 - "Community 948"
Cohesion: 0.20
Nodes (1): TestLocBooleanMask

### Community 949 - "Community 949"
Cohesion: 0.20
Nodes (1): TestAtAndiAT

### Community 950 - "Community 950"
Cohesion: 0.20
Nodes (1): TestSetitemWithExpansion

### Community 951 - "Community 951"
Cohesion: 0.20
Nodes (1): TestDataFrameTake

### Community 952 - "Community 952"
Cohesion: 0.51
Nodes (9): buffer_to_ndarray(), categorical_column_to_series(), datetime_column_to_ndarray(), from_dataframe(), parse_datetime_format_str(), primitive_column_to_ndarray(), protocol_df_chunk_to_pandas(), set_nulls() (+1 more)

### Community 953 - "Community 953"
Cohesion: 0.20
Nodes (2): NA values are marked as False, TestOverlaps

### Community 954 - "Community 954"
Cohesion: 0.20
Nodes (1): TestIceberg

### Community 955 - "Community 955"
Cohesion: 0.20
Nodes (10): count_rows(), test_api_to_sql_append(), test_api_to_sql_replace(), test_delete_rows_success(), test_options_auto(), test_options_sqlalchemy(), test_to_sql(), test_to_sql_callable() (+2 more)

### Community 956 - "Community 956"
Cohesion: 0.20
Nodes (5): _check_cast(), IntegerArrayNoCopy, Check if all dtypes of df are equal to v, test_astype_to_string_dtype_not_modifying_input(), test_astype_to_string_not_modifying_input()

### Community 957 - "Community 957"
Cohesion: 0.20
Nodes (1): TestDataFrameRound

### Community 958 - "Community 958"
Cohesion: 0.20
Nodes (1): TestDatetimeIndexRound

### Community 959 - "Community 959"
Cohesion: 0.20
Nodes (1): TestSeriesRound

### Community 960 - "Community 960"
Cohesion: 0.20
Nodes (1): TestTimedeltaRound

### Community 962 - "Community 962"
Cohesion: 0.31
Nodes (1): TestSeriesToCSV

### Community 963 - "Community 963"
Cohesion: 0.27
Nodes (4): create_mock_series_weights(), create_mock_weights(), test_ewm_consistency_mean(), test_ewm_consistency_var_debiasing_factors()

### Community 965 - "Community 965"
Cohesion: 0.20
Nodes (1): TestGetLevelValues

### Community 968 - "Community 968"
Cohesion: 0.20
Nodes (1): TestSetOps

### Community 969 - "Community 969"
Cohesion: 0.29
Nodes (3): Tests for the following offsets: - BHalfYearBegin - BHalfYearEnd, TestBHalfYearBegin, TestBHalfYearEnd

### Community 970 - "Community 970"
Cohesion: 0.27
Nodes (3): Tests for the following offsets: - BQuarterBegin - BQuarterEnd, TestBQuarterBegin, TestBQuarterEnd

### Community 971 - "Community 971"
Cohesion: 0.29
Nodes (3): Tests for the following offsets: - HalfYearBegin - HalfYearEnd, TestHalfYearBegin, TestHalfYearEnd

### Community 972 - "Community 972"
Cohesion: 0.27
Nodes (3): Tests for the following offsets: - QuarterBegin - QuarterEnd, TestQuarterBegin, TestQuarterEnd

### Community 973 - "Community 973"
Cohesion: 0.20
Nodes (3): pandas_core_strings_accessor, any_allowed_skipna_inferred_dtype(), Fixture for all (inferred) dtypes allowed in StringMethods.__init__      The cov

### Community 974 - "Community 974"
Cohesion: 0.20
Nodes (1): TestGetItem

### Community 975 - "Community 975"
Cohesion: 0.22
Nodes (2): _permute(), TestPeriodIndex

### Community 976 - "Community 976"
Cohesion: 0.20
Nodes (1): TestGetStandardColors

### Community 977 - "Community 977"
Cohesion: 0.20
Nodes (1): TestRangeIndexConstructors

### Community 978 - "Community 978"
Cohesion: 0.33
Nodes (6): ArrowArrayWrapper, ArrowStreamWrapper, test_dataframe_from_arrow(), test_series_arrow_interface(), test_series_arrow_interface_arrow_dtypes(), test_series_arrow_interface_stringdtype()

### Community 979 - "Community 979"
Cohesion: 0.24
Nodes (6): _get_fill(), Create a 0-dim ndarray containing the fill value      Parameters     ----------, Perform a binary operation between two arrays.      Parameters     ----------, wrap op result to have correct dtype, _sparse_array_op(), _wrap_result()

### Community 980 - "Community 980"
Cohesion: 0.20
Nodes (2): Convert SparseArray to a NumPy array.          Returns         -------         a, Cumulative sum of non-NA/null values.          When performing the cumulative su

### Community 981 - "Community 981"
Cohesion: 0.20
Nodes (1): TestSparseArrayAnalytics

### Community 982 - "Community 982"
Cohesion: 0.20
Nodes (2): Tests for GH#56505 - fast path using PyArrow cast for int/bool., TestFromSequenceIntBool

### Community 983 - "Community 983"
Cohesion: 0.20
Nodes (2): Make sure non supported operations on Timedelta returns NonImplemented         a, TestTimedeltaComparison

### Community 984 - "Community 984"
Cohesion: 0.22
Nodes (10): combine_hash_arrays(), hash_array(), _hash_ndarray(), hash_pandas_object(), hash_tuples(), Hash a MultiIndex / listlike-of-tuples efficiently.      Parameters     --------, Given a 1d array, return an array of deterministic integers.      This function, See hash_array.__doc__. (+2 more)

### Community 985 - "Community 985"
Cohesion: 0.25
Nodes (8): compare_or_regex_search(), Methods used by Block.replace and related methods., Parameters     ----------     values : ArrayLike         Object dtype.     rx :, Decide whether to treat `to_replace` as a regular expression., Compare two array-like inputs of the same shape or two scalar values      Calls, # TODO: should use missing.mask_missing?, replace_regex(), should_use_regex()

### Community 986 - "Community 986"
Cohesion: 0.22
Nodes (1): TestGetIndexerNonUnique

### Community 987 - "Community 987"
Cohesion: 0.28
Nodes (3): Delegate, Delegator, TestPandasDelegate

### Community 988 - "Community 988"
Cohesion: 0.22
Nodes (1): Indexing

### Community 989 - "Community 989"
Cohesion: 0.22
Nodes (1): ToNumpy

### Community 990 - "Community 990"
Cohesion: 0.36
Nodes (2): Categories, MultipleCategories

### Community 991 - "Community 991"
Cohesion: 0.22
Nodes (1): Transform

### Community 992 - "Community 992"
Cohesion: 0.22
Nodes (1): ToDatetimeISO8601

### Community 995 - "Community 995"
Cohesion: 0.22
Nodes (1): TestAppend

### Community 996 - "Community 996"
Cohesion: 0.22
Nodes (1): TestGetIndexer

### Community 997 - "Community 997"
Cohesion: 0.39
Nodes (1): TestValueCounts

### Community 998 - "Community 998"
Cohesion: 0.22
Nodes (1): TestGenRangeGeneration

### Community 999 - "Community 999"
Cohesion: 0.22
Nodes (1): TestGetIndexer

### Community 1000 - "Community 1000"
Cohesion: 0.22
Nodes (3): Default NA value to use for this type.          This is used in e.g. ExtensionAr, ExtensionDtype that may be backed by more than one implementation., StorageExtensionDtype

### Community 1001 - "Community 1001"
Cohesion: 0.22
Nodes (7): Strict construction from a string, raise a TypeError if not         possible, attempt to construct this type from a string, raise a TypeError         if its n, Construct a SparseDtype from a string form.          Parameters         --------, Construct this type from a string.          Parameters         ----------, Construct a temporal ArrowDtype from string., Construct a CategoricalDtype from a string.          Parameters         --------, Construct a DatetimeTZDtype from a string.          Parameters         ---------

### Community 1002 - "Community 1002"
Cohesion: 0.22
Nodes (1): TestIsScalar

### Community 1003 - "Community 1003"
Cohesion: 0.22
Nodes (1): TestLibMissing

### Community 1004 - "Community 1004"
Cohesion: 0.22
Nodes (2): Various Series and DataFrame logical ops methods., TestLogicalOps

### Community 1005 - "Community 1005"
Cohesion: 0.28
Nodes (6): CapturingStringArray, Extend StringArray to capture arguments to __getitem__, test_ellipsis_index(), test_is_extension_array_dtype(), TestExtensionArrayDtype, pandas_core_dtypes

### Community 1006 - "Community 1006"
Cohesion: 0.22
Nodes (1): TestPeriodArray

### Community 1008 - "Community 1008"
Cohesion: 0.22
Nodes (8): _border_expander(), Utilities for interpreting CSS from Stylers for formatting non-HTML outputs., # TODO: Can we use current color as initial value to comply with CSS standards?, # TODO: Warn user if item entered more than once (e.g. "border: red green"), Wrapper to expand shorthand property into top, right, bottom, left properties, # TODO: support %, Wrapper to expand 'border' property into border color, style, and width properti, _side_expander()

### Community 1009 - "Community 1009"
Cohesion: 0.36
Nodes (5): MockEncoding, Used to add a side effect when accessing the 'encoding' property. If the     sid, test_detect_console_encoding_fallback_to_default(), test_detect_console_encoding_fallback_to_locale(), test_detect_console_encoding_from_stdout_stdin()

### Community 1010 - "Community 1010"
Cohesion: 0.22
Nodes (1): TestTimedelta64Formatter

### Community 1011 - "Community 1011"
Cohesion: 0.25
Nodes (2): test_adjoin(), TestFormatBase

### Community 1012 - "Community 1012"
Cohesion: 0.22
Nodes (4): df_short(), Short dataframe for testing table/tabular/longtable LaTeX env., TestToLatexBold, TestToLatexPosition

### Community 1013 - "Community 1013"
Cohesion: 0.25
Nodes (2): TestToStringNumericFormatting, _three_digit_exp()

### Community 1014 - "Community 1014"
Cohesion: 0.22
Nodes (2): DummyElement, test_frame_with_zero_len_series_corner_cases()

### Community 1015 - "Community 1015"
Cohesion: 0.22
Nodes (1): TestFrameComparisons

### Community 1016 - "Community 1016"
Cohesion: 0.22
Nodes (1): TestDataFrame

### Community 1017 - "Community 1017"
Cohesion: 0.22
Nodes (1): TestSeries

### Community 1018 - "Community 1018"
Cohesion: 0.39
Nodes (1): TestNumericOnly

### Community 1020 - "Community 1020"
Cohesion: 0.22
Nodes (2): # TODO: De-duplicate/parametrize, TestAtWithDuplicates

### Community 1021 - "Community 1021"
Cohesion: 0.22
Nodes (1): TestGetitem

### Community 1022 - "Community 1022"
Cohesion: 0.22
Nodes (1): TestLocListlike

### Community 1023 - "Community 1023"
Cohesion: 0.22
Nodes (1): TestXS

### Community 1024 - "Community 1024"
Cohesion: 0.22
Nodes (7): create_block_manager_from_blocks(), create_block_manager_from_column_arrays(), _form_blocks(), raise_construction_error(), raise a helpful message about our construction, _stack_arrays(), _tuples_to_blocks_no_consolidate()

### Community 1025 - "Community 1025"
Cohesion: 0.39
Nodes (1): TestGetDtypesCache

### Community 1026 - "Community 1026"
Cohesion: 0.22
Nodes (1): TestIntervalArithmetic

### Community 1027 - "Community 1027"
Cohesion: 0.22
Nodes (1): TestTableSchemaType

### Community 1028 - "Community 1028"
Cohesion: 0.22
Nodes (1): assert_json_roundtrip_equal()

### Community 1029 - "Community 1029"
Cohesion: 0.22
Nodes (1): TestPyObjectHashTableWithNans

### Community 1030 - "Community 1030"
Cohesion: 0.22
Nodes (1): # TODO: so, so many other variants of this...

### Community 1031 - "Community 1031"
Cohesion: 0.22
Nodes (9): create_subplots(), flatten_axes(), _get_layout(), handle_shared_axes(), _has_externally_shared_axis(), Create a figure with a set of subplots already made.      This utility wrapper m, Return whether an axis is externally shared.      Parameters     ----------, _remove_labels_from_axis() (+1 more)

### Community 1032 - "Community 1032"
Cohesion: 0.22
Nodes (1): TestPeriodIndex

### Community 1033 - "Community 1033"
Cohesion: 0.22
Nodes (1): TestFrameAsof

### Community 1034 - "Community 1034"
Cohesion: 0.22
Nodes (1): TestPeriodIndexAsType

### Community 1035 - "Community 1035"
Cohesion: 0.22
Nodes (1): TestSeriesDiff

### Community 1036 - "Community 1036"
Cohesion: 0.22
Nodes (1): TestDataFrameFilter

### Community 1037 - "Community 1037"
Cohesion: 0.22
Nodes (1): TestRepeat

### Community 1038 - "Community 1038"
Cohesion: 0.22
Nodes (1): TestSeriesSearchSorted

### Community 1039 - "Community 1039"
Cohesion: 0.22
Nodes (1): TestDataFrameSortIndexKey

### Community 1040 - "Community 1040"
Cohesion: 0.22
Nodes (1): # TODO: better name, de-duplicate with test_sort_index_level above

### Community 1041 - "Community 1041"
Cohesion: 0.25
Nodes (4): all_data(), create_dataframes(), create_series(), Test:         - Empty Series / DataFrame         - All NaN         - All consist

### Community 1044 - "Community 1044"
Cohesion: 0.31
Nodes (4): assert_multiindex_copied(), test_copy(), test_shallow_copy(), test_view()

### Community 1046 - "Community 1046"
Cohesion: 0.22
Nodes (1): TestMultiIndexSorted

### Community 1047 - "Community 1047"
Cohesion: 0.22
Nodes (1): TestAstype

### Community 1048 - "Community 1048"
Cohesion: 0.22
Nodes (1): TestGetLoc

### Community 1049 - "Community 1049"
Cohesion: 0.33
Nodes (2): TestJoinInt64Index, TestJoinUInt64Index

### Community 1050 - "Community 1050"
Cohesion: 0.22
Nodes (1): TestCustomBusinessDay

### Community 1051 - "Community 1051"
Cohesion: 0.42
Nodes (2): get_utc_offset_hours(), TestDST

### Community 1052 - "Community 1052"
Cohesion: 0.31
Nodes (8): kleene_and(), kleene_or(), kleene_xor(), raise_for_nan(), Ops for masked arrays., Boolean ``and`` using Kleene logic.      Values are ``NA`` for ``NA & NA`` or ``, Boolean ``or`` using Kleene logic.      Values are NA where we have ``NA | NA``, Boolean ``xor`` using Kleene logic.      This is the same as ``or``, with the fo

### Community 1053 - "Community 1053"
Cohesion: 0.22
Nodes (1): TestPeriodIndex

### Community 1054 - "Community 1054"
Cohesion: 0.22
Nodes (1): TestIteration

### Community 1055 - "Community 1055"
Cohesion: 0.25
Nodes (1): Get the location of the first fill value.          Returns         -------

### Community 1056 - "Community 1056"
Cohesion: 0.22
Nodes (1): TestGetitem

### Community 1057 - "Community 1057"
Cohesion: 0.22
Nodes (1): TestSorting

### Community 1058 - "Community 1058"
Cohesion: 0.22
Nodes (1): TestTimestampRendering

### Community 1059 - "Community 1059"
Cohesion: 0.22
Nodes (1): TestToDatetimeInferFormat

### Community 1060 - "Community 1060"
Cohesion: 0.22
Nodes (9): test_datetime_like(), test_numeric_dtypes(), test_period(), test_really_large_in_arr(), test_really_large_scalar(), test_scalar(), test_str(), test_timedelta() (+1 more)

### Community 1061 - "Community 1061"
Cohesion: 0.25
Nodes (6): Appender, indent(), A decorator to take a function's docstring and perform string     substitution o, Update self.params with supplied args., A function decorator that will append an addendum to the docstring     of the ta, Substitution

### Community 1062 - "Community 1062"
Cohesion: 0.22
Nodes (1): TestEngine

### Community 1063 - "Community 1063"
Cohesion: 0.22
Nodes (1): TestTableMethod

### Community 1064 - "Community 1064"
Cohesion: 0.25
Nodes (1): TestLambdaMangling

### Community 1065 - "Community 1065"
Cohesion: 0.25
Nodes (1): TestDatetime64SeriesComparison

### Community 1066 - "Community 1066"
Cohesion: 0.25
Nodes (1): TestNumericArraylikeArithmeticWithDatetimeLike

### Community 1067 - "Community 1067"
Cohesion: 0.39
Nodes (7): _cum_func(), cummax(), cummin(), cumprod(), cumsum(), masked_accumulations.py is for accumulation algorithms using a mask-based approa, Accumulations for 1D masked array.      We will modify values in place to replac

### Community 1068 - "Community 1068"
Cohesion: 0.39
Nodes (7): _nanquantile(), _nanquantile_1d(), quantile_compat(), quantile_with_mask(), Wrapper for np.quantile that skips missing values, specialized to     1-dimensio, Wrapper for np.quantile that skips missing values.      Parameters     ---------, Compute the quantiles of the given values for each quantile in `qs`.      Parame

### Community 1069 - "Community 1069"
Cohesion: 0.25
Nodes (4): Return an array and missing value suitable for factorization.          This meth, Encode the extension array as an enumerated type.          This method encodes t, Hook for hash_pandas_object.          Default is to use the values returned by _, Reconstruct an ExtensionArray after factorization.          This method reverses

### Community 1070 - "Community 1070"
Cohesion: 0.25
Nodes (8): generate_daily_offset_range(), _generate_range_overflow_safe(), _generate_range_overflow_safe_signed(), generate_regular_range(), Generate a range for offsets whose on-offset dates are a subset of a     daily g, Calculate the second endpoint for passing to np.arange, checking     to avoid an, A special case for _generate_range_overflow_safe where `periods * stride`     ca, Generate a range of dates or timestamps with the spans between dates     describ

### Community 1071 - "Community 1071"
Cohesion: 0.25
Nodes (5): Tests for DatetimeArray, # TODO: tests with td64, # TODO: merge this into tests/arithmetic/test_datetime64 once it is, # TODO: simplify once we can just .astype to other unit, TestDatetimeArrayComparisons

### Community 1072 - "Community 1072"
Cohesion: 0.25
Nodes (1): TestIndexConstructor

### Community 1073 - "Community 1073"
Cohesion: 0.39
Nodes (3): IndexArithmetic, IrregularOps, NumericInferOps

### Community 1074 - "Community 1074"
Cohesion: 0.25
Nodes (5): CategoricalComparisons, IntFrameWithScalar, # TODO: GH#33198 the setting here shouldn't need two steps, pandas_computation_expressions, pandas_core_computation_expressions

### Community 1075 - "Community 1075"
Cohesion: 0.25
Nodes (1): TimeLogicalOps

### Community 1076 - "Community 1076"
Cohesion: 0.25
Nodes (2): ToDatetimeFormat, ToDatetimeNONISO8601

### Community 1077 - "Community 1077"
Cohesion: 0.25
Nodes (1): ToDatetimeFromIntsFloats

### Community 1079 - "Community 1079"
Cohesion: 0.25
Nodes (1): TestCategoricalIndexingWithFactor

### Community 1080 - "Community 1080"
Cohesion: 0.25
Nodes (1): TestReindex

### Community 1081 - "Community 1081"
Cohesion: 0.25
Nodes (1): TestIndexConcat

### Community 1082 - "Community 1082"
Cohesion: 0.25
Nodes (1): TestConcatSort

### Community 1083 - "Community 1083"
Cohesion: 0.25
Nodes (8): can_set_locale(), get_locales(), Get all the locales that are available on the system.      Parameters     ------, Context manager for temporarily setting a locale.      Parameters     ----------, Check to see if we can set a locale, and subsequently get the locale,     withou, Return a list of normalized locales that do not throw an ``Exception``     when, set_locale(), _valid_locales()

### Community 1085 - "Community 1085"
Cohesion: 0.25
Nodes (8): Register a custom accessor on objects.      Parameters     ----------     name :, Register a custom accessor on DataFrame objects.      Use as a decorator to add, Register a custom accessor on Series objects.      Use as a decorator to add a c, Register a custom accessor on Index objects.      Use as a decorator to add a cu, _register_accessor(), register_dataframe_accessor(), register_index_accessor(), register_series_accessor()

### Community 1086 - "Community 1086"
Cohesion: 0.25
Nodes (1): TestTake

### Community 1087 - "Community 1087"
Cohesion: 0.25
Nodes (8): astype_array(), astype_array_safe(), astype_float_to_int_nansafe(), _astype_nansafe(), astype with a check preventing converting NaN to a meaningless integer value., Cast array (ndarray or ExtensionArray) to the new dtype.      Parameters     ---, Cast array (ndarray or ExtensionArray) to the new dtype.      This basically is, Cast the elements of an array to a given dtype a nan-safe manner.      Parameter

### Community 1088 - "Community 1088"
Cohesion: 0.25
Nodes (4): Check whether 'other' is equal to self.          By default, 'other' is consider, r"""         Construct this type from a string.          This is useful mainly f, Check if we match 'dtype'.          Parameters         ----------         dtype, Parameters         ----------         dtype : ExtensionDtype class or instance o

### Community 1089 - "Community 1089"
Cohesion: 0.25
Nodes (1): TestNumpyEADtype

### Community 1090 - "Community 1090"
Cohesion: 0.25
Nodes (4): test_find_result_type_datetime(), test_find_result_type_floats(), test_find_result_type_int_int(), test_find_result_type_uint_int()

### Community 1091 - "Community 1091"
Cohesion: 0.25
Nodes (1): TestNumberScalar

### Community 1092 - "Community 1092"
Cohesion: 0.32
Nodes (7): get_console_size(), in_interactive_session(), in_ipython_frontend(), Internal module for console introspection, Return console size as tuple = (width, height).      Returns (None,None) in non-, Check if we're running in an interactive shell.      Returns     -------     boo, Check if we're inside an IPython zmq frontend.      Returns     -------     bool

### Community 1093 - "Community 1093"
Cohesion: 0.29
Nodes (8): _parse_latex_cell_styles(), _parse_latex_css_conversion(), _parse_latex_header_span(), _parse_latex_options_strip(), r"""     Mutate the ``display_value`` string including LaTeX commands from ``lat, r"""     Refactor the cell `display_value` if a 'colspan' or 'rowspan' attribute, Strip a css_value which may have latex wrapping arguments, css comment identifie, Convert CSS (attribute,value) pairs to equivalent LaTeX (command,options) pairs.

### Community 1094 - "Community 1094"
Cohesion: 0.25
Nodes (1): TestDatetime64Formatter

### Community 1095 - "Community 1095"
Cohesion: 0.25
Nodes (1): TestAllowNonNano

### Community 1096 - "Community 1096"
Cohesion: 0.25
Nodes (1): TestCompat

### Community 1097 - "Community 1097"
Cohesion: 0.25
Nodes (1): TestGetGroup

### Community 1098 - "Community 1098"
Cohesion: 0.25
Nodes (2): # TODO: overlap with tests.series.test_ufunc.test_reductions, # TODO: do we have cases both with and without NAs?

### Community 1099 - "Community 1099"
Cohesion: 0.25
Nodes (1): TestAtSetItemWithExpansion

### Community 1100 - "Community 1100"
Cohesion: 0.25
Nodes (1): TestGetitemListLike

### Community 1101 - "Community 1101"
Cohesion: 0.25
Nodes (1): TestDataFrameInsert

### Community 1102 - "Community 1102"
Cohesion: 0.25
Nodes (4): Fixture to create a Series [(0, 1], (1, 2], (2, 3]], Fixture to get an interval (0.5, 1.5], Fixture to get a key 0, TestSetitemFloatIntervalWithIntIntervalValues

### Community 1103 - "Community 1103"
Cohesion: 0.25
Nodes (1): TestSetitemDT64Values

### Community 1104 - "Community 1104"
Cohesion: 0.25
Nodes (8): blockwise_all(), _get_same_shape_values(), _iter_block_pairs(), operate_blockwise(), Reset mgr_locs to correspond to our original DataFrame., Slice lblk.values to align with rblk.  Squeeze if we have EAs., Blockwise `all` reduction., _reset_block_mgr_locs()

### Community 1105 - "Community 1105"
Cohesion: 0.25
Nodes (3): 'encoding' shouldn't be passed to 'open' in binary mode.          GH 35058, bz2 and xz do not write the byte order mark (BOM) for utf-16/32.          https:, TestMMapWrapper

### Community 1106 - "Community 1106"
Cohesion: 0.54
Nodes (8): drop_view(), get_all_tables(), get_all_views(), mysql_pymysql_engine(), postgresql_adbc_conn(), postgresql_psycopg2_engine(), sqlite_adbc_conn(), sqlite_engine()

### Community 1107 - "Community 1107"
Cohesion: 0.39
Nodes (7): add_sum(), grouped_kahan_sum(), grouped_sum(), Numba 1D sum kernels that can be shared by * Dataframe / Series * groupby * roll, remove_sum(), sliding_sum(), numba_extending

### Community 1108 - "Community 1108"
Cohesion: 0.25
Nodes (1): TestHashTableUnsorted

### Community 1109 - "Community 1109"
Cohesion: 0.25
Nodes (4): data(), numpy_dtype(), Fixture returning parametrized 'data' array with different integer and     float, Fixture returning numpy dtype from 'data' input array.

### Community 1110 - "Community 1110"
Cohesion: 0.25
Nodes (1): TestSeriesArgsort

### Community 1111 - "Community 1111"
Cohesion: 0.25
Nodes (1): TestSeriesAsof

### Community 1112 - "Community 1112"
Cohesion: 0.25
Nodes (1): TestDropna

### Community 1113 - "Community 1113"
Cohesion: 0.25
Nodes (1): TestDataFrameDataTypes

### Community 1115 - "Community 1115"
Cohesion: 0.25
Nodes (1): TestTimedeltaIndexInsert

### Community 1116 - "Community 1116"
Cohesion: 0.25
Nodes (1): TestSeriesSortValues

### Community 1117 - "Community 1117"
Cohesion: 0.25
Nodes (1): TestTimestampToJulianDate

### Community 1118 - "Community 1118"
Cohesion: 0.25
Nodes (1): TestTimestampToPyDatetime

### Community 1119 - "Community 1119"
Cohesion: 0.25
Nodes (1): TestDataFrameTruncate

### Community 1120 - "Community 1120"
Cohesion: 0.25
Nodes (1): TestUnique

### Community 1121 - "Community 1121"
Cohesion: 0.25
Nodes (1): TestContains

### Community 1122 - "Community 1122"
Cohesion: 0.25
Nodes (1): TestMixedResolutionDatetime64

### Community 1123 - "Community 1123"
Cohesion: 0.29
Nodes (3): TestBYearBegin, TestBYearEnd, TestBYearEndLagged

### Community 1124 - "Community 1124"
Cohesion: 0.32
Nodes (7): dispatch_fill_zeros(), _fill_zeros(), mask_zero_div_zero(), Missing data handling for arithmetic operations.  In particular, pandas conventi, Call _fill_zeros with the appropriate fill value depending on the operation,, If this is a reversed op, then flip x,y      If we have an integer value (or arr, Set results of  0 // 0 to np.nan, regardless of the dtypes     of the numerator

### Community 1125 - "Community 1125"
Cohesion: 0.25
Nodes (1): TestTake

### Community 1126 - "Community 1126"
Cohesion: 0.25
Nodes (1): TestSeriesFlexComparison

### Community 1129 - "Community 1129"
Cohesion: 0.25
Nodes (1): TestReprBase

### Community 1130 - "Community 1130"
Cohesion: 0.25
Nodes (1): TestTimestampConstructorFoldKeyword

### Community 1131 - "Community 1131"
Cohesion: 0.25
Nodes (3): TimeGetDateField, TimeGetStartEndField, TimeGetTimedeltaField

### Community 1132 - "Community 1132"
Cohesion: 0.25
Nodes (8): _get_commit_hash(), _get_dependency_info(), _get_sys_info(), Use vendored versioneer code to get git hash, which handles     git worktree cor, Returns system information as a JSON serializable dictionary., Returns dependency information as a JSON serializable dictionary., Provide useful information, important for bug reports.      It comprises info ab, show_versions()

### Community 1134 - "Community 1134"
Cohesion: 0.25
Nodes (1): TestExpanding

### Community 1136 - "Community 1136"
Cohesion: 0.29
Nodes (1): TestPeriodIndexComparisons

### Community 1137 - "Community 1137"
Cohesion: 0.29
Nodes (3): assert_dtype(), get_expected_name(), Helper to check the dtype for a Series, Index, or single-column DataFrame.

### Community 1138 - "Community 1138"
Cohesion: 0.43
Nodes (6): _cum_func(), cummax(), cummin(), cumsum(), datetimelke_accumulations.py is for accumulations of datetimelike extension arra, Accumulations for 1D datetimelike arrays.      Parameters     ----------     fun

### Community 1139 - "Community 1139"
Cohesion: 0.43
Nodes (3): Autosummary, PandasAutosummary, This alternative autosummary class lets us override the table summary for     Se

### Community 1140 - "Community 1140"
Cohesion: 0.29
Nodes (1): TestIndexRendering

### Community 1141 - "Community 1141"
Cohesion: 0.29
Nodes (2): BasePrintingTests, Tests checking the formatting of your EA when printed.

### Community 1142 - "Community 1142"
Cohesion: 0.33
Nodes (3): BaseIndexer, PrescribedWindowIndexer, TestMinMaxNumba

### Community 1143 - "Community 1143"
Cohesion: 0.29
Nodes (3): ApplyIndex, BinaryOpsMultiIndex, TimedeltaOps

### Community 1144 - "Community 1144"
Cohesion: 0.29
Nodes (1): Concat

### Community 1145 - "Community 1145"
Cohesion: 0.29
Nodes (1): Rank

### Community 1146 - "Community 1146"
Cohesion: 0.29
Nodes (1): Apply

### Community 1147 - "Community 1147"
Cohesion: 0.29
Nodes (1): Equals

### Community 1148 - "Community 1148"
Cohesion: 0.29
Nodes (1): Nth

### Community 1149 - "Community 1149"
Cohesion: 0.29
Nodes (2): Concat, ConcatIndexDtype

### Community 1150 - "Community 1150"
Cohesion: 0.29
Nodes (1): MergeAsof

### Community 1151 - "Community 1151"
Cohesion: 0.29
Nodes (1): Merge

### Community 1152 - "Community 1152"
Cohesion: 0.48
Nodes (3): Categorical, SubclassedCategorical, TestCategoricalSubclassing

### Community 1153 - "Community 1153"
Cohesion: 0.29
Nodes (1): TestPeriodConcat

### Community 1154 - "Community 1154"
Cohesion: 0.29
Nodes (2): pandas._config is considered explicitly upstream of everything else in pandas, s, pandas_config_display

### Community 1156 - "Community 1156"
Cohesion: 0.29
Nodes (1): TestDatetimeArrayConstructor

### Community 1157 - "Community 1157"
Cohesion: 0.29
Nodes (1): TestWhere

### Community 1158 - "Community 1158"
Cohesion: 0.29
Nodes (1): TestDatetimeIndexIteration

### Community 1159 - "Community 1159"
Cohesion: 0.29
Nodes (5): Register an ExtensionType with pandas as class decorator.      This enables oper, Registry for dtype inference.      The registry allows one to map a string repr, Parameters         ----------         dtype : ExtensionDtype class, register_extension_dtype(), Registry

### Community 1160 - "Community 1160"
Cohesion: 0.52
Nodes (1): TestNAObj

### Community 1162 - "Community 1162"
Cohesion: 0.29
Nodes (1): get_exp_unit()

### Community 1163 - "Community 1163"
Cohesion: 0.29
Nodes (6): _require_timezone_database(), test_dt_day_month_name(), test_dt_strftime(), test_dt_tz_localize(), test_dt_tz_localize_none(), test_dt_tz_localize_nonexistent()

### Community 1164 - "Community 1164"
Cohesion: 0.29
Nodes (1): TestFloatArrayFormatter

### Community 1165 - "Community 1165"
Cohesion: 0.29
Nodes (1): TestHTMLIndex

### Community 1166 - "Community 1166"
Cohesion: 0.29
Nodes (1): TestToLatexHeader

### Community 1167 - "Community 1167"
Cohesion: 0.29
Nodes (1): TestDataFrameCumulativeOps

### Community 1168 - "Community 1168"
Cohesion: 0.29
Nodes (1): _check_colors_box()

### Community 1169 - "Community 1169"
Cohesion: 0.29
Nodes (4): assert_stat_op_calc(), make_skipna_wrapper(), Check that operator opname works as advertised on frame      Parameters     ----, Create a function for calling on an array.      Parameters     ----------     al

### Community 1170 - "Community 1170"
Cohesion: 0.29
Nodes (1): TestContains

### Community 1171 - "Community 1171"
Cohesion: 0.29
Nodes (1): TestILocSeries

### Community 1172 - "Community 1172"
Cohesion: 0.33
Nodes (7): _check_values_indices_shape_match(), _ensure_2d(), _get_axes(), ndarray_to_mgr(), _prep_ndarraylike(), Check that the shape implied by our axes matches the actual shape of the     dat, Reshape 1D values, raise on anything else other than 2D.

### Community 1174 - "Community 1174"
Cohesion: 0.29
Nodes (1): TestMethods

### Community 1175 - "Community 1175"
Cohesion: 0.29
Nodes (1): ToJSONLines

### Community 1176 - "Community 1176"
Cohesion: 0.38
Nodes (1): TestCompression

### Community 1177 - "Community 1177"
Cohesion: 0.29
Nodes (7): as_json_table_type(), build_table_schema(), convert_pandas_type_to_json_field(), Sets index names to 'index' for regular, or 'level_x' for Multi, Create a Table schema from ``data``.      This method is a utility to generate a, Convert a NumPy / pandas type to its corresponding json_table.      Parameters, set_default_names()

### Community 1178 - "Community 1178"
Cohesion: 0.33
Nodes (5): bisect_left(), Numba 1D min/max kernels that can be shared by * Dataframe / Series * groupby *, Same as https://docs.python.org/3/library/bisect.html; not in numba yet!, sliding_min_max(), numba

### Community 1179 - "Community 1179"
Cohesion: 0.43
Nodes (6): add_var(), grouped_var(), Numba 1D var kernels that can be shared by * Dataframe / Series * groupby * roll, remove_var(), sliding_var(), pandas_core_numba_kernels_shared

### Community 1180 - "Community 1180"
Cohesion: 0.29
Nodes (4): test_pyobject_hashtable_map_locations_refcount(), test_pyobject_hashtable_set_item_refcount(), test_pyobject_hashtable_unique_refcount(), _WeakRefKey

### Community 1181 - "Community 1181"
Cohesion: 0.29
Nodes (1): TestInfinity

### Community 1182 - "Community 1182"
Cohesion: 0.29
Nodes (3): data(), Length-10 ListArray for semantics test., pandas_tests_extension_list_array

### Community 1183 - "Community 1183"
Cohesion: 0.29
Nodes (1): TestCombine

### Community 1184 - "Community 1184"
Cohesion: 0.29
Nodes (1): TestDatetimeIndexFactorize

### Community 1185 - "Community 1185"
Cohesion: 0.29
Nodes (6): expected_dtype(), test_rank_average_pct(), test_rank_dense_pct(), test_rank_first_pct(), test_rank_max_pct(), test_rank_min_pct()

### Community 1186 - "Community 1186"
Cohesion: 0.29
Nodes (1): TestPeriodIndexShift

### Community 1187 - "Community 1187"
Cohesion: 0.29
Nodes (1): TestTimedeltaIndexShift

### Community 1188 - "Community 1188"
Cohesion: 0.29
Nodes (1): TestSeriesSortingKey

### Community 1189 - "Community 1189"
Cohesion: 0.29
Nodes (1): TestDateTimeIndexToJulianDate

### Community 1191 - "Community 1191"
Cohesion: 0.29
Nodes (1): TestSliceLocs

### Community 1195 - "Community 1195"
Cohesion: 0.29
Nodes (1): TestCartesianProduct

### Community 1196 - "Community 1196"
Cohesion: 0.29
Nodes (4): generate_shared_aggregator(), # TODO: Preserve complex dtypes, Generate a Numba function that loops over the columns 2D object and applies, # TODO: Optimize this

### Community 1197 - "Community 1197"
Cohesion: 0.29
Nodes (5): ILocModel, IlocType, IndexModel, SeriesModel, typeof_iloc()

### Community 1198 - "Community 1198"
Cohesion: 0.29
Nodes (4): pandas_libs_tslib, ipython analogue:  tr = TimeIntsToPydatetime() mi = pd.MultiIndex.from_product(, # TODO: fold?, TimeIntsToPydatetime

### Community 1199 - "Community 1199"
Cohesion: 0.29
Nodes (1): TestUnsupportedFeatures

### Community 1200 - "Community 1200"
Cohesion: 0.29
Nodes (1): TestPeriodComparisons

### Community 1201 - "Community 1201"
Cohesion: 0.29
Nodes (1): TestGetIndexer

### Community 1202 - "Community 1202"
Cohesion: 0.29
Nodes (1): TestGetLoc

### Community 1203 - "Community 1203"
Cohesion: 0.29
Nodes (1): TestPeriodRangeKeywords

### Community 1204 - "Community 1204"
Cohesion: 0.29
Nodes (1): TestRegistration

### Community 1205 - "Community 1205"
Cohesion: 0.29
Nodes (7): Series with date range index and random data for test purposes., simple_date_range_series(), test_corner_cases_date(), test_how_lambda_functions(), test_resample_anchored_intraday3(), test_resample_anchored_monthstart(), test_resample_timestamp_to_period()

### Community 1206 - "Community 1206"
Cohesion: 0.29
Nodes (1): TestSAS7BDAT

### Community 1207 - "Community 1207"
Cohesion: 0.38
Nodes (5): bench(), bench_subset(), bench_with(), seaborn, timeit

### Community 1208 - "Community 1208"
Cohesion: 0.29
Nodes (1): TestSeriesFlexArithmetic

### Community 1209 - "Community 1209"
Cohesion: 0.29
Nodes (7): _check_is_partition(), _levels_to_axis(), Convert a sparse Series to a scipy.sparse.coo_matrix using index     levels row_, For a MultiIndexed sparse Series `ss`, return `ax_coords` and `ax_labels`,     w, For an arbitrary MultiIndexed sparse Series return (v, i, j, ilabels,     jlabel, sparse_series_to_coo(), _to_ijv()

### Community 1211 - "Community 1211"
Cohesion: 0.29
Nodes (1): TestDuplicated

### Community 1212 - "Community 1212"
Cohesion: 0.29
Nodes (1): TestRank

### Community 1213 - "Community 1213"
Cohesion: 0.29
Nodes (1): TestIsMonotonic

### Community 1214 - "Community 1214"
Cohesion: 0.29
Nodes (1): TestRandomState

### Community 1215 - "Community 1215"
Cohesion: 0.29
Nodes (1): TestExtensionTake

### Community 1216 - "Community 1216"
Cohesion: 0.29
Nodes (1): TestVectorizedTimedelta

### Community 1217 - "Community 1217"
Cohesion: 0.29
Nodes (1): TestTimestampConstructorPositionalAndKeywordSupport

### Community 1218 - "Community 1218"
Cohesion: 0.29
Nodes (1): TestDatetimeParsingWrappers

### Community 1219 - "Community 1219"
Cohesion: 0.29
Nodes (2): Tests for ArrowExtensionArray._hash_pandas_object (GH#48964)., TestHashArrow

### Community 1223 - "Community 1223"
Cohesion: 0.29
Nodes (1): TestEWM

### Community 1225 - "Community 1225"
Cohesion: 0.33
Nodes (1): TestDatetime64ArrayLikeComparisons

### Community 1226 - "Community 1226"
Cohesion: 0.33
Nodes (1): TestPeriodArrayLikeComparisons

### Community 1227 - "Community 1227"
Cohesion: 0.33
Nodes (1): TestTimedelta64ArrayLikeComparisons

### Community 1228 - "Community 1228"
Cohesion: 0.33
Nodes (3): Set the ordered attribute to the boolean value.          Parameters         ----, Set the Categorical to be ordered.          This method returns a new Categorica, Set the Categorical to be unordered.          This method returns a new Categori

### Community 1229 - "Community 1229"
Cohesion: 0.33
Nodes (3): Remove the specified categories.          The ``removals`` argument must be a su, Remove categories which are not used.          This method is useful when workin, Return the ``Categorical`` which ``categories`` and ``codes`` are         unique

### Community 1230 - "Community 1230"
Cohesion: 0.33
Nodes (1): TestEmpty

### Community 1231 - "Community 1231"
Cohesion: 0.33
Nodes (3): BaseIndexTests, Tests for Indexes backed by arbitrary ExtensionArrays., Tests for Index object backed by an ExtensionArray

### Community 1232 - "Community 1232"
Cohesion: 0.33
Nodes (1): Ops

### Community 1233 - "Community 1233"
Cohesion: 0.33
Nodes (1): Timeseries

### Community 1234 - "Community 1234"
Cohesion: 0.33
Nodes (1): CategoricalSlicing

### Community 1235 - "Community 1235"
Cohesion: 0.33
Nodes (1): Reindex

### Community 1236 - "Community 1236"
Cohesion: 0.33
Nodes (1): Rename

### Community 1237 - "Community 1237"
Cohesion: 0.53
Nodes (2): AggEngine, TransformEngine

### Community 1238 - "Community 1238"
Cohesion: 0.33
Nodes (1): Apply

### Community 1239 - "Community 1239"
Cohesion: 0.47
Nodes (5): GroupByCythonAgg, GroupByCythonAggEaDtypes, GroupByNumbaAgg, Benchmarks specifically targeting our cython aggregation algorithms     (using a, Benchmarks specifically targeting our numba aggregation algorithms     (using a

### Community 1240 - "Community 1240"
Cohesion: 0.33
Nodes (1): InsertColumns

### Community 1241 - "Community 1241"
Cohesion: 0.33
Nodes (1): ToDatetimeCache

### Community 1242 - "Community 1242"
Cohesion: 0.33
Nodes (1): Join

### Community 1243 - "Community 1243"
Cohesion: 0.33
Nodes (2): MergeRangeLikeFastPath, Benchmarks for merge(sort=False) where one side is unsorted and the other     si

### Community 1244 - "Community 1244"
Cohesion: 0.33
Nodes (1): TestCategoricalIndex2

### Community 1245 - "Community 1245"
Cohesion: 0.33
Nodes (1): TestCategoricalIndexConstructors

### Community 1246 - "Community 1246"
Cohesion: 0.33
Nodes (1): TestEquals

### Community 1247 - "Community 1247"
Cohesion: 0.33
Nodes (1): TestContains

### Community 1248 - "Community 1248"
Cohesion: 0.33
Nodes (1): TestGetLoc

### Community 1250 - "Community 1250"
Cohesion: 0.33
Nodes (3): loads(), Analogous to pickle._loads., Unpickler

### Community 1251 - "Community 1251"
Cohesion: 0.33
Nodes (5): Add a temporary variable to the scope.          Parameters         ----------, Replace a number with its hexadecimal representation. Used to tag     temporary, Return the padded hexadecimal id of ``obj``., _raw_hex_id(), _replacer()

### Community 1252 - "Community 1252"
Cohesion: 0.33
Nodes (4): check_bool_indexer(), Convert indexing key into something we can use to do actual fancy         indexi, Much simpler as we only have to deal with our valid types., Check if key is a valid boolean indexer for an object with such index and     pe

### Community 1253 - "Community 1253"
Cohesion: 0.47
Nodes (3): DataFrame, A subclass of DataFrame that does not define a constructor., SimpleDataFrameSubClass

### Community 1254 - "Community 1254"
Cohesion: 0.33
Nodes (1): TestDatetimeIndexArithmetic

### Community 1255 - "Community 1255"
Cohesion: 0.33
Nodes (1): TestGetItem

### Community 1256 - "Community 1256"
Cohesion: 0.33
Nodes (1): TestPickle

### Community 1257 - "Community 1257"
Cohesion: 0.33
Nodes (2): DecimalDtype, Return the array type associated with this dtype.          Returns         -----

### Community 1259 - "Community 1259"
Cohesion: 0.33
Nodes (1): TestTableSchemaRepr

### Community 1260 - "Community 1260"
Cohesion: 0.33
Nodes (1): TestDataFrameToStringLineWidth

### Community 1261 - "Community 1261"
Cohesion: 0.33
Nodes (1): TestEmptyDataFrameReductions

### Community 1262 - "Community 1262"
Cohesion: 0.53
Nodes (4): A subclass of Series that does not define a constructor., SimpleSeriesSubClass, TestSubclassWithoutConstructor, Series

### Community 1263 - "Community 1263"
Cohesion: 0.40
Nodes (2): MySubclassWithMetadata, test_constructor_with_metadata()

### Community 1264 - "Community 1264"
Cohesion: 0.47
Nodes (2): TestDataFrameToXArray, TestSeriesToXArray

### Community 1265 - "Community 1265"
Cohesion: 0.33
Nodes (1): Tests of the groupby API, including internal consistency and with other pandas o

### Community 1266 - "Community 1266"
Cohesion: 0.33
Nodes (1): TestGroupVar

### Community 1267 - "Community 1267"
Cohesion: 0.33
Nodes (1): TestEngine

### Community 1268 - "Community 1268"
Cohesion: 0.33
Nodes (1): TestIndexing

### Community 1269 - "Community 1269"
Cohesion: 0.33
Nodes (1): TestSeriesGetitemListLike

### Community 1270 - "Community 1270"
Cohesion: 0.60
Nodes (1): TestSetitemValidation

### Community 1271 - "Community 1271"
Cohesion: 0.53
Nodes (1): TestLocWithEllipsis

### Community 1272 - "Community 1272"
Cohesion: 0.33
Nodes (1): TestPartialStringSlicing

### Community 1273 - "Community 1273"
Cohesion: 0.47
Nodes (3): generate_indices(), generate the indices     if values is True , use the axis values     is False, u, TestScalar

### Community 1274 - "Community 1274"
Cohesion: 0.33
Nodes (1): TestSetitemSlices

### Community 1275 - "Community 1275"
Cohesion: 0.33
Nodes (1): TestSetitemTZAwareValues

### Community 1277 - "Community 1277"
Cohesion: 0.33
Nodes (3): Insert item at selected position.          Parameters         ----------, When inserting a new Block at location 'loc', we increment         all of the mg, When inserting a new Block at location 'loc', we update our         _blklocs and

### Community 1278 - "Community 1278"
Cohesion: 0.33
Nodes (1): TestContains

### Community 1279 - "Community 1279"
Cohesion: 0.33
Nodes (1): TestInterval

### Community 1281 - "Community 1281"
Cohesion: 0.33
Nodes (4): Benchmark for the parallel read_csv path (C engine, large local files).      The, File-path read: takes the parallel path for large files., BytesIO read: always serial (parallel path requires a file path)., ReadCSVParallelLargeFile

### Community 1282 - "Community 1282"
Cohesion: 0.33
Nodes (1): Pickle

### Community 1283 - "Community 1283"
Cohesion: 0.33
Nodes (6): create_and_load_types(), mysql_pymysql_engine_types(), postgresql_psycopg2_engine_types(), sqlite_engine_types(), sqlite_str_types(), types_table_metadata()

### Community 1284 - "Community 1284"
Cohesion: 0.53
Nodes (4): activated_tracemalloc(), get_allocated_khash_memory(), test_tracemalloc_for_empty_StringHashTable(), test_tracemalloc_works_for_StringHashTable()

### Community 1285 - "Community 1285"
Cohesion: 0.33
Nodes (1): TestAssign

### Community 1286 - "Community 1286"
Cohesion: 0.33
Nodes (1): TestBetween

### Community 1287 - "Community 1287"
Cohesion: 0.33
Nodes (1): TestCopy

### Community 1288 - "Community 1288"
Cohesion: 0.33
Nodes (1): TestEquals

### Community 1289 - "Community 1289"
Cohesion: 0.33
Nodes (1): TestFirstValidIndex

### Community 1290 - "Community 1290"
Cohesion: 0.33
Nodes (1): TestInferObjects

### Community 1291 - "Community 1291"
Cohesion: 0.33
Nodes (1): TestMap

### Community 1292 - "Community 1292"
Cohesion: 0.33
Nodes (1): TestDataFramePctChange

### Community 1293 - "Community 1293"
Cohesion: 0.33
Nodes (1): TestReindexSetIndex

### Community 1294 - "Community 1294"
Cohesion: 0.33
Nodes (1): TestDataFrameRenameAxis

### Community 1295 - "Community 1295"
Cohesion: 0.33
Nodes (1): TestDataFrameReplaceRegex

### Community 1296 - "Community 1296"
Cohesion: 0.33
Nodes (1): TestToFrame

### Community 1297 - "Community 1297"
Cohesion: 0.33
Nodes (1): TestToNumpy

### Community 1298 - "Community 1298"
Cohesion: 0.33
Nodes (1): TestUpdate

### Community 1299 - "Community 1299"
Cohesion: 0.33
Nodes (1): TestSliceLocs

### Community 1300 - "Community 1300"
Cohesion: 0.47
Nodes (2): TestBMonthBegin, TestBMonthEnd

### Community 1301 - "Community 1301"
Cohesion: 0.53
Nodes (3): TestYearBegin, TestYearEnd, TestYearEndDiffMonth

### Community 1302 - "Community 1302"
Cohesion: 0.33
Nodes (1): TestPeriodIndexDisallowedFreqs

### Community 1303 - "Community 1303"
Cohesion: 0.33
Nodes (1): TestJoin

### Community 1304 - "Community 1304"
Cohesion: 0.33
Nodes (1): TestPeriodRangeDisallowedFreqs

### Community 1305 - "Community 1305"
Cohesion: 0.33
Nodes (2): A group of tests which covers reading HDF5 files written by plain PyTables     (, TestReadPyTablesHDF5

### Community 1306 - "Community 1306"
Cohesion: 0.33
Nodes (3): Max of array values, ignoring NA values if specified.          Parameters, Min of array values, ignoring NA values if specified.          Parameters, Min/max of non-NA/null values          Parameters         ----------         kin

### Community 1307 - "Community 1307"
Cohesion: 0.33
Nodes (1): TestIsna

### Community 1308 - "Community 1308"
Cohesion: 0.33
Nodes (1): TestMinMax

### Community 1311 - "Community 1311"
Cohesion: 0.33
Nodes (1): TestIsBoolIndexer

### Community 1312 - "Community 1312"
Cohesion: 0.33
Nodes (1): TestFlags

### Community 1313 - "Community 1313"
Cohesion: 0.33
Nodes (1): TestMerge

### Community 1315 - "Community 1315"
Cohesion: 0.33
Nodes (6): _coerce_scalar_to_timedelta_type(), _convert_listlike(), Convert string 'r' to a timedelta object., Convert a list of objects to a timedelta index object., Convert argument to timedelta.      Timedeltas are absolute differences in times, to_timedelta()

### Community 1317 - "Community 1317"
Cohesion: 0.33
Nodes (1): TestAstypeOverflowSafe

### Community 1319 - "Community 1319"
Cohesion: 0.33
Nodes (1): TestArrayStrptimeResolutionInference

### Community 1320 - "Community 1320"
Cohesion: 0.33
Nodes (1): TimedeltaProperties

### Community 1321 - "Community 1321"
Cohesion: 0.40
Nodes (2): PrescribedWindowIndexer, TestMinMax

### Community 1322 - "Community 1322"
Cohesion: 0.40
Nodes (2): pandas_core_internals_api, pandas_core_internals_concat

### Community 1323 - "Community 1323"
Cohesion: 0.40
Nodes (3): MockExecutionEngine, Execution Engine to test if the execution engine interface receives and     uses, BaseExecutionEngine

### Community 1324 - "Community 1324"
Cohesion: 0.40
Nodes (1): TestDatetime64OverflowHandling

### Community 1325 - "Community 1325"
Cohesion: 0.40
Nodes (1): TestNumericComparisons

### Community 1326 - "Community 1326"
Cohesion: 0.40
Nodes (1): TestUFuncCompat

### Community 1327 - "Community 1327"
Cohesion: 0.60
Nodes (2): MyIndex, test_index_ops_defer_to_unknown_subclasses()

### Community 1328 - "Community 1328"
Cohesion: 0.40
Nodes (1): TestObjectComparisons

### Community 1329 - "Community 1329"
Cohesion: 0.60
Nodes (1): Formatting function for scalar values.          This is used in the default '__r

### Community 1330 - "Community 1330"
Cohesion: 0.40
Nodes (1): TestUnaryOps

### Community 1331 - "Community 1331"
Cohesion: 0.60
Nodes (2): BaseAccumulateTests, Accumulation specific tests. Generally these only     make sense for numeric/boo

### Community 1332 - "Community 1332"
Cohesion: 0.40
Nodes (1): TestWhere

### Community 1333 - "Community 1333"
Cohesion: 0.60
Nodes (2): constructor(), TestConstruction

### Community 1334 - "Community 1334"
Cohesion: 0.40
Nodes (1): DateInferOps

### Community 1335 - "Community 1335"
Cohesion: 0.40
Nodes (1): AsType

### Community 1336 - "Community 1336"
Cohesion: 0.40
Nodes (1): IsMonotonic

### Community 1337 - "Community 1337"
Cohesion: 0.40
Nodes (1): Isnull

### Community 1338 - "Community 1338"
Cohesion: 0.40
Nodes (1): NSort

### Community 1339 - "Community 1339"
Cohesion: 0.40
Nodes (1): Repr

### Community 1340 - "Community 1340"
Cohesion: 0.40
Nodes (1): Round

### Community 1341 - "Community 1341"
Cohesion: 0.40
Nodes (1): Fillna

### Community 1342 - "Community 1342"
Cohesion: 0.40
Nodes (1): MergeCategoricals

### Community 1343 - "Community 1343"
Cohesion: 0.40
Nodes (2): data(), Fixture returning boolean array, with valid and missing values.

### Community 1344 - "Community 1344"
Cohesion: 0.40
Nodes (1): TestFillNA

### Community 1345 - "Community 1345"
Cohesion: 0.40
Nodes (1): TestCategoricalSort

### Community 1346 - "Community 1346"
Cohesion: 0.50
Nodes (5): _align_core(), _align_core_single_unary_op(), align_terms(), Align a set of terms., _zip_axes_from_type()

### Community 1347 - "Community 1347"
Cohesion: 0.40
Nodes (1): TestInvalidConcat

### Community 1349 - "Community 1349"
Cohesion: 0.40
Nodes (2): Return number of unique elements in the object.          Excludes NA values by d, Return True if values in the object are unique.          This property checks wh

### Community 1350 - "Community 1350"
Cohesion: 0.40
Nodes (1): TestGetSliceBounds

### Community 1351 - "Community 1351"
Cohesion: 0.40
Nodes (1): TestBusinessDatetimeIndex

### Community 1353 - "Community 1353"
Cohesion: 0.40
Nodes (1): Base

### Community 1354 - "Community 1354"
Cohesion: 0.40
Nodes (4): Class level fixture of dtype for TestDatetimeTZDtype, Class level fixture of dtype for TestPeriodDtype, Class level fixture of dtype for TestIntervalDtype, Class level fixture of dtype for TestCategoricalDtype

### Community 1355 - "Community 1355"
Cohesion: 0.40
Nodes (1): TestABCClasses

### Community 1356 - "Community 1356"
Cohesion: 0.40
Nodes (1): TestToLatexFormatters

### Community 1357 - "Community 1357"
Cohesion: 0.40
Nodes (1): TestToLatexLongtable

### Community 1358 - "Community 1358"
Cohesion: 0.40
Nodes (1): TestDataFrameToStringColSpace

### Community 1359 - "Community 1359"
Cohesion: 0.40
Nodes (1): TestDataFrameToStringHeader

### Community 1360 - "Community 1360"
Cohesion: 0.40
Nodes (2): take a list of frames, zip them together under the     assumption that these all, zip_frames()

### Community 1361 - "Community 1361"
Cohesion: 0.40
Nodes (1): _generate_4_axes_via_gridspec()

### Community 1362 - "Community 1362"
Cohesion: 0.60
Nodes (1): TestDataFramePlotsGroupby

### Community 1363 - "Community 1363"
Cohesion: 0.40
Nodes (1): TestAsArray

### Community 1364 - "Community 1364"
Cohesion: 0.40
Nodes (1): TestDataFrameEvalWithFrame

### Community 1365 - "Community 1365"
Cohesion: 0.40
Nodes (1): TestDataFrameQueryWithMultiIndex

### Community 1367 - "Community 1367"
Cohesion: 0.40
Nodes (5): cartesian_product_for_groupers(), Reindex to a cartesian product for the groupers,     preserving the nature (Cate, test_observed(), test_observed_codes_remap(), test_observed_two_columns()

### Community 1368 - "Community 1368"
Cohesion: 0.40
Nodes (3): Memory usage of the values.          Parameters         ----------         deep, return the number of bytes in the underlying data, return the number of bytes in the underlying data         deeply introspect the

### Community 1369 - "Community 1369"
Cohesion: 0.40
Nodes (2): return a list of tuples of start, stop, step, Return a list of tuples of the (attr, formatted_value)

### Community 1370 - "Community 1370"
Cohesion: 0.40
Nodes (2): The minimum value of the RangeIndex, The maximum value of the RangeIndex

### Community 1371 - "Community 1371"
Cohesion: 0.40
Nodes (1): TestIndexUtils

### Community 1372 - "Community 1372"
Cohesion: 0.60
Nodes (2): TestNumericEngine, TestObjectEngine

### Community 1373 - "Community 1373"
Cohesion: 0.40
Nodes (1): TestGetIndexer

### Community 1374 - "Community 1374"
Cohesion: 0.40
Nodes (1): TestGetLoc

### Community 1375 - "Community 1375"
Cohesion: 0.40
Nodes (1): TestTake

### Community 1376 - "Community 1376"
Cohesion: 0.40
Nodes (1): TestAtSetItem

### Community 1377 - "Community 1377"
Cohesion: 0.40
Nodes (1): TestDataFrameDelItem

### Community 1378 - "Community 1378"
Cohesion: 0.40
Nodes (1): TestSeriesDelItem

### Community 1379 - "Community 1379"
Cohesion: 0.40
Nodes (1): TestILocSetItemDuplicateColumns

### Community 1380 - "Community 1380"
Cohesion: 0.40
Nodes (1): TestDataframeNoneCoercion

### Community 1381 - "Community 1381"
Cohesion: 0.40
Nodes (1): TestDatetimelikeCoercion

### Community 1382 - "Community 1382"
Cohesion: 0.40
Nodes (1): TestDeprecatedIndexers

### Community 1383 - "Community 1383"
Cohesion: 0.40
Nodes (1): TestLocCallable

### Community 1384 - "Community 1384"
Cohesion: 0.40
Nodes (1): TestDataFrameSetItemSlicing

### Community 1385 - "Community 1385"
Cohesion: 0.40
Nodes (3): Test ``dtype_to_arrow_c_fmt`` utility function., # TODO: use ArrowSchema to get reference C-string., test_dtype_to_arrow_c_fmt()

### Community 1386 - "Community 1386"
Cohesion: 0.40
Nodes (1): TestIndexing

### Community 1387 - "Community 1387"
Cohesion: 0.40
Nodes (1): TestIntervalIndexRendering

### Community 1388 - "Community 1388"
Cohesion: 0.40
Nodes (1): ToCSVFloatFormatVariants

### Community 1389 - "Community 1389"
Cohesion: 0.40
Nodes (1): ToCSVIndexes

### Community 1390 - "Community 1390"
Cohesion: 0.40
Nodes (1): ToJSONMem

### Community 1391 - "Community 1391"
Cohesion: 0.40
Nodes (1): SAS

### Community 1392 - "Community 1392"
Cohesion: 0.50
Nodes (2): Stata, StataMissing

### Community 1393 - "Community 1393"
Cohesion: 0.40
Nodes (5): format_query(), test_xsqlite_execute_closed_connection(), test_xsqlite_if_exists(), test_xsqlite_write_row_by_row(), tquery()

### Community 1394 - "Community 1394"
Cohesion: 0.40
Nodes (1): We treat dictionaries as a mapping in fillna, not a scalar.

### Community 1395 - "Community 1395"
Cohesion: 0.70
Nodes (1): TestSetitemValidation

### Community 1396 - "Community 1396"
Cohesion: 0.40
Nodes (5): do_adjust_figure(), format_date_labels(), maybe_adjust_figure(), Whether fig has constrained_layout enabled., Call fig.subplots_adjust unless fig has constrained_layout enabled.

### Community 1397 - "Community 1397"
Cohesion: 0.40
Nodes (1): TestAsUnit

### Community 1398 - "Community 1398"
Cohesion: 0.40
Nodes (1): TestTimestampAsUnit

### Community 1399 - "Community 1399"
Cohesion: 0.40
Nodes (1): TestDataFrameCov

### Community 1400 - "Community 1400"
Cohesion: 0.40
Nodes (1): TestSeriesCorr

### Community 1401 - "Community 1401"
Cohesion: 0.40
Nodes (1): TestGetNumericData

### Community 1402 - "Community 1402"
Cohesion: 0.40
Nodes (1): TestNormalize

### Community 1403 - "Community 1403"
Cohesion: 0.40
Nodes (1): TestSeriesPctChange

### Community 1404 - "Community 1404"
Cohesion: 0.40
Nodes (1): TestSetIndexCustomLabelType

### Community 1405 - "Community 1405"
Cohesion: 0.40
Nodes (1): TestSetIndexInvalid

### Community 1406 - "Community 1406"
Cohesion: 0.40
Nodes (1): TestSortValuesLevelAsStr

### Community 1407 - "Community 1407"
Cohesion: 0.40
Nodes (1): TestTruncate

### Community 1408 - "Community 1408"
Cohesion: 0.40
Nodes (1): TestPutmask

### Community 1409 - "Community 1409"
Cohesion: 0.40
Nodes (2): TestIsLexsorted, TestLexsortDepth

### Community 1411 - "Community 1411"
Cohesion: 0.40
Nodes (1): TestSearchsorted

### Community 1412 - "Community 1412"
Cohesion: 0.40
Nodes (1): TestGetIndexer

### Community 1413 - "Community 1413"
Cohesion: 0.40
Nodes (2): Assertion helpers and base class for offsets tests, WeekDay

### Community 1414 - "Community 1414"
Cohesion: 0.40
Nodes (1): TestCommonCBM

### Community 1415 - "Community 1415"
Cohesion: 0.40
Nodes (1): TestWhere

### Community 1416 - "Community 1416"
Cohesion: 0.40
Nodes (1): TestPeriodRange

### Community 1417 - "Community 1417"
Cohesion: 0.40
Nodes (1): TestPeriodDisallowedFreqs

### Community 1418 - "Community 1418"
Cohesion: 0.40
Nodes (1): TestPeriodIndexOps

### Community 1420 - "Community 1420"
Cohesion: 0.40
Nodes (1): TestCategoricalSeriesReductions

### Community 1421 - "Community 1421"
Cohesion: 0.40
Nodes (1): TestDatetime64SeriesReductions

### Community 1422 - "Community 1422"
Cohesion: 0.40
Nodes (4): downsample_method(), Fixture for parametrization of Grouper downsample methods., Fixture for parametrization of Grouper resample methods., resample_method()

### Community 1423 - "Community 1423"
Cohesion: 0.40
Nodes (5): _fast_string_path_available(), test_string_fast_path_blank_missing(), test_string_fast_path_invalid_utf8(), test_string_fast_path_matches_object_path(), test_string_fast_path_truncated_file()

### Community 1424 - "Community 1424"
Cohesion: 0.40
Nodes (1): TestTimeSeriesArithmetic

### Community 1425 - "Community 1425"
Cohesion: 0.40
Nodes (1): TestSeriesMissingData

### Community 1426 - "Community 1426"
Cohesion: 0.40
Nodes (1): TestSeriesUnaryOps

### Community 1427 - "Community 1427"
Cohesion: 0.40
Nodes (3): is_object_or_nan_string_dtype(), Implementation of pandas.Series.str and its interface.  * strings.accessor.Strin, Check if string-like dtype is following NaN semantics, i.e. is object     dtype

### Community 1428 - "Community 1428"
Cohesion: 0.40
Nodes (3): get_obj(), Helpers for sharing tests between DataFrame/Series, For sharing tests using frame_or_series, either return the DataFrame     unchang

### Community 1429 - "Community 1429"
Cohesion: 0.60
Nodes (2): SubclassedDataFrame, SubclassedSeries

### Community 1430 - "Community 1430"
Cohesion: 0.40
Nodes (1): TestEnsureNumeric

### Community 1431 - "Community 1431"
Cohesion: 0.40
Nodes (1): TestTimedeltaArrayConstructor

### Community 1432 - "Community 1432"
Cohesion: 0.40
Nodes (1): TestTimedeltaIndexRendering

### Community 1433 - "Community 1433"
Cohesion: 0.40
Nodes (1): TestFreq

### Community 1434 - "Community 1434"
Cohesion: 0.40
Nodes (1): TestGetLoc

### Community 1435 - "Community 1435"
Cohesion: 0.40
Nodes (1): TestMaybeCastSliceBound

### Community 1436 - "Community 1436"
Cohesion: 0.40
Nodes (1): TestTake

### Community 1437 - "Community 1437"
Cohesion: 0.40
Nodes (1): TestJoin

### Community 1438 - "Community 1438"
Cohesion: 0.40
Nodes (1): TestTimestampConstructorUnitKeyword

### Community 1439 - "Community 1439"
Cohesion: 0.40
Nodes (1): TestTimestampConversion

### Community 1440 - "Community 1440"
Cohesion: 0.40
Nodes (1): TestEWM

### Community 1441 - "Community 1441"
Cohesion: 0.40
Nodes (1): TestEWM

### Community 1442 - "Community 1442"
Cohesion: 0.50
Nodes (1): TestObjectDtypeEquivalence

### Community 1443 - "Community 1443"
Cohesion: 0.50
Nodes (1): TestTimedelta64ArrayComparisons

### Community 1444 - "Community 1444"
Cohesion: 0.50
Nodes (2): Return a Series containing counts of each category.          Every category will, Describes this Categorical          Returns         -------         description:

### Community 1445 - "Community 1445"
Cohesion: 0.50
Nodes (4): factorize_from_iterable(), factorize_from_iterables(), Factorize an input `values` into `categories` and `codes`. Preserves     categor, A higher-level wrapper over `factorize_from_iterable`.      Parameters     -----

### Community 1447 - "Community 1447"
Cohesion: 0.50
Nodes (3): Fixture returning DatetimeArray from parametrized PeriodIndex objects, Fixture returning DatetimeArray with parametrized frequency and         timezone, Fixture returning DatetimeArray with daily frequency.

### Community 1448 - "Community 1448"
Cohesion: 0.50
Nodes (1): TestTimedeltaArray

### Community 1449 - "Community 1449"
Cohesion: 0.50
Nodes (1): TestGetLoc

### Community 1450 - "Community 1450"
Cohesion: 0.50
Nodes (1): TestGetSliceBounds

### Community 1451 - "Community 1451"
Cohesion: 0.50
Nodes (1): Finalize

### Community 1452 - "Community 1452"
Cohesion: 0.50
Nodes (1): Duplicated

### Community 1453 - "Community 1453"
Cohesion: 0.50
Nodes (1): Fillna

### Community 1454 - "Community 1454"
Cohesion: 0.50
Nodes (1): Update

### Community 1455 - "Community 1455"
Cohesion: 0.50
Nodes (1): MethodLookup

### Community 1456 - "Community 1456"
Cohesion: 0.50
Nodes (2): MaybeConvertNumeric, ToTimedeltaErrors

### Community 1457 - "Community 1457"
Cohesion: 0.50
Nodes (1): ToNumeric

### Community 1458 - "Community 1458"
Cohesion: 0.50
Nodes (1): ToTimedelta

### Community 1459 - "Community 1459"
Cohesion: 0.50
Nodes (1): Values

### Community 1460 - "Community 1460"
Cohesion: 0.50
Nodes (1): StringArrayConstruction

### Community 1461 - "Community 1461"
Cohesion: 0.50
Nodes (1): TestPrivateCategoricalAPI

### Community 1462 - "Community 1462"
Cohesion: 0.50
Nodes (1): TestTake

### Community 1463 - "Community 1463"
Cohesion: 0.50
Nodes (4): diff(), factorize_monotonic_codes(), difference of n between self,     analogous to s-s.shift(n)      Parameters, Factorize an array known to be monotonic and of length >= 2.      Uses adjacent-

### Community 1464 - "Community 1464"
Cohesion: 0.50
Nodes (4): _managle_lambda_list(), maybe_mangle_lambdas(), Possibly mangle a list of aggfuncs.      Parameters     ----------     aggfuncs, Make new lambdas with unique names.      Parameters     ----------     agg_spec

### Community 1465 - "Community 1465"
Cohesion: 0.50
Nodes (4): is_null_slice(), is_true_slices(), We have a null slice., Find non-trivial slices in "line": yields a bool.

### Community 1466 - "Community 1466"
Cohesion: 0.50
Nodes (2): Ensure that key is valid for current indexer.          Parameters         ------, Check that 'key' is a valid position in the desired axis.          Parameters

### Community 1467 - "Community 1467"
Cohesion: 0.50
Nodes (3): Validate that a positional indexer cannot enlarge its target         will raise, Given an indexer for the first dimension, create an equivalent tuple     for ind, _tuplify()

### Community 1468 - "Community 1468"
Cohesion: 0.50
Nodes (1): TestSequenceToDT64NS

### Community 1469 - "Community 1469"
Cohesion: 0.50
Nodes (1): TestFreq

### Community 1470 - "Community 1470"
Cohesion: 0.50
Nodes (2): Return the array type associated with this dtype.          Returns         -----, Construct an ExtensionArray of this dtype with the given shape.          Analogo

### Community 1471 - "Community 1471"
Cohesion: 0.50
Nodes (1): TestExcelWriterEngineTests

### Community 1473 - "Community 1473"
Cohesion: 0.50
Nodes (2): has_info_repr(), has_non_verbose_info_repr()

### Community 1474 - "Community 1474"
Cohesion: 0.50
Nodes (1): TestFormatPercentiles

### Community 1475 - "Community 1475"
Cohesion: 0.50
Nodes (1): TestGenericArrayFormatter

### Community 1476 - "Community 1476"
Cohesion: 0.50
Nodes (1): TestDataFrameConstructorIndexInference

### Community 1477 - "Community 1477"
Cohesion: 0.50
Nodes (4): bdate_range(), date_range(), Return a fixed frequency DatetimeIndex.      Returns the range of equally spaced, Return a fixed frequency DatetimeIndex with business day as the default.      Th

### Community 1478 - "Community 1478"
Cohesion: 0.50
Nodes (2): Determines if two MultiIndex objects have the same labeling information, Return True if the levels of both MultiIndex objects are the same

### Community 1479 - "Community 1479"
Cohesion: 0.50
Nodes (2): Parameters         ----------         other : Any         op : callable that acc, The value of the `step` parameter (``1`` if this was not supplied).          The

### Community 1480 - "Community 1480"
Cohesion: 0.50
Nodes (2): Check if other range is contained in self, Form the union of two Index objects and sorts if possible          Parameters

### Community 1481 - "Community 1481"
Cohesion: 0.50
Nodes (1): TestConversion

### Community 1483 - "Community 1483"
Cohesion: 0.50
Nodes (1): TestIndexConstructorUnwrapping

### Community 1484 - "Community 1484"
Cohesion: 0.50
Nodes (1): TestGetitemSlice

### Community 1486 - "Community 1486"
Cohesion: 0.50
Nodes (1): TestILocErrors

### Community 1487 - "Community 1487"
Cohesion: 0.50
Nodes (1): TestLocBooleanLabelsAndSlices

### Community 1488 - "Community 1488"
Cohesion: 0.50
Nodes (1): TestMultiIndexScalar

### Community 1489 - "Community 1489"
Cohesion: 0.50
Nodes (1): TestSetValue

### Community 1490 - "Community 1490"
Cohesion: 0.50
Nodes (1): TestSetitemScalarIndexer

### Community 1491 - "Community 1491"
Cohesion: 0.50
Nodes (1): TestIntervalComparisons

### Community 1492 - "Community 1492"
Cohesion: 0.50
Nodes (1): TestIntervalConstructors

### Community 1493 - "Community 1493"
Cohesion: 0.50
Nodes (1): TestSliceLocs

### Community 1494 - "Community 1494"
Cohesion: 0.50
Nodes (1): TestIntervalIndexInsideMultiIndex

### Community 1495 - "Community 1495"
Cohesion: 0.50
Nodes (1): ToCSVMultiIndexUnusedLevels

### Community 1496 - "Community 1496"
Cohesion: 0.50
Nodes (1): ToCSVPeriodIndex

### Community 1497 - "Community 1497"
Cohesion: 0.50
Nodes (1): ToCSVPeriod

### Community 1498 - "Community 1498"
Cohesion: 0.50
Nodes (1): DoesStringLookLikeDatetime

### Community 1499 - "Community 1499"
Cohesion: 0.50
Nodes (1): Base

### Community 1500 - "Community 1500"
Cohesion: 0.50
Nodes (4): create_and_load_postgres_datetz(), test_datetime_with_timezone_query(), test_datetime_with_timezone_query_chunksize(), test_datetime_with_timezone_table()

### Community 1501 - "Community 1501"
Cohesion: 0.50
Nodes (4): convert_json_field_to_pandas_type(), parse_table_schema(), Converts a JSON field descriptor into its corresponding NumPy / pandas type, Builds a DataFrame from a given schema      Parameters     ----------     json :

### Community 1502 - "Community 1502"
Cohesion: 0.50
Nodes (1): TestMisc

### Community 1503 - "Community 1503"
Cohesion: 0.50
Nodes (1): TestPadBackfill

### Community 1504 - "Community 1504"
Cohesion: 0.50
Nodes (1): TestAsOf

### Community 1505 - "Community 1505"
Cohesion: 0.50
Nodes (1): TestAstypeAPI

### Community 1506 - "Community 1506"
Cohesion: 0.50
Nodes (1): TestDelete

### Community 1507 - "Community 1507"
Cohesion: 0.50
Nodes (1): TestTimedeltaIndexFactorize

### Community 1508 - "Community 1508"
Cohesion: 0.50
Nodes (1): TestDataFrameSetItem

### Community 1509 - "Community 1509"
Cohesion: 0.50
Nodes (1): TestTimestampNormalize

### Community 1510 - "Community 1510"
Cohesion: 0.50
Nodes (1): TestPipe

### Community 1511 - "Community 1511"
Cohesion: 0.50
Nodes (1): TestDataFramePop

### Community 1512 - "Community 1512"
Cohesion: 0.50
Nodes (1): TestDataFrameReindexLike

### Community 1513 - "Community 1513"
Cohesion: 0.50
Nodes (1): TestSeriesRenameAxis

### Community 1514 - "Community 1514"
Cohesion: 0.50
Nodes (1): TestTimestampTZConvert

### Community 1515 - "Community 1515"
Cohesion: 0.50
Nodes (1): TestPrivateValues

### Community 1516 - "Community 1516"
Cohesion: 0.50
Nodes (4): create_data_for_split(), Convert the DataFrame to a dictionary.      The type of the key-value pairs can, Simple helper method to create data for to ``to_dict(orient="split")``     to cr, to_dict()

### Community 1517 - "Community 1517"
Cohesion: 0.50
Nodes (1): TestKeyErrorsWithMultiIndex

### Community 1518 - "Community 1518"
Cohesion: 0.50
Nodes (1): TestContains

### Community 1519 - "Community 1519"
Cohesion: 0.50
Nodes (1): TestTake

### Community 1520 - "Community 1520"
Cohesion: 0.50
Nodes (1): TestWhere

### Community 1521 - "Community 1521"
Cohesion: 0.50
Nodes (1): TestEaster

### Community 1522 - "Community 1522"
Cohesion: 0.50
Nodes (4): get_op_result_name(), _maybe_match_name(), Find the appropriate name to pin to an operation result.  This result     should, Try to find a name to attach to the result of an operation between     a and b.

### Community 1523 - "Community 1523"
Cohesion: 0.50
Nodes (4): _create_series(), Helper for the _series dict, Fixture for tests on series with changing types of indices., series_with_simple_index()

### Community 1524 - "Community 1524"
Cohesion: 0.50
Nodes (2): is_index_col(), Extract and return the names, index_names, col_names if the column         names

### Community 1525 - "Community 1525"
Cohesion: 0.50
Nodes (3): Set the columns that should not undergo dtype conversions.          Currently, a, Check if parse_dates are in columns.      If user has provided names for parse_d, validate_parse_dates_presence()

### Community 1526 - "Community 1526"
Cohesion: 0.50
Nodes (1): TestShallowCopy

### Community 1527 - "Community 1527"
Cohesion: 0.50
Nodes (1): TestSimpleNew

### Community 1528 - "Community 1528"
Cohesion: 0.50
Nodes (1): TestPeriodIndexRendering

### Community 1529 - "Community 1529"
Cohesion: 0.50
Nodes (1): TestContains

### Community 1530 - "Community 1530"
Cohesion: 0.50
Nodes (1): TestTake

### Community 1531 - "Community 1531"
Cohesion: 0.50
Nodes (1): TestReductions

### Community 1532 - "Community 1532"
Cohesion: 0.50
Nodes (1): TestSearchsorted

### Community 1533 - "Community 1533"
Cohesion: 0.50
Nodes (1): TestCommon

### Community 1534 - "Community 1534"
Cohesion: 0.50
Nodes (2): Test timedelta converter, TestTimeDeltaConverter

### Community 1535 - "Community 1535"
Cohesion: 0.50
Nodes (1): TestSeriesPlots

### Community 1537 - "Community 1537"
Cohesion: 0.50
Nodes (1): TestDatetimeLikeStatReductions

### Community 1538 - "Community 1538"
Cohesion: 0.50
Nodes (4): _groupby_and_merge(), merge_ordered(), groupby & merge; we are always performing a left-by type operation      Paramete, Perform a merge for ordered data with optional filling/interpolation.      Desig

### Community 1539 - "Community 1539"
Cohesion: 0.50
Nodes (1): TestNamePreservation

### Community 1540 - "Community 1540"
Cohesion: 0.50
Nodes (1): TestSeriesConstructorIndexCoercion

### Community 1541 - "Community 1541"
Cohesion: 0.50
Nodes (1): TestSeriesConstructorInternals

### Community 1542 - "Community 1542"
Cohesion: 0.50
Nodes (1): TestSparseIndexIntersect

### Community 1543 - "Community 1543"
Cohesion: 0.50
Nodes (1): TestUnaryMethods

### Community 1544 - "Community 1544"
Cohesion: 0.50
Nodes (4): cls(), Fixture giving array type from parametrized 'dtype, test_constructor_raises(), test_from_sequence_no_mutate()

### Community 1545 - "Community 1545"
Cohesion: 0.50
Nodes (4): box_expected(), Helper function to wrap the expected output of a test in a given box_class., Similar to pd.array, but does not cast numpy dtypes to nullable dtypes., to_array()

### Community 1546 - "Community 1546"
Cohesion: 0.50
Nodes (1): TestDiff

### Community 1547 - "Community 1547"
Cohesion: 0.50
Nodes (1): TestTimedeltaIndexDelete

### Community 1548 - "Community 1548"
Cohesion: 0.50
Nodes (1): TestGetItem

### Community 1549 - "Community 1549"
Cohesion: 0.50
Nodes (1): TestWhere

### Community 1550 - "Community 1550"
Cohesion: 0.50
Nodes (1): TestTimedeltaRangeUnitInference

### Community 1551 - "Community 1551"
Cohesion: 0.50
Nodes (1): TestTimedeltaIndex

### Community 1552 - "Community 1552"
Cohesion: 0.50
Nodes (1): TestTimestampResolutionInference

### Community 1553 - "Community 1553"
Cohesion: 0.50
Nodes (2): Tests for Timestamp timezone-related methods, TestTimestampTZOperations

### Community 1554 - "Community 1554"
Cohesion: 0.50
Nodes (1): TestToTime

### Community 1555 - "Community 1555"
Cohesion: 0.50
Nodes (1): Normalize

### Community 1556 - "Community 1556"
Cohesion: 0.50
Nodes (1): TimeTZConvert

### Community 1557 - "Community 1557"
Cohesion: 0.67
Nodes (1): TestSparseAccessor

### Community 1558 - "Community 1558"
Cohesion: 0.67
Nodes (1): TestStrAccessor

### Community 1559 - "Community 1559"
Cohesion: 0.67
Nodes (1): TestCategoricalComparisons

### Community 1560 - "Community 1560"
Cohesion: 0.67
Nodes (1): transforms.py is for shape-preserving functions.

### Community 1562 - "Community 1562"
Cohesion: 0.67
Nodes (2): pyarrow_array_to_numpy_and_mask(), Convert a primitive pyarrow.Array to a numpy array and boolean mask based     on

### Community 1563 - "Community 1563"
Cohesion: 0.67
Nodes (2): allow_na_ops(), Whether to skip test cases including NaN

### Community 1564 - "Community 1564"
Cohesion: 0.67
Nodes (1): FrameWithFrameWide

### Community 1565 - "Community 1565"
Cohesion: 0.67
Nodes (1): MixedFrameWithSeriesAxis

### Community 1566 - "Community 1566"
Cohesion: 0.67
Nodes (1): OffsetArrayArithmetic

### Community 1567 - "Community 1567"
Cohesion: 0.67
Nodes (1): OpWithFillValue

### Community 1568 - "Community 1568"
Cohesion: 0.67
Nodes (1): Interpolate

### Community 1569 - "Community 1569"
Cohesion: 0.67
Nodes (1): MaskBool

### Community 1570 - "Community 1570"
Cohesion: 0.67
Nodes (1): MemoryUsage

### Community 1571 - "Community 1571"
Cohesion: 0.67
Nodes (1): SortMultiKey

### Community 1572 - "Community 1572"
Cohesion: 0.67
Nodes (1): ToDict

### Community 1573 - "Community 1573"
Cohesion: 0.67
Nodes (1): ToRecords

### Community 1574 - "Community 1574"
Cohesion: 0.67
Nodes (1): Resample

### Community 1575 - "Community 1575"
Cohesion: 0.67
Nodes (1): Sample

### Community 1576 - "Community 1576"
Cohesion: 0.67
Nodes (1): Shift

### Community 1577 - "Community 1577"
Cohesion: 0.67
Nodes (1): Size

### Community 1578 - "Community 1578"
Cohesion: 0.67
Nodes (1): SumTimeDelta

### Community 1579 - "Community 1579"
Cohesion: 0.67
Nodes (1): GetItemSingleColumn

### Community 1580 - "Community 1580"
Cohesion: 0.67
Nodes (1): IndexSingleRow

### Community 1581 - "Community 1581"
Cohesion: 0.67
Nodes (1): NumericMaskedIndexing

### Community 1582 - "Community 1582"
Cohesion: 0.67
Nodes (1): SeriesSetitem

### Community 1583 - "Community 1583"
Cohesion: 0.67
Nodes (1): Setitem

### Community 1584 - "Community 1584"
Cohesion: 0.67
Nodes (1): SortedAndUnsortedDatetimeIndexLoc

### Community 1585 - "Community 1585"
Cohesion: 0.67
Nodes (1): ConcatDataFrames

### Community 1586 - "Community 1586"
Cohesion: 0.67
Nodes (1): JoinEmpty

### Community 1587 - "Community 1587"
Cohesion: 0.67
Nodes (1): TestUnaryOps

### Community 1589 - "Community 1589"
Cohesion: 0.67
Nodes (2): _get_pretty_string(), Return a prettier version of obj.      Parameters     ----------     obj : objec

### Community 1590 - "Community 1590"
Cohesion: 0.67
Nodes (2): get_array(), Helper method to get array for a DataFrame column or a Series.      Equivalent o

### Community 1591 - "Community 1591"
Cohesion: 0.67
Nodes (3): _expansion_can_hold(), infer_and_maybe_downcast(), Can new_arr's values be set losslessly into an array of orig's dtype?      Decid

### Community 1592 - "Community 1592"
Cohesion: 0.67
Nodes (1): TestAccumulator

### Community 1593 - "Community 1593"
Cohesion: 0.67
Nodes (1): TestContains

### Community 1594 - "Community 1594"
Cohesion: 0.67
Nodes (1): TestIndexerBetweenTime

### Community 1595 - "Community 1595"
Cohesion: 0.67
Nodes (1): TestMaybeCastSliceBound

### Community 1596 - "Community 1596"
Cohesion: 0.67
Nodes (1): TestDatetimeIndexReindex

### Community 1598 - "Community 1598"
Cohesion: 0.67
Nodes (1): TestDataFrameAlterAxes

### Community 1601 - "Community 1601"
Cohesion: 0.67
Nodes (1): TestDataFrame2

### Community 1602 - "Community 1602"
Cohesion: 0.67
Nodes (3): _lexsort_depth(), Compute and return the lexsort_depth, the number of levels of the         MultiI, Count depth (up to a maximum of `nlevels`) with which codes are lexsorted.

### Community 1605 - "Community 1605"
Cohesion: 0.67
Nodes (1): TestCaching

### Community 1606 - "Community 1606"
Cohesion: 0.67
Nodes (1): TestGetValue

### Community 1607 - "Community 1607"
Cohesion: 0.67
Nodes (1): TestILocCallable

### Community 1608 - "Community 1608"
Cohesion: 0.67
Nodes (1): _safe_add()

### Community 1609 - "Community 1609"
Cohesion: 0.67
Nodes (1): Pointer to start of the buffer as an integer.

### Community 1610 - "Community 1610"
Cohesion: 0.67
Nodes (2): Return an iterator yielding the chunks.          See `DataFrame.get_chunks` for, Return an iterator yielding the chunks.          By default (None), yields the c

### Community 1611 - "Community 1611"
Cohesion: 0.67
Nodes (2): The metadata for the column. See `DataFrame.metadata` for more details., The metadata for the data frame, as a dictionary with string keys. The         c

### Community 1612 - "Community 1612"
Cohesion: 0.67
Nodes (2): Return the number of chunks the column consists of., Return the number of chunks the DataFrame consists of.

### Community 1613 - "Community 1613"
Cohesion: 0.67
Nodes (3): Fixture for generating intervals of types from a start value and a shift     val, Fixture for generating intervals of different types from a start value     and a, start_shift()

### Community 1614 - "Community 1614"
Cohesion: 0.67
Nodes (1): ToCSVDatetimeIndex

### Community 1615 - "Community 1615"
Cohesion: 0.67
Nodes (3): create_and_load_types_sqlite3(), sqlite_adbc_types(), sqlite_buildin_types()

### Community 1616 - "Community 1616"
Cohesion: 0.67
Nodes (3): dtype_backend_expected(), test_read_sql_dtype_backend(), test_read_sql_dtype_backend_table()

### Community 1617 - "Community 1617"
Cohesion: 0.67
Nodes (3): get_sqlite_column_type(), test_sqlite_notna_dtype(), test_sqlite_test_dtype()

### Community 1619 - "Community 1619"
Cohesion: 0.67
Nodes (2): JSONDtype, Return the array type associated with this dtype.          Returns         -----

### Community 1620 - "Community 1620"
Cohesion: 0.67
Nodes (2): orient(), Fixture for orients excluding the table format.

### Community 1621 - "Community 1621"
Cohesion: 0.67
Nodes (1): This fails when we get to tm.assert_series_equal when left.index         contain

### Community 1622 - "Community 1622"
Cohesion: 0.67
Nodes (2): is_monotonic_increasing(), Check if int64 values are monotonically increasing.

### Community 1623 - "Community 1623"
Cohesion: 0.67
Nodes (1): get_test_data()

### Community 1624 - "Community 1624"
Cohesion: 0.67
Nodes (1): _join_by_hand()

### Community 1625 - "Community 1625"
Cohesion: 0.67
Nodes (2): rand_str(), Generate one random byte string.

### Community 1626 - "Community 1626"
Cohesion: 0.67
Nodes (1): TestDataFrameCount

### Community 1627 - "Community 1627"
Cohesion: 0.67
Nodes (1): TestSeriesCount

### Community 1628 - "Community 1628"
Cohesion: 0.67
Nodes (1): TestSeriesCov

### Community 1629 - "Community 1629"
Cohesion: 0.67
Nodes (1): TestFactorize

### Community 1630 - "Community 1630"
Cohesion: 0.67
Nodes (1): TestIsMonotonic

### Community 1631 - "Community 1631"
Cohesion: 0.67
Nodes (1): TestIsna

### Community 1632 - "Community 1632"
Cohesion: 0.67
Nodes (1): TestMatmul

### Community 1633 - "Community 1633"
Cohesion: 0.67
Nodes (1): TestReorderLevels

### Community 1634 - "Community 1634"
Cohesion: 0.67
Nodes (1): TestSetName

### Community 1635 - "Community 1635"
Cohesion: 0.67
Nodes (1): TestSeriesToDict

### Community 1636 - "Community 1636"
Cohesion: 0.67
Nodes (3): assert_categorical_single_grouper(), test_categorical_single_grouper_observed_false(), test_categorical_single_grouper_observed_true()

### Community 1637 - "Community 1637"
Cohesion: 0.67
Nodes (1): TestValues

### Community 1638 - "Community 1638"
Cohesion: 0.67
Nodes (1): TestWhere

### Community 1639 - "Community 1639"
Cohesion: 0.67
Nodes (1): TestGetSliceBounds

### Community 1640 - "Community 1640"
Cohesion: 0.67
Nodes (1): TestSetOpsSort

### Community 1641 - "Community 1641"
Cohesion: 0.67
Nodes (1): TestGetIndexerNonUnique

### Community 1642 - "Community 1642"
Cohesion: 0.67
Nodes (3): Boilerplate for pandas conventions in arithmetic and comparison methods.      Pa, Boilerplate for pandas conventions in arithmetic and comparison methods.      En, unpack_zerodim_and_defer()

### Community 1643 - "Community 1643"
Cohesion: 0.67
Nodes (3): dtype_backend(), Parametrized fixture for pd.options.mode.string_storage.      * 'python'     * ', string_storage()

### Community 1644 - "Community 1644"
Cohesion: 0.67
Nodes (2): pandas_core_window_ewm, pandas_core_window_expanding

### Community 1645 - "Community 1645"
Cohesion: 0.67
Nodes (2): Validate the 'usecols' parameter.      Checks whether or not the 'usecols' param, _validate_usecols_arg()

### Community 1647 - "Community 1647"
Cohesion: 0.67
Nodes (1): TestPickle

### Community 1648 - "Community 1648"
Cohesion: 0.67
Nodes (2): Wish to match NumPy units, TestPeriodRepresentation

### Community 1649 - "Community 1649"
Cohesion: 0.67
Nodes (1): _check_ax_limits()

### Community 1650 - "Community 1650"
Cohesion: 0.67
Nodes (1): TestHDFStoreSubclass

### Community 1651 - "Community 1651"
Cohesion: 0.67
Nodes (1): TestSas

### Community 1652 - "Community 1652"
Cohesion: 0.67
Nodes (2): Tests for error handling related to data types of method arguments., test_validate_bool_args()

### Community 1653 - "Community 1653"
Cohesion: 0.67
Nodes (1): Create a SparseArray from a scipy.sparse matrix.          Parameters         ---

### Community 1654 - "Community 1654"
Cohesion: 0.67
Nodes (1): TestSparseArrayConcat

### Community 1655 - "Community 1655"
Cohesion: 0.67
Nodes (1): TestSparseIndexUnion

### Community 1656 - "Community 1656"
Cohesion: 0.67
Nodes (1): TestArgmaxArgmin

### Community 1657 - "Community 1657"
Cohesion: 0.67
Nodes (1): TestHashTable

### Community 1658 - "Community 1658"
Cohesion: 0.67
Nodes (2): everything you wanted to test about sorting, TestSorted

### Community 1659 - "Community 1659"
Cohesion: 0.67
Nodes (1): TestTimedeltaIndexArithmetic

### Community 1660 - "Community 1660"
Cohesion: 0.67
Nodes (1): TestAccumulator

### Community 1661 - "Community 1661"
Cohesion: 0.67
Nodes (1): TestContains

### Community 1662 - "Community 1662"
Cohesion: 0.67
Nodes (1): TestGetIndexer

### Community 1663 - "Community 1663"
Cohesion: 0.67
Nodes (1): TestSearchSorted

### Community 1664 - "Community 1664"
Cohesion: 0.67
Nodes (1): TestTimedeltaIndexDifference

### Community 1665 - "Community 1665"
Cohesion: 0.67
Nodes (1): Tests that the tslibs API is locked down

### Community 1668 - "Community 1668"
Cohesion: 1.00
Nodes (1): algos/ directory is intended for individual functions from core.algorithms  In m

### Community 1669 - "Community 1669"
Cohesion: 1.00
Nodes (2): int_frame_const_col(), Fixture for DataFrame of ints which are constant per column      Columns are ['A

### Community 1670 - "Community 1670"
Cohesion: 1.00
Nodes (1): core.array_algos is for algorithms that operate on ndarray and ExtensionArray. T

### Community 1671 - "Community 1671"
Cohesion: 1.00
Nodes (1): pandas_tests_extension_array_with_attr_array

### Community 1672 - "Community 1672"
Cohesion: 1.00
Nodes (1): The categories of this categorical.          Setting assigns new values to each

### Community 1673 - "Community 1673"
Cohesion: 1.00
Nodes (1): Concatenate multiple arrays of this dtype.          Parameters         ---------

### Community 1674 - "Community 1674"
Cohesion: 1.00
Nodes (1): Analogous to np.empty(shape, dtype=dtype)          Parameters         ----------

### Community 1675 - "Community 1675"
Cohesion: 1.00
Nodes (1): Return a Series containing counts of unique values.          Parameters

### Community 1676 - "Community 1676"
Cohesion: 1.00
Nodes (2): Decorator to ravel a 2D array before passing it to a cython operation,     then, ravel_compat()

### Community 1677 - "Community 1677"
Cohesion: 1.00
Nodes (1): Fixture returning parametrized time units

### Community 1678 - "Community 1678"
Cohesion: 1.00
Nodes (1): BaseExtensionTests

### Community 1679 - "Community 1679"
Cohesion: 1.00
Nodes (1): Tests for CategoricalIndex.__repr__ and related methods.

### Community 1680 - "Community 1680"
Cohesion: 1.00
Nodes (1): pandas_core_computation_eval

### Community 1681 - "Community 1681"
Cohesion: 1.00
Nodes (1): Find indices where elements should be inserted to maintain order.          Find

### Community 1682 - "Community 1682"
Cohesion: 1.00
Nodes (1): Return a tuple of the shape of the underlying data.          For a Series this i

### Community 1683 - "Community 1683"
Cohesion: 1.00
Nodes (1): Return the number of elements in the underlying data.          For a Series or I

### Community 1684 - "Community 1684"
Cohesion: 1.00
Nodes (1): A NumPy ndarray representing the values in this Series or Index.          This m

### Community 1685 - "Community 1685"
Cohesion: 1.00
Nodes (1): Return a list of the values.          These are each a scalar type, which is a P

### Community 1686 - "Community 1686"
Cohesion: 1.00
Nodes (1): Return the transpose, which is by definition self.          Returns         ----

### Community 1687 - "Community 1687"
Cohesion: 1.00
Nodes (1): Return a Series containing counts of unique values.          The resulting objec

### Community 1688 - "Community 1688"
Cohesion: 1.00
Nodes (2): all_none(), Returns a boolean indicating if all arguments are None.

### Community 1689 - "Community 1689"
Cohesion: 1.00
Nodes (2): all_not_none(), Returns a boolean indicating if all arguments are not None.

### Community 1690 - "Community 1690"
Cohesion: 1.00
Nodes (2): any_none(), Returns a boolean indicating if any argument is None.

### Community 1691 - "Community 1691"
Cohesion: 1.00
Nodes (2): any_not_none(), Returns a boolean indicating if any argument is not None.

### Community 1692 - "Community 1692"
Cohesion: 1.00
Nodes (2): apply_if_callable(), Evaluate possibly callable input using obj and kwargs if it is callable,     oth

### Community 1693 - "Community 1693"
Cohesion: 1.00
Nodes (2): cast_scalar_indexer(), Disallow indexing with a float key, even if that key is a round number.      Par

### Community 1694 - "Community 1694"
Cohesion: 1.00
Nodes (2): convert_to_list_like(), Convert list-like or scalar input to list-like. List, numpy and pandas array-lik

### Community 1695 - "Community 1695"
Cohesion: 1.00
Nodes (2): count_not_none(), Returns the count of arguments that are not None.

### Community 1696 - "Community 1696"
Cohesion: 1.00
Nodes (2): fill_missing_names(), If a name is missing then replace it by level_n, where n is the count      Param

### Community 1697 - "Community 1697"
Cohesion: 1.00
Nodes (2): flatten(), Flatten an arbitrarily nested sequence.      Parameters     ----------     line

### Community 1698 - "Community 1698"
Cohesion: 1.00
Nodes (2): get_cython_func(), if we define an internal function for this argument, return it

### Community 1699 - "Community 1699"
Cohesion: 1.00
Nodes (2): get_rename_function(), Returns a function that will map names/labels, dependent if mapper     is a dict

### Community 1700 - "Community 1700"
Cohesion: 1.00
Nodes (2): is_bool_indexer(), Check whether `key` is a valid boolean indexer.      Parameters     ----------

### Community 1701 - "Community 1701"
Cohesion: 1.00
Nodes (2): is_empty_slice(), We have an empty slice, e.g. no values are selected.

### Community 1702 - "Community 1702"
Cohesion: 1.00
Nodes (2): is_full_slice(), We have a full length slice.

### Community 1703 - "Community 1703"
Cohesion: 1.00
Nodes (2): is_local_in_caller_frame(), Helper function used in detecting chained assignment.      If the pandas object

### Community 1704 - "Community 1704"
Cohesion: 1.00
Nodes (2): maybe_iterable_to_list(), If obj is Iterable but not list-like, consume into list.

### Community 1705 - "Community 1705"
Cohesion: 1.00
Nodes (2): not_none(), Returns a generator consisting of the arguments that are not None.

### Community 1706 - "Community 1706"
Cohesion: 1.00
Nodes (2): pipe(), Apply a function ``func`` to object ``obj`` either by passing obj as the     fir

### Community 1707 - "Community 1707"
Cohesion: 1.00
Nodes (2): random_state(), Helper function for processing random_state arguments.      Parameters     -----

### Community 1708 - "Community 1708"
Cohesion: 1.00
Nodes (2): Helper function to standardize a supplied mapping.      Parameters     ---------, standardize_mapping()

### Community 1709 - "Community 1709"
Cohesion: 1.00
Nodes (2): Temporarily set attribute on an object.      Parameters     ----------     obj :, temp_setattr()

### Community 1710 - "Community 1710"
Cohesion: 1.00
Nodes (2): Check the length of data matches the length of the index., require_length_match()

### Community 1711 - "Community 1711"
Cohesion: 1.00
Nodes (1): pandas_tests_extension_date_array

### Community 1712 - "Community 1712"
Cohesion: 1.00
Nodes (1): Test different DatetimeIndex constructions with timezone         Follow-up of GH

### Community 1713 - "Community 1713"
Cohesion: 1.00
Nodes (2): astype_is_view(), Checks if astype avoided copying the data.      Parameters     ----------     dt

### Community 1714 - "Community 1714"
Cohesion: 1.00
Nodes (1): Whether this dtype should be considered boolean.          By default, ExtensionD

### Community 1715 - "Community 1715"
Cohesion: 1.00
Nodes (1): Can arrays with this dtype be modified with __setitem__? If not, return

### Community 1716 - "Community 1716"
Cohesion: 1.00
Nodes (1): Whether columns with this dtype should be considered numeric.          By defaul

### Community 1717 - "Community 1717"
Cohesion: 1.00
Nodes (1): A character code (one of 'biufcmMOSUV'), default 'O'          This should match

### Community 1718 - "Community 1718"
Cohesion: 1.00
Nodes (1): A string identifying the data type.          Will be used for display in, e.g. `

### Community 1719 - "Community 1719"
Cohesion: 1.00
Nodes (1): Ordered list of field names, or None if there are no fields.          This is fo

### Community 1720 - "Community 1720"
Cohesion: 1.00
Nodes (1): Do ExtensionArrays with this dtype support 2D arrays?          Historically Exte

### Community 1721 - "Community 1721"
Cohesion: 1.00
Nodes (2): ensure_python_int(), Ensure that a value is a python int.      Parameters     ----------     value: i

### Community 1722 - "Community 1722"
Cohesion: 1.00
Nodes (2): ensure_str(), Ensure that bytes and non-strings get converted into ``str`` objects.

### Community 1723 - "Community 1723"
Cohesion: 1.00
Nodes (2): is_1d_only_ea_dtype(), Analogue to is_extension_array_dtype but excluding DatetimeTZDtype.

### Community 1724 - "Community 1724"
Cohesion: 1.00
Nodes (2): is_categorical_dtype(), Check whether an array-like or dtype is of the Categorical dtype.      .. deprec

### Community 1725 - "Community 1725"
Cohesion: 1.00
Nodes (2): is_datetime64tz_dtype(), Check whether an array-like or dtype is of a DatetimeTZDtype dtype.      .. depr

### Community 1726 - "Community 1726"
Cohesion: 1.00
Nodes (2): is_ea_or_datetimelike_dtype(), Check for ExtensionDtype, datetime64 dtype, or timedelta64 dtype.      Notes

### Community 1727 - "Community 1727"
Cohesion: 1.00
Nodes (2): is_interval_dtype(), Check whether an array-like or dtype is of the Interval dtype.      .. deprecate

### Community 1728 - "Community 1728"
Cohesion: 1.00
Nodes (2): is_numeric_v_string_like(), Check if we are comparing a string-like object to a numeric ndarray.     NumPy d

### Community 1729 - "Community 1729"
Cohesion: 1.00
Nodes (2): is_period_dtype(), Check whether an array-like or dtype is of the Period dtype.      .. deprecated:

### Community 1730 - "Community 1730"
Cohesion: 1.00
Nodes (2): is_scipy_sparse(), Check whether an array-like is a scipy.sparse.spmatrix instance.      Parameters

### Community 1731 - "Community 1731"
Cohesion: 1.00
Nodes (2): is_sparse(), Check whether an array-like is a 1-D pandas sparse array.      .. deprecated:: 2

### Community 1732 - "Community 1732"
Cohesion: 1.00
Nodes (2): is_string_or_object_np_dtype(), Faster alternative to is_string_dtype, assumes we have an np.dtype object.

### Community 1733 - "Community 1733"
Cohesion: 1.00
Nodes (2): needs_i8_conversion(), Check whether the dtype should be converted to int64.      Dtype "needs" such a

### Community 1734 - "Community 1734"
Cohesion: 1.00
Nodes (2): Return None if all args are hashable, else raise a TypeError.      Parameters, validate_all_hashable()

### Community 1735 - "Community 1735"
Cohesion: 1.00
Nodes (2): get_is_dtype_funcs(), Get all functions in pandas.core.dtypes.common that     begin with 'is_' and end

### Community 1736 - "Community 1736"
Cohesion: 1.00
Nodes (2): convert list of string dtypes to EA dtype, to_ea_dtypes()

### Community 1737 - "Community 1737"
Cohesion: 1.00
Nodes (2): convert list of string dtypes to numpy dtype, to_numpy_dtypes()

### Community 1738 - "Community 1738"
Cohesion: 1.00
Nodes (1): For various parameters, we should get the same result whether we         limit t

### Community 1739 - "Community 1739"
Cohesion: 1.00
Nodes (1): Sheets can contain blank cells with no data. Some of our readers         were in

### Community 1740 - "Community 1740"
Cohesion: 1.00
Nodes (1): Test2DCompat

### Community 1741 - "Community 1741"
Cohesion: 1.00
Nodes (1): If the test fails, it at least won't hang.

### Community 1742 - "Community 1742"
Cohesion: 1.00
Nodes (1): Check that display logic is correct.          GH #37359          See description

### Community 1743 - "Community 1743"
Cohesion: 1.00
Nodes (2): biggie_df_fixture(), Fixture for a big mixed Dataframe and an empty Dataframe

### Community 1744 - "Community 1744"
Cohesion: 1.00
Nodes (1): Multiindex dataframe for testing multirow LaTeX macros.

### Community 1745 - "Community 1745"
Cohesion: 1.00
Nodes (1): Multicolumn dataframe for testing multicolumn LaTeX macros.

### Community 1746 - "Community 1746"
Cohesion: 1.00
Nodes (1): Check that every plot type gets properly collected.

### Community 1748 - "Community 1748"
Cohesion: 1.00
Nodes (2): df_cat(), DataFrame with multiple categorical columns and a column of integers.     Shorte

### Community 1749 - "Community 1749"
Cohesion: 1.00
Nodes (1): Returns a FrozenList with elements from other removed from self.          Parame

### Community 1750 - "Community 1750"
Cohesion: 1.00
Nodes (1): This method will not function because object is immutable.

### Community 1751 - "Community 1751"
Cohesion: 1.00
Nodes (1): Returns a FrozenList with other concatenated to the end of self.          Parame

### Community 1752 - "Community 1752"
Cohesion: 1.00
Nodes (2): maybe_droplevels(), Attempt to drop level or levels from the given index.      Parameters     ------

### Community 1753 - "Community 1753"
Cohesion: 1.00
Nodes (2): names_compat(), A decorator to allow either `name` or `names` keyword but not both.      This ma

### Community 1754 - "Community 1754"
Cohesion: 1.00
Nodes (1): Returns the indices that would sort the index and its         underlying data.

### Community 1755 - "Community 1755"
Cohesion: 1.00
Nodes (1): An int array that for performance reasons is created only when needed.

### Community 1756 - "Community 1756"
Cohesion: 1.00
Nodes (1): Get integer location for requested label.          Parameters         ----------

### Community 1757 - "Community 1757"
Cohesion: 1.00
Nodes (1): return if the index has unique values

### Community 1758 - "Community 1758"
Cohesion: 1.00
Nodes (1): Return an iterator of the values.          Returns         -------         itera

### Community 1759 - "Community 1759"
Cohesion: 1.00
Nodes (1): return the length of the RangeIndex

### Community 1760 - "Community 1760"
Cohesion: 1.00
Nodes (1): Memory usage of my values          Parameters         ----------         deep :

### Community 1761 - "Community 1761"
Cohesion: 1.00
Nodes (1): Return the number of bytes in the underlying data.

### Community 1762 - "Community 1762"
Cohesion: 1.00
Nodes (1): Should an integer key be treated as positional?

### Community 1763 - "Community 1763"
Cohesion: 1.00
Nodes (1): The value of the `start` parameter (``0`` if this was not supplied).          Th

### Community 1764 - "Community 1764"
Cohesion: 1.00
Nodes (1): The value of the `stop` parameter.          This property returns the `stop` val

### Community 1765 - "Community 1765"
Cohesion: 1.00
Nodes (1): Test that is_monotonic_decreasing is correct on slices.

### Community 1766 - "Community 1766"
Cohesion: 1.00
Nodes (2): any_dtype_for_small_pos_integer_indexes(), Dtypes that can be given to an Index with small positive integers.      This mea

### Community 1767 - "Community 1767"
Cohesion: 1.00
Nodes (2): Return a fixed frequency TimedeltaIndex with day as the default.      This funct, timedelta_range()

### Community 1768 - "Community 1768"
Cohesion: 1.00
Nodes (1): parse_datetime_string_with_reso return parameter if type not matched.         Pe

### Community 1769 - "Community 1769"
Cohesion: 1.00
Nodes (2): _check_where_equivalences(), test_where_dt64_2d()

### Community 1770 - "Community 1770"
Cohesion: 1.00
Nodes (1): Buffer size in bytes.

### Community 1771 - "Community 1771"
Cohesion: 1.00
Nodes (1): Device type and device ID for where the data in the buffer resides.         Uses

### Community 1772 - "Community 1772"
Cohesion: 1.00
Nodes (1): Produce DLPack capsule (see array API standard).          Raises:              -

### Community 1773 - "Community 1773"
Cohesion: 1.00
Nodes (1): Pointer to start of the buffer as an integer.

### Community 1774 - "Community 1774"
Cohesion: 1.00
Nodes (1): If the dtype is categorical, there are two options:         - There are only val

### Community 1775 - "Community 1775"
Cohesion: 1.00
Nodes (1): Return the missing value (or "null") representation the column dtype         use

### Community 1776 - "Community 1776"
Cohesion: 1.00
Nodes (1): Dtype description as a tuple ``(kind, bit-width, format string, endianness)``.

### Community 1777 - "Community 1777"
Cohesion: 1.00
Nodes (1): Return a dictionary containing the underlying buffers.          The returned dic

### Community 1778 - "Community 1778"
Cohesion: 1.00
Nodes (1): Number of null elements, if known.          Note: Arrow uses -1 to indicate "unk

### Community 1779 - "Community 1779"
Cohesion: 1.00
Nodes (1): Offset of first element.          May be > 0 if using chunks; for example for a

### Community 1780 - "Community 1780"
Cohesion: 1.00
Nodes (1): Size of the column, in elements.          Corresponds to DataFrame.num_rows() if

### Community 1781 - "Community 1781"
Cohesion: 1.00
Nodes (1): Return an iterator yielding the column names.

### Community 1782 - "Community 1782"
Cohesion: 1.00
Nodes (1): Return the column whose name is the indicated name.

### Community 1783 - "Community 1783"
Cohesion: 1.00
Nodes (1): Return the column at the indicated position.

### Community 1784 - "Community 1784"
Cohesion: 1.00
Nodes (1): Return an iterator yielding the columns.

### Community 1785 - "Community 1785"
Cohesion: 1.00
Nodes (1): Return the number of columns in the DataFrame.

### Community 1786 - "Community 1786"
Cohesion: 1.00
Nodes (1): Return the number of rows in the DataFrame, if available.

### Community 1787 - "Community 1787"
Cohesion: 1.00
Nodes (1): Create a new DataFrame by selecting a subset of columns by name.

### Community 1788 - "Community 1788"
Cohesion: 1.00
Nodes (1): Create a new DataFrame by selecting a subset of columns by index.

### Community 1789 - "Community 1789"
Cohesion: 1.00
Nodes (2): check_ndim(), ndim inference and validation.      Validates that values.ndim and ndim are cons

### Community 1790 - "Community 1790"
Cohesion: 1.00
Nodes (2): extract_pandas_array(), Ensure that we don't allow NumpyExtensionArray / NumpyEADtype in internals.

### Community 1791 - "Community 1791"
Cohesion: 1.00
Nodes (2): dataclasses_to_dicts(), Converts a list of dataclass instances to a list of dictionaries.      Parameter

### Community 1792 - "Community 1792"
Cohesion: 1.00
Nodes (2): Check if we should use nested_data_to_arrays., treat_as_nested()

### Community 1793 - "Community 1793"
Cohesion: 1.00
Nodes (1): Make sure that read_html ignores empty tables.

### Community 1794 - "Community 1794"
Cohesion: 1.00
Nodes (1): Don't fail with bs4 when there is a header and only one column         as descri

### Community 1795 - "Community 1795"
Cohesion: 1.00
Nodes (1): Ensure parser adds <tr> within <thead> on malformed HTML.

### Community 1796 - "Community 1796"
Cohesion: 1.00
Nodes (1): Make sure that read_html reads tfoot, containing td or th.         Ignores empty

### Community 1797 - "Community 1797"
Cohesion: 1.00
Nodes (2): create_and_load_types_postgresql(), postgresql_adbc_types()

### Community 1798 - "Community 1798"
Cohesion: 1.00
Nodes (1): The test does .astype(object).stack(). If we happen to have         any missing

### Community 1799 - "Community 1799"
Cohesion: 1.00
Nodes (1): This currently fails in NumPy on np.array(self, dtype=str) with          *** Val

### Community 1800 - "Community 1800"
Cohesion: 1.00
Nodes (1): This currently fails in Series.name.setter, since the         name must be hasha

### Community 1801 - "Community 1801"
Cohesion: 1.00
Nodes (1): This fails in Index._do_unique_check with          >   hash(val)         E   Typ

### Community 1803 - "Community 1803"
Cohesion: 1.00
Nodes (1): Test files dedicated to individual (stand-alone) Series methods  Ideally these f

### Community 1804 - "Community 1804"
Cohesion: 1.00
Nodes (1): Tests for non numerical index types  - object, period, timedelta         Note th

### Community 1805 - "Community 1805"
Cohesion: 1.00
Nodes (2): Due to new MultiIndex-ing behaviour in v0.14.0,     dicts with tuple keys passed, test_map_dict_with_tuple_keys()

### Community 1806 - "Community 1806"
Cohesion: 1.00
Nodes (2): Test Series.map with a dictionary subclass that defines __missing__,     i.e. se, test_map_dict_subclass_with_missing()

### Community 1807 - "Community 1807"
Cohesion: 1.00
Nodes (1): Test for #23305: to ensure category dtypes are maintained         after replace

### Community 1808 - "Community 1808"
Cohesion: 1.00
Nodes (1): Test to ensure category dtypes are maintained         after replace with dict va

### Community 1809 - "Community 1809"
Cohesion: 1.00
Nodes (2): seed_df(), test_series_groupby_value_counts()

### Community 1810 - "Community 1810"
Cohesion: 1.00
Nodes (2): maybe_cast_str_impl(), Converts numba UnicodeCharSeq (numpy string scalar) -> unicode type (string).

### Community 1811 - "Community 1811"
Cohesion: 1.00
Nodes (2): Convert an Index object to a native structure.      Note: Object dtype is not al, unbox_index()

### Community 1812 - "Community 1812"
Cohesion: 1.00
Nodes (2): any_signed_int_ea_dtype(), Parameterized fixture for any signed nullable integer dtype.      * 'Int8'     *

### Community 1813 - "Community 1813"
Cohesion: 1.00
Nodes (2): any_signed_int_numpy_dtype(), Parameterized fixture for signed integer dtypes.      * int     * 'int8'     * '

### Community 1814 - "Community 1814"
Cohesion: 1.00
Nodes (2): any_skipna_inferred_dtype(), Fixture for all inferred dtypes from _libs.lib.infer_dtype      The covered (inf

### Community 1815 - "Community 1815"
Cohesion: 1.00
Nodes (2): any_string_dtype(), Parametrized fixture for string dtypes.     * 'object'     * 'string[python]' (N

### Community 1816 - "Community 1816"
Cohesion: 1.00
Nodes (2): any_unsigned_int_numpy_dtype(), Parameterized fixture for unsigned integer dtypes.      * 'uint8'     * 'uint16'

### Community 1817 - "Community 1817"
Cohesion: 1.00
Nodes (2): as_index(), Fixture for 'as_index' argument in groupby.

### Community 1818 - "Community 1818"
Cohesion: 1.00
Nodes (2): ascending(), Fixture for 'ascending' argument in sort_values/sort_index/rank.

### Community 1819 - "Community 1819"
Cohesion: 1.00
Nodes (2): axis(), Fixture for returning the axis numbers of a DataFrame.

### Community 1820 - "Community 1820"
Cohesion: 1.00
Nodes (2): box_with_array(), Fixture to test behavior for Index, Series, DataFrame, and pandas Array     clas

### Community 1821 - "Community 1821"
Cohesion: 1.00
Nodes (2): bytes_dtype(), Parametrized fixture for bytes dtypes.      * bytes     * 'bytes'

### Community 1822 - "Community 1822"
Cohesion: 1.00
Nodes (2): cache(), Fixture for 'cache' argument in to_datetime.

### Community 1823 - "Community 1823"
Cohesion: 1.00
Nodes (2): closed(), Fixture for trying all interval closed parameters.

### Community 1824 - "Community 1824"
Cohesion: 1.00
Nodes (2): compare_operators_no_eq_ne(), Fixture for dunder names for compare operations except == and !=      * >=     *

### Community 1825 - "Community 1825"
Cohesion: 1.00
Nodes (2): comparison_op(), Fixture for operator module comparison functions.

### Community 1826 - "Community 1826"
Cohesion: 1.00
Nodes (2): complex_dtype(), Parameterized fixture for complex dtypes.      * complex     * 'complex64'     *

### Community 1827 - "Community 1827"
Cohesion: 1.00
Nodes (2): complex_or_float_dtype(), Parameterized fixture for complex and numpy float dtypes.      * complex     * '

### Community 1828 - "Community 1828"
Cohesion: 1.00
Nodes (2): compression_only(), Fixture for trying common compression types in compression tests excluding     u

### Community 1829 - "Community 1829"
Cohesion: 1.00
Nodes (2): compression(), Fixture for trying common compression types in compression tests.

### Community 1830 - "Community 1830"
Cohesion: 1.00
Nodes (2): configure_tests(), Configure settings for all tests and test modules.

### Community 1831 - "Community 1831"
Cohesion: 1.00
Nodes (2): _create_mi_with_dt64tz_level(), MultiIndex with a level that is a tzaware DatetimeIndex.

### Community 1832 - "Community 1832"
Cohesion: 1.00
Nodes (2): _create_multiindex(), MultiIndex used to test the general functionality of this object

### Community 1833 - "Community 1833"
Cohesion: 1.00
Nodes (2): datapath(), Get the path to a data file.      Parameters     ----------     path : str

### Community 1834 - "Community 1834"
Cohesion: 1.00
Nodes (2): datetime_series(), Fixture for Series of floats with DatetimeIndex

### Community 1835 - "Community 1835"
Cohesion: 1.00
Nodes (2): datetime64_dtype(), Parametrized fixture for datetime64 dtypes.      * 'datetime64[ns]'     * 'M8[ns

### Community 1836 - "Community 1836"
Cohesion: 1.00
Nodes (2): dict_subclass(), Fixture for a dictionary subclass.

### Community 1837 - "Community 1837"
Cohesion: 1.00
Nodes (2): dropna(), Boolean 'dropna' parameter.

### Community 1838 - "Community 1838"
Cohesion: 1.00
Nodes (2): ea_scalar_and_dtype(), Fixture that tests each scalar and datetime type.

### Community 1839 - "Community 1839"
Cohesion: 1.00
Nodes (1): fixed_now_ts()

### Community 1840 - "Community 1840"
Cohesion: 1.00
Nodes (2): float_ea_dtype(), Parameterized fixture for float dtypes.      * 'Float32'     * 'Float64'

### Community 1841 - "Community 1841"
Cohesion: 1.00
Nodes (2): float_frame(), Fixture for DataFrame of floats with index of unique strings      Columns are ['

### Community 1842 - "Community 1842"
Cohesion: 1.00
Nodes (2): frame_or_series(), Fixture to parametrize over DataFrame and Series.

### Community 1843 - "Community 1843"
Cohesion: 1.00
Nodes (2): inclusive_endpoints_fixture(), Fixture for trying all interval 'inclusive' parameters.

### Community 1844 - "Community 1844"
Cohesion: 1.00
Nodes (2): index_flat_sortable(), index_flat fixture, but excluding types that are not orderable.

### Community 1845 - "Community 1845"
Cohesion: 1.00
Nodes (2): index_flat(), index fixture, but excluding MultiIndex cases.

### Community 1846 - "Community 1846"
Cohesion: 1.00
Nodes (2): index_or_series_memory_obj(), Fixture for tests on indexes, series, series with a narrow dtype and     series

### Community 1847 - "Community 1847"
Cohesion: 1.00
Nodes (2): index_or_series_obj_orderable(), index_or_series_obj fixture, but excluding types that are not orderable.

### Community 1848 - "Community 1848"
Cohesion: 1.00
Nodes (2): index_or_series_obj(), Fixture for tests on indexes, series and series with a narrow dtype     copy to

### Community 1849 - "Community 1849"
Cohesion: 1.00
Nodes (2): index_or_series_or_array(), Fixture to parametrize over Index, Series, and ExtensionArray

### Community 1850 - "Community 1850"
Cohesion: 1.00
Nodes (2): index_or_series(), Fixture to parametrize over Index and Series, made necessary by a mypy     bug,

### Community 1851 - "Community 1851"
Cohesion: 1.00
Nodes (2): index_sortable(), index fixture, but excluding types that are not orderable.

### Community 1852 - "Community 1852"
Cohesion: 1.00
Nodes (2): index_with_missing_sortable(), index_with_missing fixture, but excluding types that are not orderable.

### Community 1853 - "Community 1853"
Cohesion: 1.00
Nodes (2): index_with_missing(), Fixture for indices with missing values.      Integer-dtype and empty cases are

### Community 1854 - "Community 1854"
Cohesion: 1.00
Nodes (2): indexer_al(), Parametrize over at.__setitem__, loc.__setitem__

### Community 1855 - "Community 1855"
Cohesion: 1.00
Nodes (2): indexer_ial(), Parametrize over iat.__setitem__, iloc.__setitem__

### Community 1856 - "Community 1856"
Cohesion: 1.00
Nodes (2): indexer_li(), Parametrize over loc.__getitem__, iloc.__getitem__

### Community 1857 - "Community 1857"
Cohesion: 1.00
Nodes (2): indexer_si(), Parametrize over __setitem__, iloc.__setitem__

### Community 1858 - "Community 1858"
Cohesion: 1.00
Nodes (2): indexer_sli(), Parametrize over __setitem__, loc.__setitem__, iloc.__setitem__

### Community 1859 - "Community 1859"
Cohesion: 1.00
Nodes (2): indexer_sl(), Parametrize over __setitem__, loc.__setitem__

### Community 1860 - "Community 1860"
Cohesion: 1.00
Nodes (2): index(), Fixture for many "simple" kinds of indices.      These indices are unlikely to c

### Community 1861 - "Community 1861"
Cohesion: 1.00
Nodes (2): int_frame(), Fixture for DataFrame of ints with index of unique strings      Columns are ['A'

### Community 1862 - "Community 1862"
Cohesion: 1.00
Nodes (2): ip(), Get an instance of IPython.InteractiveShell.      Will raise a skip if IPython i

### Community 1863 - "Community 1863"
Cohesion: 1.00
Nodes (2): join_type(), Fixture for trying all types of join operations.

### Community 1864 - "Community 1864"
Cohesion: 1.00
Nodes (2): keep(), Valid values for the 'keep' parameter used in     .duplicated or .drop_duplicate

### Community 1865 - "Community 1865"
Cohesion: 1.00
Nodes (2): lexsorted_two_level_string_multiindex(), 2-level MultiIndex, lexsorted, with string names.

### Community 1866 - "Community 1866"
Cohesion: 1.00
Nodes (2): mpl_cleanup(), Ensure Matplotlib is cleaned up around a test.      Before a test is run:      1

### Community 1867 - "Community 1867"
Cohesion: 1.00
Nodes (2): multiindex_dataframe_random_data(), DataFrame with 2 level MultiIndex with random data

### Community 1868 - "Community 1868"
Cohesion: 1.00
Nodes (2): multiindex_year_month_day_dataframe_random_data(), DataFrame with 3 level MultiIndex (year, month, day) covering     first 100 busi

### Community 1869 - "Community 1869"
Cohesion: 1.00
Nodes (2): na_action(), Fixture for 'na_action' argument in map.

### Community 1870 - "Community 1870"
Cohesion: 1.00
Nodes (2): names(), A 3-tuple of names, the first two for operands, the last for a result.

### Community 1871 - "Community 1871"
Cohesion: 1.00
Nodes (2): nogil(), Fixture for nogil keyword argument for numba.jit.

### Community 1872 - "Community 1872"
Cohesion: 1.00
Nodes (2): non_dict_mapping_subclass(), Fixture for a non-mapping dictionary subclass.

### Community 1873 - "Community 1873"
Cohesion: 1.00
Nodes (2): np_nat_fixture(), Fixture for each NaT type in numpy.

### Community 1874 - "Community 1874"
Cohesion: 1.00
Nodes (2): nselect_method(), Fixture for trying all nselect methods.

### Community 1875 - "Community 1875"
Cohesion: 1.00
Nodes (2): nullable_string_dtype(), Parametrized fixture for string dtypes.      * 'string[python]'     * 'string[py

### Community 1876 - "Community 1876"
Cohesion: 1.00
Nodes (2): nulls_fixture(), Fixture for each null type in pandas.

### Community 1877 - "Community 1877"
Cohesion: 1.00
Nodes (2): object_dtype(), Parametrized fixture for object dtypes.      * object     * 'object'

### Community 1878 - "Community 1878"
Cohesion: 1.00
Nodes (2): object_series(), Fixture for Series of dtype object with Index of unique strings

### Community 1879 - "Community 1879"
Cohesion: 1.00
Nodes (2): observed(), Pass in the observed keyword to groupby for [True, False]     This indicates whe

### Community 1880 - "Community 1880"
Cohesion: 1.00
Nodes (2): ordered(), Boolean 'ordered' parameter for Categorical.

### Community 1881 - "Community 1881"
Cohesion: 1.00
Nodes (2): other_closed(), Secondary closed fixture to allow parametrizing over all pairs of closed.

### Community 1882 - "Community 1882"
Cohesion: 1.00
Nodes (2): parallel(), Fixture for parallel keyword argument for numba.jit.

### Community 1883 - "Community 1883"
Cohesion: 1.00
Nodes (2): performance_warning(), Fixture to check if performance warnings are enabled. Either produces     ``Perf

### Community 1884 - "Community 1884"
Cohesion: 1.00
Nodes (2): pyarrow_string_dtype(), Parametrized fixture for string dtypes backed by Pyarrow.      * 'str[pyarrow]'

### Community 1885 - "Community 1885"
Cohesion: 1.00
Nodes (2): rand_series_with_duplicate_datetimeindex(), Fixture for Series with a DatetimeIndex that has duplicates.

### Community 1886 - "Community 1886"
Cohesion: 1.00
Nodes (2): rank_method(), Fixture for 'rank' argument in rank.

### Community 1887 - "Community 1887"
Cohesion: 1.00
Nodes (2): Returns the configuration for the test setting `--no-strict-data-files`., strict_data_files()

### Community 1888 - "Community 1888"
Cohesion: 1.00
Nodes (2): Fixture for trying timezones including default (None): {0}, tz_naive_fixture()

### Community 1889 - "Community 1889"
Cohesion: 1.00
Nodes (2): Fixture for trying explicit timezones: {0}, tz_aware_fixture()

### Community 1890 - "Community 1890"
Cohesion: 1.00
Nodes (2): Fixture to provide variants of UTC timezone strings and tzinfo objects., utc_fixture()

### Community 1891 - "Community 1891"
Cohesion: 1.00
Nodes (2): datetime64 units we support., unit()

### Community 1892 - "Community 1892"
Cohesion: 1.00
Nodes (2): Parametrized fixture for string dtypes.      * str     * 'str'     * 'U', string_dtype()

### Community 1893 - "Community 1893"
Cohesion: 1.00
Nodes (2): Parametrized fixture for string dtypes.     * 'string[python]' (NA variant), string_dtype_no_object()

### Community 1894 - "Community 1894"
Cohesion: 1.00
Nodes (2): Parametrized fixture for StringDtype storage and na_value.      * 'python' + pd., string_dtype_arguments()

### Community 1895 - "Community 1895"
Cohesion: 1.00
Nodes (2): Parametrized fixture for timedelta64 dtypes.      * 'timedelta64[ns]'     * 'm8[, timedelta64_dtype()

### Community 1896 - "Community 1896"
Cohesion: 1.00
Nodes (2): Fixture for Tick based datetime offsets available for a time series., tick_classes()

### Community 1897 - "Community 1897"
Cohesion: 1.00
Nodes (2): Simple fixture for testing keys in sorting methods.     Tests None (no key) and, sort_by_key()

### Community 1898 - "Community 1898"
Cohesion: 1.00
Nodes (2): Fixture to check if infer string option is enabled., using_infer_string()

### Community 1899 - "Community 1899"
Cohesion: 1.00
Nodes (2): tzinfo for Europe/Warsaw using pytz, dateutil, or zoneinfo., warsaw()

### Community 1900 - "Community 1900"
Cohesion: 1.00
Nodes (2): Generate a unique file for testing use. See link for removal policy.     https:/, temp_file()

### Community 1901 - "Community 1901"
Cohesion: 1.00
Nodes (2): Boolean 'sort' parameter., sort()

### Community 1902 - "Community 1902"
Cohesion: 1.00
Nodes (2): Boolean 'skipna' parameter., skipna()

### Community 1903 - "Community 1903"
Cohesion: 1.00
Nodes (2): Fixture that an array is writable., writable()

### Community 1904 - "Community 1904"
Cohesion: 1.00
Nodes (2): Fixture for each null type in pandas, each null type exactly once., unique_nulls_fixture()

### Community 1905 - "Community 1905"
Cohesion: 1.00
Nodes (2): Fixture for Series of floats with Index of unique strings, string_series()

### Community 1906 - "Community 1906"
Cohesion: 1.00
Nodes (2): iris(), The iris dataset as a DataFrame.

### Community 1907 - "Community 1907"
Cohesion: 1.00
Nodes (1): Tests for reductions where we want to test for matching behavior across Array, I

### Community 1908 - "Community 1908"
Cohesion: 1.00
Nodes (2): *this is an internal non-public method*      Returns the levels, labels and name, restore_dropped_levels_multijoin()

### Community 1910 - "Community 1910"
Cohesion: 1.00
Nodes (2): Errors in RLE/RDC decompression should propagate., test_rle_rdc_exceptions()

### Community 1911 - "Community 1911"
Cohesion: 1.00
Nodes (1): The percent of non- ``fill_value`` points, as decimal.          This is calculat

### Community 1912 - "Community 1912"
Cohesion: 1.00
Nodes (1): The number of non- ``fill_value`` points.          This property returns the num

### Community 1913 - "Community 1913"
Cohesion: 1.00
Nodes (1): Returns a Series containing counts of unique values.          Parameters

### Community 1914 - "Community 1914"
Cohesion: 1.00
Nodes (2): arr_data(), Fixture returning numpy array with valid and missing entries

### Community 1915 - "Community 1915"
Cohesion: 1.00
Nodes (2): arr(), Fixture returning SparseArray from 'arr_data

### Community 1916 - "Community 1916"
Cohesion: 1.00
Nodes (2): dtype(), Fixture giving StringDtype from parametrized storage and na_value arguments

### Community 1917 - "Community 1917"
Cohesion: 1.00
Nodes (2): assert_metadata_equivalent(), Check that ._metadata attributes are equivalent.

### Community 1919 - "Community 1919"
Cohesion: 1.00
Nodes (2): Cast a numeric column to object-dtype strings so that to_datetime with a     ``f, stringify_numeric_column()

### Community 1920 - "Community 1920"
Cohesion: 1.00
Nodes (2): Convert argument to a numeric type.      If the input is already of a numeric dt, to_numeric()

### Community 1921 - "Community 1921"
Cohesion: 1.00
Nodes (2): assert_fp_equal(), test_transform_broadcast()

### Community 1922 - "Community 1922"
Cohesion: 1.00
Nodes (2): Tests that the output does not contain the `<index>` field when the index of the, test_index_false_with_offset_input_index()

### Community 1923 - "Community 1923"
Cohesion: 1.00
Nodes (2): read_xml_iterparse_comp(), test_compression_read()

## Knowledge Gaps
- **1891 isolated node(s):** `algos/ directory is intended for individual functions from core.algorithms  In m`, `A subset of the cartesian product of cases have special motivations:      "nans"`, `# TODO: GH#33198 the setting here shouldn't need two steps`, `Benchmarks specifically targeting our numba aggregation algorithms     (using a`, `These benchmarks are for Series and DataFrame indexing methods.  For the lower-l` (+1886 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 12`** (1 nodes): `pandas_core_arrays_arrow_extension_types`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (1 nodes): `TestDataFrameConstructors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (1 nodes): `NDFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (1 nodes): `TestDataFramePlots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (2 nodes): `test_constructor()`, `TestSeriesConstructors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `# TODO: test the numeric_only=True case`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (1 nodes): `# TODO: the result below is wrong, should be fixed (GH53325)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `TestPandasContainer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (2 nodes): `sqlalchemy`, `sqlite3`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (1 nodes): `TestIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (1 nodes): `TestTSPlot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (2 nodes): `# TODO: Make inplace by using out parameter of ndarray.round?`, `# TODO: Cannot rely on Numpy returning view after version 2.3`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (2 nodes): `Test that bar and line plots with the same x values are superposed         and t`, `TestSeriesPlots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (1 nodes): `TestLocBaseIndependent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (1 nodes): `TestStata`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (1 nodes): `TestPivotTable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (1 nodes): `test .agg behavior / note that .apply is tested generally in test_groupby.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (1 nodes): `TestDataFrameIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (1 nodes): `TestDataFrameReplace`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (1 nodes): `# TODO: implemented SeriesGroupBy.corrwith. See GH 32293`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 66`** (2 nodes): `lzma`, `xml_etree_elementtree`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 71`** (2 nodes): `Tests Independent Of Base Class`, `TestiLocBaseIndependent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 72`** (1 nodes): `pandas_tests_apply_conftest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 74`** (2 nodes): `flavor_read_html()`, `TestReadHtml`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 75`** (2 nodes): `BaseMethodsTests`, `Various Series and DataFrame methods.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 79`** (1 nodes): `TestDataFrameColor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 81`** (1 nodes): `TestAsOfMerge`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 82`** (1 nodes): `TestToDatetime`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 83`** (1 nodes): `TestCategoricalConstructors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 84`** (1 nodes): `TestDataFrameAnalytics`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 85`** (1 nodes): `TestDataFrameToCSV`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 87`** (1 nodes): `TestStyler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 89`** (1 nodes): `TestAstype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 92`** (1 nodes): `# TODO: constructing DatetimeIndex with dtype="M8[s]" without truncating`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 94`** (1 nodes): `TestUltraJSONTests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 95`** (1 nodes): `pandas_tests_strings`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 98`** (1 nodes): `TestSeriesReplace`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 104`** (1 nodes): `TestExcelWriter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 107`** (1 nodes): `TestDataFrameSetItem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 108`** (1 nodes): `TestSeriesInterpolateData`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 109`** (2 nodes): `_copy_array_with_layout()`, `test_mask_memory_layout_mismatch()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 117`** (1 nodes): `TestPeriodIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 121`** (1 nodes): `TestReaders`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 122`** (1 nodes): `hashlib`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 123`** (1 nodes): `TestDataFrameSelectReindex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 127`** (1 nodes): `# TODO: this is raising in constructing a Categorical when calling`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 128`** (2 nodes): `Tests for Timedelta methods:          __mul__, __rmul__,         __div__, __rdiv`, `TestTimedeltaMultiplicationDivision`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 135`** (1 nodes): `TestDatetimeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 140`** (2 nodes): `TestBase`, `TestNumericBase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 143`** (1 nodes): `TestDataFrameShift`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 146`** (1 nodes): `TestTimedeltaArraylikeMulDivOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 148`** (2 nodes): `BaseSetitemTests`, `Fixture for an indexer to pass to obj.loc to get/set the full length of the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 153`** (1 nodes): `TestInferFreqDeprecation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 155`** (1 nodes): `TestTimedeltas`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 159`** (1 nodes): `TestResetIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 162`** (2 nodes): `get_dir()`, `TestSeriesDatetimeValues`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 163`** (1 nodes): `Tests that work on both the Python and C engines but do not have a specific clas`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 164`** (1 nodes): `TestTypeInference`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 165`** (2 nodes): `test_cast_pontwise_result_decimal_nan()`, `TestArrowArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 166`** (1 nodes): `TestFillNA`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 167`** (1 nodes): `TestRename`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 168`** (1 nodes): `these are systematically testing all of the args to value_counts with different`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 170`** (1 nodes): `This module tests the functionality of StringArray and ArrowStringArray. Tests f`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 171`** (1 nodes): `TestDataFrameReshape`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 172`** (2 nodes): `Interval specific tests for is_unique in addition to base class tests`, `TestIntervalIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 173`** (1 nodes): `TestRangeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 174`** (1 nodes): `TestGetDummies`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 175`** (1 nodes): `TestRolling`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 178`** (2 nodes): `TestDataFrameToString`, `TestSeriesToString`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 179`** (2 nodes): `Tests that apply specifically to the CParser. Unless specifically stated as a CP`, `# NOTE: This is only true for the C engine, not Python engine.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 184`** (2 nodes): `dtype()`, `TestNumpyExtensionArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 185`** (1 nodes): `TestDataFrameRepr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 187`** (2 nodes): `pandas_io_sas_sas7bdat`, `pandas_io_sas_sas_constants`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 188`** (1 nodes): `TestPeriodIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 189`** (2 nodes): `Cases where ``Series.argmax`` and related should raise an exception`, `TestSeriesReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 194`** (1 nodes): `TestJSONArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 201`** (2 nodes): `PeriodIndex.__sub__ and __isub__ with several representations of         the int`, `TestPeriodIndexArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 203`** (1 nodes): `TestGrouping`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 207`** (1 nodes): `# TODO: standardize return type for MultiIndex.get_loc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 209`** (1 nodes): `TestOperations`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 210`** (1 nodes): `TestFromRecords`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 212`** (2 nodes): `This test will fail for:             period:                 since period isn't`, `TestDataFramePlotsSubplots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 213`** (1 nodes): `TestStackUnstackMultiLevel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 215`** (2 nodes): `TestDataFrameIsIn`, `TestSeriesIsIn`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 217`** (1 nodes): `Methods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 218`** (1 nodes): `TestDataFrameFormatting`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 220`** (2 nodes): `TestSample`, `TestSampleDataFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 222`** (2 nodes): `BaseGetitemTests`, `Tests for ExtensionArray.__getitem__.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 226`** (1 nodes): `TestToDatetimeMisc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 228`** (1 nodes): `TestCategoricalConcat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 232`** (1 nodes): `TestJoin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 235`** (1 nodes): `Tests that apply specifically to the Python parser. Unless specifically stated a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 237`** (1 nodes): `TestToDatetimeDataFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 238`** (1 nodes): `TestRollingTS`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 244`** (1 nodes): `Tests that the file header is properly handled or inferred during parsing for al`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 245`** (1 nodes): `TestDataFramePlots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 255`** (1 nodes): `TestLocSetitemWithExpansion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 257`** (1 nodes): `pandas_core_util_hashing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 258`** (2 nodes): `Tests that NA values are properly handled during parsing for all of the parsers`, `# TODO: this test isn't about the na_values keyword, it is about the empty entri`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 263`** (1 nodes): `TestInference`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 265`** (1 nodes): `TestDataFrameSubclassing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 267`** (2 nodes): `pure get/set item & fancy indexing`, `TestFancy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 270`** (1 nodes): `TestMelt`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 272`** (1 nodes): `# TODO: should this raise TypeError`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 273`** (1 nodes): `TestTimestampConstructors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 276`** (2 nodes): `check_round_trip()`, `TestParquetPyArrow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 281`** (1 nodes): `SharedTests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 284`** (2 nodes): `_eval_single_bin()`, `TestEval`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 293`** (1 nodes): `TestCrosstab`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 296`** (1 nodes): `TestDatetimeArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 298`** (2 nodes): `# TODO: Block splitting would allow us to avoid copying b`, `# TODO: Add these in a further optimization`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 303`** (1 nodes): `TestGroupBy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 304`** (1 nodes): `TestDataFrameIndexingWhere`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 305`** (2 nodes): `# TODO: assert something?`, `TestDataFrameAlign`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 306`** (1 nodes): `TestDataFrameInterpolate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 307`** (1 nodes): `TestDataFrameSortIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 309`** (1 nodes): `TestFactorize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 310`** (2 nodes): `TestDatetime64NaNOps`, `TestnanopsDataFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 311`** (1 nodes): `TestNonNano`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 316`** (1 nodes): `TestDatetimeIndexSetOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 319`** (1 nodes): `TestSeriesFillNA`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 320`** (1 nodes): `TestDataFrameQuantile`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 323`** (1 nodes): `TestSeriesRepr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 324`** (2 nodes): `Tests for Timedelta methods:          __add__, __radd__,         __sub__, __rsub`, `TestTimedeltaAdditionSubtraction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 325`** (1 nodes): `Tests the usecols functionality during parsing for all of the parsers defined in`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 330`** (1 nodes): `TestDatetimeIndexOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 332`** (1 nodes): `TestSparseArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 334`** (1 nodes): `TestDataFrameMisc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 336`** (2 nodes): `Also test support for datetime64[ns] in Series / DataFrame`, `TestDatetimeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 337`** (1 nodes): `TestJSONNormalize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 339`** (1 nodes): `TestDataFrameDrop`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 340`** (1 nodes): `TestTZLocalize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 341`** (2 nodes): `assert_array_dicts_equal()`, `TestTextReader`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 344`** (1 nodes): `test all other .agg behavior`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 345`** (1 nodes): `TestConcatenate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 346`** (2 nodes): `dtypes_for_minmax()`, `Fixture of dtypes with min and max values used for testing     cummin and cummax`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 349`** (1 nodes): `TestDataFrameCombineFirst`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 350`** (2 nodes): `test_join()`, `TestDataFrameJoin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 361`** (1 nodes): `TestIsValidNAForDtype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 363`** (2 nodes): `The tests in this package are to ensure the proper resultant dtypes of set opera`, `# TODO: pin down desired dtype; do we want it to be commutative?`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 364`** (1 nodes): `TestXSWithMultiIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 366`** (2 nodes): `TestGetIndexer`, `TestGetLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 368`** (2 nodes): `TestJoinMultiMulti`, `TestMergeMulti`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 369`** (1 nodes): `pandas_tests_test_register_accessor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 370`** (1 nodes): `TestPeriodConstruction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 371`** (1 nodes): `TestDataFrameGroupByPlots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 375`** (1 nodes): `TestCategoricalRepr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 376`** (1 nodes): `TestConfig`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 378`** (2 nodes): `TestBusinessDateRange`, `TestCustomDateRange`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 379`** (1 nodes): `TestSlicing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 380`** (1 nodes): `TestCategoricalDtypeParametrized`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 383`** (1 nodes): `TestCategoricalIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 386`** (1 nodes): `TestDataFrameToDict`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 387`** (1 nodes): `TestDataFramePlots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 389`** (1 nodes): `TestTimedeltas`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 390`** (1 nodes): `TestTimeConversionFormats`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 393`** (1 nodes): `TestNonNano`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 394`** (2 nodes): `Though Index.fillna and Series.fillna has separate impl, test here to confirm th`, `pandas_tests_base_common`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 395`** (1 nodes): `Iteration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 399`** (1 nodes): `TestDateRangeNonTickFreq`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 406`** (1 nodes): `TestDataFrameDiff`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 407`** (1 nodes): `TestDataFrameSortValues`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 408`** (1 nodes): `TestToPeriod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 409`** (1 nodes): `TestMultiIndexLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 410`** (1 nodes): `_check_plot_works()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 411`** (1 nodes): `TestDataFramePlots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 412`** (1 nodes): `TestSeriesPlots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 413`** (1 nodes): `TestUnique`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 414`** (1 nodes): `TestToDatetimeUnit`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 418`** (2 nodes): `BaseDtypeTests`, `Base class for ExtensionDtype classes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 423`** (1 nodes): `pandas_tests_copy_view_util`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 426`** (1 nodes): `TestStringArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 430`** (1 nodes): `TestLocSeries`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 432`** (2 nodes): `HDF`, `HDFStoreDataFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 435`** (1 nodes): `TestDatetimeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 436`** (2 nodes): `# TODO: these can work but need to update ser construction.`, `# TODO: use ser.replace(np.nan, NA) once that works`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 437`** (1 nodes): `TestSelectDtypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 440`** (2 nodes): `Test properties such as year, month, weekday, etc....`, `TestPeriodProperties`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 442`** (1 nodes): `TestSeriesMisc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 445`** (1 nodes): `TestNonNano`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 448`** (1 nodes): `TestTimedeltaArraylikeAddSubOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 449`** (1 nodes): `TestNonNano`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 460`** (1 nodes): `TestFrameArithmeticUnsorted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 461`** (1 nodes): `TestFrameFlexArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 462`** (1 nodes): `TestCounting`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 463`** (1 nodes): `# TODO: Should this be 3?`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 465`** (1 nodes): `TestSetOpsUnsorted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 466`** (1 nodes): `TestChaining`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 468`** (1 nodes): `TestTableOrient`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 472`** (1 nodes): `TestSetIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 473`** (2 nodes): `_get_with_delta()`, `TestToTimestamp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 474`** (2 nodes): `dataframe_with_duplicate_index()`, `Fixture for DataFrame used in tests for gh-4145 and gh-4146`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 475`** (1 nodes): `TestGetIndexer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 476`** (1 nodes): `pandas_io_formats_style`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 477`** (1 nodes): `Tests that the specified index column (a.k.a "index_col") is properly handled or`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 478`** (1 nodes): `TestUnionCategoricals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 479`** (1 nodes): `TestConstructors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 480`** (2 nodes): `Testing that we work in the downstream packages`, `# TODO: could check with arraylike of Period objects`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 483`** (1 nodes): `TestMultiplicationDivision`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 484`** (1 nodes): `Validate / convert value to be StringArray compatible.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 487`** (1 nodes): `TestCategoricalAnalytics`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 488`** (2 nodes): `TestCategoricalOps`, `TestCategoricalOpsWithFactor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 489`** (2 nodes): `Test common dtype coercion rules between concat and append.`, `TestConcatAppendCommon`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 494`** (1 nodes): `pandas_core_reshape`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 495`** (1 nodes): `# TODO: desired behavior when operating with boolean?  defer?`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 498`** (2 nodes): `assert_framelist_equal()`, `test_same_ordering()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 499`** (1 nodes): `TestBasic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 500`** (1 nodes): `JSONArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 504`** (2 nodes): `# TODO: de-duplicate with test_get_loc_duplicates above?`, `# TODO: Try creating a UnicodeDecodeError in exception message`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 505`** (2 nodes): `_create_offset()`, `TestCommon`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 506`** (1 nodes): `TestDataFrameGroupByPlots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 509`** (1 nodes): `TestSeriesLogicalOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 512`** (2 nodes): `Replicate result expected in GH #6297`, `test_rolling_max_gh6297()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 517`** (2 nodes): `BaseMissingTests`, `Whether the EA honors the copy keyword in methods like fillna.          EAs that`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 520`** (1 nodes): `TestDataFrameBlockInternals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 521`** (1 nodes): `TestCommon`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 525`** (1 nodes): `TestFeather`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 527`** (1 nodes): `TestTimestampRound`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 528`** (1 nodes): `TestDataFrameUpdate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 530`** (1 nodes): `TestMultiIndexBasic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 532`** (2 nodes): `Test frequency conversion of date objects`, `TestFreqConversion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 533`** (1 nodes): `TestPeriodMethods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 535`** (1 nodes): `ultrajson`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 536`** (1 nodes): `TestWideToLong`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 537`** (1 nodes): `TestPivot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 539`** (2 nodes): `_permute()`, `TestSeriesArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 541`** (1 nodes): `TestMultiLevel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 542`** (1 nodes): `TestTimestampArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 543`** (1 nodes): `TestOrigin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 545`** (2 nodes): `TestNamedAggregationDataFrame`, `TestNamedAggregationSeries`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 546`** (1 nodes): `TestDatetime64Arithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 549`** (1 nodes): `TestCategoricalAPI`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 550`** (2 nodes): `DateArray`, `DateDtype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 554`** (1 nodes): `TestDataFrameConstructorWithDatetimeTZ`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 560`** (2 nodes): `check_partition_names()`, `TestParquetFastParquet`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 562`** (1 nodes): `TestAsFreq`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 564`** (1 nodes): `TestRank`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 565`** (1 nodes): `# NOTE: if MI representation changes, may make sense to allow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 569`** (2 nodes): `_offset()`, `TestCustomBusinessHour`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 570`** (1 nodes): `TestDataFrameGroupByPlots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 573`** (1 nodes): `TestTimedeltaIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 576`** (1 nodes): `TestArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 578`** (2 nodes): `BaseInterfaceTests`, `Tests that the basic interface is satisfied.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 580`** (1 nodes): `MultiIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 582`** (1 nodes): `TestAppend`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 583`** (2 nodes): `48510 `concat` to an empty EA should maintain type EA dtype.`, `TestEmptyConcat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 585`** (1 nodes): `Get Addition of DataFrame and other, column-wise.          Equivalent to ``DataF`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 586`** (1 nodes): `TestDecimalArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 590`** (1 nodes): `TestDataFrameEval`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 592`** (1 nodes): `TestDtypeEnforced`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 593`** (1 nodes): `TestSeriesGetitemScalars`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 594`** (1 nodes): `TestLocWithMultiIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 596`** (1 nodes): `TestIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 597`** (1 nodes): `TestMergeDtypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 598`** (1 nodes): `TestConvertDtypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 599`** (1 nodes): `TestDataFrameCorrWith`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 600`** (1 nodes): `TestTZConvert`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 602`** (1 nodes): `TestSeriesPeriod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 606`** (2 nodes): `Tests for GH#33603 - string resolution for TimedeltaIndex slicing.`, `TestStringSliceResolution`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 613`** (1 nodes): `TimelikeOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 614`** (2 nodes): `Column`, `PandasColumn`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 622`** (1 nodes): `TestIsNA`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 625`** (1 nodes): `TestIteration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 626`** (1 nodes): `TestDataFrameNonuniqueIndexes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 630`** (2 nodes): `test coercion triggered by where`, `TestWhereCoercion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 631`** (2 nodes): `test coercion triggered by fillna`, `TestFillnaSeriesCoercion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 632`** (1 nodes): `TestGetitemBooleanMask`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 633`** (2 nodes): `Tests for DataFrame.mask; tests DataFrame.where as a side-effect.`, `TestDataFrameMask`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 634`** (1 nodes): `TestEmptyFrameSetitemExpansion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 635`** (1 nodes): `pandas_io`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 636`** (1 nodes): `Render`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 638`** (1 nodes): `TestSeriesQuantile`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 639`** (1 nodes): `TestDataFrameToRecords`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 640`** (2 nodes): `_distant_date_only_for_zoneinfo()`, `TestTimestampTZLocalize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 641`** (1 nodes): `# TODO: reshape`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 644`** (2 nodes): `TestFrameAccessor`, `TestSeriesAccessor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 645`** (1 nodes): `# TODO: Strimg option, this should return string dtype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 646`** (1 nodes): `TestTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 649`** (1 nodes): `test cython .agg behavior`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 651`** (2 nodes): `TestPeriodArray`, `TestTimedeltaArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 654`** (2 nodes): `Fixture that provides a CategoricalIndex.`, `TestCategoricalIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 655`** (1 nodes): `TestTimeSeries`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 656`** (1 nodes): `TestIntervalDtype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 657`** (1 nodes): `TestFrameArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 658`** (1 nodes): `TestNDFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 659`** (1 nodes): `TestMixedIntIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 662`** (1 nodes): `TestNestedToRecord`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 663`** (2 nodes): `# TODO: moved from test_algos; may be redundancies with other tests`, `tracemalloc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 666`** (1 nodes): `TestDataFrameMissingData`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 667`** (1 nodes): `TestTimestampReplace`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 668`** (1 nodes): `TestTranspose`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 671`** (1 nodes): `TestJoin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 672`** (1 nodes): `TestIndexReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 674`** (1 nodes): `TestSeriesCumulativeOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 675`** (2 nodes): `Fixture returning SparseArray with integer entries and 'fill_value=0`, `zarr()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 676`** (1 nodes): `TestSafeSort`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 677`** (1 nodes): `# TODO: Test more than just reductions (e.g. actually test transformations once`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 681`** (1 nodes): `BaseConstructorsTests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 682`** (1 nodes): `TestDatetimeConcat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 683`** (1 nodes): `TestTimezoneConcat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 684`** (1 nodes): `TestMultiIndexConcat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 687`** (1 nodes): `TestDatetimeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 688`** (2 nodes): `# TODO: moved from test_datetimelike; de-duplicate with version below`, `# TODO: moved from test_datetimelike; dedup with version below`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 693`** (2 nodes): `get1()`, `TestFromScalar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 694`** (2 nodes): `TestBoxWithBy`, `TestHistWithBy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 697`** (1 nodes): `TestIndexConstructorInference`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 698`** (1 nodes): `TestLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 701`** (2 nodes): `build_kwargs()`, `TestClipboard`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 702`** (1 nodes): `TestNumpyJSONTests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 703`** (1 nodes): `TestAstypeCategorical`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 704`** (1 nodes): `TestDataFrameCorr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 705`** (1 nodes): `TestGetLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 706`** (2 nodes): `check_level_names()`, `test_changing_names()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 707`** (1 nodes): `TestMultiIndexSlicers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 708`** (1 nodes): `Tests compressed data parsing functionality for all of the parsers defined in pa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 709`** (2 nodes): `_compare_with_tz()`, `test_append_with_timezones()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 710`** (1 nodes): `TestRangeIndexSetOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 711`** (1 nodes): `TestSeriesMode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 713`** (1 nodes): `TestTimedeltaIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 716`** (2 nodes): `compare_op()`, `TestAdditionSubtraction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 717`** (1 nodes): `TestTimedelta64ArithmeticUnsorted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 720`** (1 nodes): `TestDataFrameConcat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 721`** (1 nodes): `TestFromDict`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 722`** (1 nodes): `Reversed Operations not available in the stdlib operator module. Defining these`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 724`** (1 nodes): `TestCategoricalDtype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 725`** (1 nodes): `TestReprHTML`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 727`** (1 nodes): `TestDatetimeLike`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 728`** (2 nodes): `test index's coercion triggered by assign key`, `TestSetitemCoercion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 730`** (1 nodes): `TestMisc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 731`** (1 nodes): `TestDataFrameSetitemCopyViewSemantics`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 732`** (1 nodes): `TestSetitemBooleanMask`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 733`** (1 nodes): `TestIntervalRange`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 735`** (2 nodes): `TestBuildSchema`, `TestTableOrientReader`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 736`** (1 nodes): `TestTableSchemaType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 739`** (2 nodes): `Should process np.nan argument as None`, `TestDataFrameClip`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 742`** (1 nodes): `TestInsert`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 743`** (1 nodes): `TestSeriesRank`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 745`** (2 nodes): `Factory function to create simple 3 x 3 dataframe with     both columns and row`, `simple_multiindex_dataframe()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 746`** (2 nodes): `TestCustomBusinessMonthBegin`, `TestCustomBusinessMonthEnd`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 747`** (1 nodes): `TestDateOffset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 749`** (1 nodes): `TestPeriodArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 750`** (2 nodes): `TestDateTimeConverter`, `TestPeriodConverter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 751`** (1 nodes): `TestSeriesComparison`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 752`** (1 nodes): `TestSparseArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 754`** (2 nodes): `tests solely that the result is the same whether or not numexpr is         enabl`, `TestExpressions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 756`** (1 nodes): `Tests for helper functions in the cython tslibs.offsets`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 757`** (1 nodes): `TestArrayToTimedelta64`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 759`** (1 nodes): `TestDatetimeIndexArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 760`** (1 nodes): `TestDatetimeIndexComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 765`** (2 nodes): `CheckDtypes`, `SelectDtypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 768`** (1 nodes): `TestAstype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 769`** (1 nodes): `TestCategoricalIndexReprStringCategories`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 773`** (1 nodes): `TestDatetimeTZDtype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 774`** (1 nodes): `# TODO: should this be object with `not using_nan_is_na` to avoid`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 775`** (1 nodes): `TestToLatex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 776`** (1 nodes): `TestFrameLegend`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 779`** (1 nodes): `TestFrozenList`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 780`** (1 nodes): `TestPartialSetting`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 782`** (2 nodes): `Tests for the pseudo-public API implemented in internals/api.py and exposed in c`, `pandas_api_internals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 783`** (1 nodes): `TestBlockPlacement`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 784`** (2 nodes): `Fixture providing a Series with an IntervalIndex.`, `TestIntervalIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 785`** (2 nodes): `shared endpoints are marked as overlapping`, `TestIntervalTree`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 789`** (2 nodes): `TestHashTable`, `TestHashTableWithNans`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 791`** (1 nodes): `TestMergeOrdered`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 792`** (1 nodes): `TestMergeCategorical`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 793`** (2 nodes): `Should process np.nan argument as None`, `TestSeriesClip`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 794`** (2 nodes): `assert_check_nselect_boundary()`, `TestSeriesNLargestNSmallest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 799`** (1 nodes): `TestSeriesStatReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 800`** (1 nodes): `TestTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 802`** (1 nodes): `TestReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 803`** (1 nodes): `TestMode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 804`** (1 nodes): `TestValueCounts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 806`** (1 nodes): `TestTimestampComparison`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 807`** (1 nodes): `TestTimestampProperties`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 810`** (1 nodes): `TestDatetime64DateOffsetArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 811`** (2 nodes): `Test PeriodIndex and Period Series Ops consistency`, `TestPeriodIndexSeriesMethods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 813`** (2 nodes): `DataFrameNumericIndexing`, `DataFrameStringIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 816`** (1 nodes): `TestCategoricalIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 819`** (1 nodes): `TestSeriesConcat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 820`** (2 nodes): `Fixture returning DatetimeArray with parametrized timezones`, `TestReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 821`** (1 nodes): `TestDatetimeIndexTimezones`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 823`** (1 nodes): `TestIntervalArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 824`** (1 nodes): `TestDataFrameQueryStrings`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 825`** (1 nodes): `TestDataFrameUnaryOperators`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 827`** (1 nodes): `TestLocILocDataFrameCategorical`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 828`** (1 nodes): `TestDataFrameSetItemWithExpansion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 835`** (1 nodes): `TestTimedeltaIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 836`** (1 nodes): `TestSeriesConvertDtypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 837`** (1 nodes): `TestDatetimeIndexShift`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 838`** (1 nodes): `TestSeriesSortIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 839`** (1 nodes): `TestDataFrameValues`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 840`** (1 nodes): `TestRepr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 842`** (1 nodes): `TestS3`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 844`** (2 nodes): `numeric_as_float()`, `TestXport`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 845`** (1 nodes): `TestTimedeltas`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 847`** (1 nodes): `TestTimestampSeriesArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 848`** (1 nodes): `TestDatetimeArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 849`** (1 nodes): `TestReshape`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 851`** (1 nodes): `Constructor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 852`** (2 nodes): `Eval`, `Query`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 853`** (1 nodes): `Range`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 855`** (1 nodes): `TestTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 856`** (1 nodes): `TestMath`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 858`** (1 nodes): `TestDatetimeIndexRendering`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 859`** (1 nodes): `TestGetLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 860`** (1 nodes): `TestJoin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 861`** (2 nodes): `TestBusinessDatetimeIndex`, `TestCustomDatetimeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 862`** (2 nodes): `dateutil_parser`, `Tests column conversion functionality during parsing for all of the parsers defi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 864`** (1 nodes): `TestPeriodDtype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 866`** (2 nodes): `Tests for write_only mode (GH#41681).`, `TestWriteOnly`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 867`** (1 nodes): `TestCategorical`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 868`** (1 nodes): `TestDatetimeArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 870`** (2 nodes): `Parameters:         -----------         formatter: EngFormatter under test`, `TestEngFormatter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 872`** (1 nodes): `TestDataFrameLogicalOperators`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 875`** (2 nodes): `Tests for groupby operations on SparseArray columns (GH#36123).`, `TestSparseGroupby`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 877`** (1 nodes): `TestAtErrors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 878`** (2 nodes): `test coercion triggered by insert`, `TestInsertIndexCoercion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 879`** (1 nodes): `TestGet`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 880`** (1 nodes): `TestSeriesGetitemSlices`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 881`** (1 nodes): `TestDataFrameSetItemBooleanMask`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 884`** (2 nodes): `TestHelpFunctions`, `TestHelpFunctionsWithNans`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 886`** (1 nodes): `TestAtTime`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 887`** (1 nodes): `TestBetweenTime`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 888`** (1 nodes): `TestCombineFirst`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 890`** (1 nodes): `TestNLargestNSmallest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 891`** (1 nodes): `TestQuantileExtensionDtype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 892`** (1 nodes): `TestSeriesSortIndexKey`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 893`** (1 nodes): `TestDataFrameSortKey`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 894`** (1 nodes): `TestSeriesValueCounts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 895`** (1 nodes): `TestGetIndexer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 897`** (1 nodes): `TestMultiIndexPartial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 900`** (1 nodes): `Tests that duplicate columns are handled appropriately when parsed by the CSV en`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 901`** (1 nodes): `TestPeriodIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 902`** (1 nodes): `TestGetIndexer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 903`** (1 nodes): `TestReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 905`** (1 nodes): `TestCategoricalRepr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 907`** (1 nodes): `TestAstype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 909`** (2 nodes): `Foo`, `test_AbstractMethodError_classmethod()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 910`** (1 nodes): `TestReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 911`** (1 nodes): `TestTimestampClassMethodConstructors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 912`** (1 nodes): `TestTimestamp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 914`** (1 nodes): `TimedeltaConstructor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 919`** (1 nodes): `TestCatAccessor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 921`** (1 nodes): `TestNumericArithmeticUnsorted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 922`** (2 nodes): `BaseCastingTests`, `Casting to and from ExtensionDtypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 923`** (2 nodes): `BaseGroupbyTests`, `Groupby-specific tests.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 924`** (2 nodes): `BaseReduceTests`, `Reduction specific tests. Generally these only     make sense for numeric/boolea`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 925`** (1 nodes): `TestToIterable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 926`** (1 nodes): `Ops2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 927`** (1 nodes): `IndexCache`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 932`** (1 nodes): `TestCategoricalDtypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 933`** (1 nodes): `TestCategoricalMissing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 938`** (1 nodes): `TestRoundTrip`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 941`** (2 nodes): `Dataframe with special characters for testing chars escaping.`, `TestToLatexEscape`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 942`** (1 nodes): `TestDataFrameToStringFormatters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 943`** (1 nodes): `TestFrameFlexComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 945`** (1 nodes): `TestSelection`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 946`** (1 nodes): `TestValidateIndices`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 947`** (1 nodes): `TestLabelSlicing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 948`** (1 nodes): `TestLocBooleanMask`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 949`** (1 nodes): `TestAtAndiAT`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 950`** (1 nodes): `TestSetitemWithExpansion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 951`** (1 nodes): `TestDataFrameTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 953`** (2 nodes): `NA values are marked as False`, `TestOverlaps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 954`** (1 nodes): `TestIceberg`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 957`** (1 nodes): `TestDataFrameRound`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 958`** (1 nodes): `TestDatetimeIndexRound`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 959`** (1 nodes): `TestSeriesRound`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 960`** (1 nodes): `TestTimedeltaRound`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 962`** (1 nodes): `TestSeriesToCSV`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 965`** (1 nodes): `TestGetLevelValues`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 968`** (1 nodes): `TestSetOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 974`** (1 nodes): `TestGetItem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 975`** (2 nodes): `_permute()`, `TestPeriodIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 976`** (1 nodes): `TestGetStandardColors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 977`** (1 nodes): `TestRangeIndexConstructors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 980`** (2 nodes): `Convert SparseArray to a NumPy array.          Returns         -------         a`, `Cumulative sum of non-NA/null values.          When performing the cumulative su`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 981`** (1 nodes): `TestSparseArrayAnalytics`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 982`** (2 nodes): `Tests for GH#56505 - fast path using PyArrow cast for int/bool.`, `TestFromSequenceIntBool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 983`** (2 nodes): `Make sure non supported operations on Timedelta returns NonImplemented         a`, `TestTimedeltaComparison`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 986`** (1 nodes): `TestGetIndexerNonUnique`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 988`** (1 nodes): `Indexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 989`** (1 nodes): `ToNumpy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 990`** (2 nodes): `Categories`, `MultipleCategories`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 991`** (1 nodes): `Transform`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 992`** (1 nodes): `ToDatetimeISO8601`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 995`** (1 nodes): `TestAppend`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 996`** (1 nodes): `TestGetIndexer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 997`** (1 nodes): `TestValueCounts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 998`** (1 nodes): `TestGenRangeGeneration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 999`** (1 nodes): `TestGetIndexer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1002`** (1 nodes): `TestIsScalar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1003`** (1 nodes): `TestLibMissing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1004`** (2 nodes): `Various Series and DataFrame logical ops methods.`, `TestLogicalOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1006`** (1 nodes): `TestPeriodArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1010`** (1 nodes): `TestTimedelta64Formatter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1011`** (2 nodes): `test_adjoin()`, `TestFormatBase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1013`** (2 nodes): `TestToStringNumericFormatting`, `_three_digit_exp()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1014`** (2 nodes): `DummyElement`, `test_frame_with_zero_len_series_corner_cases()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1015`** (1 nodes): `TestFrameComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1016`** (1 nodes): `TestDataFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1017`** (1 nodes): `TestSeries`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1018`** (1 nodes): `TestNumericOnly`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1020`** (2 nodes): `# TODO: De-duplicate/parametrize`, `TestAtWithDuplicates`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1021`** (1 nodes): `TestGetitem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1022`** (1 nodes): `TestLocListlike`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1023`** (1 nodes): `TestXS`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1025`** (1 nodes): `TestGetDtypesCache`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1026`** (1 nodes): `TestIntervalArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1027`** (1 nodes): `TestTableSchemaType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1028`** (1 nodes): `assert_json_roundtrip_equal()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1029`** (1 nodes): `TestPyObjectHashTableWithNans`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1030`** (1 nodes): `# TODO: so, so many other variants of this...`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1032`** (1 nodes): `TestPeriodIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1033`** (1 nodes): `TestFrameAsof`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1034`** (1 nodes): `TestPeriodIndexAsType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1035`** (1 nodes): `TestSeriesDiff`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1036`** (1 nodes): `TestDataFrameFilter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1037`** (1 nodes): `TestRepeat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1038`** (1 nodes): `TestSeriesSearchSorted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1039`** (1 nodes): `TestDataFrameSortIndexKey`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1040`** (1 nodes): `# TODO: better name, de-duplicate with test_sort_index_level above`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1046`** (1 nodes): `TestMultiIndexSorted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1047`** (1 nodes): `TestAstype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1048`** (1 nodes): `TestGetLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1049`** (2 nodes): `TestJoinInt64Index`, `TestJoinUInt64Index`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1050`** (1 nodes): `TestCustomBusinessDay`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1051`** (2 nodes): `get_utc_offset_hours()`, `TestDST`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1053`** (1 nodes): `TestPeriodIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1054`** (1 nodes): `TestIteration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1055`** (1 nodes): `Get the location of the first fill value.          Returns         -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1056`** (1 nodes): `TestGetitem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1057`** (1 nodes): `TestSorting`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1058`** (1 nodes): `TestTimestampRendering`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1059`** (1 nodes): `TestToDatetimeInferFormat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1062`** (1 nodes): `TestEngine`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1063`** (1 nodes): `TestTableMethod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1064`** (1 nodes): `TestLambdaMangling`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1065`** (1 nodes): `TestDatetime64SeriesComparison`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1066`** (1 nodes): `TestNumericArraylikeArithmeticWithDatetimeLike`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1072`** (1 nodes): `TestIndexConstructor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1075`** (1 nodes): `TimeLogicalOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1076`** (2 nodes): `ToDatetimeFormat`, `ToDatetimeNONISO8601`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1077`** (1 nodes): `ToDatetimeFromIntsFloats`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1079`** (1 nodes): `TestCategoricalIndexingWithFactor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1080`** (1 nodes): `TestReindex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1081`** (1 nodes): `TestIndexConcat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1082`** (1 nodes): `TestConcatSort`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1086`** (1 nodes): `TestTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1089`** (1 nodes): `TestNumpyEADtype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1091`** (1 nodes): `TestNumberScalar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1094`** (1 nodes): `TestDatetime64Formatter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1095`** (1 nodes): `TestAllowNonNano`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1096`** (1 nodes): `TestCompat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1097`** (1 nodes): `TestGetGroup`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1098`** (2 nodes): `# TODO: overlap with tests.series.test_ufunc.test_reductions`, `# TODO: do we have cases both with and without NAs?`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1099`** (1 nodes): `TestAtSetItemWithExpansion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1100`** (1 nodes): `TestGetitemListLike`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1101`** (1 nodes): `TestDataFrameInsert`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1103`** (1 nodes): `TestSetitemDT64Values`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1108`** (1 nodes): `TestHashTableUnsorted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1110`** (1 nodes): `TestSeriesArgsort`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1111`** (1 nodes): `TestSeriesAsof`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1112`** (1 nodes): `TestDropna`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1113`** (1 nodes): `TestDataFrameDataTypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1115`** (1 nodes): `TestTimedeltaIndexInsert`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1116`** (1 nodes): `TestSeriesSortValues`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1117`** (1 nodes): `TestTimestampToJulianDate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1118`** (1 nodes): `TestTimestampToPyDatetime`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1119`** (1 nodes): `TestDataFrameTruncate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1120`** (1 nodes): `TestUnique`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1121`** (1 nodes): `TestContains`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1122`** (1 nodes): `TestMixedResolutionDatetime64`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1125`** (1 nodes): `TestTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1126`** (1 nodes): `TestSeriesFlexComparison`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1129`** (1 nodes): `TestReprBase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1130`** (1 nodes): `TestTimestampConstructorFoldKeyword`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1134`** (1 nodes): `TestExpanding`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1136`** (1 nodes): `TestPeriodIndexComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1140`** (1 nodes): `TestIndexRendering`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1141`** (2 nodes): `BasePrintingTests`, `Tests checking the formatting of your EA when printed.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1144`** (1 nodes): `Concat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1145`** (1 nodes): `Rank`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1146`** (1 nodes): `Apply`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1147`** (1 nodes): `Equals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1148`** (1 nodes): `Nth`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1149`** (2 nodes): `Concat`, `ConcatIndexDtype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1150`** (1 nodes): `MergeAsof`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1151`** (1 nodes): `Merge`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1153`** (1 nodes): `TestPeriodConcat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1154`** (2 nodes): `pandas._config is considered explicitly upstream of everything else in pandas, s`, `pandas_config_display`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1156`** (1 nodes): `TestDatetimeArrayConstructor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1157`** (1 nodes): `TestWhere`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1158`** (1 nodes): `TestDatetimeIndexIteration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1160`** (1 nodes): `TestNAObj`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1162`** (1 nodes): `get_exp_unit()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1164`** (1 nodes): `TestFloatArrayFormatter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1165`** (1 nodes): `TestHTMLIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1166`** (1 nodes): `TestToLatexHeader`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1167`** (1 nodes): `TestDataFrameCumulativeOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1168`** (1 nodes): `_check_colors_box()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1170`** (1 nodes): `TestContains`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1171`** (1 nodes): `TestILocSeries`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1174`** (1 nodes): `TestMethods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1175`** (1 nodes): `ToJSONLines`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1176`** (1 nodes): `TestCompression`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1181`** (1 nodes): `TestInfinity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1183`** (1 nodes): `TestCombine`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1184`** (1 nodes): `TestDatetimeIndexFactorize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1186`** (1 nodes): `TestPeriodIndexShift`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1187`** (1 nodes): `TestTimedeltaIndexShift`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1188`** (1 nodes): `TestSeriesSortingKey`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1189`** (1 nodes): `TestDateTimeIndexToJulianDate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1191`** (1 nodes): `TestSliceLocs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1195`** (1 nodes): `TestCartesianProduct`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1199`** (1 nodes): `TestUnsupportedFeatures`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1200`** (1 nodes): `TestPeriodComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1201`** (1 nodes): `TestGetIndexer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1202`** (1 nodes): `TestGetLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1203`** (1 nodes): `TestPeriodRangeKeywords`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1204`** (1 nodes): `TestRegistration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1206`** (1 nodes): `TestSAS7BDAT`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1208`** (1 nodes): `TestSeriesFlexArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1211`** (1 nodes): `TestDuplicated`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1212`** (1 nodes): `TestRank`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1213`** (1 nodes): `TestIsMonotonic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1214`** (1 nodes): `TestRandomState`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1215`** (1 nodes): `TestExtensionTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1216`** (1 nodes): `TestVectorizedTimedelta`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1217`** (1 nodes): `TestTimestampConstructorPositionalAndKeywordSupport`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1218`** (1 nodes): `TestDatetimeParsingWrappers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1219`** (2 nodes): `Tests for ArrowExtensionArray._hash_pandas_object (GH#48964).`, `TestHashArrow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1223`** (1 nodes): `TestEWM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1225`** (1 nodes): `TestDatetime64ArrayLikeComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1226`** (1 nodes): `TestPeriodArrayLikeComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1227`** (1 nodes): `TestTimedelta64ArrayLikeComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1230`** (1 nodes): `TestEmpty`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1232`** (1 nodes): `Ops`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1233`** (1 nodes): `Timeseries`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1234`** (1 nodes): `CategoricalSlicing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1235`** (1 nodes): `Reindex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1236`** (1 nodes): `Rename`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1237`** (2 nodes): `AggEngine`, `TransformEngine`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1238`** (1 nodes): `Apply`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1240`** (1 nodes): `InsertColumns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1241`** (1 nodes): `ToDatetimeCache`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1242`** (1 nodes): `Join`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1243`** (2 nodes): `MergeRangeLikeFastPath`, `Benchmarks for merge(sort=False) where one side is unsorted and the other     si`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1244`** (1 nodes): `TestCategoricalIndex2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1245`** (1 nodes): `TestCategoricalIndexConstructors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1246`** (1 nodes): `TestEquals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1247`** (1 nodes): `TestContains`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1248`** (1 nodes): `TestGetLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1254`** (1 nodes): `TestDatetimeIndexArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1255`** (1 nodes): `TestGetItem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1256`** (1 nodes): `TestPickle`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1257`** (2 nodes): `DecimalDtype`, `Return the array type associated with this dtype.          Returns         -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1259`** (1 nodes): `TestTableSchemaRepr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1260`** (1 nodes): `TestDataFrameToStringLineWidth`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1261`** (1 nodes): `TestEmptyDataFrameReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1263`** (2 nodes): `MySubclassWithMetadata`, `test_constructor_with_metadata()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1264`** (2 nodes): `TestDataFrameToXArray`, `TestSeriesToXArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1265`** (1 nodes): `Tests of the groupby API, including internal consistency and with other pandas o`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1266`** (1 nodes): `TestGroupVar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1267`** (1 nodes): `TestEngine`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1268`** (1 nodes): `TestIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1269`** (1 nodes): `TestSeriesGetitemListLike`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1270`** (1 nodes): `TestSetitemValidation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1271`** (1 nodes): `TestLocWithEllipsis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1272`** (1 nodes): `TestPartialStringSlicing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1274`** (1 nodes): `TestSetitemSlices`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1275`** (1 nodes): `TestSetitemTZAwareValues`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1278`** (1 nodes): `TestContains`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1279`** (1 nodes): `TestInterval`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1282`** (1 nodes): `Pickle`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1285`** (1 nodes): `TestAssign`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1286`** (1 nodes): `TestBetween`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1287`** (1 nodes): `TestCopy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1288`** (1 nodes): `TestEquals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1289`** (1 nodes): `TestFirstValidIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1290`** (1 nodes): `TestInferObjects`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1291`** (1 nodes): `TestMap`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1292`** (1 nodes): `TestDataFramePctChange`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1293`** (1 nodes): `TestReindexSetIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1294`** (1 nodes): `TestDataFrameRenameAxis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1295`** (1 nodes): `TestDataFrameReplaceRegex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1296`** (1 nodes): `TestToFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1297`** (1 nodes): `TestToNumpy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1298`** (1 nodes): `TestUpdate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1299`** (1 nodes): `TestSliceLocs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1300`** (2 nodes): `TestBMonthBegin`, `TestBMonthEnd`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1302`** (1 nodes): `TestPeriodIndexDisallowedFreqs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1303`** (1 nodes): `TestJoin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1304`** (1 nodes): `TestPeriodRangeDisallowedFreqs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1305`** (2 nodes): `A group of tests which covers reading HDF5 files written by plain PyTables     (`, `TestReadPyTablesHDF5`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1307`** (1 nodes): `TestIsna`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1308`** (1 nodes): `TestMinMax`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1311`** (1 nodes): `TestIsBoolIndexer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1312`** (1 nodes): `TestFlags`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1313`** (1 nodes): `TestMerge`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1317`** (1 nodes): `TestAstypeOverflowSafe`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1319`** (1 nodes): `TestArrayStrptimeResolutionInference`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1320`** (1 nodes): `TimedeltaProperties`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1321`** (2 nodes): `PrescribedWindowIndexer`, `TestMinMax`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1322`** (2 nodes): `pandas_core_internals_api`, `pandas_core_internals_concat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1324`** (1 nodes): `TestDatetime64OverflowHandling`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1325`** (1 nodes): `TestNumericComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1326`** (1 nodes): `TestUFuncCompat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1327`** (2 nodes): `MyIndex`, `test_index_ops_defer_to_unknown_subclasses()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1328`** (1 nodes): `TestObjectComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1329`** (1 nodes): `Formatting function for scalar values.          This is used in the default '__r`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1330`** (1 nodes): `TestUnaryOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1331`** (2 nodes): `BaseAccumulateTests`, `Accumulation specific tests. Generally these only     make sense for numeric/boo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1332`** (1 nodes): `TestWhere`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1333`** (2 nodes): `constructor()`, `TestConstruction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1334`** (1 nodes): `DateInferOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1335`** (1 nodes): `AsType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1336`** (1 nodes): `IsMonotonic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1337`** (1 nodes): `Isnull`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1338`** (1 nodes): `NSort`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1339`** (1 nodes): `Repr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1340`** (1 nodes): `Round`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1341`** (1 nodes): `Fillna`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1342`** (1 nodes): `MergeCategoricals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1343`** (2 nodes): `data()`, `Fixture returning boolean array, with valid and missing values.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1344`** (1 nodes): `TestFillNA`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1345`** (1 nodes): `TestCategoricalSort`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1347`** (1 nodes): `TestInvalidConcat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1349`** (2 nodes): `Return number of unique elements in the object.          Excludes NA values by d`, `Return True if values in the object are unique.          This property checks wh`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1350`** (1 nodes): `TestGetSliceBounds`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1351`** (1 nodes): `TestBusinessDatetimeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1353`** (1 nodes): `Base`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1355`** (1 nodes): `TestABCClasses`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1356`** (1 nodes): `TestToLatexFormatters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1357`** (1 nodes): `TestToLatexLongtable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1358`** (1 nodes): `TestDataFrameToStringColSpace`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1359`** (1 nodes): `TestDataFrameToStringHeader`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1360`** (2 nodes): `take a list of frames, zip them together under the     assumption that these all`, `zip_frames()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1361`** (1 nodes): `_generate_4_axes_via_gridspec()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1362`** (1 nodes): `TestDataFramePlotsGroupby`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1363`** (1 nodes): `TestAsArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1364`** (1 nodes): `TestDataFrameEvalWithFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1365`** (1 nodes): `TestDataFrameQueryWithMultiIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1369`** (2 nodes): `return a list of tuples of start, stop, step`, `Return a list of tuples of the (attr, formatted_value)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1370`** (2 nodes): `The minimum value of the RangeIndex`, `The maximum value of the RangeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1371`** (1 nodes): `TestIndexUtils`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1372`** (2 nodes): `TestNumericEngine`, `TestObjectEngine`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1373`** (1 nodes): `TestGetIndexer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1374`** (1 nodes): `TestGetLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1375`** (1 nodes): `TestTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1376`** (1 nodes): `TestAtSetItem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1377`** (1 nodes): `TestDataFrameDelItem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1378`** (1 nodes): `TestSeriesDelItem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1379`** (1 nodes): `TestILocSetItemDuplicateColumns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1380`** (1 nodes): `TestDataframeNoneCoercion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1381`** (1 nodes): `TestDatetimelikeCoercion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1382`** (1 nodes): `TestDeprecatedIndexers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1383`** (1 nodes): `TestLocCallable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1384`** (1 nodes): `TestDataFrameSetItemSlicing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1386`** (1 nodes): `TestIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1387`** (1 nodes): `TestIntervalIndexRendering`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1388`** (1 nodes): `ToCSVFloatFormatVariants`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1389`** (1 nodes): `ToCSVIndexes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1390`** (1 nodes): `ToJSONMem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1391`** (1 nodes): `SAS`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1392`** (2 nodes): `Stata`, `StataMissing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1394`** (1 nodes): `We treat dictionaries as a mapping in fillna, not a scalar.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1395`** (1 nodes): `TestSetitemValidation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1397`** (1 nodes): `TestAsUnit`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1398`** (1 nodes): `TestTimestampAsUnit`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1399`** (1 nodes): `TestDataFrameCov`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1400`** (1 nodes): `TestSeriesCorr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1401`** (1 nodes): `TestGetNumericData`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1402`** (1 nodes): `TestNormalize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1403`** (1 nodes): `TestSeriesPctChange`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1404`** (1 nodes): `TestSetIndexCustomLabelType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1405`** (1 nodes): `TestSetIndexInvalid`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1406`** (1 nodes): `TestSortValuesLevelAsStr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1407`** (1 nodes): `TestTruncate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1408`** (1 nodes): `TestPutmask`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1409`** (2 nodes): `TestIsLexsorted`, `TestLexsortDepth`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1411`** (1 nodes): `TestSearchsorted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1412`** (1 nodes): `TestGetIndexer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1413`** (2 nodes): `Assertion helpers and base class for offsets tests`, `WeekDay`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1414`** (1 nodes): `TestCommonCBM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1415`** (1 nodes): `TestWhere`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1416`** (1 nodes): `TestPeriodRange`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1417`** (1 nodes): `TestPeriodDisallowedFreqs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1418`** (1 nodes): `TestPeriodIndexOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1420`** (1 nodes): `TestCategoricalSeriesReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1421`** (1 nodes): `TestDatetime64SeriesReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1424`** (1 nodes): `TestTimeSeriesArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1425`** (1 nodes): `TestSeriesMissingData`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1426`** (1 nodes): `TestSeriesUnaryOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1429`** (2 nodes): `SubclassedDataFrame`, `SubclassedSeries`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1430`** (1 nodes): `TestEnsureNumeric`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1431`** (1 nodes): `TestTimedeltaArrayConstructor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1432`** (1 nodes): `TestTimedeltaIndexRendering`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1433`** (1 nodes): `TestFreq`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1434`** (1 nodes): `TestGetLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1435`** (1 nodes): `TestMaybeCastSliceBound`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1436`** (1 nodes): `TestTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1437`** (1 nodes): `TestJoin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1438`** (1 nodes): `TestTimestampConstructorUnitKeyword`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1439`** (1 nodes): `TestTimestampConversion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1440`** (1 nodes): `TestEWM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1441`** (1 nodes): `TestEWM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1442`** (1 nodes): `TestObjectDtypeEquivalence`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1443`** (1 nodes): `TestTimedelta64ArrayComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1444`** (2 nodes): `Return a Series containing counts of each category.          Every category will`, `Describes this Categorical          Returns         -------         description:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1448`** (1 nodes): `TestTimedeltaArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1449`** (1 nodes): `TestGetLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1450`** (1 nodes): `TestGetSliceBounds`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1451`** (1 nodes): `Finalize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1452`** (1 nodes): `Duplicated`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1453`** (1 nodes): `Fillna`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1454`** (1 nodes): `Update`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1455`** (1 nodes): `MethodLookup`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1456`** (2 nodes): `MaybeConvertNumeric`, `ToTimedeltaErrors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1457`** (1 nodes): `ToNumeric`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1458`** (1 nodes): `ToTimedelta`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1459`** (1 nodes): `Values`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1460`** (1 nodes): `StringArrayConstruction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1461`** (1 nodes): `TestPrivateCategoricalAPI`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1462`** (1 nodes): `TestTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1466`** (2 nodes): `Ensure that key is valid for current indexer.          Parameters         ------`, `Check that 'key' is a valid position in the desired axis.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1468`** (1 nodes): `TestSequenceToDT64NS`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1469`** (1 nodes): `TestFreq`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1470`** (2 nodes): `Return the array type associated with this dtype.          Returns         -----`, `Construct an ExtensionArray of this dtype with the given shape.          Analogo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1471`** (1 nodes): `TestExcelWriterEngineTests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1473`** (2 nodes): `has_info_repr()`, `has_non_verbose_info_repr()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1474`** (1 nodes): `TestFormatPercentiles`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1475`** (1 nodes): `TestGenericArrayFormatter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1476`** (1 nodes): `TestDataFrameConstructorIndexInference`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1478`** (2 nodes): `Determines if two MultiIndex objects have the same labeling information`, `Return True if the levels of both MultiIndex objects are the same`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1479`** (2 nodes): `Parameters         ----------         other : Any         op : callable that acc`, `The value of the `step` parameter (``1`` if this was not supplied).          The`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1480`** (2 nodes): `Check if other range is contained in self`, `Form the union of two Index objects and sorts if possible          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1481`** (1 nodes): `TestConversion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1483`** (1 nodes): `TestIndexConstructorUnwrapping`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1484`** (1 nodes): `TestGetitemSlice`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1486`** (1 nodes): `TestILocErrors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1487`** (1 nodes): `TestLocBooleanLabelsAndSlices`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1488`** (1 nodes): `TestMultiIndexScalar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1489`** (1 nodes): `TestSetValue`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1490`** (1 nodes): `TestSetitemScalarIndexer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1491`** (1 nodes): `TestIntervalComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1492`** (1 nodes): `TestIntervalConstructors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1493`** (1 nodes): `TestSliceLocs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1494`** (1 nodes): `TestIntervalIndexInsideMultiIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1495`** (1 nodes): `ToCSVMultiIndexUnusedLevels`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1496`** (1 nodes): `ToCSVPeriodIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1497`** (1 nodes): `ToCSVPeriod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1498`** (1 nodes): `DoesStringLookLikeDatetime`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1499`** (1 nodes): `Base`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1502`** (1 nodes): `TestMisc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1503`** (1 nodes): `TestPadBackfill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1504`** (1 nodes): `TestAsOf`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1505`** (1 nodes): `TestAstypeAPI`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1506`** (1 nodes): `TestDelete`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1507`** (1 nodes): `TestTimedeltaIndexFactorize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1508`** (1 nodes): `TestDataFrameSetItem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1509`** (1 nodes): `TestTimestampNormalize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1510`** (1 nodes): `TestPipe`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1511`** (1 nodes): `TestDataFramePop`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1512`** (1 nodes): `TestDataFrameReindexLike`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1513`** (1 nodes): `TestSeriesRenameAxis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1514`** (1 nodes): `TestTimestampTZConvert`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1515`** (1 nodes): `TestPrivateValues`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1517`** (1 nodes): `TestKeyErrorsWithMultiIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1518`** (1 nodes): `TestContains`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1519`** (1 nodes): `TestTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1520`** (1 nodes): `TestWhere`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1521`** (1 nodes): `TestEaster`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1524`** (2 nodes): `is_index_col()`, `Extract and return the names, index_names, col_names if the column         names`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1526`** (1 nodes): `TestShallowCopy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1527`** (1 nodes): `TestSimpleNew`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1528`** (1 nodes): `TestPeriodIndexRendering`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1529`** (1 nodes): `TestContains`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1530`** (1 nodes): `TestTake`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1531`** (1 nodes): `TestReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1532`** (1 nodes): `TestSearchsorted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1533`** (1 nodes): `TestCommon`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1534`** (2 nodes): `Test timedelta converter`, `TestTimeDeltaConverter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1535`** (1 nodes): `TestSeriesPlots`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1537`** (1 nodes): `TestDatetimeLikeStatReductions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1539`** (1 nodes): `TestNamePreservation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1540`** (1 nodes): `TestSeriesConstructorIndexCoercion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1541`** (1 nodes): `TestSeriesConstructorInternals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1542`** (1 nodes): `TestSparseIndexIntersect`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1543`** (1 nodes): `TestUnaryMethods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1546`** (1 nodes): `TestDiff`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1547`** (1 nodes): `TestTimedeltaIndexDelete`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1548`** (1 nodes): `TestGetItem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1549`** (1 nodes): `TestWhere`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1550`** (1 nodes): `TestTimedeltaRangeUnitInference`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1551`** (1 nodes): `TestTimedeltaIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1552`** (1 nodes): `TestTimestampResolutionInference`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1553`** (2 nodes): `Tests for Timestamp timezone-related methods`, `TestTimestampTZOperations`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1554`** (1 nodes): `TestToTime`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1555`** (1 nodes): `Normalize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1556`** (1 nodes): `TimeTZConvert`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1557`** (1 nodes): `TestSparseAccessor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1558`** (1 nodes): `TestStrAccessor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1559`** (1 nodes): `TestCategoricalComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1560`** (1 nodes): `transforms.py is for shape-preserving functions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1562`** (2 nodes): `pyarrow_array_to_numpy_and_mask()`, `Convert a primitive pyarrow.Array to a numpy array and boolean mask based     on`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1563`** (2 nodes): `allow_na_ops()`, `Whether to skip test cases including NaN`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1564`** (1 nodes): `FrameWithFrameWide`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1565`** (1 nodes): `MixedFrameWithSeriesAxis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1566`** (1 nodes): `OffsetArrayArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1567`** (1 nodes): `OpWithFillValue`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1568`** (1 nodes): `Interpolate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1569`** (1 nodes): `MaskBool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1570`** (1 nodes): `MemoryUsage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1571`** (1 nodes): `SortMultiKey`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1572`** (1 nodes): `ToDict`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1573`** (1 nodes): `ToRecords`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1574`** (1 nodes): `Resample`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1575`** (1 nodes): `Sample`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1576`** (1 nodes): `Shift`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1577`** (1 nodes): `Size`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1578`** (1 nodes): `SumTimeDelta`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1579`** (1 nodes): `GetItemSingleColumn`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1580`** (1 nodes): `IndexSingleRow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1581`** (1 nodes): `NumericMaskedIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1582`** (1 nodes): `SeriesSetitem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1583`** (1 nodes): `Setitem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1584`** (1 nodes): `SortedAndUnsortedDatetimeIndexLoc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1585`** (1 nodes): `ConcatDataFrames`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1586`** (1 nodes): `JoinEmpty`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1587`** (1 nodes): `TestUnaryOps`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1589`** (2 nodes): `_get_pretty_string()`, `Return a prettier version of obj.      Parameters     ----------     obj : objec`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1590`** (2 nodes): `get_array()`, `Helper method to get array for a DataFrame column or a Series.      Equivalent o`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1592`** (1 nodes): `TestAccumulator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1593`** (1 nodes): `TestContains`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1594`** (1 nodes): `TestIndexerBetweenTime`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1595`** (1 nodes): `TestMaybeCastSliceBound`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1596`** (1 nodes): `TestDatetimeIndexReindex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1598`** (1 nodes): `TestDataFrameAlterAxes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1601`** (1 nodes): `TestDataFrame2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1605`** (1 nodes): `TestCaching`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1606`** (1 nodes): `TestGetValue`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1607`** (1 nodes): `TestILocCallable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1608`** (1 nodes): `_safe_add()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1609`** (1 nodes): `Pointer to start of the buffer as an integer.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1610`** (2 nodes): `Return an iterator yielding the chunks.          See `DataFrame.get_chunks` for`, `Return an iterator yielding the chunks.          By default (None), yields the c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1611`** (2 nodes): `The metadata for the column. See `DataFrame.metadata` for more details.`, `The metadata for the data frame, as a dictionary with string keys. The         c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1612`** (2 nodes): `Return the number of chunks the column consists of.`, `Return the number of chunks the DataFrame consists of.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1614`** (1 nodes): `ToCSVDatetimeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1619`** (2 nodes): `JSONDtype`, `Return the array type associated with this dtype.          Returns         -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1620`** (2 nodes): `orient()`, `Fixture for orients excluding the table format.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1621`** (1 nodes): `This fails when we get to tm.assert_series_equal when left.index         contain`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1622`** (2 nodes): `is_monotonic_increasing()`, `Check if int64 values are monotonically increasing.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1623`** (1 nodes): `get_test_data()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1624`** (1 nodes): `_join_by_hand()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1625`** (2 nodes): `rand_str()`, `Generate one random byte string.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1626`** (1 nodes): `TestDataFrameCount`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1627`** (1 nodes): `TestSeriesCount`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1628`** (1 nodes): `TestSeriesCov`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1629`** (1 nodes): `TestFactorize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1630`** (1 nodes): `TestIsMonotonic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1631`** (1 nodes): `TestIsna`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1632`** (1 nodes): `TestMatmul`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1633`** (1 nodes): `TestReorderLevels`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1634`** (1 nodes): `TestSetName`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1635`** (1 nodes): `TestSeriesToDict`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1637`** (1 nodes): `TestValues`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1638`** (1 nodes): `TestWhere`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1639`** (1 nodes): `TestGetSliceBounds`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1640`** (1 nodes): `TestSetOpsSort`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1641`** (1 nodes): `TestGetIndexerNonUnique`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1644`** (2 nodes): `pandas_core_window_ewm`, `pandas_core_window_expanding`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1645`** (2 nodes): `Validate the 'usecols' parameter.      Checks whether or not the 'usecols' param`, `_validate_usecols_arg()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1647`** (1 nodes): `TestPickle`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1648`** (2 nodes): `Wish to match NumPy units`, `TestPeriodRepresentation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1649`** (1 nodes): `_check_ax_limits()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1650`** (1 nodes): `TestHDFStoreSubclass`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1651`** (1 nodes): `TestSas`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1652`** (2 nodes): `Tests for error handling related to data types of method arguments.`, `test_validate_bool_args()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1653`** (1 nodes): `Create a SparseArray from a scipy.sparse matrix.          Parameters         ---`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1654`** (1 nodes): `TestSparseArrayConcat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1655`** (1 nodes): `TestSparseIndexUnion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1656`** (1 nodes): `TestArgmaxArgmin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1657`** (1 nodes): `TestHashTable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1658`** (2 nodes): `everything you wanted to test about sorting`, `TestSorted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1659`** (1 nodes): `TestTimedeltaIndexArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1660`** (1 nodes): `TestAccumulator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1661`** (1 nodes): `TestContains`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1662`** (1 nodes): `TestGetIndexer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1663`** (1 nodes): `TestSearchSorted`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1664`** (1 nodes): `TestTimedeltaIndexDifference`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1665`** (1 nodes): `Tests that the tslibs API is locked down`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1668`** (1 nodes): `algos/ directory is intended for individual functions from core.algorithms  In m`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1669`** (2 nodes): `int_frame_const_col()`, `Fixture for DataFrame of ints which are constant per column      Columns are ['A`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1670`** (1 nodes): `core.array_algos is for algorithms that operate on ndarray and ExtensionArray. T`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1671`** (1 nodes): `pandas_tests_extension_array_with_attr_array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1672`** (1 nodes): `The categories of this categorical.          Setting assigns new values to each`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1673`** (1 nodes): `Concatenate multiple arrays of this dtype.          Parameters         ---------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1674`** (1 nodes): `Analogous to np.empty(shape, dtype=dtype)          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1675`** (1 nodes): `Return a Series containing counts of unique values.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1676`** (2 nodes): `Decorator to ravel a 2D array before passing it to a cython operation,     then`, `ravel_compat()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1677`** (1 nodes): `Fixture returning parametrized time units`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1678`** (1 nodes): `BaseExtensionTests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1679`** (1 nodes): `Tests for CategoricalIndex.__repr__ and related methods.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1680`** (1 nodes): `pandas_core_computation_eval`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1681`** (1 nodes): `Find indices where elements should be inserted to maintain order.          Find`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1682`** (1 nodes): `Return a tuple of the shape of the underlying data.          For a Series this i`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1683`** (1 nodes): `Return the number of elements in the underlying data.          For a Series or I`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1684`** (1 nodes): `A NumPy ndarray representing the values in this Series or Index.          This m`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1685`** (1 nodes): `Return a list of the values.          These are each a scalar type, which is a P`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1686`** (1 nodes): `Return the transpose, which is by definition self.          Returns         ----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1687`** (1 nodes): `Return a Series containing counts of unique values.          The resulting objec`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1688`** (2 nodes): `all_none()`, `Returns a boolean indicating if all arguments are None.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1689`** (2 nodes): `all_not_none()`, `Returns a boolean indicating if all arguments are not None.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1690`** (2 nodes): `any_none()`, `Returns a boolean indicating if any argument is None.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1691`** (2 nodes): `any_not_none()`, `Returns a boolean indicating if any argument is not None.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1692`** (2 nodes): `apply_if_callable()`, `Evaluate possibly callable input using obj and kwargs if it is callable,     oth`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1693`** (2 nodes): `cast_scalar_indexer()`, `Disallow indexing with a float key, even if that key is a round number.      Par`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1694`** (2 nodes): `convert_to_list_like()`, `Convert list-like or scalar input to list-like. List, numpy and pandas array-lik`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1695`** (2 nodes): `count_not_none()`, `Returns the count of arguments that are not None.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1696`** (2 nodes): `fill_missing_names()`, `If a name is missing then replace it by level_n, where n is the count      Param`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1697`** (2 nodes): `flatten()`, `Flatten an arbitrarily nested sequence.      Parameters     ----------     line`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1698`** (2 nodes): `get_cython_func()`, `if we define an internal function for this argument, return it`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1699`** (2 nodes): `get_rename_function()`, `Returns a function that will map names/labels, dependent if mapper     is a dict`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1700`** (2 nodes): `is_bool_indexer()`, `Check whether `key` is a valid boolean indexer.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1701`** (2 nodes): `is_empty_slice()`, `We have an empty slice, e.g. no values are selected.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1702`** (2 nodes): `is_full_slice()`, `We have a full length slice.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1703`** (2 nodes): `is_local_in_caller_frame()`, `Helper function used in detecting chained assignment.      If the pandas object`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1704`** (2 nodes): `maybe_iterable_to_list()`, `If obj is Iterable but not list-like, consume into list.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1705`** (2 nodes): `not_none()`, `Returns a generator consisting of the arguments that are not None.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1706`** (2 nodes): `pipe()`, `Apply a function ``func`` to object ``obj`` either by passing obj as the     fir`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1707`** (2 nodes): `random_state()`, `Helper function for processing random_state arguments.      Parameters     -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1708`** (2 nodes): `Helper function to standardize a supplied mapping.      Parameters     ---------`, `standardize_mapping()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1709`** (2 nodes): `Temporarily set attribute on an object.      Parameters     ----------     obj :`, `temp_setattr()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1710`** (2 nodes): `Check the length of data matches the length of the index.`, `require_length_match()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1711`** (1 nodes): `pandas_tests_extension_date_array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1712`** (1 nodes): `Test different DatetimeIndex constructions with timezone         Follow-up of GH`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1713`** (2 nodes): `astype_is_view()`, `Checks if astype avoided copying the data.      Parameters     ----------     dt`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1714`** (1 nodes): `Whether this dtype should be considered boolean.          By default, ExtensionD`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1715`** (1 nodes): `Can arrays with this dtype be modified with __setitem__? If not, return`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1716`** (1 nodes): `Whether columns with this dtype should be considered numeric.          By defaul`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1717`** (1 nodes): `A character code (one of 'biufcmMOSUV'), default 'O'          This should match`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1718`** (1 nodes): `A string identifying the data type.          Will be used for display in, e.g. ``
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1719`** (1 nodes): `Ordered list of field names, or None if there are no fields.          This is fo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1720`** (1 nodes): `Do ExtensionArrays with this dtype support 2D arrays?          Historically Exte`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1721`** (2 nodes): `ensure_python_int()`, `Ensure that a value is a python int.      Parameters     ----------     value: i`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1722`** (2 nodes): `ensure_str()`, `Ensure that bytes and non-strings get converted into ``str`` objects.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1723`** (2 nodes): `is_1d_only_ea_dtype()`, `Analogue to is_extension_array_dtype but excluding DatetimeTZDtype.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1724`** (2 nodes): `is_categorical_dtype()`, `Check whether an array-like or dtype is of the Categorical dtype.      .. deprec`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1725`** (2 nodes): `is_datetime64tz_dtype()`, `Check whether an array-like or dtype is of a DatetimeTZDtype dtype.      .. depr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1726`** (2 nodes): `is_ea_or_datetimelike_dtype()`, `Check for ExtensionDtype, datetime64 dtype, or timedelta64 dtype.      Notes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1727`** (2 nodes): `is_interval_dtype()`, `Check whether an array-like or dtype is of the Interval dtype.      .. deprecate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1728`** (2 nodes): `is_numeric_v_string_like()`, `Check if we are comparing a string-like object to a numeric ndarray.     NumPy d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1729`** (2 nodes): `is_period_dtype()`, `Check whether an array-like or dtype is of the Period dtype.      .. deprecated:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1730`** (2 nodes): `is_scipy_sparse()`, `Check whether an array-like is a scipy.sparse.spmatrix instance.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1731`** (2 nodes): `is_sparse()`, `Check whether an array-like is a 1-D pandas sparse array.      .. deprecated:: 2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1732`** (2 nodes): `is_string_or_object_np_dtype()`, `Faster alternative to is_string_dtype, assumes we have an np.dtype object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1733`** (2 nodes): `needs_i8_conversion()`, `Check whether the dtype should be converted to int64.      Dtype "needs" such a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1734`** (2 nodes): `Return None if all args are hashable, else raise a TypeError.      Parameters`, `validate_all_hashable()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1735`** (2 nodes): `get_is_dtype_funcs()`, `Get all functions in pandas.core.dtypes.common that     begin with 'is_' and end`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1736`** (2 nodes): `convert list of string dtypes to EA dtype`, `to_ea_dtypes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1737`** (2 nodes): `convert list of string dtypes to numpy dtype`, `to_numpy_dtypes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1738`** (1 nodes): `For various parameters, we should get the same result whether we         limit t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1739`** (1 nodes): `Sheets can contain blank cells with no data. Some of our readers         were in`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1740`** (1 nodes): `Test2DCompat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1741`** (1 nodes): `If the test fails, it at least won't hang.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1742`** (1 nodes): `Check that display logic is correct.          GH #37359          See description`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1743`** (2 nodes): `biggie_df_fixture()`, `Fixture for a big mixed Dataframe and an empty Dataframe`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1744`** (1 nodes): `Multiindex dataframe for testing multirow LaTeX macros.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1745`** (1 nodes): `Multicolumn dataframe for testing multicolumn LaTeX macros.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1746`** (1 nodes): `Check that every plot type gets properly collected.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1748`** (2 nodes): `df_cat()`, `DataFrame with multiple categorical columns and a column of integers.     Shorte`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1749`** (1 nodes): `Returns a FrozenList with elements from other removed from self.          Parame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1750`** (1 nodes): `This method will not function because object is immutable.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1751`** (1 nodes): `Returns a FrozenList with other concatenated to the end of self.          Parame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1752`** (2 nodes): `maybe_droplevels()`, `Attempt to drop level or levels from the given index.      Parameters     ------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1753`** (2 nodes): `names_compat()`, `A decorator to allow either `name` or `names` keyword but not both.      This ma`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1754`** (1 nodes): `Returns the indices that would sort the index and its         underlying data.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1755`** (1 nodes): `An int array that for performance reasons is created only when needed.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1756`** (1 nodes): `Get integer location for requested label.          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1757`** (1 nodes): `return if the index has unique values`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1758`** (1 nodes): `Return an iterator of the values.          Returns         -------         itera`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1759`** (1 nodes): `return the length of the RangeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1760`** (1 nodes): `Memory usage of my values          Parameters         ----------         deep :`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1761`** (1 nodes): `Return the number of bytes in the underlying data.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1762`** (1 nodes): `Should an integer key be treated as positional?`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1763`** (1 nodes): `The value of the `start` parameter (``0`` if this was not supplied).          Th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1764`** (1 nodes): `The value of the `stop` parameter.          This property returns the `stop` val`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1765`** (1 nodes): `Test that is_monotonic_decreasing is correct on slices.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1766`** (2 nodes): `any_dtype_for_small_pos_integer_indexes()`, `Dtypes that can be given to an Index with small positive integers.      This mea`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1767`** (2 nodes): `Return a fixed frequency TimedeltaIndex with day as the default.      This funct`, `timedelta_range()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1768`** (1 nodes): `parse_datetime_string_with_reso return parameter if type not matched.         Pe`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1769`** (2 nodes): `_check_where_equivalences()`, `test_where_dt64_2d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1770`** (1 nodes): `Buffer size in bytes.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1771`** (1 nodes): `Device type and device ID for where the data in the buffer resides.         Uses`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1772`** (1 nodes): `Produce DLPack capsule (see array API standard).          Raises:              -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1773`** (1 nodes): `Pointer to start of the buffer as an integer.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1774`** (1 nodes): `If the dtype is categorical, there are two options:         - There are only val`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1775`** (1 nodes): `Return the missing value (or "null") representation the column dtype         use`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1776`** (1 nodes): `Dtype description as a tuple ``(kind, bit-width, format string, endianness)``.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1777`** (1 nodes): `Return a dictionary containing the underlying buffers.          The returned dic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1778`** (1 nodes): `Number of null elements, if known.          Note: Arrow uses -1 to indicate "unk`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1779`** (1 nodes): `Offset of first element.          May be > 0 if using chunks; for example for a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1780`** (1 nodes): `Size of the column, in elements.          Corresponds to DataFrame.num_rows() if`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1781`** (1 nodes): `Return an iterator yielding the column names.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1782`** (1 nodes): `Return the column whose name is the indicated name.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1783`** (1 nodes): `Return the column at the indicated position.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1784`** (1 nodes): `Return an iterator yielding the columns.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1785`** (1 nodes): `Return the number of columns in the DataFrame.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1786`** (1 nodes): `Return the number of rows in the DataFrame, if available.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1787`** (1 nodes): `Create a new DataFrame by selecting a subset of columns by name.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1788`** (1 nodes): `Create a new DataFrame by selecting a subset of columns by index.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1789`** (2 nodes): `check_ndim()`, `ndim inference and validation.      Validates that values.ndim and ndim are cons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1790`** (2 nodes): `extract_pandas_array()`, `Ensure that we don't allow NumpyExtensionArray / NumpyEADtype in internals.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1791`** (2 nodes): `dataclasses_to_dicts()`, `Converts a list of dataclass instances to a list of dictionaries.      Parameter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1792`** (2 nodes): `Check if we should use nested_data_to_arrays.`, `treat_as_nested()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1793`** (1 nodes): `Make sure that read_html ignores empty tables.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1794`** (1 nodes): `Don't fail with bs4 when there is a header and only one column         as descri`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1795`** (1 nodes): `Ensure parser adds <tr> within <thead> on malformed HTML.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1796`** (1 nodes): `Make sure that read_html reads tfoot, containing td or th.         Ignores empty`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1797`** (2 nodes): `create_and_load_types_postgresql()`, `postgresql_adbc_types()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1798`** (1 nodes): `The test does .astype(object).stack(). If we happen to have         any missing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1799`** (1 nodes): `This currently fails in NumPy on np.array(self, dtype=str) with          *** Val`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1800`** (1 nodes): `This currently fails in Series.name.setter, since the         name must be hasha`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1801`** (1 nodes): `This fails in Index._do_unique_check with          >   hash(val)         E   Typ`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1803`** (1 nodes): `Test files dedicated to individual (stand-alone) Series methods  Ideally these f`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1804`** (1 nodes): `Tests for non numerical index types  - object, period, timedelta         Note th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1805`** (2 nodes): `Due to new MultiIndex-ing behaviour in v0.14.0,     dicts with tuple keys passed`, `test_map_dict_with_tuple_keys()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1806`** (2 nodes): `Test Series.map with a dictionary subclass that defines __missing__,     i.e. se`, `test_map_dict_subclass_with_missing()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1807`** (1 nodes): `Test for #23305: to ensure category dtypes are maintained         after replace`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1808`** (1 nodes): `Test to ensure category dtypes are maintained         after replace with dict va`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1809`** (2 nodes): `seed_df()`, `test_series_groupby_value_counts()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1810`** (2 nodes): `maybe_cast_str_impl()`, `Converts numba UnicodeCharSeq (numpy string scalar) -> unicode type (string).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1811`** (2 nodes): `Convert an Index object to a native structure.      Note: Object dtype is not al`, `unbox_index()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1812`** (2 nodes): `any_signed_int_ea_dtype()`, `Parameterized fixture for any signed nullable integer dtype.      * 'Int8'     *`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1813`** (2 nodes): `any_signed_int_numpy_dtype()`, `Parameterized fixture for signed integer dtypes.      * int     * 'int8'     * '`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1814`** (2 nodes): `any_skipna_inferred_dtype()`, `Fixture for all inferred dtypes from _libs.lib.infer_dtype      The covered (inf`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1815`** (2 nodes): `any_string_dtype()`, `Parametrized fixture for string dtypes.     * 'object'     * 'string[python]' (N`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1816`** (2 nodes): `any_unsigned_int_numpy_dtype()`, `Parameterized fixture for unsigned integer dtypes.      * 'uint8'     * 'uint16'`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1817`** (2 nodes): `as_index()`, `Fixture for 'as_index' argument in groupby.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1818`** (2 nodes): `ascending()`, `Fixture for 'ascending' argument in sort_values/sort_index/rank.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1819`** (2 nodes): `axis()`, `Fixture for returning the axis numbers of a DataFrame.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1820`** (2 nodes): `box_with_array()`, `Fixture to test behavior for Index, Series, DataFrame, and pandas Array     clas`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1821`** (2 nodes): `bytes_dtype()`, `Parametrized fixture for bytes dtypes.      * bytes     * 'bytes'`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1822`** (2 nodes): `cache()`, `Fixture for 'cache' argument in to_datetime.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1823`** (2 nodes): `closed()`, `Fixture for trying all interval closed parameters.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1824`** (2 nodes): `compare_operators_no_eq_ne()`, `Fixture for dunder names for compare operations except == and !=      * >=     *`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1825`** (2 nodes): `comparison_op()`, `Fixture for operator module comparison functions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1826`** (2 nodes): `complex_dtype()`, `Parameterized fixture for complex dtypes.      * complex     * 'complex64'     *`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1827`** (2 nodes): `complex_or_float_dtype()`, `Parameterized fixture for complex and numpy float dtypes.      * complex     * '`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1828`** (2 nodes): `compression_only()`, `Fixture for trying common compression types in compression tests excluding     u`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1829`** (2 nodes): `compression()`, `Fixture for trying common compression types in compression tests.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1830`** (2 nodes): `configure_tests()`, `Configure settings for all tests and test modules.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1831`** (2 nodes): `_create_mi_with_dt64tz_level()`, `MultiIndex with a level that is a tzaware DatetimeIndex.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1832`** (2 nodes): `_create_multiindex()`, `MultiIndex used to test the general functionality of this object`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1833`** (2 nodes): `datapath()`, `Get the path to a data file.      Parameters     ----------     path : str`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1834`** (2 nodes): `datetime_series()`, `Fixture for Series of floats with DatetimeIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1835`** (2 nodes): `datetime64_dtype()`, `Parametrized fixture for datetime64 dtypes.      * 'datetime64[ns]'     * 'M8[ns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1836`** (2 nodes): `dict_subclass()`, `Fixture for a dictionary subclass.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1837`** (2 nodes): `dropna()`, `Boolean 'dropna' parameter.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1838`** (2 nodes): `ea_scalar_and_dtype()`, `Fixture that tests each scalar and datetime type.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1839`** (1 nodes): `fixed_now_ts()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1840`** (2 nodes): `float_ea_dtype()`, `Parameterized fixture for float dtypes.      * 'Float32'     * 'Float64'`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1841`** (2 nodes): `float_frame()`, `Fixture for DataFrame of floats with index of unique strings      Columns are ['`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1842`** (2 nodes): `frame_or_series()`, `Fixture to parametrize over DataFrame and Series.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1843`** (2 nodes): `inclusive_endpoints_fixture()`, `Fixture for trying all interval 'inclusive' parameters.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1844`** (2 nodes): `index_flat_sortable()`, `index_flat fixture, but excluding types that are not orderable.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1845`** (2 nodes): `index_flat()`, `index fixture, but excluding MultiIndex cases.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1846`** (2 nodes): `index_or_series_memory_obj()`, `Fixture for tests on indexes, series, series with a narrow dtype and     series`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1847`** (2 nodes): `index_or_series_obj_orderable()`, `index_or_series_obj fixture, but excluding types that are not orderable.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1848`** (2 nodes): `index_or_series_obj()`, `Fixture for tests on indexes, series and series with a narrow dtype     copy to`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1849`** (2 nodes): `index_or_series_or_array()`, `Fixture to parametrize over Index, Series, and ExtensionArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1850`** (2 nodes): `index_or_series()`, `Fixture to parametrize over Index and Series, made necessary by a mypy     bug,`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1851`** (2 nodes): `index_sortable()`, `index fixture, but excluding types that are not orderable.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1852`** (2 nodes): `index_with_missing_sortable()`, `index_with_missing fixture, but excluding types that are not orderable.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1853`** (2 nodes): `index_with_missing()`, `Fixture for indices with missing values.      Integer-dtype and empty cases are`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1854`** (2 nodes): `indexer_al()`, `Parametrize over at.__setitem__, loc.__setitem__`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1855`** (2 nodes): `indexer_ial()`, `Parametrize over iat.__setitem__, iloc.__setitem__`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1856`** (2 nodes): `indexer_li()`, `Parametrize over loc.__getitem__, iloc.__getitem__`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1857`** (2 nodes): `indexer_si()`, `Parametrize over __setitem__, iloc.__setitem__`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1858`** (2 nodes): `indexer_sli()`, `Parametrize over __setitem__, loc.__setitem__, iloc.__setitem__`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1859`** (2 nodes): `indexer_sl()`, `Parametrize over __setitem__, loc.__setitem__`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1860`** (2 nodes): `index()`, `Fixture for many "simple" kinds of indices.      These indices are unlikely to c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1861`** (2 nodes): `int_frame()`, `Fixture for DataFrame of ints with index of unique strings      Columns are ['A'`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1862`** (2 nodes): `ip()`, `Get an instance of IPython.InteractiveShell.      Will raise a skip if IPython i`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1863`** (2 nodes): `join_type()`, `Fixture for trying all types of join operations.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1864`** (2 nodes): `keep()`, `Valid values for the 'keep' parameter used in     .duplicated or .drop_duplicate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1865`** (2 nodes): `lexsorted_two_level_string_multiindex()`, `2-level MultiIndex, lexsorted, with string names.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1866`** (2 nodes): `mpl_cleanup()`, `Ensure Matplotlib is cleaned up around a test.      Before a test is run:      1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1867`** (2 nodes): `multiindex_dataframe_random_data()`, `DataFrame with 2 level MultiIndex with random data`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1868`** (2 nodes): `multiindex_year_month_day_dataframe_random_data()`, `DataFrame with 3 level MultiIndex (year, month, day) covering     first 100 busi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1869`** (2 nodes): `na_action()`, `Fixture for 'na_action' argument in map.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1870`** (2 nodes): `names()`, `A 3-tuple of names, the first two for operands, the last for a result.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1871`** (2 nodes): `nogil()`, `Fixture for nogil keyword argument for numba.jit.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1872`** (2 nodes): `non_dict_mapping_subclass()`, `Fixture for a non-mapping dictionary subclass.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1873`** (2 nodes): `np_nat_fixture()`, `Fixture for each NaT type in numpy.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1874`** (2 nodes): `nselect_method()`, `Fixture for trying all nselect methods.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1875`** (2 nodes): `nullable_string_dtype()`, `Parametrized fixture for string dtypes.      * 'string[python]'     * 'string[py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1876`** (2 nodes): `nulls_fixture()`, `Fixture for each null type in pandas.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1877`** (2 nodes): `object_dtype()`, `Parametrized fixture for object dtypes.      * object     * 'object'`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1878`** (2 nodes): `object_series()`, `Fixture for Series of dtype object with Index of unique strings`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1879`** (2 nodes): `observed()`, `Pass in the observed keyword to groupby for [True, False]     This indicates whe`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1880`** (2 nodes): `ordered()`, `Boolean 'ordered' parameter for Categorical.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1881`** (2 nodes): `other_closed()`, `Secondary closed fixture to allow parametrizing over all pairs of closed.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1882`** (2 nodes): `parallel()`, `Fixture for parallel keyword argument for numba.jit.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1883`** (2 nodes): `performance_warning()`, `Fixture to check if performance warnings are enabled. Either produces     ``Perf`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1884`** (2 nodes): `pyarrow_string_dtype()`, `Parametrized fixture for string dtypes backed by Pyarrow.      * 'str[pyarrow]'`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1885`** (2 nodes): `rand_series_with_duplicate_datetimeindex()`, `Fixture for Series with a DatetimeIndex that has duplicates.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1886`** (2 nodes): `rank_method()`, `Fixture for 'rank' argument in rank.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1887`** (2 nodes): `Returns the configuration for the test setting `--no-strict-data-files`.`, `strict_data_files()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1888`** (2 nodes): `Fixture for trying timezones including default (None): {0}`, `tz_naive_fixture()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1889`** (2 nodes): `Fixture for trying explicit timezones: {0}`, `tz_aware_fixture()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1890`** (2 nodes): `Fixture to provide variants of UTC timezone strings and tzinfo objects.`, `utc_fixture()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1891`** (2 nodes): `datetime64 units we support.`, `unit()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1892`** (2 nodes): `Parametrized fixture for string dtypes.      * str     * 'str'     * 'U'`, `string_dtype()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1893`** (2 nodes): `Parametrized fixture for string dtypes.     * 'string[python]' (NA variant)`, `string_dtype_no_object()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1894`** (2 nodes): `Parametrized fixture for StringDtype storage and na_value.      * 'python' + pd.`, `string_dtype_arguments()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1895`** (2 nodes): `Parametrized fixture for timedelta64 dtypes.      * 'timedelta64[ns]'     * 'm8[`, `timedelta64_dtype()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1896`** (2 nodes): `Fixture for Tick based datetime offsets available for a time series.`, `tick_classes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1897`** (2 nodes): `Simple fixture for testing keys in sorting methods.     Tests None (no key) and`, `sort_by_key()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1898`** (2 nodes): `Fixture to check if infer string option is enabled.`, `using_infer_string()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1899`** (2 nodes): `tzinfo for Europe/Warsaw using pytz, dateutil, or zoneinfo.`, `warsaw()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1900`** (2 nodes): `Generate a unique file for testing use. See link for removal policy.     https:/`, `temp_file()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1901`** (2 nodes): `Boolean 'sort' parameter.`, `sort()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1902`** (2 nodes): `Boolean 'skipna' parameter.`, `skipna()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1903`** (2 nodes): `Fixture that an array is writable.`, `writable()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1904`** (2 nodes): `Fixture for each null type in pandas, each null type exactly once.`, `unique_nulls_fixture()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1905`** (2 nodes): `Fixture for Series of floats with Index of unique strings`, `string_series()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1906`** (2 nodes): `iris()`, `The iris dataset as a DataFrame.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1907`** (1 nodes): `Tests for reductions where we want to test for matching behavior across Array, I`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1908`** (2 nodes): `*this is an internal non-public method*      Returns the levels, labels and name`, `restore_dropped_levels_multijoin()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1910`** (2 nodes): `Errors in RLE/RDC decompression should propagate.`, `test_rle_rdc_exceptions()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1911`** (1 nodes): `The percent of non- ``fill_value`` points, as decimal.          This is calculat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1912`** (1 nodes): `The number of non- ``fill_value`` points.          This property returns the num`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1913`** (1 nodes): `Returns a Series containing counts of unique values.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1914`** (2 nodes): `arr_data()`, `Fixture returning numpy array with valid and missing entries`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1915`** (2 nodes): `arr()`, `Fixture returning SparseArray from 'arr_data`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1916`** (2 nodes): `dtype()`, `Fixture giving StringDtype from parametrized storage and na_value arguments`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1917`** (2 nodes): `assert_metadata_equivalent()`, `Check that ._metadata attributes are equivalent.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1919`** (2 nodes): `Cast a numeric column to object-dtype strings so that to_datetime with a     ``f`, `stringify_numeric_column()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1920`** (2 nodes): `Convert argument to a numeric type.      If the input is already of a numeric dt`, `to_numeric()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1921`** (2 nodes): `assert_fp_equal()`, `test_transform_broadcast()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1922`** (2 nodes): `Tests that the output does not contain the `<index>` field when the index of the`, `test_index_false_with_offset_input_index()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1923`** (2 nodes): `read_xml_iterparse_comp()`, `test_compression_read()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `StringDtype` connect `Community 4` to `Community 5`, `Community 812`, `Community 1`, `Community 57`, `Community 1069`, `Community 1329`, `Community 147`, `Community 515`, `Community 17`, `Community 20`, `Community 484`, `Community 41`, `Community 33`, `Community 253`, `Community 16`, `Community 456`, `Community 6`, `Community 8`, `Community 1087`, `Community 1713`, `Community 67`, `Community 136`, `Community 1728`, `Community 1733`, `Community 1722`, `Community 1721`, `Community 1723`, `Community 1726`, `Community 1734`, `Community 1731`, `Community 1730`, `Community 1725`, `Community 1729`, `Community 1727`, `Community 1724`, `Community 1732`, `Community 46`, `Community 1740`, `Community 426`, `Community 555`, `Community 11`, `Community 27`, `Community 283`, `Community 22`, `Community 1789`, `Community 1790`, `Community 365`, `Community 1172`, `Community 1792`, `Community 1791`, `Community 47`, `Community 500`, `Community 1619`, `Community 1027`, `Community 3`, `Community 86`, `Community 1908`, `Community 1538`, `Community 64`, `Community 982`, `Community 35`, `Community 157`, `Community 268`, `Community 1917`, `Community 1920`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Why does `DataFrame` connect `Community 6` to `Community 8`, `Community 1`, `Community 857`, `Community 585`, `Community 4`, `Community 3`, `Community 286`, `Community 9`, `Community 120`, `Community 300`, `Community 106`, `Community 402`, `Community 30`, `Community 55`, `Community 555`, `Community 17`, `Community 38`, `Community 608`, `Community 77`, `Community 141`, `Community 52`, `Community 37`, `Community 34`, `Community 18`, `Community 292`, `Community 604`, `Community 35`?**
  _High betweenness centrality (0.026) - this node is a cross-community bridge._
- **Why does `ExtensionArray` connect `Community 5` to `Community 762`, `Community 1`, `Community 57`, `Community 1069`, `Community 1329`, `Community 4`, `Community 78`, `Community 3`, `Community 1228`, `Community 612`, `Community 110`, `Community 1229`, `Community 1444`, `Community 679`, `Community 1445`, `Community 1672`, `Community 41`, `Community 157`, `Community 613`, `Community 26`, `Community 33`, `Community 1673`, `Community 1675`, `Community 1674`, `Community 1676`, `Community 134`, `Community 20`, `Community 484`, `Community 16`, `Community 8`, `Community 37`, `Community 6`, `Community 34`, `Community 9`, `Community 18`, `Community 1919`, `Community 446`, `Community 156`?**
  _High betweenness centrality (0.015) - this node is a cross-community bridge._
- **Are the 1007 inferred relationships involving `StringDtype` (e.g. with `ExtensionArray` and `ExtensionArrayNaResult`) actually correct?**
  _`StringDtype` has 1007 INFERRED edges - model-reasoned connections that need verification._
- **Are the 658 inferred relationships involving `DataFrame` (e.g. with `OpsMixin` and `Methods that can be shared by many array-like classes or subclasses:     Series`) actually correct?**
  _`DataFrame` has 658 INFERRED edges - model-reasoned connections that need verification._
- **What connects `algos/ directory is intended for individual functions from core.algorithms  In m`, `A subset of the cartesian product of cases have special motivations:      "nans"`, `# TODO: GH#33198 the setting here shouldn't need two steps` to the rest of the system?**
  _1891 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.004135668204061465 - nodes in this community are weakly interconnected._