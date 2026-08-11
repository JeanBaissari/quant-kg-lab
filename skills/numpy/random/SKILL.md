---
name: numpy-random
description: "Use when generating random numbers with NumPy — Generator, default_rng, distributions, permutation, and seeding."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
source_commit: ab2199763cb17878cd8f34fcbc97106c5397f922
extraction_date: 2026-07-29
graph:
  nodes: 8345
  edges: 13507
  community_count: 670
  graph_hash: 11fb7485308e9cec
tags: [numpy, random]
related_skills: []
---

# NumPy Random Number Generation (`numpy.random`)

NumPy's random module provides a modern, reproducible, and high-performance random number generation system backed by multiple bit generators, seed sequences for independent streams, and a rich set of probability distributions.

## Quick Reference: Top 10 APIs

| API | Signature | Description |
|-----|-----------|-------------|
| `default_rng` | `default_rng(seed=None)` | Create a new Generator with default BitGenerator (PCG64) |
| `Generator` | Class wrapping a BitGenerator | Primary distribution-sampling interface |
| `PCG64` | `PCG64(seed=None)` | Default BitGenerator — fast, statistically sound |
| `SeedSequence` | `SeedSequence(entropy=None)` | Generate independent seed states for parallel streams |
| `random` | `rng.random(size=None, dtype=np.float64)` | Uniform floats in [0, 1) |
| `normal` | `rng.normal(loc=0.0, scale=1.0, size=None)` | Gaussian/normal distribution |
| `uniform` | `rng.uniform(low=0.0, high=1.0, size=None)` | Uniform floats in [low, high) |
| `integers` | `rng.integers(low, high=None, size=None)` | Random integers in [low, high) |
| `choice` | `rng.choice(a, size=None, replace=True, p=None)` | Random sample from a 1-D array |
| `permutation` | `rng.permutation(x)` | Randomly permute a sequence or return a permuted range |

## Architecture

```
SeedSequence(entropy) → spawn(n) → independent seeds
                                  ↓
                            seed → BitGenerator → Generator
                                  (PCG64)          ├─ .random()
                                   (MT19937)       ├─ .normal()
                                   (Philox)        ├─ .uniform()
                                   (SFC64)         ├─ .choice()
                                                   └─ .permutation()
```

## BitGenerators

The underlying pseudo-random number generators that produce raw uint64 streams:

| BitGenerator | Characteristics |
|-------------|-----------------|
| **PCG64** | Default. Permuted Congruential Generator. Fast, good statistical properties. |
| **PCG64DXSM** | PCG variant with improved statistical quality for float generation. |
| **MT19937** | Mersenne Twister. Legacy standard, long period (2^19937-1). Large state (2.5 KB). |
| **Philox** | Counter-based. Fully parallelizable, minimal state (64 bytes). Best for GPU/JIT. |
| **SFC64** | Small Fast Chaotic. Very fast, compact state (32 bytes). Statistically good. |

### SeedSequence

```python
from numpy.random import SeedSequence

# Single seed → reproducible stream
ss = SeedSequence(12345)
rng = np.random.default_rng(ss)

# Spawn independent child streams (for parallel processing)
child_seeds = ss.spawn(4)
rngs = [np.random.default_rng(s) for s in child_seeds]

# Multi-component entropy (e.g., job ID + task ID)
ss = SeedSequence((job_id, task_id))
```

## Common Patterns

```python
import numpy as np

# Modern API (recommended) — create a Generator
rng = np.random.default_rng(seed=42)

# Uniform random floats in [0, 1)
rng.random(10)              # shape (10,)
rng.random((3, 4))          # shape (3, 4)

# Normal distribution
rng.normal(loc=0, scale=1, size=1000)
rng.normal(loc=[0, 5, 10], scale=[1, 2, 3], size=(1000, 3))  # broadcasting

# Uniform in range
rng.uniform(low=0, high=10, size=100)

# Random integers
rng.integers(0, 100, size=10)           # [0, 100)
rng.integers(5, size=(3, 4))            # [0, 5)
rng.integers(0, 256, dtype=np.uint8)    # specific dtype

# Choice from an array
rng.choice(['a', 'b', 'c'], size=10, p=[0.5, 0.3, 0.2])
rng.choice(100, size=5, replace=False)  # sample without replacement

# Permutation
arr = np.arange(10)
rng.permutation(arr)         # returns permuted copy (original unchanged)
rng.shuffle(arr)              # permutes in-place

# Other key distributions
rng.standard_normal(100)     # N(0, 1)
rng.standard_exponential(100)# Exp(1)
rng.binomial(n=10, p=0.5, size=100)
rng.poisson(lam=5, size=100)
rng.gamma(shape=2, scale=1, size=100)
rng.beta(a=2, b=5, size=100)
rng.chisquare(df=3, size=100)
rng.dirichlet(alpha=(1, 2, 3), size=100)
rng.multinomial(n=10, pvals=[0.2, 0.3, 0.5], size=100)
rng.multivariate_normal(mean=[0, 0], cov=[[1, 0.5], [0.5, 1]], size=100)

# Reproducibility with bit generator state
state = rng.bit_generator.state  # get state
rng2 = np.random.default_rng()
rng2.bit_generator.state = state  # restore state — generates same sequence

# BitGenerator directly (not recommended for most users)
bg = np.random.PCG64(seed=42)
bg.random_raw(5)  # raw uint64 values

# Legacy API (compatibility only — avoid in new code)
np.random.seed(42)
np.random.rand(10)            # ← prefer rng.random
np.random.randn(10)           # ← prefer rng.standard_normal
np.random.randint(0, 100, 10) # ← prefer rng.integers
```

## Distributions Reference

| Distribution | Generator Method |
|-------------|-----------------|
| Beta | `beta(a, b)` |
| Binomial | `binomial(n, p)` |
| Chi-square | `chisquare(df)` |
| Dirichlet | `dirichlet(alpha)` |
| Exponential | `exponential(scale=1.0)` |
| F (Fisher-Snedecor) | `f(dfnum, dfden)` |
| Gamma | `gamma(shape, scale=1.0)` |
| Geometric | `geometric(p)` |
| Gumbel | `gumbel(loc=0.0, scale=1.0)` |
| Hypergeometric | `hypergeometric(ngood, nbad, nsample)` |
| Laplace | `laplace(loc=0.0, scale=1.0)` |
| Logistic | `logistic(loc=0.0, scale=1.0)` |
| Lognormal | `lognormal(mean=0.0, sigma=1.0)` |
| Logseries | `logseries(p)` |
| Multinomial | `multinomial(n, pvals)` |
| Multivariate normal | `multivariate_normal(mean, cov)` |
| Negative binomial | `negative_binomial(n, p)` |
| Noncentral chi-square | `noncentral_chisquare(df, nonc)` |
| Normal | `normal(loc=0.0, scale=1.0)` |
| Pareto | `pareto(a)` |
| Poisson | `poisson(lam=1.0)` |
| Power | `power(a)` |
| Rayleigh | `rayleigh(scale=1.0)` |
| Standard Cauchy | `standard_cauchy()` |
| Standard exponential | `standard_exponential()` |
| Standard gamma | `standard_gamma(shape)` |
| Standard normal | `standard_normal()` |
| Standard t | `standard_t(df)` |
| Triangular | `triangular(left, mode, right)` |
| Uniform | `uniform(low=0.0, high=1.0)` |
| Von Mises | `vonmises(mu, kappa)` |
| Wald | `wald(mean, scale)` |
| Weibull | `weibull(a)` |
| Zipf | `zipf(a)` |

## Legacy API (RandomState)

The older `np.random.RandomState` uses MT19937 globally and has a global-only seed (`np.random.seed()`). The legacy API is **not recommended** for new code due to:

- Single global state (thread-unsafe by default)
- `choice(a, p=p)` is slower than Generator's version
- No SeedSequence for independent parallel streams
- Inconsistent distributions (e.g., `randint` is endpoint-exclusive)
- No `integers()` (must use `randint`)
- Can't be pickled or use `bit_generator.state`

Pickling helpers exist in `numpy.random._pickle`: `__generator_ctor()`, `__bit_generator_ctor()`, `__randomstate_ctor()` for serializing random state.

## Pitfalls

1. **Don't use legacy np.random.\* in new code**: Always use `rng = np.random.default_rng()` and call methods on it. The legacy `np.random.seed()` and `np.random.*` functions share global state and are not thread-safe.

2. **SeedSequence entropy is NOT a simple seed**: `SeedSequence(seed)` hashes the entropy to produce a high-quality seed state. Don't rely on small integer differences producing obviously different sequences — they always do, but the relationship is non-obvious.

3. **PCG64 is not cryptographically secure**: None of NumPy's BitGenerators are suitable for cryptographic use. Use `secrets` or `os.urandom` for security-sensitive randomness.

4. **choice with `p` parameter is slow for large arrays**: For large arrays with probabilities, the algorithm must compute cumulative sums. Pre-compute `cumsum(p)` if calling repeatedly.

5. **Generator.spawn() vs SeedSequence.spawn()**: `Generator.spawn(n)` creates child Generators from the current state. `SeedSequence.spawn(n)` creates independent seeds before creating Generators. Use `SeedSequence.spawn()` for truly independent parallel streams.

## Cross-Library Bridges

| Source | Target | Relation | Description |
|--------|--------|----------|-------------|
| numpy.random | `scipy.stats` | **complements** | numpy.random generates samples; scipy.stats models distributions (PDF, CDF, fits) |
| numpy.random | `numba` / `cffi` | **extensible** | numba can JIT-compile custom distributions; cffi can access underlying C functions from `distributions.h` |

- **scipy.stats** provides: `rvs()` (uses numpy.random internally), `pdf()`, `cdf()`, `ppf()`, `fit()`, distribution parameter estimation, and hypothesis testing.
- **numba** integration: Custom BitGenerators and distributions can be written as numba JIT functions for GPU/parallel execution.

## Verification Checklist

- [ ] `default_rng(seed).random()` produces the same output each run with the same seed
- [ ] `SeedSequence.spawn(n)` produces n independent streams
- [ ] All distribution methods accept `size` parameter for batched output
- [ ] `integers()` respects dtype and endpoint exclusivity
- [ ] `choice()` with `p` array correctly samples weighted distribution
- [ ] `permutation()` returns a copy; `shuffle()` mutates in-place
- [ ] Generator is pickleable and restorable via `bit_generator.state`
- [ ] `PCG64` is the default BitGenerator
