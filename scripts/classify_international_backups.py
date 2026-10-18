#!/usr/bin/env python3
"""Apply the user's explicit classification to every remaining International Backup entry."""
from pathlib import Path
import re, unicodedata

PLAYLIST = Path('International-Playlist.m3u')
ORDER = ['Bangla','Indian','Pakistani','International','Documentary & Wildlife','Religious','Adult','Backup']
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)=(?:"([^"]*)"|\'([^\']*)\'|([^\s,]+))')

INDIAN = {
    'tv', 'andexplorer', 'andtv', 'asiansonymax2', 'colors', 'ddindia',
    'history18telugu', 'ktvindia', 'mazhavilmanorama', 'mtvplus', 'setmax',
    'sonysab', 'stargoldselect', 'starmaagold', 'starmaamovies', 'udaya',
    'zeemarathi', 'zeetalkies',
}
BANGLA = {'atnbanglausa', 'channel24', 'ntv', 'madanitvbangla'}
KIDS = {
    'babytv', 'babytvhdi', 'discoveryfamily', 'disneyjr', 'disneyxd',
    'nick', 'nickjreast', 'nickplus', 'nickelodeon', 'sonyyay',
}
RELIGIOUS = {'saudisunnah', 'takbeer'}
DOCUMENTARY = {'nationalgeographic', 'tlc', 'tlceast', 'tlcworld'}
INTERNATIONAL = {'vh1', 'hbo', 'hboeast', 'ktntv'}

ID_GROUP = {
    'natgeo.us': 'International',
    'nationalgeographicchannelhd.in': 'Indian',
    'tlc.us': 'International',
    'babytvhd.in': 'Kids',
    'discoveryfamilia.us': 'Kids',
    'disneyjunior.us': 'Kids',
    'disneychannel.us': 'Kids',
    'nick.in': 'Kids',
    'nickjr.us': 'Kids',
    'nickhdplus.in': 'Kids',
    'nickelodeon.ca': 'Kids',
    'sonyyay.in': 'Kids',
    'ntv-in': 'Bangla',
    'vh1.us': 'International',
}

def attrs(s):
    out = {}
    for m in ATTR_RE.finditer(s):
        out[m.group(1)] = next(v for v in m.groups()[1:] if v is not None)
    return out

def set_attr(s, key, value):
    p = re.compile(rf'{re.escape(key)}\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s,]+)', re.I)
    if p.search(s):
        return p.sub(f'{key}="{value}"', s, 1)
    return s.replace('#EXTINF:-1 ', f'#EXTINF:-1 {key}="{value}" ', 1)

def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).casefold()
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|plus)\b', ' ', s)
    return re.sub(r'[^a-z0-9]+', '', s)

def name_of(info):
    a = attrs(info)
    return (a.get('tvg-name') or info.rsplit(',', 1)[-1]).strip()

def is_backup(info):
    a = attrs(info)
    if a.get('group-title', '').strip().casefold() == 'backup':
        return True
    return bool(re.search(r'group-title\s*=\s*(?:"Backup"|\'Backup\'|Backup)(?=\s|,|$)', info, re.I))

def classify(info):
    a = attrs(info)
    for key in ('tvg-id', 'channel-id'):
        ident = a.get(key, '').strip().casefold()
        if ident in ID_GROUP:
            return ID_GROUP[ident]
    n = norm(name_of(info))
    if n in INDIAN: return 'Indian'
    if n in BANGLA: return 'Bangla'
    if n in KIDS: return 'Kids'
    if n in RELIGIOUS: return 'Religious'
    if n in DOCUMENTARY: return 'Documentary & Wildlife'
    if n in INTERNATIONAL: return 'International'
    return 'International'

def parse(text):
    pre, blocks, cur = [], [], None
    for line in text.replace('\r','').splitlines():
        if line.startswith('#EXTINF:'):
            if cur is not None: blocks.append(cur)
            cur = [line]
        elif cur is None:
            pre.append(line)
        else:
            cur.append(line)
    if cur is not None: blocks.append(cur)
    return pre, blocks

def url_of(b):
    return next((x.strip() for x in b[1:] if x.strip().startswith(('http://','https://'))), '')

def main():
    text = PLAYLIST.read_text(encoding='utf-8-sig')
    pre, blocks = parse(text)
    moved = 0
    breakdown = {}
    for b in blocks:
        if not is_backup(b[0]):
            continue
        target = classify(b[0])
        b[0] = set_attr(b[0], 'group-title', target)
        moved += 1
        breakdown[target] = breakdown.get(target, 0) + 1

    rank = {x:i for i,x in enumerate(ORDER)}
    def natural(s):
        return tuple(int(x) if x.isdigit() else x for x in re.split(r'(\d+)', s.casefold()))
    blocks.sort(key=lambda b: (rank.get(attrs(b[0]).get('group-title',''), len(rank)), natural(name_of(b[0])), url_of(b).casefold()))
    lines = pre[:]
    for b in blocks: lines.extend(b)
    PLAYLIST.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')
    print('Manual orphan classification:', moved, breakdown)

if __name__ == '__main__': main()
