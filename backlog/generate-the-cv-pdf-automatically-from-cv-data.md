---
id: k773
title: Generate the CV PDF automatically from CV data
kind: idea
status: dropped
size: S
created: 2026-10-29
updated: 2026-10-30
tags: [cv]
priority: 3
---

The mockups' cv-sv.pdf / cv-fi.pdf were printed from the CV page's print stylesheet with headless Chromium (no street address). In the real site, either Joel uploads a PDF through the CMS, or a build step prints it from the CV page. Printing would need an Actions workflow, which the human has to add.

Update 2026-10-30: tools/print_cv.py now does the printing by hand; Joel's route is uploading a PDF through the CMS unless this item is built.

Dropped 2026-10-30: the site offers Joel's own CV files for download, so no generated PDF is needed.
