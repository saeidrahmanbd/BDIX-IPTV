#!/usr/bin/env python3
"""Enforce the immutable attribution block in one selected published M3U."""
from pathlib import Path
import sys

BLOCK=("#=================================","# Developed by: SAEID RAHMAN","# Facebook: https://www.facebook.com/saeid.rahman.sr","# Email: saeidrahman.mkt@gmail.com","#=================================")

def enforce(path: Path)->bool:
 if not path.is_file(): raise SystemExit(f"{path}: playlist not found")
 lines=path.read_text(encoding="utf-8-sig").replace("\r","").splitlines()
 if not lines or not lines[0].startswith("#EXTM3U"): raise SystemExit(f"{path}: missing #EXTM3U first line; refusing to rewrite.")
 i=1
 while i<=len(lines)-len(BLOCK):
  if tuple(lines[i:i+len(BLOCK)])==BLOCK: del lines[i:i+len(BLOCK)]
  else: i+=1
 lines[1:1]=list(BLOCK)
 content="\n".join(lines).rstrip("\n")+"\n"
 old=path.read_text(encoding="utf-8-sig").replace("\r","")
 if old!=content: path.write_text(content,encoding="utf-8"); print(f"{path}: restored protected attribution block.")
 else: print(f"{path}: attribution block verified.")
 check=path.read_text(encoding="utf-8").splitlines()
 if tuple(check[1:1+len(BLOCK)])!=BLOCK or sum(line==BLOCK[1] for line in check)!=1: raise SystemExit(f"{path}: attribution verification failed.")
 return True

if __name__=="__main__":
 paths=sys.argv[1:] or ["IPTV-Playlist.m3u"]
 for name in paths: enforce(Path(name))
