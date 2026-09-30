#!/usr/bin/env python3
"""Synchronize verified EPG mappings from the CSV into the Xtream worker."""
import csv, json, re
from pathlib import Path

CSV = Path("reports/epg-india-channel-mapping.csv")
WORKER = Path("xtream/worker.js")

def main():
    rows=[]
    with CSV.open(encoding="utf-8-sig",newline="") as fh:
        for r in csv.DictReader(fh):
            status=r.get("status","")
            if r.get("tvg_id") and r.get("epg_id") and status.startswith("MAPPED"):
                ids=[x.strip() for x in r["epg_id"].split("|") if x.strip()]
                if ids: rows.append((r["tvg_id"].strip(),ids))
    mapping={}
    for key,ids in rows:
        mapping.setdefault(key,[])
        for x in ids:
            if x not in mapping[key]: mapping[key].append(x)
    text=WORKER.read_text(encoding="utf-8")
    pattern=re.compile(r'const EPG_ID_MAP\s*=\s*\{.*?\};',re.S)
    replacement="const EPG_ID_MAP = " + json.dumps(dict(sorted(mapping.items())),ensure_ascii=False,separators=(",",":")) + ";\n"
    if not pattern.search(text): raise SystemExit("EPG_ID_MAP block not found")
    new=pattern.sub(replacement,text,count=1)
    if new!=text: WORKER.write_text(new,encoding="utf-8")
    print(f"EPG worker mappings synchronized: {len(mapping)} channel identities")

if __name__=="__main__": main()
