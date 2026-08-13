---
name: polars-performance
description: "Use when optimizing polars pipelines — lazy execution, scan/sink streaming, query planning, and parallelization."
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
- performance
- lazy
related_skills:
- polars
- polars-dataframe
- polars-expressions
---

# polars.performance

The lazy execution model: `LazyFrame` query plans, `scan_*`/`sink_*` streaming,
optimization flags, and the parallelism rules behind polars' speed.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `LazyFrame` | `lazyframe/base.py` | Lazy query plan — optimized and executed by collect()/sink_* |
| `QueryOptFlags` | `lazyframe/opt_flags.py` | Optimization flags (predicate pushdown, projection pushdown) |
| `scan_parquet` / `sink_parquet` | `lazyframe/` + `io/` | Streaming read/write — constant memory |
| `collect()` | `lazyframe/frame.py` | Executes the plan eagerly |
| `config.py` | `config.py` | Module: global configuration (threads, streaming toggle) |

## Common Patterns

- **Lazy pipeline**: `pl.scan_parquet(dir).filter(...).group_by(...).agg(...).collect()` —
  pushdowns happen automatically.
- **Big-data streaming**: `sink_parquet("out.parquet")` instead of `collect()` for
  out-of-memory datasets.
- **Verify the plan**: `lf.explain()` — check pushdown actually happened.
- **Threads**: `pl.Config.set_tbl_rows` / thread control for constrained hosts.

## Pitfalls

- **Over-partitioning**: thousands of tiny files slow scans — use `pl.scan_parquet` on
  coarser files.
- **collect() materializes**: for huge results prefer sink or `collect(streaming=True)`.

## Provenance

Graph: `knowledge_graphs/polars/.graphify/graph.json` — 5296 nodes · 16925 edges ·
485 communities · graphify @ 1f779c902568, backend opencode, description coverage 81.6%.

## Verification Checklist

- [ ] `pl.scan_parquet(dir).explain()` shows predicate pushdown
