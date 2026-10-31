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
})();
