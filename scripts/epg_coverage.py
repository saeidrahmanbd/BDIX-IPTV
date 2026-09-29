#!/usr/bin/env python3
import csv, gzip, io, re, urllib.request, xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
PLAYLIST=Path('IPTV-Playlist.m3u'); MAPPING=Path('reports/epg-india-channel-mapping.csv'); REPORT=Path('reports/epg-coverage.md')
SOURCES=['https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz','https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz']
ATTR_RE=re.compile(r'([\\w-]+)="([^"]*)"')
def attrs(s): return dict(ATTR_RE.findall(s))
def playlist():
 lines=PLAYLIST.read_text(encoding='utf-8-sig').splitlines(); out=[]; cur=None
 for line in lines:
  if line.startswith('#EXTINF:'):
   a=attrs(line)
   cur={'tvg_id':a.get('tvg-id','').strip(),'name':a.get('tvg-name','').strip() or line.rsplit(',',1)[-1].strip(),'group':a.get('group-title','').strip(),'country':a.get('tvg-country','').strip().upper()}
  elif cur and line.strip() and not line.startswith('#'):
   if cur['group'] not in ('Backup','Not Playing'):
    is_india=(cur['group'].startswith('Indian') or cur['country']=='IN' or re.search(r'\.in(?:@|$)',cur['tvg_id'],re.I))
    if is_india: out.append(cur)
   cur=None
 return list({(x['group'],x['tvg_id'],x['name']):x for x in out}.values())

def norm_name(s):
 return re.sub(r'[^a-z0-9]+','',re.sub(r'\b(hd|sd|uhd|fhd|tv|channel)\b','',str(s).lower()))
def norm_id(s):
 return re.sub(r'[^a-z0-9]+','',re.sub(r'@(?:sd|hd|uhd|fhd)
def parse_source(url):
 req=urllib.request.Request(url,headers={'User-Agent':'BDIX-IPTV-EPG-Coverage/2.0','Accept':'application/xml,text/xml,application/gzip,*/*'})
 with urllib.request.urlopen(req,timeout=60) as r: data=r.read()
 if url.endswith('.gz') or data[:2]==b'\x1f\x8b': data=gzip.decompress(data)
 ids=set(); future=set(); counts=defaultdict(int); names=defaultdict(set); now=datetime.now(timezone.utc)
 for _,elem in ET.iterparse(io.BytesIO(data),events=('end',)):
  if elem.tag=='channel':
   cid=elem.attrib.get('id','').strip()
   if cid:
    ids.add(cid)
    for dn in elem.findall('display-name'):
     if dn.text: names[norm_name(dn.text)].add(cid)
  elif elem.tag=='programme':
   cid=elem.attrib.get('channel','').strip()
   if cid:
    counts[cid]+=1
    for stamp in (elem.attrib.get('start',''),elem.attrib.get('stop','')):
     m=re.match(r'^(\d{14})\s*([+-]\d{4})?',stamp)
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
 return ids,future,counts,names
def main():
 channels=playlist(); mapping={}
 if MAPPING.exists():
  for r in csv.DictReader(MAPPING.open(encoding='utf-8-sig')):
   if r.get('tvg_id') and r.get('status')=='MAPPED':
    mapping.setdefault(r['tvg_id'],[]).extend(x.strip() for x in r.get('epg_id','').split('|') if x.strip())
 source_data=[]; source_status=[]
 for src in SOURCES:
  try:
   parsed=parse_source(src); source_data.append(parsed)
   ids,future,counts,names=parsed
   source_status.append((src,'OK',len(ids),len(future),sum(counts.values()),''))
  except Exception as e:
   source_data.append((set(),set(),defaultdict(int),defaultdict(set)))
   source_status.append((src,'FAILED',0,0,0,str(e)[:180]))
 rows=[]
 for ch in channels:
  candidates=list(mapping.get(ch['tvg_id'],[]))+[ch['tvg_id'],re.sub(r'@[^.]+$','',ch['tvg_id'])]
  candidates=list(dict.fromkeys(x for x in candidates if x))
  normalized_candidates={norm_id(x) for x in candidates}
  name_key=norm_name(ch['name']); hits=[]; hit_sources=set(); total_rows=0; has_future=False
  for src,(ids,future,counts,names) in zip(SOURCES,source_data):
   src_hits=[x for x in candidates if x in ids]
   if not src_hits: src_hits=[x for x in ids if norm_id(x) in normalized_candidates]
   if not src_hits: src_hits=list(names.get(name_key,set()))
   if src_hits:
    hit_sources.add(src)
    for x in src_hits:
     if x not in hits: hits.append(x)
     total_rows+=counts.get(x,0)
     if x in future: has_future=True
  status='LIVE EPG' if has_future else ('EPG FOUND' if total_rows else ('NO PROGRAMME DATA' if hits else 'NO GUIDE HIT'))
  rows.append({**ch,'epg_id':' | '.join(hits[:8]),'sources':sorted(hit_sources),'status':status,'programme_rows':total_rows})
 live=[r for r in rows if r['status']=='LIVE EPG']; found=[r for r in rows if r['status']=='EPG FOUND']; no_rows=[r for r in rows if r['status']=='NO PROGRAMME DATA']; no_source=[r for r in rows if r['status']=='NO GUIDE HIT']
 lines=['# EPG Coverage Report','','Generated: **'+datetime.now(timezone.utc).isoformat(timespec='seconds')+'**','','This report audits every active Indian channel in the playlist against the live IN1 + IN4 India XMLTV guides. Matching uses exact ID, normalized ID/punctuation variants, curated mapping aliases, and normalized display names.','','## Coverage Summary','','- Active Indian channels audited: **'+str(len(rows))+'**','- LIVE EPG (current/future programme): **'+str(len(live))+'**','- EPG FOUND (rows exist, no current/future row): **'+str(len(found))+'**','- NO PROGRAMME DATA: **'+str(len(no_rows))+'**','- NO GUIDE HIT: **'+str(len(no_source))+'**','- Current/future coverage: **'+str(len(live))+'/'+str(len(rows))+' ('+str(round(len(live)/len(rows)*100,1) if rows else 0)+'%)**','','## Source Status','']
 for x in source_status:
  lines.append('- **OK** — '+x[0]+' — '+str(x[2])+' channel IDs, '+str(x[3])+' IDs with current/future rows, '+str(x[4])+' total programme rows' if x[1]=='OK' else '- **FAILED** — '+x[0]+' — '+x[5])
 lines += ['','## Missing / Incomplete Channels','','| Group | Channel | Playlist ID | EPG ID matched | Status | Programme rows |','|---|---|---|---|---|---:|']
 for r in sorted(no_rows+no_source+found,key=lambda z:(z['status'],z['group'],z['name'])):
  lines.append('| '+r['group']+' | '+r['name']+' | '+r['tvg_id']+' | '+r['epg_id']+' | '+r['status']+' | '+str(r['programme_rows'])+' |')
 lines += ['','## Channel-by-Channel Result','','| Group | Channel | Playlist ID | EPG ID matched | Source(s) | Status | Programme rows |','|---|---|---|---|---|---|---:|']
 for r in sorted(rows,key=lambda z:(z['group'],z['name'])):
  lines.append('| '+r['group']+' | '+r['name']+' | '+r['tvg_id']+' | '+r['epg_id']+' | '+(', '.join(r['sources']) if r['sources'] else '-')+' | '+r['status']+' | '+str(r['programme_rows'])+' |')
 REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print('Indian EPG audit:',len(rows),'channels;',len(live),'live;',len(found),'rows-only;',len(no_rows),'no-data;',len(no_source),'no-guide-hit')

if __name__=='__main__': main()
,'',str(s).lower()))

def parse_source(url):
 req=urllib.request.Request(url,headers={'User-Agent':'BDIX-IPTV-EPG-Coverage/2.0','Accept':'application/xml,text/xml,application/gzip,*/*'})
 with urllib.request.urlopen(req,timeout=60) as r: data=r.read()
 if url.endswith('.gz') or data[:2]==b'\x1f\x8b': data=gzip.decompress(data)
 ids=set(); future=set(); counts=defaultdict(int); names=defaultdict(set); now=datetime.now(timezone.utc)
 for _,elem in ET.iterparse(io.BytesIO(data),events=('end',)):
  if elem.tag=='channel':
   cid=elem.attrib.get('id','').strip()
   if cid:
    ids.add(cid)
    for dn in elem.findall('display-name'):
     if dn.text: names[norm_name(dn.text)].add(cid)
  elif elem.tag=='programme':
   cid=elem.attrib.get('channel','').strip()
   if cid:
    counts[cid]+=1
    for stamp in (elem.attrib.get('start',''),elem.attrib.get('stop','')):
     m=re.match(r'^(\d{14})\s*([+-]\d{4})?',stamp)
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
 return ids,future,counts,names
def main():
 channels=playlist(); mapping={}
 if MAPPING.exists():
  for r in csv.DictReader(MAPPING.open(encoding='utf-8-sig')):
   if r.get('tvg_id') and r.get('status')=='MAPPED':
    mapping.setdefault(r['tvg_id'],[]).extend(x.strip() for x in r.get('epg_id','').split('|') if x.strip())
 source_data=[]; source_status=[]
 for src in SOURCES:
  try:
   parsed=parse_source(src); source_data.append(parsed)
   ids,future,counts,names=parsed
   source_status.append((src,'OK',len(ids),len(future),sum(counts.values()),''))
  except Exception as e:
   source_data.append((set(),set(),defaultdict(int),defaultdict(set)))
   source_status.append((src,'FAILED',0,0,0,str(e)[:180]))
 rows=[]
 for ch in channels:
  candidates=list(mapping.get(ch['tvg_id'],[]))+[ch['tvg_id'],re.sub(r'@[^.]+$','',ch['tvg_id'])]
  candidates=list(dict.fromkeys(x for x in candidates if x))
  normalized_candidates={norm_id(x) for x in candidates}
  name_key=norm_name(ch['name']); hits=[]; hit_sources=set(); total_rows=0; has_future=False
  for src,(ids,future,counts,names) in zip(SOURCES,source_data):
   src_hits=[x for x in candidates if x in ids]
   if not src_hits: src_hits=[x for x in ids if norm_id(x) in normalized_candidates]
   if not src_hits: src_hits=list(names.get(name_key,set()))
   if src_hits:
    hit_sources.add(src)
    for x in src_hits:
     if x not in hits: hits.append(x)
     total_rows+=counts.get(x,0)
     if x in future: has_future=True
  status='LIVE EPG' if has_future else ('EPG FOUND' if total_rows else ('NO PROGRAMME DATA' if hits else 'NO GUIDE HIT'))
  rows.append({**ch,'epg_id':' | '.join(hits[:8]),'sources':sorted(hit_sources),'status':status,'programme_rows':total_rows})
 live=[r for r in rows if r['status']=='LIVE EPG']; found=[r for r in rows if r['status']=='EPG FOUND']; no_rows=[r for r in rows if r['status']=='NO PROGRAMME DATA']; no_source=[r for r in rows if r['status']=='NO GUIDE HIT']
 lines=['# EPG Coverage Report','','Generated: **'+datetime.now(timezone.utc).isoformat(timespec='seconds')+'**','','This report audits every active Indian channel in the playlist against the live IN1 + IN4 India XMLTV guides. Matching uses exact ID, normalized ID/punctuation variants, curated mapping aliases, and normalized display names.','','## Coverage Summary','','- Active Indian channels audited: **'+str(len(rows))+'**','- LIVE EPG (current/future programme): **'+str(len(live))+'**','- EPG FOUND (rows exist, no current/future row): **'+str(len(found))+'**','- NO PROGRAMME DATA: **'+str(len(no_rows))+'**','- NO GUIDE HIT: **'+str(len(no_source))+'**','- Current/future coverage: **'+str(len(live))+'/'+str(len(rows))+' ('+str(round(len(live)/len(rows)*100,1) if rows else 0)+'%)**','','## Source Status','']
 for x in source_status:
  lines.append('- **OK** — '+x[0]+' — '+str(x[2])+' channel IDs, '+str(x[3])+' IDs with current/future rows, '+str(x[4])+' total programme rows' if x[1]=='OK' else '- **FAILED** — '+x[0]+' — '+x[5])
 lines += ['','## Missing / Incomplete Channels','','| Group | Channel | Playlist ID | EPG ID matched | Status | Programme rows |','|---|---|---|---|---|---:|']
 for r in sorted(no_rows+no_source+found,key=lambda z:(z['status'],z['group'],z['name'])):
  lines.append('| '+r['group']+' | '+r['name']+' | '+r['tvg_id']+' | '+r['epg_id']+' | '+r['status']+' | '+str(r['programme_rows'])+' |')
 lines += ['','## Channel-by-Channel Result','','| Group | Channel | Playlist ID | EPG ID matched | Source(s) | Status | Programme rows |','|---|---|---|---|---|---|---:|']
 for r in sorted(rows,key=lambda z:(z['group'],z['name'])):
  lines.append('| '+r['group']+' | '+r['name']+' | '+r['tvg_id']+' | '+r['epg_id']+' | '+(', '.join(r['sources']) if r['sources'] else '-')+' | '+r['status']+' | '+str(r['programme_rows'])+' |')
 REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print('Indian EPG audit:',len(rows),'channels;',len(live),'live;',len(found),'rows-only;',len(no_rows),'no-data;',len(no_source),'no-guide-hit')

if __name__=='__main__': main()
