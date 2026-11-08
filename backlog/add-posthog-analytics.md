---
id: t66n
title: Add PostHog analytics
kind: task
status: doing
size: XS
created: 2026-10-29
updated: 2026-11-08
tags: [site]
priority: 2
sessions: [cse_017t6DEyKrrQsABK1EpP3SmQ]
---

Decided: the site uses PostHog, not Google Analytics. Remove the old Universal Analytics tag (UA-87934251-1, dead since 2023) when the new site is built, and do not add GA4.

To do: add the PostHog snippet to the Jekyll layout, leave it out of /admin/, and use the EU host if the project is in PostHog's EU cloud.

Decided (2026-11-08): cookieless, page views only: `cookieless_mode: 'always'` with `person_profiles: 'never'`, and autocapture, heatmaps, recordings and surveys off. No consent banner. The snippet is `_includes/posthog.html`, configured in `_config.yml` (`posthog.key`, `posthog.api_host`); /admin/ has its own page and no snippet. The old UA tag is already gone.

Open: the human puts the project key in `_config.yml` and turns on Settings > Project > Web analytics > Enable cookieless tracking in PostHog (without it PostHog drops the events).
