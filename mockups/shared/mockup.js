// Mockup controls only: palette, font and the "Aktuellt" switch. Not part of the final site.
// Runs in <head> so the chosen palette is set before the first paint.
(function () {
  var root = document.documentElement;
  var query = new URLSearchParams(location.search);
  var defaults = { palette: 'elfenben', font: 'cormorant', news: '0' };

  function read(key) {
    try { return localStorage.getItem('jf-' + key); } catch (e) { return null; }
  }
  function write(key, value) {
    try { localStorage.setItem('jf-' + key, value); } catch (e) { /* the choice just won't persist */ }
  }

  var state = {};
  Object.keys(defaults).forEach(function (key) {
    state[key] = query.get(key) || read(key) || defaults[key];
    if (query.get(key)) write(key, state[key]);
  });
  root.dataset.palette = state.palette;
  root.dataset.font = state.font;

  function shareableUrl() {
    var params = new URLSearchParams();
    Object.keys(state).forEach(function (key) {
      if (state[key] !== defaults[key]) params.set(key, state[key]);
    });
    var search = params.toString();
    history.replaceState(null, '', location.pathname + (search ? '?' + search : '') + location.hash);
  }

  function applyNews() {
    var news = document.querySelector('.news');
    if (news) news.hidden = state.news !== '1';
  }

  document.addEventListener('DOMContentLoaded', function () {
    applyNews();
    document.querySelectorAll('[data-mock]').forEach(function (control) {
      var key = control.dataset.mock;
      if (control.type === 'checkbox') control.checked = state[key] === '1';
      else control.value = state[key];
      control.addEventListener('change', function () {
        state[key] = control.type === 'checkbox' ? (control.checked ? '1' : '0') : control.value;
        write(key, state[key]);
        if (key === 'news') applyNews();
        else root.dataset[key] = state[key];
        shareableUrl();
      });
    });
  });
})();
