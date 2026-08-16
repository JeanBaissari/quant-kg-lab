# Graph Report - knowledge_graphs/polars/repo/py-polars/src/polars  (2026-08-13)

## Corpus Check
- 207 files · ~403,571 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 5296 nodes · 16925 edges · 485 communities detected
- Non-singleton communities: 453
- Extraction: EXTRACTED: 39.0% · INFERRED: 61.0%
- Edge kinds: calls: 1236 · contains: 852 · imports: 13 · imports_from: 179 · inherits: 151 · method: 1965 · rationale_for: 2208 · uses: 10321

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 207 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `1f779c9`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `CompatLevel` (532)
- `sphinx_accessor` (505)
- `ModuleUpgradeRequiredError` (458)
- `ShapeError` (436)
- `QueryOptFlags` (367)
- `ComputeError` (316)
- `Schema` (311)
- `Series` (289)
- `ExprStringNameSpace` (281)
- `ExprDateTimeNameSpace` (278)

## Surprising Connections (you probably didn't know these)
- `Configure polars; offers options for table formatting and more.      Notes     -` --uses--> `GPUEngine`  [INFERRED]
  config.py → lazyframe/engine_config.py
- `Parameters supported by the polars Config.` --uses--> `GPUEngine`  [INFERRED]
  config.py → lazyframe/engine_config.py
- `Order the top level keys and then recursively go to depth.      Parameters     -` --uses--> `Schema`  [INFERRED]
  convert/normalize.py → schema.py
- `Normalize semi-structured deserialized JSON data into a flat table.      Diction` --uses--> `Schema`  [INFERRED]
  convert/normalize.py → schema.py
- `Main recursive function.      Designed for the most basic use case of `pl.json_n` --uses--> `Schema`  [INFERRED]
  convert/normalize.py → schema.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.03
Nodes (53): Datetime, Data type representing a calendar date and time of day.      Parameters     ----, r"""         Count all successive non-overlapping regex matches.          Parame, Convert a String column into a Datetime column.          Parameters         ----, Split the string by a substring.          Parameters         ----------, Split the string by a substring using `n` splits.          Results in a struct o, Split the string by a substring, restricted to returning at most `n` items., r"""         Replace first matching regex/literal substring with a new string va (+45 more)

### Community 1 - "Community 1"
Cohesion: 0.03
Nodes (54): ChronoFormatWarning, Warning issued when a chrono format string contains dubious patterns.      Polar, ExprStringNameSpace, Check if the string contains a substring that matches a pattern.          .. eng, Return the bytes offset of the first substring matching a pattern.          If t, Convert a String column into a Datetime column.          .. engine-support:: in-, Check if string values end with a substring.          .. engine-support:: in-mem, Check if string values start with a substring.          .. engine-support:: in-m (+46 more)

### Community 2 - "Community 2"
Cohesion: 0.02
Nodes (53): ExprDateTimeNameSpace, Determine whether the year of the underlying date is a leap year.          Appli, Extract ISO year from underlying Date representation.          Applies to Date a, Extract quarter from underlying Date representation.          Applies to Date an, Extract month from underlying Date representation.          Applies to Date and, Extract the number of days in the month from the underlying Date representation., Extract the week from the underlying Date representation.          Applies to Da, Extract the week day from the underlying Date representation.          Applies t (+45 more)

### Community 3 - "Community 3"
Cohesion: 0.06
Nodes (57): Shift values by the given number of indices.          Parameters         -------, Start a lazy query from this point. This returns a `LazyFrame` object., Add columns to this DataFrame.          Added columns will replace existing colu, Aggregate the columns of this DataFrame to their maximum value.          Example, Aggregate the columns of this DataFrame to their minimum value.          Example, Aggregate the columns of this DataFrame to their sum value.          Examples, Aggregate the columns of this DataFrame to their mean value.          Examples, Aggregate the columns of this DataFrame to their standard deviation value. (+49 more)

### Community 4 - "Community 4"
Cohesion: 0.10
Nodes (66): Binary, Boolean, Categorical, Date, Decimal, Duration, Enum, Float16 (+58 more)

### Community 5 - "Community 5"
Cohesion: 0.03
Nodes (46): CustomUFuncWarning, OutOfBoundsError, Warning issued when a custom ufunc is handled differently than numpy ufunc would, Exception raised when the given index is out of bounds., Compute the element-wise value for the cosine.          .. engine-support:: in-m, Compute the element-wise value for the inverse tangent.          .. engine-suppo, Compute the element-wise value for the inverse hyperbolic sine.          .. engi, Convert from degrees to radians.          .. engine-support:: in-memory, streami (+38 more)

### Community 6 - "Community 6"
Cohesion: 0.03
Nodes (84): approx_n_unique(), arctan2(), arctan2d(), arg_sort_by(), arg_where(), coalesce(), collect_all(), collect_all_async() (+76 more)

### Community 7 - "Community 7"
Cohesion: 0.04
Nodes (40): Get part of the DataFrame as a new DataFrame, Series, or scalar.          Parame, Modify DataFrame elements in place, using assignment syntax.          Parameters, Get an ordered mapping of column names to their data type.          This is an a, Write to Apache Avro file.          Parameters         ----------         file, Write DataFrame as delta table.          Parameters         ----------         t, Return an estimation of the total (heap) allocated size of the `DataFrame`., Replace a column at an index location.          This operation is in place., Replace a column by a new Series (in place). (+32 more)

### Community 8 - "Community 8"
Cohesion: 0.04
Nodes (78): all(), alpha(), alphanumeric(), array(), binary(), boolean(), by_dtype(), by_index() (+70 more)

### Community 9 - "Community 9"
Cohesion: 0.03
Nodes (39): Set the number of columns that are visible when displaying tables.          Para, Display the data type next to the column name (to the right, in parentheses)., Print the DataFrame shape information below the data when displaying tables., Set table formatting style.          Parameters         ----------         forma, Hide table column data types (i64, f64, str etc.).          Examples         ---, Hide table column names.          Examples         --------         >>> df = pl., Hide the '---' separator displayed between the column names and column types., Hide the DataFrame shape information when displaying tables.          Examples (+31 more)

### Community 10 - "Community 10"
Cohesion: 0.03
Nodes (35): assert_schema_equal(), Assert that the schema of the left and right frame are equal.      Raises a deta, raise_assertion_error(), Raise a detailed assertion error., Start a `when-then-otherwise` expression.      Always initiated by a `pl.when()., when(), Lazily read from an Apache Iceberg table.      Parameters     ----------     sou, scan_iceberg() (+27 more)

### Community 11 - "Community 11"
Cohesion: 0.05
Nodes (26): Method equivalent of equality operator `series == other` where `None == None`., Method equivalent of equality operator `series != other` where `None == None`., Convert leaf dtype the to given primitive datatype.          This is equivalent, Format output data in HTML for display in Jupyter Notebooks., A Series represents a single column in a Polars DataFrame.      Parameters     -, Return the Series as a scalar, or return the element at the given index., Cast this Series to a DataFrame.          Parameters         ----------, Raise to the power of the given exponent.          If the exponent is float, the (+18 more)

### Community 12 - "Community 12"
Cohesion: 0.08
Nodes (35): ArrowDriverProperties, ODBCCursorProxy, OracleCursorProxy, Cursor proxy for `python-oracledb` connections., Cursor proxy for ODBC connections (requires `arrow-odbc`)., Execute a query (n/a: just store query for the fetch* methods)., # TODO: is this fetch_all not supposed to be from the argument?, Cursor proxy for both SurrealDB and AsyncSurrealDB connections. (+27 more)

### Community 13 - "Community 13"
Cohesion: 0.03
Nodes (33): r'''         Offers a structured way to apply a sequence of user-defined functio, r"""         Compute time-based exponentially-weighted moving sum.          .. w, Compute the natural logarithm of each element plus one.          This computes `, Return the cumulative count of the non-null values in the column.          .. en, Take values by index.          .. engine-support:: in-memory, streaming, Get minimum value.          .. engine-support:: in-memory, streaming, distribute, Get minimum value, but propagate/poison encountered NaN values.          This di, Return a boolean mask indicating the first occurrence of each distinct value. (+25 more)

### Community 14 - "Community 14"
Cohesion: 0.05
Nodes (35): PerformanceWarning, Warning issued to indicate potential performance pitfalls., Allows to alter the lazy frame during the plan stage with the resolved schema., Return the `k` largest rows.          Non-null elements are always preferred ove, Return the `k` smallest rows.          Non-null elements are always preferred ov, Cache the result once the execution of the physical plan hits this node., Select columns from this LazyFrame.          This will run all expression sequen, Perform an asof join.          This is similar to a left-join except that we mat (+27 more)

### Community 15 - "Community 15"
Cohesion: 0.09
Nodes (29): CredentialProviderBuilder, CredentialProviderAzure, Azure Credential Provider.      Using this requires the `azure-identity` Python, Initialize a credential provider for Microsoft Azure.          By default, this, Fetch the credentials., Configuration for writing to multiple output files.      .. warning::         Th, Catalog, CatalogCredentialProvider (+21 more)

### Community 16 - "Community 16"
Cohesion: 0.03
Nodes (22): Expr, Compute the element-wise value for the cotangent.          .. engine-support:: i, Compute the element-wise value for the inverse cosine.          .. engine-suppor, Method equivalent of bitwise "not" operator `~expr`.          This has the effec, Returns a boolean Series indicating which values are null.          .. engine-su, Run an expression over a sliding window that increases `1` slot every iteration., Evaluate the number of unset bits.          .. engine-support:: in-memory, strea, Read an expression from a JSON encoded string to construct an Expression. (+14 more)

### Community 17 - "Community 17"
Cohesion: 0.03
Nodes (30): ExprBinaryNameSpace, r"""         Check if values start with a binary substring.          .. engine-s, r"""         Decode values using the provided encoding.          .. engine-suppo, Namespace for bin related expressions., r"""         Encode a value using the provided encoding.          .. engine-supp, r"""         Get the size of binary values in the given unit.          .. engine, r"""         Check if binaries in Series contain a binary substring.          .., r"""         Interpret bytes as another type.          Supported types are numer (+22 more)

### Community 18 - "Community 18"
Cohesion: 0.06
Nodes (45): DuplicateError, Exception raised when a column name is duplicated.              Examples, Export a Schema via the Arrow PyCapsule Interface.          https://arrow.apache, Get the column names of the schema.          Examples         --------         >, Get the data types of the schema.          Examples         --------         >>>, Convert the schema to a pyarrow schema.          Parameters         ----------, Create an empty DataFrame (or LazyFrame) from this Schema.          Parameters, Get the number of schema entries.          Examples         --------         >>> (+37 more)

### Community 19 - "Community 19"
Cohesion: 0.05
Nodes (30): PolarsDataFrame, Return the column with the given name.          Parameters         ----------, Return an iterator yielding the columns., Create a new dataframe by selecting a subset of columns by index.          Param, Create a new dataframe by selecting a subset of columns by name.          Parame, Return an iterator yielding the chunks of the dataframe.          Parameters, A dataframe object backed by a Polars DataFrame.      Parameters     ----------, Return chunks of this dataframe according to the chunks of the first column. (+22 more)

### Community 20 - "Community 20"
Cohesion: 0.04
Nodes (28): ExprCatNameSpace, Return the number of characters of the string representation of each value., Check if string representations of values start with a substring.          .. en, Namespace for categorical related expressions., Check if string representations of values end with a substring.          .. engi, Extract a substring from the string representation of each value.          .. en, Get the categories stored in this data type.          Examples         --------, Convert to a categorical or enum `dtype`.          The input must be of the phys (+20 more)

### Community 21 - "Community 21"
Cohesion: 0.04
Nodes (28): Calculate the lower bound.          Returns a unit Series with the lowest value, Replace the given values by different values of the same data type.          .., Replace all values by different values.          .. engine-support:: in-memory,, Get a slice of this expression.          .. engine-support:: in-memory, streamin, r"""         Cast between data types.          .. engine-support:: in-memory, st, Get minimum value, ordered by another expression.          If the by expression, Get mask of unique values.          .. engine-support:: in-memory          Examp, Take every nth value in the Series and return as a new Series.          .. engin (+20 more)

### Community 22 - "Community 22"
Cohesion: 0.08
Nodes (52): arrow_to_pydf(), _check_pandas_columns(), dataframe_to_pydf(), dict_to_pydf(), _establish_dataclass_or_model_schema(), _expand_dict_data(), _expand_dict_values(), _handle_columns_arg() (+44 more)

### Community 23 - "Community 23"
Cohesion: 0.07
Nodes (29): _prepare_other_arg(), Module containing logic related to eager DataFrames., # TODO: Only raise when data must be copied, Convert categorical variables into dummy/indicator variables.          Parameter, Rechunk the data in this DataFrame to a contiguous allocation.          This wil, Create a new DataFrame that shows the null counts per column.          Examples, Sample from this DataFrame.          Parameters         ----------         n, # TODO: Dispatch to a native floordiv (+21 more)

### Community 24 - "Community 24"
Cohesion: 0.05
Nodes (29): _bytes_loader_lookup(), _convert_predicate(), _ensure_boolean_expression(), extract_field_initial_default(), IcebergColumnStatisticsLoader, IcebergStatisticsLoader, IdentityTransformedPartitionValuesBuilder, LoadBinaryFromBytes (+21 more)

### Community 25 - "Community 25"
Cohesion: 0.04
Nodes (25): Module containing the implementation of the Python dataframe interchange protoco, CompatLevel, Export a Series via the Arrow PyCapsule Interface.          https://arrow.apache, Return whether all values in the column are `True`.          Only works on colum, Drop all null values.          The original order of the remaining elements is p, Get the minimal value in this Series.          Examples         --------, Get the quantile value of this Series.          Parameters         ----------, Get a distinct integer ID for each run of identical values.          The ID star (+17 more)

### Community 26 - "Community 26"
Cohesion: 0.08
Nodes (26): CredentialProviderBuilderImpl, InitializedCredentialProvider, Instantiate a credential provider from configuration.          Parameters, Initialize with an already constructed provider., Content-based key that survives pickle round-trips., Wraps an already initialized credential provider., Builds credential providers.      This is used to defer credential provider init, Initialize configuration for building a credential provider.          Parameters (+18 more)

### Community 27 - "Community 27"
Cohesion: 0.04
Nodes (27): ModuleUpgradeRequiredError, Exception raised when a module is installed but needs to be upgraded., ModuleNotFoundError, Compute the cube root of the elements.          Optimization for          >>> pl, Compute the base 10 logarithm of the input array, element-wise.          Example, Reduce this Series to the mean value.          Examples         --------, Get variance of this Series.          Parameters         ----------         ddof, Bin continuous values into discrete categories based on their quantiles. (+19 more)

### Community 28 - "Community 28"
Cohesion: 0.04
Nodes (26): property, Return whether any of the values in the column are `True`.          Only works o, Compute the exponential, element-wise.          Examples         --------, Reduce this Series to the product value.          Notes         -----         If, Get the median of this Series.          Examples         --------         >>> s, Compress the Series data using run-length encoding.          Run-length encoding, Get the length of each individual chunk.          Examples         --------, Return the cumulative count of the non-null values in the column.          Param (+18 more)

### Community 29 - "Community 29"
Cohesion: 0.04
Nodes (26): ComputeError, Exception raised when Polars could not perform an underlying computation., Return an estimation of the total (heap) allocated size of the Series., Compute the logarithm to a given base.          Examples         --------, Drop all floating point NaN values.          The original order of the remaining, Get the maximum value in this Series.          Examples         --------, Get dummy/indicator variables.          Parameters         ----------         se, Count the occurrences of unique values.          Parameters         ---------- (+18 more)

### Community 30 - "Community 30"
Cohesion: 0.04
Nodes (26): Exception raised when trying to perform operations on data structures with incom, ShapeError, Compute the square root of the elements.          Syntactic sugar for          >, Compute the natural logarithm of the input array plus one, element-wise., Reduce this Series to the sum value.          Notes         -----         * Dtyp, Get the standard deviation of this Series.          Parameters         ---------, Bin continuous values into discrete categories.          .. warning::, Return a count of the unique values in the order of appearance.          Example (+18 more)

### Community 31 - "Community 31"
Cohesion: 0.05
Nodes (29): NamedTuple, LRUCache, Clear the cache, removing all items., Return value associated with `key` if present, otherwise return `default`., Initialize cache with keys from an iterable, all set to the same value., Return an iterable view of the cache's items (keys and values)., Return an iterable view of the cache's keys., Remove specified key from the cache and return the associated value.          If (+21 more)

### Community 32 - "Community 32"
Cohesion: 0.07
Nodes (25): by_name(), expand_selector(), _expand_selector_dicts(), _expand_selector_dicts_tuple_keys(), _expand_selectors(), is_selector(), Expand selector to column names, with respect to a specific frame or target sche, Select all columns matching the given names.      .. versionadded:: 0.20.27 (+17 more)

### Community 33 - "Community 33"
Cohesion: 0.07
Nodes (12): DataFrame, Add columns to this DataFrame.          Added columns will replace existing colu, Compare a DataFrame with another object., Compare a DataFrame with another DataFrame., Compare a DataFrame with a non-DataFrame object., Shrink DataFrame memory usage.          Shrinks to fit the exact capacity needed, Two-dimensional data structure representing data as a table with rows and column, Convert this DataFrame to a pandas DataFrame.          This operation copies dat (+4 more)

### Community 34 - "Community 34"
Cohesion: 0.05
Nodes (25): # TODO: either make a change and return py-native list data here, or find, Set Series values in-place using a single index, boolean mask, or index array., # TODO: implement for these types without casting to series, # TODO: Use variable-length strings instead when NumPy 2.0.0 comes out:, # TODO: Only raise when data must be copied, # NOTE: This `= None` is needed to generate the docs with sphinx_accessor., r"""         Return the `k` smallest elements.          Non-null elements are al, Get unique index as Series.          Returns         -------         Series (+17 more)

### Community 35 - "Community 35"
Cohesion: 0.06
Nodes (22): Bin values into buckets and count their occurrences.          .. engine-support:, Append expressions.          This is done by adding the chunks of `other` to thi, Rounds down to the nearest integer value.          Only works on floating point, Create an object namespace of all struct related methods.          See the indiv, Fill null values using the specified value or strategy.          To interpolate, Fill missing values with the last non-null value.          This is an alias of `, Fill missing values with the next non-null value.          This is an alias of `, Compute the product of an expression.          .. engine-support:: in-memory, st (+14 more)

### Community 36 - "Community 36"
Cohesion: 0.10
Nodes (33): Int16, Int32, Int8, IntegerType, Base class for integer data types., Base class for signed integer data types., Base class for unsigned integer data types., 8-bit signed integer type. (+25 more)

### Community 37 - "Community 37"
Cohesion: 0.07
Nodes (21): BaseSchema, Get a mask of all duplicated rows in this DataFrame.          Examples         -, Convert a `DataFrame` to a `Series` of type `Struct`.          Parameters, Export a DataFrame via the Arrow PyCapsule Interface.          https://arrow.apa, Convert DataFrame to a dictionary mapping column name to values.          Parame, Serialize to JSON representation.          Parameters         ----------, Create a plot namespace.          .. warning::             This functionality is, Offers a structured way to apply a sequence of user-defined functions (UDFs). (+13 more)

### Community 38 - "Community 38"
Cohesion: 0.05
Nodes (21): DataType, ObjectType, Base class for all Polars data types., Return this DataType's fundamental/root type class.          Examples         --, Check if this DataType is the same as another DataType.          This is a stric, Check whether the data type is a numeric type., Check whether the data type is a decimal type., Check whether the data type is an integer type. (+13 more)

### Community 39 - "Community 39"
Cohesion: 0.08
Nodes (13): LazyFrame, Create a string representation of the query plan.          Different optimizatio, Show a plot of the query plan.          Note that Graphviz must be installed to, Representation of a Lazy computation graph/query against a DataFrame.      This, Return lazy representation, i.e. itself.          Useful for writing code that e, Create an empty copy of the current LazyFrame, with zero to 'n' rows.          R, Create a copy of this LazyFrame.          This is a cheap operation that does no, Common code for filter/remove ops. (+5 more)

### Community 40 - "Community 40"
Cohesion: 0.13
Nodes (34): _build_table_patterns(), _extract_table(), from_arrow(), from_dataframe(), _from_dataframe_repr(), from_dict(), from_dicts(), from_numpy() (+26 more)

### Community 41 - "Community 41"
Cohesion: 0.09
Nodes (22): DataTypeGroup, frozenset, _gpu_engine_callback(), Show the first `n` rows.          Parameters         ----------         limit :, # TODO: drop sort once we have efficient retrieval of multiple quantiles, Profile a LazyFrame.          .. deprecated:: 1.43.0             It was made for, Materialize this `LazyFrame` into a `DataFrame`.          By default, all query, Collect DataFrame asynchronously in thread pool.          .. warning:: (+14 more)

### Community 42 - "Community 42"
Cohesion: 0.09
Nodes (22): PolarsInefficientMapWarning, Warning issued when a potentially slow `map_*` operation is performed., BytecodeParser, InstructionTranslator, Introspect UDF bytecode and determine if we can rewrite as native expression., Initialize BytecodeParser instance and prepare to introspect UDFs.          Para, Drop extraneous/implied bool (eg: `pl.col("d") & pl.col("d").dt.date()`)., Return single function parameter name. (+14 more)

### Community 43 - "Community 43"
Cohesion: 0.06
Nodes (14): Column, PolarsColumn, Size of the column in elements., Offset of the first element with respect to the start of the underlying buffer., Data type of the column., Description of the categorical data type of the column., Description of the null representation the column uses., Number of null elements, if known. (+6 more)

### Community 44 - "Community 44"
Cohesion: 0.07
Nodes (19): LazyGroupBy, Apply a custom/user-defined function (UDF) over the groups as a new DataFrame., Utility class for performing a group by operation over a lazy DataFrame.      Ge, Get the first `n` rows of each group.          Parameters         ----------, Get the last `n` rows of each group.          Parameters         ----------, Aggregate the groups into Series.          Examples         --------         >>>, Filter groups with a list of predicates after aggregation.          Using this m, Return the number of rows in each group.          Parameters         ---------- (+11 more)

### Community 45 - "Community 45"
Cohesion: 0.06
Nodes (15): Filter elements by a boolean mask.          The original order of the remaining, Get the last `n` elements.          Parameters         ----------         n, Sort this Series.          Parameters         ----------         descending, Negate a boolean Series.          Returns         -------         Series, Construct a Series from Arrows C interface.          Parameters         --------, Create an empty copy of the current Series, with zero to 'n' elements., Return the underlying values, validity, and offsets buffers as Series., Construct a Series from information about its underlying buffer.          Parame (+7 more)

### Community 46 - "Community 46"
Cohesion: 0.10
Nodes (26): Buffer, IntEnum, PolarsBuffer, A buffer object backed by a Polars Series consisting of a single chunk.      Par, Buffer size in bytes., Pointer to start of the buffer as an integer., Represent this structure as DLPack interface., Device type and device ID for where the data in the buffer resides. (+18 more)

### Community 47 - "Community 47"
Cohesion: 0.09
Nodes (17): Config, Configure polars; offers options for table formatting and more.      Notes     -, Select columns from this DataFrame.          Parameters         ----------, Select columns from this DataFrame.          This will run all expression sequen, Get the maximum value horizontally across columns.          Returns         ----, Get the minimum value horizontally across columns.          Returns         ----, Sum all values horizontally across columns.          Parameters         --------, Take the mean of all values horizontally across columns.          Parameters (+9 more)

### Community 48 - "Community 48"
Cohesion: 0.07
Nodes (34): binary(), booleans(), categories(), data(), dates(), datetimes(), decimals(), durations() (+26 more)

### Community 49 - "Community 49"
Cohesion: 0.07
Nodes (15): Expr, ChainedThen, ChainedWhen, Define a default for the `when-then-otherwise` expression.          Parameters, Utility class for the `when-then-otherwise` expression.      Represents the stat, Attach a statement to the corresponding condition.          Parameters         -, Utility class for the `when-then-otherwise` expression.      Represents the stat, Add another condition to the `when-then-otherwise` expression.          Paramete (+7 more)

### Community 50 - "Community 50"
Cohesion: 0.09
Nodes (23): Returns all data as a dictionary of python-native values keyed by some column., Returns an iterator over the DataFrame of rows of python-native values., r"""         Returns a non-copying iterator of slices over the underlying DataFr, Return the DataFrame as a scalar, or return the element at the given row/column., Sort the dataframe by the given columns.          Parameters         ----------, Get a slice of this DataFrame.          Parameters         ----------         of, Get a single column by name.          Parameters         ----------         name, Create a spreadsheet-style pivot table as a DataFrame.          Only available i (+15 more)

### Community 51 - "Community 51"
Cohesion: 0.07
Nodes (17): ConfigParameters, Parameters supported by the polars Config., _check_if_delta_available(), _get_delta_lake_table(), Initialize a Delta lake table for use in read and scan operations.      Notes, _resolve_delta_lake_uri(), Return the number of threads in the Polars thread pool.      Notes     -----, Return the number of threads in the Polars thread pool.      .. deprecated:: 0.2 (+9 more)

### Community 52 - "Community 52"
Cohesion: 0.06
Nodes (14): Protocol, BasicConnection, BasicCursor, NumpyArray, PandasDataFrame, PandasIndex, PandasSeries, Protocol to match pandas dataframes without needing pandas-stubs installed. (+6 more)

### Community 53 - "Community 53"
Cohesion: 0.09
Nodes (14): Return a NumPy ndarray with the given data type.          This method ensures a, Get number of chunks used by the ChunkedArrays of this DataFrame.          Param, Returns an iterator over the columns of this DataFrame.          Yields, Decompose struct columns into separate columns for each of their fields., Return pairwise Pearson product-moment correlation coefficients between columns., Convert this DataFrame to a NumPy ndarray.          This operation copies data o, Insert a Series (or expression) at a certain column index.          This operati, Return a new DataFrame grown horizontally by stacking multiple Series to it. (+6 more)

### Community 54 - "Community 54"
Cohesion: 0.13
Nodes (29): ParameterCollisionError, Exception raised when the same parameter occurs multiple times., _csv_buffer_to_frame(), _drop_null_data(), _empty_frame(), _get_read_options(), _get_sheet_names(), _initialise_spreadsheet_parser() (+21 more)

### Community 55 - "Community 55"
Cohesion: 0.10
Nodes (12): IcebergSinkState, PlIcebergPathProviderConfig, _InternalPlPathProviderConfig, Inspect a node in the computation graph.          Print the value that this node, Resolve the schema of this LazyFrame.          .. caution::             Computin, Sink DataFrame as delta table.          .. engine-support:: streaming, distribut, Evaluate the query in streaming mode and get a generator that returns chunks., Get the column names.          Returns         -------         list of str (+4 more)

### Community 56 - "Community 56"
Cohesion: 0.09
Nodes (18): _compatible_frame(), _ensure_lazyframe(), _get_frame_locals(), Initialize a new `SQLContext`.          .. versionchanged:: 0.20.31, Immediately execute a SQL query, automatically registering frame globals., Track currently registered tables on scope entry; supports nested scopes., Unregister any tables created within the given scope on context exit.          S, Parse the given SQL query and execute it against the registered frame data. (+10 more)

### Community 57 - "Community 57"
Cohesion: 0.09
Nodes (9): Categories, A named collection of categories for :py:class:`Categorical`.      Two categorie, Creates a new `Categories` with a random name.          Parameters         -----, The name of this `Categories`., The namespace of this `Categories`., The physical type used to represent the categories., Returns whether this refers to the global categories., Return a :class:`Series` containing all categories in this `Categories`. (+1 more)

### Community 58 - "Community 58"
Cohesion: 0.07
Nodes (14): ListNameSpace, Run any polars expression against the lists' elements.          Parameters, Run any polars aggregation expression against the list' elements.          Param, Drop all null values in the list.          The original order of the remaining e, Namespace for list related methods., Evaluate whether all boolean values in a list are true.          Parameters, Concat the arrays in a Series dtype List in linear time.          Parameters, Get the value by index in the sublists.          So index `0` would return the f (+6 more)

### Community 59 - "Community 59"
Cohesion: 0.09
Nodes (28): _create_decimal_with_prec(), date_to_int(), datetime_to_int(), _localize_datetime(), negate_duration_string(), parse_as_duration_string(), _parse_fixed_tz_offset(), _raise_invalid_time_unit() (+20 more)

### Community 60 - "Community 60"
Cohesion: 0.10
Nodes (14): Get all runtime metadata for each column.          This is unstable and is meant, Select columns from this LazyFrame.          .. engine-support:: in-memory, stre, Selects rows from this LazyFrame at the given indices.          .. engine-suppor, Add columns to this LazyFrame.          Added columns will replace existing colu, Rename column names.          .. engine-support:: in-memory, streaming, distribu, Approximate count of unique values.          .. deprecated:: 0.20.11, Take every nth row in the LazyFrame and return as a new LazyFrame.          .. e, Fill null values using the specified value or strategy.          .. engine-suppo (+6 more)

### Community 61 - "Community 61"
Cohesion: 0.09
Nodes (14): Cast LazyFrame column(s) to the specified dtype(s).          .. engine-support::, Start a group by operation.          .. engine-support:: in-memory, partially-st, Group based on a time value (or index value of type Int32, Int64).          Time, Add a join operation to the Logical Plan.          .. engine-support:: in-memory, Remove columns from the DataFrame.          .. engine-support:: in-memory, strea, Add a row index as the first column in the LazyFrame.          .. engine-support, Support slice syntax, returning a new LazyFrame.          All other forms of sub, Add a column at index 0 that counts the rows.          .. deprecated:: 0.20.4 (+6 more)

### Community 62 - "Community 62"
Cohesion: 0.08
Nodes (14): Get a mask of all unique rows in this DataFrame.          Examples         -----, Hash and combine the rows in this DataFrame.          The hash value is of type, Write to Arrow IPC record batch stream.          See "Streaming format" in https, Execute a SQL query against the DataFrame.          .. versionadded:: 0.20.24, Check whether the DataFrame is equal to another DataFrame.          Parameters, Create rolling groups based on a temporal or integer column.          Different, Get the shape of the DataFrame.          Examples         --------         >>> d, PolarsDataset (+6 more)

### Community 63 - "Community 63"
Cohesion: 0.10
Nodes (14): Array, NestedType, Fixed length list type.      Parameters     ----------     inner         The `Da, The size of the Array., Struct composite type.      Parameters     ----------     fields         The fie, Return Struct dtype as a schema dict., Base class for nested data types., Struct (+6 more)

### Community 64 - "Community 64"
Cohesion: 0.08
Nodes (13): BinaryNameSpace, r"""         Decode values using the provided encoding.          Parameters, r"""         Encode values using the provided encoding.          Parameters, r"""         Get the size of the binary values in a Series in the given unit., Series.bin namespace., r"""         Interpret bytes as another type.          Supported types are numer, r"""         Slice the binary values.          Parameters         ----------, r"""         Get the byte value at the given index.          For example, index (+5 more)

### Community 65 - "Community 65"
Cohesion: 0.08
Nodes (13): CatNameSpace, Return the number of characters of the string representation of each value., Check if string representations of values start with a substring.          Param, Check if string representations of values end with a substring.          Paramet, Namespace for categorical related series., Extract a substring from the string representation of each string value., Create a Series with a categorical or enum `dtype`.          The input series mu, Get the physical values of a Series with a categorical or enum data type. (+5 more)

### Community 66 - "Community 66"
Cohesion: 0.27
Nodes (22): The metadata for the column., Return the number of chunks the column consists of., Return an iterator yielding the column chunks.          Parameters         -----, Return a dictionary containing the underlying buffers., A column object backed by a Polars Series.      Parameters     ----------     co, Size of the column in elements., Offset of the first element with respect to the start of the underlying buffer., Data type of the column. (+14 more)

### Community 67 - "Community 67"
Cohesion: 0.11
Nodes (12): _get_all_caller_variables(), Replace python method calls with synthetic POLARS_EXPRESSION op., Expand known 'superinstructions' into their component parts., Update/modify specific instructions to simplify multi-version parsing., Get all local and global variables from caller's frame., Standalone class that applies Instruction rewrite/filtering rules.      This sig, Check if a sequence of Instructions matches the specified ops/argvals., Apply rewrite rules, potentially injecting synthetic operations.          Rules (+4 more)

### Community 68 - "Community 68"
Cohesion: 0.09
Nodes (11): Return a NumPy ndarray with the given data type.          This method ensures a, Numpy universal functions., Quick summary statistics of a Series.          Series with mixed datatypes will, Append a Series to this one.          The resulting series will consist of multi, Check whether the Series contains one or more null values.          Examples, Check whether the Series contains one or more null values.          .. deprecate, Returns a boolean Series indicating which values are not null.          Returns, Cast to physical representation of the logical dtype.          - :func:`polars.d (+3 more)

### Community 69 - "Community 69"
Cohesion: 0.12
Nodes (11): HTMLFormatter, Module for formatting output data in HTML., Write the body of an HTML table., Append a raw string to the inner HTML., Return the lines needed to render a HTML table., Return the lines needed to render a HTML table., Replace consecutive spaces with HTML non-breaking spaces., Class for representing an HTML tag. (+3 more)

### Community 70 - "Community 70"
Cohesion: 0.14
Nodes (19): deque, apply(), _CancelledHandle, _get_event_loop(), _NestAsyncio2, _patch_asyncio(), _patch_loop(), _patch_policy() (+11 more)

### Community 71 - "Community 71"
Cohesion: 0.10
Nodes (11): Execute a SQL query against the LazyFrame.          .. engine-support:: streamin, Execute the query into a `QueryResult`.          This method of materializing a, Create rolling groups based on a temporal or integer column.          Different, Offers a structured way to apply a sequence of user-defined functions (UDFs)., Run a query remotely on Polars Cloud.          This allows you to run Polars rem, The result of a Polars query.      .. note::      This object should not be inst, The first n rows of the result., Total rows that are outputted by the result. (+3 more)

### Community 72 - "Community 72"
Cohesion: 0.13
Nodes (20): CategoricalRemappingWarning, PanicException, PolarsError, Exception raised when an unexpected schema mismatch causes an error., Exception raised when a specified schema field is not found., Exception raised when an error occurs in the SQL interface., Exception raised from the SQL interface when encountering invalid syntax., Exception raised when string caches come from different sources. (+12 more)

### Community 73 - "Community 73"
Cohesion: 0.10
Nodes (20): concat_arr(), concat_list(), concat_str(), date_(), datetime_(), duration(), format(), list() (+12 more)

### Community 74 - "Community 74"
Cohesion: 0.10
Nodes (10): _NamespaceSuggestMixin, Drop one or more fields from the struct.          Parameters         ----------, Get the struct definition as a name/dtype schema dict.          Examples, Convert this struct Series to a DataFrame with a separate column for each field., Convert this struct to a string column with json values.          Examples, Series.struct namespace., Get the names of the fields.          Examples         --------         >>> s =, Retrieve one of the fields of this `Struct` as a new Series.          Parameters (+2 more)

### Community 75 - "Community 75"
Cohesion: 0.14
Nodes (20): dtypes(), _flat_dtypes(), _instantiate_dtype(), _instantiate_flat_dtype(), _instantiate_nested_dtype(), _nested_dtypes(), _parse_dtype_restrictions(), Create a strategy for generating Polars :class:`DataType` objects.      .. warni (+12 more)

### Community 76 - "Community 76"
Cohesion: 0.10
Nodes (17): arrlen(), _cast_repr_strings_with_schema(), deduplicate_names(), display_dot_graph(), extend_bool(), _get_stack_locals(), _in_marimo_notebook(), _in_notebook() (+9 more)

### Community 77 - "Community 77"
Cohesion: 0.17
Nodes (9): BaseExtension, Extension, Base class for extension data types.      .. warning::         This functionalit, Creates an Extension type instance from its parameters., Returns the name of this extension type., Returns the storage type for this extension type., Returns the metadata for this extension type., Return a short string representation of the extension type.          This should (+1 more)

### Community 78 - "Community 78"
Cohesion: 0.10
Nodes (3): DataTypeClass, Metaclass for nicely printing DataType classes., type

### Community 79 - "Community 79"
Cohesion: 0.12
Nodes (10): Check whether the DataFrame is sorted by the given columns.          Parameters, Convert to a dataframe object implementing the dataframe interchange protocol., Show the first `n` rows.          Parameters         ----------         limit :, Get the first `n` rows.          Parameters         ----------         n, Get the first `n` rows.          Alias for :func:`DataFrame.head`.          Para, Extend the memory backed by this `DataFrame` with the values from `other`., Compute aggregations for each group of a group by operation.          Parameters, Apply a custom/user-defined function (UDF) over the groups as a new DataFrame. (+2 more)

### Community 80 - "Community 80"
Cohesion: 0.15
Nodes (15): _check_for_numpy(), _check_for_pandas(), _check_for_pyarrow(), _check_for_pydantic(), _check_for_pytz(), _check_for_torch(), import_optional(), _lazy_import() (+7 more)

### Community 81 - "Community 81"
Cohesion: 0.11
Nodes (10): _prepare_rolling_by_window_args(), Apply a rolling min based on another column.          .. warning::             T, Apply a rolling max based on another column.          .. warning::             T, Apply a rolling mean based on another column.          .. warning::, Apply a rolling sum based on another column.          .. warning::             T, Compute a rolling standard deviation based on another column.          .. warnin, Compute a rolling variance based on another column.          .. warning::, Compute a rolling median based on another column.          .. warning:: (+2 more)

### Community 82 - "Community 82"
Cohesion: 0.13
Nodes (17): arrow_to_pyseries(), _construct_series_with_fallbacks(), dataframe_to_pyseries(), iterable_to_pyseries(), numpy_to_pyseries(), pandas_to_pyseries(), # TODO: eventually go into struct builder, Construct Series, with fallbacks for basic type mismatch (eg: bool/int). (+9 more)

### Community 83 - "Community 83"
Cohesion: 0.12
Nodes (9): Group by the given columns and return the groups as separate dataframes., r"""         Drop duplicate rows from this DataFrame.          Parameters, Return the number of unique rows, or the number of unique row-subsets., Get the values of a single row, either by index or by predicate.          Parame, Returns all data in the DataFrame as a list of rows of python-native values., Returns `True` if the DataFrame contains no rows.          Examples         ----, Convert every row to a dictionary of Python-native values.          Notes, Write frame data to a table in an Excel workbook/worksheet.          Parameters (+1 more)

### Community 84 - "Community 84"
Cohesion: 0.11
Nodes (10): _prepare_alpha(), r"""         Compute exponentially-weighted moving average.          .. versionc, r"""         Compute exponentially-weighted moving sum.          .. engine-suppo, r"""         Compute exponentially-weighted moving standard deviation., r"""         Compute exponentially-weighted moving variance.          .. engine-, Compute the logarithm to a given base.          .. engine-support:: in-memory, s, Normalise EWM decay specification in terms of smoothing factor 'alpha'., # NOTE: This `= None` is needed to generate the docs with sphinx_accessor. (+2 more)

### Community 85 - "Community 85"
Cohesion: 0.12
Nodes (9): ExprStructNameSpace, Namespace for struct related expressions., Expand the struct into its individual fields.          Alias for `Expr.struct.fi, Rename the fields of the struct.          .. engine-support:: in-memory, streami, Return a struct field by name or by index.          .. engine-support:: in-memor, Drop one or more fields from the struct.          .. engine-support:: in-memory,, Convert this struct to a string column with json values.          .. engine-supp, Add or overwrite fields of this struct.          This is similar to `with_column (+1 more)

### Community 86 - "Community 86"
Cohesion: 0.20
Nodes (17): _combine_predicates(), _is_iterable(), _parse_constraints(), _parse_inputs_as_iterable(), parse_into_expression(), parse_into_list_of_expressions(), parse_into_list_of_expressions_require_selectors(), parse_into_selector() (+9 more)

### Community 87 - "Community 87"
Cohesion: 0.14
Nodes (14): call_expr(), _EmptyBytecodeHelper, expr_dispatch(), _expr_lookup(), get_ffi_func(), _is_empty_method(), Confirm that the given function has no implementation.      Definitions of empty, Dynamically obtain the proper FFI function/ method.      Parameters     -------- (+6 more)

### Community 88 - "Community 88"
Cohesion: 0.18
Nodes (13): BatchedCsvReader, Read a CSV file in batches., Read `n` batches from the reader.          Parameters         ----------, r"""     Read a CSV file into a DataFrame.      Polars expects CSV data to stric, r"""     Lazily read from a CSV file or multiple files via glob patterns.      T, # TODO: This is a hack. We conditionally set `missing_columns` to mimic, # TODO: We can't dispatch this for all paths due to a few reasons:, r"""     Read a CSV file in batches.      Upon creation of the `BatchedCsvReader (+5 more)

### Community 89 - "Community 89"
Cohesion: 0.15
Nodes (8): Get the DataType wrapped in a list.          Examples         --------         >, Get the DataType wrapped in an array.          Examples         --------, Get the unsigned integer version of the same bitsize.          Examples, Get the signed integer version of the same bitsize.          Examples         --, Get the inner DataType of a List or Array., DataTypeExprListNameSpace, Get the inner DataType of list., Namespace for list datatype expressions.

### Community 90 - "Community 90"
Cohesion: 0.17
Nodes (9): ABC, IcebergCatalogTableDescriptor, IcebergScanTableSerializer, IcebergTableSerializer, _NativeIcebergScanData, _PyIcebergScanData, Resolved parameters for a native Iceberg scan., Resolved parameters for reading via PyIceberg. (+1 more)

### Community 91 - "Community 91"
Cohesion: 0.14
Nodes (14): contains_nested(), _get_annotations(), get_first_non_none(), is_namedtuple(), is_pydantic_model(), is_sqlalchemy_row(), nt_unpack(), Determine if value contains (or is) nested structured data. (+6 more)

### Community 92 - "Community 92"
Cohesion: 0.19
Nodes (9): DeltaDataset, Fetch the DeltaTable object., Dataset interface for Delta., Fetch the schema of the table., Construct a LazyFrame scan., Lazily read from a Delta lake table.      Parameters     ----------     source, Reads into a DataFrame from a Delta lake table.      Parameters     ----------, read_delta() (+1 more)

### Community 93 - "Community 93"
Cohesion: 0.13
Nodes (8): ExprListNameSpace, Count how often the value produced by `element` occurs.          .. engine-suppo, Namespace for list related expressions., Compute the var value of the lists in the array.          .. engine-support:: in, Concat the arrays in a Series dtype List in linear time.          .. engine-supp, Check if sub-lists contain the given item.          .. engine-support:: in-memor, Retrieve an index of a minimal value in every sublist.          When multiple va, Retrieve the index of the maximum value in every sub-list.          When multipl

### Community 94 - "Community 94"
Cohesion: 0.16
Nodes (12): _check_empty(), _ensure_columns_are_unique(), looks_like_url(), null_count_dtype(), parse_columns_arg(), parse_row_index_args(), prepare_file_arg(), process_file_url() (+4 more)

### Community 95 - "Community 95"
Cohesion: 0.14
Nodes (14): all_horizontal(), any_horizontal(), cum_sum_horizontal(), max_horizontal(), mean_horizontal(), min_horizontal(), Get the maximum value horizontally across columns.      Parameters     ---------, Get the minimum value horizontally across columns.      Parameters     --------- (+6 more)

### Community 96 - "Community 96"
Cohesion: 0.17
Nodes (12): _create_namespace(), NameSpace, Decorator for registering custom functionality with a Polars DataFrame.      Par, Decorator for registering custom functionality with a Polars LazyFrame.      Par, Decorator for registering custom functionality with a polars Series.      Parame, Establish property-like namespace object for user-defined functionality., Register custom namespace against the underlying Polars class., Decorator for registering custom functionality with a Polars Expr.      Paramete (+4 more)

### Community 97 - "Community 97"
Cohesion: 0.19
Nodes (8): _convert_iceberg_to_object_store_storage_options(), IcebergScanResolver, IcebergTableWrap, Iceberg scan resolver.      Defers scan resolution to run during IR resolution., Fetch the schema of the table., Construct a LazyFrame scan., Fetch the PyIceberg Table object., Fetch the arrow schema of the table.

### Community 98 - "Community 98"
Cohesion: 0.21
Nodes (13): # TODO: Dispatch all paths to `scan_ipc` - this will need a breaking, Read into a DataFrame from Arrow IPC record batch stream.      See "Streaming fo, Get the schema of an IPC file without reading data.      Parameters     --------, Lazily read from an Arrow IPC (Feather v2) file or multiple files via glob patte, Read into a DataFrame from Arrow IPC (Feather v2) file.      See "File or Random, read_ipc(), _read_ipc_impl(), read_ipc_schema() (+5 more)

### Community 99 - "Community 99"
Cohesion: 0.13
Nodes (8): Cluster sequential `with_columns` calls to independent calls., Elide duplicate plans and caches their outputs., Elide duplicate expressions and caches their outputs., Do not maintain order if the order would not be observed., Replace simple projections with a faster inlined projection that skips the expre, The set of the optimizations considered during query optimization.      .. warni, Prepartition hive-partitioned joins on their partition key (requires `predicate_, IdentityFunction

### Community 100 - "Community 100"
Cohesion: 0.15
Nodes (14): _deprecate_function(), deprecate_nonkeyword_arguments(), deprecate_parameter_as_multi_positional(), deprecate_renamed_parameter(), deprecate_streaming_parameter(), deprecated(), _find_deprecated_functions(), identify_deprecations() (+6 more)

### Community 101 - "Community 101"
Cohesion: 0.31
Nodes (14): _convert_np_ndarray_to_indices(), _convert_series_to_indices(), get_df_item_by_key(), get_series_item_by_key(), _raise_on_boolean_mask(), _select_columns(), _select_columns_by_index(), _select_columns_by_mask() (+6 more)

### Community 102 - "Community 102"
Cohesion: 0.20
Nodes (9): Col, _create_col(), _get_class_objname(), _polars_dtype_match(), _python_dtype_match(), Create Polars column expressions.      Notes     -----     An instance of this c, Create one or more expressions representing columns in a DataFrame.          Par, Create a column expression using attribute syntax.          Note that this synta (+1 more)

### Community 103 - "Community 103"
Cohesion: 0.15
Nodes (11): Functions for reading data., FileProviderArgs, _InternalPlPathProviderConfig, _parse_to_pyexpr_list(), _PartitionByInner, Holds information on the file being sinked to.      .. warning::         This fu, Holds parsed partitioned sink options.      For internal use., Information on sinked paths. (+3 more)

### Community 104 - "Community 104"
Cohesion: 0.21
Nodes (11): column, dataframes(), _handle_null_probability_deprecation(), Hypothesis strategy for producing Polars DataFrames or LazyFrames.      .. warni, Hypothesis strategy for producing Polars Series.      .. warning::         This, Define a column for use with the `dataframes` strategy.      .. warning::, series(), columns() (+3 more)

### Community 105 - "Community 105"
Cohesion: 0.15
Nodes (12): all(), any(), cum_sum(), max(), min(), Get the maximum value.      Syntactic sugar for `col(names).max()`.      Paramet, Either return an expression representing all columns, or evaluate a bitwise AND, Get the minimum value.      Syntactic sugar for `col(names).min()`.      Paramet (+4 more)

### Community 106 - "Community 106"
Cohesion: 0.17
Nodes (2): NoPickleOption, Wrapper that does not pickle the wrapped value.      This wrapper will unpickle

### Community 107 - "Community 107"
Cohesion: 0.15
Nodes (6): DateTimeNameSpace, Cast the underlying data to another time unit. This may lose precision., Base offset from UTC.          This is usually constant for all datetimes in a g, Extract the century from underlying representation.          Applies to Date and, Extract the year from the underlying date representation.          Applies to Da, Offset by `n` business days.          .. warning::             This functionalit

### Community 108 - "Community 108"
Cohesion: 0.15
Nodes (6): Method equivalent of operator expression `series <= other`., Method equivalent of operator expression `series < other`., Method equivalent of operator expression `series == other`., Method equivalent of operator expression `series != other`., Method equivalent of operator expression `series >= other`., Method equivalent of operator expression `series > other`.

### Community 109 - "Community 109"
Cohesion: 0.17
Nodes (2): _AioDataFrameResult, _GeventDataFrameResult

### Community 110 - "Community 110"
Cohesion: 0.17
Nodes (6): DataTypeExprArrNameSpace, Get the inner DataType of array., Get the array width.          Examples         --------         >>> pl.select(pl, Get the array shape.          Examples         --------         >>> pl.select(pl, Namespace for arr datatype expressions., Create an object namespace of all array related methods.

### Community 111 - "Community 111"
Cohesion: 0.17
Nodes (6): DataTypeExpr, Get whether the output DataType is matches a certain selector.          Examples, Create an object namespace of all list related methods., Create an object namespace of all struct related methods., A lazily instantiated :class:`DataType` that can be used in an :class:`Expr`., Re-export Polars functionality to avoid cyclical imports.

### Community 112 - "Community 112"
Cohesion: 0.20
Nodes (10): dtype_short_repr_to_dtype(), dtype_to_ffiname(), dtype_to_py_type(), is_polars_dtype(), maybe_cast(), numpy_char_code_to_dtype(), py_type_to_arrow_type(), # TODO: further-improve handling for nested types (such as List,Struct) (+2 more)

### Community 113 - "Community 113"
Cohesion: 0.17
Nodes (6): ExprArrayNameSpace, Namespace for array related expressions., Compute the var of the values of the sub-arrays.          .. engine-support:: in, Retrieve an index of a minimal value in every sub-array.          When multiple, Retrieve an index of a maximum value in every sub-array.          When multiple, Check if sub-arrays contain the given item.          .. engine-support:: in-memo

### Community 114 - "Community 114"
Cohesion: 0.21
Nodes (7): IcebergCatalogConfig, Configuration for constructing a PyIceberg catalog.      This is useful for cons, Constructs an IcebergCatalogConfig from an instantiated PyIceberg catalog., Default options suitable for Iceberg / Deltalake.          This in general has a, Cast options applied when scanning files., Common configuration for scanning files.          .. warning::             This, ScanCastOptions

### Community 115 - "Community 115"
Cohesion: 0.21
Nodes (11): _datetime_to_dtype(), dtype_to_polars_dtype(), _duration_to_dtype(), get_buffer_length_in_elements(), polars_dtype_to_data_buffer_dtype(), polars_dtype_to_dtype(), Convert interchange protocol data type to Polars data type., Get the length of a buffer in elements. (+3 more)

### Community 116 - "Community 116"
Cohesion: 0.17
Nodes (6): Creates a summary of statistics for a LazyFrame, returning a DataFrame., Sort the LazyFrame by the given columns.          .. engine-support:: in-memory,, Aggregate the columns in the LazyFrame to their standard deviation value., Aggregate the columns in the LazyFrame as the sum of their null value count., Aggregate the columns in the LazyFrame to their quantile value.          .. engi, Return the number of non-null elements for each column.          .. engine-suppo

### Community 117 - "Community 117"
Cohesion: 0.18
Nodes (6): Get the number of chunks that this Series contains.          Examples         --, Convert this Series to a NumPy ndarray.          This operation copies data only, Convert this Series to a Jax Array.          .. versionadded:: 0.20.27, Convert this Series to a PyTorch Tensor.          .. versionadded:: 0.20.23, Return the underlying Arrow array.          If the Series contains only a single, Convert this Series to a pandas Series.          This operation copies data if `

### Community 118 - "Community 118"
Cohesion: 0.24
Nodes (2): AutoInit, _build_with_cache()

### Community 119 - "Community 119"
Cohesion: 0.20
Nodes (5): # NOTE: This `= None` is needed to generate the docs with sphinx_accessor., DataTypeExprStructNameSpace, Get the DataType of field with a specific field name.          Notes         ---, Get the field names in a struct as a list.          Examples         --------, Namespace for struct datatype expressions.

### Community 120 - "Community 120"
Cohesion: 0.22
Nodes (10): _normalise_numpy_dtype(), numpy_type_to_constructor(), numpy_values_and_dtype(), polars_type_to_constructor(), py_type_to_constructor(), Return numpy values and their associated dtype, adjusting if required., Get the right PySeries constructor for the given Polars dtype., Get the right PySeries constructor for the given Python dtype. (+2 more)

### Community 121 - "Community 121"
Cohesion: 0.44
Nodes (10): _categorical_column_to_series(), _column_to_series(), _construct_data_buffer(), _construct_offsets_buffer(), _construct_validity_buffer(), _construct_validity_buffer_from_bitmask(), _construct_validity_buffer_from_bytemask(), from_dataframe() (+2 more)

### Community 122 - "Community 122"
Cohesion: 0.18
Nodes (5): Draw line plot.          Polars does not implement plotting logic itself but ins, Series.plot namespace., Draw histogram.          Polars does not implement plotting logic itself but ins, Draw kernel density estimate plot.          Polars does not implement plotting l, SeriesPlot

### Community 123 - "Community 123"
Cohesion: 0.18
Nodes (5): Get a slice of this Series.          Parameters         ----------         offse, Get the first `n` elements.          Parameters         ----------         n, Get the first `n` elements.          Alias for :func:`Series.head`.          Par, Convert this Series to a Python list.          This operation copies data., Convert Series to instantiable string representation.          Parameters

### Community 124 - "Community 124"
Cohesion: 0.29
Nodes (5): check_cpu_flags(), CPUID, CPUID_struct, _open_posix_libc(), _read_cpu_flags()

### Community 125 - "Community 125"
Cohesion: 0.20
Nodes (5): EmptyCredentialError, _get_credentials_from_provider_expiry_aware(), Fetch the credentials for the configured profile name., Raised when boto3 returns empty credentials.          This generally indicates t, Exception

### Community 126 - "Community 126"
Cohesion: 0.36
Nodes (7): _get_adbc_driver_name_from_uri(), _get_adbc_module_name_from_uri(), _import_optional_adbc_driver(), _open_adbc_connection(), Run asynchronous code as if it was synchronous., _read_sql_adbc(), _run_async()

### Community 127 - "Community 127"
Cohesion: 0.20
Nodes (5): Evaluate whether any boolean value in a list is true.          .. engine-support, Run any polars aggregation expression against the lists' elements.          .. e, Count the number of unique values in every sub-list.          .. engine-support:, Evaluate whether all boolean values in a list are true.          .. engine-suppo, Get the single value of the sub-list.          .. engine-support:: in-memory, st

### Community 128 - "Community 128"
Cohesion: 0.27
Nodes (9): Get the schema of a Parquet file without reading data.      If you would like to, Get file-level custom metadata of a Parquet file without reading data.      .. w, Lazily read from a local or cloud-hosted parquet file (or files).      This func, Read into a DataFrame from a parquet file.      .. versionchanged:: 0.20.4, read_parquet(), read_parquet_metadata(), read_parquet_schema(), _read_parquet_with_pyarrow() (+1 more)

### Community 129 - "Community 129"
Cohesion: 0.20
Nodes (5): ArrayNameSpace, Compute the var of the values of the sub-arrays.          Examples         -----, Namespace for array related methods., Evaluate whether all boolean values are true for every subarray.          Parame, Run any polars aggregation expression against the arrays' elements.          Par

### Community 130 - "Community 130"
Cohesion: 0.20
Nodes (10): is_bool_sequence(), is_int_sequence(), _is_iterable_of(), is_path_or_str_sequence(), is_str_sequence(), Check whether the given iterable is of the given type(s)., Check that `val` is a sequence of strings or paths.      Note that a single stri, Check whether the given sequence is a sequence of booleans. (+2 more)

### Community 131 - "Community 131"
Cohesion: 0.33
Nodes (8): dtype_from_cursor_description(), dtype_from_database_typename(), integer_dtype_from_nbits(), Attempt to infer Polars dtype from database cursor description `type_code`., Return matching Polars integer dtype from num bits and signed/unsigned flag., Return `time_unit` from integer precision value.      Examples     --------, Attempt to infer Polars dtype from database cursor `type_code` string value., timeunit_from_precision()

### Community 132 - "Community 132"
Cohesion: 0.22
Nodes (4): Update the current optimization flags., Create new empty set off optimizations., Remove selected optimizations., Create new empty set off optimizations.

### Community 133 - "Community 133"
Cohesion: 0.33
Nodes (8): _is_dynamic_lib(), Serialize the function's keyword arguments., Get the file path of the dynamic library file., Register a plugin function.      See the `user guide <https://docs.pola.rs/user-, register_plugin_function(), _resolve_file_path(), _resolve_plugin_path(), _serialize_kwargs()

### Community 134 - "Community 134"
Cohesion: 0.36
Nodes (7): json_normalize(), _normalize_json(), _normalize_json_ordered(), Order the top level keys and then recursively go to depth.      Parameters     -, Normalize semi-structured deserialized JSON data into a flat table.      Diction, Main recursive function.      Designed for the most basic use case of `pl.json_n, _simple_json_normalize()

### Community 135 - "Community 135"
Cohesion: 0.25
Nodes (4): Unpack the query result., Fetch all results (as a list of dictionaries)., Fetch results in batches (simulated)., Unpack the async query result.

### Community 136 - "Community 136"
Cohesion: 0.25
Nodes (6): FloatType, NumericType, Base class for numeric data types., Return a literal expression representing the maximum value of this data type., Return a literal expression representing the minimum value of this data type., Base class for float data types.

### Community 137 - "Community 137"
Cohesion: 0.25
Nodes (4): Run any polars aggregation expression against the arrays' elements.          .., Count the number of unique values in every sub-arrays.          .. engine-suppor, Evaluate whether any boolean value is true for every subarray.          .. engin, Evaluate whether all boolean values are true for every subarray.          .. eng

### Community 138 - "Community 138"
Cohesion: 0.25
Nodes (4): Get the value by index in the sublists.          This is syntactic sugar for :me, Get the value by index in every sublist.          .. engine-support:: in-memory,, Get the first value of every sub-list.          .. engine-support:: in-memory, s, Get the last value of every sub-list.          .. engine-support:: in-memory, st

### Community 139 - "Community 139"
Cohesion: 0.39
Nodes (7): _one_or_zero_by_dtype(), ones(), Construct a column of length `n` filled with ones.      This is syntactic sugar, Construct a column of length `n` filled with zeros.      This is syntactic sugar, Construct a column of length `n` filled with the given value.      Parameters, repeat(), zeros()

### Community 140 - "Community 140"
Cohesion: 0.29
Nodes (4): Polars: Blazingly fast DataFrames =================================  Polars is a, # TODO: remove need for importing wrap utils at top level, Does nothing.      .. deprecated:: 1.41.0         The string cache was used to m, StringCache

### Community 141 - "Community 141"
Cohesion: 0.25
Nodes (4): ExtensionNameSpace, Series.ext namespace., Create a Series with an extension `dtype`.          The input series must have t, Get the storage values of a Series with an extension data type.          If the

### Community 142 - "Community 142"
Cohesion: 0.25
Nodes (2): PyArrowTable, Protocol to match PyArrow tables without needing PyArrow installed.      Only us

### Community 143 - "Community 143"
Cohesion: 0.29
Nodes (2): Field, Definition of a single field within a `Struct` DataType.      Parameters     ---

### Community 144 - "Community 144"
Cohesion: 0.29
Nodes (6): get_extension_type(), Register the extension type for the given extension name.      .. warning::, Unregister the extension type for the given extension name.      .. warning::, Get the extension type class for the given extension name.      If an extension, register_extension_type(), unregister_extension_type()

### Community 145 - "Community 145"
Cohesion: 0.29
Nodes (6): dtype_of(), Get a lazily evaluated :class:`DataType` of a column or expression.      .. warn, Get the dtype of `self` in `map_elements` and `map_batches`.      .. warning::, Create a new datatype expression that represents a Struct datatype.      .. warn, self_dtype(), struct_with_fields()

### Community 146 - "Community 146"
Cohesion: 0.33
Nodes (6): arange(), int_range(), int_ranges(), Generate a range of integers.      Parameters     ----------     start         S, Generate a range of integers for each row of the input columns.      Parameters, Generate a range of integers.      Alias for :func:`int_range`.      Parameters

### Community 147 - "Community 147"
Cohesion: 0.29
Nodes (6): disable_string_cache(), enable_string_cache(), Does nothing.      .. deprecated:: 1.41.0         The string cache was used to m, Does nothing.      .. deprecated:: 1.41.0         The string cache was used to m, Always returns true.      .. deprecated:: 1.41.0         The string cache was us, using_string_cache()

### Community 148 - "Community 148"
Cohesion: 0.53
Nodes (5): _assert_correct_input_type(), assert_frame_equal(), assert_frame_not_equal(), Assert that the left and right frame are **not** equal.      This function is in, Assert that the left and right frame are equal.      Raises a detailed `Assertio

### Community 149 - "Community 149"
Cohesion: 0.53
Nodes (5): _assert_correct_input_type(), assert_series_equal(), assert_series_not_equal(), Assert that the left and right Series are **not** equal.      This function is i, Assert that the left and right Series are equal.      Raises a detailed `Asserti

### Community 150 - "Community 150"
Cohesion: 0.33
Nodes (4): Enum, lit(), Return an expression representing a literal value.      Parameters     ---------, _NoDefault

### Community 151 - "Community 151"
Cohesion: 0.33
Nodes (3): Run any polars expression against the arrays' elements.          .. engine-suppo, Get the unique/distinct values in every sub-array.          .. engine-support::, Reverse the sub-arrays in this column.          .. engine-support:: in-memory, s

### Community 152 - "Community 152"
Cohesion: 0.33
Nodes (3): Get the value by index in the sub-arrays.          So index `0` would return the, Get the first value of the sub-arrays.          .. engine-support:: in-memory, s, Get the last value of the sub-arrays.          .. engine-support:: in-memory, st

### Community 153 - "Community 153"
Cohesion: 0.33
Nodes (3): Run any polars expression against every lists' elements.          .. engine-supp, Reverse the arrays in the list.          .. engine-support:: in-memory, streamin, Get the unique/distinct values in every sub-list.          .. engine-support:: i

### Community 154 - "Community 154"
Cohesion: 0.53
Nodes (3): _check_dtype(), _is_arrow_schema_exportable(), _required_init_args()

### Community 155 - "Community 155"
Cohesion: 0.33
Nodes (3): Fill null values using the specified value or strategy.          Parameters, Fill missing values with the next non-null value.          This is an alias of `, Fill missing values with the last non-null value.          This is an alias of `

### Community 156 - "Community 156"
Cohesion: 0.33
Nodes (3): Set new maximum cache size; cache is trimmed if value is smaller., Remove the least recently used value; raises KeyError if cache is empty., Insert a value into the cache.

### Community 157 - "Community 157"
Cohesion: 0.33
Nodes (2): FnPoolWrap, PyScanResolveThreadPool

### Community 158 - "Community 158"
Cohesion: 0.40
Nodes (4): Read the results of a SQL query into a DataFrame, given a URI.      Parameters, Read the results of a SQL query into a DataFrame, given a connection object., read_database(), read_database_uri()

### Community 159 - "Community 159"
Cohesion: 0.40
Nodes (4): _extract_delta_deletion_vectors(), _fetch_deletion_vectors(), Extract the deletion_vectors for the provided requested_paths.      Input reques, Fetch the deletion_vectors, mapping file_uri to "deletion_vector".      Schema:

### Community 160 - "Community 160"
Cohesion: 0.50
Nodes (4): business_day_count(), _holidays_to_expr(), Convert into Expr of List of Date., Count the number of business days between `start` and `end` (not including `end`

### Community 161 - "Community 161"
Cohesion: 0.50
Nodes (4): r"""     Construct a LazyFrame which scans lines into a string column from a fil, r"""     Read lines into a string column from a file.      .. warning::, read_lines(), scan_lines()

### Community 162 - "Community 162"
Cohesion: 0.50
Nodes (4): Lazily read from a newline delimited JSON file or multiple files via glob patter, r"""     Read into a DataFrame from a newline delimited JSON file.      Paramete, read_ndjson(), scan_ndjson()

### Community 163 - "Community 163"
Cohesion: 0.50
Nodes (4): _defer(), Deferred execution.      Takes a function that produces a `DataFrame` but defers, Register your IO plugin and initialize a LazyFrame.      See the `user guide <ht, register_io_source()

### Community 164 - "Community 164"
Cohesion: 0.60
Nodes (4): _get_dependency_list(), _get_dependency_version(), Print out the version of Polars and its optional dependencies.      Examples, show_versions()

### Community 165 - "Community 165"
Cohesion: 0.50
Nodes (4): load_profile(), Load a named (or custom) hypothesis profile for use with the parametric tests., Set the env var `POLARS_HYPOTHESIS_PROFILE` to the given profile name/value., set_profile()

### Community 166 - "Community 166"
Cohesion: 0.40
Nodes (4): Pickle the partially applied function `_scan_pyarrow_dataset_impl`.      The byt, Take the projected columns and materialize an arrow table.      Parameters     -, _scan_pyarrow_dataset(), _scan_pyarrow_dataset_impl()

### Community 167 - "Community 167"
Cohesion: 0.40
Nodes (4): date_range(), date_ranges(), Create a column of date ranges.      Parameters     ----------     start, Generate a date range.      Parameters     ----------     start         Lower bo

### Community 168 - "Community 168"
Cohesion: 0.40
Nodes (4): datetime_range(), datetime_ranges(), Create a column of datetime ranges.      Parameters     ----------     start, Generate a datetime range.      Parameters     ----------     start         Lowe

### Community 169 - "Community 169"
Cohesion: 0.40
Nodes (4): linear_space(), linear_spaces(), Generate a sequence of evenly-spaced values for each row between `start` and `en, Create sequence of evenly-spaced points.      Parameters     ----------     star

### Community 170 - "Community 170"
Cohesion: 0.40
Nodes (4): Create a column of time ranges.      Parameters     ----------     start, Generate a time range.      Parameters     ----------     start         Lower bo, time_range(), time_ranges()

### Community 171 - "Community 171"
Cohesion: 0.40
Nodes (4): is_pycapsule(), pycapsule_to_frame(), Check if object looks like it supports the PyCapsule interface., Convert PyCapsule object to DataFrame.

### Community 172 - "Community 172"
Cohesion: 0.40
Nodes (4): issue_unstable_warning(), Issue a warning for use of unstable functionality.      The `warn_unstable` sett, Decorator to mark a function as unstable., unstable()

### Community 174 - "Community 174"
Cohesion: 0.50
Nodes (2): pandas_series_to_arrow(), Convert a pandas Series to an Arrow Array.      Parameters     ----------     va

### Community 175 - "Community 175"
Cohesion: 0.50
Nodes (2): Fetch all results as a pyarrow Table., Fetch results as an iterable of RecordBatches.

### Community 176 - "Community 176"
Cohesion: 0.50
Nodes (2): classinstmethod, Decorator that allows a method to be called from the class OR instance.

### Community 177 - "Community 177"
Cohesion: 0.50
Nodes (2): Get the first `n` elements of the sub-arrays.          .. engine-support:: in-me, Slice every subarray.          .. engine-support:: in-memory, streaming, distrib

### Community 178 - "Community 178"
Cohesion: 0.50
Nodes (2): Flatten a list or string column.          Alias for :func:`Expr.list.explode`., Explode a list expression.          This means that every item is expanded to a

### Community 179 - "Community 179"
Cohesion: 0.50
Nodes (2): Slice every sub-list.          .. engine-support:: in-memory, streaming, distrib, Slice the first `n` values of every sub-list.          .. engine-support:: in-me

### Community 180 - "Community 180"
Cohesion: 0.50
Nodes (3): len(), Module containing the `len` function.  Keep this function in its own module to a, Return the number of rows in the context.      This is similar to `COUNT(*)` in

### Community 181 - "Community 181"
Cohesion: 0.50
Nodes (3): Functions for scanning Arrow C Stream sources., Scan a source that implements the Arrow PyCapsule Interface.      This creates a, scan_arrow_c_stream()

### Community 182 - "Community 182"
Cohesion: 0.50
Nodes (2): Convert a Date/Time/Datetime column into a String column with the given format., Convert a Date/Time/Datetime column into a String column with the given format.

### Community 183 - "Community 183"
Cohesion: 0.50
Nodes (2): Create an object namespace of all string related methods., Replace values by different values of the same data type.          Parameters

### Community 184 - "Community 184"
Cohesion: 0.50
Nodes (2): Count the null values in this Series.          Examples         --------, Return the number of non-null elements in the column.          See Also

### Community 185 - "Community 185"
Cohesion: 0.50
Nodes (2): Get the native polars datatype of this column.          .. warning::, Get the native polars schema of this table.          .. warning::             Th

### Community 186 - "Community 186"
Cohesion: 0.50
Nodes (4): issue_deprecation_warning(), Rename a keyword argument of a function., Issue a deprecation warning.      Parameters     ----------     message, _rename_keyword_argument()

### Community 188 - "Community 188"
Cohesion: 0.50
Nodes (3): Utility for serializing Polars objects., Serialize a Polars object (DataFrame/LazyFrame/Expr)., serialize_polars_object()

### Community 189 - "Community 189"
Cohesion: 0.50
Nodes (4): qualified_type_name(), Return the module-qualified name of the given object as a string.      Parameter, Raise an error if the two arguments are not of the same type.      The check wil, require_same_type()

### Community 190 - "Community 190"
Cohesion: 0.67
Nodes (2): escape_regex(), r"""     Escapes string regex meta characters.      Parameters     ----------

### Community 191 - "Community 191"
Cohesion: 0.67
Nodes (2): r"""     Set the global random seed for Polars.      This random seed is used to, set_random_seed()

### Community 192 - "Community 192"
Cohesion: 0.67
Nodes (2): parse_interval_argument(), Parse the interval argument as a Polars duration string.

### Community 193 - "Community 193"
Cohesion: 0.67
Nodes (2): _NamespaceSuggestMixin, Mixin that adds suggestions to AttributeError on namespace typos.

### Community 194 - "Community 194"
Cohesion: 1.00
Nodes (1): Execute a query (n/a: store query for the fetch* methods).

### Community 195 - "Community 195"
Cohesion: 1.00
Nodes (1): Fetch all rows as a single Arrow-capable dataframe object.

### Community 196 - "Community 196"
Cohesion: 1.00
Nodes (1): Fetch rows in batches, yielding Arrow-capable dataframe objects.

### Community 197 - "Community 197"
Cohesion: 1.00
Nodes (1): Execute a query (n/a: just store query for the fetch* methods).

### Community 198 - "Community 198"
Cohesion: 1.00
Nodes (1): Materialize the :class:`DataTypeExpr` in a specific context.          This is a

### Community 199 - "Community 199"
Cohesion: 1.00
Nodes (1): Get a default value of a specific type.          - Integers and floats are their

### Community 200 - "Community 200"
Cohesion: 1.00
Nodes (1): Get a formatted version of the output DataType.          Examples         ------

### Community 201 - "Community 201"
Cohesion: 1.00
Nodes (1): Union of two Enums.          .. deprecated:: 1.38             `Enum.union()` is

### Community 202 - "Community 202"
Cohesion: 1.00
Nodes (1): Return a literal expression representing the maximum value of this data type.

### Community 203 - "Community 203"
Cohesion: 1.00
Nodes (1): Return a literal expression representing the minimum value of this data type.

### Community 204 - "Community 204"
Cohesion: 1.00
Nodes (1): Count how often the value produced by `element` occurs.          .. engine-suppo

### Community 205 - "Community 205"
Cohesion: 1.00
Nodes (1): Returns a column with a separate row for every array element.          .. engine

### Community 206 - "Community 206"
Cohesion: 1.00
Nodes (1): Join all string items in a sub-array and place a separator between them.

### Community 207 - "Community 207"
Cohesion: 1.00
Nodes (1): Return the number of elements in each array.          .. engine-support:: in-mem

### Community 208 - "Community 208"
Cohesion: 1.00
Nodes (1): Compute the max values of the sub-arrays.          .. engine-support:: in-memory

### Community 209 - "Community 209"
Cohesion: 1.00
Nodes (1): Compute the mean of the values of the sub-arrays.          .. engine-support:: i

### Community 210 - "Community 210"
Cohesion: 1.00
Nodes (1): Compute the median of the values of the sub-arrays.          .. engine-support::

### Community 211 - "Community 211"
Cohesion: 1.00
Nodes (1): Compute the min values of the sub-arrays.          .. engine-support:: in-memory

### Community 212 - "Community 212"
Cohesion: 1.00
Nodes (1): Shift array values by the given number of indices.          .. engine-support::

### Community 213 - "Community 213"
Cohesion: 1.00
Nodes (1): Sort every sub-array.          .. engine-support:: in-memory, streaming, distrib

### Community 214 - "Community 214"
Cohesion: 1.00
Nodes (1): Compute the std of the values of the sub-arrays.          .. engine-support:: in

### Community 215 - "Community 215"
Cohesion: 1.00
Nodes (1): Compute the sum values of the sub-arrays.          .. engine-support:: in-memory

### Community 216 - "Community 216"
Cohesion: 1.00
Nodes (1): Slice the last `n` values of every sublist.          .. engine-support:: in-memo

### Community 217 - "Community 217"
Cohesion: 1.00
Nodes (1): Convert an Array column into a List column with the same inner data type.

### Community 218 - "Community 218"
Cohesion: 1.00
Nodes (1): Convert the Series of type `Array` to a Series of type `Struct`.          Parame

### Community 219 - "Community 219"
Cohesion: 1.00
Nodes (1): Return whether all values in the column are `True`.          Only works on colum

### Community 220 - "Community 220"
Cohesion: 1.00
Nodes (1): Compute the element-wise value for the inverse hyperbolic cosine.          .. en

### Community 221 - "Community 221"
Cohesion: 1.00
Nodes (1): Compute the element-wise value for the inverse sine.          .. engine-support:

### Community 222 - "Community 222"
Cohesion: 1.00
Nodes (1): Get the index values that would sort this column.          .. engine-support:: i

### Community 223 - "Community 223"
Cohesion: 1.00
Nodes (1): Return indices where expression evaluates `True`.          .. warning::

### Community 224 - "Community 224"
Cohesion: 1.00
Nodes (1): Get index of first unique value.          .. engine-support:: in-memory, streami

### Community 225 - "Community 225"
Cohesion: 1.00
Nodes (1): Create an object namespace of all binary related methods.          See the indiv

### Community 226 - "Community 226"
Cohesion: 1.00
Nodes (1): Evaluate the number most-significant unset bits before seeing a set bit.

### Community 227 - "Community 227"
Cohesion: 1.00
Nodes (1): Perform an aggregation of bitwise ORs.          .. engine-support:: in-memory, s

### Community 228 - "Community 228"
Cohesion: 1.00
Nodes (1): Evaluate the number least-significant unset bits before seeing a set bit.

### Community 229 - "Community 229"
Cohesion: 1.00
Nodes (1): Set values outside the given boundaries to the boundary value.          .. engin

### Community 230 - "Community 230"
Cohesion: 1.00
Nodes (1): Get an array with the cumulative min computed at every element.          .. engi

### Community 231 - "Community 231"
Cohesion: 1.00
Nodes (1): Bin continuous values into discrete categories.          .. engine-support:: in-

### Community 232 - "Community 232"
Cohesion: 1.00
Nodes (1): Compute the dot/inner product between two Expressions.          .. engine-suppor

### Community 233 - "Community 233"
Cohesion: 1.00
Nodes (1): Drop all null values.          .. engine-support:: in-memory, streaming, distrib

### Community 234 - "Community 234"
Cohesion: 1.00
Nodes (1): r"""         Check if this expression is close, i.e. almost equal, to the other

### Community 235 - "Community 235"
Cohesion: 1.00
Nodes (1): Return a boolean mask indicating the last occurrence of each distinct value.

### Community 236 - "Community 236"
Cohesion: 1.00
Nodes (1): Compute the kurtosis (Fisher or Pearson) of a dataset.          Kurtosis is the

### Community 237 - "Community 237"
Cohesion: 1.00
Nodes (1): Get maximum value.          .. engine-support:: in-memory, streaming, distribute

### Community 238 - "Community 238"
Cohesion: 1.00
Nodes (1): Compute the most occurring value(s).          Can return multiple Values.

### Community 239 - "Community 239"
Cohesion: 1.00
Nodes (1): Count null values.          .. engine-support:: in-memory, streaming, distribute

### Community 240 - "Community 240"
Cohesion: 1.00
Nodes (1): Get quantile value.          .. engine-support:: in-memory          Parameters

### Community 241 - "Community 241"
Cohesion: 1.00
Nodes (1): Compute a rolling kurtosis.          .. warning::             This functionality

### Community 242 - "Community 242"
Cohesion: 1.00
Nodes (1): Compute a rolling standard deviation.          A window of length `window_size`

### Community 243 - "Community 243"
Cohesion: 1.00
Nodes (1): Round to a number of significant figures.          .. engine-support:: in-memory

### Community 244 - "Community 244"
Cohesion: 1.00
Nodes (1): Sample from this expression.          .. engine-support:: in-memory          Par

### Community 245 - "Community 245"
Cohesion: 1.00
Nodes (1): Find indices where elements should be inserted to maintain order.          .. ma

### Community 246 - "Community 246"
Cohesion: 1.00
Nodes (1): Flags the expression as 'sorted'.          Enables downstream code to user fast

### Community 247 - "Community 247"
Cohesion: 1.00
Nodes (1): Shift values by the given number of indices.          .. engine-support:: in-mem

### Community 248 - "Community 248"
Cohesion: 1.00
Nodes (1): Shrink numeric columns to the minimal required datatype.          Shrink to the

### Community 249 - "Community 249"
Cohesion: 1.00
Nodes (1): Shuffle the contents of this expression.          Note this is shuffled independ

### Community 250 - "Community 250"
Cohesion: 1.00
Nodes (1): Compute the element-wise sign function on numeric types.          The returned v

### Community 251 - "Community 251"
Cohesion: 1.00
Nodes (1): Compute the element-wise value for the sine.          .. engine-support:: in-mem

### Community 252 - "Community 252"
Cohesion: 1.00
Nodes (1): Compute the element-wise value for the hyperbolic sine.          .. engine-suppo

### Community 253 - "Community 253"
Cohesion: 1.00
Nodes (1): r"""         Compute the sample skewness of a data set.          For normally di

### Community 254 - "Community 254"
Cohesion: 1.00
Nodes (1): Sort this column by the ordering of other columns.          .. engine-support::

### Community 255 - "Community 255"
Cohesion: 1.00
Nodes (1): Sort this column.          When used in a projection/selection context, the whol

### Community 256 - "Community 256"
Cohesion: 1.00
Nodes (1): Compute the square root of the elements.          .. engine-support:: in-memory,

### Community 257 - "Community 257"
Cohesion: 1.00
Nodes (1): Get standard deviation.          .. engine-support:: in-memory, streaming, distr

### Community 258 - "Community 258"
Cohesion: 1.00
Nodes (1): Create an object namespace of all string related methods.          See the indiv

### Community 259 - "Community 259"
Cohesion: 1.00
Nodes (1): Method equivalent of subtraction operator `expr - other`.          .. engine-sup

### Community 260 - "Community 260"
Cohesion: 1.00
Nodes (1): Get sum value.          .. engine-support:: in-memory, streaming, distributed

### Community 261 - "Community 261"
Cohesion: 1.00
Nodes (1): Compute the element-wise value for the tangent.          .. engine-support:: in-

### Community 262 - "Community 262"
Cohesion: 1.00
Nodes (1): Compute the element-wise value for the hyperbolic tangent.          .. engine-su

### Community 263 - "Community 263"
Cohesion: 1.00
Nodes (1): Cast to physical representation of the logical dtype.          - :func:`polars.d

### Community 264 - "Community 264"
Cohesion: 1.00
Nodes (1): r"""         Return the elements corresponding to the `k` largest elements of th

### Community 265 - "Community 265"
Cohesion: 1.00
Nodes (1): r"""         Return the `k` largest elements.          Non-null elements are alw

### Community 266 - "Community 266"
Cohesion: 1.00
Nodes (1): Method equivalent of float division operator `expr / other`.          .. engine-

### Community 267 - "Community 267"
Cohesion: 1.00
Nodes (1): Truncate numeric data toward zero to `decimals` number of decimal places.

### Community 268 - "Community 268"
Cohesion: 1.00
Nodes (1): Return a count of the unique values in the order of appearance.          This me

### Community 269 - "Community 269"
Cohesion: 1.00
Nodes (1): Get unique values of this expression.          `null` is considered to be a uniq

### Community 270 - "Community 270"
Cohesion: 1.00
Nodes (1): Calculate the upper bound.          Returns a unit Series with the highest value

### Community 271 - "Community 271"
Cohesion: 1.00
Nodes (1): Count the occurrence of unique values.          .. engine-support:: in-memory, s

### Community 272 - "Community 272"
Cohesion: 1.00
Nodes (1): Get variance.          .. engine-support:: in-memory, streaming, distributed

### Community 273 - "Community 273"
Cohesion: 1.00
Nodes (1): Filter a single column.          .. deprecated:: 0.20.4             Use the :fun

### Community 274 - "Community 274"
Cohesion: 1.00
Nodes (1): Method equivalent of bitwise exclusive-or operator `expr ^ other`.          .. e

### Community 275 - "Community 275"
Cohesion: 1.00
Nodes (1): Calculate the first discrete difference between shifted items of every sub-list.

### Community 276 - "Community 276"
Cohesion: 1.00
Nodes (1): Drop all null values in the list.          .. engine-support:: in-memory, stream

### Community 277 - "Community 277"
Cohesion: 1.00
Nodes (1): Returns a column with a separate row for every sub-list.          .. engine-supp

### Community 278 - "Community 278"
Cohesion: 1.00
Nodes (1): Filter elements in each list by a boolean expression.          .. engine-support

### Community 279 - "Community 279"
Cohesion: 1.00
Nodes (1): Take every n-th value start from offset in every sub-list.          .. engine-su

### Community 280 - "Community 280"
Cohesion: 1.00
Nodes (1): Take sub-lists by multiple indices.          .. engine-support:: in-memory, stre

### Community 281 - "Community 281"
Cohesion: 1.00
Nodes (1): Join all string items in a sub-list and place a separator between them.

### Community 282 - "Community 282"
Cohesion: 1.00
Nodes (1): Return the number of elements in each list.          Null values count towards t

### Community 283 - "Community 283"
Cohesion: 1.00
Nodes (1): Compute the max value of the lists in the array.          .. engine-support:: in

### Community 284 - "Community 284"
Cohesion: 1.00
Nodes (1): Compute the mean value of the lists in the array.          .. engine-support:: i

### Community 285 - "Community 285"
Cohesion: 1.00
Nodes (1): Compute the median value of the lists in the array.          .. engine-support::

### Community 286 - "Community 286"
Cohesion: 1.00
Nodes (1): Compute the min value of the lists in the array.          .. engine-support:: in

### Community 287 - "Community 287"
Cohesion: 1.00
Nodes (1): Sample from this list.          .. engine-support:: in-memory, streaming, distri

### Community 288 - "Community 288"
Cohesion: 1.00
Nodes (1): Compute the SET DIFFERENCE between the elements in this list and the elements of

### Community 289 - "Community 289"
Cohesion: 1.00
Nodes (1): Compute the SET INTERSECTION between the elements in this list and the elements

### Community 290 - "Community 290"
Cohesion: 1.00
Nodes (1): Compute the SET SYMMETRIC DIFFERENCE between the elements in this list and the e

### Community 291 - "Community 291"
Cohesion: 1.00
Nodes (1): Compute the SET UNION between the elements in this list and the elements of `oth

### Community 292 - "Community 292"
Cohesion: 1.00
Nodes (1): Shift every sub-lists values by the given number of indices.          .. engine-

### Community 293 - "Community 293"
Cohesion: 1.00
Nodes (1): Sort the lists in this column.          .. engine-support:: in-memory, streaming

### Community 294 - "Community 294"
Cohesion: 1.00
Nodes (1): Compute the std value of the lists in the array.          .. engine-support:: in

### Community 295 - "Community 295"
Cohesion: 1.00
Nodes (1): Sum all the lists in the array.          .. engine-support:: in-memory, streamin

### Community 296 - "Community 296"
Cohesion: 1.00
Nodes (1): Slice the last `n` values of every sub-list.          .. engine-support:: in-mem

### Community 297 - "Community 297"
Cohesion: 1.00
Nodes (1): Convert a List column into an Array column with the same inner data type.

### Community 298 - "Community 298"
Cohesion: 1.00
Nodes (1): Convert the Series of type `List` to a Series of type `Struct`.          .. engi

### Community 299 - "Community 299"
Cohesion: 1.00
Nodes (1): Apply predicates/filters as early as possible.

### Community 300 - "Community 300"
Cohesion: 1.00
Nodes (1): Only read columns that are used later in the query.

### Community 301 - "Community 301"
Cohesion: 1.00
Nodes (1): Run many expression optimization rules until fixed point.

### Community 302 - "Community 302"
Cohesion: 1.00
Nodes (1): Pushdown slices/limits.

### Community 303 - "Community 303"
Cohesion: 1.00
Nodes (1): Collapse sequential sort nodes into a single sort node.

### Community 304 - "Community 304"
Cohesion: 1.00
Nodes (1): Public functions that provide information about the Polars package or the enviro

### Community 305 - "Community 305"
Cohesion: 1.00
Nodes (1): Evaluate whether any boolean value is true for every subarray.          Paramete

### Community 306 - "Community 306"
Cohesion: 1.00
Nodes (1): Retrieve an index of a maximum value in every sub-array.          When multiple

### Community 307 - "Community 307"
Cohesion: 1.00
Nodes (1): Retrieve an index of a minimal value in every sub-array.          When multiple

### Community 308 - "Community 308"
Cohesion: 1.00
Nodes (1): Check if sub-arrays contain the given item.          Parameters         --------

### Community 309 - "Community 309"
Cohesion: 1.00
Nodes (1): Count how often the value produced by `element` occurs.          Parameters

### Community 310 - "Community 310"
Cohesion: 1.00
Nodes (1): Run any polars expression against the arrays' elements.          Parameters

### Community 311 - "Community 311"
Cohesion: 1.00
Nodes (1): Returns a column with a separate row for every array element.          Parameter

### Community 312 - "Community 312"
Cohesion: 1.00
Nodes (1): Get the first value of the sub-arrays.          Examples         --------

### Community 313 - "Community 313"
Cohesion: 1.00
Nodes (1): Get the value by index in the sub-arrays.          So index `0` would return the

### Community 314 - "Community 314"
Cohesion: 1.00
Nodes (1): Get the first `n` elements of the sub-arrays.          Parameters         ------

### Community 315 - "Community 315"
Cohesion: 1.00
Nodes (1): Join all string items in a sub-array and place a separator between them.

### Community 316 - "Community 316"
Cohesion: 1.00
Nodes (1): Get the last value of the sub-arrays.          Examples         --------

### Community 317 - "Community 317"
Cohesion: 1.00
Nodes (1): Return the number of elements in each array.          Returns         -------

### Community 318 - "Community 318"
Cohesion: 1.00
Nodes (1): Compute the max values of the sub-arrays.          Examples         --------

### Community 319 - "Community 319"
Cohesion: 1.00
Nodes (1): Compute the mean of the values of the sub-arrays.          Examples         ----

### Community 320 - "Community 320"
Cohesion: 1.00
Nodes (1): Compute the median of the values of the sub-arrays.          Examples         --

### Community 321 - "Community 321"
Cohesion: 1.00
Nodes (1): Compute the min values of the sub-arrays.          Examples         --------

### Community 322 - "Community 322"
Cohesion: 1.00
Nodes (1): Count the number of unique values in every sub-arrays.          Examples

### Community 323 - "Community 323"
Cohesion: 1.00
Nodes (1): Reverse the arrays in this column.          Examples         --------         >>

### Community 324 - "Community 324"
Cohesion: 1.00
Nodes (1): Shift array values by the given number of indices.          Parameters         -

### Community 325 - "Community 325"
Cohesion: 1.00
Nodes (1): Slice the sub-arrays.          Parameters         ----------         offset

### Community 326 - "Community 326"
Cohesion: 1.00
Nodes (1): Sort the arrays in this column.          Parameters         ----------         d

### Community 327 - "Community 327"
Cohesion: 1.00
Nodes (1): Compute the std of the values of the sub-arrays.          Examples         -----

### Community 328 - "Community 328"
Cohesion: 1.00
Nodes (1): Compute the sum values of the sub-arrays.          Notes         -----         I

### Community 329 - "Community 329"
Cohesion: 1.00
Nodes (1): Slice the last `n` values of every sublist.          Parameters         --------

### Community 330 - "Community 330"
Cohesion: 1.00
Nodes (1): Convert an Array column into a List column with the same inner data type.

### Community 331 - "Community 331"
Cohesion: 1.00
Nodes (1): Convert the series of type `Array` to a series of type `Struct`.          Parame

### Community 332 - "Community 332"
Cohesion: 1.00
Nodes (1): Get the unique/distinct values in the array.          Parameters         -------

### Community 333 - "Community 333"
Cohesion: 1.00
Nodes (1): Create a naive Datetime from an existing Date/Datetime expression and a Time.

### Community 334 - "Community 334"
Cohesion: 1.00
Nodes (1): Convert to given time zone for a Series of type Datetime.          Parameters

### Community 335 - "Community 335"
Cohesion: 1.00
Nodes (1): Extract (local) date.          Applies to Date/Datetime columns.          Return

### Community 336 - "Community 336"
Cohesion: 1.00
Nodes (1): Extract (local) datetime.          .. deprecated:: 0.20.4             Use `dt.re

### Community 337 - "Community 337"
Cohesion: 1.00
Nodes (1): Extract the number of days in the month from the underlying date representation.

### Community 338 - "Community 338"
Cohesion: 1.00
Nodes (1): Extract the day from the underlying date representation.          Applies to Dat

### Community 339 - "Community 339"
Cohesion: 1.00
Nodes (1): Additional offset currently in effect (typically due to daylight saving time).

### Community 340 - "Community 340"
Cohesion: 1.00
Nodes (1): Get the time passed since the Unix EPOCH in the give time unit.          Paramet

### Community 341 - "Community 341"
Cohesion: 1.00
Nodes (1): Extract the hour from the underlying DateTime representation.          Applies t

### Community 342 - "Community 342"
Cohesion: 1.00
Nodes (1): Determine whether each day lands on a business day.          .. warning::

### Community 343 - "Community 343"
Cohesion: 1.00
Nodes (1): Determine whether the year of the underlying date representation is a leap year.

### Community 344 - "Community 344"
Cohesion: 1.00
Nodes (1): Extract ISO year from underlying Date representation.          Applies to Date a

### Community 345 - "Community 345"
Cohesion: 1.00
Nodes (1): Return maximum as Python datetime.          Examples         --------         >>

### Community 346 - "Community 346"
Cohesion: 1.00
Nodes (1): Return mean as python DateTime.          .. deprecated:: 1.0.0             Use t

### Community 347 - "Community 347"
Cohesion: 1.00
Nodes (1): Return median as python DateTime.          .. deprecated:: 1.0.0             Use

### Community 348 - "Community 348"
Cohesion: 1.00
Nodes (1): Extract the microseconds from the underlying DateTime representation.          A

### Community 349 - "Community 349"
Cohesion: 1.00
Nodes (1): Extract the millennium from underlying representation.          Applies to Date

### Community 350 - "Community 350"
Cohesion: 1.00
Nodes (1): Extract the milliseconds from the underlying DateTime representation.          A

### Community 351 - "Community 351"
Cohesion: 1.00
Nodes (1): Return minimum as Python datetime.          Examples         --------         >>

### Community 352 - "Community 352"
Cohesion: 1.00
Nodes (1): Extract the minutes from the underlying DateTime representation.          Applie

### Community 353 - "Community 353"
Cohesion: 1.00
Nodes (1): Roll forward to the last day of the month.          Returns         -------

### Community 354 - "Community 354"
Cohesion: 1.00
Nodes (1): Roll backward to the first day of the month.          Returns         -------

### Community 355 - "Community 355"
Cohesion: 1.00
Nodes (1): Extract the month from the underlying date representation.          Applies to D

### Community 356 - "Community 356"
Cohesion: 1.00
Nodes (1): Extract the nanoseconds from the underlying DateTime representation.          Ap

### Community 357 - "Community 357"
Cohesion: 1.00
Nodes (1): Offset this date by a relative time offset.          This differs from `pl.col("

### Community 358 - "Community 358"
Cohesion: 1.00
Nodes (1): Extract ordinal day from underlying date representation.          Applies to Dat

### Community 359 - "Community 359"
Cohesion: 1.00
Nodes (1): Extract quarter from underlying Date representation.          Applies to Date an

### Community 360 - "Community 360"
Cohesion: 1.00
Nodes (1): Replace time zone for a Series of type Datetime.          Different from `conver

### Community 361 - "Community 361"
Cohesion: 1.00
Nodes (1): Replace time unit.          Parameters         ----------         year

### Community 362 - "Community 362"
Cohesion: 1.00
Nodes (1): Divide the date/ datetime range into buckets.          - Each date/datetime in t

### Community 363 - "Community 363"
Cohesion: 1.00
Nodes (1): Extract seconds from underlying DateTime representation.          Applies to Dat

### Community 364 - "Community 364"
Cohesion: 1.00
Nodes (1): Extract (local) time.          Applies to Date/Datetime/Time columns.          R

### Community 365 - "Community 365"
Cohesion: 1.00
Nodes (1): Return a timestamp in the given time unit.          Parameters         ---------

### Community 366 - "Community 366"
Cohesion: 1.00
Nodes (1): Extract the total days from a Duration type.          Parameters         -------

### Community 367 - "Community 367"
Cohesion: 1.00
Nodes (1): Extract the total hours from a Duration type.          Parameters         ------

### Community 368 - "Community 368"
Cohesion: 1.00
Nodes (1): Extract the total microseconds from a Duration type.          Parameters

### Community 369 - "Community 369"
Cohesion: 1.00
Nodes (1): Extract the total milliseconds from a Duration type.          Parameters

### Community 370 - "Community 370"
Cohesion: 1.00
Nodes (1): Extract the total minutes from a Duration type.          Parameters         ----

### Community 371 - "Community 371"
Cohesion: 1.00
Nodes (1): Extract the total nanoseconds from a Duration type.          Parameters

### Community 372 - "Community 372"
Cohesion: 1.00
Nodes (1): Extract the total seconds from a Duration type.          Parameters         ----

### Community 373 - "Community 373"
Cohesion: 1.00
Nodes (1): Divide the date/ datetime range into buckets.          Each date/datetime is map

### Community 374 - "Community 374"
Cohesion: 1.00
Nodes (1): Extract the week day from the underlying date representation.          Applies t

### Community 375 - "Community 375"
Cohesion: 1.00
Nodes (1): Extract the week from the underlying date representation.          Applies to Da

### Community 376 - "Community 376"
Cohesion: 1.00
Nodes (1): Set time unit a Series of dtype Datetime or Duration.          .. deprecated:: 0

### Community 377 - "Community 377"
Cohesion: 1.00
Nodes (1): Returns a column with a separate row for every list element.          Parameters

### Community 378 - "Community 378"
Cohesion: 1.00
Nodes (1): Filter elements in each list by a boolean expression, returning a new Series of

### Community 379 - "Community 379"
Cohesion: 1.00
Nodes (1): Get the first value of the sublists.          Examples         --------

### Community 380 - "Community 380"
Cohesion: 1.00
Nodes (1): Take every n-th value start from offset in sublists.          Parameters

### Community 381 - "Community 381"
Cohesion: 1.00
Nodes (1): Take sublists by multiple indices.          The indices may be defined in a sing

### Community 382 - "Community 382"
Cohesion: 1.00
Nodes (1): Slice the first `n` values of every sublist.          Parameters         -------

### Community 383 - "Community 383"
Cohesion: 1.00
Nodes (1): Get the single value of the sublists.          This errors if the sublist length

### Community 384 - "Community 384"
Cohesion: 1.00
Nodes (1): Join all string items in a sublist and place a separator between them.

### Community 385 - "Community 385"
Cohesion: 1.00
Nodes (1): Get the last value of the sublists.          Examples         --------         >

### Community 386 - "Community 386"
Cohesion: 1.00
Nodes (1): Return the number of elements in each list.          Null values count towards t

### Community 387 - "Community 387"
Cohesion: 1.00
Nodes (1): Compute the max value of the arrays in the list.          Examples         -----

### Community 388 - "Community 388"
Cohesion: 1.00
Nodes (1): Compute the mean value of the arrays in the list.          Examples         ----

### Community 389 - "Community 389"
Cohesion: 1.00
Nodes (1): Compute the median value of the arrays in the list.          Examples         --

### Community 390 - "Community 390"
Cohesion: 1.00
Nodes (1): Compute the min value of the arrays in the list.          Examples         -----

### Community 391 - "Community 391"
Cohesion: 1.00
Nodes (1): Count the number of unique values in every sub-lists.          Examples

### Community 392 - "Community 392"
Cohesion: 1.00
Nodes (1): Reverse the arrays in the list.          Examples         --------         >>> s

### Community 393 - "Community 393"
Cohesion: 1.00
Nodes (1): Sample from this list.          Parameters         ----------         n

### Community 394 - "Community 394"
Cohesion: 1.00
Nodes (1): Compute the SET DIFFERENCE between the elements in this list and the elements of

### Community 395 - "Community 395"
Cohesion: 1.00
Nodes (1): Compute the SET INTERSECTION between the elements in this list and the elements

### Community 396 - "Community 396"
Cohesion: 1.00
Nodes (1): Compute the SET SYMMETRIC DIFFERENCE between the elements in this list and the e

### Community 397 - "Community 397"
Cohesion: 1.00
Nodes (1): Compute the SET UNION between the elements in this list and the elements of `oth

### Community 398 - "Community 398"
Cohesion: 1.00
Nodes (1): Shift list values by the given number of indices.          Parameters         --

### Community 399 - "Community 399"
Cohesion: 1.00
Nodes (1): Slice every sublist.          Parameters         ----------         offset

### Community 400 - "Community 400"
Cohesion: 1.00
Nodes (1): Sort the arrays in this column.          Parameters         ----------         d

### Community 401 - "Community 401"
Cohesion: 1.00
Nodes (1): Compute the std value of the arrays in the list.          Examples         -----

### Community 402 - "Community 402"
Cohesion: 1.00
Nodes (1): Sum all the arrays in the list.          Notes         -----         If there ar

### Community 403 - "Community 403"
Cohesion: 1.00
Nodes (1): Slice the last `n` values of every sublist.          Parameters         --------

### Community 404 - "Community 404"
Cohesion: 1.00
Nodes (1): Convert a List column into an Array column with the same inner data type.

### Community 405 - "Community 405"
Cohesion: 1.00
Nodes (1): Convert the series of type `List` to a series of type `Struct`.          Paramet

### Community 406 - "Community 406"
Cohesion: 1.00
Nodes (1): Get the unique/distinct values in the list.          Parameters         --------

### Community 407 - "Community 407"
Cohesion: 1.00
Nodes (1): Compute the var value of the arrays in the list.          Examples         -----

### Community 408 - "Community 408"
Cohesion: 1.00
Nodes (1): Get part of the Series as a new Series or scalar.          Parameters         --

### Community 409 - "Community 409"
Cohesion: 1.00
Nodes (1): Interpolate intermediate values.          Nulls at the beginning and end of the

### Community 410 - "Community 410"
Cohesion: 1.00
Nodes (1): Interpolate intermediate values with x-coordinate based on another column.

### Community 411 - "Community 411"
Cohesion: 1.00
Nodes (1): Compute absolute values.          Same as `abs(series)`.          Examples

### Community 412 - "Community 412"
Cohesion: 1.00
Nodes (1): Assign ranks to data, dealing with ties appropriately.          Parameters

### Community 413 - "Community 413"
Cohesion: 1.00
Nodes (1): Calculate the first discrete difference between shifted items.          Paramete

### Community 414 - "Community 414"
Cohesion: 1.00
Nodes (1): Computes percentage change between values.          Percentage change (as fracti

### Community 415 - "Community 415"
Cohesion: 1.00
Nodes (1): r"""         Compute the sample skewness of a data set.          For normally di

### Community 416 - "Community 416"
Cohesion: 1.00
Nodes (1): Compute the kurtosis (Fisher or Pearson) of a dataset.          Kurtosis is the

### Community 417 - "Community 417"
Cohesion: 1.00
Nodes (1): Set values outside the given boundaries to the boundary value.          Paramete

### Community 418 - "Community 418"
Cohesion: 1.00
Nodes (1): Return the lower bound of this Series' dtype as a unit Series.          See Also

### Community 419 - "Community 419"
Cohesion: 1.00
Nodes (1): Return the upper bound of this Series' dtype as a unit Series.          See Also

### Community 420 - "Community 420"
Cohesion: 1.00
Nodes (1): Replace all values by different values.          Parameters         ----------

### Community 421 - "Community 421"
Cohesion: 1.00
Nodes (1): Convert from radians to degrees.          Examples         --------         >>>

### Community 422 - "Community 422"
Cohesion: 1.00
Nodes (1): Convert from degrees to radians.          Examples         --------         >>>

### Community 423 - "Community 423"
Cohesion: 1.00
Nodes (1): Shuffle the contents of this Series.          Parameters         ----------

### Community 424 - "Community 424"
Cohesion: 1.00
Nodes (1): r"""         Compute exponentially-weighted moving average.          .. versionc

### Community 425 - "Community 425"
Cohesion: 1.00
Nodes (1): r"""         Compute exponentially-weighted moving sum.          .. warning::

### Community 426 - "Community 426"
Cohesion: 1.00
Nodes (1): r"""         Compute time-based exponentially weighted moving average.

### Community 427 - "Community 427"
Cohesion: 1.00
Nodes (1): r"""         Compute time-based exponentially weighted moving sum.          .. w

### Community 428 - "Community 428"
Cohesion: 1.00
Nodes (1): r"""         Compute exponentially-weighted moving standard deviation.

### Community 429 - "Community 429"
Cohesion: 1.00
Nodes (1): r"""         Compute exponentially-weighted moving variance.          .. version

### Community 430 - "Community 430"
Cohesion: 1.00
Nodes (1): Shrink numeric columns to the minimal required datatype.          Shrink to the

### Community 431 - "Community 431"
Cohesion: 1.00
Nodes (1): Get the chunks of this Series as a list of Series.          Examples         ---

### Community 432 - "Community 432"
Cohesion: 1.00
Nodes (1): Evaluate the number of set bits.

### Community 433 - "Community 433"
Cohesion: 1.00
Nodes (1): Evaluate the number of unset bits.

### Community 434 - "Community 434"
Cohesion: 1.00
Nodes (1): Evaluate the number most-significant set bits before seeing an unset bit.

### Community 435 - "Community 435"
Cohesion: 1.00
Nodes (1): Evaluate the number most-significant unset bits before seeing a set bit.

### Community 436 - "Community 436"
Cohesion: 1.00
Nodes (1): Evaluate the number least-significant set bits before seeing an unset bit.

### Community 437 - "Community 437"
Cohesion: 1.00
Nodes (1): Evaluate the number least-significant unset bits before seeing a set bit.

### Community 438 - "Community 438"
Cohesion: 1.00
Nodes (1): Perform an aggregation of bitwise ANDs.

### Community 439 - "Community 439"
Cohesion: 1.00
Nodes (1): Perform an aggregation of bitwise ORs.

### Community 440 - "Community 440"
Cohesion: 1.00
Nodes (1): Perform an aggregation of bitwise XORs.

### Community 441 - "Community 441"
Cohesion: 1.00
Nodes (2): _format_argument_list(), Format allowed arguments list for use in the warning message of `deprecate_nonke

### Community 442 - "Community 442"
Cohesion: 1.00
Nodes (1): Utility functions.  Functions that are part of the public API are re-exported he

### Community 443 - "Community 443"
Cohesion: 1.00
Nodes (2): is_sequence(), Check whether the given input is a numpy array or python sequence.

### Community 444 - "Community 444"
Cohesion: 1.00
Nodes (2): normalize_filepath(), Create a string path, expanding the home directory if present.

### Community 445 - "Community 445"
Cohesion: 1.00
Nodes (2): ordered_unique(), Return unique list of sequence values, maintaining their order of appearance.

### Community 446 - "Community 446"
Cohesion: 1.00
Nodes (2): parse_percentiles(), Transforms raw percentiles into our preferred format, adding the 50th percentile

### Community 447 - "Community 447"
Cohesion: 1.00
Nodes (2): parse_version(), Simple version parser; split into a tuple of ints for comparison.

### Community 448 - "Community 448"
Cohesion: 1.00
Nodes (2): range_to_series(), Fast conversion of the given range to a Series.

### Community 449 - "Community 449"
Cohesion: 1.00
Nodes (2): range_to_slice(), Return the given range as an equivalent slice.

### Community 450 - "Community 450"
Cohesion: 1.00
Nodes (2): Warn for possibly unintentional comparisons with None., warn_null_comparison()

### Community 451 - "Community 451"
Cohesion: 1.00
Nodes (2): Scale size in bytes to other size units (eg: "kb", "mb", "gb", "tb")., scale_bytes()

### Community 452 - "Community 452"
Cohesion: 1.00
Nodes (2): Escape a string for use in a Polars (Rust) regex., re_escape()

## Knowledge Gaps
- **852 isolated node(s):** `Utility functions.  Functions that are part of the public API are re-exported he`, `Initialize an LRU (Least Recently Used) cache with a specified maximum size.`, `Returns True if the cache is not empty, False otherwise.`, `Check if the key is in the cache.`, `Remove the item with the specified key from the cache.` (+847 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 106`** (2 nodes): `NoPickleOption`, `Wrapper that does not pickle the wrapped value.      This wrapper will unpickle`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 109`** (2 nodes): `_AioDataFrameResult`, `_GeventDataFrameResult`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 118`** (2 nodes): `AutoInit`, `_build_with_cache()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 142`** (2 nodes): `PyArrowTable`, `Protocol to match PyArrow tables without needing PyArrow installed.      Only us`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 143`** (2 nodes): `Field`, `Definition of a single field within a `Struct` DataType.      Parameters     ---`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 157`** (2 nodes): `FnPoolWrap`, `PyScanResolveThreadPool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 174`** (2 nodes): `pandas_series_to_arrow()`, `Convert a pandas Series to an Arrow Array.      Parameters     ----------     va`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 175`** (2 nodes): `Fetch all results as a pyarrow Table.`, `Fetch results as an iterable of RecordBatches.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 176`** (2 nodes): `classinstmethod`, `Decorator that allows a method to be called from the class OR instance.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 177`** (2 nodes): `Get the first `n` elements of the sub-arrays.          .. engine-support:: in-me`, `Slice every subarray.          .. engine-support:: in-memory, streaming, distrib`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 178`** (2 nodes): `Flatten a list or string column.          Alias for :func:`Expr.list.explode`.`, `Explode a list expression.          This means that every item is expanded to a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 179`** (2 nodes): `Slice every sub-list.          .. engine-support:: in-memory, streaming, distrib`, `Slice the first `n` values of every sub-list.          .. engine-support:: in-me`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 182`** (2 nodes): `Convert a Date/Time/Datetime column into a String column with the given format.`, `Convert a Date/Time/Datetime column into a String column with the given format.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 183`** (2 nodes): `Create an object namespace of all string related methods.`, `Replace values by different values of the same data type.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 184`** (2 nodes): `Count the null values in this Series.          Examples         --------`, `Return the number of non-null elements in the column.          See Also`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 185`** (2 nodes): `Get the native polars datatype of this column.          .. warning::`, `Get the native polars schema of this table.          .. warning::             Th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (2 nodes): `escape_regex()`, `r"""     Escapes string regex meta characters.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 191`** (2 nodes): `r"""     Set the global random seed for Polars.      This random seed is used to`, `set_random_seed()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 192`** (2 nodes): `parse_interval_argument()`, `Parse the interval argument as a Polars duration string.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 193`** (2 nodes): `_NamespaceSuggestMixin`, `Mixin that adds suggestions to AttributeError on namespace typos.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 194`** (1 nodes): `Execute a query (n/a: store query for the fetch* methods).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 195`** (1 nodes): `Fetch all rows as a single Arrow-capable dataframe object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 196`** (1 nodes): `Fetch rows in batches, yielding Arrow-capable dataframe objects.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 197`** (1 nodes): `Execute a query (n/a: just store query for the fetch* methods).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 198`** (1 nodes): `Materialize the :class:`DataTypeExpr` in a specific context.          This is a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 199`** (1 nodes): `Get a default value of a specific type.          - Integers and floats are their`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 200`** (1 nodes): `Get a formatted version of the output DataType.          Examples         ------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 201`** (1 nodes): `Union of two Enums.          .. deprecated:: 1.38             `Enum.union()` is`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 202`** (1 nodes): `Return a literal expression representing the maximum value of this data type.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 203`** (1 nodes): `Return a literal expression representing the minimum value of this data type.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 204`** (1 nodes): `Count how often the value produced by `element` occurs.          .. engine-suppo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 205`** (1 nodes): `Returns a column with a separate row for every array element.          .. engine`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 206`** (1 nodes): `Join all string items in a sub-array and place a separator between them.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 207`** (1 nodes): `Return the number of elements in each array.          .. engine-support:: in-mem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 208`** (1 nodes): `Compute the max values of the sub-arrays.          .. engine-support:: in-memory`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 209`** (1 nodes): `Compute the mean of the values of the sub-arrays.          .. engine-support:: i`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 210`** (1 nodes): `Compute the median of the values of the sub-arrays.          .. engine-support::`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 211`** (1 nodes): `Compute the min values of the sub-arrays.          .. engine-support:: in-memory`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 212`** (1 nodes): `Shift array values by the given number of indices.          .. engine-support::`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 213`** (1 nodes): `Sort every sub-array.          .. engine-support:: in-memory, streaming, distrib`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 214`** (1 nodes): `Compute the std of the values of the sub-arrays.          .. engine-support:: in`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 215`** (1 nodes): `Compute the sum values of the sub-arrays.          .. engine-support:: in-memory`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 216`** (1 nodes): `Slice the last `n` values of every sublist.          .. engine-support:: in-memo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 217`** (1 nodes): `Convert an Array column into a List column with the same inner data type.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 218`** (1 nodes): `Convert the Series of type `Array` to a Series of type `Struct`.          Parame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 219`** (1 nodes): `Return whether all values in the column are `True`.          Only works on colum`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 220`** (1 nodes): `Compute the element-wise value for the inverse hyperbolic cosine.          .. en`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 221`** (1 nodes): `Compute the element-wise value for the inverse sine.          .. engine-support:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 222`** (1 nodes): `Get the index values that would sort this column.          .. engine-support:: i`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 223`** (1 nodes): `Return indices where expression evaluates `True`.          .. warning::`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 224`** (1 nodes): `Get index of first unique value.          .. engine-support:: in-memory, streami`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 225`** (1 nodes): `Create an object namespace of all binary related methods.          See the indiv`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 226`** (1 nodes): `Evaluate the number most-significant unset bits before seeing a set bit.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 227`** (1 nodes): `Perform an aggregation of bitwise ORs.          .. engine-support:: in-memory, s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 228`** (1 nodes): `Evaluate the number least-significant unset bits before seeing a set bit.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 229`** (1 nodes): `Set values outside the given boundaries to the boundary value.          .. engin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 230`** (1 nodes): `Get an array with the cumulative min computed at every element.          .. engi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 231`** (1 nodes): `Bin continuous values into discrete categories.          .. engine-support:: in-`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 232`** (1 nodes): `Compute the dot/inner product between two Expressions.          .. engine-suppor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 233`** (1 nodes): `Drop all null values.          .. engine-support:: in-memory, streaming, distrib`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 234`** (1 nodes): `r"""         Check if this expression is close, i.e. almost equal, to the other`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 235`** (1 nodes): `Return a boolean mask indicating the last occurrence of each distinct value.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 236`** (1 nodes): `Compute the kurtosis (Fisher or Pearson) of a dataset.          Kurtosis is the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 237`** (1 nodes): `Get maximum value.          .. engine-support:: in-memory, streaming, distribute`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 238`** (1 nodes): `Compute the most occurring value(s).          Can return multiple Values.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 239`** (1 nodes): `Count null values.          .. engine-support:: in-memory, streaming, distribute`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 240`** (1 nodes): `Get quantile value.          .. engine-support:: in-memory          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 241`** (1 nodes): `Compute a rolling kurtosis.          .. warning::             This functionality`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 242`** (1 nodes): `Compute a rolling standard deviation.          A window of length `window_size``
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 243`** (1 nodes): `Round to a number of significant figures.          .. engine-support:: in-memory`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 244`** (1 nodes): `Sample from this expression.          .. engine-support:: in-memory          Par`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 245`** (1 nodes): `Find indices where elements should be inserted to maintain order.          .. ma`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 246`** (1 nodes): `Flags the expression as 'sorted'.          Enables downstream code to user fast`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 247`** (1 nodes): `Shift values by the given number of indices.          .. engine-support:: in-mem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 248`** (1 nodes): `Shrink numeric columns to the minimal required datatype.          Shrink to the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 249`** (1 nodes): `Shuffle the contents of this expression.          Note this is shuffled independ`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 250`** (1 nodes): `Compute the element-wise sign function on numeric types.          The returned v`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 251`** (1 nodes): `Compute the element-wise value for the sine.          .. engine-support:: in-mem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 252`** (1 nodes): `Compute the element-wise value for the hyperbolic sine.          .. engine-suppo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 253`** (1 nodes): `r"""         Compute the sample skewness of a data set.          For normally di`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 254`** (1 nodes): `Sort this column by the ordering of other columns.          .. engine-support::`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 255`** (1 nodes): `Sort this column.          When used in a projection/selection context, the whol`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 256`** (1 nodes): `Compute the square root of the elements.          .. engine-support:: in-memory,`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 257`** (1 nodes): `Get standard deviation.          .. engine-support:: in-memory, streaming, distr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 258`** (1 nodes): `Create an object namespace of all string related methods.          See the indiv`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 259`** (1 nodes): `Method equivalent of subtraction operator `expr - other`.          .. engine-sup`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 260`** (1 nodes): `Get sum value.          .. engine-support:: in-memory, streaming, distributed`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 261`** (1 nodes): `Compute the element-wise value for the tangent.          .. engine-support:: in-`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 262`** (1 nodes): `Compute the element-wise value for the hyperbolic tangent.          .. engine-su`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 263`** (1 nodes): `Cast to physical representation of the logical dtype.          - :func:`polars.d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 264`** (1 nodes): `r"""         Return the elements corresponding to the `k` largest elements of th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 265`** (1 nodes): `r"""         Return the `k` largest elements.          Non-null elements are alw`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 266`** (1 nodes): `Method equivalent of float division operator `expr / other`.          .. engine-`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 267`** (1 nodes): `Truncate numeric data toward zero to `decimals` number of decimal places.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 268`** (1 nodes): `Return a count of the unique values in the order of appearance.          This me`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 269`** (1 nodes): `Get unique values of this expression.          `null` is considered to be a uniq`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 270`** (1 nodes): `Calculate the upper bound.          Returns a unit Series with the highest value`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 271`** (1 nodes): `Count the occurrence of unique values.          .. engine-support:: in-memory, s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 272`** (1 nodes): `Get variance.          .. engine-support:: in-memory, streaming, distributed`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 273`** (1 nodes): `Filter a single column.          .. deprecated:: 0.20.4             Use the :fun`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 274`** (1 nodes): `Method equivalent of bitwise exclusive-or operator `expr ^ other`.          .. e`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 275`** (1 nodes): `Calculate the first discrete difference between shifted items of every sub-list.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 276`** (1 nodes): `Drop all null values in the list.          .. engine-support:: in-memory, stream`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 277`** (1 nodes): `Returns a column with a separate row for every sub-list.          .. engine-supp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 278`** (1 nodes): `Filter elements in each list by a boolean expression.          .. engine-support`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 279`** (1 nodes): `Take every n-th value start from offset in every sub-list.          .. engine-su`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 280`** (1 nodes): `Take sub-lists by multiple indices.          .. engine-support:: in-memory, stre`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 281`** (1 nodes): `Join all string items in a sub-list and place a separator between them.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 282`** (1 nodes): `Return the number of elements in each list.          Null values count towards t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 283`** (1 nodes): `Compute the max value of the lists in the array.          .. engine-support:: in`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 284`** (1 nodes): `Compute the mean value of the lists in the array.          .. engine-support:: i`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 285`** (1 nodes): `Compute the median value of the lists in the array.          .. engine-support::`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 286`** (1 nodes): `Compute the min value of the lists in the array.          .. engine-support:: in`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 287`** (1 nodes): `Sample from this list.          .. engine-support:: in-memory, streaming, distri`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 288`** (1 nodes): `Compute the SET DIFFERENCE between the elements in this list and the elements of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 289`** (1 nodes): `Compute the SET INTERSECTION between the elements in this list and the elements`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 290`** (1 nodes): `Compute the SET SYMMETRIC DIFFERENCE between the elements in this list and the e`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 291`** (1 nodes): `Compute the SET UNION between the elements in this list and the elements of `oth`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 292`** (1 nodes): `Shift every sub-lists values by the given number of indices.          .. engine-`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 293`** (1 nodes): `Sort the lists in this column.          .. engine-support:: in-memory, streaming`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 294`** (1 nodes): `Compute the std value of the lists in the array.          .. engine-support:: in`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 295`** (1 nodes): `Sum all the lists in the array.          .. engine-support:: in-memory, streamin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 296`** (1 nodes): `Slice the last `n` values of every sub-list.          .. engine-support:: in-mem`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 297`** (1 nodes): `Convert a List column into an Array column with the same inner data type.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 298`** (1 nodes): `Convert the Series of type `List` to a Series of type `Struct`.          .. engi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 299`** (1 nodes): `Apply predicates/filters as early as possible.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 300`** (1 nodes): `Only read columns that are used later in the query.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 301`** (1 nodes): `Run many expression optimization rules until fixed point.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 302`** (1 nodes): `Pushdown slices/limits.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 303`** (1 nodes): `Collapse sequential sort nodes into a single sort node.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 304`** (1 nodes): `Public functions that provide information about the Polars package or the enviro`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 305`** (1 nodes): `Evaluate whether any boolean value is true for every subarray.          Paramete`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 306`** (1 nodes): `Retrieve an index of a maximum value in every sub-array.          When multiple`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 307`** (1 nodes): `Retrieve an index of a minimal value in every sub-array.          When multiple`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 308`** (1 nodes): `Check if sub-arrays contain the given item.          Parameters         --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 309`** (1 nodes): `Count how often the value produced by `element` occurs.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 310`** (1 nodes): `Run any polars expression against the arrays' elements.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 311`** (1 nodes): `Returns a column with a separate row for every array element.          Parameter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 312`** (1 nodes): `Get the first value of the sub-arrays.          Examples         --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 313`** (1 nodes): `Get the value by index in the sub-arrays.          So index `0` would return the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 314`** (1 nodes): `Get the first `n` elements of the sub-arrays.          Parameters         ------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 315`** (1 nodes): `Join all string items in a sub-array and place a separator between them.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 316`** (1 nodes): `Get the last value of the sub-arrays.          Examples         --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 317`** (1 nodes): `Return the number of elements in each array.          Returns         -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 318`** (1 nodes): `Compute the max values of the sub-arrays.          Examples         --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 319`** (1 nodes): `Compute the mean of the values of the sub-arrays.          Examples         ----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 320`** (1 nodes): `Compute the median of the values of the sub-arrays.          Examples         --`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 321`** (1 nodes): `Compute the min values of the sub-arrays.          Examples         --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 322`** (1 nodes): `Count the number of unique values in every sub-arrays.          Examples`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 323`** (1 nodes): `Reverse the arrays in this column.          Examples         --------         >>`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 324`** (1 nodes): `Shift array values by the given number of indices.          Parameters         -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 325`** (1 nodes): `Slice the sub-arrays.          Parameters         ----------         offset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 326`** (1 nodes): `Sort the arrays in this column.          Parameters         ----------         d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 327`** (1 nodes): `Compute the std of the values of the sub-arrays.          Examples         -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 328`** (1 nodes): `Compute the sum values of the sub-arrays.          Notes         -----         I`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 329`** (1 nodes): `Slice the last `n` values of every sublist.          Parameters         --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 330`** (1 nodes): `Convert an Array column into a List column with the same inner data type.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 331`** (1 nodes): `Convert the series of type `Array` to a series of type `Struct`.          Parame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 332`** (1 nodes): `Get the unique/distinct values in the array.          Parameters         -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 333`** (1 nodes): `Create a naive Datetime from an existing Date/Datetime expression and a Time.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 334`** (1 nodes): `Convert to given time zone for a Series of type Datetime.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 335`** (1 nodes): `Extract (local) date.          Applies to Date/Datetime columns.          Return`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 336`** (1 nodes): `Extract (local) datetime.          .. deprecated:: 0.20.4             Use `dt.re`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 337`** (1 nodes): `Extract the number of days in the month from the underlying date representation.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 338`** (1 nodes): `Extract the day from the underlying date representation.          Applies to Dat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 339`** (1 nodes): `Additional offset currently in effect (typically due to daylight saving time).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 340`** (1 nodes): `Get the time passed since the Unix EPOCH in the give time unit.          Paramet`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 341`** (1 nodes): `Extract the hour from the underlying DateTime representation.          Applies t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 342`** (1 nodes): `Determine whether each day lands on a business day.          .. warning::`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 343`** (1 nodes): `Determine whether the year of the underlying date representation is a leap year.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 344`** (1 nodes): `Extract ISO year from underlying Date representation.          Applies to Date a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 345`** (1 nodes): `Return maximum as Python datetime.          Examples         --------         >>`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 346`** (1 nodes): `Return mean as python DateTime.          .. deprecated:: 1.0.0             Use t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 347`** (1 nodes): `Return median as python DateTime.          .. deprecated:: 1.0.0             Use`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 348`** (1 nodes): `Extract the microseconds from the underlying DateTime representation.          A`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 349`** (1 nodes): `Extract the millennium from underlying representation.          Applies to Date`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 350`** (1 nodes): `Extract the milliseconds from the underlying DateTime representation.          A`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 351`** (1 nodes): `Return minimum as Python datetime.          Examples         --------         >>`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 352`** (1 nodes): `Extract the minutes from the underlying DateTime representation.          Applie`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 353`** (1 nodes): `Roll forward to the last day of the month.          Returns         -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 354`** (1 nodes): `Roll backward to the first day of the month.          Returns         -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 355`** (1 nodes): `Extract the month from the underlying date representation.          Applies to D`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 356`** (1 nodes): `Extract the nanoseconds from the underlying DateTime representation.          Ap`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 357`** (1 nodes): `Offset this date by a relative time offset.          This differs from `pl.col("`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 358`** (1 nodes): `Extract ordinal day from underlying date representation.          Applies to Dat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 359`** (1 nodes): `Extract quarter from underlying Date representation.          Applies to Date an`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 360`** (1 nodes): `Replace time zone for a Series of type Datetime.          Different from `conver`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 361`** (1 nodes): `Replace time unit.          Parameters         ----------         year`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 362`** (1 nodes): `Divide the date/ datetime range into buckets.          - Each date/datetime in t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 363`** (1 nodes): `Extract seconds from underlying DateTime representation.          Applies to Dat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 364`** (1 nodes): `Extract (local) time.          Applies to Date/Datetime/Time columns.          R`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 365`** (1 nodes): `Return a timestamp in the given time unit.          Parameters         ---------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 366`** (1 nodes): `Extract the total days from a Duration type.          Parameters         -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 367`** (1 nodes): `Extract the total hours from a Duration type.          Parameters         ------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 368`** (1 nodes): `Extract the total microseconds from a Duration type.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 369`** (1 nodes): `Extract the total milliseconds from a Duration type.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 370`** (1 nodes): `Extract the total minutes from a Duration type.          Parameters         ----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 371`** (1 nodes): `Extract the total nanoseconds from a Duration type.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 372`** (1 nodes): `Extract the total seconds from a Duration type.          Parameters         ----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 373`** (1 nodes): `Divide the date/ datetime range into buckets.          Each date/datetime is map`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 374`** (1 nodes): `Extract the week day from the underlying date representation.          Applies t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 375`** (1 nodes): `Extract the week from the underlying date representation.          Applies to Da`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 376`** (1 nodes): `Set time unit a Series of dtype Datetime or Duration.          .. deprecated:: 0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 377`** (1 nodes): `Returns a column with a separate row for every list element.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 378`** (1 nodes): `Filter elements in each list by a boolean expression, returning a new Series of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 379`** (1 nodes): `Get the first value of the sublists.          Examples         --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 380`** (1 nodes): `Take every n-th value start from offset in sublists.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 381`** (1 nodes): `Take sublists by multiple indices.          The indices may be defined in a sing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 382`** (1 nodes): `Slice the first `n` values of every sublist.          Parameters         -------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 383`** (1 nodes): `Get the single value of the sublists.          This errors if the sublist length`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 384`** (1 nodes): `Join all string items in a sublist and place a separator between them.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 385`** (1 nodes): `Get the last value of the sublists.          Examples         --------         >`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 386`** (1 nodes): `Return the number of elements in each list.          Null values count towards t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 387`** (1 nodes): `Compute the max value of the arrays in the list.          Examples         -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 388`** (1 nodes): `Compute the mean value of the arrays in the list.          Examples         ----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 389`** (1 nodes): `Compute the median value of the arrays in the list.          Examples         --`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 390`** (1 nodes): `Compute the min value of the arrays in the list.          Examples         -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 391`** (1 nodes): `Count the number of unique values in every sub-lists.          Examples`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 392`** (1 nodes): `Reverse the arrays in the list.          Examples         --------         >>> s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 393`** (1 nodes): `Sample from this list.          Parameters         ----------         n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 394`** (1 nodes): `Compute the SET DIFFERENCE between the elements in this list and the elements of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 395`** (1 nodes): `Compute the SET INTERSECTION between the elements in this list and the elements`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 396`** (1 nodes): `Compute the SET SYMMETRIC DIFFERENCE between the elements in this list and the e`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 397`** (1 nodes): `Compute the SET UNION between the elements in this list and the elements of `oth`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 398`** (1 nodes): `Shift list values by the given number of indices.          Parameters         --`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 399`** (1 nodes): `Slice every sublist.          Parameters         ----------         offset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 400`** (1 nodes): `Sort the arrays in this column.          Parameters         ----------         d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 401`** (1 nodes): `Compute the std value of the arrays in the list.          Examples         -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 402`** (1 nodes): `Sum all the arrays in the list.          Notes         -----         If there ar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 403`** (1 nodes): `Slice the last `n` values of every sublist.          Parameters         --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 404`** (1 nodes): `Convert a List column into an Array column with the same inner data type.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 405`** (1 nodes): `Convert the series of type `List` to a series of type `Struct`.          Paramet`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 406`** (1 nodes): `Get the unique/distinct values in the list.          Parameters         --------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 407`** (1 nodes): `Compute the var value of the arrays in the list.          Examples         -----`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 408`** (1 nodes): `Get part of the Series as a new Series or scalar.          Parameters         --`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 409`** (1 nodes): `Interpolate intermediate values.          Nulls at the beginning and end of the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 410`** (1 nodes): `Interpolate intermediate values with x-coordinate based on another column.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 411`** (1 nodes): `Compute absolute values.          Same as `abs(series)`.          Examples`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 412`** (1 nodes): `Assign ranks to data, dealing with ties appropriately.          Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 413`** (1 nodes): `Calculate the first discrete difference between shifted items.          Paramete`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 414`** (1 nodes): `Computes percentage change between values.          Percentage change (as fracti`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 415`** (1 nodes): `r"""         Compute the sample skewness of a data set.          For normally di`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 416`** (1 nodes): `Compute the kurtosis (Fisher or Pearson) of a dataset.          Kurtosis is the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 417`** (1 nodes): `Set values outside the given boundaries to the boundary value.          Paramete`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 418`** (1 nodes): `Return the lower bound of this Series' dtype as a unit Series.          See Also`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 419`** (1 nodes): `Return the upper bound of this Series' dtype as a unit Series.          See Also`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 420`** (1 nodes): `Replace all values by different values.          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 421`** (1 nodes): `Convert from radians to degrees.          Examples         --------         >>>`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 422`** (1 nodes): `Convert from degrees to radians.          Examples         --------         >>>`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 423`** (1 nodes): `Shuffle the contents of this Series.          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 424`** (1 nodes): `r"""         Compute exponentially-weighted moving average.          .. versionc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 425`** (1 nodes): `r"""         Compute exponentially-weighted moving sum.          .. warning::`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 426`** (1 nodes): `r"""         Compute time-based exponentially weighted moving average.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 427`** (1 nodes): `r"""         Compute time-based exponentially weighted moving sum.          .. w`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 428`** (1 nodes): `r"""         Compute exponentially-weighted moving standard deviation.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 429`** (1 nodes): `r"""         Compute exponentially-weighted moving variance.          .. version`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 430`** (1 nodes): `Shrink numeric columns to the minimal required datatype.          Shrink to the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 431`** (1 nodes): `Get the chunks of this Series as a list of Series.          Examples         ---`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 432`** (1 nodes): `Evaluate the number of set bits.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 433`** (1 nodes): `Evaluate the number of unset bits.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 434`** (1 nodes): `Evaluate the number most-significant set bits before seeing an unset bit.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 435`** (1 nodes): `Evaluate the number most-significant unset bits before seeing a set bit.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 436`** (1 nodes): `Evaluate the number least-significant set bits before seeing an unset bit.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 437`** (1 nodes): `Evaluate the number least-significant unset bits before seeing a set bit.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 438`** (1 nodes): `Perform an aggregation of bitwise ANDs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 439`** (1 nodes): `Perform an aggregation of bitwise ORs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 440`** (1 nodes): `Perform an aggregation of bitwise XORs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 441`** (2 nodes): `_format_argument_list()`, `Format allowed arguments list for use in the warning message of `deprecate_nonke`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 442`** (1 nodes): `Utility functions.  Functions that are part of the public API are re-exported he`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 443`** (2 nodes): `is_sequence()`, `Check whether the given input is a numpy array or python sequence.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 444`** (2 nodes): `normalize_filepath()`, `Create a string path, expanding the home directory if present.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 445`** (2 nodes): `ordered_unique()`, `Return unique list of sequence values, maintaining their order of appearance.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 446`** (2 nodes): `parse_percentiles()`, `Transforms raw percentiles into our preferred format, adding the 50th percentile`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 447`** (2 nodes): `parse_version()`, `Simple version parser; split into a tuple of ints for comparison.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 448`** (2 nodes): `range_to_series()`, `Fast conversion of the given range to a Series.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 449`** (2 nodes): `range_to_slice()`, `Return the given range as an equivalent slice.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 450`** (2 nodes): `Warn for possibly unintentional comparisons with None.`, `warn_null_comparison()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 451`** (2 nodes): `Scale size in bytes to other size units (eg: "kb", "mb", "gb", "tb").`, `scale_bytes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 452`** (2 nodes): `Escape a string for use in a Polars (Rust) regex.`, `re_escape()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `sphinx_accessor` connect `Community 28` to `Community 111`, `Community 89`, `Community 199`, `Community 110`, `Community 198`, `Community 119`, `Community 200`, `Community 16`, `Community 2`, `Community 253`, `Community 236`, `Community 229`, `Community 21`, `Community 270`, `Community 250`, `Community 251`, `Community 5`, `Community 261`, `Community 221`, `Community 252`, `Community 20`, `Community 262`, `Community 220`, `Community 13`, `Community 17`, `Community 249`, `Community 244`, `Community 84`, `Community 271`, `Community 268`, `Community 246`, `Community 248`, `Community 35`, `Community 226`, `Community 228`, `Community 227`, `Community 225`, `Community 233`, `Community 230`, `Community 243`, `Community 267`, `Community 232`, `Community 238`, `Community 255`, `Community 258`, `Community 265`, `Community 264`, `Community 222`, `Community 245`, `Community 254`, `Community 247`, `Community 257`, `Community 272`, `Community 237`, `Community 260`, `Community 239`, `Community 224`, `Community 269`, `Community 235`, `Community 240`, `Community 231`, `Community 273`, `Community 178`, `Community 263`, `Community 259`, `Community 266`, `Community 274`, `Community 234`, `Community 219`, `Community 81`, `Community 223`, `Community 256`, `Community 242`, `Community 241`, `Community 108`, `Community 11`, `Community 34`, `Community 408`, `Community 68`, `Community 25`, `Community 29`, `Community 30`, `Community 27`, `Community 117`, `Community 123`, `Community 45`, `Community 183`, `Community 184`, `Community 155`, `Community 409`, `Community 410`, `Community 411`, `Community 412`, `Community 413`, `Community 414`, `Community 415`, `Community 416`, `Community 417`, `Community 418`, `Community 419`, `Community 420`, `Community 421`, `Community 422`, `Community 423`, `Community 424`, `Community 425`, `Community 426`, `Community 427`, `Community 428`, `Community 429`, `Community 430`, `Community 431`, `Community 432`, `Community 433`, `Community 434`, `Community 435`, `Community 436`, `Community 437`, `Community 438`, `Community 439`, `Community 440`, `Community 74`, `Community 76`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Why does `CompatLevel` connect `Community 25` to `Community 33`, `Community 23`, `Community 53`, `Community 83`, `Community 3`, `Community 79`, `Community 37`, `Community 62`, `Community 47`, `Community 50`, `Community 7`, `Community 66`, `Community 46`, `Community 43`, `Community 39`, `Community 14`, `Community 41`, `Community 60`, `Community 116`, `Community 55`, `Community 71`, `Community 61`, `Community 18`, `Community 108`, `Community 11`, `Community 34`, `Community 408`, `Community 68`, `Community 29`, `Community 30`, `Community 27`, `Community 28`, `Community 117`, `Community 123`, `Community 45`, `Community 183`, `Community 184`, `Community 155`, `Community 409`, `Community 410`, `Community 411`, `Community 412`, `Community 413`, `Community 414`, `Community 415`, `Community 416`, `Community 417`, `Community 418`, `Community 419`, `Community 420`, `Community 421`, `Community 422`, `Community 423`, `Community 424`, `Community 425`, `Community 426`, `Community 427`, `Community 428`, `Community 429`, `Community 430`, `Community 431`, `Community 432`, `Community 433`, `Community 434`, `Community 435`, `Community 436`, `Community 437`, `Community 438`, `Community 439`, `Community 440`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Why does `SeriesBuffers` connect `Community 34` to `Community 108`, `Community 11`, `Community 408`, `Community 68`, `Community 25`, `Community 29`, `Community 30`, `Community 27`, `Community 28`, `Community 117`, `Community 123`, `Community 45`, `Community 183`, `Community 184`, `Community 155`, `Community 409`, `Community 410`, `Community 411`, `Community 412`, `Community 413`, `Community 414`, `Community 415`, `Community 416`, `Community 417`, `Community 418`, `Community 419`, `Community 420`, `Community 421`, `Community 422`, `Community 423`, `Community 424`, `Community 425`, `Community 426`, `Community 427`, `Community 428`, `Community 429`, `Community 430`, `Community 431`, `Community 432`, `Community 433`, `Community 434`, `Community 435`, `Community 436`, `Community 437`, `Community 438`, `Community 439`, `Community 440`, `Community 10`, `Community 32`, `Community 9`, `Community 66`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Are the 525 inferred relationships involving `CompatLevel` (e.g. with `DataFrame` and `Module containing logic related to eager DataFrames.`) actually correct?**
  _`CompatLevel` has 525 INFERRED edges - model-reasoned connections that need verification._
- **Are the 502 inferred relationships involving `sphinx_accessor` (e.g. with `DataTypeExpr` and `Get whether the output DataType is matches a certain selector.          Examples`) actually correct?**
  _`sphinx_accessor` has 502 INFERRED edges - model-reasoned connections that need verification._
- **Are the 455 inferred relationships involving `ModuleUpgradeRequiredError` (e.g. with `CloseAfterFrameIter` and `ConnectionExecutor`) actually correct?**
  _`ModuleUpgradeRequiredError` has 455 INFERRED edges - model-reasoned connections that need verification._
- **Are the 433 inferred relationships involving `ShapeError` (e.g. with `Check pandas dataframe columns can be converted to polars.` and `Construct a PyDataFrame from a pandas DataFrame.`) actually correct?**
  _`ShapeError` has 433 INFERRED edges - model-reasoned connections that need verification._