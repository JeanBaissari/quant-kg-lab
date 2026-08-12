---
name: numpy-core
description: "Use when working with NumPy arrays. Fixture: clean module skill whose only planted violation is a missing Provenance section."
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
tags: [numpy, core]
related_skills: []
---

# NumPy Core (`numpy.core`)

Fixture module skill. Everything conforms except the required `## Provenance` section,
which is intentionally absent.

## Quick Reference
| API | Graph Node | Purpose | Key Params |
|-----|-----------|---------|------------|
| `array` | `array.py:L1` | Create an ndarray | `dtype` |
| `linspace` | `linspace.py:L1` | Evenly spaced values | `num` |

## Common Patterns
```python
import numpy as np
x = np.linspace(0, 1, 10)
```

## Pitfalls
1. Planted violation: no `## Provenance` section below.
