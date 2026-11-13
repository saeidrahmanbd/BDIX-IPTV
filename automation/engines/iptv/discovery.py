"""IPTV Bangladesh/India source adapter with advisory country/logo metadata and no file writes."""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import sys
from urllib.request import Request, urlopen
from automation.engines.iptv.candidate_engine import DiscoveryCandidate

MAX_SOURCE_BYTES = 50 * 1024 * 1024
DEFAULT_TIMEOUT = 45

@dataclass(frozen=True)
class DiscoveryBatch:
    candidates: tuple[DiscoveryCandidate,...]
    warnings: tuple[str,...]
    rejected_reasons: tuple[tuple[str,int],...]
    source_counts: tuple[tuple[str,int],...]

@lru_cache(maxsize=1)
def _legacy_policy():
    """Reuse the tested source eligibility policy without invoking its file-writing main()."""
    root=Path(__file__).resolve().parents[3]
    scripts=str(root/"scripts")
    added=scripts not in sys.path
    if added:
        sys.path.insert(0,scripts)
    try:
        import discover_bd_in_new_queues as policy
        return policy
    finally:
        if added:
            try:
                sys.path.remove(scripts)
            except ValueError:
                pass

def fetch_source_feed(url: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Fetch only one of the two approved iptv-org source feeds; never writes the response."""
    policy=_legacy_policy()
    approved={source for _,source in policy.SOURCES}
    if url not in approved:
        raise ValueError("discovery source URL is not in the approved source registry")
    if timeout < 1 or timeout > 120:
        raise ValueError("source timeout must be between 1 and 120 seconds")
    request=Request(url,headers={"User-Agent":"BDIX-IPTV-AutomationV2/1.0"})
    with urlopen(request,timeout=timeout) as response:
        raw=response.read(MAX_SOURCE_BYTES+1)
    if not raw or len(raw)>MAX_SOURCE_BYTES:
        raise ValueError("discovery source is empty or exceeds the size limit")
    return raw.decode("utf-8-sig","replace")

def fetch_all_source_feeds(timeout: int = DEFAULT_TIMEOUT) -> tuple[dict[str,str],tuple[str,...]]:
    """Fetch both registered feeds independently; one unavailable feed does not suppress the other."""
    policy=_legacy_policy()
    feeds: dict[str,str]={}
    warnings: list[str]=[]
    for country,url in policy.SOURCES:
        try:
            feeds[country]=fetch_source_feed(url,timeout)
        except Exception as exc:
            warnings.append(f"{country} source unavailable: {type(exc).__name__}")
    return feeds,tuple(warnings)

def _local_logo(root: Path, logo_value: str) -> str:
    if not logo_value.startswith("logos/"):
        return ""
    candidate=(root/logo_value).resolve()
    if not candidate.is_relative_to(root.resolve()) or not candidate.is_file():
        return ""
    if "unused" in candidate.parts:
        return ""
    if candidate.suffix.lower() not in {".png",".jpg",".jpeg",".webp",".svg"}:
        return ""
    return logo_value

def build_discovery_batch(playlist_text: str, source_feeds: dict[str,str],
                          repository_root: str | Path,
                          max_new_channels: int = 40,
                          max_new_backups: int = 80) -> DiscoveryBatch:
    """Build manual-review candidates; uncertain country/logo metadata is warning-only."""
    policy=_legacy_policy()
    root=Path(repository_root).resolve()
    existing=policy.parse(playlist_text)
    existing_urls={policy.stream_url_key(url) for _,_,url in existing}
    existing_names={policy.norm(name) for _,name,_ in existing}
    existing_ids={policy.base_id(attrs.get("tvg-id") or attrs.get("channel-id"))
                  for attrs,_,_ in existing
                  if policy.base_id(attrs.get("tvg-id") or attrs.get("channel-id"))}

    candidates=[]
    warnings=[]
    rejected={}
    source_counts=[]
    seen_urls=set(existing_urls)
    for country,source_text in sorted(source_feeds.items()):
        if country not in {"Bangladesh","India"}:
            warnings.append(f"Unrecognized source country ignored: {country}")
            continue
        source_rows=policy.parse(source_text)
        source_counts.append((country,len(source_rows)))
        for attrs,name,url in source_rows:
            normalized,reason=policy.evaluate(country,attrs,name,url)
            if normalized is None:
                rejected[reason or "policy rejected"] = rejected.get(reason or "policy rejected",0)+1
                continue
            key=policy.stream_url_key(url)
            if key in seen_urls:
                rejected["duplicate stream URL"] = rejected.get("duplicate stream URL",0)+1
                continue
            seen_urls.add(key)
            candidates.append((country,dict(normalized),name,url))

    candidates.sort(key=lambda item:(item[0]!="Bangladesh",policy.norm(item[2]),item[3]))
    new_channels=[]
    new_backups=[]
    planned_names=set(existing_names)
    planned_ids=set(existing_ids)
    for country,attrs,name,url in candidates:
        name_key=policy.norm(name)
        channel_id=policy.base_id(attrs.get("tvg-id") or attrs.get("channel-id"))
        is_backup=name_key in planned_names or bool(channel_id and channel_id in planned_ids)
        queue="New Backups" if is_backup else "New Channels"
        if is_backup and len(new_backups)>=max_new_backups:
            continue
        if not is_backup and len(new_channels)>=max_new_channels:
            continue

        declared_country=policy.channel_country(attrs)
        expected_country="BD" if country=="Bangladesh" else "IN"
        if declared_country is None:
            warnings.append(f"{name}: country metadata missing or unverified; retained in {queue}")
        elif declared_country != expected_country:
            warnings.append(f"{name}: source country conflicts with metadata; retained in {queue}")

        original_logo=(attrs.get("tvg-logo") or "").strip()
        local_logo=_local_logo(root,original_logo)
        if original_logo and not local_logo:
            warnings.append(f"{name}: non-local or unavailable logo omitted; retained in {queue}")
        elif not local_logo:
            warnings.append(f"{name}: no authentic local logo found; retained in {queue}")
        if local_logo:
            attrs["tvg-logo"]=local_logo
        else:
            attrs.pop("tvg-logo",None)

        extinf=policy.extinf(attrs,name,queue,country)
        discovery=DiscoveryCandidate(extinf,url,backup=is_backup)
        if is_backup:
            new_backups.append(discovery)
        else:
            new_channels.append(discovery)
            if name_key:
                planned_names.add(name_key)
            if channel_id:
                planned_ids.add(channel_id)

    return DiscoveryBatch(
        tuple(new_channels+new_backups),
        tuple(sorted(set(warnings))),
        tuple(sorted(rejected.items())),
        tuple(source_counts),
    )
