#!/usr/bin/env python3
"""Generate CHANGELOG.md from skill version bumps.

Reads bump output from stdin (JSON array) or runs bump_skill_versions.py.
Diffs old vs new SKILL.md content to produce per-skill changelog entries.
"""
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
QKG_072_COMMIT = "6e88d7c"


def git_show(path: str, ref: str = "HEAD") -> str | None:
    try:
        return subprocess.check_output(
            ["git", "show", f"{ref}:{path}"],
            cwd=REPO, text=True, stderr=subprocess.DEVNULL,
        )
    except Exception:
        return None


def git_diff_names(commit: str) -> set[str]:
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", f"{commit}~1", commit, "--", "skills/"],
            cwd=REPO, text=True, stderr=subprocess.DEVNULL,
        )
        return {l.strip() for l in out.splitlines() if l.strip()}
    except Exception:
        return set()


def extract_table_rows(text: str) -> list[str]:
    """Extract Quick Reference table data rows."""
    rows = []
    in_table = False
    for line in text.splitlines():
        if "Quick Reference" in line:
            in_table = True
            continue
        if in_table:
            if line.startswith("## ") or (line.strip() == "" and rows):
                break
            if line.startswith("|") and "---" not in line and "Method" not in line:
                rows.append(line.strip())
    return rows


def parse_table_apis(rows: list[str]) -> set[str]:
    """Extract API names from table rows."""
    apis = set()
    for row in rows:
        cells = [c.strip() for c in row.split("|") if c.strip()]
        if cells:
            # First cell is typically the API reference
            name = re.sub(r"`|^\s*\d+\.\s*", "", cells[0]).strip()
            if name:
                apis.add(name)
    return apis


def diff_sections(old: str, new: str) -> list[str]:
    """Produce human-readable diff summary."""
    changes = []

    # Compare Quick Reference rows
    old_rows = extract_table_rows(old)
    new_rows = extract_table_rows(new)
    old_apis = parse_table_apis(old_rows)
    new_apis = parse_table_apis(new_rows)

    removed = old_apis - new_apis
    added = new_apis - old_apis
    if removed:
        changes.append(f"Removed {', '.join(sorted(removed))}")
    if added:
        changes.append(f"Added {', '.join(sorted(added))}")

    # Compare sections
    old_headings = re.findall(r"^##\s+(.+)$", old, re.MULTILINE)
    new_headings = re.findall(r"^##\s+(.+)$", new, re.MULTILINE)
    old_set = set(old_headings)
    new_set = set(new_headings)
    for h in sorted(new_set - old_set):
        changes.append(f"Added section: {h}")
    for h in sorted(old_set - new_set):
        changes.append(f"Removed section: {h}")

    # Compare Pitfalls
    old_pitfalls = len(re.findall(r"Pitfall\s+\d+", old))
    new_pitfalls = len(re.findall(r"Pitfall\s+\d+", new))
    if new_pitfalls > old_pitfalls:
        changes.append(f"Added {new_pitfalls - old_pitfalls} new Pitfall(s)")
    elif new_pitfalls < old_pitfalls:
        changes.append(f"Removed {old_pitfalls - new_pitfalls} Pitfall(s)")

    if not changes:
        # Fallback: generic line-level summary
        old_lines = set(old.splitlines())
        new_lines = set(new.splitlines())
        added_lines = len(new_lines - old_lines)
        removed_lines = len(old_lines - new_lines)
        changes.append(f"Changed {added_lines} lines added, {removed_lines} removed")

    return changes


def skill_label(path: str) -> str:
    """Convert skills/foo/bar/SKILL.md to foo/bar."""
    parts = Path(path).parts
    idx = list(parts).index("skills")
    return "/".join(parts[idx + 1:-1])


def main():
    # Read bump data from stdin (piped JSON) or run the bumper
    bumps = None
    if not sys.stdin.isatty():
        try:
            raw = sys.stdin.read().strip()
            if raw:
                bumps = json.loads(raw)
        except (json.JSONDecodeError, EOFError):
            pass

    if bumps is None:
        result = subprocess.run(
            [sys.executable, str(REPO / "scripts" / "bump_skill_versions.py")],
            capture_output=True, text=True, cwd=REPO,
        )
        if result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            sys.exit(1)
        bumps = json.loads(result.stdout)

    if not bumps:
        print("No version bumps detected.", file=sys.stderr)
        sys.exit(0)

    today = date.today().isoformat()
    qkg072_files = git_diff_names(QKG_072_COMMIT)

    # Group bumps by new version
    by_version: dict[str, list] = {}
    for b in bumps:
        by_version.setdefault(b["new_version"], []).append(b)

    lines = ["# Changelog\n"]
    for ver in sorted(by_version.keys()):
        entries = by_version[ver]
        lines.append(f"## {ver} ({today})\n")
        for b in entries:
            label = skill_label(b["path"])
            new_text = Path(REPO / b["path"]).read_text()

            # For QKG_072 skills, compare against pre-repair state
            if b["path"] in qkg072_files:
                old_text = git_show(b["path"], ref=f"{QKG_072_COMMIT}~1")
            else:
                old_text = git_show(b["path"])

            if old_text:
                diff_notes = diff_sections(old_text, new_text)
            else:
                diff_notes = ["New skill (no prior version in git)"]

            lines.append(f"### {label} ({b['old_version']} → {b['new_version']})")
            for note in diff_notes:
                lines.append(f"- {note}")
            lines.append("")

    changelog = REPO / "CHANGELOG.md"
    changelog.write_text("\n".join(lines))
    print(f"Written {changelog}", file=sys.stderr)
    print(f"{len(bumps)} skills bumped")


if __name__ == "__main__":
    main()
