#!/usr/bin/env python3
"""Final deterministic playlist hardening.

Hardens one explicitly selected playlist at a time. Stream URLs are never
changed or removed; exact duplicate URLs block the run for manual review.
"""
from pathlib import Path
import json, re, sys, unicodedata
from country_verification import reference_from_playlists, verify_country
from discover_bd_in_new_queues import prohibited_channel

PLAYLIST_ORDERS={
    'IPTV-Playlist.m3u': ['Bangladesh','Indian Bangla','Indian Movies','Indian Music','Indian Entertainment','Pakistani','International','Documentary & Wildlife','Kids','Religious','Sports','Review','New Channels','New Backups','Backup'],
}
ATTR=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NON_NUMBERED={'Backup','Review','Not Playing','New Channels','New Backups'}
REVIEW_GROUPS={'New Channels','New Backups'}
def attrs(s): return dict(ATTR.findall(s))
def key(s):
 s=unicodedata.normalize('NFKD',str(s or '')).casefold().strip()
 return tuple(int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s))
def normalize_name(s):
 s=unicodedata.normalize('NFKD',str(s or '')).casefold().strip()
 s=re.sub(r'\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|360p)\b',' ',s)
 return re.sub(r'[^a-z0-9]+',' ',s).strip()
def set_attr(line,k,v):
 p=re.compile(rf'{re.escape(k)}="[^"]*"')
 return p.sub(f'{k}="{v}"',line,1) if p.search(line) else line.replace('#EXTINF:-1 ',f'#EXTINF:-1 {k}="{v}" ',1)
def remove_attr(line,k):
 return re.sub(rf'\s+{re.escape(k)}="[^"]*"','',line, count=1)
def parse(path):
 lines=path.read_text(encoding='utf-8-sig').replace('\r\n','\n').replace('\r','\n').splitlines(); pre=[]; rec=[]; cur=None
 for line in lines:
  if line.startswith('#EXTINF:'):
   if cur is not None: rec.append(cur)
   cur=[line]
  elif cur is not None: cur.append(line)
  else: pre.append(line)
 if cur is not None: rec.append(cur)
 return pre,rec
def process(path):
 if not path.is_file(): return
 order=PLAYLIST_ORDERS[path.name]; rank={x:i for i,x in enumerate(order)}
 pre,rec=parse(path)
 # Keep the Playlist Studio registry synchronized with the enforced group order.
 registry_prefix='#PLAYLIST-STUDIO-CATEGORIES:'
 registry_positions=[i for i,line in enumerate(pre) if line.startswith(registry_prefix)]
 if len(registry_positions)>1:
  raise SystemExit(f'{path}: multiple category registries; refusing ambiguous rewrite.')
 registry_line=registry_prefix+json.dumps(order,ensure_ascii=False)
 if registry_positions:
  pre[registry_positions[0]]=registry_line
 else:
  header_index=next((i+1 for i,line in enumerate(pre) if line.startswith('#EXTM3U')),len(pre))
  pre.insert(header_index,registry_line)
 reference=reference_from_playlists([path])
 filtered=[]; removed=[]; demoted=[]; permanently_removed=[]
 for r in rec:
  a=attrs(r[0]); name=(a.get('tvg-name') or r[0].rsplit(',',1)[-1]).strip()
  group=a.get('group-title','').strip()
  if prohibited_channel(a,name) == 'permanently banned channel':
   permanently_removed.append((name,'permanently banned channel'))
   continue
  if group == 'Not Playing':
   r[0]=set_attr(r[0],'group-title','Review'); group='Review'
  # A foreign country suffix in a discovery queue is not an eligible BD/IN
  # candidate. Preserve it in the general Review quarantine instead of aborting
  # the entire daily discovery run or silently relabelling its country.
  if group in REVIEW_GROUPS:
   declared_suffixes={
    match.group(1).upper()
    for value in (a.get('tvg-id',''),a.get('channel-id',''))
    if (match:=re.search(r'\.([a-z]{2})(?:@|$)',value.strip(),re.I))
   }
   if declared_suffixes and (len(declared_suffixes)!=1 or not declared_suffixes.issubset({'BD','IN'})):
    r[0]=set_attr(r[0],'group-title','Review')
    group='Review'
  verified=verify_country(a,name,reference)
  if verified.ok and verified.country=='IN':
   reason=prohibited_channel(a,name,'IN')
   if reason and group in REVIEW_GROUPS:
    removed.append((name,reason))
    continue
   if reason and group.casefold() not in {'backup','review','not playing'}:
    r[0]=set_attr(r[0],'group-title','Backup')
    demoted.append((name,reason))
  filtered.append(r)
 rec=filtered
 if permanently_removed:
  print(f'REMOVED PERMANENTLY BANNED CHANNEL ROWS: {len(permanently_removed)}')
  for name,reason in permanently_removed: print(f'  - {name}: {reason}')
 if removed:
  print(f'REMOVED PROHIBITED INDIAN REVIEW-QUEUE ROWS: {len(removed)}')
  for name,reason in removed: print(f'  - {name}: {reason}')
 if demoted:
  print(f'DEMOTED PROHIBITED INDIAN PRIMARY CHANNELS TO BACKUP: {len(demoted)}')
  for name,reason in demoted: print(f'  - {name}: {reason}')
 seen=set(); duplicate_urls=[]
 for r in rec:
  u=next((x.strip() for x in r[1:] if x.strip().startswith(('http://','https://'))),'')
  k=u.casefold()
  if k and k in seen: duplicate_urls.append(u)
  if k: seen.add(k)
 if duplicate_urls:
  raise SystemExit(f'{path}: {len(duplicate_urls)} duplicate stream URL occurrences; refusing to delete any entry.')
 # New Channels/New Backups may hold only candidates verified as BD/IN; normalize tvg-country, never delete.
 country_errors=[]
 for r in rec:
  a=attrs(r[0])
  if a.get('group-title','').strip() in REVIEW_GROUPS:
   v=verify_country(a,(a.get('tvg-name') or r[0].rsplit(',',1)[-1]).strip(),reference)
   if not v.ok: country_errors.append(f"review queue entry not verified as BD/IN: {(a.get('tvg-name') or r[0].rsplit(',',1)[-1]).strip()} ({v.reason})")
   elif a.get('tvg-country','').strip().upper()!=v.country: r[0]=set_attr(r[0],'tvg-country',v.country)
 if country_errors: raise SystemExit(f'{path}: '+'; '.join(country_errors))
 for r in rec:
  a=attrs(r[0]); cid=(a.get('tvg-id') or a.get('channel-id') or '').strip().casefold(); g=a.get('group-title','').strip()
  if cid=='ultimatetv.in@sd' and g!='Backup': r[0]=set_attr(r[0],'group-title','Indian Music')
  if g in NON_NUMBERED and 'tvg-chno' in a:
   r[0]=remove_attr(r[0],'tvg-chno')
 def rkey(r):
  a=attrs(r[0]); g=a.get('group-title','').strip(); n=(a.get('tvg-name') or r[0].rsplit(',',1)[-1]).strip()
  u=next((x.strip() for x in r[1:] if x.strip().startswith(('http://','https://'))),'')
  if g == 'Bangladesh':
   raw=a.get('tvg-chno','').strip()
   number=int(raw) if raw.isdigit() else 10**12
   return (rank.get(g,len(rank)),number,key(n),u.casefold())
  return (rank.get(g,len(rank)),key(n),u.casefold())
 # Fill missing Bangladesh channel numbers deterministically without changing
 # any existing number. This prevents one unnumbered legacy row from blocking
 # discovery; the final sort restores numeric order.
 bd_rows=[r for r in rec if attrs(r[0]).get('group-title','').strip()=='Bangladesh']
 used_numbers={int(attrs(r[0])['tvg-chno']) for r in bd_rows if attrs(r[0]).get('tvg-chno','').strip().isdigit()}
 next_number=1
 for r in bd_rows:
  a=attrs(r[0])
  if not a.get('tvg-chno','').strip().isdigit():
   while next_number in used_numbers: next_number+=1
   r[0]=set_attr(r[0],'tvg-chno',next_number)
   used_numbers.add(next_number)
   next_number+=1
 rec.sort(key=rkey)
 errors=[]; transitions=[]; last=None
 for r in rec:
  g=attrs(r[0]).get('group-title','').strip()
  if g!=last: transitions.append(g); last=g
 last_i=-1
 for g in transitions:
  if g not in rank: errors.append(f'unknown category: {g}'); continue
  i=rank[g]
  if i<last_i: errors.append(f'category order: {g}')
  last_i=max(last_i,i)
 if any(transitions.count(g)>1 for g in set(transitions)): errors.append('split category block')
 for g in order:
  group_records=[r for r in rec if attrs(r[0]).get('group-title','').strip()==g]
  if not group_records: continue
  if g == 'Bangladesh':
   numbers=[int(attrs(r[0]).get('tvg-chno','')) for r in group_records if attrs(r[0]).get('tvg-chno','').strip().isdigit()]
   if len(numbers)!=len(group_records) or numbers!=sorted(numbers):
    errors.append('channel-number order/coverage: Bangladesh')
  elif g not in REVIEW_GROUPS:
   names=[(attrs(r[0]).get('tvg-name') or r[0].rsplit(',',1)[-1]).strip() for r in group_records]
   if names!=sorted(names,key=key): errors.append(f'A-Z order: {g}')
 for r in rec:
  a=attrs(r[0]); g=a.get('group-title','').strip()
  cid=(a.get('tvg-id') or a.get('channel-id') or '').strip().casefold()
  name=(a.get('tvg-name') or r[0].rsplit(',',1)[-1]).strip().casefold()
  if name=='channel s uk' and (g not in {'Bangladesh','Backup','Review','Not Playing'} or cid!='channels.uk@679aa9'): errors.append('Channel S UK must retain its canonical identity in Bangladesh/Backup/Review')
  if cid=='ultimatetv.in@sd' and g not in {'Indian Music','Backup'}: errors.append('Ultimate TV must be Indian Music primary or Backup alternate')
 if errors:
  raise SystemExit(f'{path}: '+ '; '.join(errors))
 path.write_text('\n'.join(pre+[x for r in rec for x in r])+'\n',encoding='utf-8')
 print(f'HARDENED {path}: {len(rec)} records')

def main():
 paths=sys.argv[1:] or list(PLAYLIST_ORDERS)
 for name in paths:
  p=Path(name)
  if p.name not in PLAYLIST_ORDERS: raise SystemExit(f'Unsupported playlist: {p}')
  process(p)

if __name__ == "__main__":
 main()
