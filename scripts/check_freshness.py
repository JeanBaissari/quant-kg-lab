#!/usr/bin/env python3
"""Check if graph pins are stale vs upstream HEAD."""
import json, subprocess, sys, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent

def main():
    lock = json.load(open(ROOT / "graphs.lock"))["libraries"]
    results = []
    for lib, meta in lock.items():
        repo = meta["repo"]
        pinned = meta["commit"]
        try:
            out = subprocess.run(
                ["git", "ls-remote", f"https://github.com/{repo}", "HEAD"],
                capture_output=True, text=True, timeout=30
            )
            upstream = out.stdout.split()[0] if out.stdout.strip() else None
        except Exception as e:
            upstream = None
            results.append({"lib": lib, "pinned": pinned[:12], "upstream": None, "status": "ERROR", "drift": 0})
            continue
        if upstream and upstream != pinned:
            results.append({"lib": lib, "pinned": pinned[:12], "upstream": upstream[:12], "status": "STALE", "drift": -1})
        else:
            results.append({"lib": lib, "pinned": pinned[:12], "upstream": (upstream or "?")[:12], "status": "CURRENT", "drift": 0})

    current = sum(1 for r in results if r["status"] == "CURRENT")
    stale = sum(1 for r in results if r["status"] == "STALE")
    error = sum(1 for r in results if r["status"] == "ERROR")

    report = {
        "checked_at": datetime.datetime.now().isoformat(),
        "total": len(results),
        "current": current,
        "stale": stale,
        "error": error,
        "libs": results
    }

    ci = "--ci" in sys.argv
    json.dump(report, sys.stdout, indent=2)
    if ci and (stale > 0 or error > 0):
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
