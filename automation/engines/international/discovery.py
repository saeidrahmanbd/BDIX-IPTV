"""International discovery adapter; country/logo uncertainty is warning-only in manual-review queues."""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import sys
from urllib.request import Request, urlopen
from automation.engines.iptv.candidate_engine import DiscoveryCandidate

MAX_SOURCE_BYTES=50*1024*1024
DEFAULT_TIMEOUT=90
UNRESTRICTED_COUNTRIES={"BD","IN","PK"}

@dataclass(frozen=True)
class InternationalDiscoveryBatch:
    candidates: tuple[DiscoveryCandidate,...]
    warnings: tuple[str,...]
    rejected_reasons: tuple[tuple[str,int],...]
    source_rows: int

@lru_cache(maxsize=1)
def _policy_module():
    root=Path(__file__).resolve().parents[3]
    scripts=str(root/"scripts")
    added=scripts not in sys.path
    if added:
        sys.path.insert(0,scripts)
    try:
        import discover_international_channels as policy
        return policy
    finally:
        if added:
            try:
                sys.path.remove(scripts)
            except ValueError:
                pass

def fetch_international_source(url: str | None = None, timeout: int = DEFAULT_TIMEOUT) -> str:
    policy=_policy_module()
    source=url or policy.SOURCE_URL
    if source != policy.SOURCE_URL:
        raise ValueError("International discovery source URL is not approved")
    if timeout < 1 or timeout > 180:
        raise ValueError("source timeout must be between 1 and 180 seconds")
    request=Request(source,headers={"User-Agent":"BDIX-IPTV-AutomationV2/1.0"})
    with urlopen(request,timeout=timeout) as response:
        raw=response.read(MAX_SOURCE_BYTES+1)
    if not raw or len(raw)>MAX_SOURCE_BYTES:
        raise ValueError("International source is empty or exceeds the size limit")
    return raw.decode("utf-8-sig","replace")

def _local_logo(root: Path, value: str) -> str:
    if not value.startswith("logos/"):
        return ""
    candidate=(root/value).resolve()
    if not candidate.is_relative_to(root.resolve()) or not candidate.is_file():
        return ""
    if "unused" in candidate.parts or candidate.suffix.lower() not in {".png",".jpg",".jpeg",".webp",".svg"}:
        return ""
    return value

def _build_extinf(attrs: dict[str,str], name: str, group: str) -> str:
    fields=[]
    for key in ("tvg-id","tvg-name","tvg-logo","tvg-country","tvg-language","channel-id","tvg-content"):
        value=(attrs.get(key) or "").replace('"',"").strip()
        if value:
            fields.append(f'{key}="{value}"')
    if not attrs.get("tvg-name","").strip():
        fields.append(f'tvg-name="{name.replace(chr(34),"").strip()}"')
    fields.append(f'group-title="{group}"')
    return "#EXTINF:-1 " + " ".join(fields) + "," + name.replace('"',"").strip()

def build_international_discovery_batch(playlist_text: str, source_text: str,
                                        repository_root: str | Path,
                                        max_new_channels: int = 50,
                                        max_new_backups: int = 50) -> InternationalDiscoveryBatch:
    """Build manual-review candidates; BD/IN/PK are unrestricted and other verified countries are Movie/Music-only."""
    policy=_policy_module()
    root=Path(repository_root).resolve()
    _,existing=policy.parse(playlist_text)
    existing_urls={policy.stream_url_key(policy.url_of(row)) for row in existing if policy.url_of(row)}
    existing_identities=set()
    for row in existing:
        attrs=policy.attrs(row[0])
        identity=policy.primary_identity(attrs,policy.name_of(row))
        if identity:
            existing_identities.add(policy.norm(identity))

    _,source_rows=policy.parse(source_text)
    rejected={}
    warnings=[]
    candidates=[]
    seen_urls=set(existing_urls)
    for row in source_rows:
        attrs=policy.attrs(row[0])
        name=policy.name_of(row)
        url=policy.url_of(row)
        if not name or policy.BAD_NAME_RE.search(name):
            rejected["test/VOD/non-TV name"] = rejected.get("test/VOD/non-TV name",0)+1
            continue
        if not policy.safe_url(url):
            rejected["unsafe or tokenized URL"] = rejected.get("unsafe or tokenized URL",0)+1
            continue
        key=policy.stream_url_key(url)
        if key in seen_urls:
            rejected["duplicate stream URL"] = rejected.get("duplicate stream URL",0)+1
            continue
        declared_country=policy.country_code({"tvg-country":attrs.get("tvg-country","")})
        id_country=policy.country_code({"tvg-id":attrs.get("tvg-id",""),"channel-id":attrs.get("channel-id","")})
        country_conflict=declared_country!="ZZ" and id_country!="ZZ" and declared_country!=id_country
        code="ZZ" if country_conflict else policy.country_code(attrs)
        if code not in UNRESTRICTED_COUNTRIES and code != "ZZ":
            _,reason,_=policy.policy(attrs,name)
            if reason:
                rejected[reason]=rejected.get(reason,0)+1
                continue
        elif code=="ZZ":
            warnings.append(f"{name}: country could not be verified; retained in manual-review queue")

        if country_conflict:
            warnings.append(f"{name}: tvg-country conflicts with channel ID; retained without country-based filtering for owner review")
        elif declared_country=="ZZ" and id_country=="ZZ" and code=="ZZ":
            warnings.append(f"{name}: country could not be verified; retained in manual-review queue")
        elif declared_country=="ZZ" and code!="ZZ":
            warnings.append(f"{name}: tvg-country missing or unverified; source ID retained for owner review")

        safe_attrs=dict(attrs)
        original_logo=(safe_attrs.get("tvg-logo") or "").strip()
        logo=_local_logo(root,original_logo)
        if original_logo and not logo:
            warnings.append(f"{name}: external/unavailable logo omitted; retained for owner review")
        elif not logo:
            warnings.append(f"{name}: no authentic local logo found; retained for owner review")
        if logo:
            safe_attrs["tvg-logo"]=logo
        else:
            safe_attrs.pop("tvg-logo",None)

        identity=policy.norm(policy.primary_identity(safe_attrs,name))
        backup=identity in existing_identities
        queue="New Backups" if backup else "New Channels"
        candidates.append((name,url,_build_extinf(safe_attrs,name,queue),backup,identity))
        seen_urls.add(key)
        if identity:
            existing_identities.add(identity)

    candidates.sort(key=lambda item:(item[3],policy.norm(item[0]),item[1]))
    new=[]; backups=[]
    for name,url,extinf,backup,identity in candidates:
        target=backups if backup else new
        limit=max_new_backups if backup else max_new_channels
        if len(target)<limit:
            target.append(DiscoveryCandidate(extinf,url,backup=backup))
    return InternationalDiscoveryBatch(tuple(new+backups),tuple(sorted(set(warnings))),
                                       tuple(sorted(rejected.items())),len(source_rows))
