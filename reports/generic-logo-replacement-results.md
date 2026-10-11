# Generic Logo Replacement and Authenticity Results

Audit date: 2026-10-11

This report separates playlist/path integrity from actual image authentication. A valid local file path is not proof that the image is official.

## Current playlist snapshot

| Playlist | Entries | With logo | Without logo | External refs | Known generic filename refs |
|---|---:|---:|---:|---:|---:|
| IPTV-Playlist.m3u | 1,145 | 1,123 | 22 | 0 | 0 |
| BDIX-Playlist.m3u | 190 | 184 | 6 | 5 | 0 |
| NVisionBD-Playlist.m3u | 561 | 328 | 233 | 0 | 0 |

## Image-level findings and changes

- **Rejected `logos/btv-news.png`:** the image visibly contains BTV News branding plus an unrelated “M3U World 4K” overlay. Removed its playlist references from IPTV-Playlist.m3u and BDIX-Playlist.m3u.
- **Rejected `logos/bangla-tv.png`:** the image visibly carries a “BONGO FLIX” watermark. Removed its playlist references from IPTV-Playlist.m3u, BDIX-Playlist.m3u, and NVisionBD-Playlist.m3u.
- Total references removed for these two contaminated images: **11**.
- Channel entries and stream URLs were preserved. The image files remain in the repository for traceability; no replacement was guessed.
- Previous generic-looking `channel-N.png` references remain unlinked from playlists.

## Next verification sources

- BTV official site: https://btv.gov.bd/
- Bangladesh TV logo source category on Wikimedia Commons: https://commons.wikimedia.org/wiki/Category:Logos_of_television_channels_in_Bangladesh
- JioStar official media toolkit: https://www.jiostar.com/mediatoolkit/all-logos/

These links help find candidate official assets. A logo is not approved until the actual repository image is compared with the exact source image and the source attribution is recorded.

## Important limitation

The remaining 1,635 logo references have not all been individually authenticated. Continue with image-by-image checks; do not label an asset official solely because its filename or displayed channel name matches.
