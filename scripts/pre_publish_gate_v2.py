#!/usr/bin/env python3
"""Stricter publication gate: protects review queues and verifies local logos."""
import re, subprocess, sys
from collections import Counter, defaultdict
from pathlib import Path
P=Path('IPTV-Playlist.m3u'); EXCLUDE={'Backup','Not Playing'}; RAW='https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/'
ATTR=re.compile(r'([\w-]+)="([^"]*)"')
def attrs(s): return dict(ATTR.findall(s))
def parse(text):
    out=[]; cur=None
    for line in text.replace('\r','').splitlines():
        if line.startswith('#EXTINF:'): cur=(line,attrs(line))
        elif cur and line.strip().startswith(('http://','https://')): out.append((cur[0],cur[1],line.strip())); cur=None
    return out
def bad_removal(u):
    u=u.lower(); return bool(re.search(r'https?://[^/]*vods?\d*\.[^/]+/',u) or re.search(r'/vod(?:/|$)',u) or 'api.toonamiaftermath.com:3000/movies/' in u or 'dvltv.cc/play/' in u)
def main():
    cur=parse(P.read_text(encoding='utf-8-sig'))
    try: old=parse(subprocess.check_output(['git','show','HEAD:IPTV-Playlist.m3u'],text=True))
    except Exception: old=[]
    issues=[]
    urls=Counter(u.casefold() for _,_,u in cur)
    if any(n>1 for n in urls.values()): issues.append('duplicate stream URLs')
    oldq={u.casefold():a.get('group-title','').strip() for _,a,u in old if a.get('group-title','').strip() in EXCLUDE}
    newq={u.casefold():a.get('group-title','').strip() for _,a,u in cur if a.get('group-title','').strip() in EXCLUDE}
    deleted=[u for u in oldq if u not in newq]
    promoted=[u for u in oldq if u not in newq and any(x.casefold()==u for _,_,x in cur)]
    moved=[u for u in oldq if u in newq and oldq[u]!=newq[u]]
    if deleted: issues.append(f'review queue deletions: {len(deleted)}')
    if promoted: issues.append(f'review queue promotions: {len(promoted)}')
    if moved: issues.append(f'review queue reclassification: {len(moved)}')
    queue_numbers=[a.get('tvg-name','') for _,a,_ in cur if a.get('group-title','').strip() in EXCLUDE and a.get('tvg-chno','').strip()]
    if queue_numbers: issues.append(f'review entries with tvg-chno: {len(queue_numbers)}')
    primary=[(a,u) for _,a,u in cur if a.get('group-title','').strip() not in EXCLUDE]
    ch=Counter(a.get('tvg-chno','').strip() for a,_ in primary if a.get('tvg-chno','').strip())
    if any(n>1 for n in ch.values()): issues.append('primary channel-number collisions')
    if any(not a.get('tvg-chno','').strip() for a,_ in primary): issues.append('primary entries missing tvg-chno')
    identities=defaultdict(list)
    for a,u in primary:
        cid=(a.get('tvg-id') or a.get('channel-id') or '').strip().casefold()
        if cid: identities[cid].append(u)
    if any(len(v)>1 for v in identities.values()): issues.append('duplicate primary identities')
    missing=[]
    for _,a,_ in cur:
        logo=a.get('tvg-logo','').strip()
        if not logo or not logo.startswith(RAW): missing.append(a.get('tvg-name',''))
        elif not (Path('logos')/Path(logo.split('?',1)[0]).name).exists(): missing.append(a.get('tvg-name',''))
    if missing: issues.append(f'missing local logo assets: {len(missing)}')
    old_urls={u.casefold() for _,_,u in old}; removed=[u for _,_,u in old if u.casefold() not in {x.casefold() for _,_,x in cur}]
    unexpected=[u for u in removed if not bad_removal(u)]
    if unexpected: issues.append(f'unapproved primary stream removals: {len(unexpected)}')
    status='PASS' if not issues else 'BLOCK'
    print(f'Pre-publish gate v2: {status}; entries={len(cur)}')
    for x in issues: print('BLOCK:',x)
    if issues: sys.exit(1)
if __name__=='__main__': main()
