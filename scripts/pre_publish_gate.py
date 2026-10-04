#!/usr/bin/env python3
"""Final non-destructive publication gate for playlist changes."""
import re,subprocess,sys
from datetime import datetime,timezone
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
    cur_all_groups=defaultdict(set)
    for _,a,u in current:
        cur_all_groups[u.lower()].add(a.get("group-title","").strip())
    quarantined=[]
    removed=[]
    for a,u in old_primary:
        groups=cur_all_groups.get(u.lower(), set())
        if groups & {"Backup","Not Playing"}:
            quarantined.append((a.get("tvg-name",""),u,next(iter(groups & {"Backup","Not Playing"}))))
        elif not groups:
            removed.append((a.get("tvg-name",""),u))
    blocked_removed=removed
    old_review={u.lower():a.get("group-title","").strip() for _,a,u in old if a.get("group-title","").strip() in {"New Channels","New Backup"}}
    cur_review={u.lower():a.get("group-title","").strip() for _,a,u in current if a.get("group-title","").strip() in {"New Channels","New Backup"}}
    review_reclassified=[u for u,g in old_review.items() if u in cur_review and cur_review[u] != g]
    review_promoted=[u for u,g in old_review.items() if u not in cur_review and any(x.lower()==u for _,_,x in current)]
    review_removed=[u for u,g in old_review.items() if u not in cur_review and not any(x.lower()==u for _,_,x in current)]
    reclassified=review_reclassified + review_promoted
    primary_chno=Counter(a.get("tvg-chno","").strip() for a,u in cur_primary if a.get("tvg-chno","").strip())
    chno_dupes=[n for n,c in primary_chno.items() if c>1]
    primary_identity=defaultdict(list)
    for a,u in cur_primary:
        cid=(a.get("tvg-id") or a.get("channel-id") or "").strip().lower()
        group=a.get("group-title","").strip()
        if cid:
            primary_identity[(cid,group)].append((a.get("tvg-name",""),u))
    duplicate_primary=[k for k,v in primary_identity.items() if len(v)>1]
    missing=[a.get("tvg-name","") for a,u in cur_primary if not a.get("tvg-chno","").strip()]
    issues=[]
    if dup_urls: issues.append(f"duplicate stream URLs: {len(dup_urls)}")
    if blocked_removed: issues.append(f"unapproved primary streams removed: {len(blocked_removed)}")
    if reclassified: issues.append(f"review entries reclassified: {len(reclassified)}")
    if review_removed: issues.append(f"review entries deleted: {len(review_removed)}")
    if chno_dupes: issues.append(f"duplicate primary channel numbers: {len(chno_dupes)}")
    if duplicate_primary: issues.append(f"duplicate primary identities: {len(duplicate_primary)}")
    if missing: issues.append(f"primary entries missing tvg-chno: {len(missing)}")
    status="PASS" if not issues else "BLOCK"
    old_by_url={u.lower():(a.get("tvg-name",""),a.get("group-title","")) for _,a,u in old}
    cur_by_url_all={u.lower():(a.get("tvg-name",""),a.get("group-title","")) for _,a,u in current}
    added=[u for u in cur_by_url_all if u not in old_by_url]
    removed_all=[u for u in old_by_url if u not in cur_by_url_all]
    modified=[u for u in cur_by_url_all if u in old_by_url and cur_by_url_all[u]!=old_by_url[u]]
    lines=["# Pre-Publish Safety Gate","",f"Generated: **{datetime.now(timezone.utc).isoformat(timespec="seconds")}**","",f"Status: **{status}**","",f"- Current entries: **{len(current)}**",
           f"- Duplicate stream URLs: **{len(dup_urls)}**",f"- Primary streams removed: **{len(removed)}**",f"- Primary streams quarantined: **{len(quarantined)}**",
           f"- Review entries reclassified: **{len(reclassified)}**",f"- Review entries deleted: **{len(review_removed)}**",f"- Duplicate primary channel numbers: **{len(chno_dupes)}**",
           f"- Primary entries missing tvg-chno: **{len(missing)}**",f"- Entries added this run: **{len(added)}**",f"- Entries removed this run: **{len(removed_all)}**",f"- Entries modified this run: **{len(modified)}**","","## Change Summary",
           "1. Never publish duplicate stream URLs.","2. Never silently remove an existing primary stream.",
           "3. Never silently promote/reclassify review-queue entries.",
           "4. Never silently delete New Channels or New Backup review entries.","5. Never publish duplicate or missing primary channel numbers."]
    if added:
        lines.append("Added: " + ", ".join(added[:20]) + (" ..." if len(added)>20 else ""))
    else: lines.append("Added: none")
    if removed_all:
        lines.append("Removed: " + ", ".join(removed_all[:20]) + (" ..." if len(removed_all)>20 else ""))
    else: lines.append("Removed: none")
    lines.append("Modified metadata entries: " + str(len(modified)))
    if quarantined:
        lines.append("Quarantined primary streams: " + ", ".join(f"{name} -> {group}" for name,_,group in quarantined[:20]) + (" ..." if len(quarantined)>20 else ""))
    else:
        lines.append("Quarantined primary streams: none")
    lines += ["","## Blocking Reasons"]+["- "+x for x in issues] if issues else ["","No blocking conditions detected."]
    R.parent.mkdir(parents=True,exist_ok=True); R.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("Pre-publish gate:",status)
    if issues: sys.exit(1)
if __name__=="__main__": main()
