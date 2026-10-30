# Codex Deployment Guide

This guide enables Codex (or any Claude Code environment) to deploy changes to the portfolio live.

---

## Setup (One-time)

### 1. Create Vercel Token

1. Go to: https://vercel.com/account/tokens
2. Click **"Create Token"**
3. Name: `codex-portfolio-deploy`
4. Scope: Leave as default (full account access)
5. Expiration: Leave as default
6. Click **"Create"** and copy the token

### 2. Add Token to Settings

Replace `ADD_YOUR_TOKEN_HERE` in `.claude/settings.json` with your actual token:

```json
{
  "env": {
    "VERCEL_TOKEN": "your_actual_token_here"
  },
  "permissions": [
    "bash",
    "npm"
  ]
}
```

---

## Deploy Changes (For Codex)

### Quick Deploy

When you have changes ready, run:

```bash
cd /Users/nikki/Documents/Obsidian/Job\ Search/Portfolio
python3 build_web.py
python3 make_site.py
cd site && npx vercel deploy --prod --yes
```

### What Each Step Does

- **`build_web.py`** - Generates HTML from Python (data, content, About text)
- **`make_site.py`** - Builds the full static site into `site/` folder
- **`vercel deploy --prod --yes`** - Pushes to production (live site)

---

## File Reference

**Content/Data Files:**
- `build_web.py` - Projects list, About section, Experience, all text content
- `img/` - All images (WebP optimized, JPG originals)

**Styling Files:**
- `sky_theme.py` - All CSS, responsive breakpoints, animations
  - Tile styling (border, background, padding)
  - Hero sizes (clamp values)
  - Section spacing (padding-block)
  - Colors (--line, --paper, --bg, etc.)

**Build/Deploy:**
- `make_site.py` - Site generator
- `.claude/settings.json` - Codex auth & permissions

---

## Common Codex Tasks

### Edit About Section
File: `build_web.py` (around line 575)
```python
<p class="lead reveal">A Delhite currently in Bengaluru...</p>
```

### Change Project Tiles
File: `sky_theme.py` (line ~401)
```css
.tile { 
  border: 6px solid #161616; 
  background: #ffffff; 
  padding: 24px;
}
```

### Adjust Font Sizes
File: `sky_theme.py`
- Hero h1: Line 60 — `clamp(36px, 7vw, 110px)`
- Section h2: Line 95 — `clamp(38px, 5vw, 64px)`

### Add/Update Images
1. Save image to `img/` folder
2. Reference in `build_web.py` (e.g., `<img src="img/photo.webp">`)
3. Run build & deploy

---

## Troubleshooting

**Build fails with "missing: ['img/...']"**
- Check image exists in `img/` folder
- Verify filename matches exactly in code (case-sensitive)

**Changes not live after deploy**
- Hard refresh browser: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)
- Check deploy succeeded (should see "Aliased https://..." in output)

**Token expired**
- Generate a new token at https://vercel.com/account/tokens
- Update `.claude/settings.json`

---

## Live Site Info

- **URL:** https://manyata-manocha.vercel.app
- **Project:** Vercel (automatic builds from `site/` folder)
- **Auth:** `VERCEL_TOKEN` env var handles all deployment
- **Domain:** `manyata-manocha.vercel.app` (manual upload to Vercel)

---

**Ready to deploy?** Just ask Codex to:
- Edit files (build_web.py, sky_theme.py, etc.)
- Run the deploy commands above
- Confirm changes are live at the URL

All automated. ✓
