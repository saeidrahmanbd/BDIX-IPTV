#!/usr/bin/env python3
"""Repeatable policy-based cleanup for International-Playlist.m3u."""
from collections import Counter
from pathlib import Path
import json,re,unicodedata
PLAYLIST=Path("International-Playlist.m3u")
RAW_BASE="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
FIXED=["Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani"]
TAIL=["International Movies","International Music","Documentary & Wildlife","Kids","Religious","Sports","Adult","Backups","New Channels","New Backups"]
ATTR_RE=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
P={
"news":re.compile(r"\b(news|newsroom|breaking news|headlines|news 24|24 news|noticias|notizie|nachrichten|haber|khabar|akhbar|nieuws|actualites|informativo|news tv|tv news|cnbc|cnn|bloomberg|reuters|euronews|france 24|al jazeera|msnbc|fox news|sky news|bbc news|abc news|nbc news|dw news|rt news|ndtv|aaj tak|times now|news18|news 18|news nation|republic tv|republic bharat|india today|tv9|dd news|atn news|dbc news|somoy tv|jamuna tv|channel 24|ekattor tv|independent tv|news 21|wion)\b",re.I),
"nonislam":re.compile(r"\b(christian|christ|gospel|bible|church|catholic|evangel(?:ical)?|orthodox|3abn|three angels|hindu|hinduism|bhakti|bhakthi|sanatan|sikh|gurbani|guru bani|jain|buddh(?:a|ist|ism)?|temple|mandir|devotional|aarti|satsang|aastha|prarthana|darshan|worship|sermon|zoroastrian|ministry|dharma|krishna|shiva|ganesh|hanuman|bhagwan|vedic|bhagavad|gita|mantra|deity|holy mass|shrine|jainism)\b",re.I),
"islam":re.compile(r"\b(islam(?:ic)?|muslim|quran|qur'an|koran|sunnah|sunna|mecca|makkah|madina|madinah|medina|masjid|mosque|azan|adhan|ramadan|hajj|ummah|allah|muhammad|mohammad|madani|iqra|peace tv|kaaba|kabah|haramain|huda tv|hidayat tv|takbeer|al huda|saudi quran|quran kareem|qtv|deen tv|madina live)\b",re.I),
"adult":re.compile(r"\b(adult|xxx|porn|erotic|redlight|playboy|penthouse|hustler|brazzers|dorcel|blue hustler|satisfaction|sexy|babes|private tv|desire tv|passion tv|hot adult)\b",re.I),
"kids":re.compile(r"\b(kids?|children|cartoon|baby shark|disney (?:jr|junior|channel|xd)|nick(?:elodeon)?(?: jr| junior|toons)?|pogo|pbs kids|toongoggles?|toonami|teletubbies|doraemon|discovery kids|mr bean animated|strawberry shortcake|smurf(?:s)? tv|duck tv|zoo moo|boomerang|spacetoon|kartoon|lego channel|caillou|jungle book|moonbug|retrocrush|pop kids|tinypop|yugioh|yu-gi-oh)\b",re.I),
"sports":re.compile(r"\b(sports?|football|soccer|basketball|tennis|cricket|golf|racing|motorsport|fight|boxing|wrestling|ufc|esports?|arena sport|league|espn|fox sports|bein sport|sky sports|eurosport|nba|nfl|nhl|mlb|fifa|olympic|horse racing|willow|ten sports|sony sports|star sports|sport tv|sport1|setanta|sportitalia|motorvision)\b",re.I),
"doc":re.compile(r"\b(documentary|documentaries|wildlife|animal planet|nat geo|national geographic|bbc earth|discovery(?: channel| science| turbo| world| life| investigation| family)?|history (?:channel|tv)|smithsonian|nature|love nature|wildearth|wild earth|science channel|exploration|inwild|inwonder|investigation discovery|destination america|american heroes channel|motortrend|powernation|food network|cooking channel)\b",re.I),
"movie":re.compile(r"\b(movie|movies|cinema|film|films|bollywood|hollywood|aflam|cine|cineplex|ciné|action hollywood|thriller|horror|western|star movies|zee cinema|b4u movies|jalsha movies|the movie club|movieplex|fxm|epix|hbo\b|amc\b|ifc\b|turner classic movies|tcm\b|screenpix|cinemax|starz|shemaroo bollywood|goldmines|pictures|movie sphere|moviesphere|filmrise|cinevault|gravitas)\b",re.I),
"music":re.compile(r"\b(music|musix|musica|musique|tunes|xite|v2beat|trace urban|kronehit|cmc tv|eu music|ua music|arabica tv|epic music|totalmusic|vevo|qello concerts|concerts|mtv|vh1|now (?:70s|80s|rock|90s)|4music|music box|8xm|9xm|9x (?:jalwa|jhakaas|tashan)|stingray|zoom music|star music|afrobeats|dance tv|melody|sangeet|ptc music|ary music|joo music|balle balle|fuse|axs tv|california music channel)\b",re.I),
"fake":re.compile(r"^(?:\d+|n/?a|unknown|test|demo|sample|placeholder|new channel|unnamed|no name|not available)$",re.I)}
def attrs(s):return dict(ATTR_RE.findall(s))
def split_info(line):
 q=False;e=False
 for i,ch in enumerate(line):
  if ch=='"' and not e:q=not q
  if ch==',' and not q:return line[:i],line[i+1:]
  if ch=='\\' and not e:e=True
  else:e=False
 return line,""
def normalize(s):
 s=unicodedata.normalize("NFKD",str(s or "")).casefold()
 s="".join(c for c in s if not unicodedata.combining(c))
 s=re.sub(r"\b(?:backup|uhd|fhd|hd|sd|4k|8k|2160[pi]|1080[pi]|720[pi]|576[pi]|480[pi]|360p|240p|144p)\b"," ",s)
 return re.sub(r"[^a-z0-9]+","",s)
def clean(s):
 s=re.sub(r"\s*\[(?:geo[\s-]?blocked|not\s*24/7|test|demo|placeholder|sample)\]\s*"," ",str(s or ""),flags=re.I)
 s=re.sub(r"\s*\((?:\s*(?:2160|1080|720|576|480|360|240|144)\s*[pi]|UHD|FHD|HD(?:\+)?|SD|4K|8K)\s*\)\s*"," ",s,flags=re.I)
 s=re.sub(r"\s+\b(?:2160|1080|720|576|480|360|240|144)\s*[pi]\b"," ",s,flags=re.I)
 return re.sub(r"\s+"," ",s).strip()
def country(a,g):
 if g.strip().casefold()=="bangladesh":return "BD"
 c=(a.get("tvg-country") or "").upper().split(";")[0].strip()
 if c in {"BD","IN","PK"}:return c
 m=re.search(r"\.([a-z]{2})(?:@[^.]*)?$",(a.get("tvg-id") or a.get("channel-id") or "").casefold())
 c=m.group(1).upper() if m else "ZZ"
 return "GB" if c=="UK" else c
def parse(text):
 pre=[];blocks=[];cur=None
 for line in text.replace("\r","").splitlines():
  if line.startswith("#EXTINF:"):
   if cur is not None:blocks.append(cur)
   cur=[line]
  elif cur is None:pre.append(line)
  else:cur.append(line)
 if cur is not None:blocks.append(cur)
 return pre,blocks
def split_ext(line):
 left,disp=split_info(line);a=attrs(left);opts={}
 for opt in ("http-user-agent","http-referrer"):
  if a.get(opt):
   opts[opt]=a[opt];left=re.sub(rf'\s+{opt}="[^"]*"',"",left,count=1)
 a=attrs(left)
 if re.search(r"like Gecko\)|Mobile Safari/|Chrome/\d",disp):
  m=re.search(r",\s*([^,]+)\s*$",disp)
  if m:disp=m.group(1).strip()
 name=clean(a.get("tvg-name") or disp)
 return left,a,disp,opts,name
def classify(a,n,g):
 c=country(a,g);gl=g.casefold();full=f"{n} {a.get('tvg-id','')} {a.get('tvg-name','')}"
 if not n or P["fake"].fullmatch(n) or re.search(r"\b(test channel|demo channel|placeholder|coming soon|stream unavailable|service unavailable|channel not found)\b",n,re.I):return None,"non-real/test channel"
 bd=c=="BD" or gl=="bangladesh"
 if P["news"].search(full) or re.search(r"\b(news|headlines|current affairs|noticias|notizie|nachrichten|newsroom)\b",gl):return ("Bangladesh",None) if bd else (None,"news channel outside Bangladesh")
 rel=bool(re.search(r"\b(?:religious|religion|faith|devotional)\b",gl))
 if P["nonislam"].search(full) or (rel and not P["islam"].search(full)):return None,"non-Islamic religious channel"
 if P["islam"].search(full):return "Religious",None
 if P["adult"].search(full) or gl=="adult":return "Adult",None
 if P["kids"].search(full) or re.search(r"\bkids?\b",gl):return "Kids",None
 if P["sports"].search(full) or re.search(r"\bsports?\b",gl):return "Sports",None
 if P["doc"].search(full) or re.search(r"\b(?:documentary|wildlife)\b",gl):return "Documentary & Wildlife",None
 movie=bool(P["movie"].search(full) or re.search(r"\b(?:movies?|cinema|film|films)\b",gl));music=bool(P["music"].search(full) or re.search(r"\b(?:music|musics)\b",gl))
 if bd:return "Bangladesh",None
 if c=="IN" or gl in {"indian bangla","indian movies","indian music","indian entertainment"}:
  if gl=="indian bangla" or re.search(r"\b(?:bengali|bangla)\b",f"{a.get('tvg-language','')} {n}",re.I):return "Indian Bangla",None
  if movie and music:return None,"ambiguous movie/music identity"
  if movie:return "Indian Movies",None
  if music:return "Indian Music",None
  return "Indian Entertainment",None
 if c=="PK" and (movie or music) and not(movie and music):return "Pakistani",None
 if movie and music:return None,"ambiguous movie/music identity"
 if movie:return "International Movies",None
 if music:return "International Music",None
 return None,"outside Bangladesh/India and not an allowed category"
def local_paths():
 p=Path("logos");return {x.as_posix() for x in p.rglob("*") if x.is_file()} if p.exists() else set()
def rewrite_ext(block,group,paths):
 left,a,disp,opts,name=split_ext(block[0]);logo=(a.get("tvg-logo") or "").strip()
 left=re.sub(r'\s+group-title="[^"]*"',"",left);left=re.sub(r'\s+tvg-name="[^"]*"',"",left);left=re.sub(r'\s+tvg-logo="[^"]*"',"",left);left=re.sub(r'\s+tvg-chno="[^"]*"',"",left)
 rel=""
 if logo.startswith(RAW_BASE):rel=logo[len(RAW_BASE):].split("?")[0].split("#")[0]
 elif logo.startswith("logos/"):rel=logo[6:].split("?")[0].split("#")[0]
 if rel and "logos/"+rel in paths and "unused" not in Path(rel).parts:left+=f' tvg-logo="{logo}"'
 left=left.rstrip()+f' group-title="{group}" tvg-name="{name}"'
 return left+","+name,opts
def main():
 if not PLAYLIST.is_file():raise SystemExit("International playlist missing")
 source=PLAYLIST.read_text(encoding="utf-8-sig");pre,blocks=parse(source);paths=local_paths();removed=Counter();rows=[]
 stats=Counter();stats["before"]=len(blocks)
 for b in blocks:
  left,a,disp,opts,name=split_ext(b[0]);g=a.get("group-title","").strip()
  url=next((x.strip() for x in b[1:] if x.strip().startswith(("http://","https://"))),"")
  if not url:removed["missing stream URL"]+=1;continue
  target,why=classify(a,name,g)
  if why:removed[why]+=1;continue
  if not target:removed["uncategorized"]+=1;continue
  if name!=str(a.get("tvg-name") or disp).strip():stats["names_normalized"]+=1
  if opts and re.search(r"like Gecko\)|Mobile Safari/|Chrome/\d",disp):stats["HTTP_options_repaired"]+=1
  new_ext,new_opts=rewrite_ext(b,target,paths)
  extra=[x for x in b[1:] if x.strip() and not x.strip().startswith(("http://","https://")) and not re.match(r"#EXTVLCOPT:http-(?:user-agent|referrer)=",x.strip(),re.I)]
  rows.append({"group":target,"name":name,"key":normalize(name) or name.casefold(),"url":url,"ext":new_ext,"options":new_opts,"extra":extra})
 group_rank={x:i for i,x in enumerate(FIXED+TAIL)}
 rows.sort(key=lambda r:(group_rank.get(r["group"],999),r["key"],r["url"].casefold()))
 url_seen=set();ids=set();output=[];dups=0;alt=0
 for r in rows:
  u=r["url"].casefold()
  if u in url_seen:dups+=1;continue
  url_seen.add(u);g=r["group"];ident=(g,r["key"])
  if g not in {"Backups","New Channels","New Backups"}:
   if ident in ids:g="Backups";alt+=1
   else:ids.add(ident)
  ext=re.sub(r'\s+group-title="[^"]*"',"",r["ext"]).rstrip()+f' group-title="{g}"'
  if g in {"Backups","New Channels","New Backups"}:ext=re.sub(r'\s+tvg-chno="[^"]*"',"",ext)
  block=[ext,*r["extra"]]
  for opt,val in r["options"].items():block.append(f"#EXTVLCOPT:{opt}={val}")
  block.append(r["url"]);output.append((g,r["name"],r["key"],r["url"],block))
 present={r[0] for r in output};dynamic=sorted(present-set(FIXED)-set(TAIL));order=FIXED+dynamic+TAIL;rank={x:i for i,x in enumerate(order)}
 output.sort(key=lambda r:(rank[r[0]],r[2],r[3].casefold()))
 pre=[x for x in pre if x and not x.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
 ix=next((i+1 for i,x in enumerate(pre) if x.startswith("#EXTM3U")),0);pre.insert(ix,"#PLAYLIST-STUDIO-CATEGORIES:"+json.dumps(order,ensure_ascii=False))
 new="\n".join(pre+[line for r in output for line in r[4]]).rstrip()+"\n"
 _,check=parse(new);urls=[];groups=[];last=None;counts=Counter()
 for b in check:
  a=attrs(b[0]);g=a.get("group-title","").strip();disp=split_info(b[0])[1].strip();u=next((x.strip() for x in b[1:] if x.strip().startswith(("http://","https://"))),"")
  if not g or not u:raise SystemExit(f"Malformed entry: {disp}")
  if g!=last:
   if g in groups:raise SystemExit(f"Split group: {g}")
   groups.append(g);last=g
  if re.search(r"(?:\(\s*(?:2160|1080|720|576|480|360|240|144)\s*[pi]\s*\)|\[Geo-blocked\]|\[Not 24/7\])",disp,re.I):raise SystemExit(f"Unnormalized name: {disp}")
  logo=a.get("tvg-logo","").strip()
  if logo:
   rel=logo[len(RAW_BASE):].split("?")[0].split("#")[0] if logo.startswith(RAW_BASE) else logo[6:] if logo.startswith("logos/") else ""
   if not rel or "logos/"+rel not in paths or "unused" in Path(rel).parts:raise SystemExit(f"Nonlocal logo: {disp}")
  urls.append(u.casefold());counts[g]+=1
 if len(urls)!=len(set(urls)):raise SystemExit("Duplicate stream URLs remain")
 if [g for g in order if g in groups]!=groups:raise SystemExit("Category ordering failed")
 if len(check)<200:raise SystemExit("Unexpectedly small result")
 PLAYLIST.write_text(new,encoding="utf-8")
 print(json.dumps({"before":len(blocks),"after":len(check),"removed":dict(removed),"counts":dict(counts),"names_normalized":stats["names_normalized"],"HTTP_options_repaired":stats["HTTP_options_repaired"],"duplicate_URL_rows_skipped":dups,"additional_channel_streams_moved_to_Backups":alt},ensure_ascii=False))
if __name__=="__main__":main()
