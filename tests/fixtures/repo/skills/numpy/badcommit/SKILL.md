---
name: numpy-badcommit
description: "Use when testing source_commit validation. Fixture: pins a commit that does not match graphs.lock."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
source_commit: ffffffffffffffffffffffffffffffffffffffff
extraction_date: 2026-08-12
graph:
  nodes: 3
  edges: 0
  community_count: 2
  graph_hash: df564aefc267559e
tags: [numpy]
related_skills: []
---

# NumPy Bad Commit (`numpy.badcommit`)

Fixture module skill. Its `source_commit` does not match graphs.lock — planted violation.

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
1. Planted violation: wrong source_commit.

## Provenance
- Knowledge graph: numpy, 3 nodes, 0 edges, 2 communities
