---
name: vectorbt
description: "Use when working with vectorbt. Router indexing the 3 vectorbt sub-skills; load the sub-skill for the module you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: polakowo/vectorbt
source_commit: f9897528f675114e6b34790178dbb2ca137acb51
extraction_date: 2026-07-29
graph:
  nodes: 3682
  edges: 9212
  community_count: 353
  graph_hash: 0c9c535c173d5a38
tags: [vectorbt]
related_skills: [vectorbt-core, vectorbt-portfolio, vectorbt-signals]
---

# vectorbt (router)

Indexes the 3 spec-driven vectorbt sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [vectorbt-core](core/SKILL.md) | `vectorbt.core` | vectorbt internals |
| [vectorbt-portfolio](portfolio/SKILL.md) | `vectorbt.portfolio` | simulating portfolios with vectorbt |
| [vectorbt-signals](signals/SKILL.md) | `vectorbt.signals` | entry/exit signals with vectorbt |

## Provenance
- Knowledge graph: vectorbt, 3682 nodes, 9212 edges, 353 communities
- Rebuild: `scripts/rebuild_graph.sh vectorbt` (pinned commit f9897528f675)
