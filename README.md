<!-- BDIX-IPTV banner -->
<p align="center">
  <img src="assets/bdix-iptv-banner.jpg" alt="BDIX-IPTV — Bangladesh, India and international IPTV playlists" width="100%">
</p>

<h1 align="center">📺 BDIX-IPTV</h1>

<p align="center">
  <b>Bangladesh & India IPTV Hub — Worldwide Channel Collections</b><br>
  Curated M3U playlists · Public EPG · Local logo assets · Automated quality checks
</p>

<p align="center">
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/stargazers"><img src="https://img.shields.io/github/stars/saeidrahmanbd/BDIX-IPTV?style=for-the-badge&logo=github&color=f5c542" alt="GitHub stars"></a>
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/network/members"><img src="https://img.shields.io/github/forks/saeidrahmanbd/BDIX-IPTV?style=for-the-badge&logo=git&logoColor=white&color=2ea44f" alt="GitHub forks"></a>
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/issues"><img src="https://img.shields.io/github/issues/saeidrahmanbd/BDIX-IPTV?style=for-the-badge&color=e5534b" alt="Open issues"></a>
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/commits/main"><img src="https://img.shields.io/github/last-commit/saeidrahmanbd/BDIX-IPTV?style=for-the-badge&color=0969da" alt="Last commit"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Format-M3U%20%2F%20M3U8-6f42c1?style=flat-square" alt="M3U and M3U8 format">
  <img src="https://img.shields.io/badge/Compatible%20with-M3U%20Players-00b4d8?style=flat-square" alt="M3U player compatibility">
  <img src="https://img.shields.io/badge/Public%20EPG-Enabled-2ea44f?style=flat-square" alt="Public EPG enabled">
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/actions/workflows/iptv-maintenance.yml"><img src="https://github.com/saeidrahmanbd/BDIX-IPTV/actions/workflows/iptv-maintenance.yml/badge.svg" alt="IPTV Playlist Update workflow"></a>
</p>

<p align="center">
  <a href="#-playlists">Playlists</a> ·
  <a href="#-quick-start">Quick Start</a> ·
  <a href="#-epg-programme-guide">EPG</a> ·
  <a href="#-repository-showcase">Showcase</a> ·
  <a href="#-download-center">Downloads</a> ·
  <a href="#-playlist-studio">Playlist Studio</a> ·
  <a href="#-reports-and-status">Reports</a> ·
  <a href="#-faq--troubleshooting">FAQ</a> ·
  <a href="#-support">Support</a>
</p>

---

## ✨ Overview

**BDIX-IPTV** maintains three M3U playlists covering Bangladesh, India, BDIX-focused viewing and international channels. The project focuses on clean organization: consistent channel metadata, repository-local logos, duplicate-URL checks, reviewed backup references and a public programme guide (EPG).

| 🏷️ Channel Metadata | 🖼️ Logo Assets | 🩺 Stream Review | 🗓️ Programme Guide |
|:---:|:---:|:---:|:---:|
| Names, IDs and groups | Repository-local assets | Health and backup checks | **Public EPG enabled** |

### Why use it?

- **Organized** — channels sorted into clear categories and country groups.
- **Consistent** — standardized names, IDs and logos across all playlists.
- **Maintained** — automated workflows audit playlists and check stream health.
- **Guide-ready** — XMLTV EPG for players that support programme data.
- **Player-friendly** — works with XCIPTV, TiviMate, VLC, IPTV Smarters, Kodi and other M3U players.

---

## 📺 Playlists

| Playlist | Description | Link |
|---|---|---|
| **IPTV-Playlist.m3u** | Main curated Bangladesh and India collection | [Open M3U](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u) |
| **BDIX-Playlist.m3u** | BDIX-focused channel collection | [Open M3U](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u) |
| **International-Playlist.m3u** | International movie and music country groups, with separate thematic categories | [Open M3U](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u) |

> 💡 **BDIX note:** BDIX channels are typically reachable only from within participating Bangladeshi ISP networks. If a BDIX stream does not load, check that you are connected to a supported ISP.

---

## 🚀 Quick Start

**1. Copy a playlist URL**

```text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u
```

**2. Add it to your player**

Open your player (XCIPTV, TiviMate, VLC, IPTV Smarters, Kodi, …), choose **Add playlist → M3U URL**, paste the link, save, and refresh the channel list.

**3. (Optional) Add the EPG**

Paste the EPG URL from the [EPG section](#-epg-programme-guide) into your player's EPG / XMLTV setting to see programme information.

<p align="center">
  <a href="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u">
    <img src="https://img.shields.io/badge/▶%20OPEN%20MAIN%20PLAYLIST-1f6feb?style=for-the-badge" alt="Open main M3U playlist">
  </a>
</p>

### Player setup at a glance

| Player | Platform | Where to add the playlist |
|---|---|---|
| **XCIPTV** | Android / Android TV | *Add playlist → M3U URL* |
| **TiviMate** | Android TV | *Add playlist → M3U Playlist* |
| **IPTV Smarters** | Android / iOS / Smart TV | *Add user → Load Your Playlist or File/URL* |
| **VLC** | Windows / macOS / Linux / mobile | *Media → Open Network Stream* |
| **Kodi** | Multi-platform | *PVR IPTV Simple Client → M3U playlist URL* |

---

## 🗓️ EPG (Programme Guide)

Public XMLTV/EPG publication is **enabled**. Add the EPG URL to any player that supports XMLTV to get programme information alongside your channels.

**EPG URL**
```text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml
```

- Guide data is mapped to the channel IDs used in the playlists, so matching is automatic in most players.
- The mapping pipeline includes the official RTV schedule parser, and restricted legacy EPG.PW feeds have been removed.
- Coverage varies by channel; see the [coverage report](reports/epg-coverage.md) for current status.
- Source details and licensing information are tracked in the [source-rights register](epg/source-rights-register.csv). Setup and maintenance notes are in the [EPG documentation](epg/README.md).

> If a channel shows no guide data, refresh the EPG in your player first. Some channels do not have a public schedule source.

---

## 🖼️ Repository Showcase

<p align="center">
  <a href="assets/iptv-project-showcase.svg">
    <img src="assets/iptv-project-showcase.svg" alt="BDIX-IPTV repository showcase with the three playlists and project quality checks" width="100%">
  </a>
</p>

### Repository Dashboard

<p align="center">
  <a href="assets/dashboard.svg">
    <img src="assets/dashboard.svg" alt="BDIX-IPTV project dashboard showing playlist inventory and EPG publication status" width="100%">
  </a>
</p>

> The dashboard and linked reports are generated snapshots, not live monitoring pages. Check each report's generation timestamp before relying on its findings.

---

## 📥 Download Center

| Resource | Description |
|---|---|
| [Main IPTV Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u) | Main curated collection |
| [BDIX Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u) | BDIX-focused collection |
| [International Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u) | International movie/music and thematic groups |
| [Public EPG (XMLTV)](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml) | Programme guide for supported channels |
| [Playlist Studio 5.0](https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5.0.exe) | Windows playlist manager, editor and player |
| [Playlist Studio Windows Build Kit](https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5_0-Windows-Build-Kit-Debug22.zip) | Windows build package |
| [Xtream Gateway documentation](xtream/README.md) | Optional Xtream-compatible access details |
| [Full Download Center](docs/DOWNLOADS.md) | All key downloads and documentation |
| [Documentation index](docs/README.md) | Project guides and references |

---

## 🖥️ Playlist Studio

[**Playlist Studio 5.0**](https://github.com/saeidrahmanbd/Playlist-Studio) is a separate Windows application for managing, editing, testing and playing IPTV playlists.

### Program Glimpse

<p align="center">
  <a href="assets/playlist-studio-5.png">
    <img src="assets/playlist-studio-5.png" alt="Playlist Studio 5.0 application screenshot" width="100%">
  </a>
</p>

### Key features

| Feature | Details |
|---|---|
| ✏️ **Editing** | M3U / M3U8 editing and category organization |
| 🏷️ **Metadata** | Channel metadata, logo, EPG and stream URL editing |
| 🔍 **Testing** | Stream scanning, duplicate detection and built-in playback |
| 🔌 **Sources** | Xtream Codes and MAC / Stalker Portal support |
| 🐙 **Workflow** | GitHub integration and Save / Save As |

<p align="center">
  <a href="https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5.0.exe"><img src="https://img.shields.io/badge/⬇%20Download%20Portable%20App-2ea44f?style=for-the-badge" alt="Download Playlist Studio"></a>
  <a href="https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5_0-Windows-Build-Kit-Debug22.zip"><img src="https://img.shields.io/badge/🛠%20Windows%20Build%20Kit-6e7681?style=for-the-badge" alt="Download Windows Build Kit"></a>
  <a href="docs/PLAYLIST-STUDIO.md"><img src="https://img.shields.io/badge/📖%20Usage%20Guide-0969da?style=for-the-badge" alt="Playlist Studio guide"></a>
</p>

---

## 📊 Reports and Status

Automated workflows generate playlist audits, maintenance summaries and stream-health reports. Results may differ by playlist and workflow. Endpoint failures can reflect provider authentication, entitlement or geographic restrictions, so a failed check is a **review signal**, not definitive proof that a stream is unavailable to everyone.

| Report | Purpose |
|---|---|
| [Project Dashboard](assets/dashboard.svg) | Playlist inventory and EPG publication status |
| [IPTV Playlist Audit](reports/iptv-playlist-audit.md) | Duplicate URLs, identity and metadata checks |
| [IPTV Channel Discovery](reports/iptv-channel-discovery.md) | Discovered Bangladesh and India channel candidates |
| [Stream Health](reports/stream-health.md) | Endpoint checks and failure classification |
| [Backup Independence Audit](reports/backup-independence-audit.md) | Review of backup stream and infrastructure independence |
| [Maintenance Report](reports/maintenance-report.md) | Automated maintenance summary |
| [Update Report](reports/Update%20Report.md) | Latest generated update snapshot |
| [Stream Risk Review](reports/stream-risk-review.md) | Stream references flagged for additional review |
| [EPG Coverage Report](reports/epg-coverage.md) | Programme-guide coverage and publication status |

### Maintenance principles

- Keep channel names, IDs, groups and logo references consistent.
- Avoid duplicate stream URLs and use local logo assets in published playlists.
- Protect primary entries and backup references from indiscriminate automatic deletion.
- Treat new channels and backups as candidates for review.
- Check report timestamps before treating generated metrics as current.

---

## 📦 Delivery and Rollback

Playlists, EPG and logo assets are served from the repository's `main` branch through GitHub raw-content URLs. These URLs reflect the current branch contents, so updates can become visible as soon as changes are committed.

For a reproducible snapshot, use a reviewed **commit-specific URL** where supported:

```text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/<commit-sha>/IPTV-Playlist.m3u
```

Git history provides a record of changes and rollback points.

---

## ❓ FAQ & Troubleshooting

<details>
<summary><b>A channel does not play. What should I do?</b></summary>

Refresh the playlist in your player, then try again later. Some streams are geo-restricted, ISP-restricted (especially BDIX) or temporarily offline. If it still fails, [open an issue](https://github.com/saeidrahmanbd/BDIX-IPTV/issues) with the channel name and playlist.
</details>

<details>
<summary><b>Why do BDIX channels only work on some connections?</b></summary>

BDIX streams are generally served inside Bangladeshi ISP networks and may not be reachable from other ISPs or from abroad.
</details>

<details>
<summary><b>The programme guide is empty or outdated.</b></summary>

Confirm the EPG URL is entered in your player's XMLTV/EPG setting, then force an EPG refresh. Not every channel has a public schedule source; see the [coverage report](reports/epg-coverage.md).
</details>

<details>
<summary><b>Logos are missing in my player.</b></summary>

Logos are loaded from this repository. Check that your device can reach `raw.githubusercontent.com`, and report any missing logo via an issue.
</details>

<details>
<summary><b>Can I get a stable, unchanging playlist?</b></summary>

Yes. Use a commit-specific raw URL (see [Delivery and Rollback](#-delivery-and-rollback)) instead of the `main` branch URL.
</details>

---

## 🤝 Support

Found a broken stream, incorrect channel information or a missing logo? [Open an issue](https://github.com/saeidrahmanbd/BDIX-IPTV/issues) and include:

- the channel name,
- the relevant playlist or stream URL,
- a short description of the problem.

You can also join [GitHub Discussions](https://github.com/saeidrahmanbd/BDIX-IPTV/discussions).

## 🧩 Contributing

Contributions are welcome — channel corrections, logo fixes, backup stream suggestions and EPG mapping improvements. Please keep channel names, IDs and groups consistent with existing entries, avoid duplicate URLs, and treat new channels as candidates for review.

## 📬 Contact

For project-related questions, collaboration or feedback:

<p align="center">
  <a href="mailto:saeidrahman.mkt@gmail.com"><img src="https://img.shields.io/badge/Email-saeidrahman.mkt@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://github.com/saeidrahmanbd"><img src="https://img.shields.io/badge/GitHub-saeidrahmanbd-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://www.facebook.com/saeid.rahman.sr"><img src="https://img.shields.io/badge/Facebook-Saeid%20Rahman-1877F2?style=for-the-badge&logo=facebook" alt="Facebook"></a>
</p>

---

## 📄 License

Repository code and documentation are licensed under the [MIT License](LICENSE), to the extent owned by the maintainer. Third-party logos, names, trademarks, programme data, stream endpoints and other third-party content remain subject to their respective owners' rights and terms.

## ⚠️ Disclaimer

This repository provides references to streams; it does not host television channels or video content. Availability and programme information may change without notice. Users are responsible for complying with applicable laws, regulations and service terms.

<p align="center">
  ⭐ <b>If you find the project useful, consider starring the repository.</b><br><br>
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV">github.com/saeidrahmanbd/BDIX-IPTV</a><br><br>
  <sub>Made with ❤️ by <a href="https://github.com/saeidrahmanbd">Saeid Rahman</a></sub>
</p>
