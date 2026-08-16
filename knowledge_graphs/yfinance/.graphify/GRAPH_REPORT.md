# Graph Report - knowledge_graphs/yfinance/repo/yfinance  (2026-08-13)

## Corpus Check
- Corpus is ~48,288 words - fits in a single context window. You may not need a graph.

## Summary
- 823 nodes · 1584 edges · 52 communities detected
- Non-singleton communities: 46
- Extraction: EXTRACTED: 74.6% · INFERRED: 25.4%
- Edge kinds: calls: 302 · contains: 127 · imports_from: 74 · inherits: 26 · method: 475 · rationale_for: 177 · uses: 403

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 34 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `93eb4c2`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `YfData` (125)
- `YFDataException` (90)
- `YFException` (64)
- `Ticker` (62)
- `TickerBase` (57)
- `utils.py` (51)
- `YFRateLimitError` (40)
- `FastInfo` (40)
- `Domain` (39)
- `WebSocket` (31)

## Surprising Connections (you probably didn't know these)
- `Per-call scratch state for download(). Concurrent calls each get     their own i` --uses--> `YfData`  [INFERRED]
  multi.py → data.py
- `Download yahoo tickers     :Parameters:         tickers : str, list` --uses--> `YfData`  [INFERRED]
  multi.py → data.py
- `Returns a dictionary of events, earnings, and dividends for the ticker` --uses--> `TickerBase`  [INFERRED]
  ticker.py → base.py
- `Returns a DataFrame with the recommendations         Columns: period  strongBuy` --uses--> `YfData`  [INFERRED]
  base.py → data.py
- `Valuation measures (market cap, P/E, P/S, P/B, EV/EBITDA, ...).          Returns` --uses--> `YfData`  [INFERRED]
  base.py → data.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (52): Returns a DataFrame with the recommendations         Columns: period  strongBuy, Valuation measures (market cap, P/E, P/S, P/B, EV/EBITDA, ...).          Returns, Keys:   current  low  high  mean  median, Index:      0q  +1q  0y  +1y         Columns:    numberOfAnalysts  avg  low  hig, Index:      0q  +1q  0y  +1y         Columns:    numberOfAnalysts  avg  low  hig, Index:      pd.DatetimeIndex         Columns:    epsEstimate  epsActual  epsDiff, Index:      0q  +1q  0y  +1y         Columns:    current  7daysAgo  30daysAgo  6, Index:      0q  +1q  0y  +1y         Columns:    upLast7days  upLast30days  down (+44 more)

### Community 1 - "Community 1"
Cohesion: 0.07
Nodes (3): FastInfo, Quote, Valuation measures (market cap, P/E, P/S, P/B, EV/EBITDA, ...).          Returns

### Community 2 - "Community 2"
Cohesion: 0.04
Nodes (2): Ticker, TickerBase

### Community 3 - "Community 3"
Cohesion: 0.06
Nodes (20): YFNotImplementedError, NotImplementedError, Financials, Fundamentals, Fetch a fundamentals-timeseries URL and return the parsed `result`         list., EquityQuery, ETFQuery, FundQuery (+12 more)

### Community 4 - "Community 4"
Cohesion: 0.05
Nodes (2): Returns a DataFrame with the recommendations changes (upgrades/downgrades), TickerBase

### Community 5 - "Community 5"
Cohesion: 0.11
Nodes (20): CalendarQuery, Calendars, Get economic calendars, for example, Earnings, IPO, Economic Events, Splits, Simple CalendarQuery class for calendar queries, similar to yf.screener.query.Qu, :param str | datetime | date start: start date (default today) \             eg., Retrieve tickers from YF, converts them into operands accepted by YF.         Sa, Get startdatetime operands for start/end dates.         If no dates passed, defa, :param operator: Operator string, e.g., 'eq', 'gte', 'and', 'or'.         :param (+12 more)

### Community 6 - "Community 6"
Cohesion: 0.08
Nodes (18): Lookup, Returns all available financial instruments.          :param count: The number o, Returns stock related financial instruments.          :param count: The number o, Returns mutual funds related financial instruments.          :param count: The n, Returns ETFs related financial instruments.          :param count: The number of, Returns Indices related financial instruments.          :param count: The number, Returns Futures related financial instruments.          :param count: The number, Returns Currencies related financial instruments.          :param count: The num (+10 more)

### Community 7 - "Community 7"
Cohesion: 0.08
Nodes (19): FundsData, Returns the top holdings of the fund.          Returns:             pd.DataFrame, Returns the equity holdings of the fund.          Returns:             pd.DataFr, ETF and Mutual Funds Data     Queried Modules: quoteType, summaryProfile, fundPr, Returns the bond holdings of the fund.          Returns:             pd.DataFram, Returns the bond ratings of the fund.          Returns:             Dict[str, fl, Returns the sector weightings of the fund.          Returns:             Dict[st, Fetches the raw JSON data from the API.          Returns:             dict: The (+11 more)

### Community 8 - "Community 8"
Cohesion: 0.10
Nodes (14): ABC, Domain, Retrieves research reports related to the domain entity.          Returns:, Fetches data from the given query URL.          Args:             query_url (str, Abstract base class representing a domain entity in financial data, with key att, Initializes the Domain object with a key, session, and region.          Args:, Abstract method for fetching and parsing domain-specific data.          Must be, Ensures that the given attribute is fetched by calling `_fetch_and_parse()` if t (+6 more)

### Community 9 - "Community 9"
Cohesion: 0.11
Nodes (10): _dts_in_same_interval(), fix_Yahoo_returning_live_separate(), fix_Yahoo_returning_prepost_unrequested(), get_all_by_isin(), get_info_by_isin(), get_news_by_isin(), get_ticker_by_isin(), _interval_to_timedelta() (+2 more)

### Community 10 - "Community 10"
Cohesion: 0.20
Nodes (2): _normalize_proxy(), YfData

### Community 11 - "Community 11"
Cohesion: 0.19
Nodes (1): PriceHistory

### Community 12 - "Community 12"
Cohesion: 0.10
Nodes (13): Get the quotes from the search results., Get the news from the search results., Get the lists from the search results., Get the research reports from the search results., Get the navigation links from the search results., Get all the results from the search results: filtered down version of response., Get the raw response from the search results., Fetches and organizes search results from Yahoo Finance, including stock quotes (+5 more)

### Community 13 - "Community 13"
Cohesion: 0.24
Nodes (2): _is_transient_error(), lru_cache_freezeargs()

### Community 14 - "Community 14"
Cohesion: 0.10
Nodes (12): Domain, Industry, Parses the top growth companies data.                  Args:             top_gro, Represents an industry within a sector., Fetches and parses the industry data., Args:             key (str): The key identifier for the industry.             se, Returns a string representation of the Industry instance.                  Retur, Returns the sector key of the industry.                  Returns:             st (+4 more)

### Community 15 - "Community 15"
Cohesion: 0.11
Nodes (9): AsyncWebSocket, BaseWebSocket, Unsubscribe from a stock symbol or a list of stock symbols.          Args:, Start listening to messages from the WebSocket server.          Args:, Close the WebSocket connection., Start listening to messages from the WebSocket server.          Args:, Asynchronous WebSocket client for streaming real time pricing data., Initialize the AsyncWebSocket client.          Args:             url (str): The (+1 more)

### Community 16 - "Community 16"
Cohesion: 0.12
Nodes (11): Parses industry data from the API response into a DataFrame.          Args:, Fetches and parses sector data from the API.          Fetches data for the secto, Represents a financial market sector and allows retrieval of sector-related data, Args:             key (str): The key representing the sector.             sessio, Returns the string representation of the Sector object.          Returns:, Gets the top ETFs for the sector.          Returns:             Dict[str, str]:, Gets the top mutual funds for the sector.          Returns:             Dict[str, Gets the industries within the sector.          Returns:             pandas.Data (+3 more)

### Community 17 - "Community 17"
Cohesion: 0.14
Nodes (17): cookie_jar(), is_supported_session(), new_session(), HTTP backend abstraction.  Prefers ``curl_cffi`` for browser TLS impersonation., Create a default Session for the active backend., Return the underlying ``http.cookiejar.CookieJar`` for either backend.      ``cu, True if ``obj`` is a Session from either supported backend., _supported_session_classes() (+9 more)

### Community 18 - "Community 18"
Cohesion: 0.21
Nodes (1): Holders

### Community 19 - "Community 19"
Cohesion: 0.28
Nodes (1): Analysis

### Community 20 - "Community 20"
Cohesion: 0.21
Nodes (2): ConfigMgr, NestedConfig

### Community 21 - "Community 21"
Cohesion: 0.20
Nodes (7): _CookieSchema, _ISIN_KV, Meta, Sets the path to create the "py-yfinance" cache folder in.     Useful if the def, set_cache_location(), set_tz_cache_location(), _TZ_KV

### Community 22 - "Community 22"
Cohesion: 0.20
Nodes (7): _disable_debug_mode(), enable_debug_mode(), get_indented_logger(), get_yf_logger(), IndentLoggerAdapter, MultiLineFormatter, YFLogFormatter

### Community 23 - "Community 23"
Cohesion: 0.27
Nodes (5): Market, MarketRegion, Market regions accepted by Yahoo's ``quote/marketSummary`` endpoint.      Member, Enum, str

### Community 24 - "Community 24"
Cohesion: 0.22
Nodes (2): _CookieCache, _CookieCacheManager

### Community 25 - "Community 25"
Cohesion: 0.22
Nodes (2): _ISINCache, _ISINCacheManager

### Community 26 - "Community 26"
Cohesion: 0.22
Nodes (2): _TzCache, _TzCacheManager

### Community 27 - "Community 27"
Cohesion: 0.25
Nodes (3): _TzCacheException, _TzDBManager, Exception

### Community 28 - "Community 28"
Cohesion: 0.29
Nodes (2): _CookieCacheException, _CookieDBManager

### Community 29 - "Community 29"
Cohesion: 0.29
Nodes (2): _ISINCacheException, _ISINDBManager

### Community 30 - "Community 30"
Cohesion: 0.33
Nodes (1): Tickers

### Community 31 - "Community 31"
Cohesion: 0.48
Nodes (1): ProgressBar

### Community 32 - "Community 32"
Cohesion: 0.33
Nodes (3): Parses and assigns common data fields such as name, symbol, overview, and top co, Parses the overview data for the domain entity.          Args:             overv, Parses the top companies data and converts it into a pandas DataFrame.

### Community 33 - "Community 33"
Cohesion: 0.40
Nodes (2): _CookieCacheDummy, Dummy cache to use if Cookie cache is disabled

### Community 34 - "Community 34"
Cohesion: 0.40
Nodes (2): _ISINCacheDummy, Dummy cache to use if isin cache is disabled

### Community 35 - "Community 35"
Cohesion: 0.40
Nodes (2): Dummy cache to use if tz cache is disabled, _TzCacheDummy

### Community 36 - "Community 36"
Cohesion: 0.40
Nodes (5): camel2title(), format_annual_financial_statement(), format_quarterly_financial_statement(), format_annual_financial_statement formats any annual financial statement      Re, format_quarterly_financial_statements formats any quarterly financial statement

### Community 37 - "Community 37"
Cohesion: 0.40
Nodes (5): generate_list_table_from_dict(), generate_list_table_from_dict_universal(), _generate_table_configurations(), Generate a list-table for the docstring showing permitted keys/values., Generate a list-table for the docstring showing permitted keys/values.

### Community 39 - "Community 39"
Cohesion: 0.50
Nodes (1): IndentationContext

### Community 40 - "Community 40"
Cohesion: 0.67
Nodes (1): ISODateTimeField

### Community 41 - "Community 41"
Cohesion: 1.00
Nodes (1): Returns a dictionary of events, earnings, and dividends for the ticker

### Community 42 - "Community 42"
Cohesion: 1.00
Nodes (2): build_template(), build_template returns the details required to rebuild any of the yahoo finance

### Community 43 - "Community 43"
Cohesion: 1.00
Nodes (2): dynamic_docstring(), A decorator to dynamically update the docstring of a function or method.

### Community 44 - "Community 44"
Cohesion: 1.00
Nodes (2): is_valid_period_format(), Check if the provided period has a valid format.

### Community 45 - "Community 45"
Cohesion: 1.00
Nodes (2): retrieve_financial_details returns all of the available financial details under, retrieve_financial_details()

## Knowledge Gaps
- **43 isolated node(s):** `HTTP backend abstraction.  Prefers ``curl_cffi`` for browser TLS impersonation.`, `Create a default Session for the active backend.`, `Return the underlying ``http.cookiejar.CookieJar`` for either backend.      ``cu`, `True if ``obj`` is a Session from either supported backend.`, `Returns a DataFrame with the recommendations changes (upgrades/downgrades)` (+38 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 2`** (2 nodes): `Ticker`, `TickerBase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 4`** (2 nodes): `Returns a DataFrame with the recommendations changes (upgrades/downgrades)`, `TickerBase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 10`** (2 nodes): `_normalize_proxy()`, `YfData`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (1 nodes): `PriceHistory`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (2 nodes): `_is_transient_error()`, `lru_cache_freezeargs()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (1 nodes): `Holders`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (1 nodes): `Analysis`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (2 nodes): `ConfigMgr`, `NestedConfig`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (2 nodes): `_CookieCache`, `_CookieCacheManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (2 nodes): `_ISINCache`, `_ISINCacheManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (2 nodes): `_TzCache`, `_TzCacheManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (2 nodes): `_CookieCacheException`, `_CookieDBManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (2 nodes): `_ISINCacheException`, `_ISINDBManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (1 nodes): `Tickers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (1 nodes): `ProgressBar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (2 nodes): `_CookieCacheDummy`, `Dummy cache to use if Cookie cache is disabled`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (2 nodes): `_ISINCacheDummy`, `Dummy cache to use if isin cache is disabled`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (2 nodes): `Dummy cache to use if tz cache is disabled`, `_TzCacheDummy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `IndentationContext`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `ISODateTimeField`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (1 nodes): `Returns a dictionary of events, earnings, and dividends for the ticker`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (2 nodes): `build_template()`, `build_template returns the details required to rebuild any of the yahoo finance`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (2 nodes): `dynamic_docstring()`, `A decorator to dynamically update the docstring of a function or method.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (2 nodes): `is_valid_period_format()`, `Check if the provided period has a valid format.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (2 nodes): `retrieve_financial_details returns all of the available financial details under`, `retrieve_financial_details()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `YfData` connect `Community 10` to `Community 0`, `Community 4`, `Community 5`, `Community 13`, `Community 6`, `Community 17`, `Community 19`, `Community 3`, `Community 7`, `Community 18`, `Community 1`, `Community 12`, `Community 30`?**
  _High betweenness centrality (0.413) - this node is a cross-community bridge._
- **Why does `TickerBase` connect `Community 4` to `Community 13`, `Community 10`, `Community 0`, `Community 41`, `Community 2`?**
  _High betweenness centrality (0.194) - this node is a cross-community bridge._
- **Why does `Ticker` connect `Community 2` to `Community 13`, `Community 4`, `Community 41`, `Community 38`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Are the 102 inferred relationships involving `YfData` (e.g. with `Returns a DataFrame with the recommendations         Columns: period  strongBuy` and `Valuation measures (market cap, P/E, P/S, P/B, EV/EBITDA, ...).          Returns`) actually correct?**
  _`YfData` has 102 INFERRED edges - model-reasoned connections that need verification._
- **Are the 88 inferred relationships involving `YFDataException` (e.g. with `Returns a DataFrame with the recommendations         Columns: period  strongBuy` and `Valuation measures (market cap, P/E, P/S, P/B, EV/EBITDA, ...).          Returns`) actually correct?**
  _`YFDataException` has 88 INFERRED edges - model-reasoned connections that need verification._
- **Are the 57 inferred relationships involving `YFException` (e.g. with `CalendarQuery` and `Calendars`) actually correct?**
  _`YFException` has 57 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `TickerBase` (e.g. with `YfData` and `YFDataException`) actually correct?**
  _`TickerBase` has 7 INFERRED edges - model-reasoned connections that need verification._