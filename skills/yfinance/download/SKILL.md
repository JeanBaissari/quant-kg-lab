---
name: yfinance-download
description: "Use when fetching multi-symbol market data with yfinance \u2014 download()\
  \ batches, Tickers, search, screeners, and the shared YfData request layer."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: ranaroussi/yfinance
source_commit: 93eb4c234acc7d0cf9d176e602b8443179546253
extraction_date: 2026-08-13
graph:
  nodes: 823
  edges: 1584
  community_count: 52
  graph_hash: 897483b2af81c8f8
tags:
- yfinance
- download
- batch
- screener
- search
related_skills:
- yfinance
- yfinance-ticker
- pandas-core
- polars-dataframe
- quantstats-reports
---

# yfinance.download

Batch and discovery surface: `yf.download(tickers, ...)` returns a MultiIndex history
frame; `Tickers` gives batch object access; `Search` and the `Screener` find symbols;
`YfData` is the shared HTTP/cookie layer underneath.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `download()` | `multi.py:L55` | Batch history across symbols → MultiIndex (Ticker, OHLCV) frame |
| `YfData` | `data.py:L80` | Shared request/cookie/session layer — deg 125 hub |
| `YfData.get()` | `data.py:L394` | Generic GET with cookie/auth handling |
| `YfData._make_request()` | `data.py:L412` | Raw request + response plumbing |
| `Auth` | `data.py:L576` | Yahoo authentication helper (cookie/CSRF) |
| `SingletonMeta` | `data.py:L60` | Singleton metaclass for shared state |
| `Tickers` | `tickers.py:L30` | Batch Ticker collection — iterate or index by symbol |
| `Search` | `search.py:L31` | Symbol search — `Search("apple")` → quotes list |
| `Lookup` | `lookup.py:L34` | Symbol lookup/validation helper |
| `Screener` | `screener/screener.py:L64` | Market screener — preset queries (e.g. "day_gainers") |
| `QueryBase` | `screener/query.py:L15` | Screener query base with pagination |
| `Domain` | `domain/domain.py:L11` | Domain classification (sector/industry/market) |
| `Sector` | `domain/sector.py:L12` | Sector taxonomy |
| `Industry` | `domain/industry.py:L12` | Industry taxonomy |
| `Calendars` | `calendars.py:L169` | Calendar data accessor (earnings dates) |
| `CalendarQuery` | `calendars.py:L17` | Calendar query helper |
| `YFException` | `exceptions.py:L1` | Library error base |

## Common Patterns

- **Universe history**:
  ```python
  import yfinance as yf
  data = yf.download(["AAPL", "MSFT", "GOOG"], period="1y", interval="1d",
                     group_by="ticker", auto_adjust=True)
  # data["AAPL"]["Close"] → returns matrix
  ```
- **Batch object access**: `tk = yf.Tickers("AAPL MSFT"); tk.tickers["AAPL"].history(...)`.
- **Symbol discovery**: `yf.Search("artificial intelligence", max_results=10)` — screen
  candidates before downloading.
- **Screener flows**: `yf.Screener("day_gainers")` — market-wide top movers as a
  starting universe.
- **Rate-limit discipline**: batch downloads hammer the same cookie — chunk the ticker
  list and sleep between chunks; catch `YFRateLimitError`.

## Pitfalls

- **group_by semantics**: `group_by="ticker"` vs `"column"` changes the MultiIndex
  layout — pick once and standardize the downstream accessor.
- **Symbol validity**: batch download silently skips unknown tickers (or returns
  NaNs) — verify coverage before assuming a full panel.
- **Threading**: yfinance's internal parallelism can trigger rate limits faster —
  prefer sequential chunks for large universes.
- **Session reuse**: pass a shared `session=` to download/Ticker for cookie reuse;
  fresh sessions per call re-auth each time.
- **Timezone drift**: batch results are exchange-local — normalize to a single
  timezone before merging with other data sources.

## Provenance

Graph: `knowledge_graphs/yfinance/.graphify/graph.json` — 823 nodes · 1584 edges ·
45 communities · graphify @ 93eb4c234acc, backend opencode, description coverage 97.2%.

## Verification Checklist

- [ ] `yf.download(["AAPL"], period="5d")` returns a MultiIndex frame
- [ ] `yf.Search("apple")` returns quote candidates
- [ ] QR rows cite `data.py:L1`/`tickers.py:L1`/`search.py:L1`/`screener/*.py` resolvable in the yfinance graph
