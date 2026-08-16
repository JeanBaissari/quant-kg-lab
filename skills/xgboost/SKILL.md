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
  graph_hash: 47615a42dd12a0a8
tags:
- xgboost
related_skills:
- xgboost-core
- xgboost-sklearn
target_version: '3.3.0 (dev: after 3.3.0, before 3.4.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `xgboost` ahead of the latest PyPI release (3.3.0 (dev: after 3.3.0, before 3.4.0)). Some APIs may not exist in your installed version.

# XGBoost (router)

Indexes the 2 spec-driven XGBoost sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [xgboost-core](core/SKILL.md) | `xgboost.core` | XGBoost native API |
| [xgboost-sklearn](sklearn/SKILL.md) | `xgboost.sklearn` | XGBoost scikit-learn wrappers |

## Provenance

- Knowledge graph: xgboost, 1631 nodes, 4318 edges, 80 communities
- God nodes: `Categories` (179), `DMatrix` (161), `Objective` (146) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 2a4786e61e08, backend opencode, description coverage 84%
