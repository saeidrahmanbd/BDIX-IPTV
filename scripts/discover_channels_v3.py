#!/usr/bin/env python3
from __future__ import annotations
import json, shlex, unicodedata, urllib.request
from pathlib import Path
from urllib.parse import urlparse, parse_qsl, unquote_plus

P=Path("IPTV-Playlist.m3u"); R=Path("reports/channel-discovery.md"); STATE=Path("reports/discovery-state.json")
S=[("Bangladesh","https://iptv-org.github.io/iptv/countries/bd.m3u"),("India","https://iptv-org.github.io/iptv/countries/in.m3u")]
BLOCK={"sports","religious","kids"}; INDIA={"music","movies","movie","entertainment"}
BAD=("vod","catchup","catch-up","test","demo","proxy","proxied","cors","webcam","radio","podcast","event","ppv","24/7","timeshift")
HOSTBAD=("proxy","proxied","cors","localhost","workers.dev","worker.dev","pages.dev")
QBAD=("token=","auth=","authorization=","hdnts=","sig=","signature=","expires=","session=","jwt=","key=")

def attrs(line):
    try: t=shlex.split(line,posix=True)
    except ValueError: return {}
    return dict(x.split("=",1) for x in t[1:] if "=" in x)

def split_extinf(line):
    """Split EXTINF metadata from display text without breaking quoted commas."""
    in_quote = False
    escaped = False
    for i, ch in enumerate(line):
        if ch == '"' and not escaped:
            in_quote = not in_quote
        elif ch == "," and not in_quote:
            return line[:i], line[i + 1:]
        escaped = (ch == "\\") and not escaped
        if ch != "\\": escaped = False
    return line, ""

def norm(s):
    # Normalize channel names independently of quality/country/formatting labels.
    # Remove all parenthesized/bracketed metadata, not just the last suffix.
    s=unicodedata.normalize("NFKC",s).lower()
    s=s.replace("_"," ")
    while True:
        z=s
        s=s.replace("("," ").replace(")"," ").replace("["," ").replace("]"," ")
        # Remove common quality markers that may remain outside brackets.
        s=" ".join(x for x in s.split() if x not in {
            "uhd","fhd","hd","sd","4k","1080p","720p","576p","480p","360p","240p"
        })
        if s==z: break
    return "".join(c for c in s if c.isalnum() or unicodedata.category(c).startswith("L"))

def base_id(s):
    # IPTV-org often adds @SD/@HD/etc. to an identity already present locally.
    return (s or "").strip().lower().split("@",1)[0]

def parse(text):
    ls=text.replace("\r","").splitlines(); out=[]; i=0
    while i<len(ls):
        if ls[i].startswith("#EXTINF"):
            j=i+1
            while j<len(ls) and not ls[j].strip(): j+=1
            if j<len(ls) and ls[j].startswith(("http://","https://")):
                a=attrs(ls[i]); _, display=split_extinf(ls[i]); n=a.get("tvg-name") or display.strip()
                out.append((a,n.strip(),ls[j].strip())); i=j
        i+=1
    return out

def cats(a):
    z=set()
    for k in ("group-title","category","categories"):
        z.update(x.strip().lower() for x in a.get(k,"").replace("; ",",").replace("|",",").split(",") if x.strip())
    return z

def ok(country,a,n,u):
    c=cats(a); h=" ".join((n,a.get("tvg-id",""),a.get("group-title",""),a.get("category",""))).lower()
    if c&BLOCK or any(x in h for x in BAD): return False
    if country=="India" and ("news" in c or not c&INDIA): return False
    p=urlparse(u)
    if p.scheme not in ("http","https") or not p.netloc or p.fragment: return False
    # Ordinary query parameters are valid for many live streams. Reject only
    # query keys commonly used for authentication, signatures, or expiry.
    for key, value in parse_qsl(p.query, keep_blank_values=True):
        qkey=unquote_plus(key).strip().lower()
        if any(qkey == bad.rstrip("=") for bad in QBAD):
            return False
    if any(x in p.netloc.lower() for x in HOSTBAD): return False
    return p.path.lower().endswith((".m3u8",".m3u",".ts")) and "vod" not in p.path.lower() and "catchup" not in p.path.lower()

def ext(a,n,g):
    cid=(a.get("tvg-id") or a.get("channel-id") or "").strip()
    if not cid: return None
    x=f'#EXTINF:-1 tvg-id="{cid}" tvg-name="{n}"'
    if a.get("tvg-logo"): x+=f' tvg-logo="{a["tvg-logo"].strip()}"'
    x+=f' channel-id="{a.get("channel-id",cid).strip()}" group-title="{g}"'
    return x+","+n

def url_key(u):
    return (u or "").strip().lower().rstrip("/")

def load_state():
    default={"review_candidates":[],"rejected_new_channels":[],"rejected_new_backups":[]}
    if not STATE.exists():
        return default
    try:
        data=json.loads(STATE.read_text(encoding="utf-8"))
        if not isinstance(data,dict):
            return default
        for k,v in default.items():
            if not isinstance(data.get(k),list):
                data[k]=v
        return data
    except Exception:
        return default

def save_state(state):
    STATE.parent.mkdir(parents=True,exist_ok=True)
    STATE.write_text(json.dumps(state,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def rejection_key(item):
    return (url_key(item.get("url")), item.get("norm_name",""), item.get("base_id",""))

def unique_records(items):
    out=[]; seen=set()
    for item in items:
        key=rejection_key(item)
        if key not in seen:
            out.append(item); seen.add(key)
    return out


def main():
    original=P.read_text(encoding="utf-8-sig"); entries=parse(original)
    state=load_state()

    current_urls={url_key(u) for a,n,u in entries if u.strip()}
    review_prev={url_key(x.get("url")):x for x in state.get("review_candidates",[]) if url_key(x.get("url"))}
    rejected_new_channels=unique_records(state.get("rejected_new_channels",[]))
    rejected_new_backups=unique_records(state.get("rejected_new_backups",[]))

    # Anything that disappeared from the previous review queue was deliberately
    # removed by the user. Remember that decision before discovering new feeds.
    for key,item in review_prev.items():
        if key in current_urls:
            continue
        if item.get("group")=="New Channels":
            rejected_new_channels.append(item)
        elif item.get("group")=="New Backup":
            rejected_new_backups.append(item)

    rejected_new_channels=unique_records(rejected_new_channels)
    rejected_new_backups=unique_records(rejected_new_backups)

    # If a previously rejected New Channel was later manually promoted, forget
    # that rejection so future backup discovery remains useful.
    active_names={norm(n) for a,n,u in entries if a.get("group-title","").strip() not in {"Backup","New","New Channels","New Backup","Not Playing"}}
    active_ids={base_id(a.get("tvg-id") or a.get("channel-id")) for a,n,u in entries
                if a.get("group-title","").strip() not in {"Backup","New","New Channels","New Backup","Not Playing"}
                and base_id(a.get("tvg-id") or a.get("channel-id"))}
    rejected_new_channels=[
        x for x in rejected_new_channels
        if x.get("norm_name","") not in active_names
        and x.get("base_id","") not in active_ids
        and url_key(x.get("url","")) not in current_urls
    ]
    rejected_new_backups=[
        x for x in rejected_new_backups
        if url_key(x.get("url","")) not in current_urls
    ]

    pairs={(norm(n),u) for a,n,u in entries}
    existing_urls={url_key(u) for a,n,u in entries if u.strip()}
    names={norm(n) for a,n,u in entries}
    ids={base_id(a.get("tvg-id") or a.get("channel-id")) for a,n,u in entries
         if base_id(a.get("tvg-id") or a.get("channel-id"))}
    cand=[]; rejected=0; candidate_urls=set(existing_urls)
    for country,src in S:
        try:
            q=urllib.request.Request(src,headers={"User-Agent":"BDIX-IPTV-discovery/1.0"})
            text=urllib.request.urlopen(q,timeout=30).read().decode("utf-8","replace")
        except Exception as e:
            print("Source unavailable:",src,e); continue
        for a,n,u in parse(text):
            if ok(country,a,n,u) and (norm(n),u) not in pairs and url_key(u) not in candidate_urls:
                cand.append((country,a,n,u)); candidate_urls.add(url_key(u))
            elif not ok(country,a,n,u): rejected+=1
    cand.sort(key=lambda x:(x[0]!="Bangladesh",norm(x[2]),x[3]))
    new=[]; backups=[]; planned_names=set(names); planned_ids=set(ids); seen=set(pairs)
    rejected_channel_urls={url_key(x.get("url")) for x in rejected_new_channels}
    rejected_backup_urls={url_key(x.get("url")) for x in rejected_new_backups}
    rejected_channel_names={x.get("norm_name","") for x in rejected_new_channels}
    rejected_channel_ids={x.get("base_id","") for x in rejected_new_channels}

    for c,a,n,u in cand:
        pair=(norm(n),u)
        if pair in seen:
            continue

        cid=base_id(a.get("tvg-id") or a.get("channel-id"))
        name_key=norm(n)
        uk=url_key(u)

        # Existing channel identity => backup candidate. Deleting one backup
        # suppresses that exact URL, not every future backup for the channel.
        if name_key in planned_names or (cid and cid in planned_ids):
            if uk in rejected_backup_urls or uk in rejected_channel_urls:
                rejected += 1
                continue
            backups.append((c,a,n,u))
        else:
            # Deleting a New Channel suppresses the exact URL and recurring
            # discovery of the same normalized channel identity.
            if uk in rejected_channel_urls or name_key in rejected_channel_names or (cid and cid in rejected_channel_ids):
                rejected += 1
                continue
            new.append((c,a,n,u))
            planned_names.add(name_key)
            if cid: planned_ids.add(cid)
        seen.add(pair)

    seen_urls=set(existing_urls)
    unique_new=[]; unique_backups=[]
    for item in new:
        u=url_key(item[3])
        if u not in seen_urls:
            unique_new.append(item); seen_urls.add(u)
    for item in backups:
        u=url_key(item[3])
        if u not in seen_urls:
            unique_backups.append(item); seen_urls.add(u)
    new=unique_new[:40]; backups=unique_backups[:80]

    lines=original.replace("\r","").splitlines(); add=[]
    for c,a,n,u in new:
        z=ext(a,n,"New Channels")
        if z: add += [z,u]
    for c,a,n,u in backups:
        z=ext(a,n,"New Backup")
        if z: add += [z,u]

    if add:
        while lines and not lines[-1].strip():
            lines.pop()
        if lines and add:
            lines.append("")
        lines.extend(add)
        for i,l in enumerate(lines):
            if l.startswith("#PLAYLIST-STUDIO-CATEGORIES:"):
                cs=json.loads(l.split(":",1)[1])
                for g in ("New Channels","New Backup"):
                    if g not in cs:
                        cs.append(g)
                lines[i]="#PLAYLIST-STUDIO-CATEGORIES:"+json.dumps(cs,ensure_ascii=False); break
        P.write_text("\n".join(lines)+"\n",encoding="utf-8")

    # Persist the current review queue. On the next run, anything deleted from
    # this snapshot is treated as an explicit user rejection.
    final_entries=parse(P.read_text(encoding="utf-8-sig"))
    state["review_candidates"]=[
        {
            "group":a.get("group-title","").strip(),
            "name":n,
            "norm_name":norm(n),
            "base_id":base_id(a.get("tvg-id") or a.get("channel-id")),
            "url":u
        }
        for a,n,u in final_entries
        if a.get("group-title","").strip() in {"New Channels","New Backup"}
    ]
    state["rejected_new_channels"]=unique_records(rejected_new_channels)
    state["rejected_new_backups"]=unique_records(rejected_new_backups)
    save_state(state)

    R.parent.mkdir(parents=True,exist_ok=True)
    R.write_text(
        "# Channel Discovery\n\n"
        + f"- New channels: **{len(new)}**\n"
        + f"- New backups: **{len(backups)}**\n"
        + f"- Rejected/suppressed: **{rejected}**\n"
        + f"- Remembered rejected new-channel identities: **{len(rejected_new_channels)}**\n"
        + f"- Remembered rejected backup URLs: **{len(rejected_new_backups)}**\n\n"
        + "## New Channels\n\n"
        + "\n".join(f"- {n} ({c}) — {u}" for c,a,n,u in new)
        + "\n\n## New Backups\n\n"
        + "\n".join(f"- {n} ({c}) — {u}" for c,a,n,u in backups)
        + "\n",encoding="utf-8")
    print(f"Discovery: {len(new)} new channels, {len(backups)} new backups, {rejected} rejected/suppressed; review deletions are remembered.")

if __name__=="__main__": main()
