#!/usr/bin/env python3
"""Audit and repair International-Playlist.m3u only."""
from pathlib import Path
import json,re,unicodedata,urllib.request,urllib.parse
from difflib import SequenceMatcher

PLAYLIST=Path('International-Playlist.m3u'); LOGOS=Path('logos')
REFERENCE_PLAYLISTS=(Path('IPTV-Playlist.m3u'),Path('BDIX-Playlist.m3u'))
RAW_BASE='https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/'
IPTV_LOGOS='https://iptv-org.github.io/api/logos.json'; IPTV_CHANNELS='https://iptv-org.github.io/api/channels.json'
ORDER=['Bangla','Indian','Pakistani','International','Documentary & Wildlife','Religious','Adult','Backup']; NO_NUMBER={'Backup','Not Playing'}
ATTR_RE=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
BAD={x.casefold() for x in ('generated-fallback-btv-news.png','generated-fallback-channel-1.png','generated-fallback-channel-16.png','generated-fallback-channel-52.png','placeholder-btv-news.png','placeholder-channel-1.png','placeholder-channel-16.png','placeholder-channel-52.png')}

def attrs(s): return dict(ATTR_RE.findall(s))
def set_attr(s,k,v):
 p=re.compile(rf'{re.escape(k)}="[^"]*"'); return p.sub(f'{k}="{v}"',s,1) if p.search(s) else s.replace('#EXTINF:-1 ',f'#EXTINF:-1 {k}="{v}" ',1)
def remove_attr(s,k): return re.sub(rf'\s+{re.escape(k)}="[^"]*"','',s,1)
def name_of(s):
 a=attrs(s); return (a.get('tvg-name') or s.rsplit(',',1)[-1]).strip()
def norm(s):
 s=unicodedata.normalize('NFKD',str(s or '')).casefold(); s=''.join(c for c in s if not unicodedata.combining(c))
 s=re.sub(r'\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|plus)\b',' ',s)
 return re.sub(r'[^a-z0-9]+','',s)
def url_of(b): return next((x.strip() for x in b[1:] if x.strip().startswith(('http://','https://'))),'')
def exact_name_key(value):
 value=unicodedata.normalize('NFKC',str(value or '')).casefold().strip()
 return re.sub(r'\\s+',' ',value)
def build_primary_id_index(texts=None):
 # Reuse an ID only when the exact displayed name maps to one ID across
 # both existing primary playlists. No suffix stripping or fuzzy matching.
 if texts is None:
  texts=[p.read_text(encoding='utf-8-sig') for p in REFERENCE_PLAYLISTS if p.is_file()]
 ids_by_name={}
 excluded={'backup','not playing','not playing...','not playing…','test'}
 for text in texts:
  _,rows=parse(text)
  for block in rows:
   info=block[0]; a=attrs(info)
   if a.get('group-title','').strip().casefold() in excluded: continue
   cid=(a.get('tvg-id') or '').strip()
   key=exact_name_key(name_of(info))
   if cid and key: ids_by_name.setdefault(key,set()).add(cid)
 return {name:next(iter(ids)) for name,ids in ids_by_name.items() if len(ids)==1}
def backfill_exact_tvg_id(info,group,id_by_name):
 a=attrs(info)
 if a.get('tvg-id','').strip() or str(group or '').strip().casefold() in {'backup','not playing','test'}:
  return info,False
 cid=id_by_name.get(exact_name_key(name_of(info)),'')
 if not cid: return info,False
 return set_attr(info,'tvg-id',cid),True
def parse(text):
 pre=[]; blocks=[]; cur=None
 for line in text.replace('\r','').splitlines():
  if line.startswith('#EXTINF:'):
   if cur is not None: blocks.append(cur)
   cur=[line]
  elif cur is None: pre.append(line)
  else: cur.append(line)
 if cur is not None: blocks.append(cur)
 return pre,blocks

def fetch_json(url):
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'BDIX-IPTV-International-Audit/1.0'})
  with urllib.request.urlopen(req,timeout=30) as r: return json.loads(r.read().decode())
 except Exception as e:
  print('Warning:',url,e); return []

def build_iptv_org():
 channels=fetch_json(IPTV_CHANNELS); logos=fetch_json(IPTV_LOGOS)
 ids_by_name={}
 for c in channels if isinstance(channels,list) else []:
  cid=str(c.get('id','')).strip(); n=norm(c.get('name',''))
  if cid and n: ids_by_name.setdefault(n,set()).add(cid)
 best={}
 for x in logos if isinstance(logos,list) else []:
  cid=str(x.get('channel','')).strip(); u=str(x.get('url','')).strip()
  if not cid or not u.startswith('https://') or x.get('in_use') is False: continue
  score=(0 if x.get('format')=='PNG' else 1,0 if 'horizontal' in x.get('tags',[]) else 1,-int(x.get('width') or 0))
  if cid not in best or score<best[cid][0]: best[cid]=(score,u)
 return best,ids_by_name

def safe_local(name):
 target=norm(name)
 if not target:return None
 candidates=[]
 for p in LOGOS.rglob('*'):
  if not p.is_file() or p.suffix.lower() not in {'.png','.jpg','.jpeg','.webp','.svg'} or p.name.casefold() in BAD: continue
  stem=norm(p.stem)
  if stem==target:candidates.append((0,0,p))
  elif stem and (stem in target or target in stem):candidates.append((1,abs(len(stem)-len(target)),p))
 return sorted(candidates,key=lambda x:(x[0],x[1],str(x[2])))[0][2] if candidates else None

def download(src,name):
 try:
  req=urllib.request.Request(src,headers={'User-Agent':'Mozilla/5.0 IPTV-logo-audit'})
  with urllib.request.urlopen(req,timeout=15) as r:data=r.read(2*1024*1024+1); ctype=(r.headers.get('Content-Type') or '').split(';')[0].lower()
  if len(data)>2*1024*1024:return None
  sigs=((b'\x89PNG','.png'),(b'\xff\xd8\xff','.jpg'),(b'RIFF','.webp'),(b'<svg','.svg'),(b'<?xml','.svg'))
  ext=next((e for s,e in sigs if data.lstrip().startswith(s)),None)
  if not ext:ext={"image/png":".png","image/jpeg":".jpg","image/webp":".webp","image/svg+xml":".svg"}.get(ctype)
  if not ext:return None
  p=LOGOS/'international'/f'{norm(name) or "channel"}{ext}'; p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(data); return p
 except Exception:return None

def repair_logo(info,org):
 a=attrs(info); name=name_of(info); old=a.get('tvg-logo','').strip(); p=safe_local(name)
 if not p and old.startswith(('http://','https://')):p=download(old,name)
 if not p:
  candidates=[]
  for k in ('tvg-id','channel-id'):
   cid=a.get(k,'').strip()
   if cid in org[0]:candidates.append(org[0][cid][1])
  for cid in org[1].get(norm(name),set()):
   if cid in org[0]:candidates.append(org[0][cid][1])
  for src in candidates:
   p=download(src,name)
   if p:break
 if not p:return info,False
 desired=RAW_BASE+str(p.relative_to(LOGOS)).replace('\\','/')
 return set_attr(info,'tvg-logo',desired),old!=desired

def fuzzy_group(name,by_name):
 k=norm(name); scored=[]
 if not k:return None
 for cand,g in by_name.items():
  r=SequenceMatcher(None,k,cand).ratio()
  if r>=.96 or (min(len(k),len(cand))>=8 and (k in cand or cand in k) and r>=.90):scored.append((r,g))
 scored.sort(reverse=True)
 return scored[0][1] if scored and (len(scored)==1 or scored[0][0]-scored[1][0]>=.03) else None

def main():
 if not PLAYLIST.exists():raise SystemExit('International-Playlist.m3u not found')
 pre,blocks=parse(PLAYLIST.read_text(encoding='utf-8-sig')); seen=set(); kept=[]; duplicate=malformed=ids_backfilled=0
 id_by_name=build_primary_id_index()
 for b in blocks:
  u=url_of(b)
  if not u:malformed+=1;continue
  if u.casefold() in seen:duplicate+=1;continue
  seen.add(u.casefold()); info=b[0]; a=attrs(info); g=a.get('group-title','').strip()
  if g not in ORDER:info=set_attr(info,'group-title','International');g='International'
  info,id_added=backfill_exact_tvg_id(info,g,id_by_name)
  ids_backfilled+=int(id_added)
  if g in NO_NUMBER and attrs(info).get('tvg-chno'):info=remove_attr(info,'tvg-chno')
  b[0]=info;kept.append(b)
 blocks=kept
 by_id={};by_name={}
 for b in blocks:
  a=attrs(b[0]);g=a.get('group-title','').strip()
  if g=='Backup':continue
  n=norm(name_of(b[0]));
  if n:by_name.setdefault(n,set()).add(g)
  for k in ('tvg-id','channel-id'):
   v=a.get(k,'').strip().casefold()
   if v:by_id.setdefault(v,set()).add(g)
 migrated=orphan=0; orphan_rows=[]
 for b in blocks:
  a=attrs(b[0])
  if a.get('group-title','').strip()!='Backup':continue
  targets=[]
  for k in ('tvg-id','channel-id'):
   v=a.get(k,'').strip().casefold()
   if v and v in by_id:targets += list(by_id[v])
  if not targets:targets += list(by_name.get(norm(name_of(b[0])),set()))
  targets=[x for x in set(targets) if x!='Backup']
  target=targets[0] if len(targets)==1 else fuzzy_group(name_of(b[0]),{k:next(iter(v)) for k,v in by_name.items()})
  if target:b[0]=set_attr(b[0],'group-title',target);migrated+=1
  else:orphan+=1;orphan_rows.append((name_of(b[0]),a.get('tvg-id',''),a.get('channel-id',''),url_of(b)))
 org=build_iptv_org();repaired=unresolved=downloaded=0; unresolved_rows=[]
 for b in blocks:
  old=attrs(b[0]).get('tvg-logo','');new,did=repair_logo(b[0],org)
  if did:b[0]=new;repaired+=1;downloaded += int('iptv-org' in new)
  if not attrs(b[0]).get('tvg-logo','').strip():unresolved+=1;unresolved_rows.append((name_of(b[0]),attrs(b[0]).get('tvg-id',''),attrs(b[0]).get('channel-id',''),url_of(b)))
 rank={x:i for i,x in enumerate(ORDER)}
 def natural(s):return tuple(int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s.casefold()))
 blocks.sort(key=lambda b:(rank.get(attrs(b[0]).get('group-title',''),len(rank)),natural(name_of(b[0])),url_of(b).casefold()))
 canonical='#PLAYLIST-STUDIO-CATEGORIES:["'+'", "'.join(ORDER)+'"]';pre=[x for x in pre if not x.startswith('#PLAYLIST-STUDIO-CATEGORIES:')]
 idx=next((i+1 for i,x in enumerate(pre) if x.startswith('#EXTM3U')),0);pre.insert(idx,canonical);lines=pre[:]
 for b in blocks:lines.extend(b)
 PLAYLIST.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
 out=[f'# International Playlist Audit','',f'- Entries: {len(blocks)}',f'- Missing tvg-id values backfilled from exact, unambiguous primary-playlist names: {ids_backfilled}',f'- Exact duplicate URLs removed: {duplicate}',f'- Malformed entries removed: {malformed}',f'- Backup entries migrated: {migrated}',f'- Remaining true orphan backups: {orphan}',f'- Logos repaired to repository-local assets: {repaired}',f'- Logos recovered using external/iptv-org sources: {downloaded}',f'- Entries still without a safe local logo: {unresolved}','- Stream URLs changed: 0','', '## Remaining orphan backups']
 out += [f'{i}. **{n}** | tvg-id: `{tid or "-"}` | channel-id: `{cid or "-"}` | URL: `{u}`' for i,(n,tid,cid,u) in enumerate(orphan_rows,1)]
 out += ['', '## Unresolved logos']+[f'{i}. **{n}** | tvg-id: `{tid or "-"}` | channel-id: `{cid or "-"}` | URL: `{u}`' for i,(n,tid,cid,u) in enumerate(unresolved_rows,1)]
 Path('reports').mkdir(exist_ok=True);Path('reports/international-playlist-audit.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
 print(f'International audit: entries={len(blocks)} tvg_ids_backfilled={ids_backfilled} duplicate_urls_removed={duplicate} malformed_removed={malformed} backups_migrated={migrated} orphan_backups={orphan} logos_repaired={repaired} logos_external={downloaded} logos_unresolved={unresolved}')
if __name__=='__main__':main()
