#!/usr/bin/env python3
"""Reconcile International primary/Backup entries without contaminating primary groups.

Rules:
1. A Backup is promoted only when its corresponding primary is genuinely absent.
2. If a primary already exists, its Backup copy stays Backup.
3. If multiple primary copies of the same channel exist, keep one primary and move
   the extras to Backup.
4. Channel identity is primarily the normalized channel name. An explicit ID is
   used only as a tie-breaker when the name is missing. This prevents bad/shared
   tvg-ids from merging genuinely different channels such as Discovery and Disney.
"""
from pathlib import Path
import re, unicodedata, subprocess

PLAYLIST = Path('International-Playlist.m3u')
ORDER = ['Bangla','Indian','Pakistani','International','Documentary & Wildlife','Religious','Adult','Kids','Backup']
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)=(?:"([^"]*)"|\'([^\']*)\'|([^\s,]+))')
GROUP_RE = re.compile(r'\s+group-title\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s,]+)', re.I)
BASELINE_REF = '68b3f7cd'

INDIAN = {'tv','andexplorer','andtv','asiansonymax2','colors','ddindia','history18telugu','ktvindia','mazhavilmanorama','mtvplus','setmax','sonysab','stargoldselect','starmaagold','starmaamovies','udaya','zeemarathi','zeetalkies'}
BANGLA = {'atnbanglausa','channel24','ntv','madanitvbangla'}
KIDS = {'babytv','babytvhdi','discoveryfamily','disneyjr','disneyxd','nick','nickjreast','nickplus','nickelodeon','sonyyay'}
RELIGIOUS = {'saudisunnah','takbeer'}
DOCUMENTARY = {'nationalgeographic','tlc','tlceast','tlcworld'}
INTERNATIONAL = {'vh1','hbo','hboeast','ktntv'}
ID_GROUP = {'natgeo.us':'International','nationalgeographicchannelhd.in':'Indian','tlc.us':'International','babytvhd.in':'Kids','discoveryfamilia.us':'Kids','disneyjunior.us':'Kids','disneychannel.us':'Kids','nick.in':'Kids','nickjr.us':'Kids','nickhdplus.in':'Kids','nickelodeon.ca':'Kids','sonyyay.in':'Kids','ntv-in':'Bangla','vh1.us':'International'}

def attrs(s):
    out={}
    for m in ATTR_RE.finditer(s): out[m.group(1)] = next(v for v in m.groups()[1:] if v is not None)
    return out

def set_group(s, value):
    s = GROUP_RE.sub('', s)
    return s.replace('#EXTINF:-1 ', f'#EXTINF:-1 group-title="{value}" ', 1)

def norm(s):
    s=unicodedata.normalize('NFKD',str(s or '')).casefold()
    s=''.join(c for c in s if not unicodedata.combining(c))
    s=re.sub(r'\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|plus)\b',' ',s)
    return re.sub(r'[^a-z0-9]+','',s)

def name_of(info):
    a=attrs(info); return (a.get('tvg-name') or info.rsplit(',',1)[-1]).strip()

def url_of(block): return next((x.strip() for x in block[1:] if x.strip().startswith(('http://','https://'))),'')
def group_of(info): return attrs(info).get('group-title','').strip()
def is_backup(info): return group_of(info).casefold()=='backup'

def channel_key(info):
    n=norm(name_of(info))
    if n: return ('name', n)
    a=attrs(info); ident=(a.get('tvg-id') or a.get('channel-id') or '').strip().casefold()
    return ('id', ident) if ident else ('empty','')

def same_channel(a_info,b_info): return channel_key(a_info)==channel_key(b_info)

def classify(info):
    a=attrs(info)
    for key in ('tvg-id','channel-id'):
        ident=a.get(key,'').strip().casefold()
        if ident in ID_GROUP: return ID_GROUP[ident]
    n=norm(name_of(info))
    if n in INDIAN:return 'Indian'
    if n in BANGLA:return 'Bangla'
    if n in KIDS:return 'Kids'
    if n in RELIGIOUS:return 'Religious'
    if n in DOCUMENTARY:return 'Documentary & Wildlife'
    if n in INTERNATIONAL:return 'International'
    return 'International'

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

def baseline_backup_urls():
    try: text=subprocess.check_output(['git','show',f'{BASELINE_REF}:International-Playlist.m3u'],text=True,stderr=subprocess.DEVNULL)
    except Exception: return set()
    _, blocks=parse(text)
    return {url_of(b).casefold() for b in blocks if url_of(b) and is_backup(b[0])}

def main():
    pre,blocks=parse(PLAYLIST.read_text(encoding='utf-8-sig'))
    baseline=baseline_backup_urls()
    restored=promoted=kept_backup=moved_duplicate=0

    # Restore every known pre-classification Backup record before considering promotion.
    for b in blocks:
        if url_of(b).casefold() in baseline and not is_backup(b[0]):
            b[0]=set_group(b[0],'Backup'); restored+=1

    # Promote only a known orphan Backup when no primary with the same channel identity exists.
    primaries=[b for b in blocks if not is_backup(b[0])]
    for b in blocks:
        if not is_backup(b[0]): continue
        if baseline and url_of(b).casefold() not in baseline: continue
        if any(same_channel(p[0],b[0]) for p in primaries):
            kept_backup+=1; continue
        b[0]=set_group(b[0],classify(b[0])); primaries.append(b); promoted+=1

    # Keep exactly one primary per normalized channel name; every extra becomes Backup.
    by_key={}
    for b in blocks:
        if not is_backup(b[0]): by_key.setdefault(channel_key(b[0]),[]).append(b)
    for key,group in by_key.items():
        if len(group)<2: continue
        def score(b):
            a=attrs(b[0]); u=url_of(b).casefold()
            return (u not in baseline, bool(a.get('tvg-id') or a.get('channel-id')))
        ordered=sorted(group,key=score,reverse=True)
        for extra in ordered[1:]:
            extra[0]=set_group(extra[0],'Backup'); moved_duplicate+=1

    rank={x:i for i,x in enumerate(ORDER)}
    def natural(s): return tuple(int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s.casefold()))
    blocks.sort(key=lambda b:(rank.get(group_of(b[0]),len(rank)),natural(name_of(b[0])),url_of(b).casefold()))
    lines=pre[:]
    for b in blocks: lines.extend(b)
    PLAYLIST.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')

    report=Path('reports/international-playlist-audit.md')
    with report.open('a',encoding='utf-8') as f:
        f.write('\n\n## Primary/Backup reconciliation\n')
        f.write(f'- Known pre-classification backups restored to Backup: {restored}\n')
        f.write(f'- Genuine orphan backups promoted because no primary existed: {promoted}\n')
        f.write(f'- Existing backups retained because a primary exists: {kept_backup}\n')
        f.write(f'- Duplicate primary copies moved to Backup: {moved_duplicate}\n')
    print(f'Primary/Backup reconciliation: restored={restored} promoted={promoted} retained_backup={kept_backup} duplicate_primaries_to_backup={moved_duplicate}')

if __name__=='__main__': main()
