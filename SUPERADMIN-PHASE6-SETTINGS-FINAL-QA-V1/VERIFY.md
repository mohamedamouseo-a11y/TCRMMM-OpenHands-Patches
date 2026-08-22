# Phase 6 — Settings + Final QA V1

## Scope
Presentation-only final pass for Super Admin System Settings plus full regression/visual QA across Phases 1–5.1.

## Patch target
- `/var/www/TCRMMT/server/_core/index.ts`

## Must not change
- DB
- API
- Auth
- Routes
- Permissions
- Business Logic
- Billing/Subscription logic
- Existing IDs or JavaScript handlers

## Preflight
1. Run `git status --short`.
2. Do not Reset/Clean/Restore any existing worktree changes.
3. Confirm Phase 5.1 marker exists once:
   `SUPER_ADMIN_PHASE5_1_TENANT_DRAWER_OVERFLOW_FIX_V1`
4. Apply `python3 apply_phase6.py` once.
5. Confirm Phase 6 marker exists once:
   `SUPER_ADMIN_PHASE6_SETTINGS_FINAL_QA_V1`

## Static validation
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

All must PASS before restart.

## Settings acceptance
Open System Settings from the sidebar and validate:
- Drawer opens/closes normally.
- ESC closes it.
- Backdrop closes it.
- Appearance section is compact and readable.
- Dark/Light buttons work.
- Account section loads and remains readable.
- Owner-only Source Code panel keeps its permission gate.
- Source Code refresh/download controls retain current behavior.
- Logout button retains current behavior.
- Focus-visible state is clear for keyboard navigation.
- No clipping.
- No page-level horizontal overflow.
- Long account/source values wrap safely instead of expanding the drawer.

## Full Super Admin final QA
Validate at least these surfaces:
1. Overview / Executive Dashboard
2. Companies
3. Tenant Details drawer and all major tabs
4. Users
5. Platform Admins
6. Plans Catalog
7. Plans Editor
8. Companies / Overrides
9. Commercial / Subscriptions / Billing
10. Activity
11. Audit Log
12. GitHub Sync
13. Evolution API
14. Tara APIs
15. System Settings

For every surface verify:
- No clipped text/cards/actions.
- No page-level horizontal overflow.
- Internal table scrolling is allowed where intended.
- Sidebar expanded/collapsed works and persists after reload.
- Navigation opens the correct surface.
- Light/Dark both remain readable.
- Existing buttons/filters/tabs/drawers still respond.
- No obvious console errors caused by the UI work.

## Responsive matrix
Perform real viewport checks where the browser tooling allows:
- 1440×900
- 1024×768
- 768×900
- 600×900 (explicitly closes the deferred <620px QA gap)
- 390×844

At 600px and 390px specifically verify:
- Sidebar/mobile navigation does not cover inaccessible content.
- Settings drawer fits inside the viewport.
- No horizontal page scroll.
- Buttons do not overlap.
- Tables scroll internally rather than stretching the page.

## Overflow measurement
On each key viewport run a browser-side measurement equivalent to:
`document.documentElement.scrollWidth - document.documentElement.clientWidth`
Expected page-level result: `0`.

If any non-zero result exists, identify the exact DOM element causing it before considering Phase 6 PASS.

## Required evidence
Provide screenshots for:
1. Settings — Desktop Light
2. Settings — Desktop Dark
3. Settings — 600px viewport
4. Settings — 390px viewport
5. Overview — Desktop
6. Companies — Desktop
7. Users — Desktop
8. Plans / Commercial
9. Activity / Audit
10. GitHub Sync
11. Evolution API
12. Tara APIs
13. Tenant Drawer open
14. Sidebar collapsed

Also provide a compact final matrix with PASS/FAIL for every surface and viewport tested, plus measured page overflow.

## Stop conditions
- Do not commit.
- Do not push.
- If any functional regression appears, stop and report it rather than altering business logic.
- If the patch baseline markers/IDs do not match, stop without forcing changes.
