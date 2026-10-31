/* Journey page: the plane follows your scroll along the path, stages fade in, the sky gets deeper, clouds drift. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var path = document.getElementById('path');
  var fill = document.getElementById('fill');
  var plane = document.getElementById('plane');
  var stages = [].slice.call(document.querySelectorAll('.stage'));
  var clouds = [].slice.call(document.querySelectorAll('.cloud'));
  var root = document.documentElement;

  function mix(a, b, t) {
    var out = '#';
    for (var i = 0; i < 3; i++) {
      var x = parseInt(a.substr(1 + i * 2, 2), 16), y = parseInt(b.substr(1 + i * 2, 2), 16);
      var v = Math.round(x + (y - x) * t).toString(16);
      out += v.length < 2 ? '0' + v : v;
    }
    return out;
  }

  // stages fade in when they come into view
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('seen'); io.unobserve(e.target); } });
    }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });
    stages.forEach(function (s) { io.observe(s); });
  } else {
    stages.forEach(function (s) { s.classList.add('seen'); });
  }

  var ticking = false;
  function update() {
    ticking = false;
    var y = window.scrollY, vh = window.innerHeight;
    var rect = path.getBoundingClientRect();
    var top = rect.top + y, h = path.offsetHeight;

    // the plane sits a little below the middle of the screen and follows the scroll
    var pos = Math.max(0, Math.min(h, y + vh * 0.55 - top));
    fill.style.height = pos + 'px';
    plane.style.top = pos + 'px';

    stages.forEach(function (s) {
      var n = s.querySelector('.node');
      var ny = n.getBoundingClientRect().top + y - top + 11;
      s.classList.toggle('reached', pos >= ny);
    });

    // sky: deeper blue as you go up the page
    var max = Math.max(1, document.documentElement.scrollHeight - vh);
    var p = Math.max(0, Math.min(1, y / max));
    root.style.setProperty('--top', mix('#8fc3ea', '#4f95d0', p));
    root.style.setProperty('--bot', mix('#dcedfa', '#a9d2f0', p));

    if (!reduce) {
      var span = vh + 260;
      clouds.forEach(function (c) {
        var sp = parseFloat(c.getAttribute('data-speed')) || 0.1;
        var base = (parseFloat(c.getAttribute('data-top')) || 0) * vh;
        var yy = base - y * sp * 3;
        yy = ((yy + 130) % span + span) % span - 130;   // wrap, so a cloud that leaves at the top comes back from the bottom
        c.style.transform = 'translate3d(0,' + yy.toFixed(1) + 'px,0)';
      });
    }
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  update();
})();
