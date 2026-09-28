#!/usr/bin/env python3
import csv, gzip, io, re, urllib.request, xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
PLAYLIST=Path('IPTV-Playlist.m3u'); MAPPING=Path('reports/epg-india-channel-mapping.csv'); REPORT=Path('reports/epg-coverage.md')
SOURCES=['https://epg.pw/xmltv/epg_IN.xml','https://iptv-org.github.io/epg/guides/in/dishtv.in.epg.xml','https://iptv-org.github.io/epg/guides/in/tataplay.com.epg.xml','https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz','https://iptv-epg.org/files/epg-in.xml']
ATTR_RE=re.compile(r'([\\w-]+)="([^"]*)"')
def attrs(s): return dict(ATTR_RE.findall(s))
def playlist():
 lines=PLAYLIST.read_text(encoding='utf-8-sig').splitlines(); out=[]; cur=None
 for line in lines:
  if line.startswith('#EXTINF:'):
   a=attrs(line); cur=(a.get('tvg-id','').strip(),a.get('tvg-name','').strip() or line.rsplit(',',1)[-1].strip(),a.get('group-title','').strip())
  elif cur and line.strip() and not line.startswith('#'):
   if cur[2] not in ('Backup','Not Playing'): out.append(cur)
   cur=None
 return list(dict.fromkeys(out))
def parse_source(url):
 req=urllib.request.Request(url,headers={'User-Agent':'BDIX-IPTV-EPG-Coverage/2.0','Accept':'application/xml,text/xml,application/gzip,*/*'})
 with urllib.request.urlopen(req,timeout=60) as r: data=r.read()
 if url.endswith('.gz') or data[:2]==b'\x1f\x8b': data=gzip.decompress(data)
 ids=set(); future=set(); counts=defaultdict(int); now=datetime.now(timezone.utc)
 for _,elem in ET.iterparse(io.BytesIO(data),events=('end',)):
  if elem.tag=='channel':
   cid=elem.attrib.get('id','').strip()
   if cid: ids.add(cid)
  elif elem.tag=='programme':
   cid=elem.attrib.get('channel','').strip()
   if cid:
    counts[cid]+=1
    for stamp in (elem.attrib.get('start',''),elem.attrib.get('stop','')):
     m=re.match(r'^(\\d{14})\\s*([+-]\\d{4})?',stamp)
     if not m: continue
     try:
      dt=datetime.strptime(m.group(1),'%Y%m%d%H%M%S'); off=m.group(2)
      if off:
       sign=1 if off[0]=='+' else -1; mins=int(off[1:3])*60+int(off[3:5]); dt=dt.replace(tzinfo=timezone(sign*timedelta(minutes=mins)))
      else: dt=dt.replace(tzinfo=timezone.utc)
      if dt>=now: future.add(cid)
      break
     except Exception: pass
   elem.clear()
 return ids,future,counts
def main():
 channels=playlist(); mapping=list(csv.DictReader(MAPPING.open(encoding='utf-8-sig'))) if MAPPING.exists() else []; mapped=[r for r in mapping if r.get('status')=='MAPPED']
 results={}; source_status=[]
 for src in SOURCES:
  try:
   ids,future,counts=parse_source(src); source_status.append((src,'OK',len(ids),len(future),sum(counts.values()),''))
   for r in mapped:
    candidates=[x.strip() for x in r.get('epg_id','').split('|') if x.strip()]; hits=[x for x in candidates if x in ids]; futures=[x for x in candidates if x in future]
    if hits:
     q=results.setdefault(r['tvg_id'],{'future':set(),'rows':0,'sources':set()}); q['future'].update(futures); q['rows']+=sum(counts.get(x,0) for x in hits); q['sources'].add(src)
  except Exception as e: source_status.append((src,'FAILED',0,0,0,str(e)[:180]))
 live=[]; found=[]; no_rows=[]; no_source=[]
 for r in mapped:
  q=results.get(r['tvg_id'])
  if not q: no_source.append(r)
  elif q['future']: live.append((r,q))
  elif q['rows']>0: found.append((r,q))
  else: no_rows.append((r,q))
 lines=['# EPG Coverage Report','','Generated: **'+datetime.now(timezone.utc).isoformat(timespec='seconds')+'**','','This report checks mapped India EPG channels against actual downloaded XMLTV programme rows. LIVE EPG means at least one programme is current/future. EPG FOUND means rows exist but no current/future row was detected. NO PROGRAMME DATA means the mapped guide ID exists but produced no programme rows. NO GUIDE HIT means the mapped ID was absent from the downloaded guide.','','## Coverage Summary','',
 '- Active playlist channels: **'+str(len(channels))+'**',
 '- India-mapped channels: **'+str(len(mapped))+'**',
 '- LIVE EPG (current/future programme): **'+str(len(live))+'**',
 '- EPG FOUND (rows exist, no current/future row): **'+str(len(found))+'**',
 '- NO PROGRAMME DATA: **'+str(len(no_rows))+'**',
 '- NO GUIDE HIT: **'+str(len(no_source))+'**',
 '- Actual current/future coverage among mapped: **'+str(len(live))+'/'+str(len(mapped))+' ('+str(round(len(live)/len(mapped)*100,1) if mapped else 0)+'%)**','','## Source Status','']
 for x in source_status:
  if x[1]=='OK': lines.append('- **OK** — '+x[0]+' — '+str(x[2])+' channel IDs, '+str(x[3])+' IDs with current/future rows, '+str(x[4])+' total programme rows')
  else: lines.append('- **FAILED** — '+x[0]+' — '+x[5])
 lines += ['','## Channel-by-Channel Result','','| Group | Channel | Playlist ID | EPG ID | Source(s) | Status | Programme rows |','|---|---|---|---|---|---|---:|']
 def row(r,q,status): return '| '+r['group']+' | '+r['channel']+' | '+chr(96)+r['tvg_id']+chr(96)+' | '+chr(96)+r['epg_id']+chr(96)+' | '+(', '.join(sorted(q['sources'])) if q else '-')+' | '+status+' | '+str(q['rows'] if q else 0)+' |'
 for r,q in sorted(live,key=lambda z:(z[0]['group'],z[0]['channel'])): lines.append(row(r,q,'LIVE EPG'))
 for r,q in sorted(found,key=lambda z:(z[0]['group'],z[0]['channel'])): lines.append(row(r,q,'EPG FOUND'))
 for r,q in sorted(no_rows,key=lambda z:(z[0]['group'],z[0]['channel'])): lines.append(row(r,q,'NO PROGRAMME DATA'))
 for r in sorted(no_source,key=lambda z:(z['group'],z['channel'])): lines.append(row(r,None,'NO GUIDE HIT'))
 REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text('\\n'.join(lines)+'\\n',encoding='utf-8')
 print('EPG programme coverage:',len(mapped),'mapped;',len(live),'live/future;',len(found),'rows-only;',len(no_rows),'no-data;',len(no_source),'no-guide-hit')
if __name__=='__main__': main()
