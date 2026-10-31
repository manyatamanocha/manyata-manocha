(function () {
  var about = document.getElementById('about'); if (!about) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // corner pictures slide in once
  var pics = about.querySelectorAll('.ab-pic');
  if (window.IntersectionObserver) {
    var seen = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.remove('waiting'); seen.unobserve(e.target); }
      });
    }, { rootMargin: '50px', threshold: 0 });
    pics.forEach(function (p) { p.classList.add('waiting'); seen.observe(p); });
  }

  // split the text into letters; a hidden plain copy stays for screen readers
  var text = document.getElementById('about-text'); if (!text) return;
  var sr = document.createElement('span'); sr.className = 'ab-sr'; sr.textContent = text.textContent;
  var shown = document.createElement('span'); shown.setAttribute('aria-hidden', 'true');
  var chars = [];
  Array.prototype.slice.call(text.childNodes).forEach(function (node) {
    if (node.nodeName === 'BR') { shown.appendChild(document.createElement('br')); return; }
    node.textContent.split(/( +)/).forEach(function (part) {
      if (!part) return;
      if (!part.trim()) { shown.appendChild(document.createTextNode(' ')); return; }
      var word = document.createElement('span'); word.className = 'w';
      part.split('').forEach(function (c) {
        var s = document.createElement('span'); s.textContent = c; s.style.opacity = '.2';
        word.appendChild(s); chars.push(s);
      });
      shown.appendChild(word);
    });
  });
  text.textContent = '';
  text.appendChild(sr); text.appendChild(shown);

  var ticking = false;
  function update() {
    ticking = false;
    var box = text.getBoundingClientRect(), vh = window.innerHeight;
    // starts when the text's top reaches 80% of the screen, ends when its bottom reaches 20%
    var progress = (vh * 0.8 - box.top) / (box.height + vh * 0.6);
    chars.forEach(function (c, i) {
      var t = Math.min(1, Math.max(0, progress * chars.length - i));
      c.style.opacity = (0.2 + 0.8 * t).toFixed(2);
    });
  }
  function request() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }
  window.addEventListener('scroll', request, { passive: true });
  window.addEventListener('resize', request);
  update();
})();
