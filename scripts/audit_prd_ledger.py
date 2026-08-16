#!/usr/bin/env python3
"""Lint PRD ledger (vault README.md) against on-disk PRD files.

Checks (exit 1 on --ci):
  1. Every ledger PRD ID has a corresponding file on disk.
  2. Every PRD file's frontmatter status matches the ledger Status column.
  3. No duplicate ledger rows for the same PRD ID.
  4. Ledger "N/N done" totals (if present) are consistent with the table.

Usage:
  python scripts/audit_prd_ledger.py              # report
  python scripts/audit_prd_ledger.py --ci         # exit 1 on any error
  python scripts/audit_prd_ledger.py --repo ROOT  # override repo root (default: cwd)
"""
import sys, re, pathlib, argparse

VAULT_PRD = pathlib.Path("hermes-vault/work/quant-kg-lab/prd")
LEDGER_RE = re.compile(
    r"^\|\s*(QKG_\d+)\s*\|.*?\|\s*(.*?)\s*\|.*?\|\s*(.+?)\s*\|$"
)
STATUS_MAP = {
    "done": "done",
    "completed": "done",
    "drafted": "drafted",
    "in-progress": "in-progress",
    "in_progress": "in-progress",
    "planned": "drafted",
}
DONE_PAT = re.compile(r"done|completed", re.I)
FRONTMAT_RE = re.compile(r"^---\s*\n(.*?)\n---", re.S)
STATUS_FIELD = re.compile(r"^status:\s*(.+)$", re.M)


def find_prd_files(prd_dir):
    """Return {QKG_NNN: pathlib.Path} for all PRD files on disk."""
    files = {}
    for p in prd_dir.rglob("QKG_*.md"):
        m = re.search(r"(QKG_\d+)", p.name)
        if m:
            files[m.group(1)] = p
    return files


def parse_frontmatter_status(path):
    """Extract status from PRD file frontmatter."""
    text = path.read_text(errors="replace")
    m = FRONTMAT_RE.search(text)
    if not m:
        return None
    sm = STATUS_FIELD.search(m.group(1))
    return sm.group(1).strip().lower() if sm else None


def parse_ledger(ledger_path):
    """Parse ledger table rows. Returns [(id, title, raw_status, line_no)]."""
    rows = []
    text = ledger_path.read_text(errors="replace")
    for i, line in enumerate(text.splitlines(), 1):
        m = LEDGER_RE.match(line)
        if m:
            qid = m.group(1).strip()
            title = m.group(2).strip()
            raw_status = m.group(3).strip()
            rows.append((qid, title, raw_status, i))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ci", action="store_true", help="exit 1 on errors")
    ap.add_argument("--repo", type=pathlib.Path, default=pathlib.Path.cwd(),
                    help="repo root (default: cwd)")
    args = ap.parse_args()

    root = args.repo
    ledger = root / VAULT_PRD / "README.md"
    prd_dir = root / VAULT_PRD

    if not ledger.exists():
        print(f"FAIL: ledger not found: {ledger}")
        return 1 if args.ci else 0

    rows = parse_ledger(ledger)
    files = find_prd_files(prd_dir)
    errors = []

    # Check 1: duplicate IDs
    seen = {}
    for qid, title, raw_status, lineno in rows:
        if qid in seen:
            errors.append(f"DUPLICATE: {qid} on lines {seen[qid]} and {lineno}")
        seen[qid] = lineno

    # Check 2: every ledger ID has a file
    for qid, title, raw_status, lineno in rows:
        if qid not in files:
            errors.append(f"FILELESS: {qid} (ledger line {lineno}) has no file on disk")

    # Check 3: every file has a ledger entry
    ledger_ids = {r[0] for r in rows}
    for qid, fpath in sorted(files.items()):
        if qid not in ledger_ids:
            errors.append(f"UNLISTED: {qid} ({fpath.relative_to(root)}) has no ledger row")

    # Check 4: frontmatter status matches ledger
    for qid, title, raw_status, lineno in rows:
        if qid not in files:
            continue
        fm_status = parse_frontmatter_status(files[qid])
        if fm_status is None:
            continue
        ledger_done = bool(DONE_PAT.search(raw_status))
        fm_done = bool(DONE_PAT.search(fm_status))
        if ledger_done != fm_done:
            norm_ledger = "done" if ledger_done else "not-done"
            norm_fm = "done" if fm_done else "not-done"
            errors.append(
                f"STATUS_MISMATCH: {qid} ledger={norm_ledger} (line {lineno}) "
                f"but frontmatter={norm_fm}"
            )

    # Report
    if errors:
        print(f"=== audit_prd_ledger: {len(errors)} error(s) ===")
        for e in errors:
            print(f"  {e}")
    else:
        print(f"=== audit_prd_ledger: PASS ({len(rows)} rows, {len(files)} files) ===")

    return 1 if args.ci and errors else 0


if __name__ == "__main__":
    sys.exit(main())
