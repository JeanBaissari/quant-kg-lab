---
name: numpy-io
description: "Use when reading or writing NumPy arrays — loadtxt/savetxt/genfromtxt text I/O, save/load/savez binary .npy/.npz round-trips, and memmap for large on-disk arrays."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: numpy/numpy
source_commit: ab2199763cb17878cd8f34fcbc97106c5397f922
extraction_date: 2026-08-13
graph:
  nodes: 8306
  edges: 13483
  community_count: 670
  graph_hash: df005c66bd19581a
tags:
- numpy
- io
- loadtxt
- memmap
related_skills:
- numpy
- numpy-core
- pandas-core
- polars-io
---

# NumPy I/O

Array persistence: text formats (`loadtxt`/`savetxt`/`genfromtxt`) for interchange,
binary `.npy`/`.npz` for fast lossless round-trips, and `memmap` for arrays too large
to hold in memory.

## Quick Reference

| API | Signature | Description | Graph Node |
|-----|-----------|-------------|------------|
| `loadtxt` | `np.loadtxt(fname, delimiter=',')` | Read a text array — simple, fast, strict |
| `savetxt` | `np.savetxt(fname, X, delimiter=',')` | Write a text array with a format string |
| `genfromtxt` | `np.genfromtxt(fname, delimiter=',')` | Text read with missing-value handling |
| `save` | `np.save('x.npy', arr)` | Binary single-array save (.npy) |
| `load` | `np.load('x.npy')` | Binary load — also accepts `mmap_mode` |
| `savez` | `np.savez('x.npz', a=a, b=b)` | Uncompressed multi-array archive (.npz) |
| `savez_compressed` | `np.savez_compressed('x.npz', a=a)` | Compressed multi-array archive |
| `memmap` | `np.memmap(path, dtype, mode='r')` | Memory-mapped array — lazy on-disk access |
| `ndarray` | `np.ndarray` | The loaded array type |

## Common Patterns

- **Text interchange**: `np.loadtxt('data.csv', delimiter=',', skiprows=1)` —
  simple numeric data; `np.genfromtxt` when the file has missing values
  (`missing_values='NA'`).
- **Binary round-trip**: `np.save('arr.npy', arr)` → `np.load('arr.npy')` — the
  fastest faithful persistence; `.npz` archives multiple named arrays
  (`data['a']`, `data['b']`).
- **Compressed archives**: `np.savez_compressed` for storage-constrained artifacts —
  slower writes, smaller files.
- **Large arrays**: `np.load('big.npy', mmap_mode='r')` / `np.memmap(...)` — no full
  load; slices hit disk lazily. Ideal for factor panels too large for RAM.
- **Pipeline glue**: `loadtxt` → numpy → `savetxt`/`save` at the boundary of
  pandas/polars workflows.

## Pitfalls

- **loadtxt is strict**: missing values raise — switch to `genfromtxt` (slower) when
  the data is messy.
- **.npy vs .npz**: `save` writes one array; `savez` a dict-like archive — mixing them
  up loads the wrong shape.
- **memmap lifetime**: the file must stay open/consistent while the memmap is alive —
  deleting the backing file corrupts access.
- **Text precision**: `savetxt` default `fmt` truncates — pass `fmt='%.10f'` or
  higher when precision matters.
- **load(..., allow_pickle=False)**: the default rejects pickled objects — loading
  object arrays needs the explicit opt-in (security).

## Provenance

Graph: `knowledge_graphs/numpy/.graphify/graph.json` — 8306 nodes · 13483 edges ·
670 communities · graphify @ ab2199763c, backend opencode, description coverage ~84%.
Split from `numpy-core` (QKG_055); I/O section of the original skill.

## Verification Checklist

- [ ] `np.save`/`np.load` round-trips a small array byte-identically
- [ ] `np.loadtxt` reads a delimiter-separated text file
- [ ] QR rows cite graph-resolvable numpy nodes
