#!/usr/bin/env python3
"""Restore Backup/Not Playing review entries without deleting unrelated streams.

Safety policy:
- Protected entries are restored exactly as captured in the snapshot.
- An exact URL already present in the current playlist is not duplicated.
- A different URL with the same tvg-id/tvg-name is NOT removed automatically.
  It may be a legitimate replacement or alternate stream and must survive for
  the normal no-removal guard to evaluate.
"""
from pathlib import Path
import re
import sys

SNAPSHOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/tmp/iptv-protected-review.m3u')
PLAYLIST = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('IPTV-Playlist.m3u')


def blocks(text):
    lines = text.replace('\r', '').splitlines()
    result = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('#EXTINF:'):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].strip().lower().startswith(('http://', 'https://')):
                result.append((lines[i], lines[j].strip()))
                i = j + 1
                continue
        i += 1
    return result


def attrs(info):
    return dict(re.findall(r'([\w-]+)="([^"]*)"', info))


def group_of(info):
    return attrs(info).get('group-title', '').strip()


def restore():
    if not SNAPSHOT.is_file() or not PLAYLIST.is_file():
        return

    protected = blocks(SNAPSHOT.read_text(encoding='utf-8'))
    if not protected:
        return

    current_text = PLAYLIST.read_text(encoding='utf-8-sig').replace('\r', '')
    current = current_text.splitlines()

    # Only exact stream URLs are used to decide whether a protected record is
    # already present.  Do NOT remove a current entry merely because its
    # tvg-id/tvg-name matches a protected entry: that can destroy a legitimate
    # alternate/replacement stream before the global removal guard evaluates it.
    current_urls = {
        line.strip().casefold()
        for line in current
        if line.strip().lower().startswith(('http://', 'https://'))
    }

    restored = 0
    skipped_existing = 0

    for info, url in protected:
        if url.casefold() in current_urls:
            skipped_existing += 1
            continue

        group = group_of(info)
        insert_at = None
        i = 0
        while i < len(current):
            if current[i].startswith('#EXTINF:') and group_of(current[i]) == group:
                j = i + 1
                while j < len(current) and not current[j].strip():
                    j += 1
                if j < len(current) and current[j].strip().lower().startswith(('http://', 'https://')):
                    insert_at = j + 1
            i += 1

        record = [info, url]
        if insert_at is None:
            current.extend(record)
        else:
            current[insert_at:insert_at] = record
        current_urls.add(url.casefold())
        restored += 1

    PLAYLIST.write_text('\n'.join(current).rstrip() + '\n', encoding='utf-8')
    print(
        f'Protected review restore: restored={restored} '
        f'skipped_exact_existing={skipped_existing} '
        f'removed_conflicting_copies=0'
    )


if __name__ == '__main__':
    restore()
