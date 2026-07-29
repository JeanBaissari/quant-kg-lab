# Graph Report - .  (2026-07-29)

## Corpus Check
- cluster-only mode - file stats not available

## Summary
- 20436 nodes · 30581 edges · 1227 communities detected
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 2203 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: contains: 9515 · method: 8459 · calls: 7127 · rationale_for: 2608 · uses: 2203 · inherits: 558 · imports_from: 92 · imports: 19


## Graph Freshness
- Built from Git commit: `ab21997`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `AxisError` - 420 edges
2. `TestRegression` - 339 edges
3. `ABCPolyBase` - 245 edges
4. `MaskedArray` - 213 edges
5. `Benchmark` - 206 edges
6. `ComplexWarning` - 171 edges
7. `TestUfunc` - 147 edges
8. `TestMethods` - 131 edges
9. `TestDateTime` - 129 edges
10. `CommaDecimalPointLocale` - 120 edges

## Surprising Connections (you probably didn't know these)
- `Template meson build file generation class.` --uses--> `Backend`  [INFERRED]
  numpy/f2py/_backends/_meson.py → numpy/f2py/_backends/_backend.py
- `Benchmarks for the NumPy small-allocation cache.  NumPy caches data allocations` --uses--> `Benchmark`  [INFERRED]
  benchmarks/benchmarks/bench_alloc_cache.py → benchmarks/benchmarks/common.py
- `A magical feature score for each feature in each dataset         :ref:`Haxby et` --uses--> `Benchmark`  [INFERRED]
  benchmarks/benchmarks/bench_app.py → benchmarks/benchmarks/common.py
- `Benchmark meshgrid generation` --uses--> `Benchmark`  [INFERRED]
  benchmarks/benchmarks/bench_creation.py → benchmarks/benchmarks/common.py
- `Cast datetime64 to a coarser calendar unit (Y/M/W).     Y and M require year/mon` --uses--> `Benchmark`  [INFERRED]
  benchmarks/benchmarks/bench_datetime.py → benchmarks/benchmarks/common.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.01
Nodes (1): TestRegression

### Community 1 - "Community 1"
Cohesion: 0.02
Nodes (198): allclose(), allequal(), array(), _arraymethod(), asanyarray(), asarray(), _check_fill_value(), _check_mask_axis() (+190 more)

### Community 2 - "Community 2"
Cohesion: 0.01
Nodes (64): CommaDecimalPointLocale, Sets LC_NUMERIC to a locale with comma as decimal point.      Classes derived fr, assert_arg_sorted(), assert_arr_partitioned(), Bar, Foo, Other, # NOTE: Because Py2 str/Py3 bytes supports the buffer interface, setting (+56 more)

### Community 3 - "Community 3"
Cohesion: 0.02
Nodes (41): A, get_mat(), _make_complex(), PhysicalQuantity2, Construct an input/output test pair for trim_zeros, # TODO: Note that times have dubious rounding as of fixing NaTs!, # TODO: Median does not support Datetime, due to `mean`., Like real + 1j * imag, but behaves as expected when imag contains non-finite (+33 more)

### Community 4 - "Community 4"
Cohesion: 0.01
Nodes (1): TestUfunc

### Community 5 - "Community 5"
Cohesion: 0.05
Nodes (122): dbdsdc_(), dbdsqr_(), dgebak_(), dgebal_(), dgebd2_(), dgebrd_(), dgeev_(), dgehd2_() (+114 more)

### Community 6 - "Community 6"
Cohesion: 0.05
Nodes (122): sbdsdc_(), sbdsqr_(), sgebak_(), sgebal_(), sgebd2_(), sgebrd_(), sgeev_(), sgehd2_() (+114 more)

### Community 7 - "Community 7"
Cohesion: 0.05
Nodes (82): DataSource, DataSource(destpath='.')      A generic data source file (file, http, ftp, ...)., ConversionWarning, ConverterError, ConverterLockError, _decode_line(), easy_dtype(), flatten_dtype() (+74 more)

### Community 8 - "Community 8"
Cohesion: 0.02
Nodes (2): TestBroadcast, TestRandomDist

### Community 9 - "Community 9"
Cohesion: 0.03
Nodes (26): MAError, MaskError, mvoid, Class for masked array related errors., Class for mask related errors., Return the next value, or raise StopIteration.          Examples         -------, Fake a 'void' object to use for masked array with structured dtypes., Defines an iterator for mvoid (+18 more)

### Community 10 - "Community 10"
Cohesion: 0.03
Nodes (78): allclose(), argwhere(), array_equal(), array_equiv(), astype(), base_repr(), binary_repr(), convolve() (+70 more)

### Community 11 - "Community 11"
Cohesion: 0.02
Nodes (1): TestDateTime

### Community 12 - "Community 12"
Cohesion: 0.04
Nodes (6): Ensure that fromhex is only used for values with the correct prefix and, Ensure that the exception message raised during failed floating point         co, strptime(), TestFromTxt, TestLoadTxt, TextIO

### Community 13 - "Community 13"
Cohesion: 0.03
Nodes (45): DeprecationWarning, get_include(), Fortran to Python Interface Generator.  Copyright 1999 -- 2011 Pearu Peterson al, Return the directory that contains the ``fortranobject.c`` and ``.h`` files., ComplexWarning, ModuleDeprecationWarning, Exceptions and Warnings =======================  General exceptions used by NumP, The warning raised when casting a complex dtype to a real dtype.      As impleme (+37 more)

### Community 14 - "Community 14"
Cohesion: 0.05
Nodes (74): abs2(), addUfuncs(), call_evd(), call_geev(), call_gelsd(), call_geqrf(), call_gesdd(), call_gesv() (+66 more)

### Community 15 - "Community 15"
Cohesion: 0.04
Nodes (42): Benchmark, ClipFloat, ClipInteger, SearchSorted, TrimZeros, ArgPack, ArgParsing, ArgParsingReduce (+34 more)

### Community 16 - "Community 16"
Cohesion: 0.02
Nodes (1): # NOTE: This is true even for a reduction, where we return a 0-stride

### Community 17 - "Community 17"
Cohesion: 0.03
Nodes (42): MaskedArray, MaskedConstant, An array class with possibly masked values.      Masked values of True exclude t, Force the mask to hard, preventing unmasking by assignment.          Whether the, Force the mask to soft (default), allowing unmasking by assignment.          Whe, Specifies whether values can be unmasked through assignments.          By defaul, Copy the mask and set the `sharedmask` flag to ``False``.          Whether the m, Share status of the mask (read-only). (+34 more)

### Community 18 - "Community 18"
Cohesion: 0.02
Nodes (16): Tests suite for MaskedArray. Adapted from the original test_ma by Pierre Gerard-, test the examples given in the docstring of ma.median, TestApplyAlongAxis, TestApplyOverAxes, TestArraySetOps, TestAverage, TestCompressFunctions, TestConcatenator (+8 more)

### Community 19 - "Community 19"
Cohesion: 0.04
Nodes (90): AxisConcatenator, AxisConcatenator, Translates slice objects to concatenation along an axis.      For detailed docum, apply_along_axis(), apply_over_axes(), average(), clump_masked(), clump_unmasked() (+82 more)

### Community 20 - "Community 20"
Cohesion: 0.03
Nodes (27): ABCPolyBase, Return series instance that has the specified roots.          Returns a series r, Identity function.          If ``p`` is the returned series, then ``p(x) == x``, Series basis polynomial of degree `deg`.          Returns the series representin, Convert series to series of this class.          The `series` is expected to be, Check if coefficients match.          Parameters         ----------         othe, Check if domains match.          Parameters         ----------         other : c, An abstract base class for immutable series classes.      ABCPolyBase provides t (+19 more)

### Community 21 - "Community 21"
Cohesion: 0.02
Nodes (15): call_func(), _make_distinct_arena_arrays(), Make two arrays with distinct dtype instances and equal arena layouts.      All, test_assignment_distinct_allocators(), test_binary(), test_choose_distinct_allocators(), test_concatenate_distinct_allocators(), test_flat_assignment_distinct_allocators() (+7 more)

### Community 22 - "Community 22"
Cohesion: 0.05
Nodes (81): analyzeargs(), analyzebody(), analyzecommon(), analyzeline(), analyzevars(), appenddecl(), appendmultiline(), buildimplicitrules() (+73 more)

### Community 23 - "Community 23"
Cohesion: 0.05
Nodes (75): bounded_lemire_uint64(), bounded_masked_uint64(), buffered_bounded_bool(), buffered_bounded_lemire_uint16(), buffered_bounded_lemire_uint32(), buffered_bounded_lemire_uint8(), buffered_bounded_masked_uint16(), buffered_bounded_masked_uint32() (+67 more)

### Community 24 - "Community 24"
Cohesion: 0.02
Nodes (1): TestMethods

### Community 25 - "Community 25"
Cohesion: 0.07
Nodes (83): cgebak_(), cgebal_(), cgebd2_(), cgebrd_(), cgeev_(), cgehd2_(), cgehrd_(), cgelq2_() (+75 more)

### Community 26 - "Community 26"
Cohesion: 0.07
Nodes (83): zgebak_(), zgebal_(), zgebd2_(), zgebrd_(), zgeev_(), zgehd2_(), zgehrd_(), zgelq2_() (+75 more)

### Community 27 - "Community 27"
Cohesion: 0.03
Nodes (26): check_ufunc_scalar_equivalence(), # TODO: It would be nice to resolve this issue., This test covers scalar subclass deferral.  Note that this is exceedingly     co, # TODO: Power is a bit special, but here mostly bools seem to behave oddly, This is a thorough test attempting to cover important promotion paths     and en, recursionlimit(), _signs(), test_array_scalar_ufunc_dtypes() (+18 more)

### Community 28 - "Community 28"
Cohesion: 0.03
Nodes (2): TestBroadcast, TestRandomDist

### Community 30 - "Community 30"
Cohesion: 0.03
Nodes (2): TestMaskedArrayFunctions, TestMaskedArrayMethods

### Community 31 - "Community 31"
Cohesion: 0.03
Nodes (71): cheb2poly(), chebadd(), chebcompanion(), chebder(), chebdiv(), chebfit(), chebfromroots(), chebgauss() (+63 more)

### Community 32 - "Community 32"
Cohesion: 0.03
Nodes (2): TestMaskedArray, TestMaskedConstant

### Community 33 - "Community 33"
Cohesion: 0.05
Nodes (52): array_protocol_descr_get(), array_typestr_get(), arraydescr_field_subset_view(), _arraydescr_isnative(), arraydescr_isnative_get(), arraydescr_new(), arraydescr_newbyteorder(), arraydescr_protocol_descr_get() (+44 more)

### Community 34 - "Community 34"
Cohesion: 0.04
Nodes (2): TestBroadcast, TestRandomDist

### Community 35 - "Community 35"
Cohesion: 0.06
Nodes (62): add_minutes_to_datetimestruct(), add_seconds_to_datetimestruct(), can_cast_datetime64_metadata(), can_cast_datetime64_units(), can_cast_timedelta64_metadata(), can_cast_timedelta64_units(), cast_datetime_to_datetime(), cast_timedelta_to_timedelta() (+54 more)

### Community 36 - "Community 36"
Cohesion: 0.03
Nodes (2): Tests specific to `np.loadtxt` added during the move of loadtxt to be backed by, # NOTE: It is unclear that the `  # comment` should succeed. Except

### Community 37 - "Community 37"
Cohesion: 0.05
Nodes (25): BytesIO, assert_equal_(), BytesIOSRandomSize, roundtrip(), roundtrip_randsize(), roundtrip_truncated(), test_bad_header(), test_descr_to_dtype() (+17 more)

### Community 38 - "Community 38"
Cohesion: 0.03
Nodes (33): # FIXME: NAN raises FP invalid exception:, # FIXME: a not used, # NOTE: this class is used in doc/source/user/basics.subclassing.rst, `nextafter(-0.0, +0.0)` must return the sign of the second parameter, Check np.nan is a positive nan., #31421 abs(nan) preserves positive sign bit correctly., #31421 abs(nan) array preserves positive sign bit correctly., Test bug in reduceat when structured arrays are not copied. (+25 more)

### Community 39 - "Community 39"
Cohesion: 0.12
Nodes (49): CondCases, DetCases, EigCases, EigvalsCases, InvCases, LinalgTestCase, LstsqCases, PinvCases (+41 more)

### Community 40 - "Community 40"
Cohesion: 0.05
Nodes (3): container, Container class for backward compatibility with NumArray.  The user_array.contai, container(data, dtype=None, copy=True)      Standard container-class for easy mu

### Community 41 - "Community 41"
Cohesion: 0.07
Nodes (54): byteswap(), d(), gcd(), lcm(), make_rational_fast(), make_rational_int(), make_rational_slow(), npyrational_compare() (+46 more)

### Community 42 - "Community 42"
Cohesion: 0.04
Nodes (31): asmatrix(), bmat(), _convert_from_string(), _from_string(), matrix, Build a matrix object from a string, nested sequence, or array.      Parameters, A convenience function for operations that need to preserve axis         orienta, A convenience function for operations that want to collapse         to a scalar (+23 more)

### Community 43 - "Community 43"
Cohesion: 0.05
Nodes (5): Most einsum operations are reductions and until NumPy 2.3 reductions     never (, # NOTE: This test is triggered by the fact that the default buffersize,, test_einsum_chunking_precision(), TestEinsum, TestEinsumPath

### Community 44 - "Community 44"
Cohesion: 0.04
Nodes (4): Check that we return subclasses, even if a NaN scalar., TestMedian, TestPercentile, TestQuantile

### Community 45 - "Community 45"
Cohesion: 0.12
Nodes (3): assert_array_strict_equal(), A property-based test using Hypothesis.          This aims for maximum generalit, TestClip

### Community 47 - "Community 47"
Cohesion: 0.04
Nodes (9): Eindot, Einsum, Linalg, LinalgNorm, LinalgSmallArrays, LinAlgTransposeVdot, Lstsq, MatmulStrided (+1 more)

### Community 48 - "Community 48"
Cohesion: 0.06
Nodes (22): NDArrayOperatorsMixin, Mixin defining all operator special methods using __array_ufunc__.      This cla, NDArrayOperatorsMixin, ArrayNoInheritance, assert_startswith(), ComplicatedSubArray, CSAIterator, MSubArray (+14 more)

### Community 49 - "Community 49"
Cohesion: 0.07
Nodes (53): _arange_safe_ceil_to_intp(), _array_fill_strides(), _array_from_array_like(), _array_from_buffer_3118(), array_from_text(), array_fromfile_binary(), byte_swap_vector(), _calc_length() (+45 more)

### Community 50 - "Community 50"
Cohesion: 0.05
Nodes (33): npyv_load2_tillz_s32(), npyv_load_till_s32(), npyv_load_till_s64(), npyv_load_tillz_s32(), npyv_load_tillz_s64(), npyv__loadl(), npyv_loadn2_s32(), npyv_loadn2_till_s32() (+25 more)

### Community 51 - "Community 51"
Cohesion: 0.05
Nodes (40): npyv_load2_tillz_s32(), npyv_load_tillz_s64(), npyv_loadn2_f32(), npyv_loadn2_f64(), npyv_loadn2_s32(), npyv_loadn2_s64(), npyv_loadn2_till_s32(), npyv_loadn2_till_s64() (+32 more)

### Community 52 - "Community 52"
Cohesion: 0.05
Nodes (42): npyv_load2_tillz_s32(), npyv_load_tillz_s64(), npyv_loadn2_f32(), npyv_loadn2_f64(), npyv_loadn2_s32(), npyv_loadn2_s64(), npyv_loadn2_till_s32(), npyv_loadn2_till_s64() (+34 more)

### Community 53 - "Community 53"
Cohesion: 0.07
Nodes (51): libdivide_128_div_128_to_64(), libdivide_128_div_64_to_64(), libdivide_64_div_32_to_32(), libdivide_count_leading_zeros32(), libdivide_count_leading_zeros64(), libdivide_internal_s32_gen(), libdivide_internal_s64_gen(), libdivide_internal_u32_gen() (+43 more)

### Community 54 - "Community 54"
Cohesion: 0.05
Nodes (35): npyv_load2_tillz_s32(), npyv_load_tillz_s64(), npyv_loadn2_f32(), npyv_loadn2_s32(), npyv_loadn2_till_s32(), npyv_loadn2_tillz_s32(), npyv_loadn2_u32(), npyv_loadn_f32() (+27 more)

### Community 55 - "Community 55"
Cohesion: 0.05
Nodes (36): npyv_load2_tillz_s32(), npyv_load_till_s32(), npyv_load_till_s64(), npyv_load_tillz_s32(), npyv_load_tillz_s64(), npyv_loadn2_f32(), npyv_loadn2_s32(), npyv_loadn2_till_s32() (+28 more)

### Community 56 - "Community 56"
Cohesion: 0.04
Nodes (54): herme2poly(), hermeadd(), hermecompanion(), hermeder(), hermediv(), hermefit(), hermefromroots(), hermegauss() (+46 more)

### Community 57 - "Community 57"
Cohesion: 0.04
Nodes (54): herm2poly(), hermadd(), hermcompanion(), hermder(), hermdiv(), hermfit(), hermfromroots(), hermgauss() (+46 more)

### Community 58 - "Community 58"
Cohesion: 0.05
Nodes (36): npyv_load2_tillz_s32(), npyv_load_till_s64(), npyv_load_tillz_s64(), npyv_loadn2_f32(), npyv_loadn2_s32(), npyv_loadn2_till_s32(), npyv_loadn2_tillz_s32(), npyv_loadn2_u32() (+28 more)

### Community 59 - "Community 59"
Cohesion: 0.07
Nodes (12): Array, flags2names(), flags_info(), get_testdir(), Intent, Build the required testing extension module, Check that created array shares data with input array., Test if intent(in) array can be passed without copies (+4 more)

### Community 60 - "Community 60"
Cohesion: 0.05
Nodes (21): apply_tag(), get_complex_dtype(), get_real_dtype(), _make_strided_cases(), Test functions for linalg module, Add the given tag (a string) to each of the cases (a list of LinalgCase     obje, Generate cartesian product of strides for all axes, _stride_comb_iter() (+13 more)

### Community 61 - "Community 61"
Cohesion: 0.04
Nodes (18): we pre-create arrays as we sometime want to pass the same instance     and somet, Test that convolve raises the correct error message when inputs are empty., sub_array, _test_array_equal_parametrizations(), TestArgwhere, TestAsType, TestBoolCmp, TestBoolScalar (+10 more)

### Community 62 - "Community 62"
Cohesion: 0.05
Nodes (35): _check_mode(), _FileOpeners, open(), A file interface for handling local and remote data files.  The goal of datasour, Return the keys of currently supported file openers.          Parameters, Open `path` with `mode` and return the file object.      If ``path`` is a URL, i, Create a DataSource with a local path at destpath., Test if the filename is a zip file by looking at the file extension. (+27 more)

### Community 64 - "Community 64"
Cohesion: 0.06
Nodes (31): npyiter_ass_subscript(), npyiter_cache_values(), npyiter_close(), npyiter_convert_dtypes(), npyiter_convert_op_axes(), npyiter_convert_op_flags_array(), npyiter_convert_ops(), npyiter_copy() (+23 more)

### Community 65 - "Community 65"
Cohesion: 0.05
Nodes (52): lag2poly(), lagadd(), lagcompanion(), lagder(), lagdiv(), lagfit(), lagfromroots(), laggauss() (+44 more)

### Community 66 - "Community 66"
Cohesion: 0.05
Nodes (52): leg2poly(), legadd(), legcompanion(), legder(), legdiv(), legfit(), legfromroots(), leggauss() (+44 more)

### Community 67 - "Community 67"
Cohesion: 0.06
Nodes (22): assert_state_equal(), Base, gauss_from_uint(), Test spawning new generators and bit_generators directly., Test that spawn raises ValueError for negative n_children., test_generator_spawning(), test_spawn_negative_n_children(), TestDefaultRNG (+14 more)

### Community 68 - "Community 68"
Cohesion: 0.07
Nodes (34): float_to_string(), get_cast_spec(), **
get_casts()(), get_dtypes(), get_s2type_dtypes(), get_type2s_dtypes(), getFloatToStringCastSpec(), getIntToStringCastSpec() (+26 more)

### Community 69 - "Community 69"
Cohesion: 0.06
Nodes (31): BoolValuesApi, check_api_dict(), find_functions(), fullapi_hash(), Function, FunctionApi, get_api_functions(), GlobalVarApi (+23 more)

### Community 70 - "Community 70"
Cohesion: 0.05
Nodes (26): The `numpy.core` submodule exists solely for backward compatibility purposes. Th, Discrete Fourier Transform ==========================  .. currentmodule:: numpy., ``numpy.lib`` is mostly a space for implementing functions that don't belong in, ``numpy.linalg`` ================  The NumPy linear algebra functions rely on BL, ============= Masked Arrays =============  Arrays sometimes contain invalid or m, Sub-package containing the matrix class and related functions., hugepage_setup(), _mac_os_check() (+18 more)

### Community 71 - "Community 71"
Cohesion: 0.05
Nodes (14): Test both numpy and built-in complex., Test coef fallback for object arrays of non-numeric coefficients., Test the latex repr used by Jupyter, Test the output is properly configured via printoptions.     The exponential not, test_complex_coefficients(), test_nonnumeric_object_coefficients(), test_numeric_object_coefficients(), TestFormat (+6 more)

### Community 72 - "Community 72"
Cohesion: 0.05
Nodes (19): applyrules(), containscommon(), containsderivedtypes(), containsmodule(), dictappend(), flatlist(), getargs2(), hasassumedshape() (+11 more)

### Community 73 - "Community 73"
Cohesion: 0.04
Nodes (46): polyadd(), polycompanion(), polyder(), polydiv(), polyfit(), polyfromroots(), polygrid2d(), polygrid3d() (+38 more)

### Community 74 - "Community 74"
Cohesion: 0.08
Nodes (4): normalize_filename(), Test tofile, fromfile, tobytes, and fromstring, Including this fixture in a test will automatically         execute it with both, TestIO

### Community 75 - "Community 75"
Cohesion: 0.08
Nodes (12): Test that _replace_nan returns the original array if there are no     NaNs, not, SharedNanFunctionsTestsMixin, test__replace_nan(), TestNanFunctions_ArgminArgmax, TestNanFunctions_CumSumProd, TestNanFunctions_MeanVarStd, TestNanFunctions_Median, TestNanFunctions_MinMax (+4 more)

### Community 76 - "Community 76"
Cohesion: 0.06
Nodes (20): MesonTemplate, Template meson build file generation class., Test functions for linalg module, Reproduce the F90 line-wrapping logic from rules.py buildmodule., Reproduce the F77 line-wrapping logic from rules.py buildmodule., Test that F77/F90 line wrapping does not produce invalid continuations.      Reg, TestAssignmentOnlyModules, TestComplexStructCompat (+12 more)

### Community 77 - "Community 77"
Cohesion: 0.05
Nodes (20): cross(), diagonal(), LinAlgError, _raise_linalgerror_eigenvalues_nonconvergence(), _raise_linalgerror_lstsq(), _raise_linalgerror_nonposdef(), _raise_linalgerror_qr(), _raise_linalgerror_singular() (+12 more)

### Community 78 - "Community 78"
Cohesion: 0.06
Nodes (21): npyiter_allocate_buffers(), npyiter_coalesce_axes(), npyiter_copy_from_buffers(), npyiter_copy_to_buffers(), NpyIter_DebugPrint(), NpyIter_EnableExternalLoop(), npyiter_fill_buffercopy_params(), NpyIter_GetDataPtrArray() (+13 more)

### Community 79 - "Community 79"
Cohesion: 0.05
Nodes (7): add_loop(), init_comparison(), init_mixed_type_ufunc(), init_promoter(), init_string_ufuncs(), init_ufunc(), install_promoter()

### Community 80 - "Community 80"
Cohesion: 0.05
Nodes (9): CorrConv, CountNonzero, Indices, Nonzero, NumPyChar, PackBits, StatsMethods, Temporaries (+1 more)

### Community 81 - "Community 81"
Cohesion: 0.04
Nodes (1): TestMaskedArrayArithmetic

### Community 82 - "Community 82"
Cohesion: 0.05
Nodes (12): Tests for hermite_e module., TestArithmetic, TestCompanion, TestConstants, TestDerivative, TestEvaluation, TestFitting, TestGauss (+4 more)

### Community 83 - "Community 83"
Cohesion: 0.05
Nodes (12): Tests for hermite module., TestArithmetic, TestCompanion, TestConstants, TestDerivative, TestEvaluation, TestFitting, TestGauss (+4 more)

### Community 84 - "Community 84"
Cohesion: 0.05
Nodes (12): Tests for laguerre module., TestArithmetic, TestCompanion, TestConstants, TestDerivative, TestEvaluation, TestFitting, TestGauss (+4 more)

### Community 85 - "Community 85"
Cohesion: 0.08
Nodes (17): assert_all(), TestCommonType, TestImag, TestIscomplex, TestIscomplexobj, TestIsfinite, TestIsinf, TestIsnan (+9 more)

### Community 86 - "Community 86"
Cohesion: 0.05
Nodes (19): add_sfloats(), add_sfloats_resolve_descriptors(), cast_sfloat_to_sfloat_aligned(), cast_sfloat_to_sfloat_unaligned(), check_factor(), get_sfloat_dtype(), multiply_sfloats_resolve_descriptors(), python_sfloat_scaled_copy() (+11 more)

### Community 87 - "Community 87"
Cohesion: 0.05
Nodes (9): add_object_and_unicode_promoters(), add_promoter(), init_stringdtype_ufuncs(), init_ufunc(), is_integer_dtype(), string_inputs_promoter(), string_multiply_promoter(), string_object_bool_output_promoter() (+1 more)

### Community 88 - "Community 88"
Cohesion: 0.07
Nodes (16): _BaseVersion, _cmpkey(), Infinity, InvalidVersion, _legacy_cmpkey(), LegacyVersion, NegativeInfinity, parse() (+8 more)

### Community 89 - "Community 89"
Cohesion: 0.06
Nodes (12): BooleanAssignmentOrder, FlatIterIndexing, Indexing, IndexingSeparate, IndexingStructured0D, IndexingWith1DArr, ScalarIndexing, memmap (+4 more)

### Community 90 - "Community 90"
Cohesion: 0.07
Nodes (5): eq(), eqmask(), TestArrayMethods, TestMa, TestUfuncs

### Community 91 - "Community 91"
Cohesion: 0.07
Nodes (29): casting_parser(), casting_parser_full(), casting_parser_same_value(), dimension_from_scalar(), PyArray_AsTypeCopyConverter(), PyArray_AxisConverter(), PyArray_BoolConverter(), PyArray_ByteorderConverter() (+21 more)

### Community 92 - "Community 92"
Cohesion: 0.08
Nodes (41): array_absolute(), array_add(), array_bitwise_and(), array_bitwise_or(), array_bitwise_xor(), array_divmod(), array_float(), array_floor_divide() (+33 more)

### Community 93 - "Community 93"
Cohesion: 0.04
Nodes (2): _foo2(), TestVectorize

### Community 94 - "Community 94"
Cohesion: 0.04
Nodes (1): TestIndexing

### Community 95 - "Community 95"
Cohesion: 0.05
Nodes (4): fft1(), TestFFT1D, TestFFTShift, TestFFTThreadSafe

### Community 96 - "Community 96"
Cohesion: 0.06
Nodes (15): JustReader, JustWriter, Test loading non-.npy files and name mapping in .npz., # TODO: specify exact message, save_func : callable             Function used to save arrays to file.         f, RoundtripTest, test_ducktyping(), test_gzip_load() (+7 more)

### Community 97 - "Community 97"
Cohesion: 0.06
Nodes (3): If a user extends a NumPy array before 1.20 and then runs it         on NumPy 1., TestNewBufferProtocol, TestPickling

### Community 98 - "Community 98"
Cohesion: 0.05
Nodes (12): get_mat(), Test functions for matrix module, TestDiag, TestEye, TestFliplr, TestFlipud, TestHistogram2d, TestTri (+4 more)

### Community 99 - "Community 99"
Cohesion: 0.05
Nodes (1): Module containing non-deprecated functions borrowed from Numeric.

### Community 100 - "Community 100"
Cohesion: 0.06
Nodes (27): ndenumerate, Multidimensional index iterator.      Return an iterator yielding pairs of array, Standard iterator method, returns the index tuple and array value.          Retu, Standard iterator method, updates the index and returns the index         tuple., Test ndindex produces empty iterators for explicit     zero-length dimensions., Test that non-integer dimensions raise TypeError., Test that StopIteration is raised properly after exhaustion., Test that each ndindex instance creates independent iterators. (+19 more)

### Community 101 - "Community 101"
Cohesion: 0.07
Nodes (26): _check_object_rec(), create_casting_impl(), dtype_kind_to_simplified_ordering(), ensure_castingimpl_exists(), _get_castingimpl(), min_scalar_type_num(), npy_casting_to_string(), npy_set_invalid_cast_error() (+18 more)

### Community 102 - "Community 102"
Cohesion: 0.07
Nodes (23): array_iter_base_dealloc(), arrayiter_dealloc(), arraymultiter_new(), iter_array(), iter_ass_sub_Bool(), iter_ass_sub_int(), iter_ass_subscript(), iter_richcompare() (+15 more)

### Community 103 - "Community 103"
Cohesion: 0.05
Nodes (5): TestFlags, TestPutmask, TestSizeOf, TestTake, TestWhere

### Community 104 - "Community 104"
Cohesion: 0.05
Nodes (1): RNG

### Community 105 - "Community 105"
Cohesion: 0.05
Nodes (12): Tests related to the ``symbol`` attribute of the ABCPolyBase class., Test polynomial creation with symbol kwarg., Test other methods for manipulating/creating polynomial objects., Values for symbol that should pass input validation., 'symbol' attribute is read only., Ensure symbol is preserved for numeric operations on polynomials with     the sa, TestBinaryOperatorsDifferentSymbol, TestBinaryOperatorsSameSymbol (+4 more)

### Community 106 - "Community 106"
Cohesion: 0.13
Nodes (40): BigInt_Add(), BigInt_Compare(), BigInt_Copy(), BigInt_DivideWithRemainder_MaxQuotient9(), BigInt_IsEven(), BigInt_IsZero(), BigInt_Multiply(), BigInt_Multiply10() (+32 more)

### Community 108 - "Community 108"
Cohesion: 0.05
Nodes (5): TestArgmaxArgminCommon, TestDot, TestLexsort, TestMinScalarType, TestStringCompare

### Community 109 - "Community 109"
Cohesion: 0.06
Nodes (12): Bincount, Histogram1D, Histogram2D, Linspace, Mean, Median, Partition, Percentile (+4 more)

### Community 110 - "Community 110"
Cohesion: 0.07
Nodes (30): ediff1d(), intersect1d(), _isin(), Set operations for arrays based on sorting.  Notes -----  For floating point arr, Find the union of two arrays.      Return the unique, sorted array of values tha, Find the set difference of two arrays.      Return the unique values in `ar1` th, Unpacks one-element tuples for use as return values, Find the unique elements of an array.      Returns the sorted unique elements of (+22 more)

### Community 111 - "Community 111"
Cohesion: 0.06
Nodes (29): apply_along_axis(), apply_over_axes(), array_split(), column_stack(), dsplit(), dstack(), expand_dims(), hsplit() (+21 more)

### Community 113 - "Community 113"
Cohesion: 0.07
Nodes (34): _accumulate(), _arrays_for_stack_dispatcher(), atleast_1d(), atleast_2d(), atleast_3d(), _atleast_nd(), _block(), _block_check_depths_match() (+26 more)

### Community 114 - "Community 114"
Cohesion: 0.06
Nodes (37): Enum, ArithOp, as_deref(), as_ref(), eliminate_quotes(), ExprWarning, fromstring(), _FromStringWorker (+29 more)

### Community 115 - "Community 115"
Cohesion: 0.08
Nodes (40): _check_version(), descr_to_dtype(), dtype_to_descr(), _filter_header(), header_data_from_array_1_0(), isfileobj(), magic(), open_memmap() (+32 more)

### Community 116 - "Community 116"
Cohesion: 0.05
Nodes (15): angle(), asarray_chkfinite(), bartlett(), _chbevl(), _closest_observation(), _discrete_interpolation_to_boundaries(), _get_gamma_mask(), _i0_1() (+7 more)

### Community 117 - "Community 117"
Cohesion: 0.05
Nodes (20): FarrayTestCase, Test Farray __getitem__ method, out-of-range col, Test Farray asString method, Test Farray __str__ method, Test Farray view method, Test Farray size constructor, Test Farray copy constructor, Test Farray size constructor, negative nrows (+12 more)

### Community 118 - "Community 118"
Cohesion: 0.05
Nodes (10): Test functions for 1D array set operations., Test isin's invert parameter, Hit the standard isin code with integers, Test that isin works for boolean input, Test that isin works for timedelta input, Test that isin works as expected for mixed dtype input., Test values outside intp range (negative ones if 32bit system), Test that isin works as expected for bool/int input. (+2 more)

### Community 119 - "Community 119"
Cohesion: 0.05
Nodes (4): TestDigitize, TestGradient, TestMeshgrid, TestTrapezoid

### Community 120 - "Community 120"
Cohesion: 0.06
Nodes (33): diag(), diagflat(), eye(), fliplr(), flipud(), histogram2d(), mask_indices(), _min_int() (+25 more)

### Community 121 - "Community 121"
Cohesion: 0.07
Nodes (23): array_from_pyobj(), check_and_fix_dimensions(), dump_attrs(), dump_dims(), f2py_cb_start_call_clock(), f2py_cb_start_clock(), f2py_cb_stop_call_clock(), f2py_cb_stop_clock() (+15 more)

### Community 122 - "Community 122"
Cohesion: 0.05
Nodes (8): CommaDecimalPointLocale, Confirm that extracting a value doesn't convert to python float, Test that string representations of long-double roundtrip both     for array cas, test_array_and_stringlike_roundtrip(), test_scalar_extraction(), TestCommaDecimalPointLocale, TestFileBased, TestCommaDecimalPointLocale

### Community 123 - "Community 123"
Cohesion: 0.08
Nodes (35): _get_bin_edges(), _get_outer_edges(), _hist_bin_auto(), _hist_bin_doane(), _hist_bin_fd(), _hist_bin_rice(), _hist_bin_scott(), _hist_bin_sqrt() (+27 more)

### Community 124 - "Community 124"
Cohesion: 0.06
Nodes (11): pcg_oneseq_8_rxs_m_xs_8_boundedrand_r(), pcg_oneseq_8_rxs_m_xs_8_random_r(), pcg_oneseq_8_srandom_r(), pcg_oneseq_8_step_r(), pcg_output_rxs_m_xs_8_8(), pcg_setseq_8_rxs_m_xs_8_boundedrand_r(), pcg_setseq_8_rxs_m_xs_8_random_r(), pcg_setseq_8_srandom_r() (+3 more)

### Community 125 - "Community 125"
Cohesion: 0.07
Nodes (18): argmax(), argmin(), as_pystring(), common_instance(), compare(), _eq_comparison(), init_string_dtype(), init_stringdtype_sorts() (+10 more)

### Community 126 - "Community 126"
Cohesion: 0.05
Nodes (1): TestNonarrayArgs

### Community 127 - "Community 127"
Cohesion: 0.07
Nodes (5): float, PhysicalQuantity, TestGeomspace, TestLinspace, TestLogspace

### Community 128 - "Community 128"
Cohesion: 0.07
Nodes (36): _add(), _as_int(), as_series(), _div(), _fit(), _fromroots(), getdomain(), _gridnd() (+28 more)

### Community 129 - "Community 129"
Cohesion: 0.07
Nodes (10): Casting, get_expected_stringlength(), The tests exercise the casting machinery in a more low-level manner. The reason, Returns a copy of arr1 that may be non-contiguous or unaligned, and a         ma, This test checks numeric direct casts for dtypes supported also by the         s, Returns the string length when casting the basic dtypes to strings., Tests casts from and to string by checking the roundtripping property., # TODO: While this test is fairly thorough, right now, it does not (+2 more)

### Community 130 - "Community 130"
Cohesion: 0.09
Nodes (19): AbstractTest, assert_features_equal(), Ensure that the environment is reset, Ensure that when selecting `NPY_ENABLE_CPU_FEATURES`, only the         features, Ensure that when both environment variables are set then an         ImportError, Test that an error is thrown if the environment variables are too long         t, Test that the maximum accepted environment variable length can be         proces, Test that a RuntimeError is thrown if an impossible feature-disabling         re (+11 more)

### Community 131 - "Community 131"
Cohesion: 0.07
Nodes (2): The addition method is special for the scaled float, because it         includes, TestSFloat

### Community 132 - "Community 132"
Cohesion: 0.14
Nodes (34): deprecate_integer_datetime_operation(), find_userloop(), linear_search_type_resolver(), linear_search_userloop_type_resolver(), npy_casting_to_py_object(), PyUFunc_AbsoluteTypeResolver(), PyUFunc_AdditionTypeResolver(), PyUFunc_DefaultLegacyInnerLoopSelector() (+26 more)

### Community 133 - "Community 133"
Cohesion: 0.08
Nodes (16): as_apply(), as_eq(), as_expr(), as_ge(), as_gt(), as_le(), as_lt(), as_ne() (+8 more)

### Community 134 - "Community 134"
Cohesion: 0.11
Nodes (31): legacy_beta(), legacy_chisquare(), legacy_double(), legacy_exponential(), legacy_f(), legacy_gamma(), legacy_gauss(), legacy_geometric_inversion() (+23 more)

### Community 135 - "Community 135"
Cohesion: 0.09
Nodes (25): count_boolean_trues(), count_nonzero_bytes_384(), count_nonzero_int(), count_nonzero_u8(), count_zero_bytes_u16(), count_zero_bytes_u8(), _new_argsortlike(), _new_sortlike() (+17 more)

### Community 136 - "Community 136"
Cohesion: 0.07
Nodes (37): pcg_mcg_128_xsh_rr_64_boundedrand_r(), pcg_mcg_128_xsh_rr_64_random_r(), pcg_oneseq_128_rxs_m_xs_128_boundedrand_r(), pcg_oneseq_128_rxs_m_xs_128_random_r(), pcg_oneseq_128_srandom_r(), pcg_oneseq_128_step_r(), pcg_oneseq_128_xsh_rr_64_boundedrand_r(), pcg_oneseq_128_xsh_rr_64_random_r() (+29 more)

### Community 137 - "Community 137"
Cohesion: 0.07
Nodes (37): pcg_mcg_64_xsh_rr_32_boundedrand_r(), pcg_mcg_64_xsh_rr_32_random_r(), pcg_oneseq_64_rxs_m_xs_64_boundedrand_r(), pcg_oneseq_64_rxs_m_xs_64_random_r(), pcg_oneseq_64_srandom_r(), pcg_oneseq_64_step_r(), pcg_oneseq_64_xsh_rr_32_boundedrand_r(), pcg_oneseq_64_xsh_rr_32_random_r() (+29 more)

### Community 138 - "Community 138"
Cohesion: 0.08
Nodes (15): assert_almost_equal(), test_matrix_norm(), test_pinv_rtol_arg(), test_vector_norm(), TestMultiDot, _TestNorm, _TestNorm2D, _TestNormBase (+7 more)

### Community 139 - "Community 139"
Cohesion: 0.06
Nodes (7): TestChoose, TestClip, TestNewaxis, TestRepeat, TestResize, TestVdot, TestView

### Community 140 - "Community 140"
Cohesion: 0.06
Nodes (1): TestCreation

### Community 141 - "Community 141"
Cohesion: 0.07
Nodes (12): Copy, CopyStructured, CopyTo, LoadNpyOverhead, LoadtxtCSVComments, LoadtxtCSVDateTime, LoadtxtCSVdtypes, LoadtxtCSVSkipRows (+4 more)

### Community 142 - "Community 142"
Cohesion: 0.07
Nodes (31): CLexer, Directive, _get_c_source_file(), LegacyDirective, linkcode_resolve(), NumPyLexer, Adapted from docutils/parsers/rst/directives/admonitions.py      Uses a default, Rename numpy types to use the canonical names to make sphinx behave (+23 more)

### Community 143 - "Community 143"
Cohesion: 0.09
Nodes (33): _cook_nd_args(), fft(), fft2(), fftn(), hfft(), ifft(), ifft2(), ifftn() (+25 more)

### Community 144 - "Community 144"
Cohesion: 0.10
Nodes (22): concatenateRoutines(), create_name_header(), dumpRoutineNames(), ensure_executable(), FortranLibrary, FortranRoutine, getLapackRoutines(), getWrappedRoutineNames() (+14 more)

### Community 145 - "Community 145"
Cohesion: 0.13
Nodes (36): _assert_finite(), _assert_stacked_square(), cholesky(), _commonType(), _complexType(), cond(), det(), eig() (+28 more)

### Community 146 - "Community 146"
Cohesion: 0.06
Nodes (15): chararray, For each element in `self`, return a list of the words in         the string, us, For each element in `self`, return a copy with the trailing         characters r, For each element in `self`, return True if there are only         decimal charac, chararray(shape, itemsize=1, unicode=False, buffer=None, offset=0,, Return (self + other), that is string concatenation,         element-wise for a, Return the indices that sort the array lexicographically.          For full docu, Returns an array with the number of non-overlapping occurrences of         subst (+7 more)

### Community 147 - "Community 147"
Cohesion: 0.08
Nodes (28): array_function_errmsg_formatter(), array_ufunc_errmsg_formatter(), _copy_fields(), _gcd(), _getfield_is_safe(), _lcm(), _makenames_list(), _newnames() (+20 more)

### Community 148 - "Community 148"
Cohesion: 0.08
Nodes (17): MaskedRecords, _mrreconstruct(), Returns the data as a recarray., Sets the attribute attr to the value val., Returns all the fields sharing the same fieldname base.          The fieldname b, Sets the given record to value., Calculates the string representation., Calculates the repr representation. (+9 more)

### Community 149 - "Community 149"
Cohesion: 0.06
Nodes (5): npyv_abs_f64(), npyv_ceil_f64(), npyv_floor_f64(), npyv_rint_f64(), npyv_trunc_f64()

### Community 150 - "Community 150"
Cohesion: 0.06
Nodes (1): TestMethods

### Community 151 - "Community 151"
Cohesion: 0.08
Nodes (12): _GenericTest, Test rank 3 array for all dtypes., Test comparing an array with a scalar when all values are equal., Test comparing an array with a scalar when not all values equal., Test comparing an array with a scalar with strict option., Test comparing two arrays with strict option., Test two equal array of rank 1 are found equal., Test two different array of rank 1 are found not equal. (+4 more)

### Community 152 - "Community 152"
Cohesion: 0.07
Nodes (8): TestBCCharHandling, TestCharacter, TestCharacterString, TestMiscCharacter, TestNewCharHandling, TestStringAssumedLength, TestStringOptionalInOut, TestStringScalarArr

### Community 153 - "Community 153"
Cohesion: 0.14
Nodes (15): invalid_httpurl(), invalid_textfile(), Stub to replace urlopen for testing., TestDataSourceAbspath, TestDataSourceExists, TestDataSourceOpen, TestOpenFunc, TestRepositoryAbspath (+7 more)

### Community 154 - "Community 154"
Cohesion: 0.06
Nodes (8): Test the scalar constructors, which also do type-coercion, Test scalar.device attribute and scalar.to_device() method., TestAsIntegerRatio, TestBitCount, TestClassGetItem, TestDevice, TestIsInteger, TestSignature

### Community 155 - "Community 155"
Cohesion: 0.06
Nodes (1): Core

### Community 156 - "Community 156"
Cohesion: 0.08
Nodes (11): Isin, Nan, Pad, Benchmarks for `numpy.lib`., Benchmark for np.unique with np.nan values., Benchmarks for `numpy.pad`.      When benchmarking the pad function it is useful, Benchmark for np.unique with integer dtypes., Benchmarks for `numpy.isin`. (+3 more)

### Community 157 - "Community 157"
Cohesion: 0.09
Nodes (13): Concatenate, Corrcoef, Cov, Indexing, MA, MACreation, MAFunctions1v, MAFunctions2v (+5 more)

### Community 158 - "Community 158"
Cohesion: 0.10
Nodes (29): bmm_einsum(), _compute_size_by_dict(), einsum(), einsum_path(), _find_contraction(), _flop_count(), _greedy_path(), _optimal_path() (+21 more)

### Community 159 - "Community 159"
Cohesion: 0.06
Nodes (33): argmax(), argmin(), argpartition(), argsort(), around(), choose(), clip(), compress() (+25 more)

### Community 160 - "Community 160"
Cohesion: 0.08
Nodes (29): as_array(), as_ctypes(), as_ctypes_type(), _concrete_ndptr, _ctype_from_dtype(), _ctype_from_dtype_scalar(), _ctype_from_dtype_structured(), _ctype_from_dtype_subarray() (+21 more)

### Community 161 - "Community 161"
Cohesion: 0.13
Nodes (31): _as_pairs(), _get_edges(), _get_linear_ramps(), _get_stats(), pad(), _pad_simple(), The arraypad module contains a group of functions to pad values onto the edges o, Set empty-padded area in given dimension.      Parameters     ----------     pad (+23 more)

### Community 162 - "Community 162"
Cohesion: 0.10
Nodes (17): _check_nonneg_int(), _ensure_ndmin_ndarray(), _ensure_ndmin_ndarray_check_param(), fromregex(), genfromtxt(), load(), loadtxt(), NpzFile (+9 more)

### Community 163 - "Community 163"
Cohesion: 0.06
Nodes (26): _DomainCheckInterval, _DomainedBinaryOperation, _DomainGreater, _DomainGreaterEqual, _DomainTan, _MaskedPrintOption, _MaskedUFunc, _MaskedUnaryOperation (+18 more)

### Community 164 - "Community 164"
Cohesion: 0.07
Nodes (33): pcg_mcg_16_step_r(), pcg_mcg_16_xsh_rr_8_boundedrand_r(), pcg_mcg_16_xsh_rr_8_random_r(), pcg_mcg_16_xsh_rs_8_boundedrand_r(), pcg_mcg_16_xsh_rs_8_random_r(), pcg_oneseq_16_rxs_m_xs_16_boundedrand_r(), pcg_oneseq_16_rxs_m_xs_16_random_r(), pcg_oneseq_16_srandom_r() (+25 more)

### Community 165 - "Community 165"
Cohesion: 0.07
Nodes (33): pcg_mcg_32_step_r(), pcg_mcg_32_xsh_rr_16_boundedrand_r(), pcg_mcg_32_xsh_rr_16_random_r(), pcg_mcg_32_xsh_rs_16_boundedrand_r(), pcg_mcg_32_xsh_rs_16_random_r(), pcg_oneseq_32_rxs_m_xs_32_boundedrand_r(), pcg_oneseq_32_rxs_m_xs_32_random_r(), pcg_oneseq_32_srandom_r() (+25 more)

### Community 166 - "Community 166"
Cohesion: 0.11
Nodes (22): assert_poly_almost_equal(), Poly(), Test inter-conversion of different polynomial classes.  This tests the convert a, test_add(), test_call_with_list(), test_cutdeg(), test_deriv(), test_divmod() (+14 more)

### Community 167 - "Community 167"
Cohesion: 0.10
Nodes (19): Tests for numpy/_core/src/multiarray/conversion_utils.c, Tests of PyArray_SortkindConverter, Tests of PyArray_SelectkindConverter, Tests of PyArray_SearchsideConverter, Tests of PyArray_OrderConverter, Tests of PyArray_ClipmodeConverter, Tests of PyArray_CastingConverter, Tests of PyArray_IntpConverter (+11 more)

### Community 168 - "Community 168"
Cohesion: 0.10
Nodes (1): TestMaskedArrayInPlaceArithmetic

### Community 169 - "Community 169"
Cohesion: 0.06
Nodes (9): Test that arguments are coerced from arrays, Test that return values are coerced to arrays, Test that vague ndpointer return values do not promote to arrays, Test conversion from dtypes to ctypes types, TestAsArray, TestAsCtypesType, TestLoadLibrary, TestNdpointer (+1 more)

### Community 170 - "Community 170"
Cohesion: 0.07
Nodes (12): assert_raises_fpe(), Confirms a small number of known half values, Checks that rounding when converting to half is correct, Take every finite float16, and check the casting functions with            a man, Make sure comparisons are working right, Test the various ArrFuncs, Test np.spacing and np.nextafter, Test the various ufuncs (+4 more)

### Community 171 - "Community 171"
Cohesion: 0.07
Nodes (11): allocator_lock_order_workload(), assert_no_deadlock(), _detected_blas(), _openblas_predates_gemm_fix(), Run ``workload`` in a fresh subprocess; fail if it does not finish in time., test_blas_gemm_thread_safety(), test_concurrent_allocator_acquire_no_deadlock(), test_concurrent_unique_no_deadlock() (+3 more)

### Community 172 - "Community 172"
Cohesion: 0.07
Nodes (1): TestHistogram

### Community 173 - "Community 173"
Cohesion: 0.10
Nodes (14): consistent_subclass(), get_rtol(), HermitianGeneralizedTestCase, HermitianTestCase, LinalgGeneralizedNonsquareTestCase, LinalgNonsquareTestCase, LinalgTestCase, PinvHermitianCases (+6 more)

### Community 174 - "Community 174"
Cohesion: 0.06
Nodes (4): RaiseOnBool, TestArrayConstruction, TestArrayCreationCopyArgument, TestFlat

### Community 175 - "Community 175"
Cohesion: 0.07
Nodes (7): Test append_fields with arrays containing objects, Test append_fields when the base array contains objects, TestAppendFields, TestAppendFieldsObj, TestMergeArrays, TestRecursiveFillFields, TestStackArrays

### Community 176 - "Community 176"
Cohesion: 0.09
Nodes (27): arccos(), arcsin(), arctanh(), _fix_int_lt_zero(), _fix_real_abs_gt_1(), _fix_real_lt_zero(), log(), log10() (+19 more)

### Community 177 - "Community 177"
Cohesion: 0.06
Nodes (30): DummyArray, Dummy object that just exists to hang __array_interface__ dictionaries     and p, Construct an array viewing the first byte of each element of `x`, view_element_first_byte(), coerce(), coerce2(), dtype2(), na_object() (+22 more)

### Community 178 - "Community 178"
Cohesion: 0.07
Nodes (24): common_type(), _getmaxmin(), imag(), iscomplex(), iscomplexobj(), isreal(), isrealobj(), mintypecode() (+16 more)

### Community 179 - "Community 179"
Cohesion: 0.07
Nodes (28): append(), argsort(), common_fill_value(), _convert2ma(), default_fill_value(), _deprecate_argsort_axis(), _extremum_fill_value(), _get_dtype_of() (+20 more)

### Community 180 - "Community 180"
Cohesion: 0.09
Nodes (15): default_calloc(), default_free(), default_malloc(), get_handler_name(), get_handler_version(), indicate_hugepages(), _npy_alloc_cache(), npy_alloc_cache_dim() (+7 more)

### Community 181 - "Community 181"
Cohesion: 0.08
Nodes (13): array_dataptr_get(), array_descr_set(), array_descr_set_internal(), array_imag_get(), array_imag_set(), array_interface_get(), array_protocol_strides_get(), array_real_get() (+5 more)

### Community 182 - "Community 182"
Cohesion: 0.13
Nodes (30): check_mask_for_writemasked_reduction(), intp_abs(), NpyIter_AdvancedNew(), npyiter_allocate_arrays(), npyiter_allocate_transfer_functions(), npyiter_apply_forced_iteration_order(), npyiter_calculate_ndim(), npyiter_casting_to_string() (+22 more)

### Community 183 - "Community 183"
Cohesion: 0.08
Nodes (3): TestMethods, TestMethodsEmptyArray, TestMethodsScalarValues

### Community 184 - "Community 184"
Cohesion: 0.07
Nodes (4): new_and_old_dlpack(), # NOTE: The copy converter should be stricter, but not just here., TestDLPack, TestRegisterDlpackDtype

### Community 185 - "Community 185"
Cohesion: 0.06
Nodes (3): TestExp, TestLog, TestSpecialFloats

### Community 186 - "Community 186"
Cohesion: 0.12
Nodes (21): array(), _deprecate_shape_0_as_None(), find_duplicate(), format_parser, fromarrays(), fromfile(), fromrecords(), fromstring() (+13 more)

### Community 187 - "Community 187"
Cohesion: 0.09
Nodes (12): array_dealloc(), array_might_be_written(), array_new(), array_richcompare(), _clear_array_attributes(), DEPRECATE_silence_error(), PyArray_CheckStrides(), PyArray_FailUnlessWriteable() (+4 more)

### Community 188 - "Community 188"
Cohesion: 0.15
Nodes (26): array_assign_boolean_subscript(), array_assign_item(), array_assign_subscript(), array_boolean_subscript(), array_item(), array_item_asarray(), array_subscript(), array_subscript_asarray() (+18 more)

### Community 189 - "Community 189"
Cohesion: 0.08
Nodes (11): afound_new_run_(), amerge_at_(), atimsort_(), compute_min_run(), compute_min_run_short(), found_new_run_(), powerloop(), resize_buffer_intp() (+3 more)

### Community 190 - "Community 190"
Cohesion: 0.08
Nodes (2): These currently never use the hash-based solution.  However,         it seems ea, TestUnique

### Community 191 - "Community 191"
Cohesion: 0.07
Nodes (9): Check that the cython API can write to a vstring array., Check that the cython API can load strings from a vstring array., Check that the cython API can acquire/release multiple vstring allocators., Check that allocators for non-StringDType arrays is NULL., test_npystring_allocators_other_dtype(), test_npystring_load(), test_npystring_multiple_allocators(), test_npystring_pack() (+1 more)

### Community 192 - "Community 192"
Cohesion: 0.08
Nodes (1): TestUnwrap

### Community 193 - "Community 193"
Cohesion: 0.08
Nodes (27): _check_correct_qualname_and_module(), check_dir(), is_unexpected(), Check if this needs to be considered., Test that we don't add anything that looks like a new public module by     accid, Returns a mapping of all objects with the wrong __module__ attribute., Method checking all objects. The pkgutil-based method in     `test_all_modules_a, Check that all submodules listed higher up in this file can be imported      Not (+19 more)

### Community 194 - "Community 194"
Cohesion: 0.10
Nodes (9): AddReduce, AddReduceSeparate, AnyAll, ArgMax, ArgMin, FMinMax, SmallReduction, SmallReduction2D (+1 more)

### Community 195 - "Community 195"
Cohesion: 0.11
Nodes (25): build_func_data(), _check_order(), check_td_order(), docstrings, english_upper(), FullTypeDescr, FuncNameSuffix, indent() (+17 more)

### Community 196 - "Community 196"
Cohesion: 0.08
Nodes (13): finfo, _fr0(), _fr1(), iinfo, Machine limits for Float32 and Float64 and (long double) if available..., fix rank-0 --> rank-1, fix rank > 0 --> rank-0, Return the value for tiny, alias of smallest_normal.          Returns         -- (+5 more)

### Community 197 - "Community 197"
Cohesion: 0.10
Nodes (28): almost(), approx(), assert_almost_equal(), assert_array_almost_equal(), assert_array_approx_equal(), assert_array_compare(), assert_array_equal(), assert_array_less() (+20 more)

### Community 198 - "Community 198"
Cohesion: 0.11
Nodes (17): MesonBackend, build_code(), build_meson(), build_module(), CompilerChecker, F2PyTest, get_module_dir(), get_temp_module_name() (+9 more)

### Community 199 - "Community 199"
Cohesion: 0.08
Nodes (6): assert_dtype_equal(), Test whether equivalent record dtypes hash the same., Test if an appropriate exception is raised when passing bad values to         th, Test whether equivalent subarray dtypes hash the same., test_result_type_integers_and_unitless_timedelta64(), TestRecord

### Community 200 - "Community 200"
Cohesion: 0.09
Nodes (15): assert_finfo_equal(), assert_iinfo_equal(), Test functions for limits module., Test that the subnormal is zero warning is not being raised., test_instances(), test_subnormal_warning(), TestDouble, TestFinfo (+7 more)

### Community 201 - "Community 201"
Cohesion: 0.10
Nodes (20): assert_copy_equivalent(), _check_assignment(), check_internal_overlap(), check_may_share_memory_easy_fuzz(), check_may_share_memory_exact(), _indices(), _indices_for_axis(), _indices_for_nelems() (+12 more)

### Community 202 - "Community 202"
Cohesion: 0.10
Nodes (5): _aligned_zeros(), Allocate a new ndarray with aligned memory.      The ndarray is guaranteed *not*, TestAlignment, TestBinop, TestPEP3118Dtype

### Community 203 - "Community 203"
Cohesion: 0.12
Nodes (17): check_complex_value(), check_real_value(), # TODO: branch cuts (use Pauli code), # TODO: conj 'symmetry', # TODO: FPU exceptions, # FIXME: this will probably change when we require full C99 compatibility, # TODO: replace with a check on whether platform-provided C99 funcs are used, # FIXME: ugly workaround for isinf bug. (+9 more)

### Community 204 - "Community 204"
Cohesion: 0.12
Nodes (9): _FilterInvalids, TestBool, TestFmax, TestFmin, TestHypot, TestLogAddExp, TestLogAddExp2, TestMaximum (+1 more)

### Community 205 - "Community 205"
Cohesion: 0.08
Nodes (9): cmp_arg_types(), _free_loop1d_list(), _loop1d_list_free(), PyUFunc_GetDefaultIdentity(), PyUFunc_RegisterLoopForDescr(), PyUFunc_RegisterLoopForType(), _typecharfromnum(), ufunc_get_identity() (+1 more)

### Community 206 - "Community 206"
Cohesion: 0.13
Nodes (18): pcg128_add(), pcg128_mult(), pcg128_mult_64(), pcg64_cm_next32(), pcg64_cm_next64(), PCG_128BIT_CONSTANT(), pcg_cm_advance_r(), pcg_cm_random_r() (+10 more)

### Community 207 - "Community 207"
Cohesion: 0.08
Nodes (7): npyv_divc_s16(), npyv_divc_s64(), npyv_divc_s8(), npyv_divc_u64(), npyv__mullhi_u64(), npyv_sum_u32(), npyv_sumup_u16()

### Community 208 - "Community 208"
Cohesion: 0.16
Nodes (24): acquire_allocator_lock(), allocator_seen(), arena_free(), arena_malloc(), heap_or_arena_allocate(), heap_or_arena_deallocate(), is_short_string(), NpyString_acquire_allocator() (+16 more)

### Community 209 - "Community 209"
Cohesion: 0.07
Nodes (9): iter_struct_object_dtypes(), # NOTE: Mutating should be deprecated, but new API added to replace it., Iterates over a few complex dtypes and object pattern which     fill the array w, Tests subarray fields which contain sparse dtypes so that     not all memory is, TestDtypeAttributeDeletion, TestDtypeAttributes, TestDTypeSignatures, TestStructuredDtypeSparseFields (+1 more)

### Community 210 - "Community 210"
Cohesion: 0.09
Nodes (5): _mean(), _std(), TestFromBuffer, TestStats, _var()

### Community 211 - "Community 211"
Cohesion: 0.10
Nodes (3): TestAttributes, TestScalarIndexing, TestZeroRank

### Community 212 - "Community 212"
Cohesion: 0.08
Nodes (7): Test the scalar constructors, which also do type-coercion, Strings containing an unrepresentable float overflow, gh-15467 and gh-19125, TestArrayFromScalar, TestExtraArgs, TestFromInt, TestFromString

### Community 213 - "Community 213"
Cohesion: 0.13
Nodes (13): cleanComments(), CommentQueue, LenSubsScanner, LineQueue, MyScanner, Replace dlamch_ calls with appropriate macros, Following clapack, we remove ftnlen arguments, which f2c puts after     a char *, removeBuiltinFunctions() (+5 more)

### Community 214 - "Community 214"
Cohesion: 0.10
Nodes (13): npy_float_to_half(), npy_half_divmod(), npy_half_eq_nonan(), npy_half_ge(), npy_half_gt(), npy_half_isfinite(), npy_half_isinf(), npy_half_isnan() (+5 more)

### Community 215 - "Community 215"
Cohesion: 0.08
Nodes (22): assert_no_warnings(), _assert_no_warnings_context(), assert_raises(), assert_raises_regex(), assert_string_equal(), break_cycles(), decorate_methods(), _Dummy (+14 more)

### Community 216 - "Community 216"
Cohesion: 0.09
Nodes (10): loop_pos, looper, Helper for looping over sequences, particular in templates.  Often in a loop in, Returns true if this item is the start of a new group,         where groups mean, Returns true if this item is the end of a new group,         where groups mean t, Helper for looping (particularly in templates)      Use this like::          for, A small templating language  This implements a small templating language.  This, Lex a string into chunks:          >>> lex('hey')         ['hey']         >>> le (+2 more)

### Community 217 - "Community 217"
Cohesion: 0.07
Nodes (2): Tests of interaction of matrix with other parts of numpy.  Note that tests with, TestConcatenatorMatrix

### Community 218 - "Community 218"
Cohesion: 0.09
Nodes (2): TestAllclose, TestIsclose

### Community 219 - "Community 219"
Cohesion: 0.10
Nodes (8): Test permuting elements for each 128-bit lane.         npyv_permi128_##sfx, Test expand intrinsics:             npyv_expand_u16_u8             npyv_expand_u, Test integer division intrinsics:             npyv_divisor_##sfx             npy, Test reduce sum intrinsics:             npyv_sum_##sfx, Conditional addition and subtraction for all supported data types.         Test, To test all vector types at once, Test lookup table intrinsics:             npyv_lut32_##sfx             npyv_lut1, _SIMD_ALL

### Community 220 - "Community 220"
Cohesion: 0.09
Nodes (7): npyv_divc_s16(), npyv_divc_s64(), npyv_divc_s8(), npyv_divc_u64(), npyv__mullhi_u64(), npyv_sum_u32(), npyv_sumup_u16()

### Community 221 - "Community 221"
Cohesion: 0.10
Nodes (10): Bounded, Choice, Permutation, Randint, Randint_dtype, Random, Timer for 8-bit bounded values.          Parameters (packed as args)         ---, Compare to uint32 below (+2 more)

### Community 222 - "Community 222"
Cohesion: 0.13
Nodes (13): _AbstractBinary, _AbstractUnary, BinaryComplex, BinaryFP, BinaryFPSpecial, BinaryInt, BinaryIntContig, LogisticRegression (+5 more)

### Community 223 - "Community 223"
Cohesion: 0.08
Nodes (14): asarray(), Return an array with the elements of `self`         right-justified in a string, For each element in `self`, return a copy of the string with         uppercase c, For each element in `self`, return a titlecased version of the         string: w, For each element in `self`, return a copy of the string where         all charac, Return an array with the elements of `self` converted to         uppercase., Return the numeric string left-filled with zeros in a string of         length `, Convert the input to a `~numpy.char.chararray`, copying the data only if     nec (+6 more)

### Community 224 - "Community 224"
Cohesion: 0.15
Nodes (24): _aligned_offset(), _byte_order_str(), _construction_repr(), _datetime_metadata_str(), _is_packed(), _isunsized(), _kind_name(), _name_get() (+16 more)

### Community 225 - "Community 225"
Cohesion: 0.08
Nodes (16): empty(), eye(), identity(), ones(), rand(), randn(), Return a matrix of given shape and type, filled with zeros.      Parameters, Returns the square identity matrix of given size.      Parameters     ---------- (+8 more)

### Community 226 - "Community 226"
Cohesion: 0.08
Nodes (2): Test getting and setting global print options., TestPrintOptions

### Community 227 - "Community 227"
Cohesion: 0.08
Nodes (2): TestIndices, TestNonzero

### Community 228 - "Community 228"
Cohesion: 0.11
Nodes (20): CClass, diag_indices(), _diag_indices_from(), fill_diagonal(), IndexExpression, ix_(), MGridClass, nd_grid (+12 more)

### Community 229 - "Community 229"
Cohesion: 0.11
Nodes (8): poly1d, polyadd(), polymul(), polysub(), A one-dimensional polynomial class.      .. note::        This forms part of the, Find the sum of two polynomials.      .. note::        This forms part of the ol, Difference (subtraction) of two polynomials.      .. note::        This forms pa, Find the product of two polynomials.      .. note::        This forms part of th

### Community 230 - "Community 230"
Cohesion: 0.09
Nodes (4): npyv_muladd_f32(), npyv_muladd_f64(), npyv_muladdsub_f32(), npyv_muladdsub_f64()

### Community 232 - "Community 232"
Cohesion: 0.10
Nodes (5): MaskedArray, MMatrix, TestConcatenator, TestMaskedMatrix, TestSubclassing

### Community 233 - "Community 233"
Cohesion: 0.17
Nodes (23): compute_min_run_short(), npy_acount_run(), npy_aforce_collapse(), npy_agallop_left(), npy_agallop_right(), npy_amerge_at(), npy_amerge_left(), npy_amerge_right() (+15 more)

### Community 234 - "Community 234"
Cohesion: 0.09
Nodes (5): PyArray_CHKFLAGS(), PyArray_DESCR(), PyArray_DTYPE(), PyArray_FLAGS(), PyArray_TYPE()

### Community 235 - "Community 235"
Cohesion: 0.08
Nodes (1): TestMemmap

### Community 236 - "Community 236"
Cohesion: 0.08
Nodes (4): MatmulCommon, Common tests for '@' operator and numpy.matmul., TestMatmul, TestMatmulOperator

### Community 237 - "Community 237"
Cohesion: 0.08
Nodes (1): TestSpecialMethods

### Community 238 - "Community 238"
Cohesion: 0.13
Nodes (11): ABC, Backend, Backend, _get_flags(), _meson_identifier(), MesonBackend, _prepare_objects(), _prepare_sources() (+3 more)

### Community 239 - "Community 239"
Cohesion: 0.10
Nodes (8): AtLeast1D, Block, Block2D, Block3D, Kron, Benchmarks for Kronecker product of two arrays, Benchmarks for np.atleast_1d, This benchmark concatenates an array of size ``(5n)^3``

### Community 240 - "Community 240"
Cohesion: 0.11
Nodes (20): isdtype(), issctype(), issubclass_(), issubdtype(), issubsctype(), obj2sctype(), _preprocess_dtype(), _PreprocessDTypeError (+12 more)

### Community 241 - "Community 241"
Cohesion: 0.15
Nodes (23): get_kind(), isarray(), iscomplexarray(), isdouble(), isint1(), isint1array(), isinteger(), islong_long() (+15 more)

### Community 242 - "Community 242"
Cohesion: 0.21
Nodes (20): cb_routsign2map(), cb_sign2map(), common_sign2map(), f2cexpr(), get_elsize(), getarrdims(), getarrdocsign(), getctype() (+12 more)

### Community 243 - "Community 243"
Cohesion: 0.16
Nodes (20): buildmodules(), callcrackfortran(), CombineIncludePaths, dict_append(), f2py_parser(), filter_files(), get_newer_options(), main() (+12 more)

### Community 244 - "Community 244"
Cohesion: 0.13
Nodes (14): __New_PyArray_Std(), power_of_ten(), PyArray_ArgMax(), _PyArray_ArgMaxWithKeepdims(), PyArray_ArgMin(), _PyArray_ArgMinMaxCommon(), _PyArray_ArgMinWithKeepdims(), PyArray_Conjugate() (+6 more)

### Community 245 - "Community 245"
Cohesion: 0.11
Nodes (10): check_and_adjust_axis(), check_and_adjust_axis_msg(), _check_compatibility_with_new_dtype(), convert_shape_to_string(), dot_alignment_error(), _get_subarray_base_and_dimensions(), _get_subarray_ndim(), _may_have_objects() (+2 more)

### Community 246 - "Community 246"
Cohesion: 0.11
Nodes (10): fields_traverse_data_clone(), fields_traverse_data_free(), get_clear_function(), get_fields_traverse_function(), get_subarray_traverse_func(), npy_get_clear_void_and_legacy_user_dtype_loop(), npy_get_zerofill_void_and_legacy_user_dtype_loop(), PyArray_GetClearFunction() (+2 more)

### Community 247 - "Community 247"
Cohesion: 0.18
Nodes (17): doubleTestCase, FlatTestCase, floatTestCase, intTestCase, longLongTestCase, longTestCase, Test Process function 1D array, Test Process function 3D array (+9 more)

### Community 249 - "Community 249"
Cohesion: 0.09
Nodes (4): Regression test for gh-5096., Regression test for gh-16354., Coefficients should be modifiable, TestPolynomial

### Community 250 - "Community 250"
Cohesion: 0.09
Nodes (1): TestRegression

### Community 251 - "Community 251"
Cohesion: 0.09
Nodes (7): _check_neg_zero(), Check all ufuncs that the correct type is returned. Avoid     object and boolean, Check that contiguous and non-contiguous calls to ufuncs     have the same resul, test_addition_negative_zero(), test_addition_reduce_negative_zero(), test_ufunc_noncontiguous(), test_ufunc_types()

### Community 252 - "Community 252"
Cohesion: 0.11
Nodes (5): BroadcastArrays, BroadcastArraysTo, ConcatenateNestedArrays, ConcatenateStackArrays, DimsManipulations

### Community 253 - "Community 253"
Cohesion: 0.18
Nodes (15): change_decimal_from_locale_to_dot(), ensure_decimal_point(), ensure_minimum_exponent_length(), fix_ascii_format(), NumPyOS_ascii_ftolf(), NumPyOS_ascii_isalnum(), NumPyOS_ascii_isalpha(), NumPyOS_ascii_isdigit() (+7 more)

### Community 254 - "Community 254"
Cohesion: 0.19
Nodes (20): Exception, F2CError, find_position(), isolate_expression(), lex(), parse(), parse_cond(), parse_def() (+12 more)

### Community 255 - "Community 255"
Cohesion: 0.10
Nodes (4): get_names(), get_names_flat(), Collection of utilities to manipulate structured arrays.  Most of these function, Returns the field names of the input datatype as a tuple. Input datatype     mus

### Community 256 - "Community 256"
Cohesion: 0.10
Nodes (19): drop_metadata(), get_include(), _get_indent(), _info(), _makenamedict(), _median_nancheck(), _opt_info(), Determines the leading whitespace that could be removed from all the lines. (+11 more)

### Community 257 - "Community 257"
Cohesion: 0.15
Nodes (19): arr_bincount(), arr_interp(), arr_interp_complex(), arr__monotonicity(), arr_ravel_multi_index(), arr_unravel_index(), astype_anyint(), binary_search_with_guess() (+11 more)

### Community 258 - "Community 258"
Cohesion: 0.13
Nodes (6): Check wrapping on each side individually if the wrapped area is longer         t, Assert that 'wrap' pads only with multiples of the original area if         the, TestEdge, TestReflect, TestSymmetric, TestWrap

### Community 259 - "Community 259"
Cohesion: 0.09
Nodes (3): Basic test of array2string., Test custom format function for each element in array., TestArray2String

### Community 260 - "Community 260"
Cohesion: 0.09
Nodes (1): TestFillingValues

### Community 261 - "Community 261"
Cohesion: 0.10
Nodes (7): hello_world_f77(), Generates a single f77 file for testing, # TODO: Clean up to prevent passing --overwrite-signature, # TODO: populate, # TODO: f2py2e should not call sys.exit() after printing the version, # TODO: These should be tested separately, retreal_f77()

### Community 262 - "Community 262"
Cohesion: 0.11
Nodes (7): scale function used by the below tests, test that nans are propagated, Test that interp between opposite infs gives nan, Test that interp where both axes have a bound at inf gives nan, Test interp where the x axis has a bound at inf, Test interp where the f axis has a bound at inf, TestInterp

### Community 263 - "Community 263"
Cohesion: 0.16
Nodes (1): TestRegression

### Community 264 - "Community 264"
Cohesion: 0.15
Nodes (15): _display_as_base(), Various richly-typed exceptions, that also help us deal with string formatting i, A decorator that makes an exception class look like its base.      We use this t, Base class for all ufunc exceptions, Thrown when a ufunc loop cannot be found, Thrown when a binary resolution fails, Thrown when a ufunc input cannot be casted, Thrown when a ufunc output cannot be casted (+7 more)

### Community 265 - "Community 265"
Cohesion: 0.18
Nodes (13): array_function_method_impl(), array__get_implementing_args(), array_implement_c_array_function_creation(), call_array_function(), dispatcher_vectorcall(), fix_name_if_typeerror(), get_args_and_kwargs(), get_array_function() (+5 more)

### Community 266 - "Community 266"
Cohesion: 0.10
Nodes (13): This module is home to specific dtypes related functionality and their classes., Register a NumPy dtype for a DLPack ``(code, bits)`` pair so that     `numpy.fro, register_dlpack_dtype(), Protocol, TypedDict, A protocol class representing `~class.__array_function__`., # NOTE: This includes `builtins.bool`, but not `numpy.bool`., _SupportsArray (+5 more)

### Community 267 - "Community 267"
Cohesion: 0.10
Nodes (6): assert_dtype_not_equal(), Test whether different subarray dtypes hash differently., Test some data types that are equal, Test some simple cases that shouldn't be equal, Test some more complicated cases that shouldn't be equal, TestSubarray

### Community 268 - "Community 268"
Cohesion: 0.10
Nodes (1): TestIntegers

### Community 269 - "Community 269"
Cohesion: 0.10
Nodes (10): Provide test coverage when using provided estimators for optimal number of     b, Smaller datasets have the potential to cause issues with the data         adapti, Check a Value Error is thrown when an unknown string is passed in, Check that methods handle no variance in data         Primarily for Scott and FD, Check when IQR is 0, but variance exists, we return a reasonable value., Check the FD, Scott and Doane with outliers.          The FD estimates a smaller, Test that bin width for integer data is at least 1., Test that the bin-width>=1 requirement *only* applies to auto binning. (+2 more)

### Community 270 - "Community 270"
Cohesion: 0.13
Nodes (19): formatargspec(), formatargvalues(), getargs(), getargspec(), getargvalues(), iscode(), isfunction(), ismethod() (+11 more)

### Community 271 - "Community 271"
Cohesion: 0.16
Nodes (16): ABCPolyBase, Chebyshev, A Chebyshev series class.      The Chebyshev class provides the standard Python, HermiteE, A HermiteE series class.      The HermiteE class provides the standard Python nu, Hermite, A Hermite series class.      The Hermite class provides the standard Python nume, A sub-package for efficiently dealing with polynomials.  Within the documentatio (+8 more)

### Community 274 - "Community 274"
Cohesion: 0.15
Nodes (9): clear_and_catch_warnings, assert_warn_len_equal(), _get_fresh_mod(), my_cacw, test_clear_and_catch_warnings(), test_clear_and_catch_warnings_inherit(), test_suppress_warnings_module(), test_suppress_warnings_type() (+1 more)

### Community 275 - "Community 275"
Cohesion: 0.18
Nodes (18): as_complex(), as_factors(), as_integer(), as_numer_denom(), as_real(), as_term_coeff(), as_terms(), normalize() (+10 more)

### Community 276 - "Community 276"
Cohesion: 0.11
Nodes (20): average(), corrcoef(), cov(), _get_gamma(), _get_indexes(), _lerp(), percentile(), quantile() (+12 more)

### Community 277 - "Community 277"
Cohesion: 0.14
Nodes (14): _calculate_shapes(), _create_arrays(), _parse_input_dimensions(), Incrementally check and update core dimension sizes for a single argument., Parse broadcast and core dimensions for vectorize with a signature.      Argumen, Helper for calculating broadcast shapes with core dimensions., Helper for creating output arrays in vectorize., vectorize(pyfunc=np._NoValue, otypes=None, doc=None, excluded=None,     cache=Fa (+6 more)

### Community 278 - "Community 278"
Cohesion: 0.21
Nodes (19): rk_altfill(), rk_devfill(), rk_double(), rk_fill(), rk_gauss(), rk_hash(), rk_interval(), rk_long() (+11 more)

### Community 279 - "Community 279"
Cohesion: 0.22
Nodes (19): _discover_array_parameters(), discover_dtype_from_pyobject(), find_descriptor_from_array(), find_scalar_descriptor(), handle_promotion(), handle_scalar(), npy_cast_raw_scalar_item(), npy_discover_dtype_from_pytype() (+11 more)

### Community 280 - "Community 280"
Cohesion: 0.17
Nodes (17): _attempt_nocopy_reshape(), _fix_unknown_dimension(), PyArray_CreateMultiSortedStridePerm(), PyArray_CreateSortedStridePerm(), PyArray_Flatten(), PyArray_MatrixTranspose(), PyArray_Newshape(), PyArray_Ravel() (+9 more)

### Community 281 - "Community 281"
Cohesion: 0.12
Nodes (6): _get_argpartition_func(), *
get_argpartition_func(int type, NPY_SELECTKIND which)(), _get_partition_func(), *
get_partition_func(int type, NPY_SELECTKIND which)(), introselect_(), store_pivot()

### Community 282 - "Community 282"
Cohesion: 0.13
Nodes (9): npy_cpack(), npy_cpackf(), npy_cpackl(), npy_csetimag(), npy_csetimagf(), npy_csetimagl(), npy_csetreal(), npy_csetrealf() (+1 more)

### Community 283 - "Community 283"
Cohesion: 0.10
Nodes (2): Test that appended and prepended values are equal, TestStatistic

### Community 284 - "Community 284"
Cohesion: 0.11
Nodes (8): Tests for the array padding functions., Test behavior of pad's kwargs for the given mode., Test if C and F order is preserved for all pad modes., Check how padding behaves on arrays with an empty dimension., test_kwargs(), test_memory_layout_persistence(), TestEmpty, TestEmptyArray

### Community 285 - "Community 285"
Cohesion: 0.11
Nodes (8): Callback tests using Python thread-local storage instead of     compiler-provide, The reproduction of the reported issue requires specific input that     extensio, TestCBFortranCallstatement, TestF77Callback, TestF77CallbackPythonTLS, TestF90Callback, TestGH18335, TestGH25211

### Community 286 - "Community 286"
Cohesion: 0.17
Nodes (2): Check that np.dtype('x,y') matches [np.dtype('x'), np.dtype('y')]         Exampl, TestFromCTypes

### Community 287 - "Community 287"
Cohesion: 0.22
Nodes (5): ArrayLike, _assert_equal_type_and_value(), # NOTE: This class should be kept as an exact copy of the example from the, TestNDArrayOperatorsMixin, wrap_array_like()

### Community 288 - "Community 288"
Cohesion: 0.17
Nodes (1): TestBlock

### Community 290 - "Community 290"
Cohesion: 0.12
Nodes (12): array(), equal(), greater_equal(), less_equal(), not_equal(), This module contains a set of functions for vectorized string operations and met, Create a `~numpy.char.chararray`.      .. deprecated:: 2.5        ``chararray``, Return (x1 >= x2) element-wise.      Unlike `numpy.greater_equal`, this comparis (+4 more)

### Community 291 - "Community 291"
Cohesion: 0.13
Nodes (7): dict, bunch, coerce_text(), _Empty, TemplateDef, TemplateObject, TemplateObjectGetter

### Community 292 - "Community 292"
Cohesion: 0.12
Nodes (14): as_array(), as_string(), as_symbol(), as_ternary(), ewarn(), _Pair, Return object as TERNARY expression (cond?expr1:expr2)., Replace substrings of input that are enclosed in parenthesis.      Return a new (+6 more)

### Community 293 - "Community 293"
Cohesion: 0.18
Nodes (14): fortranSourceLines(), getDependencies(), isBlank(), isComment(), isContinuation(), isLabel(), LineIterator, lineType() (+6 more)

### Community 294 - "Community 294"
Cohesion: 0.11
Nodes (4): _nan_mask(), Functions that ignore NaN.  Functions ---------  - `nanmin` -- minimum non-NaN v, # TODO: What to do when arr1d = [1, np.nan] and weights = [0, 1]?, Parameters     ----------     a : array-like         Input array with at least 1

### Community 295 - "Community 295"
Cohesion: 0.12
Nodes (14): polyder(), polyval(), The polynomial coefficients, The name of the polynomial variable, The order or degree of the polynomial, The roots of the polynomial, where self(x) == 0, Return a derivative of this polynomial.          Refer to `polyder` for full doc, Return the roots of a polynomial with coefficients given in p.      .. note:: (+6 more)

### Community 296 - "Community 296"
Cohesion: 0.12
Nodes (16): addfield(), _checknames(), fromarrays(), fromrecords(), fromtextfile(), _guessvartypes(), openfile(), :mod:`numpy.ma..mrecords`  Defines the equivalent of :class:`numpy.recarrays` fo (+8 more)

### Community 297 - "Community 297"
Cohesion: 0.18
Nodes (19): can_cast_fields_safety(), can_cast_pyscalar_scalar_to(), cast_to_void_dtype_class(), _get_cast_safety_from_castingimpl(), give_bad_field_error(), _is_view_safe_cast(), nonstructured_to_structured_resolve_descriptors(), PyArray_CanCastArrayTo() (+11 more)

### Community 298 - "Community 298"
Cohesion: 0.16
Nodes (14): arrayflags_aligned_set(), arrayflags_farray_get(), arrayflags_fnc_get(), arrayflags_forc_get(), arrayflags_getitem(), arrayflags_new(), arrayflags_print(), arrayflags_setitem() (+6 more)

### Community 299 - "Community 299"
Cohesion: 0.25
Nodes (15): doubleTestCase, floatTestCase, FortranTestCase, intTestCase, longLongTestCase, longTestCase, Test Fortran matrix initialized from reshaped NumPy fortranarray, Test Fortran matrix initialized from nested list fortranarray (+7 more)

### Community 300 - "Community 300"
Cohesion: 0.11
Nodes (3): Only test hash runs at all., TestBuiltin, TestClassGetItem

### Community 301 - "Community 301"
Cohesion: 0.11
Nodes (1): TestStructured

### Community 302 - "Community 302"
Cohesion: 0.11
Nodes (2): This file adds basic tests to test the NEP 50 style promotion compatibility mode, # NOTE: It may make sense to normalize the behavior!

### Community 303 - "Community 303"
Cohesion: 0.11
Nodes (1): TestFromrecords

### Community 304 - "Community 304"
Cohesion: 0.18
Nodes (11): A, B, B0, B1, C, C0, D, HasNew (+3 more)

### Community 305 - "Community 305"
Cohesion: 0.19
Nodes (7): Test to make sure equivalent Travis O's r2array function, Test to make sure equivalent Travis O's r1array function, TestAtleast1d, TestAtleast2d, TestAtleast3d, TestHstack, TestVstack

### Community 306 - "Community 306"
Cohesion: 0.26
Nodes (2): Check that strings are stored in the arena when possible.      This tests implem, TestImplementation

### Community 307 - "Community 307"
Cohesion: 0.12
Nodes (2): TestMethodsWithUnicode, TestMixedTypeMethods

### Community 308 - "Community 308"
Cohesion: 0.16
Nodes (4): Check the message is formatted correctly for the decimal value.            Also, Check the message is formatted correctly, TestAlmostEqual, TestEqual

### Community 309 - "Community 309"
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

### Community 310 - "Community 310"
Cohesion: 0.12
Nodes (4): npyv_sum_u32(), npyv_sum_u64(), npyv_sumup_u16(), npyv_sumup_u8()

### Community 311 - "Community 311"
Cohesion: 0.11
Nodes (1): Where

### Community 312 - "Community 312"
Cohesion: 0.12
Nodes (11): _extendLine(), _extendLine_pretty(), _get_legacy_print_mode(), _object_format(), Array printing function  $Id: arrayprint.py,v 1.9 2005/09/13 13:58:44 teoliphant, # TODO: Custom repr for user DTypes, logic should likely move., Return the legacy print mode as an int., Object arrays containing lists should be printed unambiguously (+3 more)

### Community 313 - "Community 313"
Cohesion: 0.13
Nodes (6): _count_reduce_items(), _mean(), Array methods which are called by both the C-code for the method and the Python, # TODO: Optimize case when `where` is broadcast along a non-reduction, _std(), _var()

### Community 314 - "Community 314"
Cohesion: 0.15
Nodes (14): as_strided(), broadcast_arrays(), _broadcast_shape(), broadcast_shapes(), _broadcast_to(), _maybe_view_as_subclass(), Utilities that manipulate strides to achieve desirable effects.  An explanation, Create a sliding window view into the array with the given window shape.      Al (+6 more)

### Community 316 - "Community 316"
Cohesion: 0.24
Nodes (17): _append_char(), _append_field_name(), _append_str(), array_getbuffer(), _buffer_format_string(), _buffer_get_info(), _buffer_info_cmp(), _buffer_info_free() (+9 more)

### Community 317 - "Community 317"
Cohesion: 0.15
Nodes (8): array_dlpack(), array_dlpack_device(), array_get_dl_device(), create_dlpack_capsule(), dlpack_dtype_registry_lookup(), dlpack_export_registry_lookup(), fill_dl_tensor_information(), from_dlpack()

### Community 318 - "Community 318"
Cohesion: 0.11
Nodes (1): These tests are based on the doctests from `numpy/lib/recfunctions.py`.

### Community 319 - "Community 319"
Cohesion: 0.16
Nodes (10): assert_warns(), _assert_warns_context(), clear_and_catch_warnings, Fail unless the given callable throws the specified warning.      A warning of c, Context manager that resets warning registry for catching warnings      Warnings, Context manager and decorator doing much the same as     ``warnings.catch_warnin, Add a new suppressing filter or apply it if the state is entered.          Param, Append a new recording filter or apply it if the state is entered.          All (+2 more)

### Community 320 - "Community 320"
Cohesion: 0.11
Nodes (1): TestInformation

### Community 321 - "Community 321"
Cohesion: 0.11
Nodes (9): _DeprecationTestCase, Test that warnings are not raised.          This is just a shorthand for:, TestCharArray, TestDeprecatedDTypeAliases, TestDeprecatedDTypeParenthesizedRepeatCount, TestPyIntConversion, TestTakeOutDtype, TestTestDeprecated (+1 more)

### Community 322 - "Community 322"
Cohesion: 0.12
Nodes (13): CreateZeros, normalize_descr(), Check the creation of heterogeneous arrays zero-valued, Check creation of 0-dimensional objects, Check creation of single-dimensional objects, Check creation of multi-dimensional objects, Check the creation of heterogeneous arrays zero-valued (plain), Check the creation of heterogeneous arrays zero-valued (nested) (+5 more)

### Community 323 - "Community 323"
Cohesion: 0.13
Nodes (11): Check the creation of heterogeneous arrays (plain, single row), Check the reading of values in heterogeneous arrays (plain), Check the values of heterogeneous arrays (plain, multiple rows), ReadValuesPlain, TestBoolDefinition, TestCreateValuesPlainSingle, TestDocStrings, TestEmptyField (+3 more)

### Community 324 - "Community 324"
Cohesion: 0.14
Nodes (9): check_floatstatus(), # NOTE: Please avoid the use of numpy.testing since NPYV intrinsics, To only test single precision, Round to nearest even integer, assume CPU control register is set to rounding., To only test double precision, To call NPV intrinsics without the attribute 'npyv' and         auto suffixing i, _SIMD_FP32, _SIMD_FP64 (+1 more)

### Community 325 - "Community 325"
Cohesion: 0.11
Nodes (10): _NestedSequence, A module containing the `_NestedSequence` protocol., A protocol for representing nested sequences.      Warning     -------     `_Nes, Implement ``len(self)``., Implement ``self[x]``., Implement ``x in self``., Implement ``iter(self)``., Implement ``reversed(self)``. (+2 more)

### Community 326 - "Community 326"
Cohesion: 0.12
Nodes (2): byte_to_true(), simd_logical_or_u8()

### Community 327 - "Community 327"
Cohesion: 0.16
Nodes (10): adjust_offsets(), findslice_for_replace(), string_count(), string_find(), string_index(), string_pad(), string_replace(), string_rfind() (+2 more)

### Community 328 - "Community 328"
Cohesion: 0.16
Nodes (14): npyv_rev64_f32(), npyv_rev64_s16(), npyv_rev64_s32(), npyv_rev64_s8(), npyv_rev64_u16(), npyv_rev64_u32(), npyv_rev64_u8(), npyv_unzip_f32() (+6 more)

### Community 329 - "Community 329"
Cohesion: 0.15
Nodes (7): npyv_divc_s16(), npyv_divc_s64(), npyv_divc_s8(), npyv_divc_u64(), npyv__mullhi_u64(), npyv_sum_u32(), npyv_sumup_u16()

### Community 330 - "Community 330"
Cohesion: 0.14
Nodes (5): Create, MeshGrid, Benchmark for creation functions, Benchmark meshgrid generation, UfuncsFromDLP

### Community 331 - "Community 331"
Cohesion: 0.12
Nodes (6): poly(), polyfit(), _raise_power(), Functions to operate on polynomials., Find the coefficients of a polynomial with the given sequence of roots.      .., Least squares polynomial fit.      .. note::        This forms part of the old p

### Community 332 - "Community 332"
Cohesion: 0.18
Nodes (5): NumpyVersion, Utility to compare (NumPy) version strings.  The NumpyVersion class allows prope, Parse and compare numpy version strings.      NumPy has the following versioning, Compare major.minor.bugfix, Compare alpha/beta/rc/final.

### Community 333 - "Community 333"
Cohesion: 0.15
Nodes (6): fill_arraymethod_from_slots(), is_contiguous(), npy_default_get_strided_loop(), PyArrayMethod_FromSpec(), PyArrayMethod_FromSpec_int(), validate_spec()

### Community 334 - "Community 334"
Cohesion: 0.12
Nodes (9): Array2TestCase, Test Array2 nrows, ncols constructor, negative nrows, Test Array2 nrows, ncols constructor, negative ncols, Test Array2 nrows method, Test Array2 ncols method, Test Array2 resize method, negative nrows, Test Array2 resize method, negative ncols, Test Array2 __setitem__, __getitem__ methods (+1 more)

### Community 335 - "Community 335"
Cohesion: 0.13
Nodes (10): arraylikes(), is_parametric_dtype(), Tests for array coercion, mainly through testing `np.array` results directly. No, Returns True if the dtype is a parametric legacy dtype (itemsize     is 0, or a, Test parameters for functions converting an array into various array-likes., # TODO: This discrepancy _should_ be resolved, either by relaxing the, # TODO: This is arguably weird/wrong, but seems old:, TestSpecialAttributeLookupFailure (+2 more)

### Community 336 - "Community 336"
Cohesion: 0.12
Nodes (17): get_io_paths(), Tests that functions can be skipped     CLI :: skip:, Test that functions can be kept by only:     CLI :: only:, Tests that it is possible to return to file processing mode     CLI :: :     BUG, Checks the generation of files based on a module name     CLI :: -m, Check that pyf files are correctly generated with module structure     CLI :: -m, Lowers cases by flag or when -h is present      CLI :: --[no-]lower, Takes in a temporary file for testing and returns the expected output and input (+9 more)

### Community 337 - "Community 337"
Cohesion: 0.12
Nodes (3): Test that adjacent entries in an edge array can be equal, Test that if an edge array is input, its type is preserved, TestHistogramdd

### Community 338 - "Community 338"
Cohesion: 0.12
Nodes (2): TestConcatenator, TestRavelUnravelIndex

### Community 339 - "Community 339"
Cohesion: 0.12
Nodes (3): TestFillDiagonal, TestGrid, TestNdenumerate

### Community 340 - "Community 340"
Cohesion: 0.19
Nodes (1): TestZeroSizeFlexible

### Community 341 - "Community 341"
Cohesion: 0.13
Nodes (2): Metadata handling in promotion does not appear formalized         right now in N, TestTypes

### Community 342 - "Community 342"
Cohesion: 0.12
Nodes (1): TestCount

### Community 343 - "Community 343"
Cohesion: 0.12
Nodes (3): Ensures that the singleton bitgen is restored after a test, restore_singleton_bitgen(), TestBinomial

### Community 344 - "Community 344"
Cohesion: 0.12
Nodes (13): Test the runtime usage of `numpy.typing`., Test `typing.get_args`., Test `typing.get_origin`., Test `typing.get_type_hints`., Test `typing.get_type_hints` with string-representation of types., Test that ``TYPES.keys()`` and ``numpy.typing.__all__`` are synced., test_get_args(), test_get_origin() (+5 more)

### Community 345 - "Community 345"
Cohesion: 0.16
Nodes (5): compare_results(), This will fail if we change default axis, Compare lists of arrays., TestArraySplit, TestSplit

### Community 346 - "Community 346"
Cohesion: 0.26
Nodes (5): To test all float vector types at once, Test intrinsics:             npyv_rint_##SFX             npyv_ceil_##SFX, Test intrinsics:             npyv_max_##sfx             npyv_maxp_##sfx, Compare Not NaN. Test intrinsics:             npyv_notnan_##SFX, _SIMD_FP

### Community 347 - "Community 347"
Cohesion: 0.13
Nodes (4): assert_incompatible_shapes_raise(), assert_same_as_ufunc(), test_incompatible_shapes_raise_valueerror(), test_same_as_ufunc()

### Community 348 - "Community 348"
Cohesion: 0.15
Nodes (4): assert_arctan2_isnan(), assert_arctan2_isnzero(), assert_arctan2_ispzero(), TestArctan2SpecialValues

### Community 349 - "Community 349"
Cohesion: 0.12
Nodes (14): ByteorderValues, Check the byteorder of unicode arrays in round-trip conversions, Check the byteorder in unicode (size 1, UCS2 values), Check the byteorder in unicode (size 1, UCS4 values), Check the byteorder in unicode (size 2, UCS2 values), Check the byteorder in unicode (size 2, UCS4 values), Check the byteorder in unicode (size 1009, UCS2 values), Check the byteorder in unicode (size 1009, UCS4 values) (+6 more)

### Community 350 - "Community 350"
Cohesion: 0.16
Nodes (6): npyv_combine_f32(), npyv_combine_f64(), npyv_unzip_f32(), npyv_unzip_f64(), npyv_zip_f32(), npyv_zip_f64()

### Community 351 - "Community 351"
Cohesion: 0.18
Nodes (4): ArrayFunction, DuckArray, mock_broadcast_to(), mock_concatenate()

### Community 352 - "Community 352"
Cohesion: 0.24
Nodes (11): add_128(), ceildiv_128_64(), divmod_128_64(), floordiv_128_64(), gt_128(), mul_64_64(), neg_128(), shl_128() (+3 more)

### Community 353 - "Community 353"
Cohesion: 0.26
Nodes (11): BoolFormat, ComplexFloatingFormat, DatetimeFormat, FloatingFormat, _get_formatdict(), IntegerFormat, Formatter for subtypes of np.complexfloating, Formatter for subtypes of np.floating (+3 more)

### Community 354 - "Community 354"
Cohesion: 0.16
Nodes (11): _add_docstring(), add_newdoc(), geomspace(), linspace(), logspace(), _needs_add_docstring(), Return numbers spaced evenly on a log scale.      In linear space, the sequence, Return evenly spaced numbers over a specified interval.      Returns `num` evenl (+3 more)

### Community 355 - "Community 355"
Cohesion: 0.13
Nodes (1): This module contains a set of functions for vectorized string operations.

### Community 356 - "Community 356"
Cohesion: 0.26
Nodes (5): fill_command(), get_file_template(), paste_script_template_renderer(), sub(), Template

### Community 357 - "Community 357"
Cohesion: 0.17
Nodes (10): Array1TestCase, ArrayZTestCase, Test ArrayZ length constructor, negative, Test ArrayZ length method, Test ArrayZ resize method, negative length, Test ArrayZ __setitem__, __getitem__ methods, Test Array1 length constructor, negative, Test Array1 length method (+2 more)

### Community 358 - "Community 358"
Cohesion: 0.13
Nodes (5): Test sum function with wrong dimensions, Test sum function with non-container, Test reverse function, Test reverse function with wrong dimensions, VectorTestCase

### Community 359 - "Community 359"
Cohesion: 0.13
Nodes (5): Test that in most cases:            * `np.array(scalar, dtype=dtype)`, NumPy arrays are read/write which means that anything but invariant         beha, Signed integers are currently different in that they do not cast other         N, scalar_instances(), TestScalarDiscovery

### Community 360 - "Community 360"
Cohesion: 0.19
Nodes (4): Test if DeprecationWarnings are given and raised.          This first checks if, TestDeprecatedArrayAttributeSetting, TestDeprecatedViewDtypePropertySetter, TestTriDeprecationWithNonInteger

### Community 361 - "Community 361"
Cohesion: 0.15
Nodes (10): Test deprecation and future warnings., Check mode='full' and mode='economic' raise ValueError., # NOTE: As you can see, finalizing this deprecation breaks some (very) old, test_qr_mode_full_removed(), TestCtypesGetter, TestDeprecatedArrayWrap, TestDTypeAlignBool, TestRemovedGlobals (+2 more)

### Community 362 - "Community 362"
Cohesion: 0.23
Nodes (15): exc_iter(), Iterate over Cartesian product of *args, and if an exception is raised,     add, test_add_128(), test_ceildiv_128_64(), test_divmod_128_64(), test_floordiv_128_64(), test_gt_128(), test_mul_64_64() (+7 more)

### Community 363 - "Community 363"
Cohesion: 0.13
Nodes (1): TestBinomial

### Community 364 - "Community 364"
Cohesion: 0.15
Nodes (6): async_test_context_locality(), concurrent_context1(), concurrent_context2(), get_module(), Add a memory policy that returns a false pointer 64 bytes into the     actual al, test_context_locality()

### Community 365 - "Community 365"
Cohesion: 0.13
Nodes (1): TestMRecords

### Community 366 - "Community 366"
Cohesion: 0.13
Nodes (11): Check the reading of values in heterogeneous arrays (nested), Check reading the top fields of a nested array, Check reading the nested fields of a nested array (1st level), Check reading the nested fields of a nested array (2nd level), Check access nested descriptors of a nested array (1st level), Check access nested descriptors of a nested array (2nd level), Check the values of heterogeneous arrays (nested, single row), Check the values of heterogeneous arrays (nested, multiple rows) (+3 more)

### Community 367 - "Community 367"
Cohesion: 0.13
Nodes (4): # TODO: Include test for randint once it can broadcast, TestBinomial, TestMultinomial, TestSeed

### Community 368 - "Community 368"
Cohesion: 0.17
Nodes (1): TestRecord

### Community 369 - "Community 369"
Cohesion: 0.15
Nodes (4): TestKron, TestMayShareMemory, TestSqueeze, TestTile

### Community 370 - "Community 370"
Cohesion: 0.13
Nodes (2): check_itemsize(), TestReplaceOnArrays

### Community 371 - "Community 371"
Cohesion: 0.17
Nodes (4): foo, Compare the result of the object loop with non-object one, Test generic loops.      The loops to be tested are:          PyUFunc_ff_f_As_dd, TestUfuncGenericLoops

### Community 372 - "Community 372"
Cohesion: 0.13
Nodes (4): Test the behavior of the `strict` option., Check the message is formatted correctly when overflow can occur            (gh2, TestAssertAllclose, TestStringEqual

### Community 373 - "Community 373"
Cohesion: 0.13
Nodes (3): Test arrays with nan values in them., TestApproxEqual, TestArrayAssertLess

### Community 374 - "Community 374"
Cohesion: 0.20
Nodes (16): _check_axis_support(), check_for_trivial_loop(), _check_keepdims_support(), execute_ufunc_loop(), _get_coredim_sizes(), _has_output_coredims(), _initialize_variable_parts(), _parse_axes_arg() (+8 more)

### Community 376 - "Community 376"
Cohesion: 0.13
Nodes (1): ArrayCoercionSmall

### Community 377 - "Community 377"
Cohesion: 0.23
Nodes (7): collect_stats(), FunctionHtmlFormatter, # TODO: Handle compressed callgrind files, Custom HTML formatter to insert extra information with the lines., SourceFile, SourceFiles, HtmlFormatter

### Community 378 - "Community 378"
Cohesion: 0.13
Nodes (14): getbufsize(), geterr(), geterrcall(), Functions for changing global ufunc configuration  This provides helpers which w, Get the current way of handling floating-point errors.      Returns     -------, Set the size of the buffer used in ufuncs.      .. versionchanged:: 2.0, Return the size of the buffer used in ufuncs.      Returns     -------     getbu, Set how floating-point errors are handled.      Note that operations on integer (+6 more)

### Community 379 - "Community 379"
Cohesion: 0.14
Nodes (2): pow_zi(), z_div()

### Community 380 - "Community 380"
Cohesion: 0.13
Nodes (7): Arrayterator, A buffered iterator for big arrays.  This module solves the problem of iterating, Return a new arrayterator., Return corresponding data., A 1-D flat iterator for Arrayterator objects.          This iterator returns ele, Buffered iterator for big arrays.      `Arrayterator` creates a buffered iterato, The shape of the array to be iterated over.          For an example, see `Arrayt

### Community 381 - "Community 381"
Cohesion: 0.16
Nodes (14): _binary_method(), _disables_array_ufunc(), _inplace_binary_method(), _numeric_methods(), Mixin classes for custom array types that don't inherit from ndarray., True when __array_ufunc__ is set to None., # TODO: handle the optional third argument for __pow__?, Implement a forward binary method with a ufunc, e.g., __add__. (+6 more)

### Community 382 - "Community 382"
Cohesion: 0.15
Nodes (4): check_object(), get_lapack_lite_state(), lapack_lite_clear(), lapack_lite_free()

### Community 384 - "Community 384"
Cohesion: 0.16
Nodes (10): make_mask_descr(), _mareconstruct(), Private function allowing recursion in _replace_dtype_fields., Construct a dtype description list from a given dtype.      Returns a new dtype, Puts printoptions in result where mask is True.      Private function allowing f, Restore the internal state of the masked array, for         pickling purposes., Internal function that builds a new MaskedArray from the     information stored, _recursive_printoption() (+2 more)

### Community 385 - "Community 385"
Cohesion: 0.14
Nodes (2): initialize_abstract_dtypes(), make_raw_dtype()

### Community 386 - "Community 386"
Cohesion: 0.28
Nodes (13): apply_business_day_count(), apply_business_day_offset(), apply_business_day_roll(), array_busday_count(), array_busday_offset(), array_is_busday(), business_day_count(), business_day_offset() (+5 more)

### Community 387 - "Community 387"
Cohesion: 0.20
Nodes (14): build(), build_and_import_extension(), _c_compile(), compile_extension_module(), _convert_str_to_file(), get_so_suffix(), _make_methods(), _make_source() (+6 more)

### Community 388 - "Community 388"
Cohesion: 0.13
Nodes (5): Test min function with bad list, Test min function with non-container, Test min function with wrong dimensions, Test scale function with wrong type, SuperTensorTestCase

### Community 389 - "Community 389"
Cohesion: 0.13
Nodes (5): Test min function with bad list, Test min function with non-container, Test min function with wrong dimensions, Test scale function with wrong type, TensorTestCase

### Community 390 - "Community 390"
Cohesion: 0.13
Nodes (7): TestEval, TestF77CommonBlockReader, TestFortranGroupCounters, TestFortranReader, TestFunctionReturn, TestNoSpace, TestUnicodeComment

### Community 391 - "Community 391"
Cohesion: 0.16
Nodes (7): Test raising a matrix to an integer power works as expected., Check that 'not implemented' operations produce a failure., TestAlgebra, TestCasting, TestCtor, TestIndexing, TestMatrixReturn

### Community 392 - "Community 392"
Cohesion: 0.15
Nodes (4): Check most properties relevant to "canonical" versions of a dtype,         which, TestDTypeMakeCanonical, TestFromDTypeAttribute, TestFromDTypeProtocol

### Community 393 - "Community 393"
Cohesion: 0.16
Nodes (14): Check formatting when using print, Check formatting.          This is only for the str function, and only for simpl, Test the str.format method with NumPy scalar types, Check formatting of nan & inf.          This is only for the str function, and o, Check formatting of complex types.          This is only for the str function, a, Check inf/nan formatting of complex types., test_complex_inf_nan(), test_complex_type_print() (+6 more)

### Community 394 - "Community 394"
Cohesion: 0.13
Nodes (2): Test printing of scalar types., TestRealScalars

### Community 395 - "Community 395"
Cohesion: 0.16
Nodes (13): _key_func(), Validate that mypy correctly infers the return-types of     the expressions in `, Validate that the code in `path` properly during runtime., Split at the first occurrence of the ``:`` character.      Windows drive-letters, Strip the filename and line number from a mypy message., `re.sub` helper function for stripping module names., Clears the cache and run mypy before running any of the typing tests.      The m, run_mypy() (+5 more)

### Community 396 - "Community 396"
Cohesion: 0.14
Nodes (8): bad_arcsinh(), _check_branch_cut(), on_powerpc(), True if we are running on a Power PC platform., The blocklisted trig functions are not accurate on aarch64/PPC for     complex25, Check loss of precision in complex arc* functions, Check for a branch cut in a function.      Assert that `x0` lies on a branch cut, TestComplexFunctions

### Community 397 - "Community 397"
Cohesion: 0.23
Nodes (10): _check_ufunc_fperr(), extobj_get_extobj_dict(), extobj_make_extobj(), _extract_pyvals(), fetch_curr_extobj_state(), _get_bufsize_errmask(), init_extobj(), make_extobj_capsule() (+2 more)

### Community 398 - "Community 398"
Cohesion: 0.16
Nodes (15): convert_ufunc_arguments(), _keepdims_converter(), _parse_axis(), PyUFunc_Accumulate(), PyUFunc_GenericReduction(), PyUFunc_Reduce(), PyUFunc_Reduceat(), reducelike_promote_and_resolve() (+7 more)

### Community 399 - "Community 399"
Cohesion: 0.18
Nodes (13): check_api_version(), get_api_versions(), main(), MismatchCAPIError, Return current C API checksum and the recorded checksum.      Return current C A, Emits a MismatchCAPIWarning if the C API version needs updating., matrix_rank(), outer() (+5 more)

### Community 400 - "Community 400"
Cohesion: 0.14
Nodes (1): Mapping

### Community 401 - "Community 401"
Cohesion: 0.34
Nodes (13): dlamc1_(), dlamc2_(), dlamc3_(), dlamc4_(), dlamc5_(), dlamch_(), lsame_(), slamc1_() (+5 more)

### Community 402 - "Community 402"
Cohesion: 0.14
Nodes (14): nanargmax(), nanargmin(), nancumprod(), nancumsum(), nanprod(), nansum(), Return the indices of the minimum values in the specified axis ignoring     NaNs, Return the indices of the maximum values in the specified axis ignoring     NaNs (+6 more)

### Community 403 - "Community 403"
Cohesion: 0.18
Nodes (14): _fix_defaults(), _fix_output(), _get_fieldspec(), join_by(), _keep_fields(), Superposes arrays fields by fields      Parameters     ----------     arrays : a, Join arrays `r1` and `r2` on key `key`.      The key should be either a string o, Join arrays `r1` and `r2` on keys.     Alternative to join_by, that always retur (+6 more)

### Community 404 - "Community 404"
Cohesion: 0.14
Nodes (14): _assert_stacked_2d(), _is_empty_2d(), matmul(), pinv(), qr(), QRResult, Compute the (Moore-Penrose) pseudo-inverse of a matrix.      Calculate the gener, Transpose each matrix in a stack of matrices.      Unlike np.transpose, this onl (+6 more)

### Community 407 - "Community 407"
Cohesion: 0.18
Nodes (6): npyv_all_s64(), npyv_all_u64(), npyv_any_s64(), npyv_any_u64(), npyv_cmpgt_s64(), npyv_cmpgt_u64()

### Community 409 - "Community 409"
Cohesion: 0.14
Nodes (8): __array_namespace_info__, Array API Inspection namespace  This is the namespace for inspection functions a, The default device used for new NumPy arrays.          For NumPy, this always re, The default data types used for new NumPy arrays.          For NumPy, this alway, The array API data types supported by NumPy.          Note that this function on, Get the array API inspection namespace for NumPy.      The array API inspection, The devices supported by NumPy.          For NumPy, this always returns ``('cpu', Return a dictionary of array API library capabilities.          The resulting di

### Community 410 - "Community 410"
Cohesion: 0.14
Nodes (7): check_fpu_mode(), pytest_itemcollected(), Pytest configuration and fixtures for the Numpy test suite., Check FPU precision mode was not changed during test collection.      The clumsy, Check FPU precision mode was not changed during the test., Filter out the wall of DeprecationWarnings., warnings_errors_and_rng()

### Community 411 - "Community 411"
Cohesion: 0.16
Nodes (4): npyv_combine_f64(), npyv_rev64_u16(), npyv_rev64_u8(), npyv_unzip_f64()

### Community 412 - "Community 412"
Cohesion: 0.15
Nodes (4): MatrixTestCase, Test ceil function with wrong dimensions, Test ceil function with non-array, Test det function with bad list

### Community 413 - "Community 413"
Cohesion: 0.26
Nodes (12): doubleTestCase, floatTestCase, intTestCase, longLongTestCase, longTestCase, scharTestCase, shortTestCase, ucharTestCase (+4 more)

### Community 414 - "Community 414"
Cohesion: 0.26
Nodes (12): doubleTestCase, floatTestCase, intTestCase, longLongTestCase, longTestCase, scharTestCase, shortTestCase, ucharTestCase (+4 more)

### Community 415 - "Community 415"
Cohesion: 0.26
Nodes (12): doubleTestCase, floatTestCase, intTestCase, longLongTestCase, longTestCase, scharTestCase, shortTestCase, ucharTestCase (+4 more)

### Community 416 - "Community 416"
Cohesion: 0.26
Nodes (12): doubleTestCase, floatTestCase, intTestCase, longLongTestCase, longTestCase, scharTestCase, shortTestCase, ucharTestCase (+4 more)

### Community 417 - "Community 417"
Cohesion: 0.14
Nodes (2): Test whether matrix.sum(axis=1) preserves orientation.         Fails in NumPy <=, TestProperties

### Community 418 - "Community 418"
Cohesion: 0.16
Nodes (7): Test functions for fftpack.helper module  Copied from fftpack.helper by Pearu Pe, Test 2D input, which has uneven dimension sizes, Test the new (>=v1.15) and old implementations are equal (see #10073), TestFFTFreq, TestFFTShift, TestIRFFTN, TestRFFTFreq

### Community 419 - "Community 419"
Cohesion: 0.20
Nodes (2): Test ufunc call memory overlap handling, TestUFunc

### Community 420 - "Community 420"
Cohesion: 0.19
Nodes (2): TestBroadcast, TestCreationFuncs

### Community 421 - "Community 421"
Cohesion: 0.29
Nodes (1): TestArrayLike

### Community 422 - "Community 422"
Cohesion: 0.14
Nodes (1): TestParameters

### Community 423 - "Community 423"
Cohesion: 0.14
Nodes (3): Tests for polyutils module., TestDomain, TestMisc

### Community 424 - "Community 424"
Cohesion: 0.26
Nodes (6): Only testing for integer splits., TestColumnStack, TestDsplit, TestDstack, TestHsplit, TestVsplit

### Community 425 - "Community 425"
Cohesion: 0.14
Nodes (1): TestConcatenate

### Community 426 - "Community 426"
Cohesion: 0.32
Nodes (2): Test extend reduce sum intrinsics:             npyv_sumup_##sfx, Logical operations for boolean types.         Test intrinsics:             npyv_

### Community 427 - "Community 427"
Cohesion: 0.14
Nodes (13): dtype(), get_dtype(), Test the two-argument ufuncs match python builtin behavior., Helper to work around pd_NA boolean behavior, Cartesian project of missing data sentinel and string coercion options, test_dtype_creation(), test_dtype_equality(), test_nonzero() (+5 more)

### Community 428 - "Community 428"
Cohesion: 0.14
Nodes (1): TestSymbolic

### Community 429 - "Community 429"
Cohesion: 0.14
Nodes (1): TestArrayAlmostEqualNulp

### Community 430 - "Community 430"
Cohesion: 0.19
Nodes (7): npyv_pack_b8_b16(), npyv_pack_b8_b32(), npyv_pack_b8_b64(), npyv_round_s32_f32(), npyv_round_s32_f64(), npyv__trunc_s32_f32(), npyv__trunc_s32_f64()

### Community 431 - "Community 431"
Cohesion: 0.21
Nodes (8): DatetimeAsString, DatetimeAstypeCoarser, DatetimeToObject, DatetimeWideRange, Cast datetime64 to a coarser calendar unit (Y/M/W).     Y and M require year/mon, Convert datetime64 to a Python datetime.date / datetime.datetime array.     Each, Same as DatetimeAsString but spanning a wider date range     (~+-2700 years from, ISO string formatting from datetime64 — exercises set_datetimestruct_days     on

### Community 432 - "Community 432"
Cohesion: 0.21
Nodes (7): Returns an ordered array of the given size and dtype., Returns a randomly-shuffled array., Returns an ordered array., Returns an array that's in descending order., Returns an array that has the same value everywhere., Returns an array with blocks that are all sorted., SortGenerator

### Community 433 - "Community 433"
Cohesion: 0.15
Nodes (7): NdindexBenchmark, Setup method called before each benchmark run., Measure time taken by np.ndindex.         It creates an iterator that goes over, Measure time taken by itertools.product.         Same goal: iterate over all ind, Measure peak memory used when fully consuming         np.ndindex iterator by con, Measure peak memory used when fully consuming         itertools.product iterator, Benchmark comparing numpy.ndindex() and itertools.product()     for different mu

### Community 434 - "Community 434"
Cohesion: 0.17
Nodes (2): ScalarMath, ScalarStr

### Community 435 - "Community 435"
Cohesion: 0.24
Nodes (10): main(), parse_loop_header(), parse_string(), parse_structure(), parse_values(), process_file(), process_str(), The returned line number is from the beginning of the string, starting     at ze (+2 more)

### Community 436 - "Community 436"
Cohesion: 0.18
Nodes (13): getcallprotoargument(), getcallstatement(), getmultilineblock(), getpymethoddef(), getusercode(), getusercode1(), hascallstatement(), isarrayofstrings() (+5 more)

### Community 437 - "Community 437"
Cohesion: 0.17
Nodes (13): hasnote(), hasresultnote(), isfunction(), isfunction_wrap(), isintent_c(), islogical(), islogicalfunction(), islong_double() (+5 more)

### Community 438 - "Community 438"
Cohesion: 0.17
Nodes (13): append(), diff(), gradient(), Return the gradient of an N-dimensional array.      The gradient is computed usi, Calculate the n-th discrete difference along the given axis.      The first diff, r"""     Unwrap by taking the complement of large deltas with respect to the per, r"""     Integrate along the given axis using the composite trapezoidal rule., Append values to the end of an array.      Parameters     ----------     arr : a (+5 more)

### Community 440 - "Community 440"
Cohesion: 0.29
Nodes (9): _descr_from_subtype(), PyArray_CastScalarDirect(), PyArray_CastScalarToCtype(), PyArray_DescrFromScalar(), PyArray_DescrFromTypeObject(), PyArray_FromScalar(), PyArray_Scalar(), PyArray_ScalarAsCtype() (+1 more)

### Community 441 - "Community 441"
Cohesion: 0.19
Nodes (4): empty_array_like(), unique_numeric(), unique_string(), unique_vstring()

### Community 442 - "Community 442"
Cohesion: 0.23
Nodes (8): _next(), npy_clear_floatstatus(), npy_clear_floatstatus_barrier(), npy_get_floatstatus(), npy_get_floatstatus_barrier(), _npy_spacing(), npy_spacingf(), npy_spacingl()

### Community 443 - "Community 443"
Cohesion: 0.17
Nodes (2): NpyCapsule_FromVoidPtr(), NpyCapsule_FromVoidPtrAndDesc()

### Community 444 - "Community 444"
Cohesion: 0.17
Nodes (3): MyArr, MyArrNoWrap, test_array_wrap()

### Community 445 - "Community 445"
Cohesion: 0.15
Nodes (2): Regression test for https://github.com/numpy/numpy/issues/5982, TestOperations

### Community 446 - "Community 446"
Cohesion: 0.26
Nodes (1): TestPickling

### Community 447 - "Community 447"
Cohesion: 0.17
Nodes (6): TestAllocatableCharacterArray, TestModuleAndSubroutine, TestModuleDocString, TestModuleFilterPublicEntities, TestModuleWithoutPublicEntities, TestUsedModule

### Community 448 - "Community 448"
Cohesion: 0.15
Nodes (1): TestWritebackIfCopy

### Community 449 - "Community 449"
Cohesion: 0.21
Nodes (2): NIterError, TestFromiter

### Community 450 - "Community 450"
Cohesion: 0.28
Nodes (2): assert_mt19937_state_equal(), TestSetState

### Community 451 - "Community 451"
Cohesion: 0.15
Nodes (1): TestRecFunctions

### Community 452 - "Community 452"
Cohesion: 0.18
Nodes (8): _add_keepdims(), hack in keepdims behavior into a function taking an axis, Test it translates from arg<func> to <func>, Test it errors when indices has too few dimensions, Test everything is ok with empty results, even with inserted dims, Test that non-indexing dimensions are broadcast in both directions, TestPutAlongAxis, TestTakeAlongAxis

### Community 453 - "Community 453"
Cohesion: 0.18
Nodes (2): TestApplyAlongAxis, TestApplyOverAxes

### Community 454 - "Community 454"
Cohesion: 0.15
Nodes (1): TestLowlevelAPIAccess

### Community 455 - "Community 455"
Cohesion: 0.15
Nodes (1): TestPower

### Community 456 - "Community 456"
Cohesion: 0.22
Nodes (1): TestRationalFunctions

### Community 457 - "Community 457"
Cohesion: 0.15
Nodes (12): AssignValues, Check the assignment of unicode arrays with values, Check the assignment of valued arrays (size 1, UCS2 values), Check the assignment of valued arrays (size 1, UCS4 values), Check the assignment of valued arrays (size 2, UCS2 values), Check the assignment of valued arrays (size 2, UCS4 values), Check the assignment of valued arrays (size 1009, UCS4 values), TestAssignValues_1009_UCS4 (+4 more)

### Community 458 - "Community 458"
Cohesion: 0.15
Nodes (9): buffer_length(), CreateZeros, Check the creation of zero-valued arrays, Check the creation of zero-valued arrays (size 1), Check the creation of zero-valued arrays (size 2), Check the creation of zero-valued arrays (size 1009), TestCreateZeros_1, TestCreateZeros_1009 (+1 more)

### Community 459 - "Community 459"
Cohesion: 0.15
Nodes (12): CreateValues, Check the creation of unicode arrays with values, Check the creation of valued arrays (size 1, UCS2 values), Check the creation of valued arrays (size 1, UCS4 values), Check the creation of valued arrays (size 2, UCS2 values), Check the creation of valued arrays (size 1009, UCS2 values), Check the creation of valued arrays (size 1009, UCS4 values), TestCreateValues_1009_UCS2 (+4 more)

### Community 460 - "Community 460"
Cohesion: 0.24
Nodes (9): call_converter_function(), double_from_ucs4(), npy_to_cdouble(), npy_to_cfloat(), npy_to_double(), npy_to_float(), npy_to_generic(), npy_to_generic_with_converter() (+1 more)

### Community 462 - "Community 462"
Cohesion: 0.32
Nodes (10): diophantine_dfs(), diophantine_precompute(), diophantine_simplify(), euclid(), get_array_memory_extents(), offset_bounds_from_strides(), solve_diophantine(), solve_may_have_internal_overlap() (+2 more)

### Community 463 - "Community 463"
Cohesion: 0.24
Nodes (7): _add_trailing_padding(), _dtype_from_pep3118(), _fix_names(), _prod(), Replace names which are None with the next unused f%d name, Inject the specified number of padding bytes at the end of a dtype, _Stream

### Community 464 - "Community 464"
Cohesion: 0.18
Nodes (10): array_function_dispatch(), array_function_from_dispatcher(), finalize_array_function_like(), get_array_function_like_doc(), Implementation of __array_function__ overrides from NEP-18., Decorator for adding dispatch with the __array_function__ protocol.      See NEP, Like array_function_dispatcher, but with function arguments flipped., Verify that a dispatcher function has the right signature. (+2 more)

### Community 465 - "Community 465"
Cohesion: 0.17
Nodes (12): decode(), encode(), _get_num_chars(), _join(), mod(), Helper function that returns the number of characters per field in     a string, Helper function to cast a result back into an array     with the appropriate dty, Return a string which is the concatenation of the strings in the     sequence `s (+4 more)

### Community 466 - "Community 466"
Cohesion: 0.30
Nodes (11): conv(), expand_sub(), find_and_remove_repl_patterns(), find_repl_patterns(), parse_structure(), process_file(), process_str(), Obtain a unique key given a dictionary. (+3 more)

### Community 467 - "Community 467"
Cohesion: 0.27
Nodes (7): add_gufuncs(), copy_input(), copy_output(), fft_loop(), irfft_loop(), _pocketfft_umath_exec(), rfft_impl()

### Community 468 - "Community 468"
Cohesion: 0.20
Nodes (3): ieeeck_(), ilaenv_(), iparmq_()

### Community 470 - "Community 470"
Cohesion: 0.23
Nodes (7): decide_view_dtype_path(), get_optional_set_dtype_and_dtype(), npy_fallocate(), PyArray_ToFile(), PyArray_ToList(), PyArray_View(), recursive_tolist()

### Community 471 - "Community 471"
Cohesion: 0.32
Nodes (11): _any_labels_are_negative(), get_combined_dims_view(), get_single_op_view(), parse_operand_subscripts(), parse_output_subscripts(), prepare_op_axes(), *
PyArray_EinsteinSum(char *subscripts, npy_intp nop,
                    PyArrayObject **op_in,
                    PyArray_Descr *dtype,
                    NPY_ORDER order, NPY_CASTING casting,
                    PyArrayObject *out)(), unbuffered_loop_nop1_ndim2() (+3 more)

### Community 472 - "Community 472"
Cohesion: 0.23
Nodes (6): _append_new(), _PyArray_LegacyDescrNewFromPrototype(), PyArray_RegisterCanCast(), PyArray_RegisterCastFunc(), PyArray_RegisterDataType(), _warn_if_cast_exists_already()

### Community 473 - "Community 473"
Cohesion: 0.20
Nodes (3): npyv_pack_b8_b16(), npyv_pack_b8_b32(), npyv_pack_b8_b64()

### Community 474 - "Community 474"
Cohesion: 0.17
Nodes (12): pcg_mcg_128_step_r(), pcg_mcg_128_xsh_rs_64_boundedrand_r(), pcg_mcg_128_xsh_rs_64_random_r(), pcg_mcg_128_xsl_rr_64_boundedrand_r(), pcg_mcg_128_xsl_rr_64_random_r(), pcg_oneseq_128_xsh_rs_64_boundedrand_r(), pcg_oneseq_128_xsh_rs_64_random_r(), pcg_output_xsh_rs_128_64() (+4 more)

### Community 475 - "Community 475"
Cohesion: 0.17
Nodes (12): pcg_mcg_64_step_r(), pcg_mcg_64_xsh_rs_32_boundedrand_r(), pcg_mcg_64_xsh_rs_32_random_r(), pcg_mcg_64_xsl_rr_32_boundedrand_r(), pcg_mcg_64_xsl_rr_32_random_r(), pcg_oneseq_64_xsh_rs_32_boundedrand_r(), pcg_oneseq_64_xsh_rs_32_random_r(), pcg_output_xsh_rs_64_32() (+4 more)

### Community 476 - "Community 476"
Cohesion: 0.27
Nodes (8): mulhilo64(), philox4x64_R(), _philox4x64bumpkey(), _philox4x64round(), philox_next(), philox_next32(), philox_next64(), _umul128()

### Community 477 - "Community 477"
Cohesion: 0.18
Nodes (12): assert_allclose(), assert_approx_equal(), assert_array_compare(), assert_array_equal(), assert_array_less(), assert_equal(), build_err_msg(), Raises an AssertionError if two array_like objects are not equal.      Given two (+4 more)

### Community 478 - "Community 478"
Cohesion: 0.17
Nodes (1): f90_return_integer

### Community 479 - "Community 479"
Cohesion: 0.17
Nodes (1): f90_return_logical

### Community 480 - "Community 480"
Cohesion: 0.36
Nodes (11): npyv__bitscan_revnz_u32(), npyv__bitscan_revnz_u64(), npyv__divh128_u64(), npyv_divisor_s16(), npyv_divisor_s32(), npyv_divisor_s64(), npyv_divisor_s8(), npyv_divisor_u16() (+3 more)

### Community 481 - "Community 481"
Cohesion: 0.20
Nodes (3): npyv_setall_s64(), npyv_setall_u64(), npyv__setr_epi64()

### Community 482 - "Community 482"
Cohesion: 0.18
Nodes (2): npyv_cmpgt_s64(), npyv_cmpgt_u64()

### Community 483 - "Community 483"
Cohesion: 0.23
Nodes (5): num_codepoints_for_utf8_bytes(), num_utf8_bytes_for_codepoint(), utf8_buffer_size(), utf8_decode(), utf8_size()

### Community 484 - "Community 484"
Cohesion: 0.18
Nodes (1): NAType

### Community 485 - "Community 485"
Cohesion: 0.17
Nodes (6): Ensure faulty usage is discovered., Test casting for a single value., Test proper casting for two different values., Test if `x` already matching desired output are passed through., Test results if `as_index=True`., TestAsPairs

### Community 486 - "Community 486"
Cohesion: 0.17
Nodes (1): TestConditionalShortcuts

### Community 487 - "Community 487"
Cohesion: 0.17
Nodes (4): Ensure that array printing does not use NumPy Dragon4 formatting     for user-de, test_multithreaded_array_printing(), test_user_defined_floating_dtype_printing_does_not_corrupt_precision(), TestComplexArray

### Community 488 - "Community 488"
Cohesion: 0.17
Nodes (1): _assert_equal_hash()

### Community 489 - "Community 489"
Cohesion: 0.17
Nodes (2): TestComparisons, TestComparisonsMixed2

### Community 490 - "Community 490"
Cohesion: 0.17
Nodes (4): Test that timedelta64 array + integer array triggers deprecation., Test that datetime64 array + integer array triggers deprecation., Verify the specific non-associative case from gh-31255 warns., TestDeprecatedGenericTimedelta

### Community 491 - "Community 491"
Cohesion: 0.17
Nodes (1): TestString

### Community 492 - "Community 492"
Cohesion: 0.21
Nodes (10): float16_ma(), float32_ma(), float64_ma(), MachArLike, Machine arithmetic parameters for float16., Machine arithmetic parameters for float32., Machine arithmetic parameters for float64., Test that finfo properties match expected machine arithmetic values. (+2 more)

### Community 493 - "Community 493"
Cohesion: 0.17
Nodes (3): Tests to exercise indexerrors not covered by other tests., take from a 0-length dimension, TestIndexErrors

### Community 494 - "Community 494"
Cohesion: 0.17
Nodes (1): TestArange

### Community 495 - "Community 495"
Cohesion: 0.17
Nodes (1): TestRecord

### Community 496 - "Community 496"
Cohesion: 0.21
Nodes (3): TestArithmetic, TestDerivative, trim()

### Community 497 - "Community 497"
Cohesion: 0.17
Nodes (1): TestJoinBy

### Community 498 - "Community 498"
Cohesion: 0.21
Nodes (2): Test scalar buffer interface adheres to PEP 3118, TestScalarPEP3118

### Community 499 - "Community 499"
Cohesion: 0.24
Nodes (5): To test all boolean vector types at once, Pack multiple vectors into one         Test intrinsics:             npyv_pack_b8, Test intrinsics:             npyv_any_##SFX             npyv_all_##SFX, Create list of consecutive numbers according to number of vector's lanes., _SIMD_BOOL

### Community 500 - "Community 500"
Cohesion: 0.21
Nodes (2): comp_state(), warmup()

### Community 501 - "Community 501"
Cohesion: 0.26
Nodes (7): RNGData, TestDefaultRNG, TestMT19937, TestPCG64, TestPCG64DXSM, TestPhilox, TestSFC64

### Community 502 - "Community 502"
Cohesion: 0.17
Nodes (3): Test that numpy.fix emits a DeprecationWarning., TestFixDeprecation, TestUfunclike

### Community 503 - "Community 503"
Cohesion: 0.20
Nodes (2): npyv_pack_b8_b16(), npyv_pack_b8_b32()

### Community 504 - "Community 504"
Cohesion: 0.22
Nodes (3): npyv_pack_b8_b16(), npyv_pack_b8_b32(), npyv_pack_b8_b64()

### Community 505 - "Community 505"
Cohesion: 0.18
Nodes (11): amax(), amin(), max(), min(), Sum of array elements over a given axis.      Parameters     ----------     a :, Return the maximum of an array or maximum along an axis.      Parameters     ---, Return the maximum of an array or maximum along an axis.      `amax` is an alias, Return the minimum of an array or minimum along an axis.      Parameters     --- (+3 more)

### Community 506 - "Community 506"
Cohesion: 0.25
Nodes (6): _ctypes, _getintp_ctype(), Return the shape tuple as an array of some other c-types         type. For examp, Return the strides tuple as an array of some other         c-types type. For exa, A pointer to the memory area of the array as a Python integer.         This memo, (c_intp*self.ndim): A ctypes array of length self.ndim where         the basetyp

### Community 507 - "Community 507"
Cohesion: 0.18
Nodes (9): fftfreq(), fftshift(), ifftshift(), Discrete Fourier Transforms - _helper.py, Return the Discrete Fourier Transform sample frequencies.      The returned floa, Return the Discrete Fourier Transform sample frequencies     (for usage with rff, Shift the zero-frequency component to the center of the spectrum.      This func, The inverse of `fftshift`. Although identical for even-length `x`, the     funct (+1 more)

### Community 508 - "Community 508"
Cohesion: 0.24
Nodes (5): FutureWarning, MaskedArrayFutureWarning, TestArgsort, TestDtypeSet, TestMinimumMaximum

### Community 509 - "Community 509"
Cohesion: 0.22
Nodes (3): npyv_pack_b8_b16(), npyv_pack_b8_b32(), npyv_pack_b8_b64()

### Community 510 - "Community 510"
Cohesion: 0.20
Nodes (2): array_converter_wrap(), find_wrap()

### Community 511 - "Community 511"
Cohesion: 0.25
Nodes (11): add_numeric_cast(), add_other_to_and_from_string_cast(), dtype_kind_to_ordering(), initialize_void_and_object_globals(), PyArray_AddCastingImplementation(), PyArray_AddCastingImplementation_FromSpec(), PyArray_InitializeCasts(), PyArray_InitializeNumericCasts() (+3 more)

### Community 513 - "Community 513"
Cohesion: 0.18
Nodes (6): _CopyMode, _NoValueType, Module defining global singleton classes.  This module raises a RuntimeError if, Special keyword value.      The instance of this class may be used as the defaul, An enumeration for the copy modes supported     by numpy.copy() and numpy.array(, _SignatureDescriptor

### Community 514 - "Community 514"
Cohesion: 0.18
Nodes (1): Object

### Community 516 - "Community 516"
Cohesion: 0.22
Nodes (3): npyv_pack_b8_b16(), npyv_pack_b8_b32(), npyv_pack_b8_b64()

### Community 517 - "Community 517"
Cohesion: 0.31
Nodes (5): allocateMemory(), allocateRows(), Array2(), deallocateMemory(), resize()

### Community 518 - "Community 518"
Cohesion: 0.18
Nodes (11): compiler_check_f2pycli(), Check that modules are named correctly      CLI :: defaults, Check that distutils backend and related options fail     CLI :: --fcompiler --h, Ensures that the extra object can be specified when using meson backend, CLI :: --no-freethreading-compatible, CLI :: --freethreading_compatible, test_cli_obj(), test_freethreading_compatible() (+3 more)

### Community 519 - "Community 519"
Cohesion: 0.24
Nodes (3): TestPut, TestPutMask, TestTake

### Community 520 - "Community 520"
Cohesion: 0.27
Nodes (1): TestBool

### Community 521 - "Community 521"
Cohesion: 0.20
Nodes (2): TestBaseRepr, TestBinaryRepr

### Community 522 - "Community 522"
Cohesion: 0.18
Nodes (2): TestCross, TestTensordot

### Community 523 - "Community 523"
Cohesion: 0.22
Nodes (4): dispatched_one_arg(), _new_duck_type_and_implements(), Create a duck array type and implements functions., TestArrayFunctionDispatch

### Community 524 - "Community 524"
Cohesion: 0.25
Nodes (4): Return the content of a string buffer as integer value.          For example:, TestDocStringArguments, TestFixedString, TestString

### Community 525 - "Community 525"
Cohesion: 0.18
Nodes (1): TestDivision

### Community 526 - "Community 526"
Cohesion: 0.20
Nodes (2): TestArrayAlmostEqual, TestULP

### Community 527 - "Community 527"
Cohesion: 0.29
Nodes (9): _128Bit, _16Bit, _32Bit, _64Bit, _8Bit, _96Bit, NBitBase, A module with the precisions of generic `~numpy.number` types. (+1 more)

### Community 528 - "Community 528"
Cohesion: 0.25
Nodes (6): add_dtype_loops(), comp_name(), get_min_max(), get_value_range(), patch_cached_int_loop(), resolve_descriptors_with_scalars()

### Community 529 - "Community 529"
Cohesion: 0.24
Nodes (3): npyv_setall_s64(), npyv_setall_u64(), npyv__setr_epi64()

### Community 530 - "Community 530"
Cohesion: 0.36
Nodes (1): Import

### Community 531 - "Community 531"
Cohesion: 0.20
Nodes (1): Records

### Community 532 - "Community 532"
Cohesion: 0.29
Nodes (5): npy__cpu_baseline_fid(), npy__cpu_check_env(), npy__cpu_dispatch_fid(), npy_cpu_init(), npy__cpu_validate_baseline()

### Community 533 - "Community 533"
Cohesion: 0.36
Nodes (7): find_item(), find_item_buckets(), identity_list_hash(), PyArrayIdentityHash_GetItem(), PyArrayIdentityHash_SetItemDefault(), PyArrayIdentityHash_SetItemDefaultLockHeld(), _resize_if_necessary()

### Community 534 - "Community 534"
Cohesion: 0.20
Nodes (10): _array2string(), _formatArray(), _leading_trailing(), _make_options_dict(), Set printing options.      These options determine the way floating point number, Keep only the N-D corners (leading and trailing edges) of an array.      Should, Make a dictionary out of the non-None arguments, plus conversion of     *legacy*, Return a string representation of an array.      Parameters     ----------     a (+2 more)

### Community 535 - "Community 535"
Cohesion: 0.29
Nodes (8): dtype_from_ctypes_type(), _from_ctypes_array(), _from_ctypes_scalar(), _from_ctypes_structure(), _from_ctypes_union(), Conversion from ctypes to dtype.  In an ideal world, we could achieve this throu, Construct a dtype object from a ctypes type, Return the dtype type with endianness included if it's the case

### Community 536 - "Community 536"
Cohesion: 0.20
Nodes (3): Provide python-space access to the functions exposed in numpy/__init__.pxd for t, byte_bounds(), Returns pointers to the end-points of an array.      Parameters     ----------

### Community 537 - "Community 537"
Cohesion: 0.22
Nodes (4): Wrapper to strip each member of the output of `method`.          Parameters, Returns the dtype of the input variable., Returns dtype for datetime64 and type of dtype otherwise., Set StringConverter attributes directly.          Parameters         ----------

### Community 538 - "Community 538"
Cohesion: 0.20
Nodes (10): apply_along_fields(), _common_stride(), _get_fields_and_offsets(), Converts an n-D unstructured array into an (n-1)-D structured array.      The la, Apply function 'func' as a reduction across fields of a structured array.      T, Returns a flat list of (dtype, count, offset) tuples of all the     scalar field, Returns the stride between the fields, or None if the stride is not     constant, Converts an n-D structured array into an (n+1)-D unstructured array.      The ne (+2 more)

### Community 539 - "Community 539"
Cohesion: 0.29
Nodes (6): init_genrand(), mt19937_init_by_array(), mt19937_next(), mt19937_next32(), mt19937_next64(), mt19937_next_double()

### Community 540 - "Community 540"
Cohesion: 0.22
Nodes (2): busdaycalendar_init(), normalize_holidays_list()

### Community 541 - "Community 541"
Cohesion: 0.29
Nodes (8): _fill_with_none(), PyArray_ClearArray(), PyArray_ClearBuffer(), PyArray_INCREF(), PyArray_Item_INCREF(), PyArray_Item_XDECREF(), PyArray_SetObjectsToNone(), PyArray_XDECREF()

### Community 543 - "Community 543"
Cohesion: 0.20
Nodes (1): f90_return_char

### Community 544 - "Community 544"
Cohesion: 0.20
Nodes (1): f90_return_complex

### Community 546 - "Community 546"
Cohesion: 0.20
Nodes (1): f90_return_real

### Community 547 - "Community 547"
Cohesion: 0.20
Nodes (9): allows_array_function_override(), allows_array_ufunc_override(), get_overridable_numpy_array_functions(), get_overridable_numpy_ufuncs(), Tools for testing implementations of __array_function__ and ufunc overrides, List all numpy ufuncs overridable via `__array_ufunc__`      Parameters     ----, Determine if a function can be overridden via `__array_ufunc__`      Parameters, List all numpy functions overridable via `__array_function__`      Parameters (+1 more)

### Community 549 - "Community 549"
Cohesion: 0.20
Nodes (2): Test the error paths, including for memory leaks, TestArrayLikes

### Community 550 - "Community 550"
Cohesion: 0.20
Nodes (1): TestConstant

### Community 551 - "Community 551"
Cohesion: 0.20
Nodes (4): Tests for chebyshev module., TestDerivative, TestGauss, TestPrivate

### Community 552 - "Community 552"
Cohesion: 0.20
Nodes (6): # NOTE: list(b'123') == [49, 50, 51], Regression test for ticket 1948., test_empty_indexing(), TestChar, TestComparisonsMixed1, TestWhitespace

### Community 553 - "Community 553"
Cohesion: 0.20
Nodes (1): TestNewScalarIndexing

### Community 554 - "Community 554"
Cohesion: 0.20
Nodes (1): TestShape

### Community 555 - "Community 555"
Cohesion: 0.27
Nodes (1): LoadTxtBase

### Community 556 - "Community 556"
Cohesion: 0.20
Nodes (4): Tests for legendre module., TestCompanion, TestFitting, TestGauss

### Community 557 - "Community 557"
Cohesion: 0.20
Nodes (9): CreateValues, Check the creation of heterogeneous arrays with values, Check creation from tuples, Check the creation of heterogeneous arrays (plain, multiple rows), Check the creation of heterogeneous arrays (nested, single row), Check the creation of heterogeneous arrays (nested, multiple rows), TestCreateValuesNestedMultiple, TestCreateValuesNestedSingle (+1 more)

### Community 558 - "Community 558"
Cohesion: 0.20
Nodes (2): TestNDArrayArrayFunction, TestNDArrayMethods

### Community 559 - "Community 559"
Cohesion: 0.20
Nodes (1): TestRandint

### Community 560 - "Community 560"
Cohesion: 0.20
Nodes (1): Test_SIMD_MODULE

### Community 561 - "Community 561"
Cohesion: 0.20
Nodes (2): _signs(), TestRemainder

### Community 562 - "Community 562"
Cohesion: 0.20
Nodes (1): Tests for the NumpyVersion class.

### Community 564 - "Community 564"
Cohesion: 0.27
Nodes (10): _get_end_of_name(), _get_size(), _is_alnum_underscore(), _is_alpha_underscore(), _is_same_name(), _next_non_white_space(), _parse_signature(), PyUFunc_FromFuncAndData() (+2 more)

### Community 565 - "Community 565"
Cohesion: 0.28
Nodes (3): npyv_setall_s64(), npyv_setall_u64(), npyv__setr_epi64()

### Community 566 - "Community 566"
Cohesion: 0.28
Nodes (3): Put, PutMask, Take

### Community 567 - "Community 567"
Cohesion: 0.22
Nodes (1): CustomInplace

### Community 569 - "Community 569"
Cohesion: 0.33
Nodes (8): build_func_rx(), iter_source_files(), main(), Return (code_without_comments, updated_in_block).     Removes // line comments a, Return a list of source files under 'root', where filenames end with any of the, Scan a single file.     Returns list of (func_name, line_number, path_str, raw_l, scan_file(), strip_comments()

### Community 570 - "Community 570"
Cohesion: 0.25
Nodes (3): A data-type scalar that allows field access as attribute lookup., Pretty-print all fields., record

### Community 571 - "Community 571"
Cohesion: 0.25
Nodes (9): _clean_args(), Helper function for delegating arguments to Python string     functions.      Ma, For each element in `a`, return a list of the words in the     string, using `se, For each element in `a`, return a list of the lines in the     element, breaking, For each element in `a`, return a copy of the string where all     characters oc, _rsplit(), _split(), _splitlines() (+1 more)

### Community 572 - "Community 572"
Cohesion: 0.22
Nodes (1): foddity

### Community 573 - "Community 573"
Cohesion: 0.22
Nodes (7): fix(), isneginf(), isposinf(), Module of functions that are like ufuncs in acting on arrays and optionally stor, Test element-wise for negative infinity, return result as bool array.      Param, Round to nearest integer towards zero.      .. deprecated:: 2.5         `numpy.f, Test element-wise for positive infinity, return result as bool array.      Param

### Community 574 - "Community 574"
Cohesion: 0.22
Nodes (9): _clear_cast_info_after_get_loop_failure(), define_cast_for_descrs(), get_legacy_dtype_cast_function(), get_wrapped_legacy_cast_function(), init_cast_info(), _multistep_cast_auxdata_clone(), _multistep_cast_auxdata_clone_int(), wrap_aligned_transferfunction() (+1 more)

### Community 575 - "Community 575"
Cohesion: 0.42
Nodes (8): _array_descr_builtin(), _array_descr_walk(), _array_descr_walk_fields(), _array_descr_walk_subarray(), _is_array_descr_builtin(), _normalize_byteorder(), PyArray_DescrHash(), _PyArray_DescrHashImp()

### Community 576 - "Community 576"
Cohesion: 0.44
Nodes (8): can_cast_fields(), _equivalent_fields(), _equivalent_subarrays(), PyArray_LegacyCanCastSafely(), PyArray_LegacyCanCastTo(), PyArray_LegacyCanCastTypeTo(), PyArray_LegacyEquivTypenums(), PyArray_LegacyEquivTypes()

### Community 578 - "Community 578"
Cohesion: 0.28
Nodes (3): aradixsort0(), nth_byte(), radixsort0()

### Community 579 - "Community 579"
Cohesion: 0.22
Nodes (4): A, B, C, D

### Community 580 - "Community 580"
Cohesion: 0.28
Nodes (4): Typing tests for `numpy._core._ufunc_config`., Write1, Write2, Write3

### Community 585 - "Community 585"
Cohesion: 0.36
Nodes (4): allocateMemory(), Array1(), deallocateMemory(), resize()

### Community 586 - "Community 586"
Cohesion: 0.36
Nodes (4): allocateMemory(), ArrayZ(), deallocateMemory(), resize()

### Community 587 - "Community 587"
Cohesion: 0.25
Nodes (2): allocateMemory(), Farray()

### Community 588 - "Community 588"
Cohesion: 0.22
Nodes (3): GenericObject, print_new_cast_table(), Prints new casts, the values given are default "can-cast" values, not     actual

### Community 589 - "Community 589"
Cohesion: 0.22
Nodes (1): Tests for the private NumPy argument parsing functionality. They mainly exists t

### Community 590 - "Community 590"
Cohesion: 0.25
Nodes (5): This file tests the generic aspects of ArrayMethod.  At the time of writing this, Test `ndarray.__class_getitem__`., TestClassGetItem, TestResolveDescriptors, TestSimpleStridedCall

### Community 591 - "Community 591"
Cohesion: 0.22
Nodes (1): TestArrayRepr

### Community 592 - "Community 592"
Cohesion: 0.33
Nodes (2): TestArithmetic, trim()

### Community 593 - "Community 593"
Cohesion: 0.25
Nodes (3): TestCompanion, TestFitting, TestInterpolate

### Community 594 - "Community 594"
Cohesion: 0.22
Nodes (1): TestMisc

### Community 595 - "Community 595"
Cohesion: 0.22
Nodes (4): # TODO: Allowing unsafe casting by, # NOTE: some of the operations may be supported, # TODO: add absolute (gold standard) time span limit strings, TestDateTimeData

### Community 596 - "Community 596"
Cohesion: 0.28
Nodes (1): TestGeneric

### Community 597 - "Community 597"
Cohesion: 0.22
Nodes (1): TestMultinomial

### Community 598 - "Community 598"
Cohesion: 0.31
Nodes (2): TestArithmetic, trim()

### Community 599 - "Community 599"
Cohesion: 0.36
Nodes (7): _check_api_module(), limited_api_cython_module_names(), limited_api_module_names(), _module_names(), test_limited_api_abi3(), test_limited_api_cython(), test_limited_opaque()

### Community 600 - "Community 600"
Cohesion: 0.22
Nodes (1): TestMatrixPower

### Community 601 - "Community 601"
Cohesion: 0.22
Nodes (2): Tests suite for mrecords.  :author: Pierre Gerard-Marchant :contact: pierregm_at, TestMRecordsImport

### Community 604 - "Community 604"
Cohesion: 0.22
Nodes (1): TestTemporaryElide

### Community 605 - "Community 605"
Cohesion: 0.22
Nodes (1): TestIterNested

### Community 606 - "Community 606"
Cohesion: 0.36
Nodes (2): Test ones_like, zeros_like, empty_like and full_like, TestLikeFuncs

### Community 607 - "Community 607"
Cohesion: 0.36
Nodes (1): TestRequire

### Community 608 - "Community 608"
Cohesion: 0.22
Nodes (1): TestArrayFunctionImplementation

### Community 609 - "Community 609"
Cohesion: 0.28
Nodes (5): ArrayFunctionInterceptor, Tests for polynomial module., test_polygrid2d_array_function_hook(), test_polyval2d_array_function_hook(), TestFraction

### Community 610 - "Community 610"
Cohesion: 0.22
Nodes (1): TestRandint

### Community 611 - "Community 611"
Cohesion: 0.22
Nodes (1): TestMultinomial

### Community 612 - "Community 612"
Cohesion: 0.22
Nodes (3): Tests for structural pattern matching support (PEP 634)., TestPathUsage, TestPatternMatching

### Community 613 - "Community 613"
Cohesion: 0.22
Nodes (2): test_writeable(), TestSlidingWindowView

### Community 614 - "Community 614"
Cohesion: 0.22
Nodes (1): TestComparisons

### Community 615 - "Community 615"
Cohesion: 0.31
Nodes (4): FindFuncs, ParseCall, Tests which scan for certain occurrences in the code, they may not find all of t, test_warning_calls()

### Community 616 - "Community 616"
Cohesion: 0.36
Nodes (6): buffer_info_from_unicode(), fb_del(), fb_nextbuf(), it_nextbuf(), process_stringlike(), stream_python_file()

### Community 617 - "Community 617"
Cohesion: 0.28
Nodes (4): find_missing(), FindAttributes, main(), Find top-level attributes/functions/classes in stubs files.      Do this by walk

### Community 618 - "Community 618"
Cohesion: 0.31
Nodes (3): DiffLinter, Original Author: Josh Wilson (@person142)         Source:             https://gi, Run C-API borrowed-ref checker

### Community 619 - "Community 619"
Cohesion: 0.33
Nodes (5): countchar(), default_find(), fastsearch(), two_way_count(), two_way_find()

### Community 620 - "Community 620"
Cohesion: 0.22
Nodes (9): _check_and_copy_sig_to_signature(), prepare_input_arguments_for_outer(), replace_with_wrapped_result_and_return(), _set_full_args_out(), try_trivial_scalar_call(), tuple_all_none(), ufunc_generic_fastcall(), ufunc_generic_vectorcall() (+1 more)

### Community 622 - "Community 622"
Cohesion: 0.25
Nodes (2): Benchmarks for the NumPy small-allocation cache.  NumPy caches data allocations, SmallArrayCreation

### Community 623 - "Community 623"
Cohesion: 0.25
Nodes (1): Polynomial

### Community 624 - "Community 624"
Cohesion: 0.36
Nodes (7): get_data(), get_indexes(), get_indexes_rand(), get_square(), get_squares(), get_values(), Generates a cached random array that covers several scenarios that     may affec

### Community 625 - "Community 625"
Cohesion: 0.25
Nodes (8): array_repr(), _array_repr_implementation(), dtype_is_implied(), dtype_short_repr(), Determine if the given dtype is implied by the representation     of its values., Convert a dtype to a short form which evaluates to the same dtype.      The inte, Internal version of array_repr() that allows overriding array2string., Return the string representation of an array.      Parameters     ----------

### Community 626 - "Community 626"
Cohesion: 0.25
Nodes (7): _get_format_function(), Formatter for structured np.void objects.      This does not work on structured, This is a second way to initialize StructuredVoidFormat,         using the raw d, Implements the repr for structured-void scalars. It is called from the     scala, find the right formatting function for the dtype_, StructuredVoidFormat, _void_scalar_to_string()

### Community 627 - "Community 627"
Cohesion: 0.25
Nodes (5): bincount(), Create the numpy._core.multiarray namespace for backward compatibility. In v1.16, bincount(x, /, weights=None, minlength=0)      Count number of occurrences of ea, ravel_multi_index(multi_index, dims, mode='raise', order='C')      Converts a tu, ravel_multi_index()

### Community 628 - "Community 628"
Cohesion: 0.29
Nodes (7): english_capitalize(), english_lower(), english_upper(), String-handling utilities to avoid locale-dependence.  Used primarily to generat, Apply English case rules to convert ASCII strings to all lower case.      This i, Apply English case rules to convert ASCII strings to all upper case.      This i, Apply English case rules to convert the first character of an ASCII     string t

### Community 629 - "Community 629"
Cohesion: 0.25
Nodes (2): foo, procedure

### Community 630 - "Community 630"
Cohesion: 0.36
Nodes (7): doxy_config(), doxy_gen(), DoxyTpl, main(), Generate Doxygen configuration file., Fetch all Doxygen sub-config files and gather it with the main config file., Template

### Community 631 - "Community 631"
Cohesion: 0.29
Nodes (5): F2PYError, throw_error, buildcallback(), buildcallbacks(), Build call-back mechanism for f2py2e.  Copyright 1999 -- 2011 Pearu Peterson all

### Community 632 - "Community 632"
Cohesion: 0.32
Nodes (6): append_needs(), errmess(), get_needs(), C declarations, CPP macros, and C functions for f2py2e. Only required declaratio, Write an error message to stderr.      This indirection is needed because sys.st, # TODO: These should be dynamically generated, too many mapped to int things,

### Community 633 - "Community 633"
Cohesion: 0.54
Nodes (7): assubr(), createfuncwrapper(), createsubrwrapper(), Rules for building C/API module with f2py2e.  Copyright 1999 -- 2011 Pearu Peter, useiso_c_binding(), useiso_fortran_env(), var2fixfortran()

### Community 634 - "Community 634"
Cohesion: 0.25
Nodes (4): Traverse expression tree with visit function.          The visit function is app, Check if self contains other., Return a set of symbols contained in self., Return a set of expressions used as atoms in polynomial self.

### Community 635 - "Community 635"
Cohesion: 0.25
Nodes (8): _nanmedian1d(), _nanquantile_1d(), _nanquantile_ureduce_func(), Private function for rank 1 arrays. Compute the median ignoring NaNs.     See na, Private function that doesn't support extended axis or keepdims.     These metho, Equivalent to arr1d[~arr1d.isnan()], but in a different order      Presumably fa, Private function for rank 1 arrays. Compute quantile ignoring NaNs.     See nanp, _remove_nan_1d()

### Community 636 - "Community 636"
Cohesion: 0.25
Nodes (5): polydiv(), polyint(), Return an antiderivative (indefinite integral) of this polynomial.          Refe, Return an antiderivative (indefinite integral) of a polynomial.      .. note::, Returns the quotient and remainder of polynomial division.      .. note::

### Community 637 - "Community 637"
Cohesion: 0.25
Nodes (8): _assert_2d(), multi_dot(), _multi_dot_matrix_chain_order(), _multi_dot_three(), Compute the dot product of two or more arrays in a single function call,     whi, Find the best order for three arrays and do the multiplication.      For three a, Return a np.array that encodes the optimal order of multiplications.      The op, Actually do the multiplication with the given order.

### Community 638 - "Community 638"
Cohesion: 0.25
Nodes (8): matrix_norm(), _multi_svd_norm(), norm(), Compute a function of the singular values of the 2-D matrices in `x`.      This, Matrix or vector norm.      This function is able to return one of eight differe, Computes the matrix norm of a matrix (or a stack of matrices) ``x``.      This f, Computes the vector norm of a vector (or batch of vectors) ``x``.      This func, vector_norm()

### Community 639 - "Community 639"
Cohesion: 0.46
Nodes (7): array_datetime_as_string(), convert_datetimestruct_utc_to_local(), get_localtime(), lossless_unit_from_datetimestruct(), NpyDatetime_GetDatetimeISO8601StrLen(), NpyDatetime_MakeISO8601Datetime(), NpyDatetime_ParseISO8601Datetime()

### Community 640 - "Community 640"
Cohesion: 0.32
Nodes (8): get_fields_transfer_function(), get_n_to_n_transfer_function(), get_one_to_n_transfer_function(), get_subarray_broadcast_transfer_function(), get_subarray_transfer_function(), PyArray_CastRawArrays(), PyArray_GetDTypeTransferFunction(), PyArray_GetMaskedDTypeTransferFunction()

### Community 641 - "Community 641"
Cohesion: 0.29
Nodes (8): array_concatenate(), PyArray_CompareLists(), PyArray_Concatenate(), PyArray_ConcatenateArrays(), PyArray_ConcatenateFlattenedArrays(), PyArray_ConcatenateInto(), PyArray_GetPriority(), PyArray_GetSubType()

### Community 642 - "Community 642"
Cohesion: 0.36
Nodes (4): rotl(), sfc64_next(), sfc64_next32(), sfc64_next64()

### Community 643 - "Community 643"
Cohesion: 0.36
Nodes (1): TestNumpyConfig

### Community 644 - "Community 644"
Cohesion: 0.25
Nodes (1): TestBasic

### Community 645 - "Community 645"
Cohesion: 0.25
Nodes (1): TestVecString

### Community 646 - "Community 646"
Cohesion: 0.29
Nodes (4): get_docdir(), _path(), # TODO: implement test methods for other example Fortran codes, TestDocAdvanced

### Community 647 - "Community 647"
Cohesion: 0.25
Nodes (2): Test cases related to more complex DType promotions.  Further promotion     test, TestPromotion

### Community 648 - "Community 648"
Cohesion: 0.25
Nodes (1): TestErrstate

### Community 649 - "Community 649"
Cohesion: 0.25
Nodes (1): TestIOSF

### Community 650 - "Community 650"
Cohesion: 0.25
Nodes (4): Test `int` kind_func for integers up to 10**40., Test (processor-dependent) `real` kind_func for real numbers         of up to 31, Test kind_func for quadruple precision [`real(16)`] of 32+ digits ., TestKind

### Community 651 - "Community 651"
Cohesion: 0.25
Nodes (1): TestMisc

### Community 652 - "Community 652"
Cohesion: 0.25
Nodes (1): TestCReaderUnitTests

### Community 653 - "Community 653"
Cohesion: 0.25
Nodes (1): TestConversion

### Community 656 - "Community 656"
Cohesion: 0.25
Nodes (1): TestResize

### Community 657 - "Community 657"
Cohesion: 0.25
Nodes (1): TestEvaluation

### Community 658 - "Community 658"
Cohesion: 0.25
Nodes (1): TestMisc

### Community 659 - "Community 659"
Cohesion: 0.46
Nodes (1): TestSetState

### Community 660 - "Community 660"
Cohesion: 0.25
Nodes (1): TestSeed

### Community 661 - "Community 661"
Cohesion: 0.43
Nodes (3): TestCReturnReal, TestFReturnReal, TestReturnReal

### Community 662 - "Community 662"
Cohesion: 0.25
Nodes (1): params_1()

### Community 663 - "Community 663"
Cohesion: 0.25
Nodes (2): TestAbsoluteNegative, TestMinMax

### Community 664 - "Community 664"
Cohesion: 0.29
Nodes (5): check_python_h_included_first(), diff_files(), process_files(), Find the diff since the given SHA.      Adapted from lint.py, Check that the passed file includes Python.h first if it does at all.      Perha

### Community 665 - "Community 665"
Cohesion: 0.29
Nodes (2): get_initial_from_ufunc(), PyArray_NewLegacyWrappingArrayMethod()

### Community 666 - "Community 666"
Cohesion: 0.43
Nodes (7): add_unwrap_loop(), f2h(), floor_mod(), h2f(), init_unwrap_ufunc(), unwrap_half_loop(), unwrap_loop()

### Community 667 - "Community 667"
Cohesion: 0.29
Nodes (2): get_wrapping_auxdata(), wrapping_method_get_loop()

### Community 669 - "Community 669"
Cohesion: 0.29
Nodes (2): ops_module, subroutine

### Community 670 - "Community 670"
Cohesion: 0.43
Nodes (3): LaplaceInplace, MaxesOfDots, A magical feature score for each feature in each dataset         :ref:`Haxby et

### Community 671 - "Community 671"
Cohesion: 0.52
Nodes (6): _bad_strides(), cblas_matrixproduct(), gemm(), gemv(), _select_matrix_shape(), syrk()

### Community 672 - "Community 672"
Cohesion: 0.43
Nodes (4): initialize_keywords(), _npy_parse_arguments(), raise_incorrect_number_of_positional_args(), raise_missing_argument()

### Community 673 - "Community 673"
Cohesion: 0.29
Nodes (3): This file is separate from ``_add_newdocs.py`` so that it can be mocked out by o, # TODO: These docs probably need an if to highlight the default rather than, # TODO: work out how to put this on the base class, np.floating

### Community 674 - "Community 674"
Cohesion: 0.29
Nodes (5): greater(), less(), Return (x1 > x2) element-wise.      Unlike `numpy.greater`, this comparison is p, Return (self > other) element-wise.          See Also         --------         g, Return (self < other) element-wise.          See Also         --------         l

### Community 675 - "Community 675"
Cohesion: 0.33
Nodes (4): _ArrayMemoryError, Thrown when an array cannot be allocated, Convert a number of bytes into a binary size string, MemoryError

### Community 676 - "Community 676"
Cohesion: 0.29
Nodes (2): c_void_p, dummy_ctype

### Community 677 - "Community 677"
Cohesion: 0.29
Nodes (7): iscomplex(), iscomplexfunction(), iscomplexfunction_warn(), islong_complex(), outmess(), process_f2cmap_dict(), Update the Fortran-to-C type mapping dictionary with new mappings and     return

### Community 678 - "Community 678"
Cohesion: 0.29
Nodes (7): copy(), delete(), meshgrid(), _quantile_ureduce_func(), Return a tuple of coordinate matrices from coordinate vectors.      Make N-D coo, Return a new array with sub-arrays along an axis deleted. For a one     dimensio, Return an array copy of the given object.      Parameters     ----------     a :

### Community 679 - "Community 679"
Cohesion: 0.29
Nodes (6): _get_vectorize_dtype(), iterable(), _parse_gufunc_signature(), _piecewise_dispatcher(), Parse string signatures for a generalized universal function.      Arguments, Check whether or not an object can be iterated over.      Parameters     -------

### Community 680 - "Community 680"
Cohesion: 0.33
Nodes (7): append_fields(), _izip_records(), merge_arrays(), Returns an iterator of concatenated items from a sequence of arrays.      Parame, Merge arrays field by field.      Parameters     ----------     seqarrays : sequ, Add new fields to an existing array.      The names of the fields are given with, rec_append_fields()

### Community 681 - "Community 681"
Cohesion: 0.29
Nodes (5): EighResult, SlogdetResult, SVDResult, NamedTuple, XYGrid

### Community 683 - "Community 683"
Cohesion: 0.52
Nodes (6): add_state(), copy_state(), gen_next(), get_coef(), horner1(), mt19937_jump_state()

### Community 684 - "Community 684"
Cohesion: 0.57
Nodes (6): can_elide_temp(), can_elide_temp_unary(), check_callers(), check_unique_temporary(), find_addr(), try_binary_elide()

### Community 685 - "Community 685"
Cohesion: 0.33
Nodes (5): ABCArray1, ABCArray2, ArrayBase, AttrArray, NotArray

### Community 687 - "Community 687"
Cohesion: 0.29
Nodes (1): Object

### Community 688 - "Community 688"
Cohesion: 0.29
Nodes (7): assert_(), assert_no_gc_cycles(), _assert_no_gc_cycles_context(), _assert_valid_refcount(), Assert that works in release mode.     Accepts callable msg to allow deferring e, Check that ufuncs don't mishandle refcount of object `1`.     Used in a few regr, Fail if the given callable produces any reference cycles.      If called with al

### Community 689 - "Community 689"
Cohesion: 0.29
Nodes (6): __bit_generator_ctor(), __generator_ctor(), __randomstate_ctor(), Pickling helper function that returns a bit generator object      Parameters, Pickling helper function that returns a Generator object      Parameters     ---, Pickling helper function that returns a legacy RandomState-like object      Para

### Community 690 - "Community 690"
Cohesion: 0.29
Nodes (1): TestABC

### Community 691 - "Community 691"
Cohesion: 0.29
Nodes (1): TestNested

### Community 692 - "Community 692"
Cohesion: 0.29
Nodes (3): Ensure that end values are exact., Check correct behavior of unsigned dtypes if there is a negative         differe, TestLinearRamp

### Community 693 - "Community 693"
Cohesion: 0.29
Nodes (1): TestPadWidth

### Community 694 - "Community 694"
Cohesion: 0.29
Nodes (1): TestEvaluation

### Community 695 - "Community 695"
Cohesion: 0.48
Nodes (4): TestData, TestDataF77, TestDataMultiplierF77, TestDataWithCommentsF77

### Community 696 - "Community 696"
Cohesion: 0.29
Nodes (1): TestDTypeClasses

### Community 697 - "Community 697"
Cohesion: 0.29
Nodes (1): TestMultivariateHypergeometric

### Community 698 - "Community 698"
Cohesion: 0.29
Nodes (1): TestSeed

### Community 700 - "Community 700"
Cohesion: 0.29
Nodes (1): TestISOC

### Community 701 - "Community 701"
Cohesion: 0.29
Nodes (1): TestEvaluation

### Community 702 - "Community 702"
Cohesion: 0.43
Nodes (1): TestQR

### Community 703 - "Community 703"
Cohesion: 0.29
Nodes (2): TestTensorinv, TestTensorsolve

### Community 704 - "Community 704"
Cohesion: 0.52
Nodes (1): TestView

### Community 705 - "Community 705"
Cohesion: 0.29
Nodes (1): TestAssignment

### Community 706 - "Community 706"
Cohesion: 0.29
Nodes (1): TestFancyIndexing

### Community 707 - "Community 707"
Cohesion: 0.29
Nodes (7): iter_indices(), test_iter_best_order_c_index_1d(), test_iter_best_order_c_index_2d(), test_iter_best_order_c_index_3d(), test_iter_best_order_f_index_1d(), test_iter_best_order_f_index_2d(), test_iter_best_order_f_index_3d()

### Community 708 - "Community 708"
Cohesion: 0.29
Nodes (2): This test array_equal for a few combinations:          - are the two inputs the, TestArrayComparisons

### Community 709 - "Community 709"
Cohesion: 0.29
Nodes (1): TestMoveaxis

### Community 710 - "Community 710"
Cohesion: 0.29
Nodes (1): Test_sctype2char

### Community 711 - "Community 711"
Cohesion: 0.29
Nodes (1): TestIsSubDType

### Community 712 - "Community 712"
Cohesion: 0.29
Nodes (2): Check the numpy config is valid., TestNumPyConfigs

### Community 713 - "Community 713"
Cohesion: 0.29
Nodes (1): TestGetImplementingArgs

### Community 714 - "Community 714"
Cohesion: 0.29
Nodes (1): TestConstants

### Community 715 - "Community 715"
Cohesion: 0.29
Nodes (1): params_0()

### Community 716 - "Community 716"
Cohesion: 0.29
Nodes (3): test direct implementation of these magic methods, test implementations via __float__, TestRoundingFunctions

### Community 717 - "Community 717"
Cohesion: 0.29
Nodes (2): TestBitwiseUFuncs, TestFrompyfunc

### Community 718 - "Community 718"
Cohesion: 0.47
Nodes (3): IsAligned(), IsUintAligned(), raw_array_is_aligned()

### Community 719 - "Community 719"
Cohesion: 0.60
Nodes (5): extract_cpuinfo_field(), get_feature_from_proc_cpuinfo(), get_file_size(), has_list_item(), read_file()

### Community 720 - "Community 720"
Cohesion: 0.33
Nodes (6): prod(), Return the shape of an array.      Parameters     ----------     a : array_like, Return the product of array elements over a given axis.      Parameters     ----, Return the number of elements along a given axis.      Parameters     ----------, shape(), size()

### Community 721 - "Community 721"
Cohesion: 0.33
Nodes (6): Return a new array with the specified shape.      If the new array is larger tha, Return a contiguous flattened array.      A 1-D array, containing the elements o, Returns a reshaped ndarray without changing data.      Parameters     ----------, ravel(), reshape(), resize()

### Community 722 - "Community 722"
Cohesion: 0.33
Nodes (3): _missing_ctypes, Return the data pointer cast to a particular c-types object.         For example, Overrides the ctypes semi-magic method          Enables `c_func(some_array.ctype

### Community 724 - "Community 724"
Cohesion: 0.40
Nodes (6): _ischaracter(), ischaracter_or_characterarray(), ischaracterarray(), isexternal(), _isstring(), isstring_or_stringarray()

### Community 725 - "Community 725"
Cohesion: 0.33
Nodes (1): coddity

### Community 726 - "Community 726"
Cohesion: 0.33
Nodes (6): i0(), kaiser(), piecewise(), Modified Bessel function of the first kind, order 0.      Usually denoted :math:, Return the Kaiser window.      The Kaiser window is a taper formed by using a Be, Evaluate a piecewise-defined function.      Given a set of conditions and corres

### Community 727 - "Community 727"
Cohesion: 0.33
Nodes (6): median(), _quantile_unchecked(), Internal Function.     Call `func` with `a` as first argument swapping the axes, Compute the median along the specified axis.      Returns the median of the arra, Assumes that q is in [0, 1], and is an ndarray, _ureduce()

### Community 728 - "Community 728"
Cohesion: 0.33
Nodes (6): _copyto(), nanmax(), nanmin(), Replace values in `a` with NaN where `mask` is True.  This differs from     copy, Return minimum of an array or minimum along an axis, ignoring any NaNs.     When, Return the maximum of an array or maximum along an axis, ignoring any     NaNs.

### Community 729 - "Community 729"
Cohesion: 0.33
Nodes (6): _divide_by_count(), nanstd(), nanvar(), Compute the variance along the specified axis, while ignoring NaNs.      Returns, Compute the standard deviation along the specified axis, while     ignoring NaNs, Compute a/b ignoring invalid results. If `a` is an array the division     is don

### Community 730 - "Community 730"
Cohesion: 0.33
Nodes (6): nanmean(), _nanmedian(), _nanmedian_small(), sort + indexing median, faster for small medians along multiple     dimensions d, Compute the median along the specified axis, while ignoring NaNs.      Returns t, Compute the arithmetic mean along the specified axis, ignoring NaNs.      Return

### Community 731 - "Community 731"
Cohesion: 0.33
Nodes (6): nanpercentile(), nanquantile(), _nanquantile_unchecked(), Compute the qth percentile of the data along the specified axis,     while ignor, Compute the qth quantile of the data along the specified axis,     while ignorin, Assumes that q is in [0, 1], and is an ndarray

### Community 732 - "Community 732"
Cohesion: 0.33
Nodes (6): drop_fields(), Fills fields from output with fields from input,     with support for nested str, Return a new array with fields in `drop_names` dropped.      Nested fields are s, Returns a new numpy.recarray with fields in `drop_names` dropped., rec_drop_fields(), recursive_fill_fields()

### Community 733 - "Community 733"
Cohesion: 0.33
Nodes (6): get_datetime_to_unicode_transfer_function(), get_nbo_cast_datetime_transfer_function(), get_nbo_datetime_to_string_transfer_function(), get_nbo_string_to_datetime_transfer_function(), get_unicode_to_datetime_transfer_function(), _safe_print()

### Community 734 - "Community 734"
Cohesion: 0.33
Nodes (6): array_array(), array_asanyarray(), array_asarray(), array_ascontiguousarray(), array_asfortranarray(), _array_fromobject_generic()

### Community 735 - "Community 735"
Cohesion: 0.33
Nodes (6): array_scalar(), _finfo_get_realdtype(), PyArray_EquivTypenums(), PyArray_EquivTypes(), resolve_part_view_descr(), resolve_view_part_descr()

### Community 736 - "Community 736"
Cohesion: 0.47
Nodes (3): array_repr(), array_str(), npy_PyErr_SetStringChained()

### Community 737 - "Community 737"
Cohesion: 0.47
Nodes (4): npy_aquicksort(), npy_aquicksort_impl(), npy_quicksort(), npy_quicksort_impl()

### Community 738 - "Community 738"
Cohesion: 0.40
Nodes (2): bounded_uint(), bounded_uints()

### Community 741 - "Community 741"
Cohesion: 0.33
Nodes (6): assert_array_almost_equal_nulp(), assert_array_max_ulp(), nulp_diff(), Compare two arrays relatively to their spacing.      This is a relatively robust, Check that all items of arrays differ in at most N Units in the Last Place., For each item in x and y, return the number of representable floating     points

### Community 742 - "Community 742"
Cohesion: 0.33
Nodes (6): check_free_memory(), _get_mem_available(), _parse_size(), Check whether `free_bytes` amount of memory is currently free.     Returns: None, Convert memory size strings ('12 GB' etc.) to float, Return available memory in bytes, or None if unknown.

### Community 743 - "Community 743"
Cohesion: 0.33
Nodes (1): TestTimeScalars

### Community 744 - "Community 744"
Cohesion: 0.33
Nodes (1): TestByteBounds

### Community 745 - "Community 745"
Cohesion: 0.40
Nodes (2): TestAssumedShapeSumExample, TestF2cmapOption

### Community 746 - "Community 746"
Cohesion: 0.40
Nodes (5): check_operations(), Generate value+dtype pairs that generate floating point errors during     casts., There are many dedicated paths in NumPy which cast and should check for     floa, test_floatingpoint_errors_casting(), values_and_dtypes()

### Community 747 - "Community 747"
Cohesion: 0.33
Nodes (2): test_fit(), TestInterpolate

### Community 748 - "Community 748"
Cohesion: 0.33
Nodes (1): TestParamEval

### Community 749 - "Community 749"
Cohesion: 0.33
Nodes (1): TestParamParseNestedParens

### Community 750 - "Community 750"
Cohesion: 0.33
Nodes (2): Test deeply nested subtypes., TestMonsterType

### Community 751 - "Community 751"
Cohesion: 0.33
Nodes (1): TestMetadata

### Community 752 - "Community 752"
Cohesion: 0.60
Nodes (1): TestSingleEltArrayInput

### Community 753 - "Community 753"
Cohesion: 0.33
Nodes (1): TestRoll

### Community 754 - "Community 754"
Cohesion: 0.33
Nodes (2): Check correctness of `np.isdtype`. The test considers different argument     con, TestIsDType

### Community 755 - "Community 755"
Cohesion: 0.33
Nodes (3): Test that names correspond to where the type is under ``np.``, Test the dtype constructor maps names back to the type, TestScalarTypeNames

### Community 756 - "Community 756"
Cohesion: 0.33
Nodes (1): TestNumPyFunctions

### Community 757 - "Community 757"
Cohesion: 0.33
Nodes (1): TestVerifyMatchingSignatures

### Community 758 - "Community 758"
Cohesion: 0.60
Nodes (1): TestSingleEltArrayInput

### Community 759 - "Community 759"
Cohesion: 0.33
Nodes (1): TestJoinBy2

### Community 760 - "Community 760"
Cohesion: 0.53
Nodes (2): TestFReturnCharacter, TestReturnCharacter

### Community 761 - "Community 761"
Cohesion: 0.53
Nodes (2): TestFReturnComplex, TestReturnComplex

### Community 762 - "Community 762"
Cohesion: 0.53
Nodes (2): TestFReturnInteger, TestReturnInteger

### Community 763 - "Community 763"
Cohesion: 0.53
Nodes (2): TestFReturnLogical, TestReturnLogical

### Community 764 - "Community 764"
Cohesion: 0.33
Nodes (4): Check that SeedSequence generates data the same as the C++ reference.      https, Ensure that the implicit zero-padding does not cause problems., test_reference_data(), test_zero_padding()

### Community 765 - "Community 765"
Cohesion: 0.33
Nodes (1): TestExpandDims

### Community 766 - "Community 766"
Cohesion: 0.40
Nodes (3): SimpleSubClass, test_subclasses(), VerySimpleSubClass

### Community 767 - "Community 767"
Cohesion: 0.33
Nodes (1): TestGUFuncProcessCoreDims

### Community 768 - "Community 768"
Cohesion: 0.33
Nodes (3): assert_hypot_isinf(), assert_hypot_isnan(), TestHypotSpecialValues

### Community 769 - "Community 769"
Cohesion: 0.40
Nodes (3): interesting_binop_operands(), Helper to create "interesting" operands to cover common code paths:     * scalar, TestDivisionIntegerOverflowsAndDivideByZero

### Community 770 - "Community 770"
Cohesion: 0.33
Nodes (2): TestExpm1, TestLog1p

### Community 771 - "Community 771"
Cohesion: 0.33
Nodes (4): Check the creation of valued arrays (size 2, UCS4 values), Check the assignment of valued arrays (size 1009, UCS2 values), TestAssignValues_1009_UCS2, TestCreateValues_2_UCS4

### Community 772 - "Community 772"
Cohesion: 0.33
Nodes (3): Test assert_no_gc_cycles, Test that in cases where the garbage cannot be collected, we raise an         er, TestAssertNoGcCycles

### Community 773 - "Community 773"
Cohesion: 0.40
Nodes (4): nep_metadata(), parse_replaces_metadata(), Scan the directory of nep files and extract their metadata.  The metadata is pas, Handle :Replaces: as integer or list of integers

### Community 774 - "Community 774"
Cohesion: 0.33
Nodes (5): add_newdoc(), _parse_docstrings(), A module for creating docstrings for sphinx ``data`` domains., Append ``_docstrings_list`` with a docstring for `name`.      Parameters     ---, Convert all docstrings in ``_docstrings_list`` into a single     sphinx-legible

### Community 775 - "Community 775"
Cohesion: 0.60
Nodes (5): NPY_CPU_DISPATCH_CURFX(), simd_cosine_poly_f32(), simd_range_reduction_f32(), simd_sincos_f32(), simd_sine_poly_f32()

### Community 776 - "Community 776"
Cohesion: 0.60
Nodes (5): copy_positional_args_to_kwargs(), get_array_ufunc_overrides(), initialize_normal_kwds(), normalize_signature_keyword(), PyUFunc_CheckOverride()

### Community 777 - "Community 777"
Cohesion: 0.33
Nodes (6): new_array_op(), resolve_descriptors(), trivial_at_loop(), ufunc_at(), ufunc_at__fast_iter(), ufunc_at__slow_iter()

### Community 778 - "Community 778"
Cohesion: 0.33
Nodes (5): This is a module for defining private helpers which do not depend on the rest of, Private decorator for overriding __module__ on a function or class.      Example, Generate decorator for backward-compatible keyword renaming.      Apply the deco, _rename_parameter(), set_module()

### Community 781 - "Community 781"
Cohesion: 0.40
Nodes (1): StringComparisons

### Community 782 - "Community 782"
Cohesion: 0.60
Nodes (4): get_processor(), main(), process_and_write_file(), Process tempita templated file and write out the result.      The template file

### Community 783 - "Community 783"
Cohesion: 0.60
Nodes (4): import_tempita(), main(), process_tempita(), Process tempita templated file and write out the result.      The template file

### Community 786 - "Community 786"
Cohesion: 0.40
Nodes (5): array_str(), _array_str_implementation(), _guarded_repr_or_str(), Internal version of array_str() that allows overriding array2string., Return a string representation of the data in an array.      The data in the arr

### Community 787 - "Community 787"
Cohesion: 0.40
Nodes (5): format_float_positional(), format_float_scientific(), _none_or_positive_arg(), Format a floating-point scalar as a decimal string in scientific notation., Format a floating-point scalar as a decimal string in positional notation.

### Community 788 - "Community 788"
Cohesion: 0.50
Nodes (3): multiply(), Return (a * i), that is string multiple concatenation,     element-wise.      Va, Return (self * i), that is string multiple concatenation,         element-wise.

### Community 789 - "Community 789"
Cohesion: 0.40
Nodes (5): partition(), Partition each element in `a` around `sep`.      Calls :meth:`str.partition` ele, Partition (split) each element around the right-most separator.      Calls :meth, Partition each element in `self` around `sep`.          See Also         -------, rpartition()

### Community 790 - "Community 790"
Cohesion: 0.40
Nodes (5): all(), any(), Test whether any array element along a given axis evaluates to True.      Return, Test whether all array elements along a given axis evaluate to True.      Parame, _wrapreduction_any_all()

### Community 791 - "Community 791"
Cohesion: 0.40
Nodes (5): _cumulative_func(), cumulative_prod(), cumulative_sum(), Return the cumulative product of elements along a given axis.      This function, Return the cumulative sum of the elements along a given axis.      This function

### Community 792 - "Community 792"
Cohesion: 0.40
Nodes (2): Pytest configuration and fixtures for the Numpy test suite., SkipMatplotlibOutputChecker

### Community 793 - "Community 793"
Cohesion: 0.60
Nodes (4): main(), process_html(), process_tex(), Remove unnecessary section titles from the LaTeX file.

### Community 794 - "Community 794"
Cohesion: 0.50
Nodes (5): isintent_hide(), isintent_nothide(), isoptional(), isrequired(), l_or()

### Community 795 - "Community 795"
Cohesion: 0.40
Nodes (2): mod1, mod2

### Community 796 - "Community 796"
Cohesion: 0.40
Nodes (2): mod1, mod2

### Community 797 - "Community 797"
Cohesion: 0.60
Nodes (3): PyArray_calloc_aligned(), PyArray_malloc_aligned(), PyArray_realloc_aligned()

### Community 798 - "Community 798"
Cohesion: 0.40
Nodes (5): flatten_descr(), Flatten a structured data-type description.      Examples     --------     >>> i, Combine the dtype description of a series of arrays.      Parameters     -------, _zip_descr(), _zip_dtype()

### Community 799 - "Community 799"
Cohesion: 0.40
Nodes (2): mathops, useops

### Community 800 - "Community 800"
Cohesion: 0.70
Nodes (4): copycast_isaligned(), PyArray_AssignArray(), raw_array_assign_array(), raw_array_wheremasked_assign_array()

### Community 801 - "Community 801"
Cohesion: 0.60
Nodes (3): _get_wrap_prepare_args(), npy_apply_wrap(), npy_apply_wrap_simple()

### Community 802 - "Community 802"
Cohesion: 0.40
Nodes (5): array_innerproduct(), array_matrixproduct(), PyArray_InnerProduct(), PyArray_MatrixProduct(), PyArray_MatrixProduct2()

### Community 805 - "Community 805"
Cohesion: 0.50
Nodes (2): _PyArrayNeighborhoodIter_IncrCoord(), PyArrayNeighborhoodIter_Next()

### Community 806 - "Community 806"
Cohesion: 0.40
Nodes (3): IntSubClass, Tests for miscellaneous (non-magic) ``np.ndarray``/``np.generic`` methods.  More, SubClass

### Community 807 - "Community 807"
Cohesion: 0.60
Nodes (4): npyv_ifdiv_f32(), npyv_ifdiv_f64(), npyv_ifdivz_f32(), npyv_ifdivz_f64()

### Community 808 - "Community 808"
Cohesion: 0.40
Nodes (1): TestContextManager

### Community 809 - "Community 809"
Cohesion: 0.40
Nodes (1): TestConstants

### Community 810 - "Community 810"
Cohesion: 0.40
Nodes (2): TestCommonBlock, TestCommonWithUse

### Community 811 - "Community 811"
Cohesion: 0.40
Nodes (1): TestMarkinnerspaces

### Community 812 - "Community 812"
Cohesion: 0.40
Nodes (1): TestPublicPrivate

### Community 813 - "Community 813"
Cohesion: 0.70
Nodes (1): TestSetState

### Community 814 - "Community 814"
Cohesion: 0.70
Nodes (1): TestThread

### Community 815 - "Community 815"
Cohesion: 0.40
Nodes (1): TestConstants

### Community 816 - "Community 816"
Cohesion: 0.40
Nodes (1): TestVander

### Community 817 - "Community 817"
Cohesion: 0.70
Nodes (1): TestBoolArray

### Community 818 - "Community 818"
Cohesion: 0.60
Nodes (1): TestFloatExceptions

### Community 819 - "Community 819"
Cohesion: 0.40
Nodes (1): Check the numpy version is valid.  Note that a development version is marked by

### Community 820 - "Community 820"
Cohesion: 0.40
Nodes (1): TestVander

### Community 821 - "Community 821"
Cohesion: 0.50
Nodes (4): normalize_whitespace(), Remove leading and trailing whitespace, and convert internal     stretches of wh, Regression test for gh-10712., test_from_template()

### Community 822 - "Community 822"
Cohesion: 0.70
Nodes (1): TestThread

### Community 823 - "Community 823"
Cohesion: 0.70
Nodes (1): TestSingleEltArrayInput

### Community 824 - "Community 824"
Cohesion: 0.70
Nodes (1): TestThread

### Community 825 - "Community 825"
Cohesion: 0.40
Nodes (2): TestRenamedFunc, TestRenamedSubroutine

### Community 826 - "Community 826"
Cohesion: 0.40
Nodes (1): Test scripts  Test that we can run executable scripts that have been installed w

### Community 827 - "Community 827"
Cohesion: 0.40
Nodes (2): TestCallstatement, TestMultiline

### Community 828 - "Community 828"
Cohesion: 0.40
Nodes (3): To test all integer vector types at once, Test intrinsics:             npyv_reduce_max_##sfx             npyv_reduce_min_#, _SIMD_INT

### Community 829 - "Community 829"
Cohesion: 0.40
Nodes (1): TestSizeSumExample

### Community 830 - "Community 830"
Cohesion: 0.40
Nodes (1): TestUFuncInspectSignature

### Community 831 - "Community 831"
Cohesion: 0.40
Nodes (1): TestUfuncKwargs

### Community 832 - "Community 832"
Cohesion: 0.40
Nodes (1): TestAccuracy

### Community 833 - "Community 833"
Cohesion: 0.40
Nodes (1): TestAVXFloat32Transcendental

### Community 834 - "Community 834"
Cohesion: 0.40
Nodes (1): TestSign

### Community 835 - "Community 835"
Cohesion: 0.40
Nodes (1): TestBuildErrorMessage

### Community 836 - "Community 836"
Cohesion: 0.40
Nodes (1): TestWarns

### Community 837 - "Community 837"
Cohesion: 0.70
Nodes (4): field_type_grow_recursive(), field_types_create(), field_types_xclear(), get_from_ucs4_function()

### Community 838 - "Community 838"
Cohesion: 0.60
Nodes (3): error_if_matching_control_characters(), _load_from_filelike(), _readtext_from_stream()

### Community 839 - "Community 839"
Cohesion: 0.60
Nodes (4): check_built_version(), check_requirements_files(), main(), Checks related to the OpenBLAS version used in CI.  Options: 1. Check that the B

### Community 840 - "Community 840"
Cohesion: 0.40
Nodes (5): _get_dtype(), _get_fixed_signature(), py_resolve_dtypes(), py_resolve_dtypes_and_context(), py_resolve_dtypes_generic()

### Community 841 - "Community 841"
Cohesion: 0.50
Nodes (1): mod

### Community 842 - "Community 842"
Cohesion: 0.50
Nodes (1): # FIXME: there's no official way to provide extra information to the test log

### Community 843 - "Community 843"
Cohesion: 0.50
Nodes (1): utils

### Community 844 - "Community 844"
Cohesion: 0.83
Nodes (3): do_generate_api(), generate_api(), main()

### Community 845 - "Community 845"
Cohesion: 0.83
Nodes (3): do_generate_api(), generate_api(), main()

### Community 846 - "Community 846"
Cohesion: 0.83
Nodes (3): main(), normalize_doc(), write_code()

### Community 848 - "Community 848"
Cohesion: 0.83
Nodes (3): _is_basic_python_type(), PyArray_LookupSpecial(), PyArray_LookupSpecial_OnInstance()

### Community 849 - "Community 849"
Cohesion: 0.67
Nodes (2): npy_longdouble_from_PyLong(), _PyLong_Bytes()

### Community 851 - "Community 851"
Cohesion: 0.50
Nodes (3): EnsureGIL, NpyStringAcquireAllocator, SaveThreadState

### Community 852 - "Community 852"
Cohesion: 0.67
Nodes (2): PyUFunc_HasOverride(), PyUFuncOverride_GetNonDefaultArrayUfunc()

### Community 853 - "Community 853"
Cohesion: 0.50
Nodes (3): _array_method_doc(), This is only meant to add docs to objects defined in C-extension modules. The pu, Interenal helper function for adding docstrings to a common method of     `numpy

### Community 854 - "Community 854"
Cohesion: 0.50
Nodes (4): get_printoptions(), printoptions(), Return the current print options.      Returns     -------     print_opts : dict, Context manager for setting print options.      Set print options for the scope

### Community 855 - "Community 855"
Cohesion: 0.50
Nodes (3): Functions in the ``as*array`` family that promote array-likes into arrays.  `req, Return an ndarray of the provided type that satisfies requirements.      This fu, require()

### Community 856 - "Community 856"
Cohesion: 0.50
Nodes (4): matrix_transpose(), Interchange two axes of an array.      Parameters     ----------     a : array_l, Transposes a matrix (or a stack of matrices) ``x``.      This function is Array, swapaxes()

### Community 858 - "Community 858"
Cohesion: 0.50
Nodes (1): gh23879

### Community 859 - "Community 859"
Cohesion: 0.83
Nodes (3): hypergeometric_hrua(), hypergeometric_sample(), random_hypergeometric()

### Community 860 - "Community 860"
Cohesion: 0.67
Nodes (3): buildhooks(), findcommonblocks(), Build common block mechanism for f2py2e.  Copyright 1999 -- 2011 Pearu Peterson

### Community 861 - "Community 861"
Cohesion: 0.67
Nodes (3): buildhooks(), findf90modules(), Build F90 module support for f2py2e.  Copyright 1999 -- 2011 Pearu Peterson all

### Community 862 - "Community 862"
Cohesion: 0.67
Nodes (3): buildapi(), buildmodule(), Rules for building C/API module with f2py2e.  Here is a skeleton of a new wrappe

### Community 863 - "Community 863"
Cohesion: 0.67
Nodes (3): buildusevar(), buildusevars(), Build 'use others module data' mechanism for f2py2e.  Copyright 1999 -- 2011 Pea

### Community 864 - "Community 864"
Cohesion: 0.50
Nodes (4): dcabs1_(), dzasum_(), izamax_(), zaxpy_()

### Community 865 - "Community 865"
Cohesion: 0.50
Nodes (4): _arg_trim_zeros(), Return indices of the first and last non-zero element.      Parameters     -----, Remove values along a dimension which are zero along all other.      Parameters, _trim_zeros()

### Community 866 - "Community 866"
Cohesion: 0.50
Nodes (4): flip(), Rotate an array by 90 degrees in the plane specified by axes.      Rotation dire, Reverse the order of elements in an array along the given axis.      The shape o, rot90()

### Community 867 - "Community 867"
Cohesion: 0.50
Nodes (3): opt_func_info(), Introspection helper functions., Returns a dictionary containing the currently supported CPU dispatched     featu

### Community 868 - "Community 868"
Cohesion: 0.50
Nodes (2): Returns the type of the dtype of the input variable., Upgrade the mapper of a StringConverter by adding a new function and         its

### Community 869 - "Community 869"
Cohesion: 0.50
Nodes (4): assign_fields_by_name(), Assigns values from one structured array to another by field name.      Normally, Casts a structured array to a new dtype using assignment by field-name.      Thi, require_fields()

### Community 870 - "Community 870"
Cohesion: 0.50
Nodes (4): find_duplicates(), get_fieldstructure(), Find the duplicates in a structured array along a given key      Parameters, Returns a dictionary with fields indexing lists of their parent fields.      Thi

### Community 872 - "Community 872"
Cohesion: 0.83
Nodes (3): PyArray_AssignRawScalar(), raw_array_assign_scalar(), raw_array_wheremasked_assign_scalar()

### Community 873 - "Community 873"
Cohesion: 0.83
Nodes (3): PyArray_CommonDType(), PyArray_PromoteDTypeSequence(), reduce_dtypes_to_most_knowledgeable()

### Community 874 - "Community 874"
Cohesion: 0.50
Nodes (4): datetime_known_scalar_types(), python_builtins_are_known_scalar_types(), signed_integers_is_known_scalar_types(), string_known_scalar_types()

### Community 875 - "Community 875"
Cohesion: 0.83
Nodes (3): npy_fnv1a(), npy_fnv1a_32(), npy_fnv1a_64()

### Community 876 - "Community 876"
Cohesion: 0.50
Nodes (4): array_choose(), array_reshape(), array_resize(), NpyArg_ParseKeywords()

### Community 877 - "Community 877"
Cohesion: 0.50
Nodes (4): array_getfield(), array_setfield(), PyArray_GetField(), PyArray_SetField()

### Community 878 - "Community 878"
Cohesion: 0.50
Nodes (4): array_correlate2(), _pyarray_correlate(), PyArray_Correlate2(), _pyarray_revert()

### Community 879 - "Community 879"
Cohesion: 0.50
Nodes (4): array_einsum(), einsum_list_to_subscripts(), einsum_sub_op_from_lists(), einsum_sub_op_from_str()

### Community 880 - "Community 880"
Cohesion: 0.50
Nodes (4): initialize_global_state(), _multiarray_umath_exec(), set_flaginfo(), setup_scalartypes()

### Community 881 - "Community 881"
Cohesion: 0.50
Nodes (4): _is_user_defined_string_array(), _vec_string(), _vec_string_no_args(), _vec_string_with_args()

### Community 886 - "Community 886"
Cohesion: 0.50
Nodes (2): Index, SubClass

### Community 887 - "Community 887"
Cohesion: 0.50
Nodes (1): Simple expression that should pass with mypy.

### Community 888 - "Community 888"
Cohesion: 0.50
Nodes (4): assert_almost_equal(), assert_array_almost_equal(), Raises an AssertionError if two objects are not equal up to desired     precisio, Raises an AssertionError if two items are not equal up to desired     precision.

### Community 889 - "Community 889"
Cohesion: 0.50
Nodes (4): GetPerformanceAttributes(), memusage(), Return virtual memory size in bytes of the running python., Return memory usage of running python. [Not implemented]

### Community 890 - "Community 890"
Cohesion: 0.50
Nodes (4): jiffies(), measure(), Return elapsed time for executing code in the namespace of the caller.      The, Return number of jiffies elapsed.          Return number of jiffies (1/100ths of

### Community 891 - "Community 891"
Cohesion: 0.50
Nodes (2): F_GLOBALS, MOD_TYPES

### Community 892 - "Community 892"
Cohesion: 0.50
Nodes (2): dat, datonly

### Community 893 - "Community 893"
Cohesion: 0.50
Nodes (1): mtypes

### Community 896 - "Community 896"
Cohesion: 0.83
Nodes (3): splitmix64_next(), splitmix64_next32(), splitmix64_next64()

### Community 898 - "Community 898"
Cohesion: 0.50
Nodes (3): Test Array2 asString method, Test ArrayZ asString method, Test Array1 asString method

### Community 899 - "Community 899"
Cohesion: 0.50
Nodes (3): Test Array2 default constructor, Test Array1 default constructor, Test ArrayZ default constructor

### Community 900 - "Community 900"
Cohesion: 0.50
Nodes (3): Test Array2 nrows, ncols constructor, Test ArrayZ length constructor, Test Array1 length constructor

### Community 901 - "Community 901"
Cohesion: 0.50
Nodes (3): Test Array2 array constructor, Test ArrayZ array constructor, Test Array1 array constructor

### Community 902 - "Community 902"
Cohesion: 0.50
Nodes (3): Test Array2 copy constructor, Test ArrayZ copy constructor, Test Array1 copy constructor

### Community 903 - "Community 903"
Cohesion: 0.50
Nodes (3): Test Array2 __getitem__ method, negative index, Test ArrayZ __getitem__ method, negative index, Test Array1 __getitem__ method, negative index

### Community 904 - "Community 904"
Cohesion: 0.50
Nodes (3): Test Array2 __getitem__ method, out-of-range index, Test ArrayZ __getitem__ method, out-of-range index, Test Array1 __getitem__ method, out-of-range index

### Community 905 - "Community 905"
Cohesion: 0.50
Nodes (3): Test Array2 __len__ method, Test ArrayZ __len__ method, Test Array1 __len__ method

### Community 906 - "Community 906"
Cohesion: 0.50
Nodes (3): Test Array2 resize method, size, Test ArrayZ resize method, length, Test Array1 resize method, length

### Community 907 - "Community 907"
Cohesion: 0.50
Nodes (3): Test Array2 resize method, array, Test ArrayZ resize method, array, Test Array1 resize method, array

### Community 908 - "Community 908"
Cohesion: 0.50
Nodes (3): Test Array2 __setitem__ method, negative index, Test ArrayZ __setitem__ method, negative index, Test Array1 __setitem__ method, negative index

### Community 909 - "Community 909"
Cohesion: 0.50
Nodes (3): Test Array2 __setitem__ method, out-of-range index, Test ArrayZ __setitem__ method, out-of-range index, Test Array1 __setitem__ method, out-of-range index

### Community 910 - "Community 910"
Cohesion: 0.50
Nodes (3): Test Array1 __str__ method, Test Array2 __str__ method, Test ArrayZ __str__ method

### Community 911 - "Community 911"
Cohesion: 0.50
Nodes (3): Test Array1 view method, Test Array2 view method, Test ArrayZ view method

### Community 912 - "Community 912"
Cohesion: 0.50
Nodes (3): find_comma_decimal_point_locale(), Provide class for testing in French locale, See if platform has a decimal point as comma locale.      Find a locale that use

### Community 913 - "Community 913"
Cohesion: 0.50
Nodes (1): TestAbstractInterface

### Community 914 - "Community 914"
Cohesion: 0.50
Nodes (3): Test expected behaviors of ``asarray``., Confirm the intended behavior for *dtype* kwarg.          The result of ``asarra, TestAsArray

### Community 915 - "Community 915"
Cohesion: 0.50
Nodes (1): TestBadSequences

### Community 916 - "Community 916"
Cohesion: 0.50
Nodes (1): TestStringDiscovery

### Community 917 - "Community 917"
Cohesion: 0.50
Nodes (2): get_module(), Some codes to generate data and manage temporary buffers use when     sharing wi

### Community 918 - "Community 918"
Cohesion: 0.50
Nodes (2): These test cases exercise some behaviour changes, TestChanges

### Community 919 - "Community 919"
Cohesion: 0.50
Nodes (1): TestVander

### Community 920 - "Community 920"
Cohesion: 0.50
Nodes (2): This test suite tests various expressions that are used as dimension     specifi, TestDimSpec

### Community 921 - "Community 921"
Cohesion: 0.50
Nodes (1): TestInplace

### Community 922 - "Community 922"
Cohesion: 0.50
Nodes (2): Test if all ``.pyi`` files are properly installed., TestIsFile

### Community 923 - "Community 923"
Cohesion: 0.50
Nodes (1): TestDerivative

### Community 924 - "Community 924"
Cohesion: 0.50
Nodes (1): TestIntegral

### Community 925 - "Community 925"
Cohesion: 0.50
Nodes (1): TestNorm_NonSystematic

### Community 926 - "Community 926"
Cohesion: 0.50
Nodes (4): mixed_types_structured(), Function providing heterogeneous input data with a structured dtype, along     w, test_structured_dtype_and_skiprows_no_empty_lines(), test_unpack_structured()

### Community 927 - "Community 927"
Cohesion: 0.50
Nodes (1): TestMixed

### Community 929 - "Community 929"
Cohesion: 0.50
Nodes (4): iter_multi_index(), test_iter_best_order_multi_index_1d(), test_iter_best_order_multi_index_2d(), test_iter_best_order_multi_index_3d()

### Community 930 - "Community 930"
Cohesion: 0.50
Nodes (1): TestMultipleFields

### Community 931 - "Community 931"
Cohesion: 0.50
Nodes (1): TestCompanion

### Community 932 - "Community 932"
Cohesion: 0.50
Nodes (2): See https://github.com/numpy/numpy/pull/10676., TestQuotedCharacter

### Community 933 - "Community 933"
Cohesion: 0.50
Nodes (4): assert_shapes_correct(), test_same_input_shapes(), test_two_compatible_by_ones_input_shapes(), test_two_compatible_by_prepending_ones_input_shapes()

### Community 934 - "Community 934"
Cohesion: 0.50
Nodes (1): TestStringLikeCasts

### Community 935 - "Community 935"
Cohesion: 0.50
Nodes (1): TestOverride

### Community 936 - "Community 936"
Cohesion: 0.50
Nodes (2): Tests for PyUFunc_ReplaceLoopBySignature C API., TestReplaceLoopBySignature

### Community 937 - "Community 937"
Cohesion: 0.50
Nodes (1): TestConstants

### Community 938 - "Community 938"
Cohesion: 0.67
Nodes (1): TestLDExp

### Community 939 - "Community 939"
Cohesion: 0.50
Nodes (1): TestLog2

### Community 940 - "Community 940"
Cohesion: 0.50
Nodes (1): TestOut

### Community 941 - "Community 941"
Cohesion: 0.83
Nodes (3): get_authors(), get_pull_requests(), main()

### Community 942 - "Community 942"
Cohesion: 0.67
Nodes (3): get_files(), main(), Check if all the test and .pyi files are installed after building.  Examples::

### Community 943 - "Community 943"
Cohesion: 0.50
Nodes (3): Standalone script for writing release doc::      python tools/write_release <ver, Copy the <version>-notes.rst file to the OUTPUT_DIR and use     pandoc to transl, write_release()

### Community 944 - "Community 944"
Cohesion: 0.50
Nodes (3): # NOTE: Nested literals get flattened and de-duplicated at runtime, which isn't, # TODO: add `_StringCodes` once it has a scalar type, # NOTE: `StringDType' has no scalar type, and therefore has no name that can

### Community 945 - "Community 945"
Cohesion: 0.83
Nodes (3): count_axes(), PyArray_CopyInitialReduceValues(), PyUFunc_ReduceWrapper()

### Community 948 - "Community 948"
Cohesion: 0.50
Nodes (1): A set of methods retained from np.compat module that are still used across codeb

### Community 949 - "Community 949"
Cohesion: 0.67
Nodes (1): test

### Community 952 - "Community 952"
Cohesion: 0.67
Nodes (2): parse_distributions_h(), Parse distributions.h located in inc_dir for CFFI, filling in the ffi.cdef

### Community 954 - "Community 954"
Cohesion: 1.00
Nodes (2): accumulate(), main()

### Community 956 - "Community 956"
Cohesion: 0.67
Nodes (1): mod

### Community 958 - "Community 958"
Cohesion: 0.67
Nodes (1): Docstrings for generated ufuncs  The syntax is designed to look like the functio

### Community 959 - "Community 959"
Cohesion: 0.67
Nodes (1): mod

### Community 960 - "Community 960"
Cohesion: 0.67
Nodes (2): data, typedefmod

### Community 964 - "Community 964"
Cohesion: 0.67
Nodes (1): Returns true for each element if all cased characters in the         string are

### Community 965 - "Community 965"
Cohesion: 0.67
Nodes (3): Remove axes of length one from `a`.      Parameters     ----------     a : array, squeeze(), _wrapit()

### Community 966 - "Community 966"
Cohesion: 0.67
Nodes (1): Create the numpy._core.umath namespace for backward compatibility. In v1.16 the

### Community 968 - "Community 968"
Cohesion: 0.67
Nodes (1): test_bug

### Community 969 - "Community 969"
Cohesion: 0.67
Nodes (1): utils

### Community 970 - "Community 970"
Cohesion: 0.67
Nodes (1): util

### Community 971 - "Community 971"
Cohesion: 0.67
Nodes (1): foo

### Community 972 - "Community 972"
Cohesion: 0.67
Nodes (1): foo

### Community 973 - "Community 973"
Cohesion: 0.67
Nodes (1): foo

### Community 974 - "Community 974"
Cohesion: 0.67
Nodes (2): ISO_C_BINDING maps for f2py2e. Only required declarations/macros/functions will, # TODO: See gh-25229

### Community 975 - "Community 975"
Cohesion: 0.67
Nodes (1): data

### Community 978 - "Community 978"
Cohesion: 0.67
Nodes (3): caxpy_(), icamax_(), scabs1_()

### Community 979 - "Community 979"
Cohesion: 0.67
Nodes (1): foo_fixed

### Community 980 - "Community 980"
Cohesion: 0.67
Nodes (1): foo_free

### Community 981 - "Community 981"
Cohesion: 0.67
Nodes (1): alloc_char_mod

### Community 982 - "Community 982"
Cohesion: 0.67
Nodes (1): mod

### Community 983 - "Community 983"
Cohesion: 1.00
Nodes (3): array_reduce_ex(), array_reduce_ex_picklebuffer(), array_reduce_ex_regular()

### Community 984 - "Community 984"
Cohesion: 0.67
Nodes (3): array_may_share_memory(), array_shares_memory(), array_shares_memory_impl()

### Community 986 - "Community 986"
Cohesion: 0.67
Nodes (1): r""" Building the required library in this example requires a source distributio

### Community 989 - "Community 989"
Cohesion: 0.67
Nodes (1): A

### Community 990 - "Community 990"
Cohesion: 0.67
Nodes (2): Tests for :mod:`numpy._core.numeric`.  Does not include tests which fall under `, SubClass

### Community 992 - "Community 992"
Cohesion: 0.67
Nodes (1): adder

### Community 993 - "Community 993"
Cohesion: 0.67
Nodes (1): char_test

### Community 994 - "Community 994"
Cohesion: 0.67
Nodes (1): Test floor function with wrong type

### Community 995 - "Community 995"
Cohesion: 0.67
Nodes (1): Test floor function with wrong type

### Community 996 - "Community 996"
Cohesion: 0.67
Nodes (1): TestBlockDocString

### Community 998 - "Community 998"
Cohesion: 0.67
Nodes (1): TestIntegral

### Community 999 - "Community 999"
Cohesion: 0.67
Nodes (2): Testing the utilities of the CPU dispatcher, test_dispatcher()

### Community 1000 - "Community 1000"
Cohesion: 0.67
Nodes (2): address ReDOS vulnerability:         https://github.com/numpy/numpy/issues/23338, TestNameArgsPatternBacktracking

### Community 1001 - "Community 1001"
Cohesion: 0.67
Nodes (1): TestCrackFortran

### Community 1002 - "Community 1002"
Cohesion: 0.67
Nodes (1): TestExternal

### Community 1003 - "Community 1003"
Cohesion: 0.67
Nodes (1): TestModuleProcedure

### Community 1004 - "Community 1004"
Cohesion: 0.67
Nodes (2): Tests for structural pattern matching support (PEP 634)., TestPatternMatching

### Community 1005 - "Community 1005"
Cohesion: 0.67
Nodes (1): TestPower

### Community 1006 - "Community 1006"
Cohesion: 0.67
Nodes (1): TestFlatiterIndexing0dBoolIndex

### Community 1007 - "Community 1007"
Cohesion: 0.67
Nodes (1): TestFlatiterIndexingFloatIndex

### Community 1008 - "Community 1008"
Cohesion: 0.67
Nodes (1): TestRoundDeprecation

### Community 1009 - "Community 1009"
Cohesion: 0.67
Nodes (1): TestWarningUtilityDeprecations

### Community 1010 - "Community 1010"
Cohesion: 0.67
Nodes (1): TestF2Cmap

### Community 1011 - "Community 1011"
Cohesion: 0.67
Nodes (3): f2cmap_f90(), hello_world_f90(), Generates a single f90 file for testing

### Community 1012 - "Community 1012"
Cohesion: 0.67
Nodes (1): Straightforward testing with a mixture of linspace data (for         consistency

### Community 1013 - "Community 1013"
Cohesion: 0.67
Nodes (1): TestSctypeDict

### Community 1014 - "Community 1014"
Cohesion: 0.67
Nodes (1): TestIntegral

### Community 1016 - "Community 1016"
Cohesion: 0.67
Nodes (2): Compile and run pyinstaller-smoke.py using PyInstaller., test_pyinstaller()

### Community 1017 - "Community 1017"
Cohesion: 0.67
Nodes (1): TestUnicodeOnlyMethodsRaiseWithBytes

### Community 1018 - "Community 1018"
Cohesion: 0.67
Nodes (1): TestAddDocstring

### Community 1019 - "Community 1019"
Cohesion: 0.67
Nodes (1): TestAttributes

### Community 1020 - "Community 1020"
Cohesion: 0.67
Nodes (1): TestCbrt

### Community 1021 - "Community 1021"
Cohesion: 0.67
Nodes (1): TestFPClass

### Community 1022 - "Community 1022"
Cohesion: 0.67
Nodes (1): TestHypotErrorMessages

### Community 1023 - "Community 1023"
Cohesion: 0.67
Nodes (1): TestPositive

### Community 1024 - "Community 1024"
Cohesion: 0.67
Nodes (1): TestUserCode

### Community 1025 - "Community 1025"
Cohesion: 0.67
Nodes (1): TestValueAttr

### Community 1026 - "Community 1026"
Cohesion: 1.00
Nodes (2): create_conv_funcs(), read_rows()

### Community 1028 - "Community 1028"
Cohesion: 0.67
Nodes (2): get_submodule_paths(), Get paths to submodules so that we can exclude them from things like     check_t

### Community 1030 - "Community 1030"
Cohesion: 0.67
Nodes (1): fortfuncs

### Community 1032 - "Community 1032"
Cohesion: 1.00
Nodes (1): precision

### Community 1036 - "Community 1036"
Cohesion: 1.00
Nodes (1): This file is used by asv_compare.conf.json.tpl.

### Community 1042 - "Community 1042"
Cohesion: 1.00
Nodes (1): Use cffi to access any of the underlying C functions from distributions.h

### Community 1110 - "Community 1110"
Cohesion: 1.00
Nodes (1): FloatStatus

### Community 1111 - "Community 1111"
Cohesion: 1.00
Nodes (1): Half

### Community 1116 - "Community 1116"
Cohesion: 1.00
Nodes (1): Returns true for each element if all characters in the string are         digits

### Community 1117 - "Community 1117"
Cohesion: 1.00
Nodes (1): For each element in `self`, return True if there are only         numeric charac

### Community 1118 - "Community 1118"
Cohesion: 1.00
Nodes (1): Returns true for each element if there are only whitespace         characters in

### Community 1119 - "Community 1119"
Cohesion: 1.00
Nodes (1): Returns true for each element if the element is a titlecased         string and

### Community 1120 - "Community 1120"
Cohesion: 1.00
Nodes (1): Return a string which is the concatenation of the strings in the         sequenc

### Community 1121 - "Community 1121"
Cohesion: 1.00
Nodes (1): For each element in `self`, return a copy with the leading characters         re

### Community 1122 - "Community 1122"
Cohesion: 1.00
Nodes (1): Return (other + self), that is string concatenation,         element-wise for a

### Community 1123 - "Community 1123"
Cohesion: 1.00
Nodes (1): For each element in `self`, return a copy of the string with all         occurre

### Community 1124 - "Community 1124"
Cohesion: 1.00
Nodes (1): For each element in `self`, return the highest index in the string         where

### Community 1125 - "Community 1125"
Cohesion: 1.00
Nodes (1): Like `rfind`, but raises :exc:`ValueError` when the substring `sub` is         n

### Community 1126 - "Community 1126"
Cohesion: 1.00
Nodes (1): For each element in `self`, return a list of the lines in the         element, b

### Community 1127 - "Community 1127"
Cohesion: 1.00
Nodes (1): For each element in `self`, return a copy with the leading and         trailing

### Community 1128 - "Community 1128"
Cohesion: 1.00
Nodes (2): diagonal(), Return specified diagonals.      If `a` is 2-D, returns the diagonal of `a` with

### Community 1129 - "Community 1129"
Cohesion: 1.00
Nodes (2): mean(), Compute the arithmetic mean along the specified axis.      Returns the average o

### Community 1130 - "Community 1130"
Cohesion: 1.00
Nodes (2): ndim(), Return the number of dimensions of an array.      Parameters     ----------

### Community 1131 - "Community 1131"
Cohesion: 1.00
Nodes (2): partition(), Return a partitioned copy of an array.      Creates a copy of the array and part

### Community 1132 - "Community 1132"
Cohesion: 1.00
Nodes (2): ptp(), Range of values (maximum - minimum) along an axis.      The name of the function

### Community 1133 - "Community 1133"
Cohesion: 1.00
Nodes (2): put(), Replaces specified elements of an array with given values.      The indexing wor

### Community 1134 - "Community 1134"
Cohesion: 1.00
Nodes (2): Return a sorted copy of an array.      Parameters     ----------     a : array_l, sort()

### Community 1135 - "Community 1135"
Cohesion: 1.00
Nodes (2): Return the sum along diagonals of the array.      If `a` is 2-D, the sum along i, trace()

### Community 1136 - "Community 1136"
Cohesion: 1.00
Nodes (2): r"""     Compute the standard deviation along the specified axis.      Returns t, std()

### Community 1137 - "Community 1137"
Cohesion: 1.00
Nodes (2): r"""     Compute the variance along the specified axis.      Returns the varianc, var()

### Community 1138 - "Community 1138"
Cohesion: 1.00
Nodes (2): busday_count(), busday_count(         begindates,         enddates,         weekmask='1111100',

### Community 1139 - "Community 1139"
Cohesion: 1.00
Nodes (2): busday_offset(), busday_offset(         dates,         offsets,         roll='raise',         wee

### Community 1140 - "Community 1140"
Cohesion: 1.00
Nodes (2): can_cast(), can_cast(from_, to, casting='safe')      Returns True if cast between data types

### Community 1141 - "Community 1141"
Cohesion: 1.00
Nodes (2): concatenate(), concatenate(         arrays,         /,         axis=0,         out=None,

### Community 1142 - "Community 1142"
Cohesion: 1.00
Nodes (2): copyto(), copyto(dst, src, casting='same_kind', where=True)      Copies values from one ar

### Community 1143 - "Community 1143"
Cohesion: 1.00
Nodes (2): datetime_as_string(), datetime_as_string(arr, unit=None, timezone='naive', casting='same_kind')      C

### Community 1144 - "Community 1144"
Cohesion: 1.00
Nodes (2): dot(), dot(a, b, out=None)      Dot product of two arrays. Specifically,      - If both

### Community 1145 - "Community 1145"
Cohesion: 1.00
Nodes (2): empty_like(), empty_like(         prototype,         /,         dtype=None,         order='K',

### Community 1146 - "Community 1146"
Cohesion: 1.00
Nodes (2): inner(), inner(a, b, /)      Inner product of two arrays.      Ordinary inner product of

### Community 1147 - "Community 1147"
Cohesion: 1.00
Nodes (2): is_busday(), is_busday(         dates,         weekmask='1111100',         holidays=None,

### Community 1148 - "Community 1148"
Cohesion: 1.00
Nodes (2): lexsort(), lexsort(keys, axis=-1)      Perform an indirect stable sort using a sequence of

### Community 1149 - "Community 1149"
Cohesion: 1.00
Nodes (2): may_share_memory(), may_share_memory(a, b, /, max_work=0)      Determine if two arrays might share m

### Community 1150 - "Community 1150"
Cohesion: 1.00
Nodes (2): min_scalar_type(), min_scalar_type(a, /)      For scalar ``a``, returns the data type with the smal

### Community 1151 - "Community 1151"
Cohesion: 1.00
Nodes (2): packbits(), packbits(a, /, axis=None, bitorder='big')      Packs the elements of a binary-va

### Community 1152 - "Community 1152"
Cohesion: 1.00
Nodes (2): putmask(), putmask(a, /, mask, values)      Changes elements of an array based on condition

### Community 1153 - "Community 1153"
Cohesion: 1.00
Nodes (2): unravel_index(indices, shape, order='C')      Converts a flat index or array of, unravel_index()

### Community 1154 - "Community 1154"
Cohesion: 1.00
Nodes (2): unpackbits(a, /, axis=None, count=None, bitorder='big')      Unpacks elements of, unpackbits()

### Community 1155 - "Community 1155"
Cohesion: 1.00
Nodes (2): shares_memory(a, b, /, max_work=-1)      Determine if two arrays share memory., shares_memory()

### Community 1156 - "Community 1156"
Cohesion: 1.00
Nodes (2): where(condition, [x, y], /)      Return elements chosen from `x` or `y` dependin, where()

### Community 1157 - "Community 1157"
Cohesion: 1.00
Nodes (2): result_type(*arrays_and_dtypes)      Returns the type that results from applying, result_type()

### Community 1158 - "Community 1158"
Cohesion: 1.00
Nodes (2): r"""     vdot(a, b, /)      Return the dot product of two vectors.      The `vdo, vdot()

### Community 1160 - "Community 1160"
Cohesion: 1.00
Nodes (1): Stores and defines the low-level format_options context variable.  This is defin

### Community 1161 - "Community 1161"
Cohesion: 1.00
Nodes (2): capitalize(), Return a copy of ``a`` with only the first character of each element     capital

### Community 1162 - "Community 1162"
Cohesion: 1.00
Nodes (2): center(), Return a copy of `a` with its elements centered in a string of     length `width

### Community 1163 - "Community 1163"
Cohesion: 1.00
Nodes (2): count(), Returns an array with the number of non-overlapping occurrences of     substring

### Community 1164 - "Community 1164"
Cohesion: 1.00
Nodes (2): endswith(), Returns a boolean array which is `True` where the string element     in ``a`` en

### Community 1165 - "Community 1165"
Cohesion: 1.00
Nodes (2): expandtabs(), Return a copy of each string element where all tab characters are     replaced b

### Community 1166 - "Community 1166"
Cohesion: 1.00
Nodes (2): find(), For each element, return the lowest index in the string where     substring ``su

### Community 1167 - "Community 1167"
Cohesion: 1.00
Nodes (2): index(), Like `find`, but raises :exc:`ValueError` when the substring is not found.

### Community 1168 - "Community 1168"
Cohesion: 1.00
Nodes (2): ljust(), Return an array with the elements of `a` left-justified in a     string of lengt

### Community 1169 - "Community 1169"
Cohesion: 1.00
Nodes (2): lower(), Return an array with the elements converted to lowercase.      Call :meth:`str.l

### Community 1170 - "Community 1170"
Cohesion: 1.00
Nodes (2): lstrip(), For each element in `a`, return a copy with the leading characters     removed.

### Community 1171 - "Community 1171"
Cohesion: 1.00
Nodes (2): multiply(), Return (a * i), that is string multiple concatenation,     element-wise.      Va

### Community 1172 - "Community 1172"
Cohesion: 1.00
Nodes (2): partition(), Partition each element in ``a`` around ``sep``.      For each element in ``a``,

### Community 1173 - "Community 1173"
Cohesion: 1.00
Nodes (2): For each element in `a`, return a copy with the leading and     trailing charact, strip()

### Community 1174 - "Community 1174"
Cohesion: 1.00
Nodes (2): Return an array with the elements converted to uppercase.      Calls :meth:`str., upper()

### Community 1175 - "Community 1175"
Cohesion: 1.00
Nodes (2): Return element-wise a copy of the string with     uppercase characters converted, swapcase()

### Community 1176 - "Community 1176"
Cohesion: 1.00
Nodes (2): Return element-wise title cased version of string or unicode.      Title case wo, title()

### Community 1177 - "Community 1177"
Cohesion: 1.00
Nodes (2): For each element in ``a``, return a copy of the string with     occurrences of s, replace()

### Community 1178 - "Community 1178"
Cohesion: 1.00
Nodes (2): Partition (split) each element around the right-most separator.      For each el, rpartition()

### Community 1179 - "Community 1179"
Cohesion: 1.00
Nodes (2): Slice the strings in `a` by slices specified by `start`, `stop`, `step`.     Lik, slice()

### Community 1180 - "Community 1180"
Cohesion: 1.00
Nodes (2): For each element, return the highest index in the string where     substring ``s, rfind()

### Community 1181 - "Community 1181"
Cohesion: 1.00
Nodes (2): Like `rfind`, but raises :exc:`ValueError` when the substring `sub` is     not f, rindex()

### Community 1182 - "Community 1182"
Cohesion: 1.00
Nodes (2): Returns a boolean array which is `True` where the string element     in ``a`` st, startswith()

### Community 1183 - "Community 1183"
Cohesion: 1.00
Nodes (2): Return an array with the elements of `a` right-justified in a     string of leng, rjust()

### Community 1184 - "Community 1184"
Cohesion: 1.00
Nodes (2): Return the numeric string left-filled with zeros. A leading     sign prefix (``+, zfill()

### Community 1185 - "Community 1185"
Cohesion: 1.00
Nodes (2): For each element in `a`, return a copy with the trailing characters     removed., rstrip()

### Community 1186 - "Community 1186"
Cohesion: 1.00
Nodes (1): Due to compatibility, numpy has a very large number of different naming conventi

### Community 1188 - "Community 1188"
Cohesion: 1.00
Nodes (1): foo

### Community 1191 - "Community 1191"
Cohesion: 1.00
Nodes (1): cmplxdat

### Community 1192 - "Community 1192"
Cohesion: 1.00
Nodes (1): foo

### Community 1200 - "Community 1200"
Cohesion: 1.00
Nodes (1): =================== Universal Functions ===================  Ufuncs are, general

### Community 1201 - "Community 1201"
Cohesion: 1.00
Nodes (1): DoxyLimbo

### Community 1204 - "Community 1204"
Cohesion: 1.00
Nodes (1): ISO_FORTRAN_ENV maps for f2py2e

### Community 1207 - "Community 1207"
Cohesion: 1.00
Nodes (2): blackman(), Return the Blackman window.      The Blackman window is a taper formed by using

### Community 1208 - "Community 1208"
Cohesion: 1.00
Nodes (2): _compute_virtual_index(), Compute the floating point indexes of an array for the linear     interpolation

### Community 1209 - "Community 1209"
Cohesion: 1.00
Nodes (2): digitize(), Return the indices of the bins to which each value in input array belongs.

### Community 1210 - "Community 1210"
Cohesion: 1.00
Nodes (2): extract(), Return the elements of an array that satisfy some condition.      This is equiva

### Community 1211 - "Community 1211"
Cohesion: 1.00
Nodes (2): hamming(), Return the Hamming window.      The Hamming window is a taper formed by using a

### Community 1212 - "Community 1212"
Cohesion: 1.00
Nodes (2): hanning(), Return the Hanning window.      The Hanning window is a taper formed by using a

### Community 1213 - "Community 1213"
Cohesion: 1.00
Nodes (2): insert(), Insert values along the given axis before the given indices.      Parameters

### Community 1214 - "Community 1214"
Cohesion: 1.00
Nodes (2): interp(), One-dimensional linear interpolation for monotonically increasing sample points.

### Community 1215 - "Community 1215"
Cohesion: 1.00
Nodes (2): place(), Change elements of an array based on conditional and input values.      Similar

### Community 1216 - "Community 1216"
Cohesion: 1.00
Nodes (2): Sort a complex array using the real part first, then the imaginary part.      Pa, _sort_complex()

### Community 1217 - "Community 1217"
Cohesion: 1.00
Nodes (2): r"""     Return the normalized sinc function.      The sinc function is equal to, sinc()

### Community 1218 - "Community 1218"
Cohesion: 1.00
Nodes (2): _izip_fields_flat(), Returns an iterator of concatenated fields from a sequence of arrays,     collap

### Community 1219 - "Community 1219"
Cohesion: 1.00
Nodes (2): _izip_fields(), Returns an iterator of concatenated fields from a sequence of arrays.

### Community 1220 - "Community 1220"
Cohesion: 1.00
Nodes (2): Rename the fields from a flexible-datatype ndarray or recarray.      Nested fiel, rename_fields()

### Community 1221 - "Community 1221"
Cohesion: 1.00
Nodes (2): Re-pack the fields of a structured array or dtype in memory.      The memory lay, repack_fields()

### Community 1222 - "Community 1222"
Cohesion: 1.00
Nodes (1): Build an example package using the limited Python C API.

### Community 1226 - "Community 1226"
Cohesion: 1.00
Nodes (2): _n_to_n_data_clone(), _n_to_n_data_free()

### Community 1227 - "Community 1227"
Cohesion: 1.00
Nodes (2): NPY_cast_info_init(), NPY_context_init()

### Community 1228 - "Community 1228"
Cohesion: 1.00
Nodes (2): _one_to_n_data_clone(), _one_to_n_data_free()

### Community 1229 - "Community 1229"
Cohesion: 1.00
Nodes (2): _subarray_broadcast_data_clone(), _subarray_broadcast_data_free()

### Community 1230 - "Community 1230"
Cohesion: 1.00
Nodes (2): datetime_common_dtype(), default_builtin_common_dtype()

### Community 1231 - "Community 1231"
Cohesion: 1.00
Nodes (2): PyArray_GETITEM(), PyDataType_GetArrFuncs()

### Community 1232 - "Community 1232"
Cohesion: 1.00
Nodes (2): any_array_ufunc_overrides(), array_ufunc()

### Community 1233 - "Community 1233"
Cohesion: 1.00
Nodes (2): array_byteswap(), PyArray_Byteswap()

### Community 1234 - "Community 1234"
Cohesion: 1.00
Nodes (2): array_deepcopy(), _deepcopy_call()

### Community 1235 - "Community 1235"
Cohesion: 1.00
Nodes (2): array_reduce(), _getlist_pkl()

### Community 1236 - "Community 1236"
Cohesion: 1.00
Nodes (2): array_setstate(), _setlist_pkl()

### Community 1237 - "Community 1237"
Cohesion: 1.00
Nodes (2): array_tofile(), PyArray_ToFileObject()

### Community 1238 - "Community 1238"
Cohesion: 1.00
Nodes (2): array__get_ndarray_c_version(), PyArray_GetNDArrayCVersion()

### Community 1239 - "Community 1239"
Cohesion: 1.00
Nodes (2): array_where(), PyArray_Where()

### Community 1240 - "Community 1240"
Cohesion: 1.00
Nodes (2): PyArray_ScalarKind(), _signbit_set()

### Community 1246 - "Community 1246"
Cohesion: 1.00
Nodes (1): Distributor init file  Distributors: you can add custom code here to support par

### Community 1248 - "Community 1248"
Cohesion: 1.00
Nodes (1): Dict of expired attributes that are discontinued since 2.0 release. Each item is

### Community 1251 - "Community 1251"
Cohesion: 1.00
Nodes (1): Test

### Community 1252 - "Community 1252"
Cohesion: 1.00
Nodes (1): Tests for :mod:`numpy._core.fromnumeric`.

### Community 1253 - "Community 1253"
Cohesion: 1.00
Nodes (1): Based on the `if __name__ == "__main__"` test code in `lib/_user_array_impl.py`.

### Community 1255 - "Community 1255"
Cohesion: 1.00
Nodes (1): # NOTE: __call__ is needed due to python/mypy#17620

### Community 1256 - "Community 1256"
Cohesion: 1.00
Nodes (1): # NOTE: `np.generic` subclasses are not guaranteed to support addition;

### Community 1261 - "Community 1261"
Cohesion: 1.00
Nodes (2): KnownFailureException, Raise this exception to mark a test as a known failing test.

### Community 1262 - "Community 1262"
Cohesion: 1.00
Nodes (2): _no_tracing(), Decorator to temporarily turn off tracing for the duration of a test.     Needed

### Community 1263 - "Community 1263"
Cohesion: 1.00
Nodes (2): print_assert_equal(), Test if two objects are equal, and print an error message if test fails.      Th

### Community 1264 - "Community 1264"
Cohesion: 1.00
Nodes (2): Run doctests found in the given file.      By default `rundocs` raises an Assert, rundocs()

### Community 1265 - "Community 1265"
Cohesion: 1.00
Nodes (2): Context manager to provide a temporary test folder.      All arguments are passe, tempdir()

### Community 1266 - "Community 1266"
Cohesion: 1.00
Nodes (2): Context manager for temporary files.      Context manager that returns the path, temppath()

### Community 1267 - "Community 1267"
Cohesion: 1.00
Nodes (2): Decorator to skip a test if not enough memory is available, requires_memory()

### Community 1268 - "Community 1268"
Cohesion: 1.00
Nodes (2): Runs a function many times in parallel, run_threaded()

### Community 1269 - "Community 1269"
Cohesion: 1.00
Nodes (2): Decorator to skip test if deep recursion is not supported., requires_deep_recursion()

### Community 1270 - "Community 1270"
Cohesion: 1.00
Nodes (2): Run ``cmd`` in a subprocess, failing the test with its captured output     if it, run_subprocess()

### Community 1271 - "Community 1271"
Cohesion: 1.00
Nodes (1): This hook should collect all binary files and any hidden modules that numpy need

### Community 1287 - "Community 1287"
Cohesion: 1.00
Nodes (1): string_test

### Community 1289 - "Community 1289"
Cohesion: 1.00
Nodes (1): Test det function with non-container

### Community 1290 - "Community 1290"
Cohesion: 1.00
Nodes (1): Test det function with wrong dimensions

### Community 1291 - "Community 1291"
Cohesion: 1.00
Nodes (1): Test det function with wrong size

### Community 1292 - "Community 1292"
Cohesion: 1.00
Nodes (1): Test floor function with non-array

### Community 1293 - "Community 1293"
Cohesion: 1.00
Nodes (1): Test floor function with wrong dimensions

### Community 1294 - "Community 1294"
Cohesion: 1.00
Nodes (1): Test floor function with wrong type

### Community 1295 - "Community 1295"
Cohesion: 1.00
Nodes (1): Test luSplit function

### Community 1296 - "Community 1296"
Cohesion: 1.00
Nodes (1): Test max function with bad list

### Community 1297 - "Community 1297"
Cohesion: 1.00
Nodes (1): Test max function with non-container

### Community 1298 - "Community 1298"
Cohesion: 1.00
Nodes (1): Test max function with wrong dimensions

### Community 1299 - "Community 1299"
Cohesion: 1.00
Nodes (1): Test min function with bad list

### Community 1300 - "Community 1300"
Cohesion: 1.00
Nodes (1): Test min function with non-container

### Community 1301 - "Community 1301"
Cohesion: 1.00
Nodes (1): Test min function with wrong dimensions

### Community 1302 - "Community 1302"
Cohesion: 1.00
Nodes (1): Test scale function with non-array

### Community 1303 - "Community 1303"
Cohesion: 1.00
Nodes (1): Test scale function with wrong dimensions

### Community 1304 - "Community 1304"
Cohesion: 1.00
Nodes (1): Test scale function with wrong size

### Community 1305 - "Community 1305"
Cohesion: 1.00
Nodes (1): Test scale function with wrong type

### Community 1306 - "Community 1306"
Cohesion: 1.00
Nodes (1): Test scale function with wrong dimensions

### Community 1307 - "Community 1307"
Cohesion: 1.00
Nodes (1): Test scale function with wrong size

### Community 1308 - "Community 1308"
Cohesion: 1.00
Nodes (1): Test scale function with non-array

### Community 1309 - "Community 1309"
Cohesion: 1.00
Nodes (1): Test floor function with non-array

### Community 1310 - "Community 1310"
Cohesion: 1.00
Nodes (1): Test ceil function with wrong type

### Community 1311 - "Community 1311"
Cohesion: 1.00
Nodes (1): Test ceil function with wrong dimensions

### Community 1312 - "Community 1312"
Cohesion: 1.00
Nodes (1): Test ceil function with non-array

### Community 1313 - "Community 1313"
Cohesion: 1.00
Nodes (1): Test luSplit function

### Community 1314 - "Community 1314"
Cohesion: 1.00
Nodes (1): Test norm function with bad list

### Community 1315 - "Community 1315"
Cohesion: 1.00
Nodes (1): Test norm function with wrong dimensions

### Community 1316 - "Community 1316"
Cohesion: 1.00
Nodes (1): Test norm function with wrong size

### Community 1317 - "Community 1317"
Cohesion: 1.00
Nodes (1): Test norm function with non-container

### Community 1318 - "Community 1318"
Cohesion: 1.00
Nodes (1): Test max function with bad list

### Community 1319 - "Community 1319"
Cohesion: 1.00
Nodes (1): Test max function with non-container

### Community 1320 - "Community 1320"
Cohesion: 1.00
Nodes (1): Test max function with wrong dimensions

### Community 1321 - "Community 1321"
Cohesion: 1.00
Nodes (1): Test scale function with wrong dimensions

### Community 1322 - "Community 1322"
Cohesion: 1.00
Nodes (1): Test scale function with wrong size

### Community 1323 - "Community 1323"
Cohesion: 1.00
Nodes (1): Test scale function with non-array

### Community 1324 - "Community 1324"
Cohesion: 1.00
Nodes (1): Test floor function with non-array

### Community 1325 - "Community 1325"
Cohesion: 1.00
Nodes (1): Test ceil function with wrong type

### Community 1326 - "Community 1326"
Cohesion: 1.00
Nodes (1): Test ceil function with wrong dimensions

### Community 1327 - "Community 1327"
Cohesion: 1.00
Nodes (1): Test ceil function with non-array

### Community 1328 - "Community 1328"
Cohesion: 1.00
Nodes (1): Test luSplit function

### Community 1329 - "Community 1329"
Cohesion: 1.00
Nodes (1): Test norm function with bad list

### Community 1330 - "Community 1330"
Cohesion: 1.00
Nodes (1): Test norm function with wrong dimensions

### Community 1331 - "Community 1331"
Cohesion: 1.00
Nodes (1): Test norm function with wrong size

### Community 1332 - "Community 1332"
Cohesion: 1.00
Nodes (1): Test norm function with non-container

### Community 1333 - "Community 1333"
Cohesion: 1.00
Nodes (1): Test max function with bad list

### Community 1334 - "Community 1334"
Cohesion: 1.00
Nodes (1): Test max function with non-container

### Community 1335 - "Community 1335"
Cohesion: 1.00
Nodes (1): Test max function with wrong dimensions

### Community 1336 - "Community 1336"
Cohesion: 1.00
Nodes (1): Test reverse function with wrong size

### Community 1337 - "Community 1337"
Cohesion: 1.00
Nodes (1): Test reverse function with wrong type

### Community 1338 - "Community 1338"
Cohesion: 1.00
Nodes (1): Test reverse function with non-array

### Community 1339 - "Community 1339"
Cohesion: 1.00
Nodes (1): Test ones function with wrong dimensions

### Community 1340 - "Community 1340"
Cohesion: 1.00
Nodes (1): Test ones function with wrong type

### Community 1341 - "Community 1341"
Cohesion: 1.00
Nodes (1): Test ones function with non-array

### Community 1342 - "Community 1342"
Cohesion: 1.00
Nodes (1): Test zeros function with wrong dimensions

### Community 1343 - "Community 1343"
Cohesion: 1.00
Nodes (1): Test zeros function with wrong type

### Community 1344 - "Community 1344"
Cohesion: 1.00
Nodes (1): Test zeros function with non-array

### Community 1345 - "Community 1345"
Cohesion: 1.00
Nodes (1): Test eoSplit function

### Community 1346 - "Community 1346"
Cohesion: 1.00
Nodes (1): Test twos function with non-integer dimension

### Community 1347 - "Community 1347"
Cohesion: 1.00
Nodes (1): Test threes function with non-integer dimension

### Community 1348 - "Community 1348"
Cohesion: 1.00
Nodes (1): Test length function with bad list

### Community 1349 - "Community 1349"
Cohesion: 1.00
Nodes (1): Test length function with wrong size

### Community 1350 - "Community 1350"
Cohesion: 1.00
Nodes (1): Test length function with wrong dimensions

### Community 1351 - "Community 1351"
Cohesion: 1.00
Nodes (1): Test length function with non-container

### Community 1352 - "Community 1352"
Cohesion: 1.00
Nodes (1): Test prod function with bad list

### Community 1353 - "Community 1353"
Cohesion: 1.00
Nodes (1): Test prod function with wrong dimensions

### Community 1354 - "Community 1354"
Cohesion: 1.00
Nodes (1): Test prod function with non-container

### Community 1355 - "Community 1355"
Cohesion: 1.00
Nodes (1): Test sum function with bad list

### Community 1356 - "Community 1356"
Cohesion: 1.00
Nodes (1): A crude *bit of everything* smoke test to verify PyInstaller compatibility.  PyI

### Community 1358 - "Community 1358"
Cohesion: 1.00
Nodes (1): there was an issue where         repr(array([0], dtype='<u2')) and repr(array([0

### Community 1360 - "Community 1360"
Cohesion: 1.00
Nodes (1): TestLowerF2PYDirective

### Community 1361 - "Community 1361"
Cohesion: 1.00
Nodes (1): TestModuleDeclaration

### Community 1362 - "Community 1362"
Cohesion: 1.00
Nodes (1): Verify that datetime dtype __setstate__ can handle bad arguments

### Community 1363 - "Community 1363"
Cohesion: 1.00
Nodes (1): check isfinite, isinf, isnan for all units of <M, >M, <m, >m dtypes

### Community 1364 - "Community 1364"
Cohesion: 1.00
Nodes (1): Dates should have symmetric limits around the unix epoch at +/-np.int64

### Community 1365 - "Community 1365"
Cohesion: 1.00
Nodes (1): Limits should roundtrip when converted to strings.          This tests the conve

### Community 1366 - "Community 1366"
Cohesion: 1.00
Nodes (1): Test the calendar conversion at Neri-Schneider algorithm boundaries         and

### Community 1367 - "Community 1367"
Cohesion: 1.00
Nodes (2): gh22819_cli(), F90 file for testing disallowed CLI arguments in ghff819

### Community 1368 - "Community 1368"
Cohesion: 1.00
Nodes (2): gh23598_warn(), F90 file for testing warnings in gh23598

### Community 1369 - "Community 1369"
Cohesion: 1.00
Nodes (2): CLI :: -c -L/path/to/lib/ -l<libname>, test_npd_lib()

### Community 1370 - "Community 1370"
Cohesion: 1.00
Nodes (2): CLI :: -I/path/to/include/, test_npd_incl()

### Community 1371 - "Community 1371"
Cohesion: 1.00
Nodes (2): CLI :: <filename>.o <filename>.so <filename>.a, test_npd_linker()

### Community 1372 - "Community 1372"
Cohesion: 1.00
Nodes (2): Check that module names are handled correctly     gh-22819     Essentially, the, test_gh22819_cli()

### Community 1373 - "Community 1373"
Cohesion: 1.00
Nodes (2): Only one .pyf file allowed     gh-22819     CLI :: .pyf files, test_gh22819_many_pyf()

### Community 1374 - "Community 1374"
Cohesion: 1.00
Nodes (2): Ensures that a signature file is generated via the CLI     CLI :: -h, test_gen_pyf()

### Community 1375 - "Community 1375"
Cohesion: 1.00
Nodes (2): Ensures that a signature file can be dumped to stdout     CLI :: -h, test_gen_pyf_stdout()

### Community 1376 - "Community 1376"
Cohesion: 1.00
Nodes (2): Ensures that the CLI refuses to overwrite signature files     CLI :: -h without, test_gen_pyf_no_overwrite()

### Community 1377 - "Community 1377"
Cohesion: 1.00
Nodes (2): Ensures that the build directory can be specified      CLI :: --build-dir, test_build_dir()

### Community 1378 - "Community 1378"
Cohesion: 1.00
Nodes (2): Ensures that the build directory can be specified      CLI :: --overwrite-signat, test_overwrite()

### Community 1379 - "Community 1379"
Cohesion: 1.00
Nodes (2): Ensures that TeX documentation is written out      CLI :: --latex-doc, test_latexdoc()

### Community 1380 - "Community 1380"
Cohesion: 1.00
Nodes (2): Ensures that TeX documentation is written out      CLI :: --no-latex-doc, test_nolatexdoc()

### Community 1381 - "Community 1381"
Cohesion: 1.00
Nodes (2): Ensures that truncated documentation is written out      TODO: Test to ensure th, test_shortlatex()

### Community 1382 - "Community 1382"
Cohesion: 1.00
Nodes (2): Ensures that RsT documentation is written out      CLI :: --rest-doc, test_restdoc()

### Community 1383 - "Community 1383"
Cohesion: 1.00
Nodes (2): Ensures that TeX documentation is written out      CLI :: --no-rest-doc, test_norestexdoc()

### Community 1384 - "Community 1384"
Cohesion: 1.00
Nodes (2): Ensures that debugging wrappers are written      CLI :: --debug-capi, test_debugcapi()

### Community 1385 - "Community 1385"
Cohesion: 1.00
Nodes (2): Ensures that debugging wrappers work      CLI :: --debug-capi -c, test_debugcapi_bld()

### Community 1386 - "Community 1386"
Cohesion: 1.00
Nodes (2): Ensures that fortran subroutine wrappers for F77 are included by default      CL, test_wrapfunc_def()

### Community 1387 - "Community 1387"
Cohesion: 1.00
Nodes (2): Ensures that fortran subroutine wrappers for F77 can be disabled      CLI :: --n, test_nowrapfunc()

### Community 1388 - "Community 1388"
Cohesion: 1.00
Nodes (2): Add to the include directories      CLI :: -include     TODO: Document this in t, test_inclheader()

### Community 1389 - "Community 1389"
Cohesion: 1.00
Nodes (2): Add to the include directories      CLI :: --include-paths, test_inclpath()

### Community 1390 - "Community 1390"
Cohesion: 1.00
Nodes (2): Add to the include directories      CLI :: --help-link, test_hlink()

### Community 1391 - "Community 1391"
Cohesion: 1.00
Nodes (2): Check that Fortran-to-Python KIND specs can be passed      CLI :: --f2cmap, test_f2cmap()

### Community 1392 - "Community 1392"
Cohesion: 1.00
Nodes (2): Reduce verbosity      CLI :: --quiet, test_quiet()

### Community 1393 - "Community 1393"
Cohesion: 1.00
Nodes (2): Increase verbosity      CLI :: --verbose, test_verbose()

### Community 1394 - "Community 1394"
Cohesion: 1.00
Nodes (2): Ensure version      CLI :: -v, test_version()

### Community 1395 - "Community 1395"
Cohesion: 1.00
Nodes (2): CLI :: -c --fcompiler, test_npd_fcompiler()

### Community 1396 - "Community 1396"
Cohesion: 1.00
Nodes (2): CLI :: -c --help-fcompiler, test_npd_help_fcompiler()

### Community 1397 - "Community 1397"
Cohesion: 1.00
Nodes (2): CLI :: -c --link-<resource>, test_npd_link_auto()

### Community 1399 - "Community 1399"
Cohesion: 1.00
Nodes (1): A bundle of arguments to be passed to a test case, with an identifying         n

### Community 1400 - "Community 1400"
Cohesion: 1.00
Nodes (2): Byte control characters (comments, delimiter) are supported., test_control_characters_as_bytes()

### Community 1401 - "Community 1401"
Cohesion: 1.00
Nodes (2): skiprows and max_rows should raise for negative parameters., test_exception_negative_row_limits()

### Community 1402 - "Community 1402"
Cohesion: 1.00
Nodes (2): Test that both 'e' and 'E' are parsed correctly., test_scientific_notation()

### Community 1403 - "Community 1403"
Cohesion: 1.00
Nodes (2): With the 'bytes' encoding, tokens are encoded prior to being     passed to the c, test_converter_with_unicode_dtype()

### Community 1404 - "Community 1404"
Cohesion: 1.00
Nodes (2): The given dtype is just 'S' or 'U' with no length. In these cases, the     lengt, test_string_no_length_given()

### Community 1405 - "Community 1405"
Cohesion: 1.00
Nodes (2): Some tests that the conversion to float64 works as accurately as the     Python, test_float_conversion()

### Community 1406 - "Community 1406"
Cohesion: 1.00
Nodes (2): Test exception when a character cannot be encoded as 'S'., test_character_not_bytes_compatible()

### Community 1407 - "Community 1407"
Cohesion: 1.00
Nodes (2): Support for quoted fields is disabled by default., test_quote_support_default()

### Community 1408 - "Community 1408"
Cohesion: 1.00
Nodes (2): Check that a UserWarning is emitted when no data is read from input., test_warn_on_no_data()

### Community 1409 - "Community 1409"
Cohesion: 1.00
Nodes (2): Check that the correct unit (e.g. month, day, second) is discovered from     the, test_parametric_unit_discovery()

### Community 1410 - "Community 1410"
Cohesion: 1.00
Nodes (2): iter_iterindices(), test_iter_iterindex()

### Community 1411 - "Community 1411"
Cohesion: 1.00
Nodes (2): Tests the strides with the contig flag for both broadcast and non-broadcast, test_iter_contig_flag_single_operand_strides()

### Community 1412 - "Community 1412"
Cohesion: 1.00
Nodes (2): using a context amanger and using nditer.close are equivalent, test_close_equivalent()

### Community 1413 - "Community 1413"
Cohesion: 1.00
Nodes (2): Checks for reference counting leaks during cleanup.  Using explicit     referenc, test_partial_iteration_cleanup()

### Community 1414 - "Community 1414"
Cohesion: 1.00
Nodes (2): Matches the expected output of a debug print with the actual output.     Note th, test_debug_print()

### Community 1415 - "Community 1415"
Cohesion: 1.00
Nodes (1): Verify fromrecords works with a 0-length input

### Community 1416 - "Community 1416"
Cohesion: 1.00
Nodes (1): Test that nested structured types are treated as records too

### Community 1417 - "Community 1417"
Cohesion: 1.00
Nodes (1): test that trailing padding is preserved

### Community 1418 - "Community 1418"
Cohesion: 1.00
Nodes (2): Test as_strided with check_bounds=True with different dtypes., test_as_strided_checked_different_dtypes()

### Community 1419 - "Community 1419"
Cohesion: 1.00
Nodes (2): Test 1D arrays with positive strides., test_as_strided_checked_1d_positive_strides()

### Community 1420 - "Community 1420"
Cohesion: 1.00
Nodes (2): Test sliding window views in 1D., test_as_strided_checked_sliding_window_1d()

### Community 1421 - "Community 1421"
Cohesion: 1.00
Nodes (2): Test 2D arrays with default strides., test_as_strided_checked_2d_default_strides()

### Community 1422 - "Community 1422"
Cohesion: 1.00
Nodes (2): Test zero strides (broadcasting a single value)., test_as_strided_checked_zero_stride_broadcasting()

### Community 1423 - "Community 1423"
Cohesion: 1.00
Nodes (2): Test that out-of-bounds positive strides raise ValueError., test_as_strided_checked_out_of_bounds_positive_strides()

### Community 1424 - "Community 1424"
Cohesion: 1.00
Nodes (2): Test as_strided      - with check_bounds=True     - considers the base array bou, test_as_strided_checked_view_of_larger_array()

### Community 1425 - "Community 1425"
Cohesion: 1.00
Nodes (2): Test as_strided      - with check_bounds=True     - on a view that doesn't start, test_as_strided_checked_view_with_offset()

### Community 1426 - "Community 1426"
Cohesion: 1.00
Nodes (2): Test that negative strides on a view correctly detect out of bounds., test_as_strided_checked_view_out_of_bounds_negative()

### Community 1427 - "Community 1427"
Cohesion: 1.00
Nodes (2): Test that positive strides on a view correctly detect out of bounds., test_as_strided_checked_view_out_of_bounds_positive()

### Community 1428 - "Community 1428"
Cohesion: 1.00
Nodes (2): Test as_strided with check_bounds=True on a view of a view., test_as_strided_checked_nested_views()

### Community 1429 - "Community 1429"
Cohesion: 1.00
Nodes (2): Test various slicing scenarios., test_as_strided_checked_sliced_array()

### Community 1430 - "Community 1430"
Cohesion: 1.00
Nodes (2): Parametrized test for various view and stride combinations., test_as_strided_checked_view_parametrized()

### Community 1431 - "Community 1431"
Cohesion: 1.00
Nodes (1): Test generalized ufunc with zero-sized operands

### Community 1432 - "Community 1432"
Cohesion: 1.00
Nodes (1): Test with fixed-sized signature.

### Community 1433 - "Community 1433"
Cohesion: 1.00
Nodes (1): The type of the result should always depend on the selected loop, not         ne

### Community 1434 - "Community 1434"
Cohesion: 1.00
Nodes (1): Try to check presence and results of all ufuncs.          The list of ufuncs com

### Community 1435 - "Community 1435"
Cohesion: 1.00
Nodes (1): Basic test for the safest casts, because ufuncs inner loops can         indicate

### Community 1436 - "Community 1436"
Cohesion: 1.00
Nodes (1): Check that (x†A)x equals x†(Ax).

### Community 1439 - "Community 1439"
Cohesion: 1.00
Nodes (1): A module with the precisions of platform-specific `~numpy.number`s.

### Community 1440 - "Community 1440"
Cohesion: 1.00
Nodes (1): # NOTE: `_StrLike_co` and `_BytesLike_co` are pointless, as `np.str_` and

## Knowledge Gaps
- **1992 isolated node(s):** `This file is used by asv_compare.conf.json.tpl.`, `# FIXME: there's no official way to provide extra information to the test log`, `Generates a cached random array that covers several scenarios that     may affec`, `Pytest configuration and fixtures for the Numpy test suite.`, `NotArray` (+1987 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 0`** (1 nodes): `TestRegression`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 4`** (1 nodes): `TestUfunc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 8`** (2 nodes): `TestBroadcast`, `TestRandomDist`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (1 nodes): `TestDateTime`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (1 nodes): `# NOTE: This is true even for a reduction, where we return a 0-stride`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `TestMethods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (2 nodes): `TestBroadcast`, `TestRandomDist`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (2 nodes): `TestMaskedArrayFunctions`, `TestMaskedArrayMethods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (2 nodes): `TestMaskedArray`, `TestMaskedConstant`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (2 nodes): `TestBroadcast`, `TestRandomDist`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (2 nodes): `Tests specific to `np.loadtxt` added during the move of loadtxt to be backed by`, `# NOTE: It is unclear that the `  # comment` should succeed. Except`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 81`** (1 nodes): `TestMaskedArrayArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 93`** (2 nodes): `_foo2()`, `TestVectorize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 94`** (1 nodes): `TestIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 99`** (1 nodes): `Module containing non-deprecated functions borrowed from Numeric.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 104`** (1 nodes): `RNG`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 126`** (1 nodes): `TestNonarrayArgs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 131`** (2 nodes): `The addition method is special for the scaled float, because it         includes`, `TestSFloat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 140`** (1 nodes): `TestCreation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 150`** (1 nodes): `TestMethods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 155`** (1 nodes): `Core`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 168`** (1 nodes): `TestMaskedArrayInPlaceArithmetic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 172`** (1 nodes): `TestHistogram`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (2 nodes): `These currently never use the hash-based solution.  However,         it seems ea`, `TestUnique`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 192`** (1 nodes): `TestUnwrap`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 217`** (2 nodes): `Tests of interaction of matrix with other parts of numpy.  Note that tests with`, `TestConcatenatorMatrix`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 218`** (2 nodes): `TestAllclose`, `TestIsclose`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 226`** (2 nodes): `Test getting and setting global print options.`, `TestPrintOptions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 227`** (2 nodes): `TestIndices`, `TestNonzero`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 235`** (1 nodes): `TestMemmap`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 237`** (1 nodes): `TestSpecialMethods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 250`** (1 nodes): `TestRegression`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 260`** (1 nodes): `TestFillingValues`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 263`** (1 nodes): `TestRegression`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 268`** (1 nodes): `TestIntegers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 283`** (2 nodes): `Test that appended and prepended values are equal`, `TestStatistic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 286`** (2 nodes): `Check that np.dtype('x,y') matches [np.dtype('x'), np.dtype('y')]         Exampl`, `TestFromCTypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 288`** (1 nodes): `TestBlock`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 301`** (1 nodes): `TestStructured`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 302`** (2 nodes): `This file adds basic tests to test the NEP 50 style promotion compatibility mode`, `# NOTE: It may make sense to normalize the behavior!`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 303`** (1 nodes): `TestFromrecords`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 306`** (2 nodes): `Check that strings are stored in the arena when possible.      This tests implem`, `TestImplementation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 307`** (2 nodes): `TestMethodsWithUnicode`, `TestMixedTypeMethods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 311`** (1 nodes): `Where`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 318`** (1 nodes): `These tests are based on the doctests from `numpy/lib/recfunctions.py`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 320`** (1 nodes): `TestInformation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 326`** (2 nodes): `byte_to_true()`, `simd_logical_or_u8()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 338`** (2 nodes): `TestConcatenator`, `TestRavelUnravelIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 340`** (1 nodes): `TestZeroSizeFlexible`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 341`** (2 nodes): `Metadata handling in promotion does not appear formalized         right now in N`, `TestTypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 342`** (1 nodes): `TestCount`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 355`** (1 nodes): `This module contains a set of functions for vectorized string operations.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 363`** (1 nodes): `TestBinomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 365`** (1 nodes): `TestMRecords`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 368`** (1 nodes): `TestRecord`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 370`** (2 nodes): `check_itemsize()`, `TestReplaceOnArrays`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 376`** (1 nodes): `ArrayCoercionSmall`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 379`** (2 nodes): `pow_zi()`, `z_div()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 385`** (2 nodes): `initialize_abstract_dtypes()`, `make_raw_dtype()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 394`** (2 nodes): `Test printing of scalar types.`, `TestRealScalars`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 400`** (1 nodes): `Mapping`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 417`** (2 nodes): `Test whether matrix.sum(axis=1) preserves orientation.         Fails in NumPy <=`, `TestProperties`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 419`** (2 nodes): `Test ufunc call memory overlap handling`, `TestUFunc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 420`** (2 nodes): `TestBroadcast`, `TestCreationFuncs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 421`** (1 nodes): `TestArrayLike`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 422`** (1 nodes): `TestParameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 425`** (1 nodes): `TestConcatenate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 426`** (2 nodes): `Test extend reduce sum intrinsics:             npyv_sumup_##sfx`, `Logical operations for boolean types.         Test intrinsics:             npyv_`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 428`** (1 nodes): `TestSymbolic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 429`** (1 nodes): `TestArrayAlmostEqualNulp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 434`** (2 nodes): `ScalarMath`, `ScalarStr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 443`** (2 nodes): `NpyCapsule_FromVoidPtr()`, `NpyCapsule_FromVoidPtrAndDesc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 445`** (2 nodes): `Regression test for https://github.com/numpy/numpy/issues/5982`, `TestOperations`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 446`** (1 nodes): `TestPickling`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 448`** (1 nodes): `TestWritebackIfCopy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 449`** (2 nodes): `NIterError`, `TestFromiter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 450`** (2 nodes): `assert_mt19937_state_equal()`, `TestSetState`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 451`** (1 nodes): `TestRecFunctions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 453`** (2 nodes): `TestApplyAlongAxis`, `TestApplyOverAxes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 454`** (1 nodes): `TestLowlevelAPIAccess`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 455`** (1 nodes): `TestPower`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 456`** (1 nodes): `TestRationalFunctions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 478`** (1 nodes): `f90_return_integer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 479`** (1 nodes): `f90_return_logical`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 482`** (2 nodes): `npyv_cmpgt_s64()`, `npyv_cmpgt_u64()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 484`** (1 nodes): `NAType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 486`** (1 nodes): `TestConditionalShortcuts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 488`** (1 nodes): `_assert_equal_hash()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 489`** (2 nodes): `TestComparisons`, `TestComparisonsMixed2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 491`** (1 nodes): `TestString`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 494`** (1 nodes): `TestArange`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 495`** (1 nodes): `TestRecord`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 497`** (1 nodes): `TestJoinBy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 498`** (2 nodes): `Test scalar buffer interface adheres to PEP 3118`, `TestScalarPEP3118`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 500`** (2 nodes): `comp_state()`, `warmup()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 503`** (2 nodes): `npyv_pack_b8_b16()`, `npyv_pack_b8_b32()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 510`** (2 nodes): `array_converter_wrap()`, `find_wrap()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 514`** (1 nodes): `Object`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 520`** (1 nodes): `TestBool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 521`** (2 nodes): `TestBaseRepr`, `TestBinaryRepr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 522`** (2 nodes): `TestCross`, `TestTensordot`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 525`** (1 nodes): `TestDivision`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 526`** (2 nodes): `TestArrayAlmostEqual`, `TestULP`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 530`** (1 nodes): `Import`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 531`** (1 nodes): `Records`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 540`** (2 nodes): `busdaycalendar_init()`, `normalize_holidays_list()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 543`** (1 nodes): `f90_return_char`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 544`** (1 nodes): `f90_return_complex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 546`** (1 nodes): `f90_return_real`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 549`** (2 nodes): `Test the error paths, including for memory leaks`, `TestArrayLikes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 550`** (1 nodes): `TestConstant`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 553`** (1 nodes): `TestNewScalarIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 554`** (1 nodes): `TestShape`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 555`** (1 nodes): `LoadTxtBase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 558`** (2 nodes): `TestNDArrayArrayFunction`, `TestNDArrayMethods`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 559`** (1 nodes): `TestRandint`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 560`** (1 nodes): `Test_SIMD_MODULE`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 561`** (2 nodes): `_signs()`, `TestRemainder`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 562`** (1 nodes): `Tests for the NumpyVersion class.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 567`** (1 nodes): `CustomInplace`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 572`** (1 nodes): `foddity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 587`** (2 nodes): `allocateMemory()`, `Farray()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 589`** (1 nodes): `Tests for the private NumPy argument parsing functionality. They mainly exists t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 591`** (1 nodes): `TestArrayRepr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 592`** (2 nodes): `TestArithmetic`, `trim()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 594`** (1 nodes): `TestMisc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 596`** (1 nodes): `TestGeneric`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 597`** (1 nodes): `TestMultinomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 598`** (2 nodes): `TestArithmetic`, `trim()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 600`** (1 nodes): `TestMatrixPower`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 601`** (2 nodes): `Tests suite for mrecords.  :author: Pierre Gerard-Marchant :contact: pierregm_at`, `TestMRecordsImport`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 604`** (1 nodes): `TestTemporaryElide`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 605`** (1 nodes): `TestIterNested`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 606`** (2 nodes): `Test ones_like, zeros_like, empty_like and full_like`, `TestLikeFuncs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 607`** (1 nodes): `TestRequire`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 608`** (1 nodes): `TestArrayFunctionImplementation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 610`** (1 nodes): `TestRandint`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 611`** (1 nodes): `TestMultinomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 613`** (2 nodes): `test_writeable()`, `TestSlidingWindowView`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 614`** (1 nodes): `TestComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 622`** (2 nodes): `Benchmarks for the NumPy small-allocation cache.  NumPy caches data allocations`, `SmallArrayCreation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 623`** (1 nodes): `Polynomial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 629`** (2 nodes): `foo`, `procedure`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 643`** (1 nodes): `TestNumpyConfig`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 644`** (1 nodes): `TestBasic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 645`** (1 nodes): `TestVecString`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 647`** (2 nodes): `Test cases related to more complex DType promotions.  Further promotion     test`, `TestPromotion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 648`** (1 nodes): `TestErrstate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 649`** (1 nodes): `TestIOSF`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 651`** (1 nodes): `TestMisc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 652`** (1 nodes): `TestCReaderUnitTests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 653`** (1 nodes): `TestConversion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 656`** (1 nodes): `TestResize`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 657`** (1 nodes): `TestEvaluation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 658`** (1 nodes): `TestMisc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 659`** (1 nodes): `TestSetState`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 660`** (1 nodes): `TestSeed`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 662`** (1 nodes): `params_1()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 663`** (2 nodes): `TestAbsoluteNegative`, `TestMinMax`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 665`** (2 nodes): `get_initial_from_ufunc()`, `PyArray_NewLegacyWrappingArrayMethod()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 667`** (2 nodes): `get_wrapping_auxdata()`, `wrapping_method_get_loop()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 669`** (2 nodes): `ops_module`, `subroutine`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 676`** (2 nodes): `c_void_p`, `dummy_ctype`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 687`** (1 nodes): `Object`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 690`** (1 nodes): `TestABC`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 691`** (1 nodes): `TestNested`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 693`** (1 nodes): `TestPadWidth`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 694`** (1 nodes): `TestEvaluation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 696`** (1 nodes): `TestDTypeClasses`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 697`** (1 nodes): `TestMultivariateHypergeometric`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 698`** (1 nodes): `TestSeed`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 700`** (1 nodes): `TestISOC`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 701`** (1 nodes): `TestEvaluation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 702`** (1 nodes): `TestQR`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 703`** (2 nodes): `TestTensorinv`, `TestTensorsolve`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 704`** (1 nodes): `TestView`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 705`** (1 nodes): `TestAssignment`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 706`** (1 nodes): `TestFancyIndexing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 708`** (2 nodes): `This test array_equal for a few combinations:          - are the two inputs the`, `TestArrayComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 709`** (1 nodes): `TestMoveaxis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 710`** (1 nodes): `Test_sctype2char`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 711`** (1 nodes): `TestIsSubDType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 712`** (2 nodes): `Check the numpy config is valid.`, `TestNumPyConfigs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 713`** (1 nodes): `TestGetImplementingArgs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 714`** (1 nodes): `TestConstants`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 715`** (1 nodes): `params_0()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 717`** (2 nodes): `TestBitwiseUFuncs`, `TestFrompyfunc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 725`** (1 nodes): `coddity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 738`** (2 nodes): `bounded_uint()`, `bounded_uints()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 743`** (1 nodes): `TestTimeScalars`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 744`** (1 nodes): `TestByteBounds`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 745`** (2 nodes): `TestAssumedShapeSumExample`, `TestF2cmapOption`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 747`** (2 nodes): `test_fit()`, `TestInterpolate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 748`** (1 nodes): `TestParamEval`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 749`** (1 nodes): `TestParamParseNestedParens`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 750`** (2 nodes): `Test deeply nested subtypes.`, `TestMonsterType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 751`** (1 nodes): `TestMetadata`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 752`** (1 nodes): `TestSingleEltArrayInput`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 753`** (1 nodes): `TestRoll`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 754`** (2 nodes): `Check correctness of `np.isdtype`. The test considers different argument     con`, `TestIsDType`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 756`** (1 nodes): `TestNumPyFunctions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 757`** (1 nodes): `TestVerifyMatchingSignatures`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 758`** (1 nodes): `TestSingleEltArrayInput`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 759`** (1 nodes): `TestJoinBy2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 760`** (2 nodes): `TestFReturnCharacter`, `TestReturnCharacter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 761`** (2 nodes): `TestFReturnComplex`, `TestReturnComplex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 762`** (2 nodes): `TestFReturnInteger`, `TestReturnInteger`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 763`** (2 nodes): `TestFReturnLogical`, `TestReturnLogical`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 765`** (1 nodes): `TestExpandDims`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 767`** (1 nodes): `TestGUFuncProcessCoreDims`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 770`** (2 nodes): `TestExpm1`, `TestLog1p`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 781`** (1 nodes): `StringComparisons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 792`** (2 nodes): `Pytest configuration and fixtures for the Numpy test suite.`, `SkipMatplotlibOutputChecker`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 795`** (2 nodes): `mod1`, `mod2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 796`** (2 nodes): `mod1`, `mod2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 799`** (2 nodes): `mathops`, `useops`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 805`** (2 nodes): `_PyArrayNeighborhoodIter_IncrCoord()`, `PyArrayNeighborhoodIter_Next()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 808`** (1 nodes): `TestContextManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 809`** (1 nodes): `TestConstants`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 810`** (2 nodes): `TestCommonBlock`, `TestCommonWithUse`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 811`** (1 nodes): `TestMarkinnerspaces`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 812`** (1 nodes): `TestPublicPrivate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 813`** (1 nodes): `TestSetState`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 814`** (1 nodes): `TestThread`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 815`** (1 nodes): `TestConstants`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 816`** (1 nodes): `TestVander`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 817`** (1 nodes): `TestBoolArray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 818`** (1 nodes): `TestFloatExceptions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 819`** (1 nodes): `Check the numpy version is valid.  Note that a development version is marked by`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 820`** (1 nodes): `TestVander`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 822`** (1 nodes): `TestThread`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 823`** (1 nodes): `TestSingleEltArrayInput`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 824`** (1 nodes): `TestThread`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 825`** (2 nodes): `TestRenamedFunc`, `TestRenamedSubroutine`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 826`** (1 nodes): `Test scripts  Test that we can run executable scripts that have been installed w`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 827`** (2 nodes): `TestCallstatement`, `TestMultiline`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 829`** (1 nodes): `TestSizeSumExample`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 830`** (1 nodes): `TestUFuncInspectSignature`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 831`** (1 nodes): `TestUfuncKwargs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 832`** (1 nodes): `TestAccuracy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 833`** (1 nodes): `TestAVXFloat32Transcendental`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 834`** (1 nodes): `TestSign`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 835`** (1 nodes): `TestBuildErrorMessage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 836`** (1 nodes): `TestWarns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 841`** (1 nodes): `mod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 842`** (1 nodes): `# FIXME: there's no official way to provide extra information to the test log`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 843`** (1 nodes): `utils`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 849`** (2 nodes): `npy_longdouble_from_PyLong()`, `_PyLong_Bytes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 852`** (2 nodes): `PyUFunc_HasOverride()`, `PyUFuncOverride_GetNonDefaultArrayUfunc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 858`** (1 nodes): `gh23879`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 868`** (2 nodes): `Returns the type of the dtype of the input variable.`, `Upgrade the mapper of a StringConverter by adding a new function and         its`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 886`** (2 nodes): `Index`, `SubClass`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 887`** (1 nodes): `Simple expression that should pass with mypy.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 891`** (2 nodes): `F_GLOBALS`, `MOD_TYPES`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 892`** (2 nodes): `dat`, `datonly`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 893`** (1 nodes): `mtypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 913`** (1 nodes): `TestAbstractInterface`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 915`** (1 nodes): `TestBadSequences`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 916`** (1 nodes): `TestStringDiscovery`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 917`** (2 nodes): `get_module()`, `Some codes to generate data and manage temporary buffers use when     sharing wi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 918`** (2 nodes): `These test cases exercise some behaviour changes`, `TestChanges`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 919`** (1 nodes): `TestVander`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 920`** (2 nodes): `This test suite tests various expressions that are used as dimension     specifi`, `TestDimSpec`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 921`** (1 nodes): `TestInplace`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 922`** (2 nodes): `Test if all ``.pyi`` files are properly installed.`, `TestIsFile`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 923`** (1 nodes): `TestDerivative`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 924`** (1 nodes): `TestIntegral`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 925`** (1 nodes): `TestNorm_NonSystematic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 927`** (1 nodes): `TestMixed`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 930`** (1 nodes): `TestMultipleFields`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 931`** (1 nodes): `TestCompanion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 932`** (2 nodes): `See https://github.com/numpy/numpy/pull/10676.`, `TestQuotedCharacter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 934`** (1 nodes): `TestStringLikeCasts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 935`** (1 nodes): `TestOverride`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 936`** (2 nodes): `Tests for PyUFunc_ReplaceLoopBySignature C API.`, `TestReplaceLoopBySignature`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 937`** (1 nodes): `TestConstants`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 938`** (1 nodes): `TestLDExp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 939`** (1 nodes): `TestLog2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 940`** (1 nodes): `TestOut`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 948`** (1 nodes): `A set of methods retained from np.compat module that are still used across codeb`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 949`** (1 nodes): `test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 952`** (2 nodes): `parse_distributions_h()`, `Parse distributions.h located in inc_dir for CFFI, filling in the ffi.cdef`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 954`** (2 nodes): `accumulate()`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 956`** (1 nodes): `mod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 958`** (1 nodes): `Docstrings for generated ufuncs  The syntax is designed to look like the functio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 959`** (1 nodes): `mod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 960`** (2 nodes): `data`, `typedefmod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 964`** (1 nodes): `Returns true for each element if all cased characters in the         string are`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 966`** (1 nodes): `Create the numpy._core.umath namespace for backward compatibility. In v1.16 the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 968`** (1 nodes): `test_bug`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 969`** (1 nodes): `utils`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 970`** (1 nodes): `util`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 971`** (1 nodes): `foo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 972`** (1 nodes): `foo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 973`** (1 nodes): `foo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 974`** (2 nodes): `ISO_C_BINDING maps for f2py2e. Only required declarations/macros/functions will`, `# TODO: See gh-25229`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 975`** (1 nodes): `data`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 979`** (1 nodes): `foo_fixed`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 980`** (1 nodes): `foo_free`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 981`** (1 nodes): `alloc_char_mod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 982`** (1 nodes): `mod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 986`** (1 nodes): `r""" Building the required library in this example requires a source distributio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 989`** (1 nodes): `A`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 990`** (2 nodes): `Tests for :mod:`numpy._core.numeric`.  Does not include tests which fall under ``, `SubClass`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 992`** (1 nodes): `adder`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 993`** (1 nodes): `char_test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 994`** (1 nodes): `Test floor function with wrong type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 995`** (1 nodes): `Test floor function with wrong type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 996`** (1 nodes): `TestBlockDocString`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 998`** (1 nodes): `TestIntegral`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 999`** (2 nodes): `Testing the utilities of the CPU dispatcher`, `test_dispatcher()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1000`** (2 nodes): `address ReDOS vulnerability:         https://github.com/numpy/numpy/issues/23338`, `TestNameArgsPatternBacktracking`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1001`** (1 nodes): `TestCrackFortran`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1002`** (1 nodes): `TestExternal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1003`** (1 nodes): `TestModuleProcedure`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1004`** (2 nodes): `Tests for structural pattern matching support (PEP 634).`, `TestPatternMatching`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1005`** (1 nodes): `TestPower`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1006`** (1 nodes): `TestFlatiterIndexing0dBoolIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1007`** (1 nodes): `TestFlatiterIndexingFloatIndex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1008`** (1 nodes): `TestRoundDeprecation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1009`** (1 nodes): `TestWarningUtilityDeprecations`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1010`** (1 nodes): `TestF2Cmap`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1012`** (1 nodes): `Straightforward testing with a mixture of linspace data (for         consistency`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1013`** (1 nodes): `TestSctypeDict`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1014`** (1 nodes): `TestIntegral`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1016`** (2 nodes): `Compile and run pyinstaller-smoke.py using PyInstaller.`, `test_pyinstaller()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1017`** (1 nodes): `TestUnicodeOnlyMethodsRaiseWithBytes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1018`** (1 nodes): `TestAddDocstring`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1019`** (1 nodes): `TestAttributes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1020`** (1 nodes): `TestCbrt`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1021`** (1 nodes): `TestFPClass`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1022`** (1 nodes): `TestHypotErrorMessages`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1023`** (1 nodes): `TestPositive`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1024`** (1 nodes): `TestUserCode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1025`** (1 nodes): `TestValueAttr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1026`** (2 nodes): `create_conv_funcs()`, `read_rows()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1028`** (2 nodes): `get_submodule_paths()`, `Get paths to submodules so that we can exclude them from things like     check_t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1030`** (1 nodes): `fortfuncs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1032`** (1 nodes): `precision`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1036`** (1 nodes): `This file is used by asv_compare.conf.json.tpl.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1042`** (1 nodes): `Use cffi to access any of the underlying C functions from distributions.h`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1110`** (1 nodes): `FloatStatus`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1111`** (1 nodes): `Half`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1116`** (1 nodes): `Returns true for each element if all characters in the string are         digits`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1117`** (1 nodes): `For each element in `self`, return True if there are only         numeric charac`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1118`** (1 nodes): `Returns true for each element if there are only whitespace         characters in`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1119`** (1 nodes): `Returns true for each element if the element is a titlecased         string and`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1120`** (1 nodes): `Return a string which is the concatenation of the strings in the         sequenc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1121`** (1 nodes): `For each element in `self`, return a copy with the leading characters         re`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1122`** (1 nodes): `Return (other + self), that is string concatenation,         element-wise for a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1123`** (1 nodes): `For each element in `self`, return a copy of the string with all         occurre`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1124`** (1 nodes): `For each element in `self`, return the highest index in the string         where`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1125`** (1 nodes): `Like `rfind`, but raises :exc:`ValueError` when the substring `sub` is         n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1126`** (1 nodes): `For each element in `self`, return a list of the lines in the         element, b`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1127`** (1 nodes): `For each element in `self`, return a copy with the leading and         trailing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1128`** (2 nodes): `diagonal()`, `Return specified diagonals.      If `a` is 2-D, returns the diagonal of `a` with`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1129`** (2 nodes): `mean()`, `Compute the arithmetic mean along the specified axis.      Returns the average o`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1130`** (2 nodes): `ndim()`, `Return the number of dimensions of an array.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1131`** (2 nodes): `partition()`, `Return a partitioned copy of an array.      Creates a copy of the array and part`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1132`** (2 nodes): `ptp()`, `Range of values (maximum - minimum) along an axis.      The name of the function`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1133`** (2 nodes): `put()`, `Replaces specified elements of an array with given values.      The indexing wor`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1134`** (2 nodes): `Return a sorted copy of an array.      Parameters     ----------     a : array_l`, `sort()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1135`** (2 nodes): `Return the sum along diagonals of the array.      If `a` is 2-D, the sum along i`, `trace()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1136`** (2 nodes): `r"""     Compute the standard deviation along the specified axis.      Returns t`, `std()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1137`** (2 nodes): `r"""     Compute the variance along the specified axis.      Returns the varianc`, `var()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1138`** (2 nodes): `busday_count()`, `busday_count(         begindates,         enddates,         weekmask='1111100',`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1139`** (2 nodes): `busday_offset()`, `busday_offset(         dates,         offsets,         roll='raise',         wee`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1140`** (2 nodes): `can_cast()`, `can_cast(from_, to, casting='safe')      Returns True if cast between data types`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1141`** (2 nodes): `concatenate()`, `concatenate(         arrays,         /,         axis=0,         out=None,`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1142`** (2 nodes): `copyto()`, `copyto(dst, src, casting='same_kind', where=True)      Copies values from one ar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1143`** (2 nodes): `datetime_as_string()`, `datetime_as_string(arr, unit=None, timezone='naive', casting='same_kind')      C`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1144`** (2 nodes): `dot()`, `dot(a, b, out=None)      Dot product of two arrays. Specifically,      - If both`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1145`** (2 nodes): `empty_like()`, `empty_like(         prototype,         /,         dtype=None,         order='K',`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1146`** (2 nodes): `inner()`, `inner(a, b, /)      Inner product of two arrays.      Ordinary inner product of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1147`** (2 nodes): `is_busday()`, `is_busday(         dates,         weekmask='1111100',         holidays=None,`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1148`** (2 nodes): `lexsort()`, `lexsort(keys, axis=-1)      Perform an indirect stable sort using a sequence of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1149`** (2 nodes): `may_share_memory()`, `may_share_memory(a, b, /, max_work=0)      Determine if two arrays might share m`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1150`** (2 nodes): `min_scalar_type()`, `min_scalar_type(a, /)      For scalar ``a``, returns the data type with the smal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1151`** (2 nodes): `packbits()`, `packbits(a, /, axis=None, bitorder='big')      Packs the elements of a binary-va`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1152`** (2 nodes): `putmask()`, `putmask(a, /, mask, values)      Changes elements of an array based on condition`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1153`** (2 nodes): `unravel_index(indices, shape, order='C')      Converts a flat index or array of`, `unravel_index()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1154`** (2 nodes): `unpackbits(a, /, axis=None, count=None, bitorder='big')      Unpacks elements of`, `unpackbits()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1155`** (2 nodes): `shares_memory(a, b, /, max_work=-1)      Determine if two arrays share memory.`, `shares_memory()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1156`** (2 nodes): `where(condition, [x, y], /)      Return elements chosen from `x` or `y` dependin`, `where()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1157`** (2 nodes): `result_type(*arrays_and_dtypes)      Returns the type that results from applying`, `result_type()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1158`** (2 nodes): `r"""     vdot(a, b, /)      Return the dot product of two vectors.      The `vdo`, `vdot()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1160`** (1 nodes): `Stores and defines the low-level format_options context variable.  This is defin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1161`** (2 nodes): `capitalize()`, `Return a copy of ``a`` with only the first character of each element     capital`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1162`** (2 nodes): `center()`, `Return a copy of `a` with its elements centered in a string of     length `width`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1163`** (2 nodes): `count()`, `Returns an array with the number of non-overlapping occurrences of     substring`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1164`** (2 nodes): `endswith()`, `Returns a boolean array which is `True` where the string element     in ``a`` en`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1165`** (2 nodes): `expandtabs()`, `Return a copy of each string element where all tab characters are     replaced b`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1166`** (2 nodes): `find()`, `For each element, return the lowest index in the string where     substring ``su`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1167`** (2 nodes): `index()`, `Like `find`, but raises :exc:`ValueError` when the substring is not found.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1168`** (2 nodes): `ljust()`, `Return an array with the elements of `a` left-justified in a     string of lengt`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1169`** (2 nodes): `lower()`, `Return an array with the elements converted to lowercase.      Call :meth:`str.l`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1170`** (2 nodes): `lstrip()`, `For each element in `a`, return a copy with the leading characters     removed.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1171`** (2 nodes): `multiply()`, `Return (a * i), that is string multiple concatenation,     element-wise.      Va`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1172`** (2 nodes): `partition()`, `Partition each element in ``a`` around ``sep``.      For each element in ``a``,`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1173`** (2 nodes): `For each element in `a`, return a copy with the leading and     trailing charact`, `strip()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1174`** (2 nodes): `Return an array with the elements converted to uppercase.      Calls :meth:`str.`, `upper()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1175`** (2 nodes): `Return element-wise a copy of the string with     uppercase characters converted`, `swapcase()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1176`** (2 nodes): `Return element-wise title cased version of string or unicode.      Title case wo`, `title()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1177`** (2 nodes): `For each element in ``a``, return a copy of the string with     occurrences of s`, `replace()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1178`** (2 nodes): `Partition (split) each element around the right-most separator.      For each el`, `rpartition()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1179`** (2 nodes): `Slice the strings in `a` by slices specified by `start`, `stop`, `step`.     Lik`, `slice()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1180`** (2 nodes): `For each element, return the highest index in the string where     substring ``s`, `rfind()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1181`** (2 nodes): `Like `rfind`, but raises :exc:`ValueError` when the substring `sub` is     not f`, `rindex()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1182`** (2 nodes): `Returns a boolean array which is `True` where the string element     in ``a`` st`, `startswith()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1183`** (2 nodes): `Return an array with the elements of `a` right-justified in a     string of leng`, `rjust()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1184`** (2 nodes): `Return the numeric string left-filled with zeros. A leading     sign prefix (``+`, `zfill()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1185`** (2 nodes): `For each element in `a`, return a copy with the trailing characters     removed.`, `rstrip()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1186`** (1 nodes): `Due to compatibility, numpy has a very large number of different naming conventi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1188`** (1 nodes): `foo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1191`** (1 nodes): `cmplxdat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1192`** (1 nodes): `foo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1200`** (1 nodes): `=================== Universal Functions ===================  Ufuncs are, general`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1201`** (1 nodes): `DoxyLimbo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1204`** (1 nodes): `ISO_FORTRAN_ENV maps for f2py2e`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1207`** (2 nodes): `blackman()`, `Return the Blackman window.      The Blackman window is a taper formed by using`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1208`** (2 nodes): `_compute_virtual_index()`, `Compute the floating point indexes of an array for the linear     interpolation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1209`** (2 nodes): `digitize()`, `Return the indices of the bins to which each value in input array belongs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1210`** (2 nodes): `extract()`, `Return the elements of an array that satisfy some condition.      This is equiva`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1211`** (2 nodes): `hamming()`, `Return the Hamming window.      The Hamming window is a taper formed by using a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1212`** (2 nodes): `hanning()`, `Return the Hanning window.      The Hanning window is a taper formed by using a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1213`** (2 nodes): `insert()`, `Insert values along the given axis before the given indices.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1214`** (2 nodes): `interp()`, `One-dimensional linear interpolation for monotonically increasing sample points.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1215`** (2 nodes): `place()`, `Change elements of an array based on conditional and input values.      Similar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1216`** (2 nodes): `Sort a complex array using the real part first, then the imaginary part.      Pa`, `_sort_complex()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1217`** (2 nodes): `r"""     Return the normalized sinc function.      The sinc function is equal to`, `sinc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1218`** (2 nodes): `_izip_fields_flat()`, `Returns an iterator of concatenated fields from a sequence of arrays,     collap`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1219`** (2 nodes): `_izip_fields()`, `Returns an iterator of concatenated fields from a sequence of arrays.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1220`** (2 nodes): `Rename the fields from a flexible-datatype ndarray or recarray.      Nested fiel`, `rename_fields()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1221`** (2 nodes): `Re-pack the fields of a structured array or dtype in memory.      The memory lay`, `repack_fields()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1222`** (1 nodes): `Build an example package using the limited Python C API.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1226`** (2 nodes): `_n_to_n_data_clone()`, `_n_to_n_data_free()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1227`** (2 nodes): `NPY_cast_info_init()`, `NPY_context_init()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1228`** (2 nodes): `_one_to_n_data_clone()`, `_one_to_n_data_free()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1229`** (2 nodes): `_subarray_broadcast_data_clone()`, `_subarray_broadcast_data_free()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1230`** (2 nodes): `datetime_common_dtype()`, `default_builtin_common_dtype()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1231`** (2 nodes): `PyArray_GETITEM()`, `PyDataType_GetArrFuncs()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1232`** (2 nodes): `any_array_ufunc_overrides()`, `array_ufunc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1233`** (2 nodes): `array_byteswap()`, `PyArray_Byteswap()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1234`** (2 nodes): `array_deepcopy()`, `_deepcopy_call()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1235`** (2 nodes): `array_reduce()`, `_getlist_pkl()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1236`** (2 nodes): `array_setstate()`, `_setlist_pkl()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1237`** (2 nodes): `array_tofile()`, `PyArray_ToFileObject()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1238`** (2 nodes): `array__get_ndarray_c_version()`, `PyArray_GetNDArrayCVersion()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1239`** (2 nodes): `array_where()`, `PyArray_Where()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1240`** (2 nodes): `PyArray_ScalarKind()`, `_signbit_set()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1246`** (1 nodes): `Distributor init file  Distributors: you can add custom code here to support par`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1248`** (1 nodes): `Dict of expired attributes that are discontinued since 2.0 release. Each item is`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1251`** (1 nodes): `Test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1252`** (1 nodes): `Tests for :mod:`numpy._core.fromnumeric`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1253`** (1 nodes): `Based on the `if __name__ == "__main__"` test code in `lib/_user_array_impl.py`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1255`** (1 nodes): `# NOTE: __call__ is needed due to python/mypy#17620`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1256`** (1 nodes): `# NOTE: `np.generic` subclasses are not guaranteed to support addition;`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1261`** (2 nodes): `KnownFailureException`, `Raise this exception to mark a test as a known failing test.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1262`** (2 nodes): `_no_tracing()`, `Decorator to temporarily turn off tracing for the duration of a test.     Needed`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1263`** (2 nodes): `print_assert_equal()`, `Test if two objects are equal, and print an error message if test fails.      Th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1264`** (2 nodes): `Run doctests found in the given file.      By default `rundocs` raises an Assert`, `rundocs()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1265`** (2 nodes): `Context manager to provide a temporary test folder.      All arguments are passe`, `tempdir()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1266`** (2 nodes): `Context manager for temporary files.      Context manager that returns the path`, `temppath()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1267`** (2 nodes): `Decorator to skip a test if not enough memory is available`, `requires_memory()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1268`** (2 nodes): `Runs a function many times in parallel`, `run_threaded()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1269`** (2 nodes): `Decorator to skip test if deep recursion is not supported.`, `requires_deep_recursion()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1270`** (2 nodes): `Run ``cmd`` in a subprocess, failing the test with its captured output     if it`, `run_subprocess()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1271`** (1 nodes): `This hook should collect all binary files and any hidden modules that numpy need`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1287`** (1 nodes): `string_test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1289`** (1 nodes): `Test det function with non-container`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1290`** (1 nodes): `Test det function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1291`** (1 nodes): `Test det function with wrong size`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1292`** (1 nodes): `Test floor function with non-array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1293`** (1 nodes): `Test floor function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1294`** (1 nodes): `Test floor function with wrong type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1295`** (1 nodes): `Test luSplit function`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1296`** (1 nodes): `Test max function with bad list`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1297`** (1 nodes): `Test max function with non-container`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1298`** (1 nodes): `Test max function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1299`** (1 nodes): `Test min function with bad list`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1300`** (1 nodes): `Test min function with non-container`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1301`** (1 nodes): `Test min function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1302`** (1 nodes): `Test scale function with non-array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1303`** (1 nodes): `Test scale function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1304`** (1 nodes): `Test scale function with wrong size`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1305`** (1 nodes): `Test scale function with wrong type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1306`** (1 nodes): `Test scale function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1307`** (1 nodes): `Test scale function with wrong size`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1308`** (1 nodes): `Test scale function with non-array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1309`** (1 nodes): `Test floor function with non-array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1310`** (1 nodes): `Test ceil function with wrong type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1311`** (1 nodes): `Test ceil function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1312`** (1 nodes): `Test ceil function with non-array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1313`** (1 nodes): `Test luSplit function`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1314`** (1 nodes): `Test norm function with bad list`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1315`** (1 nodes): `Test norm function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1316`** (1 nodes): `Test norm function with wrong size`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1317`** (1 nodes): `Test norm function with non-container`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1318`** (1 nodes): `Test max function with bad list`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1319`** (1 nodes): `Test max function with non-container`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1320`** (1 nodes): `Test max function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1321`** (1 nodes): `Test scale function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1322`** (1 nodes): `Test scale function with wrong size`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1323`** (1 nodes): `Test scale function with non-array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1324`** (1 nodes): `Test floor function with non-array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1325`** (1 nodes): `Test ceil function with wrong type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1326`** (1 nodes): `Test ceil function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1327`** (1 nodes): `Test ceil function with non-array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1328`** (1 nodes): `Test luSplit function`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1329`** (1 nodes): `Test norm function with bad list`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1330`** (1 nodes): `Test norm function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1331`** (1 nodes): `Test norm function with wrong size`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1332`** (1 nodes): `Test norm function with non-container`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1333`** (1 nodes): `Test max function with bad list`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1334`** (1 nodes): `Test max function with non-container`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1335`** (1 nodes): `Test max function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1336`** (1 nodes): `Test reverse function with wrong size`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1337`** (1 nodes): `Test reverse function with wrong type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1338`** (1 nodes): `Test reverse function with non-array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1339`** (1 nodes): `Test ones function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1340`** (1 nodes): `Test ones function with wrong type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1341`** (1 nodes): `Test ones function with non-array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1342`** (1 nodes): `Test zeros function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1343`** (1 nodes): `Test zeros function with wrong type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1344`** (1 nodes): `Test zeros function with non-array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1345`** (1 nodes): `Test eoSplit function`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1346`** (1 nodes): `Test twos function with non-integer dimension`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1347`** (1 nodes): `Test threes function with non-integer dimension`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1348`** (1 nodes): `Test length function with bad list`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1349`** (1 nodes): `Test length function with wrong size`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1350`** (1 nodes): `Test length function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1351`** (1 nodes): `Test length function with non-container`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1352`** (1 nodes): `Test prod function with bad list`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1353`** (1 nodes): `Test prod function with wrong dimensions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1354`** (1 nodes): `Test prod function with non-container`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1355`** (1 nodes): `Test sum function with bad list`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1356`** (1 nodes): `A crude *bit of everything* smoke test to verify PyInstaller compatibility.  PyI`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1358`** (1 nodes): `there was an issue where         repr(array([0], dtype='<u2')) and repr(array([0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1360`** (1 nodes): `TestLowerF2PYDirective`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1361`** (1 nodes): `TestModuleDeclaration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1362`** (1 nodes): `Verify that datetime dtype __setstate__ can handle bad arguments`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1363`** (1 nodes): `check isfinite, isinf, isnan for all units of <M, >M, <m, >m dtypes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1364`** (1 nodes): `Dates should have symmetric limits around the unix epoch at +/-np.int64`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1365`** (1 nodes): `Limits should roundtrip when converted to strings.          This tests the conve`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1366`** (1 nodes): `Test the calendar conversion at Neri-Schneider algorithm boundaries         and`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1367`** (2 nodes): `gh22819_cli()`, `F90 file for testing disallowed CLI arguments in ghff819`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1368`** (2 nodes): `gh23598_warn()`, `F90 file for testing warnings in gh23598`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1369`** (2 nodes): `CLI :: -c -L/path/to/lib/ -l<libname>`, `test_npd_lib()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1370`** (2 nodes): `CLI :: -I/path/to/include/`, `test_npd_incl()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1371`** (2 nodes): `CLI :: <filename>.o <filename>.so <filename>.a`, `test_npd_linker()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1372`** (2 nodes): `Check that module names are handled correctly     gh-22819     Essentially, the`, `test_gh22819_cli()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1373`** (2 nodes): `Only one .pyf file allowed     gh-22819     CLI :: .pyf files`, `test_gh22819_many_pyf()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1374`** (2 nodes): `Ensures that a signature file is generated via the CLI     CLI :: -h`, `test_gen_pyf()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1375`** (2 nodes): `Ensures that a signature file can be dumped to stdout     CLI :: -h`, `test_gen_pyf_stdout()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1376`** (2 nodes): `Ensures that the CLI refuses to overwrite signature files     CLI :: -h without`, `test_gen_pyf_no_overwrite()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1377`** (2 nodes): `Ensures that the build directory can be specified      CLI :: --build-dir`, `test_build_dir()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1378`** (2 nodes): `Ensures that the build directory can be specified      CLI :: --overwrite-signat`, `test_overwrite()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1379`** (2 nodes): `Ensures that TeX documentation is written out      CLI :: --latex-doc`, `test_latexdoc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1380`** (2 nodes): `Ensures that TeX documentation is written out      CLI :: --no-latex-doc`, `test_nolatexdoc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1381`** (2 nodes): `Ensures that truncated documentation is written out      TODO: Test to ensure th`, `test_shortlatex()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1382`** (2 nodes): `Ensures that RsT documentation is written out      CLI :: --rest-doc`, `test_restdoc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1383`** (2 nodes): `Ensures that TeX documentation is written out      CLI :: --no-rest-doc`, `test_norestexdoc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1384`** (2 nodes): `Ensures that debugging wrappers are written      CLI :: --debug-capi`, `test_debugcapi()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1385`** (2 nodes): `Ensures that debugging wrappers work      CLI :: --debug-capi -c`, `test_debugcapi_bld()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1386`** (2 nodes): `Ensures that fortran subroutine wrappers for F77 are included by default      CL`, `test_wrapfunc_def()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1387`** (2 nodes): `Ensures that fortran subroutine wrappers for F77 can be disabled      CLI :: --n`, `test_nowrapfunc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1388`** (2 nodes): `Add to the include directories      CLI :: -include     TODO: Document this in t`, `test_inclheader()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1389`** (2 nodes): `Add to the include directories      CLI :: --include-paths`, `test_inclpath()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1390`** (2 nodes): `Add to the include directories      CLI :: --help-link`, `test_hlink()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1391`** (2 nodes): `Check that Fortran-to-Python KIND specs can be passed      CLI :: --f2cmap`, `test_f2cmap()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1392`** (2 nodes): `Reduce verbosity      CLI :: --quiet`, `test_quiet()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1393`** (2 nodes): `Increase verbosity      CLI :: --verbose`, `test_verbose()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1394`** (2 nodes): `Ensure version      CLI :: -v`, `test_version()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1395`** (2 nodes): `CLI :: -c --fcompiler`, `test_npd_fcompiler()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1396`** (2 nodes): `CLI :: -c --help-fcompiler`, `test_npd_help_fcompiler()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1397`** (2 nodes): `CLI :: -c --link-<resource>`, `test_npd_link_auto()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1399`** (1 nodes): `A bundle of arguments to be passed to a test case, with an identifying         n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1400`** (2 nodes): `Byte control characters (comments, delimiter) are supported.`, `test_control_characters_as_bytes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1401`** (2 nodes): `skiprows and max_rows should raise for negative parameters.`, `test_exception_negative_row_limits()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1402`** (2 nodes): `Test that both 'e' and 'E' are parsed correctly.`, `test_scientific_notation()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1403`** (2 nodes): `With the 'bytes' encoding, tokens are encoded prior to being     passed to the c`, `test_converter_with_unicode_dtype()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1404`** (2 nodes): `The given dtype is just 'S' or 'U' with no length. In these cases, the     lengt`, `test_string_no_length_given()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1405`** (2 nodes): `Some tests that the conversion to float64 works as accurately as the     Python`, `test_float_conversion()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1406`** (2 nodes): `Test exception when a character cannot be encoded as 'S'.`, `test_character_not_bytes_compatible()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1407`** (2 nodes): `Support for quoted fields is disabled by default.`, `test_quote_support_default()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1408`** (2 nodes): `Check that a UserWarning is emitted when no data is read from input.`, `test_warn_on_no_data()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1409`** (2 nodes): `Check that the correct unit (e.g. month, day, second) is discovered from     the`, `test_parametric_unit_discovery()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1410`** (2 nodes): `iter_iterindices()`, `test_iter_iterindex()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1411`** (2 nodes): `Tests the strides with the contig flag for both broadcast and non-broadcast`, `test_iter_contig_flag_single_operand_strides()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1412`** (2 nodes): `using a context amanger and using nditer.close are equivalent`, `test_close_equivalent()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1413`** (2 nodes): `Checks for reference counting leaks during cleanup.  Using explicit     referenc`, `test_partial_iteration_cleanup()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1414`** (2 nodes): `Matches the expected output of a debug print with the actual output.     Note th`, `test_debug_print()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1415`** (1 nodes): `Verify fromrecords works with a 0-length input`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1416`** (1 nodes): `Test that nested structured types are treated as records too`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1417`** (1 nodes): `test that trailing padding is preserved`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1418`** (2 nodes): `Test as_strided with check_bounds=True with different dtypes.`, `test_as_strided_checked_different_dtypes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1419`** (2 nodes): `Test 1D arrays with positive strides.`, `test_as_strided_checked_1d_positive_strides()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1420`** (2 nodes): `Test sliding window views in 1D.`, `test_as_strided_checked_sliding_window_1d()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1421`** (2 nodes): `Test 2D arrays with default strides.`, `test_as_strided_checked_2d_default_strides()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1422`** (2 nodes): `Test zero strides (broadcasting a single value).`, `test_as_strided_checked_zero_stride_broadcasting()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1423`** (2 nodes): `Test that out-of-bounds positive strides raise ValueError.`, `test_as_strided_checked_out_of_bounds_positive_strides()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1424`** (2 nodes): `Test as_strided      - with check_bounds=True     - considers the base array bou`, `test_as_strided_checked_view_of_larger_array()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1425`** (2 nodes): `Test as_strided      - with check_bounds=True     - on a view that doesn't start`, `test_as_strided_checked_view_with_offset()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1426`** (2 nodes): `Test that negative strides on a view correctly detect out of bounds.`, `test_as_strided_checked_view_out_of_bounds_negative()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1427`** (2 nodes): `Test that positive strides on a view correctly detect out of bounds.`, `test_as_strided_checked_view_out_of_bounds_positive()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1428`** (2 nodes): `Test as_strided with check_bounds=True on a view of a view.`, `test_as_strided_checked_nested_views()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1429`** (2 nodes): `Test various slicing scenarios.`, `test_as_strided_checked_sliced_array()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1430`** (2 nodes): `Parametrized test for various view and stride combinations.`, `test_as_strided_checked_view_parametrized()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1431`** (1 nodes): `Test generalized ufunc with zero-sized operands`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1432`** (1 nodes): `Test with fixed-sized signature.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1433`** (1 nodes): `The type of the result should always depend on the selected loop, not         ne`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1434`** (1 nodes): `Try to check presence and results of all ufuncs.          The list of ufuncs com`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1435`** (1 nodes): `Basic test for the safest casts, because ufuncs inner loops can         indicate`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1436`** (1 nodes): `Check that (x†A)x equals x†(Ax).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1439`** (1 nodes): `A module with the precisions of platform-specific `~numpy.number`s.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 1440`** (1 nodes): `# NOTE: `_StrLike_co` and `_BytesLike_co` are pointless, as `np.str_` and`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AxisError` connect `Community 10` to `Community 13`, `Community 399`, `Community 118`, `Community 190`, `Community 9`, `Community 260`, `Community 32`, `Community 81`, `Community 30`, `Community 168`, `Community 3`, `Community 262`, `Community 44`, `Community 119`, `Community 192`, `Community 93`, `Community 363`, `Community 8`, `Community 268`, `Community 597`, `Community 697`, `Community 698`, `Community 813`, `Community 752`, `Community 814`, `Community 39`, `Community 173`, `Community 60`, `Community 1399`, `Community 600`, `Community 138`, `Community 925`, `Community 702`, `Community 703`, `Community 2`, `Community 236`, `Community 174`, `Community 74`, `Community 202`, `Community 97`, `Community 494`, `Community 108`, `Community 705`, `Community 211`, `Community 520`, `Community 139`, `Community 653`, `Community 140`, `Community 706`, `Community 103`, `Community 210`, `Community 24`, `Community 495`, `Community 301`, `Community 604`, `Community 448`, `Community 340`, `Community 75`, `Community 449`, `Community 341`, `Community 61`, `Community 708`, `Community 45`, `Community 606`, `Community 218`, `Community 521`, `Community 817`, `Community 420`, `Community 522`, `Community 818`, `Community 227`, `Community 709`, `Community 126`, `Community 607`, `Community 656`, `Community 753`, `Community 0`, `Community 305`, `Community 452`, `Community 345`, `Community 424`, `Community 453`, `Community 288`, `Community 425`, `Community 765`, `Community 369`, `Community 371`, `Community 1431`, `Community 1432`, `Community 1433`, `Community 1434`, `Community 251`, `Community 1435`, `Community 1436`, `Community 767`, `Community 454`, `Community 4`, `Community 830`, `Community 831`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Why does `MaskedArray` connect `Community 17` to `Community 1`, `Community 179`, `Community 384`, `Community 9`, `Community 19`, `Community 260`, `Community 32`, `Community 81`, `Community 30`, `Community 168`, `Community 18`, `Community 596`, `Community 232`, `Community 48`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Why does `memmap` connect `Community 89` to `Community 17`, `Community 235`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
- **Are the 414 inferred relationships involving `AxisError` (e.g. with `Return an array of zeros with the same shape and type as a given array.      Par` and `Roll array elements along a given axis.      Elements that roll beyond the last`) actually correct?**
  _`AxisError` has 414 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `TestRegression` (e.g. with `AxisError` and `ComplexWarning`) actually correct?**
  _`TestRegression` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 178 inferred relationships involving `ABCPolyBase` (e.g. with `Chebyshev` and `==================================================== Chebyshev Series (:mod:`num`) actually correct?**
  _`ABCPolyBase` has 178 INFERRED edges - model-reasoned connections that need verification._
- **Are the 107 inferred relationships involving `MaskedArray` (e.g. with `MAxisConcatenator` and `mr_class`) actually correct?**
  _`MaskedArray` has 107 INFERRED edges - model-reasoned connections that need verification._