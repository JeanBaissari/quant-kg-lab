---
name: scipy-stats
description: "Use when doing statistics with SciPy \u2014 distributions, hypothesis\
  \ tests (ttest/ks/mannwhitneyu), gaussian_kde, zscore, and bootstrap/permutation\
  \ resampling."
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
  graph_hash: a01c8f8bb3e63782
tags:
- scipy
- stats
related_skills: []
target_version: '1.18.0 (dev: after 1.18.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `scipy` ahead of the latest PyPI release (1.18.0 (dev: after 1.18.0)). Some APIs may not exist in your installed version.

# scipy.stats

Statistical functions, probability distributions, and hypothesis tests. The workhorse module for quantitative analysis — covers everything from descriptive statistics to distribution fitting, density estimation, and resampling-based inference.

## Quick Reference

| API | Source File | Degree | Description |
|-----|------------|--------|-------------|
| `UnivariateDistribution` | `stats/_distribution_infrastructure.py:L1422` | 196 | Base class for all continuous distributions; `norm`, `t`, `chi2` are instances |
| `PermutationMethod` | `stats/_resampling.py:L2249` | 105 | Resampling configuration for permutation tests |
| `BootstrapMethod` | `stats/_resampling.py:L2334` | 105 | Resampling configuration for bootstrap confidence intervals |
| `MonteCarloMethod` | `stats/_resampling.py:L2179` | 103 | Resampling configuration for Monte Carlo hypothesis tests |
| `gaussian_kde` | `stats/_kde.py:L38` | — | Kernel density estimation for multivariate data |
| `ttest_ind()` | `_stats_py.py:L6554` | 9 | Independent two-sample t-test (highest-degree test function) |
| `mannwhitneyu()` | `_mannwhitneyu.py:L246` | 7 | Mann-Whitney U rank test |
| `rv_continuous` | `stats/_distn_infrastructure.py:L1669` | 196 | Base class for custom continuous distributions |
| `norm` | `stats/_new_distributions.py:L16` | — | Normal distribution (exemplar `rv_continuous` instance) |
| `describe()` | `_stats_py.py:L1448` | 6 | Descriptive statistics summary |
| `zscore()` | `_stats_py.py:L2673` | 4 | Compute z-scores relative to sample mean and std |
| `bootstrap()` | `_resampling.py:L300` | 6 | Bootstrap confidence intervals for any statistic |

### Additional Key APIs

| API | Type | Description |
|-----|------|-------------|
| `rv_continuous` | class | Base class for custom continuous distributions; `norm`, `t`, `chi2` are instances |
| `CensoredData` | class | Right/left/interval-censored data container |
| `QMCEngine` | class | Quasi-Monte Carlo sampling (Sobol, Halton) |
| `fit()` | function | Public fit method (scipy ≥ 1.9): `dist.fit(data)` returns `(loc, scale)` tuple |
| `pearsonr()` | function | Pearson correlation coefficient with p-value |
| `spearmanr()` | function | Spearman rank correlation |
| `linregress()` | function | Linear regression with p-values |
| `kstest()` | function | Kolmogorov-Smirnov goodness-of-fit test |
| `shapiro()` | function | Shapiro-Wilk normality test |
| `levene()` | function | Levene's test for equal variances |
| `f_oneway()` | function | One-way ANOVA |
| `jarque_bera()` | function | Jarque-Bera normality test |
| `combine_pvalues()` | function | Combine p-values from independent tests |
| `binned_statistic_dd()` | function | N-dimensional binned statistics |
| `rankdata()` | function | Assign ranks to data, handling ties |
| `entropy()` | function | Calculate entropy of a distribution |
| `mode()` | function | Mode (most frequent value) |

## Distribution Objects

`stats.norm` is a frozen `rv_continuous` instance (loc=0, scale=1). To create
distributions with different parameters, pass keyword arguments:

```python
from scipy import stats

dist = stats.norm(loc=0, scale=1)  # frozen instance
dist.pdf(0)      # 0.3989...
dist.cdf(0)      # 0.5
dist.ppf(0.975)  # 1.96
dist.rvs(size=1000)

# Custom distributions subclass rv_continuous
# (ContinuousDistribution does NOT exist in released scipy)
```

## Common Patterns

### Statistical Tests
```python
from scipy import stats
import numpy as np

# Two-sample t-test
a, b = np.random.randn(100), np.random.randn(100) + 0.5
stat, p = stats.ttest_ind(a, b)
print(f"t={stat:.3f}, p={p:.4f}")

# Mann-Whitney U (non-parametric)
stat, p = stats.mannwhitneyu(a, b, alternative='two-sided')

# One-way ANOVA
g1, g2, g3 = np.random.randn(30), np.random.randn(30)+1, np.random.randn(30)+2
stat, p = stats.f_oneway(g1, g2, g3)

# Kolmogorov-Smirnov test
stat, p = stats.kstest(a, 'norm', args=(0, 1))

# Shapiro-Wilk normality test
stat, p = stats.shapiro(a)

# Correlation with p-values
r, p = stats.pearsonr(a, b)
rho, p = stats.spearmanr(a, b)
```

### Descriptive Statistics
```python
from scipy.stats import describe, zscore, iqr, trim_mean, gmean

result = describe(data)
print(result.mean, result.variance, result.skewness, result.kurtosis)

zscores = zscore(data)         # (x - mean) / std
iqr_val = iqr(data)            # Q3 - Q1
trimmed = trim_mean(data, 0.1) # 10% trimmed mean
```

### Gaussian KDE
```python
from scipy.stats import gaussian_kde
kde = gaussian_kde(data.T)         # data shape: (d, n)
density = kde.evaluate(points)     # evaluate at new points
log_dens = kde.logpdf(points.T)
samples = kde.resample(size=1000)
```

### Bootstrap and Resampling
```python
from scipy.stats import bootstrap

# Bootstrap CI for any statistic
res = bootstrap(
    (data,), np.median,
    n_resamples=9999,
    confidence_level=0.95,
    method='BCa'
)
print(res.confidence_interval)
```

### Distribution Fitting
```python
# Fit a distribution to data — returns (loc, scale) tuple
params = stats.norm.fit(data)  # → (loc, scale)

# Fit with censored data
censored = stats.CensoredData(uncensored=observed, right=censored_at)
params = stats.norm.fit(censored)
```

## Pitfalls

1. **`norm` is not a class, it's an instance**: `stats.norm` is a frozen `rv_continuous` instance with `loc=0, scale=1`. To create a distribution with different parameters, use `stats.norm(loc=5, scale=2)`. Do NOT try `stats.norm(loc=5, scale=2).__class__` — it returns the frozen instance, not a parameterized class.

2. **Small-sample tests are unreliable but still computed**: Functions like `ttest_ind`, `mannwhitneyu`, and `pearsonr` do NOT emit a `SmallSampleWarning` — they compute without warning even at n=5. Statistical tests at very small n are unreliable but still computed — validate against known outcomes before trusting results.

3. **`gaussian_kde` bandwidth scales with data range**: The default Scott's rule bandwidth can over-smooth multimodal data. For tight clusters or heavy tails, try `gaussian_kde(data, bw_method='silverman')` or manually reduce the bandwidth: `gaussian_kde(data, bw_method=0.1)`.

4. **`describe()` returns `DescribeResult` (a namedtuple)**: Access fields as `result.mean`, `result.skewness`, etc. The v1.15+ `describe` has different return structure from legacy — check `result._fields` if unsure.

5. **Bootstrap `BCa` method requires smooth statistics**: For discrete statistics (medians on small integer data), `BCa` can fail. Fall back to `method='percentile'` or `method='basic'`.

6. **Statistical tests assume i.i.d. data**: Functions like `ttest_ind` assume independent samples. For paired data, use `ttest_rel`. For time-series data where observations are autocorrelated, standard p-values are inflated — consider block bootstrap or HAC-robust inference.

7. **`ContinuousDistribution` does not exist in released scipy**: The class `ContinuousDistribution` is private (`scipy.stats._distribution_infrastructure.ContinuousDistribution`) and never exported. Use `rv_continuous` for custom distributions or `scipy.stats.norm` (and other frozen instances) for standard distributions. Use `scipy.stats.norm.fit()` for distribution fitting.

## Cross-Library Bridges

| Bridge | Relation | Description |
|--------|----------|-------------|
| scipy.stats → sklearn `SelectKBest` | `powers` | scipy.stats statistical tests (f_classif, chi2) drive sklearn feature selection |
| numpy.random → scipy.stats | `complements` | numpy.random generates raw samples; scipy.stats models distributions and performs inference |
| scipy.stats → pandas DataFrame | `data_source` | Statistical test results typically fed via pandas DataFrames in quant pipelines |

## Verification Checklist

- [ ] `stats.ttest_ind(a, b)` returns `(statistic, pvalue)` tuple
- [ ] `stats.norm.pdf(0)` ≈ 0.3989
- [ ] `stats.zscore([1,2,3,4,5])` returns `[-1.414, -0.707, 0, 0.707, 1.414]` (approx)
- [ ] `gaussian_kde(data).evaluate(points)` returns density at points
- [ ] `stats.bootstrap((data,), np.mean)` runs without error
- [ ] `stats.describe(data)` returns `DescribeResult` with `mean`, `variance` fields
- [ ] `stats.pearsonr(x, y)` returns `(r, pvalue)` — not just r
- [ ] `stats.mannwhitneyu(a, b, alternative='two-sided')` accepts `alternative` kwarg
- [ ] `stats.CensoredData` accepts `right`, `left`, `interval` keyword args
- [ ] `stats.norm.fit(data)` returns `(loc, scale)` tuple (not a FitResult object)
- [ ] `rv_continuous` is available as base class for custom distributions

## Provenance

- Knowledge graph: scipy, 14071 nodes, 23466 edges, 1076 communities
- God nodes: `CensoredData` (342), `FitError` (320), `rv_continuous` (278) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 0514ef9e7329, backend opencode, description coverage 81%
