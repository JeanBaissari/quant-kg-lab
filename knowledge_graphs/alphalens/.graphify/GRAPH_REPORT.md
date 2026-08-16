# Graph Report - knowledge_graphs/alphalens/repo/alphalens  (2026-08-13)

## Corpus Check
- Corpus is ~15,679 words - fits in a single context window. You may not need a graph.

## Summary
- 172 nodes · 231 edges · 5 communities detected
- Non-singleton communities: 5
- Extraction: EXTRACTED: 100.0%
- Edge kinds: calls: 62 · contains: 83 · imports_from: 1 · inherits: 4 · method: 4 · rationale_for: 77

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 6 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `77084f1`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `plotting.py` (21)
- `_version.py` (20)
- `utils.py` (19)
- `performance.py` (16)
- `GridFigure` (13)
- `render()` (9)
- `tears.py` (8)
- `get_versions()` (8)
- `create_event_returns_tear_sheet()` (7)
- `create_information_tear_sheet()` (7)

## Surprising Connections (you probably didn't know these)
- `NotThisMethod` --inherits--> `Exception`  [EXTRACTED]
  _version.py →   _Bridges community 0 → community 2_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.07
Nodes (38): get_config(), get_keywords(), get_versions(), git_get_keywords(), git_pieces_from_vcs(), git_versions_from_keywords(), NotThisMethod, plus_or_dot() (+30 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (34): axes_style(), customize(), plot_cumulative_returns(), plot_cumulative_returns_by_quantile(), plot_events_distribution(), plot_factor_rank_auto_correlation(), plot_ic_by_group(), plot_ic_hist() (+26 more)

### Community 2 - "Community 2"
Cohesion: 0.07
Nodes (37): Exception, add_custom_calendar_timedelta(), backshift_returns_series(), compute_forward_returns(), demean_forward_returns(), diff_custom_calendar_timedeltas(), get_clean_factor(), get_clean_factor_and_forward_returns() (+29 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (32): average_cumulative_return_by_quantile(), common_start_returns(), compute_mean_returns_spread(), create_pyfolio_input(), cumulative_returns(), factor_alpha_beta(), factor_cumulative_returns(), factor_information_coefficient() (+24 more)

### Community 4 - "Community 4"
Cohesion: 0.20
Nodes (17): object, create_event_returns_tear_sheet(), create_event_study_tear_sheet(), create_full_tear_sheet(), create_information_tear_sheet(), create_returns_tear_sheet(), create_summary_tear_sheet(), create_turnover_tear_sheet() (+9 more)

## Knowledge Gaps
- **77 isolated node(s):** `Get the keywords needed to look up the version information.`, `Container for Versioneer configuration parameters.`, `Create, populate and return the VersioneerConfig() object.`, `Exception raised if a method is not valid for the current scenario.`, `Decorator to mark a method as the handler for a particular VCS.` (+72 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `NotThisMethod` connect `Community 0` to `Community 2`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **What connects `Get the keywords needed to look up the version information.`, `Container for Versioneer configuration parameters.`, `Create, populate and return the VersioneerConfig() object.` to the rest of the system?**
  _77 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.07435897435897436 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.05128205128205128 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.06685633001422475 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.07765151515151515 - nodes in this community are weakly interconnected._