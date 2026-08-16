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

--require-complete <lib> (QKG_021 v2): additionally, every Quick Reference table
row's API symbol must RESOLVE — in the owning graph's node labels, the curated
manifest (tools/curated/<lib>.json), or the manifest's explicit exclusions.
This closes the systemic hole where an uncited gap (e.g. `arange`) was
invisible to every gate.
"""
import sys, re, pathlib, json

ROOT = pathlib.Path(__file__).resolve().parent.parent
CITE_RE = re.compile(r"`([A-Za-z0-9_./-]+\.(?:py|c)(?::L?\d+)?)`")
# unbackticked file:line spans inside QR rows (ta-lib `_ta_lib.c:L26643`, sklearn
# `decomposition/_fastica.py:L1`, …) — same shape, no backticks (QKG_033)
ANY_CITE_RE = re.compile(r"([A-Za-z0-9_./-]+\.(?:py|c)(?::L?\d+)?)")
SKIP = re.compile(r"^(https?://|docs/|scripts/|tests/|tools/|knowledge_graphs/)")
PKG_OF = {"scikit-learn": "sklearn", "ta-lib": "talib", "xgboost": "xgboost",
          "lightgbm": "lightgbm", "statsmodels": "statsmodels"}
NAME_OF = {v: k for k, v in PKG_OF.items()}
SYM_RE = re.compile(r"`([A-Za-z_][A-Za-z0-9_.]*)`")


def graph_sources(lib):
    p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not p.exists():
        return set()
    g = json.load(open(p))
    return {n.get("source_file", "") for n in g["nodes"] if n.get("source_file")}


def graph_lines(lib):
    """{source_file: set(source_location ints)} — for line-aware citation checks
    (QKG_069). source_location is the node's definition line."""
    p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not p.exists():
        return {}
    g = json.load(open(p))
    out = {}
    for n in g["nodes"]:
        sf = n.get("source_file")
        loc = n.get("source_location") or ""
        if not sf:
            continue
        m = re.match(r"L(\d+)", loc)
        if m:
            out.setdefault(sf, set()).add(int(m.group(1)))
    return out


def graph_labels(lib):
    p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not p.exists():
        return set()
    g = json.load(open(p))
    return {n.get("label", "") for n in g["nodes"]}


def manifest_labels(lib):
    p = ROOT / "tools" / "curated" / f"{lib}.json"
    if not p.exists():
        return set(), set()
    m = json.load(open(p))
    return ({s["label"] for s in m.get("symbols", [])},
            set(m.get("exclusions", [])))


def _strip_prefix(bare, lib):
    """Strip a leading '<lib>/' or '<pkg>/' segment (citations are module-qualified;
    graph source_file values are package-relative) + the legacy python-package/ prefix."""
    if "/" in bare:
        head = bare.split("/", 1)[0]
        if head in NAME_OF or head == lib:
            bare = bare.split("/", 1)[1]
    if bare.startswith("python-package/"):
        bare = "/".join(bare.split("/")[2:])
    return bare


def _file_cited(row, gsrc, lib):
    """A QR row is file-cited when it carries a source-file span that resolves in the
    owning graph — backticked or not (QKG_033: ta-lib/sklearn/optuna/xgboost/lightgbm
    rows cite unbackticked `file:line`; vectorbt rows cite backticked `<lib>/file.py`)."""
    for span in ANY_CITE_RE.findall(row):
        bare = _strip_prefix(re.sub(r":L?\d+$", "", span), lib)
        if bare in gsrc or any(sf.endswith("/" + bare) for sf in gsrc):
            return True
    return False


def lib_for_path(path):
    first = path.split("/", 1)[0]
    return NAME_OF.get(first, first)


def _lock_libs():
    p = ROOT / "graphs.lock"
    return json.load(open(p))["libraries"] if p.exists() else {}


def check_complete(lib, labels, cur, excl):
    """Every QR-row symbol of the lib's skills must resolve — as a node label,
    a curated entry, an explicit exclusion, OR via a resolvable source-file
    citation in the same row (method rows, e.g. `group_by` → lazyframe/group_by.py).
    Returns failures."""
    gsrc = graph_sources(lib)
    bad = []
    for p in sorted((ROOT / "skills" / lib).rglob("SKILL.md")):
        text = p.read_text()
        for section in re.findall(r"^## Quick Reference.*?(?=^## |\Z)", text, re.S | re.M):
            for line in section.split("\n"):
                line = line.strip()
                if not line.startswith("|"):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if not cells or set(cells[0]) <= set("-: "):
                    continue
                m = SYM_RE.match(cells[0])
                if not m:
                    continue
                full = m.group(1)
                if full.endswith((".py", ".pyx", ".c")):
                    continue  # module-node cells (e.g. `plotting.py`), not API symbols
                sym = full.split(".")[-1].split("(")[0]
                if not sym:
                    continue
                ok = (sym in labels or f"{sym}()" in labels
                      or sym in cur or f"{sym}()" in cur
                      or sym in excl or f"{sym}()" in excl)
                if not ok:
                    if _file_cited(line, gsrc, lib):
                        continue
                    bad.append((str(p.relative_to(ROOT)), sym, cells[0]))
    return bad


def main():
    a = sys.argv[1:]
    libs = [x for x in a if not x.startswith("-")] or None
    require = None
    require_lines = "--require-lines" in a
    if "--require-complete" in a:
        require = a[a.index("--require-complete") + 1]
    sources = {}
    linemaps = {}
    dangling = []
    checked = 0
    bare_rows = 0
    line_mismatch = []
    for p in sorted((ROOT / "skills").rglob("SKILL.md")):
        parts = p.relative_to(ROOT / "skills").parts
        lib = parts[0]
        if lib == "quant-patterns":
            continue  # playbooks: prose cross-library references, skipped like enrich_citations.py
        if libs and lib not in libs:
            continue
        text = p.read_text()
        # drop fenced code blocks (attribute chains like `self.c` live there)
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for m in CITE_RE.finditer(text):
            path = m.group(1)
            bare = re.sub(r":L?\d+$", "", path)
            line_no = None
            lm = re.search(r":L(\d+)$", path)
            if lm:
                line_no = int(lm.group(1))
            if SKIP.match(bare):
                continue
            if bare.startswith(("/", "../", "./")):
                continue
            own_lib = lib
            if lib == "quant-patterns" or "/" in bare and bare.split("/", 1)[0] in NAME_OF:
                own_lib = lib_for_path(bare)
            if own_lib not in sources:
                sources[own_lib] = graph_sources(own_lib)
                linemaps[own_lib] = graph_lines(own_lib)
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
                continue
            # QKG_069: line-aware — a `:L<n>` citation must hit a node's source_location
            if line_no is not None:
                ok_line = any(
                    line_no in lines for sf, lines in linemaps[own_lib].items()
                    if sf == cand or sf.endswith("/" + cand))
                if not ok_line:
                    line_mismatch.append((str(p.relative_to(ROOT)), path))
            elif require_lines:
                bare_rows += 1
                dangling.append((str(p.relative_to(ROOT)), f"{path} (no :L line — QKG_069)"))
    print(f"citations checked: {checked} | dangling: {len(dangling)}"
          + (f" | line-mismatch: {len(line_mismatch)}" if line_mismatch else ""))
    for f, cite in dangling[:30]:
        print(f"  {f}: {cite}")
    for f, cite in line_mismatch[:15]:
        print(f"  LINE {f}: {cite}")
    incomplete = 0
    require_results = {}
    if require:
        if not (ROOT / "skills" / require).is_dir():
            print(f"unknown library: {require}")
            return 1
        labels = graph_labels(require)
        cur, excl = manifest_labels(require)
        bad = check_complete(require, labels, cur, excl)
        incomplete = len(bad)
        require_results[require] = incomplete
        print(f"complete check ({require}): QR rows unresolved: {incomplete}")
        for f, sym, cell in bad[:30]:
            print(f"  {f}: {cell!r} ({sym})")
    if not require:
        for lib in sorted(_lock_libs()):
            bad = check_complete(lib, graph_labels(lib), *manifest_labels(lib))
            if bad:
                require_results[lib] = len(bad)
    # QKG_051: persist the citation evidence — timestamped, SHA-stamped, gated.
    import subprocess as _sp, datetime as _dt
    sha = ""
    try:
        sha = _sp.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
                      capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:
        pass
    report = {
        "generated": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "git_sha": sha,
        "checked": checked,
        "dangling": len(dangling),
        "require_complete": require_results,
        "pass": len(dangling) == 0 and not require_results,
    }
    (ROOT / "docs" / "reference").mkdir(parents=True, exist_ok=True)
    (ROOT / "docs" / "reference" / "citations-report.json").write_text(
        json.dumps(report, indent=2) + "\n")
    return 1 if (dangling or incomplete or line_mismatch) else 0


if __name__ == "__main__":
    sys.exit(main())
