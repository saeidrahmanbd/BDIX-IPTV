#!/usr/bin/env python3
"""Detect stale playlist/health reports before publication."""
from pathlib import Path
import re,sys
entries=len(re.findall(r'^#EXTINF:',Path('IPTV-Playlist.m3u').read_text(encoding='utf-8-sig'),re.M))
checks=[]
for fn in ('reports/playlist-audit.md','reports/stream-health.md'):
 f=Path(fn)
 if not f.exists(): checks.append(f'{fn}: missing'); continue
 s=f.read_text(encoding='utf-8',errors='replace')
 if '1,094' in s and entries!=1094: checks.append(f'{fn}: contains obsolete 1,094-entry figure while playlist has {entries}')
for x in checks: print('REPORT_STALE:',x)
if checks: sys.exit(1)
print(f'Report freshness basic check passed for {entries} playlist entries.')
