---
name: polars
description: "Use when working with polars — the DataFrame entry point. Router indexing the polars sub-skills; load the sub-skill for the layer you need."
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
- router
related_skills:
- polars-dataframe
- polars-expressions
- polars-performance
- polars-io
- polars-lazyframe
- pandas
- numpy
---

# polars

The Rust-core DataFrame library: eager/lazy dataframes, expression pipelines,
and streaming performance — the high-throughput counterpart to pandas.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [dataframe](dataframe/SKILL.md) | DataFrame/Series, schema, group_by/join/reshape, conversions |
| [expressions](expressions/SKILL.md) | col/select/group_by/window/join expression pipelines |
| [performance](performance/SKILL.md) | LazyFrame plans, scan/sink streaming, optimization flags |
| [io](io/SKILL.md) | read/scan/sink — CSV, Parquet, IPC, JSON, database, cloud |
| [lazyframe](lazyframe/SKILL.md) | LazyFrame plans, collect/sink, SQLContext, query planning |

## Common Patterns

- **Big factor data**: `pl.scan_parquet` → filter/group_by → `collect` — then convert
  selected columns to pandas for model work.
- **Interop**: `df.to_pandas()` / `pl.from_pandas()` at the boundary.

## Provenance

Graph: `knowledge_graphs/polars/.graphify/graph.json` — 5296 nodes · 16925 edges ·
485 communities · graphify @ 1f779c902568, backend opencode, description coverage 81.6%.

## Verification Checklist

- [ ] Router links resolve to the 3 module skills
- [ ] `related_skills` names resolve to real skills
