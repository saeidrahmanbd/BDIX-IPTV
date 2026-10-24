# 📺 BDIX-IPTV

> Bangladesh & India-focused IPTV hub with selected international channels, local logos, metadata, EPG and maintenance audits.

## Overview

A curated IPTV collection focused on **Bangladeshi channels, Indian channels, and selected international content** — organized for clean browsing, consistent channel identity, local logos, reviewed backup references, and transparent health/EPG reporting.

## Choose a Playlist

| Playlist | Best for | Open |
|---|---|---|
| **IPTV-Playlist.m3u** | Main curated channel collection | [Open M3U](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u) |
| **BDIX-Playlist.m3u** | BDIX-focused channel collection | [Open M3U](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u) |
| **International-Playlist.m3u** | International channel collection | [Open M3U](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u) |
| **BD.IN-Playlist.m3u** | Additional Bangladesh & India collection | [Open M3U](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BD.IN-Playlist.m3u) |

> **Automation scope:** The EPG and core quality workflows currently cover the IPTV, BDIX, and International playlists. `BD.IN-Playlist.m3u` is an additional fourth collection and is not yet included in that automated scope.

## Quick Start

Copy a playlist URL into **XCIPTV** or any M3U-compatible player:

```text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u
```

For BDIX or International collections, use the URLs above.

## Download Center

- [Main M3U Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u)
- [BDIX M3U Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u)
- [International M3U Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u)
- [BD.IN M3U Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BD.IN-Playlist.m3u)
- [Playlist Studio 5.0](https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5.0.exe)
- [Playlist Studio Build Kit](https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5_0-Windows-Build-Kit-Debug22.zip)
- [Xtream Gateway](../xtream/README.md)
- [EPG Coverage](../reports/epg-coverage.md)
- [Documentation](README.md)

## Playlist Studio

[Playlist Studio 5.0](https://github.com/saeidrahmanbd/Playlist-Studio) is a separate portable Windows playlist manager, editor and player supporting M3U/M3U8, Xtream Codes and Stalker Portal connections.

- M3U / M3U8 playlist editing
- Xtream Codes and Stalker Portal connections
- Playback and stream scanning
- Metadata editing and GitHub workflows
- [Usage & Build Guide](PLAYLIST-STUDIO.md)
- [Release Integrity](PLAYLIST-STUDIO-INTEGRITY.md)

## Project Status

| Area | Status |
|---|---|
| Playlists | Curated & updated |
| Logos | Repository-local |
| Stream Health | Automated monitoring |
| EPG | Coverage monitored |
| Playlist Audit | Automated |
| Maintenance Reports | Automated |

## Playlist Organization

The playlists are organized into country, language, content, and backup/review groups.

`New Channels` and `New Backup` are active discovery/review queues. They are subject to country and metadata validation policies and are not part of the canonical Playlist Studio category registry.

The project prioritizes clean channel identity, consistent metadata, local logos, duplicate-free stream URLs, and practical reviewed alternatives over simply collecting more entries.

## Maintenance

Automated maintenance covers stream and backup updates, metadata normalization, duplicate detection, local-logo integrity, stream health, EPG coverage, backup-independence review and maintenance reporting.

### Protection Rules

1. Duplicate stream URLs are not allowed.
2. Existing primary streams are protected from silent removal.
3. Backup streams are not automatically deleted because of health failures.
4. `New Channels` and `New Backup` are active review queues.
5. Health failures become review candidates rather than automatic deletion decisions.
6. Dashboard figures are generated from the current playlist and reports.
7. Maintenance runs record quality metrics.
8. Backup counts do not imply independent infrastructure.
9. **News, Sports, Kids and Religious channels from both Bangladesh and India are strictly prohibited from discovery queues. E-Vidya 4, 5, 6, 7, 8, 9, 10, 11, 12 and Friends TV are permanently denylisted.**

## Reports

- [Project Dashboard](../assets/dashboard.svg)
- [IPTV Playlist Audit](../reports/iptv-playlist-audit.md)
- [Stream Health](../reports/stream-health.md)
- [Backup Independence Audit](../reports/backup-independence-audit.md)
- [Maintenance Report](../reports/maintenance-report.md)
- [EPG Coverage](../reports/epg-coverage.md)
- [IPTV Channel Discovery](../reports/iptv-channel-discovery.md)
- [Update Report](../reports/Update%20Report.md)
- [Stream Risk Review](../reports/stream-risk-review.md)

## Repository Policies

- [Contributing](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)
- [License](LICENSE)
- [Python requirements](requirements.txt)

## Support

Found a broken stream, incorrect information, missing logo, or another issue? Use the repository [Issues](https://github.com/saeidrahmanbd/BDIX-IPTV/issues) or [Discussions](https://github.com/saeidrahmanbd/BDIX-IPTV/discussions).

## Disclaimer

This repository does not host television channels or video content. It contains references to publicly available streams. Availability and programme information may change without notice. Users are responsible for complying with applicable laws, regulations, and service terms.

---

⭐ If you find the project useful, consider starring the repository.
