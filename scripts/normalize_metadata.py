#!/usr/bin/env python3
"""Normalize IPTV metadata safely; preserve every stream and review queue."""
from pathlib import Path
import hashlib
from datetime import datetime, timezone
import re
import json
import unicodedata
P=Path("IPTV-Playlist.m3u"); R=Path("reports/metadata-normalization.md")
RAW="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
EXCLUDE={"Backup","Not Playing"}
IDS={
  "Jalsha Movies HD": "Star.Jalsha.Movies.HD.in",
  "Desh TV": "DeshTV.bd",
  "&pictures": "AndPictures.in@SD",
  "Ekamra Cinema": "custom.ekamra.cinema",
  "Ekamra Manoranjan": "custom.ekamra.manoranjan",
  "Sony Max": "SonyMax.in@SD",
  "Xplor": "AndxplorHD.in",
  "Ekamra Musiq": "custom.ekamra.musiq",
  "Raj Music Telugu": "RajMusicTelugu.in@SD",
  "Zing": "Zing.in@SD",
  "HUM Masala": "HUMMasala.pk",
  "MTV India": "MTVIndia.in@SD",
  "Star Bharat": "StarBharat.in",
  "&Privé HD": "AndpriveHD.in",
  "Al Jazeera": "custom.aljazeera.english",
  "AXN": "AXN.in@SD",
  "BBC News": "BBCNews.uk",
  "DW News": "DWNews.de",
  "Geo News": "GeoNews.pk",
  "Lotus TV": "LotusTV.in@SD",
  "MN+": "MoviesNowPlus.in@SD",
  "MNX": "MNX.in@SD",
  "Movies Now": "MoviesNow.in@SD",
  "Movies Now HD": "MoviesNow.in@HD",
  "Romedy Now": "RomedyNow.in@SD",
  "Sony PIX": "SonyPix.in",
  "ETV Bal Bharat": "ETVBalBharat.in@SD",
  "Hungama": "Hungama.in@SD",
  "Nick": "Nickelodeon.in@SD",
  "Nick Jr.": "NickJr.in@SD",
  "Sonic": "Sonic.in@SD",
  "Super Hungama": "SuperHungama.in@SD",
  "PTV Sports": "PTVSports.pk",
  "Sony Sports Ten 4": "SonySportsTen4.in",
  "Sony Sports Ten 5": "SonySportsTen5.in",
  "Star Sports 1": "StarSports1.in@HD",
  "Star Sports 3": "StarSports3.in@SD",
  "Star Sports Select 1": "StarSportsSelect1.in@SD",
  "Star Sports Select 2": "StarSportsSelect2.in@SD",
  "T Sports": "TSports.bd",
  "TBN24": "TBN24.us",
  "Global Punjab": "GlobalPunjab.in",
  "Fashion One": "FashionOne.uk",
  "Tunes 6": "Tunes6.in",
  "Survivor": "Survivor.us",
  "WaterBear": "WaterBear.ch",
  "EMAN TV": "EmanTv.iq",
  "Channel S UK": "ChannelS.uk@679aa9",
  "UNITE8.1": "custom.unite8.1"
}
LOGOS={
  "Desh TV": "desh-tv.png",
  "&pictures": "and-pictures.png",
  "Ekamra Cinema": "ekamra-cinema.png",
  "Ekamra Manoranjan": "ekamra-manoranjan.png",
  "Sony Max": "sony-max.png",
  "Xplor": "and-xplor-hd.svg",
  "Ekamra Musiq": "ekamra-musiq.png",
  "Raj Music Telugu": "raj-music-telugu.png",
  "Zing": "zing.png",
  "HUM Masala": "hum-masala.svg",
  "MTV India": "mtv.png",
  "Star Bharat": "star-bharat.png",
  "&Privé HD": "and-prive-hd.png",
  "Al Jazeera": "al-jazeera.png",
  "AXN": "axn.svg",
  "BBC News": "bbc-news.png",
  "DW News": "dw-news.jpg",
  "Geo News": "geo-news.png",
  "Lotus TV": "lotus-tv.svg",
  "MN+": "mn-plus.jpeg",
  "MNX": "mnx-576p-1964fe6da3.png",
  "Movies Now": "movies-now-hd.png",
  "Movies Now HD": "movies-now-hd.png",
  "Romedy Now": "romedy-now.jpeg",
  "Sony PIX": "sony-pix-hd.png",
  "ETV Bal Bharat": "etv-bal-bharat.png",
  "Hungama": "hungama.png",
  "Nick": "nick.png",
  "Nick Jr.": "nick-jr.png",
  "Sonic": "sonic.png",
  "Super Hungama": "super-hungama.png",
  "PTV Sports": "ptv-sports.png",
  "Sony Sports Ten 4": "sony-sports-ten-4.png",
  "Sony Sports Ten 5": "sony-sports-ten-5.png",
  "Star Sports 1": "star-sports-1.png",
  "Star Sports 3": "star-sports-3.png",
  "Star Sports Select 1": "star-sports-select-1.png",
  "Star Sports Select 2": "star-sports-select-2.png",
  "T Sports": "t-sports.png",
  "TBN24": "tbn24.png",
  "Global Punjab": "global-punjab.png",
  "Fashion One": "fashion-one.png",
  "Tunes 6": "tunes-6.png",
  "Survivor": "survivor.png",
  "WaterBear": "waterbear.png",
  "EMAN TV": "eman-tv.png",
  "Channel S UK": "channel-s-uk.jpg",
}

ATTR_RE=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
def attrs(s): return dict(ATTR_RE.findall(s))
def set_attr(s,k,v):
 p=re.compile(rf'{re.escape(k)}="[^"]*"')
 return p.sub(f'{k}="{v}"',s,1) if p.search(s) else s.replace('#EXTINF:-1 ',f'#EXTINF:-1 {k}="{v}" ',1)
def norm(s): return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',str(s or '')).strip()).casefold()
def parse(lines):
 out=[]; cur=[]
 for line in lines:
  if line.startswith('#EXTINF:'):
   if cur: out.append(cur)
   cur=[line]
  elif cur: cur.append(line)
  else: out.append([line])
 if cur: out.append(cur)
 return out

def main():
 if not P.exists(): return
 lines=P.read_text(encoding='utf-8-sig').replace('\r','').splitlines(); records=parse(lines); changed=0
 for r in records:
  if not r or not r[0].startswith('#EXTINF:'): continue
  a=attrs(r[0]); name=a.get('tvg-name') or r[0].rsplit(',',1)[-1]
  target=IDS.get(name) or IDS.get(next((k for k in IDS if norm(k)==norm(name)),''))
  if target and (a.get('tvg-id','').strip().lower().startswith('custom.') or not a.get('tvg-id','').strip()):
   r[0]=set_attr(r[0],'tvg-id',target); r[0]=set_attr(r[0],'channel-id',target); changed+=1
  logo=LOGOS.get(name) or LOGOS.get(next((k for k in LOGOS if norm(k)==norm(name)),''))
  if logo and (not a.get('tvg-logo','').strip() or 'raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/' not in a.get('tvg-logo','')):
   r[0]=set_attr(r[0],'tvg-logo',RAW+logo); changed+=1
 P.write_text('\n'.join(x for r in records for x in r)+'\n',encoding='utf-8')
 print(f'Normalized IPTV metadata: changes={changed}')

if __name__=='__main__': main()
