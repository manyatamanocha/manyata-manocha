# Builds prd-adhikaar.html and prd-vantage.html from the user's Word files in ~/Downloads.
# Called at the end of build_web.py.
import html as _h
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS = os.path.expanduser('~/Downloads')
E = _h.escape
ADHIKAAR_SECTIONS = ['The Chosen Problem — Case Summary', 'Stakeholder Mapping', 'The Current Claim Journey', 'Secondary Research',
                     'Existing Tools — and the Seam They Miss', 'Primary Research', 'Opportunity & Prioritization',
                     'Product Strategy — User, Buyer, Problem Statement', 'Solution Ideation & Direction', 'Product Detailing & MVP Scope',
                     'UX & Product Design', 'Analytics & Event Tracking', 'Build & Deployment', 'Launch, Growth Loop & Iteration']

STYLE = """
:root { color-scheme: light; --bg: #f3ebdf; --bg-2: #e9dfcf; --text: #2b2118; --dim: #6e6255; --line: rgba(43,33,24,.14); --red: #c2562f; }
body { margin: 0; background: var(--bg); color: var(--text); font: 17px/1.65 "Nunito Sans", system-ui, sans-serif;
  padding: 36px max(20px, env(safe-area-inset-right, 0px)) 72px max(20px, env(safe-area-inset-left, 0px)); }
main { max-width: 860px; margin: 0 auto; }
a { color: var(--text); }
.back { display: inline-block; margin-bottom: 40px; font-weight: 700; text-decoration: none; border-bottom: 1px solid var(--line); padding-bottom: 4px; }
main > p:nth-of-type(1) { font-size: 13px; letter-spacing: .2em; text-transform: uppercase; color: var(--red); }
p { margin: 0 0 14px; } b { font-weight: 700; }
.tbl { overflow-x: auto; margin: 18px 0 28px; border: 1px solid var(--line); border-radius: 12px; }
table { border-collapse: collapse; width: 100%; min-width: 560px; font-size: 15px; line-height: 1.5; }
td, th { border-bottom: 1px solid var(--line); padding: 10px 12px; vertical-align: top; }
tr:first-child td { background: var(--bg-2); font-weight: 600; }
td p { margin: 0; }
figure { margin: 20px 0 8px; } figure img { display: block; width: 100%; height: auto; border: 2px solid #161616; box-shadow: 5px 5px 0 #161616; background: #fff; }
ul, ol { padding-left: 22px; } li { margin-bottom: 6px; }
"""


def docx_body(path):
    raw = subprocess.run(['textutil', '-convert', 'html', '-stdout', path], capture_output=True, text=True, check=True).stdout
    body = re.search(r'<body>(.*)</body>', raw, re.S).group(1)
    body = re.sub(r'<span class="Apple-converted-space">([^<]*)</span>', lambda m: m.group(1).replace('\xa0', ' '), body)
    body = re.sub(r'<span class="Apple-tab-span">[^<]*</span>', ' ', body)
    body = re.sub(r'\s(class|valign|cellspacing|cellpadding|style)="[^"]*"', '', body)
    body = re.sub(r'<p><b></b><br></p>|<p><br></p>', '', body)
    return body.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')


# (caption text, picture, alt text, match whole caption?) - captions come from the user's Word files
ADH_FIGS = [("The homepage. The claim journey", 'img/prd-adhikaar-1.webp', 'Adhikaar homepage', False),
            ("A nominee verdict", 'img/prd-adhikaar-2.webp', 'Adhikaar nominee verdict page', False)]
VAN_FIGS = [("Vantage user flow", 'img/vantage-userflow.webp', 'Vantage user flow diagram: Solve, Practice and Progress', True),
            ("Landing Page", 'img/prd-vantage-2.webp', 'Vantage landing page', True),
            ("Home Page", 'img/prd-vantage-3.webp', 'Vantage home page', True),
            ("Admin analytics", 'img/prd-vantage-4.webp', 'Vantage admin analytics page', True)]


def add_figures(body, figs):
    for cap, src, alt, exact in figs:
        hits = []
        for m in re.finditer(r'<p>(.*?)</p>', body, re.S):
            t = _h.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()
            if (t == cap) if exact else t.startswith(cap):
                hits.append(m.start())
        assert hits, cap
        i = hits[-1]
        body = body[:i] + f'<figure><a href="{src}"><img src="{src}" alt="{alt}" loading="lazy"></a></figure>' + body[i:]
    return body


def page(title, body):
    head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{E(title)}</title>'
            '<link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap" rel="stylesheet">'
            f'<style>{STYLE}</style></head><body><main><a class="back" href="./">← Back to portfolio</a>\n')
    return head + body + '\n<p><a class="back" href="./">← Back to portfolio</a></p></main></body></html>'


def build():
    adh = docx_body(os.path.join(DOWNLOADS, 'Adhikaar PRD.docx'))
    # Approved fix: the top of the Adhikaar PRD was left over from the Vantage template.
    adh, n1 = re.subn(r'<p><b>Week 4 ·\s*Learning Tech &amp; AI for non tech professionals</b></p>\s*'
                      r'<p>Building - and shipping - an MVP for Tech &amp; AI Learning Platform for non tech professionals</p>',
                      '<p><b>Adhikaar · Government and public sector case study</b></p>', adh)
    contents = '<ol>' + ''.join(f'<li>{E(t)}</li>' for t in ADHIKAAR_SECTIONS) + '</ol>'
    adh, n2 = re.subn(r'(<p><b>Contents</b></p>\s*)<div class="tbl"><table>.*?</table></div>',
                      lambda m: m.group(1) + contents, adh, count=1, flags=re.S)
    assert n1 == 1 and n2 == 1, (n1, n2)
    adh = add_figures(adh, ADH_FIGS)
    open(os.path.join(HERE, 'prd-adhikaar.html'), 'w', encoding='utf-8').write(page('Adhikaar PRD', adh))
    van = add_figures(docx_body(os.path.join(DOWNLOADS, 'Vantage FINAL.docx')), VAN_FIGS)
    open(os.path.join(HERE, 'prd-vantage.html'), 'w', encoding='utf-8').write(page('Vantage PRD', van))
    print('PRD pages written')
