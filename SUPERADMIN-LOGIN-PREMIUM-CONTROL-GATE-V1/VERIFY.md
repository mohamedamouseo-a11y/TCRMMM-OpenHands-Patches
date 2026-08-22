# Super Admin Premium Login Control Gate V1 — Verification

Target: `/var/www/TCRMMT`

## Scope
Presentation-only Login UX/UI refinement for `/super-admin`.

Do not modify DB, API, Auth, Routes, Permissions, Business Logic, password recovery logic, IDs, event handlers, or authenticated Super Admin screens.

## Apply

```bash
python3 apply_login_premium_gate_v1.py
```

## Static checks

```bash
git diff --check
npm run check
npm run build
```

## Runtime acceptance

Use Playwright/Chromium with real viewport emulation.

Test unauthenticated `/super-admin` at:

- 1440x900
- 1024x768
- 768x900
- 390x844

For each viewport confirm:

1. `#loginView` is visible.
2. `#appShell` is not visually rendered while unauthenticated.
3. No Usage, Global Search, Security, tenant, plan, activity, audit, or integration cards appear below/behind the Login gate.
4. Page-level horizontal overflow is 0px.
5. Email, Password, Show password, Forgot password and Sign In are visible and usable.
6. At 1024x768, the authentication form is visible in the initial viewport without scrolling through a large brand panel.
7. At 390x844, the authentication form begins within the initial viewport and no authenticated shell content appears.
8. The brand area remains visibly Tamiyouz/TCRMMT and preserves the navy/gold enterprise identity.
9. `SUPER ADMIN ACCESS · OWNER ONLY` identity is visible.
10. The Login card is a single clear security surface without excessive outer whitespace.

## Interaction checks

- Show/Hide password toggles correctly and keeps aria state correct.
- Forgot password opens the existing recovery view.
- Back from recovery returns to Login.
- Synthetic invalid login only: error message is visible inside the initial viewport, not below the fold.
- Loading state: Sign In becomes disabled and shows the existing loading state.
- Keyboard Tab focus is clearly visible on fields, links/buttons and submit.
- Successful real authentication is not required unless authorized credentials are already available in the test environment; never expose credentials in the report.

## Dark mode

If the existing theme control can set dark mode, confirm the Login surface itself changes, including:

- Login main background
- Login card
- Inputs
- Borders
- Password toggle
- Text/secondary text
- Focus/contrast

Capture both Light and Dark at 1440x900 and 390x844.

## Authenticated regression spot check

After authentication only if an already-authorized test session is available, verify that the existing Super Admin shell still renders normally and the patch does not hide `#appShell` after `#loginView` receives `.hidden`.

## Required evidence

Return:

- Light 1440x900 screenshot
- Light 1024x768 screenshot
- Light 768x900 screenshot
- Light 390x844 screenshot
- Dark 1440x900 screenshot
- Dark 390x844 screenshot
- Invalid/error screenshot
- Measurement table with `innerWidth`, `clientWidth`, `scrollWidth`, overflow
- PASS/FAIL list for shell isolation, first-viewport form visibility, dark mode, focus, loading/error states, password toggle and recovery view
- `git diff --check`, `npm run check`, `npm run build` results

Do not Commit or Push from the target project.
