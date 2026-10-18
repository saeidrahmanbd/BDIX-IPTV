#!/usr/bin/env python3
"""Audit and repair International-Playlist.m3u only."""
from pathlib import Path
import re, unicodedata

PLAYLIST=Path("International-Playlist.m3u")
LOGOS=Path("logos")
RAW_BASE="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ORDER=["Bangla","Indian","Pakistani","International","Documentary & Wildlife","Religious","Adult","Backup"]
NO_NUMBER={"Backup","Not Playing"}
ATTR_RE=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
BAD={"generated-fallback-btv-news.png","generated-fallback-channel-1.png","generated-fallback-channel-16.png","generated-fallback-channel-52.png","placeholder-btv-news.png","placeholder-channel-1.png","placeholder-channel-16.png","placeholder-channel-52.png"}

def attrs(s): return dict(ATTR_RE.findall(s))
def set_attr(s,k,v):
    p=re.compile(rf'{re.escape(k)}="[^"]*"')
    if p.search(s): return p.sub(f'{k}="{v}"',s,1)
    return s.replace("#EXTINF:-1 ",f'#EXTINF:-1 {k}="{v}" ',1)
def remove_attr(s,k): return re.sub(rf'\s+{re.escape(k)}="[^"]*"',"",s,1)
def name_of(info):
    a=attrs(info); return (a.get("tvg-name") or info.rsplit(',',1)[-1]).strip()
def norm(s):
    s=unicodedata.normalize('NFKD',str(s or '')).casefold()
    s=''.join(c for c in s if not unicodedata.combining(c))
    s=re.sub(r'\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p)\b',' ',s)
    return re.sub(r'[^a-z0-9]+','',s)
def url_of(b): return next((x.strip() for x in b[1:] if x.strip().startswith(('http://','https://'))),'')
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

def safe_local_for(name):
    try:
        import scripts.logo_source_catalog as cat
    except Exception:
        cat=None
    if cat:
        for mapping_name in ('LOCAL_LOGO_FILES','TV_LOGO_HINTS'):
            mapping=getattr(cat,mapping_name,{})
            if name in mapping:
                rel=mapping[name]
                p=LOGOS/rel
                if p.exists() and p.is_file() and p.name.casefold() not in {x.casefold() for x in BAD}:
                    return p
    target=norm(name)
    if not target: return None
    candidates=[]
    for p in LOGOS.rglob('*'):
        if not p.is_file() or p.suffix.lower() not in {'.png','.jpg','.jpeg','.webp','.svg'}: continue
        if p.name.casefold() in {x.casefold() for x in BAD}: continue
        if norm(p.stem)==target: candidates.append(p)
    return sorted(candidates,key=lambda p:(len(str(p)),str(p)))[0] if candidates else None

def repair_logo(info):
    a=attrs(info); name=name_of(info); old=a.get('tvg-logo','').strip()
    p=safe_local_for(name)
    if not p: return info,False
    desired=RAW_BASE+str(p.relative_to(LOGOS)).replace('\\','/')
    if old==desired: return info,False
    return set_attr(info,'tvg-logo',desired),True

def main():
    if not PLAYLIST.exists(): raise SystemExit('International-Playlist.m3u not found')
    pre,blocks=parse(PLAYLIST.read_text(encoding='utf-8-sig'))
    seen=set(); kept=[]; duplicate=malformed=changed=0
    for b in blocks:
        u=url_of(b)
        if not u: malformed+=1; continue
        if u.casefold() in seen: duplicate+=1; continue
        seen.add(u.casefold())
        info=b[0]; a=attrs(info); group=a.get('group-title','').strip()
        if group not in ORDER: info=set_attr(info,'group-title','International'); changed+=1; group='International'
        if group in NO_NUMBER and attrs(info).get('tvg-chno'): info=remove_attr(info,'tvg-chno'); changed+=1
        b[0]=info; kept.append(b)
    blocks=kept
    by_id={}; by_name={}
    for b in blocks:
        a=attrs(b[0]); g=a.get('group-title','').strip()
        if g=='Backup': continue
        n=norm(name_of(b[0]))
        if n: by_name.setdefault(n,g)
        for k in ('tvg-id','channel-id'):
            v=a.get(k,'').strip().casefold()
            if v: by_id.setdefault(v,g)
    migrated=orphan=0
    for b in blocks:
        a=attrs(b[0])
        if a.get('group-title','').strip()!='Backup': continue
        ids=[a.get('tvg-id','').strip().casefold(),a.get('channel-id','').strip().casefold()]
        target=next((by_id[x] for x in ids if x and x in by_id),None) or by_name.get(norm(name_of(b[0])))
        if target and target!='Backup': b[0]=set_attr(b[0],'group-title',target); migrated+=1
        else: orphan+=1
    repaired=unresolved=0
    for b in blocks:
        new,did=repair_logo(b[0])
        if did: b[0]=new; repaired+=1
        elif not attrs(b[0]).get('tvg-logo','').strip(): unresolved+=1
    rank={x:i for i,x in enumerate(ORDER)}
    def natural(s): return tuple(int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s.casefold()))
    blocks.sort(key=lambda b:(rank.get(attrs(b[0]).get('group-title',''),len(rank)),natural(name_of(b[0])),url_of(b).casefold()))
    canonical='#PLAYLIST-STUDIO-CATEGORIES:["'+'", "'.join(ORDER)+'"]'
    pre=[x for x in pre if not x.startswith('#PLAYLIST-STUDIO-CATEGORIES:')]
    idx=next((i+1 for i,x in enumerate(pre) if x.startswith('#EXTM3U')),0); pre.insert(idx,canonical)
    lines=pre[:]
    for b in blocks: lines.extend(b)
    PLAYLIST.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
    report=Path('reports/international-playlist-audit.md'); report.parent.mkdir(exist_ok=True)
    report.write_text(f"# International Playlist Audit\n\n- Entries: {len(blocks)}\n- Exact duplicate URLs removed: {duplicate}\n- Malformed entries removed: {malformed}\n- Backup entries migrated to matching primary group: {migrated}\n- Remaining true orphan backups: {orphan}\n- Logos repaired to repository-local assets: {repaired}\n- Entries still without a safe local logo: {unresolved}\n- Stream URLs changed: 0\n",encoding='utf-8')
    print(f'International audit: entries={len(blocks)} duplicate_urls_removed={duplicate} malformed_removed={malformed} backups_migrated={migrated} orphan_backups={orphan} logos_repaired={repaired} logos_unresolved={unresolved}')
if __name__=='__main__': main()
