---
name: empyrical
description: "Use when working with empyrical \u2014 the portfolio-metrics entry point.\
  \ Router indexing the empyrical sub-skills; load the sub-skill for the metric family\
  \ you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: Quantopian/empyrical
source_commit: 40f61b4f229df10898d46d08f7b1bdc543c0f99c
extraction_date: 2026-08-13
graph:
  nodes: 180
  edges: 258
  community_count: 23
  graph_hash: 4e2d2ce735db5ea0
tags:
- empyrical
- router
- metrics
related_skills:
- empyrical-stats
- empyrical-perf-attrib
- pyfolio-timeseries
- pyfolio-tearsheets
- pandas-core
target_version: '0.5.5 (dev: after 0.5.5)'
upstream_status: dead
---

## Version Note

> ⚠️ **Upstream is frozen** (no commits since the pin). This skill describes `empyrical` at its pinned commit — an abandoned release line. Target version: 0.5.5 (dev: after 0.5.5). Verify against your installed version before use.

# empyrical

Pure-Python performance-metric primitives (Quantopian lineage): Sharpe/Sortino/omega/
Calmar, drawdown, alpha/beta, downside risk — the metric layer under pyfolio tear sheets.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [stats](stats/SKILL.md) | annual_return/volatility, sharpe/sortino/omega/calmar, max_drawdown, alpha/beta, downside risk, tail ratio, stability |
| [perf-attrib](perf-attrib/SKILL.md) | factor exposure decomposition: perf_attrib, compute_exposures |

## Common Patterns

- **Metric layer for reports**: compute empyrical stats, then hand returns to pyfolio
  tear sheets for the visual layer.
- **Consistent periods**: pass `period='daily'/'weekly'/'monthly'` + `annualization`
  consistently — every metric derives from these.
- **Aligned variants**: `*_aligned` functions compute the metric on the aligned
  intersection of returns and factor series (used internally by pyfolio).

## Provenance

Graph: `knowledge_graphs/empyrical/.graphify/graph.json` — 180 nodes · 258 edges ·
23 communities · graphify @ 40f61b4f229d, backend opencode, description coverage 93.3%.

## Verification Checklist

- [ ] Router links resolve to the 2 module skills
- [ ] `related_skills` names resolve to real skills
