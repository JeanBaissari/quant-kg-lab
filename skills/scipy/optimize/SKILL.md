---
name: scipy-optimize
description: "Use when solving optimization or root-finding problems with SciPy \u2014\
  \ minimize, curve_fit, root, linprog, milp, and differential_evolution."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scipy/scipy
source_commit: 0514ef9e73297ef8d6f46379731eedc619f9d201
extraction_date: 2026-07-29
graph:
  nodes: 14071
  edges: 23466
  community_count: 1061
  graph_hash: 0a4109fd8f56eff1
tags:
- scipy
- optimize
related_skills: []
target_version: '1.18.0 (dev: after 1.18.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `scipy` ahead of the latest PyPI release (1.18.0 (dev: after 1.18.0)). Some APIs may not exist in your installed version.

# scipy.optimize

Numerical optimization and root finding. Covers local optimization (`minimize`), global optimization (`differential_evolution`, `basinhopping`), least-squares fitting (`curve_fit`, `least_squares`), linear programming (`linprog`), and scalar root finding (`newton`, `bisect`).

## Quick Reference

| API | Source File | Degree | Description |
|-----|------------|--------|-------------|
| `OptimizeResult` | `optimize/_optimize.py:L114` | 153 | Result container for all optimizers (attributes: `x`, `fun`, `success`, `nit`) |
| `minimize()` | `_minimize.py:L54` | 10 | Unified interface for local optimization (BFGS, Nelder-Mead, SLSQP, trust-constr, etc.) |
| `ScalarFunction` | `_differentiable_functions.py:L128` | 89 | Wraps objective + gradient for scalar optimizers |
| `Bounds` | `optimize/_constraints.py:L257` | 62 | Box constraints `(lb, ub)` for variables |
| `NonlinearConstraint` | `optimize/_constraints.py:L22` | 59 | Nonlinear equality/inequality constraints |
| `LinearConstraint` | `optimize/_constraints.py:L143` | 59 | Linear constraints `A @ x` bounds |
| `DifferentialEvolutionSolver` | `optimize/_differentialevolution.py:L538` | 42 | Global optimization via differential evolution |
| `basinhopping()` | `_basinhopping.py:L351` | 9 | Global optimization with random perturbation + local refinement |
| `dual_annealing()` | `_dual_annealing.py:L453` | 9 | Generalized simulated annealing (global) |
| `curve_fit()` | `_minpack_py.py:L590` | 7 | Nonlinear least-squares curve fitting |

### Additional Key APIs (by degree rank)

| API | Type | Description |
|-----|------|-------------|
| `shgo()` | function | Simplicial homology global optimization |
| `least_squares()` | function | Nonlinear least-squares with bounds |
| `root()` | function | Unified interface for root finding |
| `linprog()` | function | Linear programming (simplex, interior-point, HiGHS) |
| `minimize_scalar()` | function | Univariate function minimization |
| `newton()` | function | Newton-Raphson root finding |
| `bisect()` | function | Bisection root finding |
| `bracket()` | function | Bracket a root for bisection/newton |
| `approx_fprime()` | function | Finite-difference gradient approximation |
| `check_grad()` | function | Verify analytical gradient against finite differences |
| `MemoizeJac` | class | Memoized Jacobian wrapper for efficiency | `optimize/_optimize.py:L63` |

| `BFGS` | class | BFGS Hessian update strategy | `optimize/_hessian_update_strategy.py:L285` |

| `HessianUpdateStrategy` | class | Base for Hessian approximation strategies | `optimize/_hessian_update_strategy.py:L11` |

| `toms748()` | function | TOMS 748 algorithm for root finding |

## Common Patterns

### Local Optimization with `minimize`
```python
from scipy.optimize import minimize, Bounds
import numpy as np

def rosenbrock(x):
    """Rosenbrock function: global minimum at x = [1, 1]."""
    return np.sum(100.0 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

# Unconstrained: BFGS (default for smooth functions)
res = minimize(rosenbrock, x0=[-1, 1], method='BFGS')
print(f"x={res.x}, fun={res.fun}, nit={res.nit}, success={res.success}")

# With bounds
res = minimize(rosenbrock, x0=[-1, 1], method='L-BFGS-B',
               bounds=Bounds([-2, -2], [2, 2]))

# With constraints
from scipy.optimize import NonlinearConstraint, LinearConstraint
res = minimize(objective, x0, method='SLSQP',
               constraints=[
                   LinearConstraint(A, lb, ub),
                   NonlinearConstraint(constraint_func, 0, 0)  # equality
               ])

# Global optimization
res = minimize(rosenbrock, x0=[-1, 1], method='trust-constr')
```

### Curve Fitting
```python
from scipy.optimize import curve_fit

def model(x, a, b, c):
    return a * np.exp(-b * x) + c

popt, pcov = curve_fit(model, xdata, ydata, p0=[1, 0.1, 0])
perr = np.sqrt(np.diag(pcov))  # 1-sigma uncertainties
```

### Root Finding
```python
from scipy.optimize import root, newton, bisect

# Scalar root: f(x) = 0
root_x = newton(lambda x: x**2 - 2, x0=1.5)
root_x = bisect(lambda x: x**2 - 2, a=0, b=2)

# Multivariate root
def system(vars):
    x, y = vars
    return [x**2 + y**2 - 1, x - y]
sol = root(system, x0=[0.5, 0.5])
print(sol.x)  # [0.707, 0.707]
```

### Linear Programming
```python
from scipy.optimize import linprog

# Minimize c @ x subject to A_ub @ x <= b_ub
res = linprog(c=[-1, 4], A_ub=[[-3, 1], [1, 2]], b_ub=[6, 4],
              bounds=[(None, None), (-3, None)], method='highs')
print(res.x, res.fun)
```

### Differential Evolution
```python
from scipy.optimize import differential_evolution

# Global optimization with bounds
bounds = [(-5, 5), (-5, 5)]  # one tuple per dimension
res = differential_evolution(rosenbrock, bounds, seed=42)
print(f"Global min: x={res.x}, fun={res.fun}")
```

## Pitfalls

1. **`minimize` method default changed**: In scipy < 1.11, `method=None` defaulted to BFGS for unconstrained problems. From 1.11+, it raises a warning and picks automatically based on constraints/bounds. Always specify `method=` explicitly — `'BFGS'`, `'L-BFGS-B'`, `'SLSQP'`, or `'trust-constr'` depending on your problem.

2. **Gradient-free methods like Nelder-Mead are slow in high dimensions**: `method='Nelder-Mead'` requires O(n²) function evaluations and fails above ~20 variables. Use `'L-BFGS-B'` for bounded problems with >10 dimensions, or `'differential_evolution'` for global search.

3. **`curve_fit` assumes ydata errors are i.i.d. normal**: The returned `pcov` is valid only if residuals are homoscedastic. For heteroscedastic data, pass `sigma=errors` and `absolute_sigma=True`, or use `least_squares` with custom loss.

4. **`linprog(method='simplex')` is deprecated**: The default `method='highs'` is faster and handles larger problems. If you must use the simplex method, explicitly set `method='revised simplex'`.

5. **Global optimizers may not find the true global minimum**: `differential_evolution` and `basinhopping` are stochastic. Always run with a fixed `seed`, check `res.success`, and consider multiple restarts. For critical applications, combine global + local: `minimize(fun, res.x, method='L-BFGS-B')` to polish the DE result.

6. **`root` default method 'hybr' is deprecated**: Use explicit methods: `method='krylov'` for large sparse systems, `method='anderson'` for fixed-point problems, or `method='broyden1'` as a general-purpose choice.

7. **`OptimizeResult` is a dict with attribute access**: `res.x` and `res['x']` both work. Fields like `jac` (Jacobian at solution) and `hess_inv` (inverse Hessian) are method-dependent and may be absent.

## Cross-Library Bridges

| Bridge | Relation | Description |
|--------|----------|-------------|
| scipy.optimize → optuna samplers | `alternative_to` | scipy.optimize (global: DE, basinhopping) can serve as alternative optimization backend to optuna's Bayesian samplers |
| scipy.optimize → numpy.linalg | `complements` | Least-squares and root finding leverage numpy linear algebra |
| scipy.optimize → sklearn estimators | `powers` | scipy `minimize` can optimize custom loss functions wrapping sklearn `predict` in quant strategies |

## Verification Checklist

- [ ] `minimize(rosenbrock, [0,0], method='BFGS').x` ≈ `[1, 1]`
- [ ] `curve_fit(lambda x,a,b: a*x+b, [0,1,2], [1,3,5])[0]` ≈ `[2, 1]`
- [ ] `newton(lambda x: x**2-2, 1)` ≈ `1.4142`
- [ ] `bisect(lambda x: x**2-2, 0, 2)` ≈ `1.4142`
- [ ] `linprog([-1,1], [[1,1]], [1], bounds=[(0,None),(0,None)]).x` ≈ `[1, 0]`
- [ ] `differential_evolution(lambda x: sum(x**2), [(-1,1)]).x` ≈ `[0]`
- [ ] `res = minimize(...); assert hasattr(res, 'success')`
- [ ] `Bounds(-1, 1)` creates box constraint on all variables
- [ ] `NonlinearConstraint(f, -1, 1)` accepts callable

## Provenance

- Knowledge graph: scipy, 14071 nodes, 23466 edges, 1076 communities
- God nodes: `OptimizeResult` (135), `_tstutils.py:L1` (76), `OptimizeWarning` (70) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 0514ef9e7329, backend opencode, description coverage 81%
