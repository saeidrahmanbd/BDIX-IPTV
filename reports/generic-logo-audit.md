# Generic Channel Logo Audit — Three Playlists

Audit date: 2026-10-11 (verified against `main` after the latest playlist commit)  
Repository: https://github.com/saeidrahmanbd/BDIX-IPTV

## Live playlist integrity

| Playlist | Entries | Entries with logo | Entries without logo | Generic-looking logo references | Non-repository logo URLs | Missing local asset paths |
|---|---:|---:|---:|---:|---:|---:|
| IPTV-Playlist.m3u | 1,145 | 1,145 | 0 | 5 filename patterns / repeated references | 0 | 0 |
| BDIX-Playlist.m3u | 190 | 190 | 0 | 3 filename patterns / 3 entry references | 5 | 0 |
| NVisionBD-Playlist.m3u | 561 | 330 | 231 | 0 of the known `channel-1/9/16/24/52.png` and `nvisionbd-*` patterns | 0 | 0 |

## Confirmed findings

- `IPTV-Playlist.m3u` still references generic-looking `channel-1.png`, `channel-9.png`, `channel-16.png`, `channel-24.png`, and `channel-52.png`. These need image-by-image review; filename-based suspicion is not proof of a fabricated image.
- `BDIX-Playlist.m3u` uses `channel-1.png`, `channel-9.png`, and `channel-24.png` for channel labels The generic-looking logo was removed from `EPL channel 1`; its channel entry and stream URL were preserved. Five entries still load images from Toffee's CDN rather than from the repository's `/logos` folder.
- `NVisionBD-Playlist.m3u` retains all 561 channel entries and stream lines. The three generic-looking logo references (`Channel 1 HD`, `Channel 9 HD`, `Channel 24 HD`) were removed from metadata; no channel or stream entry was deleted.
- Seventeen logo references were restored from pre-existing local files where the channel identity corresponded to the asset filename/name. The NVisionBD playlist now has 330 logo references and 231 entries left logo-less pending exact source verification.
- No logo URL in the three playlists points to a missing path in the current repository tree. This checks path integrity only, not whether the actual picture is official or correctly branded.
- The `logos/` folder has 2,275 image/SVG files, while the three playlists reference 713 distinct local asset paths. Many files appear unused or historical; do not bulk-delete them without checking history and references.

## Verification limits

This is a metadata and asset-path audit plus targeted identity checks. It is **not** a full visual authentication of every logo file. An image is certified only after comparing its actual pixels with a source attributable to the broadcaster/brand. Do not replace an absent logo with invented artwork or a similarly named company's logo.

## Next high-priority actions

1. Inspect and replace the five `channel-N.png` patterns in `IPTV-Playlist.m3u` only after the corresponding image is verified against the correct channel.
2. Correct the `EPL channel 1` logo in `BDIX-Playlist.m3u`, and localize the five Toffee CDN images into `/logos` only if the fetched images are valid and correspond to their channels.
3. Continue source-by-source authentication of referenced local assets, prioritizing likely mismatches and images with no recorded provenance.
4. Update the audit generator so it detects generic PNGs/JPEGs and channel-name mismatches as well as the old SVG `CHANNEL MARK` template. Do not report zero generic logos solely because there are no matching SVG files.
