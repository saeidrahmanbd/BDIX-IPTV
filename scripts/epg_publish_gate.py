#!/usr/bin/env python3
"""Prevent publication of an EPG that regresses materially from the previous guide."""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

OLD=Path("/tmp/bdix-epg-previous.xml")
NEW=Path("epg.xml")

def stats(path):
    if not path.exists() or path.stat().st_size == 0:
        return 0,0
    root=ET.parse(path).getroot()
    channels={x.get("id") for x in root.findall("channel") if x.get("id")}
    programmes=sum(1 for x in root.findall("programme") if x.get("channel") and x.findtext("title"))
    return len(channels), programmes

new_channels,new_programmes=stats(NEW)
if new_channels == 0 or new_programmes == 0:
    raise SystemExit("EPG gate BLOCK: generated guide has no usable channels/programmes")

if OLD.exists():
    old_channels,old_programmes=stats(OLD)
    if old_channels and new_channels < max(1, int(old_channels*0.80)):
        raise SystemExit(f"EPG gate BLOCK: channel coverage regressed below the 80% safety floor: {old_channels} -> {new_channels}")
    if old_programmes and new_programmes < max(1, int(old_programmes*0.90)):
        raise SystemExit(f"EPG gate BLOCK: programme volume regressed {old_programmes} -> {new_programmes}")

print(f"EPG gate PASS: channels={new_channels}, programmes={new_programmes}")
