# Edge Audit — shap

**Date**: 2026-08-13

## Summary

- Total edges: 1752
- EXTRACTED: 1543 (88.1%)
- INFERRED: 209 (11.9%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `Explainer`: 86 inferred edges
- `Masker`: 68 inferred edges
- `Model`: 31 inferred edges
- `TreeExplainer`: 6 inferred edges
- `PyTorchDeep`: 5 inferred edges
- `TFDeep`: 5 inferred edges
- `DimensionError`: 4 inferred edges
- `KernelExplainer`: 3 inferred edges
- `DeepExplainer`: 2 inferred edges
- `Return an explanation object for the model applied to X.          Parameters`: 2 inferred edges
- `Return approximate SHAP values for the model applied to the data given by X.`: 2 inferred edges
- `An explainer object for a differentiable model using a given background dataset.`: 2 inferred edges
- `Meant to approximate SHAP values for deep learning models.      This is an enhan`: 2 inferred edges
- `UnsupportedModule`: 2 inferred edges
- `ActionOptimizer`: 1 inferred edges
- `Action`: 1 inferred edges
- `AdditiveExplainer`: 1 inferred edges
- `Computes SHAP values for generalized additive models.      This assumes that the`: 1 inferred edges
- `Determines if this explainer can handle the given model.          This is an abs`: 1 inferred edges
- `Explains a single row and returns the tuple (row_values, row_expected_values, ro`: 1 inferred edges

## Cross-Module Suspicious Edges

- `_tree.py` ↔ `_explainer.py`: 33
- `_text.py` ↔ `_masker.py`: 24
- `_tabular.py` ↔ `_masker.py`: 15
- `_exact.py` ↔ `_explainer.py`: 11
- `_teacher_forcing.py` ↔ `_model.py`: 11
- `_topk_lm.py` ↔ `_model.py`: 10
- `_partition.py` ↔ `_explainer.py`: 8
- `_image.py` ↔ `_masker.py`: 8
- `_gradient.py` ↔ `_explainer.py`: 7
- `_linear.py` ↔ `_explainer.py`: 7
- `_text_generation.py` ↔ `_model.py`: 7
- `_additive.py` ↔ `_explainer.py`: 6
- `_permutation.py` ↔ `_explainer.py`: 6
- `_composite.py` ↔ `_masker.py`: 6
- `_fixed_composite.py` ↔ `_masker.py`: 6
- `_output_composite.py` ↔ `_masker.py`: 6
- `_coalition.py` ↔ `_explainer.py`: 5
- `_gpu_tree.py` ↔ `_tree.py`: 5
- `_clustering.py` ↔ `_exceptions.py`: 4
- `_kernel.py` ↔ `_explainer.py`: 3
