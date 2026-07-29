# Graph Report - .  (2026-07-29)

## Corpus Check
- cluster-only mode - file stats not available

## Summary
- 7708 nodes · 14747 edges · 360 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output
- Edge kinds: imports: 5601 · contains: 4106 · calls: 1906 · method: 1253 · rationale_for: 911 · imports_from: 819 · inherits: 124 · implements: 27


## Graph Freshness
- Built from Git commit: `2a4786e`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `XGBoostJNI` - 60 edges
2. `Booster` - 46 edges
3. `Booster` - 38 edges
4. `XGBModel` - 38 edges
5. `BoosterImplTest` - 34 edges
6. `DMatrix` - 33 edges
7. `_SparkXGBParams` - 30 edges
8. `DMatrix` - 28 edges
9. `dispatch_data_backend()` - 27 edges
10. `TestWithDask` - 25 edges

## Surprising Connections (you probably didn't know these)
- `SubtractionTrick()` --calls--> `SubtractionHist()`  [EXTRACTED]
  plugin/sycl/common/hist_util.cc → src/common/hist_util.cc
- `Init()` --calls--> `ResizeIndex()`  [EXTRACTED]
  plugin/sycl/data/gradient_index.cc → src/data/gradient_index.cc
- `generate_doxygen_xml()` --calls--> `run_doxygen()`  [EXTRACTED]
  dmlc-core/doc/conf.py → doc/conf.py
- `Run the doxygen make command in the designated folder.` --rationale_for--> `run_doxygen()`  [EXTRACTED]
  dmlc-core/doc/conf.py → doc/conf.py
- `ProcessQueue()` --calls--> `stop_()`  [EXTRACTED]
  src/collective/loop.cc → src/collective/loop.h

## Communities

### Community 0 - "Community 0"
Cohesion: 0.01
Nodes (274): base64, c_api, callback, collections, collective, compat, config, copy (+266 more)

### Community 1 - "Community 1"
Cohesion: 0.02
Nodes (87): Demo for survival analysis (regression). =======================================, Demo for survival analysis (regression) with Optuna. ===========================, csv, cudf, cupy, generate_models, Getting started with XGBoost ============================  This is a simple exam, main() (+79 more)

### Community 2 - "Community 2"
Cohesion: 0.02
Nodes (59): adaptive, api_entry, array_interface, CommGroupTest, PrintWorker, TestFileStream, TEST(), TestMean() (+51 more)

### Community 3 - "Community 3"
Cohesion: 0.02
Nodes (109): argparse, cpplint, Helper script to prepare for releasing XGBoost JVM packages to Maven Central.  #, Query list of all contributors and reviewers in a release, exec_cmd(), Submission job for local jobs., Execute the command line command., Submit function of local jobs. (+101 more)

### Community 4 - "Community 4"
Cohesion: 0.02
Nodes (87): asyncio, dask, dask_array, Example of training survival model with Dask on CPU ============================, Example of training with Dask on CPU ====================================, dask_cuda, dask_cudf, CustomEarlyStopping (+79 more)

### Community 5 - "Community 5"
Cohesion: 0.03
Nodes (41): aft_obj, cache, common_row_partitioner, TEST(), TransformDevice(), SparsePageRawFormat, functional, future (+33 more)

### Community 6 - "Community 6"
Cohesion: 0.03
Nodes (24): aggregator, algorithm, common, cstddef, device_architecture, device_properties, init_estimation, Iterator (+16 more)

### Community 7 - "Community 7"
Cohesion: 0.03
Nodes (43): categorical, categorical_helpers, GetTaskIdx(), MergeToArray(), SetNLeftElems(), SetNRightElems(), constraints, driver (+35 more)

### Community 8 - "Community 8"
Cohesion: 0.03
Nodes (70): get_data(), main(), _pickle_path(), Cross-platform model test: Train on GPU (Linux), test inference on macOS., Generate reproducible synthetic classification data., Train models using GPU and save them (binary + pickle with column sampling)., Load models and verify predictions match (binary + pickle)., Entry for both training and inference. (+62 more)

### Community 9 - "Community 9"
Cohesion: 0.03
Nodes (41): column_matrix, CheckColumWithMissingValue(), CheckSparseColumn(), TEST(), CheckIndexData(), TEST(), ExtMemQuantileDMatrix(), GetGradientIndex() (+33 more)

### Community 10 - "Community 10"
Cohesion: 0.03
Nodes (35): BusyWait(), GetNcclResult(), GetC2cLinkCountFromSmi(), GetC2cLinkCountFromSmiGlobal(), GetC2cLinkCountFromSmiImpl(), GetVersionFromSmi(), GetVersionFromSmiGlobal(), MakeAllocProp() (+27 more)

### Community 11 - "Community 11"
Cohesion: 0.03
Nodes (31): batch_utils, MakeExtMemForTest(), MakeLabelForTest(), MakeQDMForTest(), MakeSimpleDMatrixForTest(), TEST(), TestExceptionCatching(), TestXGDMatrixGetQuantileCut() (+23 more)

### Community 12 - "Community 12"
Cohesion: 0.04
Nodes (21): atomic, base, byteswap, cassert, InitializeRange(), operator(), condition_variable, deque (+13 more)

### Community 13 - "Community 13"
Cohesion: 0.04
Nodes (26): allreduce, Block(), Loop(), Process(), ProcessQueue(), stop_(), LoopTest, RefResourceView() (+18 more)

### Community 14 - "Community 14"
Cohesion: 0.03
Nodes (23): get_cache_file_set(), get_memory_mb(), get_opts(), Get the memory in MB from memory string.      mem_str: str         String repres, Get options to launch the job.      Returns     -------     args: ArgumentParser, Get the list of files to be cached.      Parameters     ----------     args: Arg, Submit jobs to Sun Grid Engine., Job submission script for SGE. (+15 more)

### Community 15 - "Community 15"
Cohesion: 0.03
Nodes (3): altrep, r, rmath

### Community 16 - "Community 16"
Cohesion: 0.06
Nodes (38): arrays, bigdensematrix, booster, collector, communicator, configuration, customeval, dataloader (+30 more)

### Community 17 - "Community 17"
Cohesion: 0.04
Nodes (26): coordinate_common, feature_map, gblinear_model, gbm, GBLinear, learner, linear_updater, CoordinateUpdater (+18 more)

### Community 18 - "Community 18"
Cohesion: 0.05
Nodes (31): array_tree_layout, communicator_inl, Dart, TEST(), TestModelSlice(), gbtree, gbtree_model, gbtree_view (+23 more)

### Community 19 - "Community 19"
Cohesion: 0.04
Nodes (57): _DASK_2024_12_1(), _DASK_2025_3_0(), _DASK_VERSION(), get_address_from_user(), get_n_threads(), Utilities for the XGBoost Dask interface., Get the number of threads from a worker and the user-supplied parameters., Get the tracker address from the optional user configuration.      Parameters (+49 more)

### Community 20 - "Community 20"
Cohesion: 0.04
Nodes (13): adapter, cat_container, columnar, ColumnarAdapter(), GetRefCats(), IteratorAdapter<DataIterHandle, XGBCallbackDataIterNext, XGBoostBatchCSR>, CSRIterForTest, TEST() (+5 more)

### Community 21 - "Community 21"
Cohesion: 0.04
Nodes (20): any, dmlc(), reset(), file_iterator, iostream, logging, memory_io, sstream (+12 more)

### Community 22 - "Community 22"
Cohesion: 0.03
Nodes (1): XGBoostJNI

### Community 23 - "Community 23"
Cohesion: 0.04
Nodes (1): sklearn_utils_estimator_checks

### Community 24 - "Community 24"
Cohesion: 0.07
Nodes (46): buffer, curl, dirent, errno, hmac, FileStream, GetPathInfo(), ListDirectory() (+38 more)

### Community 25 - "Community 25"
Cohesion: 0.05
Nodes (42): ABC, array_hasobject(), array_interface(), array_interface_dict(), _ArrayLikeArg, _arrow_array_inf(), _arrow_buf_inf(), arrow_cat_inf() (+34 more)

### Community 26 - "Community 26"
Cohesion: 0.05
Nodes (21): multi_target_tree_model, CheckProbaToMargin(), TestGammaRegressionBasic(), TestLogisticRegressionBasic(), TestPoissonRegressionBasic(), TestTweedieRegressionBasic(), test_multi_target_tree_model, test_objective_helpers (+13 more)

### Community 28 - "Community 28"
Cohesion: 0.05
Nodes (18): cmath, ConstView(), CPU(), MakeMatrixFromTest(), TEST(), linalg, AcceptsQueryWeights(), AcceptsRowWeights() (+10 more)

### Community 29 - "Community 29"
Cohesion: 0.06
Nodes (42): applicationconstants, applicationid, applicationreport, applicationsubmissioncontext, bytebuffer, container, containerexitstatus, containerid (+34 more)

### Community 30 - "Community 30"
Cohesion: 0.05
Nodes (12): MyLogistic, expectile_loss_utils, CommitModel(), CommitModelGroup(), LoadModel(), MakeIndptr(), Validate(), param_array (+4 more)

### Community 31 - "Community 31"
Cohesion: 0.06
Nodes (45): importlib_util, sklearn_base, sklearn_utils, concat(), import_cupy(), import_pandas(), import_polars(), import_pyarrow() (+37 more)

### Community 32 - "Community 32"
Cohesion: 0.07
Nodes (44): asarray(), _basic_example(), comp_booster(), get_df_impl(), _make_dm(), make_recoded(), Tests for the ordinal re-coder., Run checks with mixed types. (+36 more)

### Community 33 - "Community 33"
Cohesion: 0.07
Nodes (28): CheckDevice(), Copy(), CopyTensorInfoImpl(), Create(), Extend(), Gather(), GetTranspose(), Load() (+20 more)

### Community 34 - "Community 34"
Cohesion: 0.05
Nodes (19): initializer_list, lambdarank_obj, delta(), Eps64(), LambdaGrad(), LambdaRankMAP, LambdaRankNDCG, LambdaRankObj (+11 more)

### Community 35 - "Community 35"
Cohesion: 0.05
Nodes (3): Tests for the CUDA implementation of multi-target., Tests for the CPU implementation of multi-target., xgboost_testing_multi_target

### Community 36 - "Community 36"
Cohesion: 0.06
Nodes (22): climits, add(), add_block_to_free_list(), add_blocks_to_free_list(), add_producer(), dmlc(), enqueue(), get_or_add_implicit_producer() (+14 more)

### Community 37 - "Community 37"
Cohesion: 0.05
Nodes (8): concurrent_futures, itertools, comp_training_with_rank_objective(), Internal method that trains the dataset using the rank objective on GPU and CPU,, test_with_mq2008(), TestSHAP, xgboost_testing_ranking, xgboost_testing_with_skl

### Community 38 - "Community 38"
Cohesion: 0.06
Nodes (34): graphviz, generate_data(), main(), native_rmse(), native_rmsle(), plot_history(), py_rmsle(), Demo for defining a custom regression objective and metric ===================== (+26 more)

### Community 39 - "Community 39"
Cohesion: 0.05
Nodes (2): jvm_utils, xgboost4j

### Community 40 - "Community 40"
Cohesion: 0.05
Nodes (39): gc, numpy_random, check_inf(), get_ames_housing(), get_california_housing(), get_cancer(), get_digits(), get_mq2008() (+31 more)

### Community 41 - "Community 41"
Cohesion: 0.07
Nodes (23): Model, Node, Right child ID of a node., Whether a node is leaf., Whether a node is deleted., Gradient boosted tree model., Construct the Model from a JSON object.          parameters         ----------, Convert a sequence of bytes to a list of Python integer (+15 more)

### Community 42 - "Community 42"
Cohesion: 0.09
Nodes (29): hist_row_adder, hist_synchronizer, hist_updater, GenerateRandomGPairs(), TestHistUpdater, TestHistUpdaterApplySplit(), TestHistUpdaterBuildHistogramsLossGuide(), TestHistUpdaterEvaluateSplits() (+21 more)

### Community 43 - "Community 43"
Cohesion: 0.09
Nodes (32): CheckU64Range(), DecodeStr(), Dump(), EncodeStr(), IsInfMSVCWar(), IsSpace(), JsonTypedArray<double, Value::ValueKind::kF64Array>, JsonTypedArray<float, Value::ValueKind::kF32Array> (+24 more)

### Community 44 - "Community 44"
Cohesion: 0.07
Nodes (19): bitfield, ColumnMatrix(), GetGlobalBinIdx(), GetRowIdx(), GrowTo(), InitFromSparse(), InitView(), IsMissing() (+11 more)

### Community 45 - "Community 45"
Cohesion: 0.09
Nodes (2): Booster, getPType()

### Community 46 - "Community 46"
Cohesion: 0.05
Nodes (1): xgboost_testing_ordinal

### Community 47 - "Community 47"
Cohesion: 0.08
Nodes (18): Accept(), Bind(), Connect(), domain_(), Handle(), InaddrAny(), Loopback(), MakeSockAddress() (+10 more)

### Community 48 - "Community 48"
Cohesion: 0.07
Nodes (24): Copy(), DeviceCanWrite(), Extend(), HostDeviceVector<bst_float>, HostDeviceVector<bst_idx_t>, HostDeviceVector<double>, HostDeviceVector<Entry>, HostDeviceVector<FeatureType> (+16 more)

### Community 49 - "Community 49"
Cohesion: 0.06
Nodes (5): num_workers(), _spark_test_device(), _spark_test_mode(), TestClassifier, TestRegressor

### Community 50 - "Community 50"
Cohesion: 0.07
Nodes (17): Booster, A Booster of XGBoost.      Booster is the model of xgboost, that contains low le, Iterator method for getting individual trees.          .. versionadded:: 2.0.0, Output internal parameter configuration of Booster as a JSON         string., Load configuration returned by `save_config`.          .. versionadded:: 1.0.0, Return a copy of booster., Copy the booster object.          Returns         -------         booster :, Get attribute string from the Booster.          Parameters         ---------- (+9 more)

### Community 51 - "Community 51"
Cohesion: 0.10
Nodes (1): BoosterImplTest

### Community 52 - "Community 52"
Cohesion: 0.06
Nodes (3): and, classification, probabilities

### Community 53 - "Community 53"
Cohesion: 0.08
Nodes (17): DMatrix, Save DMatrix to an XGBoost buffer.  Saved binary can be later loaded         by, Set label of dmatrix          Parameters         ----------         label: array, Set weight of each instance.          Parameters         ----------         weig, Set base margin of booster to start from.          This can be used to specify a, Set group size of DMatrix (used for ranking).          Parameters         ------, Get the label of the DMatrix., Get the weight of the DMatrix. (+9 more)

### Community 54 - "Community 54"
Cohesion: 0.07
Nodes (19): arraylist, arrayutils, CustomObjective, LogRegObj, hashset, input, IObjective, java (+11 more)

### Community 55 - "Community 55"
Cohesion: 0.07
Nodes (11): CheckObjFunction(), CheckObjFunctionImpl(), CheckRankingObjFunction(), CreateBigTestData(), CreateSimpleTestData(), hw_decomp_ratio_(), RMMAllocator, Seed() (+3 more)

### Community 56 - "Community 56"
Cohesion: 0.06
Nodes (4): classification, from, in, index

### Community 57 - "Community 57"
Cohesion: 0.08
Nodes (18): DumpModel(), Equal(), ExpandCategorical(), ExpandNode(), FromJson(), GetDepth(), GetSplitCategories(), GraphvizGenerator (+10 more)

### Community 58 - "Community 58"
Cohesion: 0.08
Nodes (19): basedevicememorybuffer, columnvector, dtype, intstream, ExtMemQuantileDMatrix, F32NaNSerializer, F64NaNSerializer, QuantileDMatrix (+11 more)

### Community 59 - "Community 59"
Cohesion: 0.07
Nodes (9): FixedSizeStream(), GetMmapAlignment(), OpenMmap(), PeekRead(), Read(), ReadAll(), ResourceHandler(), mman (+1 more)

### Community 60 - "Community 60"
Cohesion: 0.06
Nodes (2): as, is

### Community 61 - "Community 61"
Cohesion: 0.10
Nodes (24): _aggcv(), _allreduce_metric(), CallbackContainer, EarlyStopping, EvaluationMonitor, LearningRateScheduler, Aggregate cross-validation results., Helper function for computing customized metric in distributed     environment. (+16 more)

### Community 62 - "Community 62"
Cohesion: 0.08
Nodes (15): cached_input_split, filesys, indexed_recordio_split, line_split, local_filesys, recordio, recordio_split, s3_filesys (+7 more)

### Community 63 - "Community 63"
Cohesion: 0.08
Nodes (22): cerrno, Bootstrap(), GetHostAddress(), RabitTracker(), Run(), Stop(), WaitUntilReady(), WorkerArgs() (+14 more)

### Community 64 - "Community 64"
Cohesion: 0.09
Nodes (25): LsObjMean, LsObjSvd, main(), Least squared error. Reduce the size of the gradient using mean value., One of the methods in the sketch boost paper., Reduce the size of the gradient using SVD., svd_class(), _array_impl() (+17 more)

### Community 65 - "Community 65"
Cohesion: 0.11
Nodes (6): AMRMClientAsync, CallbackHandler, ApplicationMaster, NMCallbackHandler, RMCallbackHandler, NMClientAsync

### Community 66 - "Community 66"
Cohesion: 0.08
Nodes (9): BuildHist(), BuildHistKernel(), BuildHistKernelLocal(), DispatchAndExecute(), GHistBuildingManager, ReduceHist(), SubtractionHist(), SubtractionTrick() (+1 more)

### Community 67 - "Community 67"
Cohesion: 0.09
Nodes (19): AssertSameOnAllWorkers(), DoPropertyDistributedQuantile(), DoSameOnAllWorkersDistributedQuantile(), EnumeratedSummaryEntries(), ExpectEntriesEq(), ExpectPruneMatchesReference(), GenerateWeights(), QuantileContainerTest (+11 more)

### Community 68 - "Community 68"
Cohesion: 0.08
Nodes (19): dataclasses, enum, Demonstration for parsing JSON/UBJSON tree model files =========================, Xgboost training summary integration submodule., ubjson, allreduce(), broadcast(), communicator_print() (+11 more)

### Community 69 - "Community 69"
Cohesion: 0.10
Nodes (16): BoostNewTrees(), CommitModel(), Configure(), CopyGradient(), DoBoost(), DropTrees(), InitNewTrees(), InitTreesToUpdate() (+8 more)

### Community 70 - "Community 70"
Cohesion: 0.11
Nodes (19): hypothesis_extra_numpy, no_arrow(), no_cudf(), no_cupy(), no_dask(), no_dask_cuda(), no_dask_cudf(), no_dask_ml() (+11 more)

### Community 71 - "Community 71"
Cohesion: 0.09
Nodes (20): cv(), CVPack, groups_to_rows(), mkgroupfold(), mknfold(), _PackedBooster, "Auxiliary datastruct to hold one fold of CV., Initialize the CVPack. (+12 more)

### Community 72 - "Community 72"
Cohesion: 0.08
Nodes (7): chrono, clock, mach, semaphore, delay(), TEST(), unittest_threaditer

### Community 73 - "Community 73"
Cohesion: 0.08
Nodes (8): DeleteCacheFiles(), DevicePush(), ShardName(), type_error(), global_config, sparse_page_writer, thread_local, threadpool

### Community 74 - "Community 74"
Cohesion: 0.08
Nodes (9): PredictorFunction, XGBoostModel, Float, IEvaluation, IObjective, MapPartitionFunction, objects, Serializable (+1 more)

### Community 75 - "Community 75"
Cohesion: 0.08
Nodes (19): HasArbitraryParamsDict, HasBaseMarginCol, HasEnableSparseDataOptim, HasFeaturesCol, HasFeaturesCols, HasLabelCol, HasPredictionCol, HasQueryIdCol (+11 more)

### Community 76 - "Community 76"
Cohesion: 0.09
Nodes (28): libpath, ValueError, c_str(), _check_call(), from_cstr_to_pystr(), from_pystr_to_cstr(), _get_log_callback_func(), _lib_version() (+20 more)

### Community 77 - "Community 77"
Cohesion: 0.11
Nodes (11): Estimator, Set params for the estimator., Subclasses should override this method and         returns a _SparkXGBModel subc, We repartition the dataset if the number of workers is not equal to the number o, This just gets the configuration params for distributed xgboost, Prepare the input including column pruning, repartition and so on, Check if stage-level scheduling is not needed,         return true to skip stage, Try to enable stage-level scheduling (+3 more)

### Community 78 - "Community 78"
Cohesion: 0.11
Nodes (1): DMatrix

### Community 79 - "Community 79"
Cohesion: 0.08
Nodes (18): Protocol, _arrow_string_offsets(), Categories, cuda_array_interface(), _CudaArrayLikeArg, DfCatAccessor, from_array_interface(), pd_cat_inf() (+10 more)

### Community 80 - "Community 80"
Cohesion: 0.07
Nodes (4): if, is, list, names

### Community 81 - "Community 81"
Cohesion: 0.08
Nodes (7): One should not specify the device ordinal with dask., Check parameters are roughly the same between various DMatrices, with the, run_gpu_hist(), run_with_dask_array(), run_with_dask_dataframe(), TestDistributedGPU, to_cp()

### Community 82 - "Community 82"
Cohesion: 0.09
Nodes (4): Check obtaining worker addresses using input data., Assert each worker has the correct amount of data, and DMatrix initialization, assert that we don't create duplicated DMatrix, TestWithDask

### Community 83 - "Community 83"
Cohesion: 0.12
Nodes (12): XGBModelBase, Get the underlying xgboost Booster of this model.          This will raise an ex, Set the parameters of this estimator.  Modification of the sklearn method to, Load model attributes without hyper-parameters., Number of features seen during :py:meth:`fit`., Names of features seen during :py:meth:`fit`.  Defined only when `X` has, The best score obtained by early stopping., The best iteration obtained by early stopping.  This attribute is 0-based, (+4 more)

### Community 84 - "Community 84"
Cohesion: 0.11
Nodes (17): aarch64, aslist, assertsame, assertthrows, collection, detectarch, enclosed, ArchDetectionTest (+9 more)

### Community 85 - "Community 85"
Cohesion: 0.11
Nodes (22): atexit, close_all_r_sessions(), close_r_session(), _has_ancestor_class(), _has_class(), mark_doctest_nodes(), _mark_python_node(), _mark_r_node() (+14 more)

### Community 86 - "Community 86"
Cohesion: 0.11
Nodes (17): add_enum(), Check(), describe(), Get(), Init(), is_enum_(), Load(), PrintDefaultValueString() (+9 more)

### Community 87 - "Community 87"
Cohesion: 0.07
Nodes (13): after, and, classification, in, instead, models, names, of (+5 more)

### Community 88 - "Community 88"
Cohesion: 0.10
Nodes (16): _arrow_feature_info(), _check_pyarrow_for_polars(), forbid_regen(), _from_arrow_table(), _from_polars_df(), _from_uri(), is_on_cuda(), _maybe_np_slice() (+8 more)

### Community 89 - "Community 89"
Cohesion: 0.14
Nodes (17): data_accessor, ApproxFeatureImportance(), CalculateApproxContributions(), DispatchByBatchView(), FillNodeMeanValues(), ForEachPartner(), ForEachUniqueFeature(), LaunchShap() (+9 more)

### Community 90 - "Community 90"
Cohesion: 0.14
Nodes (24): build(), cmake_args(), cmake_config(), configure(), copy_file(), copy_glob(), copy_native_library(), copy_test_resources() (+16 more)

### Community 92 - "Community 92"
Cohesion: 0.10
Nodes (6): DefaultChild(), DefaultLeft(), IsLeaf(), LeftChild(), RightChild(), xgboost()

### Community 93 - "Community 93"
Cohesion: 0.12
Nodes (25): _check_data_shape(), _convert_unknown_data(), dispatch_data_backend(), dispatch_proxy_set_data(), _from_dlpack(), _from_list(), _from_numpy_array(), _from_tuple() (+17 more)

### Community 94 - "Community 94"
Cohesion: 0.10
Nodes (15): assertarrayequals, bytearrayinputstream, bytearrayoutputstream, concurrent, main(), Main moduke of the launcher., unzip_archives(), EvalError (+7 more)

### Community 95 - "Community 95"
Cohesion: 0.10
Nodes (10): auc, BinaryAUC(), BinaryPRAUC(), BinaryROCAUC(), EvalAUC, EvalPRAUC, EvalROCAUC, GroupRankingROC() (+2 more)

### Community 96 - "Community 96"
Cohesion: 0.12
Nodes (20): _ClassificationModel, HasContribPredictionCol, HasProbabilityCol, HasRawPredictionCol, _ClassificationModel, The model returned by :func:`xgboost.spark.SparkXGBClassifier.fit`      .. Note:, The model returned by :func:`xgboost.spark.SparkXGBRegressor.fit`      .. Note::, SparkXGBClassifier is a PySpark ML estimator. It implements the XGBoost     clas (+12 more)

### Community 97 - "Community 97"
Cohesion: 0.11
Nodes (1): DMatrixTest

### Community 98 - "Community 98"
Cohesion: 0.14
Nodes (14): AcceptPeer(), Block(), Bootstrap(), ConnectPeer(), ConnectTracker(), ConnectTrackerImpl(), ConnectWorkers(), DefaultTimeoutSec() (+6 more)

### Community 100 - "Community 100"
Cohesion: 0.09
Nodes (8): federated, federated_comm, FederatedComm(), Init(), federated_tracker, grpcpp, server_builder, server_credentials

### Community 101 - "Community 101"
Cohesion: 0.10
Nodes (16): _configure_metrics(), ExtMemQuantileDMatrix, _is_iter(), QuantileDMatrix, Internal method for retrieving a reference to the training DMatrix., A DMatrix variant that generates quantilized data directly from input for the, The external memory version of the :py:class:`QuantileDMatrix`.      See :doc:`/, Parameters         ----------         data :             A user-defined :py:clas (+8 more)

### Community 102 - "Community 102"
Cohesion: 0.13
Nodes (14): blockingconcurrentqueue, concurrentqueue, create(), CreateTimer(), dmlc(), enqueue(), launch(), launch_run() (+6 more)

### Community 103 - "Community 103"
Cohesion: 0.13
Nodes (12): Allgather(), Allreduce(), Broadcast(), GetTrackerHandle(), WaitImpl(), XGCommunicatorAllgather(), XGCommunicatorAllreduce(), XGCommunicatorBroadcast() (+4 more)

### Community 104 - "Community 104"
Cohesion: 0.13
Nodes (11): AddCategories(), AddCutPoints(), AllReduce(), AllreduceCategories(), Clear(), CopyFrom(), MakeCuts(), MergeWeights() (+3 more)

### Community 105 - "Community 105"
Cohesion: 0.12
Nodes (22): cp(), deploy(), deploy_cuda_pkg(), get_current_commit_hash(), get_current_git_branch(), main(), maybe_makedirs(), normpath() (+14 more)

### Community 106 - "Community 106"
Cohesion: 0.13
Nodes (21): base_params(), f(), make_dataset(), make_matrices(), make_predictions(), plot_prediction_intervals(), prediction_intervals(), Prediction Intervals with Quantile and Expectile Regression ==================== (+13 more)

### Community 107 - "Community 107"
Cohesion: 0.10
Nodes (7): allgather, Allreduce(), collective(), AllgatherTest, Worker, TrackerAPITest, result

### Community 108 - "Community 108"
Cohesion: 0.11
Nodes (7): context_helper, optional, regex, CUDAOrdinal(), MakeDeviceOrd(), ParseInt(), SetDeviceOrdinal()

### Community 109 - "Community 109"
Cohesion: 0.12
Nodes (2): Test inplace predict with different device and data types.          The sklearn, TestGPUPredict

### Community 110 - "Community 110"
Cohesion: 0.10
Nodes (3): Checks for np array, list, tuple., Checks for both np array and pd DataFrame., TestQuantileDMatrix

### Community 111 - "Community 111"
Cohesion: 0.14
Nodes (15): basic_row_iter, csv_parser, disk_row_iter, libfm_parser, libsvm_parser, Create(), CreateCSVParser(), CreateLibFMParser() (+7 more)

### Community 112 - "Community 112"
Cohesion: 0.13
Nodes (12): coll, AllreduceTest, AllreduceWorker, federated_coll, Allgather(), AllgatherV(), Allreduce(), Broadcast() (+4 more)

### Community 113 - "Community 113"
Cohesion: 0.15
Nodes (10): collectors, filenotfoundexception, fileoutputstream, getpropertynameforlibrary, inputstream, detectArch(), detectOS(), LibraryPathProvider (+2 more)

### Community 114 - "Community 114"
Cohesion: 0.12
Nodes (12): MLReadable, MLWritable, Return the `xgboost.core.Booster` instance., Get feature importance of each feature.         Importance type can be defined a, Return the pred_contrib_col col name, Return the bool to indicate if it's a single prediction, true is single predicti, Return the true prediction function which will be running on the executor side, Post process of transform (+4 more)

### Community 115 - "Community 115"
Cohesion: 0.10
Nodes (1): TestGPUUpdaters

### Community 116 - "Community 116"
Cohesion: 0.10
Nodes (1): TestDMatrix

### Community 117 - "Community 117"
Cohesion: 0.10
Nodes (2): Test rng has an effect on column sampling., TestTreeMethod

### Community 118 - "Community 118"
Cohesion: 0.12
Nodes (20): _from_pandas_df(), _is_np_array_like(), is_pa_ext_categorical_dtype(), is_pa_ext_dtype(), is_pd_sparse_dtype(), _lazy_has_npdtypes(), _lazy_load_pd_floats(), _lazy_load_pd_is_sparse() (+12 more)

### Community 119 - "Community 119"
Cohesion: 0.13
Nodes (6): Broadcast(), BroadcastTree(), RelayToRoot(), TreePathToRoot(), comm_group, topo

### Community 120 - "Community 120"
Cohesion: 0.13
Nodes (8): ArrayInterface(), ArrayInterfaceHandler(), AssignType(), Dimension(), DispatchCall(), operator(), TypeStr(), UnSupportedType()

### Community 121 - "Community 121"
Cohesion: 0.15
Nodes (14): Convert(), Create_(), Eval(), for_each(), LuaRef(), LuaState(), operator(), reset() (+6 more)

### Community 122 - "Community 122"
Cohesion: 0.16
Nodes (9): PSTracker, RabitTracker, get enviroment variables for slaves         can be passed in as args or envs, get a ring structure that tends to share nodes with the tree         return a li, get a ring connection used to recover local data, get the link map, this is a bit hacky, call for better algorithm         to plac, Tracker module for PS, submit() (+1 more)

### Community 123 - "Community 123"
Cohesion: 0.13
Nodes (12): DataIter, Reset the booster object to release data caches used for training.          .. v, The interface for user defined data iterator. The iterator facilitates     distr, Handle of DMatrix proxy., A wrapper for user defined `reset` function., A wrapper for user defined `next` function.          `this` is not used in Pytho, Reset the data iterator.  Prototype for user defined function., Set the next batch of data.          Parameters         ----------          inpu (+4 more)

### Community 124 - "Community 124"
Cohesion: 0.14
Nodes (11): _check_rf_callback(), _cls_predict_proba(), Get xgboost specific parameters., Gets the number of xgboost boosting rounds., Emit the deprecation warning for the random forest estimators., Predict the probability of each `X` example being of a given class. If the, _warn_rf_deprecated(), XGBClassifier (+3 more)

### Community 125 - "Community 125"
Cohesion: 0.12
Nodes (13): api, build_config, build_config_default, inttypes, istream, parquet_parser, reader, serializer (+5 more)

### Community 126 - "Community 126"
Cohesion: 0.16
Nodes (12): Decode(), Encode(), FromCharFloatImpl(), ItoaUnsignedImpl(), PowerBaseComputer, RyuPrinter, ShortestDigit10(), ShortestDigit10Impl() (+4 more)

### Community 127 - "Community 127"
Cohesion: 0.14
Nodes (7): CurrentDevice(), GetDrVersionGlobal(), GetNumaId(), GetRtVersionGlobal(), GetVersionImpl(), SupportsAts(), SupportsPageableMem()

### Community 128 - "Community 128"
Cohesion: 0.21
Nodes (13): io_utils, ApplyLearningRate(), Copy(), CopyBatch(), CopyCategoryStorage(), Expand(), MultiTargetTree(), NumSplitTargets() (+5 more)

### Community 129 - "Community 129"
Cohesion: 0.14
Nodes (7): dmatrix_from_cupy(), Tests for constructing DMatrix from data structure conforming Apache     Arrow s, Test constructing DMatrix from cupy, _test_cupy_metainfo(), _test_cupy_training(), _test_from_cupy(), TestFromCupy

### Community 130 - "Community 130"
Cohesion: 0.12
Nodes (2): Test the ordering of the callbacks is preserved., TestCallbacks

### Community 131 - "Community 131"
Cohesion: 0.12
Nodes (4): IterForCacheTest, run_data_iterator(), test_data_cache(), test_data_iterator()

### Community 132 - "Community 132"
Cohesion: 0.14
Nodes (11): _can_use_qdm(), _get_qid(), ltr_metric_decorator(), Predict with `X`.  If the model is trained with early stopping, then         :py, Return the predicted leaf every tree for each sample. If the model is trained, Get the special qid column from X if exists., Evaluate score for data using the last evaluation metric. If the model is, Decorate a learning to rank metric. (+3 more)

### Community 133 - "Community 133"
Cohesion: 0.14
Nodes (5): Create(), Finalize(), GlobalCommGroupFinalize(), GlobalCommGroupInit(), Init()

### Community 134 - "Community 134"
Cohesion: 0.12
Nodes (2): cuda_runtime, new

### Community 135 - "Community 135"
Cohesion: 0.18
Nodes (11): GetMemPolicy(), GetNumaHasCpuNodes(), GetNumaHasNormalMemoryNodes(), GetNumaMaxNumNodes(), GetNumaMemBind(), GetNumaNodeCpus(), ReadCpuList(), fstream (+3 more)

### Community 136 - "Community 136"
Cohesion: 0.17
Nodes (16): dask_delayed, _can_output_df(), _check_workers_are_alive(), _get_rabit_args(), _get_workers_from_data(), _infer_predict_output(), map_worker_partitions(), _maybe_dataframe() (+8 more)

### Community 137 - "Community 137"
Cohesion: 0.15
Nodes (6): Copy(), CopyBitPattern(), HostView(), LoadJson(), Save(), Sort()

### Community 138 - "Community 138"
Cohesion: 0.13
Nodes (13): approx_train(), hist_train(), Iterator, main(), make_batches(), Load a single batch of data., Advance the iterator by 1 step and pass the data to XGBoost.  This function, Reset the iterator to its beginning (+5 more)

### Community 139 - "Community 139"
Cohesion: 0.15
Nodes (6): input_split_base, BeforeFirst(), dmlc(), InitCachedIter(), InitPreprocIter(), threadediter

### Community 140 - "Community 140"
Cohesion: 0.21
Nodes (2): CVPack, XGBoost

### Community 141 - "Community 141"
Cohesion: 0.12
Nodes (1): TestEvalMetrics

### Community 142 - "Community 142"
Cohesion: 0.15
Nodes (9): call(), ClangTidy, Convert nvcc flags to corresponding clang flags., Subprocess run wrapper., Load and configure compile_commands and clang_tidy., See if clang-tidy and our regex is working correctly.  There are many subtleties, clang tidy wrapper.     Args:       args:  Command line arguments.           cpp, Run CMake to generate compilation database. (+1 more)

### Community 143 - "Community 143"
Cohesion: 0.16
Nodes (8): c_array(), Get the number of rows in the DMatrix., Update for one iteration, with objective function calculated         internally., Boost the booster for one iteration with customized gradient statistics., Evaluate a set of data.          Parameters         ----------         evals :, Evaluate the model on mat.          Parameters         ----------         data :, Predict with data.  The full model will be used unless `iteration_range` is, Convert a python array to c array.

### Community 144 - "Community 144"
Cohesion: 0.14
Nodes (9): Get the predictors from DMatrix as a CSR matrix. This getter is mostly for, Get quantile cuts for quantization.          .. versionadded:: 2.0.0, Get the number of columns (features) in the DMatrix., Get the number of non-missing values in the DMatrix.          .. versionadded::, Labels for features (column labels).          Setting it to ``None`` resets exis, Type of features (column types).          This is for displaying the results and, Feature types for this booster.  Can be directly set by input data or by, Feature names for this booster.  Can be directly set by input data or by (+1 more)

### Community 145 - "Community 145"
Cohesion: 0.15
Nodes (6): GetCfsCPUCount(), GetCGroupV1Count(), GetCGroupV2Count(), omp_get_thread_limit(), OmpGetThreadLimit(), pthread

### Community 146 - "Community 146"
Cohesion: 0.16
Nodes (13): contextlib, load_mslr_10k(), ranking_demo(), ranking_wo_split_demo(), Learning to rank with the Dask Interface =======================================, Learning to rank with data sorted locally., Learning to rank with data partitioned according to query groups., Load the MSLR10k dataset from data_path and save parquet files in the cache_path (+5 more)

### Community 147 - "Community 147"
Cohesion: 0.17
Nodes (7): IterForDMatrixDemo, main(), A data iterator for XGBoost DMatrix.      `reset` and `next` are required for an, Generate some random data for demostration.          Actual data can be anything, Utility function for obtaining current batch of data., Utility function for obtaining current batch of label., Yield the next batch of data.

### Community 148 - "Community 148"
Cohesion: 0.13
Nodes (3): Make sure CPU algorithm can handle GPU inputs, test_cpu_data_iterator(), test_data_iterator

### Community 149 - "Community 149"
Cohesion: 0.18
Nodes (11): get_model_categories(), _objective_decorator(), pick_ref_categories(), Configure parameters for :py:meth:`fit`., Fit gradient boosting model.          Note that calling ``fit()`` multiple times, Decorate or forward a custom objective.      Parameters     ----------     func:, Fit gradient boosting ranker          Note that calling ``fit()`` multiple times, Extract the optional reference categories from the booster. Used for training (+3 more)

### Community 150 - "Community 150"
Cohesion: 0.21
Nodes (5): byteorder, Communicator, getEnumOp(), getOperand(), getSize()

### Community 151 - "Community 151"
Cohesion: 0.26
Nodes (14): collections_abc, _create_dmatrix(), _create_quantile_dmatrix(), _dmatrix_from_list_of_parts(), _extract_data(), _get_dmatrices(), _get_is_cuda(), _get_worker_parts() (+6 more)

### Community 152 - "Community 152"
Cohesion: 0.18
Nodes (11): Accumulate(), AccumulateBitwise(), Allgather(), AllgatherFunctor, AllgatherV(), AllgatherVFunctor, Allreduce(), AllreduceFunctor (+3 more)

### Community 153 - "Community 153"
Cohesion: 0.14
Nodes (4): data(), Sync(), cuda_rt_utils, cuda_stream

### Community 154 - "Community 154"
Cohesion: 0.16
Nodes (8): DaskScikitLearnBase, DaskXGBClassifier, Temporarily set the client for sklearn model., Base class for implementing scikit-learn interface with Dask, Get the correct client, when method is invoked inside a worker we         should, _set_worker_client(), XGBClassifierMixIn, XGBModel

### Community 155 - "Community 155"
Cohesion: 0.15
Nodes (8): DeviceCheck(), FromDf(), HostCheck(), df_mock, OrdRecoderTest, ios, test_cat_container, test_ordinal

### Community 156 - "Community 156"
Cohesion: 0.15
Nodes (10): datasetutils, densevector, executionenvironment, DistTrainWithFlinkExample, mapoperator, tuple13, typehint, typeinformation (+2 more)

### Community 157 - "Community 157"
Cohesion: 0.16
Nodes (10): MLReader, Return the reader for loading the estimator., Return the reader for loading the model., Spark Xgboost estimator reader., Spark Xgboost model reader., Load metadata and model for a :py:class:`_SparkXGBModel`          :return: Spark, Get the xgboost.sklearn.XGBModel default parameters and filter out some, Set xgboost parameters into spark parameters (+2 more)

### Community 158 - "Community 158"
Cohesion: 0.14
Nodes (1): TestModels

### Community 159 - "Community 159"
Cohesion: 0.14
Nodes (1): TestBasic

### Community 160 - "Community 160"
Cohesion: 0.17
Nodes (7): run_allreduce(), run_broadcast(), run_rabit_ops(), test_allreduce(), test_broadcast(), test_rabit_ops(), test_rabit_ops_ipv6()

### Community 161 - "Community 161"
Cohesion: 0.27
Nodes (14): build_rpackage(), check_example_timing(), check_rmarkdown(), check_rpackage(), get_mingw_bin(), main(), pack_rpackage(), Utilities for packaging R code and running tests. (+6 more)

### Community 162 - "Community 162"
Cohesion: 0.21
Nodes (11): begin(), Clear(), Config(), end(), Insert(), IsGenuineString(), LoadFromStream(), MakeProtoStringValue() (+3 more)

### Community 163 - "Community 163"
Cohesion: 0.13
Nodes (7): DirectoryExcursion, make_dataset_strategy(), make_datasets_with_margin(), Contains a dataset in numpy format as well as the relevant objective and metric., Factory function for creating strategies that generates datasets with weight and, Change directory.  Change back and optionally cleaning up the directory when, TestDataset

### Community 164 - "Community 164"
Cohesion: 0.15
Nodes (3): CalcGain(), CalcGainGivenWeight(), CalcWeight()

### Community 165 - "Community 165"
Cohesion: 0.13
Nodes (11): ctypes2numpy(), _get_categories(), _numpy2ctypes_type(), _prediction_output(), Get the categories in the dataset.          .. versionadded:: 3.1.0          .., Same method as :py:meth:`DMatrix.get_categories`., Convert a ctypes pointer array to a numpy array., Run prediction in-place when possible, Unlike :py:meth:`predict` method, (+3 more)

### Community 166 - "Community 166"
Cohesion: 0.14
Nodes (4): broadcast, BroadcastTest, Worker, cuda_fp16

### Community 167 - "Community 167"
Cohesion: 0.22
Nodes (10): BeforeFirst(), Chunk::Append(), Chunk::Load(), ConvertToURIs(), Init(), InitInputFileInfo(), Read(), ReadChunk() (+2 more)

### Community 168 - "Community 168"
Cohesion: 0.21
Nodes (13): MakeParamsForTest(), Run(), TEST(), TEST_P(), TestDistributedMetric, UseCUDA(), UseFederated(), UseNCCL() (+5 more)

### Community 169 - "Community 169"
Cohesion: 0.19
Nodes (14): Java_ml_dmlc_xgboost4j_java_XGBoostJNI_TrackerWorkerArgs(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGBGetGlobalConfig(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGBoosterDumpModelEx(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGBoosterDumpModelExWithFeatures(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGBoosterEvalOneIter(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGBoosterGetAttr(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGBoosterGetAttrNames(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGBoosterGetStrFeatureInfo() (+6 more)

### Community 171 - "Community 171"
Cohesion: 0.23
Nodes (12): Params, HasArbitraryParamsDict, HasBaseMarginCol, HasContribPredictionCol, HasEnableSparseDataOptim, HasFeaturesCols, HasQueryIdCol, Xgboost pyspark integration submodule for params. (+4 more)

### Community 172 - "Community 172"
Cohesion: 0.33
Nodes (12): BaseParams(), BuildShapTestCases(), CheckDartShapOutput(), CheckShapAdditivity(), CheckShapHandlesDeepTree(), CheckShapHandlesZeroCover(), CheckShapOutput(), LoadGBTreeModel() (+4 more)

### Community 173 - "Community 173"
Cohesion: 0.19
Nodes (7): dmatrix_from_cudf(), Tests for constructing DMatrix from data structure conforming Apache     Arrow s, Test constructing DMatrix from cudf, _test_cudf_metainfo(), _test_cudf_training(), _test_from_cudf(), TestFromColumnar

### Community 174 - "Community 174"
Cohesion: 0.19
Nodes (7): IterForDMatrixTest, A data iterator for XGBoost DMatrix.      `reset` and `next` are required for an, Generate some random data for demostration.          Actual data can be anything, Utility function for obtaining current batch of data., Utility function for obtaining current batch of label., Yield next batch of data, test_from_cudf_iter()

### Community 175 - "Community 175"
Cohesion: 0.15
Nodes (8): get_family(), RabitTracker, Internal function for testing., Start the tracker. Once started, the client still need to call the         :py:m, Wait for the tracker to finish all the work and shutdown. When timeout is, Get network family from address., Get arguments for workers., Tracker for the collective used in XGBoost, acting as a coordinator between

### Community 176 - "Community 176"
Cohesion: 0.15
Nodes (4): c_api_utils, CommTest, comm, in_memory_handler

### Community 177 - "Community 177"
Cohesion: 0.17
Nodes (6): cctype, cstdio, direct, stat, MakeDirectory(), TEST()

### Community 178 - "Community 178"
Cohesion: 0.15
Nodes (2): ColumnBatch, CudfColumnBatch

### Community 179 - "Community 179"
Cohesion: 0.18
Nodes (3): Column, ColumnBatch, CudfColumn

### Community 180 - "Community 180"
Cohesion: 0.21
Nodes (10): CompareFloat(), CompareJSON(), CompareJsonModels(), L1SerializationTest, LogitSerializationTest, MultiClassesSerializationTest, SerializationTest, TEST_F() (+2 more)

### Community 181 - "Community 181"
Cohesion: 0.32
Nodes (4): ExSocket, Extension of socket to handle recv and send of special data, Starts the PS scheduler, SlaveEntry

### Community 182 - "Community 182"
Cohesion: 0.17
Nodes (9): hist_train(), Iterator, make_batches(), Advance the iterator by 1 step and pass the data to XGBoost.  This function, Reset the iterator to its beginning, The hist tree method can use a special data structure `ExtMemQuantileDMatrix` fo, Create multiple batches of synthetic data and return their file paths., A custom iterator for loading files in batches. (+1 more)

### Community 183 - "Community 183"
Cohesion: 0.15
Nodes (1): TestQuantileDMatrix

### Community 184 - "Community 184"
Cohesion: 0.15
Nodes (1): TestPandas

### Community 185 - "Community 185"
Cohesion: 0.18
Nodes (11): ClickFold, init_rank_score(), PBM, A structure containing information about generated user-click data., Simulate click data with position bias model. There are other models available i, Sample clicks for one query based on input relevance degree and position., We use XGBoost to generate the initial score instead of SVMRank for     simplici, Simulate clicks for one fold. (+3 more)

### Community 186 - "Community 186"
Cohesion: 0.15
Nodes (9): TestAlpha, TestLambda, TestMaxDeltaStep, TestMaxDeltaStepGain, TestMinChildWeight, TestMinSplitLoss, TestRegularization, TestSplitWithEta (+1 more)

### Community 187 - "Community 187"
Cohesion: 0.17
Nodes (9): XGBClassifierBase, Classes represented by this estimator., Metadata shared by the single-node and Dask regressor estimators., Metadata shared by the single-node and Dask classifier estimators., Tags used for scikit-learn data validation., Update ``sklearn.utils.Tags`` inherited from ``scikit-learn`` base classes., XGBClassifierMixIn, XGBRegressorMixIn (+1 more)

### Community 188 - "Community 188"
Cohesion: 0.20
Nodes (10): Example of training controller with NVFlare ====================================, SupportedTasks, nvflare_apis_client, nvflare_apis_executor, nvflare_apis_fl_constant, nvflare_apis_fl_context, nvflare_apis_impl_controller, nvflare_apis_shareable (+2 more)

### Community 189 - "Community 189"
Cohesion: 0.20
Nodes (8): CommunicatorContext, DaskDMatrix, DaskQuantileDMatrix, A context controlling collective communicator initialization and finalization., DMatrix holding on references to Dask DataFrame or Dask Array.  Constructing a, Obtain references to local data., Create a dictionary of objects that can be pickled for function         argument, A dask version of :py:class:`QuantileDMatrix`. See :py:class:`DaskDMatrix` for

### Community 190 - "Community 190"
Cohesion: 0.21
Nodes (8): hdfs, hdfs_filesys, ConvertPathInfo(), GetPathInfo(), HDFSStream, ListDirectory(), Open(), OpenForRead()

### Community 191 - "Community 191"
Cohesion: 0.23
Nodes (12): ApplyMvsWeights(), ApplySampling(), CalcRegAbsGrad(), CalcSamplingInfo(), CalculateThreshold(), ForEachGradientSample(), GradientBasedSampling(), IsSampled() (+4 more)

### Community 192 - "Community 192"
Cohesion: 0.21
Nodes (5): BeforeFirst(), NextBatch(), NextBatchEx(), NextChunk(), ResetPartition()

### Community 193 - "Community 193"
Cohesion: 0.18
Nodes (6): Download and setup the test fixtures, Cleanup test artifacts from download and unpacking         :return:, Train an XGBoost ranking model, Test cross-validation with a group specified, Retrieve the group number from the dmatrix, TestRanking

### Community 194 - "Community 194"
Cohesion: 0.18
Nodes (8): cache_partitions(), create_dmatrix_from_partitions(), make_qdm(), PartIter, Handle empty partition for QuantileDMatrix., Create DMatrix from spark data partitions.      Parameters     ----------     it, Extract partitions from pyspark iterator. `append` is a user defined function fo, Iterator for creating Quantile DMatrix from partitions.

### Community 195 - "Community 195"
Cohesion: 0.18
Nodes (12): _assert_monotone(), is_correctly_constrained(), is_decreasing(), is_increasing(), Check for a positive (``f0``) and negative (``f1``) constraint., Grid-check monotonicity per output column for every constrained feature.      Fo, Whether ``v`` is nondecreasing along the sweep axis., Monotonicity check for deep trees with mixed feature constraints.      Uses more (+4 more)

### Community 196 - "Community 196"
Cohesion: 0.17
Nodes (7): _ProxyDMatrix, A placeholder class when DMatrix cannot be constructed (QuantileDMatrix,     inp, Reference data from CUDA array interface., Reference data from CUDA columnar format., Reference data from numpy array., Reference data from a CPU DataFrame., Reference data from scipy csr.

### Community 197 - "Community 197"
Cohesion: 0.20
Nodes (3): AutoCloseable, Column, ConfigContext

### Community 198 - "Community 198"
Cohesion: 0.20
Nodes (8): azure_filesys, blob, containerstream, filestream, ListDirectory(), split(), stdafx, storage_account

### Community 199 - "Community 199"
Cohesion: 0.27
Nodes (8): bitset, Bits(), Capacity(), Check(), Clear(), Set(), Shift(), device_ptr

### Community 200 - "Community 200"
Cohesion: 0.20
Nodes (4): Print(), PrintStatistics(), nvtx3, nvtx_utils

### Community 201 - "Community 201"
Cohesion: 0.22
Nodes (11): ArrayInterfaceImpl(), DecompAllowFallback(), FileExists(), GenerateArrayInterface(), GenerateColumnarArrayInterface(), GenerateDense(), GenerateExtMemQuantileDMatrix(), GenerateLabels() (+3 more)

### Community 202 - "Community 202"
Cohesion: 0.25
Nodes (8): create_job_manifest(), create_ps_manifest(), create_sched_job_manifest(), create_sched_svc_manifest(), create_svc_manifest(), create_wk_manifest(), kubernetes, yaml

### Community 203 - "Community 203"
Cohesion: 0.22
Nodes (9): Exception, XGBoostError, platform, find_lib_path(), is_sphinx_build(), Error thrown by when xgboost is not found, `XGBOOST_BUILD_DOC` is used by the sphinx conf.py to skip building the C++ code., Find the path to xgboost dynamic library files.      Returns     -------     lib (+1 more)

### Community 204 - "Community 204"
Cohesion: 0.22
Nodes (10): make_example_data(), native(), pipeline(), Feature engineering pipeline for categorical data ==============================, Using the sklearn pipeline., Generate data for demo., Using the native XGBoost interface., sklearn_compose (+2 more)

### Community 205 - "Community 205"
Cohesion: 0.29
Nodes (10): aws_s3_download(), aws_s3_download_with_wildcard(), aws_s3_upload(), compute_s3_url(), download(), path_equals(), Upload an artifact to an S3 bucket for later use Note. This script takes in all, resolve() (+2 more)

### Community 206 - "Community 206"
Cohesion: 0.18
Nodes (1): xgboost_testing_intercept

### Community 207 - "Community 207"
Cohesion: 0.22
Nodes (7): filepath_enumerate(), Lint, main(), process(), Print summary of lint., Enumerate the file paths of all subfiles of the list of paths, Print summary of certain result map.

### Community 208 - "Community 208"
Cohesion: 0.22
Nodes (11): AddMissingToJson(), CreateFromSparse(), MakeJsonConfigForArray(), XGBoosterPredictFromColumnar_R(), XGBoosterPredictFromCSR_R(), XGBoosterPredictFromDense_R(), XGBoosterPredictFromDMatrix_R(), XGBoosterPredictGeneric() (+3 more)

### Community 209 - "Community 209"
Cohesion: 0.18
Nodes (2): shape, works

### Community 210 - "Community 210"
Cohesion: 0.20
Nodes (9): CommunicatorContext, finalize(), _find_nccl(), init(), is_distributed(), Finalize the communicator., If the collective communicator is distributed., A context controlling collective communicator initialization and finalization. (+1 more)

### Community 211 - "Community 211"
Cohesion: 0.27
Nodes (11): dispatch_meta_backend(), _has_array_protocol(), _meta_from_arrow_table(), _meta_from_cudf_df(), _meta_from_cudf_series(), _meta_from_list(), _meta_from_numpy(), _meta_from_pandas_df() (+3 more)

### Community 212 - "Community 212"
Cohesion: 0.18
Nodes (11): _from_cudf_df(), _from_pandas_series(), _invalid_dataframe_dtype(), is_nullable_dtype(), is_pd_cat_dtype(), _lazy_load_cudf_is_bool(), _lazy_load_cudf_is_cat(), _lazy_load_pd_is_cat() (+3 more)

### Community 213 - "Community 213"
Cohesion: 0.22
Nodes (6): assertequals, asserttrue, getlibrarypathfor, LibraryPathProviderTest, linux, x86_64

### Community 214 - "Community 214"
Cohesion: 0.22
Nodes (5): DaskXGBRegressor, DaskXGBRFClassifier, DaskXGBRFRegressor, dummy doc string to workaround pylint, replaced by the decorator., XGBRegressorMixIn

### Community 215 - "Community 215"
Cohesion: 0.24
Nodes (9): get_family(), get_host_ip(), get_some_ip(), main(), Tracker script for DMLC Implements the tracker control protocol  - start dmlc jo, Standalone function to start rabit tracker.     Parameters     ----------     ar, Main function if tracker is executed in standalone mode., start_rabit_tracker() (+1 more)

### Community 216 - "Community 216"
Cohesion: 0.20
Nodes (1): classification

### Community 217 - "Community 217"
Cohesion: 0.40
Nodes (9): main(), Matrix_ArrayInterface(), Matrix_At(), Matrix_Create(), Matrix_Free(), Matrix_NFeatures(), Matrix_NSamples(), Matrix_Print() (+1 more)

### Community 218 - "Community 218"
Cohesion: 0.24
Nodes (8): MLWriter, Return the writer for saving the estimator., Return the writer for saving the model., Spark Xgboost estimator writer., Spark Xgboost model writer., Save metadata and model for a :py:class:`_SparkXGBModel`         - save metadata, SparkXGBModelWriter, SparkXGBWriter

### Community 219 - "Community 219"
Cohesion: 0.20
Nodes (10): Java_ml_dmlc_xgboost4j_java_XGBoostJNI_TrackerCreate(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGBoosterCreate(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGDMatrixCreateFromArrayInterfaceColumns(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGDMatrixCreateFromDataIter(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGDMatrixCreateFromMat(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGDMatrixCreateFromMatRef(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGDMatrixCreateFromURI(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGDMatrixSliceDMatrix() (+2 more)

### Community 220 - "Community 220"
Cohesion: 0.60
Nodes (9): booster_json(), booster_ubj(), generate_aft_survival_models(), generate_classification_model(), generate_logistic_model(), generate_ranking_model(), generate_regression_model(), skl_json() (+1 more)

### Community 221 - "Community 221"
Cohesion: 0.29
Nodes (4): build_dataset(), load_pickle(), save_pickle(), TestPickling

### Community 222 - "Community 222"
Cohesion: 0.22
Nodes (4): json_model(), Saving and loading model files from paths., Test mis-specified model format, no special hanlding is expected, the         JS, TestBoosterIO

### Community 223 - "Community 223"
Cohesion: 0.29
Nodes (8): TransformedDf, ArrowTransformed, CudfTransformed, PandasTransformed, A storage class for transformed cuDF dataframe., A storage class for transformed pandas DataFrame., Return shape of the transformed DataFrame., A storage class for transformed arrow table.

### Community 224 - "Community 224"
Cohesion: 0.25
Nodes (7): plot_censored_labels(), PlotIntermediateModel, Visual demo for survival analysis (regression) with Accelerated Failure Time (AF, Function to visualize censored labels, Custom callback to plot intermediate models., Run after training is finished., matplotlib_pyplot

### Community 225 - "Community 225"
Cohesion: 0.31
Nodes (6): cache_manager, DetectDataCaches(), DetectDataCachesSysfs(), GetCacheInfo(), ParseCacheSize(), RunCpuid()

### Community 226 - "Community 226"
Cohesion: 0.28
Nodes (4): DaskPartitionIter, A data iterator for the `DaskQuantileDMatrix`., Utility function for obtaining current batch of data., Yield next batch of data

### Community 227 - "Community 227"
Cohesion: 0.22
Nodes (8): _get_client(), _get_dask_config(), predict(), Run prediction with a trained booster.      .. note::          Using ``inplace_p, The dask client used in this model.  The `Client` object can not be         seri, Simple wrapper around testing None., Train XGBoost model.      .. versionadded:: 1.0.0      .. note::          Other, train()

### Community 228 - "Community 228"
Cohesion: 0.44
Nodes (1): ExternalCheckpointManager

### Community 229 - "Community 229"
Cohesion: 0.22
Nodes (4): Test whether prediction is correct., Under invalid CUDA_VISIBLE_DEVICES, context should reset, Test the device context is preserved after pickling., TestLoadPickle

### Community 230 - "Community 230"
Cohesion: 0.22
Nodes (1): TestGPUEvalMetrics

### Community 231 - "Community 231"
Cohesion: 0.28
Nodes (2): Test trees_to_dataframe with indicator (boolean) features., TestTreesToDataFrame

### Community 232 - "Community 232"
Cohesion: 0.22
Nodes (3): Tests for running inplace prediction., run_threaded_predict(), TestInplacePredict

### Community 233 - "Community 233"
Cohesion: 0.22
Nodes (3): index, or, separately

### Community 234 - "Community 234"
Cohesion: 0.36
Nodes (8): dmlc_usleep(), GetDurationInMilliseconds(), GetDurationInNanoseconds(), Now(), TEST(), this_is_thread_func(), thread_group, windows

### Community 235 - "Community 235"
Cohesion: 0.22
Nodes (2): class, with

### Community 236 - "Community 236"
Cohesion: 0.29
Nodes (6): assert, ctime, cxxabi, dmlc(), GetEntry(), stdexcept

### Community 237 - "Community 237"
Cohesion: 0.29
Nodes (3): Report(), SafeColl(), stack

### Community 238 - "Community 238"
Cohesion: 0.25
Nodes (3): Controller, Controller for federated XGBoost.          Args:             port: the port for, XGBoostController

### Community 239 - "Community 239"
Cohesion: 0.29
Nodes (3): cstdlib, unistd, windefs

### Community 240 - "Community 240"
Cohesion: 0.29
Nodes (7): _direct_predict_impl(), _get_model_future(), inplace_predict(), _inplace_predict_async(), _predict_async(), Inplace prediction. See doc in :py:meth:`xgboost.Booster.inplace_predict` for, Get the number of columns (features) in the DMatrix.          Returns         --

### Community 242 - "Community 242"
Cohesion: 0.36
Nodes (5): DataIterator_Free(), DataIterator_Init(), main(), TrainModel(), stddef

### Community 243 - "Community 243"
Cohesion: 0.25
Nodes (1): test_multiclass_obj

### Community 244 - "Community 244"
Cohesion: 0.25
Nodes (5): Unit tests using pathlib.Path for file interaction., Initialization from the data path., Saving to a binary file using pathlib from a DMatrix., An invalid model_file path should raise XGBoostError., TestBasicPathLike

### Community 246 - "Community 246"
Cohesion: 0.25
Nodes (6): _get_unwrapped_vec_cols(), XGBoost model trained with features_cols parameter can also predict         vect, Values in feature columns must be integral types or float/double types, It handles     1. Convert vector type to array type     2. Cast to Array(Float32, _validate_and_convert_feature_col_as_array_col(), _validate_and_convert_feature_col_as_float_col_list()

### Community 247 - "Community 247"
Cohesion: 0.32
Nodes (3): ~ConsoleLogger(), CustomLogMessage::Log(), ShouldLog()

### Community 248 - "Community 248"
Cohesion: 0.25
Nodes (8): _make_leaf_dmatrix(), _predict_leaf(), Make a prediction matrix and an in-memory reference for external memory., Predict leaves and compare external memory against in-memory data., Validate that each predicted node is a leaf in the corresponding tree., Run tests for leaf index prediction., run_predict_leaf(), _validate_leaf_indices()

### Community 249 - "Community 249"
Cohesion: 0.39
Nodes (1): BigDenseMatrix

### Community 250 - "Community 250"
Cohesion: 0.25
Nodes (6): _check_distributed_params(), _expect(), Translate input error into string.      Parameters     ----------     expectatio, Slice the DMatrix and return a new DMatrix that only contains `rindex`., Validate parameters in distributed environments., Get a slice of the tree-based model. Attributes like `best_iteration` and

### Community 251 - "Community 251"
Cohesion: 0.29
Nodes (1): array

### Community 252 - "Community 252"
Cohesion: 0.43
Nodes (6): main(), MakeArrayInterface(), MakeConfig(), MakeDMatrixConfig(), stdint, stdio

### Community 253 - "Community 253"
Cohesion: 0.48
Nodes (6): charconv, Int32Bits2Float(), TEST(), TestInteger(), TestRyu(), TestRyuParse()

### Community 254 - "Community 254"
Cohesion: 0.33
Nodes (3): cinttypes, DecRef(), reset()

### Community 255 - "Community 255"
Cohesion: 0.29
Nodes (4): _async_wrap_evaluation_matrices(), DaskXGBRanker, A switch function for async environment., XGBRankerMixIn

### Community 256 - "Community 256"
Cohesion: 0.29
Nodes (1): EllpackPageImpl

### Community 257 - "Community 257"
Cohesion: 0.29
Nodes (4): DataIter, IteratorForTest, Iterator for testing streaming DMatrix. (external memory, quantile), Return concatenated arrays.

### Community 258 - "Community 258"
Cohesion: 0.52
Nodes (1): Client

### Community 259 - "Community 259"
Cohesion: 0.38
Nodes (3): MapFunction, XGBoost, RichMapPartitionFunction

### Community 260 - "Community 260"
Cohesion: 0.33
Nodes (4): custom_callback(), Plotting, Plot evaluation result during training.  Only for demonstration purpose as it's, Demo for defining a custom callback function that plots evaluation result during

### Community 261 - "Community 261"
Cohesion: 0.33
Nodes (6): http_client, main(), Helper script for triggering Read the docs build.  See `doc/contrib/docs.rst <ht, trigger_build(), pprint, requests

### Community 262 - "Community 262"
Cohesion: 0.33
Nodes (2): ITracker, RabitTracker

### Community 263 - "Community 263"
Cohesion: 0.29
Nodes (2): ITracker, UncaughtExceptionHandler

### Community 264 - "Community 264"
Cohesion: 0.71
Nodes (6): CheckDevice(), CheckHost(), InitHostDeviceVector(), PlusOne(), TEST(), TestHostDeviceVector()

### Community 265 - "Community 265"
Cohesion: 0.29
Nodes (1): TestInteractionConstraints

### Community 266 - "Community 266"
Cohesion: 0.48
Nodes (1): TestTrainingContinuation

### Community 268 - "Community 268"
Cohesion: 0.29
Nodes (4): classification, is, prevalence, weighted

### Community 269 - "Community 269"
Cohesion: 0.29
Nodes (4): Save the metadata of an xgboost.spark._SparkXGBEstimator or         xgboost.spar, Load the metadata and the instance of an xgboost.spark._SparkXGBEstimator or, Set collective configuration, _SparkXGBSharedReadWrite

### Community 270 - "Community 270"
Cohesion: 0.29
Nodes (1): xgboost_r

### Community 271 - "Community 271"
Cohesion: 0.38
Nodes (7): GetProxyDMatrixWithBaseMargin(), MakeArrayInterfaceFromRMat(), MakeArrayInterfaceFromRVector(), XGBoosterTrainOneIter_R(), XGDMatrixSetInfo_R(), XGProxyDMatrixSetDataCSR_R(), XGProxyDMatrixSetDataDense_R()

### Community 272 - "Community 272"
Cohesion: 0.38
Nodes (4): run_dmatrix_ctor(), test_dmatrix_ctor(), test_dmatrix_ctor_gpu(), xgboost_spark_data

### Community 273 - "Community 273"
Cohesion: 0.29
Nodes (3): CatIter, An iterator for testing categorical features., Return the concatenated data.

### Community 275 - "Community 275"
Cohesion: 0.52
Nodes (6): CheckReload(), ConstructTree(), ConstructTreeCat(), GrowTree(), TEST(), TestCategoricalTreeDump()

### Community 276 - "Community 276"
Cohesion: 0.29
Nodes (4): ctypes2buffer(), Convert ctypes pointer to buffer type., Save the model to a in memory buffer representation instead of file.          Th, Parse a boosted tree model into a pandas DataFrame.          This feature is onl

### Community 277 - "Community 277"
Cohesion: 0.43
Nodes (6): _as_booster(), _as_prediction_dmatrix(), _get_iteration_range(), Interpretability functions for XGBoost models., Return SHAP values for an XGBoost model.      .. warning::        This function, shap_values()

### Community 278 - "Community 278"
Cohesion: 0.40
Nodes (6): CopyCatContainer(), GetCategoriesImpl(), XGBoosterGetCategories(), XGBoosterGetCategoriesExportToArrow(), XGDMatrixGetCategories(), XGDMatrixGetCategoriesExportToArrow()

### Community 279 - "Community 279"
Cohesion: 0.33
Nodes (6): GetDMatrixProxy(), XGProxyDMatrixSetDataColumnar(), XGProxyDMatrixSetDataCSR(), XGProxyDMatrixSetDataCudaArrayInterface(), XGProxyDMatrixSetDataCudaColumnar(), XGProxyDMatrixSetDataDense()

### Community 280 - "Community 280"
Cohesion: 0.33
Nodes (6): ValidateCAPIDataSplitMode(), XGDMatrixCreateFromColumnar(), XGDMatrixCreateFromCSC(), XGDMatrixCreateFromCSR(), XGDMatrixCreateFromDense(), XGDMatrixCreateFromURI()

### Community 282 - "Community 282"
Cohesion: 0.33
Nodes (4): ForIntrusivePtrTest, IntrusivePtrCell, NotCopyConstructible, intrusive_ptr

### Community 283 - "Community 283"
Cohesion: 0.33
Nodes (6): CreateTrainedGBM(), GenerateCSR(), GenerateDMatrix(), GetMetricEval(), GetMultiMetricEval(), RandomDataGenerator()

### Community 284 - "Community 284"
Cohesion: 0.40
Nodes (3): Trainer for federated XGBoost.          Args:             server_address: addres, XGBoostTrainer, Executor

### Community 286 - "Community 286"
Cohesion: 0.40
Nodes (5): config_logger(), main(), Job submission script, Configure the logger according to the arguments      Parameters     ----------, Main submission function.

### Community 287 - "Community 287"
Cohesion: 0.33
Nodes (1): xgboost_testing_monotone_constraints

### Community 288 - "Community 288"
Cohesion: 0.33
Nodes (1): TestSYCLPredict

### Community 289 - "Community 289"
Cohesion: 0.53
Nodes (2): TestLinear, train_result()

### Community 290 - "Community 290"
Cohesion: 0.33
Nodes (1): TestArrowTable

### Community 291 - "Community 291"
Cohesion: 0.33
Nodes (5): RabitTracker, FederatedTracker, Tracker for federated training.      Parameters     ----------     n_workers :, See :py:class:`~xgboost.federated.FederatedTracker` for more info.      Paramete, run_federated_server()

### Community 292 - "Community 292"
Cohesion: 0.33
Nodes (4): rdynload, rinternals, stdlib, visibility

### Community 293 - "Community 293"
Cohesion: 0.53
Nodes (6): XGBAltrepDeserializer_R(), XGBAltrepDuplicate_R(), XGBAltrepSetPointer(), XGBMakeEmptyAltrep(), XGBoosterCreate_R(), XGBoosterSlice_R()

### Community 294 - "Community 294"
Cohesion: 0.40
Nodes (6): data_dir(), demo_dir(), load_agaricus(), normpath(), project_root(), Look for the demo directory based on the test file name.

### Community 296 - "Community 296"
Cohesion: 0.33
Nodes (4): Config, User configuration for the communicator context. This is used for easier     int, Worker side arguments resolution., Update the arguments for the communicator.

### Community 297 - "Community 297"
Cohesion: 0.33
Nodes (6): _from_scipy_csc(), _from_scipy_csr(), Ensure correct data alignment and data type for scipy sparse inputs. Input shoul, Initialize data from a CSR matrix., Initialize data from a CSC matrix., transform_scipy_sparse()

### Community 298 - "Community 298"
Cohesion: 0.40
Nodes (5): GetDMatrixIntegralInfo(), XGDMatrixDataSplitMode(), XGDMatrixNumCol(), XGDMatrixNumNonMissing(), XGDMatrixNumRow()

### Community 299 - "Community 299"
Cohesion: 0.40
Nodes (5): XGBoostDumpModelImpl(), XGBoosterDumpModel(), XGBoosterDumpModelEx(), XGBoosterDumpModelExWithFeatures(), XGBoosterDumpModelWithFeatures()

### Community 300 - "Community 300"
Cohesion: 0.40
Nodes (2): c_api_error, jni

### Community 301 - "Community 301"
Cohesion: 0.40
Nodes (1): set

### Community 302 - "Community 302"
Cohesion: 0.70
Nodes (4): TEST(), TestBasic(), TestWeightedMultiSampling(), TestWeightedSampling()

### Community 303 - "Community 303"
Cohesion: 0.40
Nodes (3): field, unsafe, UtilUnsafe

### Community 304 - "Community 304"
Cohesion: 0.40
Nodes (4): NamedTuple, Simple data struct for holding a train-test split of a learning to rank dataset., Whether the label consists of binary relevance degree., RelDataCV

### Community 305 - "Community 305"
Cohesion: 0.50
Nodes (1): TestGPUBasicModels

### Community 306 - "Community 306"
Cohesion: 0.40
Nodes (1): TestGPUInteractionConstraints

### Community 307 - "Community 307"
Cohesion: 0.50
Nodes (2): TestGPULinear, train_result()

### Community 308 - "Community 308"
Cohesion: 0.40
Nodes (1): TestDMatrixColumnSplitRemoved

### Community 309 - "Community 309"
Cohesion: 0.50
Nodes (1): TestEarlyStopping

### Community 310 - "Community 310"
Cohesion: 0.40
Nodes (2): Integration tests for tree methods., TestTreeMethodMulti

### Community 311 - "Community 311"
Cohesion: 0.50
Nodes (1): TestPlotting

### Community 312 - "Community 312"
Cohesion: 0.40
Nodes (1): TestTreeRegularization

### Community 313 - "Community 313"
Cohesion: 0.40
Nodes (1): TestModin

### Community 314 - "Community 314"
Cohesion: 0.40
Nodes (2): classification, is

### Community 315 - "Community 315"
Cohesion: 0.40
Nodes (1): xgb

### Community 316 - "Community 316"
Cohesion: 0.40
Nodes (1): xgboost_testing_federated

### Community 318 - "Community 318"
Cohesion: 0.40
Nodes (1): TestPySparkLocalLETOR

### Community 319 - "Community 319"
Cohesion: 0.40
Nodes (1): provided

### Community 320 - "Community 320"
Cohesion: 0.67
Nodes (3): array_view, ArrayViewTest(), TEST()

### Community 321 - "Community 321"
Cohesion: 0.50
Nodes (4): CopyGradientFromArrays(), XGBoosterBoostOneIter(), XGBoosterTrainOneIter(), XGBoosterTrainOneIterWithSplitGrad()

### Community 322 - "Community 322"
Cohesion: 0.67
Nodes (4): GetRefDMatrix(), WarnDeprecatedMaxQuantileBlocks(), XGExtMemQuantileDMatrixCreateFromCallback(), XGQuantileDMatrixCreateFromCallback()

### Community 323 - "Community 323"
Cohesion: 0.50
Nodes (4): InplacePredictImpl(), XGBoosterPredictFromColumnar(), XGBoosterPredictFromCSR(), XGBoosterPredictFromDense()

### Community 324 - "Community 324"
Cohesion: 0.50
Nodes (3): CCtx, CommunicatorContext, Context with PySpark specific task ID.

### Community 326 - "Community 326"
Cohesion: 0.67
Nodes (4): ArrayIterForTest(), GenerateArrayInterfaceBatch(), MakeArrayInterfaceBatch(), NumpyArrayIterForTest()

### Community 327 - "Community 327"
Cohesion: 0.83
Nodes (1): BasicWalkThrough

### Community 328 - "Community 328"
Cohesion: 0.67
Nodes (1): XGBoostTest

### Community 329 - "Community 329"
Cohesion: 0.50
Nodes (2): SyclPredictionCache, test_prediction_cache

### Community 330 - "Community 330"
Cohesion: 0.50
Nodes (1): xgboost_testing_parse_tree

### Community 331 - "Community 331"
Cohesion: 0.83
Nodes (1): TestSYCLTrainingContinuation

### Community 332 - "Community 332"
Cohesion: 0.67
Nodes (2): TestSYCLUpdaters, train_result()

### Community 333 - "Community 333"
Cohesion: 0.50
Nodes (1): TestMonotoneConstraints

### Community 334 - "Community 334"
Cohesion: 0.50
Nodes (2): classification, separately

### Community 335 - "Community 335"
Cohesion: 0.50
Nodes (1): DirectoryExcursion

### Community 336 - "Community 336"
Cohesion: 0.50
Nodes (3): Create an XGBoostTrainingSummary instance from a nested dictionary of metrics., A class that holds the training and validation objective history     of an XGBoo, XGBoostTrainingSummary

### Community 337 - "Community 337"
Cohesion: 0.50
Nodes (4): CopyArrayToR(), SafeAllocInteger(), SafeAllocReal(), XGDMatrixGetQuantileCut_R()

### Community 338 - "Community 338"
Cohesion: 0.50
Nodes (1): TestDaskCallbacks

### Community 339 - "Community 339"
Cohesion: 0.50
Nodes (4): has_ipv6(), no_ipv6(), PyTest skip mark for IPv6., Check whether IPv6 is enabled on this host.

### Community 340 - "Community 340"
Cohesion: 0.50
Nodes (3): Callback for testing multi-output., ResetStrategy, TrainingCallback

### Community 341 - "Community 341"
Cohesion: 0.50
Nodes (4): _from_cupy_array(), _meta_from_cupy_array(), Initialize DMatrix from cupy ndarray., _transform_cupy_array()

### Community 342 - "Community 342"
Cohesion: 0.67
Nodes (3): DispatchModelType(), XGBoosterLoadModel(), XGBoosterLoadModelFromBuffer()

### Community 343 - "Community 343"
Cohesion: 0.67
Nodes (3): OldGetInfoImpl(), XGDMatrixGetFloatInfo(), XGDMatrixGetUIntInfo()

### Community 344 - "Community 344"
Cohesion: 0.67
Nodes (1): pseudo_huber

### Community 345 - "Community 345"
Cohesion: 0.67
Nodes (3): _add_column(), no_group_split(), A function to prevent query group from being scattered to different     workers.

### Community 347 - "Community 347"
Cohesion: 0.67
Nodes (1): ConfigContextTest

### Community 348 - "Community 348"
Cohesion: 0.67
Nodes (1): QuantileCut

### Community 349 - "Community 349"
Cohesion: 0.67
Nodes (3): Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGDMatrixCreateFromCSC(), Java_ml_dmlc_xgboost4j_java_XGBoostJNI_XGDMatrixCreateFromCSR(), MakeJVMSparseInput()

### Community 352 - "Community 352"
Cohesion: 0.67
Nodes (1): xgb

### Community 353 - "Community 353"
Cohesion: 0.67
Nodes (3): MakeArrayInterfaceFromRDataFrame(), XGDMatrixCreateFromDF_R(), XGProxyDMatrixSetDataColumnar_R()

### Community 354 - "Community 354"
Cohesion: 0.67
Nodes (3): XGDMatrixCreateFromCallback_R(), XGDMatrixCreateFromCallbackGeneric_R(), XGQuantileDMatrixCreateFromCallback_R()

### Community 355 - "Community 355"
Cohesion: 1.00
Nodes (2): setenv(), TEST()

### Community 356 - "Community 356"
Cohesion: 0.67
Nodes (3): is_windows(), Check if the current platform is Windows., skip_win()

### Community 359 - "Community 359"
Cohesion: 0.67
Nodes (2): names, predictions

### Community 360 - "Community 360"
Cohesion: 1.00
Nodes (2): XGBBuildInfoDevice(), XGBuildInfo()

### Community 361 - "Community 361"
Cohesion: 1.00
Nodes (2): XGDMatrixSliceDMatrix(), XGDMatrixSliceDMatrixEx()

### Community 362 - "Community 362"
Cohesion: 1.00
Nodes (1): DMLC Tracker modules for running jobs on different platforms.

### Community 363 - "Community 363"
Cohesion: 1.00
Nodes (1): elementwise_metric

### Community 368 - "Community 368"
Cohesion: 1.00
Nodes (1): multiclass_metric

### Community 369 - "Community 369"
Cohesion: 1.00
Nodes (1): survival_metric

### Community 370 - "Community 370"
Cohesion: 1.00
Nodes (2): run_sklearn_api(), test_sklearn_api()

### Community 371 - "Community 371"
Cohesion: 1.00
Nodes (2): run_validation_weights(), test_validation_weights()

### Community 382 - "Community 382"
Cohesion: 1.00
Nodes (2): _DMatrixFinalizer(), XGDMatrixFree_R()

### Community 383 - "Community 383"
Cohesion: 1.00
Nodes (2): SafeMkChar(), XGBoosterDumpModel_R()

### Community 384 - "Community 384"
Cohesion: 1.00
Nodes (2): captured_output(), Reassign stdout temporarily in order to test printed statements     Taken from:

### Community 385 - "Community 385"
Cohesion: 1.00
Nodes (2): eval_error_metric_skl(), Evaluation metric that looks like metrics provided by sklearn.

### Community 386 - "Community 386"
Cohesion: 1.00
Nodes (2): eval_error_metric(), Evaluation metric for xgb.train.      Parameters     ----------     rev_link : W

### Community 387 - "Community 387"
Cohesion: 1.00
Nodes (2): logregobj(), Binary regression custom objective.

### Community 388 - "Community 388"
Cohesion: 1.00
Nodes (2): make_regression(), Make a simple regression dataset.

### Community 389 - "Community 389"
Cohesion: 1.00
Nodes (2): Custom softprob objective for testing.      Parameters     ----------     use_cu, softprob_obj()

### Community 390 - "Community 390"
Cohesion: 1.00
Nodes (2): Make a pytest mark for the `pytest-timeout` package.      Parameters     -------, timeout()

### Community 394 - "Community 394"
Cohesion: 1.00
Nodes (1): Return the evaluation results.          If **eval_set** is passed to the :py:met

## Knowledge Gaps
- **1088 isolated node(s):** `classification`, `index`, `from`, `in`, `if` (+1083 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 22`** (1 nodes): `XGBoostJNI`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (1 nodes): `sklearn_utils_estimator_checks`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (2 nodes): `jvm_utils`, `xgboost4j`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (2 nodes): `Booster`, `getPType()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (1 nodes): `xgboost_testing_ordinal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (1 nodes): `BoosterImplTest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 60`** (2 nodes): `as`, `is`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 78`** (1 nodes): `DMatrix`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 97`** (1 nodes): `DMatrixTest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 109`** (2 nodes): `Test inplace predict with different device and data types.          The sklearn`, `TestGPUPredict`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 115`** (1 nodes): `TestGPUUpdaters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 116`** (1 nodes): `TestDMatrix`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 117`** (2 nodes): `Test rng has an effect on column sampling.`, `TestTreeMethod`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 130`** (2 nodes): `Test the ordering of the callbacks is preserved.`, `TestCallbacks`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 134`** (2 nodes): `cuda_runtime`, `new`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 140`** (2 nodes): `CVPack`, `XGBoost`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 141`** (1 nodes): `TestEvalMetrics`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 158`** (1 nodes): `TestModels`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 159`** (1 nodes): `TestBasic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 178`** (2 nodes): `ColumnBatch`, `CudfColumnBatch`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 183`** (1 nodes): `TestQuantileDMatrix`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 184`** (1 nodes): `TestPandas`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 206`** (1 nodes): `xgboost_testing_intercept`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 209`** (2 nodes): `shape`, `works`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 216`** (1 nodes): `classification`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 228`** (1 nodes): `ExternalCheckpointManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 230`** (1 nodes): `TestGPUEvalMetrics`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 231`** (2 nodes): `Test trees_to_dataframe with indicator (boolean) features.`, `TestTreesToDataFrame`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 235`** (2 nodes): `class`, `with`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 243`** (1 nodes): `test_multiclass_obj`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 249`** (1 nodes): `BigDenseMatrix`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 251`** (1 nodes): `array`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 256`** (1 nodes): `EllpackPageImpl`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 258`** (1 nodes): `Client`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 262`** (2 nodes): `ITracker`, `RabitTracker`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 263`** (2 nodes): `ITracker`, `UncaughtExceptionHandler`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 265`** (1 nodes): `TestInteractionConstraints`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 266`** (1 nodes): `TestTrainingContinuation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 270`** (1 nodes): `xgboost_r`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 287`** (1 nodes): `xgboost_testing_monotone_constraints`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 288`** (1 nodes): `TestSYCLPredict`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 289`** (2 nodes): `TestLinear`, `train_result()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 290`** (1 nodes): `TestArrowTable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 300`** (2 nodes): `c_api_error`, `jni`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 301`** (1 nodes): `set`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 305`** (1 nodes): `TestGPUBasicModels`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 306`** (1 nodes): `TestGPUInteractionConstraints`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 307`** (2 nodes): `TestGPULinear`, `train_result()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 308`** (1 nodes): `TestDMatrixColumnSplitRemoved`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 309`** (1 nodes): `TestEarlyStopping`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 310`** (2 nodes): `Integration tests for tree methods.`, `TestTreeMethodMulti`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 311`** (1 nodes): `TestPlotting`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 312`** (1 nodes): `TestTreeRegularization`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 313`** (1 nodes): `TestModin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 314`** (2 nodes): `classification`, `is`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 315`** (1 nodes): `xgb`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 316`** (1 nodes): `xgboost_testing_federated`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 318`** (1 nodes): `TestPySparkLocalLETOR`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 319`** (1 nodes): `provided`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 327`** (1 nodes): `BasicWalkThrough`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 328`** (1 nodes): `XGBoostTest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 329`** (2 nodes): `SyclPredictionCache`, `test_prediction_cache`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 330`** (1 nodes): `xgboost_testing_parse_tree`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 331`** (1 nodes): `TestSYCLTrainingContinuation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 332`** (2 nodes): `TestSYCLUpdaters`, `train_result()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 333`** (1 nodes): `TestMonotoneConstraints`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 334`** (2 nodes): `classification`, `separately`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 335`** (1 nodes): `DirectoryExcursion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 338`** (1 nodes): `TestDaskCallbacks`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 344`** (1 nodes): `pseudo_huber`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 347`** (1 nodes): `ConfigContextTest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 348`** (1 nodes): `QuantileCut`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 352`** (1 nodes): `xgb`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 355`** (2 nodes): `setenv()`, `TEST()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 359`** (2 nodes): `names`, `predictions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 360`** (2 nodes): `XGBBuildInfoDevice()`, `XGBuildInfo()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 361`** (2 nodes): `XGDMatrixSliceDMatrix()`, `XGDMatrixSliceDMatrixEx()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 362`** (1 nodes): `DMLC Tracker modules for running jobs on different platforms.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 363`** (1 nodes): `elementwise_metric`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 368`** (1 nodes): `multiclass_metric`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 369`** (1 nodes): `survival_metric`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 370`** (2 nodes): `run_sklearn_api()`, `test_sklearn_api()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 371`** (2 nodes): `run_validation_weights()`, `test_validation_weights()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 382`** (2 nodes): `_DMatrixFinalizer()`, `XGDMatrixFree_R()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 383`** (2 nodes): `SafeMkChar()`, `XGBoosterDumpModel_R()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 384`** (2 nodes): `captured_output()`, `Reassign stdout temporarily in order to test printed statements     Taken from:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 385`** (2 nodes): `eval_error_metric_skl()`, `Evaluation metric that looks like metrics provided by sklearn.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 386`** (2 nodes): `eval_error_metric()`, `Evaluation metric for xgb.train.      Parameters     ----------     rev_link : W`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 387`** (2 nodes): `logregobj()`, `Binary regression custom objective.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 388`** (2 nodes): `make_regression()`, `Make a simple regression dataset.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 389`** (2 nodes): `Custom softprob objective for testing.      Parameters     ----------     use_cu`, `softprob_obj()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 390`** (2 nodes): `Make a pytest mark for the `pytest-timeout` package.      Parameters     -------`, `timeout()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 394`** (1 nodes): `Return the evaluation results.          If **eval_set** is passed to the :py:met`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Booster` connect `Community 50` to `Community 0`, `Community 143`, `Community 144`, `Community 165`, `Community 250`, `Community 276`, `Community 101`, `Community 123`?**
  _High betweenness centrality (0.016) - this node is a cross-community bridge._
- **Why does `XGBoostJNI` connect `Community 22` to `Community 29`, `Community 366`?**
  _High betweenness centrality (0.015) - this node is a cross-community bridge._
- **Why does `DMatrix` connect `Community 53` to `Community 0`, `Community 144`, `Community 101`, `Community 143`, `Community 250`, `Community 165`, `Community 196`?**
  _High betweenness centrality (0.011) - this node is a cross-community bridge._
- **What connects `classification`, `index`, `from` to the rest of the system?**
  _1088 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.009646104694028016 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.018542713567839195 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.02064935064935065 - nodes in this community are weakly interconnected._