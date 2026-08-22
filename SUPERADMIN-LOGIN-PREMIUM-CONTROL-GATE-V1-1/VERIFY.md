# Super Admin Login Premium Control Gate V1.1 — VERIFY

## Scope
Presentation-only corrective patch after real responsive QA of V1.

Fix only:
1. `1024x768` full sign-in task must fit inside the initial viewport, including `Sign In`.
2. Remove the perceived double-card / double-surface on tablet and mobile.
3. Make Dark Mode one coherent dark login surface.

Do not change Auth, API, DB, routes, permissions, handlers, password recovery logic, IDs, or business logic.

## Apply
Target: `/var/www/TCRMMT`

Before applying:
```bash
git status --short
```

Do not use Reset / Clean / Restore.

Apply exactly once:
```bash
python3 apply_login_premium_gate_v1_1.py
```

## Static checks
```bash
git diff --check
npm run check
npm run build
```

Only after all pass, restart `tamiyouz-crm`.

## Responsive acceptance
Use real Playwright/Chromium viewport contexts:

- 1440x900
- 1024x768
- 768x900
- 390x844

For every viewport record:
- `window.innerWidth`
- `document.documentElement.clientWidth`
- `document.documentElement.scrollWidth`
- page-level overflow
- login form/card top + bottom
- `#loginBtn` top + bottom

Required:
- page-level horizontal overflow = 0px
- `#appShell` remains hidden while unauthenticated
- no authenticated content visible
- no clipping/overlap
- form does not extend outside the viewport horizontally

### Critical 1024x768 gate
At `1024x768`:
- complete login form must fit in first viewport
- `#loginBtn` bottom must be <= 768
- no scroll required to reach Sign In
- error/status area must not push the primary task unusably below fold

### Mobile gate
At `390x844`:
- one visual login card/security surface only
- no blank outer card around the form
- card must stay fully inside viewport width
- Email, Password, Forgot Password, Sign In visible and usable

## Dark mode
At 1440x900 and 390x844 verify:
- login main background is dark
- login card/form surface is dark, not white
- headings/labels readable
- fields remain dark
- password toggle readable
- focus states visible
- error state readable

## Functional spot checks
Do not use real credentials.

Verify:
- Email input
- Password input
- Show/Hide password and ARIA state
- Forgot password view
- Back to Sign In
- Synthetic invalid login error
- Loading state
- Keyboard focus

## Evidence required
Screenshots:
1. Light 1440x900
2. Light 1024x768
3. Light 768x900
4. Light 390x844
5. Dark 1440x900
6. Dark 390x844
7. Invalid login error
8. Password recovery

Report a final PASS/FAIL matrix.

## Prohibited
- No manual code edits
- No Commit
- No Push
- No Auth/API/DB/Route/Permission/Business Logic changes
- Do not hide defects with page-level `overflow:hidden` / `overflow:clip`
