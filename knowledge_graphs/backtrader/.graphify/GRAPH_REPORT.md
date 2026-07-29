# Graph Report - .  (2026-07-29)

## Corpus Check
- cluster-only mode - file stats not available

## Summary
- 3458 nodes · 6863 edges · 257 communities detected
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 1451 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: method: 1724 · uses: 1451 · contains: 823 · imports: 799 · calls: 714 · rationale_for: 646 · imports_from: 418 · inherits: 288


## Graph Freshness
- Built from Git commit: `b853d7c`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `MetaParams` - 247 edges
2. `LineRoot` - 110 edges
3. `Strategy` - 107 edges
4. `LineSingle` - 100 edges
5. `PandasMarketCalendar` - 74 edges
6. `DataBase` - 72 edges
7. `CommInfoBase` - 71 edges
8. `LineIterator` - 69 edges
9. `IBStore` - 67 edges
10. `LineBuffer` - 65 edges

## Surprising Connections (you probably didn't know these)
- `Base Class for the Commission Schemes.      Params:        - ``commission`` (def` --uses--> `MetaParams`  [INFERRED]
  backtrader/comminfo.py → backtrader/metabase.py
- `Wrapper for filters added via .addfilter to turn them     into processors.` --uses--> `LineSeries`  [INFERRED]
  backtrader/dataseries.py → backtrader/lineseries.py
- `This class is a placeholder for the values of the standard lines of a     DataBa` --uses--> `LineSeries`  [INFERRED]
  backtrader/dataseries.py → backtrader/lineseries.py
- `Initializes a bar to the default not-updated vaues` --uses--> `LineSeries`  [INFERRED]
  backtrader/dataseries.py → backtrader/lineseries.py
- `Returns if a bar has already been updated          Uses the fact that NaN is the` --uses--> `LineSeries`  [INFERRED]
  backtrader/dataseries.py → backtrader/lineseries.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.02
Nodes (9): backtrader_indicators, RelativeVolume, parse_args(), runstrategy(), parse_args(), runstrat(), testcommon, TS2 (+1 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (46): LineIterator, StrategyBase, LineSingle, Base class for LineXXX instances that hold a single line, LineSeriesStub, findbases(), ItemCollection, Holds a collection of items that can be reached by        - Index       - Name ( (+38 more)

### Community 2 - "Community 2"
Cohesion: 0.04
Nodes (52): parse_args(), runstrategy(), argparse, backtrader_analyzers, parse_args(), runstrat(), parse_args(), runstrat() (+44 more)

### Community 3 - "Community 3"
Cohesion: 0.06
Nodes (24): backtrader, MetaTimeFrameAnalyzerBase, backtrader_stores, backtrader_utils, backtrader_utils_py3, calendar, collections, copy (+16 more)

### Community 4 - "Community 4"
Cohesion: 0.04
Nodes (48): autodict, _MetaTALibIndicator, bisect, parse_args(), runstrat(), date, GenericCSV, YahooFinance (+40 more)

### Community 5 - "Community 5"
Cohesion: 0.04
Nodes (43): MetaBroker, Class has already been created ... fill missing methods if needed be, CommissionInfo, Returns the actual margin/guarantees needed for a single item of the         ass, Returns the level of leverage allowed for this comission scheme, Returns the needed size to meet a cash operation at a given price, Returns the needed amount of cash an operation would cost, Returns the value of size for given a price. For future-like         objects it (+35 more)

### Community 6 - "Community 6"
Cohesion: 0.05
Nodes (24): LineBuffer, Resets the internal buffer structure and the indices, The linebuffer must guarantee the minimum requested size to be         available, Real data that can be currently held in the internal buffer          The interna, Returns a slice of the array relative to *ago*          Keyword Args:, Returns a single value of the array relative to the real zero         of the buf, Returns a slice of the array relative to the real zero of the buffer          Ke, Sets a value at position "ago" and executes any associated bindings          Key (+16 more)

### Community 7 - "Community 7"
Cohesion: 0.04
Nodes (42): backtrader_feeds, backtrader_filters, backtrader_utils_flushfile, parse_args(), runstrat(), parse_args(), runstrategy(), parse_args() (+34 more)

### Community 8 - "Community 8"
Cohesion: 0.05
Nodes (19): LineRoot, Receive notification of how large the buffer must at least be, Direct minperiod manipulation. It could be used for example         by a strateg, Update the minperiod if needed. The minperiod will have been         calculated, Add a minperiod to own ... to be defined by subclasses, Increment the minperiod with no considerations, It will be called during the "minperiod" phase of an iteration., It will be called when the minperiod phase is over for the 1st         post-minp (+11 more)

### Community 9 - "Community 9"
Cohesion: 0.04
Nodes (22): OrderBase, OrderData, Returns the name for a given status or the one of the order, Returns the name for a given exectype or the one of the order, Returns the name for a given ordtype or the one of the order, Returns True if the order is in a status in which it can still be         execut, Stores a CommInfo scheme associated with the asset, Add the keys, values of kwargs to the internal info dictionary to         hold c (+14 more)

### Community 10 - "Community 10"
Cohesion: 0.07
Nodes (5): BackBroker, Returns the actual fundmode (True or False), Returns the current cash (alias: ``getcash``), Sets the cash parameter (alias: ``setcash``), Add/Remove cash to the system (use a negative value to remove)

### Community 11 - "Community 11"
Cohesion: 0.09
Nodes (33): Used during optimization to pass the cerebro over the multiprocesing         mod, Used during optimization to prevent optimization result `runstrats`         from, If invoked from inside a strategy or anywhere else, including other         thre, Internal method invoked by ``run``` to run a set of strategies, Internal method which kicks the broker and delivers any broker         notificat, Actual implementation of run in vector mode.          Strategies are still invok, Receives a timer notification where ``timer`` is the timer which was         ret, Internal method to really create the timer (not started yet) which         can b (+25 more)

### Community 12 - "Community 12"
Cohesion: 0.08
Nodes (24): array, LineActions, LineDelay(), _LineForward, LineNum(), LineOwnOperation, LinesOperation, PseudoArray (+16 more)

### Community 13 - "Community 13"
Cohesion: 0.10
Nodes (36): CommInfoBase, Base Class for the Commission Schemes.      Params:        - ``commission`` (def, BuyOrder, Order, Class which holds creation/execution data and type of oder.      The order may h, SellOrder, StopBuyOrder, StopLimitBuyOrder (+28 more)

### Community 14 - "Community 14"
Cohesion: 0.05
Nodes (29): DataBase, IBOrder, IBOrderState, MetaIBBroker, Class has already been created ... register, Subclasses the IBPy order to provide the minimum extra functionality     needed, Get the printout from the base class and add some ib.Order specific         fiel, MetaOandaData (+21 more)

### Community 15 - "Community 15"
Cohesion: 0.06
Nodes (23): DataSeries, OHLC, OHLCDateTime, Indicator, LinePlotterIndicator, MetaIndicator, MtLinePlotterIndicator, Class has already been created ... register subclasses (+15 more)

### Community 16 - "Community 16"
Cohesion: 0.08
Nodes (40): Accum, AllN, AnyN, ApplyN, Average, BaseApplyN, ExponentialSmoothing, ExponentialSmoothingDynamic (+32 more)

### Community 17 - "Community 17"
Cohesion: 0.04
Nodes (45): accdecoscillator, aroon, atr, awesomeoscillator, basicops, bollinger, cci, crossover (+37 more)

### Community 18 - "Community 18"
Cohesion: 0.05
Nodes (23): DoubleExponentialMovingAverage, DEMA was first time introduced in 1994, in the article "Smoothing Data with, TEMA was first time introduced in 1994, in the article "Smoothing Data with, TripleExponentialMovingAverage, DicksonMovingAverage, By Nathan Dickson      The *Dickson Moving Average* combines the ``ZeroLagIndica, ExponentialMovingAverage, A Moving Average that smoothes data exponentially over time.      It is a subcla (+15 more)

### Community 19 - "Community 19"
Cohesion: 0.07
Nodes (20): dict, OrderedDict, py3, AutoDict, AutoDictList, AutoOrderedDict, DotDict, date2num() (+12 more)

### Community 20 - "Community 20"
Cohesion: 0.08
Nodes (3): AbstractDataBase, CSVDataBase, DataClone

### Community 21 - "Community 21"
Cohesion: 0.07
Nodes (11): API, OandaNetworkError, OandaRequestError, OandaStore, OandaStreamError, OandaTimeFrameError, Singleton class wrapping to control the connections to Oanda.      Params:, Returns ``DataCls`` with args, kwargs (+3 more)

### Community 22 - "Community 22"
Cohesion: 0.07
Nodes (19): Analyzer, MetaAnalyzer, Support for invoking ``len`` on analyzers by actually returning the         curr, Receives the cash/value notification before each next cycle, Receives the current cash, value, fundvalue and fund shares, Receives order notifications before each next cycle, Receives trade notifications before each next cycle, Invoked for each next invocation of the strategy, once the minum         preiod (+11 more)

### Community 23 - "Community 23"
Cohesion: 0.15
Nodes (36): Wrapper for filters added via .addfilter to turn them     into processors., SimpleFilterWrapper, TimeFrame, MetaCSVDataBase, # FIXME: These two are never used and could be removed, Returns the next eos using a trading calendar if available, Can be overriden by classes to return a timezone for input, To be overriden by subclasses which may auto-calculate the         timezone (+28 more)

### Community 24 - "Community 24"
Cohesion: 0.09
Nodes (5): Commissions are calculated by ib, but the trades calculations in the     ```Stra, Returns the needed amount of cash an operation would cost, Broker implementation for VisualChart.      This class maps the orders/positions, VCBroker, VCCommInfo

### Community 25 - "Community 25"
Cohesion: 0.14
Nodes (6): _BaseResampler, DTFaker, Returns the point of time intraday for a given time according to the         tim, Called to check if the current stored bar has to be delivered in         spite o, Adjusts the time of calculated bar (from underlying data source) by         usin, Called for each set of values produced by the data source

### Community 26 - "Community 26"
Cohesion: 0.11
Nodes (1): Strategy

### Community 27 - "Community 27"
Cohesion: 0.09
Nodes (17): HurstExponent, References:        - https://www.quantopian.com/posts/hurst-exponent       - htt, LaguerreFilter, LaguerreRSI, Defined by John F. Ehlers in `Cybernetic Analysis for Stock and Futures`,     20, CointN, OLS_BetaN, OLS_Slope_InterceptN (+9 more)

### Community 28 - "Community 28"
Cohesion: 0.10
Nodes (5): Lines, LineSeries, LineSeriesMaker(), Return the alias for a line given the index, Returns either a delayed verison of itself in the form of a         LineDelay ob

### Community 29 - "Community 29"
Cohesion: 0.10
Nodes (4): PumpEvents(), RTEventSink, _SymInfo, VCStore

### Community 30 - "Community 30"
Cohesion: 0.07
Nodes (22): annualreturn, benchmark, broker, buysell, calmar, drawdown, leverage, logreturns (+14 more)

### Community 31 - "Community 31"
Cohesion: 0.07
Nodes (9): BrokerBase, Adds a ``CommissionInfo`` object that will be the default for all assets if, Returns the current number of shares in the fund-like mode, Set the actual fundmode (True or False)          If the argument fundstartval is, Returns the actual fundmode (True or False), Add order history. See cerebro for details, Add fund history. See cerebro for details, Retrieves the ``CommissionInfo`` scheme associated with the given         ``data (+1 more)

### Community 32 - "Community 32"
Cohesion: 0.11
Nodes (5): IBBroker, IBCommInfo, Commissions are calculated by ib, but the trades calculations in the     ```Stra, Returns the needed amount of cash an operation would cost, Broker implementation for Interactive Brokers.      This class maps the orders/p

### Community 33 - "Community 33"
Cohesion: 0.17
Nodes (5): Cerebro, OptReturn, Actual implementation of run in full next mode. All objects have its         ``n, API for lineiterators to disable runonce (see HeikinAshi), Add a history of orders to be directly executed in the broker for         perfor

### Community 34 - "Community 34"
Cohesion: 0.18
Nodes (19): All, And, Any, Cmp, CmpEx, DivByZero, DivZeroByZero, If (+11 more)

### Community 35 - "Community 35"
Cohesion: 0.09
Nodes (15): codecs, VChartFeed, MetaVChartFile, Class has already been created ... register, # FIXME: find reference to tick counter for format, getdata(), parse_args(), runstrat() (+7 more)

### Community 36 - "Community 36"
Cohesion: 0.10
Nodes (11): IBData, MetaIBData, Returns ``True`` to notify ``Cerebro`` that preloading and runonce         shoul, Receives an environment (cerebro) and passes it over to the store it         bel, Parses dataname generates a default contract, Starts the IB connecction and gets the real contract and         contractdetails, Class has already been created ... register, Stops and tells the store to stop (+3 more)

### Community 37 - "Community 37"
Cohesion: 0.10
Nodes (18): FixedPerc, parse_args(), This sizer simply returns a fixed size for any operation      Params:       - ``, runstrat(), parse_args(), runstrat(), parse_args(), runstrat() (+10 more)

### Community 38 - "Community 38"
Cohesion: 0.09
Nodes (23): backtrader_indicators_contrib, backtrader_studies_contrib, brokers, cerebro, dataseries, errors, feed, flt (+15 more)

### Community 39 - "Community 39"
Cohesion: 0.09
Nodes (13): AutoOrderedDict, _Bar, This class is a placeholder for the values of the standard lines of a     DataBa, Initializes a bar to the default not-updated vaues, Returns if a bar has already been updated          Uses the fact that NaN is the, Updates a bar with the values from data          Returns True if the update was, Updates the current trade. The logic does not check if the         trade is reve, Represents the status and update event for each update a Trade has      This obj (+5 more)

### Community 40 - "Community 40"
Cohesion: 0.10
Nodes (4): IBStore, Singleton class wrapping an ibpy ibConnection instance.      The parameters can, Calculate a duration in between 2 datetimes, Calculate a duration in between 2 datetimes. Returns single size

### Community 41 - "Community 41"
Cohesion: 0.16
Nodes (1): OandaBroker

### Community 42 - "Community 42"
Cohesion: 0.13
Nodes (14): ADFormatter, ADLocator, dateutil_relativedelta, matplotlib_dates, AutoDateFormatter, AutoDateLocator, _idx2dt(), Pick the best locator based on a distance. (+6 more)

### Community 43 - "Community 43"
Cohesion: 0.10
Nodes (19): btcsv, chainer, csvgeneric, ibdata, ibstore, influxfeed, mt4csv, oanda (+11 more)

### Community 44 - "Community 44"
Cohesion: 0.10
Nodes (7): Total, Average, Compound and Annualized Returns calculated using a     logarithm, Returns, This analyzer calculates the Returns by looking at the beginning     and end of, TimeReturn, Variability-Weighted Return: Better SharpeRatio with Log Returns      Alias:, VWR, TimeFrameAnalyzerBase

### Community 45 - "Community 45"
Cohesion: 0.22
Nodes (2): PInfo, Plot_OldSync

### Community 46 - "Community 46"
Cohesion: 0.18
Nodes (8): MultiCursor, MultiCursor2, Abstract base class for GUI neutral widgets, Set whether the widget is active., Get whether the widget is active., Return True if event should be ignored.         This method (or a version of it), Provide a vertical (default) and/or horizontal line cursor shared between     mu, Widget

### Community 47 - "Community 47"
Cohesion: 0.19
Nodes (5): Actual implementation of run in vector mode.         Strategies are still invoke, The system wide writer class.      It can be parametrized with:        - ``out``, WriterBase, WriterFile, WriterStringIO

### Community 48 - "Community 48"
Cohesion: 0.13
Nodes (6): Reuses queue for tickerId, returning the new tickerId and q, Creates ticker/Queue for data delivery to a data feed, Extension of the raw reqHistoricalData proxy, which takes two dates         rath, Proxy to reqHistorical Data, Creates a request for (5 seconds) Real Time Bars          Params:           - co, Creates a MarketData subscription          Params:           - contract: a ib.ex

### Community 49 - "Community 49"
Cohesion: 0.13
Nodes (9): Analyzer, AnnualReturn, This analyzer calculates the AnnualReturns by looking at the beginning     and e, Extension of the SharpeRatio which returns the Sharpe Ratio directly in     annu, This analyzer calculates the SharpeRatio of a strategy using a risk free     ass, SharpeRatio, SharpeRatio_A, Provides statistics on closed trades (keeps also the count of open ones) (+1 more)

### Community 50 - "Community 50"
Cohesion: 0.16
Nodes (6): Adds a SignalStrategy subclass which can accept signals, Receive data notifications in cerebro          This method can be overridden in, Adds a *callback* to the list of callbacks that will be called with the, Returns the broker instance.          This is also available as a ``property`` b, Plots the strategies inside cerebro          If ``plotter`` is None a default ``, Timer

### Community 51 - "Community 51"
Cohesion: 0.16
Nodes (6): OandaData, Returns ``True`` to notify ``Cerebro`` that preloading and runonce         shoul, Receives an environment (cerebro) and passes it over to the store it         bel, Starts the Oanda connecction and gets the real contract and         contractdeta, Stops and tells the store to stop, Oanda Data Feed.      Params:        - ``qcheck`` (default: ``0.5``)          Ti

### Community 52 - "Community 52"
Cohesion: 0.14
Nodes (7): MetaRollOver, Returns ``True`` to notify ``Cerebro`` that preloading and runonce         shoul, To be overriden by subclasses which may auto-calculate the         timezone, Class has already been created ... register, Intercept const. to copy timeframe/compression from 1st data, Class that rolls over to the next future when a condition is met      Params:, RollOver

### Community 53 - "Community 53"
Cohesion: 0.22
Nodes (12): _AroonBase, AroonDown, AroonOscillator, AroonUp, AroonUpDown, AroonUpDownOscillator, This is the AroonDown from the indicator AroonUpDown developed by Tushar     Cha, Developed by Tushar Chande in 1995.      It tries to determine if a trend exists (+4 more)

### Community 54 - "Community 54"
Cohesion: 0.31
Nodes (1): Returns a given data by name using the environment (cerebro)

### Community 55 - "Community 55"
Cohesion: 0.13
Nodes (7): Chainer, MetaChainer, Class has already been created ... register, Intercept const. to copy timeframe/compression from 1st data, Class that chains datas, Returns ``True`` to notify ``Cerebro`` that preloading and runonce         shoul, To be overriden by subclasses which may auto-calculate the         timezone

### Community 56 - "Community 56"
Cohesion: 0.26
Nodes (11): matplotlib_collections, matplotlib_legend, matplotlib_lines, CandlestickPlotHandler, LineOnClosePlotHandler, OHLCPlotHandler, plot_candlestick(), plot_lineonclose() (+3 more)

### Community 57 - "Community 57"
Cohesion: 0.22
Nodes (8): _CrossBase, CrossDown, CrossOver, CrossUp, NonZeroDifference, This indicator gives a signal if the provided datas (2) cross up or down., Keeps track of the difference between two data inputs skipping, memorizing     t, This indicator gives a signal if the 1st provided data crosses over the 2nd

### Community 58 - "Community 58"
Cohesion: 0.38
Nodes (11): AverageDirectionalMovementIndex, AverageDirectionalMovementIndexRating, _DirectionalIndicator, DirectionalMovement, DirectionalMovementIndex, DownMove, MinusDirectionalIndicator, PlusDirectionalIndicator (+3 more)

### Community 59 - "Community 59"
Cohesion: 0.29
Nodes (12): btrun(), getdatas(), getfunctions(), getmodclasses(), getmodfunctions(), getobjects(), loadmodule(), loadmodule2() (+4 more)

### Community 60 - "Community 60"
Cohesion: 0.22
Nodes (9): Fills one by one bars as needed from time_start to time_end          Invalidates, This class can be applied to a data source as a filter and will filter out     i, Return Values:            - False: nothing to filter           - True: filter cu, Return Values:            - False: data stream was not touched           - True:, Bar Filler for a Data Source inside the declared session start/end times.      T, Params:           - data: the data source to filter/process          Returns:, SessionFiller, SessionFilter (+1 more)

### Community 61 - "Community 61"
Cohesion: 0.26
Nodes (8): Observer, BuySell, This observer keeps track of the individual buy/sell orders (individual     exec, DrawDown, DrawDown_Old, DrawDownLength, This observer keeps track of the current drawdown level (plotted) and     the ma, This observer keeps track of the current drawdown length (plotted) and     the d

### Community 62 - "Community 62"
Cohesion: 0.22
Nodes (10): Broker, Cash, FundShares, FundValue, This observer keeps track of the current fund-like value      Params: None, This observer keeps track of the current fund-like shares      Params: None, This observer keeps track of the current amount of cash in the broker      Param, This observer keeps track of the current portfolio value in the broker     inclu (+2 more)

### Community 63 - "Community 63"
Cohesion: 0.24
Nodes (5): _execute(), FakeCommInfo, FakeData, Minimal interface to avoid errors when trade tries to get information from     t, test_run()

### Community 64 - "Community 64"
Cohesion: 0.36
Nodes (7): Indicator, DownDay, DownDayBool, Defined by J. Welles Wilder, Jr. in 1978 in his book *"New Concepts in     Techn, RelativeStrengthIndex, UpDay, UpDayBool

### Community 65 - "Community 65"
Cohesion: 0.21
Nodes (8): Momentum, MomentumOscillator, RateOfChange, RateOfChange100, Measures the ratio of change in prices over a period with base 100      This is, Measures the change in price by calculating the difference between the     curre, Measures the ratio of change in prices over a period      Formula:       - mosc, Measures the ratio of change in prices over a period      Formula:       - roc =

### Community 66 - "Community 66"
Cohesion: 0.21
Nodes (6): IQFeedTool, Build Pandas Dataframe in memory, Load ticker list from txt file, Encode IQFeed API messages., Send data query to IQFeed API., Request historical 5 minute data from DTN.

### Community 67 - "Community 67"
Cohesion: 0.22
Nodes (5): ParamsBase, ParamsBase, This class is used as base for tests that check the proper     handling of meta, SampleParamsHolder, TestStrategy

### Community 68 - "Community 68"
Cohesion: 0.18
Nodes (5): HeikinAshi, The filter remodels the open, high, low, close to make HeikinAshi     candlestic, object, StFetcher, YahooDownload

### Community 69 - "Community 69"
Cohesion: 0.18
Nodes (9): Description:     The Relative Momentum Index was developed by Roger Altman and w, RelativeMomentumIndex, Subclass of RSI which changes parameers ``safediv`` to ``True`` as the     defau, Uses a SimpleMovingAverage as described in Wikipedia and other soures      See:, Uses an ExponentialMovingAverage as described in Wikipedia      See:       - htt, RSI_EMA, RSI_Safe, RSI_SMA (+1 more)

### Community 70 - "Community 70"
Cohesion: 0.33
Nodes (7): This version displays the 3 possible lines:        - percK       - percD       -, By Dr. George Lane in the 50s. It compares a closing price to the price     rang, The regular (or slow version) adds an additional moving average layer and     th, Stochastic, _StochasticBase, StochasticFast, StochasticFull

### Community 71 - "Community 71"
Cohesion: 0.22
Nodes (5): DayStepsCloseFilter, DayStepsReplayFilter, Replays a bar in 2 steps:        - In the 1st step the "Open-High-Low" could be, Called when the data is no longer producing bars         Can be called multiple, St

### Community 72 - "Community 72"
Cohesion: 0.24
Nodes (8): AllInSizer, AllInSizerInt, PercentSizer, PercentSizerInt, This sizer return percents of available cash      Params:       - ``percents`` (, This sizer return all available cash of broker       Params:        - ``percents, This sizer return percents of available cash in form of size truncated     to an, This sizer return all available cash of broker with the     size truncated to an

### Community 73 - "Community 73"
Cohesion: 0.20
Nodes (5): Cancels a Queue for data delivery, Signal end of contractdetails, Cancels an existing HistoricalData request          Params:           - q: the Q, Cancels an existing MarketData subscription          Params:           - q: the, Receives the events of a historical data request

### Community 74 - "Community 74"
Cohesion: 0.22
Nodes (4): DrawDown, This analyzer calculates trading system drawdowns on the chosen     timeframe wh, This analyzer calculates trading system drawdowns stats such as drawdown     val, TimeDrawDown

### Community 75 - "Community 75"
Cohesion: 0.31
Nodes (8): BacktraderError, FromModuleImportError, ModuleImportError, Base exception for all other exceptions, Requests the platform to skip this strategy for backtesting. To be     raised du, Raised if a class requests a module to be present to work and it cannot     be i, StrategySkipError, Exception

### Community 76 - "Community 76"
Cohesion: 0.22
Nodes (5): NoExit, parse_args(), runstrat(), SMACrossOver, St

### Community 77 - "Community 77"
Cohesion: 0.29
Nodes (7): matplotlib_ticker, getlocator(), MyDateFormatter, MyVolFormatter, patch_formatter(), patch_locator(), Return the label for time x at position pos

### Community 78 - "Community 78"
Cohesion: 0.22
Nodes (6): DataTrades, MetaDataTrades, This observer keeps track of full trades and plot the PnL level achieved     whe, Trades, trade, uuid

### Community 79 - "Community 79"
Cohesion: 0.24
Nodes (4): FakeCommInfo, FakeData, Minimal interface to avoid errors when trade tries to get information from     t, test_run()

### Community 80 - "Community 80"
Cohesion: 0.31
Nodes (2): LongShortStrategy, This strategy buys/sells upong the close price crossing     upwards/downwards a

### Community 81 - "Community 81"
Cohesion: 0.25
Nodes (4): Adds a ``Data Feed`` instance to the mix.          If ``name`` is not None it wi, Chains several data feeds into one          If ``name`` is passed as named argum, Adds a ``Data Feed`` to be replayed by the system          If ``name`` is not No, Adds a ``Data Feed`` to be resample by the system          If ``name`` is not No

### Community 82 - "Community 82"
Cohesion: 0.22
Nodes (8): bsplitter, calendardays, datafiller, datafilter, daysteps, heikinashi, renko, session

### Community 83 - "Community 83"
Cohesion: 0.33
Nodes (8): comminfo, CommInfo, CommInfo_Futures, CommInfo_Futures_Fixed, CommInfo_Futures_Perc, CommInfo_Stocks, CommInfo_Stocks_Fixed, CommInfo_Stocks_Perc

### Community 84 - "Community 84"
Cohesion: 0.28
Nodes (6): This is intended to load files which were downloaded before Yahoo     discontinu, Executes a direct download of data from Yahoo servers for the given time     ran, Parses pre-downloaded Yahoo CSV Data Feeds (or locally generated if they     com, YahooFinanceCSVData, YahooFinanceData, YahooLegacyCSV

### Community 85 - "Community 85"
Cohesion: 0.22
Nodes (1): TestStrategy

### Community 86 - "Community 86"
Cohesion: 0.36
Nodes (6): AverageTrueRange, Defined by J. Welles Wilder, Jr. in 1978 in his book *"New Concepts in     Techn, Defined by J. Welles Wilder, Jr. in 1978 in his book New Concepts in     Technic, TrueHigh, TrueLow, TrueRange

### Community 87 - "Community 87"
Cohesion: 0.22
Nodes (1): TestStrategy

### Community 88 - "Community 88"
Cohesion: 0.31
Nodes (6): FixedReverser, FixedSize, FixedSizeTarget, This sizer simply returns a fixed size for any operation.     Size can be contro, This sizer returns the needes fixed size to reverse an open position or     the, This sizer simply returns a fixed target size, useful when coupled     with Targ

### Community 89 - "Community 89"
Cohesion: 0.22
Nodes (1): TestStrategy

### Community 90 - "Community 90"
Cohesion: 0.22
Nodes (4): St, Bar Filler to add missing calendar days to trading days, Empty bars (NaN) or with last close price are added for weekdays with no, WeekDaysFiller

### Community 91 - "Community 91"
Cohesion: 0.31
Nodes (2): LongShortStrategy, This strategy buys/sells upong the close price crossing     upwards/downwards a

### Community 92 - "Community 92"
Cohesion: 0.39
Nodes (3): AbstractDataBase, DataFiller, This class will fill gaps in the source data using the following     information

### Community 93 - "Community 93"
Cohesion: 0.25
Nodes (3): MetaLineActions, Returns either a delayed verison of itself in the form of a         LineDelay ob, Metaclass for Lineactions      Scans the instance before init for LineBuffer (or

### Community 94 - "Community 94"
Cohesion: 0.39
Nodes (2): MetaBase, type

### Community 95 - "Community 95"
Cohesion: 0.25
Nodes (3): Extension of regular Value observer to add leveraged view, St, ValueUnlever

### Community 96 - "Community 96"
Cohesion: 0.25
Nodes (7): colorsys, matplotlib_colors, matplotlib_path, Given the location and size of the box, return the path of     the box around it, Shade Color     This color utility function allows the user to easily darken or, shade_color(), tag_box_style()

### Community 97 - "Community 97"
Cohesion: 0.32
Nodes (4): BuySellArrows, parse_args(), runstrat(), St

### Community 98 - "Community 98"
Cohesion: 0.32
Nodes (5): MACrossOver, parse_args(), PearsonR, runstrat(), scipy_stats

### Community 99 - "Community 99"
Cohesion: 0.32
Nodes (5): MetaMovAvBase, MovAv, MovingAverage, MovingAverageBase, MovingAverage (alias MovAv)      A placeholder to gather all Moving Average Type

### Community 100 - "Community 100"
Cohesion: 0.25
Nodes (4): Subclass of TheStrategy to simply change the parameters, This strategy is capable of:        - Going Long with a Moving Average upwards C, TheStrategy, TheStrategy2

### Community 101 - "Community 101"
Cohesion: 0.36
Nodes (4): LogReturns, LogReturns2, This observer stores the *log returns* of the strategy or a      Params:, Extends the observer LogReturns to show two instruments

### Community 102 - "Community 102"
Cohesion: 0.36
Nodes (3): MyStrategy, Logging function fot this strategy, OrderObserver

### Community 103 - "Community 103"
Cohesion: 0.32
Nodes (4): getdata(), parse_args(), runstrat(), St

### Community 104 - "Community 104"
Cohesion: 0.43
Nodes (1): RelativeVolumeByBar

### Community 105 - "Community 105"
Cohesion: 0.39
Nodes (1): TestStrategy

### Community 106 - "Community 106"
Cohesion: 0.32
Nodes (4): NYSE_2016, parse_args(), runstrat(), St

### Community 107 - "Community 107"
Cohesion: 0.33
Nodes (2): Calmar, This analyzer calculates the CalmarRatio     timeframe which can be different fr

### Community 108 - "Community 108"
Cohesion: 0.29
Nodes (3): SQN or SystemQualityNumber. Defined by Van K. Tharp to categorize trading     sy, Replace default implementation to instantiate an AutoOrdereDict         rather t, SQN

### Community 109 - "Community 109"
Cohesion: 0.33
Nodes (3): CSVFeedBase, FeedBase, MetaAbstractDataBase

### Community 110 - "Community 110"
Cohesion: 0.43
Nodes (2): Logging function fot this strategy, SMACrossOver

### Community 111 - "Community 111"
Cohesion: 0.38
Nodes (4): BidAskCSV, parse_args(), runstrategy(), St

### Community 112 - "Community 112"
Cohesion: 0.33
Nodes (3): parse_args(), runstrat(), St

### Community 113 - "Community 113"
Cohesion: 0.29
Nodes (5): MT4CSVData, Parses a `Metatrader4 <https://www.metaquotes.net/en/metatrader4>`_ History, Parses a `SierraChart <http://www.sierrachart.com>`_ CSV exported file.      Spe, SierraChartCSVData, GenericCSVData

### Community 114 - "Community 114"
Cohesion: 0.33
Nodes (4): PandasData, PandasDirectData, Uses a Pandas DataFrame as the feed source, using indices into column     names, Uses a Pandas DataFrame as the feed source, iterating directly over the     tupl

### Community 115 - "Community 115"
Cohesion: 0.33
Nodes (4): CalendarDays, Bar Filler to add missing calendar days to trading days      Params:        - fi, If the data has a gap larger than 1 day amongst bars, the missing bars         a, Fills one by one bars as needed from time_start to time_end          Invalidates

### Community 116 - "Community 116"
Cohesion: 0.29
Nodes (3): BarReplayer_Open, This filters splits a bar in two parts:        - ``Open``: the opening price of, Called when the data is no longer producing bars         Can be called multiple

### Community 117 - "Community 117"
Cohesion: 0.38
Nodes (4): BollingerBands, BollingerBandsPct, Defined by John Bollinger in the 80s. It measures volatility by defining     upp, Extends the Bollinger Bands with a Percentage line

### Community 118 - "Community 118"
Cohesion: 0.38
Nodes (4): MeanDeviation, Calculates the standard deviation of the passed data for a given period      Not, MeanDeviation (alias MeanDev)      Calculates the Mean Deviation of the passed d, StandardDeviation

### Community 119 - "Community 119"
Cohesion: 0.43
Nodes (5): Envelope, _EnvelopeBase, EnvelopeMixIn, MixIn class to create a subclass with another indicator. The main line of     th, It creates envelopes bands separated from the source data by a given     percent

### Community 120 - "Community 120"
Cohesion: 0.38
Nodes (4): MACD, MACDHisto, Moving Average Convergence Divergence. Defined by Gerald Appel in the 70s., Subclass of MACD which adds a "histogram" of the difference between the     macd

### Community 121 - "Community 121"
Cohesion: 0.38
Nodes (4): Oscillator, OscillatorMixIn, MixIn class to create a subclass with another indicator. The main line of     th, Oscillation of a given data around another data      Datas:       This indicator

### Community 122 - "Community 122"
Cohesion: 0.57
Nodes (4): DemarkPivotPoint, FibonacciPivotPoint, PivotPoint, Defines a level of significance by taking into account the average of price

### Community 123 - "Community 123"
Cohesion: 0.57
Nodes (5): PercentagePriceOscillator, PercentagePriceOscillatorShort, _PriceOscBase, PriceOscillator, Shows the difference between a short and long exponential moving     averages ex

### Community 124 - "Community 124"
Cohesion: 0.38
Nodes (4): Defined by Jack Hutson in the 80s and shows the Rate of Change (%) or slope, Extension of Trix with a signal line (ala MACD)      Formula:       - trix = Tri, Trix, TrixSignal

### Community 125 - "Community 125"
Cohesion: 0.33
Nodes (4): Developed by Larry Williams to show the relation of closing prices to     the hi, By Larry Williams. It does cumulatively measure if the price is     accumulating, WilliamsAD, WilliamsR

### Community 126 - "Community 126"
Cohesion: 0.43
Nodes (2): St, TestInd

### Community 127 - "Community 127"
Cohesion: 0.38
Nodes (2): MultiDataStrategy, This strategy operates on 2 datas. The expectation is that the 2 datas are     c

### Community 128 - "Community 128"
Cohesion: 0.38
Nodes (2): MultiDataStrategy, This strategy operates on 2 datas. The expectation is that the 2 datas are     c

### Community 129 - "Community 129"
Cohesion: 0.43
Nodes (2): MultiTradeStrategy, This strategy buys/sells upong the close price crossing     upwards/downwards a

### Community 130 - "Community 130"
Cohesion: 0.33
Nodes (4): parse_args(), runstrat(), SlipSt, SMACrossOver

### Community 131 - "Community 131"
Cohesion: 0.52
Nodes (4): AutoStopOrStopTrail, BaseStrategy, ManualStopOrStopTrail, ManualStopOrStopTrailCheat

### Community 132 - "Community 132"
Cohesion: 0.29
Nodes (3): Returns all account value infos sent by TWS during regular updates         Waits, Returns the net liquidation value sent by TWS during regular updates         Wai, Returns the total cash value sent by TWS during regular updates         Waits fo

### Community 134 - "Community 134"
Cohesion: 0.48
Nodes (1): TestStrategy

### Community 135 - "Community 135"
Cohesion: 0.48
Nodes (1): TestStrategy

### Community 136 - "Community 136"
Cohesion: 0.43
Nodes (2): flushfile, StdOutDevNull

### Community 137 - "Community 137"
Cohesion: 0.33
Nodes (2): GrossLeverage, This analyzer calculates the Gross Leverage of the current strategy     on a tim

### Community 138 - "Community 138"
Cohesion: 0.33
Nodes (2): LogReturnsRolling, This analyzer calculates rolling returns for a given timeframe and     compressi

### Community 139 - "Community 139"
Cohesion: 0.33
Nodes (3): PyFolio, Returns a tuple of 4 elements which can be used for further processing with, This analyzer uses 4 children analyzers to collect data and transforms it     in

### Community 140 - "Community 140"
Cohesion: 0.40
Nodes (1): Filter

### Community 141 - "Community 141"
Cohesion: 0.33
Nodes (1): MetaLineIterator

### Community 142 - "Community 142"
Cohesion: 0.40
Nodes (6): average(), Args:       x: iterable with len        oneless: (default ``False``) reduces the, Args:       x: iterable with len      Returns:       A list with the variance fo, Args:       x: iterable with len        bessel: (default ``False``) to be passed, standarddev(), variance()

### Community 143 - "Community 143"
Cohesion: 0.40
Nodes (3): parse_args(), runstrat(), St

### Community 144 - "Community 144"
Cohesion: 0.47
Nodes (1): St

### Community 145 - "Community 145"
Cohesion: 0.47
Nodes (4): PandasDataOptix, parse_args(), runstrat(), StrategyOptix

### Community 146 - "Community 146"
Cohesion: 0.40
Nodes (4): Quandl, QuandlCSV, Executes a direct download of data from Quandl servers for the given time     ra, Parses pre-downloaded Quandl CSV Data Feeds (or locally generated if they     co

### Community 147 - "Community 147"
Cohesion: 0.33
Nodes (3): Filter, Modify the data stream to draw Renko bars (or bricks)      Params:        - ``hi, Renko

### Community 148 - "Community 148"
Cohesion: 0.33
Nodes (2): CommodityChannelIndex, Introduced by Donald Lambert in 1980 to measure variations of the     "typical p

### Community 149 - "Community 149"
Cohesion: 0.40
Nodes (3): parse_args(), runstrat(), TheStrategy

### Community 150 - "Community 150"
Cohesion: 0.40
Nodes (3): parse_args(), runstrat(), St

### Community 151 - "Community 151"
Cohesion: 0.33
Nodes (2): This strategy is loosely based on some of the examples from the Van     K. Tharp, TheStrategy

### Community 152 - "Community 152"
Cohesion: 0.47
Nodes (2): OrderExecutionStrategy, Logging function fot this strategy

### Community 153 - "Community 153"
Cohesion: 0.47
Nodes (2): SmaCross, St

### Community 154 - "Community 154"
Cohesion: 0.47
Nodes (1): PairTradingStrategy

### Community 155 - "Community 155"
Cohesion: 0.47
Nodes (4): parse_args(), runstrat(), SMACloseSignal, SMAExitSignal

### Community 156 - "Community 156"
Cohesion: 0.73
Nodes (5): average(), parse_args(), run(), standarddev(), variance()

### Community 157 - "Community 157"
Cohesion: 0.47
Nodes (4): parse_args(), runstrat(), St0, St1

### Community 158 - "Community 158"
Cohesion: 0.40
Nodes (4): This class is used for testing that inheriting from base class that     uses `fr, Instantiate the TestFrompackages and see that no exception is raised     Bug Dis, test_run(), TestFrompackages

### Community 159 - "Community 159"
Cohesion: 0.40
Nodes (1): TestStrategy

### Community 160 - "Community 160"
Cohesion: 0.33
Nodes (1): St

### Community 161 - "Community 161"
Cohesion: 0.33
Nodes (1): St

### Community 162 - "Community 162"
Cohesion: 0.33
Nodes (1): St

### Community 163 - "Community 163"
Cohesion: 0.33
Nodes (3): InfluxDBTool, Write Pandas Dataframe to InfluxDB database, Load ticker list from txt file

### Community 164 - "Community 164"
Cohesion: 0.40
Nodes (2): PositionsValue, This analyzer reports the value of the positions of the current set of     datas

### Community 165 - "Community 165"
Cohesion: 0.40
Nodes (2): This analyzer reports the transactions occurred with each an every data in     t, Transactions

### Community 166 - "Community 166"
Cohesion: 0.40
Nodes (1): _TALibIndicator

### Community 167 - "Community 167"
Cohesion: 0.40
Nodes (4): bbroker, ibbroker, oandabroker, vcbroker

### Community 168 - "Community 168"
Cohesion: 0.50
Nodes (3): parse_args(), runstrat(), St

### Community 169 - "Community 169"
Cohesion: 0.40
Nodes (3): OandaCommInfo, Returns the needed amount of cash an operation would cost, CommInfoBase

### Community 170 - "Community 170"
Cohesion: 0.40
Nodes (1): SMAStrategy

### Community 171 - "Community 171"
Cohesion: 0.40
Nodes (1): SMAStrategy

### Community 172 - "Community 172"
Cohesion: 0.40
Nodes (3): BacktraderCSV, BacktraderCSVData, Parses a self-defined CSV Data used for testing.      Specific parameters:

### Community 173 - "Community 173"
Cohesion: 0.40
Nodes (2): Support for `Visual Chart <www.visualchart.com>`_ binary on-disk files for     b, VChartData

### Community 174 - "Community 174"
Cohesion: 0.40
Nodes (3): Parses a `VisualChart <http://www.visualchart.com>`_ CSV exported file.      Spe, VChartCSV, VChartCSVData

### Community 175 - "Community 175"
Cohesion: 0.40
Nodes (2): Support for `Visual Chart <www.visualchart.com>`_ binary on-disk files for     b, VChartFile

### Community 176 - "Community 176"
Cohesion: 0.40
Nodes (2): DataFilter, This class filters out bars from a given data source. In addition to the     sta

### Community 177 - "Community 177"
Cohesion: 0.40
Nodes (2): DetrendedPriceOscillator, Defined by Joe DiNapoli in his book *"Trading with DiNapoli levels"*      It mea

### Community 178 - "Community 178"
Cohesion: 0.50
Nodes (3): parse_args(), runstrat(), St

### Community 179 - "Community 179"
Cohesion: 0.50
Nodes (3): parse_args(), runstrat(), TestSizer

### Community 180 - "Community 180"
Cohesion: 0.50
Nodes (2): MyStrategy, Logging function fot this strategy

### Community 181 - "Community 181"
Cohesion: 0.40
Nodes (2): This observer stores the *returns* of the strategy.      Params:        - ``time, TimeReturn

### Community 182 - "Community 182"
Cohesion: 0.50
Nodes (3): OptimizeStrategy, parse_args(), runstrat()

### Community 183 - "Community 183"
Cohesion: 0.40
Nodes (2): This strategy is loosely based on some of the examples from the Van     K. Tharp, TheStrategy

### Community 184 - "Community 184"
Cohesion: 0.50
Nodes (2): Store provider for Visual Chart binary files      Params:        - ``path`` (def, VChartFile

### Community 185 - "Community 185"
Cohesion: 0.50
Nodes (3): parse_args(), runstrat(), TALibStrategy

### Community 186 - "Community 186"
Cohesion: 0.50
Nodes (3): parse_args(), runstrat(), TALibStrategy

### Community 187 - "Community 187"
Cohesion: 0.40
Nodes (1): St

### Community 188 - "Community 188"
Cohesion: 0.50
Nodes (2): PeriodStats, Calculates basic statistics for given timeframe      Params:        - ``timefram

### Community 189 - "Community 189"
Cohesion: 0.50
Nodes (2): The core method to perform backtesting. Any ``kwargs`` passed to it         will, Adds a ``Strategy`` class to the mix for a single pass run.         Instantiatio

### Community 190 - "Community 190"
Cohesion: 0.50
Nodes (2): Handy function which turns things into things that can be iterated upon, Adds a ``Strategy`` class to the mix for optimization. Instantiation         wil

### Community 191 - "Community 191"
Cohesion: 0.50
Nodes (2): MetaLineRoot, Once the object is created (effectively pre-init) the "owner" of this     class

### Community 192 - "Community 192"
Cohesion: 0.50
Nodes (3): BaseApplyN, PercentRank, Measures the percent rank of the current value with respect to that of     perio

### Community 193 - "Community 193"
Cohesion: 0.50
Nodes (1): St

### Community 194 - "Community 194"
Cohesion: 0.50
Nodes (2): Fractal, References:         [Ref 1] http://www.investopedia.com/articles/trading/06/frac

### Community 195 - "Community 195"
Cohesion: 0.50
Nodes (2): See:       - http://www.vortexindicator.com/VFX_VORTEX.PDF, Vortex

### Community 196 - "Community 196"
Cohesion: 0.50
Nodes (2): BlazeData, Support for `Blaze <blaze.pydata.org>`_ ``Data`` objects.      Only numeric indi

### Community 197 - "Community 197"
Cohesion: 0.50
Nodes (2): GenericCSVData, Parses a CSV file according to the order and field presence defined by the     p

### Community 198 - "Community 198"
Cohesion: 0.50
Nodes (2): DaySplitter_Close, Splits a daily bar in two parts simulating 2 ticks which will be used to     rep

### Community 199 - "Community 199"
Cohesion: 0.67
Nodes (1): St

### Community 200 - "Community 200"
Cohesion: 0.50
Nodes (2): AccelerationDecelerationOscillator, Acceleration/Deceleration Technical Indicator (AC) measures acceleration     and

### Community 201 - "Community 201"
Cohesion: 0.50
Nodes (2): AwesomeOscillator, Awesome Oscillator (AO) is a momentum indicator reflecting the precise     chang

### Community 202 - "Community 202"
Cohesion: 0.50
Nodes (2): DV2, RSI(2) alternative     Developed by David Varadi of http://cssanalytics.wordpres

### Community 203 - "Community 203"
Cohesion: 0.50
Nodes (2): haDelta, Heikin Ashi Delta. Defined by Dan Valcu in his book "Heikin-Ashi: How to     Tra

### Community 204 - "Community 204"
Cohesion: 0.50
Nodes (2): HeikinAshi, Heikin Ashi candlesticks in the forms of lines      Formula:         ha_open = (

### Community 205 - "Community 205"
Cohesion: 0.50
Nodes (2): Ichimoku, Developed and published in his book in 1969 by journalist Goichi Hosoda      For

### Community 206 - "Community 206"
Cohesion: 0.50
Nodes (2): KnowSureThing, It is a "summed" momentum indicator. Developed by Martin Pring and     published

### Community 207 - "Community 207"
Cohesion: 0.50
Nodes (2): PercentChange, Measures the perccentage change of the current value with respect to that

### Community 208 - "Community 208"
Cohesion: 0.50
Nodes (2): PrettyGoodOscillator, The "Pretty Good Oscillator" (PGO) by Mark Johnson measures the distance of

### Community 209 - "Community 209"
Cohesion: 0.50
Nodes (2): The True Strength Indicators was first introduced in Stocks & Commodities     Ma, TrueStrengthIndicator

### Community 210 - "Community 210"
Cohesion: 0.50
Nodes (2): Formula:       # Buying Pressure = Close - TrueLow       BP = Close - Minimum(Lo, UltimateOscillator

### Community 211 - "Community 211"
Cohesion: 0.50
Nodes (2): See:       - http://www.vortexindicator.com/VFX_VORTEX.PDF, Vortex

### Community 212 - "Community 212"
Cohesion: 0.50
Nodes (1): St

### Community 213 - "Community 213"
Cohesion: 0.50
Nodes (1): St

### Community 214 - "Community 214"
Cohesion: 0.50
Nodes (1): St

### Community 215 - "Community 215"
Cohesion: 0.50
Nodes (3): This data filter simply adds the time given in param ``endtime`` to the     curr, Params:           - data: the data source to filter/process          Returns:, SessionEndFiller

### Community 216 - "Community 216"
Cohesion: 0.50
Nodes (1): St

### Community 217 - "Community 217"
Cohesion: 0.67
Nodes (2): PivotPoint, PivotPoint1

### Community 218 - "Community 218"
Cohesion: 0.50
Nodes (1): PlotScheme

### Community 219 - "Community 219"
Cohesion: 0.50
Nodes (1): St

### Community 220 - "Community 220"
Cohesion: 0.50
Nodes (1): St

### Community 221 - "Community 221"
Cohesion: 0.50
Nodes (1): SmaCross

### Community 222 - "Community 222"
Cohesion: 0.50
Nodes (2): MA_CrossOver, This is a long-only strategy which operates on a moving average cross      Note:

### Community 223 - "Community 223"
Cohesion: 0.83
Nodes (3): check_futures(), check_stocks(), test_run()

### Community 224 - "Community 224"
Cohesion: 0.50
Nodes (1): TestStrategy

### Community 225 - "Community 225"
Cohesion: 0.67
Nodes (1): Adds an ``Observer`` class to the mix. Instantiation will be done at         ``r

### Community 226 - "Community 226"
Cohesion: 0.67
Nodes (1): Signal

### Community 227 - "Community 227"
Cohesion: 0.67
Nodes (2): fixedsize, percents_sizer

### Community 228 - "Community 228"
Cohesion: 0.67
Nodes (1): St

### Community 229 - "Community 229"
Cohesion: 0.67
Nodes (1): St

### Community 230 - "Community 230"
Cohesion: 0.67
Nodes (1): St

### Community 231 - "Community 231"
Cohesion: 0.67
Nodes (2): PlotStrategy, The strategy does nothing but create indicators for plotting purposes

### Community 232 - "Community 232"
Cohesion: 0.67
Nodes (1): St

### Community 233 - "Community 233"
Cohesion: 0.67
Nodes (1): St

### Community 234 - "Community 234"
Cohesion: 0.67
Nodes (1): St

### Community 235 - "Community 235"
Cohesion: 0.67
Nodes (1): TheStrategy

### Community 236 - "Community 236"
Cohesion: 0.67
Nodes (1): CloseSMA

### Community 237 - "Community 237"
Cohesion: 0.67
Nodes (1): St

### Community 238 - "Community 238"
Cohesion: 0.67
Nodes (1): RewriteStrategy

### Community 239 - "Community 239"
Cohesion: 1.00
Nodes (1): backtrader_btrun

### Community 240 - "Community 240"
Cohesion: 1.00
Nodes (1): If signals are added to the system and the ``accumulate`` value is         set t

### Community 241 - "Community 241"
Cohesion: 1.00
Nodes (1): If signals are added to the system and the ``concurrent`` value is         set t

### Community 243 - "Community 243"
Cohesion: 1.00
Nodes (1): Called when the data is no longer producing bars          Can be called multiple

### Community 244 - "Community 244"
Cohesion: 1.00
Nodes (1): btrun

### Community 245 - "Community 245"
Cohesion: 1.00
Nodes (1): sma_crossover

### Community 246 - "Community 246"
Cohesion: 1.00
Nodes (1): Receive the event commissionReport

### Community 247 - "Community 247"
Cohesion: 1.00
Nodes (1): Receive answer and pass it to the queue

### Community 248 - "Community 248"
Cohesion: 1.00
Nodes (1): Return the pending "store" notifications

### Community 249 - "Community 249"
Cohesion: 1.00
Nodes (1): Returns broker with *args, **kwargs from registered ``BrokerCls``

### Community 250 - "Community 250"
Cohesion: 1.00
Nodes (1): Returns ``DataCls`` with args, kwargs

### Community 251 - "Community 251"
Cohesion: 1.00
Nodes (1): returns a contract from the parameters without check

### Community 252 - "Community 252"
Cohesion: 1.00
Nodes (1): Receive the event ``openOrder`` events

### Community 253 - "Community 253"
Cohesion: 1.00
Nodes (1): Receive the event ``orderStatus``

### Community 254 - "Community 254"
Cohesion: 1.00
Nodes (1): Receive event positions

### Community 255 - "Community 255"
Cohesion: 1.00
Nodes (1): Receives x seconds Real Time Bars (at the time of writing only 5         seconds

### Community 256 - "Community 256"
Cohesion: 1.00
Nodes (1): Proxy to reqAccountUpdates          If ``account`` is ``None``, wait for the ``m

### Community 257 - "Community 257"
Cohesion: 1.00
Nodes (1): Proxy to reqPositions

### Community 258 - "Community 258"
Cohesion: 1.00
Nodes (1): Returns (bool)  if a queue is still valid

## Knowledge Gaps
- **282 isolated node(s):** `Intercept the strategy parameter`, `Analyzer base class. All analyzers are subclass of this one      An Analyzer ins`, `Support for invoking ``len`` on analyzers by actually returning the         curr`, `Receives the cash/value notification before each next cycle`, `Receives the current cash, value, fundvalue and fund shares` (+277 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 26`** (1 nodes): `Strategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (1 nodes): `OandaBroker`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (2 nodes): `PInfo`, `Plot_OldSync`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (1 nodes): `Returns a given data by name using the environment (cerebro)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 80`** (2 nodes): `LongShortStrategy`, `This strategy buys/sells upong the close price crossing     upwards/downwards a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 85`** (1 nodes): `TestStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 87`** (1 nodes): `TestStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 89`** (1 nodes): `TestStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 91`** (2 nodes): `LongShortStrategy`, `This strategy buys/sells upong the close price crossing     upwards/downwards a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 94`** (2 nodes): `MetaBase`, `type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 104`** (1 nodes): `RelativeVolumeByBar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 105`** (1 nodes): `TestStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 107`** (2 nodes): `Calmar`, `This analyzer calculates the CalmarRatio     timeframe which can be different fr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 110`** (2 nodes): `Logging function fot this strategy`, `SMACrossOver`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 126`** (2 nodes): `St`, `TestInd`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 127`** (2 nodes): `MultiDataStrategy`, `This strategy operates on 2 datas. The expectation is that the 2 datas are     c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 128`** (2 nodes): `MultiDataStrategy`, `This strategy operates on 2 datas. The expectation is that the 2 datas are     c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 129`** (2 nodes): `MultiTradeStrategy`, `This strategy buys/sells upong the close price crossing     upwards/downwards a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 134`** (1 nodes): `TestStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 135`** (1 nodes): `TestStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 136`** (2 nodes): `flushfile`, `StdOutDevNull`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 137`** (2 nodes): `GrossLeverage`, `This analyzer calculates the Gross Leverage of the current strategy     on a tim`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 138`** (2 nodes): `LogReturnsRolling`, `This analyzer calculates rolling returns for a given timeframe and     compressi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 140`** (1 nodes): `Filter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 141`** (1 nodes): `MetaLineIterator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 144`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 148`** (2 nodes): `CommodityChannelIndex`, `Introduced by Donald Lambert in 1980 to measure variations of the     "typical p`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 151`** (2 nodes): `This strategy is loosely based on some of the examples from the Van     K. Tharp`, `TheStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 152`** (2 nodes): `OrderExecutionStrategy`, `Logging function fot this strategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 153`** (2 nodes): `SmaCross`, `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 154`** (1 nodes): `PairTradingStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 159`** (1 nodes): `TestStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 160`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 161`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 162`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 164`** (2 nodes): `PositionsValue`, `This analyzer reports the value of the positions of the current set of     datas`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 165`** (2 nodes): `This analyzer reports the transactions occurred with each an every data in     t`, `Transactions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 166`** (1 nodes): `_TALibIndicator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 170`** (1 nodes): `SMAStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 171`** (1 nodes): `SMAStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 173`** (2 nodes): `Support for `Visual Chart <www.visualchart.com>`_ binary on-disk files for     b`, `VChartData`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 175`** (2 nodes): `Support for `Visual Chart <www.visualchart.com>`_ binary on-disk files for     b`, `VChartFile`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 176`** (2 nodes): `DataFilter`, `This class filters out bars from a given data source. In addition to the     sta`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 177`** (2 nodes): `DetrendedPriceOscillator`, `Defined by Joe DiNapoli in his book *"Trading with DiNapoli levels"*      It mea`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 180`** (2 nodes): `MyStrategy`, `Logging function fot this strategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 181`** (2 nodes): `This observer stores the *returns* of the strategy.      Params:        - ``time`, `TimeReturn`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 183`** (2 nodes): `This strategy is loosely based on some of the examples from the Van     K. Tharp`, `TheStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 184`** (2 nodes): `Store provider for Visual Chart binary files      Params:        - ``path`` (def`, `VChartFile`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 187`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 188`** (2 nodes): `PeriodStats`, `Calculates basic statistics for given timeframe      Params:        - ``timefram`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 189`** (2 nodes): `The core method to perform backtesting. Any ``kwargs`` passed to it         will`, `Adds a ``Strategy`` class to the mix for a single pass run.         Instantiatio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (2 nodes): `Handy function which turns things into things that can be iterated upon`, `Adds a ``Strategy`` class to the mix for optimization. Instantiation         wil`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 191`** (2 nodes): `MetaLineRoot`, `Once the object is created (effectively pre-init) the "owner" of this     class`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 193`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 194`** (2 nodes): `Fractal`, `References:         [Ref 1] http://www.investopedia.com/articles/trading/06/frac`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 195`** (2 nodes): `See:       - http://www.vortexindicator.com/VFX_VORTEX.PDF`, `Vortex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 196`** (2 nodes): `BlazeData`, `Support for `Blaze <blaze.pydata.org>`_ ``Data`` objects.      Only numeric indi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 197`** (2 nodes): `GenericCSVData`, `Parses a CSV file according to the order and field presence defined by the     p`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 198`** (2 nodes): `DaySplitter_Close`, `Splits a daily bar in two parts simulating 2 ticks which will be used to     rep`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 199`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 200`** (2 nodes): `AccelerationDecelerationOscillator`, `Acceleration/Deceleration Technical Indicator (AC) measures acceleration     and`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 201`** (2 nodes): `AwesomeOscillator`, `Awesome Oscillator (AO) is a momentum indicator reflecting the precise     chang`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 202`** (2 nodes): `DV2`, `RSI(2) alternative     Developed by David Varadi of http://cssanalytics.wordpres`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 203`** (2 nodes): `haDelta`, `Heikin Ashi Delta. Defined by Dan Valcu in his book "Heikin-Ashi: How to     Tra`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 204`** (2 nodes): `HeikinAshi`, `Heikin Ashi candlesticks in the forms of lines      Formula:         ha_open = (`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 205`** (2 nodes): `Ichimoku`, `Developed and published in his book in 1969 by journalist Goichi Hosoda      For`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 206`** (2 nodes): `KnowSureThing`, `It is a "summed" momentum indicator. Developed by Martin Pring and     published`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 207`** (2 nodes): `PercentChange`, `Measures the perccentage change of the current value with respect to that`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 208`** (2 nodes): `PrettyGoodOscillator`, `The "Pretty Good Oscillator" (PGO) by Mark Johnson measures the distance of`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 209`** (2 nodes): `The True Strength Indicators was first introduced in Stocks & Commodities     Ma`, `TrueStrengthIndicator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 210`** (2 nodes): `Formula:       # Buying Pressure = Close - TrueLow       BP = Close - Minimum(Lo`, `UltimateOscillator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 211`** (2 nodes): `See:       - http://www.vortexindicator.com/VFX_VORTEX.PDF`, `Vortex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 212`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 213`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 214`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 216`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 217`** (2 nodes): `PivotPoint`, `PivotPoint1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 218`** (1 nodes): `PlotScheme`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 219`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 220`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 221`** (1 nodes): `SmaCross`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 222`** (2 nodes): `MA_CrossOver`, `This is a long-only strategy which operates on a moving average cross      Note:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 224`** (1 nodes): `TestStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 225`** (1 nodes): `Adds an ``Observer`` class to the mix. Instantiation will be done at         ``r`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 226`** (1 nodes): `Signal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 227`** (2 nodes): `fixedsize`, `percents_sizer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 228`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 229`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 230`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 231`** (2 nodes): `PlotStrategy`, `The strategy does nothing but create indicators for plotting purposes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 232`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 233`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 234`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 235`** (1 nodes): `TheStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 236`** (1 nodes): `CloseSMA`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 237`** (1 nodes): `St`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 238`** (1 nodes): `RewriteStrategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 239`** (1 nodes): `backtrader_btrun`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 240`** (1 nodes): `If signals are added to the system and the ``accumulate`` value is         set t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 241`** (1 nodes): `If signals are added to the system and the ``concurrent`` value is         set t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 243`** (1 nodes): `Called when the data is no longer producing bars          Can be called multiple`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 244`** (1 nodes): `btrun`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 245`** (1 nodes): `sma_crossover`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 246`** (1 nodes): `Receive the event commissionReport`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 247`** (1 nodes): `Receive answer and pass it to the queue`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 248`** (1 nodes): `Return the pending "store" notifications`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 249`** (1 nodes): `Returns broker with *args, **kwargs from registered ``BrokerCls```
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 250`** (1 nodes): `Returns ``DataCls`` with args, kwargs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 251`** (1 nodes): `returns a contract from the parameters without check`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 252`** (1 nodes): `Receive the event ``openOrder`` events`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 253`** (1 nodes): `Receive the event ``orderStatus```
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 254`** (1 nodes): `Receive event positions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 255`** (1 nodes): `Receives x seconds Real Time Bars (at the time of writing only 5         seconds`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 256`** (1 nodes): `Proxy to reqAccountUpdates          If ``account`` is ``None``, wait for the ``m`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 257`** (1 nodes): `Proxy to reqPositions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 258`** (1 nodes): `Returns (bool)  if a queue is still valid`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MetaParams` connect `Community 5` to `Community 31`, `Community 33`, `Community 11`, `Community 189`, `Community 47`, `Community 190`, `Community 50`, `Community 241`, `Community 240`, `Community 225`, `Community 81`, `Community 13`, `Community 140`, `Community 3`, `Community 94`, `Community 12`, `Community 9`, `Community 32`, `Community 14`, `Community 41`, `Community 169`, `Community 24`, `Community 36`, `Community 51`, `Community 40`, `Community 251`, `Community 252`, `Community 253`, `Community 246`, `Community 257`, `Community 254`, `Community 256`, `Community 132`, `Community 250`, `Community 249`, `Community 248`, `Community 48`, `Community 73`, `Community 258`, `Community 247`, `Community 255`, `Community 21`, `Community 29`?**
  _High betweenness centrality (0.154) - this node is a cross-community bridge._
- **Why does `Strategy` connect `Community 26` to `Community 33`, `Community 11`, `Community 189`, `Community 47`, `Community 190`, `Community 50`, `Community 241`, `Community 240`, `Community 225`, `Community 81`, `Community 4`, `Community 1`, `Community 54`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Why does `LineRoot` connect `Community 8` to `Community 12`, `Community 6`, `Community 93`, `Community 15`, `Community 1`, `Community 141`, `Community 191`, `Community 28`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 243 inferred relationships involving `MetaParams` (e.g. with `BrokerBase` and `MetaBroker`) actually correct?**
  _`MetaParams` has 243 INFERRED edges - model-reasoned connections that need verification._
- **Are the 60 inferred relationships involving `LineRoot` (e.g. with `LineActions` and `LineBuffer`) actually correct?**
  _`LineRoot` has 60 INFERRED edges - model-reasoned connections that need verification._
- **Are the 50 inferred relationships involving `Strategy` (e.g. with `Cerebro` and `OptReturn`) actually correct?**
  _`Strategy` has 50 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Intercept the strategy parameter`, `Analyzer base class. All analyzers are subclass of this one      An Analyzer ins`, `Support for invoking ``len`` on analyzers by actually returning the         curr` to the rest of the system?**
  _282 weakly-connected nodes found - possible documentation gaps or missing edges._