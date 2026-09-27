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
