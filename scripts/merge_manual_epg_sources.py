#!/usr/bin/env python3
"""Merge narrowly verified direct XMLTV sources into epg/epg.xml.

Only explicit channel-ID mappings are accepted; no fuzzy name matching.
Current verified Bangladesh additions:
  ATN Bangla -> epg.pw channel 9199
  NTV        -> epg.pw channel 9374
"""
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET
import copy

TARGET=Path('epg/epg.xml')
SOURCES={
 'ATNBangla.bd':'https://epg.pw/api/epg.xml?channel_id=9199',
 'NTV.bd':'https://epg.pw/api/epg.xml?channel_id=9374',
}
UPSTREAM={'ATNBangla.bd':'9199','NTV.bd':'9374'}

def fetch(url):
 req=urllib.request.Request(url,headers={'User-Agent':'BDIX-IPTV-EPG/1.0'})
 with urllib.request.urlopen(req,timeout=30) as r: return r.read()

def main():
 if not TARGET.exists(): raise SystemExit('epg/epg.xml not found')
 root=ET.parse(TARGET).getroot()
 existing_channels={c.attrib.get('id') for c in root.findall('channel')}
 existing_programmes={(p.attrib.get('channel'),p.attrib.get('start'),p.attrib.get('stop'),''.join(p.itertext()).strip()) for p in root.findall('programme')}
 added_channels=added_programmes=0
 for target,url in SOURCES.items():
  data=fetch(url); src=ET.fromstring(data)
  source_id=UPSTREAM[target]
  src_channels=[c for c in src.findall('channel') if c.attrib.get('id')==source_id]
  if not src_channels:
   print(f'SKIP {target}: source channel {source_id} not found'); continue
  if target not in existing_channels:
   ch=copy.deepcopy(src_channels[0]); ch.set('id',target); root.insert(0,ch); existing_channels.add(target); added_channels+=1
  for p in src.findall('programme'):
   if p.attrib.get('channel')!=source_id: continue
   p=copy.deepcopy(p); p.set('channel',target)
   key=(p.attrib.get('channel'),p.attrib.get('start'),p.attrib.get('stop'),''.join(p.itertext()).strip())
   if key in existing_programmes: continue
   root.append(p); existing_programmes.add(key); added_programmes+=1
 ET.ElementTree(root).write(TARGET,encoding='utf-8',xml_declaration=True)
 print(f'Manual EPG merge: channels added={added_channels}; programmes added={added_programmes}')
if __name__=='__main__': main()
