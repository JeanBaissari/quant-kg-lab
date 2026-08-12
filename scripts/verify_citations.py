#!/usr/bin/env python3
"""Verify every graph-node citation in skills/ resolves in the committed graphs.

A citation is any backticked or plain path containing ".py"/".c" found in a
SKILL.md (e.g. `core/frame.py`, `vectorbt/utils/config.py:L12`). Resolution:
suffix-match against the owning library's graph.json source_file values (paths
are repo-relative; optional :L<line> suffix stripped for the path check).
Playbooks are included (their citations are cross-library). URLs and docs/
references are ignored. Exits 1 on any dangling citation (CI gate, QKG_012).
"""
import sys, re, pathlib, json

ROOT = pathlib.Path(__file__).resolve().parent.parent
CITE_RE = re.compile(r"([A-Za-z0-9_./-]+\.(?:py|c)(?::L?\d+)?)")
SKIP = re.compile(r"^(https?://|docs/|scripts/|tests/|tools/|knowledge_graphs/)")
LIB_DIRS = {"scikit-learn": "sklearn", "ta-lib": "talib", "xgboost": "xgboost",
            "lightgbm": "lightgbm", "statsmodels": "statsmodels"}


def graph_sources(lib):
    p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not p.exists():
        return set()
    g = json.load(open(p))
    return {n.get("source_file", "") for n in g["nodes"] if n.get("source_file")}


def lib_for_path(path):
    first = path.split("/", 1)[0]
    for lib, pkg in LIB_DIRS.items():
        if first == pkg:
            return lib
    return first if first in LIB_DIRS else first


def main():
    a = sys.argv[1:]
    libs = [x for x in a if not x.startswith("-")] or None
    sources = {}
    dangling = []
    checked = 0
    for p in sorted((ROOT / "skills").rglob("SKILL.md")):
        parts = p.relative_to(ROOT / "skills").parts
        lib = parts[0]
        if libs and lib not in libs:
            continue
        text = p.read_text()
        for m in CITE_RE.finditer(text):
            path = m.group(1)
            bare = re.sub(r":L?\d+$", "", path)
            if SKIP.match(bare):
                continue
            # keep only plausible graph-relative paths (no leading ../, no ./)
            if bare.startswith(("/", "../", "./")):
                continue
            own_lib = lib
            if lib == "quant-patterns" and "/" in bare:
                own_lib = lib_for_path(bare)
            if own_lib not in sources:
                sources[own_lib] = graph_sources(own_lib)
            checked += 1
            match = any(sf == bare or sf.endswith("/" + bare)
                        for sf in sources[own_lib])
            if not match:
                dangling.append((str(p.relative_to(ROOT)), path))
    print(f"citations checked: {checked} | dangling: {len(dangling)}")
    for f, cite in dangling[:30]:
        print(f"  {f}: {cite}")
    return 1 if dangling else 0


if __name__ == "__main__":
    sys.exit(main())
