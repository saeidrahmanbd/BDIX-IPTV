#!/usr/bin/env python3
"""Enforce the immutable SAEID RAHMAN attribution block in every published M3U."""
from pathlib import Path
import sys

PLAYLISTS = (
    Path("BDIX-Playlist.m3u"),
    Path("IPTV-Playlist.m3u"),
    Path("NVisionBD-Playlist.m3u"),
)
BLOCK = (
    "#=================================",
    "# Developed by: SAEID RAHMAN",
    "# Facebook: https://www.facebook.com/saeid.rahman.sr",
    "# Email: saeidrahman.mkt@gmail.com",
    "#=================================",
)

def enforce(path: Path) -> bool:
    if not path.is_file():
        # Some focused workflows may run in a checkout where a playlist is absent.
        return False
    lines = path.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    if not lines or not lines[0].startswith("#EXTM3U"):
        raise SystemExit(f"{path}: missing #EXTM3U first line; refusing to rewrite.")
    # Remove exact existing copies of the protected block, then restore exactly one
    # copy immediately after #EXTM3U. Other playlist metadata and channel entries
    # remain in their existing order and are not changed by this guard.
    i = 1
    while i <= len(lines) - len(BLOCK):
        if tuple(lines[i:i + len(BLOCK)]) == BLOCK:
            del lines[i:i + len(BLOCK)]
        else:
            i += 1
    lines[1:1] = list(BLOCK)
    content = "\n".join(lines).rstrip("\n") + "\n"
    old = path.read_text(encoding="utf-8-sig").replace("\r", "")
    if old != content:
        path.write_text(content, encoding="utf-8")
        print(f"{path}: restored protected attribution block.")
    else:
        print(f"{path}: attribution block verified.")
    # Verify exact placement and uniqueness after write.
    check = path.read_text(encoding="utf-8").splitlines()
    if tuple(check[1:1 + len(BLOCK)]) != BLOCK or sum(line == BLOCK[1] for line in check) != 1:
        raise SystemExit(f"{path}: protected attribution verification failed.")
    return True

def main():
    missing = []
    for path in PLAYLISTS:
        if path.exists():
            enforce(path)
        else:
            missing.append(str(path))
    if missing:
        print("Playlists not present in this checkout (skipped): " + ", ".join(missing))
    print("Protected playlist attribution guard passed.")

if __name__ == "__main__":
    main()
