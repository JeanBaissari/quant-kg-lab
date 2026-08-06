---
name: scipy
description: "Use when working with SciPy. Router indexing the 3 scipy sub-skills; load the sub-skill for the module you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scipy/scipy
source_commit: 0514ef9e73297ef8d6f46379731eedc619f9d201
extraction_date: 2026-07-29
graph:
  nodes: 31042
  edges: 51352
  community_count: 1929
  graph_hash: 4a63d9a8dfdca80b
tags: [scipy]
related_skills: [scipy-optimize, scipy-signal, scipy-stats]
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
- Knowledge graph: scipy, 31042 nodes, 51352 edges, 1929 communities
- Rebuild: `scripts/rebuild_graph.sh scipy` (pinned commit 0514ef9e7329)
