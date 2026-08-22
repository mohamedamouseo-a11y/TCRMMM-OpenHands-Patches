# Phase 2.1 — Responsive No-Clipping Verification

Target: `/var/www/TCRMMT`

## Scope
Presentation-only corrective for the existing Super Admin Executive Command Center. Do not change DB, APIs, Auth, Routes, Permissions, data handlers, or Business Logic.

## Required baseline
The target must already contain:
- `SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1`
- `SUPER_ADMIN_PHASE1_2_DENSITY_LAYOUT_CORRECTIVE_V1`
- `SUPER_ADMIN_PHASE2_EXECUTIVE_COMMAND_CENTER_V1`

## Execute
1. `git status --short`
2. Do not reset/clean/restore pre-existing work.
3. Run `python3 apply_phase2_1.py` once.
4. Confirm marker `SUPER_ADMIN_PHASE2_1_RESPONSIVE_NO_CLIPPING_V1` exists once only.
5. Run:
   - `git diff --check`
   - `npm run check`
   - `npm run build`
6. Restart only `tamiyouz-crm` if build passes.

## Visual acceptance
Test at desktop, tablet, and mobile-like widths if the browser allows it.

### Overview
- No cropped text, cards, badges, buttons, KPI rows, or dynamic lists.
- No fixed-height clipping in Overview containers.
- Smart Insights: 4 columns wide desktop, then 2, then 1.
- Executive Ribbon: 3 columns wide desktop, then 1 at narrow width.
- KPI Details open/close without crop or overflow.
- Quick Actions: 6 compact actions wide desktop, then 3, then 1.
- Support area: full-width Quick Actions followed by clean 2-column insight area on desktop, 1-column on narrow screens.
- Search, Alerts, Usage, Security stay readable. Long lists may scroll internally, but parent cards must not clip them.
- Activity remains compact and readable.

### Shell
- Sidebar approx 208px expanded and 68px collapsed.
- Collapse/expand and persistence still work.
- Topbar does not crop labels or overflow.
- `document.documentElement.scrollWidth <= window.innerWidth` in tested states.
- Light and Dark both work.

### Regression spot checks
- Companies
- Users
- GitHub Sync
- Evolution API
- Activity
- Settings

## Screenshots
Capture at least:
1. Overview desktop above fold.
2. Overview desktop with KPI Details open.
3. Overview narrower width showing 2-column behavior.
4. Overview narrow/mobile-like showing 1-column behavior.
5. Overview with sidebar collapsed.

## Stop condition
Do not Commit or Push. Return a concise validation report and screenshots, then stop.
