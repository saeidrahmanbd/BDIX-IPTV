#!/usr/bin/env python3
"""Safe IPTV-Playlist.m3u fixer based on the supplied audit/fix design."""
import argparse,csv,re,time,unicodedata,urllib.error,urllib.request
from collections import defaultdict,Counter
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

BACKUP='Backup'
UA='Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 VLC/3.0.20'
CRED=[
 re.compile(r'^https?://[^/]+/(?:live|movie|series)/[^/?]+/[^/?]+/\d+(?:\.\w+)?(?:\?|$)',re.I),
 re.compile(r'[?&](?:username|password|pass|pwd)=',re.I),
 re.compile(r'/(?:get|player_api|xmltv)\.php\?',re.I),
 re.compile(r'/iptv/[A-Za-z0-9]{10,}/\d+/',re.I),
]
EXP=re.compile(r'[?&~=](?:e|exp|expires)=(\d{10})\b',re.I)

def norm(s):
 s=unicodedata.normalize('NFKD',s or '').encode('ascii','ignore').decode().lower()
 s=re.sub(r'\b(?:hd|uhd|fhd|sd)\b',' ',s)
 return re.sub(r'[^a-z0-9]','',s)

def slug(s): return 'custom.'+'.'.join(re.findall(r'[a-z0-9]+',unicodedata.normalize('NFKD',s or '').encode('ascii','ignore').decode().lower()))

def parse(text):
 lines=text.replace('\r','').splitlines(); header=[]; entries=[]; cur=None; pending=[]; seen=False
 for no,raw in enumerate(lines,1):
  s=raw.strip()
  if cur is None:
   if s.startswith('#EXTINF'):
    seen=True; cur={'pre':pending,'ext':s,'opts':[],'url':'','line':no}; pending=[]
   elif not seen: header.append(raw)
   elif s: pending.append(raw)
  else:
   if s.startswith('#EXTINF'):
    entries.append(cur); cur={'pre':[],'ext':s,'opts':[],'url':'','line':no}
   elif s.startswith('#'): cur['opts'].append(raw.rstrip())
   elif s: cur['url']=s; entries.append(cur); cur=None
 return header,entries

def attrs(ext): return dict(re.findall(r'([A-Za-z0-9_-]+)="([^"]*)"',ext))
def setv(ext,k,v):
 p=re.compile(r'(?<![\w-])'+re.escape(k)+r'="[^"]*"')
 return p.sub(f'{k}="{v}"',ext,1) if p.search(ext) else ext.rstrip()+f' {k}="{v}"'
def title(ext):
 q=False
 for i,c in enumerate(ext):
  if c=='"': q=not q
  elif c==',' and not q: return ext[i+1:].strip()
 return ''
def settitle(ext,v):
 q=False
 for i,c in enumerate(ext):
  if c=='"': q=not q
  elif c==',' and not q: return ext[:i+1]+v
 return ext+','+v
def delattr(ext,k): return re.sub(r'\s+'+re.escape(k)+r'="[^"]*"','',ext,count=1)
def cred(url): return any(p.search(url) for p in CRED)
def expiry(url):
 m=EXP.search(url)
 if not m:return None
 t=int(m.group(1)); return t if 1500000000<t<2500000000 else None

def fix(entries,report):
 prim={}
 for e in entries:
  a=attrs(e['ext']); g=a.get('group-title',''); n=title(e['ext']) or a.get('tvg-name','')
  e['name']=n; e['group']=g
  if g!=BACKUP and a.get('tvg-id'): prim[norm(n)]=e
 owners=defaultdict(set); out=[]; seen=set(); private=[]; quarantine=[]; orphans=[]
 for e in entries:
  a=attrs(e['ext']); n=e['name']; u=e['url']
  for k in ('tvg-id','channel-id'):
   v=a.get(k,'')
   if v.startswith('staging.'):
    e['ext']=setv(e['ext'],k,'custom.'+v[8:]); report.append(f'line {e["line"]}: {k} staging.* -> custom.*')
  a=attrs(e['ext']); tid=a.get('tvg-id',''); cid=a.get('channel-id','')
  if e['group']==BACKUP:
   p=prim.get(norm(n))
   if not tid or not cid:
    if p:
     pa=attrs(p['ext']); v=pa.get('tvg-id') or pa.get('channel-id')
     if v:
      e['ext']=setv(setv(e['ext'],'tvg-id',v),'channel-id',v); report.append(f'line {e["line"]}: Backup identity inherited from primary {v}')
    else:
     v=tid or cid or slug(n)
     e['ext']=setv(setv(e['ext'],'tvg-id',v),'channel-id',v); orphans.append(e)
   e['ext']=delattr(e['ext'],'tvg-chno')
  a=attrs(e['ext'])
  if a.get('tvg-country','').upper()=='UK': e['ext']=setv(e['ext'],'tvg-country','GB'); report.append(f'line {e["line"]}: UK -> GB')
  if n.casefold()=='ntv (malyalam)': e['ext']=settitle(setv(e['ext'],'tvg-name','NTV (Malayalam)'),'NTV (Malayalam)'); report.append(f'line {e["line"]}: Malayalam spelling fixed')
  low=u.lower()
  if 'dfsdfsdf' in low or re.search(r'^https?://(?:[^/]+\.)?dvltv\.cc/play(?:/|$)',u,re.I): quarantine.append((e,'malformed/blocked endpoint')); continue
  if expiry(u) and expiry(u)<time.time(): quarantine.append((e,'expired token')); continue
  if cred(u): private.append((e,'credential-bearing URL')); continue
  if n.casefold()=='zoom music' and ('dai.google.com' in low or 'doubleclick.net' in low): quarantine.append((e,'volatile ad-insertion URL')); continue
  key=u.strip().lower()
  if key and key in seen: quarantine.append((e,'duplicate stream URL')); continue
  if key: seen.add(key)
  out.append(e)
 return out,private,quarantine,orphans

def render(header,entries):
 lines=list(header)
 for e in entries: lines += e['pre']+[e['ext']]+e['opts']+[e['url']]
 return '\n'.join(lines).rstrip()+'\n'

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('input'); ap.add_argument('--outdir',default='fixed_output'); ap.add_argument('--epg'); args=ap.parse_args()
 src=Path(args.input); out=Path(args.outdir); out.mkdir(parents=True,exist_ok=True); (out/'reports').mkdir(exist_ok=True)
 header,entries=parse(src.read_text(encoding='utf-8',errors='replace')); report=[]
 public,private,quarantine,orphans=fix(entries,report)
 (out/f'{src.stem}.fixed.m3u').write_text(render(header,public),encoding='utf-8')
 if private: (out/f'{src.stem}.private.m3u').write_text(render(header,[e for e,_ in private]),encoding='utf-8')
 if quarantine: (out/f'{src.stem}.quarantine.m3u').write_text(render(header,[e for e,_ in quarantine]),encoding='utf-8')
 with (out/'reports'/'orphans.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f); w.writerow(['line','name','tvg_id','url']); [w.writerow([e['line'],e['name'],attrs(e['ext']).get('tvg-id',''),e['url']]) for e in orphans]
 (out/'reports'/'fix-report.md').write_text('# IPTV playlist fix report\n\n'+'\n'.join('- '+x for x in report)+f'\n\nInput: {len(entries)} entries\nPublic: {len(public)}\nPrivate: {len(private)}\nQuarantine: {len(quarantine)}\nOrphans: {len(orphans)}\n',encoding='utf-8')
 print(f'Input={len(entries)} Public={len(public)} Private={len(private)} Quarantine={len(quarantine)} Orphans={len(orphans)}')

if __name__=='__main__': main()
