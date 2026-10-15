# Three-Playlist Logo Repair Results

Run time: **2026-10-15 08:29 UTC**  
Repository-first local logo search completed before external lookup.  
IPTV-org data: loaded  
Historical mapping index: loaded 336 historical name mappings

## Results by playlist

| Playlist | Entries | References changed | Generated fallbacks | Missing after | Known generic/contaminated refs after | Unresolved repair targets |
|---|---:|---:|---:|---:|---:|---:|
| BDIX-Playlist.m3u | 139 | 0 | 0 | 0 | 0 | 0 |
| IPTV-Playlist.m3u | 1037 | 2 | 2 | 0 | 0 | 0 |

## Repair log

| Playlist | Line | Channel | Previous logo | Replacement | Source | Attribution | Result |
|---|---:|---|---|---|---|---|---|
| IPTV-Playlist.m3u | 783 | Cook & Bake | generated-fallback-cook-and-bake-00755d7b.svg | generated-fallback-cook-and-bake-00755d7b.svg | Generated channel-specific fallback | Original generated artwork; not an official broadcaster logo | fallback installed; exact clean original not found |
| IPTV-Playlist.m3u | 959 | Vevo '70s & '80s | generated-fallback-vevo-70s-and-80s-34700aa0.svg | generated-fallback-vevo-70s-and-80s-34700aa0.svg | Generated channel-specific fallback | Original generated artwork; not an official broadcaster logo | fallback installed; exact clean original not found |

## Quality rule

- Exact, clean local assets are searched first; then curated, source-attributed external logo URLs are downloaded and validated.
- When no exact clean original is found, a distinct channel-labelled fallback is installed; generated fallbacks are explicitly marked as unofficial in the authenticity manifest.
- Contaminated or mismatched source files are never reused as fallbacks; the generated art does not imitate a broadcaster's official mark.
- Original playlist entries, channel metadata, categories, and stream URLs are preserved.
