"""Verify the retained October 14–15 packages without rewriting evidence files."""
from pathlib import Path
import json
import runpy
import sys


CHECKERS = (
    "check_retained_reconciliation_20261014.py",
    "check_retained_evening_20261014.py",
    "check_retained_morning_20261015.py",
)


def verify_all():
    """Run existing offline verification functions; preserve their evidence scope."""
    summaries = []
    for name in CHECKERS:
        try:
            result = runpy.run_path(str(Path(__file__).with_name(name)))["verify"]()
            summary = {key: result[key] for key in ("checks", "failed", "network_calls")}
            summary["tool"] = name
            summary["failures"] = [item["check"] for item in result["results"] if not item["passed"]]
        except Exception as exc:
            summary = {"tool": name, "checks": 0, "failed": 1,
                       "network_calls": 0, "failures": [f"{type(exc).__name__}: {exc}"]}
        summaries.append(summary)
    return {"mode": "local_offline_read_only",
            "scope": "retained October 14–15 diagnostic packages",
            "checks": sum(item["checks"] for item in summaries),
            "failed": sum(item["failed"] for item in summaries),
            "tools": summaries}


if __name__ == "__main__":
    result = verify_all()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(bool(result["failed"]))
