#!/usr/bin/env python3
import concurrent.futures, json, re, socket, time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

PLAYLIST=Path('IPTV-Playlist.m3u')
REPORT=Path('reports/live-stream-audit.md')
TIMEOUT=10
WORKERS=24
ATTR_RE=re.compile(r'([\w-]+)="([^"]*)"')

def attrs(s): return dict(ATTR_RE.findall(s))

def parse(text):
    lines=text.replace('\\r','').splitlines(); out=[]; i=0
    while i < len(lines):
        if lines[i].startswith('#EXTINF'):
            info=lines[i]; j=i+1
            while j<len(lines) and not lines[j].strip(): j+=1
            if j<len(lines) and lines[j].startswith(('http://','https://')):
                a=attrs(info)
                out.append({'name':a.get('tvg-name') or info.rsplit(',',1)[-1].strip(),'id':a.get('tvg-id') or a.get('channel-id') or '','group':a.get('group-title') or '','url':lines[j].strip()})
            i=j
        i+=1
    return out

def get(url):
    req=Request(url,headers={'User-Agent':'BDIX-IPTV-LiveAudit/1.0','Accept':'*/*','Range':'bytes=0-131071','Connection':'close'})
    with urlopen(req,timeout=TIMEOUT) as r:
        return getattr(r,'status',200), r.geturl(), r.headers.get('Content-Type','').lower(), r.read(131072)

def check(e):
    r={**e,'status':'Connection error','detail':'','latency_ms':0,'final_url':'','content_type':'','segment_status':''}
    t=time.monotonic()
    try:
        code, final, ctype, body=get(e['url'])
        r.update(final_url=final,content_type=ctype)
        if code < 200 or code >= 400:
            r.update(status='HTTP error',detail=f'HTTP {code}'); return r
        base=final
        text=body.decode('utf-8','replace').lstrip('\\ufeff \\r\\n\\t')
        looks_hls=e['url'].lower().split('?')[0].endswith(('.m3u8','.m3u')) or 'mpegurl' in ctype
        if looks_hls:
            if '#EXTM3U' not in text and '#EXT-X-' not in text:
                r.update(status='Invalid HLS',detail='HTTP 200 but no HLS markers'); return r
            raw=text.splitlines(); variants=[]
            for idx,line in enumerate(raw):
                if '#EXT-X-STREAM-INF:' in line:
                    j=idx+1
                    while j<len(raw) and not raw[j].strip(): j+=1
                    if j<len(raw) and not raw[j].lstrip().startswith('#'): variants.append(raw[j].strip())
            lines=[x.strip() for x in raw if x.strip() and not x.startswith('#')]
            child=variants[0] if variants else (lines[0] if lines else None)
            if child:
                child_url=urljoin(base,child)
                c2,f2,ct2,b2=get(child_url)
                if c2<200 or c2>=400:
                    r.update(status='Segment/variant error',detail=f'child HTTP {c2}',segment_status=str(c2)); return r
                t2=b2.decode('utf-8','replace').lstrip('\\ufeff \\r\\n\\t')
                if '#EXTM3U' in t2 or '#EXT-X-' in t2:
                    segs=[x.strip() for x in t2.splitlines() if x.strip() and not x.startswith('#')]
                    if segs:
                        s2,f3,ct3,b3=get(urljoin(f2,segs[0]))
                        if s2<200 or s2>=400 or not b3:
                            r.update(status='Segment error',detail=f'first media segment HTTP {s2} / empty={not bool(b3)}',segment_status=str(s2)); return r
            r.update(status='Healthy' if final.rstrip('/')==e['url'].rstrip('/') else 'Redirect/temporary',detail='manifest and playable child/segment reachable'); return r
        if not body:
            r.update(status='HTTP error',detail='empty response'); return r
        r.update(status='Healthy' if final.rstrip('/')==e['url'].rstrip('/') else 'Redirect/temporary',detail='HTTP resource reachable'); return r
    except HTTPError as x: r.update(status='HTTP error',detail=f'HTTP {x.code}')
    except (TimeoutError,socket.timeout): r.update(status='Timeout',detail='request exceeded timeout')
    except (URLError,ConnectionError,OSError) as x: r.update(status='Connection error',detail=str(getattr(x,'reason',x))[:220])
    except Exception as x: r.update(status='Connection error',detail=str(x)[:220])
    finally: r['latency_ms']=round((time.monotonic()-t)*1000)
    return r

def main():
    entries=parse(PLAYLIST.read_text(encoding='utf-8-sig')); unique={}
    for e in entries: unique.setdefault(e['url'].lower(),e)
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        fs=[pool.submit(check,e) for e in unique.values()]
        for f in concurrent.futures.as_completed(fs): results.append(f.result())
    results.sort(key=lambda x:x['name'].lower()); counts={}
    for r in results: counts[r['status']]=counts.get(r['status'],0)+1
    now=time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime())
    lines=['# Live Stream Availability Audit','',f'Last checked: **{now}**','',f'- Playlist entries parsed: **{len(entries)}**',f'- Unique stream URLs tested: **{len(results)}**',f'- Duplicate URLs in playlist: **{len(entries)-len(results)}**','', '## Summary','']
    for k in ('Healthy','Redirect/temporary','Timeout','HTTP error','Invalid HLS','Segment/variant error','Segment error','Connection error'): lines.append(f'- {k}: **{counts.get(k,0)}**')
    lines += ['', '## Results by Status','']
    for status in ('Timeout','HTTP error','Invalid HLS','Segment/variant error','Segment error','Connection error','Redirect/temporary','Healthy'):
        group=[r for r in results if r['status']==status]
        if not group: continue
        lines += [f'### {status}','']
        for r in group: lines.append(f"- **{r['name']}** — {r['group']} — {r['url']} — {r['detail']} — {r['latency_ms']} ms")
        lines.append('')
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('LIVE AUDIT',json.dumps({'entries':len(entries),'unique_urls':len(results),'counts':counts},ensure_ascii=False))

if __name__=='__main__': main()
