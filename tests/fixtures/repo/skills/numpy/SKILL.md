---
name: numpy
description: "Use when working with NumPy. Fixture router indexing the numpy sub-skills."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
source_commit: ab2199763cb17878cd8f34fcbc97106c5397f922
extraction_date: 2026-08-12
graph:
  nodes: 3
  edges: 0
  community_count: 2
  graph_hash: df564aefc267559e
tags: [numpy]
related_skills: [numpy-core]
---

# NumPy (fixture router)

Router fixture: exempt from the §3 required-section check (SKILL_SPEC §6) — it carries
only a sub-skill index plus provenance.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [numpy-core](core/SKILL.md) | `numpy.core` | arrays |
| [numpy-stalehash](stalehash/SKILL.md) | `numpy.stalehash` | stale hash fixture |
| [numpy-dangling](dangling/SKILL.md) | `numpy.dangling` | dangling related fixture |
| [numpy-badcommit](badcommit/SKILL.md) | `numpy.badcommit` | bad commit fixture |
| [numpy-hallucinated](linalg/SKILL.md) | `numpy.linalg` | hallucinated API fixture |

## Provenance
- Knowledge graph: numpy, 3 nodes, 0 edges, 2 communities
