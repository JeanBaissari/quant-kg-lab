---
name: backtrader
description: "Use when working with backtrader. Router indexing the 2 backtrader sub-skills; load the sub-skill for the module you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: mementum/backtrader
source_commit: b853d7c90b6721476eb5a5ea3135224e33db1f14
extraction_date: 2026-07-29
graph:
  nodes: 3458
  edges: 6863
  community_count: 261
  graph_hash: b54e4c68d9bf8f46
tags: [backtrader]
related_skills: [backtrader-analyzers, backtrader-core]
---

# backtrader (router)

Indexes the 2 spec-driven backtrader sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [backtrader-analyzers](analyzers/SKILL.md) | `backtrader.analyzers` | performance analyzers to a backtrader strategy |
| [backtrader-core](core/SKILL.md) | `backtrader.core` | event-driven backtests with backtrader |

## Provenance
- Knowledge graph: backtrader, 3458 nodes, 6863 edges, 261 communities
- Rebuild: `scripts/rebuild_graph.sh backtrader` (pinned commit b853d7c90b67)
