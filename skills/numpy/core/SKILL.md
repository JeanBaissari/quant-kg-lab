---
name: numpy-core
description: "Use when working with NumPy arrays \u2014 ndarray, ufuncs, broadcasting,\
  \ indexing, dtypes, and array creation."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
source_commit: ab2199763cb17878cd8f34fcbc97106c5397f922
extraction_date: 2026-07-29
graph:
  nodes: 8306
  edges: 13483
  community_count: 619
  graph_hash: 9ea08f5479cbb7c7
tags:
- numpy
- core
related_skills: []
---

# NumPy Core (`numpy._core` / `numpy`)

The foundational array computing layer: the `ndarray` (N-dimensional homogeneous array over a contiguous C buffer, stride-based indexing), array creation, indexing/slicing, reshaping, reductions, sorting, and the dtype system. Ufuncs/broadcasting/einsum live in `numpy-ufuncs`; array persistence in `numpy-io`.

## Quick Reference

| API | Signature | Description | Graph Node |
|---|---------|-----------|----------|
| `array` | `np.array(object, dtype=None)` | Create an ndarray from array-like input | `__init__.py:L1` |
| `asarray` | `np.asarray(a, dtype=None)` | Convert to ndarray — no copy if input is already ndarray | `_core/_asarray.py:L24` |
| `arange` | `np.arange([start,] stop[, step])` | Evenly spaced values within a half-open interval | _core/src/multiarray/ctors.c:L3093 |
| `linspace` | `np.linspace(start, stop, num=50)` | Evenly spaced numbers over a closed interval | _core/function_base.py:L28 |
| `reshape` | `np.reshape(a, newshape)` | Reshape ndarray without changing data | _core/fromnumeric.py:L224 |
| `sum` | `np.sum(a, axis=None)` | Sum of array elements over given axes | _core/fromnumeric.py:L2389 |
| `mean` | `np.mean(a, axis=None)` | Arithmetic mean along specified axis | _core/fromnumeric.py:L3804 |
| `concatenate` | `np.concatenate((a1, a2, ...), axis=0)` | Join arrays along an existing axis | _core/multiarray.py:L198 |
| `sort` | `np.sort(a, axis=-1)` | Return a sorted copy of an array | _core/fromnumeric.py:L1000 |

## Architecture Overview

```
ndarray: N-dimensional, homogeneous, contiguous memory
  ├─ .shape     → tuple of dimensions
  ├─ .dtype     → data type (float64, int32, complex128, etc.)
  ├─ .strides   → bytes to step in each dimension
  ├─ .T         → transposed view (reverse axes)
  ├─ .flat      → 1-D iterator over all elements
  └─ .base      → base array (if this is a view)

ufunc: element-wise operation with broadcasting
  ├─ add, subtract, multiply, divide, power, mod
  ├─ sin, cos, exp, log, sqrt, abs
  ├─ greater, less, equal, logical_and, logical_or
  ├─ maximum, minimum, clip
  └─ .reduce(), .accumulate(), .outer(), .at()

broadcasting: implicit alignment of differently-shaped arrays
  (3,) + (2, 1) → broadcasts to (2, 3)

indexing: basic (slices, ints), advanced (integer arrays), boolean masking

dtype system: int8→float16→float32→float64→complex64→complex128
  kind codes: 'b' (bool), 'i' (int), 'u' (uint), 'f' (float), 'c' (complex),
              'S' (bytes), 'U' (unicode str), 'V' (void), 'M' (datetime), 'm' (timedelta)
```

## Array Creation

```python
import numpy as np

# From data
np.array([1, 2, 3])                          # 1-D
np.array([[1, 2], [3, 4]])                   # 2-D
np.array([1, 2, 3], dtype=np.float32)        # explicit dtype
np.asarray(existing_array_or_list)           # no-copy conversion

# Initialized arrays
np.zeros((3, 4))                              # all zeros (float64)
np.zeros(10, dtype=int)                       # integer zeros
np.zeros_like(other_array)                    # match shape and dtype
np.ones((3, 4))                               # all ones
np.ones_like(other_array)
np.empty((3, 4))                              # uninitialized (fast)
np.empty_like(other_array)
np.full((3, 4), 7.0)                         # fill with value
np.full_like(other_array, fill_value)

# Sequences
np.arange(10)                                 # 0, 1, ..., 9
np.arange(2, 10, 2)                           # 2, 4, 6, 8
np.linspace(0, 1, 5)                         # 0.0, 0.25, 0.5, 0.75, 1.0
np.logspace(0, 3, 4)                         # 1, 10, 100, 1000  (geometric)

# Grids
np.meshgrid(x, y, indexing='ij')             # coordinate matrices
np.ogrid[0:5, 0:3]                           # open grid (broadcast-friendly)
np.mgrid[0:5, 0:3]                           # dense grid

# Identity / diagonal
np.eye(3)                                     # identity matrix
np.identity(3)                                # identity (square only)
np.diag([1, 2, 3])                           # diagonal from 1-D array
np.diag(A)                                    # extract diagonal

# From functions
np.fromfunction(lambda i, j: i + j, (3, 3))
np.fromiter(iterable, dtype=float)
```

## Array Attributes & Inspection

```python
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)

a.shape          # (2, 3)
a.ndim           # 2
a.size           # 6  (total elements)
a.dtype          # dtype('float64')
a.itemsize       # 8  (bytes per element)
a.nbytes         # 48 (total bytes)
a.strides        # (24, 8)  (bytes to step in each dim)
a.T              # transpose view — shape (3, 2)
a.data           # memory buffer
a.base           # None (owns data) or base array (view)
a.flags          # memory layout flags (C_CONTIGUOUS, F_CONTIGUOUS, OWNDATA, ...)
```

## Indexing & Slicing

```python
a = np.arange(24).reshape(4, 6)

# Basic indexing (returns view)
a[0]             # first row
a[:, 0]          # first column
a[1:3]           # rows 1, 2
a[::2]           # every other row
a[:, 1:5:2]      # columns 1, 3
a[0, 0]          # scalar element

# Advanced indexing with integer arrays (returns copy)
rows = np.array([0, 2, 3])
cols = np.array([1, 4, 2])
a[rows]           # rows 0, 2, 3 (all columns)
a[:, cols]        # columns 1, 4, 2 (all rows)
a[rows[:, None], cols]  # specific (row, col) pairs via broadcasting

# Boolean masking
mask = a > 10
a[mask]           # flattened array of elements > 10
a[a > 10] = 0     # set elements > 10 to 0

# Newaxis (add dimension)
a[:, np.newaxis]           # shape (4, 1, 6)
a[np.newaxis, :]           # shape (1, 4, 6)

# Ellipsis (fill with :)
a[..., 0]         # equivalent to a[:, :, 0] for 3-D
```

## Reshaping & Manipulation

```python
a = np.arange(12)

# Reshape
np.reshape(a, (3, 4))         # returns reshaped copy if needed
a.reshape(3, 4)               # view if possible
a.reshape(-1, 1)              # infer one dimension: (12, 1)

# Resize (may repeat or truncate)
np.resize(a, (2, 5))          # may repeat elements if needed

# Flatten
a.ravel()                      # flattened view (C order by default)
a.flatten()                    # always returns a copy
a.reshape(-1)                  # equivalent to ravel() if contiguous

# Transpose / axis manipulation
np.transpose(a)                # reverse axes
a.T                            # shorthand for transpose
np.moveaxis(a, source, dest)   # move axis to new position
np.swapaxes(a, axis1, axis2)   # swap two axes
np.rollaxis(a, axis, start=0)  # roll axis backwards
np.expand_dims(a, axis=0)      # add singleton dim: shape (1, 12)
np.squeeze(a, axis=None)       # remove singleton dims

# Stacking / splitting
np.concatenate([a1, a2], axis=0)     # join along existing axis
np.stack([a1, a2], axis=0)           # join along new axis
np.vstack([a1, a2])                  # vertical stack (row-wise)
np.hstack([a1, a2])                  # horizontal stack (column-wise)
np.dstack([a1, a2])                  # depth stack (along 3rd axis)
np.column_stack([a1, a2])            # 1-D → columns
np.row_stack([a1, a2])               # = vstack
np.split(a, indices_or_sections)      # split along axis
np.array_split(a, n)                 # split, allow unequal sizes
np.tile(a, reps)                      # repeat array like tiles
np.repeat(a, repeats, axis=None)      # repeat each element
np.pad(a, pad_width, mode='constant') # pad with values

# Block construction
np.block([[A, B], [C, D]])            # assemble from nested lists
```

## Reductions & Statistics

Reductions collapse axes by applying a function:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

# Sum / Product
np.sum(a)              # 21 (all elements)
np.sum(a, axis=0)      # [5, 7, 9]  (columns)
np.sum(a, axis=1)      # [6, 15]    (rows)
np.sum(a, axis=(0, 1)) # 21
np.prod(a)             # 720
np.cumsum(a)           # cumulative sum
np.cumprod(a)          # cumulative product

# Basic statistics
np.mean(a)             # 3.5
np.mean(a, axis=0)     # [2.5, 3.5, 4.5]
np.std(a)              # population std (ddof=0)
np.std(a, ddof=1)      # sample std
np.var(a)              # variance
np.median(a)           # median
np.average(a, weights=...)  # weighted average

# Min / Max
np.min(a)              # 1
np.max(a)              # 6
np.amin(a, axis=0)     # minimum along axis
np.amax(a, axis=1)     # maximum along axis
np.argmin(a)           # index of minimum (flattened)
np.argmax(a)           # index of maximum
np.argmin(a, axis=0)   # indices of minima along columns
np.argmax(a, axis=1)   # indices of maxima along rows
np.ptp(a)              # peak-to-peak (max - min): 5

# Logical reductions
np.all(a > 0)         # True if all elements > 0
np.any(a > 5)         # True if any element > 5

# Where (conditional selection)
np.where(a > 3, a, 0) # replace elements ≤ 3 with 0
np.where(a > 3)       # return indices where condition is True

# Nonzero / count_nonzero
np.count_nonzero(a)    # number of non-zero elements
np.nonzero(a)          # indices of non-zero elements
np.flatnonzero(a)      # flat indices of non-zero elements

# Unique
np.unique(a)           # sorted unique elements
np.unique(a, return_counts=True, return_index=True)
```

## Sorting & Searching

```python
a = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# Sort
np.sort(a)                        # [1, 1, 2, 3, 4, 5, 6, 9]  (copy)
a.sort()                          # in-place sort
np.argsort(a)                     # indices that would sort: [1, 3, 6, 0, 2, 4, 7, 5]

# Partition (partial sort — k-th element at correct position)
np.partition(a, 3)                # 3 smallest, then rest unordered
np.argpartition(a, 3)             # same, returning indices

# Search
np.argmax(a), np.argmin(a)
np.searchsorted(sorted_array, values)  # insertion indices
np.where(condition)
np.flatnonzero(condition)

# Clip
np.clip(a, 2, 5)                 # clamp values to [2, 5]
```

## dtype System

The data type system defines how bytes in memory are interpreted:

```python
# Built-in dtypes
np.bool_           # True/False (1 byte)
np.int8, np.int16, np.int32, np.int64
np.uint8, np.uint16, np.uint32, np.uint64
np.float16, np.float32, np.float64, np.float128 (platform dependent)
np.complex64, np.complex128, np.complex256
np.bytes_          # fixed-length byte strings
np.str_            # fixed-length unicode strings
np.object_         # arbitrary Python objects
np.void            # raw bytes (structured types use this)
np.datetime64      # nanosecond-precision datetime
np.timedelta64     # nanosecond-precision time delta

# dtype introspection
dt = np.dtype('float64')
dt.name            # 'float64'
dt.byteorder       # '='
dt.itemsize        # 8
dt.kind            # 'f'
dt.char            # 'd'
dt.type            # numpy.float64

# Structured dtypes (compound types)
dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('score', 'f8')])
arr = np.array([('Alice', 30, 95.5), ('Bob', 25, 88.0)], dtype=dt)
arr['name']        # array(['Alice', 'Bob'])
arr['age'].mean() # 27.5

# Type promotion
np.result_type(np.int32, np.float32)  # float64
np.result_type(np.int32, np.int64)    # int64
np.can_cast(np.float64, np.int32)     # False (lossy)

# Info functions
np.iinfo(np.int32)   # integer info (min, max, bits)
np.finfo(np.float64) # float info (eps, min, max, precision)
```

## Common Patterns

```python
import numpy as np

# Vectorized computation (avoid loops)
x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x) * np.exp(-x/10)

# Boolean indexing for filtering
data = np.random.randn(1000)
outliers = data[np.abs(data) > 3]
data[np.abs(data) > 3] = 0  # clip in-place

# Axis operations for multi-dimensional data
scores = np.random.randn(100, 10)          # 100 samples, 10 features
mean_by_feature = scores.mean(axis=0)      # shape (10,)
normalized = scores - mean_by_feature      # broadcasting
normalized = scores / scores.std(axis=0)   # z-score per feature

# Fancy indexing for reordering
arr = np.arange(10)
indices = np.array([3, 7, 2, 5])
arr[indices]                                # [3, 7, 2, 5]

# Newaxis for broadcasting tricks
a = np.array([1, 2, 3])      # (3,)
b = np.array([[4], [5]])     # (2, 1)
result = a + b               # (2, 3) via broadcasting

# Sorting along multiple criteria
data = np.array([(3, 'c'), (1, 'a'), (3, 'b')], dtype=[('x', int), ('y', 'U1')])
np.sort(data, order=['x', 'y'])  # sort by x, then y
```

## Pitfalls

1. **View vs Copy confusion**: Slicing returns a **view** (shares memory). Fancy indexing returns a **copy**. Use `a.copy()` to force a copy, `np.shares_memory(a, b)` to check sharing. Modifying views silently affects the original.

2. **dtype promotion**: Operations between different dtypes follow type promotion rules (`int32 + float32 → float64`). Check `np.result_type()` when unsure. Integer division `/` returns float in Python 3; use `//` for floor division.

3. **Broadcasting errors**: When shapes don't align, you get `ValueError: operands could not be broadcast together`. Check `np.broadcast_shapes()` to debug.

4. **axis=None vs axis=0**: Axis `None` means "flatten and reduce" — very different from axis `0`. `np.sum(a)` reduces to scalar; `np.sum(a, axis=0)` reduces the first dimension.

5. **Memory layout and performance**: C-contiguous (row-major) and F-contiguous (column-major) arrays have different iteration performance. Use `a.flags['C_CONTIGUOUS']` or `np.ascontiguousarray(a)` to optimize. `einsum` with `optimize=True` finds the best contraction path.

## Cross-Library Bridges

| Source | Target | Relation | Description |
|--------|--------|----------|-------------|
| numpy.ndarray | `pandas.DataFrame` | **backed_by** | pandas DataFrame is backed by numpy ndarray for numerical storage |
| numpy.ufunc | `pandas.apply/transform` | **powers** | pandas apply/transform operations use numpy ufuncs under the hood |
| numpy.ndarray | `scipy.sparse` | **data_source** | scipy sparse matrices consume numpy arrays as input |
| numpy.ndarray | `vectorbt.ArrayWrapper` | **wrapped_by** | vectorbt ArrayWrapper wraps numpy ndarray for named column access |

- **pandas** relies on numpy for: DataFrame/Series internal storage, vectorized operations, dtype system
- **scipy** builds on numpy for: sparse matrices, signal processing FFT, optimization input/output
- **matplotlib** consumes numpy arrays for all plotting data

## Verification Checklist

- [ ] `array()` and `asarray()` correctly create ndarrays with specified dtype
- [ ] Broadcasting rules produce expected output shapes
- [ ] Basic indexing returns views; fancy indexing returns copies
- [ ] Reductions (`sum`, `mean`, `std`, `min`, `max`) handle `axis` correctly
- [ ] `argmin`/`argmax` return correct indices (flattened and per-axis)
- [ ] `reshape()` and `ravel()` return views when possible
- [ ] `concatenate`/`stack`/`split` handle axis correctly
- [ ] `sort()` returns sorted copy; `argsort()` returns index array
- [ ] `clip()` clamps values to specified range
- [ ] `einsum()` produces correct results with `optimize=True`
- [ ] ufuncs (add, multiply, sin, etc.) operate element-wise with broadcasting
- [ ] `np.seterr()` / `np.errstate()` control floating-point error behavior
- [ ] `np.save()` / `np.load()` roundtrip preserves array data exactly
- [ ] Structured dtypes allow field access by name

## Provenance

- Knowledge graph: numpy, 8094 nodes, 13271 edges, 670 communities
- God nodes: `MaskedArray` (151), `core.py:L1` (115), `fromnumeric.py:L1` (92) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ ab2199763cb1, backend opencode, description coverage 83%
