// Click-to-load YouTube: nothing contacts YouTube until the visitor presses play.
document.querySelectorAll('.video-facade').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube-nocookie.com/embed/' + btn.dataset.id + '?autoplay=1&rel=0';
    iframe.title = btn.getAttribute('aria-label');
    iframe.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
    iframe.allowFullscreen = true;
    btn.replaceWith(iframe);
    iframe.focus();
  });
});

// Photo lightbox. Without JavaScript each thumbnail is a plain link to the full image.
var LABELS = {
  sv: { dialog: 'Bildvisning', close: 'Stäng', zoom: 'Zooma', prev: 'Föregående bild', next: 'Nästa bild', error: 'Bilden kunde inte laddas' },
  fi: { dialog: 'Kuvanäyttö', close: 'Sulje', zoom: 'Zoomaa', prev: 'Edellinen kuva', next: 'Seuraava kuva', error: 'Kuvaa ei voitu ladata' }
};

async function initGallery(gallery) {
  var { default: PhotoSwipeLightbox } = await import('../vendor/photoswipe/photoswipe-lightbox.esm.min.js');
  var t = LABELS[document.documentElement.lang] || LABELS.sv;
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var lightbox = new PhotoSwipeLightbox({
    gallery: gallery,
    children: 'a',
    pswpModule: function () { return import('../vendor/photoswipe/photoswipe.esm.min.js'); },
    bgOpacity: 0.94,
    showHideAnimationType: reducedMotion ? 'none' : 'zoom',
    closeTitle: t.close,
    zoomTitle: t.zoom,
    arrowPrevTitle: t.prev,
    arrowNextTitle: t.next,
    errorMsg: t.error
  });
  // Joel can swap photos in the CMS, so sizes come from the loaded thumbnail instead of the markup.
  lightbox.addFilter('domItemData', function (itemData, element, linkEl) {
    var img = linkEl.querySelector('img');
    itemData.width = img.naturalWidth || 1600;
    itemData.height = img.naturalHeight || 1200;
    return itemData;
  });
  lightbox.on('uiRegister', function () {
    lightbox.pswp.ui.registerElement({
      name: 'caption',
      order: 9,
      isButton: false,
      appendTo: 'root',
      onInit: function (el, pswp) {
        el.setAttribute('aria-live', 'polite');
        pswp.on('change', function () { el.textContent = pswp.currSlide.data.element.dataset.caption || ''; });
      }
    });
  });
  lightbox.on('afterInit', function () {
    lightbox.pswp.element.setAttribute('aria-label', t.dialog);
    lightbox.pswp.element.setAttribute('aria-modal', 'true');
  });
  lightbox.init();
}

var gallery = document.querySelector('.gallery-grid');
if (gallery) initGallery(gallery);
