---
name: yfinance-ticker
description: "Use when fetching per-symbol market data with yfinance \u2014 Ticker\
  \ history, fast_info, fundamentals (income/financials/balance/cashflow), actions,\
  \ options, holders, calendar, and the scrapers behind them."
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
  graph_hash: e61aa37b110ae35f
tags:
- yfinance
- ticker
- history
- fundamentals
related_skills:
- yfinance
- yfinance-download
- pandas-core
- quantstats-reports
- empyrical-stats
target_version: 1.6.0 (released tag 1.6.0)
upstream_status: current
---

# yfinance.ticker

The per-symbol client: `Ticker("AAPL")` exposes price history, quote snapshot
(`fast_info`), fundamentals, corporate actions, options chains, holders, and
calendar data — each lazily fetched through the scrapers.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Ticker` | `ticker.py:L33` | Per-symbol client — all data accessors hang off this object |
| `TickerBase` | `base.py:L54` | Shared fetch/storage layer under Ticker (and Tickers) |
| `.history()` | `scrapers/history.py:L41` | OHLCV history — period/interval/start/end, auto_adjust |
| `PriceHistory` | `scrapers/history.py:L20` | History fetcher — the underlying request/parse layer |
| `.fast_info` | `ticker.py:L162` | Quote snapshot: last price, day range, market cap, PE |
| `FastInfo` | `scrapers/quote.py:L46` | Fast-info response object with cached fields |
| `.info` | `ticker.py:L158` | Full metadata dict (slower, richer than fast_info) |
| `.income_stmt` | `ticker.py:L201` | Income statement DataFrame |
| `.quarterly_income_stmt` | `ticker.py:L205` | Quarterly income statement |
| `.ttm_income_stmt` | `ticker.py:L209` | Trailing-twelve-months income statement |
| `.financials` | `ticker.py:L225` | Annual financials (revenue/earnings rows) |
| `.balance_sheet` | `ticker.py:L237` | Annual balance sheet |
| `.cash_flow` | `ticker.py:L253` | Annual cash-flow statement |
| `.ttm_cash_flow` | `ticker.py:L261` | TTM cash flow |
| `.earnings` | `ticker.py:L193` | Annual earnings history |
| `.quarterly_earnings` | `ticker.py:L197` | Quarterly earnings |
| `.actions` | `ticker.py:L150` | Dividends + splits combined |
| `.dividends` | `ticker.py:L138` | Dividend history |
| `.splits` | `ticker.py:L146` | Split history |
| `.capital_gains` | `ticker.py:L142` | Capital-gains distributions (funds) |
| `.shares` | `ticker.py:L154` | Share count history |
| `.option_chain()` | `ticker.py:L83` | Calls/puts DataFrame pair for a date |
| `.major_holders` | `ticker.py:L114` | Top shareholders table |
| `.institutional_holders` | `ticker.py:L118` | Institutional ownership |
| `.insider_transactions` | `ticker.py:L130` | Insider trades |
| `.calendar` | `ticker.py:L170` | Next earnings/date events |
| `.sec_filings` | `ticker.py:L177` | Recent SEC filings list |
| `.recommendations` | `ticker.py:L181` | Analyst recommendations history |
| `.upgrades_downgrades` | `ticker.py:L189` | Rating-change events |
| `.valuation` | `ticker.py:L166` | Valuation metrics snapshot |
| `.isin` | `ticker.py:L110` | ISIN identifier for the symbol |
| `.get_info()` | `base.py:L281` | Alias/refresh path for `.info` |
| `.get_dividends()` | `ticker.py:L138` | Getter method for dividend history |
| `.get_splits()` | `ticker.py:L146` | Getter method for split history |
| `.get_actions()` | `ticker.py:L150` | Getter method for dividends + splits |
| `.get_shares()` | `ticker.py:L154` | Getter method for share count history |
| `Analysis` | `scrapers/analysis.py:L11` | Analyst expectations scraper |
| `Financials` | `scrapers/fundamentals.py:L43` | Financial-statement scraper |
| `Holders` | `scrapers/holders.py:L12` | Holders scraper |
| `FundsData` | `scrapers/funds.py:L12` | Fund-specific data scraper |
| `Quote` | `scrapers/quote.py:L505` | Quote scraper (fast_info payload) |
| `WebSocket` | `live.py:L220` | Live-price websocket (streaming quotes) |
| `YFDataException` | `exceptions.py:L6` | Data-layer error base |
| `YFRateLimitError` | `exceptions.py:L69` | Rate-limit error — back off on repeated fetches |

## Common Patterns

- **Price history for a factor panel**:
  ```python
  t = yf.Ticker("AAPL")
  df = t.history(period="2y", interval="1d", auto_adjust=True)
  # df[['Open','High','Low','Close','Volume']] → returns → factors
  ```
- **Fundamental screens**: `t.income_stmt.loc["Total Revenue"]` /
  `t.balance_sheet.loc["Total Debt"]` — cross-sectional fundamental features.
- **Action adjustment**: `t.actions` + `t.splits` — property access, not method calls. Verify `auto_adjust` semantics before computing raw (unadjusted) returns.
- **Options surface**: `t.option_chain(date)` → `calls`/`puts` frames with IV/Greeks —
  the input to volatility-surface work.
- **Streaming**: `WebSocket`/`AsyncWebSocket` for live quotes in an event loop.
- **Error handling**: wrap fetches in `YFException`/`YFRateLimitError` handling — rate
  limits are normal, retry with backoff.

## Pitfalls

- **auto_adjust**: `history(auto_adjust=True)` returns adjusted OHLC but the raw
  `Volume`/`Dividends` semantics differ from unadjusted — pick one convention and
  document it per dataset.
- **fast_info vs info**: `fast_info` is a cached quote snapshot (fast); `.info` is a
  slow full-metadata fetch — don't call `.info` in tight loops.
- **Rate limits**: Yahoo throttles aggressively — `YFRateLimitError` means back off
  (sleep + retry), not retry faster.
- **Fundamentals availability**: income/financials/balance/cashflow are empty for
  non-US or small-caps — check `.empty` before slicing rows.
- **Delisted/typo symbols**: unknown symbols raise or return empty frames — validate
  the symbol via `yf.Search` before assuming data exists.
- **Timezone**: `.history()` returns exchange-local timestamps — align to UTC before
  joining across markets.
- **Ticker members are properties, not methods**: Accessing `.dividends()`, `.info()`,
  `.fast_info()`, etc. with parentheses raises `TypeError`. Use property access:
  `t.dividends`, `t.info`, `t.fast_info`. The `get_*()` variants (`.get_dividends()`,
  `.get_info()`) are explicit getter methods where they exist.

## Provenance

Graph: `knowledge_graphs/yfinance/.graphify/graph.json` — 823 nodes · 1584 edges ·
45 communities · graphify @ 93eb4c234acc, backend opencode, description coverage 97.2%.

## Verification Checklist

- [ ] `yf.Ticker("AAPL").history(period="5d")` returns OHLCV rows
- [ ] `t.fast_info` returns a cached quote snapshot (property, not method call)
- [ ] `t.info` returns full metadata dict (property, not method call)
- [ ] `t.dividends` returns dividend history (property, not method call)
- [ ] QR rows cite `ticker.py:L1`/`base.py:L1`/`scrapers/*.py` resolvable in the yfinance graph
