#!/usr/bin/env python3
"""Restore Backup/Not Playing review entries from a pre-maintenance snapshot."""
from pathlib import Path
import re
import sys

SNAPSHOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/tmp/iptv-protected-review.m3u')
PLAYLIST = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('IPTV-Playlist.m3u')

def blocks(text):
    lines = text.replace('\r', '').splitlines(); result=[]; i=0
    while i < len(lines):
        if lines[i].startswith('#EXTINF:'):
            j=i+1
            while j<len(lines) and not lines[j].strip(): j+=1
            if j<len(lines) and lines[j].strip().lower().startswith(('http://','https://')):
                result.append((lines[i],lines[j].strip())); i=j+1; continue
        i+=1
    return result

def attrs(info):
    return dict(re.findall(r'([\w-]+)="([^"]*)"', info))

def identity(info):
    a=attrs(info)
    return ((a.get('tvg-id') or a.get('channel-id') or '').strip().casefold(), a.get('tvg-name','').strip().casefold())

def group_of(info):
    return attrs(info).get('group-title','').strip()

def restore():
    if not SNAPSHOT.is_file() or not PLAYLIST.is_file(): return
    protected=blocks(SNAPSHOT.read_text(encoding='utf-8'))
    if not protected: return
    protected_urls={u.casefold() for _,u in protected}
    current_text=PLAYLIST.read_text(encoding='utf-8-sig').replace('\r','')
    current_records=blocks(current_text)
    # Retain the repaired metadata of an exact URL when reclassifying it into its
    # protected review group. Do not drop a different stream merely because its
    # channel identity matches a Backup/Not Playing entry.
    repaired_info_by_url={u.casefold(): info for info,u in current_records}
    current=current_text.splitlines()
    cleaned=[]; i=0; removed=0
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
        # Use corrected metadata from the exact same URL if a maintenance step
        # processed it. Preserve the protected category and strip primary numbering.
        info=repaired_info_by_url.get(url.casefold(), snapshot_info)
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
