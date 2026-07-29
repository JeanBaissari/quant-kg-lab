#!/usr/bin/env python3
"""
Label all 1,149 scikit-learn graph communities with 2-5 word labels.
Improved heuristics v2.
"""
import json, re, sys
from collections import defaultdict, Counter

GRAPH_PATH = '/home/baissarienterprises/projects/quant-kg-lab/knowledge_graphs/scikit-learn/repo/.graphify/graph.json'
LABELS_PATH = '/home/baissarienterprises/projects/quant-kg-lab/knowledge_graphs/scikit-learn/repo/.graphify/.graphify_labels.json'

# Known sklearn module naming
MODULE_NAMES = {
    'sklearn/base.py': 'Base Estimator',
    'sklearn/cluster': 'Clustering',
    'sklearn/cluster/_affinity_propagation': 'Affinity Propagation',
    'sklearn/cluster/_agglomerative': 'Agglomerative Clustering',
    'sklearn/cluster/_birch': 'Birch Clustering',
    'sklearn/cluster/_bisect_k_means': 'Bisecting K-Means',
    'sklearn/cluster/_dbscan': 'DBSCAN',
    'sklearn/cluster/_kmeans': 'K-Means',
    'sklearn/cluster/_mean_shift': 'Mean Shift',
    'sklearn/cluster/_optics': 'OPTICS Clustering',
    'sklearn/cluster/_spectral': 'Spectral Clustering',
    'sklearn/compose': 'Composite Estimators',
    'sklearn/decomposition': 'Matrix Decomposition',
    'sklearn/decomposition/_pca': 'PCA',
    'sklearn/decomposition/_nmf': 'NMF',
    'sklearn/decomposition/_dict_learning': 'Dictionary Learning',
    'sklearn/decomposition/_factor_analysis': 'Factor Analysis',
    'sklearn/decomposition/_fastica': 'FastICA',
    'sklearn/decomposition/_incremental_pca': 'Incremental PCA',
    'sklearn/decomposition/_kernel_pca': 'Kernel PCA',
    'sklearn/decomposition/_sparse_pca': 'Sparse PCA',
    'sklearn/decomposition/_truncated_svd': 'Truncated SVD',
    'sklearn/ensemble': 'Ensemble Methods',
    'sklearn/ensemble/_bagging': 'Bagging',
    'sklearn/ensemble/_forest': 'Random Forest',
    'sklearn/ensemble/_gb': 'Gradient Boosting',
    'sklearn/ensemble/_hist_gradient_boosting': 'Histogram GBM',
    'sklearn/ensemble/_iforest': 'Isolation Forest',
    'sklearn/ensemble/_stacking': 'Stacking',
    'sklearn/ensemble/_voting': 'Voting',
    'sklearn/ensemble/_weight_boosting': 'AdaBoost',
    'sklearn/feature_extraction': 'Feature Extraction',
    'sklearn/feature_extraction/text': 'Text Feature Extraction',
    'sklearn/feature_selection': 'Feature Selection',
    'sklearn/feature_selection/_from_model': 'Model-Based Selection',
    'sklearn/feature_selection/_rfe': 'Recursive Feature Elimination',
    'sklearn/feature_selection/_univariate_selection': 'Univariate Selection',
    'sklearn/gaussian_process': 'Gaussian Processes',
    'sklearn/impute': 'Imputation',
    'sklearn/inspection': 'Inspection',
    'sklearn/inspection/_partial_dependence': 'Partial Dependence',
    'sklearn/inspection/_permutation_importance': 'Permutation Importance',
    'sklearn/kernel_approximation': 'Kernel Approximation',
    'sklearn/linear_model': 'Linear Models',
    'sklearn/linear_model/_base': 'Linear Regression',
    'sklearn/linear_model/_coordinate_descent': 'Coordinate Descent',
    'sklearn/linear_model/_glm': 'GLM',
    'sklearn/linear_model/_least_angle': 'LARS Lasso',
    'sklearn/linear_model/_logistic': 'Logistic Regression',
    'sklearn/linear_model/_omp': 'Orthogonal Matching Pursuit',
    'sklearn/linear_model/_passive_aggressive': 'Passive Aggressive',
    'sklearn/linear_model/_perceptron': 'Perceptron',
    'sklearn/linear_model/_ransac': 'RANSAC',
    'sklearn/linear_model/_ridge': 'Ridge Regression',
    'sklearn/linear_model/_sag': 'SAG Solver',
    'sklearn/linear_model/_sgd_fast': 'SGD Classifier',
    'sklearn/linear_model/_stochastic_gradient': 'SGD',
    'sklearn/linear_model/_theil_sen': 'Theil-Sen',
    'sklearn/manifold': 'Manifold Learning',
    'sklearn/manifold/_t_sne': 't-SNE',
    'sklearn/metrics': 'Metrics',
    'sklearn/metrics/_classification': 'Classification Metrics',
    'sklearn/metrics/_ranking': 'Ranking Metrics',
    'sklearn/metrics/_regression': 'Regression Metrics',
    'sklearn/metrics/cluster': 'Clustering Metrics',
    'sklearn/metrics/pairwise': 'Pairwise Metrics',
    'sklearn/mixture': 'Gaussian Mixtures',
    'sklearn/model_selection': 'Model Selection',
    'sklearn/model_selection/_search': 'Hyperparameter Search',
    'sklearn/model_selection/_split': 'Data Splitting',
    'sklearn/model_selection/_validation': 'Cross Validation',
    'sklearn/multiclass': 'Multiclass',
    'sklearn/multioutput': 'Multioutput',
    'sklearn/naive_bayes': 'Naive Bayes',
    'sklearn/neighbors': 'Nearest Neighbors',
    'sklearn/neighbors/_base': 'KNN Base',
    'sklearn/neural_network': 'Neural Networks',
    'sklearn/neural_network/_multilayer_perceptron': 'MLP',
    'sklearn/neural_network/_rbm': 'RBM',
    'sklearn/pipeline': 'Pipeline',
    'sklearn/preprocessing': 'Preprocessing',
    'sklearn/preprocessing/_data': 'Scalers',
    'sklearn/preprocessing/_discretization': 'Discretization',
    'sklearn/preprocessing/_encoders': 'Encoders',
    'sklearn/preprocessing/_label': 'Label Encoding',
    'sklearn/preprocessing/_polynomial': 'Polynomial Features',
    'sklearn/preprocessing/_target_encoder': 'Target Encoding',
    'sklearn/random_projection': 'Random Projection',
    'sklearn/semi_supervised': 'Semi-Supervised',
    'sklearn/svm': 'SVM',
    'sklearn/tree': 'Decision Trees',
    'sklearn/utils': 'Utilities',
    'sklearn/utils/validation': 'Input Validation',
    'sklearn/utils/extmath': 'Extended Math',
    'sklearn/utils/optimize': 'Optimization',
    'benchmarks': 'Benchmarks',
    'examples': 'Examples',
    'doc': 'Documentation',
    'asv_benchmarks': 'ASV Benchmarks',
    'maint_tools': 'Maintenance Tools',
    'build_tools': 'Build Tools',
}

# ML-specific class names to recognize
ML_CLASSES = {
    'LogisticRegression', 'LinearRegression', 'Ridge', 'RidgeCV', 'RidgeClassifier',
    'Lasso', 'LassoCV', 'LassoLars', 'ElasticNet', 'ElasticNetCV',
    'SGDClassifier', 'SGDRegressor', 'SGDOneClassSVM',
    'PassiveAggressiveClassifier', 'PassiveAggressiveRegressor',
    'Perceptron', 'SVC', 'SVR', 'NuSVC', 'NuSVR', 'LinearSVC', 'LinearSVR', 'OneClassSVM',
    'KNeighborsClassifier', 'KNeighborsRegressor', 'NearestNeighbors',
    'RadiusNeighborsClassifier', 'RadiusNeighborsRegressor',
    'NearestCentroid', 'KNeighborsTransformer',
    'GaussianNB', 'MultinomialNB', 'BernoulliNB', 'ComplementNB', 'CategoricalNB',
    'DecisionTreeClassifier', 'DecisionTreeRegressor',
    'ExtraTreeClassifier', 'ExtraTreeRegressor',
    'RandomForestClassifier', 'RandomForestRegressor',
    'ExtraTreesClassifier', 'ExtraTreesRegressor',
    'GradientBoostingClassifier', 'GradientBoostingRegressor',
    'HistGradientBoostingClassifier', 'HistGradientBoostingRegressor',
    'AdaBoostClassifier', 'AdaBoostRegressor',
    'BaggingClassifier', 'BaggingRegressor',
    'VotingClassifier', 'VotingRegressor',
    'StackingClassifier', 'StackingRegressor',
    'IsolationForest', 'LocalOutlierFactor',
    'MLPClassifier', 'MLPRegressor',
    'BernoulliRBM',
    'PCA', 'KernelPCA', 'IncrementalPCA', 'SparsePCA', 'MiniBatchSparsePCA',
    'TruncatedSVD', 'NMF', 'MiniBatchNMF', 'LatentDirichletAllocation',
    'FastICA', 'FactorAnalysis', 'DictionaryLearning', 'MiniBatchDictionaryLearning',
    'KMeans', 'MiniBatchKMeans', 'BisectingKMeans',
    'DBSCAN', 'OPTICS', 'MeanShift',
    'AffinityPropagation', 'AgglomerativeClustering', 'Birch',
    'SpectralClustering', 'SpectralBiclustering', 'SpectralCoclustering',
    'FeatureAgglomeration',
    'GaussianMixture', 'BayesianGaussianMixture',
    'TSNE', 'Isomap', 'MDS', 'SpectralEmbedding', 'LocallyLinearEmbedding',
    'LabelPropagation', 'LabelSpreading', 'SelfTrainingClassifier',
    'Pipeline', 'FeatureUnion', 'ColumnTransformer',
    'StandardScaler', 'MinMaxScaler', 'MaxAbsScaler', 'RobustScaler',
    'Normalizer', 'Binarizer', 'QuantileTransformer', 'PowerTransformer',
    'KBinsDiscretizer', 'SplineTransformer',
    'OneHotEncoder', 'OrdinalEncoder', 'LabelEncoder', 'LabelBinarizer',
    'TargetEncoder', 'PolynomialFeatures', 'FunctionTransformer',
    'SimpleImputer', 'IterativeImputer', 'KNNImputer', 'MissingIndicator',
    'SelectKBest', 'SelectPercentile', 'SelectFpr', 'SelectFdr', 'SelectFwe',
    'GenericUnivariateSelect', 'VarianceThreshold',
    'RFE', 'RFECV', 'SelectFromModel', 'SequentialFeatureSelector',
    'RBFSampler', 'Nystroem', 'AdditiveChi2Sampler', 'SkewedChi2Sampler',
    'PolynomialCountSketch',
    'GaussianProcessClassifier', 'GaussianProcessRegressor',
    'LinearDiscriminantAnalysis', 'QuadraticDiscriminantAnalysis',
    'PLSRegression', 'PLSCanonical', 'PLSSVD', 'CCA',
    'EllipticEnvelope', 'EmpiricalCovariance', 'MinCovDet', 'ShrunkCovariance',
    'LedoitWolf', 'OAS', 'GraphicalLasso', 'GraphicalLassoCV',
    'RANSACRegressor', 'TheilSenRegressor', 'HuberRegressor',
    'QuantileRegressor', 'GammaRegressor', 'PoissonRegressor', 'TweedieRegressor',
    'OrthogonalMatchingPursuit', 'OrthogonalMatchingPursuitCV',
    'Lars', 'LarsCV', 'LassoLarsIC', 'LassoLarsCV',
    'BayesianRidge', 'ARDRegression',
    'MultiTaskLasso', 'MultiTaskElasticNet', 'MultiTaskLassoCV', 'MultiTaskElasticNetCV',
    'MultiOutputRegressor', 'MultiOutputClassifier',
    'ClassifierChain', 'RegressorChain',
    'OneVsRestClassifier', 'OneVsOneClassifier', 'OutputCodeClassifier',
    'CalibratedClassifierCV',
    'TransformedTargetRegressor',
    'IsotonicRegression',
    'KernelRidge',
    'NeighborhoodComponentsAnalysis',
    'GraphicalLasso',
}

def get_detailed_module(source_path):
    """Get the most specific module name for a source path."""
    if not source_path:
        return None
    parts = source_path.split('/')
    # Try increasingly specific paths
    for depth in range(len(parts), 0, -1):
        candidate = '/'.join(parts[:depth])
        if candidate in MODULE_NAMES:
            return MODULE_NAMES[candidate]
    return None

def extract_ml_classes(labels):
    """Extract known ML class names from labels."""
    found = set()
    for label in labels:
        for cls in ML_CLASSES:
            if cls in label:
                found.add(cls)
    return found

def extract_source_module_group(sources):
    """Get the dominant source module."""
    counter = Counter()
    for s in sources:
        mod = get_detailed_module(s)
        if mod:
            counter[mod] += 1
    return counter

def derive_label_v2(community_id, nodes):
    """Derive a 2-5 word label for a community."""
    labels = [n['label'] for n in nodes]
    sources = [n.get('source_file', '') for n in nodes if n.get('source_file')]
    file_types = Counter(n.get('file_type', '') for n in nodes)
    
    # Single node community: use cleaned label
    if len(nodes) == 1:
        label = nodes[0]['label'].strip().rstrip('.')
        # Clean: remove leading docstring markers
        label = re.sub(r'^[=\s]+', '', label)
        label = re.sub(r'\s*\.\s*$', '', label)
        if len(label) > 55:
            label = label[:54] + '…'
        if not label or len(label) < 3:
            label = nodes[0].get('id', 'Unknown')
        return label
    
    # Get source modules
    mod_counter = extract_source_module_group(sources)
    top_mod = mod_counter.most_common(1)
    top_mod_name = top_mod[0][0] if top_mod else None
    
    # Get ML classes
    ml_classes = extract_ml_classes(labels)
    
    # Count test functions
    test_funcs = [l for l in labels if l.startswith('test_')]
    test_ratio = len(test_funcs) / max(len(labels), 1)
    
    # Check if documentation
    is_docs = file_types.get('markdown', 0) > len(nodes) * 0.5
    if is_docs:
        return 'Documentation'
    
    # Check if examples
    example_count = sum(1 for s in sources if 'examples/' in s)
    if example_count > len(sources) * 0.5:
        # Extract example topic
        example_dirs = Counter()
        for s in sources:
            if 'examples/' in s:
                parts = s.split('/')
                ex_idx = parts.index('examples')
                if ex_idx + 1 < len(parts):
                    example_dirs[parts[ex_idx + 1]] += 1
        top_ex = example_dirs.most_common(1)
        if top_ex:
            return f"Example: {top_ex[0][0].replace('_', ' ').title()}"
        return 'Examples'
    
    # Check if benchmarks
    bench_count = sum(1 for s in sources if 'benchmark' in s.lower())
    if bench_count > len(sources) * 0.5:
        return 'Benchmarks'
    
    # Check if test community
    is_test = (
        (test_ratio > 0.4 and len(test_funcs) > 3) or
        (test_ratio > 0.2 and len(test_funcs) > 10)
    )
    
    parts = []
    
    if is_test:
        # What's being tested?
        if top_mod_name:
            parts.append(top_mod_name)
        elif ml_classes:
            parts.append(sorted(ml_classes)[0])
        else:
            # Look at source dirs
            dir_counter = Counter()
            for s in sources:
                parts_s = s.replace('/tests', '').split('/')
                if len(parts_s) > 1:
                    dir_counter[parts_s[-2]] += 1
            top_dir = dir_counter.most_common(1)
            if top_dir:
                mod = MODULE_NAMES.get(f"sklearn/{top_dir[0][0]}", top_dir[0][0].replace('_', ' ').title())
                parts.append(mod)
        parts.append('Tests')
        return ' '.join(parts[:5])
    
    # Non-test community: build from module + classes
    if top_mod_name:
        parts.append(top_mod_name)
    
    # Add distinctive classes
    if ml_classes:
        # Pick the most representative
        for cls in sorted(ml_classes):
            if cls not in ' '.join(parts):
                parts.append(cls)
                if len(parts) >= 5:
                    break
    
    # If still short, add key terms from analysis
    if len(parts) < 2:
        # Look at node IDs for module hints
        id_counter = Counter()
        for n in nodes:
            nid = n.get('id', '')
            # Extract module prefix from node IDs
            parts_id = nid.split('_')
            if len(parts_id) > 1:
                prefix = parts_id[0]
                if prefix not in ('test', 'check', 'plot', 'make'):
                    id_counter[prefix] += 1
        
        top_id_prefixes = [p for p, c in id_counter.most_common(3) if c > 2]
        for p in top_id_prefixes:
            if p not in ' '.join(parts).lower():
                parts.append(p.replace('_', ' ').title())
    
    # If still short, use source file directory
    if len(parts) < 2:
        dir_counter = Counter()
        for s in sources:
            parts_s = s.split('/')
            if len(parts_s) > 2:
                dir_counter['/'.join(parts_s[:-1])] += 1
        top_dir = dir_counter.most_common(1)
        if top_dir:
            last = top_dir[0][0].split('/')[-1]
            mod = MODULE_NAMES.get(f"sklearn/{last}", last.replace('_', ' ').title())
            if mod not in parts:
                parts.append(mod)
    
    # Fallback: use first meaningful label
    if not parts:
        for l in labels:
            clean = re.sub(r'[=#\-\s]+', ' ', l).strip()
            clean = re.sub(r'[^a-zA-Z\s]', '', clean).strip()
            words = clean.split()
            if len(words) >= 2 and clean.lower() not in ('parameters', 'fit', 'compute', 'this', 'the', 'check', 'test'):
                parts.append(' '.join(words[:4]))
                break
        if not parts:
            parts.append('Miscellaneous')
    
    result = ' '.join(parts)
    words = result.split()
    return ' '.join(words[:5])


# Main
print(f"Loading graph from {GRAPH_PATH}...")
with open(GRAPH_PATH) as f:
    graph = json.load(f)

print(f"Grouping {len(graph['nodes'])} nodes by community...")
community_nodes = defaultdict(list)
for node in graph['nodes']:
    cid = node.get('community')
    if cid is not None:
        community_nodes[cid].append(node)

print(f"Found {len(community_nodes)} communities. Labeling...")

labels = {}
for cid in sorted(community_nodes.keys()):
    label = derive_label_v2(cid, community_nodes[cid])
    labels[str(cid)] = label

# Write labels
print(f"Writing {len(labels)} labels to {LABELS_PATH}...")
with open(LABELS_PATH, 'w') as f:
    json.dump(labels, f, indent=2)

print("Done!")
print(f"\nSample labels:")
# Show diverse samples
sample_ids = [0, 1, 2, 5, 10, 20, 30, 50, 100, 150, 200, 300, 500, 700, 1000, 1148]
for cid in sample_ids:
    if cid in community_nodes:
        print(f"  Community {cid}: \"{labels[str(cid)]}\" ({len(community_nodes[cid])} nodes)")

# Stats
label_counts = Counter(labels.values())
print(f"\nMost common labels:")
for label, count in label_counts.most_common(20):
    print(f"  \"{label}\": {count}")
