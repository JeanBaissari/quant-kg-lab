---
name: arch
description: "Use when working with arch \u2014 the volatility/unit-root entry point.\
  \ Router indexing the arch sub-skills; load the sub-skill for the domain you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: bashtage/arch
source_commit: 704bb70e48372e3ccccdde7da379811657ad0224
extraction_date: 2026-08-12
graph:
  nodes: 1367
  edges: 3900
  community_count: 135
  graph_hash: e3f8bcd939a66a6d
tags:
- arch
- router
related_skills:
- arch-volatility
- arch-unitroot
- arch-bootstrap
- arch-forecast
- statsmodels-core
---

# arch

Volatility modelling (ARCH/GARCH family), unit-root testing, and bootstrap
resampling — the risk/volatility pillar of the quant stack.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [volatility](volatility/SKILL.md) | arch_model, GARCH/EGARCH, fit/forecast, conditional_volatility |
| [unitroot](unitroot/SKILL.md) | ADF, Phillips-Perron, KPSS, cointegration |
| [bootstrap](bootstrap/SKILL.md) | Stationary/circular block bootstrap, conf_int |
| [forecast](forecast/SKILL.md) | forecast()/rolling_forecast, variance paths, method selection |

## Common Patterns

- **Vol research**: stationarity gate (unitroot) → GARCH fit → forecast variance →
  risk inputs for portfolio construction.
- **Pairs**: Engle-Granger cointegration before spread strategies.

## Provenance

Graph: `knowledge_graphs/arch/.graphify/graph.json` — 1367 nodes · 3900 edges ·
135 communities · graphify @ 704bb70e4837, backend opencode, description coverage 94.3%.

## Verification Checklist

- [ ] Router links resolve to the 3 module skills
- [ ] `related_skills` names resolve to real skills
