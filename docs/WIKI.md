# BDIX-IPTV Wiki

**Maintainer:** Saeid Rahman  
**Repository:** [saeidrahmanbd/BDIX-IPTV](https://github.com/saeidrahmanbd/BDIX-IPTV)

BDIX-IPTV is a curated IPTV playlist project focused on Bangladeshi channels, Indian channels, and selected international content. It maintains M3U playlists, channel logos, EPG resources, Xtream-related documentation, quality reports, and supporting automation.

## Quick Links

- [Main IPTV playlist (M3U)](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u)
- [BDIX playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u)
- [International playlist (M3U)](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u)
- [BD.IN playlist — Bangladesh & India](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BD.IN-Playlist.m3u)
- [Download Center](docs/DOWNLOADS.md)
- [Documentation index](docs/README.md)
- [Xtream documentation](xtream/README.md)
- [EPG coverage report](reports/epg-coverage.md)
- [Playlist audit report](reports/playlist-audit.md)
- [Stream health report](reports/stream-health.md)
- [Maintenance report](reports/maintenance-report.md)
- [Update report](reports/Update%20Report.md)
- [GitHub Issues](https://github.com/saeidrahmanbd/BDIX-IPTV/issues)
- [Playlist Studio releases](https://github.com/saeidrahmanbd/Playlist-Studio/releases)

## Playlists

| Playlist | Use |
|---|---|
| IPTV-Playlist.m3u | Main curated playlist |
| BDIX-Playlist.m3u | BDIX-focused playlist |
| International-Playlist.m3u | Selected international channels, with country and content groupings |
| BD.IN-Playlist.m3u | Additional Bangladesh & India collection, separate from the three core maintained playlists |

Use the raw playlist links above to add a playlist to a compatible M3U/M3U8 player. Stream availability, provider requirements, and channel listings can change.

> **Automation scope:** The shared EPG and core quality workflows currently audit the IPTV, BDIX, and International playlists. The additional `BD.IN-Playlist.m3u` file is listed for access but is not yet included in those automated checks.

## Playlist Studio

[Playlist Studio 5.0](https://github.com/saeidrahmanbd/Playlist-Studio) is a separate, general-purpose Windows playlist manager, editor, and player. It supports M3U/M3U8 playlist workflows, channel/category organization, metadata editing, stream scanning, built-in playback, compatible Xtream Codes and Stalker Portal/MAC connections, and GitHub integration.

- [Download portable Windows application](https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5.0.exe)
- [Download Windows Build Kit — Debug22](https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5_0-Windows-Build-Kit-Debug22.zip)
- [Playlist Studio guide](docs/PLAYLIST-STUDIO.md)

The portable application is intended for regular use. The Build Kit is for users who want to build the program themselves; consult its included Readme.txt for requirements and steps.

## EPG and Channel Metadata

The project tracks EPG mapping and coverage in its report files. A mapped channel should use an appropriate, verified channel identifier; mapping coverage is not the same as confirming that every programme entry is available or accurate.

When maintaining playlists, check channel names, IDs, numbers, categories, logo references, and EPG identifiers together. Keep programme-guide presentation in English where the relevant source data or processing workflow allows it; do not claim a translation is complete unless it has been verified.

## Logo Policy

- Check the repository's `logos/` directory before sourcing a replacement externally.
- Prefer an authentic broadcaster-provided logo that matches the channel and its current or known branding.
- Store approved local logo assets in the repository and use repository-hosted URLs in playlist entries.
- Do not treat a generic placeholder as an authentic broadcaster logo. If an exact authentic asset cannot be verified, clearly identify fallback artwork as generated or illustrative.
- Review both the image and its source/identity before replacing a logo reference.

## Maintenance and Automation

Automation supports routine stream checks, playlist metadata audits, EPG coverage analysis, logo integrity checks, and maintenance reporting. Reports should reflect the current files and run, not stale results.

Protection principles:
1. Do not silently delete primary curated entries.
2. Treat health failures as review candidates; do not remove backup streams solely because a check failed.
3. Detect duplicate stream URLs and identity conflicts before making edits.
4. Keep channel metadata consistent and changes traceable.
5. Avoid adding channels that violate the project's explicit category and eligibility rules.
6. Preserve playlist attribution headers exactly in every playlist and in every workflow that writes or regenerates a playlist.

## Required Playlist Attribution

The following attribution block must appear at the top of every playlist and must not be changed or removed by automation:

```text
#=================================
# Developed by: SAEID RAHMAN
# Facebook: https://www.facebook.com/saeid.rahman.sr
# Email: saeidrahman.mkt@gmail.com
#=================================
```

Any workflow that creates, rewrites, merges, sorts, repairs, or regenerates playlist content must preserve this block exactly.

## Reports

Use the linked reports for the latest available status of playlist quality, stream health, EPG coverage, and maintenance runs. A report should be considered current only after its generating workflow has completed successfully against the latest relevant playlist revision.

## Troubleshooting

- **Playlist will not load:** confirm that the player supports M3U/M3U8 and that you used the raw playlist URL.
- **A channel does not play:** the stream may be down, geo-restricted, provider-authenticated, or no longer valid. Check the latest stream-health report.
- **Logo is missing or incorrect:** inspect the playlist's `tvg-logo` reference, then check `logos/` and the logo audit report.
- **Programme guide is missing:** check the channel's `tvg-id` and the EPG coverage report. A correct ID cannot guarantee the source currently supplies schedule data.
- **Build Kit issue:** consult `Readme.txt` included in the downloaded package and use the current release asset.

## Responsible Use

This repository provides playlist references and related metadata; it does not itself host television programming. Use only streams and services you are authorized to access, and comply with applicable laws and service terms. Availability and programme information may change without notice.

## Contact and Contributions

Report a broken stream, incorrect metadata, missing logo, or other project issue through [GitHub Issues](https://github.com/saeidrahmanbd/BDIX-IPTV/issues). Include the playlist name, channel name, relevant URL or identifier, and a concise description when possible.

- [GitHub profile](https://github.com/saeidrahmanbd)
- [Facebook](https://www.facebook.com/saeid.rahman.sr)
- Email: saeidrahman.mkt@gmail.com

---

**Maintainer:** SAEID RAHMAN
