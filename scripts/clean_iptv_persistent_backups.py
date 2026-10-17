#!/usr/bin/env python3
"""Disabled legacy cleanup guard.

Stream-health results are advisory only because the playlist owner tests channels
manually. This script is intentionally non-destructive and never edits a playlist.
"""
def main():
    print("Automatic health-based deletion is disabled. No channels were removed or reclassified; review reports/stream-health.md manually.")

if __name__ == "__main__":
    main()
