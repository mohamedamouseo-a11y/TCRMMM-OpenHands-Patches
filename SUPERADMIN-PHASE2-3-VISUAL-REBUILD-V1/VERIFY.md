# Phase 2.3 — Super Admin Visual Rebuild V1

## Scope
Presentation-only visual rebuild for the Super Admin Overview and shell. Preserve all IDs, handlers, APIs, routes, auth, permissions, DB behavior, and business logic.

## Pre-check
- Run `git status --short`.
- Do not reset, clean, restore, or overwrite unrelated/pre-existing worktree changes.
- Required baseline markers must exist: Phase 1.1, Phase 1.2, Phase 2, Phase 2.1, Phase 2.2.

## Apply
Run once:

```bash
python3 apply_phase2_3.py
```

The script is marker-guarded and must not duplicate the CSS block.

## Required validation
```bash
git diff --check
npm run check
npm run build
```

Only if all pass, restart `tamiyouz-crm` only.

## Visual acceptance criteria
- No giant decorative circles/blobs in Executive Ribbon or hero.
- Hero is visibly shorter and flatter.
- 4 primary KPI cards on desktop are compact and balanced.
- Executive Ribbon is a clean 3-card strip.
- Quick Actions behave like a compact command bar, not tall feature cards.
- Sidebar is visually lighter and approximately 196px expanded / 64px collapsed on wide desktop.
- Topbar is thinner and balanced.
- Main dashboard reading width is approximately 1240px max on large desktop.
- Typography has stronger hierarchy and contrast.
- Support cards are flatter, tighter, and free from giant empty spaces.
- No text/card/button/badge clipping.
- No horizontal page overflow.
- Light and Dark modes remain usable.
- Sidebar collapse/expand and persistence remain functional.

## Regression spot checks
- Companies
- Users
- GitHub Sync
- Evolution API
- Activity
- Settings

## Evidence screenshots
1. Overview desktop above fold.
2. Full Overview showing support deck.
3. KPI Details open.
4. Dark mode.
5. Sidebar collapsed.

Do not commit or push from the server. Stop after reporting results and screenshots.
