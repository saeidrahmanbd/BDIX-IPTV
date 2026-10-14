#!/usr/bin/env python3
"""Final deterministic playlist hardening.

This is the last playlist writer in maintenance. It enforces the canonical
category blocks and A-Z order and applies only explicitly approved metadata
classification fixes. Stream URLs and channel numbers are never changed.
"""
from pathlib import Path
import re, unicodedata

PLAYLISTS=(Path('IPTV-Playlist.m3u'),Path('BDIX-Playlist.m3u'))
CATEGORY_ORDER=['Bangladesh','Indian Bangla','Indian Movies','Indian Music','Indian Entertainment','Pakistani','International','Documentary & Wildlife','Kids','Religious','Sports','Backup','New Channels','New Backup','Not Playing']
RANK={x:i for i,x in enumerate(CATEGORY_ORDER)}
ATTR=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NON_NUMBERED={'Backup','New Backup','Not Playing'}

def attrs(s): return dict(ATTR.findall(s))
def key(s):
 s=unicodedata.normalize('NFKD',str(s or '')).casefold().strip()
 return tuple(int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s))
def set_attr(line,k,v):
 p=re.compile(rf'{re.escape(k)}="[^"]*"')
 return p.sub(f'{k}="{v}"',line,1) if p.search(line) else line.replace('#EXTINF:-1 ',f'#EXTINF:-1 {k}="{v}" ',1)
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
def rkey(r):
 a=attrs(r[0]); g=a.get('group-title','').strip(); n=(a.get('tvg-name') or r[0].rsplit(',',1)[-1]).strip()
 u=next((x.strip() for x in r[1:] if x.strip().startswith(('http://','https://'))),'')
 return (RANK.get(g,len(RANK)),key(n),u.casefold())
def validate(rec,path):
 errors=[]; transitions=[]; last=None
 for r in rec:
  g=attrs(r[0]).get('group-title','').strip()
  if g!=last: transitions.append(g); last=g
 last_i=-1
 for g in transitions:
  if g not in RANK: errors.append(f'unknown category: {g}'); continue
  i=RANK[g]
  if i<last_i: errors.append(f'category order: {g}')
  last_i=max(last_i,i)
 if any(transitions.count(g)>1 for g in set(transitions)): errors.append('split category block')
 for g in CATEGORY_ORDER:
  names=[(attrs(r[0]).get('tvg-name') or r[0].rsplit(',',1)[-1]).strip() for r in rec if attrs(r[0]).get('group-title','').strip()==g]
  if names and names!=sorted(names,key=key): errors.append(f'A-Z order: {g}')
 for r in rec:
  a=attrs(r[0]); g=a.get('group-title','').strip()
  if g in NON_NUMBERED and a.get('tvg-chno','').strip(): errors.append(f'numbered {g}: {a.get("tvg-name","")}')
  cid=(a.get('tvg-id') or a.get('channel-id') or '').strip().casefold()
  if cid=='ultimatetv.in@sd' and g!='Indian Music': errors.append('Ultimate TV not in Indian Music')
 if errors:
  raise SystemExit(f'{path}: '+ '; '.join(errors))
def process(path):
 if not path.is_file(): return
 pre,rec=parse(path)
 for r in rec:
  a=attrs(r[0]); cid=(a.get('tvg-id') or a.get('channel-id') or '').strip().casefold()
  if cid=='ultimatetv.in@sd': r[0]=set_attr(r[0],'group-title','Indian Music')
 rec.sort(key=rkey)
 validate(rec,path)
 path.write_text('\n'.join(pre+[x for r in rec for x in r])+'\n',encoding='utf-8')
 print(f'HARDENED {path}: {len(rec)} records')
for p in PLAYLISTS: process(p)
