#!/usr/bin/env python3
"""Validate that GitHub Actions workflows do not reference missing repository scripts."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
SCRIPT_RE = re.compile(r"(?:python(?:3)?\s+)?(?:\./)?(scripts/[A-Za-z0-9_.-]+\.py)")


def main() -> int:
    missing = []
    for workflow in sorted(WORKFLOWS.glob("*.yml")) + sorted(WORKFLOWS.glob("*.yaml")):
        text = workflow.read_text(encoding="utf-8", errors="replace")
        for script in sorted(set(SCRIPT_RE.findall(text))):
            if not (ROOT / script).is_file():
                missing.append(f"{workflow.relative_to(ROOT)} -> {script}")

    if missing:
        print("::error::Workflow references missing repository scripts:")
        for item in missing:
            print(f" - {item}")
        return 1

    print("Workflow script reference check passed: all referenced scripts exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
