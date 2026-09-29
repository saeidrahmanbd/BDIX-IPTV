# 📚 BDIX-IPTV Documentation

Welcome to the documentation hub for **BDIX-IPTV**.

## Quick links

| Resource | Description |
|---|---|
| 📺 [Main M3U Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u) | Current maintained IPTV playlist |
| 🖥️ [Playlist Studio](https://github.com/saeidrahmanbd/BDIX-IPTV/releases/latest) | Latest Windows portable playlist editor |
| 🛜 [Xtream Gateway](../xtream/README.md) | Xtream Codes-compatible gateway documentation |
| 📡 [EPG Documentation](../epg/README.md) | EPG sources, validation and related files |
| ⚙️ [Sample Configuration](../examples/sample-config.md) | Safe configuration examples |
| 📥 [Download Center](DOWNLOADS.md) | Main download and access links |
| 📝 [Changelog](CHANGELOG.md) | Recent playlist changes |

## 📺 Playlist

The repository's main playlist is:

```text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u
```

The playlist is organized into channel groups and includes channel metadata and repository-hosted logos.

## 🛜 Xtream Gateway

The optional gateway exposes the playlist through an Xtream Codes-compatible API for clients such as XCIPTV.

Read the [Xtream Gateway documentation](../xtream/README.md) for deployment, credentials and supported endpoints.

## 📡 EPG

EPG configuration is maintained separately from the main playlist. See the [EPG documentation](../epg/README.md) for the available sources and related files.

## 🖥️ Playlist Studio

[Playlist Studio](https://github.com/saeidrahmanbd/BDIX-IPTV/releases/latest) is the Windows portable application used for playlist management and playback-related workflows.

## 🔧 Repository structure

```text
BDIX-IPTV/
├── IPTV-Playlist.m3u       # Main playlist
├── docs/                   # Project documentation and changelog
├── epg/                    # EPG tools and configuration
├── examples/               # Configuration examples
├── xtream/                 # Xtream Gateway
├── logos/                  # Local PNG channel logos
└── assets/                 # Project and application assets
```

## ⚠️ Important

The repository links to third-party stream sources. Availability, geo-restrictions and stream behavior can change independently of this repository.

For the latest downloads, use the [Download Center](DOWNLOADS.md).
