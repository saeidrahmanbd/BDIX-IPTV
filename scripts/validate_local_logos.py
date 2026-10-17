#!/usr/bin/env python3
"""Verify every playlist logo points to an existing repository asset."""
from pathlib import Path
import re,sys
RAW='https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/'
text=Path('IPTV-Playlist.m3u').read_text(encoding='utf-8-sig')
bad=[]
for line in text.splitlines():
 if not line.startswith('#EXTINF:'): continue
 m=re.search(r'tvg-logo="([^"]+)"',line)
 if not m: bad.append('missing logo: '+line); continue
 url=m.group(1)
 if not url.startswith(RAW): bad.append('external logo: '+url); continue
 path=Path('logos')/Path(url.split('?',1)[0]).name
 if not path.exists(): bad.append('missing asset: '+str(path))
if bad:
 print('\n'.join(bad[:100])); sys.exit(1)
print('Local logo validation passed.')
