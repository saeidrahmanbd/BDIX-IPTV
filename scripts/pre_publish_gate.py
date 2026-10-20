#!/usr/bin/env python3
"""Final non-destructive publication gate for IPTV playlist changes."""
import re,subprocess,sys
from datetime import datetime,timezone
from collections import Counter,defaultdict
from pathlib import Path
P=Path("IPTV-Playlist.m3u"); R=Path("reports/pre-publish-gate.md"); EXCLUDE={"Backup","Not Playing"}
RAW_BASE="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ATTR=re.compile(r'([\w-]+)="([^"]*)"')
BAD_ASSETS={"atn-news.png","a-sports-5485adff.png","a-sports-hd.png","bein-sports-3.png","bangla-tv.png","btv-news.png","colors.png","duronto-tv.png","duronto-tv-1ad55c95.png","ekushey-tv.png","global-tv.png","green-tv.png","mohona-tv.png","nagorik-tv.png","nagorik.png","nick-bangla.png","sananda-tv.png","sananda.png","star-gold-select.png","star-gold.png","star-plus.png","zee-tv.png","tom-and-jerry.png","arirang-tv.png"}
GENERIC_PREFIXES=("placeholder-","generic-","unknown-","unidentified-")
def attrs(s): return dict(ATTR.findall(s))
def parse(text):
 lines=text.replace("\r","").splitlines(); out=[]; cur=None
 for line in lines:
  if line.startswith("#EXTINF:"): cur=(line,attrs(line))
  elif cur and line.strip().startswith(("http://","https://")): out.append((cur[0],cur[1],line.strip())); cur=None
 return out
def approved_removal(url):
 u=url.lower()
 return bool(re.search(r'https?://[^/]*vods?\d*\.[^/]+/',u) or re.search(r'/vod(?:/|$)',u) or 'api.toonamiaftermath.com:3000/movies/' in u or 'dvltv.cc/play/' in u or 'tvsen5.aynaott.com/tk2bndfsdfsdf/' in u)
def logo_audit(entries):
 missing=[]; external=[]; bad=[]
 for _,a,_ in entries:
  name=a.get("tvg-name","").strip(); logo=a.get("tvg-logo","").strip()
  if not logo: missing.append(name); continue
  if not logo.startswith(RAW_BASE): external.append(name)
  filename=Path(logo.split("?",1)[0]).name.casefold()
  if filename in BAD_ASSETS or filename.startswith(GENERIC_PREFIXES): bad.append(name)
 return missing,external,bad
def review_state(entries):
 """Index protected review entries by exact URL, preserving category and identity."""
 out={}
 for _,a,u in entries:
  group=a.get("group-title","").strip()
  if group in EXCLUDE:
   out[u.lower()]={"group":group,"name":a.get("tvg-name","").strip(),"id":(a.get("tvg-id") or a.get("channel-id") or "").strip().lower()}
 return out
def main():
 current=parse(P.read_text(encoding="utf-8-sig"))
 try: old=parse(subprocess.check_output(["git","show","HEAD:IPTV-Playlist.m3u"],text=True))
 except Exception: old=[]
 cur_urls=Counter(u.lower() for _,_,u in current)
 dup_urls=[u for u,n in cur_urls.items() if n>1]
 cur_primary=[(a,u) for _,a,u in current if a.get("group-title","").strip() not in EXCLUDE]
 old_primary=[(a,u) for _,a,u in old if a.get("group-title","").strip() not in EXCLUDE]
 cur_all_groups=defaultdict(set)
 for _,a,u in current: cur_all_groups[u.lower()].add(a.get("group-title","").strip())
 quarantined=[]; removed=[]; approved_removed=[]
 for a,u in old_primary:
  groups=cur_all_groups.get(u.lower(),set())
  if groups & {"Backup"}: quarantined.append((a.get("tvg-name",""),u,next(iter(groups & {"Backup"}))))
  elif not groups:
   if approved_removal(u): approved_removed.append((a.get("tvg-name",""),u))
   else: removed.append((a.get("tvg-name",""),u))
 old_review=review_state(old)
 cur_review=review_state(current)
 review_reclassified=[]; review_promoted=[]; review_removed=[]
 current_urls={u.lower() for _,_,u in current}
 for url,state in old_review.items():
  cur=cur_review.get(url)
  if cur and cur["group"] != state["group"]:
   review_reclassified.append((state["name"],url,state["group"],cur["group"]))
  elif not cur and url in current_urls:
   review_promoted.append((state["name"],url,state["group"]))
  elif not cur and url not in current_urls:
   review_removed.append((state["name"],url,state["group"]))
 blocked_removed=removed
 primary_chno=Counter(a.get("tvg-chno","").strip() for a,u in cur_primary if a.get("tvg-chno","").strip())
 chno_dupes=[n for n,c in primary_chno.items() if c>1]
 primary_identity=defaultdict(list)
 for a,u in cur_primary:
  cid=(a.get("tvg-id") or a.get("channel-id") or "").strip().lower(); group=a.get("group-title","").strip()
  if cid: primary_identity[cid].append((a.get("tvg-name",""),group,u))
 duplicate_primary=[k for k,v in primary_identity.items() if len(v)>1]
 missing=[a.get("tvg-name","") for a,u in cur_primary if not a.get("tvg-chno","").strip()]
 review_numbered=[a.get("tvg-name","") for _,a,u in current if a.get("group-title","").strip() in EXCLUDE and a.get("tvg-chno","").strip()]
 logo_missing,logo_external,logo_bad=logo_audit(current)
 logo_missing_files=[]
 for _,a,_ in current:
  logo=a.get("tvg-logo","").strip()
  if logo.startswith(RAW_BASE):
   fn=Path(logo.split("?",1)[0]).name
   if not (Path("logos")/fn).is_file(): logo_missing_files.append(a.get("tvg-name",""))
 issues=[]
 if dup_urls: issues.append(f"duplicate stream URLs: {len(dup_urls)}")
 if blocked_removed: issues.append(f"unapproved primary streams removed: {len(blocked_removed)}")
 if review_reclassified: issues.append(f"review entries reclassified: {len(review_reclassified)}")
 if review_promoted: issues.append(f"protected review entries promoted: {len(review_promoted)}")
 if review_removed: issues.append(f"protected review entries deleted: {len(review_removed)}")
 if chno_dupes: issues.append(f"duplicate primary channel numbers: {len(chno_dupes)}")
 if duplicate_primary: issues.append(f"duplicate primary identities: {len(duplicate_primary)}")
 if missing: issues.append(f"primary entries missing tvg-chno: {len(missing)}")
 if review_numbered: issues.append(f"Backup/Not Playing entries still numbered: {len(review_numbered)}")
 if logo_missing: issues.append(f"missing logos: {len(logo_missing)}")
 if logo_external: issues.append(f"external logo URLs: {len(logo_external)}")
 if logo_bad: issues.append(f"incorrect/placeholder/generic logos: {len(logo_bad)}")
 if logo_missing_files: issues.append(f"referenced local logo files missing from repository: {len(logo_missing_files)}")
 status="PASS" if not issues else "BLOCK"
 old_by_url={u.lower():(a.get("tvg-name",""),a.get("group-title","")) for _,a,u in old}
 cur_by_url_all={u.lower():(a.get("tvg-name",""),a.get("group-title","")) for _,a,u in current}
 added=[u for u in cur_by_url_all if u not in old_by_url]; removed_all=[u for u in old_by_url if u not in cur_by_url_all]; modified=[u for u in cur_by_url_all if u in old_by_url and cur_by_url_all[u]!=old_by_url[u]]
 lines=["# Pre-Publish Safety Gate","",f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**","",f"Status: **{status}**","",f"- Current entries: **{len(current)}**",f"- Duplicate stream URLs: **{len(dup_urls)}**",f"- Primary streams removed: **{len(removed)}**",f"- Primary streams intentionally removed as known bad: **{len(approved_removed)}**",f"- Primary streams quarantined: **{len(quarantined)}**",f"- Review entries reclassified: **{len(review_reclassified)}**",f"- Review entries promoted: **{len(review_promoted)}**",f"- Review entries deleted: **{len(review_removed)}**",f"- Duplicate primary channel numbers: **{len(chno_dupes)}**",f"- Primary entries missing tvg-chno: **{len(missing)}**",f"- Numbered review entries: **{len(review_numbered)}**",f"- Missing logos: **{len(logo_missing)}**",f"- External logo URLs: **{len(logo_external)}**",f"- Incorrect/placeholder/generic logos: **{len(logo_bad)}**",f"- Missing referenced local logo files: **{len(logo_missing_files)}**",f"- Entries added this run: **{len(added)}**",f"- Entries removed this run: **{len(removed_all)}**",f"- Entries modified this run: **{len(modified)}**","","## Protected-queue policy","Backup and Not Playing are review queues. Existing entries are protected by exact stream URL. A maintenance run must not silently delete, promote, or reclassify them.","","## Blocking Reasons"]
 if issues: lines.extend(["- "+x for x in issues])
 else: lines.append("No blocking conditions detected.")
 R.parent.mkdir(parents=True,exist_ok=True); R.write_text("\n".join(lines)+"\n",encoding="utf-8")
 print("Pre-publish gate:",status)
 for issue in issues: print("Pre-publish blocking reason:",issue)
 if issues: sys.exit(1)
if __name__=="__main__": main()
