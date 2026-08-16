---
name: pyfolio
description: "Use when working with pyfolio \u2014 the portfolio-reporting entry point.\
  \ Router indexing the pyfolio sub-skills; load the sub-skill for the reporting layer\
  \ you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: quantopian/pyfolio
source_commit: 4b901f6d73aa02ceb6d04b7d83502e5c6f2e81aa
extraction_date: 2026-08-12
graph:
  nodes: 305
  edges: 361
  community_count: 61
  graph_hash: cc432015b7700967
tags:
- pyfolio
- router
related_skills:
- pyfolio-tearsheets
- pyfolio-timeseries
- alphalens
target_version: '0.9.2 (dev: after 0.9.2)'
upstream_status: dead
---

## Version Note

> ⚠️ **Upstream is frozen** (no commits since the pin). This skill describes `pyfolio` at its pinned commit — an abandoned release line. Target version: 0.9.2 (dev: after 0.9.2). Verify against your installed version before use.

# pyfolio

Portfolio performance and risk tear sheets — the reporting layer fed by
alphalens factor analysis.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [tearsheets](tearsheets/SKILL.md) | create_returns/full/position/transaction/round-trip tear sheets |
| [timeseries](timeseries/SKILL.md) | perf_stats, rolling_sharpe, drawdown analytics |

## Common Patterns

- **Pipeline**: alphalens factor analysis → `create_pyfolio_input` → pyfolio tear sheets.
- **Strategy review**: `perf_stats` table + full tear sheet per strategy version.

## Provenance

Graph: `knowledge_graphs/pyfolio/.graphify/graph.json` — 305 nodes · 361 edges ·
61 communities · graphify @ 4b901f6d73aa, backend opencode, description coverage 80.4%.

## Verification Checklist

- [ ] Router links resolve to the 2 module skills
- [ ] `related_skills` names resolve to real skills
