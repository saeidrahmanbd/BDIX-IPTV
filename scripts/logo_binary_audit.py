#!/usr/bin/env python3
"""Read-only binary logo audit against both published playlists."""
import argparse, difflib, hashlib, json, re, subprocess, io, urllib.request, urllib.error, urllib.parse, xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
PLAYLISTS = ("IPTV-Playlist.m3u", "International-Playlist.m3u")
CLEANUP = "48b402a1ebbf1239d8ecabf485c477e95d97d85c"
ATTR = re.compile(r'\btvg-logo="([^"]*)"')
EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".bmp", ".avif"}

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()

def norm(p):
    s = Path(p).stem.lower()
    s = re.sub(r"-[0-9a-f]{8,}$", "", s)
    s = re.sub(r"-(?:\d{3,4}p|\d{3,4}x\d{3,4})$", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)

def local_path(value):
    u = urlparse(value.strip())
    p = unquote(u.path if u.scheme else value.split("?",1)[0].split("#",1)[0])
    if "/logos/" in p: return "logos/" + p.split("/logos/",1)[1]
    if p.startswith("logos/"): return p
    return None

def validate(p):
    try:
        from PIL import Image
        with Image.open(p) as im: im.verify()
        with Image.open(p) as im: im.load()
        return True, "Pillow decode OK"
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def verify_http_asset(rel):
    """Fetch the published raw URL and verify HTTP delivery and image bytes."""
    url = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/" + urllib.parse.quote(rel, safe="/")
    request = urllib.request.Request(url, headers={
        "User-Agent": "BDIX-IPTV-logo-http-audit/1.0",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    })
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            status = getattr(response, "status", 200)
            content_type = response.headers.get("Content-Type", "")
            data = response.read(10 * 1024 * 1024 + 1)
            if status != 200:
                return {"path": rel, "url": url, "http_status": status, "valid": False, "reason": "Unexpected HTTP status"}
            if len(data) > 10 * 1024 * 1024:
                return {"path": rel, "url": url, "http_status": status, "valid": False, "reason": "Response exceeded 10 MiB safety limit"}
            suffix = Path(rel).suffix.lower()
            if suffix == ".svg":
                root = ET.fromstring(data)
                if not str(root.tag).lower().endswith("svg"):
                    raise ValueError("XML root is not SVG")
            else:
                from PIL import Image
                with Image.open(io.BytesIO(data)) as image:
                    image.verify()
                with Image.open(io.BytesIO(data)) as image:
                    image.load()
                    dimensions = list(image.size)
            result = {"path": rel, "url": url, "http_status": status, "content_type": content_type,
                      "bytes": len(data), "valid": True, "reason": "HTTP 200 and image content decoded"}
            if suffix != ".svg":
                result["dimensions"] = dimensions
            return result
    except Exception as exc:
        status = getattr(exc, "code", None)
        return {"path": rel, "url": url, "http_status": status, "valid": False,
                "reason": f"{type(exc).__name__}: {str(exc)[:180]}"}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--json",default="reports/logo-binary-audit.json")
    ap.add_argument("--markdown",default="reports/logo-binary-audit.md")
    a=ap.parse_args()
    assets=sorted(p for p in (ROOT/"logos").rglob("*") if p.is_file() and p.suffix.lower() in EXTS)
    info={}; hashes=defaultdict(list); stems=defaultdict(list)
    for p in assets:
        rel=p.relative_to(ROOT).as_posix()
        digest=hashlib.sha256(p.read_bytes()).hexdigest()
        blob=git("hash-object",str(p))
        ok,msg=validate(p)
        info[rel]={"sha256":digest,"blob":blob,"bytes":p.stat().st_size,"valid":ok,"validation":msg}
        hashes[digest].append(rel); stems[norm(rel)].append((rel,digest))
    refs={n:defaultdict(list) for n in PLAYLISTS}; external={n:[] for n in PLAYLISTS}
    playlist_errors=[]
    for n in PLAYLISTS:
        f=ROOT/n
        if not f.is_file(): playlist_errors.append("Missing playlist: "+n); continue
        for ln,line in enumerate(f.read_text(encoding="utf-8",errors="replace").splitlines(),1):
            if not line.startswith("#EXTINF"): continue
            m=ATTR.search(line)
            if not m: continue
            v=m.group(1); lp=local_path(v)
            if lp: refs[n][lp].append({"line":ln,"channel":line.rsplit(",",1)[-1][:100]})
            elif v: external[n].append({"line":ln,"value":v})
    referenced={p for d in refs.values() for p in d}
    missing_metadata = {}
    for n in PLAYLISTS:
        count = 0
        for line in (ROOT/n).read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("#EXTINF") and not ATTR.search(line):
                count += 1
        missing_metadata[n] = count
    missing=[]; corrupt=[]
    for n,d in refs.items():
        for p,channels in d.items():
            if not (ROOT/p).is_file(): missing.append({"playlist":n,"path":p,"channels":channels[:8]})
            elif p in info and not info[p]["valid"]: corrupt.append({"playlist":n,"path":p,"validation":info[p]["validation"]})
    duplicates=[{"sha256":h,"files":sorted(ps),"count":len(ps),"bytes_each":info[ps[0]]["bytes"]} for h,ps in hashes.items() if len(ps)>1]
    collisions=[{"normalized_stem":s,"files":[{"path":p,"sha256":h} for p,h in sorted(v)]} for s,v in stems.items() if len(v)>1 and len({h for _,h in v})>1]
    names=[(p,norm(p),info[p]["sha256"]) for p in info]
    near=[]
    for i,(p,s,h) in enumerate(names):
        if len(s)<7: continue
        for q,t,k in names[i+1:]:
            if k==h or len(t)<7 or s[:3]!=t[:3] or abs(len(s)-len(t))>2: continue
            ratio=difflib.SequenceMatcher(None,s,t).ratio()
            if ratio>=.93:
                near.append({"file_a":p,"file_b":q,"similarity":round(ratio,3)})
                if len(near)>=1000: break
        if len(near)>=1000: break
    historical={"available":False,"cleanup_commit":CLEANUP}
    try:
        parent=git("rev-parse",CLEANUP+"^")
        rows=git("ls-tree","-r",parent,"--","logos").splitlines()
        old={}
        for row in rows:
            meta,path=row.split("\t",1); mode,typ,sha=meta.split()
            if typ=="blob": old[path]=sha
        current=sorted(referenced & set(info))
        preserved=[p for p in current if info[p]["blob"] in set(old.values())]
        historical={"available":True,"cleanup_commit":CLEANUP,"parent_commit":parent,
          "pre_cleanup_logo_count":len(old),"current_referenced_local_assets":len(current),
          "current_assets_byte_identical_to_any_pre_cleanup_logo":len(preserved),
          "current_assets_without_pre_cleanup_byte_match":sorted(set(current)-set(preserved)),
          "meaning":"Git blob identity proves byte-for-byte preservation somewhere in the pre-cleanup logos tree."}
    except Exception as e: historical["error"]=str(e)
    invalid=[{"path":p,"bytes":v["bytes"],"validation":v["validation"]} for p,v in info.items() if not v["valid"]]
    http_targets = sorted(p for p in referenced if p.startswith("logos/"))
    with ThreadPoolExecutor(max_workers=20) as pool:
        http_checks = list(pool.map(verify_http_asset, http_targets))
    http_failures = [x for x in http_checks if not x["valid"]]
    report={"repository_head":git("rev-parse","HEAD"),"asset_count":len(assets),
      "asset_bytes":sum(v["bytes"] for v in info.values()),
      "playlists":{n:{"logo_references":sum(map(len,refs[n].values()),0),"unique_local_paths":len(refs[n]),
        "missing":sum(x["playlist"]==n for x in missing),"missing_logo_metadata":missing_metadata[n],"external_or_nonlocal":len(external[n])} for n in PLAYLISTS},
      "byte_identical_duplicate_groups":sorted(duplicates,key=lambda x:(-x["count"],x["files"])),
      "missing_referenced_files":missing,"corrupt_referenced_files":corrupt,
      "invalid_assets":invalid,"http_checks":http_checks,"http_failures":http_failures,"unreferenced_assets":sorted(set(info)-referenced),
      "different_content_same_normalized_filename":collisions,"near_filename_candidates":near,
      "historical_cleanup_impact":historical,"external_logo_references":external,
      "playlist_errors":playlist_errors,"safety":"Read-only: no playlist or logo files modified or deleted."}
    jp=ROOT/a.json; mp=ROOT/a.markdown
    jp.parent.mkdir(parents=True,exist_ok=True); mp.parent.mkdir(parents=True,exist_ok=True)
    jp.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    lines=["# Binary Logo Audit","",f"- HEAD: {report['repository_head']}",
      f"- Assets scanned: {len(assets)} ({report['asset_bytes']:,} bytes)",
      f"- Byte-identical duplicate groups: {len(duplicates)}",
      f"- Missing referenced files: {len(missing)}",
      f"- Corrupt referenced files: {len(corrupt)}",
      f"- Invalid assets: {len(invalid)}",
      f"- Published raw URLs checked: {len(http_checks)}",
      f"- HTTP/content failures: {len(http_failures)}",
      f"- Unreferenced assets: {len(report['unreferenced_assets'])}",
      f"- Same-normalized-name/different-content groups: {len(collisions)}",
      f"- Near-name review candidates: {len(near)}","",
      "## Playlist summary"]
    for n,v in report["playlists"].items(): lines.append(f"- {n}: {v}")
    lines += ["","## HTTP and image-content failures"] + [f"- {x['path']}: HTTP {x.get('http_status')}; {x['reason']}" for x in http_failures[:1000]]
    lines += ["","## Historical cleanup impact","",json.dumps(historical,indent=2),"","## Duplicate groups"]
    for x in duplicates[:250]: lines.append(f"- {x['sha256']} ({x['count']}): "+", ".join(x["files"]))
    lines += ["","## Missing references"]+[f"- {x['playlist']}: {x['path']} ({x['channels'][:3]})" for x in missing[:300]]
    lines += ["","## Invalid assets"]+[f"- {x['path']}: {x['validation']}" for x in invalid[:300]]
    lines += ["","## Filename collisions"]+[f"- {x['normalized_stem']}: "+", ".join(y["path"] for y in x["files"]) for x in collisions[:300]]
    lines += ["","## Safety",report["safety"],""]
    mp.write_text("\n".join(lines),encoding="utf-8")
    print(json.dumps({k:report[k] for k in ("repository_head","asset_count","asset_bytes","playlists",
      "byte_identical_duplicate_groups","missing_referenced_files","corrupt_referenced_files","invalid_assets",
      "unreferenced_assets","different_content_same_normalized_filename","near_filename_candidates","historical_cleanup_impact")},indent=2))

if __name__=="__main__": main()
