# Three-Playlist Logo Repair Results

Run time: **2026-10-14 08:47 UTC**  
Repository-first local logo search completed before external lookup.  
IPTV-org data: loaded  
Historical mapping index: loaded 336 historical name mappings

## Results by playlist

| Playlist | Entries | References changed | Generated fallbacks | Missing after | Known generic/contaminated refs after | Unresolved repair targets |
|---|---:|---:|---:|---:|---:|---:|
| BDIX-Playlist.m3u | 139 | 0 | 0 | 0 | 0 | 0 |
| IPTV-Playlist.m3u | 940 | 2 | 2 | 0 | 0 | 0 |

## Repair log

| Playlist | Line | Channel | Previous logo | Replacement | Source | Attribution | Result |
|---|---:|---|---|---|---|---|---|
| IPTV-Playlist.m3u | 129 | Bangla Cinema | generated-fallback-bangla-cinema-ce3797ef.svg | generated-fallback-bangla-cinema-ce3797ef.svg | Generated channel-specific fallback | Original generated artwork; not an official broadcaster logo | fallback installed; exact clean original not found |
| IPTV-Playlist.m3u | 1089 | Teen Nick | generated-fallback-teen-nick-cf2a4a80.svg | (none) | Exact original tvg-logo URL from playlist history |  | Download/validation failed: downloaded image failed local validation |
| IPTV-Playlist.m3u | 1089 | Teen Nick | generated-fallback-teen-nick-cf2a4a80.svg | generated-fallback-teen-nick-cf2a4a80.svg | Generated channel-specific fallback | Original generated artwork; not an official broadcaster logo | fallback installed; exact clean original not found |

## Quality rule

- Exact, clean local assets are searched first; then curated, source-attributed external logo URLs are downloaded and validated.
- When no exact clean original is found, a distinct channel-labelled fallback is installed; generated fallbacks are explicitly marked as unofficial in the authenticity manifest.
- Contaminated or mismatched source files are never reused as fallbacks; the generated art does not imitate a broadcaster's official mark.
- Original playlist entries, channel metadata, categories, and stream URLs are preserved.
