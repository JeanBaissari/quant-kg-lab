#!/usr/bin/env python3
"""Enrich QR rows with graph-truth `file:line` citations (QKG_069).

For every skill's Quick Reference rows: resolve the first-column symbol against
the owning graph's node labels, and append `source_file:source_location` into the
row's citation cell (or the row when no citation cell exists). Only rows whose
symbol resolves UNIQUELY to one code node are auto-enriched; ambiguous or
unresolved rows are reported for manual review.

Usage:
  python3 scripts/enrich_citations.py                 # dry-run (what would change)
  python3 scripts/enrich_citations.py --apply         # write
  python3 scripts/enrich_citations.py --lib numpy     # one library
"""
import sys, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
LOCK = json.load(open(ROOT / "graphs.lock"))["libraries"]

NOISE = ("tests/", "/test", "test_", "asv_bench", "benchmarks/", "bench_", "examples/",
         "r-package", "apps/", "/doc/", "docs/", ".github", "conftest", "samples/")


def node_index(lib):
    """{symbol: [(source_file, location)]} for public code nodes."""
    p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not p.exists():
        return {}
    g = json.load(open(p))
    idx = {}
    for n in g.get("nodes", []):
        sf = n.get("source_file") or ""
        if any(x in sf.lower() for x in NOISE):
            continue
        lbl = n.get("label") or ""
        sym = lbl.rstrip("()")
        if not sym or " " in sym or len(sym) > 45:
            continue
        loc = n.get("source_location") or ""
        idx.setdefault(sym, []).append((sf, loc))
    return idx


def row_symbol(line):
    m = re.match(r"^\|\s*`([A-Za-z_][A-Za-z0-9_.]*)`", line)
    return m.group(1) if m else None


def is_bridge_row(line, own_lib):
    """Cross-library bridge rows cite ANOTHER library's symbols — not own-lib
    claims. Signals: a Bridge-ish header/description, a dotted symbol whose head
    is a DIFFERENT lib, or a dotted own-lib symbol inside a bridge table."""
    if "Bridge" in line or "equivalent" in line or "wraps" in line.lower():
        return True
    sym = row_symbol(line)
    if not sym:
        return False
    if "." in sym:
        head = sym.split(".")[0]
        if head != own_lib:
            return True
        # own-lib dotted symbol (Class.attr): bridge-table only if the row
        # references another lib's symbol later in the line
        if "`" + head in line.split("|")[-1] or "backtrader." in line or "vectorbt." in line:
            return "provides_metric" in line or "backed_by" in line or "optimized_by" in line \
                or "equivalent" in line or "wraps" in line
    return False


def enrich_skill(path, idx, dry):
    text = path.read_text()
    out_lines = []
    changed = 0
    ambiguous = []
    unresolved = []
    lib = path.relative_to(SKILLS).parts[0]
    for line in text.split("\n"):
        if not line.lstrip().startswith("|"):
            out_lines.append(line)
            continue
        sym = row_symbol(line)
        if not sym:
            out_lines.append(line)
            continue
        # skip module-node rows (cite a .py file already) and separator/header rows
        if sym.endswith((".py", ".pyx", ".c")):
            out_lines.append(line)
            continue
        if set(sym) <= set("-: "):
            out_lines.append(line)
            continue
        if is_bridge_row(line, lib):
            out_lines.append(line)
            continue
        # already has a :L citation?
        if re.search(r":L\d+", line):
            out_lines.append(line)
            continue
        # qualified Class.attr → resolve to the CLASS node (attr is a member)
        resolve = sym
        if "." in sym and not is_bridge_row(line, lib):
            resolve = sym.split(".")[0]
        # already has a file citation without :L?
        has_file = re.search(r"`[^`]+\.(?:py|pyx|c)`", line)
        cands = idx.get(resolve, [])
        code = [c for c in cands if c[1] and c[0]]
        if not code:
            unresolved.append((resolve, line.strip()[:80]))
            out_lines.append(line)
            continue
        # unique by (file, location)
        uniq = {c for c in code}
        if len(uniq) > 1:
            ambiguous.append((resolve, sorted(uniq)[:4]))
            out_lines.append(line)
            continue
        sf, loc = code[0]
        loc_num = loc.lstrip("L")
        if has_file:
            # replace the bare file citation with file:line
            new = re.sub(r"`([^`]+\.(?:py|pyx|c))`", f"`{sf}:L{loc_num}`", line, count=1)
        else:
            # append a citation cell
            strip = line.rstrip("\n")
            if strip.endswith("|"):
                strip = strip[:-1].rstrip() + " | "
            new = strip + f"`{sf}:L{loc_num}` |\n"
        if new != line:
            changed += 1
            out_lines.append(new)
            continue
        out_lines.append(line)
    if changed and not dry:
        path.write_text("\n".join(out_lines))
    return changed, ambiguous, unresolved


def main():
    args = sys.argv[1:]
    dry = "--apply" not in args
    only = None
    if "--lib" in args:
        only = args[args.index("--lib") + 1]
    total_changed = 0
    amb = []
    unres = []
    for p in sorted(SKILLS.rglob("SKILL.md")):
        lib = p.relative_to(SKILLS).parts[0]
        if lib == "quant-patterns":
            continue
        if only and lib != only:
            continue
        if lib not in LOCK:
            continue
        idx = node_index(lib)
        changed, a, u = enrich_skill(p, idx, dry)
        if changed:
            print(f"{p.relative_to(ROOT)}: {changed} rows")
        total_changed += changed
        amb += a
        unres += u
    print(f"{'would change' if dry else 'changed'}: {total_changed} rows "
          f"| ambiguous: {len(amb)} | unresolved: {len(unres)}")
    if not dry:
        return 0
    for sym, cands in amb[:10]:
        print(f"  AMBIGUOUS {sym}: {cands}")
    for sym, line in unres[:10]:
        print(f"  UNRESOLVED {sym}: {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
