# 📺 Saeid Rahman — BDIX IPTV Playlist

A curated IPTV playlist focused on Bangladeshi, Indian and selected international channels, with local logos, backups, EPG mapping and automated quality controls.

## 📂 Playlist

[Open Main M3U Playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u)

## 📊 Automated quality system

The repository now maintains:

- EPG identity mapping, source status and current/future programme coverage
- Canonical channel identity indexing
- Local logo integrity and recovery
- Duplicate URL, metadata, identity and channel-number audits
- Non-destructive stream health checks with persistent per-URL failure history
- Maintenance history and a generated project dashboard
- A pre-publish safety gate

## 🛡️ Protection rules

1. Duplicate stream URLs are never allowed.
2. Existing primary streams are not silently removed.
3. Backup streams are never deleted because a health check fails.
4. New Channels and New Backup remain user-controlled review queues.
5. Health failures become review candidates, not automatic deletion decisions.
6. Dashboard figures are generated from the current playlist and current reports.
7. Every maintenance run records quality metrics.

## 📈 Reports

- [Dashboard](reports/dashboard.md)
- [Playlist audit](reports/playlist-audit.md)
- [Stream health](reports/stream-health.md)
- [Maintenance report](reports/maintenance-report.md)
- [EPG coverage](reports/epg-coverage.md)

## ⚠️ Disclaimer

This repository contains references to publicly available streams. Availability and programme information may change. Users are responsible for complying with applicable laws, regulations and service terms.

Repository: https://github.com/saeidrahmanbd/BDIX-IPTV
