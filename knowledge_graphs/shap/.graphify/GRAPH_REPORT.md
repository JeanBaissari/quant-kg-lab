# Graph Report - knowledge_graphs/shap/repo/shap  (2026-08-13)

## Corpus Check
- 95 files · ~117,361 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1277 nodes · 1752 edges · 108 communities detected
- Non-singleton communities: 100
- Extraction: EXTRACTED: 88.1% · INFERRED: 11.9%
- Edge kinds: calls: 311 · contains: 317 · imports_from: 116 · inherits: 63 · method: 335 · rationale_for: 401 · uses: 209

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 95 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `df974a1`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `Explainer` (95)
- `Masker` (73)
- `Explanation` (48)
- `Model` (38)
- `Explainer` (35)
- `__init__.py` (31)
- `_exceptions.py` (29)
- `_explanation.py` (26)
- `_tree.py` (26)
- `_legacy.py` (25)

## Surprising Connections (you probably didn't know these)
- `UnsupportedModule` --uses--> `Cohorts`  [INFERRED]
  __init__.py → _explanation.py
- `UnsupportedModule` --uses--> `Explanation`  [INFERRED]
  __init__.py → _explanation.py
- `ExplanationError` --uses--> `DimensionError`  [INFERRED]
  benchmark/_explanation_error.py → utils/_exceptions.py
- `A measure of the explanation error relative to a model's actual output.      Thi` --uses--> `DimensionError`  [INFERRED]
  benchmark/_explanation_error.py → utils/_exceptions.py
- `Build a new explanation error benchmarker with the given masker, model, and mode` --uses--> `DimensionError`  [INFERRED]
  benchmark/_explanation_error.py → utils/_exceptions.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (34): AdditiveExplanation, AdditiveForceArrayVisualizer, AdditiveForceVisualizer, BaseVisualizer, ensure_not_numpy(), Explanation, force(), getjs() (+26 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (31): dependence_legacy(), _plot_histogram(), # TODO: This stacking could be avoided if we use the new shap.utils.potential_in, # TODO: Make the color bar a one-sided beeswarm plot so we can see the density a, Create a SHAP dependence scatter plot, optionally colored by an interaction feat, If either limit is None, suggest suitable value including a buffer either side, Suggest a suitable x_jitter value based on the unique values in the feature, Add a histogram of the data on a matching secondary axes (+23 more)

### Community 2 - "Community 2"
Cohesion: 0.07
Nodes (21): ComputeTime, Extracts a runtime benchmark result from the passed Explanation., ExplanationError, A measure of the explanation error relative to a model's actual output.      Thi, Build a new explanation error benchmarker with the given masker, model, and mode, Run this benchmark on the given explanation., BenchmarkResult, The result of a benchmark run. (+13 more)

### Community 3 - "Community 3"
Cohesion: 0.07
Nodes (19): merge_closest_groups(), merge_score(), partition_tree(), post_process_sentencepiece_tokenizer_output(), Replaces whitespace encoded as '_' with ' ' for sentencepiece tokenizers., A token representation used for token clustering., A token group (substring) representation used for token clustering., Compute the score of merging two token groups.      special_tokens: tokens (such (+11 more)

### Community 4 - "Community 4"
Cohesion: 0.10
Nodes (17): Convert number of trees to number of iterations for XGBoost models., Uses Tree SHAP algorithms to explain the output of ensemble tree models.      Tr, A consistent interface to make predictions from this model., A consistent interface to make predictions from this model.          Parameters, Build a new Tree explainer for the passed model.          Parameters         ---, This computes the expected value conditioned on the given label value., Calculate the SHAP values for the model applied to the data.          Parameters, Estimate the SHAP values for a set of samples.          Parameters         ----- (+9 more)

### Community 5 - "Community 5"
Cohesion: 0.12
Nodes (29): batch_keep_retrain(), batch_remove_retrain(), const_rand(), const_shuffle(), keep_impute(), keep_mask(), keep_resample(), keep_retrain() (+21 more)

### Community 6 - "Community 6"
Cohesion: 0.09
Nodes (28): a1a(), adult(), cache(), california(), communitiesandcrime(), corrgroups60(), diabetes(), imagenet50() (+20 more)

### Community 7 - "Community 7"
Cohesion: 0.11
Nodes (19): _assert_output_input_match(), _build_fixed_multi_output(), _build_fixed_output(), _build_fixed_single_output(), _convert_delta_mask_to_full(), _init_masks(), link_reweighting(), make_masks() (+11 more)

### Community 8 - "Community 8"
Cohesion: 0.07
Nodes (27): keep_absolute_impute__r2(), keep_absolute_impute__roc_auc(), keep_absolute_mask__r2(), keep_absolute_mask__roc_auc(), keep_absolute_resample__r2(), keep_absolute_resample__roc_auc(), keep_negative_impute(), keep_negative_mask() (+19 more)

### Community 9 - "Community 9"
Cohesion: 0.11
Nodes (14): convert_to_data(), convert_to_instance(), convert_to_instance_with_index(), convert_to_model(), Data, DenseData, DenseDataWithIndex, Instance (+6 more)

### Community 10 - "Community 10"
Cohesion: 0.09
Nodes (14): break_dependence(), custom_record_gradient(), gather(), linearity_1d_handler(), linearity_with_excluded_handler(), nonlinearity_1d_handler(), Return which inputs of this operation are variable (i.e. depend on the model inp, # TODO: set a deprecation warning for this (+6 more)

### Community 11 - "Community 11"
Cohesion: 0.13
Nodes (16): _all_subsets(), _build_tree(), CoalitionExplainer, _combine_masks(), _compute_weight(), _create_combined_masks(), _create_masks(), create_partition_hierarchy() (+8 more)

### Community 12 - "Community 12"
Cohesion: 0.13
Nodes (21): consistency_guarantees(), _fit_human(), _human_sum(), human_sum_00(), human_sum_01(), human_sum_11(), _human_xor(), human_xor_00() (+13 more)

### Community 13 - "Community 13"
Cohesion: 0.13
Nodes (11): This masks out tokens according to the given tokenizer.      The masked variable, Called by explainers to allow us to convert data to better match masking (here t, Returns the substrings associated with each token in the given string., Compute the clustering of tokens for the given string., The shape of what we return as a masker.          Note we only return a single s, The shape of the masks we expect., The names of the features for each mask position for the given input string., The names of the features for each mask position for the given input string. (+3 more)

### Community 14 - "Community 14"
Cohesion: 0.13
Nodes (11): Computes log odds scores of generating output(text) for a given batch of input(t, The function updates output tokens.          It mimics the caching mechanism to, Gets the output tokens by computing the output sentence ids and output names usi, Generates scores (log odds) for output text explanation algorithms using Teacher, The function tokenizes output sentences and returns ids.          Parameters, The function tokenizes source sentences.          In model agnostic case, the fu, Calculates log odds from logits.          This function passes the logits throug, This function performs model inference for tensorflow and pytorch models. (+3 more)

### Community 15 - "Community 15"
Cohesion: 0.12
Nodes (16): ExactExplainer, gray_code_indexes(), gray_code_masks(), partition_delta_indexes(), partition_masks(), _partition_masks_recurse(), Explains the output of model(*args), where args represents one or more parallel, Explains a single row and returns the tuple (row_values, row_expected_values, ro (+8 more)

### Community 16 - "Community 16"
Cohesion: 0.14
Nodes (16): Explainer, Uses Shapley values to explain any machine learning model or python function., Build a new explainer for the passed model.          Parameters         --------, Determines if this explainer can handle the given model.          This is an abs, Write the explainer to the given file stream., Load an Explainer from the given file stream.          Parameters         ------, # TODO: deal with estimators for each class, # FIXME: The `link` and `linearize_link` arguments are ignored. GH #3513 (+8 more)

### Community 17 - "Community 17"
Cohesion: 0.13
Nodes (10): # TODO: this could be avoided by integrating between endpoints if no local smoot, # TODO: better cloning :), # TODO: support and deal with clusterings, UnsupportedModule, bar(), # TODO: check other attributes for equality? like feature names perhaps? probabl, # TODO: Rather than just show the "1st token", "2nd token", etc. it would be bet, # TODO: improve the bar chart to look better like the waterfall plot with number (+2 more)

### Community 18 - "Community 18"
Cohesion: 0.16
Nodes (6): KernelExplainer, Estimate the SHAP values for a set of samples.          Parameters         -----, Uses the Kernel SHAP method to explain the output of any function.      Kernel S, Computes SHAP values using an extension of the Shapley sampling values explanati, SamplingExplainer, KernelExplainer

### Community 19 - "Community 19"
Cohesion: 0.11
Nodes (11): CatBoostTreeModelLoader, _check_xgboost_version(), get_xgboost_dmatrix_properties(), IsoTree, A single decision tree.      The primary point of this object is to parse many d, In sklearn the tree of the Isolation Forest does not calculated in a good way., Retrieves properties from an xgboost.sklearn.XGBModel instance that should be, This loads an XGBoost model directly from a raw memory dump. (+3 more)

### Community 20 - "Community 20"
Cohesion: 0.13
Nodes (13): FixedComposite, Creates a Composite masker from an underlying masker and returns the original ar, Computes mask on the args using the masker data attribute and returns tuple cont, Write a FixedComposite masker to a file stream., Load a FixedComposite masker from a file stream., A masker that outputs both the masked data and the original data as a pair., Masker, This is the superclass of all maskers. (+5 more)

### Community 21 - "Community 21"
Cohesion: 0.14
Nodes (10): Generates scores (log odds) for the top-k tokens for Causal/Masked LM., Gets the token names for top-k token ids for Causal/Masked LM.          Paramete, Calculates log odds from logits.          This function passes the logits throug, Take Causal/Masked LM model and tokenizer and build a log odds output model for, The function tokenizes source sentence.          Parameters         ----------, Generates top-k token ids for Causal/Masked LM.          Parameters         ----, Evaluates a Causal/Masked LM model and returns logits corresponding to next word, Computes log odds scores for a given batch of masked inputs for the top-k tokens (+2 more)

### Community 22 - "Community 22"
Cohesion: 0.11
Nodes (6): corrgroups60__gbm(), cric__gbm(), independentlinear60__gbm(), Gradient Boosted Trees, Gradient Boosted Trees, Gradient Boosted Trees

### Community 23 - "Community 23"
Cohesion: 0.13
Nodes (17): _apply_options(), get_style(), load_default_style(), Configuration of customisable style options for SHAP plots.  NOTE: This is exper, Context manager to temporarily change style options.      NOTE: This is experime, Return a new StyleConfig with any changes applied, handling any invalid options., # TODO: Use dataclass(kw_only=True) when we drop Python 3.9, A complete set of configuration options for matplotlib-based shap plots. (+9 more)

### Community 24 - "Community 24"
Cohesion: 0.12
Nodes (10): Masker, OutputComposite, Mask the args using the masker and return a tuple containing the masked input an, Write a OutputComposite masker to a file stream., A masker that is a combination of a masker and a model and outputs both masked a, Load a OutputComposite masker from a file stream., Creates a masker from an underlying masker and and model.          This masker r, Impute (+2 more)

### Community 25 - "Community 25"
Cohesion: 0.12
Nodes (12): kernel_shap_1000_meanref(), lime_tabular_classification_1000(), lime_tabular_regression_1000(), linear_shap_corr(), maple(), LIME Tabular 1000     color = red_blue_circle(0.75), LIME Tabular 1000     color = red_blue_circle(0.75), MAPLE     color = red_blue_circle(0.6) (+4 more)

### Community 26 - "Community 26"
Cohesion: 0.13
Nodes (9): lower_credit(), PartitionExplainer, # TODO: maybe? if we have a tabular masker then we build a PermutationExplainer, Uses the Partition SHAP method to explain the output of any function.      Parti, Explain the output of the model on the given arguments., Explains a single row and returns the tuple (row_values, row_expected_values, ro, Compute a nested set of recursive Owen values based on an ordering recursion., Compute a nested set of recursive Owen values based on an ordering recursion. (+1 more)

### Community 27 - "Community 27"
Cohesion: 0.15
Nodes (8): Model, Generates target sentence/ids using a base model.      It generates target sente, This function performs text generation for tensorflow and pytorch models., Create a text generator model from a pretrained transformer model or a function., Calculates if special tokens are present in the beginning/end of the model gener, Generates target sentence/ids from X.          Parameters         ----------, The function tokenizes source sentences.          In model agnostic case, the fu, TextGeneration

### Community 28 - "Community 28"
Cohesion: 0.14
Nodes (15): convert_color(), dendrogram_coords(), _dendrogram_coords_rec(), fill_counts(), fill_internal_max_values(), get_sort_order(), merge_nodes(), parse_axis_limit() (+7 more)

### Community 29 - "Community 29"
Cohesion: 0.15
Nodes (16): add_sample_images(), check_valid_image(), display_grid_plot(), is_empty(), load_image(), make_dir(), Function to check if folder at given path exists and is not empty.      Returns, Function to display grid of images and their titles/captions. (+8 more)

### Community 30 - "Community 30"
Cohesion: 0.14
Nodes (8): _auto_cohorts(), Cohorts, Pass-through from the underlying slicer object., Split this explanation into several cohorts.          Parameters         -------, A collection of :class:`.Explanation` objects, typically each explaining a clust, Internal collection of cohorts, stored as a dictionary., Call the bound methods on the Explanation objects retrieved during attribute acc, This uses a DecisionTreeRegressor to build a group of cohorts with similar SHAP

### Community 31 - "Community 31"
Cohesion: 0.19
Nodes (3): Explanation, Pass-through from the underlying slicer object., A sliceable set of parallel arrays representing a SHAP explanation.      Notes

### Community 32 - "Community 32"
Cohesion: 0.13
Nodes (5): MetaExplanation, This metaclass exposes the Explanation object's class methods for creating templ, Element-wise absolute value op., Hierarchical clustering op., type

### Community 33 - "Community 33"
Cohesion: 0.15
Nodes (9): Image, _jit_build_partition_tree(), Fill in the masked parts of the image through inpainting., This partitions an image into a hierarchical clustering based on axis-aligned sp, Write a Image masker to a file stream., Load a Image masker from a file stream., Masks out image regions with blurring or inpainting., This partitions an image into a hierarchical clustering based on axis-aligned sp (+1 more)

### Community 34 - "Community 34"
Cohesion: 0.23
Nodes (15): _css_rgba(), heatmap(), _ipython_display_html(), process_shap_values(), Format an rgba() color for HTML/CSS.      NumPy 2 scalar types stringify as ``np, Check IPython is installed, then display HTML, # TODO: we should support text output explanations (from models that output text, Plots an explanation of a string of text using coloring and interactive labels. (+7 more)

### Community 35 - "Community 35"
Cohesion: 0.19
Nodes (14): _convert(), lab2rgb(), _lab2xyz(), lch2lab(), _prepare_colorarray(), _prepare_lab_array(), Convert CIE-LAB to XYZ color space.      Internal function for :func:`~.lab2xyz`, Convert image in CIE-LAB to sRGB color space.      Parameters     ---------- (+6 more)

### Community 36 - "Community 36"
Cohesion: 0.17
Nodes (8): duplicate_components(), LinearExplainer, Computes SHAP values for a linear model, optionally accounting for inter-feature, Uses block matrix inversion identities to quickly estimate transforms., Attempt to pull out the coefficients and intercept from the given model object., Determines if we can parse the given model., Explains a single row and returns the tuple (row_values, row_expected_values, ro, Estimate the SHAP values for a set of samples.          Parameters         -----

### Community 37 - "Community 37"
Cohesion: 0.20
Nodes (9): compute_expectations(), extend_path(), This module is a pure python implementation of Tree SHAP. It is primarily for il, A pure Python (slow) implementation of Tree SHAP., Tree, tree_shap_recursive(), TreeExplainer, unwind_path() (+1 more)

### Community 38 - "Community 38"
Cohesion: 0.14
Nodes (9): Independent, This returns a mask of which features change when we mask them.          This op, Write a Tabular masker to a file stream., A common base class for Independent and Partition., Load a Tabular masker from a file stream., This masks out tabular features by integrating over the given background dataset, Build a Independent masker with the given background data.          Parameters, This masks out tabular features by integrating over the given background dataset (+1 more)

### Community 39 - "Community 39"
Cohesion: 0.14
Nodes (12): mean_abs_tree_shap(), random(), Tree MAPLE     color = red_blue_circle(0.6)     linestyle = dashed, Random     color = #777777     linestyle = solid, TreeExplainer     color = red_blue_circle(0)     linestyle = solid, mean(|TreeExplainer|)     color = red_blue_circle(0.25)     linestyle = solid, tree_maple(), tree_shap_tree_path_dependent() (+4 more)

### Community 40 - "Community 40"
Cohesion: 0.15
Nodes (5): is_1d(), Apply a numpy-style function to this Explanation., Numpy-style mean function., Numpy-style max function., Numpy-style min function.

### Community 41 - "Community 41"
Cohesion: 0.20
Nodes (11): __change_shap_base_value(), decision(), __decision_plot_matplotlib(), DecisionPlotResult, multioutput_decision(), Visualize cumulative SHAP values., The optional return value of decision_plot.      The class attributes can be use, Shift SHAP base value to a new value. This function assumes that `base_value` an (+3 more)

### Community 42 - "Community 42"
Cohesion: 0.15
Nodes (10): add_interim_values(), deeplift_grad(), get_target_input(), linear_1d(), passthrough(), The backward hook which computes the deeplift     gradient for an nn.Module, The forward hook used to save interim tensors, detached     from the graph. Used, A forward hook which saves the tensor - attached to its graph.     Used if we wa (+2 more)

### Community 43 - "Community 43"
Cohesion: 0.23
Nodes (6): Get the SHAP value computation graph for a given model output., Runs the model while also setting the learning phase flags to False., Passes a gradient op creation request to the correct handler., Using tf.gradients to implement the backpropagation was     inspired by the grad, An explainer object for a deep model using a given background dataset., TFDeep

### Community 44 - "Community 44"
Cohesion: 0.24
Nodes (12): Exception, ConvergenceError, ExplainerError, InvalidAction, InvalidAlgorithmError, InvalidClusteringError, InvalidFeaturePerturbationError, InvalidMaskerError (+4 more)

### Community 45 - "Community 45"
Cohesion: 0.17
Nodes (7): Composite, joint_clustering(), This merges several maskers for different inputs together into a single composit, Return a joint clustering that merges the clusterings of all the submaskers., Compute the shape of this masker as the sum of all the sub masker shapes., The shape of the masks we expect., Transform the argument

### Community 46 - "Community 46"
Cohesion: 0.17
Nodes (11): beeswarm(), Summary plots of SHAP values across a whole dataset., # FIXME: introduce beeswarm interaction values as a separate function `beeswarm_, # TODO: simplify this when we drop support for matplotlib 3.9, # TODO: Add support for hclustering based explanations where we sort the leaf or, # TODO: remove unused title argument / use title argument, # TODO: Add support for hclustering based explanations where we sort the leaf or, Create a SHAP beeswarm plot, colored by feature values when they are provided. (+3 more)

### Community 47 - "Community 47"
Cohesion: 0.20
Nodes (6): Explainer, Compute the MAPLE coef attributions.          Parameters         ----------, Simply tree MAPLE into the common SHAP interface.      Parameters     ----------, TreeMaple, Simply returns the global gain/gini feature importances for tree models.      Th, TreeGain

### Community 48 - "Community 48"
Cohesion: 0.31
Nodes (10): experiments(), __gen_cache_id(), __print_status(), Use ssh to run the experiments on remote machines in parallel.      Parameters, run_experiment(), run_experiments(), run_experiments_helper(), __run_remote_experiment() (+2 more)

### Community 49 - "Community 49"
Cohesion: 0.18
Nodes (6): AdditiveExplainer, Computes SHAP values for generalized additive models.      This assumes that the, Determines if this explainer can handle the given model.          This is an abs, Explains a single row and returns the tuple (row_values, row_expected_values, ro, Build an Additive explainer for the given model using the given masker object., Explains the output of model(*args), where args represents one or more parallel

### Community 50 - "Community 50"
Cohesion: 0.18
Nodes (6): PermutationExplainer, Explain the output of the model on the given arguments., Explains a single row and returns the tuple (row_values, row_expected_values, ro, This method approximates the Shapley values by iterating through permutations of, Legacy interface to estimate the SHAP values for a set of samples.          Para, Build an explainers.Permutation object for the given model using the given maske

### Community 51 - "Community 51"
Cohesion: 0.25
Nodes (10): _get_graph(), _get_model_inputs(), _get_model_output(), _get_session(), _import_tf(), Common utility to get the session for the tensorflow-based explainer.      Param, Common utility to get the graph for the tensorflow-based explainer.      Paramet, Common utility to determine the model inputs.      Parameters     ---------- (+2 more)

### Community 52 - "Community 52"
Cohesion: 0.20
Nodes (4): convert_to_link(), IdentityLink, Link, LogitLink

### Community 53 - "Community 53"
Cohesion: 0.20
Nodes (10): batch_keep_absolute_retrain__r2(), batch_keep_absolute_retrain__roc_auc(), batch_remove_absolute_retrain__r2(), batch_remove_absolute_retrain__roc_auc(), __intlogspace(), Batch Remove Absolute (retrain)     xlabel = "Fraction of features removed", Batch Keep Absolute (retrain)     xlabel = "Fraction of features kept"     ylabe, Batch Remove Absolute (retrain)     xlabel = "Fraction of features removed" (+2 more)

### Community 54 - "Community 54"
Cohesion: 0.42
Nodes (9): get_method_color(), get_method_linestyle(), get_metric_attr(), _human_score_map(), make_grid(), plot_curve(), plot_grids(), plot_human() (+1 more)

### Community 55 - "Community 55"
Cohesion: 0.38
Nodes (3): Maple, Compute the MAPLE coef attributions.          Parameters         ----------, Simply wraps MAPLE into the common SHAP interface.      Parameters     ---------

### Community 56 - "Community 56"
Cohesion: 0.22
Nodes (8): Summary plots of SHAP values (violin plot) across a whole dataset., # TODO: simplify this when we drop support for matplotlib 3.9, # TODO: remove unused title argument / use title argument, # TODO: Add support for hclustering based explanations where we sort the leaf or, Trim the color range, but prevent the color range from collapsing., Create a SHAP violin plot, colored by feature values when they are provided., _trim_crange(), violin()

### Community 57 - "Community 57"
Cohesion: 0.36
Nodes (3): PyTorchDeep, Add handles to all non-container layers in the model.         Recursively for no, Removes the x and y attributes which were added by the forward handles         R

### Community 58 - "Community 58"
Cohesion: 0.25
Nodes (5): DeepExplainer, Return an explanation object for the model applied to X.          Parameters, Return approximate SHAP values for the model applied to the data given by X., An explainer object for a differentiable model using a given background dataset., Meant to approximate SHAP values for deep learning models.      This is an enhan

### Community 59 - "Community 59"
Cohesion: 0.22
Nodes (6): GPUTreeExplainer, GPU accelerated tree explanations, Estimate the SHAP interaction values for a set of samples.          Parameters, Experimental GPU accelerated version of TreeExplainer. Currently requires source, Estimate the SHAP values for a set of samples.          Parameters         -----, TreeExplainer

### Community 60 - "Community 60"
Cohesion: 0.25
Nodes (7): compute_output_dims(), _compute_shape(), list_wrap(), A helper to patch things since slicer doesn't handle arrays of arrays (it does h, Compute the shape over potentially complex data nesting., Uses the passed data to infer which dimensions correspond to the model's output., Computes the shape of a generic object ``x``.

### Community 61 - "Community 61"
Cohesion: 0.22
Nodes (4): Model, This is the superclass of all models., Wrap a callable model as a SHAP Model object., Save the model to the given file stream.

### Community 62 - "Community 62"
Cohesion: 0.25
Nodes (8): local_accuracy(), Runtime (sec / 1k samples)     transform = "negate_log"     sort_order = 2, Test an explanation method., Converts DataFrames to numpy arrays., Local Accuracy     transform = "identity"     sort_order = 0, runtime(), __score_method(), __toarray()

### Community 63 - "Community 63"
Cohesion: 0.25
Nodes (5): Build a new Text masker given an optional passed tokenizer.          Parameters, A basic model agnostic tokenizer., Create a tokenizer based on a simple splitting pattern., Tokenize the passed string, optionally returning the offsets of each token in th, SimpleTokenizer

### Community 64 - "Community 64"
Cohesion: 0.46
Nodes (6): _decode_array_optimized(), __decode_element(), _decode_object(), _decode_simple_key_value_pair(), decode_ubjson_buffer(), This is an incomplete implementation of the UBJSON specification. Expected is a

### Community 65 - "Community 65"
Cohesion: 0.32
Nodes (3): Deserializer, Load data items from an input stream., Load a data item from the current input stream.

### Community 66 - "Community 66"
Cohesion: 0.29
Nodes (5): This is the superclass of all serializable objects., Save the model to the given file stream., This is meant to be overridden by subclasses and called with super.          We, This is meant to be overridden by subclasses and called with super.          We, Serializable

### Community 67 - "Community 67"
Cohesion: 0.29
Nodes (2): Action, Abstract action class.

### Community 68 - "Community 68"
Cohesion: 0.29
Nodes (7): _human_and(), human_and_00(), human_and_01(), human_and_11(), AND (false/false)      This tests how well a feature attribution method agrees w, AND (false/true)      This tests how well a feature attribution method agrees wi, AND (true/true)      This tests how well a feature attribution method agrees wit

### Community 69 - "Community 69"
Cohesion: 0.29
Nodes (7): _human_or(), human_or_00(), human_or_01(), human_or_11(), OR (false/false)      This tests how well a feature attribution method agrees wi, OR (false/true)      This tests how well a feature attribution method agrees wit, OR (true/true)      This tests how well a feature attribution method agrees with

### Community 70 - "Community 70"
Cohesion: 0.33
Nodes (2): An explainer object for a differentiable model using a given background dataset., _TFGradient

### Community 71 - "Community 71"
Cohesion: 0.29
Nodes (4): identity(), logit(), A no-op link function., A logit link function useful for going from probability units to log-odds units.

### Community 72 - "Community 72"
Cohesion: 0.29
Nodes (3): Fixed, This leaves the input unchanged during masking, and is used for things like scor, The shape of the masks we expect.

### Community 73 - "Community 73"
Cohesion: 0.29
Nodes (3): Save data items to an input stream., Dump a data item to the current input stream., Serializer

### Community 74 - "Community 74"
Cohesion: 0.33
Nodes (3): This is a simple wrapper around tqdm that includes a starting delay before print, show_progress(), ShowProgress

### Community 75 - "Community 75"
Cohesion: 0.53
Nodes (5): compare_plot(), get_benchmark(), get_metrics(), trend_plot(), update()

### Community 76 - "Community 76"
Cohesion: 0.33
Nodes (4): pack_values(), Explains the output of model(*args), where args is a list of parallel iterable d, Explains a single row and returns the tuple (row_values, row_expected_values, ro, Used the clean up arrays before putting them into an Explanation object.

### Community 77 - "Community 77"
Cohesion: 0.33
Nodes (4): GradientExplainer, Return an explanation object for the model applied to X.          Parameters, Return the values for the model applied to X.          Parameters         ------, Explains a model using expected gradients (an extension of integrated gradients)

### Community 78 - "Community 78"
Cohesion: 0.47
Nodes (1): _PyTorchGradient

### Community 79 - "Community 79"
Cohesion: 0.33
Nodes (4): OpHistoryItem, An operation that has been applied to an Explanation object., This adds support for OpChain indexing., Randomly samples the instances (rows) of the Explanation object.          Parame

### Community 80 - "Community 80"
Cohesion: 0.33
Nodes (3): Build a new model by wrapping the given pipeline object., This wraps a transformers pipeline object for easy explanations.      By default, TransformersPipeline

### Community 81 - "Community 81"
Cohesion: 0.33
Nodes (3): Random, Simply returns random (normally distributed) feature attributions.      This is, Explain a single row and return feature attributions.

### Community 82 - "Community 82"
Cohesion: 0.33
Nodes (5): # TODO: If we make a JS version of this plot then we could let users click on a, Plots an explanation of a single prediction as a waterfall plot.      The SHAP v, Plots an explanation of a single prediction as a waterfall plot.      The SHAP v, waterfall(), waterfall_legacy()

### Community 83 - "Community 83"
Cohesion: 0.40
Nodes (4): backward_walk_ops(), forward_walk_ops(), Follows a set of ops assuming their value is False and find blocked Switch paths, tensors_blocked_by_false()

### Community 84 - "Community 84"
Cohesion: 0.40
Nodes (2): Coefficient, Simply returns the model coefficients as the feature attributions.      This is

### Community 85 - "Community 85"
Cohesion: 0.40
Nodes (2): LimeTabular, Simply wrap of lime.lime_tabular.LimeTabularExplainer into the common shap inter

### Community 86 - "Community 86"
Cohesion: 0.40
Nodes (4): image(), image_to_text(), Plots SHAP values for image inputs with test outputs.      Parameters     ------, Plots SHAP values for image inputs.      Parameters     ----------     shap_valu

### Community 87 - "Community 87"
Cohesion: 0.50
Nodes (4): compute_bounds(), partial_dependence(), Handles any setting of xmax and xmin.      Note that we handle None, float, or ", A basic partial dependence plot function.

### Community 88 - "Community 88"
Cohesion: 0.50
Nodes (1): ActionOptimizer

### Community 89 - "Community 89"
Cohesion: 0.67
Nodes (3): monitoring(), Create a SHAP monitoring plot.      (Note this function is preliminary and subje, truncate_text()

### Community 90 - "Community 90"
Cohesion: 0.50
Nodes (3): ExperimentalWarning, Used to manage warning messages for any experimental integrations., Warning

### Community 91 - "Community 91"
Cohesion: 0.67
Nodes (1): This defines some common colors.

### Community 92 - "Community 92"
Cohesion: 0.67
Nodes (2): group_features(), Numpy-style sum function.

### Community 93 - "Community 93"
Cohesion: 0.67
Nodes (2): benchmark(), Plot a BenchmarkResult or list of such results.

### Community 94 - "Community 94"
Cohesion: 0.67
Nodes (2): embedding(), Use the SHAP values as an embedding which we project to 2D for visualization.

### Community 95 - "Community 95"
Cohesion: 0.67
Nodes (2): group_difference(), This plots the difference in mean SHAP values between two groups.      It is use

### Community 96 - "Community 96"
Cohesion: 0.67
Nodes (2): heatmap(), Create a heatmap plot of a set of SHAP values.      This plot is designed to sho

### Community 97 - "Community 97"
Cohesion: 1.00
Nodes (2): TreeExplainer (independent)     color = red_blue_circle(0)     linestyle = dashe, tree_shap_independent_200()

### Community 98 - "Community 98"
Cohesion: 1.00
Nodes (2): Saabas     color = red_blue_circle(0)     linestyle = dotted, saabas()

### Community 99 - "Community 99"
Cohesion: 1.00
Nodes (2): Gain/Gini Importance     color = red_blue_circle(0.25)     linestyle = dotted, tree_gain()

### Community 100 - "Community 100"
Cohesion: 1.00
Nodes (2): keep_positive_resample(), Keep Positive (resample)     xlabel = "Max fraction of features kept"     ylabel

### Community 101 - "Community 101"
Cohesion: 1.00
Nodes (2): keep_positive_retrain(), Keep Positive (retrain)     xlabel = "Max fraction of features kept"     ylabel

### Community 102 - "Community 102"
Cohesion: 1.00
Nodes (2): Remove Positive (mask)     xlabel = "Max fraction of features removed"     ylabe, remove_positive_mask()

### Community 103 - "Community 103"
Cohesion: 1.00
Nodes (2): Remove Negative (mask)     xlabel = "Max fraction of features removed"     ylabe, remove_negative_mask()

### Community 104 - "Community 104"
Cohesion: 1.00
Nodes (2): Remove Absolute (mask)     xlabel = "Max fraction of features removed"     ylabe, remove_absolute_mask__r2()

### Community 105 - "Community 105"
Cohesion: 1.00
Nodes (2): Remove Absolute (mask)     xlabel = "Max fraction of features removed"     ylabe, remove_absolute_mask__roc_auc()

### Community 106 - "Community 106"
Cohesion: 1.00
Nodes (2): Remove Positive (resample)     xlabel = "Max fraction of features removed"     y, remove_positive_resample()

### Community 107 - "Community 107"
Cohesion: 1.00
Nodes (2): Remove Negative (resample)     xlabel = "Max fraction of features removed"     y, remove_negative_resample()

### Community 108 - "Community 108"
Cohesion: 1.00
Nodes (2): Remove Absolute (resample)     xlabel = "Max fraction of features removed"     y, remove_absolute_resample__r2()

### Community 109 - "Community 109"
Cohesion: 1.00
Nodes (2): Remove Absolute (resample)     xlabel = "Max fraction of features removed"     y, remove_absolute_resample__roc_auc()

### Community 110 - "Community 110"
Cohesion: 1.00
Nodes (2): Remove Positive (impute)     xlabel = "Max fraction of features removed"     yla, remove_positive_impute()

### Community 111 - "Community 111"
Cohesion: 1.00
Nodes (2): Remove Negative (impute)     xlabel = "Max fraction of features removed"     yla, remove_negative_impute()

### Community 112 - "Community 112"
Cohesion: 1.00
Nodes (2): Remove Absolute (impute)     xlabel = "Max fraction of features removed"     yla, remove_absolute_impute__r2()

### Community 113 - "Community 113"
Cohesion: 1.00
Nodes (2): Remove Absolute (impute)     xlabel = "Max fraction of features removed"     yla, remove_absolute_impute__roc_auc()

### Community 114 - "Community 114"
Cohesion: 1.00
Nodes (2): Remove Negative (retrain)     xlabel = "Max fraction of features removed"     yl, remove_negative_retrain()

### Community 115 - "Community 115"
Cohesion: 1.00
Nodes (2): cric__ffnn(), 4-Layer Neural Network

### Community 116 - "Community 116"
Cohesion: 1.00
Nodes (1): human__decision_tree()

### Community 117 - "Community 117"
Cohesion: 1.00
Nodes (2): independentlinear60__ffnn(), 4-Layer Neural Network

### Community 119 - "Community 119"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 120 - "Community 120"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 121 - "Community 121"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 122 - "Community 122"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 123 - "Community 123"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 124 - "Community 124"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 125 - "Community 125"
Cohesion: 1.00
Nodes (1): Computes an optimal leaf ordering sort order using hclustering.          hclust(

### Community 126 - "Community 126"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 127 - "Community 127"
Cohesion: 1.00
Nodes (1): Stack two explanations column-wise.          Parameters         ----------

### Community 128 - "Community 128"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 129 - "Community 129"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 130 - "Community 130"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 131 - "Community 131"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 132 - "Community 132"
Cohesion: 1.00
Nodes (1): Pass-through from the underlying slicer object.

### Community 133 - "Community 133"
Cohesion: 1.00
Nodes (1): Display some basic printable info, but not everything.

## Knowledge Gaps
- **315 isolated node(s):** `An operation that has been applied to an Explanation object.`, `This metaclass exposes the Explanation object's class methods for creating templ`, `Element-wise absolute value op.`, `Hierarchical clustering op.`, `A sliceable set of parallel arrays representing a SHAP explanation.      Notes` (+310 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 67`** (2 nodes): `Action`, `Abstract action class.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 70`** (2 nodes): `An explainer object for a differentiable model using a given background dataset.`, `_TFGradient`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 78`** (1 nodes): `_PyTorchGradient`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 84`** (2 nodes): `Coefficient`, `Simply returns the model coefficients as the feature attributions.      This is`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 85`** (2 nodes): `LimeTabular`, `Simply wrap of lime.lime_tabular.LimeTabularExplainer into the common shap inter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 88`** (1 nodes): `ActionOptimizer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 91`** (1 nodes): `This defines some common colors.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 92`** (2 nodes): `group_features()`, `Numpy-style sum function.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 93`** (2 nodes): `benchmark()`, `Plot a BenchmarkResult or list of such results.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 94`** (2 nodes): `embedding()`, `Use the SHAP values as an embedding which we project to 2D for visualization.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 95`** (2 nodes): `group_difference()`, `This plots the difference in mean SHAP values between two groups.      It is use`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 96`** (2 nodes): `heatmap()`, `Create a heatmap plot of a set of SHAP values.      This plot is designed to sho`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 97`** (2 nodes): `TreeExplainer (independent)     color = red_blue_circle(0)     linestyle = dashe`, `tree_shap_independent_200()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 98`** (2 nodes): `Saabas     color = red_blue_circle(0)     linestyle = dotted`, `saabas()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 99`** (2 nodes): `Gain/Gini Importance     color = red_blue_circle(0.25)     linestyle = dotted`, `tree_gain()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 100`** (2 nodes): `keep_positive_resample()`, `Keep Positive (resample)     xlabel = "Max fraction of features kept"     ylabel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 101`** (2 nodes): `keep_positive_retrain()`, `Keep Positive (retrain)     xlabel = "Max fraction of features kept"     ylabel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 102`** (2 nodes): `Remove Positive (mask)     xlabel = "Max fraction of features removed"     ylabe`, `remove_positive_mask()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 103`** (2 nodes): `Remove Negative (mask)     xlabel = "Max fraction of features removed"     ylabe`, `remove_negative_mask()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 104`** (2 nodes): `Remove Absolute (mask)     xlabel = "Max fraction of features removed"     ylabe`, `remove_absolute_mask__r2()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 105`** (2 nodes): `Remove Absolute (mask)     xlabel = "Max fraction of features removed"     ylabe`, `remove_absolute_mask__roc_auc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 106`** (2 nodes): `Remove Positive (resample)     xlabel = "Max fraction of features removed"     y`, `remove_positive_resample()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 107`** (2 nodes): `Remove Negative (resample)     xlabel = "Max fraction of features removed"     y`, `remove_negative_resample()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 108`** (2 nodes): `Remove Absolute (resample)     xlabel = "Max fraction of features removed"     y`, `remove_absolute_resample__r2()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 109`** (2 nodes): `Remove Absolute (resample)     xlabel = "Max fraction of features removed"     y`, `remove_absolute_resample__roc_auc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 110`** (2 nodes): `Remove Positive (impute)     xlabel = "Max fraction of features removed"     yla`, `remove_positive_impute()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 111`** (2 nodes): `Remove Negative (impute)     xlabel = "Max fraction of features removed"     yla`, `remove_negative_impute()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 112`** (2 nodes): `Remove Absolute (impute)     xlabel = "Max fraction of features removed"     yla`, `remove_absolute_impute__r2()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 113`** (2 nodes): `Remove Absolute (impute)     xlabel = "Max fraction of features removed"     yla`, `remove_absolute_impute__roc_auc()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 114`** (2 nodes): `Remove Negative (retrain)     xlabel = "Max fraction of features removed"     yl`, `remove_negative_retrain()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 115`** (2 nodes): `cric__ffnn()`, `4-Layer Neural Network`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 116`** (1 nodes): `human__decision_tree()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 117`** (2 nodes): `independentlinear60__ffnn()`, `4-Layer Neural Network`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 119`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 120`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 121`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 122`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 123`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 124`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 125`** (1 nodes): `Computes an optimal leaf ordering sort order using hclustering.          hclust(`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 126`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 127`** (1 nodes): `Stack two explanations column-wise.          Parameters         ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 128`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 129`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 130`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 131`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 132`** (1 nodes): `Pass-through from the underlying slicer object.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 133`** (1 nodes): `Display some basic printable info, but not everything.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Explainer` connect `Community 16` to `Community 49`, `Community 11`, `Community 15`, `Community 17`, `Community 76`, `Community 3`, `Community 77`, `Community 78`, `Community 70`, `Community 18`, `Community 36`, `Community 26`, `Community 50`, `Community 19`, `Community 4`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Why does `Masker` connect `Community 20` to `Community 45`, `Community 72`, `Community 33`, `Community 3`, `Community 24`, `Community 38`, `Community 13`, `Community 63`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Why does `Model` connect `Community 61` to `Community 3`, `Community 14`, `Community 27`, `Community 21`, `Community 80`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 86 inferred relationships involving `Explainer` (e.g. with `AdditiveExplainer` and `Computes SHAP values for generalized additive models.      This assumes that the`) actually correct?**
  _`Explainer` has 86 INFERRED edges - model-reasoned connections that need verification._
- **Are the 68 inferred relationships involving `Masker` (e.g. with `Composite` and `This merges several maskers for different inputs together into a single composit`) actually correct?**
  _`Masker` has 68 INFERRED edges - model-reasoned connections that need verification._
- **Are the 31 inferred relationships involving `Model` (e.g. with `Computes log odds scores of generating output(text) for a given batch of input(t` and `The function updates output tokens.          It mimics the caching mechanism to`) actually correct?**
  _`Model` has 31 INFERRED edges - model-reasoned connections that need verification._
- **What connects `An operation that has been applied to an Explanation object.`, `This metaclass exposes the Explanation object's class methods for creating templ`, `Element-wise absolute value op.` to the rest of the system?**
  _315 weakly-connected nodes found - possible documentation gaps or missing edges._