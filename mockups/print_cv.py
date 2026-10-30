"""Prints the CV pages to shared/cv-{sv,fi}.pdf using the print stylesheet. Runs in the fujibox-screenshot image:

podman run --rm -i --network host --shm-size 1g --cap-drop ALL --security-opt no-new-privileges \
  --security-opt label=disable -v "$PWD/shared:/out" localhost/fujibox-screenshot:1.63.0 python3 - < print_cv.py
"""
from playwright.sync_api import sync_playwright

FOOTER = ('<div style="font-size:8px;width:100%;text-align:center;color:#666">'
          'Joel Forsström · <span class="pageNumber"></span>/<span class="totalPages"></span></div>')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    for lang in ("sv", "fi"):
        page.goto(f"http://127.0.0.1:8118/{lang}/cv.html", wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        page.pdf(path=f"/out/cv-{lang}.pdf", format="A4", display_header_footer=True,
                 header_template="<span></span>", footer_template=FOOTER,
                 margin={"top": "14mm", "bottom": "16mm", "left": "14mm", "right": "14mm"})
    browser.close()
