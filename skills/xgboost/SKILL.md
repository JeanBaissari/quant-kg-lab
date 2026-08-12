---
name: xgboost
description: Use when working with XGBoost. Router indexing the 2 xgboost sub-skills;
  load the sub-skill for the module you need.
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: dmlc/xgboost
source_commit: 2a4786e61e08b41f63916089c35a10d0ac4626d2
extraction_date: 2026-07-29
graph:
  nodes: 1631
  edges: 4318
  community_count: 80
  graph_hash: fe8085677fab40cf
tags:
- xgboost
related_skills:
- xgboost-core
- xgboost-sklearn
---

# XGBoost (router)

Indexes the 2 spec-driven XGBoost sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [xgboost-core](core/SKILL.md) | `xgboost.core` | XGBoost native API |
| [xgboost-sklearn](sklearn/SKILL.md) | `xgboost.sklearn` | XGBoost scikit-learn wrappers |

## Provenance
- Knowledge graph: xgboost, 1632 nodes, 4415 edges, 80 communities
- Rebuild: `scripts/rebuild_graph.sh xgboost` (pinned commit 2a4786e61e08)
