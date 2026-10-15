#!/usr/bin/env python3
"""Final deterministic repair pass for IPTV-Playlist.m3u only.

Applies conservative metadata, URL, numbering, and structural repairs without
modifying BDIX-Playlist.m3u.  Primary streams are preserved unless they are
clearly malformed/blocked; duplicate backup copies of an identical URL are
removed, while independent backup streams remain.
"""
from pathlib import Path
import re
from collections import defaultdict

P = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/gemini-playlist-repairs.md")
RAW = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
CATEGORIES = ["Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports","Backup"]

ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

def attrs(line):
    return dict(ATTR.findall(line))

def split_extinf(line):
    q = False
    for i, ch in enumerate(line):
        if ch == '"': q = not q
        elif ch == ',' and not q: return line[:i], line[i+1:]
    return line, ""

def set_attr(line, key, value):
    pat = re.compile(rf'{re.escape(key)}="[^"]*"')
    if pat.search(line): return pat.sub(f'{key}="{value}"', line, count=1)
    return line.replace("#EXTINF:-1 ", f'#EXTINF:-1 {key}="{value}" ', 1)

def del_attr(line, key):
    return re.sub(rf'\s*{re.escape(key)}="[^"]*"', '', line)

def norm(name):
    s = str(name or '').lower()
    s = re.sub(r'\[[^]]*\]|\([^)]*\)', ' ', s)
    s = re.sub(r'\b(?:uhd|fhd|hd|sd|4k|1080p|720p|576p|480p|360p)\b', ' ', s)
    return re.sub(r'[^a-z0-9]+', '', s)

def url_of(rec):
    for line in rec[1:]:
        if line.strip().lower().startswith(('http://','https://')):
            return line.strip()
    return ''

def parse(text):
    lines = text.replace('\r','').splitlines()
    pre=[]; recs=[]; cur=None
    for line in lines:
        if line.startswith('#EXTINF:'):
            if cur is not None: recs.append(cur)
            cur=[line]
        elif cur is None:
            pre.append(line)
        else:
            cur.append(line)
    if cur is not None: recs.append(cur)
    return pre, recs

def rebuild(pre, recs):
    return '\n'.join(pre + [line for rec in recs for line in rec] ) + '\n'

text = P.read_text(encoding='utf-8-sig')
pre, recs = parse(text)

# Canonical category registry: keep Studio's category contract but remove the
# redundant Studio name directive.  The comments remain valid M3U comments.
pre = [x for x in pre if not x.startswith('#PLAYLIST-STUDIO-NAME:')]
pre = [x for x in pre if not x.startswith('#PLAYLIST-STUDIO-CATEGORIES:')]
header_i = next((i for i,x in enumerate(pre) if x.startswith('#EXTM3U')), None)
cat_line = '#PLAYLIST-STUDIO-CATEGORIES:' + str(CATEGORIES).replace("'", '"')
if header_i is not None:
    header = pre.pop(header_i)
    pre = [header, cat_line] + [x for x in pre if x.strip()]
else:
    pre = [cat_line] + [x for x in pre if x.strip()]

# Remove only clearly blocked/malformed stream routes.  We do NOT remove
# ordinary tokenized streams merely because they contain an expiring token.
blocked=[]
kept=[]
for rec in recs:
    a=attrs(rec[0]); url=url_of(rec); low=url.lower(); name=split_extinf(rec[0])[1].strip()
    if not url:
        blocked.append((name,'missing stream URL',''))
        continue
    if re.search(r'^https?://(?:[^/]+\.)?dvltv\.cc(?::\d+)?/play(?:/|$)', url, re.I):
        blocked.append((name,'blocked dvltv.cc/play route',url)); continue
    if re.search(r'(?:^|/)(?:vods?|movies?)/', url, re.I):
        blocked.append((name,'VOD-style route',url)); continue
    if re.search(r'/(?:api/)?play/(?:[^/]+/)?(?:filamchi|manoranjan)(?:\.m3u8)?(?:[/?#]|$)', url, re.I):
        blocked.append((name,'wrong-channel/proxy play route',url)); continue
    if re.search(r'dfsdfsdf', url, re.I):
        blocked.append((name,'malformed placeholder URL',url)); continue
    kept.append(rec)
recs=kept

# Build primary identity map. Backups inherit the canonical identity, name and
# logo of the matching primary channel, but keep their own stream URL.
primary_by_name={}
primary_by_id={}
for rec in recs:
    a=attrs(rec[0]); g=a.get('group-title','').strip()
    if g == 'Backup': continue
    name=a.get('tvg-name') or split_extinf(rec[0])[1].strip()
    key=norm(name)
    if key and key not in primary_by_name: primary_by_name[key]=rec
    cid=a.get('tvg-id') or a.get('channel-id')
    if cid: primary_by_id[cid.lower()]=rec

# Canonicalize Backup records and remove exact URL duplicates when an identical
# stream is already present elsewhere in the same channel identity.
seen_urls=set(); final=[]; backup_fixes=0; duplicate_backups=0
for rec in recs:
    a=attrs(rec[0]); g=a.get('group-title','').strip(); url=url_of(rec)
    if g == 'Backup':
        name=a.get('tvg-name') or split_extinf(rec[0])[1].strip()
        primary=primary_by_name.get(norm(name))
        if primary is None and a.get('tvg-id'):
            primary=primary_by_id.get(a['tvg-id'].lower())
        if primary:
            pa=attrs(primary[0]); pname=pa.get('tvg-name') or split_extinf(primary[0])[1].strip()
            cid=pa.get('tvg-id') or pa.get('channel-id')
            rec[0]=set_attr(rec[0],'tvg-name',pname)
            if cid:
                rec[0]=set_attr(rec[0],'tvg-id',cid)
                rec[0]=set_attr(rec[0],'channel-id',cid)
            plogo=pa.get('tvg-logo','')
            if plogo: rec[0]=set_attr(rec[0],'tvg-logo',plogo)
            backup_fixes += 1
        rec[0]=set_attr(rec[0],'group-title','Backup')
        rec[0]=del_attr(rec[0],'tvg-chno')
    if url:
        key=url.lower()
        if g == 'Backup' and key in seen_urls:
            duplicate_backups += 1
            continue
        seen_urls.add(key)
    final.append(rec)
recs=final

# Preserve per-entry VLC/HLS directives exactly with their stream.  HTTP is only
# upgraded when the exact same host+path already exists as HTTPS elsewhere in
# the playlist; this avoids breaking IP-origin streams that do not support TLS.
https_urls={url_of(r) for r in recs if url_of(r).lower().startswith('https://')}
https_exact={u.lower() for u in https_urls}
http_upgrades=0
for rec in recs:
    u=url_of(rec)
    if not u.lower().startswith('http://'): continue
    candidate='https://'+u[7:]
    if candidate.lower() in https_exact:
        for i,line in enumerate(rec):
            if line.strip()==u: rec[i]=candidate; http_upgrades += 1; break

# Primary numbering: retain existing unique numbers; repair collisions and
# missing values with the smallest unused positive number. Backup never carries
# a tvg-chno. This preserves established numbering while guaranteeing uniqueness.
primary=[r for r in recs if attrs(r[0]).get('group-title','').strip()!='Backup']
used=set()
for r in primary:
    n=attrs(r[0]).get('tvg-chno','').strip()
    if n.isdigit() and int(n)>0: used.add(int(n))
next_num=1; assigned=0
seen_primary_nums=set()
for r in primary:
    a=attrs(r[0]); n=a.get('tvg-chno','').strip(); valid=n.isdigit() and int(n)>0
    if valid and int(n) not in seen_primary_nums:
        seen_primary_nums.add(int(n)); continue
    while next_num in used: next_num += 1
    r[0]=set_attr(r[0],'tvg-chno',str(next_num)); used.add(next_num); seen_primary_nums.add(next_num); next_num += 1; assigned += 1

# Structural finalization: every record must have exactly one URL and EXTINF,
# category names must be canonical, and the file must end after a complete URL.
for r in recs:
    a=attrs(r[0]); g=a.get('group-title','').strip()
    if g not in CATEGORIES:
        # Unknown groups are retained but moved to Backup rather than silently
        # deleting a potentially useful stream.
        r[0]=set_attr(r[0],'group-title','Backup')
        r[0]=del_attr(r[0],'tvg-chno')

P.write_text(rebuild(pre,recs),encoding='utf-8')
REPORT.parent.mkdir(parents=True,exist_ok=True)
REPORT.write_text(
    '# Final IPTV Playlist Repair\n\n'
    f'- Entries retained: **{len(recs)}**\n'
    f'- Clearly malformed/blocked entries removed: **{len(blocked)}**\n'
    f'- Backup metadata records canonicalized: **{backup_fixes}**\n'
    f'- Duplicate backup URLs removed: **{duplicate_backups}**\n'
    f'- Safe HTTP→HTTPS upgrades: **{http_upgrades}**\n'
    f'- Primary channel numbers repaired: **{assigned}**\n\n'
    'The repair intentionally preserves referrer directives and signed/live URLs unless the URL is explicitly malformed, blocked, VOD-style, or a duplicate backup.\n',
    encoding='utf-8')
print(f'Final repair: retained={len(recs)} removed={len(blocked)} backup_fixed={backup_fixes} dup_backups={duplicate_backups} https={http_upgrades} numbers={assigned}')
