"""Prints the CV pages to assets/cv/  using the print stylesheet. Runs in the fujibox-screenshot image:

podman run --rm -i --network host --shm-size 1g --cap-drop ALL --security-opt no-new-privileges \
  --security-opt label=disable -v "$PWD/assets/cv:/out" localhost/fujibox-screenshot:1.63.0 python3 - < tools/print_cv.py
"""
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8120"  # a local build of the site

FOOTER = ('<div style="font-size:8px;width:100%;text-align:center;color:#666">'
          'Joel Forsström · <span class="pageNumber"></span>/<span class="totalPages"></span></div>')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    for lang, path in (("sv", "/cv/"), ("fi", "/fi/cv/")):
        page.goto(f"{BASE}{path}", wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        page.pdf(path=f"/out/joel-forsstrom-cv-{lang}.pdf", format="A4", display_header_footer=True,
                 header_template="<span></span>", footer_template=FOOTER,
                 margin={"top": "14mm", "bottom": "16mm", "left": "14mm", "right": "14mm"})
    browser.close()
