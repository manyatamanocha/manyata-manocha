/* The stationary hero controls visibility; the moving mascot must not observe itself. */
(function () {
  'use strict';
  const mascot = document.getElementById('peek');
  if (!mascot) return;
  const hero = mascot.closest('.sky-hero');
  const arm = mascot.querySelector('.peek-arm');
  const pictures = Array.from(mascot.querySelectorAll('img'));
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let ready = false, inView = false, started = false, busy = false;
  let active = null, revision = 0;
  function phase(value) { mascot.dataset.phase = value; }
  function canMove() { return !motion.matches && !document.hidden && inView; }
  function rest() {
    revision++;
    if (active) active.cancel();
    active = null;
    busy = false;
    mascot.classList.remove('preparing');
    phase('resting');
  }
  function run(target, keyframes, options, done) {
    const token = revision;
    active = target.animate(keyframes, options);
    active.onfinish = function () {
      if (token !== revision) return;
      active = null;
      done();
    };
  }
  function wave() {
    phase('waving');
    run(arm, [
      { transform: 'rotate(-18deg)', opacity: 0, offset: 0 },
      { transform: 'rotate(0deg)', opacity: 1, offset: .16 },
      { transform: 'rotate(7deg)', opacity: 1, offset: .29 },
      { transform: 'rotate(-7deg)', opacity: 1, offset: .42 },
      { transform: 'rotate(7deg)', opacity: 1, offset: .55 },
      { transform: 'rotate(-7deg)', opacity: 1, offset: .68 },
      { transform: 'rotate(0deg)', opacity: 1, offset: .82 },
      { transform: 'rotate(-18deg)', opacity: 0, offset: 1 }
    ], { duration: 2200, easing: 'ease-in-out' }, function () {
      busy = false;
      phase('resting');
    });
  }
  function greet() {
    if (!ready || busy || !canMove() || !mascot.animate || !arm.animate) return;
    busy = true;
    if (started) { wave(); return; }
    started = true;
    phase('entering');
    mascot.classList.remove('preparing');
    run(mascot, [ { transform: 'translateX(105%)' }, { transform: 'translateX(0)' } ],
      { duration: 700, easing: 'cubic-bezier(0.23, 1, 0.32, 1)' }, wave);
  }
  function sync() {
    if (motion.matches) { rest(); return; }
    if (active) {
      if (canMove()) active.play(); else active.pause();
    } else if (!started) greet();
  }
  function measure() {
    const box = hero.getBoundingClientRect();
    inView = box.bottom > 0 && box.top < window.innerHeight;
    sync();
  }
  phase('loading');
  if (!motion.matches && mascot.animate) mascot.classList.add('preparing');
  mascot.addEventListener('click', greet);
  document.addEventListener('visibilitychange', sync);
  window.addEventListener('pageshow', measure);
  motion.addEventListener('change', sync);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      inView = entries[0].isIntersecting;
      sync();
    }).observe(hero);
  } else {
    window.addEventListener('scroll', measure, { passive: true });
    window.addEventListener('resize', measure);
  }
  function loaded(img) {
    if (img.decode) return img.decode().catch(function () {
      if (!img.naturalWidth) throw new Error('Mascot image did not load');
    });
    return new Promise(function (resolve, reject) {
      if (img.complete) { img.naturalWidth ? resolve() : reject(); return; }
      img.addEventListener('load', resolve, { once: true });
      img.addEventListener('error', reject, { once: true });
    });
  }
  Promise.all(pictures.map(loaded)).then(function () {
    ready = true;
    phase('ready');
    measure();
  }).catch(rest);
})();
