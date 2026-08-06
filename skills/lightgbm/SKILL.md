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
  nodes: 594
  edges: 2099
  community_count: 17
  graph_hash: af871e54ee48be1d
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
- Knowledge graph: lightgbm, 594 nodes, 2099 edges, 17 communities
- Rebuild: `scripts/rebuild_graph.sh lightgbm` (pinned commit f9bf8d1358cd)
