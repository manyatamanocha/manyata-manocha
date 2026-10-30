# Builds site/ : a clean folder you can upload to any static host (Vercel, Netlify, GitHub Pages).
# Run after build_web.py:  python3 build_web.py && python3 make_site.py
import os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'site')
PAGES = ['projects.html', 'resume.html', 'prd-adhikaar.html', 'prd-vantage.html'] + \
        sorted(f for f in os.listdir(HERE) if f.startswith('project-') and f.endswith('.html'))
DESC = 'Manyata Manocha, AI Product Manager. Six products from research and PRD to build and metrics.'

# keep site/.vercel (the link to the Vercel project); clear everything else
if os.path.exists(OUT):
    for name in os.listdir(OUT):
        if name not in ('.vercel', '.vercelignore', '.gitignore'):
            path = os.path.join(OUT, name)
            shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)
os.makedirs(os.path.join(OUT, 'img'), exist_ok=True)

land = open(os.path.join(HERE, 'portfolio-web.html'), encoding='utf-8').read()
land = land.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
        f'<meta name="description" content="{DESC}">'
        '<meta property="og:title" content="Manyata Manocha, AI Product Manager">'
        f'<meta property="og:description" content="{DESC}">'
        '<style>body{margin:0}img{max-width:100%}</style>')
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(head + '</head><body>' + land + '</body></html>')
for f in PAGES:
    shutil.copy(os.path.join(HERE, f), os.path.join(OUT, f))

used = set()
for f in os.listdir(OUT):
    if f.endswith('.html'):
        used |= set(re.findall(r'img/[A-Za-z0-9_.-]+\.(?:webp|png|jpg|jpeg|svg)', open(os.path.join(OUT, f), encoding='utf-8').read()))
missing = [u for u in sorted(used) if not os.path.exists(os.path.join(HERE, u))]
for u in sorted(used):
    if os.path.exists(os.path.join(HERE, u)):
        shutil.copy(os.path.join(HERE, u), os.path.join(OUT, u))
print('pages:', 1 + len(PAGES), '| images:', len(used) - len(missing), '| missing:', missing)
