---
name: pandas
description: "Use when working with pandas. Router indexing the 2 pandas sub-skills; load the sub-skill for the module you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: pandas-dev/pandas
source_commit: 982854070758cd2015fc9e64395684546b1c5444
extraction_date: 2026-07-29
graph:
  nodes: 37983
  edges: 69899
  community_count: 1986
  graph_hash: b70488661b79f085
tags: [pandas]
related_skills: [pandas-core, pandas-ts]
---

# pandas (router)

Indexes the 2 spec-driven pandas sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [pandas-core](core/SKILL.md) | `pandas.core` | tabular data with pandas |
| [pandas-ts](ts/SKILL.md) | `pandas.ts` | pandas time series |

## Provenance
- Knowledge graph: pandas, 37983 nodes, 69899 edges, 1986 communities
- Rebuild: `scripts/rebuild_graph.sh pandas` (pinned commit 982854070758)
