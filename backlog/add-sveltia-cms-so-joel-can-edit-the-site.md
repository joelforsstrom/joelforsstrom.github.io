---
id: wdv7
title: Add Sveltia CMS so Joel can edit the site
kind: task
status: doing
size: S
created: 2026-10-29
updated: 2026-10-31
tags: [cms]
sessions: [cc837b2f-f9aa-5d68-bf1f-89606383da7a]
---

admin/index.html (Sveltia from CDN, pinned version) and admin/config.yml with collections for bio (sv/fi), news, videos, CV data, gallery, and media uploads incl. the CV PDF. Login: GitHub personal access token for a start; optional sveltia-cms-auth Cloudflare Worker + GitHub OAuth app (human's step). Write a short Swedish guide for Joel.

Update 2026-10-30: add a "Visa Aktuellt" on/off setting (default off) so Joel can show or hide the home page news section; the news entries stay stored while it is off. The gallery is an even 3-column grid, so note in Joel's guide that a multiple of three photos fills it evenly on desktop.
