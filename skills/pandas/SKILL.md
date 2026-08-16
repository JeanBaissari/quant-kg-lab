---
name: pandas
description: Use when working with pandas. Router indexing the 2 pandas sub-skills;
  load the sub-skill for the module you need.
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: pandas-dev/pandas
source_commit: 982854070758cd2015fc9e64395684546b1c5444
extraction_date: 2026-07-29
graph:
  nodes: 11368
  edges: 39913
  community_count: 396
  graph_hash: e0d7084604dec6e0
tags:
- pandas
related_skills:
- pandas-core
- pandas-ts
- pandas-groupby
---

# pandas (router)

Indexes the 2 spec-driven pandas sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [pandas-core](core/SKILL.md) | `pandas.core` | tabular data with pandas |
| [pandas-ts](ts/SKILL.md) | `pandas.ts` | pandas time series |
| [pandas-groupby](groupby/SKILL.md) | `pandas.groupby` | split-apply-combine, group stats, resampling |

## Provenance

- Knowledge graph: pandas, 11368 nodes, 39913 edges, 410 communities
- God nodes: `DatetimeTZDtype` (1582), `CategoricalDtype` (1480), `PeriodDtype` (1087) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 982854070758, backend opencode, description coverage 81%
