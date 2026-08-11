# Graph Report - talib  (2026-08-06)

## Corpus Check
- 5 files · ~352,721 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1140 nodes · 5352 edges · 200 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output
- Edge kinds: calls: 4214 · contains: 1133 · imports_from: 3 · rationale_for: 2


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 5 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

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
  _ta_lib.c → _ta_lib.c  _Bridges community 8 → community 9_
- `__Pyx_CallUnboundCMethod0()` --calls--> `__Pyx_PyObject_CallOneArg()`  [EXTRACTED]
  _ta_lib.c → _ta_lib.c  _Bridges community 15 → community 12_
- `__Pyx_CyFunction_CallAsMethod()` --calls--> `__Pyx_PyVectorcall_FastCallDict()`  [EXTRACTED]
  _ta_lib.c → _ta_lib.c  _Bridges community 22 → community 15_
- `__Pyx_CyFunction_get_annotations()` --calls--> `__Pyx_NewRef()`  [EXTRACTED]
  _ta_lib.c → _ta_lib.c  _Bridges community 9 → community 11_
- `__Pyx_CyFunction_get_annotations()` --calls--> `__Pyx_PyObject_CallOneArg()`  [EXTRACTED]
  _ta_lib.c → _ta_lib.c  _Bridges community 9 → community 12_

## Communities

### Community 1 - "Community 1"
Cohesion: 0.03
Nodes (84): __pyx_f_5talib_7_ta_lib_check_length4(), __pyx_pf_5talib_7_ta_lib_12_ta_get_compatibility(), __pyx_pf_5talib_7_ta_lib_136CDLMATCHINGLOW(), __pyx_pf_5talib_7_ta_lib_148CDLRICKSHAWMAN(), __pyx_pf_5talib_7_ta_lib_160CDLSTALLEDPATTERN(), __pyx_pf_5talib_7_ta_lib_172CDLUNIQUE3RIVER(), __pyx_pf_5talib_7_ta_lib_372stream_ADOSC(), __pyx_pf_5talib_7_ta_lib_402stream_CDL2CROWS() (+76 more)

### Community 2 - "Community 2"
Cohesion: 0.04
Nodes (78): __pyx_f_5talib_7_ta_lib_check_begidx4(), __pyx_f_5talib_7_ta_lib_make_int_array(), __pyx_pf_5talib_7_ta_lib_100CDLGRAVESTONEDOJI(), __pyx_pf_5talib_7_ta_lib_102CDLHAMMER(), __pyx_pf_5talib_7_ta_lib_104CDLHANGINGMAN(), __pyx_pf_5talib_7_ta_lib_106CDLHARAMI(), __pyx_pf_5talib_7_ta_lib_108CDLHARAMICROSS(), __pyx_pf_5talib_7_ta_lib_110CDLHIGHWAVE() (+70 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (43): __pyx_f_5numpy_7ndarray_5shape_shape(), __pyx_pf_5talib_7_ta_lib_220LINEARREG_INTERCEPT(), __pyx_pf_5talib_7_ta_lib_228MA(), __pyx_pf_5talib_7_ta_lib_236MAMA(), __pyx_pf_5talib_7_ta_lib_252MIN(), __pyx_pf_5talib_7_ta_lib_278ROC(), __pyx_pf_5talib_7_ta_lib_292SIN(), __pyx_pf_5talib_7_ta_lib_310SUM() (+35 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (36): __Pyx_CalculateMetaclass(), __Pyx_call_type_traverse(), __Pyx_check_binary_version(), __Pyx_CreateCodeObjects(), __Pyx_CyFunction_SetDefaultsTuple(), __Pyx_CyFunction_traverse(), __Pyx_CyOrPyCFunction_GET_SELF(), __Pyx_DecompressString() (+28 more)

### Community 5 - "Community 5"
Cohesion: 0.06
Nodes (33): __pyx_f_5talib_7_ta_lib__ta_check_success(), __pyx_f_5talib_7_ta_lib___ta_getLookback(), __pyx_f_5talib_7_ta_lib___ta_paramHolderFree(), __pyx_f_5talib_7_ta_lib___ta_setOptInputParamInteger(), __pyx_f_5talib_7_ta_lib___ta_setOptInputParamReal(), __pyx_pf_5talib_7_ta_lib_142CDLMORNINGSTAR(), __pyx_pf_5talib_7_ta_lib_154CDLSHOOTINGSTAR(), __pyx_pf_5talib_7_ta_lib_166CDLTASUKIGAP() (+25 more)

### Community 6 - "Community 6"
Cohesion: 0.06
Nodes (32): __pyx_f_5numpy_7ndarray_4ndim_ndim(), __pyx_f_5talib_7_ta_lib_check_array(), __pyx_pf_5talib_7_ta_lib_132CDLLONGLINE(), __pyx_pf_5talib_7_ta_lib_144CDLONNECK(), __pyx_pf_5talib_7_ta_lib_156CDLSHORTLINE(), __pyx_pf_5talib_7_ta_lib_168CDLTHRUSTING(), __pyx_pf_5talib_7_ta_lib_246MFI(), __pyx_pf_5talib_7_ta_lib_390stream_AVGPRICE() (+24 more)

### Community 7 - "Community 7"
Cohesion: 0.06
Nodes (31): __pyx_f_5numpy_7ndarray_4data_data(), __pyx_pf_5talib_7_ta_lib_140CDLMORNINGDOJISTAR(), __pyx_pf_5talib_7_ta_lib_152CDLSEPARATINGLINES(), __pyx_pf_5talib_7_ta_lib_164CDLTAKURI(), __pyx_pf_5talib_7_ta_lib_176CDLXSIDEGAP3METHODS(), __pyx_pf_5talib_7_ta_lib_398stream_BOP(), __pyx_pf_5talib_7_ta_lib_434stream_CDLDOJISTAR(), __pyx_pf_5talib_7_ta_lib_444stream_CDLGAPSIDESIDEWHITE() (+23 more)

### Community 8 - "Community 8"
Cohesion: 0.10
Nodes (27): __Pyx_AddTraceback(), __Pyx_CreateCodeObjectForTraceback(), __pyx_f_5numpy_PyArray_MultiIterNew1(), __pyx_f_5numpy_PyArray_MultiIterNew2(), __pyx_f_5numpy_PyArray_MultiIterNew3(), __pyx_f_5numpy_PyArray_MultiIterNew4(), __pyx_f_5numpy_PyArray_MultiIterNew5(), __pyx_f_5numpy_set_array_base() (+19 more)

### Community 9 - "Community 9"
Cohesion: 0.08
Nodes (26): __Pyx_CLineForTraceback(), __pyx_CommonTypesMetaclass_init(), __Pyx_CyFunction_get_annotate(), __Pyx_CyFunction_get_annotate_from_dict_if_exists(), __Pyx_CyFunction_get_annotations(), __Pyx_CyFunction_get_annotations_locked(), __Pyx_CyFunction_get_dict_if_exists(), __Pyx_CyFunction_Init() (+18 more)

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (24): __pyx_f_5talib_7_ta_lib___ta_getFuncHandle(), __pyx_f_5talib_7_ta_lib___ta_paramHolderAlloc(), __pyx_pf_5talib_7_ta_lib_354_ta_getFuncInfo(), __pyx_pf_5talib_7_ta_lib_356_ta_getInputParameterInfo(), __pyx_pf_5talib_7_ta_lib_358_ta_getOptInputParameterInfo(), __pyx_pf_5talib_7_ta_lib_360_ta_getOutputParameterInfo(), __pyx_pf_5talib_7_ta_lib_8Function_24lookback(), __pyx_pw_5talib_7_ta_lib_353__get_flags() (+16 more)

### Community 11 - "Community 11"
Cohesion: 0.13
Nodes (23): __Pyx_CyFunction_get_is_coroutine(), __Pyx_CyFunction_get_is_coroutine_value(), __Pyx__CyFunction_SetClassObj(), __Pyx_NewRef(), __Pyx_Owned_Py_None(), __pyx_pf_5talib_7_ta_lib_14_ta_set_candle_settings(), __pyx_pf_5talib_7_ta_lib_6_ta_set_unstable_period(), __pyx_pf_5talib_7_ta_lib_8_ta_get_unstable_period() (+15 more)

### Community 12 - "Community 12"
Cohesion: 0.11
Nodes (21): __Pyx__ArgTypeTest(), __Pyx_dict_iterator(), __Pyx_GetBuiltinName(), __Pyx_HasAttr(), __Pyx_InitCachedBuiltins(), __Pyx_PEP560_update_bases(), __Pyx_PyBuiltin_Invalid(), __Pyx_PyDict_GetItemStr() (+13 more)

### Community 13 - "Community 13"
Cohesion: 0.18
Nodes (17): __pyx_pf_5talib_7_ta_lib_362_get_defaults_and_docs(), __pyx_pf_5talib_7_ta_lib_7MA_Type_2__getitem__(), __pyx_pf_5talib_7_ta_lib_8Function_10get_input_names(), __pyx_pf_5talib_7_ta_lib_8Function_16set_input_arrays(), __pyx_pf_5talib_7_ta_lib_8Function_34__input_price_series_names(), __pyx_pf_5talib_7_ta_lib_8Function_38__check_opt_input_value(), __pyx_pf_5talib_7_ta_lib_8Function_40__get_opt_input_value(), __pyx_pw_5talib_7_ta_lib_7MA_Type_3__getitem__() (+9 more)

### Community 14 - "Community 14"
Cohesion: 0.21
Nodes (17): __pyx_pf_5talib_7_ta_lib_7MA_Type___init__(), __pyx_pf_5talib_7_ta_lib_8Function_14get_input_arrays(), __pyx_pf_5talib_7_ta_lib_8Function_18get_parameters(), __pyx_pf_5talib_7_ta_lib_8Function_26output_names(), __pyx_pf_5talib_7_ta_lib_8Function_28outputs(), __pyx_pf_5talib_7_ta_lib_8Function_2__local(), __pyx_pf_5talib_7_ta_lib_8Function_30run(), __pyx_pf_5talib_7_ta_lib_8Function_36__call_function() (+9 more)

### Community 15 - "Community 15"
Cohesion: 0.16
Nodes (15): __pyx_atomic_int_cmp_exchange(), __pyx_bisect_code_objects(), __Pyx_CachedCFunction_GetAndSetInitializing(), __Pyx_CachedCFunction_SetFinishedInitializing(), __Pyx_CallUnboundCMethod0(), __Pyx_CallUnboundCMethod2(), __pyx__find_code_object(), __pyx__insert_code_object() (+7 more)

### Community 16 - "Community 16"
Cohesion: 0.26
Nodes (15): __Pyx_dict_iter_next(), __Pyx_dict_iter_next_source_is_dict(), __Pyx_IterFinish(), __Pyx_IternextUnpackEndCheck(), __pyx_pf_5talib_7_ta_lib_8Function_12set_input_names(), __pyx_pf_5talib_7_ta_lib_8Function_20set_parameters(), __pyx_pf_5talib_7_ta_lib_8Function_32__call__(), __pyx_pw_5talib_7_ta_lib_8Function_13set_input_names() (+7 more)

### Community 17 - "Community 17"
Cohesion: 0.13
Nodes (15): __pyx_f_5talib_7_ta_lib_check_length2(), __pyx_pf_5talib_7_ta_lib_238MAVP(), __pyx_pf_5talib_7_ta_lib_370stream_ADD(), __pyx_pf_5talib_7_ta_lib_380stream_AROON(), __pyx_pf_5talib_7_ta_lib_382stream_AROONOSC(), __pyx_pf_5talib_7_ta_lib_396stream_BETA(), __pyx_pf_5talib_7_ta_lib_636stream_SAREXT(), __pyx_pf_5talib_7_ta_lib_654stream_SUB() (+7 more)

### Community 18 - "Community 18"
Cohesion: 0.13
Nodes (15): __pyx_f_5talib_7_ta_lib_check_length3(), __pyx_pf_5talib_7_ta_lib_268NATR(), __pyx_pf_5talib_7_ta_lib_364stream_ACCBANDS(), __pyx_pf_5talib_7_ta_lib_374stream_ADX(), __pyx_pf_5talib_7_ta_lib_376stream_ADXR(), __pyx_pf_5talib_7_ta_lib_388stream_ATR(), __pyx_pf_5talib_7_ta_lib_676stream_ULTOSC(), __pyx_pf_5talib_7_ta_lib_682stream_WILLR() (+7 more)

### Community 19 - "Community 19"
Cohesion: 0.15
Nodes (13): __pyx_f_5talib_7_ta_lib_check_begidx2(), __pyx_pf_5talib_7_ta_lib_182CORREL(), __pyx_pf_5talib_7_ta_lib_190DIV(), __pyx_pf_5talib_7_ta_lib_212IMI(), __pyx_pf_5talib_7_ta_lib_244MEDPRICE(), __pyx_pf_5talib_7_ta_lib_36AROONOSC(), __pyx_pf_5talib_7_ta_lib_50BETA(), __pyx_pw_5talib_7_ta_lib_183CORREL() (+5 more)

### Community 20 - "Community 20"
Cohesion: 0.15
Nodes (13): __pyx_f_5talib_7_ta_lib_check_begidx3(), __pyx_pf_5talib_7_ta_lib_18ACCBANDS(), __pyx_pf_5talib_7_ta_lib_192DX(), __pyx_pf_5talib_7_ta_lib_260MINUS_DI(), __pyx_pf_5talib_7_ta_lib_272PLUS_DI(), __pyx_pf_5talib_7_ta_lib_42ATR(), __pyx_pf_5talib_7_ta_lib_54CCI(), __pyx_pw_5talib_7_ta_lib_193DX() (+5 more)

### Community 21 - "Community 21"
Cohesion: 0.18
Nodes (13): __Pyx_Fallback___Pyx_PyLong_AddObjC(), __Pyx_Float___Pyx_PyLong_AddObjC(), __Pyx_GetKwValue_FASTCALL(), __pyx_pf_5talib_7_ta_lib_352__get_flags(), __pyx_pf_5talib_7_ta_lib_8Function_22set_function_args(), __pyx_pw_5talib_7_ta_lib_8Function_23set_function_args(), __Pyx_PyBytes_Equals(), __Pyx_PyDict_GetItem() (+5 more)

### Community 22 - "Community 22"
Cohesion: 0.23
Nodes (12): __Pyx_CyFunction_Call(), __Pyx_CyFunction_CallAsMethod(), __Pyx_CyFunction_CallMethod(), __Pyx_CyFunction_get_name(), __Pyx_CyFunction_get_name_locked(), __Pyx_CyFunction_raise_argument_count_error(), __Pyx_CyFunction_raise_type_error(), __Pyx_CyFunction_Vectorcall_CheckArgs() (+4 more)

### Community 23 - "Community 23"
Cohesion: 0.18
Nodes (11): __pyx_f_5talib_7_ta_lib_check_begidx1(), __pyx_pf_5talib_7_ta_lib_178CEIL(), __pyx_pf_5talib_7_ta_lib_184COS(), __pyx_pf_5talib_7_ta_lib_188DEMA(), __pyx_pf_5talib_7_ta_lib_258MINMAXINDEX(), __pyx_pf_5talib_7_ta_lib_48BBANDS(), __pyx_pw_5talib_7_ta_lib_179CEIL(), __pyx_pw_5talib_7_ta_lib_185COS() (+3 more)

### Community 24 - "Community 24"
Cohesion: 0.18
Nodes (11): __pyx_f_5talib_7_ta_lib_make_double_array(), __pyx_pf_5talib_7_ta_lib_180CMO(), __pyx_pf_5talib_7_ta_lib_186COSH(), __pyx_pf_5talib_7_ta_lib_194EMA(), __pyx_pf_5talib_7_ta_lib_40ATAN(), __pyx_pf_5talib_7_ta_lib_52BOP(), __pyx_pw_5talib_7_ta_lib_181CMO(), __pyx_pw_5talib_7_ta_lib_187COSH() (+3 more)

### Community 25 - "Community 25"
Cohesion: 0.18
Nodes (11): __pyx_pw_5talib_7_ta_lib_363_get_defaults_and_docs(), __pyx_pw_5talib_7_ta_lib_7MA_Type_1__init__(), __pyx_pw_5talib_7_ta_lib_8Function_11get_input_names(), __pyx_pw_5talib_7_ta_lib_8Function_17set_input_arrays(), __pyx_pw_5talib_7_ta_lib_8Function_1__init__(), __pyx_pw_5talib_7_ta_lib_8Function_27output_names(), __pyx_pw_5talib_7_ta_lib_8Function_35__input_price_series_names(), __pyx_pw_5talib_7_ta_lib_8Function_39__check_opt_input_value() (+3 more)

### Community 26 - "Community 26"
Cohesion: 0.22
Nodes (10): __Pyx_copy_object_array(), __Pyx_crop_slice(), __Pyx__Import(), __Pyx__Import_GetModule(), __Pyx__Import_Lookup(), __Pyx_PyList_FromArray(), __Pyx_PyList_GetSlice(), __Pyx_PyList_GetSlice_locked() (+2 more)

### Community 27 - "Community 27"
Cohesion: 0.24
Nodes (10): __Pyx_GetItemInt_Fast(), __Pyx_GetItemInt_Generic(), __Pyx_GetItemInt_List_Fast(), __Pyx_GetItemInt_Tuple_Fast(), __Pyx_is_valid_index(), __Pyx_PyIndex_AsHash_t(), __Pyx_PyIndex_AsSsize_t(), __Pyx_PyObject_GetIndex() (+2 more)

### Community 28 - "Community 28"
Cohesion: 0.22
Nodes (10): __Pyx_ParseKeywordDict(), __Pyx_ParseKeywordDictToDict(), __Pyx_ParseKeywords(), __pyx_pw_5talib_7_ta_lib_8Function_19get_parameters(), __pyx_pw_5talib_7_ta_lib_8Function_25lookback(), __pyx_pw_5talib_7_ta_lib_8Function_33__call__(), __pyx_pw_5talib_7_ta_lib_8Function_37__call_function(), __pyx_pw_5talib_7_ta_lib_8Function_3__local() (+2 more)

### Community 29 - "Community 29"
Cohesion: 0.29
Nodes (8): __pyx_m_clear(), __Pyx_ModuleStateLookup_wait_until_no_readers(), __Pyx_State_AddModule(), __Pyx_State_AddModuleInterpIdAsIndex(), __Pyx_State_ConvertFromInterpIdAsIndex(), __Pyx_State_FindModule(), __Pyx_State_FindModuleStateLookupTableLowerBound(), __Pyx_State_RemoveModule()

### Community 30 - "Community 30"
Cohesion: 0.33
Nodes (7): __Pyx_CheckUnicodeValue(), __Pyx_PyUnicode_BuildFromAscii(), __Pyx_PyUnicode_FromOrdinal_Padded(), __Pyx____Pyx_PyUnicode_From_Py_ssize_t(), __Pyx____Pyx_PyUnicode_From_TA_RetCode(), __Pyx_uchar___Pyx_PyUnicode_From_Py_ssize_t(), __Pyx_uchar___Pyx_PyUnicode_From_TA_RetCode()

### Community 31 - "Community 31"
Cohesion: 0.33
Nodes (4): get_function_groups(), get_functions(), Returns a list of all the functions supported by TALIB, Returns a dict with keys of function-group names and values of lists     of func

### Community 32 - "Community 32"
Cohesion: 0.40
Nodes (6): __Pyx_InBases(), __Pyx_inner_PyErr_GivenExceptionMatches2(), __Pyx_IsAnySubtype2(), __Pyx_IsSubtype(), __Pyx_PyErr_GivenExceptionMatches2(), __Pyx_PyErr_GivenExceptionMatchesTuple()

### Community 33 - "Community 33"
Cohesion: 0.40
Nodes (6): __Pyx_MatchKeywordArg(), __Pyx_MatchKeywordArg_nostr(), __Pyx_MatchKeywordArg_str(), __Pyx_ParseKeywordsTuple(), __Pyx_RaiseDoubleKeywordsError(), __Pyx_UnicodeKeywordsEqual()

### Community 34 - "Community 34"
Cohesion: 0.40
Nodes (5): __Pyx_CyFunction_get_defaults(), __Pyx_CyFunction_get_defaults_locked(), __Pyx_CyFunction_get_kwdefaults(), __Pyx_CyFunction_get_kwdefaults_locked(), __Pyx_CyFunction_init_defaults()

### Community 35 - "Community 35"
Cohesion: 0.50
Nodes (4): __Pyx_check_single_interpreter(), __Pyx_copy_spec_to_module(), __Pyx_GetCurrentInterpreterId(), __pyx_pymod_create()

### Community 36 - "Community 36"
Cohesion: 0.67
Nodes (3): __Pyx_c_abs_double(), __Pyx_c_pow_double(), __Pyx_c_prod_double()

### Community 37 - "Community 37"
Cohesion: 0.67
Nodes (3): __Pyx_c_abs_float(), __Pyx_c_pow_float(), __Pyx_c_prod_float()

### Community 38 - "Community 38"
Cohesion: 0.67
Nodes (3): __Pyx_c_abs_long__double(), __Pyx_c_pow_long__double(), __Pyx_c_prod_long__double()

### Community 39 - "Community 39"
Cohesion: 0.67
Nodes (3): __Pyx_CyFunction_get_dict(), __Pyx_CyFunction_set_annotate(), __Pyx_CyFunction_set_annotate_in_dict()

### Community 40 - "Community 40"
Cohesion: 0.67
Nodes (3): __Pyx_GetTypeDict(), __Pyx_GetTypeDictOffset(), __Pyx__SetItemOnTypeDict()

### Community 41 - "Community 41"
Cohesion: 0.67
Nodes (3): __Pyx_PyByteArray_FromString(), __Pyx_PyUnicode_FromString(), __Pyx_ssize_strlen()

### Community 42 - "Community 42"
Cohesion: 0.67
Nodes (3): __Pyx_PyObject_AsString(), __Pyx_PyObject_AsStringAndSize(), __Pyx_PyUnicode_AsStringAndSize()

### Community 44 - "Community 44"
Cohesion: 1.00
Nodes (2): __Pyx_c_quot_double(), __pyx_t_double_complex_from_parts()

### Community 45 - "Community 45"
Cohesion: 1.00
Nodes (2): __Pyx_c_quot_float(), __pyx_t_float_complex_from_parts()

### Community 46 - "Community 46"
Cohesion: 1.00
Nodes (2): __Pyx_c_quot_long__double(), __pyx_t_long_double_complex_from_parts()

### Community 47 - "Community 47"
Cohesion: 1.00
Nodes (2): __Pyx_CyFunction_clear(), __Pyx__CyFunction_dealloc()

### Community 48 - "Community 48"
Cohesion: 1.00
Nodes (2): __Pyx_CyFunction_get_doc(), __Pyx_CyFunction_get_doc_locked()

### Community 49 - "Community 49"
Cohesion: 1.00
Nodes (2): __Pyx__ExceptionSave(), __Pyx_PyErr_GetTopmostException()

### Community 50 - "Community 50"
Cohesion: 1.00
Nodes (2): __pyx_f_5numpy_5dtype_8subarray_subarray(), __pyx_f_5numpy_PyDataType_SHAPE()

### Community 51 - "Community 51"
Cohesion: 1.00
Nodes (2): __Pyx_get_object_dict_version(), __Pyx_object_dict_version_matches()

### Community 52 - "Community 52"
Cohesion: 1.00
Nodes (2): __Pyx__IsSameCyOrCFunction(), __Pyx__IsSameCyOrCFunctionNoMethod()

### Community 53 - "Community 53"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_196EXP(), __pyx_pw_5talib_7_ta_lib_197EXP()

### Community 54 - "Community 54"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_198FLOOR(), __pyx_pw_5talib_7_ta_lib_199FLOOR()

### Community 55 - "Community 55"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_2_ta_initialize(), __pyx_pw_5talib_7_ta_lib_3_ta_initialize()

### Community 56 - "Community 56"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_202HT_DCPHASE(), __pyx_pw_5talib_7_ta_lib_203HT_DCPHASE()

### Community 57 - "Community 57"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_204HT_PHASOR(), __pyx_pw_5talib_7_ta_lib_205HT_PHASOR()

### Community 58 - "Community 58"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_208HT_TRENDLINE(), __pyx_pw_5talib_7_ta_lib_209HT_TRENDLINE()

### Community 59 - "Community 59"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_20ACOS(), __pyx_pw_5talib_7_ta_lib_21ACOS()

### Community 60 - "Community 60"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_214KAMA(), __pyx_pw_5talib_7_ta_lib_215KAMA()

### Community 61 - "Community 61"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_216LINEARREG(), __pyx_pw_5talib_7_ta_lib_217LINEARREG()

### Community 62 - "Community 62"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_222LINEARREG_SLOPE(), __pyx_pw_5talib_7_ta_lib_223LINEARREG_SLOPE()

### Community 63 - "Community 63"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_224LN(), __pyx_pw_5talib_7_ta_lib_225LN()

### Community 64 - "Community 64"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_230MACD(), __pyx_pw_5talib_7_ta_lib_231MACD()

### Community 65 - "Community 65"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_232MACDEXT(), __pyx_pw_5talib_7_ta_lib_233MACDEXT()

### Community 66 - "Community 66"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_240MAX(), __pyx_pw_5talib_7_ta_lib_241MAX()

### Community 67 - "Community 67"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_242MAXINDEX(), __pyx_pw_5talib_7_ta_lib_243MAXINDEX()

### Community 68 - "Community 68"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_248MIDPOINT(), __pyx_pw_5talib_7_ta_lib_249MIDPOINT()

### Community 69 - "Community 69"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_24ADD(), __pyx_pw_5talib_7_ta_lib_25ADD()

### Community 70 - "Community 70"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_250MIDPRICE(), __pyx_pw_5talib_7_ta_lib_251MIDPRICE()

### Community 71 - "Community 71"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_254MININDEX(), __pyx_pw_5talib_7_ta_lib_255MININDEX()

### Community 72 - "Community 72"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_256MINMAX(), __pyx_pw_5talib_7_ta_lib_257MINMAX()

### Community 73 - "Community 73"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_262MINUS_DM(), __pyx_pw_5talib_7_ta_lib_263MINUS_DM()

### Community 74 - "Community 74"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_264MOM(), __pyx_pw_5talib_7_ta_lib_265MOM()

### Community 75 - "Community 75"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_266MULT(), __pyx_pw_5talib_7_ta_lib_267MULT()

### Community 76 - "Community 76"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_270OBV(), __pyx_pw_5talib_7_ta_lib_271OBV()

### Community 77 - "Community 77"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_274PLUS_DM(), __pyx_pw_5talib_7_ta_lib_275PLUS_DM()

### Community 78 - "Community 78"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_276PPO(), __pyx_pw_5talib_7_ta_lib_277PPO()

### Community 79 - "Community 79"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_280ROCP(), __pyx_pw_5talib_7_ta_lib_281ROCP()

### Community 80 - "Community 80"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_282ROCR(), __pyx_pw_5talib_7_ta_lib_283ROCR()

### Community 81 - "Community 81"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_284ROCR100(), __pyx_pw_5talib_7_ta_lib_285ROCR100()

### Community 82 - "Community 82"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_286RSI(), __pyx_pw_5talib_7_ta_lib_287RSI()

### Community 83 - "Community 83"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_288SAR(), __pyx_pw_5talib_7_ta_lib_289SAR()

### Community 84 - "Community 84"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_28ADX(), __pyx_pw_5talib_7_ta_lib_29ADX()

### Community 85 - "Community 85"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_290SAREXT(), __pyx_pw_5talib_7_ta_lib_291SAREXT()

### Community 86 - "Community 86"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_294SINH(), __pyx_pw_5talib_7_ta_lib_295SINH()

### Community 87 - "Community 87"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_296SMA(), __pyx_pw_5talib_7_ta_lib_297SMA()

### Community 88 - "Community 88"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_298SQRT(), __pyx_pw_5talib_7_ta_lib_299SQRT()

### Community 89 - "Community 89"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_300STDDEV(), __pyx_pw_5talib_7_ta_lib_301STDDEV()

### Community 90 - "Community 90"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_302STOCH(), __pyx_pw_5talib_7_ta_lib_303STOCH()

### Community 91 - "Community 91"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_304STOCHF(), __pyx_pw_5talib_7_ta_lib_305STOCHF()

### Community 92 - "Community 92"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_306STOCHRSI(), __pyx_pw_5talib_7_ta_lib_307STOCHRSI()

### Community 93 - "Community 93"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_308SUB(), __pyx_pw_5talib_7_ta_lib_309SUB()

### Community 94 - "Community 94"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_30ADXR(), __pyx_pw_5talib_7_ta_lib_31ADXR()

### Community 95 - "Community 95"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_312T3(), __pyx_pw_5talib_7_ta_lib_313T3()

### Community 96 - "Community 96"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_314TAN(), __pyx_pw_5talib_7_ta_lib_315TAN()

### Community 97 - "Community 97"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_316TANH(), __pyx_pw_5talib_7_ta_lib_317TANH()

### Community 98 - "Community 98"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_318TEMA(), __pyx_pw_5talib_7_ta_lib_319TEMA()

### Community 99 - "Community 99"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_320TRANGE(), __pyx_pw_5talib_7_ta_lib_321TRANGE()

### Community 100 - "Community 100"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_322TRIMA(), __pyx_pw_5talib_7_ta_lib_323TRIMA()

### Community 101 - "Community 101"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_326TSF(), __pyx_pw_5talib_7_ta_lib_327TSF()

### Community 102 - "Community 102"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_328TYPPRICE(), __pyx_pw_5talib_7_ta_lib_329TYPPRICE()

### Community 103 - "Community 103"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_32APO(), __pyx_pw_5talib_7_ta_lib_33APO()

### Community 104 - "Community 104"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_330ULTOSC(), __pyx_pw_5talib_7_ta_lib_331ULTOSC()

### Community 105 - "Community 105"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_332VAR(), __pyx_pw_5talib_7_ta_lib_333VAR()

### Community 106 - "Community 106"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_334WCLPRICE(), __pyx_pw_5talib_7_ta_lib_335WCLPRICE()

### Community 107 - "Community 107"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_336WILLR(), __pyx_pw_5talib_7_ta_lib_337WILLR()

### Community 108 - "Community 108"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_338WMA(), __pyx_pw_5talib_7_ta_lib_339WMA()

### Community 109 - "Community 109"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_340str2bytes(), __pyx_pw_5talib_7_ta_lib_341str2bytes()

### Community 110 - "Community 110"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_342bytes2str(), __pyx_pw_5talib_7_ta_lib_343bytes2str()

### Community 111 - "Community 111"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_344str2bytes(), __pyx_pw_5talib_7_ta_lib_345str2bytes()

### Community 112 - "Community 112"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_346bytes2str(), __pyx_pw_5talib_7_ta_lib_347bytes2str()

### Community 113 - "Community 113"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_348_ta_getGroupTable(), __pyx_pw_5talib_7_ta_lib_349_ta_getGroupTable()

### Community 114 - "Community 114"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_34AROON(), __pyx_pw_5talib_7_ta_lib_35AROON()

### Community 115 - "Community 115"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_350_ta_getFuncTable(), __pyx_pw_5talib_7_ta_lib_351_ta_getFuncTable()

### Community 116 - "Community 116"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_366stream_ACOS(), __pyx_pw_5talib_7_ta_lib_367stream_ACOS()

### Community 117 - "Community 117"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_378stream_APO(), __pyx_pw_5talib_7_ta_lib_379stream_APO()

### Community 118 - "Community 118"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_384stream_ASIN(), __pyx_pw_5talib_7_ta_lib_385stream_ASIN()

### Community 119 - "Community 119"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_386stream_ATAN(), __pyx_pw_5talib_7_ta_lib_387stream_ATAN()

### Community 120 - "Community 120"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_392stream_AVGDEV(), __pyx_pw_5talib_7_ta_lib_393stream_AVGDEV()

### Community 121 - "Community 121"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_394stream_BBANDS(), __pyx_pw_5talib_7_ta_lib_395stream_BBANDS()

### Community 122 - "Community 122"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_4_ta_shutdown(), __pyx_pw_5talib_7_ta_lib_5_ta_shutdown()

### Community 123 - "Community 123"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_400stream_CCI(), __pyx_pw_5talib_7_ta_lib_401stream_CCI()

### Community 124 - "Community 124"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_46AVGDEV(), __pyx_pw_5talib_7_ta_lib_47AVGDEV()

### Community 125 - "Community 125"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_524stream_CEIL(), __pyx_pw_5talib_7_ta_lib_525stream_CEIL()

### Community 126 - "Community 126"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_526stream_CMO(), __pyx_pw_5talib_7_ta_lib_527stream_CMO()

### Community 127 - "Community 127"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_528stream_CORREL(), __pyx_pw_5talib_7_ta_lib_529stream_CORREL()

### Community 128 - "Community 128"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_530stream_COS(), __pyx_pw_5talib_7_ta_lib_531stream_COS()

### Community 129 - "Community 129"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_534stream_DEMA(), __pyx_pw_5talib_7_ta_lib_535stream_DEMA()

### Community 130 - "Community 130"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_536stream_DIV(), __pyx_pw_5talib_7_ta_lib_537stream_DIV()

### Community 131 - "Community 131"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_538stream_DX(), __pyx_pw_5talib_7_ta_lib_539stream_DX()

### Community 132 - "Community 132"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_540stream_EMA(), __pyx_pw_5talib_7_ta_lib_541stream_EMA()

### Community 133 - "Community 133"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_544stream_FLOOR(), __pyx_pw_5talib_7_ta_lib_545stream_FLOOR()

### Community 134 - "Community 134"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_546stream_HT_DCPERIOD(), __pyx_pw_5talib_7_ta_lib_547stream_HT_DCPERIOD()

### Community 135 - "Community 135"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_550stream_HT_PHASOR(), __pyx_pw_5talib_7_ta_lib_551stream_HT_PHASOR()

### Community 136 - "Community 136"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_552stream_HT_SINE(), __pyx_pw_5talib_7_ta_lib_553stream_HT_SINE()

### Community 137 - "Community 137"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_554stream_HT_TRENDLINE(), __pyx_pw_5talib_7_ta_lib_555stream_HT_TRENDLINE()

### Community 138 - "Community 138"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_558stream_IMI(), __pyx_pw_5talib_7_ta_lib_559stream_IMI()

### Community 139 - "Community 139"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_560stream_KAMA(), __pyx_pw_5talib_7_ta_lib_561stream_KAMA()

### Community 140 - "Community 140"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_562stream_LINEARREG(), __pyx_pw_5talib_7_ta_lib_563stream_LINEARREG()

### Community 141 - "Community 141"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_566stream_LINEARREG_INTERCEPT(), __pyx_pw_5talib_7_ta_lib_567stream_LINEARREG_INTERCEPT()

### Community 142 - "Community 142"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_568stream_LINEARREG_SLOPE(), __pyx_pw_5talib_7_ta_lib_569stream_LINEARREG_SLOPE()

### Community 143 - "Community 143"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_570stream_LN(), __pyx_pw_5talib_7_ta_lib_571stream_LN()

### Community 144 - "Community 144"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_574stream_MA(), __pyx_pw_5talib_7_ta_lib_575stream_MA()

### Community 145 - "Community 145"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_576stream_MACD(), __pyx_pw_5talib_7_ta_lib_577stream_MACD()

### Community 146 - "Community 146"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_578stream_MACDEXT(), __pyx_pw_5talib_7_ta_lib_579stream_MACDEXT()

### Community 147 - "Community 147"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_582stream_MAMA(), __pyx_pw_5talib_7_ta_lib_583stream_MAMA()

### Community 148 - "Community 148"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_584stream_MAVP(), __pyx_pw_5talib_7_ta_lib_585stream_MAVP()

### Community 149 - "Community 149"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_586stream_MAX(), __pyx_pw_5talib_7_ta_lib_587stream_MAX()

### Community 150 - "Community 150"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_588stream_MAXINDEX(), __pyx_pw_5talib_7_ta_lib_589stream_MAXINDEX()

### Community 151 - "Community 151"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_590stream_MEDPRICE(), __pyx_pw_5talib_7_ta_lib_591stream_MEDPRICE()

### Community 152 - "Community 152"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_596stream_MIDPRICE(), __pyx_pw_5talib_7_ta_lib_597stream_MIDPRICE()

### Community 153 - "Community 153"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_598stream_MIN(), __pyx_pw_5talib_7_ta_lib_599stream_MIN()

### Community 154 - "Community 154"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_600stream_MININDEX(), __pyx_pw_5talib_7_ta_lib_601stream_MININDEX()

### Community 155 - "Community 155"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_602stream_MINMAX(), __pyx_pw_5talib_7_ta_lib_603stream_MINMAX()

### Community 156 - "Community 156"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_606stream_MINUS_DI(), __pyx_pw_5talib_7_ta_lib_607stream_MINUS_DI()

### Community 157 - "Community 157"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_608stream_MINUS_DM(), __pyx_pw_5talib_7_ta_lib_609stream_MINUS_DM()

### Community 158 - "Community 158"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_610stream_MOM(), __pyx_pw_5talib_7_ta_lib_611stream_MOM()

### Community 159 - "Community 159"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_612stream_MULT(), __pyx_pw_5talib_7_ta_lib_613stream_MULT()

### Community 160 - "Community 160"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_614stream_NATR(), __pyx_pw_5talib_7_ta_lib_615stream_NATR()

### Community 161 - "Community 161"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_616stream_OBV(), __pyx_pw_5talib_7_ta_lib_617stream_OBV()

### Community 162 - "Community 162"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_618stream_PLUS_DI(), __pyx_pw_5talib_7_ta_lib_619stream_PLUS_DI()

### Community 163 - "Community 163"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_620stream_PLUS_DM(), __pyx_pw_5talib_7_ta_lib_621stream_PLUS_DM()

### Community 164 - "Community 164"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_622stream_PPO(), __pyx_pw_5talib_7_ta_lib_623stream_PPO()

### Community 165 - "Community 165"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_624stream_ROC(), __pyx_pw_5talib_7_ta_lib_625stream_ROC()

### Community 166 - "Community 166"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_628stream_ROCR(), __pyx_pw_5talib_7_ta_lib_629stream_ROCR()

### Community 167 - "Community 167"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_630stream_ROCR100(), __pyx_pw_5talib_7_ta_lib_631stream_ROCR100()

### Community 168 - "Community 168"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_632stream_RSI(), __pyx_pw_5talib_7_ta_lib_633stream_RSI()

### Community 169 - "Community 169"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_634stream_SAR(), __pyx_pw_5talib_7_ta_lib_635stream_SAR()

### Community 170 - "Community 170"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_638stream_SIN(), __pyx_pw_5talib_7_ta_lib_639stream_SIN()

### Community 171 - "Community 171"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_640stream_SINH(), __pyx_pw_5talib_7_ta_lib_641stream_SINH()

### Community 172 - "Community 172"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_642stream_SMA(), __pyx_pw_5talib_7_ta_lib_643stream_SMA()

### Community 173 - "Community 173"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_644stream_SQRT(), __pyx_pw_5talib_7_ta_lib_645stream_SQRT()

### Community 174 - "Community 174"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_646stream_STDDEV(), __pyx_pw_5talib_7_ta_lib_647stream_STDDEV()

### Community 175 - "Community 175"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_648stream_STOCH(), __pyx_pw_5talib_7_ta_lib_649stream_STOCH()

### Community 176 - "Community 176"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_650stream_STOCHF(), __pyx_pw_5talib_7_ta_lib_651stream_STOCHF()

### Community 177 - "Community 177"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_652stream_STOCHRSI(), __pyx_pw_5talib_7_ta_lib_653stream_STOCHRSI()

### Community 178 - "Community 178"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_656stream_SUM(), __pyx_pw_5talib_7_ta_lib_657stream_SUM()

### Community 179 - "Community 179"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_658stream_T3(), __pyx_pw_5talib_7_ta_lib_659stream_T3()

### Community 180 - "Community 180"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_660stream_TAN(), __pyx_pw_5talib_7_ta_lib_661stream_TAN()

### Community 181 - "Community 181"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_662stream_TANH(), __pyx_pw_5talib_7_ta_lib_663stream_TANH()

### Community 182 - "Community 182"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_664stream_TEMA(), __pyx_pw_5talib_7_ta_lib_665stream_TEMA()

### Community 183 - "Community 183"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_666stream_TRANGE(), __pyx_pw_5talib_7_ta_lib_667stream_TRANGE()

### Community 184 - "Community 184"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_668stream_TRIMA(), __pyx_pw_5talib_7_ta_lib_669stream_TRIMA()

### Community 185 - "Community 185"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_670stream_TRIX(), __pyx_pw_5talib_7_ta_lib_671stream_TRIX()

### Community 186 - "Community 186"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_672stream_TSF(), __pyx_pw_5talib_7_ta_lib_673stream_TSF()

### Community 187 - "Community 187"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_674stream_TYPPRICE(), __pyx_pw_5talib_7_ta_lib_675stream_TYPPRICE()

### Community 188 - "Community 188"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_76CDLBREAKAWAY(), __pyx_pw_5talib_7_ta_lib_77CDLBREAKAWAY()

### Community 189 - "Community 189"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_78CDLCLOSINGMARUBOZU(), __pyx_pw_5talib_7_ta_lib_79CDLCLOSINGMARUBOZU()

### Community 190 - "Community 190"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_80CDLCONCEALBABYSWALL(), __pyx_pw_5talib_7_ta_lib_81CDLCONCEALBABYSWALL()

### Community 191 - "Community 191"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_82CDLCOUNTERATTACK(), __pyx_pw_5talib_7_ta_lib_83CDLCOUNTERATTACK()

### Community 192 - "Community 192"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_84CDLDARKCLOUDCOVER(), __pyx_pw_5talib_7_ta_lib_85CDLDARKCLOUDCOVER()

### Community 193 - "Community 193"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_86CDLDOJI(), __pyx_pw_5talib_7_ta_lib_87CDLDOJI()

### Community 194 - "Community 194"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_88CDLDOJISTAR(), __pyx_pw_5talib_7_ta_lib_89CDLDOJISTAR()

### Community 195 - "Community 195"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_8Function_42__repr__(), __pyx_pw_5talib_7_ta_lib_8Function_43__repr__()

### Community 196 - "Community 196"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_8Function_44__unicode__(), __pyx_pw_5talib_7_ta_lib_8Function_45__unicode__()

### Community 197 - "Community 197"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_8Function_46__str__(), __pyx_pw_5talib_7_ta_lib_8Function_47__str__()

### Community 198 - "Community 198"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_8Function_6function_flags(), __pyx_pw_5talib_7_ta_lib_8Function_7function_flags()

### Community 199 - "Community 199"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_90CDLDRAGONFLYDOJI(), __pyx_pw_5talib_7_ta_lib_91CDLDRAGONFLYDOJI()

### Community 200 - "Community 200"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_92CDLENGULFING(), __pyx_pw_5talib_7_ta_lib_93CDLENGULFING()

### Community 201 - "Community 201"
Cohesion: 1.00
Nodes (2): __pyx_pf_5talib_7_ta_lib_94CDLEVENINGDOJISTAR(), __pyx_pw_5talib_7_ta_lib_95CDLEVENINGDOJISTAR()

## Knowledge Gaps
- **2 isolated node(s):** `Returns a list of all the functions supported by TALIB`, `Returns a dict with keys of function-group names and values of lists     of func`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 44`** (2 nodes): `__Pyx_c_quot_double()`, `__pyx_t_double_complex_from_parts()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (2 nodes): `__Pyx_c_quot_float()`, `__pyx_t_float_complex_from_parts()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (2 nodes): `__Pyx_c_quot_long__double()`, `__pyx_t_long_double_complex_from_parts()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (2 nodes): `__Pyx_CyFunction_clear()`, `__Pyx__CyFunction_dealloc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (2 nodes): `__Pyx_CyFunction_get_doc()`, `__Pyx_CyFunction_get_doc_locked()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 49`** (2 nodes): `__Pyx__ExceptionSave()`, `__Pyx_PyErr_GetTopmostException()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (2 nodes): `__pyx_f_5numpy_5dtype_8subarray_subarray()`, `__pyx_f_5numpy_PyDataType_SHAPE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (2 nodes): `__Pyx_get_object_dict_version()`, `__Pyx_object_dict_version_matches()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (2 nodes): `__Pyx__IsSameCyOrCFunction()`, `__Pyx__IsSameCyOrCFunctionNoMethod()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_196EXP()`, `__pyx_pw_5talib_7_ta_lib_197EXP()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_198FLOOR()`, `__pyx_pw_5talib_7_ta_lib_199FLOOR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 55`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_2_ta_initialize()`, `__pyx_pw_5talib_7_ta_lib_3_ta_initialize()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_202HT_DCPHASE()`, `__pyx_pw_5talib_7_ta_lib_203HT_DCPHASE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_204HT_PHASOR()`, `__pyx_pw_5talib_7_ta_lib_205HT_PHASOR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_208HT_TRENDLINE()`, `__pyx_pw_5talib_7_ta_lib_209HT_TRENDLINE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 59`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_20ACOS()`, `__pyx_pw_5talib_7_ta_lib_21ACOS()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 60`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_214KAMA()`, `__pyx_pw_5talib_7_ta_lib_215KAMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_216LINEARREG()`, `__pyx_pw_5talib_7_ta_lib_217LINEARREG()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 62`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_222LINEARREG_SLOPE()`, `__pyx_pw_5talib_7_ta_lib_223LINEARREG_SLOPE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_224LN()`, `__pyx_pw_5talib_7_ta_lib_225LN()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 64`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_230MACD()`, `__pyx_pw_5talib_7_ta_lib_231MACD()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 65`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_232MACDEXT()`, `__pyx_pw_5talib_7_ta_lib_233MACDEXT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 66`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_240MAX()`, `__pyx_pw_5talib_7_ta_lib_241MAX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 67`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_242MAXINDEX()`, `__pyx_pw_5talib_7_ta_lib_243MAXINDEX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 68`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_248MIDPOINT()`, `__pyx_pw_5talib_7_ta_lib_249MIDPOINT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 69`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_24ADD()`, `__pyx_pw_5talib_7_ta_lib_25ADD()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 70`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_250MIDPRICE()`, `__pyx_pw_5talib_7_ta_lib_251MIDPRICE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 71`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_254MININDEX()`, `__pyx_pw_5talib_7_ta_lib_255MININDEX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 72`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_256MINMAX()`, `__pyx_pw_5talib_7_ta_lib_257MINMAX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 73`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_262MINUS_DM()`, `__pyx_pw_5talib_7_ta_lib_263MINUS_DM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 74`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_264MOM()`, `__pyx_pw_5talib_7_ta_lib_265MOM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 75`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_266MULT()`, `__pyx_pw_5talib_7_ta_lib_267MULT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 76`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_270OBV()`, `__pyx_pw_5talib_7_ta_lib_271OBV()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 77`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_274PLUS_DM()`, `__pyx_pw_5talib_7_ta_lib_275PLUS_DM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 78`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_276PPO()`, `__pyx_pw_5talib_7_ta_lib_277PPO()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 79`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_280ROCP()`, `__pyx_pw_5talib_7_ta_lib_281ROCP()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 80`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_282ROCR()`, `__pyx_pw_5talib_7_ta_lib_283ROCR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 81`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_284ROCR100()`, `__pyx_pw_5talib_7_ta_lib_285ROCR100()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 82`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_286RSI()`, `__pyx_pw_5talib_7_ta_lib_287RSI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 83`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_288SAR()`, `__pyx_pw_5talib_7_ta_lib_289SAR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 84`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_28ADX()`, `__pyx_pw_5talib_7_ta_lib_29ADX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 85`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_290SAREXT()`, `__pyx_pw_5talib_7_ta_lib_291SAREXT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 86`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_294SINH()`, `__pyx_pw_5talib_7_ta_lib_295SINH()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 87`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_296SMA()`, `__pyx_pw_5talib_7_ta_lib_297SMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 88`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_298SQRT()`, `__pyx_pw_5talib_7_ta_lib_299SQRT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 89`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_300STDDEV()`, `__pyx_pw_5talib_7_ta_lib_301STDDEV()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 90`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_302STOCH()`, `__pyx_pw_5talib_7_ta_lib_303STOCH()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 91`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_304STOCHF()`, `__pyx_pw_5talib_7_ta_lib_305STOCHF()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 92`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_306STOCHRSI()`, `__pyx_pw_5talib_7_ta_lib_307STOCHRSI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 93`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_308SUB()`, `__pyx_pw_5talib_7_ta_lib_309SUB()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 94`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_30ADXR()`, `__pyx_pw_5talib_7_ta_lib_31ADXR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 95`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_312T3()`, `__pyx_pw_5talib_7_ta_lib_313T3()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 96`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_314TAN()`, `__pyx_pw_5talib_7_ta_lib_315TAN()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 97`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_316TANH()`, `__pyx_pw_5talib_7_ta_lib_317TANH()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 98`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_318TEMA()`, `__pyx_pw_5talib_7_ta_lib_319TEMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 99`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_320TRANGE()`, `__pyx_pw_5talib_7_ta_lib_321TRANGE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 100`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_322TRIMA()`, `__pyx_pw_5talib_7_ta_lib_323TRIMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 101`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_326TSF()`, `__pyx_pw_5talib_7_ta_lib_327TSF()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 102`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_328TYPPRICE()`, `__pyx_pw_5talib_7_ta_lib_329TYPPRICE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 103`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_32APO()`, `__pyx_pw_5talib_7_ta_lib_33APO()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 104`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_330ULTOSC()`, `__pyx_pw_5talib_7_ta_lib_331ULTOSC()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 105`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_332VAR()`, `__pyx_pw_5talib_7_ta_lib_333VAR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 106`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_334WCLPRICE()`, `__pyx_pw_5talib_7_ta_lib_335WCLPRICE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 107`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_336WILLR()`, `__pyx_pw_5talib_7_ta_lib_337WILLR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 108`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_338WMA()`, `__pyx_pw_5talib_7_ta_lib_339WMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 109`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_340str2bytes()`, `__pyx_pw_5talib_7_ta_lib_341str2bytes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 110`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_342bytes2str()`, `__pyx_pw_5talib_7_ta_lib_343bytes2str()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 111`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_344str2bytes()`, `__pyx_pw_5talib_7_ta_lib_345str2bytes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 112`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_346bytes2str()`, `__pyx_pw_5talib_7_ta_lib_347bytes2str()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 113`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_348_ta_getGroupTable()`, `__pyx_pw_5talib_7_ta_lib_349_ta_getGroupTable()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 114`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_34AROON()`, `__pyx_pw_5talib_7_ta_lib_35AROON()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 115`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_350_ta_getFuncTable()`, `__pyx_pw_5talib_7_ta_lib_351_ta_getFuncTable()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 116`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_366stream_ACOS()`, `__pyx_pw_5talib_7_ta_lib_367stream_ACOS()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 117`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_378stream_APO()`, `__pyx_pw_5talib_7_ta_lib_379stream_APO()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 118`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_384stream_ASIN()`, `__pyx_pw_5talib_7_ta_lib_385stream_ASIN()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 119`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_386stream_ATAN()`, `__pyx_pw_5talib_7_ta_lib_387stream_ATAN()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 120`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_392stream_AVGDEV()`, `__pyx_pw_5talib_7_ta_lib_393stream_AVGDEV()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 121`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_394stream_BBANDS()`, `__pyx_pw_5talib_7_ta_lib_395stream_BBANDS()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 122`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_4_ta_shutdown()`, `__pyx_pw_5talib_7_ta_lib_5_ta_shutdown()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 123`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_400stream_CCI()`, `__pyx_pw_5talib_7_ta_lib_401stream_CCI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 124`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_46AVGDEV()`, `__pyx_pw_5talib_7_ta_lib_47AVGDEV()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 125`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_524stream_CEIL()`, `__pyx_pw_5talib_7_ta_lib_525stream_CEIL()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 126`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_526stream_CMO()`, `__pyx_pw_5talib_7_ta_lib_527stream_CMO()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 127`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_528stream_CORREL()`, `__pyx_pw_5talib_7_ta_lib_529stream_CORREL()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 128`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_530stream_COS()`, `__pyx_pw_5talib_7_ta_lib_531stream_COS()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 129`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_534stream_DEMA()`, `__pyx_pw_5talib_7_ta_lib_535stream_DEMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 130`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_536stream_DIV()`, `__pyx_pw_5talib_7_ta_lib_537stream_DIV()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 131`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_538stream_DX()`, `__pyx_pw_5talib_7_ta_lib_539stream_DX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 132`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_540stream_EMA()`, `__pyx_pw_5talib_7_ta_lib_541stream_EMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 133`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_544stream_FLOOR()`, `__pyx_pw_5talib_7_ta_lib_545stream_FLOOR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 134`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_546stream_HT_DCPERIOD()`, `__pyx_pw_5talib_7_ta_lib_547stream_HT_DCPERIOD()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 135`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_550stream_HT_PHASOR()`, `__pyx_pw_5talib_7_ta_lib_551stream_HT_PHASOR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 136`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_552stream_HT_SINE()`, `__pyx_pw_5talib_7_ta_lib_553stream_HT_SINE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 137`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_554stream_HT_TRENDLINE()`, `__pyx_pw_5talib_7_ta_lib_555stream_HT_TRENDLINE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 138`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_558stream_IMI()`, `__pyx_pw_5talib_7_ta_lib_559stream_IMI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 139`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_560stream_KAMA()`, `__pyx_pw_5talib_7_ta_lib_561stream_KAMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 140`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_562stream_LINEARREG()`, `__pyx_pw_5talib_7_ta_lib_563stream_LINEARREG()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 141`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_566stream_LINEARREG_INTERCEPT()`, `__pyx_pw_5talib_7_ta_lib_567stream_LINEARREG_INTERCEPT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 142`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_568stream_LINEARREG_SLOPE()`, `__pyx_pw_5talib_7_ta_lib_569stream_LINEARREG_SLOPE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 143`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_570stream_LN()`, `__pyx_pw_5talib_7_ta_lib_571stream_LN()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 144`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_574stream_MA()`, `__pyx_pw_5talib_7_ta_lib_575stream_MA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 145`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_576stream_MACD()`, `__pyx_pw_5talib_7_ta_lib_577stream_MACD()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 146`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_578stream_MACDEXT()`, `__pyx_pw_5talib_7_ta_lib_579stream_MACDEXT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 147`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_582stream_MAMA()`, `__pyx_pw_5talib_7_ta_lib_583stream_MAMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 148`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_584stream_MAVP()`, `__pyx_pw_5talib_7_ta_lib_585stream_MAVP()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 149`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_586stream_MAX()`, `__pyx_pw_5talib_7_ta_lib_587stream_MAX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 150`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_588stream_MAXINDEX()`, `__pyx_pw_5talib_7_ta_lib_589stream_MAXINDEX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 151`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_590stream_MEDPRICE()`, `__pyx_pw_5talib_7_ta_lib_591stream_MEDPRICE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 152`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_596stream_MIDPRICE()`, `__pyx_pw_5talib_7_ta_lib_597stream_MIDPRICE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 153`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_598stream_MIN()`, `__pyx_pw_5talib_7_ta_lib_599stream_MIN()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 154`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_600stream_MININDEX()`, `__pyx_pw_5talib_7_ta_lib_601stream_MININDEX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 155`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_602stream_MINMAX()`, `__pyx_pw_5talib_7_ta_lib_603stream_MINMAX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 156`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_606stream_MINUS_DI()`, `__pyx_pw_5talib_7_ta_lib_607stream_MINUS_DI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 157`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_608stream_MINUS_DM()`, `__pyx_pw_5talib_7_ta_lib_609stream_MINUS_DM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 158`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_610stream_MOM()`, `__pyx_pw_5talib_7_ta_lib_611stream_MOM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 159`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_612stream_MULT()`, `__pyx_pw_5talib_7_ta_lib_613stream_MULT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 160`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_614stream_NATR()`, `__pyx_pw_5talib_7_ta_lib_615stream_NATR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 161`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_616stream_OBV()`, `__pyx_pw_5talib_7_ta_lib_617stream_OBV()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 162`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_618stream_PLUS_DI()`, `__pyx_pw_5talib_7_ta_lib_619stream_PLUS_DI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 163`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_620stream_PLUS_DM()`, `__pyx_pw_5talib_7_ta_lib_621stream_PLUS_DM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 164`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_622stream_PPO()`, `__pyx_pw_5talib_7_ta_lib_623stream_PPO()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 165`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_624stream_ROC()`, `__pyx_pw_5talib_7_ta_lib_625stream_ROC()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 166`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_628stream_ROCR()`, `__pyx_pw_5talib_7_ta_lib_629stream_ROCR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 167`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_630stream_ROCR100()`, `__pyx_pw_5talib_7_ta_lib_631stream_ROCR100()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 168`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_632stream_RSI()`, `__pyx_pw_5talib_7_ta_lib_633stream_RSI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 169`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_634stream_SAR()`, `__pyx_pw_5talib_7_ta_lib_635stream_SAR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 170`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_638stream_SIN()`, `__pyx_pw_5talib_7_ta_lib_639stream_SIN()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 171`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_640stream_SINH()`, `__pyx_pw_5talib_7_ta_lib_641stream_SINH()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 172`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_642stream_SMA()`, `__pyx_pw_5talib_7_ta_lib_643stream_SMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 173`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_644stream_SQRT()`, `__pyx_pw_5talib_7_ta_lib_645stream_SQRT()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 174`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_646stream_STDDEV()`, `__pyx_pw_5talib_7_ta_lib_647stream_STDDEV()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 175`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_648stream_STOCH()`, `__pyx_pw_5talib_7_ta_lib_649stream_STOCH()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 176`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_650stream_STOCHF()`, `__pyx_pw_5talib_7_ta_lib_651stream_STOCHF()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 177`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_652stream_STOCHRSI()`, `__pyx_pw_5talib_7_ta_lib_653stream_STOCHRSI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 178`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_656stream_SUM()`, `__pyx_pw_5talib_7_ta_lib_657stream_SUM()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 179`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_658stream_T3()`, `__pyx_pw_5talib_7_ta_lib_659stream_T3()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 180`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_660stream_TAN()`, `__pyx_pw_5talib_7_ta_lib_661stream_TAN()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 181`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_662stream_TANH()`, `__pyx_pw_5talib_7_ta_lib_663stream_TANH()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 182`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_664stream_TEMA()`, `__pyx_pw_5talib_7_ta_lib_665stream_TEMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 183`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_666stream_TRANGE()`, `__pyx_pw_5talib_7_ta_lib_667stream_TRANGE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 184`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_668stream_TRIMA()`, `__pyx_pw_5talib_7_ta_lib_669stream_TRIMA()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 185`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_670stream_TRIX()`, `__pyx_pw_5talib_7_ta_lib_671stream_TRIX()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 186`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_672stream_TSF()`, `__pyx_pw_5talib_7_ta_lib_673stream_TSF()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 187`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_674stream_TYPPRICE()`, `__pyx_pw_5talib_7_ta_lib_675stream_TYPPRICE()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 188`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_76CDLBREAKAWAY()`, `__pyx_pw_5talib_7_ta_lib_77CDLBREAKAWAY()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 189`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_78CDLCLOSINGMARUBOZU()`, `__pyx_pw_5talib_7_ta_lib_79CDLCLOSINGMARUBOZU()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_80CDLCONCEALBABYSWALL()`, `__pyx_pw_5talib_7_ta_lib_81CDLCONCEALBABYSWALL()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 191`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_82CDLCOUNTERATTACK()`, `__pyx_pw_5talib_7_ta_lib_83CDLCOUNTERATTACK()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 192`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_84CDLDARKCLOUDCOVER()`, `__pyx_pw_5talib_7_ta_lib_85CDLDARKCLOUDCOVER()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 193`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_86CDLDOJI()`, `__pyx_pw_5talib_7_ta_lib_87CDLDOJI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 194`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_88CDLDOJISTAR()`, `__pyx_pw_5talib_7_ta_lib_89CDLDOJISTAR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 195`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_8Function_42__repr__()`, `__pyx_pw_5talib_7_ta_lib_8Function_43__repr__()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 196`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_8Function_44__unicode__()`, `__pyx_pw_5talib_7_ta_lib_8Function_45__unicode__()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 197`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_8Function_46__str__()`, `__pyx_pw_5talib_7_ta_lib_8Function_47__str__()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 198`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_8Function_6function_flags()`, `__pyx_pw_5talib_7_ta_lib_8Function_7function_flags()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 199`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_90CDLDRAGONFLYDOJI()`, `__pyx_pw_5talib_7_ta_lib_91CDLDRAGONFLYDOJI()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 200`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_92CDLENGULFING()`, `__pyx_pw_5talib_7_ta_lib_93CDLENGULFING()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 201`** (2 nodes): `__pyx_pf_5talib_7_ta_lib_94CDLEVENINGDOJISTAR()`, `__pyx_pw_5talib_7_ta_lib_95CDLEVENINGDOJISTAR()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `__Pyx_AddTraceback()` connect `Community 8` to `Community 0`, `Community 9`, `Community 4`, `Community 6`, `Community 17`, `Community 18`, `Community 1`, `Community 24`, `Community 2`, `Community 5`, `Community 10`, `Community 7`, `Community 11`, `Community 23`, `Community 19`, `Community 20`, `Community 53`, `Community 54`, `Community 56`, `Community 57`, `Community 58`, `Community 59`, `Community 60`, `Community 61`, `Community 3`, `Community 62`, `Community 63`, `Community 64`, `Community 65`, `Community 66`, `Community 67`, `Community 68`, `Community 69`, `Community 70`, `Community 71`, `Community 72`, `Community 73`, `Community 74`, `Community 75`, `Community 76`, `Community 77`, `Community 78`, `Community 79`, `Community 80`, `Community 81`, `Community 82`, `Community 83`, `Community 84`, `Community 85`, `Community 86`, `Community 87`, `Community 88`, `Community 55`, `Community 89`, `Community 90`, `Community 91`, `Community 92`, `Community 93`, `Community 94`, `Community 95`, `Community 96`, `Community 97`, `Community 98`, `Community 99`, `Community 100`, `Community 101`, `Community 102`, `Community 103`, `Community 104`, `Community 105`, `Community 106`, `Community 107`, `Community 108`, `Community 109`, `Community 110`, `Community 113`, `Community 114`, `Community 115`, `Community 21`, `Community 13`, `Community 116`, `Community 117`, `Community 118`, `Community 119`, `Community 120`, `Community 121`, `Community 123`, `Community 124`, `Community 122`, `Community 125`, `Community 126`, `Community 127`, `Community 128`, `Community 129`, `Community 130`, `Community 131`, `Community 132`, `Community 133`, `Community 134`, `Community 135`, `Community 136`, `Community 137`, `Community 138`, `Community 139`, `Community 140`, `Community 141`, `Community 142`, `Community 143`, `Community 144`, `Community 145`, `Community 146`, `Community 147`, `Community 148`, `Community 149`, `Community 150`, `Community 151`, `Community 152`, `Community 153`, `Community 154`, `Community 155`, `Community 156`, `Community 157`, `Community 158`, `Community 159`, `Community 160`, `Community 161`, `Community 162`, `Community 163`, `Community 164`, `Community 165`, `Community 166`, `Community 167`, `Community 168`, `Community 169`, `Community 170`, `Community 171`, `Community 172`, `Community 173`, `Community 174`, `Community 175`, `Community 176`, `Community 177`, `Community 178`, `Community 179`, `Community 180`, `Community 181`, `Community 182`, `Community 183`, `Community 184`, `Community 185`, `Community 186`, `Community 187`, `Community 188`, `Community 189`, `Community 14`, `Community 190`, `Community 191`, `Community 192`, `Community 193`, `Community 194`, `Community 16`, `Community 195`, `Community 196`, `Community 197`, `Community 198`, `Community 199`, `Community 200`, `Community 201`, `Community 111`, `Community 112`, `Community 25`, `Community 28`?**
  _High betweenness centrality (0.167) - this node is a cross-community bridge._
- **Why does `__Pyx_ParseKeywords()` connect `Community 28` to `Community 0`, `Community 33`, `Community 2`, `Community 8`, `Community 6`, `Community 1`, `Community 7`, `Community 5`, `Community 11`, `Community 23`, `Community 24`, `Community 19`, `Community 20`, `Community 53`, `Community 54`, `Community 56`, `Community 57`, `Community 58`, `Community 60`, `Community 61`, `Community 59`, `Community 3`, `Community 62`, `Community 63`, `Community 64`, `Community 65`, `Community 17`, `Community 66`, `Community 67`, `Community 68`, `Community 70`, `Community 71`, `Community 72`, `Community 69`, `Community 73`, `Community 74`, `Community 75`, `Community 18`, `Community 76`, `Community 77`, `Community 78`, `Community 79`, `Community 80`, `Community 81`, `Community 82`, `Community 83`, `Community 85`, `Community 86`, `Community 87`, `Community 88`, `Community 84`, `Community 89`, `Community 90`, `Community 91`, `Community 92`, `Community 93`, `Community 95`, `Community 96`, `Community 97`, `Community 98`, `Community 94`, `Community 99`, `Community 100`, `Community 101`, `Community 102`, `Community 104`, `Community 105`, `Community 106`, `Community 107`, `Community 108`, `Community 103`, `Community 109`, `Community 110`, `Community 111`, `Community 112`, `Community 115`, `Community 10`, `Community 114`, `Community 25`, `Community 116`, `Community 117`, `Community 118`, `Community 119`, `Community 120`, `Community 121`, `Community 123`, `Community 124`, `Community 125`, `Community 126`, `Community 127`, `Community 128`, `Community 129`, `Community 130`, `Community 131`, `Community 132`, `Community 133`, `Community 134`, `Community 135`, `Community 136`, `Community 137`, `Community 138`, `Community 139`, `Community 140`, `Community 141`, `Community 142`, `Community 143`, `Community 144`, `Community 145`, `Community 146`, `Community 147`, `Community 148`, `Community 149`, `Community 150`, `Community 151`, `Community 152`, `Community 153`, `Community 154`, `Community 155`, `Community 156`, `Community 157`, `Community 158`, `Community 159`, `Community 160`, `Community 161`, `Community 162`, `Community 163`, `Community 164`, `Community 165`, `Community 166`, `Community 167`, `Community 168`, `Community 169`, `Community 170`, `Community 171`, `Community 172`, `Community 173`, `Community 174`, `Community 175`, `Community 176`, `Community 177`, `Community 178`, `Community 179`, `Community 180`, `Community 181`, `Community 182`, `Community 183`, `Community 184`, `Community 185`, `Community 186`, `Community 187`, `Community 188`, `Community 189`, `Community 13`, `Community 190`, `Community 191`, `Community 192`, `Community 193`, `Community 194`, `Community 16`, `Community 14`, `Community 21`, `Community 195`, `Community 196`, `Community 197`, `Community 198`, `Community 199`, `Community 200`, `Community 201`?**
  _High betweenness centrality (0.026) - this node is a cross-community bridge._
- **Why does `__Pyx_RaiseArgtupleInvalid()` connect `Community 25` to `Community 0`, `Community 2`, `Community 8`, `Community 6`, `Community 1`, `Community 7`, `Community 5`, `Community 11`, `Community 23`, `Community 24`, `Community 19`, `Community 20`, `Community 53`, `Community 54`, `Community 56`, `Community 57`, `Community 58`, `Community 60`, `Community 61`, `Community 59`, `Community 3`, `Community 62`, `Community 63`, `Community 64`, `Community 65`, `Community 17`, `Community 66`, `Community 67`, `Community 68`, `Community 70`, `Community 71`, `Community 72`, `Community 69`, `Community 73`, `Community 74`, `Community 75`, `Community 18`, `Community 76`, `Community 77`, `Community 78`, `Community 79`, `Community 80`, `Community 81`, `Community 82`, `Community 83`, `Community 85`, `Community 86`, `Community 87`, `Community 88`, `Community 84`, `Community 89`, `Community 90`, `Community 91`, `Community 92`, `Community 93`, `Community 95`, `Community 96`, `Community 97`, `Community 98`, `Community 94`, `Community 99`, `Community 100`, `Community 101`, `Community 102`, `Community 104`, `Community 105`, `Community 106`, `Community 107`, `Community 108`, `Community 103`, `Community 109`, `Community 110`, `Community 111`, `Community 112`, `Community 115`, `Community 10`, `Community 114`, `Community 116`, `Community 117`, `Community 118`, `Community 119`, `Community 120`, `Community 121`, `Community 123`, `Community 124`, `Community 125`, `Community 126`, `Community 127`, `Community 128`, `Community 129`, `Community 130`, `Community 131`, `Community 132`, `Community 133`, `Community 134`, `Community 135`, `Community 136`, `Community 137`, `Community 138`, `Community 139`, `Community 140`, `Community 141`, `Community 142`, `Community 143`, `Community 144`, `Community 145`, `Community 146`, `Community 147`, `Community 148`, `Community 149`, `Community 150`, `Community 151`, `Community 152`, `Community 153`, `Community 154`, `Community 155`, `Community 156`, `Community 157`, `Community 158`, `Community 159`, `Community 160`, `Community 161`, `Community 162`, `Community 163`, `Community 164`, `Community 165`, `Community 166`, `Community 167`, `Community 168`, `Community 169`, `Community 170`, `Community 171`, `Community 172`, `Community 173`, `Community 174`, `Community 175`, `Community 176`, `Community 177`, `Community 178`, `Community 179`, `Community 180`, `Community 181`, `Community 182`, `Community 183`, `Community 184`, `Community 185`, `Community 186`, `Community 187`, `Community 188`, `Community 189`, `Community 13`, `Community 190`, `Community 191`, `Community 192`, `Community 193`, `Community 194`, `Community 16`, `Community 14`, `Community 28`, `Community 21`, `Community 195`, `Community 196`, `Community 197`, `Community 198`, `Community 199`, `Community 200`, `Community 201`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **What connects `Returns a list of all the functions supported by TALIB`, `Returns a dict with keys of function-group names and values of lists     of func` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.021739130434782608 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.03327596098680436 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.037296037296037296 - nodes in this community are weakly interconnected._