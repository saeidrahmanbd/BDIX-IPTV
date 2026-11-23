#!/usr/bin/env python3
"""Structural and recovery-accounting validator for the International health rewrite."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from international_stream_health import (
    HISTORY, PLAYLIST, REPORT, validate_published_recovery_report,
    validate_rendered_playlist,
)


def main():
    if not PLAYLIST.is_file():
        raise SystemExit("International-Playlist.m3u is missing.")
    if not REPORT.is_file() or not HISTORY.is_file():
        raise SystemExit("International health report/history is missing.")
    text = PLAYLIST.read_text(encoding="utf-8-sig")
    report = REPORT.read_text(encoding="utf-8")
    history = json.loads(HISTORY.read_text(encoding="utf-8"))
    validate_rendered_playlist(text)
    recovered = validate_published_recovery_report(text, report, history)
    print(
        "International health output validation passed: playlist structure, group order, "
        f"URL rows, duplicate-stream checks and {recovered} verified recovery report rows."
    )


if __name__ == "__main__":
    main()
