<!-- BDIX-IPTV Banner -->
<p align="center">
  <img src="assets/Saeid%20Rahman.jpg" alt="BDIX-IPTV — Bangladesh, India & selected international IPTV collection" width="100%">
</p>

<h1 align="center">📺 BDIX-IPTV</h1>

<p align="center">
  <b>Bangladesh & India IPTV Hub — Selected International Channels</b><br>
  Bangladesh & India-focused live TV · Selected international channels · Metadata, logo and EPG audits
</p>

<p align="center">
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/stargazers"><img src="https://img.shields.io/github/stars/saeidrahmanbd/BDIX-IPTV?style=for-the-badge&logo=github&color=f5c542" alt="Stars"></a>
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/network/members"><img src="https://img.shields.io/github/forks/saeidrahmanbd/BDIX-IPTV?style=for-the-badge&logo=git&logoColor=white&color=2ea44f" alt="Forks"></a>
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/issues"><img src="https://img.shields.io/github/issues/saeidrahmanbd/BDIX-IPTV?style=for-the-badge&color=e5534b" alt="Issues"></a>
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/commits/main"><img src="https://img.shields.io/github/last-commit/saeidrahmanbd/BDIX-IPTV?style=for-the-badge&color=0969da" alt="Last commit"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Format-M3U%20%2F%20M3U8-6f42c1?style=flat-square" alt="Format">
  <img src="https://img.shields.io/badge/Works%20with-XCIPTV-00b4d8?style=flat-square" alt="XCIPTV">
  <img src="https://img.shields.io/badge/EPG-Coverage%20Monitored-orange?style=flat-square" alt="EPG coverage monitored">
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/actions/workflows/iptv-maintenance.yml"><img src="https://github.com/saeidrahmanbd/BDIX-IPTV/actions/workflows/iptv-maintenance.yml/badge.svg" alt="IPTV Playlist Update workflow status"></a>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> ·
  <a href="#-download-center">Downloads</a> ·
  <a href="#%EF%B8%8F-playlist-studio">Playlist Studio</a> ·
  <a href="#-project-status">Status</a> ·
  <a href="#-reports">Reports</a> ·
  <a href="#-support">Support</a>
</p>

---

## ✨ Overview

A curated IPTV collection focused on **🇧🇩 Bangladeshi channels, 🇮🇳 Indian channels, and selected international content** — organized for clean browsing, consistent channel identity, local logos, reviewed backup references, and transparent health/EPG reporting.

> **Important:** backup entries are references to alternate stream URLs. Multiple URLs can share the same CDN, origin, rendition family, or delivery infrastructure, so a backup count is **not** a guarantee of independent redundancy.

| 🧼 Metadata | 🖼️ Local Logo Assets | 🔁 Backup References | 📡 EPG Monitoring |
|:---:|:---:|:---:|:---:|
| Consistent names, groups & IDs | Repository-local when assigned; missing coverage is reported separately | Reviewed alternates; independence audited separately | Coverage measured, not guaranteed |

## 📺 Choose a Playlist

| Playlist | Best for | Open |
|---|---|---|
| **IPTV-Playlist.m3u** | Main curated channel collection | [Open M3U](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u) |
| **BDIX-Playlist.m3u** | BDIX-focused channel collection | [Open M3U](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u) |
| **International-Playlist.m3u** | International channel collection | [Open M3U](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u) |

> **Automation scope:** EPG and quality-audit workflows inspect `IPTV-Playlist.m3u`, `BDIX-Playlist.m3u`, and `International-Playlist.m3u`; stream-health coverage varies by workflow and runner. Automatic Bangladesh/India discovery permits Bangladeshi news and Indian Kids/Sports, while rejecting Indian News and non-Islamic religious content. Islamic religious channels are allowed. International discovery is restricted to movie/music candidates, with the explicitly preserved Fashion TV exception. Existing canonical rows are protected from automatic removals.

> **Content and EPG scope:** `International-Playlist.m3u` contains a separate `Adult` category. The EPG mapping registry includes rows across all maintained playlist groups (including `Adult`); despite its legacy filename, it is not India-only. The combined EPG coverage report measures all three playlists, while EPG figures in the Update Report are IPTV-playlist-only when a current per-playlist row is available.

<p align="center">
  <a href="assets/iptv-project-showcase-2026-10-22.svg">
    <img src="assets/iptv-project-showcase-2026-10-22.svg" alt="BDIX-IPTV project showcase: three maintained playlist files, organized categories, metadata, EPG and logo audits" width="100%">
  </a>
</p>

> ⭐ **Find this project useful?** Star the repository to save it for later and help other IPTV users discover it. Follow [@saeidrahmanbd](https://github.com/saeidrahmanbd) for project updates.

---

## 🚀 Quick Start

Copy the playlist URL below and paste it into **XCIPTV** or any M3U-compatible player.

```text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u
```

For the BDIX or International collection, use its URL from the **Choose a Playlist** table above.

<p align="center">
  <a href="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u">
    <img src="https://img.shields.io/badge/▶%20%20OPEN%20MAIN%20M3U%20PLAYLIST-1f6feb?style=for-the-badge" alt="Open Main M3U Playlist">
  </a>
</p>

<details>
<summary><b>📱 How to use it in XCIPTV</b></summary>

1. Open **XCIPTV** and choose **Add playlist / Login with M3U URL**.
2. Paste the playlist URL above.
3. Save, wait for the channels to load, and enjoy.

Other players (VLC, TiviMate, IPTV Smarters, Kodi, etc.) work the same way — add the URL as an M3U playlist.

</details>

---

## 📥 Download Center

| | Resource | Description |
|:---:|---|---|
| 📺 | **[Main M3U Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u)** | The primary curated playlist |
| 📡 | **[BDIX M3U Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u)** | BDIX-focused playlist |
| 🌍 | **[International M3U Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u)** | International playlist |
| 🖥️ | **[Playlist Studio v5.0](https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5.0.exe)** | Windows playlist manager, editor & player |
| 🛠️ | **[Playlist Studio Build Kit](https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5_0-Windows-Build-Kit-Debug22.zip)** | Windows build package |
| 🔌 | **[Xtream Gateway](xtream/README.md)** | Xtream Gateway / XCIPTV documentation |
| 📄 | **[EPG Coverage](reports/epg-coverage.md)** | EPG status and coverage |
| 📚 | **[Documentation](docs/README.md)** | Guides and project information |

<p align="center">
  <b><a href="docs/DOWNLOADS.md">→ Open the full Download Center</a></b>
</p>

---

## 🖥️ Playlist Studio

![Playlist Studio 5.0](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/assets/Playlist%20Studio%205.0.png)

[**Playlist Studio 5.0**](https://github.com/saeidrahmanbd/Playlist-Studio) is a separate, portable Windows playlist manager, editor and player.

- 📂 **M3U / M3U8** playlists, compatible **Xtream Codes** and **Stalker Portal** connections
- ▶️ Built-in playback and **stream scanning**
- ✏️ **Metadata editing** and GitHub workflows

<p align="center">
  <a href="https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5.0.exe"><img src="https://img.shields.io/badge/⬇%20Download%20Portable%20App-2ea44f?style=for-the-badge" alt="Download Playlist Studio"></a>
  <a href="https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5_0-Windows-Build-Kit-Debug22.zip"><img src="https://img.shields.io/badge/🛠%20Windows%20Build%20Kit-6e7681?style=for-the-badge" alt="Download Build Kit"></a>
  <a href="docs/PLAYLIST-STUDIO.md"><img src="https://img.shields.io/badge/📖%20Usage%20%26%20Build%20Guide-0969da?style=for-the-badge" alt="Usage guide"></a>
</p>

> **Build note:** the current v5.0.0 Build Kit filename contains `Debug22` because that is the published asset name; it does not mean the portable EXE is a debug build. Published SHA-256 digests are documented in [Playlist Studio v5.0.0 Release Integrity](docs/PLAYLIST-STUDIO-INTEGRITY.md) and in the official release metadata.

---

## 📊 Project Status

The repository is maintained with automated quality checks.

| Area | Status | Details |
|---|:---:|---|
| 📺 Playlists | ✅ Available | Three maintained playlist files; check each report for its actual playlist scope and generated timestamp |
| 🖼️ Logos | 🧾 Reviewed | Local assets are used where assigned; authenticity and missing-logo coverage still require review |
| 📡 Stream Health | 🤖 Automated | Endpoint checks; failures become review candidates |
| 📄 EPG | 📈 Monitored | Coverage is measured and published only when the gate allows it |
| 🧹 Playlist Audit | 🤖 Automated | Duplicates, identity, metadata and logo checks |
| 📝 Maintenance Reports | 🤖 Automated | Quality metrics on maintenance runs |

<p align="center">
  <b><a href="reports/Update%20Report.md">→ Update Report snapshot (check timestamp and source fingerprint)</a></b>
</p>

---

## 🗂️ Playlist Organization

The playlists are organized into **country, language, content, and backup/review groups**, with category order and channel identity maintained for compatible players.

`New Channels` and `New Backup` are **active discovery/review queues**, not retired categories. They are restricted by validation policy and are not part of the canonical Playlist Studio category registry.

The project prioritizes **clean channel identity, consistent metadata, local logos, duplicate-free stream URLs, and practical reviewed alternatives** over simply collecting more entries.

---

## 🔧 Maintenance

Automated maintenance covers:

| 🔄 Streams | 🧾 Metadata | 🖼️ Logos | 📡 Monitoring |
|---|---|---|---|
| Stream & backup updates | Channel identity audits | Integrity & consistency | Stream health checks |
| Duplicate URL detection | Metadata audits | Local repository logos | EPG coverage analysis |
| Backup-independence review | Metadata normalization | Logo provenance review | Maintenance & quality reports |

> 🔒 Primary curated entries are protected from indiscriminate automatic changes.

> ⚠️ **Health-check limitation:** stream checks are endpoint connectivity tests. The scheduled maintenance workflow runs on GitHub-hosted `ubuntu-latest` runners, so HTTP 403/timeouts can be caused by authentication, entitlement, or geographic restrictions. A health failure is therefore a review signal, not proof that a stream is universally dead.

---

## 🛡️ Protection Rules

1. 🚫 Duplicate stream URLs are not allowed.
2. 🔐 Existing primary streams are protected from silent removal.
3. 💾 Backup streams are not automatically deleted because of health failures.
4. 🧭 `New Channels` and `New Backup` are active review queues used by discovery and validation; they are not retired categories.
5. 🔍 Health failures become review candidates rather than automatic deletion decisions.
6. 📊 Dashboard figures are generated snapshots; verify report timestamps and source playlist fingerprints before treating the values as current.
7. 📝 Maintenance runs record quality metrics.
8. 🔗 Backup counts do not imply independent infrastructure; CDN/origin/rendition families are audited separately.

<p align="center">
  <b><a href="reports/stream-health.md">→ Stream Health Report</a> · <a href="reports/iptv-playlist-audit.md">→ IPTV Playlist Audit</a> · <a href="reports/backup-independence-audit.md">→ Backup Independence Audit</a></b>
</p>

---

## 📈 Reports

> **Freshness note:** reports and the SVG dashboard are generated snapshots, not live status pages. Check each report's `Generated` timestamp and any source SHA-256 it provides; where a fingerprint is absent, compare the reported playlist counts with the current files. Several snapshots generated on 2026-10-23 predate subsequent playlist changes and are marked historical until regenerated successfully.

| Report | |
|---|---|
| 📊 [Project Dashboard snapshot](assets/dashboard.svg) | Historical visual snapshot; values can lag behind current playlists |
| 🧹 [IPTV Playlist Audit](reports/iptv-playlist-audit.md) | Duplicates, identity and metadata checks |
| 🆕 [IPTV Channel Discovery](reports/iptv-channel-discovery.md) | Bangladesh/India discovery queue; Indian Kids/Sports allowed, Indian News and non-Islamic religious content prohibited |
| 📡 [Stream Health](reports/stream-health.md) | Endpoint availability monitoring and failure classification |
| 🧩 [Backup Independence Audit](reports/backup-independence-audit.md) | Shared-host/origin and fallback-family review |
| 🛠️ [Maintenance Report](reports/maintenance-report.md) | Automated maintenance summary |
| 📄 [EPG Coverage](reports/epg-coverage.md) | Combined programme-guide coverage across all three maintained playlists |
| 🆕 [Update Report](reports/Update%20Report.md) | Generated snapshot; verify its timestamp and source fingerprint before treating metrics as current |
| ⚠️ [Stream Risk Review](reports/stream-risk-review.md) | Fragile, signed/tokenized and higher-risk stream references |

📚 For Playlist Studio and project information, see the **[Documentation](docs/README.md)**.

---

## 📦 Delivery & Rollback

The public playlists and logos are served from the repository's `main` branch through GitHub's raw-content delivery. This is convenient for live updates, but a bad commit can become visible immediately.

For applications that support it, pin consumption to a reviewed commit SHA rather than `main` when reproducibility matters. Maintenance history and Git history provide rollback points; this project does not promise immutable `main` content.

---

## 📬 Support

Found a broken stream, incorrect information, missing logo, or another issue?

<p align="center">
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/issues"><img src="https://img.shields.io/badge/🐞%20Report%20an%20Issue-e5534b?style=for-the-badge" alt="Report an issue"></a>
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/discussions"><img src="https://img.shields.io/badge/💬%20Join%20Discussions-8250df?style=for-the-badge" alt="Join Discussions"></a>
</p>

> 📝 For stream reports, include the **channel name, stream/playlist URL, and a short description** when possible.

---

## 📞 Contact

For collaboration, feedback, IPTV playlist issues, or project-related inquiries:

<p align="center">
  <a href="mailto:saeidrahman.mkt@gmail.com"><img src="https://img.shields.io/badge/Email-saeidrahman.mkt@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://github.com/saeidrahmanbd"><img src="https://img.shields.io/badge/GitHub-saeidrahmanbd-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://www.facebook.com/saeid.rahman.sr"><img src="https://img.shields.io/badge/Facebook-Saeid%20Rahman-1877F2?style=for-the-badge&logo=facebook" alt="Facebook"></a>
</p>

---

## 📄 License

The repository's original code and documentation are licensed under the [MIT License](LICENSE), to the extent owned by the maintainer. The license does **not** relicense third-party broadcaster logos, names, trademarks, programme data, stream endpoints, or other third-party content; those remain subject to their respective owners' rights and terms. Many logo assets are still under authenticity review, so local storage does not imply official verification.

## ⚠️ Disclaimer

This repository does not host television channels or video content. It contains references to publicly available streams. Availability and programme information may change without notice.

Users are responsible for complying with applicable laws, regulations, and service terms.

---

<p align="center">
  ⭐ <b>If you find the project useful, consider starring the repository.</b><br><br>
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV">github.com/saeidrahmanbd/BDIX-IPTV</a><br><br>
  <sub>Made with ❤️ by <a href="https://github.com/saeidrahmanbd">Saeid Rahman</a></sub>
</p>
