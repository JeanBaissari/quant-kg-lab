---
name: scipy
description: Use when working with SciPy. Router indexing the 3 scipy sub-skills;
  load the sub-skill for the module you need.
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scipy/scipy
source_commit: 0514ef9e73297ef8d6f46379731eedc619f9d201
extraction_date: 2026-07-29
graph:
  nodes: 14071
  edges: 23466
  community_count: 1076
  graph_hash: 1c051b3be2968b39
tags:
- scipy
related_skills:
- scipy-optimize
- scipy-signal
- scipy-stats
---

# SciPy (router)

Indexes the 3 spec-driven SciPy sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [scipy-optimize](optimize/SKILL.md) | `scipy.optimize` | optimization or root-finding problems with SciPy |
| [scipy-signal](signal/SKILL.md) | `scipy.signal` | signals with SciPy |
| [scipy-stats](stats/SKILL.md) | `scipy.stats` | statistics with SciPy |

## Provenance

- Knowledge graph: scipy, 14071 nodes, 23466 edges, 1076 communities
- God nodes: `CensoredData` (342), `FitError` (320), `rv_continuous` (278) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 0514ef9e7329, backend opencode, description coverage 81%
