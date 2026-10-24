# Security Policy

## Reporting a security issue

Please do not publish credentials, private tokens, session URLs, or other sensitive stream information in a public issue.

For repository or automation security concerns, contact the maintainer through the email address listed in the project documentation or use a private GitHub communication channel when available.

## Sensitive stream URLs

Some stream URLs can contain short-lived tokens, signatures, sessions, usernames, or other access material. Reports and generated audit files should redact such values where possible. Do not commit working credentials or private deployment secrets.

## Scope

This policy covers the BDIX-IPTV repository, its GitHub Actions automation, generated reports, and the Xtream worker source maintained in this repository. Third-party broadcasters, CDNs, IPTV applications, and upstream stream providers are outside the repository's security scope.
