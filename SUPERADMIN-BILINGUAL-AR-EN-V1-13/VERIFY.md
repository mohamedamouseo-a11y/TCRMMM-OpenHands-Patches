# VERIFY — Super Admin Bilingual V1.13 Overview Mixed-Status Closure

## Scope
Apply only `apply_superadmin_bilingual_v1_13.py` to `/var/www/TCRMMT`.

## Hard rules
- No reset / clean / restore.
- No manual code edits.
- No commit / push.
- Only `server/superAdminUiPolish.ts` may be modified.
- Restart only `tamiyouz-crm`, and only after all static/build/dist checks pass.

## Apply
1. `git status --short`
2. Confirm marker `SUPER_ADMIN_BILINGUAL_AR_EN_V1_12_COMPANIES_EN_CLOSURE`.
3. Run `python3 apply_superadmin_bilingual_v1_13.py`.
4. Run it again; second run must be no-op.
5. `git diff --check`
6. `npm run check`
7. `npm run build`

## Dist gate
`dist/index.js` must contain:
- `SUPER_ADMIN_BILINGUAL_AR_EN_V1_13_OVERVIEW_MIXED_STATUS_CLOSURE`
- `SUPER_ADMIN_BILINGUAL_RUNTIME_V113`
- `/super-admin/bilingual-v113.js`
- `superadmin-bilingual-v113`

If any marker is missing: STOP before restart.

## Runtime
Restart only:
`pm2 restart tamiyouz-crm`

Check direct Node and public asset:
`/super-admin/bilingual-v113.js?v=superadmin-bilingual-v113`

Require HTTP 200, JavaScript content type, no-store headers, and marker `SUPER_ADMIN_BILINGUAL_RUNTIME_V113`.

## Browser gate
Fresh browser context, cache disabled.

Verify:
- default EN / LTR
- EN → AR → EN
- English persistence
- Arabic persistence

## Overview regression — must run before Companies
English Overview after >=2 seconds:
- Must NOT contain `Health N% · منتهي`.
- Specifically verify the executive tile renders `Health N% · expired`.
- Full Overview EN scan must return `NONE FOUND`.

Arabic Overview after >=2 seconds:
- Full Overview AR scan must return `NONE FOUND`.

If either Overview gate fails: STOP. Do not fix.

## Companies gate
Only after both Overview gates pass:
- Companies EN scan
- Companies AR scan

V1.12 targeted EN strings must all be clean, including:
- Shown
- Company filters
- Search & filters
- Find the company you need quickly.
- Company name, path, or email
- Created from / Created to
- Number of rows
- Clear filters
- Save view
- Status, Plan, health, and actions.
- Scroll horizontally when needed
- Path
- Health
- Remaining
- `Server-side pagination · N records`

If Companies EN or AR has ordinary untranslated static UI: STOP and report unique strings.

## Continue full audit only after Companies passes
Tenant Details, Users, Platform Admins, Activity, Audit Log, GitHub Sync, Evolution API, Tara APIs, Plans Catalog, Plan Editor, Company Overrides, Commercial, Billing, Subscriptions, Settings, Source Code — EN + AR.

## Acceptance strings
Report:
- `RUNTIME V113: PASS`
- `LANGUAGE CONTROL LIFECYCLE: PASS`
- `PERSISTENCE: PASS`
- `OVERVIEW EN STATIC UI: NONE FOUND`
- `OVERVIEW AR STATIC UI: NONE FOUND`
- `COMPANIES EN STATIC UI: NONE FOUND`
- `COMPANIES AR STATIC UI: NONE FOUND`
- `UNTRANSLATED STATIC UI: NONE FOUND`

On first failure: record exact text, page, language, selector/attribute, screenshot, then stop. No manual fix.
