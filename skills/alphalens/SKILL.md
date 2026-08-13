---
name: alphalens
description: "Use when working with alphalens — the factor-analysis entry point. Router indexing the alphalens sub-skills; load the sub-skill for the analysis layer you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: quantopian/alphalens
source_commit: 77084f1e4c2c0be407e032d444fb19e4be4b0f37
extraction_date: 2026-08-12
graph:
  nodes: 172
  edges: 231
  community_count: 5
  graph_hash: b1726a0e2484f41b
tags:
- alphalens
- router
related_skills:
- alphalens-factor-analysis
- alphalens-tearsheets
- pandas-core
---

# alphalens

Factor-performance analysis for quant research: forward returns, quantile
breakdowns, information coefficients, and tear sheets — the bridge between
factor construction and portfolio reporting.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [factor_analysis](factor_analysis/SKILL.md) | FactorData, forward returns, quantile/IC analytics |
| [tearsheets](tearsheets/SKILL.md) | Returns/IC/event tear sheets, GridFigure |

## Common Patterns

- **Factor pipeline**: factor + prices → `get_clean_factor_and_forward_returns` →
  IC/quantile metrics → tear sheets → pyfolio for portfolio-level reporting.
- **Signal validation**: monotonic quantile returns + stable positive IC before any strategy
  work.

## Provenance

Graph: `knowledge_graphs/alphalens/.graphify/graph.json` — 172 nodes · 231 edges ·
5 communities · graphify @ 77084f1e4c2c, backend opencode, description coverage 86.8%.

## Verification Checklist

- [ ] Router links resolve to the 2 module skills
- [ ] `related_skills` names resolve to real skills
