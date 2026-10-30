# joelforsstrom.com

Website of tenor Joel Forsström, in Swedish and Finnish. It is a Jekyll site that GitHub Pages builds from `master`, so there is no build step to run and no workflow to maintain: pushing to `master` publishes it.

## Where things are

- `_data/`: the content. `bio.yml`, `home.yml`, `news.yml`, `videos.yml`, `gallery.yml`, `cv.yml` and `settings.yml` hold the texts, each in both languages. `labels.yml` holds the fixed interface texts.
- `_data/settings.yml`: `show_news` turns the "Aktuellt" section on the home page on or off.
- `_layouts/`, `_includes/`: the templates.
- `assets/`: styles, script, fonts, images, the CV PDFs in `assets/cv/`, and PhotoSwipe 5.4.4 in `assets/vendor/`.
- `index.html`, `biografi.html`, `media.html`, `cv.html` and `fi/`: the pages. They only set a layout, language and address.

## Local build

Uses the same versions as GitHub Pages:

```sh
podman run --rm -v "$PWD":/src -v joel-gems:/usr/local/bundle -w /src -e LANG=C.UTF-8 \
  docker.io/library/ruby:3.3 sh -c 'bundle install && bundle exec jekyll build'
```

The result is in `_site/`.

## CV PDFs

`tools/print_cv.py` prints the CV pages of a locally served build to `assets/cv/`; see the top of that file. Update them whenever `_data/cv.yml` changes.

## Privacy

The site loads nothing from other servers until a visitor presses play on a video. Fonts, images and scripts are self-hosted, and a video thumbnail should be saved in `assets/images/video/` when a video is added.
