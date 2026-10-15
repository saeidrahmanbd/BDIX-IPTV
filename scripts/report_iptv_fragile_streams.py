#!/usr/bin/env python3
"""Report fragile/session-like IPTV URLs without deleting legitimate streams."""
from pathlib import Path
import re
from urllib.parse import urlsplit,parse_qsl

P=Path('IPTV-Playlist.m3u'); OUT=Path('reports/iptv-fragile-streams.md')
ATTR=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
SENSITIVE={'token','sig','signature','jwt','session','key','authorization','hdnts','expires','e'}

def attrs(s): return dict(ATTR.findall(s))
def parse(t):
 rows=[]; cur=None
 for line in t.splitlines():
  if line.startswith('#EXTINF:'): cur=line
  elif cur and line.strip().startswith(('http://','https://')):
   rows.append((attrs(cur),line.strip())); cur=None
 return rows

def main():
 rows=parse(P.read_text(encoding='utf-8-sig'))
 found=[]
 for a,u in rows:
  p=urlsplit(u); q={k.lower() for k,v in parse_qsl(p.query,keep_blank_values=True)}
  reasons=[]
  if q & SENSITIVE: reasons.append('sensitive query parameter')
  if any(x in u.casefold() for x in ('/api/play/','workers.dev','railway.app')): reasons.append('dynamic/proxy endpoint')
  if reasons: found.append((a.get('tvg-name',''),a.get('group-title',''),u,', '.join(reasons)))
 lines=['# IPTV Fragile Stream Review','','These streams are not automatically removed. They are flagged because their URL shape suggests token/session dependence or an intermediary/proxy endpoint.','',f'- Flagged streams: **{len(found)}**','', '| Channel | Group | Reason | URL |','|---|---|---|---|']
 for n,g,u,r in found: lines.append(f'| {n} | {g} | {r} | `{u}` |')
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print(f'Fragile stream report: {len(found)} flagged')
if __name__=='__main__': main()
