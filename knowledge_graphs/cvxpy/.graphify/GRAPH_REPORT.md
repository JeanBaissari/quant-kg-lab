# Graph Report - knowledge_graphs/cvxpy/repo/cvxpy  (2026-08-12)

## Corpus Check
- 387 files · ~236,385 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 6380 nodes · 16515 edges · 297 communities detected
- Non-singleton communities: 292
- Extraction: EXTRACTED: 42.7% · INFERRED: 57.0%
- Edge kinds: calls: 947 · contains: 929 · imports: 7 · imports_from: 6 · inherits: 233 · method: 2392 · rationale_for: 2590 · uses: 9411

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 387 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `e3b50dc`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `Constraint` (831)
- `Expression` (725)
- `Atom` (500)
- `Solution` (449)
- `Variable` (401)
- `reshape` (318)
- `AffAtom` (312)
- `ConicSolver` (283)
- `Elementwise` (243)
- `conj` (188)

## Surprising Connections (you probably didn't know these)
- `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t` --uses--> `Expression`  [INFERRED]
  atoms/affine/diff.py → expressions/expression.py
- `Computes kth order differences along the specified axis.      Takes in an array` --uses--> `Expression`  [INFERRED]
  atoms/affine/diff.py → expressions/expression.py
- `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t` --uses--> `Expression`  [INFERRED]
  atoms/harmonic_mean.py → expressions/expression.py
- `The harmonic mean of ``x``.      Parameters     ----------     x : Expression or` --uses--> `Expression`  [INFERRED]
  atoms/harmonic_mean.py → expressions/expression.py
- `Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th` --uses--> `Expression`  [INFERRED]
  atoms/inv_prod.py → expressions/expression.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.03
Nodes (161): AddExpression, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Is the expression symmetric?, Is the expression Hermitian?, Returns a shallow copy of the AddExpression atom.          Parameters         --, Sum the linear expressions.          Parameters         ----------         arg_o, The sum of any number of expressions., Returns the (row, col) shape of the expression. (+153 more)

### Community 1 - "Community 1"
Cohesion: 0.02
Nodes (80): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, Abstract base class for affine atoms., By default, the sign is the most general of all the argument signs., Is the expression imaginary?, Is the expression complex valued?, Does the affine head of the expression contain a quadratic term?          The af, Atom (+72 more)

### Community 2 - "Community 2"
Cohesion: 0.02
Nodes (74): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Returns the axis being summed., Create a sparse upper triangular matrix of ones.      This avoids allocating a d, Cumulative sum of the elements of an expression.      Attributes     ----------, Validate axis, but handle 0D arrays specially., Returns the cumulative sum of elements of an expression over an axis., Flattened if axis=None, otherwise same as input., Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix (+66 more)

### Community 3 - "Community 3"
Cohesion: 0.02
Nodes (77): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Returns self as a constant., The numeric value of the constant., Returns whether the constant is elementwise positive., Gives the (sub/super)gradient of the expression w.r.t. each variable.          M, Returns the graph implementation of the object.          Returns:             A, Returns a string with information about the expression., Return bounds for this constant.          For constants, the bounds are exactly (+69 more)

### Community 4 - "Community 4"
Cohesion: 0.03
Nodes (68): partial_trace(), Copyright 2022, adapted from Convex.jl.  Licensed under the Apache License, Vers, Helper function for partial trace.      Parameters     ----------     expr : :cl, Assumes :math:`\\texttt{expr} = X_1 \\otimes \\cdots \\otimes X_n` is a 2D Krone, _term(), nsd_wrap, psd_wrap, symmetric_wrap (+60 more)

### Community 5 - "Community 5"
Cohesion: 0.02
Nodes (61): Complex2Real, Copyright 2017 Robin Verschueren  Licensed under the Apache License, Version 2.0, Split complex gradients into real/imag gradients for backward diff.          Tra, Combine real/imag deltas into complex deltas for forward diff.          Transfor, Combine real/imag gradients into complex gradient for backward diff.          Fo, Split complex deltas into real/imag deltas for forward diff.          For comple, # TODO: implement dual variable recovery, Lifts complex numbers to a real representation.      For DPP (Disciplined Parame (+53 more)

### Community 6 - "Community 6"
Cohesion: 0.04
Nodes (49): Copyright 2018 Akshay Agrawal  Licensed under the Apache License, Version 2.0 (t, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Copyright 2013 Steven Diamond, 2022 - the CVXPY Authors.  Licensed under the Apa, Constant, Returns the (row, col) dimensions of the expression., A constant value.      Raw numerical constants such as Python primitive types or, Check if the original value has boolean dtype., Expression (+41 more)

### Community 7 - "Community 7"
Cohesion: 0.03
Nodes (48): DIFFCP, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Returns the result of the call to the solver.          Parameters         ------, Returns bibtex citation for the solver.          Parameters         ----------, An interface for the DIFFCP solver, a differentiable wrapper of SCS and ECOS., The name of the solver., Does not support a quadratic objective., Returns the solution to the original problem given the inverse_data. (+40 more)

### Community 8 - "Community 8"
Cohesion: 0.03
Nodes (55): CanonBackend, Sparse representation of a 3D Tensor. Semantically similar to COO format, with o, Concatenates the row, col, parameter_offset, and data fields of a list of, Returns a single slice of the tensor for a given parameter offset., CanonBackend handles the compilation from LinOp trees to a final sparse tensor t, Main function called from canonInterface.         Given a list of LinOp trees, e, Concatenate multiple tensors along a specified axis.          This method perfor, TensorRepresentation (+47 more)

### Community 9 - "Community 9"
Cohesion: 0.09
Nodes (65): Chain, DPPError, Error thrown for DPP violations., InverseData, Cache, Copyright 2013 Steven Diamond, 2017 Akshay Agrawal  Licensed under the Apache Li, Compute the gradient of a solution with respect to Parameters.          This met, Apply the derivative of the solution map to perturbations in the Parameters (+57 more)

### Community 10 - "Community 10"
Cohesion: 0.03
Nodes (51): ConicSolver, Conic solver class with reduction semantics, Returns the solution to the original problem given the inverse_data., CUCLARABEL, dims_to_solver_cones(), Copyright 2022, the CVXPY Authors  Licensed under the Apache License, Version 2., Returns the result of the call to the solver.          Parameters         ------, Returns bibtex citation for the solver.          Parameters         ---------- (+43 more)

### Community 11 - "Community 11"
Cohesion: 0.04
Nodes (54): as_block_diag_linear_operator(), as_linear_operator(), IdentityOperator, LinearOperator, NegativeIdentityOperator, Copyright 2017 Robin Verschueren, 2017 Akshay Agrawal  Licensed under the Apache, Returns a sparse matrix that spaces out an expression.          Parameters, Returns a ParamConeProg whose problem data tensors will yield the         coeffi (+46 more)

### Community 12 - "Community 12"
Cohesion: 0.06
Nodes (42): A single variable with no associated cone (n=1 base case in tree decomposition)., SingleVarNode, _build_pow_tree(), ExactCone2Cone, _extract_pow_duals(), _extract_pow_duals_recursive(), NonPosConversion, PowNDConversion (+34 more)

### Community 13 - "Community 13"
Cohesion: 0.04
Nodes (40): Copyright 2013 Steven Diamond, 2017 Akshay Agrawal, 2017 Robin Verschueren  Lice, Recursively canonicalize an Expression.          Canonicalizing an Expression yi, Canonicalize an expression, w.r.t. canonicalized arguments.          Parameters, Build a hashable structural key for an Expression subtree.          Returns None, Whether canonicalize_tree result for ``expr`` depends on affine_above., Reduce DCP problems to a conic form.      This reduction takes as input (minimiz, A problem is accepted if it is a minimization and is DCP., Converts a DCP problem to a conic form. (+32 more)

### Community 14 - "Community 14"
Cohesion: 0.03
Nodes (39): upper_tri, Copyright 2022, the CVXPY authors  Licensed under the Apache License, Version 2., gauss_legendre(), OpRelEntrConeQuad_canon(), pow_3d_canon(), Copyright 2022 the CVXPY developers  Licensed under the Apache License, Version, Convert PowCone3D to SOC constraints via rational approximation.      con : PowC, Helper function for returning the weights and nodes for an     n-point Gauss-Leg (+31 more)

### Community 15 - "Community 15"
Cohesion: 0.05
Nodes (44): Canonicalization, ApproxCone2Cone, SOCDim3, ConeMatrixStuffing, Dcp2Cone, Dgp2Dcp, Copyright 2018 Akshay Agrawal  Licensed under the Apache License, Version 2.0 (t, Apply chain rule for exp transformation in forward diff.          DGP variables (+36 more)

### Community 16 - "Community 16"
Cohesion: 0.03
Nodes (42): Cone, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, A base class for all conic constraints in CVXPY      These are special constrain, Method for modelling problems with the dual cone of `Cone`          If the user, Residual of the dual variable with respect to the dual cone.          This const, Copyright 2013 Steven Diamond, 2022 - the CVXPY Authors  Licensed under the Apac, # TODO: implement me., # TODO: implement me (+34 more)

### Community 17 - "Community 17"
Cohesion: 0.03
Nodes (39): PythonCanonBackend, Returns tensor of a parameter node, i.e., eye(n) across axes 0 and 2, where n is, Flatten into 2D scipy sparse matrix in order-order and transpose.          Param, Select 'rows' from tensor., Apply 'func' across all variables and parameter slices., Create new TensorView with same shape information as self, but new data., Each tensor has 3 dimensions. The first one is the parameter axis, the second on, Depth-first parsing of a linOp node.          Parameters         ---------- (+31 more)

### Community 18 - "Community 18"
Cohesion: 0.03
Nodes (39): floor, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Returns sign (is positive, is negative) of the expression., Is the atom log-log convex?, Is the atom log-log concave?, Is the atom quasiconvex?, Is the atom quasiconcave?, Is the composition non-decreasing in argument idx? (+31 more)

### Community 19 - "Community 19"
Cohesion: 0.04
Nodes (66): make_smooth_range_dom_canon(), Copyright 2025 CVXPY developers  Licensed under the Apache License, Version 2.0, Canonicalize a smooth atom with full domain (and one argument)        whose chai, Canonicalize a smooth atom with full domain (and potentially multiple        arg, Canonicalize a smooth atom (with one argument) whose domain is the        nonneg, Wrapper for canonicalizers whose domain is a bounded interval., smooth_full_domain_canon_chain_rule(), smooth_full_domain_canon_non_chain_rule() (+58 more)

### Community 20 - "Community 20"
Cohesion: 0.05
Nodes (36): # TODO: remove pwl canonicalize methods, use EliminatePwl reduction instead, And, iff(), implies(), Not, Or, Logical AND of boolean expressions.      Returns 1 if and only if all arguments, Equivalent to `cp.conj(self)`. (+28 more)

### Community 21 - "Community 21"
Cohesion: 0.04
Nodes (42): CUOPT, Copyright 2025 NVIDIA CORPORATION  Licensed under the Apache License, Version 2., The name of the solver., Cuopt supports quadratic objective., Returns a new problem and data for inverting the new solution.          Returns, Returns the solution to the original problem given the inverse_data., COO for -x_0^2 + sum_{i>0} x_i^2 <= 0 (cuOpt Lorentz / CVXPY SOC)., Pad Q to num_vars x num_vars for cuOpt SOC variable permutation. (+34 more)

### Community 22 - "Community 22"
Cohesion: 0.04
Nodes (18): ParameterError, Error thrown for accessing the value of an unspecified parameter., Bounds, Get constraint bounds for all constraints.         Also converts inequalities to, Loop through all variables and collect the intial point., Returns the scalar value of the objective given x., Returns the gradient of the objective with respect to x., Returns the constraint values. (+10 more)

### Community 23 - "Community 23"
Cohesion: 0.04
Nodes (26): DivExpression, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Sums the entries of value., Sum the linear expression's entries.          Parameters         ----------, Wrapper for Sum class., Sum the entries of an expression over a given axis.      Parameters     --------, Is the atom log-log convex?, Is the atom log-log concave? (+18 more)

### Community 24 - "Community 24"
Cohesion: 0.05
Nodes (36): _add_psd_bound_rows(), _bound_selector(), COPT, This file is the CVXPY conic extension of the Cardinal Optimizer, Can COPT solve the problem?, Returns a new problem and data for inverting the new solution.          Returns, Map the stacked ``[eq; ineq]`` dual vector to a CVXPY dual dict.          Shared, Returns the solution to the original problem given the inverse_data. (+28 more)

### Community 25 - "Community 25"
Cohesion: 0.04
Nodes (27): _as_sparse_array(), BinaryOperator, matmul(), MulExpression, outer(), Base class for expressions involving binary operators. (other than addition), scalar_product(), vdot() (+19 more)

### Community 26 - "Community 26"
Cohesion: 0.07
Nodes (46): "prob" is a ParamConeProg which represents              (Aff)   min{ c.T @ x : A, get_all_cone_ids(), get_leaf_nodes(), get_root_cone_id(), LeafNode, Copyright 2025, the CVXPY authors  Licensed under the Apache License, Version 2., Leaf node: a single 3D cone with original variable indices., Internal node combining two subtrees with a 3D cone. (+38 more)

### Community 27 - "Community 27"
Cohesion: 0.04
Nodes (40): bmat(), _promote_to_2d(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Constructs a block matrix.      Takes a list of lists. Each internal list is sta, Promote a scalar or 1-D block to a 2-D row, like ``numpy.block``., _contract_pair(), einsum(), _get_path() (+32 more)

### Community 28 - "Community 28"
Cohesion: 0.05
Nodes (37): CLARABEL, dims_to_solver_cones(), Copyright 2022, the CVXPY Authors  Licensed under the Apache License, Version 2., The name of the solver., Clarabel supports quadratic objective with any combination         of conic cons, Returns the solution to the original problem given the inverse_data., Returns the result of the call to the solver.          Parameters         ------, Returns bibtex citation for the solver.          Parameters         ---------- (+29 more)

### Community 29 - "Community 29"
Cohesion: 0.05
Nodes (45): _build_interleaved_param_mul(), _build_interleaved_param_rmul(), compute_indptr(), coo_matmul(), coo_mul_elem(), coo_reshape(), CooTensor, _empty_float() (+37 more)

### Community 30 - "Community 30"
Cohesion: 0.06
Nodes (33): COPT, Copyright 2025, the CVXPY developers  Licensed under the Apache License, Version, NLP interface for the COPT solver., Returns bibtex citation for the solver.          Parameters         ----------, Returns the solution to the original problem given the inverse_data., Returns the result of the call to the solver.          Parameters         ------, IPOPT, Copyright 2025, the CVXPY developers  Licensed under the Apache License, Version (+25 more)

### Community 31 - "Community 31"
Cohesion: 0.04
Nodes (27): matrix_frac(), MatrixFrac, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Returns the (row, col) shape of the expression., Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Quadratic if x is affine and P is constant. (+19 more)

### Community 32 - "Community 32"
Cohesion: 0.06
Nodes (34): Constant, _build_interleaved_mul(), _build_interleaved_rmul(), CooCanonBackend, Select 'rows' from each parameter slice.          O(nnz) operation - just filter, Apply 'func' across all variables and parameter slices.          func signature:, Canon backend using CooTensorView for O(nnz) operations.      This backend store, Return an empty CooTensorView. (+26 more)

### Community 33 - "Community 33"
Cohesion: 0.04
Nodes (28): huber(), HuberAtom, HuberPerspectiveAtom, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Returns the huber function applied elementwise to x., Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx? (+20 more)

### Community 34 - "Community 34"
Cohesion: 0.05
Nodes (33): quad_over_lin, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Returns sign (is positive, is negative) of the expression., Is the atom log-log convex?, Is the atom log-log concave?, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Check dimensions of arguments. (+25 more)

### Community 35 - "Community 35"
Cohesion: 0.05
Nodes (22): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Copyright 2022, the CVXPY authors  Licensed under the Apache License, Version 2., Dualize, Copyright 2020 the CVXPY developers  Licensed under the Apache License, Version, ``solution`` is a CVXPY Solution object, formatted where              (D-Opt) ma, CVXPY represents mixed-integer cone programs as          (Aff)   min{ c.T @ x : (+14 more)

### Community 36 - "Community 36"
Cohesion: 0.05
Nodes (27): CBC, Copyright 2016 Sascha-Dominic Schnug  Licensed under the Apache License, Version, Returns bibtex citation for the solver.          Parameters         ----------, An interface to the CBC solver, The name of the solver., Can Cbc solve the problem?, Returns a new problem and data for inverting the new solution.          Returns, Returns the solution to the original problem given the inverse_data. (+19 more)

### Community 37 - "Community 37"
Cohesion: 0.04
Nodes (17): Elementwise, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, asinh, atanh, Copyright 2025 CVXPY Developers  Licensed under the Apache License, Version 2.0, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Returns constraints describing the domain of the node. (+9 more)

### Community 38 - "Community 38"
Cohesion: 0.05
Nodes (26): lambda_max, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Maximum eigenvalue; :math:`\\lambda_{\\max}(A)`., Returns the largest eigenvalue of A.          Requires that A be symmetric., Returns constraints describing the domain of the node. (+18 more)

### Community 39 - "Community 39"
Cohesion: 0.05
Nodes (23): COPT, This file is the CVXPY QP extension of the Cardinal Optimizer, QP interface for the COPT solver, Returns bibtex citation for the solver.          Parameters         ----------, Returns the solution to the original problem given the inverse_data., Returns the result of the call to the solver.          Parameters         ------, constrain_cplex_infty(), CPLEX (+15 more)

### Community 40 - "Community 40"
Cohesion: 0.08
Nodes (19): cumsum, Copyright 2024 the CVXPY developers  Licensed under the Apache License, Version, Xor, Equivalent to `cp.cumsum(self, axis)`., Returns a string with information about the expression., str : The curvature of the expression., str : The log-log curvature of the expression., Is the expression affine? (+11 more)

### Community 41 - "Community 41"
Cohesion: 0.05
Nodes (24): norm(), norm2(), normNuc, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Sum of the singular values., Returns the nuclear norm (i.e. the sum of the singular values) of A., Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, Returns the (row, col) shape of the expression. (+16 more)

### Community 42 - "Community 42"
Cohesion: 0.06
Nodes (28): DictTensorView, The DictTensorView abstract class handles the dictionary aspect of the tensor re, Apply 'func' to A and b.         If 'func' is a parameter free function, then we, Adds the tensor a to b if they are both not none.         If a (b) is not None b, Returns element-wise addition of two tensors of the same type., Returns the type of the underlying tensor, Addition for dict-based tensors., Apply 'func' to each slice of the parameter representation. (+20 more)

### Community 43 - "Community 43"
Cohesion: 0.06
Nodes (10): Parameters         ----------         y : cvxpy.expressions.expression.Expressio, SuppFuncAtom, Return (A, b, K) so that         {x : x satisfies constraints}     can be writte, Return an atom representing              max{ cvxpy.vec(y) @ cvxpy.vec(x) : x in, Parse a ConeDims object, as returned from SCS's apply function.      Return a di, # TODO: implement, Given a list of CVXPY Constraint objects :math:`\\texttt{constraints}`     invol, scs_cone_selectors() (+2 more)

### Community 44 - "Community 44"
Cohesion: 0.05
Nodes (22): diag(), diag_mat, diag_vec, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Is the expression hermitian?, Is the expression a positive semidefinite matrix?, Is the expression a negative semidefinite matrix?, Convolve two vectors.          Parameters         ----------         arg_objs : (+14 more)

### Community 45 - "Community 45"
Cohesion: 0.06
Nodes (20): Atom, Copyright 2022, the CVXPY authors  Licensed under the Apache License, Version 2., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, # TODO: have to wrap derivative around scipy CSC sparse matrices, Returns constraints describing the domain of the node., Represents the von Neumann Entropy of the positive-definite matrix :math:`X,` (+12 more)

### Community 46 - "Community 46"
Cohesion: 0.07
Nodes (21): NDArrayInterface, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, MatrixInterface, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, An interface to convert constant values to the numpy matrix class., Convert an arbitrary value into a matrix of type self.target_matrix.          Ar, NDArrayInterface, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t (+13 more)

### Community 47 - "Community 47"
Cohesion: 0.06
Nodes (22): Dqcp2Dcp, _get_lazy_and_real_constraints(), Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Canonicalize arguments of an expression.          Like Canonicalization.canonica, Recursively canonicalize a constraint.          The DQCP grammar has expresions, Reduce DQCP problems to a parameterized DCP problem.      This reduction takes a, A problem is accepted if it is (a minimization) DQCP., Recursively canonicalize the objective and every constraint. (+14 more)

### Community 48 - "Community 48"
Cohesion: 0.05
Nodes (20): AffAtom, hstack(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Horizontal concatenation of an arbitrary number of Expressions.      Parameters, Horizontal concatenation, Stack the expressions horizontally.          Parameters         ----------, NegExpression, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t (+12 more)

### Community 49 - "Community 49"
Cohesion: 0.05
Nodes (23): Copyright 2018 Akshay Agrawal  Licensed under the Apache License, Version 2.0 (t, log_normcdf(), Copyright 2021 the CVXPY developers Licensed under the Apache License, Version 2, Elementwise log of the cumulative distribution function of a standard normal ran, loggamma(), Copyright 2021 the CVXPY developers Licensed under the Apache License, Version 2, Elementwise log of the gamma function.      Implementation has modest accuracy o, maximum (+15 more)

### Community 50 - "Community 50"
Cohesion: 0.06
Nodes (17): _is_const(), power(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Returns sign (is positive, is negative) of the expression., Returns bounds for power based on argument bounds., Is the atom log-log convex?, Is the atom log-log concave?, Is the expression constant? (+9 more)

### Community 51 - "Community 51"
Cohesion: 0.06
Nodes (18): geo_mean(), GeoMean, GeoMeanApprox, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Returns constraints describing the domain of the node., Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, Returns the (row, col) shape of the expression., Returns sign (is positive, is negative) of the expression. (+10 more)

### Community 52 - "Community 52"
Cohesion: 0.06
Nodes (20): log_det_canon(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Reduces the atom to an affine expression and list of constraints.      Creates t, Copyright 2025 CVXPY developers  Licensed under the Apache License, Version 2.0, log1p, Copyright 2013 Steven Diamond, Eric Chu  Licensed under the Apache License, Vers, Elementwise :math:`\\log (1 + x)`., Returns the elementwise natural log of x+1. (+12 more)

### Community 53 - "Community 53"
Cohesion: 0.07
Nodes (19): CVXOPT, dims_to_solver_dict(), Copyright 2013 Steven Diamond, 2017 Robin Verschueren  Licensed under the Apache, Returns the solution to the original problem given the inverse_data., Convert constraints and cost to solver-specific format, Check if A has redundant rows. If it does, remove redundant constraints, Returns the KKT solver selected by the user.          Removes the KKT solver fro, Returns bibtex citation for the solver.          Parameters         ---------- (+11 more)

### Community 54 - "Community 54"
Cohesion: 0.06
Nodes (17): cos, Copyright 2025 CVXPY Developers  Licensed under the Apache License, Version 2.0, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Returns constraints describing the domain of the node., Returns the gradient of the node., Elementwise :math:`\\sin x`., Returns the elementwise sine of x. (+9 more)

### Community 55 - "Community 55"
Cohesion: 0.06
Nodes (17): conv, convolve, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Convolve two vectors.          Parameters         ----------         arg_objs :, 1D discrete convolution of two vectors.      The discrete convolution :math:`c`, Convolve the two values. (+9 more)

### Community 56 - "Community 56"
Cohesion: 0.07
Nodes (35): convert(), cvxopt2dense(), dense2cvxopt(), from_1D_to_2D(), from_2D_to_1D(), get_cvxopt_dense_intf(), get_cvxopt_sparse_intf(), index() (+27 more)

### Community 57 - "Community 57"
Cohesion: 0.07
Nodes (19): partial_transpose(), Copyright 2022, the CVXPY authors.  Licensed under the Apache License, Version 2, Helper function for partial transpose.      Parameters     ----------     expr :, Assumes :math:`\\texttt{expr} = X_1 \\otimes ... \\otimes X_n` is a 2D Kronecker, _term(), hermitian_wrap, nonneg_wrap, nonpos_wrap (+11 more)

### Community 58 - "Community 58"
Cohesion: 0.06
Nodes (25): convert_conv(), convert_diag_mat(), convert_div(), convert_hstack(), convert_index(), convert_quad_form(), convert_rel_entr(), convert_reshape() (+17 more)

### Community 59 - "Community 59"
Cohesion: 0.06
Nodes (11): multiply, Copyright 2025 CVXPY developers  Licensed under the Apache License, Version 2.0, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Equivalent to `cp.mean(self, axis, keepdims)`., Equivalent to `cp.ptp(self, axis, keepdims)`., Get the label of the expression., Set the label of the expression., Delete the label of the expression. (+3 more)

### Community 60 - "Community 60"
Cohesion: 0.06
Nodes (18): cvar(), Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, r"""The conditional value at risk (CVaR) of a random variable represented by, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Gives the (sub/super)gradient of the atom w.r.t. a column argument.          Mat, Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx? (+10 more)

### Community 61 - "Community 61"
Cohesion: 0.06
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 62 - "Community 62"
Cohesion: 0.06
Nodes (22): ABC, get_nd_matmul_dims(), get_nd_rmul_dims(), is_batch_varying(), Copyright 2025, the CVXPY authors.  Licensed under the Apache License, Version 2, Compute dimensions for ND rmul X @ C.      Parameters     ----------     var_sha, Check if constant has batch dimensions with product > 1.      A batch-varying co, A TensorView represents the tensors for A and b, which are of shape     rows x v (+14 more)

### Community 63 - "Community 63"
Cohesion: 0.07
Nodes (18): moveaxis(), permute_dims(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Create a new variable equal to the argument transposed.          Parameters, Permute the dimensions of the expression.      Alias for transpose with specifie, Swap two axes of the expression.      Parameters     ----------     expr : AffAt, Move axes of the expression to new positions.      Parameters     ----------, Transpose an expression.      For an n-D expression, if axes are given, the orde (+10 more)

### Community 64 - "Community 64"
Cohesion: 0.08
Nodes (15): Symbolic form of QuadForm when quadratic matrix is not known (yet).      Paramet, SymbolicQuadForm, Copyright 2017 Robin Verschueren  Licensed under the Apache License, Version 2.0, Copyright 2017 Robin Verschueren  Licensed under the Apache License, Version 2.0, _compute_block_indices(), quad_over_lin_canon(), Copyright 2017 Robin Verschueren  Licensed under the Apache License, Version 2.0, Compute block indices for reducing along specified axes (Fortran order).      Pa (+7 more)

### Community 65 - "Community 65"
Cohesion: 0.06
Nodes (12): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Equality, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, A constraint of the form :math:`x = y`., Returns a string with information about the constraint., int : The shape of the constrained expression., int : The size of the constrained expression., An equality constraint is DCP if its argument is affine. (+4 more)

### Community 66 - "Community 66"
Cohesion: 0.10
Nodes (20): DeprecationWarning, _cast_other(), _pow_const_base(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Is the expression constant?, Casts the second argument of a binary operator as an Expression.      Args:, Is the expression quadratic?, Does the affine head of the expression contain a quadratic term?          The af (+12 more)

### Community 67 - "Community 67"
Cohesion: 0.07
Nodes (13): Copyright 2025 CVXPY developers  Licensed under the Apache License, Version 2.0, exp, Elementwise exponential function.      Computes the elementwise exponential of t, Initialize the expression., Is this Expression, X, a real matrix that satisfies X + X.T == 0?, int : The number of dimensions in the expression's shape., Is the expression a column or row vector?, Expression : The transpose of the expression. (+5 more)

### Community 68 - "Community 68"
Cohesion: 0.09
Nodes (29): format_slice(), index_to_slice(), is_single_index(), is_special_slice(), none_to_empty(), pprint_sequence(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Convert everything but None to an int. (+21 more)

### Community 69 - "Community 69"
Cohesion: 0.08
Nodes (12): gmatmul, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Is the atom log-log convex?, Is the atom log-log concave?, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, r"""Geometric matrix multiplication; :math:`A \mathbin{\diamond} X`.      For :m, Geometric matrix multiplication. (+4 more)

### Community 70 - "Community 70"
Cohesion: 0.09
Nodes (19): CPLEX, get_status(), _handle_solve_status(), hide_solver_output(), Copyright 2013 Steven Diamond, 2017 Robin Verschueren  Licensed under the Apache, Map CPLEX status to CPXPY status., # NOTE: dfeas is always false for a MIP., An interface for the CPLEX solver. (+11 more)

### Community 71 - "Community 71"
Cohesion: 0.09
Nodes (10): conj, Equivalent to `cp.max(self, axis, keepdims)`., Equivalent to `cp.prod(self, axis, keepdims)`., str: The sign of the expression., Is the expression all zero?, Is the expression positive?, Is the expression negative?, int : The number of entries in the expression. (+2 more)

### Community 72 - "Community 72"
Cohesion: 0.07
Nodes (15): C_problem, Copyright 2025, the CVXPY developers  Licensed under the Apache License, Version, Evaluate the constraint Jacobian and return its nonzero values.          The val, Return the sparsity pattern (row, col) of the lower-triangular Lagrangian Hessia, Evaluate the lower-triangular Lagrangian Hessian and return its nonzero values., Wrapper around C problem struct for CVXPY problems., Create a C problem from a CVXPY problem.          Args:             cvxpy_proble, Update parameter values in the C DAG.          Sparsity structures (Jacobian/Hes (+7 more)

### Community 73 - "Community 73"
Cohesion: 0.07
Nodes (13): gen_lambda_max, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Maximum generalized eigenvalue; :math:`\\lambda_{\\max}(A, B)`., Returns the largest generalized eigenvalue corresponding to A and B.          Re, Returns constraints describing the domain of the node., Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix (+5 more)

### Community 74 - "Community 74"
Cohesion: 0.10
Nodes (16): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Represents a parameterized cone program      minimize   q'x  + d + [(1/2)x'Px], Is the problem mixed-integer?, Returns A, b after applying parameters (and reshaping).          Args:, Multiplies by Jacobian of parameter mapping.          Assumes delA is sparse., # TODO: make this faster by intelligently operating on the, Adjoint of split_solution., Construct matrices for linear cone problems.      Linear cone problems are assum (+8 more)

### Community 75 - "Community 75"
Cohesion: 0.08
Nodes (12): condition_number, Copyright 2022, the CVXPY authors  Licensed under the Apache License, Version 2., Condition Number; :math:`\\lambda_{\\max}(A) / \\lambda_{\\min}(A)`.         Req, Returns the condition number of A.          Requires that A be a Positive Semide, Returns constraints describing the domain of the node., Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, Verify that the argument A is a square matrix., Returns the (row, col) shape of the expression. (+4 more)

### Community 76 - "Community 76"
Cohesion: 0.09
Nodes (11): dotsort, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Returns None, W is stored as an argument., Is the expression piecewise linear?, r""" Computes :math:`\langle sort\left(vec(X)\right), sort\left(vec(W)\right) \r, Returns the inner product of the sorted values of vec(X) and the sorted (+3 more)

### Community 77 - "Community 77"
Cohesion: 0.08
Nodes (11): eye_minus_inv, Copyright 2018 Akshay Agrawal  Licensed under the Apache License, Version 2.0 (t, Is the atom log-log convex?, Is the atom log-log concave?, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, r"""The resolvent of a positive matrix, :math:`(sI - X)^{-1}`.      For an eleme, r"""The unity resolvent of a positive matrix, :math:`(I - X)^{-1}`.      For an (+3 more)

### Community 78 - "Community 78"
Cohesion: 0.08
Nodes (11): diff_pos(), one_minus_pos, Copyright 2018 Akshay Agrawal  Licensed under the Apache License, Version 2.0 (t, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, r"""The difference :math:`x - y` with domain `\{x, y : x > y > 0\}`.      This a, r"""The difference :math:`1 - x` with domain `\{x : 0 < x < 1\}`.      This atom, Returns the (row, col) shape of the expression. (+3 more)

### Community 79 - "Community 79"
Cohesion: 0.08
Nodes (10): pf_eigenvalue, Copyright 2018 Akshay Agrawal  Licensed under the Apache License, Version 2.0 (t, The Perron-Frobenius eigenvalue of a positive matrix.      For an elementwise po, Verify that the argument is a square matrix., Returns the (row, col) shape of the expression., Returns sign (is positive, is negative) of the expression., Is the atom log-log convex?, Is the atom log-log concave? (+2 more)

### Community 80 - "Community 80"
Cohesion: 0.12
Nodes (12): Splits the solution into individual variables., Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, LinOp, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, CoeffExtractor, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Extract quadratic coefficients for block-structured quad forms.          Each ou, Extract P (quadratic) and q (linear + constant) from a quadratic objective. (+4 more)

### Community 81 - "Community 81"
Cohesion: 0.08
Nodes (11): Copyright 2022, the CVXPY authors  Licensed under the Apache License, Version 2., Returns constraints describing the domain of the node., r"""     :math:`\mathrm{tr}\left(X^{-1} \right),`     where :math:`X` is positiv, Returns the trinv of positive definite matrix X.          For positive definite, Verify that the argument is a square matrix., Returns the (row, col) shape of the expression., Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx? (+3 more)

### Community 82 - "Community 82"
Cohesion: 0.08
Nodes (10): Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, ceil, Returns sign (is positive, is negative) of the expression., Is the atom log-log convex?, Is the atom log-log concave?, Is the atom quasiconvex?, Is the atom quasiconcave?, Is the composition non-decreasing in argument idx? (+2 more)

### Community 83 - "Community 83"
Cohesion: 0.08
Nodes (2): indicator, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 84 - "Community 84"
Cohesion: 0.09
Nodes (11): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Indexing using logical indexing or a list of indices.      Parameters     ------, Returns bounds for special indexed expression., Is the atom log-log convex?, Is the atom log-log concave?, String representation of the special index expression., Returns the index/slice into the given value., Returns the shape of the index expression. (+3 more)

### Community 85 - "Community 85"
Cohesion: 0.11
Nodes (20): CvxPyDomainError, decomp_quad(), quad_form(), Copyright 2013 Steven Diamond, 2017 Robin Verschueren  Licensed under the Apache, Compute a matrix decomposition.      Compute scale, M1, M2 such that P = scale *, # TODO: allow indefinite quad_form, Alias for :math:`x^T P x`.      Parameters     ----------     x : vector argumen, Exception (+12 more)

### Community 86 - "Community 86"
Cohesion: 0.09
Nodes (10): Copyright 2022, the CVXPY authors  Licensed under the Apache License, Version 2., Elementwise :math:`{x}*e^{x}`., Returns sign (is positive, is negative) of the expression., Is the atom log-log convex?, Is the atom log-log concave?, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix (+2 more)

### Community 87 - "Community 87"
Cohesion: 0.10
Nodes (9): kron, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Kronecker product of two matrices.          Parameters         ----------, Kronecker product of the two values., Checks that at least one argument is constant and both arguments are 2-d., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Check a *sufficient condition* that the expression is PSD,         by checking i (+1 more)

### Community 88 - "Community 88"
Cohesion: 0.09
Nodes (10): cummax, Copyright 2017 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Is the composition non-increasing in argument idx?, Returns the largest entry in x., The same as the input., Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, Gives the (sub/super)gradient of the atom w.r.t. a column argument.          Mat, Returns sign (is positive, is negative) of the expression. (+2 more)

### Community 89 - "Community 89"
Cohesion: 0.09
Nodes (10): dist_ratio, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, norm(x - a)_2 / norm(x - b)_2, with norm(x - a)_2 <= norm(x - b).      `a` and `, Returns the distance ratio., Returns the (row, col) shape of the expression., Returns sign (is positive, is negative) of the expression., Is the atom quasiconvex?, Is the atom quasiconvex? (+2 more)

### Community 90 - "Community 90"
Cohesion: 0.09
Nodes (10): length, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Length of a vector (index of last nonzero, ones-based)., Returns the length of x., Returns the (row, col) shape of the expression., Returns sign (is positive, is negative) of the expression., Is the atom quasiconvex?, Is the atom quasiconvex? (+2 more)

### Community 91 - "Community 91"
Cohesion: 0.09
Nodes (9): log_det, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Returns constraints describing the domain of the node., Returns the logdet of PSD matrix A.          For PSD matrix A, this is the sum o, Returns the (row, col) shape of the expression., Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx? (+1 more)

### Community 92 - "Community 92"
Cohesion: 0.09
Nodes (9): quantum_rel_entr, Copyright 2023, the CVXPY authors  Licensed under the Apache License, Version 2., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, Returns constraints describing the domain of the node., An approximation of the quantum relative entropy between systems with (possibly, Returns sign (is positive, is negative) of the expression. (+1 more)

### Community 93 - "Community 93"
Cohesion: 0.09
Nodes (10): Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Sign of an expression (-1 for x <= 0, +1 for x > 0)., Returns the sign of x., Returns the (row, col) shape of the expression., Returns sign (is positive, is negative) of the expression., Is the atom quasiconvex?, Is the atom quasiconvex?, Is the composition non-decreasing in argument idx? (+2 more)

### Community 94 - "Community 94"
Cohesion: 0.09
Nodes (9): Copyright 2025 CVXPY developers  Licensed under the Apache License, Version 2.0, Copyright 2021 The CVXPY Developers  Licensed under the Apache License, Version, :math:`x\\log(x/y)`      For disambiguation between rel_entr and kl_div, see htt, Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, Returns constraints describing the domain of the node. (+1 more)

### Community 95 - "Community 95"
Cohesion: 0.10
Nodes (13): dims_to_solver_cones(), MOREAU, MoreauSolution, Copyright 2025, the CVXPY Authors  Licensed under the Apache License, Version 2., The name of the solver., Moreau supports quadratic objective with conic constraints., Returns the solution to the original problem given the inverse_data., Handle user-specified solver options.          Parameters         ---------- (+5 more)

### Community 96 - "Community 96"
Cohesion: 0.10
Nodes (9): log_sum_exp, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, :math:`\\log\\sum_i e^{x_i}`, Evaluates e^x elementwise, sums, and takes the log., Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, Gives the (sub/super)gradient of the atom w.r.t. a column argument.          Mat, Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx? (+1 more)

### Community 97 - "Community 97"
Cohesion: 0.10
Nodes (5): Cone, PowConeND, Represents a collection of N-dimensional power cone constraints     that is *mat, A power cone constraint is DCP if each argument is affine., Implements the dual cone of PowConeND See Pg 85         of the MOSEK modelling c

### Community 98 - "Community 98"
Cohesion: 0.11
Nodes (10): Is the expression nonnegative?, Is the expression nonpositive?, Is the Leaf imaginary?, Is the Leaf complex valued?, Is the expression symmetric?, Is the expression a Hermitian matrix?, Compute the attributes of the constant related to complex/real, sign., Determine whether the constant is symmetric/Hermitian. (+2 more)

### Community 99 - "Community 99"
Cohesion: 0.10
Nodes (7): Inequality, A constraint of the form :math:`x \\leq y`.      Dual variables to these constra, int : The shape of the constrained expression., int : The size of the constrained expression., A non-positive constraint is DCP if its argument is convex., An Inequality constraint is DNLP if its         argument is linearizable convex., The residual of the constraint.          Returns         ---------         NumPy

### Community 100 - "Community 100"
Cohesion: 0.10
Nodes (9): normcdf, Copyright 2025 CVXPY Developers  Licensed under the Apache License, Version 2.0, Elementwise :math:`\\Phi(x)` (standard normal cumulative distribution function)., Returns the elementwise standard normal cumulative distribution function of x., Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Returns constraints describing the domain of the node. (+1 more)

### Community 101 - "Community 101"
Cohesion: 0.15
Nodes (6): BaseMatrixInterface, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Add the block to a slice of the matrix.          Args:             matrix: The m, Formats the block for block_add.          Args:             matrix: The matrix t, An interface between constants' internal values     and the target matrix used i, Convert an arbitrary value into a matrix of type self.target_matrix.          Ar

### Community 102 - "Community 102"
Cohesion: 0.11
Nodes (8): perspective, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Returns the (row, col) shape of the expression., Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, r"""Implements the perspective transform of a convex or concave scalar     expre, Compute the perspective sf(x/s) numerically.

### Community 103 - "Community 103"
Cohesion: 0.11
Nodes (8): kl_div, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, :math:`x\\log(x/y) - x + y`      For disambiguation between kl_div and rel_entr,, Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, Returns constraints describing the domain of the node.

### Community 104 - "Community 104"
Cohesion: 0.14
Nodes (18): dense_ldl_decomp(), _dense_ldl_factor(), gershgorin_psd_check(), is_diagonal(), is_psd_within_tol(), onb_for_orthogonal_complement(), orth(), _qdldl_residual_norm() (+10 more)

### Community 105 - "Community 105"
Cohesion: 0.11
Nodes (9): imag, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Extracts the imaginary part of an expression., Imaginary part of an expression, Returns the shape of the expression., Is the expression imaginary?, Is the expression complex valued?, Is the expression symmetric? (+1 more)

### Community 106 - "Community 106"
Cohesion: 0.12
Nodes (10): dims_to_solver_dict(), Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Returns the solution to the original problem given the inverse_data., r"""         CVXPY represents cone programs as             (P) min_x { c^T x : A, Returns bibtex citation for the solver.          Parameters         ----------, An interface for the SDPA solver., The name of the solver., Can SDPA solve the problem? (+2 more)

### Community 107 - "Community 107"
Cohesion: 0.11
Nodes (8): abs, Elementwise absolute value.      Computes the elementwise absolute value of the, Returns sign (is positive, is negative) of the expression., Returns bounds for absolute value based on argument bounds., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Is the atom piecewise linear?, Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix

### Community 108 - "Community 108"
Cohesion: 0.12
Nodes (7): _is_boolean_arg(), LogicExpression, _NaryLogicExpression, Shared base for n-ary logic atoms (And, Or, Xor).      Subclasses set ``OP_NAME`, Check if an argument is a valid boolean logic input., Base class for boolean logic atoms (Not, And, Or, Xor)., Result is boolean (0 or 1), so nonneg.

### Community 109 - "Community 109"
Cohesion: 0.11
Nodes (8): logistic, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, :math:`\\log(1 + e^{x})`      This is a special case of log(sum(exp)) that is ev, Evaluates e^x elementwise, adds 1, and takes the log., Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix

### Community 110 - "Community 110"
Cohesion: 0.11
Nodes (8): Elementwise :math:`\\tan x`., Returns the elementwise tangent of x., Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Returns constraints describing the domain of the node., Returns the gradient of the node., tan

### Community 111 - "Community 111"
Cohesion: 0.11
Nodes (17): broadcast_to(), concatenate(), conv(), copy_constr(), diag_mat(), diag_vec(), div_expr(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t (+9 more)

### Community 112 - "Community 112"
Cohesion: 0.11
Nodes (17): add_bounds(), broadcast_bounds(), coords_equal(), exp_bounds(), index_bounds(), log_bounds(), maximum_bounds(), Copyright 2026 The CVXPY Developers  Licensed under the Apache License, Version (+9 more)

### Community 113 - "Community 113"
Cohesion: 0.18
Nodes (17): _compute_size_by_dict(), find_contraction(), _flop_count(), greedy_path(), optimal_path(), parse_einsum_input(), _parse_possible_contraction(), Copied from numpy._core.einsumfunc from numpy 2.4.0. Utilities for the einsum at (+9 more)

### Community 114 - "Community 114"
Cohesion: 0.13
Nodes (6): FiniteSet, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Choose between two constraining methodologies, use ``ineq_form=False`` while, The residual of the constraint.          Returns         -------         float, Constrain each entry of an Expression to take a value in a given set of real num, A FiniteSet constraint is DCP if the constrained expression is affine.

### Community 115 - "Community 115"
Cohesion: 0.12
Nodes (7): Elementwise :math:`\\sinh x`., Returns the elementwise sinh of x., Returns sign (is positive, is negative) of the expression., Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Returns constraints describing the domain of the node., sinh

### Community 116 - "Community 116"
Cohesion: 0.16
Nodes (11): add(), div_canon(), join(), multiply_like_canon(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Canonicalize functions like multiplication., Canonicalize division by a (possibly complex) constant or parameter.      For a, Canonicalize linear functions that are separable        in real and imaginary pa (+3 more)

### Community 117 - "Community 117"
Cohesion: 0.15
Nodes (11): build_param_dict(), build_var_dict(), chain_add(), normalize_shape(), Copyright 2025, the CVXPY developers  Licensed under the Apache License, Version, Normalize shape to 2D (d1, d2) for the C engine., Convert a value to a dense float64 numpy array., Combine children with a balanced binary tree of adds.      Tree depth is ceil(lo (+3 more)

### Community 118 - "Community 118"
Cohesion: 0.13
Nodes (5): Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Return the t-level sublevel set for `expr`.      Returned as a constraint phi_t(, Return the t-level superlevel set for `expr`.      Returned as a constraint phi_, sublevel(), superlevel()

### Community 119 - "Community 119"
Cohesion: 0.15
Nodes (7): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Wrapper on vstack to ensure list argument., Vertical concatenation, Is the atom log-log convex?, Is the atom log-log concave?, Stack the expressions vertically.          Parameters         ----------, vstack()

### Community 120 - "Community 120"
Cohesion: 0.14
Nodes (7): Convert to stacked sparse matrix (for compatibility)., Convert to COO format (stacked) for compatibility., Convert to CSR format (stacked) for compatibility., Convert to CSC format (stacked) for compatibility., Convert to dense array (stacked) for compatibility., Convert from stacked sparse matrix., Create tensor for constant data.          Returns {Constant.ID: {Constant.ID: te

### Community 121 - "Community 121"
Cohesion: 0.29
Nodes (5): _expr_cone_atoms(), make_problem_form(), _objective_cone_atoms(), pick_default_solver(), ProblemForm

### Community 122 - "Community 122"
Cohesion: 0.19
Nodes (5): CLARABEL, COSMO, Copyright 2022, the CVXPY Authors  Licensed under the Apache License, Version 2., Returns bibtex citation for the solver.          Parameters         ----------, An interface for the COSMO solver.

### Community 123 - "Community 123"
Cohesion: 0.24
Nodes (11): Dnlp2Smooth, Reduce a disciplined nonlinear program to an equivalent smooth program      This, _build_nlp_chain(), Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Solve an NLP problem using the DNLP reduction chain.      Parameters     -------, Build the NLP reduction chain and return (SolvingChain, kwargs).      Solver sel, Construct an initial point for variables without a user-specified value.      Us, Generate a random initial point for DNLP problems.      A variable is initialize (+3 more)

### Community 124 - "Community 124"
Cohesion: 0.18
Nodes (6): constrain_gurobi_infty(), GUROBI, Limit values of vector v between +/- infinity as     defined in the Gurobi packa, Returns bibtex citation for the solver.          Parameters         ----------, QP interface for the Gurobi solver, Construct QP problem data stored in a dictionary.         The QP has the followi

### Community 125 - "Community 125"
Cohesion: 0.17
Nodes (6): Select 'rows' from tensor. If there are multiple parameters 'p',         we must, Apply 'func' across all variables and parameter slices.         For the stacked-, Promote view by repeating along axis 0 (rows)., Broadcast view by calling np.broadcast_to on the rows and indexing the view., Given (A, b) in view, return the sum of the representation         on the row ax, Diagonal vector to matrix. Given (A, b) with n rows in view, add rows of zeros s

### Community 126 - "Community 126"
Cohesion: 0.20
Nodes (12): create_geq(), create_leq(), get_constr_expr(), neg_expr(), Add linear operators.      Parameters     ----------     operators : list, Negate an operator.      Parameters     ----------     operator : LinOp, Difference of linear operators.      Parameters     ----------     lh_op : LinOp, Returns the operator in the constraint. (+4 more)

### Community 127 - "Community 127"
Cohesion: 0.18
Nodes (4): Quadratic interface for the FICO Xpress solver, Returns a new problem and data for inverting the new solution.          Returns, Returns bibtex citation for the solver.          Parameters         ----------, XPRESS

### Community 128 - "Community 128"
Cohesion: 0.20
Nodes (12): matmul_bounds(), mul_bounds(), Return unbounded interval (-inf, inf) for given shape.      Parameters     -----, Bounds for elementwise multiplication: x * y.      Uses interval arithmetic: the, Element-wise maximum, handling sparse matrices.      Uses scipy sparse's .maximu, Element-wise minimum, handling sparse matrices.      Uses scipy sparse's .minimu, Bounds for matrix multiplication: x @ y.      When one operand is a point (lb ==, Refine bounds based on sign information.      Parameters     ----------     lb, (+4 more)

### Community 129 - "Community 129"
Cohesion: 0.20
Nodes (1): concatenate()

### Community 130 - "Community 130"
Cohesion: 0.31
Nodes (10): _bisect(), _find_bisection_interval(), _infeasible(), _lower_problem(), Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Bisect `problem` on the parameter `t`., Bisection on a one-parameter family of DCP problems.      Bisects on a one-param, Evaluates lazy constraints. (+2 more)

### Community 131 - "Community 131"
Cohesion: 0.20
Nodes (9): mul_shapes(), mul_shapes_promote(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Give the shape resulting from multiplying two shapes.      Adheres the semantics, Compute the size of a given shape by multiplying the sizes of each axis.      Th, Give the shape resulting from summing a list of shapes.      Summation semantics, Promotes shapes as necessary and returns promoted shape of product.      If lh_s, size_from_shape() (+1 more)

### Community 132 - "Community 132"
Cohesion: 0.36
Nodes (8): _collect_x_duals_into_array(), _decompose_soc_single(), _get_all_tree_cone_ids(), _get_flat_dual(), _get_original_dim(), _get_root_t_dual(), _reconstruct_soc_dual(), _to_scalar_shape()

### Community 133 - "Community 133"
Cohesion: 0.24
Nodes (3): OSQP, QP interface for the OSQP solver, Returns bibtex citation for the solver.          Parameters         ----------

### Community 134 - "Community 134"
Cohesion: 0.22
Nodes (4): PIQP, Copyright 2023, the CVXPY Authors  Licensed under the Apache License, Version 2., Returns bibtex citation for the solver.          Parameters         ----------, QP interface for the PIQP solver

### Community 135 - "Community 135"
Cohesion: 0.22
Nodes (4): PROXQP, Copyright 2022, the CVXPY Authors  Licensed under the Apache License, Version 2., Returns bibtex citation for the solver.          Parameters         ----------, QP interface for the PROXQP solver

### Community 136 - "Community 136"
Cohesion: 0.22
Nodes (4): QPALM, Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Returns bibtex citation for the solver.          Parameters         ----------, QP interface for the QPALM solver

### Community 137 - "Community 137"
Cohesion: 0.20
Nodes (9): dpp_scope(), dpp_scope_active(), quad_form_dpp_scope(), quad_form_dpp_scope_active(), Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Context manager for DPP curvature analysis      When this scope is active, param, Returns True if a `dpp_scope` is active., Context manager for quad_form DPP analysis with QP solvers.      When active, Qu (+1 more)

### Community 138 - "Community 138"
Cohesion: 0.28
Nodes (7): pnorm_approx_canon(), pnorm_exact_canon(), _pnorm_p2_canon(), Copyright 2025 CVXPY developers  Licensed under the Apache License, Version 2.0, Handle p == 2 case via SOC directly (shared by exact and approx)., Canonicalize Pnorm using power cone constraints., Canonicalize PnormApprox using SOC constraints via rational approximation.

### Community 139 - "Community 139"
Cohesion: 0.28
Nodes (8): convert_expr(), convert_matmul(), convert_multiply(), Copyright 2025, the CVXPY developers  Licensed under the Apache License, Version, # TODO: maybe multiply doesn't need parameter dict special case, Convert matrix multiplication A @ f(x), f(x) @ A, or X @ Y.      Follows numpy's, Convert elementwise multiplication., Convert a CVXPY expression to a C diff engine expression.      Args:         exp

### Community 140 - "Community 140"
Cohesion: 0.22
Nodes (5): DNLPError, DQCPError, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Error thrown for DNLP violations., Error thrown for DQCP violations.

### Community 141 - "Community 141"
Cohesion: 0.22
Nodes (4): DefaultDeepCopyContextManager, Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Called by copy.deepcopy()         Creates an independent copy of the object whil, override custom __deepcopy__ implementation and call copy.deepcopy's implementat

### Community 142 - "Community 142"
Cohesion: 0.32
Nodes (4): Is the expression a negative semidefinite matrix?, Is the composition non-decreasing in argument idx?, Is the composition non-increasing in argument idx?, Is the expression a positive semidefinite matrix?

### Community 143 - "Community 143"
Cohesion: 0.29
Nodes (7): batched_upper_tri_to_full(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Reshapes a vector into an upper triangular matrix in     row-major order. The st, Returns a coefficient matrix A that creates a symmetric matrix when     multipli, Returns a coefficient matrix that maps a vector of batch_size * tri entries, upper_tri_to_full(), vec_to_upper_tri()

### Community 144 - "Community 144"
Cohesion: 0.32
Nodes (7): mean(), Copyright 2013 CVXPY Developers  Licensed under the Apache License, Version 2.0, Returns the mean of x., Returns the standard deviation of x.      `ddof` is the quantity to use in the B, Returns the variance of x.      `ddof` is the quantity to use in the Bessel corr, std(), var()

### Community 145 - "Community 145"
Cohesion: 0.25
Nodes (4): Reshape constant data from column format to the required shape for operations th, Reshape constant data from column format to matrix format.          Dispatches t, Reshape non-parametric constant data from column to matrix format.          For, Reshape parametric constant data from column to matrix format.          For para

### Community 146 - "Community 146"
Cohesion: 0.25
Nodes (6): is_param_affine(), is_param_free(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Returns itself as a parameter., Returns true if expression is parameters-affine (and variable-free), Returns true if expression is not parametrized.

### Community 147 - "Community 147"
Cohesion: 0.25
Nodes (3): ConeDims, String representation., Summary of cone dimensions present in constraints.      Constraints must be form

### Community 148 - "Community 148"
Cohesion: 0.29
Nodes (4): Is the expression smooth?, Is the expression convex after linearizing all smooth subexpressions?, Is the expression concave after linearizing all smooth subexpressions?, The expression is smooth representable.

### Community 149 - "Community 149"
Cohesion: 0.25
Nodes (8): create_eq(), create_param(), create_var(), get_id(), Returns a new id and updates the id counter.      Returns     -------     int, Creates a new internal variable.      Parameters     ----------     shape : tupl, Creates an internal equality constraint.      Parameters     ----------     lh_o, Wraps a parameter.      Parameters     ----------     shape : tuple         The

### Community 150 - "Community 150"
Cohesion: 0.25
Nodes (5): get_dual_values(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Stacks the values of the given variables.      Parameters     ----------     var, Gets the values of the dual variables.      Parameters     ----------     result, stack_vals()

### Community 151 - "Community 151"
Cohesion: 0.25
Nodes (8): _all_isinf(), _all_zero_or_inf(), _any_isnan(), get_expr_bounds_if_supported(), Check if all values are 0 or inf, sparse-aware (O(nnz) for sparse)., Check if all values are inf, sparse-aware (O(nnz) for sparse)., Get bounds from expression for use on auxiliary variables.      Returns a [lb, u, Check if any values are NaN, sparse-aware (O(nnz) for sparse).

### Community 152 - "Community 152"
Cohesion: 0.29
Nodes (5): power_approx_canon(), power_exact_canon(), Copyright 2025 CVXPY developers  Licensed under the Apache License, Version 2.0, Canonicalize Power using power cone constraints., Canonicalize PowerApprox using SOC constraints via rational approximation.

### Community 153 - "Community 153"
Cohesion: 0.33
Nodes (3): EliminatePwl, Copyright 2017 Robin Verschueren  Licensed under the Apache License, Version 2.0, Eliminates piecewise linear atoms.

### Community 154 - "Community 154"
Cohesion: 0.38
Nodes (4): _get_unsupported_cone_message(), _has_unsupported_cones(), Copyright 2017 Robin Verschueren  Licensed under the Apache License, Version 2.0, Get a descriptive message about unsupported cones.

### Community 155 - "Community 155"
Cohesion: 0.29
Nodes (5): compute_once(), lazyprop(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Wraps a property so it is lazily evaluated., Computes an instance method caches the result.      A result is stored for each

### Community 156 - "Community 156"
Cohesion: 0.33
Nodes (1): Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th

### Community 157 - "Community 157"
Cohesion: 0.40
Nodes (3): finite_set_canon(), get_exprval_in_vec_func(), Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th

### Community 158 - "Community 158"
Cohesion: 0.33
Nodes (6): check_param_val(), create_const(), Wrapper on accessing a parameter.      Parameters     ----------     param : Par, Replaces parameters with constant nodes.      Parameters     ----------     expr, Wraps a constant.      Parameters     ----------     value : scalar, NumPy matri, replace_params_with_consts()

### Community 159 - "Community 159"
Cohesion: 0.40
Nodes (5): compress_matrix(), get_row_nnz(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Return the number of nonzeros in row., Compresses A and b by eliminating redundant rows.      Identifies rows that are

### Community 160 - "Community 160"
Cohesion: 0.40
Nodes (5): kkt_ldl(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, The meanings of arguments in this function are identical to those of the     fun, Returns a function handle "factor", which conforms to the CVXOPT     custom KKT, setup_ldl_factor()

### Community 161 - "Community 161"
Cohesion: 0.33
Nodes (6): abs_bounds(), max_reduction_bounds(), norm_inf_bounds(), Bounds for elementwise absolute value: |x|.      Parameters     ----------     l, Bounds for max reduction: max(x, axis=axis).      Parameters     ----------, Bounds for infinity-norm: max(|x|).      Parameters     ----------     lb, ub :

### Community 162 - "Community 162"
Cohesion: 0.33
Nodes (6): norm1_bounds(), Sum a sparse array, handling keepdims which scipy doesn't support., Bounds for sum reduction.      Parameters     ----------     lb, ub : array-like, Bounds for 1-norm: sum(|x|).      Parameters     ----------     lb, ub : np.ndar, _sparse_sum(), sum_bounds()

### Community 163 - "Community 163"
Cohesion: 0.33
Nodes (5): constant_grad(), error_grad(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Returns the gradient of constant terms in an expression.      Matrix expressions, Returns a gradient of all None.      Args:         expr: An expression.      Ret

### Community 164 - "Community 164"
Cohesion: 0.40
Nodes (5): _is_internal_frame(), Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Return True if *filename* belongs to cvxpy internals (not tests)., Issue a warning that appears to originate from user code.      Walks up the call, warn()

### Community 165 - "Community 165"
Cohesion: 0.40
Nodes (3): normalize_axis(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Normalize an axis argument to a canonical form.      - Negative indices become p

### Community 166 - "Community 166"
Cohesion: 0.40
Nodes (3): huber_perspective_canon(), Copyright 2025 CVXPY developers  Licensed under the Apache License, Version 2.0, Canonicalize the three-argument perspective Huber atom.      Uses the reparametr

### Community 167 - "Community 167"
Cohesion: 0.40
Nodes (2): Checks whether the constraint is DCP.          Returns         -------         b, Checks whether the constraint is DGP.          Returns         -------         b

### Community 168 - "Community 168"
Cohesion: 0.40
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 169 - "Community 169"
Cohesion: 0.40
Nodes (4): mul_sign(), Give the sign resulting from summing a list of expressions.      Args:         s, Give the sign resulting from multiplying two expressions.      Args:         lh_, sum_signs()

### Community 170 - "Community 170"
Cohesion: 0.50
Nodes (3): diff(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Computes kth order differences along the specified axis.      Takes in an array

### Community 171 - "Community 171"
Cohesion: 0.50
Nodes (2): Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix, Gives the (sub/super)gradient of the atom w.r.t. a column argument.          Mat

### Community 172 - "Community 172"
Cohesion: 0.50
Nodes (3): harmonic_mean(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, The harmonic mean of ``x``.      Parameters     ----------     x : Expression or

### Community 173 - "Community 173"
Cohesion: 0.50
Nodes (3): inv_prod(), Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, The reciprocal of a product of the entries of a vector ``x``.      Parameters

### Community 174 - "Community 174"
Cohesion: 0.50
Nodes (3): mixed_norm(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Lp,q norm; :math:`(\\sum_k (\\sum_l \\lvert x_{k,l} \\rvert^p)^{q/p})^{1/q}`.

### Community 175 - "Community 175"
Cohesion: 0.50
Nodes (3): lambda_sum_largest_canon(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, S_k(X) denotes lambda_sum_largest(X, k)     t >= k S_k(X - Z) + trace(Z), Z is P

### Community 176 - "Community 176"
Cohesion: 0.50
Nodes (3): psd_canon(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Canonicalize functions that take a Hermitian matrix.

### Community 177 - "Community 177"
Cohesion: 0.50
Nodes (3): Copyright 2022, the CVXPY authors  Licensed under the Apache License, Version 2., Reduces the atom to an affine expression and list of constraints.      Creates t, tr_inv_canon()

### Community 178 - "Community 178"
Cohesion: 0.50
Nodes (2): Raises an error due to chained constraints., Raises an exception when called.          Python 3 version.          Called when

### Community 179 - "Community 179"
Cohesion: 0.50
Nodes (2): Scalar infeasibility of the dual variable.          The violation is the infinit, Whether the dual variable satisfies the dual cone constraint.          Parameter

### Community 180 - "Community 180"
Cohesion: 0.50
Nodes (2): Is the Leaf real valued?, Is the Leaf complex valued?

### Community 181 - "Community 181"
Cohesion: 0.50
Nodes (3): Get the label of the constraint., Set the label of the constraint., Delete the label of the constraint.

### Community 182 - "Community 182"
Cohesion: 0.50
Nodes (2): The numeric violation of the constraint.          For nonspectral constraints, t, Checks whether the constraint violation is less than a tolerance.          Param

### Community 183 - "Community 183"
Cohesion: 0.50
Nodes (3): inv_pos(), Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, :math:`x^{-1}` for :math:`x > 0`.

### Community 184 - "Community 184"
Cohesion: 0.50
Nodes (3): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, Alias for ``alpha*pos(x) + beta*neg(x)``., scalene()

### Community 185 - "Community 185"
Cohesion: 0.50
Nodes (3): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, The square root of an expression., sqrt()

### Community 186 - "Community 186"
Cohesion: 0.50
Nodes (3): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t, The square of an expression., square()

### Community 187 - "Community 187"
Cohesion: 0.50
Nodes (3): Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th, Warn if importing ``importing`` would put two OMP-bundling solvers in     one pr, warn_if_omp_conflict()

### Community 188 - "Community 188"
Cohesion: 0.50
Nodes (4): div_bounds(), _ensure_dense(), Convert sparse matrix to dense numpy array and expand to shape if given.      Pa, Bounds for elementwise division: x / y.      Note: If the divisor interval conta

### Community 189 - "Community 189"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 190 - "Community 190"
Cohesion: 0.67
Nodes (1): Copyright 2024 the CVXPY developers  Licensed under the Apache License, Version

### Community 191 - "Community 191"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 192 - "Community 192"
Cohesion: 0.67
Nodes (1): Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th

### Community 193 - "Community 193"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 194 - "Community 194"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 195 - "Community 195"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 196 - "Community 196"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 197 - "Community 197"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 198 - "Community 198"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 199 - "Community 199"
Cohesion: 0.67
Nodes (1): Copyright 2024 the CVXPY developers  Licensed under the Apache License, Version

### Community 200 - "Community 200"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 201 - "Community 201"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 202 - "Community 202"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 203 - "Community 203"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 204 - "Community 204"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 205 - "Community 205"
Cohesion: 0.67
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 206 - "Community 206"
Cohesion: 0.67
Nodes (1): Copyright 2024 the CVXPY developers Licensed under the Apache License, Version 2

### Community 207 - "Community 207"
Cohesion: 0.67
Nodes (2): Counter, A counter for ids.      Attributes     ----------     count : int         The cu

### Community 208 - "Community 208"
Cohesion: 0.67
Nodes (1): Copyright 2018 CVXPY.  Licensed under the Apache License, Version 2.0 (the "Lice

### Community 209 - "Community 209"
Cohesion: 0.67
Nodes (2): get_canon_backend(), This function checks if the problem has expressions of dimension greater     tha

### Community 210 - "Community 210"
Cohesion: 0.67
Nodes (1): Copyright 2025, the CVXPY authors.  Licensed under the Apache License, Version 2

### Community 211 - "Community 211"
Cohesion: 0.67
Nodes (2): Return unique list preserving the order.     https://stackoverflow.com/a/480227, unique_list()

### Community 212 - "Community 212"
Cohesion: 1.00
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 223 - "Community 223"
Cohesion: 1.00
Nodes (1): Copyright 2017 Robin Verschueren  Licensed under the Apache License, Version 2.0

### Community 224 - "Community 224"
Cohesion: 1.00
Nodes (1): The residual of the dual variable with respect to the dual cone.          Analog

### Community 225 - "Community 225"
Cohesion: 1.00
Nodes (1): NumPy.ndarray : The value of the dual variable.

### Community 226 - "Community 226"
Cohesion: 1.00
Nodes (1): Format constraint with label if available.          For constraints, this is the

### Community 227 - "Community 227"
Cohesion: 1.00
Nodes (1): Wrapper for compatibility with variables.

### Community 228 - "Community 228"
Cohesion: 1.00
Nodes (1): Is the Leaf imaginary?

### Community 229 - "Community 229"
Cohesion: 1.00
Nodes (1): int : The maximum number of dimensions of the constrained expression.

### Community 230 - "Community 230"
Cohesion: 1.00
Nodes (1): Returns a string with information about the constraint.

### Community 231 - "Community 231"
Cohesion: 1.00
Nodes (1): The residual of the constraint.          Returns         -------         NumPy.n

### Community 232 - "Community 232"
Cohesion: 1.00
Nodes (1): Save the value of the dual variable for the constraint's parent.         Args:

### Community 233 - "Community 233"
Cohesion: 1.00
Nodes (1): Set a custom label for this constraint.          This method exists alongside th

### Community 234 - "Community 234"
Cohesion: 1.00
Nodes (1): int : The shape of the constrained expression.

### Community 235 - "Community 235"
Cohesion: 1.00
Nodes (1): int : The size of the constrained expression.

### Community 236 - "Community 236"
Cohesion: 1.00
Nodes (1): Returns a string showing the mathematical constraint.

### Community 237 - "Community 237"
Cohesion: 1.00
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 238 - "Community 238"
Cohesion: 1.00
Nodes (1): Copyright 2025 CVXPY developers  Licensed under the Apache License, Version 2.0

### Community 239 - "Community 239"
Cohesion: 1.00
Nodes (1): Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th

### Community 240 - "Community 240"
Cohesion: 1.00
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 241 - "Community 241"
Cohesion: 1.00
Nodes (1): Copyright 2017 Robin Verschueren  Licensed under the Apache License, Version 2.0

### Community 242 - "Community 242"
Cohesion: 1.00
Nodes (1): Vectorizes the expression.          order: column-major ('F') or row-major ('C')

### Community 243 - "Community 243"
Cohesion: 1.00
Nodes (1): Return a slice/index into the expression.

### Community 244 - "Community 244"
Cohesion: 1.00
Nodes (1): Is the expression a matrix?

### Community 245 - "Community 245"
Cohesion: 1.00
Nodes (1): Expression : The negation of the expression.

### Community 246 - "Community 246"
Cohesion: 1.00
Nodes (1): Equivalent to `cp.reshape(self, shape, order)`.

### Community 247 - "Community 247"
Cohesion: 1.00
Nodes (1): Expression : Called for matrix @ Expression.

### Community 248 - "Community 248"
Cohesion: 1.00
Nodes (1): Expression : The difference of two expressions.

### Community 249 - "Community 249"
Cohesion: 1.00
Nodes (1): Expression : Logical XOR with reversed operands (y ^ x).

### Community 250 - "Community 250"
Cohesion: 1.00
Nodes (1): tuple : The expression dimensions.

### Community 251 - "Community 251"
Cohesion: 1.00
Nodes (1): Equivalent to `cp.trace(self)`.

### Community 252 - "Community 252"
Cohesion: 1.00
Nodes (1): Implementation of .value.

### Community 253 - "Community 253"
Cohesion: 1.00
Nodes (1): Returns: The numeric value of the expression.

### Community 254 - "Community 254"
Cohesion: 1.00
Nodes (1): Equivalent to `cp.var(self)`.

### Community 255 - "Community 255"
Cohesion: 1.00
Nodes (1): Expression : Logical XOR (x ^ y).          Equivalent to ``cp.logic.Xor(x, y)``.

### Community 256 - "Community 256"
Cohesion: 1.00
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 257 - "Community 257"
Cohesion: 1.00
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 258 - "Community 258"
Cohesion: 1.00
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 259 - "Community 259"
Cohesion: 1.00
Nodes (2): get_expr_params(), Get a list of the parameters in the operator.      Parameters     ----------

### Community 260 - "Community 260"
Cohesion: 1.00
Nodes (2): get_expr_vars(), Get a list of the variables in the operator and their shapes.      Parameters

### Community 261 - "Community 261"
Cohesion: 1.00
Nodes (2): hstack(), Concatenates operators horizontally.      Parameters     ----------     operator

### Community 262 - "Community 262"
Cohesion: 1.00
Nodes (2): index(), Indexes/slices an operator.      Parameters     ----------     operator : LinOp

### Community 263 - "Community 263"
Cohesion: 1.00
Nodes (2): is_const(), Returns whether a LinOp is constant.      Parameters     ----------     operator

### Community 264 - "Community 264"
Cohesion: 1.00
Nodes (2): is_scalar(), Returns whether a LinOp is a scalar.      Parameters     ----------     operator

### Community 265 - "Community 265"
Cohesion: 1.00
Nodes (2): kron_l(), Kronecker product of two matrices, where the left operand is a Variable      Par

### Community 266 - "Community 266"
Cohesion: 1.00
Nodes (2): kron_r(), Kronecker product of two matrices, where the right operand is a Variable      Pa

### Community 267 - "Community 267"
Cohesion: 1.00
Nodes (2): mul_expr(), Multiply two linear operators, with the constant on the left.      Parameters

### Community 268 - "Community 268"
Cohesion: 1.00
Nodes (2): multiply(), Multiply two linear operators elementwise.      Parameters     ----------     lh

### Community 269 - "Community 269"
Cohesion: 1.00
Nodes (2): promote_lin_ops_for_mul(), Promote arguments for multiplication.      Parameters     ----------     lh_op :

### Community 270 - "Community 270"
Cohesion: 1.00
Nodes (2): promote(), Promotes a scalar operator to the given shape.      Parameters     ----------

### Community 271 - "Community 271"
Cohesion: 1.00
Nodes (2): Multiply two linear operators, with the constant on the right.      Parameters, rmul_expr()

### Community 272 - "Community 272"
Cohesion: 1.00
Nodes (2): Sum the entries of an operator.      Parameters     ----------     operator : Li, sum_entries()

### Community 273 - "Community 273"
Cohesion: 1.00
Nodes (2): Sum the diagonal entries of an operator.      Parameters     ----------     oper, trace()

### Community 274 - "Community 274"
Cohesion: 1.00
Nodes (2): Transposes an operator.      Parameters     ----------     operator : LinOp, transpose()

### Community 275 - "Community 275"
Cohesion: 1.00
Nodes (2): Reshapes an operator.      Parameters     ----------     operator : LinOp, reshape()

### Community 276 - "Community 276"
Cohesion: 1.00
Nodes (2): Vectorized upper triangular portion of a square matrix.      Parameters     ----, upper_tri()

### Community 277 - "Community 277"
Cohesion: 1.00
Nodes (2): Concatenates operators vertically.      Parameters     ----------     operators, vstack()

### Community 278 - "Community 278"
Cohesion: 1.00
Nodes (1): Copyright 2025 The CVXPY Developers  Licensed under the Apache License, Version

### Community 279 - "Community 279"
Cohesion: 1.00
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 280 - "Community 280"
Cohesion: 1.00
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 281 - "Community 281"
Cohesion: 1.00
Nodes (1): Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t

### Community 282 - "Community 282"
Cohesion: 1.00
Nodes (2): min_reduction_bounds(), Bounds for min reduction: min(x, axis=axis).      Parameters     ----------

### Community 283 - "Community 283"
Cohesion: 1.00
Nodes (2): minimum_bounds(), Bounds for elementwise minimum: min(x1, x2, ...).      Parameters     ----------

### Community 284 - "Community 284"
Cohesion: 1.00
Nodes (2): neg_bounds(), Bounds for negation: -x.      Parameters     ----------     lb, ub : np.ndarray

### Community 285 - "Community 285"
Cohesion: 1.00
Nodes (2): power_bounds(), Bounds for elementwise power: x^p.      Handles different cases based on p:

### Community 286 - "Community 286"
Cohesion: 1.00
Nodes (2): Return uniform bounds as memory-efficient broadcast views.      This creates rea, uniform_bounds()

### Community 287 - "Community 287"
Cohesion: 1.00
Nodes (2): Return bounds for a scalar.      Parameters     ----------     lb : float, scalar_bounds()

### Community 288 - "Community 288"
Cohesion: 1.00
Nodes (2): Bounds for scalar multiplication: c * x.      Parameters     ----------     lb,, scale_bounds()

### Community 289 - "Community 289"
Cohesion: 1.00
Nodes (2): Bounds for elementwise square root: sqrt(x).      sqrt is monotonically increasi, sqrt_bounds()

### Community 290 - "Community 290"
Cohesion: 1.00
Nodes (2): Reshape bounds to a new shape.      Parameters     ----------     lb, ub : array, reshape_bounds()

### Community 291 - "Community 291"
Cohesion: 1.00
Nodes (1): Copyright 2025, the CVXPY Authors  Licensed under the Apache License, Version 2.

## Knowledge Gaps
- **373 isolated node(s):** `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`, `Base class for expressions involving binary operators. (other than addition)`, `Trace is nonneg (nonpos) if its argument is elementwise nonneg         (nonpos)`, `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`, `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t` (+368 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 61`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 83`** (2 nodes): `indicator`, `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 129`** (1 nodes): `concatenate()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 156`** (1 nodes): `Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 167`** (2 nodes): `Checks whether the constraint is DCP.          Returns         -------         b`, `Checks whether the constraint is DGP.          Returns         -------         b`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 168`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 171`** (2 nodes): `Gives the (sub/super)gradient of the atom w.r.t. each argument.          Matrix`, `Gives the (sub/super)gradient of the atom w.r.t. a column argument.          Mat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 178`** (2 nodes): `Raises an error due to chained constraints.`, `Raises an exception when called.          Python 3 version.          Called when`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 179`** (2 nodes): `Scalar infeasibility of the dual variable.          The violation is the infinit`, `Whether the dual variable satisfies the dual cone constraint.          Parameter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 180`** (2 nodes): `Is the Leaf real valued?`, `Is the Leaf complex valued?`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 182`** (2 nodes): `The numeric violation of the constraint.          For nonspectral constraints, t`, `Checks whether the constraint violation is less than a tolerance.          Param`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 189`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (1 nodes): `Copyright 2024 the CVXPY developers  Licensed under the Apache License, Version`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 191`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 192`** (1 nodes): `Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 193`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 194`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 195`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 196`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 197`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 198`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 199`** (1 nodes): `Copyright 2024 the CVXPY developers  Licensed under the Apache License, Version`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 200`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 201`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 202`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 203`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 204`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 205`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 206`** (1 nodes): `Copyright 2024 the CVXPY developers Licensed under the Apache License, Version 2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 207`** (2 nodes): `Counter`, `A counter for ids.      Attributes     ----------     count : int         The cu`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 208`** (1 nodes): `Copyright 2018 CVXPY.  Licensed under the Apache License, Version 2.0 (the "Lice`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 209`** (2 nodes): `get_canon_backend()`, `This function checks if the problem has expressions of dimension greater     tha`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 210`** (1 nodes): `Copyright 2025, the CVXPY authors.  Licensed under the Apache License, Version 2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 211`** (2 nodes): `Return unique list preserving the order.     https://stackoverflow.com/a/480227`, `unique_list()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 212`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 223`** (1 nodes): `Copyright 2017 Robin Verschueren  Licensed under the Apache License, Version 2.0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 224`** (1 nodes): `The residual of the dual variable with respect to the dual cone.          Analog`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 225`** (1 nodes): `NumPy.ndarray : The value of the dual variable.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 226`** (1 nodes): `Format constraint with label if available.          For constraints, this is the`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 227`** (1 nodes): `Wrapper for compatibility with variables.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 228`** (1 nodes): `Is the Leaf imaginary?`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 229`** (1 nodes): `int : The maximum number of dimensions of the constrained expression.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 230`** (1 nodes): `Returns a string with information about the constraint.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 231`** (1 nodes): `The residual of the constraint.          Returns         -------         NumPy.n`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 232`** (1 nodes): `Save the value of the dual variable for the constraint's parent.         Args:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 233`** (1 nodes): `Set a custom label for this constraint.          This method exists alongside th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 234`** (1 nodes): `int : The shape of the constrained expression.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 235`** (1 nodes): `int : The size of the constrained expression.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 236`** (1 nodes): `Returns a string showing the mathematical constraint.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 237`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 238`** (1 nodes): `Copyright 2025 CVXPY developers  Licensed under the Apache License, Version 2.0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 239`** (1 nodes): `Copyright, the CVXPY authors  Licensed under the Apache License, Version 2.0 (th`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 240`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 241`** (1 nodes): `Copyright 2017 Robin Verschueren  Licensed under the Apache License, Version 2.0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 242`** (1 nodes): `Vectorizes the expression.          order: column-major ('F') or row-major ('C')`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 243`** (1 nodes): `Return a slice/index into the expression.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 244`** (1 nodes): `Is the expression a matrix?`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 245`** (1 nodes): `Expression : The negation of the expression.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 246`** (1 nodes): `Equivalent to `cp.reshape(self, shape, order)`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 247`** (1 nodes): `Expression : Called for matrix @ Expression.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 248`** (1 nodes): `Expression : The difference of two expressions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 249`** (1 nodes): `Expression : Logical XOR with reversed operands (y ^ x).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 250`** (1 nodes): `tuple : The expression dimensions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 251`** (1 nodes): `Equivalent to `cp.trace(self)`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 252`** (1 nodes): `Implementation of .value.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 253`** (1 nodes): `Returns: The numeric value of the expression.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 254`** (1 nodes): `Equivalent to `cp.var(self)`.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 255`** (1 nodes): `Expression : Logical XOR (x ^ y).          Equivalent to ``cp.logic.Xor(x, y)``.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 256`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 257`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 258`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 259`** (2 nodes): `get_expr_params()`, `Get a list of the parameters in the operator.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 260`** (2 nodes): `get_expr_vars()`, `Get a list of the variables in the operator and their shapes.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 261`** (2 nodes): `hstack()`, `Concatenates operators horizontally.      Parameters     ----------     operator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 262`** (2 nodes): `index()`, `Indexes/slices an operator.      Parameters     ----------     operator : LinOp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 263`** (2 nodes): `is_const()`, `Returns whether a LinOp is constant.      Parameters     ----------     operator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 264`** (2 nodes): `is_scalar()`, `Returns whether a LinOp is a scalar.      Parameters     ----------     operator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 265`** (2 nodes): `kron_l()`, `Kronecker product of two matrices, where the left operand is a Variable      Par`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 266`** (2 nodes): `kron_r()`, `Kronecker product of two matrices, where the right operand is a Variable      Pa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 267`** (2 nodes): `mul_expr()`, `Multiply two linear operators, with the constant on the left.      Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 268`** (2 nodes): `multiply()`, `Multiply two linear operators elementwise.      Parameters     ----------     lh`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 269`** (2 nodes): `promote_lin_ops_for_mul()`, `Promote arguments for multiplication.      Parameters     ----------     lh_op :`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 270`** (2 nodes): `promote()`, `Promotes a scalar operator to the given shape.      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 271`** (2 nodes): `Multiply two linear operators, with the constant on the right.      Parameters`, `rmul_expr()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 272`** (2 nodes): `Sum the entries of an operator.      Parameters     ----------     operator : Li`, `sum_entries()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 273`** (2 nodes): `Sum the diagonal entries of an operator.      Parameters     ----------     oper`, `trace()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 274`** (2 nodes): `Transposes an operator.      Parameters     ----------     operator : LinOp`, `transpose()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 275`** (2 nodes): `Reshapes an operator.      Parameters     ----------     operator : LinOp`, `reshape()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 276`** (2 nodes): `Vectorized upper triangular portion of a square matrix.      Parameters     ----`, `upper_tri()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 277`** (2 nodes): `Concatenates operators vertically.      Parameters     ----------     operators`, `vstack()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 278`** (1 nodes): `Copyright 2025 The CVXPY Developers  Licensed under the Apache License, Version`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 279`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 280`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 281`** (1 nodes): `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 282`** (2 nodes): `min_reduction_bounds()`, `Bounds for min reduction: min(x, axis=axis).      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 283`** (2 nodes): `minimum_bounds()`, `Bounds for elementwise minimum: min(x1, x2, ...).      Parameters     ----------`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 284`** (2 nodes): `neg_bounds()`, `Bounds for negation: -x.      Parameters     ----------     lb, ub : np.ndarray`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 285`** (2 nodes): `power_bounds()`, `Bounds for elementwise power: x^p.      Handles different cases based on p:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 286`** (2 nodes): `Return uniform bounds as memory-efficient broadcast views.      This creates rea`, `uniform_bounds()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 287`** (2 nodes): `Return bounds for a scalar.      Parameters     ----------     lb : float`, `scalar_bounds()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 288`** (2 nodes): `Bounds for scalar multiplication: c * x.      Parameters     ----------     lb,`, `scale_bounds()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 289`** (2 nodes): `Bounds for elementwise square root: sqrt(x).      sqrt is monotonically increasi`, `sqrt_bounds()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 290`** (2 nodes): `Reshape bounds to a new shape.      Parameters     ----------     lb, ub : array`, `reshape_bounds()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 291`** (1 nodes): `Copyright 2025, the CVXPY Authors  Licensed under the Apache License, Version 2.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Constraint` connect `Community 0` to `Community 25`, `Community 23`, `Community 59`, `Community 71`, `Community 55`, `Community 44`, `Community 48`, `Community 84`, `Community 87`, `Community 27`, `Community 63`, `Community 143`, `Community 14`, `Community 119`, `Community 57`, `Community 4`, `Community 1`, `Community 75`, `Community 73`, `Community 51`, `Community 38`, `Community 91`, `Community 31`, `Community 2`, `Community 34`, `Community 92`, `Community 81`, `Community 45`, `Community 202`, `Community 5`, `Community 15`, `Community 16`, `Community 62`, `Community 178`, `Community 224`, `Community 225`, `Community 179`, `Community 226`, `Community 227`, `Community 180`, `Community 167`, `Community 228`, `Community 181`, `Community 229`, `Community 230`, `Community 231`, `Community 232`, `Community 233`, `Community 234`, `Community 235`, `Community 236`, `Community 182`, `Community 114`, `Community 99`, `Community 26`, `Community 12`, `Community 65`, `Community 13`, `Community 157`, `Community 37`, `Community 115`, `Community 103`, `Community 52`, `Community 18`, `Community 100`, `Community 50`, `Community 54`, `Community 110`, `Community 86`, `Community 3`, `Community 19`, `Community 9`, `Community 121`, `Community 22`, `Community 83`?**
  _High betweenness centrality (0.254) - this node is a cross-community bridge._
- **Why does `Expression` connect `Community 0` to `Community 25`, `Community 23`, `Community 59`, `Community 27`, `Community 40`, `Community 2`, `Community 170`, `Community 84`, `Community 4`, `Community 57`, `Community 63`, `Community 143`, `Community 14`, `Community 1`, `Community 60`, `Community 77`, `Community 51`, `Community 172`, `Community 173`, `Community 38`, `Community 31`, `Community 174`, `Community 41`, `Community 78`, `Community 102`, `Community 85`, `Community 64`, `Community 144`, `Community 34`, `Community 26`, `Community 15`, `Community 24`, `Community 146`, `Community 3`, `Community 13`, `Community 123`, `Community 183`, `Community 49`, `Community 20`, `Community 108`, `Community 47`, `Community 50`, `Community 184`, `Community 185`, `Community 186`, `Community 66`, `Community 71`, `Community 67`, `Community 52`, `Community 242`, `Community 243`, `Community 148`, `Community 244`, `Community 245`, `Community 246`, `Community 247`, `Community 248`, `Community 249`, `Community 250`, `Community 251`, `Community 253`, `Community 252`, `Community 254`, `Community 255`, `Community 19`, `Community 6`, `Community 121`, `Community 74`, `Community 5`, `Community 83`, `Community 169`?**
  _High betweenness centrality (0.188) - this node is a cross-community bridge._
- **Why does `Solution` connect `Community 28` to `Community 35`, `Community 26`, `Community 12`, `Community 15`, `Community 36`, `Community 10`, `Community 11`, `Community 24`, `Community 122`, `Community 70`, `Community 21`, `Community 7`, `Community 95`, `Community 106`, `Community 47`, `Community 30`, `Community 39`, `Community 124`, `Community 133`, `Community 134`, `Community 135`, `Community 136`, `Community 127`, `Community 13`, `Community 4`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Are the 801 inferred relationships involving `Constraint` (e.g. with `AddExpression` and `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`) actually correct?**
  _`Constraint` has 801 INFERRED edges - model-reasoned connections that need verification._
- **Are the 612 inferred relationships involving `Expression` (e.g. with `AddExpression` and `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`) actually correct?**
  _`Expression` has 612 INFERRED edges - model-reasoned connections that need verification._
- **Are the 453 inferred relationships involving `Atom` (e.g. with `AffAtom` and `Copyright 2013 Steven Diamond  Licensed under the Apache License, Version 2.0 (t`) actually correct?**
  _`Atom` has 453 INFERRED edges - model-reasoned connections that need verification._
- **Are the 442 inferred relationships involving `Solution` (e.g. with `Dualize` and `Copyright 2020 the CVXPY developers  Licensed under the Apache License, Version`) actually correct?**
  _`Solution` has 442 INFERRED edges - model-reasoned connections that need verification._