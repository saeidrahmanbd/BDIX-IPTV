# Security Policy

## Supported versions

| Version | Security support |
|---|---|
| Default branch (`main`) | Best-effort security fixes |
| Older commits and release snapshots | Unsupported; upgrade to the latest reviewed revision |

This repository primarily publishes playlists, documentation, automation, and optional Cloudflare Worker source. A published playlist or stream endpoint is not a supported software release.

## Reporting a security issue

Please do not publish credentials, private tokens, session URLs, or other sensitive stream information in a public issue.

- **Email:** [saeidrahman.mkt@gmail.com](mailto:saeidrahman.mkt@gmail.com). Include “BDIX-IPTV security report” in the subject. Do not include live private credentials unless necessary; redact them where possible.
- **Private GitHub advisory:** [Open a private vulnerability report](https://github.com/saeidrahmanbd/BDIX-IPTV/security/advisories/new). This option depends on GitHub's private vulnerability reporting being enabled for the repository; use email if GitHub does not offer the form.

For security reports, include the affected path/workflow, impact, and reproducible steps. Please allow time for review before publicly disclosing an unpatched issue.

## Sensitive stream URLs

Some stream URLs can contain short-lived tokens, signatures, sessions, usernames, or other access material. Reports and generated audit files should redact such values where possible. Do not commit working credentials or private deployment secrets. Xtream-compatible URL paths may contain usernames/passwords by design; treat those URLs as secrets and redact them from logs, screenshots, and public reports.

## Scope

This policy covers the BDIX-IPTV repository, its GitHub Actions automation, generated reports, and the Xtream worker source maintained in this repository. Third-party broadcasters, CDNs, IPTV applications, and upstream stream providers are outside the repository's security scope.
