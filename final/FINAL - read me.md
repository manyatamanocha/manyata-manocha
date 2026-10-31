# Portfolio: final version

This folder holds the live website. It is the only version that is deployed.

- Live site: https://manyata-manocha.vercel.app
- GitHub: https://github.com/manyatamanocha/manyata-manocha (branch `main`)
- Open `index.html` to see the home page on this Mac.

## How to deploy
- Vercel deploys on each push to `main`. The Vercel Root Directory is `final`.
- Run `git push origin main` from the `Portfolio` folder.
- Edit only the files in this `final` folder. Do not make a second copy of the site.
- After each push, open the live site and check it. Hard refresh with Cmd+Shift+R.

## Pages and files
- `index.html`: the home page. It has the hero, projects, How I work, About, Experience and Contact.
- `project-pwc.html`, `project-adhikaar.html`, `project-vantage.html`, `project-shravan.html`, `project-hamsty.html`, `project-teammates.html`: one case study for each project.
- `prd-adhikaar.html`, `prd-vantage.html`: the two PRDs.
- `resume.html`: the resume.
- `cards.css`: the project cards on the home page.
- `about.css`, `about.js`: the About section. `about.js` only slides the corner pictures in.
- `vercel.json`: sends the old `/projects.html` link to the project cards on the home page.
- `img`: all pictures. The project cards use `adhikaar.webp`, `vantage.webp`, `shravan.webp`, `hamsty.webp`, `poster-pwc.webp` and `poster-teammates.webp`.

## Changes on 31 Oct 2026
- The "Based in Bangalore" box sits on the corner of the hero photo frame (left -37px, bottom -6px).
- The project display went through several designs. The final design is a grid of project cards. Each card shows the product name, a screenshot, what Manyata built, and a button. The cards have a gold edge (#c9a227) and sit slightly raised. They lift more on hover.
- The button says "View case study and PRD" for Adhikaar and Vantage. It says "View case study" for the other four. Only those two projects have a PRD.
- PwC and AI Teammates have no real screenshot. Their cards use pictures that were drawn for this site.
- The separate Projects page is removed. All project links go to the project cards on the home page.
- The top nav reads: About, Projects, Work, Contact, Resume. "Work" goes to the Experience section.
- The About section was rebuilt: a large heading, two paragraphs, and corner pictures that slide in. The scroll text effect on the first paragraph is removed. The mountain photo is next to the second paragraph.
- The mountain photo was reduced from 6.2 MB to 0.14 MB (`about-mountain-s.jpg`). The page loads faster.

## Known open items
- The hero photo `hero-cutout.png` is 1.6 MB. It slows the first screen. It can be made smaller with no change in look.
- Two old files are not linked from anywhere: `preview-projects-slider.html` and `preview-projects-stacked.html`.
- The old pages and the `site` folder were moved to the Mac Trash on 31 Oct (folder "Portfolio old version 31 Oct").
- The GitHub repo was public on 31 Oct. It holds the resume, a PDF and handoff notes. Make it private in the repo settings.
- Two GitHub tokens were shown in a chat on 31 Oct. Delete them at https://github.com/settings/tokens.
- The site has no favicon.

## History before 31 Oct
- 28 Oct: first version live.
- 29 Oct: two top clouds moved 40px down.
- 30 Oct: full-body photo added to the hero, with a gold frame and a scroll arrow at the bottom of the first screen.
