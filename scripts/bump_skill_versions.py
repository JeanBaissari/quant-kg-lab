#!/usr/bin/env python3
"""Scan all SKILL.md files, compare against git HEAD, and bump versions."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO / "skills"

# Skills repaired in QKG_072 (commit 6e88d7c) — force minor bump
QKG_072_COMMIT = "6e88d7c"


def git_diff_names(commit: str) -> set[str]:
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", f"{commit}~1", commit, "--", "skills/"],
            cwd=REPO, text=True, stderr=subprocess.DEVNULL,
        )
        return {l.strip() for l in out.splitlines() if l.strip()}
    except Exception:
        return set()


def git_show(path: str) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "show", f"HEAD:{path}"],
            cwd=REPO, text=True, stderr=subprocess.DEVNULL,
        )
    except Exception:
        return None


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip("\"'")
    return fm


def bump_version(ver: str, kind: str) -> str:
    parts = ver.split(".")
    if len(parts) != 3:
        return ver
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    if kind == "minor":
        minor += 1
        patch = 0
    else:
        patch += 1
    return f"{major}.{minor}.{patch}"


def content_diff_kind(old: str, new: str) -> str | None:
    """Classify the diff between old and new skill content."""
    if old == new:
        return None

    def extract_section(text: str, heading: str) -> str:
        pattern = rf"(^|\n)(##\s+{re.escape(heading)}.*?)(?=\n##\s|\Z)"
        m = re.search(pattern, text, re.DOTALL)
        return m.group(2).strip() if m else ""

    # Check QR rows (Quick Reference table rows)
    old_qr = extract_section(old, "Quick Reference")
    new_qr = extract_section(new, "Quick Reference")
    if old_qr != new_qr:
        # Check if only citations changed (same API names, different :line refs)
        old_apis = set(re.findall(r"`(\w[\w.]*\w)`", old_qr))
        new_apis = set(re.findall(r"`(\w[\w.]*\w)`", new_qr))
        if old_apis != new_apis:
            return "minor"

    # Check for section presence changes
    old_headings = set(re.findall(r"^##\s+(.+)$", old, re.MULTILINE))
    new_headings = set(re.findall(r"^##\s+(.+)$", new, re.MULTILINE))
    if old_headings != new_headings:
        return "minor"

    # Check API surface (code references in body, not just QR)
    old_refs = set(re.findall(r"`(\w[\w.]*\w)`", old))
    new_refs = set(re.findall(r"`(\w[\w.]*\w)`", new))
    added = new_refs - old_refs
    removed = old_refs - new_refs
    if added or removed:
        return "minor"

    # Only citation/fix changes
    return "patch"


def main():
    qkg072_files = git_diff_names(QKG_072_COMMIT)

    bumped = []
    for skill_path in sorted(SKILLS_DIR.rglob("SKILL.md")):
        rel = skill_path.relative_to(REPO)
        rel_str = str(rel)
        text = skill_path.read_text()
        fm = parse_frontmatter(text)
        cur_ver = fm.get("version", "0.0.0")

        # Get old content from git HEAD
        old_text = git_show(rel_str)

        # Determine bump kind
        if rel_str in qkg072_files:
            kind = "minor"  # QKG_072 repaired skills always get minor bump
        elif old_text is None:
            continue  # new file, no history
        else:
            kind = content_diff_kind(old_text, text)

        if kind is None:
            continue

        new_ver = bump_version(cur_ver, kind)

        # Write new version into frontmatter
        new_text = text.replace(
            f"version: {cur_ver}", f"version: {new_ver}", 1
        )
        skill_path.write_text(new_text)

        bumped.append({
            "path": rel_str,
            "old_version": cur_ver,
            "new_version": new_ver,
            "bump_kind": kind,
        })

    json.dump(bumped, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
