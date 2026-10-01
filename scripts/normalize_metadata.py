#!/usr/bin/env python3
"""Normalize IPTV metadata safely; preserve every stream and review queue."""
from pathlib import Path
import re
P=Path("IPTV-Playlist.m3u"); R=Path("reports/metadata-normalization.md")
RAW="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
EXCLUDE={"Backup","New Backup","New Channels","Not Playing"}
IDS={
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
  "UNITE8.1": "unite8-1.svg",
  "9XM": "9xm.png",
  "A.SPORTS.": "a-sports-5485adff.png",
  "Ananda TV": "ananda-tv.png",
  "ANIMAL PLANET": "animal-planet.png",
  "ANIMAL.PLANET.": "animal-planet.png",
  "Asian TV": "asian-tv.png",
  "ATN Music": "atn-music.png",
  "ATN.BANGLA.": "atn-bangla.png",
  "ATN.NEWS.": "atn-news.png",
  "B4U Kadak": "b4u-kadak.png",
  "Bangla TV": "bangla-tv.png",
  "BBC.Earth.": "bbc-earth.png",
  "Boishakhi TV": "boishakhi-tv.png",
  "BTV National": "btv-national-2db28e10.png",
  "Cartoon Network": "cartoon-network.png",
  "CARTOON NETWORK": "cartoon-network.png",
  "CHANNEL.24.": "channel-24.png",
  "CHANNEL.I.": "channel-i.png",
  "Colors": "colors.png",
  "Colors Bangla": "colors-bangla.png",
  "Colors Bangla Cinema": "colors-bangla-cinema.png",
  "COLORS.BANGLA.": "colors-bangla.png",
  "COLORS.BANGLA.CINEMA": "colors-bangla-cinema.png",
  "COLORS.CINEPLEX.": "colors-cineplex.png",
  "DBC.NEWS.": "dbc-news.png",
  "Deepto TV": "deepto-tv.png",
  "DISCOVERY": "discovery.png",
  "DISCOVERY.": "discovery.png",
  "Duronto TV": "duronto-tv.png",
  "EKATTOR.TV.": "ekattor-tv.png",
  "Ekhon TV": "ekhon-tv.png",
  "ENTER 10 BANGLA": "enterr10-bangla.png",
  "Enter10 Bangla": "enterr10-bangla.png",
  "ENTER10.BANGLA": "enterr10-bangla.png",
  "EURO SPORT HD": "euro-sport-hd.png",
  "G TV": "g-tv.png",
  "Green TV": "green-tv.png",
  "History TV18": "history.png",
  "INDEPENDENT.TV": "independent-tv.png",
  "Jalsha Movies": "jalsha-movies-hd.png",
  "JALSHA MOVIES": "jalsha-movies-hd.png",
  "JALSHA.MOVIES.": "jalsha-movies-hd.png",
  "JAMUNA.TV": "jamuna-tv.png",
  "Maasranga TV": "maasranga-tv.png",
  "MADANI.TV.": "madani-tv.png",
  "Nagorik TV": "nagorik-tv.png",
  "NAGORIK.TV.": "nagorik-tv.png",
  "NATGEO.WILD.": "nat-geo-wild.png",
  "National Geographic": "national-geographic.png",
  "NATIONAL GEOGRAPHIC": "national-geographic.png",
  "NEWS.24": "news-24.png",
  "NTV": "ntv.png",
  "PEACE.TV.BANGLA.": "peace-tv-bangla.png",
  "Pishow Stream 10007": "pishow-stream-10007.svg",
  "POGO": "pogo.png",
  "SANGEET BANGLA": "sangeet-bangla.png",
  "SANGEET.BANGLA": "sangeet-bangla.png",
  "Somoy TV": "somoy-tv.png",
  "SOMOY.TV.": "somoy-tv.png",
  "Sony AATH": "sony-aath.png",
  "SONY AATH": "sony-aath.png",
  "Sony Entertainment TV": "sony-entertainment-tv.png",
  "Sony Sports Ten 3": "sony-sports-ten-3-8653ef22.png",
  "Sony Ten 2": "sony-ten-2.png",
  "SONY YAY": "sony-yay.png",
  "SONY.BBC.EARTH.": "sony-bbc-earth.png",
  "SONY.MAX.": "sony-max.png",
  "SONY.YAY": "sony-yay.png",
  "Star Gold 2": "star-gold-2.png",
  "Star Jalsha": "star-jalsha.png",
  "STAR JALSHA": "star-jalsha.png",
  "Star Movies": "star-movies-2087bb49.png",
  "Star Movies Select": "star-movies-select-37627406.png",
  "Star Sports 2 HD": "star-sports-2.png",
  "STAR.GOLD.": "star-gold.png",
  "STAR.JALSHA.": "star-jalsha.png",
  "STAR.MOVIES.": "star-movies-2087bb49.png",
  "STAR.PLUS.": "star-plus.png",
  "Stingray Stream 101": "stingray-stream-101.svg",
  "Stingray Stream 137": "stingray-stream-137.svg",
  "SUN.BANGLA.": "sun-bangla.png",
  "TLC.": "tlc.png",
  "Travelxp Hindi": "travel-xp.png",
  "Zee Bangla": "zee-bangla.png",
  "ZEE BANGLA": "zee-bangla.png",
  "Zee Bangla Cinema": "zee-bangla-cinema.png",
  "Zee Cinema": "zee-cinema.png",
  "ZEE.BANGLA.": "zee-bangla.png",
  "ZEE.CINEMA.": "zee-cinema.png",
  "ZEE.TV.": "zee-tv.png",
  "Zoom Music": "zoom-music.png",
  "Zoom TV": "zoom-tv.png",
  "Zee TV": "zee-tv.png",
  "Sun Bangla": "sun-bangla.png"
}
ATTR=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
def attrs(s): return dict(ATTR.findall(s))
def norm(s):
 s=str(s or "").lower()
 s=re.sub(r"\[[^]]*\]|\([^)]*\)"," ",s)
 s=re.sub(r"\b(?:uhd|fhd|hd|sd|4k|1080p|720p|576p|480p|360p)\b"," ",s,flags=re.I)
 return re.sub(r"[^a-z0-9]+","",s.replace("&","and"))
def clean(s): return re.sub(r"\s+"," ",re.sub(r"[._]+"," ",str(s or ""))).strip()
def set_attr(m,k,v):
 p=re.compile(rf'{re.escape(k)}="[^"]*"')
 return p.sub(f'{k}="{v}"',m,1) if p.search(m) else m.replace("#EXTINF:-1 ",f'#EXTINF:-1 {k}="{v}" ',1)
lines=P.read_text(encoding="utf-8-sig").replace("\r","").splitlines(); rows=[]
for i,l in enumerate(lines):
 if l.startswith("#EXTINF:"):
  a=attrs(l); rows.append({"i":i,"line":l,"a":a,"name":l.split(",",1)[1] if "," in l else ""})
primary=[r for r in rows if r["a"].get("group-title","").strip() not in EXCLUDE]
byname={}
for r in primary: byname.setdefault(norm(r["a"].get("tvg-name") or r["name"]),r)
used={int(r["a"]["tvg-chno"]) for r in primary if r["a"].get("tvg-chno","").isdigit() and int(r["a"]["tvg-chno"])>0}
missing=[r for r in primary if not r["a"].get("tvg-chno","").isdigit()]
assign={}
for r in missing:
 prev=0; nxt=10**9
 for x in reversed([x for x in primary if x["i"]<r["i"]]):
  if x["a"].get("tvg-chno","").isdigit(): prev=int(x["a"]["tvg-chno"]); break
 for x in [x for x in primary if x["i"]>r["i"]]:
  if x["a"].get("tvg-chno","").isdigit(): nxt=int(x["a"]["tvg-chno"]); break
 c=next((n for n in range(max(1,prev+1),nxt) if n not in used),None)
 if c is None:
  mid=(prev+nxt)/2; pool=[n for n in range(1,max(2000,nxt+500)) if n not in used]; c=min(pool,key=lambda n:(abs(n-mid),n))
 assign[r["i"]]=c; used.add(c)
for r in missing:
 if r["name"]=="Desh TV": assign[r["i"]]=30
 if r["name"]=="Sony Max": assign[r["i"]]=384
stats={"numbers":0,"logos":0,"backups":0}
for r in rows:
 a=r["a"]; g=a.get("group-title","").strip(); m=r["line"]; display=r["name"]
 if g not in EXCLUDE:
  name=a.get("tvg-name") or r["name"]; cid=a.get("tvg-id") or a.get("channel-id") or IDS.get(name) or "custom."+norm(name)
  m=set_attr(m,"tvg-id",cid); m=set_attr(m,"channel-id",cid); m=set_attr(m,"tvg-name",name)
  if not a.get("tvg-logo") and LOGOS.get(name): m=set_attr(m,"tvg-logo",RAW+LOGOS[name]); stats["logos"]+=1
  if r["i"] in assign: m=set_attr(m,"tvg-chno",str(assign[r["i"]])); stats["numbers"]+=1
 else:
  key=norm(a.get("tvg-name") or r["name"]); pr=byname.get(key)
  if not pr and key=="jalshamovies": pr=byname.get(norm("Jalsha Movies HD"))
  name=(pr["a"].get("tvg-name") or pr["name"]) if pr else clean(a.get("tvg-name") or r["name"])
  if key=="natgeowild" and not pr: name="Nat Geo Wild"
  if key=="sonybbcearth" and not pr: name="Sony BBC Earth"
  cid=(pr["a"].get("tvg-id") if pr else None) or IDS.get(name) or a.get("tvg-id") or "custom."+norm(name)
  m=set_attr(m,"tvg-id",cid); m=set_attr(m,"channel-id",cid); m=set_attr(m,"tvg-name",name); display=name
  logo=(pr["a"].get("tvg-logo") if pr else None) or LOGOS.get(r["name"]) or LOGOS.get(name)
  if logo and not a.get("tvg-logo"): set_attr(m,"tvg-logo",logo if logo.startswith("http") else RAW+logo); stats["logos"]+=1
  m=re.sub(r'\s*tvg-chno="[^"]*"',"",m); stats["backups"]+=1
 lines[r["i"]]=f"{m},{display}"
P.write_text("\n".join(lines)+"\n",encoding="utf-8")
R.write_text("# Playlist Metadata Normalization\n\n"+f"- Entries processed: **{len(rows)}**\n- Primary channel numbers added: **{stats['numbers']}**\n- Logo references repaired: **{stats['logos']}**\n- Backup/review entries normalized: **{stats['backups']}**\n",encoding="utf-8")
print(f"Normalization: entries={len(rows)} numbers={stats['numbers']} logos={stats['logos']} backup_entries={stats['backups']}")
