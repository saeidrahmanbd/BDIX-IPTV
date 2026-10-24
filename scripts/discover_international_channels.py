#!/usr/bin/env python3
"""Discover International channels and stage country groups at a five-channel threshold.

Policy:
- A dynamic country group requires five distinct general primary identities in the
  published playlist; source-feed candidates alone do not qualify.
- General channels remain in New Channels while their country is below threshold.
- Existing country-labelled groups below threshold are moved back to New Channels.
- New alternate feeds go directly to Backup.
- Non-Bangladeshi news and non-Islamic religious channels are rejected.
- Movies and music from every country are allowed.
- Playback is never tested by discovery.
"""
from __future__ import annotations
import hashlib,re,unicodedata,urllib.parse,urllib.request
from collections import Counter,defaultdict
from datetime import datetime,timezone
from pathlib import Path
PLAYLIST=Path("International-Playlist.m3u"); REPORT=Path("reports/international-channel-discovery.md"); LOGOS=Path("logos")
SOURCE_URL="https://iptv-org.github.io/iptv/index.category.m3u"; RAW_BASE="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
COUNTRY_THRESHOLD=5; MAX_NEW_CHANNELS=50; MAX_NEW_BACKUPS=50; MAX_NEW_PER_GROUP=25; MAX_SOURCE_BYTES=50*1024*1024; MAX_LOGO_BYTES=2*1024*1024
FIXED_GROUPS=["Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani"]
TAIL_GROUPS=["Adult","International","Documentary & Wildlife","Kids","Religious","Sports","New Channels","Backup"]
STAGING_GROUPS=set(); LEGACY_GROUPS={"new channels","new backup","not playing","international movies","international music","test"}
COUNTRY_NAMES={"BD":"Bangladesh","IN":"India","PK":"Pakistan","NP":"Nepal","TH":"Thailand","JP":"Japan","KR":"South Korea","ID":"Indonesia","MY":"Malaysia","PH":"Philippines","VN":"Vietnam","CN":"China","TW":"Taiwan","HK":"Hong Kong","SG":"Singapore","AU":"Australia","NZ":"New Zealand","GB":"United Kingdom","US":"United States","CA":"Canada","MX":"Mexico","BR":"Brazil","AR":"Argentina","CL":"Chile","CO":"Colombia","PE":"Peru","ES":"Spain","PT":"Portugal","FR":"France","DE":"Germany","IT":"Italy","NL":"Netherlands","BE":"Belgium","CH":"Switzerland","AT":"Austria","SE":"Sweden","NO":"Norway","DK":"Denmark","FI":"Finland","IS":"Iceland","IE":"Ireland","PL":"Poland","CZ":"Czech Republic","SK":"Slovakia","HU":"Hungary","RO":"Romania","BG":"Bulgaria","GR":"Greece","TR":"Turkey","RU":"Russia","UA":"Ukraine","IL":"Israel","AE":"United Arab Emirates","SA":"Saudi Arabia","QA":"Qatar","KW":"Kuwait","OM":"Oman","BH":"Bahrain","JO":"Jordan","LB":"Lebanon","EG":"Egypt","MA":"Morocco","DZ":"Algeria","TN":"Tunisia","ZA":"South Africa","NG":"Nigeria","KE":"Kenya","GH":"Ghana","TZ":"Tanzania","UG":"Uganda","ZW":"Zimbabwe","ET":"Ethiopia","LK":"Sri Lanka","MM":"Myanmar","KH":"Cambodia","LA":"Laos","MN":"Mongolia","KZ":"Kazakhstan","UZ":"Uzbekistan","AZ":"Azerbaijan","GE":"Georgia","AM":"Armenia","AL":"Albania","RS":"Serbia","HR":"Croatia","SI":"Slovenia","BA":"Bosnia and Herzegovina","ME":"Montenegro","MK":"North Macedonia","LT":"Lithuania","LV":"Latvia","EE":"Estonia","IR":"Iran","IQ":"Iraq","SY":"Syria","PS":"Palestine","FJ":"Fiji","WS":"Samoa","PG":"Papua New Guinea","BT":"Bhutan","MV":"Maldives"}
ISO_CODES=set(COUNTRY_NAMES); ALIASES={"UK":"GB","EL":"GR"}; ATTR_RE=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NEWS_GROUPS={"news"}; SPORTS_GROUPS={"sport","sports"}; DOC_GROUPS={"documentary","documentaries","wildlife","nature"}; KIDS_GROUPS={"kids","kid","children","childrens"}; RELIGIOUS_GROUPS={"religious","religion","faith"}; MOVIE_GROUPS={"movie","movies","cinema","film","films"}; MUSIC_GROUPS={"music","musics"}
NEWS_NAME_RE=re.compile(r"\b(?:news|headlines?|current affairs|cnn|cnbc|bloomberg|reuters|euronews|france\s*24|al\s*jazeera|msnbc|fox\s*news|sky\s*news|bbc\s*(?:news|world)|abc\s*news|nbc\s*news|dw\s*news|rt\s*news|ndtv|aaj\s*tak|times\s*now|news\s*18|news\s*nation|republic\s*(?:tv|bharat)|india\s*today|tv9|dd\s*news|trt\s*world)\b",re.I)
RELIGIOUS_RE=re.compile(r"\b(?:religious|religion|christian|christ|3abn(?:\s*[-:]?\s*(?:kids|canada|english|french|français|francais|latino|international|proclaim|praise\s*him|russia))?|three\s*angels\s*broadcasting\s*network|gospel|bible|jesus|church|catholic|hindu|hinduism|bhakti|bhakthi|sanatan|sikh|gurbani|jain|buddh(?:a|ist|ism)?|temple|mandir|devotional|aarti|satsang|aastha|prarthana|darshan|worship|sermon|evangelical|zoroastrian|ministry|dharma|krishna|shiva|ganesh|hanuman|bhagwan|vedic|bhagavad|gita|mantra|deity|holy\s*mass|orthodox|shrine)\b",re.I)
ISLAMIC_RE=re.compile(r"\b(?:islam|islamic|muslim|quran|koran|sunnah|sunna|mecca|makkah|madina|madinah|medina|masjid|mosque|azan|adhan|ramadan|hajj|ummah|allah|muhammad|mohammad|madani|iqra|peace\s*tv|kaaba|kabah|huda\s*tv|hidayat\s*tv|takbeer|ahlulbayt|mta\s*(?:international|world|1)|quran\s*kareem|al\s*huda|saudi\s*quran|holy\s*quran)\b",re.I)
BAD_NAME_RE=re.compile(r"\b(?:vod|video\s*on\s*demand|catch[\s-]?up|test|demo|webcam|podcast|radio|timeshift|ppv|pay\s*per\s*view|preview|sample|placeholder|coming\s*soon)\b",re.I)
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
def policy(a,name):
 code=country_code(a); groups={re.sub(r"[^a-z0-9]+","",x) for x in re.split(r"[;,|/]+",a.get("group-title","").casefold()) if x.strip()}; text=f"{name} {a.get('tvg-name','')} {a.get('tvg-id','')}"
 religious=bool(groups&RELIGIOUS_GROUPS) or bool(RELIGIOUS_RE.search(text)); islamic=bool(ISLAMIC_RE.search(text)); news=bool(groups&NEWS_GROUPS) or bool(NEWS_NAME_RE.search(text))
 if religious and not islamic:return None,"non-Islamic religious channel",code
 if news and code!="BD":return None,"non-Bangladeshi or unverified-country news channel",code
 if religious and islamic:return "Religious",None,code
 if news:return "Bangladesh",None,code
 if groups&KIDS_GROUPS:return "Kids",None,code
 if groups&DOC_GROUPS:return "Documentary & Wildlife",None,code
 if groups&SPORTS_GROUPS:return "Sports",None,code
 if code=="BD":return "Bangladesh",None,code
 if code=="PK":return "Pakistani",None,code
 if code=="IN":
  if groups&MOVIE_GROUPS or re.search(r"\b(?:movie|movies|cinema|film|films)\b",name,re.I):return "Indian Movies",None,code
  if groups&MUSIC_GROUPS or re.search(r"\b(?:music|musix|musica|musique)\b",name,re.I):return "Indian Music",None,code
  if re.search(r"\b(?:bangla|bengali)\b",name,re.I) or "bn" in re.split(r"[;,|/\s]+",a.get("tvg-language","").casefold()):return "Indian Bangla",None,code
  return "Indian Entertainment",None,code
 return "International",None,code
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
  if p.is_file() and p.suffix.lower() in {".png",".jpg",".jpeg",".webp",".svg"} and "unused" not in p.parts and norm(p.stem)==target:return RAW_BASE+str(p.relative_to(LOGOS)).replace("\\","/")
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
def make_extinf(a,name,group,code,logo):
 clean=" ".join(name.replace('"',"").split()); ident=(a.get("tvg-id") or a.get("channel-id") or "custom.intl."+slug(clean).replace("-",".")).strip(); fields=[f'tvg-id="{ident}"',f'tvg-name="{clean}"']
 if logo.startswith(RAW_BASE):fields.append(f'tvg-logo="{logo}"')
 if code and code!="ZZ":fields.append(f'tvg-country="{code}"')
 if a.get("tvg-language"):fields.append(f'tvg-language="{a["tvg-language"].replace(chr(34),"")}"')
 fields.append(f'channel-id="{(a.get("channel-id") or ident).replace(chr(34),"")}"'); fields.append(f'group-title="{group}"'); return "#EXTINF:-1 "+" ".join(fields)+","+clean
def natural_key(value):return tuple(int(x) if x.isdigit() else x.casefold() for x in re.split(r"(\d+)",value or ""))
def category_registry(groups):
 fixed=set(FIXED_GROUPS); tail=set(TAIL_GROUPS)
 present={g.strip() for g in groups if g and g.strip() not in fixed|tail}
 return FIXED_GROUPS+sorted(present)+TAIL_GROUPS
def counts_toward_country_group(group,code):
 group=(group or "").strip().casefold()
 return group in {"new channels","international"} or group==country_group(code).casefold()
def qualified_country_groups(existing_ids, added_ids=None):
 added_ids=added_ids or {}
 groups=set()
 for code in set(existing_ids)|set(added_ids):
  if code in {"BD","IN","PK"} or not country_group(code):continue
  if len(set(existing_ids.get(code,set()))|set(added_ids.get(code,set())))>=COUNTRY_THRESHOLD:
   groups.add(code)
 return groups
def primary_target(base,code,country_groups):
 if code in country_groups and country_group(code):return country_group(code)
 return "New Channels" if base=="International" else base
def main():
 if not PLAYLIST.exists():raise SystemExit("International-Playlist.m3u not found; refusing to create it.")
 req=urllib.request.Request(SOURCE_URL,headers={"User-Agent":"BDIX-IPTV-International-Discovery/1.0"})
 with urllib.request.urlopen(req,timeout=90) as r:raw=r.read(MAX_SOURCE_BYTES+1)
 if not raw or len(raw)>MAX_SOURCE_BYTES:raise SystemExit("Source feed is empty or too large; playlist unchanged.")
 _,source=parse(raw.decode("utf-8-sig","replace")); prefix,existing=parse(PLAYLIST.read_text(encoding="utf-8-sig"))
 if not source:raise SystemExit("Source feed contains no channel records; playlist unchanged.")
 existing_urls={url_of(b).casefold() for b in existing if url_of(b)}
 existing_primary=defaultdict(list); country_primary_ids=defaultdict(set)
 queue_or_nonprimary={"backup","new backup","not playing","adult","test"}
 for b in existing:
  a=attrs(b[0]); name=name_of(b); key=norm(name); group=a.get("group-title","").strip()
  if group.casefold() not in {"backup","new backup","not playing"} and key:existing_primary[key].append(a)
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
   target="Backup"; canonical=planned[key][0]; cname=canonical.get("tvg-name",name).strip(); ccode=country_code(canonical)
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
  additions.append([make_extinf(canonical,cname,target,ccode,logo),url])
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
 all_blocks=existing+additions; migrated=[]; normalized=[]
 for b in all_blocks:
  a=attrs(b[0]); name=name_of(b); old=a.get("group-title","").strip(); group=old
  old_key=old.casefold()
  code=country_code(a)
  if old_key in {"new backup","not playing","test"}:
   group="Backup"
  elif old_key in {"new channels","international movies","international music"}:
   base,reason,policy_code=policy(a,name)
   if policy_code in country_groups:
    group=country_group(policy_code)
   elif old_key=="new channels":
    group=primary_target(base,policy_code,country_groups)
   else:
    group=base or "International"
  elif code in ISO_CODES and code not in {"BD","IN","PK"} and old_key==country_group(code).casefold() and code not in country_groups:
   group="New Channels"
  elif code in country_groups and old_key=="international":
   group=country_group(code)
  if group!=old:
   b[0]=make_extinf(a,name,group,code,a.get("tvg-logo",""))
   migrated.append((name,old,group))
  normalized.append(b)
 present_groups={attrs(b[0]).get("group-title","").strip() for b in normalized}; dynamic=category_registry(present_groups); rank={g.casefold():i for i,g in enumerate(dynamic)}
 normalized.sort(key=lambda b:(rank.get(attrs(b[0]).get("group-title","").strip().casefold(),len(rank)),natural_key(name_of(b)),url_of(b).casefold()))
 header="#PLAYLIST-STUDIO-CATEGORIES:"+str(dynamic).replace("'",'"'); out=[x for x in prefix if not x.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]; idx=next((i+1 for i,x in enumerate(out) if x.startswith("#EXTM3U")),0); out.insert(idx,header)
 for b in normalized:out.extend(b)
 PLAYLIST.write_text("\n".join(out).rstrip()+"\n",encoding="utf-8")
 REPORT.parent.mkdir(parents=True,exist_ok=True); report=["# International Channel Discovery","",f"- Last scan: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}",f"- Source: `{SOURCE_URL}`",f"- Source records parsed: {len(source)}",f"- Existing playlist records: {len(existing)}",f"- Exact source URLs already in playlist: {exact_existing}",f"- Duplicate URLs within source feed: {exact_source_duplicates}",f"- New eligible source records after URL/policy filtering: {len(candidates)}",f"- Country threshold: {COUNTRY_THRESHOLD} unique legitimate primary identities.","- Dynamic country groups require five distinct general primary identities actually present in the playlist; otherwise general channels remain in New Channels.","- New alternate streams go directly to Backup.","- Under-threshold country groups are consolidated into New Channels; qualifying groups are created only from published primary entries.","- Playback was not tested.",f"- New primary channels: {len(new_rows)}",f"- Backup alternates: {len(backup_rows)}",f"- Country migrations: {len(migrated)}","","## New primary channels",""]
 report += [f"- **{n}** — `{g}` — {c}" for n,g,c in new_rows]; report += ["","## Backup alternates",""]+[f"- **{n}** — {c}" for n,c in backup_rows]; report += ["","## Country Migrations",""]+[f"- **{n}**: `{old}` → `{new}`" for n,old,new in migrated]; report += ["","## Rejections",""]+[f"- {k}: {v}" for k,v in sorted(rejected.items())]; REPORT.write_text("\n".join(report)+"\n",encoding="utf-8")
 # Show the final assigned group in the report, after promotions/consolidation.
 final_group_by_identity={}
 for b in normalized:
  fa=attrs(b[0]); fg=fa.get("group-title","").strip()
  if fg.casefold() not in {"backup","adult","test","new backup","not playing"}:
   final_group_by_identity[(norm(name_of(b)),country_code(fa))]=fg
 new_rows=[(n,final_group_by_identity.get((norm(n),c),g),c) for n,g,c in new_rows]
 print(f"International discovery complete: new={len(new_rows)} new_backup={len(backup_rows)} migrations={len(migrated)} qualifying_country_groups={len(country_groups)}")
if __name__=="__main__":raise SystemExit(main())
