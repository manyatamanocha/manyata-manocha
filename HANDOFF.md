# Portfolio Handoff for Codex

**Date:** 28 Oct 2026  
**Project:** Manyata Manocha Portfolio — AI PM  
**Live URL:** https://manyata-manocha.vercel.app

---

## Session Summary

Built and iterated on the AI PM portfolio site with focus on About section, tile styling, and image management.

### Changes Made This Session

1. **About Section Text**
   - Updated to: "A Delhite currently in Bengaluru, building AI products that solve real problems..."
   - File: `build_web.py` (line ~575)

2. **Project Tiles Styling**
   - Added explicit white boxes with thick black borders
   - Border: 6px solid #161616 (black)
   - Background: #ffffff (white)
   - Shadow: 8px 8px 0 #161616
   - Padding: 24px
   - File: `sky_theme.py` (line ~401)

3. **Images**
   - Added mountain photo to About section: `img/about-mountain.jpg`
   - Portrait photo: `img/portrait-about.webp`
   - Both display in collage layout in About section
   - File references in `build_web.py` (line ~579-580)

### Current State

✓ **Live & Deployed**
- All changes pushed to Vercel
- Site renders correctly on desktop
- Tile borders visible (white boxes with black 6px borders)
- About section shows both portrait and mountain photos in collage

### Key Files

```
/Users/nikki/Documents/Obsidian Vault/Job Search/Portfolio/
├── build_web.py          # Project data, About section HTML, PROJECTS array
├── sky_theme.py          # All CSS, tile styling, responsive breakpoints
├── make_site.py          # Build script (generates site/ folder)
├── img/
│   ├── portrait-about.webp
│   ├── about-mountain.jpg
│   ├── adhikaar.png, vantage.png, shravan.png, hamsty.png (project thumbs)
│   └── ...other assets
└── site/                 # Generated HTML (deployed to Vercel)
```

### Build & Deploy Commands

```bash
# From /Users/nikki/Documents/Obsidian Vault/Job Search/Portfolio/
python3 build_web.py      # Generates landing page HTML
python3 make_site.py      # Builds full static site
cd site && npx vercel deploy --prod --yes  # Deploy to Vercel
```

---

## Known Issues & Notes

- **No git repository:** The portfolio folder is not a git repo. Changes are tracked via Vercel deployments only.
- **Image optimization:** WebP conversion happens in build process; ensure originals are high-quality JPGs.
- **Responsive design:** Tested at desktop only this session. Mobile breakpoints defined at `md: 768px`.

---

## Next Steps (Optional)

1. **Add animation?** User rejected book page-turning interface, prefers static grid
2. **Mobile test:** Verify responsive layout on actual phone
3. **More photos?** About section currently has 2 images; can add more
4. **Projects page:** Full individual project pages exist on /projects.html

---

## Contact & Context

User: Manyata Manocha  
Email: manyata126@gmail.com  
Focus: AI Product Manager portfolio for job search (fintech, Bengaluru/Gurugram roles)

**Design principles observed:**
- Bold black borders + white background = high contrast
- Monospace fonts (Space Mono) for headlines
- STE (Simplified Technical English) style
- No slop, clean brutalist aesthetic
- Plain explanation (not metaphors)

---

**Status:** Ready for next iteration or review. All code is live and committed via Vercel deployments.
