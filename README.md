# BDIX-IPTV: Bangladesh IPTV M3U/M3U8 Playlists & XMLTV EPG

<div align="center">

<img src="assets/header.svg" alt="BDIX-IPTV: free Bangladesh IPTV M3U/M3U8 playlists and XMLTV EPG for Bangla, Indian, Pakistani and international channels" width="100%">

### 📺 Free, curated IPTV playlists for Bangla TV, Indian, Pakistani and international channels

Get ready-to-use **M3U/M3U8 playlist URLs**, organized channel groups, local logos, alternate streams and a shared **XMLTV EPG** (TV programme guide) for compatible IPTV players.

<br>

<a href="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u"><img src="https://img.shields.io/badge/▶_Main_Playlist-0969da?style=for-the-badge" alt="Get the main IPTV playlist"></a>
<a href="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u"><img src="https://img.shields.io/badge/▶_International_Playlist-8957e5?style=for-the-badge" alt="Get the international IPTV playlist"></a>
<a href="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml"><img src="https://img.shields.io/badge/🗓️_XMLTV_EPG-2ea44f?style=for-the-badge" alt="Get the XMLTV EPG"></a>

<a href="https://saeidrahmanbd.github.io/BDIX-IPTV/">🌐 Project website</a> &nbsp;•&nbsp;
<a href="https://saeidrahmanbd.github.io/BDIX-IPTV/playlists.html">📖 Playlist guide</a> &nbsp;•&nbsp;
<a href="https://saeidrahmanbd.github.io/BDIX-IPTV/bangla-iptv.html">🇧🇩 বাংলা গাইড</a> &nbsp;•&nbsp;
<a href="#faq">❓ FAQ</a>

<br>

<img src="https://img.shields.io/github/stars/saeidrahmanbd/BDIX-IPTV?style=flat-square&color=f5c542" alt="GitHub stars">
<img src="https://img.shields.io/github/last-commit/saeidrahmanbd/BDIX-IPTV/main?style=flat-square&color=0969da" alt="Last commit">
<img src="https://img.shields.io/badge/license-MIT-yellow?style=flat-square" alt="MIT License">
<img src="https://img.shields.io/badge/automation-GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions automation">

</div>

---

## 🚀 Quick Start

Three steps to start watching:

1. **📋 Copy a playlist URL** from [Choose a playlist](#playlists).
2. **➕ Add it to your IPTV player** using *Add Playlist by URL* (the wording varies by app).
3. **🗓️ Add the TV guide.** Paste the [XMLTV EPG URL](#epg) into your player's EPG settings and refresh.

> [!TIP]
> New to IPTV? Follow the [step-by-step playlist guide](https://saeidrahmanbd.github.io/BDIX-IPTV/playlists.html), or read the [বাংলা IPTV গাইড](https://saeidrahmanbd.github.io/BDIX-IPTV/bangla-iptv.html) in Bangla.

---

## ✨ Why BDIX-IPTV?

| | |
|:---:|---|
| 🇧🇩 | **Bangla-first.** Bangladesh channels are the focus, with Indian and Pakistani channels and eligible international selections alongside. |
| 🗂️ | **Organized.** Channels are sorted into country and genre groups that work well in compatible players. |
| 🗓️ | **Programme guide included.** One shared XMLTV EPG serves both playlists, with coverage reports so you can see what is mapped. |
| 🖼️ | **Local logos.** Logo assets are hosted in the repository where available. |
| 🔁 | **Alternate streams.** Backup entries are kept where they are maintained. |
| 🩺 | **Transparent.** Automated checks publish reports, so you can see the evidence instead of trusting unverified claims. |
| 🆓 | **Free and open.** The playlists and project information are publicly accessible under the MIT License. |

> [!NOTE]
> Streams and programme schedules can change or stop without notice. A listed channel does not guarantee a working stream or EPG data. See [Reports](#reports) for the latest checks.

---

## 📡 Choose a Playlist

### 🟦 Main Multi-Country Playlist: `IPTV-Playlist.m3u`

Covers Bangladesh, India, Pakistan and eligible channels from other countries, grouped by country and genre. **Most users should start here.**

```text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u
```

[📥 Download](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u) · [🔍 View source](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/IPTV-Playlist.m3u)

### 🟪 International Playlist: `International-Playlist.m3u`

A companion collection with Bangladesh and India, plus eligible movie, music and other permitted selections from additional countries.

```text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u
```

[📥 Download](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u) · [🔍 View source](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/International-Playlist.m3u)

| If you want… | Choose |
|---|---|
| The main organized multi-country collection | `IPTV-Playlist.m3u` |
| The separate international companion collection | `International-Playlist.m3u` |
| A visual setup walkthrough | [Playlist guide](https://saeidrahmanbd.github.io/BDIX-IPTV/playlists.html) |
| Instructions in Bangla | [বাংলা IPTV গাইড](https://saeidrahmanbd.github.io/BDIX-IPTV/bangla-iptv.html) |

---

## 📱 Compatible IPTV Players

The playlists use the widely supported M3U/M3U8 format and work with any IPTV application that accepts remote playlist URLs:

- XCIPTV
- TiviMate
- OTT Navigator
- IPTV Smarters
- VLC media player
- Kodi
- Other M3U-compatible IPTV apps

> [!TIP]
> **General setup:** open your player, choose *Add Playlist* or *Add Playlist by URL*, paste a playlist URL, then save and refresh. Menu names vary by app and device.

This project does not provide, endorse or require any particular third-party player.

---

## 🗓️ EPG: TV Programme Guide

Both playlists use the shared **XMLTV EPG**, which provides programme schedules for channels with matching IDs.

```text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml
```

### How to add the EPG

1. Open your player's EPG or TV Guide settings.
2. Add an external XMLTV source or EPG URL.
3. Paste the URL above, save, and refresh the guide.
4. If a channel has no programme data, check that its `tvg-id` matches an ID in the guide.

### Understanding coverage

Not every channel has programme data. Coverage depends on source availability, channel-ID matching and the schedule window from programme-guide providers.

- 📊 [Latest EPG coverage and mapping report](reports/epg-coverage.md)
- 📚 [Public EPG documentation](epg/README.md)
- 📂 [EPG source and mapping files](epg/)

> [!IMPORTANT]
> **Empty guide?** Refresh the EPG, verify the XMLTV URL, check the channel's `tvg-id`, and consult the latest coverage report.

---

## 📊 Reports

Audit and diagnostic reports are generated at different times. Each one describes the inputs and checks recorded in that report. Please check each report's timestamp.

| Report | What it shows |
|---|---|
| [IPTV Playlist Audit](reports/iptv-playlist-audit.md) | Channel identity, metadata, duplicate and logo checks |
| [Stream Health Report](reports/stream-health.md) | Results and limits of stream probes |
| [EPG Coverage Report](reports/epg-coverage.md) | EPG mapping and programme coverage |
| [Channel Discovery Report](reports/iptv-channel-discovery.md) | Discovery activity and candidate channels |
| [Backup Independence Audit](reports/backup-independence-audit.md) | Backup stream and identity review |
| [Stream Risk Review](reports/stream-risk-review.md) | Stream risk and review findings |

> [!NOTE]
> A report is a snapshot of its stated inputs and test environment, not a guarantee of future availability.

---

## ⚙️ How Maintenance Works

Scripts and GitHub Actions support repeatable maintenance:

<div align="center">

<img src="assets/how-it-works.svg" alt="BDIX-IPTV workflow: discovery, stream checks, playlist maintenance, EPG mapping, publication and your IPTV player" width="100%">

</div>

| Stage | Process |
|:---:|---|
| 1 | **Discovery:** identify potential channels and candidate stream references for review. |
| 2 | **Identity checks:** examine names, groups, identifiers and duplicates. |
| 3 | **Stream diagnostics:** probe endpoints and record each outcome and its limits. |
| 4 | **Logo maintenance:** use locally stored assets and review matches where evidence exists. |
| 5 | **EPG mapping:** associate channel IDs with XMLTV schedules and validate the guide. |
| 6 | **Publication:** publish changes after workflow checks and validation. |

> [!WARNING]
> A successful probe does not guarantee a stream will stay available everywhere. A failed probe may reflect a temporary restriction, timeout or test environment. See the [stream health report](reports/stream-health.md).

**Project resources:** [GitHub Actions](https://github.com/saeidrahmanbd/BDIX-IPTV/actions) · [Contributing guide](docs/CONTRIBUTING.md) · [Security policy](docs/SECURITY.md) · [Documentation index](docs/README.md)

---

## 🖥️ Playlist Studio 5.1 for Windows

**Playlist Studio** is a separate Windows application, maintained by the project owner, for managing, editing, checking and playing M3U/M3U8 playlists in one desktop workspace.

<div align="center">

<a href="https://github.com/saeidrahmanbd/BDIX-IPTV/releases/tag/v5.1">
  <img src="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/assets/Playlist-Studio-5.1.JPG" alt="Playlist Studio 5.1 Windows IPTV playlist editor, XMLTV EPG centre and stream scanner" width="85%">
</a>

</div>

### Highlights

- 📝 **Editor:** organize channels, categories and metadata.
- 🗓️ **XMLTV EPG Centre:** load guides from URLs or local XML, GZ, XZ and ZIP files; inspect coverage and Now/Next information.
- ✏️ **EPG editing:** search and edit `tvg-id` values, preview bulk edits and keep manual corrections.
- 🩺 **Stream scanner:** review Responsive, Dead, Unreachable, Restricted, Stale, Unavailable, Unverified and Error outcomes. Timeouts and blocked requests are not automatically labelled Dead.
- 🎛️ **Scan controls:** pause, resume, cancel, and set limits, timeouts and retries.
- 🔌 **Xtream Codes and Stalker/MAC:** import supported provider playlists in the background, with safer credential handling.
- 🛡️ **Safer editing:** preserves playlist directives and unknown header keys, with backup and recovery.

### Download

<div align="center">

<a href="https://github.com/saeidrahmanbd/BDIX-IPTV/releases/download/v5.1/Playlist-Studio-5.1.exe"><img src="https://img.shields.io/badge/⬇_Download_Portable_EXE-0969da?style=for-the-badge" alt="Download Playlist Studio 5.1 portable executable"></a>
<a href="https://github.com/saeidrahmanbd/BDIX-IPTV/releases/tag/v5.1"><img src="https://img.shields.io/badge/Release_notes-24292f?style=for-the-badge&logo=github" alt="Playlist Studio 5.1 release notes"></a>

</div>

| Requirement | Details |
|---|---|
| Operating system | Windows 10 / 11 |
| Architecture | 64-bit (x64) |
| Edition | Portable executable; no traditional installation |
| Playlist formats | M3U / M3U8 |
| EPG formats | XMLTV from URLs and supported local files |
| Playback | Built-in player with bundled VLC engine |

The release includes a Windows Build Kit. See the [build instructions](docs/PLAYLIST-STUDIO.md) and [release integrity record](docs/PLAYLIST-STUDIO-INTEGRITY.md).

> [!CAUTION]
> **Windows SmartScreen:** the executable is unsigned and Windows may show a warning. Download it only from the official release and review the release notes first.

Product repository and future releases: [Playlist Studio on GitHub](https://github.com/saeidrahmanbd/Playlist-Studio).

---

<a id="faq"></a>

## ❓ Frequently Asked Questions

<details>
<summary><strong>Is BDIX-IPTV free?</strong></summary>

<br>

The playlists and project information are publicly accessible. Third-party players, internet access and external services may have their own costs or terms.
</details>

<details>
<summary><strong>Does BDIX-IPTV host TV channels or video?</strong></summary>

<br>

No. This repository provides playlist references and metadata. It does not host broadcasts, video or broadcaster infrastructure.
</details>

<details>
<summary><strong>Why is a channel listed but not playing?</strong></summary>

<br>

Stream endpoints can change, become restricted or go offline. Check the [stream health report](reports/stream-health.md) and try again later.
</details>

<details>
<summary><strong>Why is the TV guide empty for some channels?</strong></summary>

<br>

Not every channel has a matching XMLTV programme source. Check the channel's `tvg-id`, refresh your EPG and consult the [EPG coverage report](reports/epg-coverage.md).
</details>

<details>
<summary><strong>Can I use these in TiviMate, XCIPTV, VLC or Kodi?</strong></summary>

<br>

Yes, these apps support M3U playlists or remote playlist URLs. Setup varies by app and device.
</details>

<details>
<summary><strong>How do I report a broken stream or wrong channel information?</strong></summary>

<br>

Open a [GitHub Issue](https://github.com/saeidrahmanbd/BDIX-IPTV/issues) with the channel name, playlist name, stream URL, player or device, and a short description. Never post private provider credentials or tokens.
</details>

<details>
<summary><strong>Can I contribute?</strong></summary>

<br>

Yes. Read the [contributing guide](docs/CONTRIBUTING.md), then open an issue or discussion before proposing changes to playlist policies or maintenance.
</details>

---

## 💬 Support and Contact

Found a broken stream, wrong channel information, a missing logo or an EPG mapping issue? Please open an issue with enough detail to reproduce it.

<div align="center">

<a href="https://github.com/saeidrahmanbd/BDIX-IPTV/issues"><img src="https://img.shields.io/badge/🐞_Report_an_issue-e5534b?style=for-the-badge" alt="Report a BDIX-IPTV issue"></a>
<a href="https://github.com/saeidrahmanbd/BDIX-IPTV/discussions"><img src="https://img.shields.io/badge/💬_Discussions-8250df?style=for-the-badge" alt="BDIX-IPTV discussions"></a>

**Maintainer: Saeid Rahman**

<a href="mailto:saeidrahman.mkt@gmail.com"><img src="https://img.shields.io/badge/Email-saeidrahman.mkt@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email Saeid Rahman"></a>
<a href="https://github.com/saeidrahmanbd"><img src="https://img.shields.io/badge/GitHub-saeidrahmanbd-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub Saeid Rahman"></a>
<a href="https://www.facebook.com/saeid.rahman.sr"><img src="https://img.shields.io/badge/Facebook-Saeid_Rahman-1877F2?style=flat-square&logo=facebook&logoColor=white" alt="Facebook Saeid Rahman"></a>

</div>

---

## ⚖️ License and Disclaimer

The repository's original code and documentation are licensed under the [MIT License](LICENSE), to the extent owned by the maintainer.

The MIT License does **not** grant rights to third-party broadcaster names, channel logos, trademarks, programme information, stream endpoints, artwork or other third-party materials. Those remain subject to their owners' rights and applicable terms. A logo stored here is not thereby verified as official or relicensed under MIT.

> [!IMPORTANT]
> This project does not host television channels, broadcast signals or video. It provides references to streams and playlist information. Availability and programme data may change without notice. Users are responsible for complying with applicable laws, broadcaster rights and service terms. No uninterrupted service, specific channel availability or complete EPG coverage is guaranteed.

---

<div align="center">

**⭐ Find BDIX-IPTV useful? Star the project on GitHub.**

<a href="https://github.com/saeidrahmanbd/BDIX-IPTV/stargazers"><img src="https://img.shields.io/badge/Star-BDIX--IPTV-f5c542?style=for-the-badge&logo=github&logoColor=white" alt="Star the BDIX-IPTV repository"></a>

Maintained by <a href="https://github.com/saeidrahmanbd"><strong>Saeid Rahman</strong></a> · <a href="#">⬆️ Back to top</a>

<img src="assets/footer.svg" alt="" width="100%">

</div>
