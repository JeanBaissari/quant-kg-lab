#!/usr/bin/env python3
"""Add pin-version truth to every skill frontmatter (QKG_071).

For each library skill: writes `target_version` (nearest released version to
the pinned commit) + `upstream_status` (current/stale/dead) into frontmatter,
and appends a `## Version Note` banner when the pin is an unreleased dev
commit or the upstream is dead — so consumers know exactly which version a
skill describes.

The mapping is QKG_071's 28-pin audit (2026-08-16): 21 current, 2 stale
(quantstats, ta), 5 dead (backtrader, alphalens, pyfolio, empyrical,
mplfinance); only 5 pins are exact release tags, 23 are untagged dev commits.

Usage:
  python3 scripts/apply_pin_versions.py           # dry-run
  python3 scripts/apply_pin_versions.py --apply   # write
"""
import sys, json, pathlib, re
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOCK = json.load(open(ROOT / "graphs.lock"))["libraries"]

# lib -> (target_version, released?) from the QKG_071 audit
TARGET = {
    "numpy": ("2.5.1 (dev: after 2.5.1, before 2.5.2)", False),
    "scipy": ("1.18.0 (dev: after 1.18.0)", False),
    "pandas": ("3.0.5 (dev: after 3.0.5)", False),
    "scikit-learn": ("1.9.0 (dev: after 1.9.0)", False),
    "optuna": ("4.9.0 (dev: after 4.9.0)", False),
    "vectorbt": ("1.1.0 (dev: after 1.1.0)", False),
    "backtrader": ("1.9.78.123 (untagged, on release day)", False),
    "ta-lib": ("0.7.1 (released tag v0.7.1)", True),
    "xgboost": ("3.3.0 (dev: after 3.3.0, before 3.4.0)", False),
    "lightgbm": ("4.7.0 (dev: after 4.7.0)", False),
    "statsmodels": ("0.14.6 (dev: after 0.14.6)", False),
    "cvxpy": ("1.9.2 (dev: after 1.9.2)", False),
    "pyportfolioopt": ("1.6.0 (dev: after 1.6.0)", False),
    "arch": ("8.0.0 (dev: after 8.0.0)", False),
    "alphalens": ("0.4.0 (released tag v0.4.0)", True),
    "pyfolio": ("0.9.2 (dev: after 0.9.2)", False),
    "riskfolio": ("7.3.0 (dev: after 7.3.0)", False),
    "shap": ("0.52.0 (dev: after 0.52.0)", False),
    "polars": ("1.43.2 (dev: after 1.43.2)", False),
    "empyrical": ("0.5.5 (dev: after 0.5.5)", False),
    "quantstats": ("0.0.81 (released tag v0.0.81)", True),
    "yfinance": ("1.6.0 (released tag 1.6.0)", True),
    "imbalanced-learn": ("0.14.2 (released tag 0.14.2)", True),
    "pymc": ("6.3.0 (dev: after 6.3.0, before 6.3.1)", False),
    "mplfinance": ("0.12.10b0 (beta; dev after)", False),
    "catboost": ("1.2.10 (dev: after 1.2.10)", False),
    "ta": ("0.11.0 (dev: after 0.11.0)", False),
    "darts": ("0.46.1 (dev: after 0.46.1)", False),
}


def banner(lib):
    st = LOCK.get(lib, {}).get("upstream_status")
    ver, released = TARGET.get(lib, ("?", False))
    if st == "dead":
        return (f"## Version Note\n\n"
                f"> ⚠️ **Upstream is frozen** (no commits since the pin). This skill "
                f"describes `{lib}` at its pinned commit — an abandoned release line. "
                f"Target version: {ver}. Verify against your installed version before use.\n")
    if not released:
        return (f"## Version Note\n\n"
                f"> ⚠️ **Pin is an unreleased dev commit.** This skill describes `{lib}` "
                f"ahead of the latest PyPI release ({ver}). Some APIs may not exist in "
                f"your installed version.\n")
    return ""


def main():
    apply = "--apply" in sys.argv[1:]
    changed = 0
    for p in sorted((ROOT / "skills").rglob("SKILL.md")):
        if "quant-patterns" in p.parts:
            continue
        text = p.read_text()
        fm = text.split("---", 2)
        if len(fm) < 3:
            continue
        meta = yaml.safe_load(fm[1]) or {}
        lib = (p.relative_to(ROOT / "skills").parts or [""])[0]
        if lib not in TARGET:
            continue
        ver, _ = TARGET[lib]
        st = LOCK.get(lib, {}).get("upstream_status", "current")
        body = fm[2]
        meta["target_version"] = ver
        meta["upstream_status"] = st
        new_fm = "---\n" + yaml.safe_dump(meta, sort_keys=False, default_flow_style=False).rstrip() + "\n---"
        # banner: replace any existing Version Note, else insert after the
        # `# <title>` heading (the body's first section) — never before it
        b = banner(lib)
        if b:
            if "## Version Note" in body:
                # replace the banner + any trailing blank lines with the fresh
                # banner + exactly one blank line before the next section
                body = re.sub(r"## Version Note.*?(?=^# |^## )",
                              b.rstrip() + "\n\n", body, flags=re.S | re.M)
            else:
                m = re.match(r"^(# .*?\n\n)", body, flags=re.S)
                if m:
                    # insert banner between the (possibly blank) prefix and the title
                    body = body[:m.start()].rstrip("\n") + "\n\n" \
                        + b.rstrip() + "\n\n" + m.group(1) + body[m.end():]
                else:
                    body = b.rstrip() + "\n\n" + body.lstrip("\n")
        new = new_fm.rstrip() + "\n\n" + body.lstrip("\n")
        if new != text:
            print(f"{p.relative_to(ROOT)}: target={ver} status={st}")
            if apply:
                p.write_text(new)
            changed += 1
    print(f"{'would change' if not apply else 'wrote'}: {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
