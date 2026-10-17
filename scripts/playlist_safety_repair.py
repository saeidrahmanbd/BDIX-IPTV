#!/usr/bin/env python3
"""Non-destructive IPTV playlist safety repair.

Only removes channel numbers from Backup/Not Playing and applies canonical
category/name ordering. It never deletes streams or promotes review entries.
"""
from pathlib import Path
import re, unicodedata
P=Path('IPTV-Playlist.m3u')
ORDER=['Bangladesh','Indian Bangla','Indian Movies','Indian Music','Indian Entertainment','Pakistani','International','Documentary & Wildlife','Kids','Religious','Sports','Backup','Not Playing']
NO_NUMBER={'Backup','Not Playing'}
ATTR=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
def attrs(s): return dict(ATTR.findall(s))
def remove_attr(s,key): return re.sub(rf'\s+{re.escape(key)}="[^"]*"','',s,count=1)
def name(s):
 a=attrs(s); return a.get('tvg-name','').strip() or s.rsplit(',',1)[-1].strip()
def natural(s):
 s=unicodedata.normalize('NFKD',str(s or '')).casefold().strip()
 return tuple(int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s))
def main():
 lines=P.read_text(encoding='utf-8-sig').replace('\r','').splitlines(); pre=[]; blocks=[]; cur=None
 for line in lines:
  if line.startswith('#EXTINF:'):
   if cur: blocks.append(cur)
   cur=[line]
  elif cur is not None: cur.append(line)
  else: pre.append(line)
 if cur: blocks.append(cur)
 changed=0
 for b in blocks:
  a=attrs(b[0]); g=a.get('group-title','').strip()
  if g in NO_NUMBER and a.get('tvg-chno','').strip(): b[0]=remove_attr(b[0],'tvg-chno'); changed+=1
 rank={g:i for i,g in enumerate(ORDER)}
 blocks.sort(key=lambda b:(rank.get(attrs(b[0]).get('group-title','').strip(),len(rank)),natural(name(b[0]))))
 P.write_text('\n'.join(pre+[line for b in blocks for line in b]).rstrip()+'\n',encoding='utf-8')
 print(f'Safety repair complete: queue numbers removed={changed}; streams deleted=0')
if __name__=='__main__': main()
