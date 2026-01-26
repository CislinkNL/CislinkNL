# CV Sender - Interactive Demo

Interactive portfolio showcase page for Junyi Zhu - Python Expert / Developer application to Sopra Steria.

## Files

- **cv-sender.html** - Single-page interactive portfolio (Dutch/English)
- **env.yaml.template** - Configuration template (DO NOT fill in real credentials)
- **.gitignore** - Prevents sensitive files from being committed

## Setup

1. Copy `env.yaml.template` to `env.yaml` (for local use only)
2. Open `cv-sender.html` in a browser to test

## Deployment Options

### Option 1: GitHub Pages (Recommended)
1. Push this folder to your GitHub repository
2. Enable GitHub Pages in repository settings
3. Access at: `https://cislinknl.github.io/cv-sender/cv-sender.html`

### Option 2: Firebase Hosting
```bash
firebase login
firebase init hosting
firebase deploy
```

### Option 3: Direct Link
Host on any web server and share the direct URL.

## Security Notes

⚠️ **NEVER commit `env.yaml` with real credentials!**

The `.gitignore` file is configured to prevent:
- `env.yaml` (contains passwords/API keys)
- `assets/*.pdf` (personal documents)
- Service account files

## Features

- ✅ Responsive design (mobile-friendly)
- ✅ Dark theme gradient background
- ✅ Interactive project showcases
- ✅ Contact information with mailto links
- ✅ GitHub portfolio integration
- ✅ AI workflow explanation

## Tech Stack

- Pure HTML/CSS/JavaScript (no build step required)
- Responsive CSS Grid layout
- Gradient animations
- Glassmorphism card design

---

*Built for Sopra Steria application - Groningen, 2026*
