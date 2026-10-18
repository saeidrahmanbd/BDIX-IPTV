#!/usr/bin/env python3
"""Small helpers used by the IPTV maintenance workflow.

Keeping these operations in a real Python file avoids nested Bash heredocs in
GitHub Actions, which previously caused an unexpected EOF in the maintenance job.
"""
from pathlib import Path
import re
import sys

BAD_LOGOS = {
    'atn-news.png','a-sports-5485adff.png','a-sports-hd.png','bein-sports-3.png',
    'bangla-tv.png','btv-news.png','colors.png','duronto-tv.png',
    'duronto-tv-1ad55c95.png','ekushey-tv.png','global-tv.png','green-tv.png',
    'mohona-tv.png','nagorik-tv.png','nagorik.png','nick-bangla.png',
    'sananda-tv.png','sananda.png','star-gold-select.png','star-gold.png',
    'star-plus.png','zee-tv.png','tom-and-jerry.png','arirang-tv.png',
}


def snapshot_protected() -> None:
    p = Path('IPTV-Playlist.m3u')
    lines = p.read_text(encoding='utf-8-sig').replace('\r', '').splitlines()
    protected = []
    for i, line in enumerate(lines):
        if not line.startswith('#EXTINF:'):
            continue
        m = re.search(r'group-title="([^"]*)"', line)
        if not m or m.group(1).strip() not in {'Backup', 'Not Playing'}:
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j < len(lines) and lines[j].strip().lower().startswith(('http://', 'https://')):
            protected.append(line + '\n' + lines[j].strip())
    Path('/tmp/iptv-protected-review.m3u').write_text(
        '\n'.join(protected) + '\n', encoding='utf-8'
    )
    print(f'Protected review snapshot: {len(protected)} entries')


def invalidate_bad_logos(message: str) -> None:
    p = Path('IPTV-Playlist.m3u')
    lines = p.read_text(encoding='utf-8-sig').replace('\r', '').splitlines()
    out = []
    changed = 0
    for line in lines:
        if line.startswith('#EXTINF:'):
            m = re.search(r'tvg-logo="([^"]*)"', line)
            if m:
                logo = Path(m.group(1).split('?', 1)[0].split('#', 1)[0]).name.casefold()
                if logo in BAD_LOGOS:
                    line = line[:m.start(1)] + line[m.end(1):]
                    changed += 1
        out.append(line)
    p.write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')
    print(f'{message}: {changed}')


def main() -> int:
    if len(sys.argv) != 2:
        print('Usage: maintenance_helpers.py snapshot|invalidate-bad-logos', file=sys.stderr)
        return 2
    if sys.argv[1] == 'snapshot':
        snapshot_protected()
        return 0
    if sys.argv[1] == 'invalidate-bad-logos':
        invalidate_bad_logos('Known-bad local logo references invalidated')
        return 0
    if sys.argv[1] == 'invalidate-bad-logos-correction':
        invalidate_bad_logos('Known-bad references invalidated on correction pass')
        return 0
    print(f'Unknown command: {sys.argv[1]}', file=sys.stderr)
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
