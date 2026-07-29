# Graph Report - .  (2026-07-29)

## Corpus Check
- cluster-only mode - file stats not available

## Summary
- 1305 nodes · 5564 edges · 118 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output
- Edge kinds: calls: 4227 · contains: 1202 · imports: 86 · imports_from: 29 · rationale_for: 18 · inherits: 1 · method: 1


## Graph Freshness
- Built from Git commit: `a9ff1b4`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `__Pyx_AddTraceback()` - 761 edges
2. `__Pyx_ParseKeywords()` - 369 edges
3. `__Pyx_RaiseArgtupleInvalid()` - 366 edges
4. `__pyx_f_5talib_7_ta_lib__ta_check_success()` - 346 edges
5. `__pyx_f_5talib_7_ta_lib_check_array()` - 326 edges
6. `__pyx_f_5numpy_7ndarray_4data_data()` - 325 edges
7. `__Pyx_PyLong_As_int()` - 137 edges
8. `__pyx_f_5talib_7_ta_lib_check_length4()` - 136 edges
9. `__pyx_f_5numpy_7ndarray_5shape_shape()` - 128 edges
10. `__pyx_f_5talib_7_ta_lib_make_double_array()` - 99 edges

## Surprising Connections (you probably didn't know these)
- `__Pyx_AddTraceback()` --calls--> `__Pyx_CLineForTraceback()`  [EXTRACTED]
  talib/_ta_lib.c → talib/_ta_lib.c  _Bridges community 1 → community 12_
- `__Pyx_CallUnboundCMethod0()` --calls--> `__Pyx_PyObject_CallOneArg()`  [EXTRACTED]
  talib/_ta_lib.c → talib/_ta_lib.c  _Bridges community 22 → community 15_
- `__Pyx_CyFunction_CallAsMethod()` --calls--> `__Pyx_PyVectorcall_FastCallDict()`  [EXTRACTED]
  talib/_ta_lib.c → talib/_ta_lib.c  _Bridges community 30 → community 22_
- `__Pyx_CyFunction_get_annotations()` --calls--> `__Pyx_NewRef()`  [EXTRACTED]
  talib/_ta_lib.c → talib/_ta_lib.c  _Bridges community 12 → community 14_
- `__Pyx_CyFunction_get_annotations()` --calls--> `__Pyx_PyObject_CallOneArg()`  [EXTRACTED]
  talib/_ta_lib.c → talib/_ta_lib.c  _Bridges community 12 → community 15_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.02
Nodes (34): arrayobject, arrayscalars, atomic, compile, complex, cstdlib, frameobject, intrin (+26 more)

### Community 1 - "Community 1"
Cohesion: 0.03
Nodes (91): __Pyx_AddTraceback(), __Pyx_CreateCodeObjectForTraceback(), __pyx_f_5numpy_PyArray_MultiIterNew1(), __pyx_f_5numpy_PyArray_MultiIterNew2(), __pyx_f_5numpy_PyArray_MultiIterNew3(), __pyx_f_5numpy_PyArray_MultiIterNew4(), __pyx_f_5numpy_PyArray_MultiIterNew5(), __pyx_f_5numpy_set_array_base() (+83 more)

### Community 2 - "Community 2"
Cohesion: 0.03
Nodes (84): __pyx_f_5numpy_7ndarray_4data_data(), __pyx_pf_5talib_7_ta_lib_12_ta_get_compatibility(), __pyx_pf_5talib_7_ta_lib_140CDLMORNINGDOJISTAR(), __pyx_pf_5talib_7_ta_lib_152CDLSEPARATINGLINES(), __pyx_pf_5talib_7_ta_lib_164CDLTAKURI(), __pyx_pf_5talib_7_ta_lib_176CDLXSIDEGAP3METHODS(), __pyx_pf_5talib_7_ta_lib_402stream_CDL2CROWS(), __pyx_pf_5talib_7_ta_lib_404stream_CDL3BLACKCROWS() (+76 more)

### Community 3 - "Community 3"
Cohesion: 0.04
Nodes (80): __pyx_f_5talib_7_ta_lib_check_begidx4(), __pyx_f_5talib_7_ta_lib_make_int_array(), __pyx_pf_5talib_7_ta_lib_100CDLGRAVESTONEDOJI(), __pyx_pf_5talib_7_ta_lib_102CDLHAMMER(), __pyx_pf_5talib_7_ta_lib_104CDLHANGINGMAN(), __pyx_pf_5talib_7_ta_lib_106CDLHARAMI(), __pyx_pf_5talib_7_ta_lib_108CDLHARAMICROSS(), __pyx_pf_5talib_7_ta_lib_110CDLHIGHWAVE() (+72 more)

### Community 4 - "Community 4"
Cohesion: 0.04
Nodes (79): __Pyx_ParseKeywordDict(), __Pyx_ParseKeywordDictToDict(), __Pyx_ParseKeywords(), __pyx_pf_5talib_7_ta_lib_292SIN(), __pyx_pf_5talib_7_ta_lib_306STOCHRSI(), __pyx_pf_5talib_7_ta_lib_310SUM(), __pyx_pf_5talib_7_ta_lib_322TRIMA(), __pyx_pf_5talib_7_ta_lib_324TRIX() (+71 more)

### Community 5 - "Community 5"
Cohesion: 0.04
Nodes (72): __pyx_f_5talib_7_ta_lib_check_begidx1(), __pyx_f_5talib_7_ta_lib_make_double_array(), __pyx_pf_5talib_7_ta_lib_178CEIL(), __pyx_pf_5talib_7_ta_lib_180CMO(), __pyx_pf_5talib_7_ta_lib_184COS(), __pyx_pf_5talib_7_ta_lib_186COSH(), __pyx_pf_5talib_7_ta_lib_188DEMA(), __pyx_pf_5talib_7_ta_lib_194EMA() (+64 more)

### Community 6 - "Community 6"
Cohesion: 0.04
Nodes (45): __pyx_f_5numpy_7ndarray_5shape_shape(), __pyx_pf_5talib_7_ta_lib_220LINEARREG_INTERCEPT(), __pyx_pf_5talib_7_ta_lib_228MA(), __pyx_pf_5talib_7_ta_lib_236MAMA(), __pyx_pf_5talib_7_ta_lib_252MIN(), __pyx_pf_5talib_7_ta_lib_278ROC(), __pyx_pf_5talib_7_ta_lib_286RSI(), __pyx_pf_5talib_7_ta_lib_300STDDEV() (+37 more)

### Community 7 - "Community 7"
Cohesion: 0.06
Nodes (36): __Pyx_CalculateMetaclass(), __Pyx_call_type_traverse(), __Pyx_check_binary_version(), __Pyx_CreateCodeObjects(), __Pyx_CyFunction_SetDefaultsTuple(), __Pyx_CyFunction_traverse(), __Pyx_CyOrPyCFunction_GET_SELF(), __Pyx_DecompressString() (+28 more)

### Community 8 - "Community 8"
Cohesion: 0.06
Nodes (33): __pyx_f_5talib_7_ta_lib_check_length4(), __pyx_pf_5talib_7_ta_lib_136CDLMATCHINGLOW(), __pyx_pf_5talib_7_ta_lib_148CDLRICKSHAWMAN(), __pyx_pf_5talib_7_ta_lib_160CDLSTALLEDPATTERN(), __pyx_pf_5talib_7_ta_lib_172CDLUNIQUE3RIVER(), __pyx_pf_5talib_7_ta_lib_368stream_AD(), __pyx_pf_5talib_7_ta_lib_390stream_AVGPRICE(), __pyx_pf_5talib_7_ta_lib_440stream_CDLEVENINGDOJISTAR() (+25 more)

### Community 9 - "Community 9"
Cohesion: 0.06
Nodes (33): __pyx_f_5talib_7_ta_lib__ta_check_success(), __pyx_f_5talib_7_ta_lib___ta_getLookback(), __pyx_f_5talib_7_ta_lib___ta_paramHolderFree(), __pyx_f_5talib_7_ta_lib___ta_setOptInputParamInteger(), __pyx_f_5talib_7_ta_lib___ta_setOptInputParamReal(), __pyx_pf_5talib_7_ta_lib_142CDLMORNINGSTAR(), __pyx_pf_5talib_7_ta_lib_154CDLSHOOTINGSTAR(), __pyx_pf_5talib_7_ta_lib_166CDLTASUKIGAP() (+25 more)

### Community 10 - "Community 10"
Cohesion: 0.06
Nodes (32): __pyx_f_5numpy_7ndarray_4ndim_ndim(), __pyx_f_5talib_7_ta_lib_check_array(), __pyx_pf_5talib_7_ta_lib_132CDLLONGLINE(), __pyx_pf_5talib_7_ta_lib_144CDLONNECK(), __pyx_pf_5talib_7_ta_lib_156CDLSHORTLINE(), __pyx_pf_5talib_7_ta_lib_168CDLTHRUSTING(), __pyx_pf_5talib_7_ta_lib_246MFI(), __pyx_pf_5talib_7_ta_lib_398stream_BOP() (+24 more)

### Community 11 - "Community 11"
Cohesion: 0.09
Nodes (8): collections, copy, ordereddict, assert_array_not_equal(), test_SMA(), test_STOCH(), threading, time

### Community 12 - "Community 12"
Cohesion: 0.08
Nodes (26): __Pyx_CLineForTraceback(), __pyx_CommonTypesMetaclass_init(), __Pyx_CyFunction_get_annotate(), __Pyx_CyFunction_get_annotate_from_dict_if_exists(), __Pyx_CyFunction_get_annotations(), __Pyx_CyFunction_get_annotations_locked(), __Pyx_CyFunction_get_dict_if_exists(), __Pyx_CyFunction_Init() (+18 more)

### Community 13 - "Community 13"
Cohesion: 0.12
Nodes (24): __pyx_f_5talib_7_ta_lib___ta_getFuncHandle(), __pyx_f_5talib_7_ta_lib___ta_paramHolderAlloc(), __pyx_pf_5talib_7_ta_lib_354_ta_getFuncInfo(), __pyx_pf_5talib_7_ta_lib_356_ta_getInputParameterInfo(), __pyx_pf_5talib_7_ta_lib_358_ta_getOptInputParameterInfo(), __pyx_pf_5talib_7_ta_lib_360_ta_getOutputParameterInfo(), __pyx_pf_5talib_7_ta_lib_8Function_24lookback(), __pyx_pw_5talib_7_ta_lib_353__get_flags() (+16 more)

### Community 14 - "Community 14"
Cohesion: 0.13
Nodes (23): __Pyx_CyFunction_get_is_coroutine(), __Pyx_CyFunction_get_is_coroutine_value(), __Pyx__CyFunction_SetClassObj(), __Pyx_NewRef(), __Pyx_Owned_Py_None(), __pyx_pf_5talib_7_ta_lib_14_ta_set_candle_settings(), __pyx_pf_5talib_7_ta_lib_6_ta_set_unstable_period(), __pyx_pf_5talib_7_ta_lib_8_ta_get_unstable_period() (+15 more)

### Community 15 - "Community 15"
Cohesion: 0.11
Nodes (21): __Pyx__ArgTypeTest(), __Pyx_dict_iterator(), __Pyx_GetBuiltinName(), __Pyx_HasAttr(), __Pyx_InitCachedBuiltins(), __Pyx_PEP560_update_bases(), __Pyx_PyBuiltin_Invalid(), __Pyx_PyDict_GetItemStr() (+13 more)

### Community 16 - "Community 16"
Cohesion: 0.12
Nodes (15): cython_distutils, os, os_path, re, setuptools, setuptools_command_build_ext, sys, # FIXME: initialize once, then shutdown at the end, rather than each call? (+7 more)

### Community 17 - "Community 17"
Cohesion: 0.13
Nodes (18): bs4, generate_groups_markdown(), get_doc_links(), get_groups_markdown(), get_markdown_file_paths(), _get_markdown_renderer(), USAGE:  To convert markdown docs into html docs: $ python generate_html_pages.py, Generate and save markdown files for function group documentation (+10 more)

### Community 18 - "Community 18"
Cohesion: 0.13
Nodes (4): numpy, numpy_testing, pandas, talib

### Community 20 - "Community 20"
Cohesion: 0.18
Nodes (17): __pyx_pf_5talib_7_ta_lib_362_get_defaults_and_docs(), __pyx_pf_5talib_7_ta_lib_7MA_Type_2__getitem__(), __pyx_pf_5talib_7_ta_lib_8Function_10get_input_names(), __pyx_pf_5talib_7_ta_lib_8Function_16set_input_arrays(), __pyx_pf_5talib_7_ta_lib_8Function_34__input_price_series_names(), __pyx_pf_5talib_7_ta_lib_8Function_38__check_opt_input_value(), __pyx_pf_5talib_7_ta_lib_8Function_40__get_opt_input_value(), __pyx_pw_5talib_7_ta_lib_7MA_Type_3__getitem__() (+9 more)

### Community 21 - "Community 21"
Cohesion: 0.21
Nodes (17): __pyx_pf_5talib_7_ta_lib_7MA_Type___init__(), __pyx_pf_5talib_7_ta_lib_8Function_14get_input_arrays(), __pyx_pf_5talib_7_ta_lib_8Function_18get_parameters(), __pyx_pf_5talib_7_ta_lib_8Function_26output_names(), __pyx_pf_5talib_7_ta_lib_8Function_28outputs(), __pyx_pf_5talib_7_ta_lib_8Function_2__local(), __pyx_pf_5talib_7_ta_lib_8Function_30run(), __pyx_pf_5talib_7_ta_lib_8Function_36__call_function() (+9 more)

### Community 22 - "Community 22"
Cohesion: 0.16
Nodes (15): __pyx_atomic_int_cmp_exchange(), __pyx_bisect_code_objects(), __Pyx_CachedCFunction_GetAndSetInitializing(), __Pyx_CachedCFunction_SetFinishedInitializing(), __Pyx_CallUnboundCMethod0(), __Pyx_CallUnboundCMethod2(), __pyx__find_code_object(), __pyx__insert_code_object() (+7 more)

### Community 23 - "Community 23"
Cohesion: 0.26
Nodes (15): __Pyx_dict_iter_next(), __Pyx_dict_iter_next_source_is_dict(), __Pyx_IterFinish(), __Pyx_IternextUnpackEndCheck(), __pyx_pf_5talib_7_ta_lib_8Function_12set_input_names(), __pyx_pf_5talib_7_ta_lib_8Function_20set_parameters(), __pyx_pf_5talib_7_ta_lib_8Function_32__call__(), __pyx_pw_5talib_7_ta_lib_8Function_13set_input_names() (+7 more)

### Community 24 - "Community 24"
Cohesion: 0.13
Nodes (15): __pyx_f_5talib_7_ta_lib_check_length2(), __pyx_pf_5talib_7_ta_lib_238MAVP(), __pyx_pf_5talib_7_ta_lib_370stream_ADD(), __pyx_pf_5talib_7_ta_lib_380stream_AROON(), __pyx_pf_5talib_7_ta_lib_382stream_AROONOSC(), __pyx_pf_5talib_7_ta_lib_396stream_BETA(), __pyx_pf_5talib_7_ta_lib_636stream_SAREXT(), __pyx_pf_5talib_7_ta_lib_654stream_SUB() (+7 more)

### Community 25 - "Community 25"
Cohesion: 0.13
Nodes (15): __pyx_f_5talib_7_ta_lib_check_length3(), __pyx_pf_5talib_7_ta_lib_268NATR(), __pyx_pf_5talib_7_ta_lib_364stream_ACCBANDS(), __pyx_pf_5talib_7_ta_lib_374stream_ADX(), __pyx_pf_5talib_7_ta_lib_376stream_ADXR(), __pyx_pf_5talib_7_ta_lib_388stream_ATR(), __pyx_pf_5talib_7_ta_lib_676stream_ULTOSC(), __pyx_pf_5talib_7_ta_lib_682stream_WILLR() (+7 more)

### Community 26 - "Community 26"
Cohesion: 0.15
Nodes (13): __pyx_f_5talib_7_ta_lib_check_begidx2(), __pyx_pf_5talib_7_ta_lib_182CORREL(), __pyx_pf_5talib_7_ta_lib_190DIV(), __pyx_pf_5talib_7_ta_lib_212IMI(), __pyx_pf_5talib_7_ta_lib_244MEDPRICE(), __pyx_pf_5talib_7_ta_lib_36AROONOSC(), __pyx_pf_5talib_7_ta_lib_50BETA(), __pyx_pw_5talib_7_ta_lib_183CORREL() (+5 more)

### Community 27 - "Community 27"
Cohesion: 0.15
Nodes (13): __pyx_f_5talib_7_ta_lib_check_begidx3(), __pyx_pf_5talib_7_ta_lib_18ACCBANDS(), __pyx_pf_5talib_7_ta_lib_192DX(), __pyx_pf_5talib_7_ta_lib_260MINUS_DI(), __pyx_pf_5talib_7_ta_lib_272PLUS_DI(), __pyx_pf_5talib_7_ta_lib_42ATR(), __pyx_pf_5talib_7_ta_lib_54CCI(), __pyx_pw_5talib_7_ta_lib_193DX() (+5 more)

### Community 28 - "Community 28"
Cohesion: 0.18
Nodes (13): __Pyx_Fallback___Pyx_PyLong_AddObjC(), __Pyx_Float___Pyx_PyLong_AddObjC(), __Pyx_GetKwValue_FASTCALL(), __pyx_pf_5talib_7_ta_lib_352__get_flags(), __pyx_pf_5talib_7_ta_lib_8Function_22set_function_args(), __pyx_pw_5talib_7_ta_lib_8Function_23set_function_args(), __Pyx_PyBytes_Equals(), __Pyx_PyDict_GetItem() (+5 more)

### Community 29 - "Community 29"
Cohesion: 0.17
Nodes (9): atexit, functools, itertools, polars, ta_lib, get_function_groups(), get_functions(), Returns a list of all the functions supported by TALIB (+1 more)

### Community 30 - "Community 30"
Cohesion: 0.23
Nodes (12): __Pyx_CyFunction_Call(), __Pyx_CyFunction_CallAsMethod(), __Pyx_CyFunction_CallMethod(), __Pyx_CyFunction_get_name(), __Pyx_CyFunction_get_name_locked(), __Pyx_CyFunction_raise_argument_count_error(), __Pyx_CyFunction_raise_type_error(), __Pyx_CyFunction_Vectorcall_CheckArgs() (+4 more)

### Community 31 - "Community 31"
Cohesion: 0.22
Nodes (10): __Pyx_copy_object_array(), __Pyx_crop_slice(), __Pyx__Import(), __Pyx__Import_GetModule(), __Pyx__Import_Lookup(), __Pyx_PyList_FromArray(), __Pyx_PyList_GetSlice(), __Pyx_PyList_GetSlice_locked() (+2 more)

### Community 32 - "Community 32"
Cohesion: 0.24
Nodes (10): __Pyx_GetItemInt_Fast(), __Pyx_GetItemInt_Generic(), __Pyx_GetItemInt_List_Fast(), __Pyx_GetItemInt_Tuple_Fast(), __Pyx_is_valid_index(), __Pyx_PyIndex_AsHash_t(), __Pyx_PyIndex_AsSsize_t(), __Pyx_PyObject_GetIndex() (+2 more)

### Community 33 - "Community 33"
Cohesion: 0.39
Nodes (7): inspect, clean_doc(), generate_function(), main(), output_type(), parse_signature(), Return a comma-separated function signature for the given TA-Lib abstract functi

### Community 34 - "Community 34"
Cohesion: 0.29
Nodes (8): __pyx_m_clear(), __Pyx_ModuleStateLookup_wait_until_no_readers(), __Pyx_State_AddModule(), __Pyx_State_AddModuleInterpIdAsIndex(), __Pyx_State_ConvertFromInterpIdAsIndex(), __Pyx_State_FindModule(), __Pyx_State_FindModuleStateLookupTableLowerBound(), __Pyx_State_RemoveModule()

### Community 35 - "Community 35"
Cohesion: 0.38
Nodes (4): pylab, abstract_example(), func_example(), plot()

### Community 36 - "Community 36"
Cohesion: 0.33
Nodes (7): __Pyx_CheckUnicodeValue(), __Pyx_PyUnicode_BuildFromAscii(), __Pyx_PyUnicode_FromOrdinal_Padded(), __Pyx____Pyx_PyUnicode_From_Py_ssize_t(), __Pyx____Pyx_PyUnicode_From_TA_RetCode(), __Pyx_uchar___Pyx_PyUnicode_From_Py_ssize_t(), __Pyx_uchar___Pyx_PyUnicode_From_TA_RetCode()

### Community 37 - "Community 37"
Cohesion: 0.40
Nodes (6): __Pyx_InBases(), __Pyx_inner_PyErr_GivenExceptionMatches2(), __Pyx_IsAnySubtype2(), __Pyx_IsSubtype(), __Pyx_PyErr_GivenExceptionMatches2(), __Pyx_PyErr_GivenExceptionMatchesTuple()

### Community 38 - "Community 38"
Cohesion: 0.40
Nodes (6): __Pyx_MatchKeywordArg(), __Pyx_MatchKeywordArg_nostr(), __Pyx_MatchKeywordArg_str(), __Pyx_ParseKeywordsTuple(), __Pyx_RaiseDoubleKeywordsError(), __Pyx_UnicodeKeywordsEqual()

### Community 39 - "Community 39"
Cohesion: 0.40
Nodes (4): build_ext, NumpyBuildExt, Custom build_ext command that adds numpy's include_dir to extensions., Add numpy's include directory to Extension includes.

### Community 40 - "Community 40"
Cohesion: 0.40
Nodes (1): pytest

### Community 41 - "Community 41"
Cohesion: 0.40
Nodes (5): __Pyx_CyFunction_get_defaults(), __Pyx_CyFunction_get_defaults_locked(), __Pyx_CyFunction_get_kwdefaults(), __Pyx_CyFunction_get_kwdefaults_locked(), __Pyx_CyFunction_init_defaults()

### Community 42 - "Community 42"
Cohesion: 0.50
Nodes (4): __Pyx_check_single_interpreter(), __Pyx_copy_spec_to_module(), __Pyx_GetCurrentInterpreterId(), __pyx_pymod_create()

### Community 43 - "Community 43"
Cohesion: 0.67
Nodes (3): __Pyx_c_abs_double(), __Pyx_c_pow_double(), __Pyx_c_prod_double()

### Community 44 - "Community 44"
Cohesion: 0.67
Nodes (3): __Pyx_c_abs_float(), __Pyx_c_pow_float(), __Pyx_c_prod_float()

### Community 45 - "Community 45"
Cohesion: 0.67
Nodes (3): __Pyx_c_abs_long__double(), __Pyx_c_pow_long__double(), __Pyx_c_prod_long__double()

### Community 46 - "Community 46"
Cohesion: 0.67
Nodes (3): __Pyx_CyFunction_get_dict(), __Pyx_CyFunction_set_annotate(), __Pyx_CyFunction_set_annotate_in_dict()

### Community 47 - "Community 47"
Cohesion: 0.67
Nodes (3): __Pyx_GetTypeDict(), __Pyx_GetTypeDictOffset(), __Pyx__SetItemOnTypeDict()

### Community 48 - "Community 48"
Cohesion: 0.67
Nodes (3): __Pyx_PyByteArray_FromString(), __Pyx_PyUnicode_FromString(), __Pyx_ssize_strlen()

### Community 49 - "Community 49"
Cohesion: 0.67
Nodes (3): __Pyx_PyObject_AsString(), __Pyx_PyObject_AsStringAndSize(), __Pyx_PyUnicode_AsStringAndSize()

### Community 50 - "Community 50"
Cohesion: 1.00
Nodes (2): __Pyx_c_quot_double(), __pyx_t_double_complex_from_parts()

### Community 51 - "Community 51"
Cohesion: 1.00
Nodes (2): __Pyx_c_quot_float(), __pyx_t_float_complex_from_parts()

### Community 52 - "Community 52"
Cohesion: 1.00
Nodes (2): __Pyx_c_quot_long__double(), __pyx_t_long_double_complex_from_parts()

### Community 53 - "Community 53"
Cohesion: 1.00
Nodes (2): __Pyx_CyFunction_clear(), __Pyx__CyFunction_dealloc()

### Community 54 - "Community 54"
Cohesion: 1.00
Nodes (2): __Pyx_CyFunction_get_doc(), __Pyx_CyFunction_get_doc_locked()

### Community 55 - "Community 55"
Cohesion: 1.00
Nodes (2): __Pyx__ExceptionSave(), __Pyx_PyErr_GetTopmostException()

### Community 56 - "Community 56"
Cohesion: 1.00
Nodes (2): __pyx_f_5numpy_5dtype_8subarray_subarray(), __pyx_f_5numpy_PyDataType_SHAPE()

### Community 57 - "Community 57"
Cohesion: 1.00
Nodes (2): __Pyx_get_object_dict_version(), __Pyx_object_dict_version_matches()

### Community 58 - "Community 58"
Cohesion: 1.00
Nodes (2): __Pyx__IsSameCyOrCFunction(), __Pyx__IsSameCyOrCFunctionNoMethod()

### Community 59 - "Community 59"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_2_ta_initialize(), __pyx_pw_5talib_7_ta_lib_3_ta_initialize()

### Community 60 - "Community 60"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_24ADD(), __pyx_pw_5talib_7_ta_lib_25ADD()

### Community 61 - "Community 61"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_250MIDPRICE(), __pyx_pw_5talib_7_ta_lib_251MIDPRICE()

### Community 62 - "Community 62"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_262MINUS_DM(), __pyx_pw_5talib_7_ta_lib_263MINUS_DM()

### Community 63 - "Community 63"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_266MULT(), __pyx_pw_5talib_7_ta_lib_267MULT()

### Community 64 - "Community 64"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_270OBV(), __pyx_pw_5talib_7_ta_lib_271OBV()

### Community 65 - "Community 65"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_274PLUS_DM(), __pyx_pw_5talib_7_ta_lib_275PLUS_DM()

### Community 66 - "Community 66"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_288SAR(), __pyx_pw_5talib_7_ta_lib_289SAR()

### Community 67 - "Community 67"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_28ADX(), __pyx_pw_5talib_7_ta_lib_29ADX()

### Community 68 - "Community 68"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_290SAREXT(), __pyx_pw_5talib_7_ta_lib_291SAREXT()

### Community 69 - "Community 69"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_302STOCH(), __pyx_pw_5talib_7_ta_lib_303STOCH()

### Community 70 - "Community 70"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_304STOCHF(), __pyx_pw_5talib_7_ta_lib_305STOCHF()

### Community 71 - "Community 71"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_308SUB(), __pyx_pw_5talib_7_ta_lib_309SUB()

### Community 72 - "Community 72"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_30ADXR(), __pyx_pw_5talib_7_ta_lib_31ADXR()

### Community 73 - "Community 73"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_320TRANGE(), __pyx_pw_5talib_7_ta_lib_321TRANGE()

### Community 74 - "Community 74"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_328TYPPRICE(), __pyx_pw_5talib_7_ta_lib_329TYPPRICE()

### Community 75 - "Community 75"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_330ULTOSC(), __pyx_pw_5talib_7_ta_lib_331ULTOSC()

### Community 76 - "Community 76"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_334WCLPRICE(), __pyx_pw_5talib_7_ta_lib_335WCLPRICE()

### Community 77 - "Community 77"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_336WILLR(), __pyx_pw_5talib_7_ta_lib_337WILLR()

### Community 78 - "Community 78"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_344str2bytes(), __pyx_pw_5talib_7_ta_lib_345str2bytes()

### Community 79 - "Community 79"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_348_ta_getGroupTable(), __pyx_pw_5talib_7_ta_lib_349_ta_getGroupTable()

### Community 80 - "Community 80"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_34AROON(), __pyx_pw_5talib_7_ta_lib_35AROON()

### Community 81 - "Community 81"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_4_ta_shutdown(), __pyx_pw_5talib_7_ta_lib_5_ta_shutdown()

### Community 82 - "Community 82"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_400stream_CCI(), __pyx_pw_5talib_7_ta_lib_401stream_CCI()

### Community 83 - "Community 83"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_584stream_MAVP(), __pyx_pw_5talib_7_ta_lib_585stream_MAVP()

### Community 84 - "Community 84"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_596stream_MIDPRICE(), __pyx_pw_5talib_7_ta_lib_597stream_MIDPRICE()

### Community 85 - "Community 85"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_606stream_MINUS_DI(), __pyx_pw_5talib_7_ta_lib_607stream_MINUS_DI()

### Community 86 - "Community 86"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_608stream_MINUS_DM(), __pyx_pw_5talib_7_ta_lib_609stream_MINUS_DM()

### Community 87 - "Community 87"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_614stream_NATR(), __pyx_pw_5talib_7_ta_lib_615stream_NATR()

### Community 88 - "Community 88"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_616stream_OBV(), __pyx_pw_5talib_7_ta_lib_617stream_OBV()

### Community 89 - "Community 89"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_618stream_PLUS_DI(), __pyx_pw_5talib_7_ta_lib_619stream_PLUS_DI()

### Community 90 - "Community 90"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_620stream_PLUS_DM(), __pyx_pw_5talib_7_ta_lib_621stream_PLUS_DM()

### Community 91 - "Community 91"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_634stream_SAR(), __pyx_pw_5talib_7_ta_lib_635stream_SAR()

### Community 92 - "Community 92"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_638stream_SIN(), __pyx_pw_5talib_7_ta_lib_639stream_SIN()

### Community 93 - "Community 93"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_640stream_SINH(), __pyx_pw_5talib_7_ta_lib_641stream_SINH()

### Community 94 - "Community 94"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_642stream_SMA(), __pyx_pw_5talib_7_ta_lib_643stream_SMA()

### Community 95 - "Community 95"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_644stream_SQRT(), __pyx_pw_5talib_7_ta_lib_645stream_SQRT()

### Community 96 - "Community 96"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_646stream_STDDEV(), __pyx_pw_5talib_7_ta_lib_647stream_STDDEV()

### Community 97 - "Community 97"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_648stream_STOCH(), __pyx_pw_5talib_7_ta_lib_649stream_STOCH()

### Community 98 - "Community 98"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_650stream_STOCHF(), __pyx_pw_5talib_7_ta_lib_651stream_STOCHF()

### Community 99 - "Community 99"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_652stream_STOCHRSI(), __pyx_pw_5talib_7_ta_lib_653stream_STOCHRSI()

### Community 100 - "Community 100"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_656stream_SUM(), __pyx_pw_5talib_7_ta_lib_657stream_SUM()

### Community 101 - "Community 101"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_658stream_T3(), __pyx_pw_5talib_7_ta_lib_659stream_T3()

### Community 102 - "Community 102"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_660stream_TAN(), __pyx_pw_5talib_7_ta_lib_661stream_TAN()

### Community 103 - "Community 103"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_662stream_TANH(), __pyx_pw_5talib_7_ta_lib_663stream_TANH()

### Community 104 - "Community 104"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_664stream_TEMA(), __pyx_pw_5talib_7_ta_lib_665stream_TEMA()

### Community 105 - "Community 105"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_666stream_TRANGE(), __pyx_pw_5talib_7_ta_lib_667stream_TRANGE()

### Community 106 - "Community 106"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_668stream_TRIMA(), __pyx_pw_5talib_7_ta_lib_669stream_TRIMA()

### Community 107 - "Community 107"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_670stream_TRIX(), __pyx_pw_5talib_7_ta_lib_671stream_TRIX()

### Community 108 - "Community 108"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_672stream_TSF(), __pyx_pw_5talib_7_ta_lib_673stream_TSF()

### Community 109 - "Community 109"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_674stream_TYPPRICE(), __pyx_pw_5talib_7_ta_lib_675stream_TYPPRICE()

### Community 110 - "Community 110"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_78CDLCLOSINGMARUBOZU(), __pyx_pw_5talib_7_ta_lib_79CDLCLOSINGMARUBOZU()

### Community 111 - "Community 111"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_80CDLCONCEALBABYSWALL(), __pyx_pw_5talib_7_ta_lib_81CDLCONCEALBABYSWALL()

### Community 112 - "Community 112"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_82CDLCOUNTERATTACK(), __pyx_pw_5talib_7_ta_lib_83CDLCOUNTERATTACK()

### Community 113 - "Community 113"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_84CDLDARKCLOUDCOVER(), __pyx_pw_5talib_7_ta_lib_85CDLDARKCLOUDCOVER()

### Community 114 - "Community 114"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_86CDLDOJI(), __pyx_pw_5talib_7_ta_lib_87CDLDOJI()

### Community 115 - "Community 115"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_88CDLDOJISTAR(), __pyx_pw_5talib_7_ta_lib_89CDLDOJISTAR()

### Community 116 - "Community 116"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_90CDLDRAGONFLYDOJI(), __pyx_pw_5talib_7_ta_lib_91CDLDRAGONFLYDOJI()

### Community 117 - "Community 117"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_92CDLENGULFING(), __pyx_pw_5talib_7_ta_lib_93CDLENGULFING()

### Community 118 - "Community 118"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_94CDLEVENINGDOJISTAR(), __pyx_pw_5talib_7_ta_lib_95CDLEVENINGDOJISTAR()

## Knowledge Gaps
- **18 isolated node(s):** `USAGE:  To convert markdown docs into html docs: $ python generate_html_pages.py`, `Returns a dictionary of function names -> upstream documentation link`, `Generate and save markdown files for function group documentation`, `Generate markdown for function groups using the Abstract API      Returns a dict`, `Returns a function to convert a Markdown string into pygments-highlighted HTML` (+13 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 40`** (1 nodes): `pytest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (2 nodes): `__Pyx_c_quot_double()`, `__pyx_t_double_complex_from_parts()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (2 nodes): `__Pyx_c_quot_float()`, `__pyx_t_float_complex_from_parts()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (2 nodes): `__Pyx_c_quot_long__double()`, `__pyx_t_long_double_complex_from_parts()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (2 nodes): `__Pyx_CyFunction_clear()`, `__Pyx__CyFunction_dealloc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (2 nodes): `__Pyx_CyFunction_get_doc()`, `__Pyx_CyFunction_get_doc_locked()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 55`** (2 nodes): `__Pyx__ExceptionSave()`, `__Pyx_PyErr_GetTopmostException()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (2 nodes): `__pyx_f_5numpy_5dtype_8subarray_subarray()`, `__pyx_f_5numpy_PyDataType_SHAPE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (2 nodes): `__Pyx_get_object_dict_version()`, `__Pyx_object_dict_version_matches()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (2 nodes): `__Pyx__IsSameCyOrCFunction()`, `__Pyx__IsSameCyOrCFunctionNoMethod()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 59`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_2_ta_initialize()`, `__pyx_pw_5talib_7_ta_lib_3_ta_initialize()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 60`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_24ADD()`, `__pyx_pw_5talib_7_ta_lib_25ADD()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_250MIDPRICE()`, `__pyx_pw_5talib_7_ta_lib_251MIDPRICE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 62`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_262MINUS_DM()`, `__pyx_pw_5talib_7_ta_lib_263MINUS_DM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_266MULT()`, `__pyx_pw_5talib_7_ta_lib_267MULT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 64`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_270OBV()`, `__pyx_pw_5talib_7_ta_lib_271OBV()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 65`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_274PLUS_DM()`, `__pyx_pw_5talib_7_ta_lib_275PLUS_DM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 66`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_288SAR()`, `__pyx_pw_5talib_7_ta_lib_289SAR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 67`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_28ADX()`, `__pyx_pw_5talib_7_ta_lib_29ADX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 68`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_290SAREXT()`, `__pyx_pw_5talib_7_ta_lib_291SAREXT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 69`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_302STOCH()`, `__pyx_pw_5talib_7_ta_lib_303STOCH()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 70`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_304STOCHF()`, `__pyx_pw_5talib_7_ta_lib_305STOCHF()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 71`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_308SUB()`, `__pyx_pw_5talib_7_ta_lib_309SUB()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 72`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_30ADXR()`, `__pyx_pw_5talib_7_ta_lib_31ADXR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 73`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_320TRANGE()`, `__pyx_pw_5talib_7_ta_lib_321TRANGE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 74`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_328TYPPRICE()`, `__pyx_pw_5talib_7_ta_lib_329TYPPRICE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 75`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_330ULTOSC()`, `__pyx_pw_5talib_7_ta_lib_331ULTOSC()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 76`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_334WCLPRICE()`, `__pyx_pw_5talib_7_ta_lib_335WCLPRICE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 77`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_336WILLR()`, `__pyx_pw_5talib_7_ta_lib_337WILLR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 78`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_344str2bytes()`, `__pyx_pw_5talib_7_ta_lib_345str2bytes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 79`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_348_ta_getGroupTable()`, `__pyx_pw_5talib_7_ta_lib_349_ta_getGroupTable()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 80`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_34AROON()`, `__pyx_pw_5talib_7_ta_lib_35AROON()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 81`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_4_ta_shutdown()`, `__pyx_pw_5talib_7_ta_lib_5_ta_shutdown()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 82`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_400stream_CCI()`, `__pyx_pw_5talib_7_ta_lib_401stream_CCI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 83`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_584stream_MAVP()`, `__pyx_pw_5talib_7_ta_lib_585stream_MAVP()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 84`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_596stream_MIDPRICE()`, `__pyx_pw_5talib_7_ta_lib_597stream_MIDPRICE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 85`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_606stream_MINUS_DI()`, `__pyx_pw_5talib_7_ta_lib_607stream_MINUS_DI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 86`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_608stream_MINUS_DM()`, `__pyx_pw_5talib_7_ta_lib_609stream_MINUS_DM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 87`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_614stream_NATR()`, `__pyx_pw_5talib_7_ta_lib_615stream_NATR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 88`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_616stream_OBV()`, `__pyx_pw_5talib_7_ta_lib_617stream_OBV()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 89`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_618stream_PLUS_DI()`, `__pyx_pw_5talib_7_ta_lib_619stream_PLUS_DI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 90`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_620stream_PLUS_DM()`, `__pyx_pw_5talib_7_ta_lib_621stream_PLUS_DM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 91`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_634stream_SAR()`, `__pyx_pw_5talib_7_ta_lib_635stream_SAR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 92`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_638stream_SIN()`, `__pyx_pw_5talib_7_ta_lib_639stream_SIN()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 93`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_640stream_SINH()`, `__pyx_pw_5talib_7_ta_lib_641stream_SINH()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 94`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_642stream_SMA()`, `__pyx_pw_5talib_7_ta_lib_643stream_SMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 95`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_644stream_SQRT()`, `__pyx_pw_5talib_7_ta_lib_645stream_SQRT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 96`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_646stream_STDDEV()`, `__pyx_pw_5talib_7_ta_lib_647stream_STDDEV()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 97`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_648stream_STOCH()`, `__pyx_pw_5talib_7_ta_lib_649stream_STOCH()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 98`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_650stream_STOCHF()`, `__pyx_pw_5talib_7_ta_lib_651stream_STOCHF()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 99`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_652stream_STOCHRSI()`, `__pyx_pw_5talib_7_ta_lib_653stream_STOCHRSI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 100`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_656stream_SUM()`, `__pyx_pw_5talib_7_ta_lib_657stream_SUM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 101`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_658stream_T3()`, `__pyx_pw_5talib_7_ta_lib_659stream_T3()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 102`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_660stream_TAN()`, `__pyx_pw_5talib_7_ta_lib_661stream_TAN()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 103`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_662stream_TANH()`, `__pyx_pw_5talib_7_ta_lib_663stream_TANH()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 104`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_664stream_TEMA()`, `__pyx_pw_5talib_7_ta_lib_665stream_TEMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 105`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_666stream_TRANGE()`, `__pyx_pw_5talib_7_ta_lib_667stream_TRANGE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 106`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_668stream_TRIMA()`, `__pyx_pw_5talib_7_ta_lib_669stream_TRIMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 107`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_670stream_TRIX()`, `__pyx_pw_5talib_7_ta_lib_671stream_TRIX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 108`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_672stream_TSF()`, `__pyx_pw_5talib_7_ta_lib_673stream_TSF()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 109`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_674stream_TYPPRICE()`, `__pyx_pw_5talib_7_ta_lib_675stream_TYPPRICE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 110`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_78CDLCLOSINGMARUBOZU()`, `__pyx_pw_5talib_7_ta_lib_79CDLCLOSINGMARUBOZU()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 111`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_80CDLCONCEALBABYSWALL()`, `__pyx_pw_5talib_7_ta_lib_81CDLCONCEALBABYSWALL()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 112`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_82CDLCOUNTERATTACK()`, `__pyx_pw_5talib_7_ta_lib_83CDLCOUNTERATTACK()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 113`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_84CDLDARKCLOUDCOVER()`, `__pyx_pw_5talib_7_ta_lib_85CDLDARKCLOUDCOVER()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 114`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_86CDLDOJI()`, `__pyx_pw_5talib_7_ta_lib_87CDLDOJI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 115`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_88CDLDOJISTAR()`, `__pyx_pw_5talib_7_ta_lib_89CDLDOJISTAR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 116`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_90CDLDRAGONFLYDOJI()`, `__pyx_pw_5talib_7_ta_lib_91CDLDRAGONFLYDOJI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 117`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_92CDLENGULFING()`, `__pyx_pw_5talib_7_ta_lib_93CDLENGULFING()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 118`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_94CDLEVENINGDOJISTAR()`, `__pyx_pw_5talib_7_ta_lib_95CDLEVENINGDOJISTAR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `__Pyx_AddTraceback()` connect `Community 1` to `Community 0`, `Community 12`, `Community 7`, `Community 10`, `Community 24`, `Community 25`, `Community 8`, `Community 5`, `Community 3`, `Community 9`, `Community 13`, `Community 2`, `Community 14`, `Community 26`, `Community 27`, `Community 6`, `Community 60`, `Community 61`, `Community 62`, `Community 63`, `Community 64`, `Community 65`, `Community 66`, `Community 67`, `Community 68`, `Community 4`, `Community 59`, `Community 69`, `Community 70`, `Community 71`, `Community 72`, `Community 73`, `Community 74`, `Community 75`, `Community 76`, `Community 77`, `Community 79`, `Community 80`, `Community 28`, `Community 20`, `Community 82`, `Community 81`, `Community 83`, `Community 84`, `Community 85`, `Community 86`, `Community 87`, `Community 88`, `Community 89`, `Community 90`, `Community 91`, `Community 92`, `Community 93`, `Community 94`, `Community 95`, `Community 96`, `Community 97`, `Community 98`, `Community 99`, `Community 100`, `Community 101`, `Community 102`, `Community 103`, `Community 104`, `Community 105`, `Community 106`, `Community 107`, `Community 108`, `Community 109`, `Community 110`, `Community 21`, `Community 111`, `Community 112`, `Community 113`, `Community 114`, `Community 115`, `Community 23`, `Community 116`, `Community 117`, `Community 118`, `Community 78`?**
  _High betweenness centrality (0.128) - this node is a cross-community bridge._
- **Why does `__Pyx_ParseKeywords()` connect `Community 4` to `Community 0`, `Community 38`, `Community 3`, `Community 1`, `Community 10`, `Community 8`, `Community 2`, `Community 9`, `Community 14`, `Community 5`, `Community 26`, `Community 27`, `Community 6`, `Community 24`, `Community 61`, `Community 60`, `Community 62`, `Community 63`, `Community 25`, `Community 64`, `Community 65`, `Community 66`, `Community 68`, `Community 67`, `Community 69`, `Community 70`, `Community 71`, `Community 72`, `Community 73`, `Community 74`, `Community 75`, `Community 76`, `Community 77`, `Community 78`, `Community 13`, `Community 80`, `Community 82`, `Community 83`, `Community 84`, `Community 85`, `Community 86`, `Community 87`, `Community 88`, `Community 89`, `Community 90`, `Community 91`, `Community 92`, `Community 93`, `Community 94`, `Community 95`, `Community 96`, `Community 97`, `Community 98`, `Community 99`, `Community 100`, `Community 101`, `Community 102`, `Community 103`, `Community 104`, `Community 105`, `Community 106`, `Community 107`, `Community 108`, `Community 109`, `Community 110`, `Community 20`, `Community 111`, `Community 112`, `Community 113`, `Community 114`, `Community 115`, `Community 23`, `Community 21`, `Community 28`, `Community 116`, `Community 117`, `Community 118`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **Why does `__Pyx_RaiseArgtupleInvalid()` connect `Community 4` to `Community 0`, `Community 3`, `Community 1`, `Community 10`, `Community 8`, `Community 2`, `Community 9`, `Community 14`, `Community 5`, `Community 26`, `Community 27`, `Community 6`, `Community 24`, `Community 61`, `Community 60`, `Community 62`, `Community 63`, `Community 25`, `Community 64`, `Community 65`, `Community 66`, `Community 68`, `Community 67`, `Community 69`, `Community 70`, `Community 71`, `Community 72`, `Community 73`, `Community 74`, `Community 75`, `Community 76`, `Community 77`, `Community 78`, `Community 13`, `Community 80`, `Community 82`, `Community 83`, `Community 84`, `Community 85`, `Community 86`, `Community 87`, `Community 88`, `Community 89`, `Community 90`, `Community 91`, `Community 92`, `Community 93`, `Community 94`, `Community 95`, `Community 96`, `Community 97`, `Community 98`, `Community 99`, `Community 100`, `Community 101`, `Community 102`, `Community 103`, `Community 104`, `Community 105`, `Community 106`, `Community 107`, `Community 108`, `Community 109`, `Community 110`, `Community 20`, `Community 111`, `Community 112`, `Community 113`, `Community 114`, `Community 115`, `Community 23`, `Community 21`, `Community 28`, `Community 116`, `Community 117`, `Community 118`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **What connects `USAGE:  To convert markdown docs into html docs: $ python generate_html_pages.py`, `Returns a dictionary of function names -> upstream documentation link`, `Generate and save markdown files for function group documentation` to the rest of the system?**
  _18 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.016 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.03199023199023199 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.03356282271944923 - nodes in this community are weakly interconnected._