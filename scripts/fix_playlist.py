#!/usr/bin/env python3
"""Safe IPTV-Playlist.m3u fixer.

Stream URL risk is reported, not used as an automatic deletion rule.
Duplicate public stream URLs remain a hard error: only the later duplicate is removed.
"""
import argparse,csv,re,unicodedata
from collections import defaultdict
from pathlib import Path

BACKUP='Backup'
EXP=re.compile(r'[?&~=](?:e|exp|expires)=(\d{10})\b',re.I)

def norm(s):
 s=unicodedata.normalize('NFKD',s or '').encode('ascii','ignore').decode().lower()
 s=re.sub(r'\b(?:hd|uhd|fhd|sd)\b',' ',s)
 return re.sub(r'[^a-z0-9]','',s)

def slug(s):
 return 'custom.'+'.'.join(re.findall(r'[a-z0-9]+',unicodedata.normalize('NFKD',s or '').encode('ascii','ignore').decode().lower()))

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

def risk_flags(url):
 flags=[]
 low=url.casefold()
 if re.search(r'[?&~=](?:e|exp|expires)=\d{10}\b',url,re.I): flags.append('token/expiry parameter')
 if re.search(r'\b(?:username|password|pass|pwd)=',url,re.I) or re.search(r'/iptv/[A-Za-z0-9]{10,}/\d+/',url,re.I): flags.append('credential/account-bound pattern')
 if 'workers.dev' in low: flags.append('worker/proxy URL')
 if 'railway.app' in low: flags.append('proxy URL')
 if re.match(r'https?://\d{1,3}(?:\.\d{1,3}){3}(?::\d+)?(?:/|$)',url,re.I): flags.append('IP-origin URL')
 if url.startswith('http://'): flags.append('HTTP URL')
 if 'dai.google.com' in low or 'doubleclick.net' in low: flags.append('ad-insertion URL')
 return flags

def fix(entries,report):
 prim={}
 for e in entries:
  a=attrs(e['ext']); g=a.get('group-title',''); n=title(e['ext']) or a.get('tvg-name','')
  e['name']=n; e['group']=g
  if g!=BACKUP and a.get('tvg-id'): prim[norm(n)]=e
 out=[]; seen={}; quarantine=[]; orphans=[]; risks=[]
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
     if v: e['ext']=setv(setv(e['ext'],'tvg-id',v),'channel-id',v); report.append(f'line {e["line"]}: Backup identity inherited from primary {v}')
    else:
     v=tid or cid or slug(n); e['ext']=setv(setv(e['ext'],'tvg-id',v),'channel-id',v); orphans.append(e)
   e['ext']=delattr(e['ext'],'tvg-chno')
  a=attrs(e['ext'])
  if a.get('tvg-country','').upper()=='UK': e['ext']=setv(e['ext'],'tvg-country','GB'); report.append(f'line {e["line"]}: UK -> GB')
  if n.casefold()=='ntv (malyalam)': e['ext']=settitle(setv(e['ext'],'tvg-name','NTV (Malayalam)'),'NTV (Malayalam)'); report.append(f'line {e["line"]}: Malayalam spelling fixed')
  low=u.casefold()
  # Confirmed invalid/non-channel endpoints only.
  if 'dfsdfsdf' in low or re.search(r'^https?://(?:[^/]+\.)?dvltv\.cc/play(?:/|$)',u,re.I): quarantine.append((e,'confirmed malformed/blocked endpoint')); continue
  # Keep valid token/proxy/account/IP/HTTP streams. Report them for visibility only.
  rf=risk_flags(u)
  if rf: risks.append((e['line'],n,', '.join(rf)))
  # Exact URL uniqueness is mandatory; query strings remain part of URL identity.
  key=u.strip().casefold()
  if key:
   if key in seen:
    quarantine.append((e,'duplicate stream URL; later duplicate removed from public playlist')); continue
   seen[key]=e
  out.append(e)
 return out,quarantine,orphans,risks

def render(header,entries):
 lines=list(header)
 for e in entries: lines += e['pre']+[e['ext']]+e['opts']+[e['url']]
 return '\n'.join(lines).rstrip()+'\n'

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('input'); ap.add_argument('--outdir',default='fixed_output'); args=ap.parse_args()
 src=Path(args.input); out=Path(args.outdir); out.mkdir(parents=True,exist_ok=True); (out/'reports').mkdir(exist_ok=True)
 header,entries=parse(src.read_text(encoding='utf-8',errors='replace')); report=[]
 public,quarantine,orphans,risks=fix(entries,report)
 urls=[e['url'].strip().casefold() for e in public if e['url'].strip()]
 dupes=sorted({u for u in urls if urls.count(u)>1})
 if dupes: raise RuntimeError(f'Public playlist still contains {len(dupes)} duplicate URLs')
 (out/f'{src.stem}.fixed.m3u').write_text(render(header,public),encoding='utf-8')
 if quarantine: (out/f'{src.stem}.quarantine.m3u').write_text(render(header,[e for e,_ in quarantine]),encoding='utf-8')
 with (out/'reports'/'orphans.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f); w.writerow(['line','name','tvg_id','url']); [w.writerow([e['line'],e['name'],attrs(e['ext']).get('tvg-id',''),e['url']]) for e in orphans]
 with (out/'reports'/'stream-risk.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f); w.writerow(['line','channel','risk']); w.writerows(risks)
 (out/'reports'/'fix-report.md').write_text('# IPTV playlist fix report\n\n'+'\n'.join('- '+x for x in report)+f'\n\nInput: {len(entries)} entries\nPublic: {len(public)}\nQuarantine: {len(quarantine)}\nOrphans: {len(orphans)}\nRisk-flagged: {len(risks)}\nDuplicate public URLs: 0\n\nRisk-flagged URLs are retained in the public playlist; they are not automatic deletion criteria.\n',encoding='utf-8')
 print(f'Input={len(entries)} Public={len(public)} Quarantine={len(quarantine)} Orphans={len(orphans)} RiskFlagged={len(risks)} DuplicatePublicURLs=0')
if __name__=='__main__': main()
