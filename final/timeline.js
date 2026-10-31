/* Journey page script. Built for smooth scrolling:
   - positions are measured once (and again on resize), never inside the scroll handler
   - the scroll handler only writes transform and opacity, once per frame
   - stages fade in with IntersectionObserver */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var path = document.getElementById('path');
  var fill = document.getElementById('fill');
  var plane = document.getElementById('plane');
  var deep = document.getElementById('deep');
  var stages = [].slice.call(document.querySelectorAll('.stage'));
  var clouds = [].slice.call(document.querySelectorAll('.cloud'));

  var pathTop = 0, pathH = 0, nodeY = [], vh = 0, docMax = 1;
  var reachedCount = -1, ticking = false;

  function measure() {
    vh = window.innerHeight;
    var r = path.getBoundingClientRect();
    pathTop = r.top + window.scrollY;
    pathH = path.offsetHeight;
    nodeY = stages.map(function (s) {
      var n = s.querySelector('.node').getBoundingClientRect();
      return n.top + window.scrollY - pathTop + n.height / 2;
    });
    docMax = Math.max(1, document.documentElement.scrollHeight - vh);
    fill.style.height = '100%';
  }

  // stages fade in as they come into view
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('seen'); io.unobserve(e.target); } });
    }, { threshold: 0, rootMargin: '0px 0px 25% 0px' });
    stages.forEach(function (s) { io.observe(s); });
  } else {
    stages.forEach(function (s) { s.classList.add('seen'); });
  }

  function update() {
    ticking = false;
    var y = window.scrollY;

    // the plane sits a little below the middle of the screen and follows the scroll
    var pos = Math.max(0, Math.min(pathH, y + vh * 0.55 - pathTop));
    fill.style.transform = 'scaleY(' + (pathH ? pos / pathH : 0).toFixed(4) + ')';
    plane.style.transform = 'translate3d(0,' + pos.toFixed(1) + 'px,0)';

    // how many stages the plane has passed
    var count = 0;
    for (var i = 0; i < nodeY.length; i++) { if (pos >= nodeY[i]) count = i + 1; else break; }
    if (count !== reachedCount) {
      reachedCount = count;
      stages.forEach(function (s, k) { s.classList.toggle('reached', k < count); });
    }

    // the sky gets deeper as you scroll: opacity only
    deep.style.opacity = Math.min(1, y / docMax).toFixed(3);

    if (!reduce) {
      var span = vh + 260;
      for (var c = 0; c < clouds.length; c++) {
        var el = clouds[c];
        var yy = el._base - y * el._sp;
        yy = ((yy + 130) % span + span) % span - 130;   // a cloud that leaves at the top returns from the bottom
        el.style.transform = 'translate3d(' + el._x + 'px,' + yy.toFixed(1) + 'px,0)';
      }
    }
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }

  function place() {
    measure();
    clouds.forEach(function (el) {
      el._sp = (parseFloat(el.getAttribute('data-speed')) || 0.1) * 3;
      el._base = (parseFloat(el.getAttribute('data-top')) || 0) * vh;
      el._x = (parseFloat(el.getAttribute('data-left')) || 0) * window.innerWidth;
    });
    update();
  }

  var rt;
  window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(place, 120); });
  window.addEventListener('load', place);
  window.addEventListener('scroll', onScroll, { passive: true });
  place();
})();
