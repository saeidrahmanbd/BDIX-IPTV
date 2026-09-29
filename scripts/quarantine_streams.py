#!/usr/bin/env python3
"""Move non-standard and selected failed streams to Not Playing."""
import json, re
from pathlib import Path
from urllib.parse import urlsplit

PLAYLIST=Path("IPTV-Playlist.m3u")
HEALTH=Path("reports/stream-health-state.json")
REPORT=Path("reports/not-playing-quarantine.md")
ATTR_RE=re.compile(r'([\w-]+)="([^"]*)"')
FAILURE_THRESHOLD=3
BAD_EXT={".mpd",".mp3",".aac",".m4a",".ogg",".oga",".wav",".flac",".opus",".webm",".mp4",".mkv",".avi",".mov"}
BAD_HOST={"youtube.com","www.youtube.com","m.youtube.com","youtu.be","www.youtu.be"}

def attrs(s): return dict(ATTR_RE.findall(s))

def group_set(line, group):
    if 'group-title="' in line:
        return re.sub(r'(group-title=")[^"]*(")', lambda m: m.group(1)+group+m.group(2), line, count=1)
    p=line.find(',')
    return line if p<0 else line[:p]+' group-title="'+group+'"'+line[p:]

def blocks(text):
    lines=text.replace('\r','').splitlines(); head=[]; out=[]; i=0
    while i<len(lines) and not lines[i].startswith('#EXTINF'): head.append(lines[i]); i+=1
    while i<len(lines):
        if not lines[i].startswith('#EXTINF'): head.append(lines[i]); i+=1; continue
        b=[lines[i]]; i+=1
        while i<len(lines) and not lines[i].startswith('#EXTINF'): b.append(lines[i]); i+=1
        out.append(b)
    return head,out

def url_of(b):
    for x in b[1:]:
        if x.strip().startswith(('http://','https://')): return x.strip()
    return ''

def nonstandard(url):
    if not url: return ''
    if re.search(r"[?&](token|auth)=(?:test|testpub)(?:&|$)", url, re.I):
        return "test credential"
    if re.search(r"https?://[^/@]+@[^/]+", url, re.I):
        return "URL contains userinfo"
    if re.search(r"[?&]hdnts=$", url, re.I):
        return "empty hdnts parameter"
    try: p=urlsplit(url)
    except ValueError: return 'invalid URL syntax'
    if p.scheme.lower() not in {'http','https'}: return 'unsupported URL scheme'
    host=(p.hostname or '').lower().rstrip('.')
    if host in BAD_HOST or host.endswith('.youtube.com'): return 'YouTube URL'
    path=p.path.lower()
    if path.endswith('.mpd') or '/manifest.mpd' in path: return 'MPEG-DASH manifest'
    for ext in BAD_EXT:
        if path.endswith(ext): return 'non-standard media extension: '+ext
    return ''

def main():
    head, bs=blocks(PLAYLIST.read_text(encoding='utf-8-sig'))
    try: state=json.loads(HEALTH.read_text(encoding='utf-8')) if HEALTH.is_file() else {}
    except Exception as e: raise SystemExit('Cannot read stream health state: '+str(e))
    kept=[]; moved=[]
    for b in bs:
        a=attrs(b[0]); group=a.get('group-title','').strip(); url=url_of(b)
        if group == 'Not Playing': kept.append(b); continue
        reason=nonstandard(url)
        if not reason and url:
            entry=state.get(url.lower(),{})
            status=str(entry.get('status','')).strip()
            streak=int(entry.get('failure_streak',0) or 0)
            # A single GitHub-runner failure is not enough to quarantine a stream.
            # Providers may reject/geo-filter the runner while the stream remains
            # playable for real IPTV clients. Require consecutive failures.
            if status in {'Timeout','HTTP error','Invalid HLS','Connection error','Segment/variant error','Segment error'} and streak >= FAILURE_THRESHOLD:
                reason=f'{status} after {streak} consecutive health failures'
        if reason:
            b=list(b); b[0]=group_set(b[0],'Not Playing')
            moved.append((a.get('tvg-name') or b[0].rsplit(',',1)[-1].strip(),a.get('tvg-id') or a.get('channel-id') or '',group,reason,url,b))
        else: kept.append(b)
    kept.extend(x[5] for x in moved)
    out=head[:]
    for b in kept: out.extend(b)
    new='\n'.join(out).rstrip()+'\n'
    old=PLAYLIST.read_text(encoding='utf-8-sig').replace('\r','')
    if new!=old: PLAYLIST.write_text(new,encoding='utf-8',newline='\n')
    lines=['# Not Playing Quarantine','','Automatically moved non-standard streams and streams with at least 3 consecutive health-check failures.','','## Moved Streams','']
    lines += (['- **'+n+'** ['+cid+'] — '+g+' → Not Playing — '+r+' — '+u for n,cid,g,r,u,_ in moved] or ['None.'])
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('Quarantine moved:',len(moved))

if __name__=='__main__': main()