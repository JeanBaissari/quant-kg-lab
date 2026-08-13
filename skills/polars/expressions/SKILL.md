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
| `col` | `functions/col.py` | Expression constructor: `pl.col("name")` |
| `select` / `with_columns` | `dataframe/base.py` | Expression application — project or add columns |
| `group_by` | `dataframe/base.py` | Grouped aggregation: `df.group_by("k").agg(pl.col("v").mean())` |
| `functions/` | `functions/` | Expression constructors: col, lit, concat, range, duration helpers |
| `expr/` | `expr/` | Expression classes: Expr with .mean/.sum/.rank/.shift/.diff |
| `datatype_expr/` | `datatype_expr/` | Datatype-related expressions (cast, dtype checks) |

## Common Patterns

- **Ranked factors**: `df.with_columns(pl.col("ret").rank().over("date"))` — per-date ranks
  via the `over` window clause.
- **Grouped stats**: `df.group_by("asset").agg(pl.col("ret").mean(), pl.col("ret").std())`.
- **Shifts/diffs**: `pl.col("px").shift(1)` / `.diff()` — return construction.
- **Casting**: `pl.col("v").cast(pl.Float64)` — explicit, no silent coercion.
- **Joins**: `df1.join(df2, on="asset", how="left")`.

## Pitfalls

- **Eager vs lazy window**: `over()` in lazy plans computes per group — verify partition
  semantics for rolling uses.
- **Column pruning**: unused columns in lazy plans are not materialized — results may
  differ from eager expectations when inspecting intermediates.

## Provenance

Graph: `knowledge_graphs/polars/.graphify/graph.json` — 5296 nodes · 16925 edges ·
485 communities · graphify @ 1f779c902568, backend opencode, description coverage 81.6%.

## Verification Checklist

- [ ] `df.with_columns(pl.col("ret").rank().over("date"))` ranks per date
