#!/usr/bin/env python3
"""Guard: International Backup / Not Playing stream URLs must survive maintenance.

  snapshot  record the stream URLs of protected groups (before any mutation)
  verify    fail if any recorded URL no longer appears anywhere in the playlist

Removal of a protected stream needs an explicit entry in AUTHORIZED_REMOVALS (URL -> reason).
Moves, attribute fills and re-ordering are allowed here and are reviewed through the PR/bot
diff; this guard only prevents silent deletion.
"""
import json
import re
import sys
from pathlib import Path

PLAYLIST = Path("International-Playlist.m3u")
BASELINE = Path("/tmp/international-protected-baseline.json")
PROTECTED = {"backup", "backups", "not playing"}
AUTHORIZED_REMOVALS: dict[str, str] = {}
GROUP_RE = re.compile(r'group-title="([^"]*)"')


def protected_urls(text: str) -> list[str]:
    urls, group = [], None
    for line in text.replace("\r", "").splitlines():
        if line.startswith("#EXTINF:"):
            m = GROUP_RE.search(line)
            group = (m.group(1).strip().casefold() if m else "")
        elif line.strip().startswith(("http://", "https://")):
            if group in PROTECTED:
                urls.append(line.strip())
            group = None
    return urls


def all_urls(text: str) -> set[str]:
    return {l.strip() for l in text.replace("\r", "").splitlines() if l.strip().startswith(("http://", "https://"))}


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] not in {"snapshot", "verify"}:
        print(__doc__)
        return 2
    text = PLAYLIST.read_text(encoding="utf-8-sig")
    if argv[1] == "snapshot":
        urls = protected_urls(text)
        BASELINE.write_text(json.dumps(urls), encoding="utf-8")
        print(f"International protected baseline: {len(urls)} Backup/Not Playing stream URLs")
        return 0
    if not BASELINE.exists():
        print("ERROR: International protected baseline is missing", file=sys.stderr)
        return 1
    present = all_urls(text)
    missing = [u for u in json.loads(BASELINE.read_text(encoding="utf-8"))
               if u not in present and u not in AUTHORIZED_REMOVALS]
    if missing:
        print(f"ERROR: {len(missing)} protected International Backup/Not Playing stream(s) were removed without authorization:", file=sys.stderr)
        for u in missing[:50]:
            print(f"  {u}", file=sys.stderr)
        return 1
    print("International protected Backup/Not Playing streams preserved.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
