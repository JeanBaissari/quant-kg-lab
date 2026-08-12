---
name: scipy-signal
description: "Use when processing signals with SciPy \u2014 filtering (butter/filtfilt),\
  \ spectral analysis (welch/stft), detrending, and convolution/correlation."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scipy/scipy
source_commit: 0514ef9e73297ef8d6f46379731eedc619f9d201
extraction_date: 2026-07-29
graph:
  nodes: 14071
  edges: 23466
  community_count: 1076
  graph_hash: 1c051b3be2968b39
tags:
- scipy
- signal
related_skills: []
---

# scipy.signal

Signal processing toolbox for filter design, spectral analysis, convolution, peak finding, and linear time-invariant (LTI) system analysis. Essential for preprocessing time-series data before feeding into quantitative models.

## Quick Reference: Top 10 APIs

| API | Source File | Degree | Description |
|-----|------------|--------|-------------|
| `ShortTimeFFT` | `_short_time_fft.py` | 104 | Short-time Fourier transform with inverse, spectrogram, and cross-spectrogram |
| `StateSpace` | `_ltisys.py` | 26 | Linear system in state-space representation (A, B, C, D matrices) |
| `TransferFunction` | `_ltisys.py` | 17 | LTI system in transfer function form (num, den polynomials) |
| `ZerosPolesGain` | `_ltisys.py` | 16 | LTI system in zero-pole-gain form |
| `iirfilter()` | `_filter_design.py` | 15 | General IIR filter design (Butterworth, Chebyshev, elliptic) |
| `convolve()` | `_signaltools.py` | 10 | N-dimensional convolution |
| `lfilter()` | `_signaltools.py` | 8 | Direct-form II IIR filtering of a 1-D signal |
| `filtfilt()` | `_signaltools.py` | 7 | Zero-phase forward-backward digital filtering |
| `find_peaks()` | `_peak_finding.py` | 7 | Find local maxima in 1-D signal |
| `decimate()` | `_signaltools.py` | 7 | Downsample after anti-alias filtering |

### Additional Key APIs (by degree rank)

| API | Type | Description |
|-----|------|-------------|
| `welch()` | function | Power spectral density via Welch's method |
| `spectrogram()` | function | Time-frequency spectrogram |
| `correlate()` | function | N-dimensional cross-correlation |
| `butter()` | function | Butterworth filter design |
| `cheby1()` | function | Chebyshev type I filter design |
| `cheby2()` | function | Chebyshev type II filter design |
| `ellip()` | function | Elliptic (Cauer) filter design |
| `firwin()` | function | FIR filter design with window method |
| `freqz()` | function | Frequency response of digital filter |
| `sosfilt()` | function | Second-order sections filtering |
| `medfilt()` | function | Median filter (1-D) |
| `detrend()` | function | Remove linear trend from data |
| `hilbert()` | function | Hilbert transform / analytic signal |
| `resample()` | function | Resample via Fourier method |
| `impulse()` | function | Impulse response of LTI system |
| `step()` | function | Step response of LTI system |
| `lsim()` | function | Simulate LTI system output for input signal |
| `oaconvolve()` | function | Overlap-add convolution for large arrays |
| `normalize()` | function | Normalize filter numerator/denominator |
| `kaiser()` | function | Kaiser window for FIR design |
| `CZT` | class | Chirp Z-transform |
| `ZoomFFT` | class | Zoom FFT for narrowband analysis |

## Common Patterns

### Filter Design and Application
```python
from scipy.signal import butter, filtfilt, sosfilt, lfilter
import numpy as np

# Butterworth low-pass filter (order 4, cutoff 0.1 * Nyquist)
b, a = butter(4, 0.1, btype='low')
filtered = filtfilt(b, a, signal)  # zero-phase (forward + backward)

# Second-order sections (numerically stable for high orders)
sos = butter(4, 0.1, btype='low', output='sos')
filtered = sosfilt(sos, signal)

# High-pass filter
b, a = butter(4, 0.01, btype='high')
highpass = filtfilt(b, a, signal)

# Band-pass filter
b, a = butter(4, [0.01, 0.1], btype='band')
bandpass = filtfilt(b, a, signal)
```

### Spectral Analysis
```python
from scipy.signal import welch, spectrogram, periodogram

fs = 1000  # sampling frequency

# Power spectral density (Welch)
f, Pxx = welch(signal, fs, nperseg=256, noverlap=128)

# Spectrogram
f, t, Sxx = spectrogram(signal, fs, nperseg=256, noverlap=200)

# Short-time FFT (preferred for modern workflows)
from scipy.signal import ShortTimeFFT
SFT = ShortTimeFFT.from_window('hann', fs, 256, 200)
Sx = SFT.spectrogram(signal)  # complex STFT
```

### Convolution and Correlation
```python
from scipy.signal import convolve, correlate, oaconvolve

# Linear convolution
y = convolve(signal, kernel, mode='same')

# Cross-correlation for lag detection
corr = correlate(signal1, signal2, mode='same')
lags = np.arange(-len(signal1)//2, len(signal1)//2)
best_lag = lags[np.argmax(corr)]
```

### Peak Finding
```python
from scipy.signal import find_peaks, peak_widths

peaks, properties = find_peaks(signal, height=0.5, distance=10, prominence=0.2)
widths = peak_widths(signal, peaks, rel_height=0.5)
```

### Detrending and Preprocessing
```python
from scipy.signal import detrend

detrended = detrend(signal)          # remove linear trend
detrended = detrend(signal, type='constant')  # remove mean only
```

### LTI System Analysis
```python
from scipy.signal import TransferFunction, StateSpace, lsim, impulse, step

sys = TransferFunction(num=[1], den=[1, 2, 1])  # 1/(s^2 + 2s + 1)
t, y = impulse(sys)
t, y_step = step(sys)
t_out, y_out, x_out = lsim(sys, U=input_signal, T=t)
```

## Pitfalls

1. **`filtfilt` doubles the effective filter order**: Forward-backward filtering squares the magnitude response. A 4th-order Butterworth with `filtfilt` becomes effectively 8th-order. Design with half the intended order if using zero-phase filtering.

2. **`butter` can be numerically unstable at high orders**: For orders > 10, use `output='sos'` (second-order sections) instead of the default `ba` output. `filtfilt` with `ba` coefficients at high order can produce NaN or wildly inaccurate results. Same applies to `cheby1`, `cheby2`, `ellip`.

3. **Frequency normalization**: All digital filter design functions expect frequencies normalized to the Nyquist frequency (half the sampling rate). `Wn=0.1` means 0.1 × (fs/2). For analog filters, pass `analog=True` and use Hz directly.

4. **`convolve(mode='same')` trims edges**: The output length matches the first input, but edges may have boundary artifacts. For full convolution output, use `mode='full'`. The `oaconvolve` variant is faster for large arrays but has the same mode semantics.

5. **`welch` averages reduce variance at the cost of resolution**: More `nperseg` → higher frequency resolution but fewer averages → higher variance. Fewer `nperseg` → lower resolution but more robust PSD estimate. For quant applications, balance `nperseg` to get at least 10 averages.

6. **`find_peaks` missing the first/last peak**: Peaks at the very edges (index 0 or -1) are not detected by default. Check `edges` manually or pad your signal with NaN values before calling.

## Cross-Library Bridges

| Bridge | Relation | Description |
|--------|----------|-------------|
| scipy.signal → numpy | `backed_by` | scipy.signal filtering and convolution operate on numpy ndarrays |
| scipy.signal.butter/filtfilt → pandas rolling | `alternative_to` | scipy IIR filters as alternative to pandas moving averages for signal smoothing |
| scipy.signal.welch → statistical analysis | `feeds` | Periodogram estimates feed into regime-detection and feature extraction pipelines |

## Verification Checklist

- [ ] `butter(4, 0.1)` returns `(b, a)` coefficient arrays
- [ ] `filtfilt(b, a, np.ones(100))` returns filtered signal of same length
- [ ] `butter(4, 0.1, output='sos')` returns SOS array (shape `(n_sections, 6)`)
- [ ] `welch(signal, fs=1000)` returns `(frequencies, Pxx)`
- [ ] `spectrogram(signal, fs=1000)` returns `(f, t, Sxx)`
- [ ] `convolve([1,2,3], [0,1,0.5], mode='same')` returns same-length output
- [ ] `find_peaks([0,1,0,2,0,3,0])[0]` returns `[1, 3, 5]`
- [ ] `detrend(np.array([1,2,3,4,5], dtype=float))` returns zero-mean series
- [ ] `TransferFunction([1], [1,2,1])` creates a valid LTI system
- [ ] `ShortTimeFFT.from_window('hann', fs=1000, nperseg=256, noverlap=200)` is constructable
