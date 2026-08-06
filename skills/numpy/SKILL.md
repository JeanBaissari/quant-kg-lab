---
name: numpy
description: "Use when working with NumPy. Router indexing the 3 numpy sub-skills; load the sub-skill for the module you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
source_commit: ab2199763cb17878cd8f34fcbc97106c5397f922
extraction_date: 2026-07-29
graph:
  nodes: 20436
  edges: 30581
  community_count: 1561
  graph_hash: 96ded7dfb2ac7d28
tags: [numpy]
related_skills: [numpy-core, numpy-linalg, numpy-random]
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
- Knowledge graph: numpy, 20436 nodes, 30581 edges, 1561 communities
- Rebuild: `scripts/rebuild_graph.sh numpy` (pinned commit ab2199763cb1)
