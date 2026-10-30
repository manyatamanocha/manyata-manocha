# Handoff for Codex: Manyata's portfolio website

Written 28 Oct 2026. Last updated 28 Oct 2026 (end of the first long session). Read this file first. Then read `Portfolio progress.md` for the history.

## What this is

A portfolio website for Manyata Manocha. She is looking for AI Product Manager roles.
The site has these pages:

| Page | File | What it is |
|---|---|---|
| Landing | `portfolio-web.html` | Hello headline, intro, cartoon, How I work, About, Off the laptop, Contact |
| Projects | `projects.html` | Six project tiles and a "Work samples" row |
| Six project pages | `project-pwc.html`, `project-adhikaar.html`, `project-vantage.html`, `project-shravan.html`, `project-hamsty.html`, `project-teammates.html` | One case study each: Challenge, Approach, Result. Vantage also has a roadmap and the user-flow diagram. Adhikaar also has the claim journey and the verdict screenshot. |
| Resume | `resume.html` | Built from `../Master Resume.md` |
| Two PRDs | `prd-adhikaar.html`, `prd-vantage.html` | Built from her Word files. Their pictures are back in, each above its own caption. |

The PDF `Manyata_Manocha_AI_PM_Portfolio.pdf` is an older, separate version. See "Known gaps".

## Live copy

**Public site (anyone can open it, no login): `https://manyata-manocha.vercel.app`**
Deployed on 28 Oct 2026 with Vercel (project `manyata-manocha`, account `manyatamanocha`). It shows the files in `site/`.

The older Claude preview `https://claude.ai/artifact/3bS1Vr4oNwpVc1UCbw8UrR` is private. You cannot read it. Ignore it.

### Update the live site

```
python3 build_web.py && python3 make_site.py
cd site && npx vercel deploy --prod --yes
```

The first time on a new machine, run `npx vercel login`. `site/.vercel` holds the link to the project. Never upload `.env*` files (`site/.vercelignore` blocks them).

## Do not edit the HTML files by hand

Python scripts write all the HTML files. If you edit an HTML file, the next build erases your edit.
Edit the scripts. Then run the build.

| Script | What it controls |
|---|---|
| `build_web.py` | All text. The `PROJECTS` list (title, summary, numbers, links). The `STORY` dict (Challenge, Approach, Result for each project). The `STEPS` list (How I work). `ROADMAP_VANTAGE` and `JOURNEY_ADHIKAAR` (extra pictures, shown through the `extra` slot of a project, between the numbers and the Challenge block). The About section. The contact section. Calls the other scripts. |
| `sky_theme.py` | The look. All CSS. The top bar and hero. The cartoon animation (`PEEK_JS`). The split into landing, projects and project pages (`split()`). The "Work samples" row. |
| `prd_pages.py` | The two PRD pages. Reads her Word files with the macOS tool `textutil`. `add_figures()` puts the pictures back, matched by caption text (`ADH_FIGS`, `VAN_FIGS`). |
| `make_site.py` | Builds the upload folder `site/` (see "Deploy"). |

`portfolio.html` is the source of the old PDF. The web build does not use it.

## Build and preview

```
cd "/Users/nikki/Documents/Obsidian Vault/Job Search/Portfolio"
python3 build_web.py && python3 make_site.py
cd site && python3 -m http.server 8000
```

Then open `http://localhost:8000/`. `make_site.py` writes `site/index.html` with a doctype.
Needs Python 3 on macOS (it uses `textutil`). The build needs no other package.
Pillow is only needed if you make new images.

**Important:** `portfolio-web.html` has no `<!doctype>`, because it was made for the Claude page host. Do not open it directly. Its layout breaks in quirks mode. Use `site/index.html`. The other pages already have a doctype.

## How the build works (order)

1. `build_web.py` builds the landing page as one long string (hero, work list, six case studies, How I work, quote, About, Off the laptop, Contact).
2. `sky_theme.apply()` replaces the style block, the font link and the top bar and hero. It deletes the quote section.
3. `sky_theme.split()` cuts out the six case studies and the work list. It writes `projects.html` and the six `project-*.html` files. It returns the landing page without them.
4. `PEEK_JS` (the cartoon script) is added to the end of the landing page.
5. `build_web.py` writes `portfolio-web.html`, then `resume.html`, then calls `prd_pages.build()`.
6. `make_site.py` copies every page and only the images that the pages use into `site/`.

## Deploy to the public web

`make_site.py` builds the folder `site/`. It holds `index.html` (the landing page with a doctype and basic meta tags), all other pages, and only the images that the pages use (11 pages, 18 images, about 3.5 MB).
It is a plain static site. It needs no server code.
`make_site.py` clears `site/` on each run but keeps `.vercel`, `.vercelignore` and `.gitignore`. Those hold the Vercel link and the block on secret files.

```
python3 build_web.py && python3 make_site.py
cd site && npx vercel deploy --prod --yes
```

**Status on 28 Oct 2026: deployed** to `https://manyata-manocha.vercel.app` and checked on the live site (all pages load, all pictures load, no phone number, `/.env.local` returns 404).
Another static host works too (Netlify, GitHub Pages, Cloudflare Pages). Upload the `site/` folder.
After every deploy, check the live site:

```
curl -s https://manyata-manocha.vercel.app/ | grep -c "98998"      # must print 0
curl -s -o /dev/null -w "%{http_code}\n" https://manyata-manocha.vercel.app/.env.local   # must print 404
```

## Design (current)

- **Look:** sky-blue gradient at the top, white below. Three cream clouds drawn in CSS (`.cloud.c1` to `.c3`) that drift slowly and puff.
- **Boxes:** white, 2px black border, 5px hard black shadow, square corners.
- **Accent:** one orange, `--sun: #e46f3a`. Do not add a second accent color.
- **Fonts:** Space Mono for headings, IBM Plex Sans for body (Google Fonts).
- **Nav order:** About, Projects, Contact, Resume. Do not rename "Projects".
- **Images:** the project screenshots are WebP. Tiles use `*-t.webp` (640px). Project pages use `*.webp` (1400px). Keep them small. The Projects page was slow when they were big PNG files.
- **Motion:** respect `prefers-reduced-motion`. It is already in the CSS.
- **Phone:** the layout collapses to one column below 860px. Check every change at 500px wide.

## The cartoon (peeking girl)

**LIVE NOW: the 13-frame version (`wave-02.webp` to `wave-14.webp`, `CARTOON = 'frames'` in `sky_theme.py`).** She rejected the body + arm version ("the arm is coming separately"). Keep `CARTOON = 'frames'`. Do not change it without asking her.

(History) **Update (28 Oct, later):** Codex rebuilt the cartoon as a still body (`img/peek-body-v2.png`) plus a waving arm (`img/peek-arm-v2.png`), with `peek-animation.js` inlined by `sky_theme.py` and tests in `tests/peek-animation.test.cjs`. She rejected this version, so it is **not** live. The text below about `peek-clean.png` and the old frames is history.
Open request: she wants the **hand that grips the wall edge** (lower right of the body picture) removed. Pixel edits failed. It needs an image tool: make `img/peek-body-v3.png`, then switch `sky_theme.py` to it.
**Who deploys:** Codex edits and builds (`python3 build_web.py && python3 make_site.py`) but cannot reach the internet. Claude runs `cd site && npx vercel deploy --prod --yes` when Manyata says "deploy".

**Changed after the first handoff (by another tool, probably Codex):** the page now uses one clean picture, `img/peek-clean.png` (916x1716, no frames). `PEEK_JS` in `sky_theme.py` slides it in once when the page opens (950 ms, a small rotation, only `transform`). Click replays it. It does nothing for reduced motion, a hidden tab, or when it is off screen.
The old 15-frame wave (`img/wave-02.webp` to `wave-16.webp`) is no longer used. The files stay in `img/`. Do not delete them without asking.
The user asked to remove the "Hi!" bubble earlier. The new picture has no bubble.

## Rules from the user (follow them)

1. **Never invent facts.** Use only: `../Master Resume.md`, the two PRD Word files, the Paytm deck, the certificates, the live sites, and what she types. If a fact is missing, ask her.
2. **No phone number** anywhere on the site. `prd_pages.py` and the resume build already strip it. Keep it that way.
3. **Ask before you add or delete** content, sections or features.
4. **No background-removed (cut-out) photos.** She rejected them. Use whole photos with their real background.
5. **Keep the original cream CSS clouds.** She rejected the cartoon clouds.
6. **No quote or testimonial section.** She has no testimonials, and she removed the Shravan Tickoo quote. Do not add one.
7. **No photos from the internet.** Reference sites are inspiration only. Do not copy their art, text or layout. (Her references: deepalipathe.com for the sky and boxes. Her own cartoon is the mascot.)
8. **Adhikaar user numbers:** do not claim any. The live traffic is the team's own testing. Five interview participants used it.
9. **PwC dashboard:** do not name the client. Do not add a screenshot. It is client work.
10. **Write in short, plain sentences.** No slogans like "X, not Y". No marketing words.
11. The site must work on a phone.

## Facts and where they come from

- `PROJECTS` and `STORY` in `build_web.py`: her resume, her PRDs, the Paytm deck, the live sites.
- Adhikaar PRD: `~/Downloads/Adhikaar PRD.docx`. The page replaces the wrong "Week 4 · Learning Tech" heading with "Adhikaar · Government and public sector case study". The Word file itself still has the wrong heading.
- Vantage PRD: `~/Downloads/Vantage FINAL.docx`.
- The two Word files also hold pictures (Adhikaar: 2, Vantage: 4, in `word/media/`). The Vantage user flow, the Adhikaar verdict screenshot and the PRD-page pictures come from there.
- The Vantage roadmap comes from the PRD feature table (V1 / V1.1 / V1.2 / Cut). The Adhikaar claim journey comes from PRD section 3 (six stages, 0 to 6).
- **How I work** (5 steps in `STEPS`): checked against both PRDs on 28 Oct 2026. Every number is correct (9 interviews across 8 roles, 7 interviews, 53 and 268 tests, 2 of 17 testers).
- Photos: `~/Downloads/IMG_9266.jpeg` (airfield), `IMG_0938.jpeg` (hill).
- Contact: `manyata126@gmail.com`, `https://www.linkedin.com/in/manyata-manocha/`.

## Known gaps (open work)

1. **Testimonials:** she has none. Do not add a section.
2. **Wireframes:** optional. None exist beyond the Vantage user flow and the real product screenshots.
3. **Paytm pitch deck** is not in "Work samples". It names two teammates. Ask her first.
4. **Her role** in The Shravan's Round and in the Paytm team is not on the site. She has not said.
5. **Resume and PRD pages use the old sand and Nunito look,** not the sky look. They do not match the rest of the site.
6. **The PDF is out of date.** It has the older design. It lacks the skills, certificates, roadmap, user flow and Challenge/Approach/Result headings.
7. **Hamsty:** the site lists "AI reads a voucher picture". On the live demo that feature is off. She has not said if it should stay on the list.
8. **Wording:** the button "View my work" and the heading "How I work" still say "work". She renamed the nav link only.
9. **Optional:** link the words "Adhikaar" and "Vantage" in the How I work examples to their project pages. She asked if the section is okay (it is). She has not asked for the links.
10. **The Adhikaar homepage screenshot** (inside the PRD picture) shows "41 people visited Adhikaar in the last 30 days". She has not said if that picture should stay.
11. **Address:** she may want a custom domain or a shorter address.
12. **Unused files** in `img/` (old photos, cut-outs, cartoon clouds, `wave-02` to `wave-16`, `peek-1` to `peek-6`). They are safe to keep. Do not delete them without asking.

## Quick check before you finish any change

- Run `python3 build_web.py` with no error.
- Search the output for the phone number: it must find nothing.
- Open the landing, Projects and one project page at 1440px and at 500px.
- Click a project tile, then "Back to projects", then "Next".
- Check the cartoon slides in once, and does not move with reduced motion.
- After a deploy, run the two `curl` checks in the Deploy section.
