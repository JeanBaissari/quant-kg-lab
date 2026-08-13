# Graph Report - knowledge_graphs/imbalanced-learn/repo/imblearn  (2026-08-13)

## Corpus Check
- Corpus is ~49,017 words - fits in a single context window. You may not need a graph.

## Summary
- 611 nodes · 865 edges · 41 communities detected
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 160 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: rationale_for: 216 · method: 199 · uses: 160 · contains: 126 · calls: 123 · inherits: 38 · imports_from: 3


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 57 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `8504e95`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Pipeline` - 44 edges
2. `BaseSampler` - 32 edges
3. `InputTags` - 27 edges
4. `ValueDifferenceMetric` - 26 edges
5. `ArraysTransformer` - 21 edges
6. `SamplerTags` - 19 edges
7. `Tags` - 19 edges
8. `SamplerMixin` - 15 edges
9. `FunctionSampler` - 15 edges
10. `EditedNearestNeighbours` - 15 edges

## Surprising Connections (you probably didn't know these)
- `Class to perform over-sampling using SMOTE and cleaning using ENN.` --uses--> `BaseSampler`  [INFERRED]
  combine/_smote_enn.py → base.py
- `Private function to validate SMOTE and ENN objects` --uses--> `BaseSampler`  [INFERRED]
  combine/_smote_enn.py → base.py
- `Over-sampling using SMOTE and cleaning using ENN.      Combine over- and under-s` --uses--> `BaseSampler`  [INFERRED]
  combine/_smote_enn.py → base.py
- `Class to perform over-sampling using SMOTE and cleaning using Tomek links.` --uses--> `BaseSampler`  [INFERRED]
  combine/_smote_tomek.py → base.py
- `Private function to validate SMOTE and ENN objects` --uses--> `BaseSampler`  [INFERRED]
  combine/_smote_tomek.py → base.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.07
Nodes (39): BaseSampler, FunctionSampler, is_sampler(), Base class for sampling, Base method defined in each sampler to defined the sampling         strategy., Base class for sampling algorithms.      Warning: This class should not be used, Check inputs and statistics of the sampler.          You should use ``fit_resamp, Resample the dataset.          Parameters         ----------         X : {array- (+31 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (24): BaseOverSampler, Metrics to perform pairwise computation., Compute the necessary statistics from the training set.          Parameters, Compute the VDM distance pairwise.          Parameters         ----------, r"""Class implementing the Value Difference Metric.      This metric computes th, ValueDifferenceMetric, BaseSMOTE, Base class and original SMOTE methods for over-sampling (+16 more)

### Community 2 - "Community 2"
Cohesion: 0.08
Nodes (24): _check_name(), check_samplers_2d_target(), check_samplers_fit_resample(), check_samplers_list(), check_samplers_multiclass_ova(), check_samplers_pandas(), check_samplers_pandas_sparse(), check_samplers_preserve_dtype() (+16 more)

### Community 3 - "Community 3"
Cohesion: 0.07
Nodes (13): BaseUnderSampler, ClusterCentroids, Class to perform under-sampling by generating centroids based on clustering., Private function to create the KMeans estimator, Undersample by generating centroids based on clustering methods.      Method tha, The :mod:`imblearn.under_sampling.prototype_generation` submodule contains metho, InstanceHardnessThreshold, Class to perform under-sampling based on the instance hardness threshold. (+5 more)

### Community 4 - "Community 4"
Cohesion: 0.09
Nodes (32): check_neighbors_object(), check_sampling_strategy(), check_target_type(), _check_X(), _count_class_sample(), _deprecate_positional_args(), _is_neighbors_object(), Utilities for input validation (+24 more)

### Community 5 - "Community 5"
Cohesion: 0.09
Nodes (15): BaseSampler, The :mod:`imblearn.combine` provides methods which combine over-sampling and und, Class to perform over-sampling using SMOTE and cleaning using ENN., Private function to validate SMOTE and ENN objects, Over-sampling using SMOTE and cleaning using ENN.      Combine over- and under-s, SMOTEENN, Class to perform over-sampling using SMOTE and cleaning using Tomek links., Private function to validate SMOTE and ENN objects (+7 more)

### Community 6 - "Community 6"
Cohesion: 0.12
Nodes (14): _cached_transform(), _raise_or_warn_if_not_fitted(), Transform the data, and apply `transform` with the final estimator.          Cal, Apply `inverse_transform` for each step in a reverse order.          All estimat, Transform the data, and apply `score` with the final estimator.          Call `t, Get metadata routing of this object.          Please check :ref:`User Guide <met, Generate (idx, (name, trans)) tuples from self.steps.          When `filter_pass, A context manager to make sure a NotFittedError is raised, if a sub-estimator (+6 more)

### Community 7 - "Community 7"
Cohesion: 0.10
Nodes (10): BaseSMOTE, KMeansSMOTE, SMOTE variant employing some clustering before the generation., Compute the cluster sparsity., Apply a KMeans clustering before to over-sample using SMOTE.      This is an imp, BorderlineSMOTE, SMOTE variant applying some filtering before the generation process., Over-sampling using SVM-SMOTE.      Variant of SMOTE algorithm which use an SVM (+2 more)

### Community 8 - "Community 8"
Cohesion: 0.10
Nodes (8): ADASYN, Class to perform over-sampling using ADASYN., Create the necessary objects for ADASYN, Oversample using Adaptive Synthetic (ADASYN) algorithm.      This method is simi, The :mod:`imblearn.over_sampling` provides a set of method to perform over-sampl, RandomOverSampler, Class to perform random over-sampling., Class to perform random over-sampling.      Object to over-sample the minority c

### Community 9 - "Community 9"
Cohesion: 0.14
Nodes (8): Pipeline, Pipeline of transforms and resamples with a final estimator.      Sequentially a, Indicate whether pipeline has been fit.          This is done by checking whethe, Get params (metadata) for step `name`.          This transforms the metadata up, Fit the model.          Fit all the transforms/samplers one after the other and, Fit the model and transform with the final estimator.          Fits all the tran, Fit the model and sample with the final estimator.          Fits all the transfo, Apply `fit_predict` of last step in pipeline after transforms.          Applies

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (10): BalancedRandomForestClassifier, Forest classifiers trained on balanced boostrasp samples., Check the estimator and the n_estimator attribute, set the         `estimator_`, Make and configure a copy of the `base_estimator_` attribute.         Warning: T, Build a forest of trees from the training set (X, y).          Parameters, # FIXME: we could consider to support multiclass-multioutput if, Compute and set the OOB score and attributes.          Parameters         ------, Compute and set the OOB score.          Parameters         ----------         X (+2 more)

### Community 11 - "Community 11"
Cohesion: 0.14
Nodes (10): AdaBoostClassifier, The :mod:`imblearn.ensemble` module include methods generating under-sampled sub, # TODO: remove when minimum supported version of scikit-learn is 1.4, Build a boosted classifier from the training set (X, y).          Parameters, Check the estimator and the n_estimator attribute.          Sets the `estimator_, Make and configure a copy of the `base_estimator_` attribute.         Warning: T, Implement a single boost using the SAMME.R real algorithm., Random under-sampling integrated in the learning of AdaBoost.      During learni (+2 more)

### Community 12 - "Community 12"
Cohesion: 0.14
Nodes (8): BaggingClassifier, EasyEnsembleClassifier, Class to perform under-sampling using easy ensemble., # TODO: remove when minimum supported version of scikit-learn is 1.4, Check the estimator and the n_estimator attribute, set the         `estimator_`, Build a Bagging ensemble of estimators from the training set (X, y).          Pa, Attribute for older sklearn version compatibility., Bag of balanced boosted learners also known as EasyEnsemble.      This algorithm

### Community 13 - "Community 13"
Cohesion: 0.13
Nodes (8): BaseEstimator, all_estimators(), _CustomClusterer, _CustomNearestNeighbors, Basic implementation of nearest neighbors not relying on scikit-learn.      `kne, This method is not used within imblearn but it is required for         duck-typi, Class that mimics a cluster that does not expose `cluster_centers_`., Get a list of all estimators from imblearn.      This function crawls the module

### Community 14 - "Community 14"
Cohesion: 0.17
Nodes (15): classification_report_imbalanced(), geometric_mean_score(), macro_averaged_mean_absolute_error(), make_index_balanced_accuracy(), Metrics to assess performance on a classification task given class predictions., Compute Macro-Averaged MAE for imbalanced ordinal classification.      This func, Compute the sensitivity.      The sensitivity is the ratio ``tp / (tp + fn)`` wh, Compute the specificity.      The specificity is the ratio ``tn / (tn + fp)`` wh (+7 more)

### Community 15 - "Community 15"
Cohesion: 0.14
Nodes (6): BalancedBaggingClassifier, Bagging classifier trained on balanced bootstrap samples., Check the estimator and the n_estimator attribute, set the         `estimator_`, A Bagging classifier with additional balancing.      This implementation of Bagg, Build a Bagging ensemble of estimators from the training set (X, y).          Pa, Attribute for older sklearn version compatibility.

### Community 16 - "Community 16"
Cohesion: 0.15
Nodes (8): balanced_batch_generator(), BalancedBatchGenerator, import_keras(), Implement generators for ``keras`` which will balance the data., Try to import keras from keras and tensorflow.      This is possible to import t, Create a balanced batch generator to train keras model.      Returns a generator, Create balanced batches when training a keras model.      Create a keras ``Seque, The :mod:`imblearn.keras` provides utilities to deal with imbalanced dataset in

### Community 17 - "Community 17"
Cohesion: 0.20
Nodes (5): NearMiss, Class to perform under-sampling based on nearmiss methods., Select the appropriate samples depending of the strategy selected.          Para, Private function to create the NN estimator, Class to perform under-sampling based on NearMiss methods.      Read more in the

### Community 18 - "Community 18"
Cohesion: 0.18
Nodes (6): BaseCrossValidator, The :mod:`imblearn.model_selection` provides methods to split the dataset into t, InstanceHardnessCV, Returns the number of splitting iterations in the cross-validator.          Para, Instance-hardness cross-validation splitter.      Cross-validation splitter that, Generate indices to split data into training and test set.          Parameters

### Community 19 - "Community 19"
Cohesion: 0.18
Nodes (10): _fit_resample_one(), _fit_transform_one(), make_pipeline(), The :mod:`imblearn.pipeline` module implements utilities to build a composite es, # TODO: once scikit-learn >= 1.4, the following function should be simplified by, Call transform and apply weight to output.      Parameters     ----------     tr, Fits ``transformer`` to ``X`` and ``y``. The transformed result is returned, Construct a Pipeline from the given estimators.      This is a shorthand for the (+2 more)

### Community 20 - "Community 20"
Cohesion: 0.22
Nodes (4): CondensedNearestNeighbour, Class to perform under-sampling based on the condensed nearest neighbour method., Private function to create the NN estimator, Undersample based on the condensed nearest neighbour method.      Read more in t

### Community 21 - "Community 21"
Cohesion: 0.20
Nodes (4): AllKNN, Classes to perform under-sampling based on the edited nearest neighbour method., Undersample based on the AllKNN method.      This method will apply :class:`Edit, Create objects required by AllKNN

### Community 22 - "Community 22"
Cohesion: 0.22
Nodes (4): NeighbourhoodCleaningRule, Class performing under-sampling based on the neighbourhood cleaning rule., Create the objects required by NCR., Undersample based on the neighbourhood cleaning rule.      This class uses ENN a

### Community 23 - "Community 23"
Cohesion: 0.22
Nodes (4): OneSidedSelection, Class to perform under-sampling based on one-sided selection method., Private function to create the NN estimator, Class to perform under-sampling based on one-sided selection method.      Read m

### Community 24 - "Community 24"
Cohesion: 0.22
Nodes (4): Class to perform under-sampling by removing Tomek's links., Detect if samples are Tomek's link.          More precisely, it uses the target, Under-sampling by removing Tomek's links.      Read more in the :ref:`User Guide, TomekLinks

### Community 25 - "Community 25"
Cohesion: 0.22
Nodes (9): _construct_instances(), _get_check_estimator_ids(), _get_expected_failed_checks(), Construct Estimator instances if possible.      If parameter sets in INIT_PARAMS, Create pytest ids for checks.      When `obj` is an estimator, this returns the, Yield instances for a check.      For most estimators, this is a no-op.      For, Get the expected failed checks for all estimators in scikit-learn., _tested_estimators() (+1 more)

### Community 26 - "Community 26"
Cohesion: 0.22
Nodes (4): BaseCleaningSampler, Undersample based on the repeated edited nearest neighbour method.      This met, Private function to create the NN estimator, RepeatedEditedNearestNeighbours

### Community 27 - "Community 27"
Cohesion: 0.25
Nodes (3): EditedNearestNeighbours, Validate the estimator created in the ENN., Undersample based on the edited nearest neighbour method.      This method clean

### Community 28 - "Community 28"
Cohesion: 0.25
Nodes (4): Utilities for docstring in imbalanced-learn., Decorate a function's or a class' docstring to perform string     substitution o, Substitution, The :mod:`imblearn.utils` module includes various utilities.

### Community 29 - "Community 29"
Cohesion: 0.40
Nodes (5): _get_deps_info(), Utility method which prints system info to help with debugging, and filing issue, Overview of the installed version of main dependencies     Returns     -------, Print debugging information.      .. versionadded:: 0.5      Parameters     ----, show_versions()

### Community 30 - "Community 30"
Cohesion: 0.50
Nodes (3): make_imbalance(), Transform a dataset into an imbalanced dataset., Turn a dataset into an imbalanced dataset with a specific sampling strategy.

### Community 31 - "Community 31"
Cohesion: 0.50
Nodes (3): fetch_datasets(), Collection of imbalanced datasets.  This collection of datasets has been propose, Load the benchmark datasets from Zenodo, downloading it if necessary.      .. ve

### Community 32 - "Community 32"
Cohesion: 0.50
Nodes (3): raise_isinstance_error(), The :mod:`imblearn.exceptions` module includes all custom warnings and error cla, Raise consistent error message for isinstance() function.      Parameters     --

### Community 33 - "Community 33"
Cohesion: 0.50
Nodes (3): balanced_batch_generator(), Implement generators for ``tensorflow`` which will balance the data., Create a balanced batch generator to train tensorflow model.      Returns a gene

### Community 34 - "Community 34"
Cohesion: 0.50
Nodes (3): deprecate_parameter(), Utilities for deprecation, Helper to deprecate a parameter by another one.      Parameters     ----------

### Community 35 - "Community 35"
Cohesion: 0.67
Nodes (2): _estimator_has(), Check if we can delegate a method to the underlying estimator.     First, we che

### Community 36 - "Community 36"
Cohesion: 1.00
Nodes (1): The :mod:`imblearn.datasets` provides methods to generate imbalanced data.

### Community 37 - "Community 37"
Cohesion: 1.00
Nodes (1): The :mod:`imblearn.metrics` module includes score functions, performance metrics

### Community 38 - "Community 38"
Cohesion: 1.00
Nodes (1): The :mod:`imblearn.under_sampling.prototype_selection` submodule contains method

### Community 39 - "Community 39"
Cohesion: 1.00
Nodes (1): The :mod:`imblearn.tensorflow` provides utilities to deal with imbalanced datase

### Community 40 - "Community 40"
Cohesion: 1.00
Nodes (1): The :mod:`imblearn.under_sampling` provides methods to under-sample a dataset.

## Knowledge Gaps
- **139 isolated node(s):** ```imbalanced-learn`` is a set of python methods to deal with imbalanced datset i`, `The :mod:`imblearn.datasets` provides methods to generate imbalanced data.`, `Transform a dataset into an imbalanced dataset.`, `Turn a dataset into an imbalanced dataset with a specific sampling strategy.`, `Collection of imbalanced datasets.  This collection of datasets has been propose` (+134 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 35`** (2 nodes): `_estimator_has()`, `Check if we can delegate a method to the underlying estimator.     First, we che`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (1 nodes): `The :mod:`imblearn.datasets` provides methods to generate imbalanced data.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (1 nodes): `The :mod:`imblearn.metrics` module includes score functions, performance metrics`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (1 nodes): `The :mod:`imblearn.under_sampling.prototype_selection` submodule contains method`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `The :mod:`imblearn.tensorflow` provides utilities to deal with imbalanced datase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `The :mod:`imblearn.under_sampling` provides methods to under-sample a dataset.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BaseSampler` connect `Community 0` to `Community 13`, `Community 5`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Why does `ValueDifferenceMetric` connect `Community 1` to `Community 13`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Why does `ArraysTransformer` connect `Community 0` to `Community 4`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `Pipeline` (e.g. with `BalancedBaggingClassifier` and `Bagging classifier trained on balanced bootstrap samples.`) actually correct?**
  _`Pipeline` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 20 inferred relationships involving `BaseSampler` (e.g. with `InputTags` and `SamplerTags`) actually correct?**
  _`BaseSampler` has 20 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `InputTags` (e.g. with `BaseSampler` and `FunctionSampler`) actually correct?**
  _`InputTags` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 18 inferred relationships involving `ValueDifferenceMetric` (e.g. with `BaseSMOTE` and `Base class and original SMOTE methods for over-sampling`) actually correct?**
  _`ValueDifferenceMetric` has 18 INFERRED edges - model-reasoned connections that need verification._