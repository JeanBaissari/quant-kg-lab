#!/usr/bin/env python3
"""API-surface probe (QKG_021 v2 / GRAPH_SPEC c6).

Diffs a library's public top-level symbols against its committed graph and
classifies every missing symbol by extraction mechanism:

  M1   Cython module         (no tree-sitter grammar -> whole module absent)
  M2a  ufunc                 (C-implemented, no Python def)
  M2b  C builtin / dispatcher(no Python def in the package)
  M2c  constant / submodule  (data or namespace, not a callable)
  M3   Python-def'd symbol   (def exists in a .py file the graph knows)

Writes docs/reference/api-surface/<lib>.md (report) + <lib>.json (data).
With --manifest: emits tools/curated/<lib>.json — one curated-node entry per
missing symbol (label, source_file, description harvested from the live API),
consumed by scripts/inject_curated_nodes.py.
With --ci: exit 1 when resolved coverage < --threshold (default 95.0%).

Usage:
  python3 scripts/api_surface_diff.py numpy
  python3 scripts/api_surface_diff.py numpy --manifest
  python3 scripts/api_surface_diff.py numpy --ci
"""
import sys, json, types, importlib, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
THRESHOLD = 95.0
IMPORT_NAME = {"scikit-learn": "sklearn", "ta-lib": "talib", "pyportfolioopt": "pypfopt"}
PKG_OF = {"scikit-learn": "sklearn", "ta-lib": "talib", "pyportfolioopt": "pypfopt",
         "imbalanced-learn": "imblearn",
         "mplfinance": "src/mplfinance",
         "catboost": "catboost/python-package/catboost",
          "arch": "arch", "alphalens": "alphalens", "pyfolio": "pyfolio",
          "riskfolio": "riskfolio", "polars": "py-polars/src/polars", "shap": "shap"}

BUILTIN_TYPES = {"builtin_function_or_method", "method_descriptor",
                 "_ArrayFunctionDispatcher", "getset_descriptor", "classmethod",
                 "staticmethod", "overload"}


def graph_labels(g):
    return {n.get("label", "") for n in g.get("nodes", [])}


def resolve(labels, sym):
    return sym in labels or f"{sym}()" in labels


def classify(obj, sym, gsrc, labels, lib):
    """Return (mechanism, defining_file_or_None)."""
    if isinstance(obj, types.ModuleType):
        return "M2c-namespace", None
    tname = type(obj).__name__
    if tname == "ufunc":
        return "M2a-ufunc", None
    if tname == "builtin_function_or_method" or tname in BUILTIN_TYPES:
        return "M2b-builtin", None
    if isinstance(obj, (bool, int, float, str, complex, bytes)) or tname.startswith("numpy.") \
            and tname not in ("numpy.ndarray", "numpy.generic"):
        return "M2c-constant", None
    mod = getattr(obj, "__module__", None)
    if isinstance(mod, str):
        modfile = _module_file(mod, lib)
        if modfile:
            if modfile in gsrc:
                return "M3-extraction-miss", modfile
            if modfile.endswith((".pyx", ".py", ".c", ".so")):
                return "M2b-cython-or-c", modfile
    return "M2b-other", None


def _module_file(modname, lib):
    try:
        m = importlib.import_module(modname)
        f = getattr(m, "__file__", None)
        if not f:
            return None
        p = pathlib.Path(f)
        parts = p.parts
        try:
            idx = parts.index("site-packages")
        except ValueError:
            return None
        rel = pathlib.Path(*parts[idx + 1:])
        if rel.suffix not in (".py", ".pyx", ".c"):
            return None
        # graphs are package-dir-relative (ADR-0006): strip the leading <lib>/
        s = str(rel)
        if "/" in s:
            head = s.split("/", 1)[0]
            if head == "numpy" or head.endswith(("-python", "lib")):
                pass
            # heuristic: strip only the package root segment (site-packages/<pkg>/...)
        parts2 = list(rel.parts)
        if len(parts2) > 1 and parts2[0] == lib:
            return str(pathlib.Path(*parts2[1:]))
        return s
    except Exception:
        return None


def ast_symbols(lib, pkg):
    """AST fallback when the library can't be imported (old quantopian-era
    packages break on py3.12, e.g. alphalens' setup.py). Walks the pinned
    clone's package dir for top-level public symbols + their docstrings."""
    import ast
    root = ROOT / "knowledge_graphs" / lib / "repo" / pkg
    if not root.is_dir():
        return None
    out = []
    for p in sorted(root.rglob("*.py")):
        rel = str(p.relative_to(root))
        if rel.startswith("tests") or "/tests/" in rel or p.name.startswith("test_"):
            continue
        try:
            tree = ast.parse(p.read_text(errors="replace"))
        except Exception:
            continue
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) \
                    and not node.name.startswith("_"):
                doc = ast.get_docstring(node) or ""
                out.append({"symbol": node.name,
                            "kind": "class" if isinstance(node, ast.ClassDef) else "func",
                            "description": doc.strip().split("\n")[0][:220] if doc else "",
                            "source_file": str(rel)})
    return out


def load_graph(lib):
    p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    return json.load(open(p)) if p.exists() else None


def main():
    argv = sys.argv[1:]
    if not argv:
        sys.exit(__doc__)
    lib = argv[0]
    manifest = "--manifest" in argv
    ci = "--ci" in argv
    threshold = THRESHOLD
    if "--threshold" in argv:
        threshold = float(argv[argv.index("--threshold") + 1])
    g = load_graph(lib)
    if g is None:
        sys.exit(f"no graph for {lib}")
    labels = graph_labels(g)
    gsrc = {n.get("source_file", "") for n in g["nodes"]}
    pkg = PKG_OF.get(lib, lib)
    ast_syms = None
    def _obj_of(s, mod=None):
        return getattr(mod, s, None) if mod is not None else None
    try:
        mod = importlib.import_module(IMPORT_NAME.get(lib, lib))
        symbols = [s for s in dir(mod) if not s.startswith("_")]
    except Exception:
        mod = None
        ast_syms = ast_symbols(lib, pkg)
        if ast_syms is None:
            sys.exit(f"{lib}: cannot import (venv needed) and no pinned clone for AST fallback")
        symbols = [s["symbol"] for s in ast_syms]
    missing, present = [], 0
    for s in symbols:
        if resolve(labels, s):
            present += 1
            continue
        obj = _obj_of(s, mod)
        if obj is not None:
            mech, src = classify(obj, s, gsrc, labels, lib)
            doc = getattr(obj, "__doc__", None) or ""
        else:
            info = next((a for a in ast_syms if a["symbol"] == s), {})
            mech = "M2b-unimportable" + ("-class" if info.get("kind") == "class" else "")
            src = info.get("source_file")
            doc = info.get("description", "")
        missing.append({"symbol": s, "mechanism": mech, "source_file": src,
                        "description": _desc(doc, s, obj)})
    coverage = 100.0 * present / len(symbols) if symbols else 100.0
    by_mech = {}
    for m in missing:
        by_mech.setdefault(m["mechanism"], []).append(m["symbol"])
    outdir = ROOT / "docs" / "reference" / "api-surface"
    outdir.mkdir(parents=True, exist_ok=True)
    data = {"lib": lib, "total": len(symbols), "present": present,
            "missing": len(missing), "coverage": round(coverage, 2),
            "by_mechanism": {k: len(v) for k, v in sorted(by_mech.items())},
            "generated": "2026-08-12"}
    (outdir / f"{lib}.json").write_text(json.dumps(data, indent=2) + "\n")
    rows = "\n".join(
        f"| {m['symbol']} | {m['mechanism']} | {m['source_file'] or '—'} |" for m in missing)
    body = (f"<!-- generated by scripts/api_surface_diff.py — do not edit; regenerate to update -->\n\n"
            f"# API-surface — {lib}\n\n"
            f"Public top-level symbols: {data['total']} · present in graph: {data['present']} "
            f"· **coverage {data['coverage']:.1f}%** (target ≥{threshold:g}%)\n\n"
            f"| symbol | mechanism | defining source |\n|---|---|---|\n{rows}\n")
    (outdir / f"{lib}.md").write_text(body)
    print(f"{lib}: coverage {coverage:.1f}% ({present}/{len(symbols)}); "
          f"missing {len(missing)}: " + ", ".join(f"{k}={v}" for k, v in sorted(by_mech.items())))
    if manifest:
        curated = []
        for m in missing:
            obj = getattr(mod, m["symbol"], None)
            curated.append({
                "label": _label(m["symbol"], obj, m["mechanism"]),
                "source_file": m["source_file"] or "__init__.py",
                "description": m["description"],
            })
        mdir = ROOT / "tools" / "curated"
        mdir.mkdir(parents=True, exist_ok=True)
        mp = mdir / f"{lib}.json"
        mp.write_text(json.dumps({"library": lib, "symbols": curated}, indent=2) + "\n")
        print(f"manifest: {mp.relative_to(ROOT)} ({len(curated)} entries)")
    if ci and coverage < threshold:
        sys.exit(1)


def _desc(doc, sym, obj):
    d = (doc or "").strip().split("\n")[0] if doc else ""
    d = d.strip().strip(".") + "." if d and not d.endswith(".") else d
    if not d or len(d) < 12:
        d = f"Public NumPy API symbol `np.{sym}` (C-implemented or namespace; see docs)."
    return d[:220]


def _label(sym, obj, mech=""):
    if mech.startswith("M2b-unimportable-class"):
        return sym
    if mech.startswith("M2b-unimportable"):
        return f"{sym}()"
    if isinstance(obj, type):
        return sym                      # classes/types are cited bare
    if callable(obj):
        return f"{sym}()"
    return sym                          # constants / namespaces are cited bare


if __name__ == "__main__":
    main()
