#!/usr/bin/env python3
"""Generate a meaningful, non-destructive IPTV changelog from the previous playlist state."""
import re, subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
PLAYLIST=ROOT/"IPTV-Playlist.m3u"
STATE=ROOT/"reports/changelog-state.json"
DOC_CHANGELOG=ROOT/"assets/docs/CHANGELOG.md"
ATTR_RE=re.compile(r'([\w-]+)="([^"]*)"')

def attrs(s): return dict(ATTR_RE.findall(s))

def split_extinf(line):
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

def parse(text):
    lines=text.replace("\r","").splitlines()
    out=[]; i=0
    while i<len(lines):
        if lines[i].startswith("#EXTINF:"):
            a=attrs(lines[i])
            url=lines[i+1].strip() if i+1<len(lines) else ""
            if url.startswith(("http://","https://")):
                out.append({
                    "id":(a.get("tvg-id") or a.get("channel-id") or "").strip(),
                    "name":(a.get("tvg-name") or split_extinf(lines[i])[1]).strip(),
                    "group":a.get("group-title","").strip(),
                    "logo":a.get("tvg-logo","").strip(),
                    "url":url
                })
            i+=1
        i+=1
    return out

def current_playlist_commit():
    try:
        return subprocess.check_output(
            ["git","log","-1","--format=%H","--","IPTV-Playlist.m3u"],
            cwd=ROOT,text=True,stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return ""

def previous_playlist(current_commit):
    try:
        old_commit=""
        if STATE.is_file():
            old_commit=json.loads(STATE.read_text(encoding="utf-8")).get("playlist_commit","")
        if not old_commit:
            commits=subprocess.check_output(
                ["git","log","--format=%H","--","IPTV-Playlist.m3u"],
                cwd=ROOT,text=True,stderr=subprocess.DEVNULL
            ).splitlines()
            if len(commits)>1:
                old_commit=commits[1]
        if not old_commit or old_commit==current_commit:
            return ""
        return subprocess.check_output(
            ["git","show",f"{old_commit}:IPTV-Playlist.m3u"],
            cwd=ROOT,text=True,stderr=subprocess.DEVNULL
        )
    except Exception:
        return ""

def meaningful(prev,cur):
    if not prev:
        return {"added":len(parse(cur)),"removed":0,"backup_updated":0,"logos":0,"duplicates":0,"replaced":0,"new_names":[],"removed_names":[]}

    old=parse(prev); new=parse(PLAYLIST.read_text(encoding="utf-8-sig"))
    old_urls={x["url"] for x in old}; new_urls={x["url"] for x in new}
    old_by_id=defaultdict(list); new_by_id=defaultdict(list)
    for x in old: old_by_id[x["id"].lower()].append(x)
    for x in new: new_by_id[x["id"].lower()].append(x)

    added=[x for x in new if x["url"] not in old_urls]
    removed=[x for x in old if x["url"] not in new_urls]

    new_channels=[x for x in added if x["group"]=="New Channels" and x["id"].lower() not in {y["id"].lower() for y in old}]
    removed_channels=[x for x in removed if x["group"] not in {"Backup","New Channels","New Backup","New","Not Playing"} and x["id"].lower() not in {y["id"].lower() for y in new}]

    backup_updated=0
    for x in added:
        if x["group"]=="Backup" and any(y["id"].lower()==x["id"].lower() and y["group"]=="Backup" for y in removed):
            backup_updated+=1

    replaced=0
    for x in added:
        if any(y["id"].lower()==x["id"].lower() and y["url"]!=x["url"] for y in removed):
            replaced+=1

    logo_changes=0
    old_map={(x["id"].lower(),x["url"]):x["logo"] for x in old}
    new_map={(x["id"].lower(),x["url"]):x["logo"] for x in new}
    for k,v in new_map.items():
        if k in old_map and old_map[k]!=v: logo_changes+=1

    duplicate_old=len(old_urls)-len(old)
    duplicate_new=len(new_urls)-len(new)

    review_backups=[x for x in added if x["group"]=="New Backup"]
    return {
        "added":len(new_channels),
        "review_backups":len(review_backups),
        "removed":len(removed_channels),
        "backup_updated":backup_updated,
        "logos":logo_changes,
        "duplicates":max(0,duplicate_old-duplicate_new),
        "replaced":replaced,
        "new_names":[x["name"] for x in new_channels[:20]],
        "removed_names":[x["name"] for x in removed_channels[:20]]
    }

def main():
    cur=PLAYLIST.read_text(encoding="utf-8-sig")
    current_commit=current_playlist_commit()
    prev=previous_playlist(current_commit)
    state_commit=""
    if STATE.is_file():
        try: state_commit=json.loads(STATE.read_text(encoding="utf-8")).get("playlist_commit","")
        except Exception: state_commit=""
    if not prev and state_commit==current_commit:
        s={"added":0,"review_backups":0,"removed":0,"backup_updated":0,"logos":0,"duplicates":0,"replaced":0,"new_names":[],"removed_names":[]}
    else:
        s=meaningful(prev,cur)
    date=datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines=[f"# Changelog — {date}","",f"## {date}",""]
    if s["added"]: lines.append(f"- 🆕 **{s['added']} new channel candidate(s) added to New Channels**")
    if s.get("review_backups"): lines.append(f"- 🔁 **{s['review_backups']} new backup candidate(s) added to New Backup**")
    if s["removed"]: lines.append(f"- 🗑️ **{s['removed']} channel(s) removed**")
    if s["backup_updated"]: lines.append(f"- 🔄 **{s['backup_updated']} backup stream(s) updated**")
    if s["logos"]: lines.append(f"- 🖼️ **{s['logos']} logo reference(s) corrected**")
    if s["duplicates"]: lines.append(f"- 🧹 **{s['duplicates']} duplicate stream occurrence(s) removed**")
    if s["replaced"]: lines.append(f"- 📡 **{s['replaced']} stream(s) replaced**")
    if len(lines)==4: lines.append("- No meaningful playlist changes detected.")
    if s["new_names"]:
        lines += ["","### New channels"]
        lines += [f"- {x}" for x in s["new_names"]]
    if s["removed_names"]:
        lines += ["","### Removed channels"]
        lines += [f"- {x}" for x in s["removed_names"]]
    lines += ["","_Generated automatically from the repository playlist diff._",""]

    STATE.parent.mkdir(parents=True,exist_ok=True)
    STATE.write_text(json.dumps({"playlist_commit":current_commit,"generated":datetime.now(timezone.utc).isoformat()},indent=2)+"\n",encoding="utf-8")

    existing=DOC_CHANGELOG.read_text(encoding="utf-8") if DOC_CHANGELOG.exists() else "# BDIX-IPTV Changelog\n\n"
    entry="\n".join(lines[2:-2])
    marker=f"## {date}"
    if marker in existing:
        prefix, rest = existing.split(marker, 1)
        next_match=re.search(r"\n## \d{4}-\d{2}-\d{2}\n", rest)
        suffix = rest[next_match.start():] if next_match else ""
        existing = prefix.rstrip()+"\n\n"+entry+"\n"+suffix.lstrip("\n")
    else:
        existing = existing.rstrip()+"\n\n"+entry+"\n"
    DOC_CHANGELOG.write_text(existing,encoding="utf-8")

    print("\n".join(lines))

if __name__=="__main__": main()
