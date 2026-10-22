#!/usr/bin/env python3
"""Reconcile International primary/Backup entries without contaminating primary groups.

Rules:
1. A Backup is promoted only when its corresponding primary is genuinely absent.
2. If a primary already exists, its Backup copy stays Backup.
3. If multiple primary copies of the same channel exist, keep one primary and move
   the extras to Backup.
4. Channel identity is the normalized channel name. tvg-id/channel-id are only a
   fallback when the channel name is missing; they must never merge differently
   named channels because IPTV sources often reuse IDs.
"""
from pathlib import Path
import re, unicodedata, subprocess

PLAYLIST = Path('International-Playlist.m3u')
ORDER = ['Bangladesh','Indian Bangla','Indian Movies','Indian Music','Indian Entertainment','Pakistani','International','Documentary & Wildlife','Kids','Religious','Adult','Sports','Backup','New Channels','New Backup','Not Playing']
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
    # Remove only technical quality suffixes. Keep semantic words such as "Plus"
    # because "Nick" and "Nick Plus", for example, are different channels.
    s=re.sub(r'\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p)\b',' ',s)
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
    name=name_of(info)
    n=norm(name)
    country=a.get('tvg-country','ZZ').upper()
    language=(a.get('tvg-language','und').split(';')[0] or 'und').lower()
    if re.search(r'baby shark|cartoon network|discovery kids|disney|doraemon|duck tv|epic kids|kartoon|kiddo matix|lego channel|moonbug|mr bean animated|nick bangla|pogo|pbs kids|powerkids|smurf tv|strawberry shortcake|teen.?nick|teletubbies|tiny pop|tom and jerry|toonami|toongoggles|zoomoo|wow kidz|zb cartoon|tooku',name,re.I):
        return 'Kids'
    if re.search(r'national geographic|cgtn documentary|smithsonian channel|destination america|american heroes channel|law & crime|motortrend|world fishing network|true crime network|love nature',name,re.I):
        return 'Documentary & Wildlife'
    if country=='BD': return 'Bangladesh'
    if country=='PK': return 'Pakistani'
    if country=='IN':
        if language=='ben': return 'Indian Bangla'
        if re.search(r'music|musix|9xm|9x jalwa|9x jhakaas|9x tashan|7s music|mtv|vh1|stingray|xite|v2beat|now rock|now 70s|now 80s|trace urban|totalmusic|cmt\b|axs tv',name,re.I):
            return 'Indian Music'
        if re.search(r'movie|movies|cinema|cineplex|film|pictures|sony max|\bmax 2\b|\bpix\b|the movie club|zee action|pitaara|gravitas',name,re.I):
            return 'Indian Movies'
        return 'Indian Entertainment'
    if n in {'sports','espn','star sports','fox sports','sky sports'}: return 'Sports'
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
    restored=moved_duplicate=0

    # Restore historical Backup URLs first. Existing Backup rows remain manual-review entries.
    for b in blocks:
        if url_of(b).casefold() in baseline and not is_backup(b[0]):
            b[0]=set_group(b[0],'Backup')
            restored+=1

    # Do not promote Backup entries based on metadata or stream status.
    # If active groups contain same-name duplicate primaries, preserve alternates as Backup.
    by_key={}
    for b in blocks:
        grp=attrs(b[0]).get('group-title','').strip().casefold()
        if not is_backup(b[0]) and grp != 'adult':
            by_key.setdefault(channel_key(b[0]),[]).append(b)
    for key,group in by_key.items():
        if len(group)<2: continue
        ordered=sorted(group,key=lambda b:(bool(attrs(b[0]).get('tvg-id') or attrs(b[0]).get('channel-id')),url_of(b).casefold()),reverse=True)
        for extra in ordered[1:]:
            extra[0]=set_group(extra[0],'Backup')
            moved_duplicate+=1

    rank={x:i for i,x in enumerate(ORDER)}
    def natural(s): return tuple(int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s.casefold()))
    blocks.sort(key=lambda b:(rank.get(group_of(b[0]),len(rank)),natural(name_of(b[0])),url_of(b).casefold()))
    lines=pre[:]
    for b in blocks: lines.extend(b)
    PLAYLIST.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')

    report=Path('reports/international-playlist-audit.md')
    with report.open('a',encoding='utf-8') as f:
        f.write('\n\n## Backup preservation\n')
        f.write(f'- Historical Backup URLs restored to Backup: {restored}\n')
        f.write('- Backup rows are not automatically promoted or migrated.\n')
        f.write(f'- Duplicate primary copies moved to Backup for uniqueness: {moved_duplicate}\n')
    print(f'Backup preservation: restored={restored} primary_duplicates_to_backup={moved_duplicate}; existing Backup rows retained')
 
if __name__=='__main__': main()
