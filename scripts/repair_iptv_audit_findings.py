#!/usr/bin/env python3
"""Deterministic deep cleanup for IPTV-Playlist.m3u only."""
from pathlib import Path
import re, unicodedata

P=Path("IPTV-Playlist.m3u")
ATTR_RE=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NO_NUMBER={"Backup","Not Playing"}

def attrs(s): return dict(ATTR_RE.findall(s))
def set_attr(s,k,v):
 p=re.compile(rf'{re.escape(k)}="[^"]*"')
 return p.sub(f'{k}="{v}"',s,1) if p.search(s) else s.replace('#EXTINF:-1 ',f'#EXTINF:-1 {k}="{v}" ',1)
def remove_attr(s,k): return re.sub(rf'\s+{re.escape(k)}="[^"]*"',"",s,count=1)
def split_display(s):
 q=False
 for i,ch in enumerate(s):
  if ch=='"': q=not q
  elif ch==',' and not q: return s[:i],s[i+1:].strip()
 return s,""
def set_display(s,n): return split_display(s)[0]+','+n
def slug(v):
 v=unicodedata.normalize('NFKD',v or '')
 v=''.join(c for c in v if not unicodedata.combining(c))
 return re.sub(r'[^a-z0-9]+','.',v.casefold()).strip('.')
def name_of(s):
 a=attrs(s); return (a.get('tvg-name') or split_display(s)[1]).strip()
def url_of(b):
 for x in b[1:]:
  x=x.strip()
  if x.startswith(('http://','https://')): return x
 return ''
def parse(t):
 pre=[]; blocks=[]; cur=None
 for line in t.replace('\r','').splitlines():
  if line.startswith('#EXTINF:'):
   if cur is not None: blocks.append(cur)
   cur=[line]
  elif cur is None: pre.append(line)
  else: cur.append(line)
 if cur is not None: blocks.append(cur)
 return pre,blocks

def normalize(info):
 a=attrs(info); n=name_of(info); tvg=a.get('tvg-id','').strip(); cid=a.get('channel-id','').strip()
 if tvg.casefold().startswith('staging.'): tvg='custom.'+slug(n); info=set_attr(info,'tvg-id',tvg)
 if cid.casefold().startswith('staging.'): cid=tvg or 'custom.'+slug(n); info=set_attr(info,'channel-id',cid)
 if not tvg and cid: info=set_attr(info,'tvg-id',cid)
 if not cid and tvg: info=set_attr(info,'channel-id',tvg)
 if not tvg and not cid and n:
  cid='custom.'+slug(n); info=set_attr(info,'tvg-id',cid); info=set_attr(info,'channel-id',cid)
 if not attrs(info).get('tvg-name','').strip() and n: info=set_attr(info,'tvg-name',n)
 return info

def main():
 if not P.exists(): return
 pre,blocks=parse(P.read_text(encoding='utf-8-sig')); out=[]; seen=set(); changed=removed=0

 # First normalize identities and apply deterministic safety removals.
 for b in blocks:
  info=normalize(b[0]); a=attrs(info); n=name_of(info); url=url_of(b); low=url.casefold()
  if 'tvsen5.aynaott.com/tk2bndfsdfsdf/index.m3u8' in low: removed+=1; continue
  if re.search(r'^https?://(?:[^/]+\.)?dvltv\.cc(?::\d+)?/play(?:/|$)',url,re.I): removed+=1; continue
  restore_urls={'https://vods2.aynaott.com/gseriesdrama/tracks-v1a1/mono.ts.m3u8','https://vods2.aynaott.com/gseriesdrama/index.m3u8','https://vods2.aynaott.com/hindimovies/index.m3u8'}
  if low not in restore_urls and (re.search(r'https?://[^/]*vods?\d*\.[^/]+/',url,re.I) or re.search(r'/vod(?:/|$)',url,re.I)): removed+=1; continue
  if re.search(r'[?&](?:token|auth)=(?:test|testpub)(?:&|$)',url,re.I): removed+=1; continue
  if re.search(r'https?://[^/@]+@[^/]+',url,re.I): removed+=1; continue
  if n.casefold()=='ntv (malyalam)': info=set_display(set_attr(info,'tvg-name','NTV (Malayalam)'),'NTV (Malayalam)'); changed+=1
  if attrs(info).get('tvg-country','').upper()=='UK': info=set_attr(info,'tvg-country','GB'); changed+=1
  if n.casefold() in {'s un bangla','sananda'}:
   if n.casefold()=='sananda' and ('sunbangla' in low or 'sun-bangla' in low or 'sunbangla' in info.casefold()):
    info=set_attr(info,'tvg-name','Sun Bangla'); info=set_attr(info,'tvg-id','custom.sun.bangla'); info=set_attr(info,'channel-id','custom.sun.bangla'); info=set_display(info,'Sun Bangla'); changed+=1
   elif n.casefold()=='s un bangla':
    info=set_attr(info,'tvg-name','Sun Bangla'); info=set_attr(info,'tvg-id','custom.sun.bangla'); info=set_attr(info,'channel-id','custom.sun.bangla'); info=set_display(info,'Sun Bangla'); changed+=1
  if n.casefold()=='baiscope tv': info=set_attr(info,'group-title','Bangladesh'); changed+=1
  if n.casefold()=='atn music': info=set_attr(info,'group-title','Bangladesh'); changed+=1
  if 'dai.google.com' in low or 'doubleclick.net' in low: removed+=1; continue
  if n.casefold()=='b4u movies':
   if '/api/play/filamchi.m3u8' in low:
    info=set_attr(info,'tvg-name','Filamchi'); info=set_attr(info,'tvg-id','custom.filamchi'); info=set_attr(info,'channel-id','custom.filamchi'); info=set_attr(info,'group-title','Backup'); info=remove_attr(info,'tvg-chno'); info=set_display(info,'Filamchi'); changed+=1
   elif '/api/play/manoranjan%20grand.m3u8' in low:
    info=set_attr(info,'tvg-name','Manoranjan Grand'); info=set_attr(info,'tvg-id','custom.manoranjan.grand'); info=set_attr(info,'channel-id','custom.manoranjan.grand'); info=set_attr(info,'group-title','Backup'); info=remove_attr(info,'tvg-chno'); info=set_display(info,'Manoranjan Grand'); changed+=1
  g=attrs(info).get('group-title','').strip()
  if g in NO_NUMBER: info=remove_attr(info,'tvg-chno')
  key=url.strip().casefold()
  if key and key in seen: removed+=1; continue
  if key: seen.add(key)
  b[0]=info; out.append(b)

 # Backup identity migration: when a Backup name has exactly one matching
 # primary identity, use that primary's tvg-id/channel-id. This makes the
 # relationship explicit without inventing identities for ambiguous names.
 primary_by_name={}
 for b in out:
  a=attrs(b[0]); g=a.get('group-title','').strip()
  if g in NO_NUMBER: continue
  n=name_of(b[0]).casefold().strip()
  ident=(a.get('tvg-id') or a.get('channel-id') or '').strip()
  if n and ident:
   primary_by_name.setdefault(n,set()).add(ident)
 for b in out:
  a=attrs(b[0]); g=a.get('group-title','').strip()
  if g!='Backup': continue
  n=name_of(b[0]).casefold().strip(); ids=primary_by_name.get(n,set())
  if len(ids)==1:
   ident=next(iter(ids))
   if a.get('tvg-id') != ident or a.get('channel-id') != ident:
    b[0]=set_attr(b[0],'tvg-id',ident); b[0]=set_attr(b[0],'channel-id',ident); changed+=1
  b[0]=remove_attr(b[0],'tvg-chno')

 # Never give Backup/Not Playing a primary number; preserve existing valid
 # primary numbers and only fill genuinely missing primary numbers.
 used=set()
 for b in out:
  a=attrs(b[0]); g=a.get('group-title','').strip(); n=a.get('tvg-chno','').strip()
  if g not in NO_NUMBER and n.isdigit() and int(n)>0: used.add(int(n))
 seen_no=set(); next_no=1
 for b in out:
  a=attrs(b[0]); g=a.get('group-title','').strip()
  if g in NO_NUMBER:
   b[0]=remove_attr(b[0],'tvg-chno'); continue
  n=a.get('tvg-chno','').strip()
  if n.isdigit() and int(n)>0 and int(n) not in seen_no:
   seen_no.add(int(n)); continue
  while next_no in used: next_no+=1
  b[0]=set_attr(b[0],'tvg-chno',str(next_no)); used.add(next_no); seen_no.add(next_no); next_no+=1; changed+=1

 P.write_text('\n'.join(pre+[x for b in out for x in b]).rstrip()+'\n',encoding='utf-8')
 print(f'IPTV repair changed={changed} removed={removed} remaining={len(out)}')

if __name__=='__main__': main()
