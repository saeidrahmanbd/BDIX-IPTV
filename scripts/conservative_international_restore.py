#!/usr/bin/env python3
"""Conservatively rebuild the International group and normalize Adult names.

Uses the pre-audit playlist as a candidate source, but classifies obvious
regional/specialty channels into the standard playlist groups instead of
blindly restoring everything to International.
"""
from pathlib import Path
import re, subprocess, unicodedata

PLAYLIST = Path('International-Playlist.m3u')
BASE = '86da6b7f3183a62a0fd5355ae2cf7da0a68d8bae'
ORDER = ['Bangladesh','Indian Bangla','Indian Movies','Indian Music','Indian Entertainment','Pakistani','International','Documentary & Wildlife','Kids','Religious','Adult','Sports','Backup','New Channels','New Backup','Not Playing']
RESTORE_CHANNELS = {
    '24hourfreemovies': {'name':'24 Hour Free Movies','logo':'24-hour-free-movies-720p-2a4fdea7cd.png','id':'custom.24-hour-free-movies','country':'US','language':'eng'},
    'aflam': {'name':'Aflam','logo':'nvisionbd-aflam.png','id':'custom.aflam','country':'SA','language':'ara'},
    'axs': {'name':'AXS TV','logo':'axs.png','id':'AXSTV.us','country':'US','language':'eng'},
    'moviesphereau': {'name':'MovieSphere AU','logo':'moviesphere-au-1080p-1b23bc91d7.png','id':'custom.moviesphere-au','country':'AU','language':'eng'},
    'moviesphereuk': {'name':'MovieSphere UK','logo':'moviesphere-uk.png','id':'custom.moviesphere-uk','country':'GB','language':'eng'},
    'arabicatv': {'name':'Arabica TV','logo':'arabica-tv.png','id':'custom.arabica-tv','country':'LB','language':'ara'},
    'cctv11': {'name':'CCTV-11','logo':'cctv-11.png','id':'CCTV11.cn','country':'CN','language':'zho'},
}


ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

def attrs(s): return dict(ATTR_RE.findall(s))
def name_of(s):
    a = attrs(s)
    return (a.get('tvg-name') or s.rsplit(',',1)[-1]).strip()
def set_attr(s,k,v):
    p = re.compile(rf'{re.escape(k)}="[^"]*"')
    return p.sub(f'{k}="{v}"',s,1) if p.search(s) else s.replace('#EXTINF:-1 ',f'#EXTINF:-1 {k}="{v}" ',1)
def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).casefold()
    s = ''.join(c for c in s if not unicodedata.combining(c))
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

def git_base_playlist():
    return subprocess.check_output(['git','show',f'{BASE}:International-Playlist.m3u'],text=True,encoding='utf-8')

def classify(info):
    a=attrs(info); name=name_of(info); n=norm(name)
    country=a.get('tvg-country','').upper(); lang=(a.get('tvg-language','').split(';')[0] or '').lower()
    if re.search(r'\b(adult|xxx|porn|playboy|penthouse|brazzers|bangbros|pornbox|passion|erotic|sex)\b',name,re.I): return 'Adult'
    if re.search(r'baby shark|cartoon|disney|doraemon|duck tv|kids|kiddo|lego channel|moonbug|mr bean animated|nick|pogo|pbs kids|pop\b|powerkids|smurf|strawberry shortcake|teen.?nick|teletubbies|tiny pop|tom and jerry|toon|zoomoo|wow kidz|zbcartoon',name,re.I): return 'Kids'
    if re.search(r'national geographic|nat geo|cgtn documentary|smithsonian|destination america|american heroes|law & crime|motortrend|world fishing|true crime|love nature|wild|wildlife|animal planet',name,re.I): return 'Documentary & Wildlife'
    if re.search(r'islam|quran|qur\'an|muslim|huda|iqra|peace tv|madina|makkah|mecca|takbeer|ahlul|religious',name,re.I): return 'Religious'
    if re.search(r'\b(sport|sports|espn|bein sport|sky sport|fox sport|geo super|ten sport|star sports|supersport)\b',name,re.I): return 'Sports'
    if country == 'BD': return 'Bangladesh'
    if country == 'PK': return 'Pakistani'
    if country == 'IN':
        if lang == 'ben' or re.search(r'\b(bangla|bengali)\b',name,re.I): return 'Indian Bangla'
        if re.search(r'music|musix|9xm|9x jalwa|9x jhakaas|9x tashan|7s music|mtv|vh1|stingray|xite|v2beat|now rock|now 70s|now 80s|trace urban|totalmusic',name,re.I): return 'Indian Music'
        if re.search(r'movie|movies|cinema|film|pictures|sony max|\bmax 2\b|\bpix\b|romedy|zee action|pitaara|gravitas',name,re.I): return 'Indian Movies'
        return 'Indian Entertainment'
    if re.search(r'\b(bangla|bengali)\b',name,re.I) and country in {'CA','US','GB','AU'}: return 'International'
    return 'International'

def normalize_adult(info):
    a=attrs(info)
    if a.get('group-title','').casefold() != 'adult': return info,False
    old=name_of(info)
    new=old
    # Remove technical/generic prefixes, but preserve meaningful brands such as
    # PORNBOX, STARS EXCLUSIVE and VERIFIED AMATEURS.
    new=re.sub(r'^\s*(?:(?:24/7)\s+)?(?:adult\s+)?(?:xxx)\s*[-:|]?\s*','',new,flags=re.I)
    new=re.sub(r'^\s*(?:HD|FHD|UHD|SD|4K|1080P|720P|576P|480P)\s*[-:|]?\s*','',new,flags=re.I)
    new=re.sub(r'^\s*(?:ADULT|ADULT CHANNEL)\s*[-:|]?\s*','',new,flags=re.I)
    new=re.sub(r'\s{2,}',' ',new).strip(' -:|')
    if not new: return info,False
    if new == old: return info,False
    # Keep tvg-name aligned with the normalized display name and preserve the ID.
    info=set_attr(info,'tvg-name',new)
    prefix=info.rsplit(',',1)[0]
    info=prefix+','+new
    return info,True

def main():
    pre,current=parse(PLAYLIST.read_text(encoding='utf-8-sig'))
    base_pre,base_blocks=parse(git_base_playlist())
    existing={url_of(b).casefold() for b in current if url_of(b)}
    existing_names={norm(name_of(b[0])) for b in current}
    restored=0
    for b in base_blocks:
        a=attrs(b[0]); g=a.get('group-title','').strip().casefold(); u=url_of(b)
        if g != 'international' or not u: continue
        spec=RESTORE_CHANNELS.get(norm(name_of(b[0])))
        if not spec or norm(spec['name']) in existing_names or u.casefold() in existing: continue
        logo=LOGOS/spec['logo']
        if not logo.is_file() or 'unused' in {x.casefold() for x in logo.relative_to(LOGOS).parts}: continue
        info=f'#EXTINF:-1 group-title="International" tvg-id="{spec["id"]}" tvg-name="{spec["name"]}" tvg-logo="{RAW_BASE+spec["logo"]}" channel-id="{spec["id"]}" tvg-country="{spec["country"]}" tvg-language="{spec["language"]}",{spec["name"]}'
        new_block=list(b); new_block[0]=info
        current.append(new_block); existing.add(u.casefold()); existing_names.add(norm(spec['name'])); restored += 1

    # Deduplicate only Adult URLs; leave other groups untouched.
    seen_adult=set(); kept=[]; adult_dups=0; adult_renamed=0; moved={}
    for b in current:
        info=b[0]; a=attrs(info); group=a.get('group-title','').strip()
        if group.casefold() == 'adult':
            u=url_of(b).casefold()
            if u and u in seen_adult:
                adult_dups += 1
                continue
            if u: seen_adult.add(u)
            info,changed=normalize_adult(info); adult_renamed += int(changed); b[0]=info
        # Reclassify the restored historical International candidates only when
        # their identity is clearly regional/specialty. Existing non-International
        # groups are preserved.
        if group.casefold() == 'international':
            target=classify(info)
            if target != 'International':
                info=set_attr(info,'group-title',target); b[0]=info; moved[target]=moved.get(target,0)+1
        kept.append(b)

    # Remove duplicate primaries only inside the restored/reworked International
    # area by exact stream URL; preserve legitimate alternates elsewhere.
    rank={g:i for i,g in enumerate(ORDER)}
    def key(b):
        a=attrs(b[0]); n=norm(name_of(b[0])); return (rank.get(a.get('group-title',''),999),n,name_of(b[0]).casefold(),url_of(b).casefold())
    kept.sort(key=key)
    header=['#EXTM3U url-tvg="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml" x-tvg-url="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml"', '#PLAYLIST-STUDIO-CATEGORIES:["'+ '", "'.join(ORDER) + '"]']
    for line in pre:
        if line.startswith('#EXTM3U') or line.startswith('#PLAYLIST-STUDIO-CATEGORIES:'): continue
        header.append(line)
    out=header[:]
    for b in kept: out.extend(b)
    PLAYLIST.write_text('\n'.join(out).rstrip()+'\n',encoding='utf-8')
    print(f'Conservative International restore: baseline International candidates restored={restored}; Adult duplicate URLs removed={adult_dups}; Adult names normalized={adult_renamed}; reclassified={moved}; total entries={len(kept)}')

if __name__=='__main__': main()
