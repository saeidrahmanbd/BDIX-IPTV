#!/usr/bin/env python3
import gzip, re, urllib.request, xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

PLAYLIST=Path('IPTV-Playlist.m3u')
REPORT=Path('reports/epg-coverage.md')
SOURCES=[
 'https://epg.pw/xmltv/epg_IN.xml',
 'https://iptv-org.github.io/epg/guides/in/dishtv.in.epg.xml',
 'https://iptv-org.github.io/epg/guides/in/tataplay.com.epg.xml',
 'https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz',
 'https://iptv-epg.org/files/epg-in.xml',
]
ID_MAP={
 'AakaashAath.in':['AakaashAath.in@SD'], 'AlankarTV.in':['AlankarTV.in@SD'],
 'DDTripura.in':['DDTripura.in@SD'], 'KhushbooBangla.in':['KhushbooBangla.in@SD'],
 'RupasiBangla.in':['RupasiBangla.in@SD'],
 'StarJalsha.in':['StarJalsha.in@SD','StarJalsha.in@HD'],
 'ZeeBangla.in':['ZeeBangla.in@SD','ZeeBangla.in@HD'],
 'ColorsBangla.in':['ColorsBangla.in@SD','ColorsBangla.in@HD'],
 'SonyAath.in':['SonyAath.in@SD'], 'DDAssam.in':['DDAssam.in@SD'],
 'DDGoa.in':['DDGoa.in@SD'], 'DDHaryana.in':['DDHaryana.in@SD'],
 'DDHimachalPradesh.in':['DDHimachalPradesh.in@SD'], 'DDJharkhand.in':['DDJharkhand.in@SD'],
 'DDManipur.in':['DDManipur.in@SD'], 'DDMeghalaya.in':['DDMeghalaya.in@SD'],
 'DDNagaland.in':['DDNagaland.in@SD'], 'MTV.in@SD':['MTV.in@SD'],
 'KalaignarMurasu.in':['KalaignarMurasu.in'], 'Goldmines.in':['Goldmines.in@SD'],
 'GoldminesAction.in':['GoldminesAction.in@SD'], 'GoldminesBollywood.in':['GoldminesBollywood.in@SD'],
 'GoldminesMovies.in':['GoldminesMovies.in@SD'], 'MHOneMovies.in':['MHOneMovies.in@SD'],
 'local.bb3c3114fb20':['ColorsBangla.in@HD'],
 'local.285a6aa870f3':['JalshaMovies.in@HD'],
 'local.zee-24-ghanta':['Zee24Ghanta.in@SD'],
 'local.072484feec7':['ZeeBangla.in@HD'],
 'local.5f40adcebbde':['Colors.in@SD','Colors.in@HD'],
 'local.history-tv18':['HistoryTV18.in@SD','HistoryTV18.in@HD'],
 'CartoonNetwork.uk':['CartoonNetwork.in@SD'],
 'CartoonNetworkHDPlus.in':['CartoonNetwork.in@SD'],
 'DiscoveryKids.au':['DiscoveryKids.in@SD'],
 'local.enter-10-bangla':['Enterr10Bangla.in@SD'],
 'local.gold-mines-movie':['GoldminesMovies.in@SD'],
 'SonyEntertainmentTelevision':['SonyEntertainmentTelevision.in@SD','SonyEntertainmentTelevision.in@HD'],
 'ETVMusic.in':['ETVMusic.in@SD'], 'SonySAB.in':['SonySAB.in@SD'],
}
ATTR_RE=re.compile(r'([\w-]+)="([^"]*)"')

def attrs(s): return dict(ATTR_RE.findall(s))
def playlist():
 lines=PLAYLIST.read_text(encoding='utf-8-sig').splitlines(); out=[]
 for i,line in enumerate(lines):
  if line.startswith('#EXTINF:'):
   a=attrs(line); cid=a.get('tvg-id','').strip(); name=a.get('tvg-name','').strip() or line.rsplit(',',1)[-1].strip()
   if cid: out.append((cid,name,a.get('group-title','').strip()))
 return list(dict.fromkeys(out))
def norm(s):
 s=str(s).lower().replace('&amp;','&'); s=re.sub(r'\b(hd|sd|uhd|fhd|tv|channel)\b','',s); return re.sub(r'[^a-z0-9]+','',s)
def aliases(s):
 n=norm(s); out={n}
 for a,b in {'aakaashaath':'aakashaath','aakashath':'aakashaath','sonyaath':'sonyaath','starjalsa':'starjalsha','colorsbanglahd':'colorsbangla','enter10bangla':'enter10bangla','goldminesmovie':'goldminesmovies','sonyentertainmenttv':'sonyentertainmenttelevision'}.items():
  if n==a: out.add(b)
 return out
def base_variants(cid):
 v={cid}; base=cid.split('@',1)[0]; v.add(base)
 if '@' not in cid and re.search(r'\.[a-z]{2}$',cid,re.I): v.add(cid+'@SD'); v.add(cid+'@HD')
 for x in ID_MAP.get(cid,[]): v.add(x)
 return v
def parse_source(url):
 req=urllib.request.Request(url,headers={'User-Agent':'BDIX-IPTV-EPG-Coverage/1.0','Accept':'application/xml,text/xml,application/gzip,*/*'})
 with urllib.request.urlopen(req,timeout=30) as r: data=r.read()
 if url.endswith('.gz') or data[:2]==b'\x1f\x8b': data=gzip.decompress(data)
 ids=set(); names=defaultdict(set); future=set(); now=datetime.now(timezone.utc).timestamp()
 for ev,elem in ET.iterparse(__import__('io').BytesIO(data),events=('end',)):
  if elem.tag=='channel':
   cid=elem.attrib.get('id','').strip()
   if cid:
    ids.add(cid)
    for dn in elem.findall('display-name'):
     if dn.text: names[norm(dn.text)].add(cid)
  elif elem.tag=='programme':
   cid=elem.attrib.get('channel','').strip(); stop=elem.attrib.get('stop','')
   m=re.match(r'^(\d{14})\s*([+-]\d{4})?',stop)
   if cid and m:
    try:
     raw=m.group(1); dt=datetime.strptime(raw,'%Y%m%d%H%M%S').replace(tzinfo=timezone.utc)
     if m.group(2):
      off=m.group(2); sign=1 if off[0]=='+' else -1; minutes=int(off[1:3])*60+int(off[3:5]); dt=dt.replace(tzinfo=timezone(sign*__import__('datetime').timedelta(minutes=minutes)))
     if dt.timestamp()>now: future.add(cid)
    except Exception: pass
   elem.clear()
 return ids,names,future
def main():
 channels=playlist(); merged_ids=set(); merged_names=defaultdict(set); merged_future=set(); source_ok=[]; source_fail=[]
 for src in SOURCES:
  try:
   ids,names,future=parse_source(src); merged_ids|=ids; merged_future|=future
   for k,v in names.items(): merged_names[k]|=v
   source_ok.append((src,len(ids),len(future)))
  except Exception as e: source_fail.append((src,str(e)[:180]))
 exact=[]; alias=[]; missing=[]
 for cid,name,group in channels:
  direct=bool(base_variants(cid)&merged_ids) or cid in merged_ids
  if direct: exact.append((cid,name,group)) ; continue
  name_match=False
  for k in aliases(name):
   if merged_names.get(k): name_match=True; break
  if not name_match and ID_MAP.get(cid): name_match=bool(set(ID_MAP[cid])&merged_ids)
  if name_match: alias.append((cid,name,group))
  else: missing.append((cid,name,group))
 future_exact=[x for x in exact if (base_variants(x[0])&merged_future)]
 future_alias=[x for x in alias if any(merged_names.get(k)&merged_future for k in aliases(x[1])) or (set(ID_MAP.get(x[0],[]))&merged_future)]
 REPORT.parent.mkdir(parents=True,exist_ok=True)
 lines=['# EPG Coverage Report','', 'Generated: **'+datetime.now(timezone.utc).isoformat(timespec='seconds')+'**','',
  'This report audits the current playlist against the configured public EPG sources. It identifies the missing channels first; it does not publish or alter the EPG feed.','',
  '## Coverage Summary','',
  '- Playlist channels: **'+str(len(channels))+'**', '- EPG matched: **'+str(len(exact)+len(alias))+'**', '- EPG missing: **'+str(len(missing))+'**',
  '- Exact ID matches: **'+str(len(exact))+'**', '- Alias/name matches: **'+str(len(alias))+'**',
  '- Matched with future programme data: **'+str(len(future_exact)+len(future_alias))+'**',
  '- Matched but no future programme detected: **'+str(len(exact)+len(alias)-len(future_exact)-len(future_alias))+'**','',
  '## Source Status','']
 for src,n,f in source_ok: lines.append('- **OK** — '+src+' — '+str(n)+' channel IDs, '+str(f)+' IDs with future programmes')
 for src,e in source_fail: lines.append('- **FAILED** — '+src+' — '+e)
 lines += ['', '## Missing Channels — Investigation Queue','', 'These are the channels that currently have no direct or safe alias match. Investigate these specifically instead of searching EPG sources blindly.','']
 if missing:
  for cid,name,group in sorted(missing,key=lambda x:(x[2].lower(),x[1].lower())): lines.append('- **'+name+'** — `'+cid+'` — '+(group or 'Uncategorized'))
 else: lines.append('None.')
 lines += ['', '## Match Rules','', '- **Exact:** playlist ID/base/known feed variant is present in an EPG source.', '- **Alias:** verified ID mapping or normalized channel-name mapping found a guide channel.', '- **Missing:** neither direct ID nor safe alias mapping was found.', '- A match is not treated as fully healthy until future programme data is present.','']
 REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print('EPG coverage:',len(channels),'channels;',len(exact),'exact;',len(alias),'alias;',len(missing),'missing')
if __name__=='__main__': main()