#!/usr/bin/env python3
"""Conservative Wikimedia Commons logo replacement for generic CHANNEL MARK SVGs."""
import json, re, time, unicodedata
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

PLAYLIST = Path("NVisionBD-Playlist.m3u")
LOGOS = Path("logos")
REPORT = Path("reports/generic-logo-replacement-results.md")
UA = "BDIX-IPTV-logo-audit/1.0 (https://github.com/saeidrahmanbd/BDIX-IPTV)"

def norm(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()

def fetch_json(url):
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=25) as response:
        return json.loads(response.read().decode("utf-8"))

def is_generic(relative):
    relative_path = Path(relative)
    path = relative_path if relative_path.parts and relative_path.parts[0] == "logos" else LOGOS / relative_path
    if path.suffix.lower() != ".svg" or not path.is_file():
        return False
    return "CHANNEL MARK" in path.read_text(encoding="utf-8", errors="ignore").upper()

def find_candidate(channel):
    query = 'filetype:bitmap "' + channel.replace('"', "") + '" logo'
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": query, "gsrnamespace": 6, "gsrlimit": 10,
        "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata"
    }
    data = fetch_json("https://commons.wikimedia.org/w/api.php?" + urlencode(params))
    tokens = [token for token in norm(channel).split() if len(token) > 1]
    found = []
    for page in ((data.get("query") or {}).get("pages") or {}).values():
        title = page.get("title", "").replace("File:", "")
        stem = norm(Path(title).stem)
        overlap = sum(token in stem.split() for token in tokens) / max(1, len(tokens))
        if overlap < 0.8 or not any(word in stem for word in ("logo", "brand", "channel")):
            continue
        infos = page.get("imageinfo") or []
        if not infos:
            continue
        info = infos[0]
        mime = info.get("mime", "")
        if mime not in ("image/png", "image/jpeg", "image/webp"):
            continue
        if info.get("width", 0) < 80 or info.get("height", 0) < 40:
            continue
        metadata = info.get("extmetadata") or {}
        license_name = (metadata.get("LicenseShortName") or {}).get("value", "").strip()
        license_url = (metadata.get("LicenseUrl") or {}).get("value", "").strip()
        if license_name and license_url and info.get("url"):
            found.append((overlap, page, info, license_name, license_url))
    found.sort(key=lambda item: (item[0], item[2].get("width", 0) * item[2].get("height", 0)), reverse=True)
    if not found:
        return None
    if len(found) > 1 and found[0][0] == found[1][0]:
        return None
    return found[0]

def valid_image(raw, mime):
    if len(raw) < 500 or len(raw) > 5_000_000:
        return False
    if mime == "image/png":
        return raw.startswith(b"\x89PNG\r\n\x1a\n")
    if mime == "image/jpeg":
        return raw.startswith(b"\xff\xd8\xff")
    if mime == "image/webp":
        return raw[:4] == b"RIFF" and raw[8:12] == b"WEBP"
    return False

def main():
    if not PLAYLIST.is_file():
        raise SystemExit("NVisionBD-Playlist.m3u not found")
    text = PLAYLIST.read_text(encoding="utf-8", errors="replace")
    entries = re.findall(r'(#EXTINF:[^\n]*\n)([^\n#][^\n]*)', text)
    logo_to_channel = {}
    for extinf, _stream in entries:
        match = re.search(r'tvg-logo="([^"]+)"', extinf)
        if match and is_generic(match.group(1)):
            logo_to_channel.setdefault(match.group(1), extinf.split(",", 1)[-1].strip())
    replacements, unresolved = [], []
    for old, channel in sorted(logo_to_channel.items()):
        try:
            candidate = find_candidate(channel)
            if not candidate:
                unresolved.append((channel, old, "No unique, close, licensed Commons match"))
                continue
            score, page, info, license_name, license_url = candidate
            mime = info["mime"]
            extension = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp"}[mime]
            new = str(Path(old).with_suffix(extension)).replace("\\", "/")
            request = Request(info["url"], headers={"User-Agent": UA})
            with urlopen(request, timeout=30) as response:
                raw = response.read()
            if not valid_image(raw, mime):
                unresolved.append((channel, old, "Downloaded image failed signature/size validation"))
                continue
            destination = LOGOS / Path(new).name
            if destination.exists():
                unresolved.append((channel, old, "Destination already exists; manual review required"))
                continue
            destination.write_bytes(raw)
            text = text.replace('tvg-logo="' + old + '"', 'tvg-logo="' + new + '"')
            replacements.append((channel, old, new, page.get("title", ""), info.get("descriptionurl", ""), license_name, license_url))
        except Exception as error:
            unresolved.append((channel, old, "Lookup/download error: " + str(error)[:140]))
        time.sleep(0.25)
    PLAYLIST.write_text(text.rstrip() + "\n", encoding="utf-8")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Generic Logo Replacement Results", "",
        "Conservative Wikimedia Commons pass. Only unique close filename matches with license metadata and valid image bytes are applied; all other assets remain unchanged.", "",
        f"- Unique generic logo files examined: {len(logo_to_channel)}",
        f"- Replaced: {len(replacements)}",
        f"- Unresolved/manual review: {len(unresolved)}", "",
        "## Replacements", "",
        "| Channel | Old file | New file | Source | License | License URL |",
        "|---|---|---|---|---|---|"
    ]
    for channel, old, new, source, url, license_name, license_url in replacements:
        lines.append(f"| {channel.replace('|', '/')} | `{old}` | `{new}` | [{source}]({url}) | {license_name} | {license_url} |")
    lines += ["", "## Unresolved", "", "| Channel | File | Reason |", "|---|---|---|"]
    for channel, path, reason in unresolved:
        lines.append(f"| {channel.replace('|', '/')} | `{path}` | {reason.replace('|', '/')} |")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"examined={len(logo_to_channel)} replaced={len(replacements)} unresolved={len(unresolved)}")

if __name__ == "__main__":
    main()
