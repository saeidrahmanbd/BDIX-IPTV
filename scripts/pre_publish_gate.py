#!/usr/bin/env python3
"""Final non-destructive publication gate for playlist changes."""
import re,subprocess,sys
from collections import Counter,defaultdict
from pathlib import Path
P=Path("IPTV-Playlist.m3u"); R=Path("reports/pre-publish-gate.md")
ATTR=re.compile(r'([\w-]+)="([^"]*)"'); EXCLUDE={"Backup","New Backup","New Channels","Not Playing"}
def attrs(s): return dict(ATTR.findall(s))
def parse(text):
    lines=text.replace("\r","").splitlines(); out=[]; cur=None
    for line in lines:
        if line.startswith("#EXTINF:"): cur=(line,attrs(line))
        elif cur and line.strip().startswith(("http://","https://")): out.append((cur[0],cur[1],line.strip())); cur=None
    return out
def main():
    current=parse(P.read_text(encoding="utf-8-sig"))
    try: old=parse(subprocess.check_output(["git","show","HEAD:IPTV-Playlist.m3u"],text=True))
    except Exception: old=[]
    cur_urls=Counter(u.lower() for _,_,u in current)
    dup_urls=[u for u,n in cur_urls.items() if n>1]
    cur_primary=[(a,u) for _,a,u in current if a.get("group-title","").strip() not in EXCLUDE]
    old_primary=[(a,u) for _,a,u in old if a.get("group-title","").strip() not in EXCLUDE]
    cur_by_url=defaultdict(list)
    for a,u in cur_primary: cur_by_url[u.lower()].append(a)
    removed=[(a.get("tvg-name",""),u) for a,u in old_primary if not cur_by_url.get(u.lower())]
    old_review={u.lower():a.get("group-title","").strip() for _,a,u in old if a.get("group-title","").strip() in {"New Channels","New Backup"}}
    cur_review={u.lower():a.get("group-title","").strip() for _,a,u in current if a.get("group-title","").strip() in {"New Channels","New Backup"}}
    reclassified=[u for u,g in old_review.items() if u not in cur_review and any(x.lower()==u for _,_,x in current)]
    primary_chno=Counter(a.get("tvg-chno","").strip() for a,u in cur_primary if a.get("tvg-chno","").strip())
    chno_dupes=[n for n,c in primary_chno.items() if c>1]
    missing=[a.get("tvg-name","") for a,u in cur_primary if not a.get("tvg-chno","").strip()]
    issues=[]
    if dup_urls: issues.append(f"duplicate stream URLs: {len(dup_urls)}")
    if removed: issues.append(f"primary streams removed: {len(removed)}")
    if reclassified: issues.append(f"review entries reclassified: {len(reclassified)}")
    if chno_dupes: issues.append(f"duplicate primary channel numbers: {len(chno_dupes)}")
    if missing: issues.append(f"primary entries missing tvg-chno: {len(missing)}")
    status="PASS" if not issues else "BLOCK"
    lines=["# Pre-Publish Safety Gate","",f"Status: **{status}**","",f"- Current entries: **{len(current)}**",
           f"- Duplicate stream URLs: **{len(dup_urls)}**",f"- Primary streams removed: **{len(removed)}**",
           f"- Review entries reclassified: **{len(reclassified)}**",f"- Duplicate primary channel numbers: **{len(chno_dupes)}**",
           f"- Primary entries missing tvg-chno: **{len(missing)}**","","## Rules",
           "1. Never publish duplicate stream URLs.","2. Never silently remove an existing primary stream.",
           "3. Never silently promote/reclassify review-queue entries.","4. Never publish duplicate or missing primary channel numbers."]
    lines += ["","## Blocking Reasons"]+["- "+x for x in issues] if issues else ["","No blocking conditions detected."]
    R.parent.mkdir(parents=True,exist_ok=True); R.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("Pre-publish gate:",status)
    if issues: sys.exit(1)
if __name__=="__main__": main()
