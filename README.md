<!-- BDIX-IPTV Banner -->
<p align="center">
  <img src="assets/Saeid%20Rahman.png" alt="BDIX-IPTV — Bangladesh & India IPTV Hub" width="100%">
</p>

# 📺 Saeid Rahman — BDIX IPTV Playlist

A personally curated IPTV playlist focused on **Bangladeshi channels, Indian channels, and selected international content**, with an emphasis on clean organization, usable streams, accurate metadata, and reliable backup options.

The playlist is continuously refined as channels and streams change.

## ✨ What this project focuses on

- 🇧🇩 Bangladesh channels organized in a dedicated category
- 🇮🇳 Indian channels grouped by language
- 🔁 Separate backup streams where useful alternatives are available
- 🧹 Duplicate and unsuitable stream entries removed
- 🖼️ Local channel logos with consistent metadata
- 🏷️ Clean channel names and categories
- 📡 Stream URLs reviewed and replaced when better alternatives are found
- 🆕 New channels kept separate during review before being integrated
- 🗓️ EPG compatibility and coverage improved as suitable sources become available

## 📂 Playlist

### Main playlist

Use the latest version from the repository:

**[IPTV-Playlist.m3u](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u)**

The playlist is intended for compatible IPTV players such as **XCIPTV** and other M3U-compatible applications.

## 📅 EPG Coverage

The repository now maintains a separate **EPG Coverage Report** instead of relying on blind source searching.

- 📊 Counts current playlist channels, matched channels, exact-ID matches, alias/name matches, and missing channels
- 🔎 Produces a focused **Missing Channels — Investigation Queue**
- 🕒 Checks whether matched channels actually have future programme data
- 🌐 Tests the configured EPG sources individually and records source failures
- 🛡️ Does **not** modify the playlist or publish an EPG feed

📄 **[View the latest EPG Coverage Report](reports/epg-coverage.md)**

The report is refreshed automatically every 12 hours.

## 📡 Stream Health

The playlist has a separate, non-destructive stream-health layer.

- 🟢 **Healthy / Redirect** — stream endpoint responds and HLS manifests pass validation
- 🟠 **Timeout / HTTP error / Connection error** — reported for investigation
- 🔴 **Invalid HLS** — endpoint responds but the HLS manifest is malformed or unusable
- ⚪ **Not Playing** — intentionally excluded from active failure scoring
- 🔁 **Repeated failures** — a stream is listed as an **obsolete candidate only after 3 consecutive health runs**
- 🛡️ **No automatic deletion** — one failed check never removes a stream from the playlist

📊 **[View the latest Stream Health Report](reports/stream-health.md)**

The health workflow runs automatically every 6 hours and keeps a persistent failure streak per stream URL.

The maintenance layer also maintains a **logical Primary → Backup 1 → Backup 2 → … hierarchy** for each channel using current health, repeated-failure history, and stable playlist order as a tie-breaker. This hierarchy is stored separately and does **not** reorder or delete playlist entries.

## 🖥️ Playlist Studio

**Playlist Studio** is the companion Windows application for playing, browsing, and managing IPTV playlists.

- 📦 **[Download the latest Playlist Studio release](https://github.com/saeidrahmanbd/BDIX-IPTV/releases/latest)**
- 📋 **[View all releases](https://github.com/saeidrahmanbd/BDIX-IPTV/releases)**
- 💻 Portable Windows application — no installation required

![Playlist Studio 2.8.2 — IPTV playlist editor and player](assets/Playlist-Studio-screenshot.png)

*Playlist Studio 2.8.2 — playlist management, channel organization, stream checking, and playback.*

## 🧭 Organization

The playlist is structured to make browsing easier rather than simply collecting as many streams as possible.

Examples of the project structure include:

- Bangladesh
- Indian channels by language
- Indian Backup
- News
- Sports
- Movies
- Music
- Kids
- Documentary
- Religious
- International

Categories and entries are periodically reviewed as the playlist evolves.

## 🔧 Maintenance

Playlist maintenance includes:

1. Checking stream availability
2. Removing duplicate URLs
3. Reviewing new channel candidates
4. Separating backup streams from primary entries
5. Fixing channel metadata
6. Maintaining local logo references
7. Improving EPG coverage where reliable sources are available
8. Removing obsolete or unsuitable entries
9. Auditing channel identity by playlist metadata IDs rather than stream URLs
10. Detecting duplicate IDs, metadata conflicts, name collisions, and logo integrity problems
11. Protecting primary curated entries from automatic metadata or stream changes

## 🔐 Identity & automatic updates

The automatic updater is intentionally **backup-only**. It does not add new channels and does not use a display-name or stream URL to decide channel identity. Alternate streams must match an existing playlist channel ID. A country-qualified identity that conflicts with an existing primary channel is rejected, so foreign `NTV`/`MTV`/similar feeds cannot be reintroduced as backups. Ambiguous logo-name matches are left unchanged rather than guessed.

A non-destructive playlist audit runs before automatic commits and checks duplicate identities, metadata conflicts, same-name/different-ID collisions, cross-country backup collisions, actual PNG readability/dimensions, logo variants, and unexpected changes to protected primary entries. Live stream health is audited separately so a temporary stream failure cannot change channel identity or metadata.

## 🖼️ Logos & metadata

Channel logos are maintained inside the repository whenever possible instead of relying on external image hosts.

This helps keep the playlist self-contained and reduces broken-logo problems caused by third-party image URLs.

## 🗓️ EPG

EPG coverage is an ongoing part of the project. Different EPG sources may cover different channel sets, so coverage is reviewed separately from the stream playlist.

## 📬 Contact & Support

If you find a broken stream, incorrect channel information, missing logo, or have a suggestion, you can contact me through the following channels:

- 🐞 **Report a technical issue:** [GitHub Issues](https://github.com/saeidrahmanbd/BDIX-IPTV/issues)
- 💡 **Suggestions & improvements:** [GitHub Issues](https://github.com/saeidrahmanbd/BDIX-IPTV/issues)
- 💬 **General project discussion:** [GitHub Discussions](https://github.com/saeidrahmanbd/BDIX-IPTV/discussions)
- 📧 **Email:** [saeidrahman.mkt@gmail.com](mailto:saeidrahman.mkt@gmail.com)
- 📘 **Facebook:** [Saeid Rahman](https://www.facebook.com/saeid.rahman.sr)
- 👤 **Maintainer:** [Saeid Rahman](https://github.com/saeidrahmanbd)

For stream reports, please include the **channel name, playlist/stream URL, and a short description of the problem** when possible.

## ⚠️ Disclaimer

This repository does **not host television channels or video content**.

The playlist contains stream references collected from publicly available sources. Stream availability, channel names, logos, and programme information may change without notice.

Users are responsible for ensuring that their use of any stream complies with applicable laws, regulations, and the terms of the relevant service providers.

## 👤 About

Created and maintained by **Saeid Rahman**.

This is primarily a personal IPTV organization and playlist-maintenance project.

---

⭐ If you find the project useful, you can star the repository.

**Repository:** https://github.com/saeidrahmanbd/BDIX-IPTV
