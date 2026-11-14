#!/usr/bin/env python3
"""Final non-destructive publication gate for IPTV playlist changes."""
from __future__ import annotations
import hashlib,re,subprocess,json
from collections import Counter,defaultdict
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit
from country_verification import reference_from_playlists,verify_country
from stream_url_identity import stream_url_key
from logo_asset_naming import is_blocked_logo_basename
from restore_protected_review import is_authorized_removal
P=Path("IPTV-Playlist.m3u"); R=Path("reports/pre-publish-gate.md")
EXCLUDE={"Backup","Review","Not Playing","New Channels","New Backups"}; REVIEW_QUEUES={"New Channels","New Backups"}
RAW_BASE="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"; ATTR=re.compile(r'([\w-]+)="([^"]*)"')
RAW_NAME_TAG=re.compile(r"\s*(?:\[[^]]*(?:geo-blocked|geo blocked)[^]]*\]|\((?:\d{3,4}p|\d{3,4}i|UHD|FHD|HD|SD)\)|\s+(?:\d{3,4}p|\d{3,4}i))\s*$",re.I)
def attrs(s): return dict(ATTR.findall(s))
def identity_key(value):
    """Normalize only feed-quality suffixes while retaining the channel identity."""
    value = str(value or "").strip().casefold()
    return value.split("@", 1)[0] if value else ""


def parse(text):
    lines=text.replace("\r","").splitlines(); out=[]; cur=None
    for line in lines:
        if line.startswith("#EXTINF:"): cur=(line,attrs(line))
        elif cur and line.strip().startswith(("http://","https://")): out.append((cur[0],cur[1],line.strip())); cur=None
    return out
def referenced_logo_relative_path(logo):
    """Return a safe repository-relative asset path, preserving nested logo folders."""
    if not logo.startswith(RAW_BASE):
        return None
    raw_path = urlsplit(logo).path
    marker = "/main/logos/"
    if marker not in raw_path:
        return None
    relative = unquote(raw_path.split(marker, 1)[1]).lstrip("/")
    if not relative:
        return None
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        return None
    return candidate


def referenced_logo_file(logo, logos_root=Path("logos")):
    """Resolve a logo URL under logos_root without permitting path traversal."""
    relative = referenced_logo_relative_path(logo)
    if relative is None:
        return None
    root = Path(logos_root).resolve()
    target = (root / relative).resolve()
    if target == root or root not in target.parents:
        return None
    return target


def approved_removal(url):
    u=url.lower(); return bool(re.search(r'https?://[^/]*vods?\d*\.[^/]+/',u) or re.search(r'/vod(?:/|$)',u) or 'api.toonamiaftermath.com:3000/movies/' in u or 'tvsen5.aynaott.com/tk2bndfsdfsdf/' in u)
def logo_audit(entries):
    missing=[]; review_missing=[]; external=[]; bad=[]
    for _,a,_ in entries:
        name=a.get("tvg-name","").strip(); logo=a.get("tvg-logo","").strip(); group=a.get("group-title","").strip()
        if not logo:
            (review_missing if group in {"Review","New Channels","New Backups","Not Playing"} else missing).append(name)
            continue
        if not logo.startswith(RAW_BASE): external.append(name)
        filename=Path(logo.split("?",1)[0]).name.casefold()
        if group not in EXCLUDE and filename.startswith("generated-fallback-"): bad.append((name,group,filename))
        elif is_blocked_logo_basename(filename): bad.append((name,group,filename))
    return missing,review_missing,external,bad
def review_state(entries):
    out={}
    for info,a,u in entries:
        group=a.get("group-title","").strip()
        # Permanent-removal allowlist entries are intentionally removed by policy;
        # do not misreport them as accidental deletions from protected review queues.
        if group in EXCLUDE and not is_authorized_removal(info,u):
            out[stream_url_key(u)]={"group":group,"name":a.get("tvg-name","").strip(),"id":(a.get("tvg-id") or a.get("channel-id") or "").strip().lower()}
    return out
def main():
    current=parse(P.read_text(encoding="utf-8-sig"))
    try: old=parse(subprocess.check_output(["git","show","HEAD:IPTV-Playlist.m3u"],text=True))
    except (subprocess.CalledProcessError, OSError, UnicodeError): old=[]
    cur_urls=Counter(stream_url_key(u) for _,_,u in current); dup_urls=[u for u,n in cur_urls.items() if n>1]
    cur_primary=[(a,u) for _,a,u in current if a.get("group-title","").strip() not in EXCLUDE]
    old_primary=[(info,a,u) for info,a,u in old if a.get("group-title","").strip() not in EXCLUDE]
    cur_all_groups=defaultdict(set)
    for _,a,u in current: cur_all_groups[stream_url_key(u)].add(a.get("group-title","").strip())
    quarantined=[]; removed=[]; approved_removed=[]
    for info,a,u in old_primary:
        groups=cur_all_groups.get(stream_url_key(u),set())
        if groups & {"Backup","Review","New Channels","New Backups"}: quarantined.append((a.get("tvg-name",""),u,next(iter(groups & {"Backup","Review","New Channels","New Backups"}))))
        elif not groups: (approved_removed if (approved_removal(u) or is_authorized_removal(info,u)) else removed).append((a.get("tvg-name",""),u))
    old_review=review_state(old); cur_review=review_state(current); current_by_url={stream_url_key(u):(a,u) for _,a,u in current}
    review_reclassified=[]; review_promoted=[]; review_removed=[]
    for url,state in old_review.items():
        cur=cur_review.get(url)
        if cur and cur["group"]!=state["group"]:
            if (state["group"],cur["group"]) not in {("Backup","Review"),("Not Playing","Review")}:
                review_reclassified.append((state["name"],url,state["group"],cur["group"]))
        elif not cur and url in current_by_url:
            # No owner-migration exception exists in the owner-curated architecture.
            review_promoted.append((state["name"],url,state["group"]))
        elif not cur and url not in current_by_url: review_removed.append((state["name"],url,state["group"]))
    primary_chno=Counter(a.get("tvg-chno","").strip() for a,_ in cur_primary if a.get("tvg-chno","").strip()); chno_dupes=[n for n,c in primary_chno.items() if c>1]
    primary_identity=defaultdict(list)
    for a,u in cur_primary:
        for cid in {value.strip().casefold() for value in (a.get("tvg-id",""),a.get("channel-id","")) if value.strip()}:
            primary_identity[cid].append((a.get("tvg-name",""),a.get("group-title",""),u))
    duplicate_primary=[k for k,v in primary_identity.items() if len(v)>1]
    primary_ids={identity_key(value) for value in primary_identity}
    orphan_backups=[]
    incomplete_metadata=[]
    id_pair_conflicts=[]
    missing_languages=[]
    for _,a,u in current:
        group=a.get("group-title","").strip()
        ids={identity_key(value) for value in (a.get("tvg-id",""),a.get("channel-id","")) if value.strip()}
        if group=="Backup" and not (ids & primary_ids): orphan_backups.append(a.get("tvg-name",""))
        if a.get("tvg-id","").strip() and a.get("channel-id","").strip() and a["tvg-id"].strip().casefold()!=a["channel-id"].strip().casefold():
            id_pair_conflicts.append(a.get("tvg-name",""))
        if not a.get("tvg-language","").strip(): missing_languages.append(a.get("tvg-name",""))
        if group not in {"Review","Not Playing","New Channels","New Backups"}:
            missing_fields=[key for key in ("tvg-name","tvg-id","channel-id","tvg-country","tvg-logo") if not a.get(key,"").strip()]
            if missing_fields: incomplete_metadata.append((a.get("tvg-name",""),missing_fields))
    missing=[a.get("tvg-name","") for a,_ in cur_primary if not a.get("tvg-chno","").strip()]
    chno_sequence_issues=[(index+1,a.get("tvg-name",""),a.get("tvg-chno","").strip() or "(missing)") for index,(a,_) in enumerate(cur_primary) if a.get("tvg-chno","").strip()!=str(index+1)]
    review_numbered=[a.get("tvg-name","") for _,a,_ in current if a.get("group-title","").strip() in EXCLUDE and a.get("tvg-chno","").strip()]
    # Every published group, including Backup and review queues, must agree on
    # the display name for a given channel ID. This catches the common case
    # where a newly discovered backup uses a different source spelling.
    metadata_by_id=defaultdict(list)
    for _,a,u in current:
        group=a.get("group-title","").strip(); cid=(a.get("tvg-id") or a.get("channel-id") or "").strip().casefold(); name=a.get("tvg-name","").strip()
        if cid and group not in {"New Channels","New Backups","Review","Not Playing"}: metadata_by_id[cid].append((name,group,u))
    metadata_conflicts={cid:items for cid,items in metadata_by_id.items() if len({x[0].casefold() for x in items})>1}
    raw_name_issues=[(a.get("tvg-name",""),a.get("group-title","")) for _,a,_ in current if RAW_NAME_TAG.search(a.get("tvg-name","").strip())]
    logo_missing,logo_missing_review,logo_external,logo_bad=logo_audit(current); logo_missing_files=[]; logo_missing_file_details=[]
    for _,a,_ in current:
        logo=a.get("tvg-logo","").strip()
        if logo.startswith(RAW_BASE):
            relative=referenced_logo_relative_path(logo)
            logo_file=referenced_logo_file(logo)
            if relative is None or logo_file is None or not logo_file.is_file():
                name=a.get("tvg-name","")
                group=a.get("group-title","")
                report_path=relative.as_posix() if relative is not None else Path(urlsplit(logo).path).name
                logo_missing_files.append(name)
                logo_missing_file_details.append((name,group,report_path))
    issues=[]
    warnings=[]
    # Hard blockers are integrity/safety violations, not unresolved owner-review
    # metadata. Discovery queues are intentionally provisional and must never
    # stop the daily workflow merely because country, logo or metadata is pending.
    if dup_urls: issues.append(f"duplicate stream URLs: {len(dup_urls)}")
    if removed: issues.append(f"unapproved primary streams removed: {len(removed)}")
    if review_reclassified: issues.append(f"review entries reclassified: {len(review_reclassified)}")
    if review_promoted: issues.append(f"protected review entries promoted: {len(review_promoted)}")
    if review_removed: issues.append(f"protected review entries deleted: {len(review_removed)}")
    if chno_dupes: issues.append(f"duplicate primary channel numbers: {len(chno_dupes)}")
    if duplicate_primary: issues.append(f"duplicate primary identities: {len(duplicate_primary)}")

    # These findings remain visible in the report, but automation cannot
    # resolve them by moving, deleting or renumbering owner-curated rows.
    if orphan_backups: warnings.append(f"orphan Backup entries awaiting owner review: {len(orphan_backups)}")
    if incomplete_metadata: warnings.append(f"active entries with incomplete identity/country/logo metadata: {len(incomplete_metadata)}")
    if id_pair_conflicts: warnings.append(f"tvg-id/channel-id inconsistencies: {len(id_pair_conflicts)}")
    if missing_languages: warnings.append(f"entries missing tvg-language: {len(missing_languages)}")
    if missing: warnings.append(f"primary entries missing tvg-chno: {len(missing)}")
    if review_numbered: warnings.append(f"Backup/Review/discovery entries still numbered: {len(review_numbered)}")
    if metadata_conflicts: warnings.append(f"same-ID metadata name conflicts: {len(metadata_conflicts)}")
    if raw_name_issues: warnings.append(f"raw resolution/geoblock tags in channel names: {len(raw_name_issues)}")
    if logo_missing: warnings.append(f"missing logos: {len(logo_missing)}")
    if logo_external: warnings.append(f"external logo URLs: {len(logo_external)}")
    if logo_bad: warnings.append(f"incorrect/placeholder/generic logos: {len(logo_bad)}")
    if logo_missing_files: warnings.append(f"referenced local logo files missing from repository: {len(logo_missing_files)}")

    queue_errors=[]; country_reference=reference_from_playlists([P,Path("International-Playlist.m3u")])
    for _,a,u in current:
        group=a.get("group-title","").strip()
        if group not in REVIEW_QUEUES: continue
        country=a.get("tvg-country","").strip().upper()
        if country not in {"BD","IN"}: queue_errors.append(f"{a.get('tvg-name','')} has provisional/unverified queue country {country or 'missing'}")
        else:
            verdict=verify_country(a,a.get("tvg-name",""),country_reference)
            if not verdict.ok: queue_errors.append(f"{a.get('tvg-name','')} country not verified as BD/IN ({verdict.reason})")
            elif verdict.country!=country: queue_errors.append(f"{a.get('tvg-name','')} tvg-country {country} conflicts with verified {verdict.country}")
        if not u.lower().startswith(("http://","https://")): queue_errors.append(f"{a.get('tvg-name','')} has invalid stream URL")
    if queue_errors: warnings.append(f"New queue candidates pending owner review: {len(queue_errors)}")
    status="PASS" if not issues else "BLOCK"
    old_by_url={stream_url_key(u):(a.get("tvg-name",""),a.get("group-title","")) for _,a,u in old}; cur_by_url_all={stream_url_key(u):(a.get("tvg-name",""),a.get("group-title","")) for _,a,u in current}
    added=[u for u in cur_by_url_all if u not in old_by_url]; removed_all=[u for u in old_by_url if u not in cur_by_url_all]; modified=[u for u in cur_by_url_all if u in old_by_url and cur_by_url_all[u]!=old_by_url[u]]
    lines=["# Pre-Publish Safety Gate","",f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**",f"Source playlist SHA-256: **{hashlib.sha256(P.read_bytes()).hexdigest()}**","",f"Status: **{status}**","",f"- Current entries: **{len(current)}**",f"- Duplicate stream URLs: **{len(dup_urls)}**",f"- Primary streams removed: **{len(removed)}**",f"- Primary streams intentionally removed as known bad: **{len(approved_removed)}**",f"- Primary streams quarantined: **{len(quarantined)}**",f"- Review entries reclassified: **{len(review_reclassified)}**",f"- Review entries promoted: **{len(review_promoted)}**",f"- Review entries deleted: **{len(review_removed)}**",f"- Duplicate primary channel numbers: **{len(chno_dupes)}**",f"- Primary entries missing channel numbers: **{len(missing)}**",f"- Primary channel-number sequence issues (non-blocking; existing row order is protected): **{len(chno_sequence_issues)}**",f"- Numbered review entries: **{len(review_numbered)}**",f"- Same-ID metadata name conflicts: **{len(metadata_conflicts)}**",f"- Orphan Backup entries: **{len(orphan_backups)}**",f"- Active rows with incomplete required metadata: **{len(incomplete_metadata)}**",f"- tvg-id/channel-id inconsistencies: **{len(id_pair_conflicts)}**",f"- Entries missing tvg-language: **{len(missing_languages)}**",f"- Raw resolution/geoblock name tags: **{len(raw_name_issues)}**",f"- Missing logos in active groups: **{len(logo_missing)}**",f"- Missing logos deferred in review groups (Review/New Channels/New Backups): **{len(logo_missing_review)}**",f"- External logo URLs: **{len(logo_external)}**",f"- Incorrect/placeholder/generic logos: **{len(logo_bad)}**",f"- Missing referenced local logo files: **{len(logo_missing_files)}**",f"- Entries added this run: **{len(added)}**",f"- Entries removed this run: **{len(removed_all)}**",f"- Entries modified this run: **{len(modified)}**","","## Protected-queue policy","New Channels and New Backups are discovery queues. Backup and Review remain protected, and Review entries are retained for future rechecks. No automatic migration, promotion, regrouping or renumbering of existing rows is authorized; existing row order, group assignments, channel numbers and stream URLs are protected. Review, New Channels and New Backups are excluded from Xtream.","","## Channel-Number Sequence Review",f"Existing playlist row order is preserved; numbering sequence discrepancies are reported for review and do not trigger automatic reordering. Issues found: **{len(chno_sequence_issues)}**.","","## Blocking Reasons"]
    lines.extend("- "+x for x in issues) if issues else lines.append("No hard safety blockers detected.")
    lines += ["","## Warnings / Manual Review",""]
    lines.extend("- "+x for x in warnings) if warnings else lines.append("No outstanding metadata or discovery warnings.")
    lines += ["","## Review-queue logo gaps","","These entries have no verified local logo available yet. They remain in the review queue without an external or placeholder logo.",""]
    lines.extend(f"- **{name}**" for name in logo_missing_review) if logo_missing_review else lines.append("None.")
    lines += ["","## Metadata conflicts",""]
    if metadata_conflicts:
        for cid,items in sorted(metadata_conflicts.items()): lines.append(f"- **{cid}** — "+"; ".join(f"{n} [{g}]" for n,g,_ in items))
    else: lines.append("None.")
    lines += ["","## Raw name tags",""]
    lines.extend(f"- **{n}** — {g}" for n,g in raw_name_issues) if raw_name_issues else lines.append("None.")
    lines += ["","## Queue validation",""]; lines.extend("- "+x for x in queue_errors) if queue_errors else lines.append("New Channels/New Backups contain only validated BD/IN entries.")
    lines += ["","## Missing local logo files","","| Channel | Group | Referenced filename |","|---|---|---|"]
    if logo_missing_file_details:
        clean=lambda value:str(value).replace("|","\\|").replace("\\n"," ")
        lines.extend(f"| {clean(name)} | {clean(group)} | {clean(filename)} |" for name,group,filename in logo_missing_file_details)
    else: lines.append("| — | — | none |")
    lines += ["","## Blocked logo references","","| Channel | Group | Blocked filename |","|---|---|---|"]
    if logo_bad:
        clean=lambda value:str(value).replace("|","\\|").replace("\n"," "); lines.extend(f"| {clean(name)} | {clean(group)} | {clean(filename)} |" for name,group,filename in logo_bad)
    else: lines.append("| — | — | none |")
    R.parent.mkdir(parents=True,exist_ok=True); R.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("Pre-publish gate:",status)
    for issue in issues: print(f"::error::Pre-publish gate blocking reason: {issue}")
    for warning in warnings: print(f"::warning::Pre-publish gate review item: {warning}")
    for name,group,filename in logo_bad[:20]: print(f"::warning::Blocked logo reference: {name} [{group}] -> {filename}")
    for name,group,filename in logo_missing_file_details[:50]: print(f"::warning::Missing local logo file: {name} [{group}] -> logos/{filename}")
    for error in queue_errors[:20]: print(f"::warning::Discovery queue review: {error}")
    if issues: raise SystemExit(1)
if __name__=="__main__": main()
