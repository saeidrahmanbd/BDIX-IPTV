#!/usr/bin/env python3
import json, re, socket, time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

PLAYLIST=Path('IPTV-Playlist.m3u')
REPORT=Path('reports/stream-health.md')
STATE=Path('reports/stream-health-state.json')
PRIORITY=Path('reports/stream-priority.json')
TIMEOUT=8
WORKERS=24
FAILURE_THRESHOLD=3
ATTR_RE=re.compile(r'([\w-]+)="([^"]*)"')

def attrs(s): return dict(ATTR_RE.findall(s))

def parse(text):
    lines=text.replace('\r','').splitlines(); out=[]; i=0
    while i<len(lines):
        if lines[i].startswith('#EXTINF'):
            info=lines[i]; j=i+1
            while j<len(lines) and not lines[j].strip(): j+=1
            if j<len(lines) and lines[j].startswith(('http://','https://')):
                a=attrs(info)
                out.append({'name':a.get('tvg-name') or info.rsplit(',',1)[-1].strip(),'id':a.get('tvg-id') or a.get('channel-id') or '','group':a.get('group-title') or '','url':lines[j].strip()})
            i=j
        i+=1
    return out

def check(e):
    r=dict(e); r.update(status='Connection error',detail='',latency_ms=0)
    start=time.monotonic()
    try:
        req=Request(e['url'],headers={'User-Agent':'BDIX-IPTV-StreamHealth/1.0','Accept':'*/*','Range':'bytes=0-8191','Connection':'close'})
        with urlopen(req,timeout=TIMEOUT) as x:
            status=getattr(x,'status',200); final=x.geturl(); c=x.headers.get('Content-Type','').lower()
            r['redirect']=final.rstrip('/')!=e['url'].rstrip('/')
            if status<200 or status>=400: r.update(status='HTTP error',detail='HTTP '+str(status)); return r
            is_hls=e['url'].lower().split('?')[0].endswith(('.m3u8','.m3u')) or 'mpegurl' in c
            body=x.read(98304)
            if is_hls:
                s=body.decode('utf-8','replace').lstrip('\ufeff \r\n\t')
                if '#EXTM3U' not in s and '#EXT-X-' not in s: r.update(status='Invalid HLS',detail='missing HLS markers'); return r
                if '#EXTINF:' not in s and '#EXT-X-STREAM-INF:' not in s: r.update(status='Invalid HLS',detail='no media/master markers'); return r
            elif not body: r.update(status='HTTP error',detail='empty response'); return r
            r.update(status='Redirect/temporary' if r['redirect'] else 'Healthy',detail='reachable'); return r
    except HTTPError as x: r.update(status='HTTP error',detail='HTTP '+str(x.code))
    except (TimeoutError,socket.timeout): r.update(status='Timeout',detail='request exceeded timeout')
    except (URLError,ConnectionError,OSError) as x: r.update(status='Connection error',detail=str(getattr(x,'reason',x))[:200])
    except Exception as x: r.update(status='Connection error',detail=str(x)[:200])
    finally: r['latency_ms']=round((time.monotonic()-start)*1000)
    return r

def main():
    entries=parse(PLAYLIST.read_text(encoding='utf-8-sig')); unique={}
    for e in entries: unique.setdefault(e['url'].lower(),e)
    active=[e for e in unique.values() if e['group'].strip()!='Not Playing']
    not_playing=[e for e in unique.values() if e['group'].strip()=='Not Playing']
    results=[]
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        fs=[pool.submit(check,e) for e in active]
        for f in as_completed(fs): results.append(f.result())
    state={}
    if STATE.is_file():
        try: state=json.loads(STATE.read_text(encoding='utf-8'))
        except Exception: state={}
    now=datetime.now(timezone.utc).isoformat(timespec='seconds')
    for e in results:
        k=e['url'].lower(); old=state.get(k,{})
        if e['status'] in ('Healthy','Redirect/temporary'): streak=0; first=None
        else: streak=int(old.get('failure_streak',0))+1; first=old.get('first_failed') or now
        state[k]={'name':e['name'],'id':e['id'],'group':e['group'],'status':e['status'],'failure_streak':streak,'first_failed':first,'last_checked':now,'last_detail':e['detail']}
    for e in not_playing:
        state[e['url'].lower()]={'name':e['name'],'id':e['id'],'group':e['group'],'status':'Not Playing','failure_streak':0,'first_failed':None,'last_checked':now,'last_detail':'intentionally excluded from active scoring'}
    state={k:v for k,v in state.items() if k in unique}
    STATE.parent.mkdir(parents=True,exist_ok=True); STATE.write_text(json.dumps(state,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    counts=Counter(e['status'] for e in results); counts['Not Playing']=len(not_playing)

    # Build a logical primary/backup hierarchy without rewriting playlist order.
    # A healthy stream is preferred; repeated failures are required before a
    # stream can lose preference. Existing playlist order is the tie-breaker.
    by_id={}
    for e in results:
        cid=e['id'].strip().lower() or e['name'].strip().lower()
        by_id.setdefault(cid,[]).append(e)
    priority={}
    score={'Healthy':100,'Redirect/temporary':90,'HTTP error':20,'Invalid HLS':15,'Connection error':10,'Timeout':5}
    for cid, group in by_id.items():
        ranked=[]
        for e in group:
            st=state[e['url'].lower()]
            streak=int(st.get('failure_streak',0))
            base=score.get(e['status'],0)
            # A transient failure does not immediately demote a stream.
            if streak < FAILURE_THRESHOLD and e['status'] not in ('Healthy','Redirect/temporary'):
                base=70
            if streak >= FAILURE_THRESHOLD:
                base=0
            group_backup=e['group'].strip()=='Backup'
            # Keep a healthy existing primary ahead of a backup unless it has
            # actually accumulated repeated failures.
            if not group_backup and base>0:
                base += 5
            ranked.append((base,e))
        ranked.sort(key=lambda x:(-x[0], x[1]['name'].lower(), x[1]['url'].lower()))
        rows=[]
        for rank,(value,e) in enumerate(ranked,1):
            role='Primary' if rank==1 else 'Backup '+str(rank-1)
            rows.append({'role':role,'url':e['url'],'name':e['name'],'status':e['status'],'failure_streak':state[e['url'].lower()]['failure_streak'],'score':value})
        priority[cid]=rows
    PRIORITY.parent.mkdir(parents=True,exist_ok=True)
    PRIORITY.write_text(json.dumps({'generated':now,'channels':priority},ensure_ascii=False,indent=2,sort_keys=True)+'\\n',encoding='utf-8')

    candidates=[e for e in results if state[e['url'].lower()]['failure_streak']>=FAILURE_THRESHOLD]
    lines=['# Stream Health','', 'Last checked: **'+now+'**','', 'Non-destructive availability check of the current playlist.','', '## Summary','',
           '- Unique stream URLs checked: **'+str(len(results))+'**', '- Healthy: **'+str(counts['Healthy'])+'**', '- Redirect/temporary: **'+str(counts['Redirect/temporary'])+'**',
           '- Timeout: **'+str(counts['Timeout'])+'**', '- HTTP error: **'+str(counts['HTTP error'])+'**', '- Invalid HLS: **'+str(counts['Invalid HLS'])+'**',
           '- Connection error: **'+str(counts['Connection error'])+'**', '- Not Playing: **'+str(counts['Not Playing'])+'**', '- Repeated-failure candidates (>= '+str(FAILURE_THRESHOLD)+' runs): **'+str(len(candidates))+'**','',
           '## Policy','', '- A failed check never deletes a stream automatically.', '- A stream needs '+str(FAILURE_THRESHOLD)+' consecutive failed health runs before it is listed as an obsolete candidate.',
           '- A later successful check resets the failure streak to zero.', '- Valid redirects do not count as failures.', '- Not Playing entries are excluded from active failure scoring.','',
           '## Primary / Backup Hierarchy','',
           'The hierarchy below is logical maintenance metadata; the playlist itself is not reordered or rewritten.',
           'Primary is the currently preferred stream. Backup 1, Backup 2, etc. are ordered alternatives based on health and repeated-failure history.','',
           'See `reports/stream-priority.json` for the machine-readable hierarchy.','',
           '## Repeated-Failure Candidates','']
    if candidates:
        for e in sorted(candidates,key=lambda x:(-state[x['url'].lower()]['failure_streak'],x['name'].lower())):
            n=state[e['url'].lower()]['failure_streak']; lines.append('- **'+e['name']+'** — '+e['id']+' — '+str(n)+' consecutive failures — '+e['status']+' — '+e['url'])
    else: lines.append('None.')
    lines += ['', '## Detailed Results','']
    for status in ('Timeout','HTTP error','Invalid HLS','Connection error','Redirect/temporary','Healthy'):
        group=[e for e in results if e['status']==status]
        if not group: continue
        lines += ['### '+status,'']
        for e in sorted(group,key=lambda x:x['name'].lower()):
            streak=state[e['url'].lower()]['failure_streak']; suffix=' — failure streak: '+str(streak) if streak else ''
            lines.append('- **'+e['name']+'** ('+e['id']+') — '+e['detail']+suffix+' — '+e['url'])
        lines.append('')
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
    print('Stream health:',dict(counts),'obsolete_candidates=',len(candidates))

if __name__=='__main__': main()