#!/usr/bin/env python3
from pathlib import Path
import re, unicodedata
PLAYLIST=Path('IPTV-Playlist.m3u')
CATEGORIES=['Bangladesh','Indian Bangla','Indian Movies','Indian Music','Indian Entertainment','Pakistani','International','Documentary & Wildlife','Kids','Religious','Sports','Backup','New Channels','New Backup','Not Playing']
NON_NUMBERED={'Backup','New Backup','Not Playing'}
ATTR_RE=re.compile(r'([\w-]+)="([^"]*)"')
def attrs(s): return dict(ATTR_RE.findall(s))
def key(s):
 s=unicodedata.normalize('NFKD',s).casefold().strip(); return [int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s)]
def entries():
 L=PLAYLIST.read_text(encoding='utf-8').replace('\r','').splitlines(); out=[]
 for i,l in enumerate(L):
  if l.startswith('#EXTINF:'):
   a=attrs(l); u=''
   for x in L[i+1:]:
    x=x.strip()
    if x.startswith('#EXTINF:'): break
    if x.startswith(('http://','https://')): u=x; break
   out.append((a,u))
 return out
def main():
 E=entries(); err=[]; trans=[]; last=None
 for a,_ in E:
  g=a.get('group-title','').strip()
  if g!=last: trans.append(g); last=g
 idx=-1
 for g in trans:
  if g not in CATEGORIES: err.append('unknown category: '+g); continue
  n=CATEGORIES.index(g)
  if n<idx: err.append('category out of order: '+g)
  idx=max(idx,n)
 if any(trans.count(g)>1 for g in set(trans)): err.append('split category block')
 for g in CATEGORIES:
  names=[a.get('tvg-name','').strip() for a,_ in E if a.get('group-title','').strip()==g]
  if names and names!=sorted(names,key=key): err.append('not A-Z: '+g)
 P=[a for a,_ in E if a.get('group-title','').strip() not in NON_NUMBERED]
 missing=[a.get('tvg-name','') for a in P if not a.get('tvg-chno','').strip()]
 nums=[a.get('tvg-chno','').strip() for a in P]; dup=sorted({x for x in nums if x and nums.count(x)>1},key=key)
 if missing: err.append('missing tvg-chno: '+str(missing[:10]))
 if dup: err.append('duplicate tvg-chno: '+str(dup))
 if any(a.get('tvg-chno','').strip() for a,_ in E if a.get('group-title','').strip() in NON_NUMBERED): err.append('numbered non-primary entry')
 groups={a.get('group-title','').strip() for a,_ in E if a.get('tvg-id','').strip().casefold()=='ultimatetv.in@sd'}
 if len(groups)>1: err.append('ultimatetv.in@sd in multiple groups')
 if err:
  print('\n'.join('BLOCK: '+x for x in err)); raise SystemExit(1)
 print(f'PASS {len(E)} entries')
if __name__=='__main__': main()
