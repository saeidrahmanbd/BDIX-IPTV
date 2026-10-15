#!/usr/bin/env python3
"""Remove only persistently failed, redundant Backup streams from IPTV-Playlist.

Safety rules:
- IPTV-Playlist.m3u only.
- Never remove a primary stream.
- Only consider Backup entries with >=3 consecutive failures in the health history.
- Keep the failed backup when it is the only stream for its identity.
- Keep at least one non-persistently-failed stream for the same identity/name.
- Never modify BDIX-Playlist.m3u.
"""
from pathlib import Path
import json,re

PLAYLIST=Path('IPTV-Playlist.m3u')
HISTORY=Path('reports/stream-health-history.json')
ATTR=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

def attrs(s): return dict(ATTR.findall(s))
def name(s):
 a=attrs(s); return (a.get('tvg-name') or s.rsplit(',',1)[-1]).strip().casefold()
def url(block):
 for x in block[1:]:
  x=x.strip()
  if x.startswith(('http://','https://')): return x
 return ''
def parse(text):
 pre=[]; blocks=[]; cur=None
 for line in text.replace('\r','').splitlines():
  if line.startswith('#EXTINF:'):
   if cur is not None: blocks.append(cur)
   cur=[line]
  elif cur is None: pre.append(line)
  else: cur.append(line)
 if cur is not None: blocks.append(cur)
 return pre,blocks

def main():
 if not PLAYLIST.exists() or not HISTORY.exists():
  print('No IPTV playlist or health history; nothing removed.'); return
 try: history=json.loads(HISTORY.read_text(encoding='utf-8'))
 except Exception:
  print('Invalid health history; nothing removed.'); return
 pre,blocks=parse(PLAYLIST.read_text(encoding='utf-8-sig'))
 rows=[]
 for b in blocks:
  a=attrs(b[0]); rows.append((b,a,url(b)))
 persistent={u for u,h in history.items() if isinstance(h,dict) and int(h.get('consecutive_failures',0))>=3}
 # Determine usable alternatives by identity first, then by display name.
 groups={}
 for b,a,u in rows:
  ident=(a.get('tvg-id') or a.get('channel-id') or '').strip().casefold()
  key=('id',ident) if ident else ('name',name(b[0]))
  groups.setdefault(key,[]).append((b,a,u))
 remove_urls=set()
 for b,a,u in rows:
  if a.get('group-title','').strip()!='Backup' or not u or u not in persistent:
   continue
  ident=(a.get('tvg-id') or a.get('channel-id') or '').strip().casefold()
  key=('id',ident) if ident else ('name',name(b[0]))
  peers=groups.get(key,[])
  alternatives=[x for x in peers if x[2] and x[2]!=u and x[2] not in persistent]
  if alternatives:
   remove_urls.add(u)

 if not remove_urls:
  print('Persistent backup cleanup: 0 removals')
  return
 out=[]
 for b,a,u in rows:
  if u in remove_urls:
   continue
  out.append(b)
 PLAYLIST.write_text('\n'.join(pre+[x for b in out for x in b]).rstrip()+'\n',encoding='utf-8')
 print(f'Persistent backup cleanup: removed={len(remove_urls)} remaining={len(out)}')

if __name__=='__main__': main()
