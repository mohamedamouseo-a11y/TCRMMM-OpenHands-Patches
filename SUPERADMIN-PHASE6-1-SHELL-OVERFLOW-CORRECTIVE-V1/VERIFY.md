# Phase 6.1 — Shell 10px Overflow Corrective V1

## Scope
Presentation-only corrective patch for the measured Super Admin shell horizontal overflow found by Phase 6 Final Responsive QA.

Observed before patch:
- 1440x900: `innerWidth=1440`, `clientWidth=1440`, `scrollWidth=1450` => 10px overflow.
- 1024x768: `innerWidth=1024`, `clientWidth=1024`, `scrollWidth=1034` => 10px overflow.
- Diagnostic source: stretched `.topbar` with desktop `margin-inline:10px`, producing geometry outside `.mainArea`.

The patch changes CSS geometry only. It must not alter APIs, DB, auth, routes, permissions, handlers, data, billing, subscriptions, or business logic.

## Preflight
1. Run `git status --short`.
2. Do not Reset, Clean, Restore, Commit, or Push.
3. Confirm Phase 6 marker exists exactly once:
   `SUPER_ADMIN_PHASE6_SETTINGS_FINAL_QA_V1`
4. Keep all current worktree changes.

## Apply
Run exactly once:

```bash
python3 apply_phase6_1.py
```

Confirm marker exists exactly once:

```bash
grep -c 'SUPER_ADMIN_PHASE6_1_SHELL_OVERFLOW_CORRECTIVE_V1' /var/www/TCRMMT/server/_core/index.ts
```

## Static verification
Run:

```bash
git diff --check
npm run check
npm run build
```

All must PASS before restart.

If all PASS, restart only `tamiyouz-crm`.

## Required Playwright verification
Use real Playwright/Chromium viewport emulation, not `window.resizeTo`.

Test at minimum:
- 1440x900
- 1024x768
- 768x900
- 600x900
- 390x844

At every viewport record:

```js
({
  innerWidth: window.innerWidth,
  clientWidth: document.documentElement.clientWidth,
  scrollWidth: document.documentElement.scrollWidth,
  overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth
})
```

### Mandatory acceptance
At 1440x900 and 1024x768:
- page-level overflow MUST be `0px`.
- `#appShell` must not expand document width.
- `.mainArea` must stay inside the shell width.
- visible `.topbar` bounds must remain inside `.mainArea`.
- intended desktop inset remains visually present.
- no clipping or overlap.

At 768x900, 600x900 and 390x844:
- existing `0px` page-level overflow must remain `0px`.
- mobile/compact topbar remains full-width and usable.
- hamburger/navigation remains usable.

## Regression spot check
Check:
- Overview
- Companies
- Users
- Plans / Commercial
- Activity
- Audit
- GitHub Sync
- Evolution API
- Tara APIs
- System Settings
- Tenant Drawer
- Sidebar expanded/collapsed where applicable
- Light/Dark

No functional behavior may change.

## Evidence required
Send:
1. 1440x900 Overview screenshot + overflow measurement.
2. 1024x768 Overview screenshot + overflow measurement.
3. 390x844 Overview screenshot + overflow measurement.
4. Settings at 390x844.
5. Final viewport PASS/FAIL matrix.
6. Results of `git diff --check`, `npm run check`, `npm run build`.
7. `git diff -- server/_core/index.ts` summary confirming CSS-only Phase 6.1 change.

## Stop conditions
If 1440 or 1024 still reports non-zero page-level overflow, do not add ad-hoc `overflow:hidden`/`overflow:clip` masking and do not change JS. Stop and report the exact geometry/element causing the remaining width.

Do not Commit or Push.
