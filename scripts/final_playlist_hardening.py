#!/usr/bin/env python3
"""Final deterministic playlist hardening.

Hardens one explicitly selected playlist at a time. Stream URLs are never
changed or removed; exact duplicate URLs block the run for manual review.
"""
from pathlib import Path
import re, sys, unicodedata

PLAYLIST_ORDERS={
    'IPTV-Playlist.m3u': ['Bangladesh','Indian Bangla','Indian Movies','Indian Music','Indian Entertainment','Pakistani','International','Documentary & Wildlife','Kids','Religious','Sports','New Channels','New Backup','Backup','Not Playing'],
    'BDIX-Playlist.m3u': ['Bangladesh','Indian Bangla','Indian Movies','Indian Music','Indian Entertainment','Pakistani','International','Documentary & Wildlife','Kids','Religious','Sports','Backup','Not Playing','Test'],
}
ATTR=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NON_NUMBERED={'Backup','Not Playing','New Channels','New Backup'}
REVIEW_GROUPS={'New Channels','New Backup'}

def attrs(s): return dict(ATTR.findall(s))
def key(s):
 s=unicodedata.normalize('NFKD',str(s or '')).casefold().strip()
 return tuple(int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s))
def set_attr(line,k,v):
 p=re.compile(rf'{re.escape(k)}="[^"]*"')
 return p.sub(f'{k}="{v}"',line,1) if p.search(line) else line.replace('#EXTINF:-1 ',f'#EXTINF:-1 {k}="{v}" ',1)
def remove_attr(line,k):
 return re.sub(rf'\s+{re.escape(k)}="[^"]*"','',line, count=1)
def parse(path):
 lines=path.read_text(encoding='utf-8-sig').replace('\r\n','\n').replace('\r','\n').splitlines(); pre=[]; rec=[]; cur=None
 for line in lines:
  if line.startswith('#EXTINF:'):
   if cur is not None: rec.append(cur)
   cur=[line]
  elif cur is not None: cur.append(line)
  else: pre.append(line)
 if cur is not None: rec.append(cur)
 return pre,rec
def process(path):
 if not path.is_file(): return
 order=PLAYLIST_ORDERS[path.name]; rank={x:i for i,x in enumerate(order)}
 pre,rec=parse(path)
 seen=set(); duplicate_urls=[]
 for r in rec:
  u=next((x.strip() for x in r[1:] if x.strip().startswith(('http://','https://'))),'')
  k=u.casefold()
  if k and k in seen: duplicate_urls.append(u)
  if k: seen.add(k)
 if duplicate_urls:
  raise SystemExit(f'{path}: {len(duplicate_urls)} duplicate stream URL occurrences; refusing to delete any entry.')
 for r in rec:
  a=attrs(r[0]); cid=(a.get('tvg-id') or a.get('channel-id') or '').strip().casefold(); g=a.get('group-title','').strip()
  if cid=='ultimatetv.in@sd' and g!='Backup': r[0]=set_attr(r[0],'group-title','Indian Music')
  if g in NON_NUMBERED and 'tvg-chno' in a:
   r[0]=remove_attr(r[0],'tvg-chno')
 def rkey(r):
  a=attrs(r[0]); g=a.get('group-title','').strip(); n=(a.get('tvg-name') or r[0].rsplit(',',1)[-1]).strip()
  u=next((x.strip() for x in r[1:] if x.strip().startswith(('http://','https://'))),'')
  if g == 'Bangladesh':
   raw=a.get('tvg-chno','').strip()
   number=int(raw) if raw.isdigit() else 10**12
   return (rank.get(g,len(rank)),number,key(n),u.casefold())
  return (rank.get(g,len(rank)),key(n),u.casefold())
 rec.sort(key=rkey)
 errors=[]; transitions=[]; last=None
 for r in rec:
  g=attrs(r[0]).get('group-title','').strip()
  if g!=last: transitions.append(g); last=g
 last_i=-1
 for g in transitions:
  if g not in rank: errors.append(f'unknown category: {g}'); continue
  i=rank[g]
  if i<last_i: errors.append(f'category order: {g}')
  last_i=max(last_i,i)
 if any(transitions.count(g)>1 for g in set(transitions)): errors.append('split category block')
 for g in order:
  group_records=[r for r in rec if attrs(r[0]).get('group-title','').strip()==g]
  if not group_records: continue
  if g == 'Bangladesh':
   numbers=[int(attrs(r[0]).get('tvg-chno','')) for r in group_records if attrs(r[0]).get('tvg-chno','').strip().isdigit()]
   if len(numbers)!=len(group_records) or numbers!=sorted(numbers):
    errors.append('channel-number order/coverage: Bangladesh')
  elif g not in REVIEW_GROUPS:
   names=[(attrs(r[0]).get('tvg-name') or r[0].rsplit(',',1)[-1]).strip() for r in group_records]
   if names!=sorted(names,key=key): errors.append(f'A-Z order: {g}')
 for r in rec:
  a=attrs(r[0]); g=a.get('group-title','').strip()
  cid=(a.get('tvg-id') or a.get('channel-id') or '').strip().casefold()
  name=(a.get('tvg-name') or r[0].rsplit(',',1)[-1]).strip().casefold()
  if name=='channel s uk' and (g not in {'Bangladesh','Backup'} or cid!='channels.uk@679aa9'): errors.append('Channel S UK must retain its canonical identity in Bangladesh/Backup')
  if cid=='ultimatetv.in@sd' and g not in {'Indian Music','Backup'}: errors.append('Ultimate TV must be Indian Music primary or Backup alternate')
 if errors:
  raise SystemExit(f'{path}: '+ '; '.join(errors))
 path.write_text('\n'.join(pre+[x for r in rec for x in r])+'\n',encoding='utf-8')
 print(f'HARDENED {path}: {len(rec)} records')

paths=sys.argv[1:] or list(PLAYLIST_ORDERS)
for name in paths:
 p=Path(name)
 if p.name not in PLAYLIST_ORDERS: raise SystemExit(f'Unsupported playlist: {p}')
 process(p)
