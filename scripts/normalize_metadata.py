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
# All four groups below are review queues. They must not receive primary IDs,
# numbers or primary-only metadata normalization.
EXCLUDE={"Backup","Review","Not Playing","New Channels","New Backups","Adult"}
IDS={
  "Jalsha Movies HD": "Star.Jalsha.Movies.HD.in",
  "Desh TV": "DeshTV.bd",
  "&pictures": "AndPictures.in@SD",
  "Ekamra Cinema": "EkamraCinema.bd",
  "Ekamra Manoranjan": "EkamraManoranjan.bd",
  "Sony Max": "SonyMax.in@SD",
  "Xplor": "AndxplorHD.in",
  "Ekamra Musiq": "EkamraMusiq.bd",
  "Raj Music Telugu": "RajMusicTelugu.in@SD",
  "Zing": "Zing.in@SD",
  "HUM Masala": "HUMMasala.pk",
  "MTV India": "MTVIndia.in@SD",
  "Star Bharat": "StarBharat.in",
  "&Privé HD": "AndpriveHD.in",
  "Al Jazeera": "AlJazeeraEnglish.qa",
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
  "UNITE8.1": "UNITE8.1.in"
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
  "BBC.Earth.": "bbc-earth.png",
  "Boishakhi TV": "boishakhi-tv.png",
  "BTV National": "btv-national-2db28e10.png",
  "Cartoon Network": "cartoon-network.png",
  "CARTOON NETWORK": "cartoon-network.png",
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
  "Jalsha Movies HD": "jalsha-movies-hd.png",
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
  "Sun Bangla": "sun-bangla.png",
  "Deshe Bideshe": "deshe-bideshe.png",
  "Colors MENA": "colors-mena.png",
  "Colors Infinity": "colors-infinity.png",
  "Discovery Science": "discovery-science.png",
  "Discovery Turbo": "discovery-turbo.png",
  "HISTORY TV": "history.png",
  "Nat Geo TV": "national-geographic.png",
  "MTV": "mtv-india-hd-720p.png",
  "Enter10 Bangla": "enterr10-bangla.png"
}
FORCED_LOGOS = {
 "Bollygold": "nh-bollygold-dbedeff9.png",
 "Manoranjan Grand": "manoranjan-grand.png",
 "BTV News": "nvisionbd-verified-btv-news-33c61f1708.jpg",
 "Zee TV": "nvisionbd-verified-zee-tv-2fb6673cf7.svg",
 "Tom and Jerry": "nvisionbd-verified-tom-and-jerry-927bd66719.jpg",
 "Green TV": "nvisionbd-verified-green-tv-fa848f9d71.jpg",
}
ATTR=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
def attrs(s): return dict(ATTR.findall(s))
def split_extinf(line):
    """Split EXTINF metadata from display text without breaking commas in quoted attributes."""
    in_quote = False
    escaped = False
    for i, ch in enumerate(line):
        if ch == '"' and not escaped:
            in_quote = not in_quote
        elif ch == "," and not in_quote:
            return line[:i], line[i + 1:]
        escaped = (ch == "\\") and not escaped
        if ch != "\\": escaped = False
    return line, ""

# Canonical EXTINF attribute order. This is a formatting-only repair: preserve
# every key/value pair, display label, playlist record position and stream URL.
ATTRIBUTE_ORDER = (
    "tvg-id", "tvg-name", "tvg-logo", "tvg-chno",
    "channel-id", "tvg-country", "tvg-language", "group-title",
)

def canonicalize_extinf(line):
    head, display = split_extinf(line)
    duration = re.match(r"^#EXTINF:\S+", head)
    if not duration:
        return line
    matches = list(ATTR.finditer(head))
    if not matches:
        return line
    residual = ATTR.sub("", head[duration.end():]).strip()
    if residual:
        return line
    rank = {key: index for index, key in enumerate(ATTRIBUTE_ORDER)}
    pairs = [(match.group(1), match.group(2), index) for index, match in enumerate(matches)]
    pairs.sort(key=lambda item: (rank.get(item[0], len(rank)), item[2]))
    return duration.group(0) + " " + " ".join(
        f'{key}="{value}"' for key, value, _ in pairs
    ) + "," + display

def id_country(value):
 match=re.search(r"\.([a-z]{2})(?:@|$)",str(value or ""),flags=re.I)
 return match.group(1).upper() if match else None

def norm(s):
 s=str(s or "").lower()
 s=re.sub(r"\[[^]]*\]|\([^)]*\)"," ",s)
 # Jalsha Movies and Jalsha Movies HD are distinct primary channels with
 # different programming. Do not collapse the HD channel into the base name.
 raw_value=re.sub(r"[^a-z0-9]+","",s.replace("&","and"))
 if raw_value == "jalshamovieshd": return raw_value
 s=re.sub(r"\b(?:uhd|fhd|hd|sd|4k|1080p|720p|576p|480p|360p)\b"," ",s,flags=re.I)
 value=re.sub(r"[^a-z0-9]+","",s.replace("&","and"))
 aliases={"ekhonetv":"ekhontv","rocktv":"suriyantv","suriyantvtamil":"suriyantv"}
 return aliases.get(value,value)
def clean(s):
 s=re.sub(r"\s+"," ",re.sub(r"[._]+"," ",str(s or ""))).strip()
 # Preserve the channel name suffix for the separate Jalsha Movies HD service.
 if re.fullmatch(r"jalsha\s+movies\s+hd",s,flags=re.I): return "Jalsha Movies HD"
 # Drop source annotations first; otherwise a trailing geoblock label hides the
 # resolution tag from the normalizer and causes the publication gate to fail.
 s=re.sub(r"\s*\[(?:geo[\s-]?blocked)\]\s*$","",s,flags=re.I)
 s=re.sub(r"\s*\(\s*(?:\d{3,4}p|\d{3,4}i|UHD|FHD|HD\+?|SD)\s*\)\s*$","",s,flags=re.I)
 s=re.sub(r"\s+(?:\d{3,4}p|\d{3,4}i|4k(?:\s+hdr)?|uhd|fhd|hd\+?|sd)\s*$","",s,flags=re.I)
 return s.strip()
CASE={"ATN BANGLA UK":"ATN Bangla UK","SUN BANGLA":"Sun Bangla","Ekhone TV":"Ekhon TV","EKHONE TV":"Ekhon TV","Ekattor Tv":"Ekattor TV","Sony MAX":"Sony Max","Sony AATH":"Sony Aath","Sony Entertainment Television":"Sony Entertainment TV","Love nature":"Love Nature","Jtv Classic":"JTV Classic",
  "JTV BANGLA": "JTV Bangla",
  "VISION 24": "Vision 24",
  "SOLOCALCIO ITALIA": "Solo Calcio Italia",
  "INTROUBLE": "InTrouble","Get factual":"Get Factual"}
def normalize_id(cid):
 return re.sub(r"@SD(?=@ALT1$)","",str(cid or ""),flags=re.I)
def set_attr(m,k,v):
 p=re.compile(rf'{re.escape(k)}="[^"]*"')
 return p.sub(f'{k}="{v}"',m,1) if p.search(m) else m.replace("#EXTINF:-1 ",f'#EXTINF:-1 {k}="{v}" ',1)
lines=P.read_text(encoding="utf-8-sig").replace("\r","").splitlines()
# The category registry is owner-managed structure. Preserve its exact
# existing content and position during routine metadata normalization.
# Other obsolete Playlist Studio directives may be removed, but never synthesize
# or reorder the owner's category registry here.
lines=[l for l in lines if l.strip() and not (
 l.startswith("#PLAYLIST-STUDIO-") and not l.startswith("#PLAYLIST-STUDIO-CATEGORIES:")
)]
# Existing IPTV group membership, category registry and channel numbers are owner-curated.
# Routine normalization may repair supported identity/language/logo metadata only.
rows=[]
for i,l in enumerate(lines):
 if l.startswith("#EXTINF:"):
  a=attrs(l); _, display = split_extinf(l); rows.append({"i":i,"line":l,"a":a,"name":display.strip()})
primary=[r for r in rows if r["a"].get("group-title","").strip() not in EXCLUDE]
byname={}
for r in primary: byname.setdefault(norm(r["a"].get("tvg-name") or r["name"]),r)
stats={"numbers":0,"logos":0,"backups":0}
for r in rows:
 a=r["a"]; g=a.get("group-title","").strip(); m,_ = split_extinf(r["line"]); display=r["name"]
 group = g
 if group == "Adult":
  # Equivalent legacy guard: if g == "Adult":
  # Adult entries are explicitly out of scope: preserve every attribute and
  # their original EXTINF line without metadata, logo, or channel-number edits.
  continue
 if g in {"Review", "Not Playing", "New Channels", "New Backups"}:
  # These are owner-curated quarantine/discovery queues, not alternate copies
  # of an active channel. Never inherit a same-name primary ID or rewrite
  # their identity/metadata during routine normalization.
  continue
 if g not in EXCLUDE:
  # Bengali-language Colors Bangla Cinema remains a primary Indian Bangla channel.
  # Preserve the original ID and stream; maintain the user's language-first group policy.
  if (a.get("tvg-id") or "").casefold() == "colorsbanglacinema.in@sd@colors.bangla.cinema":
   m=set_attr(m,"tvg-name","Colors Bangla Cinema")
   m=set_attr(m,"group-title","Indian Bangla")
   m=set_attr(m,"tvg-language","ben")
   lines[r["i"]]=f"{m},Colors Bangla Cinema"
   continue
  name=CASE.get(clean(a.get("tvg-name") or r["name"]),clean(a.get("tvg-name") or r["name"]))
  cid=normalize_id(a.get("tvg-id") or a.get("channel-id") or IDS.get(name) or "custom."+norm(name))
  m=set_attr(m,"tvg-id",cid); m=set_attr(m,"channel-id",cid); m=set_attr(m,"tvg-name",name)
  forced_logo=FORCED_LOGOS.get(name)
  if forced_logo:
   desired=RAW+forced_logo
   if a.get("tvg-logo") != desired: m=set_attr(m,"tvg-logo",desired); stats["logos"]+=1
  elif not a.get("tvg-logo") and LOGOS.get(name): m=set_attr(m,"tvg-logo",RAW+LOGOS[name]); stats["logos"]+=1
 else:
  key=norm(a.get("tvg-name") or r["name"]); pr=byname.get(key)
  # Same-name channels in different broadcast countries are distinct identities.
  # In particular, the US-distributed Thikana TV must not overwrite the
  # Bangladesh Backup identity merely because their display names match.
  if pr:
   backup_country=(a.get("tvg-country") or id_country(a.get("tvg-id") or a.get("channel-id")) or "").upper()
   primary_country=(pr["a"].get("tvg-country") or id_country(pr["a"].get("tvg-id") or pr["a"].get("channel-id")) or "").upper()
   if backup_country and primary_country and backup_country != primary_country:
    pr=None
  if not pr and key=="jalshamovies": pr=byname.get(norm("Jalsha Movies HD"))
  name=CASE.get(clean((pr["a"].get("tvg-name") or pr["name"]) if pr else (a.get("tvg-name") or r["name"])),clean((pr["a"].get("tvg-name") or pr["name"]) if pr else (a.get("tvg-name") or r["name"])))
  if key=="natgeowild" and not pr: name="Nat Geo Wild"
  if key=="sonybbcearth" and not pr: name="Sony BBC Earth"
  cid=normalize_id((pr["a"].get("tvg-id") if pr else None) or IDS.get(name) or a.get("tvg-id") or "custom."+norm(name))
  m=set_attr(m,"tvg-id",cid); m=set_attr(m,"channel-id",cid); m=set_attr(m,"tvg-name",name); display=name
  logo=FORCED_LOGOS.get(name) or (pr["a"].get("tvg-logo") if pr else None) or LOGOS.get(r["name"]) or LOGOS.get(name)
  if logo:
   logo_url=logo if logo.startswith("http") else RAW+logo
   current_logo=(a.get("tvg-logo") or "").strip()
   if not current_logo or (pr and current_logo != logo_url):
    m=set_attr(m,"tvg-logo",logo_url); stats["logos"]+=1
  stats["backups"]+=1
 # Do not publish empty logo attributes when no verified local asset is available.
 m=re.sub(r'\s+tvg-logo=""(?=\s|$)', "", m)
 lines[r["i"]]=f"{m},{name}"

# Keep the stable playlist section order required by the playlist contract:
# curated categories first, followed by Backup, Review and discovery queues.
preamble=[]
records=[]
cur=None
for line in lines:
 if line.startswith("#EXTINF:"):
  if cur is not None: records.append(cur)
  cur=[line]
 elif cur is not None:
  cur.append(line)
 else:
  preamble.append(line)
if cur is not None: records.append(cur)
def group_of(rec):
 return re.search(r'group-title="([^"]+)"', rec[0]).group(1) if re.search(r'group-title="([^"]+)"', rec[0]) else ""
review_groups={"Review","Not Playing","New Channels","New Backups"}
# Keep the original record sequence exactly as supplied by the owner.
# Metadata normalization must never sort, group, promote or relocate existing rows.
lines=preamble+[line for rec in records for line in rec]
lines = [canonicalize_extinf(line) if line.startswith("#EXTINF:") else line for line in lines]
P.write_text("\n".join(lines)+"\n",encoding="utf-8")
digest=hashlib.sha256(P.read_bytes()).hexdigest()
R.write_text("# Playlist Metadata Normalization\n\n"+f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**\nSource playlist SHA-256: **{digest}**\n\n"+f"- Entries processed: **{len(rows)}**\n- Primary channel numbers added: **{stats['numbers']}**\n- Logo references repaired: **{stats['logos']}**\n- Backup/review entries normalized: **{stats['backups']}**\n",encoding="utf-8")
print(f"Normalization: entries={len(rows)} numbers={stats['numbers']} logos={stats['logos']} backup_entries={stats['backups']}")
