---
name: arch-bootstrap
description: "Use when resampling statistics with arch \u2014 stationary/circular\
  \ block bootstrap for confidence intervals on estimators."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: bashtage/arch
source_commit: 704bb70e48372e3ccccdde7da379811657ad0224
extraction_date: 2026-08-12
graph:
  nodes: 1367
  edges: 3900
  community_count: 135
  graph_hash: e3f8bcd939a66a6d
tags:
- arch
- bootstrap
- resampling
related_skills:
- arch
- arch-volatility
- scipy-stats
---

# arch.bootstrap

Block-bootstrap resampling: `StationaryBootstrap` / `CircularBlockBootstrap`
with a `conf_int` helper for percentile confidence intervals on any statistic.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `bootstrap/base.py` | Bootstrap base: `conf_int(stat_func, reps)` percentile intervals |
| `StationaryBootstrap` | `bootstrap/base.py` | Politis-Romano stationary bootstrap (random block lengths) |
| `CircularBlockBootstrap` | `bootstrap/base.py` | Fixed-length circular block resampling |
| `_samplers_python.py` | `bootstrap/_samplers_python.py` | Pure-Python sampler implementations (Cython `_samplers.pyx` is curated-absent) |
| `multiple_comparison.py` | `bootstrap/multiple_comparison.py` | Multiple-comparison adjusted intervals (SMM) |

## Common Patterns

- **CI on a statistic**: `bs = StationaryBootstrap(series); ci = bs.conf_int(fn, 1000)`.
- **Volatility parameter CIs**: bootstrap `res.params` distributions for ARCH fits.
- **Multiple testing**: use `multiple_comparison` when evaluating several statistics.

## Pitfalls

- **Block-length sensitivity**: stationary bootstrap's mean block length matters — compare
  with circular blocks.
- **Determinism**: set `random_state` for reproducible intervals.
- **Cython note**: the fast samplers (`_samplers.pyx`) are curated-absent per ADR-0008; the
  Python samplers are equivalent for typical sizes.

## Provenance

Graph: `knowledge_graphs/arch/.graphify/graph.json` — 1367 nodes · 3900 edges ·
135 communities · graphify @ 704bb70e4837, backend opencode, description coverage 94.3%.

## Verification Checklist

- [ ] `StationaryBootstrap(series).conf_int(np.mean, 500)` runs
