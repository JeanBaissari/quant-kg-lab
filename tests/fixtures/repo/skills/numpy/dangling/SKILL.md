---
name: numpy-dangling
description: "Use when testing related_skills resolution. Fixture: references a skill that does not exist."
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
related_skills: [no-such-skill]
---

# NumPy Dangling (`numpy.dangling`)

Fixture module skill. Its `related_skills` lists a name that resolves to nothing —
planted violation.

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
1. Planted violation: `related_skills: [no-such-skill]` does not resolve.

## Provenance
- Knowledge graph: numpy, 3 nodes, 0 edges, 2 communities
