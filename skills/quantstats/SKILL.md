---
name: quantstats
description: "Use when working with quantstats \u2014 the portfolio-analytics entry\
  \ point. Router indexing the quantstats sub-skills; load the sub-skill for the layer\
  \ you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: ranaroussi/quantstats
source_commit: fbd10daed0227aa0d10da6513f1b15e7e98d7fae
extraction_date: 2026-08-13
graph:
  nodes: 393
  edges: 531
  community_count: 51
  graph_hash: 98393f286b04d0d2
tags:
- quantstats
- router
- analytics
- reporting
related_skills:
- quantstats-stats
- quantstats-reports
- quantstats-plots
- empyrical-stats
- pyfolio-timeseries
- pandas-core
target_version: 0.0.81 (released tag v0.0.81)
upstream_status: stale
---

# quantstats

Portfolio analytics + HTML tear-sheet reporting: statistics (incl. empyrical's metric
layer), full reports, and plotting — the reporting layer of the quant stack.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [stats](stats/SKILL.md) | sharpe/sortino/cagr/max_drawdown/VaR/CVaR/kelly/win-rate/ulcer — the metric surface |
| [reports](reports/SKILL.md) | metrics()/full()/html()/basic() — HTML tear-sheet generation |
| [plots](plots/SKILL.md) | returns/drawdown/rolling/distribution heatmaps + plotly/matplotlib backends |

## Common Patterns

- **Quick report**: `qs.reports.full(returns, benchmark)` — one call, full HTML tear sheet.
- **Metric table**: `qs.stats.metrics(returns)` — the whole table in one call.
- **Benchmark mapping**: `qs.utils._prepare_benchmark` / `qs.utils.to_prices` for
  benchmark series alignment.

## Provenance

Graph: `knowledge_graphs/quantstats/.graphify/graph.json` — 393 nodes · 531 edges ·
48 communities · graphify @ fbd10daed022, backend opencode, description coverage 93.5%.

## Verification Checklist

- [ ] Router links resolve to the 3 module skills
- [ ] `related_skills` names resolve to real skills
