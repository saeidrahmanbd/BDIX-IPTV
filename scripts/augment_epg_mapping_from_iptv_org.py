#!/usr/bin/env python3
"""Augment the playlist EPG mapping from the build-time iptv-org guide.

Only exact normalized channel-name matches are applied. No fuzzy matching is
used, and Bangladesh domestic channels require an explicit identity match.
"""
import csv, re, xml.etree.ElementTree as ET
from pathlib import Path

PLAYLIST=Path("IPTV-Playlist.m3u")
MAPPING=Path("reports/epg-india-channel-mapping.csv")
GUIDE=Path("/tmp/iptv-org-guide.xml")


def norm(s):
    s=str(s or "").lower()
    s=re.sub(r"\b(hd|sd|uhd|fhd|tv|channel)\b", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def playlist_channels():
    out=[]
    cur=None
    for line in PLAYLIST.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("#EXTINF:"):
            attrs=dict(re.findall(r'([\w-]+)="([^"]*)"',line))
            cur=(attrs.get("tvg-id",""),attrs.get("tvg-name","") or line.rsplit(",",1)[-1].strip(),attrs.get("group-title",""))
        elif cur and line.strip().startswith(("http://","https://")):
            if cur[0] and cur[2] not in {"Backup","Not Playing","Test"}: out.append(cur)
            cur=None
    return out


def guide_names():
    names={}
    for _,elem in ET.iterparse(GUIDE,events=("end",)):
        if elem.tag=="channel":
            cid=elem.attrib.get("id","").strip()
            if cid:
                for dn in elem.findall("display-name"):
                    key=norm(dn.text)
                    if key: names.setdefault(key,[]).append(cid)
            elem.clear()
    return names


def main():
    if not GUIDE.is_file() or GUIDE.stat().st_size==0:
        print("No build-time iptv-org guide; nothing to augment.")
        return
    channels=playlist_channels(); names=guide_names()
    rows=[]
    with MAPPING.open(encoding="utf-8-sig",newline="") as fh:
        rows=list(csv.DictReader(fh))
    by_id={r.get("tvg_id",""):r for r in rows}
    applied=0
    for tvg_id,name,group in channels:
        row=by_id.get(tvg_id)
        if not row or row.get("epg_id","").strip(): continue
        hits=list(dict.fromkeys(names.get(norm(name),[])))
        if len(hits)!=1: continue
        if group=="Bangladesh" and not (tvg_id.lower().endswith(".bd") or tvg_id.lower().startswith("custom.btv")):
            continue
        row["epg_id"]=hits[0]
        row["source"]=(row.get("source","")+" | iptv-org/epg exact-name").strip(" |")
        row["status"]="MAPPED_ID_ONLY"
        row["note"]="Exact normalized display-name match from build-time iptv-org/epg guide."
        applied+=1
    fieldnames=["group","channel","tvg_id","epg_id","source","status","note"]
    with MAPPING.open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=fieldnames); w.writeheader(); w.writerows(rows)
    print(f"iptv-org exact-name EPG mappings added: {applied}")

if __name__=="__main__": main()
