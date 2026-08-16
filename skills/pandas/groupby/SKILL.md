---
name: pandas-groupby
description: "Use when doing split-apply-combine with pandas \u2014 DataFrameGroupBy,\
  \ agg/apply/transform, rolling group statistics, and resampling workflows."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: pandas-dev/pandas
source_commit: 982854070758cd2015fc9e64395684546b1c5444
extraction_date: 2026-08-12
graph:
  nodes: 11368
  edges: 39913
  community_count: 396
  graph_hash: e0d7084604dec6e0
tags:
- pandas
- groupby
- split-apply-combine
related_skills:
- pandas-core
- pandas-ts
- pandas
---

# pandas.groupby

Split-apply-combine: group by keys → aggregate/transform/apply → combine.
The quant workhorse for cross-sectional factor portfolios, rolling group
statistics, and resampled metrics.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `GroupBy` | `core/groupby/groupby.py:L752` | Base split-apply-combine object from `df.groupby(keys)` |
| `DataFrameGroupBy` | `core/groupby/generic.py:L2090` | DataFrame groups with agg/transform/apply/filter |
| `SeriesGroupBy` | `core/groupby/generic.py:L193` | Series groups — `.agg`, `.transform`, `.expanding`, `.rolling` |
| `Resampler` | `core/resample.py:L119` | Time-based grouping (`df.resample(freq)`) with the same API |
| `.agg()` | `core/groupby/generic.py:L109` | Named/multiple aggregations per column |
| `.transform()` | `core/groupby/generic.py:L2529` | Same-shape group statistics (demeaning, z-scores) |
| `.rolling()` | `core/window/rolling.py:L1955` | Rolling windows on groups or plain frames |

## Common Patterns

- **Cross-sectional factor ranks**: `df.groupby('date')['ret'].rank(pct=True)` — per-date
  percentile ranks (factor quantiles).
- **Multi-aggregation**: `g = df.groupby(['date', 'sector']); g['ret'].agg(['mean', 'std',
  'count'])`.
- **Demeaning**: `df.groupby('date')['ret'].transform(lambda x: x - x.mean())` — remove the
  market component cross-sectionally.
- **Grouped rolling**: `df.groupby('asset')['ret'].rolling(20).mean()` — per-asset rolling
  mean.
- **Resampling**: `df.resample('W').agg({'ret': 'sum', 'vol': 'mean'})` — weekly
  aggregation of daily data.

## Pitfalls

- **transform vs agg**: `transform` keeps the group shape; `agg` collapses it — mixing them
  breaks alignment.
- **MultiIndex after groupby**: keys land in the index — use `as_index=False` to keep
  columns.
- **Grouped rolling with MultiIndex**: the result keeps the (group, row) index — reset it
  before merging back.
- **`apply` performance**: prefer vectorized `agg`/`transform`; `apply` loops in Python for
  many groups.

## Provenance

Graph: `knowledge_graphs/pandas/.graphify/graph.json` — 11368 nodes · 39913 edges ·
410 communities · graphify @ 982854070758, backend opencode, description coverage 80.9%.

## Verification Checklist

- [ ] `df.groupby('date')['ret'].rank(pct=True)` produces per-date quantiles
- [ ] QR rows cite source files resolvable in the pandas graph
