#!/usr/bin/env python3
"""Generates the mockup pages: mockups/{sv,fi}/{index,bio,media,cv}.html and the overview page.

Run from anywhere: python3 mockups/build.py
"""
from html import escape
from pathlib import Path

from content import (BIO, CHORUS, CONCERTS, EDUCATION, EMAIL, GALLERY, LEAD, MASTERCLASSES, NEWS,
                     PHONE, PHONE_HREF, PHOTOS, ROLES, SHOW_NEWS, TEACHERS, UI, VIDEOS)

ROOT = Path(__file__).resolve().parent
LANGS = ["sv", "fi"]
PAGES = ["index", "bio", "media", "cv"]

PALETTES = {
    "elfenben": {"sv": "Elfenben", "fi": "Norsunluu"},
    "petrol": {"sv": "Pärlgrå och petrol", "fi": "Helmenharmaa ja petroli"},
    "bordeaux": {"sv": "Rosé och bordeaux", "fi": "Roosa ja viininpunainen"},
    "skog": {"sv": "Linne och skogsgrön", "fi": "Pellava ja metsänvihreä"},
    "natt": {"sv": "Nattblå", "fi": "Yönsininen"},
}
FONTS = {
    "cormorant": "Cormorant + Source Serif",
    "playfair": "Playfair + Source Sans",
    "caslon": "Libre Caslon + Libre Franklin",
    "marcellus": "Marcellus + EB Garamond",
}
FONT_URL = ("https://fonts.googleapis.com/css2?"
            "family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500"
            "&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400"
            "&family=Playfair+Display:ital,wght@0,500;0,600;1,500"
            "&family=Source+Sans+3:ital,wght@0,400;0,600;1,400"
            "&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400"
            "&family=Libre+Franklin:ital,wght@0,400;0,600;1,400"
            "&family=Marcellus"
            "&family=EB+Garamond:ital,wght@0,400;0,600;1,400"
            "&display=swap")

IMG = "../shared/img/"


def img(key, lang, loading="lazy"):
    p = PHOTOS[key]
    return (f'<img src="{IMG}{key}.jpg" width="{p["w"]}" height="{p["h"]}" '
            f'alt="{escape(p["alt"][lang])}" loading="{loading}" decoding="async">')


def mockup_bar(lang, page):
    t = UI[lang]["bar"]
    palettes = "".join(f'<option value="{k}">{v[lang]}</option>' for k, v in PALETTES.items())
    fonts = "".join(f'<option value="{k}">{v}</option>' for k, v in FONTS.items())
    news = (f'<label class="bar-check"><input type="checkbox" data-mock="news"> {t["news"]}</label>'
            if page == "index" else "")
    return f"""<div class="mockup-bar no-print" role="group" aria-label="{t["label"]}">
  <a href="../index.html">{t["label"]}</a>
  <label>{t["palette"]} <select data-mock="palette">{palettes}</select></label>
  <label>{t["font"]} <select data-mock="font">{fonts}</select></label>
  {news}
</div>"""


def header(lang, page):
    t = UI[lang]
    links = "".join(
        f'<a href="{p}.html"{" aria-current=page" if p == page else ""}>{t["nav"][p]}</a>' for p in PAGES)
    langs = "".join(
        f'<a href="../{code}/{page}.html" lang="{code}" hreflang="{code}"'
        f'{" aria-current=true" if code == lang else ""}>{UI[code]["lang_name"]}</a>' for code in LANGS)
    return f"""<header class="site-header">
  <nav class="lang-nav" aria-label="{t["lang_label"]}">{langs}</nav>
  <a class="brand" href="index.html"><span class="brand-name">Joel Forsström</span> <span class="brand-voice">{t["voice"]}</span></a>
  <nav class="main-nav" aria-label="{t["nav"]["index"]}">{links}</nav>
</header>"""


def footer(lang):
    t = UI[lang]
    return f"""<footer class="site-footer">
  <section class="contact" id="kontakt">
    <h2>{t["contact"]}</h2>
    <p class="contact-lead">{t["contact_lead"]}</p>
    <p class="contact-links"><a href="mailto:{EMAIL}">{EMAIL}</a> <a href="tel:{PHONE_HREF}">{PHONE}</a></p>
  </section>
  <p class="footer-meta"><a href="../shared/cv-{lang}.pdf" download>{t["download_cv"]}</a></p>
</footer>"""


def video(v, lang):
    return f"""<figure class="video">
  <button class="video-facade" type="button" data-id="{v["id"]}" aria-label="{UI[lang]["play"]}: {escape(v["title"][lang])}">
    <img src="{IMG}video/{v["id"]}.jpg" alt="" loading="lazy" width="1280" height="720">
    <span class="video-play" aria-hidden="true"></span>
  </button>
  <figcaption><strong>{escape(v["title"][lang])}</strong> <span>{escape(v["sub"][lang])}</span></figcaption>
</figure>"""


def page_index(lang):
    t = UI[lang]
    news = "".join(f"""<li class="news-item"><p class="news-when">{n["when"][lang]}</p>
      <h3>{n["title"][lang]}</h3><p>{n["text"][lang]}</p></li>""" for n in NEWS)
    return f"""<section class="hero">
  <div class="hero-media">{img("portratt-2021", lang, loading="eager")}</div>
  <div class="hero-text">
    <p class="eyebrow">{t["voice"]}</p>
    <h1>Joel Forsström</h1>
    <p class="lead">{LEAD[lang]}</p>
    <p class="actions"><a class="btn" href="bio.html">{t["read_bio"]}</a> <a class="btn btn--ghost" href="cv.html">{t["see_cv"]}</a></p>
  </div>
</section>
<section class="news"{"" if SHOW_NEWS else " hidden"}>
  <h2>{t["news"]}</h2>
  <ul class="news-list">{news}</ul>
</section>
<section class="featured">
  <div class="featured-text">
    <h2>{t["featured"]}</h2>
    <p>{BIO[lang][2]}</p>
    <p><a class="more" href="media.html">{t["all_media"]} →</a></p>
  </div>
  {video(VIDEOS[0], lang)}
</section>
<section class="strip" aria-label="{t["photos"]}">
  {"".join(f'<a href="media.html#bilder">{img(k, lang, loading="eager")}</a>' for k in ["monostatos-aland", "karmelitsystrarna", "tamino-flojt"])}
</section>"""


def page_bio(lang):
    t = UI[lang]
    fig = lambda k: f'<figure>{img(k, lang)}<figcaption>{PHOTOS[k]["cap"][lang]}</figcaption></figure>'
    p = [f"<p>{x}</p>" for x in BIO[lang]]
    return f"""<section class="page-head">
  <h1>{t["titles"]["bio"]}</h1>
</section>
<section class="bio prose">
  {p[0]}{p[1]}
  <div class="figure-pair">{fig("tamino-flojt")}{fig("peruk")}</div>
  {p[2]}{p[3]}
  <div class="figure-wide">{fig("karmelitsystrarna")}</div>
  {p[4]}{p[5]}
</section>"""


def page_media(lang):
    t = UI[lang]
    gallery = "".join(
        f'<a class="gallery-item" href="{IMG}{k}.jpg" data-pswp-width="{PHOTOS[k]["w"]}" data-pswp-height="{PHOTOS[k]["h"]}" '
        f'data-cropped="true" data-caption="{escape(PHOTOS[k]["cap"][lang])}" style="--pos: {PHOTOS[k]["pos"]}">{img(k, lang)}</a>'
        for k in GALLERY)
    return f"""<section class="page-head">
  <h1>{t["titles"]["media"]}</h1>
</section>
<section class="band band--videos" id="video">
  <h2>{t["videos"]}</h2>
  <div class="video-grid">{"".join(video(v, lang) for v in VIDEOS)}</div>
</section>
<section class="band band--photos" id="bilder">
  <h2>{t["photos"]}</h2>
  <div class="gallery-grid">{gallery}</div>
  <p class="note">{t["photo_credit_note"]}</p>
</section>"""


def credits(lang, director, conductor):
    t = UI[lang]
    parts = []
    if director:
        parts.append(f'{t["director"]}: {director}')
    if conductor:
        parts.append(f'{t["conductor"]}: {conductor}')
    return f'<span class="cv-credits">{" · ".join(parts)}</span>' if parts else ""


def page_cv(lang):
    t = UI[lang]
    h = t["cv_headers"]
    c = t["cols"]
    roles = "".join(f"""<tr><td class="cv-year">{y}</td><td class="cv-role">{r[lang]}</td>
      <td class="cv-work"><em>{w[lang]}</em>{f' <span class="cv-composer">{comp}</span>' if comp else ''}</td>
      <td class="cv-venue">{v[lang]}{credits(lang, d, cond)}</td></tr>""" for y, r, w, comp, v, d, cond in ROLES)
    chorus = "".join(f'<tr><td class="cv-year">{y}</td><td>{t["voice"].capitalize()}</td><td>{house[lang]}</td></tr>'
                     for y, house in CHORUS)
    concerts = "".join(f"""<tr><td class="cv-year">{y}</td>
      <td class="cv-work"><em>{w[lang]}</em> <span class="cv-composer">{comp}</span></td>
      <td class="cv-venue">{v[lang]}{credits(lang, "", cond)}</td></tr>""" for y, w, comp, v, cond in CONCERTS)
    edu = "".join(f'<li><span class="cv-year">{y}</span> <span><strong>{what[lang]}</strong>, {where}</span></li>' for y, what, where in EDUCATION)
    mc = "".join(f'<li><span class="cv-year">{y}</span> <span><strong>{who}</strong>, {where[lang]}</span></li>' for y, who, where in MASTERCLASSES)
    return f"""<section class="page-head cv-head">
  <p class="print-only print-name">Joel Forsström, {t["voice"]}</p>
  <h1>{t["titles"]["cv"]}</h1>
  <p class="print-only">{EMAIL} · {PHONE}</p>
  <p class="actions no-print"><a class="btn" href="../shared/cv-{lang}.pdf" download>{t["download_cv"]}</a></p>
</section>
<section class="cv">
  <h2>{h["roles"]}</h2>
  <table class="cv-table cv-table--roles">
    <thead><tr><th>{c["year"]}</th><th>{c["role"]}</th><th>{c["work"]}</th><th>{c["venue"]}</th></tr></thead>
    <tbody>{roles}</tbody>
  </table>
  <h2>{h["concert"]}</h2>
  <table class="cv-table cv-table--concerts">
    <thead><tr><th>{c["year"]}</th><th>{c["work"]}</th><th>{c["venue"]}</th></tr></thead>
    <tbody>{concerts}</tbody>
  </table>
  <h2>{h["chorus"]}</h2>
  <table class="cv-table cv-table--chorus">
    <thead><tr><th>{c["year"]}</th><th>{c["voice"]}</th><th>{c["house"]}</th></tr></thead>
    <tbody>{chorus}</tbody>
  </table>
  <div class="cv-cols">
    <div><h2>{h["education"]}</h2><ul class="cv-list">{edu}</ul>
      <p class="cv-teachers"><strong>{h["teachers"]}:</strong> {TEACHERS}</p></div>
    <div><h2>{h["masterclasses"]}</h2><ul class="cv-list">{mc}</ul></div>
  </div>
</section>"""


RENDER = {"index": page_index, "bio": page_bio, "media": page_media, "cv": page_cv}


def document(lang, page):
    t = UI[lang]
    title = t["titles"]["index"] if page == "index" else f'{t["titles"][page]} – Joel Forsström'
    pswp_css = '<link rel="stylesheet" href="../shared/vendor/photoswipe/photoswipe.css">\n' if page == "media" else ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{escape(title)}</title>
<meta name="description" content="{escape(LEAD[lang])}">
<script src="../shared/mockup.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONT_URL.replace("&", "&amp;")}">
{pswp_css}<link rel="stylesheet" href="../shared/site.css">
</head>
<body class="page-{page}">
{mockup_bar(lang, page)}
{header(lang, page)}
<main>
{RENDER[page](lang)}
</main>
{footer(lang)}
<script type="module" src="../shared/site.js"></script>
</body>
</html>
"""


def overview():
    palettes = "".join(f"""<li><a class="swatch" data-palette="{k}" href="sv/index.html?palette={k}">
      <span class="chips"><i style="background: var(--bg)"></i><i style="background: var(--surface)"></i><i style="background: var(--accent)"></i><i style="background: var(--deep)"></i></span>
      <span>{v["sv"]}</span></a></li>""" for k, v in PALETTES.items())
    fonts = "".join(f"""<li><a class="swatch" data-font="{k}" href="sv/index.html?font={k}">
      <span class="sample">Joel Forsström</span><span class="sample-body">{v}</span></a></li>""" for k, v in FONTS.items())
    return f"""<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Joel Forsström – designförslag</title>
<link rel="stylesheet" href="{FONT_URL.replace("&", "&amp;")}">
<link rel="stylesheet" href="shared/site.css">
</head>
<body class="page-overview">
<main>
<section class="page-head">
  <h1>Joel Forsström</h1>
  <p class="lead">Designförslag: klassisk stil med fem färgskalor och fyra typsnittspar. Välj kombination i listorna högst upp på varje sida.</p>
  <p class="actions"><a class="btn" href="sv/index.html">Svenska</a> <a class="btn btn--ghost" href="fi/index.html">Suomi</a></p>
</section>
<section class="overview">
  <h2>Färgskalor</h2>
  <ul class="swatches">{palettes}</ul>
  <h2>Typsnitt</h2>
  <ul class="swatches">{fonts}</ul>
  <p class="note">Detta är skisser. Bildtexterna är gissningar som Joel bör kontrollera.</p>
</section>
</main>
</body>
</html>
"""


def main():
    for lang in LANGS:
        out = ROOT / lang
        out.mkdir(parents=True, exist_ok=True)
        for page in PAGES:
            (out / f"{page}.html").write_text(document(lang, page), encoding="utf-8")
    (ROOT / "index.html").write_text(overview(), encoding="utf-8")
    print("built", len(LANGS) * len(PAGES) + 1, "pages")


if __name__ == "__main__":
    main()
