---
name: yfinance
description: "Use when working with yfinance — the market-data entry point. Router indexing the yfinance sub-skills; load the sub-skill for the fetch pattern you need."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: ranaroussi/yfinance
source_commit: 93eb4c234acc7d0cf9d176e602b8443179546253
extraction_date: 2026-08-13
graph:
  nodes: 823
  edges: 1584
  community_count: 45
  graph_hash: 897483b2af81c8f8
tags:
- yfinance
- router
- market-data
- yahoo
related_skills:
- yfinance-ticker
- yfinance-download
- pandas-core
- polars-io
- quantstats-reports
---

# yfinance

Yahoo Finance data client: per-symbol `Ticker` access, batch `download()`, search,
screeners, and the domain/fundamentals scrapers — the data-ingestion layer of the stack.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [ticker](ticker/SKILL.md) | Ticker/TickerBase — history, fast_info, fundamentals, actions, options |
| [download](download/SKILL.md) | download()/Tickers — multi-symbol history batches into DataFrames |

## Common Patterns

- **Single symbol**: `yf.Ticker("AAPL").history(period="1y")` — then feed pandas/polars.
- **Multi-symbol**: `yf.download(["AAPL", "MSFT"], period="6mo")` — wide MultiIndex frame.
- **Report handoff**: fetched returns → empyrical/quantstats for metrics + tear sheets.

## Provenance

Graph: `knowledge_graphs/yfinance/.graphify/graph.json` — 823 nodes · 1584 edges ·
45 communities · graphify @ 93eb4c234acc, backend opencode, description coverage 97.2%.

## Verification Checklist

- [ ] Router links resolve to the 2 module skills
- [ ] `related_skills` names resolve to real skills
