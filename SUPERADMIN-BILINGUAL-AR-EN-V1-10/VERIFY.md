# TCRMMT Super Admin Bilingual V1.10 — VERIFY

## Goal
Close the audited V1.9 **Overview English** untranslated static UI before expanding the final bilingual audit to the remaining Super Admin surfaces.

## Safety
- Target: `/var/www/TCRMMT`
- Do not reset, clean, restore, commit, or push.
- Do not modify DB, API, Auth, Routes, Permissions, Billing, Subscription, Business Logic, or navigation handlers.
- Manus must not hand-edit code. Apply the supplied patch only.
- Only `server/superAdminUiPolish.ts` may change.

## Pre-check
1. `git status --short`
2. Require markers:
   - `SUPER_ADMIN_BILINGUAL_AR_EN_V1_8_STANDALONE_RUNTIME`
   - `SUPER_ADMIN_BILINGUAL_AR_EN_V1_9_PHRASE_RUNTIME`
3. Confirm V1.10 marker is absent before first apply.

## Apply
Run:
`python3 apply_superadmin_bilingual_v1_10.py`

Run a second time and require an idempotent no-op.

## Static checks
Run:
- `git diff --check`
- `npm run check`
- `npm run build`

Before restart, require `dist/index.js` to contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_10_OVERVIEW_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V110`
- `/super-admin/bilingual-v110.js`
- `superadmin-bilingual-v110`

If any marker is missing: stop.

## Restart
Only after all static checks pass:
`pm2 restart tamiyouz-crm`

Require process online and unstable restarts = 0.

## Asset/runtime proof
Direct Node and public HTTPS must both serve:
`/super-admin/bilingual-v110.js?v=superadmin-bilingual-v110`

Require:
- HTTP 200
- JavaScript content type
- marker `SUPER_ADMIN_BILINGUAL_RUNTIME_V110`
- no-store cache headers

## Browser runtime gate
Fresh browser context, cache disabled, storage cleared.
Require:
- runtime = `SUPER_ADMIN_BILINGUAL_RUNTIME_V110`
- default `en/ltr`
- visible AR language control
- EN → AR → EN works
- English and Arabic refresh persistence both PASS

## Overview EN gate — FIRST
Authenticate, select English, wait at least 2 seconds, then scan:
- visible text nodes
- placeholder
- title
- aria-label

Exclude only real dynamic data:
- company/user names
- emails
- IPs
- IDs
- URLs
- slugs
- tokens
- repository/branch/commit
- raw technical identifiers

Specifically re-check all V1.9 findings including:
- sidebar identity/navigation/logout
- topbar subtitle and action aria-labels
- Overview KPI helper lines
- dynamic health/status/count lines
- Quick Decisions
- company filters/statuses
- Usage Analytics
- Security Review
- subscription/admin/settings drawers
- dark/light/source controls

The following dynamic patterns must be English:
- `Review <company>`
- `Health N% · expired`
- `N active of N`
- `N paid companies`
- `N suspended · N ending soon`
- `Users N% · Clients N% · <plan>`

Arabic-Indic digits in English UI should be normalized to ASCII digits.

If Overview EN has any ordinary Arabic static UI:
- do not fix it
- report UNIQUE exact strings with selector/attribute
- capture screenshot
- stop

## If Overview EN passes
Continue Overview AR, then full EN + AR audit for:
- Login
- Companies
- Tenant Details
- Users
- Platform Admins
- Activity
- Audit Log
- GitHub Sync
- Evolution API
- Tara APIs
- Plans Catalog
- Plan Editor
- Company Overrides
- Commercial
- Billing
- Subscriptions
- Settings
- Source Code

## Responsive
If translation gates pass, verify EN + AR:
- 1440x900
- 1024x768
- 768x900
- 390x844

Require no horizontal overflow, clipping, or overlap.

## Final report gate
Must state:
- `RUNTIME V110: PASS`
- `LANGUAGE CONTROL LIFECYCLE: PASS`
- `PERSISTENCE: PASS`
- `OVERVIEW EN STATIC UI: NONE FOUND`
- `UNTRANSLATED STATIC UI: NONE FOUND` only if the full audit actually completed cleanly.

If any gate fails, report evidence and stop. No manual fixes, no commit, no push.
