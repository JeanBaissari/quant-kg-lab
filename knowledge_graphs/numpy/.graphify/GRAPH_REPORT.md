# Graph Report - numpy  (2026-08-06)

## Corpus Check
- Large corpus: 448 files · ~1,685,298 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 8306 nodes · 13483 edges · 619 communities detected
- Non-singleton communities: 595
- Extraction: EXTRACTED: 93.2% · INFERRED: 5.3%
- Edge kinds: calls: 4748 · contains: 5335 · imports: 10 · imports_from: 24 · inherits: 97 · method: 881 · rationale_for: 1677 · uses: 711

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 448 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 1 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `ab21997`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `ABCPolyBase` (251)
- `__init__.py` (221)
- `MaskedArray` (151)
- `f2c_d_lapack.c` (124)
- `f2c_s_lapack.c` (124)
- `auxfuncs.py` (117)
- `core.py` (115)
- `umath_linalg.cpp` (101)
- `fromnumeric.py` (92)
- `multiarraymodule.c` (92)

## Surprising Connections (you probably didn't know these)
- `Return the data pointer cast to a particular c-types object.         For example` --uses--> `DTypePromotionError`  [INFERRED]
  _core/_internal.py → exceptions.py
- `Return the shape tuple as an array of some other c-types         type. For examp` --uses--> `DTypePromotionError`  [INFERRED]
  _core/_internal.py → exceptions.py
- `Return the strides tuple as an array of some other         c-types type. For exa` --uses--> `DTypePromotionError`  [INFERRED]
  _core/_internal.py → exceptions.py
- `A pointer to the memory area of the array as a Python integer.         This memo` --uses--> `DTypePromotionError`  [INFERRED]
  _core/_internal.py → exceptions.py
- `(c_intp*self.ndim): A ctypes array of length self.ndim where         the basetyp` --uses--> `DTypePromotionError`  [INFERRED]
  _core/_internal.py → exceptions.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (122): dbdsdc_(), dbdsqr_(), dgebak_(), dgebal_(), dgebd2_(), dgebrd_(), dgeev_(), dgehd2_() (+114 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (122): sbdsdc_(), sbdsqr_(), sgebak_(), sgebal_(), sgebd2_(), sgebrd_(), sgeev_(), sgehd2_() (+114 more)

### Community 2 - "Community 2"
Cohesion: 0.03
Nodes (96): FutureWarning, allequal(), append(), argsort(), array(), _arraymethod(), asanyarray(), _check_fill_value() (+88 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (74): abs2(), addUfuncs(), call_evd(), call_geev(), call_gelsd(), call_geqrf(), call_gesdd(), call_gesv() (+66 more)

### Community 4 - "Community 4"
Cohesion: 0.04
Nodes (92): AxisConcatenator, AxisConcatenator, Translates slice objects to concatenation along an axis.      For detailed docum, MAError, Class for masked array related errors., apply_along_axis(), apply_over_axes(), average() (+84 more)

### Community 5 - "Community 5"
Cohesion: 0.03
Nodes (27): ABCPolyBase, Return series instance that has the specified roots.          Returns a series r, Identity function.          If ``p`` is the returned series, then ``p(x) == x``, Series basis polynomial of degree `deg`.          Returns the series representin, Convert series to series of this class.          The `series` is expected to be, Check if coefficients match.          Parameters         ----------         othe, Check if domains match.          Parameters         ----------         other : c, An abstract base class for immutable series classes.      ABCPolyBase provides t (+19 more)

### Community 6 - "Community 6"
Cohesion: 0.05
Nodes (81): analyzeargs(), analyzebody(), analyzecommon(), analyzeline(), analyzevars(), appenddecl(), appendmultiline(), buildimplicitrules() (+73 more)

### Community 7 - "Community 7"
Cohesion: 0.05
Nodes (75): bounded_lemire_uint64(), bounded_masked_uint64(), buffered_bounded_bool(), buffered_bounded_lemire_uint16(), buffered_bounded_lemire_uint32(), buffered_bounded_lemire_uint8(), buffered_bounded_masked_uint16(), buffered_bounded_masked_uint32() (+67 more)

### Community 8 - "Community 8"
Cohesion: 0.07
Nodes (83): cgebak_(), cgebal_(), cgebd2_(), cgebrd_(), cgeev_(), cgehd2_(), cgehrd_(), cgelq2_() (+75 more)

### Community 9 - "Community 9"
Cohesion: 0.07
Nodes (83): zgebak_(), zgebal_(), zgebd2_(), zgebrd_(), zgeev_(), zgehd2_(), zgehrd_(), zgelq2_() (+75 more)

### Community 11 - "Community 11"
Cohesion: 0.03
Nodes (35): MaskedArray, An array class with possibly masked values.      Masked values of True exclude t, Force the mask to hard, preventing unmasking by assignment.          Whether the, Force the mask to soft (default), allowing unmasking by assignment.          Whe, Specifies whether values can be unmasked through assignments.          By defaul, Share status of the mask (read-only)., Class of the underlying data (read-only)., Compare self with other using operator.eq or operator.ne.          When either o (+27 more)

### Community 12 - "Community 12"
Cohesion: 0.05
Nodes (56): add_numeric_cast(), add_other_to_and_from_string_cast(), can_cast_fields_safety(), can_cast_pyscalar_scalar_to(), cast_to_void_dtype_class(), _check_object_rec(), create_casting_impl(), dtype_kind_to_ordering() (+48 more)

### Community 13 - "Community 13"
Cohesion: 0.03
Nodes (72): cheb2poly(), chebadd(), chebcompanion(), chebder(), chebdiv(), chebfit(), chebfromroots(), chebgauss() (+64 more)

### Community 14 - "Community 14"
Cohesion: 0.04
Nodes (50): choose(), _DomainedBinaryOperation, _extrema_operation, get_masked_subclass(), getmask(), getmaskarray(), is_masked(), left_shift() (+42 more)

### Community 15 - "Community 15"
Cohesion: 0.05
Nodes (52): array_protocol_descr_get(), array_typestr_get(), arraydescr_field_subset_view(), _arraydescr_isnative(), arraydescr_isnative_get(), arraydescr_new(), arraydescr_newbyteorder(), arraydescr_protocol_descr_get() (+44 more)

### Community 16 - "Community 16"
Cohesion: 0.07
Nodes (62): add_minutes_to_datetimestruct(), add_seconds_to_datetimestruct(), can_cast_datetime64_metadata(), can_cast_datetime64_units(), can_cast_timedelta64_metadata(), can_cast_timedelta64_units(), cast_datetime_to_datetime(), cast_timedelta_to_timedelta() (+54 more)

### Community 17 - "Community 17"
Cohesion: 0.05
Nodes (3): container, Container class for backward compatibility with NumArray.  The user_array.contai, container(data, dtype=None, copy=True)      Standard container-class for easy mu

### Community 18 - "Community 18"
Cohesion: 0.07
Nodes (54): byteswap(), d(), gcd(), lcm(), make_rational_fast(), make_rational_int(), make_rational_slow(), npyrational_compare() (+46 more)

### Community 19 - "Community 19"
Cohesion: 0.05
Nodes (30): ABC, Backend, Backend, _get_flags(), _meson_identifier(), MesonBackend, MesonTemplate, _prepare_objects() (+22 more)

### Community 20 - "Community 20"
Cohesion: 0.05
Nodes (36): _check_mask_axis(), diag(), dot(), flatten_structured_array(), inner(), make_mask_none(), MaskError, Class for mask related errors. (+28 more)

### Community 22 - "Community 22"
Cohesion: 0.07
Nodes (53): _arange_safe_ceil_to_intp(), _array_fill_strides(), _array_from_array_like(), _array_from_buffer_3118(), array_from_text(), array_fromfile_binary(), byte_swap_vector(), _calc_length() (+45 more)

### Community 23 - "Community 23"
Cohesion: 0.04
Nodes (55): herme2poly(), hermeadd(), hermecompanion(), hermeder(), hermediv(), hermefit(), hermefromroots(), hermegauss() (+47 more)

### Community 24 - "Community 24"
Cohesion: 0.04
Nodes (55): herm2poly(), hermadd(), hermcompanion(), hermder(), hermdiv(), hermfit(), hermfromroots(), hermgauss() (+47 more)

### Community 25 - "Community 25"
Cohesion: 0.05
Nodes (33): addfield(), _checknames(), fromarrays(), fromrecords(), fromtextfile(), _guessvartypes(), MaskedRecords, _mrreconstruct() (+25 more)

### Community 26 - "Community 26"
Cohesion: 0.04
Nodes (53): lag2poly(), lagadd(), lagcompanion(), lagder(), lagdiv(), lagfit(), lagfromroots(), laggauss() (+45 more)

### Community 27 - "Community 27"
Cohesion: 0.04
Nodes (53): leg2poly(), legadd(), legcompanion(), legder(), legdiv(), legfit(), legfromroots(), leggauss() (+45 more)

### Community 28 - "Community 28"
Cohesion: 0.06
Nodes (31): npyiter_ass_subscript(), npyiter_cache_values(), npyiter_close(), npyiter_convert_dtypes(), npyiter_convert_op_axes(), npyiter_convert_op_flags_array(), npyiter_convert_ops(), npyiter_copy() (+23 more)

### Community 29 - "Community 29"
Cohesion: 0.07
Nodes (34): float_to_string(), get_cast_spec(), **
get_casts()(), get_dtypes(), get_s2type_dtypes(), get_type2s_dtypes(), getFloatToStringCastSpec(), getIntToStringCastSpec() (+26 more)

### Community 30 - "Community 30"
Cohesion: 0.04
Nodes (47): polyadd(), polycompanion(), polyder(), polydiv(), polyfit(), polyfromroots(), polygrid2d(), polygrid3d() (+39 more)

### Community 31 - "Community 31"
Cohesion: 0.06
Nodes (25): The `numpy.core` submodule exists solely for backward compatibility purposes. Th, array(), _deprecate_shape_0_as_None(), find_duplicate(), format_parser, fromarrays(), fromfile(), fromrecords() (+17 more)

### Community 32 - "Community 32"
Cohesion: 0.05
Nodes (19): applyrules(), containscommon(), containsderivedtypes(), containsmodule(), dictappend(), flatlist(), getargs2(), hasassumedshape() (+11 more)

### Community 34 - "Community 34"
Cohesion: 0.05
Nodes (20): cross(), diagonal(), LinAlgError, _raise_linalgerror_eigenvalues_nonconvergence(), _raise_linalgerror_lstsq(), _raise_linalgerror_nonposdef(), _raise_linalgerror_qr(), _raise_linalgerror_singular() (+12 more)

### Community 35 - "Community 35"
Cohesion: 0.06
Nodes (21): npyiter_allocate_buffers(), npyiter_coalesce_axes(), npyiter_copy_from_buffers(), npyiter_copy_to_buffers(), NpyIter_DebugPrint(), NpyIter_EnableExternalLoop(), npyiter_fill_buffercopy_params(), NpyIter_GetDataPtrArray() (+13 more)

### Community 36 - "Community 36"
Cohesion: 0.05
Nodes (7): add_loop(), init_comparison(), init_mixed_type_ufunc(), init_promoter(), init_string_ufuncs(), init_ufunc(), install_promoter()

### Community 37 - "Community 37"
Cohesion: 0.05
Nodes (38): allclose(), convolve(), _convolve_or_correlate(), correlate(), _DomainSafeDivide, getdata(), is_mask(), mask_or() (+30 more)

### Community 38 - "Community 38"
Cohesion: 0.05
Nodes (19): add_sfloats(), add_sfloats_resolve_descriptors(), cast_sfloat_to_sfloat_aligned(), cast_sfloat_to_sfloat_unaligned(), check_factor(), get_sfloat_dtype(), multiply_sfloats_resolve_descriptors(), python_sfloat_scaled_copy() (+11 more)

### Community 39 - "Community 39"
Cohesion: 0.05
Nodes (9): add_object_and_unicode_promoters(), add_promoter(), init_stringdtype_ufuncs(), init_ufunc(), is_integer_dtype(), string_inputs_promoter(), string_multiply_promoter(), string_object_bool_output_promoter() (+1 more)

### Community 40 - "Community 40"
Cohesion: 0.05
Nodes (21): asmatrix(), matrix, A convenience function for operations that want to collapse         to a scalar, Return the matrix as a (possibly nested) list.          See `ndarray.tolist` for, Returns the sum of the matrix elements, along the given axis.          Refer to, Return a possibly reshaped matrix.          Refer to `numpy.squeeze` for more do, Interpret the input as a matrix.      Unlike `matrix`, `asmatrix` does not make, Return a flattened copy of the matrix.          All `N` elements of the matrix a (+13 more)

### Community 41 - "Community 41"
Cohesion: 0.08
Nodes (41): array_absolute(), array_add(), array_bitwise_and(), array_bitwise_or(), array_bitwise_xor(), array_divmod(), array_float(), array_floor_divide() (+33 more)

### Community 42 - "Community 42"
Cohesion: 0.07
Nodes (29): casting_parser(), casting_parser_full(), casting_parser_same_value(), dimension_from_scalar(), PyArray_AsTypeCopyConverter(), PyArray_AxisConverter(), PyArray_BoolConverter(), PyArray_ByteorderConverter() (+21 more)

### Community 43 - "Community 43"
Cohesion: 0.05
Nodes (1): Module containing non-deprecated functions borrowed from Numeric.

### Community 44 - "Community 44"
Cohesion: 0.07
Nodes (23): array_iter_base_dealloc(), arrayiter_dealloc(), arraymultiter_new(), iter_array(), iter_ass_sub_Bool(), iter_ass_sub_int(), iter_ass_subscript(), iter_richcompare() (+15 more)

### Community 45 - "Community 45"
Cohesion: 0.13
Nodes (40): BigInt_Add(), BigInt_Compare(), BigInt_Copy(), BigInt_DivideWithRemainder_MaxQuotient9(), BigInt_IsEven(), BigInt_IsZero(), BigInt_Multiply(), BigInt_Multiply10() (+32 more)

### Community 47 - "Community 47"
Cohesion: 0.07
Nodes (30): ediff1d(), intersect1d(), _isin(), Set operations for arrays based on sorting.  Notes -----  For floating point arr, Find the union of two arrays.      Return the unique, sorted array of values tha, Find the set difference of two arrays.      Return the unique values in `ar1` th, Unpacks one-element tuples for use as return values, Find the unique elements of an array.      Returns the sorted unique elements of (+22 more)

### Community 48 - "Community 48"
Cohesion: 0.07
Nodes (34): _accumulate(), _arrays_for_stack_dispatcher(), atleast_1d(), atleast_2d(), atleast_3d(), _atleast_nd(), _block(), _block_check_depths_match() (+26 more)

### Community 49 - "Community 49"
Cohesion: 0.08
Nodes (23): concatenateRoutines(), create_name_header(), dumpRoutineNames(), ensure_executable(), F2CError, FortranLibrary, FortranRoutine, getLapackRoutines() (+15 more)

### Community 50 - "Community 50"
Cohesion: 0.08
Nodes (40): _check_version(), descr_to_dtype(), dtype_to_descr(), _filter_header(), header_data_from_array_1_0(), isfileobj(), magic(), open_memmap() (+32 more)

### Community 51 - "Community 51"
Cohesion: 0.05
Nodes (15): angle(), asarray_chkfinite(), bartlett(), _chbevl(), _closest_observation(), _discrete_interpolation_to_boundaries(), _get_gamma_mask(), _i0_1() (+7 more)

### Community 52 - "Community 52"
Cohesion: 0.05
Nodes (6): datetime_common_dtype(), datetime_known_scalar_types(), default_builtin_common_dtype(), python_builtins_are_known_scalar_types(), signed_integers_is_known_scalar_types(), string_known_scalar_types()

### Community 53 - "Community 53"
Cohesion: 0.06
Nodes (33): diag(), diagflat(), eye(), fliplr(), flipud(), histogram2d(), mask_indices(), _min_int() (+25 more)

### Community 54 - "Community 54"
Cohesion: 0.07
Nodes (23): array_from_pyobj(), check_and_fix_dimensions(), dump_attrs(), dump_dims(), f2py_cb_start_call_clock(), f2py_cb_start_clock(), f2py_cb_stop_call_clock(), f2py_cb_stop_clock() (+15 more)

### Community 55 - "Community 55"
Cohesion: 0.08
Nodes (35): _get_bin_edges(), _get_outer_edges(), _hist_bin_auto(), _hist_bin_doane(), _hist_bin_fd(), _hist_bin_rice(), _hist_bin_scott(), _hist_bin_sqrt() (+27 more)

### Community 56 - "Community 56"
Cohesion: 0.07
Nodes (18): argmax(), argmin(), as_pystring(), common_instance(), compare(), _eq_comparison(), init_string_dtype(), init_stringdtype_sorts() (+10 more)

### Community 57 - "Community 57"
Cohesion: 0.07
Nodes (36): _add(), _as_int(), as_series(), _div(), _fit(), _fromroots(), getdomain(), _gridnd() (+28 more)

### Community 58 - "Community 58"
Cohesion: 0.14
Nodes (34): deprecate_integer_datetime_operation(), find_userloop(), linear_search_type_resolver(), linear_search_userloop_type_resolver(), npy_casting_to_py_object(), PyUFunc_AbsoluteTypeResolver(), PyUFunc_AdditionTypeResolver(), PyUFunc_DefaultLegacyInnerLoopSelector() (+26 more)

### Community 59 - "Community 59"
Cohesion: 0.11
Nodes (31): legacy_beta(), legacy_chisquare(), legacy_double(), legacy_exponential(), legacy_f(), legacy_gamma(), legacy_gauss(), legacy_geometric_inversion() (+23 more)

### Community 60 - "Community 60"
Cohesion: 0.11
Nodes (32): _as_pairs(), _get_edges(), _get_linear_ramps(), _get_stats(), pad(), _pad_simple(), The arraypad module contains a group of functions to pad values onto the edges o, Set empty-padded area in given dimension.      Parameters     ----------     pad (+24 more)

### Community 61 - "Community 61"
Cohesion: 0.06
Nodes (23): CClass, diag_indices(), _diag_indices_from(), fill_diagonal(), IndexExpression, ix_(), MGridClass, nd_grid (+15 more)

### Community 62 - "Community 62"
Cohesion: 0.09
Nodes (25): count_boolean_trues(), count_nonzero_bytes_384(), count_nonzero_int(), count_nonzero_u8(), count_zero_bytes_u16(), count_zero_bytes_u8(), _new_argsortlike(), _new_sortlike() (+17 more)

### Community 63 - "Community 63"
Cohesion: 0.09
Nodes (33): _cook_nd_args(), fft(), fft2(), fftn(), hfft(), ifft(), ifft2(), ifftn() (+25 more)

### Community 64 - "Community 64"
Cohesion: 0.07
Nodes (23): apply_along_axis(), array_split(), column_stack(), dsplit(), dstack(), hsplit(), _make_along_axis_idx(), put_along_axis() (+15 more)

### Community 65 - "Community 65"
Cohesion: 0.13
Nodes (36): _assert_finite(), _assert_stacked_square(), cholesky(), _commonType(), _complexType(), cond(), det(), eig() (+28 more)

### Community 66 - "Community 66"
Cohesion: 0.06
Nodes (16): chararray, For each element in `self`, return a copy with the trailing         characters r, For each element in `self`, return True if there are only         decimal charac, chararray(shape, itemsize=1, unicode=False, buffer=None, offset=0,, Return (self + other), that is string concatenation,         element-wise for a, Return the indices that sort the array lexicographically.          For full docu, Returns an array with the number of non-overlapping occurrences of         subst, Calls ``bytes.decode`` element-wise.          See Also         -------- (+8 more)

### Community 67 - "Community 67"
Cohesion: 0.08
Nodes (28): array_function_errmsg_formatter(), array_ufunc_errmsg_formatter(), _copy_fields(), _gcd(), _getfield_is_safe(), _lcm(), _makenames_list(), _newnames() (+20 more)

### Community 68 - "Community 68"
Cohesion: 0.07
Nodes (13): Arrayterator, A buffered iterator for big arrays.  This module solves the problem of iterating, Return a new arrayterator., Return corresponding data., A 1-D flat iterator for Arrayterator objects.          This iterator returns ele, Buffered iterator for big arrays.      `Arrayterator` creates a buffered iterato, The shape of the array to be iterated over.          For an example, see `Arrayt, ``numpy.lib`` is mostly a space for implementing functions that don't belong in (+5 more)

### Community 69 - "Community 69"
Cohesion: 0.06
Nodes (16): is_string_or_list_of_strings(), MaskedIterator, mvoid, Flat iterator object to iterate over masked arrays.      A `MaskedIterator` iter, Return the next value, or raise StopIteration.          Examples         -------, Copies some attributes of obj to self., x.__getitem__(y) <==> x[y]          Return the item described by i, as a masked, Return a flat iterator, or set a flattened version of self to value. (+8 more)

### Community 70 - "Community 70"
Cohesion: 0.06
Nodes (20): make_mask_descr(), _mareconstruct(), _MaskedPrintOption, Private function allowing recursion in _replace_dtype_fields., Construct a dtype description list from a given dtype.      Returns a new dtype, Construct a dtype description list from a given dtype.      Returns a new dtype, Handle the string used to represent missing data in a masked array., Create the masked_print_option object. (+12 more)

### Community 71 - "Community 71"
Cohesion: 0.10
Nodes (29): bmm_einsum(), _compute_size_by_dict(), einsum(), einsum_path(), _find_contraction(), _flop_count(), _greedy_path(), _optimal_path() (+21 more)

### Community 72 - "Community 72"
Cohesion: 0.06
Nodes (33): argmax(), argmin(), argpartition(), argsort(), around(), choose(), clip(), compress() (+25 more)

### Community 73 - "Community 73"
Cohesion: 0.08
Nodes (29): as_array(), as_ctypes(), as_ctypes_type(), _concrete_ndptr, _ctype_from_dtype(), _ctype_from_dtype_scalar(), _ctype_from_dtype_structured(), _ctype_from_dtype_subarray() (+21 more)

### Community 74 - "Community 74"
Cohesion: 0.07
Nodes (16): as_deref(), as_eq(), as_ge(), as_gt(), as_le(), as_lt(), as_ref(), Expr (+8 more)

### Community 75 - "Community 75"
Cohesion: 0.12
Nodes (28): ConverterError, ConverterLockError, Exception raised when an error occurs in a converter for string values., Exception raised when an attempt is made to upgrade a locked converter., _check_nonneg_int(), _ensure_ndmin_ndarray(), _ensure_ndmin_ndarray_check_param(), genfromtxt() (+20 more)

### Community 76 - "Community 76"
Cohesion: 0.09
Nodes (25): build_func_data(), _check_order(), check_td_order(), docstrings, english_upper(), FullTypeDescr, FuncNameSuffix, indent() (+17 more)

### Community 77 - "Community 77"
Cohesion: 0.07
Nodes (13): finfo, _fr0(), _fr1(), iinfo, Machine limits for Float32 and Float64 and (long double) if available..., fix rank-0 --> rank-1, fix rank > 0 --> rank-0, Return the value for tiny, alias of smallest_normal.          Returns         -- (+5 more)

### Community 78 - "Community 78"
Cohesion: 0.08
Nodes (19): Dict of expired attributes that are discontinued since 2.0 release. Each item is, Discrete Fourier Transform ==========================  .. currentmodule:: numpy., hugepage_setup(), _mac_os_check(), NumPy =====  Provides   1. An array object of arbitrary homogeneous items   2. F, # NOTE: It's still under discussion whether these aliases, Quick sanity checks for common bugs caused by environment.         There are som, Quick Sanity check for Mac OS look for accelerate build bugs.         Testing nu (+11 more)

### Community 79 - "Community 79"
Cohesion: 0.10
Nodes (13): cleanComments(), CommentQueue, LenSubsScanner, LineQueue, MyScanner, Replace dlamch_ calls with appropriate macros, Following clapack, we remove ftnlen arguments, which f2c puts after     a char *, removeBuiltinFunctions() (+5 more)

### Community 80 - "Community 80"
Cohesion: 0.09
Nodes (27): arccos(), arcsin(), arctanh(), _fix_int_lt_zero(), _fix_real_abs_gt_1(), _fix_real_lt_zero(), log(), log10() (+19 more)

### Community 81 - "Community 81"
Cohesion: 0.07
Nodes (24): common_type(), _getmaxmin(), imag(), iscomplex(), iscomplexobj(), isreal(), isrealobj(), mintypecode() (+16 more)

### Community 82 - "Community 82"
Cohesion: 0.08
Nodes (13): array_dataptr_get(), array_descr_set(), array_descr_set_internal(), array_imag_get(), array_imag_set(), array_interface_get(), array_protocol_strides_get(), array_real_get() (+5 more)

### Community 83 - "Community 83"
Cohesion: 0.13
Nodes (30): check_mask_for_writemasked_reduction(), intp_abs(), NpyIter_AdvancedNew(), npyiter_allocate_arrays(), npyiter_allocate_transfer_functions(), npyiter_apply_forced_iteration_order(), npyiter_calculate_ndim(), npyiter_casting_to_string() (+22 more)

### Community 84 - "Community 84"
Cohesion: 0.07
Nodes (16): asarray(), Return an array with the elements of `self`         right-justified in a string, Partition each element in `self` around `sep`.          See Also         -------, For each element in `self`, return a copy of the string with         uppercase c, For each element in `self`, return a titlecased version of the         string: w, For each element in `self`, return a copy of the string where         all charac, Return an array with the elements of `self` converted to         uppercase., Return the numeric string left-filled with zeros in a string of         length ` (+8 more)

### Community 85 - "Community 85"
Cohesion: 0.09
Nodes (29): almost(), approx(), assert_almost_equal(), assert_array_almost_equal(), assert_array_approx_equal(), assert_array_compare(), assert_array_equal(), assert_array_less() (+21 more)

### Community 86 - "Community 86"
Cohesion: 0.09
Nodes (12): array_dealloc(), array_might_be_written(), array_new(), array_richcompare(), _clear_array_attributes(), DEPRECATE_silence_error(), PyArray_CheckStrides(), PyArray_FailUnlessWriteable() (+4 more)

### Community 87 - "Community 87"
Cohesion: 0.08
Nodes (25): Enum, ArithOp, as_ne(), _get_parenthesis_kind(), Language, Op, Precedence, Fortran/C symbolic expressions  References: - J3/21-007: Draft Fortran 202x. htt (+17 more)

### Community 88 - "Community 88"
Cohesion: 0.07
Nodes (24): assert_no_warnings(), _assert_no_warnings_context(), assert_raises(), assert_raises_regex(), assert_string_equal(), break_cycles(), decorate_methods(), _Dummy (+16 more)

### Community 89 - "Community 89"
Cohesion: 0.08
Nodes (9): cmp_arg_types(), _free_loop1d_list(), _loop1d_list_free(), PyUFunc_GetDefaultIdentity(), PyUFunc_RegisterLoopForDescr(), PyUFunc_RegisterLoopForType(), _typecharfromnum(), ufunc_get_identity() (+1 more)

### Community 90 - "Community 90"
Cohesion: 0.07
Nodes (3): array_equal(), _dtype_cannot_hold_nan(), True if two arrays have the same shape and elements, False otherwise.      Param

### Community 91 - "Community 91"
Cohesion: 0.16
Nodes (24): acquire_allocator_lock(), allocator_seen(), arena_free(), arena_malloc(), heap_or_arena_allocate(), heap_or_arena_deallocate(), is_short_string(), NpyString_acquire_allocator() (+16 more)

### Community 92 - "Community 92"
Cohesion: 0.09
Nodes (16): _display_as_base(), Various richly-typed exceptions, that also help us deal with string formatting i, A decorator that makes an exception class look like its base.      We use this t, Base class for all ufunc exceptions, Thrown when a ufunc loop cannot be found, Thrown when a binary resolution fails, Thrown when a ufunc input cannot be casted, Thrown when a ufunc output cannot be casted (+8 more)

### Community 93 - "Community 93"
Cohesion: 0.11
Nodes (14): DataSource, DataSource(destpath='.')      A generic data source file (file, http, ftp, ...)., Create a DataSource with a local path at destpath., Test if the filename is a zip file by looking at the file extension., Test if the given mode will open a file for writing., Split zip extension from filename and return filename.          Returns, Return a tuple containing compressed filename variations., Test if path is a net location.  Tests the scheme and netloc. (+6 more)

### Community 94 - "Community 94"
Cohesion: 0.11
Nodes (15): default_calloc(), default_free(), default_malloc(), get_handler_name(), get_handler_version(), indicate_hugepages(), _npy_alloc_cache(), npy_alloc_cache_dim() (+7 more)

### Community 95 - "Community 95"
Cohesion: 0.10
Nodes (13): npy_float_to_half(), npy_half_divmod(), npy_half_eq_nonan(), npy_half_ge(), npy_half_gt(), npy_half_isfinite(), npy_half_isinf(), npy_half_isnan() (+5 more)

### Community 96 - "Community 96"
Cohesion: 0.15
Nodes (24): _aligned_offset(), _byte_order_str(), _construction_repr(), _datetime_metadata_str(), _is_packed(), _isunsized(), _kind_name(), _name_get() (+16 more)

### Community 98 - "Community 98"
Cohesion: 0.09
Nodes (17): as_string(), as_symbol(), as_ternary(), eliminate_quotes(), fromstring(), _FromStringWorker, insert_quotes(), _Pair (+9 more)

### Community 99 - "Community 99"
Cohesion: 0.09
Nodes (17): _decode_line(), flatten_dtype(), has_nested_fields(), _is_bytes_like(), _is_string_like(), LineSplitter, A collection of functions designed to help I/O with ascii files., Object to split a string at a given delimiter or at given places.      Parameter (+9 more)

### Community 100 - "Community 100"
Cohesion: 0.20
Nodes (20): array_assign_boolean_subscript(), array_assign_item(), array_assign_subscript(), array_boolean_subscript(), array_item(), array_item_asarray(), array_subscript(), array_subscript_asarray() (+12 more)

### Community 101 - "Community 101"
Cohesion: 0.17
Nodes (23): compute_min_run_short(), npy_acount_run(), npy_aforce_collapse(), npy_agallop_left(), npy_agallop_right(), npy_amerge_at(), npy_amerge_left(), npy_amerge_right() (+15 more)

### Community 102 - "Community 102"
Cohesion: 0.15
Nodes (23): get_kind(), isarray(), iscomplexarray(), isdouble(), isint1(), isint1array(), isinteger(), islong_long() (+15 more)

### Community 103 - "Community 103"
Cohesion: 0.21
Nodes (20): cb_routsign2map(), cb_sign2map(), common_sign2map(), f2cexpr(), get_elsize(), getarrdims(), getarrdocsign(), getctype() (+12 more)

### Community 104 - "Community 104"
Cohesion: 0.16
Nodes (20): buildmodules(), callcrackfortran(), CombineIncludePaths, dict_append(), f2py_parser(), filter_files(), get_newer_options(), main() (+12 more)

### Community 105 - "Community 105"
Cohesion: 0.09
Nodes (5): get_names(), Collection of utilities to manipulate structured arrays.  Most of these function, Returns the field names of the input datatype as a tuple. Input datatype     mus, Re-pack the fields of a structured array or dtype in memory.      The memory lay, repack_fields()

### Community 106 - "Community 106"
Cohesion: 0.13
Nodes (14): __New_PyArray_Std(), power_of_ten(), PyArray_ArgMax(), _PyArray_ArgMaxWithKeepdims(), PyArray_ArgMin(), _PyArray_ArgMinMaxCommon(), _PyArray_ArgMinWithKeepdims(), PyArray_Conjugate() (+6 more)

### Community 107 - "Community 107"
Cohesion: 0.18
Nodes (15): change_decimal_from_locale_to_dot(), ensure_decimal_point(), ensure_minimum_exponent_length(), fix_ascii_format(), NumPyOS_ascii_ftolf(), NumPyOS_ascii_isalnum(), NumPyOS_ascii_isalpha(), NumPyOS_ascii_isdigit() (+7 more)

### Community 108 - "Community 108"
Cohesion: 0.10
Nodes (19): drop_metadata(), get_include(), _get_indent(), _info(), _makenamedict(), _median_nancheck(), _opt_info(), Determines the leading whitespace that could be removed from all the lines. (+11 more)

### Community 109 - "Community 109"
Cohesion: 0.11
Nodes (19): isdtype(), issctype(), issubclass_(), issubdtype(), issubsctype(), obj2sctype(), _preprocess_dtype(), numerictypes: Define the numeric type objects  This module is designed so "from (+11 more)

### Community 110 - "Community 110"
Cohesion: 0.13
Nodes (14): fortranSourceLines(), getDependencies(), isBlank(), isComment(), isContinuation(), isLabel(), LineIterator, lineType() (+6 more)

### Community 111 - "Community 111"
Cohesion: 0.15
Nodes (19): arr_bincount(), arr_interp(), arr_interp_complex(), arr__monotonicity(), arr_ravel_multi_index(), arr_unravel_index(), astype_anyint(), binary_search_with_guess() (+11 more)

### Community 112 - "Community 112"
Cohesion: 0.12
Nodes (11): c_void_p, _ctypes, _getintp_ctype(), _missing_ctypes, Return the data pointer cast to a particular c-types object.         For example, Return the shape tuple as an array of some other c-types         type. For examp, Return the strides tuple as an array of some other         c-types type. For exa, A pointer to the memory area of the array as a Python integer.         This memo (+3 more)

### Community 113 - "Community 113"
Cohesion: 0.13
Nodes (16): as_strided(), broadcast_arrays(), _broadcast_shape(), broadcast_shapes(), _broadcast_to(), DummyArray, _maybe_view_as_subclass(), Utilities that manipulate strides to achieve desirable effects.  An explanation (+8 more)

### Community 114 - "Community 114"
Cohesion: 0.18
Nodes (13): array_function_method_impl(), array__get_implementing_args(), array_implement_c_array_function_creation(), call_array_function(), dispatcher_vectorcall(), fix_name_if_typeerror(), get_args_and_kwargs(), get_array_function() (+5 more)

### Community 115 - "Community 115"
Cohesion: 0.13
Nodes (19): formatargspec(), formatargvalues(), getargs(), getargspec(), getargvalues(), iscode(), isfunction(), ismethod() (+11 more)

### Community 116 - "Community 116"
Cohesion: 0.16
Nodes (16): ABCPolyBase, Chebyshev, A Chebyshev series class.      The Chebyshev class provides the standard Python, HermiteE, A HermiteE series class.      The HermiteE class provides the standard Python nu, Hermite, A Hermite series class.      The Hermite class provides the standard Python nume, A sub-package for efficiently dealing with polynomials.  Within the documentatio (+8 more)

### Community 117 - "Community 117"
Cohesion: 0.11
Nodes (20): average(), corrcoef(), cov(), _get_gamma(), _get_indexes(), _lerp(), percentile(), quantile() (+12 more)

### Community 118 - "Community 118"
Cohesion: 0.14
Nodes (14): _calculate_shapes(), _create_arrays(), _parse_input_dimensions(), Incrementally check and update core dimension sizes for a single argument., Parse broadcast and core dimensions for vectorize with a signature.      Argumen, Helper for calculating broadcast shapes with core dimensions., Helper for creating output arrays in vectorize., vectorize(pyfunc=np._NoValue, otypes=None, doc=None, excluded=None,     cache=Fa (+6 more)

### Community 119 - "Community 119"
Cohesion: 0.14
Nodes (8): Factory class for function transforming a string into another object     (int, f, Returns the dtype of the input variable., Returns the type of the dtype of the input variable., Returns dtype for datetime64 and type of dtype otherwise., Upgrade the mapper of a StringConverter by adding a new function and         its, Find the best converter for a given string, and return the result.          The, Set StringConverter attributes directly.          Parameters         ----------, StringConverter

### Community 120 - "Community 120"
Cohesion: 0.13
Nodes (5): poly1d, polyadd(), polymul(), Find the sum of two polynomials.      .. note::        This forms part of the ol, Find the product of two polynomials.      .. note::        This forms part of th

### Community 121 - "Community 121"
Cohesion: 0.21
Nodes (19): rk_altfill(), rk_devfill(), rk_double(), rk_fill(), rk_gauss(), rk_hash(), rk_interval(), rk_long() (+11 more)

### Community 122 - "Community 122"
Cohesion: 0.22
Nodes (19): _discover_array_parameters(), discover_dtype_from_pyobject(), find_descriptor_from_array(), find_scalar_descriptor(), handle_promotion(), handle_scalar(), npy_cast_raw_scalar_item(), npy_discover_dtype_from_pytype() (+11 more)

### Community 123 - "Community 123"
Cohesion: 0.14
Nodes (10): fields_traverse_data_clone(), fields_traverse_data_free(), get_clear_function(), get_fields_traverse_function(), get_subarray_traverse_func(), npy_get_clear_void_and_legacy_user_dtype_loop(), npy_get_zerofill_void_and_legacy_user_dtype_loop(), PyArray_GetClearFunction() (+2 more)

### Community 124 - "Community 124"
Cohesion: 0.17
Nodes (17): _attempt_nocopy_reshape(), _fix_unknown_dimension(), PyArray_CreateMultiSortedStridePerm(), PyArray_CreateSortedStridePerm(), PyArray_Flatten(), PyArray_MatrixTranspose(), PyArray_Newshape(), PyArray_Ravel() (+9 more)

### Community 125 - "Community 125"
Cohesion: 0.12
Nodes (6): _get_argpartition_func(), *
get_argpartition_func(int type, NPY_SELECTKIND which)(), _get_partition_func(), *
get_partition_func(int type, NPY_SELECTKIND which)(), introselect_(), store_pivot()

### Community 126 - "Community 126"
Cohesion: 0.11
Nodes (15): array_equiv(), binary_repr(), full(), identity(), ones(), outer(), Return a new array of given shape and type, filled with ones.      Parameters, Return the binary representation of the input number as a string.      For negat (+7 more)

### Community 127 - "Community 127"
Cohesion: 0.12
Nodes (14): _check_mode(), _FileOpeners, open(), A file interface for handling local and remote data files.  The goal of datasour, Return the keys of currently supported file openers.          Parameters, Open `path` with `mode` and return the file object.      If ``path`` is a URL, i, # TODO: Doesn't handle compressed files!, # TODO:  This should be more robust.  Handles case where path includes (+6 more)

### Community 128 - "Community 128"
Cohesion: 0.11
Nodes (4): _nan_mask(), Functions that ignore NaN.  Functions ---------  - `nanmin` -- minimum non-NaN v, # TODO: What to do when arr1d = [1, np.nan] and weights = [0, 1]?, Parameters     ----------     a : array-like         Input array with at least 1

### Community 129 - "Community 129"
Cohesion: 0.16
Nodes (14): arrayflags_aligned_set(), arrayflags_farray_get(), arrayflags_fnc_get(), arrayflags_forc_get(), arrayflags_getitem(), arrayflags_new(), arrayflags_print(), arrayflags_setitem() (+6 more)

### Community 130 - "Community 130"
Cohesion: 0.22
Nodes (6): coerce_text(), fill_command(), get_file_template(), paste_script_template_renderer(), sub(), Template

### Community 131 - "Community 131"
Cohesion: 0.23
Nodes (16): find_position(), isolate_expression(), lex(), parse(), parse_cond(), parse_def(), parse_default(), parse_expr() (+8 more)

### Community 132 - "Community 132"
Cohesion: 0.17
Nodes (13): *
add_and_return_legacy_wrapping_ufunc_loop(PyUFuncObject *ufunc,
        PyArray_DTypeMeta *operation_dtypes[], int ignore_duplicate)(), call_promoter_and_recurse(), install_logical_ufunc_promoter(), legacy_promote_using_legacy_type_resolver(), _make_new_typetup(), promote_and_get_info_and_ufuncimpl(), *
promote_and_get_ufuncimpl(PyUFuncObject *ufunc,
        PyArrayObject *const ops[],
        PyArray_DTypeMeta *signature[],
        PyArray_DTypeMeta *op_dtypes[],
        npy_bool force_legacy_promotion,
        npy_bool promoting_pyscalars,
        npy_bool ensure_reduce_compatible)(), PyUFunc_AddLoop() (+5 more)

### Community 133 - "Community 133"
Cohesion: 0.12
Nodes (11): _extendLine(), _extendLine_pretty(), _get_legacy_print_mode(), _object_format(), Array printing function  $Id: arrayprint.py,v 1.9 2005/09/13 13:58:44 teoliphant, # TODO: Custom repr for user DTypes, logic should likely move., Return the legacy print mode as an int., Object arrays containing lists should be printed unambiguously (+3 more)

### Community 134 - "Community 134"
Cohesion: 0.11
Nodes (13): array(), equal(), not_equal(), partition(), This module contains a set of functions for vectorized string operations and met, Create a `~numpy.char.chararray`.      .. deprecated:: 2.5        ``chararray``, Partition each element in `a` around `sep`.      Calls :meth:`str.partition` ele, Partition (split) each element around the right-most separator.      Calls :meth (+5 more)

### Community 135 - "Community 135"
Cohesion: 0.13
Nodes (6): _count_reduce_items(), _mean(), Array methods which are called by both the C-code for the method and the Python, # TODO: Optimize case when `where` is broadcast along a non-reduction, _std(), _var()

### Community 136 - "Community 136"
Cohesion: 0.11
Nodes (16): argwhere(), base_repr(), flatnonzero(), full_like(), isfortran(), ones_like(), Return a string representation of a number in the given base system.      Parame, Return an array of ones with the same shape and type as a given array.      Para (+8 more)

### Community 137 - "Community 137"
Cohesion: 0.12
Nodes (11): _PreprocessDTypeError, Exception, looper, Helper for looping over sequences, particular in templates.  Often in a loop in, Helper for looping (particularly in templates)      Use this like::          for, A small templating language  This implements a small templating language.  This, Lex a string into chunks:          >>> lex('hey')         ['hey']         >>> le, Exception raised while parsing a template (+3 more)

### Community 138 - "Community 138"
Cohesion: 0.20
Nodes (16): as_complex(), as_factors(), as_integer(), as_real(), as_term_coeff(), as_terms(), normalize(), OpError (+8 more)

### Community 139 - "Community 139"
Cohesion: 0.11
Nodes (16): asarray(), flatten_mask(), isMaskedArray(), masked_object(), put(), Returns a completely flattened version of the mask, where nested fields     are, Mask the array `x` where the data are exactly equal to value.      This function, Return the indices of unmasked elements that are not zero.          Returns a tu (+8 more)

### Community 140 - "Community 140"
Cohesion: 0.24
Nodes (17): _append_char(), _append_field_name(), _append_str(), array_getbuffer(), _buffer_format_string(), _buffer_get_info(), _buffer_info_cmp(), _buffer_info_free() (+9 more)

### Community 141 - "Community 141"
Cohesion: 0.15
Nodes (8): array_dlpack(), array_dlpack_device(), array_get_dl_device(), create_dlpack_capsule(), dlpack_dtype_registry_lookup(), dlpack_export_registry_lookup(), fill_dl_tensor_information(), from_dlpack()

### Community 142 - "Community 142"
Cohesion: 0.11
Nodes (1): These tests are based on the doctests from `numpy/lib/recfunctions.py`.

### Community 143 - "Community 143"
Cohesion: 0.12
Nodes (3): loop_pos, Returns true if this item is the start of a new group,         where groups mean, Returns true if this item is the end of a new group,         where groups mean t

### Community 144 - "Community 144"
Cohesion: 0.11
Nodes (10): _NestedSequence, A module containing the `_NestedSequence` protocol., A protocol for representing nested sequences.      Warning     -------     `_Nes, Implement ``len(self)``., Implement ``self[x]``., Implement ``x in self``., Implement ``iter(self)``., Implement ``reversed(self)``. (+2 more)

### Community 145 - "Community 145"
Cohesion: 0.12
Nodes (2): byte_to_true(), simd_logical_or_u8()

### Community 146 - "Community 146"
Cohesion: 0.13
Nodes (6): BoolFormat, DatetimeFormat, _get_formatdict(), IntegerFormat, TimedeltaFormat, _TimelikeFormat

### Community 147 - "Community 147"
Cohesion: 0.15
Nodes (9): Repository(baseurl, destpath='.')      A data repository where multiple DataSour, Create a Repository with a shared url or directory of baseurl., Return complete path for path.  Prepends baseurl if necessary., Extend DataSource method to prepend baseurl to ``path``., Return absolute path of file in the Repository directory.          If `path` is, Test if path exists prepending Repository base URL to path.          Test if `pa, Open and return file-like object prepending Repository base URL.          If `pa, List files in the source Repository.          Returns         -------         fi (+1 more)

### Community 148 - "Community 148"
Cohesion: 0.18
Nodes (11): ConversionWarning, Warning issued when a string converter has a problem.      Notes     -----     I, BagObj, Create a ZipFile.      Allows for Zip64, and the `file` argument can accept file, D.items() returns a set-like object providing a view on the items, D.keys() returns a set-like object providing a view on the keys, BagObj(obj)      Convert attribute look-ups to getitems on the object passed in., Save several arrays into a single file in uncompressed ``.npz`` format.      Pro (+3 more)

### Community 149 - "Community 149"
Cohesion: 0.14
Nodes (16): _binary_method(), _disables_array_ufunc(), _inplace_binary_method(), NDArrayOperatorsMixin, _numeric_methods(), Mixin classes for custom array types that don't inherit from ndarray., True when __array_ufunc__ is set to None., # TODO: handle the optional third argument for __pow__? (+8 more)

### Community 150 - "Community 150"
Cohesion: 0.13
Nodes (16): empty(), eye(), identity(), ones(), rand(), randn(), Return a matrix of given shape and type, filled with zeros.      Parameters, Returns the square identity matrix of given size.      Parameters     ---------- (+8 more)

### Community 151 - "Community 151"
Cohesion: 0.15
Nodes (6): fill_arraymethod_from_slots(), is_contiguous(), npy_default_get_strided_loop(), PyArrayMethod_FromSpec(), PyArrayMethod_FromSpec_int(), validate_spec()

### Community 152 - "Community 152"
Cohesion: 0.16
Nodes (11): _add_docstring(), add_newdoc(), geomspace(), linspace(), logspace(), _needs_add_docstring(), Return numbers spaced evenly on a log scale.      In linear space, the sequence, Return evenly spaced numbers over a specified interval.      Returns `num` evenl (+3 more)

### Community 153 - "Community 153"
Cohesion: 0.13
Nodes (1): This module contains a set of functions for vectorized string operations.

### Community 154 - "Community 154"
Cohesion: 0.14
Nodes (6): fromregex(), load(), NpzFile, r"""     Construct an array from a text file, using regular expression parsing., D.get(k,[,d]) returns D[k] if k in D, else d.  d defaults to None., Load arrays or pickled objects from ``.npy``, ``.npz`` or pickled files.      ..

### Community 155 - "Community 155"
Cohesion: 0.13
Nodes (6): polyfit(), _raise_power(), Functions to operate on polynomials., Return the roots of a polynomial with coefficients given in p.      .. note::, Least squares polynomial fit.      .. note::        This forms part of the old p, roots()

### Community 156 - "Community 156"
Cohesion: 0.17
Nodes (8): _check_compatibility_with_new_dtype(), convert_shape_to_string(), dot_alignment_error(), _get_subarray_base_and_dimensions(), _get_subarray_ndim(), _may_have_objects(), _unpack_field(), _unpack_field_index()

### Community 157 - "Community 157"
Cohesion: 0.17
Nodes (8): assert_warns(), _assert_warns_context(), Fail unless the given callable throws the specified warning.      A warning of c, Context manager and decorator doing much the same as     ``warnings.catch_warnin, Add a new suppressing filter or apply it if the state is entered.          Param, Append a new recording filter or apply it if the state is entered.          All, Function decorator to apply certain suppressions to a whole         function., suppress_warnings

### Community 158 - "Community 158"
Cohesion: 0.14
Nodes (10): Protocol, TypedDict, A protocol class representing `~class.__array_function__`., # NOTE: This includes `builtins.bool`, but not `numpy.bool`., _SupportsArray, _SupportsArrayFunc, _DTypeDict, _HasDType (+2 more)

### Community 159 - "Community 159"
Cohesion: 0.17
Nodes (11): ============================ Typing (:mod:`numpy.typing`) ======================, # NOTE: The API section will be appended with additional entries, _128Bit, _16Bit, _32Bit, _64Bit, _8Bit, _96Bit (+3 more)

### Community 160 - "Community 160"
Cohesion: 0.20
Nodes (16): _check_axis_support(), check_for_trivial_loop(), _check_keepdims_support(), execute_ufunc_loop(), _get_coredim_sizes(), _has_output_coredims(), _initialize_variable_parts(), _parse_axes_arg() (+8 more)

### Community 161 - "Community 161"
Cohesion: 0.13
Nodes (14): getbufsize(), geterr(), geterrcall(), Functions for changing global ufunc configuration  This provides helpers which w, Get the current way of handling floating-point errors.      Returns     -------, Set the size of the buffer used in ufuncs.      .. versionchanged:: 2.0, Return the size of the buffer used in ufuncs.      Returns     -------     getbu, Set how floating-point errors are handled.      Note that operations on integer (+6 more)

### Community 162 - "Community 162"
Cohesion: 0.14
Nodes (2): pow_zi(), z_div()

### Community 163 - "Community 163"
Cohesion: 0.15
Nodes (4): check_object(), get_lapack_lite_state(), lapack_lite_clear(), lapack_lite_free()

### Community 164 - "Community 164"
Cohesion: 0.28
Nodes (13): apply_business_day_count(), apply_business_day_offset(), apply_business_day_roll(), array_busday_count(), array_busday_offset(), array_is_busday(), business_day_count(), business_day_offset() (+5 more)

### Community 165 - "Community 165"
Cohesion: 0.20
Nodes (14): build(), build_and_import_extension(), _c_compile(), compile_extension_module(), _convert_str_to_file(), get_so_suffix(), _make_methods(), _make_source() (+6 more)

### Community 166 - "Community 166"
Cohesion: 0.16
Nodes (15): convert_ufunc_arguments(), _keepdims_converter(), _parse_axis(), PyUFunc_Accumulate(), PyUFunc_GenericReduction(), PyUFunc_Reduce(), PyUFunc_Reduceat(), reducelike_promote_and_resolve() (+7 more)

### Community 167 - "Community 167"
Cohesion: 0.14
Nodes (8): __array_namespace_info__, Array API Inspection namespace  This is the namespace for inspection functions a, The default device used for new NumPy arrays.          For NumPy, this always re, The default data types used for new NumPy arrays.          For NumPy, this alway, The array API data types supported by NumPy.          Note that this function on, Get the array API inspection namespace for NumPy.      The array API inspection, The devices supported by NumPy.          For NumPy, this always returns ``('cpu', Return a dictionary of array API library capabilities.          The resulting di

### Community 168 - "Community 168"
Cohesion: 0.18
Nodes (13): check_api_version(), get_api_versions(), main(), MismatchCAPIError, Return current C API checksum and the recorded checksum.      Return current C A, Emits a MismatchCAPIWarning if the C API version needs updating., matrix_rank(), outer() (+5 more)

### Community 169 - "Community 169"
Cohesion: 0.14
Nodes (10): ComplexWarning, RankWarning, The warning raised when casting a complex dtype to a real dtype.      As impleme, Matrix rank warning.      Issued by polynomial functions when the design matrix, A one-dimensional polynomial class.      .. note::        This forms part of the, The polynomial coefficients, The name of the polynomial variable, The order or degree of the polynomial (+2 more)

### Community 170 - "Community 170"
Cohesion: 0.34
Nodes (13): dlamc1_(), dlamc2_(), dlamc3_(), dlamc4_(), dlamc5_(), dlamch_(), lsame_(), slamc1_() (+5 more)

### Community 171 - "Community 171"
Cohesion: 0.14
Nodes (14): nanargmax(), nanargmin(), nancumprod(), nancumsum(), nanprod(), nansum(), Return the indices of the minimum values in the specified axis ignoring     NaNs, Return the indices of the maximum values in the specified axis ignoring     NaNs (+6 more)

### Community 172 - "Community 172"
Cohesion: 0.18
Nodes (14): _fix_defaults(), _fix_output(), _get_fieldspec(), join_by(), _keep_fields(), Superposes arrays fields by fields      Parameters     ----------     arrays : a, Join arrays `r1` and `r2` on key `key`.      The key should be either a string o, Join arrays `r1` and `r2` on keys.     Alternative to join_by, that always retur (+6 more)

### Community 173 - "Community 173"
Cohesion: 0.14
Nodes (14): _assert_stacked_2d(), _is_empty_2d(), matmul(), pinv(), qr(), QRResult, Compute the (Moore-Penrose) pseudo-inverse of a matrix.      Calculate the gener, Transpose each matrix in a stack of matrices.      Unlike np.transpose, this onl (+6 more)

### Community 174 - "Community 174"
Cohesion: 0.15
Nodes (2): initialize_abstract_dtypes(), make_raw_dtype()

### Community 175 - "Community 175"
Cohesion: 0.25
Nodes (10): _check_ufunc_fperr(), extobj_get_extobj_dict(), extobj_make_extobj(), _extract_pyvals(), fetch_curr_extobj_state(), _get_bufsize_errmask(), init_extobj(), make_extobj_capsule() (+2 more)

### Community 176 - "Community 176"
Cohesion: 0.24
Nodes (10): main(), parse_loop_header(), parse_string(), parse_structure(), parse_values(), process_file(), process_str(), The returned line number is from the beginning of the string, starting     at ze (+2 more)

### Community 177 - "Community 177"
Cohesion: 0.18
Nodes (8): find_functions(), Function, get_api_functions(), main(), ParseError, Scan the file, looking for tagged functions.      Assuming ``tag=='API'``, a tag, Parse source files to get functions tagged by the given tag., remove_whitespace()

### Community 178 - "Community 178"
Cohesion: 0.15
Nodes (7): check_fpu_mode(), pytest_itemcollected(), Pytest configuration and fixtures for the Numpy test suite., Check FPU precision mode was not changed during test collection.      The clumsy, Check FPU precision mode was not changed during the test., Filter out the wall of DeprecationWarnings., warnings_errors_and_rng()

### Community 179 - "Community 179"
Cohesion: 0.22
Nodes (7): _add_trailing_padding(), _dtype_from_pep3118(), _fix_names(), _prod(), Replace names which are None with the next unused f%d name, Inject the specified number of padding bytes at the end of a dtype, _Stream

### Community 180 - "Community 180"
Cohesion: 0.18
Nodes (13): getcallprotoargument(), getcallstatement(), getmultilineblock(), getpymethoddef(), getusercode(), getusercode1(), hascallstatement(), isarrayofstrings() (+5 more)

### Community 181 - "Community 181"
Cohesion: 0.17
Nodes (13): hasnote(), hasresultnote(), isfunction(), isfunction_wrap(), isintent_c(), islogical(), islogicalfunction(), islong_double() (+5 more)

### Community 182 - "Community 182"
Cohesion: 0.17
Nodes (13): append(), diff(), gradient(), Return the gradient of an N-dimensional array.      The gradient is computed usi, Calculate the n-th discrete difference along the given axis.      The first diff, r"""     Unwrap by taking the complement of large deltas with respect to the per, r"""     Integrate along the given axis using the composite trapezoidal rule., Append values to the end of an array.      Parameters     ----------     arr : a (+5 more)

### Community 184 - "Community 184"
Cohesion: 0.19
Nodes (2): MaskedConstant, Override of MaskedArray's __reduce__.

### Community 185 - "Community 185"
Cohesion: 0.29
Nodes (9): _descr_from_subtype(), PyArray_CastScalarDirect(), PyArray_CastScalarToCtype(), PyArray_DescrFromScalar(), PyArray_DescrFromTypeObject(), PyArray_FromScalar(), PyArray_Scalar(), PyArray_ScalarAsCtype() (+1 more)

### Community 186 - "Community 186"
Cohesion: 0.19
Nodes (4): empty_array_like(), unique_numeric(), unique_string(), unique_vstring()

### Community 187 - "Community 187"
Cohesion: 0.23
Nodes (8): _next(), npy_clear_floatstatus(), npy_clear_floatstatus_barrier(), npy_get_floatstatus(), npy_get_floatstatus_barrier(), _npy_spacing(), npy_spacingf(), npy_spacingl()

### Community 188 - "Community 188"
Cohesion: 0.24
Nodes (9): call_converter_function(), double_from_ucs4(), npy_to_cdouble(), npy_to_cfloat(), npy_to_double(), npy_to_float(), npy_to_generic(), npy_to_generic_with_converter() (+1 more)

### Community 189 - "Community 189"
Cohesion: 0.18
Nodes (7): check_api_dict(), Get API information encoded in C files.  See ``find_function`` for how functions, Write data to filename     Only write changed data to avoid updating timestamps, Check that an api dict is valid (does not use the same index twice)     and remo, skip_brackets(), split_arguments(), write_file()

### Community 190 - "Community 190"
Cohesion: 0.32
Nodes (10): diophantine_dfs(), diophantine_precompute(), diophantine_simplify(), euclid(), get_array_memory_extents(), offset_bounds_from_strides(), solve_diophantine(), solve_may_have_internal_overlap() (+2 more)

### Community 191 - "Community 191"
Cohesion: 0.17
Nodes (12): _array2string(), _formatArray(), _get_format_function(), _leading_trailing(), _make_options_dict(), Set printing options.      These options determine the way floating point number, Keep only the N-D corners (leading and trailing edges) of an array.      Should, find the right formatting function for the dtype_ (+4 more)

### Community 192 - "Community 192"
Cohesion: 0.18
Nodes (6): Formatter for structured np.void objects.      This does not work on structured, This is a second way to initialize StructuredVoidFormat,         using the raw d, Implements the repr for structured-void scalars. It is called from the     scala, StructuredVoidFormat, SubArrayFormat, _void_scalar_to_string()

### Community 193 - "Community 193"
Cohesion: 0.18
Nodes (10): array_function_dispatch(), array_function_from_dispatcher(), finalize_array_function_like(), get_array_function_like_doc(), Implementation of __array_function__ overrides from NEP-18., Decorator for adding dispatch with the __array_function__ protocol.      See NEP, Like array_function_dispatcher, but with function arguments flipped., Verify that a dispatcher function has the right signature. (+2 more)

### Community 194 - "Community 194"
Cohesion: 0.17
Nodes (12): _clean_args(), encode(), Helper function for delegating arguments to Python string     functions.      Ma, For each element in `a`, return a list of the words in the     string, using `se, For each element in `a`, return a list of the words in the     string, using `se, For each element in `a`, return a list of the lines in the     element, breaking, For each element in `a`, return a copy of the string where all     characters oc, Calls :meth:`str.encode` element-wise.      The set of available codecs comes fr (+4 more)

### Community 195 - "Community 195"
Cohesion: 0.30
Nodes (11): conv(), expand_sub(), find_and_remove_repl_patterns(), find_repl_patterns(), parse_structure(), process_file(), process_str(), Obtain a unique key given a dictionary. (+3 more)

### Community 196 - "Community 196"
Cohesion: 0.27
Nodes (7): add_gufuncs(), copy_input(), copy_output(), fft_loop(), irfft_loop(), _pocketfft_umath_exec(), rfft_impl()

### Community 197 - "Community 197"
Cohesion: 0.20
Nodes (3): ieeeck_(), ilaenv_(), iparmq_()

### Community 198 - "Community 198"
Cohesion: 0.23
Nodes (7): decide_view_dtype_path(), get_optional_set_dtype_and_dtype(), npy_fallocate(), PyArray_ToFile(), PyArray_ToList(), PyArray_View(), recursive_tolist()

### Community 199 - "Community 199"
Cohesion: 0.32
Nodes (11): _any_labels_are_negative(), get_combined_dims_view(), get_single_op_view(), parse_operand_subscripts(), parse_output_subscripts(), prepare_op_axes(), *
PyArray_EinsteinSum(char *subscripts, npy_intp nop,
                    PyArrayObject **op_in,
                    PyArray_Descr *dtype,
                    NPY_ORDER order, NPY_CASTING casting,
                    PyArrayObject *out)(), unbuffered_loop_nop1_ndim2() (+3 more)

### Community 200 - "Community 200"
Cohesion: 0.23
Nodes (6): _append_new(), _PyArray_LegacyDescrNewFromPrototype(), PyArray_RegisterCanCast(), PyArray_RegisterCastFunc(), PyArray_RegisterDataType(), _warn_if_cast_exists_already()

### Community 201 - "Community 201"
Cohesion: 0.18
Nodes (12): assert_allclose(), assert_approx_equal(), assert_array_compare(), assert_array_equal(), assert_array_less(), assert_equal(), build_err_msg(), Raises an AssertionError if two array_like objects are not equal.      Given two (+4 more)

### Community 202 - "Community 202"
Cohesion: 0.18
Nodes (1): NAType

### Community 203 - "Community 203"
Cohesion: 0.23
Nodes (9): _cmpkey(), InvalidVersion, _legacy_cmpkey(), _parse_letter_version(), _parse_local_version(), _parse_version_parts(), Utility to compare pep440 compatible version strings.  The LooseVersion and Stri, An invalid version was found, users should refer to PEP 440. (+1 more)

### Community 204 - "Community 204"
Cohesion: 0.18
Nodes (11): amax(), amin(), max(), min(), Sum of array elements over a given axis.      Parameters     ----------     a :, Return the maximum of an array or maximum along an axis.      Parameters     ---, Return the maximum of an array or maximum along an axis.      `amax` is an alias, Return the minimum of an array or minimum along an axis.      Parameters     --- (+3 more)

### Community 205 - "Community 205"
Cohesion: 0.20
Nodes (6): as_number(), as_numer_denom(), Return expression as numer-denom pair., Return a string representation of Expr., Return a, b such that a * symbol + b == self.          If self is not linear wit, Return object as INTEGER or REAL constant.

### Community 206 - "Community 206"
Cohesion: 0.18
Nodes (9): fftfreq(), fftshift(), ifftshift(), Discrete Fourier Transforms - _helper.py, Return the Discrete Fourier Transform sample frequencies.      The returned floa, Return the Discrete Fourier Transform sample frequencies     (for usage with rff, Shift the zero-frequency component to the center of the spectrum.      This func, The inverse of `fftshift`. Although identical for even-length `x`, the     funct (+1 more)

### Community 207 - "Community 207"
Cohesion: 0.18
Nodes (6): _CopyMode, _NoValueType, Module defining global singleton classes.  This module raises a RuntimeError if, Special keyword value.      The instance of this class may be used as the defaul, An enumeration for the copy modes supported     by numpy.copy() and numpy.array(, _SignatureDescriptor

### Community 208 - "Community 208"
Cohesion: 0.20
Nodes (2): array_converter_wrap(), find_wrap()

### Community 209 - "Community 209"
Cohesion: 0.18
Nodes (1): Object

### Community 210 - "Community 210"
Cohesion: 0.18
Nodes (4): Typing tests for `numpy._core._ufunc_config`., Write1, Write2, Write3

### Community 211 - "Community 211"
Cohesion: 0.25
Nodes (5): num_codepoints_for_utf8_bytes(), num_utf8_bytes_for_codepoint(), utf8_buffer_size(), utf8_decode(), utf8_size()

### Community 212 - "Community 212"
Cohesion: 0.25
Nodes (6): add_dtype_loops(), comp_name(), get_min_max(), get_value_range(), patch_cached_int_loop(), resolve_descriptors_with_scalars()

### Community 213 - "Community 213"
Cohesion: 0.24
Nodes (3): FunctionApi, Wrap a definition behind a version guard, _repl()

### Community 214 - "Community 214"
Cohesion: 0.29
Nodes (5): npy__cpu_baseline_fid(), npy__cpu_check_env(), npy__cpu_dispatch_fid(), npy_cpu_init(), npy__cpu_validate_baseline()

### Community 215 - "Community 215"
Cohesion: 0.36
Nodes (7): find_item(), find_item_buckets(), identity_list_hash(), PyArrayIdentityHash_GetItem(), PyArrayIdentityHash_SetItemDefault(), PyArrayIdentityHash_SetItemDefaultLockHeld(), _resize_if_necessary()

### Community 216 - "Community 216"
Cohesion: 0.29
Nodes (8): dtype_from_ctypes_type(), _from_ctypes_array(), _from_ctypes_scalar(), _from_ctypes_structure(), _from_ctypes_union(), Conversion from ctypes to dtype.  In an ideal world, we could achieve this throu, Construct a dtype object from a ctypes type, Return the dtype type with endianness included if it's the case

### Community 217 - "Community 217"
Cohesion: 0.20
Nodes (10): decode(), _get_num_chars(), _join(), mod(), Helper function that returns the number of characters per field in     a string, Helper function to cast a result back into an array     with the appropriate dty, Return a string which is the concatenation of the strings in the     sequence `s, Return (a % i), that is pre-Python 2.6 string formatting     (interpolation), el (+2 more)

### Community 218 - "Community 218"
Cohesion: 0.22
Nodes (7): Visible deprecation warning.      By default, python will not show deprecation w, VisibleDeprecationWarning, get_include(), Fortran to Python Interface Generator.  Copyright 1999 -- 2011 Pearu Peterson al, Return the directory that contains the ``fortranobject.c`` and ``.h`` files., ExprWarning, UserWarning

### Community 219 - "Community 219"
Cohesion: 0.27
Nodes (4): as_apply(), as_expr(), Return object as APPLY expression (function call, constructor, etc.), Convert non-Expr objects to Expr objects.

### Community 220 - "Community 220"
Cohesion: 0.24
Nodes (7): easy_dtype(), NameValidator, Object to validate a list of strings to use as field names.      The strings are, Validate a list of strings as field names for a structured array.          Param, Convenience function to create a `np.dtype` object.      The function processes, Save an array to a text file.      Parameters     ----------     fname : filenam, savetxt()

### Community 221 - "Community 221"
Cohesion: 0.20
Nodes (10): apply_along_fields(), _common_stride(), _get_fields_and_offsets(), Converts an n-D unstructured array into an (n-1)-D structured array.      The la, Apply function 'func' as a reduction across fields of a structured array.      T, Returns a flat list of (dtype, count, offset) tuples of all the     scalar field, Returns the stride between the fields, or None if the stride is not     constant, Converts an n-D structured array into an (n+1)-D unstructured array.      The ne (+2 more)

### Community 222 - "Community 222"
Cohesion: 0.22
Nodes (2): busdaycalendar_init(), normalize_holidays_list()

### Community 223 - "Community 223"
Cohesion: 0.29
Nodes (8): _fill_with_none(), PyArray_ClearArray(), PyArray_ClearBuffer(), PyArray_INCREF(), PyArray_Item_INCREF(), PyArray_Item_XDECREF(), PyArray_SetObjectsToNone(), PyArray_XDECREF()

### Community 225 - "Community 225"
Cohesion: 0.20
Nodes (9): allows_array_function_override(), allows_array_ufunc_override(), get_overridable_numpy_array_functions(), get_overridable_numpy_ufuncs(), Tools for testing implementations of __array_function__ and ufunc overrides, List all numpy ufuncs overridable via `__array_ufunc__`      Parameters     ----, Determine if a function can be overridden via `__array_ufunc__`      Parameters, List all numpy functions overridable via `__array_function__`      Parameters (+1 more)

### Community 226 - "Community 226"
Cohesion: 0.20
Nodes (5): CommaDecimalPointLocale, find_comma_decimal_point_locale(), Provide class for testing in French locale, See if platform has a decimal point as comma locale.      Find a locale that use, Sets LC_NUMERIC to a locale with comma as decimal point.      Classes derived fr

### Community 228 - "Community 228"
Cohesion: 0.27
Nodes (10): _get_end_of_name(), _get_size(), _is_alnum_underscore(), _is_alpha_underscore(), _is_same_name(), _next_non_white_space(), _parse_signature(), PyUFunc_FromFuncAndData() (+2 more)

### Community 229 - "Community 229"
Cohesion: 0.20
Nodes (1): Infinity

### Community 230 - "Community 230"
Cohesion: 0.20
Nodes (3): LegacyVersion, parse(), Parse the given version string and return either a :class:`Version` object     o

### Community 231 - "Community 231"
Cohesion: 0.20
Nodes (1): NegativeInfinity

### Community 232 - "Community 232"
Cohesion: 0.25
Nodes (4): ComplexFloatingFormat, FloatingFormat, Formatter for subtypes of np.complexfloating, Formatter for subtypes of np.floating

### Community 233 - "Community 233"
Cohesion: 0.25
Nodes (3): memmap, Create a memory-map to an array stored in a *binary* file on disk.      Memory-m, Write any changes in the array to the file on disk.          For further informa

### Community 234 - "Community 234"
Cohesion: 0.22
Nodes (7): fix(), isneginf(), isposinf(), Module of functions that are like ufuncs in acting on arrays and optionally stor, Test element-wise for negative infinity, return result as bool array.      Param, Round to nearest integer towards zero.      .. deprecated:: 2.5         `numpy.f, Test element-wise for positive infinity, return result as bool array.      Param

### Community 235 - "Community 235"
Cohesion: 0.22
Nodes (9): _clear_cast_info_after_get_loop_failure(), define_cast_for_descrs(), get_legacy_dtype_cast_function(), get_wrapped_legacy_cast_function(), init_cast_info(), _multistep_cast_auxdata_clone(), _multistep_cast_auxdata_clone_int(), wrap_aligned_transferfunction() (+1 more)

### Community 236 - "Community 236"
Cohesion: 0.42
Nodes (8): _array_descr_builtin(), _array_descr_walk(), _array_descr_walk_fields(), _array_descr_walk_subarray(), _is_array_descr_builtin(), _normalize_byteorder(), PyArray_DescrHash(), _PyArray_DescrHashImp()

### Community 237 - "Community 237"
Cohesion: 0.44
Nodes (8): can_cast_fields(), _equivalent_fields(), _equivalent_subarrays(), PyArray_LegacyCanCastSafely(), PyArray_LegacyCanCastTo(), PyArray_LegacyCanCastTypeTo(), PyArray_LegacyEquivTypenums(), PyArray_LegacyEquivTypes()

### Community 239 - "Community 239"
Cohesion: 0.22
Nodes (4): A, B, C, D

### Community 240 - "Community 240"
Cohesion: 0.22
Nodes (3): GenericObject, print_new_cast_table(), Prints new casts, the values given are default "can-cast" values, not     actual

### Community 241 - "Community 241"
Cohesion: 0.36
Nodes (6): buffer_info_from_unicode(), fb_del(), fb_nextbuf(), it_nextbuf(), process_stringlike(), stream_python_file()

### Community 242 - "Community 242"
Cohesion: 0.22
Nodes (9): _check_and_copy_sig_to_signature(), prepare_input_arguments_for_outer(), replace_with_wrapped_result_and_return(), _set_full_args_out(), try_trivial_scalar_call(), tuple_all_none(), ufunc_generic_fastcall(), ufunc_generic_vectorcall() (+1 more)

### Community 243 - "Community 243"
Cohesion: 0.39
Nodes (1): _BaseVersion

### Community 244 - "Community 244"
Cohesion: 0.25
Nodes (8): array_repr(), _array_repr_implementation(), dtype_is_implied(), dtype_short_repr(), Determine if the given dtype is implied by the representation     of its values., Convert a dtype to a short form which evaluates to the same dtype.      The inte, Internal version of array_repr() that allows overriding array2string., Return the string representation of an array.      Parameters     ----------

### Community 245 - "Community 245"
Cohesion: 0.29
Nodes (4): _ArrayMemoryError, Thrown when an array cannot be allocated, Convert a number of bytes into a binary size string, MemoryError

### Community 246 - "Community 246"
Cohesion: 0.25
Nodes (5): bincount(), Create the numpy._core.multiarray namespace for backward compatibility. In v1.16, bincount(x, /, weights=None, minlength=0)      Count number of occurrences of ea, ravel_multi_index(multi_index, dims, mode='raise', order='C')      Converts a tu, ravel_multi_index()

### Community 247 - "Community 247"
Cohesion: 0.25
Nodes (8): cross(), moveaxis(), normalize_axis_tuple(), Roll array elements along a given axis.      Elements that roll beyond the last, Normalizes an axis argument into a tuple of non-negative integer axes.      This, Move axes of an array to new positions.      Other axes remain in their original, Return the cross product of two (arrays of) vectors.      The cross product of `, roll()

### Community 248 - "Community 248"
Cohesion: 0.29
Nodes (7): english_capitalize(), english_lower(), english_upper(), String-handling utilities to avoid locale-dependence.  Used primarily to generat, Apply English case rules to convert ASCII strings to all lower case.      This i, Apply English case rules to convert ASCII strings to all upper case.      This i, Apply English case rules to convert the first character of an ASCII     string t

### Community 249 - "Community 249"
Cohesion: 0.25
Nodes (7): DeprecationWarning, ModuleDeprecationWarning, Exceptions and Warnings =======================  General exceptions used by NumP, Module deprecation warning.      .. warning::          This warning should not b, ``max_work`` was exceeded.      This is raised whenever the maximum number of ca, TooHardError, RuntimeError

### Community 250 - "Community 250"
Cohesion: 0.29
Nodes (5): F2PYError, throw_error, buildcallback(), buildcallbacks(), Build call-back mechanism for f2py2e.  Copyright 1999 -- 2011 Pearu Peterson all

### Community 251 - "Community 251"
Cohesion: 0.32
Nodes (6): append_needs(), errmess(), get_needs(), C declarations, CPP macros, and C functions for f2py2e. Only required declaratio, Write an error message to stderr.      This indirection is needed because sys.st, # TODO: These should be dynamically generated, too many mapped to int things,

### Community 252 - "Community 252"
Cohesion: 0.54
Nodes (7): assubr(), createfuncwrapper(), createsubrwrapper(), Rules for building C/API module with f2py2e.  Copyright 1999 -- 2011 Pearu Peter, useiso_c_binding(), useiso_fortran_env(), var2fixfortran()

### Community 253 - "Community 253"
Cohesion: 0.25
Nodes (8): _nanmedian1d(), _nanquantile_1d(), _nanquantile_ureduce_func(), Private function for rank 1 arrays. Compute the median ignoring NaNs.     See na, Equivalent to arr1d[~arr1d.isnan()], but in a different order      Presumably fa, Private function that doesn't support extended axis or keepdims.     These metho, Private function for rank 1 arrays. Compute quantile ignoring NaNs.     See nanp, _remove_nan_1d()

### Community 254 - "Community 254"
Cohesion: 0.25
Nodes (5): polydiv(), polyint(), Return an antiderivative (indefinite integral) of this polynomial.          Refe, Return an antiderivative (indefinite integral) of a polynomial.      .. note::, Returns the quotient and remainder of polynomial division.      .. note::

### Community 255 - "Community 255"
Cohesion: 0.25
Nodes (8): append_fields(), _izip_records(), merge_arrays(), Returns an iterator of concatenated items from a sequence of arrays.      Parame, Merge arrays field by field.      Parameters     ----------     seqarrays : sequ, Add new fields to an existing array.      The names of the fields are given with, Add new fields to an existing array.      The names of the fields are given with, rec_append_fields()

### Community 256 - "Community 256"
Cohesion: 0.25
Nodes (8): _assert_2d(), multi_dot(), _multi_dot_matrix_chain_order(), _multi_dot_three(), Compute the dot product of two or more arrays in a single function call,     whi, Find the best order for three arrays and do the multiplication.      For three a, Return a np.array that encodes the optimal order of multiplications.      The op, Actually do the multiplication with the given order.

### Community 257 - "Community 257"
Cohesion: 0.25
Nodes (8): matrix_norm(), _multi_svd_norm(), norm(), Compute a function of the singular values of the 2-D matrices in `x`.      This, Matrix or vector norm.      This function is able to return one of eight differe, Computes the matrix norm of a matrix (or a stack of matrices) ``x``.      This f, Computes the vector norm of a vector (or batch of vectors) ``x``.      This func, vector_norm()

### Community 258 - "Community 258"
Cohesion: 0.25
Nodes (4): A convenience function for operations that need to preserve axis         orienta, Indexes of the maximum values along an axis.          Return the indexes of the, Indexes of the minimum values along an axis.          Return the indexes of the, Peak-to-peak (maximum - minimum) value along the given axis.          Refer to `

### Community 259 - "Community 259"
Cohesion: 0.46
Nodes (7): array_datetime_as_string(), convert_datetimestruct_utc_to_local(), get_localtime(), lossless_unit_from_datetimestruct(), NpyDatetime_GetDatetimeISO8601StrLen(), NpyDatetime_MakeISO8601Datetime(), NpyDatetime_ParseISO8601Datetime()

### Community 260 - "Community 260"
Cohesion: 0.32
Nodes (8): get_fields_transfer_function(), get_n_to_n_transfer_function(), get_one_to_n_transfer_function(), get_subarray_broadcast_transfer_function(), get_subarray_transfer_function(), PyArray_CastRawArrays(), PyArray_GetDTypeTransferFunction(), PyArray_GetMaskedDTypeTransferFunction()

### Community 261 - "Community 261"
Cohesion: 0.29
Nodes (8): array_concatenate(), PyArray_CompareLists(), PyArray_Concatenate(), PyArray_ConcatenateArrays(), PyArray_ConcatenateFlattenedArrays(), PyArray_ConcatenateInto(), PyArray_GetPriority(), PyArray_GetSubType()

### Community 262 - "Community 262"
Cohesion: 0.29
Nodes (2): get_initial_from_ufunc(), PyArray_NewLegacyWrappingArrayMethod()

### Community 263 - "Community 263"
Cohesion: 0.43
Nodes (7): add_unwrap_loop(), f2h(), floor_mod(), h2f(), init_unwrap_ufunc(), unwrap_half_loop(), unwrap_loop()

### Community 264 - "Community 264"
Cohesion: 0.29
Nodes (2): get_wrapping_auxdata(), wrapping_method_get_loop()

### Community 265 - "Community 265"
Cohesion: 0.25
Nodes (1): Version

### Community 266 - "Community 266"
Cohesion: 0.52
Nodes (6): _bad_strides(), cblas_matrixproduct(), gemm(), gemv(), _select_matrix_shape(), syrk()

### Community 267 - "Community 267"
Cohesion: 0.43
Nodes (4): initialize_keywords(), _npy_parse_arguments(), raise_incorrect_number_of_positional_args(), raise_missing_argument()

### Community 268 - "Community 268"
Cohesion: 0.29
Nodes (3): This file is separate from ``_add_newdocs.py`` so that it can be mocked out by o, # TODO: These docs probably need an if to highlight the default rather than, # TODO: work out how to put this on the base class, np.floating

### Community 269 - "Community 269"
Cohesion: 0.29
Nodes (2): dict, bunch

### Community 270 - "Community 270"
Cohesion: 0.29
Nodes (7): iscomplex(), iscomplexfunction(), iscomplexfunction_warn(), islong_complex(), outmess(), process_f2cmap_dict(), Update the Fortran-to-C type mapping dictionary with new mappings and     return

### Community 271 - "Community 271"
Cohesion: 0.29
Nodes (7): copy(), delete(), meshgrid(), _quantile_ureduce_func(), Return a tuple of coordinate matrices from coordinate vectors.      Make N-D coo, Return a new array with sub-arrays along an axis deleted. For a one     dimensio, Return an array copy of the given object.      Parameters     ----------     a :

### Community 272 - "Community 272"
Cohesion: 0.29
Nodes (6): _get_vectorize_dtype(), iterable(), _parse_gufunc_signature(), _piecewise_dispatcher(), Parse string signatures for a generalized universal function.      Arguments, Check whether or not an object can be iterated over.      Parameters     -------

### Community 273 - "Community 273"
Cohesion: 0.29
Nodes (7): nanmean(), _nanmedian(), _nanmedian_small(), Private function that doesn't support extended axis or keepdims.     These metho, sort + indexing median, faster for small medians along multiple     dimensions d, Compute the median along the specified axis, while ignoring NaNs.      Returns t, Compute the arithmetic mean along the specified axis, ignoring NaNs.      Return

### Community 274 - "Community 274"
Cohesion: 0.29
Nodes (5): EighResult, SlogdetResult, SVDResult, NamedTuple, XYGrid

### Community 275 - "Community 275"
Cohesion: 0.52
Nodes (6): add_state(), copy_state(), gen_next(), get_coef(), horner1(), mt19937_jump_state()

### Community 276 - "Community 276"
Cohesion: 0.57
Nodes (6): can_elide_temp(), can_elide_temp_unary(), check_callers(), check_unique_temporary(), find_addr(), try_binary_elide()

### Community 277 - "Community 277"
Cohesion: 0.29
Nodes (1): Object

### Community 279 - "Community 279"
Cohesion: 0.29
Nodes (7): assert_(), assert_no_gc_cycles(), _assert_no_gc_cycles_context(), _assert_valid_refcount(), Assert that works in release mode.     Accepts callable msg to allow deferring e, Check that ufuncs don't mishandle refcount of object `1`.     Used in a few regr, Fail if the given callable produces any reference cycles.      If called with al

### Community 280 - "Community 280"
Cohesion: 0.29
Nodes (6): __bit_generator_ctor(), __generator_ctor(), __randomstate_ctor(), Pickling helper function that returns a bit generator object      Parameters, Pickling helper function that returns a Generator object      Parameters     ---, Pickling helper function that returns a legacy RandomState-like object      Para

### Community 281 - "Community 281"
Cohesion: 0.29
Nodes (1): _Empty

### Community 282 - "Community 282"
Cohesion: 0.33
Nodes (1): TemplateDef

### Community 283 - "Community 283"
Cohesion: 0.29
Nodes (2): TemplateObject, TemplateObjectGetter

### Community 284 - "Community 284"
Cohesion: 0.33
Nodes (3): Here we define the exported functions, types, etc... which need to be exported t, # NOTE: The Slots 320-360 are defined in `_experimental_dtype_api.h`, Simple script to compute the api hash of the current API.  The API has is define

### Community 285 - "Community 285"
Cohesion: 0.47
Nodes (3): IsAligned(), IsUintAligned(), raw_array_is_aligned()

### Community 286 - "Community 286"
Cohesion: 0.33
Nodes (4): multiply(), Return (a * i), that is string multiple concatenation,     element-wise.      Va, Return (self * i), that is string multiple concatenation,         element-wise., Return (self * i), that is string multiple concatenation,         element-wise.

### Community 287 - "Community 287"
Cohesion: 0.33
Nodes (6): prod(), Return the shape of an array.      Parameters     ----------     a : array_like, Return the product of array elements over a given axis.      Parameters     ----, Return the number of elements along a given axis.      Parameters     ----------, shape(), size()

### Community 288 - "Community 288"
Cohesion: 0.33
Nodes (6): Return a new array with the specified shape.      If the new array is larger tha, Return a contiguous flattened array.      A 1-D array, containing the elements o, Returns a reshaped ndarray without changing data.      Parameters     ----------, ravel(), reshape(), resize()

### Community 289 - "Community 289"
Cohesion: 0.33
Nodes (1): dummy_ctype

### Community 290 - "Community 290"
Cohesion: 0.33
Nodes (6): astype(), count_nonzero(), isscalar(), Returns True if the type of `element` is a scalar type.      Parameters     ----, Copies an array to a specified data type.      This function is an Array API com, Counts the number of non-zero values in the array ``a``.      A non-zero value i

### Community 292 - "Community 292"
Cohesion: 0.40
Nodes (6): _ischaracter(), ischaracter_or_characterarray(), ischaracterarray(), isexternal(), _isstring(), isstring_or_stringarray()

### Community 293 - "Community 293"
Cohesion: 0.33
Nodes (4): as_array(), ewarn(), Recursively substitute symbols with values in symbols map.          Symbols map, Return object as ARRAY expression (array constant).

### Community 294 - "Community 294"
Cohesion: 0.33
Nodes (6): i0(), kaiser(), piecewise(), Modified Bessel function of the first kind, order 0.      Usually denoted :math:, Return the Kaiser window.      The Kaiser window is a taper formed by using a Be, Evaluate a piecewise-defined function.      Given a set of conditions and corres

### Community 295 - "Community 295"
Cohesion: 0.33
Nodes (6): median(), _quantile_unchecked(), Internal Function.     Call `func` with `a` as first argument swapping the axes, Compute the median along the specified axis.      Returns the median of the arra, Assumes that q is in [0, 1], and is an ndarray, _ureduce()

### Community 296 - "Community 296"
Cohesion: 0.33
Nodes (6): _copyto(), nanmax(), nanmin(), Replace values in `a` with NaN where `mask` is True.  This differs from     copy, Return minimum of an array or minimum along an axis, ignoring any NaNs.     When, Return the maximum of an array or maximum along an axis, ignoring any     NaNs.

### Community 297 - "Community 297"
Cohesion: 0.33
Nodes (6): _divide_by_count(), nanstd(), nanvar(), Compute the variance along the specified axis, while ignoring NaNs.      Returns, Compute the standard deviation along the specified axis, while     ignoring NaNs, Compute a/b ignoring invalid results. If `a` is an array the division     is don

### Community 298 - "Community 298"
Cohesion: 0.33
Nodes (6): nanpercentile(), nanquantile(), _nanquantile_unchecked(), Compute the qth percentile of the data along the specified axis,     while ignor, Compute the qth quantile of the data along the specified axis,     while ignorin, Assumes that q is in [0, 1], and is an ndarray

### Community 299 - "Community 299"
Cohesion: 0.33
Nodes (6): drop_fields(), Fills fields from output with fields from input,     with support for nested str, Return a new array with fields in `drop_names` dropped.      Nested fields are s, Returns a new numpy.recarray with fields in `drop_names` dropped., rec_drop_fields(), recursive_fill_fields()

### Community 300 - "Community 300"
Cohesion: 0.33
Nodes (6): apply_over_axes(), expand_dims(), kron(), Kronecker product of two arrays.      Computes the Kronecker product, a composit, Apply a function repeatedly over multiple axes.      `func` is called as `res =, Expand the shape of an array.      Insert a new axis that will appear at the `ax

### Community 301 - "Community 301"
Cohesion: 0.33
Nodes (4): _DomainCheckInterval, Define a valid interval, so that :      ``domain_check_interval(a,b)(x) == True`, domain_check_interval(a,b)(x) = true where x < a or y > b, Execute the call behavior.

### Community 302 - "Community 302"
Cohesion: 0.33
Nodes (4): _DomainGreaterEqual, DomainGreaterEqual(v)(x) is True where x < v., DomainGreaterEqual(v)(x) = true where x < v, Executes the call behavior.

### Community 303 - "Community 303"
Cohesion: 0.33
Nodes (4): _DomainGreater, DomainGreater(v)(x) is True where x <= v., DomainGreater(v)(x) = true where x <= v, Executes the call behavior.

### Community 304 - "Community 304"
Cohesion: 0.33
Nodes (4): _DomainTan, Define a valid interval for the `tan` function, so that:      ``domain_tan(eps), domain_tan(eps) = true where abs(cos(x)) < eps), Executes the call behavior.

### Community 305 - "Community 305"
Cohesion: 0.40
Nodes (4): bmat(), _convert_from_string(), _from_string(), Build a matrix object from a string, nested sequence, or array.      Parameters

### Community 306 - "Community 306"
Cohesion: 0.40
Nodes (2): init_genrand(), mt19937_init_by_array()

### Community 307 - "Community 307"
Cohesion: 0.33
Nodes (6): get_datetime_to_unicode_transfer_function(), get_nbo_cast_datetime_transfer_function(), get_nbo_datetime_to_string_transfer_function(), get_nbo_string_to_datetime_transfer_function(), get_unicode_to_datetime_transfer_function(), _safe_print()

### Community 308 - "Community 308"
Cohesion: 0.33
Nodes (6): multi_DECREF(), _nonzero_indices(), prepare_index_noarray(), unpack_indices(), unpack_scalar(), unpack_tuple()

### Community 309 - "Community 309"
Cohesion: 0.33
Nodes (6): array_array(), array_asanyarray(), array_asarray(), array_ascontiguousarray(), array_asfortranarray(), _array_fromobject_generic()

### Community 310 - "Community 310"
Cohesion: 0.33
Nodes (6): array_scalar(), _finfo_get_realdtype(), PyArray_EquivTypenums(), PyArray_EquivTypes(), resolve_part_view_descr(), resolve_view_part_descr()

### Community 311 - "Community 311"
Cohesion: 0.47
Nodes (3): array_repr(), array_str(), npy_PyErr_SetStringChained()

### Community 312 - "Community 312"
Cohesion: 0.40
Nodes (2): bounded_uint(), bounded_uints()

### Community 313 - "Community 313"
Cohesion: 0.33
Nodes (6): assert_array_almost_equal_nulp(), assert_array_max_ulp(), nulp_diff(), Compare two arrays relatively to their spacing.      This is a relatively robust, Check that all items of arrays differ in at most N Units in the Last Place., For each item in x and y, return the number of representable floating     points

### Community 314 - "Community 314"
Cohesion: 0.33
Nodes (6): check_free_memory(), _get_mem_available(), _parse_size(), Check whether `free_bytes` amount of memory is currently free.     Returns: None, Convert memory size strings ('12 GB' etc.) to float, Return available memory in bytes, or None if unknown.

### Community 315 - "Community 315"
Cohesion: 0.33
Nodes (5): add_newdoc(), _parse_docstrings(), A module for creating docstrings for sphinx ``data`` domains., Append ``_docstrings_list`` with a docstring for `name`.      Parameters     ---, Convert all docstrings in ``_docstrings_list`` into a single     sphinx-legible

### Community 316 - "Community 316"
Cohesion: 0.60
Nodes (5): NPY_CPU_DISPATCH_CURFX(), simd_cosine_poly_f32(), simd_range_reduction_f32(), simd_sincos_f32(), simd_sine_poly_f32()

### Community 317 - "Community 317"
Cohesion: 0.60
Nodes (5): copy_positional_args_to_kwargs(), get_array_ufunc_overrides(), initialize_normal_kwds(), normalize_signature_keyword(), PyUFunc_CheckOverride()

### Community 318 - "Community 318"
Cohesion: 0.33
Nodes (6): new_array_op(), resolve_descriptors(), trivial_at_loop(), ufunc_at(), ufunc_at__fast_iter(), ufunc_at__slow_iter()

### Community 319 - "Community 319"
Cohesion: 0.33
Nodes (5): This is a module for defining private helpers which do not depend on the rest of, Private decorator for overriding __module__ on a function or class.      Example, Generate decorator for backward-compatible keyword renaming.      Apply the deco, _rename_parameter(), set_module()

### Community 321 - "Community 321"
Cohesion: 0.60
Nodes (4): get_processor(), main(), process_and_write_file(), Process tempita templated file and write out the result.      The template file

### Community 322 - "Community 322"
Cohesion: 0.60
Nodes (4): import_tempita(), main(), process_tempita(), Process tempita templated file and write out the result.      The template file

### Community 323 - "Community 323"
Cohesion: 0.40
Nodes (1): BoolValuesApi

### Community 324 - "Community 324"
Cohesion: 0.40
Nodes (1): GlobalVarApi

### Community 325 - "Community 325"
Cohesion: 0.40
Nodes (1): TypeApi

### Community 326 - "Community 326"
Cohesion: 0.40
Nodes (5): array_str(), _array_str_implementation(), _guarded_repr_or_str(), Internal version of array_str() that allows overriding array2string., Return a string representation of the data in an array.      The data in the arr

### Community 327 - "Community 327"
Cohesion: 0.40
Nodes (5): format_float_positional(), format_float_scientific(), _none_or_positive_arg(), Format a floating-point scalar as a decimal string in scientific notation., Format a floating-point scalar as a decimal string in positional notation.

### Community 328 - "Community 328"
Cohesion: 0.40
Nodes (5): all(), any(), Test whether any array element along a given axis evaluates to True.      Return, Test whether all array elements along a given axis evaluate to True.      Parame, _wrapreduction_any_all()

### Community 329 - "Community 329"
Cohesion: 0.40
Nodes (5): _cumulative_func(), cumulative_prod(), cumulative_sum(), Return the cumulative product of elements along a given axis.      This function, Return the cumulative sum of the elements along a given axis.      This function

### Community 330 - "Community 330"
Cohesion: 0.40
Nodes (3): This module is home to specific dtypes related functionality and their classes., Register a NumPy dtype for a DLPack ``(code, bits)`` pair so that     `numpy.fro, register_dlpack_dtype()

### Community 331 - "Community 331"
Cohesion: 0.50
Nodes (5): isintent_hide(), isintent_nothide(), isoptional(), isrequired(), l_or()

### Community 332 - "Community 332"
Cohesion: 0.40
Nodes (5): flatten_descr(), Flatten a structured data-type description.      Examples     --------     >>> i, Combine the dtype description of a series of arrays.      Parameters     -------, _zip_descr(), _zip_dtype()

### Community 333 - "Community 333"
Cohesion: 0.70
Nodes (4): copycast_isaligned(), PyArray_AssignArray(), raw_array_assign_array(), raw_array_wheremasked_assign_array()

### Community 334 - "Community 334"
Cohesion: 0.60
Nodes (3): _get_wrap_prepare_args(), npy_apply_wrap(), npy_apply_wrap_simple()

### Community 335 - "Community 335"
Cohesion: 0.40
Nodes (5): array_innerproduct(), array_matrixproduct(), PyArray_InnerProduct(), PyArray_MatrixProduct(), PyArray_MatrixProduct2()

### Community 338 - "Community 338"
Cohesion: 0.60
Nodes (4): npy_aquicksort(), npy_aquicksort_impl(), npy_quicksort(), npy_quicksort_impl()

### Community 339 - "Community 339"
Cohesion: 0.40
Nodes (2): Index, SubClass

### Community 340 - "Community 340"
Cohesion: 0.40
Nodes (3): IntSubClass, Tests for miscellaneous (non-magic) ``np.ndarray``/``np.generic`` methods.  More, SubClass

### Community 341 - "Community 341"
Cohesion: 0.40
Nodes (2): clear_and_catch_warnings, Context manager that resets warning registry for catching warnings      Warnings

### Community 342 - "Community 342"
Cohesion: 0.40
Nodes (5): jiffies(), measure(), Return elapsed time for executing code in the namespace of the caller.      The, Return number of jiffies elapsed.          Return number of jiffies (1/100ths of, Return number of jiffies elapsed.          Return number of jiffies (1/100ths of

### Community 343 - "Community 343"
Cohesion: 0.40
Nodes (3): Pytest test running.  This module implements the ``test()`` function for NumPy m, Run tests for module using pytest.          Parameters         ----------, _show_numpy_info()

### Community 344 - "Community 344"
Cohesion: 0.70
Nodes (4): field_type_grow_recursive(), field_types_create(), field_types_xclear(), get_from_ucs4_function()

### Community 345 - "Community 345"
Cohesion: 0.60
Nodes (3): error_if_matching_control_characters(), _load_from_filelike(), _readtext_from_stream()

### Community 346 - "Community 346"
Cohesion: 0.40
Nodes (5): _get_dtype(), _get_fixed_signature(), py_resolve_dtypes(), py_resolve_dtypes_and_context(), py_resolve_dtypes_generic()

### Community 347 - "Community 347"
Cohesion: 0.50
Nodes (4): fullapi_hash(), order_dict(), Order dict by its values., Given a list of api dicts defining the numpy C API, compute a checksum     of th

### Community 348 - "Community 348"
Cohesion: 0.50
Nodes (2): MinVersion, Version should be the normal NumPy version, e.g. "1.25"

### Community 349 - "Community 349"
Cohesion: 0.83
Nodes (3): do_generate_api(), generate_api(), main()

### Community 350 - "Community 350"
Cohesion: 0.83
Nodes (3): do_generate_api(), generate_api(), main()

### Community 351 - "Community 351"
Cohesion: 0.83
Nodes (3): main(), normalize_doc(), write_code()

### Community 354 - "Community 354"
Cohesion: 0.67
Nodes (2): npy_longdouble_from_PyLong(), _PyLong_Bytes()

### Community 355 - "Community 355"
Cohesion: 0.67
Nodes (2): PyUFunc_HasOverride(), PyUFuncOverride_GetNonDefaultArrayUfunc()

### Community 356 - "Community 356"
Cohesion: 0.50
Nodes (3): _array_method_doc(), This is only meant to add docs to objects defined in C-extension modules. The pu, Interenal helper function for adding docstrings to a common method of     `numpy

### Community 357 - "Community 357"
Cohesion: 0.50
Nodes (4): get_printoptions(), printoptions(), Return the current print options.      Returns     -------     print_opts : dict, Context manager for setting print options.      Set print options for the scope

### Community 358 - "Community 358"
Cohesion: 0.50
Nodes (3): Functions in the ``as*array`` family that promote array-likes into arrays.  `req, Return an ndarray of the provided type that satisfies requirements.      This fu, require()

### Community 359 - "Community 359"
Cohesion: 0.50
Nodes (3): greater_equal(), Return (x1 >= x2) element-wise.      Unlike `numpy.greater_equal`, this comparis, Return (self >= other) element-wise.          See Also         --------

### Community 360 - "Community 360"
Cohesion: 0.50
Nodes (3): greater(), Return (x1 > x2) element-wise.      Unlike `numpy.greater`, this comparison is p, Return (self > other) element-wise.          See Also         --------         g

### Community 361 - "Community 361"
Cohesion: 0.50
Nodes (3): less_equal(), Return (x1 <= x2) element-wise.      Unlike `numpy.less_equal`, this comparison, Return (self <= other) element-wise.          See Also         --------

### Community 362 - "Community 362"
Cohesion: 0.50
Nodes (3): less(), Return (x1 < x2) element-wise.      Unlike `numpy.greater`, this comparison is p, Return (self < other) element-wise.          See Also         --------         l

### Community 363 - "Community 363"
Cohesion: 0.50
Nodes (4): matrix_transpose(), Interchange two axes of an array.      Parameters     ----------     a : array_l, Transposes a matrix (or a stack of matrices) ``x``.      This function is Array, swapaxes()

### Community 364 - "Community 364"
Cohesion: 0.50
Nodes (4): allclose(), isclose(), Returns True if two arrays are element-wise equal within a tolerance.      The t, Returns a boolean array where two arrays are element-wise equal within a     tol

### Community 365 - "Community 365"
Cohesion: 0.50
Nodes (4): convolve(), correlate(), r"""     Cross-correlation of two 1-dimensional sequences.      This function co, Returns the discrete, linear convolution of two one-dimensional sequences.

### Community 366 - "Community 366"
Cohesion: 0.50
Nodes (4): fromfunction(), indices(), Return an array representing the indices of a grid.      Compute an array where, Construct an array by executing a function over each coordinate.      The result

### Community 367 - "Community 367"
Cohesion: 0.83
Nodes (3): hypergeometric_hrua(), hypergeometric_sample(), random_hypergeometric()

### Community 368 - "Community 368"
Cohesion: 0.67
Nodes (3): buildhooks(), findcommonblocks(), Build common block mechanism for f2py2e.  Copyright 1999 -- 2011 Pearu Peterson

### Community 369 - "Community 369"
Cohesion: 0.67
Nodes (3): buildhooks(), findf90modules(), Build F90 module support for f2py2e.  Copyright 1999 -- 2011 Pearu Peterson all

### Community 370 - "Community 370"
Cohesion: 0.67
Nodes (3): buildapi(), buildmodule(), Rules for building C/API module with f2py2e.  Here is a skeleton of a new wrappe

### Community 371 - "Community 371"
Cohesion: 0.67
Nodes (3): buildusevar(), buildusevars(), Build 'use others module data' mechanism for f2py2e.  Copyright 1999 -- 2011 Pea

### Community 372 - "Community 372"
Cohesion: 0.50
Nodes (4): dcabs1_(), dzasum_(), izamax_(), zaxpy_()

### Community 373 - "Community 373"
Cohesion: 0.50
Nodes (4): _arg_trim_zeros(), Return indices of the first and last non-zero element.      Parameters     -----, Remove values along a dimension which are zero along all other.      Parameters, _trim_zeros()

### Community 374 - "Community 374"
Cohesion: 0.50
Nodes (4): flip(), Rotate an array by 90 degrees in the plane specified by axes.      Rotation dire, Reverse the order of elements in an array along the given axis.      The shape o, rot90()

### Community 375 - "Community 375"
Cohesion: 0.50
Nodes (3): opt_func_info(), Introspection helper functions., Returns a dictionary containing the currently supported CPU dispatched     featu

### Community 376 - "Community 376"
Cohesion: 0.50
Nodes (3): polyder(), Return a derivative of this polynomial.          Refer to `polyder` for full doc, Return the derivative of the specified order of a polynomial.      .. note::

### Community 377 - "Community 377"
Cohesion: 0.50
Nodes (2): polysub(), Difference (subtraction) of two polynomials.      .. note::        This forms pa

### Community 378 - "Community 378"
Cohesion: 0.50
Nodes (4): assign_fields_by_name(), Assigns values from one structured array to another by field name.      Normally, Casts a structured array to a new dtype using assignment by field-name.      Thi, require_fields()

### Community 379 - "Community 379"
Cohesion: 0.50
Nodes (4): find_duplicates(), get_fieldstructure(), Find the duplicates in a structured array along a given key      Parameters, Returns a dictionary with fields indexing lists of their parent fields.      Thi

### Community 380 - "Community 380"
Cohesion: 0.50
Nodes (1): Mapping

### Community 381 - "Community 381"
Cohesion: 0.50
Nodes (2): Return `self` as a flattened `ndarray`.          Equivalent to ``np.asarray(x).r, Return a flattened matrix.          Refer to `numpy.ravel` for more documentatio

### Community 383 - "Community 383"
Cohesion: 0.83
Nodes (3): PyArray_AssignRawScalar(), raw_array_assign_scalar(), raw_array_wheremasked_assign_scalar()

### Community 384 - "Community 384"
Cohesion: 0.83
Nodes (3): PyArray_CommonDType(), PyArray_PromoteDTypeSequence(), reduce_dtypes_to_most_knowledgeable()

### Community 385 - "Community 385"
Cohesion: 0.83
Nodes (3): npy_fnv1a(), npy_fnv1a_32(), npy_fnv1a_64()

### Community 386 - "Community 386"
Cohesion: 0.50
Nodes (4): array_choose(), array_reshape(), array_resize(), NpyArg_ParseKeywords()

### Community 387 - "Community 387"
Cohesion: 0.50
Nodes (4): array_getfield(), array_setfield(), PyArray_GetField(), PyArray_SetField()

### Community 388 - "Community 388"
Cohesion: 0.50
Nodes (4): array_correlate2(), _pyarray_correlate(), PyArray_Correlate2(), _pyarray_revert()

### Community 389 - "Community 389"
Cohesion: 0.50
Nodes (4): array_einsum(), einsum_list_to_subscripts(), einsum_sub_op_from_lists(), einsum_sub_op_from_str()

### Community 390 - "Community 390"
Cohesion: 0.50
Nodes (4): initialize_global_state(), _multiarray_umath_exec(), set_flaginfo(), setup_scalartypes()

### Community 391 - "Community 391"
Cohesion: 0.50
Nodes (4): _is_user_defined_string_array(), _vec_string(), _vec_string_no_args(), _vec_string_with_args()

### Community 393 - "Community 393"
Cohesion: 0.50
Nodes (1): Simple expression that should pass with mypy.

### Community 394 - "Community 394"
Cohesion: 0.50
Nodes (4): assert_almost_equal(), assert_array_almost_equal(), Raises an AssertionError if two objects are not equal up to desired     precisio, Raises an AssertionError if two items are not equal up to desired     precision.

### Community 395 - "Community 395"
Cohesion: 0.50
Nodes (4): GetPerformanceAttributes(), memusage(), Return virtual memory size in bytes of the running python., Return memory usage of running python. [Not implemented]

### Community 398 - "Community 398"
Cohesion: 0.50
Nodes (3): # NOTE: Nested literals get flattened and de-duplicated at runtime, which isn't, # TODO: add `_StringCodes` once it has a scalar type, # NOTE: `StringDType' has no scalar type, and therefore has no name that can

### Community 399 - "Community 399"
Cohesion: 0.83
Nodes (3): count_axes(), PyArray_CopyInitialReduceValues(), PyUFunc_ReduceWrapper()

### Community 402 - "Community 402"
Cohesion: 0.50
Nodes (1): A set of methods retained from np.compat module that are still used across codeb

### Community 404 - "Community 404"
Cohesion: 0.67
Nodes (2): parse_distributions_h(), Parse distributions.h located in inc_dir for CFFI, filling in the ffi.cdef

### Community 406 - "Community 406"
Cohesion: 1.00
Nodes (2): accumulate(), main()

### Community 407 - "Community 407"
Cohesion: 0.67
Nodes (1): StealRef

### Community 408 - "Community 408"
Cohesion: 0.67
Nodes (1): Docstrings for generated ufuncs  The syntax is designed to look like the functio

### Community 412 - "Community 412"
Cohesion: 0.67
Nodes (3): Remove axes of length one from `a`.      Parameters     ----------     a : array, squeeze(), _wrapit()

### Community 413 - "Community 413"
Cohesion: 0.67
Nodes (1): Create the numpy._core.umath namespace for backward compatibility. In v1.16 the

### Community 414 - "Community 414"
Cohesion: 0.67
Nodes (2): ISO_C_BINDING maps for f2py2e. Only required declarations/macros/functions will, # TODO: See gh-25229

### Community 415 - "Community 415"
Cohesion: 0.67
Nodes (3): caxpy_(), icamax_(), scabs1_()

### Community 416 - "Community 416"
Cohesion: 0.67
Nodes (2): byte_bounds(), Returns pointers to the end-points of an array.      Parameters     ----------

### Community 417 - "Community 417"
Cohesion: 0.67
Nodes (2): polyval(), Evaluate a polynomial at specific values.      .. note::        This forms part

### Community 418 - "Community 418"
Cohesion: 0.67
Nodes (2): poly(), Find the coefficients of a polynomial with the given sequence of roots.      ..

### Community 419 - "Community 419"
Cohesion: 1.00
Nodes (3): array_reduce_ex(), array_reduce_ex_picklebuffer(), array_reduce_ex_regular()

### Community 420 - "Community 420"
Cohesion: 0.67
Nodes (3): array_may_share_memory(), array_shares_memory(), array_shares_memory_impl()

### Community 423 - "Community 423"
Cohesion: 0.67
Nodes (1): r""" Building the required library in this example requires a source distributio

### Community 424 - "Community 424"
Cohesion: 0.67
Nodes (1): A

### Community 425 - "Community 425"
Cohesion: 0.67
Nodes (2): Tests for :mod:`numpy._core.numeric`.  Does not include tests which fall under `, SubClass

### Community 427 - "Community 427"
Cohesion: 1.00
Nodes (2): create_conv_funcs(), read_rows()

### Community 431 - "Community 431"
Cohesion: 1.00
Nodes (1): Use cffi to access any of the underlying C functions from distributions.h

### Community 477 - "Community 477"
Cohesion: 1.00
Nodes (1): For each element in `self`, return True if there are only         numeric charac

### Community 478 - "Community 478"
Cohesion: 1.00
Nodes (1): Returns true for each element if there are only whitespace         characters in

### Community 479 - "Community 479"
Cohesion: 1.00
Nodes (1): Returns true for each element if the element is a titlecased         string and

### Community 480 - "Community 480"
Cohesion: 1.00
Nodes (1): Returns true for each element if all cased characters in the         string are

### Community 481 - "Community 481"
Cohesion: 1.00
Nodes (1): Return a string which is the concatenation of the strings in the         sequenc

### Community 482 - "Community 482"
Cohesion: 1.00
Nodes (1): For each element in `self`, return a copy with the leading characters         re

### Community 483 - "Community 483"
Cohesion: 1.00
Nodes (1): Return (other + self), that is string concatenation,         element-wise for a

### Community 484 - "Community 484"
Cohesion: 1.00
Nodes (1): For each element in `self`, return a copy of the string with all         occurre

### Community 485 - "Community 485"
Cohesion: 1.00
Nodes (1): For each element in `self`, return the highest index in the string         where

### Community 486 - "Community 486"
Cohesion: 1.00
Nodes (1): Like `rfind`, but raises :exc:`ValueError` when the substring `sub` is         n

### Community 487 - "Community 487"
Cohesion: 1.00
Nodes (1): For each element in `self`, return a list of the words in         the string, us

### Community 488 - "Community 488"
Cohesion: 1.00
Nodes (1): For each element in `self`, return a list of the words in the         string, us

### Community 489 - "Community 489"
Cohesion: 1.00
Nodes (1): For each element in `self`, return a list of the lines in the         element, b

### Community 490 - "Community 490"
Cohesion: 1.00
Nodes (1): Returns a boolean array which is `True` where the string element         in `sel

### Community 491 - "Community 491"
Cohesion: 1.00
Nodes (1): For each element in `self`, return a copy with the leading and         trailing

### Community 492 - "Community 492"
Cohesion: 1.00
Nodes (2): diagonal(), Return specified diagonals.      If `a` is 2-D, returns the diagonal of `a` with

### Community 493 - "Community 493"
Cohesion: 1.00
Nodes (2): mean(), Compute the arithmetic mean along the specified axis.      Returns the average o

### Community 494 - "Community 494"
Cohesion: 1.00
Nodes (2): ndim(), Return the number of dimensions of an array.      Parameters     ----------

### Community 495 - "Community 495"
Cohesion: 1.00
Nodes (2): partition(), Return a partitioned copy of an array.      Creates a copy of the array and part

### Community 496 - "Community 496"
Cohesion: 1.00
Nodes (2): ptp(), Range of values (maximum - minimum) along an axis.      The name of the function

### Community 497 - "Community 497"
Cohesion: 1.00
Nodes (2): put(), Replaces specified elements of an array with given values.      The indexing wor

### Community 498 - "Community 498"
Cohesion: 1.00
Nodes (2): Return a sorted copy of an array.      Parameters     ----------     a : array_l, sort()

### Community 499 - "Community 499"
Cohesion: 1.00
Nodes (2): Return the sum along diagonals of the array.      If `a` is 2-D, the sum along i, trace()

### Community 500 - "Community 500"
Cohesion: 1.00
Nodes (2): r"""     Compute the standard deviation along the specified axis.      Returns t, std()

### Community 501 - "Community 501"
Cohesion: 1.00
Nodes (2): r"""     Compute the variance along the specified axis.      Returns the varianc, var()

### Community 502 - "Community 502"
Cohesion: 1.00
Nodes (2): busday_count(), busday_count(         begindates,         enddates,         weekmask='1111100',

### Community 503 - "Community 503"
Cohesion: 1.00
Nodes (2): busday_offset(), busday_offset(         dates,         offsets,         roll='raise',         wee

### Community 504 - "Community 504"
Cohesion: 1.00
Nodes (2): can_cast(), can_cast(from_, to, casting='safe')      Returns True if cast between data types

### Community 505 - "Community 505"
Cohesion: 1.00
Nodes (2): concatenate(), concatenate(         arrays,         /,         axis=0,         out=None,

### Community 506 - "Community 506"
Cohesion: 1.00
Nodes (2): copyto(), copyto(dst, src, casting='same_kind', where=True)      Copies values from one ar

### Community 507 - "Community 507"
Cohesion: 1.00
Nodes (2): datetime_as_string(), datetime_as_string(arr, unit=None, timezone='naive', casting='same_kind')      C

### Community 508 - "Community 508"
Cohesion: 1.00
Nodes (2): dot(), dot(a, b, out=None)      Dot product of two arrays. Specifically,      - If both

### Community 509 - "Community 509"
Cohesion: 1.00
Nodes (2): empty_like(), empty_like(         prototype,         /,         dtype=None,         order='K',

### Community 510 - "Community 510"
Cohesion: 1.00
Nodes (2): inner(), inner(a, b, /)      Inner product of two arrays.      Ordinary inner product of

### Community 511 - "Community 511"
Cohesion: 1.00
Nodes (2): is_busday(), is_busday(         dates,         weekmask='1111100',         holidays=None,

### Community 512 - "Community 512"
Cohesion: 1.00
Nodes (2): lexsort(), lexsort(keys, axis=-1)      Perform an indirect stable sort using a sequence of

### Community 513 - "Community 513"
Cohesion: 1.00
Nodes (2): may_share_memory(), may_share_memory(a, b, /, max_work=0)      Determine if two arrays might share m

### Community 514 - "Community 514"
Cohesion: 1.00
Nodes (2): min_scalar_type(), min_scalar_type(a, /)      For scalar ``a``, returns the data type with the smal

### Community 515 - "Community 515"
Cohesion: 1.00
Nodes (2): packbits(), packbits(a, /, axis=None, bitorder='big')      Packs the elements of a binary-va

### Community 516 - "Community 516"
Cohesion: 1.00
Nodes (2): putmask(), putmask(a, /, mask, values)      Changes elements of an array based on condition

### Community 517 - "Community 517"
Cohesion: 1.00
Nodes (2): unravel_index(indices, shape, order='C')      Converts a flat index or array of, unravel_index()

### Community 518 - "Community 518"
Cohesion: 1.00
Nodes (2): unpackbits(a, /, axis=None, count=None, bitorder='big')      Unpacks elements of, unpackbits()

### Community 519 - "Community 519"
Cohesion: 1.00
Nodes (2): shares_memory(a, b, /, max_work=-1)      Determine if two arrays share memory., shares_memory()

### Community 520 - "Community 520"
Cohesion: 1.00
Nodes (2): where(condition, [x, y], /)      Return elements chosen from `x` or `y` dependin, where()

### Community 521 - "Community 521"
Cohesion: 1.00
Nodes (2): result_type(*arrays_and_dtypes)      Returns the type that results from applying, result_type()

### Community 522 - "Community 522"
Cohesion: 1.00
Nodes (2): r"""     vdot(a, b, /)      Return the dot product of two vectors.      The `vdo, vdot()

### Community 524 - "Community 524"
Cohesion: 1.00
Nodes (2): Return an array of zeros with the same shape and type as a given array.      Par, zeros_like()

### Community 525 - "Community 525"
Cohesion: 1.00
Nodes (2): Roll the specified axis backwards, until it lies in a given position.      This, rollaxis()

### Community 526 - "Community 526"
Cohesion: 1.00
Nodes (2): Compute tensor dot product along specified axes.      Given two tensors, `a` and, tensordot()

### Community 527 - "Community 527"
Cohesion: 1.00
Nodes (1): Stores and defines the low-level format_options context variable.  This is defin

### Community 528 - "Community 528"
Cohesion: 1.00
Nodes (2): capitalize(), Return a copy of ``a`` with only the first character of each element     capital

### Community 529 - "Community 529"
Cohesion: 1.00
Nodes (2): center(), Return a copy of `a` with its elements centered in a string of     length `width

### Community 530 - "Community 530"
Cohesion: 1.00
Nodes (2): count(), Returns an array with the number of non-overlapping occurrences of     substring

### Community 531 - "Community 531"
Cohesion: 1.00
Nodes (2): endswith(), Returns a boolean array which is `True` where the string element     in ``a`` en

### Community 532 - "Community 532"
Cohesion: 1.00
Nodes (2): expandtabs(), Return a copy of each string element where all tab characters are     replaced b

### Community 533 - "Community 533"
Cohesion: 1.00
Nodes (2): find(), For each element, return the lowest index in the string where     substring ``su

### Community 534 - "Community 534"
Cohesion: 1.00
Nodes (2): index(), Like `find`, but raises :exc:`ValueError` when the substring is not found.

### Community 535 - "Community 535"
Cohesion: 1.00
Nodes (2): ljust(), Return an array with the elements of `a` left-justified in a     string of lengt

### Community 536 - "Community 536"
Cohesion: 1.00
Nodes (2): lower(), Return an array with the elements converted to lowercase.      Call :meth:`str.l

### Community 537 - "Community 537"
Cohesion: 1.00
Nodes (2): lstrip(), For each element in `a`, return a copy with the leading characters     removed.

### Community 538 - "Community 538"
Cohesion: 1.00
Nodes (2): multiply(), Return (a * i), that is string multiple concatenation,     element-wise.      Va

### Community 539 - "Community 539"
Cohesion: 1.00
Nodes (2): partition(), Partition each element in ``a`` around ``sep``.      For each element in ``a``,

### Community 540 - "Community 540"
Cohesion: 1.00
Nodes (2): For each element in `a`, return a copy with the leading and     trailing charact, strip()

### Community 541 - "Community 541"
Cohesion: 1.00
Nodes (2): Return an array with the elements converted to uppercase.      Calls :meth:`str., upper()

### Community 542 - "Community 542"
Cohesion: 1.00
Nodes (2): Return element-wise a copy of the string with     uppercase characters converted, swapcase()

### Community 543 - "Community 543"
Cohesion: 1.00
Nodes (2): Return element-wise title cased version of string or unicode.      Title case wo, title()

### Community 544 - "Community 544"
Cohesion: 1.00
Nodes (2): For each element in ``a``, return a copy of the string with     occurrences of s, replace()

### Community 545 - "Community 545"
Cohesion: 1.00
Nodes (2): Partition (split) each element around the right-most separator.      For each el, rpartition()

### Community 546 - "Community 546"
Cohesion: 1.00
Nodes (2): Slice the strings in `a` by slices specified by `start`, `stop`, `step`.     Lik, slice()

### Community 547 - "Community 547"
Cohesion: 1.00
Nodes (2): For each element, return the highest index in the string where     substring ``s, rfind()

### Community 548 - "Community 548"
Cohesion: 1.00
Nodes (2): Like `rfind`, but raises :exc:`ValueError` when the substring `sub` is     not f, rindex()

### Community 549 - "Community 549"
Cohesion: 1.00
Nodes (2): Returns a boolean array which is `True` where the string element     in ``a`` st, startswith()

### Community 550 - "Community 550"
Cohesion: 1.00
Nodes (2): Return an array with the elements of `a` right-justified in a     string of leng, rjust()

### Community 551 - "Community 551"
Cohesion: 1.00
Nodes (2): Return the numeric string left-filled with zeros. A leading     sign prefix (``+, zfill()

### Community 552 - "Community 552"
Cohesion: 1.00
Nodes (2): For each element in `a`, return a copy with the trailing characters     removed., rstrip()

### Community 553 - "Community 553"
Cohesion: 1.00
Nodes (1): Due to compatibility, numpy has a very large number of different naming conventi

### Community 555 - "Community 555"
Cohesion: 1.00
Nodes (1): Provide python-space access to the functions exposed in numpy/__init__.pxd for t

### Community 559 - "Community 559"
Cohesion: 1.00
Nodes (1): Distributor init file  Distributors: you can add custom code here to support par

### Community 560 - "Community 560"
Cohesion: 1.00
Nodes (1): =================== Universal Functions ===================  Ufuncs are, general

### Community 562 - "Community 562"
Cohesion: 1.00
Nodes (1): ISO_FORTRAN_ENV maps for f2py2e

### Community 564 - "Community 564"
Cohesion: 1.00
Nodes (2): blackman(), Return the Blackman window.      The Blackman window is a taper formed by using

### Community 565 - "Community 565"
Cohesion: 1.00
Nodes (2): _compute_virtual_index(), Compute the floating point indexes of an array for the linear     interpolation

### Community 566 - "Community 566"
Cohesion: 1.00
Nodes (2): digitize(), Return the indices of the bins to which each value in input array belongs.

### Community 567 - "Community 567"
Cohesion: 1.00
Nodes (2): extract(), Return the elements of an array that satisfy some condition.      This is equiva

### Community 568 - "Community 568"
Cohesion: 1.00
Nodes (2): hamming(), Return the Hamming window.      The Hamming window is a taper formed by using a

### Community 569 - "Community 569"
Cohesion: 1.00
Nodes (2): hanning(), Return the Hanning window.      The Hanning window is a taper formed by using a

### Community 570 - "Community 570"
Cohesion: 1.00
Nodes (2): insert(), Insert values along the given axis before the given indices.      Parameters

### Community 571 - "Community 571"
Cohesion: 1.00
Nodes (2): interp(), One-dimensional linear interpolation for monotonically increasing sample points.

### Community 572 - "Community 572"
Cohesion: 1.00
Nodes (2): place(), Change elements of an array based on conditional and input values.      Similar

### Community 573 - "Community 573"
Cohesion: 1.00
Nodes (2): Sort a complex array using the real part first, then the imaginary part.      Pa, _sort_complex()

### Community 574 - "Community 574"
Cohesion: 1.00
Nodes (2): r"""     Return the normalized sinc function.      The sinc function is equal to, sinc()

### Community 575 - "Community 575"
Cohesion: 1.00
Nodes (2): get_names_flat(), Returns the field names of the input datatype as a tuple. Input datatype     mus

### Community 576 - "Community 576"
Cohesion: 1.00
Nodes (2): _izip_fields_flat(), Returns an iterator of concatenated fields from a sequence of arrays,     collap

### Community 577 - "Community 577"
Cohesion: 1.00
Nodes (2): _izip_fields(), Returns an iterator of concatenated fields from a sequence of arrays.

### Community 578 - "Community 578"
Cohesion: 1.00
Nodes (2): Rename the fields from a flexible-datatype ndarray or recarray.      Nested fiel, rename_fields()

### Community 579 - "Community 579"
Cohesion: 1.00
Nodes (1): Build an example package using the limited Python C API.

### Community 582 - "Community 582"
Cohesion: 1.00
Nodes (2): _n_to_n_data_clone(), _n_to_n_data_free()

### Community 583 - "Community 583"
Cohesion: 1.00
Nodes (2): _one_to_n_data_clone(), _one_to_n_data_free()

### Community 584 - "Community 584"
Cohesion: 1.00
Nodes (2): _subarray_broadcast_data_clone(), _subarray_broadcast_data_free()

### Community 585 - "Community 585"
Cohesion: 1.00
Nodes (2): any_array_ufunc_overrides(), array_ufunc()

### Community 586 - "Community 586"
Cohesion: 1.00
Nodes (2): array_byteswap(), PyArray_Byteswap()

### Community 587 - "Community 587"
Cohesion: 1.00
Nodes (2): array_deepcopy(), _deepcopy_call()

### Community 588 - "Community 588"
Cohesion: 1.00
Nodes (2): array_reduce(), _getlist_pkl()

### Community 589 - "Community 589"
Cohesion: 1.00
Nodes (2): array_setstate(), _setlist_pkl()

### Community 590 - "Community 590"
Cohesion: 1.00
Nodes (2): array_tofile(), PyArray_ToFileObject()

### Community 591 - "Community 591"
Cohesion: 1.00
Nodes (2): array__get_ndarray_c_version(), PyArray_GetNDArrayCVersion()

### Community 592 - "Community 592"
Cohesion: 1.00
Nodes (2): array_where(), PyArray_Where()

### Community 593 - "Community 593"
Cohesion: 1.00
Nodes (2): PyArray_ScalarKind(), _signbit_set()

### Community 597 - "Community 597"
Cohesion: 1.00
Nodes (1): Test

### Community 598 - "Community 598"
Cohesion: 1.00
Nodes (1): Tests for :mod:`numpy._core.fromnumeric`.

### Community 599 - "Community 599"
Cohesion: 1.00
Nodes (1): Based on the `if __name__ == "__main__"` test code in `lib/_user_array_impl.py`.

### Community 601 - "Community 601"
Cohesion: 1.00
Nodes (1): # NOTE: __call__ is needed due to python/mypy#17620

### Community 602 - "Community 602"
Cohesion: 1.00
Nodes (1): # NOTE: `np.generic` subclasses are not guaranteed to support addition;

### Community 607 - "Community 607"
Cohesion: 1.00
Nodes (2): _no_tracing(), Decorator to temporarily turn off tracing for the duration of a test.     Needed

### Community 608 - "Community 608"
Cohesion: 1.00
Nodes (2): print_assert_equal(), Test if two objects are equal, and print an error message if test fails.      Th

### Community 609 - "Community 609"
Cohesion: 1.00
Nodes (2): Run doctests found in the given file.      By default `rundocs` raises an Assert, rundocs()

### Community 610 - "Community 610"
Cohesion: 1.00
Nodes (2): Context manager to provide a temporary test folder.      All arguments are passe, tempdir()

### Community 611 - "Community 611"
Cohesion: 1.00
Nodes (2): Context manager for temporary files.      Context manager that returns the path, temppath()

### Community 612 - "Community 612"
Cohesion: 1.00
Nodes (2): Decorator to skip a test if not enough memory is available, requires_memory()

### Community 613 - "Community 613"
Cohesion: 1.00
Nodes (2): Runs a function many times in parallel, run_threaded()

### Community 614 - "Community 614"
Cohesion: 1.00
Nodes (2): Decorator to skip test if deep recursion is not supported., requires_deep_recursion()

### Community 615 - "Community 615"
Cohesion: 1.00
Nodes (2): Run ``cmd`` in a subprocess, failing the test with its captured output     if it, run_subprocess()

### Community 616 - "Community 616"
Cohesion: 1.00
Nodes (1): This hook should collect all binary files and any hidden modules that numpy need

### Community 620 - "Community 620"
Cohesion: 1.00
Nodes (1): Common test support for all numpy test scripts.  This single module should provi

### Community 621 - "Community 621"
Cohesion: 1.00
Nodes (1): A crude *bit of everything* smoke test to verify PyInstaller compatibility.  PyI

### Community 623 - "Community 623"
Cohesion: 1.00
Nodes (1): A module with the precisions of platform-specific `~numpy.number`s.

### Community 624 - "Community 624"
Cohesion: 1.00
Nodes (1): # NOTE: `_StrLike_co` and `_BytesLike_co` are pointless, as `np.str_` and

## Knowledge Gaps
- **1344 isolated node(s):** `Array API Inspection namespace  This is the namespace for inspection functions a`, `Get the array API inspection namespace for NumPy.      The array API inspection`, `Return a dictionary of array API library capabilities.          The resulting di`, `The default device used for new NumPy arrays.          For NumPy, this always re`, `The default data types used for new NumPy arrays.          For NumPy, this alway` (+1339 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 43`** (1 nodes): `Module containing non-deprecated functions borrowed from Numeric.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 142`** (1 nodes): `These tests are based on the doctests from `numpy/lib/recfunctions.py`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 145`** (2 nodes): `byte_to_true()`, `simd_logical_or_u8()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 153`** (1 nodes): `This module contains a set of functions for vectorized string operations.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 162`** (2 nodes): `pow_zi()`, `z_div()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 174`** (2 nodes): `initialize_abstract_dtypes()`, `make_raw_dtype()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 184`** (2 nodes): `MaskedConstant`, `Override of MaskedArray's __reduce__.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 202`** (1 nodes): `NAType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 208`** (2 nodes): `array_converter_wrap()`, `find_wrap()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 209`** (1 nodes): `Object`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 222`** (2 nodes): `busdaycalendar_init()`, `normalize_holidays_list()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 229`** (1 nodes): `Infinity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 231`** (1 nodes): `NegativeInfinity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 243`** (1 nodes): `_BaseVersion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 262`** (2 nodes): `get_initial_from_ufunc()`, `PyArray_NewLegacyWrappingArrayMethod()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 264`** (2 nodes): `get_wrapping_auxdata()`, `wrapping_method_get_loop()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 265`** (1 nodes): `Version`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 269`** (2 nodes): `dict`, `bunch`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 277`** (1 nodes): `Object`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 281`** (1 nodes): `_Empty`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 282`** (1 nodes): `TemplateDef`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 283`** (2 nodes): `TemplateObject`, `TemplateObjectGetter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 289`** (1 nodes): `dummy_ctype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 306`** (2 nodes): `init_genrand()`, `mt19937_init_by_array()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 312`** (2 nodes): `bounded_uint()`, `bounded_uints()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 323`** (1 nodes): `BoolValuesApi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 324`** (1 nodes): `GlobalVarApi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 325`** (1 nodes): `TypeApi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 339`** (2 nodes): `Index`, `SubClass`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 341`** (2 nodes): `clear_and_catch_warnings`, `Context manager that resets warning registry for catching warnings      Warnings`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 348`** (2 nodes): `MinVersion`, `Version should be the normal NumPy version, e.g. "1.25"`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 354`** (2 nodes): `npy_longdouble_from_PyLong()`, `_PyLong_Bytes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 355`** (2 nodes): `PyUFunc_HasOverride()`, `PyUFuncOverride_GetNonDefaultArrayUfunc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 377`** (2 nodes): `polysub()`, `Difference (subtraction) of two polynomials.      .. note::        This forms pa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 380`** (1 nodes): `Mapping`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 381`** (2 nodes): `Return `self` as a flattened `ndarray`.          Equivalent to ``np.asarray(x).r`, `Return a flattened matrix.          Refer to `numpy.ravel` for more documentatio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 393`** (1 nodes): `Simple expression that should pass with mypy.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 402`** (1 nodes): `A set of methods retained from np.compat module that are still used across codeb`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 404`** (2 nodes): `parse_distributions_h()`, `Parse distributions.h located in inc_dir for CFFI, filling in the ffi.cdef`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 406`** (2 nodes): `accumulate()`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 407`** (1 nodes): `StealRef`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 408`** (1 nodes): `Docstrings for generated ufuncs  The syntax is designed to look like the functio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 413`** (1 nodes): `Create the numpy._core.umath namespace for backward compatibility. In v1.16 the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 414`** (2 nodes): `ISO_C_BINDING maps for f2py2e. Only required declarations/macros/functions will`, `# TODO: See gh-25229`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 416`** (2 nodes): `byte_bounds()`, `Returns pointers to the end-points of an array.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 417`** (2 nodes): `polyval()`, `Evaluate a polynomial at specific values.      .. note::        This forms part`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 418`** (2 nodes): `poly()`, `Find the coefficients of a polynomial with the given sequence of roots.      ..`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 423`** (1 nodes): `r""" Building the required library in this example requires a source distributio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 424`** (1 nodes): `A`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 425`** (2 nodes): `Tests for :mod:`numpy._core.numeric`.  Does not include tests which fall under ``, `SubClass`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 427`** (2 nodes): `create_conv_funcs()`, `read_rows()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 431`** (1 nodes): `Use cffi to access any of the underlying C functions from distributions.h`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 477`** (1 nodes): `For each element in `self`, return True if there are only         numeric charac`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 478`** (1 nodes): `Returns true for each element if there are only whitespace         characters in`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 479`** (1 nodes): `Returns true for each element if the element is a titlecased         string and`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 480`** (1 nodes): `Returns true for each element if all cased characters in the         string are`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 481`** (1 nodes): `Return a string which is the concatenation of the strings in the         sequenc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 482`** (1 nodes): `For each element in `self`, return a copy with the leading characters         re`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 483`** (1 nodes): `Return (other + self), that is string concatenation,         element-wise for a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 484`** (1 nodes): `For each element in `self`, return a copy of the string with all         occurre`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 485`** (1 nodes): `For each element in `self`, return the highest index in the string         where`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 486`** (1 nodes): `Like `rfind`, but raises :exc:`ValueError` when the substring `sub` is         n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 487`** (1 nodes): `For each element in `self`, return a list of the words in         the string, us`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 488`** (1 nodes): `For each element in `self`, return a list of the words in the         string, us`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 489`** (1 nodes): `For each element in `self`, return a list of the lines in the         element, b`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 490`** (1 nodes): `Returns a boolean array which is `True` where the string element         in `sel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 491`** (1 nodes): `For each element in `self`, return a copy with the leading and         trailing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 492`** (2 nodes): `diagonal()`, `Return specified diagonals.      If `a` is 2-D, returns the diagonal of `a` with`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 493`** (2 nodes): `mean()`, `Compute the arithmetic mean along the specified axis.      Returns the average o`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 494`** (2 nodes): `ndim()`, `Return the number of dimensions of an array.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 495`** (2 nodes): `partition()`, `Return a partitioned copy of an array.      Creates a copy of the array and part`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 496`** (2 nodes): `ptp()`, `Range of values (maximum - minimum) along an axis.      The name of the function`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 497`** (2 nodes): `put()`, `Replaces specified elements of an array with given values.      The indexing wor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 498`** (2 nodes): `Return a sorted copy of an array.      Parameters     ----------     a : array_l`, `sort()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 499`** (2 nodes): `Return the sum along diagonals of the array.      If `a` is 2-D, the sum along i`, `trace()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 500`** (2 nodes): `r"""     Compute the standard deviation along the specified axis.      Returns t`, `std()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 501`** (2 nodes): `r"""     Compute the variance along the specified axis.      Returns the varianc`, `var()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 502`** (2 nodes): `busday_count()`, `busday_count(         begindates,         enddates,         weekmask='1111100',`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 503`** (2 nodes): `busday_offset()`, `busday_offset(         dates,         offsets,         roll='raise',         wee`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 504`** (2 nodes): `can_cast()`, `can_cast(from_, to, casting='safe')      Returns True if cast between data types`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 505`** (2 nodes): `concatenate()`, `concatenate(         arrays,         /,         axis=0,         out=None,`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 506`** (2 nodes): `copyto()`, `copyto(dst, src, casting='same_kind', where=True)      Copies values from one ar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 507`** (2 nodes): `datetime_as_string()`, `datetime_as_string(arr, unit=None, timezone='naive', casting='same_kind')      C`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 508`** (2 nodes): `dot()`, `dot(a, b, out=None)      Dot product of two arrays. Specifically,      - If both`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 509`** (2 nodes): `empty_like()`, `empty_like(         prototype,         /,         dtype=None,         order='K',`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 510`** (2 nodes): `inner()`, `inner(a, b, /)      Inner product of two arrays.      Ordinary inner product of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 511`** (2 nodes): `is_busday()`, `is_busday(         dates,         weekmask='1111100',         holidays=None,`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 512`** (2 nodes): `lexsort()`, `lexsort(keys, axis=-1)      Perform an indirect stable sort using a sequence of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 513`** (2 nodes): `may_share_memory()`, `may_share_memory(a, b, /, max_work=0)      Determine if two arrays might share m`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 514`** (2 nodes): `min_scalar_type()`, `min_scalar_type(a, /)      For scalar ``a``, returns the data type with the smal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 515`** (2 nodes): `packbits()`, `packbits(a, /, axis=None, bitorder='big')      Packs the elements of a binary-va`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 516`** (2 nodes): `putmask()`, `putmask(a, /, mask, values)      Changes elements of an array based on condition`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 517`** (2 nodes): `unravel_index(indices, shape, order='C')      Converts a flat index or array of`, `unravel_index()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 518`** (2 nodes): `unpackbits(a, /, axis=None, count=None, bitorder='big')      Unpacks elements of`, `unpackbits()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 519`** (2 nodes): `shares_memory(a, b, /, max_work=-1)      Determine if two arrays share memory.`, `shares_memory()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 520`** (2 nodes): `where(condition, [x, y], /)      Return elements chosen from `x` or `y` dependin`, `where()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 521`** (2 nodes): `result_type(*arrays_and_dtypes)      Returns the type that results from applying`, `result_type()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 522`** (2 nodes): `r"""     vdot(a, b, /)      Return the dot product of two vectors.      The `vdo`, `vdot()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 524`** (2 nodes): `Return an array of zeros with the same shape and type as a given array.      Par`, `zeros_like()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 525`** (2 nodes): `Roll the specified axis backwards, until it lies in a given position.      This`, `rollaxis()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 526`** (2 nodes): `Compute tensor dot product along specified axes.      Given two tensors, `a` and`, `tensordot()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 527`** (1 nodes): `Stores and defines the low-level format_options context variable.  This is defin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 528`** (2 nodes): `capitalize()`, `Return a copy of ``a`` with only the first character of each element     capital`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 529`** (2 nodes): `center()`, `Return a copy of `a` with its elements centered in a string of     length `width`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 530`** (2 nodes): `count()`, `Returns an array with the number of non-overlapping occurrences of     substring`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 531`** (2 nodes): `endswith()`, `Returns a boolean array which is `True` where the string element     in ``a`` en`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 532`** (2 nodes): `expandtabs()`, `Return a copy of each string element where all tab characters are     replaced b`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 533`** (2 nodes): `find()`, `For each element, return the lowest index in the string where     substring ``su`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 534`** (2 nodes): `index()`, `Like `find`, but raises :exc:`ValueError` when the substring is not found.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 535`** (2 nodes): `ljust()`, `Return an array with the elements of `a` left-justified in a     string of lengt`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 536`** (2 nodes): `lower()`, `Return an array with the elements converted to lowercase.      Call :meth:`str.l`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 537`** (2 nodes): `lstrip()`, `For each element in `a`, return a copy with the leading characters     removed.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 538`** (2 nodes): `multiply()`, `Return (a * i), that is string multiple concatenation,     element-wise.      Va`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 539`** (2 nodes): `partition()`, `Partition each element in ``a`` around ``sep``.      For each element in ``a``,`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 540`** (2 nodes): `For each element in `a`, return a copy with the leading and     trailing charact`, `strip()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 541`** (2 nodes): `Return an array with the elements converted to uppercase.      Calls :meth:`str.`, `upper()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 542`** (2 nodes): `Return element-wise a copy of the string with     uppercase characters converted`, `swapcase()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 543`** (2 nodes): `Return element-wise title cased version of string or unicode.      Title case wo`, `title()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 544`** (2 nodes): `For each element in ``a``, return a copy of the string with     occurrences of s`, `replace()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 545`** (2 nodes): `Partition (split) each element around the right-most separator.      For each el`, `rpartition()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 546`** (2 nodes): `Slice the strings in `a` by slices specified by `start`, `stop`, `step`.     Lik`, `slice()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 547`** (2 nodes): `For each element, return the highest index in the string where     substring ``s`, `rfind()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 548`** (2 nodes): `Like `rfind`, but raises :exc:`ValueError` when the substring `sub` is     not f`, `rindex()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 549`** (2 nodes): `Returns a boolean array which is `True` where the string element     in ``a`` st`, `startswith()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 550`** (2 nodes): `Return an array with the elements of `a` right-justified in a     string of leng`, `rjust()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 551`** (2 nodes): `Return the numeric string left-filled with zeros. A leading     sign prefix (``+`, `zfill()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 552`** (2 nodes): `For each element in `a`, return a copy with the trailing characters     removed.`, `rstrip()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 553`** (1 nodes): `Due to compatibility, numpy has a very large number of different naming conventi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 555`** (1 nodes): `Provide python-space access to the functions exposed in numpy/__init__.pxd for t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 559`** (1 nodes): `Distributor init file  Distributors: you can add custom code here to support par`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 560`** (1 nodes): `=================== Universal Functions ===================  Ufuncs are, general`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 562`** (1 nodes): `ISO_FORTRAN_ENV maps for f2py2e`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 564`** (2 nodes): `blackman()`, `Return the Blackman window.      The Blackman window is a taper formed by using`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 565`** (2 nodes): `_compute_virtual_index()`, `Compute the floating point indexes of an array for the linear     interpolation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 566`** (2 nodes): `digitize()`, `Return the indices of the bins to which each value in input array belongs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 567`** (2 nodes): `extract()`, `Return the elements of an array that satisfy some condition.      This is equiva`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 568`** (2 nodes): `hamming()`, `Return the Hamming window.      The Hamming window is a taper formed by using a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 569`** (2 nodes): `hanning()`, `Return the Hanning window.      The Hanning window is a taper formed by using a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 570`** (2 nodes): `insert()`, `Insert values along the given axis before the given indices.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 571`** (2 nodes): `interp()`, `One-dimensional linear interpolation for monotonically increasing sample points.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 572`** (2 nodes): `place()`, `Change elements of an array based on conditional and input values.      Similar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 573`** (2 nodes): `Sort a complex array using the real part first, then the imaginary part.      Pa`, `_sort_complex()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 574`** (2 nodes): `r"""     Return the normalized sinc function.      The sinc function is equal to`, `sinc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 575`** (2 nodes): `get_names_flat()`, `Returns the field names of the input datatype as a tuple. Input datatype     mus`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 576`** (2 nodes): `_izip_fields_flat()`, `Returns an iterator of concatenated fields from a sequence of arrays,     collap`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 577`** (2 nodes): `_izip_fields()`, `Returns an iterator of concatenated fields from a sequence of arrays.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 578`** (2 nodes): `Rename the fields from a flexible-datatype ndarray or recarray.      Nested fiel`, `rename_fields()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 579`** (1 nodes): `Build an example package using the limited Python C API.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 582`** (2 nodes): `_n_to_n_data_clone()`, `_n_to_n_data_free()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 583`** (2 nodes): `_one_to_n_data_clone()`, `_one_to_n_data_free()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 584`** (2 nodes): `_subarray_broadcast_data_clone()`, `_subarray_broadcast_data_free()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 585`** (2 nodes): `any_array_ufunc_overrides()`, `array_ufunc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 586`** (2 nodes): `array_byteswap()`, `PyArray_Byteswap()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 587`** (2 nodes): `array_deepcopy()`, `_deepcopy_call()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 588`** (2 nodes): `array_reduce()`, `_getlist_pkl()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 589`** (2 nodes): `array_setstate()`, `_setlist_pkl()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 590`** (2 nodes): `array_tofile()`, `PyArray_ToFileObject()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 591`** (2 nodes): `array__get_ndarray_c_version()`, `PyArray_GetNDArrayCVersion()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 592`** (2 nodes): `array_where()`, `PyArray_Where()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 593`** (2 nodes): `PyArray_ScalarKind()`, `_signbit_set()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 597`** (1 nodes): `Test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 598`** (1 nodes): `Tests for :mod:`numpy._core.fromnumeric`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 599`** (1 nodes): `Based on the `if __name__ == "__main__"` test code in `lib/_user_array_impl.py`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 601`** (1 nodes): `# NOTE: __call__ is needed due to python/mypy#17620`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 602`** (1 nodes): `# NOTE: `np.generic` subclasses are not guaranteed to support addition;`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 607`** (2 nodes): `_no_tracing()`, `Decorator to temporarily turn off tracing for the duration of a test.     Needed`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 608`** (2 nodes): `print_assert_equal()`, `Test if two objects are equal, and print an error message if test fails.      Th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 609`** (2 nodes): `Run doctests found in the given file.      By default `rundocs` raises an Assert`, `rundocs()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 610`** (2 nodes): `Context manager to provide a temporary test folder.      All arguments are passe`, `tempdir()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 611`** (2 nodes): `Context manager for temporary files.      Context manager that returns the path`, `temppath()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 612`** (2 nodes): `Decorator to skip a test if not enough memory is available`, `requires_memory()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 613`** (2 nodes): `Runs a function many times in parallel`, `run_threaded()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 614`** (2 nodes): `Decorator to skip test if deep recursion is not supported.`, `requires_deep_recursion()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 615`** (2 nodes): `Run ``cmd`` in a subprocess, failing the test with its captured output     if it`, `run_subprocess()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 616`** (1 nodes): `This hook should collect all binary files and any hidden modules that numpy need`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 620`** (1 nodes): `Common test support for all numpy test scripts.  This single module should provi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 621`** (1 nodes): `A crude *bit of everything* smoke test to verify PyInstaller compatibility.  PyI`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 623`** (1 nodes): `A module with the precisions of platform-specific `~numpy.number`s.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 624`** (1 nodes): `# NOTE: `_StrLike_co` and `_BytesLike_co` are pointless, as `np.str_` and`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `PytestTester` connect `Community 78` to `Community 31`, `Community 218`, `Community 68`, `Community 116`, `Community 343`, `Community 620`, `Community 159`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Why does `ABCPolyBase` connect `Community 5` to `Community 116`, `Community 13`, `Community 23`, `Community 24`, `Community 26`, `Community 27`, `Community 19`, `Community 30`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `MaskedArray` connect `Community 11` to `Community 2`, `Community 20`, `Community 14`, `Community 69`, `Community 70`, `Community 37`, `Community 139`, `Community 184`, `Community 4`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 184 inferred relationships involving `ABCPolyBase` (e.g. with `Chebyshev` and `==================================================== Chebyshev Series (:mod:`num`) actually correct?**
  _`ABCPolyBase` has 184 INFERRED edges - model-reasoned connections that need verification._
- **Are the 45 inferred relationships involving `MaskedArray` (e.g. with `MAxisConcatenator` and `mr_class`) actually correct?**
  _`MaskedArray` has 45 INFERRED edges - model-reasoned connections that need verification._
- **Are the 22 inferred relationships involving `matrix` (e.g. with `Kronecker product of two arrays.      Computes the Kronecker product, a composit` and `Construct an array by repeating A the number of times given by reps.      If `re`) actually correct?**
  _`matrix` has 22 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Array API Inspection namespace  This is the namespace for inspection functions a`, `Get the array API inspection namespace for NumPy.      The array API inspection`, `Return a dictionary of array API library capabilities.          The resulting di` to the rest of the system?**
  _1344 weakly-connected nodes found - possible documentation gaps or missing edges._