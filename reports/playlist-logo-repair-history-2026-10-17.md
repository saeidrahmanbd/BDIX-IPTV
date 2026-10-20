# IPTV Playlist Logo Repair Results — Historical Snapshot

> Historical results from 2026-10-17 for a 1,094-entry playlist. This is not a current audit. Use `reports/playlist-logo-repair-results.md`, `reports/logo-authenticity-manifest.json` and `reports/logo-provenance-review.md` for current status.

Run time: **2026-10-17 09:25 UTC**  
Repository-first local logo search completed before external lookup.  
IPTV-org data: loaded  
Historical mapping index: loaded 336 historical name mappings

## Results by playlist

| Playlist | Entries | References changed | Generated fallbacks | Missing after | Known generic/contaminated refs after | Unresolved repair targets |
|---|---:|---:|---:|---:|---:|---:|
| IPTV-Playlist.m3u | 1094 | 44 | 3 | 0 | 0 | 0 |

## Repair log

See the original repair history preserved in Git history for the full per-channel change list.

## Quality rule

- Exact, clean local assets are searched first; then curated, source-attributed external logo URLs are downloaded and validated.
- When no exact clean original is found, a distinct channel-labelled fallback is installed; generated fallbacks are explicitly marked as unofficial in the authenticity manifest.
- Contaminated or mismatched source files are never reused as fallbacks; generated art does not imitate a broadcaster's official mark.
- Original playlist entries, channel metadata, categories, and stream URLs are preserved.
