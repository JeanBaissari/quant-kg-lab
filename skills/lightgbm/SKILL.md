---
name: lightgbm
description: Use when working with LightGBM. Router indexing the 2 lightgbm sub-skills;
  load the sub-skill for the module you need.
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: microsoft/LightGBM
source_commit: f9bf8d1358cd7b5d649b47175e56543b62856f98
extraction_date: 2026-07-29
graph:
  nodes: 593
  edges: 2029
  community_count: 17
  graph_hash: a8013a25fbe34b59
tags:
- lightgbm
related_skills:
- lightgbm-core
- lightgbm-sklearn
---

# LightGBM (router)

Indexes the 2 spec-driven LightGBM sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [lightgbm-core](core/SKILL.md) | `lightgbm.core` | LightGBM native API |
| [lightgbm-sklearn](sklearn/SKILL.md) | `lightgbm.sklearn` | LightGBM scikit-learn wrappers |

## Provenance

- Knowledge graph: lightgbm, 593 nodes, 2029 edges, 17 communities
- God nodes: `pd_DataFrame` (231), `pd_Series` (173), `pd_CategoricalDtype` (142) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ f9bf8d1358cd, backend opencode, description coverage 84%
