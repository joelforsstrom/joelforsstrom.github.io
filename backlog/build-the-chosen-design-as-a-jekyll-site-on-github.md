---
id: 3uey
title: Build the chosen design as a Jekyll site on GitHub Pages
kind: task
status: doing
size: M
created: 2026-10-29
updated: 2026-10-30
tags: [site]
sessions: [cc837b2f-f9aa-5d68-bf1f-89606383da7a]
---

Replace the webpack 3 / node-sass toolchain with Jekyll that GitHub Pages builds natively (no Actions workflow). Content model: _data/cv.yml (bilingual rows), _data/videos.yml, _data/news.yml, Markdown pages per language; / stays Swedish, /fi/ Finnish, so old URLs keep working. Port the chosen mockup CSS from mockups/. Keep CNAME. Keep or redirect old CV PDF URLs. Remove mockups/ when done.

Update 2026-10-30, decisions from the mockup review (mockups/ on branch mockups-2026 is the reference):
- Port mockups/shared/site.css, keeping only the chosen palette and font pair. Leave out mockup.js and the mockup bar.
- "Aktuellt" on the home page is off by default and controlled by one setting (see the CMS item).
- Lightbox: PhotoSwipe 5.4.4 (MIT), vendored in shared/vendor/photoswipe, with the labels and caption in site.js.
- Video thumbnails are self-hosted so nothing contacts YouTube before play; new videos need a thumbnail too.
- The CV PDFs come from print_cv.py and the print stylesheet.
- Consider self-hosting the fonts instead of loading Google Fonts, which sends visitor IPs to Google.
