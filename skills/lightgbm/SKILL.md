---
name: lightgbm
description: "Use when working with LightGBM. Router indexing the 2 lightgbm sub-skills; load the sub-skill for the module you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: microsoft/LightGBM
source_commit: f9bf8d1358cd7b5d649b47175e56543b62856f98
extraction_date: 2026-07-29
graph:
  nodes: 2952
  edges: 5138
  community_count: 176
  graph_hash: 063abd3af521a2d7
tags: [lightgbm]
related_skills: [lightgbm-core, lightgbm-sklearn]
---

# LightGBM (router)

Indexes the 2 spec-driven LightGBM sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [lightgbm-core](core/SKILL.md) | `lightgbm.core` | LightGBM native API |
| [lightgbm-sklearn](sklearn/SKILL.md) | `lightgbm.sklearn` | LightGBM scikit-learn wrappers |

## Provenance
- Knowledge graph: lightgbm, 2952 nodes, 5138 edges, 176 communities
- Rebuild: `scripts/rebuild_graph.sh lightgbm` (pinned commit f9bf8d1358cd)
