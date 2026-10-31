(function () {
  var mos = document.getElementById('mosaic'); if (!mos) return;
  // pic is the shape of the picture area: each screenshot's own width / height, so nothing is cropped
  var P = {
    pwc: { href: 'project-pwc.html', title: 'Risk Screening Dashboard', cat: 'Product work at PwC', art: 'big', text: '67%', pic: '8 / 5' },
    adhikaar: { href: 'project-adhikaar.html', title: 'Adhikaar', cat: 'Government · Banking', img: 'img/adhikaar.webp', pic: '1400 / 875' },
    vantage: { href: 'project-vantage.html', title: 'Vantage', cat: 'Learning · AI', img: 'img/vantage.webp', pic: '980 / 730' },
    shravan: { href: 'project-shravan.html', title: 'The Shravan\'s Round', cat: 'Interview practice · Voice AI', img: 'img/shravan.webp', pic: '1400 / 800' },
    hamsty: { href: 'project-hamsty.html', title: 'Hamsty', cat: 'Personal product · In build', img: 'img/hamsty.webp', pic: '4 / 5', tall: true },
    teammates: { href: 'project-teammates.html', title: 'AI Teammates', cat: 'Hackathon · Payments', art: 'flow', text: 'Lead or failed payment → AI agent → person', pic: '8 / 5' }
  };
  // every project is in the first two columns; the third only repeats them, so phones can drop it
  var COLUMNS = [
    { tiles: [['red', '5 / 3'], 'pwc', 'adhikaar', ['blue', '2 / 1'], 'hamsty'] },
    { up: true, delay: 5, tiles: [['yellow', '2 / 1'], 'vantage', ['dark', '5 / 3'], 'shravan', 'teammates'] },
    { extra: true, delay: 9, tiles: [['cream', '2 / 1'], 'adhikaar', ['yellow', '5 / 3'], 'teammates', ['red', '2 / 1']] }
  ];
  var SPEED = 97;   // px per second: one tile about every 2.9 seconds
  var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function solid(t) {
    var d = document.createElement('div');
    d.className = 'mos-tile solid ' + t[0]; d.style.setProperty('--a', t[1]); d.setAttribute('aria-hidden', 'true');
    return d;
  }
  function tile(p, hidden) {
    var a = document.createElement('a'); a.className = 'mos-tile'; a.href = p.href;
    if (hidden) { a.tabIndex = -1; a.setAttribute('aria-hidden', 'true'); }
    var box = document.createElement('div'); box.className = 'mos-pic' + (p.tall ? ' tall' : ''); box.style.setProperty('--p', p.pic);
    if (p.img) { var im = new Image(); im.src = p.img; im.alt = ''; im.decoding = 'async'; box.appendChild(im); }
    else { var art = document.createElement('div'); art.className = 'mos-art ' + p.art; art.textContent = p.text; box.appendChild(art); }
    var cap = document.createElement('div'); cap.className = 'mos-cap';
    var b = document.createElement('b'); b.textContent = p.title;
    var s = document.createElement('span'); s.textContent = p.cat;
    cap.appendChild(b); cap.appendChild(s); a.appendChild(box); a.appendChild(cap);
    return a;
  }

  var cols = COLUMNS.map(function (c) {
    var col = document.createElement('div');
    col.className = 'mos-col' + (c.up ? ' up' : '') + (c.extra ? ' extra' : '');
    if (c.delay) col.style.animationDelay = -c.delay + 's';
    [0, 1].forEach(function (round) {
      if (round && still) return;   // no motion means no loop, so no copies
      c.tiles.forEach(function (t) {
        col.appendChild(typeof t === 'string' ? tile(P[t], round || c.extra) : solid(t));
      });
    });
    mos.appendChild(col);
    return col;
  });

  function pace() {
    cols.forEach(function (col) { if (col.offsetHeight) col.style.setProperty('--dur', (col.offsetHeight / 2 / SPEED).toFixed(2) + 's'); });
  }
  pace();
  window.addEventListener('resize', pace);
  // tabbing to a clipped tile scrolls the box; put it back afterwards so the loop stays aligned
  mos.addEventListener('focusout', function () { mos.scrollTop = 0; });
})();
