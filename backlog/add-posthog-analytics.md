---
id: t66n
title: Add PostHog analytics
kind: task
status: todo
size: XS
created: 2026-10-29
updated: 2026-10-30
tags: [site]
priority: 2
---

Decided: the site uses PostHog, not Google Analytics. Remove the old Universal Analytics tag (UA-87934251-1, dead since 2023) when the new site is built, and do not add GA4.

To do: add the PostHog snippet to the Jekyll layout, leave it out of /admin/, and use the EU host if the project is in PostHog's EU cloud.

Open: the human needs to provide the PostHog project key. Decide whether to run cookieless (persistence: memory) or ask visitors for consent.
