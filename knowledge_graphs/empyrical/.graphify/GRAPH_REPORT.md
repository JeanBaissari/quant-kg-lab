# Graph Report - knowledge_graphs/empyrical/repo/empyrical  (2026-08-13)

## Corpus Check
- Corpus is ~11,435 words - fits in a single context window. You may not need a graph.

## Summary
- 180 nodes · 258 edges · 23 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output
- Edge kinds: contains: 94 · calls: 78 · rationale_for: 78 · imports_from: 7 · inherits: 1


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 7 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `40f61b4`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `render()` - 9 edges
2. `get_versions()` - 8 edges
3. `annualization_factor()` - 8 edges
4. `_aligned_series()` - 8 edges
5. `_adjust_returns()` - 7 edges
6. `annual_return()` - 7 edges
7. `alpha_aligned()` - 7 edges
8. `default_returns_func()` - 7 edges
9. `NotThisMethod` - 6 edges
10. `gpd_risk_estimates_aligned()` - 6 edges

## Surprising Connections (you probably didn't know these)
- `alpha_aligned()` --calls--> `_adjust_returns()`  [EXTRACTED]
  stats.py → stats.py  _Bridges community 2 → community 4_
- `annual_return()` --calls--> `annualization_factor()`  [EXTRACTED]
  stats.py → stats.py  _Bridges community 5 → community 4_
- `gpd_risk_estimates()` --calls--> `_aligned_series()`  [EXTRACTED]
  stats.py → stats.py  _Bridges community 7 → community 2_
- `gpd_risk_estimates_aligned()` --calls--> `gpd_loglikelihood_minimizer_aligned()`  [EXTRACTED]
  stats.py → stats.py  _Bridges community 7 → community 3_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.07
Nodes (39): Exception, get_config(), get_keywords(), get_versions(), git_get_keywords(), git_pieces_from_vcs(), git_versions_from_keywords(), NotThisMethod (+31 more)

### Community 1 - "Community 1"
Cohesion: 0.10
Nodes (29): _1_bday_ago(), cache_dir(), data_path(), default_returns_func(), down(), ensure_directory(), get_fama_french(), get_returns_cached() (+21 more)

### Community 2 - "Community 2"
Cohesion: 0.12
Nodes (20): _aligned_series(), alpha(), alpha_aligned(), alpha_beta(), alpha_beta_aligned(), beta(), beta_aligned(), beta_fragility_heuristic() (+12 more)

### Community 3 - "Community 3"
Cohesion: 0.22
Nodes (8): gpd_loglikelihood(), gpd_loglikelihood_factory(), gpd_loglikelihood_minimizer_aligned(), gpd_loglikelihood_scale_and_shape(), gpd_loglikelihood_scale_and_shape_factory(), gpd_loglikelihood_scale_only(), gpd_loglikelihood_scale_only_factory(), # NOTE: The usual formula for covariance is::

### Community 4 - "Community 4"
Cohesion: 0.18
Nodes (14): _adjust_returns(), annual_volatility(), annualization_factor(), downside_risk(), excess_sharpe(), Returns the returns series adjusted by adjustment_factor. Optimizes for the, Return annualization factor from period entered or if a custom     value is pass, Determines the annual volatility of a strategy.      Parameters     ---------- (+6 more)

### Community 5 - "Community 5"
Cohesion: 0.14
Nodes (14): annual_return(), cagr(), calmar_ratio(), capture(), cum_returns(), cum_returns_final(), max_drawdown(), Compute capture ratio.      Parameters     ----------     returns : pd.Series or (+6 more)

### Community 6 - "Community 6"
Cohesion: 0.33
Nodes (6): down_capture(), Compute the capture ratio for periods when the benchmark return is positive, Compute the capture ratio for periods when the benchmark return is negative, Computes the ratio of up_capture to down_capture.      Parameters     ----------, up_capture(), up_down_capture()

### Community 7 - "Community 7"
Cohesion: 0.33
Nodes (6): gpd_es_calculator(), gpd_risk_estimates(), gpd_risk_estimates_aligned(), gpd_var_calculator(), Estimate VaR and ES using the Generalized Pareto Distribution (GPD)      Paramet, Estimate VaR and ES using the Generalized Pareto Distribution (GPD)      Paramet

### Community 8 - "Community 8"
Cohesion: 0.50
Nodes (4): compute_exposures(), perf_attrib(), Compute daily risk factor exposures.      Parameters     ----------     position, Attributes the performance of a returns stream to a set of risk factors.      Pe

### Community 9 - "Community 9"
Cohesion: 0.50
Nodes (3): deprecated(), Utilities for marking deprecated functions., Used to mark a function as deprecated.     Parameters     ----------     msg : s

### Community 10 - "Community 10"
Cohesion: 1.00
Nodes (2): aggregate_returns(), Aggregates returns by week, month, or year.      Parameters     ----------     r

### Community 11 - "Community 11"
Cohesion: 1.00
Nodes (2): conditional_value_at_risk(), Conditional value at risk (CVaR) of a returns stream.      CVaR measures the exp

### Community 12 - "Community 12"
Cohesion: 1.00
Nodes (2): down_alpha_beta(), Computes alpha and beta for periods when the benchmark return is negative.

### Community 13 - "Community 13"
Cohesion: 1.00
Nodes (2): omega_ratio(), Determines the Omega ratio of a strategy.      Parameters     ----------     ret

### Community 14 - "Community 14"
Cohesion: 1.00
Nodes (2): Determines R-squared of a linear fit to the cumulative     log returns. Computes, stability_of_timeseries()

### Community 15 - "Community 15"
Cohesion: 1.00
Nodes (2): Determines the ratio between the right (95%) and left tail (5%).      For exampl, tail_ratio()

### Community 16 - "Community 16"
Cohesion: 1.00
Nodes (2): Compute simple returns from a timeseries of prices.      Parameters     --------, simple_returns()

### Community 17 - "Community 17"
Cohesion: 1.00
Nodes (2): Computes alpha and beta for periods when the benchmark return is positive., up_alpha_beta()

### Community 18 - "Community 18"
Cohesion: 1.00
Nodes (2): Computes the up capture measure over a rolling window.     see documentation for, roll_up_capture()

### Community 19 - "Community 19"
Cohesion: 1.00
Nodes (2): Computes the down capture measure over a rolling window.     see documentation f, roll_down_capture()

### Community 20 - "Community 20"
Cohesion: 1.00
Nodes (2): Computes the up/down capture measure over a rolling window.     see documentatio, roll_up_down_capture()

### Community 21 - "Community 21"
Cohesion: 1.00
Nodes (2): Value at risk (VaR) of a returns stream.      Parameters     ----------     retu, value_at_risk()

### Community 22 - "Community 22"
Cohesion: 1.00
Nodes (2): Convert an array-like to a pandas object.      Parameters     ----------     ob, _to_pandas()

## Knowledge Gaps
- **78 isolated node(s):** `Get the keywords needed to look up the version information.`, `Container for Versioneer configuration parameters.`, `Create, populate and return the VersioneerConfig() object.`, `Exception raised if a method is not valid for the current scenario.`, `Decorator to mark a method as the handler for a particular VCS.` (+73 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 10`** (2 nodes): `aggregate_returns()`, `Aggregates returns by week, month, or year.      Parameters     ----------     r`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (2 nodes): `conditional_value_at_risk()`, `Conditional value at risk (CVaR) of a returns stream.      CVaR measures the exp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (2 nodes): `down_alpha_beta()`, `Computes alpha and beta for periods when the benchmark return is negative.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (2 nodes): `omega_ratio()`, `Determines the Omega ratio of a strategy.      Parameters     ----------     ret`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (2 nodes): `Determines R-squared of a linear fit to the cumulative     log returns. Computes`, `stability_of_timeseries()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (2 nodes): `Determines the ratio between the right (95%) and left tail (5%).      For exampl`, `tail_ratio()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (2 nodes): `Compute simple returns from a timeseries of prices.      Parameters     --------`, `simple_returns()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 17`** (2 nodes): `Computes alpha and beta for periods when the benchmark return is positive.`, `up_alpha_beta()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (2 nodes): `Computes the up capture measure over a rolling window.     see documentation for`, `roll_up_capture()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (2 nodes): `Computes the down capture measure over a rolling window.     see documentation f`, `roll_down_capture()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (2 nodes): `Computes the up/down capture measure over a rolling window.     see documentatio`, `roll_up_down_capture()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (2 nodes): `Value at risk (VaR) of a returns stream.      Parameters     ----------     retu`, `value_at_risk()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (2 nodes): `Convert an array-like to a pandas object.      Parameters     ----------     ob`, `_to_pandas()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `_aligned_series()` connect `Community 2` to `Community 3`, `Community 7`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **What connects `Get the keywords needed to look up the version information.`, `Container for Versioneer configuration parameters.`, `Create, populate and return the VersioneerConfig() object.` to the rest of the system?**
  _78 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.07435897435897436 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.0967741935483871 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.11578947368421053 - nodes in this community are weakly interconnected._
- **Should `Community 5` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._