# Graph Report - .  (2026-07-29)

## Corpus Check
- cluster-only mode - file stats not available

## Summary
- 2952 nodes · 5138 edges · 134 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output
- Edge kinds: contains: 1956 · imports: 1326 · calls: 1138 · rationale_for: 279 · method: 252 · imports_from: 167 · inherits: 20


## Graph Freshness
- Built from Git commit: `f9bf8d1`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `_safe_call()` - 67 edges
2. `Dataset` - 52 edges
3. `Booster` - 43 edges
4. `_AssertBoosterHandleNotNull()` - 34 edges
5. `_c_str()` - 32 edges
6. `LGBMModel` - 29 edges
7. `_create_data()` - 26 edges
8. `dummy_dataset_params()` - 21 edges
9. `LightGBMError` - 19 edges
10. `_InnerPredictor` - 19 edges

## Surprising Connections (you probably didn't know these)
- `CUDABestSplitFinder` --calls--> `InitFeatureMetaInfo()`  [EXTRACTED]
  src/treelearner/cuda/cuda_best_split_finder.hpp → src/treelearner/cuda/cuda_best_split_finder.cpp
- `CUDADataPartition` --calls--> `CalcBlockDim()`  [EXTRACTED]
  src/treelearner/cuda/cuda_data_partition.hpp → src/treelearner/cuda/cuda_data_partition.cpp
- `CUDAHistogramConstructor` --calls--> `InitFeatureMetaInfo()`  [EXTRACTED]
  src/treelearner/cuda/cuda_histogram_constructor.hpp → src/treelearner/cuda/cuda_histogram_constructor.cpp
- `CUDAScoreUpdater` --calls--> `InitCUDA()`  [EXTRACTED]
  src/boosting/cuda/cuda_score_updater.hpp → src/boosting/cuda/cuda_score_updater.cpp

## Communities

### Community 0 - "Community 0"
Cohesion: 0.02
Nodes (2): psutil, # NOTE: this was passed in with alias 'sub_row'

### Community 1 - "Community 1"
Cohesion: 0.03
Nodes (45): binary_error(), constant_metric(), _create_data(), decreasing_metric(), ExtendedLGBMClassifier, ExtendedLGBMRanker, ExtendedLGBMRegressor, mse() (+37 more)

### Community 2 - "Community 2"
Cohesion: 0.02
Nodes (5): alternate_shared_mutex, predictor, Booster, SingleRowPredictorInner, yamc_shared_lock

### Community 3 - "Community 3"
Cohesion: 0.04
Nodes (65): basic, callback, collections, compat, concurrent_futures, copy, dask, executable() (+57 more)

### Community 4 - "Community 4"
Cohesion: 0.04
Nodes (38): Booster, _dump_pandas_categorical(), _get_sample_count(), _load_pandas_categorical(), Get the index of the current iteration.          Returns         -------, Get an array of randomly chosen indices from this ``Dataset``.          Indices, Add rows to Dataset.          Parameters         ----------         data : numpy, Check the return value from C API call.      Parameters     ----------     ret : (+30 more)

### Community 5 - "Community 5"
Cohesion: 0.05
Nodes (38): _c_str(), Dataset, _log_warning(), _np2d_to_np1d(), _param_dict_to_str(), Dataset in LightGBM.      LightGBM does not train on raw data.     It discretize, Initialize Dataset.          Parameters         ----------         data : str, p, Create dataset from a reference dataset.          Parameters         ---------- (+30 more)

### Community 6 - "Community 6"
Cohesion: 0.04
Nodes (12): numbers, _create_sequence_from_ndarray(), NumpySequence, # NOTE: max_depth < 5 is significant here because the default for num_leaves=31., # NOTE: "position" is converted to int32 on the C++ side and remapped to dense, # NOTE: this intentionally contains values where num_leaves <, ==, and > (max_de, Test that Booster.rollback_one_iter() correctly rolls back one boosting iteratio, test_add_features_from_different_sources() (+4 more)

### Community 7 - "Community 7"
Cohesion: 0.05
Nodes (21): algorithm, bin, cstdint, CUDAGradientDiscretizer, data_partition, feature_group, feature_histogram, gradient_discretizer (+13 more)

### Community 8 - "Community 8"
Cohesion: 0.05
Nodes (47): abc, FutureWarning, libpath, _c_array(), _cast_numpy_array_to_dtype(), _cfloat32_array_to_numpy(), _cfloat64_array_to_numpy(), _check_for_bad_pandas_dtypes() (+39 more)

### Community 9 - "Community 9"
Cohesion: 0.05
Nodes (30): array_args, ScoreUpdater, config, CUDAObjectiveInterface, CUDASplitInfo, NCCLGBDTComponent, cuda_score_updater, dataset (+22 more)

### Community 10 - "Community 10"
Cohesion: 0.06
Nodes (37): dask_array_utils, dask_dataframe, dask_distributed, itertools, _accuracy_score(), _create_data(), _create_ranking_data(), _get_workers_hostname() (+29 more)

### Community 11 - "Community 11"
Cohesion: 0.05
Nodes (21): common, file_io, log, metric, AUCMetric, AveragePrecisionMetric, BinaryErrorMetric, BinaryLoglossMetric (+13 more)

### Community 12 - "Community 12"
Cohesion: 0.06
Nodes (28): Application(), InitTrain(), LoadData(), LoadParameters(), Predictor, boosting, BaggingSampleStrategy, CreateBoosting() (+20 more)

### Community 13 - "Community 13"
Cohesion: 0.08
Nodes (32): _c_float_array(), _c_int_array(), _convert_from_sliced_object(), _extract_arrow_stream_capsule_pointer(), _InnerPredictor, _is_1d_collection(), _is_1d_list(), _is_numpy_1d_array() (+24 more)

### Community 14 - "Community 14"
Cohesion: 0.04
Nodes (6): at, can, objective, objectives, probabilities, with

### Community 15 - "Community 15"
Cohesion: 0.05
Nodes (9): altrep, error, lightgbm_r, rdynload, rinternals, _BoosterFinalizer(), _DatasetFinalizer(), LGBM_BoosterFree_R() (+1 more)

### Community 16 - "Community 16"
Cohesion: 0.08
Nodes (26): AddFeaturesFrom(), Construct(), CopySubrow(), CopySubrowHostPart(), CopySubrowToDevice(), CreateCUDAColumnData(), FastFeatureBundling(), FindGroups() (+18 more)

### Community 17 - "Community 17"
Cohesion: 0.07
Nodes (30): LGBMClassifier, LGBMRanker, LGBMRegressor, DaskLGBMClassifier, _DaskLGBMModel, DaskLGBMRanker, DaskLGBMRegressor, _get_dask_client() (+22 more)

### Community 18 - "Community 18"
Cohesion: 0.09
Nodes (31): array, MakePrimitiveSchema(), MakeStream(), MakeStructSchema(), TEST(), CalculateQueryBoundaries(), CalculateQueryWeights(), CheckOrPartition() (+23 more)

### Community 19 - "Community 19"
Cohesion: 0.07
Nodes (25): binary_objective, cuda_binary_objective, CUDABinaryLogloss, CUDAMulticlassOVA, CUDAMulticlassSoftmax, CUDALambdarankNDCG, CUDALambdaRankObjectiveInterface, CUDARankXENDCG (+17 more)

### Community 20 - "Community 20"
Cohesion: 0.09
Nodes (29): dataclasses, functools, CallbackEnv, early_stopping(), EarlyStopException, _EarlyStoppingCallback, _format_eval_result(), _is_using_cv() (+21 more)

### Community 21 - "Community 21"
Cohesion: 0.07
Nodes (17): CreateBinary(), CreateMulticlass(), CreateNone(), CreatePredictionEarlyStopInstance(), cmath, AtofPreciseTest, NCCLTopology, functional (+9 more)

### Community 22 - "Community 22"
Cohesion: 0.08
Nodes (17): arrow, binary_writer, cstdarg, cstdlib, cstring, export, LastErrorMsg(), LGBM_SetLastError() (+9 more)

### Community 23 - "Community 23"
Cohesion: 0.06
Nodes (10): fast_double_parser, format, intrin, iterator, malloc, mm_malloc, stdlib, type_traits (+2 more)

### Community 24 - "Community 24"
Cohesion: 0.09
Nodes (19): application, byte_buffer, c_api, TEST(), test_predict_type(), TEST(), test_stream_dense(), test_stream_sparse() (+11 more)

### Community 25 - "Community 25"
Cohesion: 0.14
Nodes (30): dummy_dataset_params(), generate_dummy_pandas_frame(), generate_random_pandas_frame(), generate_random_pandas_series(), generate_simple_pandas_frame(), test_categorical_encoding_registered_but_unobserved(), test_categorical_with_missing_values(), test_dataset_construct_fields_fuzzy() (+22 more)

### Community 26 - "Community 26"
Cohesion: 0.08
Nodes (22): parallel_tree_learner, BeforeTrain(), DataParallelTreeLearner<GPUTreeLearner>, DataParallelTreeLearner<SerialTreeLearner>, FindBestSplits(), FindBestSplitsFromHistograms(), Init(), PrepareBufferPos() (+14 more)

### Community 27 - "Community 27"
Cohesion: 0.06
Nodes (2): and, handles

### Community 28 - "Community 28"
Cohesion: 0.10
Nodes (19): bagging, BoostFromAverage(), Boosting(), EvalAndCheckEarlyStopping(), EvalOneMetric(), GetEvalAt(), GetPredictAt(), GetTrainingScore() (+11 more)

### Community 29 - "Community 29"
Cohesion: 0.08
Nodes (23): BinMapper(), CopyFrom(), CreateMultiValBin(), CreateMultiValDenseBin(), CreateMultiValSparseBin(), DenseBin<uint16_t, false>, DenseBin<uint32_t, false>, DenseBin<uint8_t, false> (+15 more)

### Community 30 - "Community 30"
Cohesion: 0.17
Nodes (27): assert_equal_predict_arrow_pandas(), dummy_dataset_params(), generate_dummy_arrow_table(), generate_random_arrow_array(), generate_random_arrow_table(), generate_simple_arrow_table(), pyarrow_array_equal(), Similar to ``np.array_equal()``, but for ``pyarrow.Array`` objects.      ``pyarr (+19 more)

### Community 31 - "Community 31"
Cohesion: 0.09
Nodes (29): _AssertBoosterHandleNotNull(), GetPredictType(), LGBM_BoosterCalcNumPredict_R(), LGBM_BoosterGetCurrentIteration_R(), LGBM_BoosterGetEval_R(), LGBM_BoosterGetLowerBoundValue_R(), LGBM_BoosterGetNumClasses_R(), LGBM_BoosterGetNumFeature_R() (+21 more)

### Community 32 - "Community 32"
Cohesion: 0.08
Nodes (18): cloudpickle, filecmp, joblib, assert_all_trees_valid(), assert_silent(), assert_subtree_valid(), BuildInfo, make_ranking() (+10 more)

### Community 33 - "Community 33"
Cohesion: 0.08
Nodes (15): Exception, _is_list_of_sequences(), LightGBMError, Error thrown by LightGBM., Sample data from seqs.          Mimics behavior in c_api.cpp:LGBM_DatasetCreateF, Set categorical features.          Parameters         ----------         categor, Set predictor for continued training.          It is not recommended for user to, Set reference Dataset.          Parameters         ----------         reference (+7 more)

### Community 34 - "Community 34"
Cohesion: 0.09
Nodes (19): _agg_cv_result(), _choose_num_iterations(), cv(), CVBooster, _make_n_folds(), Perform the training with given parameters.      Parameters     ----------     p, CVBooster in LightGBM.      Auxiliary data structure to hold and redirect all bo, Initialize the CVBooster.          Parameters         ----------         model_f (+11 more)

### Community 35 - "Community 35"
Cohesion: 0.19
Nodes (25): assert_equal_predict_polars_pandas(), dummy_dataset_params(), generate_dummy_polars_frame(), generate_random_polars_frame(), generate_random_polars_series(), generate_simple_polars_frame(), test_dataset_construct_fields_fuzzy(), test_dataset_construct_fuzzy_boolean() (+17 more)

### Community 36 - "Community 36"
Cohesion: 0.12
Nodes (20): aligned_allocator, core, dense_bin, leaf_splits, AllocateGPUMemory(), BuildGPUKernels(), CompareHistograms(), ConstructGPUHistogramsAsync() (+12 more)

### Community 37 - "Community 37"
Cohesion: 0.10
Nodes (11): cctype, CheckLinker(), Construct(), Linkers(), ListenThread(), ParseMachineList(), PrintLinkers(), SetLinker() (+3 more)

### Community 38 - "Community 38"
Cohesion: 0.08
Nodes (9): ctypes, _find_lib_path(), Find the path to LightGBM library files.      Returns     -------     lib_path:, logging, os, platform, pytest, unittest_mock (+1 more)

### Community 39 - "Community 39"
Cohesion: 0.15
Nodes (20): col_sampler, cost_effective_gradient_boosting, queue, BeforeFindBestSplit(), BeforeTrain(), CheckSplit(), ComputeBestSplitForFeature(), ConstructHistograms() (+12 more)

### Community 40 - "Community 40"
Cohesion: 0.08
Nodes (4): monotone_constraints, FeatureHistogram, FeatureMetainfo, HistogramPool

### Community 41 - "Community 41"
Cohesion: 0.09
Nodes (4): cuda, CUDARandom, cuda_runtime, stdio

### Community 42 - "Community 42"
Cohesion: 0.15
Nodes (13): dask_array, distributed, lightgbm, matplotlib_pyplot, pandas, experiment(), log_loss(), Logarithmic loss with non-necessarily-binary labels. (+5 more)

### Community 43 - "Community 43"
Cohesion: 0.09
Nodes (20): _LGBMClassifierBase, _LGBMModelBase, _LGBMRegressorBase, pd_CategoricalDtype, pd_DataFrame, pd_Series, Dummy class for sklearn.base.BaseEstimator., Dummy class for sklearn.base.ClassifierMixin. (+12 more)

### Community 44 - "Community 44"
Cohesion: 0.09
Nodes (21): datetime, Directive, generate_doxygen_xml(), generate_r_docs(), IgnoredDirective, Generate XML documentation for C API by Doxygen.      Parameters     ----------, Generate documentation for R-package.      Parameters     ----------     app : s, Make reference to R-package documentation point to the actual version.      Para (+13 more)

### Community 45 - "Community 45"
Cohesion: 0.10
Nodes (14): dump(), esc(), fail(), has_shape(), Json(), JsonArray, JsonBoolean, JsonDouble (+6 more)

### Community 47 - "Community 47"
Cohesion: 0.13
Nodes (15): create_data(), DistributedMockup, Write all training data as train.txt and each training partition as train{i}.txt, Run the distributed training process on a single machine.          For each work, Compute the predictions using the model created in the fit step.          predic, Create a file train{i}.conf with the required configuration to train.          E, Test the classification task., Test the regression task. (+7 more)

### Community 48 - "Community 48"
Cohesion: 0.12
Nodes (14): binary_metric, cuda_binary_metric, CUDABinaryErrorMetric, CUDABinaryLoglossMetric, CUDABinaryMetricInterface, CUDAPointwiseMetricInterface, cuda_metric, cuda_pointwise_metric (+6 more)

### Community 49 - "Community 49"
Cohesion: 0.11
Nodes (15): cassert, condition_variable, cstddef, system_error, basic_shared_mutex, basic_shared_timed_mutex, do_try_lock_sharedwait(), do_try_lockwait() (+7 more)

### Community 50 - "Community 50"
Cohesion: 0.14
Nodes (14): AllocateBitset(), BeforeTrain(), CheckSplitValid(), ConstructBitsetForCategoricalSplit(), CUDASingleGPUTreeLearner, FitByExistingTree(), Init(), NCCLReduceHistogram() (+6 more)

### Community 51 - "Community 51"
Cohesion: 0.21
Nodes (20): dataset_loader, CheckCanLoadFromBin(), CheckCategoricalFeatureNumBin(), CheckDataset(), CheckSampleSize(), ConstructBinMappersFromTextData(), ConstructFromSampleData(), DatasetLoader() (+12 more)

### Community 52 - "Community 52"
Cohesion: 0.17
Nodes (18): CheckMultiClassObjective(), CheckParamConflict(), GetAucMuWeights(), GetBoostingType(), GetDataSampleStrategy(), GetDeviceType(), GetFirstValueAsInt(), GetInteractionConstraints() (+10 more)

### Community 53 - "Community 53"
Cohesion: 0.12
Nodes (5): AllocateBins(), CopySubrow(), CopySubrowByCol(), LightGBM(), LoadDefinitionFromMemory()

### Community 54 - "Community 54"
Cohesion: 0.16
Nodes (11): ExtendPath(), LinearModelToJSON(), NodeToJSON(), Split(), SplitCategorical(), ToJSON(), TreeSHAP(), TreeSHAPByMap() (+3 more)

### Community 55 - "Community 55"
Cohesion: 0.14
Nodes (11): BoostFromAverage(), Boosting(), NCCLGBDT, NCCLGBDT<GBDT>, TrainOneIter(), TrainTreeLearnerThread(), UpdateScoreThread(), cuda_nccl_topology (+3 more)

### Community 56 - "Community 56"
Cohesion: 0.12
Nodes (8): :obj:`dict`: The best score of fitted model., :obj:`int`: The best iteration of fitted model if ``early_stopping()`` callback, :obj:`int`: True number of boosting iterations performed.          This might be, Booster: The underlying Booster of this model., :obj:`dict`: The evaluation results if validation sets have been specified., :obj:`list` of shape = [n_features]: The names of features.          .. note::, :obj:`array` of shape = [n_classes]: The class label array., :obj:`int`: The number of classes.

### Community 57 - "Community 57"
Cohesion: 0.12
Nodes (15): cerrno, fcntl, ifaddrs, in, inet, ioctl, iphlpapi, netdb (+7 more)

### Community 58 - "Community 58"
Cohesion: 0.19
Nodes (14): CreateParser(), CSVParser, GetDataType(), GetLabelIdxForCSV(), GetLabelIdxForLibsvm(), GetLabelIdxForTSV(), GetLine(), GetNumColFromLIBSVMFile() (+6 more)

### Community 59 - "Community 59"
Cohesion: 0.13
Nodes (3): _categorical_data(), test_tree_with_categories_above_max_category_values(), test_tree_with_categories_below_max_category_values()

### Community 60 - "Community 60"
Cohesion: 0.17
Nodes (7): CalcBlockDim(), CUDADataPartition, GenDataToLeftBitVector(), ResetTrainingData(), Split(), SplitInner(), cuda_data_partition

### Community 61 - "Community 61"
Cohesion: 0.19
Nodes (10): cuda_best_split_finder, AllocateCatVectors(), CUDABestSplitFinder, Init(), InitCUDAFeatureMetaInfo(), InitFeatureMetaInfo(), ResetConfig(), ResetTrainingData() (+2 more)

### Community 62 - "Community 62"
Cohesion: 0.23
Nodes (12): CUDAFairLossMetric, CUDAGammaDevianceMetric, CUDAGammaMetric, CUDAHuberLossMetric, CUDAL1Metric, CUDAL2Metric, CUDAMAPEMetric, CUDAPoissonMetric (+4 more)

### Community 63 - "Community 63"
Cohesion: 0.17
Nodes (7): CUDATree(), InitCUDA(), InitCUDAMemory(), RecordBranchFeatures(), Split(), SplitCategorical(), cuda_tree

### Community 64 - "Community 64"
Cohesion: 0.18
Nodes (10): cuda_single_gpu_tree_learner, dense, gpu_tree_learner, linear_tree_learner, serial_tree_learner, FitByExistingTree(), GetLeafMap(), Init() (+2 more)

### Community 65 - "Community 65"
Cohesion: 0.20
Nodes (10): pipeline_reader, CountLine(), ReadAllAndProcess(), ReadAllAndProcessParallel(), ReadAllAndProcessParallelWithFilter(), ReadAllLines(), ReadAndFilterLines(), ReadPartAndProcessParallel() (+2 more)

### Community 66 - "Community 66"
Cohesion: 0.43
Nodes (7): FileLoader, test_binary(), test_binary_linear(), test_lambdarank(), test_multiclass(), test_regression(), test_xendcg()

### Community 67 - "Community 67"
Cohesion: 0.13
Nodes (2): classification, objectives

### Community 69 - "Community 69"
Cohesion: 0.14
Nodes (13): FairLossMetric, GammaDevianceMetric, GammaMetric, HuberLossMetric, L1Metric, L2Metric, MAPEMetric, PoissonMetric (+5 more)

### Community 70 - "Community 70"
Cohesion: 0.26
Nodes (12): Allgather(), AllgatherBruck(), AllgatherRecursiveDoubling(), AllgatherRing(), Allreduce(), AllreduceByAllGather(), Init(), num_machines() (+4 more)

### Community 71 - "Community 71"
Cohesion: 0.21
Nodes (8): CalcConstructHistogramKernelDim(), CUDAHistogramConstructor, Init(), InitFeatureMetaInfo(), ResetTrainingData(), cuda_histogram_constructor, cuda_leaf_splits, cuda_row_data

### Community 72 - "Community 72"
Cohesion: 0.19
Nodes (8): _LGBMModelBase, _LGBMRegressorBase, LGBMModel, LGBMRegressor, :obj:`str` or :obj:`callable`: The concrete objective used while fitting this mo, :obj:`array` of shape = [n_features]: The feature importances (the higher, the m, Implementation of the scikit-learn API for LightGBM., Update ``sklearn.utils.Tags`` inherited from ``scikit-learn`` base classes.

### Community 74 - "Community 74"
Cohesion: 0.15
Nodes (13): _AssertDatasetHandleNotNull(), LGBM_BoosterAddValidData_R(), LGBM_BoosterCreate_R(), LGBM_BoosterResetTrainingData_R(), LGBM_DatasetGetFeatureNumBin_R(), LGBM_DatasetGetField_R(), LGBM_DatasetGetFieldSize_R(), LGBM_DatasetGetNumData_R() (+5 more)

### Community 75 - "Community 75"
Cohesion: 0.38
Nodes (10): c_str(), free_dataset(), load_from_csc(), load_from_csr(), load_from_file(), load_from_mat(), save_to_binary(), test_booster() (+2 more)

### Community 76 - "Community 76"
Cohesion: 0.23
Nodes (8): h5py, create_dataset_from_multiple_hdf(), generate_hdf(), HDFSequence, main(), Construct a sequence object from HDF5 with required interface.          Paramete, Store numpy array to HDF5 file.      Please note chunk size settings in the impl, save2hdf()

### Community 77 - "Community 77"
Cohesion: 0.21
Nodes (6): _LGBMClassifierBase, LGBMClassifier, Docstring is set after definition, using a template., Docstring is inherited from the LGBMModel., Return the raw margin score for each sample.          .. versionadded:: 4.7.0, :obj:`bool`:  Indicator of whether the classifier is used for multiclass.

### Community 79 - "Community 79"
Cohesion: 0.18
Nodes (1): cuda_rocm_interop

### Community 80 - "Community 80"
Cohesion: 0.18
Nodes (2): DenseBin, DenseBinIterator

### Community 81 - "Community 81"
Cohesion: 0.25
Nodes (7): InnerRawGet(), RawGet(), Reset(), SparseBin, SparseBinIterator, SplitCategoricalInner(), SplitInner()

### Community 82 - "Community 82"
Cohesion: 0.25
Nodes (6): GetLeaf(), GetLeafByMap(), Predict(), PredictByMap(), PredictLeafIndex(), PredictLeafIndexByMap()

### Community 83 - "Community 83"
Cohesion: 0.18
Nodes (11): LGBM_BoosterPredictForMat(), LGBM_BoosterPredictForMats(), LGBM_BoosterPredictForMatSingleRow(), LGBM_BoosterPredictForMatSingleRowFast(), LGBM_DatasetCreateFromMat(), LGBM_DatasetCreateFromMats(), LGBM_DatasetPushRows(), LGBM_DatasetPushRowsWithMetadata() (+3 more)

### Community 84 - "Community 84"
Cohesion: 0.29
Nodes (6): CalculateSplittedLeafOutput(), CUDALeafSplits, GetLeafGain(), GetLeafGainGivenOutput(), Init(), Resize()

### Community 85 - "Community 85"
Cohesion: 0.22
Nodes (2): DivideCUDAFeatureGroups(), Init()

### Community 86 - "Community 86"
Cohesion: 0.22
Nodes (3): CopyMultiValBinSubset(), InitTrain(), train_share_states

### Community 87 - "Community 87"
Cohesion: 0.22
Nodes (6): LGBMRanker, Construct a proxy class.          This class transforms objective function to ma, LightGBM ranker.      .. warning::          scikit-learn doesn't support ranking, Construct a proxy class.          This class transforms evaluation function to m, r"""Construct a gradient boosting model.          Parameters         ----------, Set the parameters of this estimator.          Parameters         ----------

### Community 88 - "Community 88"
Cohesion: 0.22
Nodes (1): is

### Community 89 - "Community 89"
Cohesion: 0.22
Nodes (1): for

### Community 90 - "Community 90"
Cohesion: 0.22
Nodes (9): CreateSampleIndices(), DatasetCreateFromArrowChunkedArray(), LGBM_DatasetCreateFromArrow(), LGBM_DatasetCreateFromArrowStream(), LGBM_DatasetCreateFromCSR(), LGBM_DatasetCreateFromCSRFunc(), LGBM_GetSampleCount(), LGBM_SampleIndices() (+1 more)

### Community 91 - "Community 91"
Cohesion: 0.29
Nodes (6): ArrowChunkedArray, Iterator, MakeSchemaView(), View, Visitor, nanoarrow

### Community 92 - "Community 92"
Cohesion: 0.39
Nodes (6): DumpModel(), FeatureImportance(), ModelToIfElse(), SaveModelToFile(), SaveModelToIfElse(), SaveModelToString()

### Community 93 - "Community 93"
Cohesion: 0.32
Nodes (5): Predict(), PredictByMap(), PredictRaw(), PredictRawByMap(), prediction_early_stop

### Community 94 - "Community 94"
Cohesion: 0.36
Nodes (5): cuda_column_data, CopySubrow(), Init(), InitColumnMetaInfo(), ResizeWhenCopySubrow()

### Community 95 - "Community 95"
Cohesion: 0.25
Nodes (1): cuda_metadata

### Community 96 - "Community 96"
Cohesion: 0.29
Nodes (4): CUDAMetricInterface, CUDAScoreUpdater, InitCUDA(), cuda_utils

### Community 97 - "Community 97"
Cohesion: 0.25
Nodes (3): json, pickle, # NOTE: when you do customized loss function, the default prediction value is ma

### Community 98 - "Community 98"
Cohesion: 0.32
Nodes (4): _choose_param_value(), _ConfigAliases, Refit the existing Booster by new data.          Parameters         ----------, Get a single parameter value, accounting for aliases.      Parameters     ------

### Community 99 - "Community 99"
Cohesion: 0.33
Nodes (4): EvalResult, Result from computing an evaluation metric on a dataset.      In ``lightgbm<4.7., Whether the result was created by ``cv()``.          If ``True``:            * `, NamedTuple

### Community 100 - "Community 100"
Cohesion: 0.29
Nodes (6): _get_group_from_constructed_dataset(), _get_label_from_constructed_dataset(), _get_weight_from_constructed_dataset(), _ObjectiveFunctionWrapper, Proxy class for objective function., Call passed function with appropriate arguments.          Parameters         ---

### Community 101 - "Community 101"
Cohesion: 0.29
Nodes (6): _EvalFunctionWrapper, _extract_evaluation_meta_data(), Proxy class for evaluation function., Try to extract the ith element of one of the ``eval_*`` inputs., Validate eval args.      Returns     -------     eval_set, _validate_eval_set_Xy()

### Community 102 - "Community 102"
Cohesion: 0.29
Nodes (1): data

### Community 103 - "Community 103"
Cohesion: 0.48
Nodes (7): LGBM_BoosterDumpModel_R(), LGBM_BoosterGetEvalNames_R(), LGBM_BoosterGetLoadedParam_R(), LGBM_DatasetGetFeatureNames_R(), LGBM_DumpParamAliases_R(), safe_R_mkChar(), safe_R_string()

### Community 105 - "Community 105"
Cohesion: 0.60
Nodes (5): MakeFloatArray(), MakeFloatStructArray(), MakeFloatStructSchema(), MakePrimitiveSchema(), TEST()

### Community 106 - "Community 106"
Cohesion: 0.33
Nodes (4): Generic data access interface.      Object should support the following operatio, Return data for given row index.          A basic implementation should look lik, Return row count of this sequence., Sequence

### Community 107 - "Community 107"
Cohesion: 0.33
Nodes (3): Get parameters for this estimator.          Parameters         ----------, Process the parameters of this estimator based on its type, parameter aliases, e, Convert special values of n_jobs to their actual values according to the formula

### Community 109 - "Community 109"
Cohesion: 0.33
Nodes (2): classification, for

### Community 110 - "Community 110"
Cohesion: 0.50
Nodes (4): chunked_array, are_vectors_equal(), ChunkedArrayTest, TEST_F()

### Community 111 - "Community 111"
Cohesion: 0.40
Nodes (4): InternalRefTransform, Replaces '.rst' with '.html' in all internal links like './[Something].rst[#anch, Apply the transform to the document tree., Transform

### Community 112 - "Community 112"
Cohesion: 0.60
Nodes (5): CategoricalDecisionIfElse(), NodeToIfElse(), NodeToIfElseByMap(), NumericalDecisionIfElse(), ToIfElse()

### Community 113 - "Community 113"
Cohesion: 0.60
Nodes (3): IsMpiInitialized(), MpiAbortIfIsParallel(), MpiFinalizeIfIsParallel()

### Community 114 - "Community 114"
Cohesion: 0.40
Nodes (5): categorize(), generate_trainset_for_monotone_constraints_tests(), test_monotone_constraints(), test_monotone_penalty(), test_monotone_penalty_max()

### Community 115 - "Community 115"
Cohesion: 0.40
Nodes (5): check_constant_features(), test_constant_features_binary(), test_constant_features_multiclass(), test_constant_features_multiclassova(), test_constant_features_regression()

### Community 116 - "Community 116"
Cohesion: 0.40
Nodes (5): multi_logloss(), test_continue_train_multiclass(), test_multiclass(), test_multiclass_prediction_early_stopping(), test_multiclass_rf()

### Community 117 - "Community 117"
Cohesion: 0.40
Nodes (1): and

### Community 118 - "Community 118"
Cohesion: 0.40
Nodes (5): Get(), LGBM_BoosterPredictForCSC(), LGBM_BoosterPredictSparseOutput(), LGBM_DatasetCreateFromCSC(), NextNonZero()

### Community 122 - "Community 122"
Cohesion: 0.50
Nodes (1): are

### Community 123 - "Community 123"
Cohesion: 0.50
Nodes (2): :obj:`int`: The number of features of fitted model., Set number of features found in passed-in dataset.          Starting with ``scik

### Community 124 - "Community 124"
Cohesion: 0.50
Nodes (1): objectives

### Community 126 - "Community 126"
Cohesion: 0.50
Nodes (4): get_altrepped_raw_dataptr(), get_altrepped_raw_dataptr_or_null(), get_altrepped_raw_len(), get_ptr_from_altrepped_raw()

### Community 127 - "Community 127"
Cohesion: 0.50
Nodes (1): are

### Community 128 - "Community 128"
Cohesion: 0.50
Nodes (1): are

### Community 129 - "Community 129"
Cohesion: 0.67
Nodes (1): hip_runtime

### Community 131 - "Community 131"
Cohesion: 0.67
Nodes (3): Feature2Group(), feature_names(), FeatureBinMapper()

### Community 132 - "Community 132"
Cohesion: 0.67
Nodes (2): :obj:`array` of shape = [n_features]: scikit-learn compatible version of ``.feat, Intercept calls to delete ``feature_names_in_``.          Some code paths in ``s

### Community 133 - "Community 133"
Cohesion: 0.67
Nodes (3): constant_metric(), decreasing_metric(), test_early_stopping_for_only_first_metric()

### Community 134 - "Community 134"
Cohesion: 0.67
Nodes (3): simulate_position_bias(), test_ranking_with_position_information_with_dataset_constructor(), test_ranking_with_position_information_with_file()

### Community 135 - "Community 135"
Cohesion: 0.67
Nodes (1): lgb

### Community 139 - "Community 139"
Cohesion: 0.67
Nodes (3): LGBM_BoosterPredictForArrow(), LGBM_BoosterPredictForArrowChunkedArray(), LGBM_BoosterPredictForArrowStream()

### Community 141 - "Community 141"
Cohesion: 0.67
Nodes (3): format_to_buf(), operator(), StringToArray()

### Community 142 - "Community 142"
Cohesion: 1.00
Nodes (1): are

### Community 143 - "Community 143"
Cohesion: 1.00
Nodes (1): LightGBM

### Community 146 - "Community 146"
Cohesion: 1.00
Nodes (2): test_multi_class_error(), top_k_error()

### Community 153 - "Community 153"
Cohesion: 1.00
Nodes (2): CSC_RowIterator, IterateFunctionFromCSC()

### Community 154 - "Community 154"
Cohesion: 1.00
Nodes (2): LGBM_BoosterGetFeatureNames(), LGBM_BoosterValidateFeatureNames()

### Community 155 - "Community 155"
Cohesion: 1.00
Nodes (2): LGBM_BoosterSaveModelToString_R(), safe_R_raw()

### Community 157 - "Community 157"
Cohesion: 1.00
Nodes (1): lgb

## Knowledge Gaps
- **424 isolated node(s):** `probabilities`, `with`, `objective`, `at`, `can` (+419 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 0`** (2 nodes): `psutil`, `# NOTE: this was passed in with alias 'sub_row'`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (2 nodes): `and`, `handles`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 67`** (2 nodes): `classification`, `objectives`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 79`** (1 nodes): `cuda_rocm_interop`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 80`** (2 nodes): `DenseBin`, `DenseBinIterator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 85`** (2 nodes): `DivideCUDAFeatureGroups()`, `Init()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 88`** (1 nodes): `is`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 89`** (1 nodes): `for`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 95`** (1 nodes): `cuda_metadata`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 102`** (1 nodes): `data`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 109`** (2 nodes): `classification`, `for`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 117`** (1 nodes): `and`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 122`** (1 nodes): `are`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 123`** (2 nodes): `:obj:`int`: The number of features of fitted model.`, `Set number of features found in passed-in dataset.          Starting with ``scik`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 124`** (1 nodes): `objectives`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 127`** (1 nodes): `are`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 128`** (1 nodes): `are`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 129`** (1 nodes): `hip_runtime`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 132`** (2 nodes): `:obj:`array` of shape = [n_features]: scikit-learn compatible version of ``.feat`, `Intercept calls to delete ``feature_names_in_``.          Some code paths in ``s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 135`** (1 nodes): `lgb`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 142`** (1 nodes): `are`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 143`** (1 nodes): `LightGBM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 146`** (2 nodes): `test_multi_class_error()`, `top_k_error()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 153`** (2 nodes): `CSC_RowIterator`, `IterateFunctionFromCSC()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 154`** (2 nodes): `LGBM_BoosterGetFeatureNames()`, `LGBM_BoosterValidateFeatureNames()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 155`** (2 nodes): `LGBM_BoosterSaveModelToString_R()`, `safe_R_raw()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 157`** (1 nodes): `lgb`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `LightGBMError` connect `Community 33` to `Community 8`, `Community 4`, `Community 98`, `Community 5`, `Community 13`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Why does `_safe_call()` connect `Community 4` to `Community 8`, `Community 13`, `Community 98`, `Community 5`, `Community 33`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Why does `LGBMModel` connect `Community 72` to `Community 3`, `Community 77`, `Community 56`, `Community 132`, `Community 101`, `Community 107`, `Community 87`, `Community 123`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **What connects `probabilities`, `with`, `objective` to the rest of the system?**
  _424 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.01652892561983471 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.025050505050505052 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.02247191011235955 - nodes in this community are weakly interconnected._