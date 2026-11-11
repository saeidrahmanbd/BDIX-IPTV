#!/usr/bin/env python3
"""Verify an IPTV logo migration changed logo metadata/assets only."""
import argparse
import re
from pathlib import Path
from urllib.parse import unquote

from PIL import Image

PLAYLIST = Path("IPTV-Playlist.m3u")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"


def attrs(line):
    return dict(re.findall(r'([\w-]+)="([^"]*)"', line))


def strip_logo(line):
    return re.sub(r'\s+tvg-logo="[^"]*"', "", line, count=1)


def local_path(value):
    if value.startswith(RAW_BASE):
        relative = unquote(value[len(RAW_BASE):].split("?", 1)[0].split("#", 1)[0])
    elif value.startswith("logos/"):
        relative = unquote(value[len("logos/"):])
    else:
        raise ValueError(f"Non-local logo reference: {value}")
    path = Path(relative)
    if path.is_absolute() or not path.parts or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError(f"Unsafe local logo path: {value}")
    root = Path("logos").resolve()
    target = (root / path).resolve()
    if target == root or root not in target.parents:
        raise ValueError(f"Logo path escapes the repository logos directory: {value}")
    if not target.is_file():
        raise ValueError(f"Referenced logo file is missing: {target}")
    if target.suffix.lower() == ".svg":
        raw = target.read_text(encoding="utf-8", errors="strict")
        if "<svg" not in raw[:4096].lower() or "</svg>" not in raw[-4096:].lower():
            raise ValueError(f"Invalid SVG logo: {target}")
    else:
        with Image.open(target) as im:
            im.verify()
    return target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("before", help="Pre-migration playlist snapshot")
    args = parser.parse_args()

    before_text = Path(args.before).read_text(encoding="utf-8-sig")
    after_text = PLAYLIST.read_text(encoding="utf-8-sig")
    before_lines = before_text.replace("\r", "").splitlines()
    after_lines = after_text.replace("\r", "").splitlines()

    before_ext = [x for x in before_lines if x.startswith("#EXTINF:")]
    after_ext = [x for x in after_lines if x.startswith("#EXTINF:")]
    if len(before_ext) != len(after_ext):
        raise SystemExit(f"Refusing publish: EXTINF count changed ({len(before_ext)} -> {len(after_ext)}).")

    before_other = [x for x in before_lines if not x.startswith("#EXTINF:")]
    after_other = [x for x in after_lines if not x.startswith("#EXTINF:")]
    if before_other != after_other:
        raise SystemExit("Refusing publish: non-EXTINF playlist data changed.")

    local_count = missing_count = 0
    for index, (old, new) in enumerate(zip(before_ext, after_ext), start=1):
        if strip_logo(old) != strip_logo(new):
            raise SystemExit(f"Refusing publish: non-logo EXTINF metadata changed at record {index}.")
        value = attrs(new).get("tvg-logo", "").strip()
        if not value:
            missing_count += 1
            continue
        local_path(value)
        local_count += 1

    print(f"Logo-only verification passed: {len(after_ext)} entries; {local_count} valid local logo references; {missing_count} still unresolved.")
    print("Verified unchanged: row order, stream URL lines, group titles, tvg-id, channel-id, numbering, and all non-logo metadata.")


if __name__ == "__main__":
    main()
