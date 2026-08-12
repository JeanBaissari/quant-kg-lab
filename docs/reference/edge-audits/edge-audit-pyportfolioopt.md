# Edge Audit — pyportfolioopt

**Date**: 2026-08-12

## Summary

- Total edges: 512
- EXTRACTED: 439 (85.7%)
- INFERRED: 73 (14.3%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `EfficientFrontier`: 26 inferred edges
- `InstantiationError`: 21 inferred edges
- `OptimizationError`: 21 inferred edges
- `The ``efficient_frontier`` module houses the EfficientFrontier class and its des`: 4 inferred edges
- `BaseConvexOptimizer`: 3 inferred edges
- `BaseOptimizer`: 3 inferred edges
- `The ``base_optimizer`` module houses the parent classes ``BaseOptimizer`` from w`: 2 inferred edges
- `Utility method to save weights to a text file.          Parameters         -----`: 2 inferred edges
- `The BaseConvexOptimizer contains many private variables for use by     ``cvxpy```: 2 inferred edges
- `Parameters         ----------         weight_bounds : tuple or list of tuples, o`: 2 inferred edges
- `Returns a custom deep copy of the optimizer. This is necessary because         ``: 2 inferred edges
- `Convert input bounds into a form acceptable by cvxpy and add to the constraints`: 2 inferred edges
- `Helper method to solve the cvxpy problem and check output,         once objectiv`: 2 inferred edges
- `Instance variables:      - ``n_assets`` - int     - ``tickers`` - str list     -`: 2 inferred edges
- `Add a new term into the objective function. This term must be convex,         an`: 2 inferred edges
- `Add a new constraint to the optimization problem. This constraint must satisfy D`: 2 inferred edges
- `Adds constraints on the sum of weights of different groups of assets.         Mo`: 2 inferred edges
- `Optimize a custom convex objective function. Constraints should be added with`: 2 inferred edges
- `Parameters         ----------         n_assets : int             number of asset`: 2 inferred edges
- `Optimize some objective function using the scipy backend. This can         suppo`: 2 inferred edges

## Cross-Module Suspicious Edges

- `_base_optimizer.py` ↔ `exceptions.py`: 42
- `efficient_semivariance.py` ↔ `efficient_frontier.py`: 9
- `efficient_cdar.py` ↔ `efficient_frontier.py`: 8
- `efficient_cvar.py` ↔ `efficient_frontier.py`: 8
- `base_optimizer.py` ↔ `_base_optimizer.py`: 2
- `__init__.py` ↔ `efficient_cdar.py`: 1
- `__init__.py` ↔ `efficient_cvar.py`: 1
- `__init__.py` ↔ `efficient_frontier.py`: 1
- `__init__.py` ↔ `efficient_semivariance.py`: 1
