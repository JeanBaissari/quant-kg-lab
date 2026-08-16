# Graph Report - knowledge_graphs/ta/repo/ta  (2026-08-13)

## Corpus Check
- Corpus is ~16,991 words - fits in a single context window. You may not need a graph.

## Summary
- 538 nodes · 1208 edges · 42 communities detected
- Non-singleton communities: 42
- Extraction: EXTRACTED: 54.5% · INFERRED: 45.4%
- Edge kinds: calls: 87 · contains: 134 · inherits: 43 · method: 170 · rationale_for: 225 · uses: 549

## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 8 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `a890410`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes

- `IndicatorMixin` (259)
- `trend.py` (44)
- `IndicatorMixin` (43)
- `.. module:: wrapper    :synopsis: Wrapper of Indicators.  .. moduleauthor:: Dari` (43)
- `Add volatility technical analysis features to dataframe.      Args:         df (` (43)
- `Add trend technical analysis features to dataframe.      Args:         df (panda` (43)
- `Add trend technical analysis features to dataframe.      Args:         df (panda` (43)
- `Add others analysis features to dataframe.      Args:         df (pandas.core.fr` (43)
- `Add all technical analysis features to dataframe.      Args:         df (pandas.` (43)
- `Add volume technical analysis features to dataframe.      Args:         df (pand` (43)

## Surprising Connections (you probably didn't know these)
- `.. module:: momentum    :synopsis: Momentum Indicators.  .. moduleauthor:: Dario` --uses--> `IndicatorMixin`  [INFERRED]
  momentum.py → utils.py
- `Kaufman's Adaptive Moving Average (KAMA)      Moving average designed to account` --uses--> `IndicatorMixin`  [INFERRED]
  momentum.py → utils.py
- `Rate of Change (ROC)      The Rate-of-Change (ROC) indicator, which is also refe` --uses--> `IndicatorMixin`  [INFERRED]
  momentum.py → utils.py
- `Stochastic RSI      The StochRSI oscillator was developed to take advantage of b` --uses--> `IndicatorMixin`  [INFERRED]
  momentum.py → utils.py
- `Stochastic RSI %k      The StochRSI oscillator was developed to take advantage o` --uses--> `IndicatorMixin`  [INFERRED]
  momentum.py → utils.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (41): awesome_oscillator(), AwesomeOscillatorIndicator, Awesome Oscillator      From: https://www.tradingview.com/wiki/Awesome_Oscillato, Awesome Oscillator          Returns:             pandas.Series: New feature gene, Awesome Oscillator      From: https://www.tradingview.com/wiki/Awesome_Oscillato, ema_indicator(), EMAIndicator, Schaff Trend Cycle (STC)      The Schaff Trend Cycle (STC) is a charting indicat (+33 more)

### Community 1 - "Community 1"
Cohesion: 0.07
Nodes (22): IndicatorMixin, cumulative_return(), CumulativeReturnIndicator, daily_log_return(), daily_return(), DailyLogReturnIndicator, DailyReturnIndicator, .. module:: others    :synopsis: Others Indicators.  .. moduleauthor:: Dario Lop (+14 more)

### Community 2 - "Community 2"
Cohesion: 0.08
Nodes (18): keltner_channel_hband(), keltner_channel_hband_indicator(), keltner_channel_lband(), keltner_channel_lband_indicator(), keltner_channel_mband(), KeltnerChannel, KeltnerChannel      Keltner Channels are a trend following indicator used to ide, Keltner Channel Middle Band          Returns:             pandas.Series: New fea (+10 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (16): bollinger_hband(), bollinger_hband_indicator(), bollinger_lband_indicator(), bollinger_pband(), BollingerBands, Bollinger Channel Middle Band          Returns:             pandas.Series: New f, Bollinger Channel High Band          Returns:             pandas.Series: New fea, Bollinger Channel Low Band          Returns:             pandas.Series: New feat (+8 more)

### Community 4 - "Community 4"
Cohesion: 0.08
Nodes (17): donchian_channel_hband(), donchian_channel_lband(), donchian_channel_mband(), donchian_channel_pband(), donchian_channel_wband(), DonchianChannel, Donchian Channel      https://www.investopedia.com/terms/d/donchianchannels.asp, Donchian Channel High Band          Returns:             pandas.Series: New feat (+9 more)

### Community 5 - "Community 5"
Cohesion: 0.10
Nodes (13): psar_down(), psar_down_indicator(), psar_up(), PSARIndicator, PSAR value          Returns:             pandas.Series: New feature generated., PSAR up trend value          Returns:             pandas.Series: New feature gen, PSAR down trend value          Returns:             pandas.Series: New feature g, PSAR up trend value indicator          Returns:             pandas.Series: New f (+5 more)

### Community 6 - "Community 6"
Cohesion: 0.11
Nodes (12): ichimoku_a(), ichimoku_b(), ichimoku_base_line(), IchimokuIndicator, Kijun-sen (Base Line)      It identifies the trend and look for potential signal, Ichimoku Kinkō Hyō (Ichimoku)      It identifies the trend and look for potentia, Ichimoku Kinkō Hyō (Ichimoku)      It identifies the trend and look for potentia, Ichimoku Kinkō Hyō (Ichimoku)      http://stockcharts.com/school/doku.php?id=cha (+4 more)

### Community 7 - "Community 7"
Cohesion: 0.13
Nodes (11): Stochastic RSI      The StochRSI oscillator was developed to take advantage of b, Stochastic RSI %k      The StochRSI oscillator was developed to take advantage o, Stochastic RSI %d      The StochRSI oscillator was developed to take advantage o, Stochastic RSI      The StochRSI oscillator was developed to take advantage of b, Stochastic RSI          Returns:             pandas.Series: New feature generate, Stochastic RSI %k          Returns:             pandas.Series: New feature gener, Stochastic RSI %d          Returns:             pandas.Series: New feature gener, stochrsi() (+3 more)

### Community 8 - "Community 8"
Cohesion: 0.13
Nodes (10): MACD, macd_diff(), macd_signal(), Moving Average Convergence Divergence (MACD)      Is a trend-following momentum, Moving Average Convergence Divergence (MACD Signal)      Shows EMA of MACD., MACD Line          Returns:             pandas.Series: New feature generated., Moving Average Convergence Divergence (MACD Diff)      Shows the relationship be, Signal Line          Returns:             pandas.Series: New feature generated. (+2 more)

### Community 9 - "Community 9"
Cohesion: 0.14
Nodes (9): PercentageVolumeOscillator, pvo(), pvo_hist(), The Percentage Volume Oscillator (PVO) is a momentum oscillator for volume., The Percentage Volume Oscillator (PVO) is a momentum oscillator for volume., The Percentage Volume Oscillator (PVO) is a momentum oscillator for volume., PVO Line          Returns:             pandas.Series: New feature generated., Signal Line          Returns:             pandas.Series: New feature generated. (+1 more)

### Community 10 - "Community 10"
Cohesion: 0.14
Nodes (9): adx(), adx_neg(), ADXIndicator, Average Directional Movement Index (ADX)      The Plus Directional Indicator (+D, Average Directional Movement Index Negative (ADX)      The Plus Directional Indi, Average Directional Movement Index (ADX)      The Plus Directional Indicator (+D, Average Directional Index (ADX)          Returns:             pandas.Series: New, Plus Directional Indicator (+DI)          Returns:             pandas.Series: Ne (+1 more)

### Community 11 - "Community 11"
Cohesion: 0.14
Nodes (9): aroon_down(), aroon_up(), AroonIndicator, Aroon Indicator      Identify when trends are likely to change direction.      A, Aroon Indicator (AI)      Identify when trends are likely to change direction (u, Aroon Indicator (AI)      Identify when trends are likely to change direction (d, Aroon Up Channel          Returns:             pandas.Series: New feature genera, Aroon Down Channel          Returns:             pandas.Series: New feature gene (+1 more)

### Community 12 - "Community 12"
Cohesion: 0.14
Nodes (9): kst(), kst_sig(), KSTIndicator, KST Oscillator (KST)      It is useful to identify major stock market cycle junc, KST Oscillator (KST Signal)      It is useful to identify major stock market cyc, KST Oscillator (KST Signal)      It is useful to identify major stock market cyc, Know Sure Thing (KST)          Returns:             pandas.Series: New feature g, Signal Line Know Sure Thing (KST)          nsig-period SMA of KST          Retur (+1 more)

### Community 13 - "Community 13"
Cohesion: 0.14
Nodes (9): Vortex Indicator (VI)      It consists of two oscillators that capture positive, Vortex Indicator (VI)      It consists of two oscillators that capture positive, Vortex Indicator (VI)      It consists of two oscillators that capture positive, +VI          Returns:             pandas.Series: New feature generated., -VI          Returns:             pandas.Series: New feature generated., Diff VI          Returns:             pandas.Series: New feature generated., vortex_indicator_neg(), vortex_indicator_pos() (+1 more)

### Community 14 - "Community 14"
Cohesion: 0.17
Nodes (7): PercentagePriceOscillator, ppo_hist(), The Percentage Price Oscillator (PPO) is a momentum oscillator that measures, The Percentage Price Oscillator (PPO) is a momentum oscillator that measures, Percentage Price Oscillator Line          Returns:             pandas.Series: Ne, Percentage Price Oscillator Signal Line          Returns:             pandas.Ser, Percentage Price Oscillator Histogram          Returns:             pandas.Serie

### Community 15 - "Community 15"
Cohesion: 0.17
Nodes (8): Stochastic Oscillator      Developed in the late 1950s by George Lane. The stoch, Stochastic Oscillator          Returns:             pandas.Series: New feature g, Signal Stochastic Oscillator          Returns:             pandas.Series: New fe, Stochastic Oscillator      Developed in the late 1950s by George Lane. The stoch, Stochastic Oscillator Signal      Shows SMA of Stochastic Oscillator. Typically, stoch(), stoch_signal(), StochasticOscillator

### Community 16 - "Community 16"
Cohesion: 0.17
Nodes (11): bollinger_lband(), bollinger_mavg(), bollinger_wband(), keltner_channel_pband(), keltner_channel_wband(), .. module:: volatility    :synopsis: Volatility Indicators.  .. moduleauthor:: D, Bollinger Bands (BB)      N-period simple moving average (MA).      https://en.w, Bollinger Bands (BB)      Lower band at K times an N-period standard deviation b (+3 more)

### Community 17 - "Community 17"
Cohesion: 0.17
Nodes (8): ease_of_movement(), EaseOfMovementIndicator, Ease of movement (EoM, EMV)      It relate an asset's price change to its volume, Ease of movement (EoM, EMV)          Returns:             pandas.Series: New fea, Signal Ease of movement (EoM, EMV)          Returns:             pandas.Series:, Ease of movement (EoM, EMV)      It relate an asset's price change to its volume, Ease of movement (EoM, EMV)      It relate an asset's price change to its volume, sma_ease_of_movement()

### Community 18 - "Community 18"
Cohesion: 0.22
Nodes (5): Relative Strength Index (RSI)      Compares the magnitude of recent gains and lo, Relative Strength Index (RSI)          Returns:             pandas.Series: New f, Relative Strength Index (RSI)      Compares the magnitude of recent gains and lo, rsi(), RSIIndicator

### Community 19 - "Community 19"
Cohesion: 0.22
Nodes (5): IndicatorMixin, Util mixin indicator class, Check if fillna flag is True.          Args:             series(pandas.Series):, Bollinger Channel Percentage Band          From: https://school.stockcharts.com/, Keltner Channel Percentage Band          Returns:             pandas.Series: New

### Community 20 - "Community 20"
Cohesion: 0.22
Nodes (5): average_true_range(), AverageTrueRange, Average True Range (ATR)      The indicator provide an indication of the degree, Average True Range (ATR)      The indicator provide an indication of the degree, Average True Range (ATR)          Returns:             pandas.Series: New featur

### Community 21 - "Community 21"
Cohesion: 0.22
Nodes (6): Volume-price trend (VPT)      Is based on a running cumulative volume that adds, Volume-price trend (VPT)          Returns:             pandas.Series: New featur, Volume-price trend (VPT)      Is based on a running cumulative volume that adds, volume_price_trend(), VolumePriceTrendIndicator, Add trend technical analysis features to dataframe.      Args:         df (panda

### Community 22 - "Community 22"
Cohesion: 0.25
Nodes (5): kama(), KAMAIndicator, Kaufman's Adaptive Moving Average (KAMA)      Moving average designed to account, Kaufman's Adaptive Moving Average (KAMA)      Moving average designed to account, Kaufman's Adaptive Moving Average (KAMA)          Returns:             pandas.Se

### Community 23 - "Community 23"
Cohesion: 0.25
Nodes (5): Rate of Change (ROC)      The Rate-of-Change (ROC) indicator, which is also refe, Rate of Change (ROC)      The Rate-of-Change (ROC) indicator, which is also refe, Rate of Change (ROC)          Returns:             pandas.Series: New feature ge, roc(), ROCIndicator

### Community 24 - "Community 24"
Cohesion: 0.25
Nodes (5): True strength index (TSI)          Returns:             pandas.Series: New featu, True strength index (TSI)      Shows both trend direction and overbought/oversol, True strength index (TSI)      Shows both trend direction and overbought/oversol, tsi(), TSIIndicator

### Community 25 - "Community 25"
Cohesion: 0.25
Nodes (5): Ultimate Oscillator      Larry Williams' (1976) signal, a momentum oscillator de, Ultimate Oscillator          Returns:             pandas.Series: New feature gen, Ultimate Oscillator      Larry Williams' (1976) signal, a momentum oscillator de, ultimate_oscillator(), UltimateOscillator

### Community 26 - "Community 26"
Cohesion: 0.25
Nodes (5): Williams %R      Developed by Larry Williams, Williams %R is a momentum indicato, Williams %R          Returns:             pandas.Series: New feature generated., Williams %R      From: http://stockcharts.com/school/doku.php?id=chart_school:te, williams_r(), WilliamsRIndicator

### Community 27 - "Community 27"
Cohesion: 0.25
Nodes (7): ppo(), ppo_signal(), pvo_signal(), .. module:: momentum    :synopsis: Momentum Indicators.  .. moduleauthor:: Dario, The Percentage Price Oscillator (PPO) is a momentum oscillator that measures, The Percentage Price Oscillator (PPO) is a momentum oscillator that measures, The Percentage Volume Oscillator (PVO) is a momentum oscillator for volume.

### Community 28 - "Community 28"
Cohesion: 0.25
Nodes (5): cci(), CCIIndicator, Commodity Channel Index (CCI)      CCI measures the difference between a securit, Commodity Channel Index (CCI)      CCI measures the difference between a securit, Commodity Channel Index (CCI)          Returns:             pandas.Series: New f

### Community 29 - "Community 29"
Cohesion: 0.25
Nodes (5): dpo(), DPOIndicator, Detrended Price Oscillator (DPO)      Is an indicator designed to remove trend f, Detrended Price Oscillator (DPO)      Is an indicator designed to remove trend f, Detrended Price Oscillator (DPO)          Returns:             pandas.Series: Ne

### Community 30 - "Community 30"
Cohesion: 0.25
Nodes (5): mass_index(), MassIndex, Mass Index (MI)      It uses the high-low range to identify trend reversals base, Mass Index (MI)      It uses the high-low range to identify trend reversals base, Mass Index (MI)          Returns:             pandas.Series: New feature generat

### Community 31 - "Community 31"
Cohesion: 0.25
Nodes (7): adx_pos(), ichimoku_conversion_line(), psar_up_indicator(), .. module:: trend    :synopsis: Trend Indicators.  .. moduleauthor:: Dario Lopez, Average Directional Movement Index Positive (ADX)      The Plus Directional Indi, Tenkan-sen (Conversion Line)      It identifies the trend and look for potential, Parabolic Stop and Reverse (Parabolic SAR) Upward Trend Indicator      Returns 1

### Community 32 - "Community 32"
Cohesion: 0.25
Nodes (5): dropna(), _get_min_max(), .. module:: utils    :synopsis: Utils classes and functions.  .. moduleauthor::, Drop rows with "Nans" values, Find min or max value between two lists for each index

### Community 33 - "Community 33"
Cohesion: 0.25
Nodes (5): acc_dist_index(), AccDistIndexIndicator, Accumulation/Distribution Index (ADI)      Acting as leading indicator of price, Accumulation/Distribution Index (ADI)      Acting as leading indicator of price, Accumulation/Distribution Index (ADI)          Returns:             pandas.Serie

### Community 34 - "Community 34"
Cohesion: 0.25
Nodes (5): chaikin_money_flow(), ChaikinMoneyFlowIndicator, Chaikin Money Flow (CMF)      It measures the amount of Money Flow Volume over a, Chaikin Money Flow (CMF)          Returns:             pandas.Series: New featur, Chaikin Money Flow (CMF)      It measures the amount of Money Flow Volume over a

### Community 35 - "Community 35"
Cohesion: 0.25
Nodes (5): force_index(), ForceIndexIndicator, Force Index (FI)      It illustrates how strong the actual buying or selling pre, Force Index (FI)          Returns:             pandas.Series: New feature genera, Force Index (FI)      It illustrates how strong the actual buying or selling pre

### Community 36 - "Community 36"
Cohesion: 0.25
Nodes (5): MFIIndicator, money_flow_index(), Money Flow Index (MFI)      Uses both price and volume to measure buying and sel, Money Flow Index (MFI)          Returns:             pandas.Series: New feature, Money Flow Index (MFI)      Uses both price and volume to measure buying and sel

### Community 37 - "Community 37"
Cohesion: 0.25
Nodes (5): negative_volume_index(), NegativeVolumeIndexIndicator, Negative Volume Index (NVI)      http://stockcharts.com/school/doku.php?id=chart, Negative Volume Index (NVI)          Returns:             pandas.Series: New fea, Negative Volume Index (NVI)      http://stockcharts.com/school/doku.php?id=chart

### Community 38 - "Community 38"
Cohesion: 0.25
Nodes (5): on_balance_volume(), OnBalanceVolumeIndicator, On-balance volume (OBV)      It relates price and volume in the stock market. OB, On-balance volume (OBV)      It relates price and volume in the stock market. OB, On-balance volume (OBV)          Returns:             pandas.Series: New feature

### Community 39 - "Community 39"
Cohesion: 0.29
Nodes (4): Volume Weighted Average Price (VWAP)      VWAP equals the dollar value of all tr, Volume Weighted Average Price (VWAP)          Returns:             pandas.Series, VolumeWeightedAveragePrice, Add trend technical analysis features to dataframe.      Args:         df (panda

### Community 40 - "Community 40"
Cohesion: 0.50
Nodes (3): .. module:: volume    :synopsis: Volume Indicators.  .. moduleauthor:: Dario Lop, Volume Weighted Average Price (VWAP)      VWAP equals the dollar value of all tr, volume_weighted_average_price()

### Community 41 - "Community 41"
Cohesion: 1.00
Nodes (1): It is a Technical Analysis library useful to do feature engineering from financi

## Knowledge Gaps
- **6 isolated node(s):** `It is a Technical Analysis library useful to do feature engineering from financi`, `.. module:: utils    :synopsis: Utils classes and functions.  .. moduleauthor::`, `Util mixin indicator class`, `Check if fillna flag is True.          Args:             series(pandas.Series):`, `Drop rows with "Nans" values` (+1 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 41`** (1 nodes): `It is a Technical Analysis library useful to do feature engineering from financi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `IndicatorMixin` connect `Community 19` to `Community 0`, `Community 22`, `Community 14`, `Community 9`, `Community 27`, `Community 23`, `Community 7`, `Community 24`, `Community 25`, `Community 18`, `Community 15`, `Community 26`, `Community 1`, `Community 10`, `Community 11`, `Community 28`, `Community 29`, `Community 6`, `Community 12`, `Community 8`, `Community 30`, `Community 5`, `Community 31`, `Community 13`, `Community 32`, `Community 20`, `Community 3`, `Community 4`, `Community 2`, `Community 16`, `Community 33`, `Community 34`, `Community 17`, `Community 35`, `Community 36`, `Community 37`, `Community 38`, `Community 40`, `Community 21`, `Community 39`?**
  _High betweenness centrality (0.720) - this node is a cross-community bridge._
- **Why does `BollingerBands` connect `Community 3` to `Community 16`, `Community 1`, `Community 19`, `Community 0`, `Community 39`, `Community 21`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Why does `KeltnerChannel` connect `Community 2` to `Community 16`, `Community 1`, `Community 19`, `Community 20`, `Community 0`, `Community 39`, `Community 21`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Are the 255 inferred relationships involving `IndicatorMixin` (e.g. with `AwesomeOscillatorIndicator` and `KAMAIndicator`) actually correct?**
  _`IndicatorMixin` has 255 INFERRED edges - model-reasoned connections that need verification._
- **Are the 42 inferred relationships involving `.. module:: wrapper    :synopsis: Wrapper of Indicators.  .. moduleauthor:: Dari` (e.g. with `AwesomeOscillatorIndicator` and `KAMAIndicator`) actually correct?**
  _`.. module:: wrapper    :synopsis: Wrapper of Indicators.  .. moduleauthor:: Dari` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Are the 42 inferred relationships involving `Add volume technical analysis features to dataframe.      Args:         df (pand` (e.g. with `AwesomeOscillatorIndicator` and `KAMAIndicator`) actually correct?**
  _`Add volume technical analysis features to dataframe.      Args:         df (pand` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Are the 42 inferred relationships involving `Add volatility technical analysis features to dataframe.      Args:         df (` (e.g. with `AwesomeOscillatorIndicator` and `KAMAIndicator`) actually correct?**
  _`Add volatility technical analysis features to dataframe.      Args:         df (` has 42 INFERRED edges - model-reasoned connections that need verification._