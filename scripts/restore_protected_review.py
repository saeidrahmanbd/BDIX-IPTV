import re
from pathlib import Path

PLAYLIST=Path('IPTV-Playlist.m3u')
SNAPSHOT=Path('reports/protected-review-snapshot.json')
REVIEW_GROUPS={'Backup','Not Playing','New Channels','New Backup'}

def group_of(info):
    m=re.search(r'group-title="([^"]*)"',info,re.I)
    return m.group(1).strip() if m else ''

def restore():
    import json
    if not SNAPSHOT.exists() or not PLAYLIST.exists(): return
    snap=json.loads(SNAPSHOT.read_text(encoding='utf-8'))
    protected=[]
    for r in snap.get('entries',[]):
        if group_of(r.get('info','')) in REVIEW_GROUPS and r.get('url','').strip():
            protected.append((r['info'],r['url'].strip()))
    current=PLAYLIST.read_text(encoding='utf-8',errors='replace').splitlines()
    repaired_info_by_url={}
    for i,line in enumerate(current):
        if line.startswith('#EXTINF:'):
            j=i+1
            while j<len(current) and not current[j].strip(): j+=1
            if j<len(current) and current[j].strip().lower().startswith(('http://','https://')):
                repaired_info_by_url[current[j].strip().casefold()]=line
    protected_urls={url.casefold() for _,url in protected}
    cleaned=[]; removed=0; i=0
    while i<len(current):
        if current[i].startswith('#EXTINF:'):
            j=i+1
            while j<len(current) and not current[j].strip(): j+=1
            if j<len(current) and current[j].strip().lower().startswith(('http://','https://')):
                url=current[j].strip()
                if url.casefold() in protected_urls:
                    removed+=1; i=j+1; continue
        cleaned.append(current[i]); i+=1
    restored=0
    for snapshot_info,url in protected:
        group=group_of(snapshot_info)
        info=repaired_info_by_url.get(url.casefold(), snapshot_info)
        # Correctly strip any primary-channel number before restoring a protected entry.
        info=re.sub(r'\s+tvg-chno="[^"]*"', '', info)
        if re.search(r'group-title="[^"]*"', info):
            info=re.sub(r'group-title="[^"]*"', f'group-title="{group}"', info, count=1)
        else:
            info=info.replace('#EXTINF:-1 ', f'#EXTINF:-1 group-title="{group}" ', 1)
        insert_at=None; i=0
        while i<len(cleaned):
            if cleaned[i].startswith('#EXTINF:') and group_of(cleaned[i])==group:
                j=i+1
                while j<len(cleaned) and not cleaned[j].strip(): j+=1
                if j<len(cleaned) and cleaned[j].strip().lower().startswith(('http://','https://')): insert_at=j+1
            i+=1
        record=[info,url]
        if insert_at is None: cleaned.extend(record)
        else: cleaned[insert_at:insert_at]=record
        restored+=1
    PLAYLIST.write_text('\n'.join(cleaned).rstrip()+'\n',encoding='utf-8')
    print(f'Protected review restore: restored={restored} removed_conflicting_copies={removed}')

if __name__=='__main__': restore()
