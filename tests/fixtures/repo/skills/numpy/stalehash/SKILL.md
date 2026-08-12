---
name: numpy-stalehash
description: "Use when testing graph_hash validation. Fixture: claims a stale graph_hash and a wrong node count."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
source_commit: ab2199763cb17878cd8f34fcbc97106c5397f922
extraction_date: 2026-08-12
graph:
  nodes: 99
  edges: 0
  community_count: 2
  graph_hash: "0000000000000000"
tags: [numpy]
related_skills: []
---

# NumPy Stale Hash (`numpy.stalehash`)

Fixture module skill. Its `graph_hash` does not match the committed graph.json, and its
`nodes` count is wrong — both planted violations.

## Quick Reference
| API | Graph Node | Purpose | Key Params |
|-----|-----------|---------|------------|
| `array` | `array.py:L1` | Create an ndarray | `dtype` |

## Common Patterns
```python
import numpy as np
np.zeros(3)
```

## Pitfalls
1. Planted violation: stale graph_hash `0000000000000000`.

## Provenance
- Knowledge graph: numpy, 3 nodes, 0 edges, 2 communities
