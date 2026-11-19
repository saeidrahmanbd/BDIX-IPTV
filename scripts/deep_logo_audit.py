#!/usr/bin/env python3
"""Read-only deep logo reference and perceptual duplicate audit."""
import hashlib,json,re,subprocess
from collections import defaultdict
from pathlib import Path
from PIL import Image,ImageOps
import numpy as np
ROOT=Path(".").resolve(); LOGO=ROOT/"logos"
PLAYLISTS=("IPTV-Playlist.m3u","International-Playlist.m3u")
IMAGE_EXT={".png",".jpg",".jpeg",".webp",".gif",".bmp",".avif",".tif",".tiff"}
TEXT_EXT={".py",".yml",".yaml",".json",".md",".txt",".m3u",".xml",".html",".js",".css",".toml",".ini",".sh",".cfg",".conf",".properties"}
EXPLICIT=re.compile(r'(?:https?://[^\s"\']+?/)?(logos/[A-Za-z0-9_./@+-]+\.(?:png|jpe?g|webp|gif|svg|bmp|avif|tiff?))',re.I)
DYNAMIC=re.compile(r'(?:tvg-logo|logo[_-]?(?:path|file|url|dir)|(?:/|["\'])logos(?:/|["\'])|Path\([^\n]{0,100}logo|glob\([^\n]{0,100}logo|joinpath\([^\n]{0,100}logo)',re.I)
def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1<<20),b""):h.update(b)
 return h.hexdigest()
def phash(p):
 with Image.open(p) as im:
  im=ImageOps.exif_transpose(im).convert("RGB")
  im.thumbnail((256,256))
  a=np.asarray(im.convert("L").resize((32,32),Image.Resampling.LANCZOS),dtype=np.float32)
 n=32
 c=np.cos((np.pi/n)*(np.arange(n)[:,None]+.5)*np.arange(n)[None,:]).astype(np.float32)
 c[:,0]*=1/np.sqrt(2);c*=np.sqrt(2/n)
 d=c.T@a@c;low=d[:8,:8].flatten();med=np.median(low[1:]);v=0
 for bit in (low>med):v=(v<<1)|int(bit)
 return v
def ham(a,b):return (a^b).bit_count()
assets=sorted(p for p in LOGO.rglob("*") if p.is_file() and not p.is_symlink() and p.suffix.lower() in IMAGE_EXT)
paths={p.relative_to(ROOT).as_posix():p for p in assets}
explicit=defaultdict(set);basename=defaultdict(set);dynamic=[]
runtime_roots=("scripts/","automation/",".github/")
for p in ROOT.rglob("*"):
 if not p.is_file() or p.is_symlink() or "logos" in p.relative_to(ROOT).parts:continue
 rel=p.relative_to(ROOT).as_posix()
 if rel.startswith("reports/") or p.suffix.lower() not in TEXT_EXT:continue
 try:t=p.read_text(encoding="utf-8")
 except Exception:continue
 for m in EXPLICIT.finditer(t):explicit[m.group(1)].add(rel)
 if rel in PLAYLISTS or rel.startswith(runtime_roots) or rel in ("reports/logo-source-registry.json","reports/logo-authenticity-manifest.json"):
  for name in paths:
   if Path(name).name in t:basename[name].add(rel)
  if DYNAMIC.search(t):dynamic.append({"source":rel,"matches":DYNAMIC.findall(t)[:20]})
playlist=defaultdict(set)
for pl in PLAYLISTS:
 p=ROOT/pl
 if p.exists():
  t=p.read_text(encoding="utf-8",errors="replace")
  for name in paths:
   if name in t:playlist[name].add(pl)
runtime=defaultdict(set)
for name,sources in explicit.items():
 for s in sources:
  if s in PLAYLISTS or s.startswith(runtime_roots) or s in ("reports/logo-source-registry.json","reports/logo-authenticity-manifest.json"):runtime[name].add(s)
for name,sources in basename.items():runtime[name].update(sources)
bysha=defaultdict(list);records={}
for rel,p in paths.items():
 digest=sha(p)
 try:h=phash(p);err=None
 except Exception as e:h=None;err=f"{type(e).__name__}: {e}"
 blob=subprocess.check_output(["git","hash-object",str(p)],text=True).strip()
 records[rel]={"sha256":digest,"git_blob":blob,"bytes":p.stat().st_size,"phash64":None if h is None else f"{h:016x}","decode_error":err,"playlist_references":sorted(playlist[rel]),"runtime_references":sorted(runtime[rel])}
 bysha[digest].append(rel)
exact=[{"sha256":d,"files":sorted(v)} for d,v in sorted(bysha.items()) if len(v)>1]
valid=[(p,int(r["phash64"],16)) for p,r in records.items() if r["phash64"]]
pairs=[]
for i,(pa,ha) in enumerate(valid):
 for pb,hb in valid[i+1:]:
  if records[pa]["sha256"]==records[pb]["sha256"]:continue
  dist=ham(ha,hb)
  if dist<=5:pairs.append({"file_a":pa,"file_b":pb,"hamming_distance":dist,"similarity":round(1-dist/64,4),"referenced_a":bool(records[pa]["playlist_references"] or records[pa]["runtime_references"]),"referenced_b":bool(records[pb]["playlist_references"] or records[pb]["runtime_references"])})
manifest=[]
for group in exact:
 for candidate in group["files"]:
  if not candidate.startswith("logos/unused/"):continue
  retained="logos/"+Path(candidate).name
  if retained not in group["files"]:continue
  r=records[candidate]
  if r["playlist_references"] or r["runtime_references"]:continue
  manifest.append({"delete_candidate":candidate,"retain":retained,"sha256":r["sha256"],"git_blob":r["git_blob"],"retained_sha256":records[retained]["sha256"],"retained_git_blob":records[retained]["git_blob"],"checks":{"exact_bytes_identical":True,"playlist_reference_absent":True,"runtime_reference_absent_in_scanned_sources":True,"same_basename_root_copy":True,"visual_identity":True},"deletion_authorized":False})
head=subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
summary={"assets":len(assets),"decode_failures":sum(bool(x["decode_error"]) for x in records.values()),"explicit_reference_targets":len(explicit),"assets_with_playlist_refs":sum(bool(x["playlist_references"]) for x in records.values()),"assets_with_runtime_refs":sum(bool(x["runtime_references"]) for x in records.values()),"assets_without_scanned_playlist_or_runtime_refs":sum(not x["playlist_references"] and not x["runtime_references"] for x in records.values()),"exact_duplicate_groups":len(exact),"exact_duplicate_extra_copies":sum(len(x["files"])-1 for x in exact),"nonidentical_perceptual_pairs_le_5":len(pairs),"dynamic_reference_sources_flagged":len(dynamic),"strict_exact_duplicate_manifest_candidates":len(manifest)}
report={"schema_version":1,"repository_head":head,"summary":summary,"dynamic_reference_sources":dynamic,"exact_duplicate_groups":exact,"perceptual_pairs":pairs,"deletion_manifest":manifest,"assets":records,"safety":{"playlists_modified":False,"assets_deleted":False,"deletion_performed":False,"limitations":["Dynamic runtime construction is flagged but cannot be proven safe by static scanning alone.","Perceptual hash matches are candidates, not proof of same channel identity.","Manifest candidates are not deletion authorization."]}}
out=ROOT/"reports";out.mkdir(exist_ok=True)
(out/"logo-deep-audit.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
md=["# Deep Logo Audit","","Commit: "+head,"","## Summary"]+[f"- {k}: {v}" for k,v in summary.items()]
md+=["","## Dynamic reference sources"]+[f"- {x['source']}: {', '.join(x['matches'])}" for x in dynamic]
md+=["","## Perceptual candidates"]+[f"- Hamming {x['hamming_distance']}: {x['file_a']} <> {x['file_b']}" for x in pairs]
md+=["","## Exact-copy manifest"]+[f"- DELETE REVIEW: {x['delete_candidate']}; RETAIN: {x['retain']}; SHA-256: {x['sha256']}; deletion authorized: false" for x in manifest]
md+=["","## Safety","- No playlist modified.","- No asset deleted."]
(out/"logo-deep-audit.md").write_text("\n".join(md)+"\n",encoding="utf-8")
print(json.dumps({"head":head,"summary":summary,"reports":["reports/logo-deep-audit.json","reports/logo-deep-audit.md"]},indent=2))
