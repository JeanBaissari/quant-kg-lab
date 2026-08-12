---
name: numpy-hallucinated
description: "Use when testing the module-scoped API check. Fixture: claims functions and classes that exist nowhere in numpy or its graph."
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
related_skills: []
---

# NumPy Hallucinated (`numpy.linalg`)

Fixture module skill. Its Quick Reference claims an invented function, an invented
class, and a class that exists only in a *different* installed library (scikit-learn's
`StandardScaler`) — under the module-scoped API universe, none of these may pass.

## Quick Reference
| API | Graph Node | Purpose | Key Params |
|-----|-----------|---------|------------|
| `ictus_flip` | `linspace.py:L1` | Invented function | `n` |
| `QuandaryRegression` | `array.py:L1` | Invented class | `alpha` |
| `StandardScaler` | `array.py:L1` | Cross-library class | `with_mean` |

## Common Patterns
```python
import numpy as np
np.zeros(3)
```

## Pitfalls
1. Planted violation: hallucinated and cross-library API claims.

## Provenance
- Knowledge graph: numpy, 3 nodes, 0 edges, 2 communities
