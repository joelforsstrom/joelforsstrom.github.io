// Click-to-load YouTube (no cookies until the visitor presses play) and a small photo lightbox.
document.querySelectorAll('.video-facade').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube-nocookie.com/embed/' + btn.dataset.id + '?autoplay=1&rel=0';
    iframe.title = btn.getAttribute('aria-label');
    iframe.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
    iframe.allowFullscreen = true;
    btn.replaceWith(iframe);
  });
});

var box = document.querySelector('.lightbox');
if (box && box.showModal) {
  document.querySelectorAll('[data-lightbox]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      var img = link.querySelector('img');
      box.querySelector('img').src = link.href;
      box.querySelector('img').alt = img.alt;
      box.querySelector('p').textContent = link.parentElement.querySelector('figcaption').textContent;
      box.showModal();
    });
  });
  box.addEventListener('click', function (e) { if (e.target === box) box.close(); });
}
