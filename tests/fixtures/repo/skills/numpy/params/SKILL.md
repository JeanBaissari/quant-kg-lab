---
name: numpy-params
description: "Use when testing the QKG_050 param-table skip. Fixture: a skill whose QR contains parameter/alias tables — those rows must NOT be validated as callable API."
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

# NumPy Params (`numpy.params`)

Fixture module skill. Its Quick Reference documents constructor parameters and
aliases (lowercase, non-callable) plus a real function. Under QKG_050 the param
rows must be skipped; only the real callable is a claim.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `linspace` | `linspace.py:L1` | Real numpy function — must validate |

### Common Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `n_estimators` | int | 100 | Planted param — must NOT be an API claim |
| `max_depth` | int | 6 | Planted param — must NOT be an API claim |

### Parameter Aliases

| Primary | Alias | Graph Node |
|---------|-------|-----------|
| `learning_rate` | `eta` | `linspace.py:L1` |

## Common Patterns

```python
import numpy as np
np.linspace(0, 1, 10)
```

## Pitfalls

1. Planted fixture: params in parameter tables must never fail the API pass.

## Provenance

- Knowledge graph: numpy, 3 nodes, 0 edges, 2 communities
