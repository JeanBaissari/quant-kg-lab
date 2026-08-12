---
name: numpy
description: Use when working with NumPy. Router indexing the 3 numpy sub-skills;
  load the sub-skill for the module you need.
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
source_commit: ab2199763cb17878cd8f34fcbc97106c5397f922
extraction_date: 2026-07-29
graph:
  nodes: 8104
  edges: 13281
  community_count: 670
  graph_hash: 65eb865357d8f26a
tags:
- numpy
related_skills:
- numpy-core
- numpy-linalg
- numpy-random
---

# NumPy (router)

Indexes the 3 spec-driven NumPy sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [numpy-core](core/SKILL.md) | `numpy.core` | NumPy arrays |
| [numpy-linalg](linalg/SKILL.md) | `numpy.linalg` | linear algebra with NumPy |
| [numpy-random](random/SKILL.md) | `numpy.random` | random numbers with NumPy |

## Provenance

- Knowledge graph: numpy, 8094 nodes, 13271 edges, 670 communities
- God nodes: `ABCPolyBase` (251), `MaskedArray` (151), `f2c_d_lapack.c` (124) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ ab2199763cb1, backend opencode, description coverage 83%
