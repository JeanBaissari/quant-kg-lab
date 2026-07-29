---
name: vectorbt-core
description: vectorbt Core — Config, ArrayWrapper, Wrapping, Accessor system, indexing, type system, and data infrastructure. Extracted from the vectorbt knowledge graph (5,411 nodes, 13,588 edges).
version: 0.1.0
author: quant-kg-lab
license: MIT
source_repo: polakowo/vectorbt
graph_hash: d545b89580e72e30
extraction_date: 2026-07-29
graph_stats:
  nodes: 5411
  edges: 13588
  description_coverage: "100%"
  community_count: 395
  top_communities:
    - {id: 0, label: "Config/Drawdowns", nodes: 208}
    - {id: 1, label: "Wrapping/Builders", nodes: 197}
    - {id: 2, label: "ArrayWrapper/MappedArray", nodes: 178}
    - {id: 3, label: "Accessor System", nodes: 170}
---

# vectorbt Core (`vectorbt.base`, `vectorbt.utils`)

The foundational layer of vectorbt. Every vectorbt object wraps a pandas DataFrame/Series through `ArrayWrapper` and extends behavior via the `Wrapping` → `Accessor` pattern. Configuration flows top-down from `Config` through `Configured`, enabling global defaults that cascade to every component.

## Quick Reference

| Class / Component | Source File | Purpose | Key Params |
|-------------------|-------------|---------|------------|
| `Config` | `vectorbt/utils/config.py` | Global configuration singleton (merged dicts) | `frozen`, `readonly`, nested keys |
| `Configured` | `vectorbt/utils/config.py` | Mixin that reads config by class hierarchy | `options` attribute |
| `ArrayWrapper` | `vectorbt/base/array_wrapper.py` | Uniform pandas wrapper for 1D/2D data | `wrap`, `freq`, `group_by` |
| `Wrapping` | `vectorbt/base/array_wrapper.py` | Base class linking an object to an ArrayWrapper | `.wrapper` property |
| `BaseAccessor` | `vectorbt/base/accessors.py` | pandas accessor base (`.vbt` namespace) | registered via `@register_accessor` |
| `BaseSRAccessor` | `vectorbt/base/accessors.py` | Series-specific `.vbt` behavior | `_obj` (Series) |
| `BaseDFAccessor` | `vectorbt/base/accessors.py` | DataFrame-specific `.vbt` behavior | `_obj` (DataFrame) |
| `GenericAccessor` | `vectorbt/generic/accessors.py` | Accessor for generic (non-specialized) objects | wraps any DataFrame/Series |
| `RustSupport` | `vectorbt/_engine.py` | Rust execution engine adapter | `engine` parameter |
| `ColumnGrouper` | `vectorbt/base/column_grouper.py` | Column grouping/selection logic | `group_by`, `grouped` stacks |
| `PandasIndexer` | `vectorbt/base/indexing.py` | Multi-level pandas indexing helper | `idx_arr`, `idxs` |
| `RepEval` | `vectorbt/utils/template.py` | Template string evaluation with deferred resolution | `context`, recursive eval |

## Key Methods (by degree centrality in knowledge graph)

| Method / Attribute | Prevalence | Description |
|--------------------|------------|-------------|
| `ArrayWrapper.wrap()` | 530 edges | Wrap array-like input, handling index/freq/columns |
| `ArrayWrapper.index` | core attr | Get datetime index |
| `ArrayWrapper.columns` | core attr | Get column labels |
| `ArrayWrapper.shape` | core attr | Get (rows, cols) dimensions |
| `Wrapping.wrapper` | 422 edges | Return associated ArrayWrapper |
| `Config.__getitem__` | 575 edges | Config key lookup with freeze/readonly guards |
| `Configured.__init__` | 216 edges | Apply config defaults at construction |
| `BaseAccessor.obj` | 149 edges | Return underlying pandas object |
| `ColumnGrouper.group_by` | 90 edges | Register group labels for columns |
| `PandasIndexer.iloc` | 39 edges | Integer-location based indexing |

## Architecture Overview

```
Config (global, hierarchical defaults)
  └─ Configured (mixin, reads Config per class hierarchy)
       └─ Wrapping (has .wrapper → ArrayWrapper)
            ├─ ArrayWrapper (uniform pandas wrapping)
            │    ├─ .index → DatetimeIndex
            │    ├─ .columns → Index
            │    ├─ .shape → (rows, cols)
            │    ├─ .freq → timedelta or None
            │    └─ .group_by → group labels
            │
            ├─ ColumnGrouper (column grouping)
            │    ├─ group_by, allow_enable, allow_disable
            │    └─ PandasIndexer (2-level IndexSlice)
            │
            └─ Accessor System (pandas .vbt extension)
                 ├─ BaseAccessor → BaseSRAccessor / BaseDFAccessor
                 ├─ GenericAccessor (catch-all)
                 └─ Specialized: SignalsAccessor, ReturnsAccessor, ...
```

## Common Patterns

### Pattern 1: Configure global defaults
```python
import vectorbt as vbt

vbt.settings.wrapping['column_only_select'] = True
vbt.settings.portfolio['init_cash'] = 10000.0

# All subsequently created objects inherit these defaults
```

### Pattern 2: Wrap any data through ArrayWrapper
```python
import vectorbt as vbt
import pandas as pd

price = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
wrapper = vbt.ArrayWrapper.wrap(price, freq='D')
# wrapper.index, wrapper.columns, wrapper.shape now available
```

### Pattern 3: Accessor chain (`.vbt` namespace)
```python
import vectorbt as vbt
import pandas as pd

df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
# Every DataFrame/Series gets .vbt accessor automatically
returns = df.vbt.to_returns()          # via GenericAccessor
stats = df.vbt.stats()                 # StatsBuilderMixin
```

### Pattern 4: Column grouping
```python
import vectorbt as vbt

# Group columns by prefix/suffix for aggregate operations
price = vbt.YFData.download(['AAPL', 'MSFT', 'GOOGL']).get('Close')
price.vbt.group_by = [0, 0, 1]  # AAPL+MSFT in group 0, GOOGL in group 1
```

## Pitfalls

1. **Frozen config after first access**: Once `Config` is accessed as a dict, it freezes to prevent mutation during computation. Set all configs before calling any vectorbt method or use `vbt.settings.set_credentials()` / `vbt.settings.wrapping` before any `.vbt` access.

2. **Accessor registration is automatic but implicit**: `import vectorbt as vbt` registers `.vbt` on all pandas objects via `@register_accessor`. If you import vectorbt submodules individually, the accessor may not register. Always `import vectorbt as vbt` at module level.

3. **ArrayWrapper copies on non-ndarray input**: `ArrayWrapper.wrap()` may copy the underlying data when wrapping DataFrames — for large datasets prefer passing ndarray with explicit index/columns.

4. **Wrapping.wrapper may be None**: Objects that inherit `Wrapping` can have `.wrapper = None` before data is set. Always check or use the property pattern that lazy-initializes.

5. **ColumnGrouper and PandasIndexer interplay**: When using `group_by` with multi-level columns, `PandasIndexer` creates a 2-level index. Operations that flatten the index lose group information — re-apply `group_by` after reshape.

6. **Config key typos are silent**: Accessing `vbt.settings.wrapping['typo']` creates the key silently. Use `Config.frozen = True` during production code to surface typos.

7. **Mixin order matters**: `Configured` must come before other mixins in class definition (`class MyClass(Configured, OtherMixin)`) or config resolution breaks.

## Cross-Library Bridges

| Source | Target | Relationship | Description |
|--------|--------|-------------|-------------|
| `vectorbt.ArrayWrapper` | `pandas.DataFrame` | wraps | vectorbt wraps pandas DataFrames uniformly |
| `vectorbt.Config` | `optuna.Study` | parameterizes | HPO experiments tune vectorbt config via optuna |
| `vectorbt.Accessor` | `ta-lib.RSI` | consumes | indicator values flow into vectorbt accessor pipeline |
| `vectorbt.Wrapping` | `backtrader.DataFeed` | parallels | vectorbt's wrap + bt's feed both normalize OHLCV data |

## Verification Checklist

- [ ] `import vectorbt as vbt` works and `.vbt` accessor registered on pd.DataFrame
- [ ] `vbt.settings.wrapping` accessible before any operations
- [ ] `vbt.ArrayWrapper.wrap(df, freq='D')` returns valid wrapper with .index, .columns, .shape
- [ ] Column grouping via `.group_by` preserved through pipeline operations
- [ ] Config cascade: set `vbt.settings.portfolio.init_cash = 20000` → `Portfolio.from_signals()` uses it

## Graph Provenance

- Knowledge graph: vectorbt, 5,411 nodes, 13,588 edges, 395 communities
- Extraction: AST-only via graphify, 100% nodes described
- Core communities: 0 (Config), 1 (Wrapping/Builders), 2 (ArrayWrapper), 3 (Accessors), 8 (Indexing), 15 (Configured/Documented), 17 (RustSupport)
