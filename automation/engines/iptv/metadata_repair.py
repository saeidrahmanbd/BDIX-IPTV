"""Evidence-gated IPTV metadata repair. Only metadata changes; no stream/group/number mutation."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import re
from automation.core.playlist_contract import parse_rows, assert_iptv_existing_rows_preserved

ALLOWED_FIELDS = {"tvg_name","tvg_id","tvg_logo","display_name"}
ATTR_PATTERN = re.compile(r'(?P<prefix>\b[A-Za-z0-9_-]+=")[^"]*(")')

@dataclass(frozen=True)
class MetadataPatch:
    row_index: int
    evidence: str
    approved: bool
    tvg_name: str | None = None
    tvg_id: str | None = None
    tvg_logo: str | None = None
    display_name: str | None = None

def _validate_value(value: str, field: str) -> str:
    cleaned = value.strip()
    if not cleaned or '"' in cleaned or "\n" in cleaned or "\r" in cleaned:
        raise ValueError(f"{field} must be a non-empty single-line value without quotes")
    return cleaned

def _set_attribute(header: str, attribute: str, value: str) -> str:
    pattern = re.compile(r'(\b' + re.escape(attribute) + r'=")[^"]*(")')
    if pattern.search(header):
        return pattern.sub(lambda match:match.group(1)+value+match.group(2),header,count=1)
    return header.rstrip() + f' {attribute}="{value}"'

def _validate_local_logo(root: Path, value: str) -> str:
    logo = _validate_value(value,"tvg_logo")
    if not logo.startswith("logos/"):
        raise ValueError("tvg_logo must reference a repository-local logos/ path")
    relative = Path(logo)
    if relative.is_absolute() or ".." in relative.parts or "\\" in logo:
        raise ValueError("tvg_logo path traversal is forbidden")
    logo_root_path = root / "logos"
    if logo_root_path.is_symlink() or not logo_root_path.is_dir():
        raise ValueError("tvg_logo logos root must be a real repository directory")
    current = logo_root_path
    for part in relative.parts[1:]:
        current = current / part
        if current.is_symlink():
            raise ValueError("tvg_logo path cannot contain symlinks")
    try:
        logo_root = logo_root_path.resolve(strict=True)
        target = current.resolve(strict=True)
    except FileNotFoundError as exc:
        raise ValueError("tvg_logo target must be an existing supported local image") from exc
    if not target.is_relative_to(logo_root):
        raise ValueError("tvg_logo must remain inside the repository logos directory")
    if not target.is_file() or target.suffix.lower() not in {".png",".jpg",".jpeg",".webp",".gif",".svg"}:
        raise ValueError("tvg_logo target must be an existing supported local image")
    return logo

def apply_metadata_patches(baseline_text: str, patches: list[MetadataPatch],
                           repository_root: str | Path) -> str:
    """Apply only explicitly approved, evidence-backed metadata patches in memory."""
    if not baseline_text.lstrip("\ufeff").startswith("#EXTM3U"):
        raise ValueError("baseline must have an #EXTM3U header")
    rows = parse_rows(baseline_text)
    root = Path(repository_root).resolve()
    by_index: dict[int,MetadataPatch] = {}
    for patch in patches:
        if patch.row_index < 0 or patch.row_index >= len(rows):
            raise ValueError(f"row index out of range: {patch.row_index}")
        if patch.row_index in by_index:
            raise ValueError(f"duplicate metadata patch for row: {patch.row_index}")
        if not patch.approved or not patch.evidence.strip():
            raise ValueError("metadata patch requires approval and evidence")
        if not any(getattr(patch,field) is not None for field in ALLOWED_FIELDS):
            raise ValueError("metadata patch contains no allowed field changes")
        by_index[patch.row_index] = patch
    if not by_index:
        return baseline_text

    output: list[str] = []
    row_index = 0
    for line in baseline_text.splitlines(keepends=True):
        if line.lstrip().startswith("#EXTINF:"):
            patch = by_index.get(row_index)
            if patch:
                ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
                body = line[:-len(ending)] if ending else line
                header,separator,title = body.partition(",")
                if not separator:
                    raise ValueError(f"EXTINF row {row_index} has no display title")
                if patch.tvg_name is not None:
                    header = _set_attribute(header,"tvg-name",_validate_value(patch.tvg_name,"tvg_name"))
                if patch.tvg_id is not None:
                    header = _set_attribute(header,"tvg-id",_validate_value(patch.tvg_id,"tvg_id"))
                if patch.tvg_logo is not None:
                    header = _set_attribute(header,"tvg-logo",_validate_local_logo(root,patch.tvg_logo))
                if patch.display_name is not None:
                    title = _validate_value(patch.display_name,"display_name")
                output.append(header + "," + title + ending)
            else:
                output.append(line)
            row_index += 1
        else:
            output.append(line)
    candidate = "".join(output)
    assert_iptv_existing_rows_preserved(baseline_text,candidate)
    return candidate
