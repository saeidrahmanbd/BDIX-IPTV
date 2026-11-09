# BDIX-IPTV SEO Audit & Search Visibility

This document records the repository's search-engine setup, the public pages intended for indexing, and the off-site actions that help people discover the project. It is an operational checklist, not a claim that the site currently ranks for particular keywords.

## Latest SEO maintenance — 2026-11-09

- Corrected the English homepage title, H1, meta description, Open Graph title and Twitter title to consistently describe Bangladesh, India and the wider multi-country collection.
- Updated the English playlist guide title and description and aligned its social-sharing titles.
- Updated structured-data modification dates for changed English pages and kept the XML sitemap dates aligned with actual page changes.
- Confirmed all three public pages have unique titles and descriptions, matching canonical and Open Graph URLs, and valid JSON-LD blocks.
- GitHub Actions completed the SEO validation successfully and the GitHub Pages deployment succeeded.
- The IndexNow workflow confirmed that its verification-key file is publicly reachable and received HTTP 200 after submitting the three canonical landing-page URLs. This is a successful notification, not proof of crawling or indexing.

## Public pages

The canonical English and Bengali landing pages are:

- [English homepage](https://saeidrahmanbd.github.io/BDIX-IPTV/)
- [Multi-country IPTV M3U playlist guide](https://saeidrahmanbd.github.io/BDIX-IPTV/playlists.html)
- [বাংলা IPTV পৃষ্ঠা](https://saeidrahmanbd.github.io/BDIX-IPTV/bangla-iptv.html)

The public sitemap files are:

- [XML sitemap](https://saeidrahmanbd.github.io/BDIX-IPTV/sitemap.xml)
- [Text sitemap](https://saeidrahmanbd.github.io/BDIX-IPTV/sitemap.txt)

Only the three canonical HTML landing pages are listed. Playlist files, generated reports, internal documentation, logos and workflow files are not standalone search landing pages and are not included in the sitemap.

## Implemented on the website and in the repository

- Distinct page titles and meta descriptions for the English homepage, English playlist guide and Bengali landing page.
- Self-referencing canonical URLs and matching Open Graph URLs.
- Reciprocal English/Bengali language alternates on the English homepage and Bengali page.
- Open Graph and Twitter sharing metadata with descriptive image alternatives.
- WebSite, WebPage, CollectionPage and BreadcrumbList structured data where appropriate.
- Descriptive internal links between the homepage, playlist guide and Bengali page.
- XML and plain-text sitemaps containing only the canonical public landing pages.
- An IndexNow key file and GitHub Actions notification workflow for participating search engines when public landing pages change.
- A GitHub Actions SEO validation workflow that checks titles, descriptions, canonical URLs, indexability, H1 headings, image alt text, local links and sitemap consistency.

The project homepage uses a GitHub Pages project URL under the saeidrahmanbd.github.io host and the BDIX-IPTV path. A robots.txt file must be served from the origin's root (https://saeidrahmanbd.github.io/robots.txt), not merely from the repository subdirectory. The repository does not control that origin-root file, so this project does not add a misleading docs/robots.txt. The sitemap can be submitted directly in Search Console and Bing Webmaster Tools.

## Google Search Console

A Google site-verification meta tag is already present in the English homepage. Confirm that the matching URL-prefix property is verified in the Google account that owns the site:

https://saeidrahmanbd.github.io/BDIX-IPTV/

Then:

1. Open [Google Search Console](https://search.google.com/search-console).
2. Select the exact URL-prefix property above.
3. Open **Sitemaps** and submit sitemap.xml (the URL is https://saeidrahmanbd.github.io/BDIX-IPTV/sitemap.xml).
4. Use **URL Inspection** for the homepage, playlist guide and Bengali page. Check the indexed canonical URL, last crawl and any page indexing issue.
5. Use **Performance → Search results** to compare clicks, impressions, CTR and average position over 28-day periods.
6. Review **Queries**, **Pages**, **Countries** and **Devices** separately. Prioritize Bangladesh and India, and compare desktop with mobile.
7. Request indexing after meaningful page changes only. Repeatedly submitting an unchanged URL does not make Google crawl it faster.

Google treats sitemap submission as a discovery hint, not a guarantee of crawling or indexing. Search Console is the authoritative place to inspect Google's actual status for this property.

## Bing and other IndexNow participants

The repository includes an IndexNow workflow. When one of the public landing pages or the XML sitemap changes on main, GitHub Actions checks that the public verification-key file is reachable and submits the three canonical page URLs to IndexNow.

- [Bing Webmaster Tools](https://www.bing.com/webmasters/about)
- [Bing URL Inspection](https://www.bing.com/webmasters/help/URL-Inspection-55a30305)
- [Bing Sitemaps](https://www2.bing.com/webmasters/help/sitemaps-3b5cf6ed)
- [IndexNow protocol and FAQ](https://www.indexnow.org/faq)

If you already have a verified Google Search Console property, Bing can import that site and its sitemap after you authorize the connection. Otherwise, add and verify the GitHub Pages URL-prefix property in Bing manually, then submit sitemap.xml.

An initial repository workflow run received HTTP 202 from IndexNow, which means the URL notification was received while key validation was pending. After correcting the workflow status handling, the latest run returned HTTP 200, the protocol's successful-submission response. Neither response proves that a search engine crawled or indexed the pages; confirm processing in Bing Webmaster Tools under the IndexNow report. IndexNow notifies participating search engines about URL additions, updates and removals. It is not a Google indexing mechanism; Google does not currently participate in IndexNow. Continue using Google's sitemap and Search Console tools for Google.

## GitHub repository discoverability

The repository's GitHub description, topics, homepage field and README are also discovery surfaces. The current repository already has a homepage URL and relevant topics such as bangladesh-iptv, bangla-iptv, bdix-iptv, iptv-m3u, iptv-m3u8, iptv-playlist and epg.

The repository's live GitHub **About** description and topic list were checked on 2026-11-09.

Current description:

> Free Bangladesh, India, & International IPTV M3U/M3U8 playlists featuring Bangla TV, Indian channels, international movies and music, and an XMLTV EPG.

The homepage field points to the English landing page. Existing topics already cover Bangladesh IPTV, Bangla TV, BDIX, India IPTV, international IPTV, M3U/M3U8 and XMLTV/EPG. The repository currently uses GitHub's 20-topic allowance, so any future topic additions should replace a less useful topic rather than exceed the limit.

The available GitHub connector can update repository files but does not expose the About/topics editor. No repository description or topic change is pending at this time.

## Off-site discovery and backlinks

External links from relevant pages help people discover the project and help search engines find its public pages. Focus on genuine relevance rather than bulk link submissions.

Recommended actions:

1. Keep the repository's website field pointed to the English homepage (already configured).
2. Keep the English homepage, Bengali landing page and playlist guide linked from the root README (already present).
3. Add the project website link to relevant personal or project profile descriptions that you control, including your Facebook profile if appropriate.
4. When sharing the project in IPTV or Bangla-tech communities, provide a useful explanation and link to the playlist guide rather than posting repeated promotional links.
5. Invite genuine references from relevant blogs, app guides or community resource pages when the project is useful to their readers. Avoid paid link schemes, automated comment links and unrelated directory submissions.
6. Keep the public project description consistent across GitHub and social profiles: multi-country IPTV M3U/M3U8 playlists covering Bangladesh, India, Pakistan and eligible channels from other countries, Bangla TV, international movie/music collections and XMLTV EPG.

External social posts, directory submissions and other account-level changes are not performed by repository workflows. Publish them only from accounts you control and follow each community's posting rules.

## Search topics to measure

These are query themes to observe in actual search reports; they are not claims that the site currently ranks for them.

| Search theme | Example searches |
|---|---|
| Bangladesh IPTV | Bangladesh IPTV, Bangladeshi IPTV, BDIX IPTV |
| Bangla TV | Bangla TV channels, Bangla IPTV, বাংলা টিভি চ্যানেল |
| M3U playlists | Bangladesh IPTV M3U, Bangla IPTV M3U playlist, M3U playlist Bangladesh |
| India collection | India IPTV M3U, Indian Bangla TV playlist |
| International collection | International IPTV M3U, international movie and music channels |
| Bengali-language discovery | বাংলাদেশি IPTV, বাংলা IPTV M3U, বাংলা টিভি প্লেলিস্ট |

Use Search Console data to decide which topics merit clearer explanations. Do not repeat search phrases unnaturally or add content that does not help a visitor.

## Review schedule

| Frequency | Review |
|---|---|
| Monthly | Compare Search Console clicks, impressions, CTR and queries for the last 28 days against the previous 28 days. |
| Monthly | Check Bing Webmaster Tools indexing and sitemap status. |
| After meaningful page changes | Check the URL in Search Console and confirm the IndexNow workflow completed successfully. |
| Quarterly | Review titles, descriptions, language alternates, public links, page usefulness and the repository About details. |

## Measurement limits

- Search engines decide whether and when to crawl, index and rank pages. Sitemap submissions and IndexNow notifications do not guarantee inclusion.
- Search Console measures Google Search performance, not all search engines or actual IPTV viewing.
- A click on an M3U URL does not prove that a stream played.
- Public search-result spot checks are not a substitute for Search Console or Bing Webmaster Tools indexing reports.
- No README, keyword, structured-data block or backlink guarantees a ranking position or AI Overview citation.
