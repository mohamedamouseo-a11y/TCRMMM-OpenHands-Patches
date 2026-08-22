# Super Admin Bilingual Arabic / English V1 — Verification

## Scope

Target project: `/var/www/TCRMMT`

Patch file: `apply_superadmin_bilingual_v1.py`

Expected modified project file only:

- `server/superAdminUiPolish.ts`

This patch adds a presentation/localization layer only. It must not change DB, APIs, authentication, permissions, routes, billing/subscription business logic, or existing Super Admin action handlers.

## Preflight

1. Run `git status --short` and preserve the current worktree.
2. Do not run `git reset`, `git clean`, or `git restore`.
3. Confirm the deployed project already contains the accepted Super Admin login/dashboard baseline.
4. Copy the patch files to a temporary directory outside the project worktree.
5. Run the patch exactly once:

```bash
python3 apply_superadmin_bilingual_v1.py
```

6. Confirm marker exists exactly once in `server/superAdminUiPolish.ts`:

`SUPER_ADMIN_BILINGUAL_AR_EN_V1`

## Static checks

Run:

```bash
git diff --check
npm run check
npm run build
```

All must pass before browser QA.

If they pass, restart `tamiyouz-crm` only.

## Core language acceptance

The Super Admin UI must support exactly two languages:

- English — `lang="en"`, `dir="ltr"`
- Arabic — `lang="ar"`, `dir="rtl"`

Verify:

1. A language switch is visible on the login screen.
2. A language switch is visible after login in the Super Admin topbar.
3. The floating UI dock also exposes the language toggle.
4. Switching language updates the existing page immediately without navigation/reload.
5. The selected language persists after browser refresh using localStorage key:
   `tcrm-super-admin-language`
6. English switches the main Super Admin shell to LTR.
7. Arabic switches the main Super Admin shell to RTL.
8. Email/password/URL-like inputs remain readable LTR where appropriate.
9. Switching language must not clear typed login values, filters, selected tabs, open drawer state, or current page.
10. Real company/user names, IDs, emails, domains, plan codes, GitHub refs and API values must NOT be translated.

## Translation coverage audit

Test both English and Arabic on every major surface:

- Super Admin Login
- Forgot Password / Reset Password UI
- Overview / Executive Command Center
- Companies
- Tenant Details + all tenant tabs
- Users
- Platform Admins
- Plans Catalog
- Plans Editor
- Company Overrides
- Commercial / Billing / Subscriptions
- Activity
- Audit Log
- GitHub Sync
- Evolution API
- Tara APIs
- System Settings
- Settings Drawer
- Account / Appearance / Source Code

For every surface verify translation of:

- Page titles
- Sidebar/navigation labels
- Buttons/actions
- Form labels
- Placeholders
- Tabs
- Table headings
- Status labels when they are UI vocabulary
- Empty/loading/error states
- Tooltips / title attributes
- aria-labels where visible through accessibility inspection
- Drawer headings
- Confirmation/action labels

### Important audit rule

Do not silently fix missing translations.

If any visible static UI label remains in the wrong language, record:

- page/surface
- element text
- selector or nearby ID/class
- expected Arabic or English wording
- screenshot

Dynamic tenant/company/user data is not a translation defect.

## Responsive QA

Use real Playwright/Chromium viewport contexts, not `window.resizeTo`.

Test both languages at:

- `1440x900`
- `1024x768`
- `768x900`
- `390x844`

At minimum capture:

1. Login English 1440
2. Login Arabic 1440
3. Overview English 1440
4. Overview Arabic 1440
5. Companies English 1024
6. Companies Arabic 1024
7. Overview Arabic 390
8. Settings Arabic 390
9. Settings English 390

For each viewport record:

- `window.innerWidth`
- `document.documentElement.clientWidth`
- `document.documentElement.scrollWidth`
- page-level horizontal overflow
- current `document.documentElement.lang`
- current `document.documentElement.dir`
- current `document.documentElement.dataset.saLang`
- stored `localStorage['tcrm-super-admin-language']`

Expected page-level content overflow: `0px`.

## RTL/LTR visual acceptance

Arabic:

- labels and normal content align naturally RTL
- sidebar/navigation order remains usable
- topbar controls remain visible
- tables do not clip
- drawers remain inside viewport
- buttons do not overlap

English:

- shell is LTR
- normal labels align naturally LTR
- no mirrored/clipped controls
- sidebar/navigation remains usable

Do not change business logic to solve visual direction problems.

## Functional regression spot-check

In both languages confirm:

- login works with the existing account (do not expose credentials in report)
- password show/hide
- forgot-password navigation
- sidebar navigation
- Companies open/detail drawer
- Users
- Plans
- Settings drawer
- theme toggle
- density toggle
- language persistence after refresh
- logout

Use safe/read-only actions where possible. Do not mutate production business data for QA.

## Deliverable

Return a ZIP containing:

- final report Markdown
- PASS/FAIL matrix per surface and language
- responsive measurement matrix
- screenshots
- a section named `UNTRANSLATED STATIC UI` listing every remaining wrong-language static label, or explicitly state `NONE FOUND`
- build/typecheck/diff-check results

Do not commit or push project changes.

If untranslated static labels or RTL/LTR layout defects are found, report them and stop. They will be handled by a separate corrective patch.
