#!/usr/bin/env python3
"""Generates the mockup pages: mockups/{a,b,c}/{sv,fi}/{index,bio,media,cv}.html.

Run from anywhere: python3 mockups/build.py
"""
from html import escape
from pathlib import Path

from content import (BIO, CHORUS, CONCERTS, EDUCATION, EMAIL, GALLERY, LEAD, MASTERCLASSES, NEWS,
                     PHONE, PHONE_HREF, PHOTOS, ROLES, TEACHERS, UI, VIDEOS)

ROOT = Path(__file__).resolve().parent
LANGS = ["sv", "fi"]
PAGES = ["index", "bio", "media", "cv"]

STYLES = {
    "a": {
        "name": {"sv": "A · Klassisk", "fi": "A · Klassinen"},
        "fonts": "family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400",
        "hero": "portratt-2021",
        "bio_photos": ["tamino-flojt", "karmelitsystrarna"],
    },
    "b": {
        "name": {"sv": "B · Scen", "fi": "B · Näyttämö"},
        "fonts": "family=Bodoni+Moda:ital,opsz,wght@0,6..96,500;1,6..96,500&family=Jost:wght@300;400;500",
        "hero": "tamino-aria",
        "bio_photos": ["monostatos-aland", "nemorino-3"],
    },
    "c": {
        "name": {"sv": "C · Modern", "fi": "C · Moderni"},
        "fonts": "family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;500;600",
        "hero": "nemorino-3",
        "bio_photos": ["portratt-2021", "karmelitsystrarna"],
    },
}

IMG = "../../shared/img/"


def img(key, lang, cls="", loading="lazy", sizes=None):
    p = PHOTOS[key]
    attrs = f' class="{cls}"' if cls else ""
    return (f'<img{attrs} src="{IMG}{key}.jpg" width="{p["w"]}" height="{p["h"]}" '
            f'alt="{escape(p["alt"][lang])}" loading="{loading}" decoding="async">')


def header(style, lang, page):
    t = UI[lang]
    other = "fi" if lang == "sv" else "sv"
    links = "".join(
        f'<a href="{p}.html"{" aria-current=page" if p == page else ""}>{t["nav"][p]}</a>' for p in PAGES)
    switch = " ".join(
        f'<a href="../../{s}/{lang}/{page}.html"{" aria-current=true" if s == style else ""}>{STYLES[s]["name"][lang]}</a>'
        for s in STYLES)
    return f"""<div class="mockup-bar" role="note"><span>Mockup</span> {switch} <a href="../../index.html">↩</a></div>
<header class="site-header">
  <a class="brand" href="index.html"><span class="brand-name">Joel Forsström</span> <span class="brand-voice">{t["voice"]}</span></a>
  <nav class="main-nav" aria-label="{t["nav"]["index"]}">{links}</nav>
  <nav class="lang-nav" aria-label="Språk / Kieli">
    <a href="../sv/{page}.html" lang="sv"{" aria-current=true" if lang == "sv" else ""}>Svenska</a>
    <a href="../fi/{page}.html" lang="fi"{" aria-current=true" if lang == "fi" else ""}>Suomi</a>
  </nav>
</header>"""


def contact_block(lang):
    t = UI[lang]
    return f"""<section class="contact" id="kontakt">
  <h2>{t["contact"]}</h2>
  <p class="contact-lead">{t["contact_lead"]}</p>
  <p class="contact-links"><a href="mailto:{EMAIL}">{EMAIL}</a> <a href="tel:{PHONE_HREF}">{PHONE}</a></p>
</section>"""


def footer(lang):
    t = UI[lang]
    return f"""<footer class="site-footer">
  {contact_block(lang)}
  <p class="footer-meta">© Joel Forsström · <a href="../../shared/cv-{lang}.pdf" download>{t["download_cv"]}</a></p>
</footer>"""


def video(v, lang, big=False):
    return f"""<figure class="video{' video--big' if big else ''}">
  <button class="video-facade" type="button" data-id="{v["id"]}" aria-label="{UI[lang]["play"]}: {escape(v["title"][lang])}">
    <img src="https://i.ytimg.com/vi/{v["id"]}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">
    <span class="video-play" aria-hidden="true"></span>
  </button>
  <figcaption><strong>{escape(v["title"][lang])}</strong> <span>{escape(v["sub"][lang])}</span></figcaption>
</figure>"""


def page_index(style, lang):
    t = UI[lang]
    s = STYLES[style]
    news = "".join(f"""<li class="news-item"><p class="news-when">{n["when"][lang]}</p>
      <h3>{n["title"][lang]}</h3><p>{n["text"][lang]}</p></li>""" for n in NEWS)
    return f"""<section class="hero">
  <div class="hero-media">{img(s["hero"], lang, loading="eager")}</div>
  <div class="hero-text">
    <p class="eyebrow">{t["voice"]}</p>
    <h1>Joel Forsström</h1>
    <p class="lead">{LEAD[lang]}</p>
    <p class="actions"><a class="btn" href="bio.html">{t["read_bio"]}</a> <a class="btn btn--ghost" href="cv.html">{t["see_cv"]}</a></p>
  </div>
</section>
<section class="news">
  <h2>{t["news"]}</h2>
  <ul class="news-list">{news}</ul>
</section>
<section class="featured">
  <div class="featured-text">
    <h2>{t["featured"]}</h2>
    <p>{BIO[lang][2]}</p>
    <p><a class="more" href="media.html">{t["all_media"]} →</a></p>
  </div>
  {video(VIDEOS[0], lang, big=True)}
</section>
<section class="strip" aria-label="{t["photos"]}">
  {"".join(f'<a href="media.html#bilder">{img(k, lang, loading="eager")}</a>' for k in ["monostatos-aland", "karmelitsystrarna", "tamino-flojt"])}
</section>"""


def page_bio(style, lang):
    t = UI[lang]
    p1, p2 = STYLES[style]["bio_photos"]
    paras = BIO[lang]
    fig = lambda k: f'<figure class="bio-figure">{img(k, lang)}<figcaption>{PHOTOS[k]["cap"][lang]}</figcaption></figure>'
    body = "".join(f"<p>{p}</p>" for p in paras[:3]) + fig(p2) + "".join(f"<p>{p}</p>" for p in paras[3:])
    return f"""<section class="page-head">
  <p class="eyebrow">Joel Forsström · {t["voice"]}</p>
  <h1>{t["titles"]["bio"]}</h1>
</section>
<section class="bio">
  <div class="bio-aside">{fig(p1)}</div>
  <div class="bio-text prose">{body}</div>
</section>"""


def page_media(style, lang):
    t = UI[lang]
    videos = video(VIDEOS[0], lang, big=True) + "".join(video(v, lang) for v in VIDEOS[1:])
    gallery = "".join(
        f'<figure class="gallery-item"><a href="{IMG}{k}.jpg" data-lightbox>{img(k, lang)}</a>'
        f'<figcaption>{PHOTOS[k]["cap"][lang]}</figcaption></figure>' for k in GALLERY)
    return f"""<section class="page-head">
  <p class="eyebrow">Joel Forsström · {t["voice"]}</p>
  <h1>{t["titles"]["media"]}</h1>
</section>
<section class="videos" id="video">
  <h2>{t["videos"]}</h2>
  <div class="video-grid">{videos}</div>
</section>
<section class="gallery" id="bilder">
  <h2>{t["photos"]}</h2>
  <div class="gallery-grid">{gallery}</div>
  <p class="note">{t["photo_credit_note"]}</p>
</section>
<dialog class="lightbox"><form method="dialog"><button aria-label="×">×</button></form><img alt=""><p></p></dialog>"""


def credits(lang, director, conductor):
    t = UI[lang]
    parts = []
    if director:
        parts.append(f'{t["director"]}: {director}')
    if conductor:
        parts.append(f'{t["conductor"]}: {conductor}')
    return f'<span class="cv-credits">{" · ".join(parts)}</span>' if parts else ""


def page_cv(style, lang):
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
    edu = "".join(f'<li><span class="cv-year">{y}</span> <strong>{what[lang]}</strong>, {where}</li>' for y, what, where in EDUCATION)
    mc = "".join(f'<li><span class="cv-year">{y}</span> <strong>{who}</strong>, {where[lang]}</li>' for y, who, where in MASTERCLASSES)
    return f"""<section class="page-head cv-head">
  <p class="eyebrow">Joel Forsström · {t["voice"]}</p>
  <h1>{t["titles"]["cv"]}</h1>
  <p class="print-only">{EMAIL} · {PHONE}</p>
  <p class="actions no-print"><a class="btn" href="../../shared/cv-{lang}.pdf" download>{t["download_cv"]}</a>
    <button class="btn btn--ghost" type="button" onclick="window.print()">{t["print_cv"]}</button></p>
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


def document(style, lang, page):
    t = UI[lang]
    title = t["titles"]["index"] if page == "index" else f'{t["titles"][page]} – Joel Forsström'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{escape(title)}</title>
<meta name="description" content="{escape(LEAD[lang])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{STYLES[style]["fonts"]}&display=swap">
<link rel="stylesheet" href="../../shared/base.css">
<link rel="stylesheet" href="../style.css">
</head>
<body class="page-{page}">
{header(style, lang, page)}
<main>
{RENDER[page](style, lang)}
</main>
{footer(lang)}
<script src="../../shared/site.js" defer></script>
</body>
</html>
"""


def main():
    for style in STYLES:
        for lang in LANGS:
            out = ROOT / style / lang
            out.mkdir(parents=True, exist_ok=True)
            for page in PAGES:
                (out / f"{page}.html").write_text(document(style, lang, page), encoding="utf-8")
    print("built", len(STYLES) * len(LANGS) * len(PAGES), "pages")


if __name__ == "__main__":
    main()
