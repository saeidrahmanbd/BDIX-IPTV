#!/usr/bin/env python3
"""Discover only movie and music channels for International-Playlist.m3u.

The content filter applies to every country. News, sports, kids, documentaries,
religious programming, general entertainment, and all other categories are
rejected. Existing canonical playlist rows are preserved; only discovery
queues and the legacy generic International catch-all are policy-cleaned.
Playback is never tested by this script.
"""
from __future__ import annotations
import hashlib,re,unicodedata,urllib.parse,urllib.request
from collections import Counter,defaultdict
from datetime import datetime,timezone
from pathlib import Path
from logo_asset_naming import is_blocked_logo_basename
PLAYLIST=Path("International-Playlist.m3u"); REPORT=Path("reports/international-channel-discovery.md"); LOGOS=Path("logos")
SOURCE_URL="https://iptv-org.github.io/iptv/index.category.m3u"; RAW_BASE="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
COUNTRY_THRESHOLD=5; MAX_NEW_CHANNELS=50; MAX_NEW_BACKUPS=50; MAX_NEW_PER_GROUP=25; MAX_SOURCE_BYTES=50*1024*1024; MAX_LOGO_BYTES=2*1024*1024
FIXED_GROUPS=["Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani"]
TAIL_GROUPS=["Fashion TV","Documentary & Wildlife","Kids","Religious","Sports","Adult","New Channels","New Backup","Backup"]
STAGING_GROUPS=set(); LEGACY_GROUPS={"new channels","new backup","new backups","not playing","international","backup","international movies","international music","test"}
COUNTRY_NAMES={"BD":"Bangladesh","IN":"India","PK":"Pakistan","NP":"Nepal","TH":"Thailand","JP":"Japan","KR":"South Korea","ID":"Indonesia","MY":"Malaysia","PH":"Philippines","VN":"Vietnam","CN":"China","TW":"Taiwan","HK":"Hong Kong","SG":"Singapore","AU":"Australia","NZ":"New Zealand","GB":"United Kingdom","US":"United States","CA":"Canada","MX":"Mexico","BR":"Brazil","AR":"Argentina","CL":"Chile","CO":"Colombia","PE":"Peru","ES":"Spain","PT":"Portugal","FR":"France","DE":"Germany","IT":"Italy","NL":"Netherlands","BE":"Belgium","CH":"Switzerland","AT":"Austria","SE":"Sweden","NO":"Norway","DK":"Denmark","FI":"Finland","IS":"Iceland","IE":"Ireland","PL":"Poland","CZ":"Czech Republic","SK":"Slovakia","HU":"Hungary","RO":"Romania","BG":"Bulgaria","GR":"Greece","TR":"Turkey","RU":"Russia","UA":"Ukraine","IL":"Israel","AE":"United Arab Emirates","SA":"Saudi Arabia","QA":"Qatar","KW":"Kuwait","OM":"Oman","BH":"Bahrain","JO":"Jordan","LB":"Lebanon","EG":"Egypt","MA":"Morocco","DZ":"Algeria","TN":"Tunisia","ZA":"South Africa","NG":"Nigeria","KE":"Kenya","GH":"Ghana","TZ":"Tanzania","UG":"Uganda","ZW":"Zimbabwe","ET":"Ethiopia","LK":"Sri Lanka","MM":"Myanmar","KH":"Cambodia","LA":"Laos","MN":"Mongolia","KZ":"Kazakhstan","UZ":"Uzbekistan","AZ":"Azerbaijan","GE":"Georgia","AM":"Armenia","AL":"Albania","RS":"Serbia","HR":"Croatia","SI":"Slovenia","BA":"Bosnia and Herzegovina","ME":"Montenegro","MK":"North Macedonia","LT":"Lithuania","LV":"Latvia","EE":"Estonia","IR":"Iran","IQ":"Iraq","SY":"Syria","PS":"Palestine","FJ":"Fiji","WS":"Samoa","PG":"Papua New Guinea","BT":"Bhutan","MV":"Maldives"}
ISO_CODES=set(COUNTRY_NAMES); ALIASES={"UK":"GB","EL":"GR"}; ATTR_RE=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NEWS_GROUPS={"news"}; SPORTS_GROUPS={"sport","sports"}; DOC_GROUPS={"documentary","documentaries","wildlife","nature"}; KIDS_GROUPS={"kids","kid","children","childrens"}; RELIGIOUS_GROUPS={"religious","religion","faith"}; MOVIE_GROUPS={"movie","movies","cinema","film","films"}; MUSIC_GROUPS={"music","musics"}
NEWS_NAME_RE=re.compile(r"\b(?:news|headlines?|current affairs|cnn|cnbc|bloomberg|reuters|euronews|france\s*24|al\s*jazeera|msnbc|fox\s*news|sky\s*news|bbc\s*(?:news|world)|abc\s*news|nbc\s*news|dw\s*news|rt\s*news|ndtv|aaj\s*tak|times\s*now|news\s*18|news\s*nation|republic\s*(?:tv|bharat)|india\s*today|tv9|dd\s*news|trt\s*world)\b",re.I)
RELIGIOUS_RE=re.compile(r"\b(?:religious|religion|christian|christ|3abn(?:\s*[-:]?\s*(?:kids|canada|english|french|français|francais|latino|international|proclaim|praise\s*him|russia))?|three\s*angels\s*broadcasting\s*network|gospel|bible|jesus|church|catholic|hindu|hinduism|bhakti|bhakthi|sanatan|sikh|gurbani|jain|buddh(?:a|ist|ism)?|temple|mandir|devotional|aarti|satsang|aastha|prarthana|darshan|worship|sermon|evangelical|zoroastrian|ministry|dharma|krishna|shiva|ganesh|hanuman|bhagwan|vedic|bhagavad|gita|mantra|deity|holy\s*mass|orthodox|shrine)\b",re.I)
ISLAMIC_RE=re.compile(r"\b(?:islam|islamic|muslim|quran|koran|sunnah|sunna|mecca|makkah|madina|madinah|medina|masjid|mosque|azan|adhan|ramadan|hajj|ummah|allah|muhammad|mohammad|madani|iqra|peace\s*tv|kaaba|kabah|huda\s*tv|hidayat\s*tv|takbeer|ahlulbayt|mta\s*(?:international|world|1)|quran\s*kareem|al\s*huda|saudi\s*quran|holy\s*quran)\b",re.I)
BAD_NAME_RE=re.compile(r"\b(?:vod|video\s*on\s*demand|catch[\s-]?up|test|demo|webcam|podcast|radio|timeshift|ppv|pay\s*per\s*view|preview|sample|placeholder|coming\s*soon)\b",re.I)

NEWS_BRAND_RE=re.compile(r"\b(?:channel\s*24|somoy(?:\s*tv)?|jamuna\s*tv|dbc\s*news|ekattor(?:\s*tv)?|atn\s*news|news\s*24|bangla\s*news\s*24|independent\s*tv|ntv\s*news|news\s*18|aaj\s*tak|times\s*now|republic\s*(?:tv|bharat)|india\s*today|dd\s*news)\b",re.I)
KIDS_NAME_RE=re.compile(r"\b(?:kids?|children|cartoon(?:\s*network)?|baby\s*shark|disney\s*(?:junior|jr|channel)|nick(?:elodeon)?\s*(?:jr|junior)?|pogo|pbs\s*kids|toongoggles?|toonami|teletubbies|doraemon|discovery\s*kids|mr\s*bean\s*animated|strawberry\s*shortcake|smurf(?:s)?\s*tv|duck\s*tv|zoo\s*moo|yTV)\b",re.I)
SPORTS_NAME_RE=re.compile(r"\b(?:sports?|espn|bein\s*sports|fox\s*sports|sky\s*sports|star\s*sports|sony\s*sports|ten\s*sports|willow|cricket)\b",re.I)
FASHION_RE=re.compile(r"\bfashion\s*tv\b",re.I)
GENERAL_OUT_OF_SCOPE_RE=re.compile(r"\b(servus\s*tv|star\s*channel|warner\s*(?:channel|tv)|persiana\s*(?:family|iranian|korea|plus)|nile\s*drama|mbc\s*\+?\s*drama|groovy\s*tv|mci\s*television|general\s*entertainment|variety\s*channel)\b",re.I)
DOC_NAME_RE=re.compile(r"\b(?:documentar(?:y|ies)|wildlife|nature|discovery(?:\s*(?:channel|science|turbo|world|family|life))?|national\s*geographic|nat\s*geo|animal\s*planet|bbc\s*earth|history\s*(?:channel|tv)?|smithsonian|travel\s*channel|travelxp|love\s*nature|inwild|inwonder)\b",re.I)
MOVIE_NAME_RE=re.compile(r"\b(?:movies?|cinema|films?|bollywood|aflam|moviesphere|cinevault|cineplex|gravitas\s*movies|24\s*hour\s*(?:free\s*)?movies|star\s*movies|zee\s*cinema|b4u\s*movies|jalsha\s*movies|hallmark\s*movies|film\s*4|filmrise\s*movies|mytime\s*movie|the\s*movie\s*club|hbo(?:\s*(?:2|signature|zone|family|hits|comedy|action))?|cinemax|starz|tcm|turner\s*classic\s*movies|ifc|sundance\s*tv)\b",re.I)
MUSIC_NAME_RE=re.compile(r"\b(?:music|musix|musica|musique|tunes|xite|v2beat|trace\s*(?:urban|latina)|kronehit|cmc\s*tv|eu\s*music|ua\s*music|arabica\s*tv|epic\s*music|totalmusic|vevo|qello\s*concerts|mtv\s*(?:music|hits|80s|90s|live|classic|dance)|vh1\b|now\s*(?:70s|80s|rock)|4music|music\s*box|8xm|9xm|9x\s*(?:jalwa|jhakaas|tashan)|jalwa\s*tv|joo\s*music|joomusic|stingray\s*(?:classic|djazz|remember|today|hits)|zoom\s*music|star\s*music)\b",re.I)
MOVIE_CATEGORY_PARTS={"movie","movies","cinema","film","films","bollywood","aflam","moviesphere","internationalmovies"}
MUSIC_CATEGORY_PARTS={"music","musics","internationalmusic"}
INTERNAL_QUEUE_GROUPS={"newchannels","newbackup","newbackups","backup","backups","notplaying","test"}

def attrs(line): return dict(ATTR_RE.findall(line))
def name_of(block): return (attrs(block[0]).get("tvg-name") or block[0].rsplit(",",1)[-1]).strip()
def url_of(block): return next((x.strip() for x in block[1:] if x.strip().startswith(("http://","https://"))),"")
def parse(text):
 p,b,c=[],[],None
 for line in text.replace("\r","").splitlines():
  if line.startswith("#EXTINF:"):
   if c is not None:b.append(c)
   c=[line]
  elif c is None:p.append(line)
  else:c.append(line)
 if c is not None:b.append(c)
 return p,b
def norm(value):
 value=unicodedata.normalize("NFKD",value or "").casefold(); value="".join(c for c in value if not unicodedata.combining(c)); value=re.sub(r"\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p)\b"," ",value); return re.sub(r"[^a-z0-9]+","",value)
def country_code(a):
 for value in [a.get("tvg-country","")]:
  for item in re.split(r"[;,|/\s]+",value.upper()):
   item=ALIASES.get(item,item)
   if item in ISO_CODES:return item
 ident=(a.get("tvg-id") or a.get("channel-id") or "").casefold(); m=re.search(r"\.([a-z]{2})(?:@[^.]*)?$",ident)
 if m:
  code=ALIASES.get(m.group(1).upper(),m.group(1).upper())
  if code in ISO_CODES:return code
 return "ZZ"
def country_group(code): return COUNTRY_NAMES.get(code,"")
def policy(a,name,allow_legacy_group=False):
 code=country_code(a)
 group_text=(a.get("group-title") or "").strip().casefold()
 group_key=re.sub(r"[^a-z0-9]+","",group_text)
 group_parts=[re.sub(r"[^a-z0-9]+","",part) for part in re.split(r"[;,|/]+",group_text) if part.strip()]
 text=f"{name} {a.get('tvg-name','')} {a.get('tvg-id','')}"
 if FASHION_RE.search(text) and group_key=="fashiontv": return "Fashion TV",None,code

 # Prohibited channel identities/content always take precedence over genre matches.
 if NEWS_NAME_RE.search(text) or NEWS_BRAND_RE.search(text) or "news" in group_parts:
  return None,"news channel is prohibited",code
 if RELIGIOUS_RE.search(text) or ISLAMIC_RE.search(text) or any(x in group_parts for x in {"religious","religion","faith","devotional"}):
  return None,"religious channel is prohibited",code
 if KIDS_NAME_RE.search(text) or any(x in group_parts for x in {"kid","kids","children","childrens","child"}):
  return None,"kids channel is prohibited",code
 if SPORTS_NAME_RE.search(text) or any(x in group_parts for x in {"sport","sports"}):
  return None,"sports channel is prohibited",code
 if DOC_NAME_RE.search(text) or any(x in group_parts for x in {"documentary","documentaries","wildlife","nature"}):
  return None,"documentary/wildlife channel is prohibited",code
 if GENERAL_OUT_OF_SCOPE_RE.search(text): return None,"general entertainment is not a dedicated Movie/Music channel",code

 # When the source has a category, it must be explicitly a Movie or Music
 # category. General/Entertainment/unknown category labels are never overridden
 # by a name match. Queue labels are neutral and use the channel identity instead.
 source_category=bool(group_text) and group_key not in INTERNAL_QUEUE_GROUPS and not (allow_legacy_group and group_key=="international")
 if source_category and any(
     part not in MOVIE_CATEGORY_PARTS and part not in MUSIC_CATEGORY_PARTS
     for part in group_parts
 ):
  return None,"source category is not Movies or Music",code

 content_hint=norm(str(a.get("tvg-content","")))
 movie_match=any(part in MOVIE_CATEGORY_PARTS for part in group_parts) or bool(MOVIE_NAME_RE.search(text)) or content_hint in {"movie","movies","film","films"}
 music_match=any(part in MUSIC_CATEGORY_PARTS for part in group_parts) or bool(MUSIC_NAME_RE.search(text)) or content_hint in {"music","musics"}
 if movie_match and music_match:
  return None,"ambiguous Movie/Music classification",code
 if not movie_match and not music_match:
  return None,"channel is not clearly Movies or Music",code

 # Keep country-oriented group names for the three established core regions,
 # but only after the content has passed the Movie/Music gate.
 if code=="BD":
  return "Bangladesh",None,code
 if code=="PK":
  return "Pakistani",None,code
 if code=="IN":
  return ("Indian Movies" if movie_match else "Indian Music"),None,code
 return ("International Movies" if movie_match else "International Music"),None,code

def safe_url(url):
 try:
  p=urllib.parse.urlsplit(url)
  if p.scheme not in {"http","https"} or not p.hostname or p.username or p.password or p.fragment:return False
  if any(x in p.hostname.casefold() for x in ("workers.dev","pages.dev","corsproxy","streamproxy","localhost")):return False
  bad={"token","auth","authorization","password","passwd","pwd","username","signature","sig","expires","jwt","session"}
  return not any(k.casefold() in bad for k,_ in urllib.parse.parse_qsl(p.query,keep_blank_values=True))
 except ValueError:return False
def slug(value):
 x=unicodedata.normalize("NFKD",value).encode("ascii","ignore").decode().casefold(); x=re.sub(r"[^a-z0-9]+","-",x).strip("-")[:80]; return x or "channel-"+hashlib.sha256(value.encode()).hexdigest()[:10]
def local_logo(a,name):
 target=norm(name)
 for p in LOGOS.rglob("*") if LOGOS.exists() else []:
  if p.is_file() and p.suffix.lower() in {".png",".jpg",".jpeg",".webp",".svg"} and "unused" not in p.parts and not is_blocked_logo_basename(p.name) and norm(p.stem)==target:return RAW_BASE+str(p.relative_to(LOGOS)).replace("\\","/")
 source=(a.get("tvg-logo") or "").strip()
 if not source.startswith(("http://","https://")):return ""
 try:
  req=urllib.request.Request(source,headers={"User-Agent":"BDIX-IPTV-International-Discovery/1.0"})
  with urllib.request.urlopen(req,timeout=15) as r:data=r.read(MAX_LOGO_BYTES+1); typ=(r.headers.get("Content-Type") or "").split(";")[0].lower()
  ext={"image/png":".png","image/jpeg":".jpg","image/webp":".webp","image/svg+xml":".svg"}.get(typ)
  if not data or len(data)>MAX_LOGO_BYTES or not ext:return ""
  d=LOGOS/"international"; d.mkdir(parents=True,exist_ok=True); p=d/(slug(name)+ext)
  if not p.exists():p.write_bytes(data)
  return RAW_BASE+str(p.relative_to(LOGOS)).replace("\\","/")
 except Exception:return ""

def localize_existing_logo(a,name):
 raw=(a.get("tvg-logo") or "").strip()
 if not raw:return ""
 # This legacy entry used a G-Series logo for a differently named stream; do not
 # relabel the mismatched asset as an authentic Drama 24 logo.
 if norm(name)=="drama24":return ""
 if raw.startswith(RAW_BASE):
  rel=urllib.parse.unquote(urllib.parse.urlsplit(raw).path.split("/main/logos/",1)[-1]).lstrip("/")
  path=LOGOS/rel
  if path.is_file() and "unused" not in path.parts and not is_blocked_logo_basename(path.name):return raw
  clean=dict(a);clean.pop("tvg-logo",None)
  return local_logo(clean,name)
 if raw.startswith("logos/"):
  rel=urllib.parse.unquote(raw.split("?",1)[0].split("#",1)[0])
  path=Path(rel)
  if path.is_file() and "unused" not in path.parts and not is_blocked_logo_basename(path.name):
   return RAW_BASE+rel[len("logos/"):].replace("\\","/")
  clean=dict(a);clean.pop("tvg-logo",None)
  return local_logo(clean,name)
 if raw.startswith(("http://","https://")):return local_logo(a,name)
 return ""
def set_logo_attr(line,logo):
 line=re.sub(r'\s+tvg-logo="[^"]*"',"",line)
 if not logo or not logo.startswith(RAW_BASE):return line
 m=re.match(r"^(#EXTINF:-?\d+)(.*)$",line)
 if not m:return line
 return m.group(1)+f' tvg-logo="{logo}"'+m.group(2)
def make_extinf(a,name,group,code,logo,content_kind=""):
 clean=" ".join(name.replace('"',"").split()); ident=(a.get("tvg-id") or a.get("channel-id") or "custom.intl."+slug(clean).replace("-",".")).strip(); fields=[f'tvg-id="{ident}"',f'tvg-name="{clean}"']
 if logo.startswith(RAW_BASE):fields.append(f'tvg-logo="{logo}"')
 if code and code!="ZZ":fields.append(f'tvg-country="{code}"')
 if a.get("tvg-language"):fields.append(f'tvg-language="{a["tvg-language"].replace(chr(34),"")}"')
 fields.append(f'channel-id="{(a.get("channel-id") or ident).replace(chr(34),"")}"'); fields.append(f'group-title="{group}"')
 genre=infer_genre(a,clean)
 if content_kind in {"International Movies","Indian Movies","movie","movies","film","films"}:genre="Movies"
 elif content_kind in {"International Music","Indian Music","music","musics"}:genre="Music"
 if genre:fields.append(f'tvg-content="{genre}"')
 return "#EXTINF:-1 "+" ".join(fields)+","+clean

def set_attr(line,key,value):
 value=str(value or "").replace('"',"").strip()
 pattern=re.compile(r'\b'+re.escape(key)+r'="[^"]*"')
 if pattern.search(line):return pattern.sub(lambda _:f'{key}="{value}"',line,count=1)
 return re.sub(r'^(#EXTINF:-?\d+)',lambda m:m.group(1)+f' {key}="{value}"',line,count=1)
def set_content(line,genre):
 if genre not in {"Movies","Music"}:return line
 return set_attr(line,"tvg-content",genre)
def infer_genre(a,name):
 content=norm(str(a.get("tvg-content","")))
 group_text=(a.get("group-title") or "").strip().casefold()
 group_key=re.sub(r"[^a-z0-9]+","",group_text)
 group_parts=[re.sub(r"[^a-z0-9]+","",part) for part in re.split(r"[;,|/]+",group_text) if part.strip()]
 text=f"{name} {a.get('tvg-name','')} {a.get('tvg-id','')} {a.get('channel-id','')}"
 movie=content in {"movie","movies","film","films"} or any(p in MOVIE_CATEGORY_PARTS for p in group_parts) or bool(MOVIE_NAME_RE.search(text))
 music=content in {"music","musics"} or any(p in MUSIC_CATEGORY_PARTS for p in group_parts) or bool(MUSIC_NAME_RE.search(text))
 if movie==music:return ""
 return "Movies" if movie else "Music"
def special_group(a,name):
 text=f"{name} {a.get('tvg-name','')} {a.get('tvg-id','')} {a.get('channel-id','')}"
 content=norm(str(a.get("tvg-content","")))
 group=norm(str(a.get("group-title","")))
 if content in {"adult","xxx","porn","adultentertainment"} or group=="adult":return "Adult"
 if content in {"kids","kid","children","childrens","cartoon"} or KIDS_NAME_RE.search(text):return "Kids"
 if content in {"sport","sports"} or SPORTS_NAME_RE.search(text):return "Sports"
 if content in {"documentary","documentaries","wildlife","nature"} or DOC_NAME_RE.search(text):return "Documentary & Wildlife"
 if content in {"religious","religion","faith","devotional"} or RELIGIOUS_RE.search(text) or ISLAMIC_RE.search(text):return "Religious"
 return ""
def natural_key(value):return tuple(int(x) if x.isdigit() else x.casefold() for x in re.split(r"(\d+)",value or ""))
def category_registry(groups):
 fixed=set(FIXED_GROUPS); tail=set(TAIL_GROUPS)
 present={g.strip() for g in groups if g and g.strip() not in fixed|tail}
 return FIXED_GROUPS+sorted(present)+TAIL_GROUPS
def counts_toward_country_group(group,code):
 group=(group or "").strip().casefold()
 return group=="new channels" or group==country_group(code).casefold()
def qualified_country_groups(existing_ids, added_ids=None):
 added_ids=added_ids or {}
 groups=set()
 for code in set(existing_ids)|set(added_ids):
  if code in {"BD","IN","PK"} or not country_group(code):continue
  if len(set(existing_ids.get(code,set()))|set(added_ids.get(code,set())))>=COUNTRY_THRESHOLD:
   groups.add(code)
 return groups
def primary_target(base,code,country_groups):
 # BD, IN and PK retain their established regional groups. Other countries
 # only receive a dedicated group after the five-channel threshold is met.
 if code=="BD":return "Bangladesh"
 if code=="PK":return "Pakistani"
 if code=="IN":
  genre=infer_genre({},base)
  if not genre:genre="Movies" if "movie" in str(base).casefold() else "Music"
  return "Indian Movies" if genre=="Movies" else "Indian Music"
 if code in country_groups and country_group(code):return country_group(code)
 return "New Channels"
def main():
 if not PLAYLIST.exists():raise SystemExit("International-Playlist.m3u not found; refusing to create it.")
 req=urllib.request.Request(SOURCE_URL,headers={"User-Agent":"BDIX-IPTV-International-Discovery/1.0"})
 with urllib.request.urlopen(req,timeout=90) as r:raw=r.read(MAX_SOURCE_BYTES+1)
 if not raw or len(raw)>MAX_SOURCE_BYTES:raise SystemExit("Source feed is empty or too large; playlist unchanged.")
 _,source=parse(raw.decode("utf-8-sig","replace")); prefix,existing=parse(PLAYLIST.read_text(encoding="utf-8-sig"))
 if not source:raise SystemExit("Source feed contains no channel records; playlist unchanged.")
 existing_urls={url_of(b).casefold() for b in existing if url_of(b)}
 existing_primary=defaultdict(list); country_primary_ids=defaultdict(set)
 queue_or_nonprimary={"backup","backups","new backup","new backups","not playing","adult","test"}
 for b in existing:
  a=attrs(b[0]); name=name_of(b); key=norm(name); group=a.get("group-title","").strip()
  if group.casefold() not in {"backup","backups","new backup","new backups","not playing","test"} and key:existing_primary[key].append(a)
  code=country_code(a)
  if code in ISO_CODES and counts_toward_country_group(group,code) and group.casefold() not in queue_or_nonprimary:
   ident=(a.get("tvg-id") or a.get("channel-id") or key).strip().casefold()
   if ident:country_primary_ids[code].add(ident)
 candidates=[]; seen=set(); rejected=Counter(); exact_existing=0; exact_source_duplicates=0
 for b in source:
  a=attrs(b[0]); name=name_of(b); url=url_of(b)
  if not name:rejected["missing channel name"]+=1; continue
  if BAD_NAME_RE.search(name):rejected["test/VOD/non-TV name"]+=1; continue
  if not safe_url(url):rejected["unsafe or tokenized URL"]+=1; continue
  if url.casefold() in existing_urls:
   exact_existing+=1; continue
  if url.casefold() in seen:
   exact_source_duplicates+=1; continue
  base,reason,code=policy(a,name)
  if base is None:rejected[reason]+=1; continue
  seen.add(url.casefold()); candidates.append((a,name,url,norm(name),base,code))
 country_groups=qualified_country_groups(country_primary_ids)
 additions=[]; new_rows=[]; backup_rows=[]; per_group=Counter(); per_country=Counter(); added_primary_ids=defaultdict(set); planned={k:list(v) for k,v in existing_primary.items()}
 for a,name,url,key,base,code in candidates:
  if not key:continue
  is_backup=key in planned
  if is_backup:
   if len(backup_rows)>=MAX_NEW_BACKUPS:continue
   target="New Backup"; canonical=planned[key][0]; cname=canonical.get("tvg-name",name).strip(); ccode=country_code(canonical)
  else:
   if len(new_rows)>=MAX_NEW_CHANNELS:continue
   target=primary_target(base,code,country_groups)
   if code in ISO_CODES and code not in {"BD","IN","PK"}:
    if per_country[code]>=MAX_NEW_PER_GROUP:continue
    per_country[code]+=1
   if target!="New Channels" and per_group[target]>=MAX_NEW_PER_GROUP:continue
   canonical=a; cname=name; ccode=code
  logo=local_logo(a,cname)
  if is_backup and canonical.get("tvg-logo","").startswith(RAW_BASE) and not logo:logo=canonical["tvg-logo"]
  additions.append([make_extinf(canonical,cname,target,ccode,logo,base),url])
  if is_backup:backup_rows.append((cname,ccode))
  else:
   new_rows.append((cname,target,ccode))
   per_group[target]+=1
   ident=(a.get("tvg-id") or a.get("channel-id") or key).strip().casefold()
   if ccode in ISO_CODES and counts_toward_country_group(target,ccode) and ident:added_primary_ids[ccode].add(ident)
   planned.setdefault(key,[]).append(attrs(additions[-1][0]))
 # Qualification is based only on actual general primary entries in the playlist
 # plus the entries selected for this run, never every eligible source-feed candidate.
 country_groups=qualified_country_groups(country_primary_ids,added_primary_ids)
 all_blocks=existing+additions; migrated=[]; normalized=[]; filtered_existing=[]
 dynamic_group_to_code={country_group(code).casefold():code for code in ISO_CODES if code not in {"BD","IN","PK"}}
 for b in all_blocks:
  a=attrs(b[0]); name=name_of(b); old=a.get("group-title","").strip(); group=old
  old_key=old.casefold(); code=country_code(a); genre=""
  if FASHION_RE.search(name) and old_key not in {"backup","backups","new backup","new backups"}:
   group="Fashion TV"
  elif old_key in {"backup","backups"}:
   group="Backup"
  elif old_key in {"not playing","test"}:
   group="Backup"
  elif old_key in {"new backup","new backups"}:
   policy_a=dict(a); policy_a["group-title"]="New Channels"
   base,reason,policy_code=policy(policy_a,name)
   genre=infer_genre(policy_a,name)
   if base is None or not genre:
    filtered_existing.append((name,old,reason or "entry is not confidently classifiable as Movies/Music"))
    continue
   group="New Backup"
  elif old_key in {"new channels","international","international movies","international music"}:
   policy_a=dict(a); policy_a["group-title"]="New Channels"
   base,reason,policy_code=policy(policy_a,name,allow_legacy_group=(old_key=="international"))
   genre=infer_genre(policy_a,name)
   if base is None or not genre:
    filtered_existing.append((name,old,reason or "entry is not confidently classifiable as Movies/Music"))
    continue
   group=primary_target(base,policy_code,country_groups)
  elif old_key=="pakistani" or old_key in dynamic_group_to_code:
   policy_a=dict(a); policy_a["group-title"]="New Channels"
   base,reason,policy_code=policy(policy_a,name)
   genre=infer_genre(policy_a,name)
   if base is None or not genre:
    special=special_group(a,name)
    if special:
     group=special
    else:
     filtered_existing.append((name,old,reason or "country groups permit Movies/Music only"))
     continue
   elif old_key=="pakistani":
    # Pakistan is a fixed country group, but every row there must still be
    # explicitly and confidently identified as Movies or Music.
    group="Pakistani"; genre=genre or infer_genre(policy_a,name)
    if not a.get("tvg-country"):b[0]=set_attr(b[0],"tvg-country","PK")
   else:
    group=primary_target(base,policy_code,country_groups)
  if group!=old:
   b[0]=set_attr(b[0],"group-title",group)
   migrated.append((name,old,group))
  if genre:
   b[0]=set_content(b[0],genre)
  normalized.append(b)
 # Recompute qualifying country groups from the cleaned playlist before publication.
 cleaned_ids=defaultdict(set)
 for b in normalized:
  a=attrs(b[0]); name=name_of(b); group=a.get("group-title","").strip(); code=country_code(a)
  if code in ISO_CODES and counts_toward_country_group(group,code):
   ident=(a.get("tvg-id") or a.get("channel-id") or norm(name)).strip().casefold()
   if ident:cleaned_ids[code].add(ident)
 country_groups=qualified_country_groups(cleaned_ids)
 for b in normalized:
  a=attrs(b[0]); name=name_of(b); old=a.get("group-title","").strip(); code=country_code(a)
  if old.casefold() in dynamic_group_to_code and code not in country_groups:
   b[0]=set_attr(b[0],"group-title","New Channels")
   migrated.append((name,old,"New Channels"))
 logo_refs_repaired=0; logo_refs_removed=0
 for b in normalized:
  a=attrs(b[0]); name=name_of(b); old_logo=(a.get("tvg-logo") or "").strip()
  if not old_logo:continue
  new_logo=localize_existing_logo(a,name)
  if new_logo!=old_logo:
   b[0]=set_logo_attr(b[0],new_logo)
   if new_logo:logo_refs_repaired+=1
   else:logo_refs_removed+=1
 present_groups={attrs(b[0]).get("group-title","").strip() for b in normalized}; dynamic=category_registry(present_groups); rank={g.casefold():i for i,g in enumerate(dynamic)}
 normalized.sort(key=lambda b:(rank.get(attrs(b[0]).get("group-title","").strip().casefold(),len(rank)),natural_key(name_of(b)),url_of(b).casefold()))
 header="#PLAYLIST-STUDIO-CATEGORIES:"+str(dynamic).replace("'",'"'); out=[x for x in prefix if not x.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]; idx=next((i+1 for i,x in enumerate(out) if x.startswith("#EXTM3U")),0); out.insert(idx,header)
 for b in normalized:out.extend(b)
 PLAYLIST.write_text("\n".join(out).rstrip()+"\n",encoding="utf-8")
 REPORT.parent.mkdir(parents=True,exist_ok=True); report=["# International Channel Discovery","",f"- Last scan: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}",f"- Source: `{SOURCE_URL}`",f"- Source records parsed: {len(source)}",f"- Existing playlist records: {len(existing)}",
  f"- Existing logo references localized/repaired: {logo_refs_repaired}",
  f"- Existing logo references removed because no safe local asset was available: {logo_refs_removed}",f"- Exact source URLs already in playlist: {exact_existing}",f"- Duplicate URLs within source feed: {exact_source_duplicates}",f"- New eligible source records after URL/policy filtering: {len(candidates)}",f"- Country threshold: {COUNTRY_THRESHOLD} unique primary identities for any retained dynamic country group.","- Automatic discovery is Movie/Music only for every country; News, Sports, Kids, Documentary/Wildlife, Religious, General/Entertainment and all other categories are rejected.","- New alternate streams are staged in New Backup; curated alternates remain in Backup.","- Out-of-scope entries are removed only from discovery queues or the legacy catch-all group.","- Playback was not tested.",f"- New primary channels: {len(new_rows)}",f"- New backup review entries: {len(backup_rows)}",f"- Category migrations: {len(migrated)}",f"- Out-of-scope queue/catch-all entries removed: {len(filtered_existing)}","","## New primary channels",""]
 report += [f"- **{n}** — `{g}` — {c}" for n,g,c in new_rows]; report += ["","## Backup alternates",""]+[f"- **{n}** — {c}" for n,c in backup_rows]; report += ["","## Country Migrations",""]+[f"- **{n}**: `{old}` → `{new}`" for n,old,new in migrated]; report += ["","## Removed out-of-scope existing queue/catch-all entries",""]+[f"- **{n}** — `{g}` — {reason}" for n,g,reason in filtered_existing]; report += ["","## Rejections",""]+[f"- {k}: {v}" for k,v in sorted(rejected.items())]; REPORT.write_text("\n".join(report)+"\n",encoding="utf-8")
 # Show the final assigned group in the report, after promotions/consolidation.
 final_group_by_identity={}
 for b in normalized:
  fa=attrs(b[0]); fg=fa.get("group-title","").strip()
  if fg.casefold() not in {"backup","backups","adult","test","new backup","new backups","new channels","not playing"}:
   final_group_by_identity[(norm(name_of(b)),country_code(fa))]=fg
 new_rows=[(n,final_group_by_identity.get((norm(n),c),g),c) for n,g,c in new_rows]
 print(f"International discovery complete: new={len(new_rows)} new_backup={len(backup_rows)} migrations={len(migrated)} qualifying_country_groups={len(country_groups)}")
if __name__=="__main__":raise SystemExit(main())
