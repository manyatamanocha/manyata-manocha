# Portfolio progress

Project: Manyata's AI Product Manager portfolio. Started 28 Oct 2026 (one long session).
Status: the site is **live and public** at `https://manyata-manocha.vercel.app` (Vercel). See "Latest status" below. The private Claude preview (version 41) is older and out of date.
For the technical details, see `HANDOFF-for-Codex.md` in this folder.

## Latest status (1 Nov 2026, commit f70bdc7)

This section replaces older notes below where they disagree.

**Where it is now**
- Live site: `https://manyata-manocha.vercel.app`. Source folder: `final/`. A push to `main` on GitHub (`manyatamanocha/manyata-manocha`) deploys it. The older `site/` folder and build scripts are not the live source.
- Saved copy of the live site: `Final version - 1 Nov 2026/` (49 files). It is a frozen copy. Do not edit or deploy from it. If the site changes, export it again with `git archive origin/main final`.
- The separate Projects page is gone. `/projects` redirects to the Work section on the landing page.

**What changed on 31 Oct and 1 Nov**
- **Hero:** new t-shirt photo (`img/hero-tshirt.webp`) in the gold frame. The three intro lines are now one paragraph at one size. On screens up to 860px the photo sits below the intro.
- **Colour:** the hero sky fades into a light sky-blue tint (`#dcedfa`) on the landing page and all 6 project pages. The resume and PRD pages keep their own style.
- **About:** heading made smaller and text justified. The text was expanded and split into 2 paragraphs, with a line break before "I want to understand". The pink shirt photo is framed and sits far left. The mountain photo is 20% bigger, beside paragraph 2. The sofa cartoon is beside the heading.
- **Contact:** rebuilt as "Let's Talk?" with the tagline, the peeking cartoon, and a bar with LinkedIn, the email address and Resume. Heading and buttons are 40% smaller. The Copy button is removed. The footer line is bold and 15% bigger, and it sits right under the bar.

**Decisions to keep**
- Email button: orange, shows `manyata126@gmail.com`, and opens an email. No Copy button. Parallel sessions changed this several times, so ask before touching it.
- The resume page has no email address.
- No phone number anywhere on the site.

**Still open (optional)**
- On phones the footer line wraps onto 3 lines, with "2026" alone on the last line.
- At tablet widths around 768px the Contact cartoon is only about 5px below the Experience cards.
- The old hero image `img/hero-cutout.png` is still used by two preview pages.
- Paragraph spacing and the About `.ab-text` rules in `index.html` have old leftovers that no longer do anything.

**Working notes**
- More than one session edits `final/` at once. Check `git status` and `git diff --cached --stat` before each commit, and commit only your own change.
- Test layout changes at phone, tablet and desktop widths. Absolute positioning in About and Contact breaks easily.

## Where things are

| Item | Place |
|---|---|
| Live site (public) | `https://manyata-manocha.vercel.app` |
| Upload folder | `site/` (built by `make_site.py`) |
| Old private preview | `https://claude.ai/artifact/3bS1Vr4oNwpVc1UCbw8UrR` |
| Build scripts | `build_web.py`, `sky_theme.py`, `prd_pages.py`, `make_site.py` |
| Built pages | `portfolio-web.html`, `projects.html`, `project-*.html`, `resume.html`, `prd-*.html` |
| Old PDF | `Manyata_Manocha_AI_PM_Portfolio.pdf` (source: `portfolio.html`) |
| Pictures | `img/` |
| Her resume | `../Master Resume.md` |

## What the site has now

- **Landing page:** "Hello, I'm Manyata Manocha", her intro, the peeking cartoon, three drifting clouds, How I work (5 steps), About (experience, awards, education, certificates, skills), Off the laptop (2 photos), Contact.
- **Projects page:** 6 tiles. A "Work samples" row with both PRDs and the resume.
- **6 project pages**, each with Challenge, Approach and Result: PwC Risk Screening Dashboard, Adhikaar, Vantage, The Shravan's Round, Hamsty, AI Teammates (Paytm hackathon).
- **2 PRD pages and a resume page** made from her own files.

## Source material she gave

- Two PRDs: `Adhikaar PRD.docx` and `Vantage FINAL.docx` (an earlier "Final Adhikaar PRD.docx" was empty).
- Briefs: Rethink Systems case studies (Week 5 Case Study 4 for Vantage, C8 government for Adhikaar), the Buildathon brief.
- Paytm hackathon: Luma page and the pitch deck `Team Rethinkers.pdf`.
- Certificates: Top Operator (Certificate of Excellence) and 2nd place (Rethink AI-First Buildathon).
- Her photos, her cartoon sheets and her own intro text.

## Timeline of the main decisions

1. **Format:** she chose a PDF first (bold and colorful, general AI PM). Then she asked for a website too.
2. **Projects chosen:** Adhikaar, Vantage, Hamsty. She then added The Shravan's Round (2nd place), the Paytm hackathon, and the PwC dashboard (from the PM-portfolio video advice).
3. **Look changed many times.** Bold colors, then premium dark serif, then warm sand, then the current sky look. Each time she gave a reference or said what she disliked. See "Rejected".
4. **Layout:** one long page became a landing page, a Projects page with tiles, and one page per project.
5. **Photos:** she sent several. Cut-outs looked bad, so the site uses whole photos only. The mascot is her own cartoon.
6. **Cartoon:** she sent sheets of frames. The final one was a 16-frame sheet. The site first used 15 frames, without the "Hi!" bubble. After the deploy, another tool (probably Codex) changed it to one clean picture (`img/peek-clean.png`) that slides in once. The live site has that version.
7. **Audit:** the site was checked against theproductfolks.com "PM portfolio essentials". She approved three additions (skills and certificates, work samples row, same headings in every case study). Later she approved a roadmap, a claim journey and the PRD pictures (see below).
8. **Deploy:** she asked to make it public. It went live on Vercel the same day.
9. **How I work check:** she asked if the section is okay. It was checked against the PRDs: all five steps and all numbers are correct. No change was made.

## Deployed

- 28 Oct 2026: she signed in to Vercel. The site was deployed to production as project `manyata-manocha`. Pages, resume and both PRDs are public. No phone number is on any page (checked on the live site). The secret file Vercel made (`.env.local`) was deleted before upload and is blocked by `.vercelignore`.
- To update: edit the scripts, run `python3 build_web.py && python3 make_site.py`, then `cd site && npx vercel deploy --prod --yes`.
- Deployed three times on 28 Oct: first launch, then the roadmap and journey pictures, then the PRD pictures. The last deploy has all 11 pages and 18 images (about 3.5 MB). All checked on the live site.
- After the first deploy, the cartoon was changed to a single picture (`peek-clean.png`) by another tool. The live site has that version.
- The lower cloud was moved away from the cartoon (it drifted behind her): `.c3 { left: 52%; top: 80% }` in `sky_theme.py`.

## Added after the PM-portfolio checklist

- Skills and tools, Lean Six Sigma Green Belt, Staff Advisory Council (About).
- "Work samples" row on the Projects page (both PRDs and the resume).
- Challenge, Approach and Result on every project page.
- A **roadmap picture** on the Vantage page (V1 shipped, V1.1 next, V1.2 later, Cut). Source: the PRD feature table. Code: `ROADMAP_VANTAGE` in `build_web.py`.
- A **claim-journey picture** on the Adhikaar page (seven stages, stages 3 and 4 highlighted). Source: PRD section 3. Code: `JOURNEY_ADHIKAAR` in `build_web.py`.
- Both are live. The Paytm pitch deck was **not** added (her teammates' names).
- Pictures taken from her own PRD Word files (the pictures inside the .docx): the **Vantage user-flow diagram** is on the Vantage page. The **Adhikaar nominee-verdict screenshot** is on the Adhikaar page. All 2 Adhikaar and 4 Vantage pictures are back inside the two PRD pages, each above its own caption (`add_figures()` in `prd_pages.py`). Files: `img/vantage-userflow.webp`, `img/prd-vantage-2..4.webp`, `img/prd-adhikaar-1..2.webp`. All live.
- She has no testimonials. The site has no testimonial section. That is fine.
- The pictures are linked: click a picture to open it full size.

## Rejected by her (do not bring back)

- Cut-out (background-removed) photos.
- The Robin Noguier look (charcoal, crimson, serif) and its layout. She asked to remove it.
- The warm sand look ("shit colours, shit layout").
- The magnifying-glass effect ("of no use").
- Cartoon clouds. She wants the original cream CSS clouds.
- The Shravan Tickoo quote section.
- The "Hi!" bubble on the cartoon ("comes very late").
- The line "Different field. Same curiosity. Bigger possibilities."
- The "manyata.pm" label in the top bar.
- A phone number anywhere on the site.

## Rules she set

- Never invent facts.
- Ask before adding or deleting.
- No photos from the internet. References are inspiration only.
- Short, plain sentences.

## Problems found and fixed

- The Projects page was slow: the screenshots were 3.2 MB. They are now about 60 KB in WebP.
- The cartoon lagged: frames were swapped by `src`. They are now stacked and shown by class. A bug stopped the animation from starting. It was fixed.
- `prd_pages.py` was once emptied by a bad command. It was rewritten.
- Vercel made a secret token file (`site/.env.local`) when the project was linked. It was deleted before the first upload, and `.vercelignore` now blocks `.env*`.
- The PRD pages had lost all pictures when the Word files were converted. They are back (matched by caption).
- The Adhikaar PRD file has a wrong template heading ("Week 4 · Learning Tech"). The web page fixes it. The Word file still has it.

## Open items

1. Her role in The Shravan's Round and in the Paytm team (not on the site).
2. The Paytm pitch deck in "Work samples" (she must confirm that her teammates' names can be public).
3. Make `resume.html` and the PRD pages match the sky look.
4. Rebuild the PDF to match the website, or retire it.
5. Hamsty: the AI picture reading is off on the live demo. Should it stay on the feature list?
6. "View my work" and "How I work" still say "work".
7. Optional: link "Adhikaar" and "Vantage" in the How I work examples to their project pages.
8. The Adhikaar homepage screenshot in the PRD shows "41 people visited Adhikaar". Keep it or drop it?
9. A custom domain or a shorter address than `manyata-manocha.vercel.app`.
10. Her full-size pink-shirt photo, if she wants it used (the first one was only 656 px wide and looked soft).
11. Watch the cartoon on a real phone and tell us if it lags.
13. **Cartoon, 28 Oct (later) - REVERTED.** She said Codex's body + separate arm version looked worse ("the arm is coming separately"). Claude restored the **13-frame version** (`img/wave-02.webp` to `wave-14.webp`) and deployed it. `sky_theme.py` has a switch: `CARTOON = 'frames'` (live) or `'layers'` (Codex's version, kept in the code). Do not switch back to `'layers'` without her OK. History of the Codex version: another tool (Codex) rebuilt the cartoon as a still body (`img/peek-body-v2.png`) plus a separate waving arm (`img/peek-arm-v2.png`), with `peek-animation.js`, `tests/peek-animation.test.cjs` and its notes in `Animation update.md`. Claude deployed this version on 28 Oct 2026 (after Codex built it and reported "build passed, tests passed, not deployed"). Claude checked the resting look at desktop and phone width, and the arm placement with the arm forced visible: it lines up. The wave animation itself was not seen in motion. (Not live any more.) The frame version is live, and it still has the edge-gripping hand.
31. **About spacing (28 Oct, LIVE):** she saw empty space under "Staff Advisory Council Member". Fix: last list item has no bottom padding, `.info-box` bottom padding 18 px (was 22), `.about` bottom padding 70 px (was 110).
30. **Section order and first screen (28 Oct, LIVE):** the landing page now goes Projects (tiles, added by Codex) THEN How I work (the order is set in `split()` in `sky_theme.py`). The top section is as tall as the window (`.sky-hero { min-height: max(520px, calc(100svh - 86px)) }`) so Projects, How I work and the laptop girl are below the fold on desktop and phone (measured at 1440x900, 1440x700, 1280x720, 390x844, 500x800). `.home-work` padding 80/90, `.how` padding-top 70.
    **Facts note:** the PwC tile shows 67% (30 to 10 min per case, up to 25 cases a week). That comes from her UPDATED resume line (it was 75% / 40 to 10 min in the first version). `build_web.py` already has the new numbers.
29. **Location line added (28 Oct, LIVE):** "Bangalore · open to PM roles" under the intro, above the buttons (`<p class="where">` in `sky_theme.py`). Her words. Bangalore matches her resume.
28. **Laptop drawing moved right (28 Oct, LIVE):** `.how-pic { right: -34px }` on desktop and `right: -10px` on phone (was -10 and 2) so the drawing sits on the top-right corner of the first How I work box.
27. **Phone too (28 Oct, LIVE):** she meant the phone view. `@media (max-width: 860px) { .peek { top: -50px } .wrap .sky-hero { padding-top: 200px } }` in `FRAMES_CSS`: the peeking picture and the text are 50 px higher on phones. NOTE for later: when she says "move up", ask or change both desktop and phone.
26. **Cartoon 30 px higher on desktop (28 Oct, LIVE):** `@media (min-width: 861px) { .peek { top: -10px } }` in `FRAMES_CSS`, to match the text block that moved up 30 px. Phone unchanged.
25. **Layout polish (28 Oct, LIVE):** (a) second intro sentence on its own line (`<br>`), intro `max-width: 46em` so it fits one line on desktop. (b) Hero text block moved up 30 px on desktop (`.hero-copy { top: -30px }` at min-width 861 px). Top-left cloud moved up (`.c1 top: -18px`). (c) Empty space between the intro and How I work reduced: `.sky-hero` now `min-height: 520px; padding-block: 72px 40px` (this also REMOVED Codex's `min-height: max(520px, 100svh)` full-screen hero; the live site never had it), `.how { padding-top: 70px }` (was 190). (d) Phone: lower cloud moved to `bottom: 16px; right: 4%` so it does not sit behind the Resume button.
    **Correction:** right after this deploy a parallel edit put `min-height: max(520px, 100svh)` back into the source, so the first deploy still had the big gap. It was removed again and redeployed. Check `grep -c 100svh site/index.html` is 0 before every deploy.
    **Note:** Codex also added a laptop illustration on top of How I work step 1 (`PIC_FOR` in `build_web.py`, `img/laptop.webp`, `.how-pic`). It is live. She has not said if she wants it.
24. **Intro shortened (28 Oct, LIVE):** she asked to remove the PRD-labelling and "numbers are small" sentences. The intro is now two sentences: "Today I build AI products and write the PRDs for them. I came from fraud investigation, so I do not trust an answer until I can show the evidence."
23. **Cartoon 3% faster (28 Oct, LIVE):** step times now `[163,265,153,153,174,174,153,153,1120]` ms (first play) and `[153,153,174,174,153,153,1120]` ms (click replay).
22. **New intro, Option B (28 Oct, LIVE):** she chose Option B and asked to start from what she does now. Text (one paragraph, in `sky_theme.py` NAV): "Today I build AI products and write the PRDs for them. I came from fraud investigation, so I do not trust an answer until I can show the evidence. In my PRDs, every finding is marked: a person said it, I think it, or I still assume it. I build what I write about, and I say so when the numbers are small." The bold line above it stays. The old two paragraphs are gone. The facts come from her PRDs (SAW / THINK / ASSUME labels). Cartoon speed: every step 5% slower (168/273/158/158/179/179/158/158/1155 ms).
21. **5% smaller cartoon (28 Oct, LIVE):** `.peek { translate: 14% 0; scale: .95; transform-origin: 100% 50%; }` in `FRAMES_CSS` (`sky_theme.py`). Measured height 620 px to 589 px at 1440 px width.
20. **Slower and smoother (28 Oct, LIVE):** the sprite sequence now uses more in-between hand positions. First play: sprite positions `[0,1,2,3,4,5,6,11,12]` with `[160,260,150,150,170,170,150,150,1100]` ms. Replay (click): `[2,3,4,5,6,11,12]`. Still one wave with one tilt, then the wink.
19. **Sprite sheet (28 Oct, LIVE):** she said the wave still lagged. The 13 stacked frames were replaced by ONE picture, `img/peek-sprite.webp` (13 frames side by side, 3055x440, 265 KB). `FRAMES_BUTTON`/`FRAMES_CSS`/`PEEK_JS_FRAMES` in `sky_theme.py` now only change `background-position-x`. Sequence: sprite positions 0,1 (peek), 2,3,4 (hand up, one tilt), 11,12 (wink), rest on 1; click replays 2,3,4,11,12. No fades, no frame switching. Verified: correct order in a test, wave and wink frames render, live deploy checked. The old `wave-*.webp` files are not used by the page any more.
    **Deploy note:** to keep the live layout, the deploy copy of `site/index.html` had `max(520px, 100svh)` replaced by `520px` (Codex's full-screen hero change stays OUT of the live site). The next rebuild brings Codex's change back unless she approves it or it is undone in `sky_theme.py`.
18. **Lag attempt, NOT deployed (28 Oct):** she said the cartoon was "better but lag". Claude tried decoding all 13 frames before starting (`decode()` + `will-change`). In the test the cartoon turned pale/see-through after the animation, so it was undone. **Live = the fingertips-fixed version (`cleanT`), which tested clean.** Idea not tried: preload the frames with `<link rel=preload>` in the page head, or merge the 13 frames into one sprite sheet and move it with `background-position` (no image switching at all).
    **Local folder is ahead of live:** another tool (Codex) changed `sky_theme.py`: `.sky-hero { min-height: max(520px, 100svh) }` (hero fills the screen, so the headline sits lower). It is in `site/` but **not deployed**. Ask her before deploying.
17. **Fingertips bug (28 Oct, live):** after the wink, the previous frame stayed under the resting frame (`.pf.under` was never cleared), so the waving hand's fingertips showed past the hair. Fixed in `show()`: the `under` class is removed 100 ms after each switch (`cleanT`). Also shortened the wave to `wave = [2,3,4,11,12]`.
16. **Cartoon, final tuning (28 Oct, live):** (a) one wave only: frames `wave = [2,3,4,5,6,11,12]` in `PEEK_JS_FRAMES`, 120 ms each, wink held 1000 ms. (b) Smooth without blinks: the new frame fades in over 90 ms ON TOP of the old frame (`.pf.under` stays opaque), so the sky never shows through. Measured: 0 frames with a gap. (c) Position: `.peek { translate: 14% 0 }` (was 17%). At 10% the edge-gripping hand's knuckles show; 13% was the limit on desktop, 14% adds margin for phones. (d) Plays once on load and on click, no auto-repeat.
    **Warning:** a small cartoon head appeared in the How I work area (`HOW_PIC` in `build_web.py`). Claude did not add it. Probably Codex. Ask her if she wants it.
    **Warning:** `build_web.py` once had a syntax error from a parallel edit, which made `cd site` skip and `vercel deploy` run in the Portfolio folder. Vercel rejected it (capital P in the name), so nothing was uploaded. Always run the deploy as `cd site && npx vercel deploy --prod --yes` and check `pwd` first.
15. **Cartoon motion calmed (28 Oct, live):** she saw white blinks and too much movement. The blinks came from the 70 ms crossfade (two half-transparent frames show the sky). Fix in `sky_theme.py`: frames switch instantly (`transition: none`), no slide-in, no automatic repeat. The wave plays once on page load and again on click only. Tested: exactly one frame visible at all times.
14. **Hand fix (28 Oct, live):** ChatGPT's limit was reached, so no new artwork was possible. Claude hid the gripping hand with CSS instead: `.peek { translate: 17% 0; }` in `FRAMES_CSS` (`sky_theme.py`) pushes the cartoon 17% past the screen edge. The face stays visible. A cleaner fix is still a redrawn picture without that hand. Earlier text on this item:
    **She asked to remove the other hand** (the one gripping the wall edge, lower right of `peek-body-v2.png`). Two pixel-editing attempts by Claude left visible patches, so they were dropped and the file was restored. It needs an image tool: she gets a prompt to make `img/peek-body-v3.png`. After that: switch `sky_theme.py` to `peek-body-v3.png`, check desktop and phone, run `python3 build_web.py && python3 make_site.py`, then deploy.
12. Optional: wireframes or prototype screens, only if she has them.

Closed: testimonials (she has none), the roadmap and user-flow pictures, deploying, the Projects page speed.
