---
name: polars-expressions
description: "Use when building polars expression pipelines — col, select/filter/with_columns, group_by aggregations, window functions, and join/reshape operations."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: pola-rs/polars
source_commit: 1f779c90256872c50a16622ce0e4e4f11e885b1a
extraction_date: 2026-08-12
graph:
  nodes: 5296
  edges: 16925
  community_count: 485
  graph_hash: 4c9e707cde1bc95a
tags:
- polars
- expressions
- query
related_skills:
- polars
- polars-dataframe
- polars-performance
---

# polars.expressions

The expression API: compose operations as expressions, not string column names —
`pl.col("x")`, `select`/`filter`/`with_columns`, `group_by().agg()`, window
functions, and joins.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `col` | `functions/col.py:L154` | Expression constructor: `pl.col("name")` |
| `select` / `with_columns` | `functions/lazy.py:L2344` | Expression application — project or add columns |
| `group_by` | `lazyframe/group_by.py:L24` | Grouped aggregation: `df.group_by("k").agg(pl.col("v").mean())` |
| `Expr` | `expr/expr.py:L135` | Expression class — deg 254 hub: .mean/.sum/.rank/.shift/.diff/.over/.rolling |
| `lit` | `functions/lit.py:L31` | Constant expression — `pl.lit(1.0)` |
| `when` / `then` / `otherwise` | `functions/whenthen.py:L18` | Conditional expression — `pl.when(c).then(a).otherwise(b)` |
| `concat` | `functions/` | Horizontal/vertical frame concat — `pl.concat([df1, df2])` | `functions/eager.py:L64` |

| `Expr.cast` | `expr/expr.py:L2181` | Type cast — `pl.col("v").cast(pl.Float64)` |
| `Expr.rank` | `expr/expr.py:L9860` | Rank — `.rank(method="average"\|"min"\|"dense")` |
| `Expr.over` | `expr/expr.py:L4110` | Window clause — `.rank().over("date")` |
| `Expr.rolling_*` | `expr/expr.py:L135` | Rolling aggregations — `.rolling_mean(20)` etc. |
| `Expr.shift` / `Expr.diff` | `expr/expr.py:L3164` | Lag / first-difference — return construction |
| `Expr.ewm_*` | `expr/expr.py:L135` | Exponentially weighted — `.ewm_mean(span=20)` |
| `Expr.qcut` / `Expr.cut` | `expr/expr.py:L4777` | Quantile binning — factor-quantile building |
| `Expr.filter` | `expr/expr.py:L4984` | Row filter inside expressions |
| `Expr.is_nan` / `Expr.is_null` | `expr/expr.py:L1290` | Missing-value masks |
| `Expr.str` | `expr/string.py:L45` | String namespace — `.str.starts_with/.contains/.to_datetime` |
| `Expr.dt` | `expr/datetime.py:L38` | Datetime namespace — `.dt.month/.dt.weekday/.dt.round` |
| `Expr.arr` | `expr/list.py:L29` | List namespace — `.arr.explode/.arr.first/.arr.sum` |
| `functions/aggregation` | `functions/aggregation/` | Aggregate constructors — horizontal/vertical reductions |
| `functions/range` | `functions/range/` | Range constructors — int_range, date_range, datetime_range |

## Common Patterns

- **Ranked factors**: `df.with_columns(pl.col("ret").rank().over("date"))` — per-date ranks
  via the `over` window clause.
- **Grouped stats**: `df.group_by("asset").agg(pl.col("ret").mean(), pl.col("ret").std())`.
- **Shifts/diffs**: `pl.col("px").shift(1)` / `.diff()` — return construction.
- **Casting**: `pl.col("v").cast(pl.Float64)` — explicit, no silent coercion.
- **Joins**: `df1.join(df2, on="asset", how="left")`.
- **Conditional factors**: `pl.when(pl.col("ret") > 0).then(1).otherwise(-1)`.
- **Rolling volatility**: `pl.col("ret").rolling_std(20)` — or per-group with
  `.over("asset")`.
- **Factor quantiles**: `pl.col("ret").qcut(5, labels=["q1".."q5"])` — equal-count bins
  for cross-sectional portfolio construction.
- **Time features**: `pl.col("date").dt.month().alias("month")` — calendar features.
- **String preprocessing**: `pl.col("ticker").str.to_uppercase()`, `.str.replace(...)`.
- **NaN handling**: `.fill_null(0)` / `.drop_nans()` — explicit missing-value policy.

## Pitfalls

- **Eager vs lazy window**: `over()` in lazy plans computes per group — verify partition
  semantics for rolling uses.
- **Column pruning**: unused columns in lazy plans are not materialized — results may
  differ from eager expectations when inspecting intermediates.
- **`alias` after window**: `.rank().over("date").alias("r")` — without alias the
  result column name is derived from the full expression and can be awkward to join on.
- **`when` without `otherwise`**: unmatched rows become null, not zero — be explicit.
- **rolling windows are centered by default in some `rolling_*` variants**: check the
  `center`/`window_size` arguments for look-ahead bias in backtests.
- **`str`/`dt` namespaces only on the right dtype**: calling `.dt.*` on a non-datetime
  column raises — cast first (`pl.col("date").cast(pl.Datetime)`).

## Provenance

Graph: `knowledge_graphs/polars/.graphify/graph.json` — 5296 nodes · 16925 edges ·
485 communities · graphify @ 1f779c902568, backend opencode, description coverage 81.6%.

## Verification Checklist

- [ ] `df.with_columns(pl.col("ret").rank().over("date"))` ranks per date
