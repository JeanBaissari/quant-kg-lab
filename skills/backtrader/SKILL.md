---
name: backtrader
description: Use when working with backtrader. Router indexing the 2 backtrader sub-skills;
  load the sub-skill for the module you need.
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: mementum/backtrader
source_commit: b853d7c90b6721476eb5a5ea3135224e33db1f14
extraction_date: 2026-07-29
graph:
  nodes: 2680
  edges: 4964
  community_count: 206
  graph_hash: 58f821144ba4d073
tags:
- backtrader
related_skills:
- backtrader-analyzers
- backtrader-core
target_version: 1.9.78.123 (untagged, on release day)
upstream_status: dead
---

## Version Note

> ⚠️ **Upstream is frozen** (no commits since the pin). This skill describes `backtrader` at its pinned commit — an abandoned release line. Target version: 1.9.78.123 (untagged, on release day). Verify against your installed version before use.

# backtrader (router)

Indexes the 2 spec-driven backtrader sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [backtrader-analyzers](analyzers/SKILL.md) | `backtrader.analyzers` | performance analyzers to a backtrader strategy |
| [backtrader-core](core/SKILL.md) | `backtrader.core` | event-driven backtests with backtrader |

## Provenance

- Knowledge graph: backtrader, 2680 nodes, 4964 edges, 206 communities
- God nodes: `MetaParams` (260), `LineRoot` (119), `LineSingle` (111) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ b853d7c90b67, backend opencode, description coverage 84%
