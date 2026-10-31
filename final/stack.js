(function () {
  var stack = document.getElementById('stack'); if (!stack) return;
  // all words and numbers come from each project's own page
  var PROJECTS = [
    { href: 'project-pwc.html', title: 'Risk Screening Dashboard', cat: 'Product work at PwC', main: { big: '67%', note: 'less time per case' },
      stats: [['30 → 10 min', 'per case, end to end'], ['Up to 25', 'cases a week']] },
    { href: 'project-adhikaar.html', live: 'https://adhikaar-gamma.vercel.app', title: 'Adhikaar', cat: 'Government · Banking', main: { img: 'img/adhikaar.webp' },
      stats: [['₹17k → ₹1k', 'estimated cost, court route against simplified route'], ['7', 'interviews across 6 segments']] },
    { href: 'project-vantage.html', live: 'https://vantage-app-zeta.vercel.app', title: 'Vantage', cat: 'Learning · AI', main: { img: 'img/vantage.webp' },
      stats: [['88%', 'of testers finished a meaningful activity with no help (15 of 17)'], ['12 / 14', 'solutions rated helpful']] },
    { href: 'project-shravan.html', live: 'https://shravans-round.vercel.app', title: 'The Shravan\'s Round', cat: 'Interview practice · Voice AI', main: { img: 'img/shravan.webp' },
      stats: [['2nd', 'place, Rethink AI-First Buildathon'], ['20 min', 'one mock, answered out loud']] },
    { href: 'project-hamsty.html', live: 'https://hamsty.vercel.app', title: 'Hamsty', cat: 'Personal product · In build', main: { img: 'img/hamsty.webp', tall: true },
      stats: [['7 · 3 · 1', 'days before expiry when reminders go out'], ['1 / day', 'most reminders a person gets']] },
    { href: 'project-teammates.html', title: 'AI Teammates', cat: 'Hackathon · Payments', main: { flow: 'Lead or failed payment → AI agent → person' },
      stats: [['24.07 bn', 'UPI payments in September 2026 (NPCI)'], ['~0.8%', 'of UPI payments fail for technical reasons']] }
  ];
  var total = PROJECTS.length;
  var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text) n.textContent = text;
    return n;
  }
  function button(href, label, external) {
    var a = el('a', 'btn', label); a.href = href;
    if (external) { a.target = '_blank'; a.rel = 'noopener'; }
    return a;
  }
  function mainTile(m) {
    var box = el('div', 'stack-main');
    if (m.img) {
      var im = new Image(); im.src = m.img; im.alt = ''; im.loading = 'lazy'; im.decoding = 'async'; box.appendChild(im);
      if (m.tall) box.classList.add('tall');
    } else if (m.big) {
      box.classList.add('big'); box.appendChild(el('b', '', m.big)); box.appendChild(el('span', '', m.note));
    } else {
      box.classList.add('flow'); box.textContent = m.flow;
    }
    return box;
  }

  var cards = PROJECTS.map(function (p, i) {
    var slot = el('div', 'stack-slot'); slot.style.setProperty('--i', i);
    var card = el('article', 'stack-card');
    var head = el('div', 'stack-head');
    head.appendChild(el('span', 'stack-num', '0' + (i + 1)));
    var title = el('div', 'stack-title');
    title.appendChild(el('span', '', p.cat)); title.appendChild(el('h3', '', p.title));
    head.appendChild(title);
    var btns = el('div', 'stack-btns');
    btns.appendChild(button(p.href, 'View project'));
    if (p.live) btns.appendChild(button(p.live, 'Live site ↗', true));
    head.appendChild(btns);
    var grid = el('div', 'stack-grid');
    p.stats.forEach(function (s) {
      var stat = el('div', 'stack-stat');
      stat.appendChild(el('b', '', s[0])); stat.appendChild(el('span', '', s[1]));
      grid.appendChild(stat);
    });
    grid.appendChild(mainTile(p.main));
    card.appendChild(head); card.appendChild(grid);
    slot.appendChild(card); stack.appendChild(slot);
    return card;
  });
  if (still) return;

  var ticking = false;
  function update() {
    ticking = false;
    var box = stack.getBoundingClientRect();
    var travel = box.height - window.innerHeight;
    var progress = travel > 0 ? Math.min(1, Math.max(0, -box.top / travel)) : 0;
    cards.forEach(function (card, i) {
      var from = i / total, target = 1 - (total - 1 - i) * 0.03;
      var t = Math.min(1, Math.max(0, (progress - from) / (1 - from)));
      card.style.transform = 'scale(' + (1 + (target - 1) * t).toFixed(4) + ')';
    });
  }
  function request() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }
  window.addEventListener('scroll', request, { passive: true });
  window.addEventListener('resize', request);
  update();
})();
