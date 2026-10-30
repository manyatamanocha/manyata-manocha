# Builds the premium website (portfolio-web.html) and the resume page (resume.html).
# Run: python3 build_web.py   — then publish portfolio-web.html with the img/ files and resume.html.
# Facts here match portfolio.html (the PDF source). Never add the phone number.
import html as _h
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
E = _h.escape

EMAIL = 'manyata126@gmail.com'
LINKEDIN = 'https://www.linkedin.com/in/manyata-manocha/'
HERO_IMG = 'img/portrait.jpg'          # balcony photo, cut out, head to knees
OFFLINE_IMGS = []
# PRD links: put a public URL (for example a shared Google Doc) here to show it.
PRD_LINKS = {'adhikaar': 'prd-adhikaar.html', 'vantage': 'prd-vantage.html'}

PROJECTS = [
    dict(id='pwc', cat='Product work at PwC', title='Risk Screening Dashboard',
         one='A risk dashboard for a healthcare client.',
         visual=('stat', '67%', 'less time per case, from 30 minutes to 10'),
         blocks=[('The problem', 'Each case took about 30 minutes from creation to report delivery. The dashboard also had to cover global risk and compliance screening and continuous monitoring of entities.'),
                 ('What I did', ['Gathered business requirements and prioritised workflow improvements', 'Aligned client stakeholders with the technology partner', 'Gave feedback during release testing and live rollout', 'Streamlined case creation, data import, tracking and report delivery'])],
         nums=[('67%', 'less time per case'), ('30 → 10 min', 'per case, end to end'), ('Up to 25', 'cases a week')],
         meta=[('Context', 'Client work at PwC (confidential)'), ('Role', 'Experienced Associate')],
         live=None),
    dict(id='adhikaar', cat='Government · Banking', title='Adhikaar',
         one='Free guidance that helps a family claim the bank deposits of a person who has died, using the RBI\'s own rules.',
         visual=('img', 'img/adhikaar.png', 'Adhikaar home page'),
         blocks=[('The problem', 'Since the RBI Directions of 2025, a bank usually may not demand a succession certificate for a deposit claim. Legal websites and ChatGPT still give the old answer, so families go to court.'),
                 ('Key insight', 'The person who releases the money is the branch officer. Adhikaar gives the family a page for the officer: the RBI paragraph, with its number, beside the bank\'s own published policy.'),
                 ('What I built', ['Up to 8 questions, then 1 of 8 verdicts at a shareable link', 'Document checklist with issuer, cost and time', 'Policy table for 8 banks, with old rows flagged', 'Print or PDF by email, in English, Hindi and Kannada', '"Ask Saathi" assistant; no login, no stored claim data']),
                 ('Honest status', 'Live, with a public metrics page. Five interview participants used it. The live traffic so far is the team\'s own testing, so I report no user numbers yet.')],
         nums=[('₹17k → ₹1k', 'estimated cost, court route against simplified route'), ('7', 'interviews across 6 segments'), ('53', 'automated tests, all passing')],
         meta=[('Case study', 'Rethink Systems: Government and public sector'), ('Role', 'Research, PRD, design, build, launch'), ('Built with', 'Next.js, TypeScript, Supabase, Groq, Vercel')],
         live='https://adhikaar-gamma.vercel.app'),
    dict(id='vantage', cat='Learning · AI', title='Vantage',
         one='An AI learning app that trains client-facing consultants to judge which AI approach fits a client problem.',
         visual=('img', 'img/vantage.png', 'Vantage login page'),
         blocks=[('The problem', 'Professionals in India use AI every week, but cannot tell which AI approach fits a new client problem. Courses add more content, and free content is completed by fewer than 5% of learners.'),
                 ('Why this user', 'I ran 9 interviews across 8 roles before choosing a persona. The client-facing consultant came out on top: the problem comes back every week, a wrong approach reaches a paying client, and the answer can be graded.'),
                 ('What I built', ['Guess before reveal: the answer shows only after the learner commits, and the reveal explains why each other option loses', '90 scenarios and 120 concept questions, in difficulty tiers', 'Solve: bring a real client problem, get a step-by-step approach', 'A human review gate: no AI-made question reaches a learner unchecked']),
                 ('What the pilot taught me', '17 external testers used it with no onboarding call. Only 2 of 17 found the scenario quiz, so I changed the navigation. I cut share and invite, streaks and payments, because no evidence supported them.')],
         nums=[('88%', 'of testers finished a meaningful activity with no help (15 of 17)'), ('12 / 14', 'solutions rated helpful'), ('268', 'unit tests')],
         meta=[('Case study', 'Rethink Systems: Learning tech and AI'), ('Role', 'Interviews, PRD, design, build, pilot'), ('Built with', 'Next.js, TypeScript, Supabase, Groq, Vercel')],
         live='https://vantage-app-zeta.vercel.app'),
    dict(id='shravan', cat='Interview practice · Voice AI', title="The Shravan's Round",
         one='A 20-minute AI voice mock interview for product manager candidates, with real Indian PM cases and a score card.',
         visual=('img', 'img/shravan.png', "The Shravan's Round home page"),
         blocks=[('What it does', 'The candidate picks a role, experience level and focus. An AI interviewer in Shravan Tickoo\'s style asks questions out loud. Each answer decides the next question, and mixed Hindi and English is accepted.'),
                 ('The score card', ['Five scores out of 5: structure, product sense, metrics, prioritisation, communication', 'One thing to fix first, with the line from the answer that cost the most', 'An annotated transcript, with every cross-question saved to practise again'])],
         nums=[('2nd', 'place, Rethink AI-First Buildathon'), ('20 min', 'one mock, answered out loud'), ('0', 'logins or cards needed')],
         meta=[('Case study', 'Rethink AI-First Buildathon (team)'), ('Built with', 'Shravan Tickoo')],
         live='https://shravans-round.vercel.app'),
    dict(id='hamsty', cat='Personal product · In build', title='Hamsty',
         one='A voucher wallet. It collects vouchers from pictures and Gmail, reminds people before they expire, and lets them give unused ones away.',
         visual=('phone', 'img/hamsty.png', 'Hamsty welcome screen'),
         blocks=[('The problem', 'Vouchers arrive in email and as screenshots. Most are unnamed codes, for example ₹250 off ₹2,500. People forget them until they expire.'),
                 ('What I built', ['Stash: all vouchers in one place; the code stays hidden until "Show code"', 'Snap: AI reads a voucher picture and fills in the details', 'Expiry reminders 7, 3 and 1 day before, and on the last day', 'Share board with a weekly leaderboard and 6 badges']),
                 ('Decisions I made', ['Guest account first, so people try it before giving an email', 'Picture reader on Groq: free, and it keeps no copy by default', 'Privacy policy written alongside the build'])],
         nums=[('7 · 3 · 1', 'days before expiry when reminders go out'), ('1 / day', 'most reminders a person gets'), ('0', 'sign-up steps to try it')],
         meta=[('Context', 'Personal project'), ('Role', 'Idea, specs, build'), ('Built with', 'Expo, Supabase, Groq, Vercel')],
         live='https://hamsty.vercel.app'),
    dict(id='teammates', cat='Hackathon · Payments', title='AI Teammates',
         one='Two AI agents for a payments company: one turns a sales lead into a payment, one fixes a failed payment. Both hand off to a person at set limits.',
         visual=('flow', None, None),
         blocks=[('The problem', 'Sales teams score each lead by hand, and payment links go out slowly. Support teams check each failed payment by hand, then refund, retry or escalate it.'),
                 ('How it differs from a chatbot', ['It acts: sends payment links and triggers reversals', 'It hands off: large deals and hard cases go to a person with a case summary', 'It is measured: conversion rate, time to close, cases solved without a person, handle time']),
                 ('Business model', 'Used inside the company to lower cost per case, or sold to merchants as a paid add-on, with a small fee per solved case or closed deal.')],
         nums=[('24.07 bn', 'UPI payments in September 2026 (NPCI)'), ('~0.8%', 'of UPI payments fail for technical reasons'), ('1.33 mn', 'RBI Ombudsman complaints in FY25')],
         meta=[('Event', 'Paytm Build for India AI Hackathon, Track 3'), ('Team', 'Tushar Pathak, Manyata Manocha, Sundaram Sharma'), ('Stage', 'Stage 1 pitch, October 2026')],
         live=None),
]

# Case-study structure shared by every project page. Text comes from the blocks above; nothing new is invented.
STORY = {
    'pwc': [
        ('Challenge', 'Each case took about 30 minutes from creation to report delivery. The dashboard also had to cover global risk and compliance screening and continuous monitoring of entities.'),
        ('Approach', ['Gathered business requirements and prioritised workflow improvements', 'Aligned client stakeholders with the technology partner', 'Gave feedback during release testing and live rollout', 'Streamlined case creation, data import, tracking and report delivery']),
        ('Result', 'Processing time per case fell from 30 minutes to 10, a 67% cut, across up to 25 cases a week.'),
    ],
    'adhikaar': [
        ('Challenge', 'Since the RBI Directions of 2025, a bank usually may not demand a succession certificate for a deposit claim. Legal websites and ChatGPT still give the old answer, so families go to court.'),
        ('Approach', ['Key insight: the person who releases the money is the branch officer. The page for the family shows the RBI paragraph, with its number, beside the bank\'s own published policy.', 'Up to 8 questions, then 1 of 8 verdicts at a shareable link', 'Document checklist with issuer, cost and time', 'Policy table for 8 banks, with old rows flagged', 'Print or PDF by email, in English, Hindi and Kannada', '"Ask Saathi" assistant; no login, no stored claim data']),
        ('Result', 'Live, with a public metrics page. Five interview participants used it. The live traffic so far is the team\'s own testing, so I report no user numbers yet.'),
    ],
    'vantage': [
        ('Challenge', 'Professionals in India use AI every week, but cannot tell which AI approach fits a new client problem. Courses add more content, and free content is completed by fewer than 5% of learners.'),
        ('Approach', ['I ran 9 interviews across 8 roles before choosing a persona. The client-facing consultant came out on top: the problem comes back every week, a wrong approach reaches a paying client, and the answer can be graded.', 'Guess before reveal: the answer shows only after the learner commits, and the reveal explains why each other option loses', '90 scenarios and 120 concept questions, in difficulty tiers', 'Solve: bring a real client problem, get a step-by-step approach', 'A human review gate: no AI-made question reaches a learner unchecked']),
        ('Result', '17 external testers used it with no onboarding call. 15 of 17 finished a meaningful activity with no help, and 12 of 14 rated the solutions helpful. Only 2 of 17 found the scenario quiz, so I changed the navigation. I cut share and invite, streaks and payments, because no evidence supported them.'),
    ],
    'shravan': [
        ('Challenge', 'PM candidates need a way to rehearse the interview before the real one.'),
        ('Approach', ['The candidate picks a role, experience level and focus. An AI interviewer in Shravan Tickoo\'s style asks questions out loud. Each answer decides the next question, and mixed Hindi and English is accepted.', 'Five scores out of 5: structure, product sense, metrics, prioritisation, communication', 'One thing to fix first, with the line from the answer that cost the most', 'An annotated transcript, with every cross-question saved to practise again']),
        ('Result', '2nd place, Rethink AI-First Buildathon. The product is live, and a mock needs no login or card.'),
    ],
    'hamsty': [
        ('Challenge', 'Vouchers arrive in email and as screenshots. Most are unnamed codes, for example ₹250 off ₹2,500. People forget them until they expire.'),
        ('Approach', ['Stash: all vouchers in one place; the code stays hidden until "Show code"', 'Snap: AI reads a voucher picture and fills in the details', 'Expiry reminders 7, 3 and 1 day before, and on the last day', 'Share board with a weekly leaderboard and 6 badges', 'Guest account first, so people try it before giving an email', 'Picture reader on Groq: free, and it keeps no copy by default', 'Privacy policy written alongside the build']),
        ('Result', 'In progress. The web demo is live with test data. Phone apps come after the web launch.'),
    ],
    'teammates': [
        ('Challenge', 'Sales teams score each lead by hand, and payment links go out slowly. Support teams check each failed payment by hand, then refund, retry or escalate it.'),
        ('Approach', ['It acts: sends payment links and triggers reversals', 'It hands off: large deals and hard cases go to a person with a case summary', 'It is measured: conversion rate, time to close, cases solved without a person, handle time', 'Business model: used inside the company to lower cost per case, or sold to merchants as a paid add-on, with a small fee per solved case or closed deal']),
        ('Result', 'Pitched. The Stage 1 pitch deck was submitted in October 2026.'),
    ],
}
for _p in PROJECTS:
    _p['blocks'] = STORY[_p['id']]

ROADMAP_VANTAGE = '''<div class="viz" role="group" aria-label="Vantage roadmap">
  <h4 class="viz-title">Roadmap, from the PRD</h4>
  <div class="rm-cols">
    <div class="rm-col shipped"><span class="rm-tag">V1 · Shipped</span><ul>
      <li>Guess-then-reveal practice loop</li>
      <li>90 real-work scenarios and 120 concept questions</li>
      <li>The reveal explains why each alternative loses</li>
      <li>Ask a real client problem, get a step-by-step solution</li>
      <li>First-guess accuracy over time, and a history of every attempt</li>
      <li>Private by default: no streaks, points or leaderboards</li>
      <li>Content pipeline with a human review gate</li>
      <li>Admin analytics dashboard</li>
    </ul></div>
    <div class="rm-col"><span class="rm-tag">V1.1 · Next</span><ul>
      <li><b>Automatic question generation and approval</b><span>Review by hand does not scale past a pilot.</span></li>
      <li><b>Lightweight rating on the reveal step</b><span>Closes the rating-coverage gap.</span></li>
    </ul></div>
    <div class="rm-col"><span class="rm-tag">V1.2 · Later</span><ul>
      <li><b>Skill Improvement Rate scoring</b><span>It needs a validated rubric first.</span></li>
    </ul></div>
    <div class="rm-col cut"><span class="rm-tag">Cut</span><ul>
      <li><b>Share and invite</b><span>No evidence earned it, and it conflicts with the privacy principle.</span></li>
    </ul></div>
  </div></div>
<div class="viz">
  <h4 class="viz-title">User flow, from the PRD</h4>
  <figure class="viz-fig"><a href="img/vantage-userflow.webp"><img src="img/vantage-userflow.webp" width="2200" height="1142" alt="Vantage user flow diagram. Solve answers a real client problem. Practice builds judgment with a guess-then-reveal loop. Progress shows accuracy, history and strength by category." loading="lazy"></a>
  <figcaption>Two surfaces, one judgment engine. Solve answers the problem in front of her. Practice builds the judgment that means she needs help less next time. Click the picture to open it full size.</figcaption></figure>
</div>'''

JOURNEY_ADHIKAAR = '''<div class="viz" role="group" aria-label="Claim journey today">
  <h4 class="viz-title">How a family claims a deposit today, from the PRD</h4>
  <ol class="jr">
    <li><span class="jn">0</span><p>Register the death. 21 days at the municipal body, then a certificate 7 to 14 days later.</p><em class="no">Physical process</em></li>
    <li><span class="jn">1</span><p>Find out what accounts exist. There is no register, and UDGAM covers only deposits dormant for 10+ years.</p><em class="no">No register, no API</em></li>
    <li><span class="jn">2</span><p>Approach the bank. Some banks have an online claim route.</p><em class="no">In person by design</em></li>
    <li class="hit"><span class="jn">3</span><p>The branch tells you which documents you need.</p><em>Failure 1 · Information gap</em></li>
    <li class="hit"><span class="jn">4</span><p>You go and get those documents. This is where the money is lost.</p><em>Failure 2 · Information gap</em></li>
    <li><span class="jn">5</span><p>You submit, and wait. No portal shows a deadline breach.</p><em>Failure 3 · Information gap</em></li>
    <li><span class="jn">6</span><p>Repeat at EPFO, LIC, the depository and the pension office. Nothing carries over.</p><em class="no">Map page only</em></li>
  </ol>
  <p class="viz-note"><b>The one stage Adhikaar V1 attacks:</b> stage 3 into stage 4. It is the moment a family accepts a demand they cannot check, and leaves to get the wrong document.</p>
</div>
<div class="viz">
  <h4 class="viz-title">The page a family prints or emails, from the PRD</h4>
  <figure class="viz-fig viz-tall"><a href="img/prd-adhikaar-2.webp"><img src="img/prd-adhikaar-2.webp" width="1000" height="1500" alt="Adhikaar nominee verdict page: You should not be asked for a succession certificate, with conditions, next steps and the documents list." loading="lazy"></a>
  <figcaption>A nominee verdict: the answer in plain words, the bank's own policy beside it, then the steps. This is the page that gets printed or emailed.</figcaption></figure>
</div>'''
for _p in PROJECTS:
    if _p['id'] == 'vantage': _p['extra'] = ROADMAP_VANTAGE
    if _p['id'] == 'adhikaar': _p['extra'] = JOURNEY_ADHIKAAR

PIC_FOR = {1: '<img class="how-pic" src="img/laptop.webp" alt="Illustration of Manyata sitting cross-legged, working on a laptop" loading="lazy">'}
PIC_FOR = {i: PIC_FOR.get(i, '') for i in range(1, 20)}
STEPS = [
    ('Pick one narrow problem', 'Adhikaar covers one asset after a death, the bank deposit, and leaves out seven others I could not verify in time.'),
    ('Talk to people before choosing a user', 'For Vantage I ran 9 interviews across 8 roles. The persona came out of the interviews.'),
    ('Write the PRD with the evidence labelled', 'Each finding says whether a person said it, I think it, or it is still an assumption.'),
    ('Build and ship it myself', 'Claude Code, Next.js, Supabase and the Groq API, with automated tests: 53 in Adhikaar, 268 in Vantage.'),
    ('Measure honestly, then change the product', 'Only 2 of 17 Vantage testers found the scenario quiz, so I changed the navigation.'),
]


def ul(items):
    return '<ul>' + ''.join(f'<li>{E(i)}</li>' for i in items) + '</ul>'


def block(title, body):
    inner = ul(body) if isinstance(body, list) else f'<p>{E(body)}</p>'
    return f'<div class="blk reveal"><h4>{E(title)}</h4>{inner}</div>'


def visual(v):
    kind, a, b = v
    if kind == 'img':
        return f'<figure class="shot reveal"><img src="{a}" alt="{E(b)}" loading="lazy"></figure>'
    if kind == 'phone':
        return f'<figure class="shot phone reveal"><img src="{a}" alt="{E(b)}" loading="lazy"></figure>'
    if kind == 'stat':
        return f'<figure class="shot statvis reveal"><span class="serif">{E(a)}</span><figcaption>{E(b)}</figcaption></figure>'
    steps = ['Lead or failed payment', 'AI agent with tool calling', 'Rules: refund cap, deal-size limit', 'Mock tools: payment link, refund, reversal', 'Customer on WhatsApp or SMS']
    return ('<figure class="shot flowvis reveal"><ol>' + ''.join(f'<li><span class="serif">{i:02d}</span>{E(t)}</li>' for i, t in enumerate(steps, 1))
            + '</ol><figcaption>Over the limit, a person gets the case with a full summary. Every action goes to a Postgres audit log.</figcaption></figure>')


def project(i, p):
    links = []
    if p['live']:
        links.append(f'<a class="pill-link" href="{p["live"]}">Live site ↗</a>')
    if p['id'] in PRD_LINKS:
        links.append(f'<a class="pill-link ghost" href="{PRD_LINKS[p["id"]]}">Read the PRD ↗</a>')
    meta = ''.join(f'<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>' for k, v in p['meta'])
    nums = ''.join(f'<div class="num reveal"><span class="serif">{E(n)}</span><span>{E(l)}</span></div>' for n, l in p['nums'])
    blocks = ''.join(block(t, b) for t, b in p['blocks'])
    return f'''
<section class="case" id="{p['id']}" aria-labelledby="t-{p['id']}">
  <div class="case-head reveal">
    <div class="case-label"><span>{i:02d}</span><span>{E(p['cat'])}</span></div>
    <h3 class="serif" id="t-{p['id']}">{E(p['title'])}</h3>
    <p class="case-one">{E(p['one'])}</p>
    <div class="case-links">{''.join(links)}</div>
  </div>
  {visual(p['visual'])}
  <div class="nums">{nums}</div>
  {p.get('extra', '')}
  <div class="blocks">{blocks}</div>
  <dl class="meta reveal">{meta}</dl>
</section>'''


index_rows = ''.join(
    f'<li><a href="#{p["id"]}"><span class="ix">{i:02d}</span><span class="serif nm">{E(p["title"])}</span><span class="ct">{E(p["cat"])}</span><span class="ar" aria-hidden="true">↓</span></a></li>'
    for i, p in enumerate(PROJECTS, 1))

has_hero = os.path.exists(os.path.join(HERE, HERO_IMG))
photo = (f'<img src="{HERO_IMG}" alt="Manyata Manocha">' if has_hero else '<span class="serif mono" aria-hidden="true">MM</span>')
offline_imgs = [(src, alt) for src, alt in OFFLINE_IMGS if os.path.exists(os.path.join(HERE, src))]
offline = ('''
  <section class="offline" aria-labelledby="off-title">
    <div class="sec-head"><h2 id="off-title">Off the laptop</h2></div>
    <div class="gallery">''' + ''.join(f'<figure class="reveal"><img src="{s}" alt="{E(a)}" loading="lazy"></figure>' for s, a in offline_imgs)
           + '</div>\n  </section>') if offline_imgs else ''

def _greet(text):
    words, k = [], 0
    for w in text.split(' '):
        words.append('<span class="w">' + ''.join(f'<span class="ch" style="--i:{k + j}">{E(c)}</span>' for j, c in enumerate(w)) + '</span>')
        k += len(w)
    return ' '.join(words)
greet_letters = _greet("Hi, I'm Manyata")

ICON_IN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.5 9.5v8M6.5 6.2v.1M10.5 17.5v-8M10.5 13c0-2.2 1.3-3.6 3.2-3.6s3.1 1.3 3.1 3.6v4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'

page = f'''<title>Manyata Manocha Portfolio</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@500;600;700;800;900&family=Nunito+Sans:opsz,wght@6..12,400;6..12,500;6..12,600;6..12,700&display=swap" rel="stylesheet">
<style>
  /* Layout: one editorial column on charcoal; serif display type; crimson only for the photo block, key numbers and calls to action. */
  :root {{
    color-scheme: light;
    --bg: #f3ebdf; --bg-2: #e9dfcf; --line: rgba(43,33,24,.14);
    --text: #2b2118; --dim: #6e6255;
    --red: #c2562f; --red-ink: #ffffff;
    --serif: "Nunito", "Arial Rounded MT Bold", system-ui, sans-serif;
    --sans: "Nunito Sans", system-ui, -apple-system, sans-serif;
    --max: 1180px;
  }}
  * {{ box-sizing: border-box; }}
  html {{ overflow-x: clip; scroll-behavior: smooth; }}
  body {{ margin: 0; background: var(--bg); color: var(--text); font-family: var(--sans); font-size: 17px; line-height: 1.6;
    padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px)); padding-block: 0 64px; }}
  a {{ color: inherit; }}
  a:focus-visible, button:focus-visible {{ outline: 2px solid var(--red); outline-offset: 4px; }}
  .serif {{ font-family: var(--serif); font-weight: 400; letter-spacing: -0.01em; }}
  .wrap {{ max-width: var(--max); margin: 0 auto; }}
  .label {{ font-size: 13px; letter-spacing: .2em; text-transform: uppercase; font-weight: 600; color: var(--dim); }}

  /* top bar */
  .top {{ display: flex; justify-content: space-between; align-items: center; gap: 16px; padding-block: 28px; }}
  .top .name {{ font-weight: 700; letter-spacing: .14em; text-transform: uppercase; font-size: 13px; text-decoration: none; }}
  .mail-pill {{ background: var(--red); color: var(--red-ink); text-decoration: none; font-weight: 700; font-size: 13px; letter-spacing: .14em; text-transform: uppercase; padding: 15px 26px; border-radius: 999px; transition: transform .2s ease; }}
  .mail-pill:hover {{ transform: translateY(-2px); }}

  /* hero */
  .hero {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); align-items: center; padding-block: 64px 130px; }}
  .photo {{ position: relative; min-width: 0; background: var(--red); aspect-ratio: 6 / 5; margin-left: calc((100% * 2 - 100vw) / 2); display: grid; place-items: center; overflow: hidden; }}
  .photo img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 60% 30%; }}
  .photo::after {{ content: ""; position: absolute; inset: 0; background: linear-gradient(90deg, rgba(27,27,27,0) 45%, rgba(27,27,27,.75) 100%); pointer-events: none; }}
  .photo .mono {{ font-size: clamp(120px, 16vw, 240px); color: var(--bg); }}
  .hero-text {{ position: relative; z-index: 2; margin-left: -16%; }}
  .hero h1 {{ font-family: var(--serif); font-weight: 400; font-size: clamp(64px, 10vw, 150px); line-height: .9; letter-spacing: -0.02em; margin: 0; text-wrap: balance; }}
  .hero h1 .w {{ white-space: nowrap; }}
  .hero h1 .ch {{ display: inline-block; animation: rise .9s cubic-bezier(.2,.75,.2,1) both; animation-delay: calc(var(--i) * 35ms + 100ms); }}
  @keyframes rise {{ from {{ transform: translateY(.25em); }} to {{ transform: none; }} }}
  .hero-sub {{ margin: 34px 0 0 16%; max-width: 30em; font-size: 20px; line-height: 1.55; font-weight: 500; }}
  .socials {{ display: flex; flex-wrap: wrap; align-items: center; gap: 14px 28px; margin: 34px 0 0 16%; font-weight: 600; font-size: 15px; }}
  .socials a {{ text-decoration: none; display: inline-flex; align-items: center; gap: 8px; border-bottom: 1px solid var(--line); padding-bottom: 4px; transition: border-color .2s; }}
  .socials a:hover {{ border-color: var(--text); }}
  .socials svg {{ width: 20px; height: 20px; }}

  /* intro: asymmetric split, text left, framed real photo right */
  .top-right {{ display: flex; align-items: center; gap: 28px; }}
  .top-link {{ font-weight: 600; font-size: 14px; text-decoration: none; border-bottom: 1px solid var(--line); padding-bottom: 3px; }}
  .intro {{ display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, .85fr); gap: clamp(32px, 6vw, 96px); align-items: end;
    min-height: min(820px, calc(100dvh - 110px)); padding-block: 24px 140px; }}
  .intro h1 {{ font-family: var(--serif); font-weight: 400; font-size: clamp(60px, 9vw, 136px); line-height: .92; letter-spacing: -0.02em; margin: 0; }}
  .intro h1 .w {{ white-space: nowrap; }}
  .intro h1 .ch {{ display: inline-block; animation: rise .9s cubic-bezier(.2,.75,.2,1) both; animation-delay: calc(var(--i) * 35ms + 150ms); }}
  .intro-sub {{ margin: 32px 0 0; max-width: 26em; font-size: 20px; line-height: 1.55; font-weight: 500; color: var(--dim); }}
  .intro-cta {{ display: flex; flex-wrap: wrap; gap: 12px; margin-top: 36px; }}
  .portrait {{ margin: 0; aspect-ratio: 4 / 5; border-radius: 6px; overflow: hidden; background: var(--bg-2); animation: lift 1s cubic-bezier(.2,.7,.2,1) both .1s; }}
  .portrait img {{ display: block; width: 100%; height: 100%; object-fit: cover; animation: settle 1.6s cubic-bezier(.2,.7,.2,1) both .1s; }}
  @keyframes lift {{ from {{ opacity: .35; transform: translateY(28px); }} to {{ opacity: 1; transform: none; }} }}
  @keyframes settle {{ from {{ transform: scale(1.12); }} to {{ transform: none; }} }}
  .pill-link:active {{ transform: scale(.98); }}
  @media (prefers-reduced-motion: reduce) {{ .portrait, .portrait img, .intro h1 .ch {{ animation: none !important; }} }}
  @media (max-width: 860px) {{
    .intro {{ grid-template-columns: minmax(0, 1fr); min-height: 0; padding-block: 8px 90px; gap: 40px; }}
    .portrait {{ order: -1; aspect-ratio: 4 / 5; }}
    .intro-sub {{ font-size: 18px; margin-top: 22px; }}
    .top-link {{ display: none; }}
  }}

  /* card hero: avatar row, one big rounded image, text below */
  .card-top {{ padding-block: 22px; }}
  .who {{ display: flex; align-items: center; gap: 14px; text-decoration: none; }}
  .avatar {{ width: 52px; height: 52px; border-radius: 50%; object-fit: cover; display: block; }}
  .who b {{ display: block; font-size: 17px; font-weight: 700; }}
  .who small {{ display: block; font-size: 14px; color: var(--dim); }}
  .shot-hero {{ padding-block: 4px 130px; }}
  .cover {{ margin: 0; border-radius: 16px; overflow: hidden; aspect-ratio: 16 / 8; background: var(--bg-2); animation: lift 1s cubic-bezier(.2,.7,.2,1) both .1s; }}
  .cover img {{ display: block; width: 100%; height: 100%; object-fit: cover; object-position: 60% 35%; animation: settle 1.6s cubic-bezier(.2,.7,.2,1) both .1s; }}
  .shot-text {{ display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, .9fr); gap: 48px; align-items: end; margin-top: 44px; }}
  .shot-text h1 {{ font-family: var(--serif); font-weight: 400; font-size: clamp(56px, 8vw, 120px); line-height: .92; letter-spacing: -0.02em; margin: 0; }}
  .shot-text h1 .w {{ white-space: nowrap; }}
  .shot-text h1 .ch {{ display: inline-block; animation: rise .9s cubic-bezier(.2,.75,.2,1) both; animation-delay: calc(var(--i) * 35ms + 250ms); }}
  .shot-side p {{ margin: 0; font-size: 19px; line-height: 1.55; color: var(--dim); max-width: 26em; }}
  .shot-side .intro-cta {{ margin-top: 26px; }}
  @media (prefers-reduced-motion: reduce) {{ .cover, .cover img, .shot-text h1 .ch {{ animation: none !important; }} }}
  @media (max-width: 860px) {{
    .cover {{ aspect-ratio: 4 / 3; border-radius: 12px; }}
    .shot-text {{ grid-template-columns: minmax(0, 1fr); gap: 20px; margin-top: 28px; }}
    .who small {{ font-size: 12px; }}
    .avatar {{ width: 44px; height: 44px; }}
    .card-top .mail-pill {{ display: none; }}
  }}

  /* section heads */
  .sec-head {{ display: flex; justify-content: space-between; align-items: flex-end; gap: 24px; border-bottom: 1px solid var(--line); padding-bottom: 22px; margin-bottom: 8px; }}
  .sec-head h2 {{ font-family: var(--serif); font-weight: 400; font-size: clamp(44px, 6vw, 84px); line-height: 1; margin: 0; text-wrap: balance; }}

  /* index of work */
  .index {{ list-style: none; margin: 0 0 140px; padding: 0; }}
  .index a {{ display: grid; grid-template-columns: 56px minmax(0, 1fr) auto 32px; align-items: baseline; gap: 20px; padding: 26px 0; border-bottom: 1px solid var(--line); text-decoration: none; transition: color .25s, padding .3s; }}
  .index .ix {{ color: var(--dim); font-size: 14px; letter-spacing: .1em; }}
  .index .nm {{ font-size: clamp(30px, 4vw, 54px); line-height: 1.05; }}
  .index .ct {{ color: var(--dim); font-size: 14px; text-align: right; }}
  .index .ar {{ color: var(--dim); transition: transform .25s; }}
  .index a:hover {{ color: var(--red); padding-left: 10px; }}
  .index a:hover .ar {{ transform: translateY(4px); color: var(--red); }}

  /* case studies */
  .case {{ padding-block: 40px 130px; border-top: 1px solid var(--line); }}
  .case-label {{ display: flex; gap: 18px; font-size: 13px; letter-spacing: .2em; text-transform: uppercase; font-weight: 600; color: var(--dim); }}
  .case-label span:first-child {{ color: var(--red); }}
  .case h3 {{ font-size: clamp(54px, 8vw, 120px); line-height: .95; margin: 22px 0 0; text-wrap: balance; }}
  .case-one {{ font-size: 22px; line-height: 1.5; max-width: 32em; margin: 26px 0 0; font-weight: 500; }}
  .case-links {{ display: flex; flex-wrap: wrap; gap: 12px; margin-top: 30px; }}
  .pill-link {{ display: inline-block; text-decoration: none; background: var(--red); color: var(--red-ink); font-weight: 700; font-size: 15px; padding: 13px 24px; border-radius: 999px; transition: transform .2s; }}
  .pill-link.ghost {{ background: transparent; color: var(--text); box-shadow: inset 0 0 0 1.5px var(--text); }}
  .pill-link:hover {{ transform: translateY(-2px); }}
  .shot {{ margin: 64px 0 0; border-radius: 6px; overflow: hidden; background: var(--bg-2); }}
  .shot img {{ display: block; width: 100%; height: auto; max-width: 100%; }}
  .shot.phone {{ background: #dcd4fb; display: grid; place-items: center; padding: 56px 20px; }}
  .shot.phone img {{ width: min(300px, 70%); border-radius: 28px; box-shadow: 0 30px 60px rgba(0,0,0,.35); }}
  .statvis {{ background: var(--red); color: var(--red-ink); padding: clamp(40px, 7vw, 90px); display: grid; gap: 10px; }}
  .statvis .serif {{ font-size: clamp(120px, 22vw, 300px); line-height: .85; }}
  .statvis figcaption {{ font-size: 22px; max-width: 22em; font-weight: 500; }}
  .flowvis {{ padding: clamp(28px, 5vw, 60px); }}
  .flowvis ol {{ list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); }}
  .flowvis li {{ border-top: 2px solid var(--line); padding: 18px 18px 0 0; font-weight: 600; font-size: 16px; line-height: 1.4; }}
  .flowvis li:last-child {{ border-top-color: var(--red); }}
  .flowvis li .serif {{ display: block; font-size: 44px; color: var(--red); margin-bottom: 8px; }}
  .flowvis figcaption {{ margin-top: 30px; color: var(--dim); font-size: 16px; }}
  .nums {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; margin-top: 56px; }}
  .num {{ border-top: 1px solid var(--line); padding-top: 18px; display: grid; gap: 6px; align-content: start; }}
  .num .serif {{ font-size: clamp(42px, 5vw, 68px); line-height: 1; }}
  .num span:last-child {{ color: var(--dim); font-size: 15px; line-height: 1.45; }}
  .nums .num:first-child .serif {{ color: var(--red); }}
  .blocks {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 44px 64px; margin-top: 64px; }}
  .blk h4 {{ margin: 0 0 12px; font-size: 13px; letter-spacing: .2em; text-transform: uppercase; color: var(--dim); font-weight: 600; }}
  .blk p, .blk li {{ font-size: 17px; line-height: 1.65; margin: 0; }}
  .blk ul {{ margin: 0; padding-left: 20px; }}
  .blk li {{ margin-bottom: 6px; }}
  .meta {{ display: flex; flex-wrap: wrap; gap: 18px 56px; margin: 56px 0 0; padding-top: 22px; border-top: 1px solid var(--line); }}
  .meta dt {{ font-size: 12px; letter-spacing: .2em; text-transform: uppercase; color: var(--dim); font-weight: 600; }}
  .meta dd {{ margin: 6px 0 0; font-size: 15px; font-weight: 500; }}

  /* how I work */
  .how {{ padding-block: 40px 140px; }}
  .steps {{ list-style: none; margin: 0; padding: 0; }}
  .steps li {{ display: grid; grid-template-columns: 120px minmax(0, 1fr) minmax(0, 1.2fr); gap: 32px; align-items: baseline; padding: 34px 0; border-bottom: 1px solid var(--line); }}
  .steps .serif {{ font-size: 56px; line-height: 1; color: var(--red); }}
  .steps h3 {{ margin: 0; font-size: 24px; font-weight: 600; line-height: 1.3; }}
  .steps p {{ margin: 0; color: var(--dim); }}

  /* quote band */
  .quote {{ margin-inline: calc(50% - 50vw); background: var(--red); color: var(--red-ink);
    padding-block: clamp(70px, 10vw, 140px); padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px)); }}
  .quote blockquote {{ max-width: var(--max); margin: 0 auto; }}
  .quote p {{ font-family: var(--serif); font-size: clamp(30px, 4.2vw, 58px); line-height: 1.15; margin: 0; text-wrap: balance; }}
  .quote footer {{ margin-top: 34px; font-size: 16px; }}
  .quote footer b {{ display: block; font-size: 18px; }}

  /* about / experience */
  .about {{ padding-block: 130px 120px; }}
  .about-grid {{ display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); gap: 72px; margin-top: 40px; }}
  .lead {{ font-size: 20px; line-height: 1.6; margin: 0 0 20px; }}
  .tl {{ list-style: none; margin: 0; padding: 0; }}
  .tl li {{ padding: 24px 0; border-bottom: 1px solid var(--line); }}
  .tl .row {{ display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap; }}
  .tl b {{ font-size: 20px; font-weight: 600; }}
  .tl .when, .tl .role {{ color: var(--dim); font-size: 15px; }}
  .tl p {{ margin: 10px 0 0; font-size: 16px; }}
  .awards {{ display: grid; gap: 18px; }}
  .award {{ border: 1px solid var(--line); border-radius: 6px; padding: 28px; }}
  .award .serif {{ font-size: 44px; line-height: 1; color: var(--red); }}
  .award b {{ display: block; margin-top: 12px; font-size: 17px; }}
  .award p {{ margin: 6px 0 0; color: var(--dim); font-size: 15px; }}
  .edu {{ margin-top: 28px; }}
  .edu div {{ padding: 14px 0; border-bottom: 1px solid var(--line); }}
  .edu b {{ display: block; font-weight: 600; }}
  .edu span {{ color: var(--dim); font-size: 15px; }}

  /* off the laptop */
  .offline {{ padding-block: 20px 120px; }}
  .gallery {{ display: grid; grid-template-columns: minmax(0, 1.45fr) minmax(0, 1fr); gap: 20px; margin-top: 40px; }}
  .gallery figure {{ margin: 0; border-radius: 6px; overflow: hidden; height: clamp(320px, 42vw, 560px); }}
  .gallery img {{ display: block; width: 100%; height: 100%; object-fit: cover; transition: transform .8s cubic-bezier(.2,.7,.2,1); }}
  .gallery figure:hover img {{ transform: scale(1.04); }}

  /* contact */
  .contact {{ padding-block: 60px 40px; }}
  .contact h2 {{ font-family: var(--serif); font-weight: 400; font-size: clamp(72px, 13vw, 200px); line-height: .9; margin: 14px 0 0; }}
  .contact p {{ font-size: 20px; color: var(--dim); max-width: 30em; margin: 28px 0 0; }}
  .c-row {{ display: flex; flex-wrap: wrap; align-items: center; gap: 16px; margin-top: 40px; }}
  .c-mail {{ font-family: var(--serif); font-size: clamp(26px, 3.6vw, 46px); overflow-wrap: anywhere; }}
  .copy {{ font: inherit; font-size: 14px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; border: 0; border-radius: 999px; padding: 12px 22px; background: var(--red); color: var(--red-ink); cursor: pointer; }}
  .c-links {{ display: flex; gap: 28px; margin-top: 34px; font-weight: 600; }}
  .c-links a {{ text-decoration: none; border-bottom: 1px solid var(--line); padding-bottom: 4px; }}
  .foot {{ margin-top: 90px; padding-top: 22px; border-top: 1px solid var(--line); color: var(--dim); font-size: 14px; }}

  /* scroll reveal: visible by default; animates only where scroll timelines exist */
  @supports (animation-timeline: view()) {{
    .reveal {{ animation: fade-up linear both; animation-timeline: view(); animation-range: entry 0% entry 35%; }}
    @keyframes fade-up {{ from {{ opacity: .15; transform: translateY(40px); }} to {{ opacity: 1; transform: none; }} }}
  }}
  @media (prefers-reduced-motion: reduce) {{
    .reveal, .hero h1 .ch {{ animation: none !important; }}
    .gallery img {{ transition: none; }}
    html {{ scroll-behavior: auto; }}
  }}

  @media (max-width: 860px) {{
    body {{ font-size: 16px; }}
    .top {{ padding-block: 18px; }}
    .top .name {{ font-size: 11px; }}
    .mail-pill {{ padding: 11px 14px; font-size: 10.5px; letter-spacing: .06em; }}
    .hero {{ grid-template-columns: minmax(0, 1fr); padding-block: 20px 90px; }}
    .photo::after {{ background: linear-gradient(180deg, rgba(27,27,27,0) 55%, rgba(27,27,27,.85) 100%); }}
    .photo {{ aspect-ratio: 1 / 1; margin-left: calc(-1 * max(20px, env(safe-area-inset-left, 0px))); margin-right: calc(-1 * max(20px, env(safe-area-inset-right, 0px))); }}
    .hero-text {{ margin: -36px 0 0; }}
    .hero-sub, .socials {{ margin-left: 0; }}
    .hero-sub {{ font-size: 18px; }}
    .index a {{ grid-template-columns: 34px minmax(0, 1fr) 20px; gap: 12px; }}
    .index .ct {{ display: none; }}
    .nums {{ grid-template-columns: minmax(0, 1fr); gap: 18px; }}
    .blocks {{ grid-template-columns: minmax(0, 1fr); gap: 36px; }}
    .flowvis ol {{ grid-template-columns: minmax(0, 1fr); gap: 10px; }}
    .flowvis li {{ display: grid; grid-template-columns: 56px minmax(0, 1fr); align-items: baseline; padding: 14px 0 0; }}
    .flowvis li .serif {{ font-size: 32px; margin: 0; }}
    .steps li {{ grid-template-columns: minmax(0, 1fr); gap: 8px; padding: 26px 0; }}
    .steps .serif {{ font-size: 40px; }}
    .about-grid {{ grid-template-columns: minmax(0, 1fr); gap: 48px; }}
    .gallery {{ grid-template-columns: minmax(0, 1fr); }}
    .case-one {{ font-size: 19px; }}
  }}

  /* ===== high-end layer: floating island nav, double-bezel frames, button-in-button, grain ===== */
  :root {{ --line: rgba(43,33,24,.12); --ease: cubic-bezier(.32,.72,0,1); }}
  body::after {{ content: ""; position: fixed; inset: 0; z-index: 40; pointer-events: none; opacity: .045;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"); }}
  .card-top {{ position: sticky; top: max(14px, env(safe-area-inset-top, 0px)); z-index: 30; margin: 16px 0 24px; padding: 8px 8px 8px 10px;
    border-radius: 999px; background: rgba(243,235,223,.82); -webkit-backdrop-filter: blur(18px) saturate(140%); backdrop-filter: blur(18px) saturate(140%);
    box-shadow: 0 0 0 1px rgba(43,33,24,.12), inset 0 1px 0 rgba(255,255,255,.6), 0 18px 40px -20px rgba(0,0,0,.6); }}
  .card-top .avatar {{ width: 42px; height: 42px; }}
  .card-top .who b {{ font-size: 15px; }} .card-top .who small {{ font-size: 13px; }}
  .card-top .top-link {{ border: 0; padding: 0; color: var(--dim); transition: color .5s var(--ease); }}
  .card-top .top-link:hover {{ color: var(--text); }}
  .card-top .mail-pill {{ padding: 12px 20px; font-size: 12px; }}
  /* double bezel: outer tray + inner core with concentric radius */
  .cover, .shot, .gallery figure, .award {{ padding: 6px; border-radius: 28px; background: rgba(43,33,24,.04);
    box-shadow: 0 0 0 1px rgba(43,33,24,.1), 0 30px 60px -30px rgba(0,0,0,.55); }}
  .cover img, .shot > img, .gallery figure img {{ border-radius: 22px; }}
  .shot.phone, .statvis, .flowvis {{ border-radius: 28px; }}
  .statvis {{ box-shadow: 0 0 0 6px rgba(43,33,24,.04), 0 0 0 7px rgba(43,33,24,.1); }}
  .award {{ padding: 30px; background: linear-gradient(180deg, rgba(255,255,255,.55), rgba(255,255,255,.25)); box-shadow: 0 0 0 1px rgba(43,33,24,.1), inset 0 1px 0 rgba(43,33,24,.1); border: 0; }}
  .gallery figure {{ height: auto; }} .gallery figure img {{ height: clamp(300px, 40vw, 540px); }}
  /* button-in-button */
  .pill-link {{ display: inline-flex; align-items: center; gap: 12px; padding: 7px 7px 7px 24px; transition: transform .6s var(--ease), background-color .6s var(--ease); }}
  .pill-link .pi {{ width: 34px; height: 34px; border-radius: 50%; display: grid; place-items: center; font-size: 15px; background: rgba(255,255,255,.16); transition: transform .6s var(--ease); }}
  .pill-link.ghost .pi {{ background: rgba(43,33,24,.1); }}
  .pill-link:hover {{ transform: none; }}
  .pill-link:hover .pi {{ transform: translate(3px, -1px) scale(1.06); }}
  .pill-link:active {{ transform: scale(.98); }}
  .copy, .mail-pill {{ transition: transform .6s var(--ease); }}
  .copy:active, .mail-pill:active {{ transform: scale(.98); }}
  /* eyebrow pill on case studies */
  .case-label {{ display: inline-flex; gap: 10px; align-items: center; padding: 6px 14px; border-radius: 999px; font-size: 11px; letter-spacing: .2em;
    background: rgba(43,33,24,.05); box-shadow: 0 0 0 1px rgba(43,33,24,.1); }}
  .index a {{ transition: color .6s var(--ease), padding .6s var(--ease); }}
  .gallery img {{ transition: transform 1.2s var(--ease); }}
  @supports (animation-timeline: view()) {{
    @keyframes fade-up {{ from {{ opacity: .1; transform: translateY(56px); filter: blur(8px); }} to {{ opacity: 1; transform: none; filter: none; }} }}
  }}
  /* warm theme: rounded sans display, terracotta only accent */
  .serif, .shot-text h1, .sec-head h2, .case h3, .contact h2, .quote p, .num .serif, .award .serif, .steps .serif, .index .nm, .c-mail {{ font-weight: 800; letter-spacing: -0.03em; }}
  .shot-text h1, .case h3, .contact h2 {{ line-height: .95; }}
  .shot.statvis {{ background: var(--red); }}
  .who b {{ font-weight: 800; }}
  .card-top .top-right {{ gap: 22px; padding-right: 14px; }}
  .card-top .top-link {{ font-weight: 700; }}
  @media (max-width: 860px) {{
    .card-top {{ margin: 12px 0 18px; }}
    .card-top .who small {{ display: none; }}
    .cover, .shot, .gallery figure {{ padding: 4px; border-radius: 20px; }}
    .cover img, .shot > img, .gallery figure img {{ border-radius: 16px; }}
  }}
</style>

<div class="wrap">
  <nav class="top card-top" aria-label="Top">
    <a class="who" href="#"><img class="avatar" src="img/avatar.jpg" alt=""><span><b>Manyata Manocha</b><small>AI Product Manager · Bengaluru</small></span></a>
    <div class="top-right"><a class="top-link" href="{LINKEDIN}">LinkedIn</a><a class="top-link" href="#contact">Email</a></div>
  </nav>

  <header class="shot-hero">
    <figure class="cover"><img src="img/cover.jpg" alt="Manyata Manocha at an airfield" fetchpriority="high"></figure>
    <div class="shot-text">
      <h1 aria-label="Hi, I'm Manyata"><span aria-hidden="true">{greet_letters}</span></h1>
      <div class="shot-side">
        <p>AI Product Manager in Bengaluru. I research the problem, write the PRD, build with AI and measure honestly.</p>
        <div class="intro-cta"><a class="pill-link" href="#work">Selected work</a><a class="pill-link ghost" href="resume.html">Resume</a></div>
      </div>
    </div>
  </header>

  <section id="work" aria-labelledby="work-title">
    <div class="sec-head"><h2 id="work-title">Selected work</h2><span class="label">{len(PROJECTS)} products</span></div>
    <ol class="index">{index_rows}</ol>
  </section>
  {''.join(project(i, p) for i, p in enumerate(PROJECTS, 1))}

  <section class="how" aria-labelledby="how-title">
    <div class="sec-head"><h2 id="how-title">How I work</h2></div>
    <div class="how-grid">
      <ol class="steps">{''.join(f'<li class="reveal"><span class="serif">{i:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p>{PIC_FOR[i]}</li>' for i, (t, d) in enumerate(STEPS, 1))}</ol>
    </div>
  </section>
</div>

<section class="quote" aria-label="Quote">
  <blockquote class="reveal">
    <p>“You demonstrated excellence across every dimension: product thinking, building, ownership, initiative, and impact.”</p>
    <footer><b>Shravan Tickoo</b>Founder and CEO, Rethink Systems · from my Top Operator certificate</footer>
  </blockquote>
</section>

<div class="wrap">
  <section class="about" id="about" aria-labelledby="about-title">
    <div class="sec-head"><h2 id="about-title">About Me</h2></div>
    <div class="exp-grid">
      <div class="exp-col">
        <p class="lead reveal">A Delhite currently in Bengaluru, building AI products that solve real problems. I love watching movies and series, always hunting for the next good show, though I'm picky.<br>Dance is in my blood and music makes my day.<br>I'm curious about the world, the small and big things around us.<br>I like to understand why people think the way they do, which makes me observant.<br>Talkative (probably too much :p), and I enjoy diving into conversations about product, life, and honestly, everything.</p>
      </div>
      <div class="exp-col">
      <div class="about-collage reveal">
        <div class="collage-pic collage-pink"><img src="img/portrait-about.webp" alt="Manyata" loading="lazy"></div>
      </div>
      </div>
    </div>
  </section>

  <section class="experience" id="experience" aria-labelledby="exp-title">
    <div class="sec-head"><h2 id="exp-title">Experience</h2></div>
    <div class="timeline">
      <div class="timeline-item">
        <div class="timeline-head">
          <h3>PwC Acceleration Centers</h3>
          <span class="timeline-role">Experienced Associate</span>
          <span class="timeline-dates">Aug 2023 – Present</span>
        </div>
        <p class="timeline-desc">Leading fraud investigations and building AI-assisted risk screening dashboards. Led a team of 8, cut case processing time by 67% (30 to 10 min), and helped ship compliance tools for healthcare clients.</p>
      </div>
      <div class="timeline-item">
        <div class="timeline-head">
          <h3>ICICI Bank</h3>
          <span class="timeline-role">Privilege Banker</span>
          <span class="timeline-dates">Nov 2016 – Sep 2019</span>
        </div>
        <p class="timeline-desc">Performed financial analysis, AML monitoring, and KYC reviews on client portfolios. Built risk management reports and ensured regulatory compliance.</p>
      </div>
      <div class="timeline-item">
        <div class="timeline-head">
          <h3>HDFC Bank</h3>
          <span class="timeline-role">Personal Banker</span>
          <span class="timeline-dates">Dec 2019 – Sep 2020</span>
        </div>
        <p class="timeline-desc">Managed client portfolios and provided personalized financial advisory services.</p>
      </div>
      <div class="timeline-item">
        <div class="timeline-head">
          <h3>PwC India</h3>
          <span class="timeline-role">Corporate Finance & Investment Banking Intern</span>
          <span class="timeline-dates">May – Jul 2022</span>
        </div>
        <p class="timeline-desc">Performed data cleaning and financial statement analysis to support valuation models and client presentations.</p>
      </div>
      <div class="timeline-item">
        <div class="timeline-head">
          <h3>Credflow</h3>
          <span class="timeline-role">Channel Sales Intern</span>
          <span class="timeline-dates">May – Jun 2022</span>
        </div>
        <p class="timeline-desc">Conducted performance analysis and designed business strategies to optimize revenue growth.</p>
      </div>
    </div>
  </section>

  <footer class="contact" id="contact">
    <h2>Contact</h2>
    <h3>Let's Build Together,<br>Open to Product Manager roles</h3>
    <div class="c-row">
      <span class="c-mail" id="email-text">{EMAIL}</span>
      <button type="button" class="copy" id="copy-email">Copy</button>
      <a href="{LINKEDIN}">LinkedIn ↗</a>
    </div>
    <div class="foot">Made with a lot of Caffeine Manyata Manocha 2026</div>
  </footer>
</div>
<script>
  (function () {{
    var btn = document.getElementById('copy-email'), txt = document.getElementById('email-text');
    btn.addEventListener('click', function () {{
      function selectIt() {{ var r = document.createRange(); r.selectNodeContents(txt); var s = getSelection(); s.removeAllRanges(); s.addRange(r); btn.textContent = 'Selected'; }}
      try {{ navigator.clipboard.writeText(txt.textContent).then(function () {{ btn.textContent = 'Copied'; }}, selectIt); }} catch (e) {{ selectIt(); }}
    }});
  }})();
</script>
'''

# button-in-button: move each pill button's arrow into its own circle
page = page.replace('<a class="pill-link" href="#work">Selected work</a>', '<a class="pill-link" href="#work">Selected work ↓</a>')
page = page.replace('<a class="pill-link ghost" href="resume.html">Resume</a>', '<a class="pill-link ghost" href="resume.html">Resume ↗</a>')
page = re.sub(r'(<a class="pill-link[^"]*"[^>]*>)([^<]*?)\s*([↗↓])</a>', r'\1\2<span class="pi" aria-hidden="true">\3</span></a>', page)
import sky_theme
page = sky_theme.apply(page)
page = sky_theme.split(page, PROJECTS)
page = page + sky_theme.PEEK_JS
open(os.path.join(HERE, 'portfolio-web.html'), 'w', encoding='utf-8').write(page)


# ---------- resume page (no phone number) ----------
def md_to_html(md):
    out, in_ul = [], False

    def inline(t):
        t = _h.escape(t, quote=False)
        t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
        return re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)
    for l in md.splitlines():
        if l.startswith('- '):
            if not in_ul:
                out.append('<ul>')
                in_ul = True
            out.append(f'<li>{inline(l[2:])}</li>')
            continue
        if in_ul:
            out.append('</ul>')
            in_ul = False
        m = re.match(r'(#{1,4}) (.*)', l)
        if m:
            out.append(f'<h{len(m.group(1))}>{inline(m.group(2))}</h{len(m.group(1))}>')
        elif l.strip():
            out.append(f'<p>{inline(l)}</p>')
    if in_ul:
        out.append('</ul>')
    return '\n'.join(out)


resume_md = open(os.path.join(HERE, '..', 'Master Resume.md'), encoding='utf-8').read()
resume_md = re.sub(r'\s*\|\s*\+91[\d ]+', '', resume_md)
assert '9899828161' not in resume_md and '98998' not in resume_md
resume = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Manyata Manocha Resume</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800;900&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap" rel="stylesheet">
<style>
:root { color-scheme: light; --bg: #f3ebdf; --text: #2b2118; --dim: #6e6255; --line: rgba(43,33,24,.14); --red: #c2562f; }
body { margin: 0; background: var(--bg); color: var(--text); font: 16px/1.6 "Nunito Sans", system-ui, sans-serif; padding: 36px max(20px, env(safe-area-inset-left, 0px)) 64px; }
main { max-width: 820px; margin: 0 auto; }
a { color: var(--text); }
.back { display: inline-block; margin-bottom: 36px; font-weight: 700; text-decoration: none; border-bottom: 1px solid var(--line); padding-bottom: 4px; }
h1 { font-family: "Nunito", system-ui, sans-serif; font-weight: 400; font-size: clamp(44px, 8vw, 72px); line-height: 1; margin: 0 0 12px; }
h2 { font-family: "Nunito", system-ui, sans-serif; font-weight: 400; font-size: 30px; margin: 44px 0 10px; padding-bottom: 10px; border-bottom: 1px solid var(--line); }
h3 { font-size: 18px; margin: 22px 0 2px; }
h4 { font-size: 14px; color: var(--dim); margin: 6px 0 4px; font-weight: 600; }
p { margin: 4px 0; } ul { margin: 6px 0 12px; padding-left: 20px; } li { margin-bottom: 5px; }
</style></head><body><main><a class="back" href="./">← Back to portfolio</a>
''' + md_to_html(resume_md) + '</main></body></html>'
open(os.path.join(HERE, 'resume.html'), 'w', encoding='utf-8').write(resume)
print('written', len(page), 'hero photo' if has_hero else 'no hero photo', len(offline_imgs), 'offline photos')


import prd_pages
prd_pages.build()
