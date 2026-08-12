---
name: ta-lib-indicators
description: "Use when computing technical indicators with TA-Lib \u2014 SMA, EMA,\
  \ RSI, MACD, BBANDS, ATR, ADX, STOCH, and 200+ others."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: TA-Lib/ta-lib-python
source_commit: a9ff1b47b3ddbd57274116645d688c0ed677338b
extraction_date: 2026-07-29
graph:
  nodes: 381
  edges: 379
  community_count: 174
  graph_hash: 1cdcccf662bedb05
tags:
- ta-lib
- indicators
related_skills: []
---

# TA-Lib Indicators (`talib`)

TA-Lib (Technical Analysis Library) is a C library with Python bindings via Cython. It provides **200+ technical indicators** across multiple categories: overlap studies, momentum oscillators, volatility, volume, cycle indicators, price transforms, and candlestick pattern recognition (61 patterns). All functions accept numpy arrays and return numpy arrays.

## Quick Reference

| Function | Category | Signature | Description | Graph Node |
|--------|--------|---------|-----------|----------|
| `SMA` | Overlap | `talib.SMA(close, timeperiod=30)` | Simple Moving Average | _ta_lib.c:L35583 |
| `EMA` | Overlap | `talib.EMA(close, timeperiod=30)` | Exponential Moving Average | _ta_lib.c:L25986 |
| `WMA` | Overlap | `talib.WMA(close, timeperiod=30)` | Weighted Moving Average | _ta_lib.c:L39678 |
| `DEMA` | Overlap | `talib.DEMA(close, timeperiod=30)` | Double Exponential MA | _ta_lib.c:L25420 |
| `TEMA` | Overlap | `talib.TEMA(close, timeperiod=30)` | Triple Exponential MA | _ta_lib.c:L37747 |
| `KAMA` | Overlap | `talib.KAMA(close, timeperiod=30)` | Kaufman Adaptive MA | _ta_lib.c:L27668 |
| `MAMA` | Overlap | `talib.MAMA(close)` | MESA Adaptive MA (returns MAMA, FAMA) | _ta_lib.c:L29768 |
| `BBANDS` | Overlap | `talib.BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)` | Bollinger Bands (upper, middle, lower) | _ta_lib.c:L10779 |
| `SAR` | Overlap | `talib.SAR(high, low, acceleration=0.02, maximum=0.2)` | Parabolic SAR | _ta_lib.c:L34761 |
| `RSI` | Momentum | `talib.RSI(close, timeperiod=14)` | Relative Strength Index | _ta_lib.c:L34584 |
| `MACD` | Momentum | `talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)` | MACD (macd, signal, hist) | _ta_lib.c:L29064 |
| `MACDEXT` | Momentum | `talib.MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)` | MACD with controllable MA types | _ta_lib.c:L29294 |
| `MACDFIX` | Momentum | `talib.MACDFIX(close, signalperiod=9)` | MACD with fixed 12/26 periods | _ta_lib.c:L29566 |
| `STOCH` | Momentum | `talib.STOCH(high, low, close, fastk_period=5, slowk_period=3, slowd_period=3)` | Stochastic (slowk, slowd) | _ta_lib.c:L36111 |
| `STOCHF` | Momentum | `talib.STOCHF(high, low, close, fastk_period=5, fastd_period=3)` | Fast Stochastic | _ta_lib.c:L36393 |
| `STOCHRSI` | Momentum | `talib.STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3)` | Stochastic RSI | _ta_lib.c:L36647 |
| `ADX` | Momentum | `talib.ADX(high, low, close, timeperiod=14)` | Average Directional Index | _ta_lib.c:L8829 |
| `ADXR` | Momentum | `talib.ADXR(high, low, close, timeperiod=14)` | ADX Rating | _ta_lib.c:L9040 |
| `CCI` | Momentum | `talib.CCI(high, low, close, timeperiod=14)` | Commodity Channel Index | _ta_lib.c:L11428 |
| `MFI` | Momentum | `talib.MFI(high, low, close, volume, timeperiod=14)` | Money Flow Index | _ta_lib.c:L30742 |
| `WILLR` | Momentum | `talib.WILLR(high, low, close, timeperiod=14)` | Williams %R | _ta_lib.c:L39467 |
| `ULTOSC` | Momentum | `talib.ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)` | Ultimate Oscillator | _ta_lib.c:L38843 |
| `ATR` | Volatility | `talib.ATR(high, low, close, timeperiod=14)` | Average True Range | _ta_lib.c:L10181 |
| `NATR` | Volatility | `talib.NATR(high, low, close, timeperiod=14)` | Normalized ATR | _ta_lib.c:L32876 |
| `OBV` | Volume | `talib.OBV(close, volume)` | On-Balance Volume | _ta_lib.c:L33087 |
| `AD` | Volume | `talib.AD(high, low, close, volume)` | Chaikin A/D Line | _ta_lib.c:L8200 |
| `ADOSC` | Volume | `talib.ADOSC(high, low, close, volume, fastperiod=3, slowperiod=10)` | Chaikin A/D Oscillator | _ta_lib.c:L8588 |
| `HT_DCPERIOD` | Cycle | `talib.HT_DCPERIOD(close)` | Hilbert Transform — Dominant Cycle Period | _ta_lib.c:L26483 |
| `HT_DCPHASE` | Cycle | `talib.HT_DCPHASE(close)` | Hilbert Transform — Dominant Cycle Phase | _ta_lib.c:L26643 |
| `HT_PHASOR` | Cycle | `talib.HT_PHASOR(close)` | Hilbert Transform — Phasor Components | _ta_lib.c:L26803 |

## Full Function Reference by Category

### Overlap Studies (17 functions)
`SMA`, `EMA`, `WMA`, `DEMA`, `TEMA`, `TRIMA`, `KAMA`, `MAMA`, `T3`, `MA`, `BBANDS`, `SAR`, `SAREXT`, `MIDPOINT`, `MIDPRICE`, `HT_TRENDLINE`, `MAVP`

### Momentum Indicators (30 functions)
`RSI`, `MACD`, `MACDEXT`, `MACDFIX`, `STOCH`, `STOCHF`, `STOCHRSI`, `ADX`, `ADXR`, `APO`, `PPO`, `CCI`, `MFI`, `WILLR`, `ULTOSC`, `MOM`, `ROC`, `ROCP`, `ROCR`, `ROCR100`, `TRIX`, `AROON`, `AROONOSC`, `BOP`, `CMO`, `DX`, `MINUS_DI`, `MINUS_DM`, `PLUS_DI`, `PLUS_DM`

### Volatility Indicators (4 functions)
`ATR`, `NATR`, `TRANGE`, `AVGDEV`

### Volume Indicators (4 functions)
`OBV`, `AD`, `ADOSC`, `LINEARREG_ANGLE`

### Price Transform (4 functions)
`AVGPRICE`, `MEDPRICE`, `TYPPRICE`, `WCLPRICE`

### Cycle Indicators (6 functions)
`HT_DCPERIOD`, `HT_DCPHASE`, `HT_PHASOR`, `HT_SINE`, `HT_TRENDMODE`, `HT_TRENDLINE`

### Pattern Recognition (61 functions)
`CDL2CROWS`, `CDL3BLACKCROWS`, `CDL3INSIDE`, `CDL3LINESTRIKE`, `CDL3OUTSIDE`, `CDL3STARSINSOUTH`, `CDL3WHITESOLDIERS`, `CDLABANDONEDBABY`, `CDLADVANCEBLOCK`, `CDLBELTHOLD`, `CDLBREAKAWAY`, `CDLCLOSINGMARUBOZU`, `CDLCONCEALBABYSWALL`, `CDLCOUNTERATTACK`, `CDLDARKCLOUDCOVER`, `CDLDOJI`, `CDLDOJISTAR`, `CDLDRAGONFLYDOJI`, `CDLENGULFING`, `CDLEVENINGDOJISTAR`, `CDLEVENINGSTAR`, `CDLGAPSIDESIDEWHITE`, `CDLGRAVESTONEDOJI`, `CDLHAMMER`, `CDLHANGINGMAN`, `CDLHARAMI`, `CDLHARAMICROSS`, `CDLHIGHWAVE`, `CDLHIKKAKE`, `CDLHIKKAKEMOD`, `CDLHOMINGPIGEON`, `CDLIDENTICAL3CROWS`, `CDLINNECK`, `CDLINVERTEDHAMMER`, `CDLKICKING`, `CDLKICKINGBYLENGTH`, `CDLLADDERBOTTOM`, `CDLLONGLEGGEDDOJI`, `CDLLONGLINE`, `CDLMARUBOZU`, `CDLMATCHINGLOW`, `CDLMATHOLD`, `CDLMORNINGDOJISTAR`, `CDLMORNINGSTAR`, `CDLONNECK`, `CDLPIERCING`, `CDLRICKSHAWMAN`, `CDLRISEFALL3METHODS`, `CDLSEPARATINGLINES`, `CDLSHOOTINGSTAR`, `CDLSHORTLINE`, `CDLSPINNINGTOP`, `CDLSTALLEDPATTERN`, `CDLSTICKSANDWICH`, `CDLTAKURI`, `CDLTASUKIGAP`, `CDLTHRUSTING`, `CDLTRISTAR`, `CDLUNIQUE3RIVER`, `CDLUPSIDEGAP2CROWS`, `CDLXSIDEGAP3METHODS`

### Statistic Functions (9 functions)
`BETA`, `CORREL`, `LINEARREG`, `LINEARREG_ANGLE`, `LINEARREG_INTERCEPT`, `LINEARREG_SLOPE`, `STDDEV`, `TSF`, `VAR`

### Math Transform / Operators (24 functions)
`ACOS`, `ASIN`, `ATAN`, `CEIL`, `COS`, `COSH`, `EXP`, `FLOOR`, `LN`, `LOG10`, `SIN`, `SINH`, `SQRT`, `TAN`, `TANH`, `ADD`, `DIV`, `MAX`, `MAXINDEX`, `MIN`, `MININDEX`, `MINMAX`, `MINMAXINDEX`, `MULT`, `SUB`, `SUM`

## Architecture Overview

```
talib (Python package)
  ├─ _ta_lib.c (Cython wrapper, 1,130 nodes)
  │    ├─ Compiled from C source: wraps libta_lib.so
  │    ├─ Each function: __pyx_pw_5talib_7_ta_lib_<N><NAME>()
  │    │    ├─ Input validation: check_array(), check_length4(), check_begidx4()
  │    │    ├─ C call: TA_<NAME>() → libta_lib
  │    │    └─ Output: numpy array via make_double_array() / make_int_array()
  │    └─ Stream versions: __pyx_pw_5talib_7_ta_lib_<N>stream_<NAME>()
  │
  ├─ __init__.py
  │    ├─ get_functions() → list of all supported function names
  │    └─ get_function_groups() → dict of {group: [function_names]}
  │
  ├─ abstract.py (Abstract Function API)
  │    ├─ Function('SMA') → callable with dict params
  │    ├─ set_input_arrays() → set price arrays
  │    └─ set_function_args() → configure parameters
  │
  └─ stream.py (Streaming API)
       ├─ Stream instance per function
       └─ Streaming=1 input, no lookback
```

## Common Patterns

### Pattern 1: Basic indicator computation
```python
import talib
import numpy as np

close = np.random.randn(200).cumsum() + 100

# Single output
sma = talib.SMA(close, timeperiod=20)
rsi = talib.RSI(close, timeperiod=14)

# Multiple outputs (returns tuple)
upper, middle, lower = talib.BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2)
macd, signal, hist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
slowk, slowd = talib.STOCH(high, low, close, fastk_period=5, slowk_period=3, slowd_period=3)
```

### Pattern 2: All indicators on price data
```python
import talib
import pandas as pd

df = pd.read_csv('ohlcv.csv')
close = df['Close'].values
high = df['High'].values
low = df['Low'].values
volume = df['Volume'].values

indicators = {
    'sma_20': talib.SMA(close, 20),
    'ema_50': talib.EMA(close, 50),
    'rsi': talib.RSI(close, 14),
    'macd': talib.MACD(close)[0],        # MACD line
    'macd_signal': talib.MACD(close)[1],   # signal line
    'atr': talib.ATR(high, low, close, 14),
    'adx': talib.ADX(high, low, close, 14),
    'bb_upper': talib.BBANDS(close, 20)[0],
    'bb_middle': talib.BBANDS(close, 20)[1],
    'bb_lower': talib.BBANDS(close, 20)[2],
}
```

### Pattern 3: Candlestick pattern detection
```python
import talib

# Returns 0 (no pattern), 100 (bullish), -100 (bearish) per bar
doji = talib.CDLDOJI(open, high, low, close)
engulfing = talib.CDLENGULFING(open, high, low, close)
hammer = talib.CDLHAMMER(open, high, low, close)
morning_star = talib.CDLMORNINGSTAR(open, high, low, close)

# Filter to only bars where pattern appears
bullish_engulfing = engulfing == 100
bearish_engulfing = engulfing == -100
```

### Pattern 4: Moving Average type selection (MAType)
```python
# matype parameter controls MA calculation method
# 0=SMA, 1=EMA, 2=WMA, 3=DEMA, 4=TEMA, 5=TRIMA, 6=KAMA, 7=MAMA, 8=T3
bb_ema = talib.BBANDS(close, timeperiod=20, matype=1)  # EMA-based Bollinger
```

### Pattern 5: Pattern 5: Full strategy signal pipeline
```python
import talib
import numpy as np
import pandas as pd

# Load data
df = pd.read_csv('AAPL.csv', parse_dates=['Date'], index_col='Date')
o, h, l, c, v = [df[c].values for c in ['Open','High','Low','Close','Volume']]

# Generate signals
rsi = talib.RSI(c, timeperiod=14)
macd, signal, hist = talib.MACD(c)

# Entry conditions
entries = (rsi < 30) & (macd > signal)  # oversold + MACD bullish
exits = (rsi > 70) | (macd < signal)     # overbought or MACD bearish

# Pass to vectorbt / backtrader for portfolio simulation
```

### Pattern 6: Abstract API (dynamic function selection)
```python
import talib
from talib.abstract import Function

# Build function by name
inputs = {'open': o, 'high': h, 'low': l, 'close': c, 'volume': v}
sma_func = Function('SMA')
sma_func.set_input_arrays(inputs)
sma_func.set_function_args(timeperiod=20)
result = sma_func.outputs  # Access via .outputs after setting inputs
```

## Pitfalls

1. **NaN output for insufficient data**: All TA-Lib functions require `timeperiod` bars of warmup. The first `timeperiod-1` output values are NaN. Always slice: `result = talib.SMA(close, 20)[19:]` or handle NaN in downstream code.

2. **Return type inconsistency**: Single-output functions return `np.ndarray`. Multi-output functions (BBANDS, MACD, STOCH) return `tuple` of arrays. Test with `isinstance(result, tuple)` before indexing.

3. **Input must be numpy float64**: TA-Lib expects `np.float64` arrays. Passing `pd.Series` usually works (auto-converted), but `pd.Series` with Integer dtype can produce wrong results. Explicitly: `close = df['Close'].astype(np.float64).values`.

4. **C library loading failures**: `talib` must find `libta_lib.so` on the system path. Common install failures: missing `ta-lib` C library (install via `apt install ta-lib` or `brew install ta-lib`), or wrong architecture (ARM vs x86_64). Check: `talib.get_functions()` should return a non-empty list.

5. **Candlestick pattern NaN interpretation**: Pattern functions return 0 for no pattern and 100/-100 for patterns. The value 0 is NOT the same as NaN — 0 means "no pattern detected on this bar," which is valid output. NaN means "insufficient data to evaluate."

6. **STOCH vs STOCHF inputs**: `STOCH` returns `(slowk, slowd)` while `STOCHF` returns `(fastk, fastd)`. Their parameter names differ (`fastk_period` vs `fastk_period` with `slowk_period`/`slowd_period`). Don't confuse the two.

7. **`matype` parameter idempotency**: The `matype` parameter (0=SMA, 1=EMA, etc.) defaults to 0 (SMA). Functions like BBANDS, MACDEXT, STOCH, and AROON accept `matype` but the default may not be what you expect — e.g., BBANDS with `matype=0` uses SMA for the middle band. Switch to EMA-based with `matype=1`.

## Cross-Library Bridges

| Source | Target | Relationship | Description |
|--------|--------|-------------|-------------|
| `talib.SMA/RSI/MACD` | `vectorbt.indicators` | wrapped_by | vectorbt indicators wrap ta-lib functions |
| `talib.SMA/RSI/MACD` | `backtrader.talib` | bridged | backtrader's talib module wraps ta-lib |
| `talib.BBANDS/ATR/RSI` | `vectorbt.SignalFactory` | generates | Indicator values → entry/exit signals |
| `talib.candlestick` | `vectorbt.labels` | maps_to | Pattern recognition → label generation |
| `talib.get_functions()` | `vectorbt.IndicatorBase.parse_ta_config()` | introspection | vectorbt discovers available ta-lib functions |

## Verification Checklist

- [ ] `talib.get_functions()` returns list of 150+ function names
- [ ] `talib.SMA(close, 20)` returns float64 numpy array
- [ ] First `timeperiod-1` elements are NaN (warmup period)
- [ ] Multi-output functions return tuples: `talib.BBANDS()` → `(upper, middle, lower)`
- [ ] Input arrays are `np.float64` dtype (not int or object)
- [ ] `import talib` succeeds (libta_lib.so found on system path)
- [ ] Pattern recognition returns -100 (bearish), 0 (none), 100 (bullish)

## Provenance

- Knowledge graph: ta-lib, 381 nodes, 379 edges, 174 communities
- God nodes: `_ta_lib.c` (373), `__init__.py` (4), `get_functions()` (2) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ a9ff1b47b3dd, backend opencode, description coverage 100%
