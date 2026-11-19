# IPTV Playlist Logo Repair Results

Run time: **2026-11-19 10:16 UTC**  
Repository-first local logo search completed before external lookup.  
IPTV-org data: loaded  
Historical mapping index: loaded 336 historical name mappings

## Results by playlist

| Playlist | Entries | References changed | Generated fallbacks | Missing after (Adult excluded) | Adult entries skipped | Known generic/contaminated refs after | Unresolved repair targets |
|---|---:|---:|---:|---:|---:|---:|---:|
| IPTV-Playlist.m3u | 1346 | 0 | 0 | 0 | 0 | 0 | 0 |
| International-Playlist.m3u | 3290 | 0 | 0 | 20 | 372 | 0 | 20 |

## Repair log

| Playlist | Line | Channel | Previous logo | Replacement | Source | Attribution | Result |
|---|---:|---|---|---|---|---|---|
| International-Playlist.m3u | 127 | JTV Bangla | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 863 | cine.box | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 1017 | Cedros TV | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 1141 | Persiana Vibe | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 1857 | Tarab | (missing) | (none) | Exact external logo asset |  | Download/validation failed: HTTP Error 403: Forbidden |
| International-Playlist.m3u | 1857 | Tarab | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 2653 | Asia Flix TV | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 2661 | Bigscreen TV | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 2811 | Sine Plus | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 3681 | Abdulmajeed Abdullah | (missing) | (none) | IPTV-org exact ID: AbdulmajeedAbdullah.sa |  | Download/validation failed: HTTP Error 403: Forbidden |
| International-Playlist.m3u | 3681 | Abdulmajeed Abdullah | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 4051 | Chikitoonz | (missing) | (none) | IPTV-org exact ID: Chikitoonz.pe |  | Download/validation failed: HTTP Error 404: Not Found |
| International-Playlist.m3u | 4051 | Chikitoonz | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 4347 | EKids | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 4547 | Gopal Bhar TV | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 4903 | Mohammed Abdo | (missing) | (none) | IPTV-org exact ID: MohammedAbdo.sa |  | Download/validation failed: HTTP Error 403: Forbidden |
| International-Playlist.m3u | 4903 | Mohammed Abdo | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 5011 | NewFlix | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 5127 | Persiana Latino | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 5353 | Sky Cinema Action | (missing) | (none) | IPTV-org exact ID: SkyCinemaAction.it |  | Download/validation failed: HTTP Error 404: Not Found |
| International-Playlist.m3u | 5353 | Sky Cinema Action | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 5355 | Sky Cinema Collection | (missing) | (none) | IPTV-org exact ID: SkyCinemaCollection.it |  | Download/validation failed: HTTP Error 404: Not Found |
| International-Playlist.m3u | 5355 | Sky Cinema Collection | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 5357 | Sky Cinema Family | (missing) | (none) | IPTV-org exact ID: SkyCinemaFamily.it |  | Download/validation failed: HTTP Error 404: Not Found |
| International-Playlist.m3u | 5357 | Sky Cinema Family | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 5359 | Sky Cinema Suspense | (missing) | (none) | IPTV-org exact ID: SkyCinemaSuspense.it |  | Download/validation failed: HTTP Error 404: Not Found |
| International-Playlist.m3u | 5359 | Sky Cinema Suspense | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |
| International-Playlist.m3u | 5361 | Sky Cinema Uno | (missing) | (none) | IPTV-org exact ID: SkyCinemaUno.it |  | Download/validation failed: HTTP Error 404: Not Found |
| International-Playlist.m3u | 5361 | Sky Cinema Uno | (missing) | (none) | none |  | No exact authentic logo source; logo left missing for manual review |

## Quality rule

- Exact, clean local assets are searched first; then curated, source-attributed external logo URLs are downloaded and validated.
- If no exact authentic asset is available, leave the logo unresolved for manual verification; never generate substitute artwork.
- Contaminated, mismatched, placeholder, generic, and generated-fallback assets are never assigned to tvg-logo.
- Nvision-branded filenames are prohibited in all maintained playlists.
- Original playlist entries, channel metadata, categories, and stream URLs are preserved.
