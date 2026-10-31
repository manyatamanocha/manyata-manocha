(function () {
  var strip = document.getElementById('strip'); if (!strip) return;
  var track = document.getElementById('strip-track');
  // ratio is the screenshot's own width / height, so wide screenshots make wide cards and the phone screenshot makes a tall one
  var PROJECTS = [
    { href: 'project-pwc.html', title: 'Risk Screening Dashboard', cat: 'Product work at PwC', art: 'big', text: '67%', ratio: 1.6 },
    { href: 'project-adhikaar.html', title: 'Adhikaar', cat: 'Government · Banking', img: 'img/adhikaar.webp', ratio: 1400 / 875 },
    { href: 'project-vantage.html', title: 'Vantage', cat: 'Learning · AI', img: 'img/vantage.webp', ratio: 980 / 730 },
    { href: 'project-shravan.html', title: 'The Shravan\'s Round', cat: 'Interview practice · Voice AI', img: 'img/shravan.webp', ratio: 1400 / 800 },
    { href: 'project-hamsty.html', title: 'Hamsty', cat: 'Personal product · In build', img: 'img/hamsty.webp', ratio: 400 / 790 },
    { href: 'project-teammates.html', title: 'AI Teammates', cat: 'Hackathon · Payments', art: 'flow', text: 'Lead or failed payment → AI agent → person', ratio: 1.6 }
  ];
  var SPEED = 0.8, DECAY = 0.95, FRAME = 1000 / 60;   // px per 60 fps frame, so the speed is the same on 60 Hz and 120 Hz screens

  // two rounds of the same cards make the loop seamless; the second round is hidden from keyboards and screen readers
  [0, 1].forEach(function (round) {
    PROJECTS.forEach(function (p) {
      var a = document.createElement('a'); a.className = 'strip-card'; a.href = p.href; a.draggable = false;
      a.style.setProperty('--r', p.ratio);
      if (round) { a.tabIndex = -1; a.setAttribute('aria-hidden', 'true'); }
      if (p.img) { var im = new Image(); im.src = p.img; im.alt = ''; im.decoding = 'async'; im.draggable = false; a.appendChild(im); }
      else { var art = document.createElement('div'); art.className = 'strip-art ' + p.art; art.textContent = p.text; a.appendChild(art); }
      var cap = document.createElement('div'); cap.className = 'strip-cap';
      var b = document.createElement('b'); b.textContent = p.title;
      var s = document.createElement('span'); s.textContent = p.cat;
      cap.appendChild(b); cap.appendChild(s); a.appendChild(cap); track.appendChild(a);
    });
  });

  var cards = track.children, first = cards[0], twin = cards[PROJECTS.length];
  var period = 1, offset = 0, vel = 0, held = false, drag = null, swallowClick = false, last = null;
  var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function measure() { period = twin.offsetLeft - first.offsetLeft; }

  function frame(now) {
    if (last === null) last = now;
    var f = Math.min(3, (now - last) / FRAME); last = now;
    if (!drag) {
      if (Math.abs(vel) > 0.1) { offset += vel * f; vel *= Math.pow(DECAY, f); }
      else { vel = 0; if (!held && !still) offset -= SPEED * f; }
    }
    while (offset <= -period) offset += period;
    while (offset > 0) offset -= period;
    track.style.transform = 'translate3d(' + offset.toFixed(2) + 'px,0,0)';
    requestAnimationFrame(frame);
  }

  strip.addEventListener('pointerdown', function (e) {
    if (e.button) return;
    drag = { id: e.pointerId, x: e.clientX, moved: 0, time: performance.now() };
    vel = 0; swallowClick = false;
  });
  strip.addEventListener('pointermove', function (e) {
    if (!drag || e.pointerId !== drag.id) return;
    var dx = e.clientX - drag.x, stamp = performance.now();
    drag.moved += Math.abs(dx);
    // capture only once it is a real drag, so a plain click still opens the project
    if (drag.moved > 6 && !swallowClick) {
      swallowClick = true; strip.classList.add('dragging');
      try { strip.setPointerCapture(e.pointerId); } catch (err) {}
    }
    vel = dx / Math.max(1, stamp - drag.time) * 16;
    offset += dx;
    drag.x = e.clientX; drag.time = stamp;
  });
  function release() {
    if (drag && performance.now() - drag.time > 120) vel = 0;
    drag = null; strip.classList.remove('dragging');
  }
  strip.addEventListener('pointerup', release);
  strip.addEventListener('pointercancel', function () { vel = 0; release(); });
  strip.addEventListener('click', function (e) { if (swallowClick) { e.preventDefault(); e.stopPropagation(); swallowClick = false; } }, true);
  strip.addEventListener('dragstart', function (e) { e.preventDefault(); });
  // keyboard: hold the row still and bring the focused card into view
  strip.addEventListener('focusin', function (e) {
    if (!e.target.matches(':focus-visible')) return;   // a mouse press also focuses a link; only Tab should move the row
    held = true; vel = 0; strip.scrollLeft = 0;
    offset = -e.target.offsetLeft;
  });
  strip.addEventListener('focusout', function () { held = false; });

  measure();
  window.addEventListener('resize', measure);
  requestAnimationFrame(frame);
})();
