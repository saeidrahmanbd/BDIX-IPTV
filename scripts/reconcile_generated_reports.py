#!/usr/bin/env python3
"""Reconcile generated report metrics that use different scopes.

Keeps the Update Report honest by deriving near-duplicate and cross-queue
metadata-variant counts directly from the current playlist/report artifacts.
"""
from pathlib import Path
import re
from collections import defaultdict

PLAYLIST=Path("IPTV-Playlist.m3u")
HEALTH=Path("reports/stream-health.md")
UPDATE=Path("reports/Update Report.md")
ATTR=re.compile(r'([\w-]+)="([^"]*)"')
REVIEW={"New Channels","New Backup","Not Playing"}
ALIASES={"disney channel (india)":"Disney Channel India","gazi tv":"G TV","nick":"Nickelodeon (India)"}

def attrs(line): return dict(ATTR.findall(line))
def clean_name(name):
    value=re.sub(r"\s*(?:\[[^]]*(?:geo[- ]?blocked)[^]]*\]|\((?:\d{3,4}p|\d{3,4}i|UHD|FHD|HD|SD)\)|\s+(?:\d{3,4}p|\d{3,4}i))\s*$", "", name.strip(), flags=re.I)
    value=re.sub(r"\s+"," ",value).strip()
    return ALIASES.get(value.casefold(),value)

def canonical_url(url):
    from urllib.parse import urlsplit,urlunsplit,parse_qsl
    p=urlsplit(url); host=(p.hostname or '').lower()
    sensitive={"token","access_token","refresh_token","sig","signature","jwt","session","key","api_key","apikey","authorization","auth","hdnts","expires","e"}
    pairs=[(k.lower(),v) for k,v in parse_qsl(p.query,keep_blank_values=True) if k.lower() not in sensitive]
    query='&'.join(f'{k}={v}' for k,v in sorted(pairs))
    parts=p.path.split('/')
    low=[x.casefold() for x in parts]
    for i,s in enumerate(low):
        if s in {'live','movie','series','timeshift'} and i+3<len(parts):
            parts[i+1]='REDACTED'; parts[i+2]='REDACTED'
    return urlunsplit((p.scheme.lower(),host,'/'.join(parts).rstrip('/') or '/',query,''))

def playlist_records():
    rows=[]; cur=None
    for line in PLAYLIST.read_text(encoding='utf-8-sig').splitlines():
        if line.startswith('#EXTINF:'): cur=(line,attrs(line))
        elif cur and line.strip().lower().startswith(('http://','https://')):
            rows.append((cur[0],cur[1],line.strip())); cur=None
    return rows

def main():
    rows=playlist_records()
    families=defaultdict(set)
    for _,_,url in rows: families[canonical_url(url)].add(url)
    near=sum(1 for urls in families.values() if len(urls)>1)

    variants=defaultdict(set)
    for info,a,_ in rows:
        cid=(a.get('tvg-id') or a.get('channel-id') or '').strip().casefold()
        if not cid: continue
        variants[cid].add(clean_name(a.get('tvg-name','')))
    metadata=sum(1 for names in variants.values() if len(names)>1)
    details=[(cid,sorted(names)) for cid,names in variants.items() if len(names)>1]

    if HEALTH.exists():
        h=HEALTH.read_text(encoding='utf-8')
        h=re.sub(r'(^- Near-duplicate URL families: )\*\*\d+\*\*$',rf'\g<1>**{near}**',h,flags=re.M)
        if re.search(r'^- Near-duplicate URL families:',h,re.M) is None:
            marker='## Near-Duplicate URL Families\n\n'
            h=h.replace(marker,marker+f'- Near-duplicate URL families: **{near}**\n\n',1)
        HEALTH.write_text(h,encoding='utf-8')

    if UPDATE.exists():
        u=UPDATE.read_text(encoding='utf-8')
        u=re.sub(r'(\| Near-Duplicate URL Families \| \*\*)\d+(\*\* \|)',rf'\g<1>{near}\g<2>',u)
        u=re.sub(r'(- Metadata conflicts: \*\*)\d+(\*\*)',rf'\g<1>{metadata}\g<2>',u)
        block='## Metadata Identity Variants Across All Queues\n\n'
        if block not in u:
            body='\n'.join(f'- **{cid}** — '+', '.join(names) for cid,names in details)
            if not body: body='None.'
            u += f'\n{block}{body}\n'
        UPDATE.write_text(u,encoding='utf-8')
    print(f'Report reconciliation: near_duplicate_families={near}, metadata_identity_variants={metadata}')

if __name__=='__main__': main()
