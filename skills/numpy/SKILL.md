---
name: numpy
description: Use when working with NumPy. Router indexing the 5 numpy sub-skills;
  load the sub-skill for the module you need.
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
source_commit: ab2199763cb17878cd8f34fcbc97106c5397f922
extraction_date: 2026-07-29
graph:
  nodes: 8306
  edges: 13483
  community_count: 619
  graph_hash: 9ea08f5479cbb7c7
tags:
- numpy
related_skills:
- numpy-core
- numpy-ufuncs
- numpy-io
- numpy-linalg
- numpy-random
target_version: '2.5.1 (dev: after 2.5.1, before 2.5.2)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `numpy` ahead of the latest PyPI release (2.5.1 (dev: after 2.5.1, before 2.5.2)). Some APIs may not exist in your installed version.

# NumPy (router)

Indexes the 5 spec-driven NumPy sub-skills. Load the one for the module you need.

## Sub-skills
| Skill | Module | Covers |
|-------|--------|--------|
| [numpy-core](core/SKILL.md) | `numpy.core` | NumPy arrays — creation, indexing, dtype |
| [numpy-ufuncs](ufuncs/SKILL.md) | `numpy.ufuncs` | element-wise ufuncs, broadcasting, einsum |
| [numpy-io](io/SKILL.md) | `numpy.io` | loadtxt/save/load/memmap persistence |
| [numpy-linalg](linalg/SKILL.md) | `numpy.linalg` | linear algebra with NumPy |
| [numpy-random](random/SKILL.md) | `numpy.random` | random numbers with NumPy |

## Provenance

- Knowledge graph: numpy, 8094 nodes, 13271 edges, 670 communities
- God nodes: `ABCPolyBase` (251), `MaskedArray` (151), `f2c_d_lapack.c:L1` (124) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ ab2199763cb1, backend opencode, description coverage 83%
