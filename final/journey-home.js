/* My Journey to Product on the home page: the plane and the orange line follow the scroll, and each milestone fades in when it comes into view.
   Positions are measured when the page loads or resizes, never inside the scroll handler, which only writes transform and opacity once per frame. */
(function () {
  var sec = document.getElementById('journey'); if (!sec) return;
  var path = document.getElementById('jn-path'), fill = document.getElementById('jn-fill'), plane = document.getElementById('jn-plane');
  var stages = [].slice.call(sec.querySelectorAll('.jn-stage'));
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var vh = 0, pathH = 0, nodeY = [], reached = -1, ticking = false;

  sec.classList.add('jn-on');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('jn-seen'); io.unobserve(e.target); } });
    }, { threshold: 0, rootMargin: '0px 0px 25% 0px' });
    stages.forEach(function (s) { io.observe(s); });
  } else {
    stages.forEach(function (s) { s.classList.add('jn-seen'); });
  }

  function measure() {
    vh = window.innerHeight; pathH = path.offsetHeight;
    var top = path.getBoundingClientRect().top;
    nodeY = stages.map(function (s) { var r = s.querySelector('.jn-node').getBoundingClientRect(); return r.top - top + r.height / 2; });
  }
  function update() {
    ticking = false;
    var pathTop = path.getBoundingClientRect().top;   // the plane sits a little below the middle of the screen and follows the scroll
    var pos = Math.max(0, Math.min(pathH, vh * 0.55 - pathTop));
    fill.style.transform = 'scaleY(' + (pathH ? pos / pathH : 0).toFixed(4) + ')';
    plane.style.transform = 'translate3d(0,' + pos.toFixed(1) + 'px,0)';
    var count = 0;
    for (var i = 0; i < nodeY.length; i++) { if (pos >= nodeY[i]) count = i + 1; else break; }
    if (count !== reached) { reached = count; stages.forEach(function (s, k) { s.classList.toggle('jn-reached', k < count); }); }
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }
  function place() { measure(); update(); }

  var rt;
  window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(place, 120); });
  window.addEventListener('load', place);
  window.addEventListener('scroll', onScroll, { passive: true });
  place();
})();
