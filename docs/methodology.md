# Methodology — QuantKG Extraction Pipeline

## 1. Knowledge Graph Extraction

We use [graphify](https://github.com/sentropic/graphify) to ingest library source trees and produce structured knowledge graphs.

### Process

1. **Clone** target library at a pinned version tag
2. **Detect** file types, token counts, language distribution
3. **Extract** (AST + semantic):
   - Python AST: class/function definitions, imports, inheritance chains
   - Semantic: docstring summaries, module-level descriptions via LLM
4. **Build** undirected graph (nodes = code entities, edges = relationships)
5. **Cluster** via community detection → natural module boundaries
6. **Label** communities → human-readable module names
7. **Audit** every edge tagged EXTRACTED | INFERRED | AMBIGUOUS

### Graph Schema

```json
{
  "nodes": [
    {
      "id": "sklearn.ensemble.RandomForestClassifier",
      "label": "RandomForestClassifier",
      "file_type": "code",
      "source_file": "sklearn/ensemble/_forest.py",
      "source_location": "L1023-L1500",
      "type": "class"
    }
  ],
  "links": [
    {
      "source": "...",
      "target": "...",
      "relation": "inherits",
      "confidence": "EXTRACTED"
    }
  ]
}
```

## 2. Skill Authoring

From the knowledge graph, we extract quant-relevant modules and author spec-driven skills.

### Selection Criteria
- Module has ≥3 god nodes (high-degree API hubs)
- Community cohesion > threshold
- Direct quant applicability (model_selection, metrics, samplers, pruners)

### Skill Structure
Each skill follows `agentskills.io` with:
- **SKILL.md**: trigger conditions, quick reference, core workflows
- **references/api.md**: extracted from graph nodes (class → method signatures)
- **references/examples.md**: extracted from library examples/tutorials
- **scripts/validate.py**: cross-ref skill claims against live library

## 3. Freshness

CI pipeline checks library versions weekly. Stale graphs trigger re-extraction. Skills track extraction date and library version in frontmatter.
