# joelforsstrom.com

Website of tenor Joel Forsström, in Swedish and Finnish. It is a Jekyll site that GitHub Pages builds from `master`, so there is no build step to run and no workflow to maintain: pushing to `master` publishes it.

## Where things are

- `_data/`: the content. `bio.yml`, `home.yml`, `news.yml`, `videos.yml`, `gallery.yml`, `cv.yml` and `settings.yml` hold the texts, each in both languages. `labels.yml` holds the fixed interface texts.
- `_data/news.yml`: `show` turns the "Aktuellt" section on the home page on or off.
- `_layouts/`, `_includes/`: the templates.
- `assets/`: styles, script, fonts, images, the CV PDFs in `assets/cv/`, and PhotoSwipe 5.4.4 in `assets/vendor/`.
- `index.html`, `biografi.html`, `media.html`, `cv.html` and `fi/`: the pages. They only set a layout, language and address.

## Editing

Joel edits the site at `/admin/` with Sveltia CMS; see `docs/redigera-webbplatsen.md`. Saving commits directly to `master`, and GitHub Pages republishes. `admin/config.yml` defines the editing forms, and the Sveltia version is pinned in `admin/index.html`, with an integrity hash that must be replaced together with the version.

Sign-in goes through [sveltia-cms-auth](https://github.com/sveltia/sveltia-cms-auth), a Cloudflare Worker that holds the GitHub OAuth app's secret:

1. In Cloudflare, deploy the Worker with the button in its README and copy its URL.
2. In GitHub, [create an OAuth app](https://github.com/settings/applications/new) with homepage `https://joelforsstrom.com` and callback URL `<worker URL>/callback`, and generate a client secret.
3. In the Worker's settings, add `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET` (encrypted) and `ALLOWED_DOMAINS` set to `joelforsstrom.com`, then deploy.
4. Set `base_url` to the Worker URL in `admin/config.yml`.

Only GitHub accounts with write access to this repository can save.

## Local build

Uses the same versions as GitHub Pages:

```sh
podman run --rm -v "$PWD":/src -v joel-gems:/usr/local/bundle -w /src -e LANG=C.UTF-8 \
  docker.io/library/ruby:3.3 sh -c 'bundle install && bundle exec jekyll build'
```

The result is in `_site/`.

## CV PDFs

`assets/cv/` holds Joel's own CV files. They are separate from `_data/cv.yml`, so replace them when the CV changes.

## Privacy

The site loads nothing from other servers until a visitor presses play on a video. Fonts, images and scripts are self-hosted, and a video thumbnail should be saved in `assets/images/video/` when a video is added.
