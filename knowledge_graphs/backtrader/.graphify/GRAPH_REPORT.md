# Graph Report - backtrader  (2026-08-06)

## Corpus Check
- 171 files · ~132,440 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2680 nodes · 4964 edges · 206 communities detected
- Non-singleton communities: 194
- Extraction: EXTRACTED: 69.2% · INFERRED: 30.8%
- Edge kinds: calls: 577 · contains: 454 · imports: 1 · imports_from: 97 · inherits: 276 · method: 1409 · rationale_for: 619 · uses: 1531

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 171 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `b853d7c`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `MetaParams` (260)
- `LineRoot` (119)
- `Strategy` (111)
- `LineSingle` (111)
- `PandasMarketCalendar` (79)
- `DataBase` (72)
- `CommInfoBase` (71)
- `LineIterator` (71)
- `LineMultiple` (70)
- `IBStore` (67)

## Surprising Connections (you probably didn't know these)
- `Returns the actual margin/guarantees needed for a single item of the         ass` --uses--> `MetaParams`  [INFERRED]
  comminfo.py → metabase.py
- `Returns the needed size to meet a cash operation at a given price` --uses--> `MetaParams`  [INFERRED]
  comminfo.py → metabase.py
- `Returns the needed amount of cash an operation would cost` --uses--> `MetaParams`  [INFERRED]
  comminfo.py → metabase.py
- `Returns the value of size for given a price. For future-like         objects it` --uses--> `MetaParams`  [INFERRED]
  comminfo.py → metabase.py
- `Returns the value of a position given a price. For future-like         objects i` --uses--> `MetaParams`  [INFERRED]
  comminfo.py → metabase.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.04
Nodes (29): LineBuffer, Resets the internal buffer structure and the indices, The linebuffer must guarantee the minimum requested size to be         available, Returns a slice of the array relative to *ago*          Keyword Args:, Returns a single value of the array relative to the real zero         of the buf, Returns a slice of the array relative to the real zero of the buffer          Ke, Sets a value at position "ago" and executes any associated bindings          Key, Sets a value at position "ago" and executes any associated bindings          Key (+21 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (18): LineRoot, Receive notification of how large the buffer must at least be, Direct minperiod manipulation. It could be used for example         by a strateg, Update the minperiod if needed. The minperiod will have been         calculated, Add a minperiod to own ... to be defined by subclasses, Increment the minperiod with no considerations, It will be called during the "minperiod" phase of an iteration., It will be called when the minperiod phase is over for the 1st         post-minp (+10 more)

### Community 2 - "Community 2"
Cohesion: 0.07
Nodes (5): BackBroker, Returns the actual fundmode (True or False), Returns the current cash (alias: ``getcash``), Sets the cash parameter (alias: ``setcash``), Add/Remove cash to the system (use a negative value to remove)

### Community 3 - "Community 3"
Cohesion: 0.09
Nodes (25): LineActions, LinesOperation, Base class derived from LineBuffer intented to defined the     minimum interface, Holds an operation that operates on a two operands. Example: mul      It will "n, This method will be called before the minimum period of all         datas/indica, This method will be called once, exactly when the minimum period for         all, This method will be called for all remaining data points when the         minimu, LineSingle (+17 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (11): API, OandaNetworkError, OandaRequestError, OandaStore, OandaStreamError, OandaTimeFrameError, Singleton class wrapping to control the connections to Oanda.      Params:, Returns ``DataCls`` with args, kwargs (+3 more)

### Community 5 - "Community 5"
Cohesion: 0.04
Nodes (23): DoubleExponentialMovingAverage, DEMA was first time introduced in 1994, in the article "Smoothing Data with, TEMA was first time introduced in 1994, in the article "Smoothing Data with, TripleExponentialMovingAverage, DicksonMovingAverage, By Nathan Dickson      The *Dickson Moving Average* combines the ``ZeroLagIndica, ExponentialMovingAverage, A Moving Average that smoothes data exponentially over time.      It is a subcla (+15 more)

### Community 6 - "Community 6"
Cohesion: 0.11
Nodes (29): Set the actual fundmode (True or False)          If the argument fundstartval is, Set the starting value of the fund-like performance tracker, Configure assignment of interest to profit and loss, Configure the Cheat-On-Close method to buy the close on order bar, Configure the Cheat-On-Open method to buy the close on order bar, Configure the shortcash parameters, Configure slippage to be percentage based, Configure slippage to be fixed points based (+21 more)

### Community 7 - "Community 7"
Cohesion: 0.06
Nodes (27): CommissionInfo, Returns the level of leverage allowed for this comission scheme, Calculates the commission of an operation at a given price          pseudoexec:, Calculates the commission of an operation at a given price, Return actual profit and loss a position has, Calculates cash adjustment for a given price difference, Calculates the credit due for short selling or product specific, This method returns  the cost in terms of credit interest charged by         the (+19 more)

### Community 8 - "Community 8"
Cohesion: 0.05
Nodes (23): Observer, Broker, Cash, FundShares, FundValue, This observer keeps track of the current fund-like value      Params: None, This observer keeps track of the current fund-like shares      Params: None, This observer keeps track of the current amount of cash in the broker      Param (+15 more)

### Community 9 - "Community 9"
Cohesion: 0.06
Nodes (15): AutoOrderedDict, _Bar, DataSeries, OHLC, OHLCDateTime, This class is a placeholder for the values of the standard lines of a     DataBa, Initializes a bar to the default not-updated vaues, Returns if a bar has already been updated          Uses the fact that NaN is the (+7 more)

### Community 10 - "Community 10"
Cohesion: 0.13
Nodes (37): Wrapper for filters added via .addfilter to turn them     into processors., SimpleFilterWrapper, TimeFrame, MetaCSVDataBase, # FIXME: These two are never used and could be removed, Returns the next eos using a trading calendar if available, Can be overriden by classes to return a timezone for input, To be overriden by subclasses which may auto-calculate the         timezone (+29 more)

### Community 11 - "Community 11"
Cohesion: 0.06
Nodes (19): All, And, Any, Cmp, CmpEx, DivByZero, DivZeroByZero, If (+11 more)

### Community 12 - "Community 12"
Cohesion: 0.09
Nodes (17): Cerebro, Used during optimization to pass the cerebro over the multiprocesing         mod, The core method to perform backtesting. Any ``kwargs`` passed to it         will, Internal method invoked by ``run``` to run a set of strategies, Internal method which kicks the broker and delivers any broker         notificat, Actual implementation of run in full next mode. All objects have its         ``n, Actual implementation of run in vector mode.         Strategies are still invoke, API for lineiterators to disable runonce (see HeikinAshi) (+9 more)

### Community 13 - "Community 13"
Cohesion: 0.07
Nodes (17): StrategyBase, ItemCollection, Holds a collection of items that can be reached by        - Index       - Name (, Observer, Enable the memory saving schemes. Possible values for ``savemem``:            0:, Returns the current by name positions directly from the broker          If the g, Replace the default (fixed stake) sizer, This subclass of ``Strategy`` is meant to to auto-operate using     **signals**. (+9 more)

### Community 14 - "Community 14"
Cohesion: 0.08
Nodes (1): AbstractDataBase

### Community 15 - "Community 15"
Cohesion: 0.10
Nodes (13): findbases(), ParamsBase, DataTrades, MetaDataTrades, items(), iteritems(), iterkeys(), itervalues() (+5 more)

### Community 16 - "Community 16"
Cohesion: 0.13
Nodes (6): _BaseResampler, DTFaker, Returns the point of time intraday for a given time according to the         tim, Called to check if the current stored bar has to be delivered in         spite o, Adjusts the time of calculated bar (from underlying data source) by         usin, Called for each set of values produced by the data source

### Community 17 - "Community 17"
Cohesion: 0.07
Nodes (7): dict, OrderedDict, AutoDict, AutoDictList, AutoOrderedDict, DotDict, OrderedDefaultdict

### Community 18 - "Community 18"
Cohesion: 0.07
Nodes (12): MetaVCData, Returns the calculated time offset local equipment -> data server, Returns the timezone to consider for the input data, Returns the default output timezone for the data          This defaults to be th, Returns ``True`` to notify ``Cerebro`` that preloading and runonce         shoul, Receives an environment (cerebro) and passes it over to the store it         bel, Starts the VC connecction and gets the real contract and         contractdetails, Stops and tells the store to stop (+4 more)

### Community 19 - "Community 19"
Cohesion: 0.08
Nodes (6): LinePlotterIndicator, MetaIndicator, MtLinePlotterIndicator, Class has already been created ... register subclasses, IndicatorBase, Lines

### Community 20 - "Community 20"
Cohesion: 0.08
Nodes (19): Description:     The Relative Momentum Index was developed by Roger Altman and w, RelativeMomentumIndex, DownDay, DownDayBool, Defined by J. Welles Wilder, Jr. in 1978 in his book *"New Concepts in     Techn, Subclass of RSI which changes parameers ``safediv`` to ``True`` as the     defau, Uses a SimpleMovingAverage as described in Wikipedia and other soures      See:, Uses an ExponentialMovingAverage as described in Wikipedia      See:       - htt (+11 more)

### Community 21 - "Community 21"
Cohesion: 0.11
Nodes (13): MetaSigStrategy, Create a bracket order group (low side - buy order - high side). The         def, Create a bracket order group (low side - buy order - high side). The         def, Place an order to rebalance a position to have final size of ``target``, Place an order to rebalance a position to have final value of         ``target``, Place an order to rebalance a position to have final value of         ``target``, Returns the current position for a given data in a given broker.          If bot, Returns the current position for a given name in a given broker.          If bot (+5 more)

### Community 22 - "Community 22"
Cohesion: 0.08
Nodes (13): Total, Average, Compound and Annualized Returns calculated using a     logarithm, Returns, This analyzer calculates the Returns by looking at the beginning     and end of, TimeReturn, Variability-Weighted Return: Better SharpeRatio with Log Returns      Alias:, VWR, average(), Args:       x: iterable with len        oneless: (default ``False``) reduces the (+5 more)

### Community 23 - "Community 23"
Cohesion: 0.07
Nodes (9): BrokerBase, Adds a ``CommissionInfo`` object that will be the default for all assets if, Returns the current number of shares in the fund-like mode, Set the actual fundmode (True or False)          If the argument fundstartval is, Returns the actual fundmode (True or False), Add order history. See cerebro for details, Add fund history. See cerebro for details, Retrieves the ``CommissionInfo`` scheme associated with the given         ``data (+1 more)

### Community 24 - "Community 24"
Cohesion: 0.10
Nodes (20): IBCommInfo, Commissions are calculated by ib, but the trades calculations in the     ```Stra, Returns the needed amount of cash an operation would cost, MetaOandaBroker, OandaCommInfo, Returns the needed amount of cash an operation would cost, Class has already been created ... register, MetaVCBroker (+12 more)

### Community 25 - "Community 25"
Cohesion: 0.10
Nodes (1): VCBroker

### Community 26 - "Community 26"
Cohesion: 0.09
Nodes (11): IBData, MetaIBData, Returns ``True`` to notify ``Cerebro`` that preloading and runonce         shoul, Receives an environment (cerebro) and passes it over to the store it         bel, Parses dataname generates a default contract, Starts the IB connecction and gets the real contract and         contractdetails, Class has already been created ... register, Stops and tells the store to stop (+3 more)

### Community 27 - "Community 27"
Cohesion: 0.10
Nodes (19): AverageDirectionalMovementIndex, AverageDirectionalMovementIndexRating, _DirectionalIndicator, DirectionalMovement, DirectionalMovementIndex, DownMove, MinusDirectionalIndicator, PlusDirectionalIndicator (+11 more)

### Community 28 - "Community 28"
Cohesion: 0.09
Nodes (15): HurstExponent, References:        - https://www.quantopian.com/posts/hurst-exponent       - htt, LaguerreFilter, LaguerreRSI, Defined by John F. Ehlers in `Cybernetic Analysis for Stock and Futures`,     20, Defined by John F. Ehlers in `Cybernetic Analysis for Stock and Futures`,     20, CointN, OLS_BetaN (+7 more)

### Community 29 - "Community 29"
Cohesion: 0.09
Nodes (5): IBStore, Singleton class wrapping an ibpy ibConnection instance.      The parameters can, Calculate a duration in between 2 datetimes, Calculate a duration in between 2 datetimes. Returns single size, Receive the event commissionReport

### Community 30 - "Community 30"
Cohesion: 0.08
Nodes (13): Indicator, DetrendedPriceOscillator, Defined by Joe DiNapoli in his book *"Trading with DiNapoli levels"*      It mea, DV2, RSI(2) alternative     Developed by David Varadi of http://cssanalytics.wordpres, PercentChange, Measures the perccentage change of the current value with respect to that, PrettyGoodOscillator (+5 more)

### Community 31 - "Community 31"
Cohesion: 0.10
Nodes (13): ADFormatter, ADLocator, AutoDateFormatter, AutoDateLocator, _idx2dt(), Convert axis data interval to datetime objects., Converts the view interval to datetime objects., Pick the best locator based on a distance. (+5 more)

### Community 32 - "Community 32"
Cohesion: 0.10
Nodes (9): MultiCursor, MultiCursor2, Provide a vertical (default) and/or horizontal line cursor shared between     mu, Abstract base class for GUI neutral widgets, Set whether the widget is active., Get whether the widget is active., Return True if event should be ignored.         This method (or a version of it), Provide a vertical (default) and/or horizontal line cursor shared between     mu (+1 more)

### Community 33 - "Community 33"
Cohesion: 0.13
Nodes (2): Adds an ``Indicator`` class to the mix. Instantiation will be done at         ``, Strategy

### Community 34 - "Community 34"
Cohesion: 0.13
Nodes (1): IBBroker

### Community 35 - "Community 35"
Cohesion: 0.15
Nodes (1): OandaBroker

### Community 36 - "Community 36"
Cohesion: 0.09
Nodes (12): Analyzer, Support for invoking ``len`` on analyzers by actually returning the         curr, Receives the cash/value notification before each next cycle, Receives the current cash, value, fundvalue and fund shares, Receives order notifications before each next cycle, Receives trade notifications before each next cycle, Invoked for each next invocation of the strategy, once the minum         preiod, Invoked for each prenext invocation of the strategy, until the minimum         p (+4 more)

### Community 37 - "Community 37"
Cohesion: 0.13
Nodes (2): PumpEvents(), VCStore

### Community 38 - "Community 38"
Cohesion: 0.09
Nodes (11): Base class to be subclassed for user defined strategies., Returns the current by data positions directly from the broker          If the g, Returns the sizer which is in used if automatic statke calculation is         us, Called right before the backtesting is about to be stopped, Receives a notification from a store provider, Absolute size of the trade, Shortcut to retrieve the name of the data this trade references, Returns a datetime.datetime object with the datetime in which         the trade (+3 more)

### Community 39 - "Community 39"
Cohesion: 0.12
Nodes (12): date2num(), Localizer(), _LocalTimezone, num2date(), num2dt(), num2time(), *x* is a float value which gives the number of days     (fraction part represent, Convert :mod:`datetime` to the Gregorian date as UTC float days,     preserving (+4 more)

### Community 40 - "Community 40"
Cohesion: 0.11
Nodes (8): MetaOandaData, OandaData, Returns ``True`` to notify ``Cerebro`` that preloading and runonce         shoul, Receives an environment (cerebro) and passes it over to the store it         bel, Starts the Oanda connecction and gets the real contract and         contractdeta, Stops and tells the store to stop, Class has already been created ... register, Oanda Data Feed.      Params:        - ``qcheck`` (default: ``0.5``)          Ti

### Community 41 - "Community 41"
Cohesion: 0.13
Nodes (1): LineIterator

### Community 42 - "Community 42"
Cohesion: 0.11
Nodes (8): CandlestickPlotHandler, LineOnClosePlotHandler, OHLCPlotHandler, plot_candlestick(), plot_lineonclose(), plot_ohlc(), plot_volume(), VolumePlotHandler

### Community 43 - "Community 43"
Cohesion: 0.14
Nodes (12): _AroonBase, AroonDown, AroonOscillator, AroonUp, AroonUpDown, AroonUpDownOscillator, This is the AroonDown from the indicator AroonUpDown developed by Tushar     Cha, Developed by Tushar Chande in 1995.      It tries to determine if a trend exists (+4 more)

### Community 44 - "Community 44"
Cohesion: 0.11
Nodes (10): MetaBroker, Class has already been created ... fill missing methods if needed be, MetaFilter, MetaParams, MetaSingleton, Metaclass to make a metaclassed class a singleton, MetaSingleton, Metaclass to make a metaclassed class a singleton (+2 more)

### Community 45 - "Community 45"
Cohesion: 0.11
Nodes (10): OptReturn, Adds a ``Sizer`` class (and args) which is the default sizer for any         str, Adds a callback to get messages which would be handled by the         notify_sto, Plots the strategies inside cerebro          If ``plotter`` is None a default ``, Returns a tuple with the opening and closing times (``datetime.time``)         f, Returns the iso week number of the next trading day, given a ``day``         (da, Returns ``True`` if the given ``day`` (datetime/date) instance is the         la, Returns ``True`` if the given ``day`` (datetime/date) instance is the         la (+2 more)

### Community 46 - "Community 46"
Cohesion: 0.12
Nodes (10): Fills one by one bars as needed from time_start to time_end          Invalidates, This class can be applied to a data source as a filter and will filter out     i, Return Values:            - False: nothing to filter           - True: filter cu, This class can be applied to a data source as a filter and will filter out     i, Return Values:            - False: data stream was not touched           - True:, Bar Filler for a Data Source inside the declared session start/end times.      T, Params:           - data: the data source to filter/process          Returns:, SessionFiller (+2 more)

### Community 47 - "Community 47"
Cohesion: 0.16
Nodes (4): Adds a signal to the system which will be later added to a         ``SignalStrat, Adds an ``Observer`` class to the mix. Instantiation will be done at         ``r, The system wide writer class.      It can be parametrized with:        - ``out``, WriterFile

### Community 48 - "Community 48"
Cohesion: 0.11
Nodes (9): If invoked from inside a strategy or anywhere else, including other         thre, This can also be done with the parameter ``tz``          Adds a global timezone, Adds a global trading calendar to the system. Individual data feeds         may, Adds an ``Observer`` class to the mix. Instantiation will be done at         ``r, Returns the broker instance.          This is also available as a ``property`` b, Wrapper of ``pandas_market_calendars`` for a trading calendar. The package     `, Returns the next trading day (datetime/date instance) after ``day``         (dat, Returns the opening and closing times for the given ``day``. If the         meth (+1 more)

### Community 49 - "Community 49"
Cohesion: 0.12
Nodes (7): MetaRollOver, Returns ``True`` to notify ``Cerebro`` that preloading and runonce         shoul, To be overriden by subclasses which may auto-calculate the         timezone, Class has already been created ... register, Intercept const. to copy timeframe/compression from 1st data, Class that rolls over to the next future when a condition is met      Params:, RollOver

### Community 50 - "Community 50"
Cohesion: 0.13
Nodes (7): LineDelay(), _LineForward, LineNum(), PseudoArray, Returns either a delayed verison of itself in the form of a         LineDelay ob, Takes a LineBuffer (or derived) object and stores the value from     "ago" perio, Takes a LineBuffer (or derived) object and stores the value from     "ago" perio

### Community 51 - "Community 51"
Cohesion: 0.11
Nodes (5): LineSeriesMaker(), LineSeriesStub, Like _addanalyzer but meant for observers (or other entities) which         rely, Receives a timer notification where ``timer`` is the timer which was         ret, Returns a list of the existing data names

### Community 52 - "Community 52"
Cohesion: 0.11
Nodes (4): OrderBase, Stores a CommInfo scheme associated with the asset, Marks an order as submitted and stores the broker to which it was         submit, Marks an order as accepted

### Community 53 - "Community 53"
Cohesion: 0.18
Nodes (6): Adds a ``Data Feed`` instance to the mix.          If ``name`` is not None it wi, Chains several data feeds into one          If ``name`` is passed as named argum, Chains several data feeds into one          If ``name`` is passed as named argum, Adds a ``Data Feed`` to be replayed by the system          If ``name`` is not No, Adds a ``Data Feed`` to be resample by the system          If ``name`` is not No, Timer

### Community 54 - "Community 54"
Cohesion: 0.13
Nodes (4): CSVDataBase, CSVFeedBase, FeedBase, MetaAbstractDataBase

### Community 55 - "Community 55"
Cohesion: 0.12
Nodes (7): Chainer, MetaChainer, Class has already been created ... register, Intercept const. to copy timeframe/compression from 1st data, Class that chains datas, Returns ``True`` to notify ``Cerebro`` that preloading and runonce         shoul, To be overriden by subclasses which may auto-calculate the         timezone

### Community 56 - "Community 56"
Cohesion: 0.13
Nodes (6): Reuses queue for tickerId, returning the new tickerId and q, Creates ticker/Queue for data delivery to a data feed, Extension of the raw reqHistoricalData proxy, which takes two dates         rath, Proxy to reqHistorical Data, Creates a request for (5 seconds) Real Time Bars          Params:           - co, Creates a MarketData subscription          Params:           - contract: a ib.ex

### Community 57 - "Community 57"
Cohesion: 0.13
Nodes (9): Internal method to really create the timer (not started yet) which         can b, Schedules a timer to invoke ``notify_timer``          Arguments:            - ``, Adds a SignalStrategy subclass which can accept signals, Adds an ``Store`` instance to the if not already present, Adds a *callback* to the list of callbacks that will be called with the, PandasMarketCalendar, Wrapper of ``pandas_market_calendars`` for a trading calendar. The package     `, Returns the next trading day (datetime/date instance) after ``day``         (dat (+1 more)

### Community 58 - "Community 58"
Cohesion: 0.13
Nodes (7): Used during optimization to prevent optimization result `runstrats`         from, If signals are added to the system and the ``concurrent`` value is         set t, Adds an ``Writer`` class to the mix. Instantiation will be done at         ``run, Adds a ``Sizer`` class by idx. This idx is a reference compatible to         the, Adds an ``Analyzer`` class to the mix. Instantiation will be done at         ``r, Adds a callback to get messages which would be handled by the         notify_dat, SignalStrategy

### Community 59 - "Community 59"
Cohesion: 0.17
Nodes (9): _CrossBase, CrossDown, CrossOver, CrossUp, NonZeroDifference, This indicator gives a signal if the provided datas (2) cross up or down., Keeps track of the difference between two data inputs skipping, memorizing     t, This indicator gives a signal if the 1st provided data crosses over the 2nd (+1 more)

### Community 60 - "Community 60"
Cohesion: 0.15
Nodes (7): This version displays the 3 possible lines:        - percK       - percD       -, By Dr. George Lane in the 50s. It compares a closing price to the price     rang, The regular (or slow version) adds an additional moving average layer and     th, Stochastic, _StochasticBase, StochasticFast, StochasticFull

### Community 61 - "Community 61"
Cohesion: 0.24
Nodes (1): Plot_OldSync

### Community 62 - "Community 62"
Cohesion: 0.13
Nodes (7): MetaSingleton, Metaclass to make a metaclassed class a singleton, Base class for all Stores, Returns ``DataCls`` with args, kwargs, Returns broker with *args, **kwargs from registered ``BrokerCls``, Return the pending "store" notifications, Store

### Community 63 - "Community 63"
Cohesion: 0.18
Nodes (12): AllN, AnyN, Highest, Lowest, OperationN, Calculates the highest value for the data in a given period      Uses the built-, Calculates the lowest value for the data in a given period      Uses the built-i, Calculates the Sum of the data values over a given period      Uses ``math.fsum` (+4 more)

### Community 64 - "Community 64"
Cohesion: 0.13
Nodes (8): Momentum, MomentumOscillator, RateOfChange, RateOfChange100, Measures the ratio of change in prices over a period with base 100      This is, Measures the change in price by calculating the difference between the     curre, Measures the ratio of change in prices over a period      Formula:       - mosc, Measures the ratio of change in prices over a period      Formula:       - roc =

### Community 65 - "Community 65"
Cohesion: 0.16
Nodes (3): OrderData, Receives data execution input and stores it, Holds actual order data for Creation and Execution.      In the case of Creation

### Community 66 - "Community 66"
Cohesion: 0.16
Nodes (8): AverageTrueRange, Defined by J. Welles Wilder, Jr. in 1978 in his book *"New Concepts in     Techn, Defined by J. Welles Wilder, Jr. in 1978 in his book *"New Concepts in     Techn, Defined by J. Welles Wilder, Jr. in 1978 in his book New Concepts in     Technic, Defined by J. Welles Wilder, Jr. in 1978 in his book *"New Concepts in     Techn, TrueHigh, TrueLow, TrueRange

### Community 67 - "Community 67"
Cohesion: 0.15
Nodes (4): object, _SymInfo, flushfile, StdOutDevNull

### Community 68 - "Community 68"
Cohesion: 0.15
Nodes (4): DrawDown, This analyzer calculates trading system drawdowns on the chosen     timeframe wh, This analyzer calculates trading system drawdowns stats such as drawdown     val, TimeDrawDown

### Community 69 - "Community 69"
Cohesion: 0.15
Nodes (7): IBOrder, IBOrderState, MetaIBBroker, Class has already been created ... register, Subclasses the IBPy order to provide the minimum extra functionality     needed, Get the printout from the base class and add some ib.Order specific         fiel, OrderBase

### Community 70 - "Community 70"
Cohesion: 0.19
Nodes (8): This is intended to load files which were downloaded before Yahoo     discontinu, Executes a direct download of data from Yahoo servers for the given time     ran, Parses pre-downloaded Yahoo CSV Data Feeds (or locally generated if they     com, YahooFinance, YahooFinanceCSV, YahooFinanceCSVData, YahooFinanceData, YahooLegacyCSV

### Community 71 - "Community 71"
Cohesion: 0.15
Nodes (6): DemarkPivotPoint, FibonacciPivotPoint, PivotPoint, Defines a level of significance by taking into account the average of price, Defines a level of significance by taking into account the average of price, Defines a level of significance by taking into account the average of price

### Community 72 - "Community 72"
Cohesion: 0.33
Nodes (11): btrun(), getdatas(), getfunctions(), getmodclasses(), getmodfunctions(), getobjects(), loadmodule(), loadmodule2() (+3 more)

### Community 73 - "Community 73"
Cohesion: 0.21
Nodes (9): BacktraderError, FromModuleImportError, ModuleImportError, Base exception for all other exceptions, Requests the platform to skip this strategy for backtesting. To be     raised du, Raised if a class requests a module to be present to work and it cannot     be i, Raised if a class requests a module to be present to work and it cannot     be i, StrategySkipError (+1 more)

### Community 74 - "Community 74"
Cohesion: 0.17
Nodes (4): ExponentialSmoothing, ExponentialSmoothingDynamic, Averages a given data over a period using exponential smoothing      A regular A, Averages a given data over a period using exponential smoothing      A regular A

### Community 75 - "Community 75"
Cohesion: 0.20
Nodes (7): getlocator(), MyDateFormatter, MyVolFormatter, patch_formatter(), patch_locator(), Return the label for time x at position pos, Return the label for time x at position pos

### Community 76 - "Community 76"
Cohesion: 0.17
Nodes (6): FixedReverser, FixedSize, FixedSizeTarget, This sizer simply returns a fixed size for any operation.     Size can be contro, This sizer returns the needes fixed size to reverse an open position or     the, This sizer simply returns a fixed target size, useful when coupled     with Targ

### Community 77 - "Community 77"
Cohesion: 0.17
Nodes (6): Cancels a Queue for data delivery, Signal end of contractdetails, Cancels an existing HistoricalData request          Params:           - q: the Q, Cancels an existing MarketData subscription          Params:           - q: the, Cancels an existing MarketData subscription          Params:           - q: the, Receives the events of a historical data request

### Community 78 - "Community 78"
Cohesion: 0.24
Nodes (8): AllInSizer, AllInSizerInt, PercentSizer, PercentSizerInt, This sizer return percents of available cash      Params:       - ``percents`` (, This sizer return all available cash of broker       Params:        - ``percents, This sizer return percents of available cash in form of size truncated     to an, This sizer return all available cash of broker with the     size truncated to an

### Community 79 - "Community 79"
Cohesion: 0.20
Nodes (6): Updates the current trade. The logic does not check if the         trade is reve, Represents the status and update event for each update a Trade has      This obj, Initializes the object to the current status of the Trade, Used to fill the ``update`` part of the history entry, Returns a datetime for the time the update event happened, TradeHistory

### Community 80 - "Community 80"
Cohesion: 0.20
Nodes (5): Returns the actual margin/guarantees needed for a single item of the         ass, Returns the needed size to meet a cash operation at a given price, Returns the needed amount of cash an operation would cost, Returns the value of size for given a price. For future-like         objects it, Returns the value of a position given a price. For future-like         objects i

### Community 81 - "Community 81"
Cohesion: 0.20
Nodes (4): PandasData, PandasDirectData, Uses a Pandas DataFrame as the feed source, using indices into column     names, Uses a Pandas DataFrame as the feed source, iterating directly over the     tupl

### Community 82 - "Community 82"
Cohesion: 0.20
Nodes (5): MetaVChartFile, Class has already been created ... register, Support for `Visual Chart <www.visualchart.com>`_ binary on-disk files for     b, # FIXME: find reference to tick counter for format, VChartFile

### Community 83 - "Community 83"
Cohesion: 0.27
Nodes (7): PercentagePriceOscillator, PercentagePriceOscillatorShort, _PriceOscBase, PriceOscillator, Shows the difference between a short and long exponential moving     averages ex, Shows the difference between a short and long exponential moving     averages ex, Shows the difference between a short and long exponential moving     averages ex

### Community 84 - "Community 84"
Cohesion: 0.22
Nodes (4): Real data that can be currently held in the internal buffer          The interna, Rewinds the logical index to the beginning          The underlying buffer remain, Moves the logical index foward and enlarges the buffer as much as needed, Executes the bindings when running in "once" mode

### Community 85 - "Community 85"
Cohesion: 0.22
Nodes (4): LogReturns, LogReturns2, This observer stores the *log returns* of the strategy or a      Params:, Extends the observer LogReturns to show two instruments

### Community 86 - "Community 86"
Cohesion: 0.33
Nodes (3): AbstractDataBase, DataFiller, This class will fill gaps in the source data using the following     information

### Community 87 - "Community 87"
Cohesion: 0.47
Nodes (1): TimeFrameAnalyzerBase

### Community 88 - "Community 88"
Cohesion: 0.22
Nodes (3): Benchmark, This observer stores the *returns* of the strategy and the *return* of a     ref, TimeReturn

### Community 89 - "Community 89"
Cohesion: 0.22
Nodes (4): MeanDeviation, Calculates the standard deviation of the passed data for a given period      Not, MeanDeviation (alias MeanDev)      Calculates the Mean Deviation of the passed d, StandardDeviation

### Community 90 - "Community 90"
Cohesion: 0.22
Nodes (4): Oscillator, OscillatorMixIn, MixIn class to create a subclass with another indicator. The main line of     th, Oscillation of a given data around another data      Datas:       This indicator

### Community 91 - "Community 91"
Cohesion: 0.33
Nodes (2): MetaBase, type

### Community 92 - "Community 92"
Cohesion: 0.22
Nodes (4): Returns the name for a given status or the one of the order, Returns the name for a given exectype or the one of the order, Returns the name for a given ordtype or the one of the order, Returns True if the order is in a status in which it can still be         execut

### Community 93 - "Community 93"
Cohesion: 0.22
Nodes (2): PInfo, PlotScheme

### Community 94 - "Community 94"
Cohesion: 0.22
Nodes (3): Parses a tickString tickType 48 (RTVolume) event from the IB API into its     co, Cash Markets have no notion of "last_price"/"last_size" and the         tracking, RTVolume

### Community 95 - "Community 95"
Cohesion: 0.25
Nodes (4): Analyzer, MetaTimeFrameAnalyzerBase, AnnualReturn, This analyzer calculates the AnnualReturns by looking at the beginning     and e

### Community 96 - "Community 96"
Cohesion: 0.25
Nodes (3): SQN or SystemQualityNumber. Defined by Van K. Tharp to categorize trading     sy, Replace default implementation to instantiate an AutoOrdereDict         rather t, SQN

### Community 97 - "Community 97"
Cohesion: 0.39
Nodes (7): CommInfo, CommInfo_Futures, CommInfo_Futures_Fixed, CommInfo_Futures_Perc, CommInfo_Stocks, CommInfo_Stocks_Fixed, CommInfo_Stocks_Perc

### Community 98 - "Community 98"
Cohesion: 0.25
Nodes (1): DataClone

### Community 99 - "Community 99"
Cohesion: 0.29
Nodes (4): Quandl, QuandlCSV, Executes a direct download of data from Quandl servers for the given time     ra, Parses pre-downloaded Quandl CSV Data Feeds (or locally generated if they     co

### Community 100 - "Community 100"
Cohesion: 0.25
Nodes (3): Support for `Visual Chart <www.visualchart.com>`_ binary on-disk files for     b, VChartData, VChartFeed

### Community 101 - "Community 101"
Cohesion: 0.29
Nodes (4): CalendarDays, Bar Filler to add missing calendar days to trading days      Params:        - fi, If the data has a gap larger than 1 day amongst bars, the missing bars         a, Fills one by one bars as needed from time_start to time_end          Invalidates

### Community 102 - "Community 102"
Cohesion: 0.29
Nodes (4): BollingerBands, BollingerBandsPct, Defined by John Bollinger in the 80s. It measures volatility by defining     upp, Extends the Bollinger Bands with a Percentage line

### Community 103 - "Community 103"
Cohesion: 0.32
Nodes (5): Envelope, _EnvelopeBase, EnvelopeMixIn, MixIn class to create a subclass with another indicator. The main line of     th, It creates envelopes bands separated from the source data by a given     percent

### Community 104 - "Community 104"
Cohesion: 0.32
Nodes (5): MetaMovAvBase, MovAv, MovingAverage, MovingAverageBase, MovingAverage (alias MovAv)      A placeholder to gather all Moving Average Type

### Community 105 - "Community 105"
Cohesion: 0.29
Nodes (4): MACD, MACDHisto, Moving Average Convergence Divergence. Defined by Gerald Appel in the 70s., Subclass of MACD which adds a "histogram" of the difference between the     macd

### Community 106 - "Community 106"
Cohesion: 0.32
Nodes (3): ParabolicSAR, Defined by J. Welles Wilder, Jr. in 1978 in his book *"New Concepts in     Techn, _SarStatus

### Community 107 - "Community 107"
Cohesion: 0.29
Nodes (4): Defined by Jack Hutson in the 80s and shows the Rate of Change (%) or slope, Extension of Trix with a signal line (ala MACD)      Formula:       - trix = Tri, Trix, TrixSignal

### Community 108 - "Community 108"
Cohesion: 0.29
Nodes (1): RTEventSink

### Community 109 - "Community 109"
Cohesion: 0.29
Nodes (2): _MetaTALibIndicator, _TALibIndicator

### Community 110 - "Community 110"
Cohesion: 0.29
Nodes (3): MetaAnalyzer, Meant to be overriden by subclasses. Gives a chance to create the         struct, Intercept the strategy parameter

### Community 111 - "Community 111"
Cohesion: 0.33
Nodes (2): Calmar, This analyzer calculates the CalmarRatio     timeframe which can be different fr

### Community 112 - "Community 112"
Cohesion: 0.29
Nodes (2): LogReturnsRolling, This analyzer calculates rolling returns for a given timeframe and     compressi

### Community 113 - "Community 113"
Cohesion: 0.29
Nodes (3): PyFolio, Returns a tuple of 4 elements which can be used for further processing with, This analyzer uses 4 children analyzers to collect data and transforms it     in

### Community 114 - "Community 114"
Cohesion: 0.33
Nodes (4): Extension of the SharpeRatio which returns the Sharpe Ratio directly in     annu, This analyzer calculates the SharpeRatio of a strategy using a risk free     ass, SharpeRatio, SharpeRatio_A

### Community 115 - "Community 115"
Cohesion: 0.29
Nodes (5): MT4CSVData, Parses a `Metatrader4 <https://www.metaquotes.net/en/metatrader4>`_ History, Parses a `SierraChart <http://www.sierrachart.com>`_ CSV exported file.      Spe, SierraChartCSVData, GenericCSVData

### Community 116 - "Community 116"
Cohesion: 0.29
Nodes (3): BarReplayer_Open, This filters splits a bar in two parts:        - ``Open``: the opening price of, Called when the data is no longer producing bars         Can be called multiple

### Community 117 - "Community 117"
Cohesion: 0.29
Nodes (4): Average, PeriodN, Base class for indicators which take a period (__init__ has to be called     eit, Averages a given data arithmetically over a period      Formula:       - av = da

### Community 118 - "Community 118"
Cohesion: 0.29
Nodes (6): FindFirstIndex, FindFirstIndexHighest, FindFirstIndexLowest, Returns the index of the last data that satisfies equality with the     conditio, Returns the index of the first data that is the highest in the period      Note:, Returns the index of the first data that is the lowest in the period      Note:

### Community 119 - "Community 119"
Cohesion: 0.29
Nodes (6): FindLastIndex, FindLastIndexHighest, FindLastIndexLowest, Returns the index of the last data that satisfies equality with the     conditio, Returns the index of the last data that is the highest in the period      Note:, Returns the index of the last data that is the lowest in the period      Note:

### Community 120 - "Community 120"
Cohesion: 0.29
Nodes (2): MetaLineActions, Metaclass for Lineactions      Scans the instance before init for LineBuffer (or

### Community 121 - "Community 121"
Cohesion: 0.29
Nodes (3): Returns all account value infos sent by TWS during regular updates         Waits, Returns the net liquidation value sent by TWS during regular updates         Wai, Returns the total cash value sent by TWS during regular updates         Waits fo

### Community 123 - "Community 123"
Cohesion: 0.29
Nodes (2): MetaStrategy, Class has already been created ... register subclasses

### Community 124 - "Community 124"
Cohesion: 0.33
Nodes (3): Returns a *dict-like* object with the results of the analysis          The keys, Prints the results returned by ``get_analysis`` via a standard         ``Writerf, Prints the results returned by ``get_analysis`` using the pretty         print P

### Community 125 - "Community 125"
Cohesion: 0.33
Nodes (2): GrossLeverage, This analyzer calculates the Gross Leverage of the current strategy     on a tim

### Community 126 - "Community 126"
Cohesion: 0.33
Nodes (2): Provides statistics on closed trades (keeps also the count of open ones), TradeAnalyzer

### Community 127 - "Community 127"
Cohesion: 0.33
Nodes (2): This analyzer reports the transactions occurred with each an every data in     t, Transactions

### Community 128 - "Community 128"
Cohesion: 0.33
Nodes (3): GenericCSV, GenericCSVData, Parses a CSV file according to the order and field presence defined by the     p

### Community 129 - "Community 129"
Cohesion: 0.33
Nodes (3): Filter, Modify the data stream to draw Renko bars (or bricks)      Params:        - ``hi, Renko

### Community 130 - "Community 130"
Cohesion: 0.40
Nodes (1): Filter

### Community 131 - "Community 131"
Cohesion: 0.33
Nodes (2): Accum, Cummulative sum of the data values      Formula:       - accum += data

### Community 132 - "Community 132"
Cohesion: 0.33
Nodes (2): CommodityChannelIndex, Introduced by Donald Lambert in 1980 to measure variations of the     "typical p

### Community 133 - "Community 133"
Cohesion: 0.33
Nodes (2): LineOwnOperation, Holds an operation that operates on a single operand. Example: abs      It will

### Community 134 - "Community 134"
Cohesion: 0.40
Nodes (2): Store provider for Visual Chart binary files      Params:        - ``path`` (def, VChartFile

### Community 135 - "Community 135"
Cohesion: 0.40
Nodes (2): PeriodStats, Calculates basic statistics for given timeframe      Params:        - ``timefram

### Community 136 - "Community 136"
Cohesion: 0.40
Nodes (2): PositionsValue, This analyzer reports the value of the positions of the current set of     datas

### Community 137 - "Community 137"
Cohesion: 0.40
Nodes (2): BlazeData, Support for `Blaze <blaze.pydata.org>`_ ``Data`` objects.      Only numeric indi

### Community 138 - "Community 138"
Cohesion: 0.40
Nodes (3): BacktraderCSV, BacktraderCSVData, Parses a self-defined CSV Data used for testing.      Specific parameters:

### Community 139 - "Community 139"
Cohesion: 0.40
Nodes (3): Parses a `VisualChart <http://www.visualchart.com>`_ CSV exported file.      Spe, VChartCSV, VChartCSVData

### Community 140 - "Community 140"
Cohesion: 0.40
Nodes (2): DaySplitter_Close, Splits a daily bar in two parts simulating 2 ticks which will be used to     rep

### Community 141 - "Community 141"
Cohesion: 0.40
Nodes (2): DataFilter, This class filters out bars from a given data source. In addition to the     sta

### Community 142 - "Community 142"
Cohesion: 0.40
Nodes (2): HeikinAshi, The filter remodels the open, high, low, close to make HeikinAshi     candlestic

### Community 143 - "Community 143"
Cohesion: 0.70
Nodes (1): Indicator

### Community 144 - "Community 144"
Cohesion: 0.40
Nodes (4): ApplyN, BaseApplyN, Base class for ApplyN and others which may take a ``func`` as a parameter     bu, Calculates ``func`` for a given period      Formula:       - line = func(data, p

### Community 145 - "Community 145"
Cohesion: 0.40
Nodes (2): Calculates the weighted average of the given data over a period      The default, WeightedAverage

### Community 146 - "Community 146"
Cohesion: 0.40
Nodes (2): HeikinAshi, Heikin Ashi candlesticks in the forms of lines      Formula:         ha_open = (

### Community 147 - "Community 147"
Cohesion: 0.40
Nodes (2): Formula:       # Buying Pressure = Close - TrueLow       BP = Close - Minimum(Lo, UltimateOscillator

### Community 148 - "Community 148"
Cohesion: 0.40
Nodes (3): LineActions, LinesCoupler(), SingleCoupler

### Community 149 - "Community 149"
Cohesion: 0.40
Nodes (4): Given the location and size of the box, return the path of     the box around it, Shade Color     This color utility function allows the user to easily darken or, shade_color(), tag_box_style()

### Community 150 - "Community 150"
Cohesion: 0.40
Nodes (2): MA_CrossOver, This is a long-only strategy which operates on a moving average cross      Note:

### Community 151 - "Community 151"
Cohesion: 0.50
Nodes (3): BaseApplyN, PercentRank, Measures the percent rank of the current value with respect to that of     perio

### Community 152 - "Community 152"
Cohesion: 0.50
Nodes (2): Handy function which turns things into things that can be iterated upon, Adds a ``Strategy`` class to the mix for optimization. Instantiation         wil

### Community 153 - "Community 153"
Cohesion: 0.50
Nodes (2): Fractal, References:         [Ref 1] http://www.investopedia.com/articles/trading/06/frac

### Community 154 - "Community 154"
Cohesion: 0.50
Nodes (2): See:       - http://www.vortexindicator.com/VFX_VORTEX.PDF, Vortex

### Community 155 - "Community 155"
Cohesion: 0.50
Nodes (1): InfluxDB

### Community 156 - "Community 156"
Cohesion: 0.50
Nodes (2): AccelerationDecelerationOscillator, Acceleration/Deceleration Technical Indicator (AC) measures acceleration     and

### Community 157 - "Community 157"
Cohesion: 0.50
Nodes (2): AwesomeOscillator, Awesome Oscillator (AO) is a momentum indicator reflecting the precise     chang

### Community 158 - "Community 158"
Cohesion: 0.50
Nodes (2): haDelta, Heikin Ashi Delta. Defined by Dan Valcu in his book "Heikin-Ashi: How to     Tra

### Community 159 - "Community 159"
Cohesion: 0.50
Nodes (2): Ichimoku, Developed and published in his book in 1969 by journalist Goichi Hosoda      For

### Community 160 - "Community 160"
Cohesion: 0.50
Nodes (2): KnowSureThing, It is a "summed" momentum indicator. Developed by Martin Pring and     published

### Community 161 - "Community 161"
Cohesion: 0.50
Nodes (2): The True Strength Indicators was first introduced in Stocks & Commodities     Ma, TrueStrengthIndicator

### Community 162 - "Community 162"
Cohesion: 0.50
Nodes (2): See:       - http://www.vortexindicator.com/VFX_VORTEX.PDF, Vortex

### Community 163 - "Community 163"
Cohesion: 0.50
Nodes (1): return numeric time part of datetimefloat

### Community 164 - "Community 164"
Cohesion: 0.50
Nodes (1): Returns True if the order is a Buy order

### Community 165 - "Community 165"
Cohesion: 0.50
Nodes (1): WriterStringIO

### Community 166 - "Community 166"
Cohesion: 0.67
Nodes (2): Calculates the Reduced value of the ``period`` data points applying     ``functi, ReduceN

### Community 167 - "Community 167"
Cohesion: 0.67
Nodes (2): MetaLineRoot, Once the object is created (effectively pre-init) the "owner" of this     class

### Community 168 - "Community 168"
Cohesion: 0.67
Nodes (1): Signal

### Community 169 - "Community 169"
Cohesion: 1.00
Nodes (1): Sets a specific ``broker`` instance for this strategy, replacing the         one

### Community 170 - "Community 170"
Cohesion: 1.00
Nodes (1): If signals are added to the system and the ``accumulate`` value is         set t

### Community 171 - "Community 171"
Cohesion: 1.00
Nodes (1): Add the keys, values of kwargs to the internal info dictionary to         hold c

### Community 172 - "Community 172"
Cohesion: 1.00
Nodes (1): Tries to retrieve the status from the broker in which the order is.          Def

### Community 173 - "Community 173"
Cohesion: 1.00
Nodes (1): Marks an order as cancelled

### Community 174 - "Community 174"
Cohesion: 1.00
Nodes (1): Marks an order as completely filled

### Community 175 - "Community 175"
Cohesion: 1.00
Nodes (1): Marks an order as expired. Returns True if it worked

### Community 176 - "Community 176"
Cohesion: 1.00
Nodes (1): Returns True if the order is a Sell order

### Community 177 - "Community 177"
Cohesion: 1.00
Nodes (1): Marks an order as having met a margin call

### Community 178 - "Community 178"
Cohesion: 1.00
Nodes (1): Marks an order as partially filled

### Community 179 - "Community 179"
Cohesion: 1.00
Nodes (1): Marks an order as rejected

### Community 180 - "Community 180"
Cohesion: 1.00
Nodes (1): Receives the current position for the asset and stotres it

### Community 181 - "Community 181"
Cohesion: 1.00
Nodes (1): Called when the data is no longer producing bars          Can be called multiple

### Community 182 - "Community 182"
Cohesion: 1.00
Nodes (1): Receive answer and pass it to the queue

### Community 183 - "Community 183"
Cohesion: 1.00
Nodes (1): Return the pending "store" notifications

### Community 184 - "Community 184"
Cohesion: 1.00
Nodes (1): Returns broker with *args, **kwargs from registered ``BrokerCls``

### Community 185 - "Community 185"
Cohesion: 1.00
Nodes (1): Returns ``DataCls`` with args, kwargs

### Community 186 - "Community 186"
Cohesion: 1.00
Nodes (1): returns a contract from the parameters without check

### Community 187 - "Community 187"
Cohesion: 1.00
Nodes (1): Receive the event ``openOrder`` events

### Community 188 - "Community 188"
Cohesion: 1.00
Nodes (1): Receive the event ``orderStatus``

### Community 189 - "Community 189"
Cohesion: 1.00
Nodes (1): Receive event positions

### Community 190 - "Community 190"
Cohesion: 1.00
Nodes (1): Receives x seconds Real Time Bars (at the time of writing only 5         seconds

### Community 191 - "Community 191"
Cohesion: 1.00
Nodes (1): Proxy to reqAccountUpdates          If ``account`` is ``None``, wait for the ``m

### Community 192 - "Community 192"
Cohesion: 1.00
Nodes (1): Proxy to reqPositions

### Community 193 - "Community 193"
Cohesion: 1.00
Nodes (1): Returns (bool)  if a queue is still valid

## Knowledge Gaps
- **300 isolated node(s):** `Intercept the strategy parameter`, `Analyzer base class. All analyzers are subclass of this one      An Analyzer ins`, `Support for invoking ``len`` on analyzers by actually returning the         curr`, `Receives the cash/value notification before each next cycle`, `Receives the current cash, value, fundvalue and fund shares` (+295 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 14`** (1 nodes): `AbstractDataBase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (1 nodes): `VCBroker`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (2 nodes): `Adds an ``Indicator`` class to the mix. Instantiation will be done at         ```, `Strategy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (1 nodes): `IBBroker`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (1 nodes): `OandaBroker`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (2 nodes): `PumpEvents()`, `VCStore`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (1 nodes): `LineIterator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (1 nodes): `Plot_OldSync`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 87`** (1 nodes): `TimeFrameAnalyzerBase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 91`** (2 nodes): `MetaBase`, `type`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 93`** (2 nodes): `PInfo`, `PlotScheme`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 98`** (1 nodes): `DataClone`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 108`** (1 nodes): `RTEventSink`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 109`** (2 nodes): `_MetaTALibIndicator`, `_TALibIndicator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 111`** (2 nodes): `Calmar`, `This analyzer calculates the CalmarRatio     timeframe which can be different fr`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 112`** (2 nodes): `LogReturnsRolling`, `This analyzer calculates rolling returns for a given timeframe and     compressi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 120`** (2 nodes): `MetaLineActions`, `Metaclass for Lineactions      Scans the instance before init for LineBuffer (or`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 123`** (2 nodes): `MetaStrategy`, `Class has already been created ... register subclasses`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 125`** (2 nodes): `GrossLeverage`, `This analyzer calculates the Gross Leverage of the current strategy     on a tim`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 126`** (2 nodes): `Provides statistics on closed trades (keeps also the count of open ones)`, `TradeAnalyzer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 127`** (2 nodes): `This analyzer reports the transactions occurred with each an every data in     t`, `Transactions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 130`** (1 nodes): `Filter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 131`** (2 nodes): `Accum`, `Cummulative sum of the data values      Formula:       - accum += data`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 132`** (2 nodes): `CommodityChannelIndex`, `Introduced by Donald Lambert in 1980 to measure variations of the     "typical p`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 133`** (2 nodes): `LineOwnOperation`, `Holds an operation that operates on a single operand. Example: abs      It will`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 134`** (2 nodes): `Store provider for Visual Chart binary files      Params:        - ``path`` (def`, `VChartFile`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 135`** (2 nodes): `PeriodStats`, `Calculates basic statistics for given timeframe      Params:        - ``timefram`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 136`** (2 nodes): `PositionsValue`, `This analyzer reports the value of the positions of the current set of     datas`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 137`** (2 nodes): `BlazeData`, `Support for `Blaze <blaze.pydata.org>`_ ``Data`` objects.      Only numeric indi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 140`** (2 nodes): `DaySplitter_Close`, `Splits a daily bar in two parts simulating 2 ticks which will be used to     rep`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 141`** (2 nodes): `DataFilter`, `This class filters out bars from a given data source. In addition to the     sta`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 142`** (2 nodes): `HeikinAshi`, `The filter remodels the open, high, low, close to make HeikinAshi     candlestic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 143`** (1 nodes): `Indicator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 145`** (2 nodes): `Calculates the weighted average of the given data over a period      The default`, `WeightedAverage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 146`** (2 nodes): `HeikinAshi`, `Heikin Ashi candlesticks in the forms of lines      Formula:         ha_open = (`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 147`** (2 nodes): `Formula:       # Buying Pressure = Close - TrueLow       BP = Close - Minimum(Lo`, `UltimateOscillator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 150`** (2 nodes): `MA_CrossOver`, `This is a long-only strategy which operates on a moving average cross      Note:`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 152`** (2 nodes): `Handy function which turns things into things that can be iterated upon`, `Adds a ``Strategy`` class to the mix for optimization. Instantiation         wil`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 153`** (2 nodes): `Fractal`, `References:         [Ref 1] http://www.investopedia.com/articles/trading/06/frac`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 154`** (2 nodes): `See:       - http://www.vortexindicator.com/VFX_VORTEX.PDF`, `Vortex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 155`** (1 nodes): `InfluxDB`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 156`** (2 nodes): `AccelerationDecelerationOscillator`, `Acceleration/Deceleration Technical Indicator (AC) measures acceleration     and`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 157`** (2 nodes): `AwesomeOscillator`, `Awesome Oscillator (AO) is a momentum indicator reflecting the precise     chang`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 158`** (2 nodes): `haDelta`, `Heikin Ashi Delta. Defined by Dan Valcu in his book "Heikin-Ashi: How to     Tra`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 159`** (2 nodes): `Ichimoku`, `Developed and published in his book in 1969 by journalist Goichi Hosoda      For`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 160`** (2 nodes): `KnowSureThing`, `It is a "summed" momentum indicator. Developed by Martin Pring and     published`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 161`** (2 nodes): `The True Strength Indicators was first introduced in Stocks & Commodities     Ma`, `TrueStrengthIndicator`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 162`** (2 nodes): `See:       - http://www.vortexindicator.com/VFX_VORTEX.PDF`, `Vortex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 163`** (1 nodes): `return numeric time part of datetimefloat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 164`** (1 nodes): `Returns True if the order is a Buy order`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 165`** (1 nodes): `WriterStringIO`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 166`** (2 nodes): `Calculates the Reduced value of the ``period`` data points applying     ``functi`, `ReduceN`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 167`** (2 nodes): `MetaLineRoot`, `Once the object is created (effectively pre-init) the "owner" of this     class`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 168`** (1 nodes): `Signal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 169`** (1 nodes): `Sets a specific ``broker`` instance for this strategy, replacing the         one`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 170`** (1 nodes): `If signals are added to the system and the ``accumulate`` value is         set t`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 171`** (1 nodes): `Add the keys, values of kwargs to the internal info dictionary to         hold c`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 172`** (1 nodes): `Tries to retrieve the status from the broker in which the order is.          Def`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 173`** (1 nodes): `Marks an order as cancelled`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 174`** (1 nodes): `Marks an order as completely filled`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 175`** (1 nodes): `Marks an order as expired. Returns True if it worked`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 176`** (1 nodes): `Returns True if the order is a Sell order`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 177`** (1 nodes): `Marks an order as having met a margin call`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 178`** (1 nodes): `Marks an order as partially filled`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 179`** (1 nodes): `Marks an order as rejected`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 180`** (1 nodes): `Receives the current position for the asset and stotres it`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 181`** (1 nodes): `Called when the data is no longer producing bars          Can be called multiple`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 182`** (1 nodes): `Receive answer and pass it to the queue`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 183`** (1 nodes): `Return the pending "store" notifications`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 184`** (1 nodes): `Returns broker with *args, **kwargs from registered ``BrokerCls```
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 185`** (1 nodes): `Returns ``DataCls`` with args, kwargs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 186`** (1 nodes): `returns a contract from the parameters without check`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 187`** (1 nodes): `Receive the event ``openOrder`` events`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 188`** (1 nodes): `Receive the event ``orderStatus```
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 189`** (1 nodes): `Receive event positions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 190`** (1 nodes): `Receives x seconds Real Time Bars (at the time of writing only 5         seconds`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 191`** (1 nodes): `Proxy to reqAccountUpdates          If ``account`` is ``None``, wait for the ``m`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 192`** (1 nodes): `Proxy to reqPositions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 193`** (1 nodes): `Returns (bool)  if a queue is still valid`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MetaParams` connect `Community 7` to `Community 23`, `Community 44`, `Community 34`, `Community 24`, `Community 69`, `Community 6`, `Community 35`, `Community 25`, `Community 12`, `Community 45`, `Community 58`, `Community 48`, `Community 152`, `Community 57`, `Community 47`, `Community 170`, `Community 33`, `Community 53`, `Community 169`, `Community 80`, `Community 26`, `Community 40`, `Community 18`, `Community 130`, `Community 15`, `Community 91`, `Community 52`, `Community 65`, `Community 92`, `Community 171`, `Community 164`, `Community 176`, `Community 180`, `Community 172`, `Community 179`, `Community 173`, `Community 177`, `Community 174`, `Community 178`, `Community 175`, `Community 62`, `Community 29`, `Community 186`, `Community 187`, `Community 188`, `Community 192`, `Community 189`, `Community 191`, `Community 121`, `Community 185`, `Community 184`, `Community 183`, `Community 94`, `Community 56`, `Community 77`, `Community 193`, `Community 182`, `Community 190`, `Community 4`, `Community 108`, `Community 67`, `Community 37`?**
  _High betweenness centrality (0.263) - this node is a cross-community bridge._
- **Why does `Strategy` connect `Community 33` to `Community 12`, `Community 45`, `Community 58`, `Community 48`, `Community 152`, `Community 57`, `Community 47`, `Community 170`, `Community 53`, `Community 169`, `Community 15`, `Community 38`, `Community 41`, `Community 13`, `Community 3`, `Community 51`, `Community 21`?**
  _High betweenness centrality (0.058) - this node is a cross-community bridge._
- **Why does `LineSeries` connect `Community 9` to `Community 10`, `Community 19`, `Community 41`, `Community 3`, `Community 148`, `Community 13`, `Community 15`, `Community 0`, `Community 1`, `Community 51`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Are the 256 inferred relationships involving `MetaParams` (e.g. with `BrokerBase` and `MetaBroker`) actually correct?**
  _`MetaParams` has 256 INFERRED edges - model-reasoned connections that need verification._
- **Are the 69 inferred relationships involving `LineRoot` (e.g. with `LineActions` and `LineBuffer`) actually correct?**
  _`LineRoot` has 69 INFERRED edges - model-reasoned connections that need verification._
- **Are the 106 inferred relationships involving `LineSingle` (e.g. with `LineActions` and `LineBuffer`) actually correct?**
  _`LineSingle` has 106 INFERRED edges - model-reasoned connections that need verification._
- **Are the 54 inferred relationships involving `Strategy` (e.g. with `Cerebro` and `OptReturn`) actually correct?**
  _`Strategy` has 54 INFERRED edges - model-reasoned connections that need verification._