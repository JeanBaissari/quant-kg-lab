#!/usr/bin/env python3
"""Verify every graph-node citation in skills/ resolves in the committed graphs.

Citation convention (SKILL_SPEC §4): graph nodes are cited as backticked paths
(`core/frame.py`) or `source_file:line` (`vectorbt/utils/config.py:L12`), typically
inside Quick Reference table cells. Resolution:
  - citations are matched ONLY inside backtick spans / table rows (code fences are
    skipped, so `self.c`-style attribute chains in code blocks never match);
  - the leading "<lib>/" or "<pkg>/" segment (backtrader/, sklearn/, numpy/…) is
    stripped before suffix-matching against the owning graph's source_file values;
  - playbooks' cross-library citations resolve against the cited library's graph.
URLs and docs/scripts references are ignored. Exits 1 on any dangling citation
(CI gate, QKG_012).
"""
import sys, re, pathlib, json

ROOT = pathlib.Path(__file__).resolve().parent.parent
CITE_RE = re.compile(r"`([A-Za-z0-9_./-]+\.(?:py|c)(?::L?\d+)?)`")
SKIP = re.compile(r"^(https?://|docs/|scripts/|tests/|tools/|knowledge_graphs/)")
PKG_OF = {"scikit-learn": "sklearn", "ta-lib": "talib", "xgboost": "xgboost",
          "lightgbm": "lightgbm", "statsmodels": "statsmodels"}
NAME_OF = {v: k for k, v in PKG_OF.items()}


def graph_sources(lib):
    p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not p.exists():
        return set()
    g = json.load(open(p))
    return {n.get("source_file", "") for n in g["nodes"] if n.get("source_file")}


def lib_for_path(path):
    first = path.split("/", 1)[0]
    return NAME_OF.get(first, first)


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
        # drop fenced code blocks (attribute chains like `self.c` live there)
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for m in CITE_RE.finditer(text):
            path = m.group(1)
            bare = re.sub(r":L?\d+$", "", path)
            if SKIP.match(bare):
                continue
            if bare.startswith(("/", "../", "./")):
                continue
            own_lib = lib
            if lib == "quant-patterns" or "/" in bare and bare.split("/", 1)[0] in NAME_OF:
                own_lib = lib_for_path(bare)
            if own_lib not in sources:
                sources[own_lib] = graph_sources(own_lib)
            checked += 1
            cand = bare
            # strip a leading "<lib>/" or "<pkg>/" segment (citations are
            # module-qualified; graph source_file values are package-relative)
            if "/" in cand:
                head = cand.split("/", 1)[0]
                if head in NAME_OF or head == own_lib:
                    cand = cand.split("/", 1)[1]
            # legacy "python-package/<pkg>/" citation prefix (pre-rebuild graphs)
            if cand.startswith("python-package/"):
                cand = "/".join(cand.split("/")[2:])
            match = any(sf == cand or sf.endswith("/" + cand) for sf in sources[own_lib])
            if not match:
                dangling.append((str(p.relative_to(ROOT)), path))
    print(f"citations checked: {checked} | dangling: {len(dangling)}")
    for f, cite in dangling[:30]:
        print(f"  {f}: {cite}")
    return 1 if dangling else 0


if __name__ == "__main__":
    sys.exit(main())
