<!-- BDIX-IPTV banner -->
<p align="center">
  <img src="assets/bdix-iptv-banner.jpg" alt="BDIX-IPTV — Bangladesh, India and international IPTV playlists" width="100%">
</p>

<h1 align="center">📺 BDIX-IPTV</h1>

<p align="center">
  <b>Bangladesh & India IPTV Hub — Worldwide Channel Collections</b><br>
  Curated M3U playlists, organized categories, local logo assets, EPG mapping tools and automated quality checks.
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
  <img src="https://img.shields.io/badge/EPG-Refresh%20enabled%20%7C%20published-2ea44f?style=flat-square" alt="EPG refresh enabled and published">
  <a href="https://github.com/saeidrahmanbd/BDIX-IPTV/actions/workflows/iptv-maintenance.yml"><img src="https://github.com/saeidrahmanbd/BDIX-IPTV/actions/workflows/iptv-maintenance.yml/badge.svg" alt="IPTV Playlist Update workflow"></a>
</p>

<p align="center">
  <a href="#-playlists">Playlists</a> ·
  <a href="#-quick-start">Quick Start</a> ·
  <a href="#-epg">EPG</a> ·
  <a href="#-repository-showcase">Showcase</a> ·
  <a href="#-download-center">Downloads</a> ·
  <a href="#-playlist-studio">Playlist Studio</a> ·
  <a href="#-reports-and-status">Reports</a> ·
  <a href="#-support">Support</a>
</p>

---

## ✨ Overview

BDIX-IPTV maintains three M3U playlists for Bangladesh, India, BDIX-focused viewing and international channels, with organized categories, consistent metadata, repository-local logos, duplicate URL checks and reviewed backup references. The XMLTV refresh workflow is enabled and the public guide is published at the repository EPG endpoint.

| 🏷️ Channel Metadata | 🖼️ Logo Assets | 🩺 Stream Review | 🗓️ Programme Guide |
|:---:|:---:|:---:|:---:|
| Names, IDs and groups | Repository-local assets | Health and backup checks | EPG refresh enabled and published |

## 📺 Playlists

| Playlist | Description | Open |
|---|---|:---:|
| **IPTV-Playlist.m3u** | Main curated Bangladesh and India collection | [![Open](https://img.shields.io/badge/Open%20M3U-1f6feb?style=flat-square)](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u) |
| **BDIX-Playlist.m3u** | BDIX-focused channel collection | [![Open](https://img.shields.io/badge/Open%20M3U-2ea44f?style=flat-square)](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u) |
| **International-Playlist.m3u** | International movie and music country groups, with separate thematic categories | [![Open](https://img.shields.io/badge/Open%20M3U-8957e5?style=flat-square)](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u) |

---

## 🚀 Quick Start

Add a playlist URL to **XCIPTV** or any M3U-compatible player, such as TiviMate, VLC, IPTV Smarters or Kodi.

```text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u
```

<p align="center">
  <a href="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u">
    <img src="https://img.shields.io/badge/▶%20OPEN%20MAIN%20PLAYLIST-1f6feb?style=for-the-badge" alt="Open main M3U playlist">
  </a>
</p>

For another collection, copy its URL from the Playlists table. In your player, choose **Add playlist by M3U URL**, paste the link, save and refresh the channel list.

## 🗓️ EPG

The XMLTV refresh workflow is enabled and the public guide is published at [the target guide URL](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml). All three maintained playlists and both Xtream workers use this guide. The EPG pipeline combines useful public/accesssible sources, expands channel mappings, deduplicates schedules, applies freshness and quality checks, and publishes only validated XMLTV data. Source-review metadata is advisory, not a build or publication gate. See the [EPG status page](epg/README.md), [mapping CSV](reports/epg-channel-mapping.csv), [coverage report](reports/epg-coverage.md) and [published-playlist audit](reports/epg-three-playlist-audit.md).

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
| [Public EPG (XMLTV)](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml) | Published programme guide |
| [EPG Publication Status](reports/epg-coverage.md) | Current publication state and coverage |
| [Playlist Studio 5.0](https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5.0.exe) | Windows playlist manager, editor and player |
| [Playlist Studio Windows Build Kit](https://github.com/saeidrahmanbd/Playlist-Studio/releases/download/v5.0.0/Playlist-Studio-5_0-Windows-Build-Kit-Debug22.zip) | Windows build package |
| [Xtream Gateway documentation](xtream/README.md) | Optional Xtream-compatible access details |
| [Full Download Center](docs/DOWNLOADS.md) | All key downloads and documentation |
| [Documentation index](docs/README.md) | Project guides and references |

---

## 🖥️ Playlist Studio

[**Playlist Studio 5.0**](https://github.com/saeidrahmanbd/Playlist-Studio) is a separate Windows application for managing, editing, testing and playing IPTV playlists.
