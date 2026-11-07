#!/usr/bin/env python3
"""Structural validator for the International stream-health rewrite."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from international_stream_health import PLAYLIST, validate_rendered_playlist


def main():
    if not PLAYLIST.is_file():
        raise SystemExit("International-Playlist.m3u is missing.")
    text = PLAYLIST.read_text(encoding="utf-8-sig")
    validate_rendered_playlist(text)
    print("International health output validation passed: categories, group order, URL rows and duplicate-stream checks.")


if __name__ == "__main__":
    main()
